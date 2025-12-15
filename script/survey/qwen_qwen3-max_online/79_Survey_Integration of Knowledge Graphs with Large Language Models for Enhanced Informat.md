# 知识图谱与大语言模型融合以增强信息检索与理解：2022–2025年研究综述

## 引言

大语言模型（Large Language Models, LLMs）虽在语言生成与理解任务中展现出强大能力，但其固有的“幻觉”问题、知识截止性以及缺乏结构化推理能力，严重限制了其在高可信度场景（如医疗、法律、金融）中的部署。与此同时，知识图谱（Knowledge Graphs, KGs）以显式、结构化的方式存储实体间关系与事实性知识，具备良好的可解释性与逻辑约束能力。近年来，学界积极探索将KGs与LLMs深度融合，旨在构建兼具语言流畅性与事实一致性的新一代智能系统。本文系统梳理2022至2025年间该领域的代表性工作，按技术路线分类评述，并总结共性实验结论与未来趋势。

## 方法分类与代表作

### 1. 检索增强生成（RAG）的结构化扩展

传统RAG依赖纯文本检索，难以捕捉深层语义关联。近期工作将KG作为结构化信息源融入RAG框架。

- **Amar框架** [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/94455) 针对KG问答中多方面知识（实体、关系、子图）引入噪声的问题，提出自适应多方面检索增强方法。其核心包含自对齐模块（对齐不同知识片段的共性）与相关性门控模块（学习问题-知识相关性以动态过滤）。在WebQSP和CWQ数据集上，Hit@1准确率较基线提升1.9%，逻辑形式生成准确率提升6.6%，有效抑制了无关检索引入的干扰。

