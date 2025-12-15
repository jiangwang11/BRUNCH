## State Space Models for Semantic Segmentation in Remote Sensing 的中文学术综述 (2022–2025)

### 引言

遥感图像语义分割是地球观测领域的一项关键任务，旨在将遥感图像中的每个像素精确分类为不同的语义类别，为地质调查、城市规划和灾害检测等应用提供重要支持。传统的卷积神经网络（CNN）和基于Transformer的模型在遥感语义分割中取得了显著进展。然而，CNN受限于其局部感受野，难以有效捕获长距离依赖关系，而Transformer虽然能有效建模全局信息，却面临高计算复杂度和在低维语义信息提取上的局限性。

近年来，状态空间模型（State Space Model, SSM），尤其是Mamba及其变体，因其在处理长序列数据时的线性计算复杂度和捕捉长距离依赖关系的优势，逐渐成为遥感图像语义分割领域的新兴研究方向。本文将对2022-2025年间利用状态空间模型进行遥感图像语义分割的代表性工作进行综述，分析其核心方法、实验结论，并展望未来的研究趋势与挑战。

### 方法分类与代表作

目前，将SSM应用于遥感图像语义分割的方法主要可分为以下几类：

#### 1. 基于纯Mamba或SSM架构的模型

这类方法直接将Mamba或其变体作为骨干网络，或核心模块，以其线性复杂度和全局建模能力取代传统的CNN或Transformer结构。

