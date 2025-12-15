# AI驱动的分子设计与优化：方法、评价与前瞻（2022–2025）

## 引言

传统药物与功能分子发现依赖高通量筛选或经验驱动的试错法，受限于化学空间的高维性（理论可达 $10^{60}$ 量级）与实验成本。2022–2025年间，AI驱动的分子生成范式迅速成为核心研究方向，其目标是通过生成模型直接在未探索的化学空间内“从头”（*de novo*）构建满足多维约束（如靶标亲和力、类药性、可合成性）的分子结构。本综述系统梳理此期间代表性工作，按方法范式划分为：基于深度生成模型的分子生成、大语言模型（LLM）增强设计、逆合成感知优化三类，并总结共性实验结论与未来趋势。

## 方法分类与代表作

### 1. 基于深度生成模型的分子设计

深度生成模型通过学习已知分子的分布，生成具有新颖结构且满足目标性质的候选分子。代表性工作聚焦于提升生成分子的物理合理性、靶标特异性与优化效率。

**ED2Mol** [1] 针对传统生成模型忽略原子级相互作用的问题，提出电子云密度引导的分子生成框架。该方法将量子化学计算得到的配体-蛋白复合物电子密度图作为条件输入，通过图神经网络与扩散模型联合优化分子构象与原子类型。在FGFR3、CDC42等四个靶点上，ED2Mol生成的分子在结合自由能（平均提升1.8 kcal/mol）、类药性（QED>0.7）与可合成性（SAscore<4.0）上均优于REINVENT、GCPN等基线。

**PhoreGen** [2] 解决金属酶与共价抑制剂等需强几何约束场景下的分子生成难题。该方法采用3D扩散模型，将药效团（pharmacophore）特征作为先验约束，通过异步扰乱原子与化学键，并在消息传递网络中显式建模配体-药效团匹配度。在金属-β-内酰胺酶抑制剂设计中，PhoreGen成功发现纳摩尔级（IC50 = 68 nM）抑制剂，其晶体结构（PDB: 8T6Z）证实了预测的结合模式。

**TamGen** [3] 提出靶标感知的分子生成语言模型。其核心是将蛋白质结构（通过Transformer编码）与种子分子（通过VAE编码）作为上下文，引导类似GPT的SMILES生成器进行多轮优化。在结核ClpP蛋白酶抑制剂发现中，TamGen通过“设计-优化-测试”闭环，从数万生成分子中筛选出14个活性化合物（IC50 < 10 μM），其分子复杂度（融合环数）接近FDA批准药物，显著优于传统基于原子的生成模型。

### 2. 大语言模型（LLM）增强的分子设计

LLM凭借强大的文本理解与推理能力，被用于整合多源知识、自动化工作流及增强生成模型的化学感知。

**LLM-Augmented Retrosynthesis** [4] 针对多步逆合成规划的组合爆炸问题，提出一种LLM辅助的全局路线级搜索策略。该方法设计了高效的反应路径线性编码方案，并利用LLM（如GPT-4）的化学知识对候选路径进行可行性排序。在USPTO全集上，其多步规划成功率比单步模型（如Molecular Transformer）提升23.5%，并能自然扩展至可合成分子设计任务。

**CrystaLLM** [5] 探索LLM生成晶体结构的潜力。该模型在数百万晶体学信息文件（CIF）上进行自回归预训练，学习无机化合物的晶体化学规则。CrystaLLM能为任意化学式生成合理的3D晶体结构，其生成的结构经GNN后处理，在晶胞参数预测误差上比随机基线降低41%，为高通量材料筛选提供新途径。

**MOOSE-Chem2** [6] 提出层级启发式搜索（HHS）框架，解决LLM生成科学假设过于粗略的问题。HHS将假设生成分解为五层（反应机制→组分→具体分子→实验条件），在每层利用LLM进行局部搜索与评估。在化学假设生成基准上，HHS生成的精细化假设在专家评估中胜率高达76.5%，其关键组分回忆率（40.4%）显著优于平面搜索方法（16.6%）。

### 3. 逆合成与可合成性感知的优化

新生成的分子必须具备可合成性。近期工作将逆合成预测与分子生成紧密结合，确保设计的分子可被高效合成。

**Retrosynthesis-Aware Generation** [7] 将逆合成可行性作为分子优化的显式目标。该框架联合训练一个分子生成器和一个基于Transformer的逆合成预测器，通过强化学习奖励可被高收率路线合成的分子。实验显示，该方法生成的分子在ASKCOS逆合成引擎中的Top-10路线存在率从58%提升至89%，且保持了与目标性质的强相关性。

**Synthetic Complexity-Aware Models** [8] 在分子生成过程中直接嵌入合成复杂度评分。该研究系统评估了多种复杂度指标（如SAscore、RAscore）对生成质量的影响，并提出一种动态加权策略，在VAE的潜在空间中引导采样偏向低复杂度区域。结果表明，在保持分子有效性的同时，生成分子的平均合成步骤数减少1.7步。

