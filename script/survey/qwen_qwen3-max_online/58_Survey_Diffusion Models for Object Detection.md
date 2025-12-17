# 扩散模型在目标检测中的应用：2022–2025年研究综述

## 引言

扩散模型（Diffusion Models）自2020年兴起以来，在图像生成等任务中展现出卓越性能，其核心在于通过逐步去噪的过程建模数据分布。2022年末起，研究者开始探索将扩散机制引入判别式任务，特别是目标检测。传统目标检测器（如Faster R-CNN、DETR）依赖于预定义锚框或可学习查询，而扩散模型提供了一种从纯噪声边界框出发、通过迭代去噪生成最终检测结果的新范式。本文综述2022至2025年间该领域的代表性工作，按方法类别进行归纳，并分析其共性结论与未来趋势。

## 方法分类与代表作

### 1. 噪声到边界框（Noise-to-Box）范式

该范式将目标检测重新定义为在边界框空间（位置、尺寸）中的生成任务。

* **DiffusionDet (Chen et al., 2022)**[eet-china.com](https://www.eet-china.com/mp/a177301.html) 首次将扩散模型应用于目标检测，提出从随机噪声框到目标框的去噪过程。其核心是将带噪的边界框作为查询，从图像编码器的特征图中裁剪RoI区域，并通过检测解码器预测去噪后的框和类别。在COCO上，仅使用ResNet-50骨干和单步采样即达到45.5 AP，显著优于Faster R-CNN（40.2 AP）和DETR（42.0 AP）。

* **GeoDiffusion (Chen et al., 2023)**[zhuanzhi.ai](https://zhuanzhi.ai/paper/0492452f24dad9e032cfeffbfd1fe2dc) 专注于为检测任务生成高质量的合成训练数据。该方法将边界框等几何条件编码为文本提示，从而引导预训练的文生图扩散模型（如Stable Diffusion）生成带有精确几何对齐的图像。实验证明，使用其生成的数据训练的检测器性能优于使用传统布局到图像（L2I）方法生成的数据，且训练速度提升4倍。

### 2. 扩散增强的特征融合与去噪

这类工作利用扩散模型的去噪能力处理多传感器或多模态融合中的噪声问题。

* **DifFUSER (Le et al., 2024)**[zhuanzhi.ai](https://www.zhuanzhi.ai/paper/6b0a491c9f81292104d4bc42d23de3cf) 为多传感器融合设计了扩散模块，用于在传感器失效或数据质量下降时，对相机和激光雷达等模态的特征进行去噪或补全。其架构包含层级式cMini-BiFPN和门控自条件调制（GSM）扩散模块，并采用渐进式传感器丢弃训练（PSDT）策略。在nuScenes数据集上，其BEV分割mIoU达到70.04%，并在3D检测任务中与顶尖Transformer融合方法竞争。

* **V2X-R (Huang et al., 2025)**[chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/154252) 针对车联网（V2X）场景中恶劣天气下激光雷达性能下降的问题，提出了协同激光雷达-4D雷达融合框架。其核心创新是多模态去噪扩散（MDD）模块，利用天气鲁棒的4D雷达特征作为条件，引导扩散过程对受损的激光雷达特征进行去噪。在自建的V2X-R数据集上，MDD在雾天和雪天条件下分别将3D mAP提升5.73%和6.70%。

### 3. 小样本与特定场景下的应用

扩散模型被用于解决数据稀缺或特定任务中的目标检测挑战。

* **FQRS (Mei et al., 2025)**[jeit.ac.cn](https://www.jeit.ac.cn/cn/article/doi/10.11999/JEIT240841) 针对小样本目标检测（FSOD）中的样本稀缺问题，提出基于条件扩散模型的数据生成框架。该方法设计了类间条件控制（利用基类与新类关系）和类内条件控制（利用IoU约束）模块，以生成高质量且具代表性的新类别样本。在COCO 1-shot设置下，其性能比SOTA模型DeFRCN高出16.9%。

* **DUR (Moonlight, 2025)**[themoonlight.io](https://www.themoonlight.io/zh/review/a-diffusion-based-data-generator-for-training-object-recognition-models-in-ultra-range-distance) 旨在解决超远距离（最远25米）下的手势识别问题，通过扩散模型生成不同距离和类别的合成手势图像。这些合成数据用于训练URGR手势识别模型，最终在真实机器人交互实验中达到了95.8%的识别成功率，有效缓解了真实世界远距离数据采集的困难。

### 4. 细粒度控制与实例级生成

此类工作将扩散模型用于需要对图像中单个实例进行精确控制的场景，其输出本身可视为一种密集检测。

* **InstanceDiffusion (Wang et al., 2024)**[chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/45330) 为文生图扩散模型增加了实例级控制能力，允许用户通过点、涂鸦、边界框或掩码指定每个实例的位置，并为每个实例提供独立的文本描述。其核心组件包括UniFusion（融合文本与位置条件）、ScaleU（提升保真度）和多实例采样器（减少实例间混淆）。在COCO上，其边界框AP50比GLIGEN高出20.4%。

## 实验与评价总结

综合分析上述工作，可得出以下共性结论：
1.  **性能优势**：在标准基准（如MS-COCO、nuScenes）上，基于扩散的目标检测或相关方法在多数情况下能超越或与同期SOTA方法持平，尤其在数据受限（小样本、远距离）或传感器退化（恶劣天气）场景下优势更为明显。
2.  **灵活性与通用性**：扩散框架通常具有“一次训练，多处部署”（Once-for-all）的特性，允许在推理时动态调整计算开销（如采样步数、候选框数量）以平衡速度与精度。同时，其生成能力天然适用于数据增强和合成。
3.  **评估指标**：除传统检测指标（mAP, AP50）外，针对生成式方法，常辅以FID、IS等图像质量指标，以及针对特定控制任务的指标（如InstanceDiffusion中的PiM）。
4.  **计算开销**：迭代去噪过程导致推理速度普遍低于单次前馈的传统检测器，这是当前方法的主要瓶颈。

## 趋势与挑战

基于2025年前后的最新研究动态，可预测以下趋势：
1.  **多模态与3D感知深度融合**：扩散模型将继续作为鲁棒的多模态（视觉、激光雷达、4D雷达、文本）特征融合与补全的核心组件，特别是在自动驾驶等安全关键的3D场景理解任务中。
2.  **高效推理算法的突破**：研究焦点将从模型架构创新转向高效的单步或少步采样技术（如知识蒸馏、一致性模型），以期在保持性能的同时，将扩散检测器的推理速度提升至实用水平。
3.  **开放世界与持续学习场景**：利用扩散模型强大的生成先验，探索在开放词汇、零样本迁移以及类别持续增量的目标检测场景中的应用，以构建更具泛化能力的检测系统。

## 结论

扩散模型为期盼已久的目标检测领域注入了全新的生成式视角。从最初的Noise-to-Box范式到如今在多模态融合、小样本学习和细粒度控制等方向的深度应用，该技术已证明其在提升检测性能、增强系统鲁棒性和解决数据瓶颈方面的巨大潜力。尽管面临推理效率的挑战，但随着高效采样算法和专用硬件的发展，扩散模型有望在未来成为目标检测工具箱中不可或缺的组成部分。

## 参考文献

1.  Chen, S., Sun, P., Zhang, Y., Wang, X., Cao, Y., Qiao, Y., & Luo, P. (2022). DiffusionDet: Diffusion Model for Object Detection. *arXiv preprint arXiv:2211.09788*. [eet-china.com](https://www.eet-china.com/mp/a177301.html)
2.  Chen, K., Xie, E., Chen, Z., Wang, Y., Hong, L., Li, Z., & Yeung, D. Y. (2023). GeoDiffusion: Text-Prompted Geometric Control for Object Detection Data Generation. *arXiv preprint arXiv:2306.04607*. [zhuanzhi.ai](https://zhuanzhi.ai/paper/0492452f24dad9e032cfeffbfd1fe2dc)
3.  Le, D. T., Shi, H., Cai, J., & Rezatofighi, H. (2024). DifFUSER: Diffusion Model for Robust Multi-Sensor Fusion in 3D Object Detection and BEV Segmentation. *arXiv preprint arXiv:2404.04629*. [zhuanzhi.ai](https://www.zhuanzhi.ai/paper/6b0a491c9f81292104d4bc42d23de3cf)
4.  Huang, X., Wang, J., Xia, Q., Chen, S., Yang, B., Li, X., ... & Wen, C. (2025). V2X-R: Cooperative LiDAR-4D Radar Fusion with Denoising Diffusion for 3D Object Detection. *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*. [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/154252)
5.  Mei, T., Wang, Y., & Chen, Y. (2025). 基于条件扩散模型样本生成的小样本目标检测. *电子与信息学报, 47*(4), 1182-1191. [jeit.ac.cn](https://www.jeit.ac.cn/cn/article/doi/10.11999/JEIT240841)
6.  Moonlight. (2025). A Diffusion-based Data Generator for Training Object Recognition Models in Ultra-Range Distance. *The Moonlight Review*. [themoonlight.io](https://www.themoonlight.io/zh/review/a-diffusion-based-data-generator-for-training-object-recognition-models-in-ultra-range-distance)
7.  Wang, X., Darrell, T., Rambhatla, S. S., Girdhar, R., & Misra, I. (2024). InstanceDiffusion: Instance-level Control for Image Generation. *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*. [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/45330)
8.  Ho, J., Jain, A., & Abbeel, P. (2020). Denoising diffusion probabilistic models. *Advances in Neural Information Processing Systems, 33*, 6840-6851.
9.  Carion, N., Massa, F., Synnaeve, G., Usunier, N., Kirillov, A., & Zagoruyko, S. (2020). End-to-end object detection with transformers. *European conference on computer vision (ECCV)*.
10. Li, M., Yuan, J., Chen, S., Zhang, L., Zhu, A., Chen, X., & Chen, T. (2024). 3DET-Mamba: Causal Sequence Modelling for End-to-End 3D Object Detection. *arXiv preprint arXiv:2311.17137*. [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/79995)
11. Lyu, C., Zhang, W., Huang, H., Zhou, Y., Wang, Y., Liu, Y., ... & Chen, K. (2022). RTMDet: An Empirical Study of Designing Real-Time Object Detectors. *arXiv preprint arXiv:2212.07784*. [zhuanzhi.ai](https://www.zhuanzhi.ai/paper/6fdf980e20fce7591f6c4be1c3d04f60)
12. Qiao, L., Zhao, Y., Li, Z., Cheng, Y., Hu, P., & Lu, H. (2021). DeFRCN: Decoupled faster R-CNN for few-shot object detection. *Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV)*.