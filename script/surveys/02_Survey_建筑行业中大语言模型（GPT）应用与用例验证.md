摘要
本文综述并评估 2022 年至 2025 年 11 月期间关于“大型语言模型（LLM / GPT 系列）在建筑/施工行业应用与用例验证”的学术与预印本工作。本文以明确的检索与筛选流程为基础，按应用主题（BIM/建模与设计交互、施工估算与图纸理解、施工安全与法规抽取、风险管理与决策支持、能耗/运行维护、知识图谱与信息检索、多代理/工具化系统与评测基准）逐一梳理重要论文，针对每篇关键工作给出尽可能完整的技术描述（问题、数据、所用模型、方法、实验与评价指标、结论与局限）并指出代码/数据公开情况、研究空白与未来方向。综述旨在为研究者与工程实践者提供一个可复用的参考框架和后续研究路线图。

关键词：大型语言模型、GPT、BIM、施工估算、施工安全、风险管理、多模态、基准数据集、综述

1. 范围与方法
- 时间范围：包含 2022 年（ChatGPT 发布／GPT 系列广泛被引用后）至 2025 年 11 月的论文与预印本（包括会议、期刊与 arXiv/预印本）。  
- 检索策略：在 arXiv、主要期刊（Buildings、Journal of Computing in Civil Engineering、ITcon、Engineering, Construction and Architectural Management 等）、会议与 GitHub 中检索关键词组合如 “large language model + construction/BIM/architecture/construction safety/estimation/energy/knowledge graph/text2bim” 等，优先列出高被引或技术贡献明确且公开代码/数据的工作。若文献存在多个版本（预印本→期刊），以最终公开版本或最新版 arXiv 作为引用对象。  
- 纳入准则：论文需明确使用或评估 LLM（例如 GPT 系列、LLaMA / Llama-family、Gemma、Claude、LLaVA 等）并针对建筑/施工问题给出实验或用例验证；也收录了以 LLM 为核心的多代理/工具化框架与专门基准/数据集（例如 CEQuest）。（检索结果与代表性条目见参考文献与注释。）

2. 主题分类与总体趋势（概述）
- 主题分布（近年主要方向）：  
  1) BIM 与自然语言到可编辑模型（Text→BIM / 建模交互）；  
  2) 图纸理解、工程量清单（quantity takeoff）与估算（estimation）；  
  3) 施工安全与法规/规范抽取、合规查询；  
  4) 风险识别/管理与项目决策支持；  
  5) 建筑能耗 / 运行维护（BEMS／BEM + LLM）；  
  6) 知识抽取 / 知识图谱（KG）服务于问答与检索；  
  7) LLM 多代理与工具化（自动调用 API、模型间协作）与专门基准。  
- 趋势要点：自 2023 年 ChatGPT 引爆后，建筑领域从探索性的应用示例（prompting 案例、工具原型）快速转向系统化方法（多代理框架、规则校验集成、专门基准数据集），并出现了专门的比较研究（对比 GPT-4、LLaMA 系列、LLaVA、多模态模型等）。然而，评测多集中在小规模用例与专家评分，系统性的公开大规模基准直到 2024–2025 才开始出现（例如 CEQuest）。这些结论可通过若干代表性综述/计量分析与领域论文得到支持。

3. 关键研究与详尽介绍（按应用主题）
下面对影响较大或代表性强的论文逐一详述（每项包括：引用、问题定义、方法/模型、数据/实现、评价、结论与局限、代码/数据可用性）。

3.1 BIM / 从文本到可编辑模型（Text→BIM）与设计交互
3.1.1 Text2BIM — Du et al., arXiv:2408.08054 (Journal of Computing in Civil Engineering 提交 / 版本迭代至 2025)
- 引用：Changyu Du, Sebastian Esser, Stavros Nousias, André Borrmann. Text2BIM: Generating Building Models Using a Large Language Model-based Multi-Agent Framework. arXiv:2408.08054 (v1 2024-08; v2 修订 2025-07). 
- 问题：将自然语言指令转换为可在 BIM authoring 软件中生成、可编辑且语义化的 3D BIM 模型（包含室内布局、外壳、构件语义）。  
- 方法/模型：提出一个基于 LLM 的多代理（multi-agent）框架——各代理协同：解析用户意图、生成可调用 BIM API 的“指令/代码”（imperative code）、并引入规则化模型检查器（rule-based model checker）把领域知识转入代理循环来修正与迭代输出。作者在代理内部试验了多种 LLM（论文中比较了三种不同 LLM 性能）。该方法以“文本→代码→BIM API 调用”路径为主，并在闭环中使用基于规则的校验以提升结构合理性。  
- 数据与实验：作者在若干设计示例上（包含布局与剖面要求）对比了不同 LLM 的能力，评估指标包含模型的结构合理性、与用户意图的一致性及在 BIM 软件（文中实现为 Vectorworks 的插件原型）中的可执行性。进行了交互原型演示与定性/定量对比。  
- 主要结论：多代理方案能将抽象的语言意图转为可执行 BIM 代码，规则检查显著减少结构性错误；但对于复杂结构与规范性细节仍需人工参与或更强的域知识注入。  
- 局限：对复杂工程图纸与结构完整性验证依赖外部工程求解器；对 LLM 的“数值精确计算/工程规范细节”表现不足；计算成本与对闭源 LLM (e.g., GPT-4/4o) 依赖是现实问题。  
- 开源：作者提供了实现仓库（GitHub）与 Vectorworks 插件原型说明（论文页与仓库中列出支持的 LLM 列表与使用说明）。

