生物启发式元启发式算法在工程优化中的前沿进展与应用综述 (2022–2025)
1. 引言
1.1 研究背景与科学意义
随着现代工程系统向着大规模、高集成度和多功能化的方向演进，工程设计问题呈现出前所未有的复杂性。这些问题通常被建模为在多维约束空间内的非线性目标函数最优化任务，诸如航空航天结构的拓扑优化、可再生能源系统的参数辨识、以及大规模云计算中心的资源调度等。传统的确定性数学规划方法，如牛顿法、梯度下降法及其变体，往往依赖于目标函数的连续性、可微性以及凸性假设。然而，现实世界的工程问题往往充斥着非凸性、不可微性、多模态（Multimodality）以及离散决策变量，这使得传统方法极易陷入局部最优解，或者因无法计算梯度而完全失效 。   

面对这一挑战，元启发式算法（Metaheuristic Algorithms）作为一种基于随机搜索的通用优化范式，在过去的二十年中异军突起。这类算法并不追求数学上的绝对最优解，而是致力于在合理的时间成本内寻找足够好的近似解（Near-optimal solution）。特别是生物启发式算法（Bio-inspired Algorithms），通过模拟自然界中生物群体的觅食、求偶、迁徙等社会行为，或者物理世界的自然现象，展现出了卓越的全局勘探（Exploration）与局部开发（Exploitation）平衡能力。根据“没有免费午餐”（No Free Lunch, NFL）定理，没有任何一种单一的算法能够在其所有可能的问题上都表现最优，这为新算法的不断涌现提供了理论上的合理性 。   

1.2 2022–2025 年的发展态势分析
进入2022年以来，生物启发式算法的研究进入了一个爆发式增长的“寒武纪”阶段。这一时期的研究特征不再仅仅局限于对自然界生物行为的简单模仿，而是呈现出深度的机理创新与多学科交叉融合的趋势。文献分析显示，2022至2025年间，学术界在算法设计上更加注重对“勘探”与“开发”动态平衡机制的精细化调控，涌现出了一批具有代表性的新型算法，如蜣螂优化算法（DBO）、蛇优化算法（SO）、雾凇优化算法（RIME）等。这些算法不仅在标准的IEEE CEC基准测试函数上刷新了性能记录，更在复杂的工程约束问题中展示了强大的鲁棒性。

此外，这一时期的研究热点还出现了显著的范式转移。一方面，大语言模型（LLM）的兴起开始重塑算法设计的流程，从人工设计转向AI辅助生成；另一方面，随着全球对可持续发展的关注，算法的应用场景深度拓展到了绿色计算、低碳制造等领域。为了系统梳理这一快速发展领域的最新成果，本综述将重点聚焦于2022年至2025年间发表在顶级会议、期刊及arXiv上的代表性工作，从群智能、物理/植物启发、以及前沿交叉技术三个维度进行深度剖析，并对未来的发展趋势做出预测。

2. 动物群体行为启发的群智能算法进展
群智能（Swarm Intelligence, SI）算法依然是元启发式领域的主流。这一类算法的核心思想在于“由简单的个体规则涌现复杂的群体智能”，通过种群中个体之间的协作与信息共享来逼近全局最优。2022–2025年间，该领域涌现了多种模拟复杂生物社会行为的高效算法。

2.1 蜣螂优化算法 (Dung Beetle Optimizer, DBO)
代表性工作： Xue & Shen (2023) 。 问题背景： 传统的群智能算法在处理高维多模态问题时，往往因种群多样性丧失而过早收敛。为了解决这一问题，研究者将目光投向了蜣螂（屎壳郎）这一自然界中具有独特导航与社会行为的昆虫。 算法机理： DBO算法是2023年提出的现象级算法，其深刻地模拟了蜣螂的五种核心行为：滚球、跳舞、繁殖、觅食和偷窃。   

滚球行为（Ball-rolling）： 蜣螂利用天体线索（如太阳）进行导航，推动粪球沿直线运动。算法模型中，通过引入光强作为引导信号，使蜣螂在搜索空间中进行全局探索。位置更新公式利用了当前位置与全局最优位置的偏差，模拟了滚球过程中的路径修正。

跳舞行为（Dancing）： 当蜣螂遇到障碍物无法前行时，会执行一种“跳舞”行为来重新确定方向。数学上，这通过引入正切函数（Tangent function）来模拟，利用切线角度的变化来改变搜索方向，从而帮助算法跳出局部最优陷阱 。   

