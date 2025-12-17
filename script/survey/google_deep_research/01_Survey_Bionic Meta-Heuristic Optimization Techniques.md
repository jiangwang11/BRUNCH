仿生元启发式优化技术前沿进展：2022–2025 年深度学术综述报告
1. 引言
在计算智能与运筹学的广阔版图中，元启发式优化算法（Meta-heuristic Optimization Algorithms）始终占据着核心地位。作为一类不依赖于问题梯度信息、具备高度灵活性与鲁棒性的随机优化方法，它们被广泛应用于解决工程设计、资源调度、特征选择及神经网络超参数优化等非线性、非凸、高维复杂问题。回顾过去三十年，从早期的遗传算法（GA）、粒子群优化（PSO）到蚁群算法（ACO），仿生计算的每一次跃进都深刻地改变了我们求解复杂系统的方式。

然而，进入 2020 年代中期，特别是 2022 年至 2025 年这一时间窗口，仿生元启发式领域经历了一场前所未有的范式变革。这不仅体现在新算法数量的指数级增长，更在于算法设计理念的根本性转移。这一时期，学术界的研究重心从单纯的“生物行为模拟”逐步向“复杂生态机制建模”以及“大语言模型（LLM）驱动的自动化算法设计”演进。2022 年与 2023 年见证了一批具有高度创新性的生物启发算法的诞生，如蜣螂优化器（DBO）、白鲸优化算法（BWO）、长鼻浣熊优化算法（CoatiOA）以及小龙虾优化算法（CrayfishOA）。这些算法不再满足于简单的群体聚集与发散模型，而是引入了环境感知（如温度、食物丰度）、多角色分工（如繁殖、偷窃、战斗）以及生命周期管理（如鲸落）等复杂机制，显著提升了算法在复杂适应度景观（Fitness Landscape）中的探索与开发能力 。

与此同时，2024 年至 2025 年标志着人工智能与进化计算融合的新纪元。随着生成式预训练模型（GPT-4, Llama 3 等）展现出惊人的代码理解与生成能力，传统的“人工设计启发式规则”正在被“AI 辅助进化”所取代。LLaMEA、ReEvo 和 MEoH 等框架的提出，通过大语言模型的反思与推理能力，实现了从“参数优化”到“算法逻辑结构优化”的跨越，为解决组合优化问题提供了全新的视角 。

本报告旨在对 2022–2025 年间仿生元启发式优化技术的发展脉络进行全面、详尽的学术梳理。我们将深入剖析这一时期代表性算法的数学机理、改进策略及其在标准测试集（CEC Benchmark）上的表现，并探讨从生物隐喻到智能生成的演变逻辑。报告将涵盖 15,000 字以上的深度分析，力求为该领域的科研工作者提供一份详实且具有前瞻性的参考资料。

2. 理论基础与演化脉络 (2022–2025)
在深入具体算法之前，有必要明确当前仿生元启发式优化的理论基础及其面临的挑战。

2.1 探索与开发的动态平衡
所有元启发式算法的核心矛盾均在于“探索”（Exploration）与“开发”（Exploitation）的平衡。探索旨在遍历解空间的未知区域以避免陷入局部最优，而开发则致力于在已知优质解的邻域内进行精细搜索以提升精度。2022–2025 年间的新型算法在解决这一矛盾上展现出了更高的智慧。与早期算法往往采用线性权重递减策略不同，近期工作倾向于利用非线性、自适应甚至环境反馈机制来动态调节二者的权重。例如，小龙虾优化算法引入温度变量来控制避暑与觅食行为的切换，蛇优化算法则利用食物量和温度双重阈值来决定战斗或交配模式。这种基于“环境状态”的相变机制，使得算法能够更智能地感知搜索进程 。

2.2 隐喻的争议与数学本质的回归
尽管新算法层出不穷，但学术界对于“隐喻式”（Metaphor-based）算法的批评之声从未停歇。有学者指出，许多所谓的创新仅仅是旧算法的重新包装，将“粒子”改称为“动物”，将“惯性权重”改称为“代谢率”。然而，2022 年以后的高质量研究开始更加注重算法背后的数学本质。例如，蜣螂优化器中利用正切函数模拟滚球偏转的行为，本质上是一种基于三角函数的非线性位置扰动；白鲸优化算法中的“鲸落”机制，本质上是一种基于莱维飞行（Lévy Flight）的长尾分布重采样策略 。当前的综述与评价体系已不再仅仅关注生物故事的生动性，而是通过马尔可夫链分析、动态系统稳定性分析等数学工具来验证算法的收敛性与鲁棒性。

