好的，作为一名严谨的科研助手，我将基于您提供的真实网络搜索结果，生成一篇关于“基于扩散技术的三维重建与生成模型”的学术综述。

### **基于扩散技术的三维重建与生成模型研究综述 (2022–2025)**

---

#### **引言**

三维内容的创建与理解是计算机视觉和图形学的核心挑战。近年来，以去噪扩散概率模型（Denoising Diffusion Probabilistic Models, DDPMs）为代表的扩散技术，因其强大的生成能力和稳定的训练过程，在二维图像生成领域取得了革命性突破，并迅速扩展到三维视觉领域 [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/a77ae72a-e5f4-4bc4-9c0a-62b1d990be91)。与传统的生成对抗网络（GANs）或变分自编码器（VAEs）相比，扩散模型能更好地捕捉复杂数据的分布，为解决三维数据固有的高维度、稀疏性和结构复杂性等问题提供了全新范式。

尽管潜力巨大，但将扩散模型应用于三维任务仍面临诸多挑战：(1) 缺乏大规模、高质量的三维场景标注数据；(2) 三维表示（如点云、网格、隐式场）的多样性与非结构化特性；(3) 在生成过程中维持三维几何一致性的困难。为应对这些挑战，研究者们在2022年至2025年间提出了一系列创新方法。本综述旨在系统梳理这一时期内，利用扩散技术进行三维重建与生成的代表性工作，剖析其核心思想与技术演进，并展望未来的研究趋势。

---

#### **方法分类与代表作**

基于研究目标和技术路径的差异，我们将代表性工作分为以下四类：3D对象与形状生成、单/稀疏视图三维重建、用于加速3D生成的潜空间扩散、以及基于扩散的3D表示精炼。

##### **1. 3D对象与形状生成**
此类方法旨在从随机噪声或文本等条件出发，直接生成高质量的3D对象或场景。

