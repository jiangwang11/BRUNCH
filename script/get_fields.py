import json
import time
import os
import csv
import sys
from dotenv import load_dotenv
from openai import OpenAI, RateLimitError, APIConnectionError, APIStatusError
from openai.types.chat import (
    ChatCompletionMessageParam,
    ChatCompletionSystemMessageParam,
    ChatCompletionUserMessageParam,
)

# ================== 基础配置 ==================

load_dotenv()

API_KEY = os.environ.get("API_KEY")
if not API_KEY:
    # API_KEY = "sk-xxxxxxxx" # 如果需要硬编码，请取消注释并填入
    print("错误：未找到 API_KEY 环境变量。")
    print("请先设置环境变量：export API_KEY='sk-...'")
    exit(1)

AHM_BASE_URL = "https://aihubmix.com/v1"
MODEL_NAME = "gpt-4o"

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

PROMPT_TEMPLATE = (
    """
    步骤 1：仔细阅读{title}这篇论文
    步骤 2：给出这篇论文的细粒度主题（1–2 个短语）。
    步骤 3：给出这篇论文所属的大范围领域。
    步骤 4：生成一个位于步骤 1 与步骤 2 之间的“中等粒度研究领域”。
    该研究领域必须满足：
    - 常用于综述论文的小节标题；
    - 通常涵盖约 10-30 篇论文；
    - 针对该领域撰写的综述，有可能包含这篇论文，也可能不包含。
    最终只输出步骤 4 的研究领域。
    """
)


# ================== 工具函数 ==================

def get_openai_completion(prompt_text, system_message="你是一个专业的科研助手。"):
    messages: list[ChatCompletionMessageParam] = [
        ChatCompletionSystemMessageParam(role="system", content=system_message),
        ChatCompletionUserMessageParam(role="user", content=prompt_text),
    ]

    try:
        completion = client.chat.completions.create(
            model=MODEL_NAME,
            messages=messages,
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

    except APIStatusError as e:
        print(f"[API Error] 状态码 {e.status_code}")
        return f"ERROR_API_STATUS_{e.status_code}"
    except RateLimitError as e:
        print(f"[API Error] 速率限制: {e}")
        return "ERROR_RATE_LIMIT"
    except APIConnectionError as e:
        print(f"[API Error] 连接失败: {e}")
        return "ERROR_CONNECTION"
    except Exception as e:
        print(f"[Unknown Error] {e}")
        return f"ERROR_UNKNOWN_{e}"


def clean_field_content(text):
    """
    提取 '领域：' 之后的内容。
    """
    text = text.strip()
    # 移除可能的 markdown 格式
    text = text.replace('**', '').replace('"', '').replace("'", "")

    if "领域：" in text:
        return text.split("领域：", 1)[1].strip()
    elif "领域:" in text:
        return text.split("领域:", 1)[1].strip()
    return text


def health_check():
    print("--- 正在进行健康检查 ---")
    try:
        resp = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[ChatCompletionUserMessageParam(role="user", content="ping")],
        )
        print("--- 健康检查通过 ---")
        return True
    except Exception as e:
        print(f"健康检查失败: {e}")
        return False


# ================== 主逻辑 ==================

def main():
    # 1. 获取脚本所在的绝对路径
    script_dir = os.path.dirname(os.path.abspath(__file__))

    input_json_name = "openai_batch_output_filtered_social_science.json"
    output_filename = "paper_fields_output_social_science.json"

    input_json_path = os.path.join(script_dir, input_json_name)
    output_json_path = os.path.join(script_dir, output_filename)

    print(f"\n>>> 工作目录信息:")
    print(f"脚本目录: {script_dir}")
    print(f"数据来源: {input_json_path}")
    print(f"输出路径: {output_json_path}\n")

    NUM_TO_PROCESS = None

    if not health_check():
        return

    # 2. 准备数据
    items = []
    if not os.path.exists(input_json_path):
        print(f"错误: 找不到输入 JSON 文件。")
        print(f"请确认该路径下存在文件: {input_json_path}")
        return

    try:
        with open(input_json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            if not isinstance(data, list):
                print("错误: JSON 格式不正确。")
                return
            items = sorted(data, key=lambda x: x.get("id", 0))
    except Exception as e:
        print(f"读取输入 JSON 失败: {e}")
        return

    if not items:
        print("--- 没有要处理的数据 ---")
        return

    total_papers = len(items)
    print(f"--- 开始处理 {total_papers} 条记录 ---")

    # 3. 初始化输出容器
    results = []
    print(f">>> 将写入输出文件: {output_json_path}")

    # 4. 循环处理并追加写入
    for idx, item in enumerate(items):
        item_id = item.get("id")
        question_text = (item.get("question") or "").strip()
        paper_title = (item.get("paper_name") or "").strip()
        display_name = (question_text[:40] or paper_title[:40])
        print(f"\n--- [{idx + 1}/{total_papers}] 处理: {display_name}... ---")

        prompt_title = paper_title if paper_title else question_text
        final_prompt = PROMPT_TEMPLATE.format(title=prompt_title)
        raw_response = get_openai_completion(final_prompt)

        cleaned_field = clean_field_content(raw_response)
        print(f"提取领域: {cleaned_field}")

        result_item = {
            "id": item_id,
            "field": cleaned_field
        }

        results.append(result_item)

        time.sleep(0.5)

    try:
        with open(output_json_path, "w", encoding="utf-8") as f_out:
            json.dump(results, f_out, ensure_ascii=False, indent=2)
        print(f">>> 已保存输出文件: {output_json_path}")
    except Exception as e:
        print(f"错误: 无法写入输出文件: {e}")
        return

    print(f"\n>>> 全部完成！")

    # ================== 调试验证环节 ==================
    print("\n[调试] 正在检查目录下的文件...")
    try:
        files_in_dir = os.listdir(script_dir)
        if output_filename in files_in_dir:
            size = os.path.getsize(output_json_path)
            print(f"SUCCESS: Python 在 '{script_dir}' 目录下找到了 '{output_filename}'！")
            print(f"文件大小: {size} 字节 (如果大于0，说明内容已写入)")
        else:
            print(f"FAIL: Python 在 '{script_dir}' 目录下没有找到 '{output_filename}'。")
            print(f"当前目录下的文件列表: {files_in_dir}")
    except Exception as e:
        print(f"检查文件时出错: {e}")


if __name__ == "__main__":
    main()