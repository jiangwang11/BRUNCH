# 表格数据基础模型在机器学习中的应用：2022-2025年综述

表格数据（Tabular Data）作为当今数据科学中最普遍的数据类型之一，广泛应用于金融、医疗、电商等关键领域。传统上，梯度提升决策树（GBDT）如XGBoost、CatBoost和LightGBM等方法在表格数据上占据绝对优势达二十余年[9]。然而，近年来深度学习方法的突破，尤其是表格数据基础模型（Tabular Foundation Models, TFMs）的出现，开始挑战这一传统格局。本综述系统回顾了2022-2025年间表格数据基础模型的主要进展，涵盖五大核心方法族系：上下文学习型基础模型、Transformer多元架构、扩散与生成模型、预训练语言模型以及专用神经网络架构。通过统一的实验评估框架，我们指出当前研究的共性结论与差异，并预测了该领域在2025年前后的发展趋势，包括可扩展性突破、语义理解深化与模型异构融合的技术方向。

## 表格数据学习的核心挑战与基础模型的必要性

表格数据相较于图像、文本等非结构化数据，在深度学习框架下面临独特的系统性挑战。表格数据的异质特性表现为特征类型的混杂——包含连续数值特征与离散类别特征、特征间缺乏预定义的空间或序列关系、样本间基本无内部结构可言[2][7]。这些特点使得为图像与文本设计的通用深度学习架构（如卷积网络与自注意力机制）无法直接高效应用，导致深度学习在表格数据上的表现长期滞后于传统树模型。

传统GBDT方法的优势在于其对特征交互的隐式建模、对类别变量的原生处理能力与较少的超参数调整需求。然而这类方法存在本质限制：它们必须为每一新数据集单独训练，无法实现跨任务迁移学习；参数优化往往耗时数小时至数天；难以融入多模态学习管道[1][32]。基础模型的核心理念在于通过大规模预训练实现一次构建、多次应用，这正是表格数据学习亟待破局的关键。近年涌现的表格数据基础模型通过在数百万合成任务或真实表格语料库上进行预训练，学习通用的学习算法元知识，从而能在推理时以单次前向传播完成新表格的预测，并展现出相比GBDT数倍至千倍的速度优势[1][43][46]。

## 表格数据基础模型的方法体系与代表性工作

### 上下文学习型基础模型

上下文学习（In-Context Learning, ICL）范式代表了表格数据基础模型的前沿突破。该范式的核心思想是将训练数据作为模型输入的上下文，在单次前向传播中完成学习与预测，无需参数更新。这一思路借鉴了大规模语言模型的成功经验，但针对表格数据的特殊性进行了架构创新。

**TabPFN（Tabular Prior-data Fitted Network）**[1][55]系列是该方向最具影响力的工作。TabPFN在包含特征缩放变化、缺失值、噪声等多种数据挑战的数百万合成数据集上进行预训练，使模型学习到处理此类问题的策略。在推理时，输入包含标签训练样本和无标签测试样本，模型在2.8秒内完成分类任务，性能超过调优4小时的CatBoost，速度提升达5,140倍[1]。该模型支持密度估计、数据生成、可复用嵌入学习等基础模型特性，表明通过在合成任务空间进行元学习可以有效开发通用算法[1]。

**TabICL（Tabular In-Context Learning）**[43][46]针对TabPFN面临的可扩展性瓶颈进行突破。TabPFNv2的交替列行注意力设计在处理大规模表格时计算成本陡增，而TabICL通过两阶段架构解决此问题：先采用列-行注意力机制构建固定维度的行嵌入表示，随后通过Transformer进行高效的上下文学习。在60K样本预训练数据与500K生产表格的处理能力上，TabICL保持与TabPFNv2相当的精度同时快10倍，在超10K样本数据集上显著超越TabPFNv2与CatBoost[43][46]。这表明ICL范式的可扩展性突破使其能真正适应现实工业规模表格数据。

**TabM与其他ICL变种**[49][58]进一步探索了该方向的设计空间。研究表明，在统一评估框架下（68个数据集，严格交叉验证），TabICL与TabPFNv2在平均排名上显著领先所有其他方法，而简单前馈网络（TabM、RealMLP）的表现略逊，但仍超越所有基于微调的基础模型变种[49][58]。这一发现挑战了关于注意力机制必然性的常见假设。

### Transformer多元架构体系

Transformer架构的引入为表格数据表示学习带来了灵活的特征交互建模能力，催生出一系列微调式（而非上下文学习式）的架构创新。