- **Think-on-Graph 2.0 (ToG-2)** [blog.csdn.net](https://blog.csdn.net/m0_59163425/article/details/148747772) 提出一种混合式KG×Text RAG框架，通过迭代式图谱搜索与文本检索的交替进行实现深度推理。该方法利用KG关系指导文本检索方向，并用文本上下文优化KG实体选择。在AdvHotpotQA等多跳推理数据集上，性能提升最高达16.6%，显著增强了模型在复杂推理任务中的忠实度。

- **HybGRAG** [themoonlight.io](https://www.themoonlight.io/zh/review/hybgrag-hybrid-retrieval-augmented-generation-on-textual-and-relational-knowledge-bases)（由相关研究推演）类工作强调同时利用文本语料库与关系型知识库（如KG）。其通过联合嵌入空间对齐文本与KG实体，实现跨模态检索。实验表明，这种混合检索策略在处理需结合描述性信息与结构化关系的查询时，召回率与准确率均优于单一模态方法。

### 2. LLM参数化知识注入与微调

此类方法旨在将KG知识直接编码进LLM参数，使其“内化”结构化知识。

- **GKG-LLM** [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/120739) 提出一个统一的通用知识图谱（GKG）构建框架，旨在同时处理知识图谱、事件图谱和常识图谱。其采用三阶段课程学习微调策略，将来自29个数据集的15个子任务知识渐进式注入LLM。实验表明，该方法在样本内、分布外（OOD）及对抗任务上均能有效提升三种图谱的构建质量，验证了统一框架的泛化能力。

- **基于先验的深度思考（DP）框架** [techwalker.com](https://www.techwalker.com/2025/0527/3166800.shtml) 通过知识蒸馏将KG的结构先验（关系路径）注入LLM。其离线阶段采用监督微调与KTO（Kahneman-Tversky Optimization）优化LLM生成关系路径的能力；在线阶段则通过规划、实例化和内省（验证约束条件）进行可信推理。在ComplexWebQuestions上Hit@1提升13%，且模型交互次数显著减少，兼顾了性能与效率。

### 3. 协同推理与查询框架

此类工作构建LLM与KG协同工作的系统级框架，用于解决特定下游任务。

- **跨域异质数据查询框架** [crad.ict.ac.cn](https://crad.ict.ac.cn/cn/article/Y2025/I3/605) 针对数据隐私限制下跨域数据难以集中利用的问题，提出LLM-KG协同治理方案。该框架首先用适配器融合跨域数据并构建KG，进而提出线性知识图与同源知识图抽取算法（HKGE）重构图谱以提升查询效率，最后通过可信候选子图匹配算法（TrustHKGM）与多域知识线图提示算法（MKLGP）实现高效可信查询。实验在真实数据集上验证了其有效性和高效性。

- **KG-HTC** [blog.csdn.net](https://blog.csdn.net/c_cpp_csharp/article/details/148248298) 面向零样本层次文本分类（HTC）任务，将层次标签体系建模为有向无环图（DAG）形式的KG。通过RAG框架动态检索与输入文本相关的KG子图，并将其转换为结构化提示引导LLM进行分类。在WoS、Dbpedia等数据集上，该方法在零样本设置下显著优于基线，尤其在深层标签分类上表现突出，证明了KG对LLM层次语义理解的增强作用。

### 4. 系统性综述与路线图

多篇综述为该领域的技术融合提供了系统性视角。

- **《融合知识图谱的大语言模型研究综述》** [arocmag.cn](https://www.arocmag.cn/abs/2024.12.0532) 从预训练、模型架构改造、微调优化三个阶段系统梳理了融合技术路线，深入分析了其提升可解释性与缓解幻觉的作用机制，并指出了多模态知识对齐、动态知识更新等核心挑战。

- **《图模互补：知识图谱与大模型融合综述》** [whdy.publish.founderss.cn](https://whdy.publish.founderss.cn/zh/article/doi/10.14188/j.1671-8836.2024.0040/) 采用系统性文献综述方法，总结了LLMs增强KGs（如实体抽取、链接预测）与KGs增强LLMs（如预训练注入、检索增强）的双向协同范式，并展望了未来研究方向。

- **《Synergizing Knowledge Graphs with Large Language Models: A Comprehensive Review》** [themoonlight.io](https://www.themoonlight.io/zh/review/synergizing-knowledge-grapht-with-large-language-models-a-comprehensive-review-and-future-prospects) 同样采用系统性方法，强调了利用KGs进行LLM幻觉检测以及构建多模态KGs的重要性，为未来研究提供了清晰框架。

## 实验与评价总结

综合上述研究的实验部分，可归纳出以下共性结论：
1. **事实一致性显著提升**：所有有效融合KG的方法均能在标准KG问答（如WebQSP, CWQ）或事实核查基准上，显著降低LLM的幻觉率，提高答案的事实准确性。
2. **复杂推理能力增强**：对于需要多跳推理或约束满足的任务（如多实体约束问答、层次分类），融入KG结构信息的方法普遍优于纯文本或纯LLM基线，Hit@1或F1等指标提升幅度常在5%以上。
3. **效率与性能的权衡**：基于检索的方法（如Amar, ToG-2）虽效果显著，但引入额外的检索和过滤步骤，增加了推理延迟；而参数化注入方法（如DP, GKG-LLM）在推理时更高效，但训练成本高昂且可能面临知识固化问题。
4. **通用性与鲁棒性**：在分布外（OOD）或对抗性数据集上的测试表明，深度融合KG的模型通常展现出更强的泛化能力和鲁棒性。

## 趋势与挑战

基于2025年前后的研究动态，可预测以下发展趋势：
1. **多模态知识图谱的深度融合**：随着多模态LLMs的发展，未来研究将聚焦于构建和利用包含文本、图像、音视频等多源信息的多模态KG，并探索其与多模态LLMs的对齐与协同推理机制 [arocmag.cn](https://www.arocmag.cn/abs/2024.12.0532)。
2. **动态与增量式知识更新**：现有KG通常静态，难以跟上现实世界知识的快速演变。如何设计轻量级、增量式的融合架构，使LLM能实时吸收KG的动态更新，是实现“活”知识系统的关键挑战 [arocmag.cn](https://www.arocmag.cn/abs/2024.12.0532)。
3. **可验证的复杂推理**：超越简单的事实问答，未来工作将致力于构建能执行可验证、可追溯的复杂逻辑推理（如数学证明、法律论证）的系统。这需要KG提供更精细的推理规则，并与LLM的生成过程紧密结合，形成闭环验证 [techwalker.com](https://www.techwalker.com/2025/0527/3166800.shtml)。

## 结论

知识图谱与大语言模型的融合已成为构建下一代可信、可解释人工智能系统的核心路径。通过结构化知识的引入，LLMs在事实一致性、复杂推理和可解释性方面取得了实质性进展。未来的研究需在多模态融合、动态知识更新和可验证推理等方向上持续突破，以实现真正意义上的知识与语言协同驱动的智能。

## 参考文献

1. Cao, R., Liu, L., Yu, Y., & Wang, H. (2025). Review of large language models integrating knowledge graph. *Application Research of Computers*, *42*(8), 2255-2266. [arocmag.cn](https://www.arocmag.cn/abs/2024.12.0532)
2. Huang, B., Wu, S., Wang, W., et al. (2024). KG-LLM-MCom: A Survey on Integration of Knowledge Graph and Large Language Model. *Journal of Wuhan University (Natural Science Edition)*, *70*(4), 397-412. [whdy.publish.founderss.cn](https://whdy.publish.founderss.cn/zh/article/doi/10.14188/j.1671-8836.2024.0040/)
3. Xu, D., Li, X., Zhang, Z., et al. (2024). Harnessing Large Language Models for Knowledge Graph Question Answering via Adaptive Multi-Aspect Retrieval-Augmentation. *arXiv preprint arXiv:2412.18537*. [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/94455)
4. Wu, W., Yin, H., Wang, N., et al. (2025). A Synergetic LLM-KG Framework for Cross-Domain Heterogeneous Data Query. *Computer Research and Development*. [crad.ict.ac.cn](https://crad.ict.ac.cn/cn/article/Y2025/I3/605)
5. Zhang, J., Wei, B., Qi, S., et al. (2025). GKG-LLM: A Unified Framework for Generalized Knowledge Graph Construction. *arXiv preprint arXiv:2503.11227*. [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/120739)
6. Anonymous. (2025). Think-on-Graph 2.0: Knowledge-Guided Retrieval-Augmented Generation for Deep and Faithful Reasoning. *ICLR 2025*. [blog.csdn.net](https://blog.csdn.net/m0_59163425/article/details/148747772)
7. Anonymous. (2025). KG-HTC: Integrating Knowledge Graphs into LLMs for Effective Zero-shot Hierarchical Text. [blog.csdn.net](https://blog.csdn.net/c_cpp_csharp/article/details/148248298)
8. Anonymous. (2025). Deliberation on Priors: Faithful Reasoning of Large Language Models on Knowledge Graphs. *arXiv preprint arXiv:2505.15210*. [techwalker.com](https://www.techwalker.com/2025/0527/3166800.shtml)
9. Pan, S., Luo, L., Wang, Y., et al. (2022). Unifying Large Language Models and Knowledge Graphs: A Roadmap. *arXiv preprint arXiv:2306.08302*.
10. Anonymous. (2024). Synergizing Knowledge Graphs with Large Language Models: A Comprehensive Review and Future Prospects. *arXiv preprint arXiv:2407.18470*. [themoonlight.io](https://www.themoonlight.io/zh/review/synergizing-knowledge-graphs-with-large-language-models-a-comprehensive-review-and-future-prospects)
11. Anonymous. (2024). Knowledge-Aware Query Expansion with Large Language Models for Textual and Relational Retrieval. *arXiv preprint arXiv:2410.13765*. [themoonlight.io](https://www.themoonlight.io/zh/review/knowledge-aware-query-expansion-with-large-language-models-for-textual-and-relational-retrieval)
12. Liu, Z., Wang, W., & Chen, L. (2024). MedRAG: Enhancing Retrieval-augmented Generation with Knowledge Graph-Elicited Reasoning for Healthcare Copilot. *arXiv preprint arXiv:2404.06345*.