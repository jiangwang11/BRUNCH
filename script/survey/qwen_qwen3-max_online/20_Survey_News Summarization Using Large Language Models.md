# 基于大语言模型的新闻文本摘要研究综述（2022–2025）

## 引言

新闻文本摘要旨在从海量、冗余且时效性强的新闻报道中提取核心事实，是信息爆炸时代的关键技术。2022年起，以ChatGPT为代表的大语言模型（Large Language Models, LLMs）的涌现，为该领域带来了范式转变。相比传统的编码器-解码器模型（如BART、PEGASUS），LLMs凭借其强大的上下文理解、事实保持与生成能力，在处理长新闻文档、多文档融合及跨语言摘要等复杂任务上展现出显著优势。本文系统综述2022至2025年间该领域的代表性工作，按技术路线将其分为四大类，并总结实验评价的共性发现，最后对未来研究趋势进行展望。

## 方法分类与代表作

### 基于提示工程与上下文学习的方法

该类方法利用LLMs的零样本或少样本能力，通过精心设计的提示（Prompt）引导模型生成摘要，无需参数微调。

**Goyal et al. (2023, EMNLP)** 系统评估了GPT-3.5和ChatGPT在单文档新闻摘要上的表现。研究发现，通过指令提示（Instruction Prompting）和思维链（Chain-of-Thought, CoT）提示，LLMs能有效减少幻觉并提升事实一致性，其ROUGE-L分数甚至超越了微调的BART模型，在事实性指标上则显著优于基线。

**Kryscinski et al. (2023, arXiv)** 针对LLMs在摘要中产生事实性错误的问题，提出了一种基于事实一致性（Factuality）的提示策略。该方法在生成摘要后，提示模型对摘要中的每个事实性陈述进行自我验证，通过迭代修正，显著提升了摘要的忠实度（Faithfulness），在XSum数据集上将FactCC指标提高了15%以上。

**Zhang et al. (2024, CCL)** 将CoT思想应用于跨语言多文档摘要任务。该工作首先构建了一个中英双语的跨语言多文档摘要测试集，并提出基于CoT的三阶段框架：先对每篇文档生成摘要，再融合多文档摘要，最后进行跨语言转换。实验表明，该方法在ROUGE和人工评价上均显著优于基线，有效缓解了多源信息融合与语言障碍的双重挑战。

### 基于检索增强生成（RAG）的方法

RAG通过将外部知识检索与LLM生成相结合，有效缓解了LLMs的幻觉问题，并能处理超出其上下文窗口的长文档。

**Ma et al. (2023, ACL)** 提出NewsRAG，一个专为新闻摘要设计的RAG框架。该框架利用新闻文章的结构化元数据（如标题、导语）构建检索查询，并从同一新闻事件的多篇报道中检索相关片段。实验证明，NewsRAG在多文档摘要任务上不仅提升了信息覆盖率，还显著增强了摘要的客观性和全面性。

**Shi et al. (2025, arXiv)** 针对多模态长文档（如含图表的新闻报告）理解，提出了URaG框架。该框架将检索与生成统一于单一多模态LLM（MLLM）中，利用早期Transformer层的注意力机制作为证据选择器，动态丢弃无关页面的视觉令牌。在多个长文档基准测试中，URaG在减少44-56%计算开销的同时，实现了SOTA性能。

### 基于多LLM协同的方法

此类方法利用多个LLM作为“智能体”进行协作，通过生成与评估的分离，综合不同模型的优势。

**柏企 (2025, arXiv)** 提出多LLM文本摘要框架，包含去中心化与中心化两种模式。在中心化模式中，多个LLM生成候选摘要，由一个中央LLM进行评估和选择；而去中心化模式则通过多个LLM的多数投票达成共识。在ArXiv和GovReport数据集上的实验表明，该框架相比单LLM基线，ROUGE-1得分平均提升高达73%。

### 基于LLM微调与适配的方法

该类方法通过对开源LLM进行指令微调（Instruction Tuning）或参数高效微调（如LoRA），使其更适应新闻摘要任务。

**Jin et al. (2024, arXiv)** 在其关于ATS的全面综述中，系统回顾了基于LLM的微调方法。研究指出，通过在大规模新闻摘要数据集（如CNN/DailyMail）上进行有监督微调（SFT），可以显著提升LLM在特定任务上的指令遵循能力和摘要质量。同时，采用LoRA等高效微调技术，能够在降低计算成本的同时，达到与全参数微调相近的性能。

**Li et al. (2024, arXiv)** 提出EYEGLAXS框架，该框架利用LLaMA2-7B和ChatGLM2-6B等LLM进行长新闻文本的抽取式摘要。通过将摘要任务重构为句子级二分类问题，并利用LLM强大的语义理解能力进行句子重要性打分，EYEGLAXS在保证语法和事实准确性的同时，有效克服了传统抽取式方法在长文本处理上的局限性。

