## 基于典型相关性分析的多标签分类综述

### 引言

多标签分类（Multi-label Classification, MLC）是机器学习领域的一个重要研究方向，其任务是将每个实例与多个预定义标签相关联。与单标签分类不同，MLC 更符合现实世界中数据固有的复杂性，例如一篇文章可能同时涉及“政治”和“经济”多个主题，一幅图像可能包含“人”、“动物”和“天空”等多个对象。近年来，随着数据量的爆炸式增长和应用场景的不断拓展，MLC 在场景分类、信息检索、文本挖掘、生物信息学等领域展现出广阔的应用前景 [jns.nju.edu.cn](https://jns.nju.edu.cn/article/2023/0469-5097/0469-5097-2023-59-1-76.shtml)。

MLC 的核心挑战之一在于捕捉和利用标签之间以及实例与标签之间的复杂相关性。标签之间往往不是独立同分布的，而是存在共现、互斥或层次结构等关系 [jos.org.cn](https://jos.org.cn/html/2023/12/6802.htm)。同时，实例的原始特征通常维度较高且包含冗余信息，如何有效降维并提取与标签关联度高的判别性特征也至关重要。典型相关性分析（Canonical Correlation Analysis, CCA）作为一种多元统计方法，旨在通过寻找两组变量之间的最大线性相关性来揭示它们之间的潜在联系。其能够将高维数据投影到低维空间，同时最大化不同特征集之间的相关性 [pdf.hanspub.org](https://pdf.hanspub.org/csa20220400000_27660951.pdf)。CCA 在处理多变量之间的复杂关系方面具有天然优势，为 MLC 任务中特征与标签相关性的建模提供了有效的途径。

本综述将重点关注 2022 年至 2025 年间，利用 CCA 或其变体、以及其他强调相关性建模的深度学习和矩阵分解方法在多标签分类领域取得的代表性进展。

### 方法分类与代表作

近期关于多标签分类的研究主要围绕如何更有效地捕捉和利用数据中内在的多种相关性展开，包括标签间相关性、实例间相关性、实例与标签间相关性以及多视角数据的一致性和互补性。

#### 1. 基于典型相关性分析及其扩展的传统方法

这类方法直接或间接借鉴 CCA 的思想，通过最大化不同特征空间或特征与标签空间之间的相关性来优化多标签分类性能。

- **基于实例相关性的多视角多标签学习算法 (2022)** [image.hanspub.org](https://image.hanspub.org/Html/3-1542472_49979.htm), [pdf.hanspub.org](https://pdf.hanspub.org/csa20220400000_27660951.pdf)
    - **研究问题**: 现有多视角多标签学习算法关注变量与类标签间的关系，但往往忽略了训练实例和测试实例之间的关系，且无法有效整合多视角数据的一致性和互补信息。
    - **核心方法**: 提出一种基于实例的偏最小二乘 (PLS) 回归方法，探索训练实例和测试实例的相关性，而不是传统的变量-标签映射。通过构建多个 PLS 回归模型来处理多视角数据，并引入视角一致性约束来确保不同视角之间的一致性。模型被转化为 LASSO 问题并通过 NIPALS 求解。
    - **关键实验结论**: 在 mirickr、pascal07 等多个多视角多标签数据集上的实验显示，该算法的 Hamming Loss、Ranking Loss、One Error 较低，而 Average Precision 较高，性能优于对比的单视角和多视角算法，尤其在处理多视角数据时，协同利用不同视角的互补信息显著提升了分类性能。

#### 2. 深度学习中利用相关性建模的方法

随着深度学习的兴起，研究者们将相关性建模融入深层神经网络结构，以增强模型的特征表示能力和标签推理能力。

- **多粒度信息关系增强的多标签文本分类 (MIRE) (2023)** [jos.org.cn](https://jos.org.cn/html/2023/12/6802.htm)
    - **研究问题**: 基于深度学习的多标签文本分类方法存在两个主要缺陷：缺乏对文本信息多粒度的学习，以及对标签间约束性关系的有效利用。粗粒度学习可能忽略局部关键信息，而细粒度学习可能忽视全局上下文。
    - **核心方法**: 提出了 MIRE 模型，该模型首先通过文本-标签联合嵌入和 BERT 预训练模型获取文本和标签的隐向量特征表示。在此基础上，构建了三个模块：文档级信息浅层标签注意力分类模块（DISLA）、词级信息深层标签注意力分类模块（WIDLA）和标签约束性关系匹配辅助模块（LCRM）。DISLA 和 WIDLA 从不同粒度学习文本与标签的相互关系，LCRM 通过稀疏重构得到标记相关性矩阵，显式地学习标签间的约束性关系以辅助分类。
    - **关键实验结论**: 在 AAPD、LAIC-争议焦点识别提取和医疗公共健康问句数据集上的实验表明，MIRE 在 Micro-_F_1、Macro-_F_1、nDCG@k 和 P@k 等主要指标上均达到最佳效果。消融实验验证了文本-标签联合嵌入和 LCRM 模块对提升模型性能的有效性，尤其在标签数量较多时 LCRM 的提升更为显著。

- **基于多头图注意力网络与图模型的多标签图像分类 (ML-M-GAT) (2023)** [www.c-s-a.org.cn](https://www.c-s-a.org.cn/html/2023/6/9148.html)
    - **研究问题**: 现有模型在多标签图像分类中往往只学习图像的视觉表示特征，忽略了图像标签之间的相关信息以及标签语义与图像特征的对应关系。
    - **核心方法**: 提出 ML-M-GAT 模型，利用标签共现关系和标签属性信息构建图模型。使用多头图注意力机制学习标签之间不对称相关关系的注意力权重。随后，将学习到的标签权重与图像视觉特征（通过 ResNet101 提取并降维）进行融合，以将标签相关性和标签语义信息融入分类模型。最终通过全连接层进行分类。
    - **关键实验结论**: 在 VOC-2007 和 COCO-2014 数据集上的实验结果表明，ML-M-GAT 在 mAP、CP、OP、CR 等指标上优于 CNN-RNN、ResNet101 等基线模型，mAP 相较 ResNet101 提升了 3.9%~4.2%，证明了利用标签信息能有效提高多标签图像分类性能。

- **基于弱监督对比学习的弱多标记特征选择 (2023)** [jns.nju.edu.cn](https://jns.nju.edu.cn/CN/10.13232/j.cnki.jnju.2023.01.009)
    - **研究问题**: 在弱多标签学习（即标签仅部分可知）中，高维特征的选择对于提高分类性能至关重要，但传统的特征选择方法难以在弱监督环境下有效处理标签缺失情况并捕获特征与标签的深层相关性。
    - **核心方法**: 提出一种基于弱监督对比学习的特征选择方法。利用对比学习构建正负样本对，通过最大化同标签样本之间的相似性，同时最小化异标签样本之间的相似性来学习更具判别性的特征表示。在标签缺失的情况下，利用现有标签信息进行弱监督信号传播，以推断缺失标签，从而指导特征选择过程。
    - **关键实验结论**: 在多个弱多标签数据集上进行的实验表明，该方法能够有效选择出更有判别力的特征子集，显著提高了在标签缺失情况下的分类准确率和其他性能指标。

#### 3. 矩阵分解与协同学习方法

矩阵分解是一类常用的无监督或半监督学习方法，通过将高维矩阵分解为低维潜在因子来发现数据中的隐式结构。近年来，研究者们将其与相关性约束相结合，处理多标签分类问题。

- **基于相关性约束矩阵分解的多标签分类方法 (2023)** [jns.nju.edu.cn](https://jns.nju.edu.cn/article/2023/0469-5097/0469-5097-2023-59-1-76.shtml)
    - **研究问题**: 现有基于矩阵分解的多标签分类方法在解决标签缺失问题时，通常只考虑标签相关性和实例相关性，而忽略了潜在标签表示与实例特征表示之间的深层关联。
    - **核心方法**: 提出一种在矩阵分解框架下，综合利用标签相关性、实例相关性以及首次引入的实例与标签相关性来约束潜在实例和标签特征表示的方法。通过将潜在标签表示与实例表示的内积作为它们的线性表示权重，并用该权重与潜在标签表示的加权和重构实例表示，以优化分解出的潜在特征。
    - **关键实验结论**: 在 Emotions、Scene 和 Yeast 三个真实数据集上的实验表明，该算法在标签完整及不同程度标签缺失（40%、60%、80%）的情况下，均在汉明损失、1-错误率、覆盖范围、排序损失和平均精度等指标上取得了最高的预测精度。消融实验证实了实例与标签特征描述相关性约束对提升算法性能的重要性。

- **考虑标记间协作的标记分布学习 (LDLCL) (2022)** [jos.org.cn](https://jos.org.cn/html/2022/2/6139.htm)
    - **研究问题**: 现有标记分布学习（Label Distribution Learning, LDL）方法在处理标记多义性时，通常将标记相关性作为先验知识且仅在训练阶段利用，而未在最终预测中显式利用标记间的协作关系。
    - **核心方法**: 提出 LDLCL 方法，其核心假设是每个标记的最终预测涉及到它自身的预测和其他标记预测之间的协作。通过标记空间中的稀疏重构学习标记相关性矩阵，并将其无缝集成到模型训练和预测中，实现标记间的显式协作。引入标记独立嵌入作为潜在的标记分布空间，并利用核函数处理非线性特征映射。
    - **关键实验结论**: 在 Yeast_xx 系列、Natural Scene 等 14 个广泛使用的 LDL 数据集上，LDLCL 在 Chebyshev 距离、Clark 距离、Canberra 距离、Kullback-Leibler 散度、余弦相关系数和交叉相似度等 6 种评价指标上持续优于 PT-SVM、AA-BP、LDLLC 等基线和近期算法，证明了显式利用标记间协作对 LDL 性能的提升作用。

- **ZLPR: 多标签分类的新损失 (2022)** [www.zhuanzhi.ai](https://www.zhuanzhi.ai/paper/fd09515cfd452cf42c63785c933fec66)
    - **研究问题**: 深度学习背景下的多标签分类（MLC）损失函数难以同时处理目标标签数量不确定、标签间相关性建模和计算复杂性等问题。
    - **核心方法**: 提出 ZLPR (zero-bounded log-sum-exp & pairwise rank-based) 损失函数。该损失函数旨在处理目标标签数量不确定性，同时考虑标签间的相关性。其预测是标签独立的，在计算复杂度上可与二元相关性 (BR) 方法竞争，且优于标签幂集 (LP) 方法。此外，还提出了 ZLPR 的软版本及其对应的 KL 散度计算方法，以支持标签平滑等正则化技巧。
    - **关键实验结论**: 在多个基准数据集和多种评价指标上的实验表明 ZLPR 损失函数的有效性。该损失函数在捕捉标签相关性方面超越了 BR 方法，并在计算效率上压倒了 LP 方法。

### 实验与评价总结

上述研究普遍采用了多元评估指标来全面衡量多标签分类模型的性能。常用的指标包括：
1. **基于排名的指标**: 如 Ranking Loss (RL)、One Error (OE)、Precision@k (P@k)、nDCG@k，这类指标关注预测标签的排序质量。
2. **基于实例的指标**: 如 Hamming Loss (HL)、Accuracy、Specificity，着眼于单个实例的标签预测准确性。
3. **基于标签的（宏观/微观）指标**: 如 Micro-F1 (MF1)、Macro-F1 (MaF1)、Micro-Precision (MP)、Macro-Precision (MaP)、Micro-Recall (MR)、Macro-Recall (MaR)，这类指标从不同粒度反映模型在所有标签上的整体性能。
4. **针对特定任务的指标**: 例如在标记分布学习中，还会使用 Chebyshev 距离、Clark 距离、Canberra 距离、Kullback-Leibler 散度、余弦相关系数和交叉相似度等度量预测分布与真实分布的相似性。

综合来看，这些方法在各类数据集上均表现出显著的性能提升。CCA 及其变体，以及强调多粒度、多层次相关性建模的深度学习和矩阵分解模型，通过显式或隐式地捕捉标签间、实例间及特征-标签间的多重相关性，有效提升了多标签分类的准确性和鲁棒性。消融实验普遍验证了所提相关性建模模块的有效性，证明了不同类型相关性（如全局与局部标签相关性、实例与标签相关性、多视角一致性）对模型性能的积极贡献。特别是在处理标签缺失、数据长尾或多视角数据等复杂场景下，这些方法的优势更为明显。

### 趋势与挑战

展望 2025 年及以后，多标签分类领域将呈现以下研究趋势和挑战：

1. **更精细化的多模态与多粒度相关性融合**: 随着多模态数据（文本、图像、语音等）的日益普及，如何将来自不同模态、不同粒度的信息进行有效融合，并捕捉它们之间复杂而深层的相关性，将是重要研究方向。例如，图像-文本联合表示中，不仅要考虑视觉概念与文本关键词的粗粒度对应，还要挖掘视觉区域与文本描述的细粒度关联。
2. **层次化、结构化标签体系的深度利用**: 现实世界中许多标签具有天然的层次结构（如生物分类、领域知识图谱）。如何将这种层次结构信息深度融入多标签分类模型，例如通过图神经网络结合标签层次关系进行推理，从而实现更精准、更符合逻辑的预测，将是未来的发展重点。此外，如何在标签稀疏或标签缺失的层次化数据中进行有效学习也是一大挑战 [html.rhhz.net](https://html.rhhz.net/ZZDXXBLXB/html/20250204.htm)。
3. **结合因果推断提升模型可解释性与鲁棒性**: 现有相关性建模多停留在统计层面，难以区分相关性与因果性。未来的研究可能会探索将因果推断机制引入多标签分类，以识别标签之间真正的因果关系，从而提高模型在非独立同分布（Out-of-Distribution, OOD）数据上的泛化能力和可靠性。这将有助于模型更深刻地理解标签间的内在逻辑，而非仅仅依赖表面共现规则。

### 结论

多标签分类作为一个活跃且充满挑战的领域，近年来在相关性建模方面取得了显著进步。无论是基于 CCA 思想的传统方法、融入深度学习框架的多粒度注意力机制和图模型，还是结合相关性约束的矩阵分解和协作学习，都表明了有效利用数据中蕴含的各种相关性是提升 MLC 性能的关键。未来的研究将持续聚焦于如何更全面、更深入地挖掘和融合多模态、多粒度、层次化以及因果层面的相关信息，以应对现实世界中日益复杂的多标签分类任务挑战。

### 参考文献

- [jos.org.cn](https://jos.org.cn/html/2023/12/6802.htm) MAO Xing-Liang, LI Fang-Fang, SU Pu-Zhen, et al. Multi-label Text Classification with Enhancing Multi-granularity Information Relations [J]. Journal of Software, 2023, 34(12): 5686-5703.
- [html.rhhz.net](https://html.rhhz.net/ZZDXXBLXB/html/20250204.htm) WU Zixuan, WANG Ye, YU Hong. Hierarchical Multi-label Text Classification Method Based on Multi-scale Feature Extraction [J]. Journal of Zhengzhou University (Natural Science Edition), 2025, 57(2): 24-30.
- [jns.nju.edu.cn](https://jns.nju.edu.cn/article/2023/0469-5097/0469-5097-2023-59-1-76.shtml) TIAN Xiaoyu, QIN Yongbin, HUANG Ruizhang, et al. Multi-label classification method based on correlation-constrained matrix factorization [J]. Journal of Nanjing University (Natural Sciences), 2023, 59(1): 76-84.
- [image.hanspub.org](https://image.hanspub.org/Html/3-1542472_49979.htm) SU Kezheng, XIAO Yanshan, LIU Bo. Multi-View Multi-Label Learning by Exploiting Instance Correlations [J]. Computer Science and Application, 2022, 12(04): 785-796.
- [pdf.hanspub.org](https://pdf.hanspub.org/csa20220400000_27660951.pdf) SU Kezheng, XIAO Yanshan, LIU Bo. Based on Instance Multi-View Multi-Label Learning Algorithm [J]. Computer Science and Application, 2022, 12(4): 785-796.
- [manu44.magtech.com.cn](https://manu44.magtech.com.cn/Jwk_infotech_wk3/CN/abstract/abstract5639.shtml) LIU Kan, YOU Meilin, WEI Lanxi. Label Distribution Learning Based on Hierarchical Tag Structure [J]. Data Analysis and Knowledge Discovery, 2024, 8(2): 44-55.
- [www.c-s-a.org.cn](https://www.c-s-a.org.cn/html/2023/6/9148.html) SHI Xiuyun, LI Shun-Yong, HAN Xiang. Multi-label Image Classification Based on Multi-head Graph Attention Network and Graph Model [J]. Computer Systems and Applications, 2023, 32(6): 286-292.
- [jos.org.cn](https://jos.org.cn/html/2022/2/6139.htm) LI Rui-Yu, ZHU Ji-Hua, LIU Xin-Yuan. Label Distribution Learning with Collaboration among Labels [J]. Journal of Software, 2022, 33(2): 539-554.
- [www.zhuanzhi.ai](https://www.zhuanzhi.ai/paper/fd09515cfd452cf42c63785c933fec66) SU Jianlin, ZHU Mingren, MURTADHA Ahmed, et al. ZLPR: A Novel Loss for Multi-label Classification [J/OL]. arXiv preprint arXiv:2208.02955, 2022.
- [jns.nju.edu.cn](https://jns.nju.edu.cn/CN/10.13232/j.cnki.jnju.2023.01.009) WANG Jin, TAN Anhui, GU Shenming. Weak multi-label feature selection based on weakly-supervised contrastive learning [J]. Journal of Nanjing University (Natural Sciences), 2023, 59(1): 85-97.
- [journals.sagepub.com](https://journals.sagepub.com/doi/pdf/10.1177/02783649231206161) HUANG, Z.; CHEN, K.; DUAN, J. Enhancing Multi-granularity Features for Multi-Label Text Classification with Explicit and Implicit Label Relation Modeling. *International Journal of Advanced Robotic Systems*, 2023, 1–11.
- [www.mdpi.com](https://www.mdpi.com/1424-8220/22/23/9103) XU, P.; CHEN, X.; LI, J.; ZOU, H. Hierarchical Multi-Label Text Classification with Label-Specific Attention and Gated Fusion. *Sensors*, 2022, 22(23), 9103.