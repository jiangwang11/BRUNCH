面向分类任务的机器学习特征选择研究进展：2022–2025 年深度综述
1. 引言：高维分类任务中的特征选择新范式
在人工智能与数据科学的宏大图景中，特征选择（Feature Selection, FS）始终扮演着“看门人”的角色。它不仅决定了输入模型的数据质量，更直接界定了模型所能触及的性能上限。传统的机器学习分类任务——从垃圾邮件检测到早期的医疗诊断——往往依赖于专家手工提取的特征或经典的统计学筛选方法。然而，进入 2020 年代中期，特别是 2022 年至 2025 年这一时间窗口，特征选择领域面临着前所未有的挑战与机遇。

随着数据采集技术的指数级进步，分类任务所处理的数据维度已从千级跃升至百万级甚至亿级。在基因组学（Genomics）、高频金融交易（High-frequency Trading）以及工业物联网（IIoT）等领域，"维度灾难"（Curse of Dimensionality）不再是一个理论概念，而是每天必须面对的工程实体。与此同时，深度学习模型的参数量呈爆炸式增长，使得模型极易在冗余特征上过拟合，或习得非因果的虚假相关性（Spurious Correlations）。

本综述报告旨在对 2022–2025 年间面向分类任务的特征选择研究进行详尽的、百科全书式的梳理。我们将这一时期的研究进展概括为三次核心的“范式转移”：

从离散搜索到可微优化：不再将特征选择视为独立的预处理步骤，而是利用松弛技术（Relaxation Techniques）将其嵌入深度神经网络的端到端训练中，实现了特征权重与分类器参数的联合微分优化。

从相关性统计到因果推断：不再满足于发现与标签统计相关的特征，而是致力于通过马尔可夫毯（Markov Blanket）发现和结构学习，识别出真正的致因特征（Causal Features），以应对分布外（OOD）泛化和公平性挑战。

从数值计算到语义推理：大语言模型（LLMs）的介入彻底改变了特征工程的定义。利用 LLM 强大的世界知识（World Knowledge）和逻辑推理能力，特征选择开始从纯粹的数据驱动（Data-driven）向知识驱动（Knowledge-driven）演进。

本报告将分章节深入剖析上述领域的理论基础、核心算法、实验评价及未来趋势，力求为该领域的科研工作者提供一份详实的技术参考。

2. 基于深度学习与可微架构的特征选择
深度学习的兴起一度让部分研究者认为特征选择已不再重要，因为神经网络应当具备自动提取特征的能力。然而，2022-2025 年的研究表明，在面对高噪声、小样本或极高维数据时，显式的特征选择依然是提升模型鲁棒性和可解释性的关键。这一阶段的显著突破在于将离散的特征选择问题转化为连续的优化问题。

2.1 可微逻辑门网络（DiffLogic）：稀疏性与效率的极致
在 2024 年的 NeurIPS 和 ICML 会议上，一类被称为“可微逻辑门网络”（Differentiable Logic Gate Networks, DiffLogic）的方法引起了极大的轰动。这类研究的初衷是应对深度学习模型日益增长的推理成本，试图回归计算机科学的本源——布尔逻辑（Boolean Logic），通过构建稀疏的逻辑门电路来替代昂贵的浮点矩阵乘法。

2.1.1 核心机制：可微松弛与概率分布
传统的逻辑门网络（Logic Gate Networks, LGNs）由 AND、OR、XOR、NAND 等离散算子组成，其不可微性使得无法使用梯度下降算法（Gradient Descent）进行有效训练。2024 年的研究  提出了一种巧妙的**可微松弛（Differentiable Relaxation）**机制。   

概率化节点：网络中的每一个神经元不再硬性执行某一特定逻辑操作，而是维护一个涵盖 16 种二元布尔函数（如 f(a,b)=a∧b, f(a,b)=¬(a∨b) 等）的概率分布 α。

实值逻辑：输入信号被松弛为 $$ 区间的实数值，逻辑运算通过 T-范数（T-norms）或其平滑近似来实现。例如，AND 操作可以近似为乘法或 min(a,b) 的软化版本。

