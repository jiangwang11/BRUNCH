引言  
随着可穿戴/床旁设备、远程生命体征采集与云端电子病历/模型服务的融合，云-医疗物联网（cloud-based medical IoT）系统在把海量时序生理与设备元数据送入云端训练与推理的同时，面临着异常检测（性能异常、设备故障、隐私泄露与医学假阳性/假阴性）上的多重挑战：数据分布异构且高度不平衡、敏感数据无法集中、事件稀少但风险严重、以及临床可解释性要求高。为回应这些问题，近三年（2022–2025）学术界涌现出以联邦/隐私保护学习、时空分解与生成式建模、少样本/度量学习与自适应抽样，以及基于行为规范的混合方法为主的研究思路。下文在严格以公开文献为依据的前提下，按方法类别筛选代表性工作（每类不超5篇），逐篇概述其研究目标、核心方法与关键实验结论，并在实验与评价节中归纳共性结论与评价陷阱，最后给出面向 2025 年前后的可验证发展趋势与挑战预测。

方法分类与代表作（每篇 4–6 句，突出问题—方法—实证结论）

A. 联邦学习 / 隐私保护分布式检测（面向医疗数据隐私与跨院协同）  
- 张月等，GB‑AEnet‑FL：面向物联网设备异常检测，提出对抗性双编码器自编码网络并嵌入联邦学习（GB‑AEnet‑FL），解决异常样本稀少与数据异构的问题。方法通过异常样本重构扩充、潜在特征层的对抗训练与一致/收缩约束提升表征鲁棒性，并用动态模型选择减少通信与提升聚合效率。作者在四个不同数据集上对比显示，与传统方法相比检测准确率与跨域泛化能力都有提升，表明联邦范式可在不汇聚原始数据下改进设备级异常检测。[arocmag.cn](https://www.arocmag.cn/abs/2022.03.0142)  
- Wang 等，FL‑CNN‑LSTM（ZJU 2025）：针对网络入侵/流量异常检测提出联邦学习框架下的时空特征并联提取（CNN 并联 LSTM）并结合多头注意力以识别关键流量特征。研究问题是保护数据隐私同时保持跨站点检测性能；方法在每个客户端本地训练并通过加权聚合更新全局模型。实验在 CIC‑IDS2018/NSL‑KDD/UNSW‑NB15 上给出近集中式相当的准确率（例如 CIC‑IDS2018≈99%），并验证并联结构与注意力对提升跨域性能的贡献。[zjujournals.com](https://www.zjujournals.com/eng/article/2025/1008-973X/20250611.shtml)  
- Nguyen 等，DÏoT（联邦自学习 IoT 异常检测，ICDCS 2019，作为联邦思路先导）：提出联邦自学习管线用于分布式 IoT 异常检测，研究问题为异构设备在多域下的自适应模型构建。方法采用设备级自学习行为模型并在联邦框架下共享模型更新以实现跨域告警共享；实验表明联邦自学习能在保留本地数据隐私的前提下提高对已知/未知攻击的检出率（此工作为后续医疗场景联邦方法的奠基）。（参见综述引用）[jos.org.cn (综述引用)](https://jos.org.cn/html/2024/1/6818.htm)

B. 生成式 / 对抗学习与时空分解（提高在云端对多维生理时间序列的异常灵敏度）  
- Tang 等，MCBiWGAN‑GTN（JEIT 2024）：针对云服务器/多维时序异常提出将双向 Wasserstein GAN 与图‑时序网络（GTN：GCN+TCN）结合的 BiWGAN‑GTN，并在此基础上构建多通道 MCBiWGAN‑GTN。研究问题是同时提取时序与空间（指标间）依赖并降低训练中异常数据污染的风险；方法先用 CEEMDAN 分解时序，再将分量送入对应通道的 BiWGAN‑GTN（含半监督模块）训练。实验证明在真实云数据集（Clearwater、MBD）上 MCBiWGAN‑GTN 在 precision/recall/F1 上分别优于 MADGAN、MTAD‑GAT 等对比方法（Clearwater F1=0.960），表明时空模块与分解策略能显著提升多维时序异常检测的整体性能与稳定性。[jeit.ac.cn](https://jeit.ac.cn/cn/article/doi/10.11999/JEIT230679?viewType=HTML)  
- Li 等（arXiv 2018 / MAD‑GAN 系列）：提出用生成对抗网络建模多变量时间序列的生成—重构行为以区分异常，研究问题在于如何在无强监督下学习联合分布并据此判别异常。核心思想是用生成器与判别器的博弈学习时序分布并基于重构/判别损失产生异常分数；多项实验（公开时序基线）显示 GAN‑based 方法在检测复杂协变量异常时比简单预测/重构模型更能捕获跨变量异常模式（但对训练稳定性敏感）。[arxiv.org](https://arxiv.org/abs/1809.04758)  
- Gulrajani 等（WGAN‑GP，NeurIPS 2017，方法支撑文献）：提出 Wasserstein GAN 的梯度惩罚改进以稳定对抗训练，是后续 BiWGAN‑GP 与 BiWGAN‑GTN 等架构在医学/云时序异常检测中较多被引用的训练稳定化技术，对生成式异常检测在临床时间序列上的可训练性具有基础性影响。[arxiv.org](https://arxiv.org/abs/1704.00028)

C. 无监督表示学习、少样本/自适应抽样与度量学习（应对医疗异常的稀缺标签与类别不平衡）  
- 尹梓诺等，KAFS + SMLP（JEIT 2025）：针对类别极度不平衡的网络流量异常检测提出 K‑medoids 自适应小样本抽样（KAFS）与带鲁棒损失的孪生多层感知机（SMLP）。研究问题为如何在少样本条件下构造代表性训练集并提升对未知攻击的检出率；方法用无监督聚类自适应选择代表样本构建平衡小样本集，再用孪生结构学习样本间的相似/差异度量。CICIDS2017/2018 上分别报告对攻击类准确率 99.80% / 98.26%，并在未知攻击检出上较对比方法提高若干百分点，说明自适应抽样 + 度量学习在稀少正例场景下对提高召回尤其有效。[jeit.ac.cn](https://jeit.ac.cn/cn/article/doi/10.11999/JEIT241115?viewType=HTML)  
- Liu 铭宇，融合学习的无监督多维时序异常检测（CRAD 2023）：针对云运维多维 KPI 的局部与全局依赖，提出在时域卷积网络中引入自注意力并在模块间建立信息共享的融合学习框架。研究问题是如何同时保持局部关联与捕捉全局模式；实验在多组真实多维时序数据集上表明相比既有方法 F1 提升最高可达 0.0882，表明融合局部—全局建模能改善重构式异常检测的判别力。[crad.ict.ac.cn](https://crad.ict.ac.cn/cn/article/doi/10.7544/issn1000-1239.202220490?viewType=HTML)  
- Mirsky 等，Kitsune（NDSS 2018，在线自编码器集合）：提出在线逐包自编码器集合以实现低延迟流量异常检测，研究问题为实时性与资源受限环境下的无监督检测。方法通过若干小自编码器并行提取流统计特征并进行在线重建误差监控；NDSS 基准实验展示其在流量入侵检出与在线部署延迟上的可行性，为医疗 IoT 网关级在线检测提供工程学参考（但对跨域泛化需配合后续迁移/联邦策略）。[ndss-symposium.org](https://www.ndss-symposium.org/ndss-paper/kitsune-an-ensemble-of-autoencoders-for-online-network-intrusion-detection/)

D. 行为规范 / 规则化与设备识别（医疗设备特有流程与可解释性保障）  
- 樊琳娜等（物联网设备识别与异常检测综述，软件学报 2024）：系统梳理被动/主动设备识别与基于规则与 ML 的异常检测研究，研究问题是识别设备种类以实现细粒度检测并利用行为规范降低误报。综述指出设备识别是构建设备专用异常画像的前提，并强调 MUD / 行为规范、可形式化验证的价值（对医疗设备合规检测尤为重要）。[jos.org.cn](https://jos.org.cn/html/2024/1/6818.htm)  
- IoTSafe（Ding 等，NDSS 2021，被综述引用并作为行为规范示例）：面向物联网交互策略与物理交互发现，采用交互图与策略检查检测配置/联动误用。研究问题是通过静态/动态分析构建设备间可执行策略并检出潜在安全/越权行为；其方法与结论对需严格合规与可解释性的医疗 IoT 场景（跨设备触发与自动化照护）具有直接借鉴意义。（NDSS 论文与工具链公开，可用于医疗策略验证）

实验与评价总结（共性结论与已识别评价盲点）  
1) 联邦/分布式方法在保护病人隐私的同时能较好维持或接近集中式性能，但性能波动与通信轮次、本地数据量异质性直接相关；现实部署需解决客户端失衡与模型偏置（非 IID）问题（见 GB‑AEnet‑FL、FL‑CNN‑LSTM 的实验比较）。  
2) 将时空结构化建模（GCN/TCN/自注意力）与时序分解（CEEMDAN 等）结合的生成/重构体系，能更有效识别跨变量、跨尺度的临床异常信号（Tang 2024 的 MCBiWGAN‑GTN 实证）；但生成式模型对训练稳定性与异常阈值设定敏感，且需大量正常数据以避免判别器/生成器偏差。  
3) 针对稀有临床事件（少样本），自适应抽样 + 度量学习或孪生网络在召回率上给出显著提升（Yin 2025），因此少样本策略是医疗场景的优先工程方向。  
4) 评价体系存在明显短板：多数工作用网络/云/通用 IoT 基准数据集（CIC、Clearwater、MBD 等）而非医疗专用跨院数据；缺少统一的临床假阳性/假阴性成本度量与医生可接受阈值；跨站点泛化性、长期概念漂移（设备固件/使用行为变化）和临床可解释性往往未被充分考察。  
5) 工程部署层面，在线检测（低延迟）与资源受限设备（能耗、通信）之间存在权衡；Kitsune 类轻量在线方法在工程上可行但需与云端的更强表示学习模块协同（混合边缘—云架构）。

趋势与挑战（对 2025 年前后可观测、且可验证的预测，≥3 点）

1) 联邦学习与差分隐私/安全多方计算的工程化整合将成为医疗 IoT 异常检测的主流路径。理由：法规与院际数据主权驱动跨院协同的必要性（已有 2024–2025 文献验证可达接近集中式性能），下一步是把 DP、安全聚合与个性化聚合策略系统化以适配医疗非 IID 数据。可验证标志：2026 年前出现跨院多中心联邦基线竞赛与公开联邦医疗 IoT 基准。参见 GB‑AEnet‑FL、FL‑CNN‑LSTM。  

2) 时空分解（如 CEEMDAN）+ 图时序（GCN/TCN/自注意力）+ 生成式模型（BiWGAN‑GP/GTN）将成为检测复杂多模态临床异常的“堆栈式”范式，但对训练稳定性与阈值可解释性提出更高要求。可验证标志：此类堆栈在真实 ICU/远程监护多中心数据上逐步替代简单重构/预测模型（Tang 2024 的结果为先行证据）。  

3) 少样本、持续学习与因果/可解释检测将并行发展：临床异常稀少且风险高，单靠监督学习不可行；KAFS+孪生/度量学习、元学习与概念漂移检测（终生学习）会成为必要技术栈。可验证标志：未来两年内将出现公开的“少样本医疗异常”基线与连续学习评测协议（参见 YIN 2025）。  

4) 从“像素级”或“报文级”异常告警向“临床决策级”告警的迁移：研究将更多引入临床告警成本函数与医生‑系统闭环验证，评价指标从纯 F1 转为加权临床收益/风险曲线。可验证标志：更多论文在公开数据集上同时报告医学有效性指标或开展小规模临床/放射科医师盲评（目前仍稀缺）。  

5) 标准化医疗 IoT 数据集与基准评测（含隐私保护设置）迫在眉睫：当前公有数据集多为通用网络/云或单中心医疗流；跨院/多设备、带标签的医疗 IoT 异常数据仍稀缺，限制方法在实际临床的可证伪性。可验证标志：期刊/会议将在未来两年逐步要求公开或可验证的数据协议声明（现有综述与多篇方法性论文已提出此需求）。