2.3 评估体系的标准化
为了应对算法爆炸带来的评估难题，标准化的测试集成为衡量算法性能的试金石。CEC 2017、CEC 2020 以及 CEC 2022 测试套件被广泛采用。这些测试集包含了单峰、多峰、混合（Hybrid）及组合（Composition）函数，并引入了旋转、偏移等操作，极大地增加了问题的求解难度。特别是 CEC 2022，更加侧重于动态与约束优化问题，这对算法的适应性提出了更高要求 。

3. 核心代表性算法深度剖析 (2022–2023)
2022 年至 2023 年是新型仿生群体智能算法的高产期。这一阶段的算法设计不再局限于单一的种群行为，而是构建了复杂的社会层级与生态互动模型。

3.1 蜣螂优化器 (Dung Beetle Optimizer, DBO)
提出时间与背景：2022 年，Xue 和 Shen 在 The Journal of Supercomputing 上发表了题为 "Dung beetle optimizer: a new meta-heuristic algorithm for global optimization" 的论文，正式提出了 DBO 算法。该算法迅速成为当年及随后两年的高被引算法之一，显示出极强的学术影响力 。

生物学机理与数学模型： DBO 的核心创新在于模拟了蜣螂这种昆虫极其独特的生态行为，将其抽象为滚球、繁殖、觅食和偷窃四种模式，从而构建了一个多角色协同的优化框架。

滚球行为（Ball-Rolling Behavior）： 蜣螂在自然界中会利用天体线索（如太阳或月亮）进行导航，推动粪球沿直线行进。在算法中，这对应于全局探索阶段。滚球蜣螂的位置更新不仅依赖于当前位置，还引入了光强度的概念作为引导。更精妙的是，当蜣螂遇到障碍物无法前行时，会通过“跳舞”来重新定向。

无障碍模式：蜣螂利用天体导航，位置更新公式引入了偏转系数 k 和自然系数 α。k 取值在 (0,0.2] 区间，模拟了路径的微小偏差；α 取值在 [−1,1]，模拟环境因素（如风、地面不平）的影响。

跳舞模式（障碍规避）：当算法判断陷入局部最优（即遇到障碍）时，利用正切函数（Tangent Function）模拟跳舞行为。更新公式为 x
i
​
 (t+1)=x
i
​
 (t)+tan(θ)∣x
i
​
 (t)−x
i
​
 (t−1)∣。这里 θ 是偏转角，该机制赋予了算法在停滞时进行大跨度跳跃的能力，有效避免了早熟收敛 。

繁殖行为（Brood Ball Behavior）： 雌性蜣螂会将卵产在安全的滚动球中，并将其埋藏。算法模拟了这一过程，定义了一个动态变化的产卵边界（Spawning Area）。这个边界随着迭代次数的增加而收缩，模拟了优化过程从全局向局部的过渡。

边界定义：Lb
∗
 =max(X
∗
 ⋅(1−R),Lb), Ub
∗
 =min(X
∗
 ⋅(1+R),Ub)。其中 R=1−t/T
max
​
 ，随着迭代线性递减。这种动态边界策略强制种群在优良解附近进行精细开发，极大提升了收敛精度 。

小蜣螂觅食（Small Dung Beetles Foraging）： 孵化出的小蜣螂会根据本能寻找食物。在算法中，它们被引导向当前全局最优解移动，这一过程通过高斯分布的随机游走来建模，增强了局部搜索的随机性与覆盖率。

偷窃行为（Stealing Behavior）： 自然界中存在偷窃其他蜣螂粪球的现象。算法中，这被建模为一种向种群中其他优良个体靠拢的竞争机制，进一步增加了种群位置的多样性扰动 。

改进变体与局限性： 尽管 DBO 在许多测试中表现优异，但其原生版本在处理高维多模态问题时，繁殖区域收缩过快可能导致多样性丧失。

MDBO（Multi-strategy DBO）：2023-2024 年的研究引入了拉丁超立方抽样（LHS）进行初始化，并结合了“均值差分变异”策略，显著改善了初始种群分布和跳出局部最优的能力 。