繁殖行为（Spawning）： 蜣螂将卵产在安全区域（产卵球）。算法定义了一个动态收缩的“产卵边界”，模拟了随着迭代进行，种群逐渐向优良区域集中的过程，增强了局部开发能力。

觅食与偷窃（Foraging & Stealing）： 孵化出的小蜣螂在产卵区觅食，而偷窃蜣螂则试图抢夺其他蜣螂的粪球。这种竞争机制引入了种群内部的动态扰动。

结论与评价： DBO算法凭借其多角色的分工协作机制，在处理具有强约束的工程问题时表现出色。实验表明，在压力容器设计与焊接梁设计中，DBO及其改进变体（如MDBO、ERDBO）能够以更少的迭代次数找到成本更低的设计方案，显著优于PSO和GWO等经典算法 。然而，原始DBO在迭代后期仍存在一定的陷入局部最优风险，促使了后续基于Levy飞行和混沌映射的改进研究 。   

2.2 蛇优化算法 (Snake Optimizer, SO)
代表性工作： Hashim & Hussien (2022) 。 问题背景： 如何在算法的不同阶段自适应地切换勘探与开发策略，一直是元启发式算法设计的难点。自然界中蛇类的行为模式受环境温度和食物丰度的双重驱动，为解决这一问题提供了绝佳的生物原型。 算法机理： SO算法构建了一个受环境因素驱动的数学模型，主要包含两个阈值参数：温度（Temp）和食物数量（Q）。   

环境驱动的模式切换： 算法首先根据食物数量Q判断进入探索还是开发阶段。当食物稀缺（Q < threshold）时，蛇群执行随机搜索模式，寻找新的食物源（全局勘探）。

两性异形行为（Sexual Dimorphism）： 当食物充足时，算法进一步根据温度决定行为。若温度较低（Temp < 0.6），蛇群进入交配模式。SO算法将种群分为雄性和雌性两组，模拟它们之间的求偶与争斗行为。雄性蛇之间为了争夺配偶会发生打斗（Fighting mode），这引入了位置的随机扰动；而交配行为（Mating mode）则通过雄雌个体的位置交叉产生新的子代（新解）。   

能量利用（Exploitation）： 若温度较高，蛇群则专注于进食，仅在当前最优解附近进行微调。

结论与评价： SO算法创新性地引入了性别分组与环境双因素控制机制，使得算法在多模态景观中具有极强的适应性。在拉伸/压缩弹簧设计和压力容器设计等问题中，SO展现了优异的收敛精度。特别是针对高维问题，其分群策略有效维持了种群多样性，避免了单一最优解主导导致的早熟收敛 。   

2.3 巨鲹优化算法 (Giant Trevally Optimizer, GTO)
代表性工作： Sadeeq & Abdulazeez (2023) 。 问题背景： 针对现有算法在复杂解空间中容易陷入局部极值的问题，研究者从海洋生物巨鲹（Giant Trevally）的高效捕猎策略中汲取灵感。巨鲹不仅能够个体追击，还能进行群体协作，甚至跳出水面捕食飞鸟。 算法机理： GTO算法将巨鲹的捕猎过程数学化为三个阶段：   

广域搜索（Extensive Search）： 模拟巨鲹在广阔海域中寻找猎物的巡游行为。算法利用Levy飞行（Levy Flight）机制模拟巨鲹的随机游走，这种长尾分布的步长特征使得算法能够快速覆盖未探索的区域 。   

区域选择（Area Selection）： 一旦发现猎物踪迹（潜在最优解），群体会收缩搜索范围，聚焦于猎物所在的子区域。

攻击行为（Attacking）： 模拟巨鲹突然加速冲刺并跳出水面捕食海鸟的动作。在数学模型中，这表现为解向量向当前最优解的快速逼近，通过攻击因子控制逼近的速度与精度。

结论与评价： GTO算法在解决悬臂梁设计、三杆桁架设计等结构优化问题时表现出卓越的性能。统计检验（如Wilcoxon秩和检验）结果证实，GTO在收敛速度和最终解的质量上，均优于算术优化算法（AOA）和爬行动物搜索算法（RSA）。其独特的跳跃捕食机制被证明有助于算法在最后阶段进行高精度的局部开发。   

