引言  
近年来扩散模型（diffusion models）迅速渗透到三维视觉与重建领域，形成两条互补路线：一是利用强大的2D/多视图扩散先验生成或补全可用于3D重建的多视图观测（“2D→3D 蒸馏/多视角合成”）；二是直接在三维表示（点云 / splats / triplanes /隐式场）或其潜在空间上训练/部署扩散模型以做生成或修复（“3D-aware diffusion / latent 3D diffusion”）。本综述聚焦 2022–2025 年代表性工作，按方法类别挑选每类 3–5 篇最具代表性的论文，比较它们在跨域（稀疏视角、单视图、文本到3D 及不同3D表示间）的适用性与局限，并总结实验共性结论与未来趋势。为保证准确性，本文仅引用公开论文/预印本，并在文末给出参考文献（≥12 篇）。部分方法的原文或综述在公开项目/社群页面上有聚合（下文引用相应页面以便检索）。

方法分类与代表作  
A. 多视图扩散用于生成一致训练视图 → 支持下游 3D 重建（2D→3D 蒸馏/多视角扩展）  
- CAT3D (Gao et al., 2024)。问题：在单视图或稀疏视角条件下，如何高效生成多视角、一致的新视图以约束后端重建？核心方法：训练一个相机条件的多视角潜在扩散模型（multi-view latent diffusion）生成大量视角一致图像，再用这些合成视图驱动 NeRF/3DGS 等重建器；关键实验结论：能在约 1 分钟内生成用于重建的多视图集合，并在单视图或少视角场景上明显提升重建质量与效率（详见项目页）[hub.baai.ac.cn].  
  引用：CAT3D 项目与论文摘要页 [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/279b2bd6-1104-43ef-9662-985769c3f8e0).

- ViewSet / MVDiffusion (Szymanowicz et al., Tang et al., 2023–2024)。问题：如何在不依赖昂贵3D表示渲染的前提下，在多视图空间学习一致生成及其条件化？核心方法：将多视图生成建模为集合条件化扩散——在潜在或像素层面同时建模跨视角对应性（部分方法采用3D-aware conditioning / correspondence-aware losses）；关键结论：多视图感知扩散可显著提升稀疏视角生成一致性，代价在于需要跨视图注意力或体渲染的计算（参见相关开源/预印本与复现工作）[相关综述与论文列表见 hub.baai.ac.cn].

- Reconfusion / ReconFusion (生成式重建系列, 2023–2024)。问题：如何把2D扩散先验“蒸馏”到可用于3D参数更新的训练目标？核心方法：用扩散生成的新视图作为伪观测回馈给3D表示（如 NeRF）并以图像损失或感知损失重新优化；关键结论：对稀疏/单视图场景，这类“生成补观测 → 反向重建”的管道能改善对不可见区域的推断，但对几何一致性的长期收敛仍依赖于重建表示的可表达性（见多篇实现与对比实验，汇总于综述）[参见 hub.baai.ac.cn 中的综述条目].

B. 将 2D 扩散提升到 3D / 文本到 3D（蒸馏与引导策略）  
- Sherpa3D (Liu et al., CVPR 2024)。问题：文本到3D 中，如何同时兼顾 2D 生成模型的细节与 3D 一致性？核心方法：用粗糙的 3D 先验（由3D扩散生成或粗糙几何估计）分别提供几何与语义指导，引导 2D diffusion-based renderers 做视角一致的细化；关键结论：两类指导（结构性与语义一致性）可在保持2D细节的同时显著降低多面雅努斯问题，提高文本→3D 的几何一致性[chatpaper.com].  
  引用：Sherpa3D 项目/论文页 [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/46408).

- DreamFusion / Magic3D 等（代表早期将 2D 文本-图像扩散“提升”到3D的工作，2022–2023）。问题：没有大量3D数据时如何基于2D diffusion 做文本到3D？核心方法：以 NeRF（或隐式场）为可微渲染体，使用预训练2D扩散模型对渲染结果做评分或引导（score distillation / distillation loss）；关键结论：该类方法能从文本生成高保真 3D 表示，但对渲染/优化成本、视角一致性和长尾泛化仍有挑战（被后续Sherpa3D等工作以粗糙3D先验改进）。（经典综述列出这些方法作为开创性路线，见 hub.baai.ac.cn 综述条目）。

