好的，遵照您的指示。作为一名严谨的科研助手，我将基于提供的真实联网搜索结果，生成一篇关于“单图像去雾技术与深度学习结合的增强方法”的学术综述。

***

### **单图像去雾技术与深度学习结合的增强方法研究综述 (2022-2025)**

#### **引言**

雾霾天气下，大气中的悬浮粒子对光的吸收和散射导致图像质量严重下降，表现为对比度降低、颜色失真及细节模糊。这不仅影响人类的视觉感知，也对自动驾驶、视频监控、目标检测等高级计算机视觉任务的可靠性构成严峻挑战。单图像去雾旨在从单张退化图像中恢复出清晰的场景信息，是一个重要的计算机视觉底层任务。

早期研究主要依赖于物理模型和手工设计的先验知识，如暗通道先验（Dark Channel Prior, DCP）[jeit.ac.cn](https://jeit.ac.cn/cn/article/doi/10.11999/JEIT210868?viewType=HTML)，但这些方法在先验失效的场景（如大面积天空区域）中表现不佳。近年来，随着深度学习的飞速发展，基于数据驱动的去雾方法成为主流。本综述聚焦于 2022 至 2025 年间，深度学习在单图像去雾领域的增强方法，通过梳理代表性工作，总结其核心思想、实验表现，并展望未来的研究趋势与挑战。

#### **方法分类与代表作**

近期的研究工作主要通过改进网络结构、融合物理先验、引入新的学习范式等方式，旨在解决去雾过程中的细节丢失、颜色失真和对真实雾天场景泛化能力不足等问题。

**1. 混合模型与物理先验融合**

该类方法并未完全摒弃传统物理模型，而是将其作为先验知识融入深度神经网络的设计中，以增强模型的物理可解释性和在特定场景下的鲁棒性。

*   **融合暗通道先验损失的生成对抗网络** [oejournal.org](https://www.oejournal.org/oee/article/doi/10.12086/oee.2022.210448?viewType=HTML)
    *   **研究问题**: 基于生成对抗网络（GAN）的去雾模型在合成数据集上训练时，容易对样本真值过度拟合，导致在真实雾图上表现不佳。
    *   **核心方法**: 提出了一种将暗通道先验（DCP）作为损失函数一部分的GAN。通过引入一个基于像素值压缩的可微暗通道提取策略，该先验损失可以纠正生成图像的暗通道稀疏性，从而在训练中引导网络生成更符合物理规律的去雾结果。
    *   **关键实验结论**: 该方法在合成测试集（如SOTS）和真实图像上均有良好表现，有效阻止了模型对样本的过度拟合，提升了去雾效果和泛化能力。

*   **基于天空区域分割的海雾图像去雾算法** [opticsjournal.net](https://www.opticsjournal.net/Articles/OJc38270e9e69cda90/Abstract)
    *   **研究问题**: 经典的暗通道先验算法在处理包含大面积天空或水域的海雾图像时，会因先验失效而错误估计大气光，导致处理后图像亮度偏低、颜色失真。
    *   **核心方法**: 该算法首先通过阈值分割和区域生长精确地分割出天空区域。然后，仅在非天空区域应用暗通道先验估计透射率，而在天空区域内则采用更鲁棒的策略（如取亮度最高像素的中值）来优化全局大气光值的计算。
    *   **关键实验结论**: 实验证明，通过对特定场景（海雾）进行针对性预处理，该方法显著提升了结构相似性（SSIM）和峰值信噪比（PSNR）指标，有效解决了DCP在海天一色场景中的失效问题。

**2. 多尺度结构与细节恢复网络**

为了解决去雾过程中高频细节易丢失的问题，研究者设计了复杂的多尺度网络和独立的细节增强模块，旨在更精细地捕捉和重建图像的纹理信息。

*   **双分支卷积结合细节增强的图像去雾网络 (DBDENet)** [jnwpu.org](https://www.jnwpu.org/articles/jnwpu/pdf/2025/01/jnwpu2025431p109.pdf)
    *   **研究问题**: 现有深度学习去雾算法在特征提取过程中能力不足，导致去雾图像出现细节丢失、颜色失真和对比度下降。
    *   **核心方法**: 设计了一个双模块网络。图像去雾模块采用改进的U-Net结构，其核心是一个双分支卷积块（DBConv），该卷积块并行使用深度可分离卷积和差分卷积，以提取更丰富的梯度与纹理特征。初步去雾结果随后被送入一个独立的细节增强模块，进一步恢复高频信息。
    *   **关键实验结论**: 在ITS和Haze4K数据集上，DBDENet的PSNR和SSIM分别达到了39.69dB和0.994，优于多个对比模型，且主观视觉分析表明其在细节和颜色保真度上更接近真实无雾图像。

*   **基于多尺度特征结合细节恢复的去雾方法** [jeit.ac.cn](https://jeit.ac.cn/cn/article/doi/10.11999/JEIT210868?viewType=HTML)
    *   **研究问题**: 如何提高单幅图像去雾的准确性，并增强去雾结果的细节可见性。
    *   **核心方法**: 提出一个两阶段方法。第一阶段，构建一个包含多尺度特征提取模块（MSFEM）和多尺度特征融合模块（MSFFM）的端到端去雾网络，获得初步去雾结果。第二阶段，构造一个基于图像分块的细节恢复网络，并将其提取的细节信息与初步结果融合，得到最终的清晰图像。
    *   **关键实验结论**: 在SOTS室外测试集上，该方法的PSNR达到33.78，SSIM达到0.985，均超过了FFA-Net等代表性方法。消融实验证实，细节恢复网络能显著提升最终图像的质量。

**3. Transformer与全局特征建模**

针对卷积神经网络（CNN）在捕获长距离依赖关系上的局限性，研究者开始引入Transformer架构，以更好地建模图像的全局上下文信息。

*   **全局和局部特征融合的图像去雾网络** [opticsjournal.net](https://www.opticsjournal.net/Articles/OJd7d691bf06f516bc/FullText)
    *   **研究问题**: 纯粹基于卷积的操作关注局部特征，难以对超出感受野的全局信息进行建模，限制了特征表达能力。
    *   **核心方法**: 构建了一个混合架构的生成器。该网络的核心是一个全局和局部特征融合模块（GLFFM），其中Transformer分支用于提取全局依赖关系，而CNN分支负责提取局部感知特征，二者融合后输出。此外，还设计了一个能够根据图像内容自适应生成位置编码的全局位置编码生成器。
    *   **关键实验结论**: 该网络在合成数据集（RESIDE）和真实数据集（O-HAZE等）上均取得了当时的最佳性能，PSNR在SOTS上达到33.19 dB，证明了融合Transformer与CNN的有效性。

**4. 注意力机制的深度应用**

注意力机制允许网络自适应地关注图像中的重要区域和特征通道，从而实现更高效和精准的特征处理，已成为现代去雾网络不可或缺的组成部分。

*   **基于注意力机制和马尔可夫判别器的图像去雾** [opticsjournal.net](https://www.opticsjournal.net/Articles/OJ9f14673903ddeb43/FullText)
    *   **研究问题**: 传统网络对图像不同区域的特征（如雾浓度不均）进行无差别处理，效率低下且精度有限。
    *   **核心方法**: 在网络中引入通道和空间注意力机制，使模型能为不同区域的特征自适应分配权重，更专注于与雾度相关的特征。同时，采用带有Inception机制的模块来预测全局大气光，并使用马尔可夫判别器（PatchGAN）来提升生成图像的局部真实感。
    *   **关键实验结论**: 在SOTS和HSTS测试集上，该算法的SSIM和PSNR值均优于DCP、CAP等基线方法，且去雾后图像的亮度和饱和度得到改善。

*   **融合注意力机制的卷积网络单像素成像** [wulixb.iphy.ac.cn](https://wulixb.iphy.ac.cn/cn/article/doi/10.7498/aps.74.20250010?viewType=HTML)
    *   **研究问题**: （交叉领域参考）如何在其他图像重建任务（如单像素成像）中有效利用特征。
    *   **核心方法**: 将通道与空间注意力机制（CBAM）集成到U-Net结构的每一层。这种设计旨在充分利用注意力机制提供的关键权重信息，并结合U-Net在多尺度下强大的特征提取能力。
    *   **关键实验结论**: 尽管应用于不同领域，但实验表明，深度融合的注意力机制能够有效捕捉细节并抑制噪声，其在PSNR和SSIM上的显著优势验证了该模块设计的普遍有效性。

**5. 半监督与数据增强策略**

由于获取成对的真实世界有雾/无雾图像成本高昂，导致训练数据稀缺。半监督学习和创新的数据增强方法旨在弥合合成数据与真实数据之间的领域鸿沟（domain gap）。

*   **基于深度学习的半监督图像去雾网络** [hanspub.org](https://www.hanspub.org/journal/paperinformation?paperid=84945)
    *   **研究问题**: 真实雾图数据集稀缺，导致在合成数据上训练的模型在真实世界中泛化能力差。真实雾霾通常分布不均匀，而合成雾霾则较为均匀。
    *   **核心方法**: 提出一个名为SSDN的半监督框架。该框架包含一个基于局部数据增强的模型（EDEM），它通过对清晰图像进行随机掩码，并从真实雾图中迁移雾度特征，来生成更逼真的非均匀雾图。网络通过监督分支（使用合成数据）和无监督分支（使用真实雾图和增强雾图）联合训练。
    *   **关键实验结论**: 在SOTS室内测试集上，PSNR和SSIM分别达到26.15和0.949。更重要的是，在真实雾图数据集（RTTS）上的定性分析表明，该方法的去雾结果比仅在合成数据上训练的FFA-Net等方法更具真实感，泛化能力更强。

#### **实验与评价总结**

综合上述研究，可以总结出以下共性结论：

1.  **评价基准**: 各项研究普遍采用公开的合成数据集（如RESIDE中的ITS和SOTS，Haze4K）和真实数据集（如I-HAZE, O-HAZE, RTTS）进行评估。客观评价指标主要为峰值信噪比（PSNR）和结构相似性（SSIM）。
2.  **性能对比**: 基于深度学习的方法在PSNR和SSIM指标上全面超越了以DCP为代表的传统先验方法。2022-2025年间，新提出的网络架构（如Transformer混合模型、细节增强网络）相比于早期的CNN模型（如DehazeNet）在各项指标上实现了稳步提升。
3.  **视觉质量**: 主观视觉分析是评价去雾效果的关键。先进的方法更注重解决特定视觉缺陷，如天空区域的颜色失真 [opticsjournal.net](https://www.opticsjournal.net/Articles/OJc38270e9e69cda90/Abstract)、高频纹理的丢失 [jnwpu.org](https://www.jnwpu.org/articles/jnwpu/pdf/2025/01/jnwpu2025431p109.pdf) 和生成图像的伪影 [opticsjournal.net](https://www.opticsjournal.net/Articles/OJd7d691bf06f516bc/FullText)。
4.  **泛化能力**: 如何将模型从合成数据域泛化到真实数据域是核心挑战。半监督学习 [hanspub.org](https://image.hanspub.org/Html/19-1543189_84945.htm) 和结合物理先验的方法 [oejournal.org](https://www.oejournal.org/oee/article/doi/10.12086/oee.2022.210448?viewType=HTML) 在提升真实图像处理效果上显示出明显优势，即使它们在合成数据集上的指标不一定是最高的。

#### **趋势与挑战**

基于2022-2025年的研究进展，预计单图像去雾领域在未来将呈现以下研究趋势和挑战：

1.  **拥抱大规模预训练模型**: 当前研究大多从零开始训练或使用在ImageNet上预训练的模型。未来趋势将是利用更大规模的视觉基础模型（Foundation Models），特别是文本到图像的扩散模型（如Stable Diffusion）。研究将不再是设计全新的网络，而是探索如何通过参数高效的微调技术（如LoRA） [fitee.zjujournals.com](https://www.fitee.zjujournals.com/zh/article/doi/10.1631/FITEE.2400395/)，将这些强大生成先验知识适配到去雾任务中，从而在少量数据上实现高质量的图像恢复。

2.  **多模态信息的融合与引导**: 单一的图像输入信息有限。随着大型多模态模型（如GPT-4V）的成熟，未来的去雾方法可能会引入文本、深度图等多模态信息进行引导。例如，可以利用VLM从有雾图像中自动生成描述性文本提示（“有薄雾的城市街道，远处建筑轮廓模糊”），并利用这些提示指导扩散模型进行更可控、更具语义的去雾，而非简单地像素级恢复 [fitee.zjujournals.com](https://www.fitee.zjujournals.com/zh/article/doi/10.1631/FITEE.2400395/)。

3.  **面向真实世界和特定应用的无监督/自监督学习**: 真实世界中雾的形态（如均匀雾、非均匀雾、海雾）复杂多变，合成数据难以完全模拟。未来的研究将更加侧重于无监督和自监督学习范式，以完全摆脱对成对数据的依赖。这可能包括利用物理先验（如暗通道稀疏性 [oejournal.org](https://www.oejournal.org/oee/article/doi/10.12086/oee.2022.210448?viewType=HTML)）作为无监督损失，或设计更巧妙的自监督任务（如模拟非均匀雾 [hanspub.org](https://www.hanspub.org/journal/paperinformation?paperid=84945)）来从单一真实雾图中学习去雾映射。

#### **结论**

在2022至2025年期间，结合深度学习的单图像去雾技术取得了显著进展。研究工作从单纯的CNN架构演进到融合物理先验、引入注意力机制、结合Transformer全局建模以及采用半监督学习等多种增强策略，显著提升了去雾图像的客观指标和主观视觉质量。尽管现有方法在细节恢复和颜色保真度方面已有大幅改善，但对复杂真实雾景的泛化能力仍是核心挑战。未来的研究将可能朝着利用大规模预训练模型、融合多模态信息以及深化无监督学习范式的方向发展，以期实现更鲁棒、高效和高质量的图像去雾。

#### **参考文献**

1.  翟凤文, 朱玉彤, 金静. (2025). 双分支卷积结合细节增强的图像去雾. 西北工业大学学报. [jnwpu.org](https://www.jnwpu.org/articles/jnwpu/pdf/2025/01/jnwpu2025431p109.pdf)
2.  姜鑫, 聂海涛, 朱明. (2023). 全局和局部特征融合的图像去雾. 光学 精密工程. [opticsjournal.net](https://www.opticsjournal.net/Articles/OJd7d691bf06f516bc/FullText)
3.  徐航, 周杰, 赵丽, 胡杰. (2024). 基于深度学习的半监督图像去雾网络. 计算机科学与应用. [hanspub.org](https://www.hanspub.org/journal/paperinformation?paperid=84945)
4.  张世辉, 路佳琪, 宋丹丹, 张晓微. (2022). 基于多尺度特征结合细节恢复的单幅图像去雾方法. 电子与信息学报. [jeit.ac.cn](https://jeit.ac.cn/cn/article/doi/10.11999/JEIT210868?viewType=HTML)
5.  程德强, 尤杨杨, 寇旗旗, 徐进洋. (2022). 融合暗通道先验损失的生成对抗网络用于单幅图像去雾. 光电工程. [oejournal.org](https://www.oejournal.org/oee/article/doi/10.12086/oee.2022.210448?viewType=HTML)
6.  林克正, 耿佳浩, 程卫月, 李骜. (2022). 基于注意力机制和马尔可夫判别器的图像去雾算法. 激光与光电子学进展. [opticsjournal.net](https://www.opticsjournal.net/Articles/OJ9f14673903ddeb43/FullText)
7.  王玥, 张海峰, 岳凤英, 宋晓东. (2025). 基于天空区域分割的海雾图像去雾算法. 激光与光电子学进展. [opticsjournal.net](https://www.opticsjournal.net/Articles/OJc38270e9e69cda90/Abstract)
8.  王翔, 周义深, 张轩阁, 陈希浩. (2025). 融合注意力机制的卷积网络单像素成像. 物理学报. [wulixb.iphy.ac.cn](https://wulixb.iphy.ac.cn/cn/article/doi/10.7498/aps.74.20250010?viewType=HTML)
9.  He, K., Sun, J., & Tang, X. (2010). Single image haze removal using dark channel prior. IEEE Transactions on Pattern Analysis and Machine Intelligence.
10. Cai, B., Xu, X., Jia, K., et al. (2016). DehazeNet: An end-to-end system for single image haze removal. IEEE Transactions on Image Processing.
11. Li, B., Peng, X., Wang, Z., et al. (2017). AOD-Net: All-in-one dehazing network. In Proceedings of the IEEE International Conference on Computer Vision.
12. Qin, X., Wang, Z., Bai, Y., et al. (2020). FFA-Net: Feature fusion attention network for single image dehazing. In Proceedings of the AAAI Conference on Artificial Intelligence.
13. YANG, S., GU, Z., HAO, W., et al. (2025). Few-shot exemplar-driven inpainting with parameter-efficient diffusion fine-tuning. Frontiers of Information Technology & Electronic Engineering. [fitee.zjujournals.com](https://www.fitee.zjujournals.com/zh/article/doi/10.1631/FITEE.2400395/)