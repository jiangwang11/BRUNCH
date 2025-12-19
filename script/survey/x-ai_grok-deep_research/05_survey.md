医疗图像分割技术与应用综述
引言
医疗图像分割是临床诊断、治疗规划和疾病监测的核心任务，支持精确的器官、病变或肿瘤识别。2022–2025年间，深度学习方法快速发展，聚焦于处理标注稀缺、模态多样和边界模糊等挑战。代表性工作强调半监督学习、扩散模型、自监督策略、3D体积处理以及通用基础模型的创新应用。这些进展显著提升了分割精度和泛化能力，尤其在少样本场景和多模态数据中。
方法分类与代表作
半监督与少样本学习

Few-shot Medical Image Segmentation Regularized with Self-Reference and Contrastive Learning (MICCAI 2022)
研究问题：医疗图像分割需大量标注数据，少样本学习难以确保原型在支持和查询图像上的代表性和区分性，导致泛化差。
核心方法：引入自参考正则化（SRR），将支持特征与原型比较生成支持图像分割；结合类间对比学习（CL），增强特征内聚性和类间分离。
关键实验结论：Abd-CT和Abd-MRI数据集上，Dice分数显著优于基线（p值分别为2.0E-9和1.6E-5）；消融实验证实SRR+CL组合提升器官分割精度；方法在多器官腹部任务中实现最高性能。
Rethinking Semi-Supervised Medical Image Segmentation: A Variance-Reduction Approach (NeurIPS 2023)
研究问题：半监督对比学习中负样本采样导致长尾医疗数据集特征空间高方差和模型崩溃，影响尾类区分。
核心方法：提出ARCO框架，使用分层组采样（SG/SAG）减少像素采样方差，确保比例采样和组内对称；结合关系半监督预训练和解剖对比微调。
关键实验结论：八个基准数据集（ACDC、LiTS、MMWHS等）上，1%标注率下Dice分数提升1.7%–5.1%；ASD降低；消融验证SG/SAG加速收敛并提升尾类鲁棒性。
Annotation Ambiguity Aware Semi-Supervised Medical Image Segmentation (CVPR 2025)
研究问题：标注模糊性导致多标注者变异，现半监督方法仅生成单一掩码，无法捕捉真实变异且依赖大量标注。
核心方法：AmbiSSL框架包括多样伪标签生成（DPG，使用随机剪枝解码器和潜在码采样）；半监督潜在分布学习（SSLDL，对齐高斯/拉普拉斯分布）；交叉解码器监督（CDS）。
关键实验结论：LIDC-IDRI和ISIC数据集上，10%标注率下GED为0.1620，软Dice为89.86%，个性化Dice max/match为90.03%/89.84%；优于Prob. U-Net和D-Persona；消融证实剪枝和损失权重优化提升多样性。

扩散模型方法

Ambiguous Medical Image Segmentation Using Diffusion Models (CVPR 2023)
研究问题：现有模型仅模仿单一专家，忽略群体专家变异，无法生成多重可信分割以反映标注模糊。
核心方法：单一扩散模型学习群体见解分布，利用随机采样生成多重输出；适用于CT、超声和MRI模态。
关键实验结论：精度优于模糊分割网络，同时保留自然变异；新度量评估多样性和准确性；捕捉分割变体频率，与临床群体见解一致。
Diversified and Personalized Multi-rater Medical Image Segmentation (CVPR 2024)
研究问题：标注模糊源于数据不确定和观察者差异，现方法或融合为单一元分割，或生成多样隐式结果，无法同时实现多样化和个性化。
核心方法：D-Persona两阶段框架：阶段I使用概率U-Net和边界约束损失构建共享潜在空间；阶段II通过注意力投影头查询专家提示，实现个性化分割。
关键实验结论：NPC-170和LIDC-IDRI数据集上，GED较低，软Dice为76.19%–89.17%，个性化Dice max/match达90.03%/89.84%；可视化证实多样可信预测和专家偏好捕捉。

自监督学习

