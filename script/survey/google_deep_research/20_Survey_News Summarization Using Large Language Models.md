基于大语言模型的新闻摘要生成研究综述：2022–2025
1. 引言
在数字化信息呈指数级增长的当代社会，新闻数据的产生速度已远远超越了人类认知的处理极限。从传统的印刷媒体到全天候滚动的数字新闻流，再到社交媒体上碎片化的即时报道，海量的非结构化文本数据构成了现代信息环境的主体 。这种信息过载（Information Overload）现象不仅增加了普通读者获取关键信息的成本，也对情报分析、金融决策和舆情监控等专业领域提出了严峻挑战。在此背景下，自动文本摘要（Automatic Text Summarization, ATS）作为自然语言处理（NLP）领域的“皇冠明珠”之一，其重要性日益凸显。其核心目标是从冗长的源文档中提炼出包含关键事实、核心观点和逻辑脉络的简明文本，同时保持语义的完整性与流畅性 。   

回顾自动摘要技术的发展历程，我们可以清晰地看到一条从统计学方法向深度学习，再向大语言模型（Large Language Models, LLMs）演进的技术脉络。在2000年以前，早期的研究主要依赖于词频统计、句子位置等表面特征进行抽取式摘要（Extractive Summarization），这种方法虽然能够保留原文的准确性，但生成的摘要往往缺乏连贯性，难以整合跨段落的信息 。进入2010年代，随着序列到序列（Seq2Seq）模型、循环神经网络（RNN）以及长短期记忆网络（LSTM）的引入，生成式摘要（Abstractive Summarization）成为了可能。随后的预训练Transformer模型（如BERT, BART, T5）更是将这一领域推向了新的高度，实现了对文本语义的深层理解与重构 。然而，这些基于“预训练-微调”范式的模型在面对长文本依赖、领域迁移以及事实一致性（Hallucination）等问题时，依然表现出明显的局限性。   

2022年底，以ChatGPT为代表的大规模语言模型的爆发，标志着NLP领域进入了全新的“大模型时代”。这一范式转移（Paradigm Shift）深刻地重塑了新闻摘要的研究版图。2022年至2025年间，学术界的关注点从单纯的模型架构创新，迅速转向了对LLM涌现能力（Emergent Capabilities）的挖掘与调控。研究者们发现，经过指令微调（Instruction Tuning）的LLM展现出了惊人的零样本（Zero-shot）和少样本（Few-shot）摘要能力，甚至在无需特定领域数据训练的情况下，就能生成在流畅度和逻辑性上媲美人类专家的摘要 。与此同时，新的挑战也随之而来：如何控制生成内容的长度与风格？如何确保生成摘要的绝对忠实性？如何评估那些超越了传统参考标准（Gold Standard）的摘要质量？以及，如何将LLM从单一的文本处理工具进化为能够自主搜集、核查和撰写的智能新闻代理（News Agents）？   

本综述旨在全面、详尽地梳理2022年至2025年间关于利用大语言模型进行新闻摘要的代表性学术成果。我们将深入剖析从基础模型能力的评估、前沿的提示工程策略（如思维链、密度链）、高效的微调与对齐技术，到事实一致性的保障机制、评估指标的革命性变革，以及向个性化与智能体化演进的未来趋势。

2. 大语言模型在新闻摘要中的基础能力评估
在大语言模型介入新闻摘要任务的初期，学术界的一个核心议题是确立LLM的能力边界。与以往依赖特定数据集训练的模型不同，LLM通过海量语料的预训练获得了通用的语言理解与生成能力。然而，这种能力在新闻摘要这一对准确性与概括性要求极高的任务中究竟表现如何，2023年至2024年的一系列基准测试研究给出了深入的答案。

2.1 指令微调与模型规模的非线性关系
长期以来，深度学习领域存在一种普遍的假设，即模型的参数规模（Model Size）是决定其性能的首要因素，即“模型越大，效果越好”。然而，针对新闻摘要任务的实证研究挑战了这一简单的线性观点。Zhang等人（2024）发表在《Transactions of the Association for Computational Linguistics (TACL)》上的重磅研究《Benchmarking Large Language Models for News Summarization》揭示了指令微调（Instruction Tuning）在激活模型摘要能力中的决定性作用 。   

