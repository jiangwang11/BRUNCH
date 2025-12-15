引言  
个体化药物治疗（personalized therapy）要求把分子异质性、患者临床表型与药物作用机制耦合到可操作的决策模型中。过去三年（2022–2025）深度学习（DL）在该场景内的代表性进展，覆盖了从蛋白/结构建模、药物—靶相互作用（DTI）、药物敏感性预测、多模态/单细胞驱动的“数字孪生”到虚拟/定量临床试验（QSP/VCT）等环节。下文按方法学类别列出每类 3–5 篇代表性论文（2022–2025），每篇简要说明：研究问题、核心方法与关键实验结论；随后总结这些工作的共同实验/评估结论，讨论面向 2025 年前后的趋势与挑战，并给出结论与参考文献。为保证可检验性，文中所述论文均来自公开顶级期刊/预印本或权威综述（见参考文献），并以检索到的源页面作为索引。[html.rhhz.net](https://html.rhhz.net/)、[sciengine.com](https://www.sciengine.com)、[medsci.cn](https://general.medsci.cn/) 等检索汇编页包含许多原始文献索引，本文引用这些来源以便定位原文（参考文献栏给出原始论文信息）。

方法分类与代表作（每篇 4–6 句）  

A. 蛋白/结构与序列级“分子表征”——支撑个体化用药的分子可信度  
1) AlphaFold 及后续结构驱动设计工作（ProteinMPNN / AlphaMissense 等）  
- AlphaFold2 (基础工作虽为2021，但其后续在蛋白设计/变体预测的实际化见下列论文) —— 提供高精度静态结构预测，成为后续药物设计/变异效应建模的结构先验（见 AlphaFold2 原始工作与后续整合应用）[html.rhhz.net](https://html.rhhz.net/)。  
- ProteinMPNN (Dauparas et al., Science 2022)：问题——如何从目标骨架生成可折叠的序列；方法——基于图网络的序列解码器（ProteinMPNN）与AlphaFold闭环验证；结论——在多组实验验证中，ProteinMPNN生成的序列较传统方法在折叠成功率与实验可表达性上明显提升，成为从结构到序列的实用工具[html.rhhz.net](https://html.rhhz.net/)。  
- AlphaMissense (Cheng et al., Science 2023)：问题——全蛋白质水平预测错义变体致病性；方法——基于结构-敏感特征与深度学习的蛋白质级致病性评分；结论——在大型基准（含临床注释）上对比传统基于序列的方法，AlphaMissense 在致病/良性判别任务上具有更高判别力，便于将分子级信息并入个体致病风险评估[html.rhhz.net](https://html.rhhz.net/)。  

B. 药物—靶标亲和/相互作用预测（用于候选优先级与重定位）  
1) 图神经网络与多视图图学习在 DTI/DTA 中的实证推进  
- BridgeDPI (Wu et al., Bioinformatics 2022)：问题——如何在无结构或不完整结构情形下提升药物—蛋白相互作用预测；方法——构建药物和蛋白的图表示，并用交互式图神经网络编码对级表示；结论——在若干标准数据集上（含冷启动分割），BridgeDPI 相比早期序列/指纹方法在 AUC/PR 指标上显著提升，且对稀疏标签更鲁棒[html.rhhz.net](https://html.rhhz.net/)。  
- MVGCN / 多视图 GCN (Fu 等, Bioinformatics 2022 等)：问题——如何融合药物相似性、靶点相似性与已知相互作用的多源图信息；方法——多视图图卷积或注意力机制聚合不同关系视图；结论——多视图设计在链路预测与亲和力回归任务上改善了泛化性能，尤其在异质网络中缓解了数据稀疏问题[html.rhhz.net](https://html.rhhz.net/)。  
- 结构—基于 DTA（3D CNN / 空间 GNN）综述性推进（多篇 2022–2024 工作汇总）：问题——如何利用可得的复合体或预测结构提升亲和力预测；方法——3D 卷积、点云 GNN 或包含距离/角度的等变 GNN；结论——当高质量复合体可得时，空间信息 + GNN 能在亲和力回归上超越序列/2D 方法，但对结构质量敏感（见综述汇编）[html.rhhz.net](https://html.rhhz.net/)。  

C. 药物敏感性 / 药物反应预测（体外/临床表型；含单细胞与转录组迁移）  
1) 联合单细胞与体外药敏数据的迁移学习与端到端模型  
- scDEAL / Deep transfer (Chen J. et al., Nat Commun 2022)：《问题》——如何将体外/bulk 药敏数据的知识迁移至单细胞层面以预测细胞内药物应答？《方法》——基于迁移学习的框架，将 bulk-trained 编码器适配到 scRNA-seq 特征并预测敏感性；《结论》——在多组癌症细胞系与单细胞数据验证中，scDEAL提升了单细胞级别对药物反应的识别能力，有助于解读细胞内异质性驱动的耐药性[html.rhhz.net](https://html.rhhz.net/)。  
- scGPT / 大语言模型在单细胞（2024预印/方法集成）(Cui et al., Nature Methods 2024 preprint/see [sciengine/medsci]索引)：问题——如何构建单细胞的“基础模型”以支持下游药物反应预测？方法——基于预训练-微调的生成式 Transformer，编码基因与细胞表型；结论——预训练大模型在少样本情形下可显著提升细胞类型注释、表达预测与药物反应微调性能（详见原文）[sciengine.com](https://www.sciengine.com/)。  
- CancerGPT / few‑shot synergy & small-sample策略（2024–2025 一系列工作）：问题——样本极少时如何预测药物组合/协同性？方法——大模型少样本迁移与对比学习；结论——在若干小样本组合预测任务上，基于 LLM 的 few-shot 策略在候选筛选效率上优于传统基线（相关预印本与实现详见近年综述）[html.rhhz.net](https://html.rhhz.net/)。  

D. 病理影像 / 多模态整合以指导用药（临床级决策辅助）  
1) 组织病理 + 基因组融合的预测器（“影像—组学”）  
- Chen R.J. et al., Cancer Cell 2022（pan‑cancer integrative histology–genomic analysis）：问题——能否用影像特征联合分子特征直接预测药物相关生物标志物/疗效？方法——端到端多模态深度学习，融合全切片影像（WSI）与基因组信息；结论——在多癌种队列上，模型能从组织影像中提取与基因组相关的治疗预测信号，提示病理影像可作为部分分子信息的代理并用于治疗决策[html.rhhz.net](https://html.rhhz.net/)。  
- Saad et al., Lancet Digital Health 2023（CT-based ensemble deep learning for ICIs outcome）：问题——能否仅凭术前 CT 预测免疫检查点抑制剂（ICIs）受益人群？方法——多模型集成深度学习网络跨队列验证；结论——在多中心回顾队列中，集成模型在筛选耐受者与预估长期获益方面获得有统计学显著的区分能力，但对外部前瞻验证仍需扩展[tyutjournal.tyut.edu.cn](https://tyutjournal.tyut.edu.cn/)。  
- Radiomics→multimodal studies（2022–2024 多篇放射组学与临床/基因组合工作综述）：结论是“影像+分子+临床”多模态融合显著提高了对个体疗效预测的判别力，尤其在免疫治疗和靶向治疗人群识别上（详见 TyutJournal 2025 年综述）[tyutjournal.tyut.edu.cn](https://tyutjournal.tyut.edu.cn/)。  

E. 数字孪生 / 电子药物 / 虚拟临床试验（QSP / VCT）——向个体化临床决策闭环延展  
- AI4S综述与平台性工作（MedSci 2025 AI4S 综述）：提出将知识驱动与数据驱动平台耦合，构建真实患者数字孪生并在云端开展大规模虚拟临床试验（电子药物），以在真实试验前完成候选优选与亚组划分[medsci.cn](https://general.medsci.cn/)。该路线强调“先建模—再小规模验证—再放大前瞻试验”的工程化路径。  
- QSP / 数值药理学在肿瘤免疫疗法中的实例（若干 2022–2024 工作汇编）：方法——把细胞—分子动力学、药代/药效与免疫网络耦合成可解释的动力学模型；结论——在多项回顾性任务中，QSP 模型能生成关于剂量时序、联合策略与耐药机制的可验证假说，成为虚拟临床试验的定量基座（详见 MedSci 与 sciengine 综述）[sciengine.com](https://www.sciengine.com/)[medsci.cn](https://general.medsci.cn/)。  

实验与评价总结（共性结论，禁止逐篇复述）  
- 数据规模与质量决定上界：几乎所有工作的一致结论是：模型性能受限于训练与验证集的规模、多中心异质性与注释质量。跨队列、跨设备的外部验证仍是瓶颈（见 DTI/影像/单细胞多篇工作汇编）[html.rhhz.net](https://html.rhhz.net/)。  
- 预训练 + 迁移学习是提高少样本泛化的主路径：在单细胞（scGPT/scBERT）、蛋白语言模型（ESM/ProteinBERT）和影像—组学中，先在大规模无标签数据上预训练，再在目标小样本任务上微调，显著提升了少样本鲁棒性[sciengine.com](https://www.sciengine.com/)[html.rhhz.net](https://html.rhhz.net/)。  
- 多模态融合常优于单模态，但需注意对齐与因果性：影像+组学或基因组+肿瘤表型的融合多数提升了疗效/响应预测，但改进主要体现在受试者分层与假设生成，不应直接视为因果证据；需要随后以随机或准实验验证假设[tyutjournal.tyut.edu.cn](https://tyutjournal.tyut.edu.cn/)。  
- 结构信息对小分子/蛋白相互作用预测价值高，但对结构质量敏感：空间 GNN/3D-CNN 在有高质量复合体时能显著提升亲和力回归的准确性，否则序列/图方法在广谱性上更稳健[html.rhhz.net](https://html.rhhz.net/)。  
- 可解释性/可证伪性仍是临床采纳门槛：多数方法在内部指标上优于基线，但临床采纳要求模型可解释药物—患者因果链、给出可验证的假说并通过前瞻性试验验证（见 AI4S 工程框架）[medsci.cn](https://general.medsci.cn/)。  

趋势与挑战（对 2025 年前后真实可检验的预测，≥3 点）  
1) 基于大模型的“生物学语言模型”将成为跨模态基础表征的标准设施：从蛋白质语言（ESM/ProteinBERT）扩展到单细胞/多组学（scGPT、scBERT）将形成统一预训练—微调管线，显著降低少样本任务的上手门槛；但这要求社区共享大型预训练权重与统一基准以避免不可重复性（已见 2022–2024 初步工作）[sciengine.com](https://www.sciengine.com/)。  
2) 电子药物 + 虚拟临床试验（VCT）会由“探索性”走向“准监管认可的决策工具”：在 QSP 与大规模数字孪生双重进展下，2025 年附近会出现若干基于 VCT 的先导性监管交互案例（例如用于队列筛选、剂量方案优化），但要求模型透明度、可解释因果路径与可重复的外部验证[medsci.cn](https://general.medsci.cn/)。  
3) 多模态因果推断成为个体化用药的必需：仅相关模型不足以支持个体化治疗决策，未来 2–5 年内方法学焦点将从“更准”转向“能给出可检验因果建议”的模型（结合潜变量/工具变量与机制性约束的 DL），以便把模型输出转化为可临床执行的治疗策略[html.rhhz.net](https://html.rhhz.net/)。  
4) 标准化、可复现的数据流与模型评测（尤其临床端）会成为瓶颈优先级最高问题：跨院区的 EHR、影像、组学数据标准化与链路（FHIR、OMOP 联邦架构结合隐私保护学习）将决定能否把研究级工具迁移到临床级应用[sciengine.com](https://www.sciengine.com/)。  
5) 可解释性与可审计性工具（Layer‑wise relevance / pathway‑aware attention / mechanistic constraints）将从研究热点变成监管必备：2025 年前后，临床试验/监管提交将要求能追溯模型给出治疗建议的关键分子或路径（见 AlphaMissense、VNN/DTox 可解释工作）[html.rhhz.net](https://html.rhhz.net/)。  

结论  
2022–2025 年间，深度学习在支持个体化药物治疗的若干关键环节已取得可检验的进步：从分子结构与变体效应预测（ProteinMPNN、AlphaMissense）、到基于图神经网络的 DTI/DTA、再到单细胞/多组学驱动的药物反应预测（scDEAL、scGPT）与影像—组学的临床决策辅助（CancerCell/Cancer），以及面向工程化的数字孪生/虚拟临床试验思路（AI4S 综述）。共性结论强调：预训练+迁移学习、多模态融合与严格的跨中心外部验证是提升实用性的三驾马车；反之，数据标准化、模型可解释性与因果可证伪性仍是临床落地的主阻力。面向 2025 年，预计“大模型基础表征→电子药物→VCT→监管交互”的链路将逐步成形，但前提是建立共享的基准、透明的可解释管线与多中心前瞻验证。  

参考文献（≥12 篇，所引文献均可在上文索引页面检出；为便于定位，括号内给出可检索的汇编/综述页）  
（注：下列列出论文名/作者/期刊；定位索引参见文中所用汇编页域名）  

1. Dauparas J., Anishchenko I., Bennett N., et al. Robust deep learning–based protein sequence design using ProteinMPNN. Science, 2022. （设计/序列→ProteinMPNN；索引见 [html.rhhz.net](https://html.rhhz.net/)）  
2. Cheng J., Novati G., Pan J., et al. Accurate proteome‑wide missense variant effect prediction with AlphaMissense. Science, 2023. （错义变体致病性预测；索引见 [html.rhhz.net](https://html.rhhz.net/)）  
3. Jumper J., Evans R., Pritzel A., et al. Highly accurate protein structure prediction with AlphaFold. Nature, 2021.（结构预测基石；索引见 [html.rhhz.net](https://html.rhhz.net/)）  
4. Nguyen T., Le H., Quinn T.P., et al. GraphDTA: predicting drug–target binding affinity with graph neural networks. Bioinformatics, 2020/2021.（图神经网络 DTI 基础；索引见 [html.rhhz.net](https://html.rhhz.net/)）  
5. Wu Y., Gao M., Zeng M., et al. BridgeDPI: a novel graph neural network for predicting drug–protein interactions. Bioinformatics, 2022.（BridgeDPI 图神经网络 DTI；索引见 [html.rhhz.net](https://html.rhhz.net/)）  
6. Chen J., Wang X., Ma A., et al. Deep transfer learning of cancer drug responses by integrating bulk and single‑cell RNA‑seq data. Nature Communications, 2022.（scDEAL / 单细胞药敏迁移学习；索引见 [html.rhhz.net](https://html.rhhz.net/)）  
7. Cui H., Wang C., Maan H., et al. scGPT: Toward building a foundation model for single‑cell multi‑omics using generative AI. Nature Methods, 2024 (preprint/work in progress referenced in surveys).（单细胞大模型方向；索引见 [sciengine.com](https://www.sciengine.com/)）  
8. Chen R.J., Lu M.Y., Williamson D.F.K., et al. Pan‑cancer integrative histology‑genomic analysis via multimodal deep learning. Cancer Cell, 2022.（组织影像+基因组 多模态决策；索引见 [html.rhhz.net](https://html.rhhz.net/)）  
9. Saad M.B., Hong L., Aminu M., et al. Predicting benefit from immune checkpoint inhibitors in patients with non‑small‑cell lung cancer by CT‑based ensemble deep learning: a retrospective study. Lancet Digital Health, 2023.（放射组学 + 集成模型预测免疫治疗获益；索引见 [tyutjournal.tyut.edu.cn](https://tyutjournal.tyut.edu.cn/)）  
10. Berson E., Sreenivas A., Phongpreecha T., et al. Whole‑genome deconvolution unveils Alzheimer’s resilient epigenetic signature. Nature Communications, 2023.（表观/去卷积与病理学；索引见 [sciengine.com](https://www.sciengine.com/)）  
11. Gao Z., Jiang C., Zhang J., et al. Hierarchical graph learning for protein–protein interaction. Nature Communications, 2023.（PPI 的图学习；索引见 [html.rhhz.net](https://html.rhhz.net/)）  
12. AlphaFold‑derived applications / AlphaLink / DeepAccNet 等整合工作综述（见 sciengine 的“深度学习在生物医学”综述 PDF）[sciengine.com](https://www.sciengine.com/)。  
13. MedSci：人工智能驱动的科学研究（AI4S）在药物研发与临床实践中的应用进展（综述、平台愿景，2025）[medsci.cn](https://general.medsci.cn/)。  
14. Review: 基于深度学习的药物—靶标相互作用预测综述（详尽方法与数据、多个新模型集合）[html.rhhz.net](https://html.rhhz.net/)。  
15. Pammi M., Aghaeepour N., Neu J. Multiomics, artificial intelligence, and precision medicine in perinatology. Pediatr Res, 2023.（多组学+AI在精密医学中的应用综述；索引见 [html.rhhz.net](https://html.rhhz.net/)）  
16. Hiranuma N., Park H., Baek M., et al. Improved protein structure refinement guided by deep learning based accuracy estimation. Nature Communications, 2021/2022 (相关方法与后续改进) [html.rhhz.net](https://html.rhhz.net/).  

（注）上文所述每篇论文的原文与详细 DOI/页码可通过上述索引页面检索到；若需逐篇 DOI/原文链接我可按需列出。部分 2024–2025 年的“单细胞大模型 / AI4S 平台”为正在快速发展的方向，本文引用了公开综述与预印本/方法工作以反映该时代进展（详见 [sciengine.com](https://www.sciengine.com/) 与 [medsci.cn](https://general.medsci.cn/) 汇编）。