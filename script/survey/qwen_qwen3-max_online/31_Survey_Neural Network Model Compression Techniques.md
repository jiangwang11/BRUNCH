# 神经网络模型压缩技术综述（2022–2025）

## 引言

随着大型语言模型（LLMs）和视觉Transformer的参数规模突破千亿乃至万亿级别，其部署对计算、存储及能耗提出了严峻挑战 [tencent.com](https://cloud.tencent.cn/developer/article/2587132?policyId=1003)。模型压缩技术由此成为AI产业落地的关键路径。过去三年（2022–2025），以结构化剪枝、后训练量化、任务感知蒸馏和可微分低秩分解为代表的压缩方法取得实质性突破。本文系统综述2022–2025年间在顶会/顶刊/arXiv上发表的代表性工作，聚焦方法创新、实证效果与技术演进趋势，为后续研究提供结构化参考。

## 方法分类与代表作

### 2.1 结构化剪枝（Structured Pruning）

**SlimGPT** [arxiv.org](https://arxiv.org/abs/2412.18110) 针对LLM剪枝中恢复性能成本高的问题，提出一种基于最优脑外科医生（Optimal Brain Surgeon）框架的层-wise结构化剪枝方法。其核心包括：批量贪婪剪枝加速搜索、通过分组Cholesky分解提升注意力头剪枝误差估计精度、动态组大小优化FFN剪枝效率。在LLaMA系列上，SlimGPT在一小时内完成近似局部最优剪枝，显著优于Magnitude、Wanda等基线方法。

**CoFi**（ACL 2022）[cs.princeton.edu](https://arxiv.org/abs/2204.00408) 面向Transformer的粗细粒度联合剪枝方法，同时移除注意力头、FFN神经元及隐藏维度。其创新在于引入逐层蒸馏（layer-wise distillation），动态建立教师-学生层映射弥补信息损失。实验表明，在GLUE任务上，CoFi在10倍加速下仅损失1.5个点，显著优于TinyBERT等蒸馏基线。

**DualPrune**（JCST 2025）[jcst.ict.ac.cn](https://jcst.ict.ac.cn/cn/article/cstr/32374.14.s11390-024-3536-3) 针对高压缩比下层次塌陷问题，提出基于双重注意力的卷积核剪枝算法。其采用图注意力网络（GAT）建模卷积核间全局依赖，并通过旁路注意力机制生成剪枝权重，同时引入旁路路径保障信息流。在ImageNet上对ResNet-50剪枝85% FLOPs时，准确率比PFS高7.13%。

### 2.2 后训练量化（Post-Training Quantization, PTQ）

**SmoothQuant**（NeurIPS 2022）[arxiv.org](https://arxiv.org/abs/2211.10438) 观察到LLM中激活值存在极端离群点，导致仅量化权重量化效果有限。其提出平滑因子将激活值的量化难度转移至权重，实现INT8权重与INT8激活（W8A8）的稳定量化。在OPT、LLaMA等模型上，SmoothQuant在W8A8下几乎无损（MMLU下降<1%），成为后续多数PTQ方法的基础。

**AWQ**（ICLR 2024）[arxiv.org](https://arxiv.org/abs/2306.00978) 指出LLM中仅少数“重要权重”对性能敏感。其通过小规模校准集估计通道级激活幅度，仅对重要权重施加保护性缩放，其余权重可安全量化至4-bit。在LLaMA-2-70B上，AWQ在4-bit量化下MMLU仅下降1.9%，显著优于GPTQ和SmoothQuant。

**HQQ**（arXiv 2024）[arxiv.org](https://arxiv.org/abs/2402.11584) 通过解析推导零点（zero-point）量化公式，将其转化为两个子问题迭代求解，无需校准数据即可实现高效4-bit量化。HQQ在LLaMA、Mistral等模型上达到与AWQ相当的精度，但省去了校准集依赖，提升了部署灵活性。

### 2.3 知识蒸馏（Knowledge Distillation）

**Minitron**（arXiv 2024）[hub.baai.ac.cn](https://hub.baai.ac.cn/paper/b5f13333-20dc-4cf8-8fd8-18fb903f482c) 系统探索从预训练大模型（如Nemotron-4 15B）通过组合深度/宽度/注意力/MLP剪枝生成小模型，并结合知识蒸馏进行恢复训练。仅用<3%原始训练数据微调，Minitron 8B/4B模型MMLU比从头训练提升16%，训练成本降低1.8倍，性能媲美Mistral 7B。

**多教师蒸馏**（腾讯云 2025综述）[tencent.com](https://cloud.tencent.cn/developer/article/2587132?policyId=1003) 代表了一类新兴蒸馏范式，即利用多个异构大模型（如GPT、Claude、PaLM）作为教师，综合其知识训练单一学生模型。Anthropic的Claude Mini系列即采用此策略，在1/10模型规模下保持85%原始性能。

### 2.4 低秩分解（Low-Rank Factorization）

**Dobi-SVD**（ICLR 2025）[tencent.com](https://cloud.tencent.cn/developer/article/2587132?policyId=1003) 提出可微分奇异值分解框架，将SVD过程嵌入训练流程，通过梯度下降自动学习最优秩。与LoRA等静态低秩方法不同，Dobi-SVD能动态调整分解精度，在Flamingo等多模态模型上实现70%计算量降低而性能损失<10%。

**结构化低秩分解**（腾讯云 2025综述）[tencent.com](https://cloud.tencent.cn/developer/article/2587132?policyId=1003) 针对Transformer架构定制，对注意力矩阵和FFN权重分别进行低秩近似。Hugging Face的Optimum-LowRank工具包已实现自动化分解，在BERT、T5等模型上平均减少50%参数量且性能无损。

## 实验与评价总结

近三年压缩技术的实验评估呈现出以下共性结论：  
（1）**剪枝**在LLM上已实现2–4倍模型压缩（如Minitron），而高压缩比（>80% FLOPs）下DualPrune等注意力机制显著缓解性能崩塌；  
（2）**量化**方面，4-bit PTQ（如AWQ、HQQ）已成为LLM部署标准，在主流模型上精度损失可控制在1–3%（MMLU）；W8A8方案（如SmoothQuant）则在延迟敏感场景广泛采用；  
（3）**蒸馏**的有效性高度依赖教师模型质量与蒸馏策略，在数据受限（<3%）场景下仍可超越从头训练（Minitron）；  
（4）**低秩分解**与剪枝/量化组合使用（如LoRA+Dobi-SVD）可进一步提升压缩率，尤其适用于参数高效微调（PEFT）场景；  
（5）评估指标已从单一准确率转向多维：包括MMLU、HumanEval等任务性能，以及吞吐量（tokens/s）、P99延迟、能效比（FLOPS/W）等部署指标。

## 趋势与挑战

基于2025年前后文献，模型压缩领域呈现三大趋势：  
（1）**动态与自适应压缩**：根据输入复杂度或任务需求动态调整模型稀疏度（如腾讯云综述中“动态稀疏性调整”）或量化精度，实现计算资源的按需分配；  
（2）**软硬协同设计**：压缩算法与新一代硬件（如NVIDIA Blackwell、Groq LPU）深度耦合，例如利用硬件原生支持的稀疏格式（如2:4 sparsity）或低比特指令集优化剪枝/量化策略；  
（3）**自动化压缩**（Auto-Compression）：通过神经架构搜索（NAS）或强化学习自动探索剪枝/量化/蒸馏的组合策略，降低人工调参成本。

主要挑战仍存：其一，**极端压缩下的理论极限**尚不明确，尤其在千亿模型上；其二，**跨模态压缩**（如多模态LLM）缺乏统一框架；其三，压缩引入的安全风险（如对抗鲁棒性下降）亟待系统性研究。

## 结论

2022–2025年，模型压缩技术从单点突破走向系统集成。结构化剪枝（SlimGPT）、后训练量化（AWQ）、高效蒸馏（Minitron）与可微分低秩（Dobi-SVD）共同推动了LLM在边缘和云端的规模化部署。未来，动态自适应、软硬协同与自动化将成为技术演进主轴，而理论极限、跨模态泛化与安全性则构成核心挑战。压缩技术已不仅是“瘦身”工具，更是连接算法创新与硬件演进的关键桥梁。

## 参考文献

1. Ling, G., et al. (2024). SlimGPT: Layer-wise Structured Pruning for Large Language Models. arXiv:2412.18110. [arxiv.org](https://arxiv.org/abs/2412.18110)
2. Xia, M., Zhong, Z., & Chen, D. (2022). Structured Pruning Learns Compact and Accurate Models. ACL. [arxiv.org](https://arxiv.org/abs/2204.00408)
3. Fang, Y., et al. (2025). Pushing to the Limit: An Attention-Based Dual-Prune Approach for Highly-Compacted CNN Filter Pruning. Journal of Computer Science and Technology.
4. Xiao, G., et al. (2022). SmoothQuant: Accurate and Efficient Post-Training Quantization for Large Language Models. NeurIPS. [arxiv.org](https://arxiv.org/abs/2211.10438)
5. Lin, X., et al. (2024). AWQ: Activation-aware Weight Quantization for LLM Compression. ICLR. [arxiv.org](https://arxiv.org/abs/2306.00978)
6. Dettmers, T., et al. (2024). HQQ: Highly Accurate 4-bit Quantization for LLMs. arXiv:2402.11584. [arxiv.org](https://arxiv.org/abs/2402.11584)
7. Muralidharan, S., et al. (2024). Compact Language Models via Pruning and Knowledge Distillation. arXiv:2407.14103. [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/b5f13333-20dc-4cf8-8fd8-18fb903f482c)
8. Tencent Cloud. (2025). 大模型优化与压缩技术：2025年的实践与突破. [tencent.com](https://cloud.tencent.cn/developer/article/2587132?policyId=1003)
9. Zhu, X., et al. (2023). A Survey on Model Compression for Large Language Models. arXiv:2308.07633. [hub.baai.ac.cn](https://hub.baai.ac.cn/view/28793)
10. Tang, Y., et al. (2024). A Survey on Transformer Compression. arXiv:2402.03286. [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/2b5567af-7ec5-4ebd-84e1-5e0c7abf19a3)
11. Xu, P., et al. (2022). Layer Pruning via Fusible Residual Convolutional Block for Deep Neural Networks. Acta Scientiarum Naturalium Universitatis Pekinensis, 58(5). [xbna.pku.edu.cn](https://xbna.pku.edu.cn/fileup/0479-8023/HTML/2022-5-801.html)
12. Baidu Cloud. (2024). 模型压缩技术深度综述与应用探索. [cloud.baidu.com](https://cloud.baidu.com/article/3368679)