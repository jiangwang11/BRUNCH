好的，遵照您的指示。作为一名严谨的科研助手，我将基于提供的真实联网搜索结果，为您生成一篇关于「基于小波的神经网络函数逼近架构」的中文学术综述。

***

### **基于小波的神经网络函数逼近架构学术综述**

**摘要**：深度神经网络（DNNs）作为通用的函数逼近器，在各类任务中取得了巨大成功。然而，主流架构如卷积神经网络（CNN）和Transformer在感受野、计算效率和多尺度特征表征上仍存在固有限制。小波变换（Wavelet Transform, WT）作为一种经典的时频分析工具，因其出色的多分辨率分析能力和局部化特性，近年来被重新引入神经网络设计中，形成了新的研究范式。本综述旨在系统梳理2022-2025年间，将小波变换与神经网络架构相融合的代表性工作。本文首先对相关方法进行分类，主要涵盖小波与卷积网络、小波与Transformer架构的融合两大方向，并剖析了其在计算机视觉、信号处理等领域的具体应用。随后，本文对这些方法的实验表现和共性优势进行归纳与评价。最后，基于现有研究，本文对未来研究趋势与挑战进行了展望。

#### **1. 引言**

深度学习的发展将神经网络的函数逼近能力推向了新的高度。卷积神经网络（CNN）通过局部连接和权值共享有效提取空间层次特征，但在有限的感受野（Receptive Field, RF）下难以捕捉全局依赖。视觉Transformer（ViT）通过自注意力机制实现了全局感受野，但其二次方复杂度的计算成本高昂，且对局部细节的建模相对较弱。这些挑战促使研究者探索更高效、更能兼顾全局与局部信息的网络架构。

小波变换是一种能够将信号分解为不同尺度和频率分量的数学工具。相较于傅里叶变换，小波变换具备优异的时频局部化（time-frequency localization）特性，使其在保留信号局部信息的同时进行多尺度分析成为可能。将小波变换的原理融入神经网络设计，旨在利用其多分辨率分析能力来克服现有架构的瓶颈：一方面，通过小波分解高效地扩大感受野，增强模型对低频全局信息的感知；另一方面，在不同频带上进行差异化处理，实现对多尺度特征的精细建模。本综述聚焦于2022-2025年间将小波理论与深度学习模型结合以提升函数逼近能力的最新进展。

#### **2. 方法分类与代表作**

近年来，基于小波的神经网络架构研究主要集中在两大方向：与卷积神经网络的融合，以及与Transformer架构的结合。

##### **2.1 小波与卷积神经网络（CNN）的融合**

该方向旨在通过引入小波变换来弥补CNN在感受野和频率响应上的不足，典型工作通过替换或增强卷积、池化等基本操作实现。

