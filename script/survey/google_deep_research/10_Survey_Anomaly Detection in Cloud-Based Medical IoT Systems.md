云基医疗物联网系统中的异常检测：架构、算法与未来趋势（2022–2025）
1. 引言
1.1 医疗物联网的范式转变与安全危机
医疗物联网（Internet of Medical Things, IoMT）作为物联网技术在医疗保健领域的垂直应用，正在经历一场前所未有的数字化革命。通过将医疗设备、可穿戴传感器、植入式装置以及临床信息系统无缝连接，IoMT 构建了一个高度互联的生态系统，实现了从被动治疗向主动健康管理的范式转变 。这一变革使得实时患者监控、远程医疗诊断以及基于大数据的个性化治疗方案成为可能，显著提升了医疗服务的可及性与效率。然而，随着互联设备数量的指数级增长——预计到 2025 年全球将有数百亿台物联网设备在线，其中医疗设备占据了相当大的比例 ——这一生态系统正面临着严峻的安全挑战。   

IoMT 系统的核心特征在于其物理世界与数字世界的深度融合。胰岛素泵、心脏起搏器等关键设备不仅收集敏感的生理数据，还直接执行治疗操作。一旦这些设备遭受网络攻击或出现异常故障，后果将不再局限于数据泄露，而是直接威胁患者的生命安全 。2025 年的安全态势报告显示，针对医疗网络的攻击手段日益复杂化，漏洞普遍存在且呈升级态势，包括勒索软件、分布式拒绝服务（DDoS）攻击以及复杂的横向移动攻击 。攻击者利用 IoMT 设备固件更新滞后、默认密码未修改以及网络分段不足等弱点，试图窃取电子健康记录（EHR）或破坏医疗基础设施的正常运行。   

1.2 云基架构下的异常检测挑战
在现代 IoMT 架构中，云计算扮演着数据汇聚与处理的中枢角色。然而，这种集中式的架构在面对异常检测（Anomaly Detection, AD）任务时，面临着多重维度的技术挑战，这些挑战推动了 2022 年至 2025 年间学术界的研究热潮。

首先，数据的异构性与高维性是 IoMT 异常检测面临的首要难题。医疗数据来源广泛，涵盖了从网络层的流量日志（如 TCP/IP 包头信息）到应用层的生理信号（如心电图 ECG、脑电图 EEG、血糖水平）。这些数据不仅模态各异，而且具有极高的维度和复杂的时空依赖关系 。传统的基于规则或签名的检测方法难以捕捉这些高维数据中的细微异常模式，容易导致高误报率或漏报率。   

其次，实时性与延迟敏感性是医疗急救场景的硬性要求。在心脏骤停或设备被恶意控制的危急时刻，异常检测系统必须在毫秒级内做出响应并阻断威胁。然而，传统的云基异常检测方案往往涉及将海量原始数据上传至云端进行处理，这不仅消耗了大量的网络带宽，还会引入不可预测的传输延迟，难以满足实时控制的需求 。   

再者，资源受限性限制了复杂模型在边缘侧的部署。许多 IoMT 设备（如植入式传感器）受限于体积和电池寿命，其计算能力和存储空间极其有限。如何在资源受限的设备上部署能够抵御零日攻击（Zero-day Attacks）的高精度检测模型，是当前研究的重点之一 。   

最后，数据隐私与合规性构成了技术应用的法律边界。医疗数据受到 HIPAA（美国）、GDPR（欧盟）等法规的严格保护。传统的集中式训练模式要求将分散在各医院或患者手中的原始数据汇聚到中央服务器，这不仅增加了隐私泄露的风险，也面临着严重的合规性障碍，导致了“数据孤岛”现象的普遍存在 。   

1.3 报告范围与结构
本综述报告旨在全面梳理 2022 年至 2025 年间，针对云基医疗物联网系统异常检测的代表性学术成果。报告将深入探讨从架构演进到算法创新的全方位技术图谱，不仅关注单一的检测算法，更将视线投向整个系统的安全生态。

报告主体结构如下：

第 2 章：架构演进，分析从单一云中心向“云-边-端”协同架构的转变，以及基于微服务和雾计算的检测部署策略。

第 3 章：深度学习算法，详尽剖析 CNN-LSTM、Transformer、集成学习等核心算法在处理时空数据特征时的机制与优势。

第 4 章：隐私保护与联邦学习，探讨如何在数据不出域的前提下实现协同模型训练，以及差分隐私技术的应用。

第 5 章：零信任与安全框架，介绍零信任架构（ZTA）在医疗环境下的落地实践，包括动态信任评分与区块链辅助认证。

第 6 章：实验评估，总结主流数据集、评价指标以及各模型的性能对比。

第 7 章：未来趋势，展望生成式 AI、可解释性 AI（XAI）及 6G 技术对该领域的深远影响。

