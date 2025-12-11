好的，作为一名严谨的科研助手，我将基于您提供的真实网络搜索结果，生成一篇关于“注意力机制在图像去噪中的应用”的学术综述。

### **基于注意力机制的图像去噪技术研究综述 (2022–2025年)**

---

#### **摘要**
图像去噪是计算机视觉领域的基础任务。近年来，深度学习方法，特别是卷积神经网络（CNN）已成为主流。然而，CNN固有的局部感受野限制了其对图像全局依赖关系的建模能力。注意力机制，尤其是源于Transformer的自注意力，为解决此问题提供了有效途径。本综述聚焦于2022至2025年间，系统梳理和分析了将注意力机制应用于图像去噪领域的代表性研究工作。本文首先对现有方法进行分类，涵盖了混合架构、自监督学习以及新兴网络架构的探索；随后总结了这些方法在常用基准数据集上的共性实验表现；最后，基于当前研究现状，对未来技术趋势与面临的挑战进行了预测。

---

### **1. 引言**

在数字图像的获取与传输过程中，噪声的引入不可避免，它严重降低了图像质量并影响后续高级视觉任务的性能。图像去噪旨在从含噪图像中恢复出干净的清晰图像。早期的方法主要基于信号处理和手工先验，如块匹配三维滤波（BM3D）[www.opticsjournal.net](https://www.opticsjournal.net/Articles/OJ6f91743d6d014d4b/FullText)。随着深度学习的发展，以DnCNN为代表的卷积神经网络（CNN）因其强大的特征学习能力而占据主导地位，但CNN的卷积操作本质上是局部的，难以捕捉远距离的像素依赖关系，导致在处理非局部纹理和复杂结构时效果受限。

为突破这一局限，研究者们引入了注意力机制。该机制允许模型动态地为不同空间位置或特征通道分配不同的权重，从而聚焦于更重要的信息。特别是自注意力（Self-Attention）机制，通过计算特征内部各元素间的相关性，实现了对全局上下文的有效建模。近年来，融合注意力机制的去噪网络在性能上取得了显著突破。本综述旨在系统归纳2022至2025年间该领域的最新进展，为相关研究人员提供参考。

### **2. 方法分类与代表作**

根据注意力机制的实现方式和网络架构，近年的研究可主要分为以下几类：

#### **2.1 混合架构：CNN与注意力机制的融合**

该类别是当前的主流方向，旨在结合CNN的局部归纳偏置（Inductive Bias）和注意力机制的全局建模能力。

*   **通道注意力与卷积网络结合**
    一篇针对工业CT图像去噪的研究 [cttacn.org.cn](https://cttacn.org.cn/article/doi/10.15953/j.ctta.2025.068)，旨在解决投影数据质量差导致的重建图像信噪比低的问题。该方法在U-Net结构的解码器中嵌入了通道注意力模块（Squeeze-and-Excitation Block），通过自适应地调整各特征通道的权重，使网络在去噪时能更好地关注并保留关键的结构细节。实验结果表明，该方法在去除噪声的同时，能有效保护图像的边缘和细节，其视觉效果和定量指标均优于对比的经典算法。另一项面向遥感图像去噪的工作 [image.hanspub.org](https://image.hanspub.org/Html/9-1543124_84547.htm) 则关注于平衡感受野与计算效率。其提出的多级小波CNN模型（AMWCNN）在改进的U-Net中使用离散小波变换（DWT）替代池化层，并引入通道注意力机制来针对性地提取噪声成分。实验在高斯噪声下，其PSNR值较DNCNN和FFDNET等方法平均提升约10%，并能有效保护遥感图像的边缘特征。

*   **Transformer/自注意力与卷积网络结合**
    Jiang等人提出了一种动态关联学习方法ELF [www.cjig.cn](https://www.cjig.cn/zh/article/doi/10.11834/jig.230323/)，用于解决图像修复任务中CNN和自注意力（SA）如何高效协同的问题。该方法设计了一个新的多输入注意力模块，将CNN的局部感知能力与SA的全局聚合能力并行结合，通过关联学习的方式共同处理降质扰动消除和背景修复。实验证明，该混合架构在图像去雨任务上，PSNR值相比代表性的MPRNet提升了0.9 dB，验证了CNN与SA动态关联的有效性。另一篇针对低剂量纳米CT图像的研究提出了SwinCBD模型 [www.opticsjournal.net](https://www.opticsjournal.net/Articles/OJf6ace6d4916b8af8/FullText)，该模型旨在解决低曝光和少投影导致的严重噪声问题。它将Swin Transformer模块嵌入U-Net架构的编码器和解码器中，利用其窗口化自注意力机制高效捕捉全局和局部特征，同时结合噪声估计子网络实现盲去噪。实验结果显示，该模型可将低剂量CT切片的信噪比（SNR）提升49.26%，并将数据采集时间缩短90%以上，同时保持图像质量。

#### **2.2 自监督学习与注意力机制**

在难以获取成对（干净/含噪）训练数据时，自监督去噪成为关键。注意力机制在此类方法中同样展现了其增强特征表达的潜力。

*  **MM-SSID** [www.opticsjournal.net](https://www.opticsjournal.net/Articles/OJ6f91743d6d014d4b/FullText) 旨在解决自监督去噪因缺乏清晰图像标签而效果受限的问题。该方法提出了一种包含记忆单元（Memory Unit）的多阶段训练方案，其中细节感知网络（DSN）部分采用了堆叠的通道注意力模块来增强对图像纹理细节的表达能力。通过分阶段学习平坦与纹理区域的特征，并利用记忆单元保存中间去噪结果以协同监督训练。实验表明，该方法在SIDD和DND数据集上的PSNR分别达到37.30 dB和38.52 dB，显著优于现有的其他自监督去噪方法。

#### **2.3 新兴网络架构的探索**

随着深度学习架构的演进，研究人员开始探索将注意力机制与CNN和Transformer之外的新型骨干网络相结合。

*   **MambaIR** [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/99851) 是一项探索状态空间模型（SSM）用于图像恢复的开创性工作，旨在解决现有骨干网络在全局感受野和高效计算之间的困境。研究发现，标准的Mamba模型在应用于低级视觉任务时存在通道冗余等问题，为此，MambaIR通过引入局部增强和**通道注意力**对原始Mamba进行改进。这使得模型在具备线性复杂度和全局感受野的同时，能够有效减少冗余特征。实验显示，MambaIR在图像超分辨率任务上比SwinIR性能更高（PSNR提升0.45 dB），证明了SSM结合注意力机制在图像恢复领域的巨大潜力。

### **3. 实验与评价总结**

*   **数据集与评价指标**：上述研究普遍在公开基准数据集上进行评估，如用于真实噪声的**SIDD**和**DND**数据集 [www.opticsjournal.net](https://www.opticsjournal.net/Articles/OJ6f91743d6d014d4b/FullText)。此外，面向特定领域的研究也构建了专用数据集，如遥感图像数据集（**NWPU-RESISC45**）[image.hanspub.org](https://image.hanspub.org/Html/9-1543124_84547.htm)和**纳米CT**数据集 [www.opticsjournal.net](https://www.opticsjournal.net/Articles/OJf6ace6d4916b8af8/FullText)。评价指标方面，全参考指标**峰值信噪比（PSNR）**和**结构相似性（SSIM）**仍是金标准。同时，部分研究也引入了无参考指标如**NIQE**和**BRISQUE** [www.opticsjournal.net](https://www.opticsjournal.net/Articles/OJf6ace6d4916b8af8/FullText) 来评估在缺乏真实标签时的图像质量。

*   **共性结论**：
    1.  **性能普遍提升**：无论是作为插件模块还是作为核心构建块，注意力机制的引入普遍能为基线模型带来显著的性能增益。例如，在CNN中加入通道注意力可使PSNR提升10% [image.hanspub.org](https://image.hanspub.org/Html/9-1542465_49977.htm)；混合CNN与SA架构比单一架构性能更优 [www.cjig.cn](https://www.cjig.cn/zh/article/doi/10.11834/jig.230323/)。
    2.  **结构与细节保持**：基于自注意力的模型（如Transformer）在捕捉图像的全局结构和长距离依赖上表现出色，这使得它们在恢复具有复杂纹理和重复结构的图像时，伪影更少，细节保持更完整 [www.opticsjournal.net](https://www.opticsjournal.net/Articles/OJf6ace6d4916b8af8/FullText)。
    3.  **任务适应性**：注意力机制能够根据输入图像的内容或退化类型动态调整处理策略。例如，在处理混合失真图像时，注意力可以作为不同操作的“切换器”，自适应地选择最优的复原路径 [image.hanspub.org](https://image.hanspub.org/Html/2-1542465_49977.htm)。

### **4. 趋势与挑战**

基于2022-2025年的研究，未来图像去噪领域中注意力机制的应用将呈现以下趋势，并伴随相应挑战：

1.  **架构创新与效率的极致追求**：从CNN到Transformer再到状态空间模型（Mamba）的演进路径清晰地表明，研究界正不断寻求能以更高效率实现全局交互的新架构 [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/99851)。未来的趋势将是设计具有线性或近线性计算复杂度、同时又能保持强大长程依赖建模能力的轻量化注意力变体或全新架构。**挑战**在于如何在降低计算成本的同时避免性能损失，并使其适用于高分辨率图像和移动端设备。

2.  **自监督/无监督范式的深化**：获取大规模成对的真实噪声数据成本高昂。因此，仅使用含噪图像进行训练的自监督方法是未来研究的重点。如MM-SSID [www.opticsjournal.net](https://www.opticsjournal.net/Articles/OJ6f91743d6d014d4b/FullText) 所示，注意力机制可以与更精巧的自监督策略（如利用记忆库存储伪标签）相结合。未来的趋势是探索如何利用注意力机制从噪声中更有效地解耦信号与噪声，或者在生成式模型中引导生成更真实的伪干净图像。**挑战**在于如何设计更鲁棒的自监督损失函数以及避免模型“记住”噪声特性而非学习去噪。

3.  **面向特定领域的深度融合**：通用去噪模型在特定应用场景（如医学影像、遥感、工业检测）中常有局限性。现有工作已开始针对工业CT [cttacn.org.cn](https://cttacn.org.cn/article/doi/10.15953/j.ctta.2025.068) 和纳米CT [www.opticsjournal.net](https://www.opticsjournal.net/Articles/OJf6ace6d4916b8af8/FullText) 等设计专用模型。未来的趋势是将成像物理先验或领域知识更紧密地融入注意力网络设计中，使模型不仅从数据中学习，还能遵循物理规律。**挑战**在于如何有效地将非微分的物理模型与基于梯度的深度学习框架相结合，以及如何获取高质量的领域专用数据。

### **5. 结论**

在2022至2025年间，注意力机制已从一个增强模块演变为图像去噪网络设计的核心驱动力之一。研究工作系统地展示了其在融合CNN与Transformer、赋能自监督学习以及探索新兴架构中的关键作用。通过动态地重新校准特征，注意力机制使模型能够更智能地处理复杂的真实世界噪声，在保持图像全局结构和恢复精细纹理方面取得了显著进展。展望未来，更高效的注意力架构、更深入的自监督范式以及与领域知识的紧密结合，将是推动该领域持续向前发展的主要方向。

### **6. 参考文献**

1.  何雨, 王成祥, 余维. (2025). 基于通道注意力机制的工业CT图像去噪网络. *CT理论与应用研究*. [cttacn.org.cn](https://cttacn.org.cn/article/doi/10.15953/j.ctta.2025.068)
2.  张晓东, 祝令函, 高绍姝, 等. (2025). 基于记忆单元的多阶段图像自监督去噪方法. *激光与光电子学进展*. [www.opticsjournal.net](https://www.opticsjournal.net/Articles/OJ6f91743d6d014d4b/FullText)
3.  成丽波, 苑浩然, 李喆, 等. (2024). 基于注意力机制的多级小波CNN遥感图像去噪算法. *Computer Science and Application*. [image.hanspub.org](https://image.hanspub.org/Html/9-1543124_84547.htm)
4.  汪澳, 彭真, 汪俊, 等. (2025). 基于Swin Transformer和卷积神经网络的低剂量纳米CT重建图像去噪. *光电工程*. [www.opticsjournal.net](https://www.opticsjournal.net/Articles/OJf6ace6d4916b8af8/FullText)
5.  江奎, 贾雪梅, 黄文心, 等. (2024). 图像复原中自注意力和卷积的动态关联学习. *中国图象图形学报*. [www.cjig.cn](https://www.cjig.cn/zh/article/doi/10.11834/jig.230323/)
6.  Guo, H., Li, J., Dai, T., et al. (2024). MambaIR: A Simple Baseline for Image Restoration with State-Space Model. *ECCV 2024*. [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/99851)
7.  龚敏学, 朱烨, 符颖. (2022). 注意力机制引导的混合失真图像复原研究. *Computer Science and Application*. [image.hanspub.org](https://image.hanspub.org/Html/2-1542465_49977.htm)
8.  林晓, 周云翔, 李大志, 等. (2022). 利用多尺度特征联合注意力模型的图像修复. *计算机辅助设计与图形学学报*. [www.jcad.cn](https://www.jcad.cn/article/doi/10.3724/SP.J.1089.2022.19172)
9.  曹承瑞, 刘微容, 史长宏, 等. (2022). 多级注意力传播驱动的生成式图像修复方法. *自动化学报*. [aas.net.cn](https://aas.net.cn/cn/article/doi/10.16383/j.aas.c200485?viewType=HTML)
10. Ding, S., Wang, Q., Guo, L., et al. (2023). A novel image denoising algorithm combining attention mechanism and residual UNet network. *Knowledge and Information Systems*. [www.ablesci.com](https://www.ablesci.com/assist/detail?id=55KzDy)
11. Dabov, K., Foi, A., Katkovnik, V., et al. (2007). Image denoising by sparse 3-D transform-domain collaborative filtering. *IEEE Transactions on Image Processing*. [www.opticsjournal.net](https://www.opticsjournal.net/Articles/OJ6f91743d6d014d4b/FullText)
12. Zhang, K., Zuo, W., Chen, Y., et al. (2017). Beyond a Gaussian denoiser: Residual learning of deep CNN for image denoising. *IEEE Transactions on Image Processing*. [www.opticsjournal.net](https://www.opticsjournal.net/Articles/OJf6ace6d4916b8af8/FullText)
13. Liang, J., Cao, J., Sun, G., et al. (2021). SwinIR: Image restoration using Swin Transformer. *ICCVW 2021*. [www.opticsjournal.net](https://www.opticsjournal.net/Articles/OJf6ace6d4916b8af8/FullText)
14. Zamir, S. W., Arora, A., Khan, S., et al. (2021). Multi-stage progressive image restoration. *CVPR 2021*. [www.cjig.cn](https://www.cjig.cn/zh/article/doi/10.11834/jig.230323/)