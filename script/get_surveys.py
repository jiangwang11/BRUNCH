import json
import time
import os
import re
from dotenv import load_dotenv
from openai import OpenAI, RateLimitError, APIConnectionError, APIStatusError
from openai.types.chat import (
    ChatCompletionUserMessageParam,
)

# ================== 基础配置 ==================

load_dotenv()

API_KEY = os.environ.get("API_KEY")
if not API_KEY:
    print("错误：未找到 API_KEY 环境变量。")
    print("请先设置环境变量：export API_KEY='sk-...'")
    exit(1)

# 推荐用这个域名（你之前测试脚本也是这个）
AHM_BASE_URL = "https://api.aihubmix.com/v1"

# 便宜模型，用于健康检查
HEALTH_CHECK_MODEL = "gpt-5-mini"

# deep research 模型（以 AiHubMix 文档为准，你可以换成 o4-mini-deep-research）
DEEP_RESEARCH_MODEL = "o3-deep-research"

# 兜底用的普通 Responses 模型
FALLBACK_RESPONSES_MODEL = "gpt-5-mini"

# ================== 批量控制配置 ==================

BATCH_SIZE = 2
SKIP_EXISTING = False  # 现在没用到，先保留

# ================== 初始化客户端 ==================

try:
    client = OpenAI(
        api_key=API_KEY,
        base_url=AHM_BASE_URL,
        default_headers={
            "User-Agent": "openai-python",
            "OpenAI-Client-User-Agent": '{"lang":"python"}'
        },
        timeout=3600,  # deep research 可能很慢
    )
except Exception as e:
    print(f"错误: 无法初始化 OpenAI 客户端。 {e}")
    exit(1)

# ================== Prompt 模板 ==================

SURVEY_PROMPT_TEMPLATE = (
    "你是一个科研助手，要帮助研究人员尽可能快速地了解对应领域，"
    "一篇可读的、详尽的 survey 是最便捷的方式。"
    "请生成一篇关于「{field}」领域从 2022 年到 2025 年 11 月之间论文的综述，"
    "要求尽可能全面，尤其要覆盖引用量高或者重要的文章，同时不要忽视最新和预印本论文。"
    "注意：格式要是严格的综述格式，对主要论文的介绍尽可能完整。"
)


# ================== 工具函数 ==================

def call_deep_research(input_text: str) -> str:
    """
    只负责调用 deep research 模型。
    出错直接抛异常，外层决定要不要兜底。
    """
    response = client.responses.create(
        model=DEEP_RESEARCH_MODEL,
        input=input_text,
        tools=[
            {"type": "web_search_preview"},
            {"type": "code_interpreter", "container": {"type": "auto"}},
        ],
    )
    generated_content = getattr(response, "output_text", None)
    return (generated_content or "").strip()


def call_fallback_responses(input_text: str) -> str:
    """
    兜底：用普通 Responses 模型 + web_search_preview。
    """
    print(f"[Fallback] 使用普通模型: {FALLBACK_RESPONSES_MODEL}")
    response = client.responses.create(
        model=FALLBACK_RESPONSES_MODEL,
        input=input_text,
        tools=[
            {"type": "web_search_preview"},
        ],
    )
    generated_content = getattr(response, "output_text", None)
    return (generated_content or "").strip()


def get_openai_completion(prompt_text, system_message="你是一个专业的科研助手。"):
    """
    优先使用 deep research：
    - 成功：直接用 deep research 的结果
    - 发生 5xx / no_valid_channel_error：打印提示 + 自动兜底普通模型
    """
    input_text = f"系统指令：{system_message}\n\n用户需求：{prompt_text}"

    # 先 try deep research
    try:
        print(f"[DeepResearch] 调用模型: {DEEP_RESEARCH_MODEL}")
        return call_deep_research(input_text)

    except APIStatusError as e:
        # 这里是服务器返回 HTTP 错误
        msg = str(e)
        print(f"[DeepResearch] APIStatusError: 状态码={e.status_code}, 详情={msg}")

        # 只要是 5xx 或者包含 no_valid_channel_error，就判定为通道问题，直接兜底
        if e.status_code >= 500 or "no_valid_channel_error" in msg:
            print("[DeepResearch] 看起来服务端 deep research 通道不可用，将自动使用普通模型兜底。")
            try:
                return call_fallback_responses(input_text)
            except Exception as e2:
                print(f"[Fallback] 也失败了: {e2}")
                return f"ERROR_FALLBACK_FAILED: {e2}"
        else:
            # 其它状态码（4xx 等），直接返回错误信息
            return f"ERROR_DEEP_RESEARCH_STATUS_{e.status_code}"

    except RateLimitError as e:
        print(f"[DeepResearch] 速率限制: {e}")
        # 速率问题也可以选择兜底
        try:
            return call_fallback_responses(input_text)
        except Exception as e2:
            print(f"[Fallback] 也失败了: {e2}")
            return "ERROR_RATE_LIMIT_AND_FALLBACK_FAILED"

    except APIConnectionError as e:
        print(f"[DeepResearch] 连接失败: {e}")
        # 连接挂了也兜底
        try:
            return call_fallback_responses(input_text)
        except Exception as e2:
            print(f"[Fallback] 也失败了: {e2}")
            return "ERROR_CONNECTION_AND_FALLBACK_FAILED"

    except Exception as e:
        print(f"[DeepResearch] 未知错误: {e}")
        # 其它异常也兜底试一下
        try:
            return call_fallback_responses(input_text)
        except Exception as e2:
            print(f"[Fallback] 也失败了: {e2}")
            return f"ERROR_UNKNOWN_AND_FALLBACK_FAILED: {e}"


