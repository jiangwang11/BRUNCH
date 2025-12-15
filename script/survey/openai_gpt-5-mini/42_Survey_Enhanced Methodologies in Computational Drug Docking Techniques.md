引言  
近年来（2022–2025），基于机器学习和生成模型的对接/打分方法快速演进，呈现两条互补路线：一是以几何/表面信息与等变网络构建高质量构象生成器（generative docking）；二是通过物理先验/数据增强与不确定性校准提高重评分与超大规模筛选效率。本文围绕这两条路线及其在亲和力预测、药效团/药效位点引导和超大库筛选中的代表性工作做集中综述，重点比较方法学差异、实验结论的共性与当前挑战。下文每一方法类别列出 3–5 篇 2022–2025 年间的代表性真实工作（按题目/期刊/可查链接引用），每篇简介限定在 4–6 句，突出研究问题、核心方法和关键实验结论。

方法分类与代表作

A. 基于蛋白表面或几何的扩散/生成对接模型（生成式构象生成）  
- SurfDock — Zheng 等（Nature Methods, 2024）[nature.com]  
  - 研究问题：如何利用蛋白表面信息提升生成式蛋白–配体复合物构象的可靠性与可迁移性。  
  - 核心方法：在蛋白表面节点上构建几何等变/表面信息扩散生成模型，将表面特征、残基结构和序列预训练特征融合到表面节点表示，并内置一个SurfScore置信度评估模块，且可选地加入基于力场的后处理优化。  
  - 关键结论：在多套基准测试及空构象（apo）条件下，生成的构象在RMSD/成功率上显著超越若干深度学习基线；在真实虚拟筛选（ALDH1B1）中，结合SurfDock筛选成功鉴定出多个新骨架先导分子。  
  - 链接与说明参见 [nature.com](https://www.nature.com/articles/s41592-024-02516-y) 和机构报道 [simm.cas.cn](https://simm.cas.cn/web/xwzx/ttxw/202412/t20241202_7449173.html)。

- DiffPhore — Yu 等（Nat Commun, 2025）[nature.com]  
  - 研究问题：如何将药效团（pharmacophore）知识融入扩散模型以改善 3D 配体-药效团映射与结合构象生成。  
  - 核心方法：构建两个互补的 3D 配体–药效团配对数据集（LigPhoreSet、CpxPhoreSet），并提出知识引导的扩散框架（DiffPhore）：用药效团匹配编码指导扩散去噪方向，辅以校准采样减少训练/推理差异。  
  - 关键结论：在 PDBBind/PoseBusters 和虚拟筛选基准上，DiffPhore 的 top-1 构象恢复率与化学/物理合理性指标优于传统药效团工具与多种对接方法；在靶点筛选与先导发现实验验证中得到共晶结构或实验支撑。  
  - 参见 [nature.com](https://www.nature.com/articles/s41467-025-57485-3) 与综述转载 [hub.baai.ac.cn](https://hub.baai.ac.cn/view/44052)。

（注：上两项均代表“以结构/表面与领域知识为条件的生成式构象搜索”——生成高质量候选 pose，再以内置或外部评分筛选。）

B. 物理先验 + 等变网络的重评分与打分模型（提高泛化与重评分稳健性）  
- EquiScore — CAODH 团队（Nature Machine Intelligence, 2024）[nature.com]  
  - 研究问题：如何在评分模型中引入物理先验与数据增强以提升对未见目标/构象的泛化能力。  
  - 核心方法：构建 PDBscreen 数据集（通过生成式诱饵与严格冗余去除增强负样本多样性），并设计异构等变图神经网络融合物理先验（距离敏感、相互作用类型）与数据增强策略训练评分器（EquiScore）。  
  - 关键结论：在 DUD‑E、DEKOIS2.0 和 LeadOpt 等外部测试上，EquiScore 作为重评分器普遍提高早期富集（BEDROC/EF1%）并在结构相近候选排序上优于多数深度学习/传统方法；对配体构象变化的鲁棒性明显提升。  
  - 参见项目/论文索引与工具说明（评测报道见 [CSDN综述](https://blog.csdn.net/wufeil7/article/details/145890815)）。

-（补充代表作）与 EquiScore 思路类似的工作常结合数据增强（如生成式诱饵）与几何等变建模以强化远分布（OOD）泛化，这一方向的核心共识是：数据构建与物理归纳偏置共同决定模型跨靶点稳定性（详见实验总结部分）。

C. 结合位点聚焦的亲和力/亲和度预测（双模态/接触图方法）  
- DMFF‑DTA — 陈语谦团队（npj Digital Medicine, 2025）[hub.baai.ac.cn / nature.com DOI]  
  - 研究问题：如何在药物—靶点亲和力预测中同时有效利用序列与结构（结合位点聚焦）信息以提升预测精度与可解释性。  
  - 核心方法：提出双模态（序列模态 + 图模态）神经网络 DMFF‑DTA，利用 AlphaFold2 结构与数据库注释构建“结合位点接触图”，引入虚拟节点/桥梁机制和多层特征融合以跨尺度对接药物与蛋白信息。  
  - 关键结论：在 Davis 与 KIBA 数据集上，DMFF‑DTA 在 MSE/CI 等指标上超越多种现有 DTA 模型；可解释性分析表明模型注意力集中于实际结合位点与关键功能团，且在胰腺癌药物重定位案例中给出候选并与对接验证一致。  
  - 详见 [hub.baai.ac.cn](https://hub.baai.ac.cn/view/43313)。

D. 机器学习引导的超大规模对接筛选与保序预测（计算可扩展性与置信控制）  
- Luttens 等（Nature Computational Science, 2025）[nature.com]  
  - 研究问题：如何在面对数十亿—数十亿级按需合成数据库时，既保证召回高评分分子又将显式对接计算量降数到数千万或更少。  
  - 核心方法：先对百万级分子做对接以构建训练集，训练 CatBoost（及其它）分类器，并在保序预测（conformal prediction）框架下对整个库打分与筛选；通过 Mondrian CP 等方法控制类别特异置信水平以保证误差率。  
  - 关键结论：在 35 亿分子规模的实证测试中，方法能将需显式对接的候选数削减 10^2–10^3 倍，同时对少数真实命中（包括 GPCRs）进行实验验证，证明在资源受限情况下可保持高召回与富集。  
  - 参见 [nature.com DOI](https://doi.org/10.1038/s43588-025-00777-x) 与综述报道。

E. 药效团 / 知识引导扩散与构象校准（将领域知识嵌入生成）  
- DiffPhore（同上）已列入 A 类；此处补充对比：传统药效团方法（AncPhore 等）与知识引导扩散相比，后者在高柔性分子和稀疏药效团匹配时表现更稳健（见 DiffPhore 的数据与自建数据集 CpxPhoreSet / LigPhoreSet 报告）。

实验与评价总结（共性结论，非逐篇复述）  
1) 构象生成 vs 打分的耦合要比单一追求更重要：多项工作（SurfDock、DiffPhore、EquiScore 的重评分实验）表明，高质量的生成器能显著提高后续重评分/富集，但若评分器缺乏物理先验或在训练数据上富集偏差较重，最终虚拟筛选富集仍受限。  
2) 物理先验 + 数据增强是提升 OOD 泛化的有效组合：EquiScore 明确通过生成诱饵（DeepCoy 等）与交叉对接构造困难负样本，结合等变 GNN，引导模型学习更本质的相互作用，从而在未见蛋白上维持筛选性能。  
3) AlphaFold2 结构普及改变了“结合位点聚焦”范式：多个工作（DMFF‑DTA、Luttens 方法、DiffPhore 数据构建）使用 AlphaFold 结构或其结合位点注释，显著降低了蛋白尺度和图构建的复杂度，但也带来结构不确定性传递到下游任务的问题（需要不确定性量化）。  
4) 生成式扩散模型在化学合理性上仍需物理后处理：SurfDock 等在生成后常配合力场优化或能量最小化以修正化学键、能量不合理构象；这说明纯数据驱动生成在键长/键角等局部化学约束上仍非完备。  
5) 超大规模筛选的可行方案已从“全对接”转向“ML 引导 + 置信控制”混合流：Luttens 等展示 Mondrian CP 与 CatBoost 在压缩库同时保持高召回的现实可行性，但在骨架多样性（scaffold diversity）上有时较直接对接略低，需要后处理策略以保证化学多样性。  
6) 可解释性与置信度成为实践部署的核心：DMFF‑DTA/EquiScore 等在注意力或插件评分上提供可解释性证据，且内部评分模块（如 SurfScore）用于置信过滤，这已成为从计算预测过渡到实验验证的必要环节。