该研究对十种不同预训练方法、不同规模的LLM进行了系统性的对比评估。研究发现，在零样本（Zero-shot）设置下，未经指令微调的基础模型（Base Models），即便参数量巨大（如175B的GPT-3 Davinci），其摘要表现也往往不尽如人意。这些基础模型倾向于延续文本的生成（例如继续写新闻的下一段），而非执行“总结”这一特定任务。相比之下，经过指令微调的模型，哪怕参数量仅为350M（如Instruct-GPT-3 Curie），其在遵循摘要指令、提取关键信息方面的表现也显著优于未微调的超大模型 。   

这一发现具有重要的理论与实践意义：

能力的本质：新闻摘要能力的“涌现”并非单纯源于知识的积累（参数量的增加），而更多依赖于模型与人类意图的对齐（Alignment）。指令微调通过向模型展示多样化的任务指令，教会了模型如何利用其预训练知识来服务于特定目标。

资源效率：在资源受限的实际应用场景中（如本地部署的新闻分析系统），部署一个经过高质量指令微调的中小参数模型，可能比调用昂贵的超大模型API更具成本效益，且效果相当甚至更好 。   

2.2 “参考摘要”陷阱与人类评估的重新校准
LLM的出现不仅提升了生成效果，更暴露了现有评估体系的深层缺陷。在传统的自动摘要研究中，CNN/DailyMail和XSum等数据集被视为“黄金标准”，其提供的参考摘要（Reference Summaries）是训练和评估的基石。然而，当研究者将LLM生成的摘要与这些参考摘要并列进行人类评估时，出现了一个令人尴尬的现象：LLM生成的摘要在质量上往往超越了数据集原本的“标准答案” 。   

具体而言，XSum数据集的参考摘要通常是新闻的虽然简短但往往过度抽象的导语，有时甚至包含原文档中未提及的外部信息，导致严重的“幻觉”问题。在Likert 1-5分的连贯性（Coherence）评分中，XSum的原始参考摘要平均得分仅为2.5分左右，被人类评估者认为质量低下。相比之下，Instruct Davinci等LLM生成的摘要平均得分高达4.5分 。这一巨大的质量鸿沟导致了基于参考文本的自动评估指标（如ROUGE）失效。在XSum数据集上，ROUGE分数与人类判断之间甚至呈现出负相关——即ROUGE分越高的摘要，人类评估者反而认为其质量越差，因为这意味着模型模仿了低质量的参考摘要 。   

为了解决这一问题，研究团队不得不聘请专业的自由撰稿人（Freelance Writers）重新编写高质量的参考摘要。实验表明，当使用这些高质量的人工摘要作为基准时，LLM的评估结果才回归理性，且此时自动指标与人类判断的相关性显著提升。这一过程揭示了当前NLP研究中“数据瓶颈”的新形态：模型的生成能力已经超越了用于评估它们的静态数据集的质量。

2.3 上下文窗口与长文档摘要的挑战
虽然LLM在标准长度的新闻摘要中表现优异，但在处理长篇深度报道、调查性新闻或多文档综述时，仍面临上下文窗口（Context Window）的物理限制。尽管GPT-4、Claude 3等模型已宣称支持128k甚至更长的上下文，但在实际应用中，模型仍表现出“迷失中间”（Lost-in-the-Middle）的现象 。   

的研究指出，当输入文本过长时，LLM倾向于过度关注文档的开头和结尾部分，而忽略中间段落的关键信息。这种**位置偏差（Positional Bias）**在新闻摘要中尤为致命，因为许多深度报道的核心事实往往隐藏在文章的中段。虽然ALiBi（Attention with Linear Biases）、位置插值（Position Interpolation）等技术试图从架构层面扩展窗口 ，但如何在超长上下文中保持注意力的均匀分布，依然是2024-2025年的研究热点。   

下表总结了LLM在新闻摘要基础能力评估中的关键对比发现：

评估维度	传统认知 / 旧基准	LLM时代的新发现 (2022-2025)
驱动因素	模型参数越大越好 (Scaling Law)	
指令微调是零样本摘要能力的关键；小参数微调模型可匹敌大参数基础模型 

