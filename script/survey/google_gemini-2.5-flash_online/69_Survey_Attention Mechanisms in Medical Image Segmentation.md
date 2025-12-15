## 注意力机制在医学图像分割中的应用进展 (2022-2025)

### 引言

医学图像分割是临床诊断、治疗规划及预后评估中的关键技术。然而，医学影像固有的低对比度、模糊边界、复杂多样的器官结构及病灶形态，使得精确、鲁棒的自动分割极具挑战性。近年来，深度学习在医学图像分割领域取得了显著进展，其中注意力机制作为一种提升模型特征表达能力的关键技术，受到研究者广泛关注。通过引导模型关注图像中的重要区域并抑制不相关信息，注意力机制有效提升了模型对长距离依赖建模及局部细节捕捉的能力。本文将综述2022年至2025年间注意力机制在医学图像分割中的代表性工作，并探讨其发展趋势与挑战。

### 方法分类与代表作

本综述将注意力机制在医学图像分割中的应用分为以下几类：基于U-Net架构的注意力改进、基于Transformer的注意力机制、以及混合型CNN-Transformer架构中的注意力融合。

#### 1. 基于U-Net架构的注意力改进

传统的U-Net模型在医学图像分割中表现出色，但其跳跃连接通常采用简单的特征拼接，可能导致语义鸿沟和冗余信息。注意力机制的引入旨在优化U-Net的特征融合过程，使其更聚焦于有效信息。