3.1.2 Interactive Design by Integrating a Large Pre-Trained Language Model and BIM — Jang & Lee, arXiv:2306.14165 (2023)
- 引用：Suhyung Jang, Ghang Lee. Interactive Design by Integrating a Large Pre-Trained Language Model and Building Information Modeling. arXiv:2306.14165 (2023). 
- 问题：探讨将 GPT 系列模型用作与 BIM（Revit）联动的交互式设计助理，降低设计师在 BIM authoring 中的指令负担。  
- 方法/实现：构建三模块管线 BIM2XML（将 BIM 转为 XML）、GAIA（使用预训练语言模型解析设计意图并在 XML 层面生成/改写设计语义）[LLM-empowered knowledge graph construction: A survey - arXiv.org](https://arxiv.org/pdf/2510.20345)、XML2BIM（把改写后的 XML 转回 BIM）。在案例研究中使用 GPT 系列模型与 Revit 对接。  
- 评价：通过设计细化案例展示了 LLM 在捕捉设计意图与自动化重复性编辑的优势，但也指出模型生成的 XML/语义仍需人工审校以保证工程可实施性。  
- 局限与启示：该工作是早期示范，说明将 LLM 嵌入 BIM 工作流的可行性；同时提出若要用于工程级输出，需与工程规则和校验器结合。

3.1.3 补充工作：建筑几何生成（Ercsey & Storcz, Architecture 2025）
- 该类研究评估 GPT-3.5/4 等在组合型建筑几何生成问题的表现，发现纯 LLM 在精确组合/完整解搜索时能力有限，但与专家知识（hybrid）结合可得到可用结果并显著提高交互效率。该类论文为 Text→几何/参数化设计提供现实评估。

3.2 施工估算（图纸理解、工程量清单、估算）与基准
3.2.1 CEQuest: Benchmarking Large Language Models for Construction Estimation — Wu et al., arXiv:2508.16081 (2025)
- 引用：Yanzhao Wu, Lufan Wang, Rui Liu. CEQuest: Benchmarking Large Language Models for Construction Estimation. arXiv:2508.16081 (2025). 
- 问题与动机：建筑行业中图纸解释与工程量估算高度依赖专业知识与跨模态信息（图形＋注释）。缺乏面向 LLM 的专门基准阻碍研究测评与系统比较。  
- 工作内容：提出 CEQuest 数据集（初版 164 道题，涵盖基础图纸识读到工程量与估算），对现有代表性 LLM（包含 Gemma 3、Phi4、LLaVA、Llama 3.3、GPT-4.1 等）进行了系统评测（准确率、执行时间、模型大小等指标），并开源数据与代码以促进后续研究。  
- 关键发现：通用 LLM 在此类专门化任务上仍有显著提升空间；多模态模型（如 LLaVA）与检索/工具增强策略对图纸相关问题较有帮助，但对精确工程量计算与跨图纸交叉引用等任务表现仍有限。  
- 贡献与局限：提供首批专门面向施工估算的 benchmark，有助于量化比较与推动数据驱动的领域模型；但样本规模仍偏小（论文中将 CEQuest 表示为 pilot），需要社区扩展与更多真实世界图纸样本。

3.3 施工安全与法规抽取（合规问答、法规检索）
3.3.1 Construction Safety Query Assistant (CSQA) / ITcon 特刊论文（Tran et al., 2024）
- 引用：Si Van-Tien Tran et al. Leveraging Large Language Models for Enhanced Construction Safety Regulation Extraction. ITcon (特刊) (submitted Apr 2024; published Dec 2024). 
- 问题：从大量安全法规文本、手册与契约文件中抽取结构化安全条件并以易懂形式交付给施工人员（提升理解与合规率）。  
- 方法：提出 CSQA 系统，由（1）文档采集与预处理模块（CSI）、（2）基于 LLM 的安全条件识别模块（SCI）、（3）信息呈现与反馈模块（SID）构成。SCI 使用 LLM 对文档进行语义解析与问答检索，SID 提供交互界面并包含用户反馈循环来改进准确性。  
- 实验与结论：在法规文本与若干用例上展示 LLM 在抽取与自然语言呈现方面的高效性；但同时讨论了模型“幻觉（hallucination）”与安全关键信息错误的风险，建议人类在环校验与溯源机制。

3.4 风险识别 / 项目风险管理（LLM 与专家对比研究）
3.4.1 Can ChatGPT exceed humans in construction project risk management? — Nyqvist et al., ECAM (2024)
- 引用：Roope Nyqvist, Antti Peltokorpi, Olli Seppänen. Can ChatGPT exceed humans in construction project risk management? Engineering, Construction and Architectural Management (ECAM), 2024. 
- 研究设计：盲测比较 GPT-4 与 16 位人类风险管理专家在风险识别、分析与控制提议上的表现；采用匿名同行评审评分体系量化比较。  
- 主要发现：在覆盖性（生成全面的风险目录）与文本化风险陈述方面 GPT-4 得分高于专家平均，但存在实践可执行性与情境化细节不足的短板。研究建议将 GPT-4 作为“增强型”工具，辅助（尤其是经验较少的）从业者扩大风险考虑范围，而把具体实践与细节交由专家完善。 [[2402.06196] Large Language Models: A Survey - arXiv.org](https://arxiv.org/abs/2402.06196)

3.4.2 Comparative study: LLMs for construction risk classification — Buildings (Erfani & Khanjar, 2025)
- 引用：Abdolmajid Erfani 和 Hussein Khanjar. Large Language Models for Construction Risk Classification: A Comparative Study. Buildings 2025. 
- 内容：将 LLM（包括 GPT-4）与传统 NLP+ML 管线（TF-IDF、Word2Vec + SVM、BERT+SVM）进行对比，检验在不需训练数据（zero-shot / few-shot prompting）条件下 LLM 的分类效果。结论显示：GPT-4（few-shot）能在无训练数据场景下达到接近传统最优模型的 F1 值（论文给出数值），并表现出对类不平衡问题的鲁棒性，但仍未彻底取代有标注监督模型在严格分类任务上的优势。

3.5 建筑能耗 / 运行维护（BEM+BEMS 与 LLM）
- 若干工作尝试把 LLM 用于建筑能耗建模、自动化 BEM 脚本生成与故障诊断（示例论文与案例研究指出 LLM 可用于脚本化仿真流程、表述建筑运行意图并生成参数化控制策略，但对数值精确性、时序控制与物理一致性要求高的任务仍需要结合物理仿真器／规则）。这些结论来自 2024–2025 年的案例型论文与综述。

3.6 知识图谱（KG）构建与信息抽取（LLM 驱动）
- 近年 NLP 社群出现大量使用 LLM 进行知识抽取与 KG 构建的通用方法（例如 EDC、iText2KG 等通用框架），这些方法在建筑文本（规范、报告、维修记录）中被用来自动抽取实体/关系以支持问答与检索。代表性方法强调三段式：抽取（Extract）、定义/构造 Schema（Define）、规范化/融合（Canonicalize）。对建筑领域而言，KG 有助于把异构文档与 BIM 属性连接起来以支持检索与可追溯问答。

3.7 多代理 / LLM Agent、工具化与评估基准
- 趋势：越来越多工作将 LLM 包裹成“代理（agent）”来调用外部工具（检索、API、仿真器、BIM 软件接口），并通过多代理协作完成复杂任务（Text2BIM 就是例子之一）。同时，社区开始关注 LLM agent 的评估方法学（agent 性能、协作失败模式、成本-安全权衡等）。最近的综述与基准工作对 agent 的评测方法提出系统化框架，值得在建筑应用中借鉴。

4. 评估方法与基准数据集（汇总）
- 现有专门基准：CEQuest（施工估算/图纸理解，2025，开源 pilot 数据集）。  
- 通用/可借鉴数据集与工具：FloorPlanCAD 等建筑平面/图纸数据集（历史上对图纸理解很有价值，CEQuest 中有进一步引用），以及面向 KG /抽取任务的标准 benchmark（可迁移方法学）。  
- 评价实践：当前论文常用的评价包括（1）准确率 / F1（分类任务）、（2）专家盲评（风险管理、设计建议等主观任务）、（3）任务完成率（agent 执行 API 并成功在 BIM 中生成目标）、（4）结构/物理合理性检查（rule-based 或仿真器校验）、（5）计算成本 / 延迟 / 可部署性度量。值得注意的是：多数现有评测对“事实性（factuality）”与“可追溯性（source attribution）”考量不足，而这些在工程/安全相关应用中至关重要。

5. 常见方法学与工程实践要点
- 多模态融合：将文本、图像（图纸/平面图/剖面）、BIM 元数据结合，通常需要把图像/图纸先做视觉理解（OCR、图形解析、FloorPlan parser），再通过 RAG（retrieval-augmented generation）或多模态 LLM（如 LLaVA 等）联合推理。Text2BIM 与 CEQuest 的工作均显示多模态策略优于纯文本提示。  
- 多代理 + 规则校验：将 LLM 的生成能力与规则化的工程校验器结合可显著减少危及安全或造成不合规设计的输出（Text2BIM 引入 rule-based model checker 为代表实践）。  
- 少样本 / 零样本提示策略：在标注数据稀缺场景（风险分类、法规抽取）中，few-shot / zero-shot prompting 对 LLM 的即插即用性有价值，但其稳定性依赖 prompt 设计与后处理（分类阈值、人工审查）。相关研究表明 GPT-4 在 few-shot 下可以接近传统监督学习模型性能。  
- 可解释性与可追溯性：在施工安全、合规与决策支撑类应用中，单纯文本生成不足以支撑工程责任与审计，系统需输出证据链（法规出处、图纸片段、模型调用日志）并提供人工复核路径（论文多次强调）。

6. 主要挑战与风险
- 幻觉（hallucination）与事实不一致：LLM 在生成合规建议或工程细节时可能“自信但错误”，这在安全/法规/结构设计领域风险极高，必须用检索与证据校验、规则/仿真器作为二层保障。  
- 数据隐私与合规（企业图纸 / 合同属于敏感资产）：将闭源 LLM（在线 API）直接用于敏感项目数据会带来数据泄露与合规风险（已有论文以 ChatGPT 在项目场景的安全性问题为研究主题）。部署时需考虑本地化模型、差分隐私或企业私有检索 + 链路隔离。  
- 领域知识偏差与训练集不足：通用 LLM 对细粒度工程规范、地区性法规、材料系数等细节易欠缺；需要领域微调或构建领域知识库/检索器以补足。CEQuest 等基准指出在施工估算类任务上通用模型仍有提升空间。  
- 评估缺失：缺少统一的、可扩展的、工程验证级别的 benchmark（多数现有数据集样本量小或偏示例性），尤其是跨模态图纸→估算的端到端量化评估稀缺。  
- 多代理系统可靠性与故障模式：代理间通信、分工与纠错机制如果设计不当，会出现任务执行失败或循环错误，需要系统化的 agent 评估框架（已有一般性 agent 评估综述可借鉴）。

7. 推荐的研究与工程实践路线（对研究人员与工程化团队的具体建议）
-[Improving Factuality in LLMs via Inference-Time Knowledge Graph ...](https://arxiv.org/pdf/2509.03540) 对研究者：  
  1) 构建并开源更大规模、多样化且带 ground-truth 的图纸-估算对（e.g., 扩展 CEQuest）；鼓励真实项目数据（脱敏）参与；  
  2) 开发带证据引用和事实校验的 RAG + KG 混合框架（把法规、标准、BIM 元数据做为检索库）；引用 EDC / iText2KG 等通用 KG 构建方法论以提高可追溯性；  
  3) 研究多模态端到端度量：提出任务级别（设计可执行性、结构合理性、估算误差界限、合规性判别）的客观指标与自动校验器；  
  4) 探究高可靠性的 agent 协作协议与纠错机制，并发表细粒度失败案例数据集以促进方法改进（引用 agent 评估综述）。  
