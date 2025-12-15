# 生成式人工智能在临床文档系统中的研究综述（2022–2025）

## 引言

临床文档的生成与维护长期占据医生大量工作时间，是医疗效率提升的关键瓶颈。生成式人工智能（Generative AI），特别是大语言模型（Large Language Models, LLMs），自2022年起在该领域展现出变革性潜力。其核心价值在于将非结构化医患对话、电子健康记录（EHR）等多模态数据，转化为符合医学规范、结构清晰的正式文档。本文聚焦2022至2025年间的真实研究，系统梳理生成式AI在临床文档系统中的方法分类、核心代表工作、评价范式，并展望未来趋势。

## 方法分类与代表作

### 1. 基于对话转录的门诊病历生成  
该方法直接处理医患对话语音或文本，旨在自动化生成门诊病历。

*   **Lyu et al. (2023)** 提出利用ChatGPT将放射学报告转化为通俗语言，其核心方法是通过少量示例（few-shot）提示（prompt）引导模型。实验表明，该方法在信息保真度和可读性上获得放射科医生4.27/5的高分，证实了LLM作为患者-医生沟通媒介的可行性 [slyyx.whuznhmedj.com](https://slyyx.whuznhmedj.com/journal/254.html)。
*   **安徽医科大学第一附属医院团队 (2025)** 开发了基于讯飞星火X1和DeepSeek 70B的病历生成系统，采用专用语音设备实时捕捉门诊对话，并结合关键事件轴与迭代优化技术。试点应用显示，其生成病历合理率超83%，平均每日为医生节省2.8小时书写时间，验证了端到端解决方案的临床价值 [cn-healthcare.com](https://www.cn-healthcare.com/articlewm/20250604/content-1651301.html)。

### 2. 面向影像报告的自动化生成  
该方向聚焦于从医学影像（如CT、X光）及其初步分析中生成结构化报告。

*   **钱乾等 (2025)** 提出判别增强的多模态大语言模型微调方法MedVLM，用于肺部CT影像报告生成。该方法将影像诊断作为判别目标，结合低秩自适应（LoRA）等技术微调模型，使生成报告的肺炎诊断准确率达到87.67%，显著超越传统图像描述方法 [arocmag.cn](https://www.arocmag.cn/abs/2024.08.0303)。
*   **Hu et al. (2024)** 评估了ChatGPT在从放射学报告中零样本（zero-shot）提取结构化信息（如肿瘤位置、尺寸）的能力。研究发现，通过在提示中加入相关医学知识，可显著提升简单信息提取任务的性能，但在处理肿瘤密度等复杂任务时仍有局限 [slyyx.whuznhmedj.com](https://slyyx.whuznhmedj.com/journal/254.html)。

### 3. 检索增强生成（RAG）与知识融合  
为解决LLM的“幻觉”和知识过时问题，RAG框架被引入临床文档生成，通过实时检索外部权威知识库来增强生成内容。

*   **金哲等 (2025)** 系统综述了RAG技术在医学AI中的应用，指出其通过连接文献库、知识图谱等外部信息源，能有效解决医学场景对高准确度与可追溯性的需求。研究强调，RAG在新药研发、药物警戒和临床决策支持系统（CDSS）中已展现出关键作用 [ywlxbx.whuznhmedj.com](https://ywlxbx.whuznhmedj.com/journal/481.html)。
*   **Liu et al. (2025)** 在《Nature Medicine》发表的通用医学语言模型工作，展示了通过接入专业医学知识库（如UpToDate、PubMed）的增强框架，可在疾病诊断辅助任务上达到专家水平，其核心在于构建了高质量的医学领域检索-生成管道 [ablesci.com](https://www.ablesci.com/scholar/paper?id=3NVkRpjW3)。

### 4. 针对特定疾病领域的个性化健康文档  
此方法将生成式AI应用于慢性病等需长期管理的场景，提供个性化健康计划与文档。

*   **吴天星等 (2025)** 构建了基于“蜻蜓”大模型的重大慢病健康管理信息系统。该系统通过整合慢病知识、中国饮食文化等特定领域数据进行训练，并引入工具增强（如调用计算器处理数值）和基于不确定性知识图谱的RAG技术，显著提升了在健康管理对话中的表现 [crad.ict.ac.cn](https://crad.ict.ac.cn/article/doi/10.7544/issn1000-1239.202440570?viewType=HTML)。

## 实验与评价总结

现有研究的评价体系呈现多维度、多主体的特点。**自动化指标**如BLEU、ROUGE、METEOR等常用于衡量生成文本与参考文本的表面相似性，但其与临床效用的相关性有限。**人工评估**已成为金标准，通常由领域专家（如医生、放射科医师）从**临床准确性**、**信息完整性**、**术语规范性**、**可读性**和**安全性**（无有害幻觉）等维度进行打分。**用户研究**则关注系统对**临床工作流的影响**，核心指标包括**医生时间节省**、**文档采纳率**（如安医大一附院80%的引用率）和**用户满意度**。共性结论表明，最先进的系统在结构化良好、信息明确的任务（如门诊主诉、影像报告）上已达到可用水平，但在处理复杂、模糊或需深度推理的临床情境时，其可靠性仍是部署的主要障碍。

## 趋势与挑战

展望2025年及以后，该领域将呈现三大趋势：  
1.  **多模态深度协同**：未来的系统将不再局限于文本或单一模态，而是深度融合语音、文本、医学影像、基因组数据等多源信息，构建统一的临床理解与生成框架。  
2.  **可验证与可解释生成**：为解决“幻觉”这一核心挑战，研究将从单纯的RAG转向更精细的“生成-验证”闭环，通过引入独立的事实核查模块和可视化推理路径，确保每一条生成内容都有据可查、逻辑可溯。  
3.  **面向工作流的智能体（Agent）架构**：临床文档生成将从被动响应式工具，演进为主动参与诊疗全流程的智能体。这类智能体能自主规划、调用工具（如查询检验结果、检索指南）、进行多轮推理，并与医生形成高效的人机协作闭环。

主要挑战依然存在，包括：高质量、大规模中文临床对话数据的稀缺；严格的医疗数据隐私与合规要求对模型训练和部署的制约；以及如何建立被临床界广泛接受的、可靠的长期安全性和有效性评估体系。

## 结论

生成式AI正深刻重塑临床文档的生成范式，从效率工具向智能协作者演进。2022至2025年的研究已验证了其在特定场景下的巨大潜力，尤其是在门诊病历和影像报告自动化方面。通过RAG、多模态融合和领域微调等技术，研究者正系统性地解决模型的准确性、时效性和可靠性问题。未来，随着多模态智能体架构和可验证生成技术的成熟，生成式AI有望无缝嵌入临床工作流，成为提升医疗质量和效率不可或缺的核心组件，但其成功落地仍需跨越数据、隐私和评估等多重挑战。

## 参考文献

1.  杨鸿, 周霞. 生成式人工智能在呼吸内科的应用进展. 数理医药学杂志, 2025, 38(1): 60-66. [slyyx.whuznhmedj.com](https://slyyx.whuznhmedj.com/journal/254.html)
2.  钱乾, 孙丽萍, 刘佳霖, 等. 基于判别增强大语言模型微调的医学影像报告生成. 计算机应用研究, 2025, 42(3): 762-769. [arocmag.cn](https://www.arocmag.cn/abs/2024.08.0303)
3.  金哲, 邹健, 李逍, 等. 检索增强生成技术在医学人工智能中的应用与前沿探索. 药物流行病学杂志, 2025, 34(8): 962-971. [ywlxbx.whuznhmedj.com](https://ywlxbx.whuznhmedj.com/journal/481.html)
4.  吴天星, 曹旭东, 毕胜, 等. 基于大语言模型的重大慢病健康管理信息系统构建. 计算机研究与发展, 2025. [crad.ict.ac.cn](https://crad.ict.ac.cn/article/doi/10.7544/issn1000-1239.202440570?viewType=HTML)
5.  Liu, Xiaohong, et al. A generalist medical language model for disease diagnosis assistance. Nature Medicine, 2025, 31(3): 932-942. [ablesci.com](https://www.ablesci.com/scholar/paper?id=3NVkRpjW3)
6.  安徽医科大学第一附属医院. 从 "手动书写" 到 "智能生成"：AI病历生成创新应用. 健康界, 2025. [cn-healthcare.com](https://www.cn-healthcare.com/articlewm/20250604/content-1651301.html)
7.  孙磊, 汪安安, 宋一敏, 等. 大语言模型在临床医学领域的应用、挑战和展望. 解放军总医院学报, 2025. [xuebao.301hospital.com.cn](https://xuebao.301hospital.com.cn/article/doi/10.12435/j.issn.2095-5227.24070201)
8.  全筱筱, 熊文举, 潘军杰, 等. 基于大语言模型的数据查询机器人在医学领域的应用. 医学新知, 2024, 34(9): 1057-1063. [yxxz.whuznhmedj.com](https://yxxz.whuznhmedj.com/journal/6540.html)
9.  罗旭飞, 吕晗, 宋再伟, 等. 生成式人工智能对临床实践指南制订、评价和应用的影响. 协和医学杂志, 2024. [xhyxzz.pumch.cn](https://xhyxzz.pumch.cn/article/doi/10.12290/xhyxzz.2024-0602?viewType=HTML)
10. Yang, Rui, et al. The Evolving Landscape of Generative Large Language Models and Traditional Natural Language Processing in Medicine. arXiv preprint arXiv:2505.10261, 2025. [blog.csdn.net](https://blog.csdn.net/u013524655/article/details/148038198)
11. Hu, D., Liu, B., Zhu, X., et al. Zero-shot information extraction from radiological reports using ChatGPT. International Journal of Medical Informatics, 2024, 183: 105321.
12. Lyu, Q., Tan, J., Zapadka, M. E., et al. Translating radiology reports into plain language using ChatGPT and GPT-4 with prompt learning: results, limitations, and potential. Visual Computing for Industry, Biomedicine, and Art, 2023, 6(1): 9.