**FT-Transformer（Feature Tokenizer Transformer）**[32][39]通过特征分词机制将数值和类别特征统一映射到嵌入空间，随后输入Transformer编码器进行上下文化表示学习。该架构在11个基准数据集上的表现超越其他深度学习方法，已成为Transformer类方法的标准基准[32]。其核心贡献在于证明了简洁的特征标记化加标准Transformer就足以形成强有力的表格学习基线，避免了过度复杂设计。

**TabTransformer**[33][36]采取不同的融合策略：仅对类别特征应用Transformer进行上下文嵌入学习，数值特征保持原始形式，两者连接后输入MLP。该设计基于"数值特征的连续性不需要注意力建模"的假设。实验表明TabTransformer对缺失值与噪声特征具有鲁棒性，且可解释性优于纯Transformer方案，但在某些高维数据集上不如FT-Transformer[33]。

**SAINT（Self-Attention and INtersample attention Transformer）**[19][22]引入了行级注意力机制，在特征内部（行内）自注意力基础上增加跨样本（行间）注意力。这种双层注意力设计假设样本间的相似性信息对分类有帮助，类似于可学习距离度量的最近邻方法。在30个数据集对比中，SAINT的行间注意力变体在高维数据（特征>500）上表现尤为突出[19]。该架构证明了将关系型数据中的行维度显式建模为学习对象的可行性。

**Mambular**[15]适配了状态空间模型（SSM）架构Mamba用于表格数据，将特征序列化处理。初步结果表明Mambular在多数基准上与FT-Transformer性能相当甚至略优，同时参数量更少，为表格学习提供了新的架构选择[15]。

### 生成与扩散模型

扩散与生成模型为表格数据的合成、缺失值填充与数据增强提供了新思路。

**TabDDPM**[13]首次将扩散概率模型系统应用于通用表格数据生成，设计了混合连续-离散特征的去噪机制。相比GAN与VAE基线，TabDDPM在生成真实度与多样性上取得显著改进，且天然支持隐私保护场景的合成数据生成[13]。这项工作证明了扩散框架作为表格生成范式的通用性与优越性。

**GReaT（Generation of Realistic Tabular data）**[26]利用预训练的自回归语言模型（如GPT-2）进行表格数据生成。通过序列化表格为文本（行序列化）并进行条件采样，GReaT实现了端到端的表格生成。该方法的关键创新在于将表格生成任务转化为文本生成问题，充分利用语言模型的预训练知识[26]。

**GReaTER（Generate Realistic Tabular data after Enhancement and Reduction）**[29]在GReaT基础上进行改进，通过数据语义增强系统提升LLM对表格数据的理解，采用跨表连接方法处理多表数据。实验表明GReaTER相比GReaT在合成数据保真度上有显著提升，特别是在多表场景下[29]。这反映了表格生成中语义理解的重要性。

**TAPTAP（Table Pre-training for Tabular Prediction）**[8]采用混合策略：在预训练阶段收集450个公开表格数据集构建语料库，使用文本编码与生成策略进行预训练；在微调时产生高质量合成表格协助实际预测模型训练。TAPTAP的设计解耦了预训练与骨干模型架构，使其能适配不同下游学习器[8]。

### 预训练语言模型方向

预训练语言模型为表格数据引入了符号与语义的联合理解能力。

**TaBERT（Table BERT）**[14][17]是首个联合预训练自然语言句子与表格结构的模型。在26百万个表格及其英文上下文的语料库上进行预训练，TaBERT学习表格行列单元的分布式表示。采用水平自注意力（行内单元依赖）与垂直自注意力（列间依赖）的混合机制，以及内容快照策略处理大规模表格的计算瓶颈[14]。在弱监督语义解析任务（WikiTableQuestions）上取得新的最优结果[14]。

**PTab（Pre-trained Model for Tabular data）**[25][28]通过三阶段处理学习表格的上下文表示：模态变换（表格→文本）、掩码语言微调、分类微调。初始化使用预训练的文本语言模型（如BERT），在微调阶段充分利用大规模文本预训练知识。PTab在8个表格分类数据集上相比XGBoost达成更高的AUC，且具备实例级可解释性[25]。

**TableLLM**[44][47]是专用于表格操作任务的8B参数LLM，针对文档嵌入与电子表格嵌入两种实际场景设计。采用远距离监督方法进行训练，包含推理过程扩展与交叉验证策略确保自动生成数据质量[44]。在电子表格场景超越GPT-4o，文档场景与GPT-4o性能相当[44]，展现了任务特定预训练的优势。

