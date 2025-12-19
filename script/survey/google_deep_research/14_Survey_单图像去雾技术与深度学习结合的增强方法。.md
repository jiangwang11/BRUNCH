单图像去雾技术与深度学习结合的增强方法：2022–2025 年学术综述
摘要
单图像去雾（Single Image Dehazing）作为计算机低层视觉（Low-level Vision）领域的核心挑战之一，旨在从受大气散射影响的退化图像中恢复出具有高保真度的清晰场景。这一技术在自动驾驶、远程监控、卫星遥感及水下探测等领域具有无可替代的应用价值。随着深度学习技术的迭代演进，特别是 2022 年至 2025 年间，该领域经历了从单纯的卷积神经网络（CNN）向以视觉 Transformer（ViT）为代表的全局建模架构、以扩散模型（Diffusion Models）为核心的生成式恢复范式，以及无监督/半监督学习驱动的真实世界适应性方法的深刻变革。

本综述旨在系统性地梳理这一时期内出现的具有里程碑意义的科研成果。报告将深入剖析基于 Transformer 的线性化注意力机制改进、扩散模型中的潜空间（Latent Space）挖掘与物理提示（Physics Prompting）策略，以及无监督对比学习在解决域漂移（Domain Shift）问题上的理论突破。我们将详细论述 DehazeFormer、MB-TaylorFormer、RIDCP、DiffLI2D、ProDehaze、UCL-Dehaze、Semi-UFormer、USID-Net、DEA-Net 及 FALCON 等代表性算法的内在机理，并通过详实的定量实验数据对比其在合成数据集（SOTS）与真实世界基准（Dense-Haze, NH-HAZE）上的性能表现。最后，基于 2024-2025 年的最新文献，本文将预测“物理感知生成”（Physics-Informed Generative AI）、“零样本适应”（Zero-Shot Adaptation）及“频域高效计算”将是未来技术演进的主流方向。

1. 引言：从物理模型到生成式先验的演变
1.1 大气散射模型与去雾的病态性
在深入探讨现代深度学习方法之前，必须重申去雾任务的物理基础。在计算机视觉中，雾霾图像的形成通常由麦卡特尼（McCartney）提出的大气散射模型（Atmospheric Scattering Model, ASM）描述。该模型不仅是传统方法的基石，也是 2025 年最新“物理感知”深度学习方法的理论依据。其数学表达为：

I(x)=J(x)t(x)+A(1−t(x))
其中，I(x) 是传感器接收到的有雾观测图像，J(x) 是待恢复的无雾场景辐射度，A 是全球大气光强度（通常假设为全局常量，但在非均匀雾霾中为变量），t(x) 是透射率图（Transmission Map），描述了光线穿透介质的能力。透射率 t(x) 进一步由场景深度 d(x) 和大气散射系数 β 决定，遵循比尔-朗伯定律（Beer-Lambert Law）：t(x)=e 
−βd(x)
 。

单图像去雾是一个典型的不适定（Ill-posed）反问题。在仅已知 I(x) 的情况下，我们需要同时估计 J(x)、t(x) 和 A 三个未知量。传统的非学习方法主要依赖手工设计的统计先验，如暗通道先验（Dark Channel Prior, DCP），假设局部区域内至少有一个颜色通道的强度趋近于零。然而，这些先验在天空区域、白色物体表面或浓雾场景下往往失效，导致颜色失真或伪影。

1.2 深度学习时代的范式转移（2016-2021）
随着深度神经网络（DNN）的引入，去雾方法经历了初步的革新。早期的 AOD-Net 通过重构大气散射模型，实现了端到端的参数估计；随后的 FFA-Net 引入了特征融合注意力机制，显著提升了特征提取能力。然而，截至 2021 年，主流方法主要由卷积神经网络（CNN）主导。CNN 虽然在提取局部特征方面表现出色，但其受限的感受野（Receptive Field）使得模型难以捕捉雾霾在图像中的长距离依赖和全局分布特性。

1.3 2022-2025 年的技术爆发
进入 2022 年后，学术界开始寻求超越纯 CNN 架构的解决方案，形成了三大显著的技术流派，这也是本综述的核心讨论对象：

全局建模的崛起：Vision Transformer（ViT）的引入解决了 CNN 感受野受限的问题，但其二次方的计算复杂度（Quadratic Complexity）成为了高分辨率去雾的瓶颈。2023-2024 年的研究重点转向了线性复杂度 Transformer 的设计 。   

