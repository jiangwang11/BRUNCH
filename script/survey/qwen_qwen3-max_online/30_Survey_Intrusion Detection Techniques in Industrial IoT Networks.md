# 工业物联网网络入侵检测技术综述（2022–2025）

## 引言

工业物联网（Industrial Internet of Things, IIoT）通过深度融合信息物理系统（CPS）与联网设备，已广泛应用于智能制造、能源与交通等领域。然而，其开放性与异构性显著扩大了攻击面，传统边界防御模型难以应对如 Stuxnet、TRITON 等高级持续性威胁。由此，基于机器学习的入侵检测系统（IDS）成为研究热点。区别于通用物联网，IIoT 具备强实时性、协议专有性与物理过程耦合等特性，对检测算法的准确性、实时性与泛化能力提出更高要求。本文综述 2022–2025 年间具有代表性的 IIoT 入侵检测技术，从方法论层面进行分类，并分析其共性挑战与演进趋势。

## 方法分类与代表作

### 基于确定性有限自动机（DFA）的时空建模

针对现有方法难以建模 IIoT 中复杂时序逻辑与物理状态转移的问题，Lin 等人提出 **LSP-DFA** 模型，构建融合长-短周期的确定性有限自动机，以捕捉系统级网络-物理行为 [secrss.com](https://www.secrss.com/articles/76382)。该方法通过混合事件离散化缓解状态爆炸，并引入循环排列集（CPSet）建模转移时间的顺序性。实验表明，该方法在自建交通灯与传送带数据集上达到 98.81% F1 分数，显著优于 OTALA 与 DFA-ND 等基线，尤其在检测伪装转移与系统恢复场景中误报率降低超 5.5%。

### 联邦学习与隐私保护架构

为解决数据孤岛与隐私泄露问题，Wang 等人提出 **FL-CNN-LSTM** 框架，结合 CNN 与 LSTM 并行提取时空特征，并通过多头注意力机制聚焦关键流量 [zjujournals.com](https://www.zjujournals.com/eng/article/2025/1008-973X/20250611.shtml)。该模型在联邦学习范式下训练，仅上传模型参数以保护原始流量。在 CIC-IDS2018、NSL-KDD 和 UNSW-NB15 数据集上，其准确率分别达 99.00%、97.64% 和 75.28%，且与集中式训练性能差距小于 0.1%，有效平衡了隐私与精度。

Hao 等人进一步提出 **FL-BCID** 框架，将联邦学习与区块链结合，利用智能合约记录模型更新以确保防篡改性 [csdn.net](https://blog.csdn.net/hao_wujing/article/details/148142934)。该框架设计轻量级 IDS 模型以适配边缘设备，在 ToN-IoT 与 N-BaIoT 数据集上达到 97.3% 准确率，并将通信开销降低 41%，验证了其在资源受限 IIoT 环境中的可行性。

### 基于深度时序网络的异常检测

面对高维时序流量数据，Liu 等人提出 **MRID** 模型，采用多尺度残差时间卷积网络（TCN）增强时空表征能力，并设计改进的流量注意力机制以聚焦关键特征 [telecomsci.com](https://www.telecomsci.com/zh/article/doi/10.11959/j.issn.1000-0801.2025046/)。该模型可无缝集成于雾计算架构，实现实时检测。在 CICIDS2017 与 CSE-CIC-IDS2018 数据集上的实验表明，MRID 在保持计算效率的同时，显著提升了对隐蔽攻击的鲁棒性。

### 面向小样本与类别不平衡的检测

针对攻击样本稀疏与类别极度不平衡的现实挑战，Yin 等人提出结合 **KAFS 抽样**与**孪生多层感知机（SMLP）** 的检测方法 [jeit.ac.cn](https://jeit.ac.cn/cn/article/doi/10.11999/JEIT241115?viewType=HTML)。KAFS 算法基于 K-medoids 聚类自适应抽取代表性小样本，SMLP 则通过距离度量学习流量异同。该方法在 CICIDS2017 和 CICIDS2018 上仅用 177 与 141 个样本即达到 99.80% 与 98.26% 的准确率，对未知攻击的检出率分别提升 2.85% 与 1.73%，显著优于现有小样本方法。

### 基于大语言模型（LLM）的智能检测

为利用 LLM 的上下文理解与泛化能力，Otoum 等人提出基于微调 LLM 的端到端检测与预防框架 [csdn.net](https://blog.csdn.net/u013524655/article/details/147691632)。该框架在 IoT-23 与 TON_IoT 数据集上微调轻量级 BERT 模型（如 BERT-Small），并结合决策树实施自动化缓解。实验显示，BERT-Small 在 21 类攻击分类任务中达到 99.75% 的准确率，验证了 LLM 在复杂 IIoT 威胁识别中的巨大潜力。

## 实验与评价总结

综合近年研究，可归纳出以下共性结论：（1）**评估数据集**：多数工作依赖 CIC 系列（CICIDS2017/2018）、UNSW-NB15、ToN-IoT 等通用数据集，但其与真实 IIoT 物理过程耦合度不足；少数研究（如 LSP-DFA）构建了专用实验平台以弥补此缺陷。（2）**性能指标**：高检测率（>95%）已成常态，但对**伪装攻击**、**系统恢复**、**低频长周期攻击**等复杂场景的检测能力，以及**低误报率**（<1%）成为区分方法优劣的关键。（3）**资源效率**：面向边缘部署的研究普遍强调模型轻量化（如 FL-BCID、MRID）与低通信开销（如 FL-BCID 降低 41%），以满足 IIoT 的实时性要求。

## 趋势与挑战

基于近期进展，可预测 2025 年及以后的研究将聚焦于以下方向：
1.  **物理-信息深度融合建模**：未来工作将更紧密耦合物理过程模型（如 PDE、状态方程）与数据驱动模型，以检测仅改变物理状态（如温度、压力）而网络流量正常的隐蔽攻击。
2.  **自主化与可解释性**：结合 LLM 与 XAI（可解释人工智能）技术，构建不仅能检测/预防攻击，还能生成人类可理解的告警根因分析与处置建议的自主安全代理（Autonomous Security Agent）。
3.  **跨域联邦学习与零信任架构**：为应对多厂商、多工厂的协同安全需求，基于零信任原则的跨域联邦学习将成为主流，其核心挑战在于设计高效的跨域信任评估与模型聚合机制，以抵御投毒攻击。

## 结论

2022–2025 年间，IIoT 入侵检测技术从单一的流量分析向融合物理过程、保护数据隐私、适应资源约束的综合智能安全体系演进。以 LSP-DFA 为代表的时空建模、以 FL-CNN-LSTM 为代表的隐私计算、以及以 LLM 为代表的智能推理，共同构成了当前研究的三大支柱。未来，突破真实物理-信息耦合数据集的缺失、提升对高级隐蔽攻击的检测能力、并实现可解释的自主安全闭环，将是推动该领域走向实用化的核心挑战。

## 参考文献

1.  Lin, X., Yao, Y., Hu, B., et al. A Real-Time Anomaly Detection Method for Industrial Control Systems Based on Long-Short Period Deterministic Finite Automaton. *IEEE Internet of Things Journal*, 2025. [secrss.com](https://www.secrss.com/articles/76382)
2.  Wang, L., Liu, X., Li, J., & Feng, Z. Network intrusion detection method based on federated learning and spatiotemporal feature fusion. *Journal of Zhejiang University(Engineering Science)*, 59(6), 1201-1210, 2025. [zjujournals.com](https://www.zjujournals.com/eng/article/2025/1008-973X/20250611.shtml)
3.  Hao, W. Federated Learning Enhanced Blockchain Framework for Privacy-Preserving Intrusion Detection in Industrial IoT. *CSDN Blog*, 2025. [csdn.net](https://blog.csdn.net/hao_wujing/article/details/148142934)
4.  Liu, L., Zhao, H., Li, X., & Sun, B. Multiscale residual temporal convolutional networks-based intrusion detection model in Internet of things. *Telecommunications Science*, 41(4), 164-175, 2025. [telecomsci.com](https://www.telecomsci.com/zh/article/doi/10.11959/j.issn.1000-0801.2025046/)
5.  Yin, Z., Chen, H., Ma, H., Hu, T., & Bai, L. A Network Traffic Anomaly Detection Method Integrating Unsupervised Adaptive Sampling with Enhanced Siamese Network. *Journal of Electronics & Information Technology*, 2025. [jeit.ac.cn](https://jeit.ac.cn/cn/article/doi/10.11999/JEIT241115?viewType=HTML)
6.  Otoum, Y., Asad, A., & Nayak, A. An LLM-based Framework for Threat Detection and Prevention in IoT Ecosystems. *arXiv preprint arXiv:2505.00240*, 2025. [csdn.net](https://blog.csdn.net/u013524655/article/details/147691632)
7.  Sun, H., Long, X., Han, L., Huang, Y., & Li, Q. Overview of anomaly detection techniques for industrial Internet of things. *Journal on Communications*, 43(3), 196-210, 2022. [joconline.com.cn](https://www.joconline.com.cn/zh/article/doi/10.11959/j.issn.1000-436x.2022032/?viewType=HTML)
8.  Liu, Q., Chen, Y., Ni, J., et al. Survey on Machine Learning-Based Anomaly Detection for Industrial Internet. *Journal of Computer Research and Development*, 59(5), 994-1013, 2022. [crad.ict.ac.cn](https://crad.ict.ac.cn/cn/article/doi/10.7544/issn1000-1239.20211147?viewType=citedby-info)
9.  Wang, H., Lü, F., Cheng, Y., Lü, S., Sun, D., & Sun, L. A Review of Zero Trust Security Research in Industrial Internet of Things. *Journal of Computer Research and Development*, 2025. [crad.ict.ac.cn](https://crad.ict.ac.cn/article/doi/10.7544/issn1000-1239.202440840?viewType=HTML)
10. “Ditecting” Team. 2022 Industrial Control Network Security Situation White Paper. *Ditecting*, 2023. [secrss.com](https://www.secrss.com/articles/51103)
11. Moustafa, N., & Slay, J. UNSW-NB15: a comprehensive data set for network intrusion detection systems. In *2015 Military Communications and Information Systems Conference (MilCIS)*, 2015.
12. Koroniotis, N., Moustafa, N., Sitnikova, E., et al. Towards the development of realistic botnet dataset in the Internet of things for network forensic analytics: Bot-IoT dataset. *Future Generation Computer Systems*, 100, 779-796, 2019.