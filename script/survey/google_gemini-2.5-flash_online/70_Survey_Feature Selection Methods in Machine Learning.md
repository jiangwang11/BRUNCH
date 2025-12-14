## 机器学习特征选择方法综述（2022-2025）

### 引言

随着数据复杂性的日益增加，机器学习模型在处理高维数据时面临着维度灾难、模型过拟合、计算成本增加以及可解释性下降等诸多挑战。特征选择（Feature Selection, FS）作为一种重要的预处理技术，旨在从原始特征集中识别出最具信息量、最相关且冗余度最小的特征子集，以期提升模型性能、降低计算复杂度并增强模型的可解释性。本综述将聚焦2022年至2025年间机器学习特征选择领域的前沿进展，系统梳理不同类别的特征选择方法及其代表性工作、关键实验发现，并对未来研究趋势进行展望。

### 方法分类与代表作

根据特征选择与机器学习模型的交互方式，可将其划分为过滤式（Filter）、包裹式（Wrapper）和嵌入式（Embedded）方法。近年来，随着深度学习尤其是图神经网络（Graph Neural Networks, GNNs）和大型语言模型（Large Language Models, LLMs）的兴起，以及高维小样本数据在生物医药等领域的广泛应用，涌现出结合这些先进技术的新型特征选择策略。

#### 1. 过滤式方法 (Filter Methods)

过滤式方法独立于任何学习算法，通过评估特征本身的统计学特性来选择特征子集，计算效率高且通用性强。

