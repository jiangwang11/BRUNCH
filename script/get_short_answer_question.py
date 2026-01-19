import json
import re
import os


def process_benchmark_data():
    # 1. 定义文件路径
    input_file = 'openai_batch_output_filtered_finance.json'
    output_file = 'short_answer_finance.json'

    # 检查输入文件是否存在
    if not os.path.exists(input_file):
        print(f"错误：未找到文件 {input_file}")
        return

    print(f"正在读取文件: {input_file}...")

    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"读取JSON失败: {e}")
        return

    processed_data = []

    # 2. 遍历并处理每一条数据
    for entry in data:
        item_id = entry.get('id')
        question_text = entry.get('question', '')
        answer_text = entry.get('answer', '')

        # --- 步骤 A: 提取正确答案的字母 ---
        # 匹配 "答案：X" 或 "答案:X" 中的 X
        answer_match = re.search(r"答案[：:]\s*([A-E])", answer_text)
        if not answer_match:
            print(f"[ID: {item_id}] 警告: 无法解析答案格式 '{answer_text}'，跳过。")
            continue

        target_letter = answer_match.group(1)  # 例如 "D"

        # --- 步骤 B: 分离题干(Scenario) 和 选项 ---
        # 逻辑：找到第一个选项 "A." 的位置，前面即为题干
        # 正则含义：匹配换行符 + 可能的空格 + A + 点
        split_pattern = r"\n\s*A\."
        parts = re.split(split_pattern, question_text, maxsplit=1)

        if len(parts) < 2:
            print(f"[ID: {item_id}] 警告: 无法找到选项A的分界线，跳过。")
            continue

        # 处理题干：去除 "题干：" 前缀和首尾空格
        scenario_raw = parts[0]
        scenario = re.sub(r"^题干[：:]\s*", "", scenario_raw).strip()

        # --- 步骤 C: 提取正确选项对应的文本(Method) ---
        # 补回被切掉的 "A."，构成完整的选项部分字符串，方便后续查找
        options_text_block = "A." + parts[1]

        # 构造动态正则提取特定选项内容
        # 逻辑：找到 "Target." 开始，直到 "NextLetter." 或 字符串结束
        # (?:^|\n)  -> 行首或换行符开始
        # \s* -> 允许前置空格
        # {target}  -> 目标字母 (如 D)
        # \.        -> 字面量点
        # \s* -> 允许点后空格
        # (.*?)     -> 非贪婪捕获内容 (我们需要的部分)
        # (?=\n\s*[A-Z]\.|$|答案) -> 向前看：直到遇到下一个选项、字符串结束或答案标识

        method_pattern = re.compile(
            rf"(?:^|\n)\s*{target_letter}\.\s*(.*?)(?=\n\s*[A-Z]\.|$|答案)",
            re.DOTALL
        )

        method_match = method_pattern.search(options_text_block)

        if method_match:
            method_desc = method_match.group(1).strip()

            # 构建新的数据对象
            new_entry = {
                "id": item_id,
                "original_paper": entry.get('paper_name', 'Unknown'),
                "scenario": scenario,  # 提取出的场景描述（原题干）
                "method": method_desc,  # 提取出的正确方法描述
                "correct_option": target_letter
            }
            processed_data.append(new_entry)
        else:
            print(f"[ID: {item_id}] 警告: 无法在文本中找到选项 {target_letter} 的内容。")

    # 3. 保存结果
    print(f"处理完成，共生成 {len(processed_data)} 条有效数据。")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(processed_data, f, ensure_ascii=False, indent=2)

    print(f"文件已保存至: {output_file}")


if __name__ == "__main__":
    process_benchmark_data()