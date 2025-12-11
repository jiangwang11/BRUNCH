好的，遵照您的指示，我将基于提供的真实网络搜索结果，生成一篇关于2022-2025年间医学图像分割技术与应用的严谨学术综述。

***

### **医学图像分割技术与应用：2022-2025年进展综述**

#### **引言**
医学图像分割是计算机辅助诊断与治疗的关键环节，旨在从医学影像（如CT、MRI）中精确识别并勾勒出器官、病灶等感兴趣区域。近年来，以U-Net为代表的卷积神经网络（CNN）在此领域取得了巨大成功，但其固有的局部感受野限制了对全局上下文信息的捕获能力。为克服此局限，2022-2025年期间，研究范式发生了显著演进：研究者们从CNN主导的模型，逐步转向结合CNN局部特征提取能力与Transformer全局依赖建模优势的混合模型。近期，随着基础模型（Foundation Models）的兴起以及对计算效率的更高要求，更通用的分割模型（如SAM）和新一代高效架构（如视觉状态空间模型）成为前沿研究热点。本综述将系统梳理并总结这一时期的代表性技术与发展趋势。

#### **方法分类与代表作**
根据2022-2025年的研究趋势，我们将主流方法分为三类：CNN-Transformer混合模型、基于视觉状态空间模型的分割方法，以及基于基础模型的分割方法。

**1. CNN-Transformer混合模型**

