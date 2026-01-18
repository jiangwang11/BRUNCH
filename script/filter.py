import json
import os
import time
from dotenv import load_dotenv
from openai import OpenAI, RateLimitError, APIConnectionError, APIStatusError
from openai.types.chat import (
    ChatCompletionMessageParam,
    ChatCompletionSystemMessageParam,
    ChatCompletionUserMessageParam,
)

# ================== 基础配置 ==================

load_dotenv()

# 根据你的示例，这里可以是 AIHUBMIX_API_KEY 或者 API_KEY，请确保 .env 中名称一致
API_KEY = os.environ.get("API_KEY")
if not API_KEY:
    print("错误：未找到 API_KEY 环境变量。")
    exit(1)

AHM_BASE_URL = "https://api.aihubmix.com/v1"

# 基础模型名称（不带后缀）
BASE_MODEL_NAME = "qwen2.5-14b-instruct"

# 评估时的额外前缀模板
EXTRA_PREFIX_TEMPLATE = (
    "认真的阅读这篇论文{paper_name}，然后做这道题，"
    "要注意到如果选项中有很和这篇论文很契合的方法，就说明实践性能完全达到要求，"
    "完全可以运用在合适的环境下 ，并且可以忽略选项中的所有的贬义词和的褒义词，"
)

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


# ================== 核心调用封装 ==================


def get_openai_completion(
        prompt_text: str,
        system_message: str = "你是一个有用的助手。",
        enable_search: bool = False
) -> str:
    """
    GPT-5 (Qwen) 评估调用：
    - 根据 enable_search 决定是否在模型名后追加 :surfing
    """

    # === 关键修改逻辑开始 ===
    if enable_search:
        # 如果开启联网，追加 :surfing 后缀
        current_model = f"{BASE_MODEL_NAME}:surfing"
        search_status = "[联网开启]"
    else:
        # 如果关闭联网，使用基础模型名
        current_model = BASE_MODEL_NAME
        search_status = "[联网关闭]"
    # === 关键修改逻辑结束 ===

    print(f"[get_openai_completion] {search_status} Model: {current_model} | Prompt: '{prompt_text[:30]}...'")

    messages_list: list[ChatCompletionMessageParam] = [
        ChatCompletionSystemMessageParam(
            role="system",
            content=system_message
        ),
        ChatCompletionUserMessageParam(
            role="user",
            content=prompt_text
        ),
    ]

    try:
        completion = client.chat.completions.create(
            model=current_model,  # 使用动态生成的模型名
            messages=messages_list,
            # 这里不需要 extra_body 了，因为是通过模型名后缀控制的
        )

        content = completion.choices[0].message.content

        # content 可能是 str 或 list
        if isinstance(content, list):
            parts = []
            for part in content:
                if isinstance(part, dict) and part.get("type") == "text":
                    parts.append(part.get("text", ""))
                elif isinstance(part, str):
                    parts.append(part)
            return "".join(parts).strip()
        else:
            return (content or "").strip()

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


# ================== 答案解析 & 评估逻辑 ==================


def extract_choice_letter(text: str):
    """
    从形如“答案：C”“标准答案：B”这类文本里抽出 A–G。
    """
    if not text:
        return None
    idx = text.find("答案")
    sub = text[idx:] if idx != -1 else text
    for ch in sub:
        if ch in "ABCDEFG":
            return ch
    for ch in text:
        if ch in "ABCDEFG":
            return ch
    return None


