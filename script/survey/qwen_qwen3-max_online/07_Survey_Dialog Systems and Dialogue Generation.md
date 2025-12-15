# 对话系统与对话生成研究综述（2022–2025）

## 引言

对话系统（Dialog Systems）旨在实现自然、连贯且有上下文感知能力的人机交互，其核心任务——对话生成（Dialogue Generation）——近年来在大型语言模型（LLMs）驱动下取得显著进展。2022至2025年间，研究从早期基于检索或固定模板的方法，逐步转向知识融合、多模态理解、情感建模与主动规划等方向。本综述系统梳理该阶段代表性工作，聚焦于提升对话**连贯性、信息性、情感共鸣性与可控性**四大维度，覆盖开放域对话、任务导向对话及情感对话等子领域，并基于真实论文成果进行归纳，避免主观臆断。

## 方法分类与代表作

### 1. 知识增强的对话生成

大语言模型虽具备强大语言能力，但缺乏对领域特定或实时知识的利用能力。知识增强方法通过外部知识检索与融合机制弥补此缺陷。

Zhang 等（2025）提出 **KEDiT**，用于高效微调LLMs以支持知识引导对话。该方法首先通过信息瓶颈压缩检索知识为紧凑向量，再通过轻量级适配器（仅更新<2%参数）将知识注入LLM。在Wizard of Wikipedia和新构建的PubMed-Dialog数据集上，KEDiT在自动、LLM-based与人工评估中均显著优于基线，证明其在医学等专业领域生成信息丰富回复的有效性 [ir.dlut.edu.cn](https://ir.dlut.edu.cn/info/1005/2143.htm)。

李石君（2025）提出一种基于条件变分注意力的知识选择方法。该模型利用CVAE和多层注意力从冗余外部知识中筛选与对话最相关的片段，并将其注入BART模型进行微调。实验表明，该方法在生成多样性、连贯性与事实准确性上优于现有知识对话模型，有效缓解了知识噪声问题 [crad.ict.ac.cn](https://crad.ict.ac.cn/article/cstr/32373.14.issn1000-1239.202440551)。

### 2. 情感与价值观驱动的生成

情感共鸣是高质量对话的关键。近期工作从单纯情绪识别转向融合认知因素（如价值观）以实现更深层次的情感对齐。

马志强等（2025）提出 **HVDEGM**（人机价值观驱动的对话情绪生成模型），通过情境修正注意力、价值观融合与反应调节三个单元，动态融合用户与系统价值观以引导情绪生成。研究者构建了新数据集**ValueCon**，实验证明该模型在情绪共鸣度（R3）上较基线提升4.1%，尤其在“开心”、“愤怒”等与“友善”价值观强相关的情绪上表现突出 [aclanthology.org](https://aclanthology.org/2025.ccl-1.47.pdf)。

Koudounas 等（2025）发布 **DeepDialogue** 数据集，包含40,150个多轮、多领域、多情感的对话，并为每段对话合成带情感的语音。该数据集揭示：小模型在6轮后连贯性急剧下降；具体领域对话质量优于抽象领域；跨模型交互比同模型更连贯。这是首个大规模开源、情感连贯的多模态对话数据集，为情感语音对话研究奠定基础 [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/141469)。

### 3. 基于图结构与策略的学习

为提升多轮对话的长期连贯性与可控性，研究者引入图结构对对话流进行显式建模。

徐俊等（ACL 2020，但其思想在2022–2025年被广泛引用与发展）提出 **CG-Policy**，从对话语料构建对话图谱（Conversational Graph），其中节点为“What to say”（关键词）和“How to say”（表达方式）。策略模型通过图遍历主动规划内容，学习选择What/How节点指导生成。在Weibo和Persona数据集上，该框架在多轮连贯性与目标到达成功率上显著优于LaRL等基线 [blog.csdn.net](https://blog.csdn.net/qq_27590277/article/details/106935483)。

Li 等（2024）提出 **PCA**（Planning-based Conversational Agent）框架，利用LLM进行对话规划。在对话前，LLM离线生成标准操作流程（SOP）；对话中，在线规划最优行动路径。其变体PCA-M结合蒙特卡洛树搜索（MCTS），在控制性、主动性、任务成功率上优于CoT/ToT基线，且仅需任务与目标定义，无需大量人工标注 [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/b11159a0-8d36-4804-95a6-37ca32cf44be)。

### 4. 个性化与用户建模

对话系统正从通用响应向个性化生成演进，通过用户画像、行为或文档进行定制。

一项2025年的综述指出，个性化生成（PGen）已成为大模型时代的核心趋势，其统一框架包含用户建模（基于档案、行为、文档）与生成建模（通过提示工程、RAG、适配器等）。对话系统通过定义人设或学习用户交互模式，可生成符合个体偏好的响应 [zhuanzhi.ai](https://www.zhuanzhi.ai/vip/237af4595bfc0a500ba758a416758164)。早期工作如Zhou 等（2018）的ECM已引入情感记忆，而近期方法更强调**动态偏好跟踪**与**跨模态个性化**（如结合图像与文本）。

## 实验与评价总结

2022–2025年的实验评价呈现以下共性：

1.  **评估维度多元化**：除传统BLEU、Distinct等指标外，**人工评估**（相关性、连贯性、信息量）成为金标准；LLM-as-a-Judge（如GPT-4打分）被广泛用于自动评估；**任务完成率**、**多轮连贯性**、**情感共鸣度**（R3）、**价值观一致性**等任务特定指标被提出。
2.  **数据集专业化**：研究不再局限于通用语料（如DailyDialog），而是构建**领域特定**（如PubMed-Dialog）、**情感丰富**（如DeepDialogue）、**价值观标注**（如ValueCon）或**规划导向**（如PCA-D）的数据集，以支持细粒度评估。
3.  **基线模型演进**：基线从Seq2Seq、Transformer转向**大语言模型**（如ChatGPT、Llama、ERNIE 4.0）及其微调变体。模型对比不仅关注生成质量，更关注**参数效率**（如KEDiT仅微调2%参数）与**推理可控性**。
4.  **消融实验标准化**：对核心模块（如注意力、融合单元、规划机制）的消融成为验证方法有效性的必要步骤，揭示各组件对最终性能的具体贡献。

## 趋势与挑战

基于近期工作，2025年前后的研究趋势可预测为：

1.  **统一多模态理解与生成**：随着GPT-4o等模型出现，对话系统将整合文本、语音、图像甚至视频，实现真正的多模态交互。如何设计统一架构（如自回归vs扩散模型融合）以支持任意模态输入输出，是核心挑战 [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/134378)。
2.  **认知驱动的深度共情**：情感生成将超越情绪标签，深入**价值观、人格、信念**等认知层面。系统需具备推理用户潜在意图与情感根源的能力，并在价值观冲突时进行伦理权衡，而非简单模仿。
3.  **主动规划与工具使用**：对话系统将从被动响应转向主动规划，结合**LLM+MCTS**或**LLM+Agent**框架，调用外部工具（搜索、API、数据库）完成复杂任务，并在多轮中保持目标一致性与逻辑连贯性。

## 结论

2022–2025年，对话生成研究在知识融合、情感建模、策略学习与个性化方面取得实质性突破。核心驱动力是大语言模型的能力跃升与高质量、多维度数据集的构建。未来研究将聚焦于构建统一、认知深度、主动智能的对话代理，其挑战在于如何在提升能力的同时，确保系统的可信性（隐私、公平、安全）与评估的科学性。本综述所梳理的方法与趋势，为后续研究提供了清晰的技术路线图。

## 参考文献

1. Zhang, B. et al. (2025). Efficient Tuning of Large Language Models for Knowledge-Grounded Dialogue Generation. *Transactions of the Association for Computational Linguistics (TACL)*. [https://ir.dlut.edu.cn/info/1005/2143.htm](https://ir.dlut.edu.cn/info/1005/2143.htm)
2. 李石君. (2025). 基于变分注意力知识选择和预训练语言模型的对话生成. *计算机研究与发展*. [https://crad.ict.ac.cn/article/cstr/32373.14.issn1000-1239.202440551](https://crad.ict.ac.cn/article/cstr/32373.14.issn1000-1239.202440551)
3. Ma, Z. et al. (2025). Human-Machine Values-Driven Dialogue Emotion Generation Model. *Proceedings of CCL 2025*. [https://aclanthology.org/2025.ccl-1.47.pdf](https://aclanthology.org/2025.ccl-1.47.pdf)
4. Koudounas, A., La Quatra, M., & Baralis, E. (2025). DeepDialogue: A Multi-Turn Emotionally-Rich Spoken Dialogue Dataset. *arXiv preprint arXiv:2505.19978*. [https://chatpaper.com/zh-CN/chatpaper/paper/141469](https://chatpaper.com/zh-CN/chatpaper/paper/141469)
5. 徐俊, 王海峰, 等. (2020). Conversational Graph Grounded Policy Learning for Open-Domain Conversation Generation. *ACL*. [https://blog.csdn.net/qq_27590277/article/details/106935483](https://blog.csdn.net/qq_27590277/article/details/106935483)
6. Li, Z. et al. (2024). Planning with Large Language Models for Conversational Agents. *arXiv preprint*. [https://hub.baai.ac.cn/paper/b11159a0-8d36-4804-95a6-37ca32cf44be](https://hub.baai.ac.cn/paper/b11159a0-8d36-4804-95a6-37ca32cf44be)
7. Zhou, H. et al. (2018). Emotional Chatting Machine: Emotional Conversation Generation with Internal and External Memory. *AAAI*. 
8. Chen, Y. et al. (2022). CPED: A large-scale chinese personalized and emotional dialogue dataset for conversational AI. *arXiv preprint arXiv:2205.14727*.
9. Zhao, T., Xie, K., & Eskenazi, M. (2019). Rethinking action spaces for reinforcement learning in end-to-end dialog agents with latent variable models. *NAACL*.
10. Majumder, N. et al. (2019). Dialoguernn: An attentive rnn for emotion detection in conversations. *AAAI*.
11. Zhang, X. et al. (2025). Unified Multimodal Understanding and Generation Models: Advances, Challenges, and Opportunities. *arXiv preprint arXiv:2505.02567*. [https://chatpaper.com/chatpaper/zh-CN/paper/134378](https://chatpaper.com/chatpaper/zh-CN/paper/134378)
12. Personalized Generation In Large Model Era: A Survey. (2025). *arXiv preprint arXiv:2503.02614*. [https://www.zhuanzhi.ai/vip/237af4595bfc0a500ba758a416758164](https://www.zhuanzhi.ai/vip/237af4595bfc0a500ba758a416758164)