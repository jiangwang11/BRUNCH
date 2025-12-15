# 单图像去雾技术与深度学习结合的增强方法综述（2022–2025）

## 引言

单图像去雾旨在从受大气散射退化的图像中恢复无雾清晰内容，是提升恶劣天气下计算机视觉系统鲁棒性的关键预处理环节。传统基于物理模型（如暗通道先验）或图像增强的方法普遍存在泛化性差、细节失真等问题。2016年DehazeNet的提出标志深度学习正式进入该领域。2022至2025年间，研究焦点从单纯提升合成数据集指标转向改善真实场景泛化能力，涌现出生成式先验建模、物理引导的混合架构、无/半监督范式等创新方向。本文系统综述此阶段代表性工作，聚焦方法论创新与真实世界性能。

## 方法分类与代表作

### 1. 生成式无监督与半监督方法

为克服合成-真实域差异，无监督/半监督方法利用未配对数据训练。Yang 等人提出的 **D4**（CVPR 2022）[zhihu] 通过自增强框架，联合估计雾霾密度（散射系数）与场景深度，并利用估计的深度重新渲染不同厚度的雾图进行数据增强。该方法在非配对设定下，于真实图像上取得了优于Cycle-Dehaze等方法的PSNR/SSIM，同时参数量更低。

徐航等人（2024）[hans1] 提出的 **SSDN** 框架引入局部数据增强模型（EDEM），利用随机掩码模拟真实雾霾的非均匀性。其半监督训练策略结合了配对合成数据的监督损失与真实雾图的暗通道、总变差及自监督损失，在RTTS真实数据集上展现出更优的色彩保真度，有效缓解了天空区域颜色失真问题。

曹倩雯与李恭如（2025）[arocmag] 系统综述了生成式方法，特别指出 **Cycle-Dehaze**（CVPRW 2018）作为早期GAN应用，通过循环一致性损失实现非配对训练，但其忽略物理先验导致泛化受限。近期工作如D4和SSDN通过融入物理约束，显著提升了无监督去雾的稳定性与真实感。

### 2. 混合架构与注意力机制

为兼顾全局建模与局部细节，研究者融合CNN与Transformer。**HA-Net**（2025）[xuekanba] 设计了混合注意力模块，将改进的Transformer块与并行卷积层结合，分别捕捉长程依赖与局部纹理。其增强特征融合模块通过门控卷积和选择性核融合，有效应对了多变的雾霾分布。在RESIDE数据集上，HA-Net取得了室内集SOTA的PSNR（40.08 dB）和SSIM（0.995）。

姜鑫等人（2023）[opticsjournal] 提出的 **全局和局部特征融合网络**，利用Transformer提取全局特征，卷积提取局部特征，并设计了全局位置编码生成器（GPEG），能自适应地根据图像内容生成位置编码。该模型在合成数据集（PSNR 33.19 dB）和真实数据集（PSNR 19.31 dB）上均优于FFA-Net等基线，消融实验证实了GPEG对细节还原的关键作用。

张世辉等人（2022）[jeit] 的 **多尺度特征结合细节恢复方法**，首先通过多尺度特征提取与非线性加权融合模块获得初步去雾结果，再通过一个独立的基于图像分块的细节恢复网络提取高频信息并融合。该两阶段策略在SOTS室外集上PSNR达33.78，O-HAZE真实数据集上PSNR为25.80，显著优于FFA-Net和MSBDN。

### 3. 物理模型引导的深度学习

为提升模型可解释性与物理一致性，研究者将大气散射模型显式或隐式融入网络。**GRIDDehazeNet**（ICCV 2019）虽略早于综述窗口，但其作为注意力多尺度网络的代表，不依赖大气散射模型，通过GridNet架构高效交换多尺度信息，为后续设计奠定基础。吉波涛与陆利坤（2025）[hans2] 的综述指出，后期工作如PSD（CVPR 2021）通过引入物理兼容头，分别生成透射图和无雾图像，并估计大气光，显著提升了真实世界去雾的视觉质量。

**4kDehazing**（CVPR 2021）[hans2] 通过多引导双边学习和双边网格学习，从输入雾图中生成更多边缘和高频细节。该三阶段CNN网络能在单GPU上实现实时4K去雾，在大规模数据集上效果优于早期端到端模型，展示了物理先验与深度学习结合在高分辨率场景下的优势。

## 实验与评价总结

近年研究在评价上呈现两大共性趋势。首先，**评价基准多元化**：除传统的合成数据集（RESIDE）外，真实或接近真实的数据集（如I-HAZE, O-HAZE, NH-HAZE, BeDDE）被广泛采用。BeDDE等新基准甚至引入了可见性指数（VI）和真实性指数（RI）等更贴近人类感知的指标。其次，**评价指标综合化**：除PSNR/SSIM外，研究者常结合下游任务（如目标检测mAP）评估去雾结果的实用性，并通过用户研究评价视觉真实感。大量实验表明，过度优化合成数据上的PSNR/SSIM指标的模型（如有监督模型）在真实图像上往往表现不佳，而融入物理约束或生成式先验的无/半监督方法在真实场景中泛化能力更强，色彩与细节还原更自然。