*   **LION (Latent Point Diffusion Models for 3D Shape Generation, NeurIPS 2022)**
    该研究致力于在生成高质量3D形状的同时，保证模型具有良好的可编辑性和多任务适用性。为此，LION提出了一种分层潜点扩散模型，其本质是一个变分自编码器（VAE），将3D形状编码到一个包含全局形状信息和点云结构化信息的混合潜空间。研究者在该潜空间中训练两个级联的扩散模型进行生成，从而在保证生成质量的同时，使模型能够便捷地应用于文本/图像条件生成、形状插值等多种下游任务。实验表明，LION在ShapeNet数据集的生成任务上达到了当时的最佳性能 [zhuanzhi.ai](https://www.zhuanzhi.ai/paper/731cfc5d4536d93cf9f94aea445edfc5)。

*   **DiT-3D (Exploring Plain Diffusion Transformers for 3D Shape Generation, NeurIPS 2023)**
    该工作旨在验证Vision Transformer（ViT）架构在3D形状生成任务中的潜力，以替代当时主流的U-Net架构。DiT-3D采用了一个朴素的Transformer模型，直接对体素化的点云执行去噪过程。为解决三维数据带来的高计算复杂度，该模型引入了3D窗口注意力机制来约束自注意力的计算范围。关键实验发现，在ImageNet上预训练的2D DiT模型权重能显著提升DiT-3D在ShapeNet数据集上的性能，最终在高保真点云生成方面取得了SOTA表现 [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/10882)。

*   **Sherpa3D (Boosting High-Fidelity Text-to-3D Generation via Coarse 3D Prior, CVPR 2024)**
    该研究关注如何解决文本到3D生成中的“多面神”（Janus）问题，并融合2D扩散模型强大的纹理生成能力与3D模型良好的几何一致性。Sherpa3D提出了一种新颖的指导策略，首先利用3D扩散模型生成一个粗略的3D先验（Coarse 3D Prior），然后以此为基础设计了“结构指导”和“语义指导”两种策略。这两种策略被用于引导一个基于2D扩散模型的优化过程（Score Distillation），从而在实现高保真纹理的同时保证了几何的正确性。实验证明，该方法在生成质量和3D一致性上均优于当时的SOTA方法 [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/46408)。

##### **2. 单/稀疏视图三维重建**
此类方法专注于从单张或少量几张图像中恢复完整的三维模型，扩散模型主要用于提供强大的先验知识以补全未观测区域。

*   **CAT3D (Create Anything in 3D with Multi-View Diffusion Models, 2024)**
    该研究首次将欠约束的稀疏视图重建问题，形式化为一个生成问题，旨在从单视图或稀疏视图输入生成一个完整且一致的3D场景。其核心是一个两阶段框架：首先，利用一个经过特殊设计的多视角扩散模型（MVLDM）生成大量与输入视图保持三维一致性的新视角图像；随后，将这些生成的密集视图作为输入，送入标准的3D重建流程（如NeRF）。该方法中的MVLDM通过引入3D自注意力机制来建模跨视图依赖关系，从而保证了生成视图的一致性。实验表明，CAT3D能够在一分钟内生成高质量结果，比以往方法快一个数量级 [blog.csdn.net](https://blog.csdn.net/m0_60177079/article/details/144796428)。

*   **Enhancing Single Image to 3D Generation using Gaussian Splatting and Hybrid Diffusion Priors (2024)**
    这项工作旨在提升单图像到3D生成的几何真实感与视觉保真度，特别是在3D高斯泼溅（Gaussian Splatting, GS）表示上。其核心是一种两阶段优化策略，首先利用多视角生成模型（如Zero123++）初始化一个粗糙的3D高斯表示。接着，通过一种创新的混合频率得分蒸馏损失（hf-SDL）对其进行优化，该损失函数将来自3D扩散模型的低频几何先验和来自2D扩散模型的高频纹理先验分离开来，协同优化几何结构与表面细节。实验结果显示，该方法在Google Scanned Objects等多个数据集上的2D纹理和3D几何指标均超越了现有SOTA [themoonlight.io](https://www.themoonlight.io/zh/review/enhancing-single-image-to-3d-generation-using-gaussian-splatting-and-hybrid-diffusion-priors)。

*   **Instant 3D Human Avatar Generation using Image Diffusion Models (ECCV 2024)**
    该研究聚焦于从文本或单张图像快速生成高质量的3D数字人化身，并提供姿态和体型控制。其方法论的核心在于解耦2D生成与3D提升（3D lifting）：首先，通过对大规模图像扩散模型进行微调，使其能够根据输入条件生成目标人物的正面和背面图像；然后，一个独立的3D提升网络将这些2D图像作为输入，快速重建出完整的3D模型。该方法能在2秒内生成一个3D化身，相比此前动辄数小时的优化方法实现了四个数量级的速度提升 [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/97996)。

##### **3. 用于加速3D生成的潜空间扩散**
该方向的核心思想是通过在低维潜空间（Latent Space）中执行扩散过程，来规避在原始高维3D数据上操作带来的巨大计算开销。

*   **Sampling 3D Gaussian Scenes in Seconds with Latent Diffusion Models (2024)**
    此研究旨在解决现有3D感知扩散模型因在每步去噪中进行昂贵的体渲染而导致的采样速度缓慢问题。作者为此设计了一个两阶段的潜扩散框架：首先，训练一个自编码器，该编码器能将多视图图像压缩到一个紧凑的、代表3D高斯泼溅（3DGS）场景的潜空间表示；随后，在这个低维潜空间上训练一个多视图扩散模型。在推理时，模型仅需在潜空间中完成去噪过程，然后通过解码器一次性生成整个3D GS场景。实验表明，该方法仅需0.2秒即可生成一个完整的3D场景，比基于NeRF的生成模型快数个数量级 [blog.csdn.net](https://blog.csdn.net/qq_45752541/article/details/140201446)。

##### **4. 基于扩散的3D表示精炼**
此类方法并非从零开始生成，而是将扩散模型作为一个强大的后处理工具或神经增强器，用于提升已有3D重建结果的质量。

*   **Difix3D+ (Improving 3D Reconstructions with Single-Step Diffusion Models, 2025)**
    该工作旨在解决从极端新视角渲染时，NeRF和3DGS等表示中出现的伪影（artifacts）问题。其核心是提出了一种名为`Difix`的单步图像扩散模型，作为一个通用的神经增强器。在重建阶段，`Difix`被用来“清洗”含有伪影的训练视图，从而提炼出更高质量的3D表示。在推理阶段，它直接对新视角的渲染结果进行去伪影处理。实验结果显示，该方法在保持3D一致性的前提下，相比基线模型平均提升了2倍的FID分数，且单一模型能同时兼容NeRF和3DGS两种表示 [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/5d599177-dda4-48f2-91a7-b5de0449e570)。

---

#### **实验与评价总结**

对2022-2025年间的代表性工作进行分析，可以总结出以下共性结论：
*   **混合先验策略的有效性：** 结合强大的2D图像扩散先验（提供丰富、逼真的纹理和细节）与3D结构先验或3D感知架构（保证几何一致性）成为一种主流且高效的策略。如 Sherpa3D 和 "Enhancing Single Image to 3D Generation..." 等工作明确证明，这种“2D负责纹理，3D负责几何”的分工能够显著提升生成质量。
*   **潜空间操作的大幅加速：** 直接在三维数据（如体素、点云）或其渲染的像素空间执行扩散过程计算成本极高。通过设计自编码器将三维场景压缩至低维潜空间，并在该空间训练扩散模型（如 LION、"Sampling 3D Gaussian Scenes..."），能够将生成速度提升数个数量级，是实现快速乃至实时生成的关键。
*   **3D表示与模型架构的协同进化：** 研究趋势显示，从NeRF到3D高斯泼溅（3DGS）的转变不仅提升了渲染效率，也为生成模型的设计带来了新的思路。3DGS的显式、可微特性使得与其结合的生成或优化过程（如hf-SDL）更为直接高效。同时，Transformer等新架构（如DiT-3D）也开始替代U-Net，展现出更强的可扩展性和建模能力。
*   **通用评价指标的融合使用：** 评价体系通常结合2D和3D指标。2D指标如Fréchet Inception Distance (FID) 用于评估渲染图像的感知质量与多样性，LPIPS和PSNR用于衡量新视角合成的准确性。3D几何相关的评价相对欠缺标准化，但部分工作开始引入COLMAP重建失败率等指标来间接评估生成视频或多视图图像集的几何一致性 [aas.net.cn](https://aas.net.cn/cn/article/doi/10.16383/j.aas.c250124?viewType=HTML)。

---

#### **趋势与挑战**

基于当前研究进展，可以预见2025年前后，该领域将呈现以下主要趋势和挑战：
1.  **向高效、统一的单阶段生成框架演进：** 当前许多先进方法仍依赖于多阶段流程（如先生成多视图再重建，或先粗糙生成再精细优化）。未来的研究将致力于构建端到端的单阶段生成模型，直接从输入条件生成高质量、结构化的3D表示（如3DGS），从而进一步提升效率和易用性。
2.  **增强可控性与向动态场景扩展：** 研究重点正从生成静态对象转向生成具有精细控制能力的动态4D内容。这包括对物体姿态、相机轨迹、场景光照的精确控制，以及将3D空间一致性原则扩展到时间维度，以生成连贯、真实的视频内容。相关工作（如"3D空间先验驱动的相机轨迹可控视频扩散生成模型"）已在该方向上展现出巨大潜力 [aas.net.cn](https://aas.net.cn/cn/article/doi/10.16383/j.aas.c250124?viewType=HTML)。
3.  **与大规模多模态模型的深度融合：** 如何更有效地利用大规模预训练模型（如LLM、VLM）的知识来指导和约束3D生成是未来的关键。这不仅限于使用文本提示，更包括利用模型对物理常识、功能属性、空间关系的理解来生成更具真实感和功能性的3D世界，弥补纯几何生成模型的不足。

---

#### **结论**

在2022至2025年间，基于扩散技术的三维重建与生成领域取得了飞速发展。研究者们通过引入混合先验、开发潜空间模型、探索新颖的3D表示与网络架构，在生成质量、速度和可控性方面实现了显著突破。扩散模型已成为该领域最具主导力的技术范式。尽管在高质量3D数据稀缺、评估标准统一化等方面仍面临挑战，但随着模型向更高效、可控和多模态的方向发展，我们有理由相信，由扩散模型驱动的3D内容生成技术将在不久的将来为虚拟现实、机器人、数字孪生等应用带来颠覆性的变革。

---

#### **参考文献**

[1] Vahdat, A., Williams, F., Gojcic, Z., et al. (2022). LION: Latent Point Diffusion Models for 3D Shape Generation. *NeurIPS 2022*. [zhuanzhi.ai](https://www.zhuanzhi.ai/paper/731cfc5d4536d93cf9f94aea445edfc5)
[2] Mo, S., Xie, E., Chu, R., et al. (2023). DiT-3D: Exploring Plain Diffusion Transformers for 3D Shape Generation. *NeurIPS 2023*. [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/10882)
[3] Liu, F., Wu, D., Wei, Y., et al. (2024). Sherpa3D: Boosting High-Fidelity Text-to-3D Generation via Coarse 3D Prior. *CVPR 2024*. [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/46408)
[4] Gao, R., Holynski, A., Henzler, P., et al. (2024). CAT3D: Create Anything in 3D with Multi-View Diffusion Models. *arXiv*. [blog.csdn.net](https://blog.csdn.net/m0_60177079/article/details/144796428)
[5] Anciukevicius, T., et al. (2024). Enhancing Single Image to 3D Generation using Gaussian Splatting and Hybrid Diffusion Priors. *arXiv*. [themoonlight.io](https://www.themoonlight.io/zh/review/enhancing-single-image-to-3d-generation-using-gaussian-splatting-and-hybrid-diffusion-priors)
[6] Kolotouros, N., Alldieck, T., Corona, E., et al. (2024). Instant 3D Human Avatar Generation using Image Diffusion Models. *ECCV 2024*. [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/97996)
[7] "杀生丸学AI". (2024). 【三维AIGC】扩散模型LDM辅助3D Gaussian重建三维场景. *CSDN Blog*. [blog.csdn.net](https://blog.csdn.net/qq_45752541/article/details/140201446)
[8] Wu, J. Z., Zhang, Y., Turki, H., et al. (2025). Difix3D+: Improving 3D Reconstructions with Single-Step Diffusion Models. *arXiv*. [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/5d599177-dda4-48f2-91a7-b5de0449e570)
[9] Wang, Z., Li, D., & Jiang, R. (2024). Diffusion Models in 3D Vision: A Survey. *arXiv*. [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/a77ae72a-e5f4-4bc4-9c0a-62b1d990be91)
[10] Zhu, H., Yang, X., Zhao, M., et al. (2025). 3D空间先验驱动的相机轨迹可控视频扩散生成模型. *自动化学报*. [aas.net.cn](https://aas.net.cn/cn/article/doi/10.16383/j.aas.c250124?viewType=HTML)
[11] Anciukevicius, T., et al. (2023). Renderdiffusion: Image diffusion for 3d reconstruction, inpainting and generation. *CVPR 2023*.
[12] Szymanowicz, S., Rupprecht, C., & Vedaldi, A. (2023). Viewset diffusion: (0-)image-conditioned 3d generative models from 2d data. *ICCV 2023*.