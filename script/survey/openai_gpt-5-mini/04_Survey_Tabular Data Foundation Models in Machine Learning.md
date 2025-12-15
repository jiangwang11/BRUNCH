引言  
表格（tabular）数据在科学与工业中广泛存在，近三年（2022–2025）研究重心从单任务的树/MLP优化，逐步转向“表格基础模型”（tabular foundation models）与表格—大模型（LLM）混合范式：一类通过大规模合成先验或架构改造实现对小样本/跨域快速泛化（如 TabPFN、TabM）；另一类通过检索、图结构或程序辅助，将结构化表格信息与大型语言模型或检索模块结合（如 TableRAG、HeGTa、Turbo）。本综述按方法类别精选代表性工作，总结其核心思想与实验结论，并给出跨领域共性观察与未来趋势预测。

方法分类与代表作（每篇 4–6 句，突出问题、方法、结论）

A. 基于合成先验与上下文学习的表格基础模型
- TabPFN (Transformer-based Tabular Foundation / arXiv 2022)  
  研究问题：如何在小规模表格数据（≤10k）上实现“零/少样本”快速高质量预测？  
  核心方法：基于大规模合成数据（结构因果模型）预训练一个生成式Transformer，使模型通过上下文学习（in‑context learning）从训练样本直接推断测试样本分布；设计了行/列双向注意与状态缓存以提升推理效率。  
  关键实验结论：在多个小样本基准上，TabPFN 在不需任务特定调参的前提下，显著超越或匹配强基线（如 CatBoost/AutoML），并能实时给出不确定性估计。 参考解读见 [blog.csdn.net](https://blog.csdn.net/2501_91618231/article/details/147474963)。

- TabDDPM (Tabular Diffusion Models / arXiv 2022)  
  研究问题：如何用生成模型同时处理表格中的连续/离散/缺失混合特征以用于数据合成与增强？  
  核心方法：将扩散过程适配到表格域，设计针对混合类型的去噪与编码—解码模块，并采用特征条件化以保持统计一致性。  
  关键实验结论：在多个合成与真实表格合成任务中，TabDDPM 生成样本在下游分类/回归任务上的提升超过若干传统合成方法，尤其在保留复杂联合分布方面表现更好（详见综述汇总 [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/48f6fae9-2762-46ed-8c49-ef0d36c0ef2f)）。

B. 参数高效改造与集成提升的表格深度学习
- TabM (Parameter‑Efficient Ensembling for Tabular MLPs / 2024 summary)  
  研究问题：在不大幅增加参数/算力的前提下，是否能通过集成机制显著提升深度模型在表格任务上的表现？  
  核心方法：提出基于 BatchEnsemble 思路的 TabM，将多个轻量化子模型以参数高效方式内嵌为单一模型，从而获得“集成效果”同时保持参数与延迟友好。  
  关键实验结论：在标准表格基准上，经过参数高效集成的 MLP（TabM）比单模型与若干复杂注意力/检索架构取得更优的性能—说明简单架构 + 集成仍是一条高性价比路径。 见 [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/5dfb55c6-0530-48d1-aafd-93a314a8f811)。

C. 检索/程序辅助与百万令牌规模表格理解
- TableRAG (Million‑Token Table Understanding with LMs / arXiv 2024)  
  研究问题：面对大表格（百万令牌级），如何以较低令牌成本实现准确检索与推理？  
  核心方法：分层检索（schema/pattern + cell-level）结合单元值去重与编码预算，配合程序化求解器（program-aided solver）来执行精确聚合与数值计算；把检索的表格片段作为上下文交给 LLM。  
  关键实验结论：在多个大表格问答基准（合成与真实）上，TableRAG 在令牌效率和准确率上均优于整表输入或简单行采样方法，且对超大表格具有更好的伸缩性。 详见解读 [blog.csdn.net](https://blog.csdn.net/weixin_44025655/article/details/145527034)。

- COTable / Program‑aided hybrids (代表性思想)  
  研究问题：LLM 在数值/程序化推理上存在系统弱点，如何弥补？  
  核心方法：将检索到的结构化内容转为程序或 SQL 片段，由程序执行精确计算，再将结果回写给 LLM；或用 LLM 生成可执行程序（ReAct/Reinforced prompts）。  
  关键实验结论：程序辅助显著提升涉及计算/聚合的表格推理准确率，但在层次化表头或复杂拓扑表格上需保留结构信息以避免语义丢失（见 TableRAG 与续作比较）。

D. 表格—大模型融合：图结构、软提示与自监督对齐
- HeGTa (Heterogeneous Graph‑enhanced LLM for Few‑shot Complex Table Understanding / AAAI 2025 preprint)  
  研究问题：复杂表格（合并单元格、层次表头）在少样本情形下怎样被 LLM 正确理解？  
  核心方法：将表格转为异构图（TABLE/ROW/HEADER/DATA 节点 + 多类型边），用 HGNN 生成节点向量并通过软提示（soft‑prompt）与指令微调将图表示对齐到 LLM；引入三类多粒度自监督任务（行分类、单元匹配、上下文生成）做预训练。  
  关键实验结论：在多项 few‑shot 复杂表格基准上，HeGTa 在保留拓扑信息的同时显著优于线性化或仅 HTML 表示的方法，尤其在层次化表头/关系密集的表格上效果明显。 见 [zhuanzhi.ai](https://zhuanzhi.ai/paper/e4a856f209e289b75a2f0e01e2411219) 与技术解读 [blog.csdn.net](https://blog.csdn.net/h1453586413/article/details/145608216)。

- Turbo (Multimodal Tabular Reasoning with Privileged Structured Information / arXiv 2025)  
  研究问题：表格图像场景下，训练期可用的结构化（特权）信息如何在多模态 LLM 上迁移并提高推理？  
  核心方法：构建结构感知的推理轨迹生成器（DeepSeek‑R1 基础），以特权结构表作为桥接数据生成高质量模态桥接样本，反复生成/选择有利推理路径增强训练。  
  关键实验结论：在有限训练数据（9k）下，相较于之前方法，Turbo 在多个数据集上实现了显著提升（报告中约 +7.2% 的绝对提高），表明利用训练期结构特权能有效提升表格图像到文本推理的迁移。 见 [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/145926)。

E. 表格数据合成与LLM生成（用于隐私/增强）
- Tabby (Tabular Data Synthesis with Language Models / 2025 summaries)  
  研究问题：能否用 LLM 改造的 Transformer 高质量合成表格数据以用于隐私保护或数据增强？  
  核心方法：在标准 Transformer 架构中加入门控混合专家（MoE）与列特定参数，及 “Plain” 后训练技术，使模型能更细粒度地表示列差异并生成高保真表格样本。  
  关键实验结论：在多数据集上合成样本的质量接近或优于真实数据（在下游模型训练表现与统计检验上），对隐私替代与数据增强展示了可行性。 见解读 [blog.csdn.net](https://blog.csdn.net/weixin_40240616/article/details/146077383)。

实验与评价—共性结论（只总结共性）
- 合成先验与预训练（TabPFN、TabDDPM、Tabby）提升小样本泛化：基于结构化合成策略训练的模型在小样本基准上普遍提高了泛化稳定性，且常能在无任务特定调参下直接部署。  
- 结构/拓扑信息关键：对于层次化或跨单元依赖强的表格（如 WTQ Raw、HiTab），保留表格拓扑（图编码、Row/Col 节点）比纯线性化文本表示显著减少语义丢失，从而提高检索/推理准确度（HeGTa、TableRAG 的对比实验支持）。  
- 数值/聚合能力仍是瓶颈：纯 LLM 在数值计算、精确聚合和计数类问题上普遍落后，程序辅助或将检索到的结构化片段交由精确执行器（SQL/程序）是目前最稳健的补救（TableRAG、COTable 等实验结论）。  
- 令牌/计算效率与检索策略相关：对于百万令牌级大表格，分层检索（schema + distinct‑cell retrieval）和值去重是控制上下文长度、提升效率并保持准确性的有效方法（TableRAG 实验体现）。  
- 评价基准与指标碎片化：不同工作使用的基准（WTQ、HiTab、ArcadeQA、BirdQA、合成大表）与度量（回答准确率、令牌成本、下游任务增益）差异大，导致横向比较存在不一致性。

趋势与挑战（2025 年前后真实研究趋势预测，不少于 3 点）
1) 混合架构成为主流：未来 1–2 年内，结构化表格编码器（图神经/行列双向模块）与 LLM 的紧耦合（软提示/adapter/LoRA）将成为主流范式，以兼得拓扑感知与语言推理能力（HeGTa、TabSTAR、Turbo 的方向）。  
2) 检索与程序化求解标准化：为解决数值推理与百万令牌扩展问题，检索层（schema/值）+程序化执行器（SQL/小程序）将被标准化为表格 QA 的基线流水线，研究将集中在检索召回质量与可执行语义的鲁棒映射上（受 TableRAG 启发）。  
3) 合成先验与表格基础模型化：合成数据生成（结构因果先验、扩散或 MoE LLM 合成）将继续被用作预训练源，推进表格基础模型（可零/少样本直接应用）的实用化与产业化（延续 TabPFN 与 Tabby 路线）。  
4) 数值健壮性与可验证性研究加强：围绕数值稳定性、可验证执行与不确定性量化（尤其在金融/医疗场景），将出现更多“可审计”的程序辅助/混合解法与评估协议。  
5) 隐私与合成数据的合规化：合成表格用于隐私替代的合规评估（信息泄露风险、统计可用性）将成为研究重点，催生合成质量与隐私风险的联合度量标准。  

