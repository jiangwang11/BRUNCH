# 基于结构相似性度量的图像质量评估技术综述（2022–2025）

## 引言

图像质量评估（Image Quality Assessment, IQA）旨在建立与人类视觉感知一致的客观度量。传统的像素级指标（如 MSE、PSNR）因忽略人眼对结构信息的敏感性而与主观评价存在显著偏差。自 Wang 等人提出结构相似性（SSIM）指标以来，基于结构感知的 IQA 方法已成为主流。2022–2025 年间，该领域在深度学习驱动下，从浅层结构特征演进为对纹理、语义乃至跨模态一致性的建模，涌现出一批创新性工作。本文聚焦此期间基于结构相似性理念的代表性研究，系统梳理其方法演进与性能边界。

## 方法分类与代表作

### 基于多尺度结构与纹理统一的指标

传统 SSIM 及其变体（如 MS-SSIM）主要关注亮度、对比度和结构信息，但对复杂失真（如纹理重采样、生成伪影）鲁棒性不足。Ding 等人在 2020 年提出的 DISTS（Deep Image Structure and Texture Similarity）指标虽略早于时间窗口，但其核心思想深刻影响了后续研究。该工作首次在统一框架下显式建模结构与纹理相似性：利用 VGG 网络提取多尺度特征，并分别通过全局 SSIM 和特征均值（表征纹理）计算相似度；通过在相同纹理区域采样的约束进行优化，使其对几何变换和纹理重采样具有强鲁棒性。该工作在 CVPR 2020 发表，为后续基于深度特征的结构度量奠定了基础，并被广泛用作 LPIPS 等指标的有力竞争者 [wang_ding].

受 DISTS 启发，后续研究进一步探索了结构与纹理的解耦与融合。例如，Ke 等人提出的 MUSIQ（Multi-scale Image Quality Transformer）利用 Transformer 架构处理任意分辨率图像，通过多尺度表示捕捉不同粒度的结构信息，并引入哈希空间位置编码以处理变尺寸输入。该方法在 ICCV 2021 上展示出在大规模数据集（如 KonIQ-10k, PaQ-2-PiQ）上的 SOTA 性能，证明了多尺度建模对结构感知的重要性 [ke2021musiq].

### 基于视觉大模型与多任务学习的无参考评估

随着视觉大模型（Vision Foundation Models, VFMs）的发展，研究者开始利用其强大的语义先验进行无参考 IQA（NR-IQA）。Jin 等人于 2025 年提出的 SAM2ICAA 是首个专门针对色彩准确性评估的 NR-IQA 方法。该研究首先构建了包含8种色彩失真的大规模基准数据集 ICAA-4K，并以 SAM2 的 Hiera 编码器为骨干网络。其核心创新在于设计了一个双任务回归模块，同时预测色彩质量分数和失真类型，模拟了人类“先识别失真再评估质量”的认知过程。实验表明，该方法在色彩准确性评估上显著超越了通用 NR-IQA 模型 [jin2025sam2icaa].

同样利用大模型，Zhang 等人在 2021 年提出的 UNIQUE（Unified No-Reference Image Quality and Uncertainty Evaluator）框架解决了混合失真（合成与真实）下的评估难题。该方法采用一种迭代混合数据库训练策略，并引入不确定性度量，使其能够在一个统一模型下泛化到多种失真类型。其在跨数据库测试中表现出的鲁棒性，为通用 NR-IQA 的实用化提供了新思路 [zhang2021unique].

### 针对特定失真与场景的精细化建模

针对特定应用场景的 IQA 方法在此期间取得了显著进展。Zhou 等人于 2025 年提出了 MTA-SCI（Multi-task Attention Mechanism based No Reference Quality Assessment for Screen Content Images），专门用于评估屏幕内容图像（SCIs）。该方法结合自注意力机制提取全局特征，并设计了综合局部注意力机制聚焦于文本和图像细节。在 SCID 和 SIQAD 数据集上，其 SRCC 分别达到 0.9602 和 0.9233，证明了注意力机制对 SCI 中异构内容的有效建模能力 [zhou2025mta].

在全景图像（Omnidirectional Images, OIs）质量评估领域，Huang 等人于 2025 年提出了一个基于沉浸式立体感知的 NR-IQA 算法。该方法通过 SPHORB 算法在球面域提取高概率视点，并设计视口特征交互模块以建模跨视口依赖。此外，该工作还探索了在无视口采样的情况下直接从全景图建模立体感信息。其在 CVIQD 和 OIQA 数据集上均取得了 SOTA 性能，凸显了对 VR 等新兴应用领域特有挑战的针对性 [huang2025pano].

## 实验与评价总结

