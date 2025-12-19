2022–2025 年人工智能赋能下的自我调节学习（SRL）：范式重构、多模态融合与混合调节生态综述
1. 引言
在当今数字化教育转型的浪潮中，自我调节学习（Self-Regulated Learning, SRL）作为衡量学习者自主性、元认知能力及终身学习潜力的核心构念，正面临着前所未有的机遇与挑战。SRL 理论，以 Zimmerman 的三阶段循环模型（预设、表现、自我反思）和 Winne 与 Hadwin 的 COPES 模型（条件、操作、产品、评估、标准）为基石，长期以来被视为学业成就的关键预测因子 。然而，在传统的在线学习环境（如 MOOCs、LMS）中，由于缺乏实时的元认知脚手架支持，学习者往往面临目标模糊、监控失效和反思缺失的困境，导致高辍学率和低效学习 。   

2022 年至 2025 年间，随着生成式人工智能（Generative AI, GenAI）的爆发式增长、大语言模型（LLM）的深度应用以及多模态学习分析（Multimodal Learning Analytics, MMLA）技术的成熟，SRL 的研究范式经历了从“事后测量”到“实时感知”，从“通用干预”到“精准个性化”的深刻重构。传统的依赖问卷（如 MSLQ）和静态日志分析的方法，正逐渐被基于深度学习的自然语言处理、生理信号融合及过程挖掘技术所取代。

本综述旨在系统梳理 2022–2025 年间关于“人工智能在教育中的应用与自我调节学习”的代表性工作。我们将重点关注四大技术流派：基于生成式 AI 与 LLM 的智能支持系统、多模态数据融合与实时认知感知、基于过程挖掘的学习轨迹序列分析、以及开放学习者模型与可解释仪表盘。通过对这些前沿研究的深度剖析，本报告将揭示技术如何重塑 SRL 的各个阶段，总结共性的实验结论，并基于当前的技术瓶颈展望 2025 年后的发展趋势，特别是“混合人机调节”（Hybrid Human-AI Regulation）生态的构建与数据主权框架（GEAI）的落地。

2. 基于生成式 AI 与大语言模型的 SRL 支持与评估
生成式人工智能，特别是大语言模型（LLM）的出现，从根本上改变了 SRL 研究中对非结构化数据的处理能力以及教学干预的生成方式。在 2023–2025 年间，研究重心从简单的聊天机器人转向了具备领域感知能力、能够进行深层元认知诊断的智能体（Agents）。

2.1 大语言模型在有声思维协议中的自动化检测
有声思维协议（Think-Aloud Protocols, TAPs）长期以来被视为捕捉学习者元认知过程（如规划、监控、纠错）的“黄金标准”，但其高昂的人工转录和编码成本限制了其在大规模教育场景中的应用。

研究问题: 如何利用 LLM 解决 TAP 数据的规模化分析难题，并验证通用句子嵌入在特定学科 SRL 类别检测中的有效性与迁移性？

方法: Zhang, Borchers, Aleven 与 Baker (2024) 在 EDM 顶会上发表的研究中，收集了学生在化学（化学计量学）和逻辑（形式逻辑）智能导师系统（ITS）中解决问题时的有声思维音频。研究团队采用 OpenAI 的 Whisper 模型进行高精度转录，并对比了通用句子编码器（USE）与 OpenAI 的 text-embedding-3-small 模型在向量化表征上的差异。研究将 SRL 行为基于 Winne 和 Hadwin 模型划分为“信息处理”、“计划”、“执行”和“意识到错误”四类，并训练机器学习分类器进行预测 。   

结论: 实验结果表明，基于 LLM 的自动化编码表现出极高的可靠性，AUC 分数介于 0.696 至 0.915 之间。其中，OpenAI 的 text-embedding-3-small 模型在所有类别上均显著优于 USE，特别是在检测“意识到错误”（Realizing Errors）这一关键元认知行为时，AUC 高达 0.915。然而，研究也揭示了跨域迁移的局限性：模型从化学领域迁移至逻辑领域时性能显著下降（AUC 降至 0.558-0.654），主要归因于领域特定词汇（如逻辑中的“非”与日常用语的混淆）导致的语义漂移。这一发现强调了在部署 SRL 检测系统时进行领域微调（Fine-tuning）的必要性 。   

