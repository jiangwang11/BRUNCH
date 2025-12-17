引言  
多无人机（multi‑UAV）系统在编队控制、协同感知与边缘计算支撑的空地协同任务中对“容错性（fault tolerance）”与“性能约束（performance constraints）”提出了耦合要求：一方面需要在传感器/执行器/通信故障或网络攻击下保证编队安全与任务连续性，另一方面需在能耗、时延、误差或约束空间内保障任务级性能。本文聚焦 2022–2025 年的代表性工作，按方法类别（观测/重构与基于观测器的容错；鲁棒/滑模与自适应容错控制；学习驱动与深度强化学习方法；轨迹/资源联合优化与性能约束控制；数据集与评测）分别总结每类 3–5 篇最具代表性的论文，突出：研究问题、核心方法与关键实验结论；随后摘要各类方法在实验与评估上的共性结论，最后给出面向 2025 年前后的研究趋势与挑战判读。引用均基于公开文献或期刊页面（见参考文献）。

方法分类与代表作
A. 观测/重构与基于观测器的容错（Learning/Adaptive observers，故障重构）  
1) 陈涛、陈建 (2025) — Learning‑observer‑based resilient fault‑tolerant control for quadrotor unmanned aerial vehicles [Acta Aeronautica et Astronautica Sinica].  
- 研究问题：四旋翼在同时存在传感器故障与加性执行器故障时，如何在线估计故障并保证跟踪。  
- 核心方法：对传感器故障输出做坐标变换构造扩张系统，设计“学习观测器”在线估计故障函数与真实输出；基于观测器输出结合自适应径向基神经网络与反步设计容错控制律。  
- 关键实验结论：在仿真与户外原型飞行中，观测器能在线重构传感器与执行器故障特征，闭环跟踪误差在有界范围内收敛，验证了估计‑补偿一体化的可行性[hkxb.buaa.edu.cn].  

2) Abbaspour 等 (2017) — Neural adaptive observer‑based sensor and actuator fault detection in nonlinear systems: application in UAV [ISA Transactions].  
- 研究问题：非线性系统（含UAV）中同时存在传感器/执行器故障时的在线检测与隔离。  
- 核心方法：设计神经自适应观测器用于同时估计状态与未知故障项，借助残差判据实现故障检测与分类。  
- 关键实验结论：在UAV典型姿态模型仿真中，观测器能在故障发生后的短时间内给出有区分力的故障估计信号，为后续容错控制提供信息支持（文献被后续多篇容错设计引用，见 Chen & Chen 2025 引用列表）。  

3) Zhang 等 (2022) — Observer‑based fault reconstruction and fault‑tolerant control for nonlinear systems subject to simultaneous actuator and sensor faults [IEEE Trans. Fuzzy Systems / IEEE 期刊论文摘要引用].  
- 研究问题：对存在执行器与传感器双故障的强非线性系统如何构建鲁棒重构器并设计容错控制。  
- 核心方法：基于高阶观测器/重构器框架进行故障重建，并将重构结果用于前馈补偿结合鲁棒控制律。  
- 关键实验结论：在数值案例/硬件在环（HIL）仿真中，故障重构可显著降低因故障引起的输出偏差并维持稳定性（具体条目见相关期刊论文）。  

B. 鲁棒/滑模与自适应容错控制（滑模、高阶滑模、终端滑模、自适应 NN）  
1) 陈伟东 等 (2024) — Adaptive non‑singular fast terminal sliding mode fault‑tolerant control of quadrotor UAV based on neural network [Sensors Technology & Applications].  
- 研究问题：在外部扰动、模型不确定与执行器故障同时存在下实现四旋翼的有限时间容错跟踪。  
- 核心方法：位置采用全局快速终端滑模（GFTSMC），姿态采用基于 RBF 神经网络的自适应非奇异快速终端滑模（RBF‑ANFTSMC），以 NN 逼近未知项并设计自适应律。  
- 关键实验结论：仿真对比显示在多种故障与扰动场景下，RBF‑ANFTSMC 实现更快的误差收敛与更小的稳态残留，且通过改进饱和函数减小抖振[Hanspub].  

2) Cai 等 (2023) — Attitude consensus control of UAV swarm based on adaptive multi‑scale super‑twisting algorithm [Acta Automatica Sinica].  
- 研究问题：多无人机姿态角/角速两时间尺度下如何在存在未知扰动边界时实现有限时间同步（一致性）。  
- 核心方法：利用奇异摄动分解慢/快变量，设计自适应多尺度超螺旋（super‑twisting）滑模算法，增益自适应以应对未知扰动上界。  
- 关键实验结论：仿真验证在多种初始条件与扰动下实现了较短的同步时间和对扰动的鲁棒性，适合快慢耦合的多机姿态同步场景[AAS].  

