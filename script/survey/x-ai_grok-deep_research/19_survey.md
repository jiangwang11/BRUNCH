引言
上下文学习（In-context Learning, ICL）是大型语言模型（LLMs）在自然语言处理（NLP）中的关键能力，通过提示中的少量示例实现任务适应，而无需参数更新。2022–2025年间，ICL研究从理论机制解析转向提示优化和检索增强，聚焦于提升推理效率和泛化能力。该时期代表作主要发表于NeurIPS、ICLR、EMNLP、ACL和arXiv，强调ICL的隐式推理过程和示例选择策略。本综述分类讨论方法，并总结实验共性与未来趋势。
方法分类与代表作
理论机制
Min et al. (2022) Rethinking the Role of Demonstrations: What Makes In-Context Learning Work? (EMNLP 2022)
研究问题：示例在ICL中是否必需，以及其对任务解决的贡献机制。
核心方法：通过控制实验替换示例标签为随机值，或使用随机输入示例，同时保持任务指令不变，测试PaLM、GPT-3和Codex模型。
关键实验结论：随机标签示例性能接近真实示例，随机域内输入示例提升2–4%零样本性能，而域外示例无改善，表明示例主要提供输出格式和任务分布信息，而非具体知识。
ICL主要依赖任务指令而非示例内容。
Xie et al. (2022) An Explanation of In-context Learning as Implicit Bayesian Inference (ICLR 2022)
研究问题：ICL如何通过提示实现隐式推理。
核心方法：将ICL建模为隐式贝叶斯推理过程，其中提示示例作为证据更新潜在概念的后验分布，使用Transformer模拟此过程。
关键实验结论：在合成任务上，ICL等价于贝叶斯推理，提示顺序影响性能，逆转示例标签导致模型忽略先验。
证明ICL通过隐式更新潜在变量实现泛化。
Akyürek et al. (2022) What Learning Algorithm is In-Context Learning? (NeurIPS 2022)
研究问题：ICL对应何种学习算法。
核心方法：证明Transformer可模拟梯度下降，通过注意力机制构建线性模型并执行优化步。
关键实验结论：在回归任务上，ICL实现4–7步梯度下降，匹配显式训练性能，但受上下文长度限制。
揭示ICL为隐式元优化过程。
Garg et al. (2022) What Can Transformers Learn In-Context? (NeurIPS 2022)
研究问题：Transformer在ICL中可学习哪些函数类。
核心方法：分析Transformer在少样本下的函数拟合能力，针对线性回归和稀疏函数进行理论界限推导。
关键实验结论：Transformer在ICL中可高效学习线性函数，性能随层数增加而提升，但对非线性函数泛化有限。
确认ICL依赖模型架构深度。
提示优化
Wei et al. (2022) Chain-of-Thought Prompting Elicits Reasoning in Large Language Models (NeurIPS 2022)
研究问题：如何通过提示提升LLMs的多步推理能力。
核心方法：引入链式思考（CoT）提示，在示例中插入中间推理步骤，使用PaLM 540B等模型测试。
关键实验结论：在GSM8K数学任务上，CoT将准确率从17.9%提升至56.9%，在StrategyQA上从68.6%至77.8%，仅在大规模模型中有效。
证明CoT解锁规模化推理能力。
Wang et al. (2022) Self-Consistency Improves Chain of Thought Reasoning in Language Models (arXiv 2022)
研究问题：CoT提示中贪婪解码的局限性。
核心方法：提出自一致性解码，采样多个推理路径并通过多数投票选择一致答案，使用温度采样生成多样路径。
关键实验结论：在GSM8K上提升17.9%，SVAMP上11.0%，路径数为40时性能最优，与模型规模正相关。
显示多样路径聚合提升鲁棒性。
Zhou et al. (2022) Least-to-Most Prompting Enables Complex Reasoning in Large Language Models (arXiv 2022)
研究问题：复杂问题分解在ICL中的作用。
核心方法：最小到最大提示，将问题分解为子问题序列，先解决简单子问题再整合，使用InstructGPT测试。
关键实验结论：在GSM8K上准确率从10.4%升至40.7%，MultiArith从17.7%至78.7%，自一致性进一步提升至70.1%。
证明问题分解改善多步泛化。
Yao et al. (2023) Tree of Thoughts: Deliberate Problem Solving with Large Language Models (NeurIPS 2023)
研究问题：扩展CoT以支持搜索空间探索。
核心方法：引入思想树框架，使用LLMs生成和评估思想节点，支持前向/回溯搜索。
关键实验结论：在Game of 24任务上准确率从4%升至74%，创意写作任务上人类评估提升显著。
揭示树状结构优于线性链。
Besta et al. (2024) Graph of Thoughts: Augmenting Large Language Models with Brainstorming and Reasoning (arXiv 2024)
研究问题：非线性结构在ICL推理中的应用。
核心方法：思想图框架，将思想作为图节点，支持聚合和分支操作，使用GPT-4测试。
关键实验结论：在排序任务上效率提升60%，输入分类上准确率提高10–20%。
证明图结构增强并行推理。
检索增强ICL
Rubin et al. (2022) Learning To Retrieve Prompts for In-Context Learning (NAACL 2022)
研究问题：示例选择对ICL性能的影响。
核心方法：训练检索模型从训练集中选择相关提示，使用对比学习优化嵌入空间。
关键实验结论：在SuperGLUE任务上，检索提示将准确率提升8%，优于随机选择。
确认示例相关性关键。
Liu et al. (2022) What Makes Good In-Context Examples for GPT-3? (arXiv 2022)
研究问题：示例质量标准。
核心方法：分析多样性和输入分布，使用kNN检索优化示例选择。
关键实验结论：在语义解析任务上，优化示例提升5–10%，多样示例减少偏差。
强调分布匹配的重要性。
Ye et al. (2023) In-Context Learning with Iterative Demonstration Selection (arXiv 2023)
研究问题：动态示例选择。
核心方法：迭代选择框架，使用LLMs反馈更新示例集。
关键实验结论：在EMNLP 2023基准上，迭代选择提升15%，减少示例数量30%。
证明反馈循环改善效率。
Zhang et al. (2025) Sample Efficient Demonstration Selection for In-Context Learning (arXiv 2025)
研究问题：少样本下的高效示例选择。
核心方法：提出生成式框架，使用偏好学习优化演示选择。
关键实验结论：在ACL 2025任务上，减少示例50%仍保持90%性能。
揭示偏好模型的潜力。
实验与评价总结
ICL性能随模型参数规模（>100B）显著提升，在多步推理任务中表现突出，但对示例分布敏感，导致域外泛化受限。示例质量和多样性一致改善准确率5–20%，检索增强减少噪声影响。CoT变体在数学和符号任务上将基线准确率提升2–4倍，自一致性降低不确定性10–15%。整体，ICL在零样本设置下优于传统少样本，但计算成本随路径采样增加；评估指标显示ICL隐式模拟梯度优化，但受上下文长度约束。
趋势与挑战
2025年前后，ICL将向多模态扩展，整合视觉-文本提示提升跨域推理。理论模型化深化，聚焦注意力机制的动态适应。长上下文模型中ICL效率优化，成为挑战焦点。隐私保护ICL兴起，针对敏感数据检索。挑战包括示例偏差放大幻觉，以及计算资源限制大规模部署。
结论
2022–2025年ICL研究从理论解析到优化应用，显著推进NLP任务适应性。未来需解决泛化和效率问题，推动实际部署。
参考文献

