import json
import os
import glob
import time
import httpx
import re
import numpy as np
import jieba
import jieba.analyse
from dotenv import load_dotenv
from openai import OpenAI

# ================== 用户配置区域 ==================

TARGET_SURVEY_DIR_NAME = "x-ai_grok-deep_research"
INPUT_JSON_PATH = "short_answer.json"
OUTPUT_FILE_PATH = "survey_short_answer_result_x-ai_grok-deep_research.json"  # 改名体现新策略

START_INDEX = 0
END_INDEX = 20

GEN_MODEL_NAME = "qwen2.5-14b-instruct"
EMBED_MODEL_NAME = "text-embedding-3-small"

# --- 评分权重 ---
# 区分度分数(Discriminative) 是最核心的指标，权重给高
WEIGHT_LLM = 0.4
WEIGHT_KEYWORD = 0.2
WEIGHT_DISCRIMINATIVE = 0.4

# ================== Prompt (保持不变) ==================
SCENARIO_GEN_PROMPT = """
【参考综述】：
{survey_content}

【任务】：
用准确的一个段落的语言描述以下方法的适用场景：
{method_desc}

【指令】：
1. 只根据这份附件的综述回答问题，不要根据其他内容，并且直接描述适合的场景，不要重复方法的原文。
2. 描述该方法最适合解决什么问题、在什么数据集或输入条件下表现最好，要描述问题的类型，如“连续的、无梯度或非凸工程优化问题”，而非描述具体的场景，如“电力系统调度”。
3. 输出格式要求：直接输出200~300字的描述段落，不要包含"适用场景是..."等前缀，不要分点。
"""

JUDGE_PROMPT_TEMPLATE = """
你是一个严格的学术阅卷专家。请对比【标准答案】和【考生回答】，根据评分标准进行打分。

【标准答案 (Ground Truth)】：
{truth}

【考生回答 (Generated)】：
{gen}

【评分标准 (0-10分)】：
- 0-3分：通用废话，或回答了无关内容。如果你觉得这个回答放在其他题目下也能得分，请务必打低分。
- 4-6分：沾边，提到了相关领域，但缺乏该方法独有的特征（如特定的约束条件、特定的数据类型）。
- 7-8分：核心逻辑正确，能区分出该方法与其他类似方法的不同。
- 9-10分：完美匹配，精准描述了该方法的“指纹特征”。

【输出格式】：
只输出一个整数分数（0到10之间），不要输出任何理由。
"""

# ================== API 初始化 ==================
load_dotenv()
API_KEY = os.environ.get("API_KEY")
AHM_BASE_URL = "https://api.aihubmix.com/v1"

if not API_KEY:
    print("❌ 错误：未找到 API_KEY")
    exit(1)

os.environ["http_proxy"] = ""
os.environ["https_proxy"] = ""
os.environ["all_proxy"] = ""

try:
    http_client = httpx.Client(trust_env=False, timeout=300.0)
    client = OpenAI(
        api_key=API_KEY,
        base_url=AHM_BASE_URL,
        http_client=http_client,
    )
except Exception as e:
    print(f"❌ Client Init Error: {e}")
    exit(1)


# ================== 核心函数 ==================

def get_model_response(prompt_text: str, temperature=0.0) -> str:
    try:
        completion = client.chat.completions.create(
            model=GEN_MODEL_NAME,
            messages=[
                {"role": "system", "content": "你是一个专业的学术助手。"},
                {"role": "user", "content": prompt_text},
            ],
            temperature=temperature,
        )
        return (completion.choices[0].message.content or "").strip()
    except Exception as e:
        print(f"  [API Error] {e}")
        return ""


def get_llm_judge_score(generated_text, truth_text):
    if not generated_text: return 0
    prompt = JUDGE_PROMPT_TEMPLATE.format(truth=truth_text, gen=generated_text)
    score_str = get_model_response(prompt, temperature=0.0)
    try:
        match = re.search(r'\d+', score_str)
        if match:
            return max(0, min(10, int(match.group())))
        return 0
    except:
        return 0


