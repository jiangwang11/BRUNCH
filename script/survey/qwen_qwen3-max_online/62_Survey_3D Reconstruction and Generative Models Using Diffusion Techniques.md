# 基于扩散技术的三维重建与生成模型研究综述（2022–2025）

## 引言

扩散模型（Diffusion Models）自2020年代初在图像生成领域取得突破后，迅速被引入三维视觉任务。相较于传统生成对抗网络（GANs）与变分自编码器（VAEs），扩散模型凭借其概率建模的稳定性、对高维数据分布的良好拟合能力，以及对不确定性的自然刻画，为三维重建（3D Reconstruction）与生成（3D Generation）提供了新范式。2022年以来，该方向研究呈现爆发式增长，涵盖点云、体素、神经辐射场（NeRF）、3D高斯点绘（3DGS）等多种表示形式。本文系统综述2022至2025年间该领域的代表性工作，按方法范式分类，分析其核心思想、技术路径与实验结论，并展望未来发展趋势。

## 方法分类与代表作

### 1. 基于隐空间扩散的3D生成

此类方法将3D对象编码至紧凑隐空间，在隐空间中进行扩散去噪，以提升生成效率与质量。

- **LION** (NeurIPS 2022) 针对点云生成质量与灵活性不足的问题，提出分层隐式点扩散模型。其将3D形状编码为全局隐向量与点结构隐空间的组合，分别训练两个扩散模型。实验证明，该方法在ShapeNet多个子集上达到SOTA，FID指标显著优于Point-E等基线，同时支持高质量的形状插值与条件生成 [zhuanzhi.ai](https://www.zhuanzhi.ai/paper/731cfc5d4536d93cf9f94aea445edfc5)。

- **DiT-3D** (NeurIPS 2023) 为解决U-Net在3D生成中的可扩展性瓶颈，首次将纯Transformer架构（DiT）应用于体素化点云生成。通过引入3D窗口注意力机制降低计算复杂度，并利用ImageNet预训练的2D DiT权重进行迁移。在ShapeNet上，其在保持高保真度的同时，模型规模可轻松扩展至数亿参数，性能超越U-Net基线 [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/10882)。

### 2. 基于多视图扩散的3D重建

该范式利用预训练的2D扩散模型生成多视角一致图像，再通过经典3D重建算法（如NeRF、3DGS）恢复3D结构，有效利用了2D先验。

- **CAT3D** (CVPR 2024) 旨在解决稀疏视图或单图3D重建的欠约束问题。其提出多视角潜在扩散模型（MVLDM），通过3D自注意力层和相机位姿条件，一次性生成多视角一致图像；随后利用这些合成视图通过NeRF进行3D重建。该方法在多个benchmark上比SOTA快一个数量级，且能生成广视角、高一致性的场景 [csdn.net](https://blog.csdn.net/m0_60177079/article/details/144796428)。

- **Sherpa3D** (CVPR 2024) 针对纯2D提升方法存在的多面雅努斯（Multi-faced Janus）问题，提出利用3D扩散模型生成的粗糙3D先验来指导2D扩散模型优化。其设计了结构指导与语义指导双重策略，使2D模型在细化过程中兼顾几何保真与3D一致性。实验证明，该方法在文本到3D生成任务中，显著优于仅依赖2D先验的方法 [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/46408)。

- **Wonderland** (arXiv 2024) 专注于从单张图像生成广阔、高质量的3D场景。其创新地将相机位姿控制嵌入视频扩散模型，并设计双分支控制机制（ControlNet+LoRA）保证几何一致性；随后，利用大规模隐式3D重建模型（LaLRM）从前馈生成的视频latent中直接重建3DGS。该方法在RealEstate10K等数据集上重建质量SOTA，且端到端生成仅需约5分钟 [csdn.net](https://blog.csdn.net/weixin_49587977/article/details/144986056)。

### 3. 基于单步扩散的3D增强与去伪影

此方向不直接生成3D，而是利用扩散模型作为后处理模块，提升现有3D重建结果的质量。

- **Difix3D+** (2025) 针对NeRF和3DGS在极端视角下渲染伪影的问题，提出使用单步图像扩散模型Difix。Difix在训练阶段用于“清理”从重建模型中渲染出的伪视图，并将其重新提炼回3D表示；在推理阶段则作为神经增强器，直接去除渲染图像中的残余伪影。该通用框架在NeRF和3DGS上均适用，平均将FID分数提升2倍，同时保持3D一致性 [baai.ac.cn](https://hub.baai.ac.cn/paper/5d599177-dda4-48f2-91a7-b5de0449e570)。

### 4. 前馈式大型3D重建模型

随着模型规模增大，研究者开始探索直接从前馈网络中高效重建3D的范式。

- **GRM** (2024) 提出一种基于Transformer的大型重建模型，可直接从四张稀疏视图输入，在0.1秒内输出密集的3D高斯分布。其通过窗口化自注意力机制高效上采样特征，并直接解码为像素对齐的3D高斯。GRM在重建质量和效率上均超越传统优化方法，并可与多视图扩散模型结合，用于文本/图像到3D生成 [csdn.net](https://blog.csdn.net/weixin_41871126/article/details/144336756)。

## 实验与评价总结

对上述工作的实验分析可归纳出几点共性结论。首先，在**生成质量**上，利用2D扩散先验（特别是多视图/视频扩散模型）的方法普遍能生成细节更丰富、纹理更逼真的3D资产，其优势在处理复杂材质与光照时尤为明显。其次，在**几何一致性**方面，引入显式3D约束（如相机位姿、粗糙3D先验或3D自注意力）是解决多面雅努斯问题、保证跨视角一致性的关键。再者，在**效率**上，前馈式大型模型（如GRM）和单步扩散增强（如Difix3D+）显著改变了3D生成/重建的范式，将耗时的优化过程转变为快速推理，为实时应用铺平了道路。最后，**评估指标**正从单一的FID/PSNR等2D指标，转向结合3D几何精度（如Chamfer Distance）、多视角一致性（如LPIPS on novel views）和渲染质量的综合评价体系。

## 趋势与挑战

基于2024-2025年的最新进展，该领域未来将围绕以下方向深入发展：
1.  **世界模型与物理AI的融合**：如NVIDIA Cosmos等世界基础模型（World Foundation Models）的出现，预示着3D生成将从静态资产创建转向动态、可交互的物理仿真环境生成，为机器人和自动驾驶提供合成数据与规划平台。
2.  **统一的多模态生成框架**：未来的3D生成模型将不再局限于单一输入（如文本或图像），而是构建能无缝处理文本、图像、视频、3D草图等多种模态提示的统一架构，实现更自然、更可控的3D内容创作。
3.  **高效与可编辑性的协同优化**：研究重点将从单纯追求生成速度或质量，转向设计兼具高效推理与高度可编辑性的表示与模型（如SPAR3D的点云中间表示），以满足设计师和开发者的实际工作流需求。

## 结论

2022至2025年间，扩散技术深刻重塑了3D重建与生成领域。从早期的隐空间点云生成，到利用强大2D先验的多视图重建，再到高效的前馈式大模型和单步增强策略，研究路径日益多元且高效。未来，随着世界模型、多模态对齐和可编辑性等方向的突破，基于扩散的3D技术有望成为连接数字内容创作与物理世界仿真的核心桥梁。

## 参考文献

1.  Zeng, X., et al. LION: Latent Point Diffusion Models for 3D Shape Generation. *NeurIPS*, 2022. [zhuanzhi.ai](https://www.zhuanzhi.ai/paper/731cfc5d4536d93cf9f94aea445edfc5)
2.  Mo, S., et al. DiT-3D: Exploring Plain Diffusion Transformers for 3D Shape Generation. *NeurIPS*, 2023. [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/10882)
3.  Liu, F., et al. Sherpa3D: Boosting High-Fidelity Text-to-3D Generation via Coarse 3D Prior. *CVPR*, 2024. [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/46408)
4.  Wu, J. Z., et al. Difix3D+: Improving 3D Reconstructions with Single-Step Diffusion Models. *arXiv preprint arXiv:2503.00705*, 2025. [baai.ac.cn](https://hub.baai.ac.cn/paper/5d599177-dda4-48f2-91a7-b5de0449e570)
5.  Kolotouros, N., et al. Instant 3D Human Avatar Generation using Image Diffusion Models. *ECCV*, 2024. [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/97996)
6.  Wang, Z., Li, D., & Jiang, R. Diffusion Models in 3D Vision: A Survey. *arXiv preprint arXiv:2410.03661*, 2024. [baai.ac.cn](https://hub.baai.ac.cn/paper/a77ae72a-e5f4-4bc4-9c0a-62b1d990be91)
7.  Liang, H., et al. Wonderland: Exploring 3D from a Single Image. *arXiv preprint arXiv:2412.12091*, 2024. [csdn.net](https://blog.csdn.net/weixin_49587977/article/details/144986056)
8.  Liu, F., et al. CAT3D: Create Anything in 3D with Multi-View Diffusion Models. *arXiv preprint arXiv:2405.10314*, 2024. [csdn.net](https://blog.csdn.net/m0_60177079/article/details/144796428)
9.  Zhang, C., et al. Large Language Model-Brained GUI Agents: A Survey. *arXiv preprint arXiv:2411.18279*, 2024.
10. Jiang, R., et al. A Survey of Multimodal Controllable Diffusion Models. *Journal of Computer Science and Technology*, 2024. [jcst.ict.ac.cn](https://jcst.ict.ac.cn/cn/article/cstr/32374.14.s11390-024-3814-0)
11. Team, S. AI. SPAR3D: Stable Point-Aware Reconstruction of 3D Objects from Single Images. *Stability AI Technical Report*, 2025.
12. Research, N. Cosmos: World Foundation Model Platform for Physical AI. *NVIDIA Technical Report*, 2025.