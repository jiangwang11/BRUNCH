大语言模型与推荐系统融合研究综述：从特征增强到智能代理的范式演进 (2022–2025)
1. 引言：范式重构与语义鸿沟的跨越
1.1 推荐系统的演化脉络与瓶颈
自互联网诞生以来，推荐系统（Recommender Systems, RS）已成为解决信息过载、连接用户与内容的关键基础设施。回顾其发展历程，我们可以清晰地识别出从基于规则、协同过滤（Collaborative Filtering, CF）到深度学习（Deep Learning, DL）的三次技术跃迁。以矩阵分解（Matrix Factorization, MF）为代表的协同过滤算法，通过将用户和物品映射到低维隐向量空间，成功捕捉了交互行为中的二阶关联。随后的神经协同过滤（Neural Collaborative Filtering, NCF）与序列推荐模型（如 GRU4Rec, SASRec, BERT4Rec）进一步引入了非线性变换与注意力机制，极大地提升了对用户历史行为序列的建模能力。

然而，这一以“ID 为中心”（ID-based）的传统范式在 2022 年前后遭遇了难以突破的理论瓶颈，即“语义鸿沟”（Semantic Gap）。传统推荐模型将每个用户和物品视为孤立的 ID 标识符（Token），其语义信息仅通过随机初始化的嵌入向量（Embedding）在训练过程中习得。这种机制导致了两个根本性缺陷：

冷启动问题（Cold Start Problem）： 对于缺乏交互记录的新物品或新用户，模型无法学习到有效的 ID 嵌入，导致推荐失效。尽管有引入侧边信息（Side Information）的尝试，但 ID 模型难以深入理解文本、图像等内容的深层语义。

可解释性缺失（Lack of Explainability）： 深度推荐模型通常被视为“黑盒”，难以向用户解释为何推荐该物品。基于路径或注意力的解释往往局限于数学相关性，而非符合人类逻辑的因果推理。

1.2 大语言模型的介入与 LLM4Rec 的兴起
2022 年底，以 ChatGPT 为代表的大语言模型（Large Language Models, LLMs）的爆发，为打破上述瓶颈提供了全新的契机。LLM 在海量语料上预训练所习得的通用世界知识（World Knowledge）、卓越的自然语言理解（NLU）与逻辑推理（Reasoning）能力，使其具备了理解复杂用户意图和物品内容的先天优势。

学术界迅速响应，形成了一个被称为 LLM4Rec（Large Language Models for Recommendation）的活跃研究领域。这一领域的演进速度极快，从最初仅利用 BERT 等模型提取文本特征（Feature Extraction），迅速发展到将推荐任务转化为生成式语言任务（Generative Recommendation），再到 2024-2025 年涌现的基于智能代理（Agent）和检索增强生成（RAG）的复杂系统。

1.3 综述范围与贡献
本报告旨在对 2022 年至 2025 年初 LLM 在推荐系统中的融合应用进行详尽的学术综述。我们不仅关注模型架构的演变，更致力于深入剖析背后的技术细节、实验结论的普适性以及未解决的挑战。报告将涵盖 P5、TALLRec、Chat-REC、InteRecAgent、RecMind、LLMRec、ColdRAG 及 ExplainRec 等代表性工作，并依据技术范式将其严谨分类。此外，我们还将基于最新的预印本论文，预测 2025 年后的技术趋势，包括边缘侧部署、多模态原生推荐及可信对齐等方向。

2. 理论框架与技术分类体系
为了系统地解构 LLM 与推荐系统的融合路径，本文不再仅仅依据时间线罗列，而是基于模型在大规模推荐流水线中的角色（Role）及参数调整方式（Tuning Strategy），构建了一个多维度的分类体系。

2.1 基于训练范式的分类：微调 vs. 提示
这一维度区分了 LLM 是通过参数更新来适配推荐任务，还是仅作为冻结的推理引擎。

范式	定义与技术特点	代表性工作	优势分析	局限性与挑战
LLM 重训练 (Fine-tuning)	
定义：解冻 LLM 的全部或部分参数（如适配器层），利用推荐领域的标注数据（用户-物品对）进行有监督微调。