生成式先验的引入：扩散模型（Diffusion Models）以其卓越的分布建模能力，为恢复被浓雾遮挡的高频细节提供了可能。从 RIDCP 到 ProDehaze，研究者们致力于解决扩散模型的推理速度慢和“幻觉”生成问题 。   

真实世界适应性：针对合成雾与真实雾之间的域间隙（Domain Gap），无监督对比学习和半监督知识蒸馏成为了 2024 年的研究热点 。   

本报告将按照上述技术脉络，深入剖析各流派的代表性工作。

2. 基于视觉 Transformer 的去雾架构革新
Vision Transformer 利用自注意力机制（Self-Attention Mechanism）实现了像素间的全局交互，这对于推断非均匀分布的雾霾密度至关重要。然而，直接将用于高层视觉任务（如分类）的 ViT 迁移至底层视觉任务（如去雾）面临着分辨率敏感性和计算开销的双重挑战。2022-2025 年的代表性工作主要围绕架构微调和复杂度优化展开。

2.1 DehazeFormer：针对去雾任务的架构重构
文献来源：Song, Y., He, Z., Qian, H., & Du, X. (2023). Vision Transformers for Single Image Dehazing. IEEE Transactions on Image Processing (TIP), 32, 1927–1941. (Preprint arXiv:2204.03883).   

核心机制与理论创新： DehazeFormer 是将 Swin Transformer 成功适配于去雾领域的开山之作。该研究深入分析了通用 ViT 在去雾任务中的局限性，并提出了针对性的物理感知改进：

RescaleNorm 归一化策略：传统的 LayerNorm 旨在使特征分布标准化，这对于分类任务有益，但可能会破坏图像去雾所需的绝对强度信息（如雾霾浓度与像素亮度的关系）。DehazeFormer 提出了 RescaleNorm，它在归一化后重新引入了特征图的均值和方差，从而在保留统计稳定性的同时，维护了去雾所必需的空间亮度分布信息 。   

SoftReLU 激活函数：研究发现常用的 GELU 或 ReLU 会将负值截断为零，导致部分潜在的图像细节信息永久丢失。作者设计了 SoftReLU，通过平滑的非单调变换保留负区间的微弱信号，这对于从浓雾中恢复低对比度纹理至关重要 。   

空间信息聚合（Spatial Information Aggregation）：针对 Swin Transformer 窗口划分导致的信息割裂，DehazeFormer 改进了窗口间的特征交互机制，增强了对非均匀雾霾的全局感知能力 。   

实验表现： DehazeFormer 在合成数据集上的表现具有统治力。其大型变体（DehazeFormer-L）在 SOTS-Indoor 测试集上的 PSNR 首次突破了 40 dB（具体为 40.00+ dB），SSIM 达到 0.993 。相比之前的 SOTA 方法 FFA-Net（PSNR ~36.39 dB），提升幅度巨大，且在参数量减少的同时实现了性能跃升。此外，该工作发布的 RS-Haze 遥感去雾数据集，为非均匀雾霾处理提供了重要的基准 。   

2.2 MB-TaylorFormer：泰勒展开驱动的线性复杂度模型
文献来源：Qiu, Y., Zhang, K., Wang, C., et al. (2023). MB-TaylorFormer: Multi-branch Efficient Transformer Expanded by Taylor Formula for Image Dehazing. ICCV 2023. (TPAMI Version 2025: arXiv:2501.04486).   

核心机制与理论创新： 标准的 Softmax Attention 计算复杂度为 O(N 
2
 )（N 为像素数），这使得在高分辨率图像上进行全图注意力计算变得不可行。MB-TaylorFormer 提出了一种基于数学近似的优雅解决方案：

基于泰勒展开的注意力近似：该方法利用泰勒级数将 Softmax 函数展开为多项式形式。这种展开允许利用矩阵乘法的结合律，改变计算顺序，从而将计算复杂度从 O(N 
2
 ) 降低到线性复杂度 O(N) 。这一突破使得模型无需进行窗口划分（Window Partitioning），即可在全图范围内计算像素间的注意力，极大地扩展了感受野。   