训练与离散化：在训练过程中，利用 Gumbel-Softmax 或 Straight-Through Estimator (STE) 等技术，使得梯度能够穿过离散选择层。随着训练的进行，并通过温度参数（Temperature Parameter）的退火，概率分布逐渐趋向于 one-hot 向量，最终收敛到确定性的逻辑门组合。

2.1.2 卷积扩展与逻辑池化
 进一步将这一思想从多层感知机（MLP）扩展到了卷积神经网络（CNN）。他们提出了卷积逻辑门网络（Convolutional Differentiable Logic Gate Networks）。   

逻辑卷积核：传统的卷积核是权重的线性组合，而该方法使用“深度逻辑门树”（Deep Logic Gate Trees）作为卷积核。这不仅大幅减少了参数量，而且由于逻辑树的稀疏性，模型自动学会了忽略图像中不相关的像素区域。

逻辑 OR 池化：传统的 Max Pooling 或 Average Pooling 被“逻辑 OR 池化”（Logical OR Pooling）取代。在布尔逻辑中，OR 操作天然具有“存在性检测”的意味（即只要局部区域内存在某一特征，输出即为真），这与视觉任务中的特征检测高度契合。

2.1.3 实验表现与特征选择意义
DiffLogic 的最大贡献在于其隐式的、极致的特征选择能力。在 CIFAR-10 和 MNIST 等基准测试中，DiffLogic 模型仅使用数万至数千万个逻辑门（相比传统神经网络的数亿浮点参数），就达到了 SOTA 级别的准确率 。   

推理速度：在 CPU 上，编译后的逻辑门网络推理速度比传统的 CNN 快 160 倍至 1900 倍。

特征稀疏性：由于逻辑门网络倾向于学习简单的布尔组合，它自动剔除掉了大量冗余的输入特征。例如，在很多分类决策中，模型可能只关心某几个像素点的异或（XOR）关系，而忽略背景。这种机制为高维数据的快速特征筛选提供了一种全新的、硬件友好的解决方案。

2.2 深度依赖正则化 Knockoff (DeepDRK)：控制错误发现率
特征选择的另一个核心目标不仅仅是提高精度，还要确保所选特征的统计显著性，即控制错误发现率（False Discovery Rate, FDR）。Candes 等人提出的 Model-X Knockoff 框架是统计学界的里程碑，但在处理复杂的非线性依赖时存在局限。2024 年提出的 DeepDRK  将深度生成模型与 Knockoff 理论进行了深度融合。   

2.2.1 理论背景：Knockoff 与交换性
Knockoff 方法的核心思想是为每一个原始特征 X 
j
​
  构造一个“伪特征”  
X
~
  
j
​
 （即 Knockoff）。这个伪特征必须满足两个严格条件：

交换性（Swap Property）：如果不考虑目标变量 Y，交换 X 
j
​
  和  
X
~
  
j
​
  不会改变特征的联合分布。这意味着  
X
~
  
j
​
  在统计结构上与 X 
j
​
  无法区分。

条件独立性： 
X
~
  
j
​
  与目标变量 Y 条件独立（给定原始特征 X）。

如果一个特征选择算法选中了  
X
~
  
j
​
 ，这显然是一个错误发现（False Discovery）。利用这一性质，我们可以通过统计选中伪特征的频率来估计并控制 FDR。

2.2.2 DeepDRK 的创新：对抗生成与依赖解耦
传统的 Knockoff 生成方法（如高斯 Knockoff）假设数据服从多元高斯分布，这在现实分类任务中往往不成立。DeepDRK 采用生成对抗网络（GAN）来学习任意数据分布的 Knockoff 生成器。

多源对抗攻击视角：DeepDRK 将 Knockoff 的生成过程建模为一个多源对抗攻击问题。生成器试图生成能够“欺骗”判别器的伪特征，使得判别器无法区分原始特征和伪特征（满足交换性）。

