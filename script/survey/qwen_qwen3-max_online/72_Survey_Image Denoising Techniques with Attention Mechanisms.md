# 基于注意力机制的图像去噪技术综述（2022–2025）

## 引言

图像去噪作为底层视觉的核心任务，其目标是从含噪观测中恢复潜在的清晰图像。近年来，注意力机制因其对特征重要性进行动态建模的能力，已被广泛集成到深度去噪网络中，显著提升了去噪性能。本文聚焦2022至2025年间的真实发表成果，系统梳理了基于注意力机制的图像去噪方法，涵盖通道注意力、自注意力、混合失真处理及自监督学习等前沿方向。本综述旨在为研究者提供清晰的技术演进脉络与未来研究方向。

## 方法分类与代表作

### 1. 通道注意力机制

通道注意力通过学习各特征通道的权重，增强对去噪任务有用的特征并抑制冗余信息。余维等人（2025）[cttacn.org.cn](https://cttacn.org.cn/article/doi/10.15953/j.ctta.2025.068)针对工业CT图像去噪，将Squeeze-and-Excitation（SE）模块嵌入解码器阶段。该方法自适应调整通道权重，在去除噪声的同时有效保留了图像的结构细节，在视觉效果和定量指标上均优于经典方法。贾小宁等人（2024）[hanspub.org](https://image.hanspub.org/Html/9-1543124_84547.htm)提出了一种多级小波CNN模型，通过在U-Net的收缩与扩展路径中引入小波变换和通道注意力，有效平衡了感受野大小与计算效率。实验表明，该方法在高斯噪声下PSNR值较DnCNN等方法平均提升约10%，能有效保护遥感图像的边缘特征。

### 2. 自注意力与Transformer架构

自注意力机制能够捕获图像中的长距离依赖关系，克服了CNN感受野有限的缺点。江奎等人（2024）[cjig.cn](https://www.cjig.cn/zh/article/doi/10.11834/jig.230323/)提出了一种动态关联学习方法，将CNN的局部感知能力与自注意力（SA）的全局聚合能力相结合。其核心是一个多输入注意力模块（MAM），利用降质先验指导背景修复。该方法（ELF）在图像去雨、水下增强等任务上均取得显著提升，例如在Test1200数据集上比MPRNet的PSNR高出0.9 dB。Guo等人（2024）[chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/85148)针对Mamba模型的因果建模限制，提出了MambaIRv2，通过引入注意状态空间方程和语义引导的邻域机制，赋予其非因果建模能力。该模型在轻量级超分辨率任务中比SRFormer的PSNR提升了0.35dB，同时减少了9.3%的参数量。

### 3. 混合失真与多任务去噪

真实场景中的图像通常包含多种混合失真（如噪声、模糊、压缩伪影）。龚敏学等人（2022）[hanspub.org](https://image.hanspub.org/Html/2-1542465_49977.htm)提出了一种注意力引导的混合失真图像复原网络。该网络包含一个任务驱动的操作层，通过注意力机制对并行执行的多种操作（不同卷积、池化）进行加权，从而自适应地处理不同的退化类型。实验表明，该方法在处理包含噪声、模糊和JPEG压缩的混合失真图像时，PSNR和SSIM指标均优于现有的单任务模型（如DnCNN）和多任务模型（如RL-Restore）。

### 4. 自监督与无配对学习

自监督方法旨在解决真实去噪场景中缺乏成对清晰-含噪图像的难题。张晓东等人（2025）[opticsjournal.net](https://www.opticsjournal.net/Articles/OJ6f91743d6d014d4b/FullText)提出了一种基于记忆单元（MU）的多阶段自监督去噪方法（MM-SSID）。该方法通过记忆单元保存近似清晰的中间去噪结果来协同监督训练，并分阶段学习平坦区域与纹理区域的特征。在SIDD和DND数据集上，该方法分别达到了37.30 dB和38.52 dB的PSNR，显著优于Noise2Void、AP-BSN等现有自监督方法。一篇针对低剂量CT（LDCT）的研究（2024）[csdn.net](https://blog.csdn.net/qq_36584673/article/details/147085406)提出了WIA-LD2ND方法，该方法仅使用正常剂量CT（NDCT）数据进行自监督学习。其核心是通过向NDCT的高频分量添加噪声来对齐LDCT，并设计频率感知多尺度损失来捕获细节，性能超越了多种弱监督和自监督方法。

## 实验与评价总结

对上述代表性工作的实验结果进行综合分析，可得出以下共性结论：1）在定量指标上，几乎所有注意力机制的引入都能带来PSNR和SSIM的显著提升（通常在0.3-1.0 dB范围内），且在真实噪声数据集（如SIDD、DND）上的提升更为明显。2）在视觉质量上，注意力机制能有效缓解传统CNN产生的过度平滑问题，在保留纹理、边缘等高频细节方面表现突出。3）计算效率方面，通道注意力因其轻量级特性，通常只带来极小的计算开销；而自注意力机制虽计算复杂度较高，但通过与CNN或状态空间模型（如Mamba）结合，可在性能与效率之间取得良好平衡。

## 趋势与挑战

基于对2022–2025年研究成果的分析，未来研究将呈现以下趋势：
1.  **架构融合与高效化**：将状态空间模型（如Mamba）与注意力机制结合，以线性复杂度实现全局建模，是平衡性能与效率的关键方向。
2.  **真实场景自监督深化**：针对真实噪声建模的不完美性，发展更鲁棒的自监督范式（如利用记忆单元、图像对齐）将成为主流，以减少对昂贵配对数据的依赖。
3.  **频域与空域联合建模**：利用小波变换、傅里叶变换等工具将图像分解至频域，并结合注意力机制进行针对性处理，能更精细地分离噪声与信号，是提升细节恢复能力的有效路径。

## 结论

注意力机制已成为推动图像去噪技术发展的核心动力之一。从早期的通道注意力到近期的自注意力、状态空间注意力，其演进体现了从局部特征重标定到全局上下文建模的深化。未来的研究将更加注重架构的高效性、对真实复杂噪声的鲁棒性以及多域（空域、频域）信息的协同利用。通过解决这些挑战，基于注意力的去噪模型有望在更广泛的现实应用中发挥关键作用。

## 参考文献

1.  余维, 王成祥, 何雨. 基于通道注意力机制的工业CT图像去噪网络. CT理论与应用研究, 2025. [cttacn.org.cn](https://cttacn.org.cn/article/doi/10.15953/j.ctta.2025.068)
2.  成丽波, 苑浩然, 李喆, 贾小宁. 基于注意力机制的多级小波CNN遥感图像去噪算法. 计算机科学与应用, 2024, 14(04): 73-82. [hanspub.org](https://image.hanspub.org/Html/9-1543124_84547.htm)
3.  Jiang Kui, Jia Xuemei, Huang Wenxin, et al. Dynamic association learning of self-attention and convolution in image restoration. Journal of Image and Graphics, 2024, 29(04): 890-907. [cjig.cn](https://www.cjig.cn/zh/article/doi/10.11834/jig.230323/)
4.  Guo H, Guo Y, Zha Y, et al. MambaIRv2: Attentive State Space Restoration. arXiv preprint arXiv:2411.15269, 2024. [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/85148)
5.  龚敏学, 朱烨, 符颖. 注意力机制引导的混合失真图像复原研究. 计算机科学与应用, 2022, 12(04): 775-784. [hanspub.org](https://image.hanspub.org/Html/2-1542465_49977.htm)
6.  张晓东, 祝令函, 高绍姝, 等. 基于记忆单元的多阶段图像自监督去噪方法. 激光与光电子学进展, 2025, 62(4): 0437003. [opticsjournal.net](https://www.opticsjournal.net/Articles/OJ6f91743d6d014d4b/FullText)
7.  Zhao M, et al. WIA-LD2ND: Wavelet-based Image Alignment for Self-supervised Low-Dose CT Denoising. arXiv preprint arXiv:2403.11672, 2024. [csdn.net](https://blog.csdn.net/qq_36584673/article/details/147085406)
8.  Guo H, Li J, Dai T, et al. MambaIR: A Simple Baseline for Image Restoration with State-Space Model. In ECCV, 2024. [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/99851)
9.  Zhang K, Zuo W, Chen Y, et al. Beyond a Gaussian Denoiser: Residual Learning of Deep CNN for Image Denoising. IEEE TIP, 2017.
10. Krull A, Buchholz T O, Jug F. Noise2Void-learning denoising from single noisy images. In CVPR, 2019.
11. Abdelhamed A, Lin S, Brown M S. A high-quality denoising dataset for smartphone cameras. In CVPR, 2018.
12. Plötz T, Roth S. Benchmarking denoising algorithms with real photographs. In CVPR, 2017.