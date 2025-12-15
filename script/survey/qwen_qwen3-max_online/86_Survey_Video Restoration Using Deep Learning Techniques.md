# 基于深度学习的视频修复技术综述（2022–2025）

## 引言

视频修复（Video Restoration）旨在从存在退化（如模糊、噪声、低分辨率、遮挡等）的低质量视频中恢复高保真、时间一致的高质量视频序列。相较于图像修复，视频修复需额外建模帧间时间依赖关系，以避免闪烁、运动不连续等伪影。2022年以来，深度学习方法在该领域取得显著进展，从早期基于卷积神经网络（CNN）和循环结构的方法，逐步演化为以Transformer和扩散模型为主导的新范式。本文系统梳理2022–2025年间视频修复领域的代表性工作，重点关注模型架构创新、训练策略优化及对复杂退化（如真实世界退化、大尺度运动）的处理能力，并对未来研究趋势进行展望。

## 方法分类与代表作

### 基于Transformer的确定性视频修复

2022年，Liang等人提出的**VRT (Video Restoration Transformer)** \[1\]通过引入多尺度架构与时间互自注意力（Temporal Mutual Self-Attention, TMSA）机制，显式建模长距离时空依赖。其关键创新在于并行帧预测策略和多尺度特征融合，避免了传统滑动窗口方法对长视频的截断。在超分辨率、去模糊、去噪等5项任务上，VRT在14个基准数据集上均取得SOTA性能，尤其在处理长序列时优势显著（如在REDS上提升达2.16dB PSNR）。

**BasicVSR++** \[2\]（CVPR 2022）作为BasicVSR \[3\]的改进版本，通过增强传播与对齐模块，解决了早期循环网络因单向传播导致的误差累积问题。其采用双向传播并引入可变形对齐，在REDS数据集上将PSNR提升至32.39dB，成为后续许多工作的基础架构。

**RVRT (Recurrent Video Restoration Transformer)** \[4\]（NeurIPS 2022）结合了循环结构与Transformer的优势，通过引导式可变形注意力（Guided Deformable Attention）实现高效且精确的帧间对齐。该方法在保持较低计算复杂度的同时，在Vid4等真实场景数据集上显著优于纯Transformer或CNN方法，证明了混合架构的有效性。

### 基于扩散模型的生成式视频修复

随着扩散模型在图像生成领域的成功，其被迅速引入视频修复任务。**StableVSR** \[5\]（ECCV 2024）首次将潜变量扩散模型（LDM）应用于视频超分辨率，通过在潜在空间进行扩散过程，有效平衡了生成质量与计算效率。其在合成和真实数据集上均展现出优异的细节恢复能力和时间一致性，尤其在处理复杂纹理时优于确定性模型。

**SeedVR** \[6\]（2025）提出了一种用于通用视频修复的扩散Transformer，其核心是移位窗口注意力机制，支持处理任意长度和分辨率的视频。通过结合因果视频自动编码器和渐进式训练，SeedVR在AI生成视频的修复任务上表现出色，证明了扩散模型在处理未知野外交化方面的强大泛化能力。

**DiffuEraser** \[7\]（2025）专注于视频修复（Video Inpainting）任务，通过融入先验信息作为弱条件约束，有效抑制了扩散过程中的噪声伪影和幻觉现象。其扩展了模型的时序感受野，并利用视频扩散模型固有的时序平滑特性，在DAVIS等基准上显著提升了修复内容的结构完整性和时间连贯性。

### 面向特定任务的统一框架

针对视频人脸修复这一重要子任务，**SVFR** \[8\]（2025）提出了一个统一框架，将盲人脸恢复、补全和上色等任务集成到一个模型中。其通过任务嵌入、统一潜在正则化（ULR）和面部先验学习，使不同子任务相互促进。实验证明，该框架在VFHQ数据集上能同时提升多项指标，展示了多任务学习在特定领域修复中的潜力。

**VideoPainter** \[9\]（SIGGRAPH 2025）是首个双分支视频修复框架，明确将任务解耦为背景保留和前景生成。其通过轻量级上下文编码器和修复区域ID重采样技术，有效解决了长视频修复中的身份一致性问题，并构建了大规模数据集VPData，为未来研究提供了重要资源。

## 实验与评价总结

综合近年研究，实验评价呈现出以下共性结论：
1.  **性能-效率权衡**：基于Transformer的确定性模型（如VRT, RVRT）在PSNR/SSIM等指标上通常优于早期CNN方法，但计算成本较高。扩散模型（如SeedVR, StableVSR）在LPIPS等感知质量指标上表现更优，生成结果更逼真，但推理速度慢且需要大量计算资源。
2.  **真实世界退化的挑战**：在合成数据集（如REDS, Vimeo-90K）上，各方法性能差距逐渐缩小；但在真实世界数据集（如RealVSR, VideoLQ）上，性能显著下降，表明对复杂未知退化的建模仍是核心难点。
3.  **时间一致性是关键瓶颈**：几乎所有工作都将时间一致性作为核心评价维度。长视频序列（>100帧）的修复仍是巨大挑战，现有方法易出现身份漂移或运动不连贯问题，VideoPainter等新工作正试图解决此问题。
4.  **数据集与基准的演进**：研究趋势从单一任务（如超分辨率）向通用修复、多任务统一框架发展，评测也从单纯指标对比转向对时间一致性、身份保持、感知质量等多维度的综合评估。

