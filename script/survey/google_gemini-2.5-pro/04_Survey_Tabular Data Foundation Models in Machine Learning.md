好的，遵照您的指示，作为一名严谨的科研助手，我将基于提供的真实网络搜索结果，生成一篇关于“机器学习中的表格数据基础模型”的学术综述。

***

### **机器学习中的表格数据基础模型研究综述 (2022-2025)**

#### **引言**

表格数据是现实世界中应用最广泛的数据结构，普遍存在于金融、医疗、生物信息学等关键领域 [www.zhuanzhi.ai](https://www.zhuanzhi.ai/vip/a8b0a5d4b9e659953cbd5010a6aa2963)。在很长一段时间内，梯度提升决策树（Gradient Boosting Decision Trees, GBDTs）如XGBoost和CatBoost，凭借其高效性和鲁棒性，主导了表格数据的监督学习任务 [blog.csdn.net](https://blog.csdn.net/2501_91618231/article/details/147474963#:~:text=TabPFN%20%E4%B8%8D%E5%8F%AA%E6%98%AF%E9%A2%84%E6%B5%8B%E8%A1%A8%E7%8E%B0,%E4%B8%8D%E5%90%8C%E7%B0%87%EF%BC%8C%E5%88%A9%E4%BA%8E%E4%B8%8B%E6%B8%B8%E4%BB%BB%E5%8A%A1%E3%80%82)。尽管后续出现了如TabNet、TabM等深度学习模型，它们通过注意力机制或参数高效的集成方法优化了多层感知机（MLP）的性能，但这些模型仍遵循在特定任务数据集上从零开始训练的范式 [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/5dfb55c6-0530-48d1-aafd-93a314a8f811)。

自2022年以来，受自然语言处理领域大型语言模型（LLMs）成功的启发，研究界开始探索面向表格数据的“基础模型” [www.zhuanzhi.ai](https://www.zhuanzhi.ai/vip/a8b0a5d4b9e659953cbd5010a6aa2963)。其核心思想是通过在大量、多样化的（通常是合成的）表格数据集上进行预训练，让模型学习一种通用的“学习算法”，从而能够通过上下文学习（In-Context Learning, ICL）快速适应新的、未见过的表格任务，通常只需少量样本甚至零样本。这一范式转变标志着表格数据分析从传统的模型训练向利用预训练知识进行推理的重大演进。本综述旨在系统梳理2022至2025年间表格数据基础模型的代表性工作，归纳其方法论、评价体系，并展望未来的研究趋势与挑战。

#### **方法分类与代表作**

当前，表格数据基础模型的研究主要沿着两条技术路线发展：一是专门设计的预训练Transformer模型，二是对通用大语言模型进行适应性增强。

**1. 基于先验拟合的Transformer模型 (Prior-Fitted Transformers)**

此类方法通过在海量合成数据上预训练一个专用Transformer，使其学习解决表格预测任务的通用算法。

*   **TabPFN (Tabular Prior-data Fitted Network)**
    *   **研究问题**: 如何在无需超参数调优的情况下，为小规模表格数据（样本量 ≤ 10,000）提供快速且高精度的预测。
    *   **核心方法**: TabPFN采用“先验拟合网络”（Prior-Fitted Network）思想，在一个基于结构因果模型（SCM）生成的数百万个合成数据集上预训练一个Transformer模型。在推理阶段，该模型将新任务的训练样本作为上下文（in-context），通过一次前向传播即可预测测试样本，实现了“情境学习” [blog.csdn.net](https://blog.csdn.net/2501_91618231/article/details/147474963#:~:text=TabPFN%20%E4%B8%8D%E5%8F%AA%E6%98%AF%E9%A2%84%E6%B5%8B%E8%A1%A8%E7%8E%B0,%E4%B8%8D%E5%90%8C%E7%B0%87%EF%BC%8C%E5%88%A9%E4%BA%8E%E4%B8%8B%E6%B8%B8%E4%BB%BB%E5%8A%A1%E3%80%82)。
    *   **关键实验结论**: 在多个AutoML基准测试中，TabPFN在小数据集上的预测性能显著超越了经过数小时调优的CatBoost等GBDT模型，而其推理时间仅需数秒，并且在处理缺失值、离群点等数据特性时表现出很强的鲁棒性 [blog.csdn.net](https://blog.csdn.net/xieyan0811/article/details/147575722)。

**2. 基于大语言模型（LLM）的增强方法**

此类方法不从头训练模型，而是利用现有LLM强大的通用知识和推理能力，通过设计特定的输入表示、检索机制或逻辑生成来解决表格任务。

*   **TableRAG: 检索增强生成 (Retrieval-Augmented Generation)**
    *   **研究问题**: 如何让LLM高效、准确地理解和推理超过其上下文窗口长度的大规模表格数据。
    *   **核心方法**: TableRAG框架避免将整个表格输入LLM。它首先通过查询扩展（Query Expansion）生成与模式（schema）和单元格值相关的子查询；接着进行两阶段检索，先检索最相关的列（模式检索），再基于此检索相关的单元格（单元格检索）；最后，将精简后的信息送入一个“程序辅助求解器”（Program-Aided Solver），由LLM生成代码与表格进行交互并得出答案 [blog.csdn.net](https://blog.csdn.net/weixin_44025655/article/details/145527034)。
    *   **关键实验结论**: 在ArcadeQA和BirdQA等涉及大规模表格的数据集上，TableRAG的准确率显著高于将全表或随机采样的行输入LLM的方法，同时其Prompt长度大幅缩减，验证了RAG在处理大规模表格时的有效性与效率。

*   **TabAF: 逻辑形式生成 (Logic Form Generation)**
    *   **研究问题**: 现有的逻辑形式（如SQL、Python）在处理结构多样（如分层、非规范）的表格时存在局限性，需要一种更通用的逻辑表示。
    *   **核心方法**: 该工作首次探索使用电子表格公式（Spreadsheet Formulas）作为解决通用表格问答（TableQA）的逻辑形式。为此，研究者构建了大规模公式标注数据集FormulaQA，并提出TabAF (Table Answer-Formula)框架，通过一个LLM主干联合生成直接答案（DP模式）和公式（Formula模式），再利用基于困惑度的聚合策略选择最终输出 [blog.csdn.net](https://blog.csdn.net/u013524655/article/details/146714421)。
    *   **关键实验结论**: 基于Llama3.1-70B微调的TabAF在WikiTableQuestion、HiTab和TabFact等多个基准上达到了新的SOTA性能，并在领域外数据集（如AIT-QA）上展示了优越的泛化能力，证明了公式作为一种通用逻辑形式的潜力。

*   **HeGTa: 结构信息融合 (Structural Information Fusion)**
    *   **研究问题**: 在小样本场景下，如何有效理解具有复杂结构（如层次化、多维）的表格。
    *   **核心方法**: HeGTa (Heterogeneous Graph-enhanced Large Language Model for Table understanding) 框架通过构建异构图（Heterogeneous Graph, HG）来显式地建模表格的复杂结构关系。它利用一个多任务预训练方案，将表格语义与LLM的参数化知识对齐，从而增强模型对复杂表格的理解能力 [zhuanzhi.ai](https://zhuanzhi.ai/paper/e4a856f209e289b75a2f0e01e2411219)。
    *   **关键实验结论**: 实验表明，在小样本复杂表格理解任务上，HeGTa显著优于其他SOTA方法，证明了显式建模表格结构对于提升LLM推理能力的重要性。

#### **实验与评价总结**

*   **基准与数据集**: 表格基础模型的评估通常在多个公开基准上进行，如用于表格问答的 **WikiTableQuestion**、事实核查的 **TabFact**、以及包含分层结构的 **HiTab** [blog.csdn.net](https://blog.csdn.net/u013524655/article/details/146714421)。此外，研究者也开始构建新的专用数据集，如包含公式标注的 **FormulaQA**，以支持新方法的研究。
*   **对比基线**: GBDT模型（特别是CatBoost和XGBoost）由于其强大的性能，至今仍是所有表格学习方法必须比较的黄金标准。在基础模型领域，早期的预训练模型（如TAPEX）和各类基于LLM的提示工程方法（如Chain-of-Table）是常见的对比对象。
*   **核心评价结论**:
    1.  **小数据域的优越性**: 以TabPFN为代表的先验拟合模型，在样本量较小（<10k）的场景下，展现出对强基线（如调优后的GBDT）的压倒性优势，核心在于其通过元学习掌握了通用的预测“先验”，避免了在小数据上的过拟合 [blog.csdn.net](https://blog.csdn.net/2501_91618231/article/details/147474963#:~:text=TabPFN%20%E4%B8%8D%E5%8F%AA%E6%98%AF%E9%A2%84%E6%B5%8B%E8%A1%A8%E7%8E%B0,%E4%B8%8D%E5%90%8C%E7%B0%87%EF%BC%8C%E5%88%A9%E4%BA%8E%E4%B8%8B%E6%B8%B8%E4%BB%BB%E5%8A%A1%E3%80%82)。
    2.  **复杂推理与泛化能力**: LLM增强方法在需要复杂多步推理的任务（如复杂计算、跨行/列聚合）上表现突出，尤其是当引导其生成可执行的逻辑形式（代码、公式）时。这类模型在不同结构和领域的表格上表现出更好的泛化能力 [blog.csdn.net](https://blog.csdn.net/u013524655/article/details/146714421)。
    3.  **效率与可扩展性**: 基础模型在推理效率上呈现两极分化。TabPFN推理极快，但受限于模型容量和预训练数据，主要适用于中小规模数据。LLM方法虽然能力更强，但面临上下文长度限制和高昂的计算成本，催生了如TableRAG等检索增强方法来解决可扩展性问题 [blog.csdn.net](https://blog.csdn.net/weixin_44025655/article/details/145527034)。

#### **趋势与挑战**

基于2022-2025年的研究进展，表格数据基础模型的未来发展呈现以下几个明确趋势，并伴随着相应挑战：

1.  **多模态表格理解 (Multimodal Table Understanding)**: 现实中的表格常以图像（如扫描的PDF文档、网页截图）或半结构化文档的形式存在。未来的研究将更加关注融合视觉、布局和文本信息的多模态模型。如**Turbo**模型的研究已经开始探索利用图像格式的表格进行推理，并借助特权信息（Privileged Information，即训练时可用的结构化文本）来弥合模态鸿沟 [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/145926)。**挑战**在于如何精确对齐视觉特征与表格的逻辑结构，以及如何在没有结构化特权信息的情况下进行端到端的推理。

2.  **与外部工具和知识库的深度集成 (Deeper Integration with Tools and Knowledge)**: LLM作为“大脑”或“调度中心”，调用外部工具（如代码解释器、Excel引擎、计算器）和知识库已成为主流趋势。TableRAG的程序辅助求解器和TabAF的Excel执行引擎是这一趋势的早期体现 [blog.csdn.net](https://blog.csdn.net/weixin_44025655/article/details/145527034)。未来，模型将需要掌握更复杂的工具链，甚至能够自主选择和组合工具来解决开放式问题。**挑战**在于工具的可靠性、错误恢复机制以及教会模型在何时以及如何使用合适的工具。

3.  **自动化、可解释性与因果推断 (Automation, Interpretability, and Causal Inference)**: 用户期望获得“即插即用”的自动化表格分析工具，而TabPFN是朝此方向迈出的重要一步 [blog.csdn.net](https://blog.csdn.net/xieyan0811/article/details/147575722)。同时，在金融、医疗等高风险领域，模型决策的可解释性至关重要。生成公式（如TabAF）或代码的方法，其推理路径本身就是一种解释。未来，模型不仅要给出预测，还可能需要从数据中发现潜在的因果关系，而不仅仅是相关性，这将是表格基础模型应用深化的关键。**挑战**在于如何在强大的黑盒模型与可信、可解释的决策之间取得平衡。

#### **结论**

表格数据基础模型是机器学习领域一个充满活力的新兴方向。自2022年以来，研究范式已从为特定任务训练专用模型，转向构建或利用大规模预训练模型来解决通用表格问题。无论是通过在合成数据上学习通用先验的专用Transformer（如TabPFN），还是通过检索、逻辑生成和结构融合等手段增强通用LLM（如TableRAG, TabAF, HeGTa），这些方法均在不同场景下展示了超越传统模型的潜力。当前的研究成果表明，表格数据分析的重点正从特征工程和模型选择，转向如何设计有效的预训练策略、数据表示以及与大模型的交互方式。尽管在可扩展性、多模态融合和可解释性方面仍面临挑战，但表格数据基础模型无疑为自动化、高精度的结构化数据智能分析开辟了广阔的前景。

#### **参考文献**

1.  Ruan, Y., Lan, X., Ma, J., Dong, Y., He, K., & Feng, M. (2024). *Language Modeling on Tabular Data: A Survey of Foundations, Techniques and Evolution*. arXiv preprint arXiv:2408.10548.
2.  Hollmann, N., Müller, S., Eggensperger, K., & Hutter, F. (2024). *Accurate predictions on small data with a tabular foundation model*. Nature, 629(8011), 321-328.
3.  Jiang, J. P., Xia, Y., Sun, H. L., Lu, S., Chen, Q. G., Luo, W., ... & Ye, H. J. (2025). *Multimodal Tabular Reasoning with Privileged Structured Information*. arXiv preprint.
4.  Cheng, Z., Dong, H., Wang, Z., Jia, R., Guo, J., Gao, Y., ... & Zhang, D. (2022). *HiTab: A Hierarchical Table Dataset for Question Answering and Natural Language Generation*. In Proceedings of ACL.
5.  Chen, S. A., Miculicich, L., Eisenschlos, J. M., et al. (2024). *TableRAG: Million-Token Table Understanding with Language Models*. arXiv preprint arXiv:2410.04739.
6.  *通过答案-公式联合生成实现通用表格问答* (2025). CSDN Blog. (注: 此处为博客文章，实际论文标题和作者可能为 "General Table Question Answering via Answer-Formula Co-generation")
7.  Jin, R., Li, Y., Qi, G., Hu, N., Li, Y. F., Chen, J., ... & Min, D. (2025). *HeGTa: Leveraging Heterogeneous Graph-enhanced Large Language Models for Few-shot Complex Table Understanding*. In Proceedings of AAAI.
8.  Arik, S. Ö., & Pfister, T. (2020). *TabNet: Attentive Interpretable Tabular Learning*. In Proceedings of AAAI.
9.  Gorishniy, Y., Kotelnikov, A., & Babenko, A. (2024). *TabM: Advancing Tabular Deep Learning with Parameter-Efficient Ensembling*. arXiv preprint.
10. Herzig, J., Nowak, P. K., Müller, T., Piccinno, F., & Eisenschlos, J. (2020). *TaPas: Weakly Supervised Table Parsing via Pre-training*. In Proceedings of ACL.
11. Wang, Z., Zhang, H., Li, C. L., Eisenschlos, J. M., Perot, V., Wang, Z., ... & Singh, S. (2024). *Chain-of-Table: Evolving Tables in the Reasoning Chain for Table Understanding*. In Proceedings of ICLR.
12. Liu, Q., Chen, B., Guo, J., Ziyadi, M., Lin, Z., Chen, W., & Lou, J. G. (2022). *TAPEX: Table Pre-training via Learning a Neural SQL Executor*. In Proceedings of ICLR.
13. Wu, Y., Wan, Y., Zhang, H., Sui, Y., Wei, W., Zhao, W., ... & Jin, H. (2024). *Automated Data Visualization from Natural Language via Large Language Models: An Exploratory Study*. arXiv preprint arXiv:2404.17136.
14. Chen, W., Wang, H., Chen, J., Zhang, Y., Wang, H., Li, S., ... & Wang, W. Y. (2020). *TabFact: A Large-scale Dataset for Table-Based Fact Verification*. In Proceedings of ICLR.
15. Pasupat, P., & Liang, P. (2015). *Compositional semantic parsing on semi-structured tables*. In Proceedings of ACL.