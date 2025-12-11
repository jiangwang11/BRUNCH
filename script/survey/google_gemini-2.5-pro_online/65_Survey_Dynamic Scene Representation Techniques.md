好的，遵照您的要求，我将基于提供的搜索结果，生成一篇关于“动态场景表示技术”的严谨中文学术综述。

---

### **动态场景表示技术（2022-2025）学术综述**

#### **引言**

动态场景表示（Dynamic Scene Representation）旨在构建能够精确捕捉并描述物理世界在时间维度上变化的四维（4D, 3D空间+时间）模型。该技术不仅需要重建场景的静态几何与外观，还必须对物体的运动、形变乃至拓扑结构变化进行建模。随着自动驾驶、机器人、增强现实（AR）以及数字孪生等领域的快速发展，对高保真、实时、可交互的动态场景表示的需求日益迫切。早期工作主要聚焦于静态场景的神经辐射场（NeRF）重建，而2022至2025年间，研究重点显著转向如何高效、鲁棒地处理动态元素，并与高级语义理解相结合。本综述旨在梳理这一时期的代表性技术，将其归纳为不同范式，总结其核心思想与共性评价，并预测未来研究趋势。

#### **方法分类与代表作**

##### 1. 基于隐式神经表示的分解与变形方法

该类方法延续了NeRF的思想，通过引入时间变量或变形场来扩展到4D空间，核心在于如何有效解耦场景中的静态与动态成分。

*   **EmerNeRF (ICLR 2024)** [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/6742)：该研究旨在解决无监督环境下的动态场景时空分解问题。其核心方法是通过自监督学习，将场景分层为静态场和动态场，并从动态场中参数化一个感应流场（induced flow field）。利用该流场聚合多帧特征，能够显著提升动态物体的渲染精度，而无需依赖外部标注或预训练的光流模型。实验表明，该方法在重建动态场景时，PSNR指标比先前方法提升了3.25，并且将2D视觉基础模型特征提升到4D后，显著提高了3D感知性能（占用预测准确率提升78.5%）。

