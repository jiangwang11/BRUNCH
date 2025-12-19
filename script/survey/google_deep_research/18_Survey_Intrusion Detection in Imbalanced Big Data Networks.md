不平衡大数据网络环境下的入侵检测技术综述：2022–2025年进展与趋势
1. 引言
1.1 研究背景：大数据与网络安全的博弈
随着第五代移动通信技术（5G）、物联网（IoT）以及工业互联网（IIoT）的全面普及，全球网络空间的数据流量正经历着爆炸式的增长。网络环境的边界日益模糊，连接设备的异构性与海量数据的实时性为网络安全防御体系带来了前所未有的挑战。在大数据背景下，网络流量不仅表现出传统的“3V”特征（Volume, Velocity, Variety），更在安全维度上呈现出极端的分布不平衡性。传统的入侵检测系统（Intrusion Detection Systems, IDS）在面对海量、高维且动态变化的流量数据时，往往显得力不从心，特别是在识别隐蔽性极强的高级持续性威胁（APT）和零日攻击（Zero-day Attacks）方面，现有的检测模型面临着高漏报率（False Negative Rate）的严峻考验 。   

大数据环境下的网络入侵检测核心难点在于“大海捞针”。在真实的骨干网或企业边缘网关中，正常的业务流量占据了绝大多数（通常超过99.9%），而恶意的攻击流量，尤其是新型或针对特定目标的攻击，仅占极小比例。这种严重的数据偏斜（Data Skewness）导致了机器学习领域经典的“类别不平衡问题”（Class Imbalance Problem）。当训练数据极度不平衡时，大多数监督学习算法（如深度神经网络、随机森林等）为了最小化全局损失函数，会倾向于过度拟合多数类（正常流量），从而忽略少数类（攻击流量），导致模型对攻击样本的识别能力极弱，甚至完全失效 。   

1.2 2022–2025年技术演进概览
回顾2022年至2025年的学术界与工业界研究成果，针对不平衡大数据环境的入侵检测技术经历了一次深刻的范式转移（Paradigm Shift）。早期的研究（2022-2023）主要集中在传统的过采样技术（如SMOTE及其变体）与轻量级深度学习模型的结合上。然而，随着生成式人工智能（Generative AI）的爆发，2024年至2025年的研究前沿迅速转向了基于生成对抗网络（GANs）和扩散模型（Diffusion Models）的高保真数据增强技术。此外，大语言模型（LLMs）的引入为IDS赋予了语义理解与逻辑推理能力，使得入侵检测从单纯的“模式匹配”走向了“认知对抗”的新阶段 。   

本综述旨在对这一快速发展的领域进行详尽的梳理与深度分析。报告将涵盖以下核心维度：

数据级增强方法的革新：从传统的插值算法向基于扩散模型的复杂分布生成演进。

算法级与混合架构的突破：代价敏感学习、元学习（Meta-Learning）以及Transformer与GAN的协同架构。

分布式与隐私保护机制：联邦学习在异构、不平衡数据环境下的动态采样策略。

认知型检测系统的兴起：基于Agent的大模型入侵检测与可解释性研究。

通过对 CICIDS2017、CICIoT2023、UNSW-NB15 以及 InSDN 等权威基准数据集上的实验结果进行横向对比与纵向分析，本报告将揭示各类方法在处理不平衡大数据时的优势与局限，并展望2025年及未来的技术发展趋势。

2. 核心挑战与数据集演变
2.1 类别不平衡的数学本质与影响
在网络入侵检测任务中，数据集 D 通常由 N 个样本组成，即 D={(x 
i
​
 ,y 
i
​
 )} 
i=1
N
​
 ，其中 x 
i
​
  是高维流量特征向量，y 
i
​
 ∈{0,1,...,K} 是类别标签（0代表正常，其他代表不同类型的攻击）。不平衡性体现在不同类别的先验概率 P(y) 差异巨大。对于少数类 C 
min
​
  和多数类 C 
max
​
 ，往往存在 ∣C 
max
​
 ∣≫∣C 
min
​
 ∣，甚至不平衡比率（Imbalance Ratio, IR）可达 1000:1 以上。

