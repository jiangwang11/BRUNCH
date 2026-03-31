好的，遵照您的指示，我将基于提供的搜索结果生成一篇关于「Image Restoration via Kernel-Based Networks」的严谨中文学术综述。

---

### **图像复原中基于核的网络方法研究综述 (2022-2025)**

#### **引言**

图像复原（Image Restoration, IR）作为计算机视觉的基础任务之一，旨在从因噪声、模糊、压缩等因素导致的降质图像中重建高质量的清晰图像。该问题本质上是一个数学上的病态逆问题，其挑战在于如何在恢复图像细节与抑制伪影、噪声之间取得有效平衡 [www.opticsjournal.net](https://www.opticsjournal.net/Articles/OJ37a82ad7d27f60a/FullText)。早期方法依赖于手工设计的先验，如全变差（Total Variation）或稀疏性约束，而现代方法则通过深度学习，特别是基于“核”思想的神经网络，从大规模数据中学习隐式先验。

本文将“核”广义地定义为网络中用于特征提取与聚合的基本计算单元，其形式从传统的卷积核演变为自注意力（Self-Attention）中的相似性计算核，乃至状态空间模型（State-Space Model, SSM）中的状态转移核。本综述聚焦于 2022 至 2025 年间，基于这一广义核概念的图像复原网络架构的代表性研究，并展望未来的发展趋势与挑战 [www.cjig.cn](https://www.cjig.cn/zh/article/doi/10.11834/jig.240436/)。

#### **方法分类与代表作**

##### **1. Transformer及其高效变体**

Transformer通过自注意力机制实现了全局感受野，但其应用于高分辨率图像时面临二次方计算复杂度的瓶颈。近期研究致力于设计高效的Transformer变体，在保持全局建模能力的同时降低计算开销。

*   **Restormer (CVPR 2022)**
    该研究旨在解决标准Transformer在高分辨率图像复原任务中计算成本过高的问题 [cloud.tencent.cn](https://cloud.tencent.cn/developer/article/2398294?policyId=1003)。其核心是提出了多Dconv头转置注意力（MDTA），该模块在通道维度而非空间维度计算自注意力，使计算复杂度与图像尺寸成线性关系。同时，门控Dconv前馈网络（GDFN）通过深度卷积和门控机制增强了特征变换能力。实验表明，Restormer在图像去雨、去运动模糊和去噪等16个基准测试中均取得了当时最优的性能，验证了通道注意力和局部上下文编码的有效性。

##### **2. 大卷积核CNN架构**

受Transformer全局建模能力的启发，研究者们重新审视并设计了采用极大卷积核的CNN架构，以期在纯卷积框架内模拟长距离依赖。

*   **OKNet (AAAI 2024)**
    该工作旨在借鉴Transformer的全局感知优势，同时规避其计算瓶颈，探索大核CNN在图像复原中的潜力 [blog.csdn.net](https://blog.csdn.net/a486259/article/details/142406557)。OKNet的核心是全核模块（OKM），它并行设计了三个分支：局部分支（1x1卷积）、大分支（采用高达63x63的深度卷积及条带卷积）和全局分支（利用双域通道注意和频率门控机制）。通过仅在网络瓶颈处嵌入OKM，该模型在降低计算量的同时捕获了多尺度感受野。在图像去模糊、去雨和去雾等11个基准数据集上，OKNet及其轻量版OKNet-S均达到了SOTA水平，例如在去雾任务上，OKNet-S的PSNR比Fourmer高出3.47 dB。

##### **3. CNN与Transformer混合架构**

为了融合CNN的局部特征提取能力和Transformer的全局上下文建模优势，混合架构应运而生，通过动态或静态的方式结合两种范式。

*   **ELF (JIG 2024)**
    该研究探讨了如何有效协调CNN的局部感知能力与自注意力（SA）的全局聚合能力，特别是在图像去雨任务中 [www.cjig.cn](https://www.cjig.cn/zh/article/doi/10.11834/jig.230323/)。ELF模型通过关联学习的思路，将降质（雨纹）去除和背景修复分解为两个子任务，并设计了一个多输入注意力模块（MAM）将两者联系起来。该架构包含一个残差Transformer分支和一个编解码器CNN分支，实现了并行处理与特征融合。实验结果显示，ELF在合成去雨数据集Test1200上，PSNR值比MPRNet高出0.9 dB，在水下和低照度图像增强任务上也表现出显著优势。

##### **4. 基于算法展开的可解释深度模型**

此类方法将传统优化算法（如半二次分裂法）的迭代步骤展开成一个深度网络，每个阶段对应一次迭代，从而使网络具备良好的数学可解释性。

*   **GBAUCNN (2023)**
    该研究旨在解决深度学习模型缺乏可解释性以及传统变分模型参数调节困难的问题 [image.hanspub.org](https://image.hanspub.org/Html/19-1542874_66383.htm)。模型基于半二次分裂（HQS）算法展开，将去噪器部分设计为具可学习参数的非线性反应扩散模型。其创新之处在于，采用Gabor基函数设计卷积核以替代DCT基，从而捕获更丰富的方向和尺度信息。在图像去噪任务中，于噪声水平为25和50时，该模型相比基于DCT的TNRD模型，PSNR值提升了0.7 dB。

*   **L2范数先验模型 (2025)**
    此研究针对传统正则化模型中先验信息不足和参数设置困难的问题，提出了一种可解释的深度学习复原网络 [www.opticsjournal.net](https://www.opticsjournal.net/Articles/OJ3c8a4a3f8eb7002f/Abstract)。该方法将经典的L2范数正则化模型与深度学习结合，通过一个非线性变换模块替代正则项，并利用深度网络优化求解。这种设计不仅提升了模型求解效率，也增强了网络的可解释性。实验证明，该算法能够有效去除模糊并抑制噪声，在提高图像质量上展现出结合传统与深度学习的优势。

##### **5. 新兴架构：状态空间模型与扩散模型**

近年来，状态空间模型（SSM）和扩散模型（DM）成为图像生成和复原领域的前沿方向，它们为平衡性能与效率提供了新的解决思路。

*   **MambaIR & MambaIRv2 (ECCV 2024 & arXiv 2024)**
    MambaIR旨在解决CNN和Transformer在全局感受野与计算效率之间的矛盾 [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/99851)。它将SSM（特别是Mamba）应用于图像复原，并通过引入局部增强和通道注意力来克服标准Mamba的局部像素遗忘问题。MambaIRv2则进一步解决了Mamba固有的因果建模限制 [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/85148)。它设计了“注意力状态空间方程”，使模型能够进行非因果建模，从而一次扫描即可捕获全局信息。实验显示，MambaIR在图像超分上比SwinIR提升0.45 dB，而MambaIRv2比HAT提升高达0.29 dB，同时计算成本更低。

*   **DiffIR (2023)**
    该工作针对标准扩散模型在图像复原任务中效率低下的问题，因为IR任务大部分像素是已知的，无需从头生成 [www.zhuanzhi.ai](https://www.zhuanzhi.ai/paper/246fe9068ef5a64044cb6d4fcbe1574a)。DiffIR提出了一种高效策略，其扩散过程不再估计整个图像，而是估计一个紧凑的IR先验表示（IPR）向量。这个低维向量指导一个Transformer网络（DIRformer）完成最终的图像重建，从而显著减少了迭代次数和计算成本。实验证明，DiffIR在多个IR任务上以更低的计算代价实现了SOTA性能。

#### **实验与评价总结**

综合2022–2025年的研究，可以总结出以下共性评价结论：

1.  **评价指标与数据集**：峰值信噪比（PSNR）和结构相似性（SSIM）仍然是衡量图像复原质量最通用的客观指标。实验通常在多个标准合成数据集（如RESIDE、DPDD、Set12、BSD68）和真实世界数据集上进行，以验证模型的泛化能力 [blog.csdn.net](https://blog.csdn.net/a486259/article/details/142406557)。

2.  **感受野与性能**：无论是大核CNN（OKNet）、高效Transformer（Restormer）还是SSM（MambaIR），都印证了扩大有效感受野（ERF）对提升复原性能至关重要。具备全局或近乎全局建模能力的模型，在处理非局部降质（如雨纹、大面积模糊）时表现出明显优势。

3.  **效率与架构**：计算效率是架构设计的核心驱动力之一。Restormer的通道注意力、MambaIR的线性复杂度扫描、OKNet的瓶颈模块设计以及DiffIR的先验扩散策略，都体现了在追求高性能的同时对计算成本的严格控制。

4.  **先验与可解释性**：将经典数学模型（如HQS、L2范数）与深度网络结合的“算法展开”方法（GBAUCNN），通过赋予网络明确的物理解释，在模型紧凑性和可解释性上展现了独特价值。这类方法证明了深度学习与传统先验知识的结合是提升性能和可信度的有效途径。

#### **趋势与挑战**

基于上述研究，2025年前后图像复原领域呈现出以下明确的研究趋势与挑战：

1.  **超越Transformer：状态空间模型的崛起**。以MambaIR/MambaIRv2为代表的研究表明，SSM作为一种新兴序列建模架构，有望成为Transformer的有效替代品。SSM在理论上具备全局感受野和随图像尺寸线性增长的计算复杂度，完美契合高分辨率图像复原的需求。未来的研究将进一步探索如何为二维图像数据设计更高效的SSM扫描策略和状态更新机制。

2.  **扩散模型的特化与高效化**。通用扩散模型在复原任务上的计算瓶颈促使研究转向特化设计。如DiffIR所示，未来的趋势是利用扩散模型生成紧凑的、任务相关的中间表示（如图像先验、降质参数）而非像素本身，以此作为“可控生成”的引导信号。这将极大提升扩散模型在图像复原领域的实用性和效率。

3.  **多模态信息融合与大模型先验注入**。随着视觉-语言大模型（VLM）的成熟，利用其强大的语义理解能力为图像复原提供高级先验成为可能 [www.cjig.cn](https://www.cjig.cn/zh/article/doi/10.11834/jig.240436/)。未来的复原网络或将接受文本描述作为额外输入，引导模型恢复出更符合语义逻辑和用户意图的细节（如“恢复图中模糊的文字”），或直接利用预训练大模型提取的特征作为正则化项，解决极端降质下的结构与纹理丢失问题。

#### **结论**

在2022至2025年间，面向图像复原的核基网络研究经历了从优化Transformer到探索大核CNN、混合架构、算法展开乃至拥抱SSM和扩散模型等新兴范式的快速演进。核心驱动力始终围绕着如何在扩大模型感受野、增强全局建模能力与控制计算复杂度之间寻求最佳平衡。代表性工作如Restormer、OKNet、MambaIRv2和DiffIR分别从不同角度给出了极具竞争力的解决方案。未来的研究将更加聚焦于架构效率（如SSM）、生成模型的任务特化以及借助多模态大模型先验，以应对更复杂和真实的图像降质场景。

#### **参考文献**

[1] 杨航. 非盲图像复原综述. 中国光学, 2022, 15(5): 954-971.
[2] Zamir S W, Arora A, Khan S, et al. Restormer: Efficient Transformer for High-Resolution Image Restoration. In: Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2022: 5728-5739.
[3] 孙璐, 魏伟波, 杨光宇, 等. 基于Gabor基算法展开卷积神经网络图像恢复模型. 计算机科学与应用, 2023, 13(05): 1119-1134.
[4] Xia B, Zhang Y, Wang S, et al. DiffIR: Efficient Diffusion Model for Image Restoration. arXiv preprint arXiv:2303.09472, 2023.
[5] Chen, et al. Omni-Kernel Network for Image Restoration. In: Proceedings of the AAAI Conference on Artificial Intelligence. 2024.
[6] 江奎, 贾雪梅, 黄文心, 等. 图像复原中自注意力和卷积的动态关联学习. 中国图象图形学报, 2024, 29(4): 890-907.
[7] Guo H, Li J, Dai T, et al. MambaIR: A Simple Baseline for Image Restoration with State-Space Model. In: Proceedings of the European Conference on Computer Vision. 2024.
[8] Guo H, Guo Y, Zha Y, et al. MambaIRv2: Attentive State Space Restoration. arXiv preprint arXiv:2411.15269, 2024.
[9] 卜丽静, 杨贝妮, 董国强, 等. L2范数先验的可解释性深度学习图像复原算法. 激光与光电子学进展, 2025, 62(6): 0637004.
[10] 韦炎炎, 毛天一, 李柏昂, 等. 视觉模型及多模态大模型推进图像复原增强研究进展. 中国图象图形学报, 2025, 30(5): 1197-1219.
[11] Zhang K, Zuo W, Gu S, et al. Learning deep CNN denoiser prior for image restoration. In: Proceedings of the IEEE conference on computer vision and pattern recognition. 2017: 3929-3938. (注：此篇为背景知识，由[www.opticsjournal.net](https://www.opticsjournal.net/Articles/OJ37a82ad7d27f60a/FullText)引用提及)
[12] Liang J, Cao J, Sun G, et al. Swinir: Image restoration using swin transformer. In: Proceedings of the IEEE/CVF international conference on computer vision. 2021: 1833-1844. (注：此篇为背景知识，由[chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/99851)引用提及)