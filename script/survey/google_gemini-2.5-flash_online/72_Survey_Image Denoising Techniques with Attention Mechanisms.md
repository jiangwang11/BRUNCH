## 基于注意力机制的图像去噪技术综述（2022–2025）

### 引言

图像去噪是计算机视觉领域的核心任务之一，旨在从受损图像中恢复潜在的清晰图像，在医学影像、遥感图像处理、工业CT等领域具有广泛应用价值。近年来，随着深度学习技术的飞速发展，尤其是注意力机制的引入，显著提升了图像去噪模型的性能。注意力机制的核心在于使模型能够聚焦于图像中与去噪任务最相关的区域或特征，从而实现更精细的噪声抑制和细节恢复。本综述旨在回顾2022年至2025年间，基于注意力机制的图像去噪技术领域的代表性工作，总结其核心方法、关键结论及未来发展趋势。

### 方法分类与代表作

当前基于注意力机制的图像去噪方法可大致分为以下几类：

#### 1. 通道注意力机制去噪方法

通道注意力机制通过学习不同特征通道的重要性，自适应地调整通道权重，使模型能够关注那些对去噪贡献更大的特征。这种机制通常与卷积神经网络（CNN）结合使用，以兼顾局部特征提取和通道间相关性建模。

*   **《基于通道注意力机制的工业CT图像去噪网络》 (2025)** [cttacn.org.cn](https://cttacn.org.cn/article/doi/10.15953/j.ctta.2025.068)
    该研究针对工业CT图像中因噪声投影数据导致的重建图像信噪比降低问题，提出了一种基于深度学习的去噪方法。其核心在于将通道注意力机制模块嵌入解码器阶段，以自适应调整通道权重，从而在去噪过程中更好地保留图像结构细节。实验结果表明，该方法在显著去除噪声的同时有效保护了边缘细节，并在视觉效果和定量指标上均优于其他对比方法。

*   **《基于注意力机制的多级小波CNN遥感图像去噪算法》(2024)** [image.hanspub.org](https://image.hanspub.org/Html/9-1543124_84547.htm)
    该论文旨在解决遥感图像去噪中感受野大小与计算效率的权衡问题。作者提出了一种结合多级小波变换和通道注意力机制的CNN模型，通过小波变换在频域处理图像以保留边缘信息，同时利用通道注意力机制有针对性地提取噪声成分。实验在高斯噪声环境下，PSNR值平均提高了约10%，证实了其在保护遥感图像边缘特征方面的有效性。

*   **《A novel image denoising algorithm combining attention mechanism and residual UNet network》(2025)** [ablesci.com](https://www.ablesci.com/assist/detail?id=55KzDy)
    该工作提出了一种结合注意力机制和残差U-Net网络的新型图像去噪算法。通过在U-Net架构中引入注意力机制，模型能够更有效地捕捉和利用图像中的上下文信息进行去噪。该方法旨在提高去噪性能，同时保持图像的纹理细节。

#### 2. 自监督与多阶段注意力去噪方法

自监督学习在缺乏干净图像标签时，通过从含噪数据本身或中间结果中构建监督信号，结合注意力机制，实现了更鲁棒的去噪。多阶段训练则允许模型在不同阶段聚焦于图像的不同特征或噪声类型。

*   **《基于记忆单元的多阶段图像自监督去噪方法》(2025)** [opticsjournal.net](https://www.opticsjournal.net/Articles/OJ6f91743d6d014d4b/FullText)
    该研究解决了自监督图像去噪中缺乏清晰图像标签导致效果受限的问题，并提出了基于记忆单元（memory unit, MU）的多阶段自监督去噪算法。MU模块用于保存近似于清晰图像的中间去噪结果，协同监督网络训练，同时多阶段训练方案学习噪声图像平坦区域和纹理区域的特征，以平衡噪声去除和细节保留。实验结果在SIDD和DND数据集上取得了峰值信噪比和结构相似性指数的显著提升，优于现有自监督去噪方法。

*   **《基于Swin Transformer和卷积神经网络的低剂量纳米CT重建图像去噪》(2025)** [opticsjournal.net](https://www.opticsjournal.net/Articles/OJf6ace6d4916b8af8/FullText)
    本研究针对低剂量纳米CT重建图像的噪声问题，提出了一种融合Swin Transformer和CNN的去噪模型SwinCBD。该模型利用Swin Transformer的自注意力机制捕获长距离依赖，结合CNN的局部特征提取能力，并通过噪声估计子网络和U-Net主网络实现高质量图像重建。实验结果显示，SwinCBD在多项评价指标上显著提升了低剂量纳米CT图像的信噪比和采集效率，并表现出良好的泛化能力。

#### 3. Transformer 기반 图像去噪与恢复

Transformer架构凭借其强大的全局建模能力，在图像去噪和恢复任务中展现出潜力。结合注意力机制，Transformer能够有效处理图像中的长距离依赖，但在计算效率和局部特征捕获方面仍面临挑战。

*   **《MambaIR: A Simple Baseline for Image Restoration with State-Space Model》(2024)** [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/99851)
    该论文指出现有图像恢复骨干网络在全局感受野与计算效率之间面临困境，并提出了MambaIR，一种基于状态空间模型（State-Space Model, SSM）的图像恢复基线。MambaIR通过引入局部增强和通道注意力机制改进原始Mamba，以解决Mamba在低级视觉任务中的局部像素遗忘和通道冗余问题。实验证明，MambaIR在图像超分辨率任务中，在相似计算成本下，相比SwinIR取得了显著的改善，且具有全局感受野。

*   **《MambaIRv2: Attentive State Space Restoration》(2025)** [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/85148)
    该研究针对Mamba模型在图像恢复中因因果建模限制导致的像素利用不足问题，提出了MambaIRv2。MambaIRv2通过引入注意力状态空间方程，赋予Mamba非因果建模能力，实现超越扫描序列的关注。此外，该工作还引入了语义引导的邻域机制，以促进远距离但相似像素间的交互。实验结果表明，MambaIRv2在轻量级和经典超分辨率任务上均超越了现有SOTA方法。

*   **《注意力机制引导的混合失真图像复原研究》(2022)** [image.hanspub.org](https://image.hanspub.org/Html/2-1542465_49977.htm)
    该研究关注真实场景下多种混合失真组合的多任务图像复原问题。提出了一种由注意力机制引导的混合失真图像复原网络，包含任务驱动的操作层模块，利用注意力机制处理不同退化机制的不同表现。实验结果表明，该方法在复合失真图像复原上优于单任务复原模型，并针对单一退化类型也展现出优越性。

### 实验与评价总结

综述的代表性工作普遍采用公开数据集（如SIDD, DND, DIV2K, NWPU-RESISC45, CelebA-HQ, Places2）进行模型训练与测试，并使用峰值信噪比（PSNR）和结构相似性（SSIM）作为主要的量化评估指标。某些研究还引入了无参考图像质量评估指标（如NIQE、BRISQUE）及衬噪比（CNR）等。共同结论表明：

1.  **性能提升显著：** 引入注意力机制的深度学习方法在PSNR和SSIM等指标上，普遍优于传统去噪算法和不含注意力机制的深度学习基线模型。尤其在处理真实世界复杂噪声方面，其优势更为明显。
2.  **细节保留能力增强：** 注意力机制使得模型能够更精确地识别噪声区域和重要细节，有效去除噪声同时减少边缘模糊和纹理损失。
3.  **泛化能力：** 结合自监督学习和多阶段训练策略的方法，提高了模型在不同噪声类型和不同数据集上的泛化性能，尤其在缺乏干净标签数据时展现出实用价值。
4.  **计算效率优化：** Meskipun部分复杂模型（如基于Transformer）计算成本较高，但一些研究也致力于通过轻量化设计（如Swin Transformer、MambaIR的局部增强）在保证性能的同时优化算法效率。

### 趋势与挑战

未来基于注意力机制的图像去噪技术将呈现以下趋势与挑战：

1.  **多模态融合与跨域去噪：** 随着多模态数据（如红外、高光谱、医学CT图像）的日益丰富，将注意力机制与多模态信息融合，实现更全面的图像理解和去噪将是重要趋势 [image.hanspub.org](https://image.hanspub.org/Html/9-1543124_84547.htm)。挑战在于如何有效对齐和融合不同模态的注意力信息，以及解决跨域去噪的泛化性问题。
2.  **更高效、轻量级的注意力设计：** 现有注意力机制，特别是全局自注意力，计算成本仍然较高。未来研究将聚焦于开发更高效、轻量级的注意力模块 [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/99851)，例如稀疏注意力、局部-全局混合注意力、以及与Mamba等新型SSM模型的结合 [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/85148)，以适应边缘计算和实时去噪的需求。
3.  **自监督与无监督学习的深度探索：** 持续推进自监督和无监督去噪范式，减少对标注数据的依赖 [opticsjournal.net](https://www.opticsjournal.net/Articles/OJ6f91743d6d014d4b/FullText)。注意力机制在其中可以指导模型更好地从噪声输入中学习有用的统计信息。挑战在于如何设计更鲁棒的自监督信号和损失函数，避免模型崩溃或引入伪影。
4.  **可解释性和鲁棒性提升：** 随着模型复杂度的增加，提高去噪模型的可解释性成为重要挑战。研究将探索注意力机制如何揭示模型在去噪决策中的关注点，并增强模型在面对对抗性攻击或未知噪声类型时的鲁棒性。
5.  **与传统信号处理方法的结合：** 深度学习方法并非完全取代传统信号处理，将注意力机制与小波变换 [image.hanspub.org](https://image.hanspub.org/Html/9-1543124_84547.htm) 等传统方法结合，有望发挥各自优势，实现更优的去噪效果。

### 结论

综上所述，2022年至2025年间，基于注意力机制的图像去噪技术取得了显著进展。通道注意力、自监督多阶段训练以及与Transformer/SSM架构的结合，有效地提升了去噪性能、细节保留能力和泛化性。未来的研究将聚焦于多模态融合、更高效的注意力设计、自监督学习的深度探索、可解释性与鲁棒性提升，以及与传统方法的有机结合，以应对复杂多变的实际应用场景中的挑战。

### 参考文献

*   余维, 王成祥, 何雨. 基于通道注意力机制的工业CT图像去噪网络. [cttacn.org.cn](https://cttacn.org.cn/article/doi/10.15953/j.ctta.2025.068) (2025).
*   王硕, 张晓东, 祝令函, 高绍姝, 王鑫瑞. 基于记忆单元的多阶段图像自监督去噪方法. [opticsjournal.net](https://www.opticsjournal.net/Articles/OJ6f91743d6d014d4b/FullText) (2025).
*   贾小宁, 成丽波, 苑浩然, 李喆. 基于注意力机制的多级小波CNN遥感图像去噪算法. [image.hanspub.org](https://image.hanspub.org/Html/9-1543124_84547.htm) (2024).
*   龚敏学, 朱烨, 符颖. 注意力机制引导的混合失真图像复原研究. [image.hanspub.org](https://image.hanspub.org/Html/2-1542465_49977.htm) (2022).
*   邓彪, 汪澳, 彭真, 汪俊, 陶芬, 张玲, 杜国浩, 刘一. 基于Swin Transformer和卷积神经网络的低剂量纳米CT重建图像去噪. [opticsjournal.net](https://www.opticsjournal.net/Articles/OJf6ace6d4916b8af8/FullText) (2025).
*   Hang Guo, Jinmin Li, Tao Dai, Zhihao Ouyang, Xudong Ren, Shu-Tao Xia. MambaIR: A Simple Baseline for Image Restoration with State-Space Model. [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/99851) (2024).
*   Hang Guo, Yong Guo, Yaohua Zha, Yulun Zhang, Wenbo Li, Tao Dai, Shu-Tao Xia, Yawei Li. MambaIRv2: Attentive State Space Restoration. [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/85148) (2025).
*   Ding, S., Wang, Q., Guo, L., Zhang, J., & Liu, D. (2023). A novel image denoising algorithm combining attention mechanism and residual UNet network. Knowledge and Information Systems. [ablesci.com](https://www.ablesci.com/assist/detail?id=55KzDy) (2025).
*   曹承瑞, 刘微容, 史长宏, 张浩琛. 多级注意力传播驱动的生成式图像修复方法. 自动化学报, 2022, 48(5): 1343−1352. [aas.net.cn](https://aas.net.cn/cn/article/doi/10.16383/j.aas.c200485?viewType=HTML) (2022).
*   Zamir, S. W., Arora, A., & Khan, S., et al. (2022). Restormer: Efficient Transformer for High-Resolution Image Restoration. 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR).
*   Liu, Z., Lin, Y. T., Cao, Y., et al. (2021). Swin Transformer: Hierarchical Vision Transformer using Shifted Windows. 2021 IEEE/CVF International Conference on Computer Vision (ICCV).
*   Wang, Z., Cun, X., Bao, J., et al. (2022). Uformer: A General U-Shaped Transformer for Image Restoration. 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR).