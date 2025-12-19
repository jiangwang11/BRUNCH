语境学习（In-Context Learning）在自然语言处理中的深度综述：从涌现机理到工程范式的演进 (2022–2025)
1. 引言
在过去的几年中，大语言模型（Large Language Models, LLMs）的迅猛发展彻底重塑了自然语言处理（NLP）的研究范式。其中，语境学习（In-Context Learning, ICL）作为一种无需参数更新即可适应下游任务的新兴能力，引起了学术界的广泛关注。与传统的“预训练-微调”（Pre-training & Fine-tuning）范式不同，ICL 允许模型仅通过在推理阶段的上下文中提供少量的输入-输出示例（Demonstrations）和自然语言指令，即可通过类比推理解决复杂的未见任务 。这种范式的转变不仅极大地降低了模型部署的计算成本，更标志着人工智能从“特定任务建模”向“通用类比推理”的根本性跨越。   

尽管 ICL 在实证层面取得了令人瞩目的成功，特别是在少样本（Few-shot）和零样本（Zero-shot）场景下展现出了惊人的泛化能力，但其背后的工作机制长期以来被视为“黑盒”。模型究竟是如何从这寥寥数个示例中“学习”到任务规则的？这种学习是基于梯度的隐式模拟，还是贝叶斯推断的具象化？2022 年至 2025 年间，学术界的研究重心已从早期的现象观察和简单的提示工程（Prompt Engineering），转向了对 ICL 内在机理的深度解构、系统化的演示优化算法设计，以及在多模态、长文本等复杂场景下的边界探索。

本综述旨在对 2022 年至 2025 年间 ICL 领域的代表性工作进行详尽的梳理与深度分析。报告将首先探讨支撑 ICL 的理论基础，涵盖贝叶斯推断、归纳头机制及技能学习视角；随后深入剖析演示示例选择、排序与指令格式化的前沿优化方法；接着评估 ICL 在多模态推理、低资源语言及长文本场景下的表现与局限；最后基于 2025 年的最新研究进展，预测未来的技术演进趋势。

2. 理论机制：从黑盒观测到数学解构
ICL 为何有效？这是理解当前大模型能力边界的核心问题。2022-2025 年的研究逐渐揭示，ICL 并非简单的模式匹配或记忆检索，而是涉及复杂的隐式推理过程。目前的主流理论流派主要包括：隐式贝叶斯推断视角、机械可解释性（Mechanistic Interpretability）视角，以及数据生成视角的技能学习理论。

2.1 隐式贝叶斯推断与标度律
贝叶斯观点认为，预训练语言模型在海量数据中学习到了各种任务的先验分布（Prior Distribution），而 ICL 的过程本质上是在推理阶段根据上下文示例计算后验概率（Posterior Probability）。

Bayesian Scaling Laws for In-Context Learning (2024)    

问题：尽管已有研究尝试用幂律（Power Law）来描述模型性能随规模增长的趋势，但现有的 ICL 性能预测模型缺乏坚实的理论基础，无法解释微调（Fine-tuning）与 ICL 之间的内在联系，也难以预测“多样本”（Many-shot）场景下的性能饱和行为。

方法：Jeong 等人（2024）基于贝叶斯推断框架，推导出了专门针对 ICL 的贝叶斯标度律（Bayesian Scaling Laws）。该理论模型假设 LLM 在处理每个上下文示例后进行隐式的贝叶斯更新。作者引入了“ICL 效率系数”（ICL Efficiency Coefficient, K）来量化示例的信息密度，并将上下文长度（示例数量 n）与预测概率建立了明确的数学联系：−logp(θ∣D)∝n 
−α
 ，其中 α 与数据的信噪比相关。

结论：研究发现，该贝叶斯标度律能精确拟合不同模型规模和示例长度下的 ICL 性能曲线，且比传统幂律具有更好的解释力。更重要的是，理论推导揭示了 ICL 的效率与预训练分布的先验知识密切相关——微调可能仅是重新加权了任务先验（Reweighting Priors），而非注入新知识。这一发现为“预训练决定 ICL 上限”的假设提供了数学支持。

