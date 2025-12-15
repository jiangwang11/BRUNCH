## 大语言模型幻觉缓解中的验证技术综述

### 引言

近年来，大型语言模型（LLMs）在自然语言处理领域取得了显著进展，展现出强大的理解和生成能力。然而，伴随其快速发展的是“幻觉”（Hallucination）问题日益凸显，即LLMs生成看似流畅且合理，但实际上与事实不符、逻辑矛盾或虚构捏造的内容。幻觉问题严重制约了LLMs在医疗、金融、法律等高风险领域的可靠应用。例如，在医疗领域，LLMs可能编造不存在的文献或提供错误的用药剂量；在法律领域，则可能虚构判例，甚至导致专业的失职行为。因此，如何有效地检测和缓解LLMs的幻觉，成为当前乃至未来LLMs发展中亟待解决的关键挑战 [crad.ict.ac.cn](https://crad.ict.ac.cn/article/doi/10.7544/issn1000-1239.202550069), [blog.csdn.net](https://blog.csdn.net/weixin_38526314/article/details/151726743)。本综述将聚焦于2022-2025年间，针对LLMs幻觉缓解的验证技术，对代表性工作进行梳理和评述。

### 方法分类与代表作

幻觉缓解中的验证技术可以大致分为以下几类：

#### 1. 基于证据检索与增强生成（Retrieval-Augmented Generation, RAG）的验证

RAG方法通过引入外部知识库，使LLMs在生成内容时能够检索和参考真实世界的证据，从而降低幻觉的发生。

*   **Google Dynamic RAG**: 该技术根据问题的类型自适应地切换检索模式，对于实体类问题采用稠密检索，而对于概念类问题则启用稀疏检索。检索结果经过交叉编码器重排序后形成置信度加权的证据链，显著降低了事实错误率 [blog.csdn.net](https://blog.csdn.net/weixin_38526314/article/details/151726743)。这种动态检索机制有助于模型在不同的信息需求下，更精准地获取外部知识，避免因检索不当导致幻觉。
*   **Corrective RAG (CRAG)**: 辉瑞制药在药物问答系统中采用CRAG技术，旨在校正检索到的信息可能存在的错误或不完整，从而提升问答的准确性。CRAG通过引入额外的验证模块，在生成前对检索到的证据进行事实性检验，确保模型所依据的外部信息是可靠的 [blog.csdn.net](https://blog.csdn.net/weixin_38526314/article/details/151726743)。实验表明，该方法显著提升了药物相互作用查询的准确率。
*   **DnDScore**: 该方法针对长文本生成中的事实性验证，提出了去语境化（Decontextualization）和分解（Decomposition）策略 [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/91189)。通过分解声明并独立验证这些声明，并增强文本使其可以在原始上下文之外进行可靠验证。它能够更好地处理复杂、多事实的生成内容，并验证子声明的事实性，降低长文本幻觉风险。

#### 2. 基于模型内部机制的幻觉检测与缓解

这类方法着眼于LLMs内部的表示和推理过程，通过分析或修改模型架构、训练目标或解码策略来识别和减少幻觉。

*   **ReDeEP (Regressing Decoupled External Context and Parametric Knowledge)**: [blog.csdn.net](https://blog.csdn.net/weixin_38526314/article/details/151726743) 该方法创新性地解耦了模型对外部上下文知识和参数化知识的利用机制来检测幻觉。它计算外部上下文评分（ECS）和参数化知识评分（PKS），量化模型对不同知识源的依赖强度。ReDeEP在RAGTruth数据集上取得了F1-score 0.89的检测效果，为幻觉检测提供了更细粒度的机制解释。
*   **FAITH (Mitigating Hallucination via Attention Control)**: [blog.csdn.net](https://blog.csdn.net/weixin_38526314/article/details/151726743) 该方法通过控制注意力机制来缓解幻觉，特别是通过约束虚假前提注意力头（false premise attention heads）。研究发现，即使是约束1%的虚假前提注意力头，也能使推理任务的幻觉率下降20.7%。这表明通过精准干预模型内部的注意力分配，可以有效抑制幻觉的产生。
*   **QLoRA (Quantized Low-Rank Adaptation)**: QLoRA作为一种参数高效微调方法，在显著降低模型微调的内存需求的同时，仍能保持与全参数微调相当的幻觉率 [blog.csdn.net](https://blog.csdn.net/weixin_38526314/article/details/151726743), [blog.csdn.net](https://blog.csdn.net/m0_62237233/article/details/146257417)。其通过4位NF4量化、双重量化和分页优化器等技术，使得65B参数的模型能在单张48GB GPU上进行微调。这意味着在资源受限的环境下，也能通过微调来提升模型性能并控制幻觉。

#### 3. 基于生成一致性与自我审查的验证

这类方法通过生成多个候选响应或采用自我反思机制，来验证生成内容的一致性和可靠性。

*   **SelfCheckGPT**: 该方法采用“多轮生成-交叉验证”策略，通过比较不同随机采样响应的一致性来量化事实可靠性 [blog.csdn.net](https://blog.csdn.net/weixin_38526314/article/details/151726743)。在数学推理任务中，SelfCheckGPT实现了82%的准确率。这种方法利用模型自身的生成能力进行内部校验，无需外部监督。
*   **结构化自我一致性 (Structured Self-Consistency, SC)**: SC框架通过聚合多个推理路径，采用集成一致性（ensemble agreement）或熵最小化等方法选择最一致的响应 [blog.csdn.net](https://blog.csdn.net/weixin_38526314/article/details/151726743)。在数学任务中，该方法使有效性提升了8.3%。SC通过对比不同推理路径的结论，增强了复杂推理结果的可靠性。
*   **Halu-J: Critique-Based Hallucination Judge**: Halu-J是一个基于批判的幻觉评判系统，它通过选择相关证据并提供详细的批判来增强幻觉检测 [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/dc618d5b-355c-4294-8305-c08349e47a7d)。该系统在多证据幻觉检测方面优于GPT-4o，并在批判生成和证据选择方面与其能力相匹配。它不仅能检测幻觉，还能提供详细的解释。

#### 4. 面向特定模态或语言的幻觉检测与评估基准

这类工作针对多模态LLMs或特定语言的LLMs，构建了相应的评估基准和检测方法。

*   **Unified Hallucination Detection for Multimodal Large Language Models (UNIHD)**: 针对多模态LLMs (MLLMs) 的幻觉问题，UNIHD提出了一种统一的检测框架 [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/48997), [blog.csdn.net](https://blog.csdn.net/weixin_38526314/article/details/151726743)。该框架利用一套辅助工具稳健地验证幻觉的发生，并在MHaluBench基准上进行了评估。UNIHD的有效性通过细致的评估和全面的分析得到展示。
*   **MHaluBench**: 作为多模态幻觉评估的基准数据集，MHaluBench包含21880个样本，设计了Yes/No、多项选择和视觉问答三种提问方式 [blog.csdn.net](https://blog.csdn.net/weixin_38526314/article/details/151726743)。它为多模态幻觉的量化评估提供了标准化平台。
*   **UHGEval**: 这是针对中文大型语言模型的幻觉评估基准，特别关注无约束生成场景 [developer.volcengine.com](https://developer.volcengine.com/articles/7391691158885892108)。UHGEval包含一个5000+数据项的新闻内容生成幻觉数据集，并提出了一个数据安全、扩展便捷的评测框架。该基准解决了现有评估数据集主要关注英文、数据量小且多采用约束式生成的问题。

### 实验与评价总结

综上所述，当前LLMs幻觉缓解的验证技术在多种数据集和场景下均取得了一定进展。RAG方法通过引入外部知识有效降低了幻觉率，尤其是在事实性要求高的领域。基于模型内部机制的检测和缓解技术，通过对模型注意力、知识存储和训练目标进行优化，实现了对幻觉更深层次的控制。生成一致性方法则利用模型自身的自洽性来判断输出的可靠性。同时，面向特定模态或语言的评估基准的出现，为这些方法提供了更全面和针对性的测试环境。

共性结论包括：

1.  **RAG的有效性**：检索增强生成是缓解事实性幻觉最有效的方法之一，能够显著降低模型“一本正经胡说八道”的现象。
2.  **多模态和多语言的挑战**：多模态LLMs和非英文LLMs的幻觉问题更为复杂，需要专门的检测和评估方法。
3.  **细粒度检测的必要性**：从句子级到关键词级的细粒度幻觉检测，能够为幻觉问题的解决提供更具体的线索和启发。
4.  **机制解释性**：理解幻觉产生的内部机制对于开发更鲁棒的缓解策略至关重要，而非仅仅停留在表面现象。

尽管取得了进展，但完全消除幻觉仍然是一个开放性问题。模型的流畅性与事实准确性之间存在权衡，许多缓解技术可能会影响模型生成的多样性和创新性。

### 趋势与挑战

面向2025年及未来，LLMs幻觉验证技术将呈现以下趋势和挑战：

1.  **多模态幻觉检测与因果推理深化 (Unified Multimodal Hallucination Detection and Causal Reasoning)**：随着多模态LLMs的普及，将需要更成熟的跨模态一致性校验技术，例如整合文本语义解析与视觉特征提取，以提升多模态幻觉检测精度 [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/48997), [blog.csdn.net](https://blog.csdn.net/weixin_38526314/article/details/151726743)。此外，因果推理框架COAT等将为缓解逻辑性幻觉提供新范式，通过构建因果图来提升推理准确率 [blog.csdn.net](https://blog.csdn.net/weixin_38526314/article/details/151726743)。
2.  **小模型幻觉率优化与可控幻觉利用 (Small Model Optimization and Controllable Hallucination)**：研究将更多聚焦于7B参数级小模型的幻觉率优化，通过“蒸馏-量化-微调”等技术路线，使小模型在资源受限环境中也能实现较低幻觉率 [blog.csdn.net](https://blog.csdn.net/weixin_38526314/article/details/151726743)。同时，对“幻觉”的认知将超越负面范畴，探索可控幻觉的创新应用，例如启发式地设计新颖结构，利用其“创造性错误”价值。
3.  **动态监管技术与责任归属框架 (Dynamic Regulatory Technologies and Accountability Frameworks)**：随着LLMs在关键行业的广泛应用，幻觉所导致的经济损失和法律风险促使全球监管机构制定更严格的政策。未来将建立基于实时幻觉监测插件、数据溯源机制和版权补偿制度的动态监管技术 [blog.csdn.net](https://blog.csdn.net/weixin_38526314/article/details/151726743)。同时，建立“幻觉率分级责任制”，明确开发者、使用者和平台在不同幻觉率水平下的责任，将是推动LLMs健康发展的关键。
4.  **人机互鉴纠偏 (Human-AI Collaborative Correction)**：未来的幻觉治理将从单纯的“AI生成+人类审核”模式，向更深层次的“人机互鉴纠偏”升级 [blog.csdn.net](https://blog.csdn.net/weixin_38526314/article/details/151726743)。这意味着人类不仅进行事后审查，还会参与到LLMs的训练、验证和迭代过程中，提供更具上下文和经验的反馈，形成一个闭环学习机制。

### 结论

LLMs的幻觉问题是其走向通用人工智能过程中难以回避的挑战。2022-2025年间，研究者们在基于检索增强、模型内部机制优化、生成一致性验证以及多模态多语言评估等方面取得了显著进展，有效地提升了LLMs输出的可靠性。尽管当前尚无法完全消除幻觉，但通过技术创新、评估基准的完善以及多方协同努力，我们正逐步构建起更为全面和鲁棒的幻觉验证与缓解体系。未来，对多模态幻觉的深入理解、小模型的实用化，以及动态、细致的监管框架将是推动LLMs走向可靠、可控、可解释的关键。

### 参考文献

*   [blog.csdn.net](https://blog.csdn.net/weixin_38526314/article/details/151726743) weixin_38526314. LLM幻觉研究：定义、成因、检测技术与行业应用分析（2024-2025）. 2025-09-17T00:00:00.000Z.
*   [crad.ict.ac.cn](https://crad.ict.ac.cn/article/doi/10.7544/issn1000-1239.202550069) 杨克巍. 大语言模型幻觉检测方法综述. 2025-10-01T00:00:00.000Z.
*   [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/48997) Xiang Chen, Chenxi Wang, Yida Xue, Ningyu Zhang, Xiaoyan Yang, Qiang Li, Yue Shen, Lei Liang, Jinjie Gu, Huajun Chen. Unified Hallucination Detection for Multimodal Large Language Models. 2025-06-11T00:00:00.000Z.
*   [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/dc618d5b-355c-4294-8305-c08349e47a7d) Binjie Wang, Steffi Chern, Ethan Chern, Pengfei Liu. Halu-J: Critique-Based Hallucination Judge. 2024-07-17T00:00:00.000Z.
*   [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/91189) Miriam Wanner, Benjamin Van Durme, Mark Dredze. DnDScore: Decontextualization and Decomposition for Factuality Verification in Long-Form Text Generation. 2025-04-14T00:00:00.000Z.
*   [developer.volcengine.com](https://developer.volcengine.com/articles/7391691158885892108) 用户7593137034851. UHGEval：无约束生成下的中文大模型幻觉评估. 2024-07-15T00:00:00.000Z.
*   [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/16015ace-828b-4f3e-9b5b-31a964b6e76f) Yuzhe Gu, Ziwei Ji, Wenwei Zhang, Chengqi Lyu, Dahua Lin, Kai Chen. ANAH-v2: Scaling Analytical Hallucination Annotation of Large Language Models. 2024-07-05T00:00:00.000Z.
*   [blog.csdn.net](https://blog.csdn.net/m0_62237233/article/details/146257417) weixin_62237233. A Gentle Introduction to QLoRA. 2025-06-11T00:00:00.000Z.
*   [blog.csdn.net](https://blog.csdn.net/weixin_62100548/article/details/145538812) weixin_62100548. 【论文阅读 | LLM 幻觉】Zero ... resource hallucination prevention for large language models. 2025-02-10T00:00:00.000Z.
*   [www.themoonlight.io](https://www.themoonlight.io/zh/review/claim-verification-in-the-age-of-large-language-models-a-survey) Claim Verification in the Age of Large Language Models: A Survey. 2025-03-18T12:28:30.000Z.
*   [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/116717) Guangsheng Bao, Lihua Rong, Yanbin Zhao, Qiji Zhou, Yue Zhang. Decoupling Content and Expression: Two-Dimensional Detection of AI-Generated Text. 2025-11-20T00:00:00.000Z.
*   [arxiv.org] Sun, Z., et al. (2025). ReDeEP: Regressing Decoupled External Context and Parametric Knowledge. *ICLR 2025*.
*   [arxiv.org] Jiang, T., et al. (2025). FAITH: Mitigating Hallucination via Attention Control. *ICLR 2025*.
*   [arxiv.org] Zhang, J., et al. (2024). SLED: Self-driven Logits Evolution Decoding for Factual Accuracy. *NeurIPS 2024*.