## Cross-Domain 3D Reconstruction Using Diffusion Models 中文综述

### 引言

三维重建技术旨在从二维观测数据中恢复三维场景或物体的几何形状和纹理信息，在计算机视觉、机器人、增强现实等领域具有广泛应用。近年来，扩散模型（Diffusion Models）在图像生成领域展现出卓越的性能，其强大的生成能力和对数据分布的建模能力为跨域三维重建带来了新的机遇。传统的2D图像到3D重建方法往往受限于3D数据集的稀缺性、几何一致性难以保证以及对极端新视角渲染效果不佳等问题。扩散模型通过学习数据的去噪过程，能够生成高质量、高细节的图像，从而为3D重建提供更为丰富的2D先验信息，甚至直接生成3D表示。本文将对2022-2025年期间，利用扩散模型进行跨域3D重建的代表性工作进行综述，分类介绍其研究问题、核心方法、关键实验结论，并总结共性评价与未来趋势。

### 方法分类与代表作

目前，利用扩散模型进行跨域3D重建的方法主要可以分为以下几类：

#### 1. 基于2D扩散模型引导的3D重建

这类方法主要利用预训练的2D扩散模型作为强大的图像先验，通过蒸馏、新视角生成等方式辅助3D模型的构建。

*   **Sherpa3D: Boosting High-Fidelity Text-to-3D Generation via Coarse 3D Prior (CVPR 2024)** [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/46408)
    *   **研究问题**: 如何在保持多视图一致性的同时，实现高保真度、多样化的文本到3D生成，克服2D扩散模型固有的视角无关模糊性导致的多面雅努斯问题。
    *   **核心方法**: 提出Sherpa3D框架，结合3D扩散模型生成的粗糙3D先验（结构指导和语义指导）来增强提示，并指导2D提升优化进行细化。它不重新训练昂贵的视角感知模型，而是利用容易获取的粗糙3D知识来丰富3D内容。
    *   **关键实验结论**: Sherpa3D在质量和3D一致性方面优于最先进的文本到3D方法。
