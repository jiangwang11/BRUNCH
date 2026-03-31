好的，作为一名严谨的科研助手，我将基于提供的联网搜索结果，为您生成一篇关于“状态空间模型在图像处理中的应用”的中文学术综述。

***

## 状态空间模型在图像处理中的应用：2022-2025年进展综述

### 引言

在深度学习时代，图像处理领域长期由卷积神经网络（CNNs）和视觉变换器（Vision Transformers, ViTs）主导。CNNs凭借其强大的局部特征提取能力和归纳偏置成为基石，而ViTs则通过自注意力机制实现了卓越的全局依赖建模，但在处理高分辨率图像时面临二次方计算复杂度的挑战 [blog.csdn.net](https://blog.csdn.net/u014546828/article/details/153121475)。为寻求性能与效率的更优平衡，研究界开始探索新的架构范式。

状态空间模型（State Space Models, SSMs），源于经典控制理论，旨在通过隐状态序列来描述系统动态 [zhuanzhi.ai](https://zhuanzhi.ai/paper/7d751a091194b41e7c0601c3cbac1b00)。最初的SSMs因训练复杂性未能在视觉领域广泛应用。然而，随着结构化SSM（S4）及尤其是Mamba模型的出现（2023年），其通过选择性机制和硬件感知设计，在保持全局感受野的同时实现了与序列长度呈线性的计算复杂度，彻底点燃了SSM在序列建模任务中的革命 [www.opticsjournal.net](https://www.opticsjournal.net/Articles/OJc95fb11550c4c2a5/FullText)。自2024年起，将Mamba架构应用于二维图像处理成为研究热点。本文旨在系统梳理并评述2022至2025年间，状态空间模型在图像处理领域的代表性工作、关键挑战与未来趋势。

### 方法分类与代表作

将SSM应用于图像处理的核心挑战在于如何将本质上为一维序列设计的模型有效适配于二维或更高维的视觉数据。当前研究主要围绕扫描策略、模型结构和特定任务进行创新。

#### 1. 图像复原与增强

该领域工作主要致力于解决传统网络在感受野和计算成本间的矛盾，并针对标准Mamba的不足进行优化。

*   **MambaIR (2024)**：该研究提出一个简单的图像复原基线模型，旨在解决标准Mamba在低级视觉任务中存在的局部像素遗忘和通道冗余问题。其核心方法是在原始Mamba模块中引入局部增强（local enhancement）和通道注意力（channel attention），从而更好地利用局部像素相似性并减少通道间冗余。实验表明，在相似计算成本下，MambaIR在图像超分辨率任务上比代表性的SwinIR模型提升高达0.45dB，并实现了全局有效感受野 [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/99851)。

*   **PMambaIR (2025)**：针对MambaIR中将二维图像展平为一维序列时破坏局部空间结构的问题，该工作提出了一种全方位状态空间轻量化超分辨率模型。其创新点在于设计了“级联扫描策略”（cascaded scanning strategy），通过局部窗口、跨区域和全局三个尺度进行渐进式特征提取。同时，其提出的“混合状态空间块”（HSSB）结合了Mamba的空间建模与通道注意力的通道交互能力。在Urban100×4数据集上，该方法以相近的计算量超越了MambaIR约0.12 dB，验证了全方位信息提取的有效性 [www.opticsjournal.net](https://www.opticsjournal.net/Articles/OJc95fb11550c4c2a5/FullText)。

*   **WaterMamba (2024)**：该工作将SSM应用于极具挑战性的水下图像增强（UIE）任务，旨在解决CNN长距离依赖建模不足及Transformer计算量大的问题。作者提出了包含“空间-通道全向选择扫描”（SCCOSS）模块的空间-通道选择扫描块，能够同时对像素流和通道流进行建模。在多个UIE基准数据集上，WaterMamba在参数和计算量显著减少的情况下，取得了超越当时SOTA方法的性能 [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/20753)。

#### 2. 通用视觉骨干网络

此类研究旨在构建可广泛应用于分类、检测、分割等多种任务的通用SSM骨干网络，其核心在于设计更优的图像到序列的转换机制。

*   **DAMamba (2025)**：该研究批判了现有视觉SSM依赖人工设计固定扫描模式（如逐行扫描、Z形扫描）的局限性，认为这会破坏图像的语义空间邻接性且缺乏灵活性。为此，它提出了“动态自适应扫描”（Dynamic Adaptive Scan, DAS），一种数据驱动的方法，通过一个可学习的偏移预测网络动态地学习扫描区域和顺序。基于DAS构建的DAMamba骨干网络，在图像分类（ImageNet-1K上准确率达85.2%）、目标检测和语义分割等多个任务上，显著超越了VMamba等前期视觉Mamba模型，并超过了部分顶尖的CNN和ViT模型 [blog.csdn.net](https://blog.csdn.net/u014546828/article/details/153121475)。

*   **MambaIRv2 (2024)**：此工作旨在解决Mamba固有的因果建模（causal modeling）限制，即每个标记仅依赖于序列中的前驱，这限制了模型对像素信息的充分利用。为此，作者提出了“注意力状态空间方程”（attentive state-space equation），赋予Mamba类似ViTs的非因果建模能力，允许模型关注扫描序列之外的像素。在轻量级超分辨率任务上，MambaIRv2比SRFormer的PSNR提升了0.35dB，同时参数更少，显示出非因果建模的巨大潜力 [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/85148)。

#### 3. 视频与高维数据处理

SSM的序列建模特性天然契合视频等时序数据。研究者们探索利用SSM高效捕获时空依赖。

*   **融合邻域注意力和SSM的医学视频分割 (2025)**：该研究针对医学视频分割中精确捕获时空特征的需求，提出一种两阶段算法。第一阶段使用CNN和邻域注意力（Neighborhood Attention）捕获局部时空关联，第二阶段引入SSM以线性复杂度捕捉长程时序信息。实验结果显示，在甲状腺超声视频等数据集上，该方法的交并比（IOU）指标相较于基线模型Vivim提升了高达5.7%，且模型推理速度满足临床实时性要求 [jeit.ac.cn](https://jeit.ac.cn/cn/article/doi/10.11999/JEIT240755?viewType=HTML)。

*   **PointMamba (2024)**：该工作将SSM的应用从2D图像拓展至3D点云分析，挑战在于如何处理无序且非结构化的点云数据。该方法利用空间填充曲线（space-filling curves）对点云进行有效排序和标记化，然后输入到一个极简的非层级式Mamba编码器中。在多个点云分析基准上，PointMamba以更低的GPU内存和计算成本实现了卓越性能，展示了SSM在处理3D视觉数据方面的潜力 [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/83497)。

*   **VFIMamba (2024)**：针对视频帧插值（VFI）任务，该研究提出VFIMamba以实现高效的帧间动态建模。其核心是“混合SSM块”（Mixed-SSM Block），它首先将相邻帧的令牌交错排列，然后应用多方向的S6建模。这种设计有效促进了跨帧信息传递，同时保持了线性复杂度，在高分辨率VFI场景（如4K）中取得了显著的性能提升 [zhuanzhi.ai](https://zhuanzhi.ai/paper/6676a3ce7d5f83d5193d3108b1eff5c2)。

#### 4. 图像生成与风格化

利用SSM进行图像生成和编辑是新兴方向，旨在替代计算昂贵的Transformer或推理缓慢的扩散模型。

*   **Mamba-ST (2025)**：此工作旨在解决风格迁移任务中Transformer计算负担重和扩散模型推理慢的问题，首次将SSM成功适配于该任务。其核心创新在于，不依赖外部的跨注意力或AdaLN模块，而是直接修改Mamba模型内部的SSM方程（使状态矩阵依赖风格输入，输出矩阵依赖内容输入），以模拟跨注意力机制的行为。实验证明，Mamba-ST在ArtFID和FID等指标上与SOTA方法相当，但内存占用远低于Transformer，推理速度远快于扩散模型 [blog.csdn.net](https://blog.csdn.net/weixin_56848903/article/details/145677503)。

### 实验与评价总结

综合分析上述代表性工作，可以总结出关于SSM在图像处理中的共性结论：

1.  **性能与效率的平衡**：SSM架构，特别是基于Mamba的模型，已证明其在多种图像处理任务上能达到甚至超越顶尖ViT和CNN架构的性能。其核心优势在于以线性计算复杂度实现了全局感受野，在高分辨率输入（如图像复原、分割、高分辨率视频）场景下，展现出相较于Transformer更优的性能-效率权衡曲线 [blog.csdn.net](https://blog.csdn.net/u014546828/article/details/153121475)。

2.  **扫描策略至关重要**：消融实验普遍证实，将2D图像简单展平为1D序列会损害空间局部性，性能不佳。采用多方向扫描（如MambaIR）、多尺度级联扫描（如PMambaIR）乃至数据驱动的动态自适应扫描（如DAMamba）是发挥SSM能力的关键。智能化的扫描机制能显著提升模型性能。

3.  **与传统模块的协同**：纯SSM架构在捕捉某些视觉先验（如通道依赖、精细局部纹理）方面可能存在不足。研究表明，将SSM与通道注意力（如MambaIR）、卷积（如PMambaIR）或邻域注意力（如医学视频分割算法）等模块结合，可以互补优势，进一步提升模型整体性能。

4.  **模型内机制创新的潜力**：早期的工作倾向于将Mamba作为一个黑盒模块替换Transformer，而后期工作（如Mamba-ST, MambaIRv2）开始深入探索并改造SSM的内部方程，以实现更复杂的跨信息流融合或非因果建模。这表明SSM架构本身具有高度的可塑性和巨大的创新空间。

### 趋势与挑战

基于现有研究，可以预见状态空间模型在图像处理领域的未来发展将呈现以下趋势，并面临相应挑战：

1.  **趋势一：扫描机制的智能化与无序化**。从人工固定的扫描发展到数据驱动的动态自适应扫描（DAMamba）已显示出巨大潜力。未来，研究将进一步探索完全无序的、基于图或注意力引导的“扫描”机制，彻底摆脱序列化假设，使模型能更自然地处理图像和点云等非欧几里得数据。

2.  **趋势二：模型机理的深度融合**。研究将从“SSM+其他模块”的外部拼接，转向“SSM内部机理”的深度融合。例如，将自注意力的非因果、全连接特性与SSM的线性、递归特性在底层方程层面进行统一，可能催生出新一代兼具二者优点的“混合态”架构，如MambaIRv2的初步探索。

3.  **趋势三：向4D与多模态领域的渗透**。SSM在视频和点云处理上的成功预示着其将大规模应用于更复杂的时空数据，如动态医学成像（fMRI）、自动驾驶中的多传感器时序数据（LiDAR序列+视频）等4D视觉任务。此外，通过类似Mamba-ST的内部融合机制，SSM有望在多模态（如视觉-语言）任务中成为比Cross-Attention更高效的融合骨干。

**挑战**：
*   **可解释性**：相比于ViT中清晰的注意力图，SSM的隐状态`h(t)`是一个高度压缩的、动态演化的向量，其物理或语义意义尚不明确，这为模型的可解释性带来了新的挑战。
*   **硬件适配性**：Mamba的高效性部分依赖于针对现代GPU的硬件感知算法（如FlashAttention类似的核融合与并行扫描）。将其高效部署到资源受限的边缘设备或非英伟达架构的硬件上，仍需专门的算法与工程优化。

### 结论

自2023年Mamba模型问世以来，状态空间模型（SSM）已迅速成为图像处理领域继CNN和ViT之后的第三大支柱性架构。通过创新的扫描策略和模型结构设计，视觉SSM在图像复原、分割、检测乃至视频和3D数据处理等广泛任务中，成功地在全局依赖建模与线性计算复杂度之间取得了前所未有的平衡。研究表明，智能化的扫描机制、与传统视觉模块的协同以及对SSM内部机理的改造是释放其潜力的关键。展望未来，随着扫描机制的进一步演进、模型机理的深度融合以及向更高维度和多模态任务的拓展，SSM必将在构建下一代高效、高性能的视觉智能系统中扮演愈发核心的角色。

### 参考文献

1.  Guo, H., Li, J., Dai, T., et al. (2024). *MambaIR: A Simple Baseline for Image Restoration with State-Space Model*. ECCV 2024. [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/99851)
2.  Yan, G., Song, Z., & Geng, S. (2025). PMambaIR: panoramic vision state space model for lightweight image super-resolution. *Chinese Journal of Liquid Crystals and Displays*. [www.opticsjournal.net](https://www.opticsjournal.net/Articles/OJc95fb11550c4c2a5/FullText)
3.  Guan, M., Xu, H., Jiang, G., et al. (2024). *WaterMamba: Visual State Space Model for Underwater Image Enhancement*. arXiv. [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/20753)
4.  Ltzovo et al. (2025). *DAMamba: Vision State Space Model with Dynamic Adaptive Scan*. NeurIPS 2025. [blog.csdn.net](https://blog.csdn.net/u014546828/article/details/153121475)
5.  Guo, H., Guo, Y., Zha, Y., et al. (2024). *MambaIRv2: Attentive State Space Restoration*. arXiv. [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/85148)
6.  Ding, J., Zhang, T., Liu, J., & Ning, C. (2025). A Medical Video Segmentation Algorithm Integrating Neighborhood Attention and State Space Model. *Journal of Electronics & Information Technology*. [jeit.ac.cn](https://jeit.ac.cn/cn/article/doi/10.11999/JEIT240755?viewType=HTML)
7.  Liang, D., Zhou, X., Xu, W., et al. (2024). *PointMamba: A Simple State Space Model for Point Cloud Analysis*. NeurIPS 2024. [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/83497)
8.  Zhang, G., Liu, C., Cui, Y., et al. (2024). *VFIMamba: Video Frame Interpolation with State Space Models*. arXiv. [zhuanzhi.ai](https://zhuanzhi.ai/paper/6676a3ce7d5f83d5193d3108b1eff5c2)
9.  Botti, F. et al. (2025). *Mamba-ST: A State Space Model for Efficient Style Transfer*. WACV. [blog.csdn.net](https://blog.csdn.net/weixin_56848903/article/details/145677503)
10. Gu, A., & Dao, T. (2023). *Mamba: Linear-Time Sequence Modeling with Selective State Spaces*. arXiv.
11. Liu, Y., Tian, Y., Zhao, Y., et al. (2024). *VMamba: Visual State Space Model*. arXiv.
12. Wei, J., Holtz, J., Dillig, I., & Biswas, J. (2022). *STEADY: Simultaneous State Estimation and Dynamics Learning from Indirect Observations*. IROS 2022. [zhuanzhi.ai](https://zhuanzhi.ai/paper/7d751a091194b41e7c0601c3cbac1b00)