2.4 浣熊优化算法 (Coati Optimization Algorithm, COA)
代表性工作： Dehghani et al. (2023) 。 问题背景： 为了进一步降低算法的计算复杂度并提高实时性，研究者模仿长鼻浣熊（Coati）简单的捕食与逃避天敌行为，设计了COA算法。 算法机理： COA的逻辑简洁而高效，分为两个核心阶段：   

捕猎鬣蜥（Hunting Iguanas）： 这一阶段模拟了浣熊的协作捕猎。半数浣熊爬上树惊吓鬣蜥，迫使其跳落地面；另一半浣熊在地面等待捕食。这种垂直维度的协作在算法中转化为种群位置的大幅度更新与重组，极大地增强了全局勘探能力。

躲避掠食者（Escaping Predators）： 当浣熊遭遇天敌时，会因恐惧而随机逃窜。算法利用这种随机性在局部区域生成微小的扰动，帮助解跳出可能的局部陷阱，并进行精细化搜索 。   

结论与评价： COA以其参数少、结构简单的特点受到关注。在减速器设计（Speed Reducer Design）问题中，COA及其改进版本（如引入T分布变异的TNTWCOA）展示了极高的求解精度，能够精确满足所有齿轮应力和轴挠度的非线性约束，且计算时间显著短于同类算法 。   

2.5 斑马优化算法 (Zebra Optimization Algorithm, ZOA)
代表性工作： Trojovská et al. (2022) 。 问题背景： 针对优化过程中“勘探”与“开发”平衡难的问题，ZOA模拟了斑马群体的社会结构及其应对捕食者的防御机制。 算法机理： ZOA主要模拟两种行为：觅食与防御。在觅食阶段，斑马群跟随领头斑马（当前最优解）移动，保持群体的凝聚力；在防御阶段，当感知到狮子等捕食者攻击时，斑马会采取“之”字形（Zigzag）奔跑或聚集成防御阵型。这种防御行为在算法中被建模为受控的随机扰动，允许算法在收敛过程中保持一定的种群多样性 。 结论与评价： ZOA在处理单峰函数时收敛速度极快，而在多峰函数中通过防御机制维持了多样性。在弹簧设计和焊接梁设计中，ZOA被证明是有效的优化器，其改进版本（如MIZOA）通过多策略融合进一步提升了在复杂环境下的路径规划能力 。   

3. 植物、物理与人类行为启发的算法创新
除了动物行为，2022–2025年的研究还广泛探索了植物生长规律、物理自然现象以及人类智能行为的数学映射。

3.1 雾凇优化算法 (Rime Optimization Algorithm, RIME)
代表性工作： Su et al. (2023) 。 问题背景： 传统的生物启发算法有时存在生物隐喻过于牵强、数学模型复杂的弊端。RIME算法回归物理本质，通过模拟雾凇这一自然气象的形成过程，提出了一种无参数（Parameter-free）或少参数的高效算法。 算法机理： RIME被明确归类为基于物理的算法（Physics-based）：   

软雾凇搜索（Soft-rime Search）： 模拟雾凇粒子在微风作用下的随机附着与生长。这一过程具有高度的随机性，允许搜索代理在整个解空间内进行大范围的飞行，主要负责全局探索。

硬雾凇穿刺（Hard-rime Puncture）： 模拟强风条件下，硬雾凇定向生长并相互交叉的现象。在算法中，这被建模为一种独特的交叉算子（Crossover operator），允许代理之间交换信息。这种“穿刺”机制能够有效地利用当前最优解的信息来引导其他个体。

正向贪婪选择（Positive Greedy Selection）： 算法在更新过程中始终保留适应度更好的状态，确保种群向更优方向进化 。   

结论与评价： RIME算法因其没有复杂的控制参数（如惯性权重、学习因子），在应用时极易调试。实验显示，RIME在特征选择、神经网络超参数优化等离散与连续混合问题上，表现出了比WOA和GWO更强的收敛能力和稳定性 。   

3.2 常春藤算法 (Ivy Algorithm, IVY)
代表性工作： Ghasemi et al. (2024) 。 问题背景： 植物在资源竞争中展现出的智能生长行为——如向光性、攀附性和空间占据能力，为优化算法提供了新的视角。 算法机理： IVY算法模拟了常春藤的生长周期。算法通过模拟植物茎的伸长（寻找新的支撑点）和叶片的展开（进行光合作用积累能量）来进行空间搜索。其核心创新在于引入了“生长速率”参数，该参数根据环境反馈（适应度值的变化）进行自适应调整。当环境适宜（解质量高）时，生长速率加快，进行局部密集搜索；反之则加快茎的伸长，探索新区域。后续的IVYPSO变体更是结合了粒子群的速度更新机制，进一步增强了算法的动态性能 。 结论与评价： IVY算法在拉伸/压缩弹簧设计问题中，成功找到了重量最小化的设计方案，且在多次运行中表现出极低的标准差，证明了其优越的鲁棒性 。   