An In-Context Learning Theoretic Analysis of Chain-of-Thought (2024)    

问题：思维链（Chain-of-Thought, CoT）显著增强了模型的推理能力，但其背后的学习理论机制尚不明确。尤其是，为什么增加中间推理步骤（即使这些步骤增加了输入的长度）反而能降低学习难度？

方法：Yang 等人（2024）从学习理论（Learning Theory）的角度建立了一个分析框架。他们将 CoT 视为一种将复杂非线性函数分解为简单预测器组合的过程。通过构建一个理论上的 ICL 算法类，作者证明了 Transformers 能够通过少量的 CoT 提示学习到复杂的复合函数，而这在仅有输入-输出对（Input-Output Pairs）的情况下是数学上不可行的。

结论：理论分析表明，CoT 的有效性在于它打破了“最难推理步骤”的瓶颈（Complexity Bottleneck）。在没有 CoT 的情况下，模型必须一步跨越巨大的推理鸿沟；而 CoT 将其转化为多个样本效率极高的子步骤。实验进一步证实，基于此理论指导设计的 CoT 提示在算术和布尔逻辑任务上显著优于传统方法，有时能将准确率从随机猜测提升至接近完美。

2.2 机械可解释性：归纳头与功能向量
除了宏观的贝叶斯视角，另一派研究致力于打开 Transformer 的黑盒，寻找负责 ICL 的具体神经回路。这一领域的进展主要围绕“归纳头”（Induction Heads）及其演变形式展开。

Function Vectors in Large Language Models (2024)    

问题：大模型如何在其内部状态中表示各种 ICL 任务？这些任务是分散在整个网络中，还是存在局部的、可提取的“功能表示”？

方法：Todd 等人（2024）通过因果中介分析（Causal Mediation Analysis）识别出了一组特定的注意力头（Attention Heads），发现它们在处理 ICL 任务时会被高度激活。研究团队提出了一种方法，通过聚合这些头的输出，提取出了“功能向量”（Function Vectors, FVs）。为了验证其有效性，作者尝试将这些向量注入到其他无关的上下文中，观察是否能触发相应的任务行为。

结论：实验结果令人震惊：功能向量紧凑地编码了任务特定的信息（如“反义词生成”或“国家-首都匹配”）。即使在没有相关示例的零样本场景下，仅注入该向量也能诱导模型执行特定任务。这证明了 LLM 内部存在模块化的功能抽象，ICL 的过程可以被视为对这些潜在功能模块的激活（Activation）与组合。

Not All Induction Heads Are Created Equal (2025)    

问题：早期的“归纳头”理论（Olsson et al., 2022）认为 ICL 主要依赖于一种简单的“复制前文出现的模式”的机制（即 $ \rightarrow B$）。然而，这种简单的复制机制难以解释复杂的语境依赖行为和多步推理。

方法：Saanum 等人（2025）在 Qwen2.5-1.5B 等先进模型上进行了细粒度的注意力头分析。研究考察了当上下文中存在多个候选后继词（Successor Tokens）时，模型如何选择关注点。作者定义了不同类型的归纳头，并分析了它们在不同层级的分布与行为差异。

结论：研究发现，归纳头远比之前认为的复杂，表现出多样化的策略：有的关注最近的模式（Recency Bias），有的关注最早的模式（Primacy Bias），甚至有的能够结合二阶语境线索（即前序词的前序词）进行预测。这意味着 ICL 并非简单的机械复制，而是通过多层归纳头的协同工作，实现了对上下文依赖关系的复杂计算与动态路由。

2.3 技能学习与技能识别
A Survey to Recent Progress Towards Understanding In-Context Learning (2024/2025)    

问题：关于 ICL 是在“学习新知识”还是在“识别旧知识”存在长期争论。这一区分对于理解模型的泛化边界至关重要。

