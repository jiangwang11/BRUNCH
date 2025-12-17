好的，遵照您的指示。作为一名严谨的科研助手，我将基于提供的真实网络搜索结果，生成一篇关于「图增强推荐系统」的学术综述。

### **「图增强推荐系统」学术综述 (2022–2025)**

---

#### **摘要**
本综述旨在系统性地梳理与总结 2022 年至 2025 年间图增强推荐系统（Graph-Enhanced Recommendation Systems）领域的关键进展。推荐系统中的数据，如用户-物品交互、社交关系与知识图谱，天然具有图结构。图神经网络（Graph Neural Networks, GNNs）因其强大的图表示学习能力，已成为该领域的主流范式。本文首先扼要介绍图增强推荐的背景与意义；其次，将近期代表性工作划分为四个主要类别：基于图神经网络的序列化推荐、融合知识图谱的图推荐、解耦与因果表征学习、以及大语言模型与图的融合，并对各类别下的核心论文进行深度剖析；接着，对这些研究的共性实验设置与评价结论进行归纳；最后，基于当前研究前沿，展望未来三至五年的主要研究趋势与挑战。

---

### **1. 引言**

随着信息技术的飞速发展，信息过载已成为用户面临的普遍难题。推荐系统通过对用户偏好和物品属性进行建模，主动筛选并呈现个性化内容，有效缓解了这一问题，并已成为电子商务、社交媒体等诸多在线服务的核心组件 [hub.baai.ac.cn](https://hub.baai.ac.cn/view/20524)。

传统推荐算法，如协同过滤（CF）和矩阵分解（MF），虽然在早期取得了成功，但在处理数据稀疏性与复杂高阶关系时能力有限。深度学习模型的引入，尤其是图神经网络（GNNs）的兴起，为推荐系统带来了范式革新。GNN 能够直接在图结构数据上进行端到端的学习，有效捕捉用户与物品之间的高阶、复杂依赖关系，从而学习到更具表达力的用户与物品嵌入向量 [hub.baai.ac.cn](https://hub.baai.ac.cn/view/20524)。

2022 年至 2025 年，图增强推荐系统的研究呈现出多元化和深度融合的趋势。研究者不仅致力于优化 GNN 自身在推荐任务中的架构，更开始探索其与序列化建模、知识图谱、因果推断以及大语言模型（LLMs）的深度结合。本综述旨在对这一时期的代表性工作进行归纳与分析，以揭示领域内的关键技术演进和未来发展方向。

### **2. 方法分类与代表作**

#### **2.1 基于图神经网络的序列化推荐 (Sequential Recommendation with GNNs)**

序列化推荐旨在根据用户的历史行为序列预测其下一个交互的物品。GNN 被广泛用于构建物品之间的转移图或会话图，以捕捉序列中的复杂依赖关系。

*   **DiffuRec (2023)** [zhuanzhi.ai](https://zhuanzhi.ai/paper/2076b6c8019d906d1eedf566c952b629)
    *   **研究问题**：传统的序列推荐模型使用固定的物品向量，难以捕捉物品的多个潜在方面和用户兴趣的不确定性。
    *   **核心方法**：该研究首次将扩散模型（Diffusion Model）引入序列推荐。DiffuRec 将物品表示为分布而非固定向量，通过前向过程（向目标物品嵌入中注入高斯噪声）和反向过程（基于历史序列去噪以重构目标物品表示）来学习。这种方法能够对用户偏好的不确定性进行建模。
    *   **关键实验结论**：通过将物品表示为分布，DiffuRec 能够更好地捕捉用户兴趣的多样性，在四个公开数据集上的表现显著优于包括 SASRec 在内的强基线模型。

*   **FEARec (SIGIR 2023)** [zhuanzhi.ai](https://www.zhuanzhi.ai/paper/86c0da56bb58893ad1add80a353a6f14)
    *   **研究问题**：基于自注意力机制的序列推荐模型本质上是低通滤波器，难以捕捉用户行为序列中的高频信号（如周期性兴趣）。
    *   **核心方法**：FEARec 提出了一种频率增强的混合注意力网络。它将视角从时域转换到频域，通过改进的自注意力机制同时学习低频和高频信息。此外，模型设计了频域内的自相关机制来显式地捕捉用户行为的周期性特征。
    *   **关键实验结论**：实验表明，通过在频域中建模，FEARec 能够有效捕捉到时域中被忽略的周期性模式，其性能显著超越了仅在时域建模的先进方法。

*   **工业界异构图GNN应用 (2025)** [blog.csdn.net](https://blog.csdn.net/qdwd888/article/details/124589210)
    *   **研究问题**：在工业级下拉推荐场景中，仅加长用户行为序列对历史行为稀疏的非活跃用户和长尾查询（Query）的推荐效果提升有限。
    *   **核心方法**：该工作构建了一个包含四种关系（q-q, i-i, q-i, i-q）的异构图，并应用 GNN 学习邻居信息作为补充。研究探索了不同的邻居信息融合方式（特征拼接 vs. 独立序列），并设计了层次化注意力机制来区分不同邻居的重要性。
    *   **关键实验结论**：引入 GNN 建模的邻居信息，能够有效缓解数据稀疏问题，在非活跃用户和长尾查询上的 AUC 获得显著提升。实验证明，将邻居信息作为独立的上下文序列输入模型，效果优于简单的特征拼接。

#### **2.2 融合知识图谱的图推荐 (Knowledge Graph-Enhanced Recommendation)**

知识图谱（KGs）作为包含丰富实体与关系的辅助信息，被用于缓解数据稀疏性与冷启动问题，并增强推荐的可解释性。

*   **MKAFG (2025)** [blog.csdn.net](https://blog.csdn.net/wargzn_/article/details/124139980)
    *   **研究问题**：现有的知识图谱推荐模型或未能充分利用特征间的低阶交互，或使用的深度模型不完全适用于图结构数据。
    *   **核心方法**：该研究提出了一个名为 MKAFG 的多任务学习框架。其推荐模块结合了注意力因子分解机（AFM）和深度神经网络（DNN），分别捕捉低阶和高阶特征交互。其知识嵌入模块则采用图卷积网络（GCN）学习知识图谱的表示，并通过交叉压缩单元实现两个模块的交替学习。
    *   **关键实验结论**：在 MovieLens-1M 数据集上的实验表明，通过结合 AFM、DNN 和 GCN，MKAFG 模型能够同时有效利用用户行为信息和知识图谱结构，性能优于主流的基线模型。

#### **2.3 解耦与因果表征学习 (Disentangled and Causal Representation Learning)**

该方向致力于学习用户意图或物品属性的解耦表示，以消除混淆因素（如流行度偏见）的干扰，挖掘推荐背后的因果关系。

*   **基于图生成过程的跨领域推荐 (2022)** [arocmag.cn](https://www.arocmag.cn/abs/2022.01.0015)
    *   **研究问题**：在跨领域推荐中，暴力迁移的领域不变特征往往耦合了领域特定的结构信息，导致“错配”现象，且现有方法忽略了图数据中的噪声。
    *   **核心方法**：该工作引入了图数据的因果生成过程假设，将观测数据视为由领域特征、语义特征和噪声三类独立的隐变量生成。通过变分推断等方法解耦这些隐变量，并仅使用与领域无关的“语义特征隐变量”进行推荐，以实现领域不变的偏好建模。
    *   **关键实验结论**：通过因果解耦，模型能有效分离出用户的纯粹兴趣，减轻了领域偏移和数据噪声的负面影响，在多个公开的跨领域推荐数据集上取得了当时的最佳效果。

#### **2.4 大语言模型与图的融合 (Integration of LLMs and Graphs)**

这是近年来最引人注目的趋势。LLMs 凭借其强大的自然语言理解、常识推理和生成能力，为图推荐系统带来了新的可能性。

*   **LLMRec (WSDM 2024)** [developer.volcengine.com](https://developer.volcengine.com/articles/7391689837134708747)
    *   **研究问题**：推荐系统中的辅助信息（如多模态特征）往往存在噪声和质量不高的问题，且用户-物品交互数据稀疏。
    *   **核心方法**：LLMRec 框架利用 LLM 从两方面增强多模态 GNN：1）**结构增强**：基于用户的历史行为，利用 LLM 的推理能力生成高质量的正负样本对，扩充交互图；2）**特征增强**：利用 LLM 为用户和物品生成更丰富的文本描述与画像。同时，模型设计了剪枝和掩码自编码器（MAE）等去噪机制以保证增强数据的可靠性。
    *   **关键实验结论**：实验证明，经过 LLM 增强的交互数据和节点特征能够为 GNN 提供更丰富的监督信号和语义信息，有效提升了推荐性能，总开销仅几十美元。

*   **ETEGRec (SIGIR 2025)** [blog.csdn.net](https://blog.csdn.net/weixin_46351593/article/details/147838045)
    *   **研究问题**：生成式推荐模型通常采用两阶段范式：先训练物品标记器（Item Tokenizer），再训练生成器，两个阶段的割裂导致次优的物品表示。
    *   **核心方法**：ETEGRec 构建了一个端到端的可学习生成式推荐框架。它通过引入“序列-物品对齐”和“偏好-语义对齐”两种机制，协同优化基于 RQ-VAE 的物品标记器和基于 Transformer 的生成推荐器，使物品的离散化符号表示（Token）在训练过程中能自适应地向推荐任务的目标对齐。
    *   **关键实验结论**：端到端的联合训练使得物品 Token 表示同时蕴含了语义信息与推荐任务所需的协同信号，提升了生成式推荐的准确性。

*   **DRG (2025)** [blog.csdn.net](https://blog.csdn.net/2301_80160362/article/details/154230718)
    *   **研究问题**：课程推荐场景存在严重的数据稀疏性，且 LLM 直接推荐时缺乏对课程先后逻辑等领域知识的理解。
    *   **核心方法**：提出双关系图（DRG）框架，利用 LLM 的语义推理能力并结合传统方法（协同过滤、聚类等），构建“课程-课程”关系图和“用户-课程”关系图。这两个增强后的图被用来生成高质量的候选课程，再交由 LLM 进行最终的排序和推荐。
    *   **关键实验结论**：该框架通过 LLM 增强图结构，有效缓解了数据稀疏问题。作为一个即插即用的框架，它可以显著提升传统模型和 LLM-based 模型的推荐性能。

### **3. 实验与评价总结**

*   **数据集与指标**：研究普遍在公开基准数据集（如 MovieLens, Netflix, Amazon, Yelp）和特定任务数据集（如 MOOCCube）上进行评测。评价指标主要遵循推荐系统的标准，包括用于评估排序准确性的 **Recall@K**, **NDCG@K**, **Precision@K**，以及用于评估点击率预测的 **AUC**。

*   **共性结论**：
    1.  **图结构建模的普适有效性**：消融实验一致表明，移除 GNN 模块或图结构信息会导致显著的性能下降，证明了显式建模用户-物品图、知识图谱或序列转移图的必要性和优越性。
    2.  **辅助信息的重要性**：无论是知识图谱、多模态内容还是由 LLM 生成的语义信息，都能有效缓解数据稀疏和冷启动问题，尤其是在非活跃用户和长尾物品上提升更为明显 [blog.csdn.net](https://blog.csdn.net/qdwd888/article/details/124589210)。
    3.  **异构性处理是关键**：直接聚合不同类型节点或边的信息可能效果不佳甚至产生负向影响。为不同类型的关系设计特定的聚合器或注意力机制是提升性能的关键 [blog.csdn.net](https://blog.csdn.net/qdwd888/article/details/124589210)。
    4.  **新范式的潜力**：基于生成、因果、LLM 的新方法相较于传统的 GNN 推荐模型，在特定任务（如跨领域、可解释性）和指标上展现出巨大潜力，代表了领域的前沿方向。

### **4. 趋势与挑战**

基于 2022-2025 年的研究，我们预测图增强推荐系统未来的发展将聚焦于以下几个方向：

1.  **统一范式：生成式推荐与图模型的深度融合**
    继 ETEGRec 等工作的探索，未来研究将不再满足于将 GNN 作为编码器，而是将图结构深度融入**生成过程**。这包括：利用图的拓扑结构指导或约束自回归生成器的解码路径，以生成更合理、多样且新颖的推荐序列；或将图的构建本身也视为生成任务的一部分，实现图结构与推荐任务的端到端联合生成与优化。

2.  **大语言模型作为知识增强与推理引擎**
    LLM 的角色将从“数据增强器”（如 LLMRec）进化为“**图推理引擎**”。未来的系统可能会利用 LLM 对图中的路径进行语义解释，为推荐结果提供自然语言理由。同时，LLM 将在零样本/少样本场景下发挥更大作用，通过理解新物品的文本描述直接将其融入现有知识图谱，或在没有交互数据的情况下推理出用户可能的新兴趣。其核心挑战在于控制 LLM 的“幻觉”和高昂的计算/API成本。

3.  **因果推断的普及化与鲁棒性提升**
    随着研究的深入，因果推断将从一个小众方向（如 [arocmag.cn](https://www.arocmag.cn/abs/2022.01.0015)）走向主流。研究者将更关注消除推荐数据中普遍存在的**偏见**（如曝光偏见、流行度偏见）。基于图的反事实推断将成为关键技术，即在图上模拟“如果用户当时看到了其他物品，他会点击吗？”，从而学习用户更本质的、不受展示策略影响的偏好，最终提升模型的鲁棒性和公平性。

### **5. 结论**

在 2022 年至 2025 年期间，图增强推荐系统领域取得了长足的进步。研究范式已从经典的 GNN 结构优化，扩展到与序列化建模、知识图谱、因果科学及大语言模型的深度融合。特别是 LLM 的引入，为解决数据稀疏、知识融合和可解释性等长期挑战提供了全新的、强有力的工具。未来的研究将朝着更智能、更鲁棒、更可信的生成式与因果增强推荐系统方向迈进。

---

### **6. 参考文献**

*   Cai, R., Wu, F., & Li, Z. (2022). Cross-domain recommendation under graph generation process. *Application Research of Computers*, *39*(8), 2333-2339. [arocmag.cn](https://www.arocmag.cn/abs/2022.01.0015)
*   Cheng, J., et al. (2025). 融合知识图谱和用户行为信息的个性化推荐算法研究. Blog post based on *Computer Science and Application*. [blog.csdn.net](https://blog.csdn.net/wargzn_/article/details/124139980)
*   Du, X., et al. (2023). Frequency Enhanced Hybrid Attention Network for Sequential Recommendation. *Proceedings of the 46th International ACM SIGIR Conference on Research and Development in Information Retrieval*. [zhuanzhi.ai](https://www.zhuanzhi.ai/paper/86c0da56bb58893ad1add80a353a6f14)
*   Gao, W., et al. (2020). A Survey of Graph Neural Networks for Recommender Systems: Challenges, Methods, and Directions. arXiv preprint. (Referenced in [hub.baai.ac.cn](https://hub.baai.ac.cn/view/20524))
*   Guo, Q., et al. (2022). A Survey on Knowledge Graph-based Recommender Systems. *IEEE Transactions on Knowledge and Data Engineering*. (Referenced in [hub.baai.ac.cn](https://hub.baai.ac.cn/view/20524))
*   Li, Z., Sun, A., & Li, C. (2023). DiffuRec: A Diffusion Model for Sequential Recommendation. arXiv preprint. [zhuanzhi.ai](https://zhuanzhi.ai/paper/2076b6c8019d906d1eedf566c952b629)
*   qdwd888 (2025). GNN在下拉推荐的应用. Technical Blog Post. [blog.csdn.net](https://blog.csdn.net/qdwd888/article/details/124589210)
*   Wang, X., et al. (2025). ETEGRec: Generative Recommender with End-to-End Learnable Item Tokenization. *Proceedings of the 48th International ACM SIGIR Conference*. [blog.csdn.net](https://blog.csdn.net/weixin_46351593/article/details/147838045)
*   Wang, X., et al. (2024). Enhancing High-order Interaction Awareness in LLM-based Recommender Model. *Proceedings of EMNLP 2024*. [zhuanzhi.ai](https://www.zhuanzhi.ai/paper/166fc4c8042cf427064f1b766f21f2d2)
*   Wei, W., et al. (2024). LLMRec: LLM-enhanced Multi-modal Graph-based Recommendation. *Proceedings of the 17th ACM International WSDM Conference*. [developer.volcengine.com](https://developer.volcengine.com/articles/7391689837134708747)
*   Wu, S., et al. (2022). Graph Neural Networks in Recommender Systems: A Survey. *ACM Computing Surveys*. (Referenced in [hub.baai.ac.cn](https://hub.baai.ac.cn/view/20524))
*   Anonymous Author. (2025). DRG: A dual relational graph framework for course recommendation. Technical Blog Post. [blog.csdn.net](https://blog.csdn.net/2301_80160362/article/details/154230718)