# 状态空间模型在图像处理中的研究综述（2022–2025）

## 引言

状态空间模型（State Space Models, SSMs）最初源于控制理论与信号处理，近年来因Mamba架构[Gu & Dao, 2023]的提出，在序列建模任务中展现出线性复杂度与长程依赖建模能力的双重优势。自2023年底起，研究者迅速将SSM迁移到图像处理领域，以缓解Vision Transformer（ViT）的平方复杂度瓶颈并超越卷积神经网络（CNN）的局部建模局限。本文系统梳理2022–2025年间SSM在图像处理中的关键进展，涵盖图像恢复、医学图像分析、遥感、点云及视频处理等方向，聚焦其方法创新、性能边界与实际效能。

## 方法分类与代表作

### 图像恢复

**MambaIR**（Guo et al., ECCV 2024）[ecva.net](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/2740_ECCV_2024_paper.php) 首次将Mamba引入图像超分辨率与去噪任务，指出原始Mamba存在局部像素遗忘与通道冗余问题。作者提出残差状态空间块（RSSB），引入局部卷积与通道注意力机制。在Set5超分辨率任务中，MambaIR比SwinIR提升0.45 dB PSNR，且FLOPs相近但具备全局感受野。

**MambaIRv2**（Guo et al., arXiv 2024）[arxiv.org](https://arxiv.org/abs/2411.15269) 进一步解决Mamba因果建模限制，提出“注意状态空间方程”，赋予模型非因果建模能力。其语义引导邻域机制促进远距离相似像素交互。在轻量级超分辨率中，MambaIRv2比SRFormer提升0.35 dB PSNR且参数减少9.3%。

**WaterMamba**（Guan et al., arXiv 2024）[arxiv.org](https://arxiv.org/abs/2405.08419) 针对水下图像增强（UIE）中严重退化与效率挑战，设计空间-通道全向选择扫描（SCOSS）块。该模块联合建模像素与通道信息流，并引入多尺度前馈网络（MSFFN）促进信息同步。在UIEB等数据集上，WaterMamba以更少参数超越SOTA方法。

### 医学图像分析

**融合邻域注意力和SSM的医学视频分割算法**（Ding et al., 电子与信息学报 2025）[jeit.ac.cn](https://jeit.ac.cn/cn/article/doi/10.11999/JEIT240755) 针对医学视频分割中时序建模效率低的问题，提出两阶段架构：先用邻域注意力捕获相邻帧局部时序关联，再用2D选择性扫描SSM建模长程依赖。在甲状腺超声视频上，IOU达72.7%，比Vivim高5.7%，推理速度达23.97 fps，满足临床实时需求。

### 遥感图像处理

**RSMamba**（Chen et al., arXiv 2024）提出动态多路径激活机制，将输入序列复制为前向、反向与随机Shuffle三路径，通过共享参数Mamba建模并融合。该设计缓解了SSM对非因果图像数据的位置不敏感问题。在UC Merced等遥感分类数据集上，RSMamba显著优于CNN与Transformer基线。

**RS-Mamba**（扩展工作）进一步引入全向选择性扫描（OSSM），沿横、纵、斜及反斜八方向扫描图像，以捕获遥感场景中多方向大尺度空间特征，有效提升密集预测任务性能。

### 点云与视频分析

**PointMamba**（Liang et al., NeurIPS 2024）[openreview.net](https://openreview.net/forum?id=Kc37srXvan) 首次将Mamba应用于点云分析，利用空间填充曲线（如Hilbert曲线）将无序点云标记化为1D序列，再用非层次化Mamba编码器建模。在ModelNet40分类任务中，PointMamba以线性复杂度达到与Transformer相当的精度，同时显著降低GPU内存与FLOPs。

**MambaTrack**（arXiv 2024）[arxiv.org](https://arxiv.org/abs/2408.09178) 针对多目标跟踪中非线性运动建模难题，提出Mamba运动预测器（MTP）与轨迹补丁模块（TPM）。MTP用双Mamba编码层预测边界框偏移，TPM通过自回归修复遮挡轨迹。在DanceTrack与SportsMOT上，HOTA分别领先SOTA 2.2与近10个百分点。

**VFIMamba**（Zhang et al., arXiv 2024）为视频帧插值设计混合SSM块（MSB），通过交错排列相邻帧标记并应用多方向SSM建模。结合课程学习策略，VFIMamba在X-TEST的4K插值任务中PSNR提升0.80 dB，凸显其在高分辨率视频处理中的优势。

## 实验与评价总结

综合多篇工作，SSM在图像处理中展现出以下共性优势：（1）**计算效率显著优于Transformer**：在相近或更优性能下，FLOPs和内存占用大幅降低，尤其在高分辨率输入时优势放大；（2）**全局建模能力超越CNN**：有效感受野（ERF）可视化显示，MambaIR等模型可覆盖整图，而CNN与窗口注意力受限；（3）**硬件友好性突出**：Mamba的线性扫描机制利于GPU并行，训练/推理速度普遍快于Transformer；（4）**任务泛化性强**：从2D图像恢复到3D点云、从静态图像到动态视频，SSM均能有效适配。

但亦存在共性挑战：原始Mamba的因果性与位置不敏感性需针对性设计（如双向扫描、位置编码、非因果扩展）；在极低信噪比或纹理缺失场景（如严重水下退化），性能增益可能受限。

## 趋势与挑战

基于2025年前后的研究动态，可预测以下趋势：  
1. **多模态与跨域融合**：SSM将与视觉-语言模型（如CLIP）结合，用于图文生成、医学报告生成等任务，利用其高效序列建模能力处理多源异构数据。  
2. **3D与4D视觉扩展**：SSM在点云、NeRF、4D医学影像（3D+时间）中的应用将深化，需发展高效的3D选择性扫描与时空联合建模机制。  
3. **轻量化与边缘部署**：面向移动端与嵌入式设备，研究将聚焦Mamba的量化、剪枝与硬件定制（如NPU支持），推动实时视觉系统落地。  
4. **理论可解释性增强**：如何解释SSM的内部状态与特征选择机制，将成为提升模型可信度与可控性的关键方向。

## 结论

状态空间模型为图像处理提供了兼顾全局性、效率与可扩展性的新范式。从MambaIR到PointMamba，研究者通过针对性架构创新，成功将SSM适配于多样视觉任务，并在性能与效率上取得实质性突破。未来，随着多模态融合、3D建模与边缘计算需求的增长，SSM有望成为继CNN与Transformer之后的第三代视觉骨干网络基础。

## 参考文献

1. Gu, A., & Dao, T. (2023). Mamba: Linear-time sequence modeling with selective state spaces. *arXiv preprint arXiv:2312.00752*.  
2. Guo, H., et al. (2024). MambaIR: A Simple Baseline for Image Restoration with State-Space Model. *ECCV*. [ecva.net](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/2740_ECCV_2024_paper.php)  
3. Guo, H., et al. (2024). MambaIRv2: Attentive State Space Restoration. *arXiv preprint arXiv:2411.15269*. [arxiv.org](https://arxiv.org/abs/2411.15269)  
4. Guan, M., et al. (2024). WaterMamba: Visual State Space Model for Underwater Image Enhancement. *arXiv preprint arXiv:2405.08419*. [arxiv.org](https://arxiv.org/abs/2405.08419)  
5. Ding, J., et al. (2025). 融合邻域注意力和状态空间模型的医学视频分割算法. *电子与信息学报*, 47(5), 1582–1595. [jeit.ac.cn](https://jeit.ac.cn/cn/article/doi/10.11999/JEIT240755)  
6. Chen, K., et al. (2024). RSMamba: Remote Sensing Image Classification with State Space Model. *arXiv preprint arXiv:2403.19871*.  
7. Liang, D., et al. (2024). PointMamba: A Simple State Space Model for Point Cloud Analysis. *NeurIPS*. [openreview.net](https://openreview.net/forum?id=Kc37srXvan)  
8. Zhang, G., et al. (2024). VFIMamba: Video Frame Interpolation with State Space Models. *arXiv preprint arXiv:2407.01234*.  
9. Anonymous. (2024). MambaTrack: A Simple Baseline for Multiple Object Tracking with State Space Model. *arXiv preprint arXiv:2408.09178*. [arxiv.org](https://arxiv.org/abs/2408.09178)  
10. Liu, Y., et al. (2024). VMamba: Visual State Space Model. *NeurIPS*.  
11. Zhu, L., et al. (2024). Vision Mamba: Efficient Visual Representation Learning with Bidirectional State Space Model. *ICML*.  
12. Ma, J., et al. (2024). U-Mamba: Enhancing long-range dependency for biomedical image segmentation. *arXiv preprint arXiv:2401.04722*.