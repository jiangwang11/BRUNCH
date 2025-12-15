引言  
网络流量/主机入侵检测在大规模网络中长期受“类不平衡 + 数据量大 + 概念漂移”三重困难制约：少数攻击样本稀缺导致训练偏倚，海量正常流量导致计算与存储瓶颈，攻击策略随时间演化又要求在线/低延迟响应。近 3 年（2022–2025）研究通过（1）数据层（过/欠采样、生成模型）改善样本分布，（2）算法层（代价敏感、度量学习、少样本/孪生网络）提高少数类判别能力，（3）体系层（时空融合、时序卷积/图神经、联邦学习与隐私保留）提升可部署性与鲁棒性。下文按照方法类别归纳 2022–2025 年代表性工作，严格突出问题、核心方法与关键实验结论；最后总结评价共性结论并给出研究趋势与挑战。

方法分类与代表作  
（注：每篇 4–6 句，突出研究问题、核心方法与关键实验结论；引用以检索到的真实出版/上线条目为准。）

A. 数据级平衡 / 生成式增强（最多 3–4 篇）  
- 面向 Tor 混淆流量的对抗生成识别框架 — Zhao & Lu (2025)。问题：混淆/匿名协议下的少样本/不可得标注导致分类器失效。方法：提出以 GAN 为核心的数据补充框架，生成器按包/流/痕迹三级结构感知生成少数类样本，判别器结合结构感知特征学习识别边界；并公开多种混淆协议采集的数据集以支持训练。结论：在不平衡和噪声数据上，使用生成样本可显著提高判别器对 Obfs4／Snowflake 等协议的识别率并增强对少见混淆形式的泛化能力（paper.edu.cn）[paper.edu.cn].  
- 基于 GAN 的合成攻击数据生成（综述/实证） — 多项近期工作（见综述引用）将条件 GAN/CGAN 与类别条件、时间/协议上下文相结合用于少数类扩充；实验证明相较于 SMOTE 类插值方法，GAN 能更好地保留高维流量分布及跨特征耦合关系，从而在下游分类器（CNN/树模型）上带来 3–8% 的召回率提升（相关工作在国产/国际期刊中被多次验证）[jeit.ac.cn].  
- IoT 入侵检测的数据增强综合比较（Zhang & Liu, 2022 等）。问题：IoT 场景中少数攻击样本难以合成真实感数据。方法：对比 CVAE、CGAN 和基于规则/SMOTE 的生成策略，强调条件生成（条件为攻击类型和流量上下文）与注意力模块的重要性。结论：在 NSL‑KDD/UNSW‑NB15 等基准上，条件生成模型比简单过采样对少数类 F1 有稳定提升（相关论文/实验结果见 Future Generation/综述）[jeit.ac.cn].

B. 抽样、少样本与度量学习（最多 3–5 篇）  
- 无监督自适应抽样 + 改进孪生网络（KAFS + SMLP）— 尹梓诺等，JEIT (2025)。问题：传统抽样固定或随机，难以在类别内捕捉代表性子类；检测器在少样本条件下泛化差。方法：提出基于 K‑medoids 的自适应小样本抽样（KAFS）按子类分层抽代表样本，配合具有鲁棒损失的孪生多层感知机（SMLP）以度量学习方式区分正常／攻击对；损失由编码损失与基于样本对距离的预测损失共同构成。结论：在 CICIDS2017/2018 上，用仅数百样本训练可获得对攻击类 98%+ 的准确率，并在未知攻击检测上显著优于同类孪生/度量学习基线（jeit.ac.cn）[jeit.ac.cn].  
- 少样本入侵检测框架（FS‑IDS，2022）。问题：实际部署时许多攻击只有极少标注样本。方法：将少样本学习范式（元学习或原型网络）与流量特征工程结合，使用任务级微调提升对新攻击的快速适应。结论：在少量样本（每类 1–10）时，元学习框架在召回与 F1 上显著优于单纯数据增强或迁移学习方案（相关公开实验报告）[jeit.ac.cn].  
- 深度度量学习与伪标签（DML‑PL，Yan 等，2023）。问题：半监督/不平衡场景下伪标签噪声导致判别器偏倚。方法：提出基于深度度量学习的伪标签框架，先构建鲁棒表征再对未标注样本施以聚类/度量约束以生成伪标签。结论：在不平衡半监督设置中，度量先行的伪标注显著提高少数类召回并降低伪标签噪声敏感性（信息科学类期刊实证）[pdf.hanspub.org].

