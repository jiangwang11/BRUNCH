协议模糊测试技术与应用研究综述 (2022–2025)
1. 引言
网络协议作为现代数字基础设施的神经系统，承载着全球范围内的数据交换与指令控制功能。从底层的传输控制协议到应用层的复杂业务交互，协议实现的安全性直接关系到互联网、工业控制系统（ICS）、物联网（IoT）以及第五代移动通信（5G）网络的稳定运行。协议模糊测试（Protocol Fuzzing）作为一种自动化的漏洞挖掘技术，通过向目标协议实现发送大量畸形或意外的输入数据，旨在触发内存破坏、逻辑错误或状态机异常，从而发现潜在的安全威胁。与针对文件处理程序的传统模糊测试不同，协议模糊测试面临着更为严峻的挑战：协议不仅具有高度结构化的数据包格式，更本质地表现为反应系统（Reactive Systems），其行为依赖于复杂的内部状态机与时序交互。

在2022年之前，协议模糊测试主要依赖于基于生成的（Generation-based）方法，即依据预定义的协议规范（Specification）构建测试用例，或基于变异的（Mutation-based）灰盒方法，如AFLNet，试图通过代码覆盖率反馈来盲目探索状态空间。然而，随着协议复杂度的指数级增长（如QUIC的加密握手、5G核心网的服务化架构），传统方法逐渐显露出瓶颈。一方面，基于规范的方法高度依赖专家人工建模，难以应对私有协议或实现偏离规范的情况；另一方面，传统的覆盖率引导机制在面对深层状态逻辑时，往往因无法生成正确的状态序列而陷入“覆盖率高原”（Coverage Plateau），难以触达核心业务逻辑。

2022年至2025年间，学术界在协议模糊测试领域取得了突破性进展。研究重心从单纯的吞吐量提升转向了深层状态空间的智能探索与语义感知的输入生成。这一时期涌现了三大核心技术趋势：一是状态感知与序列导向技术的深化，通过推断状态机或优化报文序列来维持长会话交互；二是大语言模型（LLM）的深度融合，利用生成式人工智能理解复杂的RFC文档、生成高语义有效性的种子，并作为智能代理打破变异僵局；三是特定领域的定制化突破，针对5G、加密流量及工业控制协议的特性设计专用的反馈机制（如侧信道分析）。

本文旨在对2022–2025年间协议模糊测试领域的代表性研究成果进行系统性综述。文章将深入剖析各技术流派的核心思想、关键方法及实验结论，并通过横向对比揭示不同技术路线的优势与局限。此外，本文还将结合最新的实验数据，总结当前技术在漏洞挖掘能力上的共性表现，并对2025年后的研究趋势——包括代理式模糊测试（Agentic Fuzzing）、多模态信号测试及自动化形式验证——进行前瞻性预测。

2. 方法分类与代表性工作
本章将近三年的前沿工作划分为三个主要类别：状态感知与序列导向模糊测试、大模型辅助的协议模糊测试、以及特定领域与侧信道模糊测试。每个类别选取最具代表性的3–5篇顶会/顶刊论文进行深入解读。

2.1 状态感知与序列导向模糊测试 (State-Aware & Sequence-Oriented Fuzzing)
协议交互本质上是状态驱动的。传统Fuzzer往往将协议交互视为孤立的数据包发送过程，忽略了上下文依赖，导致大量测试用例因状态不匹配而被目标系统早期丢弃。该类研究致力于解决“如何生成能够深入协议状态机的有效序列”这一核心问题。

Bleem: Packet Sequence Oriented Fuzzing for Protocol Implementations (USENIX Security 2023)
研究问题：现有的协议Fuzzer多聚焦于单个数据包的生成与变异，缺乏对长序列报文交互逻辑的有效维护，导致无法在有状态协议（如TLS、QUIC）中触发深层状态后的隐藏漏洞 。   