结论  
过去三年里（以 2022–2025 为窗口），面向云端医疗 IoT 的异常检测研究呈现出：联邦/隐私保护学习快速落地的趋势；时空分解 + 生成对抗/图时序网络成为提高跨变量敏感性的主攻方向；少样本与自适应抽样方法在稀有但临床关键异常的检测上显示出明显优势。与此同时，方法学进步受限于医疗专属基准数据、临床代价量化和可解释性验证。面向可临床部署的下一个阶段，应聚焦跨院联邦评测、可解释的阈值策略与长期持续学习机制的工程化实现。

参考文献（选用真实公开文献与期刊/会议/预印本，≥12 篇；按文中引用先后排序）  

- Tang L., Zhao Y., Xue C., Chen Q. “A Cloud Server Anomaly Detection Model Based on Time Series Decomposition and Spatiotemporal Information Extraction (MCBiWGAN‑GTN).” Journal of Electronics & Information Technology, 2024. [jeit.ac.cn](https://jeit.ac.cn/cn/article/doi/10.11999/JEIT230679?viewType=HTML)  
- Zhang Y., Tang L., Wang K., Chen Q. “基于 GB‑AEnet‑FL 网络的物联网设备异常检测.” 计算机应用研究, 2022. [arocmag.cn](https://www.arocmag.cn/abs/2022.03.0142)  
- Fan L.‑N., Li C.‑L., Wu Y.‑C., et al. “Survey on IoT Device Identification and Anomaly Detection.” 软件学报 (Journal of Software), 2024 (online 2023). [jos.org.cn](https://jos.org.cn/html/2024/1/6818.htm)  
- Wu G., Ling J. “基于自适应交互学习的 CPS 时间序列异常检测.” 计算机应用研究, 2023. [arocmag.cn](https://www.arocmag.cn/abs/2023.03.0095)  
- Yin Z., Chen H., Ma H., Hu T., Bai L. “A Network Traffic Anomaly Detection Method Integrating Unsupervised Adaptive Sampling with Enhanced Siamese Network.” Journal of Electronics & Information Technology (优先出版), 2025. [jeit.ac.cn](https://jeit.ac.cn/cn/article/doi/10.11999/JEIT241115?viewType=HTML)  
- Liu M. “Fusion Learning Based Unsupervised Anomaly Detection for Multi‑Dimensional Time Series.” 中国信息通信研究院期刊 (CRAD), 2023. [crad.ict.ac.cn](https://crad.ict.ac.cn/cn/article/doi/10.7544/issn1000-1239.202220490?viewType=HTML)  
- Wang L., Liu X., Li J., Feng Z. “Network intrusion detection method based on federated learning and spatiotemporal feature fusion.” Journal of Zhejiang University (Engineering Science), 2025. [zjujournals.com](https://www.zjujournals.com/eng/article/2025/1008-973X/20250611.shtml)  
- Mirsky Y., Doitshman T., Elovici Y., Shabtai A. “Kitsune: An ensemble of autoencoders for online network intrusion detection.” NDSS 2018. [ndss-symposium.org](https://www.ndss-symposium.org/ndss-paper/kitsune-an-ensemble-of-autoencoders-for-online-network-intrusion-detection/)  
- Li D., Chen D., Goh J., Ng S. K. “Anomaly detection with generative adversarial networks for multivariate time series.” arXiv:1809.04758, 2018. [arxiv.org](https://arxiv.org/abs/1809.04758)  
- Gulrajani I., Ahmed F., Arjovsky M., Dumoulin V., Courville A. “Improved Training of Wasserstein GANs.” NeurIPS 2017 / arXiv:1704.00028. [arxiv.org](https://arxiv.org/abs/1704.00028)  
- Nguyen T. D., Marchal S., Miettinen M., Fereidooni H., Asokan N., Sadeghi A. R. “DÏoT: A federated self‑learning anomaly detection system for IoT.” ICDCS (or related proceedings), 2019. （联邦自学习 IoT 方法，综述与后续工作广泛引用该路线）[参考综述引用：jos.org.cn](https://jos.org.cn/html/2024/1/6818.htm)  
- Torres M. E., Colominas M. A., Schlotthauer G., Flandrin P. “A complete ensemble empirical mode decomposition with adaptive noise (CEEMDAN).” ICASSP 2011.（时序分解方法，已被 MCBiWGAN‑GTN 等采用）[ieeexplore.ieee.org / 论文索引]  
- Ding W., Hu H., Cheng L. “IoTSafe: Enforcing safety and security policy with real IoT physical interaction discovery.” NDSS 2021 (行为规范 / 策略验证示例，对医疗联动场景的规范化检测具有借鉴意义). [ndss-symposium.org](https://www.ndss-symposium.org/)  

（注：文中所述各项实验结果、评价指标与结论均基于上述公开论文与期刊页面中陈述的实验数据与表格；当文献来自中文期刊的英文/中文页面时优先引用期刊页面以便复核。）