这种不平衡性对标准分类器造成了根本性的偏差：

决策边界偏移：分类器会将决策边界推向少数类一侧，以压缩少数类的空间来换取整体准确率（Accuracy）的提升。

特征掩盖：在大数据的高维特征空间中，稀疏的攻击样本特征容易被海量正常样本的噪声所淹没，导致模型难以学习到鲁棒的攻击特征表示 。   

2.2 数据集的迭代：从KDD99到CICIoT2023
数据集的质量直接决定了IDS研究的有效性。2022-2025年的文献显示，学术界已基本摒弃了过时的 KDDCup99 和 NSL-KDD 数据集，转而采用更能反映现代网络流量特征（如加密流量、IoT协议、SDN控制流）的新一代数据集。

CICIDS2017 / CSE-CIC-IDS2018：这两个数据集因其包含完整的网络拓扑结构和多样化的攻击类型（如Brute Force, DoS, Web Attack, Infiltration），依然是2024-2025年研究中最广泛使用的基准。尽管如此，研究指出 CICIDS2017 存在严重的内部类别不平衡，例如 Heartbleed 攻击样本极少，这对模型提出了极高要求 。   

CICIoT2023：作为针对大规模物联网环境设计的最新数据集，CICIoT2023 包含了33种攻击类型，数据规模庞大，且类别分布极度不均。它是评估大规模、多分类不平衡处理能力的首选数据集 。   

InSDN (2020)：针对软件定义网络（SDN）环境的专用数据集，涵盖了控制平面和数据平面的特定攻击（如针对控制器的饱和攻击）。Shamim 等人 (2025) 的研究特别强调了在该数据集上解决不平衡问题的紧迫性 。   

Edge-IIoTset & TON_IoT：这两个数据集专注于工业物联网和边缘计算场景，包含了来自Modbus等工业协议的流量，体现了异构数据源的融合特征 。   

3. 数据级解决方案：生成式AI的统治
解决不平衡问题最直观的策略是改变训练数据的分布，即数据增强（Data Augmentation）。2022年至2025年，这一领域经历了从传统的几何插值（SMOTE）向深度生成模型（GANs, Diffusion）的跨越式发展。

3.1 传统过采样技术的边缘化与适应
尽管深度学习已占据主导地位，但合成少数类过采样技术（SMOTE）及其变体（如 ADASYN, Borderline-SMOTE）在2024-2025年并未完全退出历史舞台，而是演变为轻量级框架中的预处理组件，或是与深度模型结合的辅助手段。

Ismail, Dandan & Qushou (2025) 在 IEEE Access 上发表的研究展示了传统方法在资源受限环境下的生命力。针对 IoT 和 IIoT 环境（使用 TON_IoT 和 Edge-IIoTset 数据集），该研究对比了决策树、随机森林、XGBoost 和 LightGBM 等轻量级模型。为了处理数据不平衡，作者采用了 SMOTE 进行预处理。实验结果表明，在经过 SMOTE 平衡后，LightGBM 模型在保证极低推理延迟（适用于边缘设备）的同时，实现了 99.95% 的准确率和极高的 F1-Score 。这表明，在算力受限的边缘节点，"SMOTE + 高效集成树模型" 依然是极具性价比的解决方案。   

然而，Kumar 等人 (2025) 指出了 SMOTE 在处理高维、复杂分布数据时的本质缺陷：SMOTE 基于线性插值生成样本，容易在特征空间的重叠区域引入噪声，且无法捕捉数据的流形结构（Manifold Structure），导致生成的样本缺乏多样性与真实感 。   

3.2 生成对抗网络（GANs）：成熟与细分
生成对抗网络（GAN）通过生成器与判别器的零和博弈，能够逼近真实数据的潜在分布。在2022-2025年间，GAN已成为解决IDS数据不平衡的主流技术，研究重点从简单的 Vanilla GAN 转向了针对特定网络环境的定制化架构。

3.2.1 针对SDN环境的特征选择与GAN协同
软件定义网络（SDN）的集中式控制平面是攻击的高价值目标。Shamim 等人 (2025) 提出了一种专为 SDN 环境设计的 GAN 基 IDS 系统。

