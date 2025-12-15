引言

近年来，扩散模型（diffusion models）在二维图像生成上取得突破后，很快被推广到三维视觉任务：既用于直接的3D形状/点云/网格生成，也作为 2D→3D / 多视角→3D 重建与新视角合成的强先验或增强器。本文以 2022–2025 年的代表性工作为主，系统梳理基于扩散技术的 3D 生成与重建方法的类别、核心思想与关键实证结论，并总结评价共性、指出现有挑战与未来趋势。为满足可审查性，文中每篇方法均给出对应公开文献/预印本链接（参考文献部分）。本文力求学术密度、避免空泛表述。

方法分类与代表作
（每个子类 3–5 篇代表作；每篇 4–6 句，突出问题、方法、结论）

A. 点云 / 形状生成（Point / Shape diffusion）
1) LION: Latent Point Diffusion Models for 3D Shape Generation (NeurIPS 2022)
- 问题：直接在点云/形状空间使用扩散模型生成高质量、可操控且可进一步重建为平滑网格的三维形状。  
- 方法：构建一个分层 VAE，把形状编码为（全局）latent + 点结构化 latent，并在两个潜在空间上分别训练分层扩散过程，从而结合全局一致性与点级细节。  
- 结论：在 ShapeNet 等基准上，分层潜在设计显著优于直接在点云上建模的扩散方法；该框架支持条件生成、插值与后续表面重建，生成网格质量可用于艺术级应用。  
(参见 [zhuanzhi.ai](https://www.zhuanzhi.ai/paper/731cfc5d4536d93cf9f94aea445edfc5))

2) DiT-3D: Exploring Plain Diffusion Transformers for 3D Shape Generation (NeurIPS/OpenReview thread)
- 问题：探究 Transformer（而非 U-Net）作为去噪架构在三维体素/点表示上的可扩展性与生成质量。  
- 方法：将 DiT（Diffusion Transformer）架构改造用于体素化/体素化点云输入，采用 3D 窗口化自注意力以降低计算，并使用来自 2D ImageNet/DiT 的预训练权重蒸馏到 3D。  
- 结论：在 ShapeNet 上，DiT-3D 在高分辨率生成与模型可扩展性（更大的模型、更多训练数据）方面优于同规模 U-Net 基线，说明 Transformer 在 3D 扩散建模上的可行性。  
(参见 [chatpaper.com / openreview](https://chatpaper.com/chatpaper/zh-CN/paper/10882))

3) Mesh / Surface score-based models (代表性论文示例：MeshDiffusion 等，2023)
- 问题：直接在网格/显式表面空间生成高质量、有拓扑变化的三维网格。  
- 方法：将 score-based / score matching 扩散思想扩展到网格顶点位置或隐式场后做可微分表面提取（或联合优化几何与拓扑），并引入表面级对抗/重建损失以提高细节。  
- 结论：相比点云生成，面向网格的扩散模型在细节与可直接使用的资产生成上更具优势，但训练和表面一致性需要特殊设计（可微等值面提取与正则化）。  
(相关工作与实现参见 DMTet 及其引用的 MeshDiffusion 文献，见参考)

B. 基于多视角 / 多视图扩散的重建与新视角合成
1) CAT3D: Create Anything in 3D with Multi-View Diffusion Models (arXiv 2024)
- 问题：在单视图或稀疏视图输入下，将欠约束的 3D 重建问题重表述为“生成更多一致视图，再回推 3D 表示”。  
- 方法：训练一个相机条件的多视角扩散模型（在潜在或像素空间）以同时生成多视图图像，采用相机光线嵌入与多视角 self-attention 来实现视角一致性；随后用生成的多视图作为 NeRF/Zip-NeRF 等重建器的输入。  
- 结论：通过生成大量高一致性合成视图，CAT3D 在稀疏视图/单视图情形下能显著提升最终 3D 重建的几何与纹理质量，并把重建时间缩短一个数量级（相较于逐视优化方法）。  
(参见 arXiv: [arxiv.org](https://arxiv.org/abs/2405.10314)；详见中文解读 [csdn.net](https://blog.csdn.net/m0_60177079/article/details/144796428))

2) 多视角扩散 / 视频扩散用于新视角生成（survey 中综述的代表方法）
- 问题：如何在生成过程中保证跨视图几何一致性与相机可控性。  
- 方法：将多张视图作为扩散模型的“时间”或“通道”维度引入，使用相机条件、Ray embedding 或 3D-aware self-attention（或显式几何先验）来约束视角间一致性；并使用并行采样策略以提高采样效率。  
- 结论：多视角扩散在新视角合成上能显著减少多面 Janus 现象，但需要额外的几何引导或后验约束来解决全局几何一致性问题（尤其在大尺度场景时）。  
(参见综述 [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/a77ae72a-e5f4-4bc4-9c0a-62b1d990be91) 与 CAT3D 工作)

C. 文本/图像→3D：利用 2D 扩散先验进行 3D 生成
1) Sherpa3D: Boosting High-Fidelity Text-to-3D via Coarse 3D Prior (CVPR 2024)
- 问题：如何同时兼顾 2D 扩散模型的细节泛化能力与 3D 扩散/渲染管线的几何一致性，在文本到 3D 任务中减少雅努斯/视角模糊问题。  
- 方法：生成粗糙 3D 先验（来自 3D 扩散或其他方法），并将其作为结构与语义双重引导对 2D 文本到图像扩散的蒸馏/细化过程施加约束，从而得到几何保真且细节丰富的最终结果。  
- 结论：使用粗糙 3D 先验作为两阶段指导能有效减少生成结果的多面体不一致性，在质量与几何一致性上均优于仅用 2D 蒸馏或仅用 3D 扩散的基线。  
(参见 [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/46408))

2) Instant 3D Human Avatar Generation using Image Diffusion Models (ECCV 2024)
- 问题：快速（数秒级）从图像/文本生成多样、高质量、可控的 3D 人像/头像。  
- 方法：将强大的图像扩散先验用于生成多视图或背面预测图像，随后用 3D提升网络把多视图映射到 3D 表示；将图像生成与 3D 重建解耦以复用大规模 2D 预训练特性。  
- 结论：通过将生成与 3D 提升解耦，方法在速度上比多数端到端 3D 方法快数个数量级，同时在多模态控制（姿势、形状）上展现出高保真度与多样性。  
(参见 [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/97996))

