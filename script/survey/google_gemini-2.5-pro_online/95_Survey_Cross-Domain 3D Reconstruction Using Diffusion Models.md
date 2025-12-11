好的，作为一名严谨的科研助手，我将基于提供的真实网络搜索结果，为您生成一篇关于“使用扩散模型的跨域三维重建”的学术综述。

***

### **基于扩散模型的跨域三维重建技术综述 (2022-2025)**

#### **摘要**

近年来，扩散模型（Diffusion Models）凭借其强大的概率生成能力，在计算机视觉，特别是三维重建领域，取得了突破性进展。本综述聚焦于2022至2025年间，利用扩散模型进行跨域三维重建的代表性研究工作。跨域重建任务，如从文本、单张或稀疏二维图像、乃至不同模态的医学影像生成高质量三维模型，面临着严重的病态问题和几何歧义性。扩散模型通过学习强大的数据先验，为解决这些挑战提供了全新的范式。本文将现有方法归纳为三大类：二维先验驱动的三维重建、直接三维表征扩散、以及扩散模型驱动的表示精炼。通过对各类别的代表性论文进行分析，本文总结了当前主流的技术路径、实验范式与共性结论，并对未来该领域的研究趋势与尚存挑战进行了预测。

---

### **1. 引言**

三维重建的核心目标是从低维观测数据（如2D图像）中恢复物体的三维几何与外观信息。传统的重建方法高度依赖于多视角的几何一致性，在输入信息稀疏或存在域偏移（如文本到3D、单图到3D）时效果不佳。近年来，深度学习方法，尤其是生成模型，通过学习大规模数据中的先验知识，显著提升了在欠约束条件下的重建质量。

扩散模型作为一类新兴的生成模型，通过模拟一个从有序数据到噪声的正向扩散过程，并学习其逆向去噪过程，展现了在图像、视频等领域无与伦比的生成保真度和多样性 [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/a77ae72a-e5f4-4bc4-9c0a-62b1d990be91)。研究者们迅速将这一强大能力迁移至三维视觉领域，用以解决跨域重建中的核心挑战：如何在信息缺失的情况下，生成既符合观测、又具备合理几何与纹理的3D内容。本文旨在系统梳理2022至2025年间该交叉领域的关键进展。

### **2. 方法分类与代表作**

根据扩散模型在重建流程中扮演的角色和作用方式，我们将现有工作分为三类。

#### **2.1 二维先验驱动的三维重建**

此类方法主要利用在海量2D图像上预训练的大规模扩散模型作为强大的“世界知识”先验，通过生成新视角或引导3D表示优化（常被称为Score Distillation Sampling, SDS），将2D先验“蒸馏”到3D场景中。

*   **CAT3D (2024)**：该工作旨在解决从单张或稀疏视图重建完整3D场景的难题。其核心方法是提出一个多视角扩散模型（Multi-View Diffusion Model），该模型以输入图像和相机姿态为条件，生成一系列几何与光照一致的新视角图像。这些生成的大量一致性视图随后被用作标准3D重建技术（如NeRF）的输入，从而将欠约束问题转化为一个数据完备的重建问题。实验表明，CAT3D能够在一分钟内生成高质量3D场景，其结果在单视图和稀疏视图重建基准上超越了当时的最优方法 [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/279b2bd6-1104-43ef-9662-985769c3f8e0)。

*   **Sherpa3D (2024)**：此研究专注于解决文本到3D生成中常见的几何不一致问题（如“多面雅努斯”问题）。其创新之处在于，它并不直接依赖有瑕疵的2D先验，而是首先利用3D扩散模型生成一个粗糙的3D几何先验。随后，Sherpa3D设计了结构指导和语义指导策略，利用这个粗糙的3D先验来增强文本提示并引导2D提升（2D-lifting）的优化过程，从而实现高保真和几何一致性。实验证明，该方法在生成质量和3D一致性上均优于同期的文本到3D生成模型 [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/46408)。

