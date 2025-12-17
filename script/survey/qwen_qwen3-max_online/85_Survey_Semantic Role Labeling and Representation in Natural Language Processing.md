# 语义角色标注与表示在自然语言处理中的研究综述（2022–2025）

## 引言

语义角色标注（Semantic Role Labeling, SRL）旨在识别谓词的语义角色（即“谁对谁做了什么”），是深层语义理解的核心任务。传统SRL以PropBank和FrameNet为标注框架，近年来研究重点已从单一角色分类转向多粒度语义表示、跨语言迁移与大模型适应。2022–2025年间，该领域呈现三大技术路线：（1）基于微调的神经架构优化；（2）基于提示工程的生成式SRL；（3）面向具身智能的多模态语义角色建模。本文系统梳理上述方向的代表性工作，并分析评价范式与未来趋势。

## 方法分类与代表作

### 基于微调的神经SRL模型

曹学飞等人（2023）针对汉语框架语义角色识别中模型性能对超参数敏感的问题，提出基于BiLSTM的聚合模型[1]。该方法引入正则化交叉验证（RCV）约束训练/验证集的框架分布差异，通过众数投票选择无显著差异的超参数配置集合并聚合子模型。在CFN大语料上，其F1值达74.87%，较基线提升9.56个百分点，显著优于单一模型。

于媛芳等人（2023）在事件论元抽取任务中指出角色信息利用不足和论元交互缺失是性能瓶颈，提出角色信息引导的多轮抽取模型[2]。该模型独立编码角色定义与文本，通过注意力融合生成知识增强嵌入，并设计“先易后难”的多轮抽取算法动态更新历史嵌入。在ACE2005数据集上F1达55.6%，验证了角色知识引导与交互建模的有效性。

CRENER（Qiao & Peng, 2024）针对中文NER（可视为细粒度SRL）中词边界模糊问题，将任务转化为字符-字符关系分类[7]。模型定义四类字符关系标签，构建方向/距离感知的掩码自注意力编码器，并设计关系表示增强模块。在四个中文NER基准上均超越SOTA，尤其实体边界F1提升显著，证明了字符级关系建模对中文语义角色识别的有效性。

### 基于提示工程的生成式SRL

李迎旭等人（2025）针对大语言模型（LLM）在汉语框架语义解析中的推理路径简单问题，提出检索增强思维链（RAG-CoT）提示方法[3]。该方法融合模块化提示、BM25/BGE双路检索与候选框架约束，将框架识别转化为受限分类问题。在CFN2.1上，框架识别准确率提升13.52%，论元与角色F1分别提升2.24%和5.09%，验证了RAG与CoT协同对LLM语义解析的增强作用。

王梦影等人（2025）针对电力领域实体边界模糊问题，提出融合机器阅读理解（MRC）与扩散模型的MDNER[6]。该方法将NER重定义为实体边界的去噪扩散过程，正向扩散添加高斯噪声，逆向扩散通过MRC式问答逐步细化边界。在电网数据集上，其边界预测F1显著优于CRF和指针网络基线，为复杂领域SRL提供了新范式。

### 多模态与具身语义角色表示

Wang等人（2023）在具身智能综述中系统分析了大模型在机器人控制中的语义角色建模[8]。PaLM-E[17]等模型将视觉-语言-动作对齐，通过“可承担性”（affordance）表示物体在动作中的语义角色（如“可抓握”）。实验表明，此类具身SRL在RT-X[55]等多机器人数据集上可泛化至未见物体与任务，但依赖大规模具身数据。

Negation Triplet Extraction (NTE) 任务（Shi et al., 2024）扩展了传统SRL至否定结构，要求同时抽取否定主语、否定词与作用范围三元组[4]。其SSENE模型将句法依存树融入PLM编码器，并设计语义一致性辅助任务。在NegComment数据集上，F1达82.3%，证明句法结构对远距离语义角色（如主语-否定词）关联建模的关键作用。

## 实验与评价总结

近三年SRL研究在评价上呈现三大共性：（1）**任务解耦**：将SRL拆分为框架/谓词识别→论元边界→角色分类多阶段（如[3]），通过流水线设计降低复杂度，但存在错误传播风险；（2）**表示对齐**：强调语义角色与上下文/外部知识的对齐，如CAMR的Align-smatch指标[9]要求概念-词对齐，SSENE[4]的语义一致性损失；（3）**领域适配**：在医疗[1]、电力[6]、古汉语[9]等垂直领域构建专用语料与标签体系，通用模型（如BERT）微调仍是主流，但LLM提示工程[3,6]在低资源场景显优势。值得注意的是，所有生成式方法[3,6]均报告了LLM的幻觉问题，需通过候选集约束[3]或扩散过程[6]抑制。

## 趋势与挑战