多尺度注意力细化（MSAR）：泰勒展开虽然高效，但作为有限项近似会引入误差（即皮亚诺余项）。为了补偿这一精度损失，作者设计了 MSAR 模块，通过多尺度的卷积操作提取局部上下文信息，对近似后的注意力图进行校正和细化 。   

多分支架构（Multi-branch Architecture）：结合多尺度块嵌入（Multi-scale Patch Embedding），网络能够并行处理不同粒度的特征，既捕捉粗粒度的雾霾分布，又保留细粒度的物体纹理 。   

实验表现： MB-TaylorFormer 在保持极低计算开销的同时实现了卓越的性能。在 SOTS-Indoor 数据集上，其 Base 版本达到了 36.09 dB 的 PSNR，优于多数同样量级的 CNN 模型 。更重要的是，其 2025 年的 TPAMI 版本（V2）证明了该架构在去雨、去雪等多种复原任务上的通用性，且在推理速度上远超基于窗口的 Transformer（如 SwinIR）。   

2.3 LVT-UNet：轻量级混合架构的探索
文献来源：ResearchGate (2022/2023). A Single Image Dehazing using U-Net and Lightweight Vision Transformer. Conference Proceedings.   

核心机制与理论创新： 该方法代表了 CNN 与 Transformer 融合的另一条路径——混合架构。LVT-UNet 并没有完全抛弃卷积，而是将轻量级视觉 Transformer（LVT）嵌入到经典的 U-Net 结构中。

局部与全局的互补：U-Net 的编码器-解码器路径负责提取多尺度的局部特征，而 LVT 模块被置于瓶颈层或跳跃连接中，专门用于捕获全局的长距离依赖关系。

资源受限场景适配：该设计旨在解决 Transformer 在移动端难以部署的问题。通过限制 Transformer 的深度并利用 CNN 的高效归纳偏置（Inductive Bias），模型在计算资源受限的情况下仍能保持较高的去雾质量。

实验表现： 在 O-Haze（真实雾霾）数据集上，LVT-UNet 取得了 27.88 dB 的 PSNR，这一成绩是在不使用预训练 ResNet-50 骨干网络的情况下取得的 。这表明，合理的混合架构设计可以在缺乏大规模预训练数据的情况下，有效处理真实世界的复杂雾霾（如印度尼西亚的野火烟霾）。   

3. 基于扩散模型的生成式去雾：从重构到保真
扩散模型（Diffusion Models）作为生成式 AI 的核心技术，自 2023 年起彻底改变了底层视觉任务的格局。与回归模型（CNN/Transformer）倾向于输出模糊的统计平均结果不同，扩散模型通过学习数据分布的逆向去噪过程，能够生成极其逼真的高频纹理。2024-2025 年的研究重点在于解决扩散模型的两大痛点：推理效率低和内容致幻（Hallucination）。

3.1 RIDCP：码本先验与可控匹配
文献来源：Wu, R., Duan, Z., Guo, C., et al. (2023). RIDCP: Revitalizing Real Image Dehazing via High-Quality Codebook Priors. CVPR 2023.   

核心机制与理论创新： RIDCP 针对真实去雾任务中缺乏高质量参考图像的问题，提出了一种基于 VQGAN（Vector Quantized GAN）的“查表”式恢复策略：

高质量码本先验（HQ Codebook Priors）：模型首先在海量清晰图像（如 DIV2K, Flickr2K）上预训练一个 VQGAN，学习一个包含丰富清晰纹理模式的离散码本。这个码本充当了一个“纹理字典”。

特征域的最近邻匹配：在去雾过程中，模型将退化的雾图特征映射到潜在空间，并在码本中寻找最接近的“清晰特征向量”进行替换。这种机制实质上是利用存储在码本中的高质量先验来“重写”被雾霾损坏的区域，从而实现纹理的生成式修复 。   

可控匹配（Controllable Matching）：为了防止过度增强或特征误匹配，RIDCP 引入了一个可调参数 α，允许用户通过调整特征匹配的距离权重来控制去雾的强度和风格。

现象学退化管道：不同于单一的 ASM 模型，RIDCP 模拟了包括噪声、JPEG 压缩、色偏等多种真实退化，缩小了合成数据与真实数据的差距 。   

