## 状态空间模型在图像处理中的应用研究综述 (2022-2025)

### 引言

近年来，深度学习在图像处理领域取得了显著进展，其中卷积神经网络（CNN）和Transformer模型占据主导地位。然而，CNN在建模长距离依赖方面存在局限性，而Transformer的自注意力机制则面临二次计算复杂度高、内存消耗大的挑战，这限制了它们在处理高分辨率图像和实时应用中的效率。受自然语言处理（NLP）领域中Mamba等状态空间模型（State Space Models, SSMs）突破性进展的启发，研究者们开始探索将SSMs引入图像处理任务，以期结合其线性计算复杂度和建模长序列依赖的能力，开辟新的研究方向。本文旨在综述2022-2025年间状态空间模型在图像处理领域的代表性工作，重点关注其在图像恢复、超分辨率、视频处理等任务中的应用，并分析其优势、挑战与未来趋势。

### 方法分类与代表作

目前，SSMs在图像处理中的应用主要围绕如何将一维序列建模能力拓展至二维图像数据，并解决特定视觉任务中的挑战。

#### 1. 图像恢复与超分辨率

图像恢复任务旨在从退化图像中重建高质量图像，超分辨率则是其重要分支。传统SSM在处理二维图像时常面临局部空间结构破坏和通道信息利用不足的问题。