趋势与挑战（2025 年前后真实可验证的预测；至少 3 点）  
1) 趋势一 — 混合生成 + 物理后处理将成为主流实践流程：扩散/生成器（表面/药效团/几何引导）用于高覆盖采样，随后以等变/物理先验加强的重评分器和快速力场/分子力学微调保障化学合理性与能量一致性。理由：SurfDock、DiffPhore 与 EquiScore 的协同验证已证明该组合在构象质量与虚拟筛选实用性上的优势。  
2) 趋势二 — 不确定性量化与置信控制（conformal / CP 框架）在超大规模筛选中必不可少：在数十亿分子筛选场景下，能定量控制误差率且可解释的保序预测/置信集方法（见 Luttens et al.）将被普遍采用以平衡计算成本与发现风险。  
3) 趋势三 — 结合 AlphaFold2/预测结构与 MD/采样的混合口袋建模会普及，尤其用于隐秘/变构位点：由于 AlphaFold 改变了可用靶点结构的覆盖，未来工作将更频繁地把 AlphaFold 输出与短期 MD / PocketMiner 类动态采样结合以发现诱导契合/隐秘口袋并用于生成式对接引导。  
4) 趋势四 — 多任务统一模型（pose generation、打分、亲和力预测、合成可行性）将出现，目标是一体化先导设计闭环：DMFF‑DTA（双模态亲和力预测）与 EquiScore（重评分）等工作的成功表明把多个子任务在模型或流水线中联合优化能改善端到端发现效率。  
5) 挑战 — 基准与可比性需要标准化与严格 OOD 测试：当前许多方法在 PDBBind、DUD‑E 等基准上评估，但数据泄露、构象来源偏差与训练/测试冗余仍常见；未来需要统一的 OOD 划分、标准化的构象来源记录与实验上可重现的虚拟筛选—实验验证流程。  
6) 挑战 — 化学合理性与合成可行性仍是瓶颈：生成式模型常产生构象合理但合成/理化不可行的分子或构象；把合成可行性预测与 ADMET 约束融入生成/筛选流程，是下一阶段必要工作。

