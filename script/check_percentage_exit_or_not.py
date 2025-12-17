import json
import os


def analyze_json_responses(file_path):
    # 初始化计数器
    stats = {
        "total": 0,
        "has_shi": 0,  # 包含 "是"
        "has_fou": 0,  # 包含 "否"
        "others": 0  # 都不包含
    }

    # 检查文件是否存在
    if not os.path.exists(file_path):
        print(f"错误: 找不到文件 '{file_path}'")
        return

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            # 假设 JSON 文件是一个列表结构，例如 [{}, {}, ...]
            data = json.load(f)

            # 如果文件本身不是列表（是单个对象），则转为列表处理
            if isinstance(data, dict):
                data = [data]

            for item in data:
                stats["total"] += 1

                # 获取 api_response，如果不存在则为空字符串
                response_text = item.get("api_response", "")

                # 截取前 5 个字符 (Python 切片，如果不足5个字符也不会报错)
                prefix = response_text[:5]

                # 逻辑判断：优先判断“是”，其次“否”
                # 注意：如果前5个字符同时包含“是”和“否”（例如“是否可行”），
                # 下面的写法会优先归类为“是”。如果需要互斥，请根据需求调整。
                if "是" in prefix:
                    stats["has_shi"] += 1
                elif "否" in prefix:
                    stats["has_fou"] += 1
                else:
                    stats["others"] += 1

        # --- 输出统计结果 ---
        print("-" * 30)
        print(f"文件分析: {file_path}")
        print(f"数据总条数: {stats['total']}")
        print("-" * 30)

        if stats["total"] > 0:
            shi_pct = (stats["has_shi"] / stats["total"]) * 100
            fou_pct = (stats["has_fou"] / stats["total"]) * 100
            other_pct = (stats["others"] / stats["total"]) * 100

            print(f"含 '是' (前5字符): {stats['has_shi']:<5} 占比: {shi_pct:.2f}%")
            print(f"含 '否' (前5字符): {stats['has_fou']:<5} 占比: {fou_pct:.2f}%")
            print(f"未匹配            : {stats['others']:<5} 占比: {other_pct:.2f}%")
        else:
            print("文件中没有数据。")
        print("-" * 30)

    except json.JSONDecodeError:
        print("错误: 文件格式不是有效的 JSON。")
    except Exception as e:
        print(f"发生未知错误: {e}")


# --- 配置 ---
# 在这里修改你的文件名
target_file = "survey_check_result_perplexity_sonar-deep-research.json"

if __name__ == "__main__":
    analyze_json_responses(target_file)