## 深度学习在生物医学图像分割中的应用综述 (2022–2025)

### 引言

生物医学图像分割是医学影像分析中的关键步骤，旨在精确识别和勾勒出图像中的器官、病灶或细胞结构，为疾病诊断、治疗规划和预后评估提供定量依据。传统的图像分割方法往往依赖人工特征或简单的图像处理技术，难以应对生物医学图像固有的复杂性，如低对比度、边界模糊、形态变异大等问题。近年来，随着深度学习技术的飞速发展，卷积神经网络（CNNs）和 Transformer 模型在图像分割任务中展现出卓越性能，极大地推动了生物医学图像分割的进步。本综述旨在回顾 2022 年至 2025 年间深度学习在生物医学图像分割领域的代表性工作，重点关注各种新兴方法、混合模型以及基础大模型的发展，并展望未来的研究趋势与挑战。

### 方法分类与代表作

本节将深度学习在生物医学图像分割中的应用方法分为以下几类，并介绍其代表性工作：

#### 1. 基于 Transformer 的模型

Transformer 模型凭借其强大的全局特征捕获能力，在医学图像分割领域取得了显著进展，尤其在处理长程依赖关系方面表现优异。

*   **SwinUNet 及其改进型**
    *   **研究问题**：医学图像分割中全局上下文建模不足与多尺度特征表达有限。
    *   **核心方法**：檀文文等 [hanspub.org (1)](https://pdf.hanspub.org/csa_1543783.pdf) 提出改进型 SwinUNet。该方法用 Focal Transformer 替换原始 Swin Transformer 以增强局部细节和全局依赖建模，并在编码器末端引入空洞空间金字塔池化 (ASPP) 模块扩展感受野和提升多尺度特征表达。此外，在跳跃连接中引入 Tokenized Interaction Fusion (TIF) 模块，实现跨层语义与空间信息的有效融合。
    *   **关键实验结论**：在 Synapse 腹部器官数据集上，该方法在平均 Dice 系数和 Hausdorff 距离等指标上均优于基线模型 SwinUNet。
    *   **研究问题**: 传统 U-Net 结构在医学图像分割中难以捕捉全局依赖关系。
    *   **核心方法**: 姜良等 [opticsjournal.net (1)](https://www.opticsjournal.net/Articles/OJ2b2078a8cf027f69/km) 讨论了从 U-Net 到 Transformer 的演进，重点关注混合模型。SwinUNet 将 Swin Transformer 嵌入 U-Net 架构中，有效建模多尺度图像特征。
    *   **关键实验结论**: SwinUNet 在全局建模和分割精度方面优于传统卷积模型，但仍存在注意力机制窗口固定、多尺度语义聚合不足以及跳跃连接信息融合不充分的问题。

*   **VMamba-CNN 混合模型 (VMDC-Unet)**
    *   **研究问题**：传统方法在结直肠癌病理切片图像分割中，肿瘤异质性、复杂背景及模糊边界导致分割精度不足，现有 CNN 和 Transformer 模型在长范围依赖和局部细节捕获方面存在局限。
    *   **核心方法**：王劭羽等 [hanspub.org (2)](https://www.hanspub.org/journal/paperinformation?paperid=112526) 提出 VMDC-Unet，融合 VMamba 的长距离依赖处理能力和 CNN 的局部特征提取优势。通过改进 ConvNext 模块增强细粒度特征提取，并设计局部自注意力机制优化跳跃连接的特征融合效率。
    *   **关键实验结论**：在 SJTU_GSFPH 和 Glas 结直肠癌数据集上，VMDC-Unet 的分割精度和泛化能力明显优于其他基准模型，并在参数量相对较高的情况下实现了较低的浮点运算次数。

*   **C$^2$ Transformer U-Net**
    *   **研究问题**：跨模态医学图像可以提供更丰富的病灶语义信息，但传统 U-Net 主要使用单模态图像，未能充分利用跨模态和上下文语义相关性。
    *   **核心方法**：周涛等 [jeit.ac.cn](https://jeit.ac.cn/cn/article/doi/10.11999/JEIT220445?viewType=HTML) 提出 C$^2$ Transformer U-Net 模型。该模型在编码器部分设计主干和辅助 U-Net 结构提取不同模态语义信息，通过多模态上下文语义感知处理器 (MCAP) 有效融合同一病灶的跨模态语义信息。在编-解码器中采用预激活残差单元和 Transformer 架构，以提取上下文特征并增强对病灶位置信息的关注。
    *   **关键实验结论**：在临床多模态肺部医学图像数据集上的实验表明，该模型在 Acc、Pre、Recall、Dice 等指标上显著优于现有先进方法，对形状复杂肺部病灶的分割具有较高精度和较低冗余度。

#### 2. 基础大模型 (Foundation Models)

基础大模型旨在通过大规模数据预训练，实现通用化的图像分割能力，从而减少对特定任务标注数据的依赖。

*   **Segment Anything Model (SAM) 及其医学应用**
    *   **研究问题**：SAM 在自然图像分割中表现优异，但因训练数据中缺少医学图像、医学图像边缘模糊且任务差异大，直接应用于医学图像分割效果不理想。
    *   **核心方法**：姚劲草等 [opticsjournal.net (2)](https://www.opticsjournal.net/Articles/OJda3bfaa1dd74a3a/FullText) 综述了 SAM 在医学图像分割中的应用进展。研究重点关注微调 SAM 以适应医学数据集（如 Skin-SAM, Polyp-SAM, MedSAM, SAM-Med2D）、SAM 对 3D 医学图像的适应性（如 3DSAM-adapter, SAM3D-adapter, SAM3D, SAM-Med3D, SegVol, MedLSAM），以及提示工程的优化（如 AutoSAM, DeSAM, SAC）。
    *   **关键实验结论**：通过在乳腺肿瘤和孕妇骨盆数据集上的实验验证，经过大规模数据集微调的 SAM 具有更强的泛化能力。SAM 结合半监督网络生成高质量伪标签可有效提高分割效果。MedSAM 在多种医学图像分割任务中显著优于 U-Net，展现出更好的泛化能力。

*   **MedSAM2: Segment Anything in 3D Medical Images and Videos**
    *   **研究问题**：缺乏针对 3D 医学图像和视频的高效通用分割模型，尤其在结合用户交互和大规模标注研究方面。
    *   **核心方法**：Jun Ma 等 [baai.ac.cn](https://hub.baai.ac.cn/paper/279a8711-cf36-4ca8-b9c9-1f7c35eec72e) 提出了 MedSAM2，通过在包含超过 45.5 万对 3D 图像-掩码和 7.6 万帧的大规模医学数据集上微调 Segment Anything Model 2。该模型引入人机协作流程，以优化性能和效率。
    *   **关键实验结论**：MedSAM2 在多种器官、病灶和成像模态上性能优于先前模型，且在用户研究中显示可将人工标注成本降低超过 85%，表明其在实现高效、可扩展且高质量分割任务方面的潜力。

*   **DB-SAM: Delving into High Quality Universal Medical Image Segmentation**
    *   **研究问题**：Segment Anything Model (SAM) 在自然图像中表现良好，但在通用医学图像分割中存在显著性能差异，主要源于自然数据与 2D/3D 医学数据之间的领域差距。
    *   **核心方法**：Chao Qin 等 [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/64809) 提出双分支适应性 SAM 框架 DB-SAM，旨在弥合领域差距。该模型包含一个 ViT 分支 (在每个冻结注意力块后引入可学习通道注意力块捕获领域特定局部特征) 和一个卷积分支 (采用轻量级卷积块提取领域特定浅层特征)。设计双边交叉注意力块和 ViT 卷积融合块动态结合两分支信息。
    *   **关键实验结论**：在涵盖 21 个 3D 医学图像分割任务的大规模数据集上，DB-SAM 相比最新医学 SAM 适配器实现了 8.8% 的性能提升。

#### 3. CNN 结构优化与增强

尽管 Transformer 模型日益兴起，但 CNN 及其变种仍在医学图像分割中发挥着重要作用，通过结构创新、注意力机制和多尺度融合等手段提升性能。

*   **DeepLab 和可变形卷积**
    *   **研究问题**：肝脏病理图像分割面临多尺度特征建模不足、标注数据稀缺及复杂边界分割精度受限的问题，现有研究多集中于单一病灶识别，缺乏对肝脏整体病理微环境的系统性定量评估。
    *   **核心方法**：李振勇等 [hanspub.org](https://pdf.hanspub.org/csa_1543657.pdf) 提出融合自监督学习与可变形卷积的改进型 DeepLab v3+ 模型。通过 DINO 自监督学习框架对 ResNet-50 进行病理图像预训练，以缓解模型对大规模标注数据的依赖。在 DeepLab v3+ 的 ASPP 模块中集成可变形卷积，通过动态调整感受野实现局部细节与全局语义信息的自适应融合，并结合特征精修模块优化亚微米级边界分割。
    *   **关键实验结论**：在仅需少量标注数据的情况下，该改进模型在肝实质区域分割精度达到 0.84 (IoU) 和 0.90 (Dice)，显著优于传统 U-Net 与原始 DeepLab v3+，炎性细胞核分割指标提升 11%~16%。

*   **Perspective+ Unet**
    *   **研究问题**：3D 医学图像分割中，现有 CNN 模型难以捕获长距离空间关系，而全局注意力机制计算成本高昂且可能引入噪声，导致全局和局部信息捕获存在局限性。
    *   **核心方法**：Perspective+ Unet [blog.csdn.net](https://blog.csdn.net/qq_42735631/article/details/152309320) 设计了双路径编码器策略（融合标准卷积和膨胀卷积），旨在平衡全局与局部信息的处理。同时，引入高效非局部变换器（ENLTB）利用核函数近似技术实现长距离依赖的线性计算，并通过空间跨尺度集成器（SCSI）融合不同层级的全局依赖和局部信息。
    *   **关键实验结论**：在 ACDC 和 Synapse 数据集上，该方法在 Dice 系数和 Hausdorff 距离等指标上均表现出优异性能，有效增强了感受野和捕获全局依赖。

### 实验与评价总结

综观 2022-2025 年的代表性工作，生物医学图像分割领域在评估模型性能时普遍采用 Dice 相似系数 (Dice, DSC) 和 Hausdorff 距离 (HD, HD95) 作为核心指标，并辅以平均交并比 (IoU, mIoU) 和准确率 (Acc, Pre, Recall) 等。这些指标能够从重叠程度、边界精度和像素分类准确性等方面全面衡量分割效果。

*   **Transformer 模型的优势**: 基于 Transformer 的模型如 SwinUNet 及其变种 (Focal Transformer)、VMamba-CNN 混合模型和 C$^2$ Transformer U-Net，在处理全局上下文信息和长距离依赖方面表现出显著优势。它们能够提升复杂器官或病灶的整体建模能力，并在 Dice 和 HD 等指标上均超越了传统的纯 CNN 模型。这种提升尤其体现在处理具有复杂形态和模糊边界的结构时。
*   **基础大模型的潜力**: SAM 及其医学特化版本 (MedSAM, MedSAM2, DB-SAM) 通过在海量数据集上的预训练和微调，展现出强大的泛化能力和零样本学习潜力。MedSAM2 在 3D 医学图像和视频分割中能够显著降低人工标注成本。DB-SAM 通过结合 ViT 和卷积分支，有效弥合自然图像与医学图像的领域差距。这些模型在多种模态和任务中均取得了超越传统方法的性能，尤其在减少标注依赖和实现高效分割方面具有颠覆性意义。
*   **CNN 结构优化的持续价值**: 传统的 CNN 结构并未被完全取代，而是通过引入可变形卷积 (如 DeepLab v3+ 结合可变形卷积) 和精巧的模块设计 (如 Perspective+ Unet 的双路径编码器和高效非局部变换器) 持续提升。这些方法在局部细节捕获、多尺度特征融合方面依然强大，并在特定任务中（如病理图像的亚微米级边界分割）展现出卓越表现。

总的来说，各类深度学习模型在生物医学图像分割中均取得了显著进步。Transformer 模型擅长全局信息处理，基础大模型具备普适性和少样本学习能力，而优化后的 CNN 结构则在局部细节和计算效率上保持优势。许多研究通过结合不同模型的优点（例如混合模型）来进一步提升性能，证明了集成学习在复杂医学图像分割任务中的有效性。

### 趋势与挑战

2025 年前后，生物医学图像分割领域呈现以下真实研究趋势：

1.  **基础大模型 (Foundation Models) 的通用化和特化发展**：随着 MedSAM2 和 DB-SAM 等模型的发展，基础大模型将持续推动医学图像分割向更通用、少样本学习方向迈进。未来的研究趋势在于进一步提升这些模型在多模态、多任务场景下的零/少样本性能，减少对海量标注数据的依赖。同时，将出现更多针对特定医学领域（如放射学、病理学）的特化型基础模型，通过引入领域知识和专门的模块设计，在保持通用能力的同时提升特定任务的精度和鲁棒性。例如，针对 3D 医学图像的自监督预训练策略和轻量化 3D 转换方法将是重要研究方向。

2.  **混合模型与多尺度/多模态信息深度融合**：Transformer 和 CNN 的优势互补将催生更多高效的混合模型。未来的研究将不再是简单地将两者堆叠，而是探索更深层次的融合机制，以更好地整合不同模型的优点。例如，Focal Transformer、VMamba-CNN 混合模型和 Perspective+ Unet 展示了局部与全局、低层与高层特征的精细融合。此外，如何有效融合来自不同医学成像模态（如 CT、MRI、超声等）的信息，以及如何处理不同尺度的病灶和结构，将是实现更全面、更精确分割的关键。这将涉及跨模态注意力机制、图神经网络等前沿技术。

3.  **计算效率与模型部署优化**：随着模型复杂度和数据规模的增加，计算成本和模型部署的便捷性成为实际应用中的重要挑战。未来的研究将更关注参数高效微调 (PEFT) 策略，如 LoRA 的应用，以及模型轻量化和推理加速技术。在保证分割精度的前提下，探索如何开发低计算资源消耗的模型，使其能够部署到边缘设备或临床工作站进行实时处理，是推动深度学习医学图像分割技术走向临床落地的关键。同时，对模型的可解释性和鲁棒性验证也将是重点，确保模型在真实临床场景中的可靠性。

### 结论

综上所述，2022 年至 2025 年间，深度学习在生物医学图像分割领域取得了显著进展。从结合 CNN 和 Transformer 优势的混合模型，到以 SAM 为代表的基础大模型，再到对传统 CNN 结构的精细优化，各项技术持续突破，有效提升了医学图像分割的精度、效率和泛化能力。然而，该领域仍面临诸多挑战，包括基础大模型的通用化和特化平衡、多模态多尺度信息的深度融合，以及模型计算效率和临床部署的优化。未来的研究将持续围绕这些方向展开，旨在开发更智能、更鲁棒、更具临床应用价值的生物医学图像分割技术，从而最终造福患者。

### 参考文献

1.  檀文文, 卢棚, 姜韦. 基于改进SwinUNet腹部多器官分割算法研究. 计算机科学与应用, 2025, 15(10): 318-326. [pdf.hanspub.org (1)](https://pdf.hanspub.org/csa_1543783.pdf)
2.  王劭羽, 陈庆奎, 黄陈. 基于VMamba-CNN混合的结直肠癌切片图像分割. 建模与仿真, 2025, 14(4): 799-810. [hanspub.org (2)](https://www.hanspub.org/journal/paperinformation?paperid=112526)
3.  李振勇, 刘艺, 柯宇晨, 廖俊. 基于DeepLab和可变形卷积的肝脏病理环境分割方法. 计算机科学与应用, 2025, 15(6): 157-167. [pdf.hanspub.org (2)](https://pdf.hanspub.org/csa_1543657.pdf)
4.  周涛, 侯森宝, 陆惠玲, 刘赟璨, 党培. C2 Transformer U-Net：面向跨模态和上下文语义的医学图像分割模型. 电子与信息学报, 2023, 45(5): 1807-1816. [jeit.ac.cn](https://jeit.ac.cn/cn/article/doi/10.11999/JEIT220445?viewType=HTML)
5.  Jun Ma, Zongxin Yang, Sumin Kim, et al. MedSAM2: Segment Anything in 3D Medical Images and Videos. 2025. [baai.ac.cn](https://hub.baai.ac.cn/paper/279a8711-cf36-4ca8-b9c9-1f7c35eec72e)
6.  Chao Qin, Jiale Cao, Huazhu Fu, Fahad Shahbaz Khan, Rao Muhammad Anwer. DB-SAM: Delving into High Quality Universal Medical Image Segmentation. 2024. [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/64809)
7.  姜良. 从U-Net到Transformer：混合模型在医学图像分割中的应用进展. 激光与光电子学进展, 2025, 62(2): 0200001. [opticsjournal.net (1)](https://www.opticsjournal.net/Articles/OJ2b2078a8cf027f69/km)
8.  姚劲草. 分割一切模型（SAM）在医学图像分割中的应用. 中国激光, 2024, 51(21): 2107102. [opticsjournal.net (2)](https://www.opticsjournal.net/Articles/OJda3bfaa1dd74a3a/FullText)
9.  Perspective+ Unet: Enhancing Segmentation with Bi-Path Fusion and Efficient Non-Local Attentio. Medical Image Computing and Computer Assisted Intervention – MICCAI 2024. [blog.csdn.net](https://blog.csdn.net/qq_42735631/article/details/152309320)
10. Shi Jun, Wang Tiantong, Zhu Ziqi, Zhao Minfan, Wang Bingxun, An Hong. 基于深度学习的医学图像分割方法综述. 中国图象图形学报, 2025, 30(6): 2161-2186. [cjig.cn](https://www.cjig.cn/zh/article/doi/10.11834/jig.240467/)