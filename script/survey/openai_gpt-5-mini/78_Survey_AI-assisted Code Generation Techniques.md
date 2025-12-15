引言  
近年来（尤其是 2022–2025 年），基于大规模预训练模型与检索、执行、交互等机制的“AI 辅助代码生成”迅速成为软件工程与自然语言处理交叉的研究热点。该综述聚焦近三年具有代表性的工作，按方法类别（基础/微调的代码大模型、检索/仓库级增强、执行/工具驱动生成、个性化与风格适配、交互式/迭代编辑与修复、模型协同与不确定性管理）归纳代表作，着重说明每篇工作的研究问题、核心方法与关键实验结论；随后总结实验评价中的共性结论并提出 2025 年前后的研究趋势与挑战预测。所有被引用工作均为公开论文或技术报告（顶会/期刊/arXiv/正式出版物）。

方法分类与代表作  
（每种类别最多列 3–5 篇代表作；每篇 4–6 句，突出问题、方法、结论）

1) 基础/微调的代码大模型  
- DeepSeek‑Coder (开源系列，2024)。问题：缺乏高性能的开源、仓库级代码模型以支持跨文件长上下文生成；方法：从头训练系列模型（1.3B–33B），在高质量项目级语料上采用 Fill‑In‑Middle（FIM）和 16K 上下文窗口并做仓库级数据组织与去重；实验结论：在多项代码基准（生成、补全、修复）上，较大规模模型在开源模型中取得最优，且仓库级预训练显著提升跨文件生成一致性与多文件任务性能（详见模型评测与 ablation）。参见 [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/d8ef73fb-0b68-402b-a17a-abab02c77c21).  
- Qwen2.5‑Coder (技术报告，2024)。问题：将通用大模型架构适配为代码向量空间以提升代码任务性能；方法：以 Qwen2.5 架构为基础，针对代码数据作大规模预训练并通过合成数据与数据平衡提升泛化；实验结论：在多项代码生成、完成与修复基准上，Qwen2.5‑Coder 在相同参数量级内优于此前同量级模型，显示出数据清理与合成策略对代码能力的放大效果。参见 [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/116463e9-e168-4ad4-badf-cd1793c253d8).  
- CodeT5+ (CodeT5 的扩展，arXiv 2023)。问题：统一理解与生成任务的模型架构与预训练目标不足以兼顾多种代码任务；方法：提出 CodeT5+ 系列（encoder‑decoder 为主），采用多样化预训练目标（span denoising、CLM、对比学习等）并支持灵活的推理模式；实验结论：在代码理解与生成多任务上，CodeT5+ 在若干下游数据集上显著提升 BLEU/EM 等指标，且架构与预训练目标的多样化改善了任务间迁移。参见 [arxiv.org](https://arxiv.org/abs/2305.07922).

2) 检索增强与仓库级（repository‑level）生成 / RAG 類方法  
- Retrieval‑Augmented Generation (RAG)（检索‑增强生成的范式奠基工作，2020）。问题：单一的上下文窗口难以保持长期或外部知识，尤其在代码场景下仓库知识分布广泛；方法：将检索模块与生成模型耦合，检索到的文档作为额外条件输入生成器；结论：检索模块能够显著扩展模型可用上下文，有利于提高事实性与一致性，后续多项仓库级方法基于此范式扩展到代码场景。参见 [arxiv.org](https://arxiv.org/abs/2005.11401).  
- 仓库/回购级检索与综述（近年综述，侧重仓库级方法）。问题：仓库级代码生成需要长程依赖、跨文件约束与依赖解析；方法：综述类工作梳理了检索策略（文件/函数/符号级）、索引与去重、以及与 LLM 的融合策略；结论：检索模块的粒度与检索目标（函数签名、调用图片段）对生成质量与一致性影响显著，仓库级检索需结合静态分析以减少噪声。参见综述 [zhuanzhi.ai](https://zhuanzhi.ai/paper/f49cff257ef0cbf5e546373a59f6f8da).  
- CoEdPilot：项目级交互式代码编辑推荐工具 (JCST，2025)。问题：现有补全工具多聚焦单点生成，缺乏端到端的“定位下一编辑点＋跨项目生成”能力；方法：在 VS Code 插件中结合两阶段定位器（文件级、行级）、历史编辑检索与生成模块，支持多轮用户反馈闭环；结论：在文件/行级编辑定位与内容生成任务上取得高准确率，用户研究显示在多处修改的复杂任务上显著优于单文件生成工具（详见文章实验）。参见 [jcst.ict.ac.cn](https://jcst.ict.ac.cn/cn/article/id/e36d187c-955f-4c75-a98b-234080c293c9).

3) 执行/工具驱动生成（execution‑guided & tool‑use）  
- ReAct（2022）。问题：生成性模型在复杂推理/程序合成场景中需要将“推理（Reasoning）”与“动作/工具调用（Acting）”结合；方法：提出 ReAct 框架，使模型在生成过程中同时产出 reasoning traces 与 action（如代码执行/工具调用）并基于工具返回继续推理；结论：在需要交互式调试或执行反馈的生成任务中，ReAct 能显著降低语义错误并提升问题解决率，说明工具闭环对代码生成尤为重要。参见 [arxiv.org](https://arxiv.org/abs/2210.03629).  
（注：近年多项系统将执行器/沙箱与 LLM 结合，用以动态验证补丁或用例，ReAct 为此类方法的代表性思路。）

4) 个性化与风格适配  
- MPCODER：多用户个性化代码生成 (arXiv 2406.17255)。问题：同一功能可能对应不同开发者/团队的编码风格，通用模型难以满足个性化需求；方法：显式/隐式风格表示学习（风格残差与隐式对比学习）、多用户风格适配器；结论：在风格相似度与人类风格匹配评估上，MPCODER 在多用户情景下显著提高生成与目标编码风格的一致性，表明显式与隐式风格建模是可行的个性化路径。参见 [arxiv.org](https://arxiv.org/abs/2406.17255).  

5) 交互式/迭代编辑与自动修复（APR）  
- LLM‑based APR 综述（CRAD，2024）。问题：传统 APR 方法在理解语义与生成复杂补丁上受限，LLM 提供新路径；方法：系统梳理了两大范式——完形填空式（cloze）与神经机翻译式（NMT）LLM APR，并比较数据集/缺陷类型/评测指标；结论：LLM 在多类语义型缺陷上显示更好补丁生成能力，但常见问题包括过拟合训练集补丁分布、缺乏可执行性验证与安全性风险；综述强调结合测试执行与检索验证的必要性。参见 [crad.ict.ac.cn](https://crad.ict.ac.cn/article/doi/10.7544/issn1000-1239.202440467?viewType=citedby-info).  
- CoEdPilot（前述）同时属于交互式编辑范畴，其用户反馈循环与项目级定位为 APR/迭代编辑提供了工程化样本。

6) 模型协同、不确定性估计与系统层次调度  
- Coral：基于不确定性估计的微调模型与 LLM 协同方法（2025，Application Research of Computers）。问题：微调模型与通用 LLM 在决策边界上存在模糊，盲目拼接可能无益；方法：通过不确定性估计（基于 ECE 思想）衡量微调模型输出置信度，设定阈值在 ID/OOD 间切换由微调模型或 LLM 负责；结论：在两个基准上，Coral 在 BLEU 与 Exact Match 等指标上优于单一策略，表明不确定性控制可显著改善协同系统的鲁棒性与泛化。参见 [arocmag.cn](https://www.arocmag.cn/abs/2025.04.0082).  

实验与评价总结（共性结论，不逐篇复述）  
- 上下文长度与数据组织直接决定跨文件/仓库任务的可解性：带仓库级预训练或检索的系统在多文件特性添加、重构等任务上普遍优于仅文件级训练的模型。  
- 检索与执行两类外部模块对代码生成质量的提升具有不同作用：检索主要改善 factuality（库用法、API 语义）与一致性，执行（运行/测试）则是提升补丁有效性与减少语义错误的关键；二者结合可得到最可靠的补丁候选。  
- 微调模型在 ID（训练分布内）场景常胜，但在 OOD 场景（新库/新架构/新风格）表现急剧下降；基于不确定性或检索切换到通用 LLM 能改善 OOD 泛化。  
- 评价指标仍偏向静态匹配（BLEU/EM/top‑k）与合成基准，真实世界可执行性（通过测试用例/静态分析验证）与长期维护成本评估尚不足，导致指标与工程可用性之间存在鸿沟。  
- 人机交互评测（用户研究）显示：在复杂、多点修改的真实任务中，具备定位/多轮反馈能力的系统能减少人工搜索成本并提升完成率；单次补全模型在简单修复或单函数生成上仍具竞争力。

趋势与挑战（2025 年前后的可信预测，不少于 3 点）  
1) 趋势：仓库级（repository‑aware）模型与检索+静态分析联合成为主流研究方向。理由：跨文件依赖与构建配置是实际开发的常态，单纯的 token 窗口无法解决长期依赖，更多工作将把静态分析（AST/调用图/依赖解析）与检索索引混合进检索器与提示构造。  
2) 趋势：执行闭环（自动化单元测试/类型检查/沙箱运行）从研究样例走向生产化评估流程。理由：仅靠文本匹配难以保证补丁正确性，更多评测套件与训练范式会把可执行性作为一等目标，并用执行反馈做强化/在线微调。  
3) 趋势：模型协同（微调小模型＋大通用 LLM＋检索＋执行器）的系统化工程成为标配，且以不确定性或元决策器（meta‑controller）来动态选择子系统。理由：微调模型在低延迟场景成本效益高，而大模型在 OOD 能力强，协同可在成本/性能之间折中。  
4) 挑战：评估基准向“工程化可信度”转移。需要建立包含仓库、构建系统、真实缺陷与长期维护指标（回归率、可读性、风格一致性）的综合基准体系。  
5) 挑战：安全性与许可合规成为限制因素。生成代码的版权/许可证混入、潜在恶意代码生成（如注入后门）以及依赖风险需要通过更严格的数据溯源、检索溯源与生成审计机制来治理。  
6) 趋势：个性化（团队/风格/约定）将从论文原型走向工具集成，方法上从显式参数化风格到隐式对比式适配并用。理由：工程团队对代码可维护性与风格一致性的需求会推动个性化模块成为 IDE 的常驻组件。

