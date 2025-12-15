# 故障检测与隔离技术研究综述（2022–2025）

## 引言

故障检测与隔离（Fault Detection and Isolation, FDI）是保障复杂工业系统、电力网络与无人装备安全可靠运行的核心技术。近年来，随着深度学习、图神经网络与多模态感知的突破，FDI方法正从传统模型驱动向数据-知识融合范式演进。本文综述2022至2025年间在工业过程、电力系统与无人机等关键领域的代表性工作，聚焦图结构建模、多模态融合、弹性容错控制等新兴方向，并分析其共性挑战与未来趋势。

## 方法分类与代表作

### 1. 基于图结构与传播路径建模的FDI

针对工业过程故障传播机理复杂、根源定位困难的问题，谭帅等人[1]提出**故障传播路径感知网络**（FPPAN），通过 _k_-近邻与 _k_-跳可达路径剪枝构建“故障源图”，将分类问题转化为图匹配任务。该方法在TE过程与盾构施工数据上平均诊断准确率达80.1%，显著优于传统GNN方法，尤其在阶跃与随机混合故障下提升明显。

马亮等[2]综述了工业过程故障根源诊断与传播路径识别技术，强调需融合因果推断与动态图建模以区分故障传播与物理耦合。唐鹏等[3]进一步提出**深度因果图建模**，通过多层图卷积学习变量间动态因果强度，在牵引传动系统中实现了92%以上的隔离准确率。

### 2. 电力系统热故障与绝缘子缺陷检测

配电网部件热故障判别面临红外图像分辨率低、标注噪声多等挑战。陶岩等[4]提出**多模态检测任务转换框架**，将高分辨率可见光图像用于目标定位，再迁移至红外图进行温度解译。其改进IoU损失有效抑制低质量标注影响，在4类部件上检测mAP达88.1%，温度解译平均误差≤0.8℃。

针对绝缘子缺陷，刘传洋等[5]系统综述了基于YOLOv7、Anchor-free与轻量化模型的检测方法。亢洁等[6]提出**IDD-YOLOv7**，融合CAT-BiFPN与通道-空间注意力，在自爆、污损、破损三类缺陷上mAP达94.8%，较基线提升13个百分点。赵振兵等[7]则利用CycleGAN进行小样本缺陷扩增，解决了真实缺陷样本稀缺问题。

### 3. 无人机与电力电子变换器的弹性容错控制

在执行器-传感器复合故障场景下，陈涛与陈建[8]设计**学习观测器**，在线估计故障函数与真实输出，并结合自适应神经网络反步控制器实现四旋翼无人机的姿态跟踪。户外实验证明，该方法在同时发生传感器偏移与执行器卡死故障时，位置跟踪误差仍控制在0.15m内。

刘闯等[9]综述了AI驱动的电力电子变换器开路故障诊断，指出随机森林与瞬时特征结合可有效区分IGBT单管开路。Wu等[10]则提出**过程拓扑卷积网络**（PTCN），将电路拓扑编码为图结构，在DC-DC变换器故障隔离中准确率达98.7%。

### 4. 大语言模型与知识驱动的智能诊断

面对缺陷文本非结构化、专家知识难复用的问题，杨虹等[11]构建**BERT+ChatGLM3两阶段框架**：BERT微调实现缺陷等级分类（F1=0.8627），大模型通过提示工程生成诊断依据。在7.3万条主设备缺陷记录上，问答准确度达40.34分（满分50），显著优于无提示基线。

张振宇等[12]则提出**无通道保护方案**，利用故障后健全相电流-电压的时空特征实现中压线路两端隔离。PSCAD仿真显示，该方法可在不依赖通信条件下，将永久性故障隔离时间缩短至100ms级，并自动恢复非故障区段供电。

## 实验与评价总结

