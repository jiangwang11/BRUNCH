## AI辅助代码生成技术综述 (2022–2025)

### 引言

随着人工智能技术的飞速发展，特别是大型语言模型（LLMs）的兴起，AI辅助代码生成（AI-assisted Code Generation）已成为软件工程领域备受关注的研究方向。这项技术旨在利用AI模型自动化或半自动化地生成、补全、修复甚至优化代码，从而显著提高开发效率、降低开发成本并改善软件质量。传统的代码生成方法在处理复杂逻辑、保持上下文一致性以及适应多用户个性化需求方面存在局限性。近三年来，研究人员致力于开发更智能、更鲁棒的AI辅助代码生成技术，特别是聚焦于如何让LLMs更好地理解和生成符合实际工程需求的复杂代码，解决代码生成中的准确性、效率和个性化等核心问题。本综述将聚焦2022年至2025年间的代表性工作，通过方法分类、实验总结和趋势展望，系统梳理该领域的最新进展。

### 方法分类与代表作

AI辅助代码生成技术在近年集中于改进模型架构、代码表示、上下文利用和用户个性化等方面。

#### 1. 检索增强生成（Retrieval-Augmented Generation, RAG）

RAG技术旨在通过检索相关代码片段或知识库来增强LLMs的代码生成能力，以解决LLMs在处理长距离依赖和特定领域知识时的局限性。