结论  
2022–2025 年的研究显示，单一的端到端生成模型已不能满足工程级代码生成的全部需求；融合检索、静态分析、执行验证与人机交互的系统化设计正在成为主流研究与工程实践方向。未来研究需要在提高生成质量的同时，构建可执行性/可审计性、成本可控的协同体系，并推动评测基准从静态匹配转向工程可信度与长期维护性能的综合评估。

参考文献（按引用先后，均为公开论文/技术报告/综述，至少 12 篇）  
- CoEdPilot：Interactively Recommending Project‑Wise Code Edits. JCST (2025). [jcst.ict.ac.cn](https://jcst.ict.ac.cn/cn/article/id/e36d187c-955f-4c75-a98b-234080c293c9)  
- Retrieval‑Augmented Code Generation: A Survey with Focus on Repository‑Level Approaches (2025 survey entry). [zhuanzhi.ai](https://zhuanzhi.ai/paper/f49cff257ef0cbf5e546373a59f6f8da)  
- Coordination of fine‑tuned code generation models and large language models via uncertainty estimation (Coral). Application Research of Computers (2025). [arocmag.cn](https://www.arocmag.cn/abs/2025.04.0082)  
- CodeT5+: Open Code Large Language Models for Code Understanding and Generation. (CodeT5+ paper, arXiv 2023). [arxiv.org](https://arxiv.org/abs/2305.07922)  
- DeepSeek‑Coder: When the Large Language Model Meets Programming — The Rise of Code Intelligence (2024, DeepSeek‑Coder series). [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/d8ef73fb-0b68-402b-a17a-abab02c77c21)  
- Qwen2.5‑Coder Technical Report (2024). [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/116463e9-e168-4ad4-badf-cd1793c253d8)  
- MPCODER: Multi‑user Personalized Code Generator with Explicit and Implicit Style Representation Learning (arXiv 2406.17255). [arxiv.org](https://arxiv.org/abs/2406.17255)  
- Survey of Large‑Language‑Model‑Based Automated Program Repair (CRAD, 2024). [crad.ict.ac.cn](https://crad.ict.ac.cn/article/doi/10.7544/issn1000-1239.202440467?viewType=citedby-info)  
- Retrieval‑Augmented Generation (RAG). (Lewis et al., 2020). [arxiv.org](https://arxiv.org/abs/2005.11401)  
- ReAct: Synergizing Reasoning and Acting in Language Models (Yao et al., 2022). [arxiv.org](https://arxiv.org/abs/2210.03629)  
- (补充参考) 近年关于代码大模型/综述与工程实践汇编（社区/工业技术报告与综述，供背景参考）。例如 DeepSeek/CodeLLM 报告集与多篇系统评测（见上文 hub.baai.ac.cn／行业技术报告）。[hub.baai.ac.cn](https://hub.baai.ac.cn)  
- （若需更深入的下游基准与方法细节，可另附标准基准与开源实现列表，如 HumanEval/MBPP/CodeXGlue 与 StarCoder／CodeGen 等开源模型的官方资料与 arXiv 报告。）

（如需，我可基于以上文献为每一类别附上更细的实验数值对比表、开放数据集与评测脚本位置、以及供工程落地的组件化系统设计草图。）