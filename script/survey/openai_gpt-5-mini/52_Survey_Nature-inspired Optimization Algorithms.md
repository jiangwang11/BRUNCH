引言  
自然启发式优化（nature-inspired optimization）在连续/组合/约束工程问题中仍是活跃研究方向。近三年（2022–2025）研究呈现两个明显动向：一是大量基于“策略融合/混合”的工程化改造（把两个以上启发式或学习组件耦合以改善勘探/开发平衡）；二是将自适应参数控制或学习（含强化学习或基于景观的自适应）嵌入传统群体算法以提高稳定性与可扩展性。本综述聚焦 2022–2025 年代表性工作，按方法类别挑选关键论文（每类 ≤5 篇），逐篇说明研究问题、核心方法与关键实验结论，并在实验与评价、趋势与挑战处给出横向总结与判断。所有引用为公开可查的实刊/会议或机构页面（见参考文献）。

方法分类与代表作  
（注：每篇 4–6 句，着重问题、方法、要点实验结论）

A. 基于粒子群/学习驱动的 PSO 变体（结合 RL 或自适应策略）  
1) Reinforcement-learning-based PSO with neighborhood differential mutation (NRLPSO), Li et al., Swarm & Evolutionary Computation 2023.  
- 研究问题：PSO 在复杂景观上算子选择固定导致智能水平受限、易早熟。  
- 核心方法：提出基于强化学习的速度向量生成（VRL）策略与动态振荡惯性权重（DOW），并在局部用邻域差分突变（NDM）提升多样性；粒子根据状态（探索/利用/收敛/跳出）用 RL 选择速度更新范式。  
- 关键实验结论：在 CEC2017/CEC2022 基准上与多种先进 PSO 变体比较，NRLPSO 在收敛速度与最终精度上具有统计学显著优势（多函数上 Wilcoxon 检验显著）。  
[cilab.jxust.edu.cn](https://cilab.jxust.edu.cn/info/1062/1985.htm)

2) Elite-guidance social learning PSO (ESLPSO), Qi et al., Journal of Northwestern Polytechnical University 2024.  
- 研究问题：标准 PSO 对种群信息利用不足且易早熟。  
- 核心方法：提出分层拓扑（精英/平民）、精英引导的社会学习机制与极值扰动迁移，加上 cubic 混沌初始化以提高初始覆盖。  
- 关键实验结论：在 12 个单峰/多峰/旋转基准上，ESLPSO 在大多数函数上显著提升收敛精度与稳定性（平均与最优指标改进），并通过收敛曲线与多样性曲线说明跳出局部最优的机制效用。  
[jnwpu.org](https://www.jnwpu.org/articles/jnwpu/pdf/2024/05/jnwpu2024425p948.pdf)

3) Population-center-guided PSO (PSOSI / PSOLP), Zhou 2025.  
- 研究问题：提升 PSO 全局寻优能力并避免过度同化导致的早熟。  
- 核心方法：把“种群中心位置”作为额外引导项（PSOSI），并提出基于聚集度触发的局部扰动机制（PSOLP）；两者可并行使用以平衡多样性与收敛。  
- 关键实验结论：在 CEC-2022 与 8 个工程优化问题上，PSOSI/PSOLP 在平均排名与 Wilcoxon 检验中优于标准 PSO 和若干现代算法，表明种群级信息能显著改善多种实际问题的收敛稳定性。  
[pdf.hanspub.org](https://pdf.hanspub.org/csa_1543619.pdf)

B. 黏菌算法（SMA）与混合变体（振荡/收缩模型与遗传/扩散混合）  
1) SMAGA: Hybrid Slime Mould–Genetic Algorithm with spatial-attenuation self-diffusion (PAN et al., Peking Univ. Acta/2025).  
- 研究问题：SMA 勘探/开发失衡、随机重分配导致解信息浪费。  
- 核心方法：以 GA 框架引入振荡-收缩式交叉（具正负反馈与随机游走）和基于空间衰减的高斯自扩散变异，并用适应度分布偏差自适应调整交叉/变异概率。  
- 关键实验结论：在 IEEE CEC2017/CEC2021 基准上系统对比 23 种算法，SMAGA 在单峰、多峰与若干混合函数上表现尤其明显；并应用于三二极管光伏模型参数辨识以验证在实际问题上的适用性。  
[xbna.pku.edu.cn](https://xbna.pku.edu.cn/fileup/0479-8023/HTML/2025-1-14.html)

2) Chaos/Opposition and other SMA variants (代表性引用：Rizk‑Allah et al., COSMA, ISA Transactions 2022；以及若干 SMA 变体综述/改进工作).  
- 研究问题：引入混沌/反向学习等策略以提高多样性与跳出局部极值能力。  
- 核心方法：在 SMA 中嵌入混沌映射、反向学习或局部搜索（单纯形/Nelder‑Mead），常以混合/并行架构提升鲁棒性。  
- 关键实验结论：这些策略在若干工程/图像分割或光伏参数辨识任务上能显著降低收敛方差并提升查全/查准，是 SMA 系列实用化的常见路径（参见文献综述）。  
（COSMA 引文示例见 SMAGA 文献参考部分）

