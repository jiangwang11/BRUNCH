# 混合神经网络架构在计算机视觉中的应用综述 (2022–2025)

## 引言

近年来，卷积神经网络（CNN）和Transformer模型在计算机视觉领域取得了显著进展，并在各自特定任务中展现出卓越性能。CNN以其局部感知能力和参数共享特性，擅长捕获图像的局部特征和纹理细节；而Transformer凭借其自注意力机制，能够有效建模长距离依赖关系和全局上下文信息。然而，单一架构往往存在局限性：CNN在处理全局信息时表现较弱，而Transformer则可能在处理局部细节时计算成本较高且对数据量要求较大。为了融合两者的优势、弥补各自的不足，混合神经网络架构应运而生，并迅速成为计算机视觉领域的研究热点。本综述旨在总结2022年至2025年间混合神经网络架构在计算机视觉领域的代表性工作，对其主流方法进行分类，并对当前研究的实验与评价进行总结，最后展望未来的研究趋势与挑战。

## 方法分类与代表作

混合神经网络架构旨在通过不同的融合策略，结合CNN捕获局部特征的效率和Transformer建模全局依赖的能力。主要融合策略包括：串联拼接、并行拼接、局部替换和多层次集成。

### 1. 串联拼接 (Sequential Integration)

该策略将CNN和Transformer模块按顺序堆叠，通常利用CNN提取浅层局部特征，再由Transformer处理全局语义。

