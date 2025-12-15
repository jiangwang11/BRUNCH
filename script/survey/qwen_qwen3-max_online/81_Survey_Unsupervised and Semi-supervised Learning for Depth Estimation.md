# 自监督与半监督深度估计研究综述（2022–2025）

## 引言

单目深度估计（Monocular Depth Estimation, MDE）作为计算机视觉的基础任务，在自动驾驶、增强现实和三维重建等领域具有重要应用。受限于高精度深度传感器的昂贵成本，基于深度学习的方法在缺乏真实深度标签的场景中面临泛化能力不足的挑战。2022–2025年间，研究者广泛采用自监督与半监督学习范式，利用视频序列（帧间光度一致性）或立体图像对（左右视图一致性）构建替代监督信号，有效缓解了对真实深度的依赖。本文系统梳理此期间的研究进展，按方法创新维度分类，分析代表性工作，并总结评估共性，最后展望未来研究趋势。

## 方法分类与代表作

### 基于不确定性度量与引导的方法

为缓解自监督训练中遮挡、运动物体及弱纹理区域导致的深度估计不准确问题，研究者引入不确定性度量机制引导网络学习。肖春霞等人 [jcst.ict.ac.cn](https://jcst.ict.ac.cn/cn/article/doi/10.1007/s11390-023-3088-y) 提出一种不确定性量化策略，通过Snapshot（跨epoch方差）和Siamese（孪生网络方差）两种结构检测不确定性区域，并将其作为权重引入损失函数以强化对困难区域的学习；最终通过集成后处理策略修正深度图。在KITTI数据集上，该方法在七个深度指标上均优于Monodepth2基线，并在不确定性量化指标上超越现有方法，显著提升了尖锐物体的深度估计精度。

### 多帧融合与特征增强架构

利用多帧时序信息是提升深度估计鲁棒性的有效途径。寇旗旗等人 [opticsjournal.net](https://www.opticsjournal.net/Articles/OJa00c675cd4311d5f/FullText) 提出一种多尺度特征增强的多帧自监督模型，其编码器引入大核注意力（LKA）激活模块以捕获全局空间特征，并设计结构增强模块（SEM）在通道维度判别重要特征；解码器则采用动态上采样（DySample）替代近邻插值以恢复细节。实验表明，该模型在KITTI数据集上预测正确率（δ<1.25）达90.3%，深度图边缘更清晰，有效缓解了区域伪影问题。

### 混合架构与知识蒸馏

结合CNN的局部特征提取能力与Vision Transformer（ViT）的全局建模能力成为新范式。郑千惠与孔玲君 [hanspub.org](https://image.hanspub.org/html/80-2571621_87686.htm) 提出HCVNet，设计CNN-ViT混合编码器以建模局部与全局上下文，并引入通道特征聚合模块（CFAM）捕获长距离依赖；同时采用单阶段自监督知识蒸馏，利用前一轮训练的教师模型为学生模型提供监督。在KITTI和Make3D数据集上，HCVNet在所有评估指标上均优于基线，且泛化能力更强，尤其在远处物体（如路灯、建筑）的结构建模上表现突出。

### 多视图与多相机几何约束

针对自动驾驶场景的全向深度感知需求，多摄像头输入成为研究热点。Zou等人提出的M$^2$Depth [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/f0316ba8-fa2c-4e7d-833b-390e3cbe0531) 是一种双帧多摄像头自监督度量深度估计网络，其分别在空间（多相机）和时间（相邻帧）域构建代价体，并通过空间-时间融合模块整合信息；此外，该方法融合SAM（Segment Anything Model）的神经先验特征以减少前景/背景歧义。在nuScenes和DDAD基准上，M$^2$Depth实现了最先进的性能，证明了多视图几何与大模型先验的有效结合。

### 大规模数据与语义先验利用

海量无标签数据与预训练模型先验的结合是提升泛化能力的关键。Depth Anything [blog.csdn.net](https://blog.csdn.net/qq_44799766/article/details/137017569) 通过构建包含62M无标签图像的数据引擎，首先在1.5M标记图像上训练教师模型（T-model）生成伪标签，再训练学生模型（S-model）。其核心策略包括：对无标签图像施加强扰动（色彩失真、CutMix）以创建更具挑战性的优化目标，以及通过特征对齐损失从DINOv2等预训练模型继承语义先验。该方法在零样本（zero-shot）设置下大幅超越MiDaS，并可作为下游任务（如语义分割）的通用编码器。

## 实验与评价总结

综合2022–2025年的研究，实验评价呈现出以下共性：1）**数据集**：KITTI和Cityscapes仍是室外场景评估的黄金标准，而室内场景则多采用NYUv2、ScanNet等；2）**评估指标**：普遍采用Eigen等人提出的七项指标，包括绝对/平方相对误差（Abs Rel, Sq Rel）、均方根误差（RMSE）及其对数形式（RMSE log），以及不同阈值（δ<1.25, 1.25², 1.25³）下的准确率；3）**性能结论**：几乎所有先进方法均表明，通过引入额外的几何约束（如多帧、多视角）、更强的特征表示（如注意力、ViT）或外部先验（如语义、不确定性），模型在边缘清晰度、弱纹理区域一致性及运动物体处理上均有显著提升，但往往以增加计算复杂度为代价；4）**可视化验证**：高质量的深度图普遍表现为物体边界锐利、区域内部平滑且无明显伪影。

## 趋势与挑战

基于对近期文献的分析，未来研究将聚焦于以下方向：1）**基础模型驱动的深度估计**：Depth Anything等工作的成功预示了构建通用深度基础模型（Foundation Model）的趋势，未来将更深入地利用大规模视觉语言模型（VLMs）或扩散模型（Diffusion Models）作为强大的先验与数据引擎；2）**动态与复杂场景建模**：针对真实世界中普遍存在的动态物体、透明/反光表面及极端光照条件，研究将更注重解耦场景中的静态/动态成分，结合神经辐射场（NeRF）等新表示学习方法以提升鲁棒性；3）**高效与轻量化部署**：随着模型复杂度增加，面向边缘设备（如移动机器人、手机）的轻量化、实时深度估计模型将成为研究热点，知识蒸馏、神经架构搜索（NAS）及硬件-算法协同设计将是关键技术路径。

## 结论

2022–2025年，自监督与半监督深度估计研究在架构创新、损失函数设计及数据利用等方面取得了显著进展。从不确定性引导到多视图几何融合，再到大规模数据与语义先验的利用，研究者不断突破性能瓶颈。未来，深度估计将与基础模型、动态场景理解及高效部署等方向深度融合，向更通用、更鲁棒、更实用的目标迈进。

## 参考文献

1.  Li, Y. Z., Zheng, S. J., Tan, Z. X., Cao, T., Luo, F., & Xiao, C. X. (2023). Self-Supervised Monocular Depth Estimation by Digging into Uncertainty Quantification. *Journal of Computer Science and Technology*, 38(3), 543–558. [jcst.ict.ac.cn](https://jcst.ict.ac.cn/cn/article/doi/10.1007/s11390-023-3088-y)
2.  Kou, Q., Wang, W., Han, C., Lü, C., Cheng, D., & Ji, Y. (2024). Multi-frame self-supervised monocular depth estimation with multi-scale feature enhancement. *Optics and Precision Engineering*, 32(24), 3603–3619. [opticsjournal.net](https://www.opticsjournal.net/Articles/OJa00c675cd4311d5f/FullText)
3.  Zheng, Q., & Kong, L. (2024). Hybrid CNN and ViT for Self-Supervised Knowledge Distillation Monocular Depth Estimation Method. *Modeling and Simulation*, 13(3), 2868–2880. [hanspub.org](https://image.hanspub.org/html/80-2571621_87686.htm)
4.  Zou, Y., Ding, Y., Qiu, X., Wang, H., & Zhang, H. (2024). M$^2$Depth: Self-supervised Two-Frame Multi-camera Metric Depth Estimation. *arXiv preprint arXiv:2403.19918*. [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/f0316ba8-fa2c-4e7d-833b-390e3cbe0531)
5.  Yang, L., Kang, B., Huang, Z., Xu, Z., Xie, E., Li, Z., & Qiao, Y. (2024). Depth Anything: Unleashing the Power of Large-Scale Unlabeled Data. *arXiv preprint arXiv:2401.10891*. [blog.csdn.net](https://blog.csdn.net/qq_44799766/article/details/137017569)
6.  Wu, J., & He, Y. (2023). Channel Attentive Self-supervised Network for Monocular Depth Estimation. *Journal of Guangdong University of Technology*, 40(2), 22–29. [html.rhhz.net](https://html.rhhz.net/GDGYDXXB/html/1680831667538-1432911339.htm)
7.  Cheng, D., Fan, S., Qian, J., Jiang, H., & Kou, Q. (2023). Coordinate-aware attention-based multi-frame self-supervised monocular depth estimation. *Journal of Beijing University of Aeronautics and Astronautics*. [yhztjs.spacejournal.cn](https://yhztjs.spacejournal.cn/article/doi/10.13700/j.bh.1001-5965.2023.0417)
8.  Ai, H., Zhang, F., Lü, P., Tang, X., & Wang, Z. (2025). Improving Self-Supervised Monocular Indoor Depth Estimation with Local Feature Guidance. *Journal of Computer Research and Development*. [crad.ict.ac.cn](https://crad.ict.ac.cn/article/doi/10.7544/issn1000-1239.202440951)
9.  Cheng, Z., Han, C., Liang, J., Wang, Q., Zhang, X., & Liu, D. (2024). Self-supervised Adversarial Training of Monocular Depth Estimation against Physical-World Attacks. *arXiv preprint arXiv:2405.15290*. [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/ee0c8799-c366-43fa-845c-737990abb745)
10. Anonymous. (2023). Self-Supervised Monocular Depth Estimation by Direction-aware Cumulative. *Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV)*. [blog.csdn.net](https://blog.csdn.net/weixin_43559672/article/details/136353717)
11. Godard, C., Mac Aodha, O., Firman, M., & Brostow, G. J. (2019). Digging into self-supervised monocular depth estimation. *Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV)*, 3828–3838.
12. Watson, J., Mac Aodha, O., Prisacariu, V., et al. (2021). The temporal opportunist: Self-supervised multi-frame monocular depth. *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*, 1164–1174.