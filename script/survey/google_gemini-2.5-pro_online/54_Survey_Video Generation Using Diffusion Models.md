好的，作为一名严谨的科研助手，我将基于提供的真实网络搜索结果，为您生成一篇关于“使用扩散模型的视频生成”的学术综述。

***

### **基于扩散模型的视频生成技术发展综述 (2022-2025)**

**摘要：** 近年来，扩散模型（Diffusion Models）已成为视频生成领域的主流范式，展现出前所未有的生成质量与可控性。本综述旨在系统梳理 2022 年至 2025 年间基于扩散模型的视频生成技术的代表性研究进展。首先，引言部分概述了该领域的核心挑战与扩散模型的兴起。其次，对核心方法进行分类，涵盖架构演进、长视频与时序连贯性、可控生成及效率提升四个方面，并剖析了每个方向下的关键论文。随后，对现有工作的实验设置与评价指标进行归纳总结。最后，基于当前研究前沿，对未来的主要趋势与尚存挑战进行展望。

### 1. 引言

视频生成旨在合成与真实世界在视觉、动态和语义上均保持一致的视频序列，是计算机视觉领域一项极具挑战性的任务。传统的生成对抗网络（GANs）和变分自编码器（VAEs）在视频生成中面临训练不稳定、模式坍塌以及时序建模能力不足等问题。自 2020 年以来，扩散模型凭借其稳定的训练过程和卓越的样本质量，在图像生成领域取得突破，并迅速被引入视频生成任务，成为当前最先进的技术路线 [www.jcad.cn](https://www.jcad.cn/cn/article/doi/10.3724/SP.J.1089.2024-00281)。

然而，将扩散模型从图像域扩展到视频域并非易事，核心挑战包括：(1) **高维数据处理**：视频数据在时空维度上的高复杂性带来了巨大的计算与内存开销；(2) **时序连贯性**：需确保生成视频在帧间的内容、动态及身份信息上保持一致；(3) **可控性**：如何精确遵循用户输入（如文本、图像、相机轨迹）来控制生成内容；(4) **生成效率**：扩散模型固有的迭代采样过程导致推理速度缓慢，限制了其实际应用。本综述将围绕以上挑战，聚焦于 2022-2025 年的代表性工作，系统阐述学术界如何逐步克服这些难题。

### 2. 方法分类与代表作

#### 2.1 架构演进与基础模型

视频扩散模型的骨干网络经历了从基于卷积的 U-Net 到 Transformer 的演进，后者展现出更强的可扩展性与全局建模能力。

*   **Stable Video Diffusion (SVD)** [blog.csdn.net](https://blog.csdn.net/jaysszhou/article/details/148198550)
    *   **研究问题**：如何有效地将静态图像扩散模型扩展至视频领域，并验证大规模数据筛选的关键作用。
    *   **核心方法**：该工作在预训练的潜在扩散模型（Latent Diffusion Model）基础上，通过插入时序卷积与注意力层进行改造。其核心贡献是提出了一套系统的三阶段训练策略：大规模图像预训练、大规模视频数据预训练、以及在少量高质量视频上的微调。研究强调了数据整理流程（如使用光流排除静态视频）对模型性能的决定性影响。
    *   **关键结论**：实验证明，通过精细的数据筛选和分阶段训练，即使是简单的架构也能生成高质量的图像到视频（Image-to-Video）内容。该模型在用户偏好评估中超越了当时主流的开源和闭源模型，证明了数据质量优先于模型复杂度的重要性。

*   **GenTron** [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/44761)
    *   **研究问题**：探索基于 Transformer 架构的扩散模型（Diffusion Transformers, DiT）在文本到视频生成任务中的潜力与可扩展性。
    *   **核心方法**：GenTron 将图像生成领域的 DiT 架构扩展到视频生成，系统研究了文本条件注入机制。模型通过扩展参数规模（从 9 亿到超过 30 亿），验证了 Transformer 架构在视频生成领域的优越可扩展性。此外，该工作还为视频任务引入了新颖的“无运动引导”（motion-free guidance）来提升视频质量。
    *   **关键结论**：与基于 U-Net 的代表性模型 SDXL 进行的人类评估对比显示，GenTron 在视觉质量上获得了 51.1% 的胜率。这表明 DiT 架构在捕捉全局时空依赖和提升视觉保真度方面优于传统的 U-Net 结构，尤其在组合式生成任务中表现突出。

*   **Wan** [blog.csdn.net](https://blog.csdn.net/qq_44681809/article/details/146803878)
    *   **研究问题**：如何构建一个开放且先进的大规模视频基础模型，统一支持文本、图像、音频等多种模态的生成与编辑任务。
    *   **核心方法**：Wan 基于 DiT 架构和 Flow Matching 框架，并设计了高效的时空变分自编码器（Spatio-temporal VAE）来提升动态建模能力。模型在超过万亿级别的图文与视频数据上进行训练，并系统性地集成了包括图像到视频、指令编辑、个性化生成在内的八项下游任务。其训练流程采用了多维并行策略（如 FSDP、上下文并行）和激活迁移等技术来应对大规模训练的挑战。
    *   **关键结论**：Wan-14B 模型在多个公开榜单（如 VBench）上取得了 SOTA 性能，证明了其在动态质量、图像质量和指令遵循能力上的全面优势。该工作不仅展示了 DiT 架构的强大潜力，也为构建统一多模态生成系统提供了工程实践范本。

#### 2.2 长视频与时序连贯性

生成具有叙事逻辑的多镜头长视频是当前的研究热点。研究者们通过扩展上下文窗口、改进位置编码等方式来增强模型对长时序依赖的建模能力。

*   **Long Context Tuning (LCT)** [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/05bd1ee3-1dd9-4da4-814c-fc692c94d168)
    *   **研究问题**：如何使预训练的单镜头视频生成模型具备生成连贯多镜头场景的能力，而无需从头训练。
    *   **核心方法**：提出一种名为“长上下文调优”（LCT）的训练范式，将模型的全注意力机制从单个镜头扩展至覆盖整个场景的多个镜头。通过引入交错的 3D 位置嵌入和异步噪声策略，模型可以直接从数据中学习场景级别的连贯性。经过 LCT 调优后，模型可支持联合生成或高效的自回归式镜头生成。
    *   **关键结论**：实验表明，经过 LCT 调优的单镜头模型不仅能生成视觉和动态上一致的多镜头视频，还涌现出组合生成和交互式镜头扩展等新能力，为实用的视觉内容创作铺平了道路。

*   **Seedance 1.0** [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/81777871-7686-4770-9c3c-e65e0b0e9d8f)
    *   **研究问题**：如何在单一模型中同时平衡提示遵循、运动合理性与视觉质量，并原生支持多镜头叙事生成。
    *   **核心方法**：该模型在 DiT 架构中引入了多模态旋转位置编码（MM-RoPE），以原生支持多镜头视频生成。在训练阶段，模型联合学习文本到视频和图像到视频任务，并采用细粒度监督微调（SFT）和基于人类反馈的强化学习（RLHF）进行对齐。其数据管线通过精准的密集视频字幕来增强模型的叙事理解能力。
    *   **关键结论**：Seedance 1.0 能够从单个提示生成包含多个连续镜头、主体身份一致的视频。在公开基准测试中，其多镜头生成能力得到了验证，证明了其架构与训练策略在实现叙事连贯性方面的有效性 [blog.csdn.net](https://blog.csdn.net/m0_66899341/article/details/148678280)。

#### 2.3 可控生成

为满足多样化的应用需求，视频生成模型的可控性日益重要，涵盖相机运动、主体姿态、3D 空间一致性等多个维度。

*   **3D空间先验驱动的相机轨迹可控视频扩散生成模型** [aas.net.cn](https://aas.net.cn/cn/article/doi/10.16383/j.aas.c250124?viewType=HTML)
    *   **研究问题**：现有相机可控的图像到视频生成方法难以维持 3D 空间结构的一致性，导致生成视频中物体形态在多视角下发生畸变。
    *   **核心方法**：该工作在训练和推理阶段均引入了显式的 3D 空间先验。训练时，设计了“视角形变映射注入”（Warp-Injection）方法，将具备空间一致性的参考帧序列作为条件嵌入模型。推理时，通过“初始噪声空间几何校正”（Warp-Init）和“视角形变先验引导”（Warp-Guidance）策略，约束生成过程以符合 3D 一致性。
    *   **关键结论**：在 RealEstate10K 数据集上，该方法相比当时最优模型在 FVD 指标上取得 18.03 的显著优化，并将 3D 结构估计失败率（COLMAP error rate）从 19.8% 降低至 5.20%，有力证明了引入 3D 空间先验对维持结构一致性的关键作用。

*   **Human4DiT** [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/23809)
    *   **研究问题**：如何从单张图像生成高质量、时空一致且支持任意视角观看的人体视频。
    *   **核心方法**：提出一个级联的 4D 扩散 Transformer 架构，将注意力分解到视图、时间和空间维度，以有效建模 4D 空间。模型将人类身份、相机参数和时间信号等条件精确地注入到对应的 Transformer 模块中。为了训练该模型，团队构建了一个涵盖图像、视频、多视图数据和 4D 扫描的多样化数据集。
    *   **关键结论**：该方法能够合成逼真且一致的自由视角人体视频，克服了传统方法在处理复杂运动和视点变化时的局限性。这表明特定领域的 4D 建模是实现高保真、可控动态内容生成的有效途径。

#### 2.4 生成效率提升

为了克服扩散模型推理缓慢的瓶颈，学术界主要通过知识蒸馏等技术，将多步采样过程压缩至单步或少数几步，以实现实时或近实时生成。

*   **Diffusion Adversarial Post-Training (APT)** [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/100355)
    *   **研究问题**：现有的知识蒸馏方法在应用于视频单步生成时，存在显著的质量下降问题。
    *   **核心方法**：该研究提出了一种针对真实数据的对抗性后训练（APT）方法。在预训练的扩散模型基础上，APT 框架通过引入一个基于 DiT 的判别器进行对抗训练，以提升单步生成视频的真实感和细节。为了保证训练稳定性，模型架构和训练流程进行了多项改进，并引入了近似的 R1 正则化。
    *   **关键结论**：实验证明，经过 APT 训练的模型 Seaweed-APT 能够通过单次前向传播，实时生成 2 秒、720p、24fps 的视频。该方法在单步生成质量上达到了与多步采样相当的水平，验证了对抗性后训练在视频生成效率提升上的巨大潜力。

### 3. 实验与评价总结

*   **数据集**：早期工作多依赖于公开数据集，如 WebVid-10M、UCF-101 等。然而，近期（2023-2025年）的顶级模型，如 SVD、Wan、Seedance 1.0，均强调了构建大规模、高质量内部数据集的重要性 [blog.csdn.net](https://blog.csdn.net/jaysszhou/article/details/148198550)。这些数据集经过多阶段筛选、自动化标注（例如，使用 V-BLIP 和大型语言模型）和安全审查，以确保数据的高多样性、高美学价值和精确的文-视频对齐。对于特定任务，如相机控制，则使用如 RealEstate10K 等包含相机参数的数据集 [aas.net.cn](https://aas.net.cn/cn/article/doi/10.16383/j.aas.c250124?viewType=HTML)。

*   **评价指标**：
    1.  **客观指标**：最常用的指标是 **Fréchet Video Distance (FVD)** 和 **Fréchet Inception Distance (FID)**，用于衡量生成视频分布与真实视频分布在特征空间的距离，评估整体真实感和多样性。此外，**CLIPSIM** 用于评估文本-视频语义一致性。对于特定任务，如 3D 一致性，会使用 **COLMAP 重建错误率** 等指标 [aas.net.cn](https://aas.net.cn/cn/article/doi/10.16383/j.aas.c250124?viewType=HTML)。
    2.  **人类评估**：由于客观指标与人类感知存在差距，人类评估仍是金标准。通常采用成对比较（Pairwise Comparison）的方式，邀请评估者从提示遵循、视觉质量、运动合理性等多个维度对不同模型生成的视频进行投票，最终以胜率（Win Rate）作为评判依据 [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/44761)。

### 4. 趋势与挑战

基于 2024-2025 年的研究前沿，未来视频生成领域将呈现以下主要趋势：

1.  **迈向世界模型与物理一致性**：当前模型生成的视频虽然视觉逼真，但常违反物理常识（如物体穿模、动力学异常）。未来的研究将更加注重将物理规律和世界知识融入生成过程，使模型从“像素合成器”进化为具备初步推理能力的“世界模拟器”。这需要结合神经渲染、3D/4D 表征以及从大规模数据中隐式学习物理规则。

2.  **多模态统一与交互式生成**：大型基础模型正朝着统一处理多种模态（文本、图像、视频、音频、3D）的方向发展，如 Wan 模型已展现出初步能力 [blog.csdn.net](https://blog.csdn.net/qq_44681809/article/details/146803878)。下一阶段的重点将是实现实时、交互式的视频生成与编辑，用户可以像使用绘图软件一样，通过连续的指令和操作动态引导视频内容的演变，而非仅依赖于一次性的初始提示。

3.  **端到端长视频叙事生成**：尽管 LCT 等技术实现了多镜头拼接，但生成具有完整叙事结构（如起承转合、角色发展）的分钟级长视频仍是巨大挑战。未来的研究将探索层次化生成框架，从高级别的故事大纲或剧本生成关键场景描述，再由底层模型合成具体的视频镜头，并确保全局角色、场景和风格的一致性。

4.  **模型效率与端侧部署的权衡**：随着模型参数量突破百亿，高昂的训练和推理成本成为瓶颈。虽然知识蒸馏等技术显著提升了效率，但要在消费级硬件甚至移动端部署高质量视频生成模型，仍需在模型架构（如混合专家模型 MoE）、量化、硬件协同设计等方面取得根本性突破，在保持生成质量的同时极限压缩计算需求。

### 5. 结论

在 2022 年至 2025 年间，基于扩散模型的视频生成技术取得了飞跃式发展。研究者们通过改进网络架构（从 U-Net 到 DiT）、构建高质量大规模数据集、引入精细化的控制机制（如 3D 先验和人类反馈）以及发展高效的推理技术，显著提升了生成视频的质量、可控性和时序连贯性。尽管在物理真实性、长时叙事能力和部署效率方面仍面临挑战，但该领域正朝着构建更通用、更智能、更易用的世界模拟器的方向稳步前进，预示着其在内容创作、娱乐、教育和虚拟现实等领域拥有广阔的应用前景。

### 6. 参考文献

*   [1] Liu, J. Y., et al. (2025). 基于生成式人工智能的图像视频生成方法综述及展望. *小型微型计算机系统*. [www.jcad.cn](https://www.jcad.cn/cn/article/doi/10.3724/SP.J.1089.2024-00281)
*   [2] Blattmann, A., et al. (2023). Stable Video Diffusion: Scaling Latent Video Diffusion Models to Large Datasets. *arXiv preprint arXiv:2311.15127*. (as reviewed in [blog.csdn.net](https://blog.csdn.net/jaysszhou/article/details/148198550))
*   [3] Chen, S., et al. (2024). GenTron: Diffusion Transformers for Image and Video Generation. *CVPR 2024*. (as seen on [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/44761))
*   [4] Wan Team. (2025). Wan: Open and Advanced Large-Scale Video Generative Models. *arXiv preprint arXiv:2503.20314*. (as reviewed in [blog.csdn.net](https://blog.csdn.net/qq_44681809/article/details/146803878))
*   [5] Guo, Y., et al. (2025). Long Context Tuning for Video Generation. *arXiv preprint*. [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/05bd1ee3-1dd9-4da4-814c-fc692c94d168)
*   [6] Gao, Y., et al. (2025). Seedance 1.0: Exploring the Boundaries of Video Generation Models. *Technical Report*. [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/81777871-7686-4770-9c3c-e65e0b0e9d8f)
*   [7] Zhu, H. Z., et al. (2025). 3D空间先验驱动的相机轨迹可控视频扩散生成模型. *自动化学报*. [aas.net.cn](https://aas.net.cn/cn/article/doi/10.16383/j.aas.c250124?viewType=HTML)
*   [8] Shao, R., et al. (2024). Human4DiT: Free-view Human Video Generation with 4D Diffusion Transformer. *arXiv preprint arXiv:2405.17405*. (as seen on [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/23809))
*   [9] Lin, S., et al. (2025). Diffusion Adversarial Post-Training for One-Step Video Generation. *arXiv preprint arXiv:2501.08316*. [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/100355)
*   [10] Ho, J., et al. (2022). Imagen Video: High Definition Video Generation with Diffusion Models. *arXiv preprint arXiv:2210.02303*.
*   [11] Singer, U., et al. (2022). Make-A-Video: Text-to-Video Generation without Text-Video Data. *arXiv preprint arXiv:2209.14792*.
*   [12] Peebles, W., & Xie, S. (2023). Scalable Diffusion Models with Transformers. *ICCV 2023*. (as referenced by DiT-based models like GenTron and Wan)