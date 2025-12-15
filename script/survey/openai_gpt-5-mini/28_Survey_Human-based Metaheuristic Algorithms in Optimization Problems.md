引言  
人本（human‑based）元启发式算法把人类学习、社会学习或人类—机器协同设计的认知与交互特征作为启发，近三年（2022–2025）在组合优化、约束多目标、工程参数辨识与自动算法生成等领域出现了多条互补发展路线。本文在 2022–2025 年文献范围内，围绕三类方法（心理/认知驱动的人类学习优化、以人类社会学习为模型的社会学习型群体智能、以及以人经验/提示与启发式共同进化的自动算法设计），挑选代表性工作逐一凝练（每篇 4–6 句），并归纳它们在实验设计、评测指标与共同结论上的共性，最后给出面向 2025 年前后的可验证研究趋势与挑战预测。所引文献均为公开期刊 / 会议 / arXiv 源（见参考文献）。

方法分类与代表作（每类 3 篇以内，按代表性排序）

A. 人类学习（心理/认知）启发的优化算法  
1) Zhang 等 — “Novel human learning optimization algorithm for multidimensional knapsack problem” (Application Research of Computers, 2024). [arocmag.cn]  
- 研究问题：多维背包问题（多约束组合优化）的高精度求解。  
- 核心方法：提出了一种“人类学习优化（Human Learning Optimization, HLO）”变体，算法中引入了记忆表示（哈希存储过去经验）、自适应学习算子选择以及变邻域局部搜索以模拟人类记忆/对比式学习过程。  
- 关键实验结论：在 76 个标准实例（含超大规模）与若干对照算法（包括二进制 PSO、遗传算法等）上，HLO 在寻优精度和稳定性（均值与方差）上系统优于对比组，说明记忆表征与自适应学习算子对多维离散问题有明显增益。  

B. 以社会/群体“人类社会学习”机制为模型的群体智能改进（PSO 类）  
1) 齐铖 等 — “A novel elite guidance‑based social learning particle swarm optimization (ESLPSO)” (Journal of Northwestern Polytechnical University, 2024). [jnwpu.org]  
- 研究问题：经典 PSO 易早熟、对单一 gbest 过度依赖导致丧失多样性。  
- 核心方法：构建分层拓扑（精英/平民粒子）、精英引导的社会学习算子与极值扰动迁移机制；用 cubic 混沌初始化增强起始覆盖。  
- 关键实验结论：在 12 个单/多峰和旋转多峰基准（30 维）上，ESLPSO 在均值、最优与种群多样性曲线上常显著优于 7–8 种 PSO 改进算法，尤其在多模态跳出局部解能力上表现出更强的波动恢复（由扰动触发）。  

2) 周刘长 — “Population‑Center‑Guided Particle Swarm Optimization (PSOSI)” (Computer Science and Application, 2025). [pdf.hanspub.org]  
- 研究问题：如何利用种群整体信息提升 PSO 的全局探索能力并降低早熟风险。  
- 核心方法：在速度更新中额外引入“种群中心”引导项，并结合种群聚集度驱动的局部扰动策略（分为 PSOSI 与 PSOLP 两个变体）。  
- 关键实验结论：在 CEC‑2022 基准与若干工程优化问题（包括 8 个工程设计问题）上，基于种群中心的引导可提升收敛稳定性并在多数测试上优于标准 PSO 与若干主流对比算法（通过 Wilcoxon / Friedman 统计检验验证）。  

C. 人经验/提示（prompt）与启发式并行演化：自动算法设计与人机联动  
1) Liu 等 — “Experience‑guided reflective co‑evolution of prompts and heuristics for automatic algorithm design” (arXiv, 2025) — EvoPH. [chatpaper.com]  
- 研究问题：自动生成与优化启发式算法以解决组合优化（例如 TSP、装箱问题），并克服演化停滞于局部最优的问题。  
- 核心方法：提出 EvoPH 框架——将 LLM‑driven 提示与启发式算法种群共同演化，使用岛屿迁移模型与精英选择、并以性能反馈驱动提示与启发式的反思性改进（prompt + heuristic co‑evolution）。  
- 关键实验结论：在旅行商问题与装箱问题上，EvoPH 相较于纯启发式或单纯 LLM 生成的启发式，取得更低的相对误差，表明“经验引导的提示—启发式共同演化”能有效扩展搜索多样性并改进算法设计质量。  

