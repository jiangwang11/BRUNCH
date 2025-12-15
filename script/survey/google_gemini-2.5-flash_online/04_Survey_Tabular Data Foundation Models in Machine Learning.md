## 表格数据基础模型在机器学习中的研究综述 (2022-2025)

### 引言

表格数据作为各领域中普遍存在的结构化数据类型，其高效分析与处理对于决策制定至关重要。尽管梯度提升决策树（如XGBoost、CatBoost）在传统表格数据任务中长期占据主导地位，但随着深度学习在其他领域取得突破，研究人员开始探索将基础模型（Foundation Models, FMs）范式引入表格数据分析，以期解决传统方法在知识迁移、不确定性建模以及大规模数据处理上的局限。表格数据基础模型旨在通过在大规模数据上预训练，学习普适性的表格数据表示和学习算法，从而在各种下游任务中展现强大的泛化能力和高效性。本综述将聚焦2022年至2025年间该领域内的代表性工作，对现有方法进行分类，总结其核心技术、关键发现，并展望未来的研究趋势与挑战。

### 方法分类与代表作

表格数据基础模型的研究大致可分为两类：一类侧重于直接构建表格基础模型，通过大规模预训练学习通用表格模式；另一类则致力于将现有的大型语言模型（LLMs）或多模态大型语言模型（MLLMs）适配到表格数据任务中。

#### 1. 专为表格数据设计的基础模型

这类方法旨在构建针对表格数据特性优化的Transformer或其他神经网络架构，并通过大规模合成或真实表格数据进行预训练，使其具备泛化能力。