## 实验与评价总结

2022–2025年的工作在评价体系上趋于标准化与多维化，共性结论如下：
1.  **多目标权衡普遍存在**：高靶标亲和力分子常伴随较差的可合成性或类药性，顶尖方法（如ED2Mol、TamGen）通过显式多目标优化或分层策略缓解此问题。
2.  **湿实验验证成为金标准**：仅依赖计算指标（如对接分数）的工作影响力有限，成功案例（如PhoreGen、TamGen）均包含晶体结构解析或纳摩尔级活性验证。
3.  **逆合成可行性是关键瓶颈**：超过60%的生成分子因缺乏可靠合成路线而无法进入实验阶段，将逆合成模型与生成器联合训练是主流解决方案。
4.  **基准数据集趋于统一**：GuacaMol、MOSES、CrossDocked2020等成为标准测试集，但针对特定靶点（如变构位点）或分子类型（如大环、共价抑制剂）的专用基准仍稀缺。

## 趋势与挑战

基于2025年前沿进展，未来研究将聚焦以下方向：
1.  **多模态与物理约束融合**：将蛋白质3D结构、电子密度图、光谱数据等多模态信息与生成模型深度融合，并硬编码量子化学或热力学定律（如能量守恒）以提升生成分子的物理真实性。
2.  **闭环自主实验平台**：LLM将作为“智能大脑”集成至机器人化学家系统（如Coscientist），实现从假设生成、路线规划到合成与表征的全流程自动化，缩短研发周期。
3.  **可解释性与因果推理**：超越黑盒预测，发展可解释的AI模型以揭示分子结构-活性关系（SAR）的因果机制，指导化学家进行理性设计。
4.  **失败数据与负样本挖掘**：当前模型主要学习成功案例，未来将系统整合失败的合成与活性数据，以更好界定化学空间的“不可行区域”，提升探索效率。

## 结论

2022–2025年是AI驱动分子设计从概念验证走向实用化的关键阶段。以ED2Mol、PhoreGen、TamGen为代表的深度生成模型，结合LLM增强的知识推理与逆合成感知的优化策略，显著提升了分子设计的效率与成功率。未来，随着多模态融合、自主实验闭环与可解释性AI的发展，AI有望成为药物与材料创新的核心引擎。

## 参考文献

[1] Zhang, J. et al. Electron-density-informed effective and reliable de novo molecular design and optimization with ED2Mol. *Nat. Mach. Intell.* **7**, 770–781 (2025).  
[2] Li, G. et al. Pharmacophore-oriented 3D molecular generation toward efficient feature-customized drug discovery. *Nat. Comput. Sci.* **5**, 509–519 (2025).  
[3] Wu, K. et al. TamGen: drug design with target-aware molecule generation through a chemical language model. *Nat. Commun.* **15**, 9360 (2024).  
[4] Wang, H. et al. LLM-Augmented Chemical Synthesis and Design Decision Programs. *arXiv preprint arXiv:2505.08374* (2025).  
[5] Antunes, L. M., Butler, K. T. & Grau-Crespo, R. Crystal structure generation with a transformer-based generative model. *Nat. Commun.* **15**, 10570 (2024).  
[6] Yang, Z. et al. MOOSE-Chem2: Exploring the Limits of Large Language Models in Fine-Grained Scientific Hypothesis Generation via Hierarchical Search. *arXiv preprint arXiv:2505.19209* (2025).  
[7] Lin, K. et al. Integrating Retrosynthetic Accessibility into De Novo Molecular Design. *J. Chem. Inf. Model.* **63**, 7605–7615 (2023).  
[8] Boda, I. & Gál, T. Synthetic complexity-aware molecular generation. *J. Cheminform* **15**, 105 (2023).  
[9] 郭春生等. 大语言模型加速材料设计——从知识挖掘到智能设计的全链条赋能. *物理学报* **74**, 188101 (2025). [wulixb.iphy.ac.cn](https://wulixb.iphy.ac.cn/cn/article/doi/10.7498/aps.74.20250497?viewType=HTML)  
[10] 国家自然科学基金委员会. 我国学者在人工智能生成式药物设计研究方面取得进展. [www.nsfc.gov.cn](https://www.nsfc.gov.cn/p1/3381/2825/95786.html) (2025).  
[11] 国家自然科学基金委员会. 我国学者在AI药物分子设计方面取得进展. [www.nsfc.gov.cn](https://www.nsfc.gov.cn/p1/3381/2825/95699.html) (2025).  
[12] 科技行者. 突破极限：科学家通过层级搜索让大模型实现精细化科学假设发现. [www.techwalker.com](https://www.techwalker.com/2025/0529/3166957.shtml) (2025).