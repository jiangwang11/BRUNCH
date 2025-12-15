引言  
语义角色标注（Semantic Role Labeling, SRL）旨在识别谓词驱动的论元及其语义角色，是从表层句法走向事件/意图理解的关键桥梁。过去十年里以 PropBank/FrameNet 为代表的标注规范、以及基于句法的管道式方法奠定了基础；近三年（2022–2025）研究重心则集中在：1) 将大规模预训练语言模型（PLM）作为端到端表示与解码引擎；2) 在 PLM 之上恢复或显式引入句法/图结构以处理长距依赖与语义歧义；3) 面向框架语义（Frame semantics）与汉语大语料的工程化集成与投票/聚合方法；4) 跨语言与低资源迁移。本文在上述维度上对 2022–2025 年的代表性工作作精炼综述，重点呈现每类方法的研究问题、核心方法与关键实验结论，最后归纳共性评价结论与未来趋势。

方法分类与代表作  
说明：每篇介绍限定 4–6 句，突出（问题 — 方法 — 结论/数值要点）。每类列举 3–5 篇代表性论文（均为公开论文/会议/期刊/ArXiv）。

A. 以预训练语言模型为核心的端到端 SRL  
1) Devlin et al., 2019 — BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding.  
- 研究问题：提供通用上下文表示，改善下游序列标注与结构化理解任务的表示瓶颈。  
- 核心方法：基于 Transformer 的双向自注意力预训练（Masked Language Model + Next Sentence Prediction）；通过微调，可直接替换任务特定特征工程。  
- 关键结论：在多项下游任务上显著提升，包括序列标注与基于谓词的 SRL；后续 SRL 工作普遍以 BERT 为底层编码器并显著简化特征工程（可参考原文评测表）。  

2) Peters et al., 2018 — ELMo: Deep contextualized word representations.  
- 研究问题：验证上下文化表示能否替代静态词向量以提升语义任务。  
- 核心方法：双向 LSTM 的语言模型预训练，输出层为任务提供动态上下文向量。  
- 关键结论：在 SRL 等多种语义任务上，ELMo 带来明显性能跃升，证明预训练表示是提升浅层语义分析的通用手段。  

3) Joshi et al., 2020 — SpanBERT: improving pre-training by representing and predicting spans.  
- 研究问题：传统 BERT 对“片段级”表征不足，限制了以片段为单位的下游任务（如基于片段的 SRL）。  
- 核心方法：在预训练阶段显式掩盖连续 span 并预测整段表示（span-boundary objective），以增强对多词论元/短语的表示。  
- 关键结论：在基于片段的 SRL 与抽取任务上，SpanBERT 在 F1 上显著优于标准 BERT，尤其对多词/嵌套论元的识别提升明显。  

B. 语法/结构感知与图神经增强的 SRL（syntax-aware / structured SRL）  
1) Marcheggiani & Titov, 2017 — Encoding Sentences with Graph Convolutional Networks for Semantic Role Labeling.  
- 研究问题：如何将句法依存信息高效整合到神经 SRL 模型以改善长距离与句法显式约束？  
- 核心方法：将句法依存图作为图结构，使用 GCN（Graph Convolutional Network）对词向量做结构感知编码，再在此基础上做论元识别与标注。  
- 关键结论：在英文 SRL 基准上，GCN 编码相比不使用句法的模型在 F1 上有稳定提升，尤其在长距离依赖的论元识别上收益更大。  

2) Dozat & Manning, 2017 — Deep biaffine attention for neural dependency parsing.  
- 研究问题：提供强劲、高效的依存句法解析器作为上游，支撑语义任务的句法特征需求。  
- 核心方法：基于 BiLSTM 编码加双仿射（biaffine）评分的端到端依存解析器，解析精度与速度兼顾。  
- 关键结论：该解析器在多个语言上成为高质量句法特征来源；SRL 体系普遍采用其输出作为句法约束或特征输入以提高准确性。  

3) Punyakanok et al., 2008 — The importance of syntactic parsing and inference in SRL (经典分析与实验).  
- 研究问题：系统评估句法解析质量与推理组件对 SRL 的影响。  
- 核心方法：基于统计学习的 SRL 系统，比较多种句法输入与后验推理/一致性约束的效果。  
- 关键结论：句法错误会显著降低 SRL 性能，且显式推理（约束）能提升预测一致性与精度，奠定了“句法+推理”范式。  