C. 蜣螂优化（Dung Beetle Optimization, DBO）与多策略融合  
1) Multi-strategy Dung Beetle Optimization (MSDBO), Wang & Gu, CSA 2023/2024.  
- 研究问题：标准 DBO 在全局探索与收敛精度上的不足。  
- 核心方法：引入社会学习策略引导推球行为、方向跟随交互以增强个体间信息流，以及基于环境感知的概率选择以兼顾性能与时间成本。  
- 关键实验结论：在 12 个基准函数及受约束工程问题（如压力容器设计）上，MSDBO 在寻找更低目标值与降低方差方面显示统计学优势。  
[c-s-a.org.cn](https://www.c-s-a.org.cn/1003-3254/9397.html)

2) 工业机器人运动学参数辨识的多策略融合 DBO (许佳璐 et al., 中国机械工程 2025).  
- 研究问题：将 DBO 用于工业机器人运动学参数辨识时的收敛精度与局部最优问题。  
- 核心方法：在 DBO 中引入分段混沌映射与精英反向学习做初始化，并结合鱼鹰探索行为与随机扰动机制改善全局搜索与局部开发的平衡（作者称 MSFDBO）。  
- 关键实验结论：在 T6A‑19 型机器人实测辨识任务上，位置相关误差、RMSE 等指标显著下降（论文给出具体百分比改善），验证了算法在工程辨识场景中的有效性。  
[cjournal.hep.com.cn](https://cjournal.hep.com.cn/1004-132X/CN/1160171567385862339)

D. 人工蜂鸟 / 蜂群 /蝴蝶等较新生物启发算法的改进与邻域搜索策略  
1) ALAHA: Artificial Hummingbird Algorithm with adaptive neighborhood search & improved Lévy factors (He & Li, Modeling & Simulation 2024).  
- 研究问题：原 AHA（人工蜂鸟）在步长控制与局部精度间存在折衷，易陷入局部极小。  
- 核心方法：在引导/领地觅食中以改进 Lévy 飞行作为步长自适应因子，并按适应度方差触发邻域自适应围猎以精化局部搜索，此外引入非线性收敛因子控制 Lévy 振幅。  
- 关键实验结论：在 23 个基准函数与多种比较算法上，ALAHA 在收敛速度、跳出局部最优与稳健性方面表现优越（Wilcoxon 检验支持），但作者也指出参数 a（方差阈值）对不同函数类型敏感。  
[hanspub.org / image.hanspub.org](https://image.hanspub.org/Html/1-2571228_81778.htm)

2) NEI‑ABC: Neuro‑endocrine‑immune inspired ABC (NEI‑ABC), Liu et al., 2023 (期刊/会议收录).  
- 研究问题：传统 ABC 在复杂非线性工程问题上收敛慢与早熟。  
- 核心方法：受 NEI 生物调节启发加入“蓝光引导/蜜源调控/触角定向”单元，改进侦查/跟随/引领蜂的协同搜索行为。  
- 关键实验结论：在油田注采优化等实际工程案例中，NEI‑ABC 提高了解的质量与搜索鲁棒性，且在受约束工程目标上有更稳定的可行解生成能力。  
[xk.sia.cn](https://xk.sia.cn/cn/article/doi/10.13976/j.cnki.xk.2023.2056)

E. 其它专用/应用导向的改进：海马、蝴蝶、变异策略等  
1) Improved Seahorse Optimization (SHO) for Random Forest hyper‑tuning, Fu et al., 吉林大学学报 2025.  
- 研究问题：海马优化（SHO）初始化质量差导致在模型超参调优上不稳定。  
- 核心方法：用 Logistic 混沌映射改进 SHO 的初始化并与随机森林联合，用混沌增强初解分布。  
- 关键实验结论：在若干数据集的 RF 参数优化上，改进 SHO‑RF 提升了准确率/召回/F1（论文给出具体数值，例如准确率 96.15%），表明混沌初始化对学习模型超参搜索有实用价值。  
[cjournal.hep.com.cn](https://cjournal.hep.com.cn/1671-5489/CN/10.13413/j.cnki.jdxblxb.2024003)

2) Adaptive butterfly optimization with mutation strategies, Liu & Dai, Application Research of Computers 2022.  
- 研究问题：基础蝴蝶优化算法收敛慢且稳定性不足。  
- 核心方法：引入自适应转换概率、惯性权重与局部变异来维持勘探/开发平衡并增加多样性；变异与混沌记忆权重并用以避免早熟。  
- 关键实验结论：在 12 个基准函数上，改进蝶算在收敛速度、最优值与标准差上普遍优于原始 BOA 和数种基线算法，支持用自适应变异提升鲁棒性的观点。  
[arocmag.cn](https://www.arocmag.cn/abs/2021.06.0244)

实验与评价总结（共性结论，非逐篇重复）  
- 基准与统计：多数论文采用 CEC 系列（如 CEC2017/CEC2021/CEC2022）或标准单/多峰集合作为测试套件，且普遍应用非参数统计检验（Wilcoxon、Friedman 等）来验证显著性，这是当前领域的最低可接受验证门槛。  
- 混合/自适应为主流：2022–2025 年的改进多倾向于“策略融合”（混合局部搜索、混沌/反向学习、RL 驱动算子选择或基于种群统计的自适应参数），这些方法在多数基准上能同时降低均值与方差，但对复合/高维复合（composition）函数仍存在弱点。  
- 局部搜索与步长控制的权衡：邻域搜索或自适应围猎能显著提升精度，但需用显式阈值或衰减因子（如基于适应度方差或非线性收敛因子）控制触发频率，否则会牺牲全局探索能力。  
- 可重复性与工程验证：若干工作把算法直接应用到工程辨识（机器人/光伏/油田等），显示实用性；同时也暴露出参数敏感性与算法复杂度在真实问题上的实现成本问题。  
- 理论分析不足：尽管很多工作在实验上显示改进，但系统性的收敛性证明、复杂度上界与景观依赖性分析仍较少，造成跨问题泛化预测能力有限。

趋势与挑战（2025 年前后的预测，≥3 点）  
1) 学习‑增强算子选择将成为常态化设计：强化学习 / bandit /在线元学习被进一步嵌入群体算法，用于动态选择速度/变异/交叉算子；未来两年将出现更多“轻量级 RL + 演化算子”的实际模板，关注点从“能否提高精度”转向“样本效率与鲁棒性”（即少次试验下稳定改进）。  
2) 混合框架向可解释/可证性转变：单纯的策略堆叠已显边际收益递减，社区将更关注能提供部分理论保证或可诊断行为的混合结构（例如把景观特征映射到参数策略，或用 Lyapunov‑style 论证某些收敛行为）。  
3) 标准化大规模基准与可复现实验实践将加速：除 CEC 系列外，需增加带约束、多目标与真实工程数据的统一测试集合；期望在 2 年内出现更严格的可复现性要求（包括公开代码、随机种子与计算预算详细记录）。  
4) 面向高维与稀评估问题的代理/分层方法增多：为应对高维（>1000D）或代价昂贵的真值函数，代理模型（Gaussian process / ensemble surrogate）与分层群体（co‑evolution/cooperative co‑evolution）将更紧密地与自然启发式算法耦合。  
5) 领域特定工程化与资源意识：从学术基准向工业部署转变时，算法需在计算资源、参数调优成本与实时性之间取得新平衡，出现更多轻量级变体与低精度优先策略（approximate search）以满足工程约束。