D. 协同 / 多种群范式（具有人类团队协作类比）——对复杂约束与多目标问题的启发式协同  
1) 丁炜超 等 — “Two‑population co‑evolutionary algorithm for constrained multi‑objective optimization problems in complex feasible domains” (Acta Automatica Sinica, 2025). [aas.net.cn]  
- 研究问题：具有复杂可行域（不连续、小集合等）的约束多目标优化在保持多样性与快速收敛之间存在选择压力矛盾。  
- 核心方法：提出双种群协同进化框架（粒子群 + 向量群），粒子群利用辅助档案与逃逸机制加速收敛，向量群采用无约束参考向量法以维护前沿分布；并设计动态 ε‑约束松弛策略以跨越不可行区域。  
- 关键实验结论：在 73 个基准与真实问题上（含 DAS‑CMOP、LIR‑CMOP 等），所提 TCCMOA 在 IGD+ / HV 等指标上显著优于对比算法，证明双种群协同在复杂约束场景下有利于同时维护多样性与收敛。  

补充性理论/综述类参考（方法论与实践联系）  
1) 刘义庆 等 — “遗传算法协同优化改进理论与应用研究” (Software Engineering and Applications, 2025). [pdf.hanspub.org]  
- 概述遗传算法在协同优化/多目标/自适应参数调控等方向的进展，强调异构算法深度融合、边缘计算与数字孪生为协同优化带来的工程机遇，并提出量子-经典融合等未来方向（本文为方法论型补充，帮助把“人类协作”类比提升为工程可落实框架）。  

实验与评价总结（仅总结共性结论，不逐篇复述）  
- 评价数据集与指标：近年的工作在数值基准（如 CEC 系列、DTLZ/C‑DTLZ、ZXH‑CF、DAS‑CMOP 等）、若干标准工程问题（多维背包、压力容器、压缩弹簧、焊接梁等）与真实应用场景上进行验证；常用指标为平均值/标准差、IGD/IGD+、HV、收敛曲线及 Wilcoxon / Friedman 显著性检验。  
- 算法设计共性有效成分（跨研究的经验总结）：（1）基于人类学习/社会学习的结构化记忆或种群级引导（记忆表、种群中心、精英引导）能显著提高初期与中期的搜索覆盖与信息传递效率；（2）随机或条件扰动（基于聚集度/停滞步数触发）在恢复多样性、跳出局部极值上是普遍且必要的策略；（3）多种群/协同框架（双种群、辅助档案、辅助评价代理）在复杂可行域与多目标场景中更容易同时满足多样性与收敛性。  
- 实验局限与可复现性问题共性：许多论文使用的问题集、参数与实现细节（例如混沌映射参数、扰动阈值）对性能影响大，但开源实现与完整消融实验不总是齐全，导致跨论文直接比较有限制。  

趋势与挑战（面向 2025 年前后，至少 3 点）  
1) 从“人类启发”到“人—模型混合认知算子”：预计未来 2–3 年内更多工作将把形式化认知模型（记忆容量、对比学习机制、分层决策）嵌入算子设计，并与数据驱动代理（surrogate）联合，以在高维约束问题上替代经验式参数调优。  
2) LLM/提示与启发式算法的共演化（自动算法设计）将进入工程化验证阶段：EvoPH 类框架已证明提示与启发式的联合演化能改善算法质量，下一步方向是建立可度量的“提示—启发式性能回路”、标准化提示表示与可复现的评测协议。  
3) 多种群 / 协作式进化成为处理复杂可行域与多目标问题的常用范式：双种群、岛屿模型与带辅助档案的协同机制将与动态 ε‑约束、逃逸机制整合，用以应对不连续可行域与稀疏可行解问题。  
4) 理论性与可解释性要求上升：随着人本启发算子复杂性增加，必须补充严格的收敛/多样性界（或至少概率性保证）与可解释的算子语义（例如，“何种记忆结构导致何类搜索动态”）。  
5) 工程部署与资源约束（边缘/实时）将推动轻量化人本算子与在线自适应策略：在物联网、机器人在线标定等场景中，算子需在受限 CPU/能耗下保持可解释的自适应性，促使研究关注计算-样本效率与渐进稳健性。  