## 趋势与挑战

基于对2022-2025年工作的分析，未来研究将聚焦以下方向：
1.  **生成式先验与扩散模型的深度整合**：扩散模型（如DiffIR）在图像复原任务中展现了强大的先验建模能力。未来工作将探索如何将雾天成像的物理先验（如深度、散射系数）与扩散过程结合，构建更高效的生成式去雾模型。
2.  **真实世界数据驱动的自监督学习**：鉴于真实配对数据的稀缺性，研究将转向更强大的自监督和弱监督范式。例如，利用视频时序一致性、多视角几何约束或单张图像内部统计规律（如D4的自增强）来监督模型训练。
3.  **多任务与多模态融合**：去雾将不再被视为孤立的预处理步骤，而是与高层视觉任务（如检测、分割）联合优化。同时，探索如何利用其他传感器模态（如深度、偏振）信息来引导和约束单目RGB图像的去雾过程，将是一个重要挑战。

## 结论

2022至2025年间，单图像去雾研究在深度学习的驱动下，从追求合成数据指标转向解决真实世界泛化性问题。通过引入生成式模型、混合网络架构及物理引导机制，代表性工作在保持物理合理性的同时，显著提升了去雾结果的真实感与实用性。未来，与扩散模型、自监督学习及多任务学习的深度融合，将推动该技术向更鲁棒、更高效的实用化方向发展。

## 参考文献

[1] Yang, Y., Wang, C., Liu, R., Zhang, L., Guo, X., & Tao, D. (2022). Self-Augmented Unpaired Image Dehazing via Density and Depth Decomposition. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)* (pp. 2027-2036). [zhihu]

[2] 徐航, 周杰, 赵丽, & 胡杰. (2024). 基于深度学习的半监督图像去雾网络. *计算机科学与应用, 14*(4), 193-200. https://doi.org/10.12677/csa.2024.144089 [hans1]

[3] 曹倩雯, & 李恭如. (2025). 单幅图像去雾的生成式方法研究现状. *计算机应用研究, 43*(1). https://doi.org/10.19734/j.issn.1001-3695.2025.06.0198 [arocmag]

[4] 用于单张图像去雾的混合注意力网络论文. (2025). *学刊吧*. Retrieved from https://www.xuekanba.com/lunwen/ligong/4-17635.html [xuekanba]

[5] 姜鑫, 聂海涛, & 朱明. (2023). 全局和局部特征融合的图像去雾. *光学精密工程, 31*(18), 2687. https://doi.org/10.37188/OPE.20233118.2687 [opticsjournal]

[6] 张世辉, 路佳琪, 宋丹丹, & 张晓微. (2022). 基于多尺度特征结合细节恢复的单幅图像去雾方法. *电子与信息学报, 44*(11), 3967-3976. https://doi.org/10.11999/JEIT210868 [jeit]

[7] 吉波涛, & 陆利坤. (2025). 基于深度学习的图像去雾研究综述. *图像与信号处理, 14*(1), 21-33. https://doi.org/10.12677/jisp.2025.141003 [hans2]

[8] Liu, X., Ma, Y., Shi, Z., & Chen, J. (2019). GridDehazeNet: Attention-Based Multi-Scale Network for Image Dehazing. In *2019 IEEE/CVF International Conference on Computer Vision (ICCV)* (pp. 7313-7322). IEEE. [hans2]

[9] Chen, Z., Wang, Y., Yang, Y., & Liu, D. (2021). PSD: Principled Synthetic-to-Real Dehazing Guided by Physical Priors. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)* (pp. 7176-7185). [hans2]

[10] Zheng, Z., Ren, W., Cao, X., Hu, X., Wang, T., Song, F., et al. (2021). Ultra-High-Definition Image Dehazing via Multi-Guided Bilateral Learning. In *2021 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)* (pp. 16180-16189). IEEE. [hans2]

[11] Engin, D., Genc, A., & Ekenel, H. K. (2018). Cycle-Dehaze: Enhanced CycleGAN for Single Image Dehazing. In *2018 IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops (CVPRW)* (pp. 938-9388). IEEE. [arocmag]

[12] Xia, B., Zhang, Y., Wang, S., Wang, Y., Wu, X., Tian, Y., Yang, W., & Van Gool, L. (2023). DiffIR: Efficient Diffusion Model for Image Restoration. *arXiv preprint arXiv:2303.09472*. [zhuanzhi]