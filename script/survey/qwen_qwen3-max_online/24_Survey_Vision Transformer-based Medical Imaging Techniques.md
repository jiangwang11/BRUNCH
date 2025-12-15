# 基于 Vision Transformer 的医学影像分析技术综述（2022–2025）

## 引言

自 U-Net 架构确立以来，卷积神经网络（CNN）长期主导医学图像分割领域，但其固有的局部感受野限制了对长程空间依赖的建模能力。2020 年 Vision Transformer（ViT）的成功激发了医学影像社区对 Transformer 架构的广泛探索。2022 年至 2025 年间，研究者们针对医学影像的高分辨率、多模态及标注稀缺等挑战，提出了大量创新性方法，形成了从纯 Transformer 编码器、CNN-Transformer 混合架构到基于 Mamba 等新型序列模型的演进路径。本文系统梳理此期间的代表性工作，分析其技术脉络，并展望未来发展趋势。

## 方法分类与代表作

### 纯 Transformer 编码器架构
此路线以 Transformer 完全取代 CNN 作为编码器，旨在最大化全局上下文建模能力。

*   **UNETR **(Hatamizadeh et al., WACV 2022) 针对 3D 体积医学图像分割任务，首次提出将纯 ViT 作为 U-Net 的编码器。其将 3D 体素划分为块序列输入 ViT，并从不同层级提取特征，通过跳跃连接与解码器结合。在 MSD 数据集的脑肿瘤和脾脏分割任务上，其性能显著优于基于 CNN 的基线模型，验证了纯 Transformer 在 3D 医学图像分割中的可行性与有效性。

*   **Swin-UNet **(Cao et al., ECCV 2022) 针对 ViT 在处理高分辨率图像时计算复杂度高的问题，提出了一种纯 Transformer 的 U-Net 架构，其编码器、解码器及跳跃连接均基于 Swin Transformer 构建。通过分层的窗口自注意力机制，模型能在保持全局建模能力的同时有效控制计算开销。实验表明，Swin-UNet 在多个 2D 医学图像分割数据集上取得了与混合模型相当甚至更优的性能。

### CNN-Transformer 混合架构
混合架构旨在结合 CNN 的局部特征提取优势与 Transformer 的全局建模能力，是此阶段最主流的研究方向。

*   **TransUNet **(Chen et al., arXiv 2021/MedIA 2024) 作为早期开创性工作，其将 ResNet 作为 CNN 特征提取器，其输出作为 ViT 的输入进行全局上下文建模，再通过 CNN 解码器进行上采样。该架构有效缓解了直接将高分辨率图像输入 ViT 带来的计算和内存压力。在多器官分割任务中，TransUNet 展现了对复杂、可变形状结构的优越分割能力。

*   **CPCATNet **(Zeng et al., 广东工业大学学报 2025) 针对肺部肿瘤分割中病灶与组织对比度低、易粘连等问题，在 TransUNet 基础上进行改进。其在编码器中引入全局-局部注意力（GLA）模块，结合自注意力与卷积操作以同时捕获全局语义和局部细节；在跳跃连接处采用通道优先卷积注意力（CPCA）机制，动态分配空间和通道权重。在 GDPH 和 LUNG1 数据集上，其 Dice 系数分别达到 90.96% 和 88.18%，显著优于多种基线模型。

*   **跨模态哈希方法 **(Liu et al., 电子与信息学报 2025) 针对医学图像与文本报告间深层语义对齐不足的挑战，提出一种大语言模型（LLM）驱动的跨模态哈希检索框架。该方法利用 LLM 生成多种提示模板进行数据增强，并设计结构化编码层和提示指令模板来微调 LLM，实现精确的跨模态对齐。在 MIMIC 和 URBN 数据集上，其平均检索精度（MAP）分别提升 7.21% 和 7.72%。

### 基于新型序列模型的架构
为克服 Transformer 自注意力机制的二次方计算复杂度瓶颈，研究者开始探索线性复杂度的替代方案。

*   **M-UNet **(Gou et al., 计算机科学与应用 2025) 针对 Transformer 计算开销大和 CNN 感受野有限的问题，提出将 Mamba 模型的视觉状态空间（VSS）块与空洞空间卷积金字塔池化（ASPP）模块相结合。VSS 块以线性复杂度实现高效的全局信息建模，而 ASPP 模块则精准捕捉多尺度特征。在 Synapse 和 ACDC 数据集上，M-UNet 在分割精度和计算速度上均显著优于传统 CNN 和部分 Transformer 模型。

*   **MedNeXt **(Roy et al., arXiv 2023) 受 ConvNeXt 启发，该工作并未直接采用 Transformer，而是借鉴其设计理念来现代化卷积网络。MedNeXt 采用大卷积核、残差上下采样块和复合缩放策略，为数据稀缺的医学场景定制了可扩展的卷积架构。其在多个 CT 和 MRI 分割任务上达到 SOTA，表明精心设计的 CNN 仍具有强大的竞争力。

### 预训练与基础模型范式
利用大规模未标注数据进行自监督预训练，以缓解医学领域标注数据稀缺问题，成为重要趋势。

