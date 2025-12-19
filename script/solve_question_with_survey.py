import json
import os
import glob
import time
import httpx
from dotenv import load_dotenv
from openai import OpenAI

# ================== 用户配置区域 ==================

TARGET_SURVEY_DIR_NAME = "x-ai_grok-deep_research"
JSON_FILE_PATH = "openai_batch_output.filtered.json"
OUTPUT_FILE_PATH = "survey_direct_compare_result_x-ai_grok-deep_research.json"  # 改个名，防止搞混

# 设置为 0 或 None 跑全量
TEST_LIMIT = 0

# ================== Prompt 模板 ==================
SOLVE_PROMPT_TEMPLATE = """
【参考综述】：
{survey_content}

【待解问题】：
{question_content}

【指令】：
只根据这份附件的综述回答问题，不要根据其他内容，比如不要根据网络搜索或者你数据库中已有的知识回答。认真的阅读这篇综述，对于综述中提到的每篇论文都进行细致的阅读和分析，然后做这道题。
如果没有对应选项则输出None
输出这道题的答案，格式严格按照"答案：X",不要输出任何理由。
"""

# ================== API 初始化 (直连模式) ==================

load_dotenv()
API_KEY = os.environ.get("API_KEY")
AHM_BASE_URL = "https://api.aihubmix.com/v1"
LLM_MODEL_NAME = "qwen2.5-7b-instruct"

if not API_KEY:
    print("❌ 错误：未找到 API_KEY")
    exit(1)

# 强制清空代理
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

def get_openai_completion(prompt_text: str) -> str:
    try:
        completion = client.chat.completions.create(
            model=LLM_MODEL_NAME,
            messages=[
                {"role": "system", "content": "你是一个严格的学术阅读理解助手。"},
                {"role": "user", "content": prompt_text},
            ],
            temperature=0.0,  # 这里的0很关键，保证输出稳定
        )
        return (completion.choices[0].message.content or "").strip()
    except Exception as e:
        print(f"  [API Error] {e}")
        return f"ERROR: {e}"


def solve_question_with_survey(question: str, survey_content: str) -> str:
    max_chars = 50000
    truncated_survey = survey_content[:max_chars]
    final_prompt = SOLVE_PROMPT_TEMPLATE.format(
        survey_content=truncated_survey,
        question_content=question
    )
    return get_openai_completion(final_prompt)


def get_file_id(filename: str) -> int:
    try:
        return int(filename.split('_')[0])
    except (ValueError, IndexError):
        return -1


# ================== 主程序 ==================

def main():
    survey_root = "survey"
    target_dir = os.path.join(survey_root, TARGET_SURVEY_DIR_NAME)

    # 1. 加载题目和答案
    if not os.path.exists(JSON_FILE_PATH):
        print(f"❌ 找不到 JSON: {JSON_FILE_PATH}")
        return

    print("📖 加载题目数据...")
    with open(JSON_FILE_PATH, "r", encoding="utf-8") as f:
        json_data = json.load(f)

    # 建立 ID -> Data 映射
    id_to_data_map = {}
    for item in json_data:
        try:
            pid = int(item.get("id"))
            # 确保你的 JSON 里也就是这两个字段
            question = item.get("question")
            answer = item.get("answer")

            if question:
                id_to_data_map[pid] = {
                    "question": question,
                    "answer": answer  # 这里比如是 "答案：D"
                }
        except (ValueError, TypeError):
            continue

    # 2. 遍历文件
    if not os.path.exists(target_dir):
        print(f"❌ 找不到文件夹: {target_dir}")
        return

    all_files = glob.glob(os.path.join(target_dir, "*.md"))
    all_files.sort(key=lambda x: get_file_id(os.path.basename(x)))

    process_files = all_files[:TEST_LIMIT] if (TEST_LIMIT and TEST_LIMIT > 0) else all_files

    current_results = []
    print("-" * 50)

    for file_path in process_files:
        file_name = os.path.basename(file_path)
        file_id = get_file_id(file_name)
        if file_id == -1: continue

        data_item = id_to_data_map.get(file_id)
        if not data_item:
            print(f"[ID: {file_id:02d}] ❌ 无对应题目数据")
            continue

        question_text = data_item["question"]
        ground_truth = data_item["answer"]  # 比如 "答案：D"

        print(f"[ID: {file_id:02d}] 正在解题... (GT: {ground_truth})")

        # 读文件
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                survey_content = f.read()
        except:
            continue

        # API 调用
        start_time = time.time()
        model_response = solve_question_with_survey(question_text, survey_content)
        elapsed = time.time() - start_time

        # === 修改后的判题逻辑：直接全等 ===
        # 仅做 strip() 处理去除首尾看不见的空格/换行
        if ground_truth:
            is_correct = (model_response.strip() == ground_truth.strip())
        else:
            is_correct = False  # 如果JSON里没答案，算错或跳过

        status_icon = "✅" if is_correct else "❌"
        # 打印时如果不一致，可以直观看到区别
        print(f"  -> {status_icon} | 耗时:{elapsed:.1f}s")
        print(f"     Model: {model_response.strip()}")
        print(f"     Truth: {ground_truth.strip()}")

        current_results.append({
            "id": file_id,
            "question": question_text,
            "survey_file": file_name,
            "ground_truth": ground_truth,
            "model_response": model_response,  # 记录原始回复
            "is_correct": is_correct
        })

        time.sleep(1)

    # 3. 增量保存
    print("-" * 50)
    existing_data = []
    if os.path.exists(OUTPUT_FILE_PATH):
        try:
            with open(OUTPUT_FILE_PATH, "r", encoding="utf-8") as f:
                existing_data = json.load(f)
        except:
            existing_data = []

    final_data = existing_data + current_results

    with open(OUTPUT_FILE_PATH, "w", encoding="utf-8") as f:
        json.dump(final_data, f, ensure_ascii=False, indent=2)

    # 简单统计
    correct_count = sum(1 for r in current_results if r['is_correct'])
    total = len(current_results)
    if total > 0:
        print(f"📊 本次正确率: {correct_count}/{total} ({correct_count / total * 100:.1f}%)")
    print(f"💾 结果保存至: {OUTPUT_FILE_PATH}")


if __name__ == "__main__":
    main()