### 专用神经网络架构

**TabNet**[31]采用顺序注意机制进行实例级特征选择，每个决策步骤动态选择当前需处理的特征子集。这种设计既继承了树模型的可解释性与特征稀疏性，又借鉴了深度学习的端到端表示学习[31]。实验表明TabNet在多个基准上超越其他神经网络与决策树变体，但相比最新的基础模型仍有差距。

**GANDALF（Gated Adaptive Network for Deep Automated Learning of Features）**[57]提出门控特征学习单元（GFLU），将GRU机制创新性地适配用于非时序表格数据，在每一阶段学习阶段特定的特征掩码实现自适应特征选择。在TabBench与TabSurvey基准上GANDALF表现与GBDT相当，参数与计算效率优于注意力模型[57]。

**TabCaps（Tabular Capsule Network）**[20][23]采用胶囊网络范式处理表格数据，将异构特征值封装为向量特征表示。设计基于词袋模型的路由算法（BoW Routing）降低计算复杂度，在对偏差与小数据集具有鲁棒性方面展现优势[20][23]。

## 实验评估与共性发现

### 评估框架与数据集

当前表格数据模型评估已形成相对统一的框架。主流基准包括AutoML Benchmark（29个分类+28个回归数据集，样本数≤10K）、OpenML-CTR23与TALENT-300[1][5][49]。为确保公平性，规范的评估通常采用10次重复交叉验证、多折交叉验证超参数优化（时间预算30秒至4小时）、统一的CPU/GPU配置[1][49]。这些设计决定对最终模型排名有显著影响。

### 性能阶层与统计显著性

综合分析68-200个基准数据集的结果表明，当代表格学习方法形成了清晰的性能阶层[49][58]：

**第一梯队**（显著领先）：TabICL与TabPFNv2（上下文学习型基础模型）在平均排名上超越所有竞争者，二者无显著统计差异，表明ICL范式在表格学习中已确立优势地位。

**第二梯队**：TabM（简单MLP+良好正则化）、CatBoost、XGBoost排名接近，相比第一梯队性能差距不显著。RealMLP与标准MLP在充分调优后表现也位于此梯队，挑战了"需要复杂注意力机制"的常见假设。

**第三梯队**：FT-Transformer等单纯微调的Transformer模型，SAINT、TabTransformer在此位置，虽超越特定领域的模型但不及ICL与简单MLP。

**第四梯队及以下**：微调式基础模型（XTab、CARTE、TP-BERTa）表现最差，甚至不如TabNet，表明基础模型的微调策略对表格任务的适配度不足。

### 超参数优化与数据集特性的影响

关键发现表明超参数优化的方向与幅度对不同方法作用差异巨大[49][58]：仅TabM、RealMLP、SAINT、XGBoost、XTab在优化后的排名相比基线有改进，其他方法改进幅度微弱。这表明虽然通用的优化可提升绝对性能，但模型间的相对排名格局相对稳定。

缺失值处理、类别特征数量、特征维度等数据集特性对模型选择有实际指导意义：TabPFN在处理缺失值上鲁棒性最优；SAINT在高维数据（>500特征）上相对优势明显；CatBoost在原生类别处理上仍最高效[1][5]。

### 计算成本-性能权衡

**推理速度**：TabPFN与TabICL的单次前向传播（2.8-10秒）相比CatBoost训练+推理（数分钟至数小时）有压倒性优势。即使考虑GPU代价，ICL模型的成本-效益比优越。

**训练代价**：TabPFN/TabICL的预训练是一次性投入（企业/研究机构级），下游任务无训练成本，而GBDT与微调式基础模型每次新任务需重新计算。在频繁新任务场景中ICL型基础模型优势显著。

**模型大小**：TabPFN (1.2B参数)、TabICL体量相近，相比GBDT集成或传统神经网络具有内存效率，但仍需GPU加速以达到实用推理速度。

## 2025年前后的研究趋势与开放挑战

### 趋势一：可扩展性与长序列建模的深度突破

TabICL突破10K样本瓶颈至500K可处理规模[43][46]标志着ICL范式正从小规模应用向大规模工业场景演进。**预期的技术方向**包括：（1）效率更高的序列建模机制，如基于稀疏注意力或状态空间模型（Mambular已初步验证[15]）；（2）多层次分层表示学习，将大规模表格分解为可管理的子单元；（3）增量式上下文学习，支持流式新数据的在线适应。预计2025年将涌现处理百万级样本的实用基础模型。

### 趋势二：语义理解与符号推理的融合

