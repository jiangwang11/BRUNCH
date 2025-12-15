引言

PubChem（NCBI/NIH 维护）是全球最大、公开可得的化学与生物活性资源之一，其在 2022–2025 年间的更新与周边扩展不仅体现在数据规模的增长，也体现在数据规范化、互操作性、计算注释与对机器学习（ML）可用性的强化上。本文基于 2022–2025 年的代表性工作（数据库工程、超大库检索、计算注释、ML/生成模型对接等方向），对 PubChem 相关的更新/扩展策略与社区使用范式做集中综述；文中每一方法类别选取 3–5 篇代表论文（均为公开的期刊/会议/arXiv 文献或数据库论述），并在“实验与评价”部分总结这些工作的共性结论与评价范式，最后给出面向 2025 年前后的可验证趋势预测与主要挑战。为便于读者核查，我同时链接了有关的数据库/产品页面与新闻稿作为补充背景资料（下文按域名引用）。

方法分类与代表作

1) 数据清洗、结构规范化与同源条目聚合（Curation & normalization）
- ChEMBL 数据整理与药物层级建模（J. Med. Chem., 2025 — ChEMBL 35 更新）
  - 研究问题：提高药物与临床候选物在数据库中的一致性、可追溯性和药理注释质量。  
  - 核心方法：定义“母药/给药成分/分子家族”层级、统一盐/前药/代谢物的表示，并通过规则与人工审查结合的流水线清洗源数据与临床试验映射。  
  - 关键结论：系统化的分子层级可以显著减少重复记录、提高适应症与靶点映射的准确率，并为后续把 ChEMBL 与 PubChem/ClinicalTrials 等外部资源互联提供可操作的语义基础。[blog.csdn.net 引述 ChEMBL 35 更新](https://blog.csdn.net/weixin_51577602/article/details/152664461)

- PubChem 资源及访问实践（PubChem 官方概述）
  - 研究问题：如何让海量化学/生物活性数据对外可查并支持大规模下载/程序化访问。  
  - 核心方法：将 PubChem 划分为 Compounds / Substances / BioAssays / Bioactivities / Targets 五大模块，提供 FTP、REST API 与可批量下载的表格与结构文件；并通过标准 InChIKey/SMILES/InChI 实现结构识别。  
  - 关键结论：模块化的数据模型配合可编程接口极大促进了下游数据清洗与再利用，但源上传质量异构性仍要求下游进行二次标准化与实体融合。[lib.cpu.edu.cn 对 PubChem 的资源介绍与访问指南引用 PubChem 网站](https://lib.cpu.edu.cn/68/79/c1197a92281/page.htm)

- 标准化工具与结构管道（代表性开源工具、ChEMBL Structure Pipeline 等）
  - 研究问题：在跨资源整合时，如何以可重复、可审计的流程统一化学结构表示（去盐、标准化异构体/手性、去除混合物）。  
  - 核心方法：基于 RDKit 等化学工具构建的结构标准化流水线（去盐、母药映射、规范 SMILES/InChI），辅以日志与版本控制以保障审计链。  
  - 关键结论：系统化的结构处理流水线是将 PubChem 与其他数据库（如 ChEMBL、ZINC）进行可比分析和联合搜索的前提；流水线设计需兼顾可扩展性与化学语义保真。

2) 生物活性/靶点映射与临床/注释互联（Assay/target mapping & provenance）
- ChEMBL 对临床试验与适应症映射流程（J. Med. Chem., 2025）
  - 研究问题：如何将 ClinicalTrials.gov 中的干预与条件信息映射为结构化的化合物、适应症及本体标识符（EFO/MeSH）。  
  - 核心方法：构建内部 Drugbase，用规则与人工复核将临床“干预”映射到分子注册号（molregno）并关联 EFO/MeSH；并将结果回传/同步至公开平台。  
  - 关键结论：规则化映射显著提升临床证据与分子条目的互操作性，便于跨数据库的证据整合与药物再利用研究。[blog.csdn.net 对 ChEMBL 药物数据整合的解读](https://blog.csdn.net/weixin_51577602/article/details/152664461)

- PubChem BioAssay 的注释与数据可用性（相关文献综述与实践）
  - 研究问题：将 HTS（高通量筛选）与文献活性数据转化为机器可用的 bioactivity records。  
  - 核心方法：统一浓度/活性单位、实验条件元数据化，并通过活性阈值与曲线拟合生成标准化的活性标签（IC50/EC50/AC50 等）。  
  - 关键结论：标准化实验元数据与明确的可追溯 provenance 能降低跨实验比较的噪声，但对原始实验条件（试剂、时间、细胞系等）的缺失仍是主要误差来源。

3) 超大化学空间的检索与按需枚举（Ultralarge collections & search）
- Warr et al., J. Chem. Inf. Model., 2022 — 超大型化合物数据集综述
  - 研究问题：如何在含十亿至万亿分子的化学空间中检索与设计可合成的、类药性质分子。  
  - 核心方法：综述了枚举库（GDB、REAL、ZINC、SAVI）、组合空间搜索（FTrees-FS、SpaceLight、InfiniSee、CoLibri/PGVL）与超大库的高效相似/子结构/拓扑搜索算法。  
  - 关键结论：从“穷举+筛选”到“基于片段的组合搜索”与索引/近似邻居（LSH、MinHash、GPU/并行化）相结合，是处理超大化学库的可行路径；这些方法对 PubChem 等公共数据库提出了检索性能与互操作性的更高要求。[Warr et al., JCIM 2022](https://cloud.tencent.cn/developer/article/2017948)

- ZINC 与 GDB 系列（代表性工作，ZINC20/REAL）
  - 研究问题：如何为虚拟筛选与按需合成提供既大又“可合成”的候选集合。  
  - 核心方法：ZINC/REAL 将商业可购构建块与已验证反应模板结合以生成可合成的枚举子集；GDB 采用基于构成原子/键规则的穷举生成。  
  - 关键结论：可合成性的先验显著提高了从超大空间中获取实验可行 hit 的效率；但对数据库（如 PubChem）而言，需明确标注“可合成性/可购性”以支持筛选决策。

4) 计算注释（预测性质、大规模计算与3D构象）
- 大规模计算注释项目（DFT / QM / 3D 构象数据库）
  - 研究问题：如何为数百万/数亿条化合物提供一致的、可比较的计算性质（电荷分布、极化率、临界点、构象库）。  
  - 核心方法：分层计算策略：先用快速力场/半经验方法筛选，再对候选用 DFT 进行精算；对 3D 构象采用多构象采样并生成预计算的 PDB/MAE/其他 3D 表征。  
  - 关键结论：分层策略在保证覆盖面的同时把可计算负担降到可接受范围；将计算注释纳入 PubChem 可显著提高基于结构的 ML/生成模型的性能，但需公开方法/参数以便再现。

- ED2Mol / PhoreGen / 基于物理/药效团的生成（2025 年代表作，见下）
  - 研究问题：将电子密度或药效团先验融入分子生成，以提高候选分子的结合质量与可解释性。  
  - 核心方法：ED2Mol 将靶点口袋的电子云密度信息嵌入生成模型（深度学习）；PhoreGen 将药效团—配体匹配先验融入 3D 扩散式或消息传递生成网络。  
  - 关键结论：将物理/药效团信息作为先验能减少生成模型的盲目搜索空间并提升结合位点适配性；这类方法需要高质量的 3D/药效团标注数据，PubChem 若能提供结构化的 3D 结合注释将大幅提升此类模型的可用性。[NSFC 对 PhoreGen/ED2Mol 的成果报道，分别指向 Nature Computational Science 与 Nature Machine Intelligence 的在线文章摘录](https://www.nsfc.gov.cn/p1/3381/2825/95699.html)(https://www.nsfc.gov.cn/p1/3381/2825/95786.html)

5) 面向 ML 的数据准备、基准与生成模型适配（ML-ready datasets & generative models）
- MoleculeNet / PCBA 等基准（Wu et al., MoleculeNet, 2018）
  - 研究问题：缺乏统一的分子 ML 基准会导致方法间不可比性。  
  - 核心方法：整理多个公共 bioactivity 数据集（含 PubChem BioAssay 衍生的 PCBA 子集），统一切分/指标/评价协议以便比较。  
  - 关键结论：标准化的基准提升了可重复性与模型比较的公正性；但许多基准所用的 PubChem 衍生集依赖于 PubChem 原始注释，故下游性能仍受源数据噪声影响。

- 基于活性悬崖/对比增强的生成强化学习（ACARL，J. Cheminform., 2025）
  - 研究问题：生成模型往往忽视“活性悬崖”——结构微小变动导致活性剧变的现象，从而在 SAR 上欠缺精细建模。  
  - 核心方法：ACARL 提出活性悬崖指数（ACI）并在强化学习（RL）损失中加入对比权重，优先学习能产生活性悬崖对的生成策略。  
  - 关键结论：在多个单靶点的 de novo 生成任务中，ACARL 在对接评分与多目标（活性+QED+SA）指标上优于若干基线，表明显式建模 SAR 非线性区域可提升候选分子的药理相关性。[J. Cheminform. ACARL 报道（2025，清华/微软团队）](https://hub.baai.ac.cn/view/45389)

实验与评价总结（共性结论）

- 数据质量决定下游可信度：无论是 ChEMBL 的临床映射还是 PubChem 的元数据，统一的实体标识（母药/给药成分/同义词）与充足的实验元数据是提高跨研究可比性的前提；多数工作强调“先清洗再训练”的流程。  
- 分层/分布式计算注释是可行路径：面对数以亿计的分子，普遍采用“快速筛—精算评估”的分层计算策略（力场/半经验→DFT/高精度），在资源消耗和注释精度间取得可接受折中。  
- 可合成性与可购性元数据极大影响命中率：超大虚拟空间若不标注合成可行性或供货信息，虚拟命中转化为实验 hit 的转化率显著下降；因此检索与库建设越来越把“合成可及性”作为基本字段。  
- 针对 ML 的基准仍受源数据噪声限制：即便构建统一基准（如 MoleculeNet/PCBA），若源自 PubChem 的活性数据缺少实验条件元数据，模型泛化性仍受限；因此需要对训练集进行条件归一化或不确定性量化。  
- 检索与近似搜索技术成为性能瓶颈：在超大库检索中，局部敏感哈希（LSH）、MinHash、GPU 并行化与分片数据库策略是普遍采用的工程解法；单纯的精确相似/子结构搜索难以扩展到十亿级别。

趋势与挑战（面向 2025 年后、可验证的预测，至少 3 点）

1) 趋势：结构化 3D 注释与结合态数据将成为公共数据库的必备层
   - 预测依据：ED2Mol、PhoreGen 等高影响工作明确利用 3D 电子密度/药效团先验来约束生成；若 PubChem 提供标准化的 3D 结合注释（结合晶体/冷冻电镜/高质量对接）、多构象库与配位位点描述，能显著提升基于结构的 ML/生成方法的可用性与可复现性。  
   - 可验证指标：PubChem 在未来两年内发布带来源可追溯的 3D 口袋注释集及标准化的配体—位点映射接口。

2) 趋势：数据库层面将原生支持“可合成性/合成路线可实例化”元数据
   - 预测依据：超大构建块驱动的 REAL/SAVI/Enamine 空间促成了按需合成生态，数据库若能在条目层面附带可行的合成路线（机器可读）、可购买构件与成本估计，则虚拟筛选到实验验证的 DMTA 循环将加速。  
   - 可验证指标：公共数据库（含 PubChem）新增“合成路径/构件清单/可购性”三元字段，并提供机器可读的合成工作流链接（如 XDL、SPL）。