实验表现： RIDCP 在真实世界数据集（Dense-Haze）上的视觉效果极佳，能够恢复出树叶、建筑纹理等高频细节，且色彩还原度高。虽然其 PSNR 指标未必最高（因为生成内容与像素级 GT 可能不完全对齐），但在 NIQE 和 BRISQUE 等感知指标上表现优异，优于 DAD 和 PSD 等竞品 。   

3.2 DiffLI2D：冻结潜空间的语义挖掘
文献来源：Yang, Z., Yu, H., Li, B., et al. (2024). DiffLI2D: Unleashing the Potential of the Semantic Latent Space in Diffusion Models for Image Dehazing. ECCV 2024.   

核心机制与理论创新： 传统的扩散去雾方法需要重新训练庞大的去噪网络，且推理时需要数十步采样，极为耗时。DiffLI2D 提出了一种颠覆性的思路：

利用冻结的预训练模型：该方法不再重新训练扩散模型，而是直接利用在 ImageNet 上预训练好的、参数冻结的 Stable Diffusion 模型。

语义潜空间挖掘（Semantic Latent Space Exploration）：研究者发现，预训练扩散模型的潜空间（Latent Space）在不同的时间步（Time-step）包含了不同层级的信息。早期时间步包含高层语义，晚期时间步包含低层结构。DiffLI2D 通过提取这些多尺度的潜空间特征，作为强有力的语义先验输入到一个轻量级的去雾解码器中 。   

免采样推理：由于去雾过程主要由轻量级解码器完成，扩散模型仅充当特征提取器，因此该方法规避了耗时的逆向扩散采样过程，实现了单步推理。

实验表现： DiffLI2D 在 SOTS-Indoor 数据集上实现了 39.03 dB 的 PSNR ，在性能上逼近 SOTA Transformer 模型，但在训练成本上降低了数个数量级（无需训练大模型），且推理速度远超传统扩散方法（如 DehazeDiff）。   

3.3 ProDehaze：物理提示下的高保真去雾
文献来源：Zhou, T., Wang, J., Wu, S., et al. (2025). ProDehaze: Prompting Diffusion Models Toward Faithful Image Dehazing. arXiv 2025 / ICME 2025.   

核心机制与理论创新： ProDehaze 代表了 2025 年“物理感知生成”的最新趋势。它旨在解决扩散模型容易产生与原图内容不符的“幻觉”（Hallucination）问题：

结构提示恢复器（Structure-Prompted Restorer, SPR）：在潜空间中，利用 Haar 小波变换提取图像的高频结构信息，并将其作为“结构提示（Prompt）”注入到扩散模型中。这种硬性的结构约束迫使生成过程严格遵循原始图像的几何轮廓，防止结构变形 。   

雾霾感知自校正细化器（Haze-Aware Self-Correcting Refiner, HCR）：在解码阶段，引入基于暗通道先验（DCP）的雾霾密度图作为掩码。对于雾较薄的区域，模型倾向于保留原图信息；对于浓雾区域，模型依赖生成能力。这种自适应机制有效减少了颜色偏移（Color Shift）。   

实验表现： 在 I-Haze 和 O-Haze 等极具挑战性的真实数据集上，ProDehaze 的 PSNR 达到了 21.69 dB（I-Haze），SSIM 达到 0.87 。相比无约束的扩散模型，其最大的贡献在于大幅降低了 CIEDE（色差指标），证明了物理提示在提高生成保真度方面的有效性。   

4. 无监督与半监督学习：跨越真实世界的鸿沟
真实世界去雾面临的最大障碍是缺乏成对的训练数据（同一场景在同一时刻的有雾和无雾图像几乎无法获取）。2022-2025 年的方法致力于通过非成对数据（Unpaired Data）学习去雾映射。

4.1 UCL-Dehaze：无监督对比学习新范式
文献来源：Wang, Y., Yan, X., et al. (2024). UCL-Dehaze: Toward Real-World Image Dehazing via Unsupervised Contrastive Learning. IEEE Transactions on Image Processing (TIP), 33, 1361–1374..   

核心机制与理论创新： UCL-Dehaze 摒弃了传统的 CycleGAN 循环一致性架构，转而利用对比学习（Contrastive Learning）挖掘特征空间的结构信息：

非成对的正负样本构建：模型将真实世界的清晰图像集合视为“正样本”簇，将真实雾图视为“负样本”簇。注意，这里的正负样本无需内容对应。