Min et al. (2022). Rethinking the Role of Demonstrations: What Makes In-Context Learning Work? In Proceedings of EMNLP 2022.
Xie et al. (2022). An Explanation of In-context Learning as Implicit Bayesian Inference. In Proceedings of ICLR 2022.
Akyürek et al. (2022). What Learning Algorithm is In-Context Learning? In Proceedings of NeurIPS 2022.
Garg et al. (2022). What Can Transformers Learn In-Context? In Proceedings of NeurIPS 2022.
Wei et al. (2022). Chain-of-Thought Prompting Elicits Reasoning in Large Language Models. In Proceedings of NeurIPS 2022.
Wang et al. (2022). Self-Consistency Improves Chain of Thought Reasoning in Language Models. arXiv:2203.11171.
Zhou et al. (2022). Least-to-Most Prompting Enables Complex Reasoning in Large Language Models. arXiv:2205.10625.
Yao et al. (2023). Tree of Thoughts: Deliberate Problem Solving with Large Language Models. In Proceedings of NeurIPS 2023.
Besta et al. (2024). Graph of Thoughts: Augmenting Large Language Models with Brainstorming and Reasoning. arXiv:2308.09687.
Rubin et al. (2022). Learning To Retrieve Prompts for In-Context Learning. In Proceedings of NAACL 2022.
Liu et al. (2022). What Makes Good In-Context Examples for GPT-3? arXiv:2101.06804.
Ye et al. (2023). In-Context Learning with Iterative Demonstration Selection. arXiv:2310.09881.
Zhang et al. (2025). Sample Efficient Demonstration Selection for In-Context Learning. arXiv:2506.08607.
Dong et al. (2023). A Survey on In-context Learning. arXiv:2301.00234.