*   **Correlation-based Feature Selection (CFS) 及其改进**
    传统的CFS方法侧重于特征与标签的相关性以及特征之间的冗余性。在面对超高维数据时，简单相关系数如Pearson往往难以捕捉复杂的非线性关系 [blog.csdn.net](https://blog.csdn.net/fjsd155/article/details/93754257)。**SIS (Sure Independence Screening)** 及其变体，如Qa-SIS，在处理超高维问题方面展现出优势，通过筛选与响应变量相关性强的特征，实现高效的初步降维，甚至能够处理非线性关系和异方差问题 [blog.csdn.net](https://blog.csdn.net/fjsd155/article/details/93754257)。

#### 2. 包裹式方法 (Wrapper Methods)

包裹式方法将学习算法作为特征选择的评估指标，通过反复训练和测试模型来选择最佳特征子集，通常能获得更好的模型性能，但计算成本较高。

*   **基于启发式搜索的子集选择**
    **最优子集选择 (Best Subset Selection)** 旨在通过穷举所有特征组合来找到全局最优解，但计算复杂度随特征数量呈指数级增长，不适用于高维数据 [blog.csdn.net](https://blog.csdn.net/fjsd155/article/details/93754257)。**逐步筛选法 (Stepwise Selection)**，包括向前逐步回归和向后逐步回归，通过贪心策略在每次迭代中添加或删除特征，以在计算效率和性能之间取得平衡，但可能陷入局部最优 [blog.csdn.net](https://blog.csdn.net/fjsd155/article/details/93754257)。为应对超高维数据，**原始对偶激活集算法 (Primal Dual Active Set, PDAS)** 被提出，它通过引入激活集和批量迭代更新$\beta$系数，能有效处理万维级别的数据，实现最优子集选择的效果 [blog.csdn.net](https://blog.csdn.net/fjsd155/article/details/93754257)。

#### 3. 嵌入式方法 (Embedded Methods)

嵌入式方法将特征选择过程融入模型训练中，通过正则化等方式惩罚不重要特征的权重，实现特征选择与模型训练的同步进行。

*   **基于正则化的深度学习网络**
    传统的正则化方法，如L1正则化，在深度学习中用于强制模型权重稀疏。然而，高维小样本数据下的过拟合问题依然严峻 [html.rhhz.net](https://html.rhhz.net/tis/html/202402018.htm)。**稀疏重构网络 (SRnet)** [html.rhhz.net](https://html.rhhz.net/tis/html/202402018.htm) 针对高维小样本特征选择，提出了一种端到端的超网络设计。该模型通过稀疏增强和奇异值嵌入对特征进行预处理，随后利用并行辅助网络训练嵌入矩阵重构预测权重，实现了参数削减的超网络学习方式。该方法有效降低了无效参数对网络的影响，并在生物医学领域的12种高维小样本数据集上，将分类准确率平均提升3.26个百分点。其消融实验也证实了分解层、重构层、关联层在提升性能中的作用，并通过稀有增强算法和奇异值分解嵌入等机制，增强了模型对独立特征的选择能力和特征信息嵌入的合理性。

*   **基于树模型的特征重要性评估**
    **Random Forest** 模型通过计算Gini指数来评估特征重要性，进而进行特征筛选 [blog.csdn.net](https://blog.csdn.net/fjsd155/article/details/93754257)。**XGBoost** 作为GBDT的高效实现，在逐步拟合残差的过程中，自然地实现了变量选择 [blog.csdn.net](https://blog.csdn.net/fjsd155/article/details/93754257)。这些基于树的方法在处理非线性关系方面表现出色，且对数据分布没有严格假设。

*   **基于流形正则化的无监督特征选择**
    在无监督场景下，特征选择通常需要更巧妙地捕捉数据内在结构。**基于伪标签回归和流形正则化的无监督特征选择算法** [jns.nju.edu.cn](https://jns.nju.edu.cn/CN/10.13232/j.cnki.jnju.2023.02.009) 提出利用伪标签回归学习每个特征的权重，并通过流形正则化保持数据的局部几何结构，从而在无标签数据中发现有判别力的特征。该方法在多个实际数据集上展示了其在无监督特征选择任务上的有效性，通过结合数据本身的内在结构信息，提升了特征子集的区分度。

#### 4. 超网络架构 (Hypernetwork Architecture)

超网络（Hypernetwork）通过一个网络为另一个网络生成权重，显著减少了主网络的自由参数数量，从而提高泛化能力，尤其适用于小样本高维数据 [html.rhhz.net](https://html.rhhz.net/tis/html/202402018.htm)。

*   **DietNet及其扩展**
    **DietNet** [html.rhhz.net](https://html.rhhz.net/tis/html/202402018.htm) 是最早将超网络概念应用于小样本高维特征选择的模型之一，它包含一个主网络和两个辅助网络，用于预测和重构主网络的参数，以减少参数数量并增强泛化能力。然而，该模型在迭代过程中仍存在较高的方差和梯度问题。**Weight Predictor Network (WPN)** [html.rhhz.net](https://html.rhhz.net/tis/html/202402018.htm) 扩展了DietNet，利用非负矩阵分解（NMF）嵌入特征并进一步减少权重参数，在连续特征值数据集上取得了良好效果。**SRnet** [html.rhhz.net](https://html.rhhz.net/tis/html/202402018.htm) 在此基础上进行了优化，通过奇异值分解嵌入特征并细化网络结构，进一步提升了在高维小样本数据上的性能，分类准确率平均提升3.26百分点。

### 实验与评价总结

近年来的研究表明，在处理高维小样本数据时，参数较少、正则化良好的模型往往优于复杂的网络架构。

1.  **性能提升与泛化能力**：超网络和正则化机制在减少模型参数、降低过拟合风险方面表现出显著优势。例如，SRnet在生物医学数据集上的分类准确率平均提升了3.26个百分点 [html.rhhz.net](https://html.rhhz.net/tis/html/202402018.htm)，这表明通过优化网络结构和参数生成机制，可以有效提升模型在有限数据下的泛化能力。
2.  **特征嵌入的重要性**：特征嵌入方法对特征选择模型的性能具有关键影响。奇异值分解（SVD）嵌入和非负矩阵分解（NMF）等技术在连续型数据上表现出优于随机投影和点直方图嵌入的效果 [html.rhhz.net](https://html.rhhz.net/tis/html/202402018.htm)。通过捕捉特征的潜在结构和信息，这些嵌入方法能够为后续的特征选择提供更具信息量的输入。
3.  **对噪声和冗余的鲁棒性**：专为高维小样本设计的特征选择方法，如SRnet，能够有效降低无效参数的影响，通过稀疏重构和稀有增强算法，探索特征组合的潜在相关性，并对冗余特征赋予更低的权重，从而减少噪声对模型决策的干扰 [html.rhhz.net](https://html.rhhz.net/tis/html/202402018.htm)。
4.  **模型复杂度与可解释性**：在小样本高维数据背景下，平衡模型的复杂度和泛化能力是关键。虽然一些方法通过降低参数数量来缓解过拟合，但模型内部机制的透明度仍是一个挑战。例如，基于树模型的方法通常具有较好的可解释性，而深度学习方法则可能需要额外的解释性工具。

### 趋势与挑战

1.  **GNNs与FS的深度融合**：随着图神经网络在处理复杂关系数据方面的强大能力，未来趋势将是更深入地探索GNNs在特征选择中的应用，尤其是在具有内在图结构的数据（如社交网络、生物网络和知识图谱）或通过构建图来捕获特征之间复杂依赖关系的数据上。挑战在于如何设计能够同时建模特征间关系和特征与标签间关系的 GNN 架构，以及如何在GNN训练过程中有效集成特征稀疏化机制。

2.  **LLMs赋能特征选择**：大型语言模型在文本理解和生成方面的突破，预示着它们将在涉及文本或利用文本增强的特征选择场景中发挥关键作用。未来研究可能探索利用LLMs的语义理解能力来识别和提取文本特征的重要性，例如，通过分析特征描述的语义相似性或使用LLMs生成伪标签来指导无监督/半监督特征选择。挑战在于如何将LLMs的高维表示有效整合到传统特征选择流程中，以及如何解决LLMs可能引入的偏见问题和算力消耗。

3.  **高维小样本下的鲁棒性与效率**：生物医学等领域对高维小样本数据的处理需求日益增长，这要求特征选择方法不仅要高效，还要对数据噪声具有高度鲁棒性，并能有效避免过拟合。未来的研究将继续探索轻量级、自适应的特征选择网络，例如结合更先进的正则化技术、蒸馏策略或元学习方法，以在极少量样本上取得稳定的特征选择效果。同时，如何在保持高性能的同时进一步降低计算和内存开销也是一个持续的挑战。

### 结论

特征选择作为机器学习领域的核心研究方向，在应对数据爆炸式增长和复杂模型应用挑战中扮演着不可或缺的角色。近年来，以超网络、GNNs和LLMs为代表的新型方法，为高维小样本等特定场景下的特征选择带来了显著突破。通过参数削减、结构化特征嵌入和智能权重重构，这些方法有效提升了模型的泛化能力和预测准确性。展望未来，特征选择将在与新兴AI技术的深度融合中持续发展，尤其是在解决鲁棒性与效率平衡、可解释性增强以及跨模态特征选择等方面，将迎来更多创新与突破。

### 参考文献

*   [html.rhhz.net](https://html.rhhz.net/tis/html/202402018.htm) 魏俊伊, 董红斌, 余紫康. 用于高维小样本特征选择的超网络设计[J]. 智能系统学报, 2025, 20(2): 465-474. doi: 10.11992/tis.202402018
*   [blog.csdn.net](https://blog.csdn.net/fjsd155/article/details/93754257) 高维数据中特征筛选方法的思考总结——多变量分析筛选法_逐步筛选法. CSDN博客. Published online April 29, 2025.
*   [jns.nju.edu.cn](https://jns.nju.edu.cn/CN/10.13232/j.cnki.jnju.2023.02.009) 宋雨, 肖玉柱, 宋学力. 基于伪标签回归和流形正则化的无监督特征选择算法[J]. 南京大学学报(自然科学版), 2023, 59(2): 263-272.
*   [manu44.magtech.com.cn](https://manu44.magtech.com.cn/Jwk_infotech_wk3/CN/10.11925/infotech.2096-3467.2022.0718) 严颖, 黄奇, 李娜. 基于优化后集成学习模型的特征选择与疾病高效预警研究——以老年抑郁焦虑为例[J]. 数据分析与知识发现, 2023, 7(7): 74-88.
*   [github.com](https://github.com/xiaoyuexing/StarrySky) xiaoyuexing. StarrySky: 精选了千余项目，包括机器学习、深度学习、NLP、GNN、推荐系统、生物医药、机器视觉等内容. Published June 14, 2023.
*   [www.jeit.ac.cn](https://www.jeit.ac.cn/cn/article/doi/10.11999/JEIT250567?viewType=HTML) 柏园超, 刘文昌, 江俊君, 刘贤明. 深度神经网络图像压缩方法进展综述[J]. 电子与信息学报. doi: 10.11999/JEIT250567
*   [www.cicpa.org.cn](https://www.cicpa.org.cn/ztzl1/zgzckjs/zazhi2024/202501/P020250121392638821483.pdf) 陈宋生, 邹正阳. 大语言模型在会计研究中的应用[J]. 中国注册会计师, 2024(12): 18-24.
*   [blog.51cto.com](https://blog.51cto.com/whaosoft/13977365) 斯坦福大学. Exploring Diffusion Transformer Designs via Grafting. Published June 12, 2025. arXiv: 2506.05340.
*   [arxiv.org](https://arxiv.org/abs/2502.09622) 北京大学, 蚂蚁集团. Theoretical Benefit and Limitation of Diffusion Language Model. arXiv:2502.09622. Published February 25, 2025.
*   [arxiv.org](https://arxiv.org/abs/2505.05474) S-Lab, 南洋理工大学. 3D Scene Generation: A Survey. arXiv:2505.05474. Published May 9, 2025.
*   [arxiv.org](https://arxiv.org/abs/2505.01288) Hu T, Zhang J, Yi R, et al. Improving Autoregressive Visual Generation with Cluster-Oriented Token Prediction[C]//Proceedings of the Computer Vision and Pattern Recognition Conference. 2025.
*   [arxiv.org](https://arxiv.org/abs/2506.01056) 厦门大学, 中国科学技术大学. MCP-Zero: Proactive Toolchain Construction for LLM Agents from Scratch. arXiv:2506.01056. Published June 2, 2025.
*   [arxiv.org](https://arxiv.org/abs/2506.05007) 中国科学院计算技术研究所, 中国科学院软件研究所. Automatic Design of Processor Chips: The启蒙System. arXiv:2506.05007. Published June 7, 2025.
*   [arxiv.org](https://arxiv.org/pdf/2505.13544) 剑桥大学机器智能实验室. Multi-head Temporal Latent Attention. arXiv:2505.13544. Published May 21, 2025.