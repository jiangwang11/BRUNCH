import json
import time
import os
import re
from dotenv import load_dotenv
from openai import OpenAI, RateLimitError, APIConnectionError, APIStatusError
from openai.types.chat import ChatCompletionUserMessageParam

# ================== 基础配置 ==================

load_dotenv()

API_KEY = os.environ.get("OPENROUTER_KEY")
if not API_KEY:
    print("错误：未找到 OPENROUTER_KEY 环境变量。")
    print("请先设置环境变量：export OPENROUTER_KEY='sk-...'")
    exit(1)

# ✅ OpenRouter 代理
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"

# ✅ 使用 DeepSeek v3.1 + 联网
MODEL_NAME = "deepseek/deepseek-chat-v3.1:online"

# ✅ 健康检查模型（改为 DeepSeek，避免依赖 OpenAI）
HEALTH_CHECK_MODEL = "deepseek/deepseek-chat"

# ================== 批量控制 ==================

BATCH_SIZE = 1   # 每次最多生成多少篇

# ================== 初始化客户端 ==================

try:
    client = OpenAI(
        api_key=API_KEY,
        base_url=OPENROUTER_BASE_URL,
        default_headers={
            "HTTP-Referer": "https://your-project.com",
            "X-Title": "Survey-Generator"
        },
        timeout=3600,
    )
except Exception as e:
    print(f"错误: 无法初始化 OpenAI 客户端。 {e}")
    exit(1)

# ================== Prompt 模板 ==================

SURVEY_PROMPT_TEMPLATE = (
    "你是一个科研助手，要帮助研究人员尽可能快速地了解对应领域，"
    "一篇可读的、详尽的 survey 是最便捷的方式。"
    "请生成一篇关于「{field}」领域从 2022 年到 2025 年 11 月之间论文的中文综述，"
    "必须使用联网搜索工具检索并核对信息，且允许你访问论文库, "
    "优先引用权威来源（顶会/顶刊、arXiv、官方资料），覆盖高引用与最新预印本。"
    "格式要求：严格的综述结构（引言、方法分类与代表作、实验与评价、趋势与挑战、结论），"
    "对主要论文的介绍尽可能完整；"
)

# ================== 工具函数 ==================

def sanitize_filename(name):
    name = re.sub(r'[\\/*?:"<>|]', "_", name)
    return name[:80].strip()


def health_check():
    print("--- 正在进行健康检查（OpenRouter + DeepSeek） ---")
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


def get_survey_from_deep_research(prompt_text: str) -> str:
    """
    ✅ DeepSeek v3.1 + OpenRouter Exa 联网搜索
    ✅ 自动检测是否真的联网
    ✅ 自动检测是否真的使用了网页引用
    ✅ 如果没联网 → 控制台报警
    """

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": (
                    "你是一个科研助手，要帮助研究人员尽可能快速地了解对应领域，"
                    "一篇可读的、详尽的 survey 是最便捷的方式。"
                    "请生成一篇关于「{field}」领域从 2022 年到 2025 年 11 月之间论文的中文综述，"
                    "必须使用联网搜索工具检索并核对信息，且允许你访问论文库, "
                    "优先引用权威来源（顶会/顶刊、arXiv、官方资料），覆盖高引用与最新预印本。"
                    "格式要求：严格的综述结构（引言、方法分类与代表作、实验与评价、趋势与挑战、结论），"
                    "对主要论文的介绍尽可能完整；"
                )
            },
            {"role": "user", "content": prompt_text}
        ],
        extra_body={   # ✅ OpenRouter 正确插件传参方式
            "plugins": [
                {
                    "id": "web",
                    "engine": "exa",
                    "max_results": 10
                }
            ]
        }
    )

    message = response.choices[0].message
    content = (message.content or "").strip()

    # ================== ✅ 联网真实性校验 ==================

    used_web_plugin = False
    citation_count = 0

    # ✅ 1️⃣ 官方最可靠方式：检查 annotations
    annotations = getattr(message, "annotations", None)
    if annotations:
        for ann in annotations:
            if hasattr(ann, "type") and ann.type == "url_citation":
                used_web_plugin = True
                citation_count += 1


    # ✅ 2️⃣ 兜底方式：正则检测是否真的输出了网页链接
    if not used_web_plugin:
        url_pattern = re.compile(r"https?://\S+")
        found_urls = url_pattern.findall(content)
        citation_count = len(found_urls)
        if citation_count > 0:
            used_web_plugin = True

    # ================== ✅ 检测结果输出 ==================

    if used_web_plugin:
        print(f">>> ✅ 已检测到真实联网搜索引用，引用数量 ≈ {citation_count}")
    else:
        print("⚠️⚠️⚠️ 警告：本次生成【未检测到任何真实网页引用】！")
        print("⚠️⚠️⚠️ 模型可能出现“假装联网但实际未搜索”的情况！")
        print("⚠️⚠️⚠️ 建议：")
        print("    1）检查 OpenRouter 是否返回了 annotations")
        print("    2）检查 Exa 搜索额度是否耗尽")
        print("    3）检查该模型当前是否临时不支持 web 插件")

    return content

