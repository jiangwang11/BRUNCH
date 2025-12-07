import json
import re

def remove_links(text):
    if not isinstance(text, str):
        return text

    # 1. 删除完整 Markdown 链接，包括锚文本本身：[xxx](http...)
    text = re.sub(r'\[[^\]]*\]\(http[s]?://[^)]+\)', '', text)

    # 2. 删除裸露 URL
    text = re.sub(r'http[s]?://\S+', '', text)

    return text

input_file = "openai_batch_output.json"
output_file = "openai_batch_output_clean.json"

with open(input_file, "r", encoding="utf-8") as f:
    data = json.load(f)

for item in data:
    for key in ["question", "raw_output"]:
        if key in item:
            item[key] = remove_links(item[key])

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("✔ 已完成：锚文本 + URL 均已删除，输出为", output_file)
