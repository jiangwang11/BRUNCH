机器学习中的表格数据基础模型：理论范式、架构演进与未来趋势 (2022–2025)
1. 引言：结构化数据的深度学习“破壁”时刻
表格数据（Tabular Data）作为现代数据科学中最普遍、最基础的数据模态，长期以来承载着金融风控、临床医疗、工业制造及科学实验等领域的关键业务逻辑。尽管深度学习在自然语言处理（NLP）和计算机视觉（CV）领域已确立了绝对的统治地位，但在 2022 年之前，表格数据的建模任务——尤其是中小型数据集上的分类与回归——依然是梯度提升决策树（Gradient Boosting Decision Trees, GBDT）及其变体（如 XGBoost, CatBoost, LightGBM）的天下。这种现象在学术界被称为“表格数据的深度学习鸿沟”（The Deep Learning Gap in Tabular Data）。造成这一鸿沟的根本原因在于表格数据的特殊属性：极端的异构性（Heterogeneity）、缺乏像图像像素或文本 Token 那样的空间/序列局部相关性、以及复杂的特征交互模式 。   

然而，2022 年至 2025 年间，随着基础模型（Foundation Models）理念的兴起，这一格局迎来了历史性的转折。研究者们不再满足于针对特定数据集设计特定的神经网络架构（如 ResNet-like MLP 或 Transformer），而是开始探索“通用表格智能”的可能性——即构建一个能够像 GPT 处理任意文本那样，处理任意结构表格数据的单一模型。这一时期的研究呈现出爆发式增长，从早期的利用大语言模型（LLM）进行文本化适配，发展到 2024-2025 年间原生表格基础模型（Native Tabular Foundation Models, TFMs）的成熟。

本综述报告旨在详尽梳理这一激动人心的技术演进过程。我们将深入剖析 2022 年至 2025 年间的代表性工作，包括基于上下文学习（In-Context Learning, ICL）的 TabPFN 系列、验证了缩放定律（Scaling Laws）的 TabDPT、探索通用预训练协议的 UniTabE 和 TransTab，以及基于指令微调的 Table-GPT。通过对这些工作的架构原理、训练目标及实验结果的深度解构，本文将揭示表格基础模型如何逐步突破“异构性”与“小样本”的双重桎梏，并基于当前的局限性预测 2025 年后的技术演进路线。

2. 范式转移：从“一表一练”到“通用大模型”
在传统的机器学习工作流中，面对每一个新的表格数据集，数据科学家都需要经历特征工程、模型选择、超参数调优（HPO）及训练验证的完整周期。这种“一表一练”（Train-from-Scratch）的模式虽然在单一任务上能获得极高的精度（尤其是配合 GBDT 时），但由于缺乏跨任务的知识迁移能力，其不仅计算效率低下，且在面对少样本（Few-shot）或零样本（Zero-shot）场景时往往束手无策。

表格基础模型（TFM）的核心愿景是打破这一孤岛效应。通过在海量表格语料库（涵盖不同领域、不同 Schema）上进行预训练，TFM 旨在习得通用的统计规律、特征交互模式甚至因果推断能力。根据输入表征方式和推理机制的不同，现有的 TFM 研究大致可分为三大技术流派：基于 LLM 的序列化方法、原生表格架构的上下文学习方法，以及基于图和混合架构的表征学习方法。

2.1 技术流派概览
技术流派	核心逻辑	代表工作 (2022-2025)	关键优势	核心挑战
LLM 适配与序列化	将表格扁平化为自然语言，利用 LLM 的语义理解与推理能力。	
TabLLM , Table-GPT , Chain-of-Table , GTL 

强大的语义理解，零样本推理，复杂推理（Reasoning）能力。	上下文窗口限制，数值计算精度低，推理成本昂贵。
原生 ICL 与先验拟合	设计专用 Transformer，在合成或真实数据上学习“贝叶斯推理”过程。	
TabPFN v1/v2 , TabDPT 

