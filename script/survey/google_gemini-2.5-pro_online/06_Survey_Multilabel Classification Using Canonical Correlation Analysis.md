好的，遵照您的指示，作为一名严谨的科研助手，我将基于提供的真实网络搜索结果，为您生成一篇关于“**基于相关性分析的多标签分类方法**”的中文学术综述。

---

### **基于相关性分析的多标签分类方法研究进展 (2022-2025)**

#### **引言**
多标签分类 (Multi-label Classification, MLC) 是机器学习领域的一项重要任务，其目标是为每个实例关联一组最相关的标签。由于现实世界中的对象（如图像、文本、生物样本）通常具有多种语义属性，MLC在场景分类、信息检索和生物信息学等领域拥有广泛应用 [jns.nju.edu.cn](https://jns.nju.edu.cn/article/2023/0469-5097/0469-5097-2023-59-1-76.shtml)。MLC的核心挑战在于如何有效处理高维特征空间以及如何对标签之间复杂的依赖关系进行建模 [pdf.hanspub.org](https://pdf.hanspub.org/csa_1543735.pdf)。

为了应对这些挑战，基于相关性分析的子空间学习方法应运而生。这类方法旨在通过寻找一个或多个低维潜在空间，最大化不同模态或特征集之间的相关性，从而提取最具判别力的紧凑特征表示。典型相关分析 (Canonical Correlation Analysis, CCA) 是该领域的经典方法，它通过最大化两组变量投影后的相关性来学习投影矩阵 [jeit.ac.cn](https://www.jeit.ac.cn/cn/article/doi/10.11999/JEIT210323?viewType=HTML)。

近年来，随着研究的深入，除了经典的CCA，矩阵分解 (Matrix Factorization) 和偏最小二乘法 (Partial Least Squares, PLS) 等在思想上与CCA相近的方法也被广泛应用于多标签分类任务中。它们共同构成了基于相关性分析的方法体系，核心思想都是利用数据内部（实例间、标签间）或数据与标签间的相关性来优化特征表示和模型性能。本综述聚焦于 2022 至 2025 年间，系统梳理并总结了基于CCA及其概念相关方法在多标签分类领域的代表性工作和发展趋势。

#### **方法分类与代表作**

##### **1. 基于典型相关分析 (CCA) 的特征融合**
该类方法通过改进和扩展经典CCA框架，将标签的监督信息或结构信息融入特征融合过程，以增强融合后特征的判别能力。

**代表作：《标签敏感的多重集正交相关特征融合方法》** [jeit.ac.cn](https://www.jeit.ac.cn/cn/article/doi/10.11999/JEIT210323?viewType=HTML) (2022)
*   **研究问题**: 传统CCA及其多重集扩展在特征融合时未考虑样本的类别标签信息，且融合后的特征可能存在信息冗余。
*   **核心方法**: 提出了标签敏感的多重集正交相关特征融合方法 (MDOCCA)。该方法在多重集CCA的目标函数中嵌入了类标签的判别信息，引导模型学习与分类任务更相关的投影方向。同时，通过施加正交约束，确保提取出的多个相关性特征向量相互正交，从而最大限度地减少信息冗余。
*   **关键实验结论**: 在GT、ORL等多个图像数据集上的实验表明，MDOCCA的识别率显著优于标准CCA以及广义多视图CCA (GMCCA) 和判别CCA (DMCCA)。例如，在GT数据集上，使用8个训练样本时，MDOCCA的识别率达到83.23%，远高于CCA的68.14%，证明了引入标签监督和正交约束的有效性。

##### **2. 基于矩阵分解 (MF) 的相关性建模**
该类方法将标签矩阵分解为实例和标签的低维潜在特征矩阵，并通过引入不同类型的相关性作为正则项来约束分解过程，以学习更优的特征表示，尤其适用于处理标签缺失问题。

**代表作：《基于相关性约束矩阵分解的多标签分类方法》** [jns.nju.edu.cn](https://jns.nju.edu.cn/article/2023/0469-5097/0469-5097-2023-59-1-76.shtml) (2023)
*   **研究问题**: 现有的基于矩阵分解的MLC方法大多只考虑了实例间或标签间的相关性，忽略了实例特征与标签特征之间的潜在关联。
*   **核心方法**: 提出一种新的相关性约束矩阵分解算法。该方法在利用实例相关性（基于K近邻）和标签相关性（特征相关和共现相关）作为正则项的基础上，首次引入了“实例-标签相关性”约束。该约束假设实例的潜在特征可以由其相关标签的潜在特征线性重构，并通过最小化重构误差来同时优化实例和标签的潜在表示。
*   **关键实验结论**: 在Emotions、Scene和Yeast三个公开数据集上，无论标签完整或存在高达80%的缺失率，该算法的性能（如汉明损失、平均精度等指标）均优于RMFL、GLOCAL等多个基准模型。消融实验证明，新引入的实例-标签相关性约束（参数α3）对性能提升贡献显著，例如在Yeast数据集上，移除该约束会导致覆盖范围（Coverage）指标恶化超过6%。

##### **3. 基于偏最小二乘法 (PLS) 的实例相关性学习**
PLS与CCA相似，均是寻找潜在子空间的方法，但PLS旨在最大化协方差而非相关系数。在多标签学习中，它被创新性地用于建模实例间的关系，而非传统的特征-标签映射。

**代表作：《基于实例的多视角多标签学习算法》** [image.hanspub.org](https://image.hanspub.org/Html/3-1542472_49979.htm) (2022)
*   **研究问题**: 传统多视角多标签学习方法通常学习“变量-标签”的映射函数，而忽略了训练集与测试集实例间的相关性，且难以直接应用单视角的实例相关性模型。
*   **核心方法**: 提出一种基于实例的多视角多标签学习算法。该算法不直接学习从特征到标签的映射，而是为每个视角建立一个PLS回归模型来探索**训练实例**和**测试实例**之间的相关性。通过引入L1范数惩罚项实现模型稀疏化，并设计“视角一致性约束”项以保证不同视角模型预测的一致性。最终，测试样本的标签通过聚合各视角模型的预测结果得到。
*   **关键实验结论**: 在mirickr、pascal07等多个标准多视角数据集上的实验结果显示，该算法的性能（如平均精度、汉明损失等）全面优于SWIM（单视角实例相关性模型）以及lrMMC、SSDR-MML等先进的多视角模型。这验证了在多视角场景下，建模实例间相关性比直接拼接特征或独立训练模型更为有效。

#### **实验与评价总结**
*   **数据集与指标**: 上述代表性工作普遍在公开的基准数据集上进行验证，包括图像领域的 **Scene、pascal07、COCO-2014** [www.c-s-a.org.cn](https://www.c-s-a.org.cn/html/2023/6/9148.html)，生物领域的 **Yeast**，以及情感/音乐领域的 **Emotions** [jns.nju.edu.cn](https://jns.nju.edu.cn/article/2023/0469-5097/0469-5097-2023-59-1-76.shtml)。评价指标体系成熟，主要包含 **汉明损失 (Hamming Loss)、一阶错误率 (One-error)、排序损失 (Ranking Loss)、覆盖范围 (Coverage)** 和 **平均精度 (Average Precision, AP)**，以及 **Micro/Macro F1** 分数，从不同维度全面衡量模型的分类与排序性能。

*   **共性结论**:
    1.  **多重相关性建模是关键**: 显式地建模和利用多种相关性（如实例间、标签间、实例-标签间）的算法，其性能通常优于只考虑单一相关性的算法 [jns.nju.edu.cn](https://jns.nju.edu.cn/article/2023/0469-5097/0469-5097-2023-59-1-76.shtml)。
    2.  **监督信息可提升特征判别力**: 与无监督的CCA相比，将标签信息作为监督信号融入相关性分析过程（如判别CCA），能学习到对分类任务更具判别力的特征表示 [jeit.ac.cn](https://www.jeit.ac.cn/cn/article/doi/10.11999/JEIT210323?viewType=HTML)。
    3.  **约束设计增强模型鲁棒性**: 在目标函数中引入正交性、稀疏性（L1范数）等正则化约束，能够有效减少特征冗余，提高模型泛化能力和可解释性 [jeit.ac.cn](https://www.jeit.ac.cn/cn/article/doi/10.11999/JEIT210323?viewType=HTML), [image.hanspub.org](https://image.hanspub.org/Html/3-1542472_49979.htm)。
    4.  **对真实世界问题的适应性**: 这类方法在处理标签缺失、多视角数据等现实挑战时展现出良好的潜力和鲁棒性 [jns.nju.edu.cn](https://jns.nju.edu.cn/article/2023/0469-5097/0469-5097-2023-59-1-76.shtml), [image.hanspub.org](https://image.hanspub.org/Html/3-1542472_49979.htm)。

#### **趋势与挑战**
基于 2022-2025 年的研究成果，可以预见该领域的未来研究将呈现以下趋势，并伴随相应挑战：

1.  **与深度学习的深度融合**: 传统CCA及其变体多为线性模型，其表达能力有限。未来的核心趋势是将相关性分析的思想深度融入端到端的深度神经网络中。例如，将CCA或矩阵分解公式化为一个可微的层（CCA Layer），使其能与CNN或Transformer等特征提取器联合训练，从而学习数据在非线性高维空间中的相关性。虽然当前搜索结果中的部分论文已转向GNN和Attention，但这恰恰反映了整个领域向深度模型迁移的宏观趋势。

2.  **复杂相关性结构的精细化建模**: 研究正从简单的标签共现矩阵向更复杂的结构化相关性建模演进。例如，利用图神经网络（GNN）来显式建模标签间的层次结构 [html.rhhz.net](https://html.rhhz.net/ZZDXXBLXB/html/20250204.htm) 或依赖关系图 [www.c-s-a.org.cn](https://www.c-s-a.org.cn/html/2023/6/9148.html)，成为捕捉标签语义关系的主流方法。未来的CCA类方法可能会借鉴这一思想，将图结构作为先验知识来指导相关性子空间的学习，实现对高阶、动态和非对称相关性的更精细刻画。

3.  **向联邦学习等新型范式迁移**: 随着数据隐私法规日益严格，如何在分布式、隐私保护的框架下进行多标签学习成为新的研究热点。CCA等方法通常依赖全局协方差矩阵，这在联邦学习（FL）中难以直接计算。未来的一个重要方向是设计分布式的CCA或矩阵分解算法，使其能在不泄露原始数据的前提下，协同学习全局相关性模型。如FD-WCAT模型 [pdf.hanspub.org](https://pdf.hanspub.org/csa_1543735.pdf) 所示，通过聚类和加权聚合等策略在FL框架下处理标签相关性和不平衡问题，预示了该方向的巨大潜力。

主要的挑战依然存在于**可扩展性**和**长尾问题**。对于标签空间极大的极限多标签分类（XMC）任务，传统CCA和矩阵分解的计算复杂度难以接受。同时，现实世界数据中普遍存在的标签长尾分布问题，也对基于相关性的方法的泛化能力提出了严峻考验。

#### **结论**
综上所述，在2022至2025年间，基于相关性分析的多标签分类方法取得了显著进展。研究范式已从经典的典型相关分析扩展到包含矩阵分解、偏最小二乘法在内的更广泛的子空间学习技术。研究重点从简单地最大化相关性，转向将标签监督信息、结构先验和正则化约束融入模型，以学习更具判别力、鲁棒性和可解释性的特征表示。展望未来，将这些相关性分析技术与深度学习、图神经网络以及联邦学习等新兴范式进行深度融合，将是推动该领域发展的核心驱动力，也是应对极限分类和数据异构性等挑战的关键路径。

#### **参考文献**

[1] 赵前进, 平昕瑞, 苏树智, 等. 标签敏感的多重集正交相关特征融合方法[J]. 电子与信息学报, 2022, 44(10): 3458-3464. [[jeit.ac.cn](https://www.jeit.ac.cn/cn/article/doi/10.11999/JEIT210323?viewType=HTML)]

[2] 田小瑜, 秦永彬, 黄瑞章, 等. 基于相关性约束矩阵分解的多标签分类方法[J]. 南京大学学报(自然科学), 2023, 59(1): 76-84. [[jns.nju.edu.cn](https://jns.nju.edu.cn/article/2023/0469-5097/0469-5097-2023-59-1-76.shtml)]

[3] 苏可政, 肖燕珊, 刘波. 基于实例的多视角多标签学习算法[J]. 计算机科学与应用, 2022, 12(04): 785-796. [[image.hanspub.org](https://image.hanspub.org/Html/3-1542472_49979.htm)]

[4] 武子轩, 王烨, 于洪. 基于多尺度特征提取的层次多标签文本分类方法[J]. 郑州大学学报(理学版), 2025, 57(2): 24-30. [[html.rhhz.net](https://html.rhhz.net/ZZDXXBLXB/html/20250204.htm)]

[5] 石琇赟, 李顺勇, 韩翔. 基于多头图注意力网络与图模型的多标签图像分类[J]. 计算机系统应用, 2023, 32(6): 286-292. [[www.c-s-a.org.cn](https://www.c-s-a.org.cn/html/2023/6/9148.html)]

[6] 钟磊, 曾璐琨, 姜雪娇, 等. 基于标签相关性加权嵌入的联邦双阶段注意力神经网络算法研究[J]. 计算机科学与应用, 2025, 15(9): 267-282. [[pdf.hanspub.org](https://pdf.hanspub.org/csa_1543735.pdf)]

[7] Zhang M L, Zhou Z H. A review on multi-label learning algorithms[J]. IEEE Transactions on Knowledge and Data Engineering, 2014, 26(8): 1819-1837.

[8] Feng L, Huang J, Shu S L, et al. Regularized matrix factorization for multilabel learning with missing labels[J]. IEEE Transactions on Cybernetics, 2022, 52(5): 3710-3721.

[9] Zhu Y, Kwok J T, Zhou Z H. Multi-label learning with global and local label correlation[J]. IEEE Transactions on Knowledge and Data Engineering, 2018, 30(6): 1081-1094.

[10] Liu H, Li X, Zhang S. Learning instance correlation functions for multilabel classification[J]. IEEE Transactions on Cybernetics, 2016, 47(2): 499-510.

[11] Nielsen A A. Multiset canonical correlations analysis and multispectral, truly multitemporal remote sensing data[J]. IEEE Transactions on Image Processing, 2002, 11(3): 293–305.

[12] Chen J, Wang G, Giannakis G B. Graph multiview canonical correlation analysis[J]. IEEE Transactions on Signal Processing, 2019, 67(11): 2826–2838.