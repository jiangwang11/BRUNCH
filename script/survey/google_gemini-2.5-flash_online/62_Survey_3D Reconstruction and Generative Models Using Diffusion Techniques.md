## 3D 重建与生成模型中的扩散技术：2022-2025 年代表性工作综述

### 引言

三维重建与三维内容生成是计算机视觉和图形学领域的核心问题，在虚拟现实、增强现实、机器人学和数字内容创作等领域具有广泛应用前景。传统的基于几何或图像的三维重建方法往往面临数据稀疏、真实感不足以及生成多样性受限等挑战。近年来，扩散模型（Diffusion Models, DMs）凭借其强大的生成能力、出色的图像质量和高多样性，在二维图像生成领域取得了显著成功，并逐步扩展到三维视觉任务。扩散模型在三维领域的应用，尤其是在三维重建与三维生成方面，展现出解决传统方法痛点、提升生成质量和效率的巨大潜力。

本综述旨在系统性地回顾 2022 年至 2025 年间，扩散模型在三维重建与生成领域中的代表性工作，重点阐述其研究问题、核心方法和实验结论。我们将对当前主流方法进行分类，总结其共性优势与局限性，并对该领域的未来发展趋势进行展望。

### 方法分类与代表作

扩散模型在三维重建与生成中的应用可大致分为以下几类：基于 2D 扩散模型的 3D 提升、多视图扩散模型应用于 3D 重建、潜在空间扩散模型、3D 原生扩散模型以及扩散模型应用于特定 3D 任务。

#### 1. 基于 2D 扩散模型的 3D 提升 (2D Diffusion Priors for 3D Lifting)

这类方法利用在海量 2D 图像上预训练的大规模扩散模型作为强大的 2D 图像先验，通过蒸馏或优化技术将 2D 信息提升至 3D 空间。

*   **Sherpa3D: Boosting High-Fidelity Text-to-3D Generation via Coarse 3D Prior** [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/46408)
    该论文旨在解决文本到三维生成中高保真度与几何一致性之间的矛盾。核心思路是利用易于获取的粗糙三维知识作为先验，通过结构指导和语义指导两种策略来增强提示，并引导二维提升优化实现细化。实验结果表明，Sherpa3D 在质量和三维一致性方面优于现有最先进的文本到三维方法。
