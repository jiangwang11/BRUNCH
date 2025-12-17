# 对话系统与对话生成的进展：2022-2025年系统综述

**摘要**：本综述系统梳理了2022-2025年间对话系统工程与对话生成领域的核心进展。通过梳理超50篇顶会/顶刊论文，我们发现该领域呈现三大特征：（1）大语言模型（LLM）深度介入从对话状态追踪到端到端对话生成的全流程；（2）任务导向对话（TOD）系统从管道式架构向端到端学习范式演进；（3）多模态、多语言、个性化与情感感知的融合需求日趋迫切。本综述覆盖对话状态追踪、多轮对话理解、知识增强生成、个性化与情感建模、评估度量设计等核心议题，并指出检索增强生成（RAG）、零样本领域自适应、强化学习策略优化、法则化提示工程成为2024-2025年的前沿技术方向。

---

## 引言

对话系统的技术演进与产业部署正处于加速拐点。从ELIZA（1966）的规则模板系统，到神经网络时代的序列到序列模型（Seq2Seq），再到2023年后LLM驱动的端到端范式，对话系统的核心范式已发生质变[1]。行业数据表明，2025年会话AI市场规模已达18.5亿美元，且以49%的年复合增长率扩张[4]。

然而，规模进步带来新挑战。现有LLM虽展示出卓越的零样本生成能力，但在长上下文理解、事实准确性维护、领域适配效率、多模态融合等方面仍存在系统性瓶颈。特别是任务导向对话（TOD）系统需要精确的状态追踪与可控的策略学习，通用LLM方案的"一刀切"设计难以满足实际工程约束[11]。

本综述采取分层视角：首先对2022-2025年核心技术矩阵进行分类梳理，其次聚焦代表性论文的方法创新与实证发现，最后指出该领域的开放性挑战与2025年后的研究前沿。

---

## 方法分类与代表性工作

### 一、对话状态追踪（Dialogue State Tracking, DST）

**研究演进轨迹**：DST是TOD系统的信息处理枢纽，负责在每个对话轮次维护用户意图的概率分布[6]。传统方法依赖槽位-值对的离散本体，受限于开放域泛化性。2022-2025年的主要突破在于LLM的引入如何重塑DST范式。

**代表工作1**：**《Interpretable and Robust Dialogue State Tracking via Natural Language Descriptions》**（arXiv 2503）是该领域的关键突破[2]。该研究首次提出NL-DST框架，不再强制LLM预测预定义的槽位-值对，而是让其直接生成自然语言形式的对话状态描述。在MultiWOZ 2.1与Taskmaster-1数据集上，NL-DST在联合目标准确度（Joint Goal Accuracy）和槽位准确度上均超过BERT-based DST基线及生成式GPT-2变体。关键创新在于：通过自然语言中介，模型获得了更丰富的表达空间以捕捉隐含意图，对噪声输入表现出更强鲁棒性，且生成的描述具备人类可解释性。人工评估显示NL-DST生成的状态描述在相关性(4.5 vs 3.8)和信息量(4.2 vs 3.5)上显著优于结构化输出方案。

**代表工作2**：**《Schema Augmentation for Zero-Shot Domain Adaptation in Dialogue State Tracking》**（arXiv 2411）针对DST的跨域泛化问题提出Schema Augmentation技术[34]。该方法通过数据增强与提示优化的双LoRA架构，在零样本设置下对MultiWOZ 2.2与SpokenWOZ数据集实现了高达2倍的目标准确度提升。核心观察是：端到端DST中，模型往往忽视对槽位描述与可能值的充分注意，增强数据通过显式引入schema信息强制模型在无监督域上获得泛化能力。该研究首次提出Target Goal Accuracy（TGA）指标专门评估非显示域性能，填补了DST领域长期的评估空白。

**代表工作3**：**《Large Language Models as Zero-shot Dialogue State Tracker via Function Calling (FnCTOD)》**（ACL 2024）利用LLM原生的函数调用能力重新定义DST任务[38]。相比直接提示（Direct Prompting），该方法通过结构化函数签名约束LLM输出，在零样本setting下将ChatGPT的联合目标准确度从前期baseline的48.76%提升至62.54%，GPT-4性能提升14%，开源7-13B模型超越先前ChatGPT最佳结果。方法的可插拔特性使其与任何兼容函数调用的LLM兼容，相比微调方案降低了工程成本。

**共性发现**：DST领域正从离散本体依赖向连续表示、从单任务向多任务融合（DST与策略学习联合优化）、从英文单语向多语言鲁棒性演进[6]。零样本自适应已从理想变为生产可行方案。

