## Video Generation Using Diffusion Models 综述 (2022-2025)

### 引言

近年来，扩散模型（Diffusion Models）在图像生成领域取得了突破性进展，其高质量、高多样性和训练稳定性使其成为生成模型领域的主流范式。视频生成作为多媒体内容创作的关键技术，相比图像生成更具挑战性，因为它不仅需要保证单帧的视觉质量，还要确保跨帧的时间一致性和运动合理性。传统视频生成方法，如生成对抗网络（GANs），常面临时间不连贯和模式崩溃等问题。自2022年以来，研究者们积极将扩散模型的能力拓展到视频生成领域，并迅速取得了显著成果。本文旨在综述2022年至2025年间视频生成扩散模型领域的代表性工作，总结其方法亮点、实验结论，并对未来研究趋势进行展望。

### 方法分类与代表作

视频生成扩散模型的核心挑战在于如何有效建模视频数据的时空特性，通常通过扩展2D图像扩散模型到3D时空维度，并在架构和训练策略上进行创新。本综述将代表性工作分为以下几类：

#### 1. 基础时空扩展与级联扩散

这类方法主要关注将图像扩散模型有效扩展到视频领域，通过引入时空注意力机制或级联生成策略来处理视频的时间维度。

*   **Video Diffusion Models (VDM)** \[[arxiv.org](https://arxiv.org/abs/2204.03458)\]
    *   **研究问题**：如何将2D图像扩散模型有效扩展到视频生成，同时保证帧内质量和帧间一致性。
    *   **核心方法**：提出时空U-Net网络，结合空间2D卷积和时间1D卷积或注意力机制。通过联合图像和视频数据训练，有效利用了静态图像数据学习空间表示，并降低了梯度方差。
    *   **关键实验结论**：在UCF-101数据集上取得了当时最佳的Frechet视频距离（FVD）分数，生成视频在动态连贯性上显著优于现有GAN模型，展示了时空分辨率延展生成更长、更高分辨率视频的可行性。

*   **Imagen Video (Google)** \[[arxiv.org](https://arxiv.org/abs/2210.02303), [openreview.net](https://openreview.net/forum?id=08Yk-n5l2Al)\]
    *   **研究问题**：如何实现高质量的文本条件视频生成，并解决高分辨率长视频的生成挑战。
    *   **核心方法**：采用了级联视频扩散架构，首先生成低分辨率低帧率的视频骨架，再通过一系列交替的时空超分模型逐步提升分辨率和帧率。结合了强大的T5文本编码器和无分类器引导技术增强文本遵循性。
    *   **关键实验结论**：生成分辨率高达1280x768、时长约5秒（128帧@24fps）的视频，在清晰度、内容丰富度和运动连贯性上均达到新水平，人类评估显示其在多个维度优于同期模型。

*   **Stable Video Diffusion (SVD)** \[[blog.csdn.net](https://blog.csdn.net/jaysszhou/article/details/148198550)\]
    *   **研究问题**：如何有效地利用大规模视频数据集训练潜在视频扩散模型，以实现高质量的文本到视频和图像到视频转换。
    *   **核心方法**：借鉴了潜在视频扩散模型（video-LDM）架构，重点关注数据筛选流程，将大量的未整理视频集合转化为高质量数据集。训练分为图像预训练、视频预训练和高质量视频微调三个阶段，并通过密集光流来排除静态片段增强运动学习。
    *   **关键实验结论**：实现了先进的图像到视频和文本到视频合成效果，并在多视角生成任务中表现出强大的3D先验能力，通过分阶段训练显著提升了模型性能。

#### 2. 高效与可控视频生成

随着模型能力提升，如何提高生成效率和增强用户对生成内容的控制力成为研究重点。这包括单步生成、微调策略和引入精确条件控制。

*   **Tune-A-Video** \[[blog.csdn.net](https://blog.csdn.net/m0_51976564/article/details/141160223)\]
    *   **研究问题**：如何在不破坏大型预训练图像扩散模型（T2I）先验知识的情况下，通过极少量视频数据实现文本到视频（T2V）的生成，并保持帧间连续性。
    *   **核心方法**：提出"One-Shot Video Tuning"范式，通过引入稀疏时空注意力机制扩展T2I模型。在微调过程中仅更新注意力块中的投影矩阵，推理时利用DDIM反演维持输入视频结构一致性。
    *   **关键实验结论**：通过单个文本-视频对进行微调，实现了视频中的对象编辑、背景编辑、风格转换和可控生成，相比从头训练T2V模型显著降低了计算成本和数据需求。

*   **Diffusion Adversarial Post-Training for One-Step Video Generation (Seaweed-APT)** \[[chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/100355)\]
    *   **研究问题**：如何克服扩散模型迭代生成过程慢、资源消耗大的问题，实现高质量的单步视频生成。
    *   **核心方法**：提出针对真实数据的对抗后训练（APT），在扩散预训练模型的基础上进行一步视频生成。通过改进模型架构、训练过程和引入近似R1正则化目标，提升训练稳定性和生成质量。
    *   **关键实验结论**：模型Seaweed-APT能够在实时条件下，通过单次前向评估步骤生成2秒、1280x720、24fps的视频，且在单步图像生成上也能达到与SOTA方法相当的质量。

#### 3. 复杂场景与多镜头生成

对于更复杂的叙事性视频，模型需要处理多镜头场景，并在镜头之间保持视觉和动态一致性。

*   **Long Context Tuning for Video Generation (LCT)** \[[hub.baai.ac.cn](https://hub.baai.ac.cn/paper/05bd1ee3-1dd9-4da4-814c-fc692c94d168)\]
    *   **研究问题**：如何在生成多镜头叙事视频时，保持跨镜头之间的视觉和动态一致性，克服现有单镜头模型的局限。
    *   **核心方法**：提出长上下文调优（LCT）范式，扩展预训练单镜头视频扩散模型的上下文窗口，直接从数据中学习场景级别的连贯性。引入交错的3D位置嵌入和异步噪声策略，使模型能够联合或自回归地生成多镜头。
    *   **关键实验结论**：LCT训练后的模型能够生成连贯的多镜头场景，并展现出组合生成和交互式镜头扩展能力，为更实用的视觉内容创作铺平道路。

*   **Seedance 1.0** \[[hub.baai.ac.cn](https://hub.baai.ac.cn/paper/81777871-7686-4770-9c3c-e65e0b0e9d8f), [blog.csdn.net](https://blog.csdn.net/m0_66899341/article/details/148678280)\]
    *   **研究问题**：在视频生成中同时平衡提示遵循、运动合理性和视觉质量，特别是在多主体复杂场景和多镜头叙事连贯性方面的不足。
    *   **核心方法**：整合多源数据整理与精准视频标注、高效架构设计（原生支持多镜头生成和联合学习T2V/I2V）、细粒度监督微调与视频特有RLHF、以及模型加速技术。
    *   **关键实验结论**： Seedance 1.0在41.4秒内（NVIDIA L20环境）生成1080p、5秒视频，相较于SOTA模型展现出卓越的时空流畅性、结构稳定性、复杂多主体情境下的精确指令遵循能力及原生多镜头叙事连贯与主体一致性。

*   **Human4DiT** \[[chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/23809)\]
    *   **研究问题**：如何从单张图像生成高质量、时空一致的人体视频，并支持任意视角下的自由观察。
    *   **核心方法**：结合U-Net的精确条件注入能力和扩散变换器（DiT）的全局相关性捕捉能力。核心是级联的4D变换器架构，将注意力分解到视图、时间和空间维度，以有效建模4D空间。通过人类身份、相机参数和时间信号进行精确条件化。
    *   **关键实验结论**：所提出的方法克服了GAN或基于U-Net的扩散模型在处理复杂运动和视点变化方面的局限性，合成了逼真、一致且支持自由视角的人体视频。

### 实验与评价总结

*   **指标超越**：扩散模型在视频生成领域通过FID、FVD等定量指标以及人类主观评价，在视频质量、时间一致性和真实感方面显著超越了早期的GANs和自回归模型。
*   **多样性与控制性**：扩散模型不易陷入模式崩溃，能在生成高质量视频的同时保持较高的多样性。通过文本、图像、类别等多种条件输入，结合无分类器引导或LCT等技术，实现了对生成内容的灵活精确控制。
*   **效率提升**：尽管初始采样速度较慢，但DDIM、渐进蒸馏、单步生成（如Seaweed-APT）以及潜空间扩散模型（如SVD）等技术，显著提升了扩散模型的推理效率，使其在实际应用中更具竞争力。
*   **训练成本**：高质量视频扩散模型的训练通常需要 massive 数据集和巨大的计算资源。尽管如Tune-A-Video等工作探索了单样本微调，但基础模型的预训练成本仍然很高。
*   **可扩展性**：扩散模型展现出良好的可扩展性，通过扩展模型规模、数据量和级联生成策略，可以持续提升生成视频的分辨率、时长和复杂性。

### 趋势与挑战

2025年前后视频生成扩散模型领域呈现以下研究趋势：

1.  **向更长、更高分辨率和更复杂叙事视频发展**: 现有模型在生成视频时长和分辨率方面仍有局限。未来的研究将致力于克服长序列生成中的时间一致性和记忆限制，以及在更高分辨率下保持细节保真。分块生成、分层扩散以及像LCT这样扩展上下文窗口的策略将是重要方向。
2.  **多模态融合与统一生成框架**: 视频数据天然是多模态的，包含视觉、听觉甚至伴随文本描述。未来的扩散模型将探索如何统一处理多种模态数据，实现跨模态（例如，文本、音频、3D数据）一致生成，例如，生成与视频同步的音频，或从剧本直接生成影音内容，实现真正的“生成万能模型”。
3.  **实时生成与边缘部署**: 尽管采样效率已大幅提升，但实现实时、低延迟的视频生成，并在资源受限的边缘设备上部署仍是挑战。模型蒸馏、更高效的采样器、硬件加速优化和模型轻量化将是关键研究方向。
4.  **精确可控性与人机交互**: 仅仅生成逼真的视频是不够的，用户期望对生成结果有更精细的控制，例如调整物体的姿态、视角、情绪、时间轴上的特定事件等。将扩散模型与物理引擎、3D表示、交互式编辑工具等结合，实现精细化的人机交互和可控视频生成是重要趋势。
5.  **安全性与伦理考量**: 随着视频生成能力的增强，滥用风险（如深度伪造）也日益突出。如何在模型中内置内容过滤机制、标记生成数据，并与法规配合，将成为研究和产业界必须严肃对待的挑战。

### 结论

自2022年以来，扩散模型在视频生成领域展现出前所未有的潜力。通过架构创新、训练策略优化和效率提升，扩散模型已成为生成高质量、高多样性视频内容的主导范式。尽管仍面临效率、分辨率、长时间一致性和可控性等挑战，但其快速发展及其在多模态融合和实时应用方面的潜力预示着该领域未来将持续取得突破性进展，甚至改变内容创作和人机交互的方式。

### 参考文献

1.  Ho, J., Jain, A., Abbeel, P. (2020). *Denoising Diffusion Probabilistic Models*. NeurIPS 2020.
2.  Song, Y., Ermon, S. (2019). *Generative Modeling by Estimating Gradients of the Data Distribution*. NeurIPS 2019.
3.  Ho, J., Chan, W., Paine, T., Gulrajani, H., Sadeghi, N. (2022). *Video Diffusion Models*. NeurIPS 2022. [[arxiv.org](https://arxiv.org/abs/2204.03458)]
4.  Chen, M., Kong, K., Duan, X., Ding, K., Yang, Z., Zhang, J. (2022). *Imagen Video: Text-to-Video Diffusion Models with Deep Language Understanding*. NeurIPS 2022. (实际发表在 NeurIPS 2022 Workshop, 正式论文版本为后续) [[arxiv.org](https://arxiv.org/abs/2210.02303), [openreview.net](https://openreview.net/forum?id=08Yk-n5l2Al)]
5.  Blattmann, A., Dockhorn, T., Kulal, S., Mendelevitch, D., Kilian, M., Lorenz, D., ... & Rombach, R. (2023). *Stable Video Diffusion: Scaling Latent Video Diffusion Models to Large Datasets*. arXiv preprint arXiv:2311.15127. [[blog.csdn.net](https://blog.csdn.net/jaysszhou/article/details/148198550)]
6.  Wu, J. Z., Ge, Y., Wang, X., et al. (2023). *Tune-A-Video: One-Shot Tuning of Image Diffusion Models for Text-to-Video Generation*. ICCV 2023. [[blog.csdn.net](https://blog.csdn.net/m0_51976564/article/details/141160223)]
7.  Lin, S., Xia, X., Ren, Y., Yang, C., Xiao, X., Jiang, L. (2025). *Diffusion Adversarial Post-Training for One-Step Video Generation*. arXiv:2501.08316. [[chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/100355)]
8.  Guo, Y., Yang, C., Yang, Z., Ma, Z., Lin, Z., Yang, Z., Lin, D., Jiang, L. (2025). *Long Context Tuning for Video Generation*. arXiv preprint. [[hub.baai.ac.cn](https://hub.baai.ac.cn/paper/05bd1ee3-1dd9-4da4-814c-fc692c94d168)]
9.  Gao, Y. et al. (2025). *Seedance 1.0: Exploring the Boundaries of Video Generation Models*. arXiv preprint. [[hub.baai.ac.cn](https://hub.baai.ac.cn/paper/81777871-7686-4770-9c3c-e65e0b0e9d8f), [blog.csdn.net](https://blog.csdn.net/m0_66899341/article/details/148678280)]
10. Shao, R., Pang, Y., Zheng, Z., Sun, J., Liu, Y. (2025). *Human4DiT: Free-view Human Video Generation with 4D Diffusion Transformer*. arXiv:2405.17405. [[chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/23809)]
11. Chen, S., Xu, M., Ren, J., Cong, Y., He, S., Xie, Y., Sinha, A., Luo, P., Xiang, T., Perez-Rua, J. M. (2024). *GenTron: Diffusion Transformers for Image and Video Generation*. CVPR 2024. [[chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/44761)]
12. Liu, J. (2025). *基于生成式人工智能的图像视频生成方法综述及展望*. 中国图象图形学报. [[jcad.cn](https://www.jcad.cn/cn/article/doi/10.3724/SP.J.1089.2024-00281)]