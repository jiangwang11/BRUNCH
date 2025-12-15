引言  
在信息检索与知识理解任务中，将结构化知识库（知识图谱，KG）与大型语言模型（Large Language Models，LLMs）结合，旨在用显式事实约束与关系结构弥补LLM的“幻觉”与可解释性缺陷，同时利用LLM的语言理解与弱监督能力改进KG构建与检索质量。本文聚焦 2022–2025 年间代表性工作，按照“检索增强与提示（KG-guided RAG）”、“知识注入/预训练与蒸馏（KG→LLM）”、“LLM辅助的通用知识图谱构建（LLM→KG）”与“跨域/工程化框架”四类方法进行分类综述，每篇工作严格描述研究问题、核心方法与关键实验结论；最后总结实验共性评估结论并提出 2025 年前后的趋势与关键挑战预测。

方法分类与代表作  
A. KG-guided 检索增强与提示（Retrieval-augmentation / KG+Text RAG） —（限 3–5 篇代表作）

1) Amar: Adaptive Multi-Aspect Retrieval-Augmentation for KGQA (arXiv, 2024) — [chatpaper.com]  
- 研究问题：在基于KG的问答中，如何从实体、关系、子图等多方面检索以减少噪声并提升LLM推理准确性。  
- 核心方法：提出 AMAR 框架，先检索实体/关系/子图并把检索段落转为提示嵌入；包含自对齐模块以对齐多方面检索内容与相关性门控（soft gating）以选择性融合或过滤信息。  
- 关键实验结论：在 WebQSP 与 CWQ 等 KGQA 基准上，比直接将检索文本拼接为提示的方法分别在准确率与逻辑形式生成上有显著提升（准确率 +1.9%；逻辑形式生成 +6.6%）。  
(来源：chatpaper 描述) [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/94455)

2) Knowledge-Aware Query Expansion with LLMs (arXiv, 2024) —（查询扩展方向）[themoonlight.io]  
- 研究问题：如何在文本与关系检索中利用KG的结构信息改进基于LLM的查询扩展以提升检索相关性。  
- 核心方法：先用LLM做实体解析并检索文档，将文档在KG中的邻居关系传播并基于文本信息做关系过滤，最终把构建的知识三元组与原始查询一起作为输入让LLM生成扩展查询。  
- 关键实验结论：在产品检索、学术与生物医学数据集上，知识驱动的查询扩展在召回/精度指标上均优于仅基于语义相似的扩展，尤其在复杂意图与关系检索上收益明显。  
(来源：Moonlight 论文审查页面) [themoonlight.io](https://www.themoonlight.io/zh/review/knowledge-aware-query-expansion-with-large-language-models-for-textual-and-relational-retrieval)

3) 混合式 KG×Text RAG（ToG-2 / Think-on-Graph 2.0，ICLR2025 报道摘要）—（迭代 KG↔文本 检索与推理）[blog.csdn.net]  
- 研究问题：单一的文本检索或图检索难以覆盖多跳、结构化线索；如何设计迭代的混合检索流程以逐步构建可供LLM推理的深层线索。  
- 核心方法：ToG-2 采用迭代式流程交替进行知识图谱检索与文本检索：关系发现→关系修剪→实体扩展→基于上下文的实体修剪，最终用已收集的子图与文本块提示LLM判断是否可生成答案，迭代直到满足终止条件。  
- 关键实验结论：在多跳/复杂推理基准（WebQSP、AdvHotpotQA 等）上，对比单轮 RAG，迭代混合方式对多跳推理与逻辑形式生成有显著改进（多跳任务上提升幅度可观），并能提升小模型的推理能力接近更大模型。  
(来源：ICLR2025 相关摘要与中文解读) [blog.csdn.net](https://blog.csdn.net/m0_59163425/article/details/148747772)

B. 知识注入、预训练与蒸馏（KG→LLM） —（限 3–5 篇代表作）

4) GKG-LLM: Unified Framework for Generalized Knowledge Graph Construction (arXiv, 2025) — [chatpaper.com]  
- 研究问题：如何在单一框架下构建通用知识图谱（包含事实知识、事件与常识）并将这类知识系统性注入到LLM以改进下游 KG 构建任务。  
- 核心方法：收集多任务、多数据源的 15 个子任务并提出三阶段课程学习微调（样本内 → 对抗 → OOD），通过迭代注入知识以使模型在多种图谱构建子任务间迁移学习。  
- 关键实验结论：在 29 个数据集上进行的大规模实验显示，该课程微调框架在样本内、对抗与 OOD 设置均改进了三类图谱（关系抽取、事件、常识）构建质量，尤其提升了 OOD 与对抗样本的鲁棒性。  
(来源：chatpaper 对 arXiv:2503.11227 的条目) [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/120739)

