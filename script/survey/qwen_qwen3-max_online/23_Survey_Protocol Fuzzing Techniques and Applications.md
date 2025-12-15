# 协议模糊测试技术研究综述（2022–2025）

## 引言

协议模糊测试（Protocol Fuzzing）是挖掘网络服务实现中安全漏洞的关键手段。其核心挑战在于协议输入具有强结构约束（如语法、状态依赖），且缺乏机器可读的规范文档。2022–2025年间，该领域研究呈现两大主线：一是传统方法通过更精细的状态建模与覆盖引导提升效率；二是新兴方法利用大语言模型（LLM）或生成对抗网络（GAN）等机器学习技术自动提取协议知识并生成有效测试用例。本文系统梳理该时段内顶会（NDSS、ICSE、USENIX Security等）与高质量预印本中的代表性工作，按技术路线分类评述，并总结实验范式与未来趋势。

## 方法分类与代表作

### 基于状态建模与覆盖引导的增强方法

该类方法在经典灰盒模糊器（如 AFLNet）基础上，通过改进状态表示或反馈机制提升对协议状态空间的探索能力。

**NSFuzz**（NSDI 2023）[secrss.com](https://www.secrss.com/articles/77574) 针对 AFLNet 依赖响应码推断状态的局限，提出基于程序内部变量（如会话 ID、状态标志位）构建更精确的状态表示。其采用轻量级插桩捕获变量变化，并设计高效的同步机制避免状态漂移。在 Profuzzbench 基准上，NSFuzz 在状态转换覆盖率上平均比 AFLNet 高出 43%，并发现了 4 个新漏洞。

**BLEEM**（NDSS 2023）另辟蹊径，不依赖服务器内部状态，而是通过分析服务器输出的**包序列**来推断其内部状态机。其利用输出序列的相似性对输入序列聚类，将聚类中心作为状态表示，并引导生成能触发新输出序列（即新状态）的输入。实验表明，BLEEM 在多个协议实现上显著提升了状态空间覆盖率，证明了无侵入式状态建模的可行性。

### 基于生成对抗网络（GAN）的工控协议模糊测试

针对工业控制协议（ICP）规范不公开的问题，研究者利用 GAN 从网络流量中自动学习协议语法。

**GANFuzz**（早期原型，CSDN 2025综述引用）[blog.csdn.net](https://blog.csdn.net/qq_32505207/article/details/104171909) 是该方向的奠基性工作。它将协议消息视为离散序列，采用 RNN 作为生成器、CNN 作为判别器，并使用 SeqGAN 算法解决离散数据不可微问题。通过聚类（如按长度、内容特征）将消息分组训练，提升生成质量。在 Modbus/TCP 协议上，其生成的测试用例接受率显著优于随机变异。

**GPFuzz**（《网络安全与数据治理》2024）[chinaaet.com](https://www.chinaaet.com/article/3000166659) 在 GANFuzz 基础上进行改进，采用 **WGAN-GP**（Wasserstein GAN with Gradient Penalty）替代原始 GAN，解决了训练不稳定和模式崩溃问题。同时，引入 **N-gram 统计语言模型**对 GAN 生成的结果进行后处理修正。在油气集输靶场的 Modbus/TCP、Ethernet/IP 等三种协议上，GPFuzz 在异常触发率上优于其他基线方法。

### 基于大语言模型（LLM）的协议模糊测试

LLM 因其强大的自然语言理解与生成能力，被用于直接从 RFC 文档中提取协议知识，实现零样本或少样本的协议模糊测试。

**ChatAFL**（NDSS 2024）[blog.csdn.net](https://blog.csdn.net/qq_33976344/article/details/137472900) 是 LLM 引导协议模糊测试的代表性工作。其提出三种策略：1）从 LLM 提取协议消息的机器可读语法，用于结构感知变异；2）利用 LLM 丰富初始种子，补充缺失的消息类型；3）在覆盖率停滞时，提示 LLM 生成能触发新状态转换的下一个消息。在 6 个协议上，ChatAFL 比 AFLNet 多覆盖 29.55% 的状态和 5.81% 的代码，并发现了 9 个新漏洞。

**CKGFuzzer**（ICSE 2025, Best Paper）[secrss.com](https://www.secrss.com/articles/77574) 聚焦于库 API 的 Fuzz Driver 生成，其核心创新是构建**代码知识图谱（CKG）**。CKG 通过静态分析提取代码实体（函数、变量）及其关系，并作为增强上下文输入给 LLM。该方法解决了 LLM 因上下文窗口限制而无法全面理解大型代码库的问题。实验显示，CKGFuzzer 将 Fuzz Driver 的编译成功率从 57.39% 提升至 93.99%，并成功检测到 11 个真实 Bug。

**Fuzz4All**（ICSE 2024）[rivers.chaitin.cn](https://rivers.chaitin.cn/blog/cq954b90lnechd244o80) 提出了一种通用的 LLM 驱动的模糊测试框架，适用于任何接受结构化输入（如编程语言）的系统。其关键技术是**自动提示蒸馏（Autoprompting）**，即从冗长的官方文档中自动提炼出简洁有效的 LLM 提示。Fuzz4All 在 C/C++/Go/SMT2/Java/Python 六种语言的编译器和求解器上均取得了比专用 Fuzzer 更高的覆盖率，并发现了 98 个漏洞。

## 实验与评价总结

2022–2025 年的协议模糊测试研究在实验评价上形成了相对统一的范式与共性结论：

1.  **基准平台**：绝大多数网络协议模糊测试工作采用 **Profuzzbench** 作为标准评估平台，其包含 LIVE555 (RTSP)、ProFTPD (FTP) 等 6 个广泛使用的、有状态的网络服务实现。工控协议研究则多在自建或公开的工业靶场（如油气集输系统）中进行。
2.  **核心指标**：评价聚焦于**状态空间覆盖**（覆盖的状态数、状态转换数）与**代码覆盖**（分支覆盖率）。新漏洞发现数量是衡量实用性的黄金标准。LLM/GAN 相关工作还会报告**种子接受率**（被测程序能正常处理的测试用例比例），以衡量生成质量。
3.  **共性结论**：实验普遍证实，利用外部知识（无论是通过程序分析、流量学习还是 LLM 理解）来指导模糊测试，能显著超越纯随机或基于反馈的变异策略。尤其是在探索深层、罕见的状态路径和生成语法有效的复杂输入方面，知识引导方法展现出巨大优势。然而，这类方法通常引入了额外的计算或查询开销，需要在效率与效果之间权衡。

## 趋势与挑战

基于对近期工作的分析，2025年及之后的研究将聚焦于以下方向：

1.  **多智能体协同模糊测试**：如 CKGFuzzer 所示，单一 LLM 难以胜任所有任务。未来系统将由多个专业化智能体（如状态推断智能体、语法生成智能体、崩溃分析智能体）协同工作，形成自动化模糊测试流水线。
2.  **模糊测试与形式化方法的融合**：当前 LLM 生成存在“幻觉”风险。结合形式化规约（如用 TLA+ 描述的协议）或轻量级形式验证，可对 LLM 生成的测试用例进行正确性校验，或反向用模糊测试结果修正形式模型。
3.  **面向新型协议的模糊测试**：随着 Web3、物联网和 AI 原生协议（如 gRPC、各种 LLM 服务 API）的普及，模糊测试技术需适应其动态性、加密性和复杂状态机等新特性。如何在缺乏清晰规范的情况下对这些协议进行有效测试，是亟待解决的挑战。

## 结论

2022–2025 年是协议模糊测试技术快速演进的时期。研究从传统的覆盖反馈驱动，转向了以知识（协议规范、代码结构、流量模式）为核心驱动力的新范式。大语言模型和生成对抗网络的引入，极大地提升了模糊测试在协议理解、种子生成和状态探索方面的自动化与智能化水平。尽管在效率、可靠性方面仍存挑战，但知识引导的模糊测试已成为主流方向，并展现出在更广泛的软件安全领域（如编译器、AI 框架）的应用潜力。

## 参考文献

1.  Pham, V.-T., Böhme, M., & Roychoudhury, A. (2020). AFLNet: A greybox fuzzer for network protocols. *ICST*.
2.  Qin, S., et al. (2023). NSFuzz: Towards efficient and state-aware network service fuzzing. *NSDI*.
3.  Ba, J., et al. (2022). Stateful greybox fuzzing. *USENIX Security*.
4.  Natella, R., & Pham, V.-T. (2021). Profuzzbench: A benchmark for stateful protocol fuzzing. *ISSTA*.
5. 胡志成, 等. (2018). GANFuzz: A GAN-based industrial network protocol fuzzing framework. *arXiv preprint arXiv:1807.05355*. [blog.csdn.net](https://blog.csdn.net/qq_32505207/article/details/104171909)
6.  宗学军, 等. (2024). 基于生成对抗网络的工控协议模糊测试研究. *网络安全与数据治理*, *43*(7), 13-20. [chinaaet.com](https://www.chinaaet.com/article/3000166659)
7.  Meng, R., et al. (2024). Large Language Model guided Protocol Fuzzing. *NDSS*. [blog.csdn.net](https://blog.csdn.net/qq_33976344/article/details/137472900)
8.  Xu, H., et al. (2025). CKGFuzzer: LLM-Based Fuzz Driver Generation Enhanced By Code Knowledge Graph. *ICSE*. [secrss.com](https://www.secrss.com/articles/77574)
9.  Xia, C. S., et al. (2024). Fuzz4All: Universal Fuzzing with Large Language Models. *ICSE*. [rivers.chaitin.cn](https://rivers.chaitin.cn/blog/cq954b90lnechd244o80)
10. Zhang, C., et al. (2023). Understanding Large Language Model Based Fuzz Driver Generation. *arXiv preprint arXiv:2307.12469*. [secrss.com](https://www.secrss.com/articles/65607)
11. Huang, L., et al. (2024). Large Language Models Based Fuzzing Techniques: A Survey. *arXiv preprint arXiv:2402.00350*. [secrss.com](https://www.secrss.com/articles/65103)
12. Tang, C., et al. (2025). CBFuzzer：基于执行上下文导向及保护突破的程序缺陷模糊检测. *计算机研究与发展*. [crad.ict.ac.cn](https://crad.ict.ac.cn/cn/article/Y2025/I3/790)
13. 赵浩东, 等. (2025). 基于机器学习的模糊测试系统. *人工智能与机器人研究*, *14*(2), 341-349. [hanspub.org](https://pdf.hanspub.org/airr2025142_102610569.pdf)