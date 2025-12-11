好的，遵照您的要求，作为一名严谨的科研助手，我将基于提供的真实网络搜索结果，为您生成一篇关于“神经网络模型压缩技术”的中文学术综述。

***

### **神经网络模型压缩技术（2022-2025）学术综述**

#### **引言**

近年来，深度神经网络尤其是大语言模型（LLM）的参数规模呈指数级增长，例如顶级模型的参数已突破万亿级别 [cloud.tencent.cn](https://cloud.tencent.cn/developer/article/2587132?policyId=1003)。这种规模在带来性能飞跃的同时，也引发了巨大的计算、存储和能源消耗挑战，严重制约了其在资源受限环境（如移动终端、边缘设备）中的部署。因此，模型压缩与加速技术成为将大型模型付诸实践的关键瓶颈和研究热点。本综述聚焦于 2022 年至 2025 年期间的代表性工作，系统梳理模型剪枝、量化、知识蒸馏、低秩分解以及针对特定架构的压缩方法的最新进展，并探讨其未来的趋势与挑战。

#### **方法分类与代表作**

##### **1. 模型剪枝（Model Pruning）**

模型剪枝旨在通过移除冗余的参数、神经元或更高粒度的结构来降低模型复杂度。近年来的研究趋势明显偏向于对硬件更友好的结构化剪枝 [html.rhhz.net](https://html.rhhz.net/tis/html/202311011.htm)，并且发展出无需大量重训练的高效剪枝方案。

*   **SlimGPT (2024)** [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/94334)
    *   **研究问题**: 如何在剪枝后以低计算成本快速恢复大型语言模型的性能，解决传统剪枝-微调循环的高昂代价。
    *   **核心方法**: 提出一种名为 SlimGPT 的低成本快速结构化剪枝框架。该方法采用批量贪婪剪枝策略实现近似最优的剪枝决策，并通过分组的 Cholesky 分解来提高头部剪枝误差估计的准确性，从而实现“一步式”剪枝。
    *   **关键结论**: 实验表明，SlimGPT 能在一小时内完成对 LLaMA 等模型的近似局部最优剪枝，其性能优于其他低成本剪枝方法，达到了当时的 SOTA 水平。

*   **基于可融合残差卷积块的层剪枝 (2022)** [xbna.pku.edu.cn](https://xbna.pku.edu.cn/fileup/0479-8023/HTML/2022-5-801.html)
    *   **研究问题**: 传统的卷积核剪枝方法虽然能减少参数量，但对实际推理时间的缩短效果有限，且现有层剪枝方法通常性能较差或实现复杂。
    *   **核心方法**: 提出一种新颖的层剪枝方法，将网络中的卷积层转换为“可融合残差卷积块”，并通过 L1 正则化进行稀疏化训练，根据重要性因子直接剪掉整个卷积层。训练结束后，未被剪枝的残差块可被无损地融合回标准的卷积层，不改变推理时的网络结构。
    *   **关键结论**: 在 VGG-16 和 ResNet-56 等模型上的实验证明，该方法在精度损失更小的情况下，获得了比主流卷积核剪枝方法更高的计算量和参数压缩率。推理耗时实验亦表明，层剪枝在同等计算量压缩率下比核剪枝具有更优的加速效果。

*   **Compact Language Models via Pruning and Knowledge Distillation (2024)** [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/b5f13333-20dc-4cf8-8fd8-18fb903f482c)
    *   **研究问题**: 探究从一个大型预训练模型剪枝得到一系列小型模型，是否是比从零开始训练多个小型模型更高效的策略。
    *   **核心方法**: 开发了一套结合多种结构化剪枝（深度、宽度、MLP 及注意力头）与知识蒸馏的压缩流程。首先对大型教师模型（如 Nemotron-4 15B）进行结构化剪枝得到小型学生模型的结构，然后使用知识蒸馏进行短期的重新训练。
    *   **关键结论**: 该方法仅用不到 3% 的原始预训练数据和少于 40 倍的训练 token，就能得到性能优越的 8B 和 4B 模型。压缩后的 Minitron 模型在 MMLU 分数上比从零训练的模型高出 16%，证明了“先训练大模型，再压缩”范式的有效性。

##### **2. 模型量化（Model Quantization）**

量化通过降低模型权重和/或激活值的数值精度（如从 32 位浮点数降至 8 位或 4 位整数）来显著减小模型体积和内存占用，并利用专用硬件实现加速 [cloud.baidu.com](https://cloud.baidu.com/article/2725056)。针对大模型中激活值存在显著离群点（outliers）的挑战，是近年来的研究重点。

*   **SmoothQuant (2023)** [www.zhuanzhi.ai](https://www.zhuanzhi.ai/paper/9be73d58579fd0971f754d2f81877def)
    *   **研究问题**: 如何在不对大语言模型（如 OPT-175B）进行重新训练的前提下，实现权值和激活值的 INT8 量化，同时保持模型的高精度。
    *   **核心方法**: 观察到权重比激活值更易量化，该工作提出一种数学上等价的变换，通过“平滑”激活值的分布，将量化难度从激活值迁移到权重。这个过程是离线的，无需训练数据。
    *   **关键结论**: SmoothQuant 成功实现了对 OPT-175B、BLOOM-176B 等超大模型的 W8A8（8位权值，8位激活）量化，精度损失极小。与 FP16 推理相比，实现了高达 1.56 倍的加速和 2 倍的内存节省。

*   **极低比特量化与硬件感知量化 (2025 趋势)** [cloud.tencent.cn](https://cloud.tencent.cn/developer/article/2587132?policyId=1003)
    *   **研究问题**: 追求极致压缩率，探索 4 比特甚至更低比特量化的可行性，并充分利用底层硬件的加速能力。
    *   **核心方法**: 综合性的前沿进展包括：1) 探索 2-4 比特的极低比特量化，通过更精细的量化算法将精度损失控制在 1% 以内；2) 硬件感知量化，为特定硬件（如 NVIDIA Blackwell 架构）定制量化策略以最大化吞吐量；3) 可微分量化，将量化参数纳入梯度优化。
    *   **关键结论**: 业界实践已展示出巨大潜力，例如 NVIDIA TensorRT-LLM 在 DeepSeek-R1 671B 模型上实现 FP4 高效推理，吞吐量相较 FP8 提升近 2 倍。

##### **3. 知识蒸馏（Knowledge Distillation）**

知识蒸馏通过训练一个小型“学生”模型来模仿一个大型“教师”模型的行为，从而将知识从大模型迁移至小模型 [cloud.baidu.com](https://cloud.baidu.com/article/2725056)。近年来的研究不仅限于 logits 匹配，更关注于迁移大模型的“涌现能力”。

*   **面向大模型涌现能力的蒸馏 (2023-2025 趋势)** [hub.baai.ac.cn](https://hub.baai.ac.cn/view/28793)
    *   **研究问题**: 如何让小型学生模型学习并模仿大语言模型（LLM）特有的复杂能力，如思维链（Chain-of-Thought）推理和上下文学习（In-context Learning）。
    *   **核心方法**: 区别于只匹配输出概率分布的标准蒸馏，研究者设计了新的蒸馏目标，引导学生模型复现教师模型在解决复杂问题时产生的中间推理步骤或响应模式。
    *   **关键结论**: 这种“涌现能力蒸馏”能够让小型模型在需要复杂推理的任务上表现得更好，而不仅仅是在标准分类或生成任务上模仿教师。这是使小型模型在实际应用中真正“智能”的关键。

*   **多教师与自蒸馏 (2025 趋势)** [cloud.tencent.cn](https://cloud.tencent.cn/developer/article/2587132?policyId=1003)
    *   **研究问题**: 如何突破单个教师模型的知识局限，以及如何在没有更大教师模型的情况下提升模型能力。
    *   **核心方法**: 1) **多教师蒸馏**：利用多个异构的教师模型共同指导一个学生模型，综合各家之长。2) **自蒸馏**：模型通过自我监督学习等方式，提炼并压缩自身知识，实现能力的自我提升和小型化。
    *   **关键结论**: Anthropic 的 Claude Mini 系列通过多教师蒸馏，将大模型能力压缩到 1/10 的尺寸并保留了 85% 以上的性能。微软的 Phi-3 优化版则采用自蒸馏技术，在小尺寸模型上实现了接近中型模型的能力。

##### **4. 针对特定架构的压缩**

随着 Vision Transformer (ViT) 等新架构的兴起，研究者开始设计针对其结构特性的专用压缩算法，这些方法往往比通用方法更有效 [html.rhhz.net](https://html.rhhz.net/tis/html/202311011.htm)。

*   **ToMe: Token Merging for Vision Transformers (2022)** [html.rhhz.net](https://html.rhhz.net/tis/html/202311011.htm)
    *   **研究问题**: Vision Transformer 的计算复杂度与输入的图像块（Token）数量成二次方关系，而图像中的背景等区域存在大量冗余 Token，导致计算浪费。
    *   **核心方法**: 提出一种 Token 合并（ToMe）方法，在模型的不同层级逐步合并相似的 Token，而非直接丢弃。通过二分图匹配算法高效地找到并融合最相似的 Token 对，保留信息的同时减少序列长度。
    *   **关键结论**: ToMe 是一种无需训练的轻量级方法，能够将 ViT 的吞吐量提高约 2 倍，且几乎不损失精度。它证明减少 Token 冗余是 ViT 加速的关键方向。

*   **SPViT: Pruning Self-Attentions into Convolutions (2021, 2024 年综述提及)** [html.rhhz.net](https://html.rhhz.net/tis/html/202311011.htm)
    *   **研究问题**: Transformer 中的自注意力机制计算成本高昂，而卷积在硬件上通常有更高效的实现。
    *   **核心方法**: 该研究探索了将自注意力模块在推理时等效转换为卷积层的可能性。通过一种特殊的训练过程，使得注意力模块的行为可以被一个卷积层近似，从而在部署时进行替换。
    *   **关键结论**: 该方法将注意力模块的计算转换为对硬件更友好的卷积运算，实现了对 ViT 模型的加速，尤其适用于边缘部署场景。

#### **实验与评价总结**

基于上述代表性工作，可总结出以下共性评价结论：

1.  **精度与效率的权衡是核心**：所有压缩方法都面临在模型性能（如准确率、MMLU 分数）和效率指标（如推理延迟、吞吐量、模型大小）之间的权衡。优秀的工作致力于在大幅压缩的同时，将性能损失降至最低。例如，SmoothQuant 实现了几乎无损的 W8A8 量化，而层剪枝方法在 VGG-16 上压缩 73% 的计算量仅损失 1.5% 的准确率 [cloud.tencent.cn, xbna.pku.edu.cn](https://cloud.tencent.cn/developer/article/2587132?policyId=1003)。

2.  **硬件感知成为必要条件**：压缩算法的实际加速效果高度依赖于底层硬件的支持。结构化剪枝之所以优于非结构化剪枝，是因为前者能更好地利用 SIMD 指令和并行计算硬件 [html.rhhz.net](https://html.rhhz.net/tis/html/202311011.htm)。同样，量化的收益也取决于硬件是否为低精度运算（如 INT8/INT4 Tensor Cores）提供了原生支持 [cloud.tencent.cn](https://cloud.tencent.cn/developer/article/2587132?policyId=1003)。

3.  **任务和架构的特异性**：针对特定架构（如 Vision Transformer）的压缩方法（如 Token Merging）通常比通用方法更有效 [html.rhhz.net](https://html.rhhz.net/tis/html/202311011.htm)。此外，在 LLM 压缩中，维持其复杂的涌现能力（如推理链）比在传统 CNN 压缩中保持分类准确率更具挑战性 [hub.baai.ac.cn](https://hub.baai.ac.cn/view/28793)。

4.  **评估基准的综合化**：单一的准确率指标不足以评估压缩效果。全面的评估需要涵盖模型大小、推理延迟（Latency）、吞吐量（Throughput）、浮点运算次数（FLOPs）以及在多个标准基准（如 GLUE、MMLU、HumanEval）上的性能表现 [cloud.tencent.cn](https://cloud.tencent.cn/developer/article/2587132?policyId=1003)。

#### **趋势与挑战**

展望 2025 年前后，神经网络模型压缩领域呈现出以下明确趋势与挑战：

1.  **自动化与智能化压缩 (Automation & Intelligence)**：
    *   **趋势**: 手动设定剪枝率、量化比特数等超参数的过程繁琐且依赖专家经验。未来的研究将更多地采用 AutoML、神经架构搜索（NAS）和强化学习等技术，自动搜索在给定硬件和性能约束下的最优压缩策略 [cloud.tencent.cn](https://cloud.tencent.cn/developer/article/2587132?policyId=1003)。
    *   **挑战**: 自动化搜索空间巨大，需要高效的搜索算法和评估机制，以避免过高的计算开销。

2.  **软硬件协同设计 (Software-Hardware Co-design)**：
    *   **趋势**: 压缩算法的设计越来越多地考虑硬件的特性，即“硬件感知”。反之，专用 AI 芯片（如 ASIC、LPU）的设计也开始为稀疏计算、动态精度等先进压缩技术提供原生支持，形成软硬件的协同进化 [cloud.tencent.cn](https://cloud.tencent.cn/developer/article/2587132?policyId=1003)。
    *   **挑战**: 协同设计需要跨领域的专业知识，且硬件开发周期长、成本高，这限制了其快速迭代。

3.  **混合与统一的方法论 (Hybrid & Unified Methods)**：
    *   **趋势**: 单一的压缩技术已接近瓶颈，未来的工作将更倾向于将剪枝、量化、知识蒸馏和低秩分解等多种技术有机结合，形成统一的压缩框架以达到更优的帕累托前沿 [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/b5f13333-20dc-4cf8-8fd8-18fb903f482c)。
    *   **挑战**: 多种技术的组合会使优化过程变得异常复杂，如何协调不同方法间的相互影响是一个难题。

4.  **维持大模型的复杂能力**:
    *   **趋势**: 压缩 LLM 的研究重点将从单纯地保持基准测试分数，转向如何保留其独特的“涌现能力”（如上下文学习、复杂指令遵循和逻辑推理）。这要求压缩过程不仅仅是移除参数，更是对模型知识结构的精细重构 [hub.baai.ac.cn](https://hub.baai.ac.cn/view/28793)。
    *   **挑战**: 对“涌现能力”的量化评估本身就是一个难题，如何设计有效的损失函数来指导压缩过程以保留这些能力，是前沿的开放性问题。

#### **结论**

在 2022 年至 2025 年期间，神经网络模型压缩技术取得了长足的进步，从通用的剪枝和量化算法，发展到为大语言模型和 Vision Transformer 等特定架构量身定制的高效方案。研究重点已从单纯追求高压缩率转向在保证模型核心能力（特别是 LLM 的涌eyen能力）的前提下，实现硬件友好的、自动化的、多技术融合的综合优化。尽管在精度-效率权衡、自动化以及维持复杂能力等方面仍面临挑战，但模型压缩作为推动人工智能技术普及和可持续发展的关键赋能技术，其重要性将愈发凸显。

#### **参考文献**

[1] Zhu, X., Li, J., Liu, Y., Ma, C., & Wang, W. (2023). A Survey on Model Compression for Large Language Models. *arXiv preprint arXiv:2308.07633*. [hub.baai.ac.cn](https://hub.baai.ac.cn/view/28793)
[2] Ling, G., Wang, Z., Yan, Y., & Liu, Q. (2024). SlimGPT: Layer-wise Structured Pruning for Large Language Models. *arXiv preprint arXiv:2412.18110*. [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/94334)
[3] Muralidharan, S., Sreenivas, S. T., Joshi, R., et al. (2024). Compact Language Models via Pruning and Knowledge Distillation. *arXiv July 2024*. [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/b5f13333-20dc-4cf8-8fd8-18fb903f482c)
[4] Xiao, G., Lin, J., Seznec, M., Wu, H., Demouth, J., & Han, S. (2023). SmoothQuant: Accurate and Efficient Post-Training Quantization for Large Language Models. *ICML 2023*. [www.zhuanzhi.ai](https://www.zhuanzhi.ai/paper/9be73d58579fd0971f754d2f81877def)
[5] Xu, P., Cao, J., Sun, W., Li, P., Wang, Y., & Zhang, X. (2022). Layer Pruning via Fusible Residual Convolutional Block for Deep Neural Networks. *Acta Scientiarum Naturalium Universitatis Pekinensis, 58*(5), 801-807. [xbna.pku.edu.cn](https://xbna.pku.edu.cn/fileup/0479-8023/HTML/2022-5-801.html)
[6] Bolya, D., Fu, C., Dai, X., et al. (2022). Token Merging: Your ViT but Faster. *arXiv preprint arXiv:2210.09461*. [html.rhhz.net](https://html.rhhz.net/tis/html/202311011.htm)
[7] He, H., Liu, J., Pan, Z., et al. (2021). Pruning self-attentions into convolutional layers in single path. *arXiv preprint arXiv:2111.11802*.
[8] Ding, G., Chen, H., Wang, A., et al. (2024). Review of model compression and acceleration for visual deep learning. *CAAI Transactions on Intelligent Systems, 19*(5), 1072-1081. [html.rhhz.net](https://html.rhhz.net/tis/html/202311011.htm)
[9] 安全风信子. (2025). 40_大模型优化与压缩技术：2025年的实践与突破. *腾讯云开发者社区*. [cloud.tencent.cn](https://cloud.tencent.cn/developer/article/2587132?policyId=1003)
[10] 渣渣辉. (2024). 深度探讨LLM模型压缩技术：剪枝、知识蒸馏与量化技术的综合应用. *百度智能云*. [cloud.baidu.com](https://cloud.baidu.com/article/2725056)
[11] He, K., Zhang, X., Ren, S., & Sun, J. (2016). Deep residual learning for image recognition. In *Proceedings of the IEEE conference on computer vision and pattern recognition* (pp. 770-778).
[12] Lin, M., Ji, R., Wang, Y., et al. (2020). Hrank: Filter pruning using high-rank feature map. In *Proceedings of the IEEE/CVF conference on computer vision and pattern recognition* (pp. 1529-1538).