## 遥感图像目标检测研究综述 (2022-2025)

### 引言

遥感图像目标检测在环境监测、城市规划、军事侦察等领域具有广泛应用价值。然而，与自然图像目标检测相比，遥感图像受限于高空俯视视角、目标尺度多样性、背景复杂性、密集排列以及旋转不变性等特点，使其面临独特的挑战。传统的基于深度学习的目标检测方法在处理这些特殊性时常表现出局限性。近年来，随着大模型和Transformer架构的兴起，遥感目标检测技术取得了显著进展。本综述旨在梳理2022年至2025年期间遥感图像目标检测的代表性工作，总结其方法类别、关键成果，并对未来发展趋势进行展望。

### 方法分类与代表作

本节将遥感图像目标检测方法分为以下几类，并选取最具代表性的工作进行阐述。

#### 1. 基于Transformer和大型卷积核的方法

该类方法着重于利用Transformer的全局建模能力或大核卷积的自适应感受野来解决遥感图像中目标上下文依赖性强、尺度变化大等问题。

*   **LSKNet: An Adaptive Large Kernel Network for Remote Sensing Object Detection** [mftp.mmcheng.net](https://mftp.mmcheng.net/Papers/24IJCV-LSK-CN.pdf)

    该研究指出遥感图像中目标识别高度依赖上下文信息，且不同目标所需的上下文范围差异显著。为此，提出了一种名为LSKNet的轻量级自适应大核卷积骨干网络。LSKNet通过动态调整其大空间感受野来模拟遥感场景中各种目标的不同范围上下文，并采用空间选择机制对大核深度可分离卷积核处理的特征进行加权和空间合并。LSKNet在DOTA、HRSC2016、FAIR1M和SAR-Aircraft等多个遥感目标检测基准数据集上显著提升了性能，同时在场景分类、语义分割和变化检测任务中也表现出色，验证了其作为高效特征提取骨干网络的潜力。
*   **Strip R-CNN: Large Strip Convolution for Remote Sensing Object Detection** [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/96698)

    该工作致力于解决遥感图像中高长宽比物体检测的挑战。研究表明大条带卷积在遥感目标检测中是良好的特征表示学习器。作者基于大条带卷积构建了Strip R-CNN，一个简单、高效且强大的网络架构，利用顺序正交的大条带卷积来捕捉空间信息。通过解耦检测头并为定位头配备条带卷积，Strip R-CNN增强了目标定位能力。该方法在DOTA、FAIR1M、HRSC2016和DIOR等基准测试中取得了显著改进，并在DOTA-v1.0上达到了82.75%的mAP，创造了新的最先进水平。
*   **上下文感知多感受野融合网络的定向遥感目标检测** [jeit.ac.cn](https://www.jeit.ac.cn/cn/article/doi/10.11999/JEIT240560?viewType=HTML)

    该文针对遥感图像目标种类多、尺度变化大和背景信息丰富等特点，设计了一种上下文感知多感受野融合网络。该网络通过在特征金字塔前四层构建感受野扩张模块，增强了网络对不同尺度遥感目标的感知能力。高层特征聚合模块将高层语义信息融合到低层特征中，有效整合了多尺度上下文信息。此外，该方法还在双阶段定向目标检测框架下设计了特征细化区域建议网络，提升了提案准确性。在DIOR-R和HRSC2016数据集上的实验表明，该方法能够实现更准确的检测。

#### 2. 注意力机制与特征融合增强方法

此类方法主要通过引入各种注意力机制和改进特征融合策略，以增强模型对关键信息的关注、抑制背景干扰并更有效地整合多尺度特征。

*   **FFCA-YOLO for Small Object Detection in Remote Sensing Images** [blog.csdn.net](https://blog.csdn.net/weixin_44184852/article/details/146707553)

    该工作针对遥感图像中小目标特征表示不足和背景干扰问题，提出了一种名为FFCA-YOLO的高效检测器。该模型包含特征增强模块（FEM）通过多分支空洞卷积扩展感受野，特征融合模块（FFM）通过通道信息重加权改进融合策略，以及空间上下文感知模块（SCAM）通过全局池化引导像素学习空间与通道间的关联关系。FFCA-YOLO及其轻量版L-FFCA-YOLO在VEDAI、AI-TOD和USOD等数据集上取得了优越性能，证明了其在遥感小目标检测方面的潜力。
*   **基于注意力机制的遥感目标检测方法研究与实现** [pdf.hanspub.org](https://pdf.hanspub.org/csa_1543836.pdf)

    该文提出了一种基于YOLOv8改进的遥感目标检测模型YOLO-Shuffle-MSDA，旨在提升检测精度和鲁棒性。模型通过引入ShuffleAttention模块优化特征提取，有效区分目标与复杂背景。多尺度特征融合模块（MSDA）则通过多尺度膨胀注意力机制增强模型对多尺度目标的检测能力。该模型在参数量和计算复杂度方面保持了相对较低的标准，同时在RSOD数据集上显著提高了检测精度。
*   **Swin-transformer-based YOLOv5 for Small-Object Detection in Remote Sensing Images** [sibet.cas.cn](https://www.sibet.cas.cn/sourcedb/zw/lw/202403/t20240313_7026525.html)

    该研究将Swin Transformer架构引入YOLOv5模型中，用于遥感图像中的小目标检测。Swin Transformer的层次化设计和移位窗口机制有助于捕捉不同尺度的特征并降低计算复杂度，这对于遥感图像中常见的密集小目标检测至关重要。通过将Swin Transformer作为骨干网络，该方法旨在提升YOLOv5在处理遥感图像中高分辨率、多尺度、小目标等方面的能力。

#### 3. 解决分支不对齐问题的定向目标检测方法

遥感图像中的物体通常具有任意方向，因此定向目标检测显得尤为重要。此类方法旨在解决分类和回归分支在预测角度信息时可能出现的不一致问题。

*   **基于分支对齐学习的遥感图像旋转目标检测** [opticsjournal.net](https://www.opticsjournal.net/Articles/OJe5fbf04e3ca9f35d/FullText)

    该文提出了一种分支特征对齐网络（BFA-Net），以解决遥感图像旋转目标检测中分类和回归分支预测不对齐的问题。BFA-Net通过分支对齐模块（BAM）加强分支间特征交互，并动态调整采样位。在样本分配阶段，通过设计的对齐度指标动态评估样本的分类和回归质量，并基于排序的分配策略筛选正样本。该算法在DOTA-V1.0、DOTA-V1.5和DIOR-R等常用数据集上取得了优异的平均精度均值，显著优于其他先进算法，同时在检测效率上也有明显优势。
*   **BSPDet: 基于尺度和形状感知的遥感影像目标检测方法** [dqxxkx.cn](https://www.dqxxkx.cn/CN/10.12082/dqxxkx.2025.250142)

    该研究提出了一种名为BSPDet的基于尺度和形状感知的遥感影像目标检测方法。BSPDet关注遥感图像中目标多尺度和多样形状的特点，通过引入特定的模块来增强模型对这些属性的感知和处理能力。该方法旨在提高遥感图像中不同尺寸和形状目标的检测精度和鲁棒性。

### 实验与评价总结

2022-2025年间的遥感图像目标检测研究在多个公开数据集上进行了广泛评估，包括DOTA系列、FAIR1M、HRSC2016、DIOR、VEDAI、AI-TOD和S2Looking等。普遍采用的评价指标包括平均精度均值（mAP）、mAP@50、mAP@75以及针对不同尺度目标的平均精度（mAPs、mAPm、mAPl）。

研究表明，上述方法在各种数据集上均取得了显著的性能提升。基于Transformer和大型卷积核的方法通过捕捉长程依赖和自适应感受野，有效处理了遥感图像中目标上下文依赖性强和尺度变化大的问题。注意力机制和特征融合增强方法则通过更精细地权重分配和特征整合，提高了模型对关键信息的关注度和对背景干扰的抑制能力，尤其在小目标检测方面表现出优势。解决分支不对齐问题的定向目标检测方法，通过优化分类和回归任务之间的协调，提高了旋转目标定位的精度。此外，轻量化模型的研发也取得进展，旨在平衡检测精度和计算效率，以满足实际部署需求。许多研究还强调了数据增强、预训练策略以及特定损失函数（如归一化Wasserstein距离NWD损失）对提升模型性能的重要性。

### 趋势与挑战

2025年前后遥感图像目标检测领域呈现以下研究趋势：

1.  **遥感大模型与基础模型的发展与应用**：随着视觉基础模型和大语言模型（如ChatGPT、Gemini、CLIP）的快速发展，遥感领域正积极探索构建专属的遥感大模型。这些模型通过在海量遥感数据上进行预训练，学习通用的表示能力，再通过微调适应各类下游任务 [opticsjournal.net](https://www.opticsjournal.net/Articles/OJedc4236cc0216f69/FullText)。未来的研究将侧重于如何克服自然图像与遥感图像的固有差异，开发更适配遥感数据复杂性（如多模态、异构性）和稀缺性（如大规模图像-文本对）的预训练范式和微调策略。
2.  **多模态数据融合的深度利用**：遥感数据来源日益丰富，涵盖可见光、红外、高光谱、SAR等多种模态。未来的研究将不再局限于单一模态数据，而是更深入地探索如何有效地融合这些多模态数据，以获取更全面、多维度的地物信息 [opticsjournal.net](https://www.opticsjournal.net/Articles/OJedc4236cc0216f69/FullText)。例如，DINO-MM [opticsjournal.net](https://www.opticsjournal.net/Articles/OJedc4236cc0216f69/FullText) 联合SAR和光学图像进行表示学习，SkySense [opticsjournal.net](https://www.opticsjournal.net/Articles/OJedc4236cc0216f69/FullText) 集成分解的多模态时空编码器。这要求模型能够处理不同时间、空间和光谱分辨率的数据，并从不同模态中提取互补的特征。
3.  **小目标和密集目标的精确检测**：遥感图像中常存在大量尺寸微小、密集分布或模糊不清的目标，这依然是当前检测任务的难点。未来的工作将继续致力于设计更为精细的特征增强和上下文感知模块，例如FFCA-YOLO [blog.csdn.net](https://blog.csdn.net/weixin_44184852/article/details/146707553) 通过FEM、FFM和SCAM增强小目标特征并抑制背景干扰。此外，结合扩散模型等生成技术，通过生成高质量合成数据来扩充稀缺的小目标训练样本，有望进一步提升小目标检测的稳健性和泛化能力 [opticsjournal.net](https://www.opticsjournal.net/Articles/OJedc4236cc0216f69/FullText)。
4.  **模型可解释性与鲁棒性的提升**：随着模型复杂度的增加，提高模型的透明度和对复杂环境的适应性变得至关重要。未来的研究将不仅关注检测精度，还将深入探讨如何增强模型在各种成像条件（如低分辨率、噪声、遮挡、天气影响）下的鲁棒性，并通过可解释性方法理解模型的决策过程，例如FFCA-YOLO [blog.csdn.net](https://blog.csdn.net/weixin_44184852/article/details/146707553) 针对图像退化条件进行了鲁棒性测试。
5.  **高效能与低功耗的边缘部署**：对于星载或无人机等有限计算资源的平台，开发轻量化、高效率的目标检测模型是重要的趋势。研究将继续探索更高效的模型架构（如基于PConv的L-FFCA-YOLO [blog.csdn.net](https://blog.csdn.net/weixin_44184852/article/details/146707553)）、模型压缩技术和硬件加速优化，实现遥感目标检测算法的实时边缘部署。

### 结论

2022年至2025年期间，遥感图像目标检测领域呈现出蓬勃发展态势。从基于Transformer与大核卷积的全局上下文建模，到注意力机制与多尺度特征融合的精细化特征增强，再到针对定向目标的专门优化，研究者们不断探索新的网络架构和训练策略，以克服遥感图像的固有挑战。遥感大模型与多模态数据融合正成为新兴热点，预示着该领域将迎来更通用、更强大的智能解译能力。同时，提升小目标检测精度、增强模型鲁棒性以及实现高效能边缘部署，仍是未来研究的重点方向。

### 参考文献

*   [dqxxkx.cn](https://www.dqxxkx.cn/CN/10.12082/dqxxkx.2025.250142) 程传祥, 金飞, 左溪冰, 林雨准, 王淑香, 刘潇. BSPDet: 基于尺度和形状感知的遥感影像目标检测方法. 地球信息科学学报, 2025, 27(11): 2713-2730.
*   [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/96698) Xinbin Yuan, ZhaoHui Zheng, Yuxuan Li, Xialei Liu, Li Liu, Xiang Li, Qibin Hou, Ming-Ming Cheng. Strip R-CNN: Large Strip Convolution for Remote Sensing Object Detection. ArXiv, 2025.
*   [opticsjournal.net](https://www.opticsjournal.net/Articles/OJedc4236cc0216f69/FullText) 张帅豪, 潘志刚. 遥感大模型：综述与未来设想. 遥感技术与应用, 2025, 40(1): 1.
*   [sibet.cas.cn](https://www.sibet.cas.cn/sourcedb/zw/lw/202403/t20240313_7026525.html) 曹选. Swin-transformer-based YOLOv5 for Small-Object Detection in Remote Sensing Images. Sensors, 2023.
*   [opticsjournal.net](https://www.opticsjournal.net/Articles/OJe5fbf04e3ca9f35d/FullText) 张海龙, 曾巧林, 杨杰, 王博为, 王承芳. 基于分支对齐学习的遥感图像旋转目标检测. 激光与光电子学进展, 2025, 62(4): 0428005.
*   [mftp.mmcheng.net](https://mftp.mmcheng.net/Papers/24IJCV-LSK-CN.pdf) 李宇轩, 李翔, 戴一冕, 侯淇彬, 刘丽, 刘永祥, 程明明, 杨健. LSKNet: 针对遥感图像分析的轻量级基础骨干网络. IJCV, 2024.
*   [opticsjournal.net](https://www.opticsjournal.net/Articles/OJd32c1abf737b6fb3/FullText) 胡昭华, 李昱辉. 基于改进YOLOX的遥感目标检测算法. 激光与光电子学进展, 2024, 61(12): 1228004.
*   [pdf.hanspub.org](https://pdf.hanspub.org/csa_1543836.pdf) 李聪慧. 基于注意力机制的遥感目标检测方法研究与实现. 计算机科学与应用, 2025, 15(11): 234-246.
*   [jeit.ac.cn](https://www.jeit.ac.cn/cn/article/doi/10.11999/JEIT240560?viewType=HTML) 姚婷婷, 肇恒鑫, 冯子豪, 胡青. 上下文感知多感受野融合网络的定向遥感目标检测. 电子与信息学报, 2025, 47(1): 233-243.
*   [blog.csdn.net](https://blog.csdn.net/weixin_44184852/article/details/146707553) FFCA-YOLO for Small Object Detection in Remote Sensing Images. TGRS, 2025
*   Wang, D., Zhang, J., Du, B., Xia, G.-S., Tao, D. An empirical study of remote sensing pretraining. IEEE Transactions on Geoscience and Remote Sensing, 2023, 61: 1-20.
*   Li, Y., Hou, Q., Zheng, Z., Cheng, M.-M., Yang, J., Li, X. Large selective kernel network for remote sensing object detection. ICCV, 2023.