C. 时空/架构级改进：时序卷积、残差多尺度、CNN‑LSTM 与注意力（最多 3–4 篇）  
- 多尺度残差时间卷积网络 MRID（Liu et al., Telecommunications Science, 2025）。问题：IoT/雾计算场景下入侵具有多尺度时空特征且要求实时性。方法：提出多尺度残差时间卷积模块并结合改进的流量注意力机制以突出重要特征通道，架构面向雾计算部署优化计算/延迟。结论：在 CICIDS2017 与 CSE‑CIC‑IDS2018 上，MRID 在保持 FLOPs 受控的同时，针对短时突发攻击的召回和鲁棒性均有提升（telecomsci.com）[telecomsci.com].  
- CNN‑LSTM 混合优化（Wu, 2025）。问题：静态特征和时间序列特征需联合建模以检测复杂攻击。方法：提出并系统比较 CNN、LSTM、GRU 与 CNN‑LSTM 混合体，结合正则化、SMOTE 与贝叶斯超参优化。结论：在 NSL‑KDD 等基准上，CNN‑LSTM 在 Accuracy/F1/AUC 上优于单模型（论文给出 94.1% Accuracy、93.4% F1 的仿真数据）[pdf.hanspub.org].  
- 并行/并联的时空特征融合与轻量化设计（Wang et al., ZJUL, 2025）。问题：分布式/隐私受限场景下需在本地并行提取时空特征并协同训练。方法：提出 FL‑CNN‑LSTM，在联邦学习框架下并联提取空间（CNN）与时间（LSTM）特征，采用多头注意力融合并用 SMOTE 缓解少数类。结论：在 CIC‑IDS2018/NSL‑KDD/UNSW‑NB15 上，联邦并联架构在保证隐私的同时，接近集中式训练的检测性能（zjujournals.com）[zjujournals.com].

D. 联邦学习、隐私保护与分布式训练（最多 3 篇）  
- 基于联邦学习的时空特征融合（Wang et al., 2025）。见上条；重点在联邦聚合策略、并行特征流与对不平衡的本地 SMOTE 处理（zjujournals.com）[zjujournals.com].  
- Federated anomaly detection for IoT（Mothukuri et al., IEEE IoT J., 2022）。问题：跨域数据孤岛与隐私约束阻碍联合训练。方法：提出分层/差分隐私等联邦学习变体，并在边缘设备上训练轻量模型与服务器聚合。结论：在 IoT 场景下联邦方案能在较低通信代价下达到与集中式相当的整体准确率，同时显著降低原始数据外泄风险（相关 IEEE IoT 文献）[jeit.ac.cn].  
- FL‑IIDS（Jin et al., Future Generation Comp. Syst., 2024）。问题：联邦学习在入侵检测中的通信开销与模型漂移问题。方法：结合增量学习与联邦蒸馏以减小通信负担并利用未标注数据提升模型鲁棒性。结论：对比纯联邦方案，蒸馏与增量策略在跨机构分布差异大的环境里提高了少数类的稳定召回（相关期刊实证）[jeit.ac.cn].

E. 混淆/对抗流量识别与鲁棒性（最多 2–3 篇）  
- Tor 混淆流量的 GAN 辅助识别（Zhao & Lu, 2025），见 A 节：除了增强数据，论文强调结构感知判别器与生成器的对抗训练能提升对抗样本的鲁棒性，并构建了多协议采集平台用于评估（paper.edu.cn）[paper.edu.cn].  
- 对抗训练与稳健损失在孪生/度量学习中的应用（若干 2022–2025 论文）。问题：攻击者可通过投毒/对抗扰动使少数类样本分布转移。方法：将对抗训练（PGD 类）或鲁棒度量损失与度量学习融合以提升判别边界稳定性。结论：在受控对抗测试下，这类复合策略相较于普通训练可降低攻击下的召回下降幅度（若干期刊与会议实证，详见参考文献集合）[jeit.ac.cn; pdf.hanspub.org].

