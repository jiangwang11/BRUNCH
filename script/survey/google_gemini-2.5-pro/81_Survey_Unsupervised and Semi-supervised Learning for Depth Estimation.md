好的，遵照您的指示，我将基于提供的搜索结果，生成一篇关于“自监督与半监督深度估计”的严谨中文学术综述。

---

### **面向深度估计的自监督与半监督学习研究综述 (2022–2025)**

#### **引言**

深度估计作为计算机视觉的核心任务之一，旨在从图像中推断出每个像素点的空间深度信息，对自动驾驶、三维重建、增强现实等领域至关重要。传统的监督学习方法虽然精度较高，但严重依赖于激光雷达（LiDAR）等昂贵设备采集的真值标签，限制了其大规模应用。为克服这一瓶颈，自监督单目深度估计（Self-Supervised Monocular Depth Estimation, SSMDE）应运而生。该范式仅利用连续的单目视频帧或双目图像对，通过视图合成（View Synthesis）构建光度重投影损失（Photometric Loss）作为监督信号，极大地降低了数据获取成本。

然而，自监督方法的基础——光度一致性假设，在处理遮挡、弱纹理区域、动态物体和光照变化等复杂现实场景时表现脆弱，导致监督信号失真，模型性能受限。针对这些挑战，2022至2025年间的研究工作在方法论上取得了显著进展，从早期的多帧信息融合、网络架构革新，逐步发展到引入知识蒸馏乃至大规模预训练模型的视觉先验。本综述将对这一时期的代表性工作进行分类、总结与展望。

#### **方法分类与代表作**

##### **1. 多源信息融合与时序利用**

该类方法通过融合来自多个摄像头或更多视频帧的信息来增强几何约束，以克服单目双帧输入的局限性。

*   **M²Depth (2024)** [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/f0316ba8-fa2c-4e7d-833b-390e3cbe0531)
    *   **研究问题**: 如何在自动驾驶场景中实现具有尺度感知的360°环视深度估计。
    *   **核心方法**: 提出一种双帧、多摄像头的自监督网络M²Depth，它同时在空间（多摄像头）和时间（双帧）维度上构建代价体（Cost Volume）。通过一个时空融合模块整合信息，并引入SAM（Segment Anything Model）的特征作为神经先验，以强化深度边缘和区分前景/背景。
    *   **关键结论**: 在nuScenes和DDAD等环视数据集上取得了最先进的性能，证明了融合时空多源信息对于生成高质量、尺度一致的周围深度至关重要。

