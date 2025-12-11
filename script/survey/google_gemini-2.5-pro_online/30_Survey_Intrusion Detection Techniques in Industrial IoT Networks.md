好的，遵照您的指示。作为一名严谨的科研助手，我将基于提供的真实网络搜索结果，生成一篇关于工业物联网（IIoT）网络入侵检测技术的中文学术综述。

***

### 工业物联网网络中的入侵检测技术研究综述 (2022–2025)

#### **引言**

工业物联网（Industrial Internet of Things, IIoT）通过将传感、计算与物理工业过程深度融合，正在重塑制造业、能源、交通等关键基础设施。然而，其广泛的连接性、异构的设备环境和资源受限的节点特性，也使其暴露于日益复杂的网络攻击之下 [jeit.ac.cn](https://jeit.ac.cn/cn/article/doi/10.11999/JEIT250659?viewType=HTML)。传统的边界防御模型已不足以应对这些威胁，因此，能够主动识别恶意行为的入侵检测系统（Intrusion Detection System, IDS）成为保障IIoT安全的核心。近年来，学术界致力于研究更智能、更具适应性的IIoT-IDS技术。本综述旨在系统梳理2022至2025年间该领域的代表性研究工作，重点剖析基于深度学习、联邦学习及新兴架构的检测方法，总结其共性规律，并展望未来的核心研究趋势与挑战。

#### **方法分类与代表作**

##### **1. 基于深度学习的检测方法**

深度学习模型凭借其强大的非线性特征提取能力，在处理高维、复杂的IIoT网络流量数据方面表现出色。近期研究集中于优化网络结构以捕捉时空特征和应对工业场景的特定挑战。

*   **时间序列特征提取**：为了精准捕捉IIoT流量中的时序攻击模式，刘丽伟等人在《电信科学》上提出了一种基于多尺度残差时间卷积网络（TCN）的入侵检测模型（MRID）[telecomsci.com](https://www.telecomsci.com/zh/article/doi/10.11959/j.issn.1000-0801.2025046/)。该研究针对物联网流量攻击识别问题，设计了多尺度残差时间卷积模块以增强网络对时空特征的表征能力。同时，模型集成了一种改进的流量注意力机制，使其能聚焦于关键信息。在CICIDS2017和CSE-CIC-IDS2018数据集上的实验表明，MRID模型在提升入侵检测效率和模型鲁棒性方面具有显著优势。

*   **生成式模型异常检测**：针对传统方法依赖人工合成伪异常样本、导致与实际缺陷语义关联度不高的问题，黄国恒等人在《广东工业大学学报》上提出了一种基于扩散模型的两阶段工业异常检测网络（DADNet）[xbzrb.gdut.edu.cn](https://xbzrb.gdut.edu.cn/article/doi/10.12052/gdutxb.230204)。该方法首先利用语义引导的异常生成模块合成更真实的缺陷样本，作为先验知识。随后，第一阶段采用图像重建模型修复异常，第二阶段训练一个判别模型来区分修复图像与原始图像的差异，从而定位异常。此外，通过联合关注机制强化了重建性能。实验结果显示，DADNet在多种材质的公开工业数据集上，其性能优于现有模型。

*   **传统机器学习优化**：尽管深度学习是主流，但优化传统机器学习方法在特定场景下仍具价值。一篇发表于《Sensors》的研究针对医疗物联网（IoMT）场景，提出了一种基于树模型的机器学习与过滤器特征选择相结合的优化入侵检测方法 [paper.sciencenet.cn](https://paper.sciencenet.cn/htmlpaper/2025/7/2025729142844983137174.shtm)。该工作旨在解决IoMT设备计算能力受限和数据隐私问题，通过互信息（MI）和XGBoost进行特征选择，减少计算开销。研究采用了决策树（DT）、随机森林（RF）等四种基于树的分类器。在CICIDS2017数据集上的评估显示，该方法实现了98.79%的准确率和仅0.007的虚警率，证明了特征选择和轻量级模型在资源受限环境中的有效性。

##### **2. 基于联邦学习的隐私保护检测**

为解决IIoT数据分散在不同实体、直接汇聚进行模型训练存在隐私泄露风险的问题，联邦学习（Federated Learning, FL）成为研究热点。它允许在不共享原始数据的情况下，进行分布式协同模型训练。

*   **FL与时空特征融合**：王立红等人在《浙江大学学报(工学版)》上提出一种结合联邦学习与时空特征融合的入侵检测方法 [zjujournals.com](https://www.zjujournals.com/eng/article/2025/1008-973X/20250611.shtml)。该研究旨在解决数据特征提取不全面和集中式训练的数据隐私问题，设计了一个并联的CNN和LSTM结构分别提取空间和时间特征，并融合多头注意力机制和BiGRU进行训练。整个训练过程被置于联邦学习框架下，允许多个客户端在本地训练模型，保护数据隐私。在CIC-IDS2018、NSL-KDD等多个数据集上的实验表明，该方法在FL框架下仍能达到高准确率（如在CIC-IDS2018上为99.00%），几乎与集中式训练性能持平。

*   **FL与区块链增强的可信检测**：为应对FL中模型更新可能遭受投毒攻击、缺乏可审计性的挑战，一篇发表于CSDN博客的论文提出了一个联邦学习增强的区块链框架（FL-BCID）[blog.csdn.net](https://blog.csdn.net/hao_wujing/article/details/148142934)。该框架将FL用于分布式、隐私保护的模型训练，同时利用一个支持智能合约的许可区块链来记录模型更新和异常分数，确保了过程的防篡改和可追溯。研究针对IIoT边缘设备设计了轻量级IDS模型。在ToN-IoT和N-BaIoT数据集上的实验证明，FL-BCID在实现97.3%高准确率的同时，相比集中式方法减少了41%的通信开销，为构建可信的IIoT安全架构提供了方案。

##### **3. 面向特定场景与新兴架构的检测方法**

除了通用的检测模型，面向特定工业场景（如工业控制系统）或融合新兴安全架构（如零信任、大模型）的方法也取得了显著进展。

*   **工业控制系统（ICS）的确定性模型**：林小李博士等人在《IEEE Internet of Things Journal》上发表的研究，针对ICS中现有检测方法忽略丢包、网络延迟和状态爆炸等问题，提出了一种基于长短周期确定性有限自动机（LSP-DFA）的实时异常检测方法 [secrss.com](https://www.secrss.com/articles/76382)。该方法通过学习设备级的轮询时间模式和系统级的网络-物理模型来构建双层防御机制。其网络-物理模型通过混合事件离散化、离群值替换和循环排列集等技术，有效缓解了状态爆炸并精确捕捉时序特性。在两个实验室规模的ICS平台上的实验证实，该方法F1分数和准确率分别达到98.81%和99.24%，显著优于现有技术。

*   **大语言模型（LLM）驱动的语义级检测**：针对传统规则匹配方法在物联网场景中误报率高的问题，李超豪等人在《电子与信息学报》上提出了一种由大模型驱动的数据合规检测方法 [jeit.ac.cn](https://jeit.ac.cn/cn/article/doi/10.11999/JEIT250704?viewType=HTML)。该方法分两阶段进行：首先通过快速正则匹配高效筛查出所有潜在违规数据；然后利用大语言模型对初步结果进行语义级合规性复核。研究为不同违规类型设计了基于思维链（CoT）与少样本（Few-shot）提示的增强策略，以减少语义模糊性带来的误判。实验采集了52种真实物联网设备的流量数据，结果表明，该方法将仅靠规则匹配产生的64.3%的误报率成功降至6.9%，证明了LLM在理解复杂语义、提升检测精度方面的巨大潜力。

#### **实验与评价总结**

综合上述代表性研究，可以总结出以下共性结论：

1.  **数据集与评估指标标准化**：新近研究普遍采用CIC-IDS2017/2018、NSL-KDD、UNSW-NB15、ToN-IoT和N-BaIoT等公开数据集进行模型评估，确保了结果的可复现性和可比性 [zjujournals.com](https://www.zjujournals.com/eng/article/2025/1008-973X/20250611.shtml), [blog.csdn.net](https://blog.csdn.net/hao_wujing/article/details/148142934)。准确率（Accuracy）、精确率（Precision）、召回率（Recall）和F1分数（F1-Score）已成为衡量模型性能的“黄金标准”。
2.  **深度模型在特征提取上的优势**：基于TCN、CNN-LSTM等深度学习结构的模型在自动提取IIoT流量的时空强关联特征方面，表现出比传统方法更优越的性能，尤其是在识别复杂和多变的攻击模式时 [telecomsci.com](https://www.telecomsci.com/zh/article/doi/10.11959/j.issn.1000-0801.2025046/)。
3.  **隐私与性能的权衡**：联邦学习框架被证实可以在保护数据隐私的前提下，获得与集中式训练相近（甚至更高）的检测精度，通信开销和收敛速度是其优化的关键 [blog.csdn.net](https://blog.csdn.net/hao_wujing/article/details/148142934), [zjujournals.com](https://www.zjujournals.com/eng/article/2025/1008-973X/20250611.shtml)。
4.  **场景特定知识的重要性**：面向ICS等特定工业场景，融入物理过程知识（如操作周期、状态转移）的模型（如DFA）在检测精度和对抗网络不完美性（如延迟、丢包）方面展现出巨大优势，这表明纯数据驱动的方法存在局限性 [secrss.com](https://www.secrss.com/articles/76382)。
5.  **新兴AI范式的有效性**：生成式模型（如扩散模型）和大型语言模型（LLM）等新兴AI技术在IIoT-IDS领域显示出巨大潜力，前者能生成高质量训练数据以提升模型鲁棒性，后者则能通过语义理解大幅降低误报率 [xbzrb.gdut.edu.cn](https://xbzrb.gdut.edu.cn/article/doi/10.12052/gdutxb.230204), [jeit.ac.cn](https://jeit.ac.cn/cn/article/doi/10.11999/JEIT250704?viewType=HTML)。

#### **趋势与挑战**

基于2025年前后的研究成果，工业物联网入侵检测技术的未来发展呈现以下几个明确趋势：

1.  **去中心化与可信安全架构的融合**：随着数据隐私法规的日益严格和对模型完整性的担忧，单一的IDS将向集成了联邦学习、区块链和零信任（Zero Trust）思想的可信安全架构演进。联邦学习解决“数据孤岛”和隐私问题 [zjujournals.com](https://www.zjujournals.com/eng/article/2025/1008-973X/20250611.shtml)，区块链提供不可篡改的审计日志 [blog.csdn.net](https://blog.csdn.net/hao_wujing/article/details/148142934)，而零信任架构则强调“持续验证、永不信任”，将为动态IIoT环境提供更细粒度的访问控制和威胁响应 [crad.ict.ac.cn](https://crad.ict.ac.cn/article/doi/10.7544/issn1000-1239.202440840?viewType=HTML)。
2.  **信息-物理融合（Cyber-Physical Fusion）安全分析**：未来的攻击将更加隐蔽，倾向于通过操纵信息系统来间接破坏物理过程。因此，IDS必须从单纯分析网络数据（Cyber）转向融合物理系统（Physical）的传感器读数、状态变量和操作日志。构建能够理解物理过程动态演化规律的模型（如数字孪生、DFA）将是检测这类高级攻击的关键 [secrss.com](https://www.secrss.com/articles/76382), [jeit.ac.cn](https://jeit.ac.cn/cn/article/doi/10.11999/JEIT250659?viewType=HTML)。
3.  **大模型与生成式AI的深度应用**：大型语言模型（LLMs）和生成式AI的应用将从初步探索走向深化。LLMs不仅可用于语义增强的告警研判和自动生成安全策略 [jeit.ac.cn](https://jeit.ac.cn/cn/article/doi/10.11999/JEIT250704?viewType=HTML)，还可能作为人机交互接口，辅助安全分析师理解和响应威胁。同时，扩散模型等生成式技术将在高质量数据增强、生成未知攻击场景以进行压力测试和提升模型泛化能力方面发挥核心作用 [xbzrb.gdut.edu.cn](https://xbzrb.gdut.edu.cn/article/doi/10.12052/gdutxb.230204)。

#### **结论**

2022至2025年间，工业物联网的入侵检测技术研究取得了长足进步，呈现出向智能化、去中心化和情境感知的明确趋势。基于深度学习的方法不断优化，以更精确地捕捉IIoT流量的复杂模式；联邦学习已成为解决数据隐私与协同训练矛盾的关键技术；而针对特定工业场景和融合新兴AI范式（如LLM、生成式AI）的IDS架构，则展示了未来发展的巨大潜力。尽管如此，如何构建真正可信、能够理解物理过程并适应动态环境的IDS，仍是该领域面临的核心挑战。未来的研究将更加聚焦于信息-物理融合分析、可信去中心化架构和AI新技术的深度应用，以构建下一代IIoT安全防御体系。

#### **参考文献**
1.  王文婷, 田博彦, 吴法宗, 等. 面向智能电网信息物理融合攻击的建模、检测和防御理论与方法. 电子与信息学报, 2025. [jeit.ac.cn](https://jeit.ac.cn/cn/article/doi/10.11999/JEIT250659?viewType=HTML)
2.  刘丽伟, 赵红超, 李学威, 等. 基于多尺度残差时间卷积网络的物联网入侵检测模型. 电信科学, 2025, 41(04): 164-175. [telecomsci.com](https://www.telecomsci.com/zh/article/doi/10.11959/j.issn.1000-0801.2025046/)
3.  曾炜峰, 程良伦, 黄国恒. 基于扩散生成的两阶段工业异常检测方法. 广东工业大学学报, 2025. [xbzrb.gdut.edu.cn](https://xbzrb.gdut.edu.cn/article/doi/10.12052/gdutxb.230204)
4.  Balhareth, G.; Ilyas, M. Optimized Intrusion Detection for IoMT Networks with Tree-Based Machine Learning and Filter-Based Feature Selection. Sensors, 2024, 24, 5712. [paper.sciencenet.cn](https://paper.sciencenet.cn/htmlpaper/2025/7/2025729142844983137174.shtm)
5.  王立红, 刘新倩, 李静, 冯志全. 基于联邦学习和时空特征融合的网络入侵检测方法. 浙江大学学报(工学版), 2025, 59(6): 1201-1210. [zjujournals.com](https://www.zjujournals.com/eng/article/2025/1008-973X/20250611.shtml)
6.  hao_wujing. 工业物联网中隐私保护入侵检测的联邦学习增强型区块链框架. CSDN博客, 2025. [blog.csdn.net](https://blog.csdn.net/hao_wujing/article/details/148142934)
7.  Lin X, Yao Y, Hu B, et al. A Real-Time Anomaly Detection Method for Industrial Control Systems Based on Long-Short Period Deterministic Finite Automaton. IEEE Internet of Things Journal, 2025. [secrss.com](https://www.secrss.com/articles/76382)
8.  李超豪, 王浩然, 周少鹏, 等. 面向物联网场景的大模型驱动数据合规检测方法. 电子与信息学报, 2025. [jeit.ac.cn](https://jeit.ac.cn/cn/article/doi/10.11999/JEIT250704?viewType=HTML)
9.  王航宇, 吕飞, 程裕亮, 等. 工业物联网零信任安全研究综述. 计算机研究与发展, 2025. [crad.ict.ac.cn](https://crad.ict.ac.cn/article/doi/10.7544/issn1000-1239.202440840?viewType=HTML)
10. Sivanathan, A., Gharakheili, H. H., Loi, F., et al. Classifying IoT devices in smart environments using network traffic characteristics. IEEE Transactions on Mobile Computing, 2019, 18(8): 1745-1759. (引用自[jos.org.cn](https://jos.org.cn/html/2024/1/6818.htm))
11. Mothukuri, V., Khare, P., Parizi, R. M., et al. Federated-learning-based anomaly detection for IoT security attacks. IEEE Internet of Things Journal, 2022, 9(4): 2545-2554. (引用自[zjujournals.com](https://www.zjujournals.com/eng/article/2025/1008-973X/20250611.shtml))
12. Nguyen, T. D., Marchal, S., Miettinen, M., et al. DÏoT: A federated self-learning anomaly detection system for IoT. In: Proc. of the 39th IEEE Int’l Conf. on Distributed Computing Systems (ICDCS), 2019. 756–767. (引用自[jos.org.cn](https://jos.org.cn/html/2024/1/6818.htm))
13. 樊琳娜, 李城龙, 吴毅超, 等. 物联网设备识别及异常检测研究综述. 软件学报, 2024, 35(1): 288-308. [jos.org.cn](https://jos.org.cn/html/2024/1/6818.htm)