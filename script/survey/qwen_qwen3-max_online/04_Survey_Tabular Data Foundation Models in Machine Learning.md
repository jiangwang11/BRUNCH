# 表格数据基础模型在机器学习中的研究进展（2022–2025）：综述

## 引言

表格数据，即以结构化行列形式组织的数值与类别混合特征，构成了工业界与科研中最为普遍的数据形态。尽管梯度提升树（如XGBoost、CatBoost）在该领域长期占据主导地位，但自2022年起，以基础模型（Foundation Models）为核心的新范式开始重塑表格数据的学习格局。这类模型通过在大规模合成或真实数据上进行预训练，旨在学习通用的数据分布先验，从而在下游小样本任务上实现“即插即用”（out-of-the-box）的高性能推理。本综述系统梳理了2022至2025年间在该方向的代表性工作，将其归纳为基于元学习的表格先验模型、基于大语言模型（LLM）的表格理解与生成、以及参数高效的深度集成模型三大类别，并总结其共性挑战与未来趋势。

## 方法分类与代表作

### 基于元学习的表格先验模型

该类方法通过在数百万个合成的小型表格数据集上进行元学习，训练一个能够“学会学习”的模型，使其在面对新任务时无需训练即可推理。

**TabPFN** [1] 是该类方法的开创性工作。其研究问题是在极小样本（≤10,000）且无需超参调优的场景下实现高性能预测。核心方法是基于Transformer架构，在由结构因果模型（SCM）生成的海量合成数据集上进行预训练，将预测任务建模为上下文学习（In-Context Learning）。其关键实验结论表明，TabPFN在2.8秒内于OpenML等基准上超越了经过4小时调优的CatBoost，并能处理回归、密度估计等任务。

**TabM** [2] 则重新审视了多层感知机（MLP）在表格学习中的潜力。其研究问题是如何在保持MLP简洁性的同时提升其性能与效率。核心方法是提出一种参数高效的集成策略，将多个MLP子模型集成在一个统一架构（TabM）中，通过BatchEnsemble的变体实现。实验表明，TabM在多个公共基准上不仅性能优于基于注意力的复杂模型（如SAINT、TabNet），且在推理效率上更具优势，证明了简单架构通过高效集成亦可成为强大的基础模型。

### 基于大语言模型（LLM）的表格理解与生成

随着LLM的兴起，研究者开始探索如何利用其强大的语义理解与生成能力来处理表格数据，主要分为理解与生成两个方向。

**HeGTa** [3] 聚焦于少样本下的**复杂表格理解**（TU）任务，如层次化表头的问答。其研究问题是如何在标注数据稀缺且表格结构复杂的情况下进行精准理解。核心方法是构建一个异构图（Heterogeneous Graph）来精确捕获表格中单元格、行、表头间的多层次关系，并将图编码器的输出作为软提示（soft prompt）注入LLM。实验在9个TU数据集上验证了其SOTA性能，尤其在保留原始复杂结构的WTQ（Raw）上，显著优于将表格线性化的基线，证明了结构信息建模的关键性。

**Tabby** [4] 则致力于**高质量表格数据合成**。其研究问题是如何利用LLM生成在统计特性上与真实数据难以区分的合成表格。核心方法是对标准Transformer LLM进行后训练修改，引入门控混合专家（MoE）机制，为表格的每一列分配专门的专家网络，以建模列间异质性。结合其提出的Plain训练技术，Tabby在六个真实数据集上生成的合成数据训练的下游模型，其效能（MLE）最高可比真实数据提升44%，显著优于传统合成方法。

**TableRAG** [5] 解决了LLM处理**超大规模表格**（百万token级别）的效率瓶颈。其研究问题是如何在不将整个大表输入LLM的前提下，实现高效准确的表格问答。核心方法是采用检索增强生成（RAG）框架，分别对表格的模式（schema）和单元格值进行独立的查询扩展与检索，并结合程序辅助求解器（Program-Aided Solver）进行数值推理。实验表明，TableRAG在ArcadeQA和BirdQA等大规模表格QA基准上，以更短的prompt长度取得了最高的准确率。

### 其他关键方向：表格数据增强与语言建模范式

**浙大TDA综述** [6] 系统性地梳理了表格数据增强（TDA）的技术脉络，特别是在生成式AI时代下的新进展。该工作将TDA流程划分为预增强、增强（基于检索/生成）和后增强三大阶段，并根据操作粒度（行、列、单元格、表）对70项工作进行了分类。其关键结论是，生成式AI（特别是LLM和扩散模型）正成为TDA的主流范式，并指出检索与生成方法的结合、TDA自动化是未来核心趋势。

**语言建模范式综述** [7] 则从宏观视角回顾了表格数据建模从传统MLP、预训练Transformer到利用PLM（如BERT）再到LLM的演进。该综述强调，直接从头预训练表格Transformer面临可扩展性问题，而利用现有PLM/LLM的知识迁移是更高效且性能更优的路径，并系统总结了数据处理、架构设计和训练目标等关键技术点。

## 实验与评价总结

