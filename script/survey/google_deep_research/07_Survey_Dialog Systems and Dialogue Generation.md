大语言模型时代的对话系统与对话生成：演进、范式与前沿（2022–2025）
1. 引言：范式转移与对话智能的重构
自 2022 年底以 ChatGPT 为代表的大语言模型（Large Language Models, LLMs）横空出世以来，自然语言处理（NLP）领域，尤其是对话系统（Dialogue Systems）的研究范式经历了根本性的重构。在深度学习时代早期，对话系统被严格划分为任务型对话（Task-oriented Dialogue, TOD）与开放域对话（Open-domain Dialogue, ODD）两个泾渭分明的流派。前者致力于通过槽位填充（Slot Filling）和对话状态追踪（DST）解决特定的垂直领域问题，追求精确性；后者则侧重于闲聊（Chit-chat），追求语义的连贯性与情感共鸣。然而，2023 年至 2025 年的文献表明，这种二元对立的局面已被打破。基于 LLM 的统一对话代理（Unified Conversational Agents）不仅在单一模型中融合了任务执行与闲聊能力，更涌现出了工具使用（Tool Use）、多步推理（Reasoning）、长期记忆（Long-term Memory）以及多智能体协作（Multi-Agent Collaboration）等前所未有的特性 。   

本综述旨在对 2022 年至 2025 年间对话系统领域的变革性工作进行详尽的学术梳理。这一时期，研究重心已从单一的模型架构（如 Transformer 变体）优化，转向了更高层级的系统工程与认知能力构建。核心议题包括：如何通过偏好对齐（Alignment）将预训练模型的概率分布转化为符合人类价值观的对话策略；如何通过检索增强生成（RAG）克服参数化知识的幻觉与时效性限制；以及如何通过代理（Agent）架构赋予模型自主规划与环境交互的能力。此外，随着生成能力的指数级提升，评估范式也经历了从 N-gram 统计指标（BLEU/ROUGE）向基于 LLM 的语义评估（LLM-as-a-Judge）的彻底转型 。   

本文将深入剖析上述领域的演进逻辑。不同于一般的文献罗列，本文将侧重于分析方法论背后的理论动因与技术迭代路径。文章结构如下：第二部分探讨基础模型的对齐与优化技术，重点分析从 RLHF 到 DPO 的算法演进；第三部分论述检索增强生成（RAG）从被动检索向主动纠错的范式转变；第四部分聚焦于智能体架构，分析工具学习与多智能体协作的涌现；第五部分探讨长期记忆机制的工程化实现；第六部分详述基于 LLM 的评估新标准；最后，基于 2025 年初的最新文献，预测未来的研究趋势。

2. 基础模型优化与对齐技术：从 RLHF 到 DPO
对话系统的核心驱动力已由特定任务的监督微调（SFT）转向了通用基础模型的偏好对齐。在预训练阶段，模型学习的是互联网文本的统计规律，这往往包含噪声、偏见甚至有害信息。为了构建“有用（Helpful）、诚实（Honest）、无害（Harmless）”（3H 原则）的对话系统，研究者在 2023-2024 年间对对齐算法进行了密集迭代，致力于降低强化学习的复杂性并提升对齐精度。

2.1 偏好优化算法的演进
传统的强化学习人类反馈（RLHF）通常采用 PPO（Proximal Policy Optimization）算法，需要训练独立的奖励模型（Reward Model）和评论家模型（Critic Model），流程繁琐且超参数敏感。近期的研究趋势是去除显式的奖励模型，直接在策略层面进行优化。

Direct Preference Optimization (DPO)
   

研究问题：传统的 RLHF 流程（训练奖励模型 -> PPO 优化）存在训练不稳定、计算资源消耗大以及对超参数极度敏感的问题，限制了其在开源社区的普及。

核心方法：DPO 基于 Bradley-Terry 模型推导出了最优策略与奖励函数之间的解析映射关系，证明了可以直接利用语言模型本身作为隐式的奖励模型。该方法将约束优化问题转化为一个简单的二元交叉熵分类损失函数，直接在偏好数据对（优选/厌选）上优化模型策略，完全摒弃了显式的奖励建模和强化学习采样过程。

