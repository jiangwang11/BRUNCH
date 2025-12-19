2022–2025 年基于 Vision Transformer 的医学影像技术深度综述：从架构演进到通用基础模型
摘要
过去十年，深度学习在医学影像分析领域取得了革命性进展，成为辅助临床诊断、治疗规划及预后评估的关键技术。尽管卷积神经网络（CNN）长期以来凭借其局部归纳偏置和位移不变性在该领域占据主导地位，但自 2021 年起，Vision Transformer（ViT）凭借其卓越的全局上下文建模能力和长距离依赖捕捉能力，开始在医学视觉任务中引发范式转移。本综述旨在对 2022 年至 2025 年间 Vision Transformer 在医学影像领域的应用进行详尽的梳理与深度分析。报告涵盖了从基础架构的混合化改良、针对特定模态（如 MRI 重建、病理全玻片分析）的定制化设计，到 2024–2025 年爆发的医学通用基础模型（Foundation Models）如 MedSAM、Virchow 和 UNI 的最新进展。

本报告深入探讨了 ViT 在医学图像分割、分类、合成与重建中的具体表现，分析了其在处理高分辨率、三维体数据及多模态数据时的优势与局限。通过对 Med-Former、Swin UNETR、MetaUNETR、FPS-Former 等代表性工作的剖析，揭示了当前技术从“纯 Transformer”向“混合架构”及“频域感知架构”演变的内在逻辑。此外，本报告还重点关注了边缘计算环境下的 ViT 压缩、持续学习（Continual Learning）在医学场景中的落地挑战，并基于现有文献对未来的多模态大模型融合与临床部署趋势进行了预测。

1. 引言：医学影像分析的范式转移与技术背景
1.1 医学影像数据的独特性与挑战
医学影像分析旨在通过计算方法辅助医生进行疾病诊断、治疗规划及预后评估。与自然图像处理（如自动驾驶、安防监控）相比，医学影像数据具有独特的复杂性，这对深度学习模型的架构设计提出了极高的要求。

首先，医学影像具有高维度与多模态特性。临床常用的计算机断层扫描（CT）和磁共振成像（MRI）本质上是三维（3D）甚至四维（4D，包含时间维度）的体素数据。这种数据结构要求模型不仅要在二维平面内提取特征，还需要理解层与层之间的解剖连续性。此外，不同模态（如 PET 的代谢信息与 CT 的解剖信息）之间的融合需要模型具备强大的多源异构数据处理能力 。   

其次，细微差异与高精度要求是医学诊断的核心挑战。病变区域（如早期的肺结节或微小的脑肿瘤）与周围正常组织之间的像素强度差异往往极小，且边界模糊不清。这要求模型具备极高的灵敏度来捕捉高频细节（如纹理变化），同时又需要全局上下文来排除伪影干扰 。   

最后，数据稀缺与标注成本是制约该领域发展的最大瓶颈。与 ImageNet 等拥有数千万标注数据的自然图像数据集不同，高质量的医学标注数据获取需要资深放射科医生的参与，成本极高且涉及隐私伦理问题。这导致了医学影像领域长期处于“小样本学习”（Small-Sample Learning）的困境 。   

1.2 从 CNN 到 Vision Transformer 的演进
长期以来，以 U-Net 为代表的卷积神经网络（CNN）凭借其平移不变性（Translational Invariance）和局部归纳偏置（Local Inductive Bias），成为处理 X 射线、CT、MRI 及病理图像的标准工具。CNN 通过滑动窗口操作有效地提取了图像的局部纹理和边缘特征，且参数共享机制使其在训练数据有限的情况下也能较快收敛 。   

然而，CNN 的局限性也日益凸显：它难以有效捕捉长距离依赖关系（Long-range Dependencies）。在医学诊断中，判断某个器官的病变往往需要参考远离该区域的另一解剖结构的相对位置（例如，判断淋巴结转移需要结合原发灶的位置信息）。CNN 需要堆叠极深的网络层才能获得足够的感受野来覆盖全图，这不仅导致了计算效率的下降，还引发了优化困难和梯度消失等问题 。   

