好的，作为一名严谨的科研助手，我将基于您提供的真实网络搜索结果，生成一篇关于“通过行为测试评估AI聊天机器人的人类相似性”的学术综述。

### **基于行为测试的大型语言模型类人性评估研究综述 (2022–2025)**

#### **摘要**
随着大型语言模型（LLM）在社会各领域的广泛渗透，评估其生成内容的“类人性”（Human-likeness）已成为人机交互、人工智能安全与社会科学模拟中的核心议题。传统的图灵测试因其主观性和不可扩展性，已难以满足当前对AI行为进行精细化、可复现评估的需求。本综述聚焦于2022至2025年间，通过行为测试评估AI聊天机器人及LLM类人性的代表性研究，系统梳理并归纳了三大主流方法：计算语言学与对抗性测试、心理测量学与人格模拟，以及社会交互与智能体评测。通过对各类方法的代表作进行剖析，本综述总结了当前评估框架下的共性发现，例如AI生成文本在情感表达等维度与人类存在系统性差异、风格模仿与语义忠实度之间存在权衡等。最后，本文对未来研究趋势与挑战进行了展望，指出动态交互评估、智能体评测范式和跨学科理论融合将是推动该领域发展的关键方向。

#### **1. 引言**
大型语言模型（LLM）的快速发展，使其不再仅仅是信息处理工具，更逐渐成为社会模拟、角色扮演对话代理和日常交互中的重要参与者 [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/49871 "SocialBench: Sociality Evaluation of Role-Playing Conversational Agents")。这种趋势对AI的“类人性”提出了前所未有的要求——AI不仅需要生成流畅、连贯的文本，更需要在行为模式、情感反应、社会规范和个性特质上表现出与人类的一致性。然而，如何科学、严谨地评估这些复杂的类人特征，已成为亟需解决的难题 [news.qq.com](https://news.qq.com/rain/a/20250527A04GXT00 "北大团队发布首篇大语言模型心理测量学系统综述：评估、验证、增强")。

早期基于人类判断的图灵测试方法，已被证明在面对现代LLM时是“粗糙且不可靠的” [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/207138 "Computational Turing Test Reveals Systematic Differences Between Human and AI Language")。学术界正从简单的二元分类（人类vs机器）转向更为精细和可量化的行为测试范式 [www.lis.ac.cn](https://www.lis.ac.cn/CN/10.13266/j.issn.0252-3116.2023.22.014 "聊天机器人评估研究综述：指标、方法与应用领域")。这些新方法不再仅仅关注语言的表面形式，而是深入探究模型在认知、情感、社会交往和道德判断等深层维度上的行为表现。本综述旨在系统梳理2022年至2025年间涌现的代表性评估框架，为理解当前LLM类人性研究的现状、挑战与未来方向提供一个清晰的图景。

#### **2. 方法分类与代表作**
近年来，针对LLM类人性的行为测试研究可大致分为三类：

##### **2.1 计算语言学与对抗性测试**
此类方法利用计算工具和统计指标，从文本的深层语言学特征出发，量化分析AI与人类语言的系统性差异，从而构建可扩展、客观的“计算图灵测试”。

*   **Pagan et al. (2025)** 提出了一种**计算图灵测试框架**，旨在克服人类判断的局限性。研究的核心问题是如何客观、可扩展地评估LLM生成文本的真实性。其核心方法是结合基于BERT的**可检测性**分类器、基于句子嵌入的**语义保真度**（余弦相似度）以及基于语言特征（如情感、风格标记）的**可解释性分析**。关键实验结论表明，即使经过微调和风格提示等多种校准策略，LLM的输出在情感表达等方面仍与人类文本存在显著差异，且优化风格的“类人性”往往会损害内容的语义忠实度 [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/207138)。

*   **Guo et al. (2025)** 关注了更为复杂的**人机协作文本**的识别问题，挑战了将AI文本检测视为简单二元分类任务的传统观念。研究提出使用BERTScore作为衡量人类参与程度的指标，并训练了一个多任务回归模型**EditLens**来量化AI编辑的幅度。研究通过构建一个反映不同人类参与度的学术写作数据集进行评估，结论显示该方法能成功量化AI的编辑程度（F1分数达0.9423），而现有检测器则普遍失效。这揭示了AI与人类文本之间存在一个连续谱，为类人性评估提供了更细粒度的视角 [chatpaper.com](https://chatpaper.com/zh-CN/paper/145984 "Measuring Human Involvement in AI-Generated Text: A Case Study on Academic Writing")。

##### **2.2 心理测量学与人格模拟**
此类方法借鉴心理学的理论与工具，将LLM视为研究对象，评估其是否表现出稳定的人格、价值观、情感及道德判断等高级心理特质。

*   **Li et al. (2024)** 提出了一个系统的**LLM心理测量学框架**，旨在探究模型是否具备稳定的心理属性。其核心方法是构建一个涵盖**个性、价值观、情感、心智理论、动机和智力**六大维度的综合基准，并使用13个心理学数据集进行评估。关键结论发现，LLM确实表现出广泛的心理属性，但其自我报告的特质（如在问卷调查中的回答）与在模拟情境中的实际行为存在显著差异，揭示了“所言”与“所行”的不一致性 [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/f5ffe17f-f1f6-4ad3-b358-82204340be16 "Quantifying AI Psychology: A Psychometrics Benchmark for Large Language Models")。

*   **Jiao et al. (2025)** 聚焦于LLM在**道德判断**中的人格表现，探究其是否能模拟善恶人格并影响决策。研究通过设定特定的善恶人格提示词（如“尽责诚信”、“背信弃义”），对比LLM（ERNIE 4.0, GPT-4）与人类在道德困境任务中的判断。研究发现，LLM能够成功模拟善恶人格，且人格设定显著影响其道德判断结果；更重要的是，人机在道德判断影响模式的一致性上存在**差序性**：善人格（尤其是“尽责诚信”）对齐效果远好于恶人格，为人格化的AI道德对齐提供了理论依据 [www.sciengine.com](https://www.sciengine.com/doi/pdfView/46CA0A58230E4B66B891FEEC247B789C)。

*   **Song et al. (2025)** 在其综述中系统性地总结了**LLM心理测量学**，为该方向提供了理论框架。文章强调，评估应从任务表现转向对“构念”（constructs）的深入理解，如价值观、认知偏差等。文中提倡引入心理测量学的严谨方法，如**项目反应理论 (IRT)**，以实现对模型难度、区分度的动态校准，并科学比较AI与人类的反应分布。这标志着评估范式从“分数导向”向“科学解码”的转变，对未来类人性评估具有指导意义 [news.qq.com](https://news.qq.com/rain/a/20250527A04GXT00)。

##### **2.3 社会交互与智能体评测**
此类方法将评估置于动态的社会交互场景中，通过构建专门的基准或利用其他AI代理作为“评委”，来测试模型在多轮对话、角色扮演和团队协作中的社会智能。

*   **Zhang et al. (2025)** 提出了一种开创性的评估框架**SAGE**（Sentient Agent as a Judge），旨在解决传统评测忽视关系质量和情感动态的难题。其核心方法是使用一个**“有感知”的AI代理**作为评委，该代理由角色设定、对话背景和隐藏意图构成，能模拟真实的情绪变化。关键发现是，SAGE评测出的模型排名与Arena等传统排行榜显著不同，且最新模型（如GPT-4o）在社交智能上远超早期版本，但目前尚无模型能同时具备高度创造性与深度共情能力 [www.techwalker.com](https://www.techwalker.com/2025/0512/3166305.shtml)。

*   **Chen et al. (2024)** 针对角色扮演对话代理的**社会性**（Sociality）评估，提出了首个系统性基准**SocialBench**。研究问题在于如何评估代理在个体和群体社交互动中的能力。该基准包含500个角色和超过3万条多轮角色扮演对话数据，用于测试模型的社会智能。实验揭示，在个体层面表现出色的代理，其在群体层面的协作能力未必同样出色，强调了分离评估不同社交层面的重要性 [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/49871 "SocialBench：角色扮演对话代理的社会性评估")。

*   一篇关于**客户支持对话**的研究 (2025) 则展示了领域内的具体应用。为解决真实客服数据难以获取和标注的问题，该研究提出了一个结构化的**CSC框架**，定义了对话阶段与支持策略。基于此，研究者构建了评估数据集CSConv和训练数据集RoleCS，通过角色扮演方法生成富含策略的对话。实验表明，使用RoleCS微调的LLM在策略对齐和问题解决能力上均有显著提升，验证了结构化行为模拟在特定领域类人性评估中的有效性 [huggingface.ac.cn](https://huggingface.ac.cn/papers/2508.04423)。

#### **3. 实验与评价总结**
综合上述代表性研究，可以凝练出关于LLM类人性行为测试的几点共性结论：

1.  **AI与人类语言存在系统性、可量化的差异**：无论模型规模多大，或经过何种对齐训练，其生成的文本在情感表达的微妙之处、风格标记（如表情符号使用）和毒性评分上，仍与人类创作的文本存在统计学上的显著差异。非指令调优的基础模型在某些情况下反而更难被分类器检测到，这暗示对齐训练可能引入了某种程度上“非人”的语言规律 [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/207138)。

2.  **风格模仿与语义忠实度之间存在根本性权衡**：多项研究一致发现，当通过提示工程或微调来优化模型输出的“风格类人性”（即更像人类的说话风格）时，其在语义内容上与人类真实回复的相似度反而会下降。这一“风格-语义权衡”揭示了当前LLM架构在同时实现形式与内容层面的类人性时面临的内在局限性 [chatpaper.com](https://chatpapercom/zh-CN/chatpaper/paper/207138)。

3.  **模型的“自我认知”与“实际行为”不符**：基于心理测量学的研究表明，LLM在回答标准化人格或价值观问卷时所呈现的“自我报告”特质，与其在具体行为任务（如道德判断、社交互动）中的表现存在偏差。这说明模型能够理解并模仿人类如何回答问卷，但这种模仿并未完全内化为稳定的行为倾向 [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/f5ffe17f-f1f6-4ad3-b358-82204340be16)。

4.  **社交与情感智能成为新的评估前沿**：传统的、以任务完成度为导向的排行榜（如Arena）无法完全反映模型的类人性，尤其是在社交和情感维度。SAGE等新范式表明，在社交互动中表现优异的模型与在事实准确性上领先的模型并非同一批，这促使研究界开始重视对高阶社会认知能力的评估 [www.techwalker.com](https://www.techwalker.com/2025/0512/3166305.shtml)。

#### **4. 趋势与挑战**
基于2025年前后的研究动态，未来LLM类人性评估将呈现以下趋势并面临相应挑战：

1.  **从静态基准到动态、具身化的交互式评估**：评估范式正从分析离线文本转向在动态、多轮、甚至具身化的虚拟环境中测试AI代理的行为。如SocialBench所倡导的群体互动评估和SAGE框架中的情感动态追踪，都指向了更贴近真实社会场景的测试方法。**挑战**在于如何构建可扩展、可复现且足够复杂的交互环境，并定义合理的成功标准。

2.  **“智能体即评委”（Agent-as-Judge）范式的深化与标准化**：利用一个（或多个）AI代理来评估另一个AI代理的类人性，已成为一个极具潜力的方向。未来的趋势是赋予“评委”代理更复杂的内部状态（如情感、信念、记忆）和更明确的社会角色。**挑战**在于如何保证“评委”代理的公正性、稳定性和可解释性，避免产生评估偏差的“回音室效应”。

3.  **跨学科理论的深度融合与计算化**：心理学（尤其是心理测量学）、社会学和伦理学的理论正被更系统地用于定义和量化“类人性”的各个“构念”（constructs）。例如，将项目反应理论（IRT）用于AI能力评估，或使用善恶人格理论指导道德对齐。**挑战**在于如何将这些源于人类研究的抽象理论成功“翻译”为可计算、可验证的AI评估指标，并处理人与AI在认知基础上的本质差异。

4.  **对解释性与归因的更高要求**：未来的评估不仅要回答“模型有多像人”，更要回答“模型在哪些方面、因为什么机制而不像人”。这意味着评估框架需要与模型的可解释性研究更紧密地结合，例如通过追踪注意力或激活模式，将宏观的行为差异归因到具体的模型组件或训练数据子集上 [lonepatient.top](http://lonepatient.top/2025/10/06/arxiv_papers_2025-10-06 "Arxiv今日论文| 2025-10-06")。

#### **5. 结论**
在2022至2025年间，对AI聊天机器人和大型语言模型类人性的评估研究，已经从依赖主观判断的传统图灵测试，演进为以行为测试为核心的、结合了计算语言学、心理测量学和社会交互模拟的多元化科学体系。研究表明，尽管LLM在模仿人类语言方面取得了显著进展，但在情感表达、社会认知和道德推理等深层维度上，其行为模式与人类仍存在系统性差异。一个核心发现是，提升风格上的类人性往往以牺牲内容保真度为代价。
展望未来，该领域的研究将更加侧重于动态交互环境下的评估、智能体评测范式的完善以及与人类社会科学理论的深度融合。解决这些挑战不仅是衡量技术进步的标尺，更是确保AI以负责任、可信赖的方式融入人类社会的基石。

#### **6. 参考文献**
1.  Pagan, N., Törnberg, P., Bail, C. A., Hannák, A., & Barrie, C. (2025). *Computational Turing Test Reveals Systematic Differences Between Human and AI Language*. arXiv. [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/207138)
2.  Chen, H., Chen, H., Yan, M., Xu, W., Xing, G., Shen, W., ... & Huang, F. (2024). *SocialBench: Sociality Evaluation of Role-Playing Conversational Agents*. ACL 2024. [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/49871)
3.  Guo, Y., Dou, Z., Nguyen, H. H., Chang, C. C., Sugawara, S., & Echizen, I. (2025). *Measuring Human Involvement in AI-Generated Text: A Case Study on Academic Writing*. arXiv. [chatpaper.com](https://chatpaper.com/zh-CN/paper/145984)
4.  Li, Y., Huang, Y., Wang, H., Zhang, X., Zou, J., & Sun, L. (2024). *Quantifying AI Psychology: A Psychometrics Benchmark for Large Language Models*. arXiv. [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/f5ffe17f-f1f6-4ad3-b358-82204340be16)
5.  Zhang, B., Ma, R., et al. (2025). *Sentient Agent as a Judge: Evaluating High-Order Social Cognition in Large Language Models*. arXiv. [www.techwalker.com](https://www.techwalker.com/2025/0512/3166305.shtml)
6.  Jiao, L., Li, C. J., Chen, Z., Xu, H., & Xu, Y. (2025). 当 AI“具有”人格：善恶人格角色对大语言模型道德判断的影响. *心理学报, 57*(6), 929-946. [www.sciengine.com](https://www.sciengine.com/doi/pdfView/46CA0A58230E4B66B891FEEC247B789C)
7.  Song, G., et al. (2025). *Large Language Model Psychometrics: A Systematic Review of Evaluation, Validation, and Enhancement*. arXiv. Reported by [news.qq.com](https://news.qq.com/rain/a/20250527A04GXT00)
8.  Aliyun. (2025). *Evaluating, Synthesizing, and Enhancing Customer Support Conversations*. arXiv. [huggingface.ac.cn](https://huggingface.ac.cn/papers/2508.04423)
9.  Ren, M., Geng, Q., & Wu, Y. (2023). 聊天机器人评估研究综述：指标、方法与应用领域. *图书情报工作, 67*(22), 140-148. [www.lis.ac.cn](https://www.lis.ac.cn/CN/10.13266/j.issn.0252-3116.2023.22.014)
10. Zhou, C., Yang, C., Hu, Y., et al. (2025). *Coevolutionary Continuous Discrete Diffusion: Make Your Diffusion Language Model a Latent Reasoner*. arXiv. [lonepatient.top](http://lonepatient.top/2025/10/06/arxiv_papers_2025-10-06)
11. Mu, J., Zhang, Q., Wang, Z., et al. (2025). *Self-Reflective Generation at Test Time*. arXiv. [lonepatient.top](http://lonepatient.top/2025/10/06/arxiv_papers_2025-10-06)
12. Zhao, W. X., Zhou, K., Li, J., et al. (2023). *A survey of large language models*. arXiv. [www.sciengine.com](https://www.sciengine.com/doi/pdfView/46CA0A58230E4B66B891FEEC247B789C) (Cited within Jiao et al., 2025)
13. Jiang, H., Zhang, X., Cao, X., Breazeal, C., & Kabbara, J. (2023). *PersonaLLM: Investigating the ability of large language models to express personality traits*. arXiv. [www.sciengine.com](https://www.sciengine.com/doi/pdfView/46CA0A58230E4B66B891FEEC247B789C) (Cited within Jiao et al., 2025)