极速推理（单次前向），小样本性能 SOTA，无需调参。	上下文长度限制（虽有改善），大规模数据下的训练成本。
通用编码与图表征	将异构表格映射为统一 Token 或图结构，进行掩码重建或对比学习。	
UniTabE , TransTab , CARTE 

处理 Schema 不匹配，跨表迁移，支持增量列。	预训练目标的有效性依赖于数据规模与质量。
  
3. 基于大语言模型的表格智能：语义与推理的融合
在 TFM 发展的初期（2022-2023），最直观的路径是利用已有的强大 LLM（如 GPT-3, LLaMA）来处理表格。这一流派的核心假设是：表格的列名和文本特征中蕴含了丰富的语义信息（如“年龄”、“血压”），这些先验知识可以被 LLM 利用，从而在缺乏训练数据的场景下实现优越的冷启动性能。

3.1 序列化策略与语义理解：TabLLM 与 GTL
将二维结构的表格转化为一维的 Token 序列是 LLM 处理表格的第一步。TabLLM (AISTATS 2023)  系统性地研究了这一过程。该研究指出，简单的数值拼接会丢失结构信息，而包含元数据的序列化（如 Column: Feature Name, Value: 23）能显著提升效果。TabLLM 的研究表明，在少样本（Few-shot）分类任务中，经过指令微调的 T5 或 GPT-3 模型能够击败专门设计的深度表格模型，甚至在极少样本下优于 GBDT。这证明了 LLM 内部的通用知识（World Knowledge）可以迁移到表格任务中，弥补样本的不足。   

随后，Generative Tabular Learning (GTL, KDD 2024)  将这一思路推向了新的高度。GTL 不仅利用 LLM 进行预测，还引入了思维链（Chain-of-Thought）和上下文示例（In-Context Examples）来辅助模型理解特征的物理含义。GTL 使用 LLaMA-2 作为基座，通过指令微调使其适应表格预测任务。实验显示，GTL 在零样本和少样本场景下具有极强的泛化能力，能够理解复杂的列名语义并据此做出合理的分类判断。   

3.2 深度推理链：Chain-of-Table (ICLR 2024)
当任务从简单的分类回归扩展到复杂的表格问答（Table QA）或逻辑推理时，静态的序列化往往受限于上下文窗口且难以捕捉多步逻辑。Chain-of-Table  提出了一种动态的推理机制，旨在解决这一问题。   

与直接让 LLM 输出答案不同，Chain-of-Table 要求 LLM 动态规划一系列“表格操作”（Table Operations），如 Add_Column(), Select_Row(), Group_By() 等。

机制解析： 模型首先根据问题（如“哪个国家的自行车手前三名最多？”）生成第一步操作（如“按国家分组”），然后执行该操作生成一个中间表格（Intermediate Table）。这个中间表格作为新的上下文输入给模型，以规划下一步操作。

意义： 这种“演化表格”（Evolving Tables）的策略有效地缩短了上下文长度，剔除了无关信息，并迫使模型展示推理过程。在 WikiTQ 和 TabFact 等高难度基准测试中，Chain-of-Table 刷新了 SOTA，证明了表格基础模型不仅需要“感知”能力，更需要具备类似 SQL 的“操作与推理”能力。

3.3 指令微调的集大成者：Table-GPT (SIGMOD 2024)
微软研究院推出的 Table-GPT  标志着“表格微调”（Table-tuning）范式的成熟。为了让通用 LLM 真正理解表格，研究团队构建了一个庞大的指令微调数据集，涵盖了 18 类不同的表格任务。   

Table-GPT 的任务谱系（Task Taxonomy）： 该研究采用了“合成后增强”（Synthesis-then-Augment）的数据构造策略，生成的任务包括但不限于：

表格理解（Table Understanding）： 如缺失值识别 (T-1)、列类型推断 (T-4)。这要求模型理解数据的分布和类型约束。

数据增强与操作（Data Augmentation & Manipulation）： 如列扩充 (T-14)、行扩充 (T-15)、行列交换 (T-16)。这些任务迫使模型学习表格的结构不变性和生成能力。