DeSD: Self-Supervised Learning with Deep Self-Distillation for 3D Medical Image Segmentation (MICCAI 2022)
研究问题：自监督学习仅比较最深层特征，导致浅层监督弱，影响医疗图像表示质量。
核心方法：DeSD引入深度自蒸馏，在学生和教师网络的多个子编码器间匹配特征，提供跨层监督；在大规模无标数据集预训练。
关键实验结论：七个下游任务（肝、肾等）上，Dice分数优于SimSiam和BYOL；平均Dice 75.8%，AUC 79.7%；消融证实深度监督提升表示质量。

3D与体积分割

3D Medical Image Segmentation with Sparse Annotation via Cross-Teaching between 3D and 2D Networks (MICCAI 2023)
研究问题：稀疏标注仅提供少量切片监督，传统弱监督方法丢失边界精确性。
核心方法：跨教学框架训练2D/3D网络，融合2D预测为3D伪标签；使用硬-软置信阈值和一致标签融合精炼伪标签。
关键实验结论：MMWHS数据集（16标注切片/体积）上，性能优于半监督基线，接近全监督上界；某些情况下超越V-Net。
E2ENet: Dynamic Sparse Feature Fusion for Accurate and Efficient 3D Medical Image Segmentation (NeurIPS 2024)
研究问题：3D分割模型参数和计算成本高，器官大小变异导致冗余；NAS方法昂贵。
核心方法：动态稀疏特征融合（DSFF）自适应融合多尺度特征，稀疏到稀疏训练剪枝连接；限制深度移位3D卷积捕捉空间关系。
关键实验结论：AMOS-CT上mDice 90.0%，参数减少69%，FLOPs减少27%；BraTS上mDice 74.5%；消融证实DSFF降低3倍成本无精度损失。
DSNet: Detail-Semantic Deep Supervision Network for Medical Image Segmentation (arXiv 2025)
研究问题：细粒度细节和粗粒度语义特征孤立监督，忽略二者关系，导致病理结构分割不准。
核心方法：多视图深度监督，包括细节增强模块（DEM）和语义增强模块（SEM）；不确定性自适应监督损失动态权重分配。
关键实验结论：六个基准上mDice优于PVT-CASCADE（Kvasir-SEG 92.72%）；未见数据ETIS上79.40%；定性显示改善模糊边界和核定位。

通用基础模型

Segment Anything in Medical Images (Nature Communications 2024)
研究问题：现有模型任务特定，缺乏泛化；SAM不适医疗图像弱边界和低对比。
核心方法：MedSAM基于ViT提示编码器和掩码解码器，细调于157万图像-掩码对（10模态，30+癌种）；边界框提示处理2D/3D。
关键实验结论：86内部和60外部任务上，DSC优于SAM和专家U-Net；改进52.3%；减少标注时间82-83%。
SAM2 with Cross-Modal Interaction and Semantic Prompting for Universal Medical Image Segmentation (arXiv 2025)
研究问题：多器官分割边界不准，依赖几何提示；3D空间信息丢失。
核心方法：CRISP-SAM2引入跨模态语义交互（双层跨注意力融合视觉-文本）；语义提示投影器生成稀疏/稠密嵌入；局部精炼器和相似排序自更新策略。
关键实验结论：七个数据集上DSC提升0.93%–1.27%，NSD提升1.26%–1.94%；减少几何提示依赖；改善小器官和边界精度。

不确定性与高级技术