核心方法：Bleem提出了一种“面向报文序列”的黑盒模糊测试框架，它不依赖源码插桩，而是通过非侵入式地分析系统输出序列（即响应报文序列）来推断状态反馈，并引入了“状态空间追踪”机制。该机制动态构建并维护一个状态图，利用交互式流量信息指导变异策略，优先选择能拓展状态转换路径的序列进行变异，而非仅仅关注代码覆盖率。

关键实验结论：在OpenSSL、Quic-go等15个广泛使用的协议实现上，Bleem在24小时内的分支覆盖率比现有最先进工具（如Peach、AFLNet）提升了高达174.93%，并成功挖掘出15个安全关键漏洞，其中10个被分配了CVE编号 。   

StateFuzz: System Call-Based State-Aware Linux Driver Fuzzing (USENIX Security 2022)
研究问题：传统的覆盖率引导（Coverage-guided）策略倾向于探索新的代码行，但往往忽略了“同一代码在不同内部状态下”可能触发不同行为的场景，导致状态机探索不充分，难以发现逻辑竞态或状态混淆漏洞 。   

核心方法：StateFuzz提出了一种基于三维反馈机制（代码覆盖、状态变量值、状态转换）的灰盒测试方法。它首先通过静态分析自动识别驱动程序中的关键状态变量（如枚举类型、标志位），然后通过轻量级插桩在运行时追踪这些变量的值变化，结合系统调用序列推断状态转换，从而优先调度那些能触发新状态组合的测试用例。

关键实验结论：在Linux内核驱动程序的测试中，StateFuzz比基准工具Syzkaller多发现了32%的状态覆盖和19%的代码覆盖，并发现了18个未知漏洞，证明了状态维度反馈在复杂驱动协议测试中的有效性 。   

Logos: Log Guided Fuzzing for Protocol Implementations (ISSTA 2024)
研究问题：传统的灰盒测试依赖源码插桩获取反馈，而纯黑盒测试缺乏指导效率低下。在许多商业或工业场景中，协议实现源码不可得，但系统会产生丰富的运行时日志，现有工具未能有效利用这些非结构化日志作为模糊测试的反馈信号 。   

核心方法：Logos提出了一种利用非侵入式运行时日志进行模糊测试引导的新范式。它首先将非结构化的文本日志标准化，并利用自然语言处理技术将其嵌入到高维向量空间中进行语义表示（Semantic Representation）。通过计算日志向量之间的距离，Logos动态维护一个“语义覆盖率”指标，以此量化测试用例对协议逻辑的探索程度，并指导种子调度。

关键实验结论：在8个广泛使用的协议实现（包括Live555、Dnsmasq等）上，Logos在24小时内比现有的非侵入式或专家知识驱动的Fuzzer（如NSFuzz）提高了26.75%–106.19%的分支覆盖率，并发现了12个安全关键漏洞 。   

2.2 大模型辅助的协议模糊测试 (LLM-Assisted Protocol Fuzzing)
自2023年起，大语言模型（LLM）的引入彻底改变了协议模糊测试的格局。LLM不仅具备强大的代码理解与生成能力，还能从自然语言规范（如RFC文档）中提取结构化知识，弥补了传统Fuzzer在语义理解上的先天不足。

ChatAFL: Large Language Model Guided Protocol Fuzzing (NDSS 2024)
研究问题：传统灰盒Fuzzer难以生成符合复杂语法结构的高质量种子，且在遇到覆盖率瓶颈（Plateau）时，由于缺乏对协议状态机语义的理解，无法生成特定的握手序列来突破状态停滞 。   

核心方法：ChatAFL构建了一个LLM引导的混合模糊测试引擎。它利用LLM从RFC文档中提取协议的机器可读语法（Grammar）以构建结构化变异器，并在Fuzzer检测到覆盖率增长停滞时，通过与LLM的多轮对话，将当前的客户端-服务端交互历史作为上下文，请求LLM预测并生成能够触发新状态转换的后续消息序列。

