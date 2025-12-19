import json

def calculate_averages(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        if isinstance(data, dict):
            data = [data]
        elif not isinstance(data, list):
            print("错误：JSON文件格式不符合预期（应为列表或字典）")
            return

        # --- 修正点 1: 变量名统一为 tokens_total ---
        tokens_total = 0
        total_duration_sec = 0.0
        total_length_chars = 0
        count = 0

        for item in data:
            # 确保所有需要的字段都存在
            if all(key in item for key in ['tokens_total', 'duration_sec', 'length_chars']):
                # --- 修正点 2: 这里的变量名现在与上面一致了 ---
                tokens_total += item['tokens_total']
                total_duration_sec += item['duration_sec']
                total_length_chars += item['length_chars']
                count += 1

        if count == 0:
            print("未找到有效数据（字段缺失或列表为空）。")
            return

        # --- 修正点 3: 计算平均值时使用正确的变量 ---
        avg_tokens_total = tokens_total / count
        avg_duration_sec = total_duration_sec / count
        avg_length_chars = total_length_chars / count

        print(f"处理了 {count} 条数据。")
        print(f"平均 tokens_total: {avg_tokens_total:.2f}")
        print(f"平均 duration_sec: {avg_duration_sec:.4f}")
        print(f"平均 length_chars: {avg_length_chars:.2f}")

    except FileNotFoundError:
        print(f"错误：找不到文件 '{file_path}'")
    except json.JSONDecodeError:
        print("错误：JSON文件格式无效")
    except Exception as e:
        # 打印具体的错误信息，方便调试
        print(f"发生未知错误: {type(e).__name__}: {e}")

if __name__ == "__main__":
    calculate_averages('survey/x-ai_grok-deep_research/surveys_stats.json')