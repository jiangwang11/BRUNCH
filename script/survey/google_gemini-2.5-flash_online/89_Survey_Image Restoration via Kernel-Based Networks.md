## 基于核网络图像恢复的学术综述 (2022–2025)

### 引言
图像恢复旨在从退化的观测中重建高质量图像，是计算机视觉领域的核心任务之一。传统的卷积神经网络 (CNN) 方法因其局部感受野的限制，在处理长距离依赖和复杂退化方面存在不足。近年来，Transformer 模型凭借其强大的全局依赖建模能力在图像恢复领域取得了显著进展，但其高昂的计算复杂度限制了在高分辨率图像上的应用。为解决这一困境，研究者重新审视了基于核（Kernel-Based）的网络结构，通过设计大核卷积、状态空间模型（SSM）等方式，在保持计算效率的同时，有效拓展了模型的感受野和全局建模能力，成为 2022-2025 年图像恢复领域的重要研究方向。本综述将聚焦于此，对相关代表性工作进行梳理与分析。

### 方法分类与代表作

本节将基于核网络在图像恢复中的应用，将其分为以下几个主要类别：

#### 1. 大型卷积核网络（Large Kernel Network）
针对传统CNN局部感受野有限的问题，这类方法通过设计大尺寸卷积核，以增强模型捕捉多尺度和长距离特征的能力，同时通过重参数化等技术优化计算效率。

