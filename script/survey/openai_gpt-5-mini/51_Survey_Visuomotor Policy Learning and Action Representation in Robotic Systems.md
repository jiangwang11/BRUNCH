引言  
随着感知模型与生成模型在计算能力和数据规模上的快速发展，近三年（2022–2025）视觉—运动（visuomotor）策略学习与动作表示方向出现两条显著路线：一是将扩散/生成模型直接作为动作/轨迹生成器以表达多模态、高维动作序列；二是基于大规模视觉-语言-动作（VLA）预训练与后训练，把“通用能力 + 小样本/强化微调”作为落地实机的主流范式。本综述围绕这两条路线以及与三维表示、双手/迁移学习和在线微调相关的代表性工作作分类评述，重点比较研究问题、方法要点与关键实验结论，并在最后给出面向 2025 年前后的可验证趋势与挑战预测。文中所引均为顶会/顶刊或 arXiv 的真实论文或项目页（详见参考文献）。

方法分类与代表作（每类 3–5 篇，简介 4–6 句）
A. 扩散/生成式动作策略（Trajectory-as-Generation）
- Diffusion Policy — Chi et al., arXiv (Diffusion Policy)  
  研究问题：行为克隆中动作分布多模态与序列一致性难题。  
  核心方法：将 policy 建模为条件去噪扩散过程（DDPM/score-based），在动作空间上以随机 Langevin/去噪迭代生成整段动作序列，并结合滚动时域控制与视觉 conditioning。  
  关键实验结论：在多基准（仿真 + 真实）15 个任务上平均性能显著优于多种基线，优势来源于对多模态动作的自然表达、对高维动作序列的可扩展性和训练稳定性；并通过 DDIM 减少推理步实现接近实时控制。[arxiv.org](https://arxiv.org/abs/2303.04137), [blog.csdn.net](https://blog.csdn.net/qq_33673253/article/details/142553377)

- 3D Diffusion Policy (DP3) — Ze et al., RSS 2024 / project  
  研究问题：在稀少演示下如何提升视觉模仿在多任务与跨域（视角/实例）上的泛化。  
  核心方法：将动作扩散策略与紧凑的 3D 视觉表示（稀疏点云 + 高效点编码器）结合，条件化去噪网络接入 3D 特征以生成动作轨迹。  
  关键实验结论：在 72 个仿真任务与若干真实任务上展示了显著的数据效率（少量演示即可成功）与泛化改进，表明 3D 表示能与扩散生成机制协同减少演示需求。[hub.baai.ac.cn](https://hub.baai.ac.cn/paper/218b0ac1-fc3d-4759-9e39-e0c6c1e79f07)

- AdaManip (用在适应性铰链物体上的扩散/3D 策略) — ICLR 2025（环境 + 策略）  
  研究问题：铰链/带内部（不可见）状态的物体需要适应性策略（失败尝试后调整），如何在仿真和现实中模拟并学习该能力。  
  核心方法：构建含 5 类适应机制的 AdaManip 仿真库，并采用基于 3D 视觉的扩散策略学习适应性示范轨迹以获得多峰初始策略与历史驱动的自我修正能力。  
  关键实验结论：在该环境及若干真实物体上，基于适应性示范 + 扩散策略的管道在处理不可见内部机制时，比静态示范/非适应基线更能恢复失败并完成任务（仿真 + 真实验证）。[hub.baai.ac.cn](https://hub.baai.ac.cn/view/43812)

B. 视觉—语言—动作（VLA）与视频条件策略（Foundation + Fine-tune）
- RT-2 (RT-2: vision-language-action models) — Brohan et al., CoRL/technical reports 2023  
  研究问题：如何把大规模网络（网络/文本-图像知识）迁移到机器人控制以获得零样本/少样本能力。  
  核心方法：基于大型视觉—语言预训练，构建可接受指令并直接产生命令的视觉—语言—动作模型，强调通过大规模数据与属性对齐来获得泛化。  
  关键实验结论：RT-2 展示了从网络/文本知识向机器人能力迁移的可行性，在若干下游任务中显著提升零/少样本表现，表明 VLM 知识可为物理策略提供有用先验。（见相关综述/引用）[ConRFT 引用处](https://17aitech.com/?p=40230)

- Vid2Robot — Jain et al., 2024  
  研究问题：直接从人类演示视频推断并执行对应机器人动作（video → action）的可行性。  
  核心方法：构建视频条件化的跨注意力 transformer，把提示视频特征与当前视觉观测融合以直接生成动作序列，同时用对比式辅助损失对齐人类/机器人表示。  
  关键实验结论：在真实机器人上，使用人类演示视频作为条件时，比其他视频条件策略在若干任务上提升约 20%（定量评测），并显现出长时依赖的迁移能力。[hub.baai.ac.cn](https://hub.baai.ac.cn/paper/9c5d6525-4b29-40a1-8da2-cbf980be7ecc)

- WorldVLA — 阿里达摩院 & 浙大 (WorldVLA, 2025 arXiv)  
  研究问题：如何把动作模型与世界模型统一起来以实现图像预测与动作生成的互助提升。  
  核心方法：将视觉/文本/动作编码为统一 token，采用自回归生成同时预测未来图像与动作，并提出注意力掩码策略减少长期自回归错误传播。  
  关键实验结论：在动作-图像联合建模上优于独立模型，表明世界模型信息能改善动作生成的长期一致性与物理可行性。[ai-bot.cn](https://ai-bot.cn/worldvla)

C. 三维/构型表示与铰接物体操作（3D 表示驱动的策略）
- VAT-MART — ICLR 2022 (Visual Action Trajectory proposals for 3D articulated objects)  
  研究问题：如何为 3D 铰链对象生成可操作的动作轨迹候选。  
  核心方法：学习基于三维形状的动作轨迹 proposal（affordance-like）用于下游操控规划。  
  关键实验结论：在若干 3D 铰链基准上提升了动作候选质量，为后续“基于 3D 表示的策略”提供重要工程模块。（见 AdaManip 引用）[hub.baai.cn 引用处](https://hub.baai.ac.cn/view/43812)

- AdaAfford — ECCV 2022  
  研究问题：少次交互下如何自适应调整对 3D 铰链物体的操控 affordance。  
  核心方法：通过少量交互学习对可操作部件的 affordance 并适配到新实例。  
  关键实验结论：在 few-shot 适应性操作上优于静态 affordance 方法，表明少量交互数据可显著改进 3D 操作泛化。[hub.baai.cn 引用处](https://hub.baai.ac.cn/view/43812)

- 3D Diffusion Policy (DP3) — 上述 DP3 同时也属于此类（用 3D 表示提升数据效率与泛化）。[hub.baai.ac.cn](https://hub.baai.ac.cn/paper/218b0ac1-fc3d-4759-9e39-e0c6c1e79f07)

D. 动作表示、迁移与双手/技能组合（Transfer / Fine‑tuning / Consistency）
- AnyBimanual — Lu et al., arXiv (Dec 2024)  
  研究问题：如何把单手策略迁移到通用双手操控以降低双手数据采集成本。  
  核心方法：技能管理器动态调度单手技能原语并用视觉对齐器缩减感知差异，结合少量双手演示进行线性/补偿组合以表示双手动作。  
  关键实验结论：在 RLBench2 和若干真实任务上显示，用少量双手示范即可把单手策略高效迁移至双手任务，成功率与样本效率均有改善。[chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/88436)

- ConRFT (Consistency-based Reinforced Fine-tuning) — Chen et al., arXiv / RSS 2025  
  研究问题：预训练 VLA 模型在真实机器人上微调时，如何兼顾安全性与样本效率。  
  核心方法：两阶段（离线 Cal-QL + 在线 HIL）强化微调框架，采用一致性策略（consistency policy）作为动作头并保留 BC 正则以防发散；在线阶段引入 human‑in‑the‑loop 干预以保障安全。  
  关键实验结论：在 8 个真实任务上少量在线微调（几十分钟）后显著提升 VLA 下游成功率并缩短轨迹长度，说明一致性策略 + 离线预训练对真实机器人微调非常有效。[17aitech.com](https://17aitech.com/?p=40230)

- Cal‑QL / Consistency Policy (相关方法引用)  
  研究问题：离线预训练与在线微调如何协同避免分布移位与不稳定性。  
  核心方法：Cal‑QL（校准的离线‑在线 RL 预训练）与 consistency policy（用流 ODE 类方法做轻量采样映射）被用于提高 Q 函数鲁棒性与推理效率。  
  关键实验结论：在少样本/安全受限场景下，这类技术能显著减少在线采样需求并提高微调稳定性（见 ConRFT 的实证比较）。[17aitech.com](https://17aitech.com/?p=40230)

实验与评价总结（跨工作共性结论，禁止逐篇复述）
1) 多模态动作与序列一致性：以往单步回归/MDN/GMM 方法在多峰轨迹与轨迹级一致性上普遍受限；以扩散为代表的生成式轨迹模型天然能通过随机初始化与采样过程表达多模态，同时通过序列级生成减少时序抖动（jitter）——这是其在现实任务中表现优异的共同机制（见 Diffusion Policy / DP3 / AdaManip）。  
2) 3D 视觉表征的重要性：将稀疏点云或 3D 表示用于条件化策略（DP3、VAT‑MART、AdaAfford）能在少样本设置显著提升泛化（视角、实例与外观变化），说明几何先验对具身操作比二维图像特征更具样本效率。  
3) 预训练 + 高效微调成为可重复落地的范式：大规模 VLA 预训练（RT‑2、WorldVLA、Pi0 等方向）提供了“通用感知—语言—动作”先验，结合离线校准（Cal‑QL）与一致性/BC 正则的在线微调（ConRFT）可在真实机器人上以有限交互快速收敛并保证安全。  
4) 推理效率 vs 表达力的权衡：扩散/生成模型在表达力上占优，但原生采样步数与延迟问题限制高频控制；DDIM/采样加速及 consistency policy 式轻量采样是当前减少推理延迟的主要方向。  
5) 评测基准与实验报告的一致性问题：不同工作使用的任务集、成功判据、动作空间（位置 vs 速度）差异较大，导致横向比较仍困难；许多论文为真实机器人提供视频/项目页，但可复现性仍需统一基准推动。

趋势与挑战（面向 2025 年前后、不少于 3 点）
1) 模型架构走向“混合生成 + 轻量采样”实用化：扩散模型将与更高效的采样方案（DDIM、预测-校准混合、consistency 映射）以及局部优化（短 horizon MPC）结合，以满足 10–100 ms 级控制需求。  
2) 3D 表示与多模态感知成为样本效率核心：稀疏点云、神经场（NeRF-lite）与触觉/力觉融合会成为降低演示需求与提升跨视角泛化的主流方向；同时三维感知将被更紧密地集成到策略条件化流程。  
3) VLA 基座模型的“安全可控微调”成为工程常态：预训练 VLA 提供强先验，但现实部署要求少量在线微调 + 人在环监督（HIL）与基于一致性的正则化（如 ConRFT）来保证行为稳定与安全。  
4) 迁移学习与技能组合（零-shot 组合/插拔技能）会优先解决双手与复杂工具操作问题：以 AnyBimanual 为代表的技能调度/视觉对齐方法将扩展为更泛的“技能库 + 管理器”框架，降低多臂数据需求。  
5) 评测套件与复现性法规化：社区需推出统一的真实-仿真混合基准（包含铰链、流体、双手与碰撞安全指标），并要求公开低延迟推理配置与安全策略以促成可比实验。  
6) 理论与控制结合的深入：对扩散策略与最优控制（LQR/非线性控制）的数学联系将被进一步解析，用以构造带稳定性证据的策略架构和推理调度。