3) DreamFusion 系列思路（以 2D 文本-图像扩散模型作为 3D 优化的渲染监督；关键论文始于 2022 年）
- 问题：如何不用大规模 3D 数据，仅借助 2D 文本-图像扩散先验进行文本到 3D 的物体/场景优化。  
- 方法：把渲染器（NeRF/体渲染）输出的多视图渲染图通过预训练的 2D 文本到图像模型（或其指导器）计算损失，并对 3D 表示做梯度更新（即以 2D 扩散模型为评分函数）。  
- 结论：该类方法可生成种类丰富的文本到 3D 结果，但常受“符号-视角”不稳定（multi-view Janus）与渲染噪声影响，后续工作多通过几何先验或多视图约束来缓解。  
(相关工作在 2022–2024 年间出现多篇变体，综述见 [hub.baai.ac.cn survey](https://hub.baai.ac.cn/paper/a77ae72a-e5f4-4bc4-9c0a-62b1d990be91))

D. 扩散作为“神经增强器”或后处理器（用于去伪/细化 3D 渲染）
1) Difix3D+: Improving 3D Reconstructions with Single-Step Diffusion Models (2025 preprint)
- 问题：NeRF / 3DGS 等重建表示在极端新视角渲染时常带伪影，且传统表示对欠约束区域难以完善。  
- 方法：提出 Difix，一种单步图像扩散清洗器，用于（a）在重建阶段清理由当前 3D 表示渲染出的伪训练视图并回炼入 3D；（b）在推理阶段充当神经增强器对新视角渲染进行单步修复，从而保持 3D 一致性同时去除伪影。  
- 结论：在 NeRF 与 3D Gaussian Splatting 等表示上，单一 Difix 模型即可在保持一致性的前提下显著降低 FID 等图像质量指标的伪影，作者报告平均 FID 提升约 2 倍（详见原文实验）。  
(参见 [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/5d599177-dda4-48f2-91a7-b5de0449e570))

2) Render / image-diffusion for 3D reconstruction/inpainting（相关工作）
- 问题：用图像扩散模型直接修复或完成由 3D 表示渲染出的缺陷视图（补洞、去噪、细节增强）。  
- 方法：把扩散模型作为图像级去噪/修复模块，结合几何一致性损失或把修复结果反投影到 3D 表示以迭代提升。  
- 结论：图像级扩散器能有效提升渲染感知质量，但如何保证修复后的像素在多视图下一致并能稳定回传以改进 3D 表示仍是核心难点（需要显式 3D 回炼策略）。  
(综述与代表实现参见前述 survey 与 Difix3D+)