方法论：该研究并没有直接将原始流量输入 GAN，而是先利用卡方检验（Chi-square test）从 InSDN 数据集的80+特征中筛选出最具区分力的48个特征。这一步至关重要，因为它降低了 GAN 训练的模态坍塌（Mode Collapse）风险。随后，定制的 GAN 架构被用于生成稀疏攻击类型的合成流量记录。

实验评价：在 InSDN 和 CICIDS2017 数据集上的评估显示，该框架不仅在离线分析中表现优异，在实时流量分析中也保持了极高的检测率。特别是结合 XGBoost 分类器时，系统在 InSDN 数据集上达到了 99.95% 的准确率，显著优于未经过 GAN 增强的基准模型 。这一工作确立了“特征降维 + GAN 增强 + 高效分类器”作为处理高维网络流数据的标准范式。   

3.2.2 Transformer-GAN：时空特征的深度融合
传统的 GAN（通常基于 MLP 或 CNN）在处理网络流量的时间依赖性（Temporal Dependencies）方面存在不足。网络攻击往往是一个序列过程，单条数据记录的上下文信息至关重要。 Moghaddam 等人 (2025) 在 Future Internet 和 IEEE Access 上发表的一系列工作，提出了 Transformer-GAN 协同架构 。   

架构创新：该模型创造性地将 Transformer 架构整合进 GAN 的生成器和判别器中。Transformer 的自注意力机制（Self-Attention）使其能够捕捉流量数据中的长程依赖关系和全局上下文。

优化策略：为了解决 Transformer-GAN 训练难收敛的问题，作者引入了一种改进的非支配排序生物地理学优化算法（INSBBO）来动态微调网络的超参数（如学习率、Dropout 率）。

性能突破：在包含33类攻击的 CICIoT2023 数据集上，该模型展现了惊人的性能，多分类准确率达到 99.67%，F1-score 达到 99.61%，AUC 高达 99.80% 。这一结果在多分类不平衡任务中是目前文献报道的最高水平之一，证明了 Transformer 强大的特征提取能力与 GAN 的数据生成能力相结合产生的巨大协同效应。   

3.3 扩散模型（Diffusion Models）：新一代生成范式
尽管 GAN 表现优异，但其训练不稳定性（如梯度消失、模态坍塌）始终是挥之不去的阴影。2024年底至2025年，扩散模型（Diffusion Models）开始在 IDS 领域崭露头角，被视为 GAN 的强力挑战者。扩散模型通过逐步添加噪声再逐步去噪的过程（Stepwise Denoising）来生成数据，理论上能覆盖更完整的数据分布。

3.3.1 LRT-DDPM：打破采样速度瓶颈
扩散模型的主要缺点是采样速度慢，难以满足网络安全的实时性要求。Wang, Wu & Wang (2025) 提出的 LRT-DDPM 模型针对这一痛点进行了重大改进 。   

核心机制 - TACBlock：该研究引入了时间自适应控制块（Time-Adaptive Control Block, TACBlock）。传统的扩散模型在反向采样时使用固定的时间步长，而 TACBlock 能够根据生成过程的阶段动态调整时间步长和噪声权重。这不仅加速了采样过程，还提高了生成样本的保真度。

特征增强：模型结合了带有残差连接的 CNN 来增强对流量特征的提取。

实验结果：在 NSL-KDD 和 CICIDS2017 数据集上，LRT-DDPM 分别实现了 99.40% 和 99.53% 的准确率。更重要的是，相比于 GAN，该模型在生成少数类样本时表现出更好的多样性，有效避免了 GAN 常见的“生成重复样本”问题 。   

3.3.2 Diff-IDS：跨模态的视觉化检测
Yang 等人 (2025) 提出的 Diff-IDS 展示了另一种思路：将一维的表格化网络流量转换为二维灰度图像，利用计算机视觉领域成熟的 U-Net 架构进行处理 。   

方法：通过特征掩码增强算法和图像翻转技术进行数据增强，然后训练一个基于 U-Net 的扩散模型。