依赖正则化（Dependency Regularization）：这是 DeepDRK 的点睛之笔。在高维数据中，特征之间往往存在强相关性，导致生成器倾向于生成与原始特征过于相似的 Knockoff，从而失去了检验能力（Power）。DeepDRK 引入了一种基于扰动的正则化项，强制降低 Knockoff 的“可重构性”（Reconstructability）。这一机制有效地“解耦”了特征间的强依赖，使得模型在保持交换性的同时，能够更敏锐地捕捉到特征与标签之间的微弱信号。

2.2.3 实验验证
在涉及基因表达数据（典型的 p≫n 场景）的分类实验中，DeepDRK 展现了卓越的性能。与 DeepPINK、Deep Knockoffs 等基线方法相比，DeepDRK 在严格控制 FDR（例如 α=0.1）的前提下，显著提升了特征选择的功效（Power），即找出了更多真实的生物标志物 。   

2.3 基于门控拉普拉斯的无监督特征选择
在缺乏标签信息的场景下，如何进行有效的特征选择？2022-2024 年间，无监督特征选择（Unsupervised Feature Selection, UFS）也迎来了可微化的革新。 提出的 Gated Laplacian 方法重新审视了经典的拉普拉斯分数（Laplacian Score）。   

传统局限：传统的拉普拉斯分数是在全特征空间上构建近邻图（Nearest Neighbor Graph），然后评估每个特征保持局部结构的能力。然而，在高维空间中，距离度量失效（Distance Concentration），全特征空间构建的图往往被噪声主导。

门控机制：该研究引入了一个可学习的门控向量（Gating Vector），该向量由连续松弛的伯努利变量（Continuously Relaxed Bernoulli Variables）组成。

联合优化：算法不再在固定的图上评估特征，而是动态地：

利用当前门控选中的特征子集构建图拉普拉斯矩阵。

计算该子集上的拉普拉斯损失（衡量局部结构保持程度）。

通过梯度下降更新门控参数，使得选出的特征子集能构建出最清晰、最能反映数据流形结构的图。

应用：这一方法在单细胞测序数据聚类和图像分类预处理中表现优异，证明了在高噪声环境下，基于子集的动态构图远优于基于全集的静态构图 。   

3. 因果特征选择：超越相关性的革命
如果说深度学习解决了“怎么拟合”的问题，那么因果科学（Causal Science）则试图回答“为什么相关”的问题。在 2022-2025 年的综述中，我们观察到因果特征选择已从理论探讨走向了算法落地，成为了解决模型鲁棒性（Robustness）、可解释性（Interpretability）和公平性（Fairness）的核心手段。

3.1 理论基石：马尔可夫毯与因果图
因果特征选择的理论核心在于马尔可夫毯（Markov Blanket, MB）。在贝叶斯网络或因果图中，一个目标变量 T 的马尔可夫毯 MB(T) 包含其父节点（Parents）、子节点（Children）以及配偶节点（Spouses，即子节点的其他父节点）。

核心性质：给定 MB(T)，目标变量 T 与网络中所有其他变量条件独立。这意味着 MB(T) 是预测 T 所需的最小且全信息的特征子集。

超越相关性：传统方法（如互信息）容易选出 T 的后代节点的后代，或者与 T 受同一隐变量影响的兄弟节点。这些特征虽然统计相关，但在因果干预下是不稳定的。

3.2 应对隐变量挑战：LatentLCD 算法
现实世界的数据往往是不完整的，存在大量未被观测的隐变量（Latent Confounders）。这违反了传统因果发现算法中的“因果充分性”（Causal Sufficiency）假设。

 和  针对这一痛点，提出了 LatentLCD (Local Causal Discovery without Causal Sufficiency) 算法，这是 2025 年 AAAI 会议上的亮点工作。   

3.2.1 局部最大祖先图（LocalMAG）
为了描述包含隐变量的因果结构，研究者引入了最大祖先图（Maximal Ancestral Graph, MAG）。然而，学习全局 MAG 是一个 NP-hard 问题。LatentLCD 创新性地提出了 LocalMAG 的概念，仅关注目标变量局部的因果结构。

