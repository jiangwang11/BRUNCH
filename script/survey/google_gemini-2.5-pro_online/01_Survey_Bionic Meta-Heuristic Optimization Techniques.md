好的，作为一名严谨的科研助手，我将基于提供的真实网络搜索结果，为您生成一篇关于“仿生元启发式优化技术”的学术综述。

***

### **仿生元启发式优化技术（2022–2025年）研究综述**

#### **引言**

仿生元启发式优化算法（Bionic Meta-heuristic Optimization Algorithms）是一类通过模拟自然界中生物群体的智能行为或物理现象来求解复杂优化问题的计算方法 [[sjcj.nuaa.edu.cn](https://sjcj.nuaa.edu.cn/html/2018/4/20180411.htm)]。这些算法因其不依赖问题梯度信息、鲁棒性强以及内在的并行性，在传统数学方法难以处理的高维度、非线性和多模态优化问题上展现出巨大潜力。近年来，特别是2022至2025年间，该领域的研究呈现出三大趋势：1）受新生物现象启发的新型算法不断涌现；2）深度融合与改进现有算法的混合策略日益复杂；3）与大型语言模型（LLM）等前沿人工智能技术交叉融合，开辟了自动算法设计的新范式。本综述旨在梳理此期间的代表性工作，总结其评价方法与共性，并展望未来的研究趋势与挑战。

#### **方法分类与代表作**

##### **1. 新型群体智能算法**

研究者持续从自然界中发掘新的灵感，以构建具有独特搜索机制的优化算法。

*   **蝎子狩猎策略算法 (Scorpion Hunting Strategy, SHS)**：该研究旨在提出一种全新的自然启发式优化算法，以有效平衡探索（Exploration）与利用（Exploitation）能力 [[hub.baai.ac.cn](https://hub.baai.ac.cn/paper/3ee713e8-0bda-47c8-a489-741dbd75f252)]。SHS算法通过数学建模模拟蝎子利用α和β振动算子来识别、定位和捕捉猎物的行为，从而控制算法在解空间中的搜索动态。在20个基准函数（含CEC2020）上的实验表明，其性能在Wilcoxon秩和检验与Friedman测试中均显著优于12种现有先进元启发式算法。此外，该算法在六个真实世界优化任务中的成功应用，也验证了其解决复杂问题的实用性。

*   **减法平均优化器 (Subtraction-Average-Based Optimizer, SABO)**：该算法旨在开发一种数学启发而非直接生物模拟的、兼具高效收敛速度与强大寻优能力的元启发式方法 [[blog.sciencenet.cn](https://blog.sciencenet.cn/blog-3516770-1445795.html)]。SABO的核心机制是通过计算种群中所有个体位置的平均值，并从每个个体中减去该平均值的加权形式来更新其位置，从而引导种群向最优解区域移动。在包含52个标准测试函数（含CEC 2017）的评估中，SABO在大部分函数上均取得了优于12种对比算法的结果。其在压力容器设计等工程问题上的应用也显示出较高的求解效率。

##### **2. 混合与改进型元启发算法**

通过融合多种算法优势或引入新的机制来改进现有算法，是提升优化性能的主流方向。

*   **改进人工蜂鸟优化算法 (ALAHA)**：该工作针对标准人工蜂鸟算法（AHA）寻优精度低、易陷入局部最优的问题进行改进 [[image.hanspub.org](https://image.hanspub.org/Html/1-2571228_81778.htm)]。ALAHA引入了两大核心策略：一是受鲸鱼优化算法启发的自适应距离围猎搜索，根据种群适应度方差触发，以增强局部搜索精度；二是通过非线性收敛因子改进的莱维飞行（Lévy Flight）来替代原步长因子，以强化全局探索能力。在23个基准测试函数上的对比实验表明，ALAHA在寻优能力、稳定性及鲁棒性上均优于标准AHA及灰狼优化器（GWO）等算法。

*   **黏菌遗传混合算法 (SMAGA)**：此研究旨在解决元启发式算法普遍存在的勘探与开发不平衡问题，特别是针对黏菌算法（SMA）全局搜索能力弱的缺陷 [[xbna.pku.edu.cn](https://xbna.pku.edu.cn/fileup/0479-8023/HTML/2025-1-14.html)]。SMAGA以遗传算法（GA）为基础框架，将SMA中具有正负反馈的振荡收缩机制改进为交叉算子，并创新性地提出一种基于空间衰减的自扩散机制作为变异算子。同时，算法通过判别式控制策略自适应调整交叉与变异概率。在IEEE CEC2017和CEC2021测试集上的实验显示，与23种算法相比，SMAGA的优化精度至少存在一个数量级的优势。

*   **改进黑翅鸢智能优化算法 (IBKA)**：此项工作旨在提升2024年新提出的黑翅鸢优化算法（BKA）的综合性能 [[blog.csdn.net](https://blog.csdn.net/hustef/article/details/144065972)]。研究者集成了四种改进策略：采用混沌映射改善种群初始化的多样性，引入精英反向学习和透镜成像反向学习加速收敛，并利用黄金正弦变异策略来避免算法陷入局部最优。在CEC系列标准测试函数上的对比实验证明，该多策略改进版本相较于原始BKA及GWO、鲸鱼优化算法（WOA）等经典算法，具有更强的寻优性能。

##### **3. 与大型语言模型融合的自动算法设计**

将元启发式优化的思想与大型语言模型（LLM）相结合，用于自动设计或优化算法/提示，是2024–2025年间最前沿的探索方向。

*   **经验引导的提示与启发式共进化框架 (EvoPH)**：该研究致力于解决利用LLM自动设计启发式算法时易陷入局部最优的难题 [[chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/192842)]。EvoPH框架提出让提示（Prompts）与启发式算法（Heuristics）在性能反馈的引导下进行反思性共进化。该框架利用岛屿迁移模型和精英选择算法来维持多样化的启发式算法种群，实现算法的自动生成与迭代优化。在旅行商问题（TSP）和装箱问题（BPP）上的实验显示，EvoPH生成的算法相较于最优解实现了最低的相对误差。

*   **基于蒙特卡洛树搜索的自动启发式设计 (MCTS-AHD)**：该工作针对现有基于LLM的自动启发式设计（AHD）方法中，种群进化机制因其贪心特性而导致的局部最优问题，提出了替代方案 [[chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/100577)]。MCTS-AHD使用蒙特卡洛树搜索（MCTS）代替传统的种群进化过程，在树结构中保留所有由LLM生成的启发式方法，从而实现对解空间更全面的探索。通过新颖的思维对齐过程和探索衰减技术，该方法能够在多种复杂任务上生成质量显著更高的启发式方法。

*   **基于Puma算法的多目标提示优化 (Puma-MOPT)**：此研究旨在解决现有提示工程方法在多目标优化场景下的可扩展性与自适应性局限 [[www.arocmag.cn](https://www.arocmag.cn/abs/2025.03.0074)]。Puma-MOPT框架将新型仿生算法——美洲狮算法（Puma Algorithm）的自适应相位切换和全局搜索能力，与提示生成及评估机制相结合，实现了对提示词的自动多目标权衡搜索。为提高效率，该框架还引入了语义相似性约束与对抗性过滤技术。在数学推理、代码生成等五个领域的实验结果表明，该框架在多项评估指标上均显著优于NSGA-II及EvoPrompt等基线方法。


#### **实验与评价总结**

综合分析2022–2025年的代表性工作，其在实验设计与性能评价上呈现出高度的规范性和严谨性，具体共性如下：
1.  **基准测试集的广泛应用**：绝大多数新算法或改进算法的性能验证均在国际公认的、高难度的标准测试函数集上进行，特别是IEEE进化计算大会（CEC）发布的系列测试集（如CEC2017、CEC2020、CEC2021）。这些测试集包含单峰、多峰、混合及复合等多种复杂特性的函数，能够全面评估算法的勘探、开发及平衡能力 [[xbna.pku.edu.cn](https://xbna.pku.edu.cn/fileup/0479-8023/HTML/2025-1-14.html)]。
2.  **严格的统计学检验**：为确保结论的科学性，研究者普遍采用非参数统计检验方法（如Wilcoxon秩和检验、Friedman检验）来比较算法间的性能差异。在设定的显著性水平（通常为α=0.05）下，判断新算法的优势是否具有统计学意义，避免了仅凭单次最优值或平均值比较带来的偶然性 [[image.hanspub.org](https://image.hanspub.org/Html/1-2571228_81778.htm), [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/3ee713e8-0bda-47c8-a489-741dbd75f252)]。
3.  **多维度的性能指标**：评价指标通常包括多次独立运行得到的最优值（Best）、平均值（Avg）和标准差（Std）。这三个指标分别用于衡量算法的峰值寻优能力、平均性能和稳定性。部分研究通过对比收敛曲线，直观分析算法的收日志速度和跳出局部最优的能力 [[xbna.pku.edu.cn](https://xbna.pku.edu.cn/fileup/0479-8023/HTML/2025-1-14.html)]。
4.  **面向实际问题的验证**：除了在抽象的数学函数上进行测试，越来越多的研究倾向于将新提出的算法应用于解决具体的工程或科学问题，如光伏模型参数辨识 [[xbna.pku.edu.cn](https://xbna.pku.edu.cn/fileup/0479-8023/HTML/2025-1-14.html)]、组合优化问题 [[chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/192842)] 以及多智能体协同控制 [[aas.net.cn](https://aas.net.cn/cn/article/doi/10.16383/j.aas.c240392?viewType=HTML)]，以此证明算法的现实应用价值。

#### **趋势与挑战**

基于2025年前后的研究成果，仿生元启发式优化领域呈现出以下明确的研究趋势与并存的挑战：

1.  **趋势一：与大语言模型（LLM）和生成式AI的深度交叉**。元启发式算法正从单纯的“求解器”向“设计器”演进。研究不再局限于手动设计算法，而是利用LLM的推理和生成能力，自动构建、变异和选择解决特定问题的启发式策略（如EvoPH和MCTS-AHD）[[chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/192842), [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/100577)]。反之，元启发式算法也被用于优化LLM的提示（Prompt），以应对复杂的多目标需求（如Puma-MOPT）[[www.arocmag.cn](https://www.arocmag.cn/abs/2025.03.0074)]。
    *   **挑战**：该融合方向面临计算成本高昂、生成结果的稳定性和可解释性差等问题。如何高效地引导LLM生成高质量且可信的算法逻辑，是当前的核心挑战。

2.  **趋势二：自适应混合策略的精密化**。单一的仿生模拟已难以满足复杂优化需求。当前的主流是设计高度集成的混合算法，通过融合不同算法的优势算子（如SMAGA）或叠加多种改进机制（如ALAHA、IBKA）来提升性能 [[xbna.pku.edu.cn](https://xbna.pku.edu.cn/fileup/0479-8023/HTML/2025-1-14.html), [image.hanspub.org](https://image.hanspub.org/Html/1-2571228_81778.htm)]。其核心在于“自适应”，即算法参数（如交叉/变异率、步长）能够根据种群多样性、收敛状态等实时反馈进行动态调整，从而实现勘探与开发能力的智能平衡。
    *   **挑战**：算法的复杂度显著增加，导致理论分析变得困难。“无免费午餐”定理 [[xbna.pku.edu.cn](https://xbna.pku.edu.cn/fileup/0479-8023/HTML/2025-1-14.html)] 指出，不存在普适最优的算法。如何理解各组件在特定问题上的贡献，并进行有效的“算法选择”或“组件配置”，成为新的难题。

3.  **趋势三：向多智能体强化学习（MARL）与多目标优化拓展**。群体智能与多智能体系统（MAS）在概念上同源，二者的融合正在加深。元启发式算法被视为解决MARL中信用分配、策略探索和通信协调等问题的潜在框架 [[aas.net.cn](https://aas.net.cn/cn/article/doi/10.16383/j.aas.c240392?viewType=HTML)]。同时，算法的设计目标正从单目标优化转向更具现实意义的多目标优化（Multi-objective Optimization），要求算法不仅能找到单个最优解，还要能有效逼近和维护帕累托前沿（Pareto Front）[[www.arocmag.cn](https://www.arocmag.cn/abs/2025.03.0074)]。
    *   **挑战**：在多智能体环境中，环境的非平稳性（Non-stationarity）为算法收敛带来巨大困难。在多目标优化中，如何高效地维持解的分布性和收敛性，尤其是在高维目标空间中，仍是开放性问题。

#### **结论**

在2022至2025年间，仿生元启发式优化领域经历了从提出新型算法、改进现有算法到与人工智能前沿技术深度融合的快速演进。研究工作在方法论上愈发精细化和混合化，在实验评估上愈发规范化和严格化。特别是与大型语言模型的结合，为“自动算法设计”这一宏伟目标开辟了全新的路径。尽管面临着理论分析困难、计算成本高昂以及在多智能体和多目标场景下的收敛性挑战，但该领域展现出的强大生命力和广阔的应用前景预示着其在未来科学与工程计算中将继续扮演不可或缺的角色。

#### **参考文献**
1.  [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/192842) Liu, Y., Li, J., Zhao, W. X., Lu, H., & Wen, J. R. (2025). Experience-guided reflective co-evolution of prompts and heuristics for automatic algorithm design. *arXiv preprint arXiv:2509.24509*.
2.  [blog.sciencenet.cn](https://blog.sciencenet.cn/blog-3516770-1445795.html) Trojovský, P., & Dehghani, M. (2023). Subtraction-Average-Based Optimizer (SABO). *Biomimetics*.
3.  [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/3ee713e8-0bda-47c8-a489-741dbd75f252) Singh, A., Mousavi, S. M. H., & Gaurav, K. (2024). SHS: Scorpion Hunting Strategy Swarm Algorithm. *arXiv preprint*.
4.  [image.hanspub.org](https://image.hanspub.org/Html/1-2571228_81778.htm) 何永康, & 李旭芳. (2024). 邻域搜索和改进莱维因子的人工蜂鸟优化算法. *建模与仿真*, *13*(02), 987-1003.
5.  [www.arocmag.cn](https://www.arocmag.cn/abs/2025.03.0074) 董祥千, & 肖铮. (2025). 基于Puma算法引导帕累托前沿的高效多目标提示优化方法. *计算机应用研究*, *42*(10), 3041-3052.
6.  [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/100577) Zheng, Z., Xie, Z., Wang, Z., & Hooi, B. (2025). Monte Carlo Tree Search for Comprehensive Exploration in LLM-Based Automatic Heuristic Design. *arXiv preprint arXiv:2501.08603*.
7.  [blog.csdn.net](https://blog.csdn.net/hustef/article/details/144065972) 小熊科研路. (2024). 【2024新算法多策略综合改进】改进黑翅鸢智能优化算法IBKA与BKA-WOA-GWO-PSO算法对比研究. *CSDN博客*.
8.  [xbna.pku.edu.cn](https://xbna.pku.edu.cn/fileup/0479-8023/HTML/2025-1-14.html) 潘家文, 翟卫欣, 郭舟, 胡班韶, 程承旗, & 吴才聪. (2025). 基于空间衰减自扩散机制的黏菌遗传混合算法. *北京大学学报(自然科学版)*, *61*(1).
9.  [sjcj.nuaa.edu.cn](https://sjcj.nuaa.edu.cn/html/2018/4/20180411.htm) 陈喆, 耿国胜, 崔行悦, 殷拓, & 殷福亮. (2018). 基于仿生学的优化算法及其在信号处理中的应用. *数据采集与处理*, *33*(4), 662-682.
10. [aas.net.cn](https://aas.net.cn/cn/article/doi/10.16383/j.aas.c240392?viewType=HTML) 罗彪, 胡天萌, 周育豪, 黄廷文, 阳春华, & 桂卫华. (2025). 多智能体强化学习控制与决策研究综述. *自动化学报*, *51*(3), 510-539.
11. [image.hanspub.org](https://image.hanspub.org/Html/1-2571228_81778.htm) Zhao, W. G., Wang, L. Y., & Mirjalili, S. (2022). Artificial hummingbird algorithm: A new bio-inspired optimizer with its engineering applications. *Computer Methods in Applied Mechanics and Engineering*, *388*, 114194.
12. [xbna.pku.edu.cn](https://xbna.pku.edu.cn/fileup/0479-8023/HTML/2025-1-14.html) Li, S., Chen, H., Wang, M., Heidari, A. A., & Mirjalili, S. (2020). Slime mould algorithm: A new method for stochastic optimization. *Future Generation Computer Systems*, *111*, 300-323.
13. [blog.csdn.net](https://blog.csdn.net/hustef/article/details/144065972) Wang, J., et al. (2024). Black Kite Optimization (BKA). *Artificial Intelligence Review*.