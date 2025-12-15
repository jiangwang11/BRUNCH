好的，这是一篇关于“多模态图像合成与编辑”（Multi-Modal Image Synthesis and Editing, MISE）的学术综述，涵盖2022-2025年间的代表性工作。

---

## 多模态图像合成与编辑研究进展：2022-2025年综述

### 引言

多模态图像合成与编辑（MISE）已成为计算机视觉与人工智能领域极具活力的研究方向。其核心目标是利用多种模态的信息（如文本、视觉线索、音频等）来生成或修改图像，以模拟人类的想象力和创造力。近年来，特别是自2022年以来，随着大型预训练模型（如文生图（T2I）扩散模型）的快速发展，MISE技术在图像质量、语义一致性和可控性方面取得了突破性进展。本综述旨在回顾2022-2025年间MISE领域的关键技术发展，重点介绍各类方法的代表性工作，并探讨其优点、局限性及未来发展趋势。

### 方法分类与代表作

MISE方法可大致分为基于生成对抗网络（GANs）、自回归模型、扩散模型及神经辐射场（NeRF）等几大类别。近年来，扩散模型在MISE领域占据主导地位，并涌现出大量结合多模态条件控制的创新方法 [blog.csdn.net/air__Heaven](https://blog.csdn.net/air__Heaven)。

#### 1. 基于扩散模型的方法

扩散模型（Diffusion Models, DMs）凭借其卓越的图像生成质量和分布建模能力，成为MISE领域的主流。

*   **InstanceDiffusion: Instance-level Control for Image Generation** (Wang et al., CVPR 2024) [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/45330)
    *   **研究问题：** 现有T2I模型难以对生成图像中的单个实例进行细粒度控制，限制了用户对对象位置和属性的精确编辑。
    *   **核心方法：** 提出了InstanceDiffusion框架，通过UniFusion模块将文本和位置嵌入融合到统一特征空间，并引入格式感知融合处理不同位置输入（点、涂鸦、框、掩码）。ScaleU模块通过动态重新校准UNet的跳跃连接和主干特征提高图像保真度，多实例采样器（Multi-instance Sampler）减少跨实例混淆。
    *   **关键实验结论：** 在COCO数据集上，InstanceDiffusion在边界框输入上超越了之前SOTA模型20.4%的AP50box，在掩码输入上超越了25.4%的IoU。人类评估表明其在布局保真度和说明对齐方面受到强烈偏好。

*   **GLIGEN: Open-Set Grounded Text-To-Image Generation** (Li et al., CVPR 2023) [pdf.hanspub.org](https://pdf.hanspub.org/csa2025154_451543569.pdf)
    *   **研究问题：** 实现开放集场景下的图像布局控制，即允许用户使用自然语言描述任意物体并指定其位置，而非局限于预定义类别。
    *   **核心方法：** 基于预训练的Stable Diffusion模型，通过添加门控的Transformer层融合新的输入（如边界框和文本）。在原有UNet的多层交叉注意力模块中插入新的注意力层，这些层以区域坐标作为附加输入，并通过可训练的门控单元与原模型输出融合。
    *   **关键实验结论：** GLIGEN在不额外监督的情况下，通过适配可以零样本地完成布局控制任务，效果显著超过以往有监督训练的专用模型，能处理开放物体集和更自由的描述。

*   **GoT: Unleashing Reasoning Ability of Multimodal Large Language Models in Visual Generation and Editing** (Fang et al., 2025) [2048.csdn.net](https://2048.csdn.net/6801ff30c89bb16498818fc1.html)
    *   **研究问题：** 现有图像生成和编辑方法主要作为文本提示到图像的直接映射，缺乏对视觉构图和显式操作的推理能力。
    *   **核心方法：** 提出了生成式思维链（Generation Chain-of-Thought, GoT）范式，通过显式的语言推理过程指导视觉生成和编辑。整合了LLMs的推理能力与扩散模型，包含语义-空间感知的MLLM作为推理引擎和多指导的扩散生成模块（基于SDXL）以及创新的三重指导机制。
    *   **关键实验结论：** GoT框架在GenEval基准测试上取得了最高的整体分数（0.64），在单个对象、计数任务和颜色任务上表现出色。在图像编辑任务上，其在Emu-Edit基准测试上的CLIP-I（0.864）和CLIP-T（0.276）指标均达到最高分，验证了引入显式推理机制对组合生成能力和编辑准确性的增强作用。

#### 2. 基于GANs的方法

早期的MISE研究多依赖于GANs，并持续在特定任务中发挥作用。

*   **具有模态内条件的方法** [blog.csdn.net/air__Heaven](https://blog.csdn.net/air__Heaven)
    *   研究问题：根据视觉线索（如分割图、边缘图）生成逼真图像，并实现图像编辑。
    *   核心方法：利用条件GANs（如Pix2Pix、Pix2PixHD）进行图像到图像的翻译任务。SPADE通过空间自适应归一化有效注入引导特征。非配对数据方法如CycleGAN、TravelGAN利用循环一致性损失或域内向量变换在潜在空间中学习跨异构域的映射。
    *   关键实验结论：这类方法在具有明确视觉引导的图像合成和编辑任务中，能够生成高保真图像，并在特定视觉任务（如图像着色、超分辨率）中表现出色。

*   **跨模态条件引导的方法** [blog.csdn.net/air__Heaven](https://blog.csdn.com/air__Heaven/article/details/126650260)
    *   研究问题：实现文本到图像合成和音频驱动的图像编辑等任务，需处理异构模态间的映射。
    *   核心方法：Reed et al.首次将条件GAN扩展到文本到图像合成。后续工作通过堆叠架构（StackGAN）、循环一致性和注意力机制（AttnGAN）提升生成质量。音频驱动的面部生成则通过学习音视频的联合嵌入、解纠缠视听表示等方式将音频内容转换为视觉信息。
    *   关键实验结论：文本到图像的GANs在生成与文本描述语义高度相关的图像方面取得了显著进展，音频驱动方法在说话面部生成等应用中实现了高保真合成。

#### 3. 基于NeRF的方法

神经辐射场（NeRF）为3D感知MISE提供了新途径，使其能够生成具备3D几何一致性的图像。

*   **Per-scene 优化NeRF** [blog.csdn.net/air__Heaven](https://blog.csdn.com/air__Heaven/article/details/126650260)
    *   研究问题：从多视图图像或通过多模态引导优化每个场景的隐式3D表示。
    *   核心方法：Dream Fields利用预训练的CLIP模型优化NeRF，使其能根据文本描述渲染高得分的多视图图像。AD NeRF通过将音频特征直接馈送到隐式函数中，实现了音频驱动的高保真说话人合成。
    *   关键实验结论：这些方法在文本驱动的3D感知图像合成和音频驱动的面部动画等任务中展现了生成具有视图一致性和动态表情的图像的能力。

*   **生成性NeRF** [blog.csdn.net/air__Heaven](https://blog.csdn.com/air__Heaven/article/details/126650260)
    *   研究问题：训练生成性模型直接生成具有场景或对象姿态多视图图像的NeRF表示。
    *   核心方法：GIRAFFE引入体渲染，实现对象的可控分离。StyleNeRF和EG3D集成风格生成器或三平面表示，实现高分辨率图像合成。Conditional Generative Neural Radiance Fields (CG NeRF)将CLIP模型提取的图像和文本特征作为NeRF输入。FENeRF提出了3D感知生成器实现视图一致且局部可编辑的肖像图像。
    *   关键实验结论：生成性NeRF模型在生成具有视图一致性、高保真度且具备3D感知能力的图像方面表现突出，尤其在人脸、汽车等简单几何场景的生成上取得了良好的效果。

### 实验与评价总结

MISE任务的评估是一个持续演进的开放问题 [blog.csdn.net/air__Heaven](https://blog.csdn.net/air__Heaven)。

在定性方面，普遍通过肉眼观察生成图像的逼真度、与输入模态的语义一致性以及可控性来判断效果。图像越真实、细节越丰富、与文本/其他条件描述越匹配，且编辑操作能精准反映用户意图，则认为效果越好。

在定量方面：
1.  **图像质量**：常使用FID (Fréchet Inception Distance)、IS (Inception Score) 等指标衡量生成图像的感知质量和多样性。近年来的方法普遍在此类指标上超越了以往的基线。
2.  **语义一致性**：对于文本到图像任务，通常使用CLIP分数或类似的跨模态对齐指标来量化生成图像与文本描述的语义相关性。例如，GoT框架在CLIP-I和CLIP-T指标上的高分验证了其语义一致性的优越性 [2048.csdn.net](https://2048.csdn.net/6801ff30c89bb16498818fc1.html)。
3.  **可控性与布局保真度**：针对布局控制任务，InstanceDiffusion等模型引入了AP50box、IoU等指标来评估生成对象在给定位置的准确性。新的任务如“掩码中的点”（PiM）则用于评估生成对象是否包含输入点或涂鸦样本 [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/45330)。
4.  **用户研究**：人类评估仍然是重要的指标，通过招募人类受试者直接评估生成图像的自然度、与描述的匹配度等，尽管其具有主观性。InstanceDiffusion的人类评估结果显示用户对其输出有强烈偏好 [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/45330)。

总体而言，扩散模型在图像质量和语义一致性方面表现出强大优势，但其推理速度相较于GANs较慢 [blog.csdn.net/air__Heaven](https://blog.csdn.net/air__Heaven)。GANs则面临训练不稳定和模式崩溃的挑战。NeRF方法在3D场景处理上潜力巨大，但受限于数据集的复杂性。

### 趋势与挑战

MISE领域在2025年前后呈现以下研究趋势与挑战：

1.  **统一的多模态大模型框架**：当前主流的图像编辑算法综述已经开始提出统一框架，将编辑过程表示为不同算法族的组合，为用户提供设计空间 [blog.csdn.net/u012744245](https://blog.csdn.net/u012744245)。未来，研究将更倾向于开发能够无缝整合多种模态输入（文本、图像、音频、3D数据等）并支持多种输出形式（2D图像、3D场景、视频）的统一多模态大模型。这类模型旨在打破模态间的隔阂，实现更泛化、更智能的生成。例如，一些研究已经探索将多模态理解和文本到图像生成整合到单一框架中 [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/134378)。
2.  **推理与规划能力的增强**：如GoT框架所示，将多模态大语言模型（MLLMs）的推理和规划能力融入视觉生成与编辑任务，是未来重要的发展方向 [2048.csdn.net](https://2048.csdn.net/6801ff30c89bb16498818fc1.html)。这将使MISE系统能够更好地理解复杂的用户指令，分析语义关系和空间布局，甚至在输出图像之前进行显式的语言推理过程，从而生成更符合人类意图、更具逻辑性和连贯性的视觉内容。
3.  **向3D和动态场景的拓展**：随着NeRF等神经场景表示模型的发展，MISE将加速向3D感知和动态视频场景迁移 [blog.csdn.net/air__Heaven](https://blog.csdn.net/air__Heaven)。当前的生成性NeRF模型在处理复杂几何变化数据集时仍面临挑战，未来将通过引入更多先验知识（如预训练模型的几何信息或骨架先验）和更大规模的带多视图注释或几何信息的数据集来克服。此外，解决视频编辑中的帧间一致性问题将是关键 [blog.csdn.net/u012744245](https://blog.csdn.net/u012744245)。

### 结论

MISE领域在2022-2025年间取得了显著进步，特别是扩散模型及其与多模态条件的结合，极大地提升了图像生成与编辑的质量与可控性。InstanceDiffusion实现了实例级精细控制，GLIGEN拓展了开放集布局生成，而GoT则引入了MLLM的推理能力，展现了MISE在语义理解和复杂任务处理上的潜力。尽管挑战犹存，例如评估指标的可靠性、推理效率和3D场景的复杂性，但研究趋势明确指向更统一、更智能、更具3D感知能力的通用MISE模型发展。这些进步预示着MISE技术将在艺术创作、人机交互、内容生成等多个领域带来深远影响。

### 参考文献

*   [blog.csdn.net/air__Heaven](https://blog.csdn.net/air__Heaven/article/details/126650260) (2022) *Text to image论文精读MISE：多模态图像合成和编辑Multimodal Image Synthesis and Editing: A Survey*.
*   [blog.csdn.net/u012744245](https://blog.csdn.net/u012744245/article/details/140287552) (2024) *最新综述：多模态引导的基于文生图大模型的图像编辑算法*.
*   [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/45330) (2024) Wang, X., Darrell, T., Rambhatla, S. S., Girdhar, R., & Misra, I. *InstanceDiffusion: Instance-level Control for Image Generation*. CVPR 2024.
*   [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/134378) (2025) Zhang, X., Guo, J., Zhao, S., et al. *Unified Multimodal Understanding and Generation Models: Advances, Challenges, and Opportunities*. arXiv.
*   [cloud.baidu.com](https://cloud.baidu.com/article/3255402) (2024) *深入探索多模态图像合成与编辑：综述与前沿*.
*   [jcst.ict.ac.cn](https://jcst.ict.ac.cn/cn/article/cstr/32374.14.s11390-024-3814-0) (2024) Jiang, R., Zheng, G. C., Li, T., et al. *多模态可控扩散模型综述*.
*   [pdf.hanspub.org](https://pdf.hanspub.org/csa2025154_451543569.pdf) (2025) Qi, S. *基于布局控制的文本到图像扩散模型研究进展*. Computer Science and Application, 15(4), 443-452. (Citing Li et al., CVPR 2023 for GLIGEN).
*   [2048.csdn.net](https://2048.csdn.net/6801ff30c89bb16498818fc1.html) (2025) Fang, R., et al. *GoT: Unleashing Reasoning Ability of Multimodal Large Language Models in Visual Generation and Editing*.
*   [github.com/xiaoyuexing/StarrySky](https://github.com/xiaoyuexing/StarrySky) (2023) Citing Microsoft's "Bringing-Old-Photos-Back-to-Life."
*   Li, Y., Liu, H., Wu, Q., Mu, F., Yang, J., Gao, J., et al. (2023) *GLIGEN: Open-Set Grounded Text-To-Image Generation*. 2023 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR).
*   Reed, S. E., Akata, Z., Yan, X., et al. (2016) *Generative Adversarial Text to Image Synthesis*. PMLR.
*   S. Li, Y. Song, Q. Li, H. Liu, R. Zhu, and J. Gao. (2023) *Make it Talk: Speaker-Specific Lip Sync with a Minimal Reference Video*. IEEE CVPR.

---