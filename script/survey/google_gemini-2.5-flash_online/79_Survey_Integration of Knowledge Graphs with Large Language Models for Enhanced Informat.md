好的，这是一篇关于“知识图谱与大型语言模型集成以增强信息检索与理解”的中文学术综述，涵盖2022-2025年的代表性工作。

---

## 知识图谱与大型语言模型集成以增强信息检索与理解研究综述

### 引言

近年来，大型语言模型（Large Language Models, LLMs）在自然语言处理（NLP）领域展现出惊人的能力，尤其是在文本生成、语义理解和对话交互等方面 [arocmag.cn](https://www.arocmag.cn/abs/2024.12.0532), [jos.org.cn](https://www.jos.org.cn/html/2025/9/7247.htm)。然而，LLMs也面临固有的局限性，如“幻觉”问题、知识时效性不足、可解释性差以及在复杂逻辑推理任务中的表现不佳 [arocmag.cn](https://www.arocmag.cn/abs/2024.12.0532), [themoonlight.io](https://www.themoonlight.io/zh/review/synergizing-knowledge-graphs-with-large-language-models-a-comprehensive-review-and-future-prospects), [zhuanzhi.ai](https://zhuanzhi.ai/vip/aff53ce0dec658f93190865e2d58d7b8?from=doc_carousel_rec)。知识图谱（Knowledge Graphs, KGs）作为结构化的语义网络，能够以事实三元组的形式存储海量事实知识，为实体-关系推理和知识校验提供了强有力的支持，从而有望弥补LLMs的上述不足 [arocmag.cn](https://www.arocmag.cn/abs/2024.12.0532), [themoonlight.io](https://www.themoonlight.io/zh/review/synergizing-knowledge-graphs-with-large-language-models-a-comprehensive-review-and-future-prospects)。因此，将LLMs与KGs进行有效集成，已成为当前人工智能领域的研究热点，旨在构建更可靠、更智能的信息检索和理解系统 [163.com](https://www.163.com/dy/article/K17KRLBF05118UGF.html)。

本综述旨在系统梳理2022年至2025年间，LLMs与KGs集成以增强信息检索与理解的代表性工作。我们将根据知识图谱在与LLM结合时所扮演的不同角色，对现有方法进行分类，并总结其核心技术、关键实验结论及未来发展趋势。

### 方法分类与代表作

LLMs与KGs的集成方法根据KGs在LLMs中的作用可以大致分为以下几类：知识图谱作为LLMs的增强、LLMs作为知识图谱的增强，以及两者协同工作 [themoonlight.io](https://www.themoonlight.io/zh/review/synergizing-knowledge-graphs-with-large-language-models-a-comprehennsive-review-and-future-prospects)。

#### 1. 知识图谱增强大型语言模型 (KG-Enhanced LLMs)

这类方法主要利用KGs为LLMs提供结构化知识支撑，以提升其知识准确性、减少幻觉、增强可解释性及推理能力。

*   **注入结构化知识进行预训练与微调**
    研究问题：传统LLMs在常识性知识和领域特定知识方面存在局限，且易产生幻觉，如何有效将KGs中的结构化知识注入LLMs以提升其性能？
    核心方法：**Cao Rongrong et al. (2025)** [arocmag.cn](https://www.arocmag.cn/abs/2024.12.0532)系统梳理了将KGs融入LLMs的技术路线，从预训练、模型架构改造和微调优化三个阶段分析了代表性方法。他们指出，通过将KGs中的事实知识直接注入LLM的预训练或微调阶段，可以为模型提供强有力的知识约束。
    关键实验结论：深度融合KGs显著提升了LLMs生成内容的事实一致性，有效缓解了幻觉问题，并增强了模型在垂直领域应用中的可控性。

*   **检索增强生成 (Retrieval-Augmented Generation, RAG) 与图检索增强生成 (Graph RAG)**
    研究问题：LLMs的知识存在截止日期，且容易生成不符合事实的“幻觉”内容，如何通过外部知识检索来增强LLMs的最新知识和事实准确性？
    核心方法：**Derong Xu et al. (2025)** [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/94455) 提出了一种自适应多方面检索增强知识图谱（Adaptive Multi-Aspect Retrieval-Augmentation, Amar）框架，旨在通过检索包括实体、关系和子图在内的知识来帮助LLMs进行复杂知识推理和答案预测。他们通过自对齐模块增强检索文本以减少噪声，并通过相关性门控模块学习问题与多方面检索数据的相关性评分。
    关键实验结论：Amar框架在WebQSP和CWQ等数据集上取得了先进的性能，相比最佳竞争对手提高了1.9%的准确率，并在逻辑形式生成上比直接使用检索文本的方法提高了6.6%，表明其在提升LLMs推理能力方面的有效性。
    **Ma Jie et al. (2025)** [jos.org.cn](https://www.jos.org.cn/html/2025/9/7247.htm) 提出了基于相关性提示的知识图谱问答方法，旨在解决现有RAG方法在垂直领域引入无关噪声知识导致LLMs回答准确率下降的问题。他们引入了“检索-相关性评估-问答”框架，通过额外训练相关性计算模型量化检索到的知识图谱三元组与问题的相关性，并将其作为prompt的一部分输入LLM，引导LLM选择合理知识。
    关键实验结论：该方法在机械制造和航空航天领域的问答任务上，相对于基线模型显著提升了LLM的Score和Accuracy，说明相关性提示有效帮助模型利用证据三元组，提高回答准确性，并有效提升用户满意度。

*   **知识图谱作为推理指南与验证器**
    研究问题：LLMs在多跳推理和答案事实性验证方面存在不足，如何利用KGs的结构化特性引导LLMs进行更准确的推理并验证其生成结果？
    核心方法：**Wang C. et al. (2025)** 探讨了LLMs遇上知识图谱的问答系统，将KGs在与LLM结合时所扮演的角色分为背景知识、推理指南和验证者和优化器 [163.com](https://www.163.com/dy/article/K17KRLBF05118UGF.html)。作为推理指南，KGs可以在LLM推理前提供潜在路径或子图，或直接参与LLM的推理过程。作为验证者，KGs可以帮助LLM验证和细化中间答案，过滤不准确信息。
    关键实验结论：通过图归纳（Graph-based Induction）或知识聚合模块（Knowledge Aggregation Module），LLM在处理复杂多跳问题时能够生成更精确的答案并提供可解释的推理路径，减轻了LLM的“幻觉”问题。

#### 2. 大型语言模型增强知识图谱 (LLM-Enhanced KGs)

这类方法主要利用LLMs强大的文本理解和生成能力，自动化或半自动化地执行知识图谱构建、补全、更新和查询扩展等任务。

*   **知识图谱构建与补全**
    研究问题：传统KGs构建通常依赖大量人工，成本高昂且效率低下，如何利用LLMs自动化从非结构化文本中抽取实体、关系和事件以构建或更新KGs。
    核心方法：**Jian Zhang et al. (2025)** [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/120739) 提出了一个统一的通用知识图谱（Generalized Knowledge Graph, GKG）构建框架GKG-LLM，能够同时构建知识图谱、事件知识图谱和常识知识图谱。他们通过课程学习微调框架，迭代地将三种类型图谱的知识注入LLMs中。
    关键实验结论：GKG-LLM在样本内、分布外（OOD）和对抗任务数据上均改善了所有三种图谱的构建，克服了任务特定差异带来的挑战，展示了LLMs在统一且自动化KGs构建方面的潜力。
    **themoonlight.io (2025)** 提及LLMs在KG构建过程中扮演至关重要的角色，尤其在实体抽取、实体解析和匹配以及链接预测等方面发挥优势 [themoonlight.io](https://www.themoonlight.io/zh/review/synergizing-knowledge-graphs-with-large-language-models-a-comprehensive-review-and-future-prospects)。通过提示工程（prompt engineering）等技术，LLMs可以有效地应用于关系知识的检索和图谱补全。
    关键实验结论：LLMs的语义理解和关系推断能力显著提升了KG构建的自动化程度和效率，减少了人工标注成本。

*   **知识图谱查询扩展**
    研究问题：用户查询的表达往往不完整或模糊，如何利用LLMs对查询进行扩展以提升信息检索的准确性和召回率？
    核心方法：**themoonlight.io (2025)** 描述了一项研究，提出一种知识驱动的查询扩展框架，通过引入知识图（KG）中的结构化文档关系来增强LLM的能力 [themoonlight.io](https://www.themoonlight.io/zh/review/knowledge-aware-query-expansion-with-large-language-models-for-textual-and-relational-retrieval)。该方法包括实体解析、文档检索、KG关系传播、文档基础的关系过滤和构建知识三元组，最终将知识三元组与原始查询一起输入LLM生成扩展查询。
    关键实验结论：该框架在产品检索、学术论文检索和生物医学检索等领域表现优越，显著改善了文本和关系半结构化检索中查询效果，尤其是在处理复杂查询要求时提供了更准确的结果。

#### 3. 知识图谱与大型语言模型协同框架 (Synergetic LLM-KG Frameworks)

这类方法强调LLMs和KGs之间的双向交互和迭代优化，旨在构建一个统一的、知识驱动的智能系统。

*   **跨域异质数据查询**
    研究问题：实际场景中数据来源多样且存在隐私安全问题，导致跨域异质数据难以集中共享和高效利用，如何构建LLM与KG协同的框架以实现高效可信的跨域数据查询？
    核心方法：**李博涵 et al. (2025)** [crad.ict.ac.cn](https://crad.ict.ac.cn/cn/article/Y2025/I3/605) 提出了一种LLM和知识图谱（KG）协同的跨域异质数据查询框架。该方法首先采用适配器融合数据并构建相应的知识图谱，引入线性知识图和同源知识图抽取算法（HKGE）重构图谱以提高查询效率。为保证高可信度，提出可信候选子图匹配算法（TrustHKGM）检验数据置信度并剔除低质量节点，最终通过基于线性知识图提示的多域数据查询算法（MKLGP）实现高效可信跨域查询。
    关键实验结论：在多个真实数据集上的实验验证了所提方法的有效性和高效性，显著提升了LLM在多场景跨域异质数据查询中的性能与可信度。

*   **多模态知识图谱与LLMs的集成**
    研究问题：当前的KGs主要依赖文本和图形结构，而LLMs在处理多模态数据方面能力提升，如何构建多模态KGs并与LLMs有效集成？
    核心方法：**themoonlight.io (2025)** 预测未来研究将更多探讨构建多模态KGs，以应对LLMs在处理多模态数据方面的提升 [themoonlight.io](https://www.themoonlight.io/zh/review/synergizing-knowledge-graphs-with-large-language-models-a-comprehensive-review-and-future-prospects)。
    **专知.ai (2024)** [zhuanzhi.ai](https://zhuanzhi.ai/vip/aff53ce0dec658f93190865e2d58d7b8?from=doc_carousel_rec) 提及多模态问答系统，如VQA，其研究MMJG（Wang et al., 2022）引入自适应知识选择机制，从视觉和文本知识中联合选择信息。RAMQA（Bai et al., 2025）通过多任务学习方式增强多模态检索增强问答系统。KVQA（Dong et al., 2024）通过两阶段提示和伪孪生图谱媒介融合来平衡模态内和模态间推理。
    关键实验结论：这些研究展示了多模态知识图谱在整合不同模态信息方面的潜力，并能有效提升LLMs在多模态问答任务中的表现，为更复杂、更接近人类感知的信息处理奠定基础。

### 实验与评价总结

现有研究在评估LLMs与KGs集成系统时，通常采用以下几类指标：

1.  **答案质量指标**：包括BERTScore、答案相关性、幻觉度、准确性匹配及人工验证完整性等，用以衡量生成答案的质量和事实准确性 [zhuanzhi.ai](https://zhuanzhi.ai/vip/aff53ce0dec658f93190865e2d58d7b8?from=doc_carousel_rec)。许多工作采用LLM-Score和Accuracy等指标，通过与基线模型对比，验证集成方法在提升LLM回答准确性方面的有效性 [jos.org.cn](https://www.jos.org.cn/html/2025/9/7247.htm)。
2.  **检索质量指标**：评估检索到的知识片段与问题或任务的相关性，包括上下文相关性、忠实度得分、精确度、上下文召回率、平均倒数排名和标准化折扣累积增益等 [zhuanzhi.ai](https://zhuanzhi.ai/vip/aff53ce0dec658d7b8?from=doc_carousel_rec)。这些指标衡量KG在为LLM提供外部知识时的效率和质量。
3.  **推理质量指标**：如跳跃准确率和推理准确率，用于评估系统在复杂逻辑推理任务中的表现，尤其是多跳推理能力 [zhuanzhi.ai](https://zhuanzhi.ai/vip/aff53ce0dec658d7b8?from=doc_carousel_rec), [jos.org.cn](https://www.jos.org.cn/html/2025/9/7247.htm)。

常用的基准数据集包括WebQSP、BioASQ-QA、CAQA、CR-LT KGQA、EXAQT、Mecha-QA和Aero-QA等，涵盖了知识库问答、多选题问答、多跳问答、多模态问答和时间问答等多种任务类型 [jos.org.cn](https://www.jos.org.cn/html/2025/9/7247.htm), [zhuanzhi.ai](https://zhuanzhi.ai/vip/aff53ce0dec658d7b8?from=doc_carousel_rec)。
总体而言，实验结果普遍表明，LLMs与KGs的集成方法在提高信息检索和理解的准确性、鲁棒性、可解释性和事实一致性方面，均展现出超越单一LLMs或KGs的性能。尤其是在垂直领域或知识密集型任务中，这种结合能有效缓解LLMs的“幻觉”问题、知识截止问题及推理能力不足等缺陷 [jos.org.cn](https://www.jos.org.cn/html/2025/9/7247.htm), [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/94455)。

### 趋势与挑战

2025年前后，LLMs与KGs集成领域的研究呈现以下趋势和面临的挑战：

1.  **多模态KGs的深入融合与跨模态对齐**：随着LLMs处理多模态能力增强，未来将更关注构建多模态KGs [themoonlight.io](https://www.themoonlight.io/zh/review/synergizing-knowledge-graphs-with-large-language-models-a-comprehensive-review-and-future-prospects)。挑战在于如何实现不同模态知识的有效抽取、表示融合与语义对齐，以及在复杂多模态推理任务中的应用。
2.  **动态知识更新与增量式融合**：KGs的知识更新滞后性与LLMs的知识截止问题是重要瓶颈 [arocmag.cn](https://www.arocmag.cn/abs/2024.12.0532)。未来的研究将侧重开发轻量化、增量式的融合机制，使LLMs能够动态感知并整合KG的最新知识，而非仅限于静态知识快照。这可能涉及实时KG更新、自适应知识融合策略等。
3.  **可解释性与信任构建**：尽管KGs能增强LLMs的可解释性，但当前集成机制仍多为“黑盒”模型 [themoonlight.io](https://www.themoonlight.io/zh/review/synergizing-knowledge-graphs-with-large-language-models-a-comprehensive-review-and-future-prospects), [zhuanzhi.ai](https://zhuanzhi.ai/vip/aff53ce0dec658f93190865e2d58d7b8?from=doc_carousel_rec)。未来的研究将探索更透明、可追溯的集成框架，使用户不仅知道“什么”是答案，还能理解“为什么”是这个答案，尤其是在关键决策和垂直领域应用中。
4.  **自主知识发现与推理能力提升**：现有系统在很大程度上依赖预构建的KGs和既定的推理模式。未来趋势是赋予LLMs结合KGs进行自主知识发现和更复杂的推理能力，例如通过链式推理、辩证交互等方式，实现更深层次的语义理解和新知识生成。
5.  **高效性与计算成本优化**：LLMs与KGs的结合常伴随较高的计算资源消耗。未来研究将寻求优化技术，如基于索引、提示和成本的优化，以减少LLM调用次数、加速知识检索，实现更具成本效益的问答能力 [163.com](https://www.163.com/dy/article/K17KRLBF05118UGF.html)。

### 结论

LLMs与KGs的集成代表了人工智能发展的一个重要方向，它弥补了两种技术的固有缺陷，并为构建更强大、更可靠的信息检索和理解系统提供了新的范式。通过将结构化知识与强大的语言处理能力相结合，研究取得了显著进展，尤其是在提升事实准确性、可解释性和领域适应性方面。然而，多模态知识的融合、动态知识更新、可解释性构建、推理能力提升以及计算效率优化等挑战依然存在。未来的研究将需要跨学科的持续努力，以突破这些技术瓶颈，最终实现知识与语言协同驱动的智能系统，从而推动人工智能在更广泛的应用场景中发挥其潜力。

### 参考文献

*   [arocmag.cn](https://www.arocmag.cn/abs/2024.12.0532) 曹荣荣, 柳林, 于艳东, 王海龙. 融合知识图谱的大语言模型研究综述. 计算机应用研究, 2025, 42(8): 2255-2266.
*   [themoonlight.io](https://www.themoonlight.io/zh/review/synergizing-knowledge-graphs-with-large-language-models-a-comprehensive-review-and-future-prospects) Synergizing Knowledge Graphs with Large Language Models: A Comprehensive Review and Future Prospects. (Reviewed on 2025-03-22).
*   [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/94455) Xu, D., Li, X., Zhang, Z., Lin, Z., Zhu, Z., Zheng, Z., Wu, X., Zhao, X., Xu, T., & Chen, E. Harnessing Large Language Models for Knowledge Graph Question Answering via Adaptive Multi-Aspect Retrieval-Augmentation. arXiv preprint arXiv:2412.18537, 2024.
*   [crad.ict.ac.cn](https://crad.ict.ac.cn/cn/article/Y2025/I3/605) 吴文隆, 尹海莲, 王宁, 徐梦飞, 赵鑫喆, 殷崭祚, 刘元睿, 王昊奋, 丁岩, 李博涵. 大语言模型和知识图谱协同的跨域异质数据查询框架. 计算机研究与发展, 2025, 62(3): 605-620.
*   [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/120739) Zhang, J., Wei, B., Qi, S., Zhu, H., Liu, J., & Lin, Q. GKG-LLM: A Unified Framework for Generalized Knowledge Graph Construction. arXiv preprint arXiv:2503.11227, 2025.
*   [themoonlight.io](https://www.themoonlight.io/zh/review/knowledge-aware-query-expansion-with-large-language-models-for-textual-and-relational-retrieval) Knowledge-Aware Query Expansion with Large Language Models for Textual and Relational Retrieval. (Reviewed on 2025-03-22).
*   [jos.org.cn](https://www.jos.org.cn/html/2025/9/7247.htm) 马杰, 孙望淳, 王平辉, 张若非, 李帅鹏, 苏洲. 基于相关性提示的知识图谱问答. 软件学报, 2025, 36(9): 4056-4071.
*   [163.com](https://www.163.com/dy/article/K17KRLBF05118UGF.html) 马传涛, 汗 A. 大语言模型与知识图谱强强联手：问答系统的完美协作与未来机遇. 至顶头条 (网易号), 2025-06-04.
*   [zhuanzhi.ai](https://zhuanzhi.ai/vip/aff53ce0dec658f93190865e2d58d7b8?from=doc_carousel_rec) 大型语言模型遇上知识图谱：问答系统中的融合与机遇. 专知VIP, 2024-01-01.