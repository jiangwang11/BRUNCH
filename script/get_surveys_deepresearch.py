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
    print("错误：未找到 API_KEY 环境变量。")
    print("请先设置环境变量：export API_KEY='sk-...'")
    exit(1)

# ✅ 改为 OpenRouter 代理
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"

# ✅ 使用 Deep Research 模型
MODEL_NAME = "alibaba/tongyi-deepresearch-30b-a3b"

# 便宜模型用于健康检查
HEALTH_CHECK_MODEL = "openai/gpt-4o-mini"

# ================== 批量控制 ==================

BATCH_SIZE = 3

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
    "你是一名严谨的科研助理，请生成一篇关于「{field}」的中文学术综述，覆盖 2022–2025 年的代表性工作。"
    "【强制要求】1. 只引用真实存在的论文（顶会/顶刊/arXiv），不得编造。2. 每种方法类别最多选 3–5 篇最具代表性的论文。3. 每篇论文的介绍限制在 4–6 句内，突出：- 研究问题 - 核心方法- 关键实验结论4. 实验与评价部分只总结共性结论，不逐篇复述。5. 禁止无信息量的泛泛表述（如“取得了良好效果”）。6. 结尾给出 2025 年前后的真实研究趋势预测（不少于 3 点）。【结构必须为】- 引言- 方法分类与代表作 - 实验与评价总结- 趋势与挑战- 结论- 参考文献（不少于 12 篇）【输出风格】- 学术密度优先于篇幅- 禁止水文- 禁止空话套话"

)

# ================== 工具函数 ==================

def sanitize_filename(name):
    name = re.sub(r'[\\/*?:"<>|]', "_", name)
    return name[:80].strip()


def health_check():
    print("--- 正在进行健康检查（OpenRouter） ---")
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


def get_survey_from_deep_research(prompt_text: str) -> dict:
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": "你是一个专业的科研助手。必须使用联网搜索检索并核对信息，优先引用权威来源（顶会/顶刊、arXiv、官方资料）。在输出中给出参考文献列表（含标题、作者、年份、来源链接），并确保正文关键论断至少附一条引用。"},
            {"role": "user", "content": prompt_text}
        ],
        max_tokens=40000,
    )
    content = (getattr(response.choices[0].message, "content", "") or "").strip()

    usage = getattr(response, "usage", None)
    prompt_tokens = getattr(usage, "prompt_tokens", None) if usage else None
    completion_tokens = getattr(usage, "completion_tokens", None) if usage else None
    total_tokens = getattr(usage, "total_tokens", None) if usage else None
    if total_tokens is None and isinstance(prompt_tokens, int) and isinstance(completion_tokens, int):
        total_tokens = prompt_tokens + completion_tokens

    ref_count = len(re.findall(r"https?://\S+", content))

    return {
        "content": content,
        "tokens": {
            "prompt": prompt_tokens,
            "completion": completion_tokens,
            "total": total_tokens,
        },
        "references": ref_count,
    }


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
    metrics_path = os.path.join(model_output_dir, "surveys_stats.json")
    with open(metrics_path, "w", encoding="utf-8") as f:
        json.dump([], f, ensure_ascii=False, indent=2)

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
    results = []

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
            result = get_survey_from_deep_research(final_prompt)
            survey_content = result.get("content", "")
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

            token_info = result.get("tokens", {})
            citation_count = result.get("references", 0)
            entry = {
                "id": fid,
                "field": field_name,
                "md_path": file_path,
                "tokens_total": token_info.get("total"),
                "tokens_prompt": token_info.get("prompt"),
                "tokens_completion": token_info.get("completion"),
                "references": citation_count,
                "duration_sec": duration,
                "length_chars": len(survey_content),
            }

            try:
                with open(metrics_path, "r", encoding="utf-8") as mf:
                    current = json.load(mf)
                    if not isinstance(current, list):
                        current = []
            except Exception:
                current = []

            current.append(entry)
            current.sort(key=lambda x: x.get("id", 0))

            with open(metrics_path, "w", encoding="utf-8") as mf:
                json.dump(current, mf, ensure_ascii=False, indent=2)
            print(f">>> 📈 已追加统计到: {metrics_path}")
        except Exception as e:
            print(f"保存失败: {e}")

        time.sleep(1)

    try:
        with open(metrics_path, "r", encoding="utf-8") as f:
            all_stats = json.load(f)
        print(f"\n>>> 任务完成！本次共生成 {generated_count} 篇综述。累计统计条目: {len(all_stats)}，路径: {metrics_path}")
    except Exception as e:
        print(f"\n⚠️ 读取统计失败: {e}")
        print(f">>> 任务完成！本次共生成 {generated_count} 篇综述。")


if __name__ == "__main__":
    main()