关键实验结论：在ProFuzzBench基准测试中，ChatAFL的状态转换覆盖率比基线AFLNet高出50%，状态覆盖率高出30%，并发现了9个AFLNet和NSFuzz未能发现的独特漏洞，展示了LLM在打破状态探索僵局方面的巨大潜力 。   

PSG: Enhancing Protocol Fuzzing via Diverse Seed Corpus Generation (CCS 2024 / TSE 2025)
研究问题：初始种子语料库的质量直接决定了Fuzzer的起步效能，但现有的种子生成方法往往导致种子多样性不足（受限于捕获的流量），且手动构建协议语法的成本极高，限制了Fuzzer对复杂协议特性的覆盖 。   

核心方法：PSG提出了一种利用LLM处理海量协议RFC文档，自动生成多样化且符合规范的种子语料库的方法。它引入了一种无需显式语法的生成策略，并通过“迭代细化”（Iterative Refinement）机制，利用目标服务器返回的有限错误反馈（如错误码）来修正LLM生成的无效消息，从而在无需人工干预的情况下显著提高种子的通过率和语义多样性。

关键实验结论：在7个广泛使用的协议（如BGP、RTSP）上，PSG生成的语料库显著提升了AFLNet等现有Fuzzer的性能，帮助发现了多个被现有工具遗漏的零日漏洞（Zero-day bugs），且生成的语料库具有跨实现复用的能力 。   

G2Fuzz: Grammar-Aware Fuzzing with LLM-Synthesized Input Generators (USENIX Security 2025)
研究问题：虽然LLM擅长生成文本，但在直接生成复杂的非文本（二进制）输入（如PDF、图像或压缩协议数据）时往往效率低下，且难以大规模并行化，这限制了其在二进制协议测试中的应用 。   

核心方法：G2Fuzz提出了一种“生成器合成”策略：它不直接让LLM生成测试用例，而是提示LLM编写并变异能够产生符合特定格式数据的Python脚本（Input Generators）。这些脚本一旦生成，就能高效地批量生产符合复杂语法的二进制数据。随后，G2Fuzz结合AFL++对这些生成器产出的数据进行传统的位级变异，形成“整体搜索”（LLM优化生成器逻辑）与“局部搜索”（Fuzzer优化数据细节）的混合策略。

关键实验结论：在34种复杂输入格式（包括图像格式和视频流协议）的测试中，G2Fuzz在代码覆盖率和漏洞发现能力上均优于AFL++、Fuzztruction等SOTA工具，且大幅降低了对LLM推理接口的调用频率和成本 。   

2.3 特定领域与侧信道模糊测试 (Domain-Specific & Side-Channel Fuzzing)
通用Fuzzer在面对具有特殊架构或安全机制的领域（如5G、加密通信、工业控制）时往往失效。该类研究通过结合领域知识（Domain Knowledge）和侧信道反馈，解决了特定场景下的不可达性问题。

CoreCrisis: Threat-Guided and Context-Aware Iterative Learning and Fuzzing of 5G Core Networks (USENIX Security 2025)
研究问题：5G核心网（5GC）采用微服务架构（SBA），各网元间通过REST API交互，逻辑极其复杂且状态空间庞大。现有的状态分析工具多依赖静态输入，仅能发现浅层逻辑错误，难以挖掘导致核心网崩溃或拒绝服务的深层实现漏洞 。   

核心方法：CoreCrisis采用动态两阶段方法。首先，利用分治法和属性驱动的等价性检查，仅使用良性输入构建5GC实现的初始有限状态机（FSM），以解决状态空间爆炸问题。其次，在Fuzzing阶段，它利用学习到的FSM定位未探索状态，并引入“威胁引导”（Threat-Guided）的变异策略，专门生成针对特定信令流程的攻击性输入，并根据网络响应不断精炼FSM模型。

关键实验结论：在Open5GS等开源及商业5GC实现中，CoreCrisis发现了7类规范偏差和13个导致崩溃的严重漏洞，涉及拒绝服务、认证绕过和计费欺诈等关键安全问题，验证了威胁模型引导在电信协议测试中的必要性 。   

