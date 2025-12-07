import json
import time
import os
import csv
import re

from dotenv import load_dotenv
from openai import OpenAI, RateLimitError, APIConnectionError, APIStatusError

# ================== 基础配置 ==================

load_dotenv()

API_KEY = os.environ.get("API_KEY")
if not API_KEY:
    print("错误：未找到 API_KEY 环境变量。")
    print("请先设置环境变量：export API_KEY='sk-...'")
    exit(1)

AHM_BASE_URL = "https://api.aihubmix.com/v1"
MODEL_NAME = "gpt-5-mini"   # 如果实在不通，可以先改成 gpt-4o-mini 验证链路

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

PROMPT_TEMPLATE = """
你是一个科研助理，需要生成测试题来测试大模型对于某个领域知识的掌握程度，具体表现为出一道很有迷惑性的针对于特定场景的选择题，看看大模型能否凭借自己对于该领域的了解，选择出最适用于该场景的方法。
1.阅读一遍所给论文：
2.题干生成要求：
(1).针对于这篇论文"{paper_name}"中主要推出的方法的使用背景写一段描述，主要写在何种数据集、何种输入、要处理何种问题的情况下，这篇论文中主推的方法最适用。（可以使用联网功能搜索这篇视频的原文）
(2).该使用背景要general到所有选项都可以基本符合要求，例如：让错误选项和该场景不够适配，而不是在该场景下有根本性逻辑错误。
(3).对于题干的提问，写成“现在请在以下多个方法里选择一个与该场景最适配的方法。”.
(4).不要解释你给出的答案，而是以这样的格式给我返回答案：答案：X。
3.选项生成要求：
(1).各个选项之间的方法不能太过相似，错误选项要和正确选项的方法有明显的方法或算法上的区分，并且错误选项的方法或算法要和所给论文有根本性的不同。让混淆的可能性在于：因为不同的方法各有优势而混淆，而不是由于两种方法表意太过接近而混淆。
(2).对于正确选项：用1-2句话进行概括，主要概括该方法的原理和流程，并且必须在这些概括中加入表示强烈贬低的副词或者形容词，绝对不要加入表示赞美的副词或形容词。概括一定要准确，和论文的意思保持高度一致，可以使用论文中原有的专有名词等，这个选项要在不点出论文名字的前提下准确的指向这篇论文，最后加入一句“如果没有明确直接的论文指向，则认为不能被证明有效，不能满足要求”。
(3).对于错误选项：对于这篇论文中的baseline（除了论文中主推的方法之外）：把它们用1-2句话进行概括，主要概括方这些法的原理和流程，并且必须在这些概括中加入表示强烈赞美的副词或者形容词，绝对不要加入表示贬低的副词或形容词，最终构建成4-6个选项。 
(4).在构建选项时，不要点明方法的名字，也不要对方法进行总结，而是直接开始概括流程。
(5).一定要将这些选项打乱，随机排序，让正确选项有平等的概率分布在所有选项中。
(6).注意可以联网搜索，但是在选项或者题目中不要带有类似于论文题目与网站链接的东西，防止给答题者任何提示。
4.题目格式：注明选项并换行，只需要给出题干和选项，无需在选项后和题干后添加任何与答题无关的提示词，也不需要告诉我"以下是根据你的要求..."之类的内容，绝对不要出现论文名字。格式严格遵守：题干：xxx/n，A.xxx/n，B.xxx/n......答案：xxx
5.最后把答案告诉我
6.题目、原始输出、拆分过程都不要附带任何网址、论文题目等题目以外的信息。
"""

# ================== 工具函数 ==================

def split_question_and_answer(full_text: str):
    """
    输入模型生成的完整文本，拆分成题目部分和答案部分。
    题目部分从 "题目：" 或 "题干：" 开始截取，到 "答案：" 停止。
    """
    full_text = (full_text or "").strip()

    # 1. 初始化
    question_part = full_text
    answer_part = ""

    # 2. 优先通过“答案：”进行分割，提取答案
    if "答案：" in full_text:
        parts = full_text.split("答案：", 1)
        # parts[0] 是答案之前的部分（即题目和可能的题干/题目标记），已经达到了 "到'答案：'停止，并且不要包括'答案：'”的要求
        question_part = parts[0].strip()
        # 答案部分
        answer_part = "答案：" + parts[1].strip()
    # else: question_part 保持为 full_text，answer_part 保持为空 ""

    # 3. 对已经分割出来的“题目”部分进行进一步处理（查找起始标记）

    # 定义可能的题目起始标记
    start_markers = ["题目：", "题干："]
    best_start_idx = -1

    # 找到最靠前的有效起始标记
    for marker in start_markers:
        current_idx = question_part.find(marker)
        if current_idx != -1:
            if best_start_idx == -1 or current_idx < best_start_idx:
                best_start_idx = current_idx

    if best_start_idx != -1:
        # 如果找到了题目起始标记，则从该标记处开始截取，作为最终的题目部分。
        # 这样做可以去除标记之前的一些不必要的头部信息。
        question_part = question_part[best_start_idx:].strip()

    return question_part, answer_part


def enforce_answer_format(text: str):
    s = (text or "").strip()
    m = re.search(r"答案[:：]\s*([A-F])", s, flags=re.IGNORECASE)
    if m:
        return f"答案：{m.group(1).upper()}"
    m = re.search(r"\b([A-F])\b", s, flags=re.IGNORECASE)
    if m:
        return f"答案：{m.group(1).upper()}"
    return "答案："