3.3 树冠生长优化器 (Crown Growth Optimizer, CGO)
代表性工作： Liu et al. (2024) 。 问题背景： 树木在生长过程中，为了获得最佳的光照和空间，不仅会生长新枝，还会主动“修剪”那些效率低下的枝条。这种“生与灭”的动态平衡是CGO算法的灵感来源。 算法机理： CGO创新性地引入了“修剪机制”（Pruning mechanism）。算法模拟了树冠的三个过程：生长（Growing）、发芽（Sprouting）和修剪。生长和发芽负责在解空间中生成新的候选解，而修剪机制则受Ludvig定律和斐波那契数列启发，定期剔除种群中适应度较差的个体，并重新初始化这些资源。这种机制有效地防止了算法在劣质区域浪费计算资源，显著提高了收敛效率 。 结论与评价： 在光伏电池参数提取（PV Parameter Extraction）这一高度非线性问题中，CGO展现了极高的拟合精度，其RMSE指标优于SMA、HHO等主流算法，验证了修剪策略在复杂多峰景观中的有效性 。   

3.4 星鸦优化算法 (Nutcracker Optimization Algorithm, NOA)
代表性工作： Abdel-Basset et al. (2023) 。 问题背景： 许多元启发式算法缺乏“记忆”机制，无法有效利用历史搜索信息。星鸦（Nutcracker）这种鸟类具有惊人的空间记忆力，能记住数千个食物储藏点，为引入记忆机制提供了生物学蓝本。 算法机理： NOA算法模拟了星鸦的两种核心策略：   

觅食与储存（Foraging & Storage）： 模拟星鸦在夏季和秋季收集种子并分散埋藏的行为。这对应于算法的全局探索阶段，通过随机游走探索解空间。

缓存搜索与恢复（Cache-search & Recovery）： 模拟星鸦在冬季依靠记忆找回埋藏种子的行为。算法通过引入“参考记忆”（Reference Memory）矩阵，存储历史上访问过的优质区域信息，引导当前的搜索过程。这是一种典型的基于记忆的局部开发策略 。   

结论与评价： NOA在IEEE CEC 2014/2017/2020基准测试集上均取得了优异成绩。特别是在光伏参数辨识任务中，NOA凭借其记忆恢复机制，能够精准定位全局最优参数，均方根误差极低，显著优于传统无记忆算法 。   

4. 2022–2025年实验评价总结与工程应用实效
为了客观评估上述算法的实际效能，本章综合了多篇文献中的实验数据，选取了经典的结构工程设计问题（焊接梁、压力容器）以及能源领域的关键问题（光伏参数辨识、绿色云调度）进行横向对比。

4.1 经典结构工程设计问题实测
结构优化问题通常要求在满足应力、挠度、屈曲等多重非线性约束的前提下，最小化结构的重量或造成成本。

4.1.1 焊接梁设计问题 (Welded Beam Design)
问题描述： 目标是最小化焊接梁的制造成本，涉及焊缝厚度(h)、连接梁长度(l)、梁高(t)和梁宽(b)四个变量，需满足剪切应力、弯曲应力等7个约束。 实验数据综合对比：

算法名称	提出年份	最优成本 (Best Cost)	表现评价	数据来源
MDBO (改进蜣螂)	2023	1.6927	表现最优，收敛速度最快，约束处理能力强	
GTO (巨鲹)	2023	1.6952	极具竞争力，优于经典PSO和GSA	
IVY (常春藤)	2024	1.6954	表现稳定，标准差极小	
Traditional PSO	-	1.7248	陷入局部最优，成本较高	
  
共性分析： 新一代算法（如MDBO, GTO）普遍能够突破1.70的成本瓶颈，说明其在处理边界约束（Boundary Constraints）时具有更精细的搜索机制。

4.1.2 压力容器设计问题 (Pressure Vessel Design)
问题描述： 最小化圆柱形压力容器的总成本（材料、成型、焊接），包含4个混合变量（整数与连续变量）和4个约束。 实验数据综合对比：