*   **PUMIT **(Luo et al., arXiv 2023) 提出首个通用医学图像 Transformer 基础模型。为处理医学影像在成像模态和空间属性（如体素间距）上的高度异质性，PUMIT 设计了空间自适应卷积（SAC）模块。其在 55 个公共数据集上进行大规模自监督预训练，微调后在下游分类和分割任务中展现出卓越的性能和数据效率，验证了通用医学基础模型的巨大潜力。

## 实验与评价总结

对 2022–2025 年代表性工作的实验分析可归纳出以下共性结论：1）**架构有效性**：纯 Transformer 模型在全局上下文建模上优势明显，但对高分辨率数据计算开销大；混合架构（CNN-Transformer）在性能与效率间取得最佳平衡，成为主流；新型序列模型（如 Mamba）展现出在保持高性能的同时大幅降低计算成本的潜力。2）**任务特异性**：针对特定任务（如肺部肿瘤分割、跨模态检索）设计的注意力机制或数据增强策略能带来显著性能提升。3）**数据依赖性**：预训练基础模型（如 PUMIT）在标注数据稀缺场景下优势突出，其性能高度依赖于预训练数据的规模和多样性。4）**评估指标**：Dice 系数（DSC）和 Hausdorff 距离（HD/HD95）是分割任务的核心指标，前者衡量区域重叠度，后者评估边界精度，二者常需权衡。

## 趋势与挑战

基于现有工作，2025 年及以后的研究将呈现以下趋势：1）**通用医学基础模型的深化**：构建更大规模、更具通用性的医学视觉基础模型（如 PUMIT 的后续工作），并探索其与大语言模型（LLM）的深度融合，以实现真正的多模态、零样本或少样本诊疗推理。2）**高效架构的持续探索**：超越 Transformer 的线性复杂度模型（如 Mamba、状态空间模型）将被更广泛地应用于 3D 甚至 4D（动态）医学影像分析，以解决高分辨率体积数据带来的计算瓶颈。3）**可解释性与临床整合**：研究重点将从单纯的性能提升转向模型可解释性、鲁棒性和不确定性量化，以增强临床医生的信任，并推动这些模型从“实验室”走向真实的临床决策支持工作流。主要挑战仍在于高质量标注数据的获取、多中心数据的异质性以及模型在真实世界复杂场景中的泛化能力。

## 结论

2022 至 2025 年间，基于 Vision Transformer 的医学影像分析技术经历了从初步探索到深度优化的快速发展。研究者们通过设计纯 Transformer、混合架构、高效序列模型以及通用预训练范式等多种路径，有效提升了模型在分割、检索等任务上的性能。未来的研究将在构建更强大的通用基础模型、开发更高效的计算架构以及增强模型的临床可用性等方向上持续推进，为实现精准医疗提供核心技术支持。

## 参考文献

1.  Hatamizadeh, A., et al. (2022). UNETR: Transformers for 3D Medical Image Segmentation. In *Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision (WACV)* (pp. 574-584).
2.  Cao, H., et al. (2022). Swin-Unet: Unet-like Pure Transformer for Medical Image Segmentation. In *European Conference on Computer Vision (ECCV)* (pp. 205-218). Springer.
3.  Chen, J., et al. (2024). TransUNet: Rethinking the U-Net Architecture Design for Medical Image Segmentation through the Lens of Transformers. *Medical Image Analysis*, 97, 103280.
4.  Zeng, A., et al. (2025). 基于Transformer与注意力机制的肺部肿瘤分割方法. *广东工业大学学报*, 42(1), 24-32.
5.  Liu, Q., et al. (2025). 面向大语言模型的医学图像语义挖掘跨模态哈希. *电子与信息学报*. doi: 10.11999/JEIT250529 [jeit.ac.cn](https://www.jeit.ac.cn/cn/article/doi/10.11999/JEIT250529?viewType=HTML)
6.  Gou, J., Li, D., & Liu, F. (2025). 基于Mamba模型的U型医学图像分割网络. *计算机科学与应用*, 15(10), 341-350.
7.  Roy, S., et al. (2023). MedNeXt: Transformer-driven Scaling of ConvNets for Medical Image Segmentation. *arXiv preprint arXiv:2303.09975*.
8.  Luo, L., et al. (2023). Pre-trained Universal Medical Image Transformer. *arXiv preprint arXiv:2312.07630*.
9.  Yin, Y., Ma, J., Zhang, W., & Jiang, L. (2025). 从U-Net到Transformer：混合模型在医学图像分割中的应用进展. *激光与光电子学进展*, 62(2), 0200001. [opticsjournal.net](https://www.opticsjournal.net/Articles/OJ2b2078a8cf027f69/km)
10. Liu, Z., Zhao, Z., & Shi, Z. (2025). 医学影像大模型：肿瘤精准诊疗的范式革新. *协和医学杂志*. [xhyxzz.pumch.cn](https://xhyxzz.pumch.cn/article/doi/10.12290/xhyxzz.2025-0328?viewType=citedby-info)
11. Vaswani, A., et al. (2017). Attention is All You Need. In *Advances in Neural Information Processing Systems (NeurIPS)* (pp. 5998-6008).
12. Dosovitskiy, A., et al. (2020). An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale. *arXiv preprint arXiv:2010.11929*.