*   **Attention U-Net系列 (2022)**: [opticsjournal.net](https://www.opticsjournal.net/Articles/OJec746e5b1671dd9e/Abstract)
    *   该类工作旨在通过在U-Net的跳跃连接中引入注意力门控机制，使模型能够自动识别和突出与分割任务相关的区域，抑制不相关背景的特征传递。例如，一些改进模型提出了跨模态多编码混合注意力U-Net用于肺部肿瘤分割。
    *   核心方法是在编码器-解码器连接处加入可学习的注意力模块，通过权重分配使解码器更侧重于从编码器传递过来的关键特征。
    *   研究结论显示此类方法能够提升模型对感兴趣区域的敏感性，尤其在处理边界模糊和目标形状复杂的任务时。
    *   实验结果通常通过Dice系数和Hausdorff距离来评估，证明了其在多种医学图像分割任务中的有效性。

#### 2. 基于Transformer的注意力机制

Transformer模型以其强大的长距离依赖建模能力在自然语言处理领域取得巨大成功后，逐渐被引入图像领域。其自注意力机制使其能够捕捉全局上下文信息，弥补了CNN在全局建模上的不足。

*   **UNETR及其变体 (2022-2025)**: [html.rhhz.net](https://html.rhhz.net/GDGYDXXB/html/1736152746337-1505189003.htm)
    *   **研究问题**: 传统CNN难以捕捉图像的全局依赖关系，且Transformer模型在局部细节建模上存在不足。
    *   **核心方法**: UNETR以Transformer作为编码器，利用其多头自注意力机制捕捉全局多尺度信息，再结合CNN解码器进行像素级分割。例如，[html.rhhz.net](https://html.rhhz.net/GDGYDXXB/html/1736152746337-1505189003.htm)中的工作引入了Global-Local注意力机制，使网络同时关注全局和局部上下文信息。
    *   **关键实验结论**: 在肺部肿瘤分割任务中，此类模型在Dice指标上表现出色，相较于纯CNN模型取得了显著提升，为临床诊疗提供了可靠辅助。
*   **MDT-AF (Multi-dimension Transformer with Attention-based Filtering) (2024)**: [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/7b39f2f8-3fc8-42da-9a43-57e196d9e31b)
    *   **研究问题**: 医学图像分割中存在的低信噪比以及通道和空间信息利用不足问题。
    *   **核心方法**: 该方法在Transformer中融入了基于注意力的特征过滤机制，并扩展了自注意力机制以包含空间和通道维度，同时引入交互机制来增强特征聚合。其采用粗到细的过程缓解低信噪比影响。
    *   **关键实验结论**: 在三个公共医学图像分割基准测试中实现了领先的性能，通过改进块嵌入和自注意力机制有效解决了低信噪比的挑战。

#### 3. 混合型CNN-Transformer架构中的注意力融合

为了兼顾CNN的局部特征提取优势和Transformer的全局上下文建模能力，混合型模型成为当前研究热点。注意力机制在这些混合架构中扮演着关键角色，用于引导不同模态特征的有效融合。

*   **DuAT (Dual-Aggregation Transformer Network) (2025)**: [blog.csdn.net](https://blog.csdn.net/weixin_44184852/article/details/146547729)
    *   **研究问题**: 纯Transformer模型在捕捉长距离依赖时可能丢失局部细节，导致小物体的预测过于平滑和边界模糊。
    *   **核心方法**: DuAT提出双聚合模块，包括全局到局部空间聚合（GLSA）模块和选择性边界聚合（SBA）模块。GLSA结合局部和全局特征，SBA则用于增强边界信息并重新校准对象。
    *   **关键实验结论**: 在多个息肉、皮肤病变和显微图像数据集上实现了最先进的性能，解决了小目标分割和边界模糊问题，展现了更强的泛化能力。
*   **SwinUNet及其改进 (2025)**: [pdf.hanspub.org](https://pdf.hanspub.org/csa_1543783.pdf), [opticsjournal.net](https://www.opticsjournal.net/Articles/OJ2b2078a8cf027f69/km)
    *   **研究问题**: SwinUNet存在全局上下文建模不足和多尺度特征表达有限的问题，尤其是窗口注意力机制难以兼顾长距离依赖与局部细节。
    *   **核心方法**: 檀文文等人在SwinUNet中首先用Focal Transformer替换Swin Transformer增强局部细节和全局依赖建模。其次，在编码器末端引入ASPP结构扩展感受野并提升多尺度特征表达。最后，在跳跃连接中加入TIF（Tokenized Interaction Fusion）模块实现语义与空间信息的高效融合。
    *   **关键实验结论**: 在Synapse腹部器官数据集上，该改进方法在平均Dice和Hausdorff距离等指标上均优于基线模型，验证了其在腹部多器官分割中的有效性。
*   **MCT-Net (Mix CNN-Transformer Multi-scale Feature Network) (2025)**: [pdf.hanspub.org](https://pdf.hanspub.org/mos2025141_372572027.pdf)
    *   **研究问题**: 肝脏肿瘤分割面临界限模糊、大小和形状可变性等挑战，以及单一尺度特征提取难以捕捉全局信息和精细细节。
    *   **核心方法**: MCT-Net采用双编码器融合多尺度特征，结合DFEM细节特征提取模块、Transformer编码器（引入Max-SA多轴自注意力）、局部空间注意力模块（LAM）和全局空间注意力模块（GAM）。解码器通过多尺度信息交互模块（MSIF）实现高低分辨率特征的互补。
    *   **关键实验结论**: 在LiTS2017和3D-IRCADb数据集上，Dice和ASD等评价指标均优于其他方法，尤其在处理复杂边界和多变形态的肿瘤时展现出良好性能和泛化能力。

### 实验与评价总结

2022-2025年间的工作普遍采用Dice相似系数（DSC）、Hausdorff距离（HD/HD95）、平均交并比（mIoU）和平均绝对误差（MAE）等指标来评估模型性能。这些研究的共同发现是，引入注意力机制和Transformer结构能够有效提升医学图像分割的准确性和鲁棒性。具体体现在：

1.  **全局上下文建模能力增强**: Transformer结构及其自注意力机制显著提升了模型捕获长距离依赖和全局语义信息的能力。
2.  **局部细节捕捉优化**: 结合如焦点注意力、多轴自注意力等机制，模型在保持全局视野的同时，能更精细地处理图像的局部细节，尤其对于边界模糊和小目标分割具有重要意义。
3.  **多尺度特征融合改进**: 通过注意力模块或Tokenized Interaction Fusion (TIF) 等机制，不同层级、不同尺度的特征得以更有效地交互和融合，减少了语义鸿沟和冗余信息。
4.  **对复杂病灶的适应性增强**: 针对肿瘤形态多变、对比度低等问题，引入注意力机制的模型表现出更强的自适应性。
5.  **泛化能力提升**: 在不同数据集上的交叉验证或未见数据集上的测试表明，这些改进后的模型具有较好的泛化能力。

### 趋势与挑战

**趋势预测：**

1.  **3D/4D Transformer模型的普及与优化**: 随着计算资源的增长，基于Transformer的3D/4D医学图像分割模型将成为主流，特别是针对医疗影像序列（如CT、MRI序列、超声视频）中时间或层间连续性的建模。例如，MedSAM2 [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/279a8711-cf36-4ca8-b9c9-1f7c35eec72e)作为3D医学图像和视频分割的基础模型，预示了这一方向。
2.  **多模态融合与跨任务注意力**: 未来的研究将更加注重如何有效整合CT、MRI、PET等多种模态的医学图像信息，注意力机制将用于学习不同模态之间的互补关系。同时，注意力机制也将被应用于多任务学习（如分割、分类、疾病检测），以实现知识共享和模型协同。
3.  **轻量化与可解释性并重**: 面对临床应用对实时性和计算效率的要求，如何在保持高性能的同时设计更轻量化的注意力机制和模型结构将是重要方向（如MCT-Net的Max-SA）。此外，提高注意力机制的可解释性，让医生更好地理解模型决策过程，将是提升其临床接受度的关键。

**挑战：**

1.  **数据稀缺与标注成本**: 大规模、高质量的医学图像标注数据依然稀缺，限制了深度学习，尤其是数据饥渴型Transformer模型的训练。如何通过自监督学习、半监督学习或更高效的数据增强策略来克服这一挑战至关重要。
2.  **计算资源与部署限制**: Transformer模型通常参数量庞大，计算复杂度高，在边缘设备或资源受限的临床环境中部署仍面临挑战。
3.  **小目标与模糊边界的精细分割**: 尽管已有显著进步，但对于微小病灶、结构复杂且边界极度模糊的区域，实现像素级的高精度分割仍是难题。

### 结论

注意力机制与Transformer模型在2022-2025年间显著推动了医学图像分割技术的发展。从早期基于U-Net的注意力门控到全Transformer编码器，再到融合CNN和Transformer优势的混合架构，注意力机制始终是提升模型性能的核心。未来的研究将聚焦于3D/4D多模态数据、轻量化与可解释性，并持续应对数据稀缺、计算成本高以及小目标精细分割等固有挑战。

### 参考文献

1.  尹艺晓, 马金刚, 张文凯, 姜良. 从U-Net到Transformer：混合模型在医学图像分割中的应用进展. 激光与光电子学进展, 2025, 62(2): 0200001. [opticsjournal.net](https://www.opticsjournal.net/Articles/OJ2b2078a8cf027f69/km)
2.  檀文文, 卢棚, 姜韦. 基于改进SwinUNet腹部多器官分割算法研究. 计算机科学与应用, 2025, 15(10): 318-326. [pdf.hanspub.org](https://pdf.hanspub.org/csa_1543783.pdf)
3.  曾安, 王丹, 杨宝瑶, 张小波, 石镇维, 刘再毅, 潘丹. 基于Transformer与注意力机制的肺部肿瘤分割方法. 广东工业大学学报, 2025, 42(1): 24-32. [html.rhhz.net](https://html.rhhz.net/GDGYDXXB/html/1736152746337-1505189003.htm)
4.  Wang, Wentao, et al. Multi-dimension Transformer with Attention-based Filtering for Medical Image Segmentation. 2024. [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/7b39f2f8-3fc8-42da-9a43-57e196d9e31b)
5.  DuAT: Dual-Aggregation Transformer Network for Medical Image Segmentation. PRCV 2022. [blog.csdn.net](https://blog.csdn.net/weixin_44184852/article/details/146547729)
6.  汤文超, 丁德锐, 袁浩成, 刘华卿. 一种混合CNN-Transformer多尺度特征的肝脏肿瘤分割网络. 建模与仿真, 2025, 14(1): 388-403. [pdf.hanspub.org](https://pdf.hanspub.org/mos2025141_372572027.pdf)
7.  Perspective+ Unet: Enhancing Segmentation with Bi-Path Fusion and Efficient Non-Local Attention. Medical Image Computing and Computer Assisted Intervention – MICCAI 2024. [blog.csdn.net](https://blog.csdn.net/qq_42735631/article/details/152309320)
8.  Ma, Jun, et al. MedSAM2: Segment Anything in 3D Medical Images and Videos. 2025. [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/279a8711-cf36-4ca8-b9c9-1f7c35eec72e)
9.  Roy, Saikat, et al. MedNeXt: Transformer-driven Scaling of ConvNets for Medical Image Segmentation. 2023. [zhuanzhi.ai](https://www.zhuanzhi.ai/paper/a585c49cef893453d77fa612080fe159)
10. MC-Net: Multi-scale Context-Attention Network for Medical CT Image Segmentation. Applied Intelligence, 2021. [blog.csdn.net](https://blog.csdn.net/Acmer_future_victor/article/details/121335624)
11. Chen, J., Lu, Y., Yu, Q., et al. TransUNet: Transformers Make Strong Encoders for Medical Image Segmentation. arXiv: 2102.04306.
12. Oktay, O., Schlemper, J., Folgoc, L.L., et al. Attention U-Net: Learning Where to Look for the Pancreas. arXiv: 1804.03999.