参考数据	CNN/DM, XSum为黄金标准	
现有参考摘要质量低于LLM生成水平；导致ROUGE指标失效甚至负相关 

人类偏好	偏好人工编写的参考摘要	
在盲测中，人类评估者往往更偏好LLM生成的摘要，认为其更连贯、信息更丰富 

长文处理	截断处理或层级RNN	
支持超长上下文，但存在位置偏差（关注首尾，忽略中间） 

  
3. 高级提示工程：从“思维链”到“密度链”
如果说预训练赋予了LLM知识的海洋，那么提示工程（Prompt Engineering）就是引导这股水流精准灌溉新闻摘要任务的渠系。2023年至2025年间，研究者们不再满足于简单的“请总结这篇文章”这类指令，而是开发了一系列复杂的、结构化的提示策略，旨在提升摘要的信息密度、逻辑深度和可控性。

3.1 密度链（Chain of Density, CoD）：平衡信息量与可读性
在新闻摘要中，存在一个永恒的权衡（Trade-off）：信息量（Informativeness）与可读性（Readability）。过于简略的摘要丢失细节，而过于详尽的摘要则变得冗长难读。Adams等人（2023）提出的“密度链”（Chain of Density, CoD）策略，是解决这一矛盾的里程碑式工作 。   

3.1.1 核心机制
CoD不仅仅是一个提示，而是一个迭代优化的过程。其核心思想是在保持摘要长度固定（Fixed Length）的前提下，逐步增加实体（Entities）的密度。具体流程如下：

初始生成：模型首先生成一个“实体稀疏”（Entity-Sparse）的初稿。这个初稿通常比较啰嗦，包含大量填充词，给后续压缩留有余地。

缺失实体识别：在每一轮迭代中，模型被要求回顾源文档，识别出当前摘要中尚未包含、但对理解新闻至关重要的“缺失实体”（Missing Entities）。

融合与重写：模型必须将这些新识别的实体融入到摘要中，同时严格保持与上一轮相同的字数。这一约束迫使模型进行深度的抽象（Abstraction）和句法融合（Fusion），例如将“美国总统拜登在周三宣布”压缩为“拜登周三宣布”，腾出空间给新信息。

循环迭代：上述过程重复5次，生成从Step 1到Step 5密度逐级递增的摘要序列。

3.1.2 实验结果与洞察
实验数据显示，通过CoD策略，摘要中的实体密度（Entities/Token）从初始的0.089显著提升至0.167，超过了人类参考摘要的平均密度（0.151）。更重要的是，人类评估揭示了一个“倒U型”的偏好曲线：   

Step 1（稀疏）：信息太少，被评为不佳。

Step 5（极密）：虽然包含最多信息，但句子结构过于紧凑，甚至出现语法生硬，导致可读性下降。

Step 2 & 3（平衡点）：人类评估者最倾向于中间步骤的摘要。这表明，虽然LLM具备极强的压缩能力，但人类对新闻摘要的阅读体验有一个“认知负荷”的上限。CoD方法不仅提供了一种生成高质量摘要的手段，更提供了一个调节“信息密度”的旋钮，适应不同读者的需求（如专家需要高密度，大众需要低密度）。

3.2 摘要思维链（SumCoT）：基于要素的结构化推理
受思维链（Chain-of-Thought, CoT）在数学推理任务中成功的启发，Wang等人（2023）提出了专门面向摘要任务的SumCoT（Summary Chain-of-Thought）。   

传统的摘要生成往往是端到端（End-to-End）的黑盒过程，容易产生遗漏或幻觉。SumCoT引入了新闻学中的经典Lasswell通信模型（即5W1H：Who, What, When, Where, Why, How），将摘要过程分解为两个显式的推理步骤：

要素抽取（Element Extraction）：模型首先被引导回答一系列关于新闻核心要素的问题。例如，“这就事情的主角是谁？”、“发生在什么时间？”、“起因是什么？”。这一步迫使模型先理解并定位关键事实。

基于要素的生成（Element-aware Generation）：在提取了这些结构化要素后，模型再基于这些要素生成连贯的摘要。

