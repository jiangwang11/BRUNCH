好的，作为一名严谨的科研助手，我将基于提供的真实联网搜索结果，为您生成一篇关于「Human-based Metaheuristic Algorithms in Optimization Problems」的中文学术综述。

***

### **面向优化问题的人本元启发式算法研究综述（2022-2025）**

**摘要：** 人本元启发式算法（Human-based Metaheuristic Algorithms）通过模拟人类社会交互、认知规划及协同决策等行为来求解复杂优化问题，是智能计算领域的一个重要分支。本综述旨在系统梳理 2022 至 2025 年间该领域的代表性研究进展。通过对近期工作的分析，本文将方法归纳为社会交互模型与认知规划模型两大类，并重点介绍了粒子群优化-社会影响算法（PSOSI）、双种群协同进化算法（TCCMOA）、基于蒙特卡洛树搜索的自动启发式设计（MCTS-AHD）等前沿工作。综述进一步总结了这些新方法在标准测试集和工程问题上的共性实验表现，并指出了当前研究向人机融合智能、大语言模型驱动的自动算法设计及多策略协同进化等方向发展的明确趋势与挑战。

**关键词：** 元启发式算法；人本优化；群体智能；人机融合；大语言模型；自动算法设计

---

### **1. 引言**

元启发式算法（Metaheuristic Algorithms）为求解大规模、非线性的NP难优化问题提供了不依赖问题梯度信息的高效框架。在众多灵感来源中，模拟人类社会行为、认知过程或组织结构的“人本元启发式算法”因其独特的搜索机制而备受关注。传统的人本算法多侧重于对宏观社会现象（如群体学习、社会影响）的抽象模拟，而 2022 年以来的研究呈现出两大新动向：一是与人工智能前沿技术深度融合，利用大型语言模型（LLM）进行认知层面的推理与规划；二是从“模拟人”向“融合人”转变，构建人机协同决策的智能系统，以期实现超越纯机器智能或人类专家的决策水平 [jeit.ac.cn](https://www.jeit.ac.cn/cn/article/doi/10.11999/JEIT250260)。本综述将聚焦于 2022-2025 年的代表性工作，对人本元启发式算法的最新方法、评测范式及未来趋势进行系统性总结与展望。

### **2. 方法分类与代表作**

根据算法核心机制的启发来源，可将近期的人本元启发式算法分为社会交互模型和认知规划模型两类。

#### **2.1 社会交互模型 (Social Interaction Models)**

此类算法通过模拟群体间的学习、影响与协同机制来驱动优化过程，旨在通过信息共享与分工协作提升全局搜索效率和鲁棒性。

*   **粒子群优化-社会影响算法 (PSO-Social Influence, PSOSI):**
    该研究针对传统粒子群优化（PSO）易陷入局部最优的问题，提出了一种改进机制 [pdf.hanspub.org](https://pdf.hanspub.org/csa_1543619.pdf)。其核心方法是在粒子速度更新公式中引入“种群中心位置”作为额外的社会影响因子，模拟个体决策受到群体整体趋势（或社会共识）引导的现象。该方法增强了粒子跳出局部最优区域的能力，促进了种群多样性。在CEC-2022标准测试集及多个工程设计问题上的实验表明，PSOSI在优化精度和收敛稳定性上均显著优于标准PSO及多种对比算法（如HHO、WOA），验证了社会影响机制在提升全局寻优性能上的有效性。

*   **双种群协同进化约束多目标优化算法 (TCCMOA):**
    该研究旨在解决具有复杂可行域的约束多目标优化问题（CMOPs），这类问题要求在满足复杂约束的同时平衡多个冲突目标 [aas.net.cn](https://aas.net.cn/cn/article/doi/10.16383/j.aas.c250023)。其核心方法是建立一个双种群协同进化框架，其中“粒子群”负责快速收敛，“向量群”负责维护多样性，两者通过信息共享与优势互补进行协同搜索。这种设计模拟了团队中不同角色的分工与协作，有效地平衡了算法的选择压力，避免了在复杂约束下的早熟收敛。在多达73个基准和真实世界问题上的测试结果显示，TCCMOA能够快速收敛至约束前沿，同时保持良好的种群多样性，性能超越了多种先进的CMOPs求解算法。

*   **人机协同型决策框架 (Human-Machine Collaborative Framework):**
    区别于纯粹的算法模拟，该研究将人的角色直接纳入决策环路，构建了人机融合智能决策的系统性框架 [jeit.ac.cn](https://www.jeit.ac.cn/cn/article/doi/10.11999/JEIT250260)。该框架依据人机关系将决策模式划分为人类主导、机器主导和人机协同三类，通过态势感知与协同决策两大模块实现人机优势互补。人类提供直觉判断与伦理考量，机器负责高速计算与数据分析，形成闭环反馈。该框架的价值体现在军事指挥、自动驾驶等高风险领域，其应用证明了人机融合决策在提升准确性、可解释性和系统鲁棒性方面的独特优势。

#### **2.2 认知与规划模型 (Cognitive and Planning Models)**

此类算法借鉴人类的推理、规划和问题求解等高级认知过程，特别是借助大型语言模型（LLM）的兴起，在自动算法设计领域取得了突破性进展。

*   **基于蒙特卡洛树搜索的自动启发式设计 (MCTS-AHD):**
    此项研究针对现有基于LLM的自动启发式设计（AHD）方法存在的贪婪性和早熟收敛问题 [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/100577)。核心方法是采用蒙特卡洛树搜索（MCTS）来代替传统进化计算中的种群结构，MCTS模拟了人类在决策空间中的探索性规划过程。该方法在树结构中保留所有由LLM生成的候选启发式算法，通过选择、扩展、模拟和反向传播等步骤进行全面探索，避免了因过早丢弃“看似”低质量的解而陷入局部最优。关键实验结论表明，在旅行商问题（TSP）、背包问题（KP）等NP难组合优化任务上，MCTS-AHD生成的启发式算法质量显著高于包括Funsearch在内的其他先进AHD方法。

*   **经验引导的提示与启发式反思共进化 (EvoPH):**
    该研究同样聚焦于利用LLM自动设计启发式算法，旨在解决搜索过程易于停滞在局部最优的挑战 [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/192842)。EvoPH框架的核心是一种新颖的“反思共进化”机制，其中LLM的提示（Prompts）与生成的启发式算法共同演化，并受性能反馈的指导，模拟了人类从经验中学习和反思的迭代优化过程。该框架结合了岛屿迁移模型与精英选择策略，以维持多样化的启发式算法种群。在旅行商问题和装箱问题上的实验结果证实，EvoPH相较于基线方法实现了最低的相对误差，推动了基于LLM的自动算法设计领域的发展。

*   **多智能体强化学习 (MARL) 的决策视角:**
    一项发表于《自动化学报》的综述系统性地探讨了多智能体强化学习（MARL）在控制与决策中的应用 [aas.net.cn](https://aas.net.cn/cn/article/doi/10.16383/j.aas.c240392?viewType=HTML)。MARL通过对多个智能体间的协作与博弈进行建模，本质上是在模拟一个去中心化的社会决策系统。其关注的核心问题——环境动态性与他者策略的不确定性——与人类社会中的复杂决策场景高度相似。因此，MARL中的诸多概念，如博弈论、协同控制和序列决策，为从计算层面理解和构建高级人本优化算法提供了重要的理论基础和工具。

### **3. 实验与评价总结**

综合分析近期研究，可以总结出以下共性实验与评价范式：
*   **评测基准：** 算法性能的验证普遍依赖两类基准：一是学术界公认的标准化测试函数集，如CEC系列（例如 CEC2022），用于全面评估算法在不同特性（多峰、非线性、高维等）问题上的寻优能力 [pdf.hanspub.org](https://pdf.hanspub.org/csa_1543619.pdf)；二是来源于现实世界的工程设计优化问题，如弹簧设计、车辆路径规划（CVRP）、装箱问题（BPP）等，用于检验算法的实用性和处理约束的能力 [aas.net.cn](https://aas.net.cn/cn/article/doi/10.16383/j.aas.c250023), [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/100577)。

*   **评价指标：** 性能评估通常采用多维度指标。**优化精度**（多次运行的最优值均值）和**收敛稳定性**（标准差）是核心度量。此外，为了确保结论的统计学意义，**Wilcoxon秩和检验**和**Friedman检验**等非参数统计检验被广泛用于比较不同算法间的性能是否存在显著差异。

*   **共性结论：**
    1.  **社会/协同机制提升全局搜索能力：** 融入了社会影响、协同进化或多群体协作机制的算法（如PSOSI、TCCMOA）在避免早熟收敛和提升全局搜索性能方面，普遍优于其基线版本或结构单一的对比算法。
    2.  **认知模型在自动算法设计上取得突破：** 基于LLM和认知规划模型（如MCTS-AHD、EvoPH）的方法在自动生成高质量启发式算法方面表现出巨大潜力，其性能在多个NP难问题上能够超越传统AHD方法，甚至逼近或超过专门训练的深度学习模型。
    3.  **人机融合关注多维价值：** 对于人机融合框架的评估，除了传统的优化精度，更加强调**决策过程的可解释性、系统的鲁棒性以及在不确定环境下的适应性**，这些在高风险应用场景中至关重要 [jeit.ac.cn](https://www.jeit.ac.cn/cn/article/doi/10.11999/JEIT250260)。

### **4. 趋势与挑战**

展望 2025 年前后，人本元启发式算法的研究呈现出以下几个明确的趋势与相伴的挑战：

1.  **从行为模拟到认知融合的深化：** 算法设计的灵感来源正从模拟宏观的社会行为（如鸟群、狼群）转向模拟更深层次的人类认知功能（如推理、规划、反思、创造）。以MCTS-AHD为代表的研究，将LLM作为认知引擎，结合MCTS进行规划，是这一趋势的力证 [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/100577)。**挑战**在于如何精确地建模复杂认知过程，以及如何高效地在计算资源受限的情况下实现这些模型。

2.  **人机在环的智能决策系统成为主流：** 未来的优化系统将不再是完全自主的“黑箱”，而是更加强调与人类专家进行高效交互的“白箱”或“灰箱”。人机融合智能框架 [jeit.ac.cn](https://www.jeit.ac.cn/cn/article/doi/10.11999/JEIT250260) 预示着未来的优化算法需具备动态任务分配、双向反馈和信任建立等能力。**挑战**在于如何设计高效、低延迟的人机交互接口，并建立可靠的人机信任与责任分配机制。

3.  **大语言模型驱动的“元优化”：** 利用LLM自动设计和优化“优化算法”本身，正成为一个前沿研究方向。EvoPH等工作展示了LLM不仅能生成候选解，还能通过反思和进化来优化求解策略本身 [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/192842)。**挑战**在于LLM生成内容的“幻觉”问题可能导致代码不可靠或逻辑错误，同时，高昂的API调用成本和计算延迟限制了其在实时或大规模迭代场景中的应用。

4.  **多策略与多智能体协同的复杂化：** 面对日益复杂的约束多目标问题，采用单一策略的算法已显不足。双种群协同进化 [aas.net.cn](https://aas.net.cn/cn/article/doi/10.16383/j.aas.c250023) 和通用进化元启发式框架（GEM） [themoonlight.io](https://www.themoonlight.io/zh/review/a-generalized-evolutionary-metaheuristic-gem-algorithm-for-engineering-optimization) 的提出，表明了向多策略、多智能体混合系统发展的趋势。**挑战**在于如何设计高效的种群间/策略间信息交互机制，并自适应地平衡不同组件的贡献。

### **5. 结论**

在2022至2025年间，面向优化问题的人本元启发式算法研究经历了深刻的范式演进。研究重点已从简单的社会行为模拟，扩展至与大型语言模型、人机交互等前沿AI技术深度融合的认知与协同层面。社会交互模型通过引入更精巧的协同机制，有效提升了全局搜索性能；而认知规划模型则在自动算法设计领域开辟了全新的道路。尽管在模型可解释性、计算成本和人机信任等方面仍面临挑战，但将人类的认知优势与机器的计算能力相结合，构建高效、鲁棒且可信赖的优化系统，无疑是该领域未来发展和应用的核心方向。

### **6. 参考文献**

[1] 李哲, 王可, 王彪, 等. 人机融合智能决策：概念、框架与应用[J]. 电子与信息学报. [jeit.ac.cn](https://www.jeit.ac.cn/cn/article/doi/10.11999/JEIT250260)
[2] 罗彪, 胡天萌, 周育豪, 等. 多智能体强化学习控制与决策研究综述[J]. 自动化学报, 2025, 51(3): 510-539. [aas.net.cn](https://aas.net.cn/cn/article/doi/10.16383/j.aas.c240392?viewType=HTML)
[3] Zhou Liuchang. 面向全局优化的种群中心引导型粒子群优化算法[J]. 计算机科学与应用, 2025, 15(5): 173-183. [pdf.hanspub.org](https://pdf.hanspub.org/csa_1543619.pdf)
[4] Ding Weichao, Sun Liye, Luo Fei, et al. 面向复杂可行域约束多目标优化问题的双种群协同进化算法[J]. 自动化学报, 2025. [aas.net.cn](https://aas.net.cn/cn/article/doi/10.16383/j.aas.c250023)
[5] Zheng Z, Xie Z, Wang Z, et al. Monte Carlo Tree Search for Comprehensive Exploration in LLM-Based Automatic Heuristic Design[J]. arXiv preprint arXiv:2501.08603, 2025. [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/100577)
[6] Liu Y, Li J, Zhao W X, et al. Experience-guided reflective co-evolution of prompts and heuristics for automatic algorithm design[J]. arXiv preprint arXiv:2509.24509, 2025. [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/192842)
[7] Pan Jiawen, Zhai Weixin, Guo Zhou, et al. 基于空间衰减自扩散机制的黏菌遗传混合算法[J]. 北京大学学报(自然科学版), 2025, 61(1). [xbna.pku.edu.cn](https://xbna.pku.edu.cn/fileup/0479-8023/HTML/2025-1-14.html)
[8] Yang X S. A Generalized Evolutionary Metaheuristic (GEM) Algorithm for Engineering Optimization[J]. arXiv preprint arXiv:2407.02113, 2024. [themoonlight.io](https://www.themoonlight.io/zh/review/a-generalized-evolutionary-metaheuristic-gem-algorithm-for-engineering-optimization)
[9] 董祥千, 肖铮. 基于Puma算法引导帕累托前沿的高效多目标提示优化方法[J]. 计算机应用研究, 2025, 42(10): 3041-3052. [arocmag.cn](https://www.arocmag.cn/abs/2025.03.0074)
[10] 何永康, 李旭芳. 邻域搜索和改进莱维因子的人工蜂鸟优化算法[J]. 建模与仿真, 2024, 13(02): 987-1003. [image.hanspub.org](https://image.hanspub.org/Html/1-2571228_81778.htm)
[11] 梁星星, 冯旸赫, 马扬, 等. 多Agent深度强化学习综述[J]. 自动化学报, 2020, 46(12): 2537-2557. [aas.net.cn](https://aas.net.cn/cn/article/doi/10.16383/j.aas.c240392?viewType=HTML)
[12] Gronauer S, Diepold K. Multi-agent deep reinforcement learning: A survey[J]. Artificial Intelligence Review, 2022, 55(2): 895-943. [aas.net.cn](https://aas.net.cn/cn/article/doi/10.16383/j.aas.c240392?viewType=HTML)