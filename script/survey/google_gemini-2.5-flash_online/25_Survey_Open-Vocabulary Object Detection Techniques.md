## 开放词汇目标检测技术研究综述

### 引言

传统目标检测模型受限于预定义类别，难以应对真实世界中不断涌现的未知物体。开放词汇目标检测（Open-Vocabulary Object Detection, OVOD）旨在使模型具备识别和定位训练集中未出现的任意语义类别的能力，极大地提升了目标检测的泛化性和灵活性，在机器人学、自动驾驶等开放场景中具有广阔的应用前景。本综述将聚焦2022-2025年间的代表性工作，系统梳理OVOD领域的核心技术路线与进展，总结共性实验结论，并展望未来的研究趋势与挑战。

### 方法分类与代表作

当前OVOD技术主要围绕视觉-语言对齐、知识迁移和训练策略等角度展开，核心在于利用大规模视觉-语言预训练模型（Vision and Language Models, VLMs）的跨模态能力。

#### 1. 基于知识蒸馏的方法

知识蒸馏旨在将VLM的丰富知识迁移至目标检测器，尤其关注视觉特征与文本嵌入的对齐，以提升分类泛化能力。

*   **ViLD [jcjs.siat.ac.cn]**
    *   **研究问题**: 如何有效地将预训练的VLM知识迁移到两阶段目标检测器，使其具备开放词汇能力。
    *   **核心方法**: 首次将CLIP模型作为教师模型，通过L1损失对齐检测器（学生模型）中候选框的视觉嵌入。
    *   **关键实验结论**: 在LVIS数据集上验证了该方法能有效提升检测器对稀有类别的泛化能力。

*   **DK-DETR [jcjs.siat.ac.cn]**
    *   **研究问题**: 如何在知识蒸馏中引入关系知识，以更全面地传承教师模型的目标关系理解。
    *   **核心方法**: 在确保视觉嵌入一致性的基础上，通过语义相似度矩阵对齐目标间的关系知识，并使用Kullback-Leibler散度度量关系图的差异。
    *   **关键实验结论**: 实现了视觉嵌入的拉近（同一目标）与拉远（不同目标），显著提升了模型在开放世界场景中的关系理解能力。

*   **SAMP [jcjs.siat.ac.cn]**
    *   **研究问题**: 面对类别多样性挑战与图文对齐层级差异，如何增强OVOD模型的鲁棒性。
    *   **核心方法**: 提出了场景自适应和区域感知的多模态提示，通过低秩分解机制构建特定于场景的多模态提示集，并利用区域提示提取全局特征中的位置信息融入区域特性。
    *   **关键实验结论**: 在LVIS基础类别数据训练且无额外数据集辅助下，取得了领先的性能，表明蒸馏策略可通过算法创新弥补数据规模不足。

#### 2. 基于预训练策略的方法

此类方法通过在更大规模的无标注或弱标注数据上进行预训练，将外部知识注入模型，突破传统检测模型的类别限制。

*   **GLIP [jcjs.siat.ac.cn]**
    *   **研究问题**: 如何构建统一的视觉范式，融合异构监督信号，从而利用多种类型的数据源进行OVOD预训练。
    *   **核心方法**: 将目标检测重新定义为视觉定位任务，将图像与所有候选类别拼接的文本提示作为输入，构建了目标检测与视觉定位的统一学习框架。
    *   **关键实验结论**: 通过整合视觉定位数据进行预训练，显著丰富了训练样本，并在LVIS数据集上取得了较强的开放词汇检测性能。

*   **Grounding DINO [opendeep.wiki], [blog.csdn.net/m0_55898550], [jcjs.siat.ac.cn]**
    *   **研究问题**: GLIP中所有类别随机拼接可能引入无关类别的相互影响，如何优化文本特征提取。
    *   **核心方法**: 将Transformer-based检测器DINO与接地预训练相结合，引入了子句文本特征技术，以去除无关类别间的注意力干扰，优化了语言与视觉模态的融合。
    *   **关键实验结论**: 在COCO检测零样本迁移基准上达到52.5 AP，微调后达63.0 AP，并在ODinW零样本基准上创下新高，展现了强大的开放集对象检测能力。

*   **DetCLIPv3-T [jcjs.siat.ac.cn]**
    *   **研究问题**: 如何有效利用多种异构数据源（目标检测、视觉定位、图像-文本对）提升OVOD模型的泛化能力和识别精度。
    *   **核心方法**: 在开放词汇检测器基础上配备了对象描述器，设计了自动标注方案，利用语言建模为每个检测到的目标区域生成多粒度的类别标签。
    *   **关键实验结论**: 在LVIS数据集上使用了较小视觉主干网络时取得了最佳表现，领先同规模及更大规模模型，证明了综合使用多种数据类型和精细化标签生成策略的有效性。

