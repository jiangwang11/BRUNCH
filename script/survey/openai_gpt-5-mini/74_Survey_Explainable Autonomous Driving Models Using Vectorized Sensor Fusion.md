引言  
本综述聚焦“基于向量化表征的传感器融合（vectorized sensor fusion）在可解释自动驾驶模型中的应用”，覆盖 2022–2025 年的代表性工作。向量化表征（如 BEV 网格、矢量化高精地图元素、基于高斯/向量的空间原语）已经成为把多模态（相机、LiDAR、雷达）信息映射到车辆决策可读、可审计表示的主要途径。本文按方法范式分类（BEV 统一表征、生成/修复式融合、面向矢量/地图的高阶表征、以设计/训练为主的可解释范式），在每类挑选 3–5 篇代表作进行精炼介绍，随后总结实验共性、存在的可解释性瓶颈，并给出 2025 年前后的研究趋势预测。为保证可检索性，文内每篇工作后均给出检索链接（来源为已公开的论文/技术报告或权威汇总页面）。

方法分类与代表作  
一、BEV（Bird’s‑Eye‑View）统一表征的融合（以场景级、格网/张量 BEV 为中心）  
- BEVFusion (MIT, ICRA 2023 / arXiv 2022) — 将相机与 LiDAR 特征统一到共享 BEV 表示空间，重点贡献是高效的 camera→BEV 视图变换（优化的 BEV pool 内核）与一个全卷积 BEV 编码器用于融合与下游多任务（检测/分割）。核心方法：分别提取模态特征后，用预测的离散深度分布将相机功能“抛洒(splat)”到 BEV 网格，再与沿 z 展平的 LiDAR BEV 特征按元素级拼接并用卷积精细对齐。实验结论：在 nuScenes 上兼顾检测与 BEV 地图分割，两模态融合显著提升语义密集任务（如 BEV 分割），并通过视图变换加速实现接近实时的推理。[blog.csdn.net](https://blog.csdn.net/weixin_62497890/article/details/133708937)

- BEVFusion (ADLab‑AutoDrive / NeurIPS‑variant, arXiv 2022) —（与上条同名但不同实现/思想流派）提出并评估了一套稳健的 LiDAR‑camera 并行流水线，强调相机流程不依赖 LiDAR 输入以提高故障鲁棒性与可解释性（模态独立可单独审查）。核心方法：并行图像流与点云流各自产生 BEV，再在 BEV 级融合；设计上保留每模态的独立预测头以便决策追踪与故障诊断。实验结论：在多种点云退化条件下，分支独立性带来更强的故障容错与可追溯的决策来源判别能力。[blog.csdn.net](https://blog.csdn.net/qq_44799766/article/details/136836260)

- Transfusion / 类 BEV‑based works（代表性融合改进与 BEV 表示扩展） — 若干后续工作（参见 BEV 系列实现笔记）表明：将多模态特征先投射到统一 BEV 能把“几何证据（来自 LiDAR）”与“语义证据（来自相机）”分离呈现，便于把回归（几何）与分类（语义）责任在不同子模块中分配，从而增强模型内部可解释性与审计路径（即“哪一模态提供了哪个证据”）。这些实现细节与工程化经验多见于开源实现与复现报告。[blog.csdn.net](https://blog.csdn.net/zzw2002/article/details/133... )

二、生成/修复式融合与概率化表征（增强鲁棒性并提供置信/不确定性）  
- DifFUSER (ECCV/ArXiv 2024) — 提出用潜空间扩散（latent diffusion）作为跨模态融合器，利用扩散的去噪/细化能力在传感器失效或缺损时“补全”或修复模态特征，提升融合鲁棒性。核心方法：在 BiFPN 风格的层级结构中串联 diffusion blocks（cMini‑BiFPN），并引入门控自条件调制（GSM）与 Progressive Sensor Dropout Training（PSDT）以增强对传感器失效的健壮性。实验结论：在 nuScenes 的 BEV 分割与 3D 检测任务中，扩散融合在传感器遮挡/丢失场景下，比常规模态注意力融合保持更高的 mIoU 与检测鲁棒性；同时扩散模块可输出概率化不确定性度量，利于可解释性和风险评估。[zhuanzhi.ai](https://www.zhuanzhi.ai/paper/6b0a491c9f81292104d4bc42d23de3cf)

- GaussianFusion (arXiv 2025) — 提出用二维高斯（2D Gaussians）作为稠密但紧凑的空间原语，对场景用一组带显式物理属性（位置、尺度、旋转）与隐式/显式特征的高斯进行参数化，并通过交叉注意力与迭代细化把多模态观测整合到高斯集合中，用于端到端轨迹/规划与地图推断。核心方法：初始化均匀高斯集合、用点/像交叉注意力更新显式与隐式特征，再用高斯解码器（概率叠加）生成地图与轨迹；输出是可解释的高斯集合（便于逐个原语验证）。实验结论：用高斯集合作为向量化场景表征能直接用于级联规划头和地图重构，提供了一种兼顾稠密语义与可审计物理属性的中间表示。[blog.csdn.net](https://blog.csdn.net/weixin_45657478/article/details/148632173)

- GGS / Gaussian‑splatting（可泛化 3D Gaussian splatting，arXiv 2024–2025） — 在视点合成/渲染领域提出用高斯溅射（Gaussian splatting）生成逼真新视图的可泛化方法（加入邻域深度细化与扩散损失用于虚拟车道构造）。相关技术被移植到自动驾驶合成与数据增强（生成可解释的虚拟视角、用于训练/检验感知模块）。实验结论：高斯溅射在大视角变化下能提高新视图合成质量，从而为训练时的模态一致性检测与可解释性校验提供工具。[blog.csdn.net](https://blog.csdn.net/weixin_45657478/article/details/145860370)

三、面向矢量化/地图输出的多模态融合（直接产出可解释的矢量地图要素）  
- SuperFusion (ICRA 2024 / arXiv 2022) — 目标是长距离高精 HD 地图生成，提出多层次融合（数据级用于深度估计、特征级用于远距 LiDAR BEV 预测、BEV 级对齐用于最终融合），并设计了跨尺度对齐与流场 Δ 用于特征对齐。核心方法：图像引导的深度估计 + 图像引导的远距 LiDAR BEV 预测，再在 BEV 层对齐并融合得到高精地图元素（车道线、人行道等）。实验结论：多层次融合在长距离（90m）HD 地图语义分割上显著超越单模态与简单融合基线，且输出本身为地图要素，有利于后续规划的可解释审查。[blog.csdn.net](https://blog.csdn.net/qq_41204464/article/details/136723582)

- 其他面向矢量化输出的尝试（如基于 anchor 的级联规划与矢量高斯解码器）表明：把输出设计为矢量原语（线段、曲线、轨迹、带属性的高斯）能直接为可解释性审计（“该地图元素源自哪些模态/哪些特征”）提供明确路径；系统可以回溯到产生该矢量元素的高斯/BEV 单元，从而支持证据链检查与人工校验。[blog.csdn.net](https://blog.csdn.net/weixin_45657478/article/details/148632173)

四、以设计与训练原则提高可解释性的范式（结构性约束、责任分离、数据增强）  
- Detecting As Labeling (DAL, ECCV 2024) — 从“数据标注过程”出发提出范式性原则：回归（几何）应仅依赖 LiDAR（标签由 LiDAR 生成），而相机特征用于候选产生与分类，从而把“谁负责提供回归证据”作为结构性设计约束以降低过拟合与提高可解释性。核心方法：密集→稀疏管道（图像与点云 BEV 融合产生热图），但在稀疏细化阶段回归只用点云特征；并提出 BEVPoolV2 等工程优化以提升视图变换效率；还引入速度增强等数据合成策略。实验结论：按“标注即检测”原则解耦回归与分类后，能在标准基准上同时改善泛化（跨域表现）与速度/精度权衡，并使得回归证据来源可追溯，利于审计与解释。[chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/99733)

- 数据级/训练级的可解释性手段（传感器 dropout、模态专用损失、辅助分类任务）——这些做法在多个工作中被证明能把模型行为的“失败模式”限定到某些可枚举情形，从而便于解释和后验修正（例如 DifFUSER 的 PSDT、DAL 的速度增强）。若干实证结果显示：强制模态责任分离或引入显式不确定性输出，会牺牲一点端到端单点最优性能但换来更可审计、更稳定的失败模式。

实验与评价总结（共性结论，仅列共性）  
1) 统一 BEV/矢量化中间表示有利于可解释性：把多模态原始观测投射到共享 BEV 或矢量原语集合，使“证据→表示→决策”的链路变得可追溯（例如可标注哪些 BEV 格点或哪些高斯对某个检测/地图元素贡献最大）。多篇工作均通过可视化 BEV 激活或高斯权重来辅助人工诊断。  
2) 责任分离（Regression vs. Classification）增强审计能力：将几何回归限制为以 LiDAR 为主的子模块而相机承担语义增强/分类，能减少图像域增强对回归产生的隐式偏移，从而使回归结果的来源更清晰（DAL 的核心发现）。  
3) 概率化与生成式融合能输出置信/不确定性度量：使用扩散/高斯等概率化模块（DifFUSER、GaussianFusion）能在缺传感器或遮挡时给出可解释的置信分布，便于风险估计与决策保守化。  
4) 可解释性与效率存在权衡：更可解释的结构（模态独立分支、显式高斯原语、概率化模块）往往伴随更复杂的计算或更高的内存/推理成本；工程优化（如 BEVPoolV2、专用 GPU 内核）是可解释化实用化的必要条件。  
5) 评测缺口：当前基准（如 nuScenes）强调检测/分割指标，但缺少统一的“可解释性评价”指标（例如证据来源可追溯性、解释一致性、决策可证性），这限制了可解释方法的横向比较。

趋势与挑战（2025 年前后预测，基于上述作品与共性结论）  
1) 从像素/点到“可核验矢量原语”的范式将常态化：研究将更倾向于把输出设计为带物理/语义属性的矢量原语（线段、曲线、高斯原语、轨迹锚等），因为这直接支持验证、人工介入与功能审计。  
2) 生成式融合（扩散/高斯）将成为鲁棒性与可解释性的主力：扩散模型、概率化高斯参数化不仅能修复缺失模态，还能提供自然的置信度度量；未来会有更多工作把这些概率量纳入决策合成（例如用于避险阈值和可解释告警）。  
3) 责任分离的范式化与规范化：从 DAL 类思想出发，行业/学界可能形成一套“可解释性设计准则”（例如哪些任务应仅由几何模态承担、哪些可由视觉补充），并在训练管线中默认加入模态责任约束与可审计记录。  
4) 可解释性评价基准与工具链将出现：需要开发包括证据可追溯性、一致性/反事实测试、模态干预测试等指标与自动化工具，为可解释模型提供客观对比基准。  
5) 端-边协同部署：鉴于可解释结构通常更重，工程上将更多采用“边缘轻量化感知 + 云/车端可解释诊断”的协同架构，即在边缘保证实时性、在中央保留更丰富的可解释性分析日志与推理回放。  
6) 法规/合规驱动的可解释性需求上升：随着自动驾驶产品化进程，监管会要求“决策证据链”的保存（谁、何时、基于何证据做出该决策），因此研究将更多关注模型可审计日志与人机可解释报告。

