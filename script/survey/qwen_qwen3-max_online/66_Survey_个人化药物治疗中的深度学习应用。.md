# 个人化药物治疗中的深度学习应用（2022–2025）：综述

## 引言

个人化药物治疗旨在依据个体遗传、表型及环境特征定制用药方案，以提升疗效并降低不良反应。传统药理模型受限于高维异质数据的整合能力，而深度学习凭借其强大的表征学习与多模态融合能力，近年在药物响应预测、协同用药设计及电子药物构建等核心任务中取得突破。本文系统梳理2022至2025年间该领域的代表性工作，按方法范式分类评述，并总结共性挑战与未来趋势。

## 方法分类与代表作

### 1. 基于图神经网络的药物-靶标相互作用预测

药物-靶标相互作用（DTI）预测是个性化用药的基石。DTIAM \[Nat Commun, 2025\] 提出统一框架，通过自监督预训练学习药物与靶标子结构表征，联合预测DTI、结合亲和力及作用机制（MoA），在多个基准上显著优于现有方法，为候选药物MoA解析提供新工具。另一工作提出基于多层注意力和消息传递网络的方法 \[自动化学报, 2023\]，通过分子质心位置编码与原子级注意力机制构建药物图特征，在ZhangDDI和ChCh-Miner数据集上AUROC达99.14%与98.45%，有效捕获原子对DDI的差异化贡献。

### 2. 多模态融合驱动的药物协同作用预测

癌症联合治疗可延缓耐药，但组合空间庞大。SynergyX \[BIB, 2024\] 构建多模态互注网络，整合药物ESPF指纹与细胞系4079个基因的6组学特征，通过DCMA、DDMA等互注意模块动态建模药物-细胞、药物-药物交互，在盲测与跨数据集验证中性能领先，并提供药物子结构与基因的可解释性分析。DTSyn \[Brief Bioinform, 2022\] 则采用双Transformer架构，分别处理药物与细胞输入，通过交叉注意力融合信息，显著提升协同分数预测的准确性。

### 3. 检索增强生成（RAG）与知识图谱整合

大语言模型（LLM）易产生“幻觉”，RAG通过外接知识库缓解此问题。一项研究 \[药物流行病学杂志, 2025\] 将RAG应用于新药研发与药物警戒，通过实时检索医学文献与药品数据库，为药物重定位提供可溯源、高时效的证据支持。另一工作HyKGE \[自动化学报, 2025\] 在医疗问答中结合医学知识图谱（KG）与RAG，通过KG路径检索增强LLM对疾病-药物关系的理解，提升了回答的专业性与准确性。此外，KAG框架 \[arXiv:2409.13731\] 将KG与向量检索结合，通过逻辑引导推理，在多跳问答任务中F1分数提升33.5%。

### 4. 基于数字孪生与虚拟临床试验的电子药物

AI4S范式通过构建患者数字孪生模型实现精准用药。一项综述 \[中国胸心血管外科临床杂志, 2025\] 详述了“电子药物”概念：基于患者基因组（含胚系与肿瘤）与多组学数据构建药物数字孪生，并在云端进行大规模虚拟临床试验。其案例显示，结合胚系基因组可将PD-1/PD-L1抑制剂疗效预测准确率从7/9提升至9/9，并揭示了泛癌种原发耐药的信号通路规律。

## 实验与评价总结

共性实验结论可归纳为三点：（1）**多模态数据融合是性能提升的关键**，特别是将基因组、转录组等分子特征与临床表型或药物化学结构结合，能显著优于单模态模型；（2）**可解释性与预测性能同等重要**，通过注意力权重、互注机制或知识图谱路径，模型能揭示潜在的生物标志物或耐药机制，为临床决策提供洞见；（3）**评估标准趋向复杂化**，除传统指标（如AUROC、AUPRC）外，研究更重视在盲测（新药物/新细胞系）和跨数据集场景下的泛化能力，以及虚拟与真实临床试验结果的一致性。

## 趋势与挑战

基于近期研究动态，可预测2025年后的三个核心趋势：（1）**从静态模型向动态持续学习演进**，面对不断更新的医学知识与患者数据，模型需具备在线学习与“灾难性遗忘”规避能力 \[自动化学报, 2025\]；（2）**多模态与多智能体协同成为新范式**，如将RAG、LLM与图神经网络结合，或构建多智能体系统（如MALADE框架 \[arXiv:2408.01869\]）以完成复杂的药物警戒任务；（3）**因果推断深度融入**，超越相关性发现，通过因果模型（如TWIRLS方法 \[中国胸心血管外科临床杂志, 2025\]）解析药物作用的因果机制，为根治性疗法提供理论支撑。主要挑战仍在于高质量标注数据的稀缺、模型可解释性的临床可接受度，以及跨机构数据共享的隐私与合规壁垒。

## 结论

2022–2025年间，深度学习在个人化药物治疗领域从单一任务预测走向多模态、可解释、动态化的系统构建。以图神经网络、多模态融合、RAG及数字孪生为代表的技术，正推动药物研发与临床实践范式的变革。未来研究需在持续学习、多智能体协作与因果推理等方向深化，以真正实现安全、有效、可信赖的精准用药。

## 参考文献

1.  谭洪, 林圣庚, 熊毅. 人工智能赋能癌症协同药物组合预测的现状与挑战. 中国癌症杂志, 2024, 34(9): 807-813.
2.  饶晓洁, 张通, 孟献兵, 陈俊龙. 基于多层注意力和消息传递网络的药物相互作用预测方法. 自动化学报, 2023, 49(12): 2507-2519.
3.  金哲, 邹健, 李逍, 等. 检索增强生成技术在医学人工智能中的应用与前沿探索. 药物流行病学杂志, 2025, 34(8): 962-971.
4.  牛钢, 张春莉. 人工智能驱动的科学研究（AI4S）在药物研发与临床实践中的应用进展. 中国胸心血管外科临床杂志, 2025, 32(5): 523-530.
5.  Hu J, Gao J, Fang X M, et al. DTSyn: a dual-transformer-based neural network to predict synergistic drug combinations. Briefings in Bioinformatics, 2022, 23(5): bbac302.
6.  Li D, Jiang N, Huang K, et al. From questions to clinical recommendations: large language models driving evidence-based clinical decision making. arXiv:2505.10282.
7.  Liang L, Sun M, Gui Z, et al. KAG: boosting LLMs in professional domains via knowledge augmented generation. arXiv:2409.13731.
8.  Choi J, Palumbo N, Chalasani P, et al. MALADE: orchestration of LLM-powered agents with retrieval augmented generation for pharmacovigilance. arXiv:2408.01869.
9.  Tian Y L, Wang Y T, Wang X X, et al. From retrieval-augmented generation to SAGE: The state of the art and prospects. Acta Automatica Sinica, 2025, 51(6): 1145-1169.
10. Wang Q Z A, Wang R Z, Wu Y C, et al. The evolution of continual learning methodologies in the era of large models. Acta Automatica Sinica, 2025, 51(8): 1-27.
11. DTIAM: A unified framework for predicting drug-target interactions, binding affinity, and mechanism of action. Nature Communications, 2025.
12. SynergyX: A multimodal mutual attention network for interpretable drug synergy prediction. Briefings in Bioinformatics, 2024.