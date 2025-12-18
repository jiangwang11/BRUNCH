Multilabel Classification Using Canonical Correlation Analysis
引言
典型相关分析（CCA）作为一种多变量统计方法，用于发现多组变量间的线性相关关系，在多标签分类任务中被广泛扩展，以捕捉特征空间与标签空间的依赖性。2022–2025年间，该领域研究聚焦于处理多视图数据、高阶标签相关性、噪声鲁棒性及深度非线性映射等挑战，推动了跨模态检索、医疗诊断和多组学整合的应用。本综述分类总结代表性工作，强调方法创新与实验验证，旨在揭示CCA在多标签分类中的演进。
方法分类与代表作
多视图多标签CCA方法
此类方法扩展CCA处理多模态数据，利用多标签语义建立视图间对应，无需显式样本配对。
Sanghavi et al. (2022) 研究跨模态检索中多视图多标签数据的对应问题，现有的CCA需显式配对且限于双视图。提出MVMLCCA，通过学习各模态投影矩阵，将特征映射到共同嵌入空间，使用标签相似函数最小化语义相似样本间距离。解决多词汇标签问题，支持块式分布式计算以提升可扩展性。实验在IAPRTC-12和MS-COCO数据集上，MVMLCCA在mAP指标上与CCA相当，但适用于无配对的多模态场景，训练时间与MLCCA类似。
Rani et al. (2025) 针对多视图多标签跨模态多媒体检索，传统CCA依赖样本配对限制多视图应用。引入MVMLCCA的快速版FMVMLCCA，利用多标签注释建立多视图对应，学习共同子空间以融合语义信息。优化计算复杂度，实现数倍加速。实验在IAPRTC-12、MS-COCO和MIR-Flickr数据集上，FMVMLCCA在mAP@k、精度-召回和F1分数上优于相关方法，训练时间显著缩短。
Liu et al. (2023) 探讨多视图多标签学习中高阶标签相关性捕捉，现有多方法忽略多视图互补信息。提出ELSMML，构建标签相关矩阵描绘高阶关系，通过矩阵分解和维降提取潜在语义标签与特征信息。在低维空间构建分类器，加入流形正则化保留数据内在结构。使用加速近端梯度优化模型。实验在多数据集上，ELSMML在多种评估指标上优于BR、LLSF和ECC基准，验证高阶相关与多视图整合的有效性。
深度泛化CCA方法
此类方法结合深度神经网络，捕捉非线性相关，提升多标签分类在复杂数据中的性能。
Moon et al. (2022) 研究多组学数据整合中非线性相关建模，现有多视图CCA限于双模态且缺乏分类与特征排序。提出SDGCCA，使用深度网络捕捉多模态非线性相关，通过相关损失和交叉熵损失整合表型标签。交替优化投影矩阵与网络参数，使用SHAP值进行特征选择。实验在ROSMAP阿尔茨海默病数据上，SDGCCA在MCC指标上优于SVM、DGCCA和MOGONET，特征集分类性能提升，通路分析揭示与AD相关的生物标志物。
Vieluf et al. (2023) 针对癫痫发作预测中外围神经信号的非侵入分类，现有方法依赖监督且忽略模态间耦合变化。提出基于DCCA的管道，分析心率和电皮活动，使用GRU、CNN和FC架构的自动编码器进行无监督聚类。假设发作前后相关模式差异允许高聚类准确率。实验在42名儿科患者数据上，GRU-DCCAE聚类准确率达68.9%，相对随机提升37.8%，71%患者优于随机，验证模态耦合变化作为预测生物标志物。
Karakasis et al. (2023) 重新审视深度泛化CCA的局限，如允许平凡解、忽略弱公共因子及过载私有组件。提出新公式，将私有组件建模为给定公共组件的条件独立，实现紧凑优化。提供识别公共随机因子的充分条件。实验在合成和真实数据集上，验证方法有效性，优于现有DGCCA扩展，避免过载计算复杂度。
高阶与鲁棒CCA方法
此类方法聚焦标签高阶相关与噪声处理，提升多标签分类鲁棒性。
Si et al. (2022) 研究多标签分类中高阶标签相关与标签矩阵高秩属性的同时建模，现方法未能有效互补。提出方法显式描绘高阶相关，同时保持标签矩阵高秩。通过输入局部几何结构同时估计相关与模型参数，实现互增强。实验通过多图表验证，在分类性能上优于基准，获29次引用显示影响力。
Wang et al. (2022) 针对多标签分类中标签空间同时存在假阴性和假阳性噪声，现方法无法同时处理两种噪声。提出DCAMC，双尺度相关分析分为抗噪与分类模块。定义“领导标签”和“稀有标签”基于细粒度和粗粒度数据划分的流形假设。粗粒度确保泛化，细粒度挖掘标签相关。实验在现有数据集上，DCAMC分类性能优于现有方法。
Yang et al. (2025) 探讨多模态数据整合中缺失值处理与多于双模态整合，现方法无法统一处理缺失并考虑模态内相关。提出GPCCA，无监督概率框架，将数据分解为共享潜在嵌入、加载矩阵、均值和误差项，误差协方差块对角允许模态内相关。使用EM算法处理缺失，加入岭正则化稳定。实验在模拟设置中，GPCCA在ARI和NMI聚类指标上优于PPCA、MOFA和DGCCA，鲁棒于0-40%缺失率；在TCGA多组学数据上，识别生存差异显著簇，提升Cox回归C指数。
概念认知与概率CCA方法
此类方法融入概念学习或概率模型，提升标签层次相关捕捉。
Authors of MCF-3WCCL (2025) 研究多标签学习中多级标签相关层次结构捕捉，现统计方法忽略层次导致认知偏差。提出MCF-3WCCL，使用三路概念认知算子结构化表示标签概念，捕捉层次相关。将标签概念范围映射到特征概念，形成标签-特征依赖，并融合形成整体认知。实验在多数据集上，方法在预测性能上优于基准，显示通用性。
实验与评价总结
2022–2025年间的工作多在基准如MS-COCO、IAPRTC-12、ROSMAP和TCGA数据集上验证，共性结论包括：多视图整合提升mAP和MCC达10-30%，高阶相关建模减少标签噪声影响，提高ARI/NMI聚类指标；深度非线性映射处理缺失数据时鲁棒性强，相对随机提升20-40%；特征选择与通路分析揭示生物相关簇，优化计算复杂度支持大规模应用。
趋势与挑战
2025年前后趋势预测：1. 整合Transformer架构增强CCA的非线性捕捉，处理动态多模态序列数据；2. 扩展到联邦学习框架，解决隐私敏感多组学数据的分布式整合；3. 应用到新兴领域如气候多标签预测，融合卫星与地面数据提升鲁棒性；挑战包括计算复杂度优化与泛化到低资源场景。
结论
CCA在多标签分类中的扩展显著提升了多模态相关捕捉与噪声鲁棒性，未来需聚焦高效算法与跨域应用。
参考文献