技术：广泛采用参数高效微调（PEFT）技术，如 LoRA (Low-Rank Adaptation)、P-Tuning，以及全量微调（Full Fine-tuning）。数据通常被格式化为指令（Instruction）形式。

P5 


TALLRec 


ExplainRec 


LlaMA-E

深度适配：模型能深刻理解推荐任务的特定模式（如评分分布、排序逻辑）。


性能卓越：在特定数据集上往往能达到或超越传统 SOTA（State-of-the-Art）。


领域知识注入：有效将协同过滤信号注入语言模型。

成本高昂：训练需要大量算力与显存。


灾难性遗忘：微调可能导致 LLM 丧失通用的对话或推理能力。


数据过拟合：在小样本上容易过拟合，需精心设计正则化。

LLM 复用 (Prompting)	
定义：保持 LLM 参数完全冻结，仅通过设计精巧的文本提示（Prompt）引导模型输出结果。


技术：包括零样本提示（Zero-shot）、少样本上下文学习（In-Context Learning, ICL）及链式思维（Chain-of-Thought, CoT）。

Chat-REC 


ColdRAG 


PromptRec 


NIR-Prompt

零训练成本：无需反向传播，即插即用。


冷启动友好：利用 LLM 的通用知识解决新物品推荐。


灵活性高：可随时调整 Prompt 策略以适应不同任务。

性能天花板：准确率通常低于微调模型，难以捕捉复杂的协同过滤模式。


上下文限制：Prompt 长度受限于 Context Window，无法输入长用户历史。


依赖模型能力：高度依赖底座模型（如 GPT-4）的推理能力。

  
2.2 基于系统角色的分类
特征编码器（Feature Encoder）： LLM 仅用于生成物品描述或用户评论的语义向量（Embedding），这些向量被输入到传统的 ID 模型（如 SASRec）中作为辅助特征。这是工业界早期落地的首选方案，因为它不改变现有的推理链路。

生成式推荐器（Generative Recommender）： 这是一个根本性的范式转移。模型不再输出评分或概率，而是直接生成目标物品的名称（Title）或特定 ID。P5 和 TALLRec 是此方向的先驱。

决策控制代理（Decision Agent）： LLM 充当系统的“大脑”，负责意图识别、规划（Planning）和工具调用（Tool Use），协调检索器（Retriever）和排序器（Ranker）完成复杂任务。InteRecAgent 和 RecMind 是典型代表。

数据合成与增强器（Data Factory）： 利用 LLM 生成合成交互数据、补全缺失属性或模拟用户反馈，用于训练小模型。LLMRec 和 Agent4Rec 属于此类。

3. 生成式推荐范式的确立：从 P5 到 TALLRec (2022-2023)
2022 年至 2023 年是生成式推荐（Generative Recommendation）的奠基之年。研究者们试图验证一个核心假设：是否可以将推荐任务完全形式化为自然语言处理（NLP）任务，从而利用 Transformer 架构的强大序列建模能力？

3.1 P5：统一的大模型推荐范式
P5 (Pretrain, Personalized Prompt & Predict Paradigm)  是该领域具有里程碑意义的工作，它首次提出将各类推荐子任务统一到一个共享的 Encoder-Decoder 框架中。   

3.1.1 核心架构与方法论
P5 基于 T5 (Text-to-Text Transfer Transformer) 架构，参数量分为 Base (223M) 和 Small 两版。其核心思想是“推荐即语言处理”（Recommendation as Language Processing）。

多任务统一： P5 将推荐系统中的五大核心任务——序列推荐（Sequential Recommendation）、评分预测（Rating Prediction）、解释生成（Explanation Generation）、评论摘要（Review Summarization）和直接推荐（Direct Recommendation）——全部转化为“输入文本 -> 输出文本”的形式。

个性化提示模版（Prompt Families）： 为了区分不同任务，P5 设计了 5 个提示族（Prompt Families）。例如，对于序列推荐任务，模版可能设计为：“用户 购买了，基于此历史，该用户下一个可能购买什么？”。这种设计使得模型能够在一个权重下通过不同的 Prompt 切换任务 。   