#### 3. 基于模型微调的方法

这类方法通过冻结VLM的视觉编码器与文本编码器参数，仅对检测头等下游任务模块进行轻量化训练，在效率与性能间取得平衡。

*   **F-VLM [jcjs.siat.ac.cn]**
    *   **研究问题**: 在不依赖知识蒸馏或伪标注的情况下，如何利用冻结的VLM提升OVOD性能。
    *   **核心方法**: 冻结预训练VLM中的视觉编码器和文本编码器参数，仅在视觉编码器后添加目标检测头，并利用基础类别的标注数据进行训练。
    *   **关键实验结论**: 简化了训练流程，提供了高效灵活的解决方案，在LVIS数据集上取得了稳定的性能表现。

*   **Multi-Modal [jcjs.siat.ac.cn]**
    *   **研究问题**: 如何通过结合文本描述和图像示例两种模态信息构建更鲁棒的分类器权重。
    *   **核心方法**: 冻结文本和视觉编码器，训练视觉特征聚合器生成视觉分类权重向量。结合大语言模型生成的类别描述和CLIP文本编码器生成文本分类权重，并通过双路径归一化融合。
    *   **关键实验结论**: 减少了训练开销，同时有效提升了目标检测的鲁棒性，特别是其Multi-Modal-2版本通过引入图像分类数据集显著提升了OVOD泛化能力。

*   **YOLO-World [cloud.tencent.com.cn], [hub.baai.ac.cn], [jcjs.siat.ac.cn]**
    *   **研究问题**: 传统YOLO系列检测器受限于预定义类别，且在大规模词汇场景下计算效率下降，如何实现实时高效的开放词汇目标检测。
    *   **核心方法**: 整合YOLOv8检测器与CLIP文本编码器，提出了可重参数化的视觉语言路径聚合网络（RepVL-PAN）和区域-文本对比损失，促进视觉和语言信息交互。YOLO-UniOW进一步引入自适应决策学习（AdaDL）策略和通配符学习（Wildcard Learning），在CLIP潜在空间中实现轻量级对齐，并动态感知未知物体。
    *   **关键实验结论**: YOLO-World在LVIS数据集上以52.0 FPS的速度取得了35.4 AP，在准确性和速度方面超越了许多先进方法。YOLO-UniOW在LVIS上达到了34.6 AP和30.0 APr，平均速度为69.6 FPS，并在多个开放世界基准测试中树立了新标杆，实现了开放世界与开放词汇检测的统一。

#### 4. 通用目标检测（Universal Object Detection）

通用目标检测是OVOD的进一步延伸，旨在检测场景中的所有物体，无论类别是否在训练中出现，并能处理异构标签空间。

*   **UniDetector [blog.csdn.net/qq_40279050]**
    *   **研究问题**: 如何构建一个能够在开放世界中识别大量类别、利用多源异构标签空间进行训练的通用目标检测器。
    *   **核心方法**: 通过图像和文本空间的对齐，利用多源异构标签空间的图像进行训练，并通过解耦训练和概率校准提升对新类别的泛化能力，提出了类别无关的本地化网络（CLN）。
    *   **关键实验结论**: 仅通过500个类别的训练后，能检测超过7000个类别；在没有对应图像的零样本场景中，比传统监督基线平均高出4%AP；在COCO上使用纯CNN模型和ResNet50网络达到49.3%AP。

### 实验与评价总结

LVIS数据集是OVOD领域常用的评估基准，其长尾分布（稀有、常见、频繁类别）很好地模拟了真实世界场景。AP（平均精度）是最常用的性能指标，而F-AP（Fixed Average Precision）则通过限制每个类别的检测数量来保障评估独立性。此外，对于通用开放世界检测，U-Recall（未知召回率）、WI（Wilderness Impact）和A-OSE（Absolute Open-Set Error）等指标用于衡量未知物体检测和误报情况。

共性趋势表明，OVOD的性能提升离不开模型规模、数据多样性与训练策略的协同。大规模图像-文本对预训练数据对提示学习和伪标注任务至关重要。视觉-语言对齐的准确性、跨模态信息的深度融合、以及应对长尾分布和“未知”物体识别的能力是各项工作共同关注的焦点。

### 趋势与挑战

2025年前后，OVOD领域将继续朝着更通用、更高效、更鲁棒的方向发展，面临以下趋势与挑战：