SAECRED: A State-Aware, Over-the-Air Protocol Testing Approach for SAE Handshake (AsiaCCS 2024 / SP 2025 Pipeline)
研究问题：WPA3引入的SAE（Simultaneous Authentication of Equals）握手协议旨在防止密码猜测攻击，但其引入了变长结构和上下文敏感的复杂数学运算，极易出现解析错误。现有的Wi-Fi Fuzzer缺乏对SAE复杂状态机和加密约束的感知，难以穿透握手初期阶段 。   

核心方法：SAECRED将SAE握手漏洞的挖掘转化为一个二维搜索问题（数据包结构维度 + 协议状态维度）。它结合了迭代加深搜索（IDS）与上下文敏感的语法模糊测试，利用语法制导合成（SyGuS）求解器辅助生成满足SAE加密约束的复杂握手包。通过这种方式，SAECRED能够在黑盒条件下精准控制协议状态流转，覆盖从连接初始化到密钥确认的全过程。

关键实验结论：在6款商用现货（COTS）Wi-Fi接入点和hostapd上，SAECRED发现了多类漏洞，包括可导致降级攻击（Downgrade Attack）和拒绝服务攻击的严重缺陷，证明了形式化约束求解在加密握手协议测试中的有效性 。   

Fuzztruction-Net: Network Application Fuzzing via Fault Injection (CCS 2024)
研究问题：许多网络应用（如SSH客户端、TLS服务器）涉及加密或专有协议，传统的源码插桩难以穿透加密层（导致覆盖率反馈失效），且现有的黑盒工具缺乏内部执行状态反馈，难以指导变异方向 。   

核心方法：Fuzztruction-Net扩展了基于故障注入的模糊测试技术。它不依赖源码插桩，而是通过在运行时动态注入故障（如比特翻转、指令跳过）来观察程序的崩溃或行为差异，以此作为侧信道来推断执行路径并引导变异。该工具特别设计了针对网络交互的同步机制，支持对服务端和客户端的双向模糊测试。

关键实验结论：在Nginx、OpenSSH、ngtcp2（QUIC库）等成熟且久经测试的软件中，Fuzztruction-Net发现了23个远程可触发的新漏洞，证明了故障注入作为侧信道反馈在突破加密协议测试盲区方面的巨大潜力 。   

MSGFuzzer: Message Sequence Guided Industrial Robot Protocol Fuzzing (ICST 2024)
研究问题：工业机器人协议通常具有严格的时序约束和专有的消息格式，通用的网络Fuzzer难以生成符合工业控制逻辑的消息序列，导致测试往往被拒绝在协议栈入口 。   

核心方法：MSGFuzzer提出了一种消息序列引导的策略。它基于消息字节特征过滤原始流量，构建最小化的有效消息序列集，并通过分析工业机器人的实时反馈来区分每条消息的序列约束。该方法利用变异策略在保持序列合法性的前提下探索边界条件。

关键实验结论：在真实工业机器人系统上的评估显示，MSGFuzzer发现了12个唯一的崩溃漏洞，其崩溃发现效率比现有最先进的协议Fuzzer高出至少71.4%，揭示了工业控制系统中存在的严重安全隐患 。   

3. 实验与评价总结
综合上述2022–2025年的研究工作，本章从覆盖率提升、漏洞挖掘能力以及资源开销三个维度，对不同技术流派的实验结果进行横向比较与总结。

3.1 覆盖率评价 (Code & State Coverage Analysis)
覆盖率是衡量Fuzzer探索能力的核心指标。近三年的研究表明，单纯的代码覆盖率已不足以评估协议测试的充分性，状态覆盖率（State Coverage）和状态转换覆盖率（Transition Coverage）成为新的评价标准。

表 3-1: 不同技术流派在覆盖率提升上的相对表现（基于基准对比）

