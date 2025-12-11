好的，作为一名严谨的科研助手，我将基于提供的真实网络搜索结果，为您生成一篇关于“单目视觉系统动态场景重建技术”的中文学术综述。

***

### **面向单目视觉系统的动态场景重建技术研究综述 (2022-2025)**

#### **摘要**
单目动态场景重建旨在仅通过单视角视频序列恢复时变三维场景的几何与外观，是计算机视觉、增强现实与机器人技术中的核心挑战。近年来，随着神经表达（Neural Representation）技术的突破，该领域经历了从隐式神经辐射场（NeRF）到显式三维高斯泼溅（3DGS）的范式演进。本综述系统梳理了2022至2025年间基于神经表达的单目动态场景重建代表性工作，将其归纳为两大技术路线：基于神经辐射场的方法和基于三维高斯泼溅的方法。我们深入剖析了各类方法的关键思想与技术贡献，总结了主流的实验评估基准，并在此基础上分析了当前技术面临的核心挑战，最后对未来研究趋势进行了展望。

---

#### **1. 引言**

从单目视频中重建动态三维场景，因其固有的深度模糊性和运动复杂性，长期以来是计算机视觉领域的一大难题。传统方法，如基于多视角几何（MVS）和同时定位与建图（SLAM）的流程，通常在处理动态元素时面临困难，且计算成本高昂。自神经辐射场（NeRF）[<sup>[1]</sup>](#ref1)问世以来，使用神经网络隐式表达场景成为主流，动态场景重建也随之涌现出如D-NeRF等开创性工作 [[telecomsci.com](https://www.telecomsci.com/zh/article/doi/10.11959/j.issn.1000-0801.2025152/)]。

进入2022-2025年，研究热点进一步分化。一方面，基于NeRF的方法通过改进网络结构和时空分解策略，在效率和质量上不断优化。另一方面，三维高斯泼溅（3DGS）[<sup>[2]</sup>](#ref2)作为一种新兴的显式表达方式，凭借其出色的渲染质量和实时性能，被迅速应用于动态场景，并展现出超越NeRF的潜力 [[eet-china.com](https://www.eet-china.com/mp/a297533.html)]。本综述聚焦于此背景下两种主流技术路线的代表性研究，旨在为相关领域研究者提供清晰的技术脉络和前沿洞见。

#### **2. 方法分类与代表作**

基于神经表达的动态场景重建方法主要分为两大类：基于神经辐射场（NeRF）的隐式方法和基于三维高斯泼溅（3DGS）的显式方法。

##### **2.1 基于神经辐射场 (NeRF) 的方法**
这类方法将动态场景建模为一个连续的函数，通常由多层感知机（MLP）实现，将四维时空坐标（x, y, z, t）映射到体密度和颜色。早期的工作（如D-NeRF [[telecomsci.com](https://www.telecomsci.com/zh/article/doi/10.11959/j.issn.1000-0801.2025152/)]）通过一个变形网络将观测空间的点反向映射回一个规范空间，但这种“逆向流”（backward-flow）优化难度大，影响重建质量。近期研究致力于改进时空表达效率与场景分解能力。

*   **HexPlane (CVPR 2023)** [[telecomsci.com](https://www.telecomsci.com/zh/article/doi/10.11959/j.issn.1000-0801.2025152/)]
    *   **研究问题**: 如何在保持高质量渲染的同时，大幅提升动态神经辐射场的训练与渲染效率。
    *   **核心方法**: 提出一种高效的动态场景表示方法，将4D时空张量分解为六个2D特征平面（三个时空平面和三个空间平面）。通过对这六个平面进行特征采样和融合，来查询任意时空点的属性。
    *   **关键实验结论**: 该方法在保持与D-NeRF等方法相当渲染质量的同时，显著减少了模型参数量和训练时间，实现了更快的动态场景重建。

*   **EmerNeRF (ICLR 2024)** [[chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/6742)]
    *   **研究问题**: 如何在没有显式动态物体或运动标签的情况下，通过自监督方式学习动态场景的时空分解。
    *   **核心方法**: 提出一种自监督框架，将场景分层为独立的静态场和动态场。通过从动态场中参数化一个感应流场（induced flow field），并利用该流场聚合多帧特征，从而增强动态对象的渲染精度。
    *   **关键实验结论**: 在传感器模拟任务中，该方法在静态和动态场景的重建质量（PSNR）上均显著优于先前方法，证明了自监督分解策略的有效性。

*   **NeuralRecon (TPAMI 2024)** [[ablesci.com](https://www.ablesci.com/assist/detail?id=M4bNVM)]
    *   **研究问题**: 如何从单目视频中实现实时、连贯的稠密三维场景重建。
    *   **核心方法**: 采用一种基于学习的框架，设计了一个GRU（门控循环单元）融合模块，用于在统一的体素网格中逐步、高效地聚合来自连续视频帧的几何特征。该方法避免了传统方法中对多视图几何的显式依赖。
    *   **关键实验结论**: NeuralRecon能够在GPU上实现实时运行，并在ScanNet等数据集上生成比传统实时SLAM系统更完整、更准确的几何重建结果。

##### **2.2 基于三维高斯泼溅 (3DGS) 的方法**
这类方法使用一组离散的、可优化的三维高斯分布显式地表达场景。每个高斯具有位置、旋转、缩放、颜色和不透明度等属性。渲染过程通过高效的GPU光栅化（Splatting）完成，具有天然的速度优势。将3DGS应用于动态场景是当前的研究热点。

*   **Deformable 3D Gaussians (CVPR 2024)** [[eet-china.com](https://www.eet-china.com/mp/a297533.html)]
    *   **研究问题**: 如何将静态3DGS的高保真度和高效率优势拓展到单目动态场景重建中。
    *   **核心方法**: 首次将变形场（Deformation Field）与3DGS结合，在规范空间中定义一组3D高斯，并通过一个小型MLP预测每个高斯在不同时间戳的位置和形状参数。这种“前向流”（forward-flow）策略比NeRF的逆向映射更稳定。
    *   **关键实验结论**: 在D-NeRF合成数据集上，该方法相比以往最优方法实现了超过10个点的PSNR提升。同时，在消费级GPU上（如3090）可达到68 FPS（800x800分辨率）的实时渲染速度。

*   **4D Gaussian Splatting (CVPR 2024)** [[telecomsci.com](https://www.telecomsci.com/zh/article/doi/10.11959/j.issn.1000-0801.2025152/)]
    *   **研究问题**: 如何为一个完整的、非刚性的动态场景构建一个高效的、可实时渲染的四维表示。
    *   **核心方法**: 将每个3D高斯点的运动轨迹建模为一个紧凑的时间函数，例如使用一组基函数（如傅里叶级数或低秩分解）来表示。这使得模型能够在一个统一的优化框架内学习高斯点的静态属性和动态轨迹。
    *   **关键实验结论**: 该方法能够对复杂的动态场景（如多人交互）进行高质量建模，并实现前所未有的实时渲染性能，为自由视点视频生成提供了新的解决方案。

*   **Asymmetric Dual 3D Gaussian Splatting (arXiv, 2025)** [[chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/146190)]
    *   **研究问题**: 如何在充满光照不一致、瞬态物体等干扰的“野外”（in-the-wild）图像中实现鲁棒的神经渲染和3D重建。
    *   **核心方法**: 提出一种非对称双模型训练框架，并行训练两个3DGS模型。通过施加一致性约束来强化真实的场景结构，同时利用伪影的随机性来抑制它们。不对称性通过引入互补的掩码策略实现，防止两个模型陷入相似的错误模式。
    *   **关键实验结论**: 在具有挑战性的真实世界数据集上，该方法在重建质量上优于现有SOTA方法，同时保持了高效的训练速度，显著提升了模型在非理想数据下的鲁棒性。

#### **3. 实验与评价总结**

*   **数据集与评估指标**:
    *   **合成数据集**: D-NeRF数据集仍是评估动态场景重建质量的核心基准，包含具有复杂非刚性运动的物体。
    *   **真实数据集**: HyperNeRF和NeRF-DS等数据集提供了包含相机位姿不准、高光反射等真实挑战的场景 [[eet-china.com](https://www.eet-china.com/mp/a297533.html)]。此外，ScanNet++、Aria等大规模视频数据集也开始被用于训练更具泛化能力的大型模型 [[blog.csdn.net](https://blog.csdn.net/amusi1994/article/details/147818644)]。
    *   **评估指标**: 渲染质量通常使用峰值信噪比（PSNR）、结构相似性指数（SSIM）和学习感知图像块相似度（LPIPS）来衡量。几何重建质量则通过准确度（Accuracy）和完整度（Completeness）来评估。

*   **共性结论**:
    1.  **质量与效率的飞跃**: 3DGS-based方法（如Deformable 3D Gaussians）相较于NeRF-based方法在渲染质量和速度上取得了突破性进展。在D-NeRF等标准基准上，PSNR等指标的大幅提升（超过10个点）已成为常态 [[eet-china.com](https://www.eet-china.com/mp/a297533.html)]。
    2.  **实时渲染成为可能**: 由于采用高效的GPU光栅化管线，3DGS方法普遍能够实现动态场景的实时渲染（通常>30 FPS），这对于AR/VR等交互式应用至关重要。
    3.  **对相机位姿的敏感性**: 显式表达（如3DGS）相比平滑的隐式表达（如NeRF）对不准确的相机位姿更为敏感。因此，一些工作（如Deformable 3D Gaussians中的退火平滑训练）开始引入特定机制以缓解此问题 [[eet-china.com](https://www.eet-china.com/mp/a297533.html)]。

#### **4. 趋势与挑战**

基于2024-2025年的前沿工作，单目动态场景重建领域呈现以下主要趋势和挑战：

1.  **融合大模型与可扩展架构**: 以**SLAM3R (CVPR 2025)** [[blog.csdn.net](https://blog.csdn.net/amusi1994/article/details/147818644)]为代表的工作，正推动领域范式从“为每个场景单独优化”转向“使用大规模预训练模型进行前馈式重建”。SLAM3R通过在海量视频数据上训练，实现了从长视频中实时、高质量地重建稠密点云，而无需迭代优化。这一趋势表明，利用大模型的泛化能力处理开放世界场景将是未来的重要方向。

2.  **提升语义理解与场景分解能力**: 重建的未来不仅是几何和颜色，更是结构化的场景理解。**PanoSSC (2024)** [[chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/28582)]等工作开始探索在三维体素空间中进行全景分割（panoptic segmentation），即同时预测语义和实例信息。这种对前景物体和背景的精细化区分，对于自动驾驶和机器人交互等下游任务至关重要。类似地，EmerNeRF的自监督场分解也反映了这一趋势。

3.  **追求极端场景下的鲁棒性与实时性**: 随着技术走向实际应用，处理“野外”数据成为核心挑战。**Asymmetric Dual 3DGS (2025)**等研究专注于解决光照变化、运动模糊和临时遮挡物等问题。同时，**Zero-Shot Monocular Scene Flow Estimation (2025)** [[chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/101119)]的研究表明，更精准和泛化的运动（场景流）估计是处理复杂动态的基础。如何在消费级硬件上实现上述能力的实时化，仍是持续的挑战。

#### **5. 结论**

在2022至2025年间，面向单目视觉的动态场景重建技术取得了长足进步。研究范式经历了从基于NeRF的隐式优化到基于3DGS的显式、高效重建的重大转变。当前最优方法已能在保证高保真度的同时实现实时渲染。展望未来，该领域正朝着利用大模型实现更强泛化能力、融合语义信息以进行结构化理解、以及在复杂真实环境中实现更高鲁棒性的方向快速发展。这些技术突破将为构建下一代沉浸式数字世界和具身智能系统奠定坚实的基础。

#### **6. 参考文献**
<a name="ref1"></a>[1] Mildenhall, B., Srinivasan, P. P., Tancik, M., et al. (2020). NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis. In *ECCV*.
<a name="ref2"></a>[2] Kerbl, B., Kopanas, G., Leimkühler, T., & Drettakis, G. (2023). 3D Gaussian Splatting for Real-Time Radiance Field Rendering. *ACM Transactions on Graphics*.
<a name="ref3"></a>[3] Cao, A., & Johnson, J. (2023). HexPlane: A Fast Representation for Dynamic Scenes. In *CVPR*.
<a name="ref4"></a>[4] Yang, J., Ivanovic, B., Litany, O., et al. (2024). EmerNeRF: Emergent Spatial-Temporal Scene Decomposition via Self-Supervision. In *ICLR*.
<a name="ref5"></a>[5] Chen, X., Sun, J., Xie, Y., et al. (2024). NeuralRecon: Real-Time Coherent 3D Scene Reconstruction from Monocular Video. *IEEE Transactions on Pattern Analysis and Machine Intelligence*.
<a name="ref6"></a>[6] Yang, Z., Gao, X., Zhou, W., et al. (2024). Deformable 3D Gaussians for High-Fidelity Monocular Dynamic Scene Reconstruction. In *CVPR*.
<a name="ref7"></a>[7] Wu, G., Yi, T., Fang, J., et al. (2024). 4D Gaussian Splatting for Real-Time Dynamic Scene Rendering. In *CVPR*.
<a name="ref8"></a>[8] Li, C., Shi, Z., Lu, Y., et al. (2025). Robust Neural Rendering in the Wild with Asymmetric Dual 3D Gaussian Splatting. *arXiv preprint*.
<a name="ref9"></a>[9] Liu, Y., Dong, S., Wang, S., et al. (2025). SLAM3R: Real-Time Dense Scene Reconstruction from Monocular RGB Videos. In *CVPR*.
<a name="ref10"></a>[10] Shi, Y., Li, J., Jiang, K., et al. (2024). PanoSSC: Exploring Monocular Panoptic 3D Scene Reconstruction for Autonomous Driving. *arXiv preprint*.
<a name="ref11"></a>[11] Liang, Y., Badki, A., Su, H., et al. (2025). Zero-Shot Monocular Scene Flow Estimation in the Wild. *arXiv preprint*.
<a name="ref12"></a>[12] 陆平, 孙俊杰, 李婉等. (2025). 基于神经表达的动态场景重建综述. *电信科学*.
<a name="ref13"></a>[13] Pumarola, A., Corona, E., Pons-Moll, G., & Moreno-Noguer, F. (2021). D-NeRF: Neural Radiance Fields for Dynamic Scenes. In *CVPR*.
<a name="ref14"></a>[14] Huang, J., Artemov, A., Chen, Y., et al. (2024). SSR-2D: Semantic 3D Scene Reconstruction From 2D Images. *IEEE Transactions on Pattern Analysis and Machine Intelligence*.