*   **寇旗旗等人 (2024)** [opticsjournal.net](https://www.opticsjournal.net/Articles/OJa00c675cd4311d5f/FullText)
    *   **研究问题**: 现有室外场景深度估计网络对空间特征提取不充分，导致物体边缘模糊和伪影。
    *   **核心方法**: 提出一种多尺度特征增强的多帧自监督模型。在编码器中引入基于大核注意力（Large Kernel Attention, LKA）的激活模块以捕获全局空间上下文，并设计结构增强模块以感知通道维度的重要结构特征。解码器则采用动态上采样方法来恢复细节。
    *   **关键结论**: 在KITTI数据集上的预测正确率（δ<1.25）达到90.3%，定量和定性结果均表明该模型生成的深度图边缘更清晰、伪影更少，优于当时的主流算法。

##### **2. 知识蒸馏与混合架构**

此类方法利用教师-学生模型框架或融合不同类型的网络（如CNN和Transformer）来提升模型性能、效率或可解释性。

*   **HCVNet (2024)** [image.hanspub.org](https://image.hanspub.org/html/80-2571621_87686.htm)
    *   **研究问题**: 如何有效结合CNN的局部信息捕获能力和Vision Transformer（ViT）的全局依赖建模能力，同时解决模型效率问题。
    *   **核心方法**: 提出HCVNet，设计了CNN-ViT混合特征编码器以高效提取局部与全局特征。引入单阶段自监督知识蒸馏，利用上一轮训练的模型作为教师指导当前轮次的训练，避免了同时训练两个模型的开销。同时，使用通道特征聚合模块增强场景结构感知。
    *   **关键结论**: 在KITTI和Make3D数据集上均展现出优于主流方法的性能和泛化能力，证明了混合架构与自蒸馏结合的有效性。

*   **LoFtDepth (2025)** [crad.ict.ac.cn](https://crad.ict.ac.cn/article/doi/10.7544/issn1000-1239.202440951)
    *   **研究问题**: 自监督方法在结构复杂的室内场景中性能下降明显。
    *   **核心方法**: 提出LoFtDepth，一种面向室内场景、由局部特征引导的知识蒸馏方法。它使用一个预训练的深度估计网络生成结构化的深度图作为“深度先验”，并从中提取边界点等局部特征知识，通过知识蒸馏迁移至自监督网络中，同时引入法线损失和位姿一致性约束。
    *   **关键结论**: 在室内公开数据集上将相对误差降至0.121，生成的深度图具有更高的全局准确度和结构完整性。

*   **CCDepth (2024)** [cup.edu.cn](https://www.cup.edu.cn/cupai/kxyj/kydt/15c2b941d7af475caafdaf85f3700225.htm)
    *   **研究问题**: 现有深度估计模型参数量过大，难以部署于边缘设备，且作为“黑盒”模型缺乏可解释性。
    *   **核心方法**: 提出轻量化网络CCDepth，其编码器由CNN和“白盒”CRATE（Coding Rate reduction TransformEr）网络混合构成。CNN用于提取高分辨率特征图的局部信息，CRATE则在低分辨率特征图上捕捉可被数学解释的全局信息。
    *   **关键结论**: 在保持与先进方法相当性能的同时，模型参数量显著减少（如比Monodepth2减少78.8%），并首次为自监督深度估计模型的全局特征提取过程提供了数学可解释性。

##### **3. 引入大规模模型先验**

这是2024-2025年前后最前沿的方向，旨在利用Stable Diffusion等大规模生成模型的强大视觉先验来解决自监督学习的固有缺陷。

*   **Jasmine (2025)** [cnblogs.com](https://www.cnblogs.com/aaooli/p/19137028)
    *   **研究问题**: 如何在不破坏大规模扩散模型（如Stable Diffusion）珍贵预训练先验的前提下，将其强大能力注入到充满“噪声”监督信号的自监督深度估计框架中。
    *   **核心方法**: 提出Jasmine框架，包含两大核心组件：1) **混合批次图像重建 (MIR)**，在训练批次中混合真实帧（用于自监督深度学习）和高质量自然图像（用于图像重建任务），以“干净”的重建信号锚定扩散模型的视觉先验；2) **尺度-位移门控循环单元 (SSG)**，对齐扩散模型输出的尺度-位移不变深度与自监督所需的尺度不变深度，并过滤有害梯度。
    *   **关键结论**: 在KITTI基准上达到新的SOTA水平，并在多个数据集上展现出卓越的零样本泛化能力。其生成的深度图细节（如水面倒影、纤细栏杆）前所未有地丰富，标志着该领域的范式转变。

##### **4. 创新网络结构与注意力机制**

这类研究通过设计新颖的卷积或注意力模块，从网络结构层面优化特征表达。

*   **吴俊贤等人 (2023)** [html.rhhz.net](https://html.rhhz.net/GDGYDXXB/html/1680831667538-1432911339.htm)
    *   **研究问题**: 以往方法忽略了图像特征中的通道维度信息，限制了网络表达能力。
    *   **核心方法**: 在Monodepth2的基础上，通过在编码器中插入SE（Squeeze-and-Excitation）模块，并设计一个多尺度融合通道注意力模块（CADC）用于解码器，以显式地对通道间依赖关系进行建模和重校准。
    *   **关键结论**: 在KITTI数据集的多种训练设置下，精度和误差指标均超越了基线模型，生成的深度图细节更清晰，证明了通道注意力机制的有效性。

*   **ICCV 2023·方向感知累积卷积 (2024)** [blog.csdn.net](https://blog.csdn.net/weixin_43559672/article/details/136353717)
    *   **研究问题**: 深度预测对物体的环境和方向信息（如垂直与水平平移）敏感，而传统卷积对此处理效率低下。
    *   **核心方法**: 提出“方向感知模块”和“累积卷积”。前者通过可学习的仿射变换改变采样密度，使网络能差异化地处理不同方向的信息；后者受“地平面是关键参考”的启发，从下至上累积信息，以更好地利用连接区域的深度线索。
    *   **关键结论**: 实验表明，深度估计确实具有方向敏感性（垂直拉伸图像改善性能，水平拉伸则恶化），所提出的模块能有效利用此先验提升性能。

#### **实验与评价总结**

*   **基准数据集**: 户外自动驾驶场景的评估主要在 **KITTI** 和 **CityScapes** 数据集上进行。**Make3D** 数据集常被用于评估模型对不同场景的泛化能力。随着多摄像头方案的兴起，**nuScenes** 等360°环视数据集的应用日益增多。
*   **评价指标**: 沿用标准度量体系。误差指标包括绝对相对误差（Abs Rel）、平方相对误差（Sq Rel）、均方根误差（RMSE）和对数均方根误差（RMSE log），这些指标数值越低越好。精度指标为准确率（δ < 1.25, δ < 1.25², δ < 1.25³），数值越高越好。
*   **共性结论**:
    1.  **多源信息优势**: 融合多帧或多摄像头信息（如M²Depth, 寇旗旗等人）能提供更强的几何约束，在精度和尺度一致性上系统性优于仅依赖双帧的单目方法。
    2.  **混合架构的平衡性**: CNN与Transformer的混合架构（如HCVNet, CCDepth）已被证实是权衡局部细节与全局上下文的有效策略，其性能普遍超越了纯CNN架构。
    3.  **知识蒸馏的有效性**: 无论是利用预训练模型的先验知识（LoFtDepth）还是自蒸馏（HCVNet），知识蒸馏都是一种行之有效的性能提升手段，尤其能改善学生模型在弱纹理和边界区域的表现。
    4.  **基础模型先验的颠覆性**: 引入扩散模型先验（Jasmine）带来了质的飞跃，不仅在已知数据集上刷新记录，更重要的是其强大的零样本泛化能力和无与伦比的细节恢复能力，预示了新的技术范式。
    5.  **定性提升**: 相比早期模型，近期工作生成的深度图在物体边缘、细小结构（如栏杆、路灯）和远景的轮廓上更加清晰锐利，伪影也显著减少。

#### **趋势与挑战**

基于2022至2025年的研究进展，未来几年的研究趋势与挑战可预见如下：

1.  **大规模基础模型的深度融合与高效利用**: `Jasmine`的成功开启了利用基础模型（Foundation Models）先验的大门。未来的研究将不再局限于将深度估计作为下游任务进行微调，而是探索更深度的融合方式。**趋势**包括：① 探索多模态基础模型（如结合语言描述）为深度估计提供更高级的语义引导；② 研究更高效的参数高效微调（Parameter-Efficient Fine-Tuning, PEFT）和蒸馏技术，以更低的计算成本将基础模型的能力迁移到轻量化模型中。**挑战**在于如何设计机制，在利用先验的同时，避免模型产生“幻觉”或忽略真实的几何约束。

2.  **面向部署的轻量化、可解释性与鲁棒性**: 随着技术走向应用，模型在边缘设备（如车载芯片）上的部署成为刚需。`CCDepth`已展现出轻量化与可解释性的潜力。**趋势**包括：① 设计专为移动端优化的、兼顾精度与速度的混合网络架构；② 发展如 `CRATE` 这样的“白盒”或可解释模块，增强模型在安全关键应用（如自动驾驶）中的可信度。此外，如**对抗训练研究** [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/ee0c8799-c366-43fa-845c-737990abb745) 所示，提升模型在物理世界攻击下的鲁棒性也是一个重要方向。

3.  **解耦动态场景与统一感知**: 自监督方法的核心痛点——静态场景假设，仍是制约其在真实世界应用的主要障碍。**趋势**包括：① 将深度估计与光流、实例分割、运动分割等任务进行更紧密的联合学习，显式地解耦相机运动与物体自身运动；② 发展能够为场景中每个动态对象估计独立位姿的模型，如 **Boulahbal (2024) 的工作** [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/16612598-de11-4898-8a90-f75f0190d9c3) 所述；③ 将深度预测从“感知过去”扩展到“预测未来”，即从视频序列中预测未来的深度图，为决策规划提供更长的时间窗口。

#### **结论**

2022至2025年，自监督与半监督深度估计领域经历了从优化现有范式到引入革命性新技术的快速演进。研究者们通过多源信息融合、设计精巧的混合架构与知识蒸馏策略，不断提升模型的精度、鲁棒性和效率。其中，将大规模扩散模型先验成功注入自监督框架是此阶段最具标志性的突破，它极大地提升了深度图的细节保真度和泛化能力。展望未来，该领域将朝着与基础模型更深度融合、追求轻量化与可解释性、以及攻克动态复杂场景三大方向持续发展，逐步推动高精度、高可靠性的深度感知技术从实验室走向真实世界应用。

#### **参考文献**

1.  Zou, Y., Ding, Y., Qiu, X., Wang, H., & Zhang, H. (2024). *M²Depth: Self-supervised Two-Frame Multi-camera Metric Depth Estimation*. Retrieved from [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/f0316ba8-fa2c-4e7d-833b-390e3cbe0531)
2.  寇旗旗, 王伟臣, 韩成功, 吕晨, 程德强, & 姬玉成. (2024). 多尺度特征增强的多帧自监督单目深度估计. *光学 精密工程*, 32(24). Retrieved from [opticsjournal.net](https://www.opticsjournal.net/Articles/OJa00c675cd4311d5f/FullText)
3.  郑千惠, & 孔玲君. (2024). 混合CNN和ViT的自监督知识蒸馏单目深度估计方法. *建模与仿真*, 13(03). Retrieved from [image.hanspub.org](https://image.hanspub.org/html/80-2571621_87686.htm)
4.  艾浩军, 张锋, 吕鹏飞, 唐雪华, & 王中元. (2025). 局部特征引导的室内自监督单目深度估计方法. *计算机研究与发展*. Retrieved from [crad.ict.ac.cn](https://crad.ict.ac.cn/article/doi/10.7544/issn1000-1239.202440951)
5.  张熙, 薛亚茹, 贾邵程, & 裴新. (2024). CCDepth：一种可解释性增强的轻量化自监督深度估计网络. *IEEE ITSC*. Retrieved from [cup.edu.cn](https://www.cup.edu.cn/cupai/kxyj/kydt/15c2b941d7af475caafdaf85f3700225.htm)
6.  aaooli. (2025). Jasmine论文浅读（自监督深度估计SOTA）. Retrieved from [cnblogs.com](https://www.cnblogs.com/aaooli/p/19137028)
7.  吴俊贤, & 何元烈. (2023). 基于通道注意力的自监督深度估计方法. *广东工业大学学报*, 40(2). Retrieved from [html.rhhz.net](https://html.rhhz.net/GDGYDXXB/html/1680831667538-1432911339.htm)
8.  weixin_43559672. (2024). 【自监督单目深度估计】Self-Supervised Monocular Depth Estimation by Direction-aware Cumulative（ICCV23）. Retrieved from [blog.csdn.net](https://blog.csdn.net/weixin_43559672/article/details/136353717)
9.  Cheng, Z., Han, C., Liang, J., Wang, Q., Zhang, X., & Liu, D. (2024). *Self-supervised Adversarial Training of Monocular Depth Estimation against Physical-World Attacks*. Retrieved from [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/ee0c8799-c366-43fa-845c-737990abb745)
10. Boulahbal, H. (2024). *On depth prediction for autonomous driving using self-supervised learning*. Retrieved from [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/16612598-de11-4898-8a90-f75f0190d9c3)
11. Godard, C., Aodha, O. M., Firman, M., et al. (2019). Digging into self-supervised monocular depth estimation. *Proceedings of the IEEE/CVF International Conference on Computer Vision*.
12. Watson, J., Mac Aodha, O., Prisacariu, V., et al. (2021). The temporal opportunist: Self-supervised multi-frame monocular depth. *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition*.