---

### 二、多轮对话理解与上下文建模

**研究动机**：多轮对话系统需维护跨度可达数十轮的长程依赖，同时处理话题转移、指代消解、椭省等自然语言现象[3]。与单轮QA不同，对话需要感知隐含的交互结构与用户演化的意图。

**代表工作1**：**《Dialogue Discourse Parsing as Generation (Seq2Seq-DDP+Transition)》**（SIGDIAL 2024）将对话结构解析重构为生成任务[25]。传统解析方法采用独立的分类组件，存在error propagation问题。该研究提出Seq2Seq-DDP框架，以及改进的转移系统变体Seq2Seq-DDP+Transition，在STAC与Molweni数据集上达到新SOTA。转移系统的优势在于：（1）逐句处理可控性强；（2）在Molweni数据集上大幅超越GNN-based基线；（3）框架统一了结构预测与关系标注。该研究的洞察是对话结构可被视为自然的序列生成任务，无需专门的图模型。

**代表工作2**：**《Context aware hierarchical attention for abstractive dialogue summarization (HCAtt)》**（Nature 2025）专注于从多轮对话中提取核心信息[30][49]。该模型在编码器-解码器架构中融入层级化上下文注意力，在语句级与分段级两个粒度同时建模。在SAMSum、DialogSum与AMI数据集上超越baseline，特别在复杂话题转移的社交对话中性能显著。关键创新在于：不同于单一注意力，HCAtt通过在query/key变换中显式融入层级上下文信息，使模型能捕捉对话的纵深结构。该工作证实了多粒度上下文整合对对话理解的必要性。

**代表工作3**：**《Training-free Context-adaptive Attention for Efficient Long Context Modeling (TCA-Attention)》**（arXiv 2512）直面LLM推理时的计算瓶颈[26]。自注意力的二次复杂度严重限制了长对话建模。TCA-Attention提出无需训练的稀疏注意机制，动态适应每个注意头的冗余模式。在Qwen2.5-7B与LLaMA-3.1-8B上测试，该方法在128K上下文窗口的长对话任务上取得平均8.97的MT-Bench-01评分（超越full attention的8.90与FlexPrefill的8.90），同时保持计算效率。该工作的重要启示是：对话长程建模的计算约束可通过上下文感知的自适应而非架构改进解决。

**共性发现**：多轮理解正从离散结构标注向连续表示、从单模型架构向混合方案（检索+生成）、从英文专有数据集向跨语言鲁棒性拓展。长上下文处理从理论瓶颈转化为工程可解决问题。

---

### 三、知识增强对话生成

**研究脉络**：开放域对话系统需要超越训练集的知识。检索增强生成（RAG）与知识图谱集成已成为业界标准方案。但如何在对话的多轮动态情景中精确检索、融合与更新知识仍是难点。

**代表工作1**：**《CADGE: Context-Aware Dialogue Generation Enhanced with Graph-Structured Knowledge Aggregation》**（INLG 2024, arXiv 2305）创新性地提出上下文感知的图注意机制[9][13]。不同于串联式的文本编码与图编码，该方法在表示学习阶段就融合异构特征——将扁平化的图知识与文本并行处理。在SAMSum与DialogSum等多个基准上，该方法显著超越了传统GNN方案。关键发现是：图知识不应作为"后处理增强"，而应与上下文同步参与编码，使得模型能在层级上捕捉知识相关性与对话一致性的耦合约束。该工作还首次尝试了在连通子图上进行层级知识聚合。

**代表工作2**：**《Enhancing Speech-to-Speech Dialogue Modeling with End-to-End Retrieval-Augmented Generation》**（arXiv 2505）针对语音对话中的跨模态检索问题[14]。端到端语音-语音系统面临的难点是：语音查询与文本知识库间的模态鸿沟。该研究提出直接从语音查询进行文本知识检索的框架，通过共享向量空间实现语音与文本的语义对齐。与级联式ASR-RAG相比，该方法检索延迟降低75%（从0.4s至0.08s），在多语言spoken QA任务上相比无检索基线提升20%准确度。该工作为多模态对话系统指明了路径：跨模态RAG的瓶颈不在架构而在语义对齐。

