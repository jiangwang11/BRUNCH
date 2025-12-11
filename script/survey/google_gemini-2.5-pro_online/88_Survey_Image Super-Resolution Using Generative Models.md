好的，作为一名严谨的科研助手，我将基于提供的真实网络搜索结果，生成一篇关于“使用生成模型的图像超分辨率”的中文学术综述。

***

### **基于生成模型的图像超分辨率研究综述 (2022–2025)**

### **引言**

单图像超分辨率（Single Image Super-Resolution, SISR）作为计算机视觉中的一个基础且关键的任务，旨在从单张低分辨率（LR）图像中恢复出具有丰富细节的高分辨率（HR）图像 [image.hanspub.org](https://image.hanspub.org/Html/19-1543134_81938.htm)。早期方法以插值和传统重建为主，随着深度学习的发展，基于卷积神经网络（CNN）的模型通过端到端学习取得了显著进步。然而，这些方法大多采用L1或L2等像素级损失函数进行优化，虽然在峰值信噪比（PSNR）等失真度指标上表现优异，但生成的图像往往存在过度平滑的问题，缺乏真实感和高频纹理细节，与人类的主观感知存在差距 [blog.csdn.net](https://blog.csdn.net/mycfjmx/article/details/128208831)。

为了解决这一问题，研究者们转向了生成模型，特别是生成对抗网络（GAN）和去噪扩散概率模型（DDPM），它们在图像生成任务中展现了强大的能力。这些模型通过学习真实图像的数据分布，能够生成在感知质量上更优、纹理更逼真的结果，极大地推动了SISR技术的发展。本综述将聚焦于2022至2025年间，基于生成模型的SISR领域的代表性工作，系统梳理其方法分类、核心进展与挑战，并展望未来的研究趋势。

### **方法分类与代表作**

近年来，基于生成模型的SISR方法主要可以分为两大主流技术路线：基于生成对抗网络（GAN）的方法和基于扩散模型（Diffusion Model）的方法。此外，一个显著的新兴趋势是融合大规模预训练模型先验的方法。

#### **2.1 基于生成对抗网络 (GAN) 的方法**

GAN通过生成器与判别器的对抗训练，使生成器学习真实HR图像的分布，从而在SISR任务中生成锐利且细节丰富的纹理。尽管GAN能够显著提升感知质量，但其训练过程的不稳定性以及可能产生的伪影一直是研究的挑战 [blog.csdn.net](https://blog.csdn.net/mycfjmx/article/details/128208831)。

*   **HSR-GAN (2022)**
    该研究针对现有GAN模型在单一尺度提取特征且监督信息不足、易产生伪影的问题。HSR-GAN (Hierarchical Generative Adversarial Networks) 提出了一种分层架构，其核心是分层特征提取模块(HFEM)和分层引导重建模块(HGRM)。HFEM负责在多个尺度上提取特征，以同时关注局部纹理和全局语义；HGRM则通过引入中间监督，以渐进方式重建图像。实验表明，这种分层设计能有效恢复更自然的结构纹理，在五个常用数据集上，其结果在视觉质量和定量指标上均优于当时的主流方法 [fuxi.163.com](https://fuxi.163.com/database/437)。

*   **SROOE (2023)**
    该工作解决了传统感知驱动SISR方法中，固定组合的损失函数难以适应图像不同区域内容多样性的问题。SROOE (Perception-Oriented SISR using Optimal Objective Estimation) 框架包含一个预测模型和一个生成模型。预测模型首先为输入的LR图像推断出一个“最优目标图”，该图指导生成模型在不同区域应用不同的损失组合。这种对目标函数的区域自适应生成策略，使得模型能够更精细地平衡失真与感知。实验结果显示，SROOE在LPIPS、DISTS等感知度量上超越了其他先进的感知驱动SR方法，证明了其在生成合理视觉结果方面的优越性 [blog.csdn.net](https://blog.csdn.net/qq_41771998/article/details/131250877)。

#### **2.2 基于扩散模型 (Diffusion Model) 的方法**

扩散模型通过学习一个逐步去噪的过程来生成图像，相比GAN，其训练更稳定，生成图像的保真度和多样性更高。该方向的初期挑战主要在于推理速度较慢和在复杂、未知退化场景下的应用。

*   **SR3+ (2023)**
    该研究旨在提升扩散模型在真实世界盲超分（Blind SR）任务中的鲁棒性，此前扩散模型在该任务上落后于顶尖的GAN模型。为此，研究者提出了SR3+，一个专为盲超分设计的扩散模型。其核心策略是将自监督训练与训练和测试阶段的噪声条件增强相结合，使模型能够适应未知的、多样的图像退化。实验证明，SR3+的性能显著优于其基线模型SR3，并在相同数据上训练时，表现优于著名的GAN模型Real-ESRGAN，展示了扩散模型在处理真实世界复杂退化方面的巨大潜力 [blog.csdn.net](https://blog.csdn.net/qq_41771998/article/details/131250877)。

*   **IDM (2023)**
    传统SR方法通常只能处理固定的整数倍放大，限制了其应用灵活性。IDM（Implicit Diffusion Models for Continuous Super-Resolution）通过将隐式神经表示（Implicit Neural Representation）与扩散模型结合，构建了一个统一的端到端框架。该方法设计了一种尺度自适应调节机制，使模型能够学习连续的分辨率表示。实验证实，IDM能够在任意（包括非整数）放大倍数下实现高保真度的超分辨率重建，在连续超分辨率任务上展现了卓越的性能和灵活性 [blog.csdn.net](https://blog.csdn.net/qq_41771998/article/details/131250877)。

*   **SSDM-SR (2025)**
    该工作解决了有监督SR方法严重依赖大规模成对数据集，且难以泛化到未知退化类型图像的问题。SSDM-SR（Self-supervised Diffusion Model for SISR）提出了一种自监督方案，它仅利用待处理的单张LR图像自身的信息。通过从该图像中提取图块来训练一个微型的、图像专属的扩散模型，从而学习其内部的统计信息分布。实验表明，这种方法无需外部数据集即可适应不同输入，在标准和未知退化数据集上，其失真度和感知质量均超越了当时的有监督和无监督方法 [signal.ejournal.org.cn](https://signal.ejournal.org.cn/article/doi/10.12466/xhcl.2025.02.014?viewType=HTML)。

#### **2.3 融合大规模预训练先验的方法**

这一新兴方向通过利用大型文本-图像生成模型（如Stable Diffusion）强大的生成先验知识，将SISR任务从像素级重建提升到语义级修复。

*   **SUPIR (2024)**
    该研究旨在利用生成先验和模型缩放（Model Scaling）的力量来解决当前SISR模型对复杂真实世界语义理解有限的问题。SUPIR (Scaling-UP Image Restoration) 借助在两千万级别的图文对上预训练的多模态大模型，实现了照片级的图像修复。它创新地引入了文本提示来指导修复过程，并开发了负质量提示和修复引导采样等方法来平衡重建的保真度与感知质量。实验证明，SUPIR不仅取得了出色的修复效果，还开启了通过文本提示操控修复结果的新范式，是迈向智能、可控图像修复的重要一步 [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/db6ed53d-b000-42f5-b2e0-fbbdea3e2a6b)。

### **实验与评价总结**

*   **评价指标的权衡**：基于生成模型的SISR研究普遍证实了**感知-失真权衡**（Perception-Distortion Trade-off）的存在。相比于优化PSNR/SSIM的传统方法，GAN和扩散模型通常会在这些失真度指标上有所牺牲，但在LPIPS、DISTS和人类主观评分（MOS）等感知度量上取得显著优势 [blog.csdn.net](https://blog.csdn.net/mycfjmx/article/details/128208831)。
*   **数据集与任务设定**：虽然DIV2K、Flickr2K等标准数据集仍被广泛用于训练和评估，但研究重点正逐渐转向更具挑战性的真实世界场景。盲超分辨率和零样本（Zero-shot）超分辨率成为检验模型泛化能力和实用性的重要标准，RealSR等真实世界数据集的重要性日益凸显。
*   **共性结论**：GAN-based方法在生成逼真纹理方面是先驱，但需要精巧的网络结构（如HSR-GAN）和损失函数设计（如SROOE）来抑制伪影。扩散模型作为后起之秀，在训练稳定性和生成保真度上更具优势，其主要挑战——推理效率，也正在通过两阶段方法（如C2F）等得到缓解 [www.arocmag.cn](https://www.arocmag.cn/language?lang=cn&returnUrl=%2Fabs%2F2024.10.0438)。而融合大型模型先验（如SUPIR）的方法，则将任务的上限提升到了语义理解和内容创作的层面。

### **趋势与挑战**

展望2025年前后的发展，基于生成模型的图像超分辨率研究呈现出以下几个明确的趋势与挑战：

1.  **大规模先验与多模态融合**：利用大型文本-图像模型（如Diffusion Transformer、Sora）的先验知识将成为主流。这不仅能提供高质量的纹理和结构先验，还能通过文本、涂鸦甚至声音等多模态输入实现对修复过程的精细控制。其核心挑战在于如何在保持对原始LR图像内容忠实度的同时，有效利用大模型的“想象力”来修复严重退化的内容，避免“无中生有”的幻觉 [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/db6ed53d-b000-42f5-b2e0-fbbdea3e2a6b)。

2.  **高效推理与实时化部署**：扩散模型的高计算成本是其走向实际应用（尤其是在移动端和边缘设备）的最大障碍。未来的研究将重点关注模型压缩与加速技术，如知识蒸馏（将大型扩散模型的能力提炼到轻量级网络）、量化、剪枝以及开发更高效的采样算法 [blog.csdn.net](https://blog.csdn.net/mycfjmx/article/details/128208831)。实现与GAN相当甚至更快的推理速度，是扩散模型能否全面取代GAN的关键。

3.  **统一的真实世界退化建模**：真实世界的图像退化是复杂、混合且未知的。未来的研究将致力于构建能够处理任意复杂退化的统一模型，即真正的“盲超分”。这需要模型具备解耦和估计多种退化（如模糊、噪声、压缩伪影）的能力，或者通过自监督/元学习等方式，快速适应特定图像的退化特征 [image.hanspub.org](https://image.hanspub.org/Html/19-1543134_81938.htm)。同时，结合任意尺度重建能力，形成一个灵活、通用的SISR解决方案，是该领域的终极目标之一。

### **结论**

在2022至2025年间，基于生成模型的图像超分辨率研究取得了飞跃式发展。研究范式已从追求像素级精度的失真优化，转向了更符合人类视觉感知的质量优化。生成对抗网络（GAN）在提升感知质量方面扮演了开创性角色，而扩散模型则以其训练稳定性和更高的生成保真度成为当前的研究热点。更重要的是，融合大规模预训练模型先验的方法正引领SISR进入一个更加智能和可控的新时代。未来，该领域将朝着更高效、更鲁棒、更智能的方向持续演进，以满足日益增长的现实世界应用需求。

### **参考文献**

[1] 陈伟民, 马宇晴, 刘祥龙, 等. Hierarchical Generative Adversarial Networks for Single Image Super-Resolution. 网易伏羲 [fuxi.163.com](https://fuxi.163.com/database/437).
[2] 王睿琪. 图像超分辨率重建综述. 计算机科学与应用, 2024. [image.hanspub.org](https://image.hanspub.org/Html/19-1543134_81938.htm).
[3] qq_41771998 (博主). CVPR 2023 | 图像超分，结合扩散模型/GAN/部署优化. CSDN博客 [blog.csdn.net](https://blog.csdn.net/qq_41771998/article/details/131250877).
[4] Yu, F., Gu, J., Li, Z., et al. Scaling Up to Excellence: Practicing Model Scaling for Photo-Realistic Image Restoration In the Wild. 2024. [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/db6ed53d-b000-42f5-b2e0-fbbdea3e2a6b).
[5] 谢源远, 周非, 周志远, 等. 基于预训练扩散模型的两阶段高分辨率图像复原方法. 计算机应用研究, 2025. [www.arocmag.cn](https://www.arocmag.cn/language?lang=cn&returnUrl=%2Fabs%2F2024.10.0438).
[6] 牛阿茜, 孙瑾秋, 朱宇, 等. 用于单帧图像超分辨重建的自监督图像扩散模型. 信号处理, 2025. [signal.ejournal.org.cn](https://signal.ejournal.org.cn/article/doi/10.12466/xhcl.2025.02.014?viewType=HTML).
[7] mycfjmx (博主). SISR综述：From Beginner to Master: A Survey for Deep Learning-based Single-Image Super-Resolution. CSDN博客 [blog.csdn.net](https://blog.csdn.net/mycfjmx/article/details/128208831).
[8] Kim, S., et al. Perception-Oriented Single Image Super-Resolution using Optimal Objective Estimation. CVPR, 2023.
[9] Ree, S., et al. Implicit Diffusion Models for Continuous Super-Resolution. CVPR, 2023.
[10] Saharia, C., et al. Image Super-Resolution via Iterative Refinement. (SR3, a foundational work for diffusion-based SR, referenced as context for SR3+).
[11] 韦炎炎, 毛天一, 李柏昂, 等. 视觉模型及多模态大模型推进图像复原增强研究进展. 中国图象图形学报, 2025. [www.cjig.cn](https://www.cjig.cn/zh/article/doi/10.11834/jig.240436/).
[12] Zhang, X., et al. Efficient Long-Range Attention Network for Image Super-resolution. ECCV, 2022. [blog.csdn.net](https://blog.csdn.net/BigerBang/article/details/134991611).
[13] Dong, C., Loy, C. C., He, K., & Tang, X. Learning a Deep Convolutional Network for Image Super-Resolution. ECCV, 2014.