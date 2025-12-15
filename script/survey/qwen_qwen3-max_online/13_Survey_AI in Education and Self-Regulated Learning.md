# 人工智能赋能自我调节学习：2022–2025年研究综述

## 引言

自我调节学习（Self-Regulated Learning, SRL）作为学习者主动设定目标、监控过程并调整策略的核心能力，是终身学习的关键。生成式人工智能（GenAI）的兴起，尤其是以ChatGPT为代表的大语言模型，为SRL研究与实践开辟了新范式。区别于传统计算机辅助学习环境（CBLEs）中预设规则的有限支持，GenAI凭借其强大的内容生成、自然语言交互与上下文理解能力，能够动态响应学习者的复杂需求，嵌入SRL的完整循环（计划、策略、监测）。本文聚焦2022至2025年间的代表性工作，系统梳理AI赋能SRL的技术路径、实证发现及未来挑战，旨在为构建“人机协同”的下一代学习环境提供理论参照。

## 方法分类与代表作

### 1. GenAI作为认知脚手架与个性化导师

此类研究将GenAI视为可动态提供认知支持的“虚拟导师”，通过对话交互嵌入SRL过程。

朱俊华等人（2025）基于对大学生与ChatGPT自发对话的质性分析，发现学生主要将AI用作写作助手、工具和SRL辅导教师 [ymc.gzu.edu.cn](https://ymc.gzu.edu.cn/_t1039/2025/0324/c8954a246887/page.htm)。研究编码出9类SRL行为，证实AI在“目标导向搜索”和“知识拓展”方面支持显著，但在“学习计划制定”和“内容充分性评估”等高阶元认知活动中，学生参与度低，其效能高度依赖学习者的前置知识与元认知水平。

Huang等人（2025）提出了一种两层问题驱动的个性化学习方法，利用GenAI为学生生成符合其认知水平的探究性问题与学习材料 [sci-open.net](https://sci-open.net/index.php/ETR/article/view/3490)。实验表明，该方法能显著提升学生的阅读表现，其核心机制在于AI通过推理链解释，有效促进了学生的元认知调控，帮助其从信息加工层面跃迁至高阶思维。

Fu与Hiniker（2025）的研究则聚焦AI在阅读理解中的认知支持，展示了AI不仅能提供词汇与句法层面的即时帮助，更能通过生成逻辑推理链条，引导学生进行批判性思考 [sci-open.net](https://sci-open.net/index.php/ETR/article/view/3490)。这种策略性反馈超越了传统纠错功能，直接作用于SRL的监控与调节阶段。

### 2. AI驱动的智能辅导系统（ITS）与教育智能体

此类研究超越了简单的问答交互，致力于构建具备自主性、记忆和规划能力的智能教育代理。

王宇程（2025）系统论述了基于大语言模型的教育智能体（Educational Intelligent Agent）架构，其核心包含规划体、记忆体和工具体 [hanspub.org](https://pdf.hanspub.org/ces_3095840.pdf)。该架构能将复杂学习任务分解为子目标（规划），利用RAG技术检索知识（记忆），并调用外部工具执行（行动），形成“感知-决策-行动”闭环，为个性化SRL提供系统性支持。

李柠希（2025）针对心理学实验教学，提出构建“实验心理学”垂直领域大模型作为智能助教 [hanspub.org](https://www.hanspub.org/journal/paperinformation?paperid=113716)。该模型不仅可辅助学生进行实验设计与数据分析，更能通过“提出任务–人机协同–批判创新”的新模式，引导学生在自主创新实验中实践SRL，有效缓解了“实验难”与“创新难”问题。

郑博芳与汤金坤（2025）构建了“认知–情感–社会”三元理论框架，强调智能系统应同时提供认知支持、情感激励与社会协作 [hanspub.org](https://pdf.hanspub.org/ae2025154_1651169260.pdf)。其设计的自适应教育内容推荐系统，能根据学生学业表现与兴趣动态调整材料，体现了智能辅导系统在个性化学习路径规划上的进阶。

### 3. AI辅助的学习动机与效果干预研究

此类研究采用量化方法，实证检验AI工具对学习动机、效果及依赖性的综合影响。

刘昕畅（2025）通过元分析方法，整合多项研究发现，AI能通过个性化学习、互动问答和创新评估显著提升学生的学习动机与效果 [sci-open.net](https://www.sci-open.net/index.php/FSS/article/view/1748)。然而，研究也警示了过度依赖的风险，即可能导致学生思维能力下降和学习动机减弱，强调了教师引导的必要性。

舒琪等人（2025）通过问卷调查300名学生，量化了AI读写工具的双刃剑效应 [hanspub.org](https://pdf.hanspub.org/oetpr202571_31310138.pdf)。数据显示，AI在提升语法、拼写等基础技能上效果显著（80%学生认可），但对创意写作帮助有限（仅45%）。更重要的是，65%的学生承认对AI产生依赖，且在无AI辅助时写作能力下降，独立思考与创造力受到抑制。

## 实验与评价总结

综合上述研究，可归纳出以下共性结论：
1.  **支持的非对称性**：AI在SRL的“策略执行”阶段（如信息搜索、知识拓展、基础技能练习）支持效果最为显著，但在“高阶元认知”阶段（如目标设定、深度反思、批判性评估）的作用有限，其效能高度依赖于学习者自身的元认知能力。
2.  **依赖性的普遍性**：多项实证研究一致发现，学生普遍存在对AI工具的依赖性，这种依赖在短期内可提升学习效率和信心，但长期可能削弱其独立思考、问题解决和创造性表达能力。
3.  **人机协同的必要性**：所有研究均指向“AI+教师”的双轨模式是最佳实践。AI擅长处理标准化、重复性任务和提供即时反馈，而教师则在高阶思维引导、情感支持、价值观塑造和防止技术滥用方面不可替代。

## 趋势与挑战

基于2022-2025年的研究进展，可以预见以下真实趋势：
1.  **从通用模型到领域垂直智能体**：研究将从直接调用通用大模型（如ChatGPT）转向构建深度融合学科知识与教学法的垂直领域教育智能体，如李柠希（2025）提出的“实验心理学”大模型 [hanspub.org](https://www.hanspub.org/journal/paperinformation?paperid=113716)。
2.  **从被动响应到主动引导式交互**：未来的AI系统将超越“有问必答”模式，采用“苏格拉底式”提问、提供线索而非直接答案等方式，强制激发学生的元认知活动，如王宇程（2025）架构中的“规划体”与“反思”机制 [hanspub.org](https://pdf.hanspub.org/ces_3095840.pdf)。
3.  **伦理与素养并重的治理框架**：随着AI深度融入教育，研究焦点将从技术效能转向构建包含AI素养教育、数据隐私保护、算法透明化及防止数字鸿沟在内的综合性治理框架，如杨德升等人（2025）所强调的技术、教师与制度三维度协同 [hanspub.org](https://pdf.hanspub.org/ces_3095457.pdf)。

## 结论

2022至2025年间，AI赋能SRL的研究已从概念验证走向深度实证，清晰揭示了其在提升学习效率与激发认知依赖之间的张力。未来研究的核心在于构建真正意义上的“人机协同”生态：技术上发展具备主动引导能力的领域智能体，教学上强化教师对AI工具的驾驭与引导能力，制度上建立保障教育公平与伦理的治理规范。唯有如此，AI才能真正成为促进而非替代人类自主学习能力的赋能工具。

## 参考文献

1.  朱俊华, 许璐瑶, 马近远. (2025). 生成式人工智能如何赋能学生学习 ——基于大学生自我调节学习行为的实证研究. *高等工程教育研究*, (2), 66-72. [ymc.gzu.edu.cn](https://ymc.gzu.edu.cn/_t1039/2025/0324/c8954a246887/page.htm)
2.  Huang, C., et al. (2025). Enhancing student reading performance through a personalized two-tier problem-based learning approach with generative artificial intelligence. *Humanities and Social Sciences Communications*, 12(1), 1-16. [sci-open.net](https://sci-open.net/index.php/ETR/article/view/3490)
3.  Fu, Y., & Hiniker, A. (2025). Supporting students' reading and cognition with AI. *arXiv preprint arXiv:2501.0139*.
4.  王宇程. (2025). 基于大语言模型的教育智能体个性化学习应用理论研究. *创新教育研究*, 13(11), 486-492. [hanspub.org](https://pdf.hanspub.org/ces_3095840.pdf)
5.  李柠希. (2025). 生成式人工智能影响下的心理学实验教学：现状、改进与展望. *教育进展*, 15(5), 163-168. [hanspub.org](https://www.hanspub.org/journal/paperinformation?paperid=113716)
6.  郑博芳, 汤金坤. (2025). 人工智能赋能教育的理论框架与实践创新. *教育进展*, 15(4), 1165-1171. [hanspub.org](https://pdf.hanspub.org/ae2025154_1651169260.pdf)
7.  刘昕畅. (2025). 人工智能对学习者学习动机与效果的影响研究. *社会科学前沿*, 1(4). [sci-open.net](https://www.sci-open.net/index.php/FSS/article/view/1748)
8.  舒琪, 王文正, 翟健. (2025). 人工智能辅助工具对学生读写能力的影响：自主学习与依赖性的平衡探讨. *国外英语考试教学与研究*, 7(1), 25-30. [hanspub.org](https://pdf.hanspub.org/oetpr202571_31310138.pdf)
9.  李黎婕. (2025). 人工智能反馈机制对大学生英语阅读理解能力的提升作用探讨. *教育理论与研究*, 1(5). [sci-open.net](https://sci-open.net/index.php/ETR/article/view/3490)
10. 杨德升, 姜娜, 刘静, 朱国进, 刘音序. (2025). 人工智能辅助教学在高等教育中的挑战与影响. *创新教育研究*, 13(8), 286-292. [hanspub.org](https://pdf.hanspub.org/ces_3095457.pdf)
11. Bastani, H., et al. (2024). Generative AI Can Harm Learning. *The Wharton School Research Paper*. [papers.ssrn.com](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4895486)
12. Ng, D. T., Tan, C. W., & Leung, J. K. (2024). Empowering student self‐regulated learning and science education through ChatGPT: a pioneering pilot study. *British Journal of Educational Technology*, 55(4), 1328-1353.