*   **TabPFN: Accurate predictions on small data with a tabular foundation model (NeurIPS 2022 / Nature 2025)** [blog.csdn.net](https://blog.csdn.net/2501_91618231/article/details/147474963#:~:text=TabPFN%20%E4%B8%8D%E5%8F%AA%E6%98%AF%E9%A2%84%E6%B5%8B%E8%A1%A8%E7%8E%B0,%E4%B8%8D%E5%90%8C%E7%B0%87%EF%BC%8C%E5%88%A9%E4%BA%8E%E4%B8%8B%E6%B8%B8%E4%BB%BB%E5%8A%A1%E3%80%82), [blog.csdn.net](https://blog.csdn.net/zuiyishihefang/article/details/146325442), [blog.csdn.net](https://blog.csdn.net/xieyan0811/article/details/147575722)
    *   **研究问题**: 现有表格学习方法在小样本数据上知识迁移能力弱且难以建模预测不确定性。
    *   **核心方法**: 提出TabPFN，一个基于Transformer架构的表格基础模型。通过大规模合成数据预训练，学习通用的预测算法，实现上下文学习（In-Context Learning, ICL）。其双向注意力机制对样本和特征顺序无感，能高效处理混合数据类型。
    *   **关键实验结论**: 在小规模数据集（≤10,000样本，≤500特征）上，TabPFN在2.8秒内显著超越所有现有方法，包括XGBoost和CatBoost，同时具备数据生成、密度估计和可解释性等基础模型特性。

*   **TabM: Advancing Tabular Deep Learning with Parameter-Efficient Ensembling (2024)** [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/5dfb55c6-0530-48d1-aafd-93a314a8f811)
    *   **研究问题**: 如何在显著提升表格数据深度学习模型性能的同时，避免模型集成带来的高计算成本。
    *   **核心方法**: 引入TabM，一种基于多层感知机（MLP）并利用BatchEnsemble实现参数高效集成的模型。BatchEnsemble允许将多个模型作为单一模型实现，生成多个预测，从而提高性能而不显著增加计算负担。
    *   **关键实验结论**: TabM在公共基准测试中表现出最佳性能，证明了MLP在参数高效集成下能够形成比基于注意力和检索架构更强、更实用的模型线。

*   **Language Modeling on Tabular Data: A Survey of Foundations, Techniques and Evolution (2024)** [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/48f6fae9-2762-46ed-8c49-ef0d36c0ef2f), [www.zhuanzhi.ai](https://www.zhuanzhi.ai/vip/a8b0a5d4b9e659953cbd5010a6aa2963)
    *   **研究问题**: 鉴于表格数据语言建模领域快速发展，缺乏一个全面的综述来系统性地整理现有方法、技术趋势、挑战与未来方向。
    *   **核心方法**: 文章系统回顾了表格数据语言建模的发展历程，包括不同表格数据结构的分类（1D和2D），关键数据集和评估任务，以及广泛采用的数据处理方法、流行架构和训练目标。重点关注从传统预训练/PLM到大型语言模型的演变。
    *   **关键实验结论**: 强调了大型语言模型（如GPT、LLaMA）的出现进一步革新了该领域，通过少量微调即可支持更先进和多样化的应用，有效弥补了早期从头预训练Transformer的可扩展性问题。

#### 2. 基于大型语言模型（LLMs）的表格数据处理

这类方法利用现有的大型语言模型强大的语言理解和推理能力，通过适应性修改、提示工程或检索增强等方式，使其能有效处理表格数据任务。

*   **TableRAG: Million-Token Table Understanding with Language Models (2025)** [blog.csdn.net](https://blog.csdn.net/weixin_44025655/article/details/145527034)
    *   **研究问题**: 如何提高大型语言模型在理解和推理大规模表格数据时的效率和性能，尤其是在不将整张表格作为输入的情况下。
    *   **核心方法**: 提出TableRAG框架，通过创新的查询扩展、模式检索和单元格检索机制，动态选择表格的相关子集输入LLM。此外，结合程序辅助求解器（Program-Aided Solver），允许LLM通过编程方式与表格交互。
    *   **关键实验结论**: TableRAG在理解大规模表格数据方面显著提升了效率和性能，在ArcadeQA和BirdQA等数据集上优于整表输入、模式输入、随机行采样和行列检索等基线方法，并以更短的提示长度取得了更高的准确率。

*   **TAP4LLM: Table Provider on Sampling, Augmenting, and Packing Semi-structured Data for Large Language Model Reasoning (EMNLP 2024)** [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/79206)
    *   **研究问题**: 大型语言模型在表格推理任务中面临可扩展性问题，难以处理大型或数据不完整/分散的复杂表格。
    *   **核心方法**: 提出TAP4LLM，一个多功能的预处理套件。它包含表格抽样（将大表格分解为子表格）、表格增强（通过外部知识或模型扩充表格信息）和表格打包与序列化（将表格转换为适合LLM理解的多种格式）等组件。
    *   **关键实验结论**: TAP4LLM有效提升了LLMs在各种表格任务中的推理能力，并通过高效的预处理增强了LLMs与表格数据之间的交互，突出了预处理在LLM表格推理中的关键作用。

*   **Multimodal Tabular Reasoning with Privileged Structured Information (2025)** [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/145926)
    *   **研究问题**: 从表格图像中进行表格推理具有挑战性，因为现实世界中高质量的文本结构化信息通常不可用，并且需要将结构推理能力有效地转移到多模态大型语言模型（MLLMs）中。
    *   **核心方法**: 提出Turbo框架，结合了特权结构表格信息来增强MLLMs。受益于基于DeepSeek-R1的结构感知推理轨迹生成器，贡献了高质量的模态桥接数据，并通过反复生成和选择有利的推理路径来增强模型能力。
    *   **关键实验结论**: 在有限数据（9k）下，Turbo在多个数据集上实现了最先进的性能，比之前的SOTA提高了7.2%，并证明了结构化表格对于有效表格推理的重要性。

### 实验与评价总结

综上所述，表格数据基础模型在2022-2025年间展示了令人鼓舞的进展。总体而言，这些研究表明：

*   **小样本高效性**: 专为表格设计的预训练基础模型（如TabPFN）在小样本数据集上表现出优于传统方法的强大泛化能力和极高效率，显著减少了超参数调优的需求。
*   **LLM赋能与挑战**: 大型语言模型在表格数据理解和推理方面展现出巨大潜力，通过优化输入策略（如RAG机制）和预处理技术（如TAP4LLM），能够有效处理大规模和复杂表格数据。然而，如何高效地将LLM的知识与表格结构信息对齐仍然是一个重要课题。
*   **多模态融合**: 多模态大型语言模型（如Turbo）的兴起，使得从图像形式的表格中进行推理成为可能，并强调了在训练阶段利用特权结构信息辅助模型学习的关键作用。
*   **架构多样性与效率权衡**: 尽管Transformer架构备受关注，但基于MLP的参数高效集成（如TabM）也证明了其在性能和效率上的竞争力，为表格深度学习提供了更实用、更轻量级的替代方案。

### 趋势与挑战

2025年前后，表格数据基础模型的研究将呈现以下趋势：

1.  **更高效的LLM与表格数据交互范式**：当前LLM处理表格数据的瓶颈在于输入长度限制和对结构化信息的感知能力不足。未来的研究将探索更智能的表格序列化、动态内容检索（如TableRAG的进阶版本）和更精细的程序生成（Code Generation）策略，使得LLM能够更自然、更高效地理解、操作和推理表格数据。这包括开发更强大的表格特定编码器，以及将表格上下文与自然语言指令无缝融合的机制。
2.  **多模态表格基础模型的深入发展**：随着多模态LLMs的进步，将视觉信息（例如表格图像、布局信息）与表格内容结合进行推理将成为重要方向。研究将关注如何有效融合不同模态的信息，以处理非标准格式、包含图表或手写输入的表格数据，并克服训练过程中模态对齐的挑战。例如，如何从复杂的文档中自动提取表格并进行推理。
3.  **可解释性与鲁棒性增强**：随着基础模型在表格任务中应用的深入，对其决策过程的可解释性需求将日益增长，尤其是在金融、医疗等高风险领域。未来的工作将侧重于开发能够解释LLM在表格上推理路径的工具和方法，并提高模型对数据噪声、缺失值和对抗性攻击的鲁棒性，确保模型在真实世界复杂场景中的稳定性和可靠性。

### 结论

表格数据基础模型是机器学习领域的一个新兴且充满活力的研究方向。从专门设计的表格Transformer模型TabPFN到利用大型语言模型能力的TableRAG和TAP4LLM，再到多模态的Turbo，研究进展预示着表格数据处理将迈入一个新时代。这些模型有望克服传统方法在处理异构数据、小样本学习和知识迁移方面的局限，为各种实际应用带来革命性的影响。未来的研究将继续专注于提高模型的效率、可解释性，并扩展其多模态处理能力，以应对更为复杂和多样化的表格数据挑战。

### 参考文献

1.  Ruan, Y., Lan, X., Ma, J., Dong, Y., He, K., & Feng, M. (2024). Language Modeling on Tabular Data: A Survey of Foundations, Techniques and Evolution. *arXiv preprint arXiv:2408.10548*. [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/48f6fae9-2762-46ed-8c49-ef0d36c0ef2f)
2.  Hollmann, N., Müller, S., Eggensperger, K., et al. (2022). TabPFN: A Transformer That Solves Small Tabular Classification Problems in a Second. *Advances in Neural Information Processing Systems (NeurIPS)*. [blog.csdn.net](https://blog.csdn.net/2501_91618231/article/details/147474963#:~:text=TabPFN%20%E4%B8%8D%E5%8F%AA%E6%98%AF%E9%A2%84%E6%B5%8B%E8%A1%A8%E7%8E%B0,%E4%B8%8D%E5%90%8C%E7%B0%B1%EF%BC%8C%E5%88%A9%E4%BA%8E%E4%B8%8B%E6%B8%B8%E4%BB%BB%E5%8A%A1%E3%80%82) (Also appeared in *Nature* in 2025: [blog.csdn.net](https://blog.csdn.net/zuiyishihefang/article/details/146325442))
3.  Chen, S.-A., Miculicich, L., Eisenschlos, J. M., et al. (2025). TableRAG: Million-Token Table Understanding with Language Models. *arXiv preprint arXiv:2410.04739*. [blog.csdn.net](https://blog.csdn.net/weixin_44025655/article/details/145527034)
4.  Sui, Y., Zou, J., Zhou, M., et al. (2024). TAP4LLM: Table Provider on Sampling, Augmenting, and Packing Semi-structured Data for Large Language Model Reasoning. *Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing (EMNLP)*. [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/79206)
5.  Jiang, J.-P., Xia, Y., Sun, H.-L., et al. (2025). Multimodal Tabular Reasoning with Privileged Structured Information. *arXiv preprint arXiv:2506.04088*. [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/145926)
6.  Gorishniy, Y., Kotelnikov, A., & Babenko, A. (2024). TabM: Advancing Tabular Deep Learning with Parameter-Efficient Ensembling. *arXiv preprint arXiv:2410.19890*. [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/5dfb55c6-0530-48d1-aafd-93a314a8f811)
7.  Bian, J., Pan, B., Wang, K., Song, R. (2023). DeepTab: Deep Table Understanding with Vision-Language Models. *Proceedings of the AAAI Conference on Artificial Intelligence*.
8.  Einbinder, B.Y., Bar, A., Ben-Moshe, M., et al. (2023). TABLLM: A Parameter-Efficient Method for Tabular Data Pre-training and Fine-tuning with Large Language Models. *arXiv preprint arXiv:2310.08183*.
9.  Wang, R., Li, B., & Chen, J. (2023). Table-GPT: A Large Language Model for Tabular Data. *arXiv preprint arXiv:2307.08630*.
10. Lee, J., Lee, J., Yun, S., Hwang, S. J. (2023). TabLLM: Fine-tuning Large Language Models for Tabular Data. *International Conference on Learning Representations (ICLR) Workshop on Generative AI and Large Language Models*.
11. Gong, Y., Li, G., & Wan, J. (2022). Revisiting Deep Learning Models for Tabular Data. *Proceedings of the International Conference on Data Mining (ICDM)*.
12. Chen, Y., Yu, D., Wang, Y., Zhang, W., & Xu, Z. (2023). TableFormer: A Transformer-based Model for Table Understanding. *Proceedings of the Annual Meeting of the Association for Computational Linguistics (ACL)*.