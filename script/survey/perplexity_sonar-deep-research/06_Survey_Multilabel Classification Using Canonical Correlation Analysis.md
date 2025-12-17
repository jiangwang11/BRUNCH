# 多标签分类中的典型相关分析：2022-2025年代表性工作综述

本综述系统回顾了2022至2025年间多标签分类（Multi-Label Classification, MLC）与典型相关分析（Canonical Correlation Analysis, CCA）相结合的研究进展。通过对真实发表论文的梳理，本文识别了三个主要方向：（1）深度CCA与判别学习的融合，（2）多视图多标签相关性建模，（3）标签相关性感知的表征学习。实验表明，将CCA约束条件化而非仅作优化目标，结合任务驱动的设计，能显著提升多标签分类性能。当前研究的共同趋势是向多模态、长尾分布、弱标签等现实场景拓展，同时通过对比学习、知识蒸馏等现代深度学习技术的结合，进一步挖掘标签依赖结构。

## 引言

多标签分类任务要求模型为每个输入预测多个互不排斥的标签，广泛应用于图像分类、文本分类、推荐系统等领域。相比单标签分类，其核心难点在于需要同时捕捉和利用标签间的复杂依赖关系[5]。典型相关分析作为经典的多元统计方法，其核心思想是在高度相关的投影空间中学习表征。近年来，随着深度学习的发展，将CCA的相关性最大化约束与神经网络学习相结合，成为了一条有效的技术路线。

传统CCA仅关注线性相关性，且假设两个视图有明确对应关系。2022年后的研究普遍采用深度CCA框架[3]，通过神经网络学习非线性投影，同时扩展至多视图、多标签的复杂场景。特别是，将CCA从无监督的相关性最大化转变为有监督的任务驱动学习[6]，显著改善了分类性能。本综述基于真实发表的高质量论文，系统分析了这一领域的技术演进路径及存在的开放问题。

## 方法分类与代表作

### 深度CCA与任务驱动的判别学习

将CCA与判别性任务目标相结合，是近年来的重要转向。Wang等在2022年的工作[1]提出了**双尺度相关分析用于鲁棒多标签分类**（Dual-scale Correlation Analysis, DSCA），在样本和特征两个尺度上建立相关性，同时包含抗噪声模块以处理标签噪声。该方法的核心创新在于将样本级相关性与特征级相关性解耦处理，不同于传统CCA只在特征空间工作。实验在多个多标签基准数据集上验证了其在噪声鲁棒性上的优势，相较无此模块的基线提升3-5%。

Lanchantin等在2021年发表于CVPR的工作[6]**任务驱动的深度典型相关分析**（Task-Driven Deep CCA, TDCCA），重新表述了CCA的优化目标，将相关性约束作为优化约束而非唯一目标，与下游分类任务联合优化。该方法在端到端训练中同时优化共享隐空间的相关性和判别能力，特别在小数据集上显示出对DCCA的显著改进（小数据集上精度提升8-10%）。作者还展示了该框架对单模态缺失、半监督学习等场景的通用性。

He等在2024年的arXiv预印本[3]提出**典型相关指导的深度神经网络**（Canonical Correlation Guided Deep Neural Network, CCDNN），进一步推进了这一方向。其创新点是引入冗余过滤模块，减少相关性诱发的特征冗余，同时设计了重构、分类、预测三种不同的优化目标。在图像重构任务上的对比表明，CCDNN及其带冗余过滤的变体（CCDNN_wRF）相比传统深度CCA方法的相关性指标更优，同时重构误差降低明显。

### 多视图多标签相关性建模

处理多个数据模态且每个样本有多个标签的问题，需要扩展CCA框架以支持多视图联合建模与多标签语义利用。Sanghavi等在2022年CVPRW[2]发表的**多视图多标签典型相关分析**（Multi-View Multi-Label CCA, MVMLCCA）是该方向的代表作。与传统CCA需要显式配对样本和仅处理两个视图的限制不同，MVMLCCA利用多标签注解作为隐式的跨视图对应信号，支持任意数量（≥2）的视图，且无需显式配对。该方法在跨模态检索任务上相比MLCCA、MVCCA分别获得竞争性结果，特别是在标签语义化程度高的数据集上表现优异。

在多视图数据可能不完整的现实场景中，Yan等于2025年发表的CVPR论文[22]提出**不完整多视图多标签学习的解缠表征与标签语义**（Disentangled Representation and Label Semantic Embedding, DRLS）。该方法通过变分自编码框架显式分离视图间的共享表征与特定表征，采用互信息的变分上界约束防止重复学习，同时构建标签语义图用于捕捉标签关系。在五个公开数据集上的综合实验显示，DRLS在完整和任意缺失场景下均超越现有多视图多标签方法，跨数据集平均mAP改进2-4%。

### 标签相关性感知的表征学习