方法：Mao 等人（2024/2025）通过数据生成的视角重新定义了 ICL，将其严格区分为“技能识别”（Skill Recognition）和“技能学习”（Skill Learning）。“技能识别”是指模型激活预训练中已有的函数（如翻译、分类），而“技能学习”是指模型从上下文中学习从未见过的数据生成函数（如合成的线性回归规则）。

结论：分析指出，当前的 LLM 在 ICL 中主要表现为技能识别，即从示例中定位预训练分布中的特定任务。然而，在某些合成数据实验中，模型也展示了有限的技能学习能力，表现为类似梯度下降（Gradient Descent）的优化行为。这一理论框架解释了为什么 ICL 在处理反常识任务（如将“好”定义为负面情感）时往往表现不佳——因为这与预训练的“技能”冲突。

3. 方法分类：演示优化的工程范式
为了最大化 ICL 的性能，研究者在演示示例的“选择（Selection）”、“排序（Ordering）”和“格式化（Formatting）”三个维度上提出了大量优化算法。这些方法旨在解决 ICL 固有的不稳定性（Instability）和对提示形式的敏感性。

3.1 演示示例选择 (Demonstration Selection)
选择即检索。如何从海量训练数据中找到最能帮助当前输入 x 的 k 个示例是提升 ICL 性能的关键。2024-2025 年的研究不仅关注语义相似性，更引入了基于学习和反馈的复杂选择机制。

Mixture of Demonstrations for In-Context Learning (NeurIPS 2024)    

问题：传统的检索方法（如 BM25 或基于 BERT 的语义相似度）在高维、庞大的搜索空间中往往难以找到最优解。此外，简单的相似性检索忽略了不同示例组合后的协同效应（Synergy），且容易选出包含误导信息的“相似但错误”的样本。

方法：Wang 等人（2024）提出了“混合演示”（Mixture of Demonstrations, MoD）框架。该方法借鉴了混合专家模型（MoE）的思想，将演示池划分为多个组，每组由一个“专家”检索器管理。MoD 设计了一种专家级训练策略（Expert-wise Training），优化检索模型使其能够区分有益和有害的示例。在推理时，多个专家协同工作，为当前查询检索出最佳组合。

结论：MoD 有效降低了检索的搜索空间复杂度，同时保证了检索结果的多样性和相关性。在多个 NLP 任务上的实验显示，MoD 显著优于现有的检索基线（如 K-NN 和随机采样），尤其是在示例池规模巨大的情况下，其优势更加明显，确立了新的 SOTA 标准。

In-Context Learning with Iterative Demonstration Selection (EMNLP 2024)    

问题：现有的选择方法存在两难：仅关注语义相似度可能导致信息冗余（Redundancy），而仅关注多样性可能引入无关噪声。更关键的是，仅基于输入（Input-based）的选择忽略了模型对特定示例的推理路径（Reasoning Path）的偏好。

方法：Qin 等人（2024）提出了“迭代演示选择”（Iterative Demonstration Selection, IDS）。该方法利用零样本思维链（Zero-shot CoT）生成的推理路径作为反馈信号。IDS 通过迭代的方式，根据模型对测试样本的初步回答及其推理过程，去检索那些既具有多样性又与测试样本在推理逻辑上高度相关的示例。

结论：IDS 能够在兼顾多样性与相关性的同时，利用模型自身的推理反馈来精炼示例集。实验表明，该方法在算术推理、问答和分类任务上均取得了一致的性能提升，尤其是在需要复杂推理步骤的任务中，IDS 能有效避免“推理断链”。

Unraveling the Mechanics of Learning-Based Demonstration Selection (ACL 2025)    

问题：随着“多样本学习”（Many-shot ICL）的兴起，传统的针对少样本（Few-shot）的选择方法由于计算复杂度过高（O(n 
2
 )）不再适用，导致现有 Many-shot 工作主要依赖低效的随机采样。

