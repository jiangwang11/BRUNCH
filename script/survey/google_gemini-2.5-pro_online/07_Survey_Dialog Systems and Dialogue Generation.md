好的，作为一名严谨的科研助手，我将基于提供的真实网络搜索结果，为您撰写一篇关于“对话系统与生成技术（2022-2025）”的学术综述。

***

### **基于大型语言模型的对话系统与生成技术研究综述 (2022–2025)**

#### **1. 引言**

对话系统，旨在通过自然语言与人类进行交互，是人工智能领域的长期目标之一。近年来，随着大型语言模型（Large Language Models, LLMs）的兴起，该领域经历了革命性的范式转移 [www.zhuanzhi.ai](https://www.zhuanzhi.ai/vip/1bd55bf4f470a39b15fdec7182e69b1f)。传统的基于规则或独立模块（如NLU, DST, NLG）的系统正迅速被端到端的、由LLM驱动的架构所取代，这些新架构展现出前所未有的语言理解与生成能力 [pdf.hanspub.org](https://pdf.hanspub.org/airr2025141_192610518.pdf)。2022至2025年间，研究焦点从提升基础语言能力转向如何使对话系统更具知识性、策略性、情感共鸣和个性化。本文旨在系统梳理此期间LLM在对话系统中的关键进展，重点剖析其核心方法、评估范式，并展望未来的研究趋势与挑战。

#### **2. 方法分类与代表作**

基于LLM的对话系统研究逐渐模糊了开放域对话（ODD）与任务导向对话（TOD）的界限，并催生了以增强模型特定能力为导向的新研究范式。

##### **2.1 认知与情感增强对话**

该方向致力于通过建模更深层次的认知因素（如情感、价值观、个性），使对话系统超越简单的信息传递，实现更富有人性化的情感共鸣。

*   **《人机价值观驱动的对话情绪生成模型》（Ma et al., 2025）**
    该研究解决了现有情感对话模型忽视用户与系统间“价值观对齐”（Value Alignment）的问题，这种忽视导致生成情绪与用户期望不符，降低了情感共鸣 [aclanthology.org](https://aclanthology.org/2025.ccl-1.47.pdf)。研究者提出了人机价值观驱动的对话情绪生成模型（HVDEGM），其核心是通过一个多阶段门控机制，动态融合用户在对话中体现的价值观特征与系统的历史价值观。在新建的价值观对话数据集ValueCon上，HVDEGM在精确率、召回率等指标上实现了提升，尤其在专门衡量情感共鸣的指标R3上提升了4.1%，验证了价值观对齐对于增强对话共鸣度的有效性。

*   **《通过敏感情绪识别与合理知识选择的共情对话生成》（SEEK, 2022）**
    这篇工作针对共情对话生成中情感状态被视为静态变量，以及外部知识与情感表达易产生冲突的核心痛点 [blog.csdn.net](https://blog.csdn.net/qq_42393368/article/details/127951656)。SEEK模型采用语句级（utterance-level）编码以捕捉对话过程中情感的动态变化，并设计了情感-知识双向交互框架。该框架利用预训练模型COMET生成情感相关的知识，并通过专门的子任务（如情感意图预测）进行优化。人工A/B测试结果显示，SEEK在连贯性、共情性和流畅性上均优于基线模型，证明了动态建模情感并协调知识互动能显著提升生成质量。

*   **《用于对话式智能辅导系统的个性化学生模拟》（Liu et al., 2024）**
    该研究关注于在训练和评估智能辅导系统（ITS）时，如何有效刻画和模拟具有不同个性的学生，这是一个重要的挑战 [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/77199)。研究者提出了一个框架，通过整合认知与非认知特征来构建学生档案，并利用LLM进行个性化的学生行为模拟。实验证明，先进的LLM能够根据预设的语言能力和个性特征生成多样化且一致的学生回应。这不仅验证了LLM模拟复杂人类角色的能力，也为开发具备自适应教学策略的对话式ITS提供了高质量的模拟环境。

##### **2.2 策略与任务导向对话**

在LLM时代，任务导向对话不再局限于僵化的流程，而是通过学习和执行复杂的策略来实现更灵活、高效的目标达成。

*   **《评估、合成和增强客户支持对话》（Zhu et al., 2025）**
    该研究指出，有效的客户支持对话不仅需要解决问题，还必须遵循专业沟通策略，但现有数据集普遍缺乏此种战略指导 [huggingface.ac.cn](https://huggingface.ac.cn/papers/2508.04423)。为解决此问题，论文提出了一个包含5个对话阶段和12种策略的客户支持对话（CSC）框架，并构建了高质量的训练数据集RoleCS与评估数据集CSConv，两者均通过LLM驱动的角色扮演和重写生成。实验表明，在RoleCS上微调的LLM在CSConv上的表现显著提升，人工评估进一步证实了其问题解决能力的改善，凸显了显式策略建模对提升专业领域对话质量的重要性。

##### **2.3 上下文工程与检索增强生成（RAG）**

为了克服LLM固有的知识局限性与“幻觉”问题，研究界将重点放在如何优化模型推理时所依赖的上下文信息上，这一领域被系统性地定义为“上下文工程”（Context Engineering） [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/1a3763b7-6e29-4e77-ad27-5a1337b23b24)。

*   **检索增强生成（RAG）**
    作为上下文工程中最具代表性的实现，RAG已成为提升对话系统事实性和时效性的关键技术 [pdf.hanspub.org](https://pdf.hanspub.org/airr2025141_192610518.pdf)。其核心机制是：在生成回应前，系统首先根据当前对话上下文从外部知识库（如维基百科、企业文档）中检索相关信息。随后，LLM将这些检索到的信息作为上下文的一部分，共同生成最终答复。这种“检索-生成”的两阶段范式极大地减少了模型捏造事实（幻觉）的现象，并使其能够回答关于最新事件的问题，有效扩展了模型的知识边界。

#### **3. 实验与评价总结**

*   **数据集构建的新范式**：研究者不再满足于通用对话语料，而是转向构建面向特定能力的高质量、精细标注的数据集。例如，`ValueCon`专注于价值观对齐的评估 [aclanthology.org](https://aclanthology.org/2025.ccl-1.47.pdf)，而`CSConv`则用于衡量策略执行能力 [huggingface.ac.cn](https://huggingface.ac.cn/papers/2508.04423)。此外，利用LLM进行数据合成（如`RoleCS`）或重写，已成为一种高效生成大规模、高质量训练数据的标准做法。

*   **评估指标的演进**：传统基于n-gram重叠度的自动评估指标（如BLEU, ROUGE）在LLM时代已暴露出明显不足，它们无法有效衡量语义一致性、逻辑性和创造性 [pdf.hanspub.org](https://pdf.hanspub.org/airr2025141_192610518.pdf)。为此，研究开始探索更具针对性的自动指标，如用于度量情感共鸣的R3指标。同时，**人工评估**（如A/B测试、李克特量表）仍然是评估共情、连贯性等高级质量的黄金标准。一个新兴趋势是利用更强大的LLM（如GPT-4）作为评估器，其评判结果与人类判断的相关性显著高于传统指标。

#### **4. 趋势与挑战**

1.  **从提示工程到系统的上下文工程**：研究正从设计孤立的提示词（Prompt Engineering）转向一个更系统的“上下文工程”（Context Engineering）框架 [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/1a3763b7-6e29-4e77-ad27-5a1337b24)。这包括检索增强生成（RAG）、记忆系统和工具集成（Tool Use），使对话系统能访问实时数据、执行代码或调用外部API。这标志着对话系统正从“封闭世界的语言模型”进化为“与数字世界交互的智能体”。

2.  **多模态对话的兴起与统一**：对话本质上是多模态的。随着GPT-4o等模型的出现，能够理解并生成文本、图像、音频等多模态内容的统一对话模型成为明确的研究热点 [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/134378)。核心挑战在于如何弥合不同模态在模型架构上的差异（如用于理解的自回归模型与用于图像生成的扩散模型），以实现无缝的跨模态理解与生成。

3.  **基于智能体的模拟与交互范式**：LLM正被广泛用作能够模拟复杂人类行为的“智能体”（Agents） [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/67467)。这一范式在对话系统中有两大应用：一是通过角色扮演（如`RoleCS`）高效生成专业领域的高质量训练数据 [huggingface.ac.cn](https://huggingface.ac.cn/papers/2508.04423)；二是通过模拟（如个性化学生模拟）来评估和优化对话系统的策略与适应性 [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/77199)。这推动了从单轮响应生成向模拟复杂社会交互的转变。

*   **核心挑战**：尽管进展显著，但领域仍面临严峻挑战。**“理解-生成能力不对称”** 问题尤为突出：模型借助上下文工程能理解极为复杂的输入，但在生成同等复杂度、长篇且连贯的输出方面仍显不足 [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/1a3763b7-6e29-4e77-ad27-5a1337b24)。此外，**事实性与幻觉**、灾难性遗忘以及生成内容的可控性与安全性问题，依然是所有基于LLM的对话系统需要持续攻克的难关 [pdf.hanspub.org](https://pdf.hanspub.org/airr2025141_192610518.pdf)。

#### **5. 结论**

在2022至2025年间，基于大型语言模型的对话系统研究取得了飞跃式发展。研究重点已成功从提升基础生成流畅度，转向通过上下文工程、认知情感建模和策略化交互来构建更智能、更可靠、更具人性化的对话伙伴。未来的研究将持续深化智能体交互、多模态融合，并致力于解决事实性、可控性及理解-生成能力不对称等根本性挑战，推动对话系统迈向更高级的人工智能形态。

#### **6. 参考文献**

1.  [huggingface.ac.cn](https://huggingface.ac.cn/papers/2508.04423) Zhu, J., Dou, H., Li, J., Guo, L., Chen, F., Zhang, C., & Kong, F. (2025). *Evaluating, Synthesizing, and Enhancing Customer Support Conversations*.
2.  [aclanthology.org](https://aclanthology.org/2025.ccl-1.47.pdf) Ma, Z., Ye, H., Liu, J., & Lü, K. (2025). *Human-Machine Values-Driven Dialogue Emotion Generation Model*.
3.  [blog.csdn.net](https://blog.csdn.net/qq_42393368/article/details/127951656) (Unofficial review of) Li, J., et al. (2022). *Empathetic Dialogue Generation via Sensitive Emotion Recognition and Sensible Knowledge Selection*. EMNLP.
4.  [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/77199) Liu, Z., Yin, S. X., Lin, G., & Chen, N. F. (2024). *Personality-aware Student Simulation for Conversational Intelligent Tutoring Systems*. EMNLP.
5.  [www.zhuanzhi.ai](https://www.zhuanzhi.ai/vip/1bd55bf4f470a39b15fdec7182e69b1f) (Survey) B. Li, et al. (2024). *A Survey on Recent Advances in LLM-Based Multi-turn Dialogue Systems*.
6.  [pdf.hanspub.org](https://pdf.hanspub.org/airr2025141_192610518.pdf) (Survey) Liu, J., & Du, Y. (2025). *A Review of Text Generation Based on Large Language Model*.
7.  [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/1a3763b7-6e29-4e77-ad27-5a1337b24) (Survey) Mei, L., et al. (2025). *A Survey of Context Engineering for Large Language Models*.
8.  [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/134378) (Survey) Zhang, X., et al. (2025). *Unified Multimodal Understanding and Generation Models: Advances, Challenges, and Opportunities*.
9.  [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/67467) Ji, J., et al. (2024). *Dynamic and Textual Graph Generation Via Large-Scale LLM-based Agent Simulation*.
10. [github.com](https://github.com/xiaoyuexing/StarrySky) (Repository) xiaoyuexing. *StarrySky: A collection of over a thousand projects, including machine learning, deep learning, NLP, GNN, etc.*
11. [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/134378) (Reference within survey) GPT-4o, OpenAI.
12. [www.zhuanzhi.ai](https://www.zhuanzhi.ai/vip/1bd55bf4f470a39b15fdec7182e69b1f) (Reference within survey) Lewis, M., et al. (2020). *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*.