问答与摘要（QA & Summarization）： 如表格问答 (T-3)、表格摘要 (T-13)。

通过在这些多样化任务上对 GPT-3.5/ChatGPT 进行微调，Table-GPT 不仅在传统的预测任务上表现出色，更具备了处理“脏数据”、辅助数据清洗以及进行探索性数据分析（EDA）的通用能力 。这表明未来的表格基础模型将不再是单一的预测器，而是数据科学家的智能助手。   

4. 原生表格基础模型：架构创新与规模化效应 (2024-2025)
尽管基于 LLM 的方法在语义理解上具有优势，但在处理高维数值特征、推理速度以及大规模数据拟合方面存在天然劣势。为了解决这些问题，2024 年至 2025 年间，学术界涌现出了一批原生表格基础模型（Native TFMs）。这些模型设计了专门的 Tokenizer 和 Transformer 架构，直接在数值和类别特征上进行预训练，试图重现 NLP 领域的 Scaling Laws。

4.1 TabPFN 系列：贝叶斯推断的神经网络近似
TabPFN (Tabular Prior-Data Fitted Network) 是该领域最具颠覆性的工作之一。其核心思想源于“元学习”（Meta-Learning）：TabPFN 不是在特定数据集上训练，而是被训练来近似在一系列合成数据集上的贝叶斯后验预测分布（Posterior Predictive Distribution, PPD）。

4.1.1 理论基础：先验拟合 (Prior-Fitting)
TabPFN v1  利用结构因果模型（Structural Causal Models, SCMs）生成了数百万个合成数据集。这些数据集涵盖了各种可能的因果结构、特征分布和类别关系。Transformer 模型被训练为在给定训练集（作为上下文）和测试输入的情况下，预测测试标签。从理论上讲，如果在足够多样化的先验分布上训练至收敛，TabPFN 就能在单次前向传播中执行贝叶斯推理，无需任何梯度更新 。   

4.1.2 TabPFN v2 (2025)：全能型选手的诞生
针对 v1 版本在上下文长度（仅支持约 1000 样本）和任务类型（仅支持分类）上的局限，2025 年发布的 TabPFN v2  实现了全面进化：   

支持回归任务： v2 引入了对数似然损失函数，使其能够输出连续值的预测分布，填补了 v1 在回归任务上的空白。

规模与上下文的飞跃： 采用了分块注意力（Tiled-block Attention）等技术，v2 支持的上下文长度达到了 50,000 个数据点和 2,000 个特征，相比前代提升了 20 倍。这使得它能够处理中等规模的真实世界数据集。

随机特征 Token (Randomized Feature Tokens)： 为了处理异构特征，v2 引入了一种新颖的 Tokenizer，通过随机投影和分箱将数值特征转化为离散 Token。这种设计增强了模型对特征分布偏移的鲁棒性，并避免了复杂的预处理。

架构升级： 引入了 2D 注意力机制，模型不仅关注行与行之间的关系（样本相关性），还关注列与列之间的关系（特征交互），极大地增强了表征能力。

性能霸主： 在 TabArena 基准测试中，TabPFN v2 在中小规模数据集（≤ 10k 样本）上对默认参数的 XGBoost 实现了 100% 的胜率，在更大规模数据集上也达到了 87% 的胜率 。这一结果具有里程碑意义，意味着对于绝大多数日常表格任务，TabPFN v2 已经可以作为一个“即插即用”的通用求解器，彻底省去了调参的繁琐。   

此外，为了解决 Transformer 推理慢的问题，TabPFN v2.5 引入了蒸馏引擎，允许将预训练好的大模型知识蒸馏到轻量级的 MLP 或 GBDT 中，从而在保持高精度的同时实现毫秒级的推理延迟 。   

4.2 TabDPT：表格数据的缩放定律 (NeurIPS 2025)
如果说 TabPFN 证明了“先验拟合”的可行性，那么 TabDPT (Scaling Tabular Foundation Models on Real Data)  则从工程和理论层面验证了表格模型的可扩展性。该研究的核心贡献在于首次严格验证了表格领域的神经缩放定律（Neural Scaling Laws）。   