*   **Samba: Semantic Segmentation of Remotely Sensed Images with State Space Model (2024)** [blog.csdn.net](https://blog.csdn.net/CVHub/article/details/137410927)
    *   **研究问题：** 高分辨率遥感图像的语义分割面临CNN感受野受限和ViT计算开销巨大的挑战。
    *   **核心方法：** 首次将Mamba架构引入遥感图像语义分割任务。Samba采用编码器-解码器结构，其中Samba块作为编码器用于多级语义信息的高效提取，UperNet作为解码器。Samba块中Mamba取代了ViT中的多头自注意力机制，以线性复杂度捕捉全局语义信息。
    *   **关键实验结论：** 在LoveDA数据集上，Samba的mIoU性能优于CNN-based和ViT-based的最先进模型，展现了Mamba作为遥感高分图像新一代骨干网络的潜力。

*   **PPMamba: A Pyramid Pooling Local Auxiliary SSM-Based Model for Remote Sensing Image Semantic Segmentation (2025)** [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/58227)
    *   **研究问题：** 传统CNN和Transformer在遥感语义分割中面临捕捉长距离依赖和局部语义信息保留不足的问题。
    *   **核心方法：** 提出金字塔池化Mamba (PPMamba)，结合CNN和Mamba。核心的PP-SSM模块融合局部辅助机制和全向状态空间模型（OSS），OSS从八个方向扫描特征图，金字塔形卷积分支提取多尺度局部特征。
    *   **关键实验结论：** 在ISPRS Vaihingen和LoveDA Urban数据集上，PPMamba在性能上与最先进的模型具有竞争力。

*   **RS$^3$Mamba: Visual State Space Model for Remote Sensing Image Semantic Segmentation (2025)** [blog.csdn.net](https://blog.csdn.net/gaoxiaoxiao1209/article/details/142139032)
    *   **研究问题：** CNN和Transformer在遥感语义分割中分别受限于长距离建模能力和高计算复杂性。
    *   **核心方法：** 提出双分支网络RS$^3$Mamba，利用VSS块构建辅助分支以提供全局信息，辅助基于卷积的主分支进行特征提取。引入协同补全模块（CCM）以自适应机制精炼和融合双编码器特征。
    *   **关键实验结论：** 在ISPRS Vaihingen和LoveDA Urban数据集上，RS$^3$Mamba的mIoU分别达到0.66%和1.70%，优于当时最好的方法，验证了其有效性和潜力。

#### 2. SSM与多模态/异构数据融合的模型

这类方法利用SSM的优势，结合多模态遥感数据（如可见光、SAR、激光雷达等）或异构图结构，解决遥感图像语义分割中的复杂性。

*   **基于异质图和Mamba的跨模态遥感语义分割 (2025)** [arocmag.cn](https://www.arocmag.cn/abs/2025.05.0225)
    *   **研究问题：** 可见光遥感影像语义分割中存在跨模态特征异构性显著及深层语义交互效率低下问题。
    *   **核心方法：** 提出跨模态异质图引导的Mamba网络（CHGMNet）。设计跨模态异构特征对齐模块（CHFAM），利用异质图卷积构建可学习特征相似性度量，实现光谱-几何特征校准。创新性提出多路径融合Mamba模块（MPFM），捕获多层次融合特征并提高计算效率。
    *   **关键实验结论：** 在Vaihingen和Potsdam数据集上，CHGMNet在mIoU、mF1和OA等指标上显著优于现有主流方法，验证了其在跨模态遥感解译任务中的优越性。

*   **CVS-Net：基于时空关系建模与边缘信息强化的遥感影像语义变化检测方法 (2025)** [dqxxkx.cn](https://www.dqxxkx.cn/CN/article/showChannelArticle.do?id=997)
    *   **研究问题：** 现有语义变化检测方法对遥感影像的局部和全局特征利用不足，忽略时空依赖性，且变化对象边缘模糊。
    *   **核心方法：** 提出CVS-Net网络，融合CNN与VSSM，结合CNN局部特征提取与VSSM长距离依赖捕捉能力。嵌入基于VSSM的双向时空关系建模模块，引导网络理解时空变化逻辑。提出边缘感知强化分支，通过联合拉普拉斯算法和多任务架构增强模型边缘识别精度。
    *   **关键实验结论：** 在SECOND和FZ-SCD数据集上，CVS-Net在分离卡帕系数（SeK）和平均交并比（mIoU）上优于其他对比方法，验证了该方法有效提升语义变化检测的属性和几何精度。

#### 3. SSM与其他深度学习范式的结合模型

这类方法将SSM与其他有效的深度学习技术（如CNN、Transformer、图神经网络等）相结合，以弥补SSM在某些方面的不足，或增强模型的综合性能。

*   **SHW-Stacking：精准捕捉降水空间异质性的加权堆叠遥感日降水产品质量提升方法 (2025)** [dqxxkx.cn](https://www.dqxxkx.cn/CN/article/showChannelArticle.do?id=997)
    *   **研究问题：** 现有逐日卫星降水产品在局部降水细节捕捉和部分区域误差较大方面存在不足。
    *   **核心方法：** 提出SHW-Stacking方法，用于提升遥感日降水产品质量。方法首先耦合特征重要性与非线性相关性进行自适应特征优选。利用高斯混合聚类获得描述日降水空间异质性的同质子区。最后构建加权堆叠机器学习模型融合SPP与站点数据。
    *   **关键实验结论：** 在中国区域2016-2020年逐日IMERG降水数据上的实验表明，SHW-Stacking在日、季和年尺度上MAE分别至少降低4.6%、3.1%和2.7%，KGE分别至少提高3.4%、1.9%和2.0%。

*   **DMFPNet：增强多尺度目标感知的双路径高分辨率遥感图像分割算法 (2025)** [dqxxkx.cn](https://www.dqxxkx.cn/CN/article/showChannelArticle.do?id=997)
    *   **研究问题：** 高分辨率遥感图像语义分割存在类内方差大、类间方差小、目标尺度变化显著等问题，传统CNN受限，Transformer在局部信息提取方面有缺陷。
    *   **核心方法：** 提出DMFPNet，采用基于DCNN和Transformer的非对称双编码器结构。构建可变通道空间金字塔模块（SCSP）动态提取融合多通道信息。提出多尺度特征增强Transformer模块，通过特征锚点预处理和可学习余弦相似矩阵，引导模型聚焦不同尺度目标。构建双边特征引导融合模块(BFGF)实现双分支信息交换。
    *   **关键实验结论：** 在Vaihingen和Potsdam数据集上，DMFPNet的mIoU分别提升0.76%和1.42%相较于对比方法，证明了在处理类内类间方差大、目标尺度多变等复杂问题方面的良好性能。

*   **MDSNet：多尺度深度监督高分辨遥感图像语义分割方法 (2025)** [dqxxkx.cn](https://www.dqxxkx.cn/CN/article/showChannelArticle.do?id=997)
    *   **研究问题：** 遥感图像包含大量空间与语义特征，但现有方法在有效提取融合二者方面存在不足，导致边缘分割不完整，且忽略边缘信息的精确提取。
    *   **核心方法：** 针对空间与语义特征分别设计特征提取分支，引入空间去冗余残差模块（结合小波变换和坐标卷积）聚焦空间特征和边缘特征。语义分支加入残差注意力Mamba提取全局语义特征。特征融合采用多尺度融合机制，设计大内核分组特征提取模块逐层融合特征。采用深度监督机制，添加辅助监督头提高训练效率。
    *   **关键实验结论：** 在ISPRS Potsdam和随机采样裁剪数据增强后的Vaihingen数据集上，平均交并比达到83.43%和86.49%，相比9种最新方法至少提高了5.00%和3.00%。

### 实验与评价总结

**数据集与评估指标：**
遥感图像语义分割任务普遍采用ISPRS Vaihingen、ISPRS Potsdam、LoveDA Urban以及SAMRS等公开数据集进行模型性能评估。这些数据集涵盖了不同的空间分辨率（9 cm、5 cm、0.3 米等），包含多样化的地物类别，如不透水面、建筑物、低矮植被、树木、汽车等，为模型在复杂场景下的泛化能力提供了测试。常用的评估指标包括平均交并比（mIoU）、总体准确率（OA）、F1分数（mF1）以及在特定任务中使用的分离卡帕系数（SeK）等。

**模型性能共性结论：**
本综述中提及的基于SSM的方法普遍展现出超越传统CNN和纯Transformer模型的性能。特别地，Mamba及其变体能够有效解决传统方法在处理高分辨率遥感图像时面临的挑战：
1.  **长距离依赖建模：** SSM的线性计算复杂度和全局信息捕获能力使其在处理遥感图像中的长距离上下文信息时表现出色，克服了CNN有限感受野的缺陷。
2.  **计算效率：** 相比于Transformer的二次方计算复杂度，SSM的线性复杂度在处理长序列或高分辨率图像时展现出显著的计算效率优势。
3.  **多尺度特征融合：** SSM与其他模块（如金字塔池化、CNN分支、Transformer模块）结合后，能够更有效地提取和融合多尺度特征，提升对不同大小目标的识别能力。
4.  **边缘细节与语义一致性：** 引入边缘细化损失函数、空间去冗余残差模块或边缘感知强化分支等机制，提高了模型对目标边缘的识别精度和分割的完整性，缓解了边缘模糊和误分类问题。
5.  **跨模态/异构数据处理：** SSM与其他深度学习范式结合的模型，如基于异质图的Mamba网络，能够有效处理多模态和异构特征，缓解模态间维度失配，提升复杂场景下的分割精度。

### 趋势与挑战

**趋势：**

1.  **Mamba/SSM成为主流骨干网络：** 随着Mamba模型在长序列建模方面的优势日益凸显，预计2025年前后，Mamba或其改进型将成为遥感语义分割领域中与CNN和Transformer并列的主流骨干网络之一，并涌现更多基于Mamba的编码器-解码器架构。
2.  **多模态融合与跨域适应性增强：** 遥感领域海量多源异构数据的特点将推动SSM与多模态学习的深度融合。研究将聚焦于SSM如何有效整合光学、SAR、高光谱、LiDAR等多元数据，并增强模型的跨地域、跨场景泛化能力，减少对特定数据集的依赖。
3.  **轻量化与高效部署：** 尽管Mamba具有线性复杂度，但在遥感图像处理中仍面临模型复杂度和部署效率的挑战。未来的研究将致力于轻量化Mamba模型设计，探索模型压缩、量化和知识蒸馏等技术，以实现在星载实时处理或边缘设备上的高效部署。
4.  **结合基础模型(Foundation Models)范式：** 遥感大模型将借鉴视觉和语言基础模型的发展范式，利用SSM的强大表示能力，在无监督或自监督预训练下学习通用遥感特征，并通过少量样本或零样本学习适应下游语义分割任务。

**挑战：**

1.  **局部精细度与细节保留：** 尽管SSM在全局建模方面表现优异，但在捕捉遥感图像中细微的局部细节和纹理特征时，可能仍不如强卷积网络。如何平衡SSM的全局视野与局部精细度是重要挑战。
2.  **对标注数据的依赖：** 虽然SSM旨在减少对大量标注数据的需求，但多数高性能模型仍依赖于高标注质量的训练集。研发更高效的自监督或半监督学习策略，进一步降低对人工标注的依赖，是持续的挑战。
3.  **模型可解释性：** 深度学习模型，包括SSM在内，通常被视为“黑箱”。提升SSM在遥感语义分割中的可解释性，理解其决策过程，对于模型的可靠性和在关键应用领域的采纳至关重要。
4.  **超参数敏感性与优化：** SSM模型的复杂结构可能导致超参数敏感性较高，模型优化和收敛可能更具挑战性，需要更精细的调优策略。

### 结论

本综述系统回顾了2022-2025年间状态空间模型（SSM）在遥感图像语义分割领域的应用进展。Mamba及其变体的引入，通过其独特的序列建模能力和线性计算复杂度，有效弥补了传统CNN在长距离依赖捕获上的不足以及Transformer在高计算开销上的限制。代表性工作展示了SSM在纯架构应用、多模态异构数据融合以及与其他深度学习范式结合方面的巨大潜力，并在多个标准遥感数据集上取得了优于现有主流方法的性能。

尽管SSM在遥感语义分割中展现出显著优势，但仍面临如何平衡全局与局部细节、降低对标注数据依赖、提升模型可解释性及优化超参数等挑战。展望未来，Mamba/SSM有望成为遥感领域的核心骨干网络，尤其是在多模态融合、轻量化部署和结合基础模型范式方面将迎来更多突破，为遥感智能解译带来新的范式和机遇。

### 参考文献

*   [blog.csdn.net](https://blog.csdn.net/CVHub/article/details/137410927) Samba: Semantic Segmentation of Remotely Sensed Images with State Space Model. (2024).
*   [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/58227) Hu, Y., Ma, X., Sui, J., & Pun, M.-O. (2025). PPMamba: A Pyramid Pooling Local Auxiliary SSM-Based Model for Remote Sensing Image Semantic Segmentation.
*   [blog.csdn.net](https://blog.csdn.net/gaoxiaoxiao1209/article/details/142139032) RS$^3$Mamba: Visual State Space Model for Remote Sensing Image Semantic Segmentation. (2025).
*   [arocmag.cn](https://www.arocmag.cn/abs/2025.05.0225) 叶志伟, 冯青阳, 刘明明, 王苑, 高榕, & 严灵毓. (2025). 基于异质图和Mamba的跨模态遥感语义分割. *计算机应用研究*, *43*(2).
*   [dqxxkx.cn](https://www.dqxxkx.cn/CN/article/showChannelArticle.do?id=997) 刘宣广, 李玉洁, 张振超, 戴晨光, 张昊, 缪毓喆, 朱涵, & 卢金浩. (2025). CVS-Net：基于时空关系建模与边缘信息强化的遥感影像语义变化检测方法. *地球信息科学学报*, *27*(5), 1144-1162.
*   [dqxxkx.cn](https://www.dqxxkx.cn/CN/article/showChannelArticle.do?id=997) 杨淑凡, 李艳艳, 王兴杰, 杨子明, 徐联中, 洪壮壮, 潘宏铭, & 陈传法. (2025). SHW-Stacking：精准捕捉降水空间异质性的加权堆叠遥感日降水产品质量提升方法. *地球信息科学学报*, *27*(5), 1179-1194.
*   [dqxxkx.cn](https://www.dqxxkx.cn/CN/article/showChannelArticle.do?id=997) 罗健伟, & 张银胜. (2025). DMFPNet：增强多尺度目标感知的双路径高分辨率遥感图像分割算法. *地球信息科学学报*, *27*(5), 1195-1213.
*   [dqxxkx.cn](https://www.dqxxkx.cn/CN/article/showChannelArticle.do?id=997) 单慧琳, 王兴涛, 刘文星, 吴心悦, 高润泽, & 李红旭. (2025). MDSNet：多尺度深度监督高分辨遥感图像语义分割方法. *地球信息科学学报*, *27*(6), 1381-1400.
*   [zjujournals.com](https://www.zjujournals.com/eng/article/2025/1008-973X/20250413.shtml) 张振利, 胡新凯, 李凡, 冯志成, & 陈智超. (2025). 基于CNN和Efficient Transformer的多尺度遥感图像语义分割算法. *浙江大学学报(工学版)*, *59*(4), 778-786.
*   [dqxxkx.cn](https://www.dqxxkx.cn/CN/10.12082/dqxxkx.2024.230729) 王志华, 杨晓梅, 张俊瑶, 刘晓亮, 李连发, 董文, & 贺伟. (2025). 面向复杂自然场景的遥感地学分区智能解译框架及初探. *地球信息科学学报*, *27*(2), 305-330.
*   [html.rhhz.net](https://html.rhhz.net/ZGKXYDXXB/1698194467808-62919333.htm) 王寅达, 陈嘉辉, 彭玲, 李兆博, & 杨丽娜. (2025). 高分辨率关系图卷积网络遥感语义分割方法. *中国科学院大学学报*, *42*(1), 107-115.
*   [opticsjournal.net](https://www.opticsjournal.net/Articles/OJedc4236cc0216f69/FullText) 张帅豪, 潘志刚. (2025). 遥感大模型：综述与未来设想. *遥感技术与应用*, *40*(1), 1.