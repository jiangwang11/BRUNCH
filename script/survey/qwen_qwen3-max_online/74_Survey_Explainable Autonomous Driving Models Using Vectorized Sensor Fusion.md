# 基于矢量化传感器融合的可解释自动驾驶模型综述（2022–2025）

## 引言

端到端自动驾驶系统对安全性和可靠性的高要求催生了对模型可解释性的迫切需求。传统的黑盒模型难以建立用户信任，亦不利于故障诊断与系统迭代。矢量化传感器融合（Vectorized Sensor Fusion）因其结构紧凑、语义明确、易于可视化与干预，成为构建可解释自动驾驶模型的重要范式。该范式通常将感知结果（如车道线、边界框、轨迹）抽象为带有语义属性的向量或图结构，而非稠密的栅格化特征（如BEV特征图），从而天然地提升了模型决策的透明度。本文聚焦2022至2025年间在该领域的代表性工作，依据其融合策略与可解释性设计进行分类综述，并总结当前挑战与未来趋势。

## 方法分类与代表作

### 1. 基于高斯分布的矢量融合

该类别将环境中的动态与静态元素建模为具有物理属性（均值、协方差、语义）的高斯分布，利用其数学上的可解释性和生成能力进行多传感器信息融合。

*   **GaussianFusion** (arXiv 2025) [^1] 针对现有融合方法可解释性差或计算开销大的问题，提出了一种基于高斯分布的多传感器融合框架。其核心是将驾驶场景初始化为一组2D高斯，通过点交叉注意力和图像交叉注意力模块，从LiDAR和相机数据中迭代地细化每个高斯的物理属性和显式/隐式特征。在nuScenes上，该方法在端到端轨迹预测任务中展示了明确的高斯-物体对应关系，其隐式特征专门用于规划，显式特征用于建图，实现了功能解耦的可解释性。

*   **GGS** (arXiv 2024) [^2] 虽然主要目标是车道切换渲染，但其可泛化的3D高斯溅射（3DGS）框架为可解释的环境建模提供了新思路。它通过多视图深度细化和虚拟车道生成模块，优化高斯参数以适应大视角变化。其可解释性体现在每个高斯都对应场景中的一个可渲染实体，其位置、尺度、旋转和颜色均可直接关联到物理世界，为后续的规划决策提供了直观的环境表征。

### 2. 检测即标注（Detecting As Labeling）范式

此类工作通过对模型架构和训练目标的重新设计，使其内部决策流程与真实世界的数据标注过程对齐，从而获得内在的可解释性。

*   **DAL** (ECCV 2024) [^3] 针对现有LiDAR-相机融合方法因违反数据标注原则（3D框由LiDAR定义）而导致过拟合的问题，提出了“检测即标注”范式。其核心方法是将回归任务（预测3D框的几何属性）与图像特征解耦，仅使用LiDAR特征进行回归，而将相机特征用于候选生成和分类。在nuScenes上的实验表明，该方法不仅达到了SOTA性能（71.5 mAP），而且其决策逻辑清晰可追溯：几何定位的可靠性完全由LiDAR保证，视觉信息仅用于语义确认，极大地提升了模型的鲁棒性和可解释性。

### 3. 统一鸟瞰图（BEV）下的多任务融合

该类别在统一的BEV空间进行特征融合，并通过支持多任务（如3D检测与BEV分割）来增强模型对环境的全面理解，其可解释性来源于任务间的语义关联和BEV空间的直观性。

*   **BEVFusion (MIT)** (ICRA 2023) [^4] 针对点级融合方法会丢弃相机特征的语义密度、导致面向语义任务（如BEV分割）性能不佳的问题，提出在统一的BEV空间进行多模态特征融合。其核心方法是将相机和LiDAR特征均转换到BEV空间，并通过优化的BEV池化（预计算和间隔缩减）解决了视图转换的效率瓶颈。在nuScenes上，该方法在3D检测mAP上提升了1.3%，在BEV分割mIoU上大幅提升了13.6%，证明了统一BEV表征能同时保留几何和语义信息，为多任务决策提供了一致且可解释的环境理解。

*   **SuperFusion** (ICRA 2024) [^5] 为解决长距离（90米）高清地图生成的挑战，提出了激光雷达与相机的多层次融合框架。其方法包括数据级融合（用LiDAR深度监督图像深度估计）、特征级融合（用图像特征通过交叉注意力引导LiDAR远距离BEV特征预测）和BEV级融合。其可解释性体现在多层次的特征交互过程清晰：深度估计的准确性、远距离特征的生成机制均可通过中间特征图进行可视化和分析，为长距离规划提供了可靠的依据。

### 4. 基于扩散模型的鲁棒融合

此类工作利用扩散模型固有的去噪和生成能力，处理传感器故障或数据缺失等极端情况，其可解释性体现在模型能够“想象”并修复缺失的传感器信息。

*   **DifFUSER** (ECCV 2024) [^6] 针对多传感器融合系统在传感器故障时性能急剧下降的问题，首次将扩散模型引入到3D检测与BEV分割的融合中。其核心是设计了一种门控自条件调制（GSM）的潜扩散模块和渐进式传感器丢弃训练（PSDT）范式。在nuScenes上，DifFUSER在BEV分割上达到了70.04% mIoU的SOTA性能，并且在模拟传感器故障场景下，能有效修复或合成传感器特征，其去噪过程本身即为一种可解释的鲁棒性机制。

