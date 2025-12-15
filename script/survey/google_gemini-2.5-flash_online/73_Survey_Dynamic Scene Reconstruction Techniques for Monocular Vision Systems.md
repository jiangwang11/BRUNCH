## Dynamic Scene Reconstruction Techniques for Monocular Vision Systems (基于单目视觉系统的动态场景重建技术综述)

### 引言

动态场景重建是计算机视觉和机器人学领域的核心问题，旨在从图像或视频序列中恢复随时间变化的场景三维结构和运动。在自动驾驶、虚拟现实、增强现实和人机交互等应用中，从单个摄像机（单目视觉系统）中进行动态场景重建具有广泛的实用价值，但其固有挑战在于从二维图像中恢复三维深度信息以及在时间和空间维度上建模场景变化。随着深度学习和神经渲染技术的飞速发展，特别是以神经辐射场（NeRF）和三维高斯泼溅（3D Gaussian Splatting, 3DGS）为代表的新型神经表示的出现，单目动态场景重建技术在2022-2025年间取得了显著进展。本综述将聚焦于这一时期基于单目视觉系统的动态场景重建代表性工作，对其核心方法、关键结论进行分类总结，并展望未来的研究趋势。

### 方法分类与代表作

当前单目动态场景重建方法主要围绕神经辐射场和三维高斯泼溅两种核心神经表示展开，并结合变形场、SLMA范式或大模型先验来处理场景的时间动态和几何复杂性。

**1. 基于可变形神经辐射场（Deformable NeRFs）**

此类方法通常通过引入显式或隐式的变形场来建模场景随时间的运动，将观测到的动态场景映射到静态的规范空间中进行表示，从而实现高质量的动态渲染。