Vision Transformer（ViT）的引入标志着一种新的范式转移。ViT 将图像视为补丁序列（Sequence of Patches），利用自注意力机制（Self-Attention Mechanism）直接建模图像中任意两个位置之间的交互。这种机制使得 ViT 在第一层就能获得全局感受野，从而能够更好地理解解剖结构的整体拓扑关系。尽管 ViT 在自然图像领域取得了巨大成功，但将其迁移至医学影像领域面临着独特的挑战：标准 ViT 缺乏对局部归纳偏置的假设，导致其需要海量数据进行预训练才能收敛，且对高频细节的捕捉能力不如 CNN 。   

1.3 2022–2025 年的发展脉络
回顾 2022 年至 2025 年的研究进展，医学 Vision Transformer 的发展呈现出清晰的三个阶段：

架构探索与混合化（2022-2023）：为了解决 ViT 对数据量的饥渴和局部特征提取能力的不足，大量研究致力于将 CNN 与 ViT 结合，设计出 Hybrid ViT（混合架构），如 TransUNet 和 Swin UNETR。这一阶段的核心目标是在保留 CNN 归纳偏置的同时引入 ViT 的全局建模能力 。   

效率优化与维度适配（2023-2024）：针对 3D 医学影像带来的巨大计算成本，研究者提出了线性注意力机制、稀疏注意力及基于频域的优化方案，如 FPS-Former 和 Lite Swin UNETR。这一阶段的研究重点在于如何让 ViT 在显存受限的医疗设备上高效运行 。   

基础模型与通用化（2024-2025）：随着 Segment Anything Model (SAM) 的发布，医学影像领域迅速进入“通用大模型”时代。MedSAM、SAM2 的医学适配版以及针对病理学的十亿级参数模型（如 Virchow、UNI）展示了少样本（Few-shot）甚至零样本（Zero-shot）的强大泛化能力，标志着医学 AI 从“专用模型”向“通用助手”的转变 。   

本综述将沿着这一脉络，详细剖析各子领域的关键技术突破、实验结果及临床意义。

2. 核心架构演进：从纯 ViT 到混合与高效设计
在医学影像中直接应用标准 ViT 往往效果不佳，主要原因在于标准 ViT 缺乏对局部边缘细节的捕捉能力，且在小样本数据上极易过拟合。因此，2022-2025 年的主流趋势是架构的“特异化”改良，旨在结合 CNN 的优势并降低计算复杂度。

2.1 混合架构（Hybrid Vision Transformers）
混合架构的核心思想是结合 CNN 的局部特征提取能力与 ViT 的全局建模能力。根据 2024 年和 2025 年发布的系统性综述 ，混合架构已成为医学图像分割和分类任务中最主流且有效的选择。   

2.1.1 互补优势的融合逻辑
CNN 的卷积层能够高效地提取底层的纹理、边缘和形状特征，这对于医学图像（如 X 光片中的骨折线、MRI 中的肿瘤边界）至关重要。而 Transformer 层则擅长在深层特征空间中聚合全局语义，理解不同解剖结构之间的相对位置关系。混合架构通过在编码器（Encoder）或解码器（Decoder）阶段交替使用卷积层和 Transformer 块，有效缓解了纯 ViT 丢失高频信息的问题 。   

2.1.2 代表性设计模式
系统性回顾指出了三种主要的混合策略：

ViT 嵌入编码器（ViT in Encoder）：这是最常见的设计，如 TransUNet。它通常使用 CNN（如 ResNet-50）作为特征提取器（Stem），将提取到的特征图展平后输入 ViT 层进行全局上下文建模。这种设计利用 CNN 解决了 ViT 对原始像素输入不敏感的问题。

ViT 嵌入解码器（ViT in Decoder）：较少见，但在某些生成任务中使用，旨在利用 ViT 的长距离依赖能力来恢复高分辨率的解剖细节。

并行双流架构：同时运行 CNN 分支和 ViT 分支，通过交叉注意力（Cross-Attention）模块融合两者的特征。

在放射学影像的器官分割任务上，混合设计表现出了比纯 CNN（如 U-Net）和纯 ViT 更优越的性能和更快的收敛速度。例如，在腹部多器官分割任务中，混合架构能够更准确地分割出胰腺、胆囊等形状多变且位置依赖性强的小器官 。   

2.2 分层与金字塔结构（Hierarchical ViTs）
为了处理医学图像（尤其是 CT 和 MRI）的多尺度特性，金字塔结构的 Transformer 逐渐取代了柱状结构的 ViT（如 ViT-Base）。

