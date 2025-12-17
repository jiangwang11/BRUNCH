# 大语言模型在推荐系统中的集成：2022–2025 研究综述

## 引言

推荐系统（Recommender Systems, RS）的核心挑战在于准确建模用户偏好并进行个性化预测。传统方法严重依赖协同过滤信号和浅层特征工程，在处理冷启动、数据稀疏和可解释性等问题上存在固有局限。自2022年起，大语言模型（Large Language Models, LLMs）凭借其强大的世界知识、语义理解与生成能力，为推荐系统研究注入了新范式。初期研究尝试直接将LLM作为端到端推荐器，但其高昂的推理成本和对协同信号的建模不足限制了实际应用。近期工作转向更为务实的“LLM增强”（LLM-augmented）范式，即利用LLM在离线阶段增强数据、特征或模型训练，而在线服务仍由高效的专用推荐模型完成。本文系统梳理2022至2025年间该领域的代表性工作，按其集成方式分类，并总结共性挑战与未来趋势。

## 方法分类与代表作

### 基于特征增强的范式

此类方法将LLM作为强大的特征提取器，为用户和物品生成富含语义的嵌入，以弥补传统ID嵌入的语义鸿沟。

*   **P5 (Geng et al., RecSys'22)** 首次将推荐任务统一为语言建模范式。它将用户-物品交互、物品描述等转化为自然语言序列，通过微调T5等预训练语言模型，直接生成推荐结果（如评分、解释）。该工作证明了LLM在捕捉用户意图和生成自然语言解释方面的潜力，但其端到端推理模式难以满足工业级低延迟需求。

*   **LLMRec (Wei et al., WSDM'24)** 提出一种图增强策略，利用LLM（如GPT-4）丰富用户-物品交互图。具体包括：1）增强用户-物品边的语义描述；2）深化物品节点属性理解；3）从文本角度剖析用户画像。通过引入去噪机制保证增强数据质量，该方法在多个基准数据集上显著优于仅使用原始交互数据的基线模型。

*   **FLIP (Wang et al., arXiv'23)** 旨在精细化对齐ID-based模型与LLM。它将表格数据（ID）和文本数据通过提示工程转化为统一文本，并在预训练阶段同时进行掩码语言建模（MLM）和掩码表格建模（MTM），辅以实例级对比学习（ICL）迫使两种模态的全局表示靠近。实验表明，该对齐策略使模型在CTR预测任务上显著优于简单拼接或独立使用任一模态的方法。

### 生成式推荐范式

此类方法将推荐视为一个序列到序列的生成任务，利用LLM的强大生成能力直接输出推荐结果或其语义表示。

*   **CALRec (Li et al., arXiv'24)** 提出一个两阶段微调框架，将LLM（PaLM-2）适配于序列推荐。它将用户历史交互中的物品属性（标题、类别等）转化为结构化文本，并让模型自回归生成下一个物品的描述。通过结合生成损失与对比损失，并采用BM25进行后处理去重，CALRec在Amazon数据集上超越了SASRec等SOTA序列模型。

*   **OneRec (Deng et al., arXiv'25)** 构建了一个端到端的生成式推荐框架，旨在替代传统的多阶段检索-排序架构。它采用平衡K-means（RQ-VAE变体）将视频内容编码为离散的语义token，并通过基于MoE（Mixture of Experts）的编码器-解码器结构，自回归生成完整的推荐会话。该方法在快手内部大规模数据集上实现了显著的在线指标提升。

*   **TIGER (Rajput et al., NeurIPS'23)** 引入“生成式检索”概念。它为每个物品分配一个从其内容特征派生的语义ID（如编码词组），而非传统的数字ID。推荐过程被建模为自回归解码下一个语义ID，这使模型能基于语义相似性进行零样本或少样本推荐，在处理新物品时展现出优越性能。

### 代理式交互范式

此类方法将LLM视为能够进行规划、记忆和工具调用的智能代理，实现动态、交互式的推荐。

*   **RecAgent (Wang et al., arXiv'23)** 提出一种新颖的推荐系统模拟范式。它将每个真实用户建模为一个由LLM驱动的自主代理，这些代理能在虚拟环境中自由交互、浏览、点击，并受社交等因素影响。该模拟器能大规模生成高质量、低成本的用户行为数据，为推荐算法的离线评估和训练提供了新途径。

*   **MACRec (Wang et al., arXiv'24)** 通过协调多个专家代理来完成推荐任务。该框架包含管理者、用户/物品分析员、反思者、搜索者和任务解释者等多个角色。这些代理通过协作，共同完成从信息分析、候选检索到生成解释和最终推荐的全过程，在多种推荐任务上展现出卓越性能。

*   **InteRecAgent (Huang et al., arXiv'23)** 将LLM作为“大脑”，而将传统推荐模型视为提供领域知识的“工具”。该代理能解析用户意图，并通过调用信息查询、项目检索和项目排名等核心工具来生成响应。这种架构有效结合了LLM的通用推理能力和推荐模型的专业知识。

### 可信与多模态推荐范式

针对多模态数据中的噪声问题和LLM的不确定性，近期研究开始关注可信推荐。

*   **Large-TR (Yan et al., 计算机学报'25)** 提出一种基于LLM的可信多模态推荐算法。它利用LLM卓越的自然语言理解能力，高效过滤多模态数据（如商品评价、图片）中的噪声，并设计了一种可信决策机制，动态评估推荐结果的不确定性。在4个公开数据集上的实验表明，其性能优于其他基线算法。

*   **DPRec (Li et al., 计算机学报'25)** 针对多模态推荐中特征失真、编码视角单一和对齐效果欠佳三大问题，提出一个双视角（记忆与扩展）多级跨模态对齐模型。该模型引入超图进行多级精准对齐，在3个真实数据集上验证了其有效性。

*   **FreLLM4Rec (Wang et al., arXiv'25)** 发现直接应用LLM会削弱固有的协同信号（即“协作频率衰减”现象）。为此，该方法从谱的角度平衡语义与协同信息，通过全局图低通滤波器（G-LPF）净化嵌入，并利用时间频率调制（TFM）逐层主动保留协同信号，在NDCG@10上相比最佳基线最高提升8.00%。

## 实验与评价总结

对上述工作的实验结果进行横向比较，可得出以下共性结论：
1.  **数据质量与冷启动**：利用LLM生成或增强的语义特征能有效缓解数据稀疏性问题，并在冷启动和长尾物品推荐场景中带来显著增益。
2.  **协同与语义的权衡**：纯粹依赖LLM语义信号的端到端生成式模型，在标准排序指标上常难以超越精心设计的、以协同信号为核心的专用序列模型（如SASRec）。最有效的方法往往是能巧妙融合两者优势的混合架构。
3.  **评估复杂性**：生成式和代理式方法的评估远比传统Top-N推荐复杂。除了NDCG、HR等指标外，还需引入多样性、新颖性、解释质量，甚至通过用户模拟或A/B测试来衡量其在真实交互场景中的价值。
4.  **推理成本**：几乎所有在在线服务中直接调用LLM的工作都面临推理延迟和成本的严峻挑战，这推动了“离线增强、在线高效”这一主流技术路线的形成。

## 趋势与挑战

基于对2022-2025年工作的分析，未来研究将聚焦于以下几个关键方向：
1.  **检索增强生成（RAG）与终身学习**：为解决LLM知识过时和无法处理超长用户行为序列的问题，RAG将成为主流。通过动态检索用户历史和外部知识库，LLM能保持对用户长期兴趣的精准理解和推荐的时效性。
2.  **多模态智能体**：下一代推荐代理将超越纯文本交互，发展为能够理解图像、视频、音频等多模态输入，并能生成多模态内容（如个性化广告图）的多模态智能体，提供沉浸式的推荐体验。
3.  **可信、公平与安全**：随着LLM在推荐中的深度集成，其固有的幻觉、偏见和安全风险（如被恶意提示攻击）将成为研究重点。构建具备内在可信决策机制、能主动检测和缓解偏见，并与人类价值观对齐的推荐系统是必然趋势。
4.  **统一的“搜索-推荐”基础模型**：工业界正朝着构建一个能同时处理搜索和推荐任务的统一基础模型方向发展（如Spotify、LinkedIn的实践），以简化系统架构并利用任务间的协同效应。

## 结论

2022至2025年，大语言模型与推荐系统的集成经历了从“直接替代”到“深度增强”的范式转变。早期探索验证了LLM在语义理解和生成方面的巨大潜力，而近期工作则更务实地聚焦于利用LLM解决推荐系统的核心痛点，如数据稀疏、冷启动和可解释性。通过特征增强、生成式建模、代理交互和可信多模态等多样化路径，研究者们正逐步构建更智能、更鲁棒、更人性化的下一代推荐系统。未来，随着RAG、多模态智能体和统一基础模型等方向的发展，LLM在推荐领域的价值将进一步释放，但其带来的可信、公平与安全挑战也亟待解决。

## 参考文献

1.  Geng, S., Liu, S., Fu, Z., Ge, Y., & Zhang, Y. (2022). Recommendation as Language Processing (RLP): Pre-train, Personalized Prompt, and Predict for Recommendation. In *Proceedings of the 16th ACM Conference on Recommender Systems (RecSys'22)*.
2.  Wei, W., Ren, X., Tang, J., Wang, Q., Su, L., Cheng, S., ... & Huang, C. (2024). LLMRec: Large Language Models with Graph Augmentation for Recommendation. In *Proceedings of the 17th ACM International Conference on Web Search and Data Mining (WSDM'24)*.
3.  Wang, H., et al. (2023). FLIP: Fine-Grained Alignment between ID-Based Models and Pretrained Language Models for CTR Prediction. *arXiv preprint arXiv:2310.19453*.
4.  Li, Y., Zhai, X., Alzantot, M., Yu, K., Vulic, I., Korhonen, A., & Hammad, M. (2024). CALRec: Contrastive Alignment of Generative LLMs for Sequential Recommendation. *arXiv preprint arXiv:2405.02429*.
5.  Deng, J., Wang, S., Cai, K., Ren, L., Hu, Q., Ding, W., ... & Zhou, G. (2025). OneRec: Unifying Retrieval and Ranking with Generative Recommendation and Iterative Preference Alignment. *arXiv preprint arXiv:2502.18965*.
6.  Rajput, S., Mehta, N., Singh, A., Keshavan, R. H., Vu, T., Heldt, L., ... & Tay, Y. (2023). Recommendation with Generative Retrieval. *Advances in Neural Information Processing Systems (NeurIPS'23)*, 36.
7.  Wang, L., Zhang, J., Chen, X., Lin, Y., Song, R., Zhao, W. X., & Wen, J. R. (2023). RecAgent: A Novel Recommender System Simulation Paradigm. *arXiv preprint arXiv:2310.10108*.
8.  Wang, Z., Yu, Y., Zheng, W., Ma, W., & Zhang, M. (2024). Multi-Agent Collaborative Framework for Recommender Systems. *arXiv preprint arXiv:2402.15235*.
9.  Huang, X., Lian, J., Lei, Y., Yao, J., Lian, D., & Xie, X. (2023). RecAI Agent: Integrating Large Language Models for Interactive Recommendation. *arXiv preprint arXiv:2308.16505*.
10. Yan, M., Xu, C., Huang, H., Zhao, W., & Guan, Z. (2025). 基于大语言模型的可信多模态推荐算法. *计算机学报*.
11. Li, Y., Yu, Y., Yu, Z., Si, Y., & Ye, Y. (2025). 基于大语言模型的双视角多级跨模态推荐. *计算机学报*.
12. Wang, M., He, Y., Xu, C., Zhu, Z., & Zhang, W. (2025). Beyond Semantic Understanding: Preserving Collaborative Frequency Components in LLM-based Recommendation. *arXiv preprint arXiv:2508.10312*.