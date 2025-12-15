# 混合神经网络架构与自适应特征融合研究综述（2022–2025）

## 引言

多模态感知与表征学习已成为人工智能在自动驾驶、医学影像、人机交互等高阶任务中的核心技术瓶颈。单一模态（如可见光图像、文本）往往存在信息缺失或环境敏感等局限，而多模态（如红外–可见光、文本–图像、音频–视频）可提供互补信息。然而，如何构建既能保留模态特异性又能有效融合跨模态语义的模型架构，成为近年来的研究焦点。2022–2025年间，**混合神经网络架构**（Hybrid Architectures）与**自适应特征融合**（Adaptive Feature Fusion）策略成为主流技术路径，其核心目标是平衡局部细节与全局语义、动态调节模态权重，并在特征/决策层面实现高效协同。本文系统梳理该方向代表性进展，聚焦架构设计、融合机制与性能验证三大维度。

## 方法分类与代表作

### 1. CNN–Transformer 混合架构

此类方法结合CNN的局部感知能力与Transformer的全局建模能力，广泛应用于图像融合与医学分割任务。

- **MCT-Net**（汤文超等，2025）[hanspub.org](https://pdf.hanspub.org/mos2025141_372572027.pdf) 针对肝脏肿瘤边界模糊与形态多变问题，提出双编码器结构：CNN分支通过细节特征提取模块（DFEM）捕获边缘局部特征，Transformer分支引入多轴自注意力（Max-SA）扩展感受野。在LiTS2017数据集上Dice达72.16%，ASD为3.380 mm，显著优于U-Net++与TransUNet。

- **基于Transformer-CNN的红外与可见光融合网络**（李玉等，2025）[hanspub.org](https://pdf.hanspub.org/jisp_2670448.pdf) 构建双分支编码器提取模态特征，提出跨模态差异融合模块（CMDFM）通过特征差分计算互补信息，并采用参数自适应Swish激活函数动态生成通道权重。在MSRS与RoadScene数据集上，SSIM分别达0.9359与0.961，EN、AG、VIF等指标均优于DSFusion、RFN-Nest等7种基线。

- **CDDFuse**（arXiv:2310.15453，2023）采用双分支Transformer–CNN特征提取器：Lite Transformer处理低频全局特征，可逆神经网络（INN）提取高频局部细节，并引入相关性驱动的特征分解机制。在红外–可见光融合任务中，主观视觉质量与客观指标（如SF、VIF）均优于U2Fusion与GANMcC。

### 2. 扩散模型与CNN协同融合

利用扩散模型的生成能力与CNN的细节保持能力，实现高质量多模态图像融合。

- **DCAFuse**（Lu et al., ACM MM 2024）[csdn.net](https://blog.csdn.net/qq_42722197/article/details/146433326) 提出双分支扩散–CNN框架：基于DDPM的分支建模全局语义，CNN分支提取局部纹理，并设计互补特征聚合模块（CFAM）通过坐标注意力动态融合。在红外–可见光与医学图像融合任务中，余弦散度损失与时间步策略有效提升了特征互补性，性能超越SOTA方法。

- **FeINFN**（Liang et al., NeurIPS 2024）[openreview.net](https://openreview.net/forum?id=CscowTrOP9) 针对多/高光谱图像融合中INR丢失高频信息问题，提出空间–频率隐式融合函数（Spa-Fre IFF）与空间–频率交互解码器（SFID），利用Gabor小波激活函数增强频域建模。在两个基准数据集上实现SOTA性能，消融实验证明傅里叶相位建模对高频恢复至关重要。

### 3. 决策级自适应融合与门控机制

在特征交互后，通过门控或权重学习机制自适应融合多模态表征。

- **跨模态自适应特征融合的VQA方法**（陈巧红等，2025）[hit.alljournals.cn](https://hit.alljournals.cn/hitxb_cn/article/html/20250410) 设计卷积自注意力单元（ConvSA）同时捕获全局语义与视觉对象空间关系，并提出多模态门控融合模块，根据模态重要性自适应调整视觉偏移向量权重。在VQA2.0测试集上准确率达72.00%，优于MCAN且未使用额外预训练。

- **DepMamba**（Ye et al., ICASSP 2025）[arxiv.org](https://arxiv.org/abs/2409.15936) 针对多模态抑郁症检测中长序列建模效率低问题，提出分层上下文建模（CNN + Mamba）与渐进融合策略：协作状态空间模型（CoSSM）共享状态转移矩阵以学习模态间共享上下文，EnSSM增强模态凝聚力。相比Transformer基线，推理速度提升15倍，内存占用减少92.3%。

- **基于多粒度渐进式融合的多模态NER**（应旭剑等，2025）[arocmag.cn](https://www.arocmag.cn/abs/2025.03.0071) 设计动态门控过滤机制筛选相关视觉区域，并构建文本级、文本–区域图像级、文本–全局图像级三层并联融合网络。在Twitter-2015/2017上F1值分别提升0.89%与1.08%，有效缓解细粒度语义缺失问题。

## 实验与评价总结

上述工作在实验设计上呈现以下共性：  
1. **多数据集验证**：主流研究均在至少两个公开数据集（如MSRS/RoadScene、LiTS/3D-IRCADb、VQA2.0/GQA）上验证泛化性；  
2. **多指标评估**：除主观视觉质量外，普遍采用EN（信息熵）、SSIM（结构相似性）、AG（平均梯度）、VIF（视觉信息保真度）、SF（空间频率）等7项以上客观指标；  
3. **消融实验规范**：均通过移除关键模块（如CMDFM、MSIF、CFAM）验证组件有效性，量化各模块对性能提升的贡献；  
4. **计算效率关注**：新兴工作（如DepMamba、MCT-Net）开始报告FLOPs与内存占用，强调模型实用性。

共性结论包括：  
- 混合架构（CNN+Transformer/扩散/Mamba）在保留局部细节与建模全局上下文方面显著优于单一架构；  
- 自适应融合机制（门控、注意力、参数化激活）能有效抑制模态冗余，提升互补信息利用率；  
- 特征级融合在图像任务中占主导，而决策级融合在高阶语义任务（如VQA、NER）中更具优势。

## 趋势与挑战

基于2025年前后最新文献，可归纳三大趋势：  
1. **架构轻量化与高效推理**：随着Mamba等状态空间模型兴起，研究正从高计算开销的Transformer转向线性复杂度架构（如DepMamba），以满足边缘部署需求；  
2. **融合机制可解释性增强**：从隐式注意力转向显式门控或概率建模（如贝叶斯融合、证据理论），以提升决策可信度，尤其在医疗、自动驾驶等安全关键领域；  
3. **跨模态对齐前置化**：FUSION（arXiv:2504.09925）等新工作将文本引导对齐融入视觉编码早期阶段，实现像素级语义对齐，而非仅在解码后期交互。

主要挑战包括：  
- **模态异构性**：不同模态（如点云与图像）的采样率、分辨率、语义粒度差异导致对齐困难；  
- **标注稀缺性**：高质量多模态对齐数据（如细粒度QA对）构建成本高，制约模型泛化；  
- **动态场景适应性**：现有方法多假设静态场景，对时序动态变化（如运动模糊、光照突变）鲁棒性不足。

## 结论

2022–2025年，混合神经网络架构与自适应特征融合研究已从简单拼接或加权，发展为基于注意力、门控、状态空间模型的精细化协同机制。CNN–Transformer混合、扩散–CNN协同、Mamba序列建模等架构创新，结合参数自适应激活、坐标注意力、多粒度门控等融合策略，显著提升了多模态任务的性能上限。未来研究需在效率、可解释性与动态适应性三方面突破，以支撑真实场景下的可靠部署。

## 参考文献

1. 汤文超, 丁德锐, 袁浩成, 刘华卿. 一种混合 CNN-Transformer 多尺度特征的肝脏肿瘤分割网络[J]. 建模与仿真, 2025, 14(1): 388–403. [hanspub.org](https://pdf.hanspub.org/mos2025141_372572027.pdf)  
2. 李玉, 张志超, 祁艳杰. 基于 Transformer-CNN 的红外与可见光融合网络[J]. 图像与信号处理, 2025, 14(4): 377–386. [hanspub.org](https://pdf.hanspub.org/jisp_2670448.pdf)  
3. 陈巧红, 项深祥, 方贤, 孙麒. 跨模态自适应特征融合的视觉问答方法[J]. 哈尔滨工业大学学报, 2025, 57(4): 94–104. [hit.alljournals.cn](https://hit.alljournals.cn/hitxb_cn/article/html/20250410)  
4. 应旭剑, 朱艳辉, 陈豪, 等. 基于多粒度渐进式融合的多模态命名实体识别方法[J]. 计算机应用研究, 2025, 42(10): 3027–3033. [arocmag.cn](https://www.arocmag.cn/abs/2025.03.0071)  
5. Ye, J., et al. DepMamba: Progressive Fusion Mamba for Multimodal Depression Detection. In *ICASSP 2025*. [arxiv.org](https://arxiv.org/abs/2409.15936)  
6. Liang, Y., et al. Fourier-enhanced Implicit Neural Fusion Network for Multispectral and Hyperspectral Image Fusion. *NeurIPS 2024*. [openreview.net](https://openreview.net/forum?id=CscowTrOP9)  
7. Lu, X., et al. DCAFuse: Dual-Branch Diffusion-CNN Complementary Feature Aggregation Network for Multi-Modality Image Fusion. In *ACM MM 2024*. [csdn.net](https://blog.csdn.net/qq_42722197/article/details/146433326)  
8. Tian, A., Zhang, C. 多模态深度学习中的决策级融合方法及其应用研究[J]. 图像与信号处理, 2025, 14(4): 412–421.  
9. FUSION: Fully Integrated Visual-Language Representation for Deep Cross-Modal Understanding. *arXiv:2504.09925*, 2025.  
10. Chen, Q., et al. Multimodal named entity recognition method based on multi-granularity progressive fusion. *Application Research of Computers*, 2025, 42(10): 3027–3033.  
11. Li, H., Wu, X., Kittler, J. RFN-Nest: An End-to-End Residual Fusion Network for Infrared and Visible Images. *Information Fusion*, 2021, 73: 72–86.  
12. Liu, K., et al. DSFusion: Infrared and Visible Image Fusion Method Combining Detail and Scene Information. *Pattern Recognition*, 2024, 154: 110633.