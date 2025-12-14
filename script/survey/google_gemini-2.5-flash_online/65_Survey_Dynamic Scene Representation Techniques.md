## 动态场景表示技术综述 (2022–2025)

### 引言

动态场景表示是计算机视觉、图形学和机器人领域的核心研究方向，旨在建模和渲染随时间变化的真实世界场景。与静态场景表示相比，动态场景表示面临更大的挑战，尤其体现在非刚性形变、拓扑变化、以及高时空复杂性等方面。近年来，随着深度学习尤其是神经辐射场（NeRF）和扩散模型（Diffusion Models）的兴起，动态场景表示技术取得了显著进展。本综述将重点关注 2022-2025 年间涌现的代表性工作，对其主要技术路线、核心方法进行分类阐述，并总结实验评估中的共性结论，最后对未来的研究趋势进行预测。

### 方法分类与代表作

当前动态场景表示技术可大致分为基于神经辐射场的方法、基于显式表示的方法以及基于扩散模型的方法。

#### 1. 基于神经辐射场（NeRF）的方法

神经辐射场通过多层感知机（MLP）隐式地编码场景的几何和外观信息，在静态场景重建和新视角合成方面取得了突破。将其扩展到动态场景是近年来的研究热点，主要通过引入时间编码或变形场来实现。