结论  
近三年（2022–2025）自然启发优化研究以“策略融合”与“自适应/学习嵌入”为主流方向，若干代表工作在基准与工程任务上取得了统计学上的改进。未来研究需把重点从单一性能提升转向可解释性、可复现性与样本/计算效率，并加强理论与工程之间的桥接，以便把实验室中的算法可靠地移植至复杂、受限的实际问题场景。

参考文献（按文中出现顺序，均为可检索来源；链接以域名标注）  
1. Li S., Chen H., Wang M., Heidari A. A., Mirjalili S. Slime mould algorithm: a new method for stochastic optimization. Future Generation Computer Systems, 2020. —（基础参考）[futuregenerationcomputersystems.org](https://www.sciencedirect.com/journal/future-generation-computer-systems)  
2. PAN Jiawen, ZHAI Weixin, et al. A Hybrid Slime Mould Genetic Algorithm Based on Spatial Attenuation Self-diffusion Mechanism (SMAGA). Acta Scientiarum Naturalium Universitatis Pekinensis (北京大学学报(自然科学版)), 2025. [xbna.pku.edu.cn](https://xbna.pku.edu.cn/fileup/0479-8023/HTML/2025-1-14.html)  
3. Rizk‑Allah R. M., Hassanien A. E., Song D. Chaos‑opposition‑enhanced slime mould algorithm (COSMA). ISA Transactions, 2022. — (代表 SMA 改进方向，详见 SMAGA 引用) [doi via SMAGA refs]  
4. Liwei et al. (NRLPSO) Reinforcement learning-based particle swarm optimization with neighborhood differential mutation strategy. Swarm and Evolutionary Computation, 2023. [cilab.jxust.edu.cn](https://cilab.jxust.edu.cn/info/1062/1985.htm) — DOI:10.1016/j.swevo.2023.101274  
5. Qi Cheng, XIE Junwei, WANG Xue, et al. A novel elite guidance-based social learning particle swarm optimization algorithm (ESLPSO). Journal of Northwestern Polytechnical University, 2024. [jnwpu.org](https://www.jnwpu.org/articles/jnwpu/pdf/2024/05/jnwpu2024425p948.pdf)  
6. Zhou Liuchang. Population-Center-Guided Particle Swarm Optimization Algorithm (PSOSI / PSOLP). Computer Science and Application, 2025. [pdf.hanspub.org](https://pdf.hanspub.org/csa_1543619.pdf)  
7. Wang Leyao, Gu Lei. Improved Dung Beetle Optimization Algorithm with Multi‑strategy (MSDBO). Computer Systems & Applications (计算机系统应用), 2024. [c-s-a.org.cn](https://www.c-s-a.org.cn/1003-3254/9397.html)  
8. 许佳璐, 刘笑楠, 李朋超, 刘振宇. 基于多策略融合蜣螂优化算法的工业机器人运动学参数辨识方法. 中国机械工程, 2025. [cjournal.hep.com.cn](https://cjournal.hep.com.cn/1004-132X/CN/1160171567385862339)  
9. He Yongkang, Li Xufang. Neighborhood Search and Artificial Hummingbird Optimization Algorithms with Improved Lévy Factors (ALAHA). Modeling and Simulation, 2024. [image.hanspub.org](https://image.hanspub.org/Html/1-2571228_81778.htm)  
10. Fu Haitao, Zhang Zhiyong, Wang Zenghui, Jin Chenlei. Improved SHO algorithm for optimizing Random Forest model hyperparameters. Journal of Jilin University (Science Edition), 2025. [cjournal.hep.com.cn](https://cjournal.hep.com.cn/1671-5489/CN/10.13413/j.cnki.jdxblxb.2024003)  
11. Liu Bao, Zhang Yue, Yang Jinying. Improved Intelligent Artificial Bee Colony Algorithm and Its Application to Optimization of Injection and Production in Oilfield (NEI‑ABC). 2023. [xk.sia.cn](https://xk.sia.cn/cn/article/doi/10.13976/j.cnki.xk.2023.2056)  
12. Liu Kai, Dai Yongqiang. Adaptive butterfly optimization algorithm based on mutation strategies. Application Research of Computers, 2022. [arocmag.cn](https://www.arocmag.cn/abs/2021.06.0244)  
13. Heidari A. A., Mirjalili S., Faris H., et al. Harris Hawks Optimization: Algorithm and Applications. Future Generation Computer Systems, 2019. —（参照现代群体算法评测与对照）[futuregenerationcomputersystems.org](https://www.sciencedirect.com/journal/future-generation-computer-systems)  
14. Rizk‑Allah R. M., Hassanien A. E., Song D. Chaos‑opposition‑enhanced slime mould algorithm for wind turbine cost minimization. ISA Transactions, 2022. —（示例：SMA 在工程问题的应用）[sciencedirect.com](https://www.sciencedirect.com)  

（注）文内多篇论文的具体实验细节、统计检验结果、参数设置与数值表格请参见对应原文；本文旨在横向整合 2022–2025 年代表性改进方向与共性结论，以便快速判断未来研究的可行路径与短板。若需我导出某一篇论文的关键表格/收敛曲线或把某类算法的代码实现要点整理成 checklist，我可以基于原文逐篇提取并生成。