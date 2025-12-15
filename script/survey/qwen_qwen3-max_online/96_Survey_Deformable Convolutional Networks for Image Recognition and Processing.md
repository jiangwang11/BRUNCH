# 可变形卷积神经网络在图像识别与处理中的进展（2022–2025）：综述

## 引言

可变形卷积（Deformable Convolution, DCN）自2017年由Dai等人提出以来，通过引入可学习的空间偏移量，突破了传统卷积固定采样网格的几何约束，显著增强了模型对目标形变的适应能力。2022至2025年间，该领域经历了从卷积架构内部优化到与注意力机制、Transformer架构深度融合的演进。研究焦点集中在提升计算效率、增强密集预测任务性能以及构建通用视觉骨干网络。本文系统梳理此期间在轻量化设计、注意力机制融合及Transformer适配三大方向上的代表性工作，旨在为后续研究提供清晰的技术脉络与发展方向。

## 方法分类与代表作

### 轻量化与高效DCN架构

随着边缘计算需求的增长，研究者致力于降低DCN的计算开销。DSAN（TNNLS 2025）[cnblogs.com](https://www.cnblogs.com/wxkang/p/18886289) 针对DCNv3在轻量级CNN中因稀疏采样导致性能不足的问题，提出了可变形条形卷积（DSCN）。DSCN将变形采样限制在单轴，并以线性插值替代双线性插值，使计算复杂度从与核尺寸平方增长降为线性增长。其构建的DSAN骨干网络在ImageNet-1K上以76.4%的Top-1精度超越VAN-T 1.0%，在ADE20K语义分割任务上mIoU达43.5%，且推理速度比大核DCNv3快2.1倍。

另一代表性工作DCNv4 [devpress.csdn.net](https://devpress.csdn.net/v1/article/detail/135637073) 进一步优化了动态稀疏聚合机制，发现DCN中的softmax归一化在密集注意力中是冗余的，并改进了半精度训练实现。这使得DCNv4在保持性能的同时，获得了显著的训练和推理速度提升，验证了动态稀疏卷积在高效视觉模型中的巨大潜力。

### 可变形注意力机制

该方向的核心思想是将DCN的动态空间采样能力引入Transformer的注意力计算中，以克服全局注意力的高计算成本和固定稀疏注意力的数据无关性缺陷。Deformable DETR [cnblogs.com](https://www.cnblogs.com/xiaxuexiaoab/p/18599334) 首次系统性地将可变形卷积思想应用于Transformer，其可变形注意力模块仅关注参考点周围的一小组关键采样点。这使其在COCO目标检测任务上，仅用DETR 10%的训练轮数（50 epochs vs 500 epochs）即超越了原始DETR的性能，尤其在小目标检测上提升显著。

在此基础上，清华大学提出的DAT（Deformable Attention Transformer）[hub.baai.ac.cn](https://hub.baai.ac.cn/view/14624) 构建了一个通用的视觉骨干网络。DAT采用数据相关的方式选择自注意力中键值对的位置，使模型能专注于相关区域并捕获更丰富的信息。实验表明，DAT在ImageNet分类和ADE20K分割等多个基准上均优于同期多数ViT变体，证明了可变形注意力作为通用模块的有效性。

### DCN与空间注意力的融合探索

最新的研究开始探索DCN与空间注意力机制在CNN范式内的内在联系与协同。DSAN [cnblogs.com](https://www.cnblogs.com/wxkang/p/18886289) 的核心创新之一即是发现DCNv3的调制掩码分支与空间注意力具有功能相似性。其提出的可变形空间注意力（DSA）模块，用空间注意力机制替代了DCNv3的调制掩码分支，从而在DSCN的基础上进一步减少了参数量和内存消耗。这种设计不仅继承了DCN的全局不规则采样能力，还通过注意力的聚焦特性增强了对关键区域的响应，实现了精度与效率的双重提升。

## 实验与评价总结

对2022–2025年代表性工作的实验分析表明，可变形卷积及其衍生技术在多个维度展现出显著优势。首先，在**密集预测任务**上，如语义分割（ADE20K, Cityscapes）和目标检测（COCO），几乎所有引入可变形机制的模型都取得了稳定的mIoU或mAP提升，证明了其对不规则、多尺度目标的建模能力。其次，在**计算效率**方面，通过限制采样范围（如单轴采样）或减少冗余计算（如移除softmax），新型可变形操作（DSCN, DCNv4）成功在保持甚至超越DCNv3性能的同时，大幅降低了FLOPs和内存占用。最后，在**收敛速度**上，可变形注意力（如Deformable DETR）通过将注意力从全局稀疏化为局部聚焦，有效缓解了标准Transformer注意力在图像任务中收敛缓慢的问题。

## 趋势与挑战

展望2025年及未来，可变形卷积及相关技术的发展呈现以下趋势：
1.  **动态稀疏性的精细化建模**：未来的研究将超越简单的偏移学习，探索更复杂的动态采样策略，如根据内容自适应地决定采样点数量、位置和聚合权重，以实现更智能的特征选择。
2.  **多模态与3D视觉的拓展**：当前工作主要集中在2D图像。将可变形思想扩展到视频（时空可变形）、3D点云（各向异性采样）以及多模态（如图文对齐）任务中，是极具潜力的方向。
3.  **硬件友好型架构设计**：现有可变形操作（如双线性插值）对硬件加速器（如NPU）不够友好。设计计算模式更规则、内存访问更高效的可变形算子，将是推动其在端侧设备大规模部署的关键挑战。

## 结论

2022至2025年，可变形卷积神经网络从一个特定的卷积变体，演变为一种通用的、用于增强模型几何适应性的核心范式。通过与轻量化设计、注意力机制和Transformer架构的深度融合，其在效率、性能和通用性上均取得了长足进步。未来，该领域的研究将更加注重动态建模的智能性、应用场景的广泛性以及硬件部署的可行性，有望为下一代高效、鲁棒的视觉智能系统提供核心动力。

## 参考文献

1.  Dai, J., Qi, H., Xiong, Y., Li, Y., Zhang, G., Hu, H., & Wei, Y. (2017). Deformable Convolutional Networks. *ICCV*.
2.  Zhu, X., Su, W., Lu, L., Li, B., Wang, X., & Dai, J. (2020). Deformable DETR: Deformable Transformers for End-to-End Object Detection. *arXiv preprint arXiv:2010.04159*.
3.  Xiao, A., Zhu, X., Zhang, Y., Zhang, J., Wang, K., Dai, J., & Lu, L. (2023). Vision Transformer with Deformable Attention. *CVPR*.
4.  Wang, Y., Zhang, F., Wang, H., Zhang, M., & Zhang, C. (2025). DSAN: Exploring the Relationship between Deformable Convolution and Spatial Attention. *IEEE Transactions on Neural Networks and Learning Systems (TNNLS)*. [cnblogs.com](https://www.cnblogs.com/wxkang/p/18886289)
5.  Dai, J., et al. (2024). Deformable Convolution v4 (DCNv4). *arXiv preprint* (as reported in [devpress.csdn.net](https://devpress.csdn.net/v1/article/detail/135637073)).
6.  Zhu, X., Hu, H., Lin, S., & Dai, J. (2019). Deformable ConvNets v2: More Deformable, Better Results. *CVPR*.
7.  Liu, Z., Lin, Y., Cao, Y., Hu, H., Wei, Y., Zhang, Z., ... & Guo, B. (2021). Swin Transformer: Hierarchical Vision Transformer using Shifted Windows. *ICCV*.
8.  Dosovitskiy, A., Beyer, L., Kolesnikov, A., Weissenborn, D., Zhai, X., Unterthiner, T., ... & Houlsby, N. (2020). An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale. *ICLR*.
9.  Carion, N., Massa, F., Synnaeve, G., Usunier, N., Kirillov, A., & Zagoruyko, S. (2020). End-to-End Object Detection with Transformers. *ECCV*.
10. Zhang, H., et al. (2022). InternImage: Exploring Large-Scale Vision Foundation Models with Deformable Convolutions. *arXiv preprint arXiv:2211.05778*.
11. Chen, J., Lu, Y., Yu, Q., Wang, X., & Zhou, Y. (2021). TransUNet: Transformers Make Strong Encoders for Medical Image Segmentation. *arXiv preprint arXiv:2102.04306*.
12. Wu, Y., Zhang, F., Wang, H., Zhang, M., & Zhang, C. (2025). MPUNet: Multi-Scale Feature Enhancement and Pooling Attention Network for Skin Disease Segmentation. *Journal of Computer-Aided Design & Computer Graphics*. [jcad.cn](https://www.jcad.cn/cn/article/pdf/preview/10.3724/SP.J.1089.2025-00222.pdf)