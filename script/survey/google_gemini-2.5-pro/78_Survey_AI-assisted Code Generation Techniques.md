好的，作为一名严谨的科研助手，我将基于提供的真实网络搜索结果，为您生成一篇关于“AI辅助代码生成技术”的学术综述。

***

### **面向软件工程的AI辅助代码生成技术研究综述 (2022–2025)**

#### **引言**

近年来，以大语言模型（Large Language Models, LLMs）为代表的人工智能技术在软件工程领域取得了革命性进展，尤其是在代码生成（Code Generation）任务中。早期的模型主要集中于函数级的代码补全或根据自然语言描述生成简短代码片段，但随着模型规模与能力的指数级增长，研究焦点已转向更复杂的任务，例如仓库级的代码理解与生成、自动化程序修复（Automated Program Repair, APR）、以及满足个性化编码风格的需求。这些进步旨在将AI从一个“代码提示工具”转变为能够深度参与软件开发全生命周期的“智能编程伙伴”。本综述旨在系统梳理2022至2025年间AI辅助代码生成领域的关键技术与代表性工作，总结其评价体系，并展望未来的核心挑战与研究趋势。

#### **方法分类与代表作**

##### 1. 基于代码结构与多模态信息的预训练

该类方法认为代码不仅是文本序列，更包含了丰富的结构（如抽象语法树AST）和多模态信息（如注释），通过在预训练阶段融合这些信息来构建更精确的代码表示。

