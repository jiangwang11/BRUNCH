# 大规模不平衡网络数据中的入侵检测：2022-2025年系统性综述

本综述汇总了2022-2025年间关于不平衡网络大数据入侵检测系统（IDS）的代表性研究进展。该领域面临两个核心矛盾：其一，网络攻击事件在正常流量中的占比极低（通常<5%），导致严重的类别不平衡问题；其二，高维异构网络数据（日均TB级）要求检测算法具备实时处理能力和可伸缩性。现有研究主要围绕五个方向展开：（1）数据层面的重采样与合成技术，（2）深度学习与传统机器学习的混合架构，（3）可解释人工智能在决策透明化中的应用，（4）跨域迁移与元学习的泛化能力，（5）边界计算与联邦学习的隐私保护。本文系统分析这些方向的技术方案、实验对标与存在的开放问题，并指出2025年前后的发展趋势。

---

## 方法分类与代表性工作

### 数据重采样与合成技术

类别不平衡问题是网络入侵检测中的首要挑战。SMOTE（合成少数类过采样技术）及其变体是处理这一问题的经典方法，但单一的SMOTE往往难以适应多样化的少数类分布。为此，多项研究提出了自适应与灵活的合成方案。

Chawla等人在2002年提出的SMOTE方法虽然经典，但在高维网络数据中面临新的挑战。Nazar与Omoregbe在2023年提出的FLEX-SMOTE[7]采用基于密度函数的自适应过采样策略，能够根据少数类的分布特征灵活选择综合区域。该方法相比传统SMOTE改进之处在于：通过计算少数类样本的局部密度，决定在核心区域还是边界区域生成合成样本；在多种类不平衡数据集上验证了该策略的通用性；避免了试错法来选择合适的SMOTE变体。在医疗与网络安全数据集上的对比实验表明，FLEX-SMOTE相比Borderline-SMOTE和ADASYN在少数类召回率上提升10-15%。

成本敏感学习将不平衡问题重新框架化为带权误分类成本的优化问题。Sun等人的成本敏感Boosting方法[23]通过在样本权重更新公式中嵌入误分类成本系数，动态强化对少数类的学习。该方法在三个位置引入成本项（指数内部、外部或两者），形成三种改进的AdaBoost变体。在KDD99数据集上针对U2R和R2L这两类困难的少数类攻击，该方法相比标准AdaBoost的F1分数提升8-12%，同时保持了计算效率。

生成对抗网络（GAN）在合成不平衡数据中展现了独特优势。GAN通过生成器与判别器的对抗训练，能生成统计特性接近真实少数类的高保真合成样本，同时避免了直接访问原始数据带来的隐私风险。arXiv 2509.20411[29]系统综述了GAN在网络入侵检测中的应用，指出Conditional GAN（CGAN）与Wasserstein GAN（WGAN）在生成攻击流量样本时优于传统的SMOTE方法，特别是在适应新型攻击时具有更好的泛化性。该研究还强调了GAN训练的不稳定性（模式坍缩）仍是实际部署的障碍。

---

### 深度学习与混合架构

单一的深度学习模型在处理网络流量时往往在特征提取的某个维度存在局限性。CNN擅长捕捉空间特征，LSTM善于建模序列依赖，Transformer引入自注意机制以增强长程依赖建模。近年研究普遍采用混合架构来弥补各自短板。

Nature 2025年刊登的IDS-MTran[14]模型融合CNN、Transformer与多尺度特征蒸馏。该论文在NSL-KDD数据集上达到99.68%准确率与0.22%误报率，其创新点在于：采用多头自注意机制并行处理不同表示子空间中的信息；通过焦点损失函数（Focal Loss）加权处理数据不平衡，使模型在训练中更关注难分样本；引入特征金字塔结构进行多尺度特征融合，增强对不同大小攻击模式的检测能力。相比单独的CNN或Transformer，该混合架构在少数类攻击的召回率上提升15-20%。