4.2.1 幂律关系的发现
TabDPT 的研究表明，表格基础模型的性能（超额损失，Excess Loss）与模型参数量 (P) 和预训练数据量 (D) 之间遵循严格的幂律关系：

l
^
 (P,D)−E≈ 
P 
α
 
A
​
 + 
D 
β
 
B
​
 
通过大量实验，作者测定出缩放指数 α≈0.42 和 β≈0.39 。这不仅是一个数学拟合，更是一个强有力的信号：它意味着表格基础模型并非受限于某些不可逾越的理论障碍（如“没有流形结构”），只要我们持续增加真实数据的规模和模型的容量，其性能就能持续、可预测地提升。   

4.2.2 真实数据 vs. 合成数据
与 TabPFN 依赖合成数据不同，TabDPT 强调了真实数据预训练的重要性。研究发现，仅在合成数据上预训练的模型在面对真实世界的复杂分布（如长尾分布、复杂的缺失模式）时，泛化能力存在天花板。TabDPT 通过混合真实表格语料库进行预训练，证明了在同等计算量下，真实数据能提供更丰富的监督信号，从而实现更快的收敛和更好的下游泛化 。   

4.2.3 架构设计：检索增强与行编码
TabDPT 采用了一种基于行的 Transformer 编码器（Row-based Transformer Encoder）。它将每一行视为一个 Token，并通过检索机制（Retrieval）从历史数据中寻找最相似的样本作为上下文。这种设计不仅规避了全量注意力带来的 O(N 
2
 ) 计算复杂度，还使得模型能够高效利用超大规模的预训练数据集作为知识库 。   

4.3 异构融合与通用协议：UniTabE 与 TransTab
除了上下文学习，另一种主流思路是学习通用的特征编码器。

UniTabE (ICLR 2024)  提出了“TabUnit”模块化架构。   

TabUnit 机制： 面对不同表格列名和顺序各异的问题，UniTabE 将表格拆解为最基本的单元——Cell。每个 Cell 由其数值和列名 Embedding 共同编码。通过这种方式，模型不再依赖固定的列顺序。

预训练目标： UniTabE 在 Kaggle 收集的 130 亿样本上进行了预训练，采用了多阶段的掩码重建（Masked Cell Modeling）和对比学习（Contrastive Learning）目标 。结果显示，UniTabE 在处理增量列（Incremental Columns）和跨表知识迁移方面表现优异，尤其是在列名部分重叠的场景下。   

TransTab (NeurIPS 2022)  则专注于解决“数据孤岛”问题。通过垂直分区对比学习（Vertical-Partition Contrastive Learning, VPCL），TransTab 能够将拥有不同特征子集的多个表格映射到同一语义空间，从而实现对新特征的零样本适应。这对于企业内部整合分散的数据库表具有极高的实用价值。   

4.4 基于图的结构化表征：CARTE (2024)
CARTE  另辟蹊径，将表格数据建模为图结构。   

Graphlets： CARTE 将每一行数据视为一个星型图（Star Graph/Graphlet），中心节点连接着各个特征节点，特征节点包含了值和列名信息。

知识图谱增强： 该模型的一个显著特点是利用预训练语言模型（如 BERT）初始化节点嵌入，并结合外部知识图谱（Knowledge Graphs）来增强对实体列（Entity Columns）的理解。

优势： 这种图结构天然具有置换不变性（Permutation Invariance），且特别擅长处理包含大量字符串（String）类型的表格。在包含复杂文本实体的基准测试中，CARTE 的表现显著优于传统的树模型 。   

5. 生成式模型与合成数据：质量与隐私的博弈
基础模型在表格领域的另一大应用是生成式表格数据（Generative Tabular Data）。这一方向主要解决数据隐私保护（生成合成数据替代真实敏感数据）和数据增强（平衡小样本类别）的问题。