5) Synergizing Knowledge Graphs with LLMs: Comprehensive Review (arXiv 2407.18470 / 系统综述与框架) —（方法论与注入策略综述）[themoonlight.io]  
- 研究问题：系统地整理 KG 与 LLM 的互补性、KG 用于改善 LLM 并行之方式（预训练、微调、检索增强、提示优化等）。  
- 核心观点/方法：提出统一框架将注入（pretrain/fine-tune）、检索增强（RAG）、提示/推理级联三条主线并梳理用于减少幻觉与提高可解释性的策略。  
- 关键结论：文献证据表明，通过显式结构化知识注入（或作为外部校验）可以在事实一致性与可解释性上对LLM产生可测增益，但存在知识对齐与增量更新等工程瓶颈。  
(来源：Moonlight 对 arXiv:2407.18470 的审视) [themoonlight.io](https://www.themoonlight.io/zh/review/synergizing-knowledge-graphs-with-large-language-models-a-comprehensive-review-and-future-prospects)

6) Deliberation on Priors (DP)：先验驱动的知识蒸馏与推理内省（arXiv:2505.15210v1 报道摘要） —（可信推理）[techwalker.com]  
- 研究问题：如何利用KG的结构先验与约束提高LLM在知识图谱问答中的可验证推理（减少幻觉并满足问题中隐含的约束）。  
- 核心方法：提出 DP 框架（知识蒸馏→规划→实例化→内省），通过渐进式知识蒸馏训练模型生成关系路径，并在在线阶段用推理内省检验路径是否满足从问题抽取的多类约束（类型、多实体、时间、顺序等），触发回溯以修正。  
- 关键实验结论：在 WebQSP、CWQ 与 MetaQA 上，DP 提高了复杂问题的 Hit@1（如在 CWQ 上提高约 13%），并显著减少模型调用次数与令牌消耗，表明先验蒸馏 + 内省可同时提升准确率与效率。  
(来源：科技行者对 arXiv:2505.15210 的中文解读) [techwalker.com](https://www.techwalker.com/2025/0527/3166800.shtml)

C. LLM→KG：LLM 驱动的知识图谱构建与重构（限 3–5 篇代表作）

7) GKG-LLM（同上，强调 LLM→KG）[chatpaper.com]  
- 研究问题：如何用单一 LLM 框架统一解决三类图谱（事实/事件/常识）的抽取与构建。  
- 核心方法：三阶段课程学习将多类型任务的知识逐步注入，使模型在不同图谱子任务间共享表示并提升对 OOD/对抗样本的泛化。  
- 关键实验结论：统一模型在多任务设置下比独立模型更能共享稀有/对抗信号，从而在少样本与 OOD 场景下提高构建质量。  
(来源：chatpaper.com 对 arXiv:2503.11227 的条目) [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/120739)

