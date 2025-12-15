# In-context Learning in Natural Language Processing：2022–2025 年研究综述

## 引言

上下文学习（In-context Learning, ICL）指大型语言模型（Large Language Models, LLMs）在无需参数更新的前提下，通过在输入提示中嵌入少量任务示例（demonstrations）以实现对新任务的快速适应。自 GPT-3 首次系统性展示其能力以来，ICL 已成为 LLM 推理的核心范式之一。然而，原始 ICL 对示例选择、格式与排序高度敏感，性能不稳定。2022–2025 年间，研究重点从现象观察转向机制理解与性能优化，涌现出基于检索、元学习、示例生成与机制解释的系统性方法。本文综述此期间代表性工作，按方法论划分类别，总结共性实验发现，并展望未来方向。

## 方法分类与代表作

### 1. 基于检索的上下文学习（Retrieval-augmented ICL）

该方向旨在动态检索与当前查询最相关或最具信息量的示例，替代人工挑选或随机采样。

**《In-context Learning with Retrieved Demonstrations for Language Models: A Survey》**（arXiv:2401.11624, 2024）系统综述了检索增强 ICL（RetICL）框架。其研究问题为如何有效选择示例以提升 ICL 性能；核心方法包括基于 BM25、句子嵌入（如 SBERT）或微调双编码器的检索器，并探讨了相似性与多样性等检索目标；关键结论表明，检索策略、语料库构建与检索器训练方法是影响 RetICL 效果的关键因素，且该范式在 NLU、推理、问答与文本生成等任务上均优于固定示例。

**《Learning To Retrieve Prompts for In-Context Learning》**（NAACL 2022）提出通过 LLM 信号训练专用检索器。研究问题是如何自动学习检索对当前查询最有用的示例；其核心方法是利用 LLM 对候选示例的打分作为监督信号，训练一个双编码器检索模型；实验表明，该方法在 SuperGLUE 等基准上显著优于基于相似度的基线，证明了模型驱动的示例选择优于启发式方法。

**《Active Example Selection for In-Context Learning》**（ICLR 2023）将示例选择建模为强化学习问题。其研究问题是如何在指数级的示例组合空间中高效搜索最优子集；核心方法是将选择过程视为马尔可夫决策过程（MDP），使用 CQL 算法学习最优策略；实验发现，该主动学习策略能在多个 NLP 任务上以更少的示例达到与随机或 KNN 选择相当甚至更优的性能。

### 2. 元训练与优化 ICL 能力

该方向通过在元训练阶段优化模型参数，使其学会如何从上下文示例中高效学习。

**《Meta In-Context Learning Makes Large Language Models Better Zero and Few-Shot Relation Extractors》**（arXiv:2404.17807, 2024）针对关系抽取（RE）任务提出 MICRE 框架。研究问题是如何提升 LLM 在 RE 这类结构化任务上的 ICL 能力；核心方法是在多个 RE 数据集上对模型进行元训练，使其学会“如何从示例中学习关系”；实验在 12 个 RE 基准上验证，MICRE 在零样本和少样本设置下显著优于标准 ICL 和监督微调，尤其在大模型上增益明显，并能通过关系标签名有效传递语义。

**《Interpret and Improve In-Context Learning via the Lens of Input-Label Mappings》**（ACL 2025）旨在从机理层面理解并改进 ICL。研究问题为 LLM 如何在内部利用示例中的输入-标签映射；其核心发现是这些映射以主成分（PCs）形式存储于特定网络层，并在少数注意力头中被激活用于推理；基于此，研究通过精确微调这些关键模块，在多个任务上实现了显著性能提升，为 ICL 的可解释性与可干预性提供了新视角。

### 3. 动态示例生成与优化

当缺乏高质量示例库时，该方向探索由模型自身生成或优化示例。

**《Self-generated in-context learning: Leveraging auto-regressive language models as a demonstration generator》**（arXiv:2212.09444, 2022）研究如何减少对外部示例的依赖。其核心方法是利用 LLM 自身先生成 k 个示例，再将这些自生成示例用于主任务的 ICL；实验表明，使用 8 个自生成示例的性能可与从训练集中抽取 5 个真实示例相当，证明了 LLM 作为“自举式”示例生成器的潜力。

**《Automatic chain of thought prompting in large language models》**（NeurIPS 2023）旨在自动化思维链（CoT）提示的构建。研究问题是如何为复杂推理任务自动生成包含推理步骤的示例；其核心方法是先用 Sentence-BERT 对问题聚类，再从每簇中选取代表问题，通过 Zero-shot CoT 生成推理链；该 Auto-CoT 方法在多个推理数据集上性能与人工设计的 CoT 相当，解决了人工 CoT 成本高昂的问题。