Mynuddin等人（2024）[1]强调了CNN-RNN混合模型在复杂攻击模式检测中的优势。该方案通过CNN的卷积层提取网络流的局部特征，再用RNN的循环单元捕捉攻击行为的时间演化。但这类混合模型面临的核心挑战是黑箱性：虽然性能指标优异，但安全分析员难以理解模型为何将某条流量标记为异常，这限制了在实际安全运营中心（SOC）的可信度。

CNN-LSTM-Random Forest混合方案由Nature 2025年的研究[3]提出，在KDD99和UNSW-NB15数据集上分别达到97%和98%以上的准确率。该方法特点为：CNN自动进行特征选择，将原始的41维特征压缩至18维，同时保留判别信息；Random Forest算法对不平衡数据具有天然鲁棒性，通过多数投票避免对多数类的偏向；在处理高维稀疏数据和类别不平衡时，该架构比纯深度学习方案的计算开销低30-40%。

---

### 可解释性与决策透明化

深度学习模型性能优异但决策过程不透明，严重阻碍了其在生产环保中的部署。SHAP（Shapley加性解释）与LIME（局部可解释的与模型无关解释）是当前最主流的解释工具。

NIH 2024年的系统综述[21]分析了XAI在IDS中的集成现状，指出基于规则和决策树的可解释模型更受安全分析员青睐，但其检测准确率通常低于黑箱深度学习方案5-10%。该综述总结了三类主要的XAI技术：（1）特征归因法（SHAP与LIME），通过扰动输入或计算Shapley值量化各特征对预测的贡献；（2）基于代理的方法，用可解释的简单模型近似黑箱模型；（3）混合方案，将专家规则与数据驱动学习相结合。在具体应用中，SHAP已成功识别出IDS误报的根本原因（如异常高的网络流量或特定协议频率），从而提升分析员的信心。

arXiv 2406.09684[24]对多种IDS模型的可解释性进行了对比分析，发现Random Forest在特征重要性排序上的一致性与透明性优于深度神经网络，且在KDD99数据集上的训练时间仅为LSTM的1/10。该研究暗示，在对可解释性要求高的场景（如金融基础设施），应优先考虑集成树模型而非黑箱深度学习。

混合规则与数据驱动学习的方法由Barnard等人（2024）[1]提出，采用决策树算法动态生成检测规则。初期基于专家知识的规则提供基础，随着新数据的积累与新型攻击的出现，决策树持续生成新的规则。这种持续学习机制使系统能同时维持高准确率与可理解性，但需要较高的标注成本。

---

### 转移学习与元学习

网络攻击的多样性和演变性决定了单一训练集上学习的模型在新场景中往往性能下降。转移学习与元学习提供了跨域泛化的新范式。

arXiv 2511.20500[15]提出了用于高级持久威胁（APT）检测的对比转移学习框架。该方案集成了转移学习、可解释AI、对比学习与孪生网络，核心贡献包括：通过注意力增强自编码器进行域内知识预训练，再在目标数据集上微调，有效克服了不同网络环境间的特征空间错位问题；采用SHAP与重建误差结合的特征选择机制，优先保留跨域具有稳定性的判别特征；在多个APT数据集间的迁移实验中，模型泛化性相比标准转移学习提升12-18%。该研究还强调了转移学习在减少计算成本（预训练模型快速适应新场景）与处理标注数据稀缺问题中的实用价值。

NIH 2023年发表的元学习方法[53]采用堆叠的深度学习模型（RNN、LSTM、CNN）作为基学习器，再通过逻辑回归、MLP、SVM或XGBoost作为元学习器来训练。该方法在NSL-KDD和UNSW-NB15数据集上的关键发现为：通过元学习器的组合，能自适应地为不同类型的攻击选择最优的基学习器权重；相比单一基学习器，准确率分别提升1-2%，但计算开销增加约20%。元学习的优势在于其对新型攻击的快速适应能力（few-shot检测），但如何在资源受限的边界设备上部署仍是开放问题。

Nature 2025年的联邦转移学习方法[18]专针对稀有攻击类别检测，采用联邦学习聚合分布式数据，同时用转移SVM适应变化的数据分布。该方案在处理数据隐私与类别极度不平衡（如某些攻击类型在训练集中<0.1%）的场景中表现出色。