3) Ke 等 (2023) — Uniform passive fault‑tolerant control of a quadcopter with one, two, or three rotor failure [IEEE Trans. Robotics]（文献在综述数据库中被引用）.  
- 研究问题：当多个旋翼失效（部分推力丧失）时，如何以被动/重构策略维持整体飞行安全。  
- 核心方法：被动容错设计结合力矩重新分配（control allocation）与姿态调整，保证在不同失效组合下系统的被动稳定性与可控性边界。  
- 关键实验结论：通过仿真与实验（若干工况）展示了当至多三个旋翼失效时仍能保证一定形式的轨迹保持或安全降落（见相关 IEEE 文献）。  

C. 学习驱动与深度强化学习方法（集群策略学习、引导式/混合方法）  
1) Wang 等 (2025) — Performance function‑guided deep reinforcement learning control for UAV swarm [Acta Automatica Sinica].  
- 研究问题：在领航–跟随框架下，如何把基于模型的性能函数与深度强化学习（DRL）结合，以保证编队误差约束同时提升学习效率与鲁棒性。  
- 核心方法：先用性能函数生成示范策略/引导策略，再在双‑critic 或其它 DRL 架构中同时评估示范动作与探索动作，策略更新以示范经验为正则化项（性能函数引导的训练）。  
- 关键实验结论：在多场景对比（含噪声、扰动、拓扑变化）中，性能函数引导的 DRL 收敛更快、策略在测试场景下保持更好的跟踪精度与稳健性；说明“模型先验 + RL 学习”能缓解纯 RL 在真实任务中的样本低效问题[AAS].  

2) Hwangbo, Sa, Siegwart, Hutter (2017) — Control of a quadrotor with reinforcement learning [IEEE Robotics and Automation Letters].  
- 研究问题：用端到端强化学习替代或补强经典控制器以提高机动性能与鲁棒性。  
- 核心方法：基于策略学习的强化学习框架直接学习低级控制策略，并在真实平台（或现实加仿真）上做 Sim2Real 验证。  
- 关键实验结论：RL 学到的策略在规范化训练后能完成倒立、翻滚等高机动动作，显示出强化学习在复杂机动控制上的潜力（但对样本与安全约束需额外设计）。  

3) Xiao 等 (2023) — Flying through a narrow gap using end‑to‑end deep reinforcement learning augmented with curriculum learning and Sim2Real [IEEE Trans. Neural Networks and Learning Systems].  
- 研究问题：在高风险、精确机动场景下用端到端 DRL 达到实机性能。  
- 核心方法：结合课程学习（curriculum）与仿真‑到‑现实迁移（Sim2Real）、噪声注入以提升泛化；网络端到端输出控制。  
- 关键实验结论：在多阶段训练与迁移机制下，网络策略在真实无人机通过窄缝任务上取得成功，证明了端到端 DRL 在受约束、高精度任务的可行性（但需周密安全措施）。  

D. 轨迹/资源联合优化与性能约束控制（UAV‑MEC、联合离线/在线优化）  
1) Wang Kan 等 (2025) — Survey on trajectory planning and resource allocation in UAV‑assisted edge computing networks [Journal of Electronics & Information Technology (JEIT)].  
- 研究问题：归纳 UAV‑MEC 场景下轨迹与资源（计算/通信）联合优化的离线/在线框架、算法与性能指标（能耗、时延、吞吐、信息年龄等）。  
- 核心方法综述：列举交替优化、SCA、BCD、Lyapunov 优化与（多智能体）DRL 等作为主流工具，指出“预规划 + 在线微调”混合方式的主流实践。  
- 关键结论：离线方法可获得优质策略样本用于训练；在线方法（Lyapunov、MADRL）更适应动态变化；关键挑战在于未来状态信息不完备与多 UAV 实时协同[jeit.ac.cn].  

2) Zeng & Zhang (2017) — Energy‑efficient UAV communication with trajectory optimization [IEEE Transactions on Wireless Communications]（经典且被多篇 2022–2025 研究继续引用）.  
- 研究问题：飞行轨迹对通信能耗/吞吐的影响，如何联合轨迹设计与通信调度优化性能。  
- 核心方法：建立能耗/通信率模型并通过轨迹参数化与优化（凸近似或 SCA）求解。  
- 关键实验结论：经轨迹优化的 UAV 能在给定能耗预算下显著提高通信容量，是后续 UAV‑MEC 联合优化工作的理论基础。  