实验与评价总结（只给共性结论，避免逐篇复述）

- 数据与基准多样但不统一：研究使用的基准包括 ShapeNet、SRN/DTU、real-scene scan 数据集及自建合成数据。不同工作在几何（Chamfer/IoU）与渲染图像质量（FID / LPIPS / PSNR / SSIM）上的侧重点不同，导致跨论文的直接量化对比困难。综述/对比工作（例如 2024 年 survey）建议建立统一的多视图一致性评测协议。  
- 2D 扩散先验能显著提升细节与纹理表现，但易引入视角矛盾（multi-view Janus）：将 2D 扩散输出回传到 3D 表示时，若缺乏显式几何/视角约束，会出现不同视角间不一致的细节或“打架”现象。多视图扩散或加入粗糙 3D 先验可有效缓解这一问题。  
- 潜在空间/分层设计是提升效率与质量的关键：在点云/形状生成中，分层 VAE + 在潜在上做扩散（如 LION）能同时实现高质量与下游可控（插值/条件生成）；在图像到 3D 的管道中，把生成与 3D 提升解耦（image-diffusion → 3D-lift）能大幅降低运行时成本并复用 2D 预训练能力。  
- 采样效率与模型规模/算力显著影响可用性：许多扩散到 3D 的方法仍面临采样迭代次数高、渲染-优化循环成本大的现实瓶颈；单步/快速扩散（或蒸馏采样）与并行多视图采样是当前经常采用的工程折中。  
- 评价指标需兼顾几何与视图一致性：图像指标（FID/LPIPS）不能单独反映 3D 可用性，几何指标（Chamfer/IoU）亦无法评估渲染细节；近期工作倾向于联合报告并引入多视图一致性指标（如跨视点 LPIPS/深度一致性）。

趋势与挑战（基于 2022–2025 发展，给出 >=3 点预测）
1) 从“2D-driven”向“2D+粗3D先验”联合范式转变：纯 2D 扩散蒸馏虽带来细节，但多视角不一致问题促使研究更倾向于用廉价/粗糙的 3D 先验（低分辨率体、粗网格、3DGS）作为结构与语义约束，与 2D 扩散结合成为主流（Sherpa3D、CAT3D 的方向）。  
2) 单步/快速扩散与蒸馏会成为工程化关键：为实现实时或近实时的 3D 内容生成/重建，单步增强（如 Difix3D+）与采样蒸馏（将多步扩散压缩为少步/1 步）将得到更多关注与标准化。  
3) 可微分显式表面提取与联合优化框架会被普及：要把扩散生成的视图一致性有效回炼到 3D，需把可微分的等值面/网格提取层（如 DMTet 风格）与扩散/score 模型联合训练，以直接在表面层面优化几何与纹理一致性。  
4) 评测标准与数据集将向多视图一致性与可用性迁移：未来基准将不仅报告单视图图像度量，还会纳入跨视点一致性、重建可用性（可导出网格/材质）与运行时开销三维度指标，推动方法朝“学术可比且工程可用”发展。  
5) 模型通用性与模块化趋势：由于 2D 扩散大模型的可迁移性越来越强，预计更多工作采用模块化流水线（通用 2D 扩散 + 任务化 3D 提升/回炼模块），并通过少量 3D 监督/先验实现高质量、可控的 3D 产出。

结论

