# Human-based Metaheuristic Algorithms in Optimization Problems: A Review of Representative Works (2022–2025)

## 引言

Human-based元启发式算法（Human-based Metaheuristic Algorithms, HMAs）是一类受人类学习、社会行为或认知过程启发而设计的优化方法。这类算法通过模拟人类解决问题的策略——如记忆、推理、合作与竞争等机制——来引导搜索过程，以期在复杂优化问题中实现探索（exploration）与开发（exploitation）的有效平衡。近年来，随着对群体智能和认知科学交叉研究的深入，HMAs在组合优化、工程设计、机器学习超参数调优等领域展现出独特优势。本文聚焦于2022至2025年间发表于顶会、顶刊及arXiv平台的代表性工作，系统梳理其方法创新、实验验证及发展趋势，旨在为后续研究提供理论参考与实践指引。

## 方法分类与代表作

### 1. 基于人类学习与记忆机制的优化

张翼鹏等人（2024）针对多维背包问题（MKP）求解精度低、稳定性差的问题，提出一种新型人类学习优化算法（Human Learning Optimization, HLO）[arocmag.cn](https://www.arocmag.cn/abs/2024.04.0127)。该方法引入哈希函数模拟人类记忆行为以避免重复搜索，并结合认知心理学中的对比认知理论自适应调整学习算子选择策略，同时采用变邻域搜索提升局部能力。在76个标准MKP实例（涵盖小至超大规模）上的实验表明，新算法在求解四种规模问题时均显著优于传统HLO、二进制PSO和遗传算法，尤其在超大规模算例上展现出更强的稳定性与收敛性。

齐铖等人（2024）提出的基于精英引导的社会学习粒子群优化算法（ESLPSO）[jnwpu.org](https://www.jnwpu.org/articles/jnwpu/pdf/2024/05/jnwpu2024425p948.pdf)，将粒子按适应度分为精英与平民，构建分层拓扑结构。算法采用Cubic混沌映射初始化以增强初始多样性，并设计精英引导的社会学习策略，结合极值扰动迁移机制激励粒子探索新区域。在12个基准函数上的对比实验显示，ESLPSO在收敛精度和跳出局部最优能力方面显著优于8种主流PSO变体，尤其在多峰和旋转多峰函数上表现突出。

周刘长（2025）针对标准PSO易陷入局部最优的问题，提出面向全局优化的种群中心引导型粒子群优化算法（PSOSI与PSOLP）[hanspub.org](https://pdf.hanspub.org/csa_1543619.pdf)。PSOSI引入种群中心位置作为额外引导信息，而PSOLP则基于种群聚集度触发局部扰动。在CEC-2022标准测试集及8个工程设计问题上的评估表明，两种算法在优化精度和收敛稳定性上均优于标准PSO及多种先进对比算法，其中PSOSI整体表现更优。

### 2. 融合多策略与协同进化的框架

丁炜超等人（2025）针对复杂可行域约束多目标优化问题（CMOPs）中选择压力与多样性难以平衡的挑战，提出双种群协同进化算法（TCCMOA）[aas.net.cn](https://aas.net.cn/cn/article/doi/10.16383/j.aas.c250023)。该框架并行维护粒子群（用于快速收敛）和向量群（用于维持多样性），前者采用带辅助档案的PSO并引入逃逸机制，后者使用无约束参考向量法引导进化。在73个基准与真实世界问题上的实验验证了TCCMOA能在保持多样性的同时快速收敛到约束前沿，性能超越多种SOTA对比算法。

Liu等人（2025）提出经验引导的提示与启发式算法的反思共进化框架（EvoPH）[chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/192842)，用于自动算法设计。该框架将岛屿迁移模型与精英选择相结合，使大型语言模型（LLMs）驱动的提示（prompts）与启发式算法共同演化，并受性能反馈指导。在旅行商问题（TSP）和装箱问题（Bin Packing）上的实验表明，EvoPH相对于最优解的平均相对误差最低，有效缓解了LLM驱动方法易陷入局部最优的问题。

### 3. 基于混合机制的新型算法

潘家文等人（2025）针对黏菌算法（SMA）勘探与开发不平衡的问题，提出基于空间衰减自扩散机制的黏菌遗传混合算法（SMAGA）[pku.edu.cn](https://xbna.pku.edu.cn/fileup/0479-8023/HTML/2025-1-14.html)。该算法以遗传算法为框架，设计了兼具正负反馈和随机游走特性的振荡收缩机制作为交叉算子，并提出随算法生命周期衰减的空间尺度自扩散机制作为变异算子。在CEC2017和CEC2021基准集上与23种算法的对比表明，SMAGA在优化精度上至少领先一个数量级，尤其在高维问题上展现出优异的鲁棒性。

许佳璐等人（2025）针对工业机器人运动学参数标定中蜣螂优化算法（DBO）全局探索能力不足的问题，提出多策略融合蜣螂优化算法（MSFDBO）[cjournal.hep.com.cn](https://cjournal.hep.com.cn/1004-132X/CN/1160171567385862339)。该算法结合Piecewise混沌映射与精英反向学习初始化种群，融入鱼鹰探索行为以增强全局搜索，并通过随机扰动机制扩大搜索范围。对4台T6A-19型机器人的实验验证了其有效性，绝对位置平均误差和均方根误差分别降低了85.47%和83.92%。

## 实验与评价总结

综合分析2022–2025年的代表性工作，其共性实验结论可归纳为：（1）几乎所有新算法均在标准基准测试集（如CEC系列、MKP标准库）上与至少5种SOTA算法进行对比，验证其普适性；（2）性能评价指标不仅包括最终解的质量（如平均值、最优值），还强调稳定性（标准差）和收敛速度（收敛曲线）；（3）统计检验（如Wilcoxon秩和检验、Friedman检验）已成为验证性能差异显著性的标配，确保结论的科学性；（4）算法在真实工程问题（如机器人标定、光伏模型参数识别、压力容器设计）上的有效性被普遍重视，体现了从理论到应用的闭环验证。

## 趋势与挑战

基于对近期文献的分析，2025年前后的研究趋势呈现以下三点：（1）**人机协同的自动化算法设计**：如EvoPH所示，利用LLMs等大模型自动生成和优化启发式算法，将成为解决特定领域优化问题的新范式；（2）**多目标与约束处理的深度整合**：针对复杂可行域的CMOPs，双种群、多档案等协同进化策略将与更精细的约束处理技术（如动态ε-约束）深度融合；（3）**认知科学与优化的交叉深化**：将更多来自认知心理学（如工作记忆、注意力机制）的理论模型引入优化算法设计，以提升算法的智能性与自适应能力。

主要挑战在于：如何构建更具可解释性的HMA模型，以及如何在保持算法通用性的同时，有效适配特定问题的结构先验。

## 结论

2022–2025年间，Human-based元启发式算法研究在方法创新与应用拓展上取得了显著进展。通过融合社会学习、记忆机制、多策略协同及混合框架，新一代HMAs在解决复杂单/多目标优化问题上展现出卓越性能。未来，随着人机协同和认知科学的进一步发展，HMAs有望在自动化算法设计与高维复杂工程优化等领域发挥更大作用。

## 参考文献

1. 张翼鹏, 刘勇, 马良. 多维背包问题的新型人类学习优化算法. 计算机应用研究, 2024, 41(12): 3689-3700. [arocmag.cn](https://www.arocmag.cn/abs/2024.04.0127)
2. 齐铖, 谢军伟, 王雪, 等. 基于精英引导的社会学习粒子群优化算法. 西北工业大学学报, 2024, 42(5): 948-958. [jnwpu.org](https://www.jnwpu.org/articles/jnwpu/pdf/2024/05/jnwpu2024425p948.pdf)
3. 周刘长. 面向全局优化的种群中心引导型粒子群优化算法. 计算机科学与应用, 2025, 15(5): 173-183. [hanspub.org](https://pdf.hanspub.org/csa_1543619.pdf)
4. 丁炜超, 孙立烨, 罗飞, 等. 面向复杂可行域约束多目标优化问题的双种群协同进化算法. 自动化学报, 2025, 51(8): 1-21. [aas.net.cn](https://aas.net.cn/cn/article/doi/10.16383/j.aas.c250023)
5. Liu, Y., Li, J., Zhao, W. X., et al. Experience-guided reflective co-evolution of prompts and heuristics for automatic algorithm design. arXiv:2509.24509, 2025. [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/192842)
6. 潘家文, 翟卫欣, 郭舟, 等. 基于空间衰减自扩散机制的黏菌遗传混合算法. 北京大学学报(自然科学版), 2025, 61(1): 14-25. [pku.edu.cn](https://xbna.pku.edu.cn/fileup/0479-8023/HTML/2025-1-14.html)
7. 许佳璐, 刘笑楠, 李朋超, 等. 基于多策略融合蜣螂优化算法的工业机器人运动学参数辨识方法. 中国机械工程, 2025, 36(2): 294-304. [cjournal.hep.com.cn](https://cjournal.hep.com.cn/1004-132X/CN/1160171567385862339)
8. 王乐遥, 顾磊. 多策略融合改进的蜣螂优化算法. 计算机系统应用, 2024, 33(2): 224-231. [c-s-a.org.cn](https://www.c-s-a.org.cn/1003-3254/9397.html)
9. 付海涛, 张智勇, 王增辉, 等. 改进SHO算法优化随机森林模型. 吉林大学学报(理学版), 2025, 63(3): 861-866. [cjournal.hep.com.cn](https://cjournal.hep.com.cn/1671-5489/CN/10.13413/j.cnki.jdxblxb.2024003)
10. Cheng, R., & Jin, Y. A social learning particle swarm optimization algorithm for scalable optimization. Information Sciences, 2015, 291: 43-60. (作为ESLPSO的基础)
11. Liang, J. J., Qin, A. K., Suganthan, P. N., & Baskar, S. Comprehensive learning particle swarm optimizer for global optimization of multimodal functions. IEEE Transactions on Evolutionary Computation, 2006, 10(3): 281-295. (作为PSOSI/PSOLP的对比基础)
12. Deb, K., Thiele, L., Laumanns, M., & Zitzler, E. Scalable test problems for evolutionary multiobjective optimization. In Evolutionary Multiobjective Optimization. Springer, 2005: 105-145. (作为TCCMOA的基准问题来源)