*   **Pumarola et al. (D-NeRF, CVPR 2021 [telecomsci.com](https://www.telecomsci.com/zh/article/doi/10.11959/j.issn.1000-0801.2025152/))**：该工作提出了D-NeRF，通过将时间编码作为神经辐射场的额外输入来模拟场景形变。它通过预测场景中每个点的三维位移来将其映射到规范空间，从而将动态场景建模为一个静态NeRF和一个变形场的组合。实验表明，D-NeRF在合成动态场景数据集上实现了高质量的新视角合成，验证了变形场在解耦几何和运动方面的有效性。

*   **Park et al. (Nerfies, ICCV 2021 [telecomsci.com](https://www.telecomsci.com/zh/article/doi/10.11959/j.issn.1000-0801.2025152/))**：Nerfies同样提出了可变形的神经辐射场，但其侧重于处理非刚性变形，例如面部表情变化。它通过一个基于局部形变的嵌入空间来捕捉精细的形变，使得在非刚性场景中也能进行高保真渲染。结果显示，该方法能够有效地重建和渲染具有复杂非刚性运动的单目视频。

*   **Yan et al. (NeRF-DS, CVPR 2023 [telecomsci.com](https://www.telecomsci.com/zh/article/doi/10.11959/j.issn.1000-0801.2025152/))**：该研究专注于具有动态高光反射物体的场景重建，提出了一种新的神经辐射场方法。他们引入了专门的处理机制来应对动态高光反射表面带来的挑战，这些表面会随时间和视角发生剧烈变化。实验结果表明，NeRF-DS在处理高光反射动态场景方面优于现有方法，提升了渲染的真实感。

**2. 基于可变形三维高斯泼溅（Deformable 3D Gaussian Splatting）**

3DGS因其出色的渲染质量和实时渲染能力，迅速成为动态场景重建领域的热点。可变形3DGS方法旨在将3DGS的优势扩展到动态场景，通过引入变形场或时间编码来处理高斯点的时变属性。

*   **Yang et al. (Deformable 3D Gaussians, CVPR 2024 [eet-china.com](https://www.eet-china.com/mp/a297533.html))**：该工作首次将变形场与3D高斯相结合，实现了高质量的单目动态场景重建与新视角渲染。它将COLMAP初始化的3D高斯视为规范空间，通过变形场预测每个高斯随时间变化的位置和形状参数。在D-NeRF数据集上，该方法实现了显著的PSNR提升，并在真实场景中增加了渲染细节。该方法还引入了退火平滑训练（AST）来提高时间插值的稳定性和平滑性。

*   **Wu et al. (4D Gaussian Splatting, CVPR 2024 [telecomsci.com](https://www.telecomsci.com/zh/article/doi/10.11959/j.issn.1000-0801.2025152/))**：该论文提出了4D Gaussian Splatting for Real-Time Dynamic Scene Rendering，探索了实现实时动态场景渲染的方法，同时兼顾训练和存储效率。其核心在于将3D高斯模型与4D神经体素结合，通过分解的神经体素编码和轻量级MLP预测高斯变形，实现了动态场景的整体表示。实验结果表明，4DGS在实时动态场景渲染方面表现出高性能，并在保持高视觉质量的同时提高了效率。

*   **Bae et al. (Per-Gaussian embedding-based deformation, ECCV 2024 [telecomsci.com](https://www.telecomsci.com/zh/article/doi/10.11959/j.issn.1000-0801.2025152/))**：该工作提出了基于每个高斯嵌入的变形方法（E-DGGS），通过定义每个高斯的变形来提高动态场景重建的质量。它将变形分解为粗略变形和精细变形，以分别捕捉慢速和快速运动。与之前基于坐标函数的变形场不同，该方法将变形定义为每个高斯嵌入和时间嵌入的函数，从而更好地处理3DGS作为多个高斯场混合的特性，提升了复杂动态场景的重建准确性。

**3. 结合SLMA范式与大模型先验**

为了克服单目视觉的固有限制，一些研究将单目动态重建与同时定位与地图构建（SLAM）范式相结合，或利用大模型强大的泛化能力来补全信息。

*   **Liu et al. (SLAM3R, CVPR 2025 [blog.csdn.net](https://blog.csdn.net/amusi1994/article/details/147818644))**：北京大学团队提出的SLAM3R是一个实时三维重建系统，首次实现了从长视频（单目RGB序列）中实时且高质量地重建场景的稠密点云。该方案通过前馈神经网络将局部多视角三维重建与全局增量式坐标配准无缝集成，无需迭代优化相机参数或三维点云。SLAM3R在多个数据集上展示了先进的重建质量，并在消费级显卡上保持20+ FPS的实时性能，为纯数据驱动的长视频序列三维几何感知提供了新思路。

*   **Shi et al. (PanoSSC, arXiv 2024 [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/28582))**：PanoSSC探索了用于自动驾驶的单目全景三维场景重建，通过语义化的均匀体素表示周围环境。该方法解决了现代占用网络中单个物体预测不一致和相邻物体预测混合的问题，通过分别预测前景物体和背景并进行合并。PanoSSC将几何重建、3D语义分割和3D实例分割统一到框架中，在SemanticKITTI语义场景补全基准测试中取得了有竞争力的结果，展示了单目视觉系统在复杂驾驶场景下进行精细三维感知的潜力。

*   **Liang et al. (Zero-Shot Monocular Scene Flow Estimation, arXiv 2025 [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/101119))**：该研究解决了场景流估计的泛化性问题，提出了一种能够联合估计几何和运动的方法，并在大规模合成数据上进行训练。通过一种数据配方缓解了场景流数据稀缺问题，并评估了不同的场景流预测参数化方法。该模型在3D端点误差方面超越了现有方法，并在随意视频和机器人操作场景中展示了零样本泛化能力，使得场景流预测在实际应用中更具可行性。

### 实验与评价总结

综上所述，当前单目动态场景重建的代表性工作在以下几个方面取得了显著进展：

*   **渲染质量大幅提升**：基于神经辐射场和三维高斯泼溅的方法在合成数据集（如D-NeRF）和真实世界数据集上均展现出照片级真实渲染能力，相较于早期的隐式表示方法，PSNR等定量指标有显著提高，视觉伪影减少。浙江大学团队的Deformable 3D Gaussians [eet-china.com](https://www.eet-china.com/mp/a297533.html)在PSNR上实现了10多个点的提升，是这一趋势的典型代表。
*   **处理复杂动态场景的能力增强**：除了刚性运动，研究也开始有效处理非刚性形变（如Nerfies [telecomsci.com](https://www.telecomsci.com/zh/article/doi/10.11959/j.issn.1000-0801.2025152/)）、动态高光反射（如NeRF-DS [telecomsci.com](https://www.telecomsci.com/zh/article/doi/10.11959/j.issn.1000-0801.2025152/)）等更具挑战性的场景属性。
*   **实时性与效率提高**：相较于传统NeRF的训练和渲染速度瓶颈，基于3DGS的方法及其优化在训练和渲染效率上实现了质的飞跃，部分方法已能在消费级GPU上实现实时渲染（例如4D Gaussian Splatting [telecomsci.com](https://www.telecomsci.com/zh/article/doi/10.11959/j.issn.1000-0801.2025152/)和SLAM3R [blog.csdn.net](https://blog.csdn.net/amusi1994/article/details/147818644)）。
*   **泛化能力与鲁棒性提升**：通过大规模数据训练和引入大模型先验（如Zero-Shot Monocular Scene Flow Estimation [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/101119)），模型的跨场景、跨数据集泛化能力得到加强。同时，针对现实世界相机位姿不准（如Deformable 3D Gaussians [eet-china.com](https://www.eet-china.com/mp/a297533.html)）及低质量输入（如Robust Neural Rendering [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/146190)）的鲁棒性也得到关注。
*   **几何表示的精细化与结构化**：除了生成逼真的图像，模型也开始关注输出结构化、语义化的三维几何信息，例如PanoSSC [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/28582)在自动驾驶场景中进行全景语义体素重建，以及DP-Recon [qbitai.com](https://www.qbitai.com/2025/04/275969.html)通过扩散模型先验实现分解式物体重建。

### 趋势与挑战

2025年前后，单目动态场景重建领域呈现出以下几个显著的研究趋势及伴随的挑战：

1.  **大规模预训练模型与零样本/少样本泛化**：大型基础模型在图像和文本领域展现出强大能力，在3D领域也开始扮演重要角色。未来的研究将更多地探索如何将大规模3D数据和预训练模型（如LRM: Large Reconstruction Model [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/6d4757c9-de47-4f69-9248-a2185b219a36)）引入单目动态场景重建，以实现更好的零样本或少样本泛化能力。挑战在于3D数据获取成本高昂、大规模3D模型训练计算资源需求巨大，以及如何有效引导通用性强的生成模型产生几何和时间上精确且一致的结果。

2.  **实时、鲁棒的稠密几何与语义重建**：随着应用对实时交互和环境理解的需求增加，如何在保持高性能（如SLAM3R [blog.csdn.net](https://blog.csdn.net/amusi1994/article/details/147818644)）的同时，实现高精度的动态稠密几何重建，并进一步融入语义理解（如PanoSSC [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/28582)）仍是核心挑战。尤其是在复杂多变、光照不均或快速运动的野外场景中，如何确保重建的鲁棒性（如Robust Neural Rendering [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/146190)）仍然是一个开放问题。

3.  **多模态融合与物理一致性**：单一RGB输入限制了深度和运动估计的准确性。未来的工作可能探索单目RGB与其他廉价传感器（如惯性测量单元IMU）的融合，以提升重建精度和鲁棒性。同时，引入物理约束（如物体间的相互作用，场景中物体的运动学规律）将是提升重建模型合理性和一致性的重要方向。当前基于大模型先验的方法（如DP-Recon [qbitai.com](https://www.qbitai.com/2025/04/275969.html)）已经开始展现通过“脑补”恢复被遮挡信息的能力，但确保这些补全信息符合物理真实性仍有待深入研究。

### 结论

2022-2025年间，单目动态场景重建技术取得了突破性进展，这主要得益于神经辐射场和三维高斯泼溅等新型神经表示的兴起。通过引入变形场、结合SLAM范式或利用大模型先验，研究人员显著提升了动态场景的渲染质量、实时性、鲁棒性及泛化能力。未来的研究趋势将聚焦于更大规模模型的引入、实时稠密语义重建、多模态融合和物理一致性约束，以期在更复杂的真实世界单目动态场景中实现精确、高效且智能的重建。

### 参考文献

*   [eet-china.com](https://www.eet-china.com/mp/a297533.html) Yang, Z., Gao, X., Zhou, W., et al. (2024). Deformable 3D Gaussians for High-Fidelity Monocular Dynamic Scene Reconstruction. *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*.
*   [blog.csdn.net](https://blog.csdn.net/amusi1994/article/details/147818644) Liu, Y., Dong, S., Wang, S., et al. (2025). SLAM3R: Real-Time Dense Scene Reconstruction from Monocular RGB Videos. *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*.
*   [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/101119) Liang, Y., Badki, A., Su, H., Tompkins, J., & Gallo, O. (2025). Zero-Shot Monocular Scene Flow Estimation in the Wild. *arXiv preprint arXiv:2501.10357*.
*   [telecomsci.com](https://www.telecomsci.com/zh/article/doi/10.11959/j.issn.1000-0801.2025152/) Lu, P., Sun, J.J., Li, W., et al. (2025). A review of dynamic scene reconstruction based on neural representation. *Telecommunications Science, 41*(6), 166-179.
*   [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/28582) Shi, Y., Li, J., Jiang, K., et al. (2024). PanoSSC: Exploring Monocular Panoptic 3D Scene Reconstruction for Autonomous Driving. *arXiv preprint arXiv:2406.07037*.
*   [telecomsci.com](https://www.telecomsci.com/zh/article/doi/10.11959/j.issn.1000-0801.2025152/) Pumarola, A., Corona, E., Pons-Moll, G., et al. (2021). D-NeRF: Neural radiance fields for dynamic scenes. *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*.
*   [telecomsci.com](https://www.telecomsci.com/zh/article/doi/10.11959/j.issn.1000-0801.2025152/) Park, K., Sinha, U., Barron, J.T., et al. (2021). Nerfies: Deformable neural radiance fields. *Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV)*.
*   [telecomsci.com](https://www.telecomsci.com/zh/article/doi/10.11959/j.issn.1000-0801.2025152/) Yan, Z., Li, C., Lee, G.H. (2023). NeRF-DS: Neural Radiance Fields for Dynamic Specular Objects. *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*.
*   [telecomsci.com](https://www.telecomsci.com/zh/article/doi/10.11959/j.issn.1000-0801.2025152/) Wu, G.J., Yi, T.R., Fang, J.M., et al. (2024). 4D Gaussian Splatting for Real-Time Dynamic Scene Rendering. *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*.
*   [telecomsci.com](https://www.telecomsci.com/zh/article/doi/10.11959/j.issn.1000-0801.2025152/) Bae, J., Kim, S., Yun, Y., et al. (2024). Per-Gaussian Embedding-Based Deformation for Deformable 3D Gaussian Splatting. *Proceedings of the European Conference on Computer Vision (ECCV)*.
*   [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/146190) Li, C., Shi, Z., Lu, Y., He, W., & Xu, X. (2025). Robust Neural Rendering in the Wild with Asymmetric Dual 3D Gaussian Splatting. *arXiv preprint arXiv:2506.03538*.
*   [qbitai.com](https://www.qbitai.com/2025/04/275969.html) Ni, J., Liu, Y., Lu, R., et al. (2025). Diffusion Model Enables Complete 3D Reconstruction and Scene Editing from Sparses Views. *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*. (Referred to as DP-Recon in the text)
*   [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/6d4757c9-de47-4f69-9248-a2185b219a36) Hong, Y., Zhang, K., Gu, J., et al. (2023). LRM: Large Reconstruction Model for Single Image to 3D. *arXiv preprint arXiv:2311.04400*.