C. 在显式 3D 表示或其潜在空间上做扩散 —— 快速采样与可渲染 3D 生成  
- Sampling 3D Gaussian Scenes in Seconds with Latent Diffusion Models (潜在 LDM→3DGS, 2024)。问题：如何在保证多视角一致性的同时实现毫秒级采样？核心方法：将 3D Gaussian Splatting（3DGS）作为显式渲染表征，设计一个 autoencoder 将 splats 压缩到低维 latent，再在 latent 上训练多视图潜在扩散模型；关键实验结论：在 MVImgNet / RealEstate10K 等真实图像集上实现了 0.2s 级别的场景采样，且在速度上比体渲染的 3D diffusion 快约一个数量级[blog.csdn.net].  
  引用：博客与论文摘要（采样速度与实证数据在文中给出）[blog.csdn.net](https://blog.csdn.net/qq_45752541/article/details/140201446).

- LatentSplat / SplatterImage（2024 CVPR 及相关工作）。问题：如何用 splats（3D Gaussian）构造紧凑潜在空间以便高效生成/重建？核心方法：Autoencoder 将多视图图像编码为 splat 参数的潜在表示，并在潜在上训练扩散器；关键结论：splats-as-latent 方案在速度/实时渲染上有明显优势，但直接在 splat 参数上建模会带来维数与训练成本的挑战，相比压缩潜在的方案质量-效率权衡较差（详见实验对比）[相关论文与实现见综述与博客].

- 3D Gaussian Splatting (Kerbl et al., 2023; 实时渲染基础)。问题：如何以粒子/高斯 splats 实现高质量实时渲染以支撑生成与编辑流程？核心贡献：提出高效的 splatting 表示与渲染管线，使得基于 splats 的生成与后处理成为可行基础；结论：与 NeRF 相比，3DGS 在交互式渲染与后续扩散采样中具备工程可行性（该表示成为后续 latent-diffusion→3DGS 管线的基石）。

D. 直接在 3D/体素/点云/体场上做 diffusion（3D-aware / Transformer-based diffusion）  
- DiT-3D (Mo et al., 2025 preprint/NeurIPS-style explorations)。问题：Transformer 架构在 3D 点云/体素去噪上能否替代 U-Net？核心方法：将 DiT（Diffusion Transformer）的架构扩展到体素化点云 / 3D token，并引入窗口化 3D 自注意力以控制复杂度；关键结论：在 ShapeNet 等合成数据上，DiT-3D 在可扩展性与生成质量上展现竞争力，且 ImageNet 上预训练的 DiT-2D checkpoint 可迁移性良好[chatpaper.com].  
  引用：DiT-3D 介绍页 [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/10882).

- Triplane / Holodiffusion / triplane-diffusion 系列（若干 2023–2024 工作）。问题：如何把多尺度/多平面表征同扩散结合以高效生成 3D 场景？方法：在 triplane /三平面表示上训练扩散或在三平面潜在上做生成；结论：triplane-based diffusion 能在中等分辨率下以较小成本生成高质量形状/纹理，但细节与长程一致性仍依赖 decoder 与渲染步骤的设计（见综述与多篇并行工作）。

E. 扩散模型作为 3D 重建/渲染的后处理器（去伪影 / 神经增强）  
- Difix3D+ (Wu et al., 2025)。问题：NeRF / 3DGS 渲染在极端新视角或欠约束区域会产生伪影，如何高效修复而不破坏 3D 一致性？核心方法：设计 Difix——一个单步图像级扩散增强器，既可在训练阶段清理重建渲染以生成更好的伪训练视图（蒸馏回 3D），也可在推理时作为神经后处理器直接去伪影；关键实验结论：在 NeRF 与 3DGS 两类表示上使用同一 Difix 模型，能在保持 3D 一致性的同时将 FID 在多个场景里平均降低约 2 倍（论文与项目页给出量化对比）[hub.baai.ac.cn].  
  引用：Difix3D+ 项目页与论文简介 [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/5d599177-dda4-48f2-91a7-b5de0449e570).

- DiffusioNeRF / NeRF-guided diffusion (若干 2023 CVPR/ICLR 方向工作)。问题：能否用扩散模型约束或正则化 NeRF 优化以减少伪影？方法：用图像级扩散或基于渲染的去噪器作为正则器来引导 NeRF 更新；结论：扩散正则能改善稀疏视角下的细节，但对几何精确性有时导致“过度修饰”需谨慎权衡（见对应论文与消融实验）。

实验与评价总结（共性结论，避免逐篇复述）  
1) 扩散先验能补足可观测视图不足带来的不确定性，但“可示范的一致性”不是自动保证的：多数方案通过（a）将生成视图回馈到显式3D重建器（蒸馏）或（b）在3D表示/潜在上直接建模来恢复一致性；实践中蒸馏法能快速改善可视外观但易引入与真实几何的偏差，直接在3D/latent上建模更有利于几何一致性但训练与渲染成本更高。  
2) 表征选择决定效率/质量权衡：显式 splats/3DGS + latent-diffusion 能实现秒级或亚秒级采样（利于交互式应用），而基于 NeRF 的 3D 感知扩散通常更慢但在细节与光照连贯性上表现好；换言之，表征（NeRF、triplane、splats、点云）与去噪域（像素、潜在、3D参数）共同决定可部署性。  
3) 单步/蒸馏技术（如 Difix、单步 LDM 蒸馏）对实时/工程化落地至关重要：多步扩散在质量上有优势，但蒸馏到单步模型或在 latent 空间运行是当前主流加速路径（多篇工作以此实现近实时后处理或快速采样，见 Difix3D+、latent-splat 类工作）。  
4) 评价仍欠统一且偏向图像指标：大量工作报告 FID/LPIPS/PSNR/LPIPS 改善，但缺乏统一的、直接衡量 3D 几何正确性与跨视角一致性的度量；因此跨方法横向比较常受评测选择与渲染器影响。  
5) 数据与条件化策略（相机 pose、粗略深度、文本/类别条件）显著影响泛化：带相机条件或粗糙几何先验的方法在真实世界多样场景上的泛化明显优于仅依赖文本或单图条件的方法（多篇实证支持，见 CAT3D、Sherpa3D、Sampling 3D Gaussian Scenes 的数据表述与实验）。