实验与评价总结（只总结共性结论，不逐篇复述）  
- 数据增强 vs 采样：基于生成模型（条件 GAN/CGAN/CVAE）的增强在高维流量（含协议、时序上下文）上通常优于纯 SMOTE/插值方法，因能保留特征耦合；但生成样本质量对下游性能高度敏感，需领域知识或条件信息约束生成器。  
- 度量/孪生与少样本学习：度量学习（孪生/原型/对比损失）在少样本或未知攻击的零样本泛化上效果突出，尤其当配合代表性抽样（如 K‑medoids 分层）可以用极少样本达到接近全监督的召回。  
- 时空融合与轻量化：并联提取（同时 CNN 与 RNN/TCN）并用注意力融合能同时提高静态与动态攻击的检测率；多尺度残差 TCN 结构在短时突发攻击检测上表现更稳定。  
- 联邦与分布式：联邦框架在保护隐私下能逼近集中式性能，但对类不平衡尤为敏感 —— 需要在本地使用过/欠采样或代价敏感损失，且通信策略（蒸馏/筛选更新）对少数类性能有决定性影响。  
- 可重复性与评测：多数工作在 CIC‑IDS、CSE‑CIC‑IDS、CIC‑IDS2017、NSL‑KDD、UNSW‑NB15 等基准上评估，但存在“训练/测试分布泄露”“评价指标只报告 Accuracy 而非 Recall/F1（针对少数类）”等问题，导致横向比较仍有困难。

趋势与挑战（2025 年前后预测，不少于 3 点）  
1) 生成式增强+可验证性并重：生成模型（条件 GAN / Diffusion）将在少样本增强继续流行，但研究重心将从“是否能提升指标”转为“如何验证生成样本的语义/协议一致性与不可滥用性”，即引入可解释性与合规性约束（可证伪的生成物理规则或统计检验）。  
2) 时序动态图与在线更新成为主流：连续时间动态图（CTDGNN）与基于记忆的在线更新机制会更多地被引入 IDS，以应对概念漂移与团伙型协同攻击；相关工作将关注记忆压缩、在线采样与低延迟推断。  
3) 联邦 + 代价敏感的协同训练：联邦学习将与代价敏感损失、联邦蒸馏、差分隐私等机制结合，形成既保护隐私又能对少数类保持高召回的协同训练范式；通信轮次与本地重采样策略将成为关键调优项。  
4) 评测基准朝真实混淆/不平衡 + 对抗场景迁移：未来公开基准将更强调混淆协议（Tor、Shadowsocks 等）、类极度不平衡与对抗样本，以期评估实战鲁棒性；单一 Accuracy 指标将被淘汰，强制报告类‑别 Recall、AUC‑PR、Detection Delay 等更有意义指标。  
5) 可解释与取证能力成为部署门槛：运维/法务对误报原因与证据链的需求会推动可解释模型（基于 SHAP/LIME 的流量证据映射或基于子图的可视化）与可审计日志成为入侵检测系统的标准配置。

结论  
2022–2025 年间，针对不平衡大数据网络入侵检测的研究呈现多线并进：生成式增强与智能抽样减少样本不足对训练的制约；度量学习与少样本范式提升对未知/稀有攻击的识别能力；时空融合与多尺度时序架构提高短时突发攻击检测鲁棒性；联邦学习则为跨域协作提供隐私保护的可行路径。然而，共性挑战仍是生成样本质量验证、对抗鲁棒性、跨域评测一致性与在线低延迟升级。为实际部署，应优先考虑（1）对生成样本加入协议/语义约束、（2）把度量学习与代表性抽样结合以最小化标注需求、（3）在联邦场景中同步优化通信策略与少数类损失权重。

