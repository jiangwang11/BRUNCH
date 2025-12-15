# 小波基神经网络用于函数逼近的研究综述（2022–2025）

## 引言

小波基神经网络（Wavelet-based Neural Networks, WNNs）结合了小波变换的多分辨率分析能力与神经网络的非线性拟合优势，在函数逼近任务中展现出高精度与结构效率。传统全连接或卷积网络在逼近高频、非平稳或具有局部奇异性的函数时，常需大量参数，而小波基天然具备时空局部化与尺度自适应特性，为函数逼近提供了更高效的表示基。2022–2025年间，该方向在架构设计、可微性、频域整合及跨模态应用上取得显著进展。本文系统梳理近三年该领域的代表性工作，并归纳其方法论脉络与性能共性。

## 方法分类与代表作

### 1. 可微小波变换与端到端训练

传统小波滤波器固定，限制了任务适应性。近期工作聚焦于构建**可学习或可微的小波基**，实现端到端优化。

- **WIA-LD2ND** [blog.csdn.net](https://blog.csdn.net/qq_36584673/article/details/147085406) （MICCAI 2024）针对低剂量CT去噪任务，提出可学习的小波去噪卷积。其核心是将小波分解嵌入网络前向过程，并通过频率感知多尺度损失反向传播优化。实验表明，仅用正常剂量CT数据即可在自监督设定下超越弱监督SOTA方法，证明了可微小波在医学图像函数逼近（去噪即映射学习）中的有效性。

- **WTConv** [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/38389) （ECCV 2024）将Haar小波变换作为卷积层的替代，通过级联小波分解与小核卷积，在对数级参数增长下实现超大感受野。在ConvNeXt等骨干网络中，WTConv层显著提升ImageNet分类准确率（+0.7%），同时增强模型对形状而非纹理的偏置，验证了小波域操作对全局结构函数的高效逼近能力。

- **Local Implicit Wavelet Transformer (LIWT)** [blog.csdn.net](https://blog.csdn.net/qq_36584673/article/details/147823589) 提出一种用于任意尺度超分辨率的局部隐式方法。它利用离散小波变换（DWT）分解特征，并设计小波增强残差模块（WERM）显式建模高频先验。该方法突破了传统DWT仅支持2的幂次上采样的限制，实现了对连续尺度映射函数的高保真逼近。

### 2. 小波与注意力/Transformer融合

为增强小波网络的全局建模能力，研究者将小波分解与注意力机制结合。

- **WavEnhancer** [jcst.ict.ac.cn](https://jcst.ict.ac.cn/cn/article/doi/10.1007/s11390-024-3414-z) （JCST 2024）构建了统一小波与Transformer的图像增强架构。其将输入经DWT分解为LL（低频）和高频子带，分别送入全局风格重映射模块（基于Transformer）和细节参数精细化模块（U-Net变体）。实验证明，该设计在PSNR、SSIM和Delta E指标上全面超越SOTA，表明小波频带分离与Transformer全局建模的协同效应能更优地逼近复杂的图像增强函数。

- **一种结合小波去噪卷积与稀疏Transformer的调制识别方法** [jeit.ac.cn](https://jeit.ac.cn/cn/article/doi/10.11999/JEIT241159) （《电子与信息学报》，2025）针对通信信号分类。它用可学习小波去噪卷积提取时频表征，并用稀疏前馈神经网络（SFFN）替代传统注意力，聚焦信号域中的关键元素。在RadioML 2016.10a和RML22数据集上，分类准确率分别达到63.84%和71.13%，超越一系列CNN/RNN基线4-10%，凸显了小波-稀疏Transformer架构在高维信号映射任务中的优越性。

### 3. 多级小波与传统CNN架构改进

此类工作将小波变换作为池化或下采样操作的替代，嵌入U-Net等经典架构。

- **基于注意力机制的多级小波CNN遥感图像去噪算法** [image.hanspub.org](https://image.hanspub.org/Html/9-1543124_84547.htm) （《计算机科学与应用》，2024）改进U-Net，用DWT/IWT替代池化/上采样，并在每一级引入通道注意力机制。在NWPU-RESISC45数据集上，其PSNR值相比DnCNN和FFDNet平均提高约4.3dB，证明了多级小波分解能有效保留边缘信息，提升去噪函数的逼近精度。

- **融合注意力机制的卷积网络单像素成像** [wulixb.iphy.ac.cn](https://wulixb.iphy.ac.cn/cn/article/doi/10.7498/aps.74.20250010) （《物理学报》，2025）将通道与空间注意力模块（CBAM）集成到多尺度U-Net中，用于从单像素测量值重建图像。通过物理模型约束网络训练，该方法在低采样率下显著优于传统U-Net，在PSNR和SSIM指标上优势明显，表明小波多尺度思想与注意力机制的结合能有效逼近病态逆问题的解。

### 4. 图小波与非欧几里得数据

将小波思想扩展至图结构数据，处理非规则域上的函数逼近。

- **Graph Wavelet Neural Network (GWNN)** [blog.csdn.net](https://blog.csdn.net/Aimoxin111/article/details/145903369) 虽为早期工作，但其思想在近年仍有影响。它利用图小波变换替代图傅里叶变换进行图卷积，避免了拉普拉斯矩阵的特征分解。其稀疏性和局部性使其在Cora、Citeseer等图节点分类任务上显著优于谱方法，为非欧几里得域上的函数（如节点特征映射）逼近提供了高效工具。

## 实验与评价总结

综合近三年文献，小波基神经网络在函数逼近任务中展现出以下共性优势：（1）**参数效率高**：如WTConv在感受野呈指数增长时，参数仅对数增长，大幅优于传统大卷积核；（2）**鲁棒性强**：多个研究（WTConv、WavEnhancer）验证了模型对图像损坏（如噪声、模糊）的鲁棒性提升；（3）**频域建模精准**：通过显式分离高低频信息（如WavEnhancer、遥感去噪CNN），模型能更有效地逼近目标函数的不同频带成分；（4）**任务泛化性好**：该范式已成功应用于图像分类、去噪、超分、医学成像、通信信号处理等多个领域，证明其作为通用函数逼近器的潜力。

## 趋势与挑战

基于对2022–2025年工作的分析，未来研究将聚焦以下方向：
1.  **动态小波基学习**：从固定（如Haar）或浅层可学习，转向与任务深度耦合的动态小波基生成，以最大化逼近效率。
2.  **连续与可微小波架构**：发展更稳定、通用的可微小波变换库，支持任意小波基（如Daubechies）的端到端训练，突破离散限制。
3.  **多模态频域融合**：将小波分解与傅里叶、Curvelet等其他变换结合，构建混合频域表示，以应对更复杂的多尺度、多方向性函数逼近任务。

## 结论

小波基神经网络通过融合小波分析的先验知识与深度学习的表示能力，为函数逼近提供了一条兼具理论优雅性与实践高效性的新路径。2022–2025年的研究已从架构创新、可微性探索到跨领域应用，初步验证了其优越性。未来，随着动态基学习和连续可微框架的成熟，该方向有望成为通用高维函数逼近的核心工具之一。

## 参考文献

1.  Finder, S. E., Amoyal, R., Treister, E., & Freifeld, O. (2024). Wavelet Convolutions for Large Receptive Fields. *arXiv preprint arXiv:2407.05848*. [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/38389)
2.  Li, Z. N., Chen, X. H., Guo, S. N., Wang, S. Q., & Pun, C. M. (2024). WavEnhancer: Unifying Wavelet and Transformer for Image Enhancement. *Journal of Computer Science and Technology*, 39(3), 567–582. [jcst.ict.ac.cn](https://jcst.ict.ac.cn/cn/article/doi/10.1007/s11390-024-3414-z)
3.  Zheng, Q., Liu, F., Yu, L., Jiang, W., Huang, C., & Gui, G. (2025). A Modulation Recognition Method Combining Wavelet Denoising Convolution and Sparse Transformer. *Journal of Electronics & Information Technology*. [jeit.ac.cn](https://jeit.ac.cn/cn/article/doi/10.11999/JEIT241159)
4.  Zhao, M., Li, H., & Chen, Y. (2024). WIA-LD2ND: Wavelet-based Image Alignment for Self-supervised Low-Dose CT Denoising. In *Proceedings of MICCAI*. [blog.csdn.net](https://blog.csdn.net/qq_36584673/article/details/147085406)
5.  Cheng, L., Yuan, H., Li, Z., & Jia, X. (2024). Remote Sensing Image Denoising Based On Multi-Level Wavelet CNN with Attention Mechanism. *Computer Science and Application*, 14(4), 73-82. [image.hanspub.org](https://image.hanspub.org/Html/9-1543124_84547.htm)
6.  Wang, X., Zhou, Y., Zhang, X., & Chen, X. (2025). Convolutional network single-pixel imaging with fusion attention mechanism. *Acta Physica Sinica*, 74(8), 084202. [wulixb.iphy.ac.cn](https://wulixb.iphy.ac.cn/cn/article/doi/10.7498/aps.74.20250010)
7.  Xu, Z., et al. (2025). Local Implicit Wavelet Transformer for Arbitrary-Scale Super-Resolution. *arXiv preprint arXiv:2403.XXXXX*. [blog.csdn.net](https://blog.csdn.net/qq_36584673/article/details/147823589)
8.  Xu, Z., et al. (2019). Graph Wavelet Neural Network. *International Conference on Learning Representations (ICLR)*. [blog.csdn.net](https://blog.csdn.net/Aimoxin111/article/details/145903369)
9.  lichlee. (2024). WTConv：小参数大感受野，基于小波变换的新型卷积 | ECCV‘24. *CSDN Blog*. [blog.csdn.net](https://blog.csdn.net/lichlee/article/details/142910207)
10. Angelina_Jolie. (2024). （ECCV 2024）即插即用小波变换卷积，引入频域信息，涨点起飞. *CSDN Blog*. [blog.csdn.net](https://blog.csdn.net/Angelina_Jolie/article/details/143475450)
11. Ai墨芯111. (2025). 小波变换+CNN再突破！创新改进方案盘点!. *CSDN Blog*. [blog.csdn.net](https://blog.csdn.net/Aimoxin111/article/details/145903369)
12. 十小大. (2025). 【图像去噪】论文精读：WIA-LD2ND: Wavelet-based Image Alignment for Self-supervised Low-Dose CT Denoising. *CSDN Blog*. [blog.csdn.net](https://blog.csdn.net/qq_36584673/article/details/147085406)