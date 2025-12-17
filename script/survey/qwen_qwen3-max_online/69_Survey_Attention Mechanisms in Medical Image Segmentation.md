# 医学图像分割中的注意力机制研究综述（2022–2025）

## 引言

医学图像分割是计算机辅助诊断、放疗规划和手术导航的核心任务，其对病灶边界的高精度刻画要求远超通用图像分割。传统卷积神经网络（CNN）受限于局部感受野，难以建模长距离依赖；而Transformer虽具全局建模能力，却易丢失局部细节且计算开销巨大。注意力机制通过动态加权特征通道或空间位置，在不显著增加参数的前提下协调局部与全局信息，成为近年医学图像分割模型的核心组件。本文系统梳理2022–2025年间注意力机制在医学图像分割领域的代表性进展，按技术路线分类评述，并总结实验规律与未来趋势。

## 方法分类与代表作

### 1. CNN-Transformer 混合架构中的注意力

混合架构结合CNN的局部细节提取能力与Transformer的全局依赖建模，注意力机制在二者间起桥梁作用。  
**TransAttUnet**（2021，后于2023年扩展为TransattUNet [baai.ac.cn](https://hub.baai.ac.cn/view/8857)）提出自感知注意力（SAA）模块，融合Transformer自注意力（TSA）与全局空间注意力（GSA），并在解码器间引入多尺度跳跃连接。在多个医学数据集上，其Dice系数显著优于ResUNet++和MCTrans，验证了多级注意力对信息衰退问题的有效缓解。  
**CPCATNet**（2025）针对肺部肿瘤边界模糊与粘连问题，在TransUNet基础上引入全局–局部注意力（GLA）与通道优先卷积注意力（CPCA）[gdut.edu.cn](https://html.rhhz.net/GDGYDXXB/html/1736152746337-1505189003.htm)。GLA并行处理全局与局部特征，CPCA在跳跃连接中动态分配通道与空间权重。在LUNG1和GDPH数据集上Dice分别达88.18%和90.96%，优于8种SOTA方法。  
**改进SwinUNet**（2025）采用Focal Transformer替代Swin Transformer以增强层次化注意力，并在编码器末端引入空洞空间金字塔池化（ASPP）扩展感受野，跳跃连接中加入Tokenized Interaction Fusion（TIF）模块实现跨层特征交互[hanspub.org](https://pdf.hanspub.org/csa_1543783.pdf)。在Synapse数据集上平均Dice达79.89，HD降至19.73，显著优于原始SwinUNet。

### 2. 专用注意力模块设计

针对医学图像特性（如小目标、边界模糊），研究者设计轻量高效注意力模块。  
**DuAT**（2022）提出双聚合Transformer网络，包含全局到局部空间聚合（GLSA）与选择性边界聚合（SBA）模块[csdn.net](https://blog.csdn.net/weixin_44184852/article/details/146547729)。GLSA分离通道分别处理全局与局部特征，SBA融合浅层边界与深层语义。在息肉、皮肤病变等6个数据集上达到SOTA，且参数量低于Polyp-PVT。  
**MCANet**（2025）设计多尺度交叉轴注意力（MCA），通过双重交叉注意力增强全局信息捕获，并在轴向路径中引入多尺度条带卷积以提升局部编码效率[baai.ac.cn](https://hub.baai.ac.cn/view/48972)。该模块仅4M+参数，在皮肤病变、细胞核、腹部器官和息肉分割四个任务上超越基于Swin Transformer的大模型。  
**MCT-Net**（2025）针对肝脏肿瘤，设计局部空间注意力（LAM）与全局空间注意力（GAM）模块，并在Transformer编码器中加入多轴自注意力（Max-SA）[hanspub.org](https://pdf.hanspub.org/mos2025141_372572027.pdf)。LAM增强微小肿瘤解析度，GAM提升大范围变异肿瘤感知。在LiTS2017上Dice达72.16%，ASD为3.380 mm，优于TransUNet等7种方法。

### 3. 小样本与新兴架构中的注意力应用

在数据稀缺或新架构探索场景，注意力机制被赋予新角色。  
**DPCENet**（2025）面向小样本分割，提出空间–通道双视角注意力，空间分支定位器官分布，通道分支增强语义抑制噪声，并采用双路径分别处理前景与背景[hanspub.org](https://pdf.hanspub.org/mos_2572665.pdf)。在ABD-CT等三个数据集上，Setting-2下Dice均值达65.74，优于SSL-ALPNet等SOTA方法。  
**M-UNet**（2025）将Mamba的VSS块与ASPP结合，VSS以线性复杂度建模全局依赖，ASPP捕捉多尺度特征[hanspub.org](https://pdf.hanspub.org/csa_1543779.pdf)。在Synapse数据集上平均Dice达80.79%，在ACDC上DSC达88.01%，显著优于U-Net与Swin-UNet，且计算效率更高。

## 实验与评价总结

综合近年研究，注意力机制在医学图像分割中的实验表现呈现以下共性：  
1. **多尺度融合是性能提升关键**：几乎所有SOTA方法均在跳跃连接或瓶颈层引入多尺度特征交互（如TIF、MSIF、SBA），有效缓解编解码器间的语义鸿沟。  
2. **局部–全局协同优于单一建模**：单纯全局注意力（如ViT）在边界清晰度上表现不佳，而结合局部卷积的混合注意力（如GLA、MCA）在Dice与HD指标上均取得平衡提升。  
3. **专用注意力模块轻量化趋势明显**：如MCA、Max-SA等模块通过分解或稀疏化注意力计算，在参数量<5M的条件下超越大型Transformer模型。  
4. **评价指标趋于全面**：除Dice外，HD95、ASD等边界敏感指标被广泛采用，反映对分割精细度的重视；小样本任务则强调跨域泛化能力（如Setting-2协议）。  
5. **数据集选择聚焦临床挑战**：Synapse（多器官尺度差异）、LiTS（肝脏肿瘤边界模糊）、LUNG1（肺部噪声与粘连）成为验证注意力有效性的标准基准。

## 趋势与挑战

基于2025年前后的最新文献，可预见以下研究趋势：  
1. **状态空间模型（SSM）与注意力融合**：Mamba等SSM以线性复杂度实现长序列建模，正逐步替代Transformer（如M-UNet），未来将探索SSM与轻量注意力的协同机制以兼顾效率与精度。  
2. **基础模型（Foundation Models）的注意力适配**：如MedSAM等通用分割模型需针对医学图像特性微调其注意力机制，研究如何将解剖先验或病理知识注入注意力权重分配。  
3. **多模态与跨模态注意力**：结合CT、MRI、病理、文本等多源信息，设计跨模态注意力以增强语义一致性，尤其在放疗靶区勾画等需多证据融合的场景。  
4. **临床可解释性驱动的注意力设计**：现有注意力热力图缺乏病理依据，未来将发展与医生诊断逻辑对齐的可解释注意力，如聚焦特定血管区域或肿瘤侵袭前沿。  
5. **联邦学习中的注意力聚合**：在隐私保护前提下，如何在联邦学习框架中聚合各中心的注意力模式以提升泛化能力，将成为多中心部署的关键挑战。

## 结论

2022–2025年间，注意力机制在医学图像分割中从辅助组件演变为架构核心。研究焦点从简单引入通道/空间注意力，转向设计轻量、专用、多尺度协同的注意力模块，并深度融入CNN-Transformer混合架构或新兴SSM框架。实验证明，有效结合局部细节与全局语义的注意力机制能显著提升分割精度与边界质量。未来，注意力机制将与基础模型、多模态融合及临床工作流深度结合，在保证可解释性与隐私安全的前提下，推动医学图像分割向“临床可用”迈进。

## 参考文献

1. Chen, J., Lu, Y., Yu, Q., et al. (2021). TransUNet: Transformers Make Strong Encoders for Medical Image Segmentation. *arXiv:2102.04306*.  
2. Hatamizadeh, A., et al. (2022). UNETR: Transformers for 3D Medical Image Segmentation. *WACV*, 574–584.  
3. Cao, H., et al. (2022). Swin-Unet: U-Net-like Pure Transformer for Medical Image Segmentation. *ECCV Workshops*, 205–218.  
4. Zeng, A., et al. (2025). Lung Tumor Segmentation Method Based on Transformer and Attention Mechanisms. *J. Guangdong Univ. Technol.*, 42(1), 24–32. [DOI:10.12052/gdutxb.230177](http://dx.doi.org/10.12052/gdutxb.230177)  
5. Tan, W., et al. (2025). Research on an Improved SwinUNet Algorithm for Multi-Organ Segmentation in the Abdomen. *Comput. Sci. Appl.*, 15(10), 318–326. [DOI:10.12677/csa.2025.1510271](https://doi.org/10.12677/csa.2025.1510271)  
6. Shao, H., et al. (2025). MCANet: Medical Image Segmentation with Multi-scale Cross-axis Attention. *Mach. Intell. Res.*, 22(3), 437–451. [DOI:10.1007/s11633-025-1552-6](https://doi.org/10.1007/s11633-025-1552-6)  
7. Tang, W., et al. (2025). A Mix CNN-Transformer Multi-Scale Feature Network for Liver Tumor Segmentation. *Model. Simul.*, 14(1), 388–403. [DOI:10.12677/mos.2025.141037](https://doi.org/10.12677/mos.2025.141037)  
8. Zu, C., et al. (2025). Few-Shot Medical Image Segmentation Based on Dual-Perspective Attention. *Model. Simul.*, 14(8), 255–265. [DOI:10.12677/mos.2025.148564](https://doi.org/10.12677/mos.2025.148564)  
9. Gou, J., et al. (2025). U-Shaped Medical Image Segmentation Network Based on the Mamba Model. *Comput. Sci. Appl.*, 15(10), 341–350. [DOI:10.12677/csa.2025.1510273](https://doi.org/10.12677/csa.2025.1510273)  
10. Yin, Y., et al. (2025). From U-Net to Transformer: Progress in the Application of Hybrid Models in Medical Image Segmentation. *Laser & Optoelectron. Prog.*, 62(2), 0200001. [opticsjournal.net](https://www.opticsjournal.net/Articles/OJ2b2078a8cf027f69/km)  
11. Guha Roy, A., et al. (2020). “Squeeze & Excite” Guided Few-Shot Segmentation of Volumetric Images. *Med. Image Anal.*, 59, 101587.  
12. Ouyang, C., et al. (2020). Self-Supervision with Superpixels: Training Few-Shot Medical Image Segmentation without Annotation. *ECCV*, 762–780.  
13. Liu, Y., et al. (2021). TransAttUnet: Multi-level Attention-guided U-Net with Transformer for Medical Image Segmentation. *arXiv:2107.05274*.  
14. Bilic, P., et al. (2023). The Liver Tumor Segmentation Benchmark (LiTS). *Med. Image Anal.*, 84, 102680.  
15. Ma, J., et al. (2024). MedSAM: Segment Anything Model for Medical Images. *arXiv:2306.14452*.