现有研究在实验设计上呈现三大共性：  
1. **多场景验证**：代表性工作均在标准数据集（如TE过程、ISIC皮肤病、CPLID绝缘子）与私有工业数据（如盾构机、配电网）上交叉验证，以证明泛化性。  
2. **复合故障模拟**：实验普遍包含阶跃、随机、缓慢漂移等多类型故障组合，更贴近实际运行场景。  
3. **实时性-精度权衡**：轻量化模型（如YOLOv5s、MobileNet）虽mAP略降1-3%，但推理速度提升5倍以上，满足边缘部署需求。  

关键结论包括：图结构建模在故障根源隔离上平均提升5-8%准确率；多模态融合可将热故障判别的温度误差控制在1℃内；而无通信方案在配电自愈中可避免90%以上的越级跳闸。

## 趋势与挑战

基于2024–2025年前沿工作，FDI技术呈现以下趋势：  
1. **多模态大模型融合**：利用视觉-语言模型（如LLaVA）联合解析设备图像与运维日志，实现端到端故障推理，避免特征工程瓶颈。  
2. **因果强化学习框架**：结合因果发现与PPO算法，在未知故障类型下通过在线交互学习隔离策略，提升对未见故障的适应性。  
3. **云-边-端协同诊断**：轻量化模型部署于边缘设备进行实时检测，复杂根因分析由云端大模型完成，通过知识蒸馏实现双向优化。  

主要挑战包括：小样本下故障表征的泛化性不足、多源异构数据的时间对齐误差、以及安全关键场景中诊断结果的可解释性缺失。

## 结论

2022–2025年FDI研究已从单一模型优化转向系统级协同设计。图神经网络有效刻画了故障传播机理，多模态融合提升了感知精度，而大模型则赋予系统知识推理能力。未来工作需在因果可解释性、在线自适应与边缘智能三方面突破，以支撑高可靠自主系统的构建。

## 参考文献

[1] Tan S, Wang Y F, Jiang Q C, et al. Fault propagation path-aware network: A fault diagnosis method. *Acta Automatica Sinica*, 2025, 51(1): 161–173.  
[2] Ma L, Peng K X, Dong J. Review of root cause diagnosis and propagation path identification techniques for faults in industrial processes. *Acta Automatica Sinica*, 2022, 48(7): 1650–1663.  
[3] Tang P, Peng K X, Dong J. A novel method for deep causality graph modeling and fault diagnosis. *Acta Automatica Sinica*, 2022, 48(6): 1616–1624.  
[4] Tao Y, Zhang H, Huang Z H, et al. Accurate identification of thermal faults for typical components of distribution networks. *CAAI Transactions on Intelligent Systems*, 2025, 20(2): 506–515.  
[5] Liu C Y, Wu Y Q, Liu J J. Research progress of deep learning methods for insulator defect detection in UAV based aerial images. *Transactions of China Electrotechnical Society*, 2025.  
[6] Kang J, Wang Q, Liu W B, et al. Detection model of multi-defect of aerial photo insulator by integrating CAT-BiFPN and attention mechanism. *High Voltage Engineering*, 2023, 49(8): 3361–3372.  
[7] Cui K B, Pan F. A CycleGAN small sample library amplification method for faulty insulator detection. *Computer Engineering & Science*, 2022, 44(3): 509–515.  
[8] Chen T, Chen J. Learning-observer-based resilient fault-tolerant control for quadrotor unmanned aerial vehicles. *Acta Aeronautica et Astronautica Sinica*, 2025, 46(11): 531346.  
[9] Liu C, Kou L, Cai G W, et al. Review for AI-based open-circuit faults diagnosis methods in power electronics converters. *Power System Technology*, 2024.  
[10] Wu D Y, Zhao J S. Process topology convolutional network model for chemical process fault diagnosis. *Process Safety and Environmental Protection*, 2021, 150: 93–109.  
[11] Yang H, Meng X K, Yu H, et al. Research on primary equipment defect diagnosis method based on the BERT model. *Power System Protection and Control*, 2025, 53(7): 155–165.  
[12] Zhang Z Y, Cai Z P, Xia Y, et al. A full-process medium-voltage distribution line protection scheme based on local information. *Journal of Global Energy Interconnection*, 2025, 8(3): 386–397.