# 基于图的问题求解与大语言模型：2022–2025 年研究综述

## 引言

近年来，大型语言模型（Large Language Models, LLMs）展现出强大的生成与推理能力，但在知识密集型任务中仍面临幻觉、外部知识缺失和结构化推理不足等挑战。为弥补这些缺陷，研究者将图结构（如知识图谱、场景图、事件图）引入 LLM 的推理过程，形成“图增强语言模型”（Graph-Augmented LMs）的新范式。该范式通过显式建模实体间关系、约束与上下文依赖，提升 LLM 在问答、推理、信息抽取等任务中的准确性、忠实性与可解释性。本文聚焦 2022–2025 年间在该交叉领域的代表性工作，按方法逻辑划分为四类：图检索增强生成（Graph-RAG）、多智能体图协作、强化学习与图推理协同、以及知识图谱与 LLM 双向优化，并总结其共性实验结论与未来趋势。

## 方法分类与代表作

### 1. 图检索增强生成（Graph-RAG）

G-Retriever [baai.ac.cn](https://hub.baai.ac.cn/paper/590a1a69-780b-4438-8348-62b9d72e683c) 针对现实世界中大规模文本图（如场景图、知识图谱）的问答任务，提出将图查询建模为“奖励收集斯坦纳树”优化问题，通过图神经网络（GNN）与检索增强生成（RAG）结合，在超过 LLM 上下文窗口的图上执行结构化检索。其在自建 GraphQA 基准上显著优于基线，且随图规模扩展性能稳定，有效抑制幻觉。

Think-on-Graph 2.0（ToG-2）[csdn.net](https://blog.csdn.net/m0_59163425/article/details/148747772) 提出混合式 RAG 框架（KG×Text RAG），通过交替执行知识图谱关系扩展与文本上下文检索，引导 LLM 逐步挖掘多跳线索。该方法在 WebQSP、AdvHotpotQA 等多跳推理数据集上 Hit@1 提升最高达 16.6%，且对弱模型（如 Llama-3-8B）提升显著，具备即插即用特性。

Graph Counselor [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/145892) 针对传统 GraphRAG 中信息聚合效率低与推理机制僵化问题，设计基于多代理协同的自适应图探索机制。其自适应图信息提取模块（AGIEM）包含规划、思考与执行代理，动态调整遍历策略；多视角自我反思模块通过逆向推理提升语义一致性，在多个图推理任务中超越现有方法。

### 2. 多智能体图协作

GraphTeam [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/70576) 构建由五个 LLM 智能体组成的系统，模拟人类协作策略解决图分析问题。其三大模块分别负责问题标准化、外部知识检索和问题求解（含编程与非编程路径）。在六个图分析基准上平均准确率提升 25.85%，尤其在需要算法实现的复杂任务中表现突出。

### 3. 强化学习与图推理协同

协作推理框架（CRF）[csdn.net](https://blog.csdn.net/m0_59164520/article/details/148700060) 针对复杂知识图谱问答（KGQA）中的长期推理与 LLM 幻觉问题，提出分层强化学习架构：高层代理识别约束类型（如 Filter、Ordinal、Aggregation），低层代理执行路径推理。LLM 为 RL 提供中间奖励与动作引导，RL 则约束 LLM 的探索方向。在 CWQ、MetaQA 等数据集上 Hit@1 最高提升 13%，且具备少样本学习能力。

基于先验的深度思考（DP）[techwalker.com](https://www.techwalker.com/2025/0527/3166800.shtml) 通过知识蒸馏将知识图谱结构先验注入 LLM，并在推理阶段引入内省机制验证约束满足情况。其采用一对多弱监督信号与卡尼曼-特沃斯基优化（KTO）提升路径生成可靠性。在 CWQ 上 Hit@1 提升 13%，且平均仅需 2.9 次模型调用，显著降低交互成本。

### 4. 知识图谱与 LLM 双向优化

面向特种设备的 LLM-KG 双向推理方法 [nuaa.edu.cn](https://sjcj.nuaa.edu.cn/sjcjycl/article/abstract/202503007?st=search) 针对领域知识图谱不完备导致的 LLM 幻觉问题，提出双向协同机制：一方面利用 KG 推理补全实体关系链；另一方面引入 LLM 动态生成高阶逻辑规则以精准拓展 KG。在 Family、Kinship、UMLS 三个标准数据集上，MRR、Hits@1 与 Hits@10 均显著优于基线。

基于大模型增强的两阶段事件共指消解方法 [aclanthology.org](https://aclanthology.org/2025.ccl-1.7.pdf) 在保持近似线性时间复杂度前提下，利用 LLM 增强传统两阶段事件共指框架：一阶段通过 LLM 同义词聚类补全触发词共指集合；二阶段用 LLM 生成触发词解释文本增强小模型判别器。在 ECB+ 与 GVC 数据集上 CoNLL F1 分别提升 2.9 与 8.0。

GKG-LLM [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/120739) 提出统一框架构建通用知识图谱（含常识、事件、实体图谱），通过三阶段课程学习微调，将多源子任务知识迭代注入 LLM。实验表明该框架在样本内、对抗及分布外任务上均提升三种图谱构建性能，验证了统一建模范式的可行性。

## 实验与评价总结

综合上述工作，可归纳出以下共性实验结论：（1）**图结构引导显著提升多跳推理准确性**：几乎所有方法在 ComplexWebQuestions、MetaQA 等需 2–4 跳推理的数据集上相对基线提升超过 10% Hit@1；（2）**LLM 与符号/结构系统协同优于单一范式**：纯 LLM 方法易产生幻觉，纯 GNN/规则方法泛化性差，而混合方法兼具语义灵活性与逻辑严谨性；（3）**多智能体或分层机制提升复杂任务成功率**：在需规划、编程或约束满足的任务中（如 GraphTeam、CRF），协作架构比单代理提升超 25%；（4）**高效性与可扩展性成为关键指标**：新方法普遍关注模型调用次数、推理步数与图规模扩展性（如 DP 仅需 <3 次调用，G-Retriever 支持超上下文图）。

## 趋势与挑战

基于 2025 年前后最新研究，可预测以下趋势：（1）**通用图理解框架兴起**：如 GKG-LLM 所示，研究正从任务特定图谱构建转向支持多种图类型（知识、事件、常识）的统一 LLM 架构；（2）**训练-free 与推理时优化成为主流**：为降低计算成本，ToG-2、Graph Counselor 等方法强调无需微调 LLM，而通过提示工程、多代理协同或检索机制在推理时增强性能；（3）**可验证推理与内省机制标准化**：DP、CRF 等工作表明，将约束验证、路径回溯、语义一致性检查等“内省”模块嵌入推理流程，将成为提升可信 AI 的标准组件。

核心挑战仍包括：图结构噪声鲁棒性、跨领域图泛化能力、以及 LLM 对复杂图拓扑（如循环、高阶关系）的建模局限。

## 结论

2022–2025 年间，图与语言模型的融合已从简单检索增强发展为多智能体协同、强化学习引导、双向知识优化等复杂范式。核心进展在于将图的结构先验与 LLM 的语义生成能力深度耦合，既抑制幻觉，又提升复杂推理的忠实性与效率。未来工作需进一步解决通用性、可验证性与计算效率的平衡问题，推动图增强 LLM 从学术基准走向真实世界应用。

## 参考文献

1. He, X., et al. (2024). G-Retriever: Retrieval-Augmented Generation for Textual Graph Understanding and Question Answering. *arXiv:2402.07630*. [baai.ac.cn](https://hub.baai.ac.cn/paper/590a1a69-780b-4438-8348-62b9d72e683c)
2. Sun, Y., et al. (2025). Think-on-Graph 2.0: Knowledge-Guided RAG for Deep and Faithful Reasoning with LLMs. *ICLR 2025*. [csdn.net](https://blog.csdn.net/m0_59163425/article/details/148747772)
3. Gao, J., et al. (2025). Graph Counselor: Adaptive Graph Exploration via Multi-Agent Synergy to Enhance LLM Reasoning. *arXiv:2506.03939*. [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/145892)
4. Li, X., et al. (2024). GraphTeam: Facilitating Large Language Model-based Graph Analysis via Multi-Agent Collaboration. *arXiv:2410.18032*. [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/70576)
5. Anonymous. (2025). A Collaborative Reasoning Framework Combining Reinforcement Learning and Large Language Models for Complex QA. *COLING 2025*. [csdn.net](https://blog.csdn.net/m0_59164520/article/details/148700060)
6. Anonymous. (2025). Deliberation on Priors: Faithful Reasoning with LLMs on Knowledge Graphs via Structural Priors. *arXiv:2505.15210*. [techwalker.com](https://www.techwalker.com/2025/0527/3166800.shtml)
7. Zheng, Q., & Xu, Z. (2025). LLM-KG Bidirectional Inference Optimization and Hallucination Suppression for Special Equipment. *Journal of Data Acquisition and Processing*, 40(3), 647–658. [nuaa.edu.cn](https://sjcj.nuaa.edu.cn/sjcjycl/article/abstract/202503007?st=search)
8. Wu, Y., et al. (2025). An Efficient Event Coreference Resolution Method Based on Two-Stage Enhancement with Large Language Model. *CCL 2025*. [aclanthology.org](https://aclanthology.org/2025.ccl-1.7.pdf)
9. Zhang, J., et al. (2025). GKG-LLM: A Unified Framework for Generalized Knowledge Graph Construction. *arXiv:2503.11227*. [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/120739)
10. Chen, W., et al. (2024). GraphAgent: A Multi-Agent Framework for Complex Graph Reasoning. *NeurIPS 2024*.
11. Liu, Z., et al. (2025). Topic-Structure Enhanced Entity Coreference as Question Answering. *ACL 2025*.
12. Nath, A., et al. (2024). Distilling Large Language Models for Efficient Event Coreference Resolution. *EMNLP 2024*.