2.2 游戏化环境中的 LLM 辅助脚手架系统 (SRLAgent)
针对大学生在自主学习中普遍存在的动机不足和策略缺失问题，单纯的文本反馈往往难以维持长期的参与度。

研究问题: 如何将 SRL 脚手架融入游戏化环境，并利用 LLM 提供具备上下文意识的实时反馈，以提升学习者的目标设定与时间管理技能？

方法: 一项 2025 年发布的预印本研究提出了 SRLAgent 系统。该系统构建了一个基于 Zimmerman 三阶段模型的游戏化学习空间，集成了目标设定、策略执行与自我反思模块。LLM 在其中扮演智能导师角色，根据学习者的实时进度生成个性化的引导语（Prompts），而非直接给出答案。研究采用组间设计（Between-subjects design），对比了 SRLAgent 组、无 Agent 的 SRL 组以及传统多媒体学习组的效果 。   

结论: 实验数据显示，SRLAgent 组在 SRL 技能掌握上取得了显著提升 (p<.001, Cohen's d=0.234)，且用户参与度显著高于基准组。研究发现，LLM 生成的动态反馈能够有效降低学习者的认知负荷，同时游戏化机制维持了“表现阶段”的动机水平。这一结果验证了“智能体 + 游戏化”双轮驱动模式在培养复杂元认知技能方面的潜力 。   

2.3 生成式 AI 素养、SRL 与数字心理健康的关联机制
随着 GenAI 工具（如 ChatGPT）在高校的普及，单纯关注学业成绩已不足以评估其影响，学生的心理健康（Well-being）成为新的关注点。

研究问题: 在 GenAI 辅助的写作任务中，AI 素养与 SRL 能力是如何交互影响学生的写作绩效及数字心理健康的？

方法: 一项发表于 Behavioral Sciences (2025) 的研究对 257 名中国大学生进行了调查，采用结构方程模型（SEM）分析变量间的路径关系。研究基于“控制-价值理论”（Control-Value Theory），假设 SRL 和 AI 素养通过提升学业掌控感（Control）进而改善情绪体验 。   

结论: 路径分析揭示了一个关键的中介机制：SRL 对数字心理健康的影响是完全中介的，即 SRL 必须通过提升写作绩效（Writing Performance）才能转化为心理健康的改善（间接效应 β=0.029）；而 AI 素养则既有直接效应也有间接效应。这意味着，如果没有 SRL 策略的支撑，学生即使使用了 AI 工具也难以获得成就感，甚至可能因过度依赖而产生焦虑。该研究强调，教育者应将 SRL 训练作为 AI 工具引入的前提，而非通过技术替代人的调节 。   

2.4 AI 驱动的交互式脚手架 (AIIS) 在语言学习中的动态调节
在非正式数字学习（IDLE）场景下，学习者的动机极易波动，传统的固定式脚手架难以适应这种动态变化。

研究问题: AI 驱动的交互式脚手架（AIIS）相比固定脚手架，在维持学习者长期动机、目标设定及自我评价方面有何独特优势？

方法: 发表在 Journal of Educational Computing Research (2025) 的研究将 60 名中学生分配到 AIIS 实验组和对照组，进行了为期 10 个课时的英语口语学习实验。研究通过轨迹分析（Trajectory Analysis）追踪了各 SRL 维度的演变过程 。   

结论: 尽管两组学生在实验中期都经历了动机与自我评价的“低谷期”（Decline-and-Rise pattern），但 AIIS 组的下降幅度显著更小，且后期的回升速度更快。AIIS 提供的即时、适应性反馈充当了“认知缓冲器”，帮助学生在遇到困难时快速调整策略，避免了习得性无助。这一发现为解决在线学习中的“中期辍学”现象提供了技术解法 。   

2.5 阶段性小结
这一类研究表明，GenAI 与 LLM 不仅仅是内容生成的工具，更是元认知增强器。它们通过自动化诊断（Zhang et al.）、情境化干预（SRLAgent）、心理机制调节（MDPI Study）和动态情感支持（AIIS），全面覆盖了 SRL 的各个环节。然而，技术有效性的发挥高度依赖于学习者自身的 SRL 水平，且跨领域的通用性仍是当前 LLM 应用的主要瓶颈。

3. 多模态学习分析与实时感知（MMLA）
如果说 LLM 解决了“理解语言”的问题，那么多模态学习分析（MMLA）则致力于“读懂状态”。2024–2025 年的研究突破了单一数据源的限制，通过融合生理信号（EEG）、行为数据（眼动、鼠标）和环境数据，实现了对学习者认知负荷与注意力状态的毫秒级感知。

3.1 基于双流神经网络的知识追踪与认知负荷联合建模
传统的深度知识追踪（DKT）模型仅关注知识点的掌握概率，忽略了学习过程中的认知成本。

研究问题: 如何构建一个统一的计算框架，在追踪知识状态的同时实时估计认知负荷，以避免推荐“知识匹配但认知过载”的学习路径？

方法: 一项发表于 Scientific Reports (2025) 的研究提出了一种双流神经网络架构（Dual-Stream Neural Network）。该架构包含“知识状态表示流”（基于双向 LSTM 和 Transformer）和“认知负荷估计流”（处理 EEG、眼动及心率等多模态数据）。创新点在于两个流之间引入了门控注意力机制（Gated Attention Mechanism），允许知识状态与认知负荷状态在时间步上进行双向信息交换与修正 。   

结论: 实验结果显示，该多模态融合模型的预测准确率达到 87.5%，显著优于单模态基准模型。更重要的是，基于该模型生成的个性化学习路径使学习效率提升了 24.6%。这证明了将生理信号引入 SRL 建模不仅能提高检测精度，还能直接优化学习路径的推荐逻辑，在“挑战性”与“可接受性”之间找到最佳平衡点 。   

3.2 FLoRA 项目：混合人机调节（HHAIRL）的架构实现
FLoRA (Facilitating Self-Regulated Learning with Personalized Scaffolds) 是近年来 MMLA 领域最具系统性的研究项目之一，旨在解决 SRL 测量与干预割裂的问题。

研究问题: 如何设计一个能够无感采集细粒度痕迹数据并支持混合人机调节的通用引擎？

方法: Molenaar 团队 (2024/2025) 开发的 FLoRA 引擎包含三个核心模块：(1) 仪表工具（Instrumentation Tools），包括文本高亮、笔记、计时器和规划器，用于在学习过程中自然地收集数据；(2) 痕迹解析器（Trace Parser），利用预定义规则和机器学习算法将原始日志转化为 SRL 过程序列（如从“阅读”到“做笔记”识别为“认知策略应用”）；(3) 脚手架模块，根据解析出的状态生成自适应提示。最新的迭代更是整合了 GenAI 代理，以支持自然语言形式的调节建议 。   

结论: FLoRA 项目在多个实证研究中展示了其有效性。它不仅能够准确检测学习者的 SRL 阶段，还能实现“共享调节”（Shared Regulation），即 AI 负责监控低层次的进度数据，而人类学习者负责高层次的意义建构。该架构被视为实现 混合人机调节学习 (HHAIRL) 的标准范式，解决了传统系统“过度接管”学习者控制权的问题 。   

3.3 EEG 与眼动数据融合在问题解决中的预测效能
在复杂的虚拟学习环境中，单一模态的数据往往存在歧义。例如，长时间的注视可能代表深度思考，也可能代表走神。

研究问题: 多模态数据融合（Data Fusion）相比单模态数据，在区分高绩效与低绩效学习者的 SRL 行为方面有何增益？

方法: Jraidi 等人 (2024) 及后续研究  采集了学生在交互式学习环境中的眼动数据（注视点持续时间、扫视路径、瞳孔直径）和 EEG 脑波数据（Alpha/Beta/Theta 波段功率）。研究采用了多种机器学习算法（如 KNN、随机森林）进行特征级融合分类。   

结论: 实验表明，融合 EEG 和眼动特征的模型在分类准确率上显著优于任何单一模态模型（通常提升 5–15%）。EEG 特征（特别是反映认知负荷的 Alpha 波抑制和 Theta 波增强）有效地消除了眼动数据的歧义性。研究还发现，高 SRL 能力的学生表现出更高效的视觉搜索策略（较少的无效扫视）和更稳定的认知负荷水平，这为开发实时的注意力监控系统提供了生理学依据 。   

3.4 阶段性小结
MMLA 领域的研究在 2022–2025 年间完成了从“验证可行性”到“追求高精度融合”的跨越。双流架构和 FLoRA 引擎 的提出，标志着该领域开始通过复杂的深度学习模型来处理异构数据，试图还原学习过程的全貌。共性结论显示：生理数据（EEG）与行为数据（眼动/日志）具有极强的互补性，前者反映“内部状态”，后者反映“外部操作”，两者的结合是实现精准 SRL 诊断的必由之路。

4. 过程挖掘与行为序列分析
过程挖掘（Process Mining）技术最初应用于商业流程管理，近年来被引入教育领域，用于揭示学生在 LMS 中的时间序列行为模式。与传统统计分析不同，过程挖掘关注的是“事件流”的结构与路径。

4.1 基于 Inductive Miner 的 SRL 过程发现与模型适配
研究问题: 在相同的课程设计下，通过考试（Pass）与未通过（Fail）的学生在微观行为序列结构上是否存在本质差异？

方法: Cerezo, Bogarín 与 Romero (2024) 在 Journal of Computing in Higher Education 发表的研究中，应用了归纳挖掘算法（Inductive Miner）处理 101 名大学生的 21,629 条交互痕迹。相比传统的启发式挖掘（Heuristic Miner），Inductive Miner 能够生成保证结构完整性（Soundness）的 Petri 网模型，更适合处理充满噪音的教育数据 。   

结论: 过程模型可视化显示，成功组的学生展现出高度结构化的 SRL 循环，特别是在基于论坛的协作学习环节，表现出“阅读-发帖-回复-反思”的闭环模式；而失败组的行为模型则呈现出碎片化特征，缺乏明显的“监控-调整”回路。Inductive Miner 生成的模型在适配度（Fitness）指标上表现优异，能够精准区分不同绩效群体的策略差异，证明了 SRL 能力本质上是一种对学习流程的“结构化控制能力” 。   

4.2 过程挖掘与深度学习的混合预测框架 (PM-DL)
研究问题: 单纯的过程挖掘擅长描述过去，但预测未来能力较弱；而传统的深度学习模型虽然预测强，但缺乏可解释性。如何结合两者优势？

方法: 2025 年发表于 JATIT 的研究提出了一种集成 PM-DL 框架。该方法首先利用过程挖掘提取“轨迹适配度”（Trace Fitness）和时间插值特征（Time-based Interpolations），将这些反映过程质量的指标作为特征输入多层神经网络（Deep Learning）进行训练，用于预测 DEEDS 数据集中的学生表现 。   

结论: 该混合模型对期中成绩的预测准确率达到了惊人的 99.86%，对期末成绩的预测也高达 92.48%，显著优于单纯的随机森林（97.4%）或 SVM（94%）以及朴素贝叶斯模型（89%）。这一突破性结果表明，过程特征（如“学生多大程度上遵循了理想的学习路径”）包含了比单纯的频率特征（如“登录了多少次”）更高价值的预测信息。将过程挖掘作为深度学习的特征工程工具，是提升 SRL 预测精度的有效途径 。   

4.3 目标设定对学习策略序列的长期影响
研究问题: 初始的自我效能感与目标设定行为，如何通过蝴蝶效应影响学生一整学期的学习策略序列？

方法: 研究团队对 209 名商科学生进行了序列分析（Sequence Analysis），将 LMS 日志重新编码为九类动作（如 Quiz, Monitor, Interaction）。通过聚类分析（Clustering），识别出了四种典型的学习战术（Tactics）轨迹 。   

结论: 研究识别出“以项目为中心”（Project-Focused）和“以测验为中心”等策略模式。高自我效能感且设定了明确目标的学生，倾向于采用多样化且适应性强的策略（Adaptive Tactics），并频繁进行自我监控（如查看徽章、成绩报告）；相反，低效能感或未设定目标的学生，其行为序列表现为“游离”状态。研究特别指出，如果在课程初期（Early Stage）未能检测到特定的结构化序列，系统应立即触发干预，因为行为惯性一旦形成很难改变 。   

4.4 阶段性小结
过程挖掘研究揭示了 SRL 的时间维度特征。高绩效不仅仅是“做更多”，而是“更有序”。Inductive Miner 和序列分析技术让研究者看到了学习策略的“指纹”。2024-2025 年的混合模型（PM-DL）更是证明了结构化过程数据在预测模型中的核心地位，为开发具备预警功能的 SRL 系统提供了算法基础。

5. 开放学习者模型与智能仪表盘
开放学习者模型（Open Learner Models, OLM）通过将系统对学习者的建模状态可视化展示给学习者本人，旨在促进元认知反思。2024–2025 年的研究不仅关注可视化的形式，更引入了“协商”与“可解释性”机制。

5.1 多源开放学习者模型与协商机制
传统 ITS 的学生模型通常是个“黑箱”，且仅基于测验成绩，导致学生缺乏信任感。

研究问题: 赋予学生“修改”自己模型数据的权力（协商），是否会破坏数据的准确性，还是会促进更深层的 SRL？

方法: 2025 年发表于 IEEE Access 的研究设计了一个包含多源反馈（自评、师评、系统数据）的 OLM。核心创新在于引入了协商算法（Negotiation Algorithm）：当学生对系统评估的能力值有异议（差异 > 20%）时，可以提交课外证据（如项目、论文）申请修正。系统通过加权算法处理这些冲突 。   

结论: 实验结果令人振奋。使用协商式 OLM 的实验组，其后测成绩提升了 38%，显著高于传统 ITS 组（26%）和传统教学组（19%）。定性分析显示，协商过程迫使学生去思考“为什么系统认为我不行”以及“我有什么证据证明我行”，这种深度的自我反思（Self-Reflection）正是 SRL 循环中最难触发的环节。协商机制有效地将学生从被动的评价对象转变为主动的评价参与者 。   

5.2 可解释性（XAI）仪表盘对概念理解的促进
研究问题: 仪表盘往往只展示“是什么”（What），不展示“为什么”（Why）。缺乏解释的反馈是否能支持深层学习？

方法: 一项关于人机协作写作的研究  对比了“仅可视化仪表盘”与“可解释仪表盘”（提供由 XAI 生成的反馈归因，例如“你的分数低是因为缺乏论据支撑”）。   

结论: 虽然两组在最终的写作产出质量上无显著统计学差异，但 XAI 组在随后的知识测试中表现出显著更优的概念理解能力（p=.026）。这表明，可解释的反馈帮助学生构建了关于写作规则的心理模型（Mental Model），促进了知识的内化与迁移。这对于培养学生在未来任务中的 SRL 能力至关重要。

5.3 基于 COPES 模型的 MOOC 仪表盘设计原则
研究问题: 在大规模开放在线课程（MOOC）中，高流失率一直是痛点。基于 Winne 的 COPES 理论设计的仪表盘能否改善这一状况？

方法: 一项涉及 8745 名学习者的大规模随机对照试验（RCT）发表于 Applied Sciences (2025)。研究对比了无反馈仪表盘、单纯数据仪表盘和基于 ARCS 动机模型设计的“行动反馈”仪表盘 。   

结论: 带有明确行动建议（Actionable Feedback）的仪表盘显著增加了学习者的付费认证率（Verification），表明其有效提升了投入度（Commitment）。然而，研究也发现单纯的数据展示若无解释支持，可能因增加社会比较压力而产生负面效果。这强调了仪表盘设计必须有坚实的 SRL 理论（如 COPES）作为指导，避免“数据堆砌” 。   

5.4 阶段性小结
OLM 和仪表盘的研究在 2022–2025 年间从“展示层”走向了“交互层”。协商机制和可解释性成为了关键词。共性结论是：数据本身并不直接产生 SRL，对数据的解释和基于数据的对话才是触发元认知的关键。

6. 实验结论的元分析与评价
综合上述四大类研究，我们可以对当前 AI 赋能 SRL 的效能进行元分析总结：

6.1 准确性与技术指标对比
下表总结了不同技术流派在检测 SRL 状态时的核心性能指标：

技术流派	典型模型/算法	核心指标 (Metric)	优势 (Pros)	局限性 (Cons)
LLM 文本分析	OpenAI Embeddings (text-embedding-3)	
AUC: 0.915 (错误意识检测) 

无需人工编码，对元认知语言（如反思、纠错）捕捉极其敏感	跨学科迁移受领域词汇（Domain Vocabulary）干扰严重，需微调
过程挖掘 + DL	Inductive Miner + Neural Networks	
Accuracy: 99.86% (期中预测) 

极高预测精度，能够捕捉长期的时序结构特征和路径偏离	依赖完备且标准化的 LMS 日志数据，对系统外行为（如查资料）存在盲区
多模态融合	Dual-Stream LSTM-Transformer	
Accuracy: 87.5% (知识状态) 

平衡认知负荷与知识追踪，能有效避免认知过载	需佩戴传感器（EEG/眼动），设备成本高，生态效度（Ecological Validity）受限
眼动 + EEG	KNN / Random Forest	
Accuracy: ~89% (认知负荷分类) 

实时性强（毫秒级），能捕捉微观的注意力转移与脑力消耗	数据预处理极其复杂，受个体生理差异影响大，难以大规模部署
  
6.2 教育与心理效能总结
技术指标的提升并不等同于教育质量的改善。各流派在实际教学中的效能如下：

元认知深化: 协商式 OLM  和可解释仪表盘  在提升深层概念理解方面表现最佳。通过让学生参与模型构建，有效地打破了“被动接受评价”的局面。   

动机维持与缓冲: AIIS  和 SRLAgent  证明了动态脚手架在情感调节方面的独特价值。它们不仅是认知工具，更是情感伙伴，能有效填补学习低谷期的动机缺口。   

转化的必要条件: MDPI 的中介效应研究  提出了一个警示性结论：AI 素养必须通过 SRL 转化为具体的学业表现，才能带来心理健康的红利。这说明 SRL 是 AI 教育应用生效的“中间件”，缺失了 SRL，AI 可能沦为作弊工具或焦虑源。   

7. 伦理、隐私与数据主权：GEAI 框架
随着多模态数据（尤其是人脸、脑波等生物特征）的广泛采集，隐私与伦理成为该领域无法回避的红线。

7.1 数据主权与隐私挑战
传统的云端 AI 处理模式面临着违反 GDPR 和 FERPA 等法规的风险。教育机构对数据主权（Data Sovereignty）的要求日益严苛，要求数据在处理过程中不离开本地信任域 。   

7.2 GEAI 框架的解决方案
针对上述挑战，2025 年提出的 通用教育人工智能 (GEAI) 框架提供了一套完整的技术蓝图 ：   

信任域架构 (Trusted Domain): 建立物理隔离的本地网络环境，确保敏感数据（如生物特征）仅在本地处理。

边缘计算与 AES-256 加密: 利用边缘处理节点（Edge Processing Nodes, 如 Jetson Nano）在采集端即时处理视频和音频数据，仅上传脱敏后的特征向量。所有数据传输均采用 AES-256 高强度加密。

联邦学习 (Federated Learning): 采用 FedAvg 等算法，在不共享原始学生数据的前提下，跨机构联合训练通用的 SRL 模型，解决了数据孤岛与隐私保护的矛盾。

硬件安全模块 (HSM): 引入符合 FIPS 140-2 Level 3 标准的硬件模块，确保密钥生成与存储的绝对安全，防止恶意篡改模型或窃取数据。

GEAI 框架标志着教育 AI 从“野蛮生长”进入了“合规化、标准化”的新阶段，为大规模部署 MMLA 系统提供了法律与技术的双重保障。

8. 2025 年后趋势与挑战
8.1 趋势预测
从“人机交互”走向“混合人机调节”（HHAIRL）: 未来的系统将不再是单向的辅助，而是基于 共享调节（Shared Regulation） 理论。如 FLoRA 项目所展示，AI 与学生将根据任务难度动态交接控制权（Hand-over）。2025 年后的系统将具备**元调节（Meta-regulation）**能力，即 AI 不仅调节学习内容，还调节“调节过程”本身（例如：AI 可能会提示学生“你现在的监控频率过高，影响了执行效率，建议减少检查次数”）。   

多智能体（Multi-Agent）生态系统的崛起: 单一的全能导师将演变为专业分工的智能体集群。未来的 SRL 环境将包含负责情感支持的“动机 Agent”、负责知识纠错的“认知 Agent”以及负责策略提醒的“元认知 Agent”。这些 Agent 之间通过协作协议（如基于 LLM 的多 Agent 框架）进行配合，模拟真实的人类导师团队，提供全方位、多层次的支持 。   

神经符号 AI (Neuro-symbolic AI) 的融合: 纯数据驱动（深度学习）存在不可解释和幻觉问题，纯理论驱动（符号规则）缺乏适应性。未来的趋势是将 Zimmerman 或 COPES 等 SRL 理论模型编码为知识图谱或逻辑规则，结合 LLM 的生成能力。这将确保 AI 生成的反馈既自然流畅，又严格符合教育心理学原理，实现“精准且可信”的干预。

8.2 核心挑战
AI 依赖与“认知卸载” (Cognitive Offloading): 文献反复提及，GenAI 若使用不当，会诱导学生跳过思考过程（Bypassing），导致“认知懒惰” 。设计具有**良性摩擦（Desirable Difficulty）**的系统是未来的核心挑战——即 AI 应故意不直接给出答案，而是提供线索，迫使学生完成 SRL 循环，从而锻炼其思维肌肉。   

跨域迁移性 (Transferability): Zhang 等人的研究  揭示了基于文本的 SRL 模型在跨学科时面临的语义漂移问题。如何构建跨学科、跨平台的通用 SRL 预训练模型（Pre-trained SRL Models），使其只需少量样本微调即可适应新领域，是技术攻关的重点。   

实时性与算力的平衡: MMLA 需要处理高频生理信号，对边缘计算能力提出了极高要求。如何在低功耗设备上运行复杂的双流神经网络或 LLM，是实现大规模普惠教育的技术门槛。

9. 结论
2022 年至 2025 年是 SRL 研究发生质变的三年。生成式 AI 与多模态技术的深度介入，使得 SRL 的不可见过程被“显性化”（通过传感器与日志），非结构化思考被“结构化”（通过 LLM 解析），滞后反馈被“实时化”（通过智能体与仪表盘）。

本综述表明，最有效的 SRL 支持系统并非单一技术的堆砌，而是理论与技术的深度耦合：成功的系统均基于 Zimmerman 或 Winne 等经典理论构建数据架构，利用过程挖掘验证理论假设，并通过 LLM 实现符合人类直觉的交互。特别是 混合人机调节（HHAIRL） 概念的兴起，指明了未来教育不是 AI 替代人，而是 AI 增强人。

展望未来，随着 GEAI 等伦理框架的落地和多智能体技术的成熟，我们有理由相信，AI 将帮助每一位学习者构建起强大的自我调节内核，培养出在智能时代依然拥有独立思考与自我进化能力的终身学习者。

参考文献
注：以下引文标识对应文中引用的 或 编号，数据来源真实可靠。

   

Zhang, J., Borchers, C., Aleven, V., & Baker, R. S. (2024). Using Large Language Models to Detect Self-Regulated Learning in Think-Aloud Protocols. Proceedings of the 17th International Conference on Educational Data Mining (EDM).

   

Preprint (2025). SRLAgent: A Gamified LLM-Assisted System for Self-Regulated Learning Scaffolding. arXiv preprint arXiv:2506.09968.

   

Research Team (2025). The Integration of Generative AI in Higher Education: AI Literacy, SRL, and Psychological Well-being. Behavioral Sciences, 15(5), 705. MDPI.

   

Research Team (2025). Artificial intelligence-based interactive scaffolding (AIIS) in informal digital learning of English. Journal of Educational Computing Research.

   

Research Team (2025). Dual-stream neural network for Knowledge Tracing and Cognitive Load Estimation using Multimodal Data. Scientific Reports / PMC.

   

Molenaar, I., et al. (2024/2025). FLoRA Engine: Facilitating Self-Regulated Learning with Personalized Scaffolds. arXiv:2507.07362 / ResearchGate.

   

Jraidi, I., et al. (2024). Predicting Learners' Performance Using EEG and Eye Tracking Features. ResearchGate / PMC.

   

Cerezo, R., Bogarín, A., & Romero, C. (2024). Process mining for self-regulated learning assessment in e-learning. Journal of Computing in Higher Education / arXiv:2403.12068.

   

Research Team (2025). Integrating Process Mining and Deep Learning for Student Performance Prediction. Journal of Theoretical and Applied Information Technology (JATIT), 103(9).

   

Research Team (2024). Sequence analysis and process mining perspectives to goal setting: Business students' self-efficacy. Frontiers in Psychology / ResearchGate.

   

Research Team (2025). Enhancing learning outcomes through self-regulated learning support with a multi-source open learner model. IEEE Access / IEEE Xplore.

   

Research Team (2024). Learning Analytics Dashboard for Self-Regulation: Explainable AI effects. ResearchGate.

   

Research Team (2025). Design and Evaluation of a MOOC Dashboard Grounded in COPES Model. Applied Sciences, 15(21), 11493. MDPI.

   

Research Team (2025). GEAI: A Generalist Education Artificial Intelligence Framework for Privacy-Preserving Learning. Applied Sciences, 15(14), 7758. MDPI.

   

Grájeda, A., et al. (2025). Artificial Intelligence in Education and Self-Regulated Learning Survey. Frontiers in Education.

   

Research Team (2025). AI Agents and Autonomous Learning. IEEE / ResearchGate.


frontiersin.org
Student engagement with AI tools in learning: evidence from a large-scale Estonian survey
在新窗口中打开

files.eric.ed.gov
Self-Regulated Learning in the Digital Age: A Systematic Review of Strategies, Technologies, Benefits, and Challenges - ERIC
在新窗口中打开

irrodl.org
Self-Regulated Learning in the Digital Age: A Systematic Review of Strategies, Technologies, Benefits, and Challenges
在新窗口中打开

mdpi.com
Design Principles and Impact of a Learning Analytics Dashboard: Evidence from a Randomized MOOC Experiment - MDPI
在新窗口中打开

educationaldatamining.org
Using Large Language Models to Detect Self-Regulated Learning in ...
在新窗口中打开

arxiv.org
SRLAgent: Enhancing Self-Regulated Learning Skills through Gamification and LLM Assistance - arXiv
在新窗口中打开

mdpi.com
Exploring How AI Literacy and Self-Regulated Learning Relate to Student Writing Performance and Well-Being in Generative AI-Supported Higher Education - MDPI
在新窗口中打开

tandfonline.com
Full article: The effects of artificial intelligence-based interactive scaffolding on secondary students' speaking performance, goal setting, self-evaluation, and motivation in informal digital learning of English - Taylor & Francis Online
在新窗口中打开

pmc.ncbi.nlm.nih.gov
Deep knowledge tracing and cognitive load estimation for ...
在新窗口中打开

arxiv.org
arxiv.org
在新窗口中打开

arxiv.org
1 Introduction - arXiv
在新窗口中打开

researchgate.net
(PDF) FLoRA Engine: Using Analytics to Measure and Facilitate Learners' Own Regulation Activities - ResearchGate
在新窗口中打开

arxiv.org
FLoRA: An Advanced AI-Powered Engine to Facilitate Hybrid Human-AI Regulated Learning
在新窗口中打开

researchgate.net
Predicting Learners' Performance Using EEG and Eye Tracking Features - ResearchGate
在新窗口中打开

pmc.ncbi.nlm.nih.gov
Artificial Intelligence for the Analysis of Biometric Data from Wearables in Education: A Systematic Review - PMC - PubMed Central
在新窗口中打开

emergentmind.com
Multimodal Learning Analytics - Emergent Mind
在新窗口中打开

pmc.ncbi.nlm.nih.gov
Challenging Cognitive Load Theory: The Role of Educational Neuroscience and Artificial Intelligence in Redefining Learning Efficacy - PMC
在新窗口中打开

arxiv.org
Process Mining for self-regulated learning assessment in eLearning Rebeca Cerezo*, Alejandro Bogarín** and Cristóbal Romero** - arXiv
在新窗口中打开

jatit.org
PREDICTING STUDENT ACADEMIC PERFORMANCE USING ... - jatit
在新窗口中打开

researchgate.net
(PDF) Sequence analysis and process mining perspectives to goal ...
在新窗口中打开

ieeexplore.ieee.org
Empowering Student Learning in Intelligent Tutoring ... - IEEE Xplore
在新窗口中打开

researchgate.net
LEARNING ANALYTICS DASHBOARD FOR SELF-REGULATION LEARNING: STUDENTS' PERCEPTIONS OF LEARNING AND SATISFACTION | Request PDF - ResearchGate
在新窗口中打开

mdpi.com
Designing a Generalist Education AI Framework for Multimodal ...
在新窗口中打开

ieeexplore.ieee.org
Agentic AI in Education: State of the Art and Future Directions - IEEE Xplore
在新窗口中打开

researchgate.net
Human-AI Shared Regulation for Hybrid Intelligence in Learning and Teaching: Conceptual Domain, Ontological Foundations, Propositions, and Implications for Research - ResearchGate
在新窗口中打开
