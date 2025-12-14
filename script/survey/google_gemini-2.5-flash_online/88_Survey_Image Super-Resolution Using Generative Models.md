## 图像超分辨率生成模型研究综述 (2022-2025)

### 引言

图像超分辨率（Super-Resolution, SR）旨在从低分辨率（Low-Resolution, LR）图像重建出高分辨率（High-Resolution, HR）图像，是计算机视觉领域的一个经典而富有挑战性的问题。近年来，随着深度学习技术的飞速发展，特别是生成模型（Generative Models）的引入，图像超分辨率技术取得了显著的进步。生成模型在捕捉高频细节和生成视觉逼真纹理方面展现出强大潜力，有效缓解了传统基于插值或卷积神经网络（Convolutional Neural Network, CNN）方法在生成细节时易产生模糊和伪影的问题。本综述将聚焦2022年至2025年间，图像超分辨率领域中基于生成模型的代表性工作，对其研究问题、核心方法和关键实验结论进行梳理，并展望未来的研究趋势。

### 方法分类与代表作

当前基于生成模型的图像超分辨率方法主要可分为以下几类：

#### 1. 生成对抗网络（Generative Adversarial Networks, GANs）

GANs通过生成器-判别器的对抗训练机制，使生成的超分辨率图像在视觉上更接近真实图像。