2. 云-边协同与微服务架构下的异常检测机制
随着云计算技术的成熟与边缘计算的兴起，IoMT 的异常检测架构正在经历从“云端集中处理”向“云-边协同处理”的深刻变革。这一转变旨在平衡计算资源、网络带宽与实时性需求，构建更加弹性且高效的安全防御体系。

2.1 基于微服务的云-边融合架构
为了应对传统单体架构在扩展性和维护性上的不足，2025 年的研究提出了一种基于微服务（Microservices）的新型云-边架构，专门用于实时医疗资产追踪与异常检测 。这种架构通过将复杂的检测系统拆解为一系列独立部署、松散耦合的微服务，极大地提升了系统的灵活性与鲁棒性。   

在该架构中，软件定义网络（SDN） 被引入作为流量调度的核心。SDN 控制器负责全局视角的流量监控与策略下发，能够根据实时检测结果动态重构网络流，隔离异常设备。而 KubeEdge 框架则充当了云端 Kubernetes 集群与边缘设备之间的桥梁，将容器化的分析服务无缝扩展至边缘节点。

具体而言，遥测收集器（Telemetry Collector）和安全执行代理（Security Enforcement Agent）被设计为 Kubernetes 的 DaemonSets，直接部署在连接医疗设备的边缘网关上。这种部署方式确保了每一个边缘节点都具备独立的监控与防御能力。例如，当监测到输液泵的流量异常时，边缘代理可以立即执行阻断策略，而无需等待云端的指令，从而实现了平均 35.2 毫秒的超低延迟响应 。此外，Open vSwitch (OVS) 与 Calico 网络的集成，使得系统能够在微服务级别实施精细化的流量控制，有效防止了攻击者利用单一微服务的漏洞进行横向移动。   

2.2 雾计算层：分层检测与资源调度
在云端与边缘端之间，雾计算（Fog Computing） 层被作为中间件引入，以进一步优化资源利用率并降低主干网络压力。雾节点通常由具有一定计算能力的路由器、交换机或专用服务器构成，它们在地理位置上更接近终端设备，能够承担部分数据预处理与初步检测任务。

在  所描述的雾-云架构中，异常检测被设计为一个分层级联的过程：   

初级过滤（雾层）：部署轻量级的异常检测模型（如浅层 LSTM 网络或决策树）。这些模型主要负责处理本地汇聚的实时数据流，快速识别明显的攻击特征或设备故障。由于雾节点具备一定的算力，它们可以对原始数据进行清洗、降维和特征提取，仅将疑似异常的数据或高层特征上传至云端。

全局分析（云层）：部署计算密集型的复杂模型（如深度集成学习模型）。云端系统接收来自多个雾节点的汇聚信息，利用其强大的算力和全局数据视图，进行关联分析和高级威胁狩猎。例如，单一雾节点可能无法察觉低频的分布式攻击（DDoS），但云端通过综合分析所有节点的流量模式，能够精准识别此类协同攻击 。   

这种分层策略不仅显著降低了云端的带宽消耗，还提高了系统的容错能力。即使云端连接中断，雾层仍能维持基本的安全防御功能，确保医疗服务的连续性。

2.3 TinyML：边缘智能的极致下沉
针对资源极度受限的 IoMT 终端设备（如可穿戴心电监测贴片、植入式传感器），TinyML（微型机器学习） 技术在 2024–2025 年间取得了突破性进展，使得在毫瓦级功耗的微控制器（MCU）上运行深度学习模型成为可能 。   

TinyML 的核心在于模型压缩与硬件协同优化。研究者们采用了以下关键技术：

模型剪枝（Pruning）：移除神经网络中对输出贡献较小的冗余权重连接，显著减少模型参数量。

量化（Quantization）：将模型权重从 32 位浮点数（FP32）转换为 8 位整数（INT8）甚至更低精度。这不仅减少了模型存储空间，还大幅降低了推理时的内存占用和计算能耗。

知识蒸馏（Knowledge Distillation）：利用庞大的“教师模型”指导轻量级的“学生模型”训练，使小模型能够模仿大模型的行为，保留核心检测能力。

在  的研究中，优化后的 CNN 模型被部署在 Raspberry Pi 和 Arduino Nano 等边缘设备上，用于实时心电图（ECG）异常检测。实验结果显示，该模型在保持 92.3% 高准确率的同时，将功耗降低至惊人的 0.024 mW。这意味着医疗可穿戴设备可以在不依赖频繁充电的情况下，实现全天候的本地异常监测。一旦检测到心律失常等危急情况，设备可立即通过蓝牙唤醒智能手机报警，极大缩短了急救响应时间。   