## 趋势与挑战

基于2022–2025年的研究进展，未来视频修复领域将呈现以下趋势：
1.  **通用视频修复大模型**：借鉴图像领域的Stable Diffusion，构建能同时处理超分辨率、去模糊、去噪、修复等多种退化的通用视频修复基础模型（Foundation Model）将成为主流。SeedVR和VideoPainter已在此方向迈出关键一步。
2.  **效率与质量的协同优化**：针对扩散模型推理慢的问题，研究将聚焦于采样加速（如一致性模型、蒸馏）、模型压缩（如Mamba状态空间模型 \[10, 11\]）以及更高效的时空建模架构，以实现实时或近实时的高质量视频修复。
3.  **面向物理世界与因果推理**：当前模型多为数据驱动的黑盒，对物理退化过程（如光学模糊、传感器噪声）缺乏显式建模。未来工作将探索将物理先验和因果推理融入深度学习框架，以提升模型在极端退化和域外泛化场景下的鲁棒性。

## 结论

2022–2025年是视频修复技术快速演进的关键时期。从确定性Transformer到生成式扩散模型，研究范式发生了深刻转变。当前，该领域正从解决单一、合成退化问题，转向构建能处理复杂、真实世界退化的通用、高效、一致的修复系统。尽管在感知质量和通用性上取得了长足进步，但在计算效率、长序列建模和物理可解释性方面仍面临严峻挑战。未来的突破将依赖于新型网络架构、更优的训练范式以及对视频退化物理机制的深度融合。

## 参考文献

[1] Liang, J., Cao, J., Fan, Y., et al. (2024). VRT: A Video Restoration Transformer. *IEEE Transactions on Image Processing*, 33, 2171-2182. [aas.net.cn](https://aas.net.cn/cn/article/doi/10.16383/j.aas.c240235)

[2] Chan, K. C. K., Zhou, S., Xu, X., & Chen, C. (2022). BasicVSR++: Improving Video Super-Resolution with Enhanced Propagation and Alignment. *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*, 5962-5971.

[3] Chan, K. C. K., Wang, X., Yu, K., Dong, C., & Loy, C. C. (2021). BasicVSR: The Search for Essential Components in Video Super-Resolution and Beyond. *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*, 4945-4954.

[4] Liang, J., Fan, Y., Xiang, X., et al. (2022). Recurrent Video Restoration Transformer with Guided Deformable Attention. *Advances in Neural Information Processing Systems (NeurIPS)*, 35.

[5] Rota, C., Buzzelli, M., & van de Weijer, J. (2024). Enhancing Perceptual Quality in Video Super-Resolution through Temporally-Consistent Detail Synthesis Using Diffusion Models. *European Conference on Computer Vision (ECCV)*.

[6] Wang, J., Lin, Z., Wei, M., et al. (2025). SeedVR: Seeding Infinity in Diffusion Transformer Towards Generic Video Restoration. *arXiv preprint arXiv:2501.01235*. [baai.ac.cn](https://hub.baai.ac.cn/paper/0e87d0a7-4467-4119-87bd-0cebfe408c85)

[7] [DiffuEraser: 一种基于扩散模型的视频修复技术](https://blog.csdn.net/weixin_42380711/article/details/145371669). CSDN Blog, 2025.

[8] [SVFR: A Unified Framework for Generalized Video Face Restoration](https://www.themoonlight.io/zh/review/svfr-a-unified-framework-for-generalized-video-face-restoration). arXiv:2501.01235, 2025.

[9] Bian, Y., et al. (2025). VideoPainter: The First Dual-Branch Video Inpainting Framework for Plug-and-Play Background Control and Consistent Long Video Inpainting. *SIGGRAPH 2025*. [csdn.net](https://blog.csdn.net/AITIME_HY/article/details/147200218)

[10] Guo, H., Li, J., Dai, T., et al. (2024). MambaIR: A Simple Baseline for Image Restoration with State-Space Model. *European Conference on Computer Vision (ECCV)*.

[11] Guo, H., Guo, Y., Zha, Y., et al. (2024). MambaIRv2: Attentive State Space Restoration. *arXiv preprint arXiv:2411.15269*.

[12] Tang, Q., Zhao, Y., Liu, M., & Yao, C. (2025). A Review of Video Super-resolution Algorithms Based on Deep Learning. *Acta Automatica Sinica*, 51(7), 1480-1524. [aas.net.cn](https://aas.net.cn/cn/article/doi/10.16383/j.aas.c240235)