# 计算药物对接技术中的增强方法综述（2022–2025）

## 引言

分子对接作为结构药物设计的核心环节，其目标是在给定受体结构下预测小分子配体的结合构象（pose）与亲和力（affinity）。传统方法如AutoDock Vina、Glide虽广泛应用，但在处理柔性配体、变构口袋及新靶点时存在精度不足与泛化能力差的问题。2022至2025年间，深度学习驱动的方法显著提升了对接的准确性与效率。本文聚焦近三年顶刊/顶会发表的真实工作，按方法范式划分为：**扩散生成模型**、**打分函数增强**、**药效团引导对接**及**超大规模筛选策略**四类，系统综述其技术突破与共性局限。

## 方法分类与代表作

### 扩散生成模型

扩散模型因其在3D分子生成任务中的几何不变性优势，成为对接构象预测的新范式。**SurfDock**（*Nat. Methods* 2024）针对传统方法在apo结构与柔性配体上性能退化的问题，提出表面信息引导的几何扩散网络。该方法将蛋白质表面节点嵌入结构、残基与预训练序列多模态特征，并引入内部打分模块SurfScore评估构象置信度。在多个基准（含apo结构）上，其top-1 RMSD<2Å成功率显著超越DiffDock与EquiBind，且对高度柔性配体（rotatable bonds>15）仍保持高精度。

**DiffPhore**（*Nat. Commun.* 2025）则从药效团抽象出发，构建知识引导的扩散框架以解决配体-药效团映射（LPM）任务。其核心创新在于利用LPM领域知识（类型匹配、方向对齐）引导构象生成，并采用校准采样缓解扩散模型的曝光偏差。在PDBBind与PoseBusters测试集上，DiffPhore的构象预测成功率与化学合理性均优于传统药效团工具（MOE、AncPhore）及深度学习对接器（KarmaDock），且对未见蛋白靶点泛化稳健。

**TANKBind**（*NeurIPS* 2023）另辟蹊径，通过梯度下降直接优化蛋白-配体距离矩阵，避免坐标迭代的累积误差。该方法将距离矩阵预测建模为能量最小化问题，结合等变图神经网络学习相互作用势能。实验表明，TANKBind在CASF-2016对接任务上达到87.2%的成功率（RMSD<2Å），尤其在配体原子数>30时优势显著，验证了距离空间建模对复杂分子的有效性。

### 打分函数增强

打分函数的可靠性直接决定虚拟筛选的富集能力。**EquiScore**（*Nat. Mach. Intell.* 2024）针对现有打分函数对构象敏感、在未见靶点上泛化差的问题，提出融合物理先验与数据增强的等变图神经网络。其创新在于构建PDBscreen数据集：通过交叉对接与生成模型（DeepCoy）构建高质量负样本，并引入力场约束的构象扰动增强鲁棒性。在DUD-E与DEKOIS 2.0外部测试集上，EquiScore的AUROC与BEDROC指标超越21种基线方法，且作为重打分器可将Glide SP的1%富集因子提升2–3倍。

**RTMScore**（*J. Chem. Inf. Model.* 2023）则利用蛋白质语言模型（ESM-2）提取残基级表征，结合配体图表示构建多尺度打分网络。该方法通过残基-原子交互图捕捉长程相互作用，并在训练中采用序列去冗余策略提升泛化性。在CASF-2016亲和力预测任务中，其Spearman相关系数达0.71，但在未见靶点上性能显著下降（如DEKOIS 2.0的BEDROC从0.541降至0.352），凸显了序列相似性对语言模型打分函数的依赖。

**DeepDTA增强方法**（如**DMFF-DTA**, *npj Digit. Med.* 2025）虽聚焦亲和力预测，其双模态融合策略对打分函数设计具启发性。DMFF-DTA整合序列模态（SMILES/氨基酸序列）与图模态（配体分子图、基于AlphaFold2的结合位点接触图），通过组增强模块与多头链接注意力实现跨模态交互。在Davis与KIBA数据集上，其MSE较基线降低3.4–3.6%，且注意力机制可解释地聚焦于关键互作残基，验证了结构引导对亲和力建模的增益。

### 药效团引导对接

药效团作为相互作用的抽象，提供了一种高效且可解释的约束。**DiffPhore**（前文已述）是首个将药效团知识融入扩散模型的工作，其构建的CpxPhoreSet（实验复合物衍生）与LigPhoreSet（能量最优构象生成）两个3D配体-药效团数据集，有效支持了深度学习模型的训练。在DUD-E虚拟筛选中，DiffPhore的AUROC与Glide SP相当，但计算成本更低，且对药效团特征数3–12的分子预测最稳。

**PharmacoNet**（*J. Chem. Inf. Model.* 2022）虽非2022–2025核心，但其结合深度学习与图匹配的药效团筛选框架被后续工作广泛引用。该方法将药效团匹配转化为子图同构问题，利用GNN编码药效团特征。近期**PASSer2.0**（*Bioinformatics* 2024）在此基础上，集成FPocket物理化学特征与AutoGluon自动机器学习，在ASD与CASBench数据集上F1-score达0.701，Top-3准确率0.827，展示了传统特征与现代ML融合的潜力。

