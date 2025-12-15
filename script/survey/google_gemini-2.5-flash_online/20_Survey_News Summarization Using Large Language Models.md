好的，这是一篇关于2022-2025年新闻摘要生成的大语言模型（LLMs）中文学术综述。

## 新闻摘要生成的大语言模型研究综述 (2022-2025)

### 引言

随着互联网信息的爆炸式增长，新闻文本作为一种重要信息来源，其数量庞大且更新迅速。自动新闻摘要技术旨在将冗长的新闻内容压缩成简洁、连贯且信息丰富的短文本，以帮助用户高效获取关键信息，缓解信息过载问题。传统摘要技术包括抽取式和生成式两大类，其中生成式摘要侧重于理解原文语义并重新组织生成全新内容，更具挑战性也更符合人类阅读习惯 [hanspub.org](https://pdf.hanspub.org/csa_1543819.pdf)。近年来，大型语言模型（LLMs）的快速发展，凭借其强大的语言理解、生成和少量样本学习能力，为新闻摘要领域带来了突破性的进展。本综述将聚焦2022年至2025年期间，基于LLMs的新闻摘要生成方面的代表性研究工作，对其核心方法、实验结论进行梳理与总结，并探讨未来的发展趋势与挑战。

### 方法分类与代表作

本节将新闻摘要生成的大语言模型方法分为以下几类，并介绍最具代表性的工作。

#### 1. 基于Seq2Seq架构的增强型模型

此类方法在Encoder-Decoder框架，特别是Transformer结构的基础上，通过引入注意力机制、双向编码器等改进，提升模型对新闻文本语义的捕捉及摘要生成的质量。

*   **《基于双向GRU与Attention机制的改进Seq2Seq自动文本摘要模型研究》 (2025)** [hanspub.org](https://pdf.hanspub.org/csa_1543819.pdf)
    该研究旨在提升传统Seq2Seq模型在文本摘要任务中的性能。文章提出了一种结合双向门控循环单元（BiGRU）和注意力机制的改进型Seq2Seq模型。BiGRU编码器能充分捕获上下文语义的前向和后向依赖信息，而注意力机制则使解码器在生成每个词时能动态关注与当前预测最相关的输入部分。在CNN/Daily Mail数据集上的ROUGE指标评估显示，改进模型在摘要质量和信息覆盖度方面均优于传统Seq2Seq模型，ROUGE-1和ROUGE-L指标有显著提升。

#### 2. 基于预训练语言模型（PLMs）的微调与知识增强

PLMs（如BERT、T5等）在海量语料上预训练，具备强大的语言表示能力，通过在特定摘要任务上进行微调或结合外部知识，可显著提高新闻摘要性能。

*   **《Multi-Document Summarization Based on Entity Information Enhancement and Multi-Granularity Fusion》 (2022)** [aclanthology.org](https://aclanthology.org/2022.ccl-1.15.pdf)
    该研究关注多文档摘要中预训练模型捕获事实性知识不足以及事实一致性问题。作者提出了基于实体信息增强和多粒度融合的多文档摘要模型MGNIE，将实体关系信息融入ERNIE预训练模型，增强知识事实以获得多层语义信息。模型在词、实体和句子多种粒度上进行融合建模，以捕捉长文本摘要生成所需关键信息。在MultiNews数据集上的实验表明，MGNIE模型在ROUGE-1、ROUGE-2和ROUGE-L指标上均显著优于强基线模型，提升了摘要的事实一致性。
*   **《基于三元组信息指导的生成式文本摘要研究》 (2023)** [bhxb.buaa.edu.cn](https://bhxb.buaa.edu.cn/bhzk/article/doi/10.13700/j.bh.1001-5965.2022.0896)
    该工作旨在解决生成式文本摘要模型在解码时对文本事实性信息利用不充分的问题。研究提出了一种以事实三元组为指导的文本摘要模型SPOATS，该模型基于Transformer结构，包含具有事实提取能力的双编码器和融合事实特征的解码器。通过构建LTP-BiLSTM-GAT模型并设计最优事实三元组选择算法，从中文文本中提取事实三元组，并利用改进的S-BERT模型进行句子级向量表示。实验在LCSTS数据集上进行，结果显示SPOATS模型相比基线模型ERPG，ROUGE-1值提升了2.0%，显著改善了摘要质量。
*   **《Improving Biomedical Abstractive Summarisation with Knowledge Aggregation》 (2023)** [blog.csdn.net](https://blog.csdn.net/yuyuyu_xxx/article/details/134953365)
    尽管此论文针对生物医学领域，其通过知识聚合增强抽象摘要的方法对新闻摘要领域具有借鉴意义。研究旨在通过聚合源文章引用的外部论文知识来提高抽象摘要的性能。作者提出了一种基于注意力的引文聚合模型，该模型将引文论文中的特定领域知识集成到神经模型中。通过对引文摘要应用注意力机制，模型能动态聚合引文知识与主论文内容，为摘要解码提供附加功能。大规模生物医学数据集上的实验证明，该模型在抽象生物医学文本摘要方面取得了实质性改进。

#### 3. 提示工程（Prompt Engineering）与上下文工程（Context Engineering）

利用LLMs进行新闻摘要，尤其是黑盒LLMs，提示工程成为关键。通过精心设计的提示词或指令，引导模型生成高质量摘要。更进一步，上下文工程系统性地优化提供给LLMs的信息内容。

*   **《Prompting LLMs with content plans to enhance the summarization of scientific articles》 (2024)** [blog.csdn.net](https://blog.csdn.net/weixin_44362044/article/details/141754202)
    该研究探讨如何通过内容计划提示来增强LLMs在科学文章摘要方面的性能。论文引入了新颖的提示技术，向摘要器提供从文章中提取的关键术语列表（如作者关键词、KeyBERT生成的术语等），以指导摘要生成。研究将此提示技术应用于LongT5、LED和BigBirdPegasus等基于Transformer的模型，并测试了不同输入文本（如引言+讨论、单独章节）。实验结果表明，提示技术能持续提高小型模型，尤其是在独立总结章节时的性能，且当输入不相关提示时，小型模型性能下降，表明其对提示信息存在依赖。
*   **《DTELS: Towards Dynamic Granularity of Timeline Summarization》 (2024)** [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/76321)
    这项研究关注时间线摘要中缺乏满足多样化粒度需求的灵活性问题。研究提出了一种新的动态粒度时间线摘要（DTELS）范式，旨在根据用户的指示或需求构建自适应时间线。文章建立了一个全面的DTELS基准，包括评估框架和大规模、多源数据集。实验评估了基于LLMs和现有最先进时间线摘要方法的解决方案，结果显示基于LLM的解决方案具有一定有效性，但即使是先进的LLM也难以始终生成兼具信息丰富性和粒度一致性的时间线，这突显了任务的挑战性。这暗示了在控制摘要粒度方面，LLMs需要更精细的提示或上下文工程。
*   **《A Survey of Context Engineering for Large Language Models》 (2025)** [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/1a3763b7-6e29-4e77-ad27-5a1337b23b24)
    该综述正式提出了“上下文工程”（Context Engineering）这一研究领域，认为LLMs的性能根本上取决于推理过程中提供的上下文信息，其超越了简单的提示设计，旨在系统性地优化提供给LLMs的信息内容。文章构建了一个全面的分类体系，分解了上下文的检索与生成、上下文处理及管理等基础组成部分，并研究了它们在RAG、记忆系统、工具集成推理及多智能体系统等高级实现中的整合方式。通过对逾1300篇论文的分析，该综述揭示了当前模型在复杂上下文理解与生成同样复杂长篇输出之间的能力不对称，为未来研究指明了方向。新闻摘要作为一种需要精细信息控制的任务，将高度受益于上下文工程的发展。

### 实验与评价总结

针对基于LLMs的新闻摘要生成研究，ROUGE（Recall-Oriented Understudy for Gisting Evaluation）系列指标（ROUGE-1、ROUGE-2、ROUGE-L）被广泛用于自动评估摘要的质量，衡量生成摘要与参考摘要之间的N-gram重叠、最长公共子序列等。这些指标可以从信息覆盖度和语义保留方面量化模型的性能。在多个研究中，当引入实体信息增强、多粒度融合或特定的提示策略时，模型的ROUGE得分普遍呈上升趋势，表明这些方法能有效提升摘要的信息量和连贯性。

除了自动评估，人工评价也作为重要的补充，从流畅性（Fluency）、信息量（Informativeness）和与原文的事实忠实度（Faithfulness）等维度对摘要进行主观打分。研究发现LLMs生成的摘要在语法、可读性方面通常表现良好，但在处理复杂的事实性信息时仍可能出现“幻觉”现象，即生成与原文不符的内容 [bhxb.buaa.edu.cn](https://bhxb.buaa.edu.cn/bhzk/article/doi/10.13700/j.bh.1001-5965.2022.0896)。知识增强和检索增强生成（RAG）方法被证明可以有效缓解这一问题，提升摘要的事实一致性 [aclanthology.org](https://aclanthology.org/2022.ccl-1.15.pdf)。同时，对于小型模型而言，恰当的提示能够显著弥补其表示能力上的不足，使其在特定任务上获得与大型模型接近的性能 [blog.csdn.net](https://blog.csdn.net/weixin_44362044/article/details/141754202)。这表明不同的模型架构、提示策略和知识整合方式，其对摘要质量的提升效果和侧重点有所不同。

### 趋势与挑战

2025年前后，新闻摘要生成的大语言模型研究呈现出以下关键趋势与挑战：

1.  **动态粒度与个性化摘要的深度探索：** 随着LLMs能力的增强，研究将更加聚焦于根据用户需求、场景或话题，生成具有动态粒度、自定义长度和侧重点的个性化新闻摘要。DTELS等工作的出现已初步体现这一趋势 [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/76321)。挑战在于如何精准捕捉用户意图，并有效控制LLM生成内容以满足精细化的粒度要求。
2.  **多模态与多源信息融合：** 现有新闻多以文本形式呈现，但未来新闻摘要将融合图片、视频、图表等多模态信息。研究将深入探索如何将不同模态的关键信息有效提取并整合到文本摘要中。同时，面对同一新闻事件来自不同源头的报道，如何进行冲突消解、观点融合并生成全面客观的综合摘要将是重要方向 [zhuanzhi.ai](https://www.zhuanzhi.ai/paper/de6ca177ce6855afe039c8fc7611fd91)。
3.  **可解释性、事实一致性与“幻觉”缓解：** LLMs的“黑箱”特性和潜在的“幻觉”问题在高风险应用领域（如医疗新闻）中是不容忽视的挑战。未来的研究将致力于提升摘要生成的可解释性，例如通过高亮原文证据、提供溯源路径等方式。同时，检索增强生成（RAG） [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/1a3763b7-6e29-4e77-ad27-5a1337b23b24) [ywlxbx.whuznhmedj.com](https://ywlxbx.whuznhmedj.com/journal/481.html) 和知识图谱增强将是解决事实不一致和“幻觉”问题的关键技术，确保新闻摘要的准确性和可靠性。
4.  **上下文工程的深化应用：** 随着LLMs上下文窗口的扩展，如何高效利用、管理和优化上下文信息变得至关重要。上下文工程将为新闻摘要任务提供更系统的框架，以检索、生成和处理大规模上下文，从而引导LLM生成更精准、更全面的摘要 [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/1a3763b7-6e29-4e77-ad27-5a1337b23b24)。

### 结论

综上所述，2022年至2025年期间，新闻摘要生成领域在大语言模型的推动下取得了显著进步。从增强传统Seq2Seq模型、利用PLMs进行微调和知识增强，到发展精巧的提示工程和上下文工程，研究者们不断探索提升摘要质量、事实一致性及用户体验的方法。尽管ROUGE指标和人工评估普遍证实了LLMs在新闻摘要中的强大潜力，但动态粒度控制、多模态融合以及对“幻觉”问题的进一步缓解仍是未来研究的核心挑战。随着LLMs技术的持续演进和对上下文工程的深入理解，新闻摘要技术有望发展出更加智能、可信赖和高度个性化的解决方案。

### 参考文献

*   Chenlong Zhang, Tong Zhou, Pengfei Cao, et al. (2024). DTELS: Towards Dynamic Granularity of Timeline Summarization. [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/76321)
*   Li Y. (2023). 基于三元组信息指导的生成式文本摘要研究 (Research on abstractive text summarization based on triplet information guidance). *Journal of Beijing University of Aeronautics and Astronautics*. [bhxb.buaa.edu.cn](https://bhxb.buaa.edu.cn/bhzk/article/doi/10.13700/j.bh.1001-5965.2022.0896)
*   Mei, L., Yao, J., Ge, Y., et al. (2025). A Survey of Context Engineering for Large Language Models. [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/1a3763b7-6e29-4e77-ad27-5a1337b23b24)
*   Song Mengpeng, Bai Haiyan. (2025). 基于大语言模型的文献综述智能生成与循证研究 (Research on Intelligent Generation and Evidence Based of Literature Review Based on Large Language Model). *Data Analysis and Knowledge Discovery*. [manu44.magtech.com.cn](https://manu44.magtech.com.cn/Jwk_infotech_wk3/CN/10.11925/infotech.2096-3467.2024.0628)
*   Tang, J., Liu, M., Zhao, T., & Zhou, J. (2022). 基于实体信息增强及多粒度融合的多文档摘要 (Multi-Document Summarization Based on Entity Information Enhancement and Multi-Granularity Fusion). CCL 2022. [aclanthology.org](https://aclanthology.org/2022.ccl-1.15.pdf)
*   yuyuyu_xxx. (2023). EMNLP 2023 | 02 Improving Biomedical Abstractive Summarisation with Knowledge Aggregation. [blog.csdn.net](https://blog.csdn.net/yuyuyu_xxx/article/details/134953365)
*   许美玲, 裘天瑜. (2025). 基于双向GRU与Attention机制的改进Seq2Seq自动文本摘要模型研究 (A Bidirectional GRU and Attention-Based Improved Seq2Seq Model for Automatic Text Summarization). *Computer Science and Application*. [hanspub.org](https://pdf.hanspub.org/csa_1543819.pdf)
*   未然AI. (2024). 摘要生成—通过关键术语提示方法微调LLM模型. [blog.csdn.net](https://blog.csdn.net/weixin_44362044/article/details/141754202)
*   金哲, 邹健, 李逍, 吕嘉欣, 胡中旭, 冯达. (2025). 检索增强生成技术在医学人工智能中的应用与前沿探索. *药物流行病学杂志*. [ywlxbx.whuznhmedj.com](https://ywlxbx.whuznhmedj.com/journal/481.html)
*   Zhang, Z., Shu, C., Chen, Y., Xiao, J., Zhang, Q., & Zheng, L. (2022). ICAF: Iterative Contrastive Alignment Framework for Multimodal Abstractive Summarization. [zhuanzhi.ai](https://www.zhuanzhi.ai/paper/de6ca177ce6855afe039c8fc7611fd91)