2.2.1 Swin Transformer 的主导地位
Swin Transformer 是该领域的里程碑式工作。它引入了“移动窗口注意力”（Shifted Window Attention）机制，将自注意力的计算限制在局部窗口内，并通过层级间的窗口移动实现跨窗口交互。这种设计将计算复杂度从图像尺寸的二次方 O(N 
2
 ) 降低到线性 O(N)，使其成为处理高分辨率 3D 医学图像的理想骨干网络。

Swin UNETR 是将 Swin Transformer 应用于 3D 医学分割的代表作。它将 3D CT 图像切分为 3D Patches，通过 3D Swin Transformer Block 进行特征编码，并通过跳跃连接（Skip Connections）与基于 CNN 的解码器融合。2024 年至 2025 年的最新版本（Swin UNETR V2 及相关变体）在脑肿瘤分割挑战赛（BraTS 2024）中表现优异，证明了其在处理 3D 体素数据时的鲁棒性 。   

2.2.2 Lite Swin UNETR：极致的效率优化
尽管 Swin UNETR 性能强大，但其参数量和计算量仍然较大，难以在资源受限的医疗设备上部署。针对这一问题，2025 年提出的 Lite Swin UNETR 引入了显著的架构创新。

Lite Module：该模型设计了一种全新的“Lite Module”来替代传统卷积或标准 Transformer 块。它利用深度可分离卷积（Depthwise Separable Convolution）来减少参数量，并采用了双分支结构：

一个分支使用 7×7×7 的大核卷积捕捉大范围的解剖上下文。

另一个分支使用 3×3×3 的小核卷积捕捉精细的边界细节。

Squeeze-and-Excitation (SE)：集成了 SE 模块以自适应地强调重要的通道特征。

性能提升：在 MSD 前列腺分割数据集上，Lite Swin UNETR 将参数量减少了 37%（从 4.38M 降至 2.76M），计算量（FLOPs）降低了 52%（从 53.07G 降至 25.66G），同时平均 Dice 分数从 58.76% 提升到了 60.89% 。这一结果有力地证明了针对医学图像特点进行的轻量化设计比单纯堆叠参数更为有效。   

2.3 频域与结构化注意力机制
ViT 在 MRI 重建等低层视觉任务中面临的主要挑战是对高频信息（纹理、边缘）捕捉不足，因为自注意力机制本质上具有低通滤波的特性。为了解决这一问题，2025 年的研究开始转向频域视角。

2.3.1 FPS-Former 的频域革新
FPS-Former  提出了一套完整的解决方案，旨在增强 ViT 的 MRI 重建能力。该模型包含三个关键创新模块：   

频率调制注意力（Frequency Modulation Attention Module, FMAM）：该模块不再仅仅在空间域计算注意力，而是利用拉普拉斯金字塔将特征图分解为不同频带。它能够自适应地重校准不同频率的特征，强制模型关注对恢复细节至关重要的高频分量。这解决了 ViT 倾向于生成平滑图像、丢失病理纹理的问题。

空间净化注意力（Spatial Purification Attention Module, SPAM）：医学图像（如 MRI）背景通常包含大量无信息的黑色区域。在标准 ViT 中，这些背景 Token 仍会参与全局交互，引入噪声并浪费计算资源。SPAM 模块通过动态识别并过滤掉这些无关 Token，显著提高了计算效率和重建信噪比。

尺度多样化前馈网络（Scale Diversification Feed-forward Network, SDFN）：通过混合尺度融合策略，增强了前馈网络对多尺度特征的建模能力。

在 fastMRI 和 SKM-TEA 等公开数据集上的实验表明，FPS-Former 在高倍加速（如 8 倍欠采样）场景下，显著优于现有的 CNN 和 Transformer 方法，能够重建出更清晰的解剖结构和更少的伪影。

3. 医学图像分割：迈向通用与持续学习
分割是医学影像分析中最为核心的任务，直接关系到病灶定量、放疗勾画和手术导航。2024-2025 年，该领域经历了从“单一任务专用模型”到“通用基础模型”的剧烈变革。

3.1 专用分割模型的极致优化：MetaUNETR 与 UNest
尽管通用模型兴起，但在特定器官的精细分割上，经过特殊设计的专用模型仍在不断刷新记录。