结论  
过去三年（2022–2025）多模态融合在自动驾驶中的研究已从单纯追求端到端性能，逐步转向同时追求鲁棒性与可解释性：统一 BEV 表示、概率化生成式融合、矢量化输出与责任分离设计成为主流路径。现有代表性工作分别在工程优化（BEVPoolV2 / 高效 BEV pool）、生成式修复（扩散、高斯 splatting）、以及范式性设计（DAL）上给出了可操作的思路。下一步需要构建统一的可解释性评测与工具链，将研究产出转化为合规、可审计的工程产物。

参考文献（按出现顺序列举；均为公开论文/预印本或权威汇总页面）  
1. BEVFusion: Multi‑Task Multi‑Sensor Fusion with Unified Bird’s‑Eye View Representation (MIT) — arXiv/ICRA; 2022–2023. 详见综述与实现笔记. [blog.csdn.net](https://blog.csdn.net/weixin_62497890/article/details/133708937)  
2. BEVFusion: A Simple and Robust LiDAR‑Camera Fusion Framework (ADLab‑AutoDrive) — arXiv 2022. 复现与实践笔记. [blog.csdn.net](https://blog.csdn.net/qq_44799766/article/details/136836260)  
3. Detecting As Labeling: Rethinking LiDAR‑camera Fusion in 3D Object Detection (DAL) — ECCV 2024 (paper/code); 论证回归只用 LiDAR 的设计原则与 BEVPoolV2 优化. [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/99733)  
4. DifFUSER: Diffusion Model for Robust Multi‑Sensor Fusion in 3D Object Detection and BEV Segmentation — arXiv / ECCV 2024 summary; latent diffusion 用于多模态融合与不确定性估计. [zhuanzhi.ai](https://www.zhuanzhi.ai/paper/6b0a491c9f81292104d4bc42d23de3cf)  
5. SuperFusion: Multilevel LiDAR‑Camera Fusion for Long‑Range HD Map Generation — arXiv / ICRA 2024; 多层次（数据/特征/BEV）融合用于长距 HD 地图生成. [blog.csdn.net](https://blog.csdn.net/qq_41204464/article/details/136723582)  
6. GaussianFusion: Gaussian‑Based Multi‑Sensor Fusion for End‑to‑End Autonomous Driving — arXiv 2025 (预印本); 用 2D 高斯原语做稠密但紧凑的向量化表征并用于端到端轨迹/地图输出. [blog.csdn.net](https://blog.csdn.net/weixin_45657478/article/details/148632173)  
7. GGS: Generalizable Gaussian Splatting for Lane Switching in Autonomous Driving — arXiv 2024; 高斯溅射用于新视点合成与虚拟车道生成，支持生成式数据增强与可解释合成检验. [blog.csdn.net](https://blog.csdn.net/weixin_45657478/article/details/145860370)  
8. DifFUSER / 生成式融合相关实现与讨论（扩散用于模态修复）——综述与实现笔记. [zhuanzhi.ai](https://www.zhuanzhi.ai/paper/6b0a491c9f81292104d4bc42d23de3cf)  
9. BEVFusion 系列开源实现与代码解读集合（多篇博文/复现笔记）——有助于工程化与可解释性可视化实践. [blog.csdn.net](https://blog.csdn.net/qq_45783225/article/details/131310517)  
10. BEV 感知 / BEVDet / LSS 系列技术综述与实现笔记（上下游工程化与视图变换细节）——若干实现与经验贴. [blog.csdn.net](https://blog.csdn.net/qq_44799766/article/details/136836260)  
11. PointPainting: Sequential Fusion for 3D Object Detection — CVPR 2020（早期点级融合基线，作为对比背景，说明点级与 BEV 级融合的差别）。可作为理解语义密度损失的参考。  
12. 生成式与高斯溅射相关技术综述 / 实践笔记（用于新视角合成与扩散监督）——多篇博客与 arXiv 引导材料（GGS、InnerGS 等）。[blog.csdn.net](https://blog.csdn.net/weixin_45657478/article/details/145860370)

（注：本文在方法选择上优先列举 2022–2025 年内公开并被复现/讨论的代表性工作与工程实践报告；若需论文 PDF、代码仓库或更精确的引用格式，我可按指定格式补充 DOI / arXiv 链接与代码链接。）