*   **Enhancing Single Image to 3D Generation using Gaussian Splatting and Hybrid Diffusion Priors** [themoonlight.io](https://www.themoonlight.io/zh/review/enhancing-single-image-to-3d-generation-using-gaussian-splatting-and-hybrid-diffusion-priors)
    该研究旨在提高单幅图像到三维生成对象的几何一致性和视觉质量，以满足机器人操作等应用需求。核心方法是结合高斯散点（Gaussian Splatting）和混合扩散先验，通过前景提取、多视角图像生成、粗略三维高斯表示初始化，以及两阶段的混合频率得分蒸馏损失优化。该方法在 2D 纹理和 3D 几何度量方面超越了现有技术。
*   **Instant 3D Human Avatar Generation using Image Diffusion Models** [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/97996)
    该论文提出一种快速、高质量的三维人体形象生成方法，可从图像和文本提示等不同模态输入生成，并能控制姿态和形状。研究将生成与三维建模解耦，利用基于扩散的图像生成网络在不同任务下进行微调，并通过一个三维提升网络实现三维建模。该方法在生成速度上实现了数量级的提升，且能生成具有多样化外观和多模态控制的准确三维形象。

#### 2. 多视图扩散模型应用于 3D 重建 (Multi-View Diffusion Models for 3D Reconstruction)

这些方法直接建模多视图图像的一致性，生成高质量的多视角图像或 3D 表示，从而实现更鲁棒的 3D 重建。

*   **CAT3D: Create Anything in 3D with Multi-View Diffusion Models** [blog.csdn.net](https://blog.csdn.net/m0_60177079/article/details/144796428)
    该论文提出 CAT3D 方法，旨在实现单视图、稀疏视图或文本提示生成三维场景。核心方法是利用多视图扩散模型生成大量一致的新视图，并将其作为三维重建的输入，通过有效的并行采样策略生成三维一致渲染的 3D 表示。CAT3D 能在短时间内生成场景和对象级的逼真结果，并在多个基准上速度优于现有最先进方法。
*   **Difix3D+: Improving 3D Reconstructions with Single-Step Diffusion Models** [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/5d599177-dda4-48f2-91a7-b5de0449e570)
    该工作致力于解决三维重建中新视角渲染由于欠约束区域导致的伪影问题。Difix3D+ 引入一种全新的管道设计，核心是 Difix，一个单步图像扩散模型，用于增强和去除新视角渲染中的伪影，并在重建阶段清理伪训练视图，在推理阶段作为神经增强器。该方法是一个通用解决方案，兼容 NeRF 和 3DGS，实现了平均 2 倍的 FID 评分提升。

#### 3. 潜在空间扩散模型 (Latent Space Diffusion Models)

为了应对 3D 数据的高维性和复杂性，这类方法将扩散过程应用于降维后的潜在空间，提高效率和可扩展性。

*   **LION: Latent Point Diffusion Models for 3D Shape Generation** [zhuanzhi.ai](https://www.zhuanzhi.ai/paper/731cfc5d4536d93cf9f94aea445edfc5)
    该研究旨在提升 3D 点云合成的生成质量、操作灵活性和输出平滑表面或网格的能力。LION 引入了分层潜在点扩散模型，通过变分自编码器（VAE）与分层潜在空间结合，包含全局形状潜在表示和点结构潜在空间。实验证明 LION 在 ShapeNet 基准上实现了最先进的生成性能，并能方便应用于多模态形状去噪、体素条件合成等任务。

#### 4. 3D 原生扩散模型 (Native 3D Diffusion Models)

这些方法直接在 3D 数据表示（如体素、点云或隐式函数）上操作，避免了 2D 到 3D 的提升过程可能带来的信息损失和不一致性。

*   **DiT-3D: Exploring Plain Diffusion Transformers for 3D Shape Generation** [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/10882)
    该论文旨在探索 Transformer 架构在 3D 形状生成中的表现，以克服现有 3D 扩散方法主要采用 U-Net 架构的局限性。DiT-3D 提出一种新型扩散 Transformer，直接对体素化点云执行去噪过程，结合 3D 位置和补丁嵌入，并引入 3D 窗口注意力。实验结果表明，DiT-3D 在高保真和多样化的 3D 点云生成方面实现了最先进的性能，且模型更具可扩展性。

#### 5. 扩散模型应用于特定 3D 任务 (Diffusion Models for Specific 3D Tasks)

这类方法将扩散模型应用于更具体的 3D 领域问题，如视频生成中的 3D 一致性，或工程设计中的特定外形生成。

*   **3D空间先验驱动的相机轨迹可控视频扩散生成模型** [aas.net.cn](https://aas.net.cn/cn/article/doi/10.16383/j.aas.c250124?viewType=HTML)
    该文旨在解决视频扩散模型在相机可控的图像到视频生成任务中，生成视频普遍存在的空间结构模糊化、多视角下物体形态畸变等 3D 空间结构一致性问题。核心方法是在训练和推理阶段都引入额外的 3D 空间先验信息，通过设计基于视角形变映射的条件嵌入（Warp-Injection），以及在推理阶段的初始噪声空间几何校正（Warp-Init）和能量函数引导策略（Warp-Guidance）实现。实验结果表明，该方法显著优化了 FVD 指标，并降低了 3D 结构估计的失败率，有效维持了生成视频的 3D 空间结构一致性。
*   **基于生成式模型的三维飞行器外形泛化表征方法** [hkxb.buaa.edu.cn](https://hkxb.buaa.edu.cn/CN/10.7527/S1000-6893.2025.31511)
    该研究旨在提升飞行器气动外形参数化方法的灵活性和有效性，解决传统方法的外形约束过强和设计变量冗余问题。核心方法是提出一种基于生成式模型的三维飞行器气动外形泛化表征方法，通过提取剖面图像几何特征，约束全局外形与局部点云扩散模型，实现三维外形点云快速生成。该方法能在短时间内生成单个外形剖面图像和三维气动外形网格文件，重构外形与初始外形平均几何误差控制在 1 mm 以内。

### 实验与评价总结

针对上述各类方法，共性实验结论主要集中在以下几个方面：

1.  **生成质量与真实感大幅提升：** 扩散模型展现出生成高度逼真、细节丰富的 3D 内容的能力，尤其在结合 2D 扩散先验时，能够捕捉复杂纹理和几何细节。例如，[difix3d.com](https://hub.baai.ac.cn/paper/5d599177-dda4-48f2-91a7-b5de0449e570) 提出的 Difix3D+ 平均 FID 评分提升 2 倍；[themoonlight.io](https://www.themoonlight.io/zh/review/enhancing-single-image-to-3d-generation-using-gaussian-splatting-and-hybrid-diffusion-priors) 的工作在 2D 纹理和 3D 几何度量方面超越现有技术。
2.  **几何一致性与多视角一致性：** 解决多视角（novel view synthesis）生成中的一致性问题是关键挑战，多视图扩散模型或引入 3D 空间先验的方法显著改善了这一问题。例如，[blog.csdn.net](https://blog.csdn.net/m0_60177079/article/details/144796428) 的 CAT3D 能够生成大量一致的新视图，并通过 3D self-attention 保证跨视图一致性；[aas.net.cn](https://aas.net.cn/cn/article/doi/10.16383/j.aas.c250124?viewType=HTML) 的工作通过 3D 空间先验降低了视频生成中的 3D 结构估计失败率。
3.  **生成效率与可扩展性：** 尽管扩散模型计算成本较高，但通过潜在空间操作、单步扩散或优化的网络架构，生成速度和对高维 3D 数据的处理能力有所提升。例如，[chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/97996) 的工作实现了三维人体形象生成的秒级速度；[chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/10882) 的 DiT-3D 采用 Transformer 架构，模型更具可扩展性。
4.  **对多样化 3D 任务的适应性：** 扩散模型在 3D 物体生成、形状补全、点云重建到场景理解等多样任务中展现出通用性。许多方法不仅能生成新内容，还能进行编辑、补全或通过条件控制生成特定内容。
5.  **数据稀疏性问题缓解：** 相比传统方法对大量 3D 数据的依赖，利用 2D 扩散先验的方法有效弥补了 3D 数据集稀缺的不足。

### 趋势与挑战

2025 年前后，3D 重建与生成领域中的扩散技术呈现以下趋势：

1.  **更高效的 3D 生成与重建：** 随着对实时性、用户交互和大规模应用的需求增加，未来研究将持续关注如何降低扩散模型的计算复杂性，提高 3D 生成和重建的速度。这可能涉及开发更轻量级的扩散模型架构、更先进的采样策略（如单步采样或少量步骤采样），以及更高效的 3D 数据表示方法。
2.  **多模态与跨领域融合：** 扩散模型强大的多模态处理能力将进一步与 3D 任务深度融合。研究将探索如何更好地利用文本、图像、音频甚至物理仿真数据作为条件，生成更具语义性、功能性和交互性的 3D 内容。例如，实现更精确的文本到 3D 场景生成，或结合物理引擎进行可交互的 3D 建模。
3.  **强调 3D 几何与物理一致性：** 尽管扩散模型在真实感方面表现出色，但其生成的 3D 内容在几何结构和物理特性上仍有提升空间。未来的工作将更侧重于如何将严格的 3D 几何约束、物理规律或渲染知识融入扩散模型，以确保生成对象在不同视角下都具有完美的几何一致性、无伪影，并能用于下游的工程分析或仿真。

### 结论

扩散模型在 2022-2025 年间已成为 3D 重建与内容生成领域的重要驱动力。从利用 2D 扩散模型提升 3D 内容，到直接在 3D 空间或其潜在空间进行扩散，再到解决特定 3D 任务，扩散技术展现出重塑该领域巨大潜力。当前研究已在生成质量、真实感、几何一致性和效率方面取得了显著进展，为创建高质量、多样化和可控的 3D 内容开辟了新途径。然而，如何在保持高效率的同时实现极致的 3D 几何精确性，以及更深层次的多模态融合，仍将是未来研究的重点。

### 参考文献

*   [hub.baai.ac.cn] Wu, J. Z., Zhang, Y., Turki, H., Ren, X., Gao, J., Shou, M. Z., ... & Ling, H. (2025). Difix3D+: Improving 3D Reconstructions with Single-Step Diffusion Models. *智源社区论文*.
*   [chatpaper.com] Mo, S., Xie, E., Chu, R., HONG, L., Nießner, M., & Li, Z. (2025). DiT-3D: Exploring Plain Diffusion Transformers for 3D Shape Generation. *NeurIPS*.
*   [chatpaper.com] Liu, F., Wu, D., Wei, Y., Rao, Y., & Duan, Y. (2024). Sherpa3D: Boosting High-Fidelity Text-to-3D Generation via Coarse 3D Prior. *CVPR*.
*   [zhuanzhi.ai] Zeng, X., Vahdat, A., Williams, F., Gojcic, Z., Litany, O., Fidler, S., & Kreis, K. (2022). LION: Latent Point Diffusion Models for 3D Shape Generation. *ArXiv preprint*.
*   [blog.csdn.net] m0_60177079. (2025). CAT3D: Create Anything in 3D with Multi-View Diffusion Models 论文解读. *CSDN Blog*.
*   [chatpaper.com] Kolotouros, N., Alldieck, T., Corona, E., Bazavan, E. G., & Sminchisescu, C. (2025). Instant 3D Human Avatar Generation using Image Diffusion Models. *ECCV*.
*   [themoonlight.io] [论文审查] Enhancing Single Image to 3D Generation using Gaussian Splatting and Hybrid Diffusion Priors. (2025). *The Moonlight*.
*   [aas.net.cn] 朱泓舟, 杨雪, 赵敏, 李崇轩, & 朱军. (2025). 3D空间先验驱动的相机轨迹可控视频扩散生成模型. *自动化学报*.
*   [hkxb.buaa.edu.cn] 薛有涛, 尧少波, 杨雨欣, 段毅, 赵文文, & 李昊歌. (2025). 基于生成式模型的三维飞行器外形泛化表征方法. *航空学报*.
*   [hub.baai.ac.cn] Wang, Z., Li, D., & Jiang, R. (2024). Diffusion Models in 3D Vision: A Survey. *智源社区论文*.