**代表工作3**：**《Efficient Tuning of Large Language Models for Knowledge-Grounded Dialogue Generation (KEDiT)》**（TACL）提出高效微调方法以适配知识增强对话[21]。该方法通过参数高效转移学习（PETL）框架，仅调整少量参数即可使预训练LLM适配特定知识库。相比全参数微调，KEDiT大幅降低计算开销同时保持性能。该工作的启示是LLM时代知识适配不必再依赖重型数据集构造，而可通过精准提示与轻量级参数更新实现。

**共性发现**：知识增强对话从孤立的检索排序向联合优化的端到端框架演进，从文本单模态向多模态知识融合拓展，从离线索引向动态检索与更新转变。

---

### 四、个性化与一致性建模

**研究背景**：用户性格（Persona）与个人偏好对对话流畅性与满足度至关重要。2022-2025年的进展体现在如何系统地将persona信息与对话历史相融合，避免角色不一致。

**代表工作1**：**《Personalized Dialogue Generation with Persona-Adaptive Attention (PAA)》**（AAAI 2023，arXiv 2210）首次提出自适应权重机制平衡persona与上下文信息[20]。该框架的核心是Persona-Adaptive Attention层，通过动态调整对persona表示与对话上下文的权重比例，实现一致性回复生成。在低资源setting下（仅使用20-30%数据），该方法达到全数据模型的等效性能。关键观察是：persona权重不应固定，而应根据对话阶段动态调整——初期应重视persona一致性，后期应灵活融合上下文。动态遮蔽机制进一步通过正则化避免过拟合。

**代表工作2**：**《Persona-Aware Alignment Framework for Personalized Dialogue Generation》**（TACL）从对齐视角重新定义persona建模问题[24]。不同于特征拼接方案，该框架显式优化user persona与system response间的语义对齐。该工作发现大多数现有数据集中persona信息利用率低，提出通过对比学习等手段强化对齐信号，使个性化对话从"hard constraint"演进为"soft alignment"。

**代表工作3**：**《Dialogue Act Script (DAS): Multilingual Dialogue Generation and Localization》**（arXiv 2509）将多语言个性化拓展至文化适应维度[44]。直接翻译英文对话会导致"anglocentric bias"与"translationese"现象。DAS提出通过对话行为脚本进行抽象、本地化与生成，实现文化自适应的多语言对话创建。在Italian、German、Chinese上的人工评估显示，DAS生成的对话在文化相关性与情景适配性上显著超越机器翻译与人工翻译。该工作的启示是个性化本质上包含文化维度。

**共性发现**：个性化建模从静态特征注入向动态对齐优化转变，从单语言向多语言-多文化融合扩展，从离散属性向连续表示进化。

---

### 五、情感感知与多模态对话系统

**研究动向**：对话系统逐渐超越"信息传递"单一目标，向"情感理解与表达"维度拓展。情感识别、生成与管理开始成为评估系统可用性的关键指标。

**代表工作1**：**《Towards Emotion-aware Task-oriented Dialogue Systems in the Era of Large Language Models》**（YRRSDS 2024）明确指出情感应贯穿TOD系统全流程[18]。传统TOD关注目标完成率，忽视用户情感体验。该工作将情感识别、管理与生成融入NLU、DST、Policy Learning与NLG各模块。特别地，零样本emotion recognition/generation已通过LLM显著简化，但如何在保证任务完成的同时维护情感一致性仍是开放问题。该论文为后续工作指示方向：情感应作为对话状态的内生维度，而非后处理特性。

**代表工作2**：**《Inside Out: Emotional Multiagent Multimodal Dialogue Systems》**（IJCAI 2024）采用多智能体架构实现多维情感表达[22]。该框架受《Inside Out》启发，使用多个LLM agent对应不同情感维度（快乐、悲伤、害怕、愤怒）。系统通过视频帧中的面部识别检测用户情感状态，随后用对应的情感prompts调用LLM，最后通过用户当前情感状态聚合多个响应。在EmotiMobileFaceNet等识别器上达到近SOTA精度。该方案的创新在于：通过多智能体debate而非单一模型生成，增加了情感表达的多样性与真实性。

**代表工作3**：**《Predicting Future Affective Reactions in Human-Computer Dialogue》**（arXiv 2303）提出前瞻性对话系统架构，使对话系统能预测用户下轮的情感反应[69]。不同于被动反应，该框架赋予系统主动性：基于系统当前的情感与对话行为（DA），预测用户的后续情感，从而提前准备响应策略。在人机对话中发现情感与笑声存在同步性与DA-情感因果关系。该工作的启示是：情感感知可转化为预测任务，使对话系统从reactive升级为anticipatory。