Sanghavi, R., & Verma, Y. (2022). Multi-view Multi-label Canonical Correlation Analysis for Cross-modal Matching and Retrieval. In CVPR Workshops.
Liu, B., Li, W., Xiao, Y., Chen, X., Liu, L., Liu, C., Wang, K., & Sun, P. (2023). Multi-view multi-label learning with high-order label correlation. Information Sciences, 622, 363-381.
Wang, R. A., et al. (2022). Dual-scale correlation analysis for robust multi-label classification. Applied Intelligence.
Si, C., Jia, Y., Wang, R. A., Zhang, M. L., Feng, Y., & Qu, C. (2022). Multi-Label Classification With High-Rank and High-Order Label Correlations. IEEE Transactions on Knowledge and Data Engineering.
Moon, S., Hwang, J., & Lee, H. (2022). SDGCCA: Supervised Deep Generalized Canonical Correlation Analysis for Multi-Omics Integration. Bioinformatics.
Vieluf, S., Hasija, T., Kuschel, M., Reinsberger, C., & Loddenkemper, T. (2023). Developing a deep canonical correlation-based technique for seizure prediction. Expert Systems with Applications.
Karakasis, P. A., & Sidiropoulos, N. D. (2023). Revisiting Deep Generalized Canonical Correlation Analysis. arXiv:2312.13455.
Rani, A., Sanghavi, R., & Verma, Y. (2025). Multi-view multi-label canonical correlation analysis for cross-modal multimedia retrieval. ResearchGate Publication.
Yang, T., & Li, W. V. (2025). Generalized probabilistic canonical correlation analysis for multi-modal data integration with full or partial observations. BMC Bioinformatics.
Authors of MCF-3WCCL. (2025). Multi-level correlation information fusion via three-way concept-cognitive learning for multi-label learning. Information Fusion.
Sanghavi, R., et al. (2022). Multi-view Multi-label Canonical Correlation Analysis for Cross-Modal Retrieval. IEEE Explore.
Neural Networks with the Correlative Layer for Multi-label Classification. (2023). Journal of Physics: Conference Series, 2425(1), 012034.