3. 核心算法演进：从机器学习到混合深度学习
2022 至 2025 年间，IoMT 异常检测的算法重心已从传统的机器学习（如 SVM、随机森林）全面转向深度学习（DL）及其混合变体。这一转变的根本驱动力在于 IoMT 数据日益增长的复杂性：传统算法依赖人工设计的特征工程，难以应对高维、非线性且动态变化的网络流量与生理信号数据。深度学习通过自动特征提取（Representation Learning），展现出了卓越的检测性能。

3.1 混合深度学习模型：时空特征的深度融合
单一的深度学习模型往往存在局限性：卷积神经网络（CNN）擅长提取空间特征，但难以捕捉长距离的时间依赖；循环神经网络（RNN/LSTM）擅长处理时序数据，但在高维空间特征提取上效率较低。因此，将二者结合的混合架构成为了当前研究的主流选择。

3.1.1 RCLNet：CNN-LSTM 与自适应注意力的协同
RCLNet 是 2024 年提出的一个专为 IoMT 环境设计的代表性异常入侵检测系统（A-IDS）。该模型通过精巧的架构设计，系统性地解决了 IoMT 数据的时空建模难题。   

空间特征提取（CNN 层）：RCLNet 首先利用一维或二维卷积层处理输入的原始数据流。在 IoMT 网络流量中，数据包的头部信息、载荷特征等被组织成矩阵形式，CNN 通过滑动卷积核识别出局部的攻击模式（如特定的字节序列或流量突发形态）。

时序依赖捕捉（LSTM 层）：CNN 提取的特征向量序列随后被送入 LSTM 层。LSTM 通过其内部的门控机制（遗忘门、输入门、输出门），能够有效记忆长期的历史状态，从而识别出跨越多个时间步的复杂攻击行为（如慢速扫描或渐进式拒绝服务攻击）。

自适应注意力层机制（SAALM）：这是 RCLNet 的点睛之笔。在传统的 CNN-LSTM 结构中，所有时间步的输出通常被同等对待。然而，在实际攻击中，异常往往只集中在极短的时间窗口内。SAALM 机制通过计算每个时间步的注意力权重，动态地放大关键时刻的特征信号，抑制背景噪声。这使得模型能够像人类专家一样，“聚焦”于最可疑的数据片段 。   

损失函数优化（Focal Loss）：针对 IoMT 数据集中严重的类别不平衡问题（正常流量远多于攻击流量），RCLNet 摒弃了传统的交叉熵损失，转而采用 Focal Loss。Focal Loss 通过引入调节因子，降低了易分类样本（大量正常样本）的权重，迫使模型在训练过程中更加关注那些难以分类的少数类样本（攻击样本），从而显著提升了检出率（Recall）。   

3.1.2 GRU 与注意力机制的高效变体
虽然 LSTM 性能强大，但其复杂的门控结构带来了较高的计算开销。为了适应资源受限的医疗设备，2025 年的一项研究提出了基于 GRU（门控循环单元） 与注意力机制的混合模型 。   

GRU 作为 LSTM 的简化变体，将遗忘门和输入门合并为更新门，参数量减少了约 1/3，但仍保留了捕捉长时序依赖的能力。该研究结合了 PCA（主成分分析） 进行特征降维，以及 SMOTE（合成少数类过采样技术） 处理数据不平衡。实验表明，该模型在 ICU Healthcare 数据集上达到了 99.99% 的准确率，且在推理速度上优于 LSTM 模型，证明了其在实时检测零日攻击（Zero-day Attacks）方面的巨大潜力 。   

3.2 Transformer 架构的崛起
随着自然语言处理领域的突破，Transformer 架构凭借其强大的全局注意力机制，开始在 IoMT 异常检测领域崭露头角 。   

图卷积与 Transformer 的融合：IoMT 设备并非孤立存在，而是形成了一个复杂的拓扑网络。2025 年的一项研究  提出了一种结合 图卷积网络（GCN） 和 Transformer 的混合模型。GCN 用于捕捉设备间的空间连接关系（即谁与谁通信），而 Transformer 则负责建模每条通信链路上的时序模式。这种“图-时序”融合的方法在 CICIOMT24 数据集上表现优异，特别是在检测针对特定设备群的协同攻击（如僵尸网络传播）方面具有独特优势。   

基于流重构的自监督学习：另一项创新应用是利用 Transformer 进行 流重构（Flow Reconstruction） 。该方法采用自监督学习范式，训练 Transformer 模型学习正常网络流量的分布规律，并尝试“重构”输入序列。当遇到恶意流量时，由于其分布与正常流量差异巨大，模型的重构误差（Reconstruction Error）会急剧上升，从而触发警报。这种方法的巨大优势在于它不需要预先标记攻击样本，因此对未知的新型攻击具有天然的泛化检测能力。   