结论  
2022–2025 年的人本元启发式研究已从单点算法改进逐步走向结构化、可解释且与机器学习工具（代理模型、LLM）结合的协同框架。社会学习式 PSO 变体（精英引导、种群中心引导）、基于人类学习模型的 HLO 变体，以及提示‑启发式共同演化的自动算法设计代表了三条互补主线：分别解决多样性维护、组合/离散问题高精度求解与算法自动生成。要推进该领域进入工程化、可复现和理论化的下一阶段，研究者需在公开实现、标准化评测与理论分析上做更多工作。

参考文献（按文中出现顺序，均为公开期刊 / arXiv / 学术期刊条目；文中引用的网络入口见后缀）  
- Zhang Y., Liu Y., Ma L. 等. 多维背包问题的新型人类学习优化算法. 计算机应用研究, 2024. [arocmag.cn](https://www.arocmag.cn/abs/2024.04.0127)  
- Qi C., Xie J., Wang X., Feng W., Zhang H. A novel elite guidance‑based social learning particle swarm optimization algorithm. Journal of Northwestern Polytechnical University, 2024. [jnwpu.org](https://www.jnwpu.org/articles/jnwpu/pdf/2024/05/jnwpu2024425p948.pdf)  
- Zhou L. Population‑Center‑Guided Particle Swarm Optimization Algorithm for Global Optimization. Computer Science and Application, 2025. [pdf.hanspub.org](https://pdf.hanspub.org/csa_1543619.pdf)  
- Liu Y., Li J., Zhao W. X., Lu H., Wen J. R. Experience‑guided reflective co‑evolution of prompts and heuristics for automatic algorithm design. arXiv:2509.24509 (EvoPH), 2025. [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/192842)  
- Ding W.‑C., Sun L.‑Y., Luo F., Gu C.‑H., Dong W.‑B. Two‑population co‑evolutionary algorithm for constrained multi‑objective optimization problems in complex feasible domains. Acta Automatica Sinica, 2025. [aas.net.cn](https://aas.net.cn/cn/article/doi/10.16383/j.aas.c250023)  
- Liu Yiqing, Tu Yiqiang, Lu Houqing. 遗传算法协同优化改进理论与应用研究. Software Engineering and Applications, 2025. [pdf.hanspub.org](https://pdf.hanspub.org/sea_2691144.pdf)  
- Kennedy J., Eberhart R. Particle Swarm Optimization. Proceedings of ICNN’95, 1995. (基础性算法原文，作为方法学背景)  
- Shi Y., Eberhart R. A modified particle swarm optimizer. Proceedings of IEEE CEC, 1998. (PSO 参数/收敛启示)  
- Liang J., Qin A. K., Suganthan P. N., Baskar S. Comprehensive learning PSO. 2004. (CLPSO，社会/综合学习线索)  
- Heidari A. A., Mirjalili S., et al. Harris Hawks Optimization: Algorithm and Applications. Future Generation Computer Systems, 2019. (示例性启发式算法设计与比较背景)  
- 文中用于对比或引用的若干基准与方法性资料（在各原文中列为参考）：CEC‑2022、DTLZ / DTLZ‑variant、ZXH‑CF、DAS‑CMOP 等（详见对应论文）。  
- 其他被本文用作方法论与实验比较背景的近期工作与综述，见上文与各代表作参考文献列表内所引引用文献。  

注：为便于读者检索，文中所有直接以 web 源引用的代表性论文链接已在各条目末尾给出（使用其发布机构/期刊的公开页面）。如需我把每篇代表性工作对应的实现代码、参数设置与可复现实验脚本整理成清单（包括可公开获取的 GitHub / 仿真参数），我可以继续补充。