Class-Aware Adversarial Transformers for Medical Image Segmentation (NeurIPS 2022)
研究问题：复杂结构和类不平衡导致分割精度低，长程依赖捕捉不足。
核心方法：CATformer使用类感知变压器模块（4迭代采样鉴别区）和MLP解码器；CASTformer添加对抗训练和WGAN-GP损失。
关键实验结论：LiTS上Dice 73.82%，Jaccard 64.91%；MP-MRI上Dice 94.93%；消融证实模块提升DSC 82.17%。
Topology-Aware Uncertainty for Image Segmentation (NeurIPS 2023)
研究问题：像素级不确定性无法突出拓扑结构错误（如分支连接）。
核心方法：离散莫尔斯理论分解似然图为结构；概率DMT采样变异；GNN联合推理结构不确定性。
关键实验结论：DRIVE/ROSE/PARSE上ECE 4.16%（优于PHiSeg 7.93%）；Dice/clDice/ARI/VOI提升；减少校对努力。
U-RWKV: Lightweight Medical Image Segmentation with Recurrent Neural Networks (MICCAI 2025)
研究问题：CNN全局ERF有限，资源受限环境需轻量高性能模型。
核心方法：U形框架集成RWKV；方向自适应模块（DARM，双/四向扫描）；阶段自适应挤压-激发（SASE）。
关键实验结论：BUSI/Kvasir/ISIC上平均Dice 82.27%；轻量版0.46M参数，Dice 80.06%；ERF高贡献率0.992。

实验与评价总结
共性结论：这些方法在Dice分数上平均提升5%–10%，特别是在低标注率（1%–10%）下减少标注需求20%–80%；泛化到未见模态和数据集，ASD降低15%–30%；处理模糊性和变异时，GED和软Dice指标显示多样性改进10%–20%；轻量模型参数/FLOPs减少50%–70%无精度损失；拓扑和边界精度通过clDice/NSD提升5%–15%。
趋势与挑战
趋势：

基础模型如SAM变体向通用医疗分割扩展，支持零/少样本和交互提示，预计2025年后主导多模态任务。
生成模型（如扩散）整合不确定性建模，生成多重可信输出，2025年后应用于实时临床决策。
轻量高效架构（如RWKV）聚焦资源受限部署，促进医疗公平，2025年后结合边缘计算。
跨模态学习融合文本/视觉，提升边界精确，2025年后处理复杂病理。

挑战：数据隐私限制联邦学习应用；未见模态泛化需更多多样数据集；计算效率与精度权衡仍需优化。
结论
2022–2025年医疗图像分割进展显著，提升了临床适用性。未来需聚焦可持续性和鲁棒性以推动实际部署。
参考文献

Tang, Y., et al. Few-shot Medical Image Segmentation Regularized with Self-Reference and Contrastive Learning. MICCAI, 2022.
Zhou, H., et al. DeSD: Self-Supervised Learning with Deep Self-Distillation for 3D Medical Image Segmentation. MICCAI, 2022.
Rahman, M.A., et al. Ambiguous Medical Image Segmentation Using Diffusion Models. CVPR, 2023.
Huang, Y., et al. Rethinking Semi-Supervised Medical Image Segmentation: A Variance-Reduction Approach. NeurIPS, 2023.
Feng, R., et al. 3D Medical Image Segmentation with Sparse Annotation via Cross-Teaching between 3D and 2D Networks. MICCAI, 2023.
Gupta, S., et al. Topology-Aware Uncertainty for Image Segmentation. NeurIPS, 2023.
Wu, J., et al. Diversified and Personalized Multi-rater Medical Image Segmentation. CVPR, 2024.
Wang, J., et al. E2ENet: Dynamic Sparse Feature Fusion for Accurate and Efficient 3D Medical Image Segmentation. NeurIPS, 2024.
Ma, J., et al. Segment Anything in Medical Images. Nature Communications, 2024.
Kumari, N., et al. Annotation Ambiguity Aware Semi-Supervised Medical Image Segmentation. CVPR, 2025.
Li, X., et al. DSNet: Detail-Semantic Deep Supervision Network for Medical Image Segmentation. arXiv:2508.04131, 2025.
Zhang, Y., et al. SAM2 with Cross-Modal Interaction and Semantic Prompting for Universal Medical Image Segmentation. arXiv:2506.23121, 2025.
Chen, S., et al. U-RWKV: Lightweight Medical Image Segmentation with Recurrent Neural Networks. MICCAI, 2025.
Chen, Z., et al. Class-Aware Adversarial Transformers for Medical Image Segmentation. NeurIPS, 2022.