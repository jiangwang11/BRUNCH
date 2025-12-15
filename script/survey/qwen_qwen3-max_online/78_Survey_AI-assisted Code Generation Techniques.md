# AI辅助代码生成技术研究综述（2022–2025）

## 引言

自2022年以来，大语言模型（Large Language Models, LLMs）在代码生成任务中展现出前所未有的能力，显著推动了AI辅助软件开发（AI-assisted Software Development）的发展。早期工作如Codex和CodeGen主要聚焦于单文件、单函数级的代码补全，而近期研究则向更复杂的项目级、交互式和个性化生成方向演进。本文系统梳理2022至2025年间在代码生成领域的代表性工作，按技术路径划分为四类：通用代码大模型、项目级上下文建模、人机协同交互机制、以及个性化与鲁棒性增强方法。综述严格基于真实发表的顶会/期刊/arXiv论文，旨在呈现该领域从“生成正确性”向“生成实用性”转型的技术脉络。

## 方法分类与代表作

### 1. 通用代码大模型（General-purpose Code LLMs）

**DeepSeek-Coder** \[arXiv:2401.14196, 2024\] 针对开源代码模型性能落后于闭源模型的问题，提出从头训练的1.3B–33B参数系列模型。其核心方法包括在2万亿token的高质量项目级语料上预训练，并引入Fill-in-the-Middle（FIM）任务与16K上下文窗口。实验表明，DeepSeek-Coder-33B在HumanEval、MBPP等基准上超越Codex和GPT-3.5，且7B版本在多项任务上优于CodeLlama-33B，证明了高质量数据与架构适配的重要性 [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/d8ef73fb-0b68-402b-a17a-abab02c77c21)。