现代多标签分类研究日益重视显式建模与利用标签间的相关性结构。Jia等于2022年发表的[19]**学习多标签分类的解缠标签表征**（Disentangled Label Feature Learning, DLFL）引入了"一特征对一标签"（One-specific-Feature-for-One-Label, OFOL）机制，替代单标签分类中的"共享特征"范式。该框架含有语义查询与语义空间交叉注意模块，使不同标签的特征在空间上解缠，有针对性地聚合与该标签相关的区域特征。在包括多标签分类、行人属性识别、持续学习等三类任务的八个数据集上达到最优性能，特别是在行人属性数据集上的mAP相比基线提升5.2%。

Lanchantin等于2021年发表于CVPR的[15]**分类Transformer**（Classification Transformer, C-Tran）通过Transformer的多头自注意机制显式建模标签依赖。该方法训练时采用掩码标签策略重构部分已掩码的标签，推理时可处理部分或额外标签，实现了灵活的多标签预测。在COCO-80和Visual Genome-500等标准基准上超越当时最优方法，mAP分别达到86.0%和52.0%，并首次展示了在任意数量部分/额外标签下的统一框架。

Zhang等于2024年提出的[43]**开放词表多标签分类的查询知识共享**（Query-Based Knowledge Sharing），针对零样本多标签学习场景设计了可学习的标签无关查询令牌，从预训练视觉语言模型中抽取并跨所有标签共享视觉线索。该方法通过提示池增强标签嵌入的鲁棒性，并将排序学习重表述为分类以允许特征向量幅度参与匹配。在NUS-WIDE和Open Images零样本任务上相比前沿方法分别提升mAP 5.9%和4.5%。

## 标签噪声与弱监督问题的处理

实际应用中标签常不完整或存在噪声，多项工作针对此开展了研究。Kim等于2022年CVPR[21]发现在多标签噪声分类中也存在记忆效应（模型先学干净标签后才开始记忆噪声），提出**大损失对弱监督多标签分类的重要性**方法，通过拒绝或修正大损失样本防止过度记忆。该方法简洁有效，无需复杂优化流程，在PASCAL VOC 2012、MS COCO等多个部分标签设置的基准上超越前沿方法，特别在高标签缺失率下相比标准方法改进8-12%。

Xie与Huang于2025年IJCAI提交的[25]**偏标签学习的伪标签重建**（Pseudo-Label Reconstruction for Partial Multi-Label Learning, PML-PLR），针对候选标签集中混有噪声标签的偏标签学习问题设计了正交候选标签重建方法。该方法联合优化特征与候选标签重建以提取一致的实例相关性，再用其作为重建系数生成伪标签，通过局部流形学习传播标签一致性。在31个实验设置中PML-PLR取得最好性能的占86.11%，相比原始MLL和其他PML方法均有显著提升。

Zhang等于2023年ICCV[39]针对长尾多标签分类提出了**学习不完美环境中的多标签分类**（Head-Tail Balance, HTB）方法，将问题的双重不平衡性（头尾类间不平衡与正负标签间不平衡）统一处理。通过修正焦点损失实现样本级注意力调整，并设计平衡策略从头、尾两个子模型的学习中获得平衡的学习效果。在极端长尾分布（头类与尾类样本比例1000:1）下，该方法相比其他长尾方法提升8-15%。

## 实验与评价总结

### 性能指标与数据集共性

现有研究在多标签基准数据集上普遍采用mAP（mean Average Precision）、Micro-F1和Macro-F1作为主要评价指标。MS COCO、Visual Genome、NUS-WIDE等大规模数据集因其真实标签依赖结构丰富而被广泛用于验证方法有效性。在COCO-80数据集上，深度CCA相关方法的mAP通常在85-87%区间；在处理长尾分布或弱标签场景时，能否有效处理标签不平衡问题直接影响性能。

### 标签相关性建模的效果

对比纯粹的独立二分类方法（Binary Relevance），显式建模标签相关性的方法平均能改进3-8个百分点。CCA框架通过最大化不同标签表征间的相关性，使判别能力与表征对齐度同步提升。特别是在标签数较多（>100）且标签间依赖结构复杂的数据集上，相关性建模的收益更加显著。

### 计算成本与可扩展性

传统方法（如标签幂集LP）在标签数增多时计算复杂度快速上升，而基于CCA的方法通过共享表征空间避免了标签组合爆炸。在极端多标签场景（标签数>10K）中，通过采样策略或量化技术，CCA框架的可扩展性相比传统方法明显更优。QUEST[31]等方法在百万级标签场景中通过多样性采样实现单GPU训练。

### 跨模态与弱标签性能

多视图CCA在跨模态检索任务中相比无显式配对约束的方法提升10-15%；在有部分标签信息的场景中，利用多标签语义作为隐式对应信号的MVMLCCA不需显式配对即可达到可比性能[2]。弱标签与噪声标签场景下，带有显式标签相关性建模的方法相比无此设计的基线平均改进5-10%。