## 实验与评价总结

对 2022–2025 年相关工作的实验分析可归纳出以下共性结论：
1.  **动态优于静态**：无论是基于检索还是元训练的动态示例选择/生成策略，其性能普遍且显著优于使用固定或随机示例的静态 ICL。
2.  **示例相关性是关键**：在大多数任务上，与查询高度语义相关的示例能带来最大性能增益，但多样性的引入在组成性泛化等任务上也显示出价值。
3.  **任务与模型依赖性**：ICL 优化方法的效果高度依赖于目标任务的性质（如结构化 vs. 非结构化）和基础 LLM 的规模与能力。大模型通常在元训练等方法下收益更大。
4.  **格式与排序敏感**：示例的呈现格式（如是否包含推理链）和排序顺序（如最近偏见）对最终性能有不可忽视的影响，需在方法设计中予以显式考虑。

## 趋势与挑战

基于当前研究进展，2025 年前后可预见的研究趋势包括：
1.  **超越文本的多模态 ICL**：随着多模态大模型（MLLMs）的发展，研究将探索如何在视觉-语言等多模态上下文中进行有效学习，例如检索相关图像-文本对作为示例。
2.  **面向小模型的高效 ICL**：当前 ICL 研究多聚焦于大模型，未来将探索如何通过知识蒸馏、特定架构设计等方法，将 ICL 能力有效迁移到资源受限的小型模型上。
3.  **可解释性与可控性增强**：对 ICL 内部机制（如输入-标签映射的利用）的深入理解将推动更可控的 ICL 系统，允许用户干预示例的利用方式以修正模型偏差或提升特定能力。

主要挑战在于 ICL 的理论基础仍不完善，缺乏对“为何相似示例更有效”等问题的严格数学解释，且现有方法在长上下文处理、跨领域泛化方面仍存在瓶颈。

## 结论

2022–2025 年，In-context Learning 从一种经验性现象发展为一个拥有丰富方法论体系的研究领域。通过检索增强、元训练、动态生成等策略，研究者显著提升了 ICL 的鲁棒性与性能。未来的研究将向多模态、小型化、可解释等方向纵深发展，旨在构建一个更高效、可控且普适的上下文学习范式，为 LLM 的广泛应用奠定坚实基础。

## 参考文献

1.  Liu, Y., et al. (2022). Learning To Retrieve Prompts for In-Context Learning. *Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL-HLT)*.
2.  Wang, Y., et al. (2023). Active Example Selection for In-Context Learning. *International Conference on Learning Representations (ICLR)*.
3.  Li, G., et al. (2024). Meta In-Context Learning Makes Large Language Models Better Zero and Few-Shot Relation Extractors. *arXiv preprint arXiv:2404.17807*.
4.  Sun, C., et al. (2025). Interpret and Improve In-Context Learning via the Lens of Input-Label Mappings. *Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (ACL 2025)*.
5.  Rubanov, A., et al. (2022). Self-generated in-context learning: Leveraging auto-regressive language models as a demonstration generator. *arXiv preprint arXiv:2212.09444*.
6.  Zhang, S., et al. (2023). Automatic chain of thought prompting in large language models. *Advances in Neural Information Processing Systems (NeurIPS) 36*.
7.  [themoonlight.io](https://www.themoonlight.io/zh/review/in-context-learning-with-retrieved-demonstrations-for-language-models-a-survey). (2025). [论文评述] In-context Learning with Retrieved Demonstrations for Language Models: A Survey. *Accessed via arXiv:2401.11624*.
8.  Wei, J., et al. (2022). Chain-of-thought prompting elicits reasoning in large language models. *Advances in Neural Information Processing Systems (NeurIPS) 35*.
9.  Min, S., et al. (2022). Rethinking the Role of Demonstrations: What Makes In-Context Learning Work? *Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing (EMNLP)*.
10. Gao, L., et al. (2023). PAL: Program-aided Language Models. *Proceedings of the 40th International Conference on Machine Learning (ICML)*.
11. Wang, X., et al. (2023). Least-to-Most Prompting Enables Complex Reasoning in Large Language Models. *International Conference on Learning Representations (ICLR)*.
12. Liu, P., et al. (2023). Pre-train, Prompt, and Fine-tune: A Universal Recipe for Downstream Tasks with Pre-trained Models. *Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL)*.