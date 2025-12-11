好的，遵照您的指示。作为一名严谨的科研助手，我将基于提供的真实联网搜索结果，为您生成一篇关于2022-2025年航空与卫星影像中目标检测的中文学术综述。

***

### **航空与卫星影像目标检测技术年度进展综述 (2022-2025)**

#### **摘要**

航空与卫星影像（遥感影像）目标检测是计算机视觉在对地观测领域的核心应用，对城市规划、环境监测和国防安全至关重要。近年来（2022-2025），深度学习技术显著推动了该领域的发展，研究重心从增量式改进转向了架构创新与大模型应用。本综述旨在系统梳理此期间的代表性工作，总结其在应对遥感影像特有挑战（如尺度变化、方向任意、背景复杂）方面的核心方法与共性规律，并对未来研究趋势进行展望。

---

#### **1. 引言**

遥感影像目标检测旨在从空中或太空视角获取的图像中定位并识别特定地物。与自然图像相比，遥感影像呈现出独特的挑战性：1) **尺度差异巨大**，从大型机场到小型车辆，目标尺寸跨越多个数量级；2) **方向任意性与高宽比**，物体（如船舶、桥梁）的朝向不固定，且常呈细长形态；3) **背景复杂与小目标密集**，目标常嵌入在庞杂的地物背景中，且小尺寸目标密集分布的情况十分常见。

为应对上述挑战，2022至2025年间的研究工作在网络架构、特征表示和学习范式上进行了深度探索。研究者们不再局限于微调通用检测器，而是设计了专门的模块和模型来增强上下文感知、优化特征融合、解决表征不对齐问题，并开始构建遥感领域的专属基础模型。

#### **2. 方法分类与代表作**

##### **2.1 扩大感受野与上下文建模**

遥感目标的准确识别高度依赖其周围环境提供的上下文信息。然而，传统卷积神经网络（CNN）的有限感受野限制了其上下文建模能力。为此，近期研究致力于通过大核卷积和注意力机制来扩展有效感受野。