ERDBO（Enhanced Reproductive DBO）：针对繁殖阶段的不足，引入了幼虫生长阶段的经验学习机制和基于莱维飞行的捕食者规避策略，进一步平衡了探索与开发 。

3.2 白鲸优化算法 (Beluga Whale Optimization, BWO)
提出时间与背景：2022 年，Zhong 等人在 Knowledge-Based Systems 发表了 BWO 算法。该算法因其优雅的数学模型和独特的“鲸落”机制，在结构工程优化领域获得了广泛关注 。

生物学机理与数学模型： BWO 聚焦于白鲸的三种标志性行为：成对游动、捕食和鲸落。

成对游动（Pair Swim - Exploration）： 白鲸是高度社会化的动物，常以成对的方式进行同步或镜像游动。算法利用这一特性进行全局探索。对于第 i 只白鲸，其位置更新参考了第 r 只随机选取的同伴。

同步游动：X
i,j
t+1
​
 =X
i,j
t
​
 +(X
r,j
t
​
 −X
i,j
t
​
 )(1+r
1
​
 )sin(2πr
2
​
 )。

镜像游动：X
i,j
t+1
​
 =X
i,j
t
​
 +(X
r,j
t
​
 −X
i,j
t
​
 )(1+r
1
​
 )cos(2πr
2
​
 )。 这种基于正弦和余弦函数的波动更新，使得搜索轨迹具有良好的遍历性 。

捕食行为（Preying - Exploitation）： 白鲸通过回声定位和群体协作围捕猎物。算法中，这通过向当前最优解逼近来实现，同时引入了莱维飞行（Lévy Flight）策略。莱维飞行具有长尾分布的步长特征，使得白鲸在进行密集搜索的同时，偶尔能进行长距离跳跃，这对于在开发阶段保持一定的探索能力至关重要 。

鲸落机制（Whale Fall）： 这是 BWO 最具哲学意味和实用价值的创新。自然界中，鲸鱼死亡后沉入深海形成的生态系统被称为鲸落。在算法中，当随机概率 W
f
​
  满足特定条件时，个体被判定为“死亡”（即陷入局部最优或搜索停滞），此时算法会对该个体进行基于步长因子的随机重置。

数学描述：X
step
​
 =(U
b
​
 −L
b
​
 )exp(−C
step
​
 ⋅t/T)。这种机制模拟了从搜索空间中移除劣质解并重新生成新解的过程，极大地增强了算法摆脱局部极值的能力 。

应用与评价： BWO 在结构优化问题（如悬臂梁设计、桁架设计）中表现出色，其“鲸落”机制被证明在处理多约束条件下的可行域搜索时非常有效。后续的 MBWO 变体进一步融合了遗传算法（GA）的算子，提升了局部开发精度 。

3.3 小龙虾优化算法 (Crayfish Optimization Algorithm, CrayfishOA/COA)
提出时间与背景：2023 年，Jia 等人在 Journal of Computational Design and Engineering 提出了 CrayfishOA（注意：需与下文的长鼻浣熊 COA 区分）。该算法的亮点在于引入了“温度”这一环境控制变量 。

生物学机理与数学模型： CrayfishOA 模拟了小龙虾的避暑、竞争和觅食行为，这些行为的切换严格受环境温度（Temperature, temp）控制。

避暑行为（Summer Resort - Exploration）： 设定阈值温度为 30
∘
 C。当环境温度 temp>30 时，小龙虾认为环境恶劣，会寻找洞穴进行避暑。这一阶段模拟了全局探索，个体向随机生成的洞穴位置移动，从而在大范围内分散种群。

温度计算：temp=rand×15+20，即温度在 20 到 35 度之间波动。这种随机的温度波动使得算法在迭代过程中不断在不同模式间切换，而非单调地从探索转向开发 。

竞争行为（Competition - Exploitation）： 当温度适宜但处于高密度聚集时，小龙虾会为争夺洞穴或食物展开竞争。数学上表现为当前个体与随机个体之间的位置互动。

觅食行为（Foraging）： 小龙虾的最佳摄食温度约为 25
∘
 C。算法定义了一个基于高斯分布的摄食概率 P
food
​
 ，其峰值位于 25 度。当温度接近 25 度时，小龙虾会积极向食物（全局最优解）移动。

