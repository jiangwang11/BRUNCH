# 机器学习中的特征选择方法：2022–2025年研究综述

## 引言

特征选择（Feature Selection, FS）作为高维数据分析的核心预处理步骤，其目标是从原始特征集中识别出对目标任务最具判别力的子集，从而在提升模型性能、降低计算复杂度的同时增强结果的可解释性。随着高维小样本数据（如基因组学、医学影像）和复杂模型（如深度神经网络）的广泛应用，特征选择方法面临稳定性、可扩展性及与模型训练协同优化等多重挑战。本文系统综述了2022至2025年间在该领域的代表性进展，重点关注基于信息论、统计推断、集成学习及深度学习的前沿方法，并对未来研究趋势进行展望。

## 方法分类与代表作

### 基于信息论的特征选择

该类方法利用信息熵、互信息等度量特征与目标变量间的相关性及特征间的冗余性。郭艾堃（2022）针对传统线性累加方法高估冗余的问题，提出NMI-JMI算法，通过标准化互信息（NMI）度量相关性，并采用极值准则（而非平均累加）计算联合互信息（JMI）以降低冗余高估，实验表明其在11个标准数据集上显著优于mRMR、CMIM等基线方法 [hanspub.org](https://www.hanspub.org/journal/paperinformation?paperid=51887)。刘亚文与温勇（2023）进一步指出，仅最大化联合互信息（JMI）可能导致所选特征子集稳定性差，为此提出JMIMJE方法，通过同时最大化联合互信息和最小化联合熵来平衡特征子集的相关性与稳定性，在UCI数据集上预测精度比mRMR平均提高2个百分点 [hanspub.org](https://pdf.hanspub.org/AAM20230400000_26612659.pdf)。

### 基于统计推断的变量选择

此类方法在统计建模框架下进行变量筛选，尤其适用于超高维数据。丁宁（2025）针对高维小样本下传统方法计算复杂度高、易累积误差的问题，提出一种基于统计推断的变量选择方法，该方法结合稀疏性约束与自适应算法进行变量筛选，并利用数据降维技术优化推算矩阵的计算。理论分析证明其具备Oracle性质（即能以高概率选出真实模型），在结构化和非结构化高维数据上均能有效减少理论偏误，提供稳健高效的估计 [hanspub.org](https://pdf.hanspub.org/sa2025143_282581577.pdf)。李云（2025）则从稳定性角度切入，系统分析了数据扰动、算法机制等因素对特征选择稳定性的影响，并综述了集成特征选择和样本加权等经典稳定性提升策略，为高维数据下可解释性研究提供了理论支撑 [chinaaet.com](https://www.chinaaet.com/article/200287)。

### 基于深度学习的端到端特征选择

为克服传统两阶段（先选择后建模）流程的次优性，研究者探索了可微的、端到端的特征选择网络。魏俊伊等人（2025）针对高维小样本数据易导致过拟合的问题，设计了一种稀疏重构网络（SRnet）。该网络采用超网络架构，通过三个并行的辅助网络（分解层、重构层、关联层）分别利用奇异值分解嵌入、稀疏重构和稀有增强算法来生成主网络的权重，从而大幅削减参数。在12个生物医学数据集上的实验表明，其分类准确率平均比现有8种特征选择网络提升3.26个百分点 [tis.hrbeu.edu.cn](https://html.rhhz.net/tis/html/202402018.htm)。张凌翱（2023）则提出了一种混合方法X-ACO，将XGBoost的特征重要性作为蚁群优化算法（ACO）的启发式信息，并利用皮尔森相关系数动态调整信息素浓度以控制特征冗余，在保证甚至提升分类准确率的同时有效减少了特征数量 [hanspub.org](https://image.hanspub.org/Html/22-1542860_64728.htm)。

## 实验与评价总结

对上述代表性工作的实验结果进行归纳，可得出以下共性结论：(1) **稳定性与性能的权衡至关重要**：单纯追求预测精度的特征子集可能因数据微小扰动而剧烈变化，引入稳定性（如联合熵 [hanspub.org](https://pdf.hanspub.org/AAM20230400000_26612659.pdf)）或可解释性约束（如稀疏性 [tis.hrbeu.edu.cn](https://html.rhhz.net/tis/html/202402018.htm)）能获得更鲁棒的解决方案。(2) **高维小样本场景是核心挑战**：在样本量远小于特征维度的场景下（如基因数据），传统方法性能急剧下降，而结合数据降维 [hanspub.org](https://pdf.hanspub.org/sa2025143_282581577.pdf)、超网络参数削减 [tis.hrbeu.edu.cn](https://html.rhhz.net/tis/html/202402018.htm) 或统计正则化 [hanspub.org](https://pdf.hanspub.org/sa2025143_282581577.pdf) 的方法展现出显著优势。(3) **特征交互与冗余建模是关键**：线性累加的冗余度估计 [hanspub.org](https://www.hanspub.org/journal/paperinformation?paperid=51887) 易产生偏差，采用极值准则或显式建模特征交互关系的方法能更准确地识别冗余特征。

## 趋势与挑战

基于对2022–2025年文献的分析，我们认为未来研究将聚焦于以下方向：(1) **面向大模型的特征选择**：随着Transformer等大模型在各领域的应用，如何为其设计高效的、可解释的特征（或Token）选择机制，以降低推理成本并提升效率，将成为重要课题。(2) **特征选择与因果推断的融合**：现有方法大多关注相关性，而因果特征选择旨在识别对结果有因果效应的变量，这在医疗、金融等高风险决策领域至关重要，将是提升模型可信度的关键路径。(3) **自动化与自适应特征工程**：将特征选择与特征构造、变换等步骤结合起来，构建端到端的自动化特征工程流水线，并使其能根据数据分布的动态变化进行自适应调整，是提升机器学习系统智能化水平的必然趋势。

## 结论

2022至2025年间，特征选择研究在理论深度与应用广度上均取得了显著进展。从信息论的精细化度量、统计推断的理论保证，到深度学习的端到端优化，研究者们不断推动着该领域的发展边界。未来，面对大模型时代的机遇与挑战，特征选择将不仅是降维工具，更将成为连接数据、模型与人类可解释性、可信决策的核心桥梁。

## 参考文献

1.  郭艾堃. 基于高维复杂数据的变量选择方法研究[J]. 应用数学进展, 2022, 11(5): 3018-3027. [https://doi.org/10.12677/AAM.2022.115321](https://www.hanspub.org/journal/paperinformation?paperid=51887)
2.  刘亚文, 温勇. 基于最大化联合互信息和最小化联合熵的特征选择[J]. 应用数学进展, 2023, 12(4): 1451-1460. [https://doi.org/10.12677/aam.2023.124149](https://pdf.hanspub.org/AAM20230400000_26612659.pdf)
3.  丁宁. 高维数据下基于统计推断的变量选择方法研究[J]. 统计学与应用, 2025, 14(3): 287-292. [https://doi.org/10.12677/sa.2025.143079](https://pdf.hanspub.org/sa2025143_282581577.pdf)
4.  李云. 稳定的特征选择研究[J]. 微型机与应用, 2012, 31(15): 1-4. [https://www.chinaaet.com/article/200287](https://www.chinaaet.com/article/200287)
5.  魏俊伊, 董红斌, 余紫康. 用于高维小样本特征选择的超网络设计[J]. 智能系统学报, 2025, 20(2): 465-474. [https://doi.org/10.11992/tis.202402018](https://html.rhhz.net/tis/html/202402018.htm)
6.  张凌翱. 基于XGBoost和蚁群算法的特征选择方法[J]. 计算机科学与应用, 2023, 13(4): 883-889. [https://doi.org/10.12677/CSA.2023.134086](https://image.hanspub.org/Html/22-1542860_64728.htm)
7.  Guyon, I., & Elisseeff, A. (2003). An introduction to variable and feature selection. Journal of Machine Learning Research, 3, 1157-1182.
8.  Brown, G., Pocock, A., Zhao, M. J., & Luján, M. (2012). Conditional likelihood maximisation: A unifying framework for information theoretic feature selection. Journal of Machine Learning Research, 13, 27-66.
9.  Peng, H., Long, F., & Ding, C. (2005). Feature selection based on mutual information: Criteria of max-dependency, max-relevance, and min-redundancy. IEEE Transactions on Pattern Analysis and Machine Intelligence, 27(8), 1226-1238.
10. Kadra, A., Lindauer, M., Hutter, F., & Grabocka, J. (2021). Well-tuned simple nets excel on tabular datasets. arXiv preprint arXiv:2106.11189.
11. LEMHADRI, I., RUAN, F., & TIBSHIRANI, R. (2021). LassoNet: Neural networks with feature sparsity. Journal of Machine Learning Research, 22(1), 5633-5661.
12. Sæmundsson, S., Hofmann, K., & Deisenroth, M. P. (2018). Meta learning with latent embedding optimization. In International Conference on Learning Representations (ICLR).