关键实验结论：在情感控制、文本摘要和多轮对话任务中，DPO 能够以更少的计算资源（无需采样）达到甚至超越 PPO 的性能，且训练稳定性显著提高，成为 Llama 3 等现代模型微调的标准范式。

SimPO: Simple Preference Optimization
   

研究问题：DPO 虽然简化了训练流程，但其损失函数中包含对参考模型（Reference Model）的 KL 散度约束，这不仅增加了推理时的内存开销，还可能导致训练目标与生成时的推理度量（Generation Metric）不一致。

核心方法：SimPO 提出了一种无参考模型（Reference-free）的偏好优化算法，旨在进一步简化对齐流程。它在 Bradley-Terry 模型的基础上引入了长度归一化（Length Normalization）以消除长度偏差，并设定了一个目标奖励边际（Target Reward Margin）来增强不同回答之间的区分度，从而直接在策略模型上进行梯度下降。

关键实验结论：在 AlpacaEval 2 和 Arena-Hard 等高难度对话基准测试中，SimPO 在不使用参考模型的情况下，性能显著优于 DPO 及其变体，且生成的回复长度更加受控，证明了 KL 正则化在特定设置下并非必须。

Constitutional AI (CAI)
   

研究问题：完全依赖人类标注员来识别和纠正有害输出（Red Teaming）不仅成本高昂，难以扩展，而且会对标注人员造成心理创伤，同时人类反馈往往难以覆盖所有复杂的伦理边界。

核心方法：Anthropic 提出的 Constitutional AI 引入了 RLAIF（Reinforcement Learning from AI Feedback）机制。该方法首先利用一组自然语言编写的“宪法”原则（如“请选择更合乎伦理的回答”）指导 AI 批评并修改自身的有害输出以生成微调数据（监督学习阶段），随后训练一个基于偏好的奖励模型，该模型的训练信号完全来自 AI 根据宪法原则对输出的自我评估。

关键实验结论：CAI 训练出的模型（如 Claude 系列）在无害性（Harmlessness）指标上显著优于仅依赖人类反馈的模型，且在有用性（Helpfulness）上未见明显衰退，验证了通过自然语言原则指导模型自我对齐的可行性。

2.2 理论洞察与方法论对比
上述方法的演进反映了对话生成领域的一个核心趋势：从显式的外部奖励向隐式的内部约束转变。

特性	PPO (RLHF)	DPO	SimPO	Constitutional AI
优化目标	最大化显式奖励 + KL 惩罚	最大化隐式奖励对数似然比	最大化带边际的长度归一化似然比	混合（SL + RL）
参考模型	需要（用于 KL 计算）	需要（作为基准分布）	不需要	需要
奖励模型	需要独立训练	隐式（策略即奖励）	隐式	需独立训练（基于 AI 反馈）
计算复杂度	高（需采样生成）	中（单次前向传播）	低（单次前向传播，内存更省）	高（涉及多阶段生成与评估）
主要优势	理论上限高，探索能力强	稳定、简单、无需采样	资源效率极高，抗长度偏差	解决安全性与人工标注瓶颈
从 DPO 到 SimPO 的跨越表明，对话模型的对齐本质上是在调整生成概率的分布形状，使“好”的回答在概率密度上与“坏”的回答拉开距离（Margin）。SimPO 的成功进一步暗示，参考模型在某些场景下可能反而限制了模型向更优策略空间的探索。而 Constitutional AI 则从数据源头解决了对齐的扩展性问题，为未来的自动化对齐（Automated Alignment）奠定了基础。

3. 检索增强生成（RAG）与知识交互：从静态检索到主动纠错
大语言模型的参数化知识存在固有的局限性：一是幻觉（Hallucination），即模型倾向于自信地编造事实；二是时效性滞后（Knowledge Cutoff），模型无法获知训练结束后的新信息。检索增强生成（RAG）通过引入外部非参数化知识库解决了这些问题。然而，2023-2024 年的研究表明，传统的“检索-阅读-生成”（Retrieve-Read-Generate）流水线在面对复杂查询或噪声文档时显得脆弱。新一代 RAG 系统正向着主动检索（Active Retrieval）和自我纠错（Self-Correction）的方向演进。