技术类别	代表工具	对比基线	覆盖率提升幅度 (平均)	关键洞察
状态/序列导向	
Bleem 

Peach / AFLNet	分支覆盖率 +174.93%	序列导向能有效维持长连接，从而触达深层逻辑代码。
状态/序列导向	
StateFuzz 

Syzkaller	状态覆盖率 +32%	引入状态变量反馈后，Fuzzer倾向于在同一代码路径上探索不同的数据状态组合。
LLM辅助	
ChatAFL 

AFLNet / NSFuzz	状态转换 +50%	LLM的语义理解能力帮助Fuzzer生成了正确的握手后续报文，突破了状态机瓶颈。
非侵入式反馈	
Logos 

NSFuzz	分支覆盖率 +26% ~ 106%	基于日志语义的反馈在无源码环境下能达到甚至超过部分灰盒工具的效果。
  
共性结论：

语义智能突破瓶颈：实验数据一致显示，引入LLM（如ChatAFL, PSG）或领域知识（CoreCrisis）后，覆盖率尤其是状态层面的覆盖率有质的飞跃。这表明传统随机变异在面对协议这种强结构化数据时存在理论上限，必须引入外部语义信息（RFC、日志、LLM知识）来打破。

多维反馈优于单一维度：StateFuzz和Bleem的成功证明，在代码覆盖率之外增加“状态”维度（State Dimension）的反馈，能显著提高测试的深度。仅追求代码行覆盖可能会遗漏大量因状态机逻辑错误导致的漏洞。

3.2 漏洞挖掘能力 (Vulnerability Discovery)
漏洞挖掘的实战成果是检验工具价值的最终标准。这一时期的研究发现了大量传统工具遗漏的深层漏洞。

表 3-2: 代表性工具发现的漏洞类型分布

工具名称	目标协议类型	发现漏洞总数	主要漏洞类型	关键发现
CoreCrisis 

5G Core (SBA)	13 (Crash)	逻辑错误、拒绝服务、计费欺诈	5G协议实现的复杂性导致逻辑一致性漏洞多于传统内存破坏。
SAECRED 

WPA3 (Wi-Fi)	多个类别	降级攻击、DoS、解析错误	即使是经过形式化验证的协议标准，其商业实现中仍存在解析逻辑缺陷。
Fuzztruction-Net 

SSH/TLS/QUIC	23	内存破坏、未初始化读取	成熟的加密协议实现中仍存在可以通过故障注入触发的深层漏洞。
Matter Fuzzer 

IoT (Matter)	147	非崩溃型逻辑Bug、死锁	新兴的IoT标准（如Matter）实现成熟度低，存在大量功能性与逻辑性缺陷。
  
共性结论：

逻辑漏洞占比显著上升：随着内存安全语言（如Rust、Go在QUIC和5G中的应用）的普及，以及Fuzzer能力的提升，单纯的缓冲区溢出（Buffer Overflow）占比下降，而协议逻辑漏洞（如状态机死锁、认证绕过、降级攻击、重放攻击）成为挖掘重点。特别是在5G和IoT领域，非崩溃型Bug（Non-crash bugs）占据了主导地位。

实现复杂性是漏洞温床：CoreCrisis和SAECRED的研究均表明，协议规范越复杂（如涉及复杂加密握手或微服务交互），其实现出现偏差的概率越高。标准文档（Specification）与代码实现之间的“语义鸿沟”是主要风险源。

3.3 效率与开销评价
LLM的时间/资源权衡：虽然LLM辅助能显著提高覆盖率，但也引入了推理延迟。G2Fuzz的研究指出，直接请求LLM生成每一个测试用例是不经济且低效的。采用“LLM生成生成器（Generator）”+“传统Fuzzer高频变异”的混合模式，能够将Token消耗降低数个数量级，同时保持每秒执行次数（Execs/sec）在较高水平 。   