结论  
2022–2025 年间，visuomotor 研究从“单步回归与局部策略”快速转向“生成式轨迹建模 + 大规模 VLA 先验 + 3D 表征”的混合范式。扩散类模型在表达多模态、高维动作序列上提供了实证优势；而 VLA/视频条件与 3D 表征路线则通过强先验与几何信息大幅降低实际演示需求。面向落地，关键瓶颈仍是推理延迟、评测可比性与真实环境下的安全微调；相应的研究焦点将在“高效采样 + 3D 感知融合 + 安全微调策略”上展开。研究者与工程团队应同时关注方法表达力与实际控制约束（实时性、安全性、复现性），以推动这些新方法在日常操作场景中的可靠部署。

参考文献（按出现顺序列出，均为真实论文/项目页，按域名引用原文或项目页）
- [arxiv.org] Diffusion Policy: Visuomotor Policy Learning via Action Diffusion — Cheng Chi et al., arXiv:2303.04137. https://arxiv.org/abs/2303.04137  
- [blog.csdn.net] 多篇中文精读与实施笔记（Diffusion Policy 汇总）— 示例整理页面。https://blog.csdn.net/qq_33673253/article/details/142553377  
- [hub.baai.ac.cn] 3D Diffusion Policy: Generalizable Visuomotor Policy Learning via Simple 3D Representations — DP3（论文/项目页）。https://hub.baai.ac.cn/paper/218b0ac1-fc3d-4759-9e39-e0c6c1e79f07  
- [hub.baai.ac.cn] Vid2Robot: End-to-end Video-conditioned Policy Learning with Cross-Attention Transformers — Jain et al., 2024（论文摘要/项目页）。https://hub.baai.ac.cn/paper/9c5d6525-4b29-40a1-8da2-cbf980be7ecc  
- [chatpaper.com] AnyBimanual: Transferring Unimanual Policy for General Bimanual Manipulation — Lu et al., arXiv (Dec 2024).https://chatpaper.com/chatpaper/zh-CN/paper/88436  
- [17aitech.com] ConRFT: A Reinforced Fine-tuning Method for VLA Models via Consistency Policy — Chen et al., arXiv / RSS 2025 (综述/解读页，含 arXiv 链接与代码页引用).https://17aitech.com/?p=40230  
- [ai-bot.cn] WorldVLA – 自回归动作世界模型（阿里达摩院/浙大，arXiv 2025 项目页）。https://ai-bot.cn/worldvla  
- [hub.baai.ac.cn] AdaManip: Adaptive Articulated Object Manipulation Environments and Policy Learning — ICLR 2025 综述/项目页。https://hub.baai.ac.cn/view/43812  
- [hub.baai.ac.cn] VAT‑MART / AdaAfford 等在铰链物体操作方向的重要参考（见 AdaManip 参考列表）— VAT‑MART (ICLR 2022)、AdaAfford (ECCV 2022)（项目与引用汇编）。https://hub.baai.ac.cn/view/43812  
- [hub.baai.ac.cn] 3D Diffusion Policy (DP3) project page（重复指向以便查阅实现细节与视频）。https://hub.baai.ac.cn/paper/218b0ac1-fc3d-4759-9e39-e0c6c1e79f07  
- [chatpaper.com] Survey of Vision-Language-Action Models for Embodied Manipulation — Li et al., arXiv 2508.15201（综述，汇总 VLA 发展）。https://chatpaper.com/zh-CN/chatpaper/paper/182383  
- [hub.baai.ac.cn] 其他相关工作与实现注解（Vid2Robot、DP3、AdaManip 的细节、视频与代码链接汇总）。https://hub.baai.ac.cn

（注：上文所述论文、项目与综述均有对应的 arXiv / 会议页或项目页；为便于查阅，参考文献列表以能直接访问论文/项目总结的公共页面为主。若需我把每项参考替换为其原始 arXiv/会议 DOI 链接列表，我可以按需补充。）