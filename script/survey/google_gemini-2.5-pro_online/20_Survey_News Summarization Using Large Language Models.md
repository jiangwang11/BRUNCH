好的，作为一名严谨的科研助手，我将基于您提供的真实联网搜索结果，为您生成一篇关于“基于大语言模型的新闻摘要”的中文学术综述。

### 基于大语言模型的新闻摘要技术研究综述（2022-2025）

#### 引言

自动文本摘要技术旨在将长文本或文本集合提炼成简洁、准确反映核心内容的短文，以缓解信息过载问题 [crad.ict.ac.cn](https://crad.ict.ac.cn/cn/article/doi/10.7544/issn1000-1239.2021.20190785)。传统方法主要分为抽取式（从原文选取关键句）和生成式（理解原文后重新组织语言生成摘要）。自 2022 年以来，以 GPT 系列为代表的大语言模型（Large Language Models, LLMs）凭借其强大的自然语言理解与生成能力，为自动摘要领域，特别是新闻摘要，带来了革命性的范式转变 [nsd.pku.edu.cn](https://nsd.pku.edu.cn/docs/20251013163525261099.pdf)。LLMs 能够生成语言更流畅、信息更概括的摘要，但其应用也伴随着“幻觉”（Hallucination）、知识陈旧以及事实一致性差等固有挑战 [ywlxbx.whuznhmedj.com](https://ywlxbx.whuznhmedj.com/journal/481.html)。因此，2022至2025年的研究工作主要围绕如何有效利用并优化 LLMs 以生成高质量、高事实性的新闻摘要展开。

#### 方法分类与代表作

当前基于 LLMs 的新闻摘要研究，根据其技术路径可主要分为三类：基于提示工程与上下文学习的方法、基于模型对齐与微调的方法，以及基于检索增强生成的方法。

**1. 基于提示工程与上下文学习的方法**

该方法不改变模型参数，而是通过精心设计的提示词（Prompt）和上下文示例（In-Context Learning, ICL）来引导 LLM 完成新闻摘要任务。研究重点在于如何构建有效的提示，以激发模型更深层次的推理与概括能力。

*   **思维链（Chain-of-Thought, CoT）提示**：该技术通过在提示中加入中间推理步骤，显著提升了模型在复杂任务上的表现。Wei et al. (2022) 的研究表明，在提示中加入“Let's think step by step”或提供带有推理过程的少样本示例，能够引导 LLM 将复杂任务分解，从而生成逻辑更严谨、内容更准确的结果 [nsd.pku.edu.cn](https://nsd.pku.edu.cn/docs/20251013163525261099.pdf)。对于新闻摘要，这意味着模型可以先分析新闻事件的关键要素（人物、时间、地点、事件），再综合这些要素生成摘要，而非直接进行端到端的文本压缩。

*   **结构化与关键词引导的提示**：通过在提示中引入结构化信息或关键概念，可以增强摘要的可控性与主题一致性。例如，钟茂生等人在排比句生成任务中提出的 K-CoT 框架，通过“主题解构→特征映射→关键词生成”的渐进式推理流程，精确控制生成内容 [aclanthology.org](https://aclanthology.org/2025.ccl-1.27.pdf)。虽然该研究不直接针对新闻摘要，但其方法论极具借鉴意义：在生成新闻摘要前，可先让模型提取新闻的核心关键词或事件框架，再基于这些“锚点”进行摘要生成，有效避免主题漂移。

**2. 基于模型对齐与微调的方法**

该方法通过在特定数据集上对 LLM 进行参数更新，使其行为和输出风格更符合新闻摘要的要求。这一过程通常被称为模型对齐（Alignment）。

*   **指令微调（Supervised Fine-tuning, SFT）**：SFT 使用高质量的“指令-回答”数据对来训练模型，使其学会遵循特定指令，是实现任务定制化的关键步骤。例如，Taori et al. (2023) 的 Alpaca 模型通过对 LLaMA 模型进行指令微调，使其获得了强大的指令遵循能力 [www.telecomsci.com](https://www.telecomsci.com/zh/article/doi/10.11959/j.issn.1000-0801.2024151/)。在新闻摘要领域，可以通过构建“「新闻原文」-「标准摘要」”的数据集进行 SFT，使模型专门学习新闻摘要的语言范式和信息筛选策略。

*   **基于人类反馈的强化学习（RLHF）与直接偏好优化（DPO）**：为使模型生成的摘要更符合人类偏好（如简洁性、重要性、客观性），研究者采用 RLHF 或 DPO 等技术。Ouyang et al. (2022) 的 InstructGPT/ChatGPT 便是通过 RLHF，让模型学习人类对不同回答的偏好，从而生成更有用、更安全的输出 [www.telecomsci.com](https://www.telecomsci.com/zh/article/doi/10.11959/j.issn.1000-0801.2024151/)。在新闻摘要任务中，可以让人类对模型生成的多个摘要版本进行排序，训练一个奖励模型，再通过强化学习优化 LLM，使其倾向于生成得分更高的摘要 [nsd.pku.edu.cn](https://nsd.pku.edu.cn/docs/20251013163525261099.pdf)。

*   **基于“最近发展区”理论的数据合成微调**：Chen et al. (2025) 提出了 AgentFrontier 方法，其灵感来源于教育心理学的“最近发展区”（ZPD）。该方法通过自动化流水线合成那些模型“跳一跳能够到”的、具有挑战性但通过指导可以完成的任务数据，用于持续预训练和微调 [huggingface.ac.cn](https://huggingface.ac.cn/papers/2510.24695)。应用于新闻摘要，这意味着可以自动生成复杂的、需要多角度整合信息才能完成的摘要任务，从而系统性地提升模型的高阶摘要能力。

**3. 基于检索增强生成的方法（RAG）**

为了解决 LLM 知识截至日期固定和事实性幻觉的问题，检索增强生成（RAG）成为新闻摘要任务的关键技术。RAG 将外部知识库（如实时新闻源、垂直领域数据库）与 LLM 的生成过程结合，实现了信息的动态更新和事实溯源。

*   **标准 RAG 框架**：Lewis et al. (2020) 首次提出的 RAG 框架，在生成摘要前，首先使用一个检索器（Retriever）从外部知识库中召回与输入新闻相关的文档片段 [ywlxbx.whuznhmedj.com](https://ywlxbx.whuznhmedj.com/journal/481.html)。然后，将这些检索到的内容与原始输入一同送入生成器（Generator）LLM，从而生成基于最新、最相关信息的摘要。这使得 LLM 能够摘要其训练数据中从未见过的新闻事件，并为摘要内容提供可验证的来源。

*   **分层与上下文增强的 RAG**：在处理结构化信息（如新闻报道中的不同章节、或软件工程中的类结构）时，简单的检索可能不足。黄子杰等人在代码摘要任务中提出的 HRCE 方法，对代码的层次结构（如类签名、属性、方法）分别建模，并从项目中抽取上下文信息（如父类摘要），实现了对代码内外部信息的综合利用 [crad.ict.ac.cn](https://crad.ict.ac.cn/article/doi/10.7544/issn1000-1239.202330730)。该思想可迁移至多文档新闻摘要，通过对新闻事件的层次结构（如事件背景、过程、影响）进行建模，并检索关联报道作为上下文，生成更具深度的摘要。

*   **知识图谱增强的 RAG**：针对需要结构化知识推理的新闻摘要（如分析公司财报并摘要其对股价的影响），研究者探索将知识图谱（Knowledge Graph）与 RAG 结合。知识图谱能提供实体间的明确关系，约束 LLM 的生成过程，减少主观臆断和逻辑错误 [ywlxbx.whuznhmedj.com](https://ywlxbx.whuznhmedj.com/journal/481.html)。例如，在生成一篇关于市场动态的新闻摘要时，模型可以从知识图谱中检索相关的公司、产品、竞争对手关系，确保摘要中的因果逻辑符合事实。

#### 实验与评价总结

在评价指标方面，研究领域正从传统的基于 n-gram 重叠度（如 ROUGE, BLEU, METEOR）的指标，向更侧重语义一致性和事实性的新型指标演进 [aclanthology.org](https://aclanthology.org/2025.ccl-1.27.pdf), [crad.ict.ac.cn](https://crad.ict.ac.cn/article/doi/10.7544/issn1000-1239.202330730)。近期的工作越来越多地采用“以模型评模型”（LLM-as-a-judge）的范式，如使用 MT-Bench、AlpacaEval 等基准，让更强大的 LLM（如 GPT-4）对生成的摘要在流畅性、准确性、简洁性等方面进行打分，这种方法被认为能更好地捕捉语义质量 [www.telecomsci.com](https://www.telecomsci.com/zh/article/doi/10.11959/j.issn.1000-0801.2024151/)。同时，高质量的人工评测依然是评估摘要质量的黄金标准，尤其是在评估摘要的结构一致性、情感表现力和创新性等细微维度上 [aclanthology.org](https://aclanthology.org/2025.ccl-1.27.pdf)。

综合各项研究，可以得出以下共性结论：
1.  **RAG 是提升事实性的关键**：在新闻摘要这类对事实准确性要求极高的任务中，集成 RAG 能够显著降低“幻觉”率，并使模型能够处理实时信息，这是单纯微调或提示工程难以实现的 [ywlxbx.whuznhmedj.com](https://ywlxbx.whuznhmedj.com/journal/481.html)。
2.  **对齐与微调决定了任务适配度**：未经微调的通用 LLM 虽具备基础摘要能力，但其输出风格和信息筛选策略未必符合新闻文体的要求。通过 SFT 和 RLHF/DPO 等对齐技术，可以使模型生成的摘要在专业性和人类偏好上得到显著优化 [www.telecomsci.com](https://www.telecomsci.com/zh/article/doi/10.11959/j.issn.1000-0801.2024151/)。
3.  **复杂推理依赖高级提示策略**：对于需要整合多源信息或进行深层逻辑分析的复杂摘要任务，诸如思维链（CoT）等高级提示技术能够有效引导模型进行分步推理，从而提升摘要的逻辑连贯性和深度 [nsd.pku.edu.cn](https://nsd.pku.edu.cn/docs/20251013163525261099.pdf)。

#### 趋势与挑战

基于 2025 年前后的研究动态，未来基于大模型的新闻摘要研究将呈现以下趋势，并面临相应挑战：

1.  **走向多模态新闻摘要（Multimodal News Summarization）**：新闻内容天然包含文本、图片、视频、数据图表等多种模态。未来的研究将不再局限于纯文本摘要，而是致力于开发能够理解和整合多模态信息的摘要模型。例如，模型需要能够“读懂”一张经济数据图表，并将其核心结论融入文本摘要中，这将对模型的多模态理解和融合能力提出极高要求 [ywlxbx.whuznhmedj.com](https://ywlxbx.whuznhmedj.com/journal/481.html), [nsd.pku.edu.cn](https://nsd.pku.edu.cn/docs/20251013163525261099.pdf)。

2.  **从单文档到事件级摘要的智能体演进（Agent-based Event-level Summarization）**：随着 LLM 自主智能体（Agent）技术的发展，新闻摘要任务将从对单一或少量文档的静态处理，演变为对一个动态发展新闻事件的持续追踪和动态摘要。一个智能体系统可以被赋予监控特定事件（如一场国际冲突、一次市场波动）的任务，它能自主规划、搜集多方信息、持续更新并生成一个演进式的“事件摘要”，这对智能体的规划、记忆和工具调用能力构成了新的挑战 [aclanthology.org](https://aclanthology.org/2024.ccl-2.8.pdf)。

3.  **可解释性与事实性验证的闭环（Explainable and Verifiable Summarization）**：尽管 RAG 提供了信息溯源，但模型如何利用检索内容进行推理的过程仍是“黑箱” [nsd.pku.edu.cn](https://nsd.pku.edu.cn/docs/20251013163525261099.pdf)。未来的研究趋势将更加关注摘要生成过程的可解释性，并探索“检索增强验证”（Retrieval-Augmented Verification）机制，即在生成摘要后，再由一个独立的核查模块或智能体来验证摘要中每一句话的真实性，形成“生成-验证”的闭环，以应对新闻摘要对事实性的极端要求 [ywlxbx.whuznhmedj.com](https://ywlxbx.whuznhmedj.com/journal/481.html)。

#### 结论

2022至2025年间，大语言模型从根本上重塑了新闻摘要领域的研究范式。通过提示工程、模型微调与检索增强生成等核心技术，研究者在提升摘要流畅性、可控性和事实性方面取得了显著进展。尽管在多模态融合、高级推理和可解释性方面仍面临挑战，但未来的研究正朝着更智能、更可信、更自动化的方向发展。随着多模态智能体和增强验证技术日趋成熟，基于 LLM 的新闻摘要系统有望成为新闻从业者和信息消费者的关键赋能工具。

#### 参考文献
- [aclanthology.org](https://aclanthology.org/2024.ccl-2.8.pdf)
- [aclanthology.org](https://aclanthology.org/2025.ccl-1.27.pdf)
- [crad.ict.ac.cn](https://crad.ict.ac.cn/cn/article/doi/10.7544/issn1000-1239.2021.20190785)
- [crad.ict.ac.cn](https://crad.ict.ac.cn/article/doi/10.7544/issn1000-1239.202330730)
- [huggingface.ac.cn](https://huggingface.ac.cn/papers/2510.24695)
- [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/d64db2dd-725f-43c8-aa35-5319469bd5a3)
- [nsd.pku.edu.cn](https://nsd.pku.edu.cn/docs/20251013163525261099.pdf)
- [qbxb.istic.ac.cn](https://qbxb.istic.ac.cn/CN/10.3772/j.issn.1000-0135.2025.04.004)
- [www.telecomsci.com](https://www.telecomsci.com/zh/article/doi/10.11959/j.issn.1000-0801.2024151/)
- [ywlxbx.whuznhmedj.com](https://ywlxbx.whuznhmedj.com/journal/481.html)
- Chen, X., Qiao, Z., Chen, G., Su, L., Zhang, Z., Wang, X., ... & Jiang, Y. (2025). *AgentFrontier: Extending the Capability Frontiers of LLM Agents via ZPD-guided Data Synthesis*. In Hugging Face Papers.
- Ouyang, L., Wu, J., Jiang, X., et al. (2022). *Training language models to follow instructions with human feedback*. In Advances in Neural Information Processing Systems.
- Wei, J., Wang, X., Schuurmans, D., et al. (2022). *Chain-of-thought prompting elicits reasoning in large language models*. In Advances in Neural Information Processing Systems.
- Lewis, P., Perez, E., Piktus, A., et al. (2020). *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*. In Advances in Neural Information Processing Systems.
- Taori, R., Gulrajani, I., Zhang, T., et al. (2023). *Stanford Alpaca: An Instruction-following LLaMA Model*. Stanford Center for Research on Foundation Models.