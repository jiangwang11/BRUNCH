好的，遵照您的指示。作为一名严谨的科研助手，我将基于提供的真实联网搜索结果，生成一篇关于“AI驱动的分子设计与优化”的学术综述。

### **AI驱动的分子设计与优化：2022-2025年研究进展综述**

#### **引言**

分子设计与优化是药物发现、材料科学和化学工程等领域的核心挑战。传统的研究范式高度依赖实验试错和研究人员的化学直觉，面临着化学空间巨大、研发周期长、成本高昂等瓶颈。近年来，人工智能（AI），特别是生成式AI模型的迅猛发展，为这一领域带来了革命性的变革 [[jcpu.cpu.edu.cn](https://jcpu.cpu.edu.cn/article/doi/10.11665/j.issn.1000-5048.2024031501)]。AI模型能够从海量数据中学习分子结构与性质之间的复杂关系，实现高效的性能预测、逆向设计和合成路径规划，正在重塑从知识挖掘到智能制造的全链条 [[wulixb.iphy.ac.cn](https://wulixb.iphy.ac.cn/cn/article/doi/10.7498/aps.74.20250497)]。

本综述旨在系统梳理2022至2025年间，AI在分子设计与优化领域的代表性工作，重点关注大语言模型（LLM）的创新应用、机器学习与传统方法的融合以及AI驱动的自动化实验，并探讨未来的发展趋势与挑战。

#### **方法分类与代表作**

##### **1. 大语言模型驱动的知识挖掘与材料设计**

LLM凭借其强大的自然语言处理和知识整合能力，成为从海量文献中提取、构建和推理化学知识的利器。

*   **Zheng等人 (2025)** 在《自然综述·材料》中，系统阐述了LLM如何革新网状化学（如MOFs和COFs）的研究范式。研究问题在于如何利用LLM从非结构化的文献中提取知识，并用于指导新材料的设计与合成。其核心方法包括利用提示工程、检索增强生成（RAG）和微调等技术，构建能够理解化学任务的“化学感知”模型 [[hub.baai.ac.cn](https://hub.baai.ac.cn/view/43169)]。研究表明，通过LLM自动化数据挖掘、辅助框架设计和预测合成结果，可将传统的经验驱动流程转变为高效的数据驱动发现循环，显著加速材料创新进程。

##### **2. 机器学习加速的高通量虚拟筛选**

在药物发现中，对数十亿级别的化合物库进行虚拟筛选是关键步骤，但计算成本极高。机器学习模型被用于构建代理模型，以低成本快速筛选出高潜力候选分子。

*   **Luttens等人 (2025)** 在《自然·计算科学》上发表的研究，旨在解决超大化学库的高效筛选难题。他们提出一种结合保序预测（Conformal Prediction, CP）框架和机器学习分类器（如CatBoost）的策略，用于快速识别高对接分数的化合物 [[hub.baai.ac.cn](https://hub.baai.ac.cn/view/44150)]。该方法首先对百万级别的化合物子集进行对接，训练模型学习评分规律，然后用模型预测数十亿化合物库中的高分候选者。关键结论是，该方法可在保证高灵敏度的同时，将所需对接的分子数量减少超过三个数量级，计算成本降低超1000倍，并成功发现了G蛋白偶联受体（GPCRs）的新型配体。

##### **3. 图结构增强的多模态分子语言模型**

分子的自然表示是图结构，而SMILES等线性表示会损失部分拓扑信息。因此，融合图表示与语言模型成为提升性能的关键方向。

*   **匿名作者 (2025)** 提出的 **Mol-LLM** 旨在构建一个能更有效利用分子图信息的通用分子语言模型。研究针对现有分子LLM对图结构理解不足的问题，提出了多模态指令调优和分子结构偏好优化（MolPO）的核心方法 [[themoonlight.io](https://www.themoonlight.io/zh/review/mol-llm-generalist-molecular-llm-with-improved-graph-utilization)]。模型架构融合了1D SELFIES 字符串表示和2D分子图嵌入，并通过创新的优化目标使模型偏好于正确的分子结构。实验证明，这种策略显著提升了模型在多种分子任务上的处理和理解能力。

##### **4. 生成式AI驱动的合成路径规划**

分子的可合成性是其实用价值的前提。生成式AI开始被用于模仿化学家的逆合成分析推理过程，直接生成多步合成路径。

*   **Lee与Vahdat (2025)** 开发的 **ReaSyn** 框架，旨在高效预测分子的多步合成路径。该研究的核心创新在于借鉴LLM的思维链（CoT），提出了“反应链”（Chain of Reaction, CoR）表示法，将合成路径表达为线性的分步推理序列 [[developer.nvidia.cn](https://developer.nvidia.cn/blog/reasoning-through-molecular-synthetic-pathways-with-generative-ai/)]。ReaSyn作为一个自回归生成模型，能够逐步构建从简单起始原料到目标分子的路径。实验表明，ReaSyn在多个逆合成规划基准测试中，其成功率显著超越了SynFormer等先前方法，尤其在ZINC250k数据集上提升近26个百分点。

##### **5. 大模型驱动的全流程自动化实验**

将AI的设计能力与自动化实验平台相结合，构建“自驱动实验室”（Self-driving Lab），是实现分子发现自动化的终极目标。

*   **Ruan等人 (2024)** 在《自然·通讯》上报告了一种由LLM驱动的自动化端到端化学合成开发平台（LLM-RDF）。该框架旨在利用LLM打通从文献调研到产物纯化的完整化学研发流程，解决化学家与自动化设备之间的交互壁垒 [[blog.csdn.net](https://blog.csdn.net/xiaoganbuaiuk/article/details/145895547)]。其核心方法是构建了六个专用LLM智能体（如文献搜索、实验设计、硬件执行等），通过自然语言与自动化液体处理工作站（Opentrons OT-2）交互。实验中，该平台成功完成了铜/TEMPO催化醇氧化反应的条件优化与放大，闭环贝叶斯优化将产率提升至94.5%，并实现了克级规模的自动化合成与纯化。

#### **实验与评价总结**

综合分析上述代表性工作，可以总结出以下共性评价模式：

1.  **评价目标的高度一致性：** 所有研究的核心目标均是加速分子发现或材料研发的“设计-合成-测试-学习”（DBTL）循环。无论是通过加速虚拟筛选，还是自动化实验流程，最终都指向降低研发成本和缩短周期。

2.  **性能评价维度的多层次化：**
    *   **对于预测与筛选任务**，评价指标集中于**准确性**（如分类精度、灵敏度）和**效率**（如计算成本降低倍数）。例如，Luttens等人的工作将计算成本降低了三个数量级以上 [[hub.baai.ac.cn](https://hub.baai.ac.cn/view/44150)]。
    *   **对于生成任务**，评价指标不仅关注生成分子的**有效性（Validity）**和**新颖性（Novelty）**，更强调**可合成性（Synthesizability）**和**性质优化得分**。ReaSyn通过生成完整的合成路径来直接保证可合成性，其评估标准为逆合成的成功率 [[developer.nvidia.cn](https://developer.nvidia.cn/blog/reasoning-through-molecular-synthetic-pathways-with-generative-ai/)]。
    *   **对于自动化平台**，评价指标是**端到端的任务成功率**和**最终产物的产率与纯度**。LLM-RDF通过将产率优化至94.5%并完成克级制备，证明了其物理世界的实际效能 [[blog.csdn.net](https://blog.csdn.net/xiaoganbuaiuk/article/details/145895547)]。

3.  **基准与数据的关键作用：** 多数研究依赖公开数据集（如ZINC、ChEMBL、Enamine REAL）和标准化基准进行模型性能的横向比较。同时，研究也普遍指出了高质量、标准化的实验数据（尤其是失败的实验数据）的稀缺是限制模型性能和泛化能力的关键瓶颈 [[hub.baai.ac.cn](https://hub.baai.ac.cn/view/43169)]。

#### **趋势与挑战**

基于2025年前后的研究成果，AI驱动的分子设计领域呈现出以下明确趋势，并伴随着相应挑战：

1.  **趋势一：从单一模态到多模态的深度融合。** 研究正从处理单一的SMILES字符串或分子图，转向融合文本（文献）、1D序列、2D图、3D构象甚至实验数据（如光谱、图像）的多模态模型。Mol-LLM的工作是这一趋势的初期体现 [[themoonlight.io](https://www.themoonlight.io/zh/review/mol-llm-generalist-molecular-llm-with-improved-graph-utilization)]。**挑战**在于如何有效对齐不同模态的特征空间，以及如何获取并标注高质量的多模态数据集。

2.  **趋势二：从“AI设计”到“AI执行”的闭环自动化。** AI的角色正在从单纯的计算和设计工具，演变为能够规划、执行并分析物理实验的智能体（Agent）。以LLM-RDF为代表的自驱动实验室是这一趋势的核心，它将AI的数字智能延伸至物理世界 [[wulixb.iphy.ac.cn](https://wulixb.iphy.ac.cn/cn/article/doi/10.7498/aps.74.20250497)]。**挑战**在于LLM生成代码的可靠性与安全性、硬件平台的标准化以及对复杂或意外实验情况的鲁棒处理能力。

3.  **趋势三：从关联性预测到因果与机理的可解释推理。** 当前AI模型擅长发现“相关性”，但往往是“黑箱”。未来的研究趋势是发展具备可解释性和因果推理能力的模型，使其不仅能预测“什么”，还能解释“为什么”。ReaSyn的“反应链”方法模仿了人类化学家的逐步推理过程，是朝向这一目标的重要尝试 [[developer.nvidia.cn](https://developer.nvidia.cn/blog/reasoning-through-molecular-synthetic-pathways-with-generative-ai/)]。**挑战**在于如何在保留模型复杂度的同时，嵌入化学物理定律和机理知识，实现模型的“白箱化”。

#### **结论**

2022至2025年，以大语言模型为代表的人工智能技术极大地推动了分子设计与优化领域的发展。研究范式已从单纯的性质预测和分子生成，迅速扩展到知识挖掘、合成规划和全流程自动化实验。多模态融合、智能体驱动的自动化平台以及可解释性推理成为未来发展的核心方向。尽管在数据质量、模型可靠性和物理世界交互等方面仍存在挑战，但AI与化学、材料科学的深度融合，无疑将持续加速科学发现的进程，引领按需设计与智能制造新时代的到来。

#### **参考文献**

1.  黄钰丹, 夏琬钧, 杜俊梅, 等. 大语言模型加速材料设计——从知识挖掘到智能设计的全链条赋能[J]. 物理学报, 2025, 74(18): 188101. [[wulixb.iphy.ac.cn](https://wulixb.iphy.ac.cn/cn/article/doi/10.7498/aps.74.20250497)]
2.  Zheng, Z., Rampal, N., Inizan, T.J. et al. Large language models for reticular chemistry. *Nat Rev Mater* (2025). [[hub.baai.ac.cn](https://hub.baai.ac.cn/view/43169)]
3.  Luttens, A., Cabeza de Vaca, I., Sparring, L. et al. Rapid traversal of vast chemical space using machine learning-guided docking screens. *Nat Comput Sci* (2025). [[hub.baai.ac.cn](https://hub.baai.ac.cn/view/44150)]
4.  Ruan, Y., Lu, C., Xu, N. et al. An LLM-driven automated end-to-end platform for chemical synthesis development. *Nat Commun* 15, 10160 (2024). [[blog.csdn.net](https://blog.csdn.net/xiaoganbuaiuk/article/details/145895547)]
5.  Mol-LLM: Generalist Molecular LLM with Improved Graph Utilization. arXiv:2502.02810 (2025). [[themoonlight.io](https://www.themoonlight.io/zh/review/mol-llm-generalist-molecular-llm-with-improved-graph-utilization)]
6.  Lee, S., Vahdat, A. Reasoning through molecular synthetic pathways with generative AI. *NVIDIA Developer Blog* (2025). [[developer.nvidia.cn](https://developer.nvidia.cn/blog/reasoning-through-molecular-synthetic-pathways-with-generative-ai/)]
7.  唐谦, 陈柔棻, 沈哲远, 等. 基于人工智能的小分子生成模型在药物发现中的研究进展[J]. 中国药科大学学报, 2024. [[jcpu.cpu.edu.cn](https://jcpu.cpu.edu.cn/article/doi/10.11665/j.issn.1000-5048.2024031501)]
8.  张香文, 侯放, 刘睿宸, 等. 机器学习辅助燃料分子设计[J]. 化学进展, 2024, 36(4): 471-485. [[manu56.magtech.com.cn](https://manu56.magtech.com.cn/progchem/CN/10.7536/PC230911)]
9.  人工智能辅助含能分子设计的应用与展望[J]. 含能材料, 2024. [[www.energetic-materials.org.cn](https://www.energetic-materials.org.cn/hncl/article/html/CJEM2023226?st=article_issue)]
10. 白延辉, 盛立民, 景剑峰, 等. 内蒙古大学学位授权点建设年度报告（学术学位 2023 年度）. [[gs.imu.edu.cn](https://gs.imu.edu.cn/__local/8/28/7F/3F8649389E08A6844F194F45326_0FE47AA5_4EC068.pdf)]