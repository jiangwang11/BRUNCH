以下是对“基于人类行为的元启发式算法在优化问题中的应用”的中文学术综述，涵盖 2022-2025 年的代表性工作。

## 人类行为启发元启发式算法在优化问题中的应用综述

### 引言

元启发式算法在解决复杂优化问题方面取得了显著进展，其灵感往往来源于自然现象、物理定律或生物行为。近年来，受人类行为和社会交互模式启发的元启发式算法，因其独特的搜索机制和解决高维度、非线性优化问题的潜力，成为计算智能领域的研究热点。这类算法尝试将人类学习、决策、社会协作等认知过程抽象为数学模型，以期在搜索空间中更有效地发现全局最优解。本综述旨在梳理2022年至2025年期间，基于人类行为的元启发式算法在优化领域的一些代表性工作，探讨其核心方法、应用效果及未来研究趋势。

### 方法分类与代表作

基于人类行为的元启发式算法可根据其模仿的人类行为类型进行分类。以下将重点介绍其中三个主要类别：人类社会交互与协作、人类决策与学习、人类认知与情感。

#### 1. 人类社会交互与协作

本类别算法模拟人类在社会群体中的交流、协作和竞争行为，通过信息共享和群体智慧来指导搜索过程。

*   **社会影响粒子群优化与局部扰动 ([pdf.hanspub.org](https://pdf.hanspub.org/csa_1543619.pdf))**
    周刘长 (2025年) 针对传统粒子群优化（PSO）易陷入局部最优的问题，提出了两种改进型算法：基于种群中心引导的PSOSI（Particle Swarm Optimization-Social Influence）和基于种群聚集程度引入扰动策略的PSOLP（Particle Swarm Optimization-Local Perturbation）。PSOSI通过引入种群中心位置作为额外引导信息，增强了粒子群的全局搜索趋势，促进了收敛效率。PSOLP则在种群聚集度过高时，引入局部扰动以跳出局部最优，提高多样性。在CEC-2022标准测试集及8个实际工程设计问题上的实验结果表明，PSOSI和PSOLP在优化精度和收敛稳定性方面均优于标准PSO及多种主流对比算法，为解决全局优化与工程优化问题提供了高效可行的工具。
*   **通用进化元启发式算法（GEM）([themoonlight.io](https://www.themoonlight.io/zh/review/a-generalized-evolutionary-metaheuristic-gem-algorithm-for-engineering-optimization))**
    Xin-She Yang (2024年) 提出了一种通用进化元启发式算法（GEM）框架，旨在整合多种自然启发式元启发算法的搜索机制。GEM通过统一的解向量初始化、引导随机化搜索和位置更新机制，将20多种现有算法的优点结合起来，实现了对不同算法特性的适应。该算法在15个基准测试函数和工程设计案例（如弹簧设计、三杆桁架设计）上进行了验证，展示了在固定参数下找到全局最优解的能力，并在某些案例中超越了已知最佳解。这项研究为优化算法的未来改进提供了新的视角和实证数据。

#### 2. 人类决策与学习

本类别算法借鉴人类在面对复杂问题时的决策制定和学习过程，通常涉及经验积累、策略调整和认知模型。

*   **人机融合智能决策 ([jeit.ac.cn](https://www.jeit.ac.cn/cn/article/doi/10.11999/JEIT250260))**
    李哲等人 (2025年) 针对数据量、计算能力和算法理论的快速发展，提出了人机融合智能决策的概念，旨在弥补人工智能在可解释性、鲁棒性和泛化能力方面的不足。该工作提出了人机融合智能决策系统的一般框架，包括态势感知和协同决策两个核心层面，并依据决策任务特性和人机关系将决策方式分为人类主导型、机器主导型和人机协同型。在军事、医疗和自动驾驶等关键任务领域的应用实践表明，该范式能有效提升决策质量和可靠性，并增强系统 robustness。这项研究为优化关键领域如军事态势感知、医疗诊断、自动驾驶等提供理论指导和应用实例。
*   **基于强化学习的流程工业智能决策 ([aas.net.cn](https://aas.net.cn/cn/article/doi/10.16383/j.aas.c250272?viewType=HTML))**
    黄慕轶等人 (2025年) 讨论了强化学习在流程工业智能决策中的应用及展望，指出流程工业生产过程的优化决策对经济效益和资源利用效率至关重要，但传统方法面临高维耦合、非线性及不确定性约束。文章系统梳理了强化学习在复杂决策空间、约束处理、大规模系统和不确定性环境中的算法演进与应用探索。通过案例研究，展示了强化学习在例如原油调度和汽油调合优化中的潜力。这项研究为复杂工业系统的智能优化提供了理论基础与方法支撑。

#### 3. 人类认知与情感

本类别算法探索人类的认知偏差、情感状态和问题解决策略如何影响优化过程，试图利用这些特点来避免局部最优或加速收敛。

*   **经验引导的反思性共同演化 ([chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/192842))**
    Yihong Liu 等人 (2025年) 针对组合优化问题中传统基于手工设计的启发式算法对领域专业知识和实施工作的高度依赖，提出了经验引导的提示与启发式算法的反思共同演化（EvoPH）框架。该框架结合了岛屿迁移模型和精英选择算法，模拟多样化启发式算法种群的演化过程，并通过性能反馈指导提示和大语言模型（LLMs）的共同演化。在旅行商问题和装箱问题上的实验结果表明，EvoPH在相对于最优解的最低相对误差方面表现更出色，有效地推动了基于LLMs的自动算法设计领域的发展。
*   **多智能体强化学习控制与决策 ([aas.net.cn](https://aas.net.cn/cn/article/doi/10.16383/j.aas.c240392?viewType=HTML))**
    罗彪等人 (2025年) 对多智能体强化学习在控制与决策领域的研究进行了综述，强调了其在解决大规模复杂问题中的潜力。该领域不仅要考虑环境的动态性，还要应对其他智能体策略的不确定性，这增加了学习和决策过程的复杂性。文中分析了多智能体强化学习在协同控制、零和博弈和非零和博弈等场景下的应用，并讨论了其在机器人协作、无人机群组、自动驾驶交通信号灯控制以及能源管理等多个典型应用中的挑战和进展。这项研究为多智能体强化学习在复杂场景下的发展提供了参考。

### 实验与评价总结

上述基于人类行为的元启发式算法在各类优化问题中展现出较强的性能。在标准基准测试函数（如CEC-2022、IEEE CEC2017和IEEE CEC2021等）上的实验，普遍验证了这些算法在寻优精度和收敛速度方面的优势。例如，PSOSI和PSOLP在CEC-2022测试集上实现了优于标准PSO的优化精度和收敛稳定性 [pdf.hanspub.org](https://pdf.hanspub.org/csa_1543619.pdf)。GEM框架在多峰函数和非线性约束问题上，能够收敛到全局最优解 [themoonlight.io](https://www.themoonlight.io/zh/review/a-generalized-evolutionary-metaheuristic-gem-algorithm-for-engineering-optimization)。此外，这些算法还成功应用于各种实际工程优化任务，包括工程设计问题（如弹簧、桁架设计）、工业流程优化、交通信号控制、能源管理和生物医学图像处理。在这些应用中，这些算法能够有效处理高维、非线性、多约束和不确定性等复杂特性，提供可行且高效的解决方案。然而，尽管性能有所提升，但在某些情况下，如具有高度复杂数学特征和多个鞍点的复合函数中，算法的收敛速度和跳出局部最优的能力仍需进一步提升。

### 趋势与挑战

2025年前后，基于人类行为的元启发式算法领域将呈现以下趋势：

1.  **与深度学习和强化学习的深度融合**：未来的研究将更加侧重于将人类行为启发的元启发式算法与深度学习和强化学习相结合。例如，将元启发式算法用于优化深度神经网络的超参数，或者利用强化学习的智能体与元启发式算法进行交互以提升决策效率。基于LLMs的自动算法设计（如EvoPH框架 [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/192842)）将是重要方向，通过大模型生成和优化启发式规则。
2.  **多目标和多任务优化中的应用拓展**：随着实际问题复杂性的增加，对多目标和多任务优化解决方案的需求日益增长。人类行为在权衡多个冲突目标和处理相关任务方面的能力，为开发更高效的多目标和多任务元启发式算法提供了丰富灵感。例如，在约束多目标优化问题中，双种群协同进化算法的应用将持续扩展 [aas.net.cn](https://aas.net.cn/cn/article/doi/10.16383/j.aas.c250023)。
3.  **可解释性与鲁棒性增强**：随着元启发式算法在关键领域（如人机融合决策 [jeit.ac.cn](https://www.jeit.ac.cn/cn/article/doi/10.11999/JEIT250260)和流程工业智能决策 [aas.net.cn](https://aas.net.cn/cn/article/doi/10.16383/j.aas.c250272?viewType=HTML)）的应用，提升算法的可解释性和鲁棒性将成为重要挑战。研究将聚焦于开发能够清晰阐释决策过程，并在不确定环境中保持稳定性能的元启发式算法。
4.  **混合模型和协同进化策略的普及**：结合不同算法优势的混合模型和协同进化策略将成为主流。例如，将遗传算法与黏菌算法的优点相结合，通过振荡收缩机制和自扩散机制等增强探索和开发能力的平衡，并利用判别式控制策略自适应调整参数 [xbna.pku.edu.cn](https://xbna.pku.edu.cn/fileup/0479-8023/HTML/2025-1-14.html)。

### 结论

基于人类行为的元启发式算法通过模拟人类在社会、认知和决策过程中的复杂行为，为解决各种优化难题提供了新颖而有效的途径。近年来，该领域涌现出大量创新性工作，这些算法在理论和实践中均展现出可靠的性能。尽管在可解释性、可伸缩性和与现实世界系统集成方面仍面临挑战，但随着与深度学习、强化学习等前沿技术的深度融合，以及对人类认知机制更深入的理解，基于人类行为的元启发式算法将在未来的优化领域发挥更为关键的作用。

### 参考文献

*   [aas.net.cn](https://aas.net.cn/cn/article/doi/10.16383/j.aas.c240392?viewType=HTML) Luo Biao, Hu Tian-Meng, Zhou Yu-Hao, Huang Ting-Wen, Yang Chun-Hua, Gui Wei-Hua. Survey on multi-agent reinforcement learning for control and decision-making. Acta Automatica Sinica, 2025, 51(3): 510−539.
*   [aas.net.cn](https://aas.net.cn/cn/article/doi/10.16383/j.aas.c250023) Ding Wei-Chao, Sun Li-Ye, Luo Fei, Gu Chun-Hua, Dong Wen-Bo. Two-population Co-evolutionary Algorithm for Constrained Multi-objective Optimization Problems in Complex Feasible Domains. Acta Automatica Sinica, 2025, 51(8): 1−21.
*   [aas.net.cn](https://aas.net.cn/cn/article/doi/10.16383/j.aas.c250272?viewType=HTML) Huang Mu-Yi, Zhu Jia-Wen, Dai Xin, Du Wen-Li, Qian Feng. A review and perspective on reinforcement learning for intelligent decision-making in process industries. Acta Automatica Sinica, xxxx, xx(x): x−xx.
*   [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/192842) Yihong Liu, Junyi Li, Wayne Xin Zhao, Hongyu Lu, Ji-Rong Wen. Experience-guided reflective co-evolution of prompts and heuristics for automatic algorithm design. 2025.
*   [jeit.ac.cn](https://www.jeit.ac.cn/cn/article/doi/10.11999/JEIT250260) Li Zhe, Wang Ke, Wang Biao, Zhao Ziqi, Li Yafei, Guo Yibo, Hu Yazhou, Wang Hua, Lv Pei, Xu Mingliang. Human-Machine Fusion Intelligent Decision-Making: Concepts, Framework, and Applications. Journal of Electronics & Information Technology. 2025.
*   [pdf.hanspub.org](https://pdf.hanspub.org/csa_1543619.pdf) Zhou Liuchang. Population-Center-Guided Particle Swarm Optimization Algorithm for Global Optimization. Computer Science and Application, 2025, 15(5): 173-183.
*   [themoonlight.io](https://www.themoonlight.io/zh/review/a-generalized-evolutionary-metaheuristic-gem-algorithm-for-engineering-optimization) Xin-She Yang. A Generalized Evolutionary Metaheuristic (GEM) Algorithm for Engineering Optimization. 2024.
*   [xbna.pku.edu.cn](https://xbna.pku.edu.cn/fileup/0479-8023/HTML/2025-1-14.html) Pan Jiawen, Zhai Weixin, Guo Zhou, Hu Banshao, Cheng Chengqi, Wu Caicong. A Hybrid Slime Mould Genetic Algorithm Based on Spatial Attenuation Self-diffusion Mechanism. Acta Scientiarum Naturalium Universitatis Pekinensis. 2025, Vol. 61, No. 1.
*   [jeit.ac.cn](https://jeit.ac.cn/cn/article/doi/10.11999/JEIT231195?viewType=HTML) Gong Maoguo, Luo Tianshi, Li Hao, He Yajing. A Survey of Collaborative of Swarm Intelligence for Evolutionary Computation. Journal of Electronics & Information Technology. 2024, 46(5): 1716-1741.
*   [image.hanspub.org](https://image.hanspub.org/Html/1-2571228_81778.htm) He Yongkang, Li Xufang. Neighborhood Search and Artificial Hummingbird Optimization Algorithms with Improved Lévy Factors. Modeling and Simulation, 2024, 13(02): 987-1003.