意义：这种跨模态（Table-to-Image）的方法利用了卷积神经网络在处理空间相关性方面的优势，实验表明其在检测精度和轻量化指标上均优于传统的 ML 模型，特别是在识别具有明显视觉纹理特征的 DDoS 攻击时效果显著。

3.3.3 DiSMHA：混合增强框架
Kumar 等人 (2025) 提出了 DiSMHA 框架，旨在解决极端类别不平衡问题 。尽管其验证场景为太阳能面板缺陷检测，但其核心思想——“扩散模型提供结构多样性 + SMOTE 提供特征空间离散度”——被证明对通用的不平衡分类问题具有普适性。该研究表明，单一的生成方法往往难以同时兼顾样本的逼真度和特征空间的覆盖率，混合策略（Hybrid Augmentation）将是未来的重要方向。   

4. 算法级与混合架构解决方案
除了数据层面的增强，直接改进学习算法以适应不平衡分布，或设计能够提取更鲁棒特征的混合神经网络架构，也是2022-2025年的研究热点。

4.1 代价敏感学习与多任务优化
Telikani 等人 (2024) 在 IEEE Transactions on Industrial Informatics 上发表的研究提出了一种无需生成合成数据的纯算法解决方案 。   

理论基础：该方法的核心在于代价敏感学习（Cost-Sensitive Learning）。传统的 SVM 或神经网络通常同等对待所有错误，但在入侵检测中，将攻击误判为正常的代价远高于将正常误判为攻击。

模型架构：

特征提取：使用堆叠自编码器（Stacked Autoencoder, SAE）从原始流量中提取高阶隐式特征。

多任务 SVM：后端分类器并非标准的 SVM，而是一个多任务学习框架。

Hinge Loss 改造：通过修改 Hinge Loss 函数，为少数类样本的误分类分配更高的惩罚权重（Cost Matrix）。

实验成效：在 UNSW-NB15 和 BoT-IoT 数据集上，该模型在未进行任何过采样的情况下，平均召回率、精确率和 F1-score 分别达到了 92.2%, 96.2% 和 94.3%。这证明了通过数学层面的优化，模型完全可以在不平衡分布下“学会”关注少数类，且避免了生成合成数据可能引入的分布偏差风险 。   

4.2 元学习（Meta-Learning）：少样本检测的曙光
面对层出不穷的零日攻击，传统的“大数据训练”模式显得滞后。元学习（Meta-Learning），即“学会如何学习”，致力于让模型具备利用极少量样本快速适应新任务的能力。

Xu 等人 (2025) 提出的 MACML（Marrying Attention and Convolution-based Meta-Learning）是这一方向的里程碑式工作 。   

方法论：MACML 结合了自注意力机制（捕捉全局依赖）和 CNN（提取局部特征），构建了一个强大的特征提取器。其核心在于采用了基于优化的元学习框架（Model-Agnostic Meta-Learning, MAML 的变体）。模型在大量不同的攻击任务（Base Tasks）上进行元训练，学习通用的初始化参数。

Few-Shot 性能：当面对从未见过的新型攻击时，MACML 仅需极少的样本（如 5-shot 或 10-shot）进行微调即可达到高性能。

实验数据：在 CICIDS2017 数据集上，仅使用 10 个训练样本，MACML 就实现了 98.75% 的准确率和 99.17% 的检测率。在 CICIoT2023 数据集上，其 5-shot 检测率显著优于 BFS-NID 和 CNN-BiGRU 等对比模型 。这意味着 IDS 可以不再依赖海量标注数据，从而极大缩短了对新威胁的响应周期。   

4.3 混合深度学习架构：Seq2Seq 与 ConvLSTM
为了充分挖掘流量数据的时空特征，Hariharan 等人 (2025) 提出了一种结合 Seq2Seq 和 ConvLSTM 子网的混合模型 。   

架构逻辑：Seq2Seq（序列到序列）模型最初用于机器翻译，能够很好地处理变长输入序列。ConvLSTM 则在 LSTM 单元中引入卷积操作，能够同时提取时间序列特征和空间结构特征。

针对性优化：该模型特别针对 CICIDS2017 进行了调优。实验表明，该混合架构在保持极高检测率（DR=99%）的同时，显著降低了误报率（FAR），在与 LuNET 等模型的对比中展现了更均衡的性能 。   

