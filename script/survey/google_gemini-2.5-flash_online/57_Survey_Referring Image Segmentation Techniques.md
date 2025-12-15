好的，这是一篇关于 2022-2025 年 Referring Image Segmentation (RIS) 技术的中文学术综述。

## Referring Image Segmentation 技术综述 (2022-2025)

### 引言

指令参考图像分割（Referring Image Segmentation, RIS），又称指代图像分割，旨在根据自然语言描述从图像中精确分割出目标对象。这项任务结合了计算机视觉和自然语言处理，要求模型不仅能够理解图像内容，还能将语言表达与图像中的像素级区域进行语义对齐。RIS 在人机交互、图像编辑、智能监控等多个领域具有广泛的应用潜力。近年来，随着大模型、Transformer 架构以及跨模态学习的快速发展，RIS 技术取得了显著进展。本综述将聚焦 2022-2025 年间 RIS 领域的代表性工作，对其主要方法进行归类梳理，总结实验趋势，并对未来的发展方向和挑战做出展望。

### 方法分类与代表作

RIS 方法的核心挑战在于有效地融合视觉与语言信息，并将语言描述映射到精细的像素级掩模。根据其核心技术范式和交互方式，可将近期工作分为以下几类：

#### 1. 基于视觉-语言预训练模型（CLIP/大模型）微调

这类方法利用在海量图像-文本对上预训练的视觉-语言大模型（如 CLIP）强大的跨模态理解能力，通过微调或适配器将其应用于像素级的 RIS 任务。

