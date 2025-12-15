## Metaheuristic Algorithms for UAV Path Planning and Engineering Design (2022-2025) 中文学术综述

### 引言

无人机（UAV）路径规划和工程设计是当下热门的研究领域，旨在通过优化无人机飞行路径或系统参数，以提升其在复杂环境下的任务执行效率、安全性及系统性能。元启发式算法因其强大的全局搜索能力和对复杂约束的处理能力，在解决此类NP-hard问题上展现出显著优势。本综述旨在梳理2022-2025年间，元启发式算法在无人机路径规划和工程设计领域的代表性研究进展，分析其核心方法、关键结论，并对未来研究趋势进行展望。

### 方法分类与代表作

本节将元启发式算法在无人机路径规划与工程设计中的应用分为几个主要类别，并精选代表性工作进行介绍。

#### 1. 基于群智能优化算法（Swarm Intelligence-based Algorithms）

**粒子群优化 (PSO) 及其变体**

*   **[opticsjournal.net](https://www.opticsjournal.net/Articles/OJ1d639f2fb4dc6f0b/FullText) (2024)**：针对城市环境中无人机三维路径规划问题，提出了一种改进的粒子群优化（PSO）算法。该方法通过混沌序列初始化粒子群以提高初始粒子分布的均匀性，引入分段自适应惯性权重和自适应指数学习因子平衡全局与局部搜索能力，并在速度更新公式中增添加速度因子和自适应调整系数优化粒子位置更新。实验结果表明，改进算法在多种测试函数和仿真场景下，相较于遗传算法和传统PSO算法，能获得更高质量的路径规划结果。

*   **[pdf.hanspub.org](https://pdf.hanspub.org/airr_2610672.pdf) (2025)**：融合遗传算法与粒子群算法解决无人机路径规划问题，旨在克服单一算法的局限性。该方法首先利用遗传算法的全局搜索能力对种群进行初始化和全局搜索，为粒子群算法提供高质量的初始解集，随后引入粒子群算法的速度与位置更新机制增强局部搜索能力。通过模拟实验平台在复杂环境下的测试，融合算法在路径长度、搜索时间及成功率等指标上均优于单一算法。

**蜣螂算法 (DBO) 及其改进**

*   **[qikan.cmes.org](https://qikan.cmes.org/zzyzdh/CN/10.3969/j.issn.1009-0134.2025.10.011) (2025)**：提出了一种改进的蜣螂算法（IDBO）解决电网巡检中车机协同无人机路径规划问题。为提升搜索效率和收敛性能，该算法采用Logistic混沌映射优化初始解分布，引入鱼鹰算法的全局搜索策略增强滚球蜣螂的全局寻优能力，并在觅食阶段引入自适应t分布策略增强局部寻优能力，避免陷入局部最优。算例实验结果显示，IDBO在不同车速场景下均表现出更高的求解精度和稳定性，尤其在无人机悬停协作等复杂情况下的解算能力显著优于对比算法。

#### 2. 基于深度强化学习 (Deep Reinforcement Learning, DRL) 方法

*   **[html.rhhz.net](https://html.rhhz.net/ZZDXXBLXB/html/20250402.htm) (2025)**：针对深度强化学习在复杂环境无人机博弈任务中学习效率低的问题，提出了一种知识和数据联合驱动的深度强化学习模型。该模型借鉴模仿学习思想，将遗传算法作为启发式搜索策略收集专家经验知识，并结合深度强化学习与环境交互收集在线经验数据，共同优化无人机博弈策略。实验结果表明，该模型显著提升了收敛速度和学习稳定性，训练后的智能体具备更强的自主博弈路径规划能力。

*   **[jeit.ac.cn](https://www.jeit.ac.cn/cn/article/doi/10.11999/JEIT250012) (2025)**：在低空混合障碍环境下，针对无人机协同多智能体航迹规划与通信能效最大化问题，提出了一种基于碰撞概率地图避障的用户调度优化多智能体深度确定性策略梯度 (MADDPG) 算法。该方法通过将传统低空障碍表示扩展为概率碰撞地图，并采用非正交多址接入 (NOMA) 技术优化通信能效，实现多机协同航迹规划。仿真分析表明，该策略在提升无人机系统能效的同时，平均碰撞概率较传统避障方法降低约8倍。

*   **[jeit.ac.cn](https://www.jeit.ac.cn/cn/article/doi/10.11999/JEIT241055?viewType=HTML) (2025)**：针对多无人机在部分未知设备位置场景下的数据收集需求，提出了一种模型辅助的联邦强化学习多无人机路径规划方法。该方法结合最大熵强化学习与单调价值函数分解机制，引入动态熵温度参数和注意力机制，优化多无人机协作的探索效率与策略稳定性。此外，设计基于信道建模与位置估计的混合模拟环境构建方法，利用改进粒子群算法快速估计未知设备位置，有效降低真实环境交互成本。仿真结果显示，该算法可提升数据收集率5.2%并减少路径长度7.7%。

#### 3. 其他混合优化算法

*   **[jeit.ac.cn](https://jeit.ac.cn/cn/article/doi/10.11999/JEIT250694?viewType=HTML) (2025)**：针对自然灾害应急救援中无人机路径规划面临的复杂约束和时效性要求，提出熵增强量子涟漪协同优化算法 (E²QRSA)。该算法构建以受困人员生存概率最大化为目标函数，综合考虑禁飞区、警戒区、动态障碍物等多重约束，并设计基于信息熵的量子态初始化策略和多涟漪协同干涉机制。实验结果表明，E²QRSA相较于次优算法可将平均生存概率提升4.3%～5.4%，显著提高了复杂灾害环境下路径规划的时效性、安全性与决策科学性。

### 实验与评价总结

综上，近期无人机路径规划和工程设计领域的研究呈现出以下共性特征和结论：

1.  **多目标优化是主流**：不仅仅关注最短路径或最低能耗，而是综合考虑安全性、时效性、生存概率、通信能效、避障效果等多维目标。例如，[jeit.ac.cn](https://jeit.ac.cn/cn/article/doi/10.11999/JEIT250694?viewType=HTML) 以受困人员生存概率最大化为目标，[jeit.ac.cn](https://www.jeit.ac.cn/cn/article/doi/10.11999/JEIT250012) 关注最大化通信能效和低碰撞概率。
2.  **融合与改进策略提升性能**：单一的元启发式算法往往在面对复杂、动态、多约束环境时表现不佳，因此，研究者普遍采用算法融合（如GA-PSO [pdf.hanspub.org](https://pdf.hanspub.org/airr_2610672.pdf)）、多策略改进（如PSO的混沌初始化、自适应权重 [opticsjournal.net](https://www.opticsjournal.net/Articles/OJ1d639f2fb4dc6f0b/FullText)；DBO的混沌映射、鱼鹰算法、自适应t分布 [qikan.cmes.org](https://qikan.cmes.org/zzyzdh/CN/10.3969/j.issn.1009-0134.2025.10.011)）来增强算法的全局搜索能力、局部开发能力、收敛速度和跳出局部最优的能力。
3.  **结合学习范式应对不确定性**：深度强化学习作为一种强大的决策框架，在处理动态和部分可观测环境问题上优势显著。例如，[html.rhhz.net](https://html.rhhz.net/ZZDXXBLXB/html/20250402.htm) 将遗传算法的专家经验与DRL结合，[jeit.ac.cn](https://www.jeit.ac.cn/cn/article/doi/10.11999/JEIT250012) 采用MADDPG算法，[jeit.ac.cn](https://www.jeit.ac.cn/cn/article/doi/10.11999/JEIT241055?viewType=HTML) 采用联邦强化学习，均有效提升了无人机在复杂、未知或动态环境下的适应性和决策能力。
4.  **实际应用场景推动方法创新**：电网巡检、应急救援、城市物流等具体应用场景的复杂性和时效性需求，直接促进了元启发式算法在约束处理（禁飞区、动态障碍）、目标函数设计（生存概率、数据收集率）以及模拟环境构建（信道建模、位置估计）等方面的创新。例如，[jeit.ac.cn](https://jeit.ac.cn/cn/article/doi/10.11999/JEIT250694?viewType=HTML) 和 [qikan.cmes.org](https://qikan.cmes.org/zzyzdh/CN/10.3969/j.issn.1009-0134.2025.10.011) 针对实际紧急情况和巡检任务的特殊要求提出了定制化的算法。

### 趋势与挑战

2025年前后，无人机路径规划和工程设计领域的研究将呈现以下趋势：

1.  **多模态、实时、自适应决策**：面对更加复杂的动态环境（如突发事件、快速变化的气象条件、高密度空域），无人机需要融合多种传感器信息（视觉、雷达、通信）进行多模态感知并进行实时、自适应的路径规划和决策。这将需要更高效的算法，能够权衡计算资源和决策优化，实现毫秒级的响应速度。
2.  **空天地一体化网络的协同优化**：无人机不再是孤立作战单元，而是作为空天地一体化网络的重要组成部分。未来的研究将更加关注多无人机、卫星、地面基站之间的协同感知、路径规划和资源分配，以实现任务效率、覆盖范围和系统鲁棒性的最大化。例如，[jeit.ac.cn](https://www.jeit.ac.cn/cn/article/doi/10.11999/JEIT241071?viewType=HTML) 和 [jeit.ac.cn](https://jeit.ac.cn/cn/article/doi/10.11999/JEIT241071) 等综述指出了无人机辅助移动边缘计算网络中轨迹规划与资源分配将是研究热点。
3.  **可解释AI与安全性保障**：随着AI算法在无人机路径规划中扮演越来越重要的角色，算法决策的可解释性变得至关重要，尤其是在安全攸关的应用场景（如应急救援）。同时，如何保障无人机在复杂电磁环境下的通信安全、对抗恶意干扰和网络攻击，将是未来工程设计和路径规划中的关键考量。
4.  **硬件-算法深度协同设计**：为满足高性能、低功耗、小体积的无人机载端需求，传统上独立的硬件设计与算法优化将趋于深度融合。这将涉及基于FPGA/ASIC的算法加速、边缘AI芯片的路径规划与决策部署，以及能量收集和无线充电技术在延长无人机续航方面的应用。

### 结论

本综述回顾了2022-2025年间元启发式算法在无人机路径规划和工程设计领域的最新研究进展。可以看到，研究趋势正从单一算法优化转向多算法融合、元启发式算法与深度强化学习结合、强化模型辅助与实时决策，并更加紧密地围绕实际应用需求进行创新。未来的研究将聚焦于提升算法的实时性、自适应性、可解释性，并考虑空天地一体化网络的协同以及硬件-算法的深度融合，以应对日益复杂的任务挑战。

### 参考文献

*   [opticsjournal.net] 黄晋, 李云飞, 王圣淳, 刘厚荣. 基于改进PSO算法的无人机城域三维路径规划[J]. 电光与控制, 2024, 31(2): 41. (HUANG Jin, LI Yunfei, WANG Shengchun, LIU Hourong. 3D Path Planning of UAVs in Urban Environments Based on Improved PSO Algorithm[J]. Electronics Optics & Control, 2024, 31(2): 41.)
*   [pdf.hanspub.org] 付三丽, 黄恒一, 韩洪哲, 洪乐, 尹承锡, 李雄祺, 高荣标. 融合遗传算法与粒子群算法无人机路径规划技术研究[J]. 人工智能与机器人研究, 2025, 14(5): 1167-1176. (FU Sanli, HUANG Hengyi, HAN Hongzhe, HONG Le, YIN Chengxi, LI Xiongqi, GAO Rongbiao. Research on Unmanned Aerial Vehicle Path Planning Technology Integrating Genetic Algorithm and Particle Swarm Optimization Algorithm[J]. Artificial Intelligence and Robotics Research, 2025, 14(5): 1167-1176.)
*   [qikan.cmes.org] 艾粤芬, 莫愿斌. 改进麋鹿群优化算法的无人机三维路径规划[J]. 制造业自动化, 2025, 47(10): 94-102.
*   [html.rhhz.net] 薛均晓, 张世文, 陆亚飞, 严笑然, 付玮. 基于深度强化学习的无人机博弈路径规划[J]. 郑州大学学报(理学版), 2025, 57(4): 8-14. (XUE Junxiao, ZHANG Shiwen, LU Yafei, YAN Xiaoran, FU Wei. UAV Game Path Planning Based on Deep Reinforcement Learning[J]. Journal of Zhengzhou University(Natural Science Edition), 2025, 57(4): 8-14.)
*   [jeit.ac.cn] 冯斯梦, 张云弈, 刘凯, 李宝龙, 董超, 张磊, 吴启晖. 低空混合障碍下无人机协同多智能体航迹规划[J]. 电子与信息学报, 2025, 47(5): 1291-1300. (FENG Simeng, ZHANG Yunyi, LIU Kai, LI Baolong, DONG Chao, ZHANG Lei, WU Qihui. Collaborative Multi-agent Trajectory Optimization for Unmanned Aerial Vehicles Under Low-altitude Mixed-obstacle Airspace[J]. Journal of Electronics & Information Technology, 2025, 47(5): 1291-1300.)
*   [jeit.ac.cn] 陆音, 刘金志, 张珉. 一种模型辅助的联邦强化学习多无人机路径规划方法[J]. 电子与信息学报, 2025, 47(5): 1368-1380. (LU Yin, LIU Jinzhi, ZHANG Min. A Model-Assisted Federated Reinforcement Learning Method for Multi-UAV Path Planning[J]. Journal of Electronics & Information Technology, 2025, 47(5): 1368-1380.)
*   [jeit.ac.cn] 王恩良, 章祯, 孙知信. 复杂约束下应急救援无人机路径的熵增强量子涟漪协同算法[J]. 电子与信息学报, 2025. (WANG Enliang, ZHANG Zhen, SUN Zhixin. Entropy Quantum Collaborative Planning Method for Emergency Path of Unmanned Aerial Vehicles Driven by Survival Probability[J]. Journal of Electronics & Information Technology, 2025.)
*   [pdf.hanspub.org] 张顺, 刘媛华, 张颢严. 基于改进蜣螂算法的车机协同巡检路径规划方法[J]. 理论数学, 2025, 15(1): 130-142. (ZHANG Shun, LIU Yuanhua, ZHANG Haoyan. Vehicle-Drone Collaborative Inspection Path Planning Method Based on Improved Dung Beetle Algorithm[J]. Pure Mathematics, 2025, 15(1): 130-142.)
*   [jeit.ac.cn] 王侃, 曹铁林, 李旭杰, 李红艳, 李萌, 周墨淼. 无人机辅助边缘计算网络轨迹规划与资源分配研究综述[J]. 电子与信息学报, 2025, 47(5): 1266-1281. (WANG Kan, CAO Tielin, LI Xujie, LI Hongyan, LI Meng, ZHOU Momiao. A Survey on Trajectory Planning and Resource Allocation in Unmanned Aerial Vehicle-assisted Edge Computing Networks[J]. Journal of Electronics & Information Technology, 2025, 47(5): 1266-1281.)
*   [jeit.ac.cn] 王侃, 曹铁林, 李旭杰, 李红艳, 李萌, 周墨淼. 无人机辅助边缘计算网络轨迹规划与资源分配研究综述[J]. 电子与信息学报, 2025, 47(5): 1266-1281. (WANG Kan, CAO Tielin, LI Xujie, LI Hongyan, LI Meng, ZHOU Momiao. A Survey on Trajectory Planning and Resource Allocation in Unmanned Aerial Vehicle-assisted Edge Computing Networks[J]. Journal of Electronics & Information Technology, 2025, 47(5): 1266-1281.)
*   [jeit.ac.cn] 周墨淼, 王侃, 曹铁林, 李旭杰, 李红艳, 李萌. 无人机辅助边缘计算网络轨迹规划与资源分配研究综述[J]. 电子与信息学报, 2025, 47(5): 1266-1281. (ZHOU Momiao, WANG Kan, CAO Tielin, LI Xujie, LI Hongyan, LI Meng. A Survey on Trajectory Planning and Resource Allocation in Unmanned Aerial Vehicle-assisted Edge Computing Networks[J]. Journal of Electronics & Information Technology, 2025, 47(5): 1266-1281.)