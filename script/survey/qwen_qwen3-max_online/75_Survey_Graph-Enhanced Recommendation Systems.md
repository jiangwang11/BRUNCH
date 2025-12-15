# 图增强推荐系统研究综述（2022–2025）

## 引言

推荐系统长期面临数据稀疏性与冷启动两大核心挑战。2022年以来，图增强推荐系统（Graph-Enhanced Recommendation Systems）凭借其对用户–物品交互与辅助信息（如知识图谱、社交网络）的统一建模能力，成为主流研究范式。典型方法包括：基于异构信息网络（HIN）的路径建模、知识图谱增强的图神经网络（GNN）、以及近年来兴起的大语言模型（LLM）与图结构的融合。本文系统梳理2022–2025年间该领域的代表性工作，聚焦方法创新与实验验证，并对未来趋势进行研判。

## 方法分类与代表作

### 异构信息网络与元路径方法

**CKG-HAN**（于嘉玮 & 薛涛，*计算机系统应用*，2022）针对HAN模型无法利用高阶邻居信息的问题，提出融合协同知识图谱（CKG）的分层注意力网络。该方法首先通过元路径将CKG划分为多个同构子图，在节点注意力层聚合高阶邻居特征，再通过关系注意力层融合不同元路径信息。在MovieLens-1M上，其Precision@20与Recall@20分别比原HAN模型提升1.1%和1.2%。

**McHa**（Wang et al., *World Wide Web*, 2022）提出一种多阶段聚类分层注意力模型，通过先对用户和物品进行聚类再建模注意力，有效缓解了大规模图上的计算负担。该模型在多个公开数据集上验证了其在推荐准确性和效率上的平衡。

### 知识图谱与图神经网络方法

**KGBCN**（马汉达 & 胡志鹏，*计算机系统应用*，2024）针对KGCN仅从物品端建模的缺陷，提出双端知识感知图卷积网络。模型同时从用户和物品两端在知识图谱中采样邻居，并利用知识感知注意力机制提取特征，最后通过不同聚合方式融合。在Last.FM和Book-Crossing数据集上，其AUC指标分别比最优基线提升4.4%和1.5%。

**KR-GCN**（Ma et al., *ACM TOIS*, 2023）设计了一种知识感知的图卷积网络，通过双线性聚合机制显式地建模知识图谱中的高阶关系。该模型在保证可解释性的同时，显著提升了推荐准确性，尤其在长尾物品推荐场景下表现突出。

### 大语言模型与图结构融合方法

**LLMRec**（Wei et al., 智源社区，2023）提出利用大语言模型（LLM）对推荐系统中的图结构进行三种增强：强化用户–物品交互边、增强物品节点属性理解、从自然语言角度分析用户节点。其核心创新在于通过LLM生成高质量的图结构增强数据，并设计去噪机制以保证数据可靠性。在多个基准数据集上的实验表明，该基于LLM的增强方法显著优于现有技术。

**KGLM**（王应文 et al., *E-Commerce Letters*, 2025）针对传统KG方法存在的知识缺失、语义不足与计算冗余问题，提出将LLM与知识图谱融合的框架。该模型将物品和用户的KG子图转化为自然语言提示，由LLM进行语义建模，生成高质量表示以替代多跳图传播。在ml-1m数据集上，其Recall@10和NDCG@10指标分别比KGAT提升9.5%和8.2%。

## 实验与评价总结

该领域工作普遍在MovieLens、Amazon、Last.FM、Book-Crossing等标准数据集上进行评估，主要采用Recall@K、NDCG@K、AUC、Precision@K等排序指标。共性结论如下：（1）引入知识图谱或社交网络等辅助信息能有效缓解数据稀疏和冷启动问题，尤其在长尾物品推荐上收益显著；（2）注意力机制与GNN的结合是主流架构，能够有效区分邻居节点的重要性；（3）近期将LLM与图结构融合的方法，在避免多跳传播带来的过平滑问题的同时，通过其强大的语义理解能力，显著提升了模型性能，尤其在AUC和NDCG等指标上优势明显。

## 趋势与挑战

基于现有文献，2025年及之后的研究趋势将集中在以下方向：
1.  **LLM与KG的深度协同**：当前工作多将LLM作为静态的“语义理解器”，未来研究将探索LLM与KG的动态交互与联合训练，以实现更深层次的知识推理与个性化。
2.  **动态与实时图推荐**：现有模型多基于静态图，难以适应用户兴趣漂移和知识图谱的实时更新。构建能高效处理动态图的推荐系统是下一阶段的核心挑战。
3.  **多模态与高阶关系建模**：将文本、图像等多模态信息与知识图谱、用户交互图进行统一建模，并设计更高效的算法来捕捉实体间的高阶、非线性关系，将成为提升模型表达能力的关键。

## 结论

2022–2025年间，图增强推荐系统从传统的异构网络和知识图谱方法，迅速演进到与大语言模型深度融合的新范式。这一演进不仅有效解决了数据稀疏、冷启动等经典难题，更通过LLM的通用语义能力，为推荐系统带来了更强的可解释性和泛化能力。未来，如何在保证效率的前提下，实现LLM、KG与动态用户行为的深度融合，将是推动该领域发展的核心动力。

## 参考文献

[1] 于嘉玮, 薛涛. 融合协同知识图谱高阶邻居特征的推荐模型. 计算机系统应用, 2022, 31(6): 252-258.
[2] Wang J, Shi Y, Li D, et al. McHa: a multistage clustering-based hierarchical attention model for knowledge graph-aware recommendation. World Wide Web, 2022, 25(3): 1103–1127.
[3] 马汉达, 胡志鹏. 基于知识图谱的双端知识感知图卷积推荐模型. 计算机系统应用, 2024, 33(1): 289-296.
[4] Ma T, Huang L, Lu Q, et al. KR-GCN: knowledge-aware reasoning with graph convolution network for explainable recommendation. ACM Transactions on Information Systems (TOIS), 2023, 41(1): 1-27.
[5] Wei W, Ren X, Tang J, et al. LLMRec: Large Language Models with Graph Augmentation for Recommendation. 智源社区, 2023.
[6] 王应文, 张伟, 李志文. 大语言模型增强的知识图谱推荐算法在电子商务中的应用与推广. 电子商务评论, 2025, 14(11): 2640-2651.
[7] Wu S, Tang Y, Zhuang Y, et al. Graph Neural Networks in Recommender Systems: A Survey. ACM Computing Surveys, 2022, 55(5): 1-37.
[8] Wang H, Zhao M, Xie X, et al. Knowledge graph convolutional networks for recommender systems. In Proceedings of the 2019 World Wide Web Conference, 2019: 3307–3313.
[9] Wang X, He X, Cao Y, et al. KGAT: Knowledge graph attention network for recommendation. In Proceedings of the 25th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining, 2019: 950–958.
[10] Yu X, Ren X, Sun Y, et al. Personalized entity recommendation: A heterogeneous information network approach. In Proceedings of the 7th ACM International Conference on Web Search and Data Mining, 2014: 283–292.
[11] Wang H, Zhang F, Wang J, et al. RippleNet: Propagating user preferences on the knowledge graph for recommender systems. In Proceedings of the 27th ACM International Conference on Information and Knowledge Management, 2018: 417–426.
[12] Ren X, Wei W, Xia L, et al. Representation Learning with Large Language Models for Recommendation. In Proceedings of the ACM Web Conference 2024, 2024: 3307–3313.