3.3 集成学习（Ensemble Learning）与 Stacking 策略
为了克服单一模型的偏差，集成学习通过组合多个基学习器来构建更强大的检测系统。

Stacking 架构：在  中，研究者设计了一种多层 Stacking 模型。该模型选取 随机森林（Random Forest） 和 人工神经网络（ANN） 作为第一层的基学习器，利用随机森林处理高维离散特征的优势和 ANN 拟合非线性关系的能力。   

元学习器（Meta-learner）：第二层采用 XGBoost 作为元学习器，对基学习器的预测结果进行再次学习和融合。XGBoost 强大的梯度提升算法能够有效纠正基学习器的偏差。实验证明，这种组合策略在 UNSW-NB15 和医疗专用数据集上均取得了优于单一模型的准确率、精确率和召回率，尤其是在降低误报率方面效果显著。

4. 隐私保护下的分布式智能：联邦学习
在医疗领域，数据隐私是不可逾越的红线。传统的集中式深度学习需要将分散在各医院、诊所甚至患者家庭的原始数据上传至云端服务器进行训练。这种模式不仅面临巨大的隐私泄露风险，还受到 HIPAA、GDPR 等法律法规的严格限制。联邦学习（Federated Learning, FL） 作为一种“数据不动模型动”的分布式机器学习范式，在 2023–2025 年间成为了 IoMT 安全研究的核心热点 。   

4.1 联邦学习的基本范式与优势
在 FL 框架下，每个参与方（客户端，如智能医院的边缘网关）利用本地的私有数据训练一个局部的异常检测模型。训练完成后，客户端仅将模型参数（如权重和梯度的更新量）上传至中央聚合服务器。服务器利用 FedAvg 等算法对所有客户端的参数进行加权聚合，生成一个新的全局模型，并将其下发回客户端。这一过程循环往复，直至模型收敛。

这种机制的核心优势在于：原始医疗数据从未离开过本地设备。这不仅从根本上降低了数据泄露的风险，还解决了跨机构数据共享的合规性难题，打破了“数据孤岛”。

4.2 AutoKAN：轻量级联邦框架的创新
针对 IoMT 设备资源受限的特点，2025 年提出的 AutoKAN 框架代表了联邦学习算法层面的最新进展 。   

AutoKAN 巧妙地结合了 Kolmogorov-Arnold Networks (KAN) 与联邦学习。KAN 是一种基于柯尔莫哥洛夫-阿诺德表示定理的新型神经网络结构，与传统的多层感知机（MLP）相比，KAN 在处理复杂的非线性函数逼近时具有更高的参数效率和可解释性。

轻量化设计：AutoKAN 利用 KAN 的特性，使得本地模型的参数量大幅减少，从而降低了联邦学习中最昂贵的通信开销（模型参数传输）。

应用场景：该框架被专门应用于糖尿病监测系统。患者的血糖数据属于高度敏感信息，AutoKAN 确保了这些数据仅在患者的个人设备上进行处理，同时通过全局聚合，让每个患者的设备都能获得基于群体智慧训练出的高精度异常检测模型，有效识别传感器故障或恶意篡改。

4.3 隐私增强技术：对抗梯度泄露
尽管联邦学习避免了原始数据交换，但研究表明，攻击者仍可能通过分析上传的梯度信息反推原始数据特征（即梯度泄露攻击）。为了封堵这一漏洞，研究者们在 FL 框架中引入了额外的隐私增强技术：

自适应差分隐私（AFL-CDP）： 提出了一种结合了 集中差分隐私（Concentrated Differential Privacy, CDP） 的自适应联邦学习框架。该方法在客户端上传梯度之前，向梯度向量中注入精心设计的统计噪声（如高斯噪声）。噪声的引入掩盖了单个数据点对模型更新的贡献，使得攻击者无法从梯度中还原出特定患者的信息。更重要的是，该框架设计了自适应机制，能够根据训练阶段动态调整噪声的强度，在保护隐私的同时，最大限度地减少噪声对模型准确性的负面影响。   

SPECK 加密算法：为了进一步保障通信安全，该研究还集成了 SPECK 轻量级分组密码算法。SPECK 专为资源受限的物联网设备设计，具有极高的软硬件实现效率。它被用于对传输中的模型参数进行加密，防止中间人攻击（Man-in-the-Middle Attacks）窃取或篡改模型更新 。   

4.4 智能家居 IoMT 的分层联邦安全
在智能家居环境下的医疗监控场景中，设备种类繁多（如智能摄像头、运动传感器、健康监测仪），网络环境复杂。一种基于 FL 的智能安全方案被提出 。   

模型架构：该方案采用了 AutoEncoder（自动编码器） 进行数据降维和特征提取，结合 LSTM 进行时序异常检测。

分层聚合：系统在家庭网关处设立了第一级聚合点，先在家庭内部进行局部模型聚合，然后再参与云端的全局联邦训练。