- 对工程团队 / 实践者：  
  1) 将 LLM 用作“增强型助理”而非自动化替代：在早期设计、风险梳理、合规提取阶段可高速扩展覆盖面，但落地输出须人类工程师复核；  
  2) 采用检索增强与证据链接：所有合规/安全建议应返回法规原文段落或图纸片段并记录模型版本与 prompt 日志；  
  3) 控制敏感数据流：对涉及合同/未公开图纸的任务，优先考虑内部部署的领域模型或私有检索 + 本地 LLM（或使用隐私合规的 API 协议）；  
  4) 引入规则校验与仿真器闭环检查：对于结构/安全/能耗输出，使用专门的物理/工程校验器做后验验证（Text2BIM 的 rule-based checker 为示例）。

8. 未来研究方向（可衡量的短期 / 中期研究议程）
- 构建大规模、多模态（文本+图纸+BIM）公开 benchmark（扩展 CEQuest，加入真实工程量 takeoff 与成本标签）；  
- 研究“事实性保证”机制：结合推理级知识图谱、检索证据与推理可解释性，让 LLM 输出带“可审计”的证据链（KG + RAG + LLM 三角结构）；  
- 多代理系统的安全可靠性工程（协议、超时/回滚、仲裁者/检查器的设计），并构建行业化 agent 评测套件；  
- 面向行业的微调/增量学习流水线：如何在不泄露敏感数据前提下用少量项目数据微调 LLM，使其在估算/规范上有稳定改进（探索参数高效微调、LoRA、RAG 与检索缓存结合的方案）。  
- 跨学科伦理/法律研究：责任归属、合规审计流程、合同条款中的 AI 使用声明，为工程实践提供法律-技术双重保障。

