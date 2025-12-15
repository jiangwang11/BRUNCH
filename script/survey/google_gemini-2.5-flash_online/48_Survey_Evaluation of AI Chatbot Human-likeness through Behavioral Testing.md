## 评估人工智能聊天机器人类人度的行为测试学术综述 (2022-2025)

### 引言

随着大型语言模型（LLMs）的飞速发展，人工智能聊天机器人在自然语言理解和生成方面的能力日益增强，对社会科学、人机交互以及人工智能伦理等领域产生了深远影响。特别是在模拟人类行为、记忆和思维方面，LLMs展现出前所未有的潜力。然而，它们的“类人度”是否能被严格定义、量化和评估，以及其在不同情境下的表现与人类存在哪些系统性差异，仍是当前研究的核心问题。本综述旨在梳理2022-2025年期间，通过行为测试评估AI聊天机器人类人度的主流方法、代表性工作、关键发现，并展望未来的研究趋势与挑战。行为测试，作为图灵测试的延伸，通过观察和分析AI在特定任务或交互中的输出行为，以判断其与人类行为的相似程度，避免了依赖主观判断的局限性。

### 方法分类与代表作

当前评估AI聊天机器人类人度的行为测试方法主要集中在以下几个方面：

#### 1. 计算图灵测试与语言特征分析

这类方法旨在通过量化的语言特征和机器学习分类器，系统性地区分AI生成文本与人类文本，从而评估AI的类人度。