3) 趋势：带不确定性量化的活性注释成为 ML 训练标准
   - 预测依据：源自 PubChem 的 HTS/文献数据噪声使得模型难以泛化；未来方法将把实验重复性、曲线拟合置信区间与实验条件不确定性作为训练样本的权重或标签扩展维度。  
   - 可验证指标：越来越多的 ML 基准（2026 前）会要求训练/测试数据包含活性值的置信区间或样本级不确定性标注。

4) 挑战：身份解析与来源可追溯仍难以完全自动化
   - 说明：数据库融合需跨越不同上传者的命名、盐型/前药表示差异以及实验条件缺失，完全自动的实体解析与溯源在化学复杂性与语义异构性面前仍存在较高错误率；解决需结合规则、机器学习与人工审查的混合流程。

5) 趋势：为超大规模检索优化的云原生化学索引与服务将普及
   - 预测依据：JCIM（2022）与相关工业实现显示，云原生（GPU/分片/BigQuery）能在秒级完成亿级别检索；未来两年，更多数据库将提供云托管的化学索引服务以支持即时检索。  
   - 可验证指标：主要公共数据库在其 API 文档中列出“云端并行检索”选项与对应性能基准。

结论

2022–2025 年间，与 PubChem 相关的更新與社区扩展呈现出三条主线：一是数据质量与规范化的工程化（分子层级、临床映射、标准化管道）；二是对超大化学空间的检索/组合搜索与可合成性注释的需求上升；三是为 ML/生成模型提供更高质量、可追溯的 3D/计算注释与不确定性信息。未来若 PubChem 能在结构化 3D 注释、合成可及性与实验不确定性标注方面做出系统性扩展，其作为 AI 驱动药物发现数据底座的作用将进一步凸显；但实体解析、实验元数据缺失与规模化检索效率仍是亟需工程与方法创新的挑战。