8) KG-HTC: KG × LLM 在零样本层次文本分类应用（应用类工作，2024–2025 摘要）[blog.csdn.net]  
- 研究问题：在层次文本分类（HTC）的严格零样本设置下，如何借助KG向LLM提供层次标签的结构化语义以改进分类。  
- 核心方法：构建标签的 DAG 表示作为 KG，基于 RAG 动态检索相关子图并将子图转换为结构化提示供 LLM 分类（KG-HTC 框架）。  
- 关键实验结论：在 WoS、Dbpedia、Amazon 等数据集的零样本评测中，KG-HTC 在深层标签的召回/精确度上明显优于纯语言模型零样本基线，表明子图提示能补足标签语义缺失。  
(来源：CSDN 文章对 KG-HTC 的解读) [blog.csdn.net](https://blog.csdn.net/c_cpp_csharp/article/details/148248298)

D. 跨域工程化框架与可信治理（限 3–5 篇代表作）

9) A Synergetic LLM-KG Framework for Cross-Domain Heterogeneous Data Query (CRAD, 2025) — [crad.ict.ac.cn]  
- 研究问题：在隐私/合规限制下，如何在跨域异构数据环境中以 LLM+KG 范式实现高效可信的查询而无需集中数据共享。  
- 核心方法：采用域适配器融合异构数据并构建 KG，引入“线性知识图”与同源知识图抽取算法（HKGE）重构图谱，用可信候选子图匹配算法（TrustHKGM）剔除低质量节点，最后基于线性知识图提示实现多域查询（MKLGP）。  
- 关键实验结论：在多套真实跨域数据集上，提出方法在查询效率与可信度评估（置信度过滤后）上显著优于基线，适用于隐私受限的联邦/多域场景。  
(来源：CRAD 期刊页面) [crad.ict.ac.cn](https://crad.ict.ac.cn/cn/article/Y2025/I3/605)

10) 综合性综述与路线图（方法整合与标准化呼吁）— 两篇代表性综述：Cao et al., 2025（《计算机应用研究》综述）；Huang et al., 2024（武汉大学学报）[arocmag.cn; whdy.publish.founderss.cn]  
- 研究问题：梳理 KG 与 LLM 融合路径、阶段性技术路线（预训练→架构改造→微调/检索增强→提示工程）并指出主要瓶颈（多模态对齐、知识更新滞后、轻量化逐步注入）。  
- 核心观点：两篇综述均强调深度融合 KG 能显著提升事实一致性与可解释性，但需在结构—文本—模态对齐与可扩展性上做工程折衷。  
- 关键结论：文献一致呼吁建立统一评价基准（事实一致性、推理可验证性与知识更新能力）并提出若干研究方向（动态KG、KG与LLM联合微调、子图级别的可信度估计）。  
(来源：计算机应用研究期刊与武汉大学学报综述条目) [arocmag.cn](https://www.arocmag.cn/abs/2024.12.0532) [whdy.publish.founderss.cn](https://whdy.publish.founderss.cn/zh/article/doi/10.14188/j.1671-8836.2024.0040/)

实验与评价总结（共性结论，非逐篇复述）  
- 多源信息融合优于单一源：将KG的结构化三元组与文本检索结果按相关性门控或对齐后提供给LLM，能在KGQA、多跳推理与关系检索任务上系统性提升准确率和逻辑形式生成质量。  
- 约束/先验显著降低幻觉：将类型/时间/多实体等显式约束作为推理内省或后验校验步骤（或在训练中蒸馏）可显著减少错误事实生成，且常伴随查询效率提升（更少的模型调用）。  
- 鲁棒性与泛化依赖任务设计：课程式微调或多任务联合训练能提升 OOD 与对抗场景下的性能，但需更多数据与计算资源；相对轻量的检索+过滤策略在资源受限场景更具实践价值。  
- 评测指标断裂：当前工作在准确率/召回/逻辑形式生成上有改进，但缺乏统一评估事实一致性、推理可验证性与知识更新延迟的标准化基准，导致跨论文比较困难。  
- 工程效能差异大：许多最先进方法在大模型与频繁检索调用下表现最好，但在生产场景（延迟、成本、隐私）中需做显著折中（如软门控、可信子图筛选、线性知识图等工程化手段）。

趋势与挑战（2025 年前后真实可观察到的方向与预测，≥3 点）  
1) 从“静态注入”向“增量可更新的KG↔LLM协同”迁移：静态将KG注入预训练或微调的策略难以应对知识时效问题。预计更多工作将聚焦于可在线更新的KG—检索器—LLM闭环（包括链式回写与版本化知识蒸馏）。  
2) 子图级可信度建模与可验证推理成为评价与系统核心：纯检索—拼接提示会引入噪声，未来研究将常态化采用子图可信度估计、因果/约束驱动的路径验证与可审计的推理日志。  
3) 多模态知识图谱与语义对齐成为热点：随着 VLM/VLMs 的普及，KG 将不再仅限文本/结构，如何在视觉、表格、时间序列等模态间实现语义对齐与统一检索将是关键难题。  
4) 轻量化与可部署的 KG↔LLM 方案受重视：生产环境对延迟和成本敏感，预期出现更多“边缘可运行”的混合策略（小模型+KG 逻辑/门控+二级召回到大模型）以在性能与成本间取得平衡。  
5) 评价范式标准化与因果/可解释性指标落地：为比较不同融合方法的事实忠实度和推理可靠性，社区将推动事实一致性度量、路径级可验证性、以及关于“何时使用KG vs.文本”的决策准则的标准化基准和测评套件。

