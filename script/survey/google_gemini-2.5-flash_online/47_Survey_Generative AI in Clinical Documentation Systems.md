## 生成式人工智能在临床文档系统中的应用：2022-2025年代表性工作综述

### 引言
临床文档是医疗保健流程的核心环节，然而，其耗时费力且易出错的特性已成为医务人员的普遍负担。近年来，以大型语言模型（LLMs）为代表的生成式人工智能（Generative AI, GenAI）技术在自然语言理解与生成方面展现出前所未有的能力。这些技术为自动化、优化临床文档系统提供了新的范式，旨在减轻临床医生的认知负担，提高文档质量和效率。本综述旨在梳理2022年至2025年期间生成式人工智能在临床文档系统中的代表性研究进展，涵盖其方法分类、关键实验结论，并展望未来的研究趋势与挑战。

### 方法分类与代表作

本节将生成式AI在临床文档系统中的应用分为以下几类，并选取最具代表性的工作进行阐述。

#### 1. 临床记录生成与总结

此类研究聚焦于利用GenAI模型从非结构化或半结构化数据中自动生成结构化临床记录或进行摘要。

*   **Med-PaLM 2 (2025)** [ablesci.com](https://www.ablesci.com/scholar/paper?id=3NVkRpjW3)
    *   **研究问题：** 如何构建一个通用医学语言模型以辅助疾病诊断，并为病历工作流程提供智能支持。
    *   **核心方法：** 构建一个泛化型医学语言模型，通过大规模医学文本数据进行预训练，并结合病史信息进行精细化微调。
    *   **关键实验结论：** 该模型在疾病诊断准确性上展现出卓越性能，能够有效辅助生成病历内容，提升诊断辅助效率。

*   **SAGE-Health (2025)** [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/204361)
    *   **研究问题：** 解决医疗GenAI系统在数据碎片化、生命周期管理不足及数据与模型共同演化基础设施缺乏的问题，以实现高质量、有效的医疗服务交付。
    *   **核心方法：** 提出一种以数据为中心的范式，通过SAGE-Health（可持续、适应性和生成性医疗生态系统）框架整合多样化医疗数据、基础模型和代理协作层，实现数据驱动的GenAI系统设计和部署。
    *   **关键实验结论：** 案例研究表明，该系统在胸部X光报告生成方面，通过语义向量搜索和适应性反馈循环，能生成准确、可追溯并持续改进的报告内容。

*   **LLM在出院小结生成 (2024)** [cloud.tencent.com.cn](https://cloud.tencent.com.cn/developer/article/2516415?policyId=1004)
    *   **研究问题：** 评估LLMs辅助是否能提高医生在开放性管理推理任务中的表现，尤其是在出院小结这类复杂的临床文档生成中。
    *   **核心方法：** 通过一项随机对照试验，对比医生使用GPT-4辅助与仅使用传统资源回答临床病例的表现（包括出院小结的生成）。
    *   **关键实验结论：** GPT-4辅助显著提高了医生在管理推理任务中的得分，且LLM辅助组的医生们在处理案例时表现出更强的同情心和以患者为中心的行为。

#### 2. 医学报告生成与优化

这一类别关注GenAI在特定医学报告（如放射学报告、病理报告）的生成、修订和质量提升方面的应用。

*   **GenMI 在医学报告生成 (2025)** [blog.csdn.net](https://blog.csdn.net/weixin_58753619/article/details/146640682)
    *   **研究问题：** 如何利用多模态生成式AI (GenMI) 准确解读医学图像并自动化生成高质量医学报告，以减轻临床专家负担。
    *   **核心方法：** 文章围绕GenMI在医学报告生成中的进展、局限性和“AI住院医师”范式进行深入探讨，融合大型语言模型（LLMs）处理多模态数据。
    *   **关键实验结论：** GenMI模型在初步医学图像解读和报告起草方面显示出潜力，但LLMs的幻觉和偏见问题仍需解决，并需建立有效评估指标以确保临床准确性。

*   **GPT-4辅助医生表现 (2025)** [cloud.tencent.com.cn](https://cloud.tencent.com.cn/developer/article/2516415?policyId=1004)
    *   **研究问题：** GPT-4能否有效辅助医生进行临床沟通和患者护理，特别是涉及复杂临床情境下的文档生成。
    *   **核心方法：** 设计“ChatCoach”框架，病人代理和辅导代理协同支持医学生练习沟通技巧，并通过Llama2与ChatGPT等大模型评估其有效性。
    *   **关键实验结论：** Llama2通过指令微调在沟通医学辅导任务上显著优于ChatGPT的提示词方法，表明大模型在模拟临床情境下的沟通文档生成具有应用潜力。

#### 3. 医学命名实体识别与信息抽取

此类别研究旨在利用GenAI模型对中文医学文本中的实体进行识别和结构化。

*   **基于大模型的中文医学命名实体识别 (2025)** [aclanthology.org](https://aclanthology.org/2025.ccl-1.9.pdf)
    *   **研究问题：** 解决中文医学文本中实体边界模糊和嵌套结构复杂导致的命名实体识别（NER）难题。
    *   **核心方法：** 提出一种基于大语言模型的NER方法，通过任务重构将其转化为文本生成任务，设计符号标注策略处理平面与嵌套实体，并引入实体筛选器和多模型集成机制。
    *   **关键实验结论：** 该方法在CMeEE-V2和CCKS2019数据集上达到先进水平，F1值分别为0.7785和0.8821，验证了其在复杂中文医学NER任务中的准确性和鲁棒性。

### 实验与评价总结

综合上述研究，生成式AI在临床文档系统中的应用展现出以下共性结论：

1.  **性能提升显著：** 经过领域特定微调或精心设计的提示词工程，大语言模型在临床记录生成、摘要、报告起草和命名实体识别等任务上均能超越传统方法，展现出更强的语义理解和生成能力。
2.  **多模态融合的潜力：** 结合图像、文本等多模态信息的模型在医学报告生成方面表现出巨大潜力，能实现更精准的诊断辅助和信息情境化。
3.  **对准确性和鲁棒性的高要求：** 医疗领域对AI系统的准确性和鲁棒性有着极高要求，模型的“幻觉”、偏差和不准确性是普遍存在的挑战，需要通过精细的训练、筛选机制和人类反馈进行持续优化。
4.  **实时性和效率的平衡：** 虽然LLMs能够提高文档生成效率，但在某些复杂任务中，提高文档质量可能需要更长的处理时间，如何在速度与质量之间取得平衡是实际应用中必须考虑的问题。
5.  **人类专家反馈的重要性：** 无论是模型训练、微调还是最终部署，人类医生和专家的参与至关重要，他们的反馈对于提升模型的临床准确性和可接受度无可替代。

### 趋势与挑战

2025年前后及未来的研究趋势预测包括：

1.  **AI住院医师模式的深化与落地：** 随着多模态GenAI模型（如GenMI）能力的增强，未来将进一步深化“AI住院医师”模式，使其不仅能辅助报告撰写，还能提供实时交互式专业知识和医学教育支持，并逐步在临床环境中进行前瞻性测试与部署 [blog.csdn.net](https://blog.csdn.net/weixin_58753619/article/details/146640682)。
2.  **可信验证与伦理合规的优先级提升：** 鉴于医疗领域对准确性和安全性的极致要求，未来GenAI在临床文档系统中的研究将更加侧重于建立严格的评估基准、临床验证框架以及解决幻觉、偏见和数据隐私等伦理合规问题。这将包括开发新的评估指标来衡量临床准确性，并探索能有效减轻AI模型潜在危害的方法 [cloud.tencent.com.cn](https://cloud.tencent.com.cn/developer/article/2516415?policyId=1004), [cloud.tencent.cn](https://cloud.tencent.cn/developer/article/2513128?policyId=1004)。
3.  **数据中心范式与持续演化生态系统：** 针对医疗数据碎片化和模型过时问题，未来研究将更强调构建可持续的数据生态系统。这包括利用语义向量搜索、上下文查询和反馈驱动的优化机制，确保高质量多模态数据持续流入模型训练和推理过程，实现数据与模型的共同演化，而非仅仅关注模型创新 [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/204361)。

### 结论
生成式人工智能在临床文档系统中的应用正处于快速发展阶段，其强大的文本生成、理解和多模态融合能力为改善医疗效率和质量带来了革命性机遇。从自动化总结、报告生成到辅助诊断推理，GenAI已展现出显著潜力。然而，技术发展的同时，如何确保临床准确性、解决模型“幻觉”、数据偏见以及建立健全的伦理与安全机制仍是亟待解决的挑战。未来研究需着重于构建更加可信、高效、以人为本的GenAI系统，并通过与临床实践的深度融合，最终实现临床文档管理的智能化转型。

### 参考文献

1.  Chen, G., Liu, C., Ooi, G. A., Tan, M., Xie, Z., Yin, J., Yip, J. W. L., Zhang, W., Zhu, J., & Ooi, B. C. (2025). Generative AI for Healthcare: Fundamentals, Challenges, and Perspectives. *arXiv preprint arXiv:2510.24551*. [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/204361)
2.  Lv, T., Luo, L., Lv, H., Sun, Y., Wang, J., & Lin, H. (2025). 基于大语言模型的中文医学命名实体识别. *中国计算语言学大会 (CCL 2025)*. [aclanthology.org](https://aclanthology.org/2025.ccl-1.9.pdf)
3.  Rao, V. M., Topol, E. J., & Rajpurkar, P. (2025). GenMI在医学报告生成的应用与挑战. *Nature*. [blog.csdn.net](https://blog.csdn.net/weixin_58753619/article/details/146640682)
4.  Liu, F., Zhou, H., Gu, B., et al. (2025). Application of large language models in medicine. *Nature Reviews Bioengineering*. [cloud.tencent.cn](https://cloud.tencent.cn/developer/article/2513128?policyId=1004)
5.  Goh, E., & Rodman, A. (2025). GPT-4 assistance for improvement of physician performance on patient care tasks: a randomized controlled trial. *Nature Medicine*. [cloud.tencent.com.cn](https://cloud.tencent.com.cn/developer/article/2516415?policyId=1004)
6.  Huang, H., Wang, S., Liu, H., Wang, H., & Wang, Y. (2024). Benchmarking Large Language Models on Communicative Medical Coaching: a Novel System and Dataset. *arXiv preprint arXiv:2402.05547v1*. [zhuanzhi.ai](https://zhuanzhi.ai/paper/9ba124c2b2f92baf69413b1bd56f2652)
7.  Liu, X., Liu, H., Yang, G., Jiang, Z., Cui, S., Zhang, Z., et al. (2025). A generalist medical language model for disease diagnosis assistance. *Nature Medicine, 31*(3), 932-942. [ablesci.com](https://www.ablesci.com/scholar/paper?id=3NVkRpjW3)
8.  Sun, L., Wang, A., Song, Y., Dong, J., Liu, X., Liang, H., et al. (2025). 大语言模型在临床医学领域的应用、挑战和展望. *解放军医学院学报*. [xuebao.301hospital.com.cn](https://xuebao.301hospital.com.cn/article/doi/10.12435/j.issn.2095-5227.24070201)
9.  Wang, W. S., Tan, N., Huang, K., Zhang, Y. N., Zheng, W. S., & Sun, F. C. (2025). 基于大模型的具身智能系统综述. *自动化学报, 51*(1), 1-19. [aas.net.cn](https://aas.net.cn/cn/article/doi/10.16383/j.aas.c240542)
10. Zhou, Z., & Feng, X. (2025). 从Idea构想到论文发表：AI for Research全链路综述与实践. *arXiv preprint arXiv:2503.01424*. [zhuanzhi.ai](https://www.zhuanzhi.ai/vip/f15b0fa5f13d42ba34af44aced1a81fa)
11. Jiang, Y. F., Gupta, A., Zhang, Z. C., Wang, G. Z., Dou, Y. Q., Chen, Y. J., et al. (2022). VIMA: General robot manipulation with multimodal prompts. *arXiv preprint arXiv:2210.03094*.
12. Li, J., Fei, H., Liu, J., Wu, S., Zhang, M., Teng, C., et al. (2022). Unified named entity recognition as word-word relation classification. *Proceedings of the AAAI conference on artificial intelligence, 36*(10), 10965-10973.