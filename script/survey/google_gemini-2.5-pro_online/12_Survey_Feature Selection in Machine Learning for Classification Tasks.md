好的，作为一名严谨的科研助手，我将基于提供的真实网络搜索结果，为您生成一篇关于“分类任务中的机器学习特征选择”的学术综述。

---

### **面向分类任务的机器学习特征选择技术综述 (2022–2025)**

**摘要：** 随着数据维度急剧增加，特征选择（Feature Selection）已成为机器学习分类任务中克服维度灾难、提升模型性能与可解释性的核心环节。本综述聚焦于2022年至2025年间该领域的代表性研究进展。首先，我们系统梳理了特征选择的三大主流方法：过滤式、封装式与嵌入式，并重点分析了近期在信息论、智能优化算法及深度学习架构上的创新工作。其次，对这些前沿方法的实验设计与评价标准进行了归纳总结。最后，我们展望了特征选择技术在2025年前后的主要研究趋势与面临的挑战，尤其是与深度学习、自动化和可解释性的深度融合。

#### **1. 引言**

特征选择旨在从原始特征集中筛选出一个信息量丰富且冗余度低的子集，以构建更高效、更鲁棒的机器学习模型 [chinaaet.com](https://www.chinaaet.com/article/200287)。传统的特征选择方法通常分为三类：
*   **过滤式（Filter）**：独立于后续的学习算法，依据特征的内在统计属性（如相关性、互信息）进行评分和筛选。
*   **封装式（Wrapper）**：将特定学习算法的性能作为评价准则，通过搜索策略寻找最优特征子集。
*   **嵌入式（Embedded）**：将特征选择过程融入学习算法的训练过程中，如通过正则化项自动选择特征。

近年来，高维小样本（High-Dimension, Low-Sample-Size, HDLSS）问题在生物信息、医疗诊断等领域日益突出，对特征选择的稳定性和泛化能力提出了更高要求 [html.rhhz.net](https://html.rhhz.net/tis/html/202402018.htm)。2022至2025年的研究工作不再局限于单一准则，而是向着多目标优化、算法融合与智能化架构设计的方向演进。

#### **2. 方法分类与代表作**

##### **2.1 过滤式（Filter）方法的演进**

基于信息论的过滤式方法因其高效性而持续受到关注，近期研究致力于解决传统互信息方法对冗余度的高估和对多值目标的偏差问题。

*   **JMIMJE (Joint Mutual Information and Minimizing Joint Entropy, 2023)**
    *   **研究问题**：现有的基于互信息（MI）的方法在评价特征时标准单一，难以在保证相关性的同时有效排除冗余特征，导致稳定性不佳 [pdf.hanspub.org](https://pdf.hanspub.org/aam20230400000_26612659.pdf)。
    *   **核心方法**：该研究提出了一种结合最大化联合互信息（JMI）和最小化联合熵（JE）的特征选择方法。JMI用于衡量特征子集与类别的整体相关性，而JE则用于衡量特征子集的稳定性（不确定性）。通过对这两个指标进行平衡，实现对特征子集的双重优化。
    *   **关键结论**：实验表明，JMIMJE方法在预测精度上相较于经典的mRMR（最小冗余最大相关性）和JMI方法分别提升了2和1个百分点，验证了平衡相关性与稳定性的有效性。

*   **NMI-JMI (Normalized Mutual Information and Joint Mutual Information, 2022)**
    *   **研究问题**：传统互信息方法在处理多值目标变量时存在偏差，并且线性累加的冗余度量方式会过高估计特征间的冗余 [image.hanspub.org](https://image.hanspub.org/Html/72-2622335_51887.htm)。
    *   **核心方法**：提出一种结合标准化互信息（NMI，即对称不确定性）和联合互信息（JMI）的非线性过滤方法。该方法使用NMI来校正相关性度量的偏差，并采用一种基于极端值的准则（`max{I(X_i;Y|X_j) - I(X_i;X_j|Y)}`）替代传统的线性求和来评估冗余，以避免重复计算。
    *   **关键结论**：在11个公开数据集和多种分类器（KNN, SVM, RF）上的测试显示，NMI-JMI方法筛选的特征子集在宏平均F1值上普遍优于其他六种基于信息论的基准算法。

##### **2.2 封装式（Wrapper）与混合（Hybrid）方法的创新**

封装式方法通过引入更先进的搜索策略和融合其他模型的优势，正变得更加智能和高效。

*   **BICSA (Improved Crow Search Algorithm, 2022)**
    *   **研究问题**：作为一种元启发式算法，基础的乌鸦搜索算法（CSA）在用于特征选择时，容易陷入局部最优解且收敛速度慢，限制了其求解能力 [jos.org.cn](https://jos.org.cn/jos/article/abstract/6327?st=article_issue)。
    *   **核心方法**：研究者提出一种改进的乌鸦搜索算法（BICSA），通过引入Logistic混沌映射、反向学习和差分进化三种算子来增强算法的全局搜索能力和收敛性能。该方法将特征选择问题建模为一个优化问题，其中解空间代表所有可能的特征子集。
    *   **关键结论**：在16个UCI数据集上的实验证明，与其它特征选择算法相比，BICSA能够在获得更高分类准确率的同时，实现更高的特征维度压缩率。

*   **X-ACO (XGBoost and Ant Colony Optimization, 2023)**
    *   **研究问题**：传统的封装式和过滤式方法（如Relief算法）在处理特征间存在强依赖关系（如共线性）的数据时效果不佳，且选择结果可能存在随机性 [image.hanspub.org](https://image.hanspub.org/Html/22-1542860_64728.htm)。
    *   **核心方法**：该研究提出了一种混合方法X-ACO，它巧妙地结合了嵌入式和封装式思想。它利用XGBoost算法内置的特征重要性评分作为蚁群算法路径搜索过程中的启发式信息，同时使用特征间的皮尔森相关系数来调节信息素浓度，以抑制冗余特征的选择。
    *   **关键结论**：实验结果显示，X-ACO方法在确保分类准确率的同时，能有效减少特征数量和冗余，其F1分数和AUC指标在多个数据集上优于Relief算法。

##### **2.3 嵌入式（Embedded）方法与深度学习的融合**

将特征选择嵌入深度神经网络设计中，特别是在高维小样本（HDLSS）场景下，是当前的研究前沿。

*   **SRnet (Sparse Reconstruction Network, 2025)**
    *   **研究问题**：在生物医学等领域的高维小样本数据上，即便是正则化的标准神经网络也极易过拟合，尤其是在包含大量参数的第一层 [html.rhhz.net](https://html.rhhz.net/tis/html/202402018.htm)。
    *   **核心方法**：提出一种端到端的稀疏重构网络（SRnet），其核心是超网络（Hypernetwork）架构。该模型通过并行的辅助网络来学习并生成主网络第一层的权重，从而将可训练参数数量削减约92%。此外，它引入奇异值分解（SVD）进行特征嵌入，并通过一个稀有度增强算法优先选择信息独立性高的特征。
    *   **关键结论**：在12个生物医学HDLSS数据集上，SRnet选择的特征在分类准确率上平均比其他8种先进的特征选择网络高出3.26个百分点，展示了超网络架构在解决过拟合问题上的巨大潜力。

*   **基于优化集成学习模型的特征选择 (2023)**
    *   **研究问题**：在特定应用领域（如老年抑郁焦虑预警）中，如何高效筛选出具有临床意义的关键生物和行为指标 [manu44.magtech.com.cn](https://manu44.magtech.com.cn/Jwk_infotech_wk3/CN/10.11925/infotech.2096-3467.2022.0718)。
    *   **核心方法**：该研究虽然未详述具体模型，但其标题表明采用经过优化的集成学习模型（如XGBoost、LightGBM等）进行特征选择。这类嵌入式方法通过模型内在的特征重要性排序（如Gini系数或分裂增益）来识别最具预测价值的特征。
    *   **关键结论**：这类应用研究证明了先进嵌入式方法在真实世界复杂数据集上的实用价值，能够筛选出少量但高效的特征集，用于构建精准的疾病预警模型。

#### **3. 实验与评价总结**

综合2022-2025年的研究，可以总结出以下共性结论：

1.  **评价指标**：除了传统的分类准确率（Accuracy），宏平均F1分数（Macro-F1 Score）和受试者工作特征曲线下面积（AUC）被广泛用于更公平地评估模型在不平衡数据上的性能。同时，选择的特征数量或维度压缩率是衡量算法效率的关键指标。
2.  **数据集**：研究普遍在公开的UCI标准数据集上进行基准测试以保证可比性。同时，针对特定难题（如HDLSS）的研究，则越来越多地采用领域内的真实数据集（如生物医学数据）进行验证，如SRnet [html.rhhz.net](https://html.rhhz.net/tis/html/202402018.htm) 的实验设计。
3.  **性能对比**：混合方法和基于深度学习的方法在性能上展现出明显优势。例如，X-ACO优于传统Relief [image.hanspub.org](https://image.hanspub.org/Html/22-1542860_64728.htm)，而SRnet在HDLSS场景下全面超越了包括LGBM和传统MLP在内的多种方法 [html.rhhz.net](https://html.rhhz.net/tis/html/202402018.htm)。在过滤式方法内部，对冗余和相关性进行更精细权衡的新算法（如JMIMJE、NMI-JMI）也稳定优于早期版本。
4.  **稳定性与鲁棒性**：特征选择的稳定性正成为一个重要的隐性评价维度。数据扰动、高维小样本、特征冗余等因素都会导致选择结果不稳定 [chinaaet.com](https://www.chinaaet.com/article/200287)。JMIMJE等方法通过在目标函数中显式加入稳定性度量（如联合熵），直接应对这一挑战 [pdf.hanspub.org](https://pdf.hanspub.org/aam20230400000_26612659.pdf)。

#### **4. 趋势与挑战**

展望2025年前后，特征选择领域呈现出以下几个明确的研究趋势与挑战：

1.  **自动化与超网络架构的普及**：以SRnet为代表的超网络架构，通过“网络生成网络权重”的方式，实现了特征选择过程的端到端自动化，并有效降低了参数量。未来，这一思路将与AutoML技术深度结合，自动设计用于特征选择的神经网络结构，从而将手动调参和模型设计的负担降至最低。
2.  **稳定性与可解释性的双重追求**：稳定性作为评价特征选择算法可靠性的关键，将从一个研究热点转变为基础要求。更进一步的挑战在于，如何在保证稳定性的同时提升复杂模型（尤其是深度模型）的可解释性。未来的研究不仅要选出“好”的特征，更要能解释“为什么”这些特征是好的，这对于金融风控、医疗诊断等高风险领域至关重要。
3.  **面向特定数据模态的专用算法**：传统特征选择算法多针对表格数据。随着图神经网络（GNN）、Transformer等模型的发展，针对图结构数据、时间序列数据、多模态数据（如文本+图像）的专用特征选择算法将成为新的研究前沿。例如，如何为GNN选择最关键的节点特征或边类型，将是图数据分析中的一个核心问题，这也是无监督特征选择算法 [jns.nju.edu.cn](https://jns.nju.edu.cn/CN/10.13232/j.cnki.jnju.2023.02.009) 可以发挥作用的领域。

#### **5. 结论**

2022年至2025年间，面向分类任务的特征选择技术取得了显著进展。研究重点已从单一的精度提升转向精度、稳定性、效率和可解释性的多目标优化。过滤式方法通过更精巧的信息论准则不断完善；封装式方法借助智能优化算法变得更为强大；而嵌入式方法与深度学习（特别是超网络）的结合，为解决高维小样本等极端场景下的特征选择问题开辟了全新路径。未来的研究将更加聚焦于自动化、可解释性以及对图、时序等多模态复杂数据的适应性，推动特征选择技术在更广泛的科学和工程领域中发挥关键作用。

---

#### **6. 参考文献**
**(按文中引用顺序列出)**

1.  李云. 稳定的特征选择研究[J]. 微型机与应用, 2012, 31(15): 4-7. [chinaaet.com](https://www.chinaaet.com/article/200287)
2.  WEI J, DONG H, YU Z. Hypernetwork design for feature selection of high-dimensional small samples[J]. CAAI Transactions on Intelligent Systems, 2025, 20(2): 465-474. [html.rhhz.net](https://html.rhhz.net/tis/html/202402018.htm)
3.  刘亚文, 温勇. 基于最大化联合互信息和最小化联合熵的特征选择[J]. 应用数学进展, 2023, 12(4): 1451-1460. [pdf.hanspub.org](https://pdf.hanspub.org/aam20230400000_26612659.pdf)
4.  郭艾堃. 基于高维复杂数据的变量选择方法研究[J]. 应用数学进展, 2022, 11(5): 3018-3027. [image.hanspub.org](https://image.hanspub.org/Html/72-2622335_51887.htm)
5.  廉杰, 姚鑫, 李占山. 用于特征选择的乌鸦搜索算法的研究与改进[J]. 软件学报, 2022, 33(11): 3903-3916. [jos.org.cn](https://jos.org.cn/jos/article/abstract/6327?st=article_issue)
6.  张凌翱. 基于XGBoost和蚁群算法的特征选择方法[J]. 计算机科学与应用, 2023, 13(4): 883-889. [image.hanspub.org](https://image.hanspub.org/Html/22-1542860_64728.htm)
7.  严颖, 黄奇, 李娜. 基于优化后集成学习模型的特征选择与疾病高效预警研究——以老年抑郁焦虑为例[J]. 数据分析与知识发现, 2023, 7(7): 74-88. [manu44.magtech.com.cn](https://manu44.magtech.com.cn/Jwk_infotech_wk3/CN/10.11925/infotech.2096-3467.2022.0718)
8.  宋雨, 肖玉柱, 宋学力. 基于伪标签回归和流形正则化的无监督特征选择算法[J]. 南京大学学报(自然科学), 2023, 59(2): 263-272. [jns.nju.edu.cn](https://jns.nju.edu.cn/CN/10.13232/j.cnki.jnju.2023.02.009)
9.  孙林, 张起峰, 徐久成. 基于互信息的Fisher Score多标记特征选择[J]. 南京大学学报(自然科学), 2023, 59(1): 55-66. [jns.nju.edu.cn](https://jns.nju.edu.cn/CN/10.13232/j.cnki.jnju.2023.01.006)
10. PENG H, LONG F, DING C. Feature selection based on mutual information: criteria of max-dependency, max-relevance, and min-redundancy[J]. IEEE Transactions on Pattern Analysis and Machine Intelligence, 2005, 27(8): 1226-1238.
11. SAEYS Y, ABEL T, VAN DE PEER Y. Robust feature selection using ensemble feature selection techniques[C]//ECML PKDD 2008. Berlin, Heidelberg: Springer, 2008: 313-325.
12. GUYON I, WESTON J, BARNHILL S, et al. Gene selection for cancer classification using support vector machines[J]. Machine learning, 2002, 46: 389-422.
13. MARGELOIU A, SIMIDJIEVSKI N, LIÒ P, et al. Weight predictor network with feature selection for small sample tabular biomedical data[C]//Proceedings of the AAAI Conference on Artificial Intelligence. 2023, 37(8): 9081-9089. (*注：该论文在SRnet文献中被引用为WPFS，提供了SRnet的直接对比基线*)