黑盒反馈的代价：Logos和Bleem证明了黑盒方法的可行性，但其吞吐量通常低于基于共享内存插桩的AFL++。然而，在无法获取源码的商业设备测试中，这是唯一可行的路径，且其发现的漏洞价值往往更高。

4. 趋势与挑战 (2025年前后趋势预测)
基于当前文献的演进脉络，协议模糊测试正处于从“自动化”向“自主化”跨越的关键时期。以下是对2025年后研究趋势的预测：

4.1 趋势一：代理式模糊测试 (Agentic Fuzzing) 的全面兴起
目前的LLM应用多停留在“辅助角色”（生成种子、解释Crash）。未来，Fuzzer将进化为全功能的自主智能体（Autonomous Agents）。这类Agent不仅能生成数据，还能像人类安全专家一样：

自主规划：根据当前的覆盖率热图，自主决定下一步是继续Fuzz当前状态，还是尝试触发特定的状态迁移 。   

工具链编排：自主编写测试桩（Harness），配置编译选项，甚至在发现异常后自主调用调试器（GDB）进行根本原因分析（Root Cause Analysis）。PBFuzz  等早期工作已经展现了Agent在推断输入约束和规划多步攻击路径上的雏形。   

4.2 趋势二：从纯数据向多模态与物理层信号渗透
现有的协议Fuzzing主要集中在OSI模型的应用层和传输层（数据包）。随着6G通信、自动驾驶和工业互联网的发展，未来的Fuzzer将向物理层/链路层下沉。

多模态输入：在车联网场景中，协议数据往往与传感器信号（雷达、视觉）强耦合。未来的Fuzzer需要具备生成和变异“数字化的物理信号”（如无线电波形数据、CAN总线时序信号）的能力 。   

跨层测试：结合软件定义无线电（SDR）技术，实现从射频信号干扰到上层协议逻辑崩溃的跨层穿透测试。

4.3 趋势三：规范自动形式化与全自动Harness生成
当前Fuzzing的一大瓶颈是人工编写Harness和建立协议模型。PSG  和Hermes  等工作展示了从自然语言文档到形式化模型的转化潜力。   

文档即Fuzzer：预计到2025年，将出现能够直接输入数千页的PDF技术规范（如3GPP标准），自动提取状态机、报文约束，并生成可编译运行的Fuzzer的端到端系统。这将彻底解决5G/6G等超大规模协议测试的门槛问题。

4.4 趋势四：持续学习与长期记忆 (Long-term Memory)
当前的Fuzzer每次运行都是“从零开始”。未来的系统将具备长期记忆能力，能够在数周甚至数月的持续集成测试中，积累对目标协议行为的理解。利用向量数据库存储历史测试中的有效序列和状态转换图，实现跨版本、跨设备的知识迁移（Transfer Learning）。

5. 结论
2022至2025年是协议模糊测试技术发生质变的三年。面对协议实现的日益复杂化和状态空间的爆炸式增长，学术界通过引入状态感知、大模型语义理解以及领域特定反馈，成功突破了传统覆盖率引导方法的局限。

状态与序列导向（Bleem, StateFuzz）确立了在时序维度上进行深层探索的方法论，证明了维持长会话对于挖掘逻辑漏洞至关重要。

大模型辅助（ChatAFL, PSG, G2Fuzz）则展示了生成式AI在理解协议规范、打破覆盖率高原以及自动化工具构建方面的革命性潜力，特别是混合模式（Hybrid Mode）成为了平衡智能与效率的标准范式。

特定领域研究（CoreCrisis, SAECRED, Fuzztruction-Net）揭示了在5G、加密通信和工业控制等高价值目标中，结合威胁模型和侧信道反馈是发现深层漏洞的必由之路。

展望未来，随着Agentic AI的成熟和多模态交互需求的增加，协议模糊测试将不再仅仅是一个测试工具，而将演变为具备自主学习、自主规划能力的“虚拟安全专家”。这一领域的持续进步，将为构建更安全、更健壮的下一代互联网基础设施提供坚实保障。

