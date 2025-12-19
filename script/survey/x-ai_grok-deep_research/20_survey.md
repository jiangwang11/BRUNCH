新闻摘要中使用大型语言模型的综述
引言
新闻摘要是自然语言处理的核心任务，旨在从海量信息中提炼关键内容。随着大型语言模型（LLMs）的快速发展，其在新闻摘要中的应用从2022年起显著增加，主要解决传统方法在抽象性和事实一致性上的局限。LLMs如GPT-3和Llama系列通过零样本或少样本学习提升摘要质量，但面临幻觉和泛化偏差问题。本综述聚焦2022–2025年代表性工作，按方法分类讨论，并总结实验共性、趋势与挑战。
方法分类与代表作
基于提示工程的方法

Goyal et al. (2022) 研究GPT-3在新闻摘要中的零样本和少样本性能问题，焦点是评价指标的可靠性。核心方法使用链式提示引导GPT-3生成摘要，并通过人类评估比较流畅性和事实性。关键实验结论显示GPT-3摘要在流畅性上优于基线，但事实错误率高达15%–20%，强调需改进参考摘要质量。
Siddiqui et al. (2024) 针对LLMs在新闻摘要中的连贯性和事实准确性不足，提出先进提示工程。核心方法设计多层提示框架，包括角色扮演和示例注入以提升生成质量。实验结论表明，该方法在CNN/Daily Mail数据集上将ROUGE-2分数提升至0.28，事实一致性提高12%。
Chen et al. (2024) 解决传统提示在复杂新闻摘要中的局限，如信息遗漏。核心方法采用多阶段提示框架，先提取关键实体再合成摘要，使用Llama模型。结论显示在Newsroom数据集上，摘要覆盖率达85%，优于单阶段提示的75%。

微调和指令调优方法

Zhang et al. (2024) 探讨指令调优对LLMs新闻摘要零样本能力的贡献。核心方法评估10种LLMs，包括指令调优变体，通过人类判断比较摘要质量。结论发现指令调优使350M参数模型性能匹敌175B模型，摘要与人类水平相当，但参考质量低导致自动指标相关性仅0.4。
Chen (2025) 针对大规模模型在新闻摘要中的计算成本高，提出LoRA微调方法。核心方法在T5-large基础上应用低秩适配，专注于新闻特定数据集训练。结论显示在XSum数据集上，ROUGE-L分数达0.45，训练成本降低80%。
Sadhukhan (2025) 研究深度学习模型在自动化新闻提取中的摘要效率。核心方法比较T5-base、T5-large、BART和PEGASUS在新闻数据集上的微调性能。结论表明PEGASUS在事实一致性上达96%，但T5-large在压缩率上优越，平均摘要长度缩短30%。

小型语言模型的应用

Lu et al. (2025) 探究小型语言模型（SLMs）是否可替代LLMs进行新闻摘要，尤其在边缘设备上。核心方法评估19种<4B参数SLMs，使用BertScore和事实一致性指标在2000样本上测试。结论显示顶级SLMs如Phi-3-Mini在BertScore上达70+，事实一致性95%，匹敌70B LLMs，但简单提示优于复杂提示。
Botev et al. (2025) 基准测试小型模型在新闻摘要中的能力，焦点是计算效率。核心方法比较20种近期SLMs在新闻数据集上的零样本性能。结论发现小型模型在连贯性上达90%，但在复杂主题上覆盖率降至70%，适合资源受限场景。

事实一致性评价方法

Tam et al. (2023) 通过新闻摘要评估LLMs的事实一致性问题。核心方法使用新闻摘要作为代理任务，提出新指标测量幻觉率。结论显示LLMs幻觉率达20%–30%，新指标与人类判断相关性0.65，高于传统指标。
Luo et al. (2023) 利用ChatGPT作为摘要事实不一致评估器。核心方法在新闻数据集上测试ChatGPT检测摘要错误的能力。结论表明ChatGPT在事实检测准确率达85%，优于BERT-based方法，但对细微错误敏感性低。
Kubli et al. (2025) 分析LLMs在科学新闻摘要中的泛化偏差。核心方法比较LLM和人类摘要，量化广义陈述频率。结论显示LLM泛化语句多5倍，导致潜在误导，需针对性提示缓解。