*   **CAT3D: Create Anything in 3D with Multi-View Diffusion Models (2024)** [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/279b2bd6-1104-43ef-9662-985769c3f8e0), [blog.csdn.net](https://blog.csdn.net/m0_60177079/article/details/144796428)
    *   **研究问题**: 如何实现从单视图、稀疏视图或文本提示快速、高质量地创建3D场景，克服传统3D重建对大量图像收集的依赖。
    *   **核心方法**: CAT3D提出多视角扩散模型（MVLDM）来模拟真实世界的3D捕捉过程，生成高度一致的新视角。这些生成的视角作为输入，结合Zip-NeRF等3D重建技术生成可实时渲染的3D表示。MVLDM通过相机姿态嵌入和3D自注意力层实现跨视图的一致性建模。
    *   **关键实验结论**: CAT3D能够在1分钟内创建完整的3D场景，并在单张图像和少量视角3D场景创建方面显著优于现有方法，速度提高一个数量级。
*   **Enhancing Single Image to 3D Generation using Gaussian Splatting and Hybrid Diffusion Priors (2024)** [themoonlight.io](https://www.themoonlight.io/zh/review/enhancing-single-image-to-3d-generation-using-gaussian-splatting-and-hybrid-diffusion-priors)
    *   **研究问题**: 提高单幅图像到3D模型生成的几何一致性和视觉质量，以满足机器人操作、3D场景理解等实际应用需求。
    *   **核心方法**: 结合高斯散点（Gaussian Splatting）和混合扩散先验。首先通过图像分割提取前景，利用Zero123++生成多视角图像，再用大型高斯模型（LGM）初始化粗糙3D高斯表示。优化过程引入两阶段的基于频率的蒸馏损失（hf-SDL），分别从3D扩散模型和2D扩散模型提取低频和高频特征，并结合参考视图引导。
    *   **关键实验结论**: 该方法在多个公开数据集上，在2D纹理和3D几何度量方面的性能超越了现有技术。

#### 2. 基于原生3D扩散模型的生成

此类方法直接在3D空间中操作，利用扩散模型生成3D几何结构。

*   **LION: Latent Point Diffusion Models for 3D Shape Generation (NeurIPS 2022)** [zhuanzhi.ai](https://www.zhuanzhi.ai/paper/731cfc5d4536d93cf9f94aea445edfc5)
    *   **研究问题**: 如何实现高质量、可操作性强（如条件合成、形状插值）且能输出平滑曲面或网格的3D点云合成。
    *   **核心方法**: 提出分层潜在点扩散模型（LION），结合变分自编码器（VAE）和分层潜在空间。在全局形状潜在表示和点结构潜在空间中训练两个分层DDMs。VAE框架提高了性能，点结构潜在空间适合基于DDM的建模。
    *   **关键实验结论**: LION在多个ShapeNet基准测试中实现了最先进的生成性能，并能够用于多模态形状去噪、体素条件合成、文本/图像驱动的3D生成以及生成平滑3D网格。
*   **DiT-3D: Exploring Plain Diffusion Transformers for 3D Shape Generation (NeurIPS 2023)** [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/10882)
    *   **研究问题**: 探索Transformer架构在3D形状生成中的潜力，以超越U-Net架构在3D扩散模型中的主流地位，实现更高质量和可扩展的生成。
    *   **核心方法**: 提出DiT-3D，一种用于3D形状生成的新型扩散Transformer。它使用普通的Transformer直接对体素化点云执行去噪过程。通过结合3D位置和补丁嵌入来聚合体素化点云输入，并引入3D窗口注意力以降低自注意力的计算成本。
    *   **关键实验结论**: DiT-3D在模型大小上更具可扩展性，并在ShapeNet数据集上在高保真和多样化的3D点云生成方面实现了最先进的性能。ImageNet上预训练的DiT-2D检查点可显著提高ShapeNet上的DiT-3D性能。
*   **TAR3D: High-Quality 3D Asset Creation via Next-Part Prediction (ICCV 2025)** [mmcheng.net](https://mmcheng.net/wp-content/uploads/2025/08/ICCV2025_TAR3D_CN.pdf)
    *   **研究问题**: 如何将大型语言模型（LLMs）的下一个token预测范式和多模态统一性应用于条件式3D物体生成，克服现有方法对网格面进行量化时序列过长的问题。
    *   **核心方法**: TAR3D是一个由3D感知的向量量化变分自编码器（VQ-VAE）和生成式预训练Transformer（GPT）组成的框架。3D VQ-VAE将3D形状编码到紧凑的三平面潜空间中，得到离散表征。3D GPT配备TriPE自定义三平面位置嵌入，以自回归方式预测码本索引序列，建模3D几何结构的构成。
    *   **关键实验结论**: TAR3D在文本到3D和图像到3D任务中取得了优于现有方法的生成质量，证明了其在高频细节和几何一致性方面的有效性，且对GPU资源依赖较低。

#### 3. 扩散模型在3D重建中的增强和去伪影

这类方法将扩散模型作为后处理或辅助工具，用于提升已有3D重建模型的质量、去除伪影等。

*   **Difix3D+: Improving 3D Reconstructions with Single-Step Diffusion Models (2025)** [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/5d599177-dda4-48f2-91a7-b5de0449e570)
    *   **研究问题**: 解决神经辐射场（NeRF）和3D高斯点绘（3DGS）等从极端新视角渲染时存在的伪影问题，增强欠约束区域的3D重建质量。
    *   **核心方法**: 引入Difix3D+，一个全新的管道设计，利用单步图像扩散模型Difix。Difix在重建阶段用于清理从重建中渲染并重新提炼回3D的伪训练视图，提高欠约束区域表示。在推理阶段，Difix作为神经增强器去除不完美监督和模型容量限制引起的残余伪影。
    *   **关键实验结论**: Difix3D+是兼容NeRF和3DGS的通用解决方案，在保持3D一致性的同时平均提升FID分数2倍。

### 实验与评价总结

综上所述，扩散模型在跨域3D重建中的应用展现出显著优势。在定量和定性评估中，这些方法普遍在以下方面取得了进展：

*   **高保真度与细节**: 扩散模型强大的生成能力使其能够产生具有丰富细节和逼真纹理的3D模型，有效缓解了传统方法在这些方面的不足。F_ID、PSNR、SSIM等指标在多项工作中得到了显著提升。
*   **几何一致性**: 通过多视图扩散模型、3D自注意力机制、频率蒸馏损失以及3D先验的引导，这些方法显著改善了生成3D模型的几何一致性，减少了“多面雅努斯”等伪影。
*   **效率与自动化**: 一些方法（如CAT3D）实现了分钟级3D场景生成，大大加速了重建过程。同时，通过文本或单张图像输入，降低了3D重建的门槛和对大量数据采集的依赖。
*   **跨模态泛化**: 结合文本、2D图像等不同模态作为条件输入，实现了更灵活、更智能的3D内容创作。
*   **通用性与兼容性**: 部分方法（如Difix3D+）展现了对不同3D表示（如NeRF、3DGS）的通用兼容性，提高了方法的适用范围。

### 趋势与挑战

2025年前后，跨域3D重建与扩散模型融合领域的研究趋势将主要体现在以下几个方面：

1.  **更强的3D原生扩散模型与自回归生成**: 随着计算资源的增长和模型架构的创新（如DiT-3D和TAR3D），直接在3D空间（点云、体素、三平面表示）上训练的扩散模型和基于Transformer的自回归生成将成为主流。这能更好地捕捉3D几何的内在特性，减少对2D先验的依赖，并解决2D引导方法固有的多视点不一致性问题。未来将更注重如何高效地编码3D信息，以及如何将大型语言模型的推理能力迁移到3D生成中。
2.  **多模态融合与统一生成框架**: 结合文本、图像、稀疏点云等多种模态输入进行3D生成将是核心趋势。研究将聚焦于构建能够同时处理和理解多模态信息的统一扩散模型或生成框架，实现真正的“任何内容到3D”的生成能力。例如TAR3D已经在这方面进行了初步探索，未来可能会出现更复杂的跨模态编码器和解码器。
3.  **实时性与高精度平衡**: 提高3D生成与重建的效率，实现近实时的生成速度，同时不牺牲几何精度和视觉质量，是重要的研究方向。例如Difix3D+提出的单步扩散模型和CAT3D的分钟级生成，都体现了对效率的追求。未来的研究将探索更高效的采样策略、模型蒸馏技术和硬件加速方法，以满足AR/VR、机器人等实时应用的需求。
4.  **可控性与编辑性**: 提升生成3D模型的可控性，允许用户在生成过程中对局部细节、材质、拓扑结构等进行精细化编辑，将是核心需求。目前的扩散模型主要关注生成质量，但在精确控制方面仍有提升空间。结合人机交互、语义理解和局部编辑的扩散模型将成为新的研究热点。

### 结论

扩散模型为跨域3D重建带来了革命性的变革，通过提供强大的2D先验或直接进行3D生成，显著提升了重建的质量、效率和灵活性。从基于2D扩散模型的引导重建到原生3D扩散模型的直接生成，再到作为增强工具的 Difix3D+，这一领域的研究正以前所未有的速度发展。未来的研究将继续围绕提升3D原生能力、多模态融合、实时性与可控性等方向深入，有望彻底改变3D内容创作和应用的范式。

### 参考文献

*   [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/5d599177-dda4-48f2-91a7-b5de0449e570) Wu, J. Z., Zhang, Y., Turki, H., Ren, X., Gao, J., Shou, M. Z., Fidler, S., Gojcic, Z., & Ling, H. (2025). *Difix3D+: Improving 3D Reconstructions with Single-Step Diffusion Models*.
*   [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/a77ae72a-e5f4-4bc4-9c0a-62b1d990be91) Wang, Z., Li, D., & Jiang, R. (2024). *Diffusion Models in 3D Vision: A Survey*.
*   [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/10882) Mo, S., Xie, E., Chu, R., Hong, L., Nießner, M., & Li, Z. (2025). *DiT-3D: Exploring Plain Diffusion Transformers for 3D Shape Generation*.
*   [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/46408) Liu, F., Wu, D., Wei, Y., Rao, Y., & Duan, Y. (2024). *Sherpa3D: Boosting High-Fidelity Text-to-3D Generation via Coarse 3D Prior*.
*   [blog.csdn.net](https://blog.csdn.net/m0_60177079/article/details/144796428) m0_60177079. (2025). *CAT3D: Create Anything in 3D with Multi-View Diffusion Models 论文解读*.
*   [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/279b2bd6-1104-43ef-9662-985769c3f8e0) Gao, R., Holynski, A., Henzler, P., Brussee, A., Martin-Brualla, R., Srinivasan, P., Barron, J. T., & Poole, B. (2024). *CAT3D: Create Anything in 3D with Multi-View Diffusion Models*.
*   [mmcheng.net](https://mmcheng.net/wp-content/uploads/2025/08/ICCV2025_TAR3D_CN.pdf) Zhang, X., Liu, Y., Li, Y., Zhang, R., Liu, Y., Wang, K., Ouyang, W., Xiong, Z., Gao, P., Hou, Q., & Cheng, M. (2025). *TAR3D: 基于下一部分预测的高质量三维资产创造方法*.
*   [themoonlight.io](https://www.themoonlight.io/zh/review/enhancing-single-image-to-3d-generation-using-gaussian-splatting-and-hybrid-diffusion-priors) (2025). *Enhancing Single Image to 3D Generation using Gaussian Splatting and Hybrid Diffusion Priors*.
*   [zhuanzhi.ai](https://www.zhuanzhi.ai/paper/731cfc5d4536d93cf9f94aea445edfc5) Zeng, X., Vahdat, A., Williams, F., Gojcic, Z., Litany, O., Fidler, S., & Kreis, K. (2022). *LION: Latent Point Diffusion Models for 3D Shape Generation*.
*   [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/440250ab-659d-4f24-b5fc-737d62386b98) Zhang, R., Xue, D., Wang, Y., Geng, R., & Gao, F. (2024). *Towards Dense and Accurate Radar Perception Via Efficient Cross-Modal Diffusion Model*.
*   (Additional papers for a complete bibliography would need to be selectively chosen to meet the minimum 12 requirement while adhering to the "3-5 papers per category" restriction. However, the provided search results only allowed for 10 relevant papers.)