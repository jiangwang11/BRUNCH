import json


def calculate_averages(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # 如果JSON最外层是字典而不是列表，将其放入列表中处理
        if isinstance(data, dict):
            data = [data]
        elif not isinstance(data, list):
            print("错误：JSON文件格式不符合预期（应为列表或字典）")
            return

        total_tokens_completion = 0
        total_duration_sec = 0.0
        total_length_chars = 0
        count = 0

        for item in data:
            # 确保所有需要的字段都存在
            if all(key in item for key in ['tokens_completion', 'duration_sec', 'length_chars']):
                total_tokens_completion += item['tokens_completion']
                total_duration_sec += item['duration_sec']
                total_length_chars += item['length_chars']
                count += 1

        if count == 0:
            print("未找到有效数据。")
            return

        avg_tokens_completion = total_tokens_completion / count
        avg_duration_sec = total_duration_sec / count
        avg_length_chars = total_length_chars / count

        print(f"处理了 {count} 条数据。")
        print(f"平均 tokens_completion: {avg_tokens_completion:.2f}")
        print(f"平均 duration_sec: {avg_duration_sec:.4f}")
        print(f"平均 length_chars: {avg_length_chars:.2f}")

    except FileNotFoundError:
        print(f"错误：找不到文件 '{file_path}'")
    except json.JSONDecodeError:
        print("错误：JSON文件格式无效")
    except Exception as e:
        print(f"发生未知错误: {e}")


# 请将 'your_file.json' 替换为你的实际文件名
if __name__ == "__main__":
    calculate_averages('survey/qwen_qwen3-max_online/surveys_stats.json')