3.1.1 MetaUNETR：反思 Token Mixer 的必要性
发表于 MICCAI 2024 的 MetaUNETR  对 Transformer 的核心组件——Token Mixer 进行了深刻反思。该研究基于 MetaFormer 的理论，即 Transformer 的成功可能更多归功于其宏观架构（Patch Embedding -> Mixer -> MLP -> Norm）而非具体的自注意力算子。   

设计理念：MetaUNETR 探索了使用简单的池化（Pooling）或 MLP 替代昂贵的自注意力机制作为 Token Mixer。

实验结果：在 BTCV（多器官分割）、AMOS 和 AbdomenCT-1K 三个规模递增的数据集上，MetaUNETR 在同等 FLOPs 和参数量约束下，取得了与 Swin UNETR 相当甚至更好的 Dice 分数。例如在 BTCV 数据集上，其表现优异，且推理速度更快。

启示：这一发现提示我们，在数据量有限的医学场景下，过参数化的复杂注意力机制可能是不必要的，甚至可能因为过拟合而损害性能。简约的架构设计往往能带来更好的泛化性。

3.1.2 UNest：结构归纳偏置的引入
针对非配对医学图像合成（Unpaired Synthesis）和分割任务，MICCAI 2024 提出的 UNest (UNet Structured Transformer)  引入了强结构归纳偏置。   

核心问题：Transformer 在缺乏配对数据监督（例如只有 MRI 数据和未配对的 CT 数据）时，往往难以收敛到最优解，生成的图像容易出现解剖结构变形（Hallucination）。

解决方案：UNest 利用基础模型 Segment Anything Model (SAM) 提取前景解剖结构，并在主要解剖区域内执行结构化注意力（Structural Attention）。这种机制实际上是将解剖学先验知识注入到了 Transformer 中。

成效：在 MRI、CT 和 PET 的跨模态合成与分割任务中，UNest 的性能提升高达 19.30%，尤其是在保持大脑沟回、鼻腔等复杂几何结构的一致性方面，显著优于 CycleGAN 和 ResViT。

3.2 通用分割模型：MedSAM 及其衍生
2024-2025 年是“Segment Anything”概念在医学领域落地的爆发期。MedSAM  是首个将 SAM 适配于医学图像的基础模型，其影响深远。   

3.3.1 MedSAM 的架构与训练策略
MedSAM 基于 SAM 的 ViT 图像编码器，但在超过 150 万对医学图像-掩膜（覆盖 10 种模态、30 多种癌症类型）上进行了全监督微调。与 SAM 的零样本推理不同，MedSAM 采用了全量微调（Full Fine-tuning）策略来适应医学图像的灰度分布。

提示工程（Prompt Engineering）：研究发现，边界框（Bounding Box）提示在医学场景中比点提示（Point Prompt）更为鲁棒。因为医学器官（如肿瘤）往往边界模糊，单点提示容易导致分割不完整或溢出。实验显示，在 BTCV 数据集上，使用 Box 提示的 MedSAM 平均 Dice 分数约为 82.88% 至 85.85%，显著优于零样本的 SAM（后者在医学图像上 Dice 通常低于 60%）。   

3.3.2 MedSAM vs. nnU-Net：通用与专用的博弈
尽管 MedSAM 泛化能力强，但在特定任务的精度上，它与自适应框架 nnU-Net 仍有差距。

对比分析：在 BTCV 数据集（30 例腹部 CT）上，经过精心调优的 nnU-Net 平均 Dice 分数可达 95.2%，而 MedSAM 通常在 80-90% 区间 。   

原因：MedSAM 本质上是一个 2D 模型，处理 3D CT 时需要逐切片推理，缺乏切片间的上下文一致性（Inter-slice Consistency）。此外，作为通用模型，它难以针对特定器官（如极小的肾上腺）的纹理特征进行极致优化。

3.3.3 MedSAM-2 与 3D 视频分割
为了解决 2D 模型的局限性，2025 年的研究开始探索 SAM2 在医学领域的应用。MedSAM-2  引入了显存机制（Memory Mechanism），使其能够处理视频序列。在医学场景中，这被转化为处理 3D 体素数据（将 CT 的 Z 轴视为时间轴）。   

时空连续性：MedSAM-2 利用 Memory Bank 存储上一张切片的分割特征，并将其传递给下一张切片。这不仅提高了 3D 分割的连续性，还支持了“单提示分割整个体积”（One-Prompt Segmentation），即用户只需在中间切片给出一个提示，模型即可分割整个器官体积。