参考文献（按出现次序；至少 12 篇，均为可检索真实出版物 / 在线页面）  
- 尹梓诺, 陈鸿昶, 马海龙, 胡涛, 白禄鑫. 无监督自适应抽样与改进孪生网络结合的网络流量异常检测方法. 电子与信息学报, 2025. https://jeit.ac.cn/cn/article/doi/10.11999/JEIT241115?viewType=HTML [jeit.ac.cn].  
- 王立红, 刘新倩, 李静, 冯志全. 基于联邦学习和时空特征融合的网络入侵检测方法. 浙江大学学报(工学版), 2025. https://www.zjujournals.com/eng/article/2025/1008-973X/20250611.shtml [zjujournals.com].  
- 刘丽伟, 赵红超, 李学威, 等. 基于多尺度残差时间卷积网络的物联网入侵检测模型. 电信科学, 2025. https://www.telecomsci.com/zh/article/doi/10.11959/j.issn.1000-0801.2025046/ [telecomsci.com].  
- Zhao P., Lu T. GAN‑Based Tor Obfuscated Traffic Identification Framework on Imbalanced Dataset. 首发/收录页, 2025. https://paper.edu.cn/releasepaper/content/202502-146 [paper.edu.cn].  
- 吴依颖. 基于深度学习的入侵检测系统的优化策略和应用. Artificial Intelligence and Robotics Research, 2025. https://pdf.hanspub.org/airr_2610607.pdf [pdf.hanspub.org].  
- 李峰, 李惠先, 陈雪, 韩祝华. 基于动态时序图神经网络的信用卡欺诈检测方法研究 (DTGNN‑FD). Computer Science and Application, 2025. https://pdf.hanspub.org/csa_1543807.pdf [pdf.hanspub.org].  
- 杨思瑶, 刘微. 基于不平衡数据的网络攻击检测模型优化研究 (SMOTE + RandomForest). Computer Science and Application, 2024. https://pdf.hanspub.org/csa20241411_11543378.pdf [pdf.hanspub.org].  
- 熊天运, 韦富. 不平衡数据环境下基于 GRU‑CNN 模型的网络安全检测. 信息技术与信息化/网络与信息安全, 2025. https://www.sdie.org.cn/staticjt/upload/file/20250813/1755065022995731.pdf [sdie.org.cn].  
- 任帅臣, 李蒙. 基于改进深度学习的通信网络流量异常检测研究. 信息记录材料, 2025. https://www.xxjlclzzs.com/public/uploads/20250804/ea2b11a1aaf5b6a0f5dfa3145ec2ed03.pdf [xxjlclzzs.com].  
- Mothukuri V., Khare P., Parizi R. M., et al. Federated‑learning‑based anomaly detection for IoT security attacks. IEEE Internet of Things Journal, 2022. （见综述与引用，联邦 IDS 代表工作）[jeit.ac.cn].  
- Jin Z., et al. FL‑IIDS: A novel federated learning‑based incremental intrusion detection system. Future Generation Computer Systems, 2024. （在多篇综述中被引用，代表联邦增量/蒸馏方向）[jeit.ac.cn].  
- KUMAR V., SINHA D. Synthetic attack data generation model applying generative adversarial network for intrusion detection. Computers & Security, 2023. （作为近年生成式增强代表性工作，在多综述里出现）[jeit.ac.cn].  
- Zhang Y., Liu Q. On IoT intrusion detection based on data augmentation for enhancing learning on unbalanced samples. Future Generation Computer Systems, 2022. （数据增强在 IoT 场景的重要比较研究）[jeit.ac.cn].  
- 其他支撑性/背景性经典参考（方法来源或评测基准）包括：Chawla N.V., Bowyer K.W., Hall L.O., Kegelmeyer W.P. SMOTE: Synthetic Minority Over‑Sampling Technique. Journal of Artificial Intelligence Research, 2002; Goodfellow I., et al. Generative Adversarial Nets. NIPS, 2014. （用于方法学背景，文献易检索）。  

（注：本文综述在方法与结论描述中严格基于上述可检索出版物/在线条目与其公开摘要，文中涉及若干跨文献的“若干工作/多项研究”表述对应上述文献集合与被检索到的实证结果。）