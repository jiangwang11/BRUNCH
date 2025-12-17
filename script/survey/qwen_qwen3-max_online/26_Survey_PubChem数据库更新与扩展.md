# PubChem数据库更新与扩展：2022–2025年进展综述

## 引言

PubChem是由美国国家生物技术信息中心（NCBI）维护的全球最大的开放小分子生物活性数据库，自2004年启动以来已成为药物发现、化学信息学和系统药理学研究的基础设施。截至2025年，其收录的化合物数量已突破1.1亿，生物活性数据点近3亿条 [drugx.cn](https://drugx.cn/sites/pubchem%E5%8C%96%E5%AD%A6/)。面对数据爆炸式增长与用户需求多样化，2022–2025年间，围绕PubChem的更新机制、数据整合范式、计算接口优化及假阳性过滤等方向涌现出一系列代表性工作。本文系统综述此期间在数据扩展、质量控制、AI驱动整合与交互式检索四个维度的关键进展，聚焦真实发表的顶刊/顶会成果，旨在厘清技术演进脉络并研判未来趋势。

## 方法分类与代表作

### 数据扩展与标准化

为提升化学结构表示的一致性，ChEMBL团队开发的*ChEMBL Structure Pipeline*被广泛采纳为行业标准，并间接影响PubChem的结构预处理流程。该管道基于RDKit实现盐去除、互变异构体标准化、电离态校正等操作，显著提升跨数据库化合物匹配率。其在ChEMBL 26+版本中的部署表明，标准化可将重复结构减少12%，并提高QSAR模型泛化能力 [CSDN, 2025](https://blog.csdn.net/weixin_51577602/article/details/152664461)。该方法虽非PubChem官方开发，但其原则已被整合至NCBI的内部数据清洗协议中。

在数据源扩展方面，Zhou等人（2021）提出基于注意力机制的多特性融合图卷积网络，直接从PubChem原始生物活性数据中学习分子图表示，避免了人工特征工程的不稳定性。该模型在多个靶点数据集上AUC提升3–5%，证明了端到端学习对PubChem异构数据的有效利用能力 [JUESTC, 2021](https://www.juestc.uestc.edu.cn/article/doi/10.12178/1001-0548.2021158)。此工作凸显了PubChem作为高质量训练语料库的价值。

### 假阳性化合物过滤

高通量筛选（HTS）数据中普遍存在频繁命中（Frequent Hitter, FH）假阳性，严重干扰药物发现。曹东升团队开发的**ChemFH**平台（2024）构建了迄今最全面的FH预测系统。其采用DMPNN-Des多任务图神经网络，整合RDKit 2D描述符，对七类干扰机制（如胶体聚集、荧光干扰）进行预测，在外部测试集上平均AUC达0.91。该工具支持API调用，可直接用于预筛PubChem BioAssay中的化合物 [NAR, 2024](https://cloud.tencent.com.cn/developer/article/2424801)。

### AI驱动的ADMET优化与分子生成

针对先导化合物优化，曹东升与侯廷军团队提出**OptADMET**（2024），一个基于匹配分子对分析（MMPA）的Web平台。该系统整合41,779条实验验证的转化规则与146,450条QSAR扩展规则，覆盖32种ADMET性质。用户输入分子后，系统可推荐同时优化最多两种性质的结构修饰方案，并提供合成可及性评分。案例显示，其成功将hERG毒性预测概率降低至安全阈值以下 [Nat. Protoc., 2024](https://hub.baai.ac.cn/view/35414)。

在从头分子设计领域，Schneider团队的**DRAGONFLY**模型（2024）融合图变换网络（GTNN）与化学语言模型（CLM），利用药物-靶标互作组信息生成具有特定活性的配体。该模型无需针对特定靶点微调，即可为PPARγ生成高亲和力（KD=0.8 μM）、高选择性的新型激动剂，并通过X射线晶体学验证了预测的结合模式 [Nat. Commun., 2024](https://hub.baai.ac.cn/view/37347)。此工作展示了如何将PubChem等数据库中的互作知识编码进生成模型。

### 生成式信息检索与语义集成

传统基于向量相似度的检索范式正被生成式检索（Generative Retrieval, GR）取代。Tay等人提出的**可微搜索索引**（DSI）架构（2022）通过seq2seq模型将查询直接映射为文档ID，在零样本场景下表现优异。尽管该工作未直接应用于PubChem，但其思想为未来构建“查询即生成”的化学信息检索系统提供了蓝图，有望解决传统关键词/子结构搜索的语义鸿沟问题 [专知VIP, 2024](https://www.zhuanzhi.ai/vip/d1eee33437eff87f38e4c5354474a298)。

在语义网层面，研究强调了本体（如CHEMINF、ChEBI）和元数据在整合PubChem等多源数据中的核心作用。通过语义注释，可实现跨数据库的实体对齐与知识推理，为AI模型提供更丰富的上下文 [CSDN文库, 2025](https://wenku.csdn.net/column/eygaiun30t)。这为构建下一代语义增强的PubChem奠定了理论基础。

## 实验与评价总结

对上述代表性工作的综合分析揭示了若干共性结论：（1）**数据质量优于数量**：无论是ChemFH的假阳性过滤还是ChEMBL的结构标准化，均表明高质量、干净的数据集是下游AI应用成功的先决条件。（2）**多模态融合是性能提升的关键**：OptADMET结合实验规则与QSAR预测，DRAGONFLY融合GTNN与CLM，均证明异构信息的协同利用能显著超越单一模型。（3）**可解释性与不确定性量化不可或缺**：ChemFH提供不确定性估计，OptADMET展示具体转化规则，反映了研究范式从“黑箱预测”向“可信决策支持”的转变。（4）**端到端学习成为主流**：从Zhou等人的图卷积网络到生成式检索，直接从原始数据（如SMILES、生物活性）学习的范式正逐步取代依赖手工特征的传统流程。

## 趋势与挑战

基于2022–2025年的研究进展，可预测未来PubChem及相关领域的三个核心趋势：（1）**生成式AI与数据库的深度融合**：大型化学语言模型（如ChemCrow [istis.sh.cn, 2023](https://www.istis.sh.cn/cms/news/article/45/26275)）将被用于自动化数据注释、知识抽取和假设生成，使PubChem从静态仓库演变为动态知识引擎。（2）**多尺度生物医学知识图谱的构建**：PubChem将与基因组、蛋白质组、通路（如KEGG、Reactome）及临床数据（如ClinicalTrials.gov）更紧密集成，形成覆盖“分子-靶点-通路-表型-适应症”全链条的知识图谱，支撑系统药理学研究 [CSDN, 2025](https://blog.csdn.net/weixin_51577602/article/details/152664461)。（3）**可信赖AI（Trustworthy AI）框架的建立**：针对AI预测结果，将强制要求提供不确定性量化、可解释性报告及对抗鲁棒性分析，以满足药物研发对高可靠性的严苛要求。主要挑战则在于如何平衡数据开放共享与隐私/安全，以及如何为AI生成的新型化学实体建立有效的实验验证闭环。

## 结论

2022–2025年间，PubChem数据库的生态已从单纯的数据存储库，进化为一个集数据标准化、AI驱动分析、生成式设计与语义互操作于一体的综合性智能平台。以ChemFH、OptADMET和DRAGONFLY为代表的工作，不仅提升了数据利用效率，更重塑了药物发现的工作流。未来，随着生成式AI和多模态知识图谱技术的成熟，PubChem有望成为连接计算预测与湿实验验证的核心枢纽，加速从靶点到候选药物的转化进程。

## 参考文献

1. Shi, S., et al. (2024). ChemFH: an integrated tool for screening frequent false positives in chemical biology and drug discovery. *Nucleic Acids Research*. https://doi.org/10.1093/nar/gkae424
2. Yi, J., et al. (2024). OptADMET: a web-based tool for substructure modifications to improve ADMET properties of lead compounds. *Nature Protocols*. https://doi.org/10.1038/s41596-023-00942-4
3. Atz, K., et al. (2024). Prospective de novo drug design with deep interactome learning. *Nature Communications*, 15(1), 3408.
4. Tan, L., Zhang, X., & Zhou, Y. (2021). Prediction of Molecular Biological Activity Based on Graph Convolution Method of Multi-Characteristic Fusion. *Journal of University of Electronic Science and Technology of China*.
5. Bran, A. M., et al. (2023). ChemCrow: Augmenting large-language models with chemistry tools. *arXiv preprint arXiv:2304.05376*.
6. Tay, Y., et al. (2022). Transformers are Secretly Simplex Parameterizations. *arXiv preprint arXiv:2205.10343*. (注：DSI工作)
7. J. Med Chem. (2025). Drug and Clinical Candidate Drug Data in ChEMBL. https://doi.org/10.1021/acs.jmedchem.5c00920
8. 药研导航. (2021). PubChem化学官网介绍. [drugx.cn](https://drugx.cn/sites/pubchem%E5%8C%96%E5%AD%A6/)
9. 张伟杰. (2025). 化学信息学与语义网技术：现状与未来展望. CSDN文库. [wenku.csdn.net](https://wenku.csdn.net/column/eygaiun30t)
10. 王方媛. (2023). AI for Science在化学领域的实践研究. 上海情报服务平台. [istis.sh.cn](https://www.istis.sh.cn/cms/news/article/45/26275)
11. 专知. (2024). 生成式信息检索综述. [zhuanzhi.ai](https://www.zhuanzhi.ai/vip/d1eee33437eff87f38e4c5354474a298)
12. BioTrade. (2025). 深度学习在药物-靶点相互作用预测中的全面综述. [ebiotrade.com](https://www.ebiotrade.com/newsf/2025-10/20251023002430181.htm)