5. 分布式与隐私保护：联邦学习的新进展
在大数据网络中，数据往往分散在数以亿计的边缘设备上，且涉及用户隐私。将所有数据上传至中心服务器进行集中训练不仅带宽成本高昂，且面临严峻的隐私合规风险。联邦学习（Federated Learning, FL）应运而生，但在不平衡数据（Non-IID）下的性能退化是其主要瓶颈。

5.1 动态采样联邦框架（DS-FedIDS）
Youm & Kim (2025) 针对异构 IoT 环境下的类别不平衡问题，提出了 DS-FedIDS 框架 。   

核心问题：在联邦学习中，如果某些客户端的数据全是正常流量，而另一些全是攻击流量（Non-IID），全局聚合模型（Global Model）会严重偏向拥有更多数据的客户端（通常是正常流量），导致对少数类攻击的识别能力下降。

解决方案：

个性化层（Personalization Layers）：基于 FedPer 架构，保留部分模型层在本地不参与聚合，以适应本地特定的流量模式。

动态上/下采样（Dynamic Up/Down Sampling）：这是该研究的核心创新。每个客户端在本地训练前，会根据自身的数据分布实时计算采样率。如果检测到某类攻击样本稀缺，则自动进行过采样；反之则欠采样。

成效：实验结果显示，DS-FedIDS 在检测 Theft 和 R2L 等稀有攻击类型时，准确率和 F1-score 均显著优于经典的 FedAvg 和 FedPer 算法，证明了“动态采样”是解决联邦学习中数据异构与不平衡问题的有效手段 。   

5.2 区块链与扩散模型的联邦协同
Shamim 等人 (2025) 进一步拓展了联邦学习的边界，提出了结合以太坊区块链与扩散模型的安全 FL 框架 。   

机制：

本地增强：在每个本地节点（Local Node），首先部署扩散模型对本地的少数类样本进行增强。这从源头上解决了数据不平衡问题，使得上传的梯度更新更加均衡。

区块链聚合：利用以太坊智能合约进行模型参数的聚合与分发，确保了模型更新的不可篡改性和可追溯性，防止恶意节点投毒（Poisoning Attacks）。

结果：该框架在 BoT-IoT 数据集上实现了 98.3% 的 F1-score，特别是对零日攻击的检测能力得到了质的提升。这代表了“隐私计算 + 生成式AI + 区块链”融合应用的前沿方向。

6. 认知型 IDS：大语言模型与智能体
2024年底至2025年，大语言模型（LLM）的爆发将 IDS 推向了“认知智能”的高度。传统的深度学习模型即使准确率再高，也只是一个“黑盒”，无法解释“为什么”判定为攻击。

6.1 IDS-Agent：具备推理与解释能力的智能体
Li 等人 (2025) 在 ICLR/NeurIPS 等顶级会议上提出的 IDS-Agent 是目前该方向最具代表性的工作 。   

核心理念：IDS-Agent 不再是一个单纯的分类器，而是一个基于 ReAct（Reasoning-followed-by-Action）框架的智能体。它利用 LLM（如 GPT-4, LLaMA）作为大脑，通过调用工具来完成检测任务。

工作流程：

数据感知：Agent 调用工具提取网络流量特征（如 PCAP 文件解析）。

多模型集成：Agent 指挥多个传统 ML 模型（Random Forest, KNN 等）进行初步判定。

知识检索（RAG）：利用检索增强生成（RAG）技术，Agent 从外部知识库中检索历史攻击案例、CVE 漏洞库或安全白皮书。

认知推理：LLM 综合分类器的概率输出和检索到的知识，进行逻辑推理。例如：“虽然 RF 模型给出的置信度不高，但该流量的特征序列与 CVE-2023-XXXX 的行为模式高度吻合，且源 IP 属于已知的恶意僵尸网络，因此判定为攻击。”

解释输出：最终输出不仅包含标签，还包含一段人类可读的自然语言解释。

