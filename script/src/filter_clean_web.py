import json
import re
import os

def remove_links(text):
    if not isinstance(text, str):
        return text

    # 1. 删除完整 Markdown 链接，包括锚文本本身：[xxx](http...)
    text = re.sub(r'\[[^\]]*\]\(http[s]?://[^)]+\)', '', text)

    # 2. 删除裸露 URL
    text = re.sub(r'http[s]?://\S+', '', text)

    return text

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    dataset_name = os.environ.get("DATASET_NAME", "social_science").strip() or "social_science"
    input_env = (os.environ.get("CLEAN_INPUT_JSON") or "").strip()
    output_env = (os.environ.get("CLEAN_OUTPUT_JSON") or "").strip()
    filter_output_name = os.environ.get("FILTER_OUTPUT_JSON", f"openai_batch_output_filtered_{dataset_name}.json")
    clean_output_name = output_env or os.environ.get("FIELDS_INPUT_JSON", "openai_batch_output_clean.json")
    candidate_inputs = []
    if input_env:
        candidate_inputs.append(input_env)
    candidate_inputs.extend([
        os.path.join(script_dir, filter_output_name),
        os.path.join(script_dir, "openai_batch_output.filtered.json"),
        os.path.join(script_dir, "openai_batch_output.json"),
    ])
    input_file = next((p for p in candidate_inputs if os.path.exists(p)), None)
    if not input_file:
        raise FileNotFoundError(f"未找到输入文件，候选路径: {candidate_inputs}")
    output_file = output_env or os.path.join(script_dir, clean_output_name)

    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    for item in data:
        for key in ["question", "raw_output"]:
            if key in item:
                item[key] = remove_links(item[key])

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("✔ 已完成：锚文本 + URL 均已删除")
    print("输入：", input_file)
    print("输出：", output_file)


if __name__ == "__main__":
    main()