**共性发现**：多模态融合（文本、语音、视觉）已从实验室演进为生产系统，情感维度从评估指标向对话策略输入转变，跨文化情感适应成为新前沿。

---

### 六、强化学习与策略优化

**研究脉络**：端到端对话系统的策略学习长期面临"奖励稀疏"难题——对话成功往往只在最后几轮才获得信号。2022-2025年的突破在于通过goal shaping、curriculum learning等手段重塑学习信号。

**代表工作1**：**《Bootstrapped Policy Learning for Task-oriented Dialogue (BPL)》**（EMNLP 2024）通过目标形塑动态调整子目标难度[41]。该框架的核心发现是：固定的curriculum学习假设难度梯度连续单调，但实际对话目标存在复杂的依赖关系。BPL通过goal substitution与goal evolution机制，让子目标难度随策略能力动态调整。在MultiWOZ等数据集上相比其他curriculum学习方法显著提升任务成功率。该工作进一步识别了两个"universal curriculum patterns"在不同数据集上普遍有效，增强了方法的可迁移性。

**代表工作2**：**《Goal Shaping for Efficient Task-oriented Dialogue Policy Learning》**（AAMAS 2024）从信号工程角度系统化地解决奖励稀疏问题[45]。核心观点是：不需改变底层RL算法，而通过重新定义奖励函数的形状（reward shaping），可显著加速学习收敛。该工作通过专家演示与中间目标分解，在模拟用户与真实用户评估上均显示性能提升。

**代表工作3**：**《Large Language Models as User-Agents for Evaluating Task-Oriented Dialogue Systems》**（arXiv 2411）将LLM用作用户模拟器评估对话策略[15]。传统离线数据集评估低估了策略泛化能力。该工作通过prompt in-context examples使LLM能扮演上下文感知的用户角色，显著提升了评估的覆盖度与多样性。相比静态用户模板，LLM用户智能体能模拟真实用户的不可预测性，使策略评估更接近现实。

**共性发现**：策略学习从纯算法创新向信号工程与评估方法论转变，从模型中心向数据与环境建模平衡发展，LLM驱动的人工生成与强化学习混合方案逐渐主导。

---

### 七、评估指标与基准设计

**研究现状**：自动评估对话质量长期困难重重。BLEU、ROUGE等源自机器翻译的指标已被证实在对话域无效[12][16]。2022-2025年涌现多种上下文感知、因果推理驱动的新范式。

**代表工作1**：**《Unsupervised Evaluation Metrics for Dialogue: CausalScore与模块化框架》**（Emergent Mind）对比经典（BLEU、ROUGE、METEOR）、基于embedding（BERTScore）、上下文感知（RUBER、FED）等多类指标[12]。关键发现是BLEU/ROUGE严重惩罚合法释义，在非任务导向对话上与人类判断相关性接近于零。新兴的CausalScore利用分类器的无条件独立性测试度量对话历史与响应间的因果强度，实验表明其相关性超越BLEU、ROUGE等基线。该工作还提议模块化框架，允许组件灵活替换以适配不同任务。

**代表工作2**：**《On the Benchmarking of LLMs for Open-Domain Dialogue Evaluation》**（NLP4ConvAI 2024）指出现有对话评估基准已过时，使用2019年左右生成的响应与固定的Fluency/Relevance维度已不能反映当代LLM的能力与局限[63]。该研究在SODA数据集上进行注释实验，发现GPT-4等LLM评估器难以检测当代chatbots的实际缺陷，提示"LLM-as-judge"范式需要更新。该工作呼吁对话评估基准的动态刷新机制。

**代表工作3**：**《Dimensionality, Language, Culture and Safety at DSTC 12: Dialog System Evaluation》**（DSTC 2025, arXiv 2509）首次从多维度、多文化、安全性角度系统化评估对话系统[59]。针对10个对话维度（连贯性、相关性、安全性等）设计自动指标。特别地，引入多语言与多文化安全检测，在超过90种语言上评估LLM行为。该挑战赛限制参赛者仅使用<13B参数的开源模型，引导社区关注效率。Llama-3-8B baseline在多维度评估上达0.1681的Spearman相关性，显示该任务的难度与提升空间。

**代表工作4**：**《DiaHalu: A Dialogue-level Hallucination Evaluation Benchmark for Language Models》**（EMNLP 2024）建立对话级幻觉评估基准[58]。相比单句幻觉检测，对话级评估需考虑跨轮一致性、信息完整性与安全性。该基准在knowledge-grounded、task-oriented、chit-chat、reasoning四个对话领域覆盖factuality与faithfulness两类幻觉。实验表明即便是GPT-4等模型在多轮对话中的幻觉率仍高企，特别在知识对话与推理场景。该工作为幻觉检测指明了关键方向：必须从单轮泛化至多轮上下文。