训练细节： P5 使用 AdamW 优化器在 4 张 NVIDIA RTX A5000 上训练了 10 个 Epoch，峰值学习率为 1e-3 。输入序列最大长度被截断为 512 tokens。   

3.1.2 ID 索引的挑战与创新
P5 在处理物品 ID 时遇到了独特的挑战。传统的 NLP Tokenizer（如 SentencePiece）会将数字 ID 切分为无意义的子词（Sub-words）。

序列索引 vs. 随机索引： P5 的后续研究  发现，如果直接使用数据集中原始的连续整数 ID（例如 1001, 1002...），会导致严重的信息泄露（Data Leakage），因为模型会倾向于预测数字上相邻的 ID。为了解决这个问题，P5 团队在 OpenP5  和后续实验中采用了独立索引（Independent Indexing）或随机索引（Random Indexing）策略，强制模型学习 ID 之间的协同关系而非字面上的数字规律。此外，也有学者尝试引入语义 ID (Semantic ID)，即利用物品的层级类别或标题生成的 Hash 码作为 ID，以保留语义信息 。   

3.1.3 实验结论与局限
实验表明，在零样本（Zero-shot）和冷启动场景下，P5 展现了惊人的适应力，显著优于未经过针对性训练的传统模型。然而，在全量数据（Full-shot）的 Top-K 推荐任务上，P5 在 MovieLens 等数据集上的表现并未完全超越专门优化的 SASRec 模型 。这揭示了生成式模型在处理纯 ID 匹配任务时，可能受限于自回归生成的效率和准确性。   

3.2 TALLRec：指令微调的高效对齐
针对 LLM 参数量大、训练成本高的问题，TALLRec (Tuning Framework to Align LLM with Recommendation)  提出了基于 LoRA 的轻量级微调方案，标志着推荐 LLM 进入了“指令微调”时代。   

3.2.1 架构设计
TALLRec 选用 LLaMA-7B 作为底座模型，通过 LoRA (Low-Rank Adaptation) 技术仅微调低秩矩阵，冻结大部分预训练参数。这种方法使得在单张消费级 GPU（如 RTX 3090）上进行微调成为可能。

3.2.2 两阶段微调策略
TALLRec 提出了独特的两阶段训练流程 ：   

第一阶段：通用指令微调 (Alpaca Tuning)： 使用 Alpaca 数据集（约 52k 条通用指令）对模型进行微调。这一步的目的是激活 LLM 的指令跟随（Instruction Following）能力，使其能够理解“回答是/否”或“按顺序列出”等格式要求。

第二阶段：推荐指令微调 (Rec-Tuning)： 使用构建的推荐指令数据进行微调。指令被格式化为 JSON 结构，包含 Instruction（任务描述）、Input（用户历史序列 + 候选物品）和 Output（用户是否喜欢，Yes/No）。

示例 Prompt： {"Instruction": "根据用户的历史购买记录，判断用户是否会喜欢目标商品。", "Input": "历史记录：[手机, 耳机, 充电宝]。目标商品：手机壳。", "Output": "Yes"} 。   

3.2.3 实验结果：少样本能力的爆发
TALLRec 最核心的贡献在于证明了 LLM 在**少样本（Few-shot）**场景下的统治力。

数据对比： 在 MovieLens 和 Amazon Book 数据集上，仅需 16 个样本（16-shot），TALLRec 的 AUC 指标即可达到 0.6724，显著优于传统强基线 SASRec (0.5043) 和 GRU4Rec (0.4907) 。   

跨域泛化： TALLRec 还展现了强大的跨域能力。在 Book 数据集上训练的模型，直接迁移到 Movie 领域进行推荐，其性能衰减远小于传统模型，证明了 LLM 习得的不仅是数据共现，更是通用的偏好推理逻辑 。   

4. 智能代理与工具学习：从被动预测到主动规划 (2023-2024)
随着 GPT-4 等强推理模型的出现，2023 年下半年至 2024 年，研究焦点从单一的推荐预测转向了能够处理复杂用户交互的 Agentic Recommender Systems。

