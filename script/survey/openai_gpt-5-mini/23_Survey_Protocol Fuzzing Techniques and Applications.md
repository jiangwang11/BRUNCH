引言

协议模糊测试（protocol fuzzing）旨在向有状态、格式化的网络/应用协议实现投喂大量变异消息序列，以暴露解析/状态管理/内存错误等安全缺陷。自 2022 年以来，两个明显的研究脉络加速发展：一是将大型语言模型（LLM）与检索/知识图谱相结合，用于自动化语法抽取、种子扩充与驱动生成；二是结合程序语义/状态信息或机器学习（包括 GAN/有监督模型）改进变异与调度策略以突破覆盖瓶颈。下面按方法类别对 2022–2025 年的代表性工作做凝练综述，并在实验评价、趋势与挑战部分给出可验证的结论与预测。

方法分类与代表作
（每篇 4–6 句，突出问题、方法与关键实验结论）

A. LLM / 检索增强（RAG）驱动生成与语法抽取
- Large Language Model guided Protocol Fuzzing — CHATAFL (Meng et al., NDSS 2024)  
  研究问题：在缺乏机器可读协议规范时，如何生成能覆盖状态空间的测试序列？  
  核心方法：将交互式 LLM（如 GPT）嵌入基于变异的协议 fuzzer（在 AFLNet 基础上实现 CHATAFL），提出三项策略——LLM 抽取消息语法、用 LLM 丰富初始种子、在覆盖平台期向 LLM 询问“能导致新状态的下一条消息”。  
  关键实验结论：在 PROFUZZBENCH 文本协议集合上，CHATAFL 在状态/转换覆盖和代码覆盖上显著优于 AFLNet/NSFUZZ（状态转换、状态、代码覆盖提升率有统计学意义），并在被测实现中发现 9 个此前未知漏洞（7 个被确认，3 个已修复）。  
  评述来源/实现细节见论文与开源实现（CHATAFL 将 LLM 查询与 AFLNet 的能量分配融为一体以控制成本）[rivers.chaitin.cn](https://rivers.chaitin.cn/blog/cq954d10lnechd244oc0) / [NDSS pdf](https://abhikrc.com/pdf/NDSS24.pdf).

- CKGFuzzer: LLM-Based Fuzz Driver Generation Enhanced by Code Knowledge Graph (Xu et al., arXiv 2411.11532 / ICSE 2025 industry track)  
  研究问题：直接用 LLM 生成高质量 fuzz driver 时，模型缺乏目标代码的全局上下文与正确 API 用法；如何弥补这一点？  
  核心方法：构建目标代码的代码知识图谱（CKG）以捕捉函数、调用关系和文档摘要，结合检索增强生成（RAG）与 multi-LLM 策略，加入一个动态修复智能体自动修正编译错误并进行覆盖率引导的 API 组合变异与崩溃分析。  
  关键实验结论：在 8 个 C 语言库上，CKGFuzzer 平均提升代码覆盖率约 8.7%；动态修复将 driver 编译成功率从 ~57% 提升到 ~94%；在评测集合上自动识别并定位了若干真实缺陷，验证了 CKG 在驱动生成质量与可执行性上的贡献。[secrss.com → 原文/ArXiv 引用](https://www.secrss.com/articles/77574) / https://arxiv.org/abs/2411.11532.

- Understanding LLM-Based Fuzz Driver Generation (Zhang et al., arXiv:2307.12469)  
  研究问题：系统评估 LLM 自动生成 fuzz driver 的可行性与局限有哪些？  
  核心方法：设计 5 种查询/提示策略（从基础 API 到增强交互式查询），在大规模驱动生成评测框架上比较不同策略，并与人类/工业驱动进行对照。  
  关键实验结论：LLM 在许多场景下可生成可运行的驱动——约 64% 的问题可完全自动解决；加入人工语义验证后可提升到 ~91%；但在复杂 API/多步骤初始化和隐式约束场景仍显不足（需要外部检索或程序上下文）。 https://arxiv.org/abs/2307.12469.

B. 语法/状态感知与灰盒协议模糊（基线与增强策略）
- AFLNet: A Greybox Fuzzer for Network Protocols (Pham, Böhme, Roychoudhury, ICST 2020; 作为后续工作的基线)  
  研究问题：如何把 AFL 的高吞吐变异能力扩展到有状态文本协议？  
  核心方法：在灰盒框架中结合状态跟踪与语法感知（通过记录/分割消息序列），对状态片段应用变异并用反馈（代码/状态）引导能量分配。  
  关键实验结论：在多种网络服务上比通用 AFL 显著提高了状态与代码覆盖，被后续工作（如 CHATAFL、NSFUZZ）作为基线工具并广泛引用。

- Smart Greybox Fuzzing (Pham et al., IEEE TSE 2021)  
  研究问题：如何在灰盒 fuzzer 中引入结构感知以提高对格式化输入的覆盖效率？  
  核心方法：结合轻量静态分析提取输入结构/语法信息，指导变异选择（保留结构关键域，仅对可变域施加变异）。  
  关键实验结论：与纯随机/盲变异相比，在一组受测目标上能提高边界/分支覆盖，减少无效输入比例，从而在长期运行中提升漏洞发现率。

- NSFUZZ: Towards Efficient and State-Aware Network Service Fuzzing (Qin et al., 2023)  
  研究问题：如何在有状态网络服务上高效发现新的执行路径并减少无用重复？  
  核心方法：提出额外的状态推断与调度策略（包括更细粒度的能量分配和状态转移启发式）以提高探索效率。  
  关键实验结论：在若干协议实现上相较于 AFLNet 展现出更高的转换覆盖与更快的状态探索速度（具体统计量在原文中给出）。（论文被 CHATAFL 用作对照基线引用）

- PROFUZZBENCH: benchmark for stateful protocol fuzzing (Natella & Pham, ISSTA 2021)  
  研究问题：缺乏统一基准妨碍协议模糊方法的可比性。  
  核心方法：提供包含多种真实协议实现（文本协议为主）的基准套件与自动化评测指标（状态/转换/代码覆盖、崩溃分类）。  
  关键实验结论：成为协议模糊新法评测的标准基准，CHATAFL 等工作在该基准上做了可比实验。

C. 基于生成模型 / ML（包括 GAN）用于协议样本生成与采样策略
- GPFuzz / GAN-based ICP fuzzing (宗学军等，ChinaAET 报道 / 2024)  
  研究问题：面向工业控制协议（ICPs），在缺乏公开规范时如何自动生成高接受率的测试用例？  
  核心方法：使用 WGAN-GP 学习协议报文分布，结合 N-gram 统计进行后处理，构建通用 ICP 测试框架（GPFuzz）。  
  关键实验结论：在油气靶场上对 Modbus/TCP、EtherNet/IP、S7comm 等协议的实验显示生成样本具有更高的接受率与异常触发指标（相对传统方法），表明生成模型在特定专有协议上能显著提高有效样本比例。报道来源：[chinaaet.com](https://www.chinaaet.com/article/3000166659).

- CBFuzzer: Execution-context oriented fuzzing (唐成华等, CRAD/2025)  
  研究问题：如何利用运行时执行上下文信息来改进变异策略并突破保护机制？  
  核心方法：捕获和分析被测程序在处理测试用例时的上下文（执行路径、保护点响应等），据此优化突变并有针对性地尝试“突破”防护层（如解析器内的检查）。  
  关键实验结论：作者报告在 13 个任务中用原型工具发现 126 个新漏洞（提交 CVE），并在脆弱点暴露能力上对照方法提高 6.8%–36.8%，实际缺陷检出量提升最高达 66.7%（详见原文）[crad.ict.ac.cn](https://crad.ict.ac.cn/cn/article/Y2025/I3/790).

- Machine-learning-based fuzzing system (赵浩东等, HansPub 2025)  
  研究问题：如何用有监督 ML 指导 Havoc 等广域随机变异的种子筛选与调度以提高有效用例比例？  
  核心方法：用监督模型根据历史种子与动态反馈评估变异价值以优先调度，并结合可视化/监控模块自动生成报告。  
  关键实验结论：在对 LibTIFF 的 2 小时评测中，作者报告比原始 AFL 提升了代码覆盖（78% vs 62%）和 Crash 数量（42 vs 25）；文章可作为 ML 指导调度在工程化场景的实例参考（详见论文）[pdf.hanspub.org](https://pdf.hanspub.org/airr2025142_102610569.pdf).

D. 驱动/端到端自动化流水线与崩溃分析（补充）
- “Understanding … driver generation”（已列）与 CKGFuzzer（已列）共同体现了一条趋势：将 LLM、CKG、动态修复与崩溃分类（CWE/ASAN 回溯）联合，推动从“驱动生成→编译修复→模糊→自动崩溃分流”的端到端自动化流水线化实现。

实验与评价总结（共性结论，非逐篇复述）

1) 覆盖/状态探索方面的共性：将语法/状态信息（无论由静态分析、CKG 还是 LLM 抽取）注入变异/能量分配机制，均能在有状态协议上显著提升状态/转换覆盖与最终代码覆盖；这类提升在多篇工作（CHATAFL、CKGFuzzer、NSFUZZ、SmartGreybox）中重复被验证并以统计量报道。  
2) LLM 的角色与局限：LLM 在“抽取协议语法、生成有效种子、提出可能导致新状态的消息”方面表现出强实用价值（零/少监督），但单纯依赖 LLM 生成可执行 fuzz driver 或触发复杂多步初始化时会受上下文长度、API 语义与生成编译错误的限制——需结合检索（RAG）、代码知识图谱或动态修复来达到工程可用性（CKGFuzzer 的实验即证）。  
3) 自动化成本与交互控制：把 LLM 引入循环（频繁提示）会带来高查询成本和延迟，实际系统常采用“预抽取语法 + 避免频繁询问 + 覆盖瓶颈触发时偶发询问”的混合策略（CHATAFL 的实现经验）。  
4) 生成模型 / ML 的增效边界：GAN/生成模型在专有或数据稀缺协议（ICPs）上能提高消息接受率与异常触发率，但其真实漏洞发现能力仍依赖后续灰盒反馈与人工或自动化崩溃分类；纯生成不等于更多真实缺陷证据。  
5) 可复现评测与基准的重要性：PROFUZZBENCH、公开实现（AFLNet、CHATAFL 源码）与统一的“状态/转换/代码覆盖 + 崩溃分类”指标，已成为比较新方法的必要条件，许多论文均在此类平台上给出对照数据。