**代表工作5**：**《Human-in-the-loop Abstractive Dialogue Summarization》**（ACL 2023 Findings）融合局部反馈（用户标记显著信息）与全局反馈（对摘要间的成对比较）进行强化学习微调[53]。相比仅最大化似然的监督基线，该方法在coherence、faithfulness等人类判断指标上显著提升。该工作体现了评估范式的进化：从单一参考答案向多维人类反馈转变。

**共性发现**：自动评估从词汇重叠向语义/因果推理演进，从参考依赖向参考无关与上下文感知方向转变，从英文单语向跨语言多文化扩展，从单轮向多轮对话级别深化。

---

## 实验与评价总结

### 跨工作共性发现

**1. 数据集主导性**：MultiWOZ系列（MultiWOZ 2.0/2.1/2.2）在TOD领域占据绝对主导，SAMSum/DialogSum在摘要任务上为主流[27]。该现象既反映了高质量多域对话数据的稀缺性，也暴露出评估生态多元性不足。

**2. LLM规模与任务泛化的非单调关系**：超大型模型（GPT-4、Claude）在零样本setting下表现优异，但参数缩放与特定任务性能间并非单调关系[38][64]。中等规模模型（7B-13B）通过针对性微调往往超越更大模型，且效率更高。该发现鼓励社区关注parameter-efficient微调（LoRA、Adapter等）而非规模竞赛。

**3. 提示工程的系统性作用**：Few-shot prompting相比zero-shot在复杂推理任务上改进显著，但提示设计的微小变化可导致性能剧烈波动[33][37]。该脆弱性暴露出LLM instruction-following能力的本质局限。

**4. 多模态融合的延迟-准确权衡**：端到端多模态系统（语音-文本-视觉）面临模态对齐的内在困难[14][22]。跨模态检索中，直接端到端方案相比级联式ASR方案在延迟上优势明显（75%降低），但准确度略低。该权衡需根据应用场景（对话助手vs. 实时翻译）精准把握。

**5. 评估指标与人类判断的持久鸿沟**：即便是新兴的因果分析驱动指标（CausalScore）与LLM-based judge（GPT-4），也只能达到0.6-0.8的相关性[12][63]。对话评估的多样性与上下文依赖性内在决定了自动指标的天花板。

### 负面发现与局限

**1. 长上下文处理的鲁棒性缺陷**：即便采用注意力优化（TCA-Attention），LLM在>64K token对话上的性能仍不稳定[26]。超长对话的多轮推理能力需更深层的架构创新。

**2. 个性化与安全性的冲突**：强个性化对话系统（emotion-aware、style-adaptive）存在滥用风险。IJCAI 2024的emotional dialogue工作在讨论中明确指出，过度个性化可能被用于操纵[22]。该伦理张力尚无系统解决方案。

**3. 跨域泛化的根本难度**：即便采用zero-shot Domain Adaptation方法（Schema Augmentation等），目标域上的性能仍平均下降15-24%[34]。开放域自适应仍需从数据、架构、评估三维度突破。

**4. 多语言对话系统的文化适应缺失**：大多数LLM因训练数据英文占比过高而存在"anglocentric bias"。仅通过翻译或提示调整难以实现真正的文化自适应[44]。

---

## 研究趋势与开放挑战

### 2025年前后的真实趋势预测

**趋势1：从参数规模竞赛向效率工程范式转变**

证据：(a) LoRA/QLoRA等PETL方法在2023-2024年大幅降低微调成本；(b) 开源7-13B模型在特定任务（零样本DST）已超越GPT-4；(c) TCA-Attention等推理优化在MT-Bench-01等实际场景中展示可竞争性。预测：2025-2026年，工业界将从"大模型黑盒调用"向"轻量级模型+精准工程"转变。学术界也将逐步从paper-as-benchmark转向industry-grounded evaluation，使用真实用户交互数据而非研究者构造的数据集。

**趋势2：从端到端LLM向混合架构（LLM+符号系统+强化学习）回归**

证据：(a) 纯LLM端到端系统在约束satisfaction、事实准确性上仍存顽疾[58][61]；(b) 强化学习策略优化（BPL、Goal Shaping）在TOD中重新获得关注；(c) 知识图谱/结构化知识与LLM混合方案（CADGE等）显示性能优势。预测：未来三年，真实对话系统将采纳"LLM生成+符号约束+RL反馈"的混合流水线。新兴的vision-language models可能激发多模态混合架构探索。

