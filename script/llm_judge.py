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

# 1. 定义待评测的模型列表
CANDIDATE_MODELS = [
    "qwen2.5-7b-instruct",
    "qwen2.5-32b-instruct",
    "llama3.1-8b",
    "gemma-3-4b-it",
    "gpt-4.1-nano"
]

# 2. 定义待评测的数据集目录列表
CANDIDATE_SURVEY_DIRS = [
    "alibaba_tongyi-deepresearch-30b-a3b",
    "google_deep_research",
    "google_gemini-2.5-flash_online",
    "google_gemini-2.5-pro_online",
    "openai_gpt-5-mini",
    "openai_o4-mini-deep-research",
    "perplexity_sonar-deep-research",
    "qwen_qwen3-max_online",
    "x-ai_grok-deep_research"
]

# 全局变量占位符 (会被循环动态修改)
GEN_MODEL_NAME = ""
TARGET_SURVEY_DIR_NAME = ""
OUTPUT_FILE_PATH = ""

INPUT_JSON_PATH = "short_answer.json"
FINAL_RESULT_PATH = "final_result.json"  # 最终汇总文件

START_INDEX = 0
END_INDEX = 20
EMBED_MODEL_NAME = "text-embedding-3-small"

# --- 评分权重 ---
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


# ================== 封装评测逻辑 ==================

def evaluate_one_round(current_model, current_survey_dir, truth_embeddings_db, target_questions):
    """
    运行单轮评测
    :return: 本轮的平均分 (float)
    """
    # 更新全局配置，以便 get_model_response 等函数调用
    global GEN_MODEL_NAME, TARGET_SURVEY_DIR_NAME, OUTPUT_FILE_PATH

    GEN_MODEL_NAME = current_model
    TARGET_SURVEY_DIR_NAME = current_survey_dir
    # 动态生成输出文件名
    OUTPUT_FILE_PATH = f"survey_short_answer_result_{current_survey_dir}.json"

    print(f"\n{'=' * 80}")
    print(f"🎬 开始评测任务")
    print(f"🤖 模型: {GEN_MODEL_NAME}")
    print(f"📂 目录: {TARGET_SURVEY_DIR_NAME}")
    print(f"💾 输出: {OUTPUT_FILE_PATH}")
    print(f"{'=' * 80}\n")

    survey_root = "survey"
    target_dir = os.path.join(survey_root, TARGET_SURVEY_DIR_NAME)

    # 索引 Survey 文件
    if not os.path.exists(target_dir):
        print(f"❌ 找不到 Survey 文件夹: {target_dir}，跳过此轮")
        return 0.0

    id_to_filepath = {}
    for fpath in glob.glob(os.path.join(target_dir, "*.md")):
        fid = get_file_id(os.path.basename(fpath))
        if fid != -1: id_to_filepath[fid] = fpath

    results = []

    # 遍历问题进行评测
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

        # 调用模型 (注意：get_model_response 内部使用了全局 GEN_MODEL_NAME)
        generated_scenario = get_model_response(gen_prompt)
        duration = time.time() - start_time

        if not generated_scenario: continue

        # --- 评分逻辑 (与原代码保持一致) ---
        vec_gen = get_embedding(generated_scenario)
        llm_score = get_llm_judge_score(generated_scenario, scenario_truth)
        llm_norm = llm_score / 10.0
        keyword_score = compute_keyword_similarity(generated_scenario, scenario_truth)

        positive_sim = compute_cosine_similarity(vec_gen, current_truth_vec)
        negative_sims = []
        for db_item in truth_embeddings_db:
            if db_item['id'] != pid:
                sim = compute_cosine_similarity(vec_gen, db_item['vec'])
                negative_sims.append(sim)

        max_negative_sim = max(negative_sims) if negative_sims else 0.0
        raw_diff = positive_sim - max_negative_sim
        try:
            disc_score = 1 / (1 + np.exp(-15 * (raw_diff - 0.1)))
        except:
            disc_score = 0.0

        penalty_multiplier = 1.0
        penalty_reasons = []
        if keyword_score < 0.25:
            penalty_multiplier *= 0.4
            penalty_reasons.append("Keys丢失")
        if raw_diff < 0:
            penalty_multiplier *= 0.5
            penalty_reasons.append("严重混淆")
        if llm_score <= 2:
            penalty_multiplier *= 0.0
            penalty_reasons.append("LLM判废")

        base_score = (disc_score * 0.5) + (llm_norm * 0.3) + (keyword_score * 0.2)
        final_score = base_score * penalty_multiplier

        print(f"[ID:{pid}] {duration:.1f}s | Score: {final_score:.4f}")

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
        # time.sleep(0.5) # 可选：减少等待时间

    # 保存单轮详细结果
    if results:
        with open(OUTPUT_FILE_PATH, "w", encoding="utf-8") as f:
            json.dump(results, f, ensure_ascii=False, indent=2)

        scores = [r["scores"]["final"] for r in results]
        avg = sum(scores) / len(scores)
        print(f"✅ 完成本轮评测。平均分: {avg:.4f}")
        return avg
    else:
        print("⚠️ 本轮无有效结果")
        return 0.0


# ================== 主程序入口 ==================

def main():
    # 1. 加载基础数据 (只加载一次)
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

    # 2. 预构建 Ground Truth 向量库 (只构建一次，节省时间和Token)
    print("🧠 正在预计算 Ground Truth 向量库 (全局共用)...")
    truth_embeddings_db = []
    for item in target_questions:
        pid = item.get("id")
        truth = item.get("scenario")
        if pid and truth:
            vec = get_embedding(truth)
            if vec:
                truth_embeddings_db.append({"id": pid, "vec": vec})

    # 3. 初始化汇总列表
    final_summary_data = []

    # 4. 双重循环
    total_tasks = len(CANDIDATE_MODELS) * len(CANDIDATE_SURVEY_DIRS)
    current_task_idx = 0

    for model_name in CANDIDATE_MODELS:
        for survey_dir in CANDIDATE_SURVEY_DIRS:
            current_task_idx += 1
            print(f"\n>>> 进度: {current_task_idx}/{total_tasks}")

            # 执行单次评测
            avg_score = evaluate_one_round(
                current_model=model_name,
                current_survey_dir=survey_dir,
                truth_embeddings_db=truth_embeddings_db,
                target_questions=target_questions
            )

            # 记录结果
            record = {
                "gen_model": model_name,
                "target_survey_dir": survey_dir,
                "average_score": avg_score,
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
            }
            final_summary_data.append(record)

            # 实时保存汇总文件 (防止中途崩溃数据丢失)
            try:
                with open(FINAL_RESULT_PATH, "w", encoding="utf-8") as f:
                    json.dump(final_summary_data, f, ensure_ascii=False, indent=2)
                print(f"📋 汇总数据已更新至: {FINAL_RESULT_PATH}")
            except Exception as e:
                print(f"❌ 保存汇总文件失败: {e}")

    print("\n🎉 所有评测任务已完成！")


if __name__ == "__main__":
    main()