性能收益：实验结果显示，这种分层 FL 架构将通信开销降低了 35%，并将检测延迟控制在 180ms 以内。这对于需要实时响应跌倒检测或非法入侵的家庭护理场景至关重要。

5. 零信任架构与动态访问控制
随着 IoMT 边界的日益模糊，传统的“边界防御”（Perimeter-based Security）已无法应对内部威胁和凭证窃取攻击。零信任架构（Zero Trust Architecture, ZTA） 作为一种“永不信任，始终验证”的安全范式，正在重塑云基 IoMT 的安全体系 。   

5.1 ZTCloudGuard：上下文感知的信任评估体系
2024 年发表的 ZTCloudGuard 框架是零信任原则在医疗云环境下的典型落地实践 。该框架超越了传统的静态身份验证，提出了一种基于上下文感知的动态信任评估机制。   

ZTCloudGuard 的核心在于其双重信任评分体系：

关键信任（Critical Trust, CT）：这是信任的基础层，基于云原生微服务的硬性安全指标计算得出。系统实时检查用户的认证状态、加密协议强度、日志完整性以及授权级别。如果 CT 分数低于阈值（例如检测到未加密的连接或异常的登录位置），访问请求将被直接拒绝。

纽带信任（Bond Trust, BT）：这是信任的高级层，侧重于行为和内容的语义分析。

语义分析 (BT 
A
​
 )：利用预训练的 Word2Vec 模型，分析访问主体（用户）、客体（数据）与环境（设备）之间的语义关联。例如，如果一名“放射科医生”试图访问大量的“精神科处方记录”，虽然其拥有合法的登录凭证，但语义关联度低，系统会判定为异常行为。

句法分析 (BT 
B
​
 )：针对生成式 AI 辅助撰写的医疗报告，系统引入了类似 IBM BLEU 分数的句法分析机制，评估生成内容的句法完整性和逻辑一致性，防止 AI 幻觉或恶意数据注入导致的医疗错误。

实验结果表明，ZTCloudGuard 在检测医疗错误和异常访问方面达到了 93.5% 的 F1 分数，有效弥补了传统 RBAC（基于角色的访问控制）在应对内部威胁时的不足。

5.2 SHACS：基于行为分析的动态访问控制
针对电子健康记录（EHR）的高频访问需求，SHACS（Secure Healthcare Access Control System） 提出了一种集成实时异常检测的动态访问控制方案 。   

SHACS 的创新之处在于将异常检测模型直接嵌入到访问控制流程中。系统利用 MIMIC-III 数据集训练的机器学习模型，建立用户正常访问行为的基线（Baseline）。这些行为特征可能包括访问时间、访问频率、查看的记录类型序列等。

实时阻断：当用户的访问行为偏离基线（例如，在非工作时间高频下载大量病历），系统会立即触发异常警报并动态撤销访问权限。

效率优化：除了安全性，SHACS 还显著提升了系统效率。通过动态调整认证策略（对于低风险行为简化认证流程），实验显示 SHACS 将平均认证时间从 40 秒降低至 28 秒，访问延迟降低了 25%，证明了高安全性与高可用性可以兼得。

5.3 区块链辅助的去中心化信任
为了解决 ZTA 中中心化策略决策点（PDP）可能成为单点故障的问题，区块链技术被引入以构建去中心化的信任根 。   

不可篡改的审计日志：区块链的分布式账本技术被用于记录所有的访问请求、信任评分计算过程及授权决策。这为事后的安全审计和取证提供了不可篡改的证据链。

分布式身份认证（DID）：通过区块链管理的去中心化身份，设备和用户可以在不依赖单一身份提供商（IdP）的情况下完成相互认证，增强了系统在部分网络瘫痪情况下的生存能力。

6. 实验数据集、评估指标与性能分析
严谨的科研综述离不开对实验数据的定量分析。2022–2025 年间，IoMT 异常检测的研究主要依赖于几个关键的基准数据集，这些数据集涵盖了网络流量、生理信号及临床记录等多模态数据。

6.1 主流数据集特征分析
表 1 总结了该领域最常用的实验数据集及其特征。

表 1：IoMT 异常检测主流数据集分析