3.3 持续语义分割（Continual Semantic Segmentation, CSS）
在临床实践中，模型经常需要学习分割新的器官或病灶，而不能重新训练旧数据（由于隐私或存储限制）。传统的 CSS 方法往往面临“灾难性遗忘”（Catastrophic Forgetting）或参数爆炸的问题。

LoCo-PVT (MICCAI 2024)：这项工作提出了一种基于 低秩适应（Low-Rank Adaptation, LoRA） 的方案 。   

机制：该模型首先在初始任务上训练一个冻结的 PVT（Pyramid Vision Transformer）基座。对于每个新的分割任务，它不改变基座参数，而是添加极其轻量级的 LoRA 参数矩阵。

关键发现：研究指出，Patch Embedding 层、多头注意力层和前馈层的适应性对于新任务至关重要。

性能突破：在覆盖全身 121 个器官 的四个数据集上，LoCo-PVT 在避免遗忘的同时，参数增长率仅为 16.7%，远低于主流架构类 CSS 方法（如动态扩展解码器）的 96.7%。且其分割精度接近全量数据联合训练的上限（Upper Bound），为医院本地模型的终身学习提供了可行路径。

4. 医学图像分类与诊断：ViT 的深层特征挖掘
在分类任务（如 X 光片疾病筛查、皮肤病变分类）中，ViT 的应用重点在于解决微小病灶检测和类别不平衡问题。

4.1 Med-Former：局部-全局特征的深度融合
发表于 MICCAI 2024 的 Med-Former  是该领域的代表作。   

挑战：胸部 X 光片中的病灶（如早期的气胸、微小结节）往往非常小，占据图像的比例不到 1%。标准 ViT 的 Patch Size（通常 16x16）对于这些微小病灶来说过于粗糙，容易导致信息丢失。

解决方案：Med-Former 提出了两个核心模块：

Local-Global Transformer Module：并行处理局部细节和全局上下文，确保微小特征不被全局信息淹没。

Spatial Attention Fusion Module：通过空间注意力机制动态融合局部和全局特征。

性能基准：

NIH Chest X-ray14：Med-Former 取得了 85.78% 的平均 AUC，这一成绩刷新了该数据集的 SOTA（相比之下，之前的 DenseNet121 变体通常在 80-84% 之间）。

Stanford CheXpert：AUC 高达 92.07%。

意义：这证明了精心设计的 Transformer 结构在捕捉胸部 X 光片中微小结节或浸润病变方面的能力已超越传统 CNN。

4.2 皮肤病与组织病理学分类
UDCD (Uncertainty-Driven Contrastive Distillation)：针对医学图像分类中的高类内方差和类别不平衡，MICCAI 2024 的另一项工作提出了基于不确定性的对比蒸馏框架。该方法利用教师模型的知识来规范化轻量级学生模型（如 ViT）的学习，特别是在皮肤病变分类中有效缓解了对多数类的偏见 。   

5. 病理学基础模型：计算病理学的“GPT 时刻”
2024 年被视为计算病理学（Computational Pathology, CPath）的“基础模型元年”。由于病理全玻片图像（WSI）具有十亿像素级的分辨率，且未标注数据海量，非常适合自监督学习（Self-Supervised Learning, SSL）和 ViT 的扩展（Scaling）。

5.1 Virchow：十亿参数级的病理巨兽
由 Paige.ai 和 Microsoft Research 发布的 Virchow  是目前最大的病理学基础模型之一。   

规模与数据：Virchow 拥有 6.32 亿参数，基于 150 万张 H&E 染色的 WSI（来自 10 万名患者）进行训练。这在数据量级上比之前的模型高出几个数量级。

技术路线：采用 DINOv2 自监督算法。DINOv2 通过学生-教师网络的蒸馏学习，能够迫使模型学习到具有语义一致性的特征表示，而无需任何人工标注。

性能突破：

泛癌检测：在包含 17 种癌症类型的样本级检测中，Virchow 实现了 0.949 的平均 AUC。

罕见癌症：对于 7 种罕见癌症类型（训练数据极其稀缺），Virchow 达到了 0.937 AUC。这一结果极具临床意义，因为收集罕见癌症的大规模标注数据几乎是不可能的。Virchow 证明了通过在大规模数据上预训练，模型可以学习到通用的组织学特征，从而在罕见病上实现“触类旁通”。

