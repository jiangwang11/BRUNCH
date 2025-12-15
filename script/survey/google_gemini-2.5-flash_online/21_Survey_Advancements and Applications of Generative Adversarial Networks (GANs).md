## 生成对抗网络（GANs）的进展与应用学术综述（2022-2025）

### 引言

生成对抗网络（Generative Adversarial Networks, GANs）自2014年提出以来，已成为深度学习领域最具影响力的生成模型之一。其核心思想是训练一个生成器（Generator）和一个判别器（Discriminator）进行对抗博弈，使生成器能够生成逼真的数据样本，而判别器则努力区分真实数据和生成数据。近年来，GANs在图像生成、图像到图像翻译、数据增强等领域取得了显著突破，其架构创新和应用拓展持续引起学界广泛关注。本综述旨在回顾2022-2025年间GANs领域的代表性工作，涵盖其在核心方法改进、特定任务应用等方面的最新进展，并对未来的发展趋势进行展望。

### 方法分类与代表作

GANs的最新进展主要集中在提升生成稳定性和图像质量、增强可控性以及拓宽其在多模态和3D生成等领域的应用。

#### 1. GANs稳定性与质量改进

尽管GANs在生成高质量图像方面表现出色，但其训练不稳定性及模式崩溃问题始终是研究热点。

