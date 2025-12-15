# 基于深度学习的生物医学图像分割研究综述（2022–2025）

## 引言

医学图像分割作为计算机辅助诊断、放疗规划与手术导航的核心预处理步骤，其自动化与精准化对提升临床效率至关重要。传统方法受限于低对比度、边界模糊及解剖结构高度异质性，难以满足临床需求。2022–2025年间，深度学习技术，特别是基于Transformer、状态空间模型（SSM）及通用分割基础模型（foundation models）的方法，显著推动了该领域的发展。本文系统综述近三年代表性工作，聚焦模型架构创新、多尺度建模、弱监督学习及临床部署等关键方向，并对未来趋势进行预测。

## 方法分类与代表作

### 1. Transformer 与混合架构

Chen 等人提出的 **TransUNet**（arXiv:2102.04306, 2021年后广泛验证）将Transformer作为U-Net的编码器，利用其自注意力机制捕获全局上下文，有效解决了CNN局部感受野不足的问题。该方法在多器官分割任务中平均Dice系数显著优于纯CNN模型，尤其在边界模糊区域表现突出。

Cao 等人的 **SwinUNet**（ECCV 2022 Workshops）构建了纯Transformer的U型架构，通过层次化滑动窗口机制降低了计算复杂度，在保持全局建模能力的同时实现了高效分割，在Synapse等数据集上取得优异性能。

檀文文等人（*计算机科学与应用*, 2025）提出**改进SwinUNet**，通过引入Focal Transformer增强局部与全局交互，结合ASPP模块扩展多尺度感受野，并设计Tokenized Interaction Fusion模块优化跨层特征融合。该方法在Synapse数据集上达到79.53的平均Dice，验证了混合注意力与多尺度特征融合的有效性。

### 2. 状态空间模型（SSM/Mamba）

勾金伟等人（*计算机科学与应用*, 2025）设计了**M-UNet**，将Mamba模型的VSS（Visual State Space）块与ASPP模块结合。VSS块以线性复杂度实现长距离依赖建模，克服了Transformer的二次计算开销，同时ASPP强化多尺度特征提取。实验表明，该模型在Synapse和ACDC数据集上精度优于传统CNN，且计算速度更快。

王劭羽等人（*建模与仿真*, 2025）针对结直肠癌病理切片分割，提出**VMDC-Unet**，融合VMamba与CNN。该模型利用VMamba处理长距离依赖，通过改进的ConvNext模块增强局部细节提取，并设计局部自注意力机制优化跳跃连接。在SJTU_GSFPH和Glas数据集上，其Dice系数分别达到88.51%和91.63%，HD95显著降低。

### 3. 通用分割基础模型（Foundation Models）

Ma 等人开发的 **MedSAM**（arXiv:2306.14452）通过对Meta的Segment Anything Model (SAM) 在大规模医学图像数据集上微调，实现了通用的2D医学图像分割。该模型仅需点或框提示即可分割任意解剖结构或病灶，在多个下游任务中展现出强于专用模型的迁移能力。

Jun Ma 团队进一步提出了 **MedSAM2**（2025），将其扩展至3D医学图像与视频分割。该模型在包含45.5万对3D图像-掩码对的数据集上训练，并通过人机协作管道进行大规模标注。用户研究表明，MedSAM2可将人工标注成本降低85%以上，为多模态、多器官的3D分割提供了高效工具。

### 4. 多任务与弱监督学习

路德昊等人（*临床医学进展*, 2025）系统回顾了弱监督学习在数据稀缺场景的应用，指出通过迁移学习、图像级标签或伪标签进行联合训练，可有效减轻精细标注的成本压力。这类策略已在肝脏、前列腺等任务中得到验证，为解决医学数据标注瓶颈提供了可行路径。

DB-SAM（arXiv:2410.04172, 2024）提出了一种双分支自适应框架，通过一个冻结的ViT分支和一个轻量级卷积分支，并结合双边交叉注意力进行特征融合，有效弥合了通用SAM与医学图像之间的领域差距。该方法在21个3D分割任务上实现了8.8%的绝对性能提升。

## 实验与评价总结

