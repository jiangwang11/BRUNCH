引言  
本文综述以“单目（monocular）视觉下的动态场景三维重建（2022–2025）”为范围，聚焦近三年中两条主流技术路线的代表性工作：以射线采样/隐式表征为核心的动态 NeRF 家族，和以光栅化 / 3D 高斯泼溅（Gaussian Splatting）为代表的显式/半显式实时管线；另增加若干针对单目输入鲁棒性（运动模糊、相机位姿误差、零样本场景流）与模块化 SLAM/场景流的补充方法。每篇论文按“研究问题—核心方法—关键实验结论”严格压缩为 4–6 句；方法类别每类保留 3–5 篇具有代表性的工作。最后总结实验共性结论，并给出 2025 年前后的可验证趋势与挑战预测。文中仅引用公开发表或 arXiv 的真实论文/资料（见参考文献）。

方法分类与代表作  
A. 隐式/射线投射为主的动态 NeRF 系列（implicit, ray-marching）  
- D-NeRF (Pumarola et al., CVPR 2021) — 问题：如何用 NeRF 表征随时间变化的场景并合成任意时间的新视图；方法：在 NeRF 的体积渲染管线中引入时间相关的变形场/隐变量（deformation field）使体素随时间变形并联合训练；结论：能在合成动态场景上生成时间一致的新视图，但对大幅形变、多视角稀疏或单目采集下的拓扑变化敏感，训练与推理成本高，且逆向映射（backward-flow）在单目下难以稳健收敛。  [openaccess.thecvf.com](https://openaccess.thecvf.com/)  
- Nerfies (Park et al., ICCV 2021) — 问题：处理具有拓扑变化或大幅变形的动态对象；方法：通过在高维（latent time）空间对 NeRF 做扩展并学习 per-point deformation field 与 appearance embedding；结论：能处理拓扑变化且提供更连贯的形变建模，但仍受逆向映射与多视几何稀疏性限制，单目数据下泛化受限。  [openaccess.thecvf.com](https://openaccess.thecvf.com/)  
- Tensor4D / K-planes / Hexplane 等（代表性：Tensor4D, CVPR 2023） — 问题：提高动态 NeRF 的效率以靠近实时或大尺度序列应用；方法：将 4D（空间×时间）分解为张量或平面集合以替代 MLP，显著减少内存与采样代价；结论：在多视角或结构化数据上大幅加速训练与渲染，但对单目、遮挡与不准位姿场景的稳健性仍是瓶颈。  [telecomsci.com（综述收录）](https://www.telecomsci.com/zh/article/doi/10.11959/j.issn.1000-0801.2025152/)  

B. 光栅化 / 3D 高斯泼溅（Gaussian Splatting）路线（显式/半显式、实时友好）  
- 3D Gaussian Splatting (Kerbl et al., ACM TOG 2023) — 问题：能否用面向光栅化的显式粒子表示达到实时且高质量的神经渲染；方法：用可微的 3D 高斯（位置、协方差、SH 颜色 coeffs）构成紧凑点云并在 CUDA 光栅化管线中做高效合成（splatting + densification）；结论：在多目高质量场景上实现了与 NeRF 比肩甚至更快的渲染（接近实时），为后续将高效显式表示扩展到动态场景奠定了工程基础。  [dl.acm.org](https://dl.acm.org/)  
- Dynamic / 4D Gaussian Splatting (CVPR/3DV 2024 系列) — 问题：如何将 3D 高斯表示扩展到随时间变化的动态场景；方法：引入时间维度、每粒子时间参数化或为每帧维护粒子集，并采用流场/跟踪机制保证时间一致性；结论：在多目动态视频上达到了实时或近实时的新视角渲染，证明显式高斯结合光栅化更易工程化以满足速度/质量平衡，但原始多目设定下的鲁棒性与单目泛化问题残存。  [telecomsci.com（综述收录）](https://www.telecomsci.com/zh/article/doi/10.11959/j.issn.1000-0801.2025152/)  
- Deformable 3D Gaussians for Monocular Dynamic Reconstruction (Zhejiang Univ. / Deformable-GS, CVPR 2024 / arXiv:2309.13101) — 问题：单目视频场景下如何同时实现高保真渲染与鲁棒几何恢复；方法：首次将显式的 3D 高斯视为规范空间实体（由 COLMAP / 随机点云初始化），并学习一个前向变形场（forward-flow）把规范高斯映射到观测空间，用光栅化可微化管线联合优化高斯属性与变形场，同时用“退火平滑训练（AST）”缓解单目位姿不准带来的训练不稳；结论：在 D-NeRF 合成集和若干真实单目序列上相较 NeRF 系列提升显著（PSNR 增益、时间插值平滑度与实时渲染帧率），表明基于光栅化的前向变形与高斯表示对单目动态重建有明显优势。  [arxiv.org](https://arxiv.org/abs/2309.13101) ；【解读与报道】[eet-china.com](https://www.eet-china.com/mp/a297533.html)  
- MoDGS / 4D-Rotor / GauFRe 等近期工作（2024–2025）尝试将高斯泼溅在“随意单目采集”、事件/模糊场景、以及更紧凑的实时 streaming 中推广——共同思路是把显式高斯与可微化的配准/变形域耦合，从而兼顾质量与速度。  [telecomsci.com（综述收录）](https://www.telecomsci.com/zh/article/doi/10.11959/j.issn.1000-0801.2025152/)  

C. 单目场景流与鲁棒性（补充类：为单目重建提供运动/几何先验）  
- Neural Scene Flow Fields (NSFF, Li et al., CVPR 2021) — 问题：如何把场景流（场景级 3D 位移）与时空视图合成耦合；方法：学习点到点的时间依赖流场并与颜色/不透明度联合建模以合成任意时刻视图；结论：在多视视频上为动态合成与几何恢复提供了有效时空约束，但对单目稀疏采样不够稳健。  [openaccess.thecvf.com](https://openaccess.thecvf.com/)  
- DyBluRF (动态模糊鲁棒 NeRF, CVPR 2024 / DyBluRF) — 问题：单目视频中存在运动模糊时如何恢复动态 NeRF；方法：将模糊成像模型整合到辐射场训练中，通过显式建模曝光内运动（或隐变量）对抗帧间模糊；结论：在含运动模糊的单目序列上比不建模模糊的方法在渲染保真度与时间一致性上更稳健。  [telecomsci.com（收录）](https://www.telecomsci.com/zh/article/doi/10.11959/j.issn.1000-0801.2025152/)  
- Zero-Shot Monocular Scene Flow Estimation in the Wild (Liang et al., 2025, arXiv:2501.10357) — 问题：能否训练出泛化到“野外单目视频”的场景流估计器而无需每域标注；方法：联合几何与运动的参数化设计、合成大规模训练集与特征化的参数化策略（zero-shot pipeline）；结论：在 DAVIS 等任意视频集与机器人操作场景上展示了零样本泛化能力，提示“通用单目场景流”在为单目动态重建提供运动先验方面可行。  [arxiv.org](https://arxiv.org/abs/2501.10357)  

D. 单目 SLAM / 动态 SLAM 与分割先验（实践性模块）  
- DynaSLAM / DynaSLAM2 等（动态物体识别并去除/插值）— 问题：在同时定位与建图（SLAM）系统中，如何处理动态目标以不破坏全局地图；方法：结合语义/实例分割（Mask R-CNN 等）与多视几何做动态掩蔽与地图修补；结论：在实际单目/RGB-D SLAM 中能显著降低位姿漂移，但对遮挡、类别未见样本与单目稀疏跟踪仍有限。 （代表性实现被多项工程化系统采用）  [相关综述与实现参见 telecomm/论文集合]  
- 单目面向动态场景的工程方案（如 ClusterSLAM、改进 ORB‑SLAM3 + 语义/YOLO 策略等）在机器人/自动驾驶的实用工件里被广泛采用，以在运行时剔除短期动态并保持实时性。 （见行业/会议实现报告）  [综述参见 hub.baai/telecomsci]  

实验与评价总结（共性结论，非逐篇复述）  
1) 质量—速度权衡：隐式 NeRF 系列（特别是基于 MLP 的变体）在表达能力与细节恢复上仍占优势，但训练/渲染代价高；显式 3D 高斯泼溅及其动态扩展在实时性与工程化上具显著优势，尤其适合需要交互帧率的应用。  
2) 单目弱可观测性：单目输入下，几何与变形的“解耦”是核心难点。直接用逆向变形（backward-flow）学习往往收敛慢且易受位姿噪声影响；采用前向变形（forward-flow）或将规范空间作为常量表示（如 Deformable 3D Gaussians）更利于单目情形的稳定优化。  
3) 对位姿/曝光/模糊的脆弱性：实际采集的相机位姿误差、时间不同步与运动模糊会显著降低隐式方法的重建质量；一类行之有效的策略是联合优化相机位姿与场景表示并在训练初期使用“退火／平滑”机制（AST）逐步引入细节。  
4) 多模态/先验的增益明显：引入场景流、外部深度/LiDAR、语义检测或置信度估计会显著提升单目动态重建的稳定性；近期工作（zero-shot scene flow、模糊鲁棒 NeRF、带置信度的匹配同步）表明把可学习的运动先验与显式几何表示结合能提升泛化与鲁棒性。  
5) 评测基准与可比性问题：目前常用的 D-NeRF、NeRF-DS、KITTI、TUM-RGB-D 等数据集各有局限（合成/真实差异、标注不一致），导致不同论文间直接比较存在困难；需要统一的单目动态基准（包含位姿噪声、模糊与遮挡）以衡量方法的实用性。

趋势与挑战（2025 年前后可验证的预测，不少于三点）  
1) 从隐式到混合显式+隐式：未来 2–3 年内，更多工作将采用“显式粒子/高斯（用于快速光栅化）+ 局部隐式细节修饰（用于高频细节/拓扑变化）”的混合架构，以在保证实时性的同时恢复细节。Deformable-GS 即为先行实例；可验证性：后续论文/代码将对比纯隐式与混合结构在单目真实序列上的速度/PSNR/LPIPS trade-off。  
2) 强化单目运动先验与零样本场景流：训练一次、跨域可泛化的单目场景流模型（zero-shot）将成为实际单目动态重建的关键模块；可验证性：未来工作会将预训练场景流器与单目重建管线耦合，展示在未见场景上的渲染与几何恢复提升。  [已出现工作示范：arXiv:2501.10357]  
3) 可微化光栅化与深度传播的普及：更多系统会公开“可微高斯光栅化”与“前向/反向深度传播”实现，推动将深度监督、逆向渲染与 SLAM/控制任务联合训练；可验证性：公开的库（CUDA kernel）与实时演示将成为研究标配（降低复现成本）。  
4) 评测体系与单目现实噪声建模标准化：为真实世界应用，社区将迫切建立包含相机位姿误差、曝光/模糊、遮挡与稀疏采样的标准基准与度量（不仅是 PSNR/SSIM/LPIPS，还包含几何一致性与下游任务指标）；可验证性：新基准数据集与 leaderboards 将出现并影响方法迭代方向。  
5) 事件相机 / 多模态传感器融合：对于高速运动与低光场景，活动相机（event camera）与单目 RGB 的融合被证明能显著抑制模糊导致的信息丢失；可验证性：近期预印本/会议投稿已开始以事件引导的高斯泼溅或 NeRF 增强高速区域细节，预计两年内进入主流会场。  [相关方向已有稿源与项目在涌现（见 chatpaper 条目汇总）]

