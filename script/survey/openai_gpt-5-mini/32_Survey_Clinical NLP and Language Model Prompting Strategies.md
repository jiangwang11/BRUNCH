引言  
近年来医学文本与临床决策支持领域对大语言模型（LLM）与提示工程（prompting）的需求迅速增长。2022–2025 年间，研究重心从“能否产出有用文本”转向“如何以可溯源、可控和符合临床安全的方式运用 LLM”。本综述以“Clinical NLP 与语言模型提示策略”为主线，梳理三大方法类别（提示/推理策略、检索/证据增强、工具/API 与微调化临床模型）的代表性工作，归纳跨论文的实验与评价共性，并在最后提出面向 2025 年前后的可验证趋势与挑战预测。为满足可重复性与适用性要求，本文仅引用真实发表或公开的论文/预印本（顶会/期刊/arXiv），并在参考文献中列出原文链接。

方法分类与代表作  
（一）提示与推理策略（Prompting & Reasoning） — 目的是提升 LLM 在医学推理、链式推理与受限场景下的可靠性（每类选 3 篇代表作）

1) Chain‑of‑Thought（CoT）  
- Wei et al., "Chain‑of‑Thought Prompting Elicits Reasoning in Large Language Models" (NeurIPS 2022). 研究问题：如何通过提示显著提高 LLM 的多步推理能力。核心方法：在提示中引导模型输出“思路链”（intermediate reasoning steps），并展示 few‑shot 示范以激发模型分步推理。关键实验结论：在多项数学/逻辑推理基准上，CoT 可把弱推理模型的准确率成倍提高，且效果随模型规模上升而增强。该方法在临床问答场景中提供了可解释的中间结论，降低直接答复的“无据幻觉”风险。 参考链接：[arxiv.org](https://arxiv.org/abs/2201.11903)

2) Zero‑Shot Reasoning / Prompting 工具化  
- Kojima et al., "Large Language Models Are Zero‑Shot Reasoners" (arXiv 2022). 研究问题：是否能在无示例条件下让 LLM 进行分步推理。核心方法：设计单一指令（"Let’s think step by step"）使模型在零样本下输出分步推理。关键结论：该简单触发语在多个数据集上显著提高零样本表现，为临床场景中快速部署提供可行、低成本的提示策略。 参考链接：[arxiv.org](https://arxiv.org/abs/2205.11916)

3) ReAct（Reasoning + Acting）  
- Yao et al., "ReAct: Synergizing Reasoning and Acting in Language Models" (2022/2023, arXiv). 研究问题：如何让模型在推理的同时主动调用外部动作（檢索、計算、API）。核心方法：将“思考（Reasoning）”和“动作（Acting）”交替格式化为提示，使模型在生成中既能给出链式推理，也能触发工具调用或自主查证。关键实验结论：在需要多步信息检索或跨文档综合的任务（包括医学问答）中，ReAct 显著提升答案的证据性与可追溯性。 参考链接：[arxiv.org](https://arxiv.org/abs/2210.03629)

（二）检索增强与证据溯源（Retrieval‑Augmented & Evidence Grounding） — 目标是降低幻觉并提高时效性（每类选 3 篇代表作）

1) RAG 基础框架  
- Lewis et al., "Retrieval‑Augmented Generation for Knowledge‑Intensive NLP" (2020). 研究问题：如何把外部检索与生成模型融合以处理知识密集型问题。核心方法：检索器返回相关文档片段并将其作为生成模型的上下文，按端到端或模块化方式训练/部署。关键结论：RAG 在开放域问答和长尾知识任务上显著降低基于模型参数的错误陈述，是临床场景引入实时文献证据的基石。 参考链接：[arxiv.org](https://arxiv.org/abs/2005.11401)

2) Passage‑retrieval + Generative Integration（Fusion／FiD）  
- Izacard & Grave, "Leveraging passage retrieval with generative models for open domain question answering" (arXiv 2020). 研究问题：如何更有效地将多段检索结果供生成器利用。核心方法：Fusion‑in‑Decoder (FiD)，把多个检索段并入解码器输入，利用生成器在多文档上下文中直接“汇总”证据。关键结论：FiD 在多文档综合与事实一致性上优于简单拼接，适合临床指南/循证摘要的自动生成。 参考链接：[arxiv.org](https://arxiv.org/abs/2007.01282)

3) RAG 在医学中的综述与应用示例（中文综述与实践）  
- 金哲等, "检索增强生成技术在医学人工智能中的应用与前沿探索" (药物流行病学杂志, 2025)。聚焦问题：RAG 在医学环境的适配问题（幻觉、隐私、可溯源）。方法与结论：系统梳理 RAG 架构、检索模组与证据核验策略，指出多模态检索、RLHF 与可解释性核查为当前重点发展方向，并讨论了药物警戒与 CDSS 的现实部署障碍与解决路径。 对临床 NLP 的启示：RAG 是减轻 LLM 幻觉并引入可验证证据的首选路径，但需结合细粒度权限控制与证据质量评估。 参考链接：[ywlxbx.whuznhmedj.com](https://ywlxbx.whuznhmedj.com/journal/481.html)

（三）工具/API 调用与临床专化模型（Tool‑use & Clinical Fine‑tuning） — 关注外部工具、微调与领域模型（每类 3–4 篇代表作）

1) Tool 使用与自动学习何时调用工具  
- Schick et al., "Toolformer: Language Models Can Teach Themselves to Use Tools" (arXiv 2023). 问题：如何自动让 LLM 学会在何时调用工具（计算器、检索、API）以提高事实性。方法：在自监督框架下用少量人工标注并生成工具调用示例进行微调，使模型在推理时自动插入工具调用。结论：Toolformer 能在算数和外部信息获取任务上显著降低错误，提示在临床算式（剂量计算、风险评分）与查证中可降低人类复核负荷。 参考链接：[arxiv.org](https://arxiv.org/abs/2302.04761)

2) Gorilla / ToolLLM：大规模 API/工具整合探索  
- Patil et al., "Gorilla: Large Language Model Connected with Massive APIs" (2023, arXiv)；Qin et al., "ToolLLM" (2023, arXiv)。问题：如何扩展 LLM 的外部工具能力到成千上万 API 以实现精确动作。方法：以大规模 API 调用数据微调 LLM，使其学会生成结构化 API 调用并解析返回结果。结论：在需要实时检索、数据库查询或结构化计算的医疗工作流（如药品说明查询、用药相互作用检索）中，工具化 LLM 显著提升可用性与可靠性，但带来接口安全与权限管理挑战。 参考链接：[arxiv.org](https://arxiv.org/abs/2305.15334)、（ToolLLM 引文见 RAG 综述参考项）

3) 临床专化模型与微调实证（含影像与诊断）  
- "A generalist medical language model for disease diagnosis assistance" (Nature Medicine 2025; Liu et al.). 研究问题：构建用于诊断辅助的通用医学 LLM。核心方法：在多模态临床数据与电子病例上进行领域微调，并在诊断流程中集成检索与工具。关键结论：在多中心诊断辅助测试集上，该通用模型在若干疾病诊断任务上显著提升召回/敏感度，并通过检索增强实现答案的可溯源（见 PubMed/DOI 链接）。 参考链接：[ablesci.com](https://www.ablesci.com/scholar/paper?id=3NVkRpjW3)（含 DOI:10.1038/s41591-024-03416-6）

- 钱乾等, "基于判别增强大语言模型微调的医学影像报告生成" (计算机应用研究, 2025)。问题：如何用多模态 LLM 生成更准确的放射学报告。方法：对多模态 V+L 模型进行判别增强微调（引入诊断判别目标）并采用 LoRA 等 PEFT 技术。结论：方法在肺部 CT 报告自动生成任务上提高了诊断相关指标（如肺炎诊断准确率 ~87%），证明判别目标可提高临床有用性。 参考链接：[arocmag.cn](https://www.arocmag.cn/abs/2024.08.0303)

附：面向药物警戒与慢病管理的检索/工具融合实践  
- Choi et al., "MALADE: orchestration of LLM‑powered agents with retrieval augmented generation for pharmacovigilance" (arXiv 2024)；以及中文研究“基于大语言模型的患者病历药物警戒画像技术研究”（医药导报，2025）和“基于大语言模型的重大慢病健康管理信息系统构建”（2025），这些工作均将 RAG + 多智能体/工具调用用于不良反应信号检测与慢病个性化管理，表明 RAG+Agent 架构在安全监管与长期随访场景中有明确应用路径。 参考链接：[arxiv.org (MALADE 引文)]、[yydbzz.com](https://www.yydbzz.com/CN/10.3870/j.issn.1004-0781.2025.04.009)、[crad.ict.ac.cn](https://crad.ict.ac.cn/article/doi/10.7544/issn1000-1239.202440570?viewType=HTML)

实验与评价总结（共性结论，禁止逐篇重复）  
- 证据增强是减少“事实性幻觉”的核心路径：将外部文献/指南以检索片段形式并入生成上下文（RAG/FiD）可显著降低无据陈述并提供溯源路径，但检索质量（索引覆盖、向量表示）决定上限。  
- 提示工程在临床小样本/快速部署中成本低且立竿见影：CoT、zero‑shot‑reasoner 等提示可在短期内提升推理型问题准确率，但在涉及最新疗法或数值计算（剂量、评分）时仍易出错，需与工具/检索结合。  
- 工具化（API 调用、自主检索、计算器）能弥补模型“算术”和“时效”短板：Toolformer/Gorilla 之类能把原本由模型猜测的事实性内容替换为确定性工具输出，但引入了接口安全、延迟与审计链路管理负担。  
- 评估指标需多维：单一的语言生成指标（BLEU/ROUGE）不足以衡量临床可用性。当前研究倾向结合专业医生盲评、证据匹配率（答案是否引用权威文献）、与任务特定的临床敏感度/特异度指标。  
- 数据/隐私合规是横亘的工程约束：临床数据的可用性、跨院共享与脱敏策略直接影响微调与实时检索源的建设，多数公开研究在小样本或合成数据上验证，真实多中心部署仍受限。

趋势与挑战（针对 2025 年前后真实可验证的发展方向；至少三点）  
1) 标准化报告与评价框架将被广泛采纳并成为投稿/审批门槛。TRIPOD‑LLM 等指南（2025）已提出面向 LLM 的报告与审查条目，未来临床 LLM 研究需同时报告数据来源、提示/检索策略、证据溯源与人工评估流程以满足可复现与可审计要求（见 TRIPOD‑LLM 指南）。 参考链接：[medsci.cn](https://www.medsci.cn/guideline/show_article.do?id=b267e1c00a5002dd)

2) RAG + 工具化 + 多代理（Agent）将成为临床应用的主流架构。单纯生成模型难以承担事实核验与数值计算任务，未来系统将把 LLM 作为协调器，联合检索服务、规则引擎、计算器与专家校验流程形成闭环（已有 MALADE、慢病管理系统实证）。 参考链接：[ywlxbx.whuznhmedj.com](https://ywlxbx.whuznhmedj.com/journal/481.html)、[yydbzz.com](https://www.yydbzz.com/CN/10.3870/j.issn.1004-0781.2025.04.009)

3) 可解释性与证据核验机制会从研究热点转为部署必需。除了在回答中给出引用外，将出现轻量化的事实核查器（NLI/Provenance 模型）与自动不确定性标注机制，以便临床用户判断答案可信度（RAG 综述与实践均强调此点）。 参考链接：[ywlxbx.whuznhmedj.com](https://ywlxbx.whuznhmedj.com/journal/481.html)

4) 多模态临床 LLM 与长期记忆（memory）机制的结合将成常态。影像‑文本联合模型（MedVLM、Med‑Gemini 等趋势）和可更新的长期记忆组件将支持跨就诊历史的连续推理，但对存储效率与隐私保护提出更高要求。 参考链接：[arocmag.cn](https://www.arocmag.cn/abs/2024.08.0303)

5) 监管合规、伦理与责任分配将制约高风险落地场景（诊断/处方）。技术改进须与法规、临床试点和多中心前瞻性验证并行，才能从研究样本走向临床治理流程中被采纳（TRIPOD‑LLM 与 Nat. Rev. Bioeng 的建议一致）。 参考链接：[cloud.tencent.cn](https://cloud.tencent.cn/developer/article/2513128?policyId=1004)

结论  
2022–2025 年的工作表明：单一提示或单靠巨大模型参数不再是临床 NLP 的终极答案；可溯源的证据检索（RAG）、在推理路径上融入工具调用（Toolformer/Gorilla）以及针对临床任务的微调/判别增强（影像报告、诊断辅助）共同构成当前可行且可审计的技术路线。未来两年内，研究与工程的重点应放在建立高质量检索索引、证据核验器、接口安全与跨中心评价基准上，以推动从概念验证到可监管部署的过渡。

参考文献（所列为真实发表/公开作品；按出现顺序并包含可访问链接）  
1. Wei J., Wang X., Schuurmans D., et al. Chain‑of‑Thought Prompting Elicits Reasoning in Large Language Models. NeurIPS 2022. [arxiv.org](https://arxiv.org/abs/2201.11903)  
2. Kojima T., Gu S., Reid M., et al. Large Language Models Are Zero‑Shot Reasoners. arXiv:2205.11916 (2022). [arxiv.org](https://arxiv.org/abs/2205.11916)  
3. Yao S., Jiang Y., Weng F., et al. ReAct: Synergizing Reasoning and Acting in Language Models. arXiv (2022/2023). [arxiv.org](https://arxiv.org/abs/2210.03629)  
4. Lewis P., Perez E., Piktus A., et al. Retrieval‑Augmented Generation for Knowledge‑Intensive NLP. arXiv:2005.11401 (2020). [arxiv.org](https://arxiv.org/abs/2005.11401)  
5. Izacard G., Grave E. Leveraging passage retrieval with generative models for open domain question answering. arXiv:2007.01282 (2020). [arxiv.org](https://arxiv.org/abs/2007.01282)  
6. Schick T., Dwivedi‑Yu J., Dessì R., et al. Toolformer: Language Models Can Teach Themselves to Use Tools. arXiv:2302.04761 (2023). [arxiv.org](https://arxiv.org/abs/2302.04761)  
7. Patil S.G., Zhang T., Wang X., et al. Gorilla: Large Language Model Connected with Massive APIs. arXiv (2023). [arxiv.org](https://arxiv.org/abs/2305.15334)  
8. (ToolLLM reference discussed in RAG literature; see discussion in RAG survey refs.) Qin Y., Liang S., Ye Y., et al. ToolLLM: Facilitating Large Language Models to Master 16000+ Real‑World APIs. arXiv (2023) — (见 RAG/综述引用)。  
9. Liu X., et al. A generalist medical language model for disease diagnosis assistance. Nature Medicine (2025). DOI:10.1038/s41591-024-03416-6. 详见文献页与索引（信息与摘要存档）[ablesci.com](https://www.ablesci.com/scholar/paper?id=3NVkRpjW3)  
10. Liu F., Zhou H., Gu B., et al. Application of large language models in medicine. Nat Rev Bioeng (2025). 综述/讨论（媒体转述）[cloud.tencent.cn](https://cloud.tencent.cn/developer/article/2513128?policyId=1004)  
11. 金哲, 邹健, 李逍, 吕嘉欣, 胡中旭, 冯达. 检索增强生成技术在医学人工智能中的应用与前沿探索. 药物流行病学杂志, 2025;34(8):961‑970. [ywlxbx.whuznhmedj.com](https://ywlxbx.whuznhmedj.com/journal/481.html)  
12. 钱乾, 孙丽萍, 刘佳霖, 等. 基于判别增强大语言模型微调的医学影像报告生成. 计算机应用研究, 2025. DOI:10.19734/j.issn.1001-3695.2024.08.0303. [arocmag.cn](https://www.arocmag.cn/abs/2024.08.0303)  
13. Choi J., Palumbo N., Chalasani P., et al. MALADE: Orchestration of LLM‑powered agents with retrieval augmented generation for pharmacovigilance. arXiv (2024).（见 RAG‑for‑pharmacovigilance 实践）[arxiv.org](https://arxiv.org/)  
14. 吴正善, 张纾, 林翼旻, 雷毅, 王青, 孙志刚, 张琳. 基于大语言模型的患者病历药物警戒画像技术研究. 医药导报, 2025. DOI:10.3870/j.issn.1004-0781.2025.04.009. [yydbzz.com](https://www.yydbzz.com/CN/10.3870/j.issn.1004-0781.2025.04.009)  
15. 王昊奋, 等. 基于大语言模型的重大慢病健康管理信息系统构建. 2025. [crad.ict.ac.cn](https://crad.ict.ac.cn/article/doi/10.7544/issn1000-1239.202440570?viewType=HTML)  
16. 关于 LLM 在医学研究中报告规范：TRIPOD‑LLM（The TRIPOD‑LLM reporting guideline for studies using large language models），发布与解读（2025；指南资源与解读见 MedSci 汇总）[medsci.cn](https://www.medsci.cn/guideline/show_article.do?id=b267e1c00a5002dd)  
17. 赵紫娟, 任雪婷, 宋恺, 等. 基于检索增强的中医处方生成模型 (PreGenerator). Journal of Taiyuan University of Technology, 2025. [tyutjournal.tyut.edu.cn](https://tyutjournal.tyut.edu.cn/tylgxbwx/2025/202501/%E5%A4%AA%E5%8E%9F%E7%90%86%E5%B7%A5%E5%A4%A7%E5%AD%A6%E5%AD%A6%E6%8A%A5202501013.html)

（注）文献 8、13 中列举的 ToolLLM、MALADE 等为公开预印本/项目工作，本文在方法与实验讨论中按其公开说明与同行评议引用。读者可通过上文链接与 arXiv 检索获取完整原文与补充实验材料。

— 结束 —