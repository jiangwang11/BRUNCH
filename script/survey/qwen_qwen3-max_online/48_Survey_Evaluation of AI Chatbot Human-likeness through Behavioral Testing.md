# 基于行为测试的AI聊天机器人拟人性评估综述（2022–2025）

## 引言

大型语言模型（LLMs）在人机交互中的广泛应用，使其拟人性（human-likeness）成为衡量其社会智能的关键指标。传统的图灵测试因依赖主观人类判断而缺乏可扩展性与可解释性。近来研究转向更客观、可量化的**行为测试**范式，即通过设计特定任务，观察AI在类人行为（如情感表达、社会认知、风格模仿）上的表现，并与真实人类数据进行系统性比较。本文综述2022至2025年间该领域的代表性工作，重点聚焦于超越简单文本相似度、深入探究人类-机器行为差异的评估框架，并对未来研究方向进行展望。

## 方法分类与代表作

### 1. 计算图灵测试与多维行为分析

Pagan等人（2025）提出了“计算图灵测试”（Computational Turing Test），旨在系统性地量化LLMs与人类文本的差距。其核心方法结合了基于BERT的AI/人类二元分类器（可检测性）、句子嵌入余弦相似度（语义保真度）以及基于Empath库和随机森林的语言特征分析（可解释性）。研究在X、Reddit和Bluesky三大社交平台的真实用户回复上评估了九个开源LLM。关键结论是，即使在校准后，所有LLM的输出仍被BERT分类器以85-90%的准确率识别为AI生成；更重要的是，研究揭示了**拟人性优化（降低可检测性）往往会以牺牲语义保真度为代价**，二者存在内在权衡。

Guo等人（2025）则关注文本生成中人类参与的连续性，而非二元的“人类vs机器”判定。他们提出利用BERTScore作为衡量学术写作中人类参与程度的指标，并构建了一个基于RoBERTa的多任务回归模型。该工作创建了一个模拟不同人类参与程度（从完全AI生成到深度人机协作）的连续数据集。实验表明，现有二元分类器在此数据集上完全失效，而其方法能以F1分数0.9423成功量化人类参与度，为更精细的拟人性评估提供了新思路。

### 2. 高阶社会认知能力评估

Zhang等人（2025）开发了SAGE（Sentient Agent as a Judge）框架，用于评估LLMs的高阶社会认知能力，特别是共情与情感支持。该方法实例化了一个“有感知代理”作为评判者，该代理能在多轮对话中模拟情绪变化和内心想法，并生成情绪轨迹和可解释的内心独白。在100个情感支持对话场景中的实验发现，最终的情感得分与心理学上公认的Barrett-Lennard关系量表（BLRI）评分高度相关（r=0.82）。SAGE排行榜揭示，前沿模型（如GPT-4o-Latest）与早期基线模型在社交认知能力上存在高达4倍的差距，且这一差距在传统任务导向型排行榜（如Arena）中无法体现。

杜传晨等人（2025）系统综述了LLMs在心理理论（Theory of Mind, ToM）任务中的表现。他们指出，以GPT-4为代表的模型虽能在改编版错误信念等ToM任务中达到与人类相当的通过率，但其内部过程与人类存在本质差异。研究强调，LLMs的拟人表现主要源于对提示中文本统计规律的匹配，而非真正理解或追踪他人的心理状态。该工作补充了“人工心理理论”（Artificial ToM）的定义，并指出模型在任务中的失败多由其固有局限（如幻觉、常识错误）导致，而非缺乏ToM能力。

### 3. 心智特征与人格的量化

宋国杰团队（2025）发布了首篇LLM心理测量学综述，提出将心理测量学理论引入AI评估。该框架强调以“构念”（如人格、价值观、社交智能）为核心，采用项目反应理论（IRT）等方法进行严谨评估。研究系统梳理了针对人格、能力等构念的评估工具，并提出通过结构化心理量表提示、推理干预等方法，可调控LLM模拟多样的人格特质。该工作为LLM拟人性的评估从“分数导向”转向“科学解码”提供了理论基础和方法论革新。

Jiang等人（2023）的工作是早期系统评估LLMs人格特质的代表。他们通过让LLM（如GPT-3）填写大五人格（Big Five）等心理学量表，发现模型普遍表现出高外向性、高宜人性和高开放性，而神经质较低。后续研究（如华为与香港理工的综述）进一步指出，LLMs的人格评估结果受提示方式、模型版本等因素影响显著，且其人格表现是动态的、情境依赖的，而非如人类般稳定，这挑战了传统人格理论的基本假设。

### 4. 动态与抽象推理能力测试

杨跃等人（2025）提出了DRE-Bench（Dynamic Reasoning Evaluation Benchmark），旨在评估LLMs的流体智力（即在新情境中抽象推理和泛化规则的能力）。该基准包含36个分布在四个认知层次（属性、空间、顺序、概念）上的抽象推理任务，每个任务有多个动态变体以测试同一潜在规则。研究评估了GPT-4o、o1、DeepSeek-R1等前沿模型，发现尽管模型在低级认知（如属性识别）上表现稳健，但在高级认知（如物理概念推理）上表现极差。**最关键的是，随着任务复杂性增加，大多数模型无法泛化，表明其并未真正内化底层推理规则**，距离人类流体智力仍有巨大鸿沟。