6. 参考文献
 A. Roychoudhury, “Protocol Fuzzing,” in Proceedings of the 31st USENIX Security Symposium, 2022.  R. Meng, M. Mirchev, M. Böhme, and A. Roychoudhury, “Large language model guided protocol fuzzing (ChatAFL),” in Proceedings of the 31st Annual Network and Distributed System Security Symposium (NDSS), 2024.  R. Meng, et al., “ChatAFL: Large Language Model Guided Protocol Fuzzing,” in NDSS, 2024.  Z. Luo, J. Yu, F. Zuo, J. Liu, Y. Jiang, T. Chen, A. Roychoudhury, and J. Sun, “Bleem: Packet Sequence Oriented Fuzzing for Protocol Implementations,” in 32nd USENIX Security Symposium, 2023.  Y. Dong, T. Yang, A. A. Ishtiaq, et al., “CoreCrisis: Threat-Guided and Context-Aware Iterative Learning and Fuzzing of 5G Core Networks,” in 34th USENIX Security Symposium, 2025.  F. Wu, Z. Luo, Y. Zhao, Q. Du, J. Yu, R. Peng, H. Shi, and Y. Jiang, “Logos: Log Guided Fuzzing for Protocol Implementations,” in Proceedings of the 33rd ACM SIGSOFT International Symposium on Software Testing and Analysis (ISSTA), 2024.  D. P. Dar, R. Lorch, and A. Sadeghi, “SAECRED: A State-Aware, Over-the-Air Protocol Testing Approach for Discovering Parsing Bugs in SAE Handshake Implementations of COTS Wi-Fi Access Points,” in Proceedings of the 19th ACM Asia Conference on Computer and Communications Security (AsiaCCS), 2024.  Y. Zhang, D. Fang, P. Liu, et al., “MSGFuzzer: Message Sequence Guided Industrial Robot Protocol Fuzzing,” in 2024 IEEE Conference on Software Testing, Verification and Validation (ICST), 2024.  Z. Luo, Q. Du, Y. Wang, and Y. Jiang, “Enhancing Protocol Fuzzing via Diverse Seed Corpus Generation (PSG),” IEEE Transactions on Software Engineering (TSE), vol. 51, no. 9, pp. 2693-2709, 2025 (Presented at CCS 2024).  B. Zhao, Z. Li, S. Qin, Z. Ma, M. Yuan, W. Zhu, Z. Tian, and C. Zhang, “StateFuzz: System Call-Based State-Aware Linux Driver Fuzzing,” in 31st USENIX Security Symposium, 2022.  D. P. Dar, et al., “SAECRED: A State-Aware, Over-the-Air Protocol Testing Approach,” in AsiaCCS, 2024.  X. Ma, L. Luo, and Q. Zeng, “From One Thousand Pages of Specification to Unveiling Hidden Bugs: Large Language Model Assisted Fuzzing of Matter IoT Devices,” in 33rd USENIX Security Symposium, 2024.  K. Zhang, et al., “G2Fuzz: Grammar-Aware Fuzzing with LLM-Synthesized Input Generators,” in 34th USENIX Security Symposium, 2025.  “PBFuzz: Agentic Directed Fuzzing for PoV Generation,” arXiv preprint, 2025.  N. Bars, M. Schloegel, N. Schiller, L. Bernhard, and T. Holz, “No Peer, no Cry: Network Application Fuzzing via Fault Injection (Fuzztruction-Net),” in Proceedings of the 2024 ACM SIGSAC Conference on Computer and Communications Security (CCS), 2024.   


usenix.org
USENIX Security '23 Technical Sessions
在新窗口中打开

usenix.org
Bleem: Packet Sequence Oriented Fuzzing for Protocol Implementations - USENIX
在新窗口中打开

semanticscholar.org
Bleem: Packet Sequence Oriented Fuzzing for Protocol Implementations - Semantic Scholar
在新窗口中打开