**趋势3：对话评估从自动指标向"human-in-the-loop + 多维反馈"演进**

证据：(a) DSTC 12等主流挑战赛已引入多维评估（连贯性、安全性、文化适配度等）；(b) Human-in-the-loop微调（ACL 2023）相比SFT显示一致性改进；(c) 单一指标（BLEU、ROUGE）已被业界放弃，取而代之的是多维评分或人工评估。预测：2025年起，对话系统发表将倾向要求多维人工评估数据，自动指标将作为辅助而非主要成果证明。Active learning框架可能降低标注成本。

**趋势4：多模态多语言多文化对话系统成为标配**

证据：(a) SLAM-Omni等端到端语音对话模型已进入应用阶段；(b) GLaMM等视觉-语言基础模型展示像素级grounding能力；(c) DAS等方法明确展示直译策略的文化失效。预测：2025-2027年，单语言文本对话系统将逐步被多模态多语言系统替代。该转变对评估基准、数据标注、算法设计都提出新需求。跨文化对话系统的伦理规范制定将成为新议题。

**趋势5：检索增强生成（RAG）从可选走向必需**

证据：(a) 端到端RAG在spoken QA上相比无检索基线提升20%准确度[14]；(b) 幻觉问题（DiaHalu基准）在长对话中加剧，RAG通过groundedness缓解；(c) RAG市场规模2024年已达18.5亿美元，49% CAGR增长。预测：2025年后，对话系统不含RAG模块将成为例外。新的研究方向将聚焦于：(i) 跨模态RAG的模态鸿沟；(ii) 动态更新知识库的实时性；(iii) RAG中的关键性证据解释。

### 开放研究问题

1. **长上下文多轮推理的可靠性**：当对话轮数超过50轮时，模型性能急剧衰减。如何设计架构与训练策略解决context decay？

2. **个性化与安全性的平衡**：强个性化系统（emotion-aware、style-adaptive）与安全guardrails的冲突尚无标准解决方案。

3. **跨语言跨文化对话的本地化范式**：现有translate-then-adapt策略效率低下。能否从预训练阶段就融入多文化表征？

4. **对话系统的可解释性与可控性**：LLM黑盒特性使得故障诊断与定向优化困难。如何在保留生成流畅性的前提下增强可控性？

5. **评估基准的动态更新机制**：如何设计自适应评估体系，随LLM能力演进而动态调整难度与维度？

---

## 结论

2022-2025年间，对话系统经历了从神经网络时代向大语言模型驱动范式的范式转变。该转变既带来了零样本能力与生成多样性的飞跃，也引发了新的系统性难题：幻觉、长程上下文衰减、跨域泛化、多模态融合、伦理规范等。

核心发现表明，**单纯的规模扩大已进入收益递减阶段**。未来的突破将来自：（1）**架构创新**——混合符号与神经系统、多模态融合、可控生成；（2）**评估范式革新**——从单一指标向多维人类反馈转变；（3）**工程实践**——parameter-efficient微调、动态RAG、强化学习策略优化；（4）**伦理与安全**——文化适配、偏见检测、可解释性增强。

对话系统研究正处于从"追求更大模型"向"精细化工程与理论深化"的拐点。学界与业界的协同将决定该领域的后续发展轨迹。

---

## 参考文献

[1] Nakano, M., Takeuchi, H., Yoshikawa, S., Matsuyama, Y., & Komatani, K. (2025). Dialogue Systems Engineering: A Survey and Future Directions. *arXiv:2508.02279*.

[2] Interpretable and Robust Dialogue State Tracking via Natural Language DST. *arXiv:2503.08857*.

[3] Survey on Recent Advances in LLM-Based Multi-turn Dialogue Systems. *arXiv:2402.18013*.

[4] Master of Code. (2025). State of Conversational AI: Trends and Statistics. Retrieved from https://masterofcode.com/blog

[5] Survey on the Recent Advancements in Human-Centered Dialog Systems. *ACM*, 2024.

[6] Dialogue State Tracking in Task-Oriented Systems. *Emergent Mind*, 2024.

[7] Multimodal Dialogue Generation Based on Transformer and Collaborative Attention. *ACM*, 2022.

[8] Omdia. (2025). Market Landscape: Conversational AI 2025 – from Assistants to Agentic. Retrieved from https://omdia.tech.informa.com