方法：Liu 等人（2025）提出了一种基于潜在概念学习（Latent Concept Learning）的高效选择策略。该方法在一个小型代理模型上学习任务的潜在嵌入，并计算每个示例对学习过程的梯度贡献（Gradient Contribution）。最终选择那些梯度方向最能促进模型收敛、最大化任务概念区分度的示例。

结论：该方法不仅在计算上可扩展至 Many-shot 场景，而且通过梯度视角的选择，揭示了高质量演示往往是那些位于决策边界附近、信息量最大的样本。

表 1：主流演示选择方法对比

方法类别	代表算法	选择依据	优点	缺点	适用场景
无监督检索	K-NN, BM25	语义/词汇相似度	计算快，无需训练	忽略标签影响，易选错	简单的分类/抽取任务
基于学习	
MoD 

专家模型打分	考虑组合效应，鲁棒性高	需额外训练检索器	大规模演示池
迭代反馈	
IDS 

CoT 推理路径	逻辑相关性强	推理成本高（多轮生成）	复杂推理 (Math, Logic)
梯度/概念	
LCL 

梯度贡献/概念区分	理论解释性强，适合 Many-shot	需代理模型计算梯度	长上下文/多样本任务
  
3.2 演示排序与不变性 (Ordering & Invariance)
ICL 对示例顺序极度敏感，不同的排列可能导致准确率在 50% 到 90% 之间剧烈波动。这主要源于 Transformers 的自回归特性导致的“近期偏见”（Recency Bias）。

Rethinking Invariance in In-context Learning (ICLR 2025)    

问题：理想的 ICL 算法应当满足“排列不变性”（Permutation Invariance），即无论示例顺序如何，预测结果应一致。然而，现有的解决方法（如特定掩码策略）往往会牺牲上下文信息的相互依赖性（Context Interdependence），导致性能下降。

方法：Fang 等人（2025）提出了 InvICL（Invariant In-Context Learning）算法。该方法利用“留一法”（Leave-one-out）嵌入策略：在计算每个示例的表示时，允许其参考所有其他示例，但在预测时保持对目标输入的独立性。这种设计在数学上保证了排列不变性，同时最大化了上下文间的相互依赖。

结论：InvICL 在理论上实现了严格的排列不变性，并在实证上超越了基于前缀（Prefix）或传统的自回归 ICL 方法。它证明了消除顺序敏感性不需要牺牲模型的表达能力，是解决 ICL 鲁棒性问题的重要方向。

Impact of Model Scale on Sensitivity (2024)    

问题：随着模型越来越大，顺序敏感性问题会自动消失吗？

结论：研究分析了 Llama-2 (7B-70B) 和 Qwen2 系列模型，发现随着参数量的增加，模型对顺序的敏感性确实有所下降（Sensitivity Decreases），但并未完全消失。特别是在 Many-shot 场景下，大规模模型依然表现出对上下文末尾示例的过度关注。

3.3 指令格式化与符号微调 (Formatting & Tuning)
Symbol Tuning Improves In-Context Learning in Language Models (2023/2024)    

问题：模型在 ICL 中往往依赖预训练中的语义先验（Semantic Priors）（如看到“积极”一词就倾向于分类为正面），而非真正学习上下文中的输入-输出映射规则。这导致模型难以适应反直觉的任务（如将“好”定义为负类）。

方法：Wei 等人（2023）提出了“符号微调”（Symbol Tuning）技术。在微调阶段，将任务的自然语言标签（如“Positive/Negative”）替换为无语义的任意符号（如“Foo/Bar”），强制模型必须通过分析上下文中的示例关系来推断任务规则，而非依赖标签的语义。

结论：符号微调显著提升了模型在未见任务上的 ICL 能力，尤其是在算法推理和需要覆盖先验知识的“翻转标签”任务中。这表明通过特定的微调策略，可以“解锁”模型更深层的抽象类比能力，使其更关注结构而非语义表面。