结论  
2022–2025 年间，动态场景重建领域呈现两条清晰且互补的发展轨迹：一方面，隐式 NeRF 系列继续推进表达能力與时空一致性，另一方面，以 3D 高斯泼溅为代表的显式/光栅化方案在实时性与工程化上取得突破，且经由“前向变形 + 可微光栅化”策略成功将高质量渲染带入单目动态重建场景。单目输入下的核心科学问题仍围绕“弱可观测性”与“位姿/模糊/遮挡的鲁棒性”；未来工作需要把泛化的场景流/运动先验、可微化渲染核与统一的评测体系结合起来，以推动从实验室原型向可部署系统的过渡。

参考文献（不少于 12 篇，按文中出现或讨论顺序）  
注：下列条目为公开论文、会议或 arXiv 资料；若有会议版/期刊版并存，优先给出公开版链接或 arXiv。  
1. Mildenhall, B., Srinivasan, P. P., Tancik, M., et al., “NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis,” ECCV 2020; arXiv:2003.08934. [arxiv.org](https://arxiv.org/abs/2003.08934)  
2. Pumarola, A., Agudo, A., et al., “D-NeRF: Neural Radiance Fields for Dynamic Scenes,” CVPR 2021. [openaccess.thecvf.com](https://openaccess.thecvf.com/)  
3. Park, K., Sinha, U., et al., “Nerfies: Deformable Neural Radiance Fields,” ICCV 2021. [openaccess.thecvf.com](https://openaccess.thecvf.com/)  
4. Park, K., et al., “HyperNeRF: A Higher-Dimensional Representation for Topologically Varying Neural Radiance Fields,” ACM TOG 2021. [dl.acm.org](https://dl.acm.org/)  
5. Li, Z., Niklaus, S., Snavely, N., et al., “Neural Scene Flow Fields for Space-Time View Synthesis of Dynamic Scenes,” CVPR 2021. [openaccess.thecvf.com](https://openaccess.thecvf.com/)  
6. Shao, R.-Z., et al., “Tensor4D: Efficient Neural 4D Decomposition for High-Fidelity Dynamic Reconstruction and Rendering,” CVPR 2023. [openaccess.thecvf.com](https://openaccess.thecvf.com/)  
7. Kerbl, F., Kopanas, G., Leimkühler, T., et al., “3D Gaussian Splatting for Real-Time Radiance Field Rendering,” ACM Transactions on Graphics (TOG) 2023 (SIGGRAPH). [dl.acm.org](https://dl.acm.org/)  
8. (Dynamic / 4D Gaussian Splatting series) — “4D Gaussian Splatting for Real-Time Dynamic Scene Rendering” / “Dynamic 3D Gaussians” (CVPR/3DV 2024 会务论文集与收录综述；见综述收集)。 [telecomsci.com（综述收录）](https://www.telecomsci.com/zh/article/doi/10.11959/j.issn.1000-0801.2025152/)  
9. Yang, Z., et al., “Deformable 3D Gaussians for High-Fidelity Monocular Dynamic Scene Reconstruction,” CVPR 2024 / arXiv:2309.13101. [arxiv.org](https://arxiv.org/abs/2309.13101)；报导解读 [eet-china.com](https://www.eet-china.com/mp/a297533.html)  
10. (DyBluRF 类) “DyBluRF: Dynamic Neural Radiance Fields from Blurry Monocular Video,” CVPR 2024（相关论文/预印本与综述收录见 2025 年综述条目）。 [telecomsci.com（综述收录）](https://www.telecomsci.com/zh/article/doi/10.11959/j.issn.1000-0801.2025152/)  
11. Liang, Y., Badki, A., Su, H., Tompkin, J., Gallo, O., “Zero-Shot Monocular Scene Flow Estimation in the Wild,” 2025, arXiv:2501.10357. [arxiv.org](https://arxiv.org/abs/2501.10357)  
12. Lin, J., “Dynamic NeRF: A Review,” (综述，2024) — 汇总动态 NeRF/3D 高斯泼溅等技术发展的综述条目（用于横向比对背景）。 [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/0e2927a9-752c-47cb-a7c8-98f9703778fc)  
13. Lu Ping, Sun Junjie, Li Wan, et al., “基于神经表达的动态场景重建综述,” 电信科学, 2025 — 系统综述动态场景重建两大类方法并列举数据集/评测指标（收录大量 2022–2024 年工作）。 [telecomsci.com](https://www.telecomsci.com/zh/article/doi/10.11959/j.issn.1000-0801.2025152/)  
14. Chatpaper / 文献汇总条目（PanoSSC、MoDGS、Event‑guided extensions 等近期工作索引）——用于追踪 2024–2025 年提交与预印本动态。 [chatpaper.com](https://chatpaper.com/)  

（注）第 2、3、6、8、10、14 项中列出的会议/综述条目指向社区公开的论文页面或综述索引；若需逐篇 DOI/作者/会议信息的逐条原文链接，可据上述索引进一步展开（本文受篇幅限制以综述与代表作索引为主）。

— 结束 —