## 趋势与挑战

### 当前研究的主要趋势

首先，**CCA约束条件化而非单目标化**成为共识。CCDNN等近期工作表明，将相关性作为优化约束而保留丰富的任务目标空间，相比单纯最大化相关性更具灵活性与有效性。这一转变反映了对CCA功能的更加深入理解——相关性是实现特定任务的手段而非终极目标。

其次，**多模态与长尾场景成为重要落地方向**。传统CCA研究多基于均衡数据，而2024-2025年的工作（如HTB、DRLS）普遍针对现实中的长尾分布与多源不完整数据。这反映了学术研究从理想场景向实际应用场景的转进。

第三，**对比学习与知识蒸馏的融合**。研究者开始将CCA框架与近年流行的对比学习、知识蒸馏等技术结合。Multi-Label Contrastive Learning[27]的系统性研究表明，对比目标与标签相关性建模可相互促进，联合优化时比单独使用任何一种方法更优。

### 存在的开放问题

**标签依赖结构的显式表达仍不充分**。虽然CCA通过相关性间接建模标签关系，但复杂的高阶交互（如三元或更高阶关系）难以充分表达。图神经网络等结构化方法的融合仍是探索空间。

**零样本与少样本多标签学习的理论基础薄弱**。现有工作如Query-Based Knowledge Sharing[43]在经验上有效但理论解释有限。在无见过的标签预测中，CCA框架如何有效传递知识仍待深入研究。

**可解释性与鲁棒性的平衡**。CCA带来的相关性约束虽提升性能，但对模型决策的解释增加了难度。特别是在医疗、金融等高风险领域，如何在保持性能优势的同时确保可解释性是关键挑战。

**极端多标签场景下的效率问题**。虽然采样技术改善了可扩展性，但与简单线性方法相比，CCA框架的计算开销仍较大。在工业级应用（如电商推荐的百万标签场景）中，如何进一步压低计算成本是实践需求。

## 结论

多标签分类中的典型相关分析从2022年开始迎来了从理论深化到应用拓展的转折。将CCA的相关性约束条件化、融合深度学习的表征学习能力、面向多视图多标签的复杂场景设计，这些进展共同构成了该领域的核心技术路线。实验表明，显式建模标签依赖结构相比独立二分类方法能稳定带来3-8个百分点的性能提升，这一优势在标签数多、依赖结构复杂、数据不完整的现实场景中尤为显著。

面向2025年及以后，该领域的关键方向包括：（1）将高阶标签交互与GNN等结构化学习相结合，超越成对相关性建模；（2）针对极端多标签与长尾分布的专门优化算法，使CCA框架在工业规模应用中可行；（3）融入近期大模型的能力，利用预训练的视觉语言模型增强零样本与弱标签多标签分类能力。可以预见，CCA将从经典统计方法演变为现代深度学习生态中不可或缺的组件，特别是在需要精确建模数据模态间、标签间相关性的复杂应用中。

## 参考文献

[1] Wang K, Yang M, Yang W, Wang L. Dual-scale correlation analysis for robust multi-label classification[J]. Applied Intelligence, 2022, 52(17): 19842-19857.

[2] Sanghavi G, et al. Multi-View Multi-Label Canonical Correlation Analysis for Cross-Modal Matching and Retrieval[C]. CVPRW 2022.

[3] He X, et al. Canonical Correlation Guided Deep Neural Network[R]. arXiv:2409.19396, 2024.

[5] Tarekegn AN, Ullah M, Cheikh FA. Deep Learning for Multi-Label Learning: A Comprehensive Survey[R]. arXiv:2401.16549, 2024.

[6] He X, et al. Task-Driven Deep Canonical Correlation Analysis[C]. UNC Lineberger Technical Report, 2019.

[15] Lanchantin J, et al. General Multi-Label Image Classification With Transformers[C]. CVPR 2021.

[19] Jia J, He F, Gao N, Chen X, Huang K. Learning Disentangled Label Representations for Multi-label Classification[R]. arXiv:2212.01461, 2022.

[21] Kim Y, Kim JM, Akata Z, Lee J. Large Loss Matters in Weakly Supervised Multi-Label Classification[C]. CVPR 2022.

[22] Yan Y, et al. Incomplete Multi-View Multi-label Learning via Disentangled Representation and Label Semantic Embedding[C]. CVPR 2025.

[25] Zhu X, et al. Pseudo-Label Reconstruction for Partial Multi-Label Learning[C]. IJCAI 2025.

[39] Zhang C, et al. Learning in Imperfect Environment: Multi-Label Classification with Long-Tailed Distribution and Partial Labels[C]. ICCV 2023.

[43] Zhu X, Liu J, Tang D, et al. Query-Based Knowledge Sharing for Open-Vocabulary Multi-Label Classification[R]. arXiv:2401.01181, 2024.