基于2025年前沿工作，SRL研究呈现以下趋势：  
1. **具身化与物理约束融合**：语义角色将不仅关联文本，还需满足物理可实现性（如“可抓握性”）。PaLM-E[17]与VoxPoser[52]等模型通过3D价值图将角色映射至可执行动作，但仿真-现实鸿沟仍是挑战。  
2. **动态角色演化建模**：传统SRL假设角色静态，而真实对话/事件中角色可变（如“攻击者”转为“防御者”）。多轮抽取[2]和扩散细化[6]初步探索此方向，但缺乏统一框架。  
3. **跨框架统一表示**：现有工作多基于单一标注体系（PropBank/FrameNet），而CAMRP[9]等尝试融合多框架。未来需构建跨语言、跨标注体系的语义角色本体，支持零样本迁移。  
4. **效率-精度权衡**：RAG[3]与聚合模型[1]显著提升性能但计算开销大。2025年研究将聚焦高效检索（如bge-m3[3]）与模型压缩（如Distill-Qwen[3]），以适配端侧应用。

## 结论

2022–2025年，SRL从封闭域分类任务演进为开放域、多模态的语义表示问题。微调模型通过架构创新（如聚合[1]、多轮交互[2]）持续突破性能上限，而LLM提示工程（RAG-CoT[3]、扩散-MRC[6]）为低资源场景提供新路径。未来，具身约束、动态演化与跨框架统一将成为核心挑战，需在表示能力、物理一致性与计算效率间取得平衡。

## 参考文献

[1] 曹学飞, 李济洪, 王瑞波, 牛倩. 基于BiLSTM聚合模型的汉语框架语义角色识别. 中国计算语言学大会 (CCL), 2023. [aclanthology.org/2023.ccl-1.38.pdf](https://aclanthology.org/2023.ccl-1.38.pdf)  
[2] 于媛芳, 张勇, 左皓阳, 等. 基于角色信息引导的多轮事件论元抽取. 北京大学学报(自然科学版), 2023, 59(1): 83–92. [xbna.pku.edu.cn/fileup/0479-8023/HTML/2023-1-83.html](https://xbna.pku.edu.cn/fileup/0479-8023/HTML/2023-1-83.html)  
[3] 李迎旭, 陈涛, 黎议泽, 李斌阳. 基于检索增强思维提示的汉语框架语义解析方法. 中国计算语言学大会 (CCL), 2025. [aclanthology.org/anthology-files/pdf/ccl/2025.ccl-1.15.pdf](https://aclanthology.org/anthology-files/pdf/ccl/2025.ccl-1.15.pdf)  
[4] Shi Y, Yang D, Liu J, et al. Negation Triplet Extraction with Syntactic Dependency and Semantic Consistency. arXiv:2404.09830, 2024. [arxiv.org/abs/2404.09830](https://arxiv.org/abs/2404.09830)  
[5] Hua Y, Xie Q, Jain V, et al. Toward General-Purpose Robots via Foundation Models: A Survey and Meta-Analysis. arXiv:2312.08782, 2023.  
[6] 王梦影, 闫丹凤. 融合阅读理解与扩散模型的实体识别研究. 中国科技论文在线, 2025. [paper.edu.cn/releasepaper/content/202502-43](https://www.paper.edu.cn/releasepaper/content/202502-43)  
[7] Qiao Y, Peng S. CRENER: A Character Relation Enhanced Chinese NER Model. arXiv:2412.10858, 2024. [arxiv.org/abs/2412.10858](https://arxiv.org/abs/2412.10858)  
[8] 王文晟, 谭宁, 黄凯, 等. 基于大模型的具身智能系统综述. 自动化学报, 2025, 51(1): 1–19. [aas.net.cn/cn/article/doi/10.16383/j.aas.c240542](https://aas.net.cn/cn/article/doi/10.16383/j.aas.c240542)  
[9] GoThereGit. Chinese AMR Corpus. GitHub, 2022. [github.com/GoThereGit/Chinese-AMR](https://github.com/GoThereGit/Chinese-AMR)  
[10] Huang S, Jiang Z, Dong H, et al. Instruct2Act: Mapping Multi-modality Instructions to Robotic Actions with Large Language Model. arXiv:2305.11176, 2023.  
[11] Wei J, Wang X, Schuurmans D, et al. Chain-of-Thought Prompting Elicits Reasoning in Large Language Models. NeurIPS, 2022.  
[12] Lewis P, Perez E, Piktus A, et al. Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks. NeurIPS, 2020.  
[13] Chen H, Zhang M, Li J, et al. Semantic Role Labeling: A Systematic Survey. arXiv:2502.08660, 2025.  
[14] Zhang Y, Zhao H, Wei J, et al. Context-Based Semantic Communication via Dynamic Programming. IEEE TCCN, 2022.  
[15] Wang G, Xie Y, Jiang Y, et al. Voyager: An Open-Ended Embodied Agent with Large Language Models. arXiv:2305.16291, 2023.  
[16] Li J, Li D, Savarese S, Hoi S. BLIP-2: Bootstrapping Language-Image Pre-Training with Frozen Image Encoders and Large Language Models. ICML, 2023.  
[17] Driess D, Xia F, Sajjadi M, et al. PaLM-E: An Embodied Multimodal Language Model. ICML, 2023.