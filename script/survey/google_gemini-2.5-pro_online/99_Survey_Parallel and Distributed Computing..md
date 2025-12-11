好的，遵照您的要求，我将扮演一位严谨的科研助手，基于提供的真实网络搜索结果，生成一篇关于并行与分布式计算在深度学习领域应用的学术综述。

***

### **面向大规模人工智能的并行与分布式计算技术进展 (2022–2025年)**

#### **摘要**
随着深度神经网络，尤其是大语言模型（LLM）的参数量呈指数级增长，单一计算设备已远无法满足其训练与推理的算力及内存需求。并行与分布式计算已成为驱动大规模人工智能发展的核心技术。本综述聚焦于 2022 年至 2025 年间，系统梳理并总结了并行与分布式计算在深度学习领域的代表性研究工作。本文从并行训练框架、分布式推理与服务、以及分布式系统与数据处理三个方面对前沿方法进行归类与剖析。最后，本文对该领域的共性实验结论进行综合评价，并对未来 2-3 年的潜在研究趋势与挑战进行了展望。

#### **1. 引言**
近年来，以 Transformer 架构为基础的大模型在自然语言处理、计算机视觉等领域取得了突破性进展。然而，模型的成功与其规模的急剧扩张相伴相生，带来了巨大的计算、内存和通信挑战 [syhya.github.io](https://syhya.github.io/zh/posts/2025-03-01-train-llm/)。为了突破单卡物理极限，学术界与工业界大力发展了各类并行与分布式计算技术，通过将计算任务、模型、数据有效切分至大规模计算集群，从而实现对巨型模型的有效训练和部署。这些技术已不再局限于传统的并行策略，而是向着自动化、全栈协同和适应异构环境的系统化方向演进。本综述旨在梳理此背景下近期的关键技术进展。

#### **2. 方法分类与代表作**
我们将近期研究进展划分为并行训练框架、分布式推理与服务、以及分布式系统与数据处理三大类。

##### **2.1 并行训练框架**
并行训练框架致力于通过高效的并行策略，提升大规模模型训练的速度和效率，解决训练过程中的算力、显存与负载均衡等核心问题。

*   **自动并行策略**
    *   **Alpa (OSDI '22)**: 该工作旨在解决手动设计并行策略的复杂性问题 [hliangzhao.cn](https://hliangzhao.cn/post/2022/12/13/osdi22-alpa/)。Alpa 提出了一种层次化方法，将并行策略分解为算子内并行（Intra-operator parallelism）和算子间并行（Inter-operator parallelism）。它通过整数线性规划和动态规划相结合的方式，自动发现并优化数据并行、算子并行和流水线并行的组合策略。实验表明，Alpa 能够为大型 Transformer 模型生成高效的并行执行计划，其性能可与甚至超越专家手动优化的方案。

*   **弹性与容错训练**
    *   **AdaptDNN (2025)**: 该研究针对云服务中价格低廉但随时可能被回收的弹性实例（Spot Instances），提出了训练稳定性的挑战 [crad.ict.ac.cn](https://crad.ict.ac.cn/article/doi/10.7544/issn1000-1239.202440560)。AdaptDNN 系统利用弹性实例被回收前的“宽限期”来高效备份训练进度，从而降低容错开销。同时，它采用“瓶颈消除”思想动态调整模型并行策略，以最大化利用集群中的可用资源。实验结果表明，该系统在实现低成本容错的同时，保证了高效的模型训练，有效降低了云上训练成本。

*   **面向特定模型的并行优化**
    *   **ParGNN (DAC '25)**: 分布式图神经网络（GNN）训练面临着严重的负载不均衡和高通信开销 [cnic.cas.cn](https://cnic.cas.cn/gzdt/202502/t20250228_7541544.html)。ParGNN 系统针对全批次（full-batch）GNN 训练设计，其核心是一种由负载均衡器指导的自适应负载均衡方法，并结合图过划分策略来缓解计算不均。此外，它通过一种新颖的子图流水线算法，实现了计算与通信过程的重叠。实验证明，相较于 DGL 和 PipeGCN 等方案，ParGNN 在保证最高训练精度的同时，能以最短时间达到目标精度。
    *   **流水线并行（综述性进展）**: 流水线并行是训练大模型的核心技术之一，但面临流水线调度、负载均衡和通信开销三大挑战 [jcst.ict.ac.cn](https://jcst.ict.ac.cn/cn/article/doi/10.1007/s11390-024-3872-3)。近期研究通过微批次（micro-batch）调度、1F1B（One-Forward-One-Backward）等异步调度策略减少流水线“气泡”，提升设备利用率。同时，研究工作也关注如何结合体系结构特征，在计算、存储和通信三者间取得平衡，以充分发挥硬件性能。

##### **2.2 分布式推理与服务**
随着大模型应用的普及，在资源受限或去中心化环境下提供低延迟、高吞吐的推理服务成为新的研究热点。

*   **去中心化服务网络**
    *   **GenTorrent (2025)**: 该研究旨在解决小型组织和个人部署与测试大语言模型时面临的可扩展性挑战 [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/133183)。受 P2P 网络的启发，GenTorrent 提出一种利用去中心化贡献者计算资源的 LLM 服务覆盖网络。研究系统性地探讨了覆盖网络组织、通信隐私、资源效率和验证服务质量四个关键问题。原型系统实验表明，与无覆盖转发的基线相比，GenTorrent 实现了超过 50% 的延迟降低，且安全特性对性能影响微乎其微。

*   **边缘与无线环境下的推理**
    *   **基于 AirComp 的分布式 CNN 推理 (2025)**: 传统空中计算（AirComp）在分布式推理中因信号相位对齐问题导致精度下降，尤其在低信噪比下 [jeit.ac.cn](https://jeit.ac.cn/cn/article/doi/10.11999/JEIT241022?viewType=HTML)。该研究提出了 MOSI-AirComp 系统，通过让同一轮计算的发射信号源自同一节点来规避相位对齐问题。其设计的双支路训练模型能模拟并抵抗信道干扰，并结合基于权重的功率控制方案实现“空中卷积”。仿真结果显示，在小尺度衰落场景下，该方法将 MNIST 和 CIFAR-10 的推理精度分别提升了 2%–18% 和 0.4%–11.2%。

*   **推理存储优化**
    *   **大语言模型推理存储优化（综述性进展）**: LLM 推理面临由庞大模型参数和键值缓存（KV Cache）带来的严峻存储挑战 [crad.ict.ac.cn](https://crad.ict.ac.cn/article/doi/10.7544/issn1000-1239.202440628?viewType=HTML)。近期优化技术主要围绕三方面展开：一是显存优化，通过高效 KV 缓存管理、压缩和注意力算子优化来降低显存占用；二是异构存储，利用多级存储（如CPU内存、NVMe）扩展容量，并通过智能放置与预取降低 I/O 开销；三是分布式存储，通过批处理、多级调度和冗余策略优化多机资源利用和容错能力。

##### **2.3 分布式系统与数据处理**
高效的分布式系统是支撑整个大模型生命周期的基石，涵盖从数据准备到模型存储的全过程。

*   **面向大模型的高性能存储系统**
    *   **ScaleFS (2025)**: 该研究针对大模型工作流（数据准备、训练、推理）对存储系统提出的海量文件（千亿级）与高效访问的需求 [crad.ict.ac.cn](https://crad.ict.ac.cn/article/cstr/32373.14.issn1000-1239.202440373)。ScaleFS 提出一种高性能、可扩展的分布式元数据设计，通过目录树元数据与属性元数据解耦，并结合均衡的目录树分层分区策略，实现高效路径解析与负载均衡。实验结果显示，ScaleFS 的每秒操作次数（OPS）是 HDFS 的 1.04 至 7.12 倍，延迟仅为 HDFS 的 12.67% 至 99.55%，展现了卓越的扩展性和访问效率。

*   **大规模分布式数据处理**
    *   **Data-Juicer (2025)**: 基础模型的数据准备过程本身就是一个大规模分布式计算难题 [docs.rayai.org.cn](https://docs.rayai.org.cn/en/latest/ray-more-libs/data_juicer_distributed_data_processing.html)。Data-Juicer 是一个基于 Ray 的分布式数据处理框架，它通过算子间的互操作性管理实现无缝的分布式执行。为优化大规模场景，Data-Juicer 实现了数据子集自动分割策略以平衡文件数与工作节点，并开发了针对 Ray 和 Arrow 的流式 JSON 文件 I/O 补丁来缓解内存压力。性能测试表明，该框架可在 6400 个 CPU 核上于 2 小时内处理 700 亿个样本，展现了强大的横向扩展能力。

#### **3. 实验与评价总结**
综合分析上述代表性工作，可以总结出以下共性结论：
1.  **可扩展性是核心评价指标**：无论是训练框架（如 ParGNN）、数据处理系统（如 Data-Juicer）还是底层存储（如 ScaleFS），其核心价值均体现在随计算或存储资源增加而近乎线性提升的处理吞吐量或降低的延迟上。然而，这些研究也共同揭示，当规模扩展到一定程度，通信开销、元数据管理或任务调度会成为新的系统瓶颈。
2.  **系统开销与收益的权衡是关键**：没有“银弹”式的解决方案。自动化并行（Alpa）引入了规划和编译开销；弹性容错（AdaptDNN）牺牲了一定的即时性能以换取成本和稳定性；流水线并行则必须面对固有的“气泡”开销。成功的系统设计在于将这些开销的负面影响最小化，使其远小于并行化带来的收益。
3.  **全栈协同优化趋势明显**：性能的极致提升不再仅依赖于单一层面的算法创新。从底层存储（ScaleFS）、数据预处理（Data-Juicer），到上层并行策略（Alpa）和模型服务架构（GenTorrent）的全栈协同设计成为必然。单一环节的瓶颈将制约整个系统的表现。
4.  **对异构和动态环境的适应性日益重要**：研究工作越来越多地考虑现实世界中复杂的部署环境。AdaptDNN 直接面向动态回收的云实例，而 AirComp 则将分布式计算延伸至不稳定的无线信道。这意味着未来的分布式系统必须具备更强的环境感知和自适应调整能力。

#### **4. 趋势与挑战**
基于上述研究，我们预测 2025 年前后并行与分布式计算领域将呈现以下主要趋势和挑战：
1.  **并行策略的自动化与自适应将成为主流**：随着模型架构和硬件拓扑日益复杂，手动配置数据并行、张量并行、流水线并行及 ZeRO 等多种策略的组合变得不切实际。以 Alpa 为代表的自动并行技术将持续深化，未来的系统不仅能静态地发现最优策略，更能**在训练或服务过程中根据负载变化、资源波动（如弹性实例增减）进行动态重配置**，实现自适应的性能优化。
2.  **AI 基础设施的深度解耦与服务化**：过去紧耦合的训练、推理一体化系统将进一步分解。我们将看到更多如 ScaleFS 和 Data-Juicer 这样的**专用、解耦的分布式服务**，分别负责数据处理、模型存储、元数据管理、训练和推理。这要求更高效、低延迟的资源互联技术，并催生面向 AI 工作流的统一资源调度与编排平台。去中心化（GenTorrent）和服务网格（Service Mesh）等思想也将被更广泛地应用于 AI 基础设施。
3.  **异构计算的边界将持续扩展**：对异构资源的利用将从传统的 CPU-GPU 协同，扩展至**涵盖 HBM、DRAM、CXL 连接的内存、NVMe 固态硬盘，乃至边缘设备和无线网络的全方位异构体系**。如推理存储优化和 AirComp 等研究所示，挑战在于如何设计智能的数据放置、预取和迁移策略，以掩盖不同层级存储和网络间的巨大延迟差异，并建立统一的编程模型来屏蔽底层硬件的复杂性。

#### **5. 结论**
本文综述了 2022 至 2025 年间，并行与分布式计算在支持大规模人工智能领域的最新进展。研究表明，该领域正从传统的并行算法设计，转向更为宏观和系统的全栈优化，其核心趋势表现为策略自动化、架构解耦化与资源异构化。未来的研究将更加聚焦于构建能够智能感知、自我调节并高效利用多样化硬件资源的分布式系统，以应对未来更大规模、更复杂模型的挑战。

#### **6. 参考文献**
1.  [crad.ict.ac.cn](https://crad.ict.ac.cn/article/cstr/32373.14.issn1000-1239.202440373) Dong, Z., et al. (2025). ScaleFS: High Performance and Scalable Metadata Design for Large Language Models. *Journal of Computer Research and Development*.
2.  [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/133183) Fang, F., et al. (2025). GenTorrent: Scaling Large Language Model Serving with An Overlay Network. *arXiv preprint*.
3.  [cnic.cas.cn](https://cnic.cas.cn/gzdt/202502/t20250228_7541544.html) Gu, J., et al. (2025). ParGNN: A Scalable Graph Neural Network Training Framework on multi-GPUs. *Proceedings of the 62st ACM/IEEE Design Automation Conference (DAC)*.
4.  [crad.ict.ac.cn](https://crad.ict.ac.cn/article/doi/10.7544/issn1000-1239.202440560) Wang, S., et al. (2025). AdaptDNN: an Adaptive and Scalable DNN Distributed Training System. *Journal of Computer Research and Development*.
5.  [jcst.ict.ac.cn](https://jcst.ict.ac.cn/cn/article/doi/10.1007/s11390-024-3872-3) Guan, L., et al. (2024). Advances of Pipeline Model Parallelism for Deep Learning Training: An Overview. *Journal of Computer Science and Technology*.
6.  [jeit.ac.cn](https://jeit.ac.cn/cn/article/doi/10.11999/JEIT241022?viewType=HTML) Liu, Q., et al. (2025). Research on Resource Scheduling of Distributed CNN Inference System Based on AirComp. *Journal of Electronics & Information Technology*.
7.  [syhya.github.io](https://syhya.github.io/zh/posts/2025-03-01-train-llm/) Shui, Y. (2025). 训练大模型并行和内存优化技术. *Personal Blog*.
8.  [hliangzhao.cn](https://hliangzhao.cn/post/2022/12/13/osdi22-alpa/) Zhao, H. (2022). 分布式训练的自动并行策略 · OSDI '22. *Personal Blog*.
9.  [docs.rayai.org.cn](https://docs.rayai.org.cn/en/latest/ray-more-libs/data_juicer_distributed_data_processing.html) Ray Team. (2025). Data-Juicer 中的分布式数据处理. *Ray Documentation*.
10. [crad.ict.ac.cn](https://crad.ict.ac.cn/article/doi/10.7544/issn1000-1239.202440628?viewType=HTML) Xiao, N., et al. (2025). Survey of Storage Optimization Techniques in Large Language Model Inference. *Journal of Computer Research and Development*.
11. Rajbhandari, S., et al. (2020). ZeRO: Memory optimizations toward training trillion parameter models. *SC20: International Conference for High Performance Computing, Networking, Storage and Analysis*.
12. Zheng, L., et al. (2022). Alpa: Automating Inter- and Intra-Operator Parallelism for Distributed Deep Learning. *16th USENIX Symposium on Operating Systems Design and Implementation (OSDI 22)*.
13. Huang, Y., et al. (2019). Gpipe: Efficient training of giant neural networks using pipeline parallelism. *Advances in Neural Information Processing Systems 32*.
14. Shoeybi, M., et al. (2019). Megatron-lm: Training multi-billion parameter language models using model parallelism. *arXiv preprint arXiv:1909.08053*.
15. Fedus, W., Zoph, B., & Shazeer, N. (2022). Switch transformers: Scaling to trillion parameter models with simple and efficient sparsity. *Journal of Machine Learning Research, 23*(120), 1-39.