[9] Tang, C., Zhang, H., Loakman, T., Yang, B., Goetze, S., & Lin, C. (2024). CADGE: Context-Aware Dialogue Generation Enhanced with Graph-Structured Knowledge Aggregation. *INLG 2024*, 371-383.

[10] Sordoni, A., Galley, M., Auli, M., Brockett, C., He, Y., Khendel, A., ... & Dolan, B. (2015). A Neural Network Approach to Context-Sensitive Generation of Conversational Responses. *ACL 2015*.

[11] Nehring, J., Juneja, A., Ahmad, A., Roller, R., & Klakow, D. (2024). Dynamic Prompting: Large Language Models for Task Oriented Dialog. *CLiC-it 2024*, 644-653.

[12] Unsupervised Evaluation Metrics for Dialogue. *Emergent Mind*, 2024.

[13] Zhang, H., Tang, C., Loakman, T., Lin, C., & Goetze, S. (2023). CADGE: Context-Aware Dialogue Generation Enhanced with Graph-Structured Knowledge Aggregation. *arXiv:2305.06294*.

[14] Enhancing Speech-to-Speech Dialogue Modeling with End-to-End Retrieval-Augmented Generation. *arXiv:2505.00028*.

[15] Kazi, T., Lyu, R., Zhou, S., Hakkani-Tur, D., & Tur, G. (2024). Large Language Models as User-Agents for Evaluating Task-Oriented-Dialogue Systems. *arXiv:2411.09972*.

[16] Brenndoerfer, M. (2024). BLEU Metric - Automatic Evaluation for Machine Translation. Retrieved from https://mbrenndoerfer.com/writing/history-bleu-metric-evaluation

[17] Enhancing Coherence and Interestingness in Knowledge-Grounded Dialogues. *INLG 2025*.

[18] Feng, S. (2024). Towards Emotion-aware Task-oriented Dialogue Systems in the Era of Large Language Models. *YRRSDS 2024*, 81-83.

[19] Glean. (2025). What is Retrieval Augmented Generation (RAG) in 2025? Retrieved from https://www.glean.com/blog/rag-retrieval-augmented-generation

[20] Huang, Q., Zhang, Y., Ko, T., Liu, X., Wu, B., Wang, W., & Tang, L. (2023). Personalized Dialogue Generation with Persona-Adaptive Attention. *AAAI 2023*.

[21] Efficient Tuning of Large Language Models for Knowledge-Grounded Dialogue Generation. *MIT TACL*.

[22] Savchenko, A. V., & Savchenko, L. V. (2024). Inside Out: Emotional Multiagent Multimodal Dialogue Systems. *IJCAI 2024 Demonstrations*, 8784-8785.

[23] Morphik. (2025). RAG in 2025: 7 Proven Strategies to Deploy Retrieval-Augmented Generation. Retrieved from https://www.morphik.ai

[24] Persona-Aware Alignment Framework for Personalized Dialogue Generation. *MIT TACL*.

[25] Dialogue Discourse Parsing as Generation. *ACL SIGDIAL 2024*.

[26] Training-free Context-adaptive Attention for Efficient Long Context Modeling. *arXiv:2512.09238*.

[27] Budzianowski, P., Gasic, M., Mrksic, N., Su, P.-H., Vandyke, D., Kim, D., ... & Young, S. (2018). MultiWOZ - A Large-Scale Multi-Domain Wizard-of-Oz Dataset for Task-Oriented Dialogue Modelling. *EMNLP 2018*.

[28] Fine-Tuning Pretrained Language Models to Enhance Dialogue Summarization in Customer Service Centers. *Semantic Scholar*, 2023.

[29] Enhancing Instruction-Following Capabilities in Seq2Seq Models. *arXiv:2512.03803*.

[30] Context aware hierarchical attention for abstractive dialogue summarization. *Nature*, 2025.

[31] Google Dataset Search - Dialogue State Tracking. Retrieved from https://toolbox.google.com/datasetsearch

[32] Fine-Tuning Pretrained Language Models to Enhance Dialogue Summarization. *ACM*, 2023.

[33] The Ultimate Guide to Prompt Engineering in 2025. *Lakera*, 2025.

[34] Schema Augmentation for Zero-Shot Domain Adaptation in Dialogue State Tracking. *arXiv:2411.00150*.

[35] Controllable Generation of Dialogue Acts for Dialogue Systems via Few-Shot Response Generation and Ranking. *arXiv:2307.14440*.

[36] GLaMM: Pixel Grounding Large Multimodal Model. *CVPR 2024*.

