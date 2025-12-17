# 多标签学习系统及其扩展：2022–2025年研究综述

## 引言

多标签学习（Multi-label Learning, MLL）任务要求模型为每个输入样本预测一个可能包含多个标签的子集，其核心挑战在于标签空间的组合爆炸、标签间的复杂依赖（相关性、层次性、排他性）以及训练数据中普遍存在的正负样本不平衡与标注噪声。近年来，随着预训练语言模型（PLMs）和视觉基础模型（VFMs）的兴起，以及对损失函数、标签关系建模和多模态融合的深入探索，MLL系统在文本、图像乃至遥感等领域的性能显著提升。本文系统综述2022至2025年间在多标签学习系统及其扩展方向上的代表性工作，聚焦于损失函数创新、标签关系建模、层次结构处理及多模态融合等关键方向，并对未来研究趋势进行展望。

## 方法分类与代表作

### 基于新型损失函数的方法

传统二元交叉熵（BCE）损失在处理多标签数据固有的正负不平衡问题时表现不佳。为解决此问题，研究者提出了更精细的损失函数设计。阿里巴巴团队提出的**Asymmetric Loss (ASL)** [Cao et al., ICCV 2021, extended in 2022–2025 practices] 通过引入不对称聚焦（asymmetric focusing）和概率偏移（probability shifting）机制，对正负样本采用不同的聚焦参数（γ+ < γ-），并硬阈值掉极易分类的负样本。该方法在MS-COCO等数据集上将mAP提升至86.6%，显著优于Focal Loss，成为后续多标签工作的标准基线之一。苏建林等人提出的**ZLPR损失** [Su et al., arXiv 2022] 结合了log-sum-exp和成对排序的思想，不仅能处理标签数量不确定的问题，还显式建模了标签间的相关性。其计算复杂度与标签无关的特性使其在大规模场景中极具优势，并支持标签平滑等正则化技术。这些工作表明，针对性的损失函数设计是提升多标签模型性能的有效且高效的途径。

### 基于标签关系与注意力机制的方法

显式建模标签间的语义和统计依赖关系是提升多标签分类性能的另一核心方向。毛星亮等人提出的**MIRE模型** [Mao et al., Journal of Software 2023] 通过文本-标签联合嵌入，将两者映射到同一语义空间，并设计了文档级和词级两个并行的注意力分类模块，分别捕获不同粒度的文本-标签交互。其标签约束性关系匹配（LCRM）辅助模块通过学习标签共现统计来增强标签间的约束性关系。该方法在AAPD、LAIC和医疗问句数据集上均取得SOTA结果，验证了多粒度交互与标签关系学习的有效性。石琇赟等人针对图像分类，提出了**ML-M-GAT模型** [Shi et al., Computer Systems & Applications 2023]，利用标签共现矩阵和Word2Vec词向量构建标签图，并采用多头图注意力网络（M-GAT）学习标签间的非对称相关权重，最终将此权重与ResNet101提取的图像特征融合。该模型在VOC-2007和COCO-2014上分别达到94%和82.2%的mAP，显著优于基线模型。

### 基于层次结构的方法

当标签天然构成层次结构（如科学文献分类、商品类目）时，标准多标签方法无法利用这种先验知识。武子轩等人提出的**MHGCLR模型** [Wu et al., Journal of Zhengzhou University 2025] 针对层次多标签文本分类（HMTC）问题，首先融合BERT词向量和Doc2Vec句向量以捕获多尺度文本特征，再通过Graphormer编码标签层次结构。模型采用对比学习策略，在层次结构指导下构建正负样本对，有效学习了标签间的父子依赖关系。该工作还提出了层次Micro/Macro-F1指标，以更合理地评估层次一致性。在WOS、RCV1-V2等数据集上，MHGCLR全面超越了HiAGM、HTCInfoMax等现有方法。陈林卿等人则将**层次结构极限多标签分类**视为序列生成问题 [Chen et al., CCL 2022]，利用Transformer的编码器-解码器架构直接生成有序的标签序列，并通过软约束机制在解码过程中利用标签的层次信息。该方法在微软学术图谱（MAG）数据集上表现出强大的性能和对标签噪声的鲁棒性。

### 基于多模态与小样本学习的方法

在数据标注成本高昂的领域（如遥感），小样本和多模态学习成为重要扩展。周维等人提出的**FSSNet模型** [Zhou et al., Journal of Electronics & Information Technology 2025] 针对小样本遥感影像地物分类，构建了一个图像-文本多模态融合网络。该模型利用CLIP模型对齐图像与文本语义，并设计了类别信息融合模块（CIM）和基于改进FPN（IFPN）的实例信息提取模块。在解码器端，通过多尺度语义聚合模块整合信息。FSSNet在PASCAL-5i、LoveDA等多个数据集上均超越SOTA模型，证明了多模态先验在小样本场景下的巨大价值。

## 实验与评价总结