*   **LSKNet** 关注到遥感目标识别需要广泛且可变的上下文信息，而现有模型普遍忽视此先验 [mftp.mmcheng.net](https://mftp.mmcheng.net/Papers/24IJCV-LSK-CN.pdf)。它提出了一种“自适应大核卷积网络（Large Selective Kernel Network）”，通过空间选择性机制，动态地对一系列由分解技术获得的大卷积核（如5x5 -> 7x7@d=3，感受野达23）特征进行加权融合。这种设计使模型能够依据输入自适应地调整每个目标所需感受野的大小。实验证明，该轻量级骨干网络在分类、检测、分割等14个遥感基准测试中均达到了顶尖性能，验证了动态大感受野的有效性。

*   **Strip R-CNN** 针对遥感图像中常见的高长宽比目标检测难题，提出了一种基于大尺寸条带卷积（Large Strip Convolution）的解决方案 [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/96698)。该方法创新性地利用顺序正交的大条带卷积来有效捕捉长条形物体的空间信息，而非传统的大方形卷积核。此外，通过解耦检测头并为定位分支配备条带卷积，显著增强了目标的定位精度。该模型在DOTA-v1.0数据集上以82.75%的mAP刷新了记录，证明了其在处理高宽比物体上的卓越能力。

*   **上下文感知多感受野融合网络** 针对现有网络对多尺度上下文信息利用不充分的问题，设计了一种层次化的特征增强框架 [jeit.ac.cn](https://www.jeit.ac.cn/cn/article/doi/10.11999/JEIT240560?viewType=HTML)。该网络构建了“感受野扩张模块”，并行使用大核选择卷积注意力和移位窗口自注意力来增强多尺度特征的感知能力。同时，“高层特征聚合模块”将特征金字塔网络（FPN）的深层语义信息有效融合到浅层特征中。在DIOR-R和HRSC2016数据集上的实验表明，该方法能更准确地区分外观相似目标并定位不同尺度物体。

##### **2.2 解决特征不对齐与定向检测**

一阶段定向检测器普遍存在分类分支与回归分支的预测不对齐问题，即分类置信度最高的预测框不一定是定位最准的框。这一问题在需要预测角度的遥感场景中尤为突出。

*   **BFA-Net (分支特征对齐网络)** 直接针对上述不对齐问题，提出了一种分支特征对齐学习方法 [opticsjournal.net](https://www.opticsjournal.net/Articles/OJe5fbf04e3ca9f35d/FullText)。其核心是“分支对齐模块（BAM）”，采用部分耦合的检测头来加强分类与回归分支的特征交互。在标签分配阶段，设计的“基于排序策略的分支对齐分配（BAAS）”方法引入“对齐度”指标，综合评估样本的分类与回归质量来筛选正样本。在DOTA-v1.0数据集上，BFA-Net取得了75.36%的mAP，显著优于基线模型，证明了对齐学习的必要性。

*   **BSPDet** 提出了一种基于尺度和形状感知的网络，以应对遥感影像中目标尺度和形态变化剧烈的挑战 [www.dqxxkx.cn](https://www.dqxxkx.cn/CN/10.12082/dqxxkx.2025.250142)。该方法通过专门设计的模块来增强模型对目标尺度和形状特征的敏感度，从而改善在复杂场景下的检测性能。这体现了通过精细化特征工程解决特定挑战的思路。虽然摘要信息有限，但其标题和关键词指明了在特征层面解决多样性问题的研究方向。

##### **2.3 优化特征融合与注意力机制**

特征融合与注意力机制是提升小目标检测和抑制复杂背景干扰的有效手段。近期研究通过设计更精巧的模块来优化这一过程。

*   **FFCA-YOLO** 针对星载实时处理场景，提出了一种兼顾精度与效率的检测器，旨在解决小目标特征表示不足和背景干扰问题 [blog.csdn.net](https://blog.csdn.net/weixin_44184852/article/details/146707553)。该模型集成了三个即插即用的轻量化模块：特征增强模块（FEM）利用多分支空洞卷积扩展局部感受野；特征融合模块（FFM）基于通道重加权策略优化多尺度特征融合；空间上下文感知模块（SCAM）则用于捕获全局关联信息。实验表明，FFCA-YOLO及其基于部分卷积（PConv）的轻量版L-FFCA-YOLO在VEDAI、AI-TOD等小目标数据集上超越了多种基准模型。

*   **一种改进YOLOX的算法** 针对遥感图像中目标模糊、尺度差异大和背景复杂的问题，对YOLOX进行了深度优化 [opticsjournal.net](https://www.opticsjournal.net/Articles/OJd32c1abf737b6fb3/FullText)。该工作引入“区域上下文聚合模块（RCAM）”扩大感受野，“特征融合模块（FFM）”实现不同尺度特征的深度融合，并结合一种新的注意力机制“CAS”（Coordinate Attention + SimAM）来增强目标特征并忽略背景干扰。改进后的算法在DIOR数据集上mAP50提升了4.08个百分点，验证了多模块协同优化的有效性。

*   **YOLO-Shuffle-MSDA** 聚焦于YOLOv8框架的改进，通过引入ShuffleAttention模块和多尺度特征融合模块（MSDA）来提升模型对多尺度目标和复杂背景的处理能力 [pdf.hanspub.org](https://pdf.hanspub.org/csa_1543836.pdf)。ShuffleAttention通过分组和通道混洗的方式高效地结合了通道和空间注意力，MSDA则利用多尺度膨胀卷积捕获更丰富的上下文信息。在RSOD数据集上的实验结果显示，YOLO-Shuffle-MSDA在精度（P）和mAP50-95等关键指标上均优于基线YOLOv8及其他变体。

##### **2.4 遥感基础模型 (Foundation Models)**

随着大模型时代的到来，构建遥感领域的专属基础模型成为一个新的研究范式。这类模型旨在通过在海量、多源的遥感数据上进行预训练，学习通用的、可迁移的特征表示，以服务于多种下游任务。

*   一篇发表于《遥感技术与应用》的综述系统性地探讨了遥感基础模型的研究现状 [opticsjournal.net](https://www.opticsjournal.net/Articles/OJedc4236cc0216f69/FullText)。文章指出，由于遥感数据与自然图像的固有差异（如数据异质性、图文对稀缺），直接应用通用视觉大模型（如ViT、CLIP）效果受限。因此，研究界正致力于开发专门的遥感基础模型，它们通过在百万级遥感图像（单模态）或图文对（多模态）上进行自监督或有监督预训练。这些预训练模型（如FoMo-Bench，RemoteCLIP，SkySense）再通过参数高效的微调（如Adapter）适应目标检测、分割等下游任务，展现出强大的零样本或少样本学习潜力。

#### **3. 实验与评价总结**

*   **常用数据集**：此期间的研究工作广泛使用了 **DOTA** 系列、**DIOR-R**、**FAIR1M**、**HRSC2016** 等大型公开数据集进行性能评测。同时，针对小目标检测的挑战，**AI-TOD** 和研究者自建的专业数据集（如 **USOD**）也得到应用 [blog.csdn.net](https://blog.csdn.net/weixin_44184852/article/details/146707553)。
*   **评价指标**：平均精度均值（**mAP**）是核心指标，通常会报告不同IoU阈值下的结果，如 **mAP50** (宽松)、**mAP75** (严格)以及 **mAP50:95** (COCO标准)。针对小目标，还会额外评估特定尺度范围内的精度（如APs）。
*   **共性结论**：
    1.  **架构创新驱动性能提升**：采用大核卷积、条带卷积等设计（如LSKNet, Strip R-CNN）的骨干网络，在处理大尺度、高宽比和上下文依赖强的目标时，性能增益显著，并多次刷新SOTA记录。
    2.  **模块化增强成为主流**：即插即用的注意力模块、特征融合模块和上下文模块（如FFCA-YOLO, 改进的YOLOX）被证明是提升现有检测框架（尤其是YOLO系列）性能的有效手段，特别是在抑制背景噪声和增强小目标特征方面。
    3.  **解决特定问题带来稳定增益**：专门针对分支不对齐等特定瓶颈问题设计的网络（如BFA-Net），通过精细化的学习策略，能够稳定提升定向目标检测的精度。
    4.  **效率与精度并重**：轻量化设计（如L-FFCA-YOLO）和对模型参数量（#P）、计算量（FLOPs）的关注日益增多，表明研究界正积极探索在资源受限平台（如星载、机载设备）上部署高性能检测器的可行路径。

#### **4. 趋势与挑战**

基于2022-2025年的研究进展，遥感目标检测领域面临以下挑战并呈现出清晰的发展趋势 [opticsjournal.net](https://www.opticsjournal.net/Articles/OJedc4236cc0216f69/FullText)：

*   **挑战**：
    1.  **数据匮乏与异质性**：高质量、大规模、多模态的遥感标注数据（尤其是图文对）依然稀缺。不同传感器（光学、SAR、红外）的数据在分辨率、光谱和成像机理上存在巨大差异，给构建统一模型带来困难。
    2.  **模型可靠性**：预训练大模型（尤其是视觉-语言模型）可能出现“幻觉”现象，即产生与图像内容不符的描述或判断，其在关键任务中的可靠性有待验证。
    3.  **评估基准的统一性**：不同研究采用的预训练策略、数据增强技巧和微调方法各不相同，导致难以对不同模型进行绝对公平的横向比较。

*   **未来趋势**：
    1.  **领域专用基础模型（Domain-Specific Foundation Models）的深化**：构建更大规模、多模态的遥感基础模型将是未来研究的核心。这些模型将在涵盖光学、SAR、高光谱等多种数据的超大规模数据集（如LAION-5B的遥感版）上进行预训练，学习遥感领域的通用物理和语义规律，旨在通过少量样本甚至零样本实现对新任务的快速适应。
    2.  **生成式AI辅助数据扩展与融合**：利用扩散模型等生成式技术，依据文本描述或稀疏标注生成高质量、多样化的合成遥感图像，将成为解决数据匮乏问题的关键途径。这不仅能扩充训练集，还有望用于模态转换（如由SAR生成光学伪彩图），以增强多模态数据融合的效果。
    3.  **高效轻量化与端侧智能部署**：随着对实时应用的迫切需求，研究将持续关注模型轻量化技术，如部分卷积、网络剪枝和量化。目标是开发能够在卫星、无人机等边缘计算设备上直接运行的高效检测器，实现从数据采集到信息提取的“星上”或“机上”闭环，极大缩短响应延迟。
    4.  **视觉-语言联合学习的广泛应用**：视觉-语言模型（VLM）将进一步渗透遥感领域，实现更智能的人机交互。用户可以通过自然语言指令进行目标搜索（“查找所有红顶建筑”）、属性查询和零样本检测，这将颠覆传统的遥感图像解译工作流。

#### **5. 结论**

2022-2025年间，航空与卫星影像目标检测领域的研究取得了显著进展。学术界通过设计具有更大感受野和更强上下文建模能力的新型架构、优化特征融合与注意力机制、解决特定检测难题以及探索领域专用基础模型等手段，持续推动着检测精度的上限。实验结果普遍证实，针对遥感数据特性进行专门设计是提升模型性能的关键。未来，随着数据、算力和算法的协同发展，遥感目标检测将朝着更大规模、更强泛化能力、更高效率和更智能化的方向持续演进。

---

#### **6. 参考文献**

1.  程传祥, 金飞, 左溪冰, 等. BSPDet: 基于尺度和形状感知的遥感影像目标检测方法[J]. 地球信息科学学报, 2025, 27(11): 2713-2730. [www.dqxxkx.cn](https://www.dqxxkx.cn/CN/10.12082/dqxxkx.2025.250142)
2.  Yuan, X., Zheng, Z., Li, Y., et al. Strip R-CNN: Large Strip Convolution for Remote Sensing Object Detection[J]. arXiv preprint, 2025. [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/96698)
3.  张帅豪, 潘志刚. 遥感大模型：综述与未来设想[J]. 遥感技术与应用, 2025, 40(1): 1. [www.opticsjournal.net](https://www.opticsjournal.net/Articles/OJedc4236cc0216f69/FullText)
4.  曹选. Swin-transformer-based YOLOv5 for Small-Object Detection in Remote Sensing Images[J]. Sensors, 2023. [www.sibet.cas.cn](https://www.sibet.cas.cn/sourcedb/zw/lw/202403/t20240313_7026525.html)
5.  张海龙, 曾巧林, 杨杰, 等. 基于分支对齐学习的遥感图像旋转目标检测[J]. 激光与光电子学进展, 2025, 62(4): 0428005. [www.opticsjournal.net](https://www.opticsjournal.net/Articles/OJe5fbf04e3ca9f35d/FullText)
6.  李宇轩, 李翔, 戴一冕, 等. LSKNet: 针对遥感图像分析的轻量级基础骨干网络[J]. International Journal of Computer Vision (IJCV), 2025. [mftp.mmcheng.net](https://mftp.mmcheng.net/Papers/24IJCV-LSK-CN.pdf)
7.  胡昭华, 李昱辉. 基于改进YOLOX的遥感目标检测算法[J]. 激光与光电子学进展, 2024, 61(12): 1228004. [www.opticsjournal.net](https://www.opticsjournal.net/Articles/OJd32c1abf737b6fb3/FullText)
8.  李聪慧. 基于注意力机制的遥感目标检测方法研究与实现[J]. 计算机科学与应用, 2025, 15(11): 234-246. [pdf.hanspub.org](https://pdf.hanspub.org/csa_1543836.pdf)
9.  姚婷婷, 肇恒鑫, 冯子豪, 等. 上下文感知多感受野融合网络的定向遥感目标检测[J]. 电子与信息学报, 2025, 47(1): 233-243. [www.jeit.ac.cn](https://www.jeit.ac.cn/cn/article/doi/10.11999/JEIT240560?viewType=HTML)
10. Wei, X., et al. FFCA-YOLO for Small Object Detection in Remote Sensing Images[J]. IEEE Transactions on Geoscience and Remote Sensing (TGRS), 2025. [blog.csdn.net](https://blog.csdn.net/weixin_44184852/article/details/146707553)
11. HAN J M, DING J, LI J, et al. Align deep features for oriented object detection[J]. IEEE Transactions on Geoscience and Remote Sensing, 2021, 60: 5602511. [www.opticsjournal.net](https://www.opticsjournal.net/Articles/OJe5fbf04e3ca9f35d/FullText#Ref_3)
12. XIE X, CHENG G, WANG J, et al. Oriented R-CNN for object detection[C]. 2021 IEEE/CVF International Conference on Computer Vision (ICCV), 2021: 3520–3529. [www.jeit.ac.cn](https://www.jeit.ac.cn/cn/article/doi/10.11999/JEIT240560?viewType=HTML#b2)
13. Kirillov, A., Mintun, E., Ravi, N., et al. Segment anything[C]. Proceedings of the IEEE/CVF International Conference on Computer Vision, 2023: 4015-4026. [www.opticsjournal.net](https://www.opticsjournal.net/Articles/OJedc4236cc0216f69/FullText#Ref_8)
14. Dosovitskiy, A., Beyer, L., Kolesnikov, A., et al. An image is worth 16x16 words: Transformers for image recognition at scale[J]. arXiv Preprint, 2020. [www.opticsjournal.net](https://www.opticsjournal.net/Articles/OJedc4236cc0216f69/FullText#Ref_9)
15. Radford, A., Kim, J. W., Hallacy, C., et al. Learning transferable visual models from natural language supervision[C]. International Conference on Machine Learning, PMLR, 2021: 8748-8763. [www.opticsjournal.net](https://www.opticsjournal.net/Articles/OJedc4236cc0216f69/FullText#Ref_5)