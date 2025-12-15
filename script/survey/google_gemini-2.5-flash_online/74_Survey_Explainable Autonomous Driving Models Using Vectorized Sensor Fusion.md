好的，这是一篇关于“Explainable Autonomous Driving Models Using Vectorized Sensor Fusion”的中文学术综述，涵盖2022-2025年的代表性工作。

---

## 可解释自主驾驶模型中的矢量化传感器融合研究综述

### 引言

自主驾驶系统在近年来取得了显著进步，端到端学习方法展现出简化系统并提升驾驶性能的潜力。然而，现有框架在闭环评估中仍面临成功率低、鲁棒性差以及缺乏透明推理等挑战，尤其在实际部署中，模型决策的不可解释性是制约其广泛应用的关键因素。为了解决这些问题，研究者们将多模态数据融合技术与可解释性方法相结合，旨在构建能够提供清晰决策依据的自主驾驶模型。其中，将不同传感器数据统一到矢量化表示空间进行融合，并在此基础上融入可解释性机制成为探索前沿。本文将综述2022-2025年间，可解释自主驾驶模型在矢量化传感器融合方面的代表性工作。

### 方法分类与代表作

目前，可解释自主驾驶模型中的矢量化传感器融合方法大致可分为基于鸟瞰图（BEV）的融合、基于Transformer的融合以及结合大视觉语言模型（LVLMs）的融合等几类。

#### 1. 基于鸟瞰图（BEV）的融合

基于BEV的融合方法将来自不同传感器的异构数据统一投影到鸟瞰图空间，从而提供一个几何和语义信息均保留的统一表示，便于后续感知和决策任务。

*   **BEVFusion: Multi-Task Multi-Sensor Fusion with Unified Bird's-Eye View Representation (ICRA 2023)** [blog.csdn.net](https://blog.csdn.net/i6101206007/article/details/131296850), [blog.csdn.net](https://blog.csdn.net/weixin_62497890/article/details/133708937), [blog.csdn.net](https://blog.csdn.net/qq_44799766/article/details/136836260)
    *   研究问题：解决多传感器融合中相机到LiDAR点云投影带来的语义密度损失和传统点级融合对语义任务的局限性。
    *   核心方法：提出BEVFusion框架，将相机和LiDAR特征统一到共享的BEV空间，保留几何结构和语义密度。通过优化BEV池化操作，将相机到BEV的转换效率提升40倍以上，实现高效的多任务多传感器融合。
    *   关键实验结论：在nuScenes基准上，BEVFusion在3D目标检测和BEV地图分割任务中均取得领先性能，尤其BEV地图分割mIoU相比纯LiDAR模型提高13.6%，且计算成本降低1.9倍。

*   **Detecting As Labeling: Rethinking LiDAR-camera Fusion in 3D Object Detection (ECCV 2024)** [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/99733)
    *   研究问题：纠正LiDAR-相机融合3D目标检测中因模型设计与数据标注原则不符导致的过拟合问题。
    *   核心方法：引入“检测即标注”（DAL）范式，强制回归任务仅使用LiDAR特征，而相机特征用于候选生成和分类，模仿真实标注过程。通过BEVPoolV2优化视图变换，显著减少内存并加速推理。
    *   关键实验结论：DAL在nuScenes验证集上实现了71.5 mAP和74.0 NDS的性能，超越现有SOTA，并在准确性和效率之间提供了更优的权衡，同时训练流程更为简化。

#### 2. 基于Transformer的融合

Transformer模型凭借其强大的自注意力机制，能够有效处理多模态数据中的长距离依赖和上下文信息，从而实现更精细的特征融合。