TaBERT、PTab、GReaTER等工作的共同启示是**表格数据的语义维度（列名、数据类型、单位、定义域）对模型理解的关键作用**[14][25][29]。当前大多数模型将表格视为无信息的数值矩阵，忽视了数据的符号语境。**预期的研究方向**：（1）多模态预训练框架，联合表格结构、自然语言元数据与知识图谱；（2）显式的本体学习与类型推断模块；（3）跨领域知识迁移机制，利用领域知识库增强泛化性。TABLELLM在办公场景的成功案例表明这一方向的实用价值[44]。

### 趋势三：模型异构融合与任务自适应

单一架构的通用性有限。**新兴的融合思路**包括：（1）集成上下文学习模型与树模型的混合方案，利用两者的互补优势；（2）动态架构选择，根据数据特性自动选用TabPFN、GBDT或简单MLP；（3）多任务学习框架（如最近提出的MultiTab[56]），在关联表格集合上同步学习，利用任务间结构关系。预计此方向将结合AutoML技术形成端到端的自适应系统。

### 挑战一：评估框架的代表性与公平性

现有基准的局限性日益凸显：（1）AutoML Benchmark限于≤10K样本，未覆盖实际工业规模；（2）数据集构成的多样性不足，某些特殊场景（如极端类别失衡、高缺失率）代表性弱；（3）超参数优化配置的不一致性导致模型间比较不公平[49][58]。**未来需要**：（1）构建包含百万级样本的开放基准集（TabICL论文已体现此趋势[43]）；（2）标准化评估协议与轻量级评估平台；（3）针对特定应用场景的垂直基准（医疗表格、金融时间序列表格等）。

### 挑战二：理论理解的缺失

虽然实证结果丰富，但对以下问题的理论说明仍然不足：（1）为何ICL在表格任务上有效？其与梯度学习的根本差异何在？（2）表格数据的内在可学性（learnability）约束是什么？（3）不同架构的归纳偏置（inductive bias）对表格特性的适配程度如何量化？**理论突破**将有助于指导下一代模型设计。

### 挑战三：可解释性与鲁棒性的对立

基础模型往往追求性能而牺牲可解释性。表格数据在金融、医疗等风险敏感领域的应用对模型透明度有硬性要求。**该领域的关键问题**：（1）如何在基础模型框架下保留TabNet式的特征选择可解释性？（2）对抗性鲁棒性评估体系的构建——当前工作多关注自然分布漂移，对精心设计的攻击防御薄弱；（3）数据隐私保护与模型性能的平衡（如差分隐私合成数据生成）。

## 结论

表格数据基础模型在2022-2025年间的发展已证明深度学习可以在这一传统上被GBDT统治的领域取得突破。上下文学习范式（TabPFN、TabICL）通过预训练元学习实现了单次前向传播的通用预测，达成了相比传统方法数倍至千倍的速度提升；Transformer多元架构（FT-Transformer、SAINT）通过灵活的特征交互建模彰显了深度学习的表示学习优势；生成模型与预训练语言模型为数据合成、缺失值处理与跨模态理解开辟了新路径。

然而，当前工作尚存显著局限：可扩展性虽有突破但仍未达工业规模数据集的通用化；模型的语义理解能力相比符号方法仍浅；单纯的微调式基础模型适配不足表明并非所有预训练策略都适用表格任务。在评估维度上，标准化基准与理论深度均有待提升。

**未来三至五年的研究重点应聚焦于**：（1）百万级样本与流式数据适应的可扩展ICL框架；（2）表格语义（元数据、领域知识）与结构的深度融合；（3）针对应用场景的异构模型自适应与融合系统；（4）基于不同应用需求（准确率-可解释性-鲁棒性）的多维评估体系构建。唯有在这些方向取得实质进展，表格数据基础模型方能真正释放深度学习在结构化数据领域的潜能。

---

## 参考文献