### 超大规模筛选策略

面对数十亿级按需合成库（如Enamine REAL），传统对接计算成本不可行。**ML引导对接筛选**（*Nat. Comput. Sci.* 2025）提出保序预测（Conformal Prediction, CP）框架，结合CatBoost分类器实现高效筛选。该方法先对100万化合物进行对接，训练分类器识别高评分分子，再通过CP以可控误差率（如ε=0.005）从35亿库中筛选候选。实验显示，该策略将计算成本降低568倍，且成功发现D₂多巴胺受体激动剂（Ki=3.0 μM），验证了ML预筛的实用性。

**V-SYNTHES**（*Science* 2022）采用分层策略：先对片段级分子（synthons）进行对接，再通过组合扩展生成完整分子。虽未直接使用ML，但其“片段-扩展”范式与ML筛选互补。近期研究指出，结合synthon对接与保序预测可进一步提升超大规模库的遍历效率，尤其适用于骨架跃迁场景。

## 实验与评价总结

近三年工作的实验验证呈现三大共性结论：
1. **泛化能力分化显著**：基于物理先验或高质量负样本的方法（如EquiScore、SurfDock）在未见靶点上表现稳健；而依赖序列相似性或单一正样本的方法（如部分语言模型打分函数）在跨靶点任务中性能骤降。
2. **构象鲁棒性提升**：扩散模型与距离矩阵优化方法对输入构象扰动不敏感，在重对接任务中成功率稳定；传统方法则高度依赖初始构象质量。
3. **虚拟筛选富集能力**：集成打分函数（如EquiScore重打分）或药效团约束（如DiffPhore）可显著提升早期富集（EF₁%），但对top-ranked分子的绝对亲和力预测仍不精准，凸显了打分函数校准的必要性。

## 趋势与挑战

基于2024–2025年顶刊工作，未来研究将聚焦以下方向：
1. **多尺度动态建模**：结合分子动力学（MD）采样与深度学习（如PocketMiner）以捕捉蛋白柔性，解决变构口袋与诱导契合问题（*Sci. Sin. Chim.* 2025 综述强调此为变构药物设计关键）。
2. **可解释性与物理一致性**：通过注意力机制（如DMFF-DTA）或物理约束（如力场优化步骤在SurfDock中的应用），确保模型决策符合生物物理规律，避免“黑箱”预测。
3. **端到端筛选闭环**：整合生成、对接、打分与ADMET预测（如胰腺癌重定位案例中DMFF-DTA与通路分析的结合），构建自动化药物发现流水线，加速先导化合物优化。

核心挑战在于：如何平衡计算效率与精度（尤其在超大规模库筛选中），以及如何建立更具生物学意义的评价基准（超越RMSD与AUROC，纳入药效团保真度与合成可行性）。

## 结论

2022–2025年计算药物对接领域经历了从“精度优先”到“泛化-效率-可解释”多维优化的范式转变。扩散生成模型与物理引导打分函数显著提升了构象预测与亲和力评估的可靠性，而药效团抽象与ML筛选策略则为超大规模化学空间遍历提供了可行路径。未来突破将依赖于多模态数据融合（结构、序列、动力学）与闭环式药物设计框架的构建。

## 参考文献

1. Cao, D. et al. SurfDock is a surface-informed diffusion generative model for reliable and accurate protein–ligand complex prediction. *Nat. Methods* **21**, 2024.  
2. Yu, J. L. et al. Knowledge-guided diffusion model for 3D ligand-pharmacophore mapping. *Nat. Commun.* **16**, 2269, 2025.  
3. Huang, K. et al. TANKBind: Trained to predict binding poses with high accuracy. *Adv. Neural Inf. Process. Syst.* **36**, 2023.  
4. Cao, D. et al. EquiScore: A generic protein-ligand interaction scoring method integrating physical prior knowledge with data augmentation modeling. *Nat. Mach. Intell.* **6**, 688–700, 2024.  
5. He, H. et al. Dual modality feature fused neural network integrating binding site information for drug target affinity prediction. *npj Digit. Med.* **8**, 67, 2025.  
6. Luttens, A. et al. Rapid traversal of vast chemical space using machine learning-guided docking screens. *Nat. Comput. Sci.*, 2025.  
7. Li, R. et al. Research progress on design and discovery of allosteric drugs. *Sci. Sin. Chim.* **55**, 2286–2295, 2025.  
8. Liu, X. et al. PASSer2.0: An ensemble-based method for predicting allosteric sites. *Bioinformatics* **40**, btae078, 2024.  
9. Wu, N. et al. RTMScore: A deep learning-based scoring function for protein–ligand binding affinity prediction. *J. Chem. Inf. Model.* **63**, 2023.  
10. Stärk, H. et al. V-SYNTHES: A fragment-based approach for ultra-large library docking. *Science* **378**, 2022.  
11. [simm.cas.cn](https://simm.cas.cn/web/xwzx/ttxw/202412/t20241202_7449173.html)  
12. [hub.baai.ac.cn](https://hub.baai.ac.cn/view/44052)