def sanitize_filename(name):
    name = re.sub(r'[\\/*?:"<>|]', "", name)
    return name[:50].strip()


def health_check():
    """
    用便宜模型做最小 chat.completions ping。
    """
    print("--- 正在进行健康检查 ---")
    try:
        client.chat.completions.create(
            model=HEALTH_CHECK_MODEL,
            messages=[ChatCompletionUserMessageParam(role="user", content="ping")],
        )
        print("--- 健康检查通过 ---")
        return True
    except Exception as e:
        print(f"健康检查失败: {e}")
        return False


# ================== 主逻辑 ==================

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))

    input_json_name = "paper_fields_output.json"
    input_json_path = os.path.join(script_dir, input_json_name)

    output_dir_name = "surveys"
    output_dir_path = os.path.join(script_dir, output_dir_name)

    print(f"\n>>> 工作目录信息:")
    print(f"脚本目录: {script_dir}")
    print(f"数据来源: {input_json_path}")
    print(f"保存目录: {output_dir_path}")
    print(f"批量设置: 每次最多 {BATCH_SIZE} 篇")
    print(f"优先模型: deep research = {DEEP_RESEARCH_MODEL}，兜底 = {FALLBACK_RESPONSES_MODEL}\n")

    if not os.path.exists(output_dir_path):
        os.makedirs(output_dir_path)

    if not health_check():
        return

    # 1. 读取及去重
    if not os.path.exists(input_json_path):
        print(f"错误: 找不到输入文件 {input_json_name}")
        return

    items = []
    try:
        with open(input_json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            if not isinstance(data, list):
                print("错误: JSON 格式不正确，应为数组。")
                return

            for it in data:
                fid = it.get("id")
                field = (it.get("field") or "").strip()
                if fid is not None and field and "Error" not in field and len(field) > 2:
                    items.append({"id": fid, "field": field})

            items.sort(key=lambda x: x["id"])
    except Exception as e:
        print(f"读取 JSON 失败: {e}")
        return

    if not items:
        print("--- 没有找到有效的领域信息 ---")
        return

    total_items = len(items)
    print(f"--- 计划生成 {total_items} 篇综述 ---")

    # 2. 批量生成循环
    generated_count = 0
    results = []

    for i, item in enumerate(items):
        if generated_count >= BATCH_SIZE:
            print(f"\n>>> 已达到本次批量限制 ({BATCH_SIZE} 篇)，脚本停止。")
            break

        fid = item["id"]
        field_name = item["field"]

        print(f"\n--- [{i + 1}/{total_items}] 正在生成: id={fid}, field={field_name} ---")

        start_time = time.time()
        final_prompt = SURVEY_PROMPT_TEMPLATE.format(field=field_name)
        survey_content = get_openai_completion(final_prompt)
        duration = time.time() - start_time

        print(f">>> 生成完成 (耗时 {duration:.1f}s)")

        safe_name = sanitize_filename(field_name)
        file_name = f"{fid:02d}_Survey_{safe_name}.md"
        file_path = os.path.join(output_dir_path, file_name)

        try:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(survey_content)
            generated_count += 1
            print(f">>> 已保存: {file_name}")
        except Exception as e:
            print(f"保存文件失败: {e}")

        for it in data:
            if it.get("id") == fid:
                it["md_path"] = file_path
                break

        time.sleep(1)

    # 3. 更新字段文件，记录 md 路径
    try:
        with open(input_json_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"\n>>> 全部任务完成！共生成 {generated_count} 篇综述，并更新 md 路径到: {input_json_path}")
    except Exception as e:
        print(f"更新字段文件失败: {e}")


if __name__ == "__main__":
    main()