3.1 动态与自适应检索机制
Self-RAG: Learning to Retrieve, Generate, and Critique
   

研究问题：传统 RAG 系统通常无差别地对所有输入进行检索，即使模型本身已具备相关知识，这不仅增加了延迟，还可能引入无关文档导致干扰；此外，模型缺乏对自己生成内容是否符合事实的判断能力。

核心方法：Self-RAG 训练单一的语言模型生成特殊的“反思词元”（Reflection Tokens）来控制生成过程。这些词元包括：Retrieve（决定是否需要检索）、IsRel（判断检索到的段落是否相关）、IsSup（判断生成的句子是否由段落支持）和 IsUse（评估回复的整体有用性），从而实现按需检索和自我批判。

关键实验结论：在 PubHealth 和 PopQA 等知识密集型任务中，Self-RAG 在长文本生成的准确性和引用质量上显著优于 ChatGPT 和 Llama 2-chat，且通过调节反思词元可以在推理时灵活平衡生成速度与事实准确性。

FLARE: Active Retrieval Augmented Generation
   

研究问题：在长文本生成过程中，模型往往在开头表现良好，但随着生成的进行，容易因上下文遗忘或知识耗尽而产生幻觉；现有的单次检索（One-shot Retrieval）无法支持长程生成中的动态信息需求。

核心方法：FLARE 提出了一种前瞻性的主动检索策略（Forward-Looking Active Retrieval）。它在生成过程中持续监测下一个句子的生成概率，一旦发现低置信度的词元（Low-confidence Tokens），系统就会暂停生成，利用模型预测的后续内容作为查询语句（Query）去检索相关文档，然后重新生成该句。

关键实验结论：在长篇问答和摘要生成任务中，FLARE 有效缓解了“后期幻觉”问题，其性能优于固定间隔检索和单次检索的基线模型，证明了基于置信度的动态检索策略在长文本生成中的必要性。

CRAG: Corrective Retrieval Augmented Generation
   

研究问题：现有的 RAG 系统严重依赖检索器的质量，当检索器返回无关或误导性文档时，生成模型往往会盲目采信，导致严重的“知识中毒”（Knowledge Poisoning）；且简单的检索无法处理模糊查询。

核心方法：CRAG 引入了一个轻量级的检索评估器（Retrieval Evaluator），对检索到的文档进行相关性打分，并根据置信度区间触发三种动作：对于高质量文档进行精炼（Refine）；对于错误文档触发网络搜索（Web Search）以寻找新源；对于模糊文档则进行知识重组。

关键实验结论：CRAG 作为一个即插即用的增强模块，在 PopQA、Biography 等四个数据集上显著提升了 RAG 系统的鲁棒性，特别是在检索器性能较弱的场景下，能够有效防止错误知识的传播。

3.2 机制分析：RAG 的控制论转向
上述工作标志着 RAG 系统从开环控制向闭环控制的转变。

Self-RAG 通过内化的反思词元，实现了模型对自己认知边界的感知（Metacognition）。

FLARE 通过置信度监控，建立了生成过程中的实时反馈回路。

CRAG 通过引入外部评估器和网络搜索，构建了针对检索质量的纠错机制。

这种演进趋势表明，未来的对话系统将不再是简单的“搜索引擎+文本生成器”，而是一个具备信息寻觅（Information Foraging）、相关性判断和多源信息融合能力的复杂认知系统。

4. 智能体、工具使用与记忆机制：迈向自主系统
如果说 RAG 解决了“知”的问题，那么智能体（Agent）架构则致力于解决“行”的问题。2023-2025 年间，对话系统逐渐演变为能够使用工具、规划任务并具备长期记忆的自主智能体。

4.1 工具学习与任务规划
Toolformer: Language Models Can Teach Themselves to Use Tools
   

