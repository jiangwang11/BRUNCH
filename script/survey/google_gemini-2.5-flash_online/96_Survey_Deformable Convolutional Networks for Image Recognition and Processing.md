好的，这是一篇关于「Deformable Convolutional Networks for Image Recognition and Processing」的中文学术综述，涵盖2022-2025年的代表性工作。

---

## Deformable Convolutional Networks for Image Recognition and Processing (2022-2025)

### 引言

深度学习在图像识别与处理领域取得了显著进展，卷积神经网络（CNNs）作为其核心组成部分，通过学习特征的局部模式表现出强大的能力。然而，标准卷积核的固定几何结构使其难以有效地适应图像中目标物体多变的几何形变、尺度变化和视角多样性，这限制了其在复杂视觉任务中的表现。可变形卷积网络（Deformable Convolutional Networks, DCNs）旨在解决这一固有局限性，通过引入可学习的偏移量来动态调整卷积核的采样位置，从而使其能够更灵活地捕获目标特征，并增强模型对几何形变的鲁棒性。

自DCNv1 [cnblogs.com](https://www.cnblogs.com/VincentLee/p/12826273.html)和DCNv2 [blog.csdn.net](https://blog.csdn.net/qq_52302919/article/details/123517535)相继提出以来，可变形卷积已成为改善各种计算机视觉任务性能的有效工具。DCNv1通过引入可学习的偏移量，使卷积核能够适应目标形状；DCNv2在此基础上加入了调制机制，允许网络同时调整采样位置和特征幅度，进一步提升了形变建模能力 [cnblogs.com](https://www.cnblogs.com/VincentLee/p/12826273.html)。近年来，随着大模型时代的到来和Attention机制的广泛应用，DCNs继续演进，涌现出DCNv3以及与空间注意力机制深度融合的新方法，以期在轻量级模型和高性能模型中均发挥其优势。本综述将重点关注2022年至2025年期间有关可变形卷积网络在图像识别与处理领域的最新进展和具有代表性的工作。

### 方法分类与代表作

本节将可变形卷积网络在2022-2025年的代表性工作分为以下几类，并对每类中的典型论文进行介绍。

#### 1. DCNv3及其轻量化与增强

DCNv3是可变形卷积的进一步发展，旨在提高其在大规模模型中的效率和稳定性，并探索其与Transformer架构的融合。

*   **InternImage: Exploring the Relationship between Deformable Convolution and Spatial Attention (2024)** [developer.volcengine.com](https://developer.volcengine.com/articles/7382310687088836658)
    *   **研究问题**: InternImage旨在解决DCNv2作为传统卷积扩展不适用于从头训练的大规模视觉基础模型的问题，并探索DCNv2与MHSA（多头自注意力）在长程依赖和自适应空间聚合能力上的相似性。
    *   **核心方法**: 作者以DCNv2为基础，通过引入共享权重(在通道维度为depth-wise，在采样点间共享point-wise)，多组机制（多头），以及Softmax归一化调制因子，得到了DCNv3。随后参考ViT的架构设计（如LN、FFN、GELU）定制化构建了InternImage。
    *   **关键实验结论**: InternImage-H在COCO test-dev上取得了65.4%mAP的新记录，且参数量比SwinV2-G少27%；在ImageNet-1K上，InternImage-T达到83.5%的准确率，比ConvNeXt-T高1.4%。这表明DCNv3不仅在常规尺度下性能优异，在大模型上也能有效扩展至与大尺度ViT相当或更优的性能。

*   **DSAN: Exploring the Relationship between Deformable Convolution and Spatial Attention (TNNLS 2025)** [cnblogs.com](https://www.cnblogs.com/wxkang/p/18886289)
    *   **研究问题**: DSAN旨在解决DCNv3在轻量级CNN中因稀疏采样导致的性能不足和计算资源限制问题，特别是在密集预测任务中的应用。
    *   **核心方法**: 作者提出了一种轻量级的可变形条形卷积（Deformable Strip Convolution, DSCN），通过限制不规则采样到单轴并使用线性插值简化了DCNv3的核心操作，并移除了调制掩码分支以减少参数量。在此基础上，DSAN进一步提出可变形空间注意力（Deformable Spatial Attention, DSA）模块，将DCNv3的调制掩码分支替换为空间注意力机制。
    *   **关键实验结论**: DSAN-T在ImageNet1K验证集上Top-1准确率达到76.4%，相比VAN-T和MSCAN-T分别提高1.0%和0.5%。在ADE20K验证集上，DSAN-T的mIoU达到43.5%，相比SegNeXt-T提高了1.2%。DSA结合DSCN的推理速度比大内核DCNv3快2.1倍，在保持甚至超越性能的同时显著降低了参数和内存消耗，证明了其在轻量级模型中的高效性和高精度。

#### 2. 可变形注意力机制

可变形注意力机制是可变形卷积思想与注意力机制的结合，旨在通过动态调整注意力采样位置来捕获更灵活的上下文信息，尤其在Transformer模型中得到了广泛应用。

*   **Deformable Attention (2025)** [blog.csdn.net](https://blog.csdn.net/weixin_47748259/article/details/136190664)
    *   **研究问题**: 本文探讨了现有注意力机制在处理不同任务和输入数据时的局限性，尤其是在特征表示的灵活性方面。它旨在提出一种能够动态调整注意力模型形状和大小的机制。
    *   **核心方法**: 可变形注意力模块允许动态调整注意力模型的形状和大小。其大体流程包括：给定特征图x，生成参考点p；将特征图线性投影到查询token q，再通过轻量子网络生成偏移量Δθ_offset(q)；在变形点处采样作为键和值，与查询共同传入多头注意力机制；最后连接头部特征并通过投影得到最终输出。
    *   **关键实验结论**: 该方法通过稀疏采样提高了计算效率，避免了传统注意力模型中可能存在的过度关注无关区域的问题。通过动态调整采样位置，模型能够更好地适应目标对象的几何形变，提升了特征提取的精确性。

*   **RFAConv: Innovating Spatial Attention and Standard Convolutional Operation (2023)** [zhuanzhi.ai](https://www.zhuanzhi.ai/paper/4e8b273e834fd94cf11d41d92742dcd8)
    *   **研究问题**: 该研究认为现有空间注意力机制（如CBAM和CA）仅关注空间特征，对大尺寸卷积核的参数共享问题解决不足，因为其生成的注意力图信息量有限。
    *   **核心方法**: 提出一种新的感受野注意力机制（Receptive-Field Attention, RFA），它不仅关注感受野空间特征，还能为大尺寸卷积核提供有效的注意力权重。基于RFA开发了感受野注意力卷积操作（RFAConv），旨在替代标准卷积操作。
    *   **关键实验结论**: RFAConv在ImageNet-1k、COCO和VOC数据集上进行了实验，结果表明其在几乎不增加计算成本和参数的情况下显著提高了网络性能。强调了将注意力机制的重点从空间特征转移到感受野空间特征对提升网络性能的重要性。

#### 3. 可变形卷积在特定任务中的应用

可变形卷积因其对几何形变的良好适应性，在多种视觉任务中展现出潜力，例如目标检测和瑕疵识别。

*   **注意力可变形卷积网络的木质板材瑕疵识别 (2024)** [xbgjxt.swu.edu.cn](https://xbgjxt.swu.edu.cn/article/doi/10.13718/j.cnki.xdzk.2024.02.016)
    *   **研究问题**: 为了解决木质板材瑕疵检测中人工成本高、效率低以及传统方法对复杂表面和多样化缺陷适应性不足的问题，本文提出一种基于可变形卷积网络和注意力机制的端到端神经架构模型。
    *   **核心方法**: 模型首先使用可变形卷积网络（DCN）将矩形网格转换为变形网格，使其专注于具有更多有用图像信息的区域，从而解决传统卷积在特征学习中的局限性。DCN的输出随后馈送到门控循环单元（GRU）层以学习高级特征。最后，应用注意力机制加强瑕疵区域的高亮度，以提高识别准确率。
    *   **关键实验结论**: 在4个木质板材缺陷数据集上进行比较，该方法在准确率、灵敏度和特异性方面均优于其他3种对比方法。例如，准确率提高了2.4%~13.2%，最佳准确率为99.2%。实验证明该模型能更好地适应各种不同形状和尺寸的缺陷，提高了网络泛化能力和检测精度。

*   **Deformable DETR: Deformable Transformers for End-to-End Object Detection (2025)** [blog.csdn.net](https://blog.csdn.net/m0_38068229/article/details/115503814)
    *   **研究问题**: Facebook AI提出的DETR目标检测器存在收敛速度慢和处理小物体性能差的问题，主要是因为Transformer注意力模块在处理图像特征图时的计算复杂度和对高分辨率特征图的限制。
    *   **核心方法**: 本文提出了可变形DETR（Deformable DETR），结合了可变形卷积中的稀疏空间采样优势与Transformer的关系建模能力。其注意力模块仅关注参考点附近的一小部分采样点作为key元素，并通过迭代式物体边界框细化机制进一步提高检测性能，同时原生支持多尺度特征聚合。
    *   **关键实验结论**: Deformable DETR显著解决了DETR的收敛慢问题，在COCO基准上，训练轮数减少了90%，却能达到更好的性能，尤其在小物体检测上表现突出。例如，COCO test-dev上的性能超越了DETR，证明了其在端到端目标检测中的有效性和高效性。

### 实验与评价总结

近期可变形卷积网络的研究在多个方面取得了共性进展和评价。首先， **计算效率与性能的平衡** 是一个核心考量。DCNv3的提出以及轻量化变体DSAN证实，通过优化DCN的核心操作、引入多组机制和标准化的调制因子 [developer.volcengine.com](https://developer.volcengine.com/articles/7382310687088836658)，可以在保持甚至超越传统CNN性能的同时，显著降低计算复杂度与内存消耗 [cnblogs.com](https://www.cnblogs.com/wxkang/p/18886289)。

其次， **与注意力机制的融合成为趋势**。Deformable Attention等工作中，可变形采样与注意力机制的结合使得模型能够动态地聚焦于图像中更相关的区域，提升了特征提取的灵活性。这种融合不仅存在于Transformer架构中，也通过RFAConv等方法与传统卷积相结合 [zhuanzhi.ai](https://www.zhuanzhi.ai/paper/4e8b273e834fd94cf11d41d92742dcd8)。

再者，DCNs在 **解决几何形变鲁棒性** 方面展现出持续的优势。在如木质板材瑕疵识别 [xbgjxt.swu.edu.cn](https://xbgjxt.swu.edu.cn/article/doi/10.13718/j.cnki.xdzk.2024.02.016)等特定应用中，DCN能够更好地适应物体多变的形状和尺寸，提升识别精度和泛化能力。在目标检测任务如Deformable DETR [blog.csdn.net](https://blog.csdn.net/m0_38068229/article/details/115503814)中，通过稀疏采样和多尺度特征聚合，显著改善了收敛速度和小目标检测性能，验证了DCN在复杂背景下精确感知目标的有效性。

总体而言，当前研究强调可变形卷积不仅通过其动态采样能力增强了模型对几何形变的适应性，而且通过与现代架构如Transformer和注意力机制的融合，大幅提升了模型在各种视觉任务上的性能、效率和鲁棒性。

### 趋势与挑战

2025年前后可变形卷积的研究趋势预测将集中在以下几个方面：

1.  **轻量化与高效部署**: 随着AI边缘计算和移动设备应用的需求增长，DCNs的轻量化将是重要趋势。DSAN等工作已经展示了在这方面的潜力，未来研究将进一步探索更紧凑、计算开销更低的可变形模块设计，使其能在资源受限环境中高效部署，同时保持高性能，例如通过简化插值方案、优化偏移量预测网络等。
2.  **DCN与多模态学习的融合**: 目前DCN主要应用于图像数据，未来将更多地探索其在多模态数据处理中的应用，例如与文本、声音等信息结合，处理更复杂的感知任务。这可能涉及到设计跨模态的可变形注意力机制，以动态捕捉不同模态间对齐的形变信息。
3.  **可解释性与鲁棒性增强**: 尽管DCNs提升了对形变的适应性，但其可解释性仍有待提高。未来的研究可能会关注如何更直观地理解可变形采样策略，以及如何进一步提升模型在面对对抗性攻击和复杂噪声时的鲁棒性，例如通过引入新的正则化项、或将可变形采样与不确定性量化相结合。

### 结论

可变形卷积网络代表了CNNs在处理几何形变方面的一个重要突破。近年来，从DCNv1到DCNv3的演进，以及与注意力机制和Transformer架构的深度融合，极大地拓展了其在图像识别与处理领域的应用前景。新提出的轻量级DSAN和高性能InternImage模型，以及融合可变形采样的Deformable Attention和RFAConv，均展示了DCNs在提升效率和精度上的显著优势。Deformable DETR在目标检测任务中的表现也再次验证了其解决复杂视觉挑战的潜力。尽管DCNs已取得了显著成就，但其在轻量级设计、多模态融合以及可解释性与鲁棒性等方面的研究仍充满机遇，预示着未来其将继续在计算机视觉领域发挥关键作用。

### 参考文献

*   [cnblogs.com](https://www.cnblogs.com/wxkang/p/18886289) (CV技术指南（公众号）, "TNNLS 2025 | 简化版可变形卷积DCNv3——可变形空间注意力，CV任务涨点起飞！", 2025-05-20)
*   [blog.csdn.net](https://blog.csdn.net/weixin_47748259/article/details/136190664) (丁希希哇, "可变形注意力（Deformable Attention）及其拓展", 2025-04-24)
*   [blog.csdn.net](https://blog.csdn.net/m0_38068229/article/details/115503814) (吃吃今天努力学习了吗, "Deformable Transformers for End-to-End Object Detection_deformable detr谁提出的", 2025-04-08)
*   [developer.volcengine.com](https://developer.volcengine.com/articles/7382310687088836658) (集智书童, "DCN升级 | 扩展DCNv3，探索大模型，COCO新纪录64.5mAP", 2024-06-20)
*   [zhuanzhi.ai](https://www.zhuanzhi.ai/paper/4e8b273e834fd94cf11d41d92742dcd8) (Xin Zhang et al., "RFAConv: Innovating Spatial Attention and Standard Convolutional Operation", 2023-04-18)
*   [xbgjxt.swu.edu.cn](https://xbgjxt.swu.edu.cn/article/doi/10.13718/j.cnki.xdzk.2024.02.016) (朱咏梅 et al., "注意力可变形卷积网络的木质板材瑕疵识别", 2023-05-09)
*   [cnblogs.com](https://www.cnblogs.com/VincentLee/p/12826273.html) (晓飞的算法工程笔记, "可变形卷积系列(二) MSRA提出升级版DCNv2，变形能力更强 | CVPR 2019", 2020-05-04)
*   [blog.csdn.net](https://blog.csdn.net/Marcus1231/article/details/149863034) (Marcus1231, "【CVPR2019】Deformable ConvNets v2: More Deformable, Better Results", 2025-08-05)
*   [blog.csdn.net](https://blog.csdn.net/qq_52302919/article/details/123517535) (小小小~, "Deformable ConvNets v2: More Deformable, Better Results", 2025-08-05)
*   [blog.csdn.net](https://blog.csdn.net/qq_41917697/article/details/116193042) (球场书生, "CNN卷积神经网络之DCN（Deformable Convolutional Networks、Deformable ConvNets v2）_dcn神经网络", 2024-11-11)