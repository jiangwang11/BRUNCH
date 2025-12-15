# 航空与卫星影像目标检测研究综述（2022–2025）

## 引言

航空与卫星遥感影像的目标检测在国土监测、军事侦察、灾害评估等关键领域具有重要价值。然而，遥感图像固有的多尺度、任意朝向、目标密集、背景复杂等特性，使得通用目标检测器性能显著下降。2022–2025年间，研究者针对这些问题，从网络架构创新、特征融合策略、损失函数设计到大模型迁移等多个维度进行了系统性探索，推动了该领域的快速发展。本综述旨在梳理这一时期的代表性工作，总结共性技术路线，并展望未来发展趋势。

## 方法分类与代表作

### 基于YOLO系列的改进方法

YOLO系列因其高效率成为遥感目标检测的主流基线。研究者通过引入注意力机制、改进特征融合等方式对其进行优化。胡昭华与李昱辉（2024）在YOLOX基础上提出改进算法，通过区域上下文聚合模块（RCAM）利用空洞卷积扩大感受野，并设计特征融合模块（FFM）结合CARAFE上采样以融合多尺度信息。该方法在DIOR数据集上mAP50达到73.87%，比原YOLOX提升4.08个百分点，有效缓解了小目标漏检问题 [laserjournal.cn](https://www.opticsjournal.net/Articles/OJd32c1abf737b6fb3/FullText)。

葛旭东等人（2024）针对YOLOv7提出YOLOv7-BW，在SPPCSPC模块中引入Bi-level Routing Attention，并采用动态非单调的WIoUv3损失函数替代CIoU。该方法在DIOR数据集上mAP50和mAP75分别达到85.63%和65.93%，显著优于基线YOLOv7，证明了注意力机制与动态损失函数对聚焦密集小目标的有效性 [aspub.org](https://www.aspub.org/jir/article/view/20)。

王文聪与张孙杰（2025）提出的IA-YOLO模型，在YOLOv5骨干网络中引入ConvNeXt模块以增强对遮挡目标的检测能力，并设计信息扩大集合（IEC）模块利用大核卷积获取长宽比较大目标的上下文信息。在DOTA-v1.5数据集上，该方法mAP@0.5提升2.5个百分点，尤其在港口（HA）等狭长目标上性能提升显著 [hanspub.org](https://pdf.hanspub.org/sea2025142_322691111.pdf)。

### 专用网络架构设计

为解决遥感图像中高长宽比目标的检测难题，研究者设计了专用的卷积结构。Yuan等人（2025）提出的Strip R-CNN，利用顺序正交的大条带卷积（Large Strip Convolution）替代传统的方形卷积核，以更高效地捕捉空间信息。该模型在DOTA-v1.0上达到了82.75%的mAP，成为当时新的SOTA，展示了专用卷积核在处理极端纵横比物体上的优越性 [arxiv.org](https://arxiv.org/abs/2501.03775)。

程传祥等人（2025）提出的BSPDet网络，显式地对目标的尺度和形状进行感知。该方法通过一个形状感知模块预测目标的长宽比，并动态调整检测头的感受野。在DOTA等数据集上的实验表明，BSPDet在检测飞机、桥梁等形状各异目标时，性能优于传统方法，验证了显式形状建模的有效性 [dqxxkx.cn](https://www.dqxxkx.cn/CN/10.12082/dqxxkx.2025.250142)。

### 旋转目标检测与分支对齐

针对遥感目标任意朝向的特性，旋转目标检测成为研究热点。张海龙等人（2025）提出的分支特征对齐网络（BFA-Net），旨在解决一阶段检测器中分类与回归分支预测不对齐的固有缺陷。该方法通过分支对齐模块（BAM）加强两分支的特征交互，并设计基于对齐度指标的样本分配策略（BAAS），在DOTA-V1.0上取得了75.36%的mAP [opticsjournal.net](https://www.opticsjournal.net/Articles/OJe5fbf04e3ca9f35d/FullText)。

### 遥感大模型与基础模型

随着视觉大模型兴起，研究者开始探索其在遥感领域的迁移应用。潘志刚（2025）的综述系统回顾了遥感大模型的发展，指出其面临数据稀缺、模态异构等挑战，并展望了单模态预训练、视觉-语言联合训练等方向 [opticsjournal.net](https://www.opticsjournal.net/Articles/OJedc4236cc0216f69/FullText)。在此背景下，RemoteCLIP等模型通过将遥感目标检测和分割标签转换为自然语言描述，构建了遥感领域的图文对数据，为大模型的微调提供了数据基础。

## 实验与评价总结

综合分析2022–2025年的研究，实验评价呈现出以下共性：
1.  **数据集标准化**：DOTA（v1.0, v1.5, v2.0）、DIOR（及其旋转版本DIOR-R）和HRSC2016成为评测的主流基准。研究普遍在多数据集上进行验证，以证明方法的泛化能力。
2.  **评价指标精细化**：除整体mAP外，研究更关注特定类别的性能（如港口、桥梁等高长宽比目标）以及不同尺度目标（APS, APM, APL）的检测精度，以全面评估模型优劣。
3.  **消融实验规范化**：几乎所有工作都包含详细的消融实验，逐个验证所提模块（如注意力机制、新损失函数、特征融合策略）的有效性，并分析计算开销（参数量、FLOPs）与性能的权衡。
4.  **可视化分析深入**：通过热力图（heatmap）可视化特征响应，以及对复杂场景（如密集小目标、遮挡目标）的检测结果进行对比，成为分析模型行为和失败案例的标配。

## 趋势与挑战

基于近期研究进展，2025年及以后的研究将围绕以下趋势展开：
1.  **遥感专用大模型的预训练与微调**：构建超大规模的遥感图文对数据集（如EarthGPT提出的MMRS-1M），并开发高效的微调技术（如Adapter、Prompt Tuning），将通用视觉-语言大模型的知识迁移至下游遥感任务，是突破数据标注瓶颈的关键方向。
2.  **多模态与多时相数据融合**：未来的模型将不仅处理单一光学影像，还将融合SAR、高光谱、LiDAR等多模态数据，以及同一区域不同时间点的多时相影像，以提升在复杂天气、夜间或变化检测场景下的鲁棒性。
3.  **面向开放世界的检测范式**：现有方法多针对封闭集（预定义类别）进行检测。未来研究将探索开放词汇（Open-Vocabulary）和零样本（Zero-Shot）检测能力，使模型能够识别训练集中未出现的新型目标，这依赖于视觉-语言大模型的强大泛化能力。

## 结论

2022–2025年，航空与卫星影像目标检测研究在专用网络设计、特征工程优化和大模型迁移等方面取得了显著进展。研究者通过引入注意力机制、设计专用卷积结构、解决分支不对齐问题等手段，有效提升了模型在复杂遥感场景下的检测性能。展望未来，构建遥感领域的大模型生态、实现多模态数据的有效融合、以及迈向开放世界的检测能力，将是推动该领域持续发展的核心驱动力。

## 参考文献

1.  Hu, Z., & Li, Y. (2024). Object Detection Algorithm in Remote Sensing Images Based on Improved YOLOX. *Laser & Optoelectronics Progress*, 61(12), 1228004. [https://www.opticsjournal.net/Articles/OJd32c1abf737b6fb3/FullText](https://www.opticsjournal.net/Articles/OJd32c1abf737b6fb3/FullText)
2.  Ge, X., Jin, X., Ma, H., & Zou, T. (2024). YOLOv7-BW: An Efficient Detector for Dense Small Objects in Remote Sensing Images. *Journal of Intelligent Robotics*, 1(1), 39-54. [https://doi.org/10.52810/JIR.2024.004](https://www.aspub.org/jir/article/view/20)
3.  Wang, W., & Zhang, S. (2025). Remote Sensing Target Detection Based on Information Expansion Collection and Adaptive Feature Fusion. *Software Engineering and Applications*, 14(2), 484-498. [https://pdf.hanspub.org/sea2025142_322691111.pdf](https://pdf.hanspub.org/sea2025142_322691111.pdf)
4.  Yuan, X., Zheng, Z., Li, Y., Liu, X., Liu, L., Li, X., ... & Cheng, M. (2025). Strip R-CNN: Large Strip Convolution for Remote Sensing Object Detection. *arXiv preprint arXiv:2501.03775*. [https://arxiv.org/abs/2501.03775](https://arxiv.org/abs/2501.03775)
5.  Cheng, C., Jin, F., Zuo, X., Lin, Y., Wang, S., & Liu, X. (2025). BSPDet: A Scale and Shape Aware Network for Object Detection in Remote Sensing Scenes. *Journal of Geo-information Science*, 27(11), 2713-2730. [https://www.dqxxkx.cn/CN/10.12082/dqxxkx.2025.250142](https://www.dqxxkx.cn/CN/10.12082/dqxxkx.2025.250142)
6.  Zhang, H., Zeng, Q., Yang, J., Wang, B., & Wang, C. (2025). Branch Alignment Learning for Oriented Object Detection in Remote Sensing Images. *Laser & Optoelectronics Progress*, 62(4), 0428005. [https://www.opticsjournal.net/Articles/OJe5fbf04e3ca9f35d/FullText](https://www.opticsjournal.net/Articles/OJe5fbf04e3ca9f35d/FullText)
7.  Pan, Z. (2025). Remote Sensing Large Models: Review and Future Prospects. *Remote Sensing Technology and Application*, 40(1), 1. [https://www.opticsjournal.net/Articles/OJedc4236cc0216f69/FullText](https://www.opticsjournal.net/Articles/OJedc4236cc0216f69/FullText)
8.  Liu, Z., Mao, H., Wu, C., Feichtenhofer, C., Darrell, T., & Xie, S. (2022). A Convnet for the 2020s. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)* (pp. 11966-11976).
9.  Xia, G., Bai, X., Ding, J., Zhu, Z., Belongie, S., Luo, J., ... & Torr, P. (2018). DOTA: A Large-scale Dataset for Object Detection in Aerial Images. In *Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR)* (pp. 3974-3983).
10. Li, K., Wan, G., Cheng, G., Meng, L., Shen, L., & Han, J. (2020). Object detection in optical remote sensing images: A survey and a new benchmark. *ISPRS Journal of Photogrammetry and Remote Sensing*, 159, 296-307.
11. Gong, H., Mu, T., Li, Q., Dai, H., Li, C., He, Z., ... & Li, X. (2022). Swin-Transformer-Enabled Yolov5 with Attention Mechanism for Small Object Detection on Satellite Images. *Remote Sensing*, 14(12), 2861.
12. Wang, C. Y., Bochkovskiy, A., & Liao, H. Y. M. (2023). YOLOv7: Trainable bag-of-freebies sets new state-of-the-art for real-time object detectors. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)* (pp. 7464-7475).
13. Liu, Z., Lin, Y., Cao, Y., Hu, H., Wei, Y., Zhang, Z., ... & Guo, B. (2021). Swin transformer: Hierarchical vision transformer using shifted windows. In *Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV)* (pp. 10012-10022).
14. Ge, Z., Liu, S., Wang, F., Li, Z., & Sun, J. (2021). Yolox: Exceeding yolo series in 2021. *arXiv preprint arXiv:2107.08430*.