5.1 从 GAN 到 LLM：GReaT 的突破
在 2023 年之前，表格生成主要依赖 GAN（如 CTGAN）和变分自编码器（TVAE）。然而，这些模型在捕捉长距离依赖和复杂逻辑约束方面往往力不从心。

GReaT (Generation of Realistic Tabular data, ICLR 2023)  提出利用自回归 LLM 生成表格。   

方法论： GReaT 将表格行转化为紧凑的文本序列（例如 "Age is 25, Income is 50k..."），然后微调 GPT-2 等解码器模型来学习这些序列的联合概率分布。

逻辑一致性： 相比 CTGAN，GReaT 生成的数据在逻辑一致性上表现更佳。例如，它能更好地遵循“年龄小于 5 岁的人不应有高收入”这类隐含的因果逻辑。

实验验证： 在多项“Train-on-Synthetic, Test-on-Real”基准测试中，使用 GReaT 生成数据训练出的分类器，其性能普遍优于使用 CTGAN 和 TVAE 生成数据训练的模型 。这意味着 GReaT 生成的数据更忠实地还原了真实数据的分布特性。   

5.2 隐私与公平性的新挑战
随着生成式模型的普及，2025 年的研究开始深入探讨其带来的次生影响。例如，文献  对比了基于真实数据预训练（如 TabDPT）和基于合成数据预训练（如 TabPFN）的模型在公平性（Fairness）上的差异，指出合成数据预训练可能在某些人口统计学特征上引入意想不到的偏差。此外，Table-GPT 等模型也被证明可以用于生成反事实样本（Counterfactuals），这为增强模型的可解释性提供了新思路。   

6. 全景评测与关键洞察：TFM vs. GBDT
为了客观评估 TFM 技术的成熟度，我们必须将其与传统的“霸主”GBDT 进行全方位的对比。基于 TabZilla、CC18 和 TabArena 等权威基准的测试结果，我们得出以下关键洞察。

6.1 性能对比矩阵
评估维度	TabPFN v2 / TabDPT (TFM)	XGBoost / CatBoost (GBDT)	分析与洞察
小样本数据 (<10k 行)	
SOTA (100% 胜率) 

易过拟合，需复杂正则化	TFM 利用预训练先验，无需调参即可在小数据上达到最优，极大降低了使用门槛。
中等数据 (10k-100k 行)	极具竞争力 (87% 胜率)	强劲，但需大量算力调参	随着 TabPFN v2 上下文长度的扩展，TFM 在此区间已开始占据上风。
大规模数据 (>100k 行)	显存/计算瓶颈，推理慢	SOTA，训练推理极快	树模型在处理大规模同构数据时依然具有计算效率上的绝对优势。
多模态/含文本列	极强 (TabLLM/CARTE)	弱，需复杂特征工程	TFM 天然适合处理混合模态数据，无需人工进行 Target Encoding 或文本向量化。
冷启动/零样本	支持 (无需训练)	不支持 (必须训练)	TFM 实现了“AutoML”的终极目标：无训练、无调参、即时预测。
  
6.2 核心洞察：归纳偏置的胜利
分析表明，TFM 并非要在所有场景下取代 GBDT，而是在 GBDT 的短板领域实施了“降维打击”。

归纳偏置的差异： GBDT 的核心归纳偏置是“特征空间的超平面切割”，它擅长在数据充足时寻找强特征边界。然而，当数据稀疏或噪声极大时，GBDT 容易迷失。相反，TFM（尤其是 TabPFN）的归纳偏置源于其预训练阶段见过的数百万个数据集的分布规律（Meta-Knowledge）。它学会了“如何学习”，因此在信息匮乏时能依靠先验知识做出更合理的推断。

缩放定律的启示： TabDPT 的成功表明，随着数据量的指数级增加，TFM 的性能曲线尚未饱和。这意味着未来如果出现“表格领域的 Common Crawl”（即互联网规模的高质量表格语料库），TFM 有可能在全量程上击败 GBDT，重现 NLP 领域的历史。