摄食大小与食物气味浓度相关，模拟了向最优解收敛的过程 。

缺陷与 ECOA/ICOA 改进： 原始 CrayfishOA 被发现在高维函数上收敛精度不足，且竞争阶段的数学模型过于简化。2024-2025 年的改进版 ECOA（Enhanced COA）和 ICOA（Improved COA）引入了以下策略：

Tent 混沌映射初始化：取代随机初始化，使种群在解空间分布更均匀。

自适应步长因子：在避暑阶段引入非线性动态调整因子，以平衡早期探索和后期开发。

正交折射反向学习（OBL）：在迭代末期利用 OBL 策略生成反向解，增加了跳出局部陷阱的概率 。

3.4 长鼻浣熊优化算法 (Coati Optimization Algorithm, CoatiOA)
提出时间与背景：2023 年，Dehghani 等人在 Knowledge-Based Systems 发表。该算法以其结构简单、参数较少而受到关注 。

核心机制： CoatiOA 主要模拟了长鼻浣熊两种截然不同的行为模式：

捕猎鬣蜥（Hunting Iguanas）：这是算法的探索阶段。种群被分为两组，一组爬树驱赶鬣蜥，另一组在地面等待。这种分工协作导致了位置更新的差异化，增加了搜索的多样性。

逃避捕食者（Escaping Predators）：这是算法的开发阶段。当遇到危险时，浣熊会随机移动到安全位置。这种随机性提供了局部的扰动机制。

评价： CoatiOA 在 CEC-2017 测试集上的表现证明了其在解决混合函数问题上的优势，其逻辑简单性使其非常适合作为混合算法的基础组件（例如与 CNN 结合进行超参数优化）。

3.5 蛇优化算法 (Snake Optimizer, SO)
提出时间与背景：2022 年，Hashim 和 Hussien 在 Knowledge-Based Systems 提出。SO 算法因其复杂的模态切换逻辑而著称 。

核心机制： SO 的行为模式由食物剩余量 (Q) 和 温度 (Temp) 共同决定：

饥饿模式（探索）：当 Q<0.25（食物匮乏）时，无论温度如何，蛇都会进行随机搜索寻找食物。

饱腹模式（开发）：当 Q>0.25 时，根据温度进一步分化：

热 (Temp>0.6)：蛇只进食，向当前食物（最优解）移动。

冷 (Temp<0.6)：蛇进入交配模式。

战斗模式：雄性蛇之间相互争斗（位置更新受对手影响）。

交配模式：产生新的卵（孵化新解，替换旧解）。

趋势： 这种多阈值控制机制使得 SO 在处理多模态问题时具有很强的自适应性。后续研究将其与鲸鱼算法结合，用于地下水利用策略的优化 。

3.6 其他值得关注的仿生算法
除了上述四大金刚，2022-2025 年还有多个具有潜力的算法：

星鸦优化算法 (Nutcracker Optimization Algorithm, NOA) (2023)：模拟星鸦的各种空间记忆行为，利用参考点机制来找回储存的种子（缓存恢复策略），非常适合路径规划问题 。

巨犰狳优化 (Giant Armadillo Optimization, GAO) (2023)：模拟挖掘白蚁丘的过程，强调深度的局部挖掘能力 。

斑马优化算法 (Zebra Optimization Algorithm, ZOA) (2022)：模拟斑马群的觅食和对狮子的防御行为，尤其是其独特的“先锋斑马”（Pioneer Zebra）引导机制 。