算法名称	最优成本 (Best Cost)	相对SO提升幅度	备注	数据来源
ISO (改进蛇优化)	5834.67 (approx)	+7.8%	相比原始SO算法，成本显著降低，可行性更高	
ZOA (斑马)	5882.90	-	在统计测试中排名靠前，优于GWO	
原始 SO	5908.30	Baseline	表现优良，但略逊于改进版	
  
共性分析： 针对混合变量问题，SO和ZOA等算法通过特定的离散化处理机制或混合策略，展示了比传统算法更好的适应性。

4.2 能源与可持续计算领域的应用
4.2.1 光伏模型参数辨识 (PV Parameter Estimation)
问题挑战： 单二极管（SDM）和双二极管（DDM）模型参数提取是一个典型的多模态、高非线性问题，极易陷入局部最优。 实测表现：

星鸦优化算法 (NOA)： 在SDM模型参数提取中，NOA实现了均方根误差（RMSE）低至 7.92×10 
−5
  的惊人精度，在所有对比算法中排名第一。在更复杂的DDM模型中，其RMSE更是低至 6.02×10 
−5
  。   

树冠生长优化器 (CGO)： 同样展现了极高的拟合优度，证明了基于生长的搜索策略在连续空间优化中的有效性 。   

4.2.2 绿色云计算任务调度 (Green Cloud Task Scheduling)
问题挑战： 在数据中心中，既要最小化任务完成时间（Makespan），又要最小化能源消耗（Energy Consumption），这是一个多目标优化问题。 实测表现：

混合策略应用： 2024年的研究表明，结合了Levy飞行和反向学习的改进型蜣螂算法（Modified DBO）及黑寡妇算法（BWO），在云任务调度中能够实现负载均衡与能耗的帕累托最优（Pareto Optimality）。相比传统的轮询调度（Round Robin）或简单的PSO，新算法在能耗上降低了约 15%-20%，同时显著缩短了任务等待时间 。   

5. 挑战、前沿技术融合与2025年趋势预测
尽管生物启发式算法在过去三年取得了长足进步，但随着问题规模的指数级增长，单一算法的局限性也日益凸显。基于2024-2025年的最新文献，本报告总结了当前面临的挑战并预测了三大发展趋势。

5.1 当前面临的主要挑战
理论基础薄弱： 许多新算法（如部分以动物命名的算法）虽然在实验中表现良好，但缺乏严谨的数学收敛性证明。其有效性往往依赖于复杂的参数调节，甚至存在“隐喻过度”（Metaphor-rich, Theory-poor）的批评。

高维灾难： 尽管在低维工程问题（<50维）表现出色，但在处理深度神经网络超参数优化（>1000维）或大规模物流调度时，许多元启发式算法仍面临“维数灾难”，搜索效率急剧下降。

计算昂贵： 许多现实工程问题（如汽车碰撞仿真）的单次适应度评估需要数小时。元启发式算法通常需要数万次评估，这在计算时间上是不可接受的。

5.2 趋势一：大语言模型（LLM）驱动的自动化算法设计 (LLM-Driven Algorithm Design)
预测： 到2025年，算法设计模式将发生根本性变革，从“人工设计”转向“AI生成”。 依据： 2024年的先锋工作（如LLaMEA, OPRO）已经展示了利用大语言模型（如GPT-4）作为“算法进化器”的潜力。研究者不再直接编写算法代码，而是通过设计提示词（Prompts）引导LLM理解优化任务，并让LLM自动生成、修改和迭代优化算法的代码。初步结果显示，LLM生成的算法在某些组合优化问题上已超越了人类专家的设计 。 展望： 未来的元启发式算法可能不再有固定的名字（如“猫算法”、“狗算法”），而是针对特定问题由LLM实时生成的“即时算法”（Ad-hoc Algorithms）。   

5.3 趋势二：代理模型辅助的昂贵优化 (Surrogate-assisted Optimization)
预测： 针对计算昂贵的工程问题，代理模型（Surrogate Model）将成为标准配置。 依据： 为了解决CFD仿真或有限元分析耗时过长的问题，研究者开始深度集成机器学习模型（如Kriging, 径向基函数RBF, 高斯过程）。2024-2025年的研究重点在于“模型管理”（Model Management），即智能地决定何时使用廉价的代理模型进行预筛选，何时调用昂贵的真实仿真进行验证。这种混合策略在汽车耐撞性设计和航空气动优化中已初现锋芒 。 展望： “数据驱动的进化计算”将成为解决复杂黑盒问题的主流方法。   