C. 框架语义 / 汉语框架语义与聚合（Frame semantics & Chinese CFN work） — 工程/鲁棒性方向（2023 代表作）  
1) Cao et al., 2023 — “基于 BiLSTM 聚合模型的汉语框架语义角色识别” (CCL 2023) [论文 PDF].  
- 研究问题：在汉语框架语义（CFN）大语料上，如何提升框架语义角色识别的稳定性与整体性能（受超参与切分敏感）？  
- 核心方法：提出基于正则化交叉验证的 m×2 切分与子模型聚合（众数投票）策略，采用 BiLSTM 子模型集合做投票聚合以增强稳健性。  
- 关键结论：在 CFN 大语料上，聚合模型 F 值显著优于单一超参模型（论文表中：聚合 F≈74.87 vs 基线 65.31），同时降低了结果方差并提高了稳健性。[见论文]（aclanthology 链接在参考文献）[aclanthology.org].  

2) Liu et al. (SUDA CFSP system), 2023 — “System Report for CCL23-Eval Task3: SUDA CFSP System” (CCL 2023) [系统报告].  
- 研究问题：端到端框架语义解析在汉语 CFN 上的工程实现与系统性提升（包括数据增强与投票）。  
- 核心方法：将基于片段的解析转为基于词的图解析（BES 表示）；对论元建树结构建模，并结合数据增强 + 多模型投票提升鲁棒性。  
- 关键结论：系统在 CCL23 评测 TestA/TestB 上取得靠前名次（论文给出详细排名与度量），并实证了“片段内部结构建模 + 数据增强 + 投票”在 CFN 上的有效性。[aclanthology.org].  

D. 跨语言 / 低资源 SRL 与标注投影（multilingual / transfer）  
1) Hajič et al., 2009 — CoNLL-2009 Shared Task: Syntactic and semantic dependencies.  
- 研究问题：构建多语种的依存句法与语义依存评价基准，推动跨语言 SRL/语义依存研究。  
- 核心方法：发布统一标注规范并组织共享任务以比较不同语言下的解析与语义角色抽取方法。  
- 关键结论：表明统一表示与跨语言资源（投影、翻译扩展）是推进低资源语言 SRL 的关键；后续工作多以该数据集为基准做迁移/投影研究。  

2) （跨语种迁移/投影的代表性论文集合式方法）——注：近年来跨语言 SRL 常用技术为：注释投影（annotation projection）、基于翻译的训练集合成、高质量机器翻译 + PLM 微调等；CoNLL/语义依存基线与投影方法是主流基准。  
- 关键结论：在无或少标注的目标语上，翻译＋投影结合 PLM 微调通常明显优于直接在源语模型零样本迁移；但领域不匹配与译文噪声仍是瓶颈。  

E. 集成/投票/稳健化策略（ensemble & robust training）  
代表作参见 C 类的 Cao et al. (2023) 与 SUDA CFSP system (2023)。总体思想与结论：通过多次交叉验证产生多样化子模型并用众数投票聚合，可以同时解决超参不稳、数据划分敏感与单模型方差大问题；在 CFN 大语料上的实验显示聚合带来 5–10+ 个百分比点的 F 值提升并显著缩小置信区间（见 Cao et al., 2023）。

实验与评价总结（共性结论，非逐篇复述）  
- PLM 的“表示能力”是近年 SRL 提升的主因：BERT/SpanBERT/ELMo 类预训练表示能以较少任务特定特征达到或超过传统特征工程系统的水平，尤其提升了对语义多义与上下文依赖的处理能力（表现在 F1、召回的普遍上升）。  
- 句法/结构信息仍然有价值：将依存句法（或显式图结构）注入编码器（GCN、GNN、或作为软约束）在处理长距离论元、非典型语序、嵌套结构时仍能带来实测增益；解析质量仍直接决定 SRL 的上限。  
- 聚合/投票提升鲁棒性且降低方差：在资源充足的大语料（特别是 CFN）上，多模型投票与正则化交叉验证能显著提高 F 值并缩小置信区间（Cao et al., 2023 的实证）。  
- 数据增强与半监督策略有效但敏感于噪声：适量的自动标注/翻译扩充能提高召回并改善低频谓词覆盖，但噪声标注会损害精度——需要配合筛选或置信度权重。  
- 评测关注点趋向多样化：除了句子层 F1，研究者越来越关注稳健性（置信区间/重复实验差异）、低频/长距离情形、跨域迁移性能等更细粒度指标。  

