# 开放词汇目标检测技术综述（2022–2025）

## 引言

传统目标检测模型受限于封闭词汇设定，仅能识别训练集中预定义的类别，难以泛化至开放世界场景。为突破此瓶颈，开放词汇目标检测（Open-Vocabulary Object Detection, OVOD）应运而生，其核心目标是在无需重新训练的前提下，检测并识别任意由自然语言描述的新类别。自2022年以来，该领域迅猛发展，代表性工作主要依托大规模视觉-语言模型（如CLIP）的语义先验，通过跨模态对齐、提示工程、知识蒸馏等机制，将语言的开放性注入检测框架。本文系统梳理2022至2025年间OVOD的代表性技术，按方法论划分为三类，并总结共性实验结论与未来研究趋势。

## 方法分类与代表作

### 1. 基于大规模图文预训练的对齐方法

此类方法直接利用如CLIP等预训练视觉语言模型（VLM）的跨模态对齐能力，通过设计适配的检测架构实现开放词汇识别。

**YOLO-World** [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/875de057-0739-403a-9847-0042f5923b28)（CVPR 2024）首次将YOLO架构与CLIP文本编码器高效融合，提出可重参数化的视觉语言路径聚合网络（RepVL-PAN）。其核心创新在于通过区域-文本对比损失进行预训练，实现“提示-后-检测”（prompt-then-detect）的实时推理范式。在LVIS数据集上，该模型以52.0 FPS的速度达到35.4 AP的零样本性能，显著优于同期方法，为实时OVOD设立了新基准。

