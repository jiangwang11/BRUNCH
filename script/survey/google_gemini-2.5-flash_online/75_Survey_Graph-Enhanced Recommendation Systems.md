## Graph-Enhanced Recommendation Systems：2022-2025 年代表性工作综述

### 引言

推荐系统是解决信息过载、提升用户体验和促进平台增长的关键技术。传统推荐方法常面临数据稀疏性、冷启动、长尾问题以及复杂的用户-物品交互模式难以建模等挑战。近年来，图神经网络（GNN）凭借其卓越的图结构数据表示学习能力，在推荐系统中展现出巨大潜力。推荐系统中的用户-物品交互、社交关系、知识图谱、序列行为等信息本质上具有图结构，GNN 能够有效捕获这些高阶连接和协作信号，从而增强用户/物品表示并提升推荐性能。本综述旨在梳理 2022 年至 2025 年间 Graph-Enhanced Recommendation Systems 领域的代表性工作，总结其核心方法、关键结论，并探讨未来研究趋势与挑战。

### 方法分类与代表作

Graph-Enhanced Recommendation Systems 主要可分为以下几类：基于协同过滤的GNN推荐、基于序列推荐的GNN、基于知识图谱增强的GNN推荐以及结合大型语言模型（LLM）的图增强推荐等。

#### 1. 基于协同过滤的 GNN 推荐

这类方法直接将用户-物品交互建模为二部图，并利用 GNN 捕获高阶用户偏好和物品关联。

*   **LightGCN (He et al., SIGIR 2020)**
    *   **研究问题：** 图卷积网络在推荐系统中引入过多的非线性变换和特征转换操作可能导致性能下降和计算复杂度增加。
    *   **核心方法：** 提出 LightGCN，通过移除 GCN 中的非线性激活函数和特征变换操作，仅保留最核心的邻域聚合操作，简化模型结构。
    *   **关键实验结论：** 在多个基准数据集上超越了 NGCF 等复杂 GNN 模型，同时显著降低了训练和推理成本，证明了简化模型对协作过滤的有效性。