## 实验与评价总结

对上述代表性工作的实验分析可总结出以下共性结论：
1.  **任务解耦提升可解释性与鲁棒性**：将几何定位（回归）与语义识别（分类）解耦（如DAL），或将显式环境建模与隐式规划特征分离（如GaussianFusion），均被证明能有效减少模态间的错误依赖，提升模型在传感器噪声或故障下的鲁棒性，同时使决策逻辑更清晰。
2.  **统一表征优于点级融合**：在统一的、结构化的空间（如BEV或高斯场）中进行融合，相较于传统的点级或特征级融合，能更完整地保留各传感器的原始信息密度，尤其在面向语义的任务（如分割、地图生成）上优势显著。
3.  **生成式模型增强鲁棒性**：扩散模型等生成式方法在处理传感器数据缺失或损坏时展现出强大的潜力，其通过学习数据分布来“修复”异常输入的能力，为构建极端条件下的可靠自动驾驶系统提供了新途径。
4.  **效率仍是关键瓶颈**：尽管BEVFusion等方法通过算法优化显著提升了效率，但基于复杂视图变换（如LSS）或多层注意力的融合方法，其计算开销仍是实际部署的重大挑战。

## 趋势与挑战

基于对近期工作的分析，2025年及以后的研究将围绕以下趋势展开：
1.  **可解释性与安全验证的紧密结合**：可解释模型将不再仅用于事后分析，而是作为形式化验证和运行时监控的输入，直接用于构建可证明安全的自动驾驶系统。
2.  **世界模型驱动的融合**：融合框架将从被动感知转向主动预测，集成世界模型（World Models）以统一处理多模态感知、状态估计和未来预测，其内部状态（如高斯场、占用网格）将成为可解释性的核心载体。
3.  **生成式AI的深度整合**：除了DifFUSER的初步探索，扩散模型、3D高斯溅射等生成式技术将更深度地融入感知-规划全栈，用于数据增强、场景重建、虚拟仿真和反事实推理，其生成过程的可控性和可解释性将成为研究重点。
4.  **标准化的可解释性评估基准**：目前对可解释性的评价多为主观或任务性能的间接反映，未来将出现专门针对自动驾驶可解释性的量化评估指标和基准数据集。

## 结论

2022至2025年间，基于矢量化传感器融合的可解释自动驾驶研究取得了显著进展。从统一BEV表征到高斯分布建模，从任务解耦设计到生成式鲁棒融合，研究者们通过多样化的技术路径，不断在模型性能、效率与可解释性之间寻求更优的平衡。未来的研究将更加强调可解释性在安全验证中的核心作用，并深度融合世界模型与生成式AI，以构建真正可靠、可信、可部署的下一代自动驾驶系统。

## 参考文献

[^1]: Le, D.-T., Shi, H., Cai, J., & Rezatofighi, H. (2025). GaussianFusion: Gaussian-Based Multi-Sensor Fusion for End-to-End Autonomous Driving. *arXiv preprint arXiv:2506.00034*.
[^2]: [GGS: Generalizable Gaussian Splatting for Lane Switching in Autonomous Driving](https://blog.csdn.net/weixin_45657478/article/details/145860370). (2025). *arXiv preprint arXiv:2409.02382*.
[^3]: Huang, J., Ye, Y., Liang, Z., Shan, Y., & Du, D. (2024). Detecting As Labeling: Rethinking LiDAR-camera Fusion in 3D Object Detection. *European Conference on Computer Vision (ECCV)*.
[^4]: [【论文解读】BEVFusion: Multi-Task Multi-Sensor Fusion with Unified Bird‘s-Eye View Representation](https://blog.csdn.net/lwk___123/article/details/143330886). (2024). *IEEE International Conference on Robotics and Automation (ICRA)*.
[^5]: [【多模态融合】SuperFusion 激光雷达与相机多层次融合 远距离高清地图预测 ICRA 2024](https://blog.csdn.net/qq_41204464/article/details/136723582). (2024). *IEEE International Conference on Robotics and Automation (ICRA)*.
[^6]: [DifFUSER: Diffusion Model for Robust Multi-Sensor Fusion in 3D Object Detection and BEV Segmentation](https://www.zhuanzhi.ai/paper/6b0a491c9f81292104d4bc42d23de3cf). (2024). *European Conference on Computer Vision (ECCV)*.
[^7]: Xu, Y., et al. (2022). BEVFusion: A Simple and Robust LiDAR-Camera Fusion Framework. *arXiv preprint arXiv:2205.13790*.
[^8]: Chen, X., et al. (2022). DeepInteraction: Efficient and Robust LiDAR-Camera Fusion for 3D Object Detection. *arXiv preprint arXiv:2211.15658*.
[^9]: Li, Z., et al. (2023). AutoAlignV2: Deformable Feature Matching for LiDAR-Camera Fusion. *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*.
[^10]: [一文读懂自动驾驶多模态传感器融合-电子工程专辑](https://www.eet-china.com/mp/a125960.html). (2022).
[^11]: [mit的BEVFusion论文笔记_mit bevfusion 分割-CSDN博客](https://blog.csdn.net/weixin_62497890/article/details/133708937). (2025).
[^12]: [MIT-BEVFusion模型理解](https://blog.csdn.net/weixin_43833005/article/details/146210098). (2025).