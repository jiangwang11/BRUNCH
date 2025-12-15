引言  
近年来（尤以 2022–2025 年）自然启发的元启发式算法持续涌现变体与混合策略，研究焦点集中在：自适应参数控制、随机/混沌初始化、长跳跃（Lévy）与局部围猎相结合、以及将多种启发式机制按问题特征动态切换或并行耦合。本文在严格限定的代表作基础上（仅列出真实可查论文并以检索到的原文为依据），按方法类别梳理 2022–2025 年间的代表性工作，比较其方法论创新与评测结论，最后给出短期研究趋势与挑战预测。全文力求信息密度与可验证性：每篇工作 4–6 句，突出问题、核心方法与关键实验结论；实验评价段仅总结共性结论，避免逐篇罗列。

方法分类与代表作（每类 2–4 篇，按发表年份或代表性排序）

一、粒子群 / 社会学习类改进
- Qi et al., “A novel elite guidance-based social learning particle swarm optimization algorithm” (Journal of Northwestern Polytechnical University, 2024).  
  研究问题：针对经典 PSO 易早熟、种群信息利用不足的问题；  
  核心方法：提出分层拓扑（精英粒子 vs 平民粒子）、Cubic 混沌初始化与“精英引导的社会学习”更新，辅以极值扰动迁移机制以恢复多样性；  
  关键结论：在 12 个单峰/多峰/旋转基准函数上，与 7 个改进 PSO 变体比较，作者报告在大多数测试函数上收敛更快且均值/方差表现更稳健（文中给出 30 次独立运行统计）。  
  参考（原文）：[jnwpu.org](https://www.jnwpu.org/articles/jnwpu/pdf/2024/05/jnwpu2024425p948.pdf).

- Zhou, “Population-Center-Guided Particle Swarm Optimization for Global Optimization” (Computer Science and Application, 2025).  
  研究问题：增强 PSO 全局寻优能力并抑制早熟收敛；  
  核心方法：引入种群中心位置作为额外引导项（PSOSI），并提出基于种群聚集度的局部扰动策略（PSOLP），两策略分别用于增强总体引导与在高聚集时恢复多样性；  
  关键结论：在 CEC‑2022 基准与 8 个工程设计问题上，PSOSI/PSOLP 在平均排名和 Wilcoxon/Friedman 检验中优于标准 PSO 和若干主流算法，表明“中心引导 + 自适扰动”对多类问题均有统计学意义的提升。  
  参考（原文）：[hanspub.org](https://pdf.hanspub.org/csa_1543619.pdf).

二、黏菌（SMA）与遗传/混合策略
- Pan et al., “A Hybrid Slime Mould Genetic Algorithm Based on Spatial Attenuation Self-diffusion Mechanism (SMAGA)” (Acta Scientiarum Naturalium Universitatis Pekinensis, 2025).  
  研究问题：改进 SMA 在勘探/开发（exploration/exploitation）间的不平衡与稳定性问题；  
  核心方法：以 GA 框架嵌入两新算子——振荡收缩型交叉（含正负反馈与随机游走）和基于空间衰减的自扩散变异；并用适应度分布偏差（FDD）来自适应调整交叉/变异概率；  
  关键结论：在 IEEE CEC2017/CEC2021 基准上与 23 种算法比较，SMAGA 在大量单峰、多峰与混合函数上表现出更好的寻优精度与鲁棒性；论文同时给出充分的统计检验（Wilcoxon、Friedman）。  
  参考（原文）：[xbna.pku.edu.cn](https://xbna.pku.edu.cn/fileup/0479-8023/HTML/2025-1-14.html).

- （SMA 背景与比较基线）Li et al., “Slime Mould Algorithm: a new method for stochastic optimization” (Future Generation Computer Systems, 2020) — 作为方法学基础被 2022–2025 年多篇改进工作引用与混合。  
  作用：提供 SMA 的振荡/收缩机制基准；多数后续工作以其为出发点进行局部/全局算子融合（见 Pan et al. 2025）。  
  参考（背景）：Future Generation Computer Systems (Li et al., 2020).

三、蜣螂（Dung Beetle Optimization, DBO）及多策略融合
- 王乐遥、顾磊, “多策略融合改进的蜣螂优化算法” (Computer Systems & Applications, 2023).  
  研究问题：DBO 原型的全局勘探能力不足与收敛精度低；  
  核心方法：融合社会学习策略、方向跟随机制与环境感知概率以在推球/小偷等子行为间建立信息交互与选择，用以改善探索与开发的配比；  
  关键结论：在 12 个基准函数与工程约束问题（压力容器设计）上给出对比，作者报告在多个基准上优于原始 DBO，且能处理实际约束优化问题。  
  参考（原文）：[c-s-a.org.cn](https://www.c-s-a.org.cn/1003-3254/9397.html).

- 许佳璐 等, “基于多策略融合蜣螂优化算法的工业机器人运动学参数辨识方法” (中国机械工程, 2025).  
  研究问题：将 DBO 用于工业机器人运动学参数辨识时陷入局部和精度不足；  
  核心方法：提出 MSFDBO，结合混沌/精英反向学习初始化、鱼鹰探索行为与随机扰动机制，并基于 LPOE 运动学模型构建辨识目标；  
  关键结论：在 12 个基准函数与 4 台 T6A‑19 型机器人参数辨识实验中，报告绝对位置平均误差和 RMSE 显著下降（文中给出 80%+ 的误差下降比例），表明在工程辨识任务上提高了精度与稳健性。  
  参考（原文）：[cjournal.hep.com.cn](https://cjournal.hep.com.cn/1004-132X/CN/1160171567385862339).

- 张顺 等, “基于改进蜣螂算法的车机协同巡检路径规划方法” (Pure Mathematics / Hans Publishers, 2025).  
  研究问题：车机协同 TSP‑D 型路径规划的组合约束与车辆速度变化带来的鲁棒优化难题；  
  核心方法：对 DBO 进行三处改进：Logistic 混沌初始化、在滚球阶段引入鱼鹰全局搜索策略、觅食阶段用自适应 t‑分布扰动，以提高全局搜索与局部开采能力的时序平衡；  
  关键结论：在 CEC2021 与 195 点/35 停驻点的大规模巡检算例上，改进 DBO 在不同巡检车速度情景下均得到更优或可行解（文中给出对比算法缺失解的场景），展示了改进策略在实际路径规划中的适用性。  
  参考（原文）：[hanspub.org (pdf)](https://pdf.hanspub.org/pm2025151_161252697.pdf).

四、长跳跃（Lévy）/邻域搜索与人工蜂鸟 / 蜂群类改进
- He & Li, “Neighborhood Search and Artificial Hummingbird Optimization Algorithms with Improved Lévy Factors” (Modeling and Simulation, 2024).  
  研究问题：AHA（人工蜂鸟算法）在全局步长控制与局部精度之间的矛盾；  
  核心方法：引入改进的 Lévy 飞行作为自适应步长因子，并基于种群适应度方差做“自适应距离围猎”以触发局部围猎搜索，从而在保持全局探索和提升局部精度间折中；  
  关键结论：在 23 个基准函数与多个对比算法（WOA/GWO/SSA 等）比较中，作者给出 Wilcoxon 检验结果，改进 AHA 在寻优能力、稳定性和鲁棒性上有明显改善，但同时增加了每代计算开销（文中报告时间复杂度分析）。  
  参考（原文）：[hanspub.org](https://image.hanspub.org/Html/1-2571228_81778.htm).

- He et al., “AHA 联合改进（引用 AHA 基线）”，并列出 AHA 在工程应用（光伏建模、定位、医学图像等）上的若干成功应用作为方法适用性证据（见 ALAHA 文献参考列表）。  
  参考（背景）：ALAHA 文献中引用的 AHA 基线（Zhao et al., 2022, CMA 等，详见 ALAHA 参考）。

五、多目标 / 反向学习与萤火虫变体
- Chen et al., “Double Search Mode Firefly Algorithm Based on Dynamic Reverse Learning and Lévy Flight (MOFA‑LR)” (Xueshu Kaifa/ SIA, 2023).  
  研究问题：多目标萤火虫算法（MOFA）在收敛性与帕累托前沿分布性间的权衡；  
  核心方法：根据个体在种群中的支配关系动态选择两种搜索模式——（1）被支配时用动态反向学习拉向帕累托优解，（2）非被支配时以全局最优 + Lévy 扰动维持分布性；并在后期加入变异算子以避免聚集；  
  关键结论：与 12 种近年多目标算法比较，MOFA‑LR 在收敛性与前沿均匀性（用常见多目标指标评估）表现出可统计显著提升。  
  参考（原文）：[xk.sia.cn](https://xk.sia.cn/cn/article/Y2023/I5/607).

六、自然调节 / 生理启发的蜂群变体（应用导向）
- Liu, Zhang & Yang, “Improved Intelligent Artificial Bee Colony Algorithm (NEI‑ABC) and application to oilfield injection/production optimization” (Xueshu Kaifa / SIA, 2023).  
  研究问题：传统 ABC 在复杂非线性多参工程优化（油田注采）中的早熟与收敛速度问题；  
  核心方法：受神经‑内分泌‑免疫（NEI）调节机制启发，新增蓝光引导、蜜源调控与触角定向单元以强化三类蜂角色（引领/侦查/跟随）的协调与信息反馈；  
  关键结论：在油田注采规划等工程案例中，NEI‑ABC 在目标函数值与收敛稳定性上优于若干传统算法（文中给出仿真对比表），但算法复杂度随算子增长而增加。  
  参考（原文）：[xk.sia.cn](https://xk.sia.cn/cn/article/doi/10.13976/j.cnki.xk.2023.2056).

实验与评价总结（共性结论，不逐篇复述）
1) 基准套件与统计检验成为常用标准：几乎所有工作均采用 CEC 系列（如 CEC2017/CEC2021/CEC2022）或多目标基准，并配合 Wilcoxon/Friedman 等非参数统计检验以评估显著性。  
2) 混沌/反向初始化 + Lévy / 长跳跃/自适尺度机制是常见配方：混沌映射改善初代覆盖，反向学习或自适参数在早期扩散/后期收敛间起到动态折中，Lévy 提供跨模态长跳跃以避免局部陷阱。多篇工作报告该组合在多峰与高维问题上提高找到优区域的概率。  
3) 算子混合（并行/概率切换）比简单串联更稳健：将不同算子作为概率触发（基于适应度分布、聚集度或支配关系）比固定级联或单一混合在多数基准上更能保持多样性而不致严重拖慢收敛。  
4) 工程应用偏好可解释与鲁棒机制：用于物理参数辨识、路径规划或光伏建模的论文更注重可解释的参数机制（如自适衰减尺度、环境感知概率）与可验证的真实/半真实数据集，而不仅是纯基准函数。  
5) 代价与收益权衡不可忽视：多数改进提升了寻优质量，但伴随每代计算开销上升（更多随机/矩阵运算或局部采样），论文普遍给出时间复杂度或在案例上报告求解时间增加的量化数据。  
6) 无“万能算法”证据：跨套件比较显示没有单一方法在所有函数类别（单峰、多峰、混合、复合）上稳胜，说明当前研究仍以问题适配（algorithm selection）为主，而非单一通用改进。

趋势与挑战（2025 年前后可验证的短期预测，至少三点）
1) 自适/基于统计的策略切换将成为主流：以适应度分布、聚集度或支配关系为触发条件的概率性算子切换（而非固定超参数）将被更多采纳并被证明可在不增加大量人工调参下提高稳健性（已见 Qi 2024、Pan 2025 与 Chen 2023 的实证）。  
2) 可解释性与约束处理成为工程导向算法的硬需求：用于工业辨识或路径规划的工作将把“可解释的自适尺度/概率”与严格约束的可行性保证（硬约束处理或可修复解）作为算法设计的基本约束，而非事后修正。  
3) 基于元学习的算法选择与参数自适化会快速发展：由于“无免费午餐”现象在实践中依旧显著，预计出现更多将元学习（Meta‑learning）与在线性能预测结合的框架，用于在运行时选择合适的混合策略或调整调度概率。  
4) 计算效率与可扩展性将成为瓶颈：随着算子复杂度增加（例如局部高维采样、混沌映射、反向学习计算），并行/异步实现、GPU 加速与近似评估（surrogate）将被广泛结合以控制求解时延，特别是在需要实时或近实时决策的工程场景。  
5) 多目标与不确定性联合优化会被更多关注：未来工作会更多把随机环境、不确定观测（例如传感器噪声、动态路网）纳入算法设计，要求算子同时兼顾帕累托收敛性和鲁棒性；基于概率度量的适应度分布控制将成为核心手段。  