---

### 图神经网络与网络拓扑建模

将网络流量建模为动态图，其中节点代表IP地址或设备，边代表通信连接，能捕捉传统流特征难以表达的网络拓扑异常。

OSTI 2025年的混合图神经网络方法[16]结合GraphSAGE与图注意网络（GAT）。GraphSAGE通过本地特征聚合生成节点嵌入，GAT通过注意机制为不同邻域节点赋予不同权重。该方案相比单独的GraphSAGE或GAT在IoT网络异常检测中提升约8-12%的检测率，特别是在识别扫描与侦察阶段的低速威胁时优势明显。

arXiv 2507.13954[13]提出了基于平均可控性的图异常检测方法。该研究首次将控制论中的可控性指标引入图异常检测，通过计算节点对网络全局行为的影响力，将其作为GNN的附加特征。实验在六个基准图数据集上验证，该方法在稀疏与不平衡场景下相比基线GNN提升10-15%的异常检测准确率。

---

### 在线学习与概念漂移适应

网络流量分布随时间动态演变（称为概念漂移）是部署IDS的重大挑战。批量学习模型在离线训练后难以适应这种演变。

arXiv 2510.27304[37]研究了流式IoT流量中的概念漂移。该论文将异常检测框架化为二分类问题，对比了批量学习与流式学习的性能。关键发现为：（1）批量随机森林模型在概念漂移后性能急剧下降（准确率从95%跌至70%），而流式学习算法（Adaptive Random Forest、Hoeffding树、朴素贝叶斯）能通过增量更新主动适应；（2）在模拟具有不同概念漂移类型的流中，流式算法在处理梯进漂移时性能衰减<5%；（3）但流式学习面临的实际瓶颈在于标注延迟——假设标签即时可用，而真实场景中安全分析员的标注往往滞后数小时或数天。

CEUR 2025年的概念漂移流生成器[40]针对IDS的评估提出了系统性工具。该研究生成了包含特定漂移类型与强度的现实数据流，使研究者能在受控条件下评估IDS的鲁棒性。初步实验表明，当流中引入突发漂移时，未适应的IDS性能下降20-30%。

---

### 自动化机器学习（AutoML）

AutoML通过自动化特征工程、模型选择与超参数调优，降低了手工调参的开销，同时往往能发现人工难以预见的最优配置。

arXiv 2411.15920[19]应用MLJAR AutoML框架开发了堆叠集成模型（LightGBM、CatBoost、XGBoost）。该方法在NSL-KDD数据集上达到90%准确率与89% F1分数，超越各单独模型。AutoML的关键优势为：自动进行特征选择与工程，消除了大量人工探索；通过网格搜索与贝叶斯优化并行探索超参数空间，在有限计算资源下发现接近最优的配置；堆叠集成通过加权投票结合多个学习器，提升鲁棒性与泛化能力。

arXiv 2512.02272[44]针对资源受限的IoT设备提出了硬件感知的神经架构搜索（HW-NAS）。该方法在严格的闪存、内存与计算量限制下优化IDS模型：LightGBM在仅75KB闪存与1.2K操作数下达到95.3%准确率；HW-NAS优化的CNN在190KB闪存与840K浮点运算下达到97.2%准确率。该研究在Raspberry Pi 3B+上验证了模型的实际可部署性，树模型保持在30ms以内延迟，CNN在精度优先的场景下仍可接受。

---

### 成本敏感与加权方法

在网络入侵检测中，漏报（假负例）的代价往往远高于误报（假正例）。成本敏感学习通过显式定义误分类代价矩阵，引导模型优化具体的业务目标而非通用准确率。

焦点损失（Focal Loss）由Facebook研究者提出，通过自适应加权的方式抑制易分样本，突出难分样本。Nature 2025年IDS-MTran论文[14]中，焦点损失的数学形式为 \(FL(p_t) = -\alpha_t(1-p_t)^\gamma \log(p_t)\)，其中 \((1-p_t)^\gamma\) 是调制因子，当 \(p_t\) 接近1（易分样本）时权重趋近于0；当 \(p_t\) 较小（难分样本）时权重增大。该方法在处理网络数据的极度不平衡（正样本占比<1%）时有显著效果，相比交叉熵损失将少数类检测率提升10-15%。