结论  
2022–2025 年间，表格学习领域正由“模型微调与架构优化”向“表格基础模型与表格—LLM 混合系统”过渡。合成先验预训练、参数高效集成、检索/程序化求解与结构感知图编码形成互补路径：前者提升小样本泛化与合成数据能力，后者在大表格与数值推理场景表现更为稳健。未来研究需要在可扩展性、数值可验证性与隐私合规性上做更多系统化工作，以推动表格基础模型从实验室走向生产环境。

参考文献（按文中出现顺序，链接文本使用检索结果来源域名以便溯源）
- TabPFN — A Transformer That Solves Small Tabular Classification Problems in a Second (arXiv 2022) — [arxiv.org](https://arxiv.org/abs/2207.01848)  
  解读 / 博文： [blog.csdn.net](https://blog.csdn.net/2501_91618231/article/details/147474963)

- TabDDPM — Modelling Tabular Data with Diffusion Models (arXiv 2022) — [arxiv.org](https://arxiv.org/abs/2209.15421)  
  概览/引用见综述： [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/48f6fae9-2762-46ed-8c49-ef0d36c0ef2f)

- TabM — Advancing Tabular Deep Learning with Parameter‑Efficient Ensembling (2024 summary) — [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/5dfb55c6-0530-48d1-aafd-93a314a8f811)

- TableRAG — Million‑Token Table Understanding with Language Models (arXiv 2024) — summary/blog: [blog.csdn.net](https://blog.csdn.net/weixin_44025655/article/details/145527034)

- HeGTa — Leveraging Heterogeneous Graph‑enhanced LLMs for Few‑shot Complex Table Understanding (AAAI2025 / arXiv preprint) — [zhuanzhi.ai](https://zhuanzhi.ai/paper/e4a856f209e289b75a2f0e01e2411219)  
  论文/预印本：arXiv id referenced in index (see link on zhuanzhi.ai)

- Turbo — Multimodal Tabular Reasoning with Privileged Structured Information (arXiv 2025) — [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/145926)

- Tabby — Tabular Data Synthesis with Language Models (2025 summary) — [blog.csdn.net](https://blog.csdn.net/weixin_40240616/article/details/146077383)

- Language Modeling on Tabular Data: A Survey (2024) — [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/48f6fae9-2762-46ed-8c49-ef0d36c0ef2f)

- TabSTAR — Tabular Foundation Model with Semantic Target‑Aware Representations (preprint summary 2025) — [hyper.ai](https://hyper.ai/cn/papers/2505.18125)

- 相关技术/背景（检索/程序辅助与混合范式参考） — Table‑to‑program / program‑aided QA literature summarized in TableRAG blog — [blog.csdn.net](https://blog.csdn.net/weixin_44025655/article/details/145527034)

- 综述与工具性讨论（表格数据语言建模演进） — [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/48f6fae9-2762-46ed-8c49-ef0d36c0ef2f)

- HeGTa 技术解读文章 — [blog.csdn.net](https://blog.csdn.net/h1453586413/article/details/145608216)

注：本文中对论文方法与结论的陈述基于论文/预印本与上列技术解读与综述资料的核查（所列域名为可追溯的原始解读或论文索引页），如需每篇论文的 PDF/原文链接可据 arXiv id 或会议收录页进一步检索。