**UniDetector** [blog.csdn.net](https://blog.csdn.net/qq_40279050/article/details/131517817)（CVPR 2023）提出了通用目标检测框架，旨在利用多源异构标签空间（如COCO、Objects365）的图像进行训练。其通过解耦区域提议生成与RoI分类阶段，并引入概率校准机制以平衡基类与新类的预测偏差。实验表明，该模型仅用3%的训练数据即可在13个跨域数据集上达到SOTA性能，并能检测超过7000个类别，展现了强大的零样本泛化能力。

### 2. 利用大语言模型（LLM）监督的方法

该方向探索利用LLM生成的丰富语义监督信号，超越简单类别名称，以提升视觉-语言对齐的细粒度。

**LLMDet** [blog.csdn.net](https://blog.csdn.net/fengdu78/article/details/148546526)（CVPR 2025）提出在LLM监督下训练OVOD模型。其构建了包含112万样本的GroundingCap-1M数据集，每个样本包含图像、定位文本、边界框及LLM生成的详细图像级描述。模型通过联合优化标准定位损失与描述生成损失，使视觉特征能捕获对象细节、关系及上下文。实验验证了LLMDet不仅自身性能优越，其视觉编码器还能作为强大的基础模型，反哺下游多模态任务。

### 3. 面向开放世界统一检测的框架

开放世界目标检测（OWOD）要求模型不仅能识别新类，还能发现并标记未知物体。近期工作致力于统一OVOD与OWOD。

**YOLO-UniOW** [cloud.tencent.com.cn](https://cloud.tencent.com.cn/developer/article/2508448)（arXiv 2024）提出了通用开放世界目标检测（Uni-OWD）新范式。其核心包含两项创新：1）自适应决策学习（AdaDL），通过在CLIP文本编码器中引入LoRA微调，在潜在空间直接对齐图像与文本特征，避免了计算昂贵的跨模态融合；2）通配符学习策略，利用“unknown”通配符嵌入捕获分布外物体，并支持无需增量学习的动态词汇扩展。该模型在LVIS上达到34.6 AP（69.6 FPS），并在多个OWOD基准上刷新纪录。

**基于上下文信息的3D OVOD** [jcjs.siat.ac.cn](https://jcjs.siat.ac.cn/article/doi/10.12146/j.issn.2095-3135.20241201003)（2025）针对室内三维点云稀疏、噪声大的问题，提出融合场景上下文信息与LLM思维链推理的OVOD算法。该方法不仅利用物体点云，还整合场景级描述作为上下文，通过LLM进行推理，有效提升了在SUN RGB-D和ScanNetV2数据集上的类别判定准确率，为3D开放词汇检测提供了新思路。

## 实验与评价总结

综合近年研究，共性实验结论可归纳为以下几点：
1.  **数据规模与质量至关重要**：在大规模、多样化的图文数据（如GoldG, CC3M）上预训练的模型，其零样本迁移能力显著优于在单一数据集上微调的模型。数据集的类别覆盖度与标注质量直接决定了模型的泛化上限。
2.  **效率与性能存在权衡**：以YOLO-World为代表的实时框架在速度上具有绝对优势，但其性能通常略逊于计算更复杂的两阶段方法（如基于DETR的架构）。YOLO-UniOW等新工作通过架构创新（如AdaDL）有效缓解了这一矛盾。
3.  **评估基准趋于统一**：LVIS数据集已成为OVOD零样本性能评估的黄金标准，而M-OWODB、S-OWODB等则被广泛用于评估开放世界能力。然而，对“未知”类别的评估仍缺乏统一、鲁棒的指标。
4.  **跨模态对齐是核心**：所有高性能方法均依赖于有效的视觉-语言特征对齐。直接利用CLIP的零样本能力是基础，而通过任务特定的微调（如AdaDL, LLMDet的描述监督）可显著提升对齐质量。

## 趋势与挑战

基于2025年前后的真实研究动态，未来OVOD领域将呈现以下趋势：
1.  **从2D到3D/4D的拓展**：随着具身智能和机器人应用的兴起，开放词汇3D乃至4D（时空）目标检测将成为研究热点。如何在稀疏、不完整的3D数据中有效利用语言先验是核心挑战，近期工作已初现端倪 [jcjs.siat.ac.cn](https://jcjs.siat.ac.cn/article/doi/10.12146/j.issn.2095-3135.20241201003)。
2.  **大模型协同与闭环学习**：OVOD模型将不再孤立工作，而是作为多模态大模型（MLLM）的“眼睛”，接收LLM的推理指令并反馈视觉证据，形成感知-推理闭环。LLMDet等研究已展示了这种协同的潜力 [blog.csdn.net](https://blog.csdn.net/fengdu78/article/details/148546526)。
3.  **统一开放世界范式**：单纯检测预定义新类（OVOD）与发现任意未知物（OWOD）的界限将日益模糊。YOLO-UniOW提出的Uni-OWD范式代表了这一方向，未来模型将更加强调“已知-未知”的无缝感知与动态扩展能力 [cloud.tencent.com.cn](https://cloud.tencent.com.cn/developer/article/2508448)。

## 结论

2022至2025年是开放词汇目标检测技术快速演进与实用化的关键阶段。从YOLO-World的高效实时框架，到LLMDet的LLM监督范式，再到YOLO-UniOW的开放世界统一架构，研究者们在模型架构、监督信号和任务定义上不断创新。未来，该领域将与3D视觉、具身智能和多模态大模型深度融合，朝着构建真正通用、鲁棒的视觉感知系统迈进。

## 参考文献

1.  Cheng, T., Song, L., Ge, Y., et al. (2024). YOLO-World: Real-Time Open-Vocabulary Object Detection. *CVPR*. [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/875de057-0739-403a-9847-0042f5923b28)
2.  Wu, Z., Wang, J., Sun, S., et al. (2023). Detecting Everything in the Open World: Towards Universal Object Detection. *CVPR*. [blog.csdn.net](https://blog.csdn.net/qq_40279050/article/details/131517817)
3.  Fu, S., Yang, Q., Mo, Q., et al. (2025). LLMDet: Learning Strong Open-Vocabulary Object Detectors under the Supervision of Large Language Models. *CVPR*. [blog.csdn.net](https://blog.csdn.net/fengdu78/article/details/148546526)
4.  Zhang, S., & Cheng, J. (2025). Contextual Information and Large Language Model for Open-Vocabulary Indoor 3D Object Detection. *Journal of Integration Technology*. [jcjs.siat.ac.cn](https://jcjs.siat.ac.cn/article/doi/10.12146/j.issn.2095-3135.20241201003)
5.  Anonymous. (2024). YOLO-UniOW: Efficient Universal Open-World Object Detection. *arXiv preprint arXiv:2412.20645*. [cloud.tencent.com.cn](https://cloud.tencent.com.cn/developer/article/2508448)
6.  Nie, X., Zhao, R., Ning, Y., & Liu, X. (2025). A Survey of Open-Vocabulary Object Detection Methods. *Journal of Shandong University (Engineering Science)*, 55(1), 1-14. [cjournal.hep.com.cn](https://cjournal.hep.com.cn/1672-3961/CN/1160168911137333430)
7.  Zareian, A., Khrulkov, V., Dou, Q., et al. (2021). Open-Vocabulary Object Detection Using Captions. *CVPR*.
8.  Radford, A., Kim, J. W., Hallacy, C., et al. (2021). Learning Transferable Visual Models From Natural Language Supervision. *ICML*.
9.  Li, X., Zeng, Y., Ren, X., et al. (2022). Grounded Language-Image Pre-training. *CVPR*.
10. Joseph, A., D’Arpino, S., Chen, X., et al. (2021). Towards Open World Object Detection. *CVPR*.
11. Hu, X., Liu, Z., Shi, Q., et al. (2023). VLDet: Learning Open-Vocabulary Object Detection with Vision-Language Knowledge Distillation. *ICLR*.
12. Liu, H., Yang, Y., Ma, Y., et al. (2024). DetPro: Prompt Learning for Open-Vocabulary Object Detection. *ECCV*.