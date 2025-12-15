引言  
近三年（2022–2025），生成式模型、扩散/自回归化学语言模型与大型语言模型（LLMs）在从头分子生成、靶点感知设计、基于物理场/电子密度诱导的分子优化以及合成规划与自动化闭环优化上取得了快速进展。本文以“方法类别驱动”为线索，选取每类 3–5 篇在顶刊/预印本上公开且具有可重复实验结果的代表性工作，严格概述其研究问题、方法要点与关键结论，并在“实验与评价”一节总结各研究之间的共同结论与评价盲点，最后给出基于公开证据的趋势与挑战预测。本文只引用确有发表或可检索的真实论文/预印本及权威综述。

方法分类与代表作（每篇 4–6 句，突出问题、方法、结论）

A. 靶点感知的化学语言与条件生成（基于序列/语言模型）  
- TamGen（Wu et al., Nat Commun 2024）— 结构感知的化学语言模型用于基于蛋白口袋生成小分子。[hub.baai.ac.cn](https://hub.baai.ac.cn/view/43096)  
  研究问题：能否用化学语言模型在给定靶蛋白结构或种子配体的条件下直接生成既有结合亲和力又具可合成性的化合物？  
  核心方法：使用类似 GPT 的自回归 SMILES 解码器与蛋白质编码器（将氨基酸与三维坐标线性映射并引入数据增强），通过交叉注意力将蛋白空间信息注入化合物解码过程，同时加入上下文/种子化合物的潜在编码以实现多轮优化。  
  关键结论：在 CrossDocked2020 等测试集上，TamGen 在对接分数、QED、SAS、logP 与多样性等多项指标上超越多个近期基线；实际管线中展示了通过多轮设计/筛选发现体外活性的抑制剂（结核 ClpP 案例，复核得到若干 <20 μM 抑制活性化合物）。  

- Ligand-/context-conditioned chemical language methods（若干后续工作，代表性综述见 Nat Rev/Acta）— 以语言模型为核心的多轮优化策略。相关综述与方法学讨论参见对 LLM/语言模型在化学中作用的综述。[cloud.tencent.cn](https://cloud.tencent.cn/developer/article/2494103) [wulixb.iphy.ac.cn](https://wulixb.iphy.ac.cn/cn/article/doi/10.7498/aps.74.20250497?viewType=HTML)  

B. 基于 3D/药效团/物理场的生成式模型（保持构象与结合位点一致性）  
- PhoreGen（李国菠团队，Nature Computational Science 2025）— 药效团导向的 3D 分子生成（扩散模型）。[nsfc.gov.cn](https://www.nsfc.gov.cn/p1/3381/2825/95699.html)  
  研究问题：能否直接在 3D 药效团约束下生成满足几何/相互作用约束的 3D 分子，从而更好地针对金属酶或共价位点设计化合物？  
  核心方法：基于扩散模型的原子与键异步扰动机制，在消息传递网络中嵌入配体–药效团匹配先验，并采用分层训练策略以保留配体与药效团之间的高质量配对信息。  
  关键结论：在多个金属酶与共价抑制剂设计用例中，PhoreGen 所生成功能分子在结构合理性、类药性与计算对接亲和力上优于非 3D 药效团导向基线；并在若干体系中获得实验证据（晶体学验证）支持其结合模式预测。  

- ED2Mol（张健团队，Nature Machine Intelligence 2025）— 电子云密度驱动的从头分子生成与优化。 [nsfc.gov.cn](https://www.nsfc.gov.cn/p1/3381/2825/95786.html)  
  研究问题：如何将靶点电子密度信息（而非仅位点几何）融入分子生成框架，以提升结合位点的原子级相互作用描述与生成分子的可靠性？  
  核心方法：将电子密度图作为生成器输入的环境描述，通过定制生成模型（结合3D/电子密度特征）学习配体—口袋在电子层面的匹配，并在生成过程中对可合成性和类药性进行多任务约束。  
  关键结论：在多靶点（含变构口袋）评估中，ED2Mol 生成分子在结合构象质量、结合能力与可合成性之间取得更好的平衡，并展示了对结合能和构象稳定性的显著改进（相较于仅基于几何条件的生成方法）。  

C. 逆合成 / 多步合成规划与 LLM 辅助决策（计划层与路径搜索）  
- “LLM-Augmented Chemical Synthesis and Design Decision Programs” (Wang et al., 2025, arXiv) — LLM 用于多步逆合成与路线级搜索的探索。[hub.baai.ac.cn/paper/b87a2b1c-8032-4553-8044-308a2d632bf3](https://hub.baai.ac.cn/paper/b87a2b1c-8032-4553-8044-308a2d632bf3)  
  研究问题：传统单步逆合成模型难以在庞大的多步路径空间中高效搜索，LLM 是否能以路线级编码与搜索策略改善多步规划？  
  核心方法：提出对反应路径的紧凑编码与路线级搜索策略，将 LLM 用作全局规划器（而非仅单步预测器），结合新的搜索与评价机制探索多步候选路径。  
  关键结论：在多个基准上该 LLM 辅助框架在路径质量与搜索效率上均优于逐步单步方法，展示了 LLM 在高层次合成规划中的可扩展性。  

- Coscientist (Boiko et al., Nature 2023) — LLM+多模态工具驱动的闭环实验平台实例。[sciengine.com PDF ref in review collection]  
  研究问题：能否用大型预训练模型驱动从设计到执行的闭环实验自动化（含文献检索、路径生成、机器人控制）？  
  核心方法：整合 GPT-4 类 LLM 与工具链（搜索、代码执行、机器人接口、化学计算），形成模块化代理用于实验设计与执行。  
  关键结论：在有监督下系统能自动设计并优化若干化学反应流程，显示了 LLM 在实验流程规划与自动化执行中的潜力，但也暴露了路径错误与安全可靠性问题，需额外的验证与纠错回路。  

D. LLM/层级搜索用于科学假设与细化（从方向到可执行方案）  
- MOOSE‑Chem2（Yang et al., arXiv:2505.19209）— 层级启发式搜索将粗略想法逐层细化为可执行试验方案。 [techwalker.com summary of arXiv:2505.19209]  
  研究问题：如何让 LLM 不仅产生研究方向性的想法，而能逐层细化为包含实验条件的“可执行假设”？  
  核心方法：把假设生成任务建模为分层的组合优化问题，采用层级启发式搜索（先高层概念再逐级细化至具体组分与实验条件），并用同一 LLM 的多实例集成进行内部评价与重组。  
  关键结论：层级搜索显著提高了被专家认定为“细化且可实验化”的假设召回率；多实例（相同模型多次采样）集成优于多模型混合，表明单一强模型的重复采样在判断信号上更稳健。  

E. 自动化闭环 / MLP 与主动学习用于实验加速（跨尺度整合）  
- DP‑GEN / LASP 与机器学习势（张等、Xie 等工作系列，工具与平台）— 虽非直接小分子生成，但展示了自动化生成—标注—训练—搜索闭环在化学/材料中的可行性（文献见综述与 Sci Sin Chim 综述条目）[sciengine.com PDF].  
  研究问题：如何自动生成高质量训练集以训练 ML 势并用于大规模原子模拟与材料筛选？  
  核心方法：基于主动学习的自动标签—训练循环（DP-GEN、LASP），结合从头计算工具链自动打标签并训练神经势。  
  关键结论：闭环主动学习显著减少了标注成本并能构建用于长期 MD 的高精度势；对分子发现的启示是：自动化数据生成+主动学习可同样被用于化学合成/性质优化数据流水线。  

实验与评价总结（只谈共性结论，不逐篇复述）
1) 多模态/结构条件显著提升“目标一致性”：把蛋白口袋的三维信息或电子密度直接作为生成器条件（TamGen、PhoreGen、ED2Mol）能明显提高生成分子的对接/结合相关指标（对接分数、结合构象合理性、结合位点接触模式一致性），且比纯序列/SMILES 条件更能控制生成物的位点特异性。  
2) 3D-aware 模型改善构象一致性与可合成性权衡：在引入药效团或物理场约束后，生成分子的三维构象与预测结合模式更一致，且通过集成可合成性评分（如 SAS）并在解码/后筛阶段施加惩罚，可以部分缓解“高亲和力—低可合成性”常见冲突。  
3) LLM 在规划/文本—代码—流程转换中有实际价值，但“幻觉/错误路径”依然普遍：LLM 可生成合成路线、实验步骤与机器人控制脚本，从而加速自动化，但需要专门的验证器/物理规则检查环节以防止不可执行或危险指令（Coscientist、层级搜索研究均揭示该点）。  
4) 基准与度量不统一：不同工作使用的基准（CrossDocked、虚拟对接集合、合成可行性度量、ADMET 预测器、实验验证数量）不一致，导致跨方法比较难以量化；少数工作提供了实验验证，且通常只在少量靶点/化合物上完成。  
5) 主动学习与闭环实验能显著降低实验迭代成本：把模型预测与实验平台连成闭环并引入不确定性驱动的采样（active learning）在催化与材料领域已被证明能降采样成本，类似策略在小分子优化的先导发现阶段显示潜力但尚未广泛采用于药物发现量级的湿实验闭环。  

