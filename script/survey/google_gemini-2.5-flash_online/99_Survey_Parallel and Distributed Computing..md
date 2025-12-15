## 并行与分布式计算研究综述 (2022-2025)

### 引言

随着计算任务的日益复杂和数据规模的爆炸式增长，并行与分布式计算已成为解决现代科学与工程挑战不可或缺的手段。特别是在人工智能领域，大语言模型（LLM）的兴起对计算资源、内存管理和训练稳定性提出了前所未有的要求。传统的单机计算能力已无法满足这些需求，分布式系统通过将计算任务拆分并分配到多个计算节点上，从而突破了单机限制。本综述将聚焦2022年至2025年间并行与分布式计算领域，特别是针对大型模型训练和服务的研究进展，总结其核心方法，并对未来趋势进行分析。

### 方法分类与代表作

本节将并行与分布式计算方法划分为数据并行、模型并行、专家并行、序列并行和存储优化五大类，并介绍各项类别中的代表性工作。

#### 1. 数据并行 (Data Parallelism)

数据并行是分布式训练中最常见也最直观的模式，其核心思想是在每个计算设备上复制一份完整的模型参数，并将数据集划分为不同批次分配给各个设备并行计算。

*   **批量同步并行与异步并行探索**
    在数据并行模式下，梯度的同步方式直接影响训练性能和收敛行为。批量同步并行 (BSP) 在每个mini-batch迭代结束后进行全局梯度同步和参数更新，保证了训练过程的同步性，但可能因慢节点而降低资源利用率。异步并行 (ASP) 则允许各节点独立进行计算和参数更新，无需全局同步，典型实现是基于参数服务器架构的异步push-pull机制，虽然提高了资源利用率，但可能引入过时梯度，影响收敛稳定性 [syhya.github.io](https://syhya.github.io/zh/posts/2025-03-01-train-llm)。

*   **PyTorch Distributed Data Parallel (DDP)**
    DDP是PyTorch中数据并行的优化实现，它通过梯度桶化（Gradient Bucketing）和通信与计算重叠策略，显著降低了梯度同步的开销。DDP会根据反向传播的进程，在某个桶内所有梯度计算完成后立即启动针对该桶的All-Reduce操作，而非等待所有梯度计算完毕，从而有效提升并行效率 [syhya.github.io](https://syhya.github.io/zh/posts/2025-03-01-train-llm)。

*   **Ring All-Reduce优化**
    Ring All-Reduce是一种高效的梯度同步方式，尤其适用于多GPU环境。它将所有计算节点组织成一个环形结构，通过分阶段传递和累加梯度，使得通信开销与节点数量近似无关，成为Horovod、NCCL等库中广泛采用的核心通信模式，显著加速了分布式训练 [syhya.github.io](https://syhya.github.io/zh/posts/2025-03-01-train-llm)。

#### 2. 模型并行 (Model Parallelism)

模型并行旨在将模型本身分割到多个计算设备上进行训练，当模型参数规模超过单个GPU内存容量时，模型并行成为必然选择。主要分为流水线并行和张量并行。

*   **流水线并行 (Pipeline Parallelism)**
    **GPipe [syhya.github.io](https://syhya.github.io/zh/posts/2025-03-01-train-llm)**：GPipe通过将mini-batch划分为多个micro-batch，并在不同阶段的GPU之间流水线式传递数据，有效减少了GPU的空闲时间（“气泡”问题）。特别地，当 micro-batch 数量远大于流水线深度时，GPipe能实现接近线性的加速效果。
    **PipeDream [syhya.github.io](https://syhya.github.io/zh/posts/2025-03-01-train-llm), [jcst.ict.ac.cn](https://jcst.ict.ac.cn/cn/article/doi/10.1007/s11390-024-3872-3)**：PipeDream采用1F1B（1-Forward-1-Backward）调度策略，使得每个GPU交替执行前向和反向传播，进一步减少气泡。其引入的权重暂存（Weight Stashing）技术解决了1F1B调度可能导致的权重版本不一致问题。PipeDream-flush和PipeDream-2BW等变体进一步优化了内存使用。

*   **张量并行 (Tensor Parallelism)**
    **Megatron-LM [syhya.github.io](https://syhya.github.io/zh/posts/2025-03-01-train-llm)**：Megatron-LM在Transformer模型中，对大型张量操作（如自注意力机制和MLP层中的矩阵乘法）进行维度切分，并将切分后的分块分配到不同的GPU上并行计算。这种层内并行化方法有效突破了单GPU显存限制，支持训练超大规模语言模型。

#### 3. 专家并行 (Mixture-of-Experts, MoE)

专家并行通过门控策略，让每个输入样本只经过模型中的部分“专家”（子网络），从而在不显著增加计算成本的前提下大幅提升模型参数量。

*   **GShard [syhya.github.io](https://syhya.github.io/zh/posts/2025-03-01-train-llm)**：GShard主要针对MoE层进行分片，将专家网络分散到多个TPU设备上。它改进了Noisy Top-k Gating机制，引入专家容量限制和局部组分发策略，以避免专家过载和提高门控效率。此外，GShard也使用辅助损失函数来平衡专家负载。
*   **Switch Transformer [syhya.github.io](https://syhya.github.io/zh/posts/2025-03-01-train-llm)**：Switch Transformer将Transformer中的密集前馈网络层替换为稀疏的Switch FFN层，实现更高的稀疏性（每个token只路由到一个专家），进一步降低计算成本。它还引入了增强训练稳定性的策略，如选择性精度、更小初始化和更高专家Dropout率。

#### 4. 序列并行 (Sequence Parallelism)

序列并行是一种针对长序列模型（如Transformer）的并行化策略，通过在序列维度上对输入进行划分，旨在降低激活内存占用并提高训练效率。

*   **Colossal-AI 序列并行 [syhya.github.io](https://syhya.github.io/zh/posts/2025-03-01-train-llm)**：该方案通过将输入序列分块并分配到不同GPU，避免单卡内存爆炸。它提出环自注意力（Ring Self-Attention, RSA）机制，通过环状通信确保持久获得全局序列信息。
*   **DeepSpeed-Ulysses 序列并行 [syhya.github.io](https://syhya.github.io/zh/posts/2025-03-01-train-llm)**：DeepSpeed-Ulysses通过在序列维度划分输入，并结合两阶段的全对全通信，有效降低通信量和激活内存。它使得每个GPU只处理局部序列，同时通过All-to-All操作交换Q/K/V，获得完整序列信息。

#### 5. 多维并行 (Multi-dimensional Parallelism)

多维并行是将数据并行、模型并行、流水线并行等多种技术有机结合，以充分利用现代GPU集群的计算资源，实现超大规模模型的高效训练。

*   **3D并行 (DeepSpeed) [syhya.github.io](https://syhya.github.io/zh/posts/2025-03-01-train-llm)**：DeepSpeed将数据并行、模型并行与流水线并行融合，构建“3D并行”策略。通过将模型层划分到流水线阶段，每个阶段内部进行模型并行，同时借助ZeRO-DP（针对优化器状态分片的数据并行）进一步优化内存和计算效率。对通信开销最大的模型并行组优先安排在同一节点内，而通信量较小的流水线并行则可跨节点调度。
*   **4D并行 (Llama3) [syhya.github.io](https://syhya.github.io/zh/posts/2025-03-01-train-llm)**：Llama3在训练中采用了张量并行、流水线并行、上下文并行和数据并行（通常是完全分片的数据并行FSDP）相结合的“4D并行”策略。这种方法进一步细化模型分片，确保每个GPU上的模型参数、优化器状态、梯度和激活值都能适应高带宽内存（HBM）的容量限制。上下文并行将输入上下文划分为多个段，缓解了长序列输入时的内存瓶颈。

#### 6. 存储优化 (Memory Optimization)

存储优化旨在减少训练过程中模型状态和激活值的内存占用，从而支持更大规模模型的训练。

*   **ZeRO (Zero Redundancy Optimizer) [syhya.github.io](https://syhya.github.io/zh/posts/2025-03-01-train-llm)**：ZeRO是一种旨在消除内存冗余的优化器并行技术。它将优化器状态、梯度和模型参数分片分布到多个数据并行进程中。ZeRO-1分片优化器状态，ZeRO-2分片优化器状态和梯度，ZeRO-3进一步分片模型参数，显著降低了每个设备上的内存消耗。
*   **CPU Offloading [jeit.ac.cn](https://jeit.ac.cn/cn/article/doi/10.11999/JEIT241022?viewType=HTML), [syhya.github.io](https://syhya.github.io/zh/posts/2025-03-01-train-llm)**：当GPU内存不足时，将暂时无需使用的数据（如优化器状态或中间激活值）卸载到CPU内存，并在需要时再加载回GPU。ZeRO-Offload和ZeRO-Infinity进一步将模型状态卸载到CPU甚至NVMe磁盘，突破GPU内存墙，支持训练更大规模模型。
*   **激活重计算/梯度检查点 (Activation Recomputation/Gradient Checkpointing) [syhya.github.io](https://syhya.github.io/zh/posts/2025-03-01-train-llm)**：这是一种以计算换内存的技术。在训练过程中只保存部分激活值，在反向传播时重新计算未保存的激活值。通过选择性地检查点层，可以将总体峰值内存需求从$O(n)$降到$O(\sqrt{n})$，尤其适用于深层神经网络。

#### 7. 分布式元数据与数据处理

除了模型训练本身的并行化，高效的数据处理和元数据管理也是大规模分布式系统面临的关键挑战。

*   **ScaleFS: 面向大语言模型的高性能可扩展元数据设计 [crad.ict.ac.cn](https://crad.ict.ac.cn/article/cstr/32373.14.issn1000-1239.202440373)**：ScaleFS通过目录树元数据与属性元数据解耦架构，结合深度与广度均衡的目录树分层分区策略，实现高效路径解析、负载均衡和系统扩展能力，能够高效管理千亿级文件。其细粒度元数据结构和优化的访问模式显著提升了元数据访问效率并减少磁盘I/O。实验表明，ScaleFS在OPS和延迟方面优于HDFS，展现出更高的扩展性和访问效率，可满足LLM对千亿级文件高效存储和访问的需求。

*   **Data-Juicer: 分布式数据处理 [docs.rayai.org.cn](https://docs.rayai.org.cn/en/latest/ray-more-libs/data_juicer_distributed_data_processing.html)**：Data-Juicer支持基于Ray和阿里云PAI的大规模分布式数据处理。通过引擎无关的核心处理函数和RayDataset/RayExecutor管理算子间互操作，几乎所有算子都可在Ray分布式模式下无缝执行。针对文件数量与worker不平衡的问题，它会自动将原始数据集分割。同时，通过定制补丁支持JSON文件的流式读取，缓解内存溢出。其优化的基于MinHash-LSH的去重算子，利用Ray Actor中的多进程Union-Find集合及负载均衡算法，可高效处理PB级别数据集。实验表明其在数十亿样本数据集上具有良好的可伸缩性。

### 实验与评价总结

2022-2025年间，并行与分布式计算领域的研究成果普遍通过以下共性实验结论体现其有效性：

1.  **显著的性能提升**：各类并行策略（数据并行、模型并行、专家并行、序列并行、多维并行）和存储优化技术（ZeRO、激活重计算）都能有效提升模型训练速度和推理效率，或在相同时间内训练更大规模的模型。例如，ScaleFS在OPS和延迟上优于HDFS，DeepSpeed-Ulysses在吞吐量上较Megatron-LM提升2.5倍。
2.  **内存效率的优化**：针对大模型训练中显存瓶颈问题，相关研究通过参数分片 (ZeRO)、激活值重计算、CPU/NVMe Offloading等手段，显著降低了GPU显存占用，使得万亿参数级别的模型训练成为可能。QLoRA在LoRA基础上结合NF4量化和双重量化，极大减少了微调时的显存占用。
3.  **可扩展性增强**：分布式元数据管理系统（如ScaleFS）和分布式数据处理框架（如Data-Juicer）的出现，解决了大规模数据场景下的I/O瓶颈和元数据管理挑战，支持对千亿级文件和PB级别数据的处理，保证了系统在高并发、大规模任务下的稳定性和效率。
4.  **鲁棒性与稳定性**：在分布式训练中，对慢节点等待、通信开销和模型收敛稳定性的权衡是关键。一些研究通过异步机制、优化通信原语（如Ring All-Reduce）以及辅助损失（Mixture-of-Experts）等方式，在提高并行效率的同时，维持或改进了模型收敛性能。

### 趋势与挑战

1.  **大规模异构并行范式将成为主流**：单一的并行策略已不足以支撑超大规模模型和超长序列训练。未来将更加侧重于数据并行、多种模型并行（流水线并行、张量并行）、专家并行和序列并行的融合，形成“N维并行”策略。例如，Llama3训练中已采用4D并行。此外，异构硬件（CPU、GPU、DPU、甚至类脑芯片）的高效协同将是关键。
2.  **系统级软件栈与硬件协同设计的深度融合**：为了最大限度地提高效率，对LLM等复杂工作负载的优化将不限于算法层面。存储系统（如ScaleFS对元数据管理）、网络通信（如GenTorrent对LLM服务），以及编译器优化（如AdaptDNN对分布式训练系统）将更紧密地与底层硬件（如HBM、NVMe、高速互联）进行协同设计，实现从数据加载到模型部署全链路的性能提升。
3.  **推理效率与服务可扩展性将备受关注**：随着LLM的广泛应用，低延迟、高吞吐量的推理服务需求日益增长。研究将进一步探索模型量化（如QLoRA）、稀疏化、离线编译优化以及分布式推理资源调度（如基于AirComp的分布式CNN推理），以降低LLM的服务成本和响应时间。同时，去中心化LLM服务网络（如GenTorrent）的出现，预示着服务可扩展性将通过新的拓扑和通信隐私范式来实现。

### 结论

2022-2025年间，并行与分布式计算领域在应对大语言模型等超大规模计算任务方面取得了显著进展。从精细化的数据并行与模型并行策略，到创新的专家并行和序列并行技术，再到全面的存储优化以及系统层面的元数据和数据处理方案，都展现了该领域持续的活力和解决复杂问题的能力。特别是多维并行和存储优化技术的发展，为训练和部署万亿参数级别的模型奠定了基础。

### 参考文献

*   [crad.ict.ac.cn](https://crad.ict.ac.cn/article/cstr/32373.14.issn1000-1239.202440373) 董振江. ScaleFS：面向大语言模型的高性能可扩展元数据设计.
*   [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/133183) Fang, F., Hua, Y., Wang, S., Zhou, R., Liu, Y., Qian, C., & Zhang, X. (2025). GenTorrent: Scaling Large Language Model Serving with An Overley Network.
*   [cnic.cas.cn](https://cnic.cas.cn/gzdt/202502/t20250228_7541544.html) Gu, J., Li, S., Cao, R., Wang, J., Wang, Z., Liang, Z., Liu, F., Li, S., Zhou, C., Wang, Y., & Chi, X. (2025). ParGNN: A Scalable Graph Neural Network Training Framework on multi-GPUs. *Proceedings of the 62st ACM/IEEE Design Automation Conference (DAC 2025)*.
*   [crad.ict.ac.cn](https://crad.ict.ac.cn/article/doi/10.7544/issn1000-1239.202440560) 刘国栋, 朱家祺, 高梓源, 包云岗, & 王卅. (2025). AdaptDNN：一个自适应可伸缩的大模型分布式训练系统.
*   [jeit.ac.cn](https://jeit.ac.cn/cn/article/doi/10.11999/JEIT241022?viewType=HTML) 刘乔寿, 邓义锋, 胡昊南, & 杨振巍. (2025). 基于AirComp的分布式CNN推理资源调度研究. *电子与信息学报, 47*(7), 2263–2272.
*   [jcst.ict.ac.cn](https://jcst.ict.ac.cn/cn/article/doi/10.1007/s11390-024-3872-3) 关磊, 李东升, 梁吉业, 王文剑, 葛可适, & 卢锡城. (2024). 深度学习训练中的流水线并行训练方法进展.
*   [syhya.github.io](https://syhya.github.io/zh/posts/2025-03-01-train-llm) Shui, Y. (2025). 训练大模型并行和内存优化技术. *syhya.github.io*.
*   [docs.rayai.org.cn](https://docs.rayai.org.cn/en/latest/ray-more-libs/data_juicer_distributed_data_processing.html) Data-Juicer. (2025). Data-Juicer 中的分布式数据处理. *Ray AI Documentation*.
*   [crad.ict.ac.cn](https://crad.ict.ac.cn/article/doi/10.7544/issn1000-1239.202440628?viewType=HTML) 葛旭冉, 欧洋, 王博, 赵宇, 吴利舟, 王子聪, 陈志广, & 肖侬. (2025). 大语言模型推理中的存储优化技术综述.
*   [github.com](https://github.com/xiaoyuexing/StarrySky) xiaoyuexing. (2023). StarrySky: 精选了千余项目，包括机器学习、深度学习、NLP、GNN. *GitHub*.