研究问题：LLM 本质上是文本预测模型，缺乏执行精确数学运算、获取实时信息或调用外部 API 的能力，且依赖大量人工标注数据来学习工具使用不仅成本高昂，还难以适应新工具。

核心方法：Toolformer 提出了一种自我监督的学习方法。它利用基础模型在原始文本中采样潜在的 API 调用位置，实际执行这些调用，并计算调用结果是否降低了后续文本的困惑度（Perplexity）。通过保留那些有助于预测的调用，模型构建了自己的微调数据集，从而学会了以自回归的方式生成 API 调用。

关键实验结论：该模型在零样本（Zero-shot）设置下，在数学推理（使用计算器）和问答（使用维基百科搜索）任务中，不仅显著超越了更大参数规模的基础模型（如 GPT-3），而且能够流畅地在文本生成与工具调用间切换。

MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework
   

研究问题：在处理如软件开发等复杂的长程任务时，单一智能体容易陷入逻辑死循环、产生累积错误或忽视全局一致性；简单的多智能体对话往往导致混乱的交互，缺乏有效的流程控制。

核心方法：MetaGPT 将人类社会的标准化操作程序（SOPs）编码到多智能体协作框架中。它定义了产品经理、架构师、工程师等特定角色，并强制智能体生成结构化的输出（如 PRD 文档、API 接口定义）。通过共享的消息池和“流水线”式的审查机制，它将抽象需求逐步转化为具体的代码实现。

关键实验结论：在 HumanEval 和 MBPP 等代码生成基准上，MetaGPT 能够生成比传统对话式多智能体系统更连贯、可执行率更高的代码项目，证明了引入结构化流程（SOP）对于规范 LLM 协作行为至关重要。

AutoGen: Enabling Next-Gen LLM Applications
   

研究问题：构建多智能体应用通常需要繁琐的底层工程适配，开发者难以灵活定义智能体的交互模式、人类介入的时机以及工具调用的逻辑。

核心方法：AutoGen 提出了“对话式编程”（Conversation Programming）范式。它将所有实体（LLM、人类、工具、脚本）均抽象为“可对话代理”（Conversable Agents）。通过预定义的对话模式（如两两对话、群聊、层级聊天）和自动反馈回路，开发者可以通过简单的配置构建包含代码执行、人类反馈和多模型协作的复杂工作流。

关键实验结论：AutoGen 在数学解题、供应链优化和文本冒险游戏等异构任务中展示了极高的灵活性，通过简单的代理配置即可实现超越单一 GPT-4 的性能，确立了多智能体对话框架的行业标准。

4.2 长期记忆与操作系统隐喻
MemGPT: Towards LLMs as Operating Systems
   

研究问题：LLM 的固定上下文窗口限制了其在长程对话和长文档分析中的应用。单纯扩展窗口长度会导致计算复杂度呈二次方增长，且容易出现“迷失中间”（Lost-in-the-Middle）现象。

核心方法：MemGPT 创造性地借鉴了操作系统的虚拟内存管理机制，构建了分层记忆架构。它将 LLM 的上下文窗口视为“主存”（Main Memory），将外部向量数据库视为“磁盘”（Disk）。模型通过特定的函数调用（系统指令）自主管理记忆，包括将关键信息写入长期存储、从磁盘检索信息到主存、以及将不活跃的记忆从主存中换出（Eviction）。

关键实验结论：在多轮长程对话和长文档问答任务中，MemGPT 能够有效检索数千轮之前的细节，且在处理超出上下文限制的任务时仍能保持对话的连贯性和准确性，为构建终身伴侣型 AI（Lifelong Companion AI）提供了可行的架构。

5. 对话评估的新范式：LLM-as-a-Judge
随着对话系统生成能力的飞跃，传统的评估指标（如 BLEU、ROUGE）因仅关注表面文本重叠而彻底失效。2023 年以后的研究重心转向了利用 LLM 本身作为评估者，即 LLM-as-a-Judge。