数据集名称	数据类型	特点与应用场景	关键研究引用
WUSTL-EHMS-2020	网络流 + 生理特征	专为 IoMT 设计，包含了真实的医疗传感器数据（如 ECG 频率）及模拟的网络攻击（如欺骗、中间人攻击）。不仅记录了网络包头，还记录了攻击对生物计量数据的影响。	
MIMIC-III	临床时序数据	包含数万名 ICU 患者的生命体征、实验室检查、处方记录等。主要用于训练针对 EHR 访问异常及患者病情恶化的检测模型。	
TON_IoT / NF-TON-IoT	综合 IoT 遥测	涵盖多种 IoT 设备层（包含医疗、工业等）的遥测数据。包含 DDoS、勒索软件、后门等多种现代攻击类型，数据量大，特征维度高。	
MIT-BIH Arrhythmia	生理信号 (ECG)	经典的心电图数据库，包含带标注的心律失常样本。是验证边缘 AI 生理异常检测算法的标准测试集。	
CICIOMT24	综合 IoMT	2024 年发布的新型数据集，模拟了 40+ 种异构医疗设备和 18 种复杂的网络攻击，旨在填补旧数据集在现代攻击场景覆盖上的空白。	
  
6.2 性能对比与关键发现
通过对文献中实验结果的横向对比，我们可以得出以下关于算法性能的关键结论。

1. 损失函数对不平衡数据的影响至关重要 在 WUSTL-EHMS-2020 数据集上，使用 Focal Loss 的 RCLNet 模型准确率达到了 99.78%，而使用传统交叉熵损失（Cross-Entropy）的同构模型准确率仅为 97.04% 。这一显著差异表明，在异常样本稀缺的 IoMT 环境中，解决类别不平衡问题是提升检测性能的关键路径。Focal Loss 成功地迫使模型“关注”那些难以分类的少数攻击样本。   

2. 混合模型在零日攻击检测上表现更优 针对 TON_IoT 数据集，基于 GRU + Attention 的混合模型展现出了 99.99% 的极高准确率 。相比于单一的 CNN 或 LSTM 模型，混合模型能够同时捕捉流量的空间指纹和时间序列上的微小扰动。注意力机制的引入，使得模型能够识别出未知攻击（零日攻击）中偏离正常模式的细微特征，体现了强大的泛化能力。   

3. 边缘 AI 的精度与效率权衡 在 MIT-BIH 心律失常数据集上，经过剪枝和量化优化的 TinyML CNN 模型实现了 92.3% 的准确率 。虽然这一数值略低于云端大模型的性能（通常 >98%），但在实际应用中，它实现了 0.024 mW 的超低功耗和毫秒级的本地推理。这种权衡对于电池供电的可穿戴设备而言是完全可以接受且必要的，它证明了边缘智能在实时预警方面的实用价值。   

6.3 评估指标的多样化趋势
除了传统的 准确率（Accuracy）、精确率（Precision）、召回率（Recall） 和 F1-Score，近年来的研究开始更加关注系统级的性能指标：

推理延迟（Inference Latency）： 强调了 35.2ms 的平均延迟对于实时阻断的重要性。   

功耗（Power Consumption）： 将 mW 级的功耗作为衡量边缘模型优劣的核心指标。   

通信开销（Communication Overhead）：在联邦学习研究中，模型参数传输的数据量成为了评估算法效率的关键 。   

7. 挑战、新兴趋势与未来展望
尽管当前技术在架构和算法上取得了显著进展，但云基 IoMT 系统的异常检测仍面临严峻挑战。技术的演进方向正朝着更加智能、透明和高效的未来迈进。

7.1 可解释性 AI（XAI）：打破黑盒信任危机
深度学习模型虽然精度高，但其“黑盒”性质在医疗领域是致命的弱点。医生和安全分析师不仅需要系统告知“检测到异常”，更需要知道“为什么是异常”。

现状与挑战：目前的模型往往给出一个概率分数，缺乏病理或攻击逻辑的解释。这导致误报发生时，人工排查极其困难。

技术演进：2024–2025 年的研究开始集成 XAI 技术。Anchor 和 RuleFit 等基于规则的 XAI 方法被用于解释 IoT 异常检测结果，将复杂的神经网络决策转化为人类可读的“如果-那么”规则 。另一项研究利用 SHAP (SHapley Additive exPlanations) 值来量化每个输入特征（如某个数据包头字段或某段 ECG 波形）对最终分类结果的贡献度 。   

未来展望：未来的 IoMT 异常检测系统将标配 XAI 模块，能够提供可视化的攻击路径图谱或生理异常的特征归因，从而增强人机互信（Human-AI Trust）。

7.2 生成式 AI 与大语言模型（LLM）的深度融合
生成式 AI（Generative AI） 正在从单纯的内容生成工具转变为异常检测的强大引擎 。   

数据增强：GANs（生成对抗网络） 被广泛用于生成合成的攻击样本或罕见的病理数据，有效解决了训练数据稀缺和不平衡的问题 。   

故障诊断与响应：多模态大语言模型（Multimodal LLMs） 展现出了在故障诊断方面的巨大潜力。在工业 4.0 的平行研究中，LLM 已被用于分析设备日志并生成维修建议 。在 IoMT 领域，华硕等厂商已开始利用生成式 AI 辅助医生进行实时异常检测和决策支持 。未来，LLM 将充当安全分析师的智能助手，自动撰写安全事件报告并推荐应急响应策略。   