def get_embedding(text: str):
    try:
        text = text.replace("\n", " ")
        response = client.embeddings.create(input=[text], model=EMBED_MODEL_NAME)
        return response.data[0].embedding
    except:
        return None


def compute_cosine_similarity(vec_a, vec_b):
    if vec_a is None or vec_b is None: return 0.0
    a = np.array(vec_a)
    b = np.array(vec_b)
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)
    if norm_a == 0 or norm_b == 0: return 0.0
    return float(np.dot(a, b) / (norm_a * norm_b))


def compute_keyword_similarity(gen_text, truth_text, top_k=20):
    if not gen_text or not truth_text: return 0.0
    try:
        truth_tags = jieba.analyse.extract_tags(truth_text, topK=top_k, withWeight=True)
    except:
        return 0.0
    if not truth_tags: return 0.0

    gen_words = set(jieba.cut(gen_text))
    total_weight = 0.0
    hit_weight = 0.0
    for word, weight in truth_tags:
        total_weight += weight
        if word in gen_words: hit_weight += weight

    return hit_weight / total_weight if total_weight > 0 else 0.0


def get_file_id(filename: str) -> int:
    try:
        return int(filename.split('_')[0])
    except:
        return -1


# ================== 主程序 ==================

# ... (前面的 import 和 函数定义 保持不变)