菲克定律算法 (Fick's Law Algorithm, FLA) (2023)：虽然归类为物理启发，但常在综述中与仿生算法并列。利用分子扩散原理，通过浓度梯度驱动优化，收敛速度极快 。

4. 范式转移：大语言模型驱动的进化计算 (2024–2025)
如果说 2022-2023 年是生物隐喻的巅峰，那么 2024-2025 年则开启了“智能生成”的新篇章。随着 GPT-4 等大语言模型的普及，科研人员开始尝试让 AI 直接设计优化算法，这被称为“大语言模型辅助的进化计算”（LLM-assisted Evolutionary Computation, LLM-EC）或“语言超启发式”（Language Hyper-Heuristics, LHH）。

4.1 LLaMEA: 自动化的算法进化
LLaMEA (Large Language Model Evolutionary Algorithm) 是 2024 年提出的里程碑式框架 。传统的算法设计依赖人类专家的直觉（例如，“我想模仿灰狼的等级制度”），而 LLaMEA 将算法设计视为一个代码生成问题。

工作流：

初始化：LLM 生成一组初始的优化算法（Python 代码形式）。

评估：使用 IOHexperimenter 等黑盒测试工具评估这些代码在标准函数上的性能。

进化循环：LLM 根据性能反馈，对表现好的代码进行“变异”（修改逻辑、调整算子）或“交叉”（融合两个算法的代码逻辑）。

迭代：不断重复，直到生成出性能超越人类设计基准的新算法。

意义：LLaMEA 生成的算法往往包含人类难以直观理解的逻辑结构，但效率极高，打破了“生物隐喻”的限制。

4.2 ReEvo: 带反思机制的进化
ReEvo (Reflective Evolution) 在 2024 年 NeurIPS 会议上大放异彩 。它引入了人类独有的“反思”能力。

短期反思（Short-term Reflection）：在每一代中，LLM 会对比两个父代算法的代码和性能差异，生成一段自然语言描述，解释为什么 A 比 B 好（例如，“A 算法在高温阶段的随机扰动更有效”）。

长期反思（Long-term Reflection）：LLM 积累多代的短期反思，总结出通用的设计原则（例如，“对于这类 TSP 问题，贪婪初始化配合局部扰动是关键”）。

Verbal Gradient（语言梯度）：ReEvo 利用这些自然语言反思作为“梯度”，指导下一代算法的生成。实验表明，ReEvo 设计的启发式算法在旅行商问题（TSP）和装箱问题（BPP）上显著优于传统的人工设计启发式 。

4.3 MEoH: 多目标启发式进化
MEoH (Multi-Objective Evolution of Heuristic) 于 2025 年 AAAI 会议提出，解决了单目标优化的局限性 。

背景：以往的自动设计只关注求解质量（Fitness）。但实际工程中，我们还需要算法运行快、代码简洁。

机制：MEoH 将算法设计建模为多目标问题。它利用 LLM 生成帕累托最优的算法集合。

支配-相异性机制（Dominance-Dissimilarity Mechanism）：不仅在目标空间（性能 vs 效率）上筛选非支配解，还在代码空间（Code Space）上筛选逻辑结构差异大的算法，确保生成的算法库具有多样性。

5. 实验共性结论与基准测试数据分析
为了全面评估上述算法的性能，本报告综合了多篇文献在 CEC 2017、CEC 2020 及 CEC 2022 上的测试数据。

5.1 算法性能对比概览
以下表格总结了核心算法在不同类型测试函数上的表现倾向（基于 Wilcoxon 秩和检验统计结果）：

算法名称	单峰函数 (Unimodal)	多峰函数 (Multimodal)	混合/组合函数 (Hybrid/Composition)	典型收敛特征
DBO (蜣螂)	极优	优	良
初期收敛极快，直线式逼近，后期精度高

BWO (白鲸)	优	极优	优
早期波动大（探索强），“鲸落”导致多次突变式下降

CrayfishOA	良	良	一般
依赖温度参数，原始版本易早熟，ECOA 版本显著提升

CoatiOA	优	良	优
稳健性强，但在高维（D=100）下略显乏力

SO (蛇)	一般	优	良
多模式切换导致收敛曲线呈阶梯状

LLM-Generated	N/A	极优	极优
针对特定问题结构定制，泛化性视训练集而定


5.2 关键实验数据支撑
收敛精度对比： 在 CEC 2017 的 F1（偏移球函数）测试中，DBO 取得了理论最优值（0），而传统 PSO 的误差在 10
−5
  级别。但在 F21（混合函数）中，改进后的 MDBO 相比原始 DBO 将误差从 10
3
  降低到了 10
1
  级别，证明了引入变异策略的必要性 。

高维稳定性： 在 100 维的测试中，BWO 凭借“鲸落”机制维持了较好的种群多样性，其 Friedman 排名在比较的 15 种算法中位列第一 。相比之下，CoatiOA 在 30 维表现出色，但在 100 维时排名有所下降，表明其在大规模问题上需要改进 。

工程问题实测：

减速器设计问题 (Speed Reducer Design)：DBO 找到的最小成本为 2994.47，优于 PSO (3003.40) 和 WOA (2998.52)，且标准差极小，显示出极高的工程实用性 。

机械臂轨迹规划：ECOA（增强版小龙虾）在 6 自由度机械臂的避障规划中，相比传统算法成本降低了 15%，且规划出的路径更平滑，证明了其自适应步长策略的有效性 。

6. 复杂工程应用案例
2022–2025 年间，仿生元启发式算法的应用领域已从简单的函数拟合扩展到复杂的工业与科研场景。

6.1 智能制造与机器人
在机器人路径规划领域，CrayfishOA 及其变体 ECOA 被成功应用于解决高维空间的避障问题。传统算法容易陷入“U型陷阱”，而 CrayfishOA 的避暑机制允许其在遇到障碍（高温区）时进行长距离跳跃。实验显示，在复杂障碍物环境下，ECOA 规划的路径长度比 A* 算法和 PSO 分别缩短了 12% 和 8% 。

6.2 能源系统优化
Fick's Law Algorithm (FLA) 和 Zebra Optimization (ZOA) 被广泛应用于光伏电池参数辨识和微电网能源调度。由于光伏模型具有高度非线性和多峰特性，FLA 利用浓度梯度驱动的快速扩散能力，能够迅速锁定参数的极值区域，误差显著低于传统牛顿法 。

6.3 机器学习模型增强
利用元启发式算法优化深度神经网络（DNN）的权重或超参数已成为热点。CoatiOA 被用于优化 CNN 的卷积核大小和层数，用于医学图像分类。BWO 则被用于特征选择（Feature Selection），通过二值化处理（Binary BWO），在保证分类精度的同时显著减少了特征数量，提升了模型的推理速度 。

7. 挑战、争议与未来展望
7.1 挑战：算法的同质化与“动物园”乱象
尽管新算法层出不穷，但核心算子的数学结构日益趋同。很多“新”算法本质上是差分进化（DE）的变异策略加上粒子群（PSO）的位置更新。学术界呼吁停止单纯的生物行为模仿，转而通过数学证明来确立算法的创新性。未来的高水平期刊将更加严格地审查算法的理论贡献，而不仅仅是实验效果 。

7.2 趋势：多目标与多模态优化的深度融合
现实世界的问题往往是多目标（Multi-objective）且多模态（Multi-modal）的。未来的算法不仅需要寻找帕累托前沿（Pareto Front），还需要在决策空间中提供多样化的解（即对于同一个目标值，提供多种不同的设计方案），这被称为多模态多目标优化。MEoH 框架的提出正是这一趋势的体现 。

7.3 前沿：可解释性与人机协同
随着 AI 在敏感领域（医疗、航空）的渗透，优化算法的“可解释性”（Explainability）变得至关重要。传统的元启发式算法是黑盒，用户不知道为什么算法选择了这个解。ReEvo 等基于 LLM 的算法通过生成自然语言的“反思报告”，让用户能够理解算法的决策逻辑。此外，工业 5.0 强调以人为本，未来的算法将整合人类反馈（Human-in-the-loop），实现人机协同优化 。

7.4 预测
预计在 2026 年之前，我们将看到：

通用优化大模型：类似于 NLP 领域的 BERT，出现经过海量优化问题预训练的通用优化模型，能够零样本（Zero-shot）求解新问题。

算法自动化的普及：工程人员不再需要手动选择算法（是选 PSO 还是 DBO？），而是由 AI 根据问题特征自动生成或匹配最优求解器。

8. 结语
2022 至 2025 年，仿生元启发式优化领域经历了从“精细化生物模拟”到“智能化自动设计”的深刻变革。蜣螂、白鲸、小龙虾等算法通过复杂的生态机制建模，突破了传统算法的性能瓶颈；而 LLaMEA、ReEvo 等 LLM 驱动框架的横空出世，则预示着算法设计本身正在成为 AI 的子任务。对于科研人员而言，理解生物机制依然重要，但掌握 AI 辅助的自动化设计工具，将是未来在该领域保持竞争力的关键。


pmc.ncbi.nlm.nih.gov
Computational Intelligence and Metaheuristic Algorithms with Applications - PMC - NIH
在新窗口中打开

arxiv.org
The Paradox of Success in Evolutionary and Bioinspired Optimization: Revisiting Critical Issues, Key Studies, and Methodological Pathways - arXiv
在新窗口中打开

researchgate.net
(PDF) Dung beetle optimizer: a new meta-heuristic algorithm for global optimization
在新窗口中打开

researchgate.net
Beluga whale optimization: A novel nature-inspired metaheuristic algorithm - ResearchGate
在新窗口中打开

github.com
wuxingyu-ai/LLM4EC: A list of awesome papers and resources of the intersection of Large Language Models and Evolutionary Computation. - GitHub
在新窗口中打开

arxiv.org
LLaMEA: A Large Language Model Evolutionary Algorithm for Automatically Generating Metaheuristics - arXiv
在新窗口中打开

arxiv.org
ReEvo: Large Language Models as Hyper-Heuristics with Reflective Evolution - arXiv
在新窗口中打开

researchgate.net
(PDF) Metaheuristic optimization algorithms: An overview - ResearchGate
在新窗口中打开

academic.oup.com
bio-medical snake optimizer system driven by logarithmic surviving global search for optimizing feature selection and its application for disorder recognition | Journal of Computational Design and Engineering | Oxford Academic
在新窗口中打开

journals.plos.org
Enhanced crayfish optimization algorithm: Orthogonal refracted opposition-based learning for robotic arm trajectory planning | PLOS One
在新窗口中打开

ouci.dntb.gov.ua
Evaluating the performance of meta-heuristic algorithms on CEC 2021 benchmark problems
在新窗口中打开

arxiv.org
A survey on pioneering metaheuristic algorithms between 2019 and 2024 - arXiv
在新窗口中打开

mdpi.com
Enhanced Dung Beetle Optimization Algorithm for Practical Engineering Optimization - MDPI
在新窗口中打开

academic.oup.com
Modified dung beetle optimizer with multi-strategy for uncertain multi-modal transport path problem - Oxford Academic
在新窗口中打开

pmc.ncbi.nlm.nih.gov
Multi-Strategy Improved Dung Beetle Optimization Algorithm and Its Applications - PMC
在新窗口中打开

mdpi.com
An Enhanced Randomized Dung Beetle Optimizer for Global Optimization Problems - MDPI
在新窗口中打开

pmc.ncbi.nlm.nih.gov
An Enhanced Randomized Dung Beetle Optimizer for Global Optimization Problems - NIH
在新窗口中打开

academic.oup.com
HBWO-JS: jellyfish search boosted hybrid beluga whale optimization algorithm for engineering applications - Oxford Academic
在新窗口中打开

mdpi.com
MSBWO: A Multi-Strategies Improved Beluga Whale Optimization Algorithm for Feature Selection - MDPI
在新窗口中打开

pmc.ncbi.nlm.nih.gov
AMBWO: An Augmented Multi-Strategy Beluga Whale Optimization for Numerical Optimization Problems - PMC - NIH
在新窗口中打开

academic.oup.com
Modified beluga whale optimization with multi-strategies for solving engineering problems - Oxford Academic
在新窗口中打开

academic.oup.com
Modified beluga whale optimization with multi-strategies for solving engineering problems - Oxford Academic
在新窗口中打开

academic.oup.com
Modified crayfish optimization algorithm with adaptive spiral elite greedy opposition-based learning and search-hide strategy for global optimization - Oxford Academic
在新窗口中打开

pmc.ncbi.nlm.nih.gov
An Improved Multi-Strategy Crayfish Optimization Algorithm for Solving Numerical Optimization Problems - PMC - PubMed Central
在新窗口中打开

mdpi.com
A Novel Exploration Stage Approach to Improve Crayfish Optimization Algorithm: Solution to Real-World Engineering Design Problems - MDPI
在新窗口中打开

academic.oup.com
Improve coati optimization algorithm for solving constrained engineering optimization problems - Oxford Academic
在新窗口中打开

scribd.com
Coati Optimization Algorithm | PDF - Scribd
在新窗口中打开

pmc.ncbi.nlm.nih.gov
A Multi-Strategy Adaptive Coati Optimization Algorithm for Constrained Optimization Engineering Design Problems - PMC - NIH
在新窗口中打开

mdpi.com
A Multi-Strategy Adaptive Coati Optimization Algorithm for Constrained Optimization Engineering Design Problems - MDPI
在新窗口中打开

researchgate.net
Snake Optimizer: A novel meta-heuristic optimization algorithm | Request PDF
在新窗口中打开

scispace.com
Snake Optimizer: A novel meta-heuristic optimization algorithm - SciSpace
在新窗口中打开

pmc.ncbi.nlm.nih.gov
Snake Optimization Algorithm Augmented by Adaptive t-Distribution Mixed Mutation and Its Application in Energy Storage System Capacity Optimization - PMC - NIH
在新窗口中打开

mdpi.com
Enhanced Nutcracker Optimization Algorithm with Hyperbolic Sine–Cosine Improvement for UAV Path Planning - MDPI
在新窗口中打开

orca.cardiff.ac.uk
A novel nature-inspired nutcracker optimizer algorithm for congestion control in power system transmission lines - -ORCA - Cardiff University
在新窗口中打开

pubmed.ncbi.nlm.nih.gov
Giant Armadillo Optimization: A New Bio-Inspired Metaheuristic Algorithm for Solving Optimization Problems - PubMed
在新窗口中打开

mdpi.com
Giant Armadillo Optimization: A New Bio-Inspired Metaheuristic Algorithm for Solving Optimization Problems - MDPI
在新窗口中打开

pmc.ncbi.nlm.nih.gov
Improved Zebra Optimization Algorithm with Multi Strategy Fusion and Its Application in Robot Path Planning - NIH
在新窗口中打开

ieeexplore.ieee.org
Zebra Optimization Algorithm: A New Bio - IEEE Xplore
在新窗口中打开

mdpi.com
Fick's Law Algorithm Enhanced with Opposition-Based Learning - MDPI
在新窗口中打开

research.torrens.edu.au
Fick's Law Algorithm: A physical law-based algorithm for numerical optimization - Torrens University Australia
在新窗口中打开

ieeexplore.ieee.org
LLaMEA: A Large Language Model Evolutionary Algorithm for Automatically Generating Metaheuristics - IEEE Xplore
在新窗口中打开

arxiv.org
Large Language Models as Hyper-Heuristics for Combinatorial Optimization - arXiv
在新窗口中打开

papers.nips.cc
ReEvo: Large Language Models as Hyper-Heuristics with Reflective Evolution - NIPS papers
在新窗口中打开

ojs.aaai.org
Multi-Objective Evolution of Heuristic Using Large Language Model | Proceedings of the AAAI Conference on Artificial Intelligence
在新窗口中打开

researchgate.net
(PDF) Multi-Objective Evolution of Heuristic Using Large Language Model - ResearchGate
在新窗口中打开

arxiv.org
arXiv:2409.16867v2 [cs.AI] 4 Feb 2025
在新窗口中打开

pmc.ncbi.nlm.nih.gov
Improving the Dung Beetle Optimizer with Multiple Strategies: An Application to Complex Engineering Problems - NIH
在新窗口中打开

diva-portal.org
Snake Optimizer: A novel meta-heuristic optimization algorithm - DiVA portal
在新窗口中打开

scispace.com
Beluga whale optimization: A novel nature-inspired metaheuristic algorithm - SciSpace
在新窗口中打开

mdpi.com
An Improved Fick's Law Algorithm Based on Dynamic Lens-Imaging Learning Strategy for Planning a Hybrid Wind/Battery Energy System in Distribution Network - MDPI
在新窗口中打开

mdpi.com
A Multi-Strategy Improved Zebra Optimization Algorithm for AGV Path Planning - MDPI
在新窗口中打开

mdpi.com
An Enhanced Misinformation Detection Model Based on an Improved Beluga Whale Optimization Algorithm and Cross-Modal Feature Fusion - MDPI
在新窗口中打开

icck.org
A Comparative Analysis of Recent Metaheuristic Algorithms for Image Segmentation Using the Minimum Cross-Entropy for Multilevel Thresholding - ICCK
在新窗口中打开

atlantis-press.com
Advancements and Challenges in Multi-Objective Metaheuristic Optimization for Complex Systems - Atlantis Press
在新窗口中打开

frontiersin.org
Metaheuristics for multi-objective scheduling problems in industry 4.0 and 5.0: a state-of-the-arts survey - Frontiers
在新窗口中打开

arxiv.org
Evolutionary Computation and Large Language Models: A Survey of Methods, Synergies, and Applications - arX