实验评价：在 ACI-IoT 和 CIC-IoT 基准测试中，IDS-Agent 的 F1-score 分别达到 0.97 和 0.75。更惊人的是，在面对训练集中未见过的零日攻击时，它实现了 0.61 的召回率，远超传统深度学习模型。这一结果证明了 LLM 的泛化推理能力可以弥补样本缺失的短板，是解决不平衡和未知威胁的终极途径之一 。   

7. 实验评价总结与对比分析
7.1 综合性能对比
为了直观展示不同方法在不平衡数据集上的表现，表 1 总结了 2024-2025 年部分代表性工作在核心基准数据集上的实验结果。

表 1：2024-2025年代表性不平衡入侵检测方法性能对比

模型/方法	核心技术范式	数据集	准确率 (Accuracy)	F1-Score	核心优势	局限性	引用
Transformer-GAN	混合生成式 AI	CICIoT2023	99.67%	99.61%	极高的多分类精度，INSBBO 优化器解决了 GAN 训练不稳定的问题。	计算资源消耗极大，训练时间长。	
LRT-DDPM	扩散模型 (Diffusion)	CICIDS2017	99.53%	High*	样本生成质量优于 GAN，TACBlock 解决了采样速度慢的瓶颈。	推理延迟仍高于轻量级模型。	
GAN-IDS (SDN)	特征工程 + GAN	InSDN	99.95%	~99.9%	针对 SDN 环境优化，特征降维后生成效率高，实时性好。	强依赖于特征选择算法的质量。	
MACML	元学习 (Few-Shot)	CICIDS2017	98.75%	-	少样本适应：仅需 10 个样本即可识别新攻击，无需海量数据。	在极端复杂的混合攻击下泛化性待验证。	
LightGBM + SMOTE	传统 ML + 过采样	Edge-IIoTset	99.9%	High	轻量化：极其适合边缘设备部署，推理速度快。	对高维非线性特征的捕捉能力弱于 DL。	
IDS-Agent	LLM Agent + RAG	ACI-IoT	-	97%	可解释性：提供自然语言报告；零日攻击推理能力强。	依赖 LLM 推理，延迟极高，不适合实时阻断。	
Cost-Sensitive Hybrid	算法级优化 (SAE+SVM)	UNSW-NB15	-	94.3%	无需生成数据，避免了分布偏差风险。	特征提取依赖 SAE，对参数敏感。	
  
*注：LRT-DDPM 文献重点报告了 Accuracy，并在定性分析中强调了 F1-score 的提升。

7.2 关键洞察
生成式 AI 的统治力已确立：无论是 Transformer-GAN 还是 LRT-DDPM，凡是结合了深度生成模型的方法，其准确率和 F1-score 普遍突破了 99% 的天花板。这证明了在不平衡大数据环境下，“生成”高质量的少数类样本是提升检测率的最有效手段。

模型复杂度与部署的权衡：尽管 Transformer-GAN 性能卓越，但其参数量巨大。相比之下，Ismail 等人的研究  提醒我们，在算力受限的 IoT 边缘节点，精心优化的轻量级模型（如 LightGBM）配合基础的 SMOTE 依然能达到工业级标准。未来的研究需要在“高性能大模型”与“低延迟轻量模型”之间寻找平衡点。   

从“识别”到“理解”的跨越：IDS-Agent 的出现打破了传统 IDS 的边界。尽管其速度目前无法满足骨干网实时检测的需求，但作为安全运营中心（SOC）的辅助分析工具，其价值不可估量。

8. 2025年及未来趋势预测
基于上述详尽的文献分析，我们对 2025 年及未来的网络入侵检测技术发展做出以下预测：

8.1 扩散模型（Diffusion Models）将全面取代 GAN
尽管 GAN 目前仍占有一席之地，但扩散模型在样本质量、多样性覆盖以及训练稳定性上的天然优势，使其正迅速成为数据增强的首选。随着 TACBlock  等加速采样技术的成熟，扩散模型的推理速度瓶颈将被打破。预计到 2025 年底，基于 Diffusion 的 IDS 将成为学术界的新基准（State-of-the-Art）。   