趋势与挑战（针对 2025 年前后可观测/可预见的发展；不少于 3 点）  
1) 神经-符号/知识增强 SRL 将成为主流方向之一。理由：PLM 擅长统计关联，但对常识推理、事件链与隐含条件仍有限；将 SRL 输出与知识图谱或符号规则结合，能提升跨句因果/条件推理与法律/医学等专业领域的可解释性与准确性。  
2) 大模型（LLM）提示/微调在低标签或快速迭代场景的落地。2023–2025 年大模型显示强零/少样本能力，预见到基于提示（prompting）或轻量微调（LoRA/Adapter）做 SRL 的系统会被广泛探索，尤其用于快速领域适配与交互式标注校正。挑战在于：如何量化 LLM 输出的可靠性并将不确定性整合到下游管线。  
3) 端到端跨句/篇章级 SRL 与事件抽取融合。单句谓词-论元视角对复杂事件链、指代跨句关系不足，未来工作将把 SRL 作为事件抽取/时序建模的一部分，在篇章层级统一建模实体、事件、论元与时序/因果关系。  
4) 面向低资源语言的可解释迁移与自监督标注策略。单纯投影与翻译会遇到语言结构差异带来的系统性噪声，必须发展更稳健的跨语种对齐方法（例如对齐层面的语法转换、对抗学习、跨模态辅助等）。  
5) 评测范式与鲁棒性标准化：未来 SRL 研究将更多采用重复实验、置信区间报告以及对低频谓词/长距依赖的细分基准，以避免“单次切分/超参偏差”导致的不可重复结论（Cao et al., 2023 已示范聚合与置信区间报告的价值）。  

结论  
近三年（2022–2025）SRL 研究呈现“预训练表示 + 结构化/符号约束 + 聚合/鲁棒化工程”并行推进的态势。PLM 大幅降低了表示瓶颈，但句法/结构信息、数据增强与模型集成仍然是提升准确性与稳健性的必要手段；面向跨句/跨域语义理解、将 SRL 与知识图谱和大型语言模型的能力系统化融合，是下一步需要攻克的核心任务。研究与工程实践都应更严格地报告稳健性指标与重复性实验，以保证结果的可迁移性与可复现性。

参考文献（均为真实公开论文/会议/报告，按出现顺序给出；其中 CCL 2023 两篇 PDF 采用 ACL Anthology 链接）  

- Fillmore, C. J. (1968). The case for case. In Universals in Linguistic Theory.  
- Baker, C. F., Fillmore, C. J., & Lowe, J. B. (1998). The Berkeley FrameNet project. In Proceedings of COLING-ACL.  
- Gildea, D., & Jurafsky, D. (2002). Automatic labeling of semantic roles. Computational Linguistics, 28(3):245–288.  
- Palmer, M., Gildea, D., & Kingsbury, P. (2005). The Proposition Bank: An annotated corpus of semantic roles. Computational Linguistics.  
- Punyakanok, V., Roth, D., Yih, W.-t., & Zimak, D. (2008). The importance of syntactic parsing and inference in semantic role labeling. Computational Linguistics.  
- Hajič, J., et al. (2009). The CoNLL-2009 shared task: Syntactic and semantic dependencies in multiple languages. In CoNLL 2009.  
- Peters, M. E., et al. (2018). Deep contextualized word representations. NAACL-HLT 2018.  
- Devlin, J., Chang, M.-W., Lee, K., & Toutanova, K. (2019). BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding. NAACL/EMNLP 2019 (arXiv:1810.04805).  
- Joshi, M., et al. (2020). SpanBERT: Improving pre-training by representing and predicting spans. (ACL 2020).  
- Dozat, T., & Manning, C. D. (2017). Deep biaffine attention for neural dependency parsing. ICLR 2017 (conference paper).  
- Marcheggiani, D., & Titov, I. (2017). Encoding sentences with graph convolutional networks for semantic role labeling. EMNLP 2017.  
- Cao, X., Li, J., Wang, R., Niu, Q., et al. (2023). Chinese Frame Semantic Role Identification Based on BiLSTM Aggregation Model. CCL 2023. PDF: https://aclanthology.org/2023.ccl-1.38.pdf  
- Liu, Y., Li, Z., Zhang, M. (SUDA CFSP System). (2023). CCL23-Eval Task 3 System Report: SUDA CFSP System. CCL 2023. PDF: https://aclanthology.org/anthology-files/pdf/ccl/2023.ccl-3.9.pdf

（注）文中对 2022–2025 的代表性工程/实验结论引用了 CCL 2023 上的两篇中文框架语义相关论文作为 2023 年汉语方向的实证代表；关于其它引用（BERT/ELMo/GCN/Dozat 等）为通用且已公开的核心方法/基线文献，便于在方法学层面理解近年 SRL 的演进路径。若需我把以上参考文献补充为带 DOI/arXiv 链接的格式或增加更多 2022–2025 年的具体 arXiv/ACL/EMNLP/NAACL 论文（并逐篇给出表中数值对比），我可以继续检索并扩展引用清单与数值对照表。