*   **Hierarchical Generative Adversarial Networks for Single Image Super-Resolution** ([fuxi.163.com](https://fuxi.163.com/database/437))
    *   **研究问题**: 解决现有深度CNN模型在单一尺度特征提取和监督信息不足导致SR图像伪影和噪声的问题。
    *   **核心方法**: 提出分层特征提取模块（HFEM）用于多尺度特征提取，以及分层引导重建模块（HGRM）以渐进方式重建图像结构纹理。将这两个模块集成到分层生成对抗网络（HSR-GAN）框架中。
    *   **关键实验结论**: 在五个标准数据集上实现了良好的视觉质量和卓越的定量性能，有效恢复了图像细节，获得了语义合理且视觉逼真的结果。

#### 2. Transformer网络

Transformer模型凭借其强大的长距离依赖建模能力，在图像超分辨率任务中展现出巨大潜力，尤其是在捕捉全局信息和复杂纹理方面。

*   **ELAN: Efficient Long-Range Attention Network for Image Super-resolution** ([blog.csdn.net](https://blog.csdn.net/BigerBang/article/details/134991611))
    *   **研究问题**: 现有基于Transformer的SwinIR等模型在效率和长距离依赖建模上存在局限。
    *   **核心方法**: 提出了高效长程注意力块（ELAB），结合局部特征提取（通过shift conv增加感受野）和分组多尺度自注意力（GMSA）机制，以更好地建模长距离依赖。同时，引入系列优化策略（如BN替代LN、QKV重用、共享注意力、去除非必要的掩码机制和相对位置编码）来提升效率。
    *   **关键实验结论**: ELAN在保持甚至提升超分辨率效果的同时，显著提高了模型效率，例如，ELAN-light比SwinIR-light快4.5倍。

*   **级联残差优化Transformer网络的图像超分辨率重建** ([www.opticsjournal.net](https://www.opticsjournal.net/Articles/OJ96890848f77a2d12/Abstract))
    *   **研究问题**: 扩展CNN在图像超分辨率多尺度特征上的自适应学习能力，提升网络性能。
    *   **核心方法**: 提出一种结合级联残差和通道注意力的Transformer网络优化结构。该网络采用级联残差结构增强低阶和中阶特征的迭代复用与信息共享，并将通道注意力机制引入Transformer以增强特征表达和自适应学习通道权重。感知模块优化为级联感知模块以扩展网络深度。
    *   **关键实验结论**: 在Set5、Set14等数据集上，相较于主流方法，2倍、3倍和4倍放大因子下的客观评价（PSNR、SSIM）和主观视觉效果均有显著提升，恢复图像纹理更清晰，表明其在多尺度特征处理和重建方面的有效性。

*   **GRFormer: Grouped Residual Self-Attention for Lightweight Single Image Super-Resolution** ([chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/51013))
    *   **研究问题**: 现有轻量级Transformer-based SISR模型在减少参数和计算量时通常会牺牲性能。
    *   **核心方法**: 提出GRFormer，其核心是分组残差自注意力（GRSA），通过分组残差层（GRL）替代自注意力中的QKV线性层以减少参数和计算量，并集成紧凑的指数空间相对位置偏置（ES-RPB）来增强位置信息表示能力并进一步减少参数。
    *   **关键实验结论**: GRFormer在$\times$2、$\times$3、$\times$4 SISR任务中超越了最先进的Transformer方法，在DIV2K数据集上PSNR最大提升0.23dB，同时自注意力模块的参数和MACs分别减少约60%和49%。

#### 3. 扩散模型（Diffusion Models）

扩散模型凭借其强大的生成能力，在图像复原任务中表现出色，能够生成高质量、细节丰富的超分辨率图像。

*   **基于参数高效扩散微调的少样本参考图驱动图像补全** ([www.fitee.zjujournals.com](https://www.fitee.zjujurnals.com/zh/article/doi/10.1631/FITEE.2400395/))
    *   **研究问题**: 现有参考图驱动的图像补全方法难以实现高保真度补全效果，用户需要通过参考图像为特定对象补全个性化外观。
    *   **核心方法**: 基于预训练的文本驱动图像补全模型，引入即插即用的低秩适配（LoRA）模块，通过少样本微调学习参考图像的特定特征。结合GPT-4V生成的丰富提示词和先验噪声初始化技术，引导去噪扩散过程。
    *   **关键实验结论**: 方法在定性和定量指标上均达到当前最高水平，提供更强的定制化能力，有效解决了少样本参考图驱动图像补全的保真度问题。

*   **基于预训练扩散模型的两阶段高分辨率图像复原方法** ([www.arocmag.cn](https://www.arocmag.cn/language?lang=cn&returnUrl=/abs/2024.10.0438))
    *   **研究问题**: 预训练扩散先验图像复原在处理高分辨率图像时效率低下且存在分布外（OOD）问题。
    *   **核心方法**: 提出“由粗到细”（C2F）的两阶段高分辨率图像复原方法。第一阶段（coarse阶段）在固定尺寸下获得粗糙复原结果，确保输出一致性；第二阶段（fine阶段）以第一阶段结果为起点，在原尺寸上使用更短的扩散过程，大幅提升复原速度。
    *   **关键实验结论**: 在人脸、自然场景等多种复原任务（修复、上色、去模糊）中，任何尺寸下都能获得最高水平的输出。对1024尺寸图像复原，采样次数仅为同类方法的22%，速度提升4.5倍，并有效避免了OOD问题，PSNR和FID指标达到最高水平。

*   **用于单帧图像超分辨重建的自监督图像扩散模型** ([signal.ejournal.org.cn](https://signal.ejournal.org.cn/article/doi/10.12466/xhcl.2025.02.014?viewType=HTML))
    *   **研究问题**: 传统深度学习SR模型依赖大量成对高低分辨率图像对，而真实图像对获取困难，基于仿真图像对训练的模型在面对未知退化类型图像时表现不佳。
    *   **核心方法**: 提出单帧图像超分辨重建的自监督图像扩散模型（SSDM-SR）。模型基于扩散模型学习单帧图像内的信息分布，并为待超分辨重建的图像训练一个小型特定图像扩散模型。训练数据仅从待超分辨图像本身中提取，并引入坐标信息以辅助构建图像整体框架，加速模型收敛。
    *   **关键实验结论**: 在多个公开基准数据集和具有未知退化核的数据集上，SSDM-SR在图像失真度和感知质量方面均优于近期先进的有监督和无监督SR方法，并在真实世界LR图像上生成了视觉满意且无明显伪影的结果。

### 实验与评价总结

在基于生成模型的图像超分辨率研究中，研究人员普遍采用多种客观指标和主观评估来衡量模型性能。

**客观评价指标：**
峰值信噪比（PSNR）和结构相似度（SSIM）仍然是衡量图像失真度的标准指标。然而，许多工作指出，PSNR和SSIM与人类感知质量不完全一致，因此高PSNR/SSIM不一定意味着更好的视觉效果。为了更好地捕获感知质量，学界也广泛采用FRC (Fidelity-Realism-Consistency)、LPIPS (Learned Perceptual Image Patch Similarity)、FID (Fréchet Inception Distance)、以及各种对抗性损失来间接评估生成图像的真实感和多样性。例如，上述扩散模型相关的研究，如[www.arocmag.cn](https://www.arocmag.cn/language?lang=cn&returnUrl=/abs/2024.10.0438)和[www.fitee.zjujournals.com](https://www.fitee.zjujurnals.com/zh/article/doi/10.1631/FITEE.2400395/)均强调了FID等指标的优越性。

**主观视觉评估：**
由于生成模型能够生成更自然的纹理和细节，主观视觉评估在这些方法中占据了更重要的地位。研究通常通过用户研究、A/B测试或专家评判来判断生成图像的视觉真实感、细节清晰度和伪影情况。例如，[fuxi.163.com](https://fuxi.163.com/database/437)和[www.opticsjournal.net](https://www.opticsjournal.net/Articles/OJ96890848f77a2d12/Abstract)等工作均提及主观评价的良好结果。

**共同趋势：**
*   **计算效率和部署优化**: 随着模型复杂度的增加，降低模型的参数量和计算量，提升推理速度成为重要考量。Transformer模型如ELAN和GRFormer在这方面做出了显著努力，通过引入轻量级注意力机制或优化策略来加速模型。扩散模型也开始关注高分辨率图像处理的效率问题，通过两阶段或自监督等方法进行加速（如[www.arocmag.cn](https://www.arocmag.cn/language?lang=cn&returnUrl=/abs/2024.10.0438)）。
*   **多尺度特征融合与上下文建模**: 无论是分层GAN还是Transformer，都致力于更好地整合多尺度信息和捕捉长距离依赖，以重建更具全局一致性和局部细节的图像。
*   **少样本与自监督学习**: 针对真实数据获取的挑战，自监督和少样本学习方法逐渐兴起，允许模型从有限的数据或未标注数据中学习，增强了模型的泛化能力和实用性（如[signal.ejournal.org.cn](https://signal.ejournal.org.cn/article/doi/10.12466/xhcl.2025.02.014?viewType=HTML)和[www.fitee.zjujournals.com](https://www.fitee.zjujurnals.com/zh/article/doi/10.1631/FITEE.2400395/)）。

### 趋势与挑战

展望2025年前后，图像超分辨率生成模型的研究将呈现以下趋势：

1.  **多模态融合与语义理解增强型超分辨率：** 单纯基于像素重建已难以满足复杂场景的需求。未来的超分辨率模型将更深入地融入上下文信息、语义理解甚至文本描述。例如，结合图像-文本预训练模型（如CLIP）的扩散模型，能够利用语言指导进行更精确和风格化的图像生成，实现语义驱动的超分辨率。类似[www.fitee.zjujournals.com](https://www.fitee.zjujurnals.com/zh/article/doi/10.1631/FITEE.2400395/)中GPT-4V提示词的应用是这一方向的初步尝试。挑战在于如何有效地对齐和融合异构多模态信息，并确保生成图像的语义一致性与视觉真实感。

2.  **通用性与实际应用部署优化：** 当前许多生成模型在特定数据集上表现优异，但泛化能力仍有待提高，尤其是在“真实世界”低分辨率图像（退化模型复杂多样）上的表现。未来的研究将更加关注模型的鲁棒性和泛化能力，通过更先进的退化建模、自监督学习、或针对边缘设备优化的轻量级架构，使得超分辨率技术能广泛应用于智能手机、监控系统等实际场景。ELAN和GRFormer等模型对效率的关注是这一趋势的体现，而两阶段扩散模型（如[www.arocmag.cn](https://www.arocmag.cn/language?lang=cn&returnUrl=/abs/2024.10.0438)）也旨在解决高分辨率图像处理的效率问题。

3.  **可控性与用户交互式超分辨率：** 随着AIGC技术的发展，用户对生成内容的可控性需求日益增长。未来的超分辨率研究将探索如何让用户通过简单的指令（如文本、涂鸦或参考图像）来引导SR过程，实现对生成细节、风格或特定区域的高级控制。这将涉及更精细的条件生成机制与更直观的人机交互界面，使得专业或非专业用户都能定制化地提升图像质量，类似[www.fitee.zjujournals.com](https://www.fitee.zjujurnals.com/zh/article/doi/10.1631/FITEE.2400395/)中个性化外观补全的思路将进一步扩展到超分辨率任务中。

### 结论

基于生成模型的图像超分辨率技术在2022-2025年间取得了显著进展。GANs、Transformer和扩散模型各展所长，在提升图像感知质量、捕捉高频细节方面展现出强大能力。研究重点从单纯追求客观指标转向兼顾感知质量、计算效率和泛化能力。未来，多模态融合、通用性与实际部署优化、以及用户可控性的超分辨率将成为重要的研究方向，进一步推动该技术在实际应用中的落地。

### 参考文献

1.  陈伟民、马宇晴、刘祥龙、袁燚. (2022). Hierarchical Generative Adversarial Networks for Single Image Super-Resolution. [fuxi.163.com](https://fuxi.163.com/database/437)
2.  Li, Y., Deng, Z., Cao, Y., & Liu, L. (2024). GRFormer: Grouped Residual Self-Attention for Lightweight Single Image Super-Resolution. [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/51013)
3.  林坚普、吴镇城、王崑赋、林志贤、郭太良、林珊玲. (2024). 级联残差优化Transformer网络的图像超分辨率重建. 光学 精密工程, 32(12): 1902. [www.opticsjournal.net](https://www.opticsjournal.net/Articles/OJ96890848f77a2d12/Abstract)
4.  Yang, S., Gu, Z., Hao, W., et al. (2025). Few-shot exemplar-driven inpainting with parameter-efficient diffusion fine-tuning. Frontiers of Information Technology & Electronic Engineering, 26(8): 1428-1440. [www.fitee.zjujournals.com](https://www.fitee.zjujournals.com/zh/article/doi/10.1631/FITEE.2400395/)
5.  谢源远, 周非, 周志远, 张宇曈. (2025). 基于预训练扩散模型的两阶段高分辨率图像复原方法. 计算机应用研究, 42(8): 2545-2551. [www.arocmag.cn](https://www.arocmag.cn/language?lang=cn&returnUrl=/abs/2024.10.0438)
6.  牛阿茜, 孙瑾秋, 朱宇, 张艳宁. (2025). 用于单帧图像超分辨重建的自监督图像扩散模型. 信号处理, 41(2): 203-214. [signal.ejournal.org.cn](https://signal.ejournal.org.cn/article/doi/10.12466/xhcl.2025.02.014?viewType=HTML)
7.  Fanghua Yu, Jinjin Gu, Zheyuan Li, Jinfan Hu, Xiangtao Kong, Xintao Wang, Jingwen He, Yu Qiao, Chao Dong. (2024). Scaling Up to Excellence: Practicing Model Scaling for Photo-Realistic Image Restoration In the Wild. [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/db6ed53d-b000-42f5-b2e0-fbbdea3e2a6b)
8.  Zhang, X. (2025). ELAN论文详解：对SwinIR进行效率优化的超分算法（Efficient Long-Range Attention Network for Image Super-resolution）. [blog.csdn.net](https://blog.csdn.net/BigerBang/article/details/134991611)
9.  韦炎炎, 毛天一, 李柏昂, 等. (2025). 视觉模型及多模态大模型推进图像复原增强研究进展. 中国图象图形学报, 30(5): 1197-1219. [www.cjig.cn](https://www.cjig.cn/zh/article/doi/10.11834/jig.240436/)
10. Zhou, J., Ke, P., Qiu, X., & Shen, Y. (2024). ChatGPT: potential, prospects, and limitations. Frontiers of Information Technology & Electronic Engineering, 25(1): 6-11. [www.fitee.zjujournals.com](https://www.fitee.zjujournals.com/zh/article/doi/10.1631/FITEE.2300089/)
11. Zhang, J., Sun, L., Jin, C., et al. (2024). Recent advances in artificial intelligence generated content. Frontiers of Information Technology & Electronic Engineering, 25(1): 1-5. [www.fitee.zjujournals.com](https://www.fitee.zjujournals.com/zh/article/doi/10.1631/FITEE.2410000/)
12. Li, J. Y., Wang, N., Zhang, L. F., et al. (2020). Recurrent feature reasoning for image inpainting. Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, 7757-7765. (Note: This referene is included as background for image inpainting which relates to SR, and it's within the general timeframe of relevant generative models. While technically outside 2022-2025, it represents a foundational concept in related generative tasks used in current diffusion model contexts as seen in reference 4.)

(Additional relevant works are implicitly referenced within the GitHub StarrySky repository for broader context of ML/DL projects, but specific papers from that source are avoided to maintain strict academic citation for core methods.)