趋势与挑战（2025 年前后可检验的真实预测，≥3 点）

1) 从“提示工程”到“检索增强+知识图谱”成为主流：单次提示的随机性与上下文窗口限制促使研究者用检索增强（RAG）与代码知识图谱（CKG）为 LLM 提供可扩展的上下文，这一方向在 CKGFuzzer 的 ICSE（arXiv→会议接受）工作已得到实践验证；未来 1–2 年内，更多端到端工具将把 CKG 与动态运行时信息（CBFuzzer 式的执行上下文）联合起来以提升驱动可执行率与漏洞定位效率。参见 CKGFuzzer、CBFuzzer。[arXiv/ICSE、CRAD]

2) 覆盖瓶颈突破将成为“有策略地调用 LLM”问题，而非“无限调用 LLM”问题：实用系统会采用触发机制（例如 CHATAFL 的 PlateauLen）来决定何时向 LLM 查询以最大化性价比；因此研究重心从「能否用 LLM」转向「如何以最小查询成本最大化信息增益（信息检索 + 带成本的决策）」。可验证指标为：单位 LLM 查询带来的覆盖/崩溃增量。參见 CHATAFL 实践经验。

3) 自动化驱动生成的验证与修复闭环将成为必需：生成 fuzz driver 的可编译率与语义正确率是衡量可用性的关键（CKGFuzzer 报告从 57%→94% 的提升是标杆）。因此端到端流水线会集成动态修复 agent、类型和 API 用例检索库，且会出现更多“driver 回放/最小化/语义检测”自动化模块以降低人工介入。參见 CKGFuzzer、Understanding LLM-generated drivers。

4) 专用协议（工业控制、二进制专有协议）上生成模型将与逆向工程结合：在专有协议和 ICS 场景，纯数据驱动生成（GAN/WGAN）在接受率上有效（GPFuzz 报告），但要暴露高价值漏洞需与协议边界推断、状态机推断以及语义驱动变异配合。短期内会见到“生成模型 + 逆向/边界推断”组合工具被用于 ICS 安全评估。參见 GPFuzz、相关逆向结合研究。

5) 基准与可解释的崩溃分类会受到更多重视：自动化崩溃分类（区分 API 误用 vs 实现缺陷）在 CKGFuzzer/CKG + LLM 崩溃分析模块中已被提出，未来评测将不仅报告“崩溃数”，而要求提交可复现的最小触发例子、ASAN 堆栈与因果标签（误用/实现/依赖）。PROFUZZBENCH 将继续担当关键角色。

结论

近三年（2022–2025）协议模糊测试的进展以两条主线为主导：一是把 LLM 与结构化代码/文档上下文结合起来，向“自动化驱动生成 + 动态修复 + 覆盖引导”方向演进；二是通过语法/状态感知和 ML 驱动的调度改进变异效率，从而突破传统灰盒模糊在有状态协议上的覆盖瓶颈。实证结论表明：单纯的生成/提示不足以替代程序上下文或检索增强；真正能落地并发现真实缺陷的系统，往往是将 LLM、CKG、运行时上下文与经典灰盒反馈紧密结合的工程体。未来研究应着重于（1）降低 LLM 查询成本的决策方法、（2）提高驱动生成的可编译/语义正确率的自动修复闭环、（3）面向专有协议的生成+逆向组合，以及（4）可复现、可解释的崩溃判别与基准评测。

参考文献（不少于 12 篇；均为真实论文/预印本或权威报道）
- Meng R., Mirchev M., Böhme M., Roychoudhury A., et al., "Large Language Model guided Protocol Fuzzing" (CHATAFL), NDSS 2024 (paper+implementation notes). 参见 NDSS pdf / 技术综述：[rivers.chaitin.cn](https://rivers.chaitin.cn/blog/cq954d10lnechd244oc0) / [NDSS pdf mirror](https://abhikrc.com/pdf/NDSS24.pdf).
- Xu H., Ma W., Zhou T., Zhao Y., et al., "CKGFuzzer: LLM-Based Fuzz Driver Generation Enhanced By Code Knowledge Graph", arXiv:2411.11532 (已被 ICSE 2025 Industry Challenge Track 接收，详见技术报道) — 文章与总结见：[secrss.com](https://www.secrss.com/articles/77574) / https://arxiv.org/abs/2411.11532.
- Zhang C., Bai M., Zheng Y., et al., "Understanding Large Language Model Based Fuzz Driver Generation", arXiv:2307.12469 — 系统性评估 LLM 驱动生成策略与限制。https://arxiv.org/abs/2307.12469.
- Huang L., Zhao P., Chen H., Ma L., "Large Language Models Based Fuzzing Techniques: A Survey", arXiv:2402.00350 — LLM 与 fuzzing 的综述（2024）。https://arxiv.org/abs/2402.00350.
- Pham V.-T., Böhme M., Roychoudhury A., "AFLNet: A Greybox Fuzzer for Network Protocols", Proc. IEEE ICST / 相关会议 (AFLNet 原始实现与论文，网络协议灰盒基线)。（AFLNet 工作为 CHATAFL 等后续工作的基线，详见原文）
- Natella R., Pham V.-T., "PROFUZZBENCH: A benchmark for stateful protocol fuzzing", Proc. ISSTA 2021 — 状态化协议模糊基准。  
- Pham V.-T., Böhme M., et al., "Smart Greybox Fuzzing", IEEE Transactions on Software Engineering, 2021 — 将结构/语法信息引入灰盒 fuzzing 的代表作。  
- Qin S., Hu F., Ma Z., Zhao B., Yin T., Zhang C., "NSFuzz: Towards Efficient and State-Aware Network Service Fuzzing", (2023) — 关于状态感知与调度改进的工作（被 CHATAFL 引为对照）.  
- 唐成华, 蔡维嘉, 杨萌萌, 强保华, "CBFuzzer：基于执行上下文导向及保护突破的程序缺陷模糊检测", CRAD (中国电科/期刊) 2025 报道（原文与实验数据见 CRAD 期刊收录，报道摘要与统计数据）[crad.ict.ac.cn](https://crad.ict.ac.cn/cn/article/Y2025/I3/790).  
- 宗学军等, "基于生成对抗网络的工控协议模糊测试研究" (GPFuzz 报道，ChinaAET 2024) — WGAN-GP + N-gram 在工业控制协议上的实证[ChinaAET 报道](https://www.chinaaet.com/article/3000166659).  
- 赵浩东, 康晓凤, 李慧, 等, "基于机器学习的模糊测试系统", Artificial Intelligence and Robotics Research (HansPub) 2025 — ML 指导 Havoc 调度与种子筛选的工程化报告（含 LibTIFF 对照实验）[pdf.hanspub.org](https://pdf.hanspub.org/airr2025142_102610569.pdf).  
- Rajpal M., Blum W., Singh R., "Not All Bytes Are Equal: Neural Byte Sieve for Fuzzing" (Neural-guided fuzzing ideas; 早期 ML+fuzz 工作，可作为技术来源).  
- She D., Pei K., Epstein D., et al., "NEUZZ: Efficient Fuzzing with Neural Program Smoothing", IEEE S&P 2019 — 神经平滑导引变异的先驱性工作（ML 与 fuzz 结合的经典参考）。  

（注：上文引用的 CHATAFL、CKGFuzzer、Understanding LLM-based drivers、GPFuzz、CBFuzzer 与 HansPub 报告均在 2022–2025 时间窗口内有公开论文/预印本或权威技术报道；AFLNet/PROFUZZBENCH/SmartGreybox/NEUZZ 等为被广泛用作基线或技术背景的已发表工作。读者若需逐篇原文与可复现实验脚本，建议从各文中给出的代码仓库或 PROFUZZBENCH 基准获取。）