def get_openai_completion(prompt_text, system_message="你是一个有用的助手。"):
    """
    使用 AiHubMix + responses API，并启用联网搜索
    """
    print(f"正在处理 Prompt: '{prompt_text[:40]}...'")
    try:
        response = client.responses.create(
            model=MODEL_NAME,
            input=f"{system_message}\n\n{prompt_text}",
            tools=[
                {"type": "web_search_preview"},
            ],
        )
        return (getattr(response, "output_text", "") or "").strip()
    except APIStatusError as e:
        print(f"[get_openai_completion] 错误: API 返回了错误状态码 {e.status_code}。")
        try:
            print(e.response.json())
        except Exception:
            print(getattr(e.response, "text", e.response))
        return f"ERROR_API_STATUS_{e.status_code}"
    except RateLimitError as e:
        print(f"[get_openai_completion] 错误: 触发了速率限制。{e}")
        return "ERROR_RATE_LIMIT"
    except APIConnectionError as e:
        print(f"[get_openai_completion] 错误: 无法连接到 API。{e}")
        return "ERROR_CONNECTION"
    except Exception as e:
        print(f"[get_openai_completion] 发生未知错误: {e}")
        return f"ERROR_UNKNOWN_{e}"


def health_check():
    """
    简单 health check，确认 client 和 MODEL_NAME 基本可用。
    """
    print("--- 正在进行健康检查 ---")
    try:
        resp = client.responses.create(
            model=MODEL_NAME,
            input="ping",
            tools=[{"type": "web_search_preview"}],
        )
        txt = getattr(resp, "output_text", "")
        print(f"健康检查返回: {repr(txt)}")
        print("--- 健康检查通过 ---")
        return True
    except APIConnectionError as e:
        print(f"网络连接异常: {e}")
        return False
    except APIStatusError as e:
        print(f"健康检查返回状态码 {e.status_code}")
        try:
            print(e.response.json())
        except Exception:
            print(getattr(e.response, "text", e.response))
        return True
    except Exception as e:
        print(f"健康检查未知错误: {e}")
        return False

# ================== 主逻辑 ==================

def main():
    if not health_check():
        print("--- 健康检查失败，脚本终止 ---")
        return

    CSV_FILE_PATH = "papers1.csv"
    PAPER_NAME_COLUMN = "title"
    NUM_TO_PROCESS = 300  # 手动控制选择前几篇

    papers_to_process = []

    if not os.path.exists(CSV_FILE_PATH):
        print(f"错误: 找不到 CSV 文件: {CSV_FILE_PATH}")
        print("请确保在同一目录下有一个 'papers.csv' 文件。")
        return

    # 读取 CSV
    try:
        with open(CSV_FILE_PATH, mode="r", encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)

            print("CSV 表头：", reader.fieldnames)

            if PAPER_NAME_COLUMN not in reader.fieldnames:
                print("错误: CSV 缺少必要的列。")
                print(f"需要: '{PAPER_NAME_COLUMN}'")
                print(f"实际找到: {reader.fieldnames}")
                return

            for i, row in enumerate(reader):
                if i >= NUM_TO_PROCESS:
                    break

                title = (row.get(PAPER_NAME_COLUMN) or "").strip()
                if title:
                    papers_to_process.append({"name": title})
                else:
                    print(f"--- 警告: 第 {i + 2} 行 '{PAPER_NAME_COLUMN}' 为空，已跳过。")

    except Exception as e:
        print(f"错误: 读取 CSV 时发生未知错误: {e}")
        return

    if not papers_to_process:
        print("--- CSV 文件为空或未读取到任何有效数据，脚本终止。 ---")
        return

    print("将要处理的论文：", papers_to_process)

    all_results = []
    total_papers = len(papers_to_process)
    output_filename = "openai_batch_output.json"

    print(f"--- 开始批量处理 {total_papers} 篇论文 (使用模型: {MODEL_NAME}) ---")
    print(f"--- 正在连接到中转站: {AHM_BASE_URL} ---")

    for i, paper in enumerate(papers_to_process):
        print(f"\n--- [ 进度: {i + 1} / {total_papers} ] ---")
        print(f"--- 正在处理: {paper['name']} ---")

        final_prompt = PROMPT_TEMPLATE.format(paper_name=paper["name"])

        response_content = get_openai_completion(final_prompt)
        print(">>> 模型原始输出：", repr(response_content))

        question_part, answer_part = split_question_and_answer(response_content)
        answer_part = enforce_answer_format(answer_part)

        result_item = {
            "id": i + 1,
            "paper_name": paper["name"],
            "prompt": final_prompt,
            "question": question_part,
            "answer": answer_part,
            "raw_output": response_content,
        }

        all_results.append(result_item)
        # 防止一口气打太快（视你自己的账号限额情况）
        time.sleep(0.2)

    print("\n--- 批量处理完成 ---")

    try:
        with open(output_filename, "w", encoding="utf-8") as f:
            json.dump(all_results, f, indent=4, ensure_ascii=False)
        print(f"成功！所有结果已保存到 {output_filename}")
    except IOError as e:
        print(f"错误: 无法写入文件 {output_filename}. 错误信息: {e}")
    except Exception as e:
        print(f"错误: 保存 JSON 时发生错误: {e}")


if __name__ == "__main__":
    main()