双向边（Bidirectional Edges）：在 MAG 中，双向边 ↔ 表示两个变量之间存在未观测的共同原因（即隐变量）。

算法流程：

骨架发现（Skeleton Discovery）：利用条件独立性测试（CI Tests），初步筛选出与目标变量存在依赖关系的候选邻居。

对撞结构识别（Collider Identification）：通过寻找 V-结构（V-structures, X→Z←Y），定向部分边。

隐变量推断：这是最关键的一步。LatentLCD 利用特定的规则（如不满足某些方向的 d-分离条件）来推断何时应当将无向边定向为双向边。例如，如果 X 和 Y 相关，且无法找到任何观测变量能阻断它们的相关性，且它们不构成因果链，则可能存在隐变量。

3.2.2 实验突破
在 "FRSPDAG" 等包含隐变量的合成数据集上，LatentLCD 的表现令人印象深刻。与传统的 PCD-by-PCD 或 CMB 算法相比，LatentLCD 在 F1 分数上提升了 30% 至 50% 。这意味着它成功地区分了“真正的因果特征”和“由隐变量导致的伪相关特征”，这对于医疗诊断（避免将并发症误认为病因）具有极高的实用价值。   

3.3 负责任的 AI：公平因果特征选择 (FairCFS)
随着 AI 伦理日益受到重视，特征选择中的公平性问题成为了 2023-2024 年的研究热点。传统算法在去除冗余时，可能会无意中保留那些作为“敏感属性代理”（Proxy for Sensitive Attributes）的特征，导致模型歧视。

 和  提出了 FairCFS 算法，旨在从因果层面阻断不公平信息的传播。   

敏感路径阻断：FairCFS 构建包含目标变量 Y、特征 X 和敏感变量 S（如种族、性别）的局部因果图。算法的目标是寻找一个特征子集，该子集在预测 Y 时最大化因果强度，同时切断任何从 S 到 Y 的非法因果路径（Inadmissible Paths）。

类特定互信息：为了处理不同群体间的数据分布异质性，FairCFS 引入了类特定互信息（Class-specific Mutual Information），确保选出的特征在不同的人群子组中都具有预测力，而不是仅由多数群体主导。

结果：实验证明，FairCFS 在保持分类准确率与 SOTA 方法持平的同时，显著降低了机会均等差（Equal Opportunity Difference）等公平性指标的违规程度 。   

3.4 动态环境下的因果发现
针对物理系统或非平稳时间序列， 在 2025 年提出了动态马尔可夫毯检测（Dynamic Markov Blanket Detection）。   

该方法结合了变分贝叶斯期望最大化（Variational Bayesian EM）和动态注意力机制。

它不假设因果结构是静态的，而是允许特征的因果角色（是父节点、子节点还是无关节点）随时间演变。这对于故障检测或宏观物理规律发现（如从微观粒子运动中发现宏观物体边界）具有开创性意义。

4. 大语言模型：特征工程的“新物种”
2024 年至 2025 年，特征选择领域发生的最具颠覆性的事件，莫过于大语言模型（LLM）的全面介入。这标志着特征选择从“基于统计的数值计算”转向了“基于语义的知识推理”。

4.1 LLM-Select：零样本特征筛选能力
 和  提出的 LLM-Select 是一项具有里程碑意义的工作。它挑战了“特征选择必须依赖训练数据”的传统观念。   

4.1.1 惊人的发现
研究者发现，当给定特征名称（如“血压”、“年龄”、“肌酐水平”）和预测任务（如“预测心力衰竭风险”）时，即使完全不提供任何样本数据（Zero-shot），GPT-4 等先进 LLM 也能给出极高质量的特征重要性评分。

相关性验证：实验显示，LLM 给出的特征重要性排名，与在数千个样本上运行 LASSO 或 Random Forest 得到的重要性排名高度相关。

