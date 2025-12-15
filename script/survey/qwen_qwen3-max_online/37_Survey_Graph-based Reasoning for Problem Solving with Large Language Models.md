# 基于图的大型语言模型推理方法综述（2022–2025）

## 引言

大型语言模型（LLMs）在复杂推理任务中常因缺乏结构化知识支撑而产生幻觉。为增强事实一致性与多跳推理能力，学界自 2022 年起系统探索将图结构（如知识图谱、文本属性图）融入 LLM 推理流程。不同于传统 RAG 仅检索孤立文本片段，图推理方法显式建模实体与关系间的拓扑依赖，通过引导 LLM 在图上进行结构化探索，实现更可控、可解释的推理过程。本文系统梳理 2022–2025 年该方向的代表性工作，按方法范式划分为图增强提示、图结构推理框架、多智能体协同探索三类，并总结实验范式、共性结论及未来趋势。

## 方法分类与代表作

### 图增强提示方法（Graph-Augmented Prompting）

该类方法通过在提示中注入图结构信息，引导 LLM 利用图拓扑进行链式推理。

**Graph Chain-of-Thought (Graph-CoT)** [^1] 针对传统 CoT 忽略文本间关联的问题，提出在图上迭代执行“LLM 推理–图交互–图执行”三步循环。在自建 GRBench 基准（涵盖 10 领域 1,740 个图推理问题）上，Graph-CoT 显著优于文本 RAG 与零样本基线，验证了显式图交互对多跳问答的必要性。

**G-Retriever** [^2] 将图问答建模为奖励收集斯坦纳树（Prize-Collecting Steiner Tree）优化问题，结合 GNN 编码图结构、LLM 生成答案并通过软提示微调。其在场景图、常识推理等任务上优于基线，且能处理远超 LLM 上下文窗口的大图，有效抑制幻觉。

**Harnessing LLMs via Adaptive Multi-Aspect Retrieval-Augmentation (Amar)** [^3] 针对 KGQA 中多源检索引入噪声的问题，提出自适应多方面检索框架：通过自对齐模块融合实体、关系、子图信息，并用相关性门控动态加权。在 WebQSP 与 CWQ 上达到 SOTA，Hit@1 提升 1.9%，证明精细的图信息融合优于粗粒度检索。

### 图结构化推理框架（Structured Graph Reasoning）

该类方法设计专用架构，将 LLM 与图算法深度耦合，实现端到端图推理。

**Grounding LLM Reasoning with Knowledge Graphs** [^4] 系统比较了 CoT、Tree-of-Thought (ToT)、Graph-of-Thought (GoT) 三种推理策略在 KG 上的表现。实验表明，基于代理（Agent）的 ToT 策略（探索多路径）在 GRBench 上性能显著优于 CoT，而 GoT 因合并机制不成熟未显优势，揭示了多路径探索对复杂图推理的价值。

**Graph-constrained Reasoning** [^5] 提出一种忠实推理框架，通过 LLM 生成候选路径后，用 KG 约束进行后验验证与修正。其在逻辑形式生成任务上优于直接生成方法，Hit@1 提升 6.6%，证明外部知识约束可有效校正 LLM 的逻辑错误。

**CRF (Collaborative Reasoning Framework)** [^6] 针对复杂 KGQA 中 RL 探索盲目与 LLM 幻觉问题，设计分层 RL-LLM 协同框架：高层策略检测约束类型（如 Filter、Aggregation），低层策略在 LLM 指导下进行路径推理。在 CWQ、PQ 等多跳数据集上显著超越纯 LLM 或 RL 方法，消融实验证明分层结构与 LLM 奖励对性能至关重要。

### 多智能体协同图探索

该类方法利用多智能体分工协作，动态适应图结构进行高效探索。

**Graph Counselor** [^7] 为克服现有 GraphRAG 信息聚合僵化的问题，提出多智能体协同框架：规划、思考、执行三类智能体通过自适应图信息提取模块（AGIEM）协同建模图结构，并动态调整提取策略。其在多个图推理任务上优于单智能体基线，验证了多智能体分工对自适应图探索的有效性。

### 基础方法与理论支撑

**Chain-of-Thought Prompting** [^8] 虽非专为图设计，但其开创性地证明 LLM 可通过生成中间推理步骤提升算术、符号、常识推理能力。该工作为后续 Graph-CoT 等图推理方法提供了核心思想基础，即显式推理链可激活 LLM 的潜在推理能力。

**融合知识图谱的大语言模型研究综述** [^9] 系统总结了 KG 与 LLM 融合的三阶段方法（预训练、架构改造、微调），指出 KG 可有效提升事实一致性与可解释性，但面临动态更新滞后、多模态对齐等挑战，为本领域研究提供宏观视角。

## 实验与评价总结

