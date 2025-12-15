# 基因组学中的数据整合与可及性研究综述（2022–2025）

## 引言

基因组学已进入多组学、单细胞与空间解析的高维时代，其核心挑战在于异构数据的语义鸿沟与资源壁垒。一方面，单细胞ATAC-seq、长读长RNA-seq、Hi-C等新技术产生稀疏、高噪、多模态的数据；另一方面，全球数据孤岛与计算资源分配不均阻碍了科学发现。2022–2025年间，学术界与国家级数据中心协同推进，涌现出一批聚焦数据整合算法、标准化基础设施与智能可及性的代表性工作。本综述按方法范式分类，系统梳理此期间的关键进展，并基于真实研究动态预测未来方向。

## 方法分类与代表作

### 1. 单细胞多组学整合与细胞注释

单细胞多组学数据的整合亟需克服模态间特征空间不一致与技术噪声问题。Zhao等人提出的scGWAS（*Genome Biology*, 2022）将单细胞转录组与全基因组关联研究（GWAS）关联，通过模块扩展-反向检测（MEBE）算法识别性状-细胞类型关联，在40个复杂性状中发现2,533个显著关联，如小胶质细胞与阿尔茨海默病。针对scATAC-seq数据稀疏性导致的注释难题，scDIFF（*Briefings in Bioinformatics*, 2025）创新性地融合bulk-level表观基因组信息（如ChIP-seq峰）与扩散Transformer架构，其在14个数据集上的Cohen's kappa系数达0.94，显著优于SANGO等基线方法，尤其在稀有细胞类型（如NK细胞，注释准确率73%）上表现突出。此外，scMODAL（*Nature Communications*, 2025）通过通用深度学习框架实现跨模态（如RNA+ATAC）的“全维度”整合，有效保留了模态特异性与共享生物学信号。

### 2. 跨尺度基因组结构与功能建模

基因组功能由其三维空间构型精密调控，但传统方法难以高通量解析。耶鲁大学开发的Perturb-tracing平台（*Nature Methods*, 2025）结合CRISPR文库、BARC-FISH条形码与染色质追踪技术，在单次实验中完成12,600+种基因扰动对染色体22多尺度结构（TAD到染色体疆域）的影响分析，新发现21个调控因子如CHD7（敲除后染色体半径增18%）和AQP3。在预测层面，一项发表于*Nucleic Acids Research*（2025）的通用AI模型，通过整合ATAC-seq、ChIP-seq与Hi-C等多模态数据，实现了对启动子-增强子互作、新生RNA表达及染色质可及性的联合预测，其在K562细胞系中对lentiMPRA验证的增强子-启动子对预测AUC达0.92，超越Enformer等模型。

### 3. 全基因组变异解读与诊断优化

全基因组测序（WGS）的临床应用受限于非编码变异的致病性解读。香港基因组项目对Genomiser工具进行系统性优化（*Briefings in Bioinformatics*, 2025），通过调整ReMM评分阈值（0.963）并整合SpliceAI、REVEL等多重预测源，在985例罕见病患者中将Top-15敏感性提升至92.54%。该流程在778例初报阴性病例中识别出20个深度内含子致病变异，包括一例Dravet综合征患者SCN1A基因c.2415+431C>G变异。同时，大型长读长RNA测序数据集SG-NEx（*Nature Methods*, 2025）的发布，为精确解析剪接异构体与融合转录本提供了基准，解决了短读长测序在复杂RNA结构解析中的固有盲区。

### 4. 国家级数据基础设施与标准化

数据可及性依赖于强大的基础设施。国家基因组科学数据中心（NGDC）（*ngdc.cncb.ac.cn*）已建成国内领先的生物大数据云平台，拥有3,720 TFlops计算能力、108PB存储与16,576个计算核心，并持续更新如CancerSCEM 2.0、iDog 2.0等专题数据库。在数据标准方面，《中国科学：生命科学》（2025）的“表观基因组技术专题”系统综述了ChIP-seq、ATAC-seq、Hi-C等技术的标准化进展，强调了从数据生成、元数据描述到分析流程的统一规范对跨研究整合的必要性。

## 实验与评价总结