G-Eval: NLG Evaluation using GPT-4 with Better Human Alignment
   

研究问题：现有的自动化指标与人类判断的相关性极低，而依赖人工评估既昂贵又不可复现。如何利用 LLM 进行符合人类标准的细粒度评估是关键挑战。

核心方法：G-Eval 提出了一种基于 GPT-4 的评估框架，引入了思维链（Chain-of-Thought, CoT）机制。它要求模型在打分前先生成详细的评估步骤和理由，并采用形式填充（Form-filling）的范式，根据连贯性、一致性、流畅度等特定标准对对话质量进行加权打分。

关键实验结论：在文本摘要和对话生成任务中，G-Eval 与人类判断的 Spearman 相关系数超过 0.5，显著优于 ROUGE 和传统的基于 BERT 的评估指标（如 BERTScore），证明了 CoT 在提升评估对齐度方面的核心作用。

Chatbot Arena: An Open Platform for Evaluating LLMs
   

研究问题：静态基准测试（Benchmarks）容易发生数据泄露（Data Contamination），且题目往往也是静态的，难以捕捉现实世界中用户提问的无限多样性和细微差别。

核心方法：Chatbot Arena 构建了一个基于众包的竞技场平台，采用成对比较（Pairwise Comparison）机制。用户输入任意提示词，系统随机展示两个匿名模型的回答，用户根据偏好投票（Model A vs Model B）。系统利用 Elo 等级分算法（Elo Rating System）基于胜率计算模型的动态排名。

关键实验结论：Arena 收集了数百万条真实用户交互数据，其 Elo 分数已成为业界公认的大模型对话能力“金标准”。它揭示了专有模型（如 GPT-4）与开源模型之间差距不断缩小的趋势，并证明了基于众包的成对比较是衡量开放域对话能力的最佳近似。

JudgeLM: Fine-tuned Large Language Models are Scalable Judges
   

研究问题：直接调用 GPT-4 进行大规模评估成本过高且存在数据隐私风险，通过闭源模型评估开源模型也存在潜在的公正性问题。

核心方法：JudgeLM 提出了微调开源模型作为专用裁判的方法。它构建了一个包含 100K 高质量判断数据的数据集，并提出了交换增强（Swap Augmentation）和参考支持等技术来解决“位置偏差”（Position Bias）和“知识偏差”问题。

关键实验结论：JudgeLM 在多个基准测试中展现了与 GPT-4 高度一致的评估能力（Agreement Rate 高），同时推理速度更快、成本大幅降低，证明了专用评估模型作为 scalable evaluation solution 的可行性。

6. 实验与评价总结：共性规律与数据洞察
综合 2022-2025 年的数百篇文献，我们可以提炼出关于对话系统性能的以下共性结论：

评估维度	关键发现与共性结论
模型规模定律 (Scaling Laws)	在对话任务中，模型参数量仍是性能的主导因素。然而，对齐红利明显：经过高质量 DPO/RLHF 微调的较小模型（如 Llama-3-8B）在对话流畅度和指令遵循上往往能超越未对齐的超大模型（如 Llama-2-70B）。
检索质量的影响	RAG 并非万能药。实验表明，低质量检索（Noisy Retrieval）对模型的伤害大于无检索。当检索内容包含误导信息时，模型极易产生幻觉。CRAG 和 Self-RAG 的实验一致证明，引入“拒答”或“过滤”机制能显著提升 F1 分数。
智能体协作效率	在多智能体系统中，结构化约束优于自由交互。MetaGPT 的实验数据表明，通过 SOP 限制智能体的通信格式，能将代码生成的通过率提升 20% 以上，而无约束的自由群聊（如早期的 AutoGen 配置）容易导致对话发散和死循环。
评估指标的偏差	LLM-as-a-Judge 存在显著的 Self-preference Bias（倾向于给自身生成的回复打高分）和 Length Bias（倾向于认为更长的回复质量更好）。SimPO 和 JudgeLM 的消融实验均表明，必须通过长度归一化和交换位置增强来校准这些偏差。
上下文利用率	尽管 MemGPT 等方法支持无限上下文，但 LLM 对上下文中间信息的利用能力（Lost-in-the-Middle）仍然较弱。将关键信息移动到 Prompt 的开头或结尾（Primacy/Recency Effect）对性能提升至关重要。
7. 趋势与挑战：2025 年展望
基于 2024 年底至 2025 年初的最新文献 ，对话系统正呈现以下显著趋势，预示着从“生成式 AI”向“认知式 AI”的跨越：   

