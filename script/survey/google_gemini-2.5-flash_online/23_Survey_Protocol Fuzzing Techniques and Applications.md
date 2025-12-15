## 协议模糊测试技术与应用研究综述 (2022-2025)

### 引言

协议模糊测试（Protocol Fuzzing）作为一种自动化软件测试方法，通过向目标程序发送异常、畸形或非预期的协议消息，以发现潜在的安全漏洞、程序缺陷或异常行为 [jos.org.cn](https://www.jos.org.cn/jos/article/abstract/7323)。传统的协议模糊测试常常面临输入生成效率低、协议状态空间覆盖不足、难以应对复杂协议结构等挑战 [chinaaet.com](https://www.chinaaet.com/article/3000166659)。近年来，随着人工智能，特别是大型语言模型（Large Language Models, LLMs）的飞速发展，为协议模糊测试带来了新的机遇 [secrss.com](https://www.secrss.com/articles/65103?app=1)。LLMs在理解、生成和处理自然语言及代码方面的强大能力，使其在协议模糊测试的各个环节展现出提升效率和准确性的潜力。本综述将聚焦2022年至2025年期间协议模糊测试领域涌现的代表性研究工作，对其方法分类、应用场景、实验评估及未来趋势进行系统性梳理和分析。

### 方法分类与代表作

本节将协议模糊测试方法分为基于LLM增强的模糊测试和非LLM驱动的模糊测试两大类，并精选代表性论文进行阐述。

#### 1. 基于大型语言模型（LLM）增强的模糊测试

LLM在协议模糊测试中的应用主要体现在提升输入生成质量、指导测试策略和自动化缺陷分析等方面。

##### 1.1 LLM辅助的驱动程序生成与语法感知变异

*   **CKGFuzzer: LLM-Based Fuzz Driver Generation Enhanced By Code Knowledge Graph (ICSE 2025)** [secrss.com](https://www.secrss.com/articles/77574)
    *   **研究问题：** 传统Fuzz Driver手动编写耗时且易遗漏测试场景，现有LLM生成方法缺乏对代码库深层上下文和复杂API交互的全面理解。
    *   **核心方法：** 提出CKGFuzzer，通过代码知识图谱（CKG）增强检索增强生成（RAG）和Multi-LLMs系统。CKG提供丰富的代码上下文，LLM结合角色提示生成Fuzz Driver，并设计基于RAG的修复智能体自动修正编译错误。
    *   **关键实验结论：** 在8个开源C语言库上，CKGFuzzer在6个库上取得最高代码覆盖率，平均提升8.73%。动态修复模块将编译成功率从57.39%提升至93.99%。
*   **Understanding Large Language Model Based Fuzz Driver Generation (arXiv 2023)** [secrss.com](https://www.secrss.com/articles/65607)
    *   **研究问题：** 探索使用LLMs自动生成Fuzz Driver的可行性与挑战，以减少Fuzz测试中驱动程序编写的人工投入。
    *   **核心方法：** 设计并实现了五种从基础到增强的LLM查询策略，包括利用API文档、示例代码以及交互式查询，系统性地生成Fuzz Driver。
    *   **关键实验结论：** 64%的问题可以完全自动化解决，若加入手动语义验证，该比例可提升至91%，显示了LLM生成驱动程序的实用性和潜力。
*   **Large Language Model Guided Protocol Fuzzing (NDSS 2024)** [csdn.net](https://blog.csdn.net/qq_33976344/article/details/137472900), [rivers.chaitin.cn](https://rivers.chaitin.cn/blog/cq954d10lnechd244oc0)
    *   **研究问题：** 如何在缺乏机器可读协议规范的情况下发现协议实现中的安全缺陷，并克服传统协议模糊测试对初始种子文件和状态空间探索的局限。
    *   **核心方法：** 提出ChatAFL，通过与LLM进行系统交互，提取协议消息语法指导结构感知突变；LLM用于丰富初始种子集多样性；利用LLM突破覆盖率瓶颈，生成导致新状态的消息。
    *   **关键实验结论：** ChatAFL比AFLNET和NSFUZZ多覆盖47.60%和42.69%的状态转换，5.81%和6.74%的代码，并发现了9个以前未知的漏洞。

##### 1.2 LLM驱动的通用模糊测试与优化

*   **Fuzz4All: Universal Fuzzing with Large Language Models (ICSE 2024)** [rivers.chaitin.cn](https://rivers.chaitin.cn/blog/cq954b90lnechd244o80)
    *   **研究问题：** 现有模糊测试工具多针对特定语言，缺乏通用性和进化能力，难以应对新语言特性和多样化输入。
    *   **核心方法：** 提出Fuzz4All，利用LLMs作为输入生成和变异引擎，通过“提示词蒸馏”（Autoprompting）生成精简有效的提示词，并在Fuzzing Loop中迭代更新提示以生成多样化输入。
    *   **关键实验结论：** Fuzz4All在六种不同语言（C, C++, Go, SMT2, Java, Python）的九个测试系统上，实现了比现有特定语言模糊测试工具更高的覆盖率。发现了98个漏洞，其中64个为未知漏洞。
*   **LLAMAFUZZ: Large Language Model Enhanced Greybox Fuzzing (arXiv 2024)** [csdn.net](https://blog.csdn.net/m0_47540684/article/details/143457894)
    *   **研究问题：** 传统灰盒模糊测试的随机变异策略在处理结构化数据时性能受限，或专用模糊测试器缺乏通用性。
    *   **核心方法：** 提出LLAMAFUZZ，利用LLM的预训练知识生成符合格式的有效输入，并通过配对的变异种子微调LLM，使其更有效地学习结构化格式和变异策略。LLM与模糊测试器异步集成。
    *   **关键实验结论：** LLAMAFUZZ在Magma基准测试中比主要竞争对手平均多发现41个漏洞，总共识别出47个独特漏洞。在真实程序集中，代码覆盖率比AFL++平均高出27.19%。

#### 2. 非LLM驱动的协议模糊测试

此类别下的研究主要通过改进符号执行、程序分析、状态建模等传统技术来提升协议模糊测试效果。

*   **CBFuzzer：基于执行上下文导向及保护突破的程序缺陷模糊检测 (计算机研究与发展 2025)** [crad.ict.ac.cn](https://crad.ict.ac.cn/article/doi/10.7544/issn1000-1239.202330755?viewType=HTML)
    *   **研究问题：** 现有模糊测试方法缺乏针对具体测试任务差异性的策略调整，导致测试效率和效果不佳，且难以突破保护机制。
    *   **核心方法：** 提出CBFuzzer，通过捕获和分析受检程序对输入测试用例实际处理过程中的具体上下文信息，快速探索程序结构特征，优化样本突变策略，并能突破保护机制。
    *   **关键实验结论：** CBFuzzer在脆弱点暴露能力方面有6.8%~36.76%的提升，实际脆弱点检出数量最高提升66.67%。共发现126个新漏洞，并提交给CVE。
*   **基于生成对抗网络的工控协议模糊测试研究 (网络安全与数据治理 2025)** [chinaaet.com](https://www.chinaaet.com/article/3000166659)
    *   **研究问题：** 传统工控协议模糊测试依赖专家经验和协议规范，神经网络方法受限于训练数据质量，缺乏通用有效的方法。
    *   **核心方法：** 提出基于WGAN-GP（Wasserstein Generative Adversarial Network with Gradient Penalty）的工控协议模糊测试方法，结合统计语言模型N-gram修正训练结果，构建了面向多种ICPs的通用模糊测试框架GPFuzz。
    *   **关键实验结论：** 在3种常见工控协议（Modbus/TCP, Ethernet/IP, S7comm）上，GPFuzz生成的测试用例多样性表现优异，在接受率和异常触发指标上优于其他模糊测试方法。

### 实验与评价总结

这些研究普遍采用代码覆盖率（分支覆盖、状态覆盖、状态转换覆盖）和漏洞发现能力作为主要的评估指标。LLM增强的模糊测试方法通常能在这些指标上超越传统的或非LLM驱动的基线工具，尤其在提高复杂协议的状态空间探索、增强变异策略的有效性以及自动化Fuzz Driver生成方面显示出显著优势。例如，ChatAFL在状态覆盖和代码覆盖方面均优于AFLNET和NSFUZZ，并发现了更多未知漏洞 [rivers.chaitin.cn](https://rivers.chaitin.cn/blog/cq954d10lnechd244oc0)。Fuzz4All则强调了LLM在多语言通用模糊测试中的潜力，验证了LLM作为通用输入生成和变异引擎的有效性 [rivers.chaitin.cn](https://rivers.chaitin.cn/blog/cq954b90lnechd244o80)。非LLM驱动的方法，如CBFuzzer，则通过精细的程序上下文分析和保护突破策略，在特定场景下实现了对脆弱点检出率的显著提升 [crad.ict.ac.cn](https://crad.ict.ac.cn/article/doi/10.7544/issn1000-1239.202330755?viewType=HTML)。总体而言，LLM的引入降低了对人工领域知识的依赖，提升了自动化水平，并扩大了模糊测试的有效范围。

### 趋势与挑战

未来协议模糊测试的研究趋势主要体现在以下几个方面：

1.  **多模态LLM与模糊测试的深度融合：** 当前研究主要侧重于单一模态LLM（文本代码）的应用。未来将探索结合视觉、听觉等多种模态的LLM，以处理更复杂的协议类型和环境信息，例如图形化协议接口、实时通信流中的非文本特征等，从而实现更全面的模糊测试。
2.  **LLM驱动的端到端自动化模糊测试流程：** 现有LLM应用仍多集中于特定环节（如输入生成、Fuzz Driver生成）。未来的研究将致力于构建完全由LLM智能体驱动的端到端模糊测试框架，包括测试目标识别、环境配置、测试执行、缺陷分析和补丁生成等全生命周期，最大限度减少人工干预。
3.  **可解释性与安全性提升：** LLM在生成模糊输入和分析结果时，其内部决策过程往往“黑盒”。未来研究将关注提升LLM在模糊测试中的可解释性，例如通过解释生成输入的意图和潜在漏洞类型。同时，也将关注LLM自身安全性问题，防范恶意提示注入或模型偏见导致的不当测试行为。
4.  **领域特定协议和硬件协议的模糊测试：** 随着物联网、工业控制系统和智能汽车等领域的发展，针对这些特定领域协议（如工控协议、车联网协议）和硬件相关协议的模糊测试需求日益增长。LLM结合领域知识图谱有望在该类协议的复杂交互和状态建模方面发挥关键作用。

挑战则包括LLM上下文窗口限制、幻觉问题、计算资源消耗、实时性要求以及如何有效评估LLM生成测试用例的质量和多样性。

### 结论

2022-2025年期间，协议模糊测试领域，尤其是LLM增强的方法，取得了显著进展。LLMs的强大语言理解和生成能力正在革新Fuzz Driver生成、测试输入变异和状态空间探索等关键环节。这些新方法有效提升了代码覆盖率、漏洞发现能力，并降低了对人工专业知识的依赖。尽管仍面临性能、可解释性等诸多挑战，但LLM与模糊测试的深度融合无疑是未来软件安全测试的重要方向，有望促使全自动化、高效率的漏洞挖掘成为现实。

### 参考文献

*   [crad.ict.ac.cn] 强保华. (2025). CBFuzzer：基于执行上下文导向及保护突破的程序缺陷模糊检测. *计算机研究与发展*, *62*(3), 517-531.
*   [chinaaet.com] 宗学军, 隋一凡, 王国刚, 等. (2025). 基于生成对抗网络的工控协议模糊测试研究. *网络安全与数据治理*, *43*(7), 13-20.
*   [csdn.net] m0\_47540684. (2024). LLAMAFUZZ:Large Language Model Enhanced Greybox Fuzzing 精翻. Retrieved from [https://blog.csdn.net/m0_47540684/article/details/143457894](https://blog.csdn.net/m0_47540684/article/details/143457894)
*   [csdn.net] qq\_33976344. (2024). \[论文分享] Large Language Model guided Protocol Fuzzing. Retrieved from [https://blog.csdn.net/qq_33976344/article/details/137472900](https://blog.csdn.net/qq_33976344/article/details/137472900)
*   [jos.org.cn] 李岩, 杨文章, 张翼, & 薛吟兴. (2025). 基于大语言模型的模糊测试研究综述. *软件学报*, *36*(6), 2404-2431. doi:10.13328/j.cnki.jos.007323
*   [rivers.chaitin.cn] Chunqiu Steven Xia, Matteo Paltenghi, Lingming Zhang, et al. (2024). Fuzz4All: Universal Fuzzing with Large Language Models. *International Conference on Software Engineering (ICSE)*. Retrieved from [https://rivers.chaitin.cn/blog/cq954b90lnechd244o80](https://rivers.chaitin.cn/blog/cq954b90lnechd244o80)
*   [rivers.chaitin.cn] Ruijie Meng, Martin Mirchev, Marcel Bohme, Abhik Roychoudhury, et al. (2024). Large Language Model guided Protocol Fuzzing. *NDSS 2024*. Retrieved from [https://rivers.chaitin.cn/blog/cq954d10lnechd244oc0](https://rivers.chaitin.cn/blog/cq954d10lnechd244oc0)
*   [secrss.com] 安全极客. (2024). *研究：基于大语言模型的模糊测试技术*. Retrieved from [https://www.secrss.com/articles/65103?app=1](https://www.secrss.com/articles/65103?app=1)
*   [secrss.com] 安全极客. (2024). *理解基于大语言模型的模糊测试驱动程序生成*. Retrieved from [https://www.secrss.com/articles/65607](https://www.secrss.com/articles/65607)
*   [secrss.com] 安全学术圈. (2025). *基于大模型的Fuzz Driver生成工具*. Retrieved from [https://www.secrss.com/articles/77574](https://www.secrss.com/articles/77574)