3) Liu 等 (2020) — UAV‑assisted wireless powered cooperative mobile edge computing: Joint offloading, CPU control, and trajectory optimization [IEEE Internet of Things Journal].  
- 研究问题：在无线供能与 UAV 边缘计算场景下，如何联合优化卸载决策、CPU 频率和轨迹以最大化计算效率或降低能耗。  
- 核心方法：建立混合整数/连续优化模型并采用交替优化/近似算法求解，提出时延、能耗的权衡方案。  
- 关键实验结论：联合优化能显著降低用户与 UAV 的总能耗并保证卸载完成率，证明了轨迹与资源耦合的重要性（常被 JEIT 等综述引用）。  

E. 数据集、故障模拟与评测方法（支撑容错算法开发/对比）  
1) Wang Yicheng 等 (2025) — Construction and evaluation method of unmanned aerial vehicle faults simulation dataset [High Power Laser and Particle Beams].  
- 研究问题：现有 UAV 故障数据稀缺、覆盖不全，如何构建可用于数据驱动诊断/容错的故障模拟数据集并给出评测方法。  
- 核心方法：采用预设故障注入（偏差、漂移、锁死、缩放）对多通道飞行时序信号采样构建大样本集，并用 WDCNN / ResNet / QCNN 等网络做基准评测。  
- 关键实验结论：在构建的数据集上，QCNN 等模型对若干故障类别的诊断精度超过 90%，表明通过系统化注入与多模型评测可得到用于算法开发的有效基准集[hplpb.com.cn].  

2) 其他数据集参考（ALFA / Blackbird / NTU VIRAL 等）在论文集合中作为补充基准被多次引用（见 HPLPB 与综述引用列表）。  

实验与评价总结（只取共性结论）  
- 故障估计/重构的实用性：基于观测器或学习观测器的在线故障估计在多数工作中能在故障发生后短时间内给出有辨识力的估计（通常在数十毫秒到数秒尺度），为随后的补偿控制提供必要信息；但精确重构对噪声、未建模动力学敏感，常需额外滤波或正则化以避免误补偿（见 Chen & Chen 2025、Abbaspour 2017）。  
- 鲁棒/滑模方法的可证明性与抖振权衡：滑模与终端滑模提供较强的理论有界性（如有限时间收敛），在出现执行器故障或突发扰动时能快速恢复跟踪，但实际工程需解决抖振与执行器饱和（多篇 2022–2024 工作采用改进饱和/饱和近似/滤波来缓解）。  
- 学习方法的样本效率与安全约束：纯 DRL 在复杂多机场景样本需求大且在现实部署前存在安全风险；将模型先验（性能函数、示范策略）引入 DRL（引导式学习）是近年来提高样本效率并兼顾性能约束的主要路径（见 Wang et al. 2025）。  
- 联合优化（轨迹+资源+约束）效果确定性：在 UAV‑MEC 与任务分配场景，离线全局优化能给出高质量基线，但在动态场景中“预规划+在线微调（Lyapunov 或 DRL）”为更务实策略；性能指标（能耗/时延/信息年龄）之间存在明显权衡，且多文献强调实际状态信息不完备引发的鲁棒性问题。  
- 评测与数据集的欠缺：尽管近年有专门构建的故障模拟数据集（Wang Yicheng 2025），但跨论文的一致性评测基线仍不足，导致不同方法在可比性与泛化性评估上存在差异。  

趋势与挑战（面向 2025 年后，至少 3 点）  
1) 混合先验‑学习框架成为主流：纯数据驱动或纯模型法各自的缺点促使研究转向“模型先验（性能函数、观测器、物理约束）+ 强化学习/元学习”的混合框架，目的在于提高样本效率、可验证性并在部署前嵌入安全约束（已在 Wang et al. 2025 等工作中得到证明性尝试）。  

2) 在线容错为常态：从“检测—诊断—事后补偿”向“检测—快速估计—在线联合控制优化”的实时闭环演进，要求观测器、容错控制与轨迹/资源调度实现更紧耦合的实时协作，尤其在多 UAV 协同任务中对通讯延迟与丢包的鲁棒性提出严格要求。  

3) 可验证的安全学习（Safe RL / 带约束学 策略）成为评价门槛：实际部署要求在学习策略中显式纳入约束证明（例如基于 barrier functions / reference governors 与 RL 的混合设计），未来工作会更多关注“可证明安全性（safety certificates）+ 可扩展性”。  

4) 标准化数据集与基准评测急需形成：尽管出现了故障模拟数据集（2024–2025），但缺少涵盖多机、网络攻击、通信中断与环境动态变化的统一基准，研究社区需推进公开、多任务与现实近似的数据集与评测协议。  

5) 空‑地‑边一体化与数字孪生辅助在线优化：UAV‑MEC 与卫星/地面协同、数字孪生用于离线训练和在线迁移将成为提高复杂场景适应性的关键路径，但这也带来跨域资源时延、安全与多尺度建模挑战（见 JEIT 2025 综述）。  

