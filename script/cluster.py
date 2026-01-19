import json
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction import text
from sklearn.cluster import KMeans
import os

# ================= 配置区域 =================
INPUT_FILE = 'paper_fields_output_finance.json'  # 请确保这里是你翻译好的英文数据文件
OUTPUT_FILE = 'clustered_result_finance.json'
NUM_CLUSTERS = 10

# --- 核心改进点：自定义学术停用词表 ---
# 这些词在AI论文中太常见，没有区分度。如果不剔除，聚类结果就会模糊。
ACADEMIC_STOP_WORDS = [
    # 论文常用套话
    'paper', 'proposed', 'method', 'approach', 'based', 'using', 'via',
    'study', 'analysis', 'results', 'model', 'algorithm', 'system', 'technique',
    'performance', 'application', 'framework', 'process', 'new', 'time', 'research',
    'review', 'state', 'art', 'survey',

    # 过于宽泛的AI词汇 (剔除它们，算法就会去找更具体的词)
    'learning', 'deep', 'data', 'artificial', 'intelligence', 'network', 'neural',
    'machine', 'models'
]


# ===========================================

def perform_clustering_and_grouping():
    # 1. 读取数据
    if not os.path.exists(INPUT_FILE):
        print(f"错误：找不到文件 {INPUT_FILE}")
        return

    print(f"正在读取文件: {INPUT_FILE}...")

    try:
        with open(INPUT_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
        df = pd.DataFrame(data)

        # 确保有 field 字段
        if 'field' not in df.columns:
            print("错误：数据中缺少 'field' 字段")
            return

    except Exception as e:
        print(f"读取或解析文件失败: {e}")
        return

    print(f"成功加载 {len(df)} 条数据，开始特征工程处理...")

    # 2. 特征提取 (TF-IDF) - 针对模糊地带的强力优化
    # 合并 sklearn 自带的英文停用词 + 我们自定义的学术停用词
    my_stop_words = list(text.ENGLISH_STOP_WORDS.union(ACADEMIC_STOP_WORDS))

    vectorizer = TfidfVectorizer(
        stop_words=my_stop_words,
        max_df=0.5,  # 【改进】如果一个词在50%以上的论文里出现，直接忽略
        min_df=2,  # 【改进】只出现一次的孤词，忽略
        ngram_range=(1, 2)  # 【改进】同时识别单词和词组 (例如能识别 "Genetic Algorithm")
    )

    # 假设你已经手动翻译好了，这里直接用 'field' 列
    try:
        X = vectorizer.fit_transform(df['field'])
    except ValueError:
        print("错误：生成特征矩阵失败，请检查数据是否包含有效的英文文本。")
        return

    # 3. K-Means 聚类
    print(f"特征提取完成，开始聚类 (K={NUM_CLUSTERS})...")
    kmeans = KMeans(n_clusters=NUM_CLUSTERS, random_state=42, n_init=10)
    kmeans.fit(X)

    df['cluster_id'] = kmeans.labels_

    # 4. 生成结果
    result_dict = {}
    print("正在生成类别名称并整理数据...")

    order_centroids = kmeans.cluster_centers_.argsort()[:, ::-1]
    terms = vectorizer.get_feature_names_out()

    for i in range(NUM_CLUSTERS):
        # --- 自动命名优化 ---
        # 取前3个关键词
        top_terms = [terms[ind] for ind in order_centroids[i, :3]]

        # 将关键词拼接成标题格式 (首字母大写)
        category_name = " ".join(top_terms).title()

        # 防止重名
        if category_name in result_dict:
            category_name = f"{category_name} ({i})"

        # 获取数据
        cluster_data = df[df['cluster_id'] == i]
        items = cluster_data[['id', 'field']].to_dict(orient='records')

        result_dict[category_name] = items
        print(f"  -> 类别 '{category_name}': 包含 {len(items)} 篇论文")

    # 5. 保存
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(result_dict, f, ensure_ascii=False, indent=2)

    print(f"\n处理完成！结果已保存至: {OUTPUT_FILE}")


if __name__ == "__main__":
    perform_clustering_and_grouping()