4.1 Chat-REC：对话式推荐的交互增强
Chat-REC  是探索 LLM 作为对话式推荐接口的先驱工作。它不再将推荐视为单次 API 调用，而是视为一个持续的多轮对话过程。   

4.1.1 交互机制
Chat-REC 利用 ChatGPT 的 API，设计了精细的 Prompt Engineering 流程。它首先将用户的历史交互转化为自然语言描述，然后结合候选物品池，引导 ChatGPT 进行筛选。

冷启动与跨域惊喜： Chat-REC 的一个重要发现是，LLM 能够利用其内部知识库实现令人惊讶的跨域推荐。例如，当用户表达对《指环王》电影的喜爱时，ChatGPT 能顺畅地推荐原著小说或相关的中世纪风格游戏，这种跨域联想能力是传统基于 ID 的协同过滤模型完全不具备的 。   

4.2 InteRecAgent：工具增强的推荐大脑
为了解决 LLM 无法处理大规模候选集（Context Window 限制）和缺乏实时数据的问题，InteRecAgent  提出了“LLM 为大脑，推荐模型为工具”的 Agent 架构。   

4.2.1 候选记忆总线 (Candidate Memory Bus)
这是 InteRecAgent 最具创新性的设计 。由于无法将电商平台百万级的商品 ID 全部塞入 Prompt，InteRecAgent 设计了一个外部的候选记忆总线。   

工作原理： 总线作为一个动态的缓存区，存储当前对话上下文中的候选物品集（Candidate Item Set）。LLM 不直接处理这些 ID，而是通过生成 SQL 查询或 API 调用指令来操作总线。例如，LLM 发出指令 Filter(Category='Action')，总线执行过滤操作后，仅返回结果的数量或摘要给 LLM。这种机制极大地降低了 Token 消耗，使系统具备了处理大规模数据的能力。

4.2.2 工具学习与动态规划
InteRecAgent 预定义了一套核心工具集 ：   

信息查询工具 (Information Query)： 查询商品属性（价格、发布日期）。

检索工具 (Item Retrieval)： 基于 SQL 或向量检索获取候选集。

排序工具 (Item Ranking)： 调用传统的精排模型（如 LightGCN）对候选集打分。

在执行任务时，InteRecAgent 采用 “Plan-first” 策略，先生成完整的工具调用链（如 Query -> Retrieve -> Rank），再逐步执行。实验表明，这种架构在任务完成率（Task Completion Rate）和用户满意度上显著优于仅依赖 Prompt 的 GPT-4 。   

4.3 RecMind：具有自我激励能力的规划代理
RecMind  进一步强化了 Agent 的推理规划能力，针对推荐场景中用户意图模糊的痛点，提出了 Self-Inspiring (自我激励) 算法。   

4.3.1 自我激励规划 (Self-Inspiring Planning)
深受“思维树”（Tree of Thoughts）的启发，RecMind 在每一步决策时，不仅依据当前状态，还会回溯并“反思”所有已探索的历史状态 。   

机制： 模型会在推理过程中生成多个潜在的推理路径（Reasoning Paths），并通过自我评估（Self-Evaluation）选择最优路径。如果当前路径受阻（例如检索结果为空），模型会触发“自我激励”机制，回溯到上一步并尝试新的搜索策略（如放宽检索条件）。

效果： 这种机制使得 RecMind 在处理复杂的组合型查询（如“推荐一部适合和孩子一起看的、评分高的、2020年后的科幻电影”）时，表现出了极高的鲁棒性。

5. 数据增强与用户模拟：LLM 的隐性价值 (2024)
除了作为直接面向用户的推荐接口，LLM 在后台数据处理和系统评估中的作用同样不可小觑。

5.1 LLMRec：图结构增强与降噪
面对推荐系统中普遍存在的数据稀疏性问题，LLMRec  提出利用 LLM 来增强传统的交互图（Interaction Graph）。   

5.1.1 三维增强策略
LLMRec 利用 LLM 的知识库，从三个维度对 User-Item 图进行增广：