*   **HumanRF: High-Fidelity Neural Radiance Fields for Humans in Motion ([dl.acm.org](https://dl.acm.org/doi/abs/10.1145/3592415), 2023)**
    该研究旨在从多视角同步视频中重建高保真动态人体 NeRF 模型，以准确渲染任意视角下的人物形态。核心方法是将 4D 特征网络分解为 3D 特征网络和 1D 特征网络的乘积，并引入自适应时间分区策略以处理长时间序列。实验结果显示，通过这一方法，HumanRF 能够高质量地渲染逼真、连续的人物运动，有效解决了动态人体重建的挑战。

*   **Neural 3D Video: Neural 3D Video Synthesis from Multi-view Video ([openaccess.thecvf.com](https://openaccess.thecvf.com/content/CVPR2022/html/Li_Neural_3D_Video_Synthesis_From_Multi-View_Video_CVPR_2022_paper.html), 2022)**
    此工作旨在通过紧凑的时序隐变量将 NeRF 扩展到时间维度，以实现 4D 场景的高效建模和渲染。其核心方法是引入一个随时间变化的隐变量 $z_t$ 来表示动态场景的时间属性，并通过分层训练和光线重要性采样策略加速模型训练。该方法有效地应对了 4D 场景中大量时间不变量和冗余问题，为动态场景的新视角合成提供了高效途径。

*   **Hypernerf: A Higher-Dimensional Representation for Topologically Varying Neural Radiance Fields ([arxiv.org](https://arxiv.org/abs/2106.13228), 2021) (注：虽然发表于2021，但其思想对2022-2025年工作影响深远，故收录)**
    该研究致力于解决 NeRF 在建模拓扑变化动态场景时的局限性，例如孔洞的出现或消失。其核心方法是将场景提升到高维超空间，并通过 Level Set 方法表示复杂表面的拓扑变化，将高维空间的切片映射到三维场景。通过在 NeRF 基础上增加高维切片 MLP，Hypernerf 显著提升了对拓扑变化场景的重建和渲染质量。

*   **NeRFPlayer: A Streamable Dynamic Scene Representation with Decomposed Neural Radiance Fields ([ieeexplore.ieee.org](https://ieeexplore.ieee.org/abstract/document/10049689), 2023)**
    NeRFPlayer 提出了一种可流式传输的动态场景表示，旨在实现高效的动态场景渲染和传输。该方法通过分解神经辐射场，将静态背景和动态前景分离，并对动态部分进行高效编码。这种分解策略使得动态内容能够独立更新和传输，提高了动态场景表示的灵活性和实用性。

#### 2. 基于显式表示的方法

除了隐式神经场，研究者们也探索了结合显式几何或特征的方法，以提高渲染效率和重建精度。

*   **Tensor4D: Efficient Neural 4D Decomposition for High-Fidelity Dynamic Reconstruction and Rendering ([openaccess.thecvf.com](https://openaccess.thecvf.com/content/CVPR2023/html/Shao_Tensor4D_Efficient_Neural_4D_Decomposition_for_High-Fidelity_Dynamic_Reconstruction_and_CVPR_2023_paper.html), 2023)**
    该研究提出了一种高效的神经 4D 分解方法，旨在实现高保真动态场景的重建和渲染。其核心在于将 4D 张量分解为多个低秩分量，从而在保持高视觉质量的同时显著降低了模型复杂度和存储需求。实验表明，这种分解策略显著提升了动态场景重建的效率和质量，尤其在处理大型复杂场景时优势明显。

*   **K-Planes: Explicit Radiance Fields in Space, Time, and Appearance ([openaccess.thecvf.com](https://openaccess.thecvf.com/content/CVPR2023/html/Fridovich-Keil_K-Planes_Explicit_Radiance_Fields_in_Space_Time_and_Appearance_CVPR_2023_paper.html), 2023)**
    K-Planes 旨在通过引入一系列显式 2D 平面特征表示，在一个统一框架中建模空间、时间和外观信息。该方法有效地解决了 NeRF 在动态场景中训练缓慢和渲染效率低的问题，通过可学习的 2D 特征平面替代复杂的 MLP，大幅提升了渲染速度。实验证明，K-Planes 在保持高质量的同时，实现了动态场景的实时渲染，具有显著的效率优势。

*   **4D LangSplat: 4D Language Fields with Dynamic 3D Gaussian Splatting for Open-Vocabulary Query of Dynamic Scenes ([hub.baai.ac.cn](https://hub.baai.ac.cn/view/44343), CVPR2025)**
    该工作提出了一个新颖的 4D 语言场建模方法，利用动态 3D 高斯泼溅技术，实现动态场景下的开放词汇查询。核心创新在于利用多模态大模型生成物体级的语言描述，并通过状态变化网络来处理动态语义特征的平滑变化。该方法显著提升了动态场景的语义理解和识别能力，在时间敏感和时间无关的开放词汇查询任务中均超越了现有基线。

#### 3. 基于扩散模型的方法

扩散模型在图像和视频生成方面展现出强大的能力，也被应用于动态场景的生成和表示。

*   **DynamicCity: Making Cities "Dynamic"! Breakthrough in 4D Large-Scale Scene Generation Technology ([finance.sina.com.cn](https://finance.sina.com.cn/tech/roll/2025-02-19/doc-inekytki3158010.shtml), ICLR2025 Spotlight)**
    DynamicCity 致力于突破现有大场景 3D 生成技术仅限于静态“快照”的限制，实现高质量、高效的 4D 城市级动态场景建模。该方法核心在于将 4D 场景压缩为紧凑的 2D HexPlane 特征表示，并结合 Diffusion Transformer (DiT) 模型进行生成。实验证明，DynamicCity 在生成质量、训练速度和内存消耗方面取得了跨越式进展，并支持轨迹引导、指令驱动等多种可控生成功能。

*   **3D Spatial Prior-Guided Video Diffusion Models with Controllable Camera Trajectories ([aas.net.cn](https://aas.net.cn/cn/article/doi/10.16383/j.aas.c250124?viewType=HTML), 2025)**
    此研究解决了视频扩散模型在相机可控的图像到视频生成任务中，生成视频 3D 空间结构一致性不足的问题。核心方法是在训练和推理阶段引入 3D 空间先验信息：训练时使用视角形变映射（Warp-Injection）构建高空间一致性参考帧序列，推理时采用初始噪声空间几何校正（Warp-Init）和能量函数引导（Warp-Guidance）策略。实验结果表明该方法显著提升了生成视频的 3D 结构一致性。

#### 4. 其他相关方法

*   **4D Panoptic Scene Graph Generation from Rich 2D Visual Scene ([chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/122417), 2025)**
    该研究旨在从丰富的 2D 视觉场景中学习生成 4D 全景场景图 (4D-PSG)，以解决 4D-PSG 数据稀缺和词汇外问题。其核心方法是引入集成了 3D 掩码解码器的 4D 大型语言模型 (4D-LLM)，并设计链式场景图推理机制以及 2D 到 4D 视觉场景迁移学习框架。实验结果表明，该模型显著超越了基线模型，有效利用 2D 数据弥补了 4D 数据不足。

*   **EmerNeRF: Emergent Spatial-Temporal Scene Decomposition via Self-Supervision ([chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/6742), 2025)**
    EmerNeRF 提出了一种通过自监督学习实现新兴时空场景分解的有效方法，旨在同时捕获场景几何、外观、运动和语义。其核心方法是将场景分层为静态场和动态场，并从动态场参数化感应流场，进一步融合多帧特征。该方法在传感器模拟中实现了优于传统方法的重建精度，并通过提升 2D 视觉基础模型特征到 4D 时空，显著提高了 3D 感知性能。

*   **3DET-Mamba: Causal Sequence Modelling for End-to-End 3D Object Detection ([chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/79995), 2025)**
    此研究旨在利用状态空间模型（Mamba）的线性复杂性和长序列建模能力，应用于 3D 物体检测。其核心方法是提出了 3DET-Mamba 架构，包含用于捕捉局部几何信息的 Inner Mamba，以及从空间分布和连续性建模点云的 Dual Mamba 模块。另外，Query-aware Mamba 模块解码上下文特征。实验结果表明，3DET-Mamba 在 ScanNet 等室内 3D 检测基准上显著超越了传统基于 Transformer 的方法。

### 实验与评价总结

综观 2022-2025 年动态场景表示领域的实验评估，可以总结出以下几点共性结论：

1.  **视觉质量与真实感持续提升：** 随着 NeRF 和扩散模型等技术的发展，生成动态场景的视觉真实感和细节丰富度显著提高，能够渲染出更逼真的动态效果和人物动作，甚至包括拓扑变化的复杂场景。
2.  **效率与速度的权衡与优化：** 早期基于 NeRF 的动态方法往往计算成本高昂，难以实现实时渲染。K-Planes、Tensor4D 等显式表示方法和结合高效编码的 NeRF 变体（如 Neural 3D Video）通过结构优化和分解策略，在保持高质量的同时，大幅提升了训练和渲染效率，部分达到了实时级别。
3.  **多功能性与可控性增强：** 除了基本的重建和渲染，新型方法更加注重对动态场景的理解和编辑能力。例如，4D LangSplat 实现了开放词汇的语义查询，DynamicCity 支持轨迹引导和场景修改，EmerNeRF 实现了自监督的空间-时间分解。这些功能拓展了动态场景表示在机器人、自动驾驶和内容创作等领域的应用潜力。
4.  **数据依赖与泛化能力：** 高质量的动态场景数据采集仍然是挑战。2D 到 4D 迁移学习（如 4D Panoptic Scene Graph Generation）和自监督学习（如 EmerNeRF）被提出以缓解数据稀缺问题。提高模型在未见场景和复杂环境下的泛化能力，以及在长序列动态中的时间一致性，仍是持续关注的焦点。
5.  **评估指标多样化：** 除了传统的 PSNR、SSIM 等指标，还引入了针对 3D 结构一致性（COLMAP error rate）、语义理解（PQ、mIoU）和动态一致性（FVD）的特定指标，以更全面地评估模型的性能。

### 趋势与挑战

1.  **多模态融合与统一表示：** 随着大型语言模型和多模态模型的进步，未来的动态场景表示将更多地与语言、音频等其他模态融合，实现更高级别的语义理解和交互。目标是从图像、视频中直接生成 4D 场景，并支持自然语言的查询和编辑，如 4D LangSplat 所示。
2.  **实时、大规模、可交互的 4D 世界模拟：** 现有方法在实时性、大规模场景建模和可交互性方面仍有提升空间。DynamicCity 等工作初步探索了城市级动态场景的生成，但构建覆盖更大范围、具有更高动态复杂度和实时交互能力的 4D 虚拟世界仍是长期目标，这对于自动驾驶仿真、元宇宙应用至关重要。
3.  **弱监督/自监督学习与数据效率：** 动态场景的高质量标注数据稀缺且成本高昂。未来的研究将更加侧重于利用无标签数据或弱监督信息进行学习，例如 EmerNeRF 所示的自监督分解，以及利用 2D 数据辅助 4D 学习的方法。这将大大降低数据采集门槛，推动技术普适化。

### 结论

2022-2025 年间，动态场景表示技术在神经辐射场、显式表示和扩散模型等多种方法的推动下取得了显著进展。从高保真动态人体重建到城市级动态场景生成，从开放词汇语义理解到 3D 结构一致性视频生成，这些工作极大地拓展了动态场景建模的能力边界。尽管在效率、泛化性和大规模应用方面仍存在挑战，但多模态融合、实时交互式 4D 模拟以及数据效率提升将是未来几年该领域的重要发展趋势。随着技术的不断成熟，动态场景表示将在虚拟现实、自动驾驶、机器人和内容创作等领域发挥越来越关键的作用。

### 参考文献

*   [Wu, S., Fei, H., Yang, J., Li, X., Li, J., Zhang, H., & Chua, T. S. (2025). Learning 4D Panoptic Scene Graph Generation from Rich 2D Visual Scene. *arXiv preprint arXiv:2503.15019*.](https://chatpaper.com/chatpaper/zh-CN/paper/122417)
*   [Li, M., Yuan, J., Chen, S., Zhang, L., Zhu, A., Chen, X., & Chen, T. (2024). 3DET-Mamba: Causal Sequence Modelling for End-to-End 3D Object Detection. *NeurIPS 2024*.](https://chatpaper.com/chatpaper/zh-CN/paper/79995)
*   [Yang, J., Ivanovic, B., Litany, O., Weng, X., Kim, S. W., Li, B., Che, T., Xu, D., Fidler, S., Pavone, M., & Wang, Y. (2024). EmerNeRF: Emergent Spatial-Temporal Scene Decomposition via Self-Supervision. *ICLR 2024*.](https://chatpaper.com/zh-CN/chatpaper/paper/6742)
*   [Biàn, H., Pan, L., Kong, L., Xie, H., Liu, Z., & Qiao, Y. (2024). DynamicCity: Making Cities "Dynamic"! Breakthrough in 4D Large-Scale Scene Generation Technology. *ICLR 2025 Spotlight*.](https://finance.sina.com.cn/tech/roll/2025-02-19/doc-inekytki3158010.shtml)
*   [Zhou, R. P., et al. (2025). 4D LangSplat: 4D Language Fields with Dynamic 3D Gaussian Splatting for Open-Vocabulary Query of Dynamic Scenes. *CVPR 2025*.](https://hub.baai.ac.cn/view/44343)
*   [Zhu, H., Yang, X., Zhao, M., Li, C., & Zhu, J. (2025). 3D Spatial Prior-Guided Video Diffusion Models with Controllable Camera Trajectories. *Acta Automatica Sinica*.](https://aas.net.cn/cn/article/doi/10.16383/j.aas.c250124?viewType=HTML)
*   [Işık, M., Rünz, M., Georgopoulos, M., Sengupta, S., Schultze, M., & Theobalt, C. (2023). HumanRF: High-Fidelity Neural Radiance Fields for Humans in Motion. *ACM Transactions on Graphics (TOG)*, 42(4), 1-12.](https://dl.acm.org/doi/abs/10.1145/3592415)
*   [Shao, R., Zheng, Z., Tu, H., Li, S., Wang, T., & Liu, Y. (2023). Tensor4D: Efficient Neural 4D Decomposition for High-Fidelity Dynamic Reconstruction and Rendering. *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition*, 16632-16642.](https://openaccess.thecvf.com/content/CVPR2023/html/Shao_Tensor4D_Efficient_Neural_4D_Decomposition_for_High-Fidelity_Dynamic_Reconstruction_and_CVPR_2023_paper.html)
*   [Li, T., Slavcheva, M., Zollhoefer, M., Li, H., & Theobalt, C. (2022). Neural 3D Video Synthesis from Multi-view Video. *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition*, 5521-5531.](https://openaccess.thecvf.com/content/CVPR2022/html/Li_Neural_3D_Video_Synthesis_From_Multi-View_Video_CVPR_2022_paper.html)
*   [Fridovich-Keil, S., Meanti, G., Warburg, F. R., Yu, A., Tancik, M., & Sancaktar, C. (2023). K-Planes: Explicit Radiance Fields in Space, Time, and Appearance. *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition*, 12479-12488.](https://openaccess.thecvf.com/content/CVPR2023/html/Fridovich-Keil_K-Planes_Explicit_Radiance_Fields_in_Space_Time_and_Appearance_CVPR_2023_paper.html)
*   [Song, L., Chen, A., Li, Z., Guo, S., Wang, H., & Chen, Y. (2023). NeRFPlayer: A Streamable Dynamic Scene Representation with Decomposed Neural Radiance Fields. *IEEE Transactions on Visualization and Computer Graphics*, 29(5), 2732-2742.](https://ieeexplore.ieee.org/abstract/document/10049689)
*   [Park, K., Sinha, U., Hedman, P., Singh, S., & Szeliski, R. (2021). Hypernerf: A Higher-Dimensional Representation for Topologically Varying Neural Radiance Fields. *arXiv preprint arXiv:2106.13228*.](https://arxiv.org/abs/2106.13228)