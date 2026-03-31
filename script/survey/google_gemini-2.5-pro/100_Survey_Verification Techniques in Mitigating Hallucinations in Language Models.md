好的，遵照您的指示，我将以一名严谨的科研助手的身份，基于提供的网络搜索结果，生成一篇关于“缓解语言模型幻觉的验证技术”的中文学术综述。

***

### **面向大型语言模型幻觉问题的验证技术研究综述 (2022-2025)**

#### **引言**

大型语言模型（Large Language Models, LLMs）在自然语言理解与生成任务中取得了革命性进展，但其“幻觉”（Hallucination）问题——即模型生成看似合理但与事实相悖、与上下文不符或无法追溯的内容——已成为其在金融、医疗、法律等高风险领域安全、可信应用的核心障碍 [crad.ict.ac.cn](https://crad.ict.ac.cn/article/doi/10.7544/issn1000-1239.202550069)。幻觉的产生机制复杂，涉及训练数据中的知识偏差、模型内在的推理缺陷以及对齐过程中的知识不一致性等多个环节 [zhuanzhi.ai](https://www.zhuanzhi.ai/paper/a9b38c620ccb48f8363b0bc451c966ae)。为应对这一挑战，学术界与工业界探索了多种缓解策略，其中，验证（Verification）技术通过引入内外部信息源对模型生成内容进行事实性校验，被证明是一条关键且有效的技术路径。本综述旨在梳理2022-2025年间缓解LLMs幻觉的代表性验证技术，归纳其核心方法论，总结评价体系共性，并展望未来研究趋势与挑战。

#### **方法分类与代表作**

根据验证信息来源和处理方式的差异，可将主流验证技术分为以下几类。

##### **1. 基于外部知识的检索与验证**

该类方法通过从外部知识库（如互联网、数据库）检索相关证据，并将其与模型生成内容进行比对，以判断其事实一致性。这是目前应用最广泛的验证范式，其核心在于证据的精准检索与有效利用。

*   **Halu-J (2024)**：该研究旨在解决传统检索验证方法仅提供分类标签而缺乏解释性的问题 [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/dc618d5b-355c-4294-8305-c08349e47a7d)。其核心方法是训练一个7B参数的“幻觉评判”模型 Halu-J，该模型不仅能从多个检索到的证据中选择最相关的部分，还能生成详细的“批判”（Critique）来解释其幻觉判断的理由。实验表明，在多证据幻觉检测任务上，Halu-J 的性能超越了 GPT-4o，且在批判生成和证据选择方面表现出与后者相当的能力，验证了基于批判的细粒度验证框架的有效性。

*   **Claim Verification Survey (2025)**：这篇综述系统性地拆解了基于外部知识的声明验证流程，为该方向提供了清晰的研究框架 [themoonlight.io](https://www.themoonlight.io/zh/review/claim-verification-in-the-age-of-large-language-models-a-survey)。该框架包括声明检测、值得检查性识别、证据检索、理由选择、真实性预测和解释生成等多个核心组件。研究强调，检索增强生成（Retrieval-Augmented Generation, RAG）是提升LLMs利用外部知识进行自我验证的关键技术，但模型对不相关信息的敏感性仍是主要挑战。

##### **2. 基于分解与重组的验证**

此类方法将模型生成的长文本分解为多个独立的原子事实（子声明），对每个原子事实进行独立验证后，再综合判断整体内容的真实性。

*   **DnDScore (2024)**：该研究聚焦于长文本生成中事实性验证的“分解-再验证”（Decompose-and-Verify）策略，并首次系统探究了“分解”（Decomposition）与“去语境化”（Decontextualization）之间的相互作用 [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/91189)。其核心方法是提出 DnDScore，一种在验证子声明时能充分考虑去语境化所增补的上下文信息的验证评分。研究发现，分解和去语境化策略的选择对最终事实性评分有显著影响，证明了在验证分解后的原子事实时，必须精巧地处理其与原始上下文的关联。

##### **3. 基于模型自身知识的对齐与验证**

该方向不完全依赖外部知识，而是尝试利用或校正模型在预训练阶段已经学到的内部（参数化）知识，通过“自我反思”和对齐来提升事实性。

*   **Self-Memory Alignment (SMA) (2025)**：该研究旨在通过利用模型自身的内在知识来缓解事实性幻觉，减少对外部知识的依赖 [themoonlight.io](https://www.themoonlight.io/zh/review/self-memory-alignment-mitigating-factual-hallucinations-with-generalized-improvement)。其核心方法是通过让模型基于知识源生成正确和错误的问答对，并利用直接偏好优化（DPO）进行微调，从而使模型偏好于生成符合其内部记忆的、事实正确的答案。在FactualBench等多个基准上的实验表明，SMA能够显著提升模型的事实准确性，证明了精确的事实性问答训练对激活和对齐模型内部知识的有效性。

*   **Knowledge Consistent Alignment (KCA) (2024)**：该工作旨在通过解决对齐数据中的外部知识与基础模型内在知识之间的不一致性来缓解幻觉 [zhuanzhi.ai](https://www.zhuanzhi.ai/paper/a9b38c620ccb48f8363b0bc451c966ae)。其核心方法是利用一个高度对齐的LLM（如GPT-4）作为评估器，自动评估基础模型对外部知识的掌握边界，并对存在知识冲突的对齐数据实例采取特定策略进行处理。实验证明，KCA能在多种模型和规模上有效减少幻觉，证实了最小化内外部知识不一致性是缓解幻觉的有效途径。

##### **4. 面向特定模态与场景的验证**

随着LLMs向多模态领域扩展，针对特定场景的幻觉验证技术也应运而生。

*   **UNIHD (2024)**：该研究解决了多模态大语言模型（MLLMs）幻觉检测方法局限于单一任务和类别的问题，提出统一的检测框架 [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/48997)。其核心方法是推出统一多模态幻觉检测框架UNIHD，该框架利用一套辅助工具集（如OCR、图像检索工具）来稳健地验证多模态内容中可能出现的幻觉。同时，研究构建了新的元评估基准MHaluBench，实验证明了UNIHD框架的有效性，并为不同幻觉类型提供了策略性的工具应用见解。

#### **实验与评价总结**

对2022-2025年的研究进行归纳，可以发现实验与评价环节呈现出以下共性结论：

1.  **高质量基准是研究的基石**：研究者普遍认识到现有基准的局限性。例如，UHGEval [developer.volcengine.com](https://developer.volcengine.com/articles/7391691158885892108) 批评了现有基准多采用“约束式生成”，与真实场景的“无约束生成”存在差异，并开创性地构建了包含5000+条新闻领域数据、采用关键词级细粒度标注的中文幻觉评估基准。同样，MHaluBench [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/48997) 和 ME-FEVER [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/dc618d5b-355c-4294-8305-c08349e47a7d) 等面向多模态和多证据场景的新基准也相继问世，推动了该领域的精细化发展。

2.  **自动化评估框架成为主流**：由于人工标注成本高昂且一致性难以保证，自动化评估成为必然趋势。ANAH-v2 [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/16015ace-828b-4f3e-9b5b-31a964b6e76f) 提出的迭代自训练框架，成功训练出性能超越GPT-4的7B幻觉注释器，证明了以模型驱动评估的可行性。此外，《面向大语言模型安全部署的可信评估体系》[crad.ict.ac.cn](https://crad.ict.ac.cn/article/doi/10.7544/issn1000-1239.202440566?viewType=HTML) 也构建了自动化工作流，对主流LLMs进行了百万次量级的查询测试，从而得出了关于模型一致性的关键结论。

3.  **细粒度与可解释性评价日益重要**：研究不再满足于句子级别的“真/假”二元判断。UHGEval [developer.volcengine.com](https://developer.volcengine.com/articles/7391691158885892108) 的关键词级标注和 Halu-J [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/dc618d5b-355c-4294-8305-c08349e47a7d) 的批判性解释生成，均体现了向更细粒度和更具可解释性评价的转变。这不仅能更精确地定位错误，也能为模型改进提供更明确的指引。

#### **趋势与挑战**

基于现有研究，预计2025年前后，缓解LLMs幻觉的验证技术将呈现以下趋势，并面临相应挑战：

1.  **从“检测”到“归因与修复”的闭环**：未来的研究将不止步于检测幻觉，而是更深入地追溯幻觉的根源（归因），并尝试在生成过程中或生成后进行自动修复。挑战在于如何精确地将幻觉归因于模型的特定知识缺陷或推理错误，并开发出既能修正错误又不损害原文流畅性和意图的修复算法。

2.  **动态内外部知识的协同与对齐**：模型需要更智能地协同其参数化的内部知识和检索到的外部知识。KCA [zhuanzhi.ai](https://www.zhuanzhi.ai/paper/a9b38c620ccb48f8363b0bc451c966ae) 和 SMA [themoonlight.io](https://www.themoonlight.io/zh/review/self-memory-alignment-mitigating-factual-hallucinations-with-generalized-improvement) 的工作是早期探索。未来的趋势是发展动态对齐机制，使模型能实时判断何时信任内部知识、何时求助于外部证据，并能有效解决两者之间的冲突。挑战在于如何高效地进行实时知识更新与对齐，尤其是在处理快速变化的世界知识时。

3.  **多模态与跨模态一致性验证**：随着多模态模型的普及，幻觉验证将从纯文本领域扩展到图文、音视频等多种模态的融合内容。如UNIHD [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/48997) 所示，验证技术需要具备跨模态的理解和推理能力。核心挑战在于如何定义和度量跨模态内容的一致性，以及如何构建能够处理复杂模态间关联的验证工具和基准。

#### **结论**

为缓解大型语言模型的幻觉问题，验证技术在过去几年取得了显著进展。研究范式已从单一的外部知识检索，发展到内外知识对齐、分解验证、多模态验证等多元化路径。同时，高质量、细粒度、自动化的评估体系建设也成为驱动该领域发展的关键动力。尽管如此，幻觉问题仍是实现通用人工智能道路上的核心挑战。未来的研究需要在验证的深度（从检测到归因与修复）、知识的协同（内外部动态对齐）以及模态的广度（跨模态一致性）上持续突破，以期构建真正可信、可靠的语言模型。

#### **参考文献**

1.  李自拓, 孙建彬, 等. (2025). *大语言模型幻觉检测方法综述*. [crad.ict.ac.cn](https://crad.ict.ac.cn/article/doi/10.7544/issn1000-1239.202550069)
2.  Ye, W., Hu, J., et al. (2025). *面向大语言模型安全部署的可信评估体系*. [crad.ict.ac.cn](https://crad.ict.ac.cn/article/doi/10.7544/issn1000-1239.202440566?viewType=HTML)
3.  Chen, X., Wang, C., et al. (2024). *Unified Hallucination Detection for Multimodal Large Language Models*. [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/48997)
4.  Wanner, M., Van Durme, B., & Dredze, M. (2024). *DnDScore: Decontextualization and Decomposition for Factuality Verification in Long-Form Text Generation*. [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/91189)
5.  (2025). *[论文评述] Claim Verification in the Age of Large Language Models: A Survey*. [themoonlight.io](https://www.themoonlight.io/zh/review/claim-verification-in-the-age-of-large-language-models-a-survey)
6.  (2025). *[论文审查] Self-Memory Alignment: Mitigating Factual Hallucinations with Generalized Improvement*. [themoonlight.io](https://www.themoonlight.io/zh/review/self-memory-alignment-mitigating-factual-hallucinations-with-generalized-improvement)
7.  Gu, Y., Ji, Z., et al. (2024). *ANAH-v2: Scaling Analytical Hallucination Annotation of Large Language Models*. [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/16015ace-828b-4f3e-9b5b-31a964b6e76f)
8.  Wang, B., Chern, S., et al. (2024). *Halu-J: Critique-Based Hallucination Judge*. [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/dc618d5b-355c-4294-8305-c08349e47a7d)
9.  中国人民大学等. (2024). *UHGEval：无约束生成下的中文大模型幻觉评估*. [developer.volcengine.com](https://developer.volcengine.com/articles/7391691158885892108)
10. Wan, F., Huang, X., et al. (2024). *Knowledge Verification to Nip Hallucination in the Bud*. [zhuanzhi.ai](https://www.zhuanzhi.ai/paper/a9b38c620ccb48f8363b0bc451c966ae)
11. Ji, Z., et al. (2023). A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions. *arXiv preprint arXiv:2311.05232*.
12. Rawte, V., et al. (2023). A Survey of Hallucination in Large Language Models. *arXiv preprint arXiv:2309.05922*.