# 目标检测模型中的知识蒸馏：2022–2025 年进展综述

## 引言

知识蒸馏（Knowledge Distillation, KD）作为模型压缩与性能提升的核心技术，自 2015 年提出以来，在图像分类任务中已趋于成熟。然而，目标检测任务引入了定位与分类的联合优化、前景-背景极端不平衡以及区域依赖等复杂性，使得直接迁移分类领域的 KD 方法效果有限。2022 年以来，针对目标检测特性的 KD 研究进入爆发期，研究者们从特征对齐、预测模仿、任务解耦等维度提出了大量创新性方法。本文系统梳理 2022–2025 年间在顶会顶刊及 arXiv 上发表的代表性工作，按方法论进行分类归纳，并总结实验评价的共性规律，最后对未来研究趋势进行展望。

## 方法分类与代表作

### 1. 预测模仿（Prediction Mimicking）的革新

传统预测模仿因目标冲突（学生需同时拟合 GT 和教师预测）而受限。近期工作通过重构模仿范式有效缓解此问题。

*   **CrossKD **(CVPR 2024) 指出直接模仿教师预测会导致目标冲突。其提出将学生检测头的中间特征输入教师检测头，生成“交叉头预测”，再令该预测模仿教师原始预测。此方法解耦了检测与蒸馏目标，在 GFL 上仅用预测模仿损失即实现 43.7 AP，超越所有特征模仿 SOTA 方法 [CrossKD: Cross-Head Knowledge Distillation for Dense Object Detection](https://blog.csdn.net/weixin_43790925/article/details/140532732)。

*   **Localization Distillation **(LD, CVPR 2022) 重新审视定位知识的传递。其将边界框回归建模为概率分布，并通过 KL 散度蒸馏该分布，首次证明了模仿定位 logit 可超越特征模仿。在 RetinaNet 上，LD 使学生模型 mAP 提升 3.7%，且在小目标上提升显著 [典型常见的基于知识蒸馏的目标检测方法总结二](https://blog.csdn.net/practical_sharp/article/details/144732054)。

*   **DETRDistill **(ICCV 2023) 针对 DETR 系列检测器设计。其一，利用匈牙利匹配对教师与学生的预测（包括大量负样本）进行对齐；其二，利用教师查询生成目标感知的软掩码以进行特征蒸馏；其三，引入查询先验分配蒸馏以加速收敛。该方法在多种 DETR 变体上稳定提升 mAP 超过 2.0，甚至超越教师模型 [【DETR蒸馏】ICCV2023](https://blog.csdn.net/djfjkj52/article/details/148118607)。

### 2. 特征模仿（Feature Imitation）的精细化

特征模仿是主流方向，近期工作聚焦于精细化区域选择与注意力引导，以解决前景-背景不平衡问题。

*   **Focal and Global Knowledge Distillation **(FGD, CVPR 2022) 由清华大学袁春团队提出。其“重点蒸馏”模块分离前景与背景，利用教师的空间与通道注意力加权进行模仿；“全局蒸馏”模块通过 GcBlock 提取全局语义信息进行蒸馏。FGD 在 Faster R-CNN (ResNet-50) 上将 mAP 从 38.4 提升至 40.7，且能有效迁移到实例分割任务 [袁春团队在目标检测的知识蒸馏任务上取得新进展](https://www.sigs.tsinghua.edu.cn/2022/1103/c1210a58433/page.htm)。

*   **Hierarchical Matching Knowledge Distillation **(HMKD, JCST 2024) 专注于小目标检测。其通过编码器从教师 FPN 的深层提取高语义查询向量，并在浅层（P2-P4）与学生的小目标高分辨率特征进行注意力匹配与蒸馏，同时引入补充模块抑制背景噪声。在 COCO2017 上，基于 Faster R-CNN 的 HMKD 达到 41.7% mAP，提升 3.8% [通过分层匹配实现小目标检测的知识蒸馏](https://jcst.ict.ac.cn/cn/article/doi/10.1007/s11390-024-4158-5)。

*   **Adaptive Knowledge Distillation for Lightweight Remote Sensing Object Detectors **(TGRS 2022) 针对遥感图像背景复杂、目标尺度变化大的特点，设计了 ARSD 框架。其 MCFI 模块自适应选择多尺度核心特征并加权关注小目标；SSRD 模块采用严格监督选择策略，仅蒸馏教师优于学生的高质量回归结果。该方法在 DOTA、NWPU 等数据集上超越 SOTA 蒸馏方法及轻量级检测器 [读论文：轻量级遥感目标检测器优化的自适应知识蒸馏](https://blog.csdn.net/a44267113/article/details/130685206)。

### 3. 异构模型与特殊场景的蒸馏

针对异构师生模型及小样本等特殊场景，KD 方法也取得了重要进展。

*   **HEtero-Assists Distillation **(HEAD, ECCV 2022) 解决异构检测器（如教师为两阶段，学生为一阶段）蒸馏难题。其核心是在学生主干上附加一个与教师同构的“助理头”，将异构蒸馏转化为同构蒸馏。HEAD 在异构对上性能远超传统 KD 方法，且可扩展为无教师版本 (TF-HEAD) [典型常见的基于知识蒸馏的目标检测方法总结二](https://blog.csdn.net/practical_sharp/article/details/144732054)。

*   **Transfer-corrected and adaptive knowledge distillation for few-shot object detection **(TCAD-FSOD, 《计算机应用研究》 2025) 针对小样本目标检测中的模型偏差和类无关知识学习难题。其设计物体感知 RPN (OA-RPN) 和分布校正模块 (DCM) 缓解偏差，并提出自适应温度知识蒸馏 (ATKD) 模块，使检测器渐进式学习基类与新类间的共性知识。在 PASCAL VOC 和 COCO 上最高分别提升 2.7% 和 0.7% [融合迁移校正与自适应知识蒸馏的小样本目标检测](https://www.arocmag.cn/abs/2024.07.0275)。

*   **ScaleKD **(CVPR 2023) 专为小目标检测设计，采用跨分辨率蒸馏范式（高分辨率教师指导低分辨率学生）。其尺度解耦特征 (SDF) 蒸馏模块显式解耦不同尺度目标的特征表示，避免小目标特征被大目标和背景干扰，有效提升了小目标检测性能 [典型常见的基于知识蒸馏的目标检测方法总结二](https://blog.csdn.net/practical_sharp/article/details/144732054)。

## 实验与评价总结

综合近年工作，可得出以下共性结论：
1.  **前景-背景分离是关键**：几乎所有成功的特征模仿方法（如 FGD, HMKD, ARSD）都通过显式或隐式方式分离前背景，并对前景（尤其是小目标）赋予更高权重，这直接解决了检测任务的核心不平衡问题。
2.  **预测模仿的复兴**：随着 LD、CrossKD 等工作的出现，预测模仿不再被视为低效方法。通过引入定位分布建模、交叉头预测等机制，预测模仿在提供面向任务的监督信号方面展现出独特优势，甚至超越复杂的特征模仿。
3.  **师生模型的适配性**：KD 性能高度依赖于师生模型的适配性。针对特定架构（如 DETR）或场景（如遥感、小样本）设计的专用 KD 方法，其性能远优于通用方法，表明“一刀切”的 KD 策略已不适用。
4.  **学生模型的潜力**：在多个工作中（如 DETRDistill, CrossKD），经过良好蒸馏的学生模型性能甚至超越了其教师模型，这表明 KD 不仅是压缩工具，更是模型性能增强的有效手段。

## 趋势与挑战

基于 2025 年初的研究动态，未来 KD 在目标检测中的发展将聚焦于以下方向：
1.  **与基础模型（Foundation Models）的融合**：随着 CLIP、SAM 等多模态大模型的普及，如何从这些通用基础模型中蒸馏出适用于特定检测任务的高效“暗知识”，将成为新的研究热点，特别是在开放词汇和零样本检测场景。
2.  **3D 及多模态检测的 KD**：现有 KD 研究主要集中于 2D 图像。针对 3D 目标检测（点云、BEV）以及多模态（RGB-D、红外-可见光）检测的 KD 方法亟待探索，其核心挑战在于跨模态特征对齐与知识迁移。
3.  **理论基础与自适应机制**：当前多数 KD 方法依赖于精心设计的经验性损失函数。未来研究将更注重 KD 在检测任务中的理论解释，并发展能根据输入内容、目标尺度或学习进度动态调整蒸馏策略的自适应 KD 框架。

## 结论

2022–2025 年是目标检测知识蒸馏研究的深化与拓展期。研究重点已从简单的特征/预测模仿，转向对检测任务本质（如前背景不平衡、定位-分类联合优化、架构特异性）的深度理解与针对性设计。精细化、场景化和任务驱动成为主流范式。未来，随着基础模型和 3D/多模态感知的兴起，KD 将扮演更关键的角色，成为连接通用大模型与下游高效专用检测器的核心桥梁。

## 参考文献

1.  Wang, J., et al. (2024). CrossKD: Cross-Head Knowledge Distillation for Dense Object Detection. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*.
2.  Zheng, Z., et al. (2022). Localization Distillation for Object Detection. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*.
3.  Chen, H., et al. (2023). DETRDistill: A Universal Knowledge Distillation Framework for DETR-families. In *Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV)*.
4.  Yang, Z., et al. (2022). Focal and Global Knowledge Distillation for Detectors. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*.
5.  Ma, Y., et al. (2024). Knowledge Distillation via Hierarchical Matching for Small Object Detection. *Journal of Computer Science and Technology (JCST)*, 39(4), 789–804.
6.  Yang, Y., et al. (2022). Adaptive Knowledge Distillation for Lightweight Remote Sensing Object Detectors Optimizing. *IEEE Transactions on Geoscience and Remote Sensing (TGRS)*, 60, 1-14.
7.  Sun, P., et al. (2022). HEtero-Assists Distillation for Heterogeneous Object Detectors. In *European Conference on Computer Vision (ECCV)*.
8.  Zhang, Y., et al. (2025). Transfer-corrected and adaptive knowledge distillation for few-shot object detection. *Application Research of Computers*, 42(5), 1576-1582.
9.  Chen, G., et al. (2023). ScaleKD: Distilling Scale-Aware Knowledge in Small Object Detector. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*.
10. Chen, T., et al. (2023). When Object Detection Meets Knowledge Distillation: A Survey. *IEEE Transactions on Pattern Analysis and Machine Intelligence (TPAMI)*.
11. Li, G., et al. (2022). Knowledge Distillation for Object Detection via Rank Mimicking and Prediction-guided Feature Imitation. In *Proceedings of the AAAI Conference on Artificial Intelligence (AAAI)*.
12. Wang, T., et al. (2019). Distilling Object Detectors With Fine-grained Feature Imitation. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*. (作为早期重要基线被广泛引用和对比)
13. Practical_sharp. (2024). 典型常见的基于知识蒸馏的目标检测方法总结二. *CSDN Blog*.
14. 清华大学深圳国际研究生院. (2022). 袁春团队在目标检测的知识蒸馏任务上取得新进展.