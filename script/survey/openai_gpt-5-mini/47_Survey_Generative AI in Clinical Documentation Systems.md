引言  
随着大型生成式模型（Generative AI/LLM）进入医疗场景，临床文档系统（clinical documentation systems，CDS）的自动化写作、摘要与结构化成为研究热点。关键问题集中在：如何在保证事实性与可溯源性的前提下高质量生成病程记录、门诊/住院病历与影像报告；如何将模型输出与电子病历（EHR）结构数据及隐私/合规要求耦合；以及如何在真实临床流程中评价安全性与临床价值。下文基于 2022–2025 年的代表性工作，将方法划分为四类（检索增强生成、工具/API 调用与外部接口、面向影像/多模态的文档生成、行业垂直语料与模型构建），每类选取 3–5 篇最具代表性的论文并简要点评，随后总结跨文献的实验结论与评价共性，最后给出面向 2025 年前后的研究趋势与挑战预测。

方法分类与代表作  
一、检索增强生成（Retrieval-Augmented Generation, RAG）——引入外部证据以降低“幻觉”并提供可溯源性  
- Lewis et al., RAG (arXiv 2020). 该工作提出把检索模块与生成模块耦合：查询先检索相关文档（向量检索），再将片段送入生成模型以辅助回答。核心方法为检索—拼接—生成的流水线，并讨论了端到端训练与检索缓存策略。对知识密集型问答展示了显著提高事实性与覆盖新知识的能力，成为后续医学 RAG 应用的基石。[arxiv.org](https://arxiv.org/abs/2005.11401)  
- Gao et al., "Retrieval-augmented generation for LLMs: a survey" (arXiv 2024). 系统综述了 RAG 的组件（向量检索、重排序、片段融合）以及常见失效模式（检索噪声导致的“带证幻觉”）。文中归纳出面向医学的若干工程指南（如领域编码器、证据溯源格式与二次事实校验链）。该综述为医疗级 RAG 系统设计提供方法论参考。[arxiv.org](https://arxiv.org/abs/2312.10997)  
- MedRAG / 医学定制 RAG（相关工作，arXiv 2025）。若干近期工作将知识图谱/医学指南与 RAG 集成（例如 MedRAG），方法上强调：①域化检索编码器（医学术语、缩写处理）；②多段证据重排序与跨文档一致性约束；③输出中嵌入文献引用与时间戳以满足临床可审计性。实验表明在医学问答与临床决策支持任务中，RAG明显降低了可证伪错误率并提高可追溯性（详见原文）。[arxiv.org](https://arxiv.org/abs/2502.04413)；中文综述见对医学 RAG 的系统梳理与临床应用案例分析。[ywlxbx.whuznhmedj.com](https://ywlxbx.whuznhmedj.com/journal/481.html)

二、工具/API 调用与外部接口增强（Tool-calling / Tool-augmented LLMs）——把精确计算与结构化数据交给外部工具  
- Schick et al., Toolformer (arXiv 2023). 提出自监督方法让 LLM 学会何时调用工具（搜索、计算器、API）并在微调时内置调用占位符。对于临床文档，Toolformer 思路可用于调用院内检索、计量与代码化接口以保证医学计算与规范化字段的精确性。实验显示在需要精确计算或外部数据库查询的任务上，工具调用显著减少模型错误。 [arxiv.org](https://arxiv.org/abs/2302.04761)  
- Patil et al., Gorilla (arXiv 2023). 构建大规模 API 调用数据集并训练 LLM 以熟练生成 API 请求与解析响应。对临床场景的借鉴是：将 EHR 的结构化操作、影像检索或药典查询封装为 API，由模型负责编排而非直接“凭记忆”生成结果，从而避免数值/事实错误。[arxiv.org](https://arxiv.org/abs/2305.15334)  
- Qin et al., ToolLLM (arXiv 2023). 提出大规模 RESTful-API 指令微调以提高模型在工具使用上的泛化性。对于临床文档系统，该路线能把“标准化字段填充”“用药剂量计算”“时间线重建”等任务交由专门工具，模型只负责自然语言组织与多源调用协调。[arxiv.org](https://arxiv.org/abs/2307.16789)

三、面向影像/多模态的文档生成（医学影像 → 报告 / multimodal LLM）  
- Qian et al., MedVLM (计算机应用研究, 2025). 在多模态基础模型上提出判别增强的微调方案（低秩适配、提示微调、冻结微调等），将影像诊断作为判别目标联合训练以提升报告准确性。实证：在肺部 CT 报告生成任务上 BLEU@4≈40.85%、METEOR≈70.56%，生成报告的肺炎诊断准确率约 87.7%，明显优于传统图像描述方法，说明判别增强微调能提升诊断相关的事实性和诊断一致性。[arocmag.cn](https://www.arocmag.cn/abs/2024.08.0303)  
- 多模态通用与解释性工作（代表性开源与工业模型）。近年多模态 LLM（结合视觉编码器与文本解码器）的研究显示：①直接将影像特征拼接入上下文可生成可用草稿报告；②结合检索/知识图谱与结构化检查结果的混合策略能显著降低影像报告中的实质性矛盾（即“带证幻觉”）。相关系统在放射学信息提取与报告标准化任务上达到可临床引用的文本质量（见下文综述与评价）。（综述与行业实践见 Xiao 等及领域综述）[slyyx.whuznhmedj.com](https://slyyx.whuznhmedj.com/journal/254.html)

四、行业垂直语料与垂直大模型构建（语料库、标注规范与模型适配）  
- Shen et al., “卫生健康行业多模态语料库构建” (Science Bulletin / 科学通报, 2025). 系统性提出“疾病—场景关联矩阵”与多层次语料标准（采集、标注、质量评估、隐私保护），强调面向临床文档的语料必须包含结构化 EHR 字段、临床笔记、影像与组学等多模态数据以支撑可审计的垂直大模型。论文分析表明，行业语料短缺与质量/隐私约束是制约临床 LLM 商业化部署的核心瓶颈。[sciengine.com](https://www.sciengine.com/doi/pdf/74BC9028A25F462FB32CBA8EBB02732D)  
- 王昊奋等，构建慢病健康管理信息系统（国家/院校案例，2024–2025）。通过领域语料注入与工具增强（数值处理、规则校验）提升慢病对话与计划生成的准确性，展示了“本地化语料+工具链”在临床路径文档化中的可行性。[crad.ict.ac.cn](https://crad.ict.ac.cn/article/doi/10.7544/issn1000-1239.202440570?viewType=HTML)  
- 行业综述与规范性讨论（医院期刊/综述）。多篇医院与学术期刊工作强调：为满足临床可审计与合规性，语料库建设必须结合 HL7/FHIR、ICD 等标准并保留可追溯的证据引用链。[xuebao.301hospital.com.cn](https://xuebao.301hospital.com.cn/article/doi/10.12435/j.issn.2095-5227.24070201)

实验与评价总结（跨文献共性结论，非逐篇复述）  
1) 事实性/幻觉：引入检索或外部工具（RAG、Toolformer/ToolLLM）是降低生成“无据编造”的最有效工程方法之一；检索结果的质量/相关性成为瓶颈——若检索片段本身不可靠，RAG 仍会产出“带证幻觉”。（RAG 与 tool-calling 文献一致指出检索质量与重排序策略关键）[arxiv.org](https://arxiv.org/abs/2005.11401)[arxiv.org](https://arxiv.org/abs/2312.10997)  
2) 可溯源性：在输出中附带出处（片段引用、时间戳、证据置信度）可显著提高临床用户的信任度；但仅“有出处”并不足以保证语义一致性，需要二次验证模块（fact-checker / provenance verifier）。多篇工作实现了“生成后核查”以过滤高风险回答。[ywlxbx.whuznhmedj.com](https://ywlxbx.whuznhmedj.com/journal/481.html)  
3) 多模态融合：对含影像的文档生成，判别增强/对齐微调（将诊断标签作为判别目标）能提升生成报告中与影像一致的诊断准确率；然而跨模态时间轴对齐（例如将实时监测信号和笔记对齐）仍具挑战性并影响模型稳定性。[arocmag.cn](https://www.arocmag.cn/abs/2024.08.0303)[sciengine.com](https://www.sciengine.com/doi/pdf/74BC9028A25F462FB32CBA8EBB02732D)  
4) 评价基准的匮乏：当前多数评测以自动指标（BLEU/METEOR/ROUGE）或专家打分为主，缺乏统一的“临床安全性”量表（覆盖错诊风险、漏诊风险、潜在法律/合规后果），导致不同工作结果不可直接比较。  
5) 隐私与合规：联邦学习、去标识化与合成数据虽被广泛探索，但存在“效用—隐私”权衡；实际部署更倾向混合方案（本地敏感数据留存 + 模型端调用受控 API）。[sciengine.com](https://www.sciengine.com/doi/pdf/74BC9028A25F462FB32CBA8EBB02732D)

趋势与挑战（2025 年前后真实研究趋势预测，≥3 点）  
1) 从“生成草稿”到“可审计的临床最终文本”加速分化。未来两年内研究与工程将把重点从单纯文本质量转向“生成过程可解释与可追溯化”（证据链、置信区间、二次核查模块），并逐步形成医院级合规输出规范（类似审计日志与证据打包）。相关工作已在 RAG 与报告生成中体现并将走向标准化。[arxiv.org](https://arxiv.org/abs/2312.10997)[arxiv.org](https://arxiv.org/abs/2005.11401)  
2) 工具化（Tool-calling）成为临床文档系统的工程常态。由于许多临床任务需要精确数值/结构化字段（剂量计算、时间线重建、编码映射），将在模型层面普遍采用“自然语言—工具协作”架构：模型负责语言与策略，工具负责精算/数据库查询/合规校验。Toolformer/Gorilla/ToolLLM 的理念将被移植到医疗接口层并与院内 EHR 深度集成。[arxiv.org](https://arxiv.org/abs/2302.04761)[arxiv.org](https://arxiv.org/abs/2305.15334)  
3) 垂直多模态语料与行业大模型化。为满足医学长尾知识与罕见病场景的需求，2025 年后垂直语料库建设（多机构、多模态、标准化标注）将是优先工程。垂直大模型（以行业语料微调或从头训练）将在特定科室/任务（放射、病理、慢病管理）里超越通用 LLM 的表现，但其可持续更新与跨机构通用性仍是主要挑战。[sciengine.com](https://www.sciengine.com/doi/pdf/74BC9028A25F462FB32CBA8EBB02732D)  
4) 评价范式走向“任务+风险”复合指标。简单的自动化文本指标无法捕捉临床风险，未来评测将结合：临床决策一致性、误导性/错诊风险度量、证据可追溯率与人机协同效率。社区会趋向建立跨机构的标准化基准集（包含注释好的危险案例与罕见病样例）。  
5) 法规、伦理与责任分担将驱动工程设计。随着商业化部署，模型输出的责任分配（医生 vs. 系统）将影响接口设计（例如强制人工复核、高风险标记机制、输出不可直接作为诊断结论等），这将限制端到端自动化而推动以“辅助—校验”为主的渐进式采纳策略。[xuebao.301hospital.com.cn](https://xuebao.301hospital.com.cn/article/doi/10.12435/j.issn.2095-5227.24070201)

结论  
2022–2025 年的工作表明：生成式 AI 在临床文档自动化上具有显著潜力，但要达到临床可用且合规的水平，需要三条并行推进：高质量多模态与可审计语料库建设、工程化的检索/工具调用与二次核查机制，以及面向临床风险的评测标准化。短期（1–3 年）可预期的成果是“人机协同的高效草稿与可溯源辅助决策”，而非完全自动化替代人工书写。研究者应优先解决检索证据质量、跨模态对齐与隐私合规这三大技术与制度问题，才能把生成式 AI 安全地推向临床文档生产线。

参考文献（按文中出现次序，均为真实公开文献/报告）  
1. Lewis P, Perez E, Piktus A, et al. Retrieval-augmented generation for knowledge‑intensive NLP tasks. arXiv:2005.11401 (2020). [arxiv.org](https://arxiv.org/abs/2005.11401)  
2. Gao Y, Xiong Y, Gao X, et al. Retrieval-augmented generation for large language models: a survey. arXiv:2312.10997 (2024). [arxiv.org](https://arxiv.org/abs/2312.10997)  
3. Jin L, et al. MedRAG: enhancing retrieval-augmented generation with knowledge graph-elicited reasoning for healthcare copilot. arXiv:2502.04413 (2025). [arxiv.org](https://arxiv.org/abs/2502.04413)  
4. Schick T, Dwivedi-Yu J, Dessì R, et al. Toolformer: language models can teach themselves to use tools. arXiv:2302.04761 (2023). [arxiv.org](https://arxiv.org/abs/2302.04761)  
5. Patil S G, Zhang T, Wang X, et al. Gorilla: large language model connected with massive APIs. arXiv:2305.15334 (2023). [arxiv.org](https://arxiv.org/abs/2305.15334)  
6. Qin Y, Liang S, Ye Y, et al. ToolLLM: facilitating large language models to master 16000+ real-world APIs. arXiv:2307.16789 (2023). [arxiv.org](https://arxiv.org/abs/2307.16789)  
7. Qian Q, Sun L, Liu J, et al. 基于判别增强大语言模型微调的医学影像报告生成. 计算机应用研究, 2025, 42(3):762–769. (MedVLM; 判别增强微调, 肺部 CT 报告实验与定量结果). [arocmag.cn](https://www.arocmag.cn/abs/2024.08.0303)  
8. Shen J, Huang R, Min D, et al. 卫生健康行业垂直大模型破茧之基石——构建行业专业多模态语料库. 科学通报 (Science Bulletin), 2025. 系统提出“疾病—场景关联矩阵”与语料库标准体系。 [sciengine.com](https://www.sciengine.com/doi/pdf/74BC9028A25F462FB32CBA8EBB02732D)  
9. 金哲, 邹健, 李逍, 等. 检索增强生成技术在医学人工智能中的应用与前沿探索. 药物流行病学杂志, 2025. 对医学场景下 RAG 的应用、幻觉问题与工程实践做中文综述。 [ywlxbx.whuznhmedj.com](https://ywlxbx.whuznhmedj.com/journal/481.html)  
10. Shen Z, et al. 大语言模型在临床医学领域的应用、挑战和展望. 中国医学（301 医学学报）综述, 2025.（医院/临床角度的系统梳理） [xuebao.301hospital.com.cn](https://xuebao.301hospital.com.cn/article/doi/10.12435/j.issn.2095-5227.24070201)  
11. Liu X, et al. A generalist medical language model for disease diagnosis assistance. Nature Medicine (2025) — DOI:10.1038/s41591-024-03416-6; PubMed record.（通用/专科结合的医学诊断辅助模型示例，见原文） [pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/39779927)  
12. Wang H, Feng Y, Xie X, et al. Path pooling: train-free structure enhancement for efficient knowledge graph retrieval-augmented generation. arXiv:2503.05203 (2025).（关于结构化知识与 RAG 的结合） [arxiv.org](https://arxiv.org/abs/2503.05203)  
13. Sankararaman H, Yasin M N, Sorensen T, et al. Provenance: a light-weight fact-checker for retrieval augmented LLM generation output. arXiv:2411.01022 (2024).（检索增强验证/事实核查机制） [arxiv.org](https://arxiv.org/abs/2411.01022)  
14. Ji Z, Lee N, Frieske R, et al. Survey of hallucination in natural language generation. ACM Computing Surveys, 2023.（幻觉现象的分类与检测方法综述） [doi.org](https://doi.org/10.1145/3571730)  
15. 王昊奋等. 基于大语言模型的重大慢病健康管理信息系统构建. 计算机研究与发展 (或相关会议/期刊), 2024.（领域语料+工具增强在慢病管理中的工程案例） [crad.ict.ac.cn](https://crad.ict.ac.cn/article/doi/10.7544/issn1000-1239.202440570?viewType=HTML)

（注：上述参考文献中以 arXiv、期刊与权威检索库为主；文中对中文综述/工程实践的引用用于反映 2024–2025 年在国内医疗场景的研究/部署进展。）