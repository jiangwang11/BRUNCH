好的，这是一篇关于2022-2025年非监督和半监督深度估计的学术综述。

## 非监督和半监督深度估计研究综述 (2022-2025)

### 引言

深度估计是计算机视觉领域的核心任务之一，旨在从2D图像中推断出场景的3D几何信息。准确的深度信息在自动驾驶、机器人导航、三维重建和增强现实等应用中至关重要。传统监督学习方法依赖于昂贵且难以大规模获取的精确深度真值标注，这极大地限制了其应用范围。为了克服这一瓶颈，非监督学习（Unsupervised Learning）和半监督学习（Semi-supervised Learning）方法应运而生。这两种方法通过利用图像序列中的几何一致性、多视角约束或少量标注数据进行自监督训练，显著降低了对真值数据的依赖。本综述旨在回顾2022年至2025年期间非监督和半监督深度估计领域的代表性工作，分析其核心方法、关键贡献及发展趋势。

### 方法分类与代表作

该领域的研究进展主要体现在利用更强大的特征表示、改进损失函数设计、融合多模态信息以及对抗复杂场景（如动态物体、低纹理、夜间环境）的能力上。

#### 1. 基于多帧几何一致性与自蒸馏的方法

这类方法利用连续视频帧之间的光度一致性和时间几何约束进行自监督学习，并通过知识蒸馏等机制进一步提升性能。