7.3 对抗性攻击与鲁棒性防御
随着 AI 防御系统的普及，攻防对抗也在升级。攻击者开始利用 AI 生成 对抗样本（Adversarial Examples）——通过在原始数据中添加人眼不可察觉的微小扰动，诱导深度学习模型做出错误判断 。   

防御策略：未来的研究将不得不将 对抗性训练（Adversarial Training） 纳入标准流程，即在训练阶段主动引入对抗样本，提高模型对扰动的鲁棒性。同时，基于去噪自动编码器的数据清洗机制也将成为防御对抗攻击的第一道防线。

7.4 6G 通信与万物智联（IoIT）
随着 6G 通信技术的研发启动，IoMT 将逐步演进为 万物智联（Internet of Intelligent Things, IoIT）。

技术红利：6G 承诺的太赫兹频段通信将带来微秒级的超低延迟和 Tbps 级的超高带宽。这将彻底消除云-边协同中的网络瓶颈，使得极其复杂的全息医疗影像传输和远程精细手术成为可能。

安全新范式：在 6G 时代，基于区块链的去中心化认证和网状网络（Mesh Network）安全将成为标配。异常检测将不再局限于单点或单链路，而是基于全网感知的分布式智能，实现“攻击即阻断”的免疫系统式防御 。   

8. 结论
2022 年至 2025 年间，云基医疗物联网系统的异常检测技术经历了深刻的变革。从架构上看，云-边-端协同已成为行业标准，通过 TinyML 实现边缘实时检测与云端全局分析的有机结合，有效解决了实时性与资源限制的矛盾。从算法上看，混合深度学习模型（如 RCLNet、GRU-Attention）通过融合 CNN 的空间提取能力与 LSTM/Transformer 的时序建模能力，设立了 99% 以上的精度新基准。

在安全与隐私方面，联邦学习与零信任架构的结合，成功在打破数据孤岛的同时构建了动态的信任防线，解决了医疗数据共享与合规的痛点。展望未来，随着 生成式 AI 的赋能与 XAI 的普及，IoMT 异常检测系统将不仅更加精准，而且更加透明、智能，能够抵御日益复杂的对抗性威胁。构建一个自适应、可解释且隐私原生的安全生态系统，将是保障全球数十亿 IoMT 设备及患者安全的关键所在。

表格索引
表 2：2022-2025 年代表性 IoMT 异常检测模型综合对比

模型架构	核心技术组件	适用场景	实验数据集	准确率 (Accuracy)	核心优势	潜在局限	来源文献
RCLNet	CNN + LSTM + SAALM + Focal Loss	云端网络入侵检测	WUSTL-EHMS-2020	99.78%	解决样本不平衡，时空特征提取能力极强	计算复杂度较高，需 GPU 加速，不适合边缘侧	
GRU-Attention	GRU + Attention + PCA	实时流量异常检测	ICU Healthcare	99.99%	参数量少于 LSTM，推理速度快，抗噪性强	依赖大量的预处理 (PCA, SMOTE)，特征工程复杂	
AutoKAN	KAN + 联邦学习	隐私敏感型监测 (如血糖)	私有/模拟数据	High (优于传统 FL)	极低的通信开销，保护数据隐私，可解释性好	KAN 网络训练稳定性尚需大规模验证	
TinyML CNN	Pruned CNN + STFT + Quantization	边缘端生理信号监测 (ECG)	MIT-BIH Arrhythmia	92.3% - 99%	毫秒级延迟，mW 级功耗，离线可用	模型容量受限，难以处理极长序列的复杂模式	
SHACS	AD + 动态访问控制	云端 EHR 访问安全	MIMIC-III	N/A (关注认证效率)	降低认证时间 30%，减少访问延迟 25%	高度依赖云端架构，对断网环境适应性差	
GCN-Transformer	GCN + Transformer	设备群协同攻击检测	CICIOMT24	优于基线	能够捕捉设备间的拓扑关系，检测僵尸网络	训练资源消耗极大，模型部署困难	
  

ieeexplore.ieee.org
Real-Time Anomaly Detection in IoMT Networks Using Stacking Model and a Healthcare- Specific Dataset - IEEE Xplore
在新窗口中打开

medium.com
Securing IoT Devices with Zero Trust Architecture: An Exhaustive Guide | by Okan Yıldız
在新窗口中打开

deepstrike.io
IoMT Vulnerabilities Statistics 2025: 99% of Hospitals Exposed - DeepStrike
在新窗口中打开

pmc.ncbi.nlm.nih.gov
A Systematic Literature Review on the Implementation and Challenges of Zero Trust Architecture Across Domains - PubMed Central
在新窗口中打开

