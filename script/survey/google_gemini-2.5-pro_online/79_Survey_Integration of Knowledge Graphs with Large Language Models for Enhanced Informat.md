好的，遵照您的指示，作为一名严谨的科研助手，我将基于提供的真实网络搜索结果，生成一篇关于“融合知识图谱与大语言模型以增强信息检索与理解”的中文学术综述。

***

### **融合知识图谱与大语言模型以增强信息检索与理解：2022-2025年研究综述**

#### **引言**

近年来，大语言模型（Large Language Models, LLMs）在自然语言处理领域取得了突破性进展，展现出强大的语言理解与生成能力。然而，LLMs在实际应用中仍面临三大核心挑战：生成内容时可能出现与事实不符的“幻觉”问题、其内部知识存在时效性滞后、以及推理过程缺乏透明度和可解释性 [arocmag.cn](https://www.arocmag.cn/abs/2024.12.0532)。知识图谱（Knowledge Graphs, KGs）作为一种以结构化形式存储、组织和管理人类知识的语义网络，恰好能弥补LLMs在事实性、可追溯性和知识更新方面的不足。因此，将LLMs的语义理解能力与KGs的结构化事实知识相结合，已成为构建更可靠、可解释和高效信息系统的关键研究方向，尤其在增强信息检索与理解方面展示了巨大潜力 [themoonlight.io](https://www.themoonlight.io/zh/review/synergizing-knowledge-graphs-with-large-language-models-a-comprehensive-review-and-future-prospects)。本综述旨在系统梳理2022至2025年间该领域的代表性工作，总结其方法、评价范式，并展望未来的核心挑战与研究趋势。

#### **方法分类与代表作**

融合知识图谱与大语言模型的方法主要可分为两大类：在推理阶段利用知识图谱增强LLM表现的**知识增强推理**，以及在训练阶段将知识注入模型参数的**知识注入学习**。

##### **1. 知识增强推理 (Knowledge-Enhanced Inference)**

该范式在LLM进行推理或生成时，动态地从知识图谱中检索相关信息作为上下文，以指导并约束其输出。这种方法以其灵活性和无需重新训练模型的优势，成为当前研究的主流，通常以检索增强生成（Retrieval-Augmented Generation, RAG）的变体形式出现。

*   **《Knowledge-Aware Query Expansion with Large Language Models for Textual and Relational Retrieval》 (arXiv, 2024)** [themoonlight.io](https://www.themoonlight.io/zh/review/knowledge-aware-query-expansion-with-large-language-models-for-textual-and-relational-retrieval)
    *   **研究问题**: 传统的查询扩展方法仅关注文本相似性，忽略了文档间的结构化关系，导致扩展后的查询在语义相似但意图上可能不相关。
    *   **核心方法**: 提出一个知识感知的查询扩展框架。该方法首先利用LLM从用户查询中解析出实体，然后在KG中检索与实体相关的文档及其结构化关系（如“引用”、“兼容”），通过基于文本表示的关系过滤机制筛选出最相关的知识三元组，最终将这些三元组与原始查询一同输入LLM以生成更精准的扩展查询。
    *   **关键结论**: 在产品、学术及生物医学等多个数据集上的实验表明，该方法通过引入KG的结构化关系，显著提升了半结构化检索任务的准确性，尤其是在处理具有复杂关系依赖的用户查询时，性能优于仅依赖文本的基线模型。

*   **《基于相关性提示的知识图谱问答》 (软件学报, 2025)** [jos.org.cn](https://www.jos.org.cn/html/2025/9/7247.htm)
    *   **研究问题**: 基于“检索-问答”的框架在从KG中为LLM检索知识时，通常会不可避免地引入大量与问题无关的噪声三元组，从而干扰LLM的判断，导致生成内容不准确。
    *   **核心方法**: 提出一个“检索-相关性评估-问答”三阶段框架。在从KG检索到子图后，该方法利用一个独立训练的相关性计算模型，量化每个三元组与给定问题的相关性分数。随后，将三元组连同其相关性分数一同构成提示词（Prompt），并按相关性升序排列后输入LLM，以引导模型关注最关键的知识。
    *   **关键结论**: 在自建的机械制造数据集Mecha-QA和航空航天数据集Aero-QA上的实验证明，该方法通过向LLM显式提供知识的相关性信息，显著提升了模型在垂直领域问答任务上的准确率和用户满意度，有效减少了生成答案中的无关信息。

*   **《Search-o1: Agentic Search-Enhanced Large Reasoning Models》 (arXiv, 2025)** [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/847cf199-ad06-48df-a2b4-c7a31fd90e25)
    *   **研究问题**: 大型推理模型（LRMs）在执行长链条推理时，常因缺乏特定知识而产生不确定性，导致推理中断或错误。
    *   **核心方法**: 提出Search-o1框架，将LLM构建为一个能够自主决策的代理（Agent）。当模型在推理过程中遇到知识不确定点时，能够主动触发代理检索机制，从外部知识源（如KG或Web）动态获取信息。此外，框架包含一个“文档内推理”模块，用于在注入推理链之前对检索到的冗长内容进行预处理和提炼，以减少噪声。
    *   **关键结论**: 在多个复杂的科学、数学和编程推理基准测试中，Search-o1展现了卓越性能。实验表明，代理式的主动搜索与信息提炼机制，能够显著增强LLM在复杂推理任务中的可靠性与事实准确性。

##### **2. 知识注入学习 (Knowledge-Injected Learning)**

此类方法致力于在预训练或微调阶段，将知识图谱中蕴含的结构化知识直接编码到LLM的参数中，从而在模型内部构建更丰富的知识体系。

*   **《SKILL: Structured Knowledge Infusion for Large Language Models》 (NAACL, 2022)** [blog.csdn.net](https://blog.csdn.net/qq_36158230/article/details/150707387)
    *   **研究问题**: 如何在不依赖文本与KG严格对齐的情况下，有效地将大规模结构化知识注入LLM。
    *   **核心方法**: 该研究提出直接在知识图谱的三元组上对T5这样的序列到序列模型进行训练。通过设计特定的训练任务，模型被教会在给定头实体和关系时预测尾实体，从而将KG的结构信息和事实知识融入其参数。
    *   **关键结论**: 在多个需要多跳推理的问答基准上的实验显示，经过SKILL方法训练的模型其性能得到显著提升。这证明了直接在结构化数据上进行训练是增强LLM事实性知识和推理能力的有效途径，尤其适用于对齐数据稀疏的场景。

*   **《ERNIE 3.0: Large-scale Knowledge Enhanced Pre-training for Language Understanding and Generation》 (arXiv, 2021)** [blog.csdn.net](https://blog.csdn.net/qq_36158230/article/details/150707387)
    *   **研究问题**: 如何构建一个统一的预训练框架，能够融合大规模文本语料和知识图谱，以同时提升模型的语言理解和生成能力。
    *   **核心方法**: ERNIE 3.0 设计了一个统一的框架，集成了自回归和自编码网络，使其能够处理各种自然语言处理任务。在预训练阶段，模型不仅从海量文本中学习，还通过知识增强策略（如知识掩码）从大规模知识图谱中吸收事实知识。
    *   **关键结论**: ERNIE 3.0 及其后续版本Titan在数十个公开NLP数据集上取得了当时的最佳性能，验证了大规模知识增强预训练的强大威力，证明了在模型训练早期注入知识对于构建通用且知识丰富的LLM至关重要。

#### **实验与评价总结**

综合分析上述代表性工作及相关研究 [themoonlight.io](https://www.themoonlight.io/zh/review/synergizing-knowledge-graphs-with-large-language-models-a-comprehensive-review-and-future-prospects)，可以总结出几点共性实验结论：

1.  **显著缓解幻觉问题**：无论是通过推理时检索还是训练时注入，引入知识图谱作为外部事实源都能有效约束LLM的输出，显著降低其生成事实性错误的频率，提升内容的可靠性 [arocmag.cn](https://www.arocmag.cn/abs/2024.12.0532)。
2.  **增强复杂推理能力**：在需要多跳推理、关系推断的复杂问答（Complex QA）任务中，KG的结构化特性为LLM提供了清晰的推理路径，使其表现远超未增强的基线模型 [blog.csdn.net](https://blog.csdn.net/qq_36158230/article/details/150707387)。
3.  **提升可解释性与可追溯性**：基于检索的方法能够将所依据的知识三元组或子图作为答案的“证据”，极大地增强了系统输出的可解释性和用户信任度。
4.  **检索噪声是关键瓶颈**：几乎所有知识增强推理方法都面临一个共同挑战——如何从检索到的大量知识中精确识别并利用关键信息，同时抑制噪声干扰。自适应检索、相关性评估等精细化策略被证明是提升性能的关键 [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/94455)。

#### **趋势与挑战**

基于2024至2025年的最新研究，未来融合知识图谱与大语言模型的研究将呈现以下趋势，并面临相应挑战：

1.  **从被动检索到主动代理交互（Agentic Interaction）**：研究趋势正从简单的RAG范式，转向将LLM塑造为能够与KG进行自主、多轮交互的智能代理 [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/847cf199-ad06-48df-a2b4-c7a31fd90e25)。未来的模型将能够主动规划推理步骤、分解复杂问题、并决策何时以及如何查询KG，甚至对KG中的信息进行验证和修正。 **挑战**在于如何设计高效的交互策略和推理算法，以及如何确保代理行为的鲁棒性和可控性。

2.  **知识表示与利用的深度统一**：当前多数方法仍将KG视为外部符号数据库，模型与知识的交互停留在“表面”的文本或ID层面。未来的研究将致力于实现LLM的向量化表示空间与KG的结构化符号空间的深度对齐和统一。这将催生出能够无缝进行符号推理和向量计算的“神经-符号”混合模型。**挑战**在于如何解决两种异构表示之间的“语义鸿沟”，并开发出可扩展的统一模型架构。

3.  **多模态与跨领域知识的融合**：知识的形态远不止于文本。未来的融合框架将不再局限于文本知识图谱，而是扩展到包含图像、音视频等信息的多模态知识图谱 [themoonlight.io](https://www.themoonlight.io/zh/review/synergizing-knowledge-graphs-with-large-language-models-a-comprehensive-review-and-future-prospects)。同时，如何高效融合来自不同领域、具有异质结构的知识图谱，以支持跨域查询和推理，也是一个重要方向 [crad.ict.ac.cn](https://crad.ict.ac.cn/cn/article/Y2025/I3/605)。**挑战**在于多模态知识的对齐、表示和融合技术，以及解决跨域知识融合中的隐私和安全问题。

4.  **知识图谱的自动化构建与动态更新闭环**：LLM的强大能力将被反向用于知识图谱的生命周期管理。未来的系统将形成一个自我演化的闭环：利用LLM从非结构化数据中自动抽取实体和关系以构建和扩充KG [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/120739)，再利用更新后的KG来增强LLM，从而实现知识的持续、动态更新。**挑战**在于如何保证LLM抽取知识的准确性，避免将“幻觉”内容注入KG，以及如何实现轻量化、增量式的知识更新。

#### **结论**

融合知识图谱与大语言模型是通往更强大、更可信人工智能系统的关键路径。知识图谱以其结构化的事实性弥补了LLM在可靠性与可解释性上的短板，而LLM则以其强大的语义理解能力为知识的利用和扩展注入了活力。综述表明，当前研究已从早期的简单结合，发展到以知识增强推理和知识注入学习为代表的系统化方法。展望未来，该领域正朝着更动态的代理交互、更深度的神经-符号统一、更广泛的多模态融合以及更智能的自动化知识管理闭环方向演进。克服其中的挑战，将为实现知识驱动的、可信赖的下一代信息检索与理解系统提供坚实的理论与技术支撑 [arocmag.cn](https://www.arocmag.cn/abs/2024.12.0532)。

#### **参考文献**

1.  曹荣荣, 柳林, 于艳东, 王海龙. (2025). 融合知识图谱的大语言模型研究综述. *计算机应用研究*, 42(8), 2255-2266. [arocmag.cn](https://www.arocmag.cn/abs/2024.12.0532)
2.  Pan, Z., et al. (2024). *Synergizing Knowledge Graphs with Large Language Models: A Comprehensive Review and Future Prospects*. arXiv preprint. [themoonlight.io](https://www.themoonlight.io/zh/review/synergizing-knowledge-graphs-with-large-language-models-a-comprehensive-review-and-future-prospects)
3.  Li, P., et al. (2024). *Knowledge-Aware Query Expansion with Large Language Models for Textual and Relational Retrieval*. arXiv preprint. [themoonlight.io](https://www.themoonlight.io/zh/review/knowledge-aware-query-expansion-with-large-language-models-for-textual-and-relational-retrieval)
4.  马杰, 孙望淳, 王平辉, 等. (2025). 基于相关性提示的知识图谱问答. *软件学报*, 36(9), 4056-4071. [jos.org.cn](https://www.jos.org.cn/html/2025/9/7247.htm)
5.  Li, X., et al. (2025). *Search-o1: Agentic Search-Enhanced Large Reasoning Models*. arXiv preprint. [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/847cf199-ad06-48df-a2b4-c7a31fd90e25)
6.  Chen, Y., et al. (2022). *SKILL: Structured Knowledge Infusion for Large Language Models*. In Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies. [blog.csdn.net](https://blog.csdn.net/qq_36158230/article/details/150707387)
7.  Sun, Y., et al. (2021). *ERNIE 3.0: Large-scale Knowledge Enhanced Pre-training for Language Understanding and Generation*. arXiv preprint. [blog.csdn.net](https://blog.csdn.net/qq_36158230/article/details/150707387)
8.  DeepResearch. (2025). *基于知识图谱与数据合成的大语言模型幻觉缓解研究前沿*. CSDN Blog. [blog.csdn.net](https://blog.csdn.net/qq_36158230/article/details/150707387)
9.  Xu, D., et al. (2025). *Harnessing Large Language Models for Knowledge Graph Question Answering via Adaptive Multi-Aspect Retrieval-Augmentation*. arXiv preprint. [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/94455)
10. 吴文隆, 尹海莲, 王宁, 等. (2025). 大语言模型和知识图谱协同的跨域异质数据查询框架. *计算机研究与发展*, 62(3), 605-618. [crad.ict.ac.cn](https://crad.ict.ac.cn/cn/article/Y2025/I3/605)
11. Zhang, J., et al. (2025). *GKG-LLM: A Unified Framework for Generalized Knowledge Graph Construction*. arXiv preprint. [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/120739)
12. Mei, L., et al. (2025). *A Survey of Context Engineering for Large Language Models*. arXiv preprint. [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/1a3763b7-6e29-4e77-ad27-5a1337b23b24)