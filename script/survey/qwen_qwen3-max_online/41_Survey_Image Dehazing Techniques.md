# 图像去雾技术研究综述（2022–2025）

## 引言

图像去雾旨在从受大气散射影响的退化图像中恢复清晰、真实的场景信息，对自动驾驶、遥感、安防监控等计算机视觉系统至关重要。近年，该领域经历了从基于物理模型与先验知识的方法向以深度学习为主导的范式迁移。2022–2025年间，研究前沿聚焦于解决合成数据与真实场景间的域偏移问题、提升模型对复杂雾霾（如非均匀、低光照雾霾）的鲁棒性，以及探索生成式模型（如扩散模型、Transformer）在图像复原中的潜力。本文系统梳理此期间代表性工作，按方法范式分类评述，并总结共性挑战与未来趋势。

## 方法分类与代表作

### 1. 基于物理先验的优化方法

尽管深度学习主导研究，对经典物理模型的精细化改进仍在特定场景（如含天空区域）展现出价值。赵代顺等人 [1] 针对暗通道先验（DCP）在天空区域易导致颜色失真和光晕伪影的问题，提出一种快速去雾算法。该方法结合图像分割技术精确估计大气光值，并采用快速引导滤波与加权最小二乘联合滤波优化透射率图。在包含天空的室外图像上，其信息熵（IE）达7.6945，SSIM为0.85，显著优于传统DCP。

宋晓东等人 [2] 专门针对海雾图像去雾，提出基于天空区域分割的算法。通过阈值分割与区域生长精确分离天空，并选择该区域亮度最高的前0.1%像素的中值作为大气光强。同时引入自适应修正因子优化快速引导滤波后的透射率。实验表明，该方法在海雾图像上的PSNR与SSIM指标显著提升，有效缓解了细节丢失与颜色失真。

### 2. 深度学习驱动的端到端方法

#### 2.1 监督学习方法

有监督方法依赖合成的成对数据集（如有雾/无雾图像对），通过深度网络直接学习映射关系。赵志强与何进良 [3] 提出的HACNet，创新性地结合多域注意力机制（MDA）与上下文自适应感知网络（CAF）。HACNet通过混合注意力融合算法（HAF）整合局部与全局特征，并利用多尺度膨胀卷积增强对雾霾浓度区域差异的感知。在RESIDE、NH-Haze等数据集上，HACNet均优于当时最先进模型，尤其在平衡局部-全局细节方面表现突出。

#### 2.2 非监督与半监督学习方法

为克服真实成对数据稀缺的瓶颈，非/半监督方法成为研究热点。Yang等人 [4] 提出的D4（Dehazing via Decomposing transmission map into Density and Depth）框架，是此方向的里程碑工作。D4不依赖成对数据，而是通过一个自增强框架，从非成对的有雾与清晰图像中联合学习散射系数（密度）和场景深度图。利用估计的深度，模型可重新渲染不同厚度的雾图用于数据增强，从而提升泛化能力。D4在参数量和FLOPs更低的情况下，其去雾效果优于其他非成对方法。

孟小哲等人 [5] 针对真实雾霾常与低光照共存的复合问题，提出基于不变学习的去雾方法。该方法首先改进大气散射模型（ASM），引入伽马校正以合成更真实的“暗雾”数据集（DarkHaze）。其次，利用随机傅里叶特征（RFF）对网络提取的高维非线性特征进行线性化，并通过全局样本加权去相关消除特征间的虚假相关性，使网络学习到对域偏移鲁棒的不变特征。实验证明，该方法在真实数据集上有效缓解了亮度损失和雾残留问题。

徐航等人 [6] 提出一种半监督去雾网络（SSDN），通过局部数据增强模型（EDEM）模拟真实雾霾的非均匀分布。EDEM利用随机掩码生成具有真实雾度特征的增强图像，SSDN则通过一个共享权重的双分支结构（监督与无监督）进行训练。该框架在合成与真实数据集上均优于传统方法，证明了利用增强数据进行自监督能有效提升模型在真实世界的泛化性。

### 3. 生成式与混合架构方法

生成对抗网络（GAN）和Transformer等架构被广泛用于提升去雾结果的视觉真实感与全局一致性。林克正等人 [7] 提出一种结合注意力机制与PatchGAN判别器的去雾算法。其网络利用注意力机制为不同雾度区域自适应分配权重，并采用Inception模块预测全局相关的大气光值。在RESIDE数据集上，该方法在PSNR和SSIM上均优于CAP、DCP等基线，且在处理含天空图像时表现更稳定。

姜鑫等人 [8] 设计了全局和局部特征融合去雾网络，旨在克服CNN局部感受野的局限。该网络在U-Net架构中嵌入一个全局和局部特征融合模块（GLFFM），分别用Transformer和卷积操作提取全局依赖与局部细节。此外，还设计了全局位置编码生成器（PEG）以自适应地建模像素位置关系。在合成与真实数据集上，该方法均取得了最优的PSNR和SSIM指标，复原图像细节更丰富、色彩更真实。

## 实验与评价总结

