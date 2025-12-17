# 基于扩散模型的视频生成技术综述（2022–2025）

## 引言

扩散模型因其在图像生成任务中展现出的高保真度、强多样性与可控性，自2022年起迅速成为视频生成领域的主流范式。相较于早期基于生成对抗网络（GAN）和自回归模型的方法，扩散模型通过迭代去噪过程能更有效地建模视频的时空复杂性。本文系统梳理2022至2025年间视频扩散模型的关键进展，从文本/图像条件生成、高效训练与推理、长视频与多镜头生成、以及可控编辑等维度，归纳代表性工作，并总结实验评价的共性结论与未来趋势。

## 方法分类与代表作

### 文本/图像到视频生成（Text/Image-to-Video）

**Stable Video Diffusion (SVD)** [blog.csdn.net](https://blog.csdn.net/jaysszhou/article/details/148198550) 解决了高质量视频数据稀缺问题，提出了一套系统化的三阶段数据策展与训练流程（图像预训练、视频预训练、高质量微调）。其核心是基于Latent Video Diffusion Model (Video-LDM)架构，利用大规模筛选后的视频数据集进行训练。实验证明，该方法在图像到视频和文本到视频任务上均达到当时最优性能，其学习到的强运动与3D先验还能通过LoRA微调实现多视角合成。

**GenTron** [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/44761) 致力于将扩散模型从主流的U-Net架构迁移至更具扩展性的Transformer架构（DiT）。工作将DiT从类别条件扩展到文本条件，并通过实证研究优化了条件注入机制；同时引入“无运动引导”策略来调节视频动态。在参数规模扩展至30亿后，其在人类评估中于视觉质量和文本对齐上均超越了SDXL，展示了DiT在视频生成中的巨大潜力。

**Seedance 1.0** [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/81777871-7686-4770-9c3c-e65e0b0e9d8f) 旨在平衡提示遵循、动作合理性和视觉质量三大核心挑战。其创新点包括：多源高质量数据整理、支持多镜头生成的联合训练范式、以及结合细粒度监督微调与视频专用多维奖励的强化学习（RLHF）。在NVIDIA L20上，该模型能在41.4秒内生成5秒1080p视频，展现出卓越的时空流畅性、结构稳定性及复杂多主体场景下的精准指令跟随能力。

### 高效训练与推理

**Tune-A-Video** [blog.csdn.net](https://blog.csdn.net/m0_51976564/article/details/141160223) 提出“One-Shot Video Tuning”范式，旨在以极低成本将强大的预训练图像扩散模型（如Stable Diffusion）适配到特定视频生成任务。其核心是引入稀疏时空注意力机制，仅让当前帧关注首帧和前一帧，并在微调时仅更新注意力块中的投影矩阵。该方法仅需一个（文本，视频）对进行微调，即可生成保留原始视频运动模式但内容被编辑的新视频，显著降低了个性化视频生成的门槛。

**Diffusion Adversarial Post-Training (APT)** [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/100355) 针对扩散模型迭代采样速度慢的问题，提出了一种对抗后训练框架以实现高质量的单步视频生成。该方法在预训练的扩散模型基础上，通过对抗训练学习一个单步生成器，并引入近似R1正则化以稳定训练。实验表明，其模型Seaweed-APT能在一个前向传播步骤内实时生成2秒、1280x720分辨率、24fps的视频，同时在单步图像生成上达到与SOTA方法相当的质量。

### 长视频与多镜头生成

**Long Context Tuning (LCT)** [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/05bd1ee3-1dd9-4da4-814c-fc692c94d168) 解决了现有单镜头视频模型无法生成多镜头连贯叙事视频的问题。LCT通过扩展预训练单镜头视频扩散模型的上下文窗口，将全注意力机制从单个镜头覆盖到整个多镜头场景，并引入交错3D位置嵌入和异步噪声策略。无需增加模型参数，LCT就能让模型学会场景级别的视觉和动态一致性，展现出组合生成和交互式镜头扩展等新兴能力。

**NUWA-XL** [blog.csdn.net](https://blog.csdn.net/wl1780852311/article/details/149169360) 采用“粗到细”的并行生成范式来应对长视频生成挑战。模型首先利用全局扩散模型生成关键帧，再通过局部扩散模型在关键帧之间进行插帧。该方法能够生成长达3376帧（数分钟）的卡通视频，为长时长、高一致性视频生成设立了新的基准，特别适用于动画制作等特定领域。

### 视频可控生成与编辑

**AnimateDiff** [blog.csdn.net](https://blog.csdn.net/wl1780852311/article/details/149169360) 为个性化视频动画生成提供了一个通用解决方案。其核心思想是将运动学习与外观生成解耦：在一个冻结的个性化文本到图像（T2I）模型上，附加一个可训练的轻量级“运动模块”来学习通用的运动动态。在推理时，只需替换T2I模型的权重，即可让任意个性化角色执行所学的动画动作，避免了为每个新角色重新训练整个视频模型的高昂成本。

**DragNUWA** [blog.csdn.net](https://blog.csdn.net/wl1780852311/article/details/149169360) 实现了对视频内容的细粒度、开放域轨迹控制。它同时引入文本（语义）、图像（空间）和用户绘制的轨迹（时间）三重条件，并提出了轨迹采样器（TS）来处理任意轨迹输入。通过多尺度融合模块和自适应训练策略，DragNUWA能生成沿指定轨迹运动且语义一致的视频，在可控视频生成方面迈出了重要一步。

## 实验与评价总结

当前视频生成领域的评价体系主要依赖两大类指标。图像层面指标（如FID、CLIPSIM）评估单帧质量和文本对齐度，而视频层面指标（如FVD、KVD）则通过I3D等3D网络提取的时空特征来衡量视频整体的动态真实性和分布相似性。然而，已有研究表明，这些自动指标与人类主观感知（如动作流畅性、物理合理性）的相关性有限，因此高质量工作普遍辅以大规模人工评估（A/B测试）。

共性实验结论包括：1）高质量、大规模、精细化标注的视频数据集是性能提升的关键瓶颈；2）将强大的2D图像先验（如通过图像预训练或联合训练）迁移到视频任务中，能显著提升生成内容的视觉保真度；3）对时空建模进行显式设计（如3D卷积、时空注意力、运动解耦）对于保证视频时序一致性至关重要；4）多阶段（级联）生成策略是平衡视频分辨率、时长和质量的有效途径。

## 趋势与挑战

基于对2025年前后最新工作的分析，视频扩散模型研究呈现以下趋势：
1.  **多模态与世界模型融合**：视频生成模型正与大型语言模型（LLM）和多模态大模型（MLLM）深度结合，如利用LLM进行动态场景规划（Dysen-VDM, VideoDirGPT）或构建视频知识图谱（VideoRAG），以增强对复杂语义和长期因果关系的理解能力。
2.  **极致效率与实时性**：研究焦点从单纯的生成质量转向效率-质量的帕累托最优。单步生成（如APT）、多阶段蒸馏（如Seedance 1.0）和高效架构设计（如Mamba-based模型）成为热点，目标是在消费级硬件上实现实时或近实时的高清视频生成。
3.  **物理一致性与可控性增强**：模型正从“看起来合理”向“物理上正确”演进，通过引入物理引擎信号、3D先验（如SVD）或更精细的控制接口（如轨迹、深度、姿态），以解决物体交互失真、运动不符合物理规律等问题，并支持工业级的高精度视频编辑与仿真。

## 结论

2022至2025年间，基于扩散模型的视频生成技术经历了从基础架构探索到性能与效率全面优化的快速发展。通过在数据、架构、训练策略和评价体系上的持续创新，研究者们已能生成在视觉质量、时序连贯性和指令遵循能力上均达到较高水平的视频。未来，该领域将更紧密地与世界模型、具身智能等前沿方向交叉，致力于构建能理解物理世界、具备长期规划能力且高效可控的通用视频生成系统。

## 参考文献

1.  Blattmann, A., et al. (2023). Stable video diffusion: Scaling latent video diffusion models to large datasets. *arXiv preprint arXiv:2311.15127*.
2.  Chen, S., et al. (2024). GenTron: Diffusion Transformers for Image and Video Generation. *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*.
3.  Gao, Y., et al. (2025). Seedance 1.0: Exploring the Boundaries of Video Generation Models. *arXiv preprint*.
4.  Wu, J. Z., et al. (2023). Tune-A-Video: One-shot tuning of image diffusion models for text-to-video generation. *Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV)*.
5.  Lin, S., et al. (2025). Diffusion Adversarial Post-Training for One-Step Video Generation. *arXiv preprint arXiv:2501.08316*.
6.  Guo, Y., et al. (2025). Long Context Tuning for Video Generation. *arXiv preprint*.
7.  Zhang, L., et al. (2025). 基于生成式人工智能的图像视频生成方法综述及展望. *计算机辅助设计与图形学学报*.
8.  Chen, H., et al. (2024). A Survey on Video Diffusion Models. *ACM Computing Surveys (CSUR)*.
9.  Guo, Y., et al. (2025). Long Context Tuning for Video Generation. *智源社区论文*.
10. Wang, J., et al. (2025). SeedVR: Seeding Infinity in Diffusion Transformer Towards Generic Video Restoration. *智源社区论文*.
11. Ren, X., et al. (2025). VideoRAG: Retrieval-Augmented Generation with Extreme Long-Context Videos. *arXiv preprint arXiv:2502.01549*.