共性实验结论表明，评估指标以Dice相似系数（DSC）和95% Hausdorff距离（HD95）为核心。DSC衡量区域重叠度，而HD95更敏感地反映边界精度。主流方法在单中心、高质量数据集上DSC普遍超过0.90，但在跨中心、异质性数据（如不同设备、扫描协议）上性能显著退化，凸显泛化能力不足。多器官分割任务中，大器官（如肝脏）分割精度高，而小器官（如胰腺、胆囊）及边界模糊病灶仍是挑战。计算效率方面，Mamba等SSM架构在保持高精度的同时显著降低了计算复杂度，为临床实时部署提供了可能。

## 趋势与挑战

基于2025年前后的真实研究进展，可预见以下趋势：
1.  **通用基础模型的3D化与临床集成**：如MedSAM2所示，将通用分割模型扩展至3D/4D（视频）医学数据，并与PACS、放疗计划系统（TPS）深度集成，将成为主流。模型将从“点状支持”走向“全流程赋能”。
2.  **联邦学习与隐私保护计算的规模化应用**：为解决数据孤岛与隐私合规问题，联邦学习、差分隐私及加密计算技术将被更广泛地应用于多中心模型协同训练，以构建泛化性强且合规的智能系统[路德昊 等, 2025]。
3.  **从分割到智能诊疗的范式跃迁**：分割模型将不再是孤立工具，而是作为智能辅助诊疗系统的核心组件，与多模态数据（CT、MRI、病理、文本报告）融合，驱动从“辅助勾画”向“智能辅助诊断与治疗规划”的转变。

## 结论

2022–2025年间，深度学习驱动的生物医学图像分割研究在模型架构（Transformer、Mamba）、通用性（Foundation Models）及临床部署（联邦学习、系统集成）方面取得了显著突破。尽管在精度与效率上已逼近临床可用水平，但模型的跨域泛化能力、可解释性及与临床工作流的无缝融合仍是核心挑战。未来研究将聚焦于构建更鲁棒、更通用、更可信的智能系统，最终实现从“算法可用”到“临床可信”的跨越。

## 参考文献

1.  Chen, J., Lu, Y., Yu, Q., et al. (2021). TransUNet: Transformers Make Strong Encoders for Medical Image Segmentation. *arXiv preprint arXiv:2102.04306*.
2.  Cao, H., Wang, Y., Chen, J., et al. (2023). Swin-Unet: Unet-Like Pure Transformer for Medical Image Segmentation. In *Computer Vision—ECCV 2022 Workshops* (pp. 205-218). Springer.
3.  檀文文, 卢棚, 姜韦. (2025). 基于改进SwinUNet腹部多器官分割算法研究. *计算机科学与应用*, *15*(10), 318-326.
4.  勾金伟, 李代民, 刘锋. (2025). 基于Mamba模型的U型医学图像分割网络. *计算机科学与应用*, *15*(10), 341-350.
5.  王劭羽, 陈庆奎, 黄陈. (2025). 基于VMamba-CNN混合的结直肠癌切片图像分割. *建模与仿真*, *14*(4), 799-810.
6.  Ma, J., Li, H., Xu, Y., et al. (2024). MedSAM: Segment Anything Model for Medical Images. *arXiv preprint arXiv:2306.14452*.
7.  Ma, J., Yang, Z., Kim, S., et al. (2025). MedSAM2: Segment Anything in 3D Medical Images and Videos. *arXiv preprint*.
8.  路德昊, 王媛菲, 张景然. (2025). 基于深度学习的CT图像分割技术在自动勾画中的研究进展与应用. *临床医学进展*, *15*(7), 689-699.
9.  Qin, C., Cao, J., Fu, H., et al. (2024). DB-SAM: Delving into High Quality Universal Medical Image Segmentation. *arXiv preprint arXiv:2410.04172*.
10. Shi, J., Wang, T., Zhu, Z., et al. (2025). 基于深度学习的医学图像分割方法综述. *中国图象图形学报*, *30*(6), 2161-2186.
11. Çiçek, Ö., Abdulkadir, A., Lienkamp, S. S., et al. (2016). 3D U-Net: Learning Dense Volumetric Segmentation from Sparse Annotation. In *MICCAI* (pp. 424-432). Springer.
12. Isensee, F., Jaeger, P. F., Kohl, S. A., et al. (2021). nnU-Net: a self-configuring method for deep learning-based biomedical image segmentation. *Nature Methods*, *18*(2), 203-211.