*   **Wavelet Convolutions for Large Receptive Fields (WTConv)**
    **研究问题**：直接增大CNN的卷积核尺寸以模拟ViT的全局感受野，会导致参数量急剧增加并很快遭遇性能瓶颈。
    **核心方法**：该研究由Finder等人提出，并发表于ECCV 2024，提出了一种新型卷积层**WTConv** [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/38389)。WTConv利用级联的哈尔（Haar）小波变换将输入特征图分解为多个频率子带，然后在每个子带上应用小型卷积核进行计算，最终通过逆小波变换重构特征。这种设计使得对于一个$k \times k$的感受野，可训练参数量仅随$k$呈对数增长，而非传统大核卷积的平方增长。
    **关键实验结论**：在ConvNeXt和MobileNetV2等架构中用WTConv替换深度可分离卷积后，ImageNet-1K分类、ADE20K语义分割和COCO目标检测任务性能均得到提升。此外，该模型表现出对图像损坏更强的鲁棒性，并增强了对形状（低频信息）而非纹理（高频信息）的偏好 [blog.csdn.net](https://blog.csdn.net/lichlee/article/details/142910207)。

*   **Remote Sensing Image Denoising Based On Multi-Level Wavelet CNN with Attention Mechanism**
    **研究问题**：在遥感图像去噪任务中，如何在扩大感受野以利用上下文信息与控制计算成本之间取得平衡。
    **核心方法**：Cheng等人于2024年提出了一种基于多级小波CNN和注意力机制的U-Net变体结构。该方法使用离散小波变换（DWT）和逆小波变换（IWT）分别替代U-Net中的下采样（池化）和上采样操作，从而在减小特征图尺寸的同时避免信息丢失 [image.hanspub.org](https://image.hanspub.org/Html/9-1543124_84547.htm)。同时，模型引入了通道注意力机制，以增强对噪声特征的针对性提取。
    **关键实验结论**：在遥感图像去噪任务中，相比于DnCNN、FFDNet等方法，该模型在高斯噪声标准差为15、25、30的设定下，PSNR值平均提升约10%，并且能更有效地保护图像的边缘和细节特征。

##### **2.2 小波与Transformer架构的结合**

该方向致力于利用小波变换的多尺度特性来辅助Transformer，或弥补其计算效率和局部建模不足的问题。

*   **WavEnhancer: Unifying Wavelet and Transformer for Image Enhancement**
    **研究问题**：传统的图像增强方法难以协同优化图像的不同频率域，导致局部细节与全局风格不协调。
    **核心方法**：Pun等人于2024年提出了图像增强框架**WavEnhancer**。该模型首先通过DWT将输入图像分解为低频（LL）分量和高频（HL, LH, HH）分量；接着，利用一个基于Transformer的全局风格重映射模块（GSR）处理代表全局信息的LL分量，同时使用一个U-Net结构的细节参数精细化模块（DPR）处理高频分量 [jcst.ict.ac.cn](https://jcst.ict.ac.cn/cn/article/doi/10.1007/s11390-024-3414-z)。
    **关键实验结论**：实验证明，通过对不同频带进行专门处理，WavEnhancer在峰值信噪比（PSNR）、结构相似性（SSIM）和Delta E等多项指标上均优于现有的SOTA方法，实现了更优的视觉增强效果。

*   **A Modulation Recognition Method Combining Wavelet Denoising Convolution and Sparse Transformer**
    **研究问题**：在处理时域信号（如无线通信信号）时，标准Transformer模型存在输入长度受限以及忽略有序特征相关性的问题。
    **核心方法**：Zheng等人于2025年提出一种用于自动调制识别（AMC）的稀疏Transformer（SENet）。该方法首先设计了一个**可学习的小波去噪卷积**模块，以自适应地提取鲁棒的时频特征表示，为后续网络提供高质量输入。然后，模型使用一个稀疏前馈网络（SFFN）替换传统Transformer中的自注意力机制，以更高效的方式对信号元素间的关系进行建模 [jeit.ac.cn](https://jeit.ac.cn/cn/article/doi/10.11999/JEIT241159?viewType=HTML)。
    **关键实验结论**：在公开数据集RadioML 2016.10a和RML22上，该模型取得了63.84%和71.13%的平均分类准确率，相比其他深度学习模型提升了4%-10%，证明了小波预处理与稀疏结构结合的有效性。

##### **2.3 在特定领域的应用探索**

除了上述通用架构的改进，小波神经网络在特定数据模态上也展现出独特的优势。

*   **Hyperspectral Image Classification Model Based on Wavelet Transform and Multi-Scale Attention (WTMSA)**
    **研究问题**：高光谱图像（HSI）数据同时包含丰富的空间信息和长序列的光谱信息，传统CNN难以捕捉长程依赖，而Transformer可能丢失局部细节。
    **核心方法**：Yi和Jiao于2025年提出**WTMSA**模型，该模型将小波变换（WT）与多尺度注意力机制（MSA）相结合。WT首先将高光谱数据分解为多个频率子带，便于进行细粒度分层分析；随后MSA模块结合不同尺寸的卷积核提取多尺度信息，并通过注意力机制学习不同尺度特征的重要性，实现高效融合 [pdf.hanspub.org](https://pdf.hanspub.org/jisp2025142_52670413.pdf)。
    **关键实验结论**：在Indian Pines、Salinas等公开高光谱数据集上，WTMSA的分类精度在OA、AA和Kappa系数上均显著优于传统的CNN及Transformer模型（如ViT、SF），证明了该方法在处理复杂高维数据上的潜力。

*   **Graph Wavelet Neural Network (GWNN)**
    **研究问题**：早期的谱域图神经网络（GNN）依赖于图傅里叶变换，其特征分解计算成本高昂（$O(N^3)$），且傅里叶基是全局的，不利于学习局部化特征。
    **核心方法**：Xu等人在ICLR 2019上提出的**GWNN**是该领域的奠基性工作之一，它用**图小波基**替代了图傅里叶基 [blog.csdn.net](https://blog.csdn.net/FengF2017/article/details/115253412)。图小波基是稀疏且局部化的，无需昂贵的矩阵特征分解即可高效计算，从而使网络能够高效学习到局部化的图结构特征。
    **关键实验结论**：在半监督节点分类任务上，GWNN在Cora、Citeseer等数据集上的性能超越了当时主流的谱域GCN方法，同时大幅提升了计算效率，验证了小波理论在非欧空间数据上的应用价值。

#### **3. 实验与评价总结**

综合上述代表性工作，基于小波的神经网络架构在多个方面展现出共同的优势：

1.  **性能与效率的协同提升**：通过将输入分解到小波域，模型可以在不显著增加参数和计算量的前提下，有效扩大感受野。如WTConv以对数级参数增长实现了全局感受野，GWNN将谱域GNN的计算复杂度从$O(N^3)$降低，这些工作均在提升模型性能的同时保证了计算效率。

2.  **增强的多尺度特征表征**：小波变换天然的多分辨率特性使网络能够并行处理不同频率的特征。例如，WavEnhancer分离处理低频（全局）和高频（细节）信息；WTMSA则通过分解与融合不同频带，更全面地捕捉高光谱数据的复杂模式。这种机制赋予了模型更强的多尺度表征能力。

3.  **改善模型偏置与可解释性**：传统CNN倾向于学习高频纹理信息。引入小波分解后，网络可以更明确地处理低频分量，从而增强了对物体形状、轮廓等全局结构的感知，即**形状偏置（shape bias）** [blog.csdn.net](https://blog.csdn.net/lichlee/article/details/142910207)。这种分频处理的范式也为理解模型行为提供了更清晰的视角。

4.  **提升鲁棒性**：对信号进行小波分解和重构的过程本质上具有去噪和平滑作用。实验表明，WTConv对图像损坏具有更强的鲁棒性，而用于信号识别的SENet通过小波去噪卷积提升了在复杂通信环境下的稳定性。

#### **4. 趋势与挑战**

基于2022-2025年的研究进展，未来基于小波的神经网络架构可能沿着以下方向发展：

1.  **可学习与自适应小波基**：目前多数工作（如WTConv）采用如哈尔小波等固定的、预定义的小波基。未来的研究将更多地关注**可学习的小波变换（Learnable Wavelet Transform）**，即让小波滤波器的参数成为网络的一部分，通过端到端的训练自适应地学习最适合特定任务和数据分布的变换基。这能进一步提升模型的灵活性和表征能力。

2.  **与主流架构的更深度、结构化融合**：当前融合模式多为替换现有模块（如用DWT替代池化）或作为“即插即用”的模块 [blog.csdn.net](https://blog.csdn.net/Angelina_Jolie/article/details/143475450)。未来的趋势是设计更深度的、结构化的融合方式，例如，在Transformer的注意力机制中引入小波域的距离度量，或构建在小波域内进行信息传递的层次化网络，实现经典信号处理理论与深度学习结构的原理性统一。

3.  **向更多模态和跨领域应用拓展**：小波分析的普适性使其非常适合应用于更多样的数据模态。除了已探索的图像、图、通信信号和高光谱数据，未来将在**视频处理**（时空多尺度分析）、**三维点云**（几何多分辨率表征）以及**生物医学信号**（如EEG/ECG）等领域看到更多创新的小波神经网络架构。

同时，该领域也面临挑战，主要在于**模型设计的复杂性**。如何设计最优的小波分解层数、选择何种小波族、以及如何有效融合不同频带的特征，这些超参数和结构选择往往依赖于经验和大量实验，缺乏统一的理论指导。

#### **5. 结论**

将小波变换与深度神经网络架构相结合，已成为提升模型性能和效率的一个重要研究方向。在2022-2025年间，以WTConv、WavEnhancer和WTMSA等为代表的研究工作，验证了这一融合范式在计算机视觉、信号处理等多个领域的有效性。这些方法通过利用小波的多分辨率分析能力，成功地在扩大感受野、提升计算效率、增强多尺度特征表征和模型鲁棒性之间取得了更好的平衡。展望未来，可学习小波基和与主流架构的深度融合将是关键的研究趋势。这一结合了经典信号处理理论与现代深度学习的跨学科方向，为构建下一代高效、鲁棒且可解释的人工智能模型提供了充满前景的路径。

#### **6. 参考文献**

[1] Finder, S. E., Amoyal, R., Treister, E., & Freifeld, O. (2024). *Wavelet Convolutions for Large Receptive Fields*. In Proceedings of the European Conference on Computer Vision (ECCV). [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/38389)

[2] lichlee. (2024). *WTConv：小参数大感受野，基于小波变换的新型卷积 | ECCV‘24*. CSDN Blog. [blog.csdn.net](https://blog.csdn.net/lichlee/article/details/142910207)

[3] Cheng, L., Yuan, H., Li, Z., & Jia, X. (2024). *Remote Sensing Image Denoising Based On Multi-Level Wavelet CNN with Attention Mechanism*. Computer Science and Application, 14(04), 73-82. [image.hanspub.org](https://image.hanspub.org/Html/9-1543124_84547.htm)

[4] Li, Z. N., Chen, X. H., Guo, S. N., Wang, S. Q., & Pun, C. M. (2024). *WavEnhancer: Unifying Wavelet and Transformer for Image Enhancement*. Journal of Computer Science and Technology. [jcst.ict.ac.cn](https://jcst.ict.ac.cn/cn/article/doi/10.1007/s11390-024-3414-z)

[5] Zheng, Q., Liu, F., Yu, L., Jiang, W., Huang, C., & Gui, G. (2025). *A Modulation Recognition Method Combining Wavelet Denoising Convolution and Sparse Transformer*. Journal of Electronics & Information Technology. [jeit.ac.cn](https://jeit.ac.cn/cn/article/doi/10.11999/JEIT241159?viewType=HTML)

[6] Yi, S., & Jiao, L. (2025). *Hyperspectral Image Classification Model Based on Wavelet Transform and Multi-Scale Attention*. Journal of Image and Signal Processing, 14(2), 149-161. [pdf.hanspub.org](https://pdf.hanspub.org/jisp2025142_52670413.pdf)

[7] Xu, B., Shen, H., Cao, K., & Li, H. (2019). *Graph Wavelet Neural Network*. In International Conference on Learning Representations (ICLR). [blog.csdn.net](https://blog.csdn.net/FengF2017/article/details/115253412)

[8] Angelina_Jolie. (2024). *（ECCV 2024）即插即用小波变换卷积，引入频域信息，涨点起飞*. CSDN Blog. [blog.csdn.net](https://blog.csdn.net/Angelina_Jolie/article/details/143475450)

[9] Xy-unu. (2024). *_Wavelet Convolutions for Large Receptive Fields_*. CSDN Blog. [blog.csdn.net](https://blog.csdn.net/weixin_45863274/article/details/141347142)

[10] Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., ... & Polosukhin, I. (2017). *Attention is all you need*. In Advances in neural information processing systems.

[11] He, K., Zhang, X., Ren, S., & Sun, J. (2016). *Deep residual learning for image recognition*. In Proceedings of the IEEE conference on computer vision and pattern recognition.

[12] Dosovitskiy, A., Beyer, L., Kolesnikov, A., Weissenborn, D., Zhai, X., Unterthiner, T., ... & Houlsby, N. (2020). *An image is worth 16x16 words: Transformers for image recognition at scale*. arXiv preprint arXiv:2010.11929.