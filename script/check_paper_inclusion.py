import json
import os
import glob
import time
import httpx  # 确保安装了 pip install httpx
from dotenv import load_dotenv
from openai import OpenAI

# ================== 用户配置区域 (超参数) ==================

# 1. 这里填写 survey 文件夹下那个具体的模型文件夹名字
TARGET_SURVEY_DIR_NAME = "x-ai_grok-deep_research"

# 2. JSON 文件路径
JSON_FILE_PATH = "openai_batch_output.filtered.json"

# 3. 结果保存路径
OUTPUT_FILE_PATH = "survey_check_result_x-ai_grok-deep_research.json"

# 4. 测试数量限制 (0 或 None 为全量)
TEST_LIMIT = 0

# ================== API 基础配置 ==================

load_dotenv()

API_KEY = os.environ.get("API_KEY")
AHM_BASE_URL = "https://api.aihubmix.com/v1"
LLM_MODEL_NAME = "gpt-4.1-nano"

if not API_KEY:
    print("错误：未找到 API_KEY 环境变量。")
    exit(1)

# --- 关键修复开始 ---
# 1. 强制清空环境变量中的代理设置，防止干扰
os.environ["http_proxy"] = ""
os.environ["https_proxy"] = ""
os.environ["all_proxy"] = ""

try:
    print(f"正在初始化客户端 (直连模式)...")

    # 2. 创建自定义 HTTP 客户端
    # trust_env=False: 强制忽略系统代理
    # timeout=300.0: 给予 5 分钟的超长等待时间，防止长文分析超时
    http_client = httpx.Client(
        trust_env=False,
        timeout=300.0
    )

    client = OpenAI(
        api_key=API_KEY,
        base_url=AHM_BASE_URL,
        http_client=http_client,  # 注入自定义客户端
    )
except Exception as e:
    print(f"错误: 无法初始化 OpenAI 客户端。 {e}")
    exit(1)


# --- 关键修复结束 ---


# ================== 核心功能函数 ==================

def get_openai_completion(prompt_text: str, system_message: str = "你是一个有用的助手。") -> str:
    try:
        completion = client.chat.completions.create(
            model=LLM_MODEL_NAME,
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": prompt_text},
            ],
        )
        return (completion.choices[0].message.content or "").strip()
    except Exception as e:
        print(f"[API Error] {e}")
        # 如果是含有 'context length' 的错误，可以在这里做特殊处理
        return f"ERROR: {e}"


def check_paper_in_survey(paper_name: str, survey_content: str) -> str:
    # 截断过长的 Survey 内容
    # 建议先设置 50000 (约 30k tokens)，如果依然稳定，可尝试加到 80000
    max_chars = 50000
    truncated_content = survey_content[:max_chars]

    prompt = (
        f"下面是一篇 Survey（综述）文章的内容：\n\n"
        f"```markdown\n{truncated_content}\n```\n\n"
        f"========\n"
        f"任务：寻找这篇suvey中是否有“{paper_name}”这篇论文或者论文中主推的方法，"
        f"注意不要因为缩写而忽略。\n"
        f"请简短回答“是”或“否”，并简要说明理由（例如：找到了，在第几章节或上下文中提到了xxx）。"
    )
    return get_openai_completion(prompt, system_message="你是一个学术文献分析助手。")


def get_file_id(filename: str) -> int:
    try:
        prefix = filename.split('_')[0]
        return int(prefix)
    except (ValueError, IndexError):
        return -1


# ================== 主程序 ==================

def main():
    survey_root = "survey"
    target_dir = os.path.join(survey_root, TARGET_SURVEY_DIR_NAME)

    # 1. 预加载 JSON 数据
    if not os.path.exists(JSON_FILE_PATH):
        print(f"错误：找不到文件 {JSON_FILE_PATH}")
        return

    print("正在加载 JSON 数据建立索引...")
    with open(JSON_FILE_PATH, "r", encoding="utf-8") as f:
        json_data = json.load(f)

    id_to_paper_map = {}
    for item in json_data:
        try:
            pid = int(item.get("id"))
            pname = item.get("paper_name")
            if pname:
                id_to_paper_map[pid] = pname
        except (ValueError, TypeError):
            continue

    # 2. 获取文件
    if not os.path.exists(target_dir):
        print(f"错误：找不到 Survey 文件夹 {target_dir}")
        return

    all_files = glob.glob(os.path.join(target_dir, "*.md"))
    all_files.sort(key=lambda x: get_file_id(os.path.basename(x)))

    # 3. 数量限制
    if TEST_LIMIT and TEST_LIMIT > 0:
        print(f"⚠️  测试模式：仅处理前 {TEST_LIMIT} 个文件 (文件夹中共找到 {len(all_files)} 个)")
        process_files = all_files[:TEST_LIMIT]
    else:
        print(f"🚀 全量模式：处理所有 {len(all_files)} 个文件")
        process_files = all_files

    results = []
    print("-" * 30)

    # 4. 循环处理
    for file_path in process_files:
        file_name = os.path.basename(file_path)
        file_id = get_file_id(file_name)

        if file_id == -1:
            print(f"[跳过] 文件名格式无法解析 ID: {file_name}")
            continue

        paper_name = id_to_paper_map.get(file_id)

        if not paper_name:
            print(f"[ID: {file_id:02d}] ❌ JSON 中未找到对应 paper_name，跳过")
            continue

        print(f"[ID: {file_id:02d}] 正在检查... (Paper: {paper_name})")

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                survey_content = f.read()
        except Exception as e:
            print(f"  读取文件失败: {e}")
            continue

        # 调用 API
        start_time = time.time()
        response = check_paper_in_survey(paper_name, survey_content)
        elapsed = time.time() - start_time

        print(f"  -> 耗时: {elapsed:.1f}s | 模型回复: {response[:100]}...")  # 只打印前100字避免刷屏

        results.append({
            "id": file_id,
            "paper_name": paper_name,
            "survey_file": file_name,
            "api_response": response
        })

        # 适当休眠避免并发过高（虽然串行已经很安全了）
        time.sleep(1)

    # 5. 保存结果
    try:
        with open(OUTPUT_FILE_PATH, "w", encoding="utf-8") as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
        print(f"\n✅ 处理完成，结果已保存至: {OUTPUT_FILE_PATH}")
    except Exception as e:
        print(f"保存结果失败: {e}")


if __name__ == "__main__":
    main()