*   **Omni-Kernel Network (OKNet)** [blog.csdn.net](https://blog.csdn.net/a486259/article/details/142406557)
    *   **研究问题**: 传统Transformer模型虽能有效建模长距离依赖，但其二次复杂度不适用于高分辨率图像恢复。现有大核CNN仍无法提供全局感受野。
    *   **核心方法**: 提出全核模块（OKM），由全局、大型和局部分支构成。全局分支通过双域通道注意和频率门控机制实现全局感知；大型分支采用超大（如63x63）深度卷积以获取多粒度大感受野，并在瓶颈层部署以降低计算量；局部分支则使用1x1深度卷积补充局部信息。
    *   **关键实验结论**: OKNet在图像去模糊、图像去雨和图像去雾等11个基准数据集上均取得了SOTA性能，例如在单图像离焦去模糊任务上，PSNR比强Transformer模型Restorer提升0.2dB，且参数量更少。

*   **RepLK-HRNet** [journal.ecust.edu.cn](https://journal.ecust.edu.cn/en/article/pdf/preview/10.14135/j.cnki.1006-3080.20240722001.pdf)
    *   **研究问题**: 高分辨率人体姿态估计在动态场景、目标遮挡及复杂背景下精度和鲁棒性面临挑战，传统Transformer模型计算复杂度高。
    *   **核心方法**: 提出融合重参数化大核卷积的高分辨率人体姿态估计模型RepLK-HRNet。以HRNet为基础框架，引入空洞重参数化大核卷积单元，通过扩大感受野、多层次特征提取和多尺度特征融合，增强模型捕捉复杂特征的能力。
    *   **关键实验结论**: RepLK-HRNet在标准数据集MS COCO2017上的姿态估计精度提高了1.83%，在遮挡数据集OCHuman上提高了23.7%，同时计算量和参数量显著降低，展现了出色的鲁棒性和泛化能力。

#### 2. 状态空间模型（State-Space Model, SSM）基线
SSM，尤其是Mamba及其变体，因其在序列建模中具备线性复杂度下捕捉长距离依赖的潜力，被引入到图像恢复领域，以克服CNN和Transformer的局限性。

*   **MambaIR: A Simple Baseline for Image Restoration with State-Space Model** [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/99851)
    *   **研究问题**: 现有图像恢复骨干网络在全局感受野和高效计算之间存在矛盾，而标准Mamba在低级视觉任务中面临局部像素遗忘和通道冗余。
    *   **核心方法**: 提出MambaIR基线模型，通过引入局部增强和通道注意力机制，改进原始Mamba模型。局部增强旨在解决局部像素遗忘问题，通道注意力则用于减少通道冗余，从而更好地利用局部像素相似性。
    *   **关键实验结论**: 在图像超分辨率任务中，MambaIR比SwinIR性能提升高达0.45dB，在相似计算成本下实现了全局感受野，并可视化展示了其显著的全局有效感受野。

*   **MambaIRv2: Attentive State Space Restoration** [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/85148)
    *   **研究问题**: Mamba固有的因果建模限制（每个标记只依赖于扫描序列中的前驱）阻碍了对图像像素的充分利用，带来了图像恢复的新挑战。
    *   **核心方法**: 提出MambaIRv2，赋予Mamba类似于ViTs的非因果建模能力。通过注意状态空间方程实现超越扫描序列的关注，并通过一次扫描促进图像展开。此外，引入语义引导的邻域机制以鼓励远距离但相似像素之间的交互。
    *   **关键实验结论**: MambaIRv2在轻量级超分辨率任务中比SRFormer的PSNR提升高达0.35dB，参数减少9.3%；在经典超分辨率任务中，性能超越HAT模型高达0.29dB。

#### 3. 基于Transformer的高效核方法
这类方法将Transformer的全局建模能力与卷积操作的局部性相结合，或通过优化注意力机制来降低计算复杂度，实现高效的图像恢复。

*   **Restormer: Efficient Transformer for High-Resolution Image Restoration** [cloud.tencent.cn](https://cloud.tencent.cn/developer/article/2398294?policyId=1003) (CVPR 2022)
    *   **研究问题**: Transformer模型在高分辨率图像恢复任务中计算复杂度过高，难以实际应用。
    *   **核心方法**: 提出Restormer，通过在构建模块中进行关键设计来捕获长距离像素交互，同时适用于大图像。核心是多Dconv头“转置”注意力（MDTA）块和门控Dconv前馈网络（GDFN）。MDTA将自注意力应用于特征维度而非空间维度，并结合深度卷积进行局部上下文混合；GDFN通过门控机制和深度卷积优化特征变换。
    *   **关键实验结论**: Restormer在图像去噪、运动去模糊、散焦去模糊和图像去雨等多个基准数据集上实现了SOTA结果，在处理高分辨率图像时具有计算效率。

#### 4. 扩散模型与核方法的融合
扩散模型在图像生成和恢复中显示出强大潜力，与核方法结合可以进一步提升其效率和性能，尤其是在处理特定退化或低资源场景下。

*   **DiffIR: Efficient Diffusion Model for Image Restoration** [zhuanzhi.ai](https://www.zhuanzhi.ai/paper/246fe9068ef5a64044cb6d4fcbe1574a) (2023)
    *   **研究问题**: 传统扩散模型在图像恢复任务中效率低下，因为大多数像素已给定，而它们仍需要大量迭代来估计完整的图像或特征图。
    *   **核心方法**: 提出DiffIR，一种高效的图像恢复扩散模型，包含紧凑的IR先验提取网络（CPEN）、动态IR转换器（DIRformer）和去噪网络。通过两阶段训练，前期CPEN提取紧凑的IR先验表示（IPR），后期DM直接估计此紧凑向量，而非完整的图像。
    *   **关键实验结论**: DiffIR在多个IR任务上实现了SOTA性能，同时显著降低了计算成本，因为它使用较少迭代即可获得准确估计和更稳定逼真的结果。

*   **Few-shot exemplar-driven inpainting with parameter-efficient diffusion fine-tuning** [www.fitee.zjujournals.com](https://www.fitee.zjujournals.com/zh/article/doi/10.1631/FITEE.2400395/) (2025)
    *   **研究问题**: 现有参考图驱动的图像补全方法难以实现高保真度，且扩散模型微调成本较高。
    *   **核心方法**: 基于预训练的文本驱动图像补全模型，引入即插即用的低秩适配（LoRA）模块，通过少样本微调学习参考图像的特定特征。结合GPT-4V提示词和先验噪声初始化技术，引导去噪扩散过程。
    *   **关键实验结论**: 该方法在定性和定量指标上均达到SOTA水平，为用户提供具有更强定制化能力的参考图驱动图像补全工具，无需大规模数据集训练即可提升高保真度。

### 实验与评价总结
2022-2025年间，基于核网络（包括大核卷积、SSM和高效Transformer）的图像恢复方法在多个典型任务上展现出优越性。这些方法普遍采用PSNR和SSIM等客观指标，并在DIV2K、MS COCO、DPDD等基准数据集上进行评估。与传统CNN和初期Transformer模型相比，这些新方法在性能（如PSNR值提高达0.2-0.45dB）和计算效率之间取得了更好的平衡。关键性改进包括：
1.  **感受野与效率的统一**：通过大核卷积和Mamba类模型的线性复杂度，实现了更广阔的感受野以捕捉全局依赖，避免了传统CNN的局部性限制和标准Transformer的二次复杂度难题。
2.  **多尺度特征学习**：引入多粒度卷积、多分支结构、空间与通道注意力等机制，增强了模型对图像不同尺度细节和上下文信息的学习能力。
3.  **针对特定任务优化**：部分工作针对图像去模糊、去雨、去雾、超分辨率甚至姿态估计等特定任务进行了量身定制的模块设计，取得了显著提升。
4.  **模型轻量化与可部署性**：通过将复杂模块置于网络瓶颈处、采用重参数化技术或低秩适配等方法，有效降低了模型参数量和计算开销，使其更适用于实际应用和资源受限环境。
5.  **融合新兴技术**：将扩散模型、自注意力机制中的高效设计与核方法相结合，开辟了新的图像恢复范式，提升了生成图像的真实感和特定化能力。

### 趋势与挑战
展望2025年及未来几年，基于核网络的图像恢复研究将呈现以下趋势与挑战：

1.  **统一多任务与通用化骨干网络**：当前研究多针对特定退化任务进行优化。未来趋势将是开发更通用的核网络骨干，能够自适应处理多种未知类型和强度的混合退化，甚至跨越图像和视频等不同模态。这要求模型不仅能识别退化类型，还能选择或组合最优恢复策略，例如 [image.hanspub.org](https://image.hanspub.org/Html/2-1542465_49977.htm) 中提出的注意力引导操作层模块。
2.  **高效与大规模部署**：随着模型规模的增长和应用场景的拓展（如边缘设备、实时系统），核网络如何进一步优化模型架构，降低推理延迟和内存占用将是关键。参数高效微调（如LoRA）与模型剪枝、量化等技术与核方法的深度融合将成为常态，以实现大规模模型的轻量化部署。
3.  **与生成模型（尤其是扩散模型）的深度融合**：扩散模型在图像质量和多样性方面表现突出，但其采样速度和对先验信息的整合仍有提升空间。结合核网络，研究者将探索更高效、可控的扩散采样策略，例如利用核方法提取更紧凑或多层次的潜在表示，以加速扩散过程并提升恢复质量，如 [zhuanzhi.ai](https://www.zhuanzhi.ai/paper/246fe9068ef5a64044cb6d4fcbe1574a) 和 [www.fitee.zjujournals.com](https://www.fitee.zjujournals.com/zh/article/doi/10.1631/FITEE.2400395/) 中的工作所示。同时，如何利用扩散模型的生成能力处理更具挑战性的逆问题（如从高度损坏的图像中重建）也将是重要方向。

### 结论
2022-2025 年，核网络在图像恢复领域重新焕发活力，通过大核卷积、状态空间模型和高效Transformer等创新设计，有效弥合了传统CNN与Transformer在效率和感受野之间的鸿沟。这些方法在多种图像恢复任务中取得了显著的性能提升，同时兼顾了计算效率，为实际应用提供了新的可能。未来的研究将继续探索更通用、更高效、更智能的核网络架构，并将其与新兴的生成模型深度融合，以应对图像恢复领域日益复杂的挑战。

### 参考文献

1.  Guo, H., Li, J., Dai, T., Ouyang, Z., Ren, X., & Xia, S.-T. (2025). MambaIR: A Simple Baseline for Image Restoration with State-Space Model. *ECCV 2024*. [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/99851)
2.  Guo, H., Guo, Y., Zha, Y., Zhang, Y., Li, W., Dai, T., Xia, S.-T., & Li, Y. (2024). MambaIRv2: Attentive State Space Restoration. *arXiv preprint arXiv:2411.15269*. [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/85148)
3.  Tu, Z., Yuan, Y., & Sun, X. (2022). Restormer: Efficient Transformer for High-Resolution Image Restoration. *CVPR 2022*. [cloud.tencent.cn](https://cloud.tencent.cn/developer/article/2398294?policyId=1003)
4.  Cai, J., Huang, X., Wu, S., & Wang, X. (2025). High-Resolution Pose Estimation Based on Reparameterized Large Kernel Convolution. *Journal of East China University of Science and Technology, 51*(3), 341-352. [journal.ecust.edu.cn](https://journal.ecust.edu.cn/en/article/pdf/preview/10.14135/j.cnki.1006-3080.20240722001.pdf)
5.  Gong, M., Zhu, Y., & Fu, Y. (2022). Attention-Guided Image Restoration on Hybrid Distortion. *Computer Science and Application, 12*(04), 775-784. [image.hanspub.org](https://image.hanspub.org/Html/2-1542465_49977.htm)
6.  Xia, B., Zhang, Y., Wang, S., Wang, Y., Wu, X., Tian, Y., Yang, W., & Gool, L. Van. (2023). DiffIR: Efficient Diffusion Model for Image Restoration. *arXiv preprint arXiv:2303.09472*. [zhuanzhi.ai](https://www.zhuanzhi.ai/paper/246fe9068ef5a64044cb6d4fcbe1574a)
7.  Yang, S., Gu, Z., Hao, W., et al. (2025). Few-shot exemplar-driven inpainting with parameter-efficient diffusion fine-tuning. *Frontiers of Information Technology & Electronic Engineering, 26*(8), 1428-1440. [www.fitee.zjujournals.com](https://www.fitee.zjujournals.com/zh/article/doi/10.1631/FITEE.2400395/)
8.  Wang, X., Lv, K., Ma, H., et al. (2024). Omni-Kernel Network for Image Restoration. *AAAI 2024*. [blog.csdn.net](https://blog.csdn.net/a486259/article/details/142406557)
9.  Wei, Y., Mao, T., Li, B., Wang, F., Li, F., Zhang, Z., & Zhao, Y. (2025). Visual and large multimodal models promote image restoration and enhancement: research progress. *Journal of Image and Graphics, 30*(5), 1197-1219. [www.cjig.cn](https://www.cjig.cn/zh/article/doi/10.11834/jig.240436/)
10. Liang, J-Y., Cao, J-Z., Sun, G-L., Fan, K., & Van Gool, L. (2021). SwinIR: Image Restoration Using Swin Transformer. *ICCV Workshops 2021*. [github.com](https://github.com/Giserlei123/StarrySky) (提及SwinIR作为对比基线模型)
11. Ding, X., Zhang, X.Y., Zhou, Y., et al. (2022). Scaling Up Your Kernels to 31x31: Revisiting Large Kernel Design in CNNs. *CVPR 2022*. [github.com](https://github.com/Giserlei123/StarrySky) (提及相关概念)
12. Zamir, S. W., Arora, A., Khan, S., & Shah, M. (2022). Multi-stage progressive image restoration. *CVPR 2022*. (提及Restorer作为对比基线模型)