7. 2025 年后的研究趋势预测
基于 2024-2025 年的技术爆发，我们对未来 3-5 年的表格基础模型研究做出以下预测。

7.1 趋势一：真实数据预训练的复兴 (The Renaissance of Real-World Data)
TabPFN 虽然取得了巨大成功，但其依赖合成数据的模式可能已接近天花板。TabDPT 和 Real-TabPFN  的研究表明，真实数据包含合成数据无法模拟的复杂相关性、长尾分布和脏数据模式。   

预测： 2026 年前将出现类似 Pile 或 Common Crawl 的开源大规模表格预训练数据集（包含 Web Tables, CSVs, Excel 文件, 数据库 Dump）。未来的 SOTA 模型预训练将转向“真实数据为主，合成数据为辅（用于补充极端案例和因果结构）”的混合策略。

7.2 趋势二：多模态通用表格智能体 (Multimodal Tabular Agents)
当前的 TFM 大多专注于分类/回归预测，但这只是表格应用的一小部分。未来的模型将是多任务通用智能体。

时序与表格的统一： 表格数据往往带有时间戳。TabPFN 团队已经发布了将表格模型扩展到时间序列预测（Time Series Forecasting）的工作 。未来将出现统一处理静态表格和动态时序的基础模型。   

交互式数据科学： 模型不仅能预测 y，还能像 Table-GPT 那样解释数据含义、生成可视化代码（Python/Matplotlib）、自动清洗脏数据、甚至根据业务目标提出优化建议。

7.3 趋势三：高效推理与端侧蒸馏 (Efficient Inference & Distillation)
为了在工业界大规模替代 XGBoost，TFM 必须解决 Transformer 的 O(N 
2
 ) 复杂度问题。

技术路径： TabPFN v2.5 的蒸馏引擎指明了方向。未来将出现更多针对表格结构的线性注意力机制（Linear Attention） 或 Mamba/SSM 架构 的应用。此外，专门针对表格特征的量化技术（Quantization）也将成为热点，以支持在边缘设备上运行 TFM。

7.4 趋势四：可解释性与因果推理 (Explainability & Causal Reasoning)
企业用户对“黑盒”Transformer 的信任度天然低于树模型（后者可直观输出特征重要性）。

发展方向： 新一代 TFM 将内置因果推断模块。通过 Chain-of-Table 类似的技术，模型不仅给出预测结果，还能给出推理路径甚至反事实解释（Counterfactual Explanations），例如：“如果将该用户的贷款额度降低 10%，其违约概率将降低 5%，因为模型参考了类似特征分布的群体 X。”

8. 结论
2022 年至 2025 年是表格数据基础模型从“概念验证”走向“工业可用”的关键时期。

TabPFN v2 的出现宣告了小样本表格学习的终结——在 1 万条数据以下，预训练模型已经可以彻底取代人工调优的 XGBoost，实现了真正的 AutoML。

TabDPT 则为领域的长远发展点亮了灯塔——缩放定律证明了只要有足够的数据和算力，表格模型也能像 LLM 一样涌现出强大的通用智能。

Table-GPT 和 Chain-of-Table 展示了 LLM 在处理复杂表格推理和语义理解上的无限潜力。

尽管目前在大规模数据集的训练成本和推理延迟上仍面临挑战，但 TFM 的技术护城河正在快速构建。对于学术界和产业界而言，现在是时候重新审视手中的表格数据策略，从“寻找更好的特征工程”转向“构建更好的基础模型”了。我们正处于表格智能（Tabular Intelligence）爆发的前夜。


openreview.net
Tabby: Tabular Adaptation for Language Models - OpenReview
在新窗口中打开

arxiv.org
LaTable: Towards Large Tabular Models - arXiv
在新窗口中打开

arxiv.org
arXiv:2210.10723v2 [cs.CL] 17 Mar 2023
在新窗口中打开

notes.aimodels.fyi
Table-GPT: Table-tuned GPT for Diverse Table Tasks - AIModels.fyi
在新窗口中打开

