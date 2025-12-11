好的，作为一名严谨的科研助手，我将基于提供的真实网络搜索结果，为您生成一篇关于“指代表达式图像分割技术”的学术综述。

***

### **指代表达式图像分割技术研究综述（2022-2025）**

#### **摘要**

指代表达式图像分割（Referring Image Segmentation, RIS）是一项旨在根据自然语言描述在图像中分割出特定对象的多模态任务。近年来，随着视觉-语言预训练模型（Vision-Language Pre-training, VLP）的兴起和对高精度、低成本分割需求的增长，该领域取得了显著进展。本综述聚焦于 2022 年至 2025 年的代表性工作，系统梳理了基于 VLP 的方法、多粒度融合方法、弱监督与通用分割方法以及后处理精调方法等关键技术分支。通过对各类别代表性论文的核心思想与实验结论进行分析，本文总结了当前主流方法的共性与局限，并对未来研究趋势，包括融合更大规模的基础模型、构建统一分割框架以及探索更弱的监督信号等方向，进行了展望。

#### **关键词**：指代表达式图像分割；多模态学习；视觉-语言模型；零样本分割；弱监督学习

***

### **1. 引言**

指代表达式图像分割（RIS）的目标是为给定的一句自然语言描述（如“左边红色的那辆车”）生成像素级别的分割掩码 [bhxb.buaa.edu.cn](https://bhxb.buaa.edu.cn/bhzk/cn/article/doi/10.13700/j.bh.1001-5965.2022.0384)。该任务融合了计算机视觉中的图像分割与自然语言处理中的指代表达式理解，在人机交互、机器人视觉、图像编辑等领域具有重要应用价值。其核心挑战在于如何有效地建立语言语义与像素级视觉特征之间的细粒度对应关系，尤其是在处理复杂场景、模糊描述以及多对象关系时。

在 2022-2025 年期间，RIS 研究呈现出两大趋势：一是深度利用大规模视觉-语言预训练模型（如 CLIP）的强大先验知识，以实现卓越的零样本和开放词汇分割能力；二是通过设计更精巧的网络结构和训练策略，解决传统方法在特征融合、边界精度和标注成本等方面的瓶颈。本综述将围绕这些前沿方向，对代表性工作进行分类、剖析与总结。

### **2. 方法分类与代表作**

#### **2.1 基于视觉-语言预训练模型 (VLP) 的方法**

这类方法是近年来的主流，它们利用在海量图文对上预训练的模型来对齐图像和文本的表示空间，极大地提升了模型的泛化和零样本能力。

*   **CRIS (CLIP-Driven Referring Image Segmentation, 2022)**
    该研究旨在解决文本与像素级特征对齐的挑战。其核心方法是受 CLIP 启发，设计了一个视觉-语言解码器来促进跨模态特征的一致性，并创新性地提出了文本到像素的对比学习损失函数 [cnblogs.com](https://www.cnblogs.com/lipoicyclic/p/16807808.html)。该损失函数直接将文本特征与相关的像素级视觉特征进行对齐，而不是仅在图像级别进行匹配。实验表明，该方法能够有效整合两种模态的信息，但也揭示了在处理歧义性表达和严重遮挡等复杂情况时仍面临挑战。

*   **LSeg (Language-Driven Semantic Segmentation, 2022)**
    LSeg 探索了将预训练的 VLP 模型直接用于零样本和少样本语义分割的可行性。其方法十分简洁：固定 CLIP 强大的文本编码器权重，仅训练一个基于 Transformer 的图像编码器，将图像像素嵌入到与文本标签相同的特征空间中 [cnblogs.com](https://www.cnblogs.com/xiaxuexiaoab/p/18778839)。分割任务通过计算像素嵌入与各类别文本嵌入之间的相似度（点积）完成。关键实验结论显示，LSeg 在 PASCAL-5i 和 COCO-20i 等数据集上的零样本性能优于此前的基线方法，证明了 VLP 模型在密集预测任务中的巨大潜力。

*   **PixelCLIP (2025)**
    该工作针对 CLIP 在迁移至像素级任务时会丢失空间位置信息的根本问题，提出了一个零样本 RIS 模型。PixelCLIP 通过融合多尺度的图像特征，同时保留了 CLIP 固有的图像整体语义与像素级的空间信息 [arocmag.cn](https://www.arocmag.cn/language?lang=en&returnUrl=%2Fabs%2F2024.06.0254)。在文本理解上，它结合了 CLIP-BERT 和大型语言模型 LLaVA，以注入更丰富的对象类别及上下文知识。实验验证了该模型通过细粒度跨模态关联，有效实现了像素水平的零样本分割。

#### **2.2 多粒度与上下文特征融合方法**

这类方法专注于设计更复杂的网络结构，以融合不同层次的视觉特征，并结合上下文信息来更精确地理解指代表达式。

*   **语言引导的多粒度特征融合目标分割方法 (2022)**
    该研究基于 Refvos 模型进行改进，旨在实现对特定指代目标的更精准定位。它采用 Swin Transformer 和 BERT 分别提取多粒度的视觉特征和文本特征，然后将文本特征与不同粒度的视觉特征进行融合，以语言为导向增强目标表达 [bhxb.buaa.edu.cn](https://bhxb.buaa.edu.cn/bhzk/cn/article/doi/10.13700/j.bh.1001-5965.2022.0384)。最终，通过一个卷积长短期记忆网络（ConvLSTM）优化融合后的多粒度特征，促进了不同粒度特征间的信息交流。与基线模型 Refvos 相比，该方法在 UNC 和 UNC+ 数据集上取得了 0.63% 到 4.1% 不等的 IoU 提升。

#### **2.3 弱监督与通用分割方法**

为了降低高昂的像素级标注成本并扩展模型的适用范围，研究者们开始探索弱监督学习和能够处理多种分割任务的通用框架。

*   **Shatter and Gather (2023)**
    此工作致力于解决像素级标注数据稀缺的问题，提出了一种仅使用文本描述作为监督源的弱监督学习方法。其模型首先在图像中自动发现潜在的语义实体（“Shatter”），然后根据输入文本查询的引导，将相关的实体掩码组合起来（“Gather”），生成最终的分割结果 [blog.csdn.net](https://blog.csdn.net/wzk4869/article/details/132752912)。通过设计一种新的损失函数，模型可在无像素级标注的情况下进行端到端训练。在四个公开基准测试上，该方法显著优于其他同类弱监督方法及当时的开放词汇分割模型。

*   **OneFormer (2022)**
    OneFormer 提出了一种通用的图像分割框架，旨在用一个模型统一处理语义、实例和全景分割任务。其核心思想是设计一个任务驱动的联合训练策略，并通过引入一个“任务 Token”来动态调节模型行为，使其在推理时能执行特定任务 [zhuanzhi.ai](https://zhuanzhi.ai/paper/1d4ac341cec84f3c13bf6422ef9bee4f)。尽管 OneFormer 并非专为 RIS 设计，但它的“一次训练，全能分割”理念代表了分割领域的重要趋势，即构建可灵活适应包括 RIS 在内的多种密集预测任务的统一架构。其实验表明，单个 OneFormer 模型在 ADE20k、Cityscapes 和 COCO 上的表现全面优于专门为各项任务训练的 Mask2Former。

#### **2.4 后处理与精调方法**

这类方法独立于主分割模型，专注于对粗糙的分割结果进行迭代优化，以提升边界质量和细节精度。

*   **SegRefiner (2023)**
    SegRefiner 提出了一种模型无关的分割精调框架，其创新性地将该任务视为一个去噪过程。该方法将任何分割模型输出的粗糙掩码视作真值的“带噪版本”，并利用扩散模型（Diffusion Model）对其进行迭代修正 [cnblogs.com](https://www.cnblogs.com/wxkang/p/17940897)。通过一个基于随机状态转移的离散扩散过程，SegRefiner 能够在每一步中修正部分“最明显的错误”，从而逐步逼近高精度的分割结果。实验表明，SegRefiner 能够显著提升多种现有分割模型（包括实例分割和语义分割）在多个高质量数据集上的 IoU 和边界准确度。

### **3. 实验与评价总结**

*   **数据集与评价指标**：RIS 任务的性能评估主要在 UNC、UNC+、G-Ref 和 ReferIt 等标准数据集上进行。核心评价指标为交并比（Intersection over Union, IoU），有时也使用在不同 IoU 阈值下的精确率（Precision@X）进行更细致的分析。

*   **共性结论**：
    1.  **VLP 模型的有效性**：基于 CLIP 等 VLP 模型的 RIS 方法（如 CRIS, LSeg, PixelCLIP）普遍展示了强大的零样本和开放词汇能力。它们能够识别训练集中未见过的对象类别，这是传统依赖固定词汇表的分割模型难以做到的。
    2.  **多粒度融合的必要性**：结合高层的全局语义信息与底层的局部细节特征是提升分割精度的关键，尤其是在处理涉及精细结构和复杂空间关系的指代语时。如“语言引导的多粒度特征融合目标分割方法”所示，显式地建模并融合多尺度特征能带来显著的性能增益 [bhxb.buaa.edu.cn](https://bhxb.buaa.edu.cn/bhzk/cn/article/doi/10.13700/j.bh.1001-5965.2022.0384)。
    3.  **弱监督学习的潜力与挑战**：以“Shatter and Gather”为代表的弱监督方法证明了仅用文本监督进行 RIS 训练的可行性，有效降低了对像素级标注的依赖。但其生成的掩码精度与全监督方法相比仍有差距，尤其是在对象边界的准确性上。
    4.  **分割精度的分阶段提升**：以 SegRefiner 为代表的精调模型表明，将 RIS 分解为“粗略定位”和“边界精调”两个阶段是提升最终性能的有效策略。这类模型无关的方法可作为即插即用模块，进一步提升任意 RIS 模型的输出质量。

### **4. 趋势与挑战**

基于 2022-2025 年的研究进展，RIS 领域未来的发展将可能集中在以下几个方面：

1.  **融合更强大的基础模型**：随着大型语言模型（LLM）和更大规模的视觉基础模型（如 LLaVA, GPT-4V）的出现，未来的 RIS 研究将不仅限于利用 CLIP。通过融合这些具备更强常识推理和复杂指令遵循能力的大模型，RIS 系统有望更好地理解包含复杂逻辑、多步推理和世界知识的自然语言描述（如“图中看起来最古老的建筑”），这将是突破当前语义理解瓶颈的关键 [arocmag.cn](https://www.arocmag.cn/language?lang=en&returnUrl=%2Fabs%2F2024.06.0254)。

2.  **构建统一、通用的分割框架**：受 OneFormer 等工作的启发，未来的研究趋势将倾向于构建能够处理多种分割任务（包括语义分割、实例分割、全景分割、RIS 乃至视频对象分割）的单一模型 [zhuanzhi.ai](https://zhuanzhi.ai/paper/1d4ac341cec84f3c13bf6422ef9bee4f)。这种“一模型通吃”的框架不仅能提高研发效率，还能通过多任务学习促进不同任务间的知识迁移，从而提升模型在单一任务上的性能。

3.  **探索更弱、更多样的监督信号**：为了彻底解决像素级标注的瓶颈，研究将继续深入探索更弱的监督形式。除了已有的文本级监督 [blog.csdn.net](https://blog.csdn.net/wzk4869/article/details/132752912)，未来可能还会探索利用包围框（Bounding Box）、点击、涂鸦等低成本交互进行混合监督的训练范式。将交互式分割与指代式分割相结合，有望在保证精度的同时大幅降低标注成本 [lin-zheng.com](https://lin-zheng.com/paper/22_ACMMM_MMIIS/22_ACMMM_MMIIS_Paper_CN.pdf)。

4.  **利用生成模型进行掩码生成与精调**：以 SegRefiner 为代表的扩散模型已在分割精调任务中展现出巨大潜力 [cnblogs.com](https://www.cnblogs.com/wxkang/p/17940897)。未来，生成模型（尤其是扩散模型）的应用将更加深入。一方面，可以探索将其用于直接从噪声中生成分割掩码，以图像和文本为条件进行引导；另一方面，可以利用其强大的生成先验来修复被遮挡或不完整对象的分割结果。

### **5. 结论**

在 2022 年至 2025 年间，指代表达式图像分割领域的研究取得了长足进步，其发展范式已从传统的特征工程和编解码器设计，转向深度依赖大规模预训练模型，并积极探索更高效、低成本的解决方案。当前，基于 VLP 的方法已成为主流，而多粒度融合、弱监督学习和后处理精调等技术方向也展现出强大的生命力。展望未来，随着更强大的基础模型和生成模型的涌现，RIS 技术将在理解能力、任务通用性和标注效率方面迎来新的突破，向着更智能、更实用的方向持续演进。

### **6. 参考文献**

1.  [cnblogs.com](https://www.cnblogs.com/lipoicyclic/p/16807808.html) Wang, Z., Li, J., et al. "CRIS: CLIP-Driven Referring Image Segmentation." *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*, 2022.
2.  [blog.csdn.net](https://blog.csdn.net/wzk4869/article/details/132752912) Lee, H. G., et al. "Shatter and Gather: Learning Referring Image Segmentation with Text Supervision." *arXiv preprint arXiv:2308.15512*, 2023.
3.  [arocmag.cn](https://www.arocmag.cn/language?lang=en&returnUrl=%2Fabs%2F2024.06.0254) 刘杰, 乔文昇, 等. "基于图像-文本大模型CLIP微调的零样本参考图像分割." *计算机应用研究*, 2025.
4.  [cnblogs.com](https://www.cnblogs.com/wxkang/p/17940897) Wang, M., et al. "SegRefiner: High-Precision Image Segmentation via Diffusion Models." *Advances in Neural Information Processing Systems (NeurIPS)*, 2023.
5.  [bhxb.buaa.edu.cn](https://bhxb.buaa.edu.cn/bhzk/cn/article/doi/10.13700/j.bh.1001-5965.2022.0384) 谭荃戈, 王蓉, 吴澳. "语言引导的多粒度特征融合目标分割方法." *北京航空航天大学学报*, 2024.
6.  [zhuanzhi.ai](https://zhuanzhi.ai/paper/1d4ac341cec84f3c13bf6422ef9bee4f) Jain, J., Li, J., et al. "OneFormer: One Transformer to Rule Universal Image Segmentation." *European Conference on Computer Vision (ECCV)*, 2022.
7.  [cnblogs.com](https://www.cnblogs.com/xiaxuexiaoab/p/18778839) Li, B., et al. "Language-driven Semantic Segmentation." *International Conference on Learning Representations (ICLR)*, 2022.
8.  [jcad.cn](https://www.jcad.cn/article/doi/10.3724/SP.J.1089.2023-00091) 杨大伟, 迟津生, 毛琳. "多重边界参考的弱监督语义分割网络." *计算机辅助设计与图形学学报*, 2024.
9.  [lin-zheng.com](https://lin-zheng.com/paper/22_ACMMM_MMIIS/22_ACMMM_MMIIS_Paper_CN.pdf) Lin, Z., et al. "Multi-modal Interactive Image Segmentation." *Proceedings of the 30th ACM International Conference on Multimedia (MM '22)*, 2022.
10. [blog.csdn.net](https://blog.csdn.net/imwaters/article/details/144055641) Zheng, P., et al. "BiRefNet: Bilateral Reference for High-Resolution Dichotomous Image Segmentation." *arXiv preprint arXiv:2401.03407*, 2024.
11. Yu, L., et al. "Modeling context in referring expressions." *European conference on computer vision (ECCV)*, 2016.
12. Hui, T., et al. "Linguistic structure guided context modeling for referring image segmentation." *European conference on computer vision (ECCV)*, 2020.
13. Li, R., et al. "Referring image segmentation via recurrent refinement networks." *Proceedings of the IEEE/CVF conference on computer vision and pattern recognition (CVPR)*, 2018.