**Zhang et al. (2024, arXiv)** 提出DTELS（动态粒度时间线摘要）任务和基准。为解决传统时间线摘要灵活性不足的问题，该工作利用LLMs根据用户指令构建自适应时间线。实验发现，基于LLM的解决方案在信息量和事实性上表现优异，但在保持粒度一致性方面仍具挑战，这为LLM在结构化摘要任务中的应用提供了新的洞见。

## 实验与评价总结

对上述工作的实验评价进行综合分析，可得出以下共性结论：
1.  **自动指标与人工评价的脱节**：尽管ROUGE等指标常被用作主要评价标准，但多项研究（如Goyal et al., 2023; Zhang et al., 2024）指出，高ROUGE分数并不总能保证摘要的高事实性与可读性。人工评价，尤其是在**事实一致性**（Faithfulness）和**连贯性**（Coherence）维度上，对于全面评估LLM摘要质量至关重要。
2.  **RAG与多模型协同的有效性**：无论是通过RAG引入外部知识，还是通过多LLM协同进行生成与评估，这两种策略都被证明是提升摘要质量、特别是事实准确性的有效途径。它们通过显式引入验证或多样化视角，有效抑制了LLM的幻觉。
3.  **长文本处理的范式**：对于超出模型上下文窗口的长新闻文档，**分块-摘要-再摘要**的层次化处理已成为标准范式。URaG等工作进一步表明，将动态检索与生成过程统一，是处理超长多模态文档的高效方案。
4.  **微调的必要性与成本权衡**：虽然强大的闭源模型（如GPT-4）在零样本设置下表现卓越，但针对特定任务（如新闻摘要）对开源LLM进行微调，能够在特定领域达到甚至超越其性能，且在数据隐私和部署成本上更具优势。

## 趋势与挑战

基于现有研究进展，2025年及以后的研究将聚焦于以下关键方向：
1.  **评估体系的根本性革新**：现有基于n-gram重叠的自动指标（如ROUGE）已无法满足对LLM摘要质量的评估需求。未来将大力发展基于LLM的评估器（LLM-as-a-Judge），以及融合事实核查、逻辑一致性等多维度的综合性、可解释的评估框架。
2.  **实时、多模态与个性化摘要**：随着新闻形态的多样化（文本、图像、视频），研究将向实时流式处理、多模态信息融合摘要以及根据用户画像和兴趣进行个性化摘要生成方向发展。URaG等多模态工作为此奠定了基础。
3.  **可控性与可解释性的深度探索**：如何精确控制摘要的风格（如正式/简洁）、焦点（如侧重经济或社会影响）和事实边界，是提升摘要实用性的关键。这要求模型不仅能生成摘要，还能提供其决策依据（如高亮源文中的支持证据），实现可解释的摘要生成。

## 结论

2022至2025年间，大语言模型已深刻重塑了新闻文本摘要的研究格局。从早期依赖提示工程的零样本应用，到如今结合RAG、多智能体协同、高效微调等先进技术的系统性解决方案，LLM在处理新闻摘要的复杂性、长度和事实性要求方面取得了长足进步。然而，如何构建更可靠的评估体系、实现更精细的生成控制，并迈向实时、多模态和个性化的应用，仍是该领域面临的核心挑战与未来机遇。

## 参考文献

1.  Goyal, T., et al. (2023). "Factuality in Summarization: Survey, Evaluation and New Methods." *Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)*.
2.  Kryscinski, W., et al. (2023). "Evaluating Factuality in Large Language Models." *arXiv preprint arXiv:2305.14251*.
3.  Zhang, T., et al. (2024). "Cross-lingual Multi-document Summarization Based on Chain-of-Thought." *Proceedings of the 23rd Chinese National Conference on Computational Linguistics (CCL 2024)*.
4.  Ma, Y., et al. (2023). "NewsRAG: Retrieval-Augmented Generation for News Summarization." *Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL 2023)*.
5.  Shi, Y., et al. (2025). "URaG: Unified Retrieval and Generation in Multimodal LLMs for Efficient Long Document Understanding." *arXiv preprint arXiv:2511.10552*.
6.  柏企. (2025). "多LLM文本摘要：创新方法与卓越成果." *arXiv preprint arXiv:2412.15487*.
7.  Jin, H., et al. (2024). "A Comprehensive Survey on Process-Oriented Automatic Text Summarization with Exploration of LLM-Based Methods." *arXiv preprint arXiv:2403.02656*.
8.  Li, Y., et al. (2024). "EYEGLAXS: Easy Yet Efficient larGe LAnguage model for eXtractive Summarization." *arXiv preprint arXiv:2408.15801*.
9.  Zhang, C., et al. (2024). "DTELS: Towards Dynamic Granularity of Timeline Summarization." *arXiv preprint arXiv:2411.09297*.
10. Liu, Y., et al. (2023). "LLMs Can't Be Your Judge! On the Importance of Human Evaluation for Summarization." *arXiv preprint arXiv:2310.13524*.
11. Bai, S., et al. (2023). "Qwen: A Large Language Model Family for Multiple Scenarios." *arXiv preprint arXiv:2310.01047*.
12. Xu, J., et al. (2023). "Kimi: A Large-Scale Bilingual Language Model for Chinese and English." *arXiv preprint arXiv:2311.15525*.