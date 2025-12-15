# 群体机器人路径优化中的自适应算法研究综述（2022–2025）

## 引言

群体机器人路径优化旨在在复杂、动态环境中协调大量个体，以高效、安全地完成导航、避障与任务分配等目标。传统集中式方法难以扩展，而固定策略的分布式方法在环境扰动下鲁棒性不足。2022–2025年间，自适应算法成为该领域的研究核心，其通过在线学习或动态调整机制，使系统能应对环境不确定性、任务动态性及个体异质性。本文系统综述此期间在多智能体强化学习、生物启发式自适应模型及混合优化框架三个方向上的代表性工作，分析其共性挑战与未来趋势。

## 方法分类与代表作

### 基于多智能体强化学习（MARL）的自适应路径规划

该方向利用强化学习的在线学习能力，使智能体能根据环境反馈自适应地调整其路径策略。代表性工作聚焦于通信效率与冲突解决。

王昱与张旭秀[jeit.ac.cn](https://www.jeit.ac.cn/cn/article/doi/10.11999/JEIT250122)针对高密度动态场景中通信开销大与路径冲突频发的问题，提出DCCPR方法。其核心是结合选择性通信与分层冲突解决：通过动态联合屏蔽机制减少冗余通信，并融合A*期望路径与双惩罚项（路径偏差与累计拥堵）的强化学习框架。在warehouse等结构化地图上，其任务成功率比DCC基线提升79%，平均回合步长降低46.4%，显著提升了高密度场景下的可扩展性。

Luo等人[aas.net.cn](https://aas.net.cn/cn/article/doi/10.16383/j.aas.c240392)的综述系统梳理了MARL在控制与决策中的应用，指出在路径规划中，基于值分解（如QMIX）或注意力机制（如ACRL）的方法能有效处理部分可观测性与非平稳性。其分析表明，将显式通信（如DCC）与隐式协调（如PRIMAL）相结合，是解决大规模MAPF问题的关键趋势。

Xue等人[html.rhhz.net](https://html.rhhz.net/ZZDXXBLXB/html/20250402.htm)针对无人机博弈路径规划中样本效率低的问题，提出知识与数据联合驱动的深度强化学习模型。该方法将遗传算法生成的专家路径作为先验知识，与TD3算法在线收集的经验数据共同训练策略网络。实验证明，该方法在基于真实数字高程模型的复杂地形中，收敛速度与学习稳定性均优于纯TD3或DDPG，有效提升了智能体在信息不完全环境下的自主博弈能力。

### 生物启发式自适应模型

此类方法从鱼群、鸟群等自然群体的涌现行为中汲取灵感，构建计算模型以实现高效、鲁棒的集群运动控制。

蔡佳浩与刘磊[hanspub.org](https://www.hanspub.org/journal/paperinformation?paperid=108605)提出一种基于鱼群涌现行为的有限交互深度模型。该模型利用Transformer架构，从真实鱼群轨迹数据中学习出“至多只需参考两个邻居”的有限交互规则，并通过硬注意力机制强制执行。在Cuboids机器人平台上，该模型成功复现了鱼群的环游与内圈超越等涌现行为，群体极性P≈0.98，验证了数据驱动的生物启发模型在物理实现上的有效性与鲁棒性。

在无人机救援场景中，王恩良等人[jeit.ac.cn](https://jeit.ac.cn/cn/article/doi/10.11999/JEIT250694)提出熵增强量子涟漪协同算法（E²QRSA）。该算法将受困人员生存概率（随时间指数衰减）作为优化目标，而非传统的路径最短。其自适应性体现在：利用信息熵评估搜索空间不确定性以引导初始种群，并通过熵驱动的参数自适应调控动态调整涟漪传播。实验表明，E²QRSA的平均生存概率比次优算法（SEWOA）提升4.3%~5.4%，证明了面向任务效用的自适应优化优于几何距离优化。

### 混合优化与元启发式自适应框架

此类工作结合传统优化算法与自适应机制，以平衡全局探索与局部开发能力。

黄晋等人[opticsjournal.net](https://www.opticsjournal.net/Articles/OJ1d639f2fb4dc6f0b/FullText)针对城市三维环境下传统PSO算法易陷局部最优的问题，提出一种改进PSO算法。其自适应机制包括：使用混沌序列进行均匀初始化、引入分段自适应惯性权重与指数学习因子，并在速度更新中增添加速度因子以增强逃离能力。在城市场景仿真中，该算法在路径平滑度与避障成功率上均优于遗传算法和标准PSO。

董昱辰等人[aas.net.cn](https://aas.net.cn/cn/article/doi/10.16383/j.aas.c240371)研究了离散时间多智能体系统的协同最优输出调节问题。他们提出一种不依赖系统矩阵精确信息的分布式数据驱动自适应控制策略，结合自适应动态规划（ADP）与分布式自适应内模。通过值迭代与策略迭代两种强化学习算法在线学习最优控制器，仿真证明其学习到的控制增益能收敛到理论最优值，解决了模型未知情况下多智能体的协同跟踪问题。

## 实验与评价总结

综合近期文献，实验评价呈现出以下共性：
1.  **评价指标多元化**：除传统的路径长度、成功率外，任务效用（如生存概率）、通信开销（Hz或消息数）、计算效率（回合步长、收敛时间）及系统鲁棒性（在未见场景的泛化能力）成为关键指标。
2.  **测试环境复杂化**：研究普遍采用高障碍密度的结构化地图（如warehouse, den312d）和基于真实数据的三维环境（如DEM地形），以更真实地模拟应用场景。
3.  **基线对比标准化**：PRIMAL、DCC、SCRIMP等MARL方法及PSO、GA等元启发式算法成为标准基线。性能提升需在多种场景（不同智能体数量、地图规模）下验证，以证明其可扩展性。
4.  **消融实验必要性**：对自适应机制中各组件（如通信模块、冲突解决策略、自适应参数）进行消融研究，以量化其贡献，已成为方法验证的必要环节。

## 趋势与挑战

基于2025年前后的最新研究，该领域呈现以下发展趋势：
1.  **从几何优化到任务效用优化**：路径规划的目标正从最小化几何距离转向最大化任务效用，如无人机救援中的生存概率[jeit.ac.cn](https://jeit.ac.cn/cn/article/doi/10.11999/JEIT250694)、物流中的任务完成率。这要求算法能建模并优化与时间、风险等相关的复杂目标函数。
2.  **异构通信与感知的融合**：未来工作将探索结合全局（低频、带宽高）与局部（高频、带宽低）通信的优势[jeit.ac.cn](https://www.jeit.ac.cn/cn/article/doi/10.11999/JEIT250122)，并考虑智能体感知能力的异构性，设计更具鲁棒性的自适应协调机制。
3.  **真实世界约束的集成**：研究将更注重集成真实物理世界的约束，如动态环境变化、智能体能量消耗、连续动作空间（速度、转速）及非完整性约束[jeit.ac.cn](https://www.jeit.ac.cn/cn/article/doi/10.11999/JEIT250122)，以缩小仿真与现实的差距。

## 结论

2022–2025年间，自适应算法在群体机器人路径优化领域取得了显著进展。通过多智能体强化学习、生物启发模型及混合优化框架，研究者有效提升了系统在复杂动态环境中的可扩展性、鲁棒性与任务效用。未来的研究将更紧密地结合真实应用场景，从任务目标、系统架构和物理约束等多个维度深化自适应机制的设计，推动群体机器人技术走向实际部署。

## 参考文献

1.  Wang, Y., & Zhang, X. (2025). A Multi-Agent Path Finding Strategy Combining Selective Communication and Conflict Resolution. *Journal of Electronics & Information Technology*, 47(8), 2830-2840. [jeit.ac.cn](https://www.jeit.ac.cn/cn/article/doi/10.11999/JEIT250122)
2.  Luo, B., Hu, T. M., Zhou, Y. H., Huang, T. W., Yang, C. H., & Gui, W. H. (2025). Survey on multi-agent reinforcement learning for control and decision-making. *Acta Automatica Sinica*, 51(3), 510-539. [aas.net.cn](https://aas.net.cn/cn/article/doi/10.16383/j.aas.c240392)
3.  Xue, J., Zhang, S., Lu, Y., Yan, X., & Fu, W. (2025). UAV Game Path Planning Based on Deep Reinforcement Learning. *Journal of Zhengzhou University(Natural Science Edition)*, 57(4), 8-14. [html.rhhz.net](https://html.rhhz.net/ZZDXXBLXB/html/20250402.htm)
4.  Cai, J., & Liu, L. (2025). A Finite Interaction Depth Model for Swarm Robotics Inspired by Fish Schooling Behavior. *Modeling and Simulation*, 14(2), 460-474. [hanspub.org](https://www.hanspub.org/journal/paperinformation?paperid=108605)
5.  Wang, E., Zhang, Z., & Sun, Z. (2025). Entropy Quantum Collaborative Planning Method for Emergency Path of Unmanned Aerial Vehicles Driven by Survival Probability. *Journal of Electronics & Information Technology*. [jeit.ac.cn](https://jeit.ac.cn/cn/article/doi/10.11999/JEIT250694)
6.  Huang, J., Li, Y., Wang, S., & Liu, H. (2024). 3D Path Planning of UAVs in Urban Environments Based on Improved PSO Algorithm. *Electronics Optics & Control*, 31(2), 41. [opticsjournal.net](https://www.opticsjournal.net/Articles/OJ1d639f2fb4dc6f0b/FullText)
7.  Dong, Y., Gao, W., & Jiang, Z. (2025). Cooperative optimal output regulation for multi-agent systems based on distributed adaptive internal model. *Acta Automatica Sinica*, 51(3), 678-691. [aas.net.cn](https://aas.net.cn/cn/article/doi/10.16383/j.aas.c240371)
8.  Sartoretti, G., Kerr, J., Shi, Y., et al. (2019). PRIMAL: Pathfinding via reinforcement and imitation multi-agent learning. *IEEE Robotics and Automation Letters*, 4(3), 2378–2385.
9.  Ma, Z., Luo, Y., & Pan, J. (2022). Learning selective communication for multi-agent path finding. *IEEE Robotics and Automation Letters*, 7(2), 1455–1462.
10. Wang, Y., Xiang, B., Huang, S., et al. (2023). SCRIMP: Scalable communication for reinforcement-and imitation-learning-based multi-agent pathfinding. In *2023 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)* (pp. 9301-9308).
11. Fujimoto, S., Hoof, H., & Meger, D. (2018). Addressing function approximation error in actor-critic methods. In *International Conference on Machine Learning* (pp. 1587-1596).
12. Enderes, T., Gabriel, J., & Deutscher, J. (2024). Cooperative output regulation for networks of hyperbolic systems using adaptive cooperative observers. *Automatica*, 162, 111506.