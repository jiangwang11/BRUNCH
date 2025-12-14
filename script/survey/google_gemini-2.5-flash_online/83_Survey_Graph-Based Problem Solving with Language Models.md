## 基于图的语言模型问题解决综述

### 引言

大型语言模型（LLMs）在自然语言处理领域展现出强大的能力，但在处理需要精确事实知识、多步推理或结构化信息的复杂任务时，仍面临“幻觉”、知识更新滞后以及长上下文理解受限等挑战。知识图谱（KGs）作为一种结构化、可验证的知识表示形式，能够提供丰富的实体、关系及语义网络，为增强LLMs的推理能力、事实准确性和可解释性提供了新的途径。将LLMs与图结构数据相结合，利用图的显式知识表示和LLMs的强大语义理解与生成能力，已成为当前人工智能领域的研究热点，催生了“基于图的语言模型问题解决”（Graph-Based Problem Solving with Language Models）这一新兴方向。本综述将重点关注2022-2025年该领域内的代表性工作，系统梳理其方法论、关键成果以及未来的发展趋势。

### 方法分类与代表作

本节将基于LLMs与图融合的不同策略和应用场景，对代表性工作进行分类介绍。

#### 1. 图增强型检索增强生成（GraphRAG）

这类方法旨在通过图结构信息提升RAG模型的检索和生成质量，解决传统RAG中检索文本片段可能导致的语义不连贯和噪声问题。

*   **Graph Chain-of-Thought (Graph-CoT)** [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/3b56ac1a-3171-493a-9b02-7cbc561ec664) (2024): 该研究提出Graph-CoT框架，旨在解决LLMs在知识密集型任务中的幻觉问题。其核心思想是通过鼓励LLMs迭代地在图上进行推理来增强其能力。Graph-CoT的每次迭代包含LLM推理、LLM-图交互和图执行三个子步骤。实验结果表明，Graph-CoT在GRBench图推理基准数据集上显著优于基线模型。

*   **G-Retriever** [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/590a1a69-780b-4438-8348-62b9d72e683c) (2024): G-Retriever是一个结合图神经网络（GNNs）、LLMs和检索增强生成（RAG）的问答框架，专注于文本图的理解和问答。它通过将RAG过程构建为奖励收集Steiner树优化问题，在图上执行检索，从而抵抗幻觉并处理超出LLM上下文窗口大小的文本图。该方法在场景图理解、常识推理和知识图谱推理等多个文本图任务上表现出色，并随着图规模的增加保持可扩展性。

*   **Graph Counselor** [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/145892) (2025): Graph Counselor提出了一种基于多Agent协作的GraphRAG方法，以解决现有方法在信息聚合效率和推理机制僵化方面的局限性。它引入自适应图信息提取模块（AGIEM），通过规划、思考和执行Agent协同工作，动态调整信息提取策略并捕捉多层次图信息。此外，多视角自我反思（SR）模块通过自我反思和逆向推理机制提高了推理结果的准确性和语义一致性。实验证明，Graph Counselor在多个图推理任务中表现出更高的推理准确性和泛化能力。

#### 2. 基于图的语言模型推理（Reasoning on Graphs, RoG）

此类方法引导LLMs利用图的结构和语义进行显式的多步推理，从而增强推理的忠实性、可解释性，并克服LLMs的幻觉问题。