*   **MambaIR与PMambaIR**

    [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/99851) MambaIR提出了一个基于改进Mamba的状态空间模型，用于图像恢复，特别是图像超分辨率。针对标准Mamba的局部像素遗忘和通道冗余问题，MambaIR通过引入局部增强和通道注意力机制来优化，实现了全局感受野和计算效率的同时提升。实验结果显示，MambaIR在图像超分辨率任务中比SwinIR性能提升高达0.45dB，且计算成本相似。
    [opticsjournal.net](https://www.opticsjournal.net/Articles/OJc95fb11550c4c2a5/FullText) 耿树泽等人在MambaIR基础上进一步提出PMambaIR，一种基于全方位状态空间模型的轻量化图像超分辨率重建算法。该研究通过引入级联扫描策略和混合状态空间块（HSSB），促进局部、跨尺度和全局信息的有效交互，同时从空间和通道两个维度对像素信息进行交互建模，以提升特征提取能力并限制无关特征影响。PMambaIR在多个基准数据集上相较现有模型平均PSNR提升0.11dB，且参数量和计算量较小，显示出其在效率和性能上的优势。

*   **MambaIRv2**

    [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/85148) MambaIRv2旨在解决早期Mamba模型固有的因果建模限制，即像素信息仅依赖于扫描序列中的前驱，导致对图像像素的利用不充分。该模型通过引入“注意状态空间方程”，赋予Mamba类似于ViT的非因果建模能力，并通过一次扫描促进图像展开，从而更充分利用图像信息。此外，MambaIRv2引入了语义引导的邻域机制，以鼓励远距离但相似像素之间的交互。该模型在轻量级超分辨率任务中比SRFormer的PSNR提升高达0.35dB，并在经典超分辨率任务中比HAT提升高达0.29dB。

*   **MambaLLIE**

    [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/81997) MambaLLIE提出了一种基于Retinex感知的低光照图像增强器，其核心在于全局-局部状态空间设计。针对传统方法在同时解决全局照明衰退和局部噪声、模糊问题上的不足，MambaLLIE提出了局部增强状态空间模块（LESSM），通过增强局部偏差来保留二维局部依赖性，并设计了隐式Retinex感知选择性核模块（IRSK）进行自适应核选择。该模型通过结合LESSM和IRSK于全局-局部状态空间块中，实现了全面的全局长程建模和灵活的局部特征聚合，显著优于现有基于CNN和Transformer的方法。

#### 2. 视频处理与医学影像分割

视频数据具有额外的时间维度，长时序依赖建模是其关键挑战。SSMs的线性计算复杂度使其在处理长视频序列时具有潜在优势。

*   **VFIMamba**

    [zhuanzhi.ai](https://zhuanzhi.ai/paper/6676a3ce7d5f83d5193d3108b1eff5c2) VFIMamba提出了一种新颖的视频帧插值方法，用于高效动态的帧间建模。该方法引入了混合SSM块（MSB），通过交错排列相邻帧的tokens并应用多方向S6建模，促进帧间信息传递。VFIMamba通过渐进式学习策略，逐步提升模型在不同运动幅度下的帧间动态建模能力，在X-TEST数据集上，4K帧和2K帧的性能分别提升0.80dB和0.96dB。

*   **医学视频分割算法**

    [jeit.ac.cn](https://jeit.ac.cn/cn/article/doi/10.11999/JEIT240755?viewType=HTML) 丁建睿等提出了一种融合邻域注意力和状态空间模型的医学视频分割算法，旨在精准捕捉医学视频中的时空特征。该算法通过两阶段设计，首先使用深度卷积网络结合邻域注意力机制捕获低层次空间语义和局部时序语义关联，再引入状态空间模型捕捉全面的时序信息并再次应用邻域注意力模块，以增强局部时序特征敏感度。该方法有效整合了视频中的时序信息，并在甲状腺超声和结肠息肉视频数据集上，IOU指标分别达到72.7%、82.3%和72.5%，相较基线模型Vivim分别提高了5.7%、1.7%和5.5%。

#### 3. 通用视觉骨干网络与自适应扫描机制

直接将Mamba从NLP迁移到视觉通常会破坏图像的空间邻接关系，因此设计有效的扫描策略至关重要。

*   **PointMamba**

    [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/83497) PointMamba将Mamba成功应用于点云分析任务。针对Transformer在点云分析中全局建模能力强但注意力机制复杂度高的问题，PointMamba利用空间填充曲线高效点标记化，并采用简单的非层次化Mamba编码器作为骨干。该模型在多个数据集上实现了优越性能，同时显著减少了GPU内存使用和浮点运算次数（FLOPs），为3D视觉任务提供了新的SSM基线。

*   **DAMamba**

    [blog.csdn.net](https://blog.csdn.net/u014546828/article/details/153121475) DAMamba提出了一种具备动态自适应扫描（DAS）机制的视觉状态空间模型。针对现有视觉SSM人工设计扫描方法破坏空间邻接性和缺乏灵活性的问题，DAS通过数据驱动方式自适应分配扫描顺序与区域，以实现更灵活的建模效能，同时保持线性计算复杂度和全局建模能力。DAMamba在图像分类、目标检测、实例分割和语义分割等任务中显著优于现有视觉Mamba模型，甚至超越了一些最新的顶尖CNN和ViT模型。

#### 4. 风格迁移

*   **Mamba-ST**

    [blog.csdn.net](https://blog.csdn.net/weixin_56848903/article/details/145677503) Mamba-ST提出了一种基于SSM的风格迁移新架构，旨在解决传统Transformer和扩散模型在风格迁移中计算负担高和推理时间长的问题。该模型通过改造Mamba的线性方程来模拟跨注意力层的行为，使其能够接收并融合双数据流输入（内容和风格），从而在不依赖额外层（如AdaLN）的情况下实现内容-风格交互。Mamba-ST在ArtFID和FID指标上均有提升，且内存占用显著低于Transformer，推理速度远超扩散模型。

### 实验与评价总结

综合来看，状态空间模型在图像处理领域的应用展现出显著优势。在计算效率方面，SSMs普遍能够实现线性或近线性的计算复杂度，显著优于Transformer的二次方复杂度，尤其是在处理高分辨率图像和长序列视频时，这种优势更为明显，能够降低GPU内存使用和浮点运算次数。在性能方面，Mamba及其变体通过引入局部增强、通道注意力、邻域机制、动态自适应扫描策略等改进，有效解决了标准Mamba在处理视觉数据时局部信息不足、空间结构破坏和通道冗余等问题，使得模型能够有效捕捉图像的长距离依赖和丰富的局部细节。在多种视觉任务中，包括图像超分辨率、低光照增强、医学视频分割、视频帧插值、点云分析，以及图像风格迁移，基于SSM的方法均取得了与甚至超越现有SOTA CNN和Transformer模型的性能，例如MambaIR和PMambaIR在超分辨率任务上超越SwinIR，MambaIRv2超越SRFormer和HAT，DAMamba在多种任务上超越现有视觉Mamba和部分CNN/ViT模型。此外，通过融合SSM与特定机制（如邻域注意力、Retinex感知等），SSMs在特定任务中表现出更高的细节恢复能力和时空信息整合能力。虽然SSMs相较于Transformer在内存和速度上有明显提升，但其在处理二维图像时如何克服一维序列建模的固有局限，实现对复杂图像结构的灵活捕捉，仍然是研究重点。

### 趋势与挑战

2025年前后，状态空间模型在图像处理领域的研究将呈现以下趋势：

1.  **高级扫描策略与结构设计**：随着DAMamba等工作证明了动态自适应扫描的潜力，未来的研究将更侧重于开发数据驱动、内容感知的扫描策略，而非固定模式。这可能包括结合图神经网络或强化学习来动态优化扫描路径，以更精准地捕捉图像中的非局部和多尺度依赖。同时，如何将这些高级扫描机制无缝集成到SSM的层级结构中，以构建更强大的视觉骨干网络，将是核心研究方向。
2.  **多模态与多任务融合**：SSMs将不仅仅局限于单一图像处理任务，而是会向多模态数据（如图像-文本、视频-音频等）和多任务学习方向发展。例如，Mamba-ST展示了其在风格迁移任务中的潜力，未来可以探索SSMs在更广泛的生成任务、跨模态内容生成与理解，以及统一的视觉-语言模型中的应用，结合其长序列建模的优势，处理更复杂的感知与推理任务。
3.  **效率与可解释性并重**：虽然SSMs在效率上优于Transformer，但对其内部工作机制的理解和可解释性仍有待提升。未来的研究将致力于开发更透明、可解释的SSM变体，例如通过可视化中间状态、选择机制和扫描轨迹，帮助研究人员更好地理解模型决策过程，从而指导模型设计和改进。此外，如何进一步优化SSMs以在资源受限设备上实现高效部署，将是实际应用中的重要考量。

### 结论

状态空间模型为图像处理领域带来了新的范式，提供了一种兼顾全局感受野与线性计算复杂度的解决方案。从图像恢复到视频处理，再到通用视觉骨干网络和风格迁移，SSMs展现出强大的潜力和竞争力。尽管仍面临如何将一维序列建模能力最优地应用于二维和多维视觉数据等挑战，但通过创新的扫描策略、结构设计和机制融合，SSMs有望在未来的图像处理技术中扮演越来越重要的角色。

### 参考文献

1.  [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/99851) Guo, H., Li, J., Dai, T., et al. (2024). MambaIR: A Simple Baseline for Image Restoration with State-Space Model. ECCV 2024.
2.  [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/85148) Guo, H., Guo, Y., Zha, Y., et al. (2024). MambaIRv2: Attentive State Space Restoration. arXiv preprint arXiv:2411.15269.
3.  [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/81997) Weng, J., Yan, Z., Tai, Y., et al. (2024). MambaLLIE: Implicit Retinex-Aware Low Light Enhancement with Global-then-Local State Space. NeurIPS 2024.
4.  [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/20753) Guan, M., Xu, H., Jiang, G., et al. (2024). WaterMamba: Visual State Space Model for Underwater Image Enhancement. arXiv preprint arXiv:2405.08419.
5.  [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/83497) Liang, D., Zhou, X., Xu, W., et al. (2024). PointMamba: A Simple State Space Model for Point Cloud Analysis. NeurIPS 2024.
6.  [blog.csdn.net](https://blog.csdn.net/u014546828/article/details/153121475) (2025). DAMamba：具备动态自适应扫描机制的视觉状态空间模型 [NeurIPS 2025].
7.  [blog.csdn.net](https://blog.csdn.net/weixin_56848903/article/details/145677503) (2025). 《Mamba-ST：面向高效风格迁移的状态空间模型》学习笔记. WACV.
8.  [opticsjournal.net](https://www.opticsjournal.net/Articles/OJc95fb11550c4c2a5/FullText) 耿树泽, 宋子怡, 阎刚. (2025). 基于全方位状态空间模型的轻量化图像超分辨率重建. 液晶与显示, 40(4): 642.
9.  [jeit.ac.cn](https://jeit.ac.cn/cn/article/doi/10.11999/JEIT240755?viewType=HTML) 丁建睿, 张听, 刘家栋, 宁春平. (2025). 融合邻域注意力和状态空间模型的医学视频分割算法. 电子与信息学报, 47(5): 1582-1595.
10. [zhuanzhi.ai](https://zhuanzhi.ai/paper/6676a3ce7d5f83d5193d3108b1eff5c2) Zhang, G., Liu, C., Cui, Y., et al. (2024). VFIMamba: Video Frame Interpolation with State Space Models.
11. Gu, A. & Dao, T. (2023). Mamba: Linear-time Sequence Modeling with Selective State Spaces. arXiv preprint arXiv:2312.00752.
12. Liu, Y., Tian, Y. J., Zhao, Y. Z., et al. (2024). VMamba: Visual state space model. NeurIPS 2024.