机制：LLM 并非在进行统计计算，而是在调用其预训练阶段习得的庞大世界知识（World Knowledge）。它“知道”医学上血压与心脏病的因果联系，因此给予高分。

4.1.2 实用价值与局限
小样本/零样本场景：在罕见病研究或冷启动推荐系统中，数据极其稀缺。LLM-Select 提供了一种基于先验知识的“热启动”方案。

数据采集指导：LLM 可以告诉研究者“应该去收集哪些数据”，从而在数据采集阶段就节省成本 。   

局限：对于匿名化特征（如 Feat_1, Feat_2）或高度领域特定的“黑话”，LLM 的表现会急剧下降。

4.2 LLM-FE：进化式自动化特征工程
如果说 LLM-Select 是在做减法（筛选），那么 LLM-FE (LLM-based Feature Engineering)  则是在做加法（创造）。   

4.2.1 算法架构：LLM 作为进化算子
LLM-FE 将特征工程建模为一个**程序搜索（Program Search）**问题，并结合了进化算法（Evolutionary Algorithm）的框架。

种群初始化：LLM 根据数据描述，生成一批初始的特征变换代码（Python 函数），例如 def new_feat(df): return df['A'] / (df + 1)。

评估（Fitness Evaluation）：在真实数据上执行这些代码，训练一个轻量级模型（如 XGBoost），以验证集性能作为适应度分数。

进化迭代：

交叉与变异：LLM 读取表现最好的特征代码，作为“上下文示例”（In-context Examples），并被提示去“修改”、“组合”或“变异”这些代码以产生更优的特征。

思维链（Chain of Thought）：LLM 在生成代码前会输出一段推理文本，解释为什么这样组合特征可能有效（例如，“根据物理学公式，距离除以时间可能得到速度特征”）。

长期记忆：系统维护一个外部记忆库，存储历史最优策略，防止 LLM 遗忘。

4.2.2 实验结果
在 Kaggle 的多个表格数据竞赛数据集上，LLM-FE 能够发现人类专家难以构思的复杂非线性特征（如 groupbythenmean, residual, sigmoid 等组合）。其性能显著优于传统的自动特征工程工具（如 OpenFE）和早期的 LLM 方法（如 CAAFE），且具有更好的抗噪性 。   

4.3 RAFS：检索增强与隐私保护
面对包含数万个特征的基因组数据，直接将所有特征名放入 LLM 的提示词（Prompt）中是不现实的（上下文窗口限制）。 和  提出了 RAFS (Retrieval-Augmented Feature Selection)。   

分层筛选：首先利用传统的轻量级方法（如相关系数）或向量数据库检索（RAG），选出与任务描述语义相关的候选特征子集。

精细推理：将候选子集分批次输入 LLM 进行详细的因果推理和筛选。

隐私优势：在医疗数据共享受限的背景下，RAFS 只需要上传特征的元数据（Metadata，即列名和描述），而无需上传任何病人的具体数值数据。这为跨机构的联邦特征选择提供了一种隐私安全的解决方案。

5. 进化计算与多目标优化：平衡的艺术
特征选择天然是一个多目标优化问题（Multi-objective Optimization Problem, MOOP）：我们既希望最大化分类精度，又希望最小化特征数量。2023-2024 年，进化计算领域在此方向取得了显著进展。

5.1 两档案进化算法 (Two-Archive Evolutionary Algorithms)
 指出，传统的进化算法在处理特征选择时，往往会被“超级个体”（即特征数极少但精度尚可的解）主导，导致种群过早收敛，失去了探索高精度（可能特征稍多）区域的能力。   

该研究提出了一种双档案机制：

收敛性档案（Convergence Archive）：利用动态降维算子，专门负责“修剪”特征，追求极致的稀疏性。

多样性档案（Diversity Archive）：利用基于拥挤距离的变异算子，专门负责“探索”未知的特征组合空间，不轻易淘汰特征数较多的解。

环境选择：不同档案中的个体通过不同的环境选择标准进行生存竞争，确保了帕累托前沿（Pareto Front）的均匀分布。