推理增强型对话（Reasoning-enhanced Generation / System 2 Thinking）

趋势：对话生成正从单纯的“模式匹配”向“系统 2 思维”演进。2025 年的研究（如 ）开始强调在生成最终回复前，隐式或显式地生成“推理链”（Reasoning Chains）。模型不仅要回答“是什么”，还要在内部规划“为什么”和“怎么做”。   

预测：未来的对话系统将普遍内置类似 OpenAI o1 的推理模块，在处理复杂用户意图、法律咨询或医疗诊断时，先进行多步逻辑推演再输出结果，显著降低逻辑谬误。

自进化与终身学习智能体（Self-Evolving & Lifelong Learning Agents）

趋势：从静态模型向动态系统的转变是必然趋势。SAGE  和 Mem0  等工作展示了具有反思和记忆增强能力的自进化智能体。   

预测：未来的对话系统将具备“在交互中学习”（Learning from Interaction）的能力。它们将利用对话历史不断更新自身的长期记忆库和策略模块，无需重新进行全量训练即可适应用户的个性化偏好和环境变化，实现真正的“越用越聪明”。

Schema-free 的动态状态追踪与多模态融合

趋势：传统的基于固定 Schema 的对话状态追踪（DST）正被淘汰。文献  展示了利用 LLM 进行零样本、Schema-free 的状态推理能力。同时，推理能力正扩展到视频和音频领域 。   

预测：对话系统将不再受限于预定义的槽位（Slots），而是能动态理解极其复杂的业务逻辑。多模态大模型将支持视频流的实时语义理解，实现与用户在物理世界中的全双工、跨模态交互（如通过智能眼镜进行的视觉辅助对话）。

8. 结论
2022 年至 2025 年是对话系统发展史上最具颠覆性的三年。大语言模型不仅统一了任务型和开放域对话的研究范式，更通过对齐技术、检索增强、工具使用和智能体架构，突破了“统计鹦鹉”的局限，向具备认知能力、能够自主规划和长期记忆的数字助理迈进。

当前的研究表明，单纯追求更大的参数规模已遭遇边际效应递减，未来的核心在于**“系统工程”与“认知架构”**：即如何设计更精妙的记忆检索机制（如 MemGPT）、更稳健的协作流程（如 MetaGPT）以及更符合人类价值观的对齐算法（如 SimPO）。与此同时，评估体系的变革也在倒逼模型能力的真实提升。随着推理增强和自进化能力的引入，下一代对话系统将不再仅仅是被动的问答机器，而是具备主动性、反思能力和深度推理能力的智能合作伙伴。