8.2 大模型驱动的“认知型”安全体系
未来的 IDS 将不再是一个孤立的分类器，而是一个由 LLM 驱动的综合智能系统。它将具备以下特征：

多模态感知：同时理解流量包（PCAP）、系统日志（Log）和自然语言情报。

自主决策：能够根据上下文自主调整检测阈值，甚至自动生成防火墙规则进行阻断。

人机协作：通过自然语言与安全分析师交互，解释攻击链条。

8.3 端云协同的联邦元学习（Federated Meta-Learning）
随着边缘计算的深入，单一的集中式训练或孤立的联邦学习已难以应对异构、动态的 IoT 网络。结合了**元学习（快速适应新攻击）和联邦学习（隐私保护与知识共享）**的混合框架将成为处理大规模不平衡数据的标准范式。这使得模型既能保护隐私，又能利用全网的攻击情报实现“一处发现，全网免疫”。

8.4 绿色 AI 与轻量化迁移
随着 Transformer 和 Diffusion 模型越来越庞大，其能耗问题日益凸显。未来的研究将更加关注**知识蒸馏（Knowledge Distillation）**技术，即如何将大模型学到的复杂分布知识，高效地迁移到适合在路由器、网关等边缘设备上运行的轻量级模型中，实现“大模型训练，小模型推理”。

9. 结论
2022年至2025年，针对不平衡大数据网络的入侵检测研究经历了一场深刻的技术革命。我们见证了从传统的数学插值（SMOTE）向基于物理过程的生成模型（Diffusion）的跨越，从单一的分类算法向具备认知能力的智能体（LLM Agents）的演进。研究表明，解决类别不平衡不再是一个单一的数据预处理步骤，而是贯穿于数据增强、模型架构设计（注意力机制、元学习）、损失函数优化（代价敏感）以及决策层（Agent推理）的全生命周期系统工程。

面对未来日益复杂且隐蔽的网络威胁，构建一个具备自适应生成能力、少样本快速学习能力、隐私协同能力以及可解释认知能力的下一代入侵检测系统，将是学术界与工业界共同的奋斗目标。

引用索引：

   


researchgate.net
(PDF) A comprehensive survey on intrusion detection systems with advances in machine learning, deep learning and emerging cybersecurity challenges - ResearchGate
在新窗口中打开

ieeexplore.ieee.org
Intrusion Detection in IoT and IIoT: Comparing Lightweight Machine Learning Techniques Using TON_IoT, WUSTL-IIOT - IEEE Xplore
在新窗口中打开

iasj.rdd.edu.iq
A Survey Study on Proposed Solutions for Imbalanced Big Data - Iraqi Academic Scientific Journals
在新窗口中打开

researchgate.net
GAN-Based IDS System for Imbalanced Datasets in SDN Environments with Offline and Real-Time Traffic Analysis - ResearchGate
在新窗口中打开

arxiv.org
Large Language Models for Network Intrusion Detection Systems: Foundations, Implementations, and Future Directions - arXiv
在新窗口中打开

openreview.net
IDS-Agent: An LLM Agent for Explainable Intrusion ... - OpenReview
在新窗口中打开

ieeexplore.ieee.org
Hybrid Framework Combining Diffusion-Based Image Augmentation and Feature Level SMOTE for Addressing Extreme Class Imbalance - IEEE Xplore
在新窗口中打开

researchgate.net
Features Dimensionality Reduction Approaches for Machine Learning Based Network Intrusion Detection - ResearchGate
在新窗口中打开

mdpi.com
Advanced Hybrid Transformer-CNN Deep Learning Model for Effective Intrusion Detection Systems with Class Imbalance Mitigation Using Resampling Techniques - MDPI
在新窗口中打开

mdpi.com
Generative Adversarial and Transformer Network Synergy for Robust Intrusion Detection in IoT Environments - MDPI
在新窗口中打开

ieeexplore.ieee.org
GAN-Based IDS System for Imbalanced Datasets in SDN Environments With Offline and Real-Time Traffic Analysis - IEEE Xplore
在新窗口中打开

researchgate.net
(PDF) Intrusion Detection in IoT and IIoT: Comparing Lightweight Machine Learning Techniques Using TON_IoT, WUSTL-IIOT-2021, and EdgeIIoTset Datasets - ResearchGate
在新窗口中打开

