# 医学图像分割技术与应用综述（2022–2025）

## 引言

医学图像分割作为计算机辅助诊断的核心环节，其目标是精确识别解剖结构或病灶区域。2022–2025年间，深度学习方法尤其是基于Transformer和通用分割模型的架构，显著推动了该领域的发展。传统U-Net及其变体虽在局部特征提取方面有效，但在建模长程依赖和泛化能力上存在局限。近年来，混合CNN-Transformer架构、可提示分割模型（如SAM）的适配、以及新兴状态空间模型（如Mamba）的引入，极大提升了分割精度与鲁棒性。本文系统梳理2022–2025年间在该领域的代表性工作，并总结实验评价范式与未来趋势。

## 方法分类与代表作

### 1. CNN-Transformer混合架构
此类方法结合CNN的局部细节建模能力和Transformer的全局上下文建模优势，成为医学图像分割的主流范式。

* **TransUNet**（Chen et al., arXiv 2021，影响力延续至2024）[hanspub.org](https://pdf.hanspub.org/acm_8104511.pdf)：针对医学图像中病灶边界模糊、对比度低的问题，提出将CNN（如ResNet）作为编码器提取低级特征，再由纯Transformer编码器建模全局依赖。在多个数据集（如Synapse）上，其Dice系数平均高出U-Net约2.5–3个百分点，尤其在小器官分割任务中优势显著。

* **SwinUNet**（Cao et al., ECCV Workshops 2022）[opticsjournal.net](https://www.opticsjournal.net/Articles/OJ2b2078a8cf027f69/km)：构建了纯Transformer的U-Net结构，利用Swin Transformer的移窗机制降低计算复杂度。实验表明，该模型在保持全局建模能力的同时，对多尺度器官分割任务（如腹部多器官）表现优异，Dice系数可达79.13%。

* **改进SwinUNet**（檀文文等，计算机科学与应用 2025）[hanspub.org](https://pdf.hanspub.org/csa_1543783.pdf)：为解决SwinUNet在多尺度建模和跨层特征融合上的不足，引入Focal Transformer以增强局部与全局交互，采用ASPP模块扩展感受野，并设计Tokenized Interaction Fusion（TIF）模块优化跳跃连接。在Synapse数据集上，该方法Dice系数达79.89，HD95降至19.73，优于基线。

### 2. 可提示通用分割模型（SAM）的医学适配
SAM的出现为通用医学图像分割提供了新范式，但其在医学图像上的直接应用效果不佳，催生了大量微调与适配工作。

* **MedSAM**（Ma et al., arXiv 2023）[hanspub.org](https://pdf.hanspub.org/acm_8104511.pdf)：首个面向通用医学图像分割的基础模型，通过在包含超百万图像-掩码对的医学数据集上微调SAM。在颅内出血、胶质瘤等任务中，其Dice中位数分别达到94.0%和94.4%，显著优于U-Net，且展现出良好的跨模态泛化能力。

* **SAM-Med2D**（Cheng et al., arXiv 2023）[opticsjournal.net](https://www.opticsjournal.net/Articles/OJda3bfaa1dd74a3a/FullText)：构建了包含460万图像和1970万掩码的大规模医学分割数据集，并在此基础上对SAM进行全面微调。该模型在MICCAI 2023的9个挑战赛数据集上验证了其泛化能力，证明了大规模、高质量数据对提升SAM医学性能的关键作用。

* **MedSAM2**（Ma et al., 2025）[baai.ac.cn](https://hub.baai.ac.cn/paper/279a8711-cf36-4ca8-b9c9-1f7c35eec72e)：将SAM2微调至3D医学图像和视频分割任务，利用超45.5万3D图像-掩码对进行训练。用户研究表明，该模型可将人工标注成本降低超过85%，并在CT、MRI和超声心动图等多种模态上实现高性能分割。

### 3. 新兴架构：状态空间模型（SSM）与混合模型
为克服Transformer高计算复杂度的缺点，研究者开始探索基于状态空间模型（如Mamba）的高效架构。

* **VMDC-Unet**（王劭羽等，建模与仿真 2025）[hanspub.org](https://www.hanspub.org/journal/paperinformation?paperid=112526)：针对结直肠癌病理图像分割，提出融合VMamba（视觉Mamba）与CNN的混合架构。该模型利用VMamba处理长距离依赖，并通过改进的ConvNext模块增强局部特征。在SJTU_GSFPH和Glas数据集上，其Dice系数分别达到88.51%和91.63，优于纯Transformer模型且计算效率更高（FLOPs仅6.66亿）。

* **DB-SAM**（Qin et al., arXiv 2024）[chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/64809)：为弥合SAM与医学图像间的领域差距，设计了双分支适配框架，包含一个冻结的ViT分支（辅以通道注意力）和一个轻量级卷积分支。通过双边交叉注意力进行特征融合，在21个3D分割任务上相比现有医学SAM适配器实现了8.8%的绝对性能提升。

### 4. 多模态与特定任务分割
针对临床中多模态成像（如PET/CT）和特定病种的需求，专用分割模型持续发展。

* **MSP-YOLACT**（周涛等，光子学报 2025）[opticsjournal.net](https://www.opticsjournal.net/Articles/OJec7c2770705b1731/FullText)：面向多模态PET/CT肺部肿瘤实例分割，设计了多模态特征混合器（MFM）以融合不同模态的病灶共性特征，并通过增强特征金字塔和并行特征增强预测头提升定位能力。在临床数据集上，其mAPseg达65.41%，有效解决了多模态信息互补性利用不足的问题。

* **CPCATNet**（曾安等，广东工业大学学报 2025）[rhhz.net](https://html.rhhz.net/GDGYDXXB/html/1736152746337-1505189003.htm)：针对肺部肿瘤分割中对比度低、边界模糊的挑战，提出基于Transformer与通道优先卷积注意力机制的网络。在编码器中引入全局-局部注意力（GLA），在跳跃连接中使用CPCA模块动态分配权重。在GDPH和LUNG1数据集上，Dice系数分别达到90.96%和88.18%，显著优于TransUNet等基线模型。

## 实验与评价总结

2022–2025年的医学图像分割研究在实验评价上形成了较为一致的范式。**评价指标**方面，Dice相似系数（DSC）和95% Hausdorff距离（HD95）成为衡量分割精度与边界质量的黄金标准。**数据集**方面，研究普遍在公开基准（如LiTS、BraTS、Synapse、AMOS）和私有临床数据集上进行验证，以评估模型的泛化能力。共性结论包括：1) 混合架构（CNN-Transformer或CNN-SSM）在精度与效率上取得最佳平衡；2) 通用模型（如SAM）通过大规模医学数据微调后，其零样本和少样本泛化能力显著提升；3) 多模态融合、注意力机制优化和特征交互设计是提升复杂病灶分割性能的关键；4) 模型在单中心数据上表现优异，但在多中心、异构数据上的性能退化问题依然突出。

## 趋势与挑战

基于近期工作，2025年前后的医学图像分割研究将呈现以下趋势：
1.  **基础模型与通用分割的深化**：以MedSAM2为代表，3D/4D（视频）通用分割基础模型将成为标配，研究重点将转向如何高效利用其进行零样本、少样本分割，并与临床工作流（如PACS、TPS）无缝集成。
2.  **高效架构与自监督学习的结合**：VMamba等状态空间模型因其线性计算复杂度，将更多地替代Transformer。同时，自监督和弱监督学习将与这些高效架构结合，以缓解对大规模像素级标注的依赖。
3.  **多模态、多任务与临床闭环**：分割模型将不再孤立，而是作为智能诊疗系统的一部分，与诊断、治疗规划、随访预测等下游任务联动。融合图像、文本报告、病理和基因组等多模态信息的跨模态大模型（如MedCLIP的延伸）将成为新方向。

核心挑战在于：如何解决模型的跨中心泛化问题、提升对小病灶和模糊边界的分割鲁棒性、构建可解释且医生可信赖的人机协同系统，以及确保在数据隐私合规前提下的模型部署与更新。

## 结论

2022–2025年是医学图像分割技术从专用模型向通用、智能、高效范式跃迁的关键时期。以TransUNet、SwinUNet为代表的混合架构奠定了高性能分割的基础，而SAM及其医学适配版本（MedSAM、MedSAM2）则开启了通用分割的新纪元。新兴的VMamba等高效模型为实时临床部署提供了可能。未来，该领域将朝着构建更通用、更高效、更智能且与临床深度耦合的分割系统方向发展。

## 参考文献

1.  Chen, J., Lu, Y., Yu, Q., et al. (2021). TransUNet: Transformers Make Strong Encoders for Medical Image Segmentation. *arXiv:2102.04306*.
2.  Cao, H., Wang, Y., Chen, J., et al. (2023). Swin-Unet: Unet-Like Pure Transformer for Medical Image Segmentation. In *Computer Vision—ECCV 2022 Workshops*. Springer.
3.  檀文文, 卢棚, 姜韦. (2025). 基于改进 SwinUNet 腹部多器官分割算法研究. *计算机科学与应用*, *15*(10), 318-326.
4.  Ma, J., Li, H., Xu, Y., et al. (2023). MedSAM: Segment Anything Model for Medical Images. *arXiv:2306.14452*.
5.  Cheng, J., Ye, J., Deng, Z., et al. (2023). SAM-Med2D. *arXiv:2308.16184*.
6.  Ma, J., Yang, Z., Kim, S., et al. (2025). MedSAM2: Segment Anything in 3D Medical Images and Videos. *智源社区*.
7.  王劭羽, 陈庆奎, 黄陈. (2025). 基于VMamba-CNN混合的结直肠癌切片图像分割. *建模与仿真*, *14*(4), 799-810.
8.  Qin, C., Cao, J., Fu, H., et al. (2024). DB-SAM: Delving into High Quality Universal Medical Image Segmentation. *arXiv:2410.04172*.
9.  周涛, 柴文文, 王亚星, 等. (2025). MSP-YOLACT：面向多模态PET/CT肺部肿瘤医学图像的实例分割模型. *光子学报*, *54*(4), 0410003.
10. 曾安, 王丹, 杨宝瑶, 等. (2025). 基于Transformer与注意力机制的肺部肿瘤分割方法. *广东工业大学学报*, *42*(1), 24-32.
11. 路德昊, 王媛菲, 张景然. (2025). 基于深度学习的CT图像分割技术在自动勾画中的研究进展与应用. *临床医学进展*, *15*(7), 689-699.
12. 吴曈, 胡浩基, 冯洋, 等. (2024). 分割一切模型（SAM）在医学图像分割中的应用. *中国激光*, *51*(21), 2107102.