引言  
并行与分布式计算（Parallel and Distributed Computing，PDC）在大模型训练、分布式图神经网络（GNN）、大规模数据预处理与推理系统中的作用日益凸显。本文聚焦 2022–2025 年间具有代表性的系统与算法进展，按方法类别精选每类 3–5 篇代表作，严格突出：研究问题、核心方法与关键实验结论。目标是为从事大规模机器学习系统、数据平台与分布式优化的研究者快速把握近三年内的实证与方法学走向。

方法分类与代表作  
1. 并行策略自动化与并行策略搜索（Parallelization planning / strategy search）  
- nnScaler (Microsoft Research, OSDI 2024)：研究问题是如何在海量并行策略空间中自动找出高效的训练并行组合。核心贡献是提出并行化原语（op-trans、op-assign、op-order）来统一表示并行策略，并用“专家约束”对搜索空间进行限定以提高搜索效率。实验在若干 Transformer / LLM 训练任务上表明，在限定搜索空间的前提下可获得与人工设计相当或更优的并行计划，且搜索速度可提升约 10×。该工作展示了用可组合原语表征并联策略并借助经验约束进行高效搜索的可行性。[microsoft.com](https://www.microsoft.com/en-us/research/articles/nnscaler/?locale=zh-cn)

- AdaptDNN (Adaptation for elastic/spot instances, CRAD 2025)：针对云上弹性实例（spot/抢占实例）训练的不稳定性，提出在弹性实例宽限期内做进度备份并动态调整并行策略以消除瓶颈。系统设计结合“利用宽限期的轻量冗余”与“瓶颈感知的并行策略切换”以在实例被回收时减少重启代价。实验在弹性集群情形显示，相较传统检查点或固定冗余方案，AdaptDNN 在平均成本下降明显的同时，训练时间延长受控（即在低成本容错与训练效率间取得较好折中）。[crad.ict.ac.cn](https://crad.ict.ac.cn/article/doi/10.7544/issn1000-1239.202440560)

- Pipeline model-parallelism survey (JCST 2024)：综述式工作分析流水线并行（pipeline parallelism）的三大挑战（调度、负载均衡、降低计算/通信/存储开销），并对同步与异步流水线调度、负载均衡技术与开销优化做系统分类。其价值在于把分散文献归一化为可比较的指标与设计要点，为并行策略自动化（如 nnScaler 类系统）提供可验证的约束与评价准则。结论指出：高效流水线设计必须同时权衡收敛性与吞吐，并依赖于动态调度与体系结构协同。该综述为并行策略搜索与自动化工具提供理论与工程上的评估基线。[jcst.ict.ac.cn](https://jcst.ict.ac.cn/cn/article/doi/10.1007/s11390-024-3872-3)

2. 张量/模型并行与高效算子实现（Tensor/model parallelism & operator optimizations）  
- PyTorch 张量并行教程（张量并行 + FSDP 实践指南，文档/教程 2024–2025）：该实践性文档详细说明了张量并行（TP）、序列并行（SP）、损失并行与与 FSDP 结合的二维 DeviceMesh 设计要点。重点在工程原语（ColwiseParallel、RowwiseParallel、SequenceParallel 等）与通信模式的配合，示范了在数百甚至上千 GPU 上可行的分块策略与通信划分。实验与示例强调：在大规模训练时，TP 与 FSDP 的组合能有效控制延迟与内存瓶颈，是可扩展训练的工程基石。（官方教程提供了可复现的配置与代码路径，为研究者部署多维并行提供操作级参考。）[docs.pytorch.ac.cn](https://docs.pytorch.ac.cn/tutorials/intermediate/TP_tutorial.html)

- FlashAttention (Tri Dao et al., 2022, arXiv)：研究问题是 Transformer 中自注意力（Attention）在 I/O 与内存方面的瓶颈。提出 IO-awareness 的块化注意力实现（FlashAttention），通过重排计算与显式内存访问优化实现对注意力的精确、低内存实现。实验在多种模型与硬件上给出：在相同数值精度下，FlashAttention 实现显著的运行时间加速与显存节约（尤其在长序列场景），从而使更大上下文长度的训练/推理成为可能。该方法成为随后高效注意力与长序列处理工作的重要基线。（参见 arXiv。）[arxiv.org](https://arxiv.org/abs/2205.14135)

- Pipeline / sequence parallel combined designs（参见 JCST survey 与 PyTorch 教程）：这些工作共同指出在 Transformer block 内部采用张量并行与序列并行的混合（例如对 LayerNorm/RMSNorm 采用序列并行，而对 Linear 层采用行/列分片）能在内存与通信之间实现更优权衡。实验结论表明：在超大模型时单一并行范式（仅 FSDP 或仅 TP）不能同时满足内存与延迟约束，必须采用二维或混合并行策略以延续扩展性（见 PyTorch 教程与流水线综述）。[docs.pytorch.ac.cn](https://docs.pytorch.ac.cn/tutorials/intermediate/TP_tutorial.html) [jcst.ict.ac.cn](https://jcst.ict.ac.cn/cn/article/doi/10.1007/s11390-024-3872-3)

3. 专用分布式训练系统与领域加速（Domain/system-specific distributed training）  
- ParGNN (分布式 GNN 全批次训练框架, DAC 2025)：针对全批次 GNN 的分布式训练负载不平衡与高通信开销，提出由负载均衡器驱动的自适应分区、子图流水线重叠通信与计算的系统设计。核心在于（1）基于划分的自适应负载均衡；（2）子图流水线算法实现通信与计算的重叠。实验对比 DGL 与 Pipe GCN，ParGNN 在达到目标精度所需时间上显著更短，且在不同拓扑与规模下保持更好的负载平衡与通信利用率（DAC 2025 收录）。[cnic.cas.cn](https://cnic.cas.cn/gzdt/202502/t20250228_7541544.html)

- vLLM / 高吞吐推理系统（vLLM 等，2023–2024 年发展的 LLM serving 系统）：研究问题是如何在推理阶段最大化 GPU/加速器利用率并降低延迟与上下文交换代价。典型方法包括批次拼接、激活缓存、内存调度与并发调度策略（例如基于流水线或分段的请求调度）。实验在大模型推理吞吐与延迟上表明：通过请求级别的调度与内存复用，可在减少 90% 以上的上下文切换成本或显著提升吞吐（相关系统实现与开源工程在 2023–2024 年被广泛采用）。（此类系统的工程细节与实验结果多见于系统论文与开源报告。）

4. 大规模数据处理与存储支持（Data processing & storage for LLM pipelines）  
- Data-Juicer 2.0（云规模自适应数据处理，项目文档与 arXiv 预印）：针对基础模型训练前的数据处理（数据清洗、去重、扩展、大规模 JSON 流式读取等），提出面向云的 Ray 模式扩展、子集分割策略、基于 MinHash-LSH 的并行去重与对 Arrow/JSON 的流式 I/O 补丁。关键实验显示：在数千到数万 CPU 核的集群上可在小时量级处理数十亿到数百亿样本，并在 PB 级去重任务上达到可操作的时间窗（例如 1280 核 3 小时处理 PB 级数据的实验报告）。该工作体现了数据预处理与分布式引擎（Ray）协同优化在基础模型数据准备中的必要性。[docs.rayai.org.cn](https://docs.rayai.org.cn/en/latest/ray-more-libs/data_juicer_distributed_data_processing.html)

- ScaleFS（CRAD 2025）：针对大模型场景下的海量文件与元数据管理问题，提出目录树元数据与属性元数据解耦、深广度平衡的目录树分区与细粒度元数据结构，并构建文件语义优化的键值元数据存储底座。实验在千亿级文件规模下比较 HDFS，ScaleFS 在每秒操作数（OPS）上高出 1.04–7.12×，并在延迟上显著优于 HDFS（延迟仅为 HDFS 的 12.67%–99.55%），在大规模文件管理与高并发元数据访问场景中显示出更好扩展性。该方向强调存储系统元数据层面的可扩展设计对大模型数据管道的基础支撑作用。[crad.ict.ac.cn](https://crad.ict.ac.cn/article/cstr/32373.14.issn1000-1239.202440373)

- 基于哈希增强的数据分片（AROC 2025）：在通用分布式系统的数据分片问题上，提出混合 LSH（MinHash + 自适应 LSH）与 meta-partitioning 的组合，通过逆块频率加权与双阶段剪边优化分片覆盖率与冗余。基准实验显示该方法在平均分片大小与最大分片规模上显著优于对比方法（平均分片大小下降约 58%），为分布式数据并行与去重提供更高质量的分片方案。[arocmag.cn](https://www.arocmag.cn/abs/2025.01.0018)

5. 去中心化 / 无等待通信的分布式学习（Decentralized / wait-free FL）  
- SWIFT (Wait-free decentralized FL, arXiv 2022)：提出无等待（wait-free）模型通信机制以避免受最慢节点拖慢的同步代价，理论证明在 convex/nonconvex 光滑优化下可达到与并行 SGD 相同的迭代收敛率 O(1/√T)。方法通过异步、去中心化的模型交流与更新协议消除了对 bounded-delay 假设的依赖。实证上在 IID 与非 IID 数据设置中，SWIFT 在运行时收敛速度比若干同步/异步基线快出 约 2×（或更高），并且通信开销在每 epoch 上下降一个数量级。该工作强调在异质网络环境下去中心化、无等待通信的可行性与效益。[arxiv.org](https://arxiv.org/abs/2210.14026)

实验与评价总结（共性结论，不逐篇复述）  
- 混合并行与多维并行已成为可扩展训练的常态。单一并行范式（仅数据并行或仅张量并行）在大模型/大 GPU 数量情形下难以同时满足内存、通信与延迟约束；因而混合 TP+FSDP+流水线的二维/三维并行设计更常见，且需精细化调度以减小通信阻塞（见 PyTorch 教程、流水线综述与 nnScaler 的动机）。[docs.pytorch.ac.cn](https://docs.pytorch.ac.cn/tutorials/intermediate/TP_tutorial.html) [jcst.ict.ac.cn](https://jcst.ict.ac.cn/cn/article/doi/10.1007/s11390-024-3872-3) [microsoft.com](https://www.microsoft.com/en-us/research/articles/nnscaler/?locale=zh-cn)

- I/O 与内存局限往往成为扩展瓶颈。算子级优化（如 FlashAttention）与元数据/存储层面的工程改进（如 ScaleFS）能够把系统瓶颈从单机内存与磁盘 I/O 推向网络与通信协调，从而显著扩展可处理的上下文长度与文件数量。[arxiv.org](https://arxiv.org/abs/2205.14135) [crad.ict.ac.cn](https://crad.ict.ac.cn/article/cstr/32373.14.issn1000-1239.202440373)

- 自动化策略搜索与经验约束的结合是提高并行策略实用性的有效路径。完全穷举搜索不可行，受专家约束的原语化搜索（nnScaler）或基于瓶颈识别的并行策略调整（AdaptDNN）在效率与效果上达到实用折中。系统设计需要可插拔的策略描述层与快速的成本模型以支持在线/离线搜索。[microsoft.com](https://www.microsoft.com/en-us/research/articles/nnscaler/?locale=zh-cn) [crad.ict.ac.cn](https://crad.ict.ac.cn/article/doi/10.7544/issn1000-1239.202440560)

- 应用与任务域细化（如 GNN、去重、数据清洗、推理服务）促生专用分布式算法与系统：GNN 的全批次训练需特殊的分区与流水线策略（ParGNN）；海量数据去重与预处理需要面向引擎的 I/O/分片优化（Data-Juicer）；推理系统需请求级调度与显存管理（vLLM / serving 系统）。这些专用系统在相应任务上带来数量级的效率改进，但其通用性依赖于可重用的中间件（通信库、流式 I/O、键值元数据层）。[cnic.cas.cn](https://cnic.cas.cn/gzdt/202502/t20250228_7541544.html) [docs.rayai.org.cn](https://docs.rayai.org.cn/en/latest/ray-more-libs/data_juicer_distributed_data_processing.html)

- 异质与不可靠资源环境（如弹性实例、异构加速器、去中心化客户端）要求系统具备适应性与容错机制：利用宽限期备份、无等待通信协议或动态并行策略切换已被证明在成本/效率/鲁棒性三者间可以取得更好的折中。 [crad.ict.ac.cn](https://crad.ict.ac.cn/article/doi/10.7544/issn1000-1239.202440560) [arxiv.org](https://arxiv.org/abs/2210.14026)

趋势与挑战（2025 年前后预测，≥3 点）  
1. 并行策略的可证收敛性与运行时成本模型将被统一。当前并行策略搜索多依赖启发或工程经验，未来研究将趋向把并行计划的性能成本模型（通信、内存、I/O）与优化收敛性分析联合起来，形成能在搜索中作约束的形式化评价指标，从而实现“搜索即保证”的自动化并行工具。证据：nnScaler 的原语化表征与流水线综述中对收敛性的强调。[microsoft.com](https://www.microsoft.com/en-us/research/articles/nnscaler/?locale=zh-cn) [jcst.ict.ac.cn](https://jcst.ict.ac.cn/cn/article/doi/10.1007/s11390-024-3872-3)

2. 存储/元数据层面成为大模型系统优化的必争之地。随着训练/推理时数据集规模与文件数量进入十亿—千亿级，像 ScaleFS 这样的元数据解耦、分区与键值化设计将成为基础设施标配，进而推动更多基于文件语义的存储优化（冷热分层、元数据缓存预取、近数据处理）。系统设计将更多关注元数据路径的低延迟与高并行访问。[crad.ict.ac.cn](https://crad.ict.ac.cn/article/cstr/32373.14.issn1000-1239.202440373)

3. 面向任务的专用并行/分布式算法会快速增长并走向工程化。GNN、MoE、长上下文 Transformer、去重/清洗流水线等都有各自独特瓶颈（通信模式、稀疏激活、I/O），需求将催生模块化、可插拔的系统组件（例如专家并行单元、MinHash-LSH 去重模块、流式 JSON 加载），以降低工程复用成本并提升跨任务可移植性。[cnic.cas.cn](https://cnic.cas.cn/gzdt/202502/t20250228_7541544.html) [docs.rayai.org.cn](https://docs.rayai.org.cn/en/latest/ray-more-libs/data_juicer_distributed_data_processing.html)

4. 异步/去中心化协议的实用化与安全性挑战并存。无等待通信（SWIFT）在异构/不可靠环境下能显著缩短实际运行时间，但同时带来了模型一致性、对抗鲁棒性与隐私泄露的新问题。预计未来两三年会有更多工作在无等待协议的收敛-鲁棒性-安全性三维度做形式化分析并提出加固策略。[arxiv.org](https://arxiv.org/abs/2210.14026)

5. 硬件-软件协同（near-data processing、CXL、PIM）将更频繁出现在分布式训练/推理的研究议程中。尤其在 MoE / 稀疏激活与超大元数据访问场景下，单纯靠网络与 GPU 通信难以满足吞吐-能效需求，近存算与异构内存访问将被用作突破口（尽管工程化成本高）。（参考 MoE 推理与硬件共设计趋势综述。）[zhuanzhi.ai](https://www.zhuanzhi.ai/vip/51658d2323f66f726b47fe456798addf)

结论  
2022–2025 年间，PDC 在大模型训练与推理、专业化分布式训练（如 GNN）与海量数据处理领域展示了迅速的系统与算法协同进展。关键共识为：单一并行范式不再足够，必须在算子、并行策略、存储元数据与容错机制之间实现跨层协同；同时自动化并行策略搜索、I/O/内存感知算子优化与任务定制化系统将是下一阶段的研究主线。面向 2025 年后的研究，应着力于把并行计划的性能建模与收敛性保证结合起来，并在元数据与硬件-软件协同上做工程级突破。

参考文献（按文中出现顺序，均为真实公开文献 / 系统文档 / 会议/期刊报道）  
- nnScaler: Constraint-Guided Parallelization Plan Generation for Deep Learning Training (Microsoft Research, OSDI 2024 coverage / project page). [microsoft.com](https://www.microsoft.com/en-us/research/articles/nnscaler/?locale=zh-cn)  
- ScaleFS: 面向大语言模型的高性能可扩展元数据设计 (CRAD, 2025). [crad.ict.ac.cn](https://crad.ict.ac.cn/article/cstr/32373.14.issn1000-1239.202440373)  
- ParGNN: A Scalable Graph Neural Network Training Framework on multi-GPUs (DAC 2025 acceptance report). [cnic.cas.cn](https://cnic.cas.cn/gzdt/202502/t20250228_7541544.html)  
- AdaptDNN: 一个自适应可伸缩的大模型分布式训练系统 (CRAD, 2025). [crad.ict.ac.cn](https://crad.ict.ac.cn/article/doi/10.7544/issn1000-1239.202440560)  
- Advances of Pipeline Model Parallelism for Deep Learning Training: An Overview (JCST, 2024). [jcst.ict.ac.cn](https://jcst.ict.ac.cn/cn/article/doi/10.1007/s11390-024-3872-3)  
- Large Scale Transformer model training with Tensor Parallel (PyTorch tutorial / docs, 2024–2025). [docs.pytorch.ac.cn](https://docs.pytorch.ac.cn/tutorials/intermediate/TP_tutorial.html)  
- FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness (Tri Dao et al., 2022, arXiv). [arxiv.org](https://arxiv.org/abs/2205.14135)  
- Data-Juicer 2.0: 云规模自适应数据处理（项目文档与预印材料）— Ray 模式实现与大规模去重实验（文档与 arXiv 预印资料）。 [docs.rayai.org.cn](https://docs.rayai.org.cn/en/latest/ray-more-libs/data_juicer_distributed_data_processing.html)  
- 基于哈希增强技术的分布式系统数据分片方案 (《计算机应用研究》/AROC, 2025). [arocmag.cn](https://www.arocmag.cn/abs/2025.01.0018)  
- SWIFT: Rapid Decentralized Federated Learning via Wait-Free Model Communication (arXiv 2210.14026, 2022). [arxiv.org](https://arxiv.org/abs/2210.14026)  
-（补充阅读）vLLM / LLM serving 系统开发报告与 arXiv/开源实现（2023–2024，多项系统实现与技术报告，见各项目仓库与预印本）——供工程参考。  
-（补充阅读）混合专家（MoE）模型推理优化综述与硬件/软件协同方向综述（近年综述与技术报告合集，参见相关综述页面与资料库）。 [zhuanzhi.ai](https://www.zhuanzhi.ai/vip/51658d2323f66f726b47fe456798addf)

（注）文中所引用的系统/文章均基于公开的会议/期刊报道、机构技术报告或 arXiv 预印件；文内链接指向可查证的原始资料或机构发布页，便于读者进一步获取实现细节与实验数据。