实验表明，SumCoT在CNN/DailyMail和XSum数据集上的ROUGE-L得分分别比基线模型提升了4.33和4.77点 。更关键的是，这种分步策略显著减少了事实性错误，因为摘要是建立在第一步提取的确凿证据之上的。这证明了在新闻摘要中，引导模型模拟人类记者的“采编”思维过程是行之有效的。   

3.3 后视链（Chain of Hindsight, CoH）：从反馈中学习
在对齐（Alignment）领域，Liu等人提出了后视链（Chain of Hindsight, CoH），这是一种利用人类反馈进行提示优化的新范式 。   

传统的RLHF（基于人类反馈的强化学习）通过训练奖励模型来优化生成策略，过程复杂且不稳定。CoH则另辟蹊径，它将人类的反馈（包括正面和负面）转化为自然语言形式的历史序列，作为上下文输入给模型。

机制：在训练或推理时，模型会看到类似这样的序列：“{负面摘要} -> {人类反馈：这个摘要遗漏了关键数据} -> {修正后的正面摘要}”。

效果：通过这种对比学习，模型不仅学会了“什么是好的摘要”，更深刻理解了“什么是不好的摘要”以及“如何避免特定的错误”。

优势：实验显示，CoH在新闻摘要任务上的表现显著优于标准的监督微调（SFT）和RLHF，特别是在对齐人类的主观偏好方面。它让模型具备了某种“自我反思”和从历史错误中汲取教训的能力。

3.4 零样本长度控制策略
除了上述复杂的推理链，针对新闻摘要中常见的长度限制要求（如“生成100词以内的摘要”），2025年的研究也提出了多种零样本策略。Retkowski等人（2025）在论文《Zero-Shot Strategies for Length-Controllable Summarization》中指出，即使是强大的模型如Llama 3，在面对严格的长度约束时也常失效 。   

为此，研究者提出了一套组合策略：

长度近似（Length Approximation）：让模型先生成一个大概长度的草稿。

目标调整（Target Adjustment）：根据草稿的实际长度偏差，动态调整下一轮生成的指令目标。

自动修订（Automated Revisions）：引入一个专门的“编辑”步骤，对超长或过短的摘要进行重写。 这些策略在不改变模型权重的情况下，大幅提升了摘要的长度合规率，对于新闻简报、推特发布等对字数敏感的应用场景至关重要。

4. 事实一致性与幻觉消减机制
新闻摘要的生命线在于“真实性”（Faithfulness）。然而，大语言模型本质上是概率生成的，这导致其在生成过程中容易产生“幻觉”（Hallucination），即生成源文档中不存在或与源文档事实相悖的内容。2023年至2025年，针对新闻摘要中幻觉检测与消减的研究呈现井喷态势，成为该领域最核心的挑战之一。

4.1 幻觉的类型学与成因分析
在新闻摘要场景下，LLM的幻觉主要表现为以下几种形式 ：   

实体错误（Entity Error）：张冠李戴，例如将事件的主角从“特朗普”错误地关联为“拜登”。

数值篡改（Numerical Error）：错误地引用新闻中的统计数据、金额或日期。

因果倒置（Causal Error）：强行在两个无关事件之间建立因果联系。

外在幻觉（Extrinsic Hallucination）：模型引入了其预训练知识中存在但源文档中未提及的信息。虽然这些信息可能在客观上是正确的，但在摘要任务中属于未授权的添加，破坏了摘要的忠实度。

的研究进一步指出，**位置偏差（Positional Bias）**是长文档摘要产生幻觉的重要诱因。模型往往对文档开头和结尾的信息记忆清晰，而对中间部分的信息记忆模糊，导致在整合中间段落的事实时容易发生拼接错误（Stitching Error）。   

4.2 SliSum：滑动生成与自洽性策略
针对长新闻摘要中的事实一致性问题，Li等人（2024）在LREC-COLING会议上提出了SliSum（Sliding Generation and Self-Consistency）框架 。   

SliSum的设计灵感来源于人类阅读长文的习惯——分段阅读并整合。其具体流程包含三个关键阶段：

重叠滑动窗口（Overlapping Sliding Windows）：将长篇新闻切分为多个有重叠部分的窗口。重叠的设计至关重要，它保证了跨窗口的上下文信息不会因为切分而丢失。