*   **Retrieval-Augmented Code Generation: A Survey with Focus on Repository-Level Approaches (2025)** [zhuanzhi.ai](https://zhuanzhi.ai/paper/f49cff257ef0cbf5e546373a59f6f8da)
    *   该综述全面审视了检索增强代码生成（RACG）领域，并特别强调了代码库级别的处理方法。研究问题在于LLMs在代码生成中难以捕获跨文件或模块的长距离依赖和全局语义一致性。作者总结了RACG在生成策略、检索模态、模型架构、训练范式和评估协议等方面的现有工作，旨在为理解该领域提供统一分析框架。
*   **ReCode: Improving LLM-based Code Repair with Fine-Grained Retrieval-Augmented Generation (2025)** [blog.csdn.net](https://blog.csdn.net/zhangjiaoshou_/article/details/151150533)
    *   为解决LLM代码修复中高成本、低传统RAG质量及对分布外（OOD）缺陷适应性差的问题，该工作提出了ReCode框架。其核心思想是结合“算法感知检索”和“双视图编码”实现细粒度的RAG，通过LLM预测代码算法类型缩小检索范围，并分别处理文本描述和代码结构。实验结果显示，ReCode在多个基准测试上显著提高了修复准确率，同时将推理成本降低了3-4倍。

#### 2. 代码生成与执行协同（Code Generation and Execution Coordination）

此类方法关注如何将代码生成与代码执行能力相结合，以更好地验证、调试和迭代生成的代码，使其更可靠地解决复杂问题。

*   **Steering Large Language Models between Code Execution and Textual Reasoning (2025)** [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/112968)
    *   该研究探讨了在代码执行与纯文本推理之间引导LLMs的重要性，指出现有方法在需要时正确引导LLMs编写代码的不足。核心在于通过代码执行来解决数学、逻辑等复杂任务，避免纯文本推理的固有局限性。作者提出了三种方法来改进LLMs的代码/文本生成引导，并对比了其在多种任务和LLMs上的表现，发现即使任务可通过代码解决，LLM生成的代码结果也并非总是优于文本推理。
*   **Dynamic Scaling of Unit Tests for Code Reward Modeling (2025)** [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/95655)
    *   针对LLMs在代码生成中一次性生成准确代码的挑战，该研究提出通过动态扩展单元测试来提高奖励信号的质量。基于单元测试数量与奖励信号质量的正相关性，他们提出了轻量级单元测试生成器CodeRM-8B和动态扩展机制，根据问题难度调整单元测试数量。实验表明，该方法显著提升了多种LLMs在代码生成任务中的性能（例如，Llama3-8B提升了18.43%）。

#### 3. 个性化与风格化代码生成（Personalized and Stylized Code Generation）

这类方法旨在使生成的代码更符合特定用户的编码习惯、风格或团队规范。

*   **MPCODER: Multi-user Personalized Code Generator with Explicit and Implicit Style Representation Learning (2025)** [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/32648)
    *   为了实现多用户个性化代码生成，该研究提出了MPCoder模型。其核心思想是通过显式编码风格残差学习捕捉语法代码风格标准，并利用隐式风格学习捕捉语义代码风格约定。MPCoder通过训练多用户风格适配器和对比学习，更好地区分不同用户的隐式特征表示，从而为多个用户生成个性化代码，并引入了新的评估指标来衡量代码风格相似性。

#### 4. 统一代码表示与跨模态预训练（Unified Code Representation and Cross-Modal Pre-training）

为了提升模型对代码的深层理解，研究人员探索了更为全面和统一的代码表示方法，并利用多模态信息进行预训练。

*   **UniXcoder: Unified Cross-Modal Pre-training for Code Representation (2022)** [zhuanzhi.ai](https://www.zhuanzhi.ai/paper/783c50562dd63fa4487c8e75872111a3)
    *   为支持代码理解和生成任务，该工作提出了UniXcoder，一个统一的跨模态预训练模型。模型利用带有前缀适配器的掩码注意力机制控制模型行为，并结合抽象语法树（AST）和代码注释等跨模态内容增强代码表示。UniXcoder创新性地将AST转换为保留结构信息的序列结构，并通过对比学习和跨模态生成任务对齐编程语言间的表示。UniXcoder在多项任务上取得了先进性能，并验证了注释和AST对模型能力的提升作用。

#### 5. 自动代码修复（Automated Program Repair, APR）

APR专注于利用AI自动识别并修复代码中的缺陷，是代码生成技术在软件维护领域的重要应用。

*   **基于大语言模型的自动代码修复综述 (2024)** [crad.ict.ac.cn](https://crad.ict.ac.cn/article/doi/10.7544/issn1000-1239.202440467?viewType=citedby-info)
    *   该综述全面调研并分析了近年基于LLM的自动代码修复（APR）技术发展。研究人员总结了完形填空模式和神经机器翻译模式两大类LLM-based APR技术，并从模型类型、规模、缺陷类型、编程语言和修复方案优缺点等方面进行了对比。文章还梳理了APR数据集及评估指标，并探讨了实证研究进展，为理解当前APR的挑战和未来方向提供了基础。
*   **THOR：通过 RL 对工具集成进行分层优化以实现数学推理 (2025)** [huggingface.ac.cn](https://huggingface.ac.cn/papers/2509.13761)
    *   尽管该论文主要关注数学推理，但其提出的强化学习（RL）工具集成框架THOR对代码生成特别是涉及精确计算和符号处理的代码生成具有启示。THOR通过构建高质量工具集成推理路径数据集和RL策略，优化轨迹级别问题解决和步骤级别代码生成，并包含自校正机制来动态修改错误推理路径。这表明将RL与工具集成用于代码生成或修复，可有效提升精确性和可靠性。

### 实验与评价总结

针对AI辅助代码生成技术，实验评估通常采用多种指标和基准数据集。在代码生成任务中，BLEU、CodeBLEU、Exact Match (EM) 等指标被广泛用于衡量生成代码与参考代码的相似性和功能正确性。对于代码修复任务，Pass@k指标（即生成的前k个补丁中包含至少一个正确补丁的比例）是衡量修复准确率的关键。

总体而言，研究表明：

1.  **LLMs在复杂代码生成和修复方面展现出卓越能力**，但其性能高度依赖于有效的上下文利用、高质量的代码表示和强大的推理机制。
2.  **检索增强技术**能够显著提升LLMs处理长距离依赖和特定领域知识的效率和准确性，尤其是在代码库级别或细粒度检索的情境下，案例与任务的相关性对性能至关重要。
3.  **代码执行和单元测试**是验证和优化生成代码不可或缺的环节，通过引入奖励模型和动态测试用例，可以有效提升代码的功能正确性和鲁棒性。
4.  **个性化和风格学习**成为新的研究热点，能够使生成的代码更加符合开发者或团队的特定需求，提高了代码的可用性和可维护性。
5.  **统一的跨模态预训练**利用AST、代码注释等多源信息，能够为模型提供更丰富的代码语义和结构信息，从而提升其在多种任务上的泛化能力。
6.  **推理成本和效率**依然是实际应用中的重要考量，通过优化检索策略、减少LLM调用次数、或协同轻量级模型与大型模型，可以有效平衡性能与资源消耗。

### 趋势与挑战

未来几年，AI辅助代码生成领域预计将沿着以下几个方向发展：

1.  **多模态与多语言融合的统一模型**：当前的LLMs在单一语言或文本模态上表现出色，但未来的趋势将是开发能够处理多种编程语言、自然语言、代码结构（如AST）、甚至UI设计图等多种信息的统一模型，实现更全面的代码理解和生成能力。这将涉及更复杂的跨模态对齐和预训练技术。
2.  **更深度的个性化与企业级定制**：除了用户个人风格，模型将更专注于学习企业内部的编码规范、设计模式和遗留系统特点，提供与企业现有代码库高度兼容和风格一致的代码。这需要更精细的用户画像构建、持续学习和基于反馈的自适应调整机制。
3.  **基于强化学习的持续优化与自适应能力**：LLMs在生成代码后，通过实际编译、运行和测试反馈，利用强化学习进行持续优化将成为主流。模型将能够从代码执行结果、性能指标和安全漏洞扫描中学习，自动迭代和改进生成的代码，使其具备更强的自适应问题解决能力和错误修复能力，而非仅仅生成静态代码。

### 结论

2022年至2025年，AI辅助代码生成技术在LLMs的推动下取得了显著进展。从检索增强、代码执行协同到个性化生成和统一代码表示，研究人员不断探索更智能、更高效的代码生成范式。这些进步不仅提升了代码生成的准确性和鲁棒性，也为软件开发的自动化和智能化开辟了新的道路。尽管现有方法已展现出巨大潜力，但在多模态融合、深度个性化和强化学习驱动的自适应优化方面仍面临挑战。未来的研究将致力于构建更通用、更智能、能与人类开发者深度协作的AI辅助代码生成系统。

### 参考文献

*   [zhuanzhi.ai](https://zhuanzhi.ai/paper/f49cff257ef0cbf5e546373a59f6f8da) Tao, Y., Qin, Y., & Liu, Y. (2025). *Retrieval-Augmented Code Generation: A Survey with Focus on Repository-Level Approaches*.
*   [blog.csdn.net](https://blog.csdn.net/zhangjiaoshou_/article/details/151150533) Zhao, Y. et al. (2025). ReCode: Improving LLM-based Code Repair with Fine-Grained Retrieval-Augmented Generation. *arXiv preprint arXiv:2509.02330*.
*   [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/112968) Chen, Y. et al. (2025). *Steering Large Language Models between Code Execution and Textual Reasoning*. ICLR 2025.
*   [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/95655) Ma, Z. et al. (2025). *Dynamic Scaling of Unit Tests for Code Reward Modeling*. arXiv preprint arXiv:2501.01054.
*   [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/32648) Dai, Z. et al. (2025). *MPCODER: Multi-user Personalized Code Generator with Explicit and Implicit Style Representation Learning*. arXiv preprint arXiv:2406.17255.
*   [zhuanzhi.ai](https://www.zhuanzhi.ai/paper/783c50562dd63fa4487c8e75872111a3) Guo, D. et al. (2022). UniXcoder: Unified Cross-Modal Pre-training for Code Representation. *ACL 2022*.
*   [crad.ict.ac.cn](https://crad.ict.ac.cn/article/doi/10.7544/issn1000-1239.202440467?viewType=citedby-info) 许鹏宇, 况博裕, 苏铓, & 付安民. (2024). 基于大语言模型的自动代码修复综述. *计算机应用研究*. (In Chinese)
*   [huggingface.ac.cn](https://huggingface.ac.cn/papers/2509.13761) Chang, Q. et al. (2025). *THOR: Tool-Integrated Hierarchical Optimization via RL for Mathematical Reasoning*. arXiv preprint arXiv:2509.13761.
*   [www.arocmag.cn](https://www.arocmag.cn/abs/2025.04.0082) 洪少东, 申国伟, 罗素芬, & 刘涛. (2025). 基于不确定性估计的微调代码生成模型与大语言模型的协同方法. *计算机应用研究* (优先出版). (In Chinese)
*   Yang, G., Zhou, Y., Chen, X., & Zhang, X. (2024). CodeScore-R: An Automated Robustness Metric for Assessing the FunctionalCorrectness of Code Synthesis. *arXiv preprint arXiv:2406.06902v1*. (Cited from [zhuanzhi.ai](https://zhuanzhi.ai/paper/8b62b2dc48cca32cace2561b6572f87c) reference)