*   **Neural 3D Video (CVPR 2022)** [blog.csdn.net](https://blog.csdn.net/m0_51976564/article/details/142719707)：此工作致力于将NeRF高效扩展至时间维度以处理动态视频。研究者提出使用随时间变化的紧凑隐变量（time-dependent latent codes）来控制一个共享的MLP网络，而非直接将时间作为输入。为提升效率，该方法采用了分层训练（Hierarchical Training）和光线重要性采样（Ray Importance Sampling）策略，优先训练场景变化显著的关键帧和像素。这一设计在DyNeRF等数据集上实现了对动态场景的快速且高质量的渲染。

*   **NeRFPlayer (TVCG 2023)** [blog.csdn.net](https://blog.csdn.net/m0_51976564/article/details/142719707)：该研究关注流式动态场景表示，以支持实时交互应用。其核心是将动态场景分解为一个高质量的静态场景基底与一个轻量级的、可流式传输的动态场景层。这种分解架构使得在渲染时可以高效合并静态背景与实时更新的动态元素，从而实现了对动态场景的流式加载和播放。该方法为网络环境下的动态场景交互提供了有效解决方案。

##### 2. 基于显式与混合表示的因子分解方法

为克服隐式MLP表示的计算瓶颈，该范式将4D时空场显式地分解为多个低维（如1D、2D）特征网格或平面，通过高效的特征采样与融合实现4D表示，在训练和渲染速度上取得了巨大突破。

*   **K-Planes / HexPlane (CVPR 2023)** [blog.csdn.net](https://blog.csdn.net/m0_51976564/article/details/142719707)：这两项工作解决了动态场景表示的效率问题，其核心思想一致，即将4D时空坐标(x,y,z,t)的查询分解到多组2D平面上。例如，K-Planes将4D场景分解为六个时空平面（XY, XZ, YZ, XT, YT, ZT），查询点的特征由其在各平面上插值得到的特征向量组合而成。这种显式分解避免了大型MLP的重复计算，从而实现了极快的训练速度和实时渲染性能，且易于扩展到更高维度。

*   **DrivingScene (2025)** [blog.csdn.net](https://blog.csdn.net/cv_autobot/article/details/154267939)：此研究针对自动驾驶场景，旨在仅凭两帧环视图像实现实时动态场景重建。方法采用两阶段训练范式：首先训练一个鲁棒的静态场景先验网络（基于3D高斯溅射），然后冻结该网络并训练一个残差流网络，专门预测动态物体的非刚性运动。该前馈式在线框架在保证高保真度的同时，推理速度（0.21s/帧）比先前的Driv3R快70%，模型参数量仅为其4.6%。

*   **4D LangSplat (CVPR 2025)** [hub.baai.ac.cn](https://hub.baai.ac.cn/view/44343)：该工作旨在实现动态场景中的开放词汇查询，解决了传统方法依赖静态CLIP特征的局限性。其核心是利用多模态大模型（MLLM）为视频中的物体生成高质量的句子级语言描述，并提取其特征以代替CLIP特征。同时，引入“状态变化网络”（Status Deformable Network）对动态语义特征进行平滑建模。实验表明，该方法在时间敏感查询任务上的帧级别准确率（ACC）提升了29.03%，显著优于基线方法。

##### 3. 基于结构化与语言模型的语义表示方法

此类方法超越了纯粹的几何与外观重建，致力于构建包含物体、关系、属性和功能的结构化语义模型，通常深度融合大型语言模型（LLM）实现高层认知。

*   **4D Panoptic Scene Graph (4D-PSG) (CVPR 2025)** [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/122417)：此研究旨在构建全面的动态4D全景场景图，但面临4D标注数据稀缺的挑战。为解决此问题，作者提出一个利用丰富的2D视觉场景标注来增强4D场景学习的框架。该框架包含一个用于端到端生成的4D大型语言模型（4D-LLM），并通过一种“时空场景超越”策略将2D场景图中的维度不变特征迁移至4D场景。实验证明，利用2D数据能有效补偿4D数据的稀缺性，模型性能显著超越了仅使用4D数据训练的基线。

*   **GPT4Scene (arXiv 2025)** [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/95719)：该工作探究并提升了视觉-语言模型（VLM）在3D空间理解方面的能力。研究发现VLM的主要缺陷在于缺乏场景全局与单帧局部之间的对应关系。为此，GPT4Scene引入一种新颖的视觉提示范式：从视频中构建鸟瞰图（BEV）并标记一致的对象ID，然后将带有标记的视频帧与BEV图一同输入模型。经过此范式训练后，开源VLM在所有3D理解任务上均达到SOTA性能，甚至在推理时无需视觉提示也能保持提升，表明其内化了3D理解能力。

##### 4. 面向动态场景的生成式模型

这一新兴方向利用生成模型（如扩散模型）学习动态场景的分布，旨在生成全新的、可控的、时空一致的4D场景，对仿真和数据增强意义重大。

*   **DynamicCity (ICLR 2025)** [finance.sina.com.cn](https://finance.sina.com.cn/tech/roll/2025-02-19/doc-inekytki3158010.shtml)：该研究首次实现了高质量、高效的大规模4D动态城市场景生成。其核心是一个两步框架：首先，利用一个基于HexPlane表示的变分自编码器（VAE），将复杂的4D场景数据压缩至紧凑的2D特征平面；其次，在 HexPlane 这一低维潜空间上训练一个扩散模型（DiT）以学习场景分布并生成新场景。该方法通过在低维空间操作，显著降低了内存消耗（减少70.84%），同时提升了重建精度（mIoU提升7.05%），并支持轨迹引导、场景编辑等多种可控生成。

#### **实验与评价总结**

*   **数据集与基准**：nuScenes、Waymo等自动驾驶数据集是动态场景重建的主要试验场。同时，研究界也发布了更专门的基准，如用于动态NeRF的DyNeRF [blog.csdn.net](https://blog.csdn.net/m0_51976564/article/details/142719707) 和HyperNeRF数据集。部分工作（如4D LangSplat）为了评估新任务，还自行构建了带有精细标注的新数据集 [hub.baai.ac.cn](https://hub.baai.ac.cn/view/44343)。
*   **评价指标**：
    *   **重建质量**：新视角合成的保真度仍是基础，主要通过PSNR、SSIM和LPIPS进行评估。
    *   **几何精度**：深度预测的准确性（如Abs Rel, RMSE）被用来衡量几何重建的质量。
    *   **语义与任务性能**：对于高级任务，评估指标更为多样。全景分割质量（PQ）用于评估像素级语义理解 [lingdong.fuxi.163.com](https://lingdong.fuxi.163.com/database/2613)。开放词汇查询则使用平均交并比（mIoU）和帧级预测准确率（ACC） [hub.baai.ac.cn](https://hub.baai.ac.cn/view/44343)。
*   **共性结论**：
    1.  **显式表达引领效率革命**：基于因子分解的显式或混合表示（如K-Planes, 3DGS）在训练/推理速度上全面超越了纯MLP的隐式方法，成为实现实时应用的主流选择。
    2.  **分解策略是控制复杂度的关键**：无论是将场景分解为静态和动态部分（EmerNeRF, DrivingScene），还是将时空特征分解为低维平面（HexPlane），这种“分而治之”的策略被证明是处理4D高维数据、稳定训练并提升性能的普适有效手段。
    3.  **大模型赋能高级语义理解**：融合预训练的视觉、语言及多模态大模型（4D-PSG, 4D LangSplat, GPT4Scene）已成为从几何重建迈向高级场景理解的必然路径，极大地扩展了动态场景表示的功能边界，使其具备开放词汇查询和推理能力。

#### **趋势与挑战**

展望2025年及以后，动态场景表示技术呈现以下明确趋势，并伴随着相应挑战：

1.  **构建交互式世界模型 (Interactive World Models)**：当前的研究正从“表示”场景转向“模拟”世界。未来的系统不仅能重建过去，更将具备预测未来和响应虚拟交互的能力。这意味着动态场景表示将成为机器人和自动驾驶系统的“沙盒模拟器”，用于策略学习和闭环测试。挑战在于如何从有限的观测数据中学习物理规律、因果关系和物体交互的常识。

2.  **语言模型驱动的端到端场景理解与生成**：以LLM/VLM为核心的统一模型将成为主流。用户将能通过自然语言指令实现对动态场景的查询、编辑、乃至从零生成（如DynamicCity的可控生成功能 [finance.sina.com.cn](https://finance.sina.com.cn/tech/roll/2025-02-19/doc-inekytki3158010.shtml)）。挑战在于如何实现语言指令与复杂时空几何、物理动态的精确对齐，以及如何保证生成内容的真实性和时空一致性。

3.  **迈向通用、在线和全生命周期的场景表示**：研究将致力于打破“离线、逐场景优化”的局限，发展能够在线运行、持续学习并适应新环境的通用模型（如DrivingScene的在线前馈框架 [blog.csdn.net](https://blog.csdn.net/cv_autobot/article/details/154267939)）。这意味着模型需要具备高效的增量更新能力和强大的泛化性，能够在整个生命周期内不断融合新信息。数据稀缺性和标注成本仍是主要障碍，驱动着自监督和弱监督学习方法的进一步发展。

#### **结论**

在2022至2025年间，动态场景表示技术经历了从隐式向显式、从几何重建向语义理解、从被动表示向主动生成的深刻变革。以时空分解为核心的效率提升和以大模型融合为核心的语义增强，共同推动了该领域向着更实时、更智能、更通用的方向发展。未来的研究将聚焦于构建可交互、语言驱动的世界模型，旨在为物理和虚拟世界中的智能体提供一个统一、动态且可理解的环境表征，为人机共融的未来奠定坚实的感知基石。

#### **参考文献**

1.  Wu, S., et al. (2025). *Learning 4D Panoptic Scene Graph Generation from Rich 2D Visual Scene*. In CVPR. [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/122417)
2.  Zhou, R., et al. (2025). *4D LangSplat*. In CVPR. [hub.baai.ac.cn](https://hub.baai.ac.cn/view/44343)
3.  Yang, J., et al. (2024). *EmerNeRF: Emergent Spatial-Temporal Scene Decomposition via Self-Supervision*. In ICLR. [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/6742)
4.  Bian, H., et al. (2025). *DynamicCity*. In ICLR Spotlight. [finance.sina.com.cn](https://finance.sina.com.cn/tech/roll/2025-02-19/doc-inekytki3158010.shtml)
5.  Qi, Z., et al. (2025). *GPT4Scene: Understand 3D Scenes from Videos with Vision-Language Models*. arXiv preprint. [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/95719)
6.  Hou, Q., et al. (2025). *DrivingScene: A Multi-Task Online Feed-Forward 3D Gaussian Splatting Method for Dynamic Driving Scenes*. [blog.csdn.net](https://blog.csdn.net/cv_autobot/article/details/154267939)
7.  Li, T., et al. (2022). *Neural 3d video synthesis from multi-view video*. In CVPR. [blog.csdn.net](https://blog.csdn.net/m0_51976564/article/details/142719707)
8.  Song, L., et al. (2023). *Nerfplayer: A streamable dynamic scene representation with decomposed neural radiance fields*. In TVCG. [blog.csdn.net](https://blog.csdn.net/m0_51976564/article/details/142719707)
9.  Fridovich-Keil, S., et al. (2023). *K-planes: Explicit radiance fields in space, time, and appearance*. In CVPR. [blog.csdn.net](https://blog.csdn.net/m0_51976564/article/details/142719707)
10. Cao, A., & Johnson, J. (2023). *Hexplane: A fast representation for dynamic scenes*. In CVPR. [blog.csdn.net](https://blog.csdn.net/m0_51976564/article/details/142719707)
11. Shao, R., et al. (2023). *Tensor4d: Efficient neural 4d decomposition for high-fidelity dynamic reconstruction and rendering*. In CVPR. [blog.csdn.net](https://blog.csdn.net/m0_51976564/article/details/142719707)
12. Işık, M., et al. (2023). *Humanrf: High-fidelity neural radiance fields for humans in motion*. In ACM Transactions on Graphics (TOG). [blog.csdn.net](https://blog.csdn.net/m0_51976564/article/details/142719707)
13. 网易伏羲. (2025). *全景语义分割：构建像素级环境理解的统一视觉认知框架*. [lingdong.fuxi.163.com](https://lingdong.fuxi.163.com/database/2613)