对比优势：在多种生物标志物预测任务中，Virchow 的 Embeddings 表现优于传统的 CTransPath 和 Phikon 模型 。   

5.2 UNI 与 Prov-GigaPath
UNI (Nature Medicine 2024) ：UNI 是另一个基于 ViT 的通用病理模型，它采用了 Masked Autoencoder (MAE) 架构，在超过 1 亿个 组织补丁（Tissue Patches）上预训练。MAE 通过遮挡图像的大部分（例如 75%）并要求模型重建，迫使模型理解组织的高级语义结构。在包含 30 多个临床任务的基准测试中，UNI 展现了极强的数据效率（Data Efficiency）。   

Prov-GigaPath：利用十亿级图像块进行预训练，进一步推动了 WSI 特征提取的极限。

主要洞察：病理学基础模型的出现意味着传统的“提取特征+训练分类器”的模式正在被“冻结的基础模型编码器+轻量级适配器（Adapter）”模式取代。这些模型展现了惊人的零样本和少样本能力，解决了病理标注昂贵的痛点。

6. 医学图像重建与合成
6.1 MRI 重建的 Transformer 革命
MRI 加速重建旨在从欠采样的 k 空间数据中恢复高质量图像，以缩短扫描时间。

挑战：标准 ViT 计算全局注意力带来的计算负担过重，且容易产生平滑效应，丢失高频细节。

FPS-Former 的解决方案：如 2.3 节所述，通过频率调制（Frequency Modulation）和空间净化（Spatial Purification），FPS-Former 在 fastMRI 和 SKM-TEA 数据集上表现优于 SwinIR 等先前方法。

量化指标：在 8 倍加速（8x Acceleration） 的极端欠采样下，FPS-Former 的 PSNR（峰值信噪比）比 Swin Transformer 基线高出约 0.5-1.0 dB，且边缘锐度显著提升。这种提升在临床上意味着更清晰的解剖结构和更少的误诊风险 。   

6.2 生成式 ViT 与数据增强
生成式 ViT 用于域泛化：MICCAI 2024 的一项研究  利用自监督 ViT 提取图像补丁特征并注入原始图像，生成具有多样化属性的合成组织病理图像。这种增强策略在 Camelyon17-WILDS 挑战赛中将域泛化性能提升了 2%，在另一项上皮-间质分类任务中提升了 26%。这证明了 ViT 不仅是判别模型，也可以作为强大的生成模型用于数据扩增。   

7. 效率、边缘部署与未来展望
7.1 边缘计算环境下的 ViT
尽管 ViT 性能强大，但其巨大的参数量和计算成本限制了在临床边缘设备（如便携式超声、床旁监护仪）上的部署。2025 年的综述  专门探讨了这一问题。   

压缩策略：

剪枝与量化：研究表明，对 ViT 进行结构化剪枝（去除冗余的注意力头）和后训练量化（Post-training Quantization, PTQ）至 8-bit 甚至 4-bit，可以在精度损失小于 1% 的情况下将推理速度提升 2-4 倍。

硬件加速：针对 FPGA 和移动 GPU 的特定加速器设计正在兴起，旨在优化 Softmax 和矩阵乘法的流水线执行。

7.2 趋势预测与未来展望
基于 2022-2025 年的文献分析，医学影像 ViT 技术呈现出以下不可逆转的趋势：

7.2.1 从“单一模态”向“多模态基础模型”演进
未来的模型将不再仅仅处理图像。结合放射学报告（Text）、基因组数据（Omics）和影像（Image）的 多模态大模型（Large Multimodal Models, LMMs） 将成为标准。CLIP 风格的对齐预训练已经在 Chest X-ray 上显示了零样本分类的潜力（如 CheXzero），未来将扩展到 3D 模态。

7.2.2 通用医疗 AI 助手（Generalist Medical AI）
随着 MedSAM 和 Virchow 的成功，单一模型解决多种任务（分割、检测、分类、报告生成）成为可能。未来的临床工作流可能仅需一个核心基础模型，通过不同的 Prompt（文本提示、视觉提示）来触发不同功能。

7.2.3 交互式与可解释性 AI
“黑盒”性质是 ViT 临床落地的最大障碍。2025 年的研究开始强调 可解释性（Interpretability），例如通过可视化 Attention Map 来定位病灶，但这还不够。未来的趋势是模型能够用自然语言解释其决策逻辑（Reasoning），即“Visual Question Answering (VQA)”与诊断报告生成的深度融合 。   

