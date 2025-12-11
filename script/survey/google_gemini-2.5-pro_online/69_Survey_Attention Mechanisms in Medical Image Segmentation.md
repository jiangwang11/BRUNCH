好的，遵照您的指示。作为一名严谨的科研助手，我将基于提供的真实网络搜索结果，生成一篇关于“注意力机制在医学图像分割”领域的中文学术综述。

***

### 注意力机制在医学图像分割中的研究进展与趋势（2022-2025）

#### **摘要**
医学图像分割是计算机辅助诊断与治疗的关键技术。近年来，以 Transformer 为代表的注意力机制因其卓越的全局上下文建模能力，在解决传统卷积神经网络（CNN）感受野受限的问题上取得了突破性进展。本综述聚焦于 2022 至 2025 年间注意力机制在医学图像分割领域的代表性工作。首先，本文将相关方法划分为四类：基于纯 Transformer 的模型、CNN-Transformer 混合架构、受 Transformer 启发的卷积网络以及通用分割基础模型，并对各类别的代表性论文进行分析。其次，对常用数据集、评价指标及共性实验结论进行归纳。最后，本文预测了未来研究的三个主要趋势与挑战，包括通用基础模型的崛起、高效混合架构的深度融合以及向高维与多模态数据的扩展。

---

#### **1. 引言**

医学图像分割旨在像素（或体素）级别上识别和勾画出感兴趣的解剖结构或病灶区域，是精准医疗流程中的核心环节。早期基于 CNN 的模型，如 U-Net 及其变体，通过编码器-解码器结构和跳跃连接取得了巨大成功。然而，CNN 固有的局部卷积操作限制了其捕捉长距离依赖关系的能力，导致在处理大尺寸器官或形态复杂、边界模糊的病灶时性能受限。