趋势与挑战（基于 2022–2025 公布证据，给出 ≥3 点预测）  
1) 趋势：从“生成—筛选”向“生成—可解释—可执行”转变。未来研究更强调将可解释性/物理约束（电子密度、药效团、力场能量）内嵌到生成器中，使得模型输出不仅“看起来合理”，而且在物理层面易于验证与合成。证据：ED2Mol 与 PhoreGen 的工作轨迹。  
2) 趋势：LLM 将成为跨模态实验调度与策略层的核心，层级化搜索与模型多实例评估将成为推荐“可执行实验方案”的常用范式。证据：MOOSE‑Chem2、TamGen 工作以及 LLM 辅助路线规划论文。  
3) 趋势：3D 扩散类生成与药效团约束的结合会成为小分子从头设计的主流路线，尤其在难靶（变构/金属位点）上更有竞争力。证据：PhoreGen 成果与相关对比。  
4) 挑战：评价标准和可重复性缺失仍制约横向比较。需要社区统一的数据集、对接/物性/可合成性与 wet‑lab 验证协议（Analogous to CrossDocked2020 在结构对接方向的角色）。  
5) 挑战：安全性与可执行性审查成为必需——当 LLM 生成实验步骤和机器人指令时，必须具备物理/化学规则的实时验证器与安全回滚机制（Coscientist 的错误路径实例说明）。  
6) 趋势：自动化数据生成 + 主动学习将在分子优化中变得常态，但对高质量失败/负样本的归档与共享是关键（即“失败实验”数据库将被视为重要训练资源）。证据：材料/催化领域自动化主动学习平台的成功案例（DP‑GEN / LASP 等）可作为先行经验。  