强化边 (Reinforcing Edges)： 询问 LLM “基于用户购买了 A，他是否可能购买 B？”，若回答肯定且置信度高，则在图中添加一条虚拟边。

增强节点属性 (Enhancing Attributes)： 利用 LLM 补全物品缺失的描述信息，丰富节点特征向量。

用户画像生成 (User Profiling)： 基于交互历史，生成用户的自然语言画像，并编码为向量 。   

5.1.2 降噪与性能
为了防止 LLM 产生幻觉（Hallucination）引入噪声边，LLMRec 设计了基于 MAE (Masked Autoencoder) 的去噪机制，剔除那些与原始分布差异过大的增强数据。实验结果显示，在 Netflix 和 MovieLens 数据集上，LLMRec 相比 SOTA 基线（如 MMSSL）提升了 13.95% (Recall@10) 和 21.43% (NDCG@10) 。   

5.1.3 代价分析
然而，这种性能提升是有代价的。LLMRec 的预处理和增强过程极其耗时。虽然推理阶段仍使用轻量级 GNN 模型，但整体 pipeline 的构建成本大幅增加。有分析指出，在全链路中引入 LLM 可能会导致推理延迟增加 1000 倍 ，这使得其目前更多应用于离线数据工厂。   

5.2 Agent4Rec：生成式用户模拟与评估
推荐系统的在线评估（A/B Testing）昂贵且有风险，而离线指标往往与真实用户体验脱节。Agent4Rec  尝试构建一个由 1000 个 LLM 驱动的生成式智能体 组成的仿真环境。   

5.2.1 社会化特征建模
Agent4Rec 不仅让 Agent 进行评分，还通过 Prompt 赋予它们特定的社会心理特征 ：   

从众性 (Conformity)： 倾向于跟随大众评分。

活跃度 (Activity)： 交互频率的高低。

多样性 (Diversity)： 对不同类目物品的接受程度。

5.2.2 仿真真实性与局限
实验发现，Agent4Rec 生成的评分分布能够大致复现真实数据集（如 MovieLens）的长尾规律。然而，深入分析  揭示了其局限性：LLM Agent 往往倾向于给出过于极端的评分（极好或极差），且在多轮交互中容易出现“疲劳退出”行为，导致与真实人类的留存曲线不符。这表明，虽然 Agent Simulation 是一个极具潜力的方向，但目前的 LLM 仍需在行为对齐 (Behavioral Alignment) 上进一步优化。   

6. 2025 年前沿突破：冷启动与可解释性的终极方案
进入 2025 年，研究逐渐从单纯的“应用 LLM”转向解决具体的顽疾。最新的预印本和会议论文显示，RAG 和 可解释性 是两大核心突破口。

6.1 ColdRAG：检索增强的冷启动推荐 (2025)
ColdRAG  是 2025 年针对物品冷启动问题提出的创新框架。它放弃了单纯依靠 LLM 内部知识生成的思路，转而采用 RAG (Retrieval-Augmented Generation)。   

6.1.1 动态知识图谱构建
对于没有任何交互记录的新物品，ColdRAG 利用 LLM 从其元数据（标题、描述、属性）中提取实体和关系，动态构建一个小型的知识图谱 (KG)。例如，从新书的简介中提取“作者”、“流派”、“主题”等实体 。   

6.1.2 多跳推理 (Multi-hop Reasoning)
在推荐时，ColdRAG 并不直接生成推荐列表，而是先在构建的 KG 上进行多跳推理，寻找用户历史偏好与新物品之间的连接路径（例如：用户喜欢《黑客帝国》 -> 关联实体“赛博朋克” -> 关联新书《神经漫游者》）。这种基于显式路径的检索，使得 ColdRAG 在极端冷启动场景下的 Recall 和 NDCG 指标显著优于仅基于 Prompt 的 Zero-shot 基线 。   

6.2 ExplainRec：偏好归因与多模态统一 (2025)
ExplainRec  试图在一个统一框架内解决准确性与可解释性这对长期存在的矛盾。   

