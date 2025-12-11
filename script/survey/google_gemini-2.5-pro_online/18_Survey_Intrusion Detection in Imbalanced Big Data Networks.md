好的，遵从您的指示。作为一名严谨的科研助手，我将基于提供的网络搜索结果，生成一篇关于“Intrusion Detection in Imbalanced Big Data Networks”的中文学术综述。

---

### **面向不平衡大数据的网络入侵检测技术综述 (2022–2025)**

#### **引言**

随着网络技术的飞速发展，网络流量呈现出大容量、高维度和高动态性的特点。网络入侵检测系统（IDS）作为保障网络安全的关键防线，面临着前所未有的挑战。其中，数据不平衡问题尤为突出：在真实网络环境中，正常流量占据绝大多数，而各类攻击流量（尤其是新型和罕见的攻击）则属于极少数类别。基于传统机器学习和深度学习的检测模型在处理此类不平衡数据集时，往往会偏向于多数类，导致对少数类攻击的检测率（Recall）低下，构成严重的安全隐患。为应对此挑战，2022至2025年间，研究人员从数据、算法和框架等多个层面提出了创新的解决方案。本综述旨在系统梳理并总结这一时期内的代表性工作，并展望未来的研究趋势。

#### **方法分类与代表作**

##### **1. 数据级方法 (Data-Level Methods)**

此类方法旨在通过修改训练数据集的分布来缓解类别不平衡问题，主要包括数据生成和自适应采样两大方向。

###### **1.1 对抗生成与数据增强**

生成对抗网络（GAN）及其变体被广泛用于生成高质量的少数类（攻击）样本。

