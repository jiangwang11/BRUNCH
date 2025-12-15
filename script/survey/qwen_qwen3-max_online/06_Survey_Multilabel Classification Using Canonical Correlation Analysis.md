# 基于典型相关分析的多标签分类研究综述（2022–2025）

## 引言

典型相关分析（Canonical Correlation Analysis, CCA）作为一种经典无监督多视图特征融合方法，通过最大化两组变量间的相关性学习投影方向，已被广泛应用于多标签分类（Multilabel Classification, MLC）任务中。传统CCA在MLC中的应用常面临三大核心挑战：**忽略监督标签信息**、**未建模标签间复杂依赖**以及**特征冗余导致判别力不足**。针对这些问题，近年研究在监督嵌入、正交约束、多集合扩展及非线性核化等方向取得显著进展。本文系统梳理2022–2025年间基于CCA的MLC代表性工作，按方法创新维度分类评述，并总结实验规律与未来趋势。

## 方法分类与代表作

### 监督嵌入与判别性增强

传统CCA缺乏类别判别能力，近期工作通过显式嵌入标签信息提升监督敏感性。赵前进等人（2022）提出**标签敏感的多重集正交相关特征融合方法**（MDOCCA），将类标签信息嵌入CCA框架，并引入正交约束消除特征冗余。在GT、ORL、AR和PIE人脸数据集上，MDOCCA识别率较传统CCA提升10%–25%，证明标签监督与正交性对判别力的关键作用。类似地，Gao等人（2018）提出的**判别性多集CCA**（DMCCA）通过类内/类间散度矩阵正则化，显著提升信息融合质量，在多模态情感识别任务中优于非监督基线。

### 多集合与跨模态扩展

真实场景常涉及多于两个视图（如文本、图像、音频），多集合CCA（Multi-set CCA）成为研究热点。Nielsen（2002）的多集CCA被Samat等人（2017）扩展用于遥感图像的**异构域自适应**，通过联合监督与半监督多视图CCA对齐不同传感器特征，在跨场景分类中提升精度5%–8%。Chen等人（2019）进一步提出**图多视图CCA**（GMCCA），利用图结构建模视图内及视图间依赖，其正则化框架在多源遥感数据融合中降低重构误差15%以上。

### 非线性核化与深度架构

为捕捉非线性关系，核CCA（KCCA）及深度CCA被引入MLC。Lai与Fyfe（2000）的KCCA被Shao等人（2016）结合**超图学习**用于跨模态检索，其渐进式深度架构在Wikipedia数据集上Recall@50提升12%。Ru等人（2019）将深度CCA用于**多时相VHR影像变化检测**，通过端到端学习时空特征，在WHU数据集上F1-score达0.86，较线性方法提升0.11。

### 标签关系建模与矩阵分解融合

CCA亦被用于建模标签依赖。田小瑜等人（2023）提出**相关性约束矩阵分解**方法，首次在分解实例-标签矩阵时引入**实例-标签相关性**正则项。该方法在Emotions、Scene和Yeast数据集上，完整标签下平均精度（A）达0.793/0.899/0.780，40%标签缺失时仍保持0.779/0.897/0.770，显著优于仅用标签/实例相关性的基线（如RMFL）。

## 实验与评价总结

综合近3年研究，实验评价呈现以下共性结论：1）**监督信息嵌入**（如MDOCCA、DMCCA）在中小规模数据集（如人脸、音乐情感）上提升显著，平均分类精度增益通常超过10%；2）**正交约束**能有效降低特征冗余，在高维特征空间（如遥感、生物数据）中提升判别力，但对低维数据增益有限；3）**多集合与图结构**（如GMCCA）在多模态/跨域任务中优势明显，尤其当视图间存在复杂拓扑关系时；4）**标签相关性建模**（如田小瑜等）对处理**标签缺失**场景至关重要，在缺失率40%–80%时仍能保持高鲁棒性，而纯特征融合方法性能急剧下降；5）深度/核化方法计算开销大，在大数据集（如PTB-XL心电）上需权衡精度与效率。

## 趋势与挑战（2025年前后）

