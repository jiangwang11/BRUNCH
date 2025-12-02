import json
import time
import os
import glob
import re
from dotenv import load_dotenv
from openai import OpenAI, RateLimitError, APIConnectionError, APIStatusError
from openai.types.chat import (
    ChatCompletionMessageParam,
    ChatCompletionSystemMessageParam,
    ChatCompletionUserMessageParam,
)

# ================== 基础配置 ==================

load_dotenv()

# 批量处理数量设置 (设置为 9999 则处理所有)
NUM_TO_PROCESS = 2

API_KEY = os.environ.get("API_KEY")
if not API_KEY:
    print("错误：未找到 API_KEY 环境变量。")
    exit(1)

AHM_BASE_URL = "https://api.aihubmix.com/v1"
MODEL_NAME = "gpt-5-mini"

# 初始化客户端
try:
    client = OpenAI(
        api_key=API_KEY,
        base_url=AHM_BASE_URL,
        default_headers={
            "User-Agent": "openai-python",
            "OpenAI-Client-User-Agent": '{"lang":"python"}'
        },
    )
except Exception as e:
    print(f"错误: 无法初始化 OpenAI 客户端。 {e}")
    exit(1)

# ================== Prompt 模板 ==================

SOLVE_PROMPT_TEMPLATE = """
【参考综述】：
{survey_content}

【待解问题】：
{question_content}

【指令】：
只根据这份附件的综述回答问题，不要根据其他内容，比如不要根据网络搜索或者你数据库中已有的知识回答。认真的阅读这篇综述，对于综述中提到的每篇论文都进行细致的阅读和分析，然后做这道题。
如果没有对应选项则输出None
输出这道题的答案，格式严格按照”答案：X“。
"""


# ================== 工具函数 ==================

def get_openai_completion(prompt_text):
    messages: list[ChatCompletionMessageParam] = [
        ChatCompletionSystemMessageParam(role="system", content="你是一个善于结合文献进行逻辑推理的科研专家。"),
        ChatCompletionUserMessageParam(role="user", content=prompt_text),
    ]

    try:
        completion = client.chat.completions.create(
            model=MODEL_NAME,
            messages=messages,
            temperature=0.3
        )
        generated_content = completion.choices[0].message.content

        if isinstance(generated_content, list):
            text_parts = []
            for part in generated_content:
                if isinstance(part, dict) and part.get("type") == "text":
                    text_parts.append(part.get("text", ""))
            return "".join(text_parts).strip()
        else:
            return (generated_content or "").strip()

    except Exception as e:
        print(f"[API Error] {e}")
        return f"Error: {e}"


def find_survey_by_id(survey_dir, target_id):
    """
    在 surveys 文件夹中寻找以 "target_id_" (例如 "01_") 开头的文件
    """
    pattern = os.path.join(survey_dir, f"{target_id:02d}_*.md")
    files = glob.glob(pattern)
    if files:
        return files[0]
    return None


def extract_option_letter(text):
    """
    核心提取逻辑：从文本中提取选项字母 (A, B, C, D, E...)
    支持格式包括但不限于:
    - "答案：A" (您的标准格式)
    - "Answer: A"
    - "答案是：A"
    - "A"
    """
    if not text:
        return None

    # 1. 优先匹配标准的 "答案：X" 或 "Answer: X" 格式 (支持中英文冒号)
    # search 会在字符串的任意位置查找匹配
    match = re.search(r"(?:答案|Answer|Result)\s*[:：是]\s*([A-E])", text, re.IGNORECASE)
    if match:
        return match.group(1).upper()

    # 2. 如果上面没匹配到，尝试查找行首或行尾的 "X"
    # 比如内容就是简单的 "A" 或者 "A."
    text = text.strip()

    # 如果整个字符串就是一个字母 A-E (可能带有句号)
    clean_text = text.replace(".", "").strip()
    if len(clean_text) == 1 and clean_text.upper() in "ABCDE":
        return clean_text.upper()

    return None