*   **Pagan, Törnberg, Bail, Hannák, & Barrie (2025)** [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/207138)：该研究引入了一种计算图灵测试框架，结合聚合指标（基于BERT的可检测性和语义相似性）与可解释的语言特征（风格标记和主题模式），以评估LLM与人类语言的接近程度。他们系统比较了九个开放权重LLM在五种校准策略下的表现，揭示LLM输出即使经过校准仍与人类文本存在显著差异，特别是在情感语调和表达方面。研究强调了优化类人性常以语义忠实度为代价的权衡。
*   **Guo, Dou, Nguyen, Chang, Sugawara, & Echizen (2025)** [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/145984)：这项工作聚焦于测量AI生成文本中人类参与的程度，而非简单的二元区分。他们提出使用BERTScore作为衡量人类参与度的指标，并训练了一个基于RoBERTa的多任务回归模型。实验在模拟学术写作场景的连续数据集上进行，结果表明该方法成功量化了不同程度的人类参与，超越了传统二元检测器的局限性。
*   **Ren, Geng, & Wu (2023)** [lis.ac.cn](https://www.lis.ac.cn/CN/10.13266/j.issn.0252-3116.2023.22.014)：这篇综述系统梳理了聊天机器人评估的指标、方法和应用领域。它指出了现有评估方法的局限性，并强调了在对话质量、用户体验和特定任务表现等方面的评估维度。尽管并非专注于计算图灵测试，但其对评估指标和方法的分类为理解类人度评估提供了宏观视角。

#### 2. 心理测量学与心理属性评估

这类方法借鉴心理学领域的理论和工具，通过设计任务或对话来探测AI的心理属性（如人格、情感、社会智能等），进而评估其类人程度。

*   **Li, Huang, Wang, Zhang, Zou, & Sun (2024)** [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/f5ffe17f-f1f6-4ad3-b358-82204340be16)：该团队提出了一个评估LLM心理学的框架和心理测量基准，涵盖人格、价值观、情感、心智理论、动机和智力六个维度。他们的研究发现LLMs展现出广泛的心理属性，但也存在自我报告特质与现实行为之间的差异。这表明目前的LLMs在模拟人类心理复杂性方面仍有挑战。
*   **Zhang, Ma, et al. (2025) (腾讯研究)** [techwalker.com](https://www.techwalker.com/2025/0512/3166305.shtml)：腾讯“混元智能数字人类”团队引入了SAGE（Sentient Agent as a Judge）评测框架，使用“有感知代理”作为评判者来评估LLM的高阶社交认知能力。该框架通过模拟人类情绪变化的评委，考察AI能否真正理解并回应人类情感需求。研究发现，传统的LLM排名与SAGE的社交智能排名存在差异，且先进模型在社交智能方面取得了显著进步。
*   **Song, G. J., et al. (北京大学团队) (2025)** [news.qq.com](https://news.qq.com/rain/a/20250527A04GXT00) [finance.sina.com.cn](https://finance.sina.com.cn/tech/roll/2025-05-27/doc-inexyrua0228913.shtml)：北京大学宋国杰教授团队发布了首篇大语言模型心理测量学系统综述。该综述强调，传统AI评估方法无法满足LLM不断增长的“心智”特征评估需求，并提出了构念导向评估、严谨方法应用和项目反应理论应用三大创新方向，以更科学地量化和理解LLM的心理特质。

#### 3. 角色扮演与社会交互评估

这类方法通过让AI扮演特定角色，并在模拟的社会交互情境中进行行为测试，以评估其社会智能和角色一致性。

*   **Chen, Chen, Yan, Xu, Xing, Shen, Quan, Li, Zhang, & Huang (2025)** [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/49871)：该研究提出了SocialBench，这是第一个旨在系统评估角色扮演代理在个体和群体社交互动层面的社会性的基准。SocialBench涵盖500个角色、6000多个问题提示和30800个多轮角色扮演发言，并发现个体层面表现优异的代理在群体层面并不必然表现出色。这突出了评估AI社会性复杂度的挑战。
*   **裴芮民, 曹彦臣, 刘昱威 (2025)** [openreview.net](https://openreview.net/pdf/46a6e94e9705d3e661798b222f523524f45b1755.pdf)：这篇论文提出通过高级机器学习方法模拟LLM对人类行为、记忆和思维的能力。研究旨在正式定义并量化LLM的模拟程度，计划使用行为、记忆和思维的综合模拟度量指标进行评估。通过将LLM与外部记忆模块和推理引擎结合，在对话、记忆检索和逻辑推理等数据集上进行实验评估。
*   **解煜彬, 周荣刚 (2025)** [sciengine.com](https://www.sciengine.com/doi/pdf/4BC60E56182F4CE1BF396FC0C04B3FE5)：该文探讨了新型人机关系下的人机双向信任，强调了“感知信任”作为人机互信交互渠道的重要作用。文中系统梳理了人机信任测量与计算建模方法的最新进展，尽管主要关注信任，但其提出的行为信任度量（依赖行为、合作行为、建议采纳行为）可被视为评估AI在社会交互中类人度的行为指标。

### 实验与评价总结

针对人工智能聊天机器人类人度行为测试的实验与评价，当前研究表现出一些共性结论：

*   **与人类文本存在系统性差异：** 尽管LLMs生成文本逼真，但计算图灵测试结果普遍表明，AI的输出在聚合语言特征和风格上与人类文本存在明显可区分的系统性差异，特别是在情感表达、上下文细微差别和风格变异方面。指令调优模型表现可能不如基础模型，且模型规模扩大不一定增强类人性 [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/207138)。
*   **类人性与语义忠实度之间的权衡：** 优化AI的类人风格往往以牺牲语义准确性为代价。即使是可检测性较低的模型，在情感和社会类别上仍存在显著差异，表明规避分类器并不等同于真正的情感或社会对齐 [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/207138)。
*   **社交智能的多维性：** AI的社交智能存在多维度差异。在个体层面表现出色的代理，在群体社交互动中可能表现不佳 [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/49871)。传统的任务导向评估忽视了关系质量和对话过程中情绪状态的变化，导致与社交智能评估结果的差异 [techwalker.com](https://www.techwalker.com/2025/0512/3166305.shtml)。
*   **心理属性的广泛分布与局限性：** LLMs展现出广泛的心理属性，但也存在自我报告特质与现实行为不一致的情况。在培养AI同时具备高度创造性和深度共情能力方面仍有显著空白 [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/f5ffe17f-f1f6-4ad3-b358-82204340be16), [techwalker.com](https://www.techwalker.com/2025/0512/3166305.shtml)。
*   **人类参与的影响：** 评估AI生成文本时，人类参与的程度是一个重要变量，简单的二元分类不足以反映人机协作的复杂性。量化人类参与的持续性指标有助于更全面地评估生成内容的真实性 [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/145984)。

### 趋势与挑战

2025年前后，评估AI聊天机器人类人度的研究趋势与挑战主要体现在：

*   **多模态与跨领域社会智能评估：** 未来的研究将不再局限于文本模态，而是扩展到语音、视觉等多模态交互场景，以更全面地评估AI在复杂社会情境中的类人度。挑战在于如何统一和融合这些异构数据，并构建跨领域的通用评估基准。
*   **动态与情境感知评估：** 传统的静态基准测试难以捕捉AI在长期交互、多轮对话中动态变化的心智特征和情绪状态。未来的趋势是开发能够适应上下文、追踪情绪变化、并评估AI在不同情境下行为一致性的动态评估框架 [techwalker.com](https://www.techwalker.com/2025/0512/3166305.shtml)。
*   **心理学与认知科学的深度融合：** 随着AI心智研究的深入，心理测量学和认知科学理论将更紧密地融入评估方法。这包括利用项目反应理论（IRT）进行动态校准，以及基于人类认知模型（如ACT-R）来理解和增强AI的记忆和思维能力，旨在揭示LLM“心智”的深层机制 [news.qq.com](https://news.qq.com/rain/a/20250527A04GXT00), [openreview.net](https://openreview.net/pdf/46a6e94e9705d3e661798b222f523524f45b1755.pdf)。
*   **双向信任与人机情感/社会对齐：** 人机交互将从单向评估转向双向信任的构建与评估，即不仅评估人类对AI的信任，也探讨AI如何“感知”并“回应”人类的信任。研究将关注如何通过AI的行为传递信任信号，以及这种双向信任感知如何影响人机协作绩效和用户接受度 [sciengine.com](https://www.sciengine.com/doi/pdf/4BC60E56182F4CE1BF396FC0C04B3FE5)。
*   **可解释性AI与伦理考量：** 随着AI类人度的提升，其“黑箱”特性带来的伦理问题（如数据污染、偏见、情感操纵等）将愈发突出。未来的研究需要更多地关注评估方法的可解释性，不仅要量化AI的类人度，还要理解其生成这些行为的原因，从而指导负责任的AI开发和部署。

### 结论

通过行为测试评估人工智能聊天机器人类人度是当前AI领域的重要研究方向。从计算图灵测试中的语言特征分析，到借鉴心理测量学的心理属性评估，再到角色扮演情境下的社会交互测试，多种方法共同揭示了当前LLMs在类人度方面的进步与局限。虽然LLMs在生成逼真文本和模拟特定心理属性上取得了显著进展，但在情感深度、语义忠实度、创造性与共情能力的结合以及真正的社会智能方面，与人类仍存在系统性差异和挑战。未来的研究将趋向于多模态、动态、情境感知、心理学深度融合的评估，并更加重视双向信任和伦理可解释性，以推动AI向更安全、可靠、普惠和真正“以人为本”的方向发展。

### 参考文献

1.  Pagan, N., Törnberg, P., Bail, C. A., Hannák, A., & Barrie, C. (2025). Computational Turing Test Reveals Systematic Differences Between Human and AI Language. *arXiv preprint arXiv:2511.04195*. [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/207138)
2.  Guo, Y., Dou, Z., Nguyen, H. H., Chang, C.-C., Sugawara, S., & Echizen, I. (2025). Measuring Human Involvement in AI-Generated Text: A Case Study on Academic Writing. *arXiv preprint arXiv:2506.03501*. [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/145984)
3.  Ren, M., Geng, Q., & Wu, Y. (2023). 聊天机器人评估研究综述：指标、方法与应用领域 [A Review on Chatbot Assessment: Indicators, Methods and Application]. *图书情报工作*, *67*(22), 140-148. [lis.ac.cn](https://www.lis.ac.cn/CN/10.13266/j.issn.0252-3116.2023.22.014)
4.  Li, Y., Huang, Y., Wang, H., Zhang, X., Zou, J., & Sun, L. (2024). Quantifying AI Psychology: A Psychometrics Benchmark for Large Language Models. *arXiv preprint arXiv:2406.18375*. [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/f5ffe17f-f1f6-4ad3-b358-82204340be16)
5.  Zhang, B., Ma, R., et al. (2025). 有感知代理作为评判者：评估大型语言模型中的高阶社交认知 [Sentient Agents as Judges: Evaluating Higher-Order Social Cognition in Large Language Models]. *arXiv preprint arXiv:2505.02847v2*. [techwalker.com](https://www.techwalker.com/2025/0512/3166305.shtml)
6.  Song, G. J., et al. (2025). Large Language Model Psychometrics: A Systematic Review of Evaluation, Validation, and Enhancement. *arXiv preprint arXiv:2505.08245*. [news.qq.com](https://news.qq.com/rain/a/20250527A04GXT00) [finance.sina.com.cn](https://finance.sina.com.cn/tech/roll/2025-05-27/doc-inexyrua0228913.shtml)
7.  Chen, H., Chen, H., Yan, M., Xu, W., Xing, G., Shen, W., Quan, X., Li, C., Zhang, J., & Huang, F. (2025). SocialBench: Sociality Evaluation of Role-Playing Conversational Agents. *Findings of the Association for Computational Linguistics: ACL 2024*. [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/49871)
8.  裴芮民, 曹彦臣, 刘昱威 (2025). 基于高级机器学习的大语言模型对人类行为、记忆和思维的模拟研究. *Open Review*. [openreview.net](https://openreview.net/pdf/46a6e94e9705d3e661798b222f523524f45b1755.pdf)
9.  解煜彬, 周荣刚 (2025). 新型人机关系下的人机双向信任 [The bidirectional trust in the context of new human-machine relationships]. *心理科学进展*, *33*(6), 916–932. [sciengine.com](https://www.sciengine.com/doi/pdf/4BC60E56182F4CE1BF396FC0C04B3FE5)
10. Lyons, J. B., Wynne, K. T., Mahoney, S., & Roebke, M. A. (2019). Trust and human-machine teaming: A qualitative study. In Lawless, W., Mittu, R., Sofge, D., Moskowitz, I. S., & Russell, S. (Eds.), *Artificial intelligence for the Internet of everything* (pp. 101–116). Academic Press.
11. Hoff, K. A., & Bashir, M. (2015). Trust in automation: Integrating empirical evidence on factors that influence trust. *Human Factors*, *57*(3), 407–434.
12. Lee, J. D., & See, K. A. (2004). Trust in automation: Designing for appropriate reliance. *Human Factors*, *46*(1), 50–80.