-   **UniXcoder** (Guo 等, 2022) [www.zhuanzhi.ai](https://www.zhuanzhi.ai/paper/783c50562dd63fa4487c8e75872111a3): 该研究旨在创建一个能同时支持代码理解与生成任务的统一预训练模型。UniXcoder利用带有前缀适配器的掩码注意力矩阵来控制模型行为，并融合了AST和代码注释等跨模态内容。其创新性地提出一种将树状的AST并行转换为序列结构的方法，保留了完整的结构信息。实验证明，在多项代码相关任务中，融合AST和注释信息能显著增强代码表示能力，使其在当时达到最优水平。

-   **语法和语义结合的代码补全方法** (付善庆 等, 2022) [jos.org.cn](https://jos.org.cn/html/2022/11/6324.htm): 此项工作解决了传统基于AST的方法在序列化后可能丢失结构信息，以及循环网络在处理长序列时依赖不足的问题。研究者提出将程序的语法特征（基于AST）与语义特征（基于控制依赖关系）相结合，并采用时间卷积网络（TCN）与LSTM结合的架构（TCN-LSTM）。该方法将代码补全视为AST节点预测问题，利用TCN捕捉长距离依赖。实验结果表明，在Python数据集上，该方法相较于基线模型将预测准确率提升了约2.8%，验证了语义信息融合的有效性。

##### 2. 基于检索增强的生成 (Retrieval-Augmented Generation, RAG)

为解决LLMs在面对领域外（Out-of-Distribution, OOD）问题或需要项目特定知识时性能下降的问题，RAG通过从外部知识库中检索相关代码片段来增强上下文，从而指导模型生成更准确、更具情境感知能力的代码。

-   **Retrieval-Augmented Code Generation: A Survey** (Tao 等, 2025) [zhuanzhi.ai](https://zhuanzhi.ai/paper/f49cff257ef0cbf5e546373a59f6f8da): 这篇综述系统性地回顾了检索增强代码生成（RACG）领域，并特别关注了极具挑战性的仓库级代码生成（RLCG）。论文指出，RAG是解决代码生成中长距离依赖、全局一致性和上下文感知问题的有效范式。它从生成策略、检索模态、模型架构等多个维度对现有工作进行了分类，并总结了常用数据集与评测协议。该综述为理解RACG的现状和未来发展提供了统一的分析框架。

-   **ReCode** (Zhao 等, 2025) [blog.csdn.net](https://blog.csdn.net/zhangjiaoshou_/article/details/151150533): 该研究针对LLM在代码修复任务中成本高、对OOD缺陷适应性差的痛点。ReCode框架提出了一种创新的细粒度RAG方法，包含“算法感知检索”（先用LLM预测代码的算法类型以缩小检索范围）和“双视图编码”（使用不同编码器分别处理自然语言描述和代码结构）。同时，研究者构建了基于真实提交记录的代码修复基准RACodeBench。实验表明，ReCode不仅显著提升了修复准确率（如在AtCoder上达到35%的通过率仅需4次LLM调用），还将推理成本降低了3-4倍。

##### 3. 模型协同与动态引导

此类方法不再依赖单一模型，而是通过多个模型协同工作或动态引导模型在不同推理路径（如代码执行与文本推理）间切换，以兼顾效率与效果。

-   **基于不确定性估计的微调模型与大语言模型的协同方法** (洪少东 等, 2025) [www.arocmag.cn](https://www.arocmag.cn/abs/2025.04.0082): 该研究旨在解决微调模型（在特定任务上表现好但泛化能力弱）与通用LLM（泛化能力强但特定任务上非最优）之间的协同问题。研究者提出Coral方法，通过不确定性估计来量化两者的决策边界。当微调模型对其生成结果的不确定性较高时（识别为OOD数据），任务便切换至LLM处理。实验证明，该协同方法在基准数据集上的BLEU和Exact Match得分均优于单独使用任一模型，实现了有效的优势互补。

-   **Steering Large Language Models between Code Execution and Textual Reasoning** (Chen 等, 2025) [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/112968): 该工作探讨了LLM在解决问题时应选择纯文本推理还是生成代码并执行的决策问题。研究发现，现有方法无法在所有场景下做出最优选择，甚至存在“反向缩放行为”（模型越大，选择越差）。为此，作者提出了三种引导LLM进行代码/文本生成决策的方法，并取得了显著改善。这项研究强调了对LLM推理路径进行有效引导的重要性，对于提高复杂任务解决的可靠性和效率至关重要。

##### 4. 基于反馈与验证的迭代优化

这类方法通过引入外部反馈机制（如单元测试、静态分析）来验证生成代码的正确性，并将验证结果作为信号指导模型进行多轮迭代修复，形成一个“生成-验证-修复”的闭环。

-   **基于大语言模型的自动代码修复综述** (许鹏宇 等, 2024) [crad.ict.ac.cn](https://crad.ict.ac.cn/article/doi/10.7544/issn1000-1239.202440467?viewType=citedby-info): 这篇综述全面调研了基于LLM的自动代码修复（APR）技术，将其归纳为完形填空和神经机器翻译两大模式。论文指出，LLM通过强大的代码理解和生成能力，弥补了传统APR方法的不足。许多先进的APR方法都包含了迭代修复的思想，即self-repair，模型首先生成一个补丁，然后通过测试或静态分析工具验证，若失败则根据错误信息再次生成，直至成功或达到最大尝试次数。

-   **Dynamic Scaling of Unit Tests for Code Reward Modeling** (Ma 等, 2025) [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/95655): 该研究解决了迭代优化中奖励信号不可靠的问题，即LLM生成的单元测试本身可能存在错误。研究发现，单元测试的数量与奖励信号的质量正相关。基于此，作者提出了一个轻量级的单元测试生成器CodeRM-8B，并设计了一种动态扩展机制，根据问题难度自动调整生成的单元测试数量。实验表明，这种高质量、动态调整的反馈机制能够显著提升Llama3-8B和GPT-4o-mini等多种模型的代码生成性能。

##### 5. 个性化与风格化生成

除了功能正确性，代码的可读性和风格一致性在团队协作中同样重要。此类研究旨在让模型生成符合特定用户或项目编码风格的代码。

-   **MPCODER** (Dai 等, 2025) [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/32648): 该工作旨在弥合现有研究主要关注代码正确性而忽略个性化风格的差距。MPCODER是一个多用户个性化代码生成器，它结合了显式和隐式风格表示学习：通过显式残差学习捕捉语法层面的风格规范，通过隐式对比学习区分不同用户的语义风格约定。实验证明，该方法能有效为多个用户生成符合其个人编码习惯的代码，并通过一种新的评估指标验证了其个性化生成能力。

#### **实验与评价总结**

1.  **数据集趋势**：早期研究多依赖于大规模但可能含有噪声的开源代码库（如GitHub）。近期工作越来越重视数据集的真实性和任务相关性，例如 `ReCode` 专门构建了基于真实用户提交的错误-修复对的基准 **RACodeBench**，以更准确地评估代码修复能力。

2.  **评价指标的演进**：传统的基于Token匹配的指标（如 **BLEU**）已不足以评估代码的功能正确性。基于执行结果的 **Pass@k** 成为了事实上的黄金标准，但其计算开销巨大。因此，研究开始探索更高效的替代方案，如 `CodeScore-R` 提出的 **CodeScore-R** 指标，它基于模型和对比学习来评估代码功能，无需执行测试用例，且具有更好的鲁棒性 [zhuanzhi.ai](https://zhuanzhi.ai/paper/8b62b2dc48cca32cace2561b6572f87c)。同时，任务成本（如LLM调用次数、推理时间）也逐渐成为衡量方法实用性的重要维度。

3.  **共性实验结论**：
    *   **结构信息至关重要**：相较于将代码视为纯文本，融合AST、控制流图等结构化信息的方法（如 `UniXcoder`、`语法和语义结合的方法`）能带来显著的性能提升。
    *   **检索增强是刚需**：RAG被普遍证明能有效提升模型在处理长上下文、OOD问题和需要特定领域知识时的表现，是解决LLM“幻觉”和知识局限性的关键路径 [zhuanzhi.ai](https://zhuanzhi.ai/paper/f49cff257ef0cbf5e546373a59f6f8da)。
    *   **反馈闭环提升上限**：对于复杂代码生成和修复任务，单次生成成功率有限，“生成-验证”的迭代闭环是提高最终成功率的有效策略，而反馈信号的质量（如 `Dynamic Scaling of Unit Tests` 所示）直接决定了优化的天花板。

#### **趋势与挑战**

1.  **从代码片段到仓库级智能 (Repository-Level Intelligence)**：未来的代码AI必须超越单一文件，能够理解和操作整个代码仓库。这要求模型具备处理数百万行代码的长上下文能力、理解构建系统、API依赖关系以及项目特有的设计模式。仓库级RAG是实现这一目标的核心技术之一。

2.  **“小模型+大模型”协同与动态推理 (Small+Large Model Collaboration)**：随着LLM的API调用成本和能源消耗问题日益突出，依赖单一巨型模型的范式将面临挑战。未来的趋势是构建异构模型系统，利用轻量、高效的微调模型处理高频、简单的任务，仅在遇到不确定性高或复杂的难题时，才动态调用昂贵的通用大模型，如 `Coral` 方法所示 [www.arocmag.cn](https://www.arocmag.cn/abs/2025.04.0082)。

3.  **面向非功能性需求的生成 (Non-Functional Requirements-Aware Generation)**：当前研究主要关注功能正确性。未来的一个重要方向是生成满足特定非功能性需求（NFRs）的代码，如高性能、高安全性、低功耗或特定编码风格（如 `MPCODER` 的探索）。这需要模型不仅理解“做什么”，还要理解“怎么做才更好”，可能需要结合静态分析工具、性能剖析器等进行多目标优化。

4.  **自主学习与自我演化 (Autonomous Learning and Self-Evolution)**：未来的高级代码AI应具备自主学习能力。这意味着模型能够通过与开发环境（IDE、版本控制系统、CI/CD流水线）的持续交互，自动发现新的API用法、编码模式甚至修复自身的缺陷，从而实现知识的持续更新和能力的自我演化，成为一个真正与软件项目共同成长的“活”的智能体。

#### **结论**

自2022年以来，AI辅助代码生成技术经历了从单一模型暴力生成到多技术融合、精细化优化的深刻演变。通过融合代码的结构与语义信息、引入检索增强机制、构建模型协同框架以及形成反馈验证闭环，研究者们在提升代码生成与修复的准确性、鲁棒性和效率方面取得了显著成就。然而，实现能够深度理解并参与复杂软件工程实践的通用人工智能编程伙伴，仍面临着仓库级上下文理解、成本效率、非功能性需求满足等多重挑战。未来的研究将更加聚焦于构建智能化、系统化、自动化的代码生成与维护生态，推动AI在软件工程领域的应用走向新的高度。

#### **参考文献**

1.  Tao, Y., Qin, Y., & Liu, Y. (2025). *Retrieval-Augmented Code Generation: A Survey with Focus on Repository-Level Approaches*. [zhuanzhi.ai](https://zhuanzhi.ai/paper/f49cff257ef0cbf5e546373a59f6f8da)
2.  Dai, Z., Yao, C., Han, W., Yuan, Y., Gao, Z., & Chen, J. (2025). *MPCODER: Multi-user Personalized Code Generator with Explicit and Implicit Style Representation Learning*. [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/32648)
3.  Chen, Y., Jhamtani, H., Sharma, S., Fan, C., & Wang, C. (2025). *Steering Large Language Models between Code Execution and Textual Reasoning*. ICLR 2025. [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/112968)
4.  洪少东, 申国伟, 罗素芬, & 刘涛. (2025). 基于不确定性估计的微调代码生成模型与大语言模型的协同方法. *计算机应用研究*. [www.arocmag.cn](https://www.arocmag.cn/abs/2025.04.0082)
5.  许鹏宇, 况博裕, 苏铓, & 付安民. (2024). 基于大语言模型的自动代码修复综述. *计算机研究与发展*. [crad.ict.ac.cn](https://crad.ict.ac.cn/article/doi/10.7544/issn1000-1239.202440467?viewType=citedby-info)
6.  Guo, D., Lu, S., Duan, N., Wang, Y., Zhou, M., & Yin, J. (2022). *UniXcoder: Unified Cross-Modal Pre-training for Code Representation*. ACL 2022. [www.zhuanzhi.ai](https://www.zhuanzhi.ai/paper/783c50562dd63fa4487c8e75872111a3)
7.  Yang, G., Zhou, Y., Chen, X., & Zhang, X. (2024). *CodeScore-R: An Automated Robustness Metric for Assessing the Functional Correctness of Code Synthesis*. *Journal of Computer Research and Development*. [zhuanzhi.ai](https://zhuanzhi.ai/paper/8b62b2dc48cca32cace2561b6572f87c)
8.  付善庆, 李征, 赵瑞莲, & 郭俊霞. (2022). 语法和语义结合的代码补全方法. *软件学报, 33*(11), 3930-3943. [jos.org.cn](https://jos.org.cn/html/2022/11/6324.htm)
9.  Ma, Z., Zhang, X., Zhang, J., Yu, J., Luo, S., & Tang, J. (2025). *Dynamic Scaling of Unit Tests for Code Reward Modeling*. arXiv preprint. [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/95655)
10. Zhao, Y., Chen, S., Zhang, J., & Li, Z. (2025). *ReCode: Improving LLM-based Code Repair with Fine-Grained Retrieval-Augmented Generation*. arXiv preprint. [blog.csdn.net](https://blog.csdn.net/zhangjiaoshou_/article/details/151150533)
11. Li, Y., Choi, D., Chung, J., et al. (2022). *Competition-Level Code Generation with AlphaCode*. *Science, 378*(6624), 1092-1097.
12. Du, Y., Li, S., Dai, H., et al. (2023). *Code Llama: Open Foundation Models for Code*. arXiv preprint arXiv:2308.12950.