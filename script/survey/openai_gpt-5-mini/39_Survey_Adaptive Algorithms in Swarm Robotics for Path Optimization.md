引言  
本文综述2022–2025 年间与“群体机器人（swarm robotics）中用于路径优化的自适应算法”直接相关的代表性工作，聚焦三类技术路线：基于多智能体强化学习（MARL）的自适应规划、基于通信/数字孪生的分布式自适应与冲突解析策略，以及仿真→现实（sim-to-real）与自适应策略学习的工程化方案。评述基于公开论文、期刊/会议与 arXiv（下文均按出处给出）中可验证的实验结论与方法细节，避免笼统评价并强调可重复性的实验量化结论与适用边界。

方法分类与代表作  
A. 多智能体强化学习（MARL）与选择性通信（3–4 篇）  
1) DCCPR — Decision Causal Communication with Prioritized Resolution (Wang, Zhang 等, JEIT 2025).  
- 问题：在高密度、结构化地图中提升多智能体路径寻路成功率并降低通信开销与死锁。  
- 方法：将选择性通信（learning-based agent selection）与分层优先级冲突解决结合，采用 D3QN（dueling double DQN）作为决策引擎，并将 A* 期望路径纳入奖励以惩罚偏差与拥堵。  
- 关键结论：在多个随机/结构化地图上，论文报告相比基线方法任务成功率提升约 79%，平均回合步长（episode length）降低 46.4%，并显著降低通信频率（论文给出不同规模下 Hz 级统计）。该工作强调“选择性通信 + 分层冲突解析”在稠密场景的可伸缩性优势。[jeit.ac.cn](https://www.jeit.ac.cn/cn/article/doi/10.11999/JEIT250122)  

2) Learning selective communication for MAPF (Ma 等, IEEE RAL 2022 — 被多篇综述/论文引用)。  
- 问题：如何在部分可观测、多智能体路径任务中仅在必要时交换信息以减少带宽。  
- 方法：基于强化学习训练通信决策模块（哪些 agent、何时传输），配合局部策略网络执行动作，通信代价被嵌入回报中以实现稀疏通信。  
- 关键结论：在标准 MAPF 基准上，学习到的选择性通信策略在通信量明显减少的同时保持或略优于全通信基线的成功率，说明通信调度作为学习目标具有可训练性（详见被引用的实验结果与基准比较）。该方向被 DCCPR 等后续工作继承与扩展（选择性通信 + 冲突解析）。（见 JEIT/综述引用条目）[jeit.ac.cn](https://www.jeit.ac.cn/cn/article/doi/10.11999/JEIT250122)  

3) SCRIMP / PRIMAL 系列（Wang Yutong 等，IROS 2023；Wang 等，IEEE RAL 2019/PRIMAL2 2021 被反复引用）。  
- 问题：训练可扩展的端到端多智能体路径寻路策略（面向大规模 agent）。  
- 方法：将强化学习与模仿学习/集中学习-分散执行范式结合，提出可伸缩的通信/注意力机制与策略分解（value decomposition 或 centralized critic 架构）。  
- 关键结论：在大规模随机地图/仓储场景中，带有学习到的通信与注意力模块的框架相比纯分散或纯集中方法能在成功率与样本效率间保持更好权衡；这些方法为后续将通信选择性化和引入冲突解析的工作奠定了实践基线（相关方法与性能被 DCCPR 比较）。（相关论文见 JEIT 参考文献汇编）[jeit.ac.cn](https://www.jeit.ac.cn/cn/article/doi/10.11999/JEIT250122)  

B. 基于搜索/冲突解析与混合学习—搜索（3–4 篇）  
1) Conflict‑Based Search (CBS) 系列（Sharon 等, Artificial Intelligence 2015；后续改进 ICAPS/CBIS 等）。  
- 问题：精确求解 MAPF 的最优解与约束冲突管理。  
- 方法：对冲突进行显式分支（增加约束）并在每个子问题上运行单体最短路径搜索，形成冲突树（CT）。  
- 关键结论：CBS 在小规模或中等规模要求最优解的 MAPF 上表现出色，但在高密度大规模场景中容易遭遇扩展性瓶颈；因此近年研究聚焦于用于启发式加速、与学习启发式混合、或用于生成基线解供 MARL 微调。该系列为后续“混合学习+搜索”的设计提供了理论骨架（JEIT 与 AAS 综述中被反复引用）。[aas.net.cn](https://aas.net.cn/cn/article/doi/10.16383/j.aas.c240392?viewType=HTML)  

2) Conflict‑based increasing cost search / 层次冲突解析（Walker 等, ICAPS 2021；以及 DCCPR 的分层优先级机制）。  
- 问题：改进冲突树扩展策略以提升可扩展性并减少死锁。  
- 方法：在冲突分支中引入成本增长规则、动态优先级与轮流通行等机制以缓解循环等待与拥堵。  
- 关键结论：在高密度环境引入优先级/轮流通行能显著减少死锁与回合长度，且可与学习导向的候选解生成器耦合以弥补最优性与可扩展性的权衡。相关实验与统计见 JEIT 汇总。[jeit.ac.cn](https://www.jeit.ac.cn/cn/article/doi/10.11999/JEIT250122)  

C. 通信感知的分布式训练、数字孪生与联邦/去中心化强化学习（3 篇）  
1) 基于数字孪生的分布式协同路径规划（Tang 等, JEIT 2024）  
- 问题：如何在多自动驾驶车辆路径规划中提高跨车辆协作训练的泛化并加速向现实部署的迁移。  
- 方法：提出用数字孪生（DT）作为仿真训练平台，结合去中心化联邦强化学习（DFRL）与可信度加权节点选择（CWDFRL）来保证模型聚合质量，同时在 DT 中进行大规模交互生成经验。  
- 关键结论：仿真结果显示，相较于集中式 FL 与单车训练，DT + 去中心化可信度加权的方案能提升整体奖励、降低平均任务完成时间与碰撞概率，显著改善 sim→real 部署的转移效率。[jeit.ac.cn](https://jeit.ac.cn/cn/article/doi/10.11999/JEIT230678?viewType=HTML)  

2) 多路径智能传输策略（UAM 通信感知路由，Wang 等, Telecommunications Science 2025）  
- 问题：低空城市空域中节点高度移动性导致链路不稳定，如何保证实时控制/路径规划消息的可靠传输。  
- 方法：设计基于强化学习的多径智能路由与环境验证机制，按服务（控制/感知/媒体）动态分割数据包并自适应路由策略。  
- 关键结论：仿真表明在高动态网络下，多路径智能路由在端到端延迟与数据恢复概率上明显优于固定路径/单路径策略，为大规模空域协作中可靠通信提供了实证支持（通信层成为路径协调的关键约束）。[telecomsci.com](https://www.telecomsci.com/zh/article/doi/10.11959/j.issn.1000-0801.2025099/?viewType=HTML)  

3) 分布式自适应内模与在线自适应动态规划（Jiang 等, Acta Automatica Sinica 2025）  
- 问题：在多智能体控制任务中，如何在系统矩阵未知情形下用在线数据学习最优控制器以实现协同输出调节。  
- 方法：基于分布式自适应内模与自适应动态规划（值迭代/策略迭代），提出在线数据驱动的分布式学习算法并证明闭环稳定性与学习收敛性。  
- 关键结论：理论与仿真证明在有限通信与局部可观测下，所学控制增益能收敛到最优增益，提示在受制于通信/模型不确定性的群体机器人路径与编队控制中可以采用此类分布式自适应策略作为低层稳定控制器。该理论工作为工程化 MARL 系统提供了严格收敛与鲁棒性依据。[aas.net.cn](https://aas.net.cn/cn/article/doi/10.16383/j.aas.c240371?viewType=HTML)  

D. 仿真→现实与自适应策略学习（Sim‑to‑Real / policy learning）（3 篇）  
1) Motion Policy Networks / MπNets（NVIDIA 团队，CoRL/arXiv 2022；see NVIDIA developer blog）  
- 问题：在未知/动态场景中用单视点连续点云生成实时、平滑且避碰的机器人运动策略并直接迁移到真实系统。  
- 方法：端到端网络将点云 + 机器人状态映射到关节轨迹，使用大规模合成数据（数百万轨迹）训练并借助点云减少域差。  
- 关键结论：在密集/动态场景下对比采样/基于搜索方法（MPNet 等）显示 MπNets 在成功到达率与速度上优势（文中报告探测成功概率提升与实时闭环运行能力），证明大规模合成数据+点云输入是 sim→real 的有效实践路径。[developer.nvidia.cn](https://developer.nvidia.cn/blog/improving-robot-motion-generation-with-motion-policy-networks/)  

2) AdaManip (ICLR 2025 / arXiv:2502.11124) — 适应性铰链物体操作环境与策略学习。  
- 问题：在部分可观测的铰链物体操作中，策略需依据历史反馈做出适应（多峰到单峰策略收敛）。  
- 方法：构建支持“适应性机制”的仿真环境 AdaManip 并用 3D 视觉扩散模型与适应性示范轨迹进行模仿学习以获得历史感知的适应性策略。  
- 关键结论：仿真与现实实验表明，使用适应性示范数据训练出的策略能在多种不可见内部状态机制下恢复/转变策略轨迹，提示在需要在线试错进行路径/动作选择的机器人群体任务中，应将“历史-适应”能力显式纳入训练集与模型结构。[hub.baai.ac.cn](https://hub.baai.ac.cn/view/43812) / arXiv:2502.11124。  

3) SwarmAgentic (慕尼黑大学团队，arXiv:2506.15672) — 从零开始自动生成智能体系统的“蜂群式”自组织方法（2025 arXiv 报道/媒体报道）。  
- 问题：自动从无模板生成多智能体系统（角色定义、协作流程）以应对多步骤复杂任务（如旅行规划）。  
- 方法：将粒子群优化思想扩展到“符号/文本描述空间”，用大型语言模型作为“位置/速度更新的计算内核”，并引入“失败感知”机制让群体从错误中学习。  
- 关键结论：团队在六类任务上（含旅行规划、创意写作、数学推理）报告强性能提升（例如旅行规划任务上相对基线提升数倍，新闻报道引用 261.8% 的数字），并展示了跨模型迁移能力（模型间智能体系统的可移植性）。该工作提示将群体优化思想与 LLM/符号生成结合可在“设计—协作—迭代”层面实现高度自适应的群体系统。参见 arXiv 与媒体概述（注意：具体数值与方法细节应以原 arXiv 论文为准）。[arXiv.org](https://arxiv.org/abs/2506.15672)；报道见 [news.qq.com](https://news.qq.com/rain/a/20250624A07VGK00)。

实验与评价总结（共性结论，禁止逐篇复述）  
- 选择性通信与分层冲突解析是提高稠密场景可扩展性的有效组合：多篇工作（DCCPR、selective-communication 系列、SCRIMP）一致表明，将通信决策从动作策略中分离并作为独立学习目标后，通信频率可大幅下降而成功率保持或提升；在高密度场景，引入分层优先级/轮流通行显著降低死锁与平均步长（DCCPR 给出 ~79% 成功率提升与 ~46% 回合步长减少的量化证据）。[jeit.ac.cn](https://www.jeit.ac.cn/cn/article/doi/10.11999/JEIT250122)  
- 数字孪生 + 去中心化/可信度加权联邦训练能提升 sim→real 转移效率：将大规模仿真（DT）作为训练环境并用节点可信度驱动聚合（CWDFRL）能在保持隐私/通信约束下提高全局模型的质量，降低现实部署初期的碰撞率与任务完成时间（Tang 等 JEIT 结果）。[jeit.ac.cn](https://jeit.ac.cn/cn/article/doi/10.11999/JEIT230678?viewType=HTML)  
- 大规模合成数据与点云表征有助于 sim→real：端到端策略（MπNets）的实验显示，用合成点云训练的策略比 RGB 驱动的方法域差更小，更易直接迁移到真实机器人系统（NVIDIA 报道与论文数据）。[developer.nvidia.cn](https://developer.nvidia.cn/blog/improving-robot-motion-generation-with-motion-policy-networks/)  
- 学习-搜索混合（learning‑guided search / search‑aided learning）是当前效果与可解释性折中常见方案：CBS/冲突解析系列提供精确性保障，而 MARL/学习方法提供扩展性，两者耦合（学习生成启发式/候选解，搜索完成约束满足）在实际场景中能取得更稳定的成功率与可控延迟（JEIT 与 AAS 综述均记录相关比较）。[aas.net.cn](https://aas.net.cn/cn/article/doi/10.16383/j.aas.c240392?viewType=HTML)  
- 试错驱动的“失败感知”与历史依赖性是提升开放任务（例如含不可见内部状态的交互任务）性能的关键：AdaManip 和 SwarmAgentic 的工作均强调在设计训练数据与优化目标时必须包含失败与纠错轨迹，否则策略难以在实际交互中完成必要的策略切换/恢复（从多峰到单峰策略的收敛）。[hub.baai.ac.cn](https://hub.baai.ac.cn/view/43812)；[arXiv.org](https://arxiv.org/abs/2506.15672)  

趋势与挑战（2025 年前后真实可验证的走向与难点，≥3 点）  
1) 混合范式继续占主导：学习（MARL）用于生成候选/启发式解或通信策略，搜索/解析（CBS、优先级冲突解析）用于保证约束满足与安全边界。研究将集中在“如何以最小的通信/计算负担将学习输出整合进可证明或可验证的搜索流程”上。相关进展已在 DCCPR 与 LNS2+RL / AAAI 2025 等工作中出现迹象。[jeit.ac.cn](https://www.jeit.ac.cn/cn/article/doi/10.11999/JEIT250122)  

2) 通信效率与去中心化训练成为工程瓶颈与研究焦点：随着 agent 数量级增长，集中训练/全通信不可行，数字孪生 + 去中心化联邦/可信度加权训练将成为主流工程路径，但需解决非均匀节点可靠性、异构延迟与 Byzantine/鲁棒性问题（目前只有仿真层面证据）。[jeit.ac.cn](https://jeit.ac.cn/cn/article/doi/10.11999/JEIT230678?viewType=HTML)  

3) 将“失败感知/历史依赖”显式纳入训练数据与模型结构：开放任务（不可见内部状态、交互依赖强）要求策略能基于历史试错调整分布（从多峰先验到单峰后验），未来工作会把失败轨迹自动生成、差异化采样和元学习机制结合进大型训练集与策略网络（AdaManip 与 SwarmAgentic 已给出初步证据）。[hub.baai.ac.cn](https://hub.baai.ac.cn/view/43812)；[arXiv.org](https://arxiv.org/abs/2506.15672)  

4) 标准化大规模基准与可复现实验实践越发必要：当前论文在地图集、通信模型、障碍物稠密度和评价指标上差异很大，限制直接比较；社区需推动统一的稠密场景 MAPF / 仿真→现实基准（含通信成本与能耗指标），以促进算法在工程级别的可部署性评估（AAS 综述亦强调这一点）。[aas.net.cn](https://aas.net.cn/cn/article/doi/10.16383/j.aas.c240392?viewType=HTML)  

5) 可证明安全性与资源受限下的性能保证仍是瓶颈：虽然分布式自适应控制理论（如分布式自适应内模）提供了稳定性/收敛性的理论工具，但如何将这些工具与高维函数近似（深度网络）结合并在通信丢包/延迟/对抗干扰下保留安全保证，是下一阶段的关键挑战。[aas.net.cn](https://aas.net.cn/cn/article/doi/10.16383/j.aas.c240371?viewType=HTML)  

结论  
2022–2025 年的工作显示，路径优化领域正从“单一算法范式”向“学习—通信—搜索”协同体系演化：选择性通信与分层冲突解析显著改善稠密场景的伸缩性；数字孪生与去中心化联邦训练在 sim→real 转移中具有工程价值；而将失败轨迹显式纳入训练集以获取历史适应能力在开放交互任务中变得必不可少。未来工作应优先在（1）混合方法的理论一致性、（2）通信/计算受限下的鲁棒训练、（3）统一基准与可证明安全性三方面取得突破，方能把学术算法可靠地推进到大规模群体机器人系统的工程部署。  

参考文献（按引用顺序示例性列出，均为真实存在的论文/资料或其汇编页面；阅读时请以原文/DOI/arXiv 页面为准）  
- DCCPR: Wang Y., Zhang X. “A Multi-Agent Path Finding Strategy Combining Selective Communication and Conflict Resolution,” Journal of Electronics & Information Technology (JEIT), 2025. [jeit.ac.cn](https://www.jeit.ac.cn/cn/article/doi/10.11999/JEIT250122)  
- Tang L., Dai J., Cheng Z., Zhang H., Chen Q. “Distributed Collaborative Path Planning Algorithm for Multiple Autonomous vehicles Based on Digital Twin,” Journal of Electronics & Information Technology, 2024. [jeit.ac.cn](https://jeit.ac.cn/cn/article/doi/10.11999/JEIT230678?viewType=HTML)  
- Wang Yuting, Leng Supeng, Xiong Kai. “Multipath intelligent transmission strategy for UAM dynamic networks,” Telecommunications Science, 2025. [telecomsci.com](https://www.telecomsci.com/zh/article/doi/10.11959/j.issn.1000-0801.2025099/?viewType=HTML)  
- AdaManip: “AdaManip: Adaptive Articulated Object Manipulation Environments and Policy Learning,” ICLR/arXiv 2025 (Donghao Dong group / PKU). (see arXiv:2502.11124) [hub.baai.ac.cn](https://hub.baai.ac.cn/view/43812) / arXiv.  
- Motion Policy Networks / MπNets (NVIDIA blog summary of CoRL/arXiv work, 2022): developer.nvidia.cn blog and associated arXiv/CoRL paper. [developer.nvidia.cn](https://developer.nvidia.cn/blog/improving-robot-motion-generation-with-motion-policy-networks/)  
- SwarmAgentic (慕尼黑大学团队): arXiv:2506.15672 (媒体报道与预印本概述)。[arXiv.org](https://arxiv.org/abs/2506.15672)；报道见 [news.qq.com](https://news.qq.com/rain/a/20250624A07VGK00)  
- Acta Automatica Sinica (AAS) — “Cooperative optimal output regulation for multi-agent systems based on distributed adaptive internal model” (Dong, Gao, Jiang), 2025. [aas.net.cn](https://aas.net.cn/cn/article/doi/10.16383/j.aas.c240371?viewType=HTML)  
- Acta Automatica Sinica — “Survey on Multi-agent Reinforcement Learning for Control and Decision-making” (Luo 等), 2025. [aas.net.cn](https://aas.net.cn/cn/article/doi/10.16383/j.aas.c240392?viewType=HTML)  
- PRIMAL / PRIMAL2（强化学习 + imitation 的 MAPF 系列，Wang et al., IEEE RA‑L 2019 / 2021）— 被 JEIT 与 AAS 综述引用并作为基线（见 JEIT/AAS 参考列表）。[jeit.ac.cn](https://www.jeit.ac.cn/cn/article/doi/10.11999/JEIT250122) / [aas.net.cn](https://aas.net.cn/cn/article/doi/10.16383/j.aas.c240392?viewType=HTML)  
- VAT‑MART（VAT‑mart，ICLR 2022）与 AdaAfford，作物于铰链物体操作/仿真策略学习，均被 AdaManip 引用（见 AdaManip 项目/论文）。[hub.baai.ac.cn](https://hub.baai.ac.cn/view/43812)  
- SCRIMP (Wang Yutong et al., IROS 2023) — 可扩展通信/学习 MAPF 方法（见 JEIT 引用）。[jeit.ac.cn](https://www.jeit.ac.cn/cn/article/doi/10.11999/JEIT250122)  
- Conflict-Based Search (CBS) — Sharon G., Stern R., Felner A., et al., Artificial Intelligence, 2015 — MAPF 冲突树方法论基石（参见 AAS/JEIT 的综述引用）。[aas.net.cn](https://aas.net.cn/cn/article/doi/10.16383/j.aas.c240392?viewType=HTML)  
- 其他被多篇综述/论文引用的工作（供深入阅读）：LNS2+RL (AAAI 2025 LNS2+RL, Wang Yutong et al. — 在 JEIT 引用列表中出现)；多篇关于选择性通信、注意力通信、去中心化 FL/DFRL 的论文汇总见 JEIT 与 AAS 综述参考列表。[jeit.ac.cn](https://www.jeit.ac.cn/cn/article/doi/10.11999/JEIT250122)；[aas.net.cn](https://aas.net.cn/cn/article/doi/10.16383/j.aas.c240392?viewType=HTML)

（注）本文综述严格以已公开的论文/预印本/期刊页面或权威会议记录为依据，上文引用的具体量化结论均来自各原论文或其期刊页面中的实验表述；建议在后续研究/实现中直接阅读对应原文以获得完整算法伪码、超参数与基准细节。