7.2.4 持续学习与联邦学习
为了解决数据孤岛和隐私问题，结合联邦学习（Federated Learning）的 ViT 训练框架将是热点。同时，如 LoCo-PVT 展示的，低成本的持续学习技术将使模型能够在医院本地不断进化，而无需上传数据或重训练大模型。

8. 结论
2022 年至 2025 年间，Vision Transformer 在医学影像领域完成了从“尝试性应用”到“确立主导地位”的跨越。技术演进的主线清晰可见：从最初简单移植自然图像 ViT，到融合 CNN 的 混合架构（Hybrid ViT），再到针对医学 3D/高频特征的 定制化改良（Swin UNETR, FPS-Former），最终迈向基于海量数据预训练的 基础模型（Foundation Models）。

当前，MedSAM 和 Virchow 等基础模型已展现出强大的泛化能力，预示着医学影像分析正步入“大模型+微调”的新时代。然而，3D 空间的高效建模、小病灶的精准捕捉以及临床可解释性仍是亟待解决的核心挑战。未来的突破将极有可能源于多模态数据的深度融合与交互式 AI 系统的临床集成。

附录：关键模型性能概览表
为了更直观地展示各代表性模型的性能，下表汇总了本报告中提及的关键模型及其在标准数据集上的表现。

模型名称	任务领域	核心机制	关键数据集性能 (SOTA)	引用
MedSAM	通用分割	SAM + Adapter 微调	BTCV Dice: ~82-85% (Box Prompt)	
nnU-Net	专用分割	自适应 U-Net	BTCV Dice: 95.2% (Benchmark)	
Med-Former	胸部 X 光分类	Local-Global Transformer	NIH ChestX-ray14 AUC: 85.78%	
Virchow	病理全玻片分析	DINOv2 (632M Params)	Pan-Cancer AUC: 0.949	
MetaUNETR	多器官分割	MetaFormer Token Mixer	BTCV Dice: 竞争级 (高效于 SwinUNETR)	
Lite Swin UNETR	前列腺分割	深度可分离卷积	参数量减少 37%, Dice 提升至 60.89%	
FPS-Former	MRI 重建	频域注意力 + 空间净化	fastMRI PSNR: 提升 ~0.5dB (8x加速)	
LoCo-PVT	持续语义分割	PVT + Low-Rank Adaptation	遗忘率极低，参数增长仅 16.7%	
UNest	非配对图像合成	SAM 结构归纳偏置	MRI-to-CT 性能提升 19.3%	
  
(本报告基于截至 2025 年的公开文献与预印本资料整理，所有数据与结论均有据可查。)


papers.miccai.org
Structural Attention: Rethinking Transformer for Unpaired Medical Image Synthesis⋆ - MICCAI
在新窗口中打开

pmc.ncbi.nlm.nih.gov
Transforming medical imaging with Transformers? A comparative review of key properties, current progresses, and future perspectives - NIH
在新窗口中打开

pmc.ncbi.nlm.nih.gov
Systematic Review of Hybrid Vision Transformer Architectures for Radiological Image Analysis - PMC
在新窗口中打开

papers.miccai.org
Med-Former: A Transformer based Architecture for Medical Image Classification - MICCAI
在新窗口中打开

researchgate.net
Med-Former: A Transformer Based Architecture for Medical Image Classification | Request PDF - ResearchGate
在新窗口中打开

arxiv.org
Foundation Models in Medical Imaging - A Review and Outlook - arXiv
在新窗口中打开

arxiv.org
Vision Transformers on the Edge: A Comprehensive Survey of Model Compression and Acceleration Strategies - arXiv
在新窗口中打开

medrxiv.org
Systematic Review of Hybrid Vision Transformer Architectures for Radiological Image Analysis | medRxiv
在新窗口中打开

pubmed.ncbi.nlm.nih.gov
Comparison of Vision Transformers and Convolutional Neural Networks in Medical Image Analysis: A Systematic Review - PubMed
在新窗口中打开

ieeexplore.ieee.org
Brain Tumor Segmentation using 3D Swin UNETR - IEEE Xplore
在新窗口中打开

researchgate.net
A Lightweight Version of Swin UNETR for Efficient 3D Medical Image Segmentation
在新窗口中打开

