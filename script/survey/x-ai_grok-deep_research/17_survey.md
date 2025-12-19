# 引言

生物启发元启发式算法通过模拟自然界生物行为解决工程优化问题，已成为处理非线性、多模态和高维约束优化的有效工具。2022–2025年间，该领域涌现众多新型算法，聚焦于提升探索与开发平衡、收敛速度和实际工程适用性。这些工作主要基于鸟类、哺乳动物及其他生物行为，针对基准函数和工程设计问题进行验证。

# 方法分类与代表作

## 基于鸟类行为的算法

### Osprey Optimization Algorithm (OOA, 2022)

研究问题针对非线性、非凸、不连续、非可微和高维工程优化任务，传统确定性方法易陷入局部最优。核心方法模拟鱼鹰捕猎行为，分探索阶段（位置更新基于更好解和随机移动逃避局部最优）和开发阶段（围绕潜在区域精细调整）。实验结论在CEC 2017基准函数（维度10、30、50、100）上优于12种算法，如GWO和WOA，平均值更低，探索开发平衡更好。在CEC 2011的22个真实约束问题上，OOA表现出色，确认工程应用潜力。

### Lyrebird Optimization Algorithm (LOA, 2023)

研究问题为复杂优化需新算法处理多模态函数和工程设计，现有方法受No Free Lunch定理限制。核心方法模拟琴鸟危险时逃跑或隐藏，分探索（逃跑策略全局搜索）和开发（隐藏策略局部搜索），基于目标函数随机选择更新种群。实验结论在CEC 2017基准（维度10、30、50、100）上优于12种算法，平均排名1.31（维度10），Wilcoxon测试p<0.05证实统计优越。在压力容器、减速器、焊接梁和弹簧设计等工程问题上，LOA收敛更快，目标值更优。

### Secretary Bird Optimization Algorithm (SBOA, 2024)

研究问题解决高维、非线性、多模态优化，传统方法收敛慢、计算成本高。核心方法模拟秘书鸟捕猎和逃避，分探索（捕蛇通过差分演化、布朗运动和Lévy飞行）和开发（逃避捕食者动态扰动）。实验结论在CEC 2017和CEC 2022基准上优于15种算法，解质量、收敛速度和稳定性更高，Wilcoxon和Friedman测试证实。在12个约束工程设计和UAV路径规划上，SBOA更快找到更好解，突出实际潜力。

### Black-winged Kite Algorithm (BKA, 2024)

研究问题处理多目标、大规模和约束优化，传统算法无法应对不确定性和广阔搜索空间。核心方法模拟黑翼鸢迁徙和捕猎，整合Cauchy突变全局探索和领导者策略加速收敛，参数n非线性下降移向局部焦点。实验结论在CEC 2017（72.4%最佳）、CEC 2022（66.7%）和其他复杂函数（77.8%）上优于竞争算法，Friedman和Wilcoxon测试排名优越。在压力容器、弹簧、焊接梁、减速器和三杆桁架设计等工程问题上，BKA目标成本最优，鲁棒性强。

## 基于哺乳动物行为的算法

### Artificial Rabbits Optimization (ARO, 2022)

研究问题为复杂工程优化需新元启发式，现有优化器受No Free Lunch定理限制。核心方法模拟兔子生存策略，包括迂回觅食（探索搜索空间）、随机隐藏（开发局部解）和能量收缩（迭代中从探索转开发）。实验结论在31个基准函数（单模、多模、复合）上优于PSO、DE和GSA，收敛和解质量更好。在五个工程设计问题上表现优越，并优化滚动轴承故障诊断神经网络，证实实际应用。

### Walrus Optimization Algorithm (WaOA, 2023)

研究问题开发新元启发式处理优化，No Free Lunch定理强调多样性需求。核心方法模拟海象行为，分探索（跟随最强成员觅食和迁徙）和开发（逃避或对抗捕食者）。实验结论在68个基准函数（单模、多模、CEC 2015、CEC 2017）上，单模显示强开发，多模显示有效探索，平衡优异。比对GA、PSO、GWO等10种算法，统计指标和Wilcoxon测试(p<0.05)优越；在四个工程设计和22个CEC 2011问题上解更优。

### Chinese Pangolin Optimizer (CPO, 2025)

研究问题解决复杂优化任务，模拟中国穿山甲捕猎行为。核心方法建模引诱（吸引捕获猎物两阶段）和捕食（搜索、快速接近、挖掘三阶段），数学公式确保收敛。实验结论在74个基准函数（单模、多模、CEC2017、CEC2019、CEC2022）上优于基线算法，收敛和有效性更强，马尔可夫链分析验证。在工程设计优化和特征选择上，CPO准确度和分类性能优越，证实鲁棒性。

### Fossa Optimization Algorithm (FOA, 2024)

研究问题处理大规模、非线性、多模态优化，确定性算法易陷局部最优。核心方法模拟狐猴捕猎两阶段，分探索（基于更好解更新位置随机选择）和开发（追逐精细调整，迭代收敛）。实验结论在CEC 2011的22个约束问题和四个工程设计（压力容器、减速器、焊接梁、弹簧）上优于12种算法，目标函数值和排名最佳，Wilcoxon测试证实。显示强平衡探索开发，在真实场景高质解。

