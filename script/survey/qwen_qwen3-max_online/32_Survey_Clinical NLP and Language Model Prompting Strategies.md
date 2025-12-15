# 临床自然语言处理与大语言模型提示策略综述（2022–2025）

## 引言

临床自然语言处理（Clinical NLP）旨在从电子病历、医学文献、医患对话等非结构化文本中提取、理解并生成医学知识，是医疗人工智能的关键基础。2022年以后，随着大语言模型（Large Language Models, LLMs）的兴起，研究重心从专用小模型转向通用大模型的适配与引导。提示工程（Prompting）成为核心策略，因其不修改模型参数即可激发领域能力，契合医学对模型稳定性与合规性的严苛要求。本文系统综述2022–2025年间临床NLP与LLM提示策略的代表性工作，聚焦于方法创新、实证评估与未来方向。

## 方法分类与代表作

### 1. 检索增强生成（Retrieval-Augmented Generation, RAG）

RAG通过在生成前检索外部知识库（如文献、指南、知识图谱），缓解LLM的“幻觉”与知识过时问题，在医学高风险场景中成为主流范式。

- **金哲等（2025）**[ywlxbx.whuznhmedj.com](https://ywlxbx.whuznhmedj.com/journal/481.html) 系统综述了RAG在医学AI中的应用，强调其在新药研发、药物警戒和罕见病诊疗中通过引入可验证证据，显著提升了回答的准确性与时效性，并指出未来将与多模态、强化学习融合。
- **Choi等（2024）**[ablesci.com](https://www.ablesci.com/scholar/paper?id=3NVkRpjW3) 提出的 **MALADE** 框架，利用多智能体协作与RAG进行药物警戒。该系统能整合来自警示通报、文献及社交媒体的多源数据，生成可溯源的风险评估报告，在药品安全监测中展现出高精度与透明度。
- **吴天星等（2025）**[crad.ict.ac.cn](https://crad.ict.ac.cn/article/doi/10.7544/issn1000-1239.202440570?viewType=HTML) 构建了面向慢病管理的 **蜻蜓大模型** 系统，结合RAG与工具增强。其采用基于不确定性知识图谱的RAG技术，显著提升了模型在个性化健康建议（尤其针对中国饮食文化）和数字信息处理上的精确性与可信度。

### 2. 领域指令微调（Domain-specific Instruction Tuning）

指令微调通过在通用LLM上使用“指令-输出”对进行微调，使其与人类意图对齐，并掌握特定领域的任务执行能力。

- **SCIR-HI团队（2023）**[github.com](https://github.com/scir-hi/huatuo-llama-med-chinese) 开源了 **本草（BenTsao）** 系列模型，利用中文医学知识图谱（cMeKG）和医学文献，通过ChatGPT API构建指令数据集，对LLaMA、Bloom等基座模型进行LoRA微调。实验证明，该方法能有效提升模型在中文医疗问答中的专业性和事实准确性。
- **Liu等（2025）** 在 **《Nature Medicine》** 发表的通用医学语言模型研究[ablesci.com](https://www.ablesci.com/scholar/paper?id=3NVkRpjW3)中，通过大规模、多来源的临床数据（包括病历、医学教科书、研究论文）进行指令微调，使其在疾病诊断辅助任务上展现出接近专家的综合能力，验证了通用医学模型的可行性。
- **张琳等（2025）**[yydbzz.com](https://www.yydbzz.com/CN/10.3870/j.issn.1004-0781.2025.04.009) 提出了一种基于LLM的患者病历药物警戒画像技术。该方法通过微调模型从非结构化病历中精准提取患者用药事件和不良反应，实现了个体化药物风险的自动化评估，为精准药物警戒提供了新工具。

### 3. 判别增强与多模态融合（Discriminative Enhancement & Multimodal Fusion）

为提升生成内容与临床事实的一致性，研究者将判别式任务（如疾病分类）作为辅助目标，并融合影像等非文本模态信息。

- **钱乾等（2025）**[arocmag.cn](https://www.arocmag.cn/abs/2024.08.0303) 提出 **MedVLM**，一种判别增强的微调方法。该方法在多模态大语言模型基础上，以肺部CT影像的疾病诊断准确性作为判别目标，联合优化报告生成模块。实验表明，此方法生成的报告不仅语言流畅，其核心诊断（如肺炎）的准确率高达87.67%，显著优于传统图像描述模型。
- **《Nature Reviews Bioengineering》综述（2025）**[cloud.tencent.cn](https://cloud.tencent.cn/developer/article/2513128?policyId=1004) 指出，多模态大语言模型（如Med-Flamingo、LLaVA-Med）通过联合微调图文数据，已初步具备放射影像理解能力，并预测未来将向整合时序数据（如心电图）方向发展，以应对更复杂的临床场景。

### 4. 合成数据生成与术语标准化（Synthetic Data & Terminology Normalization）

高质量标注数据的稀缺是临床NLP的主要瓶颈。研究者利用LLM生成合成数据，并开发高精度术语标准化算法以统一临床表达。

- **Moonlight（2025）**[themoonlight.io](https://www.themoonlight.io/zh/review/synthetic-patient-physician-dialogue-generation-from-clinical-notes-using-llm) 介绍了 **SynDial** 方法，利用LLM和反馈循环从临床笔记（如MIMIC-IV）自动生成高质量的医患对话。该方法通过ROUGE和事实性指标进行多轮迭代优化，有效解决了真实对话数据稀缺和隐私保护的难题。
- **韩振桥等（2022）**[c-s-a.org.cn](https://www.c-s-a.org.cn/html/2022/10/8757.html) 提出了一种结合RoBERTa-wwm-ext与多策略召回（Jaccard、TF-IDF）的医学术语标准化方法。该方法在基于SNOMED CT标准的中文数据集上达到了87.8%的准确率，为下游NLP任务提供了高质量的结构化输入。

## 实验与评价总结

近三年临床NLP研究的实验评价呈现出三大共性趋势：
1.  **任务导向的基准多样化**：评估不再局限于通用NLP指标（如BLEU, ROUGE），而是深入具体临床任务，如诊断准确率、ICD编码F1值、药物不良反应识别召回率等，以真实反映模型的临床价值。
2.  **对“幻觉”的量化与重视**：几乎所有高质量研究都将幻觉率（Hallucination Rate）作为核心评估指标，常通过计算生成内容与源文档或标准知识库的事实一致性（Factuality）来衡量。
3.  **人机协同评估的兴起**：越来越多的研究引入临床医生进行人工评估，从临床合理性、安全性、有用性等维度对模型输出进行打分，弥补自动指标的不足。

## 趋势与挑战

基于现有文献，2025年前后的临床NLP研究将聚焦于以下方向：
1.  **可信与可解释性增强**：未来模型不仅需生成正确答案，还需提供可验证的推理路径和证据来源。结合RAG、因果推理与不确定性量化，构建“白盒化”临床决策支持系统是核心挑战。
2.  **多模态与长时序数据融合**：电子病历是典型的多模态（文本、影像、时序信号）数据。如何高效融合这些异构信息，特别是处理长时序生理信号，将是提升模型对复杂疾病（如慢病）理解能力的关键。
3.  **面向专科与个性化场景的深化**：当前研究多集中于通用医学。未来将涌现出更多针对精神健康、康复医学、肿瘤学等专科领域的精细化模型，并能根据患者个体特征（基因、生活方式）提供高度个性化的建议。

## 结论

2022–2025年是临床NLP从专用模型迈向大模型时代的关键转型期。以RAG和指令微调为代表的提示与适配策略，有效释放了通用大语言模型在医疗领域的潜力。然而，模型的可靠性、数据的多模态性以及临床场景的复杂性，共同构成了下一阶段的核心挑战。未来的研究必须坚持临床需求驱动，通过跨学科合作，在可信、安全、高效的前提下推动技术真正落地。

## 参考文献

1.  金哲, 邹健, 李逍, 等. 检索增强生成技术在医学人工智能中的应用与前沿探索[J]. 药物流行病学杂志, 2025, 34(8): 962-971.
2.  Choi J, Palumbo N, Chalasani P, et al. MALADE: orchestration of LLM-powered agents with retrieval augmented generation for pharmacovigilance[J]. arXiv preprint arXiv:2408.01869, 2024.
3.  吴天星, 曹旭东, 毕胜, 等. 基于大语言模型的重大慢病健康管理信息系统构建[J]. 计算机研究与发展, 2025.
4.  SCIR-HI. BenTsao (HuaTuo): Instruction-tuning Large Language Models With Chinese Medical Knowledge[EB/OL]. GitHub, 2023. [https://github.com/scir-hi/huatuo-llama-med-chinese](https://github.com/scir-hi/huatuo-llama-med-chinese)
5.  Liu X, Liu H, Yang G, et al. A generalist medical language model for disease diagnosis assistance[J]. Nature Medicine, 2025, 31(3): 932-942.
6.  张琳, 吴正善, 张纾, 等. 基于大语言模型的患者病历药物警戒画像技术研究[J]. 医药导报, 2025, 44(4): 554-560.
7.  钱乾, 孙丽萍, 刘佳霖, 等. 基于判别增强大语言模型微调的医学影像报告生成[J]. 计算机应用研究, 2025, 42(3): 762-769.
8.  Liu F, Zhou H, Gu B, et al. Application of large language models in medicine[J]. Nature Reviews Bioengineering, 2025.
9.  Synthetic Patient-Physician Dialogue Generation from Clinical Notes Using LLM[EB/OL]. Moonlight AI Review, 2025. [https://www.themoonlight.io/zh/review/synthetic-patient-physician-dialogue-generation-from-clinical-notes-using-llm](https://www.themoonlight.io/zh/review/synthetic-patient-physician-dialogue-generation-from-clinical-notes-using-llm)
10. 韩振桥, 付立军, 刘俊明, 等. 结合RoBERTa与多策略召回的医学术语标准化[J]. 计算机系统应用, 2022, 31(10): 245-253.
11. 张政波, 孙磊, 汪安安, 等. 大语言模型在临床医学领域的应用、挑战和展望[J]. 解放军医学杂志, 2025.
12. Du Y, Zhao S, Cai M, et al. The CALLA Dataset: Probing LLMs’ Interactive Knowledge Acquisition from Chinese Medical Literature[J]. arXiv preprint arXiv:2309.04198, 2023.