*   **CRIS: CLIP-Driven Referring Image Segmentation** [cnblogs.com](https://www.cnblogs.com/lipoicyclic/p/16807808.html)
    *   **研究问题：** 整合文本和像素级特征以实现指代图像分割，同时确保模态间的一致性。
    *   **核心方法：** 受到 CLIP 启发，设计了一个视觉-语言解码器（Visual-Language Decoder）以促进两种模态之间的一致性。同时，提出文本到像素的对比学习损失，将文本特征与相关的像素级视觉特征对齐，以学习精细的视觉概念。
    *   **关键实验结论：** 实验结果通过可视化案例展示了模型对复杂语言表达的理解能力，尤其指出其在处理歧义性、标签标注问题和遮挡问题时的局限性。

*   **Zero-shot referring image segmentation based on fine-tuning image-text model CLIP (PixelCLIP)** [arocmag.cn](https://www.arocmag.cn/abs/2024.06.0254)
    *   **研究问题：** 针对 CLIP 模型在像素级图-文理解中丢失空间位置信息的不足，实现零样本指代图像分割。
    *   **核心方法：** 基于 CLIP 提出了一个单阶段、细粒度、多层次的 PixelCLIP 模型。通过多尺度图像特征融合聚合 CLIP 中不同视觉编码器提取的像素级特征，并结合文本的整体语义特征。引入 LLaVA 大语言模型注入上下文背景知识，通过细粒度跨模态关联匹配实现像素级分割。
    *   **关键实验结论：** 充分的数值分析结果验证了该方法的有效性，尤其在零样本设置下展现了对像素级参考图像分割的能力。

*   **Shatter and Gather: Learning Referring Image Segmentation with Text Supervision** [blog.csdn.net](https://blog.csdn.net/wzk4869/article/details/132752912)
    *   **研究问题：** 解决指代图像分割任务中训练数据手动标注昂贵和标记数据缺乏的问题，提出弱监督学习方法。
    *   **核心方法：** 提出一个新模型，首先发现输入图像中的语义实体，然后结合与这些实体相关的文本查询来预测分割掩码。引入新的损失函数，允许模型在没有进一步监督的情况下进行训练，仅使用训练图像的文本描述作为唯一监督来源。
    *   **关键实验结论：** 在四个公共基准测试上进行评估，显著优于相同任务的现有方法和最新的开放词汇分割模型。

#### 2. 统一多模态框架与高效交互

这类方法致力于构建统一的视觉-语言特征空间，简化模型架构，并探索更高效的特征融合与交互机制。

*   **OneRef: Towards Unified One-tower Expression Grounding and Segmentation with Mask Referring Modeling** [m.163.com](https://m.163.com/tech/article/KE2PBLP10511CQLG.html)
    *   **研究问题：** 现有视觉定位和指代分割工作严重依赖笨重的融合编码器/解码器和复杂的早期阶段交互技术，且传统掩码视觉语言建模（MVLM）无法捕捉细微指代关系。
    *   **核心方法：** 提出 OneRef，一个基于模态共享 Transformer 的极简指代框架，统一视觉和语言特征空间。引入掩码指代建模（MRefM）范式，包含指代感知的掩码图像建模和掩码语言建模，用于重构模态相关和跨模态指代内容，并采用指代感知的动态图像掩码策略。
    *   **关键实验结论：** 在定位和分割任务上连续超越现有方法，达到 SOTA 性能，为简化和统一指代框架提供了新思路。

*   **语言引导的多粒度特征融合目标分割方法** [bhxb.buaa.edu.cn](https://bhxb.buaa.edu.cn/bhzk/cn/article/doi/10.13700/j.bh.1001-5965.2022.0384)
    *   **研究问题：** 针对 Refvos 模型，提出一种能够对特定目标精准定位的语言引导的多粒度特征融合目标分割方法。
    *   **核心方法：** 利用 Swin Transformer 和 Bert 网络分别提取多粒度的视觉特征和文本特征，提高整体与细节的表征能力。将文本特征与不同粒度视觉特征融合，通过语言引导增强特定目标表达。通过卷积长短期记忆网络优化多粒度融合特征，促进不同粒度特征间的信息交流，得到更精细的分割结果。
    *   **关键实验结论：** 在 UNC, UNC+, G-Ref, ReferIt 数据集上进行测试，相比 Refvos，在 UNC 和 UNC+ 数据集的多个子集中 IoU 结果均有显著提升，并在 G-Ref 和 ReferIt 数据集上达到前沿水平。

#### 3. 强调边界和细节的高分辨率分割

为应对高分辨率图像中细节和边界的精确分割需求，这类方法通常引入分层处理、梯度监督或多尺度信息。

*   **BiRefNet: Bilateral Reference for High-Resolution Dichotomous Image Segmentation** [blog.csdn.net](https://blog.csdn.net/imwaters/article/details/144055641)
    *   **研究问题：** 传统方法难以在高分辨率 Dichotomous Image Segmentation (DIS) 任务中捕获非常细微的特征和精确的边界。
    *   **核心方法：** 提出一种新颖的渐进式双边参考网络 (BiRefNet)，将 DIS 任务分解为定位模块（LM）和重建模块（RM）。在 RM 中采用双边参考，包括内部参考（使用原始尺度的源图像块）和外部参考（使用梯度图进行边界监督），以增强模型对细节和边界的关注。
    *   **关键实验结论：** 在 DIS5K、HRSOD 和 COD 数据集上均取得了最先进的性能，特别是在细节区域和复杂边界分割方面表现突出，平均 Sm 指标有显著提升。

*   **多重边界参考的弱监督语义分割网络** [jcad.cn](https://www.jcad.cn/article/doi/10.3724/SP.J.1089.2023-00091)
    *   **研究问题：** 弱监督语义分割任务中，目标被重叠或遮挡时，种子区域生成的伪像素掩模难以准确覆盖目标区域，导致漏分割和错分割。
    *   **核心方法：** 设计一个边界探索模块，融合空间域边界和频率域边界，通过互参考得到目标区域边界。将这些边界作为参考信息输入网络，生成覆盖更准确目标区域的伪像素掩模。
    *   **关键实验结论：** 在 PASCAL VOC 2012 和 COCO 2014 数据集上的 mIoU 值分别达到 69.2% 和 40.6%，有效地改善了目标被遮挡或重叠时的分割精度问题。

#### 4. 交互式RIS与医学图像应用

交互式 RIS 允许用户通过少量交互修正模型预测，尤其在对精度要求极高的医学图像分割中展现出巨大潜力。

*   **多模式交互式图像分割** [lin-zheng.com](https://lin-zheng.com/paper/22_ACMMM_MMIIS/22_ACMMM_MMIIS_Paper_CN.pdf)
    *   **研究问题：** 针对医学图像分析模型中像素级标注稀缺和现有交互方法无法处理医学图像固有歧义性（不规则形状、模糊边界）的问题。
    *   **核心方法：** 提出一个多模式交互式医学图像分割框架，允许用户根据目标结构复杂程度选择初始交互模式（包围框、多边形、涂鸦），并在初始分割基础上综合利用区域和边界交互来修复错误标注。
    *   **关键实验结论：** 在广泛的医学图像数据集（X光、CT、MRI等）上验证，用户调研表明该框架显著减少了标注时间，并能处理多种歧义性，对现实世界的医学图像标注具有意义。

*   **SimTxtSeg: Weakly-Supervised Medical Image Segmentation with Simple Text Cues** [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/33107)
    *   **研究问题：** 旨在降低医学图像分割的标注成本，同时保持性能，尤其是在像素级注释昂贵且耗时的情况下。
    *   **核心方法：** 提出 SimTxtSeg 框架，利用简单的文本线索生成高质量伪标签，并通过文本到视觉线索转换器（Textual-to-Visual Cue Converter, TVCC）从文本提示生成边界框及其置信度分数，输入 SAM 生成伪掩膜。同时，设计文本引导分割模型，通过文本-视觉混合注意力（TVHA）解码器融合语义和图像特征。
    *   **关键实验结论：** 在结肠息肉分割和 MRI 脑肿瘤分割任务上，SimTxtSeg-w-TVHA 模型超越了所有现有弱监督方法，mDice 和 mIoU 均有显著提升，即使文本线索是最弱的监督形式，也实现了卓越性能。

### 实验与评价总结

2022-2025年 RIS 领域的实验普遍遵循以下趋势和共性结论：

1.  **大规模预训练模型的普适性与挑战：** CLIP 等视觉-语言大模型因其强大的泛化能力成为 RIS 领域的有力基石。然而，其在像素级精度上的固有局限性促使研究者开发针对性的微调策略、适配器或定制解码器，以弥补其对空间位置信息的不足。直接应用于像素级别任务时，大模型需要更细致的上下文理解和局部信息捕捉能力。
2.  **跨模态融合的深化：** 无论是早期简单拼接，还是基于 Transformer 的多头自注意力、交叉注意力机制，都在不断探索更高效、更具语义感知的视觉-语言特征融合方式。多粒度特征融合、动态掩码策略等被提出以更好地对齐和交互不同模态的信息。
3.  **高分辨率与细节捕捉的重要性：** 随着图像采集技术的发展，高分辨率数据的处理成为必需。对细微结构、模糊边界和复杂背景的鲁棒性是衡量模型性能的关键。基于梯度信息、双边参考、边界探索等技术被广泛用于提升分割的精细度。
4.  **弱监督与零样本学习的兴起：** 面对昂贵的像素级标注，利用文本描述、边界参考甚至无监督信息进行弱监督或零样本学习成为重要方向，旨在降低标注成本并提高模型泛化能力。实验表明这些方法在一定程度上可以达到甚至超越完全监督模型的性能。
5.  **交互式方法的价值：** 对于对精度要求高、歧义性强的场景（如医学图像），交互式 RIS 提供了修正和优化的手段。多模式交互（区域、边界、点击、涂鸦）的灵活性和协同性已被验证能有效提升标注效率和准确性。

### 趋势与挑战

2025 年 RIS 领域的研究将继续深化，未来趋势和挑战包括：

1.  **更高效的视觉-语言大模型适配：** 随着多模态大模型的不断演进，如何以更低训练成本、更高效率将其通用知识适配到像素级 RIS 任务是核心趋势。这可能涉及更精巧的参数高效微调（Parameter-Efficient Fine-tuning, PEFT）方法，或设计更具特异性的感知解码器，以平衡通用性与像素精度。
2.  **三维（3D）和时序（Temporal）RIS：** 当前大部分 RIS 研究集中在二维静态图像。然而，在自动驾驶、虚拟现实、医疗影像（如 CT, MRI 序列）等领域，三维和时序 RIS 具有巨大应用前景。这要求模型不仅能理解空间语言，还能理解时序动态，挑战在于如何高效处理高维数据和复杂的时空上下文。
3.  **可解释性与鲁棒性提升：** 随着 RIS 应用到高风险领域（如医疗诊断），模型的决策过程可解释性变得至关重要。同时，针对现实世界中的噪声、歧义性语言、视角变化和遮挡等情况，提升模型的鲁棒性和泛化能力仍是长期挑战。结合因果推理、对抗学习等技术可能成为研究方向。

### 结论

近三年来，Referring Image Segmentation 技术在视觉-语言大模型的推动下取得了显著进步。研究人员在跨模态特征融合、像素级细节捕捉、弱监督学习以及交互式分割等方面提出了众多创新方法。这些进展不仅提升了 RIS 的性能上限，也拓宽了其应用场景。然而，如何进一步提高模型的效率、在复杂高维数据上的表现、以及在实际应用中的可解释性和鲁棒性，仍将是未来研究的重点。

### 参考文献

*   [cnblogs.com](https://www.cnblogs.com/lipoicyclic/p/16807808.html) 脂环. CRIS: CLIP-Driven Referring Image Segmentation论文阅读笔记. 2022-10-19.
*   [arocmag.cn](https://www.arocmag.cn/abs/2024.06.0254) 刘杰, 乔文昇, 朱佩佩, 雷印杰, 王紫轩. 基于图像-文本大模型CLIP微调的零样本参考图像分割. 计算机应用研究, 2025, **42** (4).
*   [blog.csdn.net](https://blog.csdn.net/wzk4869/article/details/132752912) CSDN. 【图像分割】arxiv 计算机视觉关于图像分割的学术速递（8 月 31 日论文合集）. 2023-09-08. (包含 “Shatter and Gather: Learning Referring Image Segmentation with Text Supervision” 论文信息)
*   [m.163.com](https://m.163.com/tech/article/KE2PBLP10511CQLG.html) 将门创投. OneRef：一刀砍掉融合模块，极简One-tower统一框架. 2025-11-11.
*   [bhxb.buaa.edu.cn](https://bhxb.buaa.edu.cn/bhzk/cn/article/doi/10.13700/j.bh.1001-5965.2022.0384) 谭荃戈, 王蓉, 吴澳. 语言引导的多粒度特征融合目标分割方法. 北京航空航天大学学报, 2024, 50(2): 542-550.
*   [blog.csdn.net](https://blog.csdn.net/imwaters/article/details/144055641) imwaters. 【论文+去背景】24.01.BiRefNet:Bilateral Reference for High-Resolution Dichotomous高分辨率二分图像分割的双边参考 (RMBG背后的算法. 2024-12-12.
*   [jcad.cn](https://www.jcad.cn/article/doi/10.3724/SP.J.1089.2023-00091) 杨大伟, 迟津生, 毛琳. 多重边界参考的弱监督语义分割网络. 计算机辅助设计与图形学学报, 2024-05-15.
*   [lin-zheng.com](https://lin-zheng.com/paper/22_ACMMM_MMIIS/22_ACMMM_MMIIS_Paper_CN.pdf) Zheng Lin, Zhao Zhang, Ling-Hao Han, Shao-Ping Lu. 多模式交互式图像分割. Proceedings of the 30th ACM International Conference on Multimedia (MM ’22), 2022.
*   [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/33107) Yuxin Xie, Tao Zhou, Yi Zhou, Geng Chen. SimTxtSeg: Weakly-Supervised Medical Image Segmentation with Simple Text Cues. arXiv preprint arXiv:2406.19364, 2024.
*   [opticsjournal.net](https://www.opticsjournal.net/Articles/OJ2b2078a8cf027f69/km) 尹艺晓, 马金刚, 张文凯, 姜良. 从U-Net到Transformer：混合模型在医学图像分割中的应用进展. 激光与光电子学进展, 2025, 62(2): 0200001.