*   **Investigating Accuracy-Novelty Performance for Graph-based Collaborative Filtering (Zhao et al., SIGIR 2022)** \[fuxi.163.com](https://fuxi.163.com/database/346)
    *   **研究问题：** 现有的基于图的协同过滤模型常加剧流行度偏差，导致对热门物品的过度推荐，而对长尾物品关注不足。
    *   **核心方法：** 理论分析了 GNN 中对称邻域聚合导致流行度偏差的原因。提出了一种名为 r-AdjNorm 的简单插件，通过控制邻域聚合过程中的归一化强度，以权衡推荐准确性和新颖性。
    *   **关键实验结论：** 在不牺牲推荐准确性的前提下，显著提高了模型对新颖物品的推荐能力，有效缓解了流行度偏差。

*   **Less is More: Reweighting Important Spectral Graph Features for Recommendation (SIGIR 2022)** \[blog.csdn.net](https://blog.csdn.net/weixin\_41278720/article/details/125966910)
    *   **研究问题：** GCN 在推荐中如何促进邻域聚合的机制尚未被充分研究，且大部分图信息可能引入噪声。
    *   **核心方法：** 从谱域分析 GCN，发现仅少部分强调邻域平滑和差异的谱图特征有助于提升推荐准确性。提出图去噪编码器（GDE），充当带通滤波器，选择性捕获重要图特征并减轻过度平滑问题。
    *   **关键实验结论：** 该方法在多个真实世界数据集上性能优于现有技术，并实现了比 LightGCN 更快的训练速度，同时减轻了过度平滑问题。

#### 2. 基于序列推荐的 GNN

这类方法将用户行为序列建模为图结构，例如会话图或超图，以捕获物品间的转换模式和高阶依赖。

*   **An Attribute-Driven Mirroring Graph Network for Session-based Recommendation (SIGIR 2022)** \[blog.csdn.net](https://blog.csdn.net/weixin\_41278720/article/details/125966910)
    *   **研究问题：** 基于会话的推荐系统常受数据稀疏性困扰，且未充分利用物品的属性信息。
    *   **核心方法：** MGS 模型利用会话图和属性感知镜像图学习物品表示。通过迭代的双重细化机制在两类图之间传播信息，并引入对比学习策略指导属性感知模块的训练。
    *   **关键实验结论：** 在三个真实世界数据集上的实验表明，MGS 性能超越了多个先进模型，有效融合了属性信息来增强偏好估计。

*   **Multimodal long-tail micro-video recommendation based on graph neural networks (MLT-GNN) (Luo et al., 2025)** \[arocmag.cn](https://www.arocmag.cn/abs/2025.02.0058)
    *   **研究问题：** 现有GNN多模态微视频推荐算法对长尾项目节点信息有削弱作用。
    *   **核心方法：** 提出了偏好信息共享的概念，建模用户历史交互中头/尾项目节点的关联。从交互丰富的头项目节点中发现尾项目节点所需信息，并结合注意力机制进行信息弥补，缩小头尾项目节点差距。
    *   **关键实验结论：** 在 MovieLens 和 Tiktok 数据集上，该算法在 Recall、Precision 和 NDCG 指标上分别实现了至少 5.27%、3.18% 和 6.29% 的提升，有效改善了长尾项目节点对用户偏好预测的贡献度。

*   **MoGE: Graph Context Enhanced Multi-Task Recommendation Method (Zhou et al., 2023)** \[ejournal.org.cn](https://www.ejournal.org.cn/CN/10.12263/DZXB.20220964)
    *   **研究问题：** 未明确指出具体面对的挑战，但多任务推荐通常需解决子任务间关系及上下文信息利用问题。
    *   **核心方法：** 提出了基于图上下文增强的多任务推荐算法 MoGE。该方法利用图结构信息来增强不同推荐任务的上下文表示。
    *   **关键实验结论：** 实验结果验证了 MoGE 在多任务推荐场景中的有效性。

#### 3. 基于知识图谱增强的 GNN 推荐

这类方法利用知识图谱（KG）中丰富的语义关系作为辅助信息，通过 GNN 将其融入推荐模型，以缓解数据稀疏性和提高可解释性。

*   **KETCH: Knowledge Graph Enhanced Thread Recommendation in Healthcare Forums (SIGIR 2022)** \[blog.csdn.net](https://blog.csdn.net/weixin\_41278720/article/details/125966910)
    *   **研究问题：** 在线医疗健康论坛中的推荐受限于缺乏领域知识，难以准确捕获用户意图。
    *   **核心方法：** KETCH 利用医学知识图谱的附加信息指导文本嵌入，通过知识感知注意力机制，并采用消息传递机制捕获方案和请求级别的用户偏好。
    *   **关键实验结论：** 在三个真实世界的医学论坛数据集上，KETCH 性能显著优于现有先进方法，并能有效完成知识图谱并推广可信信息。

*   **Hybrid Transformer with Multi-level Fusion for Multimodal Knowledge Graph Completion (SIGIR 2022)** \[blog.csdn.net](https://blog.csdn.net/weixin\_41278720/article/details/125966910)
    *   **研究问题：** 多模态知识图谱（MKG）补全在不同任务和模态间需要灵活的模型架构，且并非所有图像/目标都与文本输入相关。
    *   **核心方法：** 提出具有多级融合的混合 Transformer，利用统一输入输出的混合 Transformer 架构。通过粗粒度前缀引导交互和细粒度相关感知融合模块集成视觉和文本表示。
    *   **关键实验结论：** 在多模态链接预测、关系抽取和命名实体识别等任务的四个数据集上，该方法取得了 SOTA 性能，验证了其在复杂多模态 MKG 补全中的普适性。

#### 4. 大型语言模型（LLM）与图增强的协同推荐

新兴趋势是将 LLM 强大的语义理解和推理能力与 GNN 的图结构建模优势相结合。

*   **LLMRec: Large Language Models with Graph Augmentation for Recommendation (Wei et al., 2023)** \[hub.baai.ac.cn](https://hub.baai.ac.cn/paper/c2e79d28-5734-44af-925f-59b307fa2009)
    *   **研究问题：** 推荐系统面临数据稀疏性、噪声、低质量辅助信息等挑战。
    *   **核心方法：** 提出 LLMRec 框架，通过三种基于 LLM 的图增强策略：强化用户-物品交互边缘、增强物品节点属性理解、从自然语言角度进行用户节点分析。同时开发去噪数据鲁棒性机制确保增强数据质量。
    *   **关键实验结论：** 在基准数据集上，基于 LLM 的增强方法优于现有技术，展示了其在解决稀疏隐式反馈和低质量辅助信息方面的有效性。

*   **Applications and Deployment of Large Language Model-Enhanced Knowledge Graph Recommender Algorithm in E-Commerce (Wang et al., 2025)** \[pdf.hanspub.org](https://pdf.hanspub.org/ecl_2317091.pdf)
    *   **研究问题：** 传统知识图谱推荐方法存在知识缺失、语义不完整、计算冗余以及缺乏对自然语言隐含语义的深度理解。
    *   **核心方法：** 提出 KGLM 框架，利用 LLM 对物品的本地知识子图进行自然语言理解与语义建模，生成高质量表示。通过提示构造的图语言建模机制增强图结构语义，并引入多粒度语义聚合策略。
    *   **关键实验结论：** 在电商场景下，KGLM 在 Recall@k 和 NDCG@k 指标上显著优于多个基线模型，有效缓解了图谱稀疏与冷启动问题，提升了推荐系统的泛化性能与语义可解释性。

*   **Enhancing High-order Interaction Awareness in LLM-based Recommender Model (Wang et al., 2024)** \[zhuanzhi.ai](https://www.zhuanzhi.ai/paper/166fc4c8042cf427064f1b766f21f2d2)
    *   **研究问题：** 现有基于 LLM 的推荐模型忽视或未能有效建模用户-物品高阶交互。
    *   **核心方法：** 提出 ELMRec 模型，通过增强全词嵌入显著提升 LLM 对图构建交互的理解，无需图预训练。同时解决 LLM 倾向于基于早期交互而非近期交互进行推荐的问题，提出重排序方案。
    *   **关键实验结论：** 在直接推荐和序列推荐任务中，ELMRec 性能优于 SOTA 方法，验证了其提升高阶交互感知能力和解决交互时序偏差的有效性。

#### 5. 基于对比学习的图增强推荐

这类方法结合对比学习，通过最大化正样本对的相似度、最小化负样本对的相似度来学习鲁棒的图表示。

*   **Graph Contrastive Learning for Recommendation (SIGIR 2022)** \[blog.csdn.net](https://blog.csdn.net/weixin\_41278720/article/details/125966910)
    *   **研究问题：** 推荐系统中隐式反馈数据的稀疏性及噪声影响表示学习质量。
    *   **核心方法：** 提出 KGCL 模型，利用知识图谱信息进行图数据增强，并通过对比学习框架提升用户和物品表示的质量。
    *   **关键实验结论：** 在知识图谱增强推荐任务中，该方法有效提高了推荐性能，并学习到更鲁棒的用户/物品表示。

*   **Self-Augmented Recommendation with Hypergraph Contrastive Collaborative Filtering (SIGIR 2022)** \[blog.csdn.net](https://blog.csdn.net/weixin\_41278720/article/details/125966910)
    *   **研究问题：** 传统的协同过滤 GNN 模型难以捕获高阶用户-物品交互，且容易受到数据噪声影响。
    *   **核心方法：** 提出 HCCF 模型，通过超图构建方式捕获复杂的协作信号，并结合自增强对比协同过滤框架，学习更鲁棒的表示。
    *   **关键实验结论：** 在多个数据集上性能优于传统 GNN 推荐模型，证明了超图建模和对比学习在增强协作过滤中的有效性。

*   **基于梯度感知图增强的图对比学习推荐算法 (Hu et al., 2025)** \[arocmag.cn](https://www.arocmag.cn/abs/2025.05.0172)
    *   **研究问题：** 基于图对比学习的推荐模型中，随机增强方法易导致语义信息丢失和流行性偏差。
    *   **核心方法：** 提出 GAA 算法，引入梯度感知图增强，利用梯度信息指导图增强策略生成对比视图。通过难负样本挖掘提升语义信息辨别能力，并引入温度自适应模块保证模型稳定性。
    *   **关键实验结论：** 在 Yelp2018 等三个公开数据集上，Alibaba-iFashion 数据集上的 Recall@K 和 NDCG@K 较最优基准模型分别提高了 7.94% 和 5.82%，验证了其在缓解语义信息丢失和流行性偏差方面的有效性。

### 实验与评价总结

Graph-Enhanced Recommendation Systems 的有效性普遍通过在各类公开基准数据集（如 MovieLens、Amazon、Yelp、Tiktok）上进行评估来验证。常用的评价指标包括召回率（Recall@k）、归一化折损累计增益（NDCG@k）、精确率（Precision@k）等，这些指标共同衡量了推荐结果的相关性和排序质量。实验结果普遍表明，利用图结构信息和 GNN 模型可以有效地捕获用户-物品之间的高阶关系、序列模式以及语义联系，从而在一定程度上缓解数据稀疏性、冷启动、长尾问题和流行度偏差。通过引入注意力机制、多跳传播、自监督学习、对比学习以及与大型语言模型的结合，模型的表示能力和泛化性均有所提升。

### 趋势与挑战

2025 年前后及未来的研究趋势将集中在以下几个方面：

1.  **大语言模型（LLM）与图神经网络（GNN）的深度融合：** LLM 的强大语义理解和推理能力与 GNN 的图结构建模优势相结合，将成为主流研究方向。挑战在于如何有效融合两种模型的不同模态信息，平衡计算成本与性能，以及解决 LLM 在推荐中可能引入的幻觉和偏差问题。
2.  **动态图与时序建模：** 真实世界的用户偏好和物品属性是动态变化的。如何有效地构建和学习动态图，捕获时序信息，并实现图表示的实时更新，是重要的研究方向。挑战包括动态图的存储、计算效率、演化模式的准确预测以及大规模动态图学习的可扩展性。
3.  **可解释性与鲁棒性：** 随着推荐系统在实际应用中的普及，其决策过程的透明度和对对抗性攻击的鲁棒性变得越来越重要。如何设计既能保持高性能，又能提供可解释性线索的图增强推荐模型，以及如何有效防御恶意用户和物品的攻击，是亟待解决的挑战。

### 结论

Graph-Enhanced Recommendation Systems 在过去几年取得了显著进展，特别是在利用 GNN 捕获复杂用户-物品交互模式、解决数据稀疏性和结合知识图谱方面。近期，大型语言模型与图模型的融合为推荐系统带来了新的突破。未来的研究将聚焦于 LLM 与 GNN 的深度融合、动态图建模以及可解释性和鲁棒性等方面，以期构建更智能、更高效、更可靠的推荐系统。

### 参考文献

*   [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/c2e79d28-5734-44af-925f-59b307fa2009) Wei, W., Ren, X., Tang, J., Wang, Q., Su, L., Cheng, S., Wang, J., Yin, D., & Huang, C. (2023). LLMRec: Large Language Models with Graph Augmentation for Recommendation. arXiv preprint arXiv:2309.02084.
*   [arocmag.cn](https://www.arocmag.cn/abs/2025.05.0172) Hu, J., Hu, X., & Li, H. (2025). 基于梯度感知图增强的图对比学习推荐算法. 《计算机应用研究》, 2025, 42(12).
*   [arocmag.cn](https://www.arocmag.cn/abs/2025.02.0058) Luo, C., You, J., Wan, X., & Li, X. (2025). 基于图神经网络的多模态长尾微视频推荐算法. 《计算机应用研究》, 2025, 42(11), 3363-3369.
*   [blog.csdn.net](https://blog.csdn.net/manongtuzi/article/details/144802910) Wu, S., et al. (2022). Graph Neural Networks in Recommender Systems: A Survey. ACM Computing Surveys, 55(4), 1-38. (This is a survey paper that covers works up to 2022, and the CSDN blog cites the ACM 2022 survey)
*   [blog.csdn.net](https://blog.csdn.net/weixin_41278720/article/details/125966910) He, X., et al. (2020). LightGCN: Simplifying and Powering Graph Convolution Network for Recommendation. SIGIR 2020. (Cited indirectly through SIGIR 2022 overview, but is a prominent work before 2022)
*   [blog.csdn.net](https://blog.csdn.net/weixin_41278720/article/details/125966910) Zhao, M., Wu, L., Liang, Y., Chen, L., Zhang, J., Deng, Q., Wang, K., Wu, R., Shen, X., & Lyu, T. (2022). Investigating Accuracy-Novelty Performance for Graph-based Collaborative Filtering. SIGIR 2022.
*   [blog.csdn.net](https://blog.csdn.net/weixin_41278720/article/details/125966910) An Attribute-Driven Mirroring Graph Network for Session-based Recommendation. SIGIR 2022.
*   [blog.csdn.net](https://blog.csdn.net/weixin_41278720/article/details/125966910) Less is More: Reweighting Important Spectral Graph Features for Recommendation. SIGIR 2022.
*   [blog.csdn.net](https://blog.csdn.net/weixin_41278720/article/details/125966910) KETCH: Knowledge Graph Enhanced Thread Recommendation in Healthcare Forums. SIGIR 2022.
*   [blog.csdn.net](https://blog.csdn.net/weixin_41278720/article/details/125966910) Hybrid Transformer with Multi-level Fusion for Multimodal Knowledge Graph Completion. SIGIR 2022.
*   [blog.csdn.net](https://blog.csdn.net/weixin_41278720/article/details/125966910) Graph Contrastive Learning for Recommendation. SIGIR 2022.
*   [blog.csdn.net](https://blog.csdn.net/weixin_41278720/article/details/125966910) Self-Augmented Recommendation with Hypergraph Contrastive Collaborative Filtering. SIGIR 2022.
*   [ejournal.org.cn](https://www.ejournal.org.cn/CN/10.12263/DZXB.20220964) Zhou, J., Hu, B., Zhang, Z., & Chen, C. (2023). MoGE: Graph Context Enhanced Multi-Task Recommendation Method. 《电子学报》, 51(11), 3377-3387.
*   [pdf.hanspub.org](https://pdf.hanspub.org/ecl_2317091.pdf) Wang, Y., Zhang, W., & Li, Z. (2025). 大语言模型增强的知识图谱推荐算法在电子商务中的应用与推广. 《电子商务评论》, 14(11), 2640-2651.
*   [zhuanzhi.ai](https://www.zhuanzhi.ai/paper/166fc4c8042cf427064f1b766f21f2d2) Wang, X., Cui, J., Fukumoto, F., & Suzuki, Y. (2024). Enhancing High-order Interaction Awareness in LLM-based Recommender Model. EMNLP 2024.