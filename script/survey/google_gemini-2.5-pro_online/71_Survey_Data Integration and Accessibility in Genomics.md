好的，作为一名严谨的科研助手，我将基于提供的真实网络搜索结果，为您生成一篇关于“基因组学中的数据整合与可及性”的中文学术综述。

***

### **基因组学数据整合与可及性研究进展（2022-2025）**

#### **引言**

随着高通量测序技术的飞速发展，基因组学已进入一个数据爆炸的时代。然而，单一模态的数据难以完整刻画复杂生命活动的调控机制与疾病的生物学异质性 [cjournal.hep.com.cn](https://cjournal.hep.com.cn/1671-7554/CN/1190599147562291324)。因此，研究范式正从单维分析转向多模态数据整合，通过融合基因组、表观组、转录组、蛋白质组、空间信息及临床表型等多源异构数据，以期获得更全面、更深刻的生物学见解和临床应用价值 [news.qq.com](https://news.qq.com/rain/a/20250317A097E600)。本文系统梳理了2022至2025年间在基因组数据整合与可及性方面的代表性方法与进展，总结了其共性评价标准，并对未来发展趋势与挑战进行了展望。

#### **方法分类与代表作**

##### **1. 单细胞多组学整合**

单细胞多组学整合旨在对齐来自同一生物系统的不同分子层面的测量数据（如scRNA-seq和scATAC-seq），以揭示细胞异质性、调控网络和细胞命运决定机制。

*   **《A comparison of integration methods for single-cell RNA sequencing data and ATAC sequencing data》** (2025)
    *   **研究问题**: 如何有效整合具有显著异质性（如稀疏度、特征空间不同）的单细胞转录组与染色质可及性数据。
    *   **核心方法**: 该综述对16种主流算法进行了系统性梳理，将其归纳为因子分析（如MOFA+）、加权近邻（如Seurat v4）、深度学习（如scAI、DCCA）及最优传输（如uniPort）等框架。这些方法通过学习联合潜变量或在共享潜空间中建立跨模态对应关系，以实现细胞的协同聚类和标签迁移。
    *   **关键结论**: 在高异质性配对数据场景下，深度非线性模型（scAI）表现出更高的精度（ARI > 0.93）；而在大规模非配对场景中，基于图卷积（scGCN）和迁移学习（scJoint）的算法在保持高精度的同时，展现出更优的可扩展性 [paper.sciencenet.cn](https://paper.sciencenet.cn/htmlpaper/2025/11/20251110133512779142316.shtm)。

##### **2. 空间多维组学整合**

空间组学技术弥补了传统单细胞测序丢失空间信息的不足，通过将分子表达谱映射回其原始组织位置，从而实现对组织微环境、细胞空间排布和互作的解析。

*   **《Spatiotemporal transcriptomic atlas of mouse organogenesis using DNA nanoball-patterned arrays》** (2022)
    *   **研究问题**: 如何在器官发育的复杂过程中，以高分辨率和大规模视场描绘基因表达的时空动态。
    *   **核心方法**: 该研究利用Stereo-seq技术，一种基于DNA纳米球图案化阵列的空间转录组学方法，实现了纳米级分辨率和厘米级视场，构建了小鼠胚胎器官发生的时空转录组图谱。
    *   **关键结论**: 成功解析了小鼠早期胚胎发育（E9.5-E16.5）过程中超过70%区域的细胞类型组成和空间轨迹，揭示了关键器官（如大脑、心脏）发育的精细分子调控机制，展示了大规模空间组学在发育生物学研究中的革新潜力 [sciengine.com](https://www.sciengine.com/doi/pdf/D905E109633A47889C41E6F0B3B683F4)。

*   **《Spatial integration of multi-omics single-cell data with SIMO》** (2025)
    *   **研究问题**: 鉴于空间表观基因组数据的稀缺性，如何利用已有的海量单细胞多组学数据和空间转录组数据来预测空间特异性的增强子活性。
    *   **核心方法**: 提出了SIMO算法，一个基于深度学习的框架，它整合空间转录组和单细胞多组学数据（scRNA-seq + scATAC-seq），在共享的潜在空间中学习跨模态关联。
    *   **关键结论**: SIMO能够有效突破数据稀缺的瓶颈，精准预测空间特异性的增强子，为在空间维度上理解基因调控提供了计算解决方案 [sciengine.com](https://www.sciengine.com/parse/pdf/1674-7232/42F5FC05CD6141A8AF2A35DD0AE08D5F.pdf)。

##### **3. 临床基因组学数据融合**

该方向致力于将患者的基因组变异信息与电子健康记录（EHR）、治疗方案和生存结局等临床数据相结合，以发现与疾病进展和治疗反应相关的生物标志物。

*   **《Characterizing mutation-treatment effects using clinico-genomics data of 78,287 patients with 20 types of cancers》** (2024)
    *   **研究问题**: 如何从大规模真实世界数据中，系统性地识别出影响特定癌症治疗方案生存结局的基因组改变。
    *   **核心方法**: 整合了78,287名癌症患者的体细胞突变数据与从EHR中提取的治疗结果数据，利用Cox比例风险模型和随机森林（RSF）机器学习模型进行关联分析和预测模型构建。
    *   **关键结论**: 研究共识别出与20种癌症中特定治疗相关的776个基因-治疗相互作用，并发现DNA修复通路突变与aNSCLC患者的免疫治疗良好反应显著相关；构建的RSF评分可作为TMB的补充指标，用于预测免疫疗法对aNSCLC患者的生存益处 [medsci.cn](https://www.medsci.cn/article/show_article.do?id=f6ef85e1400a)。

*   **《Official and data-driven optimization of Genomiser for rare disease patients: experience from the Hong Kong Genome Project》** (2025)
    *   **研究问题**: 如何优化表型驱动的变异优先排序工具（Genomiser），以提升其在全基因组测序数据中对编码和非编码致病变异的诊断能力。
    *   **核心方法**: 基于香港基因组项目的985例罕见病患者数据，通过系统调整Genomiser的参数，特别是针对非编码变异预测工具（如ReMM）的评分阈值，并结合SpliceAI等工具进行深度内含子变异的分析。
    *   **关键结论**: 将ReMM评分阈值优化为0.963后，Genomiser在Top-15候选变异中的诊断敏感性从74.63%（默认）提升至92.54%，并成功为5例初始阴性病例找到了明确的致病性深度内含子变异，显著提高了诊断效率和范畴 [medsci.cn](https://www.medsci.cn/article/show_article.do?id=1e4d8994e29c)。

##### **4. 数据可及性与标准化平台**

确保海量基因组数据遵循FAIR原则（可发现、可获取、可互操作、可重用）是最大化其科研价值的前提。大型数据中心和图谱计划在其中扮演了核心角色。

*   **国家基因组科学数据中心 (CNCB-NGDC)** (2025)
    *   **研究问题**: 如何为全球科研用户提供一个一站式、标准化的多组学数据汇交、存储、管理和共享服务。
    *   **核心方法**: CNCB-NGDC构建了涵盖原始数据归档库（GSA）、基因组序列档案库（GWH）、基因组变异图谱（GVM）等多层次的核心数据库体系，并开发了针对特定疾病（CVD Atlas）和细胞类型（CancerSCEM）的知识库。
    *   **关键结论**: GSA已成为全球核心生物数据资源（GCBR）之一，截至2024年底已支持超过25,000个科技项目，汇交数据量达60PB，其发布的数据编号被全球主要学术出版集团认可，极大地促进了我国乃至全球基因组数据的标准化与可及性 [big.cas.cn](https://www.big.cas.cn/xwdt/kyjz/202501/t20250120_7520475.html)。

*   **大型细胞图谱计划 (Human Cell Atlas等)** (2025)
    *   **研究问题**: 如何将来自全球不同实验室、涉及多种技术平台的海量单细胞数据整合成统一、可查询、可复用的细胞图谱资源。
    *   **核心方法**: 通过建立统一的数据处理流程、标准化的元数据规范（如MAMS）和共享的细胞本体论（Cell Type Ontology），并通过开发API接口简化编程访问，确保数据的互操作性。
    *   **关键结论**: 大型细胞图谱（如HuBMAP, CZI CELLxGENE）不仅显著提升了数据的可发现性和可访问性，还通过提供经过严格整理的基准数据集，推动了新计算方法的开发和性能评估 [medsci.cn](https://www.medsci.cn/article/show_article.do?id=05559019e862)。

#### **实验与评价总结**

在方法学评估方面，不同类型的整合任务采用了不同的评价体系，但呈现出一些共性。

1.  **整合质量评估**: 对于单细胞多组学整合，普遍采用**轮廓系数（Silhouette Score）**、**调整兰德指数（ARI）**和**归一化互信息（NMI）**等指标，在已知细胞类型的基准数据集上评估模型消除批次效应、同时保留生物学变异的能力 [paper.sciencenet.cn](https://paper.sciencenet.cn/htmlpaper/2025/11/20251110133512779142316.shtm)。
2.  **可扩展性与效率**: 随着数据规模增至百万细胞级别，算法的计算效率成为关键评价指标。研究普遍关注算法的**时间**和**内存**复杂度，并强调开发线性复杂度或采用小批量（mini-batch）训练策略的必要性 [medsci.cn](https://www.medsci.cn/article/show_article.do?id=05559019e862)。
3.  **临床与生物学效用**: 在临床基因组学融合研究中，评价标准更侧重于实际应用价值，如罕见病诊断中**诊断率的提升** [medsci.cn](https://www.medsci.cn/article/show_article.do?id=1e4d8994e29c)，以及在癌症研究中预测模型的**生存分析曲线（Kaplan-Meier）**和**风险比（Hazard Ratio）** [medsci.cn](https://www.medsci.cn/article/show_article.do?id=f6ef85e1400a)。
4.  **基准数据集的重要性**: “金标准”数据集（如通过独立验证手段确立参考标准的数据）对于算法的客观比较至关重要。经过严格整理的大型细胞图谱正逐渐成为社区公认的基准测试资源，用以评估新方法的鲁棒性和泛化能力 [medsci.cn](https://www.medsci.cn/article/show_article.do?id=05559019e862)。

#### **趋势与挑战**

基于2025年前后的研究动态，基因组数据整合与可及性领域呈现出以下主要趋势与挑战：

1.  **基础模型驱动的泛化表示学习**: AI领域的进展，特别是基础模型（Foundation Models），正在被引入基因组学。模型如Geneformer、scGPT等通过在海量细胞图谱数据上进行预训练，学习基因表达的泛化表示，可用于细胞注释、扰动预测等多种下游任务。主要挑战在于**模型的可解释性不足、计算资源需求高，以及在噪声高或罕见细胞类型数据集上的可靠性验证** [medsci.cn](https://www.medsci.cn/article/show_article.do?id=05559019e862)。

2.  **跨尺度整合与因果可解释性框架**: 未来的整合框架需能连接从分子（基因组、表观组）、细胞（单细胞、空间位置）到组织乃至临床表型（EHR）的跨尺度信息。简单的关联分析已不能满足需求，发展**基于因果推断（如孟德尔随机化）和生物学先验知识（如通路信息）的可解释AI框架**，以揭示“驱动”而非仅仅“关联”的机制，是当前的核心挑战 [cjournal.hep.com.cn](https://cjournal.hep.com.cn/1671-7554/CN/1190599147562291324) [news.qq.com](https://news.qq.com/rain/a/20250317A097E600)。

3.  **空间-时间多模态整合的更高维度**: 随着空间组学技术向三维、亚细胞分辨率发展，以及谱系追踪技术的成熟，整合**空间（Spatial）、时间（Temporal）、多组学（Multi-omics）**数据的挑战变得尤为突出。开发能够处理和可视化3D多模态数据、解析细胞动态互作和谱系发育轨迹的算法是前沿方向 [sciengine.com](https://www.sciengine.com/doi/pdf/D905E109633A47889C41E6F0B3B683F4)。

4.  **数据安全共享与联邦化生态系统**: 数据隐私是制约大规模、跨机构数据整合的关键瓶颈。建立**安全合规的联邦数据湖（Federated Data Lake）和发展联邦学习（Federated Learning）算法**，在不移动原始敏感数据的前提下进行分布式模型训练，将是实现数据价值最大化与隐私保护之间平衡的关键技术路径 [cjournal.hep.com.cn](https://cjournal.hep.com.cn/1671-7554/CN/1190599147562291324) [news.qq.com](https://news.qq.com/rain/a/20250317A097E600)。

#### **结论**

2022至2025年，基因组学数据整合与可及性研究取得了显著进展。方法学上，从单细胞多组学到空间、临床数据的融合算法日趋成熟，并越来越多地由深度学习和AI模型驱动。在数据可及性方面，以国家数据中心和大型国际图谱计划为代表的标准化平台建设，极大地推动了数据的规范化和共享。然而，该领域仍面临计算可扩展性、模型可解释性、跨尺度因果推断以及数据隐私保护等多重挑战。未来的研究将更加聚焦于构建可解释的、支持因果推断的AI基础模型，并探索在联邦化框架下实现多中心、多模态、多尺度数据的安全高效整合，最终推动从海量数据到精准诊疗和基础生命科学发现的闭环转化。

#### **参考文献**

1.  [cjournal.hep.com.cn](https://cjournal.hep.com.cn/1671-7554/CN/1190599147562291324)
2.  [news.qq.com](https://news.qq.com/rain/a/20250317A097E600)
3.  [paper.sciencenet.cn](https://paper.sciencenet.cn/htmlpaper/2025/11/20251110133512779142316.shtm)
4.  [sciengine.com](https://www.sciengine.com/doi/pdf/D905E109633A47889C41E6F0B3B683F4)
5.  [sciengine.com](https://www.sciengine.com/parse/pdf/1674-7232/42F5FC05CD6141A8AF2A35DD0AE08D5F.pdf)
6.  [medsci.cn](https://www.medsci.cn/article/show_article.do?id=f6ef85e1400a)
7.  [medsci.cn](https://www.medsci.cn/article/show_article.do?id=1e4d8994e29c)
8.  [big.cas.cn](https://www.big.cas.cn/xwdt/kyjz/202501/t20250120_7520475.html)
9.  [medsci.cn](https://www.medsci.cn/article/show_article.do?id=05559019e862)
10. [zhjbkz.ahmu.edu.cn](https://zhjbkz.ahmu.edu.cn/cn/article/doi/10.16462/j.cnki.zhjbkz.2025.08.014)
11. [medsci.cn](https://www.medsci.cn/article/show_article.do?id=f313836841f0) (此文献在搜索结果中存在，但未在正文详细引用，作为补充列出)
12. [medsci.cn](https://www.medsci.cn/article/show_article.do?id=5c4c809e14d4) (此文献在搜索结果中存在，但未在正文详细引用，作为补充列出)