参考文献
 Rafailov, R., et al. (2023). Direct Preference Optimization: Your Language Model is Secretly a Reward Model. arXiv preprint arXiv:2305.18290.   

 Meng, Y., et al. (2024). SimPO: Simple Preference Optimization with a Reference-Free Reward. arXiv preprint arXiv:2405.14734.   

 Bai, Y., et al. (2022). Constitutional AI: Harmlessness from AI Feedback. arXiv preprint arXiv:2212.08073.   

 Asai, A., et al. (2023). Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection. arXiv preprint arXiv:2310.11511.   

 Jiang, Z., et al. (2023). Active Retrieval Augmented Generation. arXiv preprint arXiv:2305.06983.   

 Yan, S.-Q., et al. (2024). Corrective Retrieval Augmented Generation. arXiv preprint arXiv:2401.15884.   

 Schick, T., et al. (2023). Toolformer: Language Models Can Teach Themselves to Use Tools. arXiv preprint arXiv:2302.04761.   

 Hong, S., et al. (2023). MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework. arXiv preprint arXiv:2308.00352.   

 Wu, Q., et al. (2023). AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation Framework. arXiv preprint arXiv:2308.08155.   

 Packer, C., et al. (2023). MemGPT: Towards LLMs as Operating Systems. arXiv preprint arXiv:2310.08560.   

 Liu, Y., et al. (2023). G-Eval: NLG Evaluation using GPT-4 with Better Human Alignment. arXiv preprint arXiv:2303.16634.   

 Chiang, W.-L., et al. (2024). Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference. arXiv preprint arXiv:2403.04132.   

 Introduction of Self-evolving Agents with Reflective and Memory-augmented Abilities (SAGE). (2024). arXiv preprint arXiv:2409.00872.   

 Zhu, L., et al. (2023). JudgeLM: Fine-tuned Large Language Models are Scalable Judges. arXiv preprint arXiv:2310.17631.   

 Reasoning-enhanced Personalized Text Generation. (2025). arXiv preprint arXiv:2501.04167.   


arxiv.org
A Survey of the Evolution of Language Model-Based Dialogue Systems - arXiv
在新窗口中打开

arxiv.org
[2402.18013] A Survey on Recent Advances in LLM-Based Multi-turn Dialogue Systems
在新窗口中打开

researchgate.net
A Survey on Recent Advances in LLM-Based Multi-turn Dialogue Systems - ResearchGate
在新窗口中打开

arxiv.org
Evaluating LLM-based Agents for Multi-Turn Conversations: A Survey - arXiv
在新窗口中打开

arxiv.org
[2510.23590] Lightweight Robust Direct Preference Optimization - arXiv
在新窗口中打开

aclanthology.org
Direct Preference Optimization with an Offset - ACL Anthology
在新窗口中打开

openreview.net
Direct Preference Optimization: Your Language Model is Secretly a Reward Model - OpenReview
在新窗口中打开

arxiv.org
Direct Preference Optimization: Your Language Model is Secretly a Reward Model - arXiv
在新窗口中打开

github.com
[NeurIPS 2024] SimPO: Simple Preference Optimization with a Reference-Free Reward - GitHub
在新窗口中打开

openreview.net
SimPO: Simple Preference Optimization with a Reference-Free Reward - OpenReview
在新窗口中打开

arxiv.org
SimPO: Simple Preference Optimization with a Reference-Free Reward - arXiv
在新窗口中打开

arxiv.org
[2405.14734] SimPO: Simple Preference Optimization with a Reference-Free Reward - arXiv
在新窗口中打开

anthropic.com
Constitutional AI: Harmlessness from AI Feedback - Anthropic
在新窗口中打开

www-cdn.anthropic.com
Constitutional AI: Harmlessness from AI Feedback - Anthropic
在新窗口中打开

arxiv.org
Constitutional AI: Harmlessness from AI Feedback - arXiv
在新窗口中打开

huggingface.co
Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection - Hugging Face
在新窗口中打开

par.nsf.gov
SELF-RAG: LEARNING TO RETRIEVE, GENERATE, AND CRITIQUE THROUGH SELF-REFLECTION - NSF Public Access Repository
在新窗口中打开

arxiv.org
Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection - arXiv
在新窗口中打开

openreview.net
SELF-RAG: LEARNING TO RETRIEVE, GENERATE, AND CRITIQUE THROUGH SELF-REFLECTION - OpenReview
在新窗口中打开

blog.athina.ai
Active Retrieval Augmented Generation - athina.ai
在新窗口中打开

aclanthology.org
Active Retrieval Augmented Generation - ACL Anthology
在新窗口中打开

arxiv.org
[2305.06983] Active Retrieval Augmented Generation - arXiv
在新窗口中打开

arxiv.org
Corrective Retrieval Augmented Generation - arXiv
在新窗口中打开

medium.com
Corrective Retrieval Augmented Generation (CRAG) — Paper Review | by Sulbha Jain
在新窗口中打开

arxiv.org
[2401.15884] Corrective Retrieval Augmented Generation - arXiv
在新窗口中打开