*   **DETR (DEtection TRansformer)**: Carion 等人 [arXiv:2005.12872v3](https://arxiv.org/abs/2005.12872v3) 于2020年提出的DETR首次将Transformer应用于目标检测任务。它首先使用CNN提取图像的二维特征，然后将这些特征序列化后输入Transformer编码器-解码器结构进行全局上下文建模，直接输出检测框和类别，实现了端到端的目标检测。该方法简化了传统目标检测流程，避免了Anchor和NMS等后处理步骤，展现了Transformer在高级视觉任务中的巨大潜力。

*   **CoAtNet**: Dai 等人 [arXiv:2106.04803v3](https://arxiv.org/abs/2106.04803v3) 于2021年提出的CoAtNet旨在融合CNN的归纳偏置和Transformer的全局建模能力。该模型通过交错使用改进的深度卷积模块（MBConv）和相对自注意力模块，将CNN的平移等变性和Transformer的全局感受野、输入自适应加权机制整合到统一架构中。实验证明，CoAtNet在图像分类等任务中，尤其在不同数据量规模下，均表现出优越的性能，验证了其高效性和泛化能力。

*   **CMTFusion (Cross-Modal Transformers for Infrared and Visible Image Fusion)**: Park 等人 [blog.csdn.net](https://blog.csdn.net/weixin_43858206/article/details/154353348) 在2025年提出CMTFusion，用于红外与可见光图像融合。该方法采用粗到细的多尺度特征提取，并在每一层设计了跨模态Transformer（CMT），通过空间Transformer和通道Transformer在空间域和通道域去除模态冗余信息并捕获全局交互。CMT通过门控瓶颈结构实现跨域交互，以更有效地提取互补信息。该模型在多个数据集上提升了融合性能，并对目标检测、单目深度估计等下游任务产生积极影响。

### 2. 并行拼接 (Parallel Integration)

该策略让CNN和Transformer分支并行处理输入，并通过交互模块融合各自提取的特征。

*   **Conformer**: Peng 等人 [arXiv:2105.07447v3](https://arxiv.org/abs/2105.07444) 在2021年提出了Conformer，通过设计特征耦合单元（FCU）将CNN和Transformer并行连接。这种架构允许模型同时融合CNN提取的局部特征和Transformer捕获的全局特征。Conformer在多项视觉识别任务中取得了良好性能，但在一定程度上增加了模型复杂度和参数量。

*   **Mobile-Former**: Chen 等人 [arXiv:2108.05893v2](https://arxiv.org/abs/2108.05893) 于2021年提出了Mobile-Former，旨在为移动设备提供高效的混合架构。该模型在MobileNet和Transformer两个并行结构之间设计了一个双向连接桥，实现了局部特征和全局特征的双向融合。Mobile-Former在保持计算效率的同时，有效融合了CNN的局部感知和Transformer的全局推理能力，在图像分类等任务上取得了竞争性结果。

*   **FCT-Net (Architectural style classification algorithm fusing CNN and Transformer)**: 刘东等人 [opticsjournal.net](https://www.opticsjournal.net/Articles/OJbea2a3ae7f9b0a37/FullText) 在2024年提出FCT-Net，用于建筑风格分类。该网络核心是CT-Block结构，在通道维度上将特征分为CNN和Transformer两个分支，处理后再拼接。该设计融合了CNN提取局部特征和Transformer提取全局特征的能力，同时通过通道维度的处理减轻了双分支结构带来的模型增大和参数量增多的问题，在建筑风格分类数据集上显示出更高的准确率。

### 3. 局部替换 (Local Replacement)

该策略将CNN或Transformer中的特定模块替换为另一种架构的组件，以在局部层面上进行融合。

*   **Swin Transformer**: Liu 等人 [arXiv:2103.14030v2](https://arxiv.org/abs/2103.14030) 于2021年提出的Swin Transformer引入了基于滑动窗口的自注意力机制，将Transformer的自注意力计算限制在局部窗口内。这种设计使得模型能够像CNN一样构建层次化特征表示，有效降低了计算复杂度，同时保持了捕获长距离依赖的能力，在多种视觉任务中成为具有代表性的基线模型。

*   **BoTNet (Bottleneck Transformers)**: Srinivas 等人 [arXiv:2101.11605v2](https://arxiv.org/abs/2101.11605) 于2021年提出的BoTNet将ResNet瓶颈层中的3x3卷积替换为多头自注意力模块。这种局部替换策略在不大幅增加计算开销的情况下，使得模型能够捕获更广阔的感受野和全局上下文。BoTNet在实例分割和目标检测任务中显著提升了基线性能，为CNN骨干网络提供了一种有效的改进途径。

*   **Next-ViT**: Li 等人 [arXiv:2207.05501v2](https://arxiv.org/abs/2207.05501) 在2022年提出了Next-ViT，以更高效的方式融合了卷积和Transformer。它设计了基于多头卷积注意力（MHCA）的NCB模块来提取局部特征，并利用NTB模块作为轻量级高低频信号混合器以增强全局建模能力。Next-ViT创新性地提出了（N+1）\*L混合范式，通过精简Transformer模块的比例，显著提升了模型在分割和检测等下游任务上的性能。

### 4. 多层次集成 (Multi-level Integration)

该策略通过在不同特征层次上进行融合，以更全面地捕获不同粒度的信息。

*   **CDDFuse (Correlation-Driven Dual-Branch Feature Decomposition for Multi-Modality Image Fusion)**: Zhao 等人 [blog.csdn.net](https://blog.csdn.net/berling00/article/details/149400449) 在2023年提出了CDDFuse，用于多模态图像融合。该网络采用Restormer块提取跨模态浅层特征，并通过双分支Transformer-CNN特征提取器分离处理低频全局特征和高频局部信息。CDDFuse引入相关性驱动损失，使低频特征相关而高频特征不相关，以强化模态特异性和共享特征的分解。该方法在红外-可见光融合和医学图像融合中取得了性能提升。

*   **CoCoNet (Coupled Contrastive Learning Network with Multi-level Feature Ensemble for Multi-modality Image Fusion)**: Liu 等人 [blog.csdn.net](https://blog.csdn.net/qq_42722197/article/details/140170369) 在2024年提出了CoCoNet，用于多模态图像融合。该网络开发了一种耦合对比学习方案来区分红外图像的显著目标和可见光图像的纹理细节，并应用数据敏感权重替代手动设计的权衡参数。CoCoNet还设计了一个多级注意力模块（MAM）以学习丰富的层次化特征表示，并确保特征在融合过程中得到全面传递，有效解决了融合结果中冗余和无效信息的问题。

*   **MMA-UNet (Multi-Modal Asymmetric UNet)**: 在2024年的研究中 [developer.volcengine.com](https://developer.volcengine.com/articles/7389519099556003850)，提出MMA-UNet，一种多模态非对称UNet架构，用于红外与可见光图像融合。该方法发现红外图像和可见光图像在相同网络架构下达到深度语义空间的速率存在差异。为此，MMA-UNet分别为每种模态单独训练专门的特征编码器，并采用跨尺度融合策略，融合VI-UNet的浅层特征和IR-UNet的深层特征，以实现不同模态信息在相同表示空间内的平衡融合，有效避免了浅层信息丢失或偏向单一模态的问题。

*   **BDMFuse (Multi-scale network fusion for infrared and visible images based on base and detail features)**: 司海平等人 [opticsjournal.net](https://www.opticsjournal.net/Articles/OJe6d48f45c76454ee/Abstract) 在2025年提出BDMFuse，一种基于自编码器的红外与可见光图像融合方法。该方法通过构建基础、细节和补偿编码器，提取图像的多尺度低频、高频及补充信息。在解码阶段，引入注意力策略与Fusion模块进行多尺度融合，实现图像重建，旨在强调红外图像的显著目标和保留可见光图像的纹理细节。该模型在三个数据集上生成了高质量的融合图像，且更符合人类视觉感知。

## 实验与评价总结

2022-2025年间，混合神经网络架构在图像分类、目标检测、语义分割、图像融合和医学图像分析等多种计算机视觉任务中进行了广泛的实验验证。

1.  **性能提升与鲁棒性增强**。混合模型普遍展现出超越单一CNN或Transformer架构的性能。例如，在ImageNet-1K等大型图像分类数据集上，许多混合模型（如CoAtNet、Conformer、Next-ViT）在保持较高准确率的同时，实现了参数量和计算量的有效控制。在目标检测任务中，DETR率先证明了Transformer在消除Anchor和NMS方面的潜力，而下一代混合模型（如Next-ViT）则进一步优化了检测精度和部署效率。在语义分割任务中，混合架构能够更精确地捕获像素级语义信息，如UNeXt在ISIC数据集上的F1分数显著高于传统U-Net。

2.  **多模态融合优势显著**。在红外与可见光图像融合等任务中，混合架构被广泛应用于更好地平衡源图像的显著目标和纹理细节。CMTFusion、CDDFuse、CoCoNet和MMA-UNet等模型通过精细设计跨模态交互、高阶特征建模和非对称融合策略，有效解决了信息冗余和单模态偏向问题，生成的融合图像在视觉质量和下游任务适用性方面均表现出优越性。定量指标如SF（空间频率）、AG（平均梯度）、SSIM（结构相似性指数）、VIF（视觉信息保真度）和mAP（平均精度均值）等普遍得到提升，表明融合结果具有更丰富的信息含量、更好的结构保持和更强的视觉感知质量。

3.  **计算效率与泛化能力权衡**。尽管混合架构带来了性能提升，但计算效率和泛化能力仍是重要考量。研究者通过引入轻量级模块、门控机制、可分离自注意力或复合缩放策略来降低模型复杂度和推理延迟（如Mobile-Former、Next-ViT）。在泛化能力方面，一些方法通过知识蒸馏（如DeiT）或借鉴CNN归纳偏置来减少对大规模数据的依赖。然而，跨数据集的泛化能力，特别是在未见过的复杂场景下，仍然是持续研究的领域。

## 趋势与挑战

展望2025年及未来几年，混合神经网络架构在计算机视觉领域将呈现以下趋势并面临相应挑战：

1.  **更深层次的模态交互与自适应融合**：未来的研究将不仅仅停留在简单的特征拼接，而是会探索更复杂的、数据驱动的、自适应的模态间交互机制。例如，在图像融合领域，会更加关注如何根据输入图像的特性动态调整融合策略（如BDMFuse中的注意力策略），而非固定规则。挑战在于设计能够有效量化模态间“信息差距”并据此调整融合权重的机制，以应对高度异构的多模态数据。

2.  **轻量化与高效部署**：随着模型规模的不断扩大，如何在保证性能的同时，实现混合架构的轻量化和高效部署将成为关键。这将涉及更精巧的模型压缩技术（如剪枝、量化），以及更高效的硬件架构适配（如Mobile-Former针对移动设备的优化）。挑战在于如何在模型参数量和计算量大幅减少的情况下，仍能保持高精度，尤其是在边缘计算设备上的实时推理能力。

3.  **任务驱动的端到端优化**：当前许多混合模型已经开始考虑下游任务的性能（如CMTFusion对目标检测和深度估计的提升，CoCoNet中的对比学习指导）。未来这一趋势将更加明显，模型设计将更紧密地与特定应用场景结合，实现端到端的任务驱动优化。例如，CVPR 2025年的研究将更多利用像SAM (Segment Anything Model) 这样的预训练大模型的语义先验来指导图像融合，从而统一视觉质量与任务精确性 [blog.csdn.net](https://blog.csdn.net/GUPAOAI/article/details/147352984)。挑战在于如何设计兼容多任务损失的统一框架，以及如何在多任务学习中平衡不同任务之间的性能。

## 结论

混合神经网络架构通过有机结合CNN的局部特征捕获能力和Transformer的全局上下文建模优势，为计算机视觉领域带来了革命性的进步。2022-2025年间的研究工作在算法设计、性能优化和应用拓展方面取得了显著成就，有效提升了模型在图像分类、目标检测、语义分割以及多模态图像融合等任务中的表现。尽管在计算效率、泛化能力和特定场景适应性方面仍存在挑战，但通过更深层次的模态交互、轻量化设计以及任务驱动的端到端优化，混合架构无疑将继续引领计算机视觉领域的发展，为构建更智能、更高效的视觉系统提供坚实基础。

## 参考文献

1.  Carion, N., Massa, F., Synnaeve, G., Usunier, N., Bottou, L., & Jegou, H. (2020). End-to-End Object Detection with Transformers. *ArXiv:2005.12872v3*.
2.  Dai, Z., Liu, H., Le, Q. V., & Tan, M. (2021). CoAtNet: Marrying Convolution and Attention for All Data Sizes. *ArXiv:2106.04803v3*.
3.  Park, S., Vien, A. G., & Lee, C. (2025). Cross-Modal Transformers for Infrared and Visible Image Fusion. *IEEE Transactions on Circuits and Systems for Video Technology (TCSVT)*, Accepted. [blog.csdn.net](https://blog.csdn.net/weixin_43858206/article/details/154353348)
4.  Peng, Z., Huang, W., Gu, S., Zhang, D., Li, X., & Deng, X. (2021). Conformer: Local Features Coupling Global Representations for Visual Recognition. *Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV)*. [arXiv:2105.07447v3](https://arxiv.org/abs/2105.07447v3)
5.  Chen, Y., Dai, X., Chen, D., Liu, M., & Yuan, L. (2021). Mobile-Former: Bridging MobileNet and Transformer. *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*. [arXiv:2108.05893v2](https://arxiv.org/abs/2108.05893v2)
6.  Liu, D., Zhang, R., Qin, J., Gong, J., & Cao, Z. (2024). Architectural style classification algorithm fusing CNN and Transformer. *Optical Instruments*, *46*(5), 1-13. [opticsjournal.net](https://www.opticsjournal.net/Articles/OJbea2a3ae7f9b0a37/FullText)
7.  Liu, Z., Lin, Y., Cao, Y., Hu, H., Wei, Y., Zhang, Z., ... & Guo, B. (2021). Swin Transformer: Hierarchical Vision Transformer Using Shifted Windows. *Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV)*. [arXiv:2103.14030v2](https://arxiv.org/abs/2103.14030)
8.  Srinivas, A., Lin, T. Y., Parmar, N., Shlens, J., Abadi, M., & Utsuro, H. (2021). Bottleneck Transformers for Visual Recognition. *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*. [arXiv:2101.11605v2](https://arxiv.org/abs/2101.11605)
9.  Li, J., Xia, X., Li, W., Sun, C., & Luo, Z. (2022). Next-ViT: Next Generation Vision Transformer for Efficient Deployment in Realistic Industrial Scenarios. *ArXiv:2207.05501v2*.
10. Zhao, Z., Xu, S., Zhang, C., Liu, J., Li, P., & Zhang, J. (2023). CDDFuse: Correlation-Driven Dual-Branch Feature Decomposition for Multi-Modality Image Fusion. *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*. [blog.csdn.net](https://blog.csdn.net/berling00/article/details/149400449)
11. Liu, J., Lin, R., Wu, G., Liu, R., Luo, Z., & Fan, X. (2024). CoCoNet: Coupled Contrastive Learning Network with Multi-level Feature Ensemble for Multi-modality Image Fusion. *International Journal of Computer Vision (IJCV)*, *132*(1), 1–28. [blog.csdn.net](https://blog.csdn.net/qq_42722197/article/details/140170369)
12. Xu, S. H., Zhang, H., Liu, S. M., Wang, Y., & Li, B. (2024). MMA-UNet: A Multi-Modal Asymmetric UNet Architecture for Infrared and Visible Image Fusion. *ArXiv preprint ArXiv:2407.03961*. [developer.volcengine.com](https://developer.volcengine.com/articles/7389519099556003850)
13. Si, H., Zhao, W., Li, T., Li, F., Bacao, F., Sun, C., & Li, Y. (2025). BDMFuse: Multi-scale network fusion for infrared and visible images based on base and detail features. *Journal of Infrared and Millimeter Waves*, *44*(2), 275-283. [opticsjournal.net](https://www.opticsjournal.net/Articles/OJe6d48f45c76454ee/Abstract)
14. Cui, G., Feng, H., Xu, Z., Li, Q., & Chen, Y. (2015). Detail preserved fusion of visible and infrared images using regional saliency extraction and multi-scale image decomposition. *Optics Communications*, *341*, 199–209.
15. Yin, Y., Ma, J., Zhang, W., & Jiang, L. (2025). From U-Net to Transformer: Progress in the Application of Hybrid Models in Medical Image Segmentation. *Laser & Optoelectronics Progress*, *62*(2), 0200001. [opticsjournal.net](https://www.opticsjournal.net/Articles/OJ2b2078a8cf027f69/km)
16. Unnamed Author (2025). CVPR2025 | SAM赋能多模态图像融合：让每一滴语义信息都发挥价值. [blog.csdn.net](https://blog.csdn.net/GUPAOAI/article/details/147352984)