好的，遵照您的指示，以下是关于「生成式AI在临床文档系统中的应用」的学术综述。

***

### 摘要
生成式人工智能（Generative AI），特别是大型语言模型（LLMs）和多模态基础模型，正在深刻变革临床文档的生成与管理。本综述旨在系统梳理 2022 年至 2025 年间，生成式AI在临床文档系统领域的代表性研究工作。本文首先概述了该领域面临的信息过载与效率瓶颈，随后将相关方法分为三类：早期编码器-解码器框架、基于大型语言模型（LLM）的报告生成，以及以数据为中心的结构化提取与系统演进。通过对代表性论文的深入分析，我们总结了当前方法的实验范式、评价指标的演变以及核心挑战。最后，本综述预测了未来的三大研究趋势：从静态生成到“AI住院医师”式交互、多模态融合与数据-模型协同演进、模型的可解释性与治理。

### 1. 引言

随着现代医学的发展，电子健康记录（EHR）、医学影像、基因组学数据等临床信息呈爆炸式增长，给临床医生的文档处理工作带来了沉重负担 [blog.csdn.net](https://blog.csdn.net/weixin_58753619/article/details/146640682)。传统的临床文档流程，如人工撰写放射学报告、病理报告和出院小结，不仅耗时费力，且难以保证一致性和标准化。生成式人工智能（Generative AI），尤其是基于 Transformer 架构的大型语言模型（LLMs）和视觉-语言模型（VLMs），凭借其强大的文本理解、推理与生成能力，为自动化和优化临床文档流程提供了变革性机遇 [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/204361)。

近年来，学术界致力于将GenAI应用于临床文档的自动化生成、结构化信息提取以及临床决策支持。这些工作不仅旨在提升临床效率，也探索了改善医患沟通和医学教育的新范式。本综述将聚焦于 2022 年至 2025 年间，对生成式AI在临床文档系统中的应用进行分类梳理，总结其核心方法、评价体系与共性挑战，并展望未来的发展方向。

### 2. 方法分类与代表作

根据技术范式和应用目标的演进，可将生成式AI在临床文档系统中的应用分为三类：

#### 2.1 早期编码器-解码器框架与扩展

在大型语言模型普及前，该领域主要采用“视觉编码器-语言解码器”架构。这类方法通常使用卷积神经网络（CNN）或视觉Transformer（ViT）提取图像特征，再由循环神经网络（RNN）或小型Transformer生成文本报告。尽管后续研究通过引入注意力机制、知识图谱等方式不断优化，但其生成文本的流畅度和上下文理解能力有限。

*   **ExBEHRT (Rupp et al., 2023)**：该研究旨在解决传统基于BERT的模型（如BEHRT）仅能处理有限类型EHR数据的问题。ExBEHRT通过一种新颖的特征统一方法，将人口统计学、生命体征、实验室检测等多模态、不同频率的EHR记录整合到Transformer模型中，以预测疾病亚型和进展 [zhuanzhi.ai](https://www.zhuanzhi.ai/paper/3b7093b5b5036f8c3245737fc388c8d1)。实验证明，增加多模态特征能显著提升模型在不同疾病下游任务中的性能。该工作通过对模型表征进行聚类，发现模型能够隐式理解疾病，并将相同癌症类型的患者有效分入不同风险组。

*   **UniXGen (Lee et al., 2023)**：该研究致力于解决医学影像数据隐私敏感和标注成本高的问题，提出一个统一模型同时处理胸部X光图像生成与报告生成。UniXGen采用矢量量化（Vector Quantization）将X光图像离散化为视觉词元（visual tokens），从而将图像与文本生成统一为序列到序列任务 [zhuanzhi.ai](https://www.zhuanzhi.ai/paper/7af0abe9ece781b173b57ba3bb04be42)。模型引入特殊视图词元，使其能生成指定视角（如前后位、侧位）的图像，并支持从单视角或多视角输入生成报告。实验表明，这种统一的双向生成模型在两项任务上均表现出协同增强效应，优于单一任务模型。

#### 2.2 基于大型语言模型（LLM）的报告生成

随着GPT-4等大型基础模型的出现，研究范式转向利用LLMs强大的知识储备、推理和语言组织能力。LLMs被用作更强大的语言解码器，或作为视觉-语言模型（VLM）的核心，直接处理多模态输入并生成高质量的临床报告。

*   **GenMI (Rao et al., 2025)**：这篇发表于《Nature》的综述性文章探讨了生成式医学影像（GenMI）在放射学、心脏病学、病理学等多专科报告生成中的应用 [blog.csdn.net](https://blog.csdn.net/weixin_58753619/article/details/146640682)。研究问题是如何利用基础模型（如GPT-4V、Gemini）实现跨模态、跨专科的自动化报告生成。文章倡导一种“AI住院医师”范式，即AI不仅起草报告，还能与临床医生进行交互式问答，辅助诊断和医学教育。文章总结出现有LLMs直接应用于医学图像解读时，在临床准确性上仍有不足，且存在“幻觉”现象，亟需建立更有效的评估指标。

*   **GPT-4医疗任务评估 (Goh et al., 2025)**：该研究通过一项随机对照试验，评估了GPT-4在辅助医生处理复杂临床管理任务（管理推理）时的表现，这些任务深度依赖于对临床文档的综合理解 [cloud.tencent.com.cn](https://cloud.tencent.com/developer/article/2516415?policyId=1004)。研究核心方法是将92名执业医师随机分为两组，一组仅使用传统资源（如UpToDate），另一组可使用GPT-4辅助。关键结论是：在专家制定的评分标准下，使用GPT-4辅助的医生组得分显著高于对照组（平均分差异6.5%），证明了LLM在提高临床管理推理质量方面的潜力。

#### 2.3 以数据为中心的结构化提取与系统演进

除了生成自由文本报告，另一个关键方向是如何从非结构化的临床文本中提取结构化信息（如命名实体识别），并构建能够持续演进的AI系统。这类方法强调数据质量、治理以及人机协同。

*   **基于LLM的中文医学命名实体识别 (Lv et al., 2025)**：该研究针对中文医学文本中实体边界模糊和嵌套结构复杂的问题，探索了利用LLM进行命名实体识别（NER）的方法 [aclanthology.org](https://aclanthology.org/2025.ccl-1.9.pdf)。核心方法是将NER任务重构为文本生成任务，设计了一种能够同时处理平面和嵌套实体的“符号标注策略”进行模型微调。该方法还引入实体筛选器和基于LLM决策的多模型集成分模块，以过滤错误实体并提升鲁棒性。在CMeEE-V2和CCKS2019数据集上的实验表明，该方法F1值分别达到0.7785和0.8821，优于传统的序列标注模型。

*   **SAGE-Health (Chen et al., 2025)**：该研究提出了一个以数据为中心的范式，旨在解决GenAI在医疗领域部署时面临的数据碎片化和生命周期管理不足的挑战 [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/204361)。其核心方法是构建一个可持续、自适应的医疗数据生态系统（SAGE-Health），将数据视为与模型共同演化的动态组成部分，而非静态输入。该系统通过语义向量搜索和上下文查询，为上游模型预训练提供高质量多模态数据，并作为下游应用的知识检索后端。其闭环设计允许临床医生的反馈持续优化数据质量和模型性能，确保系统能够长期保持临床相关性。

### 3. 实验与评价总结

*   **数据集**：胸部X光报告生成任务普遍采用公开数据集 **MIMIC-CXR**，其包含大量图像-报告对。针对特定语言和任务，研究也使用了如中文医学信息处理评测（CBLUE）中的 **CMeEE** 和 **CCKS** 系列数据集 [aclanthology.org](https://aclanthology.org/2025.ccl-1.9.pdf)。然而，现有研究普遍面临高质量、大规模、多模态、纵向随访数据集稀缺的挑战，这限制了模型处理复杂临床场景和罕见病的能力 [blog.csdn.net](https://blog.csdn.net/weixin_58753619/article/details/146640682)。

*   **评价指标**：评价体系正从单纯的自然语言生成（NLG）指标向临床准确性指标演进。早期研究多采用 **BLEU、ROUGE、METEOR** 等衡量文本重叠度的指标，但这些指标无法评估生成内容的临床正确性。因此，后续研究开始引入基于知识图谱的临床实体匹配指标（如**RadGraph F1**）和由专家放射科医生评估的错误评分（如**RadCliQ**）。最终，**人类专家盲审**被认为是评估模型临床可行性的黄金标准，包括评估报告的准确性、完整性和是否存在潜在危害 [blog.csdn.net](https://blog.csdn.net/weixin_58753619/article/details/146640682)。

*   **共性结论**：
    1.  **性能权衡**：在临床准确性与报告流畅度之间存在权衡。过度优化NLG指标可能导致模型生成通用、模板化的文本，而牺牲对具体影像发现的精确描述 [blog.csdn.net](https://blog.csdn.net/weixin_58753619/article/details/146640682)。
    2.  **幻觉问题**：LLMs和VLMs普遍存在“幻觉”（Hallucination）现象，即生成与事实不符的内容，如错误引用不存在的既往检查、描述图像中没有的病灶等。这是其临床应用的最大障碍之一 [zhuanzhi.ai](https://www.zhuanzhi.ai/vip/04d99974942eb847068ab686cc6507d8)。
    3.  **人机协同优势**：在包含人类反馈的闭环系统中，AI的性能得到持续提升。临床医生在使用AI工具辅助时，决策质量和工作效率均有改善，体现了“人机协同”模式的巨大价值 [cloud.tencent.com.cn](https://cloud.tencent.com/developer/article/2516415?policyId=1004)。

### 4. 趋势与挑战

基于当前的研究进展，预计2025年前后，该领域将呈现以下主要趋势与挑战：

1.  **从静态生成到“AI住院医师”式交互**：AI的角色将从离线的报告撰写工具，转变为能够实时交互的临床助手，即“AI住院医师”（AI Resident） [blog.csdn.net](https://blog.csdn.net/weixin_58753619/article/details/146640682)。这意味着模型不仅要生成报告，还要能对报告内容进行解释、回答主治医生或患者的提问、基于图像定位异常区域、对比历史病例，并辅助医学教育与培训。这要求模型具备更强的多轮对话、上下文理解和溯源能力。

2.  **多模态融合与数据-模型协同演进**：未来的系统将更深度地融合文本、影像、EHR、基因组学等多源异构数据，以进行更全面的临床推理。研究重点将从模型架构创新转向构建动态、可持续的数据生态系统 [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/204361)。这种以数据为中心的范式强调通过持续的临床反馈和自动化数据治理，实现数据与模型的共同演化，确保模型在真实临床环境中的长期有效性和适应性。

3.  **可解释性、治理与偏见消减成为核心议题**：随着模型在临床决策中的权重增加，其“黑箱”特性变得不可接受。研究将更加关注生成内容的可解释性（如将文本发现与图像区域精确对应）和可归因性（确保信息来源可靠）。同时，如何有效评估和减轻模型在训练数据中习得的偏见、防止其生成有害或不准确的建议，以及建立符合法规（如《生成式人工智能服务管理暂行办法》）的治理框架，将成为能否安全部署的关键 [xhyxzz.pumch.cn](https://xhyxzz.pumch.cn/cn/article/pdf/preview/10.12290/xhyxzz.2024-0315.pdf)。

### 5. 结论

生成式AI在临床文档系统中的应用正经历从单一、辅助性任务向综合、交互式角色的深刻转变。2022-2025年的研究表明，技术范式已从传统的编码器-解码器架构演进为以大型多模态基础模型为核心的系统，应用重点也从单纯的报告自动化生成，扩展到结构化数据提取和动态决策支持。尽管在临床准确性、模型幻觉和数据质量方面仍面临严峻挑战，但未来的研究趋势清晰地指向更具交互性、多模态融合和可信赖的“AI住院医师”模式。通过构建人机协同的闭环生态系统，并建立严格的评估与治理标准，生成式AI有望安全、有效地重塑临床文档工作流，最终提升医疗服务质量与效率。

### 6. 参考文献

1.  [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/204361) Chen, G., Liu, C., Ooi, G. A., et al. (2025). Generative AI for Healthcare: Fundamentals, Challenges, and Perspectives. arXiv preprint.
2.  [xhyxzz.pumch.cn](https://xhyxzz.pumch.cn/cn/article/pdf/preview/10.12290/xhyxzz.2024-0315.pdf) 陈子佳, 彭文茜, 张德政, 等. (2025). 大语言模型在中医药领域的应用、挑战与前景. 协和医学杂志, 16(1), 83-89.
3.  [blog.csdn.net](https://blog.csdn.net/weixin_58753619/article/details/146640682) Rao, V. M., Topol, E. J., & Rajpurkar, P. (2025). Generative artificial intelligence for medical report generation. *Nature*, s41586-025-08675-y.
4.  [cloud.tencent.com.cn](https://cloud.tencent.com.cn/developer/article/2516415?policyId=1004) Goh, E., Rodman, A., et al. (2025). GPT-4 assistance for improvement of physician performance on patient care tasks: a randomized controlled trial. *Nature Medicine*.
5.  [zhuanzhi.ai](https://www.zhuanzhi.ai/vip/04d99974942eb847068ab686cc6507d8) 董悦, 等. (2025). 视觉语言大模型的幻觉综述：成因、评估与治理. *计算机研究与发展*.
6.  [zhuanzhi.ai](https://www.zhuanzhi.ai/paper/3b7093b5b5036f8c3245737fc388c8d1) Rupp, M., Peter, O., & Pattipaka, T. (2023). ExBEHRT: Extended Transformer for Electronic Health Records to Predict Disease Subtypes & Progressions. *ICLR 2023 Workshop on Trustworthy Machine Learning for Healthcare*.
7.  [zhuanzhi.ai](https://www.zhuanzhi.ai/paper/7af0abe9ece781b173b57ba3bb04be42) Lee, H., Lee, D. Y., Kim, W., et al. (2023). UniXGen: A Unified Vision-Language Model for Multi-View Chest X-ray Generation and Report Generation. *arXiv preprint*.
8.  [aclanthology.org](https://aclanthology.org/2025.ccl-1.9.pdf) 吕腾啸, 罗凌, 吕慧怡, 等. (2025). 基于大语言模型的中文医学命名实体识别. *中国计算语言学大会 (CCL 2025)*.
9.  [zhuanzhi.ai](https://www.zhuanzhi.ai/vip/f15b0fa5f13d42ba34af44aced1a81fa) Zhou, Z., & Feng, X. (2025). From Hypothesis to Publication: A Comprehensive Survey of AI-Driven Research Support Systems. *arXiv preprint*.
10. [zhuanzhi.ai](https://www.zhuanzhi.ai/paper/9ba124c2b2f92baf69413b1bd56f2652) Huang, H., Wang, S., Liu, H., et al. (2024). Benchmarking Large Language Models on Communicative Medical Coaching: a Novel System and Dataset. *arXiv preprint*.
11. Li, J., Fei, H., Liu, J., et al. (2022). Unified named entity recognition as word-word relation classification. *Proceedings of the AAAI Conference on Artificial Intelligence*.
12. Chen, P., Zhang, M., Yu, X., & Li, S. (2022). Named entity recognition of chinese electronic medical records based on a hybrid neural network and medical mc-bert. *BMC medical informatics and decision making*.
13. Zhang, N., Chen, M., Bi, Z., et al. (2021). Cblue: A chinese biomedical language understanding evaluation benchmark. *arXiv preprint arXiv:2106.08087*.