researchgate.net
Boosting ViT-based MRI Reconstruction from the Perspectives of Frequency Modulation, Spatial Purification, and Scale Diversification - ResearchGate
在新窗口中打开

pubs.rsna.org
Foundation Models in Radiology: What, How, Why, and Why Not - RSNA Journals
在新窗口中打开

arxiv.org
Unifying Multiple Foundation Models for Advanced Computational Pathology - arXiv
在新窗口中打开

pubmed.ncbi.nlm.nih.gov
Towards a general-purpose foundation model for computational pathology - PubMed - NIH
在新窗口中打开

arxiv.org
A Recent Survey of Vision Transformers for Medical Image Segmentation - arXiv
在新窗口中打开

catalog.ngc.nvidia.com
GPU-optimized AI, Machine Learning, & HPC Software - NGC Catalog - NVIDIA
在新窗口中打开

arxiv.org
[2412.10776] Boosting ViT-based MRI Reconstruction from the Perspectives of Frequency Modulation, Spatial Purification, and Scale Diversification - arXiv
在新窗口中打开

ojs.aaai.org
Boosting ViT-based MRI Reconstruction from the Perspectives of Frequency Modulation, Spatial Purification, and Scale Diversification - AAAI Publications
在新窗口中打开

papers.miccai.org
MetaUNETR: Rethinking Token Mixer Encoding for Efficient Multi-Organ Segmentation - MICCAI
在新窗口中打开

pubmed.ncbi.nlm.nih.gov
Segment anything in medical images - PubMed
在新窗口中打开

github.com
bowang-lab/MedSAM: Segment Anything in Medical Images - GitHub
在新窗口中打开

ecva.net
I-MedSAM: Implicit Medical Image Segmentation with Segment Anything
在新窗口中打开

openreview.net
FREE-FORM LANGUAGE- BASED SEGMENTATION FOR MEDICAL IMAGES - OpenReview
在新窗口中打开

pmc.ncbi.nlm.nih.gov
Segment Anything Model (SAM) and Medical SAM (MedSAM) for Lumbar Spine MRI - PMC
在新窗口中打开

arxiv.org
Good Enough: Is it Worth Improving your Label Quality? - arXiv
在新窗口中打开

arxiv.org
Segment Anything in Medical Images and Videos: Benchmark and Deployment - arXiv
在新窗口中打开

arxiv.org
RFMedSAM 2: Automatic Prompt Refinement for Enhanced Volumetric Medical Image Segmentation with SAM 2 - arXiv
在新窗口中打开

papers.miccai.org
Low-Rank Continual Pyramid Vision Transformer: Incrementally Segment Whole-Body Organs in CT with Light-Weighted Adaptation - MICCAI
在新窗口中打开

papers.miccai.org
Low-Rank Continual Pyramid Vision Transformer: Incrementally Segment Whole-Body Organs in CT with Light-Weighted Adaptation | MICCAI 2024 - Open Access
在新窗口中打开

liner.com
[Quick Review] Low-Rank Continual Pyramid Vision Transformer: Incrementally Segment Whole-Body Organs in CT with Light-Weighted Adaptation - Liner
在新窗口中打开

papers.miccai.org
Confidence Matters: Enhancing Medical Image Classification Through Uncertainty-Driven Contrastive Self-Distillation - MICCAI
在新窗口中打开

esmo.org
Virchow: The Largest Foundation Model for Computational Pathology To Date - ESMO
在新窗口中打开

arxiv.org
[2309.07778] Virchow: A Million-Slide Digital Pathology Foundation Model - arXiv
在新窗口中打开

pmc.ncbi.nlm.nih.gov
A foundation model for clinical-grade computational pathology and rare cancers detection
在新窗口中打开

jmaj.jp
Pathology Foundation Models | JMA Journal
在新窗口中打开

liner.com
[Quick Review] Boosting ViT-based MRI Reconstruction from the Perspectives of Frequency Modulation, Spatial Purification, and Scale Diversification - Liner
在新窗口中打开

arxiv.org
1 Introduction - arXiv
在新窗口中打开

papers.miccai.org
Self-supervised Vision Transformer are Scalable Generative Models for Domain Generalization - MICCAI
在新窗口中打开

arxiv.org
[2510.12021] Evaluating the Explainability of Vision Transformers in Medical Imaging - arXiv