5.4 趋势三：绿色计算与可持续性导向 (Sustainability-Oriented Optimization)
预测： “绿色性”将成为衡量算法性能的核心指标之一。 依据： 随着碳中和目标的推进，算法不仅被用于解决绿色问题（如微网调度、低碳物流），其自身的能效也受到关注。2025年的研究将倾向于开发轻量级、低功耗的元启发式算法，以适应边缘计算（Edge Computing）和物联网（IoT）设备的资源受限环境。同时，针对绿色制造车间调度（Green Shop Scheduling）的专用算法将持续涌现，旨在同时优化生产效率与碳排放 。   

6. 结论
2022至2025年，生物启发式元启发式算法领域经历了从“数量爆发”到“质量深化”的转型。以蜣螂优化算法（DBO）、蛇优化算法（SO）和雾凇优化算法（RIME）为代表的新兴算法，通过引入更复杂的生物社会行为模拟和物理机制，在解决高维、多约束、非线性的工程优化问题上取得了显著突破。实验证据确凿地表明，这些新算法在焊接梁设计、压力容器优化及光伏参数辨识等实际应用中，相比传统算法具有更快的收敛速度和更低的工程成本。

展望未来，该领域正站在技术融合的十字路口。大语言模型的介入正在打破算法设计的传统边界，代理模型技术为解决昂贵问题架起了桥梁，而可持续发展的需求则为算法应用指明了新的方向。对于科研人员与工程实践者而言，紧跟“AI生成算法”与“代理辅助优化”的趋势，将是在下一代智能工程设计中保持竞争力的关键。

参考文献
   

Xue, J., & Shen, B. (2023). Dung beetle optimizer: a new meta-heuristic algorithm for global optimization. The Journal of Supercomputing, 79, 7305–7336.

   

Hashim, F. A., & Hussien, A. G. (2022). Snake Optimizer: A novel meta-heuristic optimization algorithm. Knowledge-Based Systems, 242, 108320.

   

Sadeeq, H. T., & Abdulazeez, A. M. (2022). Giant Trevally Optimizer (GTO): A Novel Metaheuristic Algorithm for Global Optimization and Challenging Engineering Problems. IEEE Access, 10, 121615-121640.

   

Su, H., et al. (2023). RIME: A physics-based optimization. Neurocomputing, 532, 183-214.

   

Dehghani, M., et al. (2023). Coati Optimization Algorithm: A new bio-inspired metaheuristic algorithm for solving optimization problems. Knowledge-Based Systems, 259, 110011.

   

Trojovská, E., et al. (2022). Zebra Optimization Algorithm: A New Bio-Inspired Optimization Algorithm for Solving Optimization Algorithm. IEEE Access, 10, 49445-49473.

   

Liu, C., Zhang, D., & Li, W. (2024). Crown Growth Optimizer: An Efficient Bionic Meta-Heuristic Optimizer and Engineering Applications. Mathematics, 12(15), 2343.

   

Ghasemi, M., et al. (2024). Optimization based on the smart behavior of plants with its engineering applications: Ivy Algorithm. Knowledge-Based Systems, 285, 111850.

   

Abdel-Basset, M., et al. (2023). Nutcracker optimizer: A novel nature-inspired metaheuristic algorithm for global optimization and engineering design problems. Knowledge-Based Systems, 262, 110248.

   

Hamadneh, T., et al. (2024). Fossa Optimization Algorithm: A New Bio-Inspired Metaheuristic Algorithm for Engineering Applications. International Journal of Intelligent Engineering and Systems, 17(5), 1038-1047.

   

Zhao, H., et al. (2024). Large Language Models as Evolutionary Optimizers. 2024 IEEE Congress on Evolutionary Computation (CEC).

   

Wang, Z., et al. (2025). Surrogate-assisted evolutionary algorithms for high-dimensional expensive optimization. Algorithms, 18(1), 4.

   

Zhang, Y., et al. (2023). An improved dung beetle optimizer for engineering design problems. Journal of Computational Design and Engineering.

   

Sefati, S., & Halunga, S. (2024). Energy-Efficient Task Scheduling Using a Novel Metaheuristics Approach in Cloud Data Centers. Applied Sciences.

   

Wang, L., et al. (2023). Parameter Extraction of Solar Photovoltaic Model Based on Nutcracker Optimization Algorithm. Applied Sciences.