5.2 进化多任务（Evolutionary Multitasking）
为了解决高维空间搜索慢的问题， 引入了迁移学习的思想。   

主任务与辅助任务：将“多目标特征选择”作为主任务，同时并行运行几个简单的辅助任务（如单目标特征选择，或在子采样数据上进行选择）。

基因迁移：算法允许不同任务之间交换优良的基因片段（特征组合）。辅助任务通常能快速收敛，其发现的有效特征组合可以作为“经验”直接迁移给主任务，帮助主任务跳出局部最优。

实验数据：在 27 个数据集上的测试表明，这种“多兵种协同”策略大幅缩短了算法的收敛时间 。   

6. 多模态与新兴应用领域的挑战
随着 GPT-4V 和 Gemini 等多模态模型的普及，特征选择的边界正在拓展。

6.1 多模态大模型（MLLM）中的层选择
在多模态分类任务中，通常直接使用预训练视觉编码器（如 CLIP-ViT）的最后一层特征。然而，2025 年的一项研究  挑战了这一惯例。   

深浅不一：研究发现，深层特征虽然包含丰富的语义信息（适合 OCR 或物体识别），但在处理细粒度视觉任务（如计数、定位、几何判断）时，浅层或中层特征的表现反而更好。

策略：提出了一种轻量级的特征融合策略，动态地根据任务类型选择 ViT 的不同层级特征。这实际上是一种针对神经网络内部表示（Internal Representations）的特征选择。

6.2 递归可微逻辑网络（Recurrent DiffLogic）
 将 DiffLogic 扩展到了序列建模（Seq2Seq）。这意味着在处理文本或时间序列分类时，模型可以动态地选择在每一步使用哪些逻辑门。这为在 FPGA 等低功耗硬件上部署高效的时间序列分类器铺平了道路。   

7. 实验评价体系与基准
为了客观衡量上述新方法的性能，2024-2025 年的评价体系也变得更加严谨和多维。

7.1 合成数据基准 (Synthetic Benchmarks)
为了验证因果特征选择的准确性，必须依赖拥有 Ground Truth 的合成数据。 发布的 SyntheticDatasetsFSA Toolkit 成为了该领域的标准工具。   

数据集名称	样本数	特征数 (相关/冗余/无关)	目标生成公式 (Ground Truth)	灵感来源
Trigonometric	200	2 / 5 / 50	F 
2
​
 >2sin(F 
1
​
 )−2	MLP 非线性边界
Hypersphere	400	3 / 20 / 100	900>F 
1
2
​
 +F 
2
2
​
 +F 
3
2
​
 	SVM 球形边界
10-class Multi-cut	500	6 / 20 / 100	F 
1
​
 −2F 
2
​
 +5F 
3
​
 −4F 
4
​
 +…	决策树复杂切分
Yin-Yang	600	2 / 10 / 75	图像生成的拓扑结构	艺术与拓扑
这些数据集使得研究者不仅能报告准确率，还能报告特征选择的查准率（Precision）和查全率（Recall）。

7.2 评价指标的多维化
SHD (Structural Hamming Distance)：在因果发现中，衡量学到的图与真实图之间的边差异（缺边、多边、方向错误）。

Stability (Jaccard Index)：衡量算法在数据微小扰动下，选出特征子集的稳定性。这对医疗诊断至关重要。

Pareto Hypervolume：在多目标优化中，衡量解集在目标空间覆盖的体积。

8. 趋势展望与挑战
8.1 趋势：LLM 与传统优化器的“双系统”融合
未来的特征选择系统将类似于人类的认知架构：

系统 1 (快系统)：由 DiffLogic 或进化算法组成，负责快速、并行的数值搜索和验证。

系统 2 (慢系统)：由 LLM 组成，负责宏观的假设生成、因果推理和结果解释。 LLM-FE 已经展示了这种融合的雏形。

8.2 趋势：从特征选择到“特征发现”
随着 LatentLCD 和 Dynamic MB 的成熟，我们不再局限于从给定列表中选择特征，而是能够发现数据中隐含的物理规律或因果机制（Discovery of macroscopic laws）。

