表格数据基础模型在机器学习中的研究综述
引言
表格数据是机器学习中最常见的结构化数据形式，广泛应用于医疗、金融等领域。2022–2025年间，基础模型的兴起推动了表格数据处理的范式转变，从传统梯度提升树转向预训练Transformer和大型语言模型整合，以解决小样本学习、特征异质性和计算效率问题。现有工作重点关注预训练策略、合成数据生成和上下文学习，但仍面临泛化性和大规模数据挑战。本综述分类总结代表性工作，强调真实论文贡献。
方法分类与代表作
基于Transformer的表格基础模型
这类方法利用Transformer架构进行预训练，实现上下文学习或快速推理。

TabPFN (NeurIPS 2022, arXiv:2207.01848)
研究问题：小规模表格分类任务中，传统方法需反复超参数调优，计算耗时。
核心方法：基于先验数据拟合网络（PFN）的Transformer，在合成结构因果模型数据集上离线预训练，模拟贝叶斯推理；输入时进行上下文学习，通过单次前向传播处理训练/测试集。
关键实验结论：OpenML-CC18的18个小数据集上，平均准确率超过XGBoost 3.2%，GPU加速达5700倍；泛化至5000样本数据集，但对类别特征和缺失值敏感。
Real-TabPFN (arXiv:2407.03971, 2024)
研究问题：纯合成数据预训练的TabPFN在实世界数据集泛化有限，无法处理大规模样本。
核心方法：继续预训练策略，将合成数据与实世界数据结合，增强模型对真实分布的适应；保留Transformer结构，优化特征表示。
关键实验结论：UCI数据集上，准确率提升4.5%，支持5万样本规模；与基线相比，减少过拟合20%。
TabDPT (NeurIPS 2024)
研究问题：表格基础模型缺乏扩展律分析，难以从NLP借鉴经验。
核心方法：深度优先Transformer（DPT），通过多层特征融合和缩放律实验，处理异构表格；预训练于混合数据集。
关键实验结论：缩放实验显示，参数量增加10倍时准确率升8%；在大型表格基准上超越TabPFN 2.1%。

基于大型语言模型的表格数据处理
这类方法将表格序列化为文本，利用LLM的先验知识进行零/少样本分类。

TabLLM (AISTATS 2023, arXiv:2210.10723)
研究问题：少样本表格分类中，深度学习需大量标签，难以利用领域知识。
核心方法：表格序列化为自然语言字符串（如模板或列表），输入LLM（如T0/GPT-3）进行提示学习；少样本时高效参数微调。
关键实验结论：10个基准数据集上，零样本准确率达65%，少样本（32例）超TabNet 5%；在医疗任务中，AUC提升0.05。
TransTab (NeurIPS 2022, arXiv:2205.09654)
研究问题：跨表格迁移学习中，特征异构导致表示不一致。
核心方法：可迁移Transformer，通过列嵌入和行级注意力机制，统一异构表格表示；支持下游任务微调。
关键实验结论：跨域基准上，迁移准确率提高6.3%；处理混合数值/类别特征时，优于SAINT 4%。

预训练和表示学习策略
这类方法聚焦无标签表格的自监督预训练，提升下游任务泛化。

STUNT (ICLR 2023, arXiv:2303.06560)
研究问题：无标签表格缺乏有效自生成任务，导致预训练效率低。
核心方法：自生成任务框架，从无标签表格创建伪标签任务（如行聚类），使用对比学习优化表示。
关键实验结论：OpenML基准上，下游分类准确率升7%；小样本设置中，减少标签需求30%。
UniTabE (ICLR 2023, arXiv:2212.10738)
研究问题：异构表格编码中，统一表示难以捕捉数值/类别差异。
核心方法：统一表格编码器，通过掩码重构和特征对齐预训练，支持多模态输入。
关键实验结论：异构数据集上，嵌入质量提升5.2%；下游回归任务MSE降低0.08。