mdpi.com
Metaheuristic Algorithms for Optimization: A Brief Review - MDPI
在新窗口中打开

inass.org
Fossa Optimization Algorithm: A New Bio-Inspired Metaheuristic Algorithm for Engineering Applications - INASS
在新窗口中打开

pmc.ncbi.nlm.nih.gov
A Comprehensive Review of Bio-Inspired Optimization Algorithms Including Applications in Microelectronics and Nanophotonics - PubMed Central
在新窗口中打开

mdpi.com
A Systematic Review of Bio-Inspired Metaheuristic Optimization Algorithms: The Untapped Potential of Plant-Based Approaches - MDPI
在新窗口中打开

pmc.ncbi.nlm.nih.gov
An Enhanced Randomized Dung Beetle Optimizer for Global Optimization Problems - NIH
在新窗口中打开

researchgate.net
(PDF) Dung beetle optimizer: a new meta-heuristic algorithm for global optimization
在新窗口中打开

mdpi.com
An Improved Dung Beetle Optimization Algorithm for High-Dimension Optimization and Its Engineering Applications - MDPI
在新窗口中打开

tandfonline.com
Full article: A conceptual cost estimation model for building construction projects by hybrid Back-Propagation Neural Network and Dung Beetle Optimizer algorithm - Taylor & Francis Online
在新窗口中打开

aimspress.com
An improved dung beetle optimizer algorithm for solving engineering optimization problems
在新窗口中打开

diva-portal.org
Snake Optimizer: A novel meta-heuristic optimization algorithm - DiVA portal
在新窗口中打开

mdpi.com
Improved Snake Optimizer Using Sobol Sequential Nonlinear Factors and Different Learning Strategies and Its Applications - MDPI
在新窗口中打开

pmc.ncbi.nlm.nih.gov
Improved Snake Optimization Algorithm for Global Optimization and Engineering Applications - PMC - PubMed Central
在新窗口中打开

preprints.org
Fusion of RIME Algorithm Improved Snake Optimization Algorithm and Its Applications in UAV Path Planning and Engineering Problems - Preprints.org
在新窗口中打开

semanticscholar.org
Giant Trevally Optimizer (GTO): A Novel Metaheuristic Algorithm for Global Optimization and Challenging Engineering Problems - Semantic Scholar
在新窗口中打开

researchgate.net
(PDF) Giant Trevally Optimizer (GTO): A Novel Metaheuristic Algorithm for Global Optimization and Challenging Engineering Problems - ResearchGate
在新窗口中打开

mdpi.com
Giant Trevally Optimization Approach for Probabilistic Optimal Power Flow of Power Systems Including Renewable Energy Systems Uncertainty - MDPI
在新窗口中打开

jac.ut.ac.ir
A new meta-heuristic algorithm of giant trevally for solving engineering problems
在新窗口中打开

mdpi.com
Mechanical and Civil Engineering Optimization with a Very Simple Hybrid Grey Wolf—JAYA Metaheuristic Optimizer - MDPI
在新窗口中打开

academic.oup.com
Improve coati optimization algorithm for solving constrained engineering optimization problems - Oxford Academic
在新窗口中打开

pubmed.ncbi.nlm.nih.gov
An improved Coati Optimization Algorithm with multiple strategies for engineering design optimization problems - PubMed
在新窗口中打开

researchgate.net
(PDF) An improved Coati Optimization Algorithm with multiple strategies for engineering design optimization problems - ResearchGate
在新窗口中打开

researchgate.net
(PDF) Zebra Optimization Algorithm: A New Bio-Inspired Optimization Algorithm for Solving Optimization Algorithm - ResearchGate
在新窗口中打开

journals.plos.org
Zebra optimization algorithm incorporating opposition-based learning and dynamic elite-pooling strategies and its applications | PLOS One
在新窗口中打开

pmc.ncbi.nlm.nih.gov
A Multi-Strategy Improved Zebra Optimization Algorithm for AGV Path Planning - PMC
在新窗口中打开

mdpi.com
A Multi-Strategy Improved Zebra Optimization Algorithm for AGV Path Planning - MDPI
在新窗口中打开

aliasgharheidari.com
RIME:A physics-based optimization - Ali Asghar Heidari
在新窗口中打开

researchgate.net
(PDF) RIME: A physics-based optimization - ResearchGate
在新窗口中打开

mdpi.com
A Hybrid SAO and RIME Optimizer for Global Optimization and Cloud Task Scheduling
在新窗口中打开