4. 实验评价与领域应用
4.1 多模态 ICL：挑战与突破
随着 GPT-4V 和 Gemini 的发布，ICL 被扩展到了视觉-语言领域（VL-ICL）。

VL-ICL Bench: The Devil in the Details (ICLR 2025)    

问题：现有的多模态 ICL 研究主要集中在简单的图像描述或 VQA 上，缺乏对复杂推理和长上下文视觉任务的系统评测。

方法：Zong 等人（2025）构建了 VL-ICL Bench，这是一个涵盖感知、推理和长上下文理解的综合基准。

结论：评测发现，即使是 SOTA 模型（如 GPT-4V），在处理多图像上下文时也面临巨大挑战。简单的图像堆叠（Image Stacking）往往导致信息丢失。此外，视觉模态的 ICL 效率远低于文本模态，模型很难从视觉示例中提取细粒度的风格或逻辑规则。

M²IV: Representation Engineering for VL-ICL (2025)    

方法：为了解决上述问题，研究者提出了 M²IV 方法。该方法不直接输入原始图像 Token，而是通过表征工程（Representation Engineering）提取图像的关键语义向量，并将其注入到语言模型的上下文中。

结论：M²IV 在多个基准上超越了传统的 16-shot ICL，证明了在多模态场景下，压缩和抽象视觉信息比单纯增加示例数量更有效。

4.2 低资源语言与 ICL
It’s All About In-Context Learning! (EMNLP 2025)    

问题：对于训练数据中极少见的语言（Extremely Low-Resource Languages），LLM 通常表现不佳。

结论：Li 等人（2025）的研究得出了一个反直觉的结论：对于这些语言，参数高效微调（PEFT）往往不如 ICL 有效。特别是“语言对齐后的 Zero-shot ICL”表现最佳。这意味着，与其在极少的数据上强行微调参数，不如通过对齐预训练让模型理解该语言的结构，然后利用其强大的通用 ICL 能力进行推理。

4.3 共性实验结论总结
综合 2022-2025 年的实证研究 ，我们可以总结出以下关键结论：   

维度	关键发现与趋势
规模效应	模型参数量与 ICL 能力呈强正相关。小模型（<10B）难以涌现 ICL，但符号微调可改善此情况。
不确定性	
增加示例数量（Many-shot）能提升准确率，但不一定降低不确定性。在长上下文中，模型可能对错误答案盲目自信 。

标签作用	在分类任务中，标签空间（Label Space）的分布比标签的正确性更重要；但在推理任务中，中间步骤的正确性至关重要。
长上下文	随着上下文长度增加，ICL 性能呈现“先升后降”趋势。中间部分的示例容易被忽略（Lost in the Middle），需要特殊的检索或注意力机制优化。
  
5. 趋势与挑战：面向 2025 年后的展望
尽管 ICL 已成为主流范式，但其在效率、鲁棒性和泛化边界上仍面临严峻挑战。基于  等前沿工作，我们预测如下趋势。   

5.1 核心挑战
推理成本与 KV Cache：随着 Many-shot ICL（数千个示例）的普及，推理成本呈线性甚至二次方增长。如何高效管理 Key-Value Cache 成为工程瓶颈。

鲁棒性与安全性：恶意攻击者可以通过在示例中注入对抗样本（Jailbreaking Demonstrations）来绕过模型的安全对齐。ICL 的无参数更新特性使得防御这种攻击变得极其困难 。   

视觉 ICL 的鸿沟：视觉信息的语境化效率远低于文本，如何让模型像理解文本一样理解“图像序列”的逻辑关系，是多模态 ICL 的最大痛点。

5.2 未来演进趋势 (2025–)
趋势一：进化提示 (Evolutionary Prompting) 取代人工工程

PromptQuine (2025)  的研究展示了一个令人深思的现象：通过进化算法自动修剪和变异出的提示，虽然在人类看来可能像是一串“乱码”（Gibberish），但在模型内部却能触发极高的响应效率。这预示着未来的提示工程将不再依赖人类的语言直觉，而是转向基于梯度的、自动化的离散搜索，寻找模型内部真正的“神经触发器”。   

