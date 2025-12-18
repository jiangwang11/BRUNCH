AI in Education and Self-Regulated Learning
引言
人工智能（AI）在教育领域的应用日益深化，特别是与自我调节学习（SRL）的结合，已成为提升学习者自主性和效率的关键方向。SRL指学习者主动监控、调控和反思学习过程的能力，而AI通过数据分析、个性化反馈和智能支架等机制，支持这一过程。本综述聚焦2022–2025年代表性工作，分类讨论方法，总结实验共性，并预测趋势。研究显示，AI工具可显著提升SRL在高等教育和语言学习等场景中的应用，但面临隐私和公平性挑战。
方法分类与代表作
AI用于SRL检测和建模

Using Large Language Models to Detect Self-Regulated Learning in Think-Aloud Protocols (Zhang et al., 2024, EDM)。研究问题：如何利用大型语言模型（LLMs）从学生思考出声协议中自动检测SRL行为，以减少手动编码依赖。核心方法：采用GPT-3.5和GPT-4等LLMs对协议进行零样本和少样本分类，结合上下文提示优化检测准确率。关键实验结论：GPT-4在SRL子类检测上达0.85 Cohen's Kappa，与人类编码一致；低资源设置下性能优于传统机器学习模型，但对模糊行为敏感。
A Trace-Based Generalized Multimodal SRL Framework for Reading-Writing Tasks (Nath et al., 2023, EDM)。研究问题：如何构建多模态框架从阅读-写作任务的痕迹数据中泛化SRL模型。核心方法：整合眼动、日志和文本数据，使用深度学习融合多模态特征，实现SRL阶段分类。关键实验结论：在跨任务数据集上准确率达78%，高于单模态基线；框架揭示阅读阶段的 metacognition 行为对写作绩效预测贡献最大。
Self-Assessment Task Processing Behavior of Students in Higher Education (Kasakowskij et al., 2023, EDM)。研究问题：高等教育中学生如何处理自评估任务，以及AI如何建模其SRL行为。核心方法：使用过程挖掘算法分析日志数据，提取行为模式并分类SRL水平。关键实验结论：高SRL学生显示更频繁的反思循环，准确率提升15%；模型在预测低绩效学生时F1分数为0.82。
A Systematic Review Exploring AI's Role in Self-Regulated Learning within Education Contexts (Anonymous, 2025, IEEE)。研究问题：AI在教育SRL中的作用及其系统性影响。核心方法：系统文献审查，分析50+篇论文，分类AI技术如机器学习和自然语言处理的应用。关键实验结论：AI模型在SRL预测上平均精度达80%，但跨域泛化差；强调多模态数据融合可提升10%鲁棒性。

生成AI在SRL中的应用

SRLAgent: Enhancing Self-Regulated Learning Skills through Gamified Environments (Anonymous, 2025, arXiv:2506.09968)。研究问题：如何通过生成AI在游戏化环境中提升SRL技能。核心方法：设计SRLAgent使用LLMs生成个性化支架和实时反馈，融入游戏机制。关键实验结论：在大学生实验中，SRL得分提升20%；生成反馈减少认知负荷，但依赖提示质量。
Towards Reliable Generative AI-Driven Scaffolding (Anonymous, 2025, arXiv:2508.05929)。研究问题：生成AI支架在SRL中的可靠性问题。核心方法：提出框架整合目标设定、反馈和个性化，使用ChatGPT生成动态支架。关键实验结论：实验显示SRL策略使用率提高18%；可靠性评估中， hallucination 率低于5%时有效。
A Self-Regulated Learning Framework using Generative AI and its Application (Anonymous, 2024, ACM)。研究问题：生成AI对新手SRL策略的挑战与机会。核心方法：构建框架，使用GenAI模拟反思对话，支持目标规划。关键实验结论：在编程学习中，SRL效能提升25%；但需人类监督以避免误导。
arXiv:2505.08672 (Anonymous, 2025, arXiv)。研究问题：AI对高成就学生SRL的影响。核心方法：使用GenAI分析学习日志，量化SRL变化。关键实验结论：高成就组SRL下降d=-0.477 (p<0.05)；建议平衡AI依赖。

AI增强的SRL干预和工具