近期研究的实验评价呈现三大共性：（1）**基准数据集的扩展**：评价不再局限于少数公共数据集（如10x PBMC），而是涵盖跨组织、跨平台（10x, sciATAC-seq, snATAC-seq）和跨物种的多样化数据，以检验方法的泛化能力。（2）**生物学验证的强化**：顶级研究普遍结合CRISPR筛选（如Perturb-tracing）、lentiMPRA或临床诊断结果（如Genomiser优化）进行独立验证，而非仅依赖计算指标。（3）**公平性与鲁棒性评估**：针对数据不平衡（如稀有细胞类型）和平台效应（如不同测序深度）的鲁棒性测试成为标准流程，例如scDIFF在不同细胞比例和测序深度下的稳定性分析。

## 趋势与挑战

基于2025年前后的研究动态，三大趋势已清晰显现：
1.  **通用基因组基础模型（Genomic Foundation Models）的崛起**：以Nucleic Acids Research（2025）工作为代表，能同时处理DNA序列、表观修饰、三维结构与转录输出的统一模型正成为主流，其通过大规模自监督预训练获取通用基因组“语言”能力，再通过提示（prompting）或微调适配下游任务。
2.  **临床-科研数据闭环的构建**：如香港基因组项目和NGDC的CancerSCEM 2.0所示，将临床表型、WGS/WES数据与多组学功能注释深度整合的端到端分析流程，正从研究工具向临床诊断标准演进。
3.  **长读长与空间多组学驱动的新标准**：SG-NEx数据集的发布和空间多组学技术（如联合DNA甲基化与转录组分析，*Nature*, 2025）的成熟，将推动基因组数据标准从短读长、批量分析向长读长、单细胞、空间分辨的高维范式迁移。

核心挑战包括：非编码变异功能预测的高假阳性率、跨模态数据整合中的信息损失、以及全球南方国家在数据生成与计算资源上的可及性鸿沟。

## 结论

2022–2025年是基因组学数据整合与可及性研究的关键跃升期。从单细胞注释到三维基因组建模，从变异解读到国家级基础设施建设，研究范式正从孤立工具开发转向系统性、标准化和智能化。未来，以通用AI模型为引擎、以临床需求为导向、以全球公平可及为目标的整合框架，将成为解锁基因组学全部潜力的核心路径。

## 参考文献

1. Zhao, Z. et al. scGWAS: landscape of trait-cell type associations by integrating single-cell transcriptomics-wide and genome-wide association studies. *Genome Biol* **23**, 247 (2022).
2. scDIFF: automatic cell type annotation using scATAC-seq data by incorporating bulk-level genomic and epigenomic information in a deep diffusive transformer. *Brief Bioinform* (2025).
3. Nat Commun: Breakthrough in single-cell multi-omics data integration bottleneck! The general deep learning framework scMODAL helps cross-modal analysis into the "full-dimensional" era. *MedSci.cn* (2025).
4. Perturb-tracing enables high-content screening of multi-scale 3D genome regulators. *Nat Methods* (2025).
5. Developing a general AI model for integrating diverse genomic modalities and comprehensive genomic knowledge. *Nucleic Acids Res* (2025).
6. Xi, A.M.C. et al. Official and data-driven optimization of Genomiser for rare disease patients: experience from the Hong Kong Genome Project. *Brief Bioinform* **26**, bbaf475 (2025).
7. Large-scale long-read RNA sequencing dataset released—Chinese Academy of Sciences. *cas.cn* (2025).
8. Nature: Pioneering spatial multi-omics technology! First spatial co-analysis of DNA methylation and transcriptome on the same tissue section. *MedSci.cn* (2025).
9. Lu, F. et al. Advances in epigenomic technologies. *Sci Sin Vitae* **55**, 1057–1059 (2025).
10. National Genomics Data Center (NGDC). *ngdc.cncb.ac.cn*.
11. NAR: The world's first single-cell multi-omics database based on fluorescent image data—iSMOD. *MedSci.cn* (2023).
12. Nat Methods: Breaking the resolution barrier! The GHIST framework predicts single-cell spatial gene expression directly from conventional pathology images. *MedSci.cn* (2025).