趋势二：ICL 与权重学习的融合 (The Convergence of Context and Weights)

贝叶斯标度律  暗示了 ICL 和微调在数学本质上的统一。未来可能出现混合架构，允许模型在推理时动态地将上下文信息“编译”为临时的权重更新（如利用 Hypernetworks 生成临时的 LoRA 模块），从而结合 ICL 的灵活性和微调的高效性。   

趋势三：从静态 ICL 到代理 ICL (Agentic ICL)

随着环境变得动态化，ICL 将不再局限于静态的问答，而是扩展到代理（Agent）领域。模型需要通过观察长视频流或交互式环境的反馈，实时地在上下文中“学习”物理规律和操作逻辑 。这要求 ICL 具备更强的长时间跨度记忆和错误修正能力。   

6. 结论
2022 年至 2025 年是语境学习从“神秘的涌现现象”走向“可控的工程范式”的关键时期。 在理论层面，我们利用贝叶斯推断框架和归纳头机制，初步打破了 ICL 的黑盒，证明了其本质是对预训练先验的高效激活与组合。 在方法层面，MoD 和 IDS 等技术解决了“海量数据中选什么”的难题，而 InvICL 和 符号微调 则攻克了“如何排序”和“如何克服先验”的顽疾，显著提升了 ICL 的鲁棒性。 然而，随着上下文窗口的无限扩展，ICL 正面临着效率与可靠性的双重博弈。未来的研究将不再局限于让模型简单地“看”更多的例子，而是致力于探索更本质的上下文压缩、自动化提示进化以及跨模态知识迁移机制。ICL 终将不仅仅是一种“技巧”，而是通向通用人工智能（AGI）的一块基石。

参考文献
Dong, Q., et al. (2024). A Survey on In-context Learning. Proceedings of EMNLP 2024.    

Mao, H., et al. (2025). A Survey to Recent Progress Towards Understanding In-Context Learning. arXiv preprint.    

Wang, S., et al. (2024). Mixture of Demonstrations for In-Context Learning. NeurIPS 2024.    

Qin, C., et al. (2024). In-Context Learning with Iterative Demonstration Selection. Findings of EMNLP 2024.    

Fang, L., et al. (2025). Rethinking Invariance in In-context Learning. ICLR 2025.    

Todd, E., et al. (2024). Function Vectors in Large Language Models. ICLR 2024.    

Saanum, T., et al. (2025). Not All Induction Heads Are Created Equal. CCNeuro 2025.    

Wei, J., et al. (2023). Symbol Tuning Improves In-Context Learning in Language Models. EMNLP 2023.    

Liu, H., et al. (2025). Unraveling the Mechanics of Learning-Based Demonstration Selection for In-Context Learning. ACL 2025.    

Zong, Y., et al. (2025). VL-ICL Bench: The Devil in the Details of Benchmarking Multimodal In-Context Learning. ICLR 2025.    

Li, Y., et al. (2025). It’s All About In-Context Learning! Teaching Extremely Low-Resource Languages to LLMs. EMNLP 2025.    

Wang, Y., et al. (2025). Uncertainty Unveiled: Can Exposure to More In-context Examples Mitigate Uncertainty for Large Language Models? arXiv preprint.    

Jeong, S., et al. (2024). Bayesian Scaling Laws for In-Context Learning. arXiv preprint.    

Yang, C., et al. (2024). An In-Context Learning Theoretic Analysis of Chain-of-Thought. ICML 2024 Workshop.    

Chen, Z., et al. (2025). PromptQuine: Evolutionary Prompt Search. arXiv preprint.    


aclanthology.org
A Survey on In-context Learning - ACL Anthology
在新窗口中打开

arxiv.org
[2301.00234] A Survey on In-context Learning - arXiv
在新窗口中打开