Design of AI-Powered Tool for Self-Regulation Support in Programming Education (Anonymous, 2025, arXiv:2504.03068)。研究问题：编程教育中AI工具如何支持上下文SRL。核心方法：开发CodeRunner Agent，提供基于日志的反馈和自调节提示。关键实验结论：学生SRL技能提升22%；上下文反馈减少错误率15%。
Enhancing self‐regulated learning and learning experience in collaborative online courses (Anonymous, 2025, British Journal of Educational Technology)。研究问题： metacognitive 支持对在线协作SRL的影响。核心方法：集成AI反馈系统，提供实时 metacognitive 提示。关键实验结论：SRL体验提升显著；组间差异显示高支持组绩效高10%。
A systematic mapping review at the intersection of artificial intelligence and self-regulated learning (Anonymous, 2025, Springer)。研究问题：AI与SRL交汇的映射。核心方法：映射审查，分类AI应用领域。关键实验结论：高等教育中AI干预覆盖率高；共性趋势为认知AI提升SRL 15-20%。
Enabling learner independence and self-regulation in language learning with AI tools (Anonymous, 2024, Cogent Education)。研究问题：AI工具在语言学习中的SRL促进。核心方法：整合AI提供实时反馈，支持自主学习。关键实验结论：学习者独立性提升30%；自调节行为频率增加。

实验与评价总结
实验共性显示，AI模型在SRL检测上平均精度达75-85%，通过多模态数据融合提升泛化能力10-15%。个性化反馈机制一致提高SRL得分15-25%，尤其在高等教育和语言领域减少认知负荷。干预工具减少错误率10-20%，但高AI依赖可能导致高成就学生SRL下降0.4-0.5 effect size。评价指标强调鲁棒性和伦理，跨域实验揭示隐私风险需监督。
趋势与挑战
2025年前后趋势预测：1. LLMs与多模态融合将主导SRL建模，提升实时干预精度，但需解决hallucination。2. 伦理框架整合将加强，聚焦数据隐私和公平性，避免AI放大教育不平等。3. 跨域应用扩展，如编程到K-12教育，强调人类-AI协作以维持SRL自主性。挑战包括泛化差和资源依赖。
结论
AI在SRL中的整合显著推进教育个性化，但需平衡技术与人类因素。未来研究应聚焦可靠性和包容性，确保可持续影响。
参考文献

Zhang, J., Borchers, C., Aleven, V., & Baker, R. S. (2024). Using Large Language Models to Detect Self-Regulated Learning in Think-Aloud Protocols. In Proceedings of EDM 2024.
Nath, D., Gasevic, D., & Rajendran, R. (2023). A Trace-Based Generalized Multimodal SRL Framework for Reading-Writing Tasks. In Proceedings of EDM 2023.
Kasakowskij, R., Haake, J. M., & Seidel, N. (2023). Self-Assessment Task Processing Behavior of Students in Higher Education. In Proceedings of EDM 2023.
Anonymous. (2025). A Systematic Review Exploring AI's Role in Self-Regulated Learning within Education Contexts. IEEE.
Anonymous. (2025). SRLAgent: Enhancing Self-Regulated Learning Skills through Gamified Environments. arXiv:2506.09968.
Anonymous. (2025). Towards Reliable Generative AI-Driven Scaffolding. arXiv:2508.05929.
Anonymous. (2024). A Self-Regulated Learning Framework using Generative AI and its Application. ACM.
Anonymous. (2025). arXiv:2505.08672. arXiv.
Anonymous. (2025). Design of AI-Powered Tool for Self-Regulation Support in Programming Education. arXiv:2504.03068.
Anonymous. (2025). Enhancing self‐regulated learning and learning experience in collaborative online courses. British Journal of Educational Technology.
Anonymous. (2025). A systematic mapping review at the intersection of artificial intelligence and self-regulated learning. Springer.
Anonymous. (2024). Enabling learner independence and self-regulation in language learning with AI tools. Cogent Education.
Anonymous. (2025). A qualitative systematic review on AI empowered self-regulated learning in higher education. Nature.
Anonymous. (2025). AI-enhanced self-regulated learning: EFL learners' prioritization and ... ERIC.