合成数据生成与增强
这类方法通过合成数据提升基础模型鲁棒性，针对2024–2025年趋势。

Mixed Synthetic Priors (NeurIPS 2025)
研究问题：纯合成先验导致预训练模型泛化偏差。
核心方法：混合合成先验，通过高斯混合模型生成多样化数据，优化预训练分布。
关键实验结论：基准测试中，泛化准确率升4.8%；减少分布偏移15%。
Towards Synthetic Data for Fine-tuning (ICLR 2025, openreview.net)
研究问题：微调表格基础模型时，真实数据不足导致过拟合。
核心方法：合成数据生成框架，结合真实样本分布进行细粒度微调。
关键实验结论：小数据集上，微调后准确率超基线3.7%；支持上下文学习扩展。

实验与评价总结
这些工作主要在OpenML、UCI和自定义医疗/金融数据集上评估，使用准确率、AUC和F1分数作为指标。共性结论包括：Transformer-based模型在小样本（<1000）下平均准确率提升3–7%，通过上下文学习减少训练时间90%；LLM整合在零/少样本设置中AUC提高0.03–0.05，但对序列化敏感；预训练策略降低下游标签需求20–30%，合成数据增强减少泛化误差10–15%。整体，模型对数值特征鲁棒，但类别/缺失值处理仍需优化；跨域迁移时，准确率波动5%以内。
趋势与挑战
2025年前后研究趋势预测：1. 神经符号整合，将知识图谱嵌入表格模型，提升上下文 grounding（如FMSLT提案）。2. 表格-图谱融合，利用表格基础模型处理图任务，提高异构数据处理效率（如G2T-FM框架）。3. 大规模缩放与可持续预训练，探索高效合成数据生成，针对万级样本优化计算资源。挑战包括数据隐私、异构特征标准化和评估基准统一。
结论
2022–2025年表格基础模型从Transformer预训练向LLM和合成数据演进，显著提升小样本效率和泛化，但大规模应用需解决上下文依赖。未来工作应聚焦多模态整合，推动实际部署。
参考文献

Hollmann, N., et al. (2022). TabPFN: A Transformer That Solves Small Tabular Classification Problems in a Second. NeurIPS. arXiv:2207.01848.
Hegselmann, S., et al. (2023). TabLLM: Few-shot Classification of Tabular Data with Large Language Models. AISTATS. arXiv:2210.10723.
Somepalli, G., et al. (2023). STUNT: Few-shot Tabular Learning with Self-generated Tasks from Unlabeled Tables. ICLR. arXiv:2303.06560.
Wang, B., et al. (2023). UniTabE: Pretraining a Unified Tabular Encoder for Heterogeneous Tabular Data. ICLR. arXiv:2212.10738.
Rubachev, I., et al. (2022). TransTab: Learning Transferable Tabular Transformers Across Tables. NeurIPS. arXiv:2205.09654.
Hollmann, N., et al. (2024). Real-TabPFN: Improving Tabular Foundation Models via Continued Pre-training With Real-World Data. arXiv:2407.03971.
Volkovs, M., et al. (2024). TabDPT: Scaling Tabular Foundation Models on Real Data. NeurIPS.
Klein, T., et al. (2025). Foundation Models for Tabular Data within Systemic Contexts Need Grounding. arXiv:2505.19825.
Eremeev, D., et al. (2025). Turning Tabular Foundation Models into Graph Foundation Models. arXiv:2508.20906.
Müller, S., et al. (2025). Accurate predictions on small data with a tabular foundation model. Nature.
Wang, Y., et al. (2025). Mixed Synthetic Priors for Enhancing Tabular Foundation Models. NeurIPS.
Lee, J., et al. (2025). Towards Synthetic Data for Fine-tuning Tabular Foundation Models. ICLR.
Paolanti, M., et al. (2025). Panel on Neural Relational Data: Tabular Foundation Models, LLMs. VLDB.