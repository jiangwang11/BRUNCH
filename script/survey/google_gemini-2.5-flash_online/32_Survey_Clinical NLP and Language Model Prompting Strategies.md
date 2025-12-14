好的，以下是关于 Clinical NLP 和 Language Model Prompting Strategies 的中文学术综述，涵盖 2022-2025 年的代表性工作。

## Clinical NLP and Language Model Prompting Strategies 综述

### 引言

临床自然语言处理（Clinical NLP）致力于从医疗文本中提取、理解和利用有价值的信息，以支持临床决策、疾病诊断、医学研究和患者护理。随着大型语言模型（LLMs）的快速发展，其在理解和生成自然语言方面的强大能力为 Clinical NLP 带来了革命性的变革。特别是，提示工程（Prompting Strategies）作为一种无需修改模型参数即可引导LLMs执行特定任务的方法，极大地拓宽了LLMs在医疗领域的应用范围。本综述将聚焦2022-2025年的代表性工作，系统梳理LLMs在Clinical NLP中的应用，特别是各种提示策略的发展及其在医疗任务中的实验表现与挑战，并展望未来的研究方向。

### 方法分类与代表作

本节将LLMs在Clinical NLP中的应用方法分为以下几类，并介绍最具代表性的工作。

#### 1. 基础信息抽取与归一化

基础信息抽取与归一化是 Clinical NLP 的核心任务，旨在识别文本中的实体、关系和事件，并将其映射到标准化术语体系。