[1] Hollmann, N., et al. (2024). Accurate predictions on small data with a tabular foundation model. *Nature*, 614(7949), 108–115. [论文链接：https://www.nature.com/articles/s41586-024-08328-6]

[2] Somvanshi, S., Das, S., Javed, S. A., Antariksa, G., & Hossain, A. (2024). A survey on deep tabular learning. *arXiv preprint arXiv:2410.12034*. [论文链接：https://arxiv.org/abs/2410.12034]

[5] Jiang, J. P., Liu, S. Y., Cai, H. R., Zhou, Q., & Ye, H. J. (2025). Representation learning for tabular data: A comprehensive survey. *arXiv preprint arXiv:2504.16109*. [GitHub: https://github.com/LAMDA-Tabular/Tabular-Survey]

[8] Wei, Z., et al. (2023). Generative table pre-training empowers models for tabular prediction. In *Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)* (pp. 14838–14850). [论文链接：https://aclanthology.org/2023.emnlp-main.917.pdf]

[13] Kotelnikov, A., Baranchuk, D., Rubachev, I., & Babenko, A. (2023). TabDDPM: Modelling tabular data with diffusion models. In *International Conference on Machine Learning (ICML)* (pp. 11328–11348). [论文链接：https://arxiv.org/abs/2209.15421]

[14] Yin, P., Neubig, G., Yih, W. T., & Riedel, S. (2020). TaBERT: Pretraining for joint understanding of textual and tabular data. *arXiv preprint arXiv:2005.08314*. [论文链接：https://arxiv.org/abs/2005.08314]

[15] Thielmann, A., Pfaff, R., & Krause, A. (2024). Mambular: A sequential model for tabular deep learning. *arXiv preprint arXiv:2408.06291v1*. [论文链接：https://arxiv.org/html/2408.06291v1]

[19] Somepalli, G., Goldblum, M., Schwarzschild, A., Bruss, C. B., & Goldstein, T. (2021). SAINT: Improved neural networks for tabular data via row attention and contrastive pre-training. *arXiv preprint arXiv:2106.01342*. [论文链接：https://arxiv.org/abs/2106.01342]

[25] Liu, G., Yang, J., & Wu, L. (2022). PTab: Using the pre-trained language model for modeling tabular data. *arXiv preprint arXiv:2209.08060*. [论文链接：https://arxiv.org/abs/2209.08060]

[26] Borisov, V., Sessler, K., Leemann, T., Pawelczyk, M., & Kasneci, G. (2023). Language models are realistic tabular data generators. In *International Conference on Learning Representations (ICLR)*. [论文链接：https://openreview.net/forum?id=cEygmQNOeI]

[29] Zhu, X., et al. (2025). GReaTER: Generate realistic tabular data after data enhancement and reduction. *arXiv preprint arXiv:2503.15564v1*. [论文链接：https://arxiv.org/html/2503.15564v1]

[31] Sercan Ö. Arık, T., & Pfister, T. (2021). TabNet: Attentive interpretable tabular learning. In *Proceedings of the AAAI Conference on Artificial Intelligence* (Vol. 35, No. 8, pp. 6679–6687). [论文链接：https://arxiv.org/abs/1908.07442]

[32] Gorishniy, Y., Rubachev, I., Khrulkov, V., & Babenko, A. (2021). Revisiting deep learning models for tabular data. *arXiv preprint arXiv:2106.11959*. [论文链接：https://arxiv.org/abs/2106.11959]

[43] Qu, J., Holzmüller, D., Varoquaux, G., & Le Morvan, M. (2025). TabICL: A tabular foundation model for in-context learning on large data. *arXiv preprint arXiv:2502.05564* (to appear at ICML 2025). [论文链接：https://arxiv.org/abs/2502.05564]

[44] Zhang, X., et al. (2025). TableLLM: Enabling tabular data manipulation by LLMs in real office usage scenarios. *Findings of ACL 2025*. [论文链接：https://aclanthology.org/2025.findings-acl.538.pdf]

[46] Qu, J., Holzmüller, D., Varoquaux, G., & Le Morvan, M. (2025). TabICL: A tabular foundation model for in-context learning on large data. In *ICML* (Poster). [OpenReview: https://openreview.net/forum?id=0VvD1PmNzM]

[49] Pfisterer, F., et al. (2025). Tabular data: Is deep learning all you need? *arXiv preprint arXiv:2402.03970v3*. [论文链接：https://arxiv.org/html/2402.03970]

[56] Sinodinos, D., Wei, J. Y., & Armanfard, N. (2025). MultiTab: A scalable foundation for multitask learning on tabular data. In *AAAI 2026* (Accepted). [论文链接：https://arxiv.org/abs/2511.09970]

[57] Wang, P., et al. (2023). GANDALF: Gated adaptive network for deep automated learning of features. *arXiv preprint arXiv:2207.08548v6*. [论文链接：https://arxiv.org/html/2207.08548v6]

[58] Pfisterer, F., et al. (2024). Tabular data: Is deep learning all you need? In *NeurIPS 2024 Workshop: Advances in Tabular Learning*. [论文链接：https://arxiv.org/html/2402.03970v3]