openreview.net
Corrective Retrieval Augmented Generation - OpenReview
在新窗口中打开

openreview.net
Toolformer: Language Models Can Teach Themselves to Use Tools - OpenReview
在新窗口中打开

openreview.net
Toolformer: Language Models Can Teach Themselves to Use Tools - OpenReview
在新窗口中打开

arxiv.org
[2302.04761] Toolformer: Language Models Can Teach Themselves to Use Tools - arXiv
在新窗口中打开

arxiv.org
MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework - arXiv
在新窗口中打开

openreview.net
MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework - OpenReview
在新窗口中打开

arxiv.org
MetaGPT: Meta Programming for a Multi-Agent Collaborative Framework - arXiv
在新窗口中打开

iclr.cc
ICLR 2024 MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework Oral
在新窗口中打开

openreview.net
AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversations
在新窗口中打开

microsoft.com
AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation - Microsoft
在新窗口中打开

researchgate.net
(PDF) AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation Framework - ResearchGate
在新窗口中打开

ryenwhite.com
AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversations - Ryen White
在新窗口中打开

leoniemonigatti.com
MemGPT: Towards LLMs as Operating Systems - Leonie Monigatti
在新窗口中打开

arxiv.org
MemGPT: Towards LLMs as Operating Systems - arXiv
在新窗口中打开

reddit.com
MemGPT: Towards LLMs as Operating Systems - UC Berkeley 2023 - Is able to create unbounded/infinite LLM context! : r/agi - Reddit
在新窗口中打开

arxiv.org
Mem0: Building Production-Ready AI Agents with - arXiv
在新窗口中打开

semanticscholar.org
[PDF] G-Eval: NLG Evaluation using GPT-4 with Better Human Alignment | Semantic Scholar
在新窗口中打开

openreview.net
G-Eval: NLG Evaluation using Gpt-4 with Better Human Alignment | OpenReview
在新窗口中打开

aclanthology.org
G-EVAL: NLG Evaluation using GPT-4 with Better Human Alignment - ACL Anthology
在新窗口中打开

themoonlight.io
[Literature Review] Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference - Moonlight
在新窗口中打开

arxiv.org
Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference - arXiv
在新窗口中打开

escholarship.org
Towards Robust and Scalable Evaluation for Large Language Models - UC Berkeley
在新窗口中打开

arxiv.org
JudgeLM: Fine-tuned Large Language Models are Scalable Judges - arXiv
在新窗口中打开

github.com
baaivision/JudgeLM: [ICLR 2025 Spotlight] An open-sourced LLM judge for evaluating LLM-generated answers. - GitHub
在新窗口中打开

liner.com
[Quick Review] JudgeLM: Fine-tuned Large Language Models are Scalable Judges - Liner
在新窗口中打开

arxiv.org
SAGE: Self-evolving Agents with Reflective and Memory-augmented Abilities - arXiv
在新窗口中打开

arxiv.org
Rethinking the Illusion of Thinking - arXiv
在新窗口中打开

arxiv.org
Exploring State Tracking Capabilities of Large Language Models - arXiv
在新窗口中打开

arxiv.org
Reasoning-Enhanced Self-Training for Long-Form Personalized Text Generation - arXiv
在新窗口中打开

arxiv.org
Reasoning Is All You Need for Urban Planning AI - arXiv
在新窗口中打开

arxiv.org
A-MEM: Agentic Memory for LLM Agents - arXiv
在新窗口中打开

aclanthology.org
From Schema to State: Zero-Shot Scheme-Only Dialogue State Tracking via Diverse Synthetic Dialogue and Step-by-Step Distillation - ACL Anthology
在新窗口中打开

aclanthology.org
From Schema to State: Zero-Shot Scheme-Only Dialogue State Tracking via Diverse Synthetic Dialogue and Step-by-Step Distillation - ACL Anthology
在新窗口中打开

arxiv.org
video-SALMONN-o1: Reasoning-enhanced Audio-visual Large Language Model - arXiv