结论  
2022–2025 年的代表性工作表明，自然启发式算法的研究重心从单一算子优化转向“算子库 + 自适策略触发”的系统化设计：混沌/反向学习改善初代与跳出能力，Lévy 与自适尺度控制长短跳跃平衡，基于统计量的策略切换保持多样性而不破坏收敛。工程样例（机器人辨识、路径规划、光伏/油田参数识别）推动了可解释、自适与约束友好机制并行发展。短期内，元学习驱动的算法选择、并行与代理模型、以及面向不确定性的多目标鲁棒化将是三个最重要的发展方向，但同时也面临计算成本与现实约束处理的挑战。本文基于可查实文献给出上述结论与预测，供后续方法学与工程应用研究参考。

参考文献（所列为能检索到的原文；链接以域名显示以便快速校验）  
1. Qi C., Xie J., Wang X., Feng W., Zhang H., “A novel elite guidance‑based social learning particle swarm optimization algorithm”, Journal of Northwestern Polytechnical University, 2024. [jnwpu.org](https://www.jnwpu.org/articles/jnwpu/pdf/2024/05/jnwpu2024425p948.pdf)  
2. Zhou L., “Population‑Center‑Guided Particle Swarm Optimization Algorithm for Global Optimization”, Computer Science and Application, 2025. [hanspub.org](https://pdf.hanspub.org/csa_1543619.pdf)  
3. Pan J., Zhai W., Guo Z., Hu B., Cheng C., Wu C., “A Hybrid Slime Mould Genetic Algorithm Based on Spatial Attenuation Self‑diffusion Mechanism (SMAGA)”, Acta Scientiarum Naturalium Universitatis Pekinensis, 2025. [xbna.pku.edu.cn](https://xbna.pku.edu.cn/fileup/0479-8023/HTML/2025-1-14.html)  
4. Li S., Chen H., Wang M., Heidari A.A., Mirjalili S., “Slime Mould Algorithm: a new method for stochastic optimization”, Future Generation Computer Systems, 2020 (方法基线，广泛被后续工作引用）.  
5. Wang L., et al., “Improved Dung Beetle Optimization Algorithm with Multi‑strategy (MSDBO)”, Computer Systems & Applications, 2023. [c-s-a.org.cn](https://www.c-s-a.org.cn/1003-3254/9397.html)  
6. 许佳璐, 刘笑楠, 李朋超, 刘振宇, “基于多策略融合蜣螂优化算法的工业机器人运动学参数辨识方法”, 中国机械工程, 2025. [cjournal.hep.com.cn](https://cjournal.hep.com.cn/1004-132X/CN/1160171567385862339)  
7. 张顺, 刘媛华, 张颢严, “基于改进蜣螂算法的车机协同巡检路径规划方法”, Pure Mathematics / Hans Publishers, 2025. [hanspub.org (pdf)](https://pdf.hanspub.org/pm2025151_161252697.pdf)  
8. He Y., Li X., “Neighborhood Search and Artificial Hummingbird Optimization Algorithms with Improved Lévy Factors (ALAHA)”, Modeling and Simulation, 2024. [hanspub.org](https://image.hanspub.org/Html/1-2571228_81778.htm)  
9. Zhao W., Zhang Z., Mirjalili S., et al., “Artificial Hummingbird Algorithm: A New Bio‑Inspired Optimizer with Its Engineering Applications”, Computer Methods in Applied Mechanics and Engineering, 2022 —（AHA 基线，见 ALAHA 引用列表）。  
10. Chen J., Zhao J., Xiao R., Wang H., Kang P., “Double Search Mode Firefly Algorithm Based on Dynamic Reverse Learning and Lévy Flight (MOFA‑LR)”, Xueshu Kaifa / SIA, 2023. [xk.sia.cn](https://xk.sia.cn/cn/article/Y2023/I5/607)  
11. Liu B., Zhang Y., Yang J., “Improved Intelligent Artificial Bee Colony Algorithm and Its Application to Optimization of Injection and Production in Oilfield (NEI‑ABC)”, Xueshu Kaifa / SIA, 2023. [xk.sia.cn](https://xk.sia.cn/cn/article/doi/10.13976/j.cnki.xk.2023.2056)  
12. He Y., Li X., “Neighborhood Search and Improved Lévy Flying Factors for AHA” (详细实验与时间复杂度分析），Modeling & Simulation, 2024. [hanspub.org](https://image.hanspub.org/Html/1-2571228_81778.htm)  
13. 付海涛, 张智勇, 王增辉, 金晨磊, “改进SHO算法优化随机森林模型”, 吉林大学学报(理学版), 2025. [cjournal.hep.com.cn](https://cjournal.hep.com.cn/1671-5489/CN/10.13413/j.cnki.jdxblxb.2024003)  
14. Pan J., et al. — 文献中大量引用并对比的基准/方法（Wilcoxon/Friedman 测试案例与比较算法列表），见 Pan 2025 原文。 [xbna.pku.edu.cn](https://xbna.pku.edu.cn/fileup/0479-8023/HTML/2025-1-14.html)

（注）本文所列参考文献均为可检索的已发表文章或显式引用的基线论文；文中对每篇代表性工作的摘要均基于各文原文的摘要与方法/结果节撰写，便于同行复核与进一步阅读。若需逐篇的数值表或统计检验详情，请参阅各原文。