对 2022–2025 年代表性工作的共性实验结论可归纳如下：首先，**在大规模、多样化失真数据集上的泛化能力**已成为衡量 IQA 模型优劣的核心标准。基于深度学习的方法，尤其是利用 Transformer 或视觉大模型的架构，在 KonIQ-10k、SPAQ 等真实失真数据集上显著优于传统方法。其次，**多任务学习策略**（如联合预测失真类型、不确定性或显著图）被证明能有效提升模型的可解释性和鲁棒性。最后，**对特定失真或场景的精细化建模**远胜于通用模型的“一刀切”评估，这在 SCI、全景图等任务上表现尤为突出。然而，所有方法在跨域泛化（如从合成失真到真实失真）方面仍面临挑战，且对计算资源的要求普遍较高。

## 趋势与挑战

基于近四年研究动态，2025 年及以后的发展将呈现以下明确趋势：
1.  **视觉-语言大模型（VLMs）的深度融合**：利用 CLIP、Flamingo 等模型的跨模态对齐能力，将文本提示（如“画面是否过曝”、“纹理是否自然”）引入 IQA，使评估过程更具语义指导性和任务针对性。
2.  **动态与视频质量评估的统一框架**：现有工作多聚焦于静态图像，而视频质量评估需考虑帧间一致性、运动流畅度等因素。未来将出现能同时处理静态图像和动态视频的统一 IQA 模型。
3.  **轻量化与可解释性并重**：随着 IQA 在移动设备和实时系统中的部署需求增加，如何在降低模型复杂度的同时，提供可靠的可解释性（如质量热力图、失真定位）将成为关键挑战。

## 结论

2022–2025 年是基于结构相似性的 IQA 技术从成熟走向深化的关键时期。研究重心已从通用结构建模转向结合语义先验、特定场景约束和多任务学习的精细化评估。视觉大模型的兴起为该领域注入了新的活力，但同时也带来了计算成本与可解释性等新挑战。未来，IQA 将朝着更智能（结合 VLMs）、更通用（统一图像与视频）、更实用（轻量可解释）的方向持续演进。

## 参考文献

[ke2021musiq]: Ke, J., Wang, Q., Wang, Y., Milanfar, P., & Yang, F. (2021). MUSIQ: Multi-scale image quality transformer. In *Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV)* (pp. 5128–5137).

[zhang2021unique]: Zhang, W., Ma, K., Zhai, G., & Yang, X. (2021). Uncertainty-aware blind image quality assessment in the laboratory and wild. *IEEE Transactions on Image Processing*, 30, 3474–3486.

[jin2025sam2icaa]: Jin, J., Zhou, T., Hu, Z., & Yang, B. (2025). SAM2ICAA: No-reference image color accuracy assessment via vision foundation models. *Journal of Computer-Aided Design & Computer Graphics*.

[zhou2025mta]: Zhou, Z., Dong, W., Lu, L., Ma, Q., Hou, G., & Zhang, E. (2025). Multi-task attention mechanism based no reference quality assessment algorithm for screen content images. *Opto-Electronic Engineering*.

[huang2025pano]: Huang, X., An, P., Yang, C., & Tang, X. (2025). Omnidirectional image quality assessment algorithm based on stereo perception. *Signal Processing*.

[wang_ding]: Ding, K., Ma, K., Wang, S., & Simoncelli, E. P. (2020). Image quality assessment: Unifying structure and texture similarity. *IEEE Transactions on Pattern Analysis and Machine Intelligence (TPAMI)*, 44(5), 2567–2581.

[you2021triq]: You, J., & Korhonen, J. (2021). Transformer for image quality assessment. *arXiv preprint arXiv:2101.01097*.

[golestaneh2022tr]: Golestaneh, S. A., Dadsetan, S., & Kitani, K. M. (2022). No-reference image quality assessment via transformers, relative ranking, and self-consistency. In *Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision (WACV)* (pp. 3989–3999).

[lin2020deepfl]: Lin, H. H., Hosu, V., & Saupe, D. (2020). DeepFL-IQA: Weak supervision for deep IQA feature learning. *arXiv preprint arXiv:2001.08113*.

[kim2019diqa]: Kim, J., Nguyen, A. D., & Lee, S. (2019). Deep CNN-based blind image quality predictor. *IEEE Transactions on Neural Networks and Learning Systems*, 30(1), 11–24.

[zhu2020metaiqa]: Zhu, H., Li, L., Wu, J., Dong, W., & Shi, G. (2020). MetaIQA: Deep meta-learning for no-reference image quality assessment. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)* (pp. 14131–14140).

[ma2017dipiq]: Ma, K., Liu, W., Zhang, K., Duanmu, Z., Wang, Z., & Zuo, W. (2017). dipIQ: Blind image quality assessment by learning-to-rank discriminable image pairs. *IEEE Transactions on Image Processing*, 26(8), 3951–3964.