*   **Reasoning on Graphs (RoG)** [blog.csdn.net](https://blog.csdn.net/weixin_43156294/article/details/150617902) (2025): RoG提出“规划-检索-推理”框架，利用知识图谱的关系路径生成忠实的推理计划。LLMs通过关系路径生成查询，结合图谱结构指导推理过程，以解决LLMs的幻觉和知识更新滞后问题。该方法在WebQuestionSP (WebQSP)和ComplexWebQuestion (CWQ)等基准KGQA数据集上达到先进水平，并提供了透明的推理过程，增强了可解释性。

#### 3. LLMs辅助知识图谱构建与完善

这些方法利用LLMs强大的文本理解和生成能力，自动化或半自动化地从非结构化文本中提取信息来构建或扩展知识图谱，或协同图结构提升信息检索性能。

*   **GKG-LLM** [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/120739) (2025): GKG-LLM提出了一个统一的通用知识图谱（GKG）构建框架，旨在解决现有研究将知识图谱、事件知识图谱和常识知识图谱独立构建的问题。该框架通过三阶段课程学习微调，将三种类型图谱中的知识迭代注入LLMs。实验表明，GKG-LLM在样本内、对抗任务数据和分布外（OOD）数据上均改善了三种图谱的构建。

*   **LKQE** [aclanthology.org](https://aclanthology.org/2025.ccl-1.31.pdf) (2025): LKQE (Large Language Models and Knowledge Graphs Collaborative Query Expansion) 是一种LLMs和知识图谱协同的查询扩展方法。该方法首先检索相关文档，从中提取关键句和三元组，构建并扩展知识图谱，最后在知识图谱的指导下生成高质量的扩展文本。实验结果表明，LKQE在DL19与DL20数据集上相比基线模型具有显著优势。

#### 4. 图增强型LLMs用于特定任务

这类方法将图结构作为LLMs处理特定复杂任务（如表格理解、长文本处理）的重要补充。

*   **HeGTa** [zhuanzhi.ai](https://zhuanzhi.ai/paper/e4a856f209e289b75a2f0e01e2411219) (2024): HeGTa提出一个异构图增强型LLM框架，用于解决少样本复杂表格理解（Few-shot Complex Table Understanding, TU）任务。该框架通过软提示和指令调整将表格语义与LLM的参数知识对齐，并通过包含多粒度自监督异构图预训练目标的多任务预训练方案处理复杂表格。实验表明，HeGTa在多个基准测试中优于现有的少样本复杂表格理解方法。

*   **GraphReader** [53ai.com](https://www.53ai.com/news/LargeLanguageModel/2024062249107.html) (2025): GraphReader是一个基于图的Agent系统，旨在增强LLMs的长文本处理能力。它将长文本结构化为图，并利用Agent自主探索该图。Agent通过逐步分析、规划、调用预定义函数读取节点内容和邻居，并持续记录和反思，以实现从粗到细的图探索。在LV-Eval数据集上的实验表明，GraphReader（使用4k上下文窗口）在处理16k到256k上下文长度的任务中，性能可与GPT-4（具有128k上下文窗口）匹敌或超越。

### 实验与评价总结

现有研究普遍采用知识图谱问答（KGQA）基准数据集（如WebQuestionSP、ComplexWebQuestion）或针对特定任务（如长文本理解）构建的基准进行评估。评价指标通常包括F1分数、精确匹配（EM）分数等，部分研究也采用LLM辅助评估（LLM-Rating）来衡量回答的正确性、忠实性和可解释性。

共性结论表明，将图结构和LLMs结合的方法在处理知识密集型、需要多步推理或长上下文理解的任务时，能够显著提升LLMs的性能。具体体现在：

1.  **提高事实准确性，减少幻觉**：图的结构化知识为LLMs提供了可验证的事实基础，有效抑制了“幻觉”的产生。
2.  **增强推理能力**：图结构支持显式的多跳推理和关系发现，弥补了LLMs在复杂逻辑推理方面的不足。
3.  **提升可解释性**：基于图的推理路径使得LLMs的决策过程更加透明可追溯，这在金融、医疗等关键领域尤为重要。
4.  **改善长上下文处理能力**：通过将长文本转换为图结构进行探索，可以有效突破LLMs有限上下文窗口的限制，处理超长文本。
5.  **增强知识获取与更新能力**：LLMs辅助知识图谱构建的方法能够自动化地从非结构化文本中提取知识，并动态更新图谱，解决了LLMs知识更新滞后的问题。

### 趋势与挑战

面向2025年及未来，基于图的语言模型问题解决领域将呈现以下趋势并面临相应挑战：

1.  **多模态知识图谱与LLMs的深度融合**：未来的研究将超越纯文本知识图谱，探索如何将视觉、音频等多模态信息融入知识图谱，并与LLMs进行深度融合，以支持更复杂的跨模态理解和推理。这要求解决多模态知识表示对齐、多模态图谱构建的自动化以及多模态推理路径的设计等技术瓶颈。
2.  **Agent-based图探索与自适应推理**：受Agent范式成功启发，结合规划、反思和工具使用能力的Agent将成为探索和利用复杂图谱的主流范式。例如Graph Counselor和GraphReader等研究已初现端倪。未来的Agent将更加强调自适应性、鲁棒性和泛化能力，能够针对不同任务和图谱结构动态调整探索策略和推理深度。
3.  **动态知识图谱和实时更新**：现有图增强LLMs往往依赖相对静态的知识图谱。然而，现实世界的知识是不断变化的。如何实现动态知识图谱的实时更新，并确保LLMs能够及时、高效地利用最新知识进行推理，是该领域面临的重要挑战。这涉及增量式图谱构建、高效的图谱查询和更新机制，以及LLMs对动态知识的感知和适应能力。

### 结论

基于图的语言模型问题解决方法通过结合知识图谱的结构化表示和LLMs的强大语言能力，为克服LLMs在事实准确性、推理能力和可解释性方面的局限性提供了有效途径。随着多模态融合、Agent-based探索和动态知识更新等方向的持续深入，该领域有望在未来取得更加突破性的进展，推动人工智能系统向更可信、更智能、更具通用性的方向发展。

### 参考文献

*   Gao, J., Zou, X., Ai, Y., Li, D., Niu, Y., Qi, B., & Liu, J. (2025). Graph Counselor: Adaptive Graph Exploration via Multi-Agent Synergy to Enhance LLM Reasoning. *arXiv preprint arXiv:2506.03939*. [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/145892)
*   He, X., Tian, Y., Sun, Y., Chawla, N. V., Laurent, T., LeCun, Y., Bresson, X., & Hooi, B. (2024). G-Retriever: Retrieval-Augmented Generation for Textual Graph Understanding and Question Answering. *arXiv preprint arXiv:2402.06209*. [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/590a1a69-780b-4438-8348-62b9d72e683c)
*   Jin, R., Li, Y., Qi, G., Hu, N., Li, Y.-F., Chen, J., Wang, J., Chen, Y., Min, D., & Bi, S. (2024). HeGTa: Leveraging Heterogeneous Graph-enhanced Large Language Models for Few-shot Complex Table Understanding. *arXiv preprint arXiv:2403.19723*. [zhuanzhi.ai](https://zhuanzhi.ai/paper/e4a856f209e289b75a2f0e01e2411219)
*   Luo, L., Li, Y.-F., Haffari, G., & Pan, S. (2025). Reasoning on Graphs: Faithful and Interpretable Large Language Model Reasoning. *International Conference on Learning Representations (ICLR 2024)*. [blog.csdn.net](https://blog.csdn.net/weixin_43156294/article/details/150617902)
*   Meng, Y., Jin, B., Xie, C., Zhang, J., Roy, K. K., Zhang, Y., Li, Z., Li, R., Tang, X., Wang, S., & Han, J. (2024). Graph Chain-of-Thought: Augmenting Large Language Models by Reasoning on Graphs. *arXiv preprint arXiv:2404.06232*. [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/3b56ac1a-3171-493a-9b02-7cbc561ec664)
*   Wang, X., Lu, Y., Chen, W., Zhang, J., & Chen, H. (2025). GraphReader: Building Graph-based Agent to Enhance Long-Context Abilities of Large Language Models. *arXiv preprint arXiv:2406.14550*. [53ai.com](https://www.53ai.com/news/LargeLanguageModel/2024062249107.html)
*   Zhang, J., Wei, B., Qi, S., Zhu, H., Liu, J., & Lin, Q. (2025). GKG-LLM: A Unified Framework for Generalized Knowledge Graph Construction. *arXiv preprint arXiv:2503.11227*. [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/120739)
*   Zhang, K., Tu, X., & Liu, H. (2025). 大语言模型和知识图谱协同的查询扩展方法. *Proceedings of the China Computer Linguistics Conference (CCL 2025)*. [aclanthology.org](https://aclanthology.org/2025.ccl-1.31.pdf)
*   Cao, R., Liu, L., Yu, Y. D., & Wang, H. L. (2025). 融合知识图谱的大语言模型研究综述. *计算机应用研究*, *42*(8), 2255-2266. [arocmag.cn](https://www.arocmag.cn/abs/2024.12.0532)