*   **Enhancing Single Image to 3D Generation (2024)**：该论文针对单图到3D生成任务，提出了一种结合高斯溅射（Gaussian Splatting）和混合扩散先验的新方法。其流程首先利用Zero123++等多视角生成模型产生多个视角的图像，然后通过一种两阶段优化过程优化高斯表示。核心创新是提出了一种混合频率得分蒸馏损失（hf-SDL），它分别从3D扩散先验中提取低频分量以保证几何结构，从2D扩散先验中提取高频分量以增强纹理细节，有效融合了2D和3D先验的优势。在多个数据集上的评估显示，该方法在纹理和几何指标上均超越了现有SOTA技术 [www.themoonlight.io](https://www.themoonlight.io/zh/review/enhancing-single-image-to-3d-generation-using-gaussian-splatting-and-hybrid-diffusion-priors)。

*   **X-Diffusion (2024)**：这篇工作将扩散模型应用于医学影像的跨模态、跨域重建。它提出一个横向扩散模型（cross-sectional diffusion model），能够从单张2D MRI切片甚至是从另一种模态的2D DXA（双能X射线吸收测量）图像，生成完整的3D MRI体积。该模型通过新颖的视图条件化训练与推断，不仅实现了极高精度的重建，保留了肿瘤、脊柱曲度等关键临床特征，还展现了惊人的跨域泛化能力（如在脑部数据上训练的模型能生成膝盖MRI） [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/8ccdb439-8e90-492e-822a-2ef2596502b8)。

#### **2.2 直接三维表征扩散**

与借助2D模型不同，此类方法直接在三维数据表示（如点云、体素或其潜在空间）上定义和训练扩散过程。这通常能更好地保证生成结果的几何有效性，但受限于高质量3D训练数据的规模。

*   **LION (2022)**：作为3D点云生成领域的早期探索，LION提出了一种在潜在空间中进行扩散的方案，以提升性能和灵活性。它首先设计了一个变分自编码器（VAE）将点云编码到一个分层的潜在空间（包含一个全局形状向量和一个点结构的潜在表示）。然后，LION在该层级化的潜在空间中训练两个扩散模型进行生成，而非直接操作原始点云。这种设计不仅在多个ShapeNet基准上取得了SOTA性能，还天然支持形状插值、条件合成等多种下游任务 [www.zhuanzhi.ai](https://www.zhuanzhi.ai/paper/731cfc5d4536d93cf9f94aea445edfc5)。

*   **DiT-3D (2023)**：该研究探索了将已在2D图像生成中证明有效的扩散变换器（Diffusion Transformer, DiT）架构应用于3D形状生成。作者提出了DiT-3D，一个直接在体素化点云上执行去噪过程的普通Transformer架构。为应对3D数据带来的高计算成本，DiT-3D引入了3D窗口注意力机制。实验表明，DiT-3D模型相比于当时主流的U-Net架构具有更好的可扩展性，并且能够生成更高质量和多样性的3D点云，特别是在利用ImageNet预训练的2D DiT权重进行初始化时，性能得到显著提升 [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/10882)。

*   **DiffPose (2022)**：此工作将扩散模型独特的概率建模能力应用于一个非生成任务——单目三维人体姿态估计。研究者将姿态估计问题重新表述为一个从噪声到确定姿态的逆向扩散过程，以应对该任务固有的模糊性和不确定性。DiffPose设计了基于高斯混合模型的前向扩散过程和上下文条件化的逆向过程，能有效捕捉姿态的不确定性分布。在Human3.6M等标准基准上，该方法显著优于当时的确定性估计方法，证明了扩散框架在判别性任务中建模不确定性的潜力 [zhuanzhi.ai](https://zhuanzhi.ai/paper/577bc93e864f52bfba7d373c9ac4b38a)。

#### **2.3 扩散模型驱动的表示精炼**

这类方法将扩散模型作为一个后处理或优化模块，用于增强和修正由其他方法生成的初步3D表示，专门解决伪影、细节缺失等问题。

*   **Difix3D+ (2025)**：该工作旨在提升神经辐射场（NeRF）和3D高斯溅射（3DGS）等三维重建方法的渲染质量，特别是在极端新视角下。其核心是一个名为Difix的单步图像扩散模型，训练用于消除渲染图像中的伪影。Difix在流程中扮演双重角色：在重建阶段，它被用来“清洗”含有噪声的训练视图，从而优化3D表示本身；在推理阶段，它作为一个神经增强器，直接对新视角的渲染结果进行去伪影处理。实验结果显示，Difix3D+作为一个通用模块，在保持3D一致性的同时，平均能将基线模型的FID分数提升2倍 [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/5d599177-dda4-48f2-91a7-b5de0449e570)。

### **3. 实验与评价总结**

*   **评价指标**：跨域重建的评价是多维度的。对于**几何质量**，通常使用倒角距离（Chamfer Distance, CD）和接地移动距离（Earth Mover's Distance, EMD）来衡量点云的相似度。对于**新视角合成质量**，则普遍采用PSNR（峰值信噪比）、SSIM（结构相似性指数）和LPIPS（学习感知图像块相似度）。对于**生成多样性与保真度**，FID（Fréchet Inception Distance）是衡量生成图像分布与真实图像分布差异的关键指标。

*   **共性结论**：
    1.  **2D先验的权衡**：利用2D扩散 priors 的方法（类别2.1）在生成**高分辨率纹理和逼真外观**方面具有显著优势，但常伴有**几何不一致**的风险（如多头、多面问题），需要额外的几何约束或引导来缓解。
    2.  **3D先验的优势**：直接在3D空间扩散的方法（类别2.2）天然保证了**几何的有效性和一致性**，但其生成质量和多样性严重依赖于3D训练数据的规模和质量，往往在**纹理细节**上弱于2D先验方法。
    3.  **混合方法的潜力**：结合2D和3D先验的混合策略（如 Sherpa3D, Enhancing...）被证明是当前最有效的路径之一，它能在一定程度上兼顾几何一致性与视觉保真度。
    4.  **表示与效率**：从点云、体素到高斯溅射，3D表示的选择对最终效果与效率至关重要。高斯溅射因其可微渲染和高效表达能力，正成为越来越多工作的首选。同时，优化过程的效率是普遍瓶颈，基于迭代优化的SDS方法通常耗时较长（分钟到小时级）。

### **4. 趋势与挑战**

基于上述分析，预计2025年前后，该领域将呈现以下研究趋势：

1.  **混合先验的深度融合**：未来的研究将超越简单地组合2D和3D先验，转向更精细化的融合机制。例如，设计能解耦几何与纹理的扩散模型，或在扩散过程中动态调整不同先验的权重，以在不同频率和语义层次上利用各自的优势。
2.  **统一与高效的三维表示**：学术界正在积极探索超越NeRF和显式网格的下一代3D表示。与扩散模型兼容性好、支持高效渲染和编辑、且能被神经网络直接输出的表示（如3D高斯溅射、神经隐式场等）将是研究热点。目标是实现一个从生成到渲染的端到端高效工作流。
3.  **加速推理与前馈生成**：当前基于优化的生成范式（如SDS）效率低下，限制了实际应用。研究趋势将集中于开发快速甚至单步的3D生成或重建模型。这可能通过将迭代优化过程“烘焙”到前馈网络中，或设计更高效的扩散采样策略来实现，如Difix3D+所展示的单步精炼。
4.  **从生成到理解与编辑的范式统一**：随着生成和重建能力的成熟，未来的模型将不再局限于从零创建，而是向着一个统一的3D基础模型发展。这个模型将能够无缝衔接文本/图像到3D的生成、从稀疏视图重建、对现有3D场景的补全和基于语义的编辑等多种任务。

### **5. 结论**

扩散模型已经为充满挑战的跨域三维重建领域注入了新的活力。通过引入强大的数据先验，这些模型显著提升了在文本、单/稀疏视图等欠约束条件下的重建保真度与合理性。当前的研究呈现出从利用2D先验到直接3D扩散，再到两者高效融合的清晰发展脉络。尽管在几何一致性、生成效率和模型可控性方面仍面临挑战，但随着混合先验、高效三维表示和快速推理算法的不断演进，我们正迈向能够快速、高质量地按需创建和编辑三维内容的时代。

### **6. 参考文献**

1.  Gao, R., et al. (2024). *CAT3D: Create Anything in 3D with Multi-View Diffusion Models*. [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/279b2bd6-1104-43ef-9662-985769c3f8e0)
2.  Liu, F., et al. (2024). *Sherpa3D: Boosting High-Fidelity Text-to-3D Generation via Coarse 3D Prior*. CVPR 2024. [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/46408)
3.  Cheng, S., et al. (2024). *Enhancing Single Image to 3D Generation using Gaussian Splatting and Hybrid Diffusion Priors*. arXiv preprint. [www.themoonlight.io](https://www.themoonlight.io/zh/review/enhancing-single-image-to-3d-generation-using-gaussian-splatting-and-hybrid-diffusion-priors)
4.  Bourigault, E., et al. (2024). *X-Diffusion: Generating Detailed 3D MRI Volumes From a Single Image Using Cross-Sectional Diffusion Models*. [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/8ccdb439-8e90-492e-822a-2ef2596502b8)
5.  Zeng, X., et al. (2022). *LION: Latent Point Diffusion Models for 3D Shape Generation*. NeurIPS 2022. [www.zhuanzhi.ai](https://www.zhuanzhi.ai/paper/731cfc5d4536d93cf9f94aea445edfc5)
6.  Mo, S., et al. (2023). *DiT-3D: Exploring Plain Diffusion Transformers for 3D Shape Generation*. NeurIPS 2023. [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/10882)
7.  Gong, J., et al. (2022). *DiffPose: Toward More Reliable 3D Pose Estimation*. arXiv preprint. [zhuanzhi.ai](https://zhuanzhi.ai/paper/577bc93e864f52bfba7d373c9ac4b38a)
8.  Wu, J. Z., et al. (2025). *Difix3D+: Improving 3D Reconstructions with Single-Step Diffusion Models*. [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/5d599177-dda4-48f2-91a7-b5de0449e570)
9.  Wang, Z., et al. (2024). *Diffusion Models in 3D Vision: A Survey*. [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/a77ae72a-e5f4-4bc4-9c0a-62b1d990be91)
10. Mildenhall, B., et al. (2020). *NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis*. ECCV 2020.
11. Kerbl, B., et al. (2023). *3D Gaussian Splatting for Real-Time Radiance Field Rendering*. ACM Transactions on Graphics.
12. Poole, B., et al. (2022). *DreamFusion: Text-to-3D using 2D Diffusion*. ICLR 2023.