自对比感知损失（Self-Contrastive Perceptual Loss, SCP）：该损失函数在嵌入空间（Embedding Space）中拉动生成的去雾图像向正样本簇靠近，同时推离负样本簇 。这种约束迫使网络学习到“清晰图像应有的特征分布”，而非死记硬背像素映射。   

对抗训练辅助：结合判别器，进一步校正生成图像的域分布。

实验表现： 仅使用 1,800 张非成对真实图像训练，UCL-Dehaze 在真实场景下的去雾效果在 NIQE（3.736）和 SSEQ（26.028）等无参考指标上击败了众多全监督方法（如 AOD-Net, PSD）。它证明了在没有 GT 的情况下，通过特征空间的拓扑约束也能实现高质量去雾。   

4.2 Semi-UFormer：不确定性驱动的半监督蒸馏
文献来源：Cui, Y., et al. (2024). Semi-UFormer: Semi-supervised Uncertainty-aware Transformer for Image Dehazing. IJCNN 2024..   

核心机制与理论创新： Semi-UFormer 解决的是如何利用海量未标记雾图的问题：

教师-学生框架：首先在合成数据上预训练一个教师网络，然后用它对未标记的真实雾图进行预测，生成伪标签（Pseudo-labels）以训练学生网络。

不确定性估计（Uncertainty Estimation）：由于教师网络在真实雾图上的预测可能不准确，直接学习伪标签会导致误差累积。该方法引入了一个贝叶斯不确定性模块，评估每个像素的预测置信度。学生网络被设计为“只学习教师确信的区域”（通常是薄雾或纹理清晰区），而忽略高不确定性区域 。   

实验表现： 该策略使得 Semi-UFormer 能够从真实数据中提取有效信息，显著提升了泛化能力。在 HSTS 测试集上，其 PSNR 达到 30.32 dB，SSIM 为 0.972，优于仅使用合成数据训练的基线模型 。   

4.3 USID-Net与ZID：解耦与零样本探索
USID-Net (TMM 2023)  采用解耦表示学习，将图像分解为“内容”和“雾霾”两个独立编码，通过交换编码来实现无监督去雾。其核心在于 OctEncoder，一种多频率感知编码器，能有效分离高频细节与低频雾霾。   

ZID (Zero-shot Image Dehazing)  则走到了极简主义的另一端：零样本学习。它不需要任何训练集，直接在测试时针对单张输入图像优化网络参数，利用图像内部的统计自相似性（Self-similarity）和深度先验进行去雾。虽然推理时间较长（需迭代优化），但它完全避免了域漂移问题，在水下和特殊光照场景中展现了独特的优势 。   

5. 高效与混合架构：迈向实时应用（2024-2025）
尽管 Transformer 和扩散模型效果惊人，但端侧设备（如无人机、车载摄像头）对实时性有着严苛要求。2024-2025 年的研究不仅关注性能，更关注计算效率（Efficiency）。

5.1 DEA-Net：细节增强卷积
文献来源：Chen, Z., et al. (2024). DEA-Net: Single Image Dehazing Based on Detail-Enhanced Convolution and Content-Guided Attention. TIP 2024..   

DEA-Net 的核心在于重新设计了卷积算子。它提出了 DEConv（Detail-Enhanced Convolution），在标准卷积旁增加了一个并行的“差分卷积（Difference Convolution）”分支。差分卷积通过计算相邻像素的梯度差，显式地强化了边缘和纹理信号，这正是雾霾最容易抹去的部分。配合 CGA（Content-Guided Attention），DEA-Net 以仅 3.65M 的参数量，在 SOTS-Indoor 上取得了 41.21 dB 的惊人 PSNR，在效率和性能上均超越了早期的 Transformer 模型 。   

5.2 FALCON：频域与连续密度掩码
文献来源：Kim, D., et al. (2025). FALCON: Fast Image Haze Removal Leveraging Continuous Density Mask. CVPR 2025 Workshops..   

FALCON 是 2025 年实时去雾的标杆。它引入了两个关键创新：

连续密度掩码（CDM）：利用暗通道先验计算一个连续的雾霾密度图，并将其作为一个显式的“条件通道”输入网络 。这相当于告诉网络“哪里雾浓，哪里雾淡”，大大降低了学习难度。   

频率伴随链路（FAL）：利用快速傅里叶卷积（FFC）在频域处理全局特征。频域操作具有全局感受野，且计算效率极高。

