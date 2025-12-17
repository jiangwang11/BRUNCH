# 多无人机系统容错与性能约束控制研究综述（2022–2025）

## 引言

多无人机（Multi-UAV）系统在应急救援、集群作战与自主巡检等场景中应用日益广泛，但其高动态、强耦合与网络化特性使其对执行器/传感器故障与性能约束高度敏感。2022–2025年间，学界聚焦于融合**容错能力**（Fault Tolerance）与**性能保障**（Performance Constraints）的协同控制架构，旨在提升系统在复杂干扰、模型不确定与资源受限下的任务可靠性。本文系统综述该方向近三年代表性成果，按方法范式划分为四类：基于观测器的容错控制、滑模与终端滑模方法、强化学习与引导式学习、以及任务驱动的轨迹规划优化，并总结共性实验规律与未来研究趋势。

## 方法分类与代表作

### 1. 基于观测器的容错控制

该类方法通过在线估计故障与状态，实现对传感器/执行器故障的补偿。**陈涛与陈建**（2025）[hkxb.buaa.edu.cn](https://hkxb.buaa.edu.cn/CN/10.7527/S1000-6893.2024.31346) 针对四旋翼同时存在传感器与加性执行器故障的问题，提出**学习观测器**（Learning Observer）在线估计故障函数与实际输出，并结合自适应神经网络反步控制器实现弹性容错。户外实验证明，该方法在传感器偏置与执行器效率下降40%的复合故障下仍能实现厘米级轨迹跟踪。**Ma 等**（2019）[IEEE TII] 通过高增益非线性观测器联合诊断执行器与传感器故障，在四旋翼平台上验证了对阶跃型与缓变型故障的补偿能力。**Zhang 等**（2022）[IEEE TFS] 则设计模糊自适应观测器处理传感器故障，有效抑制了零点漂移与精度下降对姿态控制的影响。

### 2. 滑模与终端滑模方法

滑模控制因其强鲁棒性被广泛用于处理故障与不确定性。**蔡运颂等**（2023）[aas.net.cn](https://www.aas.net.cn/cn/article/doi/10.16383/j.aas.c220759) 提出**自适应多尺度超螺旋算法**（Adaptive Multi-scale STW），利用奇异摄动理论分离姿态角（慢）与角速度（快）动态，通过自适应增益处理未知扰动边界。仿真表明，其改进版本将集群姿态同步的平均收敛时间从2.59秒缩短至1.95秒。**陈伟东等**（2024）[hanspub.org](https://www.hanspub.org/journal/paperinformation?paperid=101128) 设计了**基于RBF神经网络的自适应非奇异快速终端滑模**（RBF-ANFTSMC）控制器，用于应对执行器故障与外部干扰。对比实验证明，在执行器效率降至52%时，其位置跟踪误差比传统NFTSMC降低40%以上，且通过改进饱和函数有效抑制了抖振。**Gao 等**（2022）[Aerospace Science and Technology] 则采用固定时间积分型滑模处理执行器故障，确保了姿态误差在预设时间内收敛。

### 3. 强化学习与引导式学习

为克服模型依赖与复杂工况下的性能退化，数据驱动方法被引入。**王耀南等**（2025）[aas.net.cn](https://www.aas.net.cn/cn/article/doi/10.16383/j.aas.c240519) 提出**性能函数引导的深度强化学习**（Performance Function-guided DRL）方法，将基于模型的性能函数作为“示范经验”辅助DRL策略训练。在领航-跟随编队中，该方法通过双Critic架构联合评估探索与示范动作，使编队跟踪误差比纯DRL基线降低30%以上，且在风扰下保持高精度。**Hua & Fang**（2023）[IEEE TIE] 设计了一种新颖的DRL鲁棒控制器，通过离线预训练与在线微调结合，在四旋翼轨迹跟踪任务中显著优于传统滑模控制。**Zhao 等**（2021）[IEEE TNNLS] 则利用DRL实现多欠驱动四旋翼的鲁棒编队控制，有效处理了模型失配问题。

### 4. 任务驱动的轨迹规划与资源分配

在应急救援等任务中，故障容错需与任务目标（如生存概率）协同优化。**王恩良等**（2025）[jeit.ac.cn](https://jeit.ac.cn/cn/article/doi/10.11999/JEIT250694) 提出**熵增强量子涟漪协同算法**（E²QRSA），以受困者生存概率最大化为目标，将生存概率随时间指数衰减的特性融入目标函数。在台风灾害场景中，E²QRSA规划的路径使平均生存概率达到0.847，比次优算法（SEWOA）提升4.3%，且成功规避所有动态障碍与禁飞区。**王侃等**（2025）[jeit.ac.cn](https://www.jeit.ac.cn/cn/article/doi/10.11999/JEIT241071) 综述了无人机辅助边缘计算中的轨迹与资源联合优化，指出离线-在线混合优化是处理能耗、时延与安全约束的有效范式。**王怡澄等**（2025）[hplpb.com.cn](https://www.hplpb.com.cn/cn/article/doi/10.11884/HPLPB202537.240340) 构建了包含偏差、漂移、锁死与缩放四类故障的模拟数据集，并用QCNN等网络验证了其完备性，为数据驱动的故障诊断提供了基准。

## 实验与评价总结

近三年研究的实验验证呈现出三大共性结论：（1）**复合故障场景**成为主流测试范式，单一故障（如仅执行器失效）已不足以验证方法的实用性；（2）**户外实物验证**逐步替代纯仿真，以评估算法在真实风扰、通信延迟与传感器噪声下的性能；（3）**性能指标多元化**，除传统的跟踪误差、收敛时间外，生存概率（应急场景）、能耗、安全裕度、计算实时性等成为关键评价维度。此外，消融实验（Ablation Study）被广泛用于量化各算法组件（如自适应律、引导策略）的贡献。

## 趋势与挑战

基于2025年前后已发表与在审工作，未来研究将聚焦以下方向：
1.  **数字孪生与混合学习**：构建高保真数字孪生体以生成海量故障数据，并与物理系统形成“预训练-在线微调”闭环，提升策略泛化能力（王侃等，2025）。
2.  **安全-弹性-能效协同**：在保障容错与性能的同时，将能量收集（如太阳能）、服务迁移与绿色计算纳入优化框架，解决无人机续航瓶颈（王侃等，2025）。
3.  **空-天-地一体化安全**：面向6G通感算一体网络，研究卫星辅助的跨域资源调度与物理层安全机制，以抵御针对空地链路的深度伪造与信号干扰攻击（王侃等，2025；陈谋等，2023）。

## 结论

2022–2025年，多无人机容错与性能约束控制研究已从单一故障处理迈向多维约束协同优化的新阶段。基于观测器与滑模的方法在理论严谨性上持续深化，而强化学习与任务驱动的规划方法则在应对复杂场景中展现出强大潜力。未来，融合数字孪生、跨域协同与主动安全防御的智能弹性控制架构，将成为支撑大规模无人机系统在高风险任务中可靠运行的关键。

## 参考文献

[1] 陈涛, 陈建. 基于学习观测器的无人机故障弹性容错控制. 航空学报, 2025, 46(11): 531346. [hkxb.buaa.edu.cn](https://hkxb.buaa.edu.cn/CN/10.7527/S1000-6893.2024.31346)

[2] 蔡运颂, 许璟, 牛玉刚. 基于自适应多尺度超螺旋算法的无人机集群姿态同步控制. 自动化学报, 2023, 49(8): 1656–1666. [aas.net.cn](https://www.aas.net.cn/cn/article/doi/10.16383/j.aas.c220759)

[3] 陈伟东, 李家伟, 梁传福. 基于神经网络的四旋翼无人机自适应非奇异快速终端滑模容错控制. 传感器技术与应用, 2024, 12(6): 839-852. [hanspub.org](https://www.hanspub.org/journal/paperinformation?paperid=101128)

[4] 王耀南, 华和安, 张辉, 等. 性能函数引导的无人机集群深度强化学习控制方法. 自动化学报, 2025, 51(5): 905–916. [aas.net.cn](https://www.aas.net.cn/cn/article/doi/10.16383/j.aas.c240519)

[5] 王恩良, 章祯, 孙知信. 复杂约束下应急救援无人机路径的熵增强量子涟漪协同算法. 电子与信息学报, 2025. doi: 10.11999/JEIT250694. [jeit.ac.cn](https://jeit.ac.cn/cn/article/doi/10.11999/JEIT250694)

[6] 王侃, 曹铁林, 李旭杰, 等. 无人机辅助边缘计算网络轨迹规划与资源分配研究综述. 电子与信息学报, 2025, 47(5): 1266-1281. [jeit.ac.cn](https://www.jeit.ac.cn/cn/article/doi/10.11999/JEIT241071)

[7] 王怡澄, 柴梦娟, 余道杰, 等. 无人机故障模拟数据集构建与评测方法. 强激光与粒子束, 2025, 37: 043006. [hplpb.com.cn](https://www.hplpb.com.cn/cn/article/doi/10.11884/HPLPB202537.240340)

[8] 陈谋, 马浩翔, 雍可南, 等. 无人机安全飞行控制综述. 机器人, 2023, 45(3): 345-366. [html.rhhz.net](https://html.rhhz.net/jqr/html/20230309.htm)

[9] Ma H J, Liu Y L, Li T B, et al. Nonlinear high-gain observer-based diagnosis and compensation for actuator and sensor faults in a quadrotor unmanned aerial vehicle. IEEE Transactions on Industrial Informatics, 2019, 15(1): 550-562.

[10] Gao B K, Liu Y J, Liu L. Adaptive neural fault-tolerant control of a quadrotor UAV via fast terminal sliding mode. Aerospace Science and Technology, 2022, 129: 107818.

[11] Hua H A, Fang Y C. A novel reinforcement learning-based robust control strategy for a quadrotor. IEEE Transactions on Industrial Electronics, 2023, 70(3): 2812–2821.

[12] Zhao W B, Liu H, Lewis F L. Robust formation control for cooperative underactuated quadrotors via reinforcement learning. IEEE Transactions on Neural Networks and Learning Systems, 2021, 32(10): 4577–4587.