*   **“多尺度特征增强的多帧自监督单目深度估计” (2025)**：该研究针对室外场景深度估计中图像空间特征提取不足导致边缘失真、模糊及伪影问题。文章提出了一种多尺度特征增强网络，在编码器中引入大核注意力模块以捕获全局空间特征和长程依赖，同时设计结构增强模块以判别通道重要特征；解码器则采用动态上采样方法恢复细节。实验结果表明，该方法在KITTI和CityScapes数据集上提升了深度预测精度和边缘清晰度 [opticsjournal.net](https://www.opticsjournal.net/Articles/OJa00c675cd4311d5f/FullText)。
*   **"Hybrid CNN and ViT for Self-Supervised Knowledge Distillation Monocular Depth Estimation Method" (2024)**：该论文提出HCVNet，旨在解决现有单目深度估计方法在利用特征长程相关性和局部信息方面的不足。HCVNet设计了一个结合CNN和Vision Transformer的混合特征编码器来捕捉局部和全局上下文信息，并引入通道特征聚合模块增强场景结构感知。此外，它采用自监督知识蒸馏，教师模型为学生模型提供监督信号，以提高网络性能。实验在KITTI和Make3D数据集上验证了该方法在精度和泛化能力方面的优越性，能够生成结构完整、细节清晰的深度图 [hanspub.org](https://image.hanspub.org/html/80-2571621_87686.htm)。
*   **“局部特征引导的室内自监督单目深度估计方法 (LoFtDepth)” (2025)**：该工作关注复杂室内场景自监督单目深度估计性能下降的问题。LoFtDepth方法利用预训练深度网络预测的结构化相对深度图作为深度先验，提取局部特征引导深度估计细化，减少无关特征干扰并将边界知识传递至自监督网络。同时，引入逆自动掩模加权的表面法线损失以提升无纹理区域的深度精度，并施加位姿一致性约束以适应室内场景相机频繁变化。该方法在主要室内公开数据集上显著提升了全局准确度和结构特征 [crad.ict.ac.cn](https://crad.ict.ac.cn/article/doi/10.7544/issn1000-1239.202440951)。

#### 2. 针对复杂环境与鲁棒性的方法

这类方法致力于提升模型在夜间、动态场景或物理攻击等挑战性条件下的深度估计鲁棒性。

*   **"Jasmine: Harnessing Diffusion Prior for Self-Supervised Depth Estimation" (2025)**：Jasmine论文提出了首个成功将Stable Diffusion（SD）先验注入自监督深度估计的框架。该研究旨在解决传统自监督深度估计在遮挡、弱纹理和光照变化下监督信号不准确的问题。核心创新包括混合批次图像重建 (MIR) 解耦结构学习和细节保持，以及尺度-位移门控循环单元 (SSG) 克服SD输出的SSI与自监督SI之间的分布鸿沟，并过滤有害梯度。Jasmine在KITTI基准上刷新了SOTA，并展示了强大的零样本泛化能力和卓越的深度图细节表现 [cnblogs.com](https://www.cnblogs.com/aaooli/p/19137028)。
*   **"ICRA 2023 | 首个联合暗光增强和深度估计的自监督方法STEPS" (2025)**：该工作提出STEPS，一个自监督框架，用于联合学习夜间图像增强和深度估计。研究解决了夜间图像中欠曝和过曝区域导致深度估计不准确的问题。通过自监督图像增强模块生成光照图，并利用此中间产物生成像素级掩膜，以降低这些区域对训练的影响。该方法在nuScenes和RobotCar数据集上实现了SOTA性能，并引入了仿真数据集CARLA-EPE以提供密集的深度真值和真实风格图像 [blog.csdn.net](https://blog.csdn.net/hanseywho/article/details/129146059)。
*   **"Self-Supervised Adversarial Training of Monocular Depth Estimation against Physical-World Attacks" (2024)**：该论文提出了一种新的自监督对抗训练方法，增强单目深度估计模型对物理世界攻击的鲁棒性。研究关注单目深度估计模型在自动驾驶等应用中面临的安全威胁，传统对抗训练依赖地面真值，不适用于缺乏真实深度数据的单目估计。核心方法是利用视图合成进行自监督训练，并在训练过程中引入L0范数限制的扰动，以提高模型对抗真实世界攻击的能力。实验表明，该方法在两个典型的单目深度估计网络上显著提升了对抗鲁棒性，同时对良性性能影响极小 [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/ee0c8799-c366-43fa-845c-737990abb745)。

#### 3. 利用不确定性量化与注意力机制的方法

这类方法通过显式建模深度估计的不确定性、强调通道信息或融合多摄像头数据来提高精度和鲁棒性。

*   **"基于不确定性度量的自监督单目深度估计" (2023)**：本研究旨在通过设计不确定性度量策略，在训练过程中检测单目深度估计中的不准确区域并引导网络学习。它采用Snapshot和Siam网络结构来量化不确定性，将不确定性约束添加到损失函数以加强对这些区域的学习，并提出基于集成的后处理策略修正深度图。实验表明，该方法在多种量化指标上优于基线模型和现有不确定性方法，尤其提升了尖锐物体深度估计的准确性 [jcst.ict.ac.cn](https://jcst.ict.ac.cn/cn/article/doi/10.1007/s11390-023-3088-y)。
*   **"Channel Attentive Self-supervised Network for Monocular Depth Estimation" (2023)**：该论文提出一种基于自监督深度学习和通道注意力的深度估计方法。研究目标是解决以往方法忽略图像中通道信息，导致深度估计精度受限的问题。核心方法是在网络中引入SE (Squeeze-and-Excitation) 模块以捕捉特征图中通道间关系，并设计多尺度融合通道注意力模块以融合多尺度像素特征和重新校准通道权重。在KITTI数据集上的实验验证了该方法在精度、误差和深度图细节效果上优于现有自监督深度估计方法 [html.rhhz.net](https://html.rhhz.net/GDGYDXXB/html/1680831667538-1432911339.htm)。
*   **"M${^2}$Depth: Self-supervised Two-Frame Multi-camera Metric Depth Estimation" (2024)**：该研究提出M$^2$Depth，一个自监督双帧多摄像头度量深度估计网络，旨在解决自动驾驶中可靠、尺度感知的周围深度估计问题。与以往方法不同，M$^2$Depth输入来自多个摄像头的时间相邻两帧图像，通过构建空间和时间域的代价体，并提出空间-时间融合模块整合信息。同时，它结合SAM特征的神经先验与内部特征，减少前景背景歧义并加强深度边缘。在nuScenes和DDAD基准测试中，M$^2$Depth实现了最先进的性能 [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/f0316ba8-fa2c-4e7d-833b-390e3cbe0531)。

### 实验与评价总结

2022-2025年的非监督和半监督深度估计研究在多个公开数据集上进行了广泛评估，特别是自动驾驶领域的KITTI和nuScenes，以及Make3D和CityScapes等。这些方法普遍采用的评估指标包括绝对相对误差 (Abs Rel)、平方相对误差 (Sq Rel)、均方根误差 (RMSE)、均方根对数误差 (RMSElog) 以及不同阈值下的准确率 ($\delta < 1.25^n$)。

共性结论表明，引入更精细的网络架构（如结合CNN与Transformer）、优化特征提取（如多尺度特征增强、局部特征引导、通道注意力）、增强对复杂场景的适应性（如夜间增强、对抗训练）以及利用先进的自监督机制（如知识蒸馏、不确定性量化）均能显著提升深度估计的精度、鲁棒性和泛化能力。具体而言，模型的输出深度图在物体边缘清晰度、细节恢复、结构一致性以及对无纹理区域和动态物体的处理上均有明显改善。

### 趋势与挑战

**趋势预测：**

1.  **大规模预训练模型的融合与适配：** 随着Jasmine等工作成功将Stable Diffusion等大规模生成模型的先验知识引入自监督深度估计，未来将有更多研究探索如何有效、高效地利用这些通用视觉先验，解决传统自监督方法在细节、泛化能力和鲁棒性上的不足，并可能出现针对特定任务（如深度估计）进行轻量化适配的预训练模型。
2.  **多模态数据融合的深度学习：** 结合雷达、Lidar等传感器的稀疏准确深度信息与单目图像的密集纹理信息，进行非监督或半监督的多模态融合深度估计将成为重要方向，旨在兼顾精度和成本。例如M$^2$Depth利用多相机克服单一视角的局限性。
3.  **鲁棒性与安全性的进一步提升：** 针对极端条件（如恶劣天气、超低/高光照）、动态复杂场景以及潜在的对抗攻击，发展更鲁棒的模型是必然趋势。不确定性量化、对抗训练等技术将继续被探索，以提高模型在实际部署中的可靠性。

**挑战：**

1.  **尺度模糊性的根本解决：** 单目深度估计固有的尺度模糊性在非监督学习中仍是一个难题，尽管部分方法通过多帧或多视角的几何约束有所缓解，但在绝对尺度恢复和不同场景间的尺度一致性方面仍面临挑战。
2.  **动态场景与遮挡的处理：** 尽管许多方法尝试通过掩膜、光流或语义引导来处理动态物体和遮挡，但复杂多变的动态交互和严重遮挡场景下，生成精确且无伪影的深度图仍具挑战。
3.  **计算效率与模型复杂度的平衡：** 引入更复杂的网络结构（如Vision Transformer）、更大的预训练模型以及多任务联合学习，往往会增加模型的参数量和计算复杂度，如何在提高性能的同时保持模型的轻量化和推理速度，是实际应用中必须面对的问题。

### 结论

2022-2025年期间，非监督和半监督深度估计领域取得了显著进展。研究的核心驱动力在于如何摆脱对昂贵深度真值标注的依赖，同时在精度、鲁棒性和泛化能力上逼近甚至超越监督方法。通过引入更先进的神经网络架构、创新的自监督信号设计和对模型不确定性的有效利用，该领域的研究成果在模拟真实世界复杂场景的几何感知方面展现出巨大潜力。未来的研究将继续受益于大规模预训练模型的强大先验，并着力于解决尺度一致性、极端环境适应性以及计算效率等关键挑战，为更广泛的实际应用铺平道路。

### 参考文献

1.  王中元, 艾浩军, 张锋, 吕鹏飞, 唐雪华. 局部特征引导的室内自监督单目深度估计方法. 计算机研究与发展, 2025, 62(7): 1599-1616. [crad.ict.ac.cn](https://crad.ict.ac.cn/article/doi/10.7544/issn1000-1239.202440951)
2.  Zou, Y., Ding, Y., Qiu, X., Wang, H., & Zhang, H. M${^2}$Depth: Self-supervised Two-Frame Multi-camera Metric Depth Estimation. 智源社区论文, 2024. [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/f0316ba8-fa2c-4e7d-833b-390e3cbe0531)
3.  Cheng, Z., Han, C., Liang, J., Wang, Q., Zhang, X., & Liu, D. Self-Supervised Adversarial Training of Monocular Depth Estimation against Physical-World Attacks. 智源社区论文, 2024. [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/ee0c8799-c366-43fa-845c-737990abb745)
4.  寇旗旗, 王伟臣, 韩成功, 吕晨, 程德强, 姬玉成. 多尺度特征增强的多帧自监督单目深度估计. 光学 精密工程, 2024, 32(24): 3603. [opticsjournal.net](https://www.opticsjournal.net/Articles/OJa00c675cd4311d5f/FullText)
5.  Wu, J., & He, Y. Channel Attentive Self-supervised Network for Monocular Depth Estimation. JOURNAL OF GUANGDONG UNIVERSITY OF TECHNOLOGY, 2023, 40(2): 22-29. [html.rhhz.net](https://html.rhhz.net/GDGYDXXB/html/1680831667538-1432911339.htm)
6.  郑千惠, 孔玲君. 混合CNN和ViT的自监督知识蒸馏单目深度估计方法. 建模与仿真, 2024, 13(03): 2868-2880. [hanspub.org](https://image.hanspub.org/html/80-2571621_87686.htm)
7.  李远珍, 郑圣杰, 谭梓欣, 曹拓, 罗飞, 肖春霞. 基于不确定性度量的自监督单目深度估计. 计算机科学技术学报, 2023, 38(4): 733-747. [jcst.ict.ac.cn](https://jcst.ict.ac.cn/cn/article/doi/10.1007/s11390-023-3088-y)
8.  aaooli. Jasmine论文浅读（自监督深度估计SOTA）. 博客园, 2025. [cnblogs.com](https://www.cnblogs.com/aaooli/p/19137028)
9.  郑宇鹏. ICRA 2023 | 首个联合暗光增强和深度估计的自监督方法STEPS_夜间图像深度估计. CSDN博客, 2025. [blog.csdn.net](https://blog.csdn.net/hanseywho/article/details/129146059)
10. Zhou, T., Brown, M., Snavely, N., & Lowe, D. G. Unsupervised learning of depth and ego-motion from video. Proc. IEEE Conf. Comput. Vis. Pattern Recognit., 2017, pp. 6612–6619.
11. Godard, C., Aodha, O., & Brostow, G. J. Unsupervised monocular depth estimation with left-right consistency. Proc. IEEE Conf. Comput. Vis. Pattern Recognit., 2017, pp. 6602–6611.
12. Godard, C., Aodha, O. M., Firman, M., & Brostow, G. J. Digging into self-supervised monocular depth estimation. Proc. IEEE Int. Conf. Comput. Vis., 2019, pp. 3827–3837.