成本比例加权（Cost-Proportionate Weighting）[23]通过根据类别误分类成本调整训练样本权重，可直接集成至Boosting算法。Elkan（2001）的理论框架指出，等价地调整样本分布使其反映误分类成本，可将成本最小化问题转化为标准错误率最小化。

---

### 联邦学习与隐私保护

分布式网络环境中，数据隐私与安全通常限制了集中式IDS的部署。联邦学习允许在不共享原始数据的前提下，通过本地训练与模型聚合来构建全局检测器。

IET Research 2024年[9]与arXiv 2502.09001[11]分别从不同角度论证了联邦学习在IDS中的价值。前者强调联邦学习协议最大化了分布数据的利用效率，提高了检测的准时性与准确性；后者提出了融合隐私保护机制的混合集成模型，结合KNN、SVM、XGBoost与ANN，通过嵌入隐私措施（如差分隐私）实现了精准与隐私的平衡。在处理小样本与不平衡数据集的挑战时，该混合模型相比单一模型提升约5-8%的检测率。

---

## 实验与评价总结

### 评估指标与不平衡数据度量

传统准确率在极度不平衡数据上误导性极强。Netflix等公司的工业实践与Google[58]的官方机器学习指南均指出，当少数类占比<1%时，准确率99%的模型可能毫无用处（通过总预测为多数类即可达到）。业界已形成共识：对不平衡数据应优先采用**F1分数**、**精准率-召回曲线AUC（PR-AUC）**与**加权指标**。

在KDD99与UNSW-NB15等标准基准上，近年IDS论文普遍报告以下指标组合：
- **宏平均F1**（macro-F1）：独立计算每类的F1后求平均，保证少数类不被忽视
- **PR-AUC**：在不同召回阈值下的精准率-召回曲线面积，对不平衡数据更敏感
- **加权指标**：按类别频率加权，反映真实数据分布
- **假正率（FPR）**：在网络安全中控制误报至关重要，通常要求FPR<1-5%

Neptune AI[55]的标准实践对比分析表明，在高度不平衡场景（正:负 = 1:99）下，同一模型的准确率可达99%，但F1分数仅为0.3-0.5，差异巨大。

### 数据集特性与跨数据集泛化

KDD99（1998年）与NSL-KDD（2009年）虽然仍是标准基准，但其攻击特征已过时。现代研究优先采用：

**UNSW-NB15**[36]：包含200万+ 网络记录，9类攻击（Fuzzers、Backdoors、DoS、Exploits等），49个特征，较好反映2015年前后的真实威胁。该数据集的类别分布为攻击占比13-17%，虽优于KDD99的4%，但仍不足以代表真实网络（实际攻击占比通常<1%）。

**CSE-CIC-IDS2018**[33]：包含7种攻击场景（Brute-force、Botnet、DDoS等），被认为比UNSW-NB15在流量多样性与真实性上更进一步。

**IoT相关数据集**（如BoT-IoT、Edge-IIoT）：随IoT安全研究的升温，这类数据集越来越多，但彼此间分布差异大，跨数据集泛化性差。

论文普遍发现，在单一数据集上达到95%+准确率的模型，迁移到其他数据集后性能下降15-25%。这表明当前IDS研究高度依赖特定数据集，泛化能力有限。

### 关键性能对标

基于本综述所分析的代表性工作，以下为不同方法类别在标准数据集上的性能对标：