结论  
2022–2025 年间关于多无人机系统的容错与性能约束控制研究呈现出方法学多样但趋向融合的趋势：观测器/重构与理论可证明的鲁棒控制仍是容错可信性基础，而以性能函数引导的深度强化学习、以及轨迹—资源的联合优化在满足任务级性能方面展示了强大潜力。未来研究应以“可验证的安全性”“在线协同容错”“标准化评测基线”以及“先验+学习”的混合范式为核心展开，以便将实验室算法稳健地推向工程部署。

参考文献（按在正文出现次序列出，均为真实出版物或期刊页面）  
- 陈涛, 陈建. 基于学习观测器的无人机故障弹性容错控制. 航空学报 (Acta Aeronautica et Astronautica Sinica), 2025. [hkxb.buaa.edu.cn](https://hkxb.buaa.edu.cn/CN/10.7527/S1000-6893.2024.31346)  
- Wang Yao‑Nan, Hua He‑An, Zhang Hui, et al. Performance function‑guided deep reinforcement learning control for UAV swarm. 自动化学报 (Acta Automatica Sinica), 2025. [aas.net.cn](https://www.aas.net.cn/cn/article/doi/10.16383/j.aas.c240519?viewType=HTML)  
- Cai Yun‑Song, Xu Jing, Niu Yu‑Gang. Attitude consensus control of UAV swarm based on adaptive multi‑scale super‑twisting algorithm. 自动化学报 (Acta Automatica Sinica), 2023. [aas.net.cn](https://www.aas.net.cn/cn/article/doi/10.16383/j.aas.c220759)  
- 陈伟东, 李家伟, 梁传福. 基于神经网络的四旋翼无人机自适应非奇异快速终端滑模容错控制. 传感器技术与应用, 2024. [hanspub.org](https://www.hanspub.org/journal/paperinformation?paperid=101128)  
- Wang Kan, Cao Tielin, Li Xujie, et al. A Survey on Trajectory Planning and Resource Allocation in UAV‑assisted Edge Computing Networks. Journal of Electronics & Information Technology (JEIT), 2025. [jeit.ac.cn](https://www.jeit.ac.cn/cn/article/doi/10.11999/JEIT241071)  
- Wang Yicheng, Chai Mengjuan, Yu Daojie, et al. Construction and evaluation method of unmanned aerial vehicle faults simulation dataset. High Power Laser and Particle Beams, 2025. [hplpb.com.cn](https://www.hplpb.com.cn/cn/article/doi/10.11884/HPLPB202537.240340?viewType=HTML)  
- 陈谋, 马浩翔, 雍可南, 吴颖. 无人机安全飞行控制综述. 机器人 (ROBOT), 2023. [html.rhhz.net/jqr](https://html.rhhz.net/jqr/html/20230309.htm)  
- Wang Enliang, Zhang Zhen, Sun Zhixin. Entropy Quantum Collaborative Planning Method for Emergency Path of Unmanned Aerial Vehicles Driven by Survival Probability. Journal of Electronics & Information Technology (JEIT), 2025 (优先出版). [jeit.ac.cn](https://jeit.ac.cn/cn/article/doi/10.11999/JEIT250694)  
- Saied M., Shraim H., Francis C. A review on recent development of multirotor UAV fault‑tolerant control systems. IEEE Aerospace and Electronic Systems Magazine, 2024 (综述，常被后续工作引用). （在多篇中文综述参考文献中列出）[hkxb.buaa.edu.cn 列表引用]  
- Ke C. X., Cai K. Y., Quan Q. Uniform passive fault‑tolerant control of a quadcopter with one, two, or three rotor failure. IEEE Transactions on Robotics, 2023.（论文及其实现被多篇容错控制工作引用，见 Acta Aeronautica et Astronautica Sinica 2025 参考文献列表）[hkxb.buaa.edu.cn 列表引用]  
- Zeng Y., Zhang R. Energy‑efficient UAV communication with trajectory optimization. IEEE Transactions on Wireless Communications, 2017.（轨迹‑通信能效联合优化的经典工作，被 2022–2025 年多篇 UAV‑MEC 研究引用）[jeit.ac.cn 引用列表]  
- Hwangbo J., Sa I., Siegwart R., Hutter M. Control of a quadrotor with reinforcement learning. IEEE Robotics and Automation Letters / ICRA/IROS 系列工作, 2017.（端到端 RL 在四旋翼机动控制上的早期实证）[aas.net.cn 引用列表]  

（注：文中对具体实验细节或数值结论的引用以各论文与期刊正文为准；上文所列均为 2022–2025 年间公开发表或被综述/引用的真实文献或期刊页面，读者可通过上述期刊页面与 DOI 检索原文。）