# ================== 主逻辑 ==================

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))

    fields_file = os.path.join(script_dir, "paper_fields_output.json")
    questions_file = os.path.join(script_dir, "openai_batch_output.filtered.json")
    output_file = os.path.join(script_dir, "exam_results_final.json")

    print(f"\n>>> 工作目录信息:")
    print(f"脚本目录: {script_dir}")
    print(f"字段文件: {fields_file}")
    print(f"题目文件: {questions_file}")
    print(f"结果输出: {output_file}\n")

    # 1. 读取题目数据
    if not os.path.exists(questions_file):
        print(f"错误: 找不到题目文件 {questions_file}")
        return

    try:
        with open(questions_file, "r", encoding="utf-8") as f:
            questions_data = json.load(f)
    except Exception as e:
        print(f"读取题目 JSON 失败: {e}")
        return

    if not questions_data:
        print("题目数据为空。")
        return

    try:
        with open(fields_file, "r", encoding="utf-8") as f:
            fields_data = json.load(f)
    except Exception as e:
        print(f"读取字段 JSON 失败: {e}")
        return

    fields_map = {item.get("id"): item for item in (fields_data or [])}

    results = []
    total_questions = len(questions_data)

    print(f"--- 开始处理 (计划处理前 {NUM_TO_PROCESS} 条) ---")

    # 2. 循环处理每一题
    for i, item in enumerate(questions_data):
        # 批量控制
        if i >= NUM_TO_PROCESS:
            print(f"\n>>> 已达到设定处理数量 ({NUM_TO_PROCESS})，停止处理。")
            break

        q_id = item.get("id")
        question_text = item.get("question")
        # 这里获取的就是 json 中的原始答案字符串，例如 "答案：A"
        ground_truth_full = item.get("answer", "")

        print(f"\n--- [题目 ID: {q_id}] ---")

        if not question_text:
            print("跳过: 题目内容为空")
            continue

        # 3. 通过字段文件获取综述路径
        field_info = fields_map.get(q_id) or {}
        survey_path = field_info.get("md_path")

        if not survey_path or not os.path.exists(survey_path):
            print(f"警告: 未找到 ID {q_id:02d} 的综述路径或文件不存在，跳过。")
            results.append({
                "id": q_id,
                "error": "Survey path missing",
                "is_correct": False
            })
            continue

        print(f"已加载综述: {os.path.basename(survey_path)}")

        try:
            with open(survey_path, "r", encoding="utf-8") as f:
                survey_content = f.read()
        except Exception as e:
            print(f"读取综述文件失败: {e}")
            continue

        # 4. 构建 Prompt 并调用
        final_prompt = SOLVE_PROMPT_TEMPLATE.format(
            survey_content=survey_content,
            question_content=question_text
        )

        print("正在解题...")
        model_response = get_openai_completion(final_prompt)
        print(f">>> 模型回答: {model_response}")
        print(f">>> 标准答案(原始): {ground_truth_full}")

        # 5. 结果比对逻辑

        # 从模型回答中提取 'A', 'B', 'C'...
        model_choice = extract_option_letter(model_response)

        # 关键点：同时也从题目文件的标准答案中提取 'A', 'B', 'C'...
        # 这样即使标准答案是 "答案：A"，也会被 extract_option_letter 变成 "A"
        ground_truth_choice = extract_option_letter(ground_truth_full)

        # 判断是否正确
        is_correct = False
        if model_choice and ground_truth_choice:
            is_correct = (model_choice == ground_truth_choice)

        print(f"   [清洗后对比]: 模型[{model_choice}] vs 标准[{ground_truth_choice}]")
        print(f"   [判定结果]: {'TRUE (正确)' if is_correct else 'FALSE (错误)'}")

        # 6. 保存结果
        result_item = {
            "id": q_id,
            "paper_name": item.get("paper_name", ""),
            "question": question_text,
            "matched_survey": os.path.basename(survey_path),
            "ground_truth_raw": ground_truth_full,
            "model_raw_response": model_response,
            "ground_truth_choice": ground_truth_choice,
            "model_choice": model_choice,
            "is_correct": is_correct
        }
        results.append(result_item)

        try:
            with open(output_file, "w", encoding="utf-8") as f:
                json.dump(results, f, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"保存结果失败: {e}")

        time.sleep(0.5)

    print(f"\n>>> 全部完成！结果已保存至: {output_file}")

    # 统计
    correct_count = sum(1 for r in results if r.get("is_correct") is True)
    processed_count = len(results)
    if processed_count > 0:
        print(f"正确率: {correct_count}/{processed_count} ({correct_count / processed_count:.2%})")


if __name__ == "__main__":
    main()