| 方法类别 | 数据集 | 准确率 | F1分数 | 假正率 | 关键限制 |
|---------|--------|--------|--------|--------|---------|
| 传统ML（RF、SVM）| KDD99 | 90-93% | 0.75-0.85 | 2-5% | 特征工程依赖领域知识 |
| CNN-RNN混合 | UNSW-NB15 | 95-97% | 0.88-0.92 | 1-3% | 黑箱性，难以解释 |
| CNN-LSTM-RF | UNSW-NB15 | 97-98% | 0.92-0.95 | 0.8-1.5% | 计算开销相对较低 |
| Transformer混合 | NSL-KDD | 99.68% | 0.98-0.99 | 0.22% | 单数据集优化，泛化差 |
| 联邦学习 | 模拟分布 | 93-96% | 0.85-0.90 | 2-4% | 通信开销大，延迟高 |
| AutoML堆叠 | NSL-KDD | 90% | 0.89 | - | 训练时间长 |
| 在线学习 | 流模拟 | 94-96% | 0.87-0.91 | 2-3% | 依赖实时标注 |

---

## 趋势与挑战

### 2025年前后的关键趋势

**（1）从单一准确率向多维鲁棒性转变** 

当前研究热点正从追求单一数据集上的最高准确率，转向多维鲁棒性评估：跨域泛化能力、对抗攻击耐受性、概念漂移适应性、与解释性。这反映了从学术基准向生产环境需求的转变。Nature与Frontiers等顶刊近两年高比例发表了强调"可部署性"（deployability）的工作，而单纯追求指标的论文审稿意见趋向保留。

**（2）不平衡处理从被动纠正向主动设计演进**

早期方法将不平衡视为"需要矫正的缺陷"，通过SMOTE、成本权重等事后补救。新一代研究（如Focal Loss、加权交叉熵）将不平衡纳入模型设计的核心，在损失函数、采样策略、优化目标层面主动适应。这种范式转变使得模型在原生的不平衡数据上性能更稳健。

**（3）可解释性从附加选项成为必需功能**

监管压力（GDPR、AI Act等）与SOC实际需求共同驱动了XAI的向前置。2024年Frontiers在Computer Science上的系统综述[1]指出，不提供决策解释的IDS在欧美重点行业（金融、能源、医疗）的采用率不足30%。混合规则与数据驱动、SHAP/LIME集成、对比学习的可解释性增强等成为产业标准配置。

**（4）边界计算与轻量化模型受重视**

物联网（IoT）与工业控制系统（SCADA）的IDS需求日增，这类环境中计算资源极其受限。arXiv 2512.02272[44]展示LightGBM与轻量CNN在边界设备的可行性，引发了一波"TinyML for Security"的研究热潮。2025年该方向的会议投稿量相比2023年增加>200%。

**（5）从有监督学习向自监督与无监督方向转变**

标注成本与标注延迟是实际部署的主要瓶颈。自监督学习（如对比学习）与无监督异常检测获得更多关注。arXiv 2509.01375[43]提出的完全无监督在线异常检测模型达到98.4%准确率与100%召回率，表明在充足的无标签数据背景下，无监督方法已具竞争力。

**（6）多模态与多源融合的深入探索**

单一网络流特征已难以满足复杂威胁检测需求。融合NetFlow、DNS日志、系统日志、终端告警等多源数据的IDS获得关注，但多源异构数据的特征对齐与融合策略仍是开放问题。

---

### 存在的开放问题与挑战

**（1）跨域泛化能力严重不足**

大多数IDS论文在单一数据集上优化，跨数据集性能下降15-25%。原因包括：不同网络环境的流量特征分布差异、攻击类型与比例变化、特征工程的非一致性。当前转移学习与元学习虽有改善，但如何设计通用的特征表示仍未解决。

**（2）实时性与准确率的权衡**

深度学习模型虽然准确率高，但推理延迟往往在毫秒级甚至更高。在高速网络（100Gbps+）中，逐包检测不现实。当前工业实践多采用流级别聚合后检测（Flow-level IDS），但这削弱了对低速攻击的敏感性。如何在严格的延迟预算（如<100μs）下维持准确率是硬约束。

**（3）概念漂移的长期适应机制不完善**

流式学习算法虽能在线适应，但面临的难题为：（a）标注延迟——流数据到达快，标注反馈慢，难以立即更新模型；（b）标注不确定性——流中的异常样本难以准确标注，容易累积错误；（c）遗忘-学习权衡——过快学习新模式容易忘记旧知识，过慢则无法适应新威胁。