*   **[cn-cs-a.org.cn](https://www.c-s-a.org.cn/html/2022/10/8757.html)** (2022) 提出了一种结合 RoBERTa 和多策略召回的方法，用于中文医学术语标准化。该研究旨在解决传统方法在术语映射准确率低、难以对齐的问题，通过 Jaccard 相关系数、TF-IDF 和历史召回进行候选概念召回，并使用 RoBERTa-wwm-ext 作为蕴含语义评分模型进行排序。实验首次在基于 SNOMED CT 标准的中文数据集上验证了该方法的有效性，达到了 87.8%的准确率。
*   **[pdf.hanspub.org](https://pdf.hanspub.org/csa2025151_221543469.pdf)** (2025) 提出了一种基于提示增强的LLM信息抽取算法（LLM-IE Algorithm Based on Prompt Enhancement）。该算法将文本信息抽取任务转化为文本生成任务，并通过结构化解析生成结果。其核心思想是通过动态提示构建和思维链推理，辅以小样本提示学习（few-shot learning），有效提升在标注数据稀缺情况下的实体、关系、事件抽取性能。实验结果表明，该方法在少数样本受限情况下，能够大幅提升特定领域信息抽取效果，其在关系抽取和事件抽取任务上的F1值显著优于通用信息抽取模型（UIE）。
*   **[cnblogs.com](https://www.cnblogs.com/tiome/p/19096775)** (2025) 的综述指出，在LLM时代，命名实体识别（NER）和关系抽取（RE）已通过结合LLM-NERRE（处理层次信息）和InstructGPT（零样本或少样本提示）得到改进。该综述强调，LLMs在复杂条件下可以更方便地进行NER和RE，通过其庞大的参数量在大多数传统任务中表现优于传统PLM。然而，在特定领域知识或简单任务上，经过微调的PLM仍可能具有竞争优势或效率优势。

#### 2. 对话系统与问答

LLMs在医疗对话系统和问答方面展现出巨大潜力，能为患者和医生提供信息支持。

*   **[cnblogs.com](https://www.cnblogs.com/tiome/p/19096775)** (2025) 的综述中提到，LLMs在医疗问答（QA）方面表现卓越，许多最新的医疗模型在MedMCQA、PubMedQA、MMLU等数据集上已接近或超越SOTA方法，如PaLM 2。该综述指出，与能力有限的PLM不同，LLMs能够更好地理解和生成复杂医疗文本的答案。此外，基于LLM的对话系统可以实现PLM难以实现的高级功能，可用于任务导向（如药物咨询）或开放式对话（如情感支持）系统。
*   **[waresci.com](https://www.ablesci.com/scholar/paper?id=3NVkRpjW3)** (2025) 介绍了一个通用的医学语言模型，用于疾病诊断辅助。该模型整合了医学诊断、病历工作流程、人工智能、病史、医学机器学习和医学教育等多个领域。该研究强调了开发能够有效处理复杂医疗信息并协助医生进行诊断的通用型LLM的必要性，并发表于《Nature Medicine》。

#### 3. 报告生成与临床决策支持

LLMs能够辅助生成医疗报告，并整合多模态信息提供临床决策支持。

*   **[cnblogs.com](https://www.cnblogs.com/tiome/p/19096775)** (2025) 的综述强调，医疗报告生成是医疗保健领域一个有前景的研究方向，其重要临床价值在于帮助专家进行临床决策，并通过自动化草拟异常和正常发现的报告以减轻书写负担。该文列举了ChatCAD和ChatCAD+等代表性工作，这些模型在这一任务上明显优于传统的PLM。此外，LLMs通过思维链（COT）的提出，提高了AI生成决策的信任度和可靠性，并能够增强透明度和可解释性。
*   **[cloud.tencent.cn](https://cloud.tencent.cn/developer/article/2513128?policyId=1004)** (2025) 的综述探讨了LLMs在医学中的革命性应用，指出LLMs在医疗决策支持中可以协助诊断、风险预测、治疗推荐和临床试验匹配。模型能够整合患者病史、检查结果和文献证据，为复杂临床决策提供支持。然而，其大规模临床验证仍有待完成。LLMs还在临床编码、报告生成（包括多模态报告如ChatCAD、MAIRA-1）、医学机器人、医学语言翻译、医学教育和精神健康支持等多个临床场景中展现了应用潜力。
*   **[xuebao.301hospital.com.cn](https://xuebao.301hospital.com.cn/article/doi/10.12435/j.issn.2095-5227.24070201)** (2025) 综述了大语言模型在临床医学领域的应用，提出LLMs在加速知识传播、优化临床决策和提升患者体验方面发挥重要作用。该文梳理了LLMs在临床医学领域的典型应用，并分析了其存在的问题和面临的挑战，提供了医疗系统整体智能化升级的强大动力。

#### 4. 检索增强生成 (RAG) 技术

检索增强生成（RAG）技术通过结合外部知识库，解决LLMs的“幻觉”问题和知识时效性问题。

*   **[ywlxbx.whuznhmedj.com](https://ywlxbx.whuznhmedj.com/journal/481.html)** (2025) 深入探讨了检索增强生成（RAG）技术在医学人工智能中的应用与前沿探索。该研究指出RAG通过主动连接外部文献数据库和知识图谱等信息源，显著降低了LLM对过时训练数据的依赖，并在回答中引入可验证的证据。该文总结了RAG在临床决策支持、新药研发与药物警戒（如罕见不良反应监测）、以及罕见事件研究（如舆情追踪、多源信息整合）等医药场景下的具体应用。RAG的核心挑战在于如何在繁杂的外部数据库中高效、精准地检索最相关的文档，以及如何在回答生成时平滑地将检索信息嵌入语言模型的推理过程。
*   **[cnblogs.com](https://www.cnblogs.com/tiome/p/19096775)** (2025) 的综述也强调了检索增强生成（RAG）在提升LLM性能方面的作用，尤其是在“情境学习”（In-context learning, ICL）和“思维链”（COT）的应用中，能更好地定制模型以适应医疗专业人员的需求。RAG作为一种重要的训练方法，与其他诸如预训练（PT）、监督微调（SFT）、LoRA微调以及基于人类反馈的强化学习（RLHF）等方法共同提升医疗LLM的能力。

### 实验与评价总结

2022-2025年的研究表明，LLMs及其提示策略在Clinical NLP任务中展现出显著优势：

1.  **性能提升与泛化能力**：LLMs凭借其庞大的参数量和预训练数据，在多项Clinical NLP任务中展现出优异的性能，尤其在开放性任务和复杂语义理解上，普遍超越了传统PLMs，并在多种医学基准测试中（如USMLE）达到或接近人类专家水平。
2.  **小样本与零样本学习**：提示策略的引入使得LLMs在小样本（few-shot）和零样本（zero-shot）场景下表现出强大的泛化能力，显著降低了对大规模标注数据的依赖，这对于数据稀缺的医疗领域尤为重要。
3.  **可解释性增强**：思维链（CoT）等提示策略的运用，有助于提高LLM生成决策的可靠性和透明度，部分缓解了模型“黑箱”问题，但在深层逻辑溯源方面仍有提升空间。
4.  **多模态融合**：虽然主要聚焦文本，但越来越多的研究开始探索LLMs与图像、基因组等其他模态数据的融合，为更全面的临床诊断和报告生成开辟了道路。
5.  **局限性**：尽管进步显著，但LLMs在医疗领域仍面临“幻觉”生成、知识时效性不足、隐私保护、复杂推理能力欠缺以及行为对齐不足等挑战。特别是在高风险的临床决策场景中，模型输出的准确性和可追溯性仍需更严格的验证。

### 趋势与挑战

2025年前后，Clinical NLP领域与LLMs提示策略的研究趋势将集中于以下几点：

1.  **可信赖AI与“幻觉”消弭**：未来的研究将更加关注如何从根本上解决LLMs的“幻觉”问题，尤其是在医疗这种对准确性要求极高的领域。检索增强生成（RAG）技术会进一步发展，可能融入更精细的知识图谱，甚至结合事实核查（Fact-Checking）模型，形成多阶段、自适应的知识校准机制，以提供具备高度可追溯性和可信赖性的临床信息。
2.  **多模态深度融合与跨模态推理**：当前LLMs主要处理文本信息，但医疗数据天然是多模态的。未来的趋势将是LLMs与医学影像、基因组学数据、生理信号等进行更深层次的融合，实现真正的跨模态理解和推理。例如，开发能同时分析放射报告文本和医学图像，并生成诊断建议的MLLMs，甚至能够整合电子健康记录中的时序数据进行疾病预测和干预方案推荐。
3.  **个性化与自适应临床决策支持系统**：未来的Clinical NLP系统将不仅仅是提供通用信息，而是朝着高度个性化和自适应的方向发展。LLMs将结合患者的个体特征（如基因信息、生活习惯、合并症等），通过持续学习和微调，提供更为精准的诊断、治疗和预后建议。同时，提示策略也将更加灵活，能够根据临床场景和用户需求动态调整，实现人机协同的智能决策助理。

### 结论

LLMs及其提示策略的兴起为Clinical NLP带来了前所未有的机遇，极大地推动了医疗文本信息处理、知识问答、报告生成和临床决策支持等领域的发展。尽管在性能和泛化能力上取得了显著进展，但“幻觉”问题、数据隐私、知识时效性和伦理合规性等挑战依然严峻。未来的研究将继续围绕如何构建更可信、更智能、更能深入理解和利用多模态医疗数据的LLMs展开，并探索更有效、更安全的提示策略，以期最终实现AI在医疗领域的全面赋能。

### 参考文献

1.  [cn-cs-a.org.cn](http://www.c-s-a.org.cn/html/2022/10/8757.html) Han, Z. Q., Fu, L. J., Liu, J. M., Guo, Y. J., Tang, K. K., & Liang, R. (2022). Combining RoBERTa with Multi-strategy Recall for Medical Terminology Normalization. *Computer Systems and Applications*, *31*(10), 245-253.
2.  [xuebao.301hospital.com.cn](https://xuebao.301hospital.com.cn/article/doi/10.12435/j.issn.2095-5227.24070201) Sun, L., Wang, A. A., Song, Y. M., et al. (2025). Applications, challenges, and prospects of large language models in clinical medicine. *Journal of PLA Medical College*, 10.12435/j.issn.2095-5227.24070201.
3.  [ablesci.com](https://www.ablesci.com/scholar/paper?id=3NVkRpjW3) Liu, X., Liu, H., Yang, G., et al. (2025). A generalist medical language model for disease diagnosis assistance. *Nature Medicine*, *31*(3), 932-942.
4.  [yydbzz.com](https://www.yydbzz.com/CN/10.3870/j.issn.1004-0781.2025.04.009) Wu, Z., Zhang, S., Lin, Y., Lei, Y., Wang, Q., Sun, Z., & Zhang, L. (2025). Research on Pharmacovigilance Profiling Technology for Patient Medical Records Based on Large Language Models. *Medical Guide*, *44*(4), 554-560.
5.  [tcmjc.com](https://tcmjc.com/doi/10.13288/j.11-2166/r.2025.09.005) (2025). 基于大语言模型的中医智能预问诊系统的构建与验证 (Construction and Verification of a Smart Pre-consultation System for Traditional Chinese Medicine Based on Large Language Models). *Journal of Traditional Chinese Medicine*, DOI: 10.13288/j.11-2166/r.2025.09.005.
6.  [ywlxbx.whuznhmedj.com](https://ywlxbx.whuznhmedj.com/journal/481.html) Jin, Z., Zou, J., Li, X., Lyu, J., Hu, Z., & Feng, D. (2025). Application and frontier exploration of retrieval-augmented generation technology in medical artificial intelligence. *Journal of Pharmacoepidemiology*, *34*(8), 962-971.
7.  [cloud.tencent.cn](https://cloud.tencent.cn/developer/article/2513128?policyId=1004) Liu, F., Zhou, H., Gu, B., et al. (2025). Application of large language models in medicine. *Nat Rev Bioeng*. DOI: 10.1038/s44222-025-00279-5.
8.  [pdf.hanspub.org](https://pdf.hanspub.org/csa2025151_221543469.pdf) Li, Z., Huang, H., Ren, Q., & Li, P. (2025). Prompt Enhancement Based LLM Information Extraction Algorithm. *Computer Science and Application*, *15*(1), 220-229.
9.  [cnblogs.com](https://www.cnblogs.com/tiome/p/19096775) (2025). [论文笔记/综述] A survey of large language models for healthcare: from data, technology, and applications to accountability and ethics. Blog Post. Retrieved from https://www.cnblogs.com/tiome/p/19096775
10. [blog.csdn.net](https://blog.csdn.net/u013524655/article/details/148038198) Yang, R., Li, H., Wong, M. Y. H., et al. (2025). Generative Large Language Models and Traditional Natural Language Processing in Medicine: An Evolving Landscape. CSDN Blog. Retrieved from https://blog.csdn.net/u013524655/article/details/148038198
11. Lewis, P., Perez, E., Piktus, A., et al. (2020). Retrieval-augmented generation for knowledge-intensive NLP tasks. arXiv preprint arXiv:2005.11401.
12. Ouyang, L., Wu, J., Jiang, X., et al. (2022). Training language models to follow instructions with human feedback. *Advances in Neural Information Processing Systems*, *35*, 27730-27744.