1.  **多模态上下文信息的深度利用与推理能力增强：** 现有研究已开始探索图像级长描述和区域级短语的生成 [blog.csdn.net/fengdu78] 或上下文信息 [jcjs.siat.ac.cn] 对OVOD的辅助作用。未来的趋势将是更深入地结合大语言模型（LLM）的推理能力，实现对复杂场景中物体间关系、属性和背景知识的理解，从而提升检测的语义准确性和泛化性。例如，结合LLM进行思维链推理 [jcjs.siat.ac.cn]，生成更详细、更精确的描述来指导目标检测。
2.  **通用基础模型的构建与参数高效微调：** OVOD模型正向着更大规模、更普适的基础模型发展，但也带来了训练和部署的高昂成本。LLMDet [blog.csdn.net/fengdu78] 等工作展示了强大的开放词汇检测器可以作为视觉基础模型与LLM结合构建更强的多模态模型。未来的研究将致力于开发更加参数高效的学习策略，如LoRA [cloud.tencent.com.cn]、提示学习等，使大型OVOD模型能够在资源受限的环境下进行有效部署和适应新任务，同时避免灾难性遗忘。
3.  **弱监督/自监督学习范式与数据质量提升：** 尽管VLM提供了丰富的预训练知识，但高质量区域级标注数据依然稀缺且昂贵。利用无标注或弱标注数据进行伪标注生成 [jcjs.siat.ac.cn] 仍是重要方向。未来的趋势将关注：1) 发展更智能的伪标注生成技术和噪声缓解策略，提高伪标注的准确性和鲁棒性。2) 探索无大规模数据支持下更高效的模型架构和训练算法，以适应低资源配置下的OVOD应用。3) 结合人类反馈（Human-in-the-Loop）机制，实现数据-模型-人类的迭代优化，进一步提高数据质量，降低标注成本。

### 结论

开放词汇目标检测是计算机视觉领域一个充满活力且具有深远意义的研究方向。2022-2025年的研究取得了显著进展，通过深度融合视觉与语言模态，并结合知识蒸馏、先进预训练和高效微调策略，OVOD模型在识别训练集中未见类别方面展现出前所未有的能力。尽管在处理复杂场景、长尾分布和通用性方面仍面临挑战，但随着多模态基础模型和参数高效学习技术的不断发展，OVOD有望在未来几年内实现更广泛、更智能的实际应用。

### 参考文献

1.  [blog.csdn.net] Fu, S., Yang, Q., Mo, Q., Yan, J., Wei, X., Meng, J., Xie, X., & Zheng, W.-S. (2025). LLMDet: Learning Strong Open-Vocabulary Object Detectors under the Supervision of Large Language Models. *CVPR 2025*.
2.  [cloud.tencent.com.cn] CoovallyAIHub. (2025). 统一开放世界与开放词汇检测：YOLO-UniOW无需增量学习的高效通用开放世界目标检测框架. *腾讯云开发者社区*.
3.  [hub.baai.ac.cn] Cheng, T., Song, L., Ge, Y., Liu, W., Wang, X., & Shan, Y. (2024). YOLO-World: Real-Time Open-Vocabulary Object Detection. *智源社区论文*.
4.  [blog.csdn.net/qq_40279050] Javier.Lin_HUST. (2024). [论文翻译]Detecting Everything in the Open World: Towards Universal Object Detection. *CSDN博客*.
5.  [blog.csdn.net/m0_55898550] SERGIOLI0903. (2025). Grounding DINO: Marrying DINO with Grounded Pre-Training for Open-Set Object Detection 论文初读. *CSDN博客*.
6.  [opendeep.wiki] IDEA-Research. (2025). Grounded Object Detection原理 | IDEA-Research/GroundingDINO.
7.  [blog.csdn.net/CVHub] CVHub. (2025). 基于 DETR 的开放世界目标检测. *CSDN博客*.
8.  [jcjs.siat.ac.cn] 张胜, & 程俊. (2025). 基于上下文信息和大语言模型的开放词汇室内三维目标检测. *宇航计测技术*, *45*(5).
9.  [blog.csdn.net/m1024292777] m1024292777. (2024). 浅谈开放词汇目标检测. *CSDN博客*.
10. [yhjcjs.spacejournal.cn] 王秀东, 崔毅, 姜华杰, & 田瑞蛟. (2025). 开放词汇目标检测研究进展. *宇航计测技术*, *45*(5).
11. [jcjs.siat.ac.cn] Gu, X., Lin, T. Y., Kuo, W., et al. (2022). Open-vocabulary object detection via vision and language knowledge distillation. *International Conference on Learning Representations*.
12. [jcjs.siat.ac.cn] Li, L., Miao, J., Shi, D., et al. (2023). Distilling DETR with visual-linguistic knowledge for open-vocabulary object detection. *Proceedings of the IEEE/CVF International Conference on Computer Vision*.
13. [jcjs.siat.ac.cn] Zhao, X., Liu, X., Wang, D., et al. (2024). Scene-adaptive and region-aware multi-modal prompt for open vocabulary object detection. *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition*.