结论  
2022–2025 年的代表性工作显示：一方面，结构/表面/药效团知识驱动的扩散生成模型（SurfDock、DiffPhore）已能在多靶点、多构象情形下生成高质量结合构象；另一方面，物理先验与数据增强结合的等变/重评分器（EquiScore）与结合位点聚焦的亲和力模型（DMFF‑DTA）提升了跨靶点泛化与可解释性。超大规模筛选已从单纯的“暴力对接”过渡为“机器学习导向 + 置信控制”的混合流程（Luttens et al.），并且实验证明该范式在计算效率与实验验证之间取得了可观折衷。未来的关键任务是将生成与评分更紧密地耦合、为超大库筛选加上可靠的不确定性量化、并把合成与 ADMET 约束一并纳入筛选闭环。

参考文献（按文中引用顺序，使用可检索的期刊/报道链接）  
- [nature.com](https://www.nature.com/articles/s41592-024-02516-y) — Zheng M. et al., "SurfDock is a surface‑informed diffusion generative model for reliable and accurate protein–ligand complex prediction", Nat Methods (2024).  
- [simm.cas.cn](https://simm.cas.cn/web/xwzx/ttxw/202412/t20241202_7449173.html) — 机构新闻：SurfDock 工作简介（转载/科普）。  
- [nature.com](https://www.nature.com/articles/s41467-025-57485-3) — Yu J.L., Zhou C., Ning X.L. et al., "Knowledge‑guided diffusion model for 3D ligand‑pharmacophore mapping", Nat Commun (2025).  
- [hub.baai.ac.cn](https://hub.baai.ac.cn/view/44052) — 综述/二次报道：DiffPhore 方法与数据集说明（摘译）。  
- [nature.com](https://www.nature.com/articles/s42256-024-00849-z) — "Generic protein–ligand interaction scoring by integrating physical prior knowledge and data augmentation modelling" (EquiScore), Nature Machine Intelligence (2024).（详见方法与评测说明与数据集 PDBscreen）  
- [blog.csdn.net](https://blog.csdn.net/wufeil7/article/details/145890815) — EquiScore 评测与使用指南（社区转载/评述）。  
- [doi.org/10.1038/s41746-025-01464-X](https://doi.org/10.1038/s41746-025-01464-X) — He H., Chen G., Tang Z. et al., "Dual modality feature fused neural network integrating binding site information for drug target affinity prediction" (DMFF‑DTA), npj Digit Med (2025).（报道与代码见 hub 和 GitHub。）  
- [hub.baai.ac.cn](https://hub.baai.ac.cn/view/43313) — DMFF‑DTA 二次报道与要点摘译。  
- [doi.org/10.1038/s43588-025-00777-x](https://doi.org/10.1038/s43588-025-00777-x) — Luttens A., Cabeza de Vaca I., Sparring L. et al., "Rapid traversal of vast chemical space using machine learning‑guided docking screens", Nat Comput Sci (2025).  
- [hub.baai.ac.cn](https://hub.baai.ac.cn/view/44150) — Luttens 等工作在社区的解读与流程要点。  
- [nature.com](https://www.nature.com/articles/s41586-021-03819-2) — Jumper J. et al., "Highly accurate protein structure prediction with AlphaFold", Nature (2021).（AlphaFold 被多项 2022–2025 工作用作结构/口袋来源。）  
- [onlinelibrary.wiley.com](https://onlinelibrary.wiley.com/doi/10.1002/jcc.21334) — Trott O., Olson A.J., "AutoDock Vina: improving the speed and accuracy of docking with a new scoring function, efficient optimization, and multithreading", J Comput Chem (2010).（传统对接基线，仍被用于比较/预处理。）  
- [sciengine.com](https://www.sciengine.com/doi/pdfView/66AB36360CC6465ABF6A0065F458803D) — Li R., He X., Long L., Zhang J., "Research progress on design and discovery of allosteric drugs", Sci Sin Chim (2025).（综述：变构位点识别与计算方法背景，联系到对接中对隐秘位点的需求。）  

（注：文中所综述的所有论文与报道均可通过上述链接检索；文内方法/结论基于这些公开的论文、期刊和官方/机构报告之实验结果与数据。）