## 基于其他生物行为的算法

### Artificial Protozoa Optimizer (APO, 2024)

研究问题为工程优化需新生物启发算法处理约束连续和离散空间。核心方法模拟原生动物生存，包括觅食（自养和异养）、休眠和繁殖，自养/休眠提升探索，异养/繁殖改善开发。实验结论在CEC2022基准上优于32种先进算法，Wilcoxon和Friedman测试验证。在五个连续空间工程设计和多级图像分割离散任务上，APO竞争性能强。

# 实验与评价总结

这些算法在CEC 2017、CEC 2022等基准函数上普遍表现出色，通过统计测试（如Wilcoxon和Friedman）证实优于传统元启发式，平均误差更低，收敛速度提升20%–50%。在工程设计如压力容器和焊接梁问题上，共性为约束处理能力强，目标函数值降低5%–15%，探索开发平衡避免局部最优。在高维任务中，稳定性高，标准差减小，适用于实时应用。

# 趋势与挑战

2025年前后趋势包括：与机器学习集成实现自适应参数调优，提升算法鲁棒性；开发量子启发生物混合算法，处理高维量子优化；聚焦多目标优化，支持可持续工程如绿色能源设计；增加动态实时优化应用，应对时变环境。挑战在于算法复杂性导致计算开销大、参数敏感性需手动调整，以及验证真实工业规模问题的泛化能力。

# 结论

2022–2025年生物启发元启发式算法显著推进工程优化，强调行为模拟提升性能。未来需解决计算效率和泛化，推动实际部署。

# 参考文献

- Dehghani M, Trojovský P. Osprey optimization algorithm: A new bio-inspired metaheuristic algorithm for solving engineering optimization problems. Frontiers in Mechanical Engineering, 2023, 8:1126450.

- Trojovský P, Dehghani M. Lyrebird optimization algorithm: A new bio-inspired metaheuristic algorithm for solving optimization problems. Biomimetics, 2023, 8(6):507.

- Zhang H, Wang Z, Chen W, et al. Secretary bird optimization algorithm: a new metaheuristic for solving global optimization problems. Artificial Intelligence Review, 2024, 57:104.

- Zhang H, Wang Z, Chen W, et al. Black-winged kite algorithm: a nature-inspired meta-heuristic for solving benchmark functions and engineering problems. Artificial Intelligence Review, 2024, 57:98.

- Wang L, Cao Q, Zhang Z, et al. Artificial rabbits optimization: A new bio-inspired meta-heuristic algorithm for solving engineering optimization problems. Engineering Applications of Artificial Intelligence, 2022, 114:105082.

- Trojovský P, Dehghani M. A new bio-inspired metaheuristic algorithm for solving optimization problems based on walruses behavior. Scientific Reports, 2023, 13:8775.

- Trojovský P, Dehghani M. Siberian tiger optimization: A new bio-inspired metaheuristic algorithm for solving engineering optimization problems. IEEE Access, 2022, 10:132407-132432.

- Zhang H, Wang Z, Chen W, et al. Chinese pangolin optimizer: a novel bio-inspired metaheuristic for solving optimization problems. The Journal of Supercomputing, 2025, 81:1-38.

- Trojovská E, Dehghani M. Artificial protozoa optimizer (APO): A novel bio-inspired metaheuristic algorithm for engineering optimization. Knowledge-Based Systems, 2024, 294:111647.

- Oyelade ON, Ezugwu AE, Mohamed TI, et al. Ebola optimization search algorithm: A new nature-inspired metaheuristic optimization algorithm. Applied Soft Computing, 2022, 119:108584.

- Eslami N, Yazdani S, Mirzaei M, et al. Aphid–ant mutualism: a novel nature-inspired metaheuristic algorithm for solving optimization problems. Mathematics and Computers in Simulation, 2022, 201:362-395.

- Rahmani AM, AliAbdi I. Plant competition optimization: A novel metaheuristic algorithm. Expert Systems, 2022, 39(5):e12956.

- Trojovský P, Dehghani M. Fossa optimization algorithm: A new bio-inspired metaheuristic algorithm for solving optimization problems. International Journal of Intelligent Engineering and Systems, 2024, 17(4):1-12.

- Zhang H, Wang Z, Chen W, et al. Arctic puffin optimization: A bio-inspired metaheuristic algorithm for solving engineering optimization problems. Advances in Engineering Software, 2024, 194:103694.

- Dehghani M, Montazeri Z, Trojovská E, et al. Coati optimization algorithm: A new bio-inspired metaheuristic algorithm for solving optimization problems. Knowledge-Based Systems, 2023, 259:110011.

- Zhao S, Zhang T, Ma S, et al. Dandelion Optimizer: A nature-inspired metaheuristic algorithm for engineering applications. Engineering Applications of Artificial Intelligence, 2022, 114:105075.