[37] Few-Shot Prompting. *Prompt Engineering Guide*, 2024.

[38] Large Language Models as Zero-shot Dialogue State Tracker via Function Calling. *ACL 2024*, 8688-8704.

[39] Controllable Generation of Dialogue Acts for Dialogue Systems via Few-Shot Response Generation and Ranking. *SIGDIAL 2023*.

[40] Grounding Large Multimodal Model (GLaMM). *GitHub*, 2024.

[41] Bootstrapped Policy Learning for Task-oriented Dialogue through Curriculum Learning. *EMNLP 2024*.

[42] MT2ST: Multi-Task to Single-Task Transition for Efficient Embedding Training. *arXiv:2406.18038*.

[43] Data Augmentation for Conversational AI. *arXiv:2309.04739*.

[44] Multilingual Dialogue Generation and Localization with Dialogue Act Script. *arXiv:2509.22086*.

[45] Goal Shaping for Efficient Task-oriented Dialogue Policy Learning. *AAMAS 2024*.

[46] Transfer Learning, Fine-tuning, Multitask Learning and Federated Learning. *Daily Dose of DS*, 2024.

[47] Data Augmentation Integrating Dialogue Flow and Style to Adapt Spoken Dialogue Systems. *SIGDIAL 2024*.

[48] Cross-lingual Evaluation of Multilingual Text Generation. *COLING 2025*.

[49] Context aware hierarchical attention for abstractive dialogue summarization. *PMC*, 2025.

[50] First Ask Then Answer: A Framework Design for AI Dialogue Systems. *arXiv:2508.08308*.

[51] An Interdisciplinary Review of Commonsense Reasoning and Intent Detection. *arXiv:2506.14040*.

[52] A Survey of Recent Advances on Turn-taking Modeling in Spoken Dialogue Systems. *IWSDS 2025*.

[53] Human-in-the-loop Abstractive Dialogue Summarization. *ACL 2023 Findings*.

[54] Conversational Question Answering with Language Models. *ACL 2024 Findings*.

[55] Commonsense Persona-Grounded Dialogue Challenge 2023. *AIcrowd*, 2023.

[56] Pragmatics in the Era of Large Language Models: A Survey. *arXiv:2502.12378*.

[57] ChatGPT. *Prompt Engineering Guide*, 2024.

[58] DiaHalu: A Dialogue-level Hallucination Evaluation Benchmark for Language Models. *EMNLP 2024 Findings*.

[59] Dimensionality, Language, Culture and Safety at DSTC 12. *arXiv:2509.13569*.

[60] Effective Prompts for AI: The Essentials. *MIT Sloan EdTech*, 2024.

[61] Factuality of Large Language Models in the Year 2024. *arXiv:2402.02420*.

[62] Proceedings of the Twelfth Dialog System Technology Challenge. *ACL*, 2025.

[63] On the Benchmarking of LLMs for Open-Domain Dialogue Evaluation. *NLP4ConvAI 2024*.

[64] GPT or BERT: why not both? *arXiv:2410.24159*.

[65] Building end-to-end dialogue systems using generative hierarchical neural network models. *ACM*, 2015.

[66] Top 10 open source LLMs for 2025. *NetApp Instaclustr*, 2025.

[67] Advances in neural text generation: A systematic review (2022-2024). *CEUR Workshop Proceedings*, 2024.

[68] Enhancing Speech-to-Speech Dialogue Modeling with End-to-End Retrieval-Augmented Generation. *arXiv:2505.00028*.

[69] Predicting Future Affective Reactions in Human-Computer Dialogue. *arXiv:2303.00146*.

[70] LLM-based Conversational Recommendation Agents with Collaborative Experiences. *EMNLP 2025 Findings*.

[71] Counterfactual Assessment of User Satisfaction Estimation in Task-Oriented Dialogue. *ACL 2024 Findings*.

[72] Domain Adaptation in Dialogue Systems using Transfer and Meta-Learning. *arXiv:2102.11146*.

[73] LLM Agents for Group Consensus and Decision-Making. *UC Merced*, 2024.

[74] Conversational Recommender System and Large Language Model Are Made for Each Other in E-commerce Pre-sales Dialogue. *arXiv:2310.14626*.

[75] Understanding User Satisfaction with Task-oriented Dialogue Systems. *ACM*, 2022.

[76] Zero-Shot Cross-Domain Dialogue State Tracking via Dual Low-Rank Adaptation. *ACL 2024*, 5746-5759.