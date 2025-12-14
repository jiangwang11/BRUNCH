## 基于深度学习的视频修复技术研究进展 (2022-2025)

### 引言

视频修复（Video Restoration）旨在通过利用低质量视频的帧内和帧间信息，重建具有更高视觉质量和内容一致性的视频，在提升用户体验和下游任务性能方面具有重要意义 [aas.net.cn](https://aas.net.cn/cn/article/doi/10.16383/j.aas.c240235?viewType=HTML)。近年来，深度学习技术在图像和视频处理领域取得了显著突破，尤其是在视频超分辨率（Video Super-Resolution, VSR）、视频去模糊、视频去噪和视频插帧等任务中展现出强大潜力 [aas.net.cn](https://aas.net.cn/cn/article/doi/10.16383/j.aas.c240235?viewType=HTML)，极大地推动了视频修复领域的发展 [aas.net.cn](https://aas.net.cn/cn/article/doi/10.16383/j.aas.c240235?viewType=HTML)。本综述将聚焦 2022-2025 年间，深度学习在视频修复领域的核心方法、代表性工作、实验评估以及未来发展趋势，为相关研究提供参考。

### 方法分类与代表作

2022-2025年间，基于深度学习的视频修复算法主要集中在以下几个方面：Transformer架构的应用与优化、循环网络与长时序依赖建模、扩散模型引入以及实时与高效修复。

#### 1. Transformer架构的应用与优化

Transformer凭借其卓越的全局感知能力，在视频修复领域得到了广泛应用，尤其在捕获长距离帧间依赖方面表现突出。

*   **VRT (Video Restoration Transformer)** [blog.csdn.net](https://blog.csdn.net/weixin_62765017/article/details/140748639): 该模型旨在解决视频超分辨率、视频去模糊和视频去噪等多个视频修复任务。VRT采用多尺度设计，通过相互注意力机制实现帧间对齐和特征融合，有效捕捉长时序依赖。在多个视频修复基准测试中，VRT展现了领先的性能，例如在某些数据集上性能提升高达2.16dB [blog.csdn.net](https://blog.csdn.net/weixin_62765017/article/details/140748639)。
*   **Restormer: Efficient Transformer for High-Resolution Image Restoration** [cloud.tencent.cn](https://cloud.tencent.cn/developer/article/2398294?policyId=1003): 该工作提出了一种高效的Transformer模型，用以处理高分辨率图像恢复任务，克服了传统Transformer计算复杂度高的问题。Restormer引入了多Dconv头转置注意力（MDTA）块和门控Dconv前馈网络（GDFN），通过跨通道而非空间维度应用自注意力，并结合深度卷积捕获局部上下文，实现了线性复杂度的全局互联。在包括去噪、去模糊等多个图像恢复任务上取得了领先性能 [cloud.tencent.cn](https://cloud.tencent.cn/developer/article/2398294?policyId=1003)。
*   **MambaIRv2: Attentive State Space Restoration** [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/85148): 针对Mamba模型在图像恢复中存在的因果建模限制，MambaIRv2引入注意力状态空间方程，使其能够超越扫描序列进行非因果建模。通过语义引导的邻域机制，有效促进了远距离相似像素间的交互。实验结果表明，MambaIRv2在轻量级超分辨率和经典超分辨率任务上均超越了现有Transformer模型，例如在轻量级SR上实现了0.35dB的PSNR提升，同时参数量减少9.3% [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/85148)。

#### 2. 循环网络与长时序依赖建模

循环网络（如RNN）在处理视频序列时能够有效利用帧间信息，但常受限于长时序依赖和并行计算的挑战。

*   **BasicVSR++: Improving Video Super-Resolution with Enhanced Propagation and Alignment** [aas.net.cn](https://aas.net.cn/cn/article/doi/10.16383/j.aas.c240235?viewType=HTML): 该工作深入研究了视频超分辨率中信息传播和对齐的关键组件。BasicVSR++通过引入第二次迭代对齐、光流引导的可变形注意力以及特征传播中的周期性置换等技术，显著增强了对视频的长时间依赖建模和运动补偿能力。模型在多个基准数据集上持续保持领先的性能，例如在REDS数据集上PSNR达到32.39dB [aas.net.cn](https://aas.net.cn/cn/article/doi/10.16383/j.aas.c240235?viewType=HTML)。
*   **RVRT: Recurrent Video Restoration Transformer with Guided Deformable Attention** [aas.net.cn](https://aas.net.cn/cn/article/doi/10.16383/j.aas.c240235?viewType=HTML): RVRT 旨在结合循环架构的参数效率和Transformer的全局感知能力，以实现更优的视频恢复。该模型在全局循环框架内并行处理局部相邻帧，并融合了引导可变形注意力机制，有效平衡了模型大小、计算效率与长距离依赖建模。RVRT在REDS和Vimeo-90K等数据集上的PSNR表现优于许多现有的循环网络和Transformer模型 [aas.net.cn](https://aas.net.cn/cn/article/doi/10.16383/j.aas.c240235?viewType=HTML)。
*   **MambaIR: A Simple Baseline for Image Restoration with State-Space Model** [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/99851): 针对现有恢复骨干网络在全局感受野和计算效率之间的困境，MambaIR提出了一个简单有效的基线模型，引入了局部增强和通道注意力机制以改进原始Mamba。该模型利用了局部像素相似性并减少了通道冗余，在图像超分辨率任务中，其性能比SwinIR高出0.45dB，同时保持相似的计算成本 [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/99851)。

#### 3. 扩散模型的引入

扩散模型因其在生成高质量图像方面的出色能力，开始被引入视频修复领域，尤其在生成逼真细节和处理退化方面展现潜力。

*   **Upscale-A-Video: Temporal-Consistent Diffusion Model for Real-World Video Super-Resolution** [aas.net.cn](https://aas.net.cn/cn/article/doi/10.16383/j.aas.c240235?viewType=HTML): 该工作利用扩散模型生成高质量、时间一致的真实世界视频超分辨率结果。Upscale-A-Video模型专注于解决真实世界视频的复杂退化问题，并通过扩散过程引入时间一致性约束，确保生成视频的流畅性。它在真实世界VSR数据集上取得了具有竞争力的感知质量和时间一致性 [aas.net.cn](https://aas.net.cn/cn/article/doi/10.16383/j.aas.c240235?viewType=HTML)。
*   **EvTexture: Event-driven Texture Enhancement for Video Super-resolution** [aas.net.cn](https://aas.net.cn/cn/article/doi/10.16383/j.aas.c240235?viewType=HTML): EvTexture是一个事件驱动的纹理增强模型，专注于利用事件信息提升视频超分辨率的纹理细节。该模型结合了事件相机的优势，能够处理传统帧图像在高运动场景下的模糊问题，并通过一种新颖的纹理增强模块重建精细的纹理。在多个数据集上，EvTexture在PSNR/SSIM指标上达到领先水平，尤其是在复杂纹理恢复方面 [aas.net.cn](https://aas.net.cn/cn/article/doi/10.16383/j.aas.c240235?viewType=HTML)。
*   **基于预训练扩散模型的两阶段高分辨率图像复原方法 (C2F)** [www.arocmag.cn](https://www.arocmag.cn/language?lang=cn&returnUrl=%2Fabs%2F2024.10.0438): 针对高分辨率图像恢复中扩散模型效率低下和分布外（OOD）问题，C2F方法提出一个两阶段的复原机制。首先在固定尺寸的粗阶段进行初步复原，然后以粗阶段结果为起点，在原尺寸的细阶段使用更短的扩散过程，大大提升复原速度并避免OOD问题。在1024尺寸图像复原任务中，C2F采样次数仅为同类方法的22%，速度提升4.5倍，同时在PSNR和FID指标上达到了最高水平 [www.arocmag.cn](https://www.arocmag.cn/language?lang=cn&returnUrl=%2Fabs%2F2024.10.0438)。

#### 4. 高效与实时修复

随着视频应用场景的扩大，对视频修复算法的实时性和计算效率提出了更高要求。

*   **CFD-BasicVSR++: Collaborative Feedback Discriminative Propagation for Video Super-Resolution** [aas.net.cn](https://aas.net.cn/cn/article/doi/10.16383/j.aas.c240235?viewType=HTML): 该方法旨在通过协同反馈判别传播提升视频超分辨率的效率和性能。CFD-BasicVSR++结合了反馈机制和判别性传播策略，优化了特征的融合和传播过程，从而在保证重建质量的同时，提高了推理速度和计算效率。在REDS和Vimeo-90K数据集上表现出优于BasicVSR++的PSNR和SSIM [aas.net.cn](https://aas.net.cn/cn/article/doi/10.16383/j.aas.c240235?viewType=HTML)。
*   **MIA-VSR: Video Super-Resolution Transformer with Masked Inter&Intra-Frame Attention** [aas.net.cn](https://aas.net.cn/cn/article/doi/10.16383/j.aas.c240235?viewType=HTML): MIA-VSR引入了掩蔽帧间和帧内注意力机制，以提高视频超分辨率的效率和性能。该模型通过选择性地关注重要的时空信息，减少冗余计算，在保持高重建质量的同时降低了计算负担。在REDS数据集上，MIA-VSR在PSNR和SSIM性能上取得了优异成果 [aas.net.cn](https://aas.net.cn/cn/article/doi/10.16383/j.aas.c240235?viewType=HTML)。
*   **VFIMamba: Video Frame Interpolation with State Space Models** [aas.net.cn](https://aas.net.cn/cn/article/doi/10.16383/j.aas.c240572?viewType=HTML): VFIMamba探索了状态空间模型（SSM）在视频插帧中的应用，以实现高效的帧间生成。该方法利用SSM的长序列建模能力，有效捕捉视频帧间的复杂动态，同时避免了传统Transformer的二次计算复杂度。VFIMamba在Vimeo-90K和X-TEST等数据集上取得了领先的PSNR和SSIM结果 [aas.net.cn](https://aas.net.cn/cn/article/doi/10.16383/j.aas.c240572?viewType=HTML)。

### 实验与评价总结

2022-2025年间的视频修复研究在公共数据集上取得了显著进展。常用的数据集包括REDS、Vimeo-90K、Vid4、UCF101、X-TEST和SNU-FILM等，这些数据集涵盖了合成退化和真实世界退化情景，为算法的训练和评估提供了多样化的测试环境 [aas.net.cn](https://aas.net.cn/cn/article/doi/10.16383/j.aas.c240235?viewType=HTML), [aas.net.cn](https://aas.net.cn/cn/article/doi/10.16383/j.aas.c240572?viewType=HTML)。

评价指标方面，峰值信噪比（PSNR）和结构相似度（SSIM）仍然是衡量重建质量的主流指标，反映了像素级保真度 [aas.net.cn](https://aas.net.cn/cn/article/doi/10.16383/j.aas.c240235?viewType=HTML), [aas.net.cn](https://aas.net.cn/cn/article/doi/10.16383/j.aas.c240572?viewType=HTML)。然而，为了更好地反映人眼感知质量，低感知图像补丁相似度（LPIPS）等感知指标也越来越受到重视，尤其是在涉及生成模型和真实世界视频修复任务中 [aas.net.cn](https://aas.net.cn/cn/article/doi/10.16383/j.aas.c240235?viewType=HTML), [aas.net.cn](https://aas.net.cn/cn/article/doi/10.16383/j.aas.c240572?viewType=HTML)。

总体而言，当前方法在双三次插值下采样和高斯模糊下采样等合成退化场景下，PSNR和SSIM指标持续提升，表明深度学习模型在恢复结构细节和减少伪影方面取得了显著效果 [aas.net.cn](https://aas.net.cn/cn/article/doi/10.16383/j.aas.c240235?viewType=HTML)。在真实世界视频修复任务中（如RealVSR数据集），模型在PSNR/SSIM指标上仍有提升空间，但LPIPS等感知指标的改善表明模型生成的视频更符合人类视觉偏好 [aas.net.cn](https://aas.net.cn/cn/article/doi/10.16383/j.aas.c240235?viewType=HTML)。在推理时间方面，通过采用门控机制、稀疏注意力、深度可分离卷积或状态空间模型等设计，研究者们在保证性能的同时，有效降低了模型的参数量和计算复杂度，提升了算法的实时性 [aas.net.cn](https://aas.net.cn/cn/article/doi/10.16383/j.aas.c240235?viewType=HTML)。例如，C2F方法通过两阶段扩散显着加速了高分辨率图像恢复 [www.arocmag.cn](https://www.arocmag.cn/language?lang=cn&returnUrl=%2Fabs%2F2024.10.0438)。

### 趋势与挑战

2025年前后，视频修复领域的研究趋势主要体现在以下几个方面：

1.  **多模态融合与跨任务统一：** 视频修复将不再局限于单一退化类型，而是趋向于融合多种传感器数据（如事件相机数据 [aas.net.cn](https://aas.net.cn/cn/article/doi/10.16383/j.aas.c240235?viewType=HTML)）或利用多模态信息（如文本、音频线索）进行更全面的视频增强。未来模型可能发展为能够处理多种视频退化（如超分辨率、去模糊、去噪、插帧等）的通用框架，实现知识在不同任务间的迁移和共享 [www.cjig.cn](https://www.cjig.cn/zh/article/doi/10.11834/jig.240436/)。
2.  **生成式模型（尤其是扩散模型）的深度融合与时间一致性挑战：** 随着扩散模型在图像生成领域取得的巨大成功，其在视频修复中的应用将更加深入。未来的研究将致力于解决扩散模型在视频生成中面临的时间不一致性问题，通过引入更精细的时间依赖建模、帧间一致性损失或结构化时间提示等机制，生成高度逼真且时间连贯的视频内容 [aas.net.cn](https://aas.net.cn/cn/article/doi/10.16383/j.aas.c240235?viewType=HTML)。
3.  **计算效率与真实世界部署：** 随着高分辨率和高帧率视频的普及，视频修复算法对计算资源的需求将持续增加。未来的研究将更加关注模型的推理速度和部署效率，包括轻量化模型设计、硬件感知优化、边缘计算部署等。稀疏注意力机制、状态空间模型、或两阶段粗-细粒度处理等方法将进一步发展，以在保证性能的同时，实现消费级硬件上的实时视频修复。

### 结论

2022-2025年间，深度学习在视频修复领域取得了长足进步，特别是在Transformer架构的精细化、循环网络的长时序建模、扩散模型的初步探索以及实时高效算法设计方面。虽然在合成数据上重建质量已达到较高水平，但真实世界复杂退化场景下的鲁棒性、感知质量、时间一致性以及计算效率仍是未来需要重点关注的挑战。

### 参考文献

*   [aas.net.cn](https://aas.net.cn/cn/article/doi/10.16383/j.aas.c240235?viewType=HTML) 唐麒, 赵耀, 刘美琴, 姚超. 基于深度学习的视频超分辨率重建算法进展. 自动化学报, 2025, 51(7): 1480−1524.
*   [blog.csdn.net](https://blog.csdn.net/weixin_62765017/article/details/140748639) Liang, J., Cao, J., Fan, Y., Zhang, K., Ranjan, R., Li, Y., ... & Van Gool, L. (2022). VRT: A Video Restoration Transformer. In IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR). (引用自 CSDN 博客对论文的介绍)
*   [cloud.tencent.cn](https://cloud.tencent.cn/developer/article/2398294?policyId=1003) Zamir, S. W., Arora, A., Khan, S., & Van Gool, L. (2022). Restormer: Efficient Transformer for High-Resolution Image Restoration. In IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR). (引用自腾讯云开发者社区对论文的介绍)
*   [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/85148) Guo, H., Guo, Y., Zha, Y., Zhang, Y., Li, W., Dai, T., ... & Li, Y. (2025). MambaIRv2: Attentive State Space Restoration. arXiv preprint arXiv:2411.15269.
*   [aas.net.cn](https://aas.net.cn/cn/article/doi/10.16383/j.aas.c240572?viewType=HTML) 吴晨阳, 张勇, 韩树豪, 郭春乐, 李重仪, 程明明. 基于深度学习的视频插帧研究进展. 自动化学报, 2025, 51(8): 1760−1776.
*   [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/99851) Guo, H., Li, J., Dai, T., Ouyang, Z., Ren, X., & Xia, S. (2024). MambaIR: A Simple Baseline for Image Restoration with State-Space Model. In European Conference on Computer Vision (ECCV).
*   [www.arocmag.cn](https://www.arocmag.cn/language?lang=cn&returnUrl=%2Fabs%2F2024.10.0438) 谢源远, 周非, 周志远, 张宇曈. 基于预训练扩散模型的两阶段高分辨率图像复原方法. 计算机应用研究, 2025年第42卷 第8期: 2545-2551.
*   [www.cjig.cn](https://www.cjig.cn/zh/article/doi/10.11834/jig.240436/) 韦炎炎, 毛天一, 李柏昂, 王飞, 李锋, 张召, 赵洋. 视觉模型及多模态大模型推进图像复原增强研究进展. 中国图象图形学报, 2025, 30(5):1197-1219.