6.2.1 偏好归因微调 (Preference Attribution Tuning)
ExplainRec 扩展了 TALLRec 的指令微调范式，引入了 “偏好归因” 任务。它要求模型在输出“推荐”决策的同时，必须生成基于用户历史和物品属性的逻辑解释。

Prompt 改进： 不仅仅是 Output: Yes，而是 Output: Yes, because the user has shown a strong interest in dystopian themes (e.g., 1984, Brave New World), and the target item fits this genre while offering a modern narrative..   

6.2.2 零样本偏好迁移 (Zero-Shot Preference Transfer)
针对新用户，ExplainRec 构建了一个通用偏好知识库 (Universal Preference Knowledge Base)，利用 Meta-learning 机制将从其他领域学到的通用偏好模式（如“年轻男性用户通常偏好快节奏动作片”）迁移到当前任务。实验显示，ExplainRec 在新用户冷启动场景下的 AUC 比 TALLRec 提升了 0.9% 。   

7. 综合实验结论与核心洞察
综合 2022-2025 年的百余篇文献，我们可以提炼出以下核心洞察，为未来的研究与落地提供指导。

7.1 性能与数据量的非线性关系：Few-shot 是甜点区
多项研究（TALLRec, P5, ExplainRec）一致表明，LLM4Rec 的核心优势在于 Few-shot（少样本） 场景。在训练样本极少（< 100 samples）的情况下，LLM 凭借先验知识可以轻松碾压需要大量数据拟合的 ID 模型（AUC 提升可达 10% 以上）。然而，随着训练数据量的增加（> 10k samples），LLM 的性能提升趋于平缓，甚至在全量数据下可能不如经过高度优化的轻量级模型（如 SASRec）。这提示我们，LLM 不应被视为 ID 模型的简单替代品，而应定位为冷启动专家或长尾补全者。   

7.2 推理延迟：不可忽视的落地障碍
尽管 LLM 效果惊艳，但其推理成本是巨大的。基准测试显示，基于 7B 参数 LLM 的推荐器，其推理延迟（Inference Latency）是传统 LightGCN 等模型的 1000 倍以上（秒级 vs. 毫秒级）。   

结论： 在当前的算力条件下，直接将生成式 LLM 部署在拥有亿级流量的推荐系统**精排层（Ranking Layer）**是不现实的。最可行的架构是 “LLM 离线生成/重排 + ID 模型在线服务”，或者将 LLM 用于处理流量较小但价值较高的长尾请求。

7.3 ID 与文本的辩证统一
早期的 P5 试图完全用文本取代 ID，但遭遇了 Token 长度和推理效率的瓶颈；后期的 LLMRec 和 ExplainRec 则回归到了 Hybrid 模式，即在 Prompt 中同时注入语义描述（Text）和协同信号（Collaborative Signal，如邻居节点的 ID 或通过 Collaborative Indexing 生成的 ID）。事实证明，“语义 + 协同” 才是推荐系统的终极形态 。   

8. 2025 年后的趋势预测
基于当前的技术演进曲线，我们对 2025 年后的发展趋势做如下预测：

8.1 边缘侧小模型 (Edge-LLM) 的爆发
为了解决推理延迟和隐私问题，未来的推荐 LLM 将向端侧迁移。利用模型蒸馏（Distillation）和量化（Quantization）技术，将 7B+ 的模型压缩至 1B 甚至 500M 参数，直接部署在用户的手机端。

预测： 2025 年后，我们将看到大量 Edge-LLM 论文，探讨如何在移动端进行实时的、隐私保护的重排和生成 。   

8.2 多模态原生推荐 (Multimodal-Native RecSys)
目前的 LLM4Rec 大多通过“视觉转文本”（Image-to-Text）的中间步骤来处理多模态数据，这会导致信息损耗。随着 GPT-4o、Gemini 1.5 等原生多模态模型（Native Multimodal Models）的普及，未来的推荐系统将直接输入视频帧和音频波形，实现真正的基于内容理解的推荐。

预测： 视频推荐（Video Rec）将迎来革命，模型将能够理解视频的具体情节和情感色彩，而不仅仅是依赖标签 。   