researchgate.net
Optimization based on the smart behavior of plants with its engineering applications: Ivy Algorithm | Request PDF - ResearchGate
在新窗口中打开

pmc.ncbi.nlm.nih.gov
A Particle Swarm Optimization-Guided Ivy Algorithm for Global Optimization Problems - PMC
在新窗口中打开

pmc.ncbi.nlm.nih.gov
ACIVY: An Enhanced IVY Optimization Algorithm with Adaptive Cross Strategies for Complex Engineering Design and UAV Navigation - PMC
在新窗口中打开

mdpi.com
Crown Growth Optimizer: An Efficient Bionic Meta-Heuristic Optimizer and Engineering Applications - MDPI
在新窗口中打开

researchgate.net
(PDF) Crown Growth Optimizer: An Efficient Bionic Meta-Heuristic Optimizer and Engineering Applications - ResearchGate
在新窗口中打开

researchgate.net
Nature-Inspired Adaptive Differential Evolution: A Unified Meta-Heuristic Framework for Complex Engineering Optimisation and UAV Path Planning | Request PDF - ResearchGate
在新窗口中打开

researchgate.net
Nutcracker optimizer: A novel nature-inspired metaheuristic algorithm for global optimization and engineering design problems - ResearchGate
在新窗口中打开

orca.cardiff.ac.uk
A novel nature-inspired nutcracker optimizer algorithm for congestion control in power system transmission lines - -ORCA - Cardiff University
在新窗口中打开

scispace.com
(PDF) Parameter Extraction of Solar Photovoltaic Model Based on Nutcracker Optimization Algorithm (2023) | Zhenjiang Duan | 13 Citations - SciSpace
在新窗口中打开

mdpi.com
Parameter Extraction of Solar Photovoltaic Model Based on Nutcracker Optimization Algorithm - MDPI
在新窗口中打开

pmc.ncbi.nlm.nih.gov
Multi-Strategy Improved Dung Beetle Optimization Algorithm and Its Applications - PMC
在新窗口中打开

pmc.ncbi.nlm.nih.gov
A Hybrid Nonlinear Whale Optimization Algorithm with Sine Cosine for Global Optimization - PMC - NIH
在新窗口中打开

pubmed.ncbi.nlm.nih.gov
Improved Snake Optimization Algorithm for Global Optimization and Engineering Applications - PubMed
在新窗口中打开

pmc.ncbi.nlm.nih.gov
A New Swarm-Inspired Metaheuristic Algorithm for Solving Optimization Problems - NIH
在新窗口中打开

academic.oup.com
A new approach for solving global optimization and engineering problems based on modified sea horse optimizer - Oxford Academic
在新窗口中打开

mdpi.com
Towards Sustainable Cloud Computing: Load Balancing with Nature-Inspired Meta-Heuristic Algorithms - MDPI
在新窗口中打开

researchgate.net
Energy-Efficient Task Scheduling Using a Novel Metaheuristics Approach in Cloud Data Centers - ResearchGate
在新窗口中打开

researchgate.net
Swarm Intelligence-Based Task Scheduling for Enhancing Security for IoT Devices | Request PDF - ResearchGate
在新窗口中打开

ieeexplore.ieee.org
Large Language Models as Evolutionary Optimizers - IEEE Xplore
在新窗口中打开

arxiv.org
A Systematic Survey on Large Language Models for Evolutionary Optimization: From Modeling to Solving - arXiv
在新窗口中打开

arxiv.org
LLaMEA: A Large Language Model Evolutionary Algorithm for Automatically Generating Metaheuristics - arXiv
在新窗口中打开

academic.oup.com
Automated surrogate-assisted particle swarm optimizer with an adaptive parental guidance strategy for expensive engineering optimization problems - Oxford Academic
在新窗口中打开

mdpi.com
A Multi-Surrogate Assisted Multi-Tasking Optimization Algorithm for High-Dimensional Expensive Problems - MDPI
在新窗口中打开

researchgate.net
A Surrogate-assisted Multi-objective Grey Wolf Optimizer for Empty-heavy Train Allocation Considering Coordinated Line Utilization Balance | Request PDF - ResearchGate
在新窗口中打开

researchgate.net
(PDF) Metaheuristics in Sustainable and Green Optimization - ResearchGate
在新窗口中打开

researchgate.net
Analysis of Meta-Heuristic Optimization for Sustainable Green Manufacturing