*   **Polarity Sampling: Quality and Diversity Control of Pre-Trained Generative Networks via Singular Values**
    该研究提出了一种即插即用的Polarity采样方法，用于控制预训练深度生成网络（DGNs）的生成质量和多样性。其核心在于利用DGNs的奇异值矩阵进行操作，自适应地调整生成样本的感知质量和多样性，从而有效地改进了StyleGAN3、BigGAN-deep等模型的性能。实验结果表明，该方法显著提升了FID等指标，例如将FFHQ数据集上的StyleGAN2的FID提升至2.57 [cloud.tencent.cn](https://cloud.tencent.cn/developer/article/2011379)。
*   **Feature Statistics Mixing Regularization for Generative Adversarial Networks**
    本文研究了判别器偏差对生成性能的影响，并提出特征统计混合正则化（FSMR）方法。FSMR通过鼓励判别器对图像风格（如纹理和颜色）的预测保持不变，降低了判别器对局部风格的敏感性。该方法在判别器的特征空间中混合原始图像和参考图像的特征，并通过正则化使其预测一致，从而提升了多种GAN架构的性能 [cloud.tencent.cn](https://cloud.tencent.cn/developer/article/2011379)。
*   **Text-to-image Generation Model Based on Diffusion Wasserstein Generative Adversarial Networks (D-WGAN)**
    针对文本生成图像中GANs训练不稳定的问题，D-WGAN利用向判别器输入扩散过程中随机采样的实例噪声，实现了模型的稳定训练。该模型通过引入随机微分方法和对比学习的语言-图像预训练模型（CLIP）来简化采样并增强文本与图像的一致性。实验结果显示，D-WGAN在MSCOCO和CUB-200数据集上分别显著降低了FID分数并提升了IS分数 [jeit.ac.cn](https://jeit.ac.cn/cn/article/doi/10.11999/JEIT221400?viewType=HTML)。

#### 2. 图像到图像翻译与编辑

GANs在图像到图像翻译和图像编辑任务中展现出强大的能力，使得用户能够灵活地操作图像内容和风格。

*   **FlexIT: Towards Flexible Semantic Image Translation**
    FlexIT旨在实现灵活自然的图像编辑，它能够采用任何输入图像和用户定义的文本指令进行编辑。该方法将输入图像和文本组合映射到CLIP多模态嵌入空间，并通过自编码器的潜在空间，将输入图像迭代地变换到目标点，同时通过正则化项确保连贯性和质量。FlexIT扩展了GANs在语义图像翻译中的应用场景和灵活性 [cloud.tencent.cn](https://cloud.tencent.cn/developer/article/2011379)。
*   **High-Fidelity GAN Inversion for Image Attribute Editing**
    该研究提出了一种高保真GAN逆映射框架，能够在保留图像特定细节（如背景、外观和照明）的同时进行属性编辑。通过分析潜码低比特率的挑战，该方法引入“失真咨询方法”，使用失真图作为高保真重建的参考，并结合自监督训练方案的自适应失真对齐模块，弥合编辑图像和逆映射图像之间的差距 [cloud.tencent.cn](https://cloud.tencent.cn/developer/article/2011379)。
*   **基于生成对抗网络的人脸属性合成技术综述**
    该综述探讨了基于生成对抗网络的人脸属性合成技术进展，旨在保留人脸身份信息的前提下，根据指定目标重建并合成具有新属性的人脸。论文将基于GAN的人脸属性合成模型划分为有监督、无监督和半监督三类，并深入研究了年龄、表情、妆容等属性的合成模型，展望了未来面临的问题和发展方向 [arocmag.cn](https://www.arocmag.cn/abs/2024.05.0240)。

#### 3. 文本到图像生成与布局控制

文本到图像生成作为GANs的重要应用方向，在结合布局控制方面取得了显著进步。

*   **InstanceDiffusion: Instance-level Control for Image Generation**
    InstanceDiffusion为文本到图像的扩散模型引入了精确的实例级控制能力，允许用户为图像中的单个实例指定位置（通过点、涂鸦、边界框或分割掩码）和描述性文本。该模型提出了UniFusion模块、ScaleU模块和Multi-instance Sampler，以实现每个实例的自由形式语言条件和灵活的位置指定。实验结果表明，InstanceDiffusion在各类位置条件下显著超越了现有模型，例如在COCO数据集上，边界框输入超越了前沿模型20.4%的AP50box [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/45330)。
*   **GLIGEN: Open-Set Grounded Text-To-Image Generation**
    GLIGEN关注开放集场景下的文本到图像生成，允许用户用自然语言描述任意物体并指定其位置。它基于预训练的Stable Diffusion模型，通过添加门控的Transformer层融合区域坐标和文字等新输入。该方法在采样早期融合文本和布局信息，后期依靠原模型保证图像质量，实现了开放物体集和自由描述下的文本到图像生成 [pdf.hanspub.org](https://pdf.hanspub.org/csa2025154_451543569.pdf)。
*   **LayoutDiffusion: Controllable Diffusion Model for Layout-To-Image Generation**
    LayoutDiffusion是一个专门为布局生成设计的扩散模型，旨在实现对复杂多物体布局的高保真图像生成和精细控制。该模型采用条件DDPM框架，并设计了布局融合模块（LFM）和物体感知交叉注意力（OaCA），以增强多物体之间的关系建模，从而在生成过程中关注对应的布局对象信息。该方法在多物体布局生成上取得了巨大潜力 [pdf.hanspub.org](https://pdf.hanspub.org/csa2025154_451543569.pdf)。

#### 4. 视频生成与3D生成

GANs在扩展到视频和3D数据生成方面也取得了重要进展。

*   **StyleGAN-V: A Continuous Video Generator with the Price, Image Quality and Perks of StyleGAN2**
    StyleGAN-V是一个连续视频生成器，它考虑了视频的时间连续信号信息，扩展了神经表示范式。该模型通过位置嵌入设计连续运动表示，并通过一个整体判别器聚合时间信息，从而降低了训练成本。StyleGAN-V在StyleGAN2的基础上构建，以相同的分辨率进行训练并保持相似的图像质量，能够生成任意长度和帧率的视频 [cloud.tencent.cn](https://cloud.tencent.cn/developer/article/2011379)。
*   **Playable Environments: Video Manipulation in Space and Time**
    该研究提出了“可玩环境”的概念，一种用于在空间和时间中生成和操作交互式视频的新表示。通过推理时的单张图像，该框架允许用户在3D中移动对象，并通过提供一系列所需的动作生成视频。该方法为每一帧构建环境状态，通过动作模块进行操作，并通过体积渲染解码回图像空间 [cloud.tencent.cn](https://cloud.tencent.cn/developer/article/2011379)。
*   **Sparse to Dense Dynamic 3D Facial Expression Generation**
    该工作提出了一种基于中性3D人脸和表情标签生成动态3D面部表情的方案。它通过训练manifold-valued GAN (Motion3DGAN)来学习生成稀疏3D关键点的运动，并训练Sparse2Dense网格解码器(S2D-Dec)来了解稀疏关键点运动如何影响面部表面变形，从而实现了动态表情生成和网格重建的显著改进 [cloud.tencent.cn](https://cloud.tencent.cn/developer/article/2011379)。

### 实验与评价总结

GANs的研究成果普遍采用定量指标和定性评估相结合的方式。在图像质量方面，FID（Fréchet Inception Distance）和IS（Inception Score）是广泛使用的衡量生成图像真实性和多样性的指标，较低的FID和较高的IS通常代表更好的性能。LPIPS（Learned Perceptual Image Patch Similarity）则用于评估图像的感知相似度，可以更好地反映人眼对图像差异的感受。对于特定任务，例如图像编辑，除了生成图像的质量外，还会评估编辑的精确度、属性保留能力以及对无关属性的影响。文本到图像生成任务中，除了图像质量，文本-图像一致性（如CLIP分数）和布局遵循性也是关键评价维度。在视频生成和3D生成领域，时间连贯性、动态真实感和3D结构保真度是重要的评价指标。消融实验是常见的评估方法，用于验证模型各组件的有效性。人类评估也常被用于主观判断生成图像的真实性和满意度。

### 趋势与挑战

2025年前后，GANs领域呈现以下几个关键趋势：

1.  **多模态融合与开放世界生成：** 随着大型语言模型（LLMs）和视觉-语言模型（VLMs）的快速发展，GANs将继续深化与多模态数据的融合。未来的工作会更注重从文本、语音、2D/3D布局等多种模态中学习更丰富、更抽象的语义信息，实现更灵活、更精确的开放世界内容生成。这包括处理未知物体、复杂场景和动态交互。
2.  **可控性与可解释性：** 尽管扩散模型在图像生成质量上逐渐超越传统GAN，但GANs在潜在空间的可控性和可解释性方面仍具优势。未来的研究将致力于提升GAN模型的可控粒度，例如实现像素级、语义级乃至概念级的精细控制，并探索更有效的方法来理解和操控潜在空间。同时，对生成过程的透明度和可解释性需求将日益增加，以助于验证模型输出的可靠性。
3.  **高效训练与资源优化：** 大型GAN模型的训练通常需要庞大的计算资源和数据集。未来的发展趋势将包括开发更轻量级、更高效的GAN架构、引入自适应训练策略、并探索数据高效的学习方法（如少样本、零样本生成），从而降低GANs的部署和应用门槛，使其在资源受限的环境中也能发挥作用。
4.  **3D和动态内容生成：** 随着元宇宙、虚拟现实等领域的兴起，GANs在3D物体、场景、动画和视频生成方面的应用将持续拓展。这涉及到如何有效地建模3D几何、纹理、材质以及时序动态，同时保持生成内容的真实感和物理一致性。结合神经辐射场（NeRF）等新兴3D表示方法将是重要的研究方向。

### 结论

自提出以来，生成对抗网络（GANs）在图像生成和各种计算机视觉任务中取得了突破性进展。2022-2025年的研究展示了GANs在提高训练稳定性、改善生成质量、增强可控性以及拓宽多模态和3D应用方面的持续努力。虽然扩散模型在某些生成质量指标上逐渐领先，但GANs凭借其独特的对抗学习机制在生成效率、潜在空间可解释性和特定任务（如图像编辑、人脸属性合成）的精准控制方面仍具有不可替代的优势。未来的研究将继续探索GANs与其他生成范式的结合，以应对开放世界、多模态、3D内容生成等更复杂的挑战，并推动生成式AI技术在实际应用中的广泛落地。

### 参考文献

*   [cloud.tencent.cn](https://cloud.tencent.cn/developer/article/2011379) CVPR 2022 | 最全25+主题方向、最新50篇GAN论文汇总.
*   [jeit.ac.cn](https://jeit.ac.cn/cn/article/doi/10.11999/JEIT221400?viewType=HTML) 赵宏, 李文改. 基于扩散生成对抗网络的文本生成图像模型研究. 电子与信息学报, 2023, 45(12): 4371-4381. doi: 10.11999/JEIT221400.
*   [arocmag.cn](https://www.arocmag.cn/abs/2024.05.0240) 王健强, 张珂, 李培杰. 基于生成对抗网络的人脸属性合成技术综述. 计算机应用研究, 2025, 42(3): 650-662. doi: 10.19734/j.issn.1001-3695.2024.05.0240.
*   [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/45330) Wang, X., Darrell, T., Rambhatla, S. S., Girdhar, R., & Misra, I. InstanceDiffusion: Instance-level Control for Image Generation. CVPR 2024.
*   [pdf.hanspub.org](https://pdf.hanspub.org/csa2025154_451543569.pdf) 齐时达. 基于布局控制的文本到图像扩散模型研究进展. 计算机科学与应用, 2025, 15(4): 443-452. doi: 10.12677/csa.2025.154116.
*   [eet-china.com](https://www.eet-china.com/mp/a249484.html) TPAMI2023生成式AI与图像合成综述. 2023-09-06.
*   [jcst.ict.ac.cn](https://jcst.ict.ac.cn/cn/article/cstr/32374.14.s11390-024-3814-0) 江锐, 郑光聪, 李藤, 杨天瑞, 王井东, 李玺. 多模态可控扩散模型综述. 2024-06-28.
*   [arxiv.org/pdf/2511.13387](https://arxiv.org/pdf/2511.13387) 孔飞. 广义去噪扩散编码模型（gDDCM）：使用预训练的扩散模型对图像进行分词. 2025-11-18.
*   [cjeo-journal.org](https://cjeo-journal.org/wp-content/uploads/2025/11/%E7%94%9F%E6%88%90%E5%BC%8F%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD%E5%9C%A8%E9%9D%92%E5%85%89%E7%9C%BC%E9%A2%86%E5%9F%9F%E7%9A%84%E7%A0%94%E7%A9%B6%E8%BF%9B%E5%B1%95.pdf) 龚迪, 王宇宁, 许言午, 杨卫华, 汪建涛. 生成式人工智能在青光眼领域的研究进展. 中华实验眼科杂志, 2025(11).
*   [jeit.ac.cn/cn/article/doi/10.11999/JEIT221400](https://jeit.ac.cn/cn/article/doi/10.11999/JEIT221400) ZHAO Hong, LI Wengai. Text-to-image Generation Model Based on Diffusion Wasserstein Generative Adversarial Networks. _Journal of Electronics & Information Technology_, 2023, 45(12): 4371-4381.
*   [cloud.tencent.cn](https://cloud.tencent.cn/developer/article/2011379) Ho J, Jain A, Abbeel P. Denoising diffusion probabilistic models. Advances in neural information processing systems, 2020, 33: 6840-6851.
*   [blog.csdn.net/yangqoor/article/details/148351268](https://blog.csdn.net/yangqoor/article/details/148351268) Physics-Based Generative Adversarial Models for Image Restoration and Beyond论文阅读. 2025-06-09.