实验表现： FALCON 实现了超过 180 FPS 的推理速度，完全满足实时视频处理需求，且 PSNR/SSIM 指标依然保持在 SOTA 水平 。   

6. 综合实验分析与性能对比
6.1 定量性能对比（SOTS-Indoor 基准）
SOTS-Indoor 是目前最权威的合成去雾基准。下表汇总了 2020-2025 年各流派代表性方法的性能数据。

方法名称	发表年份	架构类型	核心机制	PSNR (dB)	SSIM	参数量 (M)	特点总结
FFA-Net	AAAI 2020	CNN	特征融合注意力	36.39	0.989	4.6	深度学习去雾早期的强基线
MB-TaylorFormer	ICCV 2023	ViT	泰勒展开线性化	36.09	0.989	2.6	计算复杂度低，适合高分辨率
Semi-UFormer	IJCNN 2024	ViT (Semi)	不确定性蒸馏	37.49	-	-	半监督方法的 SOTA
DiffLI2D	ECCV 2024	Diffusion	冻结潜空间	39.03	0.97	Frozen	无需重训，推理快，显存占用低
DehazeFormer-L	TIP 2023	ViT	RescaleNorm/SoftReLU	40.00+	0.993	20+	全局建模能力强，指标极高
DEA-Net	TIP 2024	Hybrid	细节增强卷积	41.21	0.989	3.65	性价比之王，参数少性能高
ProDehaze	ICME 2025	Diffusion	物理提示 (Prompt)	~41.78	~0.996	-	极高保真度，无幻觉，去色偏能力强
(注：数据来源于各原始论文及对比实验表 )   

6.2 实验共性与分析
物理先验的回归：无论是 FALCON 的密度掩码，还是 ProDehaze 的结构提示，2024-2025 年表现最好的模型都在显式地“借用”物理知识（如 ASM 模型、小波变换）。纯黑盒模型正在被“物理感知（Physics-Informed）”模型取代。

指标的局限性：扩散模型（如 RIDCP）的 PSNR 往往不如 DEA-Net，但在人眼视觉评分（LPIPS）上通常更优。这反映了 PSNR 偏向于平滑结果，而忽略了纹理的真实感。因此，近年来的论文越来越多地报告 LPIPS 和无参考指标（NIQE）。

效率为王：从 MB-TaylorFormer 的线性注意力到 DiffLI2D 的免采样策略，算法设计的重心已从单纯刷高 PSNR 转向降低 FLOPs 和推理延迟。

7. 2025 年技术趋势预测
基于上述分析，我们对 2025 年及未来的去雾技术发展做出以下预测：

7.1 趋势一：物理感知生成式 AI (Physics-Informed Generative AI)
未来的去雾模型将不再是纯粹的数据驱动。像 ProDehaze 和 FALCON 这样的工作表明，将大气散射模型的物理约束（如透射率图、暗通道）作为 Prompt 注入到扩散模型或大模型中，可以同时获得生成模型的强大修补能力和物理模型的稳定性。这种结合将彻底解决生成式模型的“致幻”问题。

7.2 趋势二：基础模型适配 (Foundation Model Adaptation)
随着 Segment Anything (SAM) 和 Stable Diffusion 的普及，针对去雾任务从头训练大模型将变得不再经济。DiffLI2D 展示了利用冻结预训练权重的潜力。未来将涌现更多基于 LoRA (Low-Rank Adaptation) 或 Adapter 的技术，通过微调少量参数，将通用的视觉大模型快速迁移至去雾、去雨等底层视觉任务。

7.3 趋势三：测试时自适应与零样本学习 (Test-Time Adaptation & Zero-Shot)
面对极端环境（如火星探测、深海作业），预训练数据可能完全失效。结合 UCL-Dehaze 的对比学习思路和 ZID 的零样本优化策略，未来的模型将具备在测试阶段（Test-time）利用单张输入图像的统计特性进行实时自我调整的能力，实现真正的“随处去雾”。

结论
2022 年至 2025 年是单图像去雾技术飞速发展的三年。DehazeFormer 和 MB-TaylorFormer 确立了 Transformer 在长距离依赖建模上的统治地位；RIDCP 和 ProDehaze 利用扩散模型开启了高保真纹理生成的新纪元；而 UCL-Dehaze 和 DEA-Net 则分别在无监督学习和高效卷积设计上取得了突破。这些工作共同勾勒出了下一代去雾系统的雏形：它将是一个物理感知、生成式增强且计算高效的智能系统。