usenix.org
StateFuzz: System Call-Based State-Aware Linux Driver Fuzzing - USENIX
在新窗口中打开

usenix.org
StateFuzz: System Call-Based State-Aware Linux Driver Fuzzing - USENIX
在新窗口中打开

wingtecher.com
Logos: Log Guided Fuzzing for Protocol Implementations - WingTecher
在新窗口中打开

conf.researchr.org
ISSTA/ECOOP 2024 Contributors - conf.researchr.org
在新窗口中打开

arxiv.org
A Survey of Protocol Fuzzing - arXiv
在新窗口中打开

researchgate.net
Logos: Log Guided Fuzzing for Protocol Implementations | Request PDF - ResearchGate
在新窗口中打开

ndss-symposium.org
Large Language Model guided Protocol Fuzzing - NDSS Symposium
在新窗口中打开

scribd.com
NDSS24-chatafl | PDF | Computing - Scribd
在新窗口中打开

abhikrc.com
Large Language Model guided Protocol Fuzzing - Abhik Roychoudhury
在新窗口中打开

ndss-symposium.org
NDSS Symposium 2024 Program
在新窗口中打开

abhikrc.com
Enhancing Protocol Fuzzing via Diverse Seed Corpus Generation - Abhik Roychoudhury
在新窗口中打开

computer.org
Enhancing Protocol Fuzzing via Diverse Seed Corpus Generation - IEEE Computer Society
在新窗口中打开

usenix.org
Low-Cost and Comprehensive Non-textual Input Fuzzing with LLM-Synthesized Input Generators - USENIX
在新窗口中打开

usenix.org
CoreCrisis: Threat-Guided and Context-Aware Iterative Learning and Fuzzing of 5G Core Networks - USENIX
在新窗口中打开

usenix.org
USENIX Security '25 Cycle 1 Accepted Papers
在新窗口中打开

usenix.org
USENIX Security '25 Technical Sessions
在新窗口中打开

figshare.com
Operator-Centric Strategies for Enhancing Performance and Reliability of Cloud-Native 5G Core and Wi-Fi Access Networks - Figshare
在新窗口中打开

papers.mathyvanhoef.com
SAECRED: A State-Aware, Over-the-Air Protocol Testing Approach for Discovering Parsing Bugs in SAE Handshake Implementations of COTS Wi-Fi Access Points - Publications
在新窗口中打开

mschloegel.me
No Peer, no Cry: Network Application Fuzzing via Fault Injection - Moritz Schloegel
在新窗口中打开

arxiv.org
No Peer, no Cry: Network Application Fuzzing via Fault Injection - arXiv
在新窗口中打开

researchgate.net
No Peer, no Cry: Network Application Fuzzing via Fault Injection - ResearchGate
在新窗口中打开

usenix.org
Fuzztruction: Using Fault Injection-based Fuzzing to Leverage Implicit Domain Knowledge - USENIX
在新窗口中打开

ieeexplore.ieee.org
MSGFuzzer: Message Sequence Guided Industrial Robot Protocol Fuzzing - IEEE Xplore
在新窗口中打开

semanticscholar.org
CNCFuzzer: Directed Blackbox Fuzzing of Computer Numerical Control System Based on Message Behaviour Guidance | Semantic Scholar
在新窗口中打开

usenix.org
From One Thousand Pages of Specification to Unveiling Hidden Bugs: Large Language Model Assisted Fuzzing of Matter IoT Devices - USENIX
在新窗口中打开

arxiv.org
PBFuzz: Agentic Directed Fuzzing for PoV Generation - arXiv
在新窗口中打开

researchgate.net
Large Language Model guided Protocol Fuzzing | Request PDF - ResearchGate
在新窗口中打开

arxiv.org
R1-Fuzz: Specializing Language Models for Textual Fuzzing via Reinforcement Learning
在新窗口中打开

usenix.org
Hermes: Unlocking Security Analysis of Cellular Network Protocols by Synthesizing Finite State Ma