8.3 可信推荐与价值观对齐 (Trustworthy & Alignment)
随着 Agent4Rec 等模拟技术的发展，如何防止推荐系统利用 LLM 强大的说服力诱导用户成瘾，或推荐带有偏见（Bias）的内容，将成为伦理研究的重点。

预测： 未来的推荐目标函数将从单一的“点击率最大化”转向 “用户价值最大化”，研究重点将包括去偏（Debiasing）、公平性（Fairness）以及与人类价值观的对齐（Alignment）。   

9. 结语
2022 至 2025 年，大语言模型与推荐系统的融合完成了一次从“特征外挂”到“范式重构”的壮阔演进。P5 和 TALLRec 证明了生成式推荐的可行性，InteRecAgent 和 RecMind 拓展了系统的决策边界，而 ColdRAG 和 ExplainRec 则为解决冷启动与可解释性难题提供了精巧的方案。

尽管推理成本和幻觉问题依然是悬在头顶的达摩克利斯之剑，但 LLM 赋予推荐系统的“语义理解”与“逻辑推理”能力是不可逆转的技术红利。未来的推荐系统，必将是一个融合了 ID 协同记忆 与 LLM 语义大脑 的混合智能体，它不仅能预测你“喜欢什么”，更能理解你“为什么喜欢”，并作为你探索数字世界的忠实向导。


yongfeng.me
Recommendation as Language Processing (RLP): A Unified Pretrain, Personalized Prompt & Predict Paradigm (P5) - Yongfeng Zhang
在新窗口中打开

scispace.com
TALLRec: An Effective and Efficient Tuning Framework to Align Large Language Model with Recommendation - SciSpace
在新窗口中打开

arxiv.org
ExplainRec: Towards Explainable Multi-Modal Zero-Shot Recommendation with Preference Attribution and Large Language Models - arXiv
在新窗口中打开

researchgate.net
Conversational Recommender System and Large Language Model Are Made for Each Other in E-commerce Pre-sales Dialogue | Request PDF - ResearchGate
在新窗口中打开

researchgate.net
Cold-Start Recommendation with Knowledge-Guided Retrieval-Augmented Generation
在新窗口中打开

arxiv.org
Benchmarking LLMs in Recommendation Tasks: A Comparative Evaluation with Conventional Recommenders - arXiv
在新窗口中打开

arxiv.org
[2203.13366] Recommendation as Language Processing (RLP): A Unified Pretrain, Personalized Prompt & Predict Paradigm (P5) - arXiv
在新窗口中打开

medium.com
VIP5 — A brief look into the multimodal recommendation systems | by Helena YH Huang
在新窗口中打开

papers.neurips.cc
Recommender Systems with Generative Retrieval
在新窗口中打开

arxiv.org
[2306.11134] OpenP5: Benchmarking Foundation Models for Recommendation - arXiv
在新窗口中打开

openreview.net
Can LLMs Outshine Conventional Recommenders? A Comparative Evaluation - OpenReview
在新窗口中打开

researchgate.net
TALLRec: An Effective and Efficient Tuning Framework to Align Large Language Model with Recommendation | Request PDF - ResearchGate
在新窗口中打开

arxiv.org
TALLRec: An Effective and Efficient Tuning Framework to Align Large Language Model with Recommendation - arXiv
在新窗口中打开

mdpi.com
TisLLM: Temporal Integration-Enhanced Fine-Tuning of Large Language Models for Sequential Recommendation - MDPI
在新窗口中打开

github.com
SAI990323/TALLRec - GitHub
在新窗口中打开

medium.com
Efficient LLM Fine-Tuning for Book & Movie Recommendations on Amazon SageMaker and Deployment on AWS Inferentia | by Nick McCarthy | Medium
在新窗口中打开

ai-scholar.tech
[Chat-REC] Proposal for LLM-based Recommendation System | AI-SCHOLAR
在新窗口中打开

ar5iv.labs.arxiv.org
Chat-REC: Towards Interactive and Explainable LLMs-Augmented Recommender System
在新窗口中打开