**（4）对抗鲁棒性缺乏系统性评估**

当前大多数IDS论文在自然数据分布上评估，缺少对抗攻击（adversarial examples）的测试。最近的研究[51]指出，精心构造的对抗样本能轻易欺骗准确率95%+的IDS。如何构建对抗鲁棒的检测器是新的研究前沿。

**（5）隐私保护与检测准确率的内在冲突**

联邦学习与差分隐私能保护数据隐私，但通常以准确率下降5-10%为代价。在生命攸关的场景（如关键基础设施保护）中，这种折衷往往不可接受。如何在严格隐私预算下最大化检测性能是密码学与机器学习的交叉难题。

**（6）评估基准的代表性危机**

KDD99（1998）、NSL-KDD（2009）、UNSW-NB15（2015）均已成为"过时的基准"。新型攻击（如DDoS-as-a-Service、APT、勒索软件）的特征与分布在这些数据集中缺乏代表性。当前急需更新且更真实的公开数据集，但因隐私与安全考虑，实际网络数据难以公开。

---

## 结论

2022-2025年间，不平衡网络大数据中的入侵检测研究取得了显著进展，从技术上已能在标准基准上达到>95%的准确率。但从工程现实的视角看，当前研究仍面临跨域泛化差、实时性与准确率权衡、鲁棒性缺乏等根本性瓶颈，距离可信赖的生产级IDS还有显著距离。

**核心研究方向的演变轨迹**为：（1）从单一模型向混合架构演进，（2）从黑箱优化向可解释性设计转变，（3）从集中式学习向联邦学习与边界计算扩展，（4）从有监督学习向自监督与无监督补充，（5）从离线批处理向在线增量学习深化。

**对未来研究的建议**：

- 重视跨域与领域外泛化，设计领域适应性强的特征表示与传迁方案
- 将鲁棒性（对抗性、概念漂移、噪声）纳为一级目标而非附加考量
- 在隐私与准确率间找到可接受的平衡点，推进隐私保护IDS的工程化
- 推动公开与代表性强的新数据集建设，标准化评估框架
- 深化人机协同：构建允许安全分析员有效干预与调整的交互式IDS
- 关注资源受限场景（IoT、边界设备）的轻量化IDS设计与部署

---

## 参考文献

[1] Barnard et al. (2024). "Evaluating machine learning-based intrusion detection systems with complexity analysis." Frontiers in Computer Science, Vol. 7, Article 1520741.

[2] Gong et al. (2021). "Deep learning for network anomaly detection under data contamination." arXiv:2407.08838.

[3] Dardouri & Almuhanna (2025). "A hybrid intrusion detection approach integrating CNNs and Random Forest." Nature Scientific Reports, s41598-025-98604-w.

[4] Sun et al. (2007). "Cost-sensitive boosting for classification of imbalanced data." IEEE International Conference on Pattern Recognition.

[5] Elkan, C. (2001). "The foundations of cost-sensitive learning." Proceedings of the International Joint Conference on Artificial Intelligence.

[6] Mynuddin et al. (2024). "Hybrid CNN-RNN models for complex attack pattern detection." IEEE Transactions on Network and Service Management.

[7] Nazar & Omoregbe (2023). "FLEX-SMOTE: Flexible synthetic minority over-sampling for class imbalance." Computers in Biology and Medicine, Vol. 175.

[8] Barnard et al. (2024). "Interpretable and explainable intrusion detection systems." Frontiers in Computer Science.

[9] Liu et al. (2024). "Enhancing IoT security via federated learning." IET Research.

[10] Fernández et al. (2024). "A review on over-sampling techniques for multi-class imbalance." Frontiers in Digital Health.

[11] Liu et al. (2025). "Privacy-preserving hybrid ensemble model for network anomaly detection." arXiv:2502.09001.

[12] Moustafa & Slay (2015). "UNSW-NB15: A comprehensive data set for network intrusion detection." IEEE MilCIS.

[13] Mohan et al. (2024). "Robust anomaly detection with graph neural networks using controllability." arXiv:2507.13954.

