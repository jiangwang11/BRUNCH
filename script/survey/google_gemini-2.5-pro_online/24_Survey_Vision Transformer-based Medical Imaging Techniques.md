好的，作为一名严谨的科研助手，我将基于提供的真实网络搜索结果，为您生成一篇关于“基于视觉Transformer的医学影像技术”的中文学术综述。

***

### **面向精准诊疗的视觉Transformer医学影像分析技术年度进展(2022-2025)综述**

**摘要：** 近年来，视觉Transformer（Vision Transformer, ViT）凭借其卓越的全局依赖建模能力，在医学影像分析领域引发了范式革新。本综述聚焦于2022至2025年间，系统梳理并评述了基于ViT的医学影像技术代表性工作。本文首先介绍了ViT在医学影像领域的研究背景与动因；然后，从纯Transformer架构、CNN-Transformer混合架构及超越Transformer的新兴架构三个维度对代表性方法进行分类与解析；接着，归纳总结了这些方法在公开基准数据集上的共性实验表现与评价模式；最后，基于最新研究动向，对未来技术趋势与尚待解决的挑战进行了展望。

### **1. 引言**

长期以来，以U-Net为代表的卷积神经网络（CNN）是医学影像分割与分类任务的主流范式 [opticsjournal.net](https://www.opticsjournal.net/Articles/OJ2b2078a8cf027f69/km)。然而，CNN固有的局部感受野特性限制了其对图像长程依赖关系的捕获能力，这在处理形态多变、边界模糊的大尺寸器官或肿瘤时表现出局限性 [pdf.hanspub.org](https://pdf.hanspub.org/mos2025141_372572027.pdf)。

受自然语言处理领域Transformer模型成功的启发，研究者们将其引入计算机视觉，提出了视觉Transformer（ViT）架构。ViT通过将图像切分为块（Patches）并将其视为序列，利用自注意力（Self-Attention）机制直接建模全局上下文信息，有效克服了CNN的感受野限制 [blog.csdn.net](https://blog.csdn.net/qq_38296005/article/details/119830386)。从2022年起，ViT及其变体在医学影像分析领域迅速发展，尤其是在3D volumetric数据处理、多模态信息融合以及自监督学习等方面展现出巨大潜力，逐步推动了肿瘤精准诊疗范式的革新 [xhyxzz.pumch.cn](https://xhyxzz.pumch.cn/article/doi/10.12290/xhyxzz.2025-0328?viewType=citedby-info)。本综述旨在对这一时期的关键技术进展进行梳理与总结。

### **2. 方法分类与代表作**

根据架构设计理念，2022-2025年的主流ViT医学影像技术可分为三类：纯Transformer架构、CNN-Transformer混合架构以及超越Transformer的新兴架构。

#### **2.1 纯Transformer架构**

此类方法完全或主要依赖Transformer作为特征提取器，旨在充分利用其全局建模能力。

*   **UNETR (Transformers for 3D Medical Image Segmentation)**
    *   **研究问题**：如何将Transformer完全作为3D医学影像分割任务的编码器，以替代传统的CNN编码器。
    *   **核心方法**：该模型首次提出将3D影像分割视为一个序列到序列的预测问题。它将输入的3D体素数据划分为均匀的、不重叠的块序列，并直接送入一个标准的ViT编码器中学习其上下文表示。编码器在不同分辨率下的特征通过跳跃连接（Skip-Connection）与一个纯卷积结构的解码器相连，以恢复局部空间信息并生成分割图 [blog.csdn.net](https://blog.csdn.net/qq_38296005/article/details/119830386)。
    *   **关键结论**：在MSD（Medical Segmentation Decathlon）数据集的脑肿瘤和脾脏分割任务上，UNETR证明了纯Transformer编码器在捕获全局多尺度信息方面的有效性，为后续研究开辟了新路径 [blog.csdn.net](https://blog.csdn.net/qq_38296005/article/details/119830386)。

#### **2.2 CNN-Transformer混合架构**

混合架构是当前的主流，旨在结合CNN强大的局部特征提取能力和Transformer卓越的全局上下文建模能力。

*   **Swin UNETR (Self-Supervised Pre-Training of Swin Transformers for 3D Medical Image Analysis)**
    *   **研究问题**：如何设计一个计算高效且能从大量无标签数据中学习的3D医学影像分析框架，以减少对昂贵人工标注的依赖。
    *   **核心方法**：Swin UNETR采用具有分层结构和移位窗口机制的Swin Transformer作为编码器，相比标准ViT，其计算复杂度呈线性增长，更适合于分割等稠密预测任务。该框架的关键创新在于其自监督预训练方案，通过在5050张公开CT图像上执行图像修复、旋转预测等借口任务（pretext tasks），使模型在微调前就学习到强大的通用表征 [developer.nvidia.cn](https://developer.nvidia.cn/blog/novel-transformer-model-achieves-state-of-the-art-benchmarks-in-3d-medical-image-analysis/)、[medium.com](https://medium.com/@s93011/swinunetr-swin-transformer%E7%9A%84self-supervise%E9%A0%90%E8%A8%93%E7%B7%B4%E7%94%A8%E6%96%BC3d%E9%86%AB%E5%AD%B8%E5%BD%B1%E5%83%8F%E5%88%86%E6%9E%90-475537b560f5)。
    *   **关键结论**：在BTCV和MSD等公开排行榜上，Swin UNETR取得了当时最先进（SOTA）的分割精度，例如在BTCV多器官分割挑战中平均Dice达到0.918，尤其在胰腺、肾上腺等小器官分割上提升显著 [developer.nvidia.cn](https://developer.nvidia.cn/blog/novel-transformer-model-achieves-state-of-the-art-benchmarks-in-3d-medical-image-analysis/)。

*   **MCT-Net (Mix CNN-Transformer Multi-scale Feature Network)**
    *   **研究问题**：如何有效融合CNN的细节捕捉能力和Transformer的全局感知能力，以解决肝脏肿瘤边界模糊、尺寸形态多变的问题。
    *   **核心方法**：MCT-Net设计了一个创新的双分支并行编码器。一个分支是基于深度可分离卷积的CNN编码器，嵌入局部空间注意力（LAM）以精细提取肿瘤边缘轮廓；另一个分支是引入了多轴自注意力（Max-SA）的Transformer编码器，以获取更大的感受野。解码器部分通过多尺度信息交互模块（MSIF）实现跨分支、跨尺度的特征融合 [pdf.hanspub.org](https://pdf.hanspub.org/mos2025141_372572027.pdf)。
    *   **关键结论**：在LiTS2017肝脏肿瘤分割数据集上，MCT-Net的Dice系数达到72.16%，平均表面距离（ASD）为3.380 mm，优于U-Net、TransUNet等基线模型，证明了其双编码器并行融合策略的有效性 [pdf.hanspub.org](https://pdf.hanspub.org/mos2025141_372572027.pdf)。

*   **跨模态PET/CT图像Transformer分割模型**
    *   **研究问题**：在多模态医学影像（如PET/CT）中，如何高效融合不同模态提供的互补信息（解剖结构与功能代谢），以提升病灶分割精度。
    *   **核心方法**：该模型设计了多分支编码器，包括PET/CT主干分支及独立的PET和CT辅助分支，以分别提取模态特有及融合特征。其在跳跃连接部分设计了“跨模态跨维度”注意力模块，从模态和空间维度两个角度捕获跨模态的有效信息。瓶颈层则构建了跨尺度Transformer模块，自适应地融合深层语义与浅层空间信息 [jeit.ac.cn](https://jeit.ac.cn/cn/article/doi/10.11999/JEIT221204)。
    *   **关键结论**：在临床多模态肺部病灶数据集上，该模型的Dice系数达到95.32%，MIoU为90.14%，显著优于单模态U-Net (Dice 87.98%)，证明了其在处理多模态数据上的优越性 [jeit.ac.cn](https://jeit.ac.cn/cn/article/doi/10.11999/JEIT221204)。

#### **2.3 超越Transformer的新兴架构**

为解决ViT的二次计算复杂度瓶颈，研究者开始探索性能与效率兼备的新架构。

*   **MedMamba (基于视觉Mamba的医学图像分类模型)**
    *   **研究问题**：如何设计一种既具备全局感受野，又具有线性计算复杂度的新型视觉骨干网络，以突破ViT模型在计算效率上的瓶颈。
    *   **核心方法**：MedMamba是首款将状态空间模型（State Space Model, SSM），特别是Mamba架构，应用于医学视觉任务的模型。Mamba通过选择性扫描机制（SSM）和硬件感知的并行算法，以线性复杂度实现了对长序列依赖的建模。MedMamba采用四向扫描策略来处理2D图像，确保每个像素都能关联到图像的全部信息，有效替代了ViT中的自注意力模块 [xugj520.cn](https://www.xugj520.cn/archives/medmamba-medical-image-classification.html)。
    *   **关键结论**：在MICCAI 2025基准测试中，MedMamba在9个医学影像数据集上平均准确率达到93.7%，比CNN-ViT混合模型高3.2%。同时，其推理速度（224x224图像仅38ms）和内存消耗均显著优于ViT，展现了作为下一代视觉骨干的巨大潜力 [xugj520.cn](https://www.xugj520.cn/archives/medmamba-medical-image-classification.html)。

### **3. 实验与评价总结**

*   **基准数据集与评价指标**：代表性工作普遍在公开的大型数据集上进行评测，如**医学分割十项全能（MSD）**、**超越颅穹窿（BTCV）**多器官分割、**LiTS (肝脏肿瘤分割)**等 [developer.nvidia.cn](https://developer.nvidia.cn/blog/novel-transformer-model-achieves-state-of-the-art-benchmarks-in-3d-medical-image-analysis/)、[pdf.hanspub.org](https://pdf.hanspub.org/mos2025141_372572027.pdf)。评价指标主要沿用传统分割任务的标准，包括衡量区域重叠度的**Dice相似系数（Dice）**、**交并比（IoU/mIoU）**，以及衡量边界吻合度的**平均表面距离（ASD）** [jeit.ac.cn](https://jeit.ac.cn/cn/article/doi/10.11999/JEIT221204)。

*   **共性结论**：
    1.  **性能优势**：无论采用纯Transformer编码器还是混合架构，基于Transformer的模型在各项指标上普遍优于仅依赖CNN的基线模型（如U-Net、Attention U-Net）。这归因于Transformer能够有效建模长距离依赖，对于分割形态不规则、尺寸变化大的病灶或器官具有天然优势 [jeit.ac.cn](https://jeit.ac.cn/cn/article/doi/10.11999/JEIT221204)。
    2.  **数据效率**：通过在大规模无标签医学影像上进行自监督预训练（如Swin UNETR），模型可以学习到鲁棒的视觉表征，从而显著减少对下游任务昂贵标注数据的依赖，在小样本场景下依然能保持较高性能。已有研究表明，预训练模型可将所需标注数据量减少40%以上 [medium.com](https://medium.com/@s93011/swinunetr-swin-transformer%E7%9A%84self-supervise%E9%A0%90%E8%A8%93%E7%B7%B4%E7%94%A8%E6%96%BC3d%E9%86%AB%E5%AD%B8%E5%BD%B1%E5%83%8F%E5%88%86%E6%9E%90-475537b560f5)。
    3.  **计算效率**：标准ViT的二次方计算复杂度是其应用于高分辨率3D医学影像的主要障碍。因此，具备分层结构和线性复杂度的**Swin Transformer**成为混合架构的主流选择，而**MedMamba**等新兴的线性复杂度模型则被视为解决该瓶颈的未来方向 [developer.nvidia.cn](https://developer.nvidia.cn/blog/novel-transformer-model-achieves-state-of-the-art-benchmarks-in-3d-medical-image-analysis/)、[xugj520.cn](https://www.xugj520.cn/archives/medmamba-medical-image-classification.html)。

### **4. 趋势与挑战**

展望2025年前后，ViT医学影像技术正呈现以下三大关键趋势，并伴随着相应的挑战：

1.  **架构创新：从Transformer到状态空间模型（SSM）**
    *   **趋势**：以Mamba为代表的SSM正成为ViT的有力竞争者和替代方案。MedMamba的成功表明，SSM能够在保持全局感受野的同时，实现线性计算复杂度和更低的内存占用，完美契合了医学影像高分辨率、高维度的特性。未来将有更多研究探索将SSM应用于更广泛的医学任务，如3D分割、多模态融合、病理学全切片分析等 [xugj520.cn](https://www.xugj520.cn/archives/medmamba-medical-image-classification.html)。
    *   **挑战**：SSM的理论基础与深度学习社区熟悉的Attention机制差异较大，其可解释性、对不同模态数据的适应性以及更深层次的理论优势仍需进一步探索和验证。

2.  **多模态融合：从影像-影像到影像-文本的深度对齐**
    *   **趋势**：研究重点正从单一影像模态或影像间融合（如PET/CT），转向影像与文本（如放射学报告、电子病历）的深度语义对齐。以大语言模型（LLM）驱动的跨模态哈希、报告生成、语义检索等成为前沿方向 [jeit.ac.cn](https://www.jeit.ac.cn/cn/article/doi/10.11999/JEIT250529?viewType=HTML)。通过LLM的语义理解与生成能力，可以实现对医学影像更深层次的语义挖掘，并以提示指令（Prompt）等方式实现更灵活的人机交互与模型微调。
    *   **挑战**：构建高质量、大规模的“影像-报告”配对数据集是核心瓶颈。同时，如何有效对齐视觉特征空间与LLM的语言嵌入空间，以及如何确保生成内容的医学准确性和可靠性，是亟待解决的技术难题。

3.  **基础模型（Foundation Model）范式的兴起**
    *   **趋势**：借鉴NLP领域GPT模型的成功，医学影像领域正朝着构建“视觉基础模型”的方向发展。这一范式旨在通过在海量、多源、无标签的医学影像上进行大规模自监督预训练，打造一个通用视觉编码器。该模型一旦训练完成，便可通过少量样本或零样本提示的方式，快速适应各种下游任务（如不同器官的分割、不同疾病的分类等）[xhyxzz.pumch.cn](https://xhyxzz.pumch.cn/article/doi/10.12290/xhyxzz.2025-0328?viewType=citedby-info)。Swin UNETR的成功已初步验证了这一思路的可行性。
    *   **挑战**：基础模型的构建需要巨大的算力资源与前所未有规模的医疗数据集，这对多数研究机构构成巨大障碍。此外，医疗数据的隐私性、标准化以及跨机构共享的困难，也为基础模型的实现带来了现实挑战。

### **5. 结论**

在2022至2025年间，基于视觉Transformer的医学影像分析技术取得了长足进步。从最初替代CNN编码器，到发展出精巧的混合架构，再到探索超越Transformer的新型模型，ViT及其衍生技术已成为推动领域发展的核心动力。它们不仅在各项基准测试中刷新了性能记录，更在多模态融合、自监督学习等方面展现了巨大潜力。尽管在计算效率、数据依赖和模型泛化性上仍面临挑战，但随着状态空间模型、大语言模型融合以及基础模型范式的持续演进，我们有理由相信，新一代的智能医学影像技术将为实现更精准、高效的临床诊疗提供前所未有的强大工具。

### **6. 参考文献**

1.  尹艺晓, 马金刚, 张文凯, 等. 从U-Net到Transformer：混合模型在医学图像分割中的应用进展[J]. 激光与光电子学进展, 2025, 62(2): 0200001. [opticsjournal.net](https://www.opticsjournal.net/Articles/OJ2b2078a8cf027f69/km)
2.  周涛, 党培, 陆惠玲, 等. 跨模态跨尺度跨维度的PET/CT图像的Transformer分割模型[J]. 电子与信息学报, 2023, 45(10): 3529-3537. [jeit.ac.cn](https://jeit.ac.cn/cn/article/doi/10.11999/JEIT221204)
3.  Hatamizadeh, A., Nath, V., Tang, Y., et al. Swin UNETR: Swin Transformers for Semantic Segmentation of Brain Tumors in MRI Images. In *International MICCAI Brainlesion Workshop*, 2021: 272-284. (The NVIDIA blog [developer.nvidia.cn] and Medium article [medium.com] reference this lineage of work, culminating in the CVPR 2022 paper on self-supervised pre-training).
4.  Hatamizadeh, A., Tang, Y., Nath, V., et al. Self-Supervised Pre-Training of Swin Transformers for 3D Medical Image Analysis. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*, 2022: 18739-18750.
5.  Hatami, A., et al. UNETR: Transformers for 3D Medical Image Segmentation. In *2022 IEEE/CVF Winter Conference on Applications of Computer Vision (WACV)*. [blog.csdn.net](https://blog.csdn.net/qq_38296005/article/details/119830386)
6.  汤文超, 丁德锐, 袁浩成, 等. 一种混合CNN-Transformer多尺度特征的肝脏肿瘤分割网络[J]. 建模与仿真, 2025, 14(1): 388-403. [pdf.hanspub.org](https://pdf.hanspub.org/mos2025141_372572027.pdf)
7.  高效码农. MedMamba如何突破医学图像分类瓶颈？深度解析视觉Mamba的架构革命. 2025. [xugj520.cn](https://www.xugj520.cn/archives/medmamba-medical-image-classification.html)
8.  刘青海, 吴钱林, 罗佳, 等. 面向大语言模型的医学图像语义挖掘跨模态哈希[J]. 电子与信息学报, 2025. (Online Published) [jeit.ac.cn](https://www.jeit.ac.cn/cn/article/doi/10.11999/JEIT250529?viewType=HTML)
9.  刘再毅, 赵致禾, 石镇维. 医学影像大模型：肿瘤精准诊疗的范式革新[J]. 协和医学杂志, 2025. (Online Published) [xhyxzz.pumch.cn](https://xhyxzz.pumch.cn/article/doi/10.12290/xhyxzz.2025-0328?viewType=citedby-info)
10. Ronneberger, O., Fischer, P., & Brox, T. U-Net: Convolutional Networks for Biomedical Image Segmentation. In *International Conference on Medical image computing and computer-assisted intervention (MICCAI)*, 2015: 234-241.
11. Oktay, O., Schlemper, J., Folgoc, L. L., et al. Attention u-net: Learning where to look for the pancreas. *arXiv preprint arXiv:1804.03999*, 2018.
12. Chen, J., Lu, Y., Yu, Q., et al. Transunet: Transformers make strong encoders for medical image segmentation. *arXiv preprint arXiv:2102.04306*, 2021.
13. xiaoyuexing. StarrySky: 精选了千余项目，包括机器学习、深度学习、NLP、GNN、推荐系统、生物医药、机器视觉等内容. *GitHub Repository*, 2023. [github.com](https://github.com/xiaoyuexing/StarrySky)