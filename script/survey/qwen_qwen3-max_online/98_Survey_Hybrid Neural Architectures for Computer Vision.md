# 混合神经架构在计算机视觉中的研究综述（2022–2025）

## 引言

近年来，卷积神经网络（CNN）与Transformer的融合催生了“混合神经架构（Hybrid Neural Architectures）”这一研究范式。CNN擅长提取局部特征且具有平移等变性，而Transformer通过自注意力机制建模长程依赖。二者融合旨在兼顾局部细节与全局语义，提升模型在图像分类、目标检测、图像融合等任务上的性能与泛化能力。本文系统梳理2022–2025年间该领域的代表性工作，按方法论分为架构参考、串并联拼接、局部替换与多层次融合四类，并总结共性结论与发展趋势。

## 方法分类与代表作

### 基于架构设计参考

研究者通过借鉴CNN的经典架构设计（如多尺度金字塔、残差连接）改进纯Transformer模型。PVTv2 [1]在原始PVT基础上引入渐进式收缩策略与重叠补丁嵌入，实现了类似CNN的多尺度特征图输出，显著提升密集预测任务性能。HRFormer [2]将HRNet的多分辨率并行结构与Transformer结合，在保持高分辨率特征的同时建模跨尺度长程依赖，在姿态估计与语义分割任务上优于ResNet与Swin Transformer。CSWin Transformer [3]提出十字形窗口注意力机制，通过跨窗口交互增强全局建模，同时保留局部连通性，在ImageNet分类上Top-1准确率达85.4%。

### 基于串并联拼接

该策略通过串联或并联方式组合CNN与Transformer模块。CoAtNet [4]将MBConv（MobileNetV2中的反向残差块）与相对自注意力交替堆叠，实现局部先验与全局感知的无缝融合，其ImageNet准确率超越EfficientNet与ViT，且训练更稳定。Conformer [5]首次采用并行结构，通过特征耦合单元（FCU）在CNN分支（局部）与Transformer分支（全局）间进行双向交互，实现特征的协同增强，在分类与检测任务上均优于单一分支模型。Mobile-Former [6]提出轻量级双向交叉桥接机制，使少量全局令牌与局部特征高效交互，在参数量仅21M时达到80.9% Top-1准确率。

### 基于局部模块替换

此类方法通过替换网络中的特定组件引入互补归纳偏置。BoTNet [7]将ResNet最后三个阶段的3×3卷积替换为多头自注意力模块，在实例分割任务上显著优于ResNet-101，且计算开销极小。CvT [8]提出卷积令牌嵌入（CTE）与卷积投影注意力（CPA），在ViT中嵌入卷积操作以保留局部性与平移不变性，在ImageNet上以更少参数取得比DeiT更高的准确率。LocalViT [9]将深度卷积引入Transformer前馈网络，为模型注入局部感知能力，有效提升小数据集上的泛化性能。

### 多层次混合架构

最新工作趋向于融合多种混合策略以最大化性能。Next-ViT [10]提出NHB混合策略，交替堆叠Next CNN Block（NCB）与Next Transformer Block（NTB），在保持高效的同时显著提升下游任务性能，在COCO检测上AP达50.1。EdgeNeXt [11]结合自适应卷积与分割深度转置注意力（SDTA），通过通道维度的自注意力建模全局依赖，在参数量仅5.6M时ImageNet准确率达78.8%。CeiT [12]整合卷积令牌嵌入、局部增强前馈层（LeFF）与逐层分类令牌注意力（LCA），在局部与全局建模上取得平衡，准确率达82.0%。

## 实验与评价总结

在ImageNet-1K分类任务上，混合模型普遍优于纯CNN（如ResNet）与纯Transformer（如ViT-B/16），Top-1准确率多在82%–85%区间，同时参数量与FLOPs显著低于ViT。在COCO目标检测任务中，基于混合主干的检测器（如CoAtNet-Backbone + RetinaNet）AP普遍提升2–4个百分点，表明其特征更具判别性。在红外-可见光图像融合等低层视觉任务中（如CDDFuse [13], SHIP [14]），混合架构能更有效保留源图像的纹理与热辐射信息，定量指标（如MI, VIF）显著领先。共性结论表明，合理的混合设计能在模型容量、计算效率与任务性能间取得更优平衡。