2022–2025年的研究在实验设计与评价上呈现出以下共性：首先，**数据集**方面，除经典的合成数据集RESIDE [9] 外，越来越多的工作采用真实雾霾数据集进行验证，如O-HAZE [10]、NH-HAZE [11] 和DENSE-HAZE [12]，以评估模型在真实场景下的泛化能力。其次，**评价指标**趋于全面，除合成数据上常用的PSNR、SSIM外，针对真实数据无参考（No-Reference）的评价指标如NIMA [13]、BIQME [14] 和PM2.5 [15] 被广泛采用，以衡量图像美学质量、综合质量和去雾彻底性。最后，**实验结论**普遍表明，单纯在合成数据上训练的模型在真实场景中易出现过饱和、雾残留或亮度损失；而结合物理先验、利用非成对/半监督学习、或引入全局建模能力（如Transformer）的方法，在真实数据上展现出更强的鲁棒性和更好的视觉效果。

## 趋势与挑战

基于近期文献，2025年及以后的研究将呈现以下趋势：
1.  **生成式模型的深度融合**：随着扩散模型在图像生成领域的成功，其在图像复原（包括去雾）中的应用将成为新热点。初步工作 [16] 已开始探索基于扩散模型的去雾方法，其有望在生成图像的细节与真实性上超越GAN。
2.  **多任务与多模态联合学习**：去雾任务将不再孤立进行，而是与深度估计、语义分割等高级视觉任务联合优化。同时，利用多光谱、偏振等多模态信息辅助去雾，以突破单幅RGB图像的信息瓶颈，是解决极端雾霾场景的关键方向。
3.  **高效与自适应推理**：面向实际应用（如自动驾驶），模型的计算效率与对动态变化雾霾（如雾浓度快速变化）的自适应能力将成为核心挑战。轻量化架构设计、在线自适应学习以及硬件-算法协同优化将是重要研究路径。

## 结论

2022–2025年间，图像去雾技术在解决真实场景泛化、复杂雾霾处理以及模型架构创新等方面取得了显著进展。从对经典物理模型的精细化改进，到利用非/半监督学习缓解数据依赖，再到通过Transformer与GAN等生成式架构提升复原质量，研究范式日益多元且务实。未来，随着生成式模型、多模态融合和高效推理技术的发展，图像去雾有望在更多实际场景中实现稳健、高效、高质的应用。

## 参考文献

[1] 赵代顺, 高蕾, 李凌霄. 基于先验知识的图像快速去雾方法[J]. 应用数学进展, 2025, 14(4): 660-674.

[2] 王玥, 张海峰, 岳凤英, 宋晓东. 基于天空区域分割的海雾图像去雾算法[J]. 激光与光电子学进展, 2025, 62(6): 0637005.

[3] 赵志强, 何进良. 上下文协同与混合注意力机制驱动的图像去雾算法[J]. 计算机应用研究, 2025, 42(9): 2875-2880.

[4] Yang, Y., Wang, C., Liu, R., Zhang, L., Guo, X., & Tao, D. (2022). Self-Augmented Unpaired Image Dehazing via Density and Depth Decomposition. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)* (pp. 2027-2036).

[5] 孟小哲, 冯钰新, 苏卓, 周凡. 基于不变学习的真实雾霾去除方法[J]. 浙江大学学报(工学版), 2024, 58(2): 268-278.

[6] 徐航, 周杰, 赵丽, 胡杰. 基于深度学习的半监督图像去雾网络[J]. 计算机科学与应用, 2024, 14(4): 193-200.

[7] 林克正, 耿佳浩, 程卫月, 李骜. 基于注意力机制和马尔可夫判别器的图像去雾算法[J]. 激光与光电子学进展, 2022, 59(16): 1610003.

[8] 姜鑫, 聂海涛, 朱明. 全局和局部特征融合的图像去雾[J]. 光学精密工程, 2023, 31(18): 2687.

[9] Li, B., Ren, W., Fu, D., Tao, D., Feng, D., Zeng, W., & Wang, Z. (2019). Benchmarking single-image dehazing and beyond. *IEEE Transactions on Image Processing, 28*(1), 492-505.

[10] Ancuti, C. O., Ancuti, C., Timofte, R., & De Vleeschouwer, C. (2018). O-HAZE: A Dehazing Benchmark with Real Hazy and Haze-Free Outdoor Images. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops (CVPRW)*.

[11] Ancuti, C. O., Ancuti, C., & Timofte, R. (2020). NH-HAZE: An Image Dehazing Benchmark with Non-Homogeneous Hazy and Haze-Free Images. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops (CVPRW)*.

[12] Ancuti, C. O., Ancuti, C., Sbert, M., & Timofte, R. (2019). Dense-Haze: A Benchmark for Image Dehazing with Dense-Haze and Haze-Free Images. In *IEEE International Conference on Image Processing (ICIP)*.

[13] Talebi, H., & Milanfar, P. (2018). NIMA: Neural image assessment. *IEEE Transactions on Image Processing, 27*(8), 3998-4011.

[14] Gu, K., Tao, D., Qiao, J. F., Yang, J., & Zhou, W. (2017). Learning a no-reference quality assessment model of enhanced images with big data. *IEEE Transactions on Neural Networks and Learning Systems, 29*(4), 1301-1313.

[15] Gu, K., Qiao, J., & Li, X. (2018). Highly efficient picture-based prediction of PM2. 5 concentration. *IEEE Transactions on Industrial Electronics, 66*(4), 3176-3184.

[16] 曹倩雯, 李恭如. 单幅图像去雾的生成式方法研究现状[J]. 计算机应用研究, 2026, 43(1).