researchgate.net
Chat-REC: Towards Interactive and Explainable LLMs-Augmented Recommender System
在新窗口中打开

researchgate.net
Recommender AI Agent: Integrating Large Language Models for Interactive Recommendations | Request PDF - ResearchGate
在新窗口中打开

scispace.com
arXiv:2308.16505v2 [cs.IR] 1 Sep 2023 - SciSpace
在新窗口中打开

arxiv.org
[2308.16505] Recommender AI Agent: Integrating Large Language Models for Interactive Recommendations - arXiv
在新窗口中打开

news.superagi.com
A New Fusion of Language Models and Recommender Systems - InteRecAgent
在新窗口中打开

arxiv.org
RecAI: Leveraging Large Language Models for Next-Generation Recommender Systems
在新窗口中打开

amazon.science
RecMind: Large language model powered agent for recommendation - Amazon Science
在新窗口中打开

aclanthology.org
RecMind: Large Language Model Powered Agent For Recommendation - ACL Anthology
在新窗口中打开

arxiv.org
RecMind: Large Language Model Powered Agent For Recommendation - arXiv
在新窗口中打开

llmrec.github.io
LLMRec
在新窗口中打开

liner.com
LLMRec: Large Language Models with Graph Augmentation for Recommendation - Liner
在新窗口中打开

github.com
LehengTHU/Agent4Rec: [SIGIR 2024 perspective] The implementation of paper "On Generative Agents in Recommendation" - GitHub
在新窗口中打开

arxiv.org
[2310.10108] On Generative Agents in Recommendation - arXiv
在新窗口中打开

emerald.com
Recommender Systems Meet Large Language Model Agents: A Survey
在新窗口中打开

openreview.net
SIMUSER: WHEN LANGUAGE MODELS PRETEND ... - OpenReview
在新窗口中打开

aclanthology.org
SimUSER: Simulating User Behavior with Large Language Models for Recommender System Evaluation - ACL Anthology
在新窗口中打开

themoonlight.io
[Literature Review] Cold-Start Recommendation with Knowledge-Guided Retrieval-Augmented Generation - Moonlight
在新窗口中打开

arxiv.org
Adaptive Candidate Retrieval with Dynamic Knowledge Graph Construction for Cold-Start Recommendation - arXiv
在新窗口中打开

arxiv.org
Cold-Start Recommendation with Knowledge-Guided Retrieval-Augmented Generation - arXiv
在新窗口中打开

chatpaper.com
ExplainRec: Towards Explainable Multi-Modal Zero-Shot Recommendation with Preference Attribution and Large Language Models - ChatPaper
在新窗口中打开

researchgate.net
(PDF) ExplainRec: Towards Explainable Multi-Modal Zero-Shot Recommendation with Preference Attribution and Large Language Models - ResearchGate
在新窗口中打开

lonepatient.top
Arxiv今日论文| 2025-11-20 - 闲记算法
在新窗口中打开

arxiv.org
ExplainRec: Towards Explainable Multi-Modal Zero-Shot Recommendation with Preference Attribution and Large Language Models - arXiv
在新窗口中打开

medium.com
Decoding Real-Time LLM Inference: A Guide to the Latency vs. Throughput Bottleneck | by Nadeem Khan(NK) | LearnWithNK | Oct, 2025 | Medium
在新窗口中打开

arxiv.org
The Application of Large Language Models in Recommendation Systems - arXiv
在新窗口中打开

mdpi.com
LLM4Rec: A Comprehensive Survey on the Integration of Large Language Models in Recommender Systems—Approaches, Applications and Challenges - MDPI
在新窗口中打开

arxiv.org
A Survey on Large Language Models in Multimodal Recommender Systems - arXiv
在新窗口中打开

ojs.aaai.org
Harnessing Multimodal Large Language Models for Multimodal Sequential Recommendation | Proceedings of the AAAI Conference on Artificial Intelligence
在新窗口中打开

appen.com
ACL 2025: 5 Trends Shaping the Future of LLMs - Appen
在新窗口中打开

arxiv.org
A Survey of Large Language Model Empowered Agents for Recommendation and Search: Towards Next-Generation Infor