## 趋势与挑战

基于2024–2025年前沿工作，未来趋势可归纳为三点：  
1. **任务驱动的动态混合**：模型根据输入内容或任务需求自适应选择CNN或Transformer路径（如Next-ViT的NHB策略），而非静态堆叠。  
2. **跨模态融合的深度集成**：将混合架构扩展至多模态任务（如红外-可见光融合[14]、LiDAR-相机3D检测[15]），通过高阶交互机制（如SHIP的协同高阶交互）挖掘模态互补性。  
3. **硬件感知的轻量化设计**：针对边缘设备优化混合模块（如MobileViTV2 [42]的可分离自注意力、EdgeViTs [56]的LGL瓶颈），在精度与延迟间寻求帕累托最优。

核心挑战在于：如何理论化归纳偏置的互补性、降低混合模块的工程复杂度，以及建立统一的评估基准以公平比较不同融合范式。

## 结论

2022–2025年，混合神经架构已成为计算机视觉的主流范式之一。通过架构参考、串并联拼接、局部替换与多层次融合等策略，研究者有效结合了CNN的局部性与Transformer的全局性，在多项视觉任务上取得突破。未来研究将聚焦于动态混合、跨模态深度集成与硬件协同设计，推动模型向高效、通用与自适应方向演进。

## 参考文献

[1] Wang, W., et al. (2021). PVTv2: Improved Baselines with Pyramid Vision Transformer. *arXiv:2106.13797*.  
[2] Yuan, Y., et al. (2021). HRFormer: High-Resolution Transformer for Dense Prediction. *arXiv:2110.09408*.  
[3] Dong, X., et al. (2022). CSWin Transformer: A General Vision Transformer Backbone with Cross-Shaped Windows. *CVPR*.  
[4] Dai, Z., et al. (2021). CoAtNet: Marrying Convolution and Attention for All Data Sizes. *NeurIPS*.  
[5] Peng, Z., et al. (2021). Conformer: Local Features Coupling Global Representations for Visual Recognition. *ICCV*.  
[6] Chen, Y., et al. (2022). Mobile-Former: Bridging MobileNet and Transformer. *CVPR*.  
[7] Srinivas, A., et al. (2021). Bottleneck Transformers for Visual Recognition. *CVPR*.  
[8] Wu, H., et al. (2021). CvT: Introducing Convolutions to Vision Transformers. *ICCV*.  
[9] Li, Y., et al. (2021). LocalViT: Bringing Locality to Vision Transformers. *arXiv:2104.05707*.  
[10] Li, J., et al. (2022). Next-ViT: Next Generation Vision Transformer for Efficient Deployment. *arXiv:2207.05501*.  
[11] Maaz, M., et al. (2022). EdgeNeXt: Efficiently Amalgamated CNN-Transformer Architecture for Mobile Vision Applications. *ECCV*.  
[12] Yuan, K., et al. (2021). Incorporating Convolution Designs into Visual Transformers. *ICCV*.  
[13] Zhao, Z., et al. (2023). CDDFuse: Correlation-Driven Dual-Branch Feature Decomposition for Multi-Modality Image Fusion. *CVPR*.  
[14] Zheng, J., et al. (2024). Probing Synergistic High-Order Interaction in Infrared and Visible Image Fusion. *CVPR*.  
[15] Huang, J., et al. (2024). Detecting As Labeling: Rethinking LiDAR-camera Fusion in 3D Object Detection. *ECCV*.  
[16] 戴洋毅, 等. (2023). CNN-Transformer混合模型在计算机视觉领域的研究综述. *建模与仿真*, 12(4), 3657–3672.  
[17] Li, H., et al. (2021). RFN-Nest: An End-to-End Residual Fusion Network for Infrared and Visible Images. *Information Fusion*.  
[18] Liu, Z., et al. (2021). Swin Transformer: Hierarchical Vision Transformer using Shifted Windows. *ICCV*.