对上述代表性工作的实验分析可归纳出几点共性结论：（1）**小样本优势**：TabPFN、HeGTa等方法在极小样本（k-shot, k≤32）场景下，其性能优势最为显著，验证了基础模型范式在数据稀缺场景下的巨大潜力。（2）**合成数据的有效性**：无论是作为预训练语料（TabPFN）还是作为下游任务的增强数据（Tabby），高质量的合成数据被证明能有效提升模型泛化能力，甚至超越真实数据。（3）**结构信息的重要性**：HeGTa等研究表明，在处理复杂表格时，显式建模单元格间的拓扑与层次关系，比简单的线性化或扁平化表示能带来显著的性能增益。（4）**效率与性能的权衡**：TabM的成功表明，对于许多表格任务，一个设计精巧的简单模型（如MLP）配合高效的集成策略，可以在性能与计算成本之间取得比复杂注意力模型更优的平衡。

## 趋势与挑战

基于2022–2025年的研究进展，可预测未来研究将聚焦于以下方向：

1.  **多模态表格理解与生成**：现实世界的表格常与图像、文本等多模态信息共存（如财报中的图表）。未来的模型将致力于融合这些异构信息，实现跨模态的联合推理与生成，如Multimodal Tabular Reasoning with Privileged Structured Information [8] 所初步探索的方向。

2.  **统一的表格基础模型（Universal Tabular FM）**：当前模型多针对特定任务（如分类、问答、合成）设计。构建一个能同时处理预测、理解、问答、合成、数据增强等多种任务的统一基础模型，是降低应用门槛、释放模型潜力的关键挑战。

3.  **可解释性、隐私与安全**：表格数据常涉及敏感信息，且决策过程需具备可解释性。如何在利用强大LLM的同时，保证合成数据的隐私安全（如通过差分隐私），并提供清晰的决策依据，将是工业落地的核心关切。浙大TDA综述 [6] 已明确指出此为未来五大机遇之一。

4.  **自动化与自适应**：从数据预处理、模型选择到后处理的全流程自动化（AutoML for Tabular FM），以及模型对数据漂移、概念漂移的自适应能力，将是提升模型鲁棒性和易用性的关键。

## 结论

2022–2025年是表格数据基础模型从概念萌芽到技术爆发的关键时期。以TabPFN、HeGTa、Tabby等为代表的创新工作，成功地将元学习、图神经网络、大语言模型等前沿技术引入表格领域，不仅在性能上挑战了传统方法，更开辟了小样本学习、数据合成、复杂结构理解等新范式。未来的研究将在多模态融合、模型统一化、以及可信AI（可解释、隐私、安全）等方向持续深入，推动表格数据这一基础数据形态的智能化处理迈向新高度。

## 参考文献

[1] Hollmann, N., Müller, S., Eggensperger, K., et al. (2022). TabPFN: A Transformer That Solves Small Tabular Classification Problems in a Second. *arXiv preprint arXiv:2207.01848*.

[2] Gorishniy, Y., Kotelnikov, A., & Babenko, A. (2024). TabM: Advancing Tabular Deep Learning with Parameter-Efficient Ensembling. *arXiv preprint arXiv:2410.12040*.

[3] Jin, R., Li, Y., Qi, G., et al. (2024). HeGTa: Leveraging Heterogeneous Graph-enhanced Large Language Models for Few-shot Complex Table Understanding. *arXiv preprint arXiv:2403.19723*. (To appear in AAAI 2025).

[4] Haldar, M., Bai, Y., Chavali, V., et al. (2024). Tabby: Tabular Data Synthesis with Language Models. *arXiv preprint arXiv:2401.05798*.

[5] Chen, S. A., Miculicich, L., Eisenschlos, J. M., et al. (2024). TableRAG: Million-Token Table Understanding with Language Models. *arXiv preprint arXiv:2410.04739*.

[6] Xu, T., Guo, C., Xu, X., et al. (2024). Tabular Data Augmentation for Machine Learning: Progress and Prospects of Embracing Generative AI. *arXiv preprint arXiv:2407.21523*.

[7] Ruan, Y., Lan, X., Ma, J., et al. (2024). Language Modeling on Tabular Data: A Survey of Foundations, Techniques and Evolution. *arXiv preprint arXiv:2408.10504*.

[8] Jiang, J. P., Xia, Y., Sun, H. L., et al. (2025). Multimodal Tabular Reasoning with Privileged Structured Information. *arXiv preprint arXiv:2506.04088*.

[9] Arik, S. O., & Pfister, T. (2021). TabNet: Attentive Interpretable Tabular Learning. *Proceedings of the AAAI Conference on Artificial Intelligence*.

[10] Somepalli, G., Goldblum, M., Geiping, J., et al. (2022). SAINT: Improved Neural Networks for Tabular Data via Row Attention and Contrastive Pre-Training. *arXiv preprint arXiv:2106.01342*.

[11] Zang, H., Huang, Z., Wang, Z., et al. (2024). Mambular: A Mamba-Based Architecture for Tabular Deep Learning. *arXiv preprint arXiv:2401.13540*.

[12] Cheng, Z., Wang, X., Zhang, Y., et al. (2021). HiTab: A Hierarchical Table Dataset for Question Answering and Natural Language Generation. *arXiv preprint arXiv:2108.06712*.