局部摘要生成（Local Summary Generation）：利用LLM对每个窗口生成局部摘要。由于每个窗口长度适中，模型能够更集中注意力，显著减少了因上下文过长导致的遗忘和幻觉。

聚类与投票聚合（Clustering and Majority Voting）：这是SliSum的核心创新。对于多个局部摘要中提取出的信息点，算法会进行语义聚类。只有当某个信息点在多个局部摘要中反复出现（即通过了“多数投票”），才会被保留在最终的全局摘要中。这种**自洽性（Self-Consistency）**机制有效地过滤掉了偶然产生的幻觉噪声。

实验结果显示，SliSum在不进行额外模型训练的情况下，显著提升了LLaMA-2、Claude-2和GPT-3.5在长文档摘要任务上的真实性得分，同时保持了摘要的流畅度和信息覆盖度 。   

4.3 细粒度检测与原子内容单元
除了生成策略的改进，幻觉的自动检测也是研究重点。介绍了一种基于**原子内容单元（Atomic Content Units, ACUs）**的细粒度检测方法。   

该方法将摘要分解为独立的、不可再分的事实单元（如“苹果公司发布了iPhone 15”分解为“苹果公司-发布-iPhone 15”）。然后，利用AMR（抽象语义表示）图将这些单元与源文档进行结构化比对。AMR图能够清晰地表示句子内部的逻辑关系（如施事者、受事者、时间状语），从而帮助检测那些仅靠关键词匹配无法发现的深层逻辑错误（如动作发出者搞反了）。这种方法特别适用于检测新闻摘要中微妙的语义篡改。

4.4 影响函数与偏差溯源
为了从根本上理解幻觉的来源，Thota等人（2024）在EMNLP上发表的研究利用**影响函数（Influence Functions）**来追踪训练数据对模型输出的影响 。研究发现，模型产生的特定类型的幻觉往往可以追溯到预训练语料中的特定模式（如某些常见的新闻套话）。这一发现为通过数据清洗来减少幻觉提供了理论依据：通过识别并移除那些容易诱导模型产生偏见的训练样本，可以从源头上提升模型的真实性。   

5. 微调技术与领域适配
虽然零样本提示展现了LLM的通用能力，但在金融、医疗等对专业术语和格式有严格要求的新闻领域，微调（Fine-tuning）仍然是不可或缺的手段。2024年至2025年，微调技术正朝着轻量化、参数高效和数据质量优先的方向发展。

5.1 参数高效微调（PEFT）的崛起
全量微调（Full Fine-tuning）动辄数百亿参数的大模型，其计算成本和显存需求是大多数研究机构和企业难以承受的 。因此，**LoRA（Low-Rank Adaptation）**及其变体（如QLoRA）成为了新闻摘要微调的标准配置。   

Rallapalli等人（2025）的研究展示了在资源受限环境下（如仅有一两张A100 GPU），如何通过PEFT技术对Llama-2和Llama-3系列模型进行微调，以适应政府报告和情报分析的需求 。研究发现：   

数据效率：仅需少量（几百到几千条）高质量的领域标注数据，配合LoRA微调，就能使基础模型在特定格式（如情报简报格式）的遵循度上大幅超越通用的GPT-4。

隐私保护：对于涉及敏感信息的政府或企业新闻数据，本地部署的微调小模型（7B或13B参数）提供了比云端大模型更优的隐私安全保障，且在特定任务上的表现毫不逊色。

5.2 领域适配中的提示设计
在微调过程中，提示词（Prompt）的设计依然扮演着微妙但关键的角色。在金融新闻摘要的研究中揭示了一个有趣的现象：在对指令微调模型进行进一步的领域微调时，提示词的“引导短语”（Lead-in phrase）（即紧跟在指令后，提示模型开始生成的词，如“Here is the summary:”）对最终效果的影响，甚至超过了指令本身的复杂度。   

研究者发现，使用特定的引导短语可以激活模型在预训练阶段习得的特定文风。在金融领域，使用类似“Market Report Summary:”这样的引导语，能够显著提升模型生成摘要的专业性，使其更符合财经新闻的行文规范。这表明微调并不是完全覆盖预训练知识，而是更好地“索引”和“激活”了相关领域的潜在能力。