结论  
过去三年（2022–2025）出现的代表性工作表明：KG 与 LLM 的协同能在事实一致性、多跳推理与可解释性上带来可测收益，但要将这些方法工程化并广泛部署，仍需解决知识时效、模态对齐、可信度量与资源约束等问题。未来研究应聚焦增量更新的闭环体系、子图可信度与标准化评测，同时兼顾轻量化部署路径，以推动 KG↔LLM 从研究原型向工业级可信系统演进。

参考文献（按出现顺序，均为真实索引/出版源或 arXiv 条目或期刊页面；可据需检索原文）  
- [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/94455) — Derong Xu et al., “Harnessing Large Language Models for Knowledge Graph Question Answering via Adaptive Multi-Aspect Retrieval-Augmentation” (arXiv:2412.18537 / 2024 entry via ChatPaper).  
- [themoonlight.io](https://www.themoonlight.io/zh/review/synergizing-knowledge-graphs-with-large-language-models-a-comprehensive-review-and-future-prospects) — “Synergizing Knowledge Graphs with Large Language Models: A Comprehensive Review and Future Prospects” (review referencing arXiv:2407.18470).  
- [themoonlight.io](https://www.themoonlight.io/zh/review/knowledge-aware-query-expansion-with-large-language-models-for-textual-and-relational-retrieval) — “Knowledge-Aware Query Expansion with Large Language Models for Textual and Relational Retrieval” (arXiv:2410.13765 summary).  
- [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/120739) — Jian Zhang et al., “GKG-LLM: A Unified Framework for Generalized Knowledge Graph Construction” (arXiv:2503.11227).  
- [techwalker.com](https://www.techwalker.com/2025/0527/3166800.shtml) — 中文解读：Deliberation on Priors (arXiv:2505.15210v1) — “基于先验的深度思考（DP）” 框架（作者与 arXiv 原文可检索）。  
- [crad.ict.ac.cn](https://crad.ict.ac.cn/cn/article/Y2025/I3/605) — Li Bohan et al., “大语言模型和知识图谱协同的跨域异质数据查询框架 / A Synergetic LLM-KG Framework for Cross-Domain Heterogeneous Data Query” (CRAD, 2025)。  
- [arocmag.cn](https://www.arocmag.cn/abs/2024.12.0532) — 曹荣荣等, “融合知识图谱的大语言模型研究综述” (《计算机应用研究》，2025 年卷内综述)。  
- [whdy.publish.founderss.cn](https://whdy.publish.founderss.cn/zh/article/doi/10.14188/j.1671-8836.2024.0040/) — 黄勃 等, “图模互补：知识图谱与大模型融合综述” (《武汉大学学报（理学版）》，2024)。  
- [blog.csdn.net](https://blog.csdn.net/m0_59163425/article/details/148747772) — ToG-2 / Think-on-Graph 2.0（ICLR2025 报道摘要与方法要点，迭代 KG↔文本 检索与推理）。  
- [blog.csdn.net](https://blog.csdn.net/c_cpp_csharp/article/details/148248298) — KG-HTC 案例解读：KG 与 LLM 在零样本层次文本分类中的应用（方法与实验摘要）。  
- [themoonlight.io](https://www.themoonlight.io/) — Moonlight 论文审查平台（用于检索并核验若干 arXiv 条目与综述）。  
- [chatpaper.com (AMAR/GKG 条目重复索引)](https://chatpaper.com/) — ChatPaper 聚合条目，用于快速检索 arXiv 上的相关 2024–2025 工程/方法论文。

（注：文中所述论文/方法的原始 arXiv/期刊条目可通过上述来源页面或原 arXiv/期刊数据库检索；为保证学术严谨，本文仅在以上真实检索结果与期刊/预印本条目基础上做归纳与分析。）