**CodeT5+** \[arXiv:2305.07922, 2023\] 解决现有模型架构单一（仅编码器或仅解码器）导致任务泛化能力受限的问题。该工作提出统一的encoder-decoder架构，可灵活切换为编码器（用于代码理解）、解码器（用于代码生成）或完整seq2seq模式。通过融合span denoising、causal LM和对比学习等多目标预训练，CodeT5+在10余项理解与生成任务上均达到SOTA，尤其在代码摘要和缺陷检测任务中优势显著 [csdn.net](https://blog.csdn.net/qq_30731313/article/details/146216224)。

**Qwen2.5-Coder** \[arXiv:2409.11677, 2024\] 作为Qwen2.5架构的代码专用版本，通过5.5万亿token的混合语料（含合成数据）预训练，并强调数据清洗与平衡策略。其7B模型在代码生成、补全、推理和修复等10+基准上持续优于同规模甚至更大模型（如CodeLlama-7B）。关键结论在于，精心设计的数据混合策略可显著提升模型在多任务上的泛化能力，而不仅依赖模型规模 [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/116463e9-e168-4ad4-badf-cd1793c253d8)。

### 2. 项目级上下文建模（Repository-level Context Modeling）

**CoEdPilot** \[JCST, 2025\] 针对现有工具（如Copilot）仅支持当前文件编辑、无法处理多轮跨文件修改的缺陷，提出项目级交互式代码编辑推荐框架。其核心包含两阶段编辑定位器（文件级+行级）和历史编辑分析模块，基于18万条开源提交微调模型。用户研究表明，在需多处协同修改的复杂特性添加任务中，CoEdPilot显著优于Copilot（p=0.02, d=0.80），证明了项目级上下文对复杂开发场景的关键价值 [jcst.ict.ac.cn](https://jcst.ict.ac.cn/cn/article/id/e36d187c-955f-4c75-a98b-234080c293c9)。

**Retrieval-Augmented Code Generation (RAG-based)** \[arXiv:2510.04905, 2025\] 面向Repository-Level Code Generation（RLCG）挑战，系统综述了基于检索增强的代码生成方法。其核心思想是通过外部检索机制（如向量数据库）动态引入相关文件或历史提交作为上下文，解决LLM长程依赖与全局一致性问题。代表性工作如RepoCoder通过跨文件检索提升多文件生成的连贯性，在跨模块API调用任务中错误率降低18% [zhuanzhi.ai](https://zhuanzhi.ai/paper/f49cff257ef0cbf5e546373a59f6f8da)。

### 3. 人机协同与不确定性感知（Human-AI Collaboration）

**Coral** \[《计算机应用研究》, 2025\] 针对微调模型与通用LLM决策边界模糊的问题，提出基于不确定性估计的协同框架。该方法为微调模型配备不确定性得分（通过预期校准误差优化），并设定阈值区分分布内（ID）与分布外（OOD）输入：ID数据由微调模型处理，OOD则交由LLM。在两个基准上，Coral的Exact Match比单一模型高4.2–6.8点，验证了不确定性驱动的分工机制的有效性 [arocmag.cn](https://www.arocmag.cn/abs/2025.04.0082)。

### 4. 个性化与风格建模（Personalization）

**MPCoder** \[arXiv:2406.17255, 2024\] 关注LLM生成代码缺乏开发者个人风格的问题，提出多用户个性化代码生成器。其方法结合显式风格残差学习（捕获语法风格如缩进、命名）与隐式对比学习（捕获语义风格如API偏好），并通过风格适配器为不同用户生成定制化代码。在GitHub用户数据集上，MPCoder在风格相似性指标上比基线高23%，且不影响功能正确性 [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/32648)。

## 实验与评价总结

近四年代码生成研究的实验范式呈现三大共性：  
1. **基准多元化**：除传统HumanEval、MBPP外，新增多文件任务（如RepoEval）、交互式任务（如CoEdPilot用户研究）和鲁棒性测试（如EvalPlus）；
2. **评价维度扩展**：从单一功能正确性（pass@k）扩展至风格一致性、跨文件一致性、用户效率（任务完成时间）、交互质量（接受率）等；
3. **开源与可复现性提升**：主流工作（如DeepSeek-Coder、Qwen2.5-Coder）均开源模型与代码，并提供宽松许可证，推动社区验证。

## 趋势与挑战

基于2025年前后最新研究，可识别出以下趋势：  
1. **从静态生成到动态交互**：研究重心正从“一次性生成”转向支持多轮反馈、编辑定位与意图演化的交互式编程助手（如CoEdPilot）；
2. **上下文粒度项目化**：模型需理解仓库级依赖、跨文件API调用及历史演进，检索增强与图神经网络等技术成为提升项目级一致性的关键；
3. **个性化与可信生成融合**：未来系统需同时满足功能正确、风格匹配、安全鲁棒（如漏洞规避）和不确定性透明四大要求，MPCoder与Coral分别从风格与置信度切入，预示多目标协同优化方向。

## 结论

2022–2025年AI辅助代码生成技术从通用大模型奠基，快速演进至项目级、交互式与个性化新阶段。代表工作如DeepSeek-Coder、CoEdPilot和MPCoder分别在模型能力、上下文建模和人机适配层面取得突破。未来研究需进一步解决长上下文推理效率、冷启动意图理解、以及生成代码的安全性验证等核心挑战，以实现真正融入开发工作流的智能编程伙伴。

## 参考文献

1. Guo, D., et al. (2024). DeepSeek-Coder: When the Large Language Model Meets Programming. *arXiv:2401.14196*.  
2. Hui, B., et al. (2024). Qwen2.5-Coder Technical Report. *arXiv:2409.11677*.  
3. Wang, Y., et al. (2023). CodeT5+: Open Code Large Language Models for Code Understanding and Generation. *arXiv:2305.07922*.  
4. Huang, Y., et al. (2025). CoEdPilot: Interactively Recommending Project-Wise Code Edits. *Journal of Computer Science and Technology*. [jcst.ict.ac.cn](https://jcst.ict.ac.cn/cn/article/id/e36d187c-955f-4c75-a98b-234080c293c9)  
5. Tao, Y., Qin, Y., & Liu, Y. (2025). Retrieval-Augmented Code Generation: A Survey with Focus on Repository-Level Approaches. *arXiv:2510.04905*. [zhuanzhi.ai](https://zhuanzhi.ai/paper/f49cff257ef0cbf5e546373a59f6f8da)  
6. Hong, S., et al. (2025). Coordination of fine-tuned code generation models and large language models via uncertainty estimation. *Application Research of Computers*. [arocmag.cn](https://www.arocmag.cn/abs/2025.04.0082)  
7. Dai, Z., et al. (2024). MPCoder: Multi-user Personalized Code Generator with Explicit and Implicit Style Representation Learning. *arXiv:2406.17255*. [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/32648)  
8. Xu, P., et al. (2024). Survey of Large-Language-Model-Based Automated Program Repair. *Journal of Computer Research and Development*.  
9. Chen, M., et al. (2021). Evaluating Large Language Models Trained on Code. *arXiv:2107.03374* (Codex).  
10. Li, R., et al. (2023). StarCoder: May the Source Be with You! *arXiv:2305.06161*.  
11. Nijkamp, E., et al. (2022). CodeGen: An Open Large Language Model for Code with Multi-Turn Program Synthesis. *arXiv:2208.07463*.  
12. Lu, Z., et al. (2023). Code Llama: Open Foundation Models for Code. *arXiv:2308.12950*.