5.3 跨语言与低资源语言的突破
探讨了LLM在匈牙利语等黏着语系新闻摘要中的应用。通过在多语言新闻语料上微调LLaMA-2，模型展现出了强大的跨语言迁移能力（Cross-lingual Transfer）。即便是预训练语料中占比极低的语言，只要在微调阶段提供少量高质量的“英语-目标语言”对照样本，模型就能学会将英语新闻摘要为目标语言，或者直接对目标语言新闻进行摘要。这为打破新闻传播的语言壁垒提供了强有力的工具。   

6. 评估方法的变革：从ROUGE到LLM-as-a-Judge
评估是自动摘要研究的指挥棒。2022年以前，ROUGE（Recall-Oriented Understudy for Gisting Evaluation）是绝对的统治者。然而，随着LLM生成能力的飞跃，ROUGE等基于n-gram重叠的统计指标逐渐显露出其滞后性，基于大模型的评估方法（LLM-as-a-Judge）正迅速取而代之。

6.1 ROUGE指标的失效与反思
ROUGE的核心逻辑是计算生成摘要与参考摘要之间的词汇重叠率。然而，TACL 2024的研究  指出，这种逻辑在LLM时代已不再适用：   

词汇多样性：LLM生成的摘要往往使用与参考摘要完全不同的词汇来表达相同的含义（同义词替换、句式重组），导致ROUGE得分偏低，尽管其语义完全正确。

负相关现象：如前所述，在XSum等参考摘要质量欠佳的数据集上，高质量的LLM摘要反而会因为“不像”低质量的参考摘要而获得低分。的研究显示，在某些情况下，ROUGE得分的提升与人类对摘要质量的感知呈现出统计学上的不相关甚至负相关。   

6.2 G-Eval框架：利用LLM进行无参考评估
为了解决这一危机，Liu等人（2023）提出了G-Eval框架，这是一种利用GPT-4等强模型作为评审员（Judge）的评估方法 。   

G-Eval不仅仅是简单地问模型“这个摘要好不好”，而是引入了结构化的评估流程：

思维链引导（CoT）：在评分前，强制模型生成评估步骤的思维链。例如，“首先检查摘要是否覆盖了原文的主语；其次检查时间线是否准确；最后评估语言是否流畅”。

多维度评分表（Rubrics）：定义清晰的评分标准（如连贯性、一致性、流畅性、相关性），要求模型分项打分。

加权汇总：根据各项指标的重要性进行加权，得出总分。

实验结果表明，G-Eval与人类判断的Spearman相关系数达到了0.514，这一数值远超ROUGE、METEOR和BERTScore等所有传统指标 。G-Eval的成功标志着摘要评估进入了“语义评估”的新阶段，也使得在没有参考摘要的开放场景下评估模型表现成为可能。   

6.3 评估中的偏见挑战
尽管LLM-as-a-Judge表现优异，但也引入了新的偏见：

自我偏好（Self-preference）：LLM倾向于给由同一模型（或同一家族模型）生成的摘要打高分。例如，GPT-4作为裁判时，往往会给GPT-4生成的摘要更高的评价 。   

长度偏见（Length Bias）：模型往往潜意识地认为“更长=信息更丰富”，从而给予长摘要更高的分数，这与摘要任务追求“简练”的初衷有时是相悖的。

因此，2025年的评估研究正致力于开发更客观、去偏见的LLM评估协议，例如引入成对比较（Pairwise Comparison）和交换顺序测试（Position-Swap Testing）来校准模型的打分。

7. 前沿趋势：从通用摘要到个性化智能体
进入2025年，新闻摘要的研究边界正在被打破。研究者不再满足于将摘要视为单一的文本压缩任务，而是将其视为智能体（Agent）与用户交互的动态过程。个性化和自主化成为了新的关键词。

7.1 个性化摘要（Personalized Summarization）：PersonalSum
传统的新闻摘要是“千人一面”，即对同一篇新闻，所有用户看到的摘要都是一样的。然而，不同用户的兴趣点截然不同。Zhang等人提出的PersonalSum数据集和研究框架，开启了“千人千面”的新闻摘要研究 。   