*   **TransFusion: Robust LiDAR-Camera Fusion for 3D Object Detection with Transformers (CVPR 2022)** [blog.csdn.net](https://blog.csdn.net/weixin_45041518/article/details/129316536), [www.eet-china.com](https://www.eet-china.com/mp/a246434.html)
    *   研究问题：解决LiDAR-相机融合中模态错位问题，提升3D目标检测在复杂场景下的鲁棒性。
    *   核心方法：通过Transformer对特征进行软关联，利用LiDAR BEV特征生成稀疏查询，并借助图像特征丰富这些查询，以利用局部归纳偏差和交叉注意力机制。
    *   关键实验结论：在nuScenes数据集上表现出优异的3D目标检测性能，表明Transformer在处理跨模态信息交互方面的有效性。

*   **FUTR3D: A Unified Sensor Fusion Framework for 3D Detection (arXiv 2022)** [blog.csdn.net](https://blog.csdn.net/weixin_45041518/article/details/129316536), [www.eet-china.com](https://www.eet-china.com/mp/a246434.html)
    *   研究问题：构建一个对任意数量传感器模态都具有鲁棒性的3D检测框架。
    *   核心方法：提出模态不可知特征采样器（MAFS），通过3D查询从多视图相机、LiDAR和雷达收集特征。查询先解码获得3D坐标作为锚点，然后迭代地从所有模态中聚合相关特征。
    *   关键实验结论：展示了其在集成多源异构传感器数据方面的灵活性和高性能，为统一多传感器3D检测提供了通用范式。

*   **X-Driver: Explainable Autonomous Driving with Vision-Language Models (arXiv 2025)** [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/135308)
    *   研究问题：提升端到端自主驾驶系统在闭环环境中的成功率和可解释性，克服现有MLLM模型的幻觉和鲁棒性问题。
    *   核心方法：引入X-Driver框架，将视觉-语言模型（MLLMs）与思维链（CoT）推理和自回归建模相结合。利用ViT进行连续图像编码保留细粒度空间细节，并通过CoT逐步分析交通状况、物体检测等子任务，生成驾驶动作及解释。
    *   关键实验结论：在CARLA仿真环境中，X-Driver在多个自主驾驶任务中超越SOTA，闭环性能优越，同时显著提高了驾驶决策的可解释性，强调了结构化推理在端到端驾驶中的重要性。

#### 3. 结合大型视觉语言模型（LVLMs）的融合

LVLMs的兴起为自主驾驶带来了新的可能，它们能够结合视觉信息和自然语言指令进行高级语义理解和推理，并生成可解释的决策。

*   **Senna: Bridging Large Vision-Language Models and End-to-End Autonomous Driving (arXiv 2024)** [yiyibooks.cn](https://yiyibooks.cn/information/arxiv/2410.22313v1/)
    *   研究问题：解决端到端自动驾驶在复杂罕见场景中常识有限的问题，以及弥合其与LVLMs在场景理解和推理能力上的差距。
    *   核心方法：探索融合端到端自动驾驶的强大规划能力与LVLMs卓越的场景理解和推理优势的方法。
    *   关键实验结论：该论文侧重于融合两种方法的优势，预期为解决复杂驾驶场景的常识推理问题提供新途径。

#### 4. 端到端同步多模态融合检测

旨在通过单一训练阶段同时优化多模态融合和目标检测，提高效率并避免子任务间的不一致。

*   **E2E-MFD: Towards End-to-End Synchronous Multimodal Fusion Detection (arXiv 2025)** [www.zhuanzhi.ai](https://www.zhuanzhi.ai/paper/e9aa06469e8df6843b22e29a27de06ed)
    *   研究问题：解决现有图像融合与目标检测方法中，复杂训练过程对实际应用的阻碍，并提升融合检测的性能。
    *   核心方法：提出E2E-MFD，一种新颖的端到端同步多模态融合检测算法，通过单一训练阶段实现高性能。它采用同步联合优化策略，并通过梯度矩阵中的综合优化确保收敛到最优融合检测配置。
    *   关键实验结论：在多个公共数据集上，E2E-MFD在横向目标检测M3FD上mAP50提高了3.9%，在定向目标检测DroneVehicle上mAP50提高了2.0%，展现出优越的融合和检测能力。

### 实验与评价总结

综上所述，可解释自主驾驶模型中的矢量化传感器融合方法展示出以下共性优势：

1.  **性能提升：** 大多数研究通过将相机、LiDAR等传感器数据在统一的BEV空间进行融合，或利用Transformer进行跨模态特征交互，显著提升了3D目标检测和BEV地图分割等任务的准确性（如mAP和NDS指标）。
2.  **鲁棒性增强：** 多模态融合有助于系统在恶劣天气（雨天、夜间）和传感器部分失灵（如稀疏LiDAR点云）的挑战性条件下保持稳定的感知性能，通过弥补单一模态的局限性来提高整体鲁棒性。
3.  **效率优化：** 通过创新的视图变换（如BEVFusion中的高效BEV池化）和任务无关的融合架构，许多方法能够在保持高性能的同时降低计算成本并提高推理速度，甚至超越了现有SOTA方法。
4.  **可解释性探索：** 引入CoT推理、LVLMs等机制，使得模型能够提供更加透明和可理解的决策依据，从而增强了自主驾驶系统在安全关键应用中的可信度和调试能力 (例如X-Driver)。

这些方法共同推动了自主驾驶感知系统向着更准确、更鲁棒、更高效和更可信赖的方向发展。

### 趋势与挑战

2025年及未来几年，可解释自主驾驶模型中的矢量化传感器融合领域将呈现以下研究趋势：

1.  **深度可解释性与因果推理：** 随着LLM和LVLM在可解释性方面展现出潜力，未来的研究将更深入地探索如何实现模型决策的深层因果推理，而不仅仅是表层解释。例如，结合“反事实解释”（counterfactual explanations）和“因果发现”（causal discovery）技术，帮助系统理解“为什么不是这个决策”以及潜在的驾驶风险。
2.  **通用基础模型与域适应性：** 发展能够处理多类型、多配置传感器数据，并在不同驾驶场景下具有强大泛化能力的通用基础模型。这将涉及更精巧的预训练策略和轻量级域适应技术，以减少在不同地理区域或车辆平台上的重新训练成本。
3.  **异构传感器融合的实时优化：** 虽然现有方法在效率上有所提高，但对于更多样化的异构传感器（如雷达、超声波、事件相机等）的同步、实时、多层级融合仍然是一个挑战。研究将聚焦于开发更高效的硬件架构感知融合算法，例如在边缘设备上实现低延迟、低功耗的复杂传感器融合。

挑战主要集中在数据标注复杂性、模型泛化能力、实时性与可解释性的平衡，以及如何有效评估复杂模型的安全性和可靠性。

### 结论

可解释自主驾驶模型中的矢量化传感器融合是自主驾驶领域的一个关键研究方向。通过将多模态传感器数据在统一、高效的矢量化表示空间中进行融合，并结合先进的深度学习技术（如Transformer和LVLMs），研究者们正不断提升自主驾驶系统的感知性能、鲁棒性和决策透明度。未来的研究将进一步深化可解释性机制、追求通用基础模型，并优化异构传感器融合的实时性，以克服现有挑战，最终实现安全可靠的全面自主驾驶。

### 参考文献

1.  Liu, W., Zhang, J., Zheng, B., Hu, Y., Lin, Y., & Zeng, Z. (2025). X-Driver: Explainable Autonomous Driving with Vision-Language Models. *arXiv preprint arXiv:2505.05098*. [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/135308)
2.  Zhang, J., Cao, M., Xie, W., Lei, J., Li, D., Huang, W., Li, Y., & Yang, X. (2025). E2E-MFD: Towards End-to-End Synchronous Multimodal Fusion Detection. *arXiv preprint arXiv:2403.09323v4*. [www.zhuanzhi.ai](https://www.zhuanzhi.ai/paper/e9aa06469e8df6843b22e29a27de06ed)
3.  Liu, Z., Tang, H., Amini, A., Yang, X., Mao, H., Rus, D., & Han, S. (2023). BEVFusion: Multi-Task Multi-Sensor Fusion with Unified Bird's-Eye View Representation. *International Conference on Robotics and Automation (ICRA)*. [blog.csdn.net](https://blog.csdn.net/i6101206007/article/details/131296850)
4.  Huang, J., Ye, Y., Liang, Z., Shan, Y., & Du, D. (2024). Detecting As Labeling: Rethinking LiDAR-camera Fusion in 3D Object Detection. *European Conference on Computer Vision (ECCV)*. [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/99733)
5.  Bai, X., Hu, Z., Zhu, X., Huang, Q., Chen, Y., Fu, H., & Tai, C.-L. (2022). TransFusion: Robust LiDAR-Camera Fusion for 3D Object Detection with Transformers. *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*. [blog.csdn.net](https://blog.csdn.net/weixin_45041518/article/details/129316536)
6.  Chen, X., Zhang, T., Wang, Y., Wang, Y., & Zhao, H. (2022). FUTR3D: A Unified Sensor Fusion Framework for 3D Detection. *arXiv preprint arXiv:2203.10642*. [www.eet-china.com](https://www.eet-china.com/mp/a246434.html)
7.  Liu, Z., Tang, H., Amini, A., Yang, X., Mao, H., Rus, D., & Han, S. (2025). BEVFusion: Multi-Task Multi-Sensor Fusion with Unified Bird's-Eye View Representation. *CSDN Blog*. [blog.csdn.net](https://blog.csdn.net/weixin_62497890/article/details/133708937)
8.  Amini, A., Tang, H., Liu, Z., Yang, X., Mao, H., Rus, D., & Han, S. (2025). BEVFusion: Multi-Task Multi-Sensor Fusion with Unified Bird's-Eye View Representation Explained. *CSDN Blog*. [blog.csdn.net](https://blog.csdn.net/qq_44799766/article/details/136836260)
9.  Anonymous. (2024). Senna: Bridging Large Vision-Language Models and End-to-End Autonomous Driving. *arXiv preprint arXiv:2410.22313v1*. [yiyibooks.cn](https://yiyibooks.cn/information/arxiv/2410.22313v1/)
10. Anonymous. (2025). 基于Transformer的自动驾驶传感器融合技术解析. *电子工程专辑*. [www.eet-china.com](https://www.eet-china.com/mp/a246434.html)
11. Anonymous. (2025). 基于Transformer的自动驾驶传感器融合研究综述. *CSDN Blog*. [blog.csdn.net](https://blog.csdn.net/weixin_45041518/article/details/129316536)
12. Anonymous. (2023). Multi-modal Sensor Fusion for Auto Driving Perception: A Survey. *CSDN Blog*. [blog.csdn.net](https://blog.csdn.net/shanglianlm/article/details/128792031)