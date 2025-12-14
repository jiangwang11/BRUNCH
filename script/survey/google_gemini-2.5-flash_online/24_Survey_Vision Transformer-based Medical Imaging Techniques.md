## Vision Transformer-based Medical Imaging Techniques 中文学术综述 (2022–2025)

### 引言

医学图像分析在疾病诊断、治疗规划及预后评估中扮演着至关重要的角色。传统深度学习方法，尤其是基于卷积神经网络 (CNN) 的模型（如 U-Net），在医学图像分割等任务中取得了显著成功。然而，CNN 固有的局部感受野限制了其捕获长程依赖和全局上下文信息的能力，这对于理解复杂的医学图像结构至关重要。近年来，受益于自然语言处理领域 Transformer 架构的突破，Vision Transformer (ViT) 模型开始被引入计算机视觉，并迅速扩展到医学图像领域，为解决传统 CNN 的局限性提供了新的视角 [opticsjournal.net](https://www.opticsjournal.net/Articles/OJ2b2078a8cf027f69/km)。本综述将聚焦 2022 年至 2025 年间 Vision Transformer 及其变体在医学图像分析中的代表性应用，特别是分割任务，总结其核心方法、关键结论及未来研究趋势。

### 方法分类与代表作

Vision Transformer 在医学图像领域的发展主要体现在以下几个方面：纯 Transformer 结构、混合模型以及针对医学图像特点的 Transformer 改进。

#### 1. 纯 Transformer 结构

纯 Transformer 模型直接将医学图像切分成 patches，通过自注意力机制捕获全局依赖。

*   **UNETR (2022)**：该工作旨在解决 3D 医学图像分割中 CNN 局部感受野的限制，提出了 UNETR (UNEt TRansformers) 模型。它首次将纯 Transformer 作为 3D 医学图像分割的编码器，将 3D 体素数据重构为一维序列输入 Transformer，并利用跳跃连接将 Transformer 编码器提取的多分辨率特征与解码器融合以进行语义分割 [blog.csdn.net](https://blog.csdn.net/qq_38296005/article/details/119830386)。实验在 MSD 数据集上的脑肿瘤和脾脏分割任务中取得了优异性能。

*   **SwinUNETR (CVPR 2022)**：这篇研究提出了基于 Swin-Transformer 的自监督预训练方法 SwinUNETR，用于 3D 医学图像分析。它通过 Swin-Transformer 编码器直接处理 3D 输入 patches，并将其应用于图像修复、3D 旋转预测和对比学习等预训练任务，以解决医学图像数据稀缺和领域鸿沟问题 [medium.com](https://medium.com/@s93011/swinunetr-swin-transformer%E7%9A%84self-supervise%E9%A0%90%E8%A8%93%E7%B7%B4%E7%94%A8%E6%96%BC3d%E9%86%AB%E5%AD%B8%E5%BD%B1%E5%83%8F%E5%88%84%E6%9E%90-475537b560f5)。SwinUNETR 在 BTCV 多器官分割挑战和 MSD 挑战中均达到了 SOTA 表现。

#### 2. 混合模型（CNN-Transformer Hybrid）

混合模型结合了 CNN 捕获局部特征和 Transformer 捕获全局依赖的优势，是当前主流的范式。

*   **TransUNet (MICCAI 2021)**：虽然发表于 2021 年，但其作为 CNN-Transformer 混合模型的开创性工作对后续研究影响深远。它将 Transformer 作为 U-Net 的编码器骨干，并从 Transformer 不同层级提取特征通过跳跃连接到 U-Net 解码器，旨在同时利用 Transformer 的全局上下文建模能力和 U-Net 的局部细节恢复能力 [blog.csdn.net](https://blog.csdn.net/qq_38296005/article/details/119830386)。这种结合在多个医学图像分割数据集上展现了优越的性能。

*   **CoTr (2024)**：CoTr 框架有效桥接了卷积神经网络和 Transformer 用于 3D 医学图像分割。该模型采用 CNN 编码器提取特征，并引入可变形 Transformer (DeTrans) 编码器建模长程依赖，同时通过跳跃连接在不同尺度上融合特征 [pdf.hanspub.org](https://pdf.hanspub.org/csa2024147_91543304.pdf)。CoTr 在多模态腹部分割数据集 (AMOS) 上的 3D 多器官分割任务中，相比纯 CNN 和纯 Transformer 方法，带来了持续的性能改进，尤其在小目标分割上表现突出。

*   **CPCATNet (2025)**：针对肺部肿瘤分割中病灶对比度低、易粘连和背景噪声大的问题，CPCATNet 提出了一种基于 Transformer 和通道优先卷积注意力机制的网络。该模型在 Transformer 编码器阶段引入全局和局部注意力机制，同时关注全局和局部上下文信息；在跳跃连接阶段使用通道优先卷积注意力机制，增强复杂病灶的空间感知能力并降低通道冗余 [html.rhhz.net](https://html.rhhz.net/GDGYDXXB/html/1736152746337-1505189003.htm)。实验结果显示，CPCATNet 在 GDPH 和 LUNG1 两个肺部肿瘤数据集上，Dice 指标分别达到 90.96% 和 88.18%，优于其他 8 种分割方法。

#### 3. 针对医学图像特点的 Transformer 改进

这些工作致力于优化 Transformer 结构以更好地适应医学图像特有的挑战, 如低信噪比、多模态融合等。

*   **MedMamba (MICCAI 2025)**：MedMamba 旨在突破医学影像分类的瓶颈，提出了首款基于选择性状态空间模型 (SSMs) 的医学视觉架构。它通过四向扫描策略实现了 100% 像素关联覆盖，解决了传统 CNN 远程依赖缺陷，同时在计算效率上进行了大幅优化 [xugj520.cn](https://www.xugj520.cn/archives/medmamba-medical-image-classification.html)。MedMamba 在 9 个医学影像数据集上平均准确率达 93.7%，较 CNN-ViT 混合模型提升 3.2%，处理 224x224 图像仅需 38ms，内存消耗降低 37%。

*   **MDT-AF (2024)**：针对医学图像分割中低信噪比和通道空间信息利用不足的问题，MDT-AF (Multi-dimension Transformer with Attention-based Filtering) 被提出。它在 Transformer 中加入了基于注意力的特征过滤机制和扩展的自注意力机制，并引入交互机制以提高空间和通道维度的特征聚合 [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/7b39f2f8-3fc8-42da-9a43-57e196d9e31b)。MDT-AF 在三个公共医学图像分割基准测试中取得了最先进的性能。

*   **C$^2$ Transformer U-Net (2023)**：为了解决 U-Net 主要使用单模态图像且未充分考虑跨模态及上下文语义相关性的问题，C$^2$ Transformer U-Net 模型被提出。该模型在编码器部分设计了主干和辅助 U-Net 网络结构以提取不同模态的语义信息，并设计了多模态上下文语义感知处理器 (MCAP) 有效提取同一病灶的跨模态语义信息 [jeit.ac.cn](https://jeit.ac.cn/cn/article/doi/10.11999/JEIT220445?viewType=HTML)。实验在临床多模态肺部医学图像数据集上验证了其对复杂形状肺部病灶分割的高精度和低冗余度。

### 实验与评价总结

综上所述，自 2022 年以来，Vision Transformer 在医学图像领域的应用展现出以下共性结论：

*   **性能提升：** 无论是纯 Transformer 模型还是混合模型，相比传统纯 CNN 方法，在医学图像分割任务中均体现出显著的性能提升，尤其在捕获长程依赖、全局上下文信息以及处理形态复杂、尺度多变的病灶方面表现更佳。研究中通常采用 Dice 系数、Hausdorff Distance (HD)、准确率 (Acc) 等指标进行评估，大量工作均报告了优于现有 SOTA 方法的结果。
*   **弥补 CNN 局限：** Transformer 的自注意力机制能够有效解决 CNN 局部感受野的限制，促进了模型对图像整体结构和远距离像素间关系的理解。
*   **挑战与对策：** 尽管 Transformer 表现出色，但其高计算复杂度和对大规模标注数据的需求仍然是挑战。研究者通过结合 CNN 降低计算量、引入自监督预训练减轻数据依赖、以及设计轻量级或高效的注意力机制来应对这些问题。例如，Swin-Transformer 的分层结构和窗口注意力机制显著提升了效率；自监督预训练（如 SwinUNETR）则有效利用了无标注数据。
*   **多模态与多任务：** Transformer 在多模态图像融合（如 C$^2$ Transformer U-Net）和多器官分割（如 CoTr）等复杂任务中展现出强大潜力，通过灵活的架构设计，能够有效聚合不同模态或不同器官的特征信息。

### 趋势与挑战

展望 2025 年前后，Vision Transformer-based Medical Imaging Techniques 的研究趋势将呈现以下几个方向：

1.  **轻量化与高效性：** 尽管 Transformer 性能优越，但其巨大的参数量和计算成本仍是部署到临床环境的障碍。未来的研究将持续关注如何设计更轻量级、计算更高效的 Transformer 变体，例如通过更精巧的注意力机制、知识蒸馏或剪枝等技术，在保持高性能的同时降低资源消耗，以实现实时处理和更广泛的临床应用 (如 MedMamba 的低延迟特性) [xugj520.cn](https://www.xugj520.cn/archives/medmamba-medical-image-classification.html)。
2.  **大模型与预训练范式：** 借鉴自然语言处理领域大模型的成功，将出现更多在海量医学图像数据上预训练的大型 Vision Transformer 模型 [xhyxzz.pumch.cn](https://xhyxzz.pumch.cn/article/doi/10.12290/xhyxzz.2025-0328?viewType=citedby-info)。这些大模型将具备强大的泛化能力和迁移学习潜力，通过少样本或零样本学习即可适应新的分割任务，大幅缓解医学数据标注昂贵且稀缺的问题 (如 SwinUNETR 的自监督预训练)。
3.  **多模态融合与统一架构：** 随着多模态医学成像技术（CT, MRI, PET 等）的普及，研究将超越单一模态，探索更有效、更鲁棒的多模态信息融合 Transformer 架构 (如 C$^2$ Transformer U-Net)，以更好地利用互补信息并提升诊断准确性。甚至可能出现一个能处理所有模态、所有任务的统一 Vision Foundation Model。

主要的挑战包括：

*   **数据隐私与共享：** 构建大规模医学图像数据集面临严格的隐私法规和数据共享壁垒。
*   **可解释性：** 深度学习模型的“黑箱”特性在医学领域尤为敏感，提高 Transformer 模型的可解释性是赢得临床信任的关键。
*   **长尾分布问题：** 罕见疾病或异常情况的医学图像数据量少，导致模型对这些情况的分割效果不佳。
*   **伦理与合规：** AI 在临床辅助诊断中的应用需通过严格的伦理审查和监管批准。

### 结论

Vision Transformer-based Medical Imaging Techniques 在短短几年内取得了飞速发展，特别是在医学图像分割领域展现出超越传统 CNN 的强大潜力。混合模型和针对医学图像特点的改进成为主流，有效地解决了长程依赖问题，并逐步探索多模态融合和自监督预训练以应对数据挑战。尽管仍面临计算资源、数据隐私和可解释性等诸多挑战，但其在肿瘤精准诊疗等领域的应用前景广阔，有望在未来几年内进一步推动医学图像分析技术的革新。

### 参考文献

1.  姜良等. 从U-Net到Transformer：混合模型在医学图像分割中的应用进展. [opticsjournal.net](https://www.opticsjournal.net/Articles/OJ2b2078a8cf027f69/km). 激光与光电子学进展, 2025, 62(2): 0200001.
2.  Tsai Jeff. SwinUNETR：Swin-Transformer的Self-supervise預訓練用於3D醫學影像分析. [medium.com](https://medium.com/@s93011/swinunetr-swin-transformer%E7%9A%84self-supervise%E9%A0%90%E8%A8%93%E7%B7%B4%E7%94%A8%E6%96%BC3d%E9%86%AB%E5%AD%B8%E5%BD%B1%E5%83%8F%E5%88%86%E6%9E%90-475537b560f5). 2022-08-15.
3.  Pan Dan. Lung Tumor Segmentation Method Based on Transformer and Attention Mechanisms. [html.rhhz.net](https://html.rhhz.net/GDGYDXXB/html/1736152746337-1505189003.htm). JOURNAL OF GUANGDONG UNIVERSITY OF TECHNOLOGY, 2025, 42(1): 24-32.
4.  Tsai Jeff. UNETR: Transformers for 3D Medical Image Segmentation. [blog.csdn.net](https://blog.csdn.net/qq_38296005/article/details/119830386). 2025-06-12 (Original article likely published earlier, this CSDN blog post describes it).
5.  Zhao Wei. 基于CoTr分割网络的3D多器官CT图像分割. [pdf.hanspub.org](https://pdf.hanspub.org/csa2024147_91543304.pdf). Computer Science and Application, 2024, 14(7): 78-83.
6.  高效码农. MedMamba如何突破医学图像分类瓶颈？深度解析视觉Mamba的架构革命. [xugj520.cn](https://www.xugj520.cn/archives/medmamba-medical-image-classification.html). 2025-06-10.
7.  Wentao Wang et al. Multi-dimension Transformer with Attention-based Filtering for Medical Image Segmentation. [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/7b39f2f8-3fc8-42da-9a43-57e196d9e31b). 2024-05-20.
8.  周涛等. C$^2$ Transformer U-Net：面向跨模态和上下文语义的医学图像分割模型. [jeit.ac.cn](https://jeit.ac.cn/cn/article/doi/10.11999/JEIT220445?viewType=HTML). 电子与信息学报, 2023, 45(5): 1807-1816.
9.  Saikat Roy et al. MedNeXt：基于Transformer的卷积神经网络在医学图像分割中的比例扩展. [zhuanzhi.ai](https://www.zhuanzhi.ai/paper/a585c49cef893453d77fa612080fe159). 2023-03-17.
10. Liu Zaiyi, Zhao Zhihe, Shi Zhenwei. 医学影像大模型：肿瘤精准诊疗的范式革新. [xhyxzz.pumch.cn](https://xhyxzz.pumch.cn/article/doi/10.12290/xhyxzz.2025-0328?viewType=citedby-info). 中华医学杂志, 2025-06-20 (Commentary/Review).
11. Chen J, Lu Y, Yu Q, et al. Transunet: Transformers Make Strong Encoders for Medical Image Segmentation. [arXiv](https://arxiv.org/abs/2102.04306v3). arXiv:2102.04306, 2021.
12. Hatamizadeh A, Tang Y, Nath V, et al. UNETR: Transformers For 3D Medical Image Segmentation. In: Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision. 2022: 574-584.