PersonalSum通过引入用户的主观信号来引导摘要生成：

实体/话题兴趣（Entities/Topics）：用户可能只关心新闻中涉及“科技”或“苹果公司”的部分。

情节偏好（Plot）：用户可能更关注事件的起因和结果，而忽略中间的细节过程。

结构偏好（Structure）：用户可能偏好列表式的摘要，而非段落式。

初步实验表明，虽然现有的LLM能够一定程度上响应这些个性化指令，但在极短的篇幅内平衡“通用的新闻重要性”与“用户的个人兴趣点”仍是一个巨大的挑战。这需要模型具备更强的用户建模能力和多目标优化能力 。   

7.2 智能体新闻系统（Agent-based News Systems）：NewsAgent
NewsAgent框架代表了新闻摘要向**多智能体协作（Multi-Agent Collaboration）**演进的趋势 。   

在NewsAgent系统中，新闻生产不再是由单个模型完成，而是由一组角色分工明确的智能体共同协作：

搜集者（Retriever）：负责从互联网、社交媒体等多渠道搜集原始素材。

分析者（Analyzer）：负责阅读长文，提取关键事实，并构建事件的时间线。

撰写者（Writer）：基于分析者的报告，撰写符合特定风格（如严肃、幽默、简报）的新闻摘要。

核查者（Fact-checker）：专门负责将生成的摘要与原始证据进行比对，纠正幻觉。

编辑（Editor）：统筹全局，确保最终输出的质量。

这种架构的优势在于：

动态性：智能体可以持续监控新闻进展，实时更新摘要，形成“进化中”的报道。

多模态能力：智能体不仅能处理文本，还能调用工具处理新闻中的图片和视频数据，生成图文并茂的综合摘要 。   

自我修正：通过核查者与撰写者的多轮对话，系统能够在发布前自动修正错误，大大提高了新闻的准确性。

还提出了AgentDiet技术，通过优化智能体的交互轨迹，去除冗余的中间推理步骤，使得这种多智能体系统的推理成本降低了20%-35%，使其在实际工业应用中更具可行性。   

8. 总结与展望
2022年至2025年，新闻摘要领域经历了一场深刻的革命。从早期的RNN/Transformer模型到如今的大语言模型，我们见证了摘要技术从“机械式的句子抽取”向“类人的语义重构”的跨越。

能力重塑：指令微调（Instruction Tuning）被确立为激活模型摘要能力的关键，打破了唯参数论的迷思。

方法升级：提示工程已演化为精密设计的推理算法。Chain of Density展示了如何在固定长度内极限压缩信息，SumCoT通过模拟记者的采编思维提升了逻辑性，SliSum通过分治与自洽性校验解决了长文幻觉问题。

评估重构：ROUGE的衰落和G-Eval的兴起，标志着我们进入了语义级评估的新时代，尽管评估的公平性仍需警惕。

未来形态：新闻摘要正在超越单纯的文本处理，向个性化（PersonalSum）和智能体化（NewsAgent）迈进。未来的新闻摘要系统将不再是一个静态的工具，而是一个能够理解用户偏好、自主搜集核查、全天候在线的私人新闻助理。

随着长上下文技术的成熟和多模态智能体的落地，我们有理由相信，在不久的将来，每个人都能拥有一份专属于自己的、实时更新的、高度可信的“日报”，而这正是大语言模型赋予新闻传播行业的全新可能。


arxiv.org
A Comprehensive Survey on Automatic Text Summarization with Exploration of LLM-Based Methods - arXiv
在新窗口中打开

arxiv.org
An Evaluation of Large Language Models on Text Summarization Tasks Using Prompt Engineering Techniques. - arXiv
在新窗口中打开

pmc.ncbi.nlm.nih.gov
Ontology-based prompt tuning for news article summarization - PMC - PubMed Central
在新窗口中打开

aclanthology.org
Benchmarking Large Language Models for News ... - ACL Anthology
在新窗口中打开

transacl.org
Benchmarking Large Language Models for News Summarization
在新窗口中打开

direct.mit.edu
Benchmarking Large Language Models for News Summarization | Transactions of the Association for Computational Linguistics - MIT Press Direct
在新窗口中打开