def main():
    survey_root = "survey"
    target_dir = os.path.join(survey_root, TARGET_SURVEY_DIR_NAME)

    # 1. 加载数据
    if not os.path.exists(INPUT_JSON_PATH):
        print("❌ 找不到输入文件")
        return

    with open(INPUT_JSON_PATH, "r", encoding="utf-8") as f:
        json_data = json.load(f)

    json_data.sort(key=lambda x: x.get('id', 0))
    if END_INDEX is not None:
        target_questions = json_data[START_INDEX:END_INDEX]
    else:
        target_questions = json_data[START_INDEX:]

    # 2. 索引 Survey 文件
    if not os.path.exists(target_dir):
        print(f"❌ 找不到 Survey 文件夹: {target_dir}")
        return
    id_to_filepath = {}
    for fpath in glob.glob(os.path.join(target_dir, "*.md")):
        fid = get_file_id(os.path.basename(fpath))
        if fid != -1: id_to_filepath[fid] = fpath

    # 3. 预构建向量库
    print("🧠 正在预计算 Ground Truth 向量库...")
    truth_embeddings_db = []
    for item in target_questions:
        pid = item.get("id")
        truth = item.get("scenario")
        if pid and truth:
            vec = get_embedding(truth)
            if vec:
                truth_embeddings_db.append({"id": pid, "vec": vec})

    results = []
    print("-" * 60)
    print(f"🚀 开始残酷评测 (Hard Mode)")
    print("-" * 60)

    for item in target_questions:
        pid = item.get("id")
        method_input = item.get("method")
        scenario_truth = item.get("scenario")

        if not (pid and method_input and scenario_truth): continue
        survey_path = id_to_filepath.get(pid)
        if not survey_path: continue

        current_truth_vec = next((x['vec'] for x in truth_embeddings_db if x['id'] == pid), None)
        if not current_truth_vec: continue

        # 读取 Survey
        try:
            with open(survey_path, "r", encoding="utf-8") as f:
                survey_content = f.read()[:30000]
        except:
            continue

        # 生成
        gen_prompt = SCENARIO_GEN_PROMPT.format(survey_content=survey_content, method_desc=method_input)
        start_time = time.time()
        generated_scenario = get_model_response(gen_prompt)
        duration = time.time() - start_time

        if not generated_scenario: continue

        # =========================================================
        # 【核心修改：残酷算分逻辑】
        # =========================================================

        # 1. 基础指标
        vec_gen = get_embedding(generated_scenario)

        # LLM 打分 (0-10)
        llm_score = get_llm_judge_score(generated_scenario, scenario_truth)
        llm_norm = llm_score / 10.0

        # 关键词召回 (0.0 - 1.0)
        keyword_score = compute_keyword_similarity(generated_scenario, scenario_truth)

        # 2. 区分度 (Max-Margin Discriminative Score)
        positive_sim = compute_cosine_similarity(vec_gen, current_truth_vec)

        negative_sims = []
        for db_item in truth_embeddings_db:
            if db_item['id'] != pid:
                sim = compute_cosine_similarity(vec_gen, db_item['vec'])
                negative_sims.append(sim)

        # 【关键点A】：不再取平均值，而是取最大值 (Hard Negative Mining)
        # 意思：你最像的那个错误答案，相似度是多少？
        max_negative_sim = max(negative_sims) if negative_sims else 0.0

        # 原始差异
        raw_diff = positive_sim - max_negative_sim

        # 【关键点B】：非线性映射 (Sigmoid-like)
        # 如果 raw_diff < 0.05 (几乎无法区分)，得分趋近于 0
        # 如果 raw_diff > 0.2 (区分明显)，得分趋近于 1
        # 这样会把拥挤在 0.1 左右的分数强行拉开
        try:
            # 缩放系数 15 控制曲线陡峭程度，偏移量 0.1 控制中心点
            disc_score = 1 / (1 + np.exp(-15 * (raw_diff - 0.1)))
        except:
            disc_score = 0.0

        # 3. 熔断机制 (Gating)
        penalty_multiplier = 1.0
        penalty_reasons = []

        # 熔断1：关键词缺失
        if keyword_score < 0.25:
            penalty_multiplier *= 0.4
            penalty_reasons.append("Keys丢失")

        # 熔断2：看起来比正确答案更像错误答案
        if raw_diff < 0:
            penalty_multiplier *= 0.5
            penalty_reasons.append("严重混淆")

        # 熔断3：LLM 觉得完全是幻觉
        if llm_score <= 2:
            penalty_multiplier *= 0.0  # 直接归零
            penalty_reasons.append("LLM判废")

        # 4. 最终合成
        # 权重：区分度(0.5) > LLM(0.3) > 关键词(0.2)
        base_score = (disc_score * 0.5) + (llm_norm * 0.3) + (keyword_score * 0.2)
        final_score = base_score * penalty_multiplier

        # 打印诊断
        icon = "🔴"
        if final_score > 0.4: icon = "🟡"
        if final_score > 0.7: icon = "🟢"

        print(f"[ID:{pid}] {duration:.1f}s | {icon}")
        print(f"  > 正例相似: {positive_sim:.4f}")
        print(f"  > 最强负例: {max_negative_sim:.4f} (Avg was {sum(negative_sims) / len(negative_sims):.2f})")
        print(f"  > 净差值(Diff): {raw_diff:.4f} -> 映射分: {disc_score:.4f}")
        print(f"  > [LLM]:{llm_score} | [Key]:{keyword_score:.2f}")
        if penalty_reasons:
            print(f"  > ⚠️ 触发熔断: {', '.join(penalty_reasons)}")
        print(f"  > [FINAL]: {final_score:.4f}")
        print("  ---")

        results.append({
            "id": pid,
            "scores": {
                "final": final_score,
                "components": {
                    "llm": llm_score,
                    "keyword": keyword_score,
                    "pos_sim": positive_sim,
                    "max_neg_sim": max_negative_sim,
                    "disc_mapped": disc_score
                },
                "penalties": penalty_reasons
            }
        })
        time.sleep(0.5)

    if results:
        with open(OUTPUT_FILE_PATH, "w", encoding="utf-8") as f:
            json.dump(results, f, ensure_ascii=False, indent=2)

        # 计算统计特征
        scores = [r["scores"]["final"] for r in results]
        avg = sum(scores) / len(scores)
        std_dev = np.std(scores)
        print(f"\n📊 统计结果:")
        print(f"平均分: {avg:.4f}")
        print(f"标准差: {std_dev:.4f} (越大说明区分度越好)")


if __name__ == "__main__":
    main()