frontiersin.org
RCLNet: an effective anomaly-based intrusion detection ... - Frontiers
在新窗口中打开

ieeexplore.ieee.org
A Cloud-Edge Microservices Architecture for Smart Healthcare: SDN-Based Medical Asset Management - IEEE Xplore
在新窗口中打开

pmc.ncbi.nlm.nih.gov
Reliable ECG Anomaly Detection on Edge Devices for Internet of ...
在新窗口中打开

mdpi.com
Multimodal Large Language Model-Based Fault Detection and Diagnosis in Context of Industry 4.0 - MDPI
在新窗口中打开

semanticscholar.org
[PDF] Federated Learning in Real-Time Medical IoT: Optimizing ...
在新窗口中打开

ieeexplore.ieee.org
A Federated Learning Model for Detecting Cyberattacks in Internet of Medical Things Networks - IEEE Xplore
在新窗口中打开

mdpi.com
Reliable ECG Anomaly Detection on Edge Devices for Internet of Medical Things Applications - MDPI
在新窗口中打开

pmc.ncbi.nlm.nih.gov
RCLNet: an effective anomaly-based intrusion detection for securing the IoMT system - PMC
在新窗口中打开

researchgate.net
(PDF) Intrusion Detection System for Internet of Medical Things ...
在新窗口中打开

mdpi.com
A Novel Internet of Medical Things Hybrid Model for Cybersecurity Anomaly Detection
在新窗口中打开

computer.org
Transformer-Based Intrusion Detection for Securing Medical ...
在新窗口中打开

ieeexplore.ieee.org
Privacy-Preserving Federated Learning for Intrusion Detection in IoT Environments: A Survey - IEEE Xplore
在新窗口中打开

researchgate.net
(PDF) AutoKAN: A Federated Lightweight Anomaly Detection Framework for Securing Constrained IoT Healthcare Diabetes Monitoring Systems - ResearchGate
在新窗口中打开

ieeexplore.ieee.org
AutoKAN: A Federated Lightweight Anomaly Detection Framework for Securing Constrained IoT Healthcare Diabetes Monitoring Systems - IEEE Xplore
在新窗口中打开

ieeexplore.ieee.org
A Smart and Secured Anomaly Detection Scheme for Internet of ...
在新窗口中打开

standards.ieee.org
Zero Trust Cybersecurity for Health Technology Tools, Services, and Devices | IEEE Standards Association
在新窗口中打开

mdpi.com
ZTCloudGuard: Zero Trust Context-Aware Access Management ...
在新窗口中打开

ieeexplore.ieee.org
Secure Healthcare Access Control System (SHACS) for Anomaly Detection and Enhanced Security in Cloud-Based Healthcare Applications - IEEE Xplore
在新窗口中打开

ieeexplore.ieee.org
Secure Healthcare Access Control System (SHACS) for Anomaly ...
在新窗口中打开

ieeexplore.ieee.org
A Zero-Trust Authentication Scheme With Access Control for 6G-Enabled IoT Environments - IEEE Xplore
在新窗口中打开

mdpi.com
Enhancing the Internet of Medical Things (IoMT) Security with Meta-Learning: A Performance-Driven Approach for Ensemble Intrusion Detection Systems - MDPI
在新窗口中打开

pmc.ncbi.nlm.nih.gov
Healthcare 5.0-Driven Clinical Intelligence: The Learn-Predict-Monitor-Detect-Correct Framework for Systematic Artificial Intelligence Integration in Critical Care - PMC - PubMed Central
在新窗口中打开

researchgate.net
Real-time Monitoring and Anomaly Detection in Cloud-based IoT Networks - ResearchGate
在新窗口中打开

pmc.ncbi.nlm.nih.gov
Advances in machine and deep learning for ECG beat classification: a systematic review
在新窗口中打开

researchgate.net
(PDF) Deep Learning for ECG Anomaly Detection: A Robust Real ...
在新窗口中打开

ieeexplore.ieee.org
A Systematic Evaluation Framework of Rule-Based XAI Methods for Anomaly Detection in IoT Systems - IEEE Xplore
在新窗口中打开

ieeexplore.ieee.org
An XAI-Enhanced Hybrid Deep Learning Framework for IoT Device Identification and Attack Detection - IEEE Xplore
在新窗口中打开

researchgate.net
generative ai techniques for anomaly detection in iot devices - ResearchGate
在新窗口中打开

frontiersin.org
Integrating generative adversarial networks with IoT for adaptive AI-powered personalized elderly care in smart homes - Frontiers
在新窗口中打开

asus.com
ASUS Unveils Breakthrough Healthcare AI Innovations During Computex 2025 | News
在新窗口中打开

irjms.com
Deep Learning for Anomaly Detection in IoT Healthcare Systems - International Research Journal of Multidis