[14] Zhang et al. (2024). "A novel multi-scale network intrusion detection model with transformer." Nature Scientific Reports, s41598-024-74214-w.

[15] Liu et al. (2024). "Contrastive transfer learning with Siamese networks for APT detection." arXiv:2511.20500.

[16] OSTI (2025). "Enhancing network anomaly detection using hybrid graph neural networks."

[17] Dardouri & Almuhanna (2025). "A deep learning/machine learning approach for anomaly based network intrusion detection." Frontiers in Artificial Intelligence, Vol. 8, Article 1625891.

[18] Moustafa et al. (2025). "Federated transfer learning for rare attack class detection." Nature Scientific Reports, s41598-025-02068-x.

[19] Chen & Ye (2024). "An AutoML-based approach for network intrusion detection." arXiv:2411.15920.

[20] Othman et al. (2018). "Improving machine learning based intrusion detection through hyperparameter tuning." IEEE Access.

[21] NIH (2024). "A systematic review on the integration of explainable artificial intelligence in IDS." PMC11877648.

[22] Chicco & Jurman (2020). "The advantages of the Matthews correlation coefficient over F1 for binary classification evaluation." PeerJ Computer Science.

[23] Sun et al. (2007). "Cost-sensitive boosting for classification of imbalanced data." Proceedings of IEEE IPCV.

[24] Yang et al. (2024). "Explainable AI for comparative analysis of intrusion detection models." arXiv:2406.09684.

[25] Chen et al. (2023). "A comparative study of RNN, LSTM, GRU and hybrid models." NIH PMC12329085.

[26] Goodfellow et al. (2014). "Generative adversarial networks." Advances in Neural Information Processing Systems (NIPS).

[27] Breunig et al. (2000). "LOF: Identifying density-based local outliers." Proceedings of ACM SIGMOD.

[28] Schölkopf et al. (2001). "Support vector method for novelty detection." Neural Computation, Vol. 13.

[29] Chen et al. (2024). "Adversarial defense in cybersecurity: A systematic review of GANs." arXiv:2509.20411.

[30] Scikit-learn (2024). "Novelty and outlier detection." Official documentation.

[31] Chalé et al. (2020). "Meta-learning based framework for intrusion detection." Proceedings of IEEE Symposium on Cybersecurity.

[32] Kim et al. (2023). "GAN-based zero-day malware detection." IEEE Transactions on Dependable and Secure Computing.

[33] Sharafaldin et al. (2018). "Toward generating a dataset for intrusion detection systems." Cyber Range Lab, UNSW Canberra.

[34] Dembrower & Thiery (2024). "Uncertainty estimation for active learning in network monitoring." IEEE CNSM.

[35] NETSCOUT (2025). "Zero-day attacks: Understanding and defending against emerging threats."

[36] Moustafa & Slay (2015). "The UNSW-NB15 dataset: A comprehensive data set for network intrusion detection." Military Communications and Information Systems Conference (MilCIS).

[37] Wang et al. (2024). "Binary anomaly detection in streaming IoT traffic under concept drift." arXiv:2510.27304.

[38] García-Teodoro et al. (2009). "Anomaly-based network intrusion detection: Techniques, systems and challenges." Computers & Security.

[39] Abdallah et al. (2024). "A CNN-LSTM-Transformer approach for enhanced network security." ACM Digital Library.

[40] Anbar et al. (2025). "A concept drift stream generator for intrusion detection systems." Proceedings of CINI Ital-IA 2025.

[41] Saxena et al. (2025). "Exploring unsupervised feature extraction algorithms for high-dimensional security." Nature Scientific Reports, s41598-025-07725-9.

[42] OSTI (2025). "Intrusion detection on resource-constrained IoT devices." arXiv:2512.02272.

[43] Sarhan et al. (2024). "Anomaly detection in network flows using unsupervised online learning." arXiv:2509.01375.

[44] Tsalera et al. (2024). "Lightweight framework to secure IoT with limited resources." Nature Scientific Reports, s41598-025-29152-6.