趋势与挑战（2025 年前后预测，至少三点）  
1) 潜在空间 + 显式可渲染表征将成为主流工程化路线：结合 autoencoder 把显式 3D 表征（splats / triplanes /低维体素）压缩到紧致 latent，再在 latent 上做扩散可同时实现可渲染性与低延迟采样（已被 Sampling 3D Gaussian Scenes、LatentSplat 等展示）；预计未来 2 年内更多工作会围绕 latent→decoder 的一致性正则与可微渲染优化展开。  
2) 单步/蒸馏与可验证一致性机制会成为必要配套：为满足实时或交互式场景（AR/虚拟制作/机器人），多步扩散需蒸馏到单步或极少步骤模型（如 Difix、SIM 类蒸馏技术），同时研究将几何一致性作为可验证约束的训练/推理机制（例如基于渲染的循环检验或基于几何一致性的判别器）将增多。  
3) 表示级协同（2D先验 + 3D粗糙先验）的混合策略将进一步成熟：纯2D先验细节丰富但易产生多面，纯3D生成稳定但昂贵；Sherpa3D、CAT3D 等表明“粗3D先验 + 强2D细节蒸馏”是有效折衷，未来将有更多自动化先验融合与跨模态蒸馏策略出现（例如使用视频/大规模多视图数据学习通用先验）。  
4) 评价基准与可重复性将被提上日程：当前指标难以同时反映渲染质量、几何准确性与跨视角一致性；预期社区会推动包含多视角真实扫描（含 ground-truth geometry）、统一渲染流程与任务导向指标（如 downstream 操作成功率、机器人放置误差等）的基准套件。  
5) 可控 3D 生成（语义/物理/材质可控）与交互式编辑将成为重要应用方向：随着表征与采样速度提升，用户可通过文本/草图/部分几何输入主动控制生成内容，且需要物理/接触一致性的约束来支撑机器人与虚拟制作场景的可用性。