-   **CSAGC-IDS** [[blog.csdn.net](https://blog.csdn.net/hao_wujing/article/details/148144069)] 针对不平衡数据和高维复杂流量，提出了一种双模块深度学习模型。其核心之一是SC-CGAN，一种融合了自注意力机制的条件生成对抗网络（Conditional GAN），用于生成高质量的少数类攻击数据以平衡训练集。在此基础上，一个成本敏感的卷积神经网络（CSCA-CNN）用于分类。实验表明，在NSL-KDD数据集上，该方法有效地提升了稀有攻击类别的检测性能，五分类任务的F1分数达到84.52%。

-   **Tor混淆流量识别框架** [[paper.edu.cn](https://paper.edu.cn/releasepaper/content/202502-146)] 针对Tor混淆流量数据集中高质量带标签样本稀缺且不平衡的问题，提出了一种新颖的GAN框架。该框架的创新之处在于，生成器直接补充少数类样本以提升判别器自身的分类性能，简化了传统基于GAN的数据增强流程。作者收集了Obfs4、Snowflake等多种新型混淆协议构建数据集。实验证明，该框架在平衡与不平衡数据集上均表现出卓越的性能和鲁棒性。

###### **1.2 自适应与小样本采样**

该方向通过智能采样策略，构建更具代表性且均衡的小样本训练集，以提升模型学习效率和泛化能力。

-   **KAFS-SMLP** [[jeit.ac.cn](https://jeit.ac.cn/cn/article/doi/10.11999/JEIT241115?viewType=HTML)] 针对传统机器学习方法受类别不平衡影响严重的问题，提出了一种无监督自适应抽样与改进孪生网络结合的方法。该方法首先设计了基于K-medoids的自适应小样本抽样算法（KAFS），在无监督情况下动态抽取最具代表性的流量样本，数据均衡。然后，一个改进的孪生多层感知机（SMLP）模型学习样本间的异同关系进行分类。实验显示，该方法在CIC-IDS2017和CIC-IDS2018数据集上分别以极少的样本（177和141个）达到了99.80%和98.26%的准确率，且对未知攻击的检出率提升显著。

##### **2. 算法级方法 (Algorithm-Level Methods)**

此类方法通过改进模型结构或优化策略，使其能更好地从不平衡数据中学习。

###### **2.1 混合模型与时空特征融合**

结合卷积神经网络（CNN）提取空间特征和循环神经网络（RNN）及其变体（如LSTM, GRU）提取时间特征的混合模型已成为研究热点。

-   **MSECNN-BiLSTM** [[jeit.ac.cn](https://jeit.ac.cn/cn/article/doi/10.11999/JEIT230825?viewType=HTML)] 针对模型对流量时空特性利用率低的问题，提出了一种融合模型。该模型利用一维CNN挖掘流量数据的空间特征，并引入多头挤压激励（MSE）注意力机制自适应地对特征进行加权。随后，双向长短期记忆网络（BiLSTM）用于捕捉流量的时序依赖性。实验证明，在NSL-KDD数据集上，该混合模型的F1分数达到90.13%，显著优于其任何单一组件。

-   **FL-CNN-LSTM** [[www.zjujournals.com](https://www.zjujournals.com/eng/article/2025/1008-973X/20250611.shtml)] 提出了一种在联邦学习框架下的时空特征融合方法，以解决数据孤岛和隐私泄露问题。其核心检测模型采用CNN和LSTM并行结构，分别提取空间和时间特征后进行融合，并结合多头注意力和BiGRU进行训练。为处理数据不平衡，该工作明确使用了SMOTE进行过采样。实验表明，该模型在CIC-IDS2018、NSL-KDD等数据集上取得了99.00%、97.64%的高准确率。

-   **MRID** [[www.telecomsci.com](https://www.telecomsci.com/zh/article/doi/10.11959/j.issn.1000-0801.2025046/)] 针对物联网（IoT）入侵检测场景，提出基于多尺度残差时间卷积网络（TCN）的模型。TCN作为一种有效的序列建模工具，能够并行处理并捕获长期依赖关系，该模型通过多尺度残差模块和流量注意力机制，增强了时空表征能力。实验验证，MRID在CIC-IDS2017和CSE-CIC-IDS2018数据集上提高了检测效率和模型鲁棒性。

###### **2.2 模型优化与自动化**

通过自动化方法（如超参数优化）来提升基础模型在特定不平衡数据集上的性能。

-   **GSDE-GRU** [[www.xxjlclzzs.com](https://www.xxjlclzzs.com/public/uploads/20251030/21ec7b431debf035699aca53388306fa.pdf)] 针对门控循环单元（GRU）等模型在参数配置上的挑战，提出了一种融合全局敏感性差分进化（GSDE）算法与GRU的模型。该研究利用GSDE算法对GRU网络的学习率、隐藏层节点数等关键超参数进行全局智能优化。这一协同机制有效解决了参数配置失配问题。在UNSW-NB15和NSL-KDD数据集上，该模型的准确率分别达到96.8%和98.2%，且收敛速度和鲁棒性均优于传统GRU模型。

-   **IRFD** [[www.telecomsci.com](https://www.telecomsci.com/zh/article/doi/10.11959/j.issn.1000-0801.2025002/)] 提出了一个基于自编码器降维的改进残差网络入侵检测模型。该方法首先利用堆叠降噪稀疏自编码器进行特征降维和有效特征提取。然后，一个集成了卷积注意力机制的残差网络（ResNet）用于分类。这种“特征工程+深度模型”的设计思路在UNSW-NB15和CIC-IDS2017数据集上均取得了超过99%的准确率和高F1分数，验证了其有效性。

#### **实验与评价总结**

-   **常用数据集**：2022-2025年的研究普遍采用公开的、具有代表性的数据集进行模型评估，主要包括**CIC-IDS2017**、**CIC-IDS2018 (CSE-CIC-IDS2018)**、**NSL-KDD**和**UNSW-NB15**。这些数据集因其包含真实世界的网络流量、多样的攻击类型以及显著的类别不平衡特性，成为评测模型鲁棒性和泛化能力的基准。

-   **核心评价指标**：鉴于类别不平衡的特性，单一的准确率（Accuracy）已不足以全面评估模型性能。研究工作普遍采用**精确率（Precision）**、**召回率（Recall）**和**F1分数（F1-Score）**作为核心指标。其中，F1分数因其兼顾了精确率和召回率，被认为是衡量模型在不平衡数据上综合性能的关键。部分研究还引入了**误报率（FAR）**和**马修斯相关系数（MCC）**来更细致地评估模型的性能。

-   **共性结论**：
    1.  **数据级方法成效显著**：通过GAN生成或SMOTE过采样等方法预处理数据，能有效缓解模型训练中的偏见，是提升后续分类器性能的有效前端步骤。
    2.  **混合模型成为主流**：结合CNN和RNN（特别是LSTM/GRU/BiLSTM）的混合模型因能同时捕获流量数据的空间与时间特征，其性能通常优于单一结构的模型。
    3.  **注意力机制是标配**：在混合模型中加入各种注意力机制（如自注意力、通道注意力等）已成为标准做法，它能帮助模型聚焦于关键特征，进一步提升检测精度。
    4.  **效率与性能并重**：一些先进方法（如自适应采样、超参数优化）能在保证甚至超越SOTA性能的同时，使用更少的训练样本或更快的收敛速度，这对于处理“大数据”至关重要。

#### **趋势与挑战**

基于上述代表性工作，面向2025年及以后，网络入侵检测领域在应对不平衡大数据挑战时呈现出以下发展趋势：

1.  **从大数据到小样本学习（Few-Shot/Zero-Shot Learning）**：随着攻击手段的快速迭代，获取大量标注的新型攻击样本变得不切实际。研究趋势正转向如何在仅有少量甚至没有样本的情况下识别新攻击。如KAFS-SMLP等工作 [[jeit.ac.cn](https://jeit.ac.cn/cn/article/doi/10.11999/JEIT241115?viewType=HTML)] 已经展现了小样本学习的潜力，未来基于元学习或度量学习的零样本/小样本入侵检测将成为关键研究方向。

2.  **从集中式到联邦学习（Federated Learning）**：数据隐私和安全法规（如GDPR）日益严格，使得跨机构的数据共享和集中式模型训练变得困难。联邦学习作为一种能够保护数据隐私的分布式机器学习范式，为解决数据孤岛问题提供了可行路径 [[www.zjujournals.com](https://www.zjujournals.com/eng/article/2025/1008-973X/20250611.shtml)]。未来的挑战在于如何应对客户端数据非独立同分布（Non-IID）问题，以及如何降低通信开销。

3.  **从“黑盒”到可解释性与自动化（Explainability & Automation）**：深度学习模型常被称为“黑盒”，其决策过程不透明，这在需要溯源和决策依据的安全领域是重大障碍。引入LIME、SHAP等可解释性分析工具 [[blog.csdn.net](https://blog.csdn.net/hao_wujing/article/details/148144069)]，以及实现超参数自动优化 [[www.xxjlclzzs.com](https://www.xxjlclzzs.com/public/uploads/20251030/21ec7b431debf035699aca53388306fa.pdf)]，将是提升模型实用性和可信度的重要趋势。

4.  **从通用检测到专用场景深度优化**：研究正从通用的网络入侵检测，向特定、高价值场景迁移和深化。例如，针对物联网、加密流量（如Tor [[paper.edu.cn](https://paper.edu.cn/releasepaper/content/202502-146)]）、大模型训练集群 [[www.paper.edu.cn](https://www.paper.edu.cn/releasepaper/content/202504-3)] 等专用网络的异常检测，将成为未来的研究热点。这些场景具有独特的流量模式和安全需求，需要定制化的模型和解决方案。

#### **结论**

面对网络入侵检测中长期存在的类别不平衡与大数据挑战，2022至2025年的研究取得了长足进步。通过数据级增强、算法级模型融合与优化以及框架级创新，检测模型的精度、召回率和F1分数均得到显著提升。混合模型结合注意力机制已成为当前高性能检测系统的坚实基础。展望未来，研究的重心将进一步向小样本学习、联邦学习框架下的隐私保护、模型可解释性以及面向专用场景的深度优化等方向倾斜，以更好地满足现实世界复杂、动态且注重隐私的网络安全需求。

#### **参考文献**
[1] 尹梓诺, 陈鸿昶, 马海龙, 胡涛, 白禄鑫. 无监督自适应抽样与改进孪生网络结合的网络流量异常检测方法[J]. 电子与信息学报. [[jeit.ac.cn](https://jeit.ac.cn/cn/article/doi/10.11999/JEIT241115?viewType=HTML)]
[2] hao_wujing. 面向复杂和不平衡数据的双模块深度学习网络入侵检测模型[EB/OL]. [[blog.csdn.net](https://blog.csdn.net/hao_wujing/article/details/148144069)]
[3] 赵鹏飞, 陆天波. 面向不平衡数据集的Tor混淆流量对抗生成识别框架[EB/OL]. 中国科技论文在线. [[paper.edu.cn](https://paper.edu.cn/releasepaper/content/202502-146)]
[4] 王立红, 刘新倩, 李静, 冯志全. 基于联邦学习和时空特征融合的网络入侵检测方法[J]. 浙江大学学报(工学版), 2025, 59(6): 1201-1210. [[www.zjujournals.com](https://www.zjujournals.com/eng/article/2025/1008-973X/20250611.shtml)]
[5] 顾伟, 行鸿彦, 侯天浩. 基于网络流量时空特征和自适应加权系数的异常流量检测方法[J]. 电子与信息学报, 2024, 46(6): 2647-2654. [[jeit.ac.cn](https://jeit.ac.cn/cn/article/doi/10.11999/JEIT230825?viewType=HTML)]
[6] 刘丽伟, 赵红超, 李学威, 孙滨. 基于多尺度残差时间卷积网络的物联网入侵检测模型[J]. 电信科学, 2025, 41(4): 164-175. [[www.telecomsci.com](https://www.telecomsci.com/zh/article/doi/10.11959/j.issn.1000-0801.2025046/)]
[7] 郭忠. 基于ＧＳＤＥ⁃ＧＲＵ 融合模型的网络入侵检测方法[J]. 信息记录材料, 2025, 26(11): 80-84. [[www.xxjlclzzs.com](https://www.xxjlclzzs.com/public/uploads/20251030/21ec7b431debf035699aca53388306fa.pdf)]
[8] 孙敬, 丁嘉伟, 冯光辉. 一种基于自编码器降维的神经卷积网络入侵检测模型[J]. 电信科学, 2025, 41(2): 129-138. [[www.telecomsci.com](https://www.telecomsci.com/zh/article/doi/10.11959/j.issn.1000-0801.2025002/)]
[9] 刘贺, 王晓湘. 基于日志与流量分析的大模型训练异常检测[EB/OL]. 中国科技论文在线. [[www.paper.edu.cn](https://www.paper.edu.cn/releasepaper/content/202504-3)]
[10] 陈解元. 基于LSTM的卷积神经网络异常流量检测方法[J]. 信息技术与网络安全, 2021, 40(7): 42-46. [[www.chinaaet.com](https://www.chinaaet.com/article/3000135286)]
[11] GUPTA N, JINDAL V, and BEDI P. CSE-IDS: Using cost-sensitive deep learning and ensemble algorithms to handle class imbalance in network-based intrusion detection systems[J]. Computers & Security, 2022, 112: 102499.
[12] YANG Jingcheng, LI Hongwei, SHAO Shuo, et al. FS-IDS: A framework for intrusion detection based on few-shot learning[J]. Computers & Security, 2022, 122: 102899.
[13] WU Zhijun, GAO Pan, CUI Lei, et al. An incremental learning method based on dynamic ensemble RVM for intrusion detection[J]. IEEE Transactions on Network and Service Management, 2022, 19(1): 671–685.
[14] JIN Zhigang, ZHOU Junyi, LI Bing, et al. FL-IIDS: A novel federated learning-based incremental intrusion detection system[J]. Future Generation Computer Systems, 2024, 151: 57–70.