import json
import time
import os
import re
from dotenv import load_dotenv
from openai import OpenAI

# ================== 基础配置 ==================

load_dotenv()

API_KEY = os.environ.get("OPENROUTER_KEY")
if not API_KEY:
    print("错误：未找到 OPENROUTER_KEY 环境变量。")
    exit(1)

OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"

# ✅ 你指定的单一模型（不做自动降级）
MODEL_NAME = "google/gemini-2.5-pro:online"
HEALTH_CHECK_MODEL = "deepseek/deepseek-chat"

BATCH_SIZE = 100

# ================== 初始化客户端 ==================

client = OpenAI(
    api_key=API_KEY,
    base_url=OPENROUTER_BASE_URL,
    default_headers={
        "HTTP-Referer": "https://your-project.com",
        "X-Title": "Survey-Generator"
    },
    timeout=3600,
)

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
    print("--- 正在进行健康检查 ---")
    try:
        client.chat.completions.create(
            model=HEALTH_CHECK_MODEL,
            messages=[{"role": "user", "content": "ping"}],
        )
        print("--- ✅ 健康检查通过 ---")
        return True
    except Exception as e:
        print(f"❌ 健康检查失败: {e}")
        return False

# ================== ✅ 核心安全生成函数（不自动降级） ==================

def get_survey_from_deep_research(prompt_text: str) -> dict:
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": "你是一个严谨的科研助手，必须基于真实联网搜索生成学术综述。"},
                {"role": "user", "content": prompt_text}
            ],
            max_tokens=15000,
            extra_body={
                "transform": "middle-out",
                "plugins": [
                    {"id": "web", "engine": "exa", "max_results": 10}
                ]
            }
        )
    except Exception as e:
        raise RuntimeError(f"API 调用直接异常（网络/节点级错误）: {e}")

    # ✅ ✅ ✅ 关键修复：完整打印 OpenRouter 的异常结构
    if not response:
        raise RuntimeError("API 返回了 None response（非常罕见）")

    # ✅ OpenRouter 错误有时是 dict 结构，不是 completion
    if isinstance(response, dict) and "error" in response:
        raise RuntimeError(f"OpenRouter 原始错误返回: {response}")

    if not hasattr(response, "choices") or not response.choices:
        raise RuntimeError(f"API 未返回 choices，原始 response = {response}")

    first_choice = response.choices[0]

    if not hasattr(first_choice, "message") or first_choice.message is None:
        raise RuntimeError(f"API choice 中无 message，原始 choice = {first_choice}")

    message = first_choice.message
    content = (getattr(message, "content", "") or "").strip()

    if not content:
        raise RuntimeError("模型返回 content 为空")

    # ✅ 引用统计
    url_pattern = re.compile(r"https?://\S+")
    citation_count = len(url_pattern.findall(content))

    # ✅ token 统计（OpenRouter 不稳定，可能为空）
    usage = getattr(response, "usage", None)
    prompt_tokens = getattr(usage, "prompt_tokens", None) if usage else None
    completion_tokens = getattr(usage, "completion_tokens", None) if usage else None
    total_tokens = getattr(usage, "total_tokens", None) if usage else None
    if total_tokens is None and isinstance(prompt_tokens, int) and isinstance(completion_tokens, int):
        total_tokens = prompt_tokens + completion_tokens

    return {
        "content": content,
        "tokens": {
            "prompt": prompt_tokens,
            "completion": completion_tokens,
            "total": total_tokens,
        },
        "references": citation_count,
    }


# ================== 主逻辑 ==================

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_json_path = os.path.join(script_dir, "paper_fields_output.json")

    survey_root_dir = os.path.join(script_dir, "survey")
    safe_model_name = sanitize_filename(MODEL_NAME.replace("/", "_"))
    model_output_dir = os.path.join(survey_root_dir, safe_model_name)

    print(f"脚本目录: {script_dir}")
    print(f"数据来源: {input_json_path}")
    print(f"输出目录: {model_output_dir}")
    print(f"使用模型: {MODEL_NAME}")

    os.makedirs(model_output_dir, exist_ok=True)
    metrics_path = os.path.join(model_output_dir, "surveys_stats.json")
    with open(metrics_path, "w", encoding="utf-8") as f:
        json.dump([], f, ensure_ascii=False, indent=2)

    if not health_check():
        return

    if not os.path.exists(input_json_path):
        print("❌ 找不到 paper_fields_output.json")
        return

    try:
        with open(input_json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        print(f"❌ JSON 读取失败: {e}")
        return

    items = []
    for it in data:
        fid = it.get("id")
        field = (it.get("field") or "").strip()
        if fid is not None and field and "ERROR" not in field:
            items.append({"id": fid, "field": field})

    items.sort(key=lambda x: x["id"])
    total_items = len(items)

    print(f"\n--- 计划生成 {total_items} 篇综述 ---")

    generated_count = 0
    results = []

    for i, item in enumerate(items):
        if generated_count >= BATCH_SIZE:
            print("\n>>> 已达到本次批量上限，停止。")
            break

        fid = item["id"]
        field_name = item["field"]

        print(f"\n--- [{i+1}/{total_items}] 生成: id={fid}, field={field_name}")

        final_prompt = SURVEY_PROMPT_TEMPLATE.format(field=field_name)

        try:
            start_time = time.time()
            result = get_survey_from_deep_research(final_prompt)
            survey_content = result.get("content", "")
            duration = time.time() - start_time
            print(f">>> ✅ 生成完成 ({duration:.1f}s)")
        except Exception as e:
            print(f"❌ 本条生成失败: {e}")
            with open(os.path.join(model_output_dir, "failed.log"), "a", encoding="utf-8") as f:
                f.write(f"id={fid}, field={field_name}, error={e}\n")
            continue

        safe_field_name = sanitize_filename(field_name)
        file_name = f"{fid:02d}_Survey_{safe_field_name}.md"
        file_path = os.path.join(model_output_dir, file_name)

        try:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(survey_content)
            print(f">>> ✅ 已保存: {file_path}")
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
            print(f"❌ 保存失败: {e}")

        time.sleep(1)

    try:
        with open(metrics_path, "r", encoding="utf-8") as f:
            all_stats = json.load(f)
        print(f"\n>>> ✅ 任务完成，本次成功生成 {generated_count} 篇综述。累计统计条目: {len(all_stats)}，路径: {metrics_path}")
    except Exception as e:
        print(f"\n⚠️ 读取统计失败: {e}")
        print(f">>> ✅ 任务完成，本次成功生成 {generated_count} 篇综述。")

if __name__ == "__main__":
    main()