arxiv.org
Bayesian scaling laws for in-context learning - arXiv
在新窗口中打开

arxiv.org
Bayesian scaling laws for in-context learning - arXiv
在新窗口中打开

openreview.net
An In-Context Learning Theoretic Analysis of Chain-of-Thought - OpenReview
在新窗口中打开

arxiv.org
Function Vectors in Large Language Models - arXiv
在新窗口中打开

openreview.net
Function Vectors in Large Language Models - OpenReview
在新窗口中打开

2025.ccneuro.org
Not all induction heads are created equal
在新窗口中打开

arxiv.org
On the Emergence of Induction Heads for In-Context Learning - arXiv
在新窗口中打开

arxiv.org
A Survey to Recent Progress Towards Understanding In-Context Learning - arXiv
在新窗口中打开

arxiv.org
[2402.02212] A Survey to Recent Progress Towards Understanding In-Context Learning
在新窗口中打开

proceedings.neurips.cc
Mixture of Demonstrations for In-Context Learning - NIPS papers
在新窗口中打开

aclanthology.org
In-Context Learning with Iterative Demonstration Selection - ACL Anthology
在新窗口中打开

arxiv.org
In-Context Learning with Iterative Demonstration Selection - arXiv
在新窗口中打开

openreview.net
In-Context Learning with Iterative Demonstration Selection - OpenReview
在新窗口中打开

aclanthology.org
Unraveling the Mechanics of Learning-Based Demonstration Selection for In-Context Learning - ACL Anthology
在新窗口中打开

aclanthology.org
Selecting Demonstrations for Many-Shot In-Context Learning via Gradient Matching - ACL Anthology
在新窗口中打开

openreview.net
RETHINKING INVARIANCE IN IN-CONTEXT LEARNING - OpenReview
在新窗口中打开

arxiv.org
Rethinking Invariance in In-context Learning - arXiv
在新窗口中打开

openreview.net
EVALUATING AND EXPLAINING PROMPT SENSITIVITY OF LLMS USING INTERACTIONS - OpenReview
在新窗口中打开

researchgate.net
Symbol tuning improves in-context learning in language models | Request PDF
在新窗口中打开

arxiv.org
symbol tuning improves in-context learning - arXiv
在新窗口中打开

research.google
Symbol tuning improves in-context learning in language models - Google Research
在新窗口中打开

openreview.net
VL-ICL Bench: The Devil in the Details of Multimodal In-Context Learning | OpenReview
在新窗口中打开

github.com
[ICLR 2025] VL-ICL Bench: The Devil in the Details of Multimodal In-Context Learning - GitHub
在新窗口中打开

arxiv.org
M²IV: Towards Efficient and Fine-grained Multimodal In-Context Learning via Representation Engineering - arXiv
在新窗口中打开

openreview.net
M²IV: Towards Efficient and Fine-grained Multimodal In-Context Learning via Representation Engineering | OpenReview
在新窗口中打开

aclanthology.org
It's All About In-Context Learning! Teaching Extremely Low-Resource Languages to LLMs
在新窗口中打开

ijournalse.org
A New Approach to Development of Students' Research Abilities in STEM Education - Emerging Science Journal
在新窗口中打开

arxiv.org
Cross-Modal Safety Mechanism Transfer in Large Vision-Language Models - arXiv
在新窗口中打开

arxiv.org
Can Exposure to More In-context Examples Mitigate Uncertainty for Large Language Models? - arXiv
在新窗口中打开

researchgate.net
Can Exposure to More In-context Examples Mitigate Uncertainty for Large Language Models? - ResearchGate
在新窗口中打开

arxiv.org
[2506.17930] Evolving Prompts In-Context: An Open-ended, Self-replicating Perspective
在新窗口中打开

arxiv.org
LoCoBench: A Benchmark for Long-Context Large Language Models in Complex Software Engineering - arXiv
在新窗口中打开

arxiv.org
LMAct: A Benchmark for In-Context Imitation Learning with Long Multimodal Demonstrations