9. 结论
从 2022 年至 2025 年，LLM 在建筑/施工领域从“概念验证与用户交互示范”迅速走向“系统化应用与专门基准”的阶段。代表性进步包括：Text2BIM 类多代理将自然语言直连 BIM API 的可执行路径、CEQuest 之类面向估算的基准开始出现、以及多个关于安全与风险管理的对比研究表明 LLM 能显著提高覆盖面与效率但仍需结合人类工程师与规则/仿真器来保证工程可实施性与安全性。总体来看，领域正从“能做什么”的问题（LLM 能否生成）转向“如何可靠地做”的工程问题（如何保证事实性、如何评估、如何部署）。本文列出的论文与方法为未来研究与产业化落地提供了明确方向与基线。

参考文献（代表性、按文中引用顺序列出；若需完整 BibTeX / DOI 列表我可导出）
- Du, C., Esser, S., Nousias, S., & Borrmann, A. Text2BIM: Generating Building Models Using a Large Language Model-based Multi-Agent Framework. arXiv:2408.08054 (v2 2025).   
- Jang, S., & Lee, G. Interactive Design by Integrating a Large Pre-Trained Language Model and Building Information Modeling. arXiv:2306.14165 (2023).   
- Tran, S. V.-T., Yang, J., Hussain, R., et al. Leveraging Large Language Models for Enhanced Construction Safety Regulation Extraction. ITcon (Special Issue), submitted Apr 2024, published Dec 2024.   
- Nyqvist, R., Peltokorpi, A., & Seppänen, O. Can ChatGPT exceed humans in construction project risk management? Engineering, Construction and Architectural Management (ECAM), 2024.   
- Wu, Y., Wang, L., & Liu, R. CEQuest: Benchmarking Large Language Models for Construction Estimation. arXiv:2508.16081 (2025).   
- Erfani, A., & Khanjar, H. Large Language Models for Construction Risk Classification: A Comparative Study. Buildings, 2025.   
- Ercsey, Z., & Storcz, T. Building Geometry Generation Example Applying GPT Models. Architecture, 2025.   
- Movva, R., Balachandar, S., Peng, K., et al. Topics, Authors, and Institutions in Large Language Model Research: Trends from 17K arXiv Papers. NAACL 2024. （用于说明 LLM 研究趋势）cite[Comprehensive LLM Agent Research Collection - GitHub](https://github.com/luo-junyu/Awesome-Agent-Papers)  
- 综述 / 方法学与工具相关：多个关于 LLM-KG 构建、agent 评估与 LLM 总览的综述与论文（例如 EDC / iText2KG / LLM agent surveys / LLM: A Survey 等），在正文相应段落中引用。

附：如果您希望下一步更快推进研究或工程化工作，我可以（请选择其中任一项或多项）：
- A. 提供一页（1–2 页）可直接发给基金/项目经理的“研究计划”，包括数据收集/脱敏方案、评价基准和里程碑；  
- B. 帮您把本文列出的关键论文做成可排序/可导出的 BibTeX + PDF 列表（并附可用的 GitHub / 数据集链接）；  
- C. 基于贵团队的具体需求（例如“Text→BIM 原型”或“估算自动化初步试验”）设计实验方案与 baseline（包括 prompt 模板、评估指标、所需样本）。  

请告诉我您下一步的优先任务（A/B/C 或指定文献深挖哪一类），我会基于您选项给出更具体的计划与可执行清单。[[2503.16416] Survey on Evaluation of LLM-based Agents - arXiv.org](https://arxiv.org/abs/2503.16416)