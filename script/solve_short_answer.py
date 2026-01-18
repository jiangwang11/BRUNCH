import json
import os
import glob
import time
import httpx
import numpy as np
import jieba
import jieba.analyse
from dotenv import load_dotenv
from openai import OpenAI

# ================== 用户配置区域 ==================

# ... (保持不变)
TARGET_SURVEY_DIR_NAME = "perplexity_sonar-deep-research"
INPUT_JSON_PATH = "short_answer.json"
OUTPUT_FILE_PATH = "survey_scenario_similarity_result.json"
START_INDEX = 0
END_INDEX = 5

GEN_MODEL_NAME = "qwen2.5-7b-instruct"
EMBED_MODEL_NAME = "text-embedding-3-small"

# 【新增配置】混合评分权重
# 语义向量占 70%，关键词重合度占 30%
# 调高 KEYWORD_WEIGHT 可以让分数对“专有名词”更敏感
SEMANTIC_WEIGHT = 0.3
KEYWORD_WEIGHT = 0.7

# ================== Prompt 模板 (保持不变) ==================
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

# ================== API 初始化 (保持不变) ==================
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
    client = OpenAI(api_key=API_KEY, base_url=AHM_BASE_URL, http_client=http_client)
except Exception as e:
    print(f"❌ Client Init Error: {e}")
    exit(1)


# ================== 核心函数 ==================

def get_qwen_generation(prompt_text: str) -> str:
    # ... (保持不变)
    try:
        completion = client.chat.completions.create(
            model=GEN_MODEL_NAME,
            messages=[
                {"role": "system", "content": "你是一个专业的学术总结助手。"},
                {"role": "user", "content": prompt_text},
            ],
            temperature=0.0,
        )
        return (completion.choices[0].message.content or "").strip()
    except Exception as e:
        print(f"  [Gen Error] {e}")
        return ""


def get_embedding(text: str):
    # ... (保持不变)
    try:
        text = text.replace("\n", " ")
        response = client.embeddings.create(
            input=[text],
            model=EMBED_MODEL_NAME
        )
        return response.data[0].embedding
    except Exception as e:
        print(f"  [Embed Error] {e}")
        return None


def compute_cosine_similarity(vec_a, vec_b):
    # ... (保持不变)
    if vec_a is None or vec_b is None:
        return 0.0
    a = np.array(vec_a)
    b = np.array(vec_b)
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return float(np.dot(a, b) / (norm_a * norm_b))


# 【新增函数】提取关键词并计算 Jaccard 相似度
# ================== 替换：基于 IDF 权重的关键词召回计算 ==================

def compute_keyword_similarity(gen_text, truth_text, top_k=20):
    """
    计算【加权关键词召回率】。
    不再只看重合词的数量，而是看重合词的"含金量"(IDF权重)。

    Args:
        gen_text: 模型生成的文本
        truth_text: 标准答案(Ground Truth)
    """
    if not gen_text or not truth_text:
        return 0.0, [], []

    # 1. 提取标准答案的关键词 + 权重 (withWeight=True)
    # 使用 extract_tags (基于TF-IDF)，因为它能给出词的权重
    try:
        truth_tags = jieba.analyse.extract_tags(truth_text, topK=top_k, withWeight=True)
        # truth_tags 是一个列表: [('旅鼠', 1.5), ('算法', 0.8), ...]
    except Exception:
        return 0.0, [], []

    if not truth_tags:
        return 0.0, [], []

    # 2. 提取生成文本的关键词 (只需要词，不需要权重)
    # 这里我们放宽一点，只要生成文本里出现了这个词就行
    gen_words = set(jieba.cut(gen_text))

    # 3. 计算得分
    total_weight = 0.0
    hit_weight = 0.0
    hit_words = []

    for word, weight in truth_tags:
        total_weight += weight
        if word in gen_words:
            hit_weight += weight
            hit_words.append(word)

    if total_weight == 0:
        return 0.0, [], []

    # 4. 核心差异：这是一个"召回率"分数，而不是相似度
    # 意味着：你必须涵盖标准答案里的核心概念，废话再多也没分
    weighted_score = hit_weight / total_weight

    # 返回格式保持一致：分数, 命中的词, 标准答案的词(仅用于打印)
    truth_words_list = [t[0] for t in truth_tags]
    return weighted_score, hit_words, truth_words_list


def get_file_id(filename: str) -> int:
    try:
        return int(filename.split('_')[0])
    except (ValueError, IndexError):
        return -1


# ================== 主程序 ==================