# ================== 主逻辑 ==================

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))

    input_json_name = "paper_fields_output.json"
    input_json_path = os.path.join(script_dir, input_json_name)

    # ✅ survey 根目录
    survey_root_dir = os.path.join(script_dir, "survey")

    # ✅ 以模型名创建子文件夹
    safe_model_name = sanitize_filename(MODEL_NAME.replace("/", "_"))
    model_output_dir = os.path.join(survey_root_dir, safe_model_name)

    print(f"\n>>> 工作目录信息:")
    print(f"脚本目录: {script_dir}")
    print(f"数据来源: {input_json_path}")
    print(f"Survey 根目录: {survey_root_dir}")
    print(f"模型子目录: {model_output_dir}")
    print(f"批量设置: 每次最多 {BATCH_SIZE} 篇")
    print(f"使用模型: {MODEL_NAME}\n")

    os.makedirs(model_output_dir, exist_ok=True)

    if not health_check():
        return

    # ========== 读取字段数据 ==========

    if not os.path.exists(input_json_path):
        print(f"错误: 找不到输入文件 {input_json_name}")
        return

    try:
        with open(input_json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            if not isinstance(data, list):
                print("错误: JSON 格式不正确，应为数组。")
                return
    except Exception as e:
        print(f"读取 JSON 失败: {e}")
        return

    items = []
    for it in data:
        fid = it.get("id")
        field = (it.get("field") or "").strip()
        if fid is not None and field and "ERROR" not in field:
            items.append({"id": fid, "field": field})

    items.sort(key=lambda x: x["id"])

    if not items:
        print("--- 没有找到有效的领域信息 ---")
        return

    total_items = len(items)
    print(f"--- 计划生成 {total_items} 篇综述 ---")

    # ========== 生成综述 ==========

    generated_count = 0

    for i, item in enumerate(items):
        if generated_count >= BATCH_SIZE:
            print(f"\n>>> 已达到本次批量限制 ({BATCH_SIZE} 篇)，脚本停止。")
            break

        fid = item["id"]
        field_name = item["field"]

        print(f"\n--- [{i + 1}/{total_items}] 正在生成: id={fid}, field={field_name} ---")

        final_prompt = SURVEY_PROMPT_TEMPLATE.format(field=field_name)

        start_time = time.time()
        try:
            survey_content = get_survey_from_deep_research(final_prompt)
        except Exception as e:
            print(f"生成失败: {e}")
            continue

        duration = time.time() - start_time
        print(f">>> 生成完成 (耗时 {duration:.1f}s)")

        safe_field_name = sanitize_filename(field_name)
        file_name = f"{fid:02d}_Survey_{safe_field_name}.md"
        file_path = os.path.join(model_output_dir, file_name)

        try:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(survey_content)
            print(f">>> 已保存: {file_path}")
            generated_count += 1
        except Exception as e:
            print(f"保存失败: {e}")

        time.sleep(1)

    print(f"\n>>> 任务完成！本次共生成 {generated_count} 篇综述。")


if __name__ == "__main__":
    main()