8.3 挑战：多模态对齐与异构性
如何从图像、文本、传感器数据等异构源中联合选择特征？目前的 MLLM 层选择还很初级。未来的挑战在于如何量化不同模态特征之间的互补信息（Complementary Information），而非仅仅是冗余信息。

8.4 挑战：因果推断的可扩展性
尽管 DeepDRK 和 LatentLCD 提升了精度，但因果算法的时间复杂度通常较高。如何在百万维特征上进行实时的因果结构学习，仍是算力上的巨大挑战。

9. 结论
2022 年至 2025 年，特征选择领域经历了一场从“术”到“道”的升华。

技术上，DiffLogic 和 DeepDRK 证明了通过可微松弛和对抗训练，我们可以在深度神经网络内部实现精确且高效的特征筛选；LatentLCD 和 FairCFS 则确立了因果性在处理隐变量和公平性问题上的核心地位，使特征选择具备了抵抗分布偏移的韧性。

而在方法论上，LLM-Select 和 LLM-FE 的出现标志着语义知识正式成为特征工程的一等公民。这不仅大幅降低了特征选择对标注数据的依赖，更为自动化科学发现（Automated Scientific Discovery）开启了新的大门。

未来的特征选择，将是一个融合了深度学习的高效计算、因果科学的严谨推理以及大语言模型广博知识的综合智能系统。它不再仅仅是为了提升几个百分点的准确率，而是为了构建更加可信、透明、且符合人类认知的智能模型。


youtube.com
NIPS 2024 spotlight | Convolutional Differentiable Logic Gate Networks - YouTube
在新窗口中打开

arxiv.org
Convolutional Differentiable Logic Gate Networks
在新窗口中打开

semanticscholar.org
DeepDRK: Deep Dependency Regularized Knockoff for Feature Selection
在新窗口中打开

proceedings.neurips.cc
DeepDRK: Deep Dependency Regularized Knockoff ... - NIPS papers
在新窗口中打开

proceedings.neurips.cc
Differentiable Unsupervised Feature Selection based on a Gated Laplacian
在新窗口中打开

raw.githubusercontent.com
Contextual Feature Selection with Conditional Stochastic Gates - GitHub
在新窗口中打开

ojs.aaai.org
Local Causal Discovery Without Causal Sufficiency
在新窗口中打开

arxiv.org
Fair Causal Feature Selection - arXiv
在新窗口中打开

arxiv.org
[2306.10336] Fair Causal Feature Selection - arXiv
在新窗口中打开

arxiv.org
Dynamic Markov Blanket Detection for Macroscopic Physics Discovery
在新窗口中打开

arxiv.org
[2407.02694] LLM-Select: Feature Selection with Large Language Models - arXiv
在新窗口中打开

openreview.net
LLM-Select: Feature Selection with Large Language Models - OpenReview
在新窗口中打开

arxiv.org
LLM-FE: Automated Feature Engineering for Tabular Data with ...
在新窗口中打开

arxiv.org
Exploring Large Language Models for Feature Selection: A Data-centric Perspective - arXiv
在新窗口中打开

arxiv.org
Exploring Large Language Models for Feature Selection: A Data-centric Perspective - arXiv
在新窗口中打开

ieeexplore.ieee.org
Balancing Different Optimization Difficulty Between Objectives in ...
在新窗口中打开

ieeexplore.ieee.org
A Multiform Optimization Framework for Multiobjective Feature ...
在新窗口中打开

aclanthology.org
Multimodal Language Models See Better When They Look Shallower
在新窗口中打开

arxiv.org
[2504.21447] Multimodal Language Models See Better When They Look Shallower - arXiv
在新窗口中打开

arxiv.org
Recurrent Deep Differentiable Logic Gate Networks - arXiv
在新窗口中打开

github.com
ro1406/SyntheticDatasetsFSA: Synthetic Datasets for ... - GitHub
在新窗口中打开