research.google
Chain-of-table: Evolving tables in the reasoning chain for table understanding
在新窗口中打开

arxiv.org
From Supervised to Generative: A Novel Paradigm for Tabular Deep Learning with Large Language Models - arXiv
在新窗口中打开

github.com
Representation Learning for Tabular Data: A Comprehensive Survey - GitHub
在新窗口中打开

arxiv.org
[2511.08667] TabPFN-2.5: Advancing the State of the Art in Tabular Foundation Models
在新窗口中打开

cs.toronto.edu
TabDPT: Scaling Tabular Foundation Models on Real Data - Department of Computer Science
在新窗口中打开

proceedings.iclr.cc
UNITABE: A UNIVERSAL PRETRAINING PROTOCOL FOR TABULAR FOUNDATION MODEL IN DATA SCIENCE - ICLR Proceedings
在新窗口中打开

transtab.readthedocs.io
Welcome to transtab documentation! — transtab alpha documentation
在新窗口中打开

arxiv.org
CARTE: Pretraining and Transfer for Tabular Learning - arXiv
在新窗口中打开

arxiv.org
TabLLM: Few-shot Classification of Tabular Data with Large Language Models - arXiv
在新窗口中打开

paperdigest.org
Most Influential KDD Papers (2024-09 Version) - Paper Digest
在新窗口中打开

arxiv.org
Chain-of-Table: Evolving Tables in the Reasoning Chain for Table Understanding - arXiv
在新窗口中打开

arxiv.org
[2310.09263] Table-GPT: Table-tuned GPT for Diverse Table Tasks - arXiv
在新窗口中打开

github.com
microsoft/Table-GPT - GitHub
在新窗口中打开

emergentmind.com
TabPFN: Transformer for Tabular Data - Emergent Mind
在新窗口中打开

arxiv.org
A Closer Look at TabPFN v2: Strength, Limitation, and Extension - arXiv
在新窗口中打开

arxiv.org
A Closer Look at TabPFN v2: Understanding Its Strengths and Extending Its Capabilities
在新窗口中打开

openreview.net
TabDPT: Scaling Tabular Foundation Models - OpenReview
在新窗口中打开

arxiv.org
TabDPT: Scaling Tabular Foundation Models on Real Data - arXiv
在新窗口中打开

scribd.com
AI For Clean Energy Grid | PDF | Electricity Generation - Scribd
在新窗口中打开

arxiv.org
TabDPT: Scaling Tabular Foundation Models on Real Data - arXiv
在新窗口中打开

arxiv.org
TabDPT: Scaling Tabular Foundation Models - arXiv
在新窗口中打开

arxiv.org
UniTabE: A Universal Pretraining Protocol for Tabular Foundation Model in Data Science
在新窗口中打开

semanticscholar.org
TransTab: Learning Transferable Tabular Transformers Across Tables - Semantic Scholar
在新窗口中打开

github.com
soda-inria/carte: Repository for CARTE: Context-Aware Representation of Table Entries
在新窗口中打开

arxiv.org
GReaTER: Generate Realistic Tabular data after data Enhancement and Reduction - arXiv
在新窗口中打开

arxiv.org
[2210.06280] Language Models are Realistic Tabular Data Generators - arXiv
在新窗口中打开

jatit.org
CTGAN VS TGAN? WHICH ONE IS MORE SUITABLE FOR GENERATING SYNTHETIC EEG DATA
在新窗口中打开

medinform.jmir.org
Synthetic Tabular Data Based on Generative Adversarial Networks in Health Care: Generation and Validation Using the Divide-and-Conquer Strategy - JMIR Medical Informatics
在新窗口中打开

arxiv.org
Towards Fair In-Context Learning with Tabular Foundation Models - arXiv
在新窗口中打开

arxiv.org
Real-TabPFN: Improving Tabular Foundation Models via Continued Pre-training With Real-World Data - arXiv
在新窗口中打开

arxiv.org
[2501.02945] From Tables to Time: How TabPFN-v2 Outperforms Specialized Time Series Forecasting Mo