实验与评价总结
实验共性结论显示，指令调优显著提升零样本摘要质量，使小型模型性能接近大型模型，但事实幻觉率普遍在15%–30%，需辅助指标如BertScore（相关性0.4–0.7）评估。SLMs在资源受限环境下事实一致性达95%，压缩率优于LLMs 20%–30%，简单提示框架下性能稳定。自动指标在低质量参考下失效，人类评估揭示LLM摘要与专业作者相当，但泛化偏差在科学新闻中放大误导风险。数据集如CNN/Daily Mail和XSum暴露覆盖率不足70%的共性问题，推动多模态增强需求。
趋势与挑战
2025年前后研究趋势预测：一是多模态集成，将文本与图像/视频结合，提升摘要丰富度，如实时新闻流处理；二是个性化摘要，融入用户偏好和上下文，实现动态调整；三是事实增强机制，如检索增强生成（RAG）减少幻觉率至10%以下。挑战包括计算成本高企、数据集偏差放大泛化问题，以及伦理考量如偏差传播。
结论
LLMs已革新新闻摘要，但事实性和效率仍需优化。未来工作应聚焦可持续模型和多源验证，以实现更可靠应用。
参考文献

Goyal, T., Li, J. J., & Durrett, G. (2022). News Summarization and Evaluation in the Era of GPT-3. arXiv preprint arXiv:2209.12356.
Tam, D., Mascarenhas, A., Zhang, S., Kwan, S., Bansal, M., & Raffel, C. (2023). Evaluating the Factual Consistency of Large Language Models Through News Summarization. In Findings of the Association for Computational Linguistics: ACL 2023.
Zhang, T., Ladhak, F., Durmus, E., Liang, P., McKeown, K., & Hashimoto, T. B. (2024). Benchmarking Large Language Models for News Summarization. Transactions of the Association for Computational Linguistics, 12, 39-57.
Lu, T., Chen, C., Huang, F., Yu, F., Li, M., Yao, Z., Yang, K., Li, J., & Zhang, L. (2025). Evaluating Small Language Models for News Summarization. In Proceedings of NAACL 2025.
Kubli, A., et al. (2025). Generalization bias in large language model summarization of science news. Royal Society Open Science, 12(4), 241776.
Siddiqui, A. M., et al. (2024). Enhanced News Summarization Using Large Language Models and Advanced Prompt Engineering. International Journal of Advanced Computer Science and Applications.
Chen, Y., et al. (2024). A Multi-Stage Prompt Framework for High-Quality News Summarization Based on Large Language Models. Preprints.org manuscript 202412.1039.
Sun, Z., et al. (2025). An Evaluation of Large Language Models on Text Summarization. arXiv preprint arXiv:2507.05123.
Botev, A., et al. (2025). Unraveling the Capabilities of Language Models in News Summarization: Benchmarking Small Models. arXiv preprint arXiv:2501.18128.
Raj, S. K., et al. (2025). Comparative Analysis of Large Language Models for Abstractive Text Summarization in Technical News Articles. Procedia Computer Science.
Sadhukhan, A. (2025). Deep learning for text summarization using NLP for automated news extraction. Scientific Reports, 15, 20224.
Chen, L. (2025). A Study of Text Summarization Based on Large Models. Proceedings of the 2025 7th International Conference on Intelligent Information Processing.
Luo, Z., et al. (2023). ChatGPT as a Factual Inconsistency Evaluator for Abstractive Text Summarization. arXiv preprint arXiv:2303.15621.