参考文献
   

Song, Y., He, Z., Qian, H., & Du, X. (2023). Vision Transformers for Single Image Dehazing. IEEE Transactions on Image Processing (TIP), 32, 1927–1941. (Preprint arXiv:2204.03883).

   

Qiu, Y., Zhang, K., Wang, C., et al. (2023). MB-TaylorFormer: Multi-branch Efficient Transformer Expanded by Taylor Formula for Image Dehazing. Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV).

   

Wu, R., Duan, Z., Guo, C., et al. (2023). RIDCP: Revitalizing Real Image Dehazing via High-Quality Codebook Priors. Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR).

   

Yang, Z., Yu, H., Li, B., et al. (2024). DiffLI2D: Unleashing the Potential of the Semantic Latent Space in Diffusion Models for Image Dehazing. European Conference on Computer Vision (ECCV).

   

Zhou, T., Wang, J., Wu, S., et al. (2025). ProDehaze: Prompting Diffusion Models Toward Faithful Image Dehazing. arXiv preprint arXiv:2503.17488 (Accepted to ICME 2025).

   

Wang, Y., Yan, X., Wang, F. L., et al. (2024). UCL-Dehaze: Toward Real-World Image Dehazing via Unsupervised Contrastive Learning. IEEE Transactions on Image Processing (TIP), 33, 1361–1374.

   

Chen, Z., He, Z., & Lu, Z. M. (2024). DEA-Net: Single Image Dehazing Based on Detail-Enhanced Convolution and Content-Guided Attention. IEEE Transactions on Image Processing (TIP), 33, 1002–1015.

   

Cui, Y., et al. (2024). Semi-UFormer: Semi-supervised Uncertainty-aware Transformer for Image Dehazing. International Joint Conference on Neural Networks (IJCNN).

   

Kim, D., Kang, S., & Hwang, S. J. (2025). FALCON: Fast Image Haze Removal Leveraging Continuous Density Mask. CVPR 2025 Workshops (NTIRE).

   

ResearchGate (2022). A Single Image Dehazing using U-Net and Lightweight Vision Transformer. Conference Proceedings.

   

Li, J., Li, Y., Zhuo, L., et al. (2023). USID-Net: Unsupervised Single Image Dehazing Network via Disentangled Representations. IEEE Transactions on Multimedia.

   

Li, B., et al. (2020/2024). Zero-shot Image Dehazing. IEEE Transactions on Image Processing. (Cited in context of 2024 applications).

   

Bi, P., et al. (2025). A Simple yet Mighty Hartley Diffusion Versatilist for Generalizable Dense Prediction. International Conference on Computer Vision (ICCV 2025).


openaccess.thecvf.com
MB-TaylorFormer: Multi-Branch Efficient ... - CVF Open Access
在新窗口中打开

researchgate.net
(PDF) A Single Image Dehazing using U-Net and Lightweight Vision Transformer
在新窗口中打开

openaccess.thecvf.com
RIDCP: Revitalizing Real Image Dehazing via ... - CVF Open Access
在新窗口中打开

researchgate.net
ProDehaze: Prompting Diffusion Models Toward Faithful Image Dehazing | Request PDF
在新窗口中打开

arxiv.org
UCL-Dehaze: Towards Real-world Image Dehazing via ...
在新窗口中打开

researchgate.net
Semi-UFormer: Semi-supervised Uncertainty-aware Transformer for Image Dehazing | Request PDF - ResearchGate
在新窗口中打开

arxiv.org
[2204.03883] Vision Transformers for Single Image Dehazing - arXiv
在新窗口中打开

emergentmind.com
DehazeFormer: Vision Transformers for Image Dehazing
在新窗口中打开

scribd.com
Vision Transformers for Single Image Dehazing_10-12 | PDF | Nonlinear System - Scribd
在新窗口中打开

scispace.com
Vision Transformers for Single Image Dehazing - SciSpace
在新窗口中打开

semanticscholar.org
[PDF] Vision Transformers for Single Image Dehazing - Semantic Scholar
在新窗口中打开

arxiv.org
Depth-agnostic Single Image Dehazing - arXiv
在新窗口中打开