def ask_and_eval(
        question_text: str,
        gt_choice: str,
        run_name: str,
        extra_prompt: str = "",
        enable_search: bool = False
) -> tuple[bool, bool]:
    """
    发起一次模型答题并评估。
    """
    base_instruction = "请直接给出你认为正确的选项，格式严格为：答案：X，不要输出其他内容。"

    if extra_prompt.strip():
        full_prompt = extra_prompt.strip() + "\n\n" + question_text + "\n\n" + base_instruction
    else:
        full_prompt = question_text + "\n\n" + base_instruction

    print(f"\n[{run_name}] 正在请求模型 (Search={enable_search})...")

    # 调用核心函数，传入 enable_search 参数
    model_answer_text = get_openai_completion(
        full_prompt,
        system_message="你是一个答题助手，只负责从选项中选择答案。",
        enable_search=enable_search
    )
    print(f"[{run_name}] 模型返回: {repr(model_answer_text)}")

    # 1. 先判断调用本身是否有效
    if not model_answer_text or model_answer_text.startswith("ERROR_"):
        print(f"[{run_name}] 本次调用无效，不计入正确率。")
        return False, False

    # 2. 解析模型选择
    model_choice = extract_choice_letter(model_answer_text)
    print(f"[{run_name}] 模型答案选项: {model_choice}")

    if model_choice is None:
        print(f"[{run_name}] 无法解析选项，不计入正确率。")
        return False, False

    # 3. 对比标准答案
    if gt_choice == model_choice:
        print(f"[{run_name}] 结果：✅ 正确")
        return True, True
    else:
        print(f"[{run_name}] 结果：❌ 错误")
        return True, False


def evaluate_from_json(json_path: str, filtered_output_path: str = "openai_batch_output_filtered_finance.json"):
    if not os.path.exists(json_path):
        print(f"错误: 找不到文件 {json_path}")
        return

    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    total_questions = 0
    valid_plain = 0
    correct_plain = 0
    valid_pref = 0
    correct_pref = 0
    skipped_by_gt = 0
    filtered_items = []

    for item in data:
        qid = item.get("id")
        question_text = item.get("question", "") or ""
        gt_answer_text = item.get("answer", "") or ""
        paper_name = (item.get("paper_name") or "").strip()
        extra_prompt = EXTRA_PREFIX_TEMPLATE.format(paper_name=paper_name)

        gt_choice = extract_choice_letter(gt_answer_text)

        print("\n==============================")
        print(f"题目 id = {qid}")
        print(f"论文名: {paper_name}")
        print(f"标准答案选项: {gt_choice}")

        total_questions += 1

        if gt_choice is None:
            print("⚠ 标准答案中未能解析出 A-G 选项，跳过。")
            skipped_by_gt += 1
            continue

        # 1. 原始提问 -> 关闭联网 (enable_search=False)
        # 此时模型参数为 BASE_MODEL_NAME
        is_valid_plain, is_correct_plain = ask_and_eval(
            question_text=question_text,
            gt_choice=gt_choice,
            run_name="原始提问",
            extra_prompt="",
            enable_search=False
        )
        if is_valid_plain:
            valid_plain += 1
            if is_correct_plain:
                correct_plain += 1

        # 2. 带前缀提问 -> 开启联网 (enable_search=True)
        # 此时模型参数会自动变为 BASE_MODEL_NAME + ":surfing"
        is_valid_pref, is_correct_pref = ask_and_eval(
            question_text=question_text,
            gt_choice=gt_choice,
            run_name="带前缀提问",
            extra_prompt=extra_prompt,
            enable_search=True
        )
        if is_valid_pref:
            valid_pref += 1
            if is_correct_pref:
                correct_pref += 1

        # 筛选逻辑：原始提问错，带前缀（联网）提问对
        if is_valid_plain and is_valid_pref and (not is_correct_plain) and is_correct_pref:
            filtered_items.append(item)

        time.sleep(0.5)

    print("\n==============================")
    print(f"JSON 中题目总数: {total_questions}")
    print(f"跳过题目数: {skipped_by_gt}")

    if valid_plain > 0:
        acc_plain = correct_plain / valid_plain
        print(f"[原始(不联网)] 正确率: {acc_plain:.2%}")
    else:
        print("[原始(不联网)] 无有效数据")

    if valid_pref > 0:
        acc_pref = correct_pref / valid_pref
        print(f"[前缀(联网)]   正确率: {acc_pref:.2%}")
    else:
        print("[前缀(联网)]   无有效数据")

    print(f"满足筛选条件的问题数: {len(filtered_items)}")

    # 保存结果
    try:
        for idx, it in enumerate(filtered_items, start=1):
            it["id"] = idx
        with open(filtered_output_path, "w", encoding="utf-8") as f:
            json.dump(filtered_items, f, ensure_ascii=False, indent=2)
        print(f"已保存到: {filtered_output_path}")
    except Exception as e:
        print(f"保存失败: {e}")


# ================== 入口 ==================

if __name__ == "__main__":
    evaluate_from_json("finance/openai_batch_output.json")