aclanthology.org
Improving Faithfulness of Large Language Models in Summarization ...
在新窗口中打开

arxiv.org
On Context Utilization in Summarization with Large Language Models - arXiv
在新窗口中打开

arxiv.org
Evaluating the Effectiveness of Large Language Models in Automated News Article Summarization - arXiv
在新窗口中打开

aclanthology.org
From Sparse to Dense: GPT-4 Summarization with Chain of Density Prompting
在新窗口中打开

pmc.ncbi.nlm.nih.gov
From Sparse to Dense: GPT-4 Summarization with Chain of Density Prompting - PMC - NIH
在新窗口中打开

arxiv.org
arXiv:2309.04269v1 [cs.CL] 8 Sep 2023 - Research University
在新窗口中打开

github.com
Alsace08/SumCoT: [ACL 2023] Code and Data Repo for Paper "Element-aware Summary and Summary Chain-of-Thought (SumCoT)" - GitHub
在新窗口中打开

arxiv.org
Element-aware Summarization with Large Language Models: Expert-aligned Evaluation and Chain-of-Thought Method - arXiv
在新窗口中打开

aclanthology.org
Element-aware Summarization with Large ... - ACL Anthology
在新窗口中打开

semanticscholar.org
[PDF] Chain of Hindsight Aligns Language Models with Feedback - Semantic Scholar
在新窗口中打开

openreview.net
Chain of Hindsight aligns Language Models with Feedback - OpenReview
在新窗口中打开

aclanthology.org
Zero-Shot Strategies for Length-Controllable Summarization - ACL Anthology
在新窗口中打开

arxiv.org
Zero-Shot Strategies for Length-Controllable Summarization - arXiv
在新窗口中打开

openreview.net
Faithfulness Hallucination Detection in Healthcare AI - OpenReview
在新窗口中打开

aclanthology.org
From Single to Multi: How LLMs Hallucinate in Multi-Document Summarization - ACL Anthology
在新窗口中打开

arxiv.org
Improving Faithfulness of Large Language Models in Summarization via Sliding Generation and Self-Consistency - arXiv
在新窗口中打开

mdpi.com
Mind the Link: Discourse Link-Aware Hallucination Detection in Summarization - MDPI
在新窗口中打开

2024.emnlp.org
Findings - EMNLP 2024
在新窗口中打开

arxiv.org
Fine-Tuning LLMs for Report Summarization: Analysis on Supervised and Unsupervised Data - arXiv
在新窗口中打开

aclanthology.org
Revelata at the FinLLM Challenge Task: Improving Financial Text Summarization by Restricted Prompt Engineering and Fine-tuning - ACL Anthology
在新窗口中打开

arxiv.org
Crafting Tomorrow's Headlines: Neural News Generation and Detection in English, Turkish, Hungarian, and Persian - arXiv
在新窗口中打开

arxiv.org
[2303.16634] G-Eval: NLG Evaluation using GPT-4 with Better Human Alignment - arXiv
在新窗口中打开

confident-ai.com
G-Eval Simply Explained: LLM-as-a-Judge for LLM Evaluation - Confident AI
在新窗口中打开

aclanthology.org
G-EVAL: NLG Evaluation using GPT-4 with Better Human Alignment - ACL Anthology
在新窗口中打开

arxiv.org
PersonalSum: A User-Subjective Guided Personalized Summarization Dataset for Large Language Models - arXiv
在新窗口中打开

openreview.net
PersonalSum: A User-Subjective Guided Personalized Summarization Dataset for Large Language Models | OpenReview
在新窗口中打开

papers.nips.cc
PersonalSum: A User-Subjective Guided Personalized Summarization Dataset for Large Language Models - NIPS papers
在新窗口中打开

arxiv.org
NEWSAGENT: Benchmarking Multimodal Agents as Journalists with Real-World Newswriting Tasks - arXiv
在新窗口中打开

arxiv.org
P1GPT: A Multi-Agent LLM Workflow Module for Multi-Modal Financial Information Analysis
在新窗口中打开

arxiv.org
Improving the Efficiency of LLM Agent Systems through Trajectory Reduction - arXiv