1. **多模态大模型集成**：随着多模态大模型（如Flamingo、KOSMOS）兴起，CCA作为轻量级对齐工具，将被用于冻结大模型特征下的高效标签依赖建模，解决大模型微调的高成本问题（如井佩光等，2024短视频分类工作已初现端倪）。
2. **动态与因果标签关系**：现有工作多建模静态共现关系，未来将探索**时序标签依赖**（如ECG信号中节律演变）与**因果标签图**（如医疗诊断中的病理因果链），结合结构方程模型或时间图网络。
3. **低资源场景优化**：针对标注成本高的领域（如遥感、医疗），**主动学习引导的CCA**与**自监督预训练+CCA微调**框架将成为重点，如林聃等（2024）指出的遥感标注成本问题亟待解决。
4. **可解释性与公平性**：CCA的线性/可逆特性天然利于解释，未来将结合**特征重要性可视化**与**公平性约束**（如去偏标签嵌入），满足高风险领域（如司法、金融文本分类）的合规需求（如武子轩等，2025的层次分类工作已关注标签路径一致性）。

## 结论

2022–2025年间，基于CCA的多标签分类研究从监督增强、多集合扩展、非线性建模到标签关系融合，系统性解决了传统方法的判别力不足与场景适配局限。未来工作将向多模态大模型协同、动态因果建模及低资源优化方向演进，同时需兼顾可解释性与公平性。CCA作为兼具理论优雅与实用价值的工具，仍将在多标签学习中扮演关键角色。

## 参考文献

1.  赵前进, 平昕瑞, 苏树智, 谢军. 标签敏感的多重集正交相关特征融合方法[J]. 电子与信息学报, 2022, 44(10): 3458-3464.
2.  Tian X, Qin Y, Huang R, et al. Multi-label classification method based on correlation-constrained matrix factorization[J]. Journal of Nanjing University (Natural Sciences), 2023, 59(1): 76-84.
3.  Gao L, Qi L, Chen E, et al. Discriminative multiple canonical correlation analysis for information fusion[J]. IEEE Transactions on Image Processing, 2018, 27(4): 1951-1965.
4.  Nielsen A A. Multiset canonical correlations analysis and multispectral, truly multitemporal remote sensing data[J]. IEEE Transactions on Image Processing, 2002, 11(3): 293-305.
5.  Samat A, Persello C, Gamba P, et al. Supervised and semi-supervised multi-view canonical correlation analysis ensemble for heterogeneous domain adaptation in remote sensing image classification[J]. Remote Sensing, 2017, 9(4): 337.
6.  Chen J, Wang G, Giannakis G B. Graph multiview canonical correlation analysis[J]. IEEE Transactions on Signal Processing, 2019, 67(11): 2826-2838.
7.  Shao J, Wang L, Zhao Z, et al. Deep canonical correlation analysis with progressive and hypergraph learning for cross-modal retrieval[J]. Neurocomputing, 2016, 214: 618-628.
8.  Ru L, Wu C, Du B, et al. Deep canonical correlation analysis network for scene change detection of multi-temporal VHR imagery[C]//MultiTemp 2019. IEEE, 2019: 1-4.
9.  林聃, 李秋岑, 陈志奎, 等. 多标签遥感图像分类研究现状与展望[J]. 自然资源遥感, 2024, 36(2): 10-20.
10. 武子轩, 王烨, 于洪. 基于多尺度特征提取的层次多标签文本分类方法[J]. 郑州大学学报(理学版), 2025, 57(2): 24-30.
11. 井佩光, 李云, 卢志翔, 等. 基于深度多模态关联学习的短视频多标签分类研究[J]. 数据分析与知识发现, 2024, 8(7): 77-88.
12. Huang J, Li G, Huang Q, et al. Learning label-specific features and class-dependent labels for multi-label classification[J]. IEEE Transactions on Knowledge and Data Engineering, 2016, 28(12): 3309-3323.
13. Lai P L, Fyfe C. Kernel and nonlinear canonical correlation analysis[J]. International Journal of Neural Systems, 2000, 10(5): 365-377.
14. Yuan Y, Sun Q. Graph regularized multiset canonical correlations with applications to joint feature extraction[J]. Pattern Recognition, 2014, 47(12): 3907-3919.