def main():
    survey_root = "survey"
    target_dir = os.path.join(survey_root, TARGET_SURVEY_DIR_NAME)

    if not os.path.exists(INPUT_JSON_PATH):
        print(f"❌ 找不到输入文件: {INPUT_JSON_PATH}")
        return

    print("📖 正在加载题目数据...")
    with open(INPUT_JSON_PATH, "r", encoding="utf-8") as f:
        json_data = json.load(f)

    json_data.sort(key=lambda x: x.get('id', 0))

    if END_INDEX is not None:
        target_questions = json_data[START_INDEX:END_INDEX]
    else:
        target_questions = json_data[START_INDEX:]

    print(f"🎯 计划处理范围: {START_INDEX} -> {END_INDEX} (共 {len(target_questions)} 题)")

    if not os.path.exists(target_dir):
        print(f"❌ 找不到 Survey 文件夹: {target_dir}")
        return

    id_to_filepath = {}
    all_files = glob.glob(os.path.join(target_dir, "*.md"))
    for fpath in all_files:
        fid = get_file_id(os.path.basename(fpath))
        if fid != -1:
            id_to_filepath[fid] = fpath

    results = []

    print("-" * 60)
    print(f"🚀 开始执行 | 混合评分: Vec({SEMANTIC_WEIGHT}) + Key({KEYWORD_WEIGHT})")
    print("-" * 60)

    for item in target_questions:
        pid = item.get("id")
        method_input = item.get("method")
        scenario_truth = item.get("scenario")

        if not (pid and method_input and scenario_truth):
            continue

        survey_path = id_to_filepath.get(pid)
        if not survey_path:
            print(f"[ID: {pid:03d}] ⚠️ 无 Survey (跳过)")
            continue

        survey_filename = os.path.basename(survey_path)
        print(f"[ID: {pid:03d}] 处理中...")

        try:
            with open(survey_path, "r", encoding="utf-8") as f:
                survey_content = f.read()
        except:
            continue

        truncated_survey = survey_content[:30000]

        # Step 1: 生成
        gen_prompt = SCENARIO_GEN_PROMPT.format(
            survey_content=truncated_survey,
            method_desc=method_input
        )
        start_time = time.time()
        generated_scenario = get_qwen_generation(gen_prompt)
        duration = time.time() - start_time

        if not generated_scenario:
            continue

        # Step 2: 向量相似度 (Semantic)
        vec_gen = get_embedding(generated_scenario)
        vec_truth = get_embedding(scenario_truth)
        cosine_score = compute_cosine_similarity(vec_gen, vec_truth)

        # Step 3: 关键词相似度 (Keyword)
        keyword_score, kw_gen, kw_truth = compute_keyword_similarity(generated_scenario, scenario_truth)

        if keyword_score < 0.3:
            # 惩罚系数：如果关键词都没抓对，Embedding 再高也打 5 折
            penalty_factor = 0.5
        else:
            penalty_factor = 1.0

        # Step 4: 混合得分
        hybrid_score = (cosine_score * SEMANTIC_WEIGHT * penalty_factor) + (keyword_score * KEYWORD_WEIGHT)

        # 打印状态
        # Jaccard分数通常比较低(0.2-0.5就很好了)，所以hybrid_score会比纯cosine低，这是正常的，拉开了差距
        score_icon = "🟢" if hybrid_score > 0.6 else ("🟡" if hybrid_score > 0.4 else "🔴")

        print(f"  -> 耗时: {duration:.1f}s")
        print(
            f"     [Vec]: {cosine_score:.4f} | [Key]: {keyword_score:.4f} | [Hybrid]: {hybrid_score:.4f} {score_icon}")
        # print(f"     关键词重合: {set(kw_gen) & set(kw_truth)}") # 调试用

        results.append({
            "id": pid,
            "survey_file": survey_filename,
            "method_prompted": method_input,
            "ground_truth_scenario": scenario_truth,
            "generated_scenario": generated_scenario,
            "cosine_score": cosine_score,
            "keyword_score": keyword_score,
            "hybrid_score": hybrid_score
        })

        time.sleep(0.5)

    print("-" * 60)
    if results:
        with open(OUTPUT_FILE_PATH, "w", encoding="utf-8") as f:
            json.dump(results, f, ensure_ascii=False, indent=2)

        avg_hybrid = sum(r["hybrid_score"] for r in results) / len(results)
        print(f"📊 平均混合得分: {avg_hybrid:.4f}")
        print(f"💾 结果已保存至: {OUTPUT_FILE_PATH}")


if __name__ == "__main__":
    main()