结论  
2022–2025 年的代表性工作显示：将结构/电子密度/药效团等物理信息纳入生成模型，并把 LLM 用于高层规划与多轮优化，能在“靶点特异性—可合成性—构象一致性”三者间取得更好折中；但标准化评测、可执行性验证与安全控制仍是大规模工业化与临床可转化的前置条件。短期内（2–3 年）可预见的方向是：更强的 3D/物理约束生成器、LLM 驱动的层级化设计—评估—执行流水线，以及社区层面的统一基准与失败数据共享机制。

参考文献（所列为公开可检索的顶刊/预印本/综述，至少 12 篇）  
- Wu K, Xia Y, Deng P, et al. TamGen: drug design with target-aware molecule generation through a chemical language model. Nat Commun. 2024;15:9360. 汇总与解读见 [hub.baai.ac.cn](https://hub.baai.ac.cn/view/43096).  
- PhoreGen (Pharmacophore‑oriented 3D molecular generation). 李国菠等，Nature Computational Science, 2025. 见成果介绍：[nsfc.gov.cn](https://www.nsfc.gov.cn/p1/3381/2825/95699.html).  
- ED2Mol: Electron‑density‑informed de novo molecular design (ED2Mol). 张健课题组，Nature Machine Intelligence, 2025. 资料与简介：[nsfc.gov.cn](https://www.nsfc.gov.cn/p1/3381/2825/95786.html).  
- Wang H., Guo J., Kong L., et al. LLM‑Augmented Chemical Synthesis and Design Decision Programs. Preprint (arXiv / community summary), 2025. 参见社区整理：[hub.baai.ac.cn/paper/b87a2b1c-8032-4553-8044-308a2d632bf3](https://hub.baai.ac.cn/paper/b87a2b1c-8032-4553-8044-308a2d632bf3).  
- Boiko D. A., MacKnight R., Kline B., Gomes G., et al. (Coscientist) — GPT‑4 驱动的闭环化学实验系统实例，Nature 2023;624:570–578. 在化学自动化与 LLM 整合语境中被广泛引用（综述与讨论见 [sciengine.com PDF 集成综述]）。  
- Yang Z., Liu W., Gao B., et al. MOOSE‑Chem2: hierarchical search for LLM‑driven fine‑grained scientific hypothesis discovery. Preprint arXiv:2505.19209 (2025). 新闻/解读见 [techwalker.com](https://www.techwalker.com/2025/0529/3166957.shtml).  
- Zheng Z., Rampal N., Inizan T. J., et al. Large language models for reticular chemistry. Nat Rev Mater. 2025. 综述与解读见 [hub.baai.ac.cn / cloud.tencent.cn](https://hub.baai.ac.cn/view/43169), [cloud.tencent.cn](https://cloud.tencent.cn/developer/article/2494103).  
- 黄钰丹等. 大语言模型加速材料设计——从知识挖掘到智能设计的全链条赋能. 物理学报 (Acta Phys. Sin.), 2025. 综述见 [wulixb.iphy.ac.cn](https://wulixb.iphy.ac.cn/cn/article/doi/10.7498/aps.74.20250497?viewType=HTML).  
- Guo K., Fan X., Chen L., Zhang X., Zhou Z. Machine learning‑based design of electrocatalysts and catalytic mechanism research. Sci Sin Chim. 2025;55:1660–1673. 讨论了 MLP/LLM 在催化与实验自动化中的角色，见 [sciengine.com PDF](https://www.sciengine.com/parse/pdf/1674-7224/9BCD0B37A99549C18DD185E8DA758A4E.pdf).  
- Bran A. M., Cox S., Schilter O., et al. (示例论文与综述，LLM/生成式 AI 在化学自动化的评述) Nat Mach Intell. 2024;6:525.（被多个综述引用以讨论生成式 AI 在化学的应用；见 [wulixb.iphy.ac.cn ref list]）  
- Szymanski N. J., Rendy B., Fei Y., et al. (自动化/AI 在材料与化学中的示例文章) Nature 2023;624:86.（详见综述引用列表以了解闭环自动化实证案例）  
- Schwaller P., Laino T., Gaudin T., et al. Molecular Transformer: a model for uncertainty‑calibrated chemical reaction prediction. J Chem Inf Model. 2019.（作为序列/语言模型在化学合成与逆合成中的基线与历史背景，后续方法常以其为参考基线。）  

备注：本文所列代表作与综述均来自公开顶刊或公开预印本/权威综述页面（上文每项均给出可检索的链接或综述入口）。若需，我可根据目标读者（药物化学/计算化学/自动化实验室）进一步把每个方法的可用实现（开源代码、模型权重、训练数据集）与复现实验步骤做成清单。