综合分析近年代表性工作，可得出以下共性结论：（1）**预训练模型的基石作用**：无论是文本还是图像任务，BERT、ResNet、CLIP等预训练模型作为特征提取器已成为标配，其强大的表征能力是性能提升的前提。（2）**标签关系建模的普适增益**：显式或隐式地建模标签间的关系（共现、层次、语义相似性）几乎在所有场景下都能带来稳定的性能提升，尤其是在标签空间较大、长尾分布严重的情况下。（3）**评价指标的演进**：除传统的Micro/Macro-F1、P@k、nDCG@k外，针对特定场景的指标（如层次F1、mIoU）被提出，以更全面地衡量模型在复杂约束下的表现。（4）**正负样本不平衡的应对**：ASL类损失函数因其简单高效，已成为处理不平衡问题的事实标准，并被广泛集成到各类新模型中。

## 趋势与挑战

基于当前研究进展，预计2025年前后多标签学习将呈现以下趋势：（1）**与通用人工智能（AGI）基础模型深度融合**：利用大语言模型（LLMs）和多模态大模型（MLMs）的零样本/少样本推理能力、指令遵循能力和链式思维（Chain-of-Thought），将多标签任务重构为提示工程（Prompt Engineering）或上下文学习（In-Context Learning）问题，以突破传统监督学习的局限。（2）**动态与开放世界多标签学习**：现实世界标签集并非静态封闭，模型需能处理新类（open-set）的持续引入、标签概念的漂移（concept drift）以及部分标签缺失/噪声等挑战，这对模型的可扩展性和鲁棒性提出更高要求。（3）**可解释性与可信多标签学习**：随着模型在司法、医疗等高风险领域的应用，其预测结果的可解释性（如关键证据的定位、标签决策路径的追溯）和可信度（如不确定性估计、对抗鲁棒性）将成为研究热点，以确保AI系统的安全可靠。

## 结论

2022–2025年是多标签学习系统迅速发展和深化的时期。研究重心已从早期的简单模型适配转向对损失函数、标签关系、层次结构和多模态信息的精细化建模。以ASL为代表的损失函数、以MIRE和ML-M-GAT为代表的标签关系建模方法、以MHGCLR为代表的层次结构处理框架，以及以FSSNet为代表的多模态小样本学习模型，共同推动了该领域的技术进步。展望未来，与AGI基础模型的融合、对动态开放世界的适应以及对可信可解释性的追求，将构成多标签学习系统下一阶段的核心发展方向。

## 参考文献

1.  Cao, Y., et al. (2021). Asymmetric Loss For Multi-Label Classification. In *Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV)*. (Widely adopted in 2022-2025 works).
2.  Su, J., Zhu, M., Murtadha, A., Pan, S., Wen, B., & Liu, Y. (2022). ZLPR: A Novel Loss for Multi-label Classification. *arXiv preprint arXiv:2208.02955*.
3.  Mao, X., Li, F., Su, P., Duan, J., & Zhang, S. (2023). Multi-label Text Classification with Enhancing Multi-granularity Information Relations. *Journal of Software (软件学报)*, 34(12), 5686-5703.
4.  Shi, X., Li, S., & Han, X. (2023). Multi-label Image Classification Based on Multi-head Graph Attention Network and Graph Model. *Computer Systems and Applications (计算机系统应用)*, 32(6), 286-292.
5.  Wu, Z., Wang, Y., & Yu, H. (2025). Hierarchical Multi-label Text Classification Method Based on Multi-scale Feature Extraction. *Journal of Zhengzhou University (Natural Science Edition) (郑州大学学报(理学版))*, 57(2), 24-30.
6.  Chen, L., He, D., Xiao, Y., Liu, Y., Lu, J., & Wang, W. (2022). Generation Model for Hierarchical Extreme Multi-label Text Classification. In *Proceedings of the 21st Chinese National Conference on Computational Linguistics (CCL 2022)* (pp. 671-683).
7.  Zhou, W., Wei, M., Xu, H., & Wu, Z. (2025). A Few-Shot Land Cover Classification Model for Remote Sensing Images Based on Multimodality. *Journal of Electronics & Information Technology (电子与信息学报)*, 47(6), 1747-1761.
8.  Liu, R., Liang, W., Luo, W., Song, Y., Zhang, H., Xu, R., Li, Y., & Liu, M. (2023). Recent Advances in Hierarchical Multi-label Text Classification: A Survey. *arXiv preprint arXiv:2307.16265*.
9.  Wang, J., Yang, Y., Mao, J., Huang, Z., Huang, C., & Xu, W. (2016). CNN-RNN: A unified framework for multi-label image classification. In *Proceedings of the IEEE conference on computer vision and pattern recognition* (often used as a baseline in recent works like Shi et al., 2023).
10. Yang, P., Sun, X., Li, W., Ma, S., Wu, W., & Wang, H. (2018). SGM: Sequence generation model for multi-label classification. In *Proceedings of the 27th International Conference on Computational Linguistics* (a foundational work for sequence-based methods like Chen et al., 2022).
11. Zhang, Z., Zhao, T., Guo, Y., Zhang, M., Wang, Y., Yao, Y., ... & Zhu, X. X. (2024). RS5M and GeoRSCLIP: A large-scale vision-language dataset and a large vision-language model for remote sensing. *IEEE Transactions on Geoscience and Remote Sensing*, 62, 5642123. (Context for Zhou et al., 2025).
12. Deng, Z., Peng, H., He, D., Liu, Y., & Wang, M. (2021). HTCInfoMax: a global model for hierarchical text classification via information maximization. In *Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies* (a key baseline for Wu et al., 2025).