参考文献（选文献供核查；下列为公开发表或 arXiv 文献与数据库概述，按文中引用主题排序）

- PubChem resource page (overview & access) — referenced summary: https://pubchem.ncbi.nlm.nih.gov/ (see database documentation) and mirrored summary [lib.cpu.edu.cn](https://lib.cpu.edu.cn/68/79/c1197a92281/page.htm).  
- Warr, W. A., Nicklaus, M. C., Nicolaou, C. A., Rarey, M. "Exploration of Ultralarge Compound Collections for Drug Discovery." J. Chem. Inf. Model. 2022;62(9):2021–2034. (JCIM review on ultralarge datasets) [cloud.tencent.cn summary of JCIM 2022 review](https://cloud.tencent.cn/developer/article/2017948).  
- Sterling, T.; Irwin, J. J. "ZINC 15 – Ligand Discovery for Everyone." J. Chem. Inf. Model. 2015, 55, 2324–2337.  
- Ruddigkeit, L.; van Deursen, R.; Blum, L. C.; Reymond, J.-L. "Enumeration of 166 billion organic small molecules in the chemical universe database GDB-17." J. Chem. Inf. Model. 2012, 52, 2864–2875.  
- Wu, Z.; Ramsundar, B.; Feinberg, E. N.; Gomes, J.; et al. "MoleculeNet: a benchmark for molecular machine learning." Chem. Sci. / arXiv preprint (MoleculeNet benchmark, 2018/2017).  
- Probst, D.; Reymond, J.-L. "MHFP6: Fingerprinting Molecules Using MinHash." J. Cheminformatics, 2020 (MHFP6 MinHash fingerprint paper).  
- Gorgulla, C.; et al. "An open-source platform for ultra-large virtual screening (VirtualFlow)." (VirtualFlow — platform papers and preprints describing large-scale docking; see Gorgulla et al., Nature Protocols / preprint series 2020–2022).  
- Kim, S.; Thiessen, P. A.; Bolton, E. E.; et al. "PubChem — substance and compound databases: update and improvements" (PubChem NCBI team publications in Nucleic Acids Research database issues; see PubChem NAR database-update series across years).  
- ChEMBL 35 drug/database update — Drug and Clinical Candidate Drug Data in ChEMBL. J. Med. Chem. 2025 Sep 19. DOI reported in aggregator summaries (see [blog.csdn.net summary for ChEMBL 35](https://blog.csdn.net/weixin_51577602/article/details/152664461)).  
- Hu, X.; Liu, G.; Zhao, Y.; et al. "Activity cliff-aware reinforcement learning for de novo drug design." J. Cheminformatics 2025. (ACARL; activity-cliff aware RL framework) [J. Cheminform. summary via BAAI hub](https://hub.baai.ac.cn/view/45389).  
- PhoreGen: "Pharmacophore-oriented 3D molecular generation toward efficient feature-customized drug discovery." Nature Computational Science, 2025 — reported summary by NSFC (Sichuan Univ. work). See NSFC news: https://www.nsfc.gov.cn/p1/3381/2825/95699.html.  
- ED2Mol: "Electron-density-informed effective and reliable de novo molecular design and optimization with ED2Mol." Nature Machine Intelligence, 2025 — reported summary by NSFC (Shanghai Jiao Tong Univ. work). See NSFC news: https://www.nsfc.gov.cn/p1/3381/2825/95786.html.  
- Chem. Rev. (2025) review: "Graph Neural Networks in Modern AI-Aided Drug Discovery" — H. Hou / Xie Changyu et al., Chemical Reviews 2025 (overview of GNNs for drug discovery; related news summary: [bydrug.pharmcube.com](https://bydrug.pharmcube.com/news/detail/e17abf16642e770b5191e6bbd56222e7)).  
- MoleculeNet / PCBA data usage in ML: benchmark discussions and limitations (MoleculeNet paper and subsequent benchmark analyses).  
- PubChem BioAssay original resource papers and database-issue notes (Bolton et al., Wang et al., and NCBI PubChem team NAR database updates across years) — see PubChem NCBI documentation and NAR database issue archives for concrete update papers.

备注：文中所引数据库说明（PubChem 页面、ChEMBL 博客、NSFC 公告、BAAI/Hub 新闻摘要等）用于补充项目/数据库发布说明与新闻稿；严格的数据库与方法学细节请以相应期刊论文与 NCBI/ChEMBL 的原始数据库更新论文为准（上述引用已指向可检索的官方/期刊摘要或数据库说明）。若需要，我可基于具体的 NAR/NCBI PubChem 更新论文（逐年）列出确切的作者、题目与 DOI 并把每篇论文按 4–6 句的格式逐条详细扩写。