代表性工作普遍在以下方面达成共识：(1) **基准建设**：多数研究构建或采用专门图推理基准，如 GRBench [^1]、GraphQA [^2]，强调问题需依赖图拓扑而非孤立节点；(2) **评价指标**：除标准问答准确率（如 Hit@1）外，部分工作引入幻觉率 [^2]、推理路径忠实度 [^5] 等细粒度指标；(3) **共性结论**：a) 利用图结构信息（尤其多跳关系）可显著提升复杂问答性能；b) 动态、自适应的图探索策略（如多路径、分层决策）优于固定模式；c) LLM 与结构化知识（KG/GNN）的协同机制（如约束、奖励、多智能体）是抑制幻觉的关键；d) 方法在图规模增大时仍能保持或提升性能，展现良好扩展性。

## 趋势与挑战

基于 2024–2025 年最新研究，未来趋势包括：(1) **多模态图推理**：将视觉、文本等多模态信息融入图结构（如场景图、多模态KG），要求 LLM 具备跨模态图对齐与推理能力；(2) **动态与增量式融合**：解决 KG 静态性与 LLM 知识过时问题，发展可在线更新的轻量化图-LLM 融合架构；(3) **复杂推理验证**：超越简单问答，支持需图上规划、优化、因果推断等高阶任务，并建立可验证的推理过程；(4) **多智能体自主协作**：从预设角色转向智能体自主协商、分工与反思，实现更灵活的图探索。

## 结论

图结构为 LLM 提供了事实性与关系性的强约束，有效缓解了其在复杂推理中的幻觉问题。2022–2025 年的研究从提示增强、结构化框架到多智能体协同，逐步深化了 LLM 与图的融合机制。未来工作需在多模态、动态性、高阶推理等方向突破，以构建更鲁棒、可信的知识驱动推理系统。

## 参考文献

[^1]: Jin, B., et al. (2024). Graph Chain-of-Thought: Augmenting Large Language Models by Reasoning on Graphs. *arXiv preprint arXiv:2404.06347* [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/3b56ac1a-3171-493a-9b02-7cbc561ec664)
[^2]: He, X., et al. (2024). G-Retriever: Retrieval-Augmented Generation for Textual Graph Understanding and Question Answering. *arXiv preprint arXiv:2402.07630* [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/590a1a69-780b-4438-8348-62b9d72e683c)
[^3]: Xu, D., et al. (2024). Harnessing Large Language Models for Knowledge Graph Question Answering via Adaptive Multi-Aspect Retrieval-Augmentation. *arXiv preprint arXiv:2412.18537* [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/94455)
[^4]: Anonymous. (2025). Grounding LLM Reasoning with Knowledge Graphs. *arXiv preprint arXiv:2502.13247* [themoonlight.io](https://www.themoonlight.io/zh/review/grounding-llm-reasoning-with-knowledge-graphs)
[^5]: Anonymous. (2025). Graph-constrained Reasoning: Faithful Reasoning on Knowledge Graphs with Large Language Models. *arXiv preprint* [themoonlight.io](https://www.themoonlight.io/review/graph-constrained-reasoning-faithful-reasoning-on-knowledge-graphs-with-large-language-models)
[^6]: m0_59164520. (2025). 结合强化学习与大型语言模型的复杂问答协作推理框架. *COLING 2025*. [CSDN](https://blog.csdn.net/m0_59164520/article/details/148700060)
[^7]: Gao, J., et al. (2025). Graph Counselor: Adaptive Graph Exploration via Multi-Agent Synergy to Enhance LLM Reasoning. *arXiv preprint arXiv:2506.03939* [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/145892)
[^8]: Wei, J., et al. (2022). Chain-of-Thought Prompting Elicits Reasoning in Large Language Models. *NeurIPS*. [CSDN](https://blog.csdn.net/weixin_52185313/article/details/139926042)
[^9]: 曹荣荣, 等. (2025). 融合知识图谱的大语言模型研究综述. *计算机应用研究, 42*(8), 2255-2266. [arocmag.cn](https://www.arocmag.cn/abs/2024.12.0532)
[^10]: Xu, F., et al. (2025). Towards Large Reasoning Models: A Survey of Reinforced Reasoning with Large Language Models. *arXiv preprint arXiv:2501.09686* [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/100784)
[^11]: Anonymous. (2025). Thinking with Knowledge Graphs: Enhancing LLM Reasoning Through Structured Data. *arXiv preprint* [themoonlight.io](https://www.themoonlight.io/review/thinking-with-knowledge-graphs-enhancing-llm-reasoning-through-structured-data)
[^12]: Anonymous. (2025). Reasoning with Graphs: Structuring Implicit Knowledge to Enhance LLMs Reasoning. *arXiv preprint* [themoonlight.io](https://www.themoonlight.io/review/reasoning-with-graphs-structuring-implicit-knowledge-to-enhance-llms-reasoning)