ieeexplore.ieee.org
Intrusion Detection in IoT and IIoT: Comparing Lightweight Machine Learning Techniques Using TON_IoT, WUSTL-IIOT - IEEE Xplore
在新窗口中打开

researchgate.net
(PDF) Hybrid Framework Combining Diffusion Based Image Augmentation and Feature Level SMOTE for Addressing Extreme Class Imbalance - ResearchGate
在新窗口中打开

researchgate.net
Ali Vaziri's research works | Stevens Institute of Technology and other places
在新窗口中打开

uh-ir.tdl.org
Generative Adversarial and Transformer Network Synergy for Robust Intrusion Detection in IoT Environments - UH Institutional Repository
在新窗口中打开

ieeexplore.ieee.org
LRT-DDPM: A Diffusion Model-Based Approach for Network Traffic Data Generation in Intrusion Detection - IEEE Xplore
在新窗口中打开

ieeexplore.ieee.org
LRT-DDPM: A Diffusion Model-Based Approach for Network Traffic Data Generation in Intrusion Detection - IEEE Xplore
在新窗口中打开

techscience.com
CMC | Free Full-Text | Diff-IDS: A Network Intrusion Detection Model Based on Diffusion Model for Imbalanced Data Samples
在新窗口中打开

researchgate.net
Diff-IDS model architecture diagram - ResearchGate
在新窗口中打开

researchgate.net
(PDF) Diff-IDS: A Network Intrusion Detection Model Based on Diffusion Model for Imbalanced Data Samples - ResearchGate
在新窗口中打开

ieeexplore.ieee.org
A Cost-Sensitive Machine Learning Model With Multitask Learning for Intrusion Detection in IoT - IEEE Xplore
在新窗口中打开

pure.rug.nl
University of Groningen A Cost-Sensitive Machine Learning Model With Multitask Learning for Intrusion Detection in IoT Telikani,
在新窗口中打开

research.rug.nl
A Cost-Sensitive Machine Learning Model With Multitask Learning for Intrusion Detection in IoT - the University of Groningen research portal
在新窗口中打开

journals.plos.org
MACML: Marrying attention and convolution-based meta-learning ...
在新窗口中打开

pmc.ncbi.nlm.nih.gov
MACML: Marrying attention and convolution-based meta-learning method for few-shot IoT intrusion detection - PMC - NIH
在新窗口中打开

ieeexplore.ieee.org
A Hybrid Deep Learning Model for Network Intrusion Detection System Using Seq2Seq and ConvLSTM-Subnets - IEEE Xplore
在新窗口中打开

researchgate.net
(PDF) A Hybrid Deep Learning Model for Network Intrusion Detection System using Seq2Seq and ConvLSTM-Subnets - ResearchGate
在新窗口中打开

researchgate.net
Performance Comparison of Proposed Hybrid Model with LuNET and Seq2Seq | Download Scientific Diagram - ResearchGate
在新窗口中打开

mdpi.com
Enhancing Federated Intrusion Detection with Class-Specific Dynamic Sampling - MDPI
在新窗口中打开

researchgate.net
Federated Learning-Based Security Attack Detection for Multi-Controller Software-Defined Networks - ResearchGate
在新窗口中打开

ieeexplore.ieee.org
Federated Learning Framework Based on Distributed Storage and Diffusion Model for Intrusion Detection on IoT Networks - IEEE Xplore
在新窗口中打开

neurips.cc
NeurIPS IDS-Agent: An LLM Agent for Explainable Intrusion Detection in IoT Networks
在新窗口中打开

mdpi.com
Innovating Intrusion Detection Classification Analysis for an Imbalanced Data Sample
在新窗口中打开

mdpi.com
An Optimized Transformer–GAN–AE for Intrusion Detection in Edge and IIoT Systems: Experimental Insights from WUSTL-IIoT-2021, EdgeIIoTset, and TON_IoT Datasets - MDPI
在新窗口中打开

mdpi.com
Future Internet, Volume 17, Issue 6 (June 2025) – 42 articles - MDPI