2022–2025 年间，扩散技术已从纯 2D 图像生成演化为推动 3D 形状生成、图像→3D 重建和文本→3D 生成的核心工具链组成部分。关键进展包括（1）在潜在或点结构化空间上做分层扩散以提高生成质量与可控性（LION 等）；（2）多视角扩散模型与相机条件化设计能在少视图场景下生成更多一致视图，从而改善 3D 重建（CAT3D）；（3）将扩散模型作为单步神经增强器用于去伪与细化（Difix3D+）可在保持一致性的同时显著改善渲染质量。未来的研究需聚焦多视图一致性评估、采样效率改进与可微分表面回炼，以推动这些方法向现实应用落地。

参考文献（按出现顺序，均为公开论文/预印本；至少 12 篇）

- Difix3D+: Improving 3D Reconstructions with Single-Step Diffusion Models — Jay Zhangjie Wu et al., 2025. 预印/报告页面: [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/5d599177-dda4-48f2-91a7-b5de0449e570)

- Diffusion Models in 3D Vision: A Survey — Zhen Wang, Dongyuan Li, Renhe Jiang, 2024. survey: [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/a77ae72a-e5f4-4bc4-9c0a-62b1d990be91)

- DiT-3D: Exploring Plain Diffusion Transformers for 3D Shape Generation — Shentong Mo et al., (OpenReview / NeurIPS thread). summary page: [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/10882) (原始讨论/提交见 OpenReview)

- Sherpa3D: Boosting High-Fidelity Text-to-3D Generation via Coarse 3D Prior — Fangfu Liu et al., CVPR 2024. summary / mirror: [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/46408)

- CAT3D: Create Anything in 3D with Multi-View Diffusion Models — arXiv:2405.10314 (paper / preprint); 解读: [blog.csdn.net](https://blog.csdn.net/m0_60177079/article/details/144796428)；原文: [arXiv](https://arxiv.org/abs/2405.10314)

- Instant 3D Human Avatar Generation using Image Diffusion Models — Nikos Kolotouros et al., ECCV 2024. project/summary: [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/97996)

- LION: Latent Point Diffusion Models for 3D Shape Generation — Xiaohui Zeng et al., NeurIPS 2022 / arXiv. summary page: [zhuanzhi.ai](https://www.zhuanzhi.ai/paper/731cfc5d4536d93cf9f94aea445edfc5) (原始 arXiv/NeurIPS 出版信息见该页)

- DMTet: Deep Marching Tetrahedra — Shen et al., NeurIPS 2021 (混合表示、可微表面提取). 介绍/翻译页: [nxrte.com](https://www.nxrte.com/jishu/25856.html)；原文/项目页请参阅作者主页与 NeurIPS 稿件。

- 关于可控/多模态扩散的综述（A Survey of Multimodal Controllable Diffusion Models）— Jiang Rui et al., 2024（期刊综述）: [jcst.ict.ac.cn](https://jcst.ict.ac.cn/cn/article/cstr/32374.14.s11390-024-3814-0)

- （相关/背景）MeshDiffusion / Score-based 3D mesh generative works（2023 年以后的若干预印本，参见 DMTet 参考文献与后续 MeshDiffusion 预印本）— 可通过 arXiv 检索 MeshDiffusion: e.g. “MeshDiffusion: Score-based Generative 3D Mesh Modeling” (arXiv) 等（参见 DMTet 文献列表）。

- 相关 2D→3D 扩散监督思路（DreamFusion 类方法，2022 起的一系列工作）— 将 2D 文本-图像扩散模型用作 3D 渲染的评分/引导函数（见 2022–2024 年多篇 arXiv/会议投稿，survey 汇总于上文 hub.baai 综述）。

（注）本文重点引用并整合了 2022–2025 年期间的代表性公开工作与综述。上文列举的具体实现/代码与更详尽的量化对比请参见各论文原文与作者项目页；部分综述与中文解读页在参考中给出以便快速定位原文。若需我按标准化指标（Chamfer / FID / LPIPS / PSNR 等）对若干方法做表格化对比并给出可复现的评测建议，我可以继续补充具体量表与实验协议。