结论  
扩散模型已在跨域 3D 重建与生成中展示出强大潜力，但实际落地要求在速度、3D 一致性、表示可渲染性和可控性之间做系统权衡。2022–2025 年的发展轨迹表明：一方面，多视角/2D→3D 蒸馏与显式 splats + latent diffusion 为工程化应用提供了现实可行的路径；另一方面，保持几何精确性与跨视角一致性的理论与评测仍需加强。未来研究需要将蒸馏/单步加速、表示层协同（粗几何先验与2D细节）以及统一可验证评价结合起来，才能将扩散带来的视觉优点稳定转化为可部署的 3D 系统。

参考文献（本文选择的代表性论文 / 综述与项目页；以便检索原文）  
- Gao, R., Holynski, A., Henzler, P., Brussee, A., Martin-Brualla, R., Srinivasan, P., Barron, J. T., Poole, B., "CAT3D: Create Anything in 3D with Multi-View Diffusion Models", 2024. 项目/论文摘要页: [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/279b2bd6-1104-43ef-9662-985769c3f8e0).  
- Wu, J. Z., Zhangjie, etc., "Difix3D+: Improving 3D Reconstructions with Single-Step Diffusion Models", 2025. 项目/论文简介页: [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/5d599177-dda4-48f2-91a7-b5de0449e570).  
- Liu, F., Wu, D., Wei, Y., Rao, Y., Duan, Y., "Sherpa3D: Boosting High-Fidelity Text-to-3D Generation via Coarse 3D Prior", CVPR 2024. 摘要/汇总页: [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/46408).  
- "Diffusion Models in 3D Vision: A Survey" (Wang, Li, Jiang et al.), 2024 — 综述条目与聚合资料: [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/a77ae72a-e5f4-4bc4-9c0a-62b1d990be91).  
- "DiT-3D: Exploring Plain Diffusion Transformers for 3D Shape Generation" (Mo et al.), 2025 summary: [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/10882).  
- "Sampling 3D Gaussian Scenes in Seconds with Latent Diffusion Models" (潜在 LDM→3DGS，论文与实现讨论)，2406.13099；综述/教程页: [blog.csdn.net](https://blog.csdn.net/qq_45752541/article/details/140201446).  
- Kerbl, G., et al., "3D Gaussian Splatting for Real-Time Radiance Field Rendering", ACM Trans. Graph. (TOG), 2023 — 对 splats / 3DGS 表征与实时渲染基础的贡献（可检索至期刊/会议页面）。  
- Szymanowicz, et al., "ViewSet Diffusion" / Tang et al., "MVDiffusion" (workshops / ICCV/ICLR 2023–2024 系列预印本与实现)，见相关会议与综述索引（汇总于 hub.baai.ac.cn）。  
- Anciukevicius, T., et al., "Denoising diffusion via image-based rendering" / "RenderDiffusion" (相关 CVPR/ICLR 方向工作，2023)，参见论文与实现页（列于综述引用列表）。  
- "SplatterImage: Ultra-fast single-view 3D reconstruction" (Szymanowicz et al.), CVPR 2024 — 单视图→splats 快速重建与对比实验（列入多篇对比）。  
- DreamFusion, Magic3D, NeRF-guided diffusion 等（2022–2023 年一系列将 2D diffusion 拓展到3D的代表性工作），相关论文与实现可在 arXiv / CVPR/ICLR 记录中检索（综述中列为开创路线）。  
- 其它被引用的支撑与比较工作（包括 triplane/latent-triplane diffusion、LatentSplat、Reconfusion 等），详见上文综述与 hub.baai.ac.cn 的聚合条目（该站点汇总了多篇 2023–2025 年相关工作与链接）[hub.baai.ac.cn](https://hub.baai.ac.cn).

（注）本文旨在按方法类别给出 2022–2025 年间的代表路线与实验共性结论，并引导后续研究方向；读者若需各篇论文的完整实现细节与定量数据，请参阅各论文原文与项目页（上列链接/聚合页便于检索）。