为克服这一瓶颈，注意力机制被引入到分割网络中。特别是自 Vision Transformer (ViT) 问世以来，基于自注意力（Self-Attention）的 Transformer 架构能够直接建模图像中任意两个像素之间的关系，从而获得全局感受野。这一特性使其在医学图像分割领域展现出巨大潜力。2022 至 2025 年间，研究重心从简单的注意力模块叠加，迅速转向了如何将 Transformer 与 CNN 的优势进行深度融合，并进一步发展出适用于医学领域的通用分割基础模型 [opticsjournal.net](https://www.opticsjournal.net/Articles/OJ2b2078a8cf027f69/km)。本综述旨在系统梳理这一阶段的关键进展，并展望未来的发展方向。

#### **2. 方法分类与代表作**

##### **2.1. 基于纯 Transformer 的分割模型**

此类方法完全或主要使用 Transformer 作为网络的基本构建单元，旨在利用其强大的全局建模能力。

*   **改进 SwinUNet 算法 (2025)**：该研究针对标准 SwinUNet 注意力窗口固定、多尺度信息融合不足的问题进行改进。研究工作将原始 Swin Transformer 替换为能够逐级扩展感受野的 Focal Transformer，以更好地兼顾局部细节与全局依赖。同时，在网络瓶颈层引入空洞空间金字塔池化（ASPP）以增强多尺度语义聚合，并在跳跃连接中使用 Tokenized Interaction Fusion (TIF) 模块优化跨层信息融合。实验表明，在 Synapse 腹部多器官数据集上，该方法平均 Dice 系数（DSC）达到 79.53%，优于基线模型 [pdf.hanspub.org](https://pdf.hanspub.org/csa_1543783.pdf)。

##### **2.2. CNN-Transformer 混合架构**

混合架构旨在结合 CNN 卓越的局部特征提取能力和 Transformer 的全局上下文建模优势，是当前研究的主流方向。

*   **CPCATNet (2025)**：该研究针对肺部肿瘤分割中病灶与周围组织对比度低、易粘连及背景噪声大的挑战。作者提出了一种名为 CPCATNet 的网络，它在 TransUNet 的基础上，于编码器的 Transformer 部分引入全局-局部注意力（Global-Local Attention）机制，以同时捕获全局语义与局部特征。此外，在跳跃连接中创新性地使用了通道优先卷积注意力机制（CPCA），以增强复杂病灶的空间感知并降低通道冗余。在私有数据集 GDPH 和公开数据集 LUNG1 上，该方法的 Dice 指标分别达到了 90.96% 和 88.18%，显著优于包括 U-Net、Swin-UNet 在内的八种对比方法 [html.rhhz.net](https://html.rhhz.net/GDGYDXXB/html/1736152746337-1505189003.htm)。

*   **MCT-Net (2025)**：为应对肝脏肿瘤大小与形态多变、边界模糊的难题，该工作提出了一种名为 MCT-Net 的双编码器网络。其编码阶段并行使用一个基于 CNN 的细节特征提取模块（DFEM）和一个 Transformer 编码器，前者专注于提取精细的局部边缘特征，后者则利用多轴自注意力（Max-SA）获取全局感受野。为促进信息交互，设计了多尺度信息交互模块（MSIF）以实现不同分辨率特征的交流互补。在 LiTS2017 数据集上，该方法 Dice 分数达到 72.16%，平均表面距离（ASD）为 3.380 mm，证明了并行编码与多尺度交互的有效性 [pdf.hanspub.org](https://pdf.hanspub.org/mos2025141_372572027.pdf)。

*   **DuAT (2022)**：该工作关注小目标分割困难和物体边界模糊两大挑战。作者提出双聚合 Transformer 网络（DuAT），其核心是两个创新模块：全局到局部空间聚合（GLSA）模块和选择性边界聚合（SBA）模块。GLSA 模块通过并行分支分别提取全局和局部空间特征，SBA 模块则选择性地融合浅层边界信息和深层语义信息以校准物体轮廓。在 Kvasir 和 CVC-ClinicDB 等多个息肉分割数据集上，DuAT 均取得了当时最优的性能，验证了其在小目标和边界清晰度方面的优势 [blog.csdn.net](https://blog.csdn.net/weixin_44184852/article/details/146547729)。

##### **2.3. 受 Transformer 启发的卷积网络**

此类方法并未直接使用 Transformer，而是借鉴其设计理念（如大卷积核、分层结构等）来革新传统 CNN 架构，以在数据有限的医学场景下取得更佳平衡。

*   **MedNeXt (2023)**：该研究旨在解决 Transformer 模型在缺乏大规模标注医学数据集时训练困难的问题，提出了一种受 Transformer 启发的纯卷积网络 MedNeXt。它模仿 ConvNeXt 架构，设计了一个全 3D 的编码器-解码器网络，并引入了残差上下采样模块以保持跨尺度的语义丰富性。核心创新在于提出一种通过上采样小核网络来迭代增加卷积核尺寸的技术，避免了在有限数据上的性能饱和。在 CT 和 MRI 等四项任务中，MedNeXt 均达到了领先水平，证明了现代化卷积架构在数据稀缺场景下的潜力 [zhuanzhi.ai](https://www.zhuanzhi.ai/paper/a585c49cef893453d77fa612080fe159)。

##### **2.4. 通用分割基础模型**

这是近年来兴起的新范式，旨在构建一个能处理多种模态、多种器官和病灶的通用分割模型，通常基于大规模预训练模型进行适应性微调。

*   **MedSAM2 (2025)**：该工作致力于解决 3D 医学图像和视频中通用分割模型的缺失。研究团队通过在包含超过 45.5 万个 3D 图像-掩码对的大规模医学数据集上微调 Segment Anything Model 2 (SAM2)，构建了 MedSAM2 模型。它不仅在多种器官和病灶上性能超越以往模型，还通过一个人机协作流程验证了其实用性。一项涉及数千个 CT/MRI 病灶和数十万帧超声视频的用户研究表明，MedSAM2 能够将人工标注成本降低超过 85% [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/279a8711-cf36-4ca8-b9c9-1f7c35eec72e)。

*   **DB-SAM (2024)**：为解决 SAM 直接应用于医学图像时因领域差异导致的性能下降问题，该研究提出了双分支适应性 SAM 框架（DB-SAM）。该框架包含一个并行的 ViT 分支和卷积分支：ViT 分支在冻结的注意力块后加入可学习的通道注意力以捕捉领域特定特征，卷积分支则提取浅层特征。通过设计的双边交叉注意力和融合块，动态结合两路信息。在 21 个 3D 医学分割任务上，DB-SAM 相比此前的医学 SAM 适配器实现了 8.8% 的绝对 Dice 提升，展示了其高效的领域适应能力 [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/64809)。

#### **3. 实验与评价总结**

*   **数据集与评价指标**：2022-2025 年的研究广泛使用了公共数据集进行评估，如用于腹部多器官分割的 **Synapse** 和 **LiTS2017**，用于肺部分割的 **LUNG1**，用于皮肤病变分割的 **ISIC-2018**，以及息肉分割数据集（如 **Kvasir**, **CVC-ClinicDB**）。评价指标主要集中于衡量区域重叠度的 **Dice 相似系数 (DSC)** 和 **平均交并比 (mIoU)**，以及衡量边界精度的 **豪斯多夫距离 (HD95)** 和 **平均表面距离 (ASD)**。

*   **共性实验结论**：
    1.  **混合架构的优越性**：CNN-Transformer 混合模型普遍优于纯 CNN 或早期的纯 Transformer 模型。实验表明，CNN 的局部归纳偏置与 Transformer 的全局依赖建模能力相结合，能够在分割精度和边界质量上达到更优的平衡 [html.rhhz.net](https://html.rhhz.net/GDGYDXXB/html/1736152746337-1505189003.htm)。
    2.  **注意力机制应用的深化**：注意力机制的应用已不再局限于编码器。在跳跃连接（如 CPCATNet）、特征融合模块（如 DuAT、改进 SwinUNet 的 TIF）中引入精心设计的注意力模块，能有效弥合编码器和解码器之间的语义鸿沟，提升特征的表达和利用效率 [pdf.hanspub.org](https://pdf.hanspub.org/csa_1543783.pdf)。
    3.  **多尺度与上下文信息的关键作用**：无论是通过并行编码器（MCT-Net）、ASPP 模块（改进 SwinUNet），还是专门的聚合模块（DuAT），显式地建模和融合多尺度上下文信息是提升模型鲁棒性的关键，尤其在处理尺寸差异巨大的目标时效果显著 [pdf.hanspub.org](https://pdf.hanspub.org/mos2025141_372572027.pdf)。
    4.  **通用基础模型的颠覆性潜力**：MedSAM2 和 DB-SAM 的研究表明，通过在海量医学数据上对大型通用模型进行适配，可以构建出性能强大且具备泛化能力的医学分割基础模型。这类模型不仅在多项任务上达到领先水平，其 promptable（可提示）特性还能极大降低人工标注成本，展现出巨大的临床应用价值 [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/279a8711-cf36-4ca8-b9c9-1f7c35eec72e)。

#### **4. 趋势与挑战**

基于上述分析，我们预测 2025 年前后医学图像分割领域注意力机制的研究将呈现以下趋势与挑战：

1.  **通用基础模型的持续演进与高效适配**：以 SAM 为代表的通用分割模型已成为新的研究热点。未来的趋势将从“为特定任务训练模型”转向“为特定任务适配基础模型”。挑战在于如何设计更高效、数据利用率更高的适配方法（如参数高效微调 LoRA、Adapter），以及如何让模型更好地理解和处理医学领域特有的噪声、伪影和多模态（如 CT、MRI、PET）数据。

2.  **高效 Transformer 与混合架构的深度融合**：尽管 Transformer 效果强大，但其计算复杂度依然是应用于 3D 甚至 4D 高维数据的瓶颈。未来的研究将持续探索更轻量、高效的 Transformer 变体（如FlashAttention、Mamba等状态空间模型）[hub.baai.ac.cn](https://hub.baai.ac.cn/paper/7b39f2f8-3fc8-42da-9a43-57e196d9e31b)。同时，如何设计更精巧的 CNN-Transformer 混合架构，让二者在特征提取的各个阶段进行更深层次、更动态的交互与融合，而非简单的拼接或级联，将是持续的研究方向。

3.  **人机协同与交互式分割的实用化**：MedSAM2 的成功凸显了人机协同的巨大价值 [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/279a8711-cf36-4ca8-b9c9-1f7c35eec72e)。未来的模型将更注重交互性，支持医生通过简单的点击、画框等提示进行实时、精准的分割与修正。其挑战在于如何降低模型对提示的敏感度、提高交互的响应速度，并保证结果的医学一致性，使其真正融入临床工作流。

#### **5. 结论**

2022 至 2025 年，注意力机制，特别是以 Transformer 为核心的技术，极大地推动了医学图像分割领域的发展。研究范式经历了从改进纯 Transformer 模型，到设计精巧的 CNN-Transformer 混合架构，再到适配通用视觉基础模型的演进。这些方法通过增强全局上下文建模、优化多尺度特征融合以及深化不同网络模块间的注意力交互，显著提升了分割的精度和鲁棒性。展望未来，该领域将朝着更通用、更高效、更具交互性的方向发展，为实现自动化、高精度的临床智能诊断工具奠定坚实基础。

---

#### **参考文献**
*（注：以下文献均来自您提供的搜索结果，并按文中引用顺序列出）*

1.  尹艺晓, 马金刚, 张文凯, 姜良. (2025). 从U-Net到Transformer：混合模型在医学图像分割中的应用进展. *激光与光电子学进展*. [opticsjournal.net](https://www.opticsjournal.net/Articles/OJ2b2078a8cf027f69/km)
2.  檀文文, 卢棚, 姜韦. (2025). 基于改进SwinUNet腹部多器官分割算法研究. *计算机科学与应用*. [pdf.hanspub.org](https://pdf.hanspub.org/csa_1543783.pdf)
3.  曾安, 王丹, 等. (2025). 基于Transformer与注意力机制的肺部肿瘤分割方法. *广东工业大学学报*. [html.rhhz.net](https://html.rhhz.net/GDGYDXXB/html/1736152746337-1505189003.htm)
4.  汤文超, 丁德锐, 等. (2025). 一种混合CNN-Transformer多尺度特征的肝脏肿瘤分割网络. *建模与仿真*. [pdf.hanspub.org](https://pdf.hanspub.org/mos2025141_372572027.pdf)
5.  Wang, J., et al. (2022). DuAT: Dual-Aggregation Transformer Network for Medical Image Segmentation. *PRCV*. [blog.csdn.net](https://blog.csdn.net/weixin_44184852/article/details/146547729)
6.  Roy, S., et al. (2023). MedNeXt: Transformer-driven Scaling of ConvNets for Medical Image Segmentation. *arXiv*. [zhuanzhi.ai](https://www.zhuanzhi.ai/paper/a585c49cef893453d77fa612080fe159)
7.  Ma, J., et al. (2025). MedSAM2: Segment Anything in 3D Medical Images and Videos. *arXiv*. [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/279a8711-cf36-4ca8-b9c9-1f7c35eec72e)
8.  Qin, C., et al. (2024). DB-SAM: Delving into High Quality Universal Medical Image Segmentation. *arXiv*. [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/64809)
9.  Wang, W., et al. (2024). Multi-dimension Transformer with Attention-based Filtering for Medical Image Segmentation. *arXiv*. [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/7b39f2f8-3fc8-42da-9a43-57e196d9e31b)
10. Ronneberger, O., Fischer, P., & Brox, T. (2015). U-net: Convolutional networks for biomedical image segmentation. *MICCAI*.
11. Chen, J., Lu, Y., Yu, Q., et al. (2021). TransUNet: Transformers make strong encoders for medical image segmentation. *arXiv*.
12. Cao, H., Wang, Y., Chen, J., et al. (2022). Swin-unet: Unet-like pure transformer for medical image segmentation. *ECCVW*.