这类方法旨在融合CNN在捕捉局部纹理细节方面的优势与Transformer在建模长距离依赖关系方面的能力，是近年来提升分割性能的主流方向 [opticsjournal.net](https://www.opticsjournal.net/Articles/OJ2b2078a8cf027f69/km)。

*   **MCT-Net (2025):** 针对肝脏肿瘤边界模糊、形态多变的问题，该研究提出了一种双编码器网络MCT-Net。其并行使用CNN编码器（内置细节特征提取模块DFEM和局部空间注意力LAM）提取精细边缘特征，以及Transformer编码器获取全局感受野。在解码阶段，通过多尺度信息交互模块（MSIF）有效融合两种尺度的信息，以提升边界分割精度。实验表明，在LiTS2017数据集上，MCT-Net的Dice系数达到72.16%，显著优于传统的U-Net及TransUNet等模型 [pdf.hanspub.org](https://pdf.hanspub.org/mos2025141_372572027.pdf)。

*   **改进的SwinUNet (2025):** 为解决SwinUNet在全局上下文建模和多尺度特征表达上的不足，该研究提出了一套改进方案。首先，采用Focal Transformer代替Swin Transformer，通过分层注意力机制增强局部细节与全局依赖的建模能力。其次，在编码器末端引入空洞空间金字塔池化（ASPP）以扩展感受野，并在跳跃连接中加入Tokenized Interaction Fusion（TIF）模块以促进跨层信息融合。在Synapse腹部多器官数据集上，该方法的平均Dice系数（79.53%）和Hausdorff距离（19.73mm）均优于基线SwinUNet模型 [pdf.hanspub.org](https://pdf.hanspub.org/csa_1543783.pdf)。

**2. 基于视觉状态空间模型的分割方法**

为应对Transformer二次方复杂度的计算瓶颈，研究者开始探索性能与效率兼具的新架构，视觉状态空间模型（Visual State Space Models, VSSM）是其中的代表。

*   **VMDC-Unet (2025):** 该研究旨在解决结直肠癌病理切片中肿瘤异质性、背景复杂导致的分割难题。其创新性地提出了VMDC-Unet，一个融合VMamba与CNN的混合架构，这是将状态空间模型应用于医学图像分割的早期探索。该方法利用VMamba高效处理长距离依赖，同时结合改进的ConvNext模块强化局部细粒度特征提取，并通过局部自注意力机制优化跳跃连接中的特征融合。实验证明，在SJTU_GSFPH和Glas数据集上，VMDC-Unet的分割精度与泛化能力均超越了包括TransUnet和Swin-Unet在内的基准模型，其MIOU在SJTU_GSFPH上达到79.40% [www.hanspub.org](https://www.hanspub.org/journal/paperinformation?paperid=112526)。

**3. 基于基础模型的分割方法**

基础模型（Foundation Models）的出现，特别是分割一切模型（Segment Anything Model, SAM），为医学图像分割带来了“一次训练、处处可用”的零样本/少样本新范式。然而，由于自然图像与医学图像间的领域鸿沟，直接应用效果有限，因此适配与微调成为核心研究方向 [opticsjournal.net](https://www.opticsjournal.net/Articles/OJda3bfaa1dd74a3a/FullText)。

*   **MedSAM / SAM-Med2D (2023-2024):** 为解决SAM在医学领域的不足，研究者通过在大型医学图像数据集上微调，开发了领域专用的基础模型。MedSAM通过在超过一百万个2D医学图像-掩码对上进行微调，显著提升了对多种模态图像的分割能力。SAM-Med2D则在规模更大的数据集（约460万图像和1970万掩码）上训练，展现出更强的泛化性能。在一项对比实验中，SAM-Med2D在ABUS肿瘤数据集上的平均交并比（mIoU）达到62.78%，远高于MedSAM的42.85%和原始SAM的40.01% [opticsjournal.net](https://www.opticsjournal.net/Articles/OJda3bfaa1dd74a3a/FullText)。

*   **DB-SAM (2024):** 针对SAM的领域适应问题，该研究提出了一种更高效的双分支适配框架DB-SAM。它冻结了SAM的大部分参数，通过一个并行的轻量级CNN分支提取领域特定的浅层特征，同时在ViT分支中引入可学习的通道注意力块以捕捉局部信息。通过设计的双边交叉注意力进行特征融合，该方法在21个3D医学分割任务上，相比最新的SAM适配器实现了8.8%的绝对性能提升，展示了参数高效微调的巨大潜力 [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/64809)。

*   **MedSAM2 (2025):** 作为SAM在医学领域应用的最新进展，MedSAM2将分割能力从2D图像扩展至3D图像和视频。该模型在SAM2的基础上，利用一个包含超过45.5万对3D图像-掩码和7.6万视频帧的超大规模数据集进行微调。MedSAM2不仅在多种器官和病灶分割任务上超越了以往模型，其集成的人机协作流程更被证实在大规模标注任务中能将人工成本降低超过85%，极具临床应用价值 [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/279a8711-cf36-4ca8-b9c9-1f7c35eec72e)。

#### **实验与评价总结**

*   **数据集与评价指标：** 公开基准数据集如Synapse多器官分割数据集和LiTS（肝脏肿瘤分割）是评估模型性能的常用平台 [pdf.hanspub.org](https://pdf.hanspub.org/csa_1543783.pdf)。同时，为推动基础模型发展，研究者们构建了百万量级的私有或半公开医学图像数据集，如MedSAM和MedSAM2所用的大规模数据集 [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/279a8711-cf36-4ca8-b9c9-1f7c35eec72e)。性能评估主要依赖两个核心指标：Dice相似系数（Dice Similarity Coefficient, DSC）用于衡量预测区域与真实标签的重叠程度，而豪斯多夫距离（Hausdorff Distance, HD95）则更侧重于评估边界的匹配精度。

*   **共性结论：**
    1.  **混合架构的有效性：** 无论是CNN-Transformer还是CNN-VMamba混合模型，均一致性地证明了融合局部特征提取器与全局依赖建模器的优势。通过结合两种架构，模型能够在提升DSC的同时，有效降低HD95，意味着分割结果在内部一致性和边界准确性上都得到了改善。
    2.  **基础模型的领域适应必要性：** 直接应用SAM等预训练于自然图像的基础模型，在医学图像上性能受限。通过在大型、多样化的医学数据集上进行微调或结构适配是释放其潜力的关键，这能显著弥合领域鸿沟，提升模型在未见过的医学模态和任务上的泛化能力 [opticsjournal.net](https://www.opticsjournal.net/Articles/OJda3bfaa1dd74a3a/FullText)。
    3.  **多尺度与跨层信息融合的重要性：** 成功的分割模型普遍重视多尺度特征的捕获与融合。如在编码器中集成ASPP模块，或在解码器及跳跃连接中设计专门的融合模块（如TIF、MSIF），被证明是处理尺寸多变、边界模糊病灶的有效策略 [pdf.hanspub.org](https://pdf.hanspub.org/csa_1543783.pdf)。

#### **趋势与挑战**

基于2022-2025年的研究进展，医学图像分割领域呈现出以下主要趋势与挑战：

1.  **趋势一：从专用模型到通用基础模型的范式转变。** 以MedSAM2为代表的研究表明，未来的发展方向是构建可处理多种模态（CT, MRI, Ultrasound）、多维度（2D, 3D, Video）和多任务的通用医学分割基础模型。这类模型通过提示（prompting）工程，仅需少量甚至零样本即可适应新的分割任务，极大地降低了模型开发门槛和对大量标注数据的依赖 [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/279a8711-cf36-4ca8-b9c9-1f7c35eec72e)。

2.  **趋势二：追求更高计算效率的新兴架构。** Transformer虽然强大，但其高计算成本限制了在3D高分辨率图像和实时视频中的应用。以VMamba为代表的视觉状态空间模型，因其在建模长序列时具有线性复杂度，正成为Transformer的有力竞争者和替代品 [www.hanspub.org](https://www.hanspub.org/journal/paperinformation?paperid=112526)。预计未来会有更多基于SSM或类似高效架构的分割模型涌现。

3.  **趋势三：面向临床应用的3D/4D与多模态融合。** 临床诊断常需综合多种影像信息。未来的分割模型将更加注重对多模态数据（如CT+MRI）的有效融合，以及对包含时间维度的4D数据（如动态MRI）的处理能力。这要求模型不仅能理解空间结构，还能捕捉时序变化，为功能性分析和疾病进展监测提供支持 [github.com](https://github.com/zdreamx/StarrySky)。

*   **核心挑战：**
    *   **数据隐私与孤岛问题：** 高质量的医学数据分散在不同机构，数据隐私法规严格。联邦学习（Federated Learning）等隐私计算技术是解决这一挑战的关键，但如何在保证隐私的同时高效训练大规模模型仍是难题 [ai.medsci.cn](https://ai.medsci.cn/article/paper-topic/55e14d68-976f-4f1d-9232-4e55be03d7d1)。
    *   **模型可解释性与可靠性：** 在高风险的医疗领域，深度学习模型的“黑箱”特性是其临床落地的主要障碍。开发可解释的AI，量化模型预测的不确定性，并确保其在面对分布外（out-of-distribution）数据时的鲁棒性，是亟待解决的问题。

#### **结论**
在2022至2025年间，医学图像分割技术经历了从专门化向通用化、从性能优先向效率与性能并重的深刻变革。CNN-Transformer混合模型通过结合局部与全局信息，显著提升了分割精度。更为前沿的视觉状态空间模型则预示了新一代高效架构的到来。而以SAM及其衍生模型为代表的基础模型，正推动该领域进入一个全新的、由大规模预训练和提示驱动的时代。尽管面临数据隐私和模型可靠性等挑战，但未来的研究无疑将朝着构建更通用、高效、可信的医学图像分割系统迈进，以更好地服务于精准医疗。

#### **参考文献**

1.  尹艺晓, 马金刚, 张文凯, 姜良. (2025). 从U-Net到Transformer：混合模型在医学图像分割中的应用进展. *激光与光电子学进展*, 62(2), 0200001. [opticsjournal.net](https://www.opticsjournal.net/Articles/OJ2b2078a8cf027f69/km)
2.  檀文文, 卢棚, 姜韦. (2025). 基于改进SwinUNet腹部多器官分割算法研究. *计算机科学与应用*, 15(10), 318-326. [pdf.hanspub.org](https://pdf.hanspub.org/csa_1543783.pdf)
3.  王劭羽, 陈庆奎, 黄陈. (2025). 基于VMamba-CNN混合的结直肠癌切片图像分割. *建模与仿真*, 14(4), 799-810. [www.hanspub.org](https://www.hanspub.org/journal/paperinformation?paperid=112526)
4.  吴曈, 胡浩基, 冯洋, 等. (2024). 分割一切模型（SAM）在医学图像分割中的应用. *中国激光*, 51(21), 2107102. [opticsjournal.net](https://www.opticsjournal.net/Articles/OJda3bfaa1dd74a3a/FullText)
5.  Ma, J., Yang, Z., Kim, S., et al. (2025). MedSAM2: Segment Anything in 3D Medical Images and Videos. *arXiv preprint*. [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/279a8711-cf36-4ca8-b9c9-1f7c35eec72e)
6.  Qin, C., Cao, J., Fu, H., et al. (2024). DB-SAM: Delving into High Quality Universal Medical Image Segmentation. *arXiv preprint*. [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/64809)
7.  汤文超, 丁德锐, 袁浩成, 刘华卿. (2025). 一种混合CNN-Transformer多尺度特征的肝脏肿瘤分割网络. *建模与仿真*, 14(1), 388-403. [pdf.hanspub.org](https://pdf.hanspub.org/mos2025141_372572027.pdf)
8.  梅斯医学. (2025). 深度学习在肿瘤影像分割与心脏病诊断中的应用. *MedSci xAi*. [ai.medsci.cn](https://ai.medsci.cn/article/paper-topic/55e14d68-976f-4f1d-9232-4e55be03d7d1)
9.  石军, 王天同, 朱子琦, 等. (2025). 基于深度学习的医学图像分割方法综述. *中国图象图形学报*, 30(6), 2161-2186. [www.cjig.cn](https://www.cjig.cn/zh/article/doi/10.11834/jig.240467/)
10. Ronneberger, O., Fischer, P., & Brox, T. (2015). U-Net: Convolutional Networks for Biomedical Image Segmentation. *Medical Image Computing and Computer-Assisted Intervention – MICCAI 2015*.
11. Chen, J., Lu, Y., Yu, Q., et al. (2021). TransUNet: Transformers Make Strong Encoders for Medical Image Segmentation. *arXiv preprint arXiv:2102.04306*.
12. Cao, H., Wang, Y., Chen, J., et al. (2023). Swin-Unet: Unet-Like Pure Transformer for Medical Image Segmentation. *European Conference on Computer Vision*. [github.com](https://github.com/zdreamx/StarrySky)