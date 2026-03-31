好的，遵照您的指示，作为一名严谨的科研助手，我将基于提供的真实网络搜索结果，生成一篇关于“深度学习在生物医学图像分割”领域的中文学术综述。

***

### **面向生物医学图像分割的深度学习技术研究进展（2022-2025）**

#### **摘要**
生物医学图像分割是计算机辅助诊断与治疗的关键环节。近年来，深度学习技术，特别是卷积神经网络（CNN）和Transformer架构的融合，极大地推动了该领域的发展。本综述聚焦于2022年至2025年间的代表性工作，系统梳理了方法学的演进。内容涵盖了从高效的CNN改进模型、CNN-Transformer混合架构，到新兴的视觉状态空间模型（Mamba），以及最具颠覆性的通用分割基础模型（如SAM）的适配与微调。通过对这些方法的分类介绍与实验共性分析，本综述总结了当前研究的技术特点与性能瓶颈。最后，基于现有研究，对未来三至五年的核心研究趋势与挑战进行了预测，旨在为相关领域的研究人员提供有价值的参考。

#### **1. 引言**
生物医学图像分割旨在对医学影像（如CT、MRI、病理切片等）中的解剖结构、病灶或感兴趣区域进行像素级或体素级的精准标定。其精度直接影响着后续的定量分析、疾病诊断、手术规划和预后评估。自全卷积网络（FCN）和U-Net被提出以来，基于深度学习的方法已成为该领域的主流 [www.cjig.cn](https://www.cjig.cn/zh/article/doi/10.11834/jig.240467/)。

2022年之前，研究主流集中于对U-Net等CNN架构的优化。然而，CNN固有的局部感受野限制了其捕捉长距离依赖关系的能力。为解决此问题，研究者们开始引入在自然语言处理领域大放异彩的Transformer架构，其自注意力机制能有效建模全局上下文信息，催生了大量CNN-Transformer混合模型 [www.opticsjournal.net](https://www.opticsjournal.net/Articles/OJ2b2078a8cf027f69/km)。2023年以来，以“分割一切模型”（Segment Anything Model, SAM）为代表的通用基础模型的出现，预示着该领域可能正从“为特定任务定制模型”向“适配通用基础模型”的范式转变，带来了新的机遇与挑战 [www.opticsjournal.net](https://www.opticsjournal.net/Articles/OJda3bfaa1dd74a3a/FullText)。本综述将重点梳理2022-2025年间在上述背景下涌现的代表性工作。

#### **2. 方法分类与代表作**

##### **2.1 基于卷积神经网络（CNN）的演进模型**
尽管面临Transformer的挑战，研究者们仍致力于挖掘纯CNN架构的潜力，尤其是在计算效率与性能的平衡上。

*   **SegNeXt** 旨在重新思考语义分割中的卷积注意力设计，以应对Transformer模型高昂的计算成本。该研究提出了一种名为MSCAN（Multi-scale Convolutional Attention Network）的纯卷积编码器，它通过多尺度的大核深度卷积高效地聚合上下文信息，并以元素乘法的方式实现空间注意。实验表明，在ADE20K和Cityscapes等基准上，SegNeXt在性能与计算复杂性之间取得了优于SegFormer等主流Transformer模型的权衡，证明了精心设计的CNN架构依然具有强大的竞争力 [mftp.mmcheng.net](https://mftp.mmcheng.net/Papers/22SegNeXt.pdf)。

*   **基于可变形卷积的DeepLab v3+改进模型** 针对肝脏病理微环境中复杂边界和不规则病灶分割的难题，有研究对经典的DeepLab v3+模型进行了优化。该工作在模型的ASPP（Atrous Spatial Pyramid Pooling）模块中集成了可变形卷积，通过动态调整感受野以自适应地捕捉病灶的几何形态。结合DINO自监督预训练，该模型在仅需少量标注的情况下，对新建的肝脏病理数据集分割精度显著优于原始DeepLab v3+和U-Net，尤其在肝实质区域的IoU和Dice指标上分别达到0.84和0.90 [pdf.hanspub.org](https://pdf.hanspub.org/csa_1543657.pdf)。

##### **2.2 基于Transformer与混合架构的模型**
结合CNN的局部特征提取能力与Transformer的全局建模优势是近年来的主流范式，Swin Transformer因其窗口化自注意力的高效性而备受青睐。

*   **改进的SwinUNet** 针对SwinUNet在全局上下文建模和多尺度特征表达上的局限性，有研究提出了多项改进。该工作采用Focal Transformer替换Swin Transformer以分层注意力机制增强全局依赖；在编码器末端引入ASPP模块以扩展感受野；并在跳跃连接中加入Tokenized Interaction Fusion (TIF)模块以促进跨层信息融合。在Synapse腹部多器官分割数据集上，该改进模型的平均Dice系数（79.89%）和Hausdorff距离（19.73）均优于基线SwinUNet [pdf.hanspub.org](https://pdf.hanspub.org/csa_1543783.pdf)。

*   **C² Transformer U-Net** 该模型旨在解决U-Net在处理跨模态医学图像时信息利用不充分的问题。研究者设计了主干-辅助双U-Net编码器结构分别提取不同模态的特征，并提出多模态上下文语义感知处理器（MCAP）来有效融合跨模态的病灶信息。同时，将Transformer架构引入编解码器以捕捉上下文特征。在临床多模态肺部数据集上的实验结果显示，该模型在各项指标上表现突出，Dice系数高达96.98%，验证了其在复杂病灶分割中的高精度 [www.jeit.ac.cn](https://www.jeit.ac.cn/cn/article/doi/10.11999/JEIT220445?viewType=HTML)。

##### **2.3 视觉状态空间模型（Mamba）的初步探索**
作为Transformer的潜在替代者，状态空间模型（SSM）及其变体Mamba因其在长序列建模中展现的线性计算复杂度而受到关注。

*   **VMDC-Unet** 该研究首次将视觉状态空间模型VMamba与CNN结合，用于结直肠癌病理切片分割。为解决CNN的局部感受野和Transformer的二次方计算复杂度问题，该工作提出了一个混合U型架构，编码器采用VMamba捕获长距离依赖，解码器则使用改进的ConvNext模块强化局部细节。在SJTU_GSFPH和Glas数据集上，VMDC-Unet的分割精度与泛化能力均优于U-Net、TransUNet和Swin-Unet等基准模型，展示了Mamba架构在医学图像分割领域的应用潜力 [www.hanspub.org](https://www.hanspub.org/journal/paperinformation?paperid=112526)。

##### **2.4 通用分割基础模型（SAM）的适配与微调**
SAM的出现为医学图像分割带来了“一次性训练，普遍适用”的可能，但由于其主要基于自然图像训练，直接应用效果不佳，因此适配与微调成为研究热点。

*   **MedSAM2** 该工作旨在构建一个通用的3D医学图像和视频分割基础模型。研究者在Segment Anything Model 2 (SAM2) 的基础上，使用一个包含超过45.5万对3D图像-掩码的大规模医学数据集进行微调。实验证明，MedSAM2在多种器官、病灶和成像模态上的性能均优于先前模型。更重要的是，通过人机协作流程进行的大规模用户研究表明，该模型能将人工标注成本降低超过85% [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/279a8711-cf36-4ca8-b9c9-1f7c35eec72e)。

*   **DB-SAM** 为解决SAM在医学数据上的领域差异问题，该研究提出了一个双分支自适应SAM框架（DB-SAM）。该框架包含一个引入了可学习通道注意力的ViT分支和一个用于提取领域特定浅层特征的轻量级卷积分支。通过设计的双边交叉注意力块进行跨分支特征融合，DB-SAM有效弥合了领域鸿沟。在21个3D医学分割任务上，DB-SAM相比于此前的医学SAM适配器实现了8.8%的绝对性能提升 [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/64809)。

#### **3. 实验与评价总结**
*   **数据集与评价指标**：公开数据集如Synapse多器官CT、AMOS、CHAOS、LiTS以及各类病理学数据集（如Glas）被广泛用于模型性能的基准测试。同时，研究中也大量使用了私有临床数据集以验证特定场景下的有效性。评价指标高度统一，主要采用Dice相似系数（DSC）和交并比（IoU）来衡量区域重叠度，并辅以豪斯多夫距离（HD95）来评估边界轮廓的匹配精度。

*   **共性实验结论**：
    1.  **混合架构的优越性**：CNN-Transformer混合模型（如各类UNet与Transformer的结合体）普遍在分割精度上优于纯CNN模型，尤其是在需要大范围上下文信息的大器官或复杂结构分割任务中 [pdf.hanspub.org](https://pdf.hanspub.org/csa_1543783.pdf)。
    2.  **基础模型的潜力与局限**：未经微调的SAM直接应用于医学图像分割时，性能通常弱于为该任务特化训练的模型。然而，通过领域自适应微调（如MedSAM2, DB-SAM），SAM及其变体能够达到甚至超越最先进的专用模型，并展现出强大的零样本或少样本泛化能力 [www.opticsjournal.net](https://www.opticsjournal.net/Articles/OJda3bfaa1dd74a3a/FullText)。
    3.  **效率与性能的权衡**：Transformer的高计算成本催生了对高效架构的探索。SegNeXt等工作证明，优化的CNN模型能够在计算开销远低于Transformer的情况下达到极具竞争力的性能 [mftp.mmcheng.net](https://mftp.mmcheng.net/Papers/22SegNeXt.pdf)。而VMamba等新兴架构则提供了在保持全局建模能力的同时实现线性计算复杂度的可能路径 [www.hanspub.org](https://www.hanspub.org/journal/paperinformation?paperid=112526)。

#### **4. 趋势与挑战**
基于2022-2025年的研究进展，未来生物医学图像分割领域将呈现以下主要趋势与挑战：

1.  **从“专用模型”到“通用基础模型”的范式迁移**：以SAM为代表的基础模型正引领一场范式革命。未来的研究重点将不再是为每个新任务从零开始设计和训练模型，而是如何更高效、更鲁棒地将一个强大的预训练基础模型适配到多样的下游医学任务中。这包括开发更先进的参数高效微调（PEFT）技术、设计更智能的自动提示工程，以及构建更大规模、更多样化的医学预训练数据集 [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/279a8711-cf36-4ca8-b9c9-1f7c35eec72e)。**挑战**在于如何有效弥合自然图像与医学图像之间的巨大领域鸿沟，以及如何处理医学数据的隐私与标准化问题。

2.  **追求线性复杂度的全局建模新架构**：Transformer的二次方计算复杂度限制了其在高分辨率图像（如全切片病理图像）和3D数据上的应用。Mamba等状态空间模型的出现，为实现与Transformer相媲美的长距离依赖建模能力，同时保持与CNN相似的线性计算复杂度，提供了极具前景的解决方案。预计未来将有更多研究围绕Mamba及其变体设计新的分割网络架构，以期在性能和效率之间达到新的平衡点 [www.hanspub.org](https://www.hanspub.org/journal/paperinformation?paperid=112526)。**挑战**在于如何将一维序列的SSM有效推广至二维和三维视觉数据，并证明其在广泛医学分割任务中的稳定性和优越性。

3.  **数据与模型协同进化：迈向多模态、弱监督与交互式应用**：随着模型能力的增强，对数据的需求也日益增长。未来的趋势之一是融合多模态信息（如PET-CT、MRI-T1/T2），通过跨模态学习提供更丰富的病灶特征 [www.jeit.ac.cn](https://www.jeit.ac.cn/cn/article/doi/10.11999/JEIT220445?viewType=HTML)。另一大趋势是利用基础模型的强大分割能力，结合半监督或弱监督学习框架，以极少量标注数据驱动模型训练，从而大幅降低标注成本 [www.opticsjournal.net](https://www.opticsjournal.net/Articles/OJda3bfaa1dd74a3a/FullText)。此外，SAM的提示驱动特性使其天然适合交互式分割，这将推动其在临床实时辅助诊断和手术导航等场景的落地应用。**挑战**在于如何设计高效的多模态融合机制，以及如何确保弱监督方法生成的伪标签的质量与可靠性。

#### **5. 结论**
在2022至2025年间，生物医学图像分割领域经历了从CNN-Transformer混合架构的成熟到通用基础模型兴起的深刻变革。研究者们在提升模型对全局上下文的理解能力、平衡计算效率与分割精度，以及减少对大规模标注数据的依赖方面取得了显著进展。当前，适配和微调SAM等基础模型已成为前沿热点，而Mamba等新兴架构则为未来的网络设计开辟了新道路。尽管面临数据获取、模型泛化和临床落地等多重挑战，但向着更通用、更高效、更智能的分割技术迈进的趋势已然明确，深度学习将继续在精准医疗中扮演愈发重要的角色。

#### **6. 参考文献**
[1] 石军, 王天同, 朱子琦, 等. 基于深度学习的医学图像分割方法综述[J]. 中国图象图形学报, 2025, 30(6): 2161-2186.
[2] 尹艺晓, 马金刚, 张文凯, 等. 从U-Net到Transformer：混合模型在医学图像分割中的应用进展[J]. 激光与光电子学进展, 2025, 62(2): 0200001.
[3] 姚劲草, 吴曈, 胡浩基, 等. 分割一切模型（SAM）在医学图像分割中的应用[J]. 中国激光, 2024, 51(21): 2107102.
[4] Guo, M. H., Lu, C. Z., Hou, Q., et al. SegNeXt: Rethinking Convolutional Attention Design for Semantic Segmentation[C]. NeurIPS, 2022.
[5] 李振勇, 刘艺, 柯宇晨, 等. 基于DeepLab和可变形卷积的肝脏病理环境分割方法[J]. 计算机科学与应用, 2025, 15(6): 157-167.
[6] 檀文文, 卢棚, 姜韦. 基于改进SwinUNet腹部多器官分割算法研究[J]. 计算机科学与应用, 2025, 15(10): 318-326.
[7] 周涛, 侯森宝, 陆惠玲, 等. C2 Transformer U-Net：面向跨模态和上下文语义的医学图像分割模型[J]. 电子与信息学报, 2023, 45(5): 1807-1816.
[8] 王劭羽, 陈庆奎, 黄陈. 基于VMamba-CNN混合的结直肠癌切片图像分割[J]. 建模与仿真, 2025, 14(4): 799-810.
[9] Ma, J., Yang, Z., Kim, S., et al. MedSAM2: Segment Anything in 3D Medical Images and Videos[EB/OL]. (2025-04-04). arXiv.
[10] Qin, C., Cao, J., Fu, H., et al. DB-SAM: Delving into High Quality Universal Medical Image Segmentation[EB/OL]. (2024-10-08). arXiv.
[11] Ma J, He Y T, Li F F, et al. Segment anything in medical images[J]. Nature Communications, 2024, 15(1): 654.
[12] Ronneberger, O., Fischer, P., & Brox, T. U-Net: Convolutional Networks for Biomedical Image Segmentation[C]. MICCAI, 2015.
[13] Chen, J., Lu, Y., Yu, Q., et al. TransUNet: Transformers Make Strong Encoders for Medical Image Segmentation[EB/OL]. (2021-02-04). arXiv.
[14] Cao, H., Wang, Y., Chen, J., et al. Swin-Unet: Unet-Like Pure Transformer for Medical Image Segmentation[C]. ECCV Workshops, 2022.