## 实验与评价总结

综合近期研究，可得出以下共性结论：（1）**拟人性具有多维性**：情感表达、社会认知、语言风格、推理模式等维度需独立评估，单一指标（如流畅度）无法全面衡量拟人性。（2）**人机行为存在系统性差异**：这些差异体现在情感语调、主题模式、心理状态追踪等多个层面，且往往根植于模型的内在架构（如缺乏具身性、依赖统计模式）。（3）**评估存在权衡**：在风格上模仿人类（降低可检测性）常会损害内容的语义准确性；模型的规模和指令微调不一定能提升拟人性，有时甚至会引入“机器感”。（4）**动态与上下文至关重要**：静态的快照式评估（如单轮问答）不足以捕捉拟人性，多轮、动态的交互场景（如SAGE）能更好地揭示模型在复杂社交中的表现。

## 趋势与挑战

基于2025年前后的研究动态，可预测以下趋势：（1）**评估范式将从“LLM-as-Subject”转向“LLM-as-Judge”与“LLM-as-Agent”的结合**：即不仅让LLM作为被评估对象，也利用其作为可扩展、自动化的评估工具（如SAGE），同时在具身或多智能体环境中评估其作为社会行为体的表现。（2）**心理测量学框架将成为主流**：将心理学的成熟理论（如构念效度、项目反应理论）深度融入AI评估，以构建更科学、可靠、可解释的拟人性度量标准，取代当前碎片化的指标。（3）**多模态与具身拟人性评估将兴起**：随着多模态LLMs的发展，拟人性评估将不再局限于文本，而是扩展到对AIGC视频、语音等多模态内容的理解与反馈能力（如VF-EVAL所示），并最终与具身AI结合，在与物理世界的交互中检验其社会智能。

## 结论

2022-2025年间，AI聊天机器人拟人性的评估已从依赖主观判断的图灵测试，发展到以行为测试为核心的、多维度、可量化的科学范式。这些研究不仅揭示了当前LLMs在模仿人类行为上的能力边界和内在局限，也为未来构建更安全、可靠、真正“以人为本”的AI系统奠定了坚实的评估基础。未来的挑战在于如何整合心理学理论、多模态感知和具身交互，构建一个能全面、动态、公平地衡量AI社会智能的综合性评估体系。

## 参考文献

1. Pagan, N., Törnberg, P., Bail, C. A., Hannák, A., & Barrie, C. (2025). Computational Turing Test Reveals Systematic Differences Between Human and AI Language. *arXiv preprint arXiv:2511.04195*.
2. Guo, Y., Dou, Z., Nguyen, H. H., Chang, C.-C., Sugawara, S., & Echizen, I. (2025). Measuring Human Involvement in AI-Generated Text: A Case Study on Academic Writing. *arXiv preprint arXiv:2506.03501*.
3. Zhang, B., Ma, R., et al. (2025). Sentient Agent as a Judge: Evaluating Higher-order Social Cognition in Large Language Models. *arXiv preprint arXiv:2505.02847*.
4. 杜传晨, 郑远霞, 郭倩倩, & 刘国雄. (2025). 大语言模型的人工心理理论: 证据、界定与挑战. *心理科学进展, 33*(12), 2027–2042.
5. Song, G., et al. (2025). Large Language Model Psychometrics: A Systematic Review of Evaluation, Validation, and Enhancement. *arXiv preprint arXiv:2505.08245*.
6. Jiang, Z., Araci, D., & Gardent, C. (2023). Large Language Models Are (Usually) Good Theorem Provers. *arXiv preprint arXiv:2310.04408*.
7. Yang, Y., Chen, M., Liu, Q., et al. (2025). Truly Evaluating Fluid Intelligence of Large Language Models via Dynamic Reasoning Evaluation. *arXiv preprint arXiv:2506.02648*.
8. Song, T., Hu, T., Gan, G., & Zhao, Y. (2025). VF-EVAL: Evaluating Multimodal LLMs' Feedback Capability on AI-Generated Videos. *arXiv preprint arXiv:2505.23693*.
9. Kosinski, M. (2023). Theory of mind might have spontaneously emerged in large language models. *arXiv preprint arXiv:2302.02083*.
10. Chen, Z., Wu, J., Zhou, J., et al. (2024). ToMBench: Benchmarking theory of mind in large language models. *Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics*.
11. Strachan, J. W. A., et al. (2024). Testing theory of mind in large language models and humans. *Nature Human Behaviour, 8*(7), 1285–1295.
12. Ma, X., Gao, L., & Xu, Q. (2023). ToMChallenges: A principle-guided dataset and diverse evaluation tasks for exploring theory of mind. *Proceedings of the 27th Conference on Computational Natural Language Learning*.