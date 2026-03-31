import json
import os
import re
import time
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

OPENROUTER_KEY = os.environ.get("OPENROUTER_KEY")
if not OPENROUTER_KEY:
    raise RuntimeError("缺少环境变量 OPENROUTER_KEY")

OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
MODEL_NAME = "qwen/qwen3-max:online"
SAFE_MODEL_DIRNAME = MODEL_NAME.replace("/", "_").replace(":", "_")
MODEL_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "survey", SAFE_MODEL_DIRNAME)
FAILED_LOG_PATH = os.path.join(MODEL_DIR, "failed.log")
STATS_PATH = os.path.join(MODEL_DIR, "surveys_stats.json")
INPUT_JSON_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "paper_fields_output.json")

client = OpenAI(
    api_key=OPENROUTER_KEY,
    base_url=OPENROUTER_BASE_URL,
    timeout=3600,
    default_headers={"HTTP-Referer": "https://your-project.com", "X-Title": "Survey-Retry"}
)

SURVEY_PROMPT_TEMPLATE = (
    "你是一名严谨的科研助理，请生成一篇关于「{field}」的中文学术综述，覆盖 2022–2025 年的代表性工作。"
    "【强制要求】1. 只引用真实存在的论文（顶会/顶刊/arXiv），不得编造。2. 每种方法类别最多选 3–5 篇最具代表性的论文。3. 每篇论文的介绍限制在 4–6 句内，突出：- 研究问题 - 核心方法- 关键实验结论4. 实验与评价部分只总结共性结论，不逐篇复述。5. 禁止无信息量的泛泛表述（如“取得了良好效果”）。6. 结尾给出 2025 年前后的真实研究趋势预测（不少于 3 点）。【结构必须为】- 引言- 方法分类与代表作 - 实验与评价总结- 趋势与挑战- 结论- 参考文献（不少于 12 篇）【输出风格】- 学术密度优先于篇幅- 禁止水文- 禁止空话套话"
)

def sanitize_filename(name):
    name = re.sub(r'[\\/*?:"<>|]', "_", name)
    return name[:80].strip()

def parse_failed_log(path):
    items = []
    if not os.path.exists(path):
        return items
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            m_id = re.search(r"id\s*=\s*(\d+)", line)
            m_field = re.search(r"field\s*=\s*(.*?)(?:,|$)", line)
            if m_id:
                fid = int(m_id.group(1))
                field_name = (m_field.group(1).strip() if m_field else "")
                items.append({"id": fid, "field": field_name})
    return items

def load_fields_map(path):
    fields = {}
    if os.path.exists(path):
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, list):
                    for it in data:
                        fid = it.get("id")
                        field = (it.get("field") or "").strip()
                        if isinstance(fid, int) and field:
                            fields[fid] = field
        except Exception:
            pass
    return fields

def get_survey_and_stats(prompt_text):
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": "你是一个严谨的科研助手，必须基于真实联网搜索生成学术综述。"},
            {"role": "user", "content": prompt_text}
        ],
        extra_body={"plugins": [{"id": "web", "engine": "exa", "max_results": 10}]}
    )
    message = response.choices[0].message
    content = (getattr(message, "content", "") or "").strip()
    usage = getattr(response, "usage", None)
    prompt_tokens = getattr(usage, "prompt_tokens", None) if usage else None
    completion_tokens = getattr(usage, "completion_tokens", None) if usage else None
    total_tokens = getattr(usage, "total_tokens", None) if usage else None
    if total_tokens is None and isinstance(prompt_tokens, int) and isinstance(completion_tokens, int):
        total_tokens = prompt_tokens + completion_tokens
    citations = 0
    annotations = getattr(message, "annotations", None)
    if annotations:
        for ann in annotations:
            if getattr(ann, "type", "") == "url_citation":
                citations += 1
    if citations == 0:
        citations = len(re.findall(r"https?://\S+", content))
    return {
        "content": content,
        "tokens_total": total_tokens,
        "tokens_prompt": prompt_tokens,
        "tokens_completion": completion_tokens,
        "references": citations
    }

def load_stats(path):
    if not os.path.exists(path):
        return []
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except Exception:
        return []

def upsert_stats(stats, entry):
    idx = None
    for i, it in enumerate(stats):
        if it.get("id") == entry.get("id"):
            idx = i
            break
    if idx is None:
        stats.append(entry)
    else:
        old = stats[idx]
        merged = dict(old)
        for k, v in entry.items():
            if k not in merged or merged[k] in (None, ""):
                merged[k] = v
        stats[idx] = merged
    stats.sort(key=lambda x: x.get("id", 0))
    return stats

def main():
    os.makedirs(MODEL_DIR, exist_ok=True)
    if not os.path.exists(STATS_PATH):
        with open(STATS_PATH, "w", encoding="utf-8") as f:
            json.dump([], f, ensure_ascii=False, indent=2)
    failed = parse_failed_log(FAILED_LOG_PATH)
    if not failed:
        print("没有需要补全的条目")
        return
    fields_map = load_fields_map(INPUT_JSON_PATH)
    for it in sorted(failed, key=lambda x: x["id"]):
        fid = it["id"]
        field_name = it["field"] or fields_map.get(fid) or ""
        if not field_name:
            print(f"跳过: id={fid} 缺少 field")
            continue
        safe_field_name = sanitize_filename(field_name)
        file_name = f"{fid:02d}_Survey_{safe_field_name}.md"
        file_path = os.path.join(MODEL_DIR, file_name)
        if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
            print(f"已存在: {file_name}，跳过生成")
            continue
        prompt = SURVEY_PROMPT_TEMPLATE.format(field=field_name)
        start = time.time()
        try:
            result = get_survey_and_stats(prompt)
        except Exception as e:
            print(f"生成失败: id={fid}, {e}")
            continue
        duration = time.time() - start
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(result["content"])
            print(f"已补全: {file_name}")
        except Exception as e:
            print(f"保存失败: id={fid}, {e}")
            continue
        entry = {
            "id": fid,
            "field": field_name,
            "md_path": file_path,
            "tokens_total": result.get("tokens_total"),
            "tokens_prompt": result.get("tokens_prompt"),
            "tokens_completion": result.get("tokens_completion"),
            "references": result.get("references", 0),
            "duration_sec": duration,
            "length_chars": len(result.get("content", "")),
        }
        current = load_stats(STATS_PATH)
        current = upsert_stats(current, entry)
        with open(STATS_PATH, "w", encoding="utf-8") as f:
            json.dump(current, f, ensure_ascii=False, indent=2)
        time.sleep(0.5)

if __name__ == "__main__":
    main()