liner.com
[Quick Review] MB-TaylorFormer: Multi-branch Efficient Transformer Expanded by Taylor Formula for Image Dehazing - Liner
在新窗口中打开

arxiv.org
MB-TaylorFormer V2: Improved Multi-branch Linear Transformer Expanded by Taylor Formula for Image Restoration - arXiv
在新窗口中打开

arxiv.org
[2501.04486] MB-TaylorFormer V2: Improved Multi-branch Linear Transformer Expanded by Taylor Formula for Image Restoration - arXiv
在新窗口中打开

jurnal.politeknik-kebumen.ac.id
A Single Image Dehazing using U-Net and Lightweight Vision Transformer
在新窗口中打开

arxiv.org
RIDCP: Revitalizing Real Image Dehazing via High-Quality Codebook Priors - arXiv
在新窗口中打开

liner.com
[Quick Review] RIDCP: Revitalizing Real Image Dehazing via High-Quality Codebook Priors
在新窗口中打开

ecva.net
Unleashing the Potential of the Semantic Latent Space in Diffusion Models for Image Dehazing - European Computer Vision Association
在新窗口中打开

ecva.net
Unleashing the Potential of the Semantic Latent Space in Diffusion Models for Image Dehazing Appendix
在新窗口中打开

openaccess.thecvf.com
A Simple yet Mighty Hartley Diffusion Versatilist for Generalizable Dense Vision Tasks - CVF Open Access
在新窗口中打开

arxiv.org
ProDehaze: Prompting Diffusion Models Toward Faithful Image Dehazing - arXiv
在新窗口中打开

zhoutianwen.com
ProDehaze: Prompting Diffusion Models Toward Faithful Image Dehazing
在新窗口中打开

researchgate.net
UCL-Dehaze: Toward Real-World Image Dehazing via Unsupervised Contrastive Learning | Request PDF - ResearchGate
在新窗口中打开

scribd.com
UCL-Dehaze Toward Real-World Image Dehazing via Unsupervised Contrastive Learning
在新窗口中打开

ieeexplore.ieee.org
Semi-UFormer: Semi-supervised Uncertainty-aware Transformer for Image Dehazing | IEEE Conference Publication | IEEE Xplore
在新窗口中打开

computer.org
Uncertainty-Driven Weakly Supervised Dehazing Network: Integrating Dynamic Attention and Multi-Scale Feature Fusion - IEEE Computer Society
在新窗口中打开

researchgate.net
USID-Net: Unsupervised Single Image Dehazing Network via Disentangled Representations - ResearchGate
在新窗口中打开

ieeexplore.ieee.org
USID-Net: Unsupervised Single Image Dehazing Network via Disentangled Representations - IEEE Xplore
在新窗口中打开

researchgate.net
Simple Zero-Shot Image Dehazing | Request PDF - ResearchGate
在新窗口中打开

arxiv.org
Dehazing Remote Sensing and UAV Imagery: A Review of Deep Learning, Prior-based, and Hybrid Approaches - arXiv
在新窗口中打开

ieeexplore.ieee.org
An Enhanced Multi-Stage Approach for Dehazing Underwater Images - IEEE Xplore
在新窗口中打开

ieeexplore.ieee.org
DEA-Net: Single Image Dehazing Based on Detail-Enhanced Convolution and Content-Guided Attention - IEEE Xplore
在新窗口中打开

ieeexplore.ieee.org
DEA-Net: Single Image Dehazing Based on Detail-Enhanced Convolution and Content-Guided Attention - IEEE Xplore
在新窗口中打开

pmc.ncbi.nlm.nih.gov
SAM2-Dehaze: Fusing High-Quality Semantic Priors with Convolutions for Single-Image Dehazing - NIH
在新窗口中打开

openaccess.thecvf.com
FALCON: Fast Image Haze Removal Leveraging Continuous Density Mask - CVF Open Access
在新窗口中打开

researchgate.net
Fig. 2: Overall pipeline of our single image dehazing method, FALCON.... - ResearchGate
在新窗口中打开

arxiv.org
FALCON: Frequency Adjoint Link with CONtinuous Density Mask for Fast Single Image Dehazing - arXiv
在新窗口中打开

arxiv.org
Efficient Dual-domain Image Dehazing with Haze Prior Perception - arXiv
在新窗口中打开
