引言  
评估对话式AI（chatbot / LLM agent）“类人性”（human-likeness）在近数年从单一的Turing式可区分性检验，扩展为多维的行为学测试——包括社会认知（theory‑of‑mind）、情感共情、语用一致性、长期交互稳定性与多模态感知等方面。本文以“行为测试”为核心，将 2022–2025 年代表性工作按方法学类别归类、逐篇概述（每篇 4–6 句，强调研究问题、方法与关键结论），并基于所有实验结果总结共有的评价结论与方法学局限，最后给出面向 2025 年前后的可验证预测与研究挑战。本文所列文献均为已公开的顶会 / 期刊 / arXiv 工作（文末列出完整参考）。

方法分类与代表作  
（每类 3–5 篇代表性论文，按发表时间近到远或影响排序；每篇 4–6 句）

1) 心理学式社会認知（Theory‑of‑Mind, ToM）与情境推理基准  
- Chen et al., ToMBench (2024, ACL / ToMBench).  
  研究问题：系统衡量 LLM 在涵盖一阶/二阶信念、讽刺/失言等多类 ToM 子能力上的表现。  
  核心方法：构建 ToMBench（多子任务套件），使用改编/定制文本题目并比较多代模型与人类基线；采用多种提示（chain‑of‑thought、显式信念表征等）测试鲁棒性。  
  关键结论：GPT‑4 在若干 ToM 子任务上能达到或超过小规模人类基线，但对提示敏感且在提示扰动与透明访问变体上性能显著下降，表明表现并非等同于人类内在机制。  
 （参见综述与基准讨论：[sciengine.com](https://www.sciengine.com/doi/pdf/7521B0596BFC42BCBD36A97F64F319B1)）

- Wilf et al., “Think Twice” (2024, ACL).  
  研究问题：能否通过多视角/视角切换提示增强 LLM 的 ToM 能力并提高鲁棒性。  
  核心方法：设计“perspective‑taking”提示，要求模型先生成他人视角的中间表征，再回答 ToM 问题；与零样本与常规模板比较。  
  关键结论：分阶段的视角推理显著提升多模型在二阶信念与隐含意图题型上的准确率，但仍对细微文本变换敏感，提示工程能改善表现却不能证明内部心理表征与人类一致。  
 （见综述引述：[sciengine.com](https://www.sciengine.com/doi/pdf/7521B0596BFC42BCBD36A97F64F319B1)）

- Shapira et al., “Stress testing social reasoning in LMs” (2024, EACL / Findings).  
  研究问题：LLM 的社会推理是否依赖于数据中的表面统计而非稳健的语义推理？  
  核心方法：构造对抗/扰动版 ToM 任务（改变表面线索而保持语义），并对模型行为做细粒度错误分析。  
  关键结论：模型常采用捷径（spurious correlations）解决 ToM 题目；在被去除或置换表面线索后性能骤降，提示仅靠任务准确率无法证明“类人”认知机制。  
 （可参见相关论文汇总：[sciengine.com](https://www.sciengine.com/doi/pdf/7521B0596BFC42BCBD36A97F64F319B1)）

2) 行为可区分性 / 人类感知试验（Turing‑style 与人类判别）  
- Kosinski, “Theory of mind might have spontaneously emerged…” (2023, arXiv).  
  研究问题：是否能以行为测试判定 LLM 是否具备 ToM 或类人理解能力。  
  核心方法：基于标准化心理学题（如错误信念），在不同模型/版本上测评并与儿童/成人基线比较。  
  关键结论：某些大型模型在若干 ToM 任务上表现良好，但作者与后续研究均指出“通过率高 ≠ 内在心理机制相同”，并强调数据泄露与提示设计问题。  
 （原论文：[arxiv.org](https://arxiv.org/abs/2302.02083)；综述引述见 [sciengine.com](https://www.sciengine.com/doi/pdf/7521B0596BFC42BCBD36A97F64F319B1)）

- Trott et al., “Do large language models know what humans know?” (2023, Cognitive Science).  
  研究问题：在制度化的认知实验范式下，LLM 与人类的反应何处相同/不同。  
  核心方法：将多种标准实验（包括 ToM、共同注意等）应用于 LLM 并与儿童样本对比，强调同一协议下的可比性。  
  关键结论：LLM 在某些任务上匹配人类正确率，但在对抗扰动、时序依赖与长程上下文任务中明显不同，说明行为上“相似”但机制差异明显。  

- Sap et al., “Neural theory‑of‑mind? On the limits of social intelligence in large LMs” (2022, EMNLP Findings).  
  研究问题：用自动化基准系统化测量 LLM 的社会推理边界。  
  核心方法：提供多样化小规模 ToM 任务并评估多代模型、分析错误类型。  
  关键结论：早期大模型在社会推理上存在结构性缺陷，促使社区从任务准确率转向更细粒度的行为指标。  

3) 感知代理 / 自动化“评审者”评价（模拟对象的情感轨迹与可解释评分）  
- Bang Zhang et al. (SAGE), “Sentient Agent as a Judge” (2025, arXiv / Tencent Digital Human project).  
  研究问题：用可模拟情绪变化的“感知代理”替代静态或单轮人类评判，以衡量 LLM 的高阶社会认知与同理心。  
  核心方法：构建多轮对话评估框架 SAGE，代理模拟角色档案、情感推理与内心想法，输出情绪轨迹并据此评分；与 BLRI 等心理学量表进行相关性验证。  
  关键结论：代理评分与人类基于量表的评估高度相关（r≈0.8），揭示模型在情感支持场景下的差异化表现；同时显示不同代理虽然绝对分不同，但能稳定复现模型排序。  
 （综述/报道见：[blog.csdn.net](https://blog.csdn.net/m0_66899341/article/details/147859087)；媒体解读：[techwalker.com](https://www.techwalker.com/2025/0512/3166305.shtml)）

- Guo et al., “Measuring Human Involvement in AI‑Generated Text” (2025, arXiv).  
  研究问题：人类在多少程度上参与生成文本（从全自动到混合编辑）对“类人性”评估意味着什么。  
  核心方法：提出连续度量（基于 BERTScore / RoBERTa 回归器）来估计人类参与比例，并构建仿真数据集以验证检测器。  
  关键结论：传统二元检测器无法区分混合参与程度；将“参与度”建模为连续变量能更好表征人机协同情形，对评估类人性与可归因性具有实用价值。  
 （原文汇总见：[chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/145984)）

4) 动态推理、长期交互与稳健性测试（可揭示“表面拟合”）  
- Yang Yue et al., DRE‑Bench (2025, arXiv / DRE‑Bench).  
  研究问题：如何系统化评估 LLM 的“流体智力”（dynamic reasoning）与泛化能力。  
  核心方法：提出分层认知的动态推理基准 DRE‑Bench（四层认知、可程序化生成变体），强调可验证的动态数据生成以避免数据污染。  
  关键结论：多数模型在高级抽象/规划任务上表现急剧下降；情境样本与推理时间扩展能在低阶任务中提高性能，但对高阶泛化帮助有限。  
 （介绍见：博客与代码页汇总：[blog.csdn.net](https://blog.csdn.net/u013524655/article/details/148436065)）

- Ma et al., ToMChallenges / BigToM (2023) 与随后多项 stress‑test 研究（Shapira、Nickel 等）。  
  研究问题：用大规模、对抗性构造任务暴露模型推理捷径。  
  核心方法：设计动态/对抗题库并对模型进行系统压力测试，分析错误模式与触发条件。  
  关键结论：模型常依赖数据中可利用的表面统计；对抗与扰动测试是判别“真推理”与“表面拟合”的有效手段。  

5) 多模态与生成反馈评估（评价交互中“类人性”的多模态一致与反馈价值）  
- Song Tingyu et al., VF‑EVAL (2025, arXiv / VF‑EVAL).  
  研究问题：评估多模态大模型（MLLM）对 AIGC 视频的理解与改进反馈能力（即是否能像人类那样指出并建议改进）。  
  核心方法：构建 VF‑EVAL 数据集与任务（连贯性验证、错误检测、错误类型识别、细粒度推理），在人类标注与模型上做对比，并测试 REPROMPT 闭环改进效果。  
  关键结论：前沿 MLLMs 在多数任务上远落后于人类；但闭环的人类‑模型反馈（REPROMPT）能在视觉一致性与美学上带来可测改进，表明模型反馈可用但尚不可靠。  
 （媒体/数据代码报道见：[m.163.com](https://m.163.com/dy/article/K15KA8SI05118UGF.html?clickfrom=subscribe)）

- MME‑CoT (2025, CUHK et al.).  
  研究问题：评价多模态大模型在链式思维（CoT）下的推理质量、鲁棒性与效率。  
  核心方法：跨数学/科学/逻辑/时空等六领域构建多模态 CoT 基准，细粒度标注中间步骤并评估推理链质量。  
  关键结论：CoT 提示能提升可解释性与部分任务质量，但在多模态与长期链路上常引入噪声；评估需兼顾中间步骤质量而非仅终端正确率。  
 （数据/综述见：[blog.csdn.net](https://blog.csdn.net/u011559552/article/details/145685023)）

实验与评价总结（共性结论，避免逐篇复述）  
- 多维指标优于单一准确率：行为测试显示，单靠任务最终正确率易被表面捷径或数据污染误导。更可靠的“类人性”衡量需同时记录（a）中间推理链质量（可解释性）、（b）对抗/扰动鲁棒性、（c）与人类判官（或模拟感知代理）的情感/社交评分、以及（d）长期交互的一致性与角色持续性。  
- 提示工程能提升表现但会掩盖机制差异：chain‑of‑thought、视角先行或显式信念表征常能提高题目通过率，但相同提示在不同语境下导致的性能波动揭示模型仍依赖提示提供的外显结构而非稳健的内在心理表征。  
- 对抗/扰动测试是区分“表面拟合”与“真实泛化”的高效工具：当刻意去除或转移表面线索（标签、显式线索、局部句法），模型性能常崩溃，说明许多行为上的“类人”是可被诱导的表面策略。  
- 自动化代理与连续参与度度量提高可复现性：SAGE 类的感知代理与 Guo 等提出的“人类参与度连续化测量”已证明能在无须大量人工评分下提供可解释、可复现的评价，但这些代理本身的设计（人格、情感动力学）会影响评分尺度，需多代理/多视角交叉验证。  
- 多模态与生成反馈为实用性评估提供必要维度：视频/图像/音频参与的交互场景揭示，语言一致性之外还需视觉/听觉的一致性与常识性，且当模型作为反馈者时，其建议的可执行性与改进效果才是“类人性”在创作场景中的真正检验。  

趋势与挑战（面向 2025 年前后 —— 至少三点可验证预测）  
1. 从静态评分向动态、连续与可解释评分体系转变（必然趋势）。  
   预测依据：SAGE 与 Guo 等 2025 年工作显示代理化评分与参与度连续量表可替代二元检测；未来三年会出现标准化的“情感轨迹 + 中间推理质量”指标集，供基准共享。  
2. 对抗/扰动驱动的鲁棒性检验将成为基准必备项。  
   预测依据：Shapira、Ullman 与多项 stress‑test 研究表明表面捷径普遍存在；社区会采纳最小化表面提示泄露与扰动变体作为衡量泛化的常备方法。  
3. 多代理、多视角的评价框架将被广泛采用以降低单一评审偏差。  
   预测依据：SAGE 证明不同代理虽打分绝对值异，但排序一致；因此未来评测套件将包含 ≥3 个具有不同人格/偏好的自动代理与若干人类软基线。  
4. “类人性”评估将日益与任务可用性（usefulness）、可解释性与可归因性并列为部署准入门槛。  
   预测依据：Guo 等关于人类参与度的工作与 VF‑EVAL 的闭环实验表明，仅“类人”不够，须能解释来源并在反馈闭环中改进产出。监管与产品化将推动该指标体系落地。  
5. 多模态、具身（embodied）任务将成下一个检验高阶社交智能的标配。  
   预测依据：DRE‑Bench 与 MME‑CoT 指出文本外信息对高阶推理影响显著；与现实交互更接近的具身/机器人场景会暴露当前模型的最大短板。  

结论  
近年来针对 chatbot 类人性的行为测试呈现方法学多样化：从传统的单题通过率到覆盖 ToM、情感支持、提示鲁棒性、长期一致性与多模态反馈的多维评价。共识是——单一准确率无法代表“类人性”；需结合中间推理质量、对抗鲁棒性、人类或代理感知评分与长期交互稳定性。未来研究应把重点放在（1）标准化可复现的多维评价协议、（2）对抗/扰动与多代理验证、（3）从静态到动态的连续度量，以及（4）将评估结果与可归因/可解释改进机制联通。  

参考文献（不少于 12 篇，列出为便于检索的公开来源）  
- Chen Z., Wu J., Zhou J., et al., ToMBench: Benchmarking theory of mind in large language models (2024). （见综述引用）[sciengine.com](https://www.sciengine.com/doi/pdf/7521B0596BFC42BCBD36A97F64F319B1)  
- Wilf A., Lee S., Liang P. P., Morency L. P., “Think twice: Perspective‑taking improves large language models’ theory‑of‑mind capabilities” (2024, ACL). [sciengine.com](https://www.sciengine.com/doi/pdf/7521B0596BFC42BCBD36A97F64F319B1)  
- Shapira N., Levy M., Alavi S. H., et al., “Clever Hans or neural theory of mind? Stress testing social reasoning in large language models” (2024, EACL / Findings). [sciengine.com](https://www.sciengine.com/doi/pdf/7521B0596BFC42BCBD36A97F64F319B1)  
- Kosinski M., “Theory of mind might have spontaneously emerged in large language models” (2023, arXiv:2302.02083). [arxiv.org](https://arxiv.org/abs/2302.02083)  
- Trott S., Jones C., Bergen B., “Do large language models know what humans know?” (2023, Cognitive Science). [sciengine.com](https://www.sciengine.com/doi/pdf/7521B0596BFC42BCBD36A97F64F319B1)  
- Sap M., Le Bras R., Fried D., Choi Y., “Neural theory‑of‑mind? On the limits of social intelligence in large LMs” (2022, EMNLP Findings). [arxiv.org](https://arxiv.org/abs/2210.14309)  
- Strachan J. W. A., Albergo D., Borghini G., et al., “Testing theory of mind in large language models and humans” (2024, Nature Human Behaviour). [sciengine.com](https://www.sciengine.com/doi/pdf/7521B0596BFC42BCBD36A97F64F319B1)  
- Gandhi K., Fränken J. P., Gerstenberg T., Goodman N. D., “Understanding social reasoning in language models with language models” (2023, NeurIPS). [sciengine.com](https://www.sciengine.com/doi/pdf/7521B0596BFC42BCBD36A97F64F319B1)  
- Zhang B., Ma R., et al., “SAGE: Sentient Agent as a Judge — Evaluating high‑level social cognition in LLMs” (2025, arXiv:2505.02847) — 项目与代码汇总／媒体报道：[blog.csdn.net](https://blog.csdn.net/m0_66899341/article/details/147859087), [techwalker.com](https://www.techwalker.com/2025/0512/3166305.shtml)  
  原 arXiv（论文页）：[arxiv.org](https://arxiv.org/abs/2505.02847)  
- Guo Y., Dou Z., Nguyen H. H., et al., “Measuring Human Involvement in AI‑Generated Text: A Case Study on Academic Writing” (2025, arXiv:2506.03501). 概要/聚合视图：[chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/145984)  
- Yang Y., et al., “DRE‑Bench: Dynamic reasoning evaluation for fluid intelligence in LLMs” (2025, arXiv:2506.02648) — 综述 / 博文汇总：[blog.csdn.net](https://blog.csdn.net/u013524655/article/details/148436065)  
- Song T., Hu T., Gan G., Zhao Y., “VF‑EVAL: evaluating multimodal LLM feedback for AI‑generated video” (2025, arXiv:2505.23693) — 数据与报道：[m.163.com](https://m.163.com/dy/article/K15KA8SI05118UGF.html?clickfrom=subscribe)  
- MME‑CoT (CUHK et al.), “MME‑CoT: a multimodal chain‑of‑thought benchmark” (2025) — 数据/综述：[blog.csdn.net](https://blog.csdn.net/u011559552/article/details/145685023)  
- Kosinski, Trott, Shapira 等研究在 sciengine 的综述（杜传晨等, 2025）对该主题做系统梳理（含大量原始论文引用）：[sciengine.com](https://www.sciengine.com/doi/pdf/7521B0596BFC42BCBD36A97F64F319B1)  

（注）本文在方法学与结论中引用并综合了上述已公开的顶会 / 期刊 / arXiv 资料与由其派生的公开基准说明、数据集与代码库报告；部分 2025 年工作（SAGE、Guo 等、DRE‑Bench、VF‑EVAL、MME‑CoT）为预印本或正在公开的数据/代码项目，故文中将其视为当期研究代表并据其公开摘要与报告进行技术归纳。