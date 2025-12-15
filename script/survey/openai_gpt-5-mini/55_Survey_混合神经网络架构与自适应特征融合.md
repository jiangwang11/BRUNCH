引言  
混合神经网络（hybrid neural architectures）与自适应特征融合是近三年（2022–2025）多模态视觉与医学影像领域的核心研究方向：前者通过组合卷积/Transformer/隐式表示/扩散等模块以兼顾局部细节与全局语义，后者关注在不同模态或不同尺度间动态分配信息权重以最大化下游任务性能。本文围绕“架构混合策略”和“自适应融合机制”两条主线，对 2022–2025 年代表性工作按方法类别进行归纳、比较与总结，重点突出每篇工作的研究问题、核心方法与关键实验结论（每篇 4–6 句），并在实验部分提取共性发现，最后给出面向 2025 年前后的研究趋势预测与挑战。所有被介绍的文献均为公开发表或 arXiv/顶会论文（列表见文末参考文献）。

方法分类与代表作  
1) CNN ↔ Transformer 混合编码器（局部—全局协同）  
- MCT‑Net（Mix CNN‑Transformer Multi‑scale Feature Network, 汤文超等，2025）——问题：肝脏肿瘤分割中边界模糊与尺度变异；核心方法：双编码器并行设计，一支为多尺度可分离卷积（DFEM + 局部注意力 LAM），另一支为 Transformer 分支（Max‑SA：Block + Grid 注意力），解码器采用多尺度信息交互（MSIF）；关键结论：在 LiTS2017 与 3D‑IRCADb 上显示比典型 U‑Net 变体更高的 Dice 与更小的 ASD，表明并行 CNN/Transformer 有利于兼顾边界细节与全局语义。[pdf.hanspub.org/mos2025141_372572027.pdf](https://pdf.hanspub.org/mos2025141_372572027.pdf)  
- 基于 Transformer‑CNN 的红外/可见光融合网络（李玉 等，2025）——问题：红外与可见光图像融合需同时保留热显著性与纹理细节；核心方法：双分支 Transformer‑CNN 编码器、跨模态差分融合模块（CMDFM）和可学习 Swish 通道权重，损失包含掩码像素/梯度/SSIM 分项以鼓励目标区域保留；关键结论：在 MSRS/RoadScene 数据集上客观指标（EN, SSIM, SF, VIF 等）显示优越性，且消融验证 MFEM 与 CMDFM 对细节/结构恢复均有作用。[pdf.hanspub.org/jisp_2670448.pdf](https://pdf.hanspub.org/jisp_2670448.pdf)  
- U2Fusion（Xu et al., TPAMI 2022，引入于综述引用）——问题：统一无监督图像融合框架的设计；核心方法：U‑Net 风格的自编码器结合多任务损失与不使用配对标签的训练策略，重视通用性与无监督学习；关键结论：在多个基准上证明端到端无监督框架能获得稳定的保真与细节保留（作为混合/对比基线被广泛采用）。（见相关文献综述引用）

2) 隐式表示（INR）与频域增强 / 生成式分支（扩散、DDPM）混合  
- FeINFN（Fourier‑enhanced Implicit Neural Fusion Network, Liang et al., NeurIPS 2024）——问题：INR 在多/高光谱图像融合中常丢失高频细节且缺乏全局感知；核心方法：提出空间‑频率隐式融合函数（Spa‑Fre IFF）与空间‑频率交互解码器（SFID），在网络内引入傅里叶增强与 Gabor 小波激活以恢复高频并扩展感受野；关键结论：在两个 MHIF 基准上实现视觉和定量（MI、SF、VIF 等）上的 SOTA，消融显示傅里叶/Gabor 组件对高频保留贡献显著。[chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/82650)  
- DCAFuse（Dual‑Branch Diffusion‑CNN Complementary Feature Aggregation, ACM MM 2024 / 同名实现与解析）——问题：扩散模型（DDPM）擅长全局建模但弱化局部细节；核心方法：双分支设计——扩散分支捕捉全局信息、CNN 分支捕捉多尺度局部细节，借助坐标感知注意力的互补特征聚合模块（CFAM）动态融合两者并使用余弦散度等约束与时间步策略；关键结论：在红外/可见与医学图像融合任务上，扩散+CNN 的互补融合在保持全局一致性的同时提升纹理细节保真度（多任务/多数据集验证）。[blog.csdn.net](https://blog.csdn.net/qq_42722197/article/details/146433326)

3) 高阶交互与协同建模（空间与通道维度的高阶融合）  
- SHIP（Probing Synergistic High‑Order Interaction, CVPR 2024 / 后续扩展）——问题：传统交叉/自注意力限于二阶空间交互，无法充分挖掘模态间高阶协同；核心方法：提出协同高阶交互范式（SHIP），在空间维度用频域等价的逐元素乘法高效构建高阶空间交互，并在通道维度推广 SE 风格的高阶统计交互，采用迭代聚合机制演化协同信息；关键结论：在 M3FD/RoadScene/TNO 等基准显示比若干 Transformer/CNN 基线更好的 MI/FMI/SF 等指标，并在 pansharpening（全色锐化）任务上展现泛化潜力，表明高阶交互有助于更细粒度的互补信息提取。[blog.csdn.net](https://blog.csdn.net/weixin_44184852/article/details/146036111)  
- 相关高阶空间/通道交互思想在若干 2023–2024 的 Transformer 拓展工作中得到理论或工程化实现（文献参见下文参考），共同指向“在不显著增加二阶矩阵乘法开销下捕获更高阶模态协同”的可行路径。

4) 自适应门控 / 卷积‑注意力融合与判别/对抗对齐（跨模态权重自适应）  
- 跨模态自适应特征融合（视觉问答场景，陈巧红，2025）——问题：VQA 中多模态交互与融合粗糙导致信息丢失；核心方法：提出卷积自注意力单元（自注意力 + 空洞卷积捕获空间关系）、自适应特征融合层与多模态门控融合模块，文本为主模态时用门控自适应调节视觉偏移；关键结论：在 VQA‑v2/GQA 上，在未使用额外预训练的情况下取得了可比提升，表明门控融合能在参数预算受限时有效调节模态贡献。[hit.alljournals.cn](https://hit.alljournals.cn/hitxb_cn/article/html/20250410)  
- 对抗训练与模态判别对齐（多模态情感/医学等，2024–2025 多篇工作）——核心思想：引入模态判别器或对抗损失以促使不同模态特征在共享语义空间对齐，同时用掩码/显著性加权保持文本或关键模态主导信息；若干实验证明对齐能在情感识别与医学预测任务中减少模态偏差并提升泛化（见 2025 年相关综述）。

5) 决策级 / 集成与证据理论（晚期融合的稳健化）  
- 决策级融合综述（田傲翔、张长伦，2025）——问题：当模态间异构且难以直接对齐时，如何在决策层集成多模态模型结果以提升稳健性；核心方法：系统归纳加权平均、贝叶斯推理、Dempster‑Shafer 证据理论与集成学习（Bagging/Boosting）在深度多模态场景的应用与改进；关键结论：证据理论在表示不确定性上具有优势但计算复杂度高；集成学习能提高鲁棒性但成本大，推动研究朝“跨模态互验证据化融合 + 反馈修正”方向发展。[pdf.hanspub.org/jisp_2670441.pdf](https://pdf.hanspub.org/jisp_2670441.pdf)

实验与评价总结（共性结论，仅总结共性，不逐篇列举）  
- 目标导向损失与显著性/掩码量化至关重要：多数工作（可见于融合与分割任务）将显著性掩码或针对目标区域的像素/梯度/SSIM 损失作为核心设计以保护目标信息，帮助在视觉质量与任务性能间取得更好折衷。  
- 局部‑全局双路径（或混合模块）普遍优于单一路径：并行或串联的 CNN（局部）与 Transformer/扩散/INR（全局）分支能互补，从而同时恢复纹理细节与全局一致性，但需设计专门的聚合模块（如 CFAM、CMDFM、MSIF）避免信息冲突。  
- 频域或小波增强对高频细节恢复效果显著：以傅里叶增强、Gabor 激活或尽量保留频谱相位信息的工作（FeINFN、SHIP 的频域等价操作）在高频保真度指标（SF、AG、FMI）上体现出明确优势。  
- 高阶交互与通道统计扩展带来额外增益但需受控计算开销：高阶空间/通道交互能显著提升模态协同识别，但原始矩阵乘法扩展会带来二次/更高复杂度，频域等价与递归聚合被证明为有效的工程折衷。  
- 生成式分支（扩散/INR）改善全局一致性但需补偿局部细节：扩散或 INR 分支提供更稳定的全局结构，但若不采用频域增强或 CNN 细化则会出现纹理/边缘平滑，故双分支设计被反复验证为必要。  
- 评估多指标与下游任务驱动：仅依赖单一图像融合指标会误导结论。近年来研究趋向用多指标集合（MI、VIF、SF、SSIM、AG、Qabf、FMI）并在目标检测/分割/识别等下游任务上做端到端验证以衡量实际效用。

趋势与挑战（2025 年前后可验证的研究方向，至少 3 点）  
1. 频域‑时频联合建模将成为主流，用于弥补纯空间注意力在高频恢复上的短板。具体表现为在隐式表示或 Transformer 中系统性地引入傅里叶/Gabor/小波激活或相位约束，以在不大幅增长计算量下保留纹理与边缘信息（已见 FeINFN、SHIP 的初步证据）。  
2. 生成式＋判别/判别式反馈的混合训练范式：扩散/INR/生成分支负责全局结构，CNN/判别器/任务网络负责局部细节和语义一致性；训练上将更多使用跨时间步特征提取、多尺度对齐与互补损失（比如余弦相似度、显著性权重），以实现生成与判别的协同优化（DCAFuse 的思路在 2024–2025 年被广泛延伸）。  
3. 高阶交互的“可扩展近似”成为热点：要在实际系统中用高阶空间/通道交互提升融合表现，必须发展基于频域等价、可分解卷积或递归聚合的近似算法，降低计算与内存开销，使得 N 阶交互可用于高分辨率图像与实时系统（SHIP 的迭代聚合提出了方向）。  
4. 任务驱动与不确定性量化将深入融合算法设计：未来融合算法不仅追求视觉指标，还须在下游检测/分割/识别任务上直接优化，同时输出不确定性估计（贝叶斯/证据理论），以便于临床/自动驾驶等高风险场景的可靠部署（决策级融合综述指出了可行路径）。  
5. 联邦/隐私‑友好与跨域泛化成为研究必需：多机构医学/遥感数据的融合应用要求算法具备跨域鲁棒性与隐私保护能力，预计出现更多基于对齐的去偏/域自适应与联邦学习融合范式。

结论  
2022–2025 年的研究表明，通过合理的架构混合（CNN、Transformer、INR、扩散）与精心设计的自适应融合模块（门控、频域增强、高阶交互、证据/贝叶斯决策），能够在多模态融合任务上同时推进视觉质量与下游任务性能。下一阶段研究需要把重点放在频域‑时频建模、生成式与判别式的协同训练、高阶交互的可扩展近似、任务驱动的不确定性量化及跨域/隐私可部署性上。本文所列代表作与实验共性为后续工作提供了可重复验证的设计模式與开放问题。

参考文献（按本文出现次序，均为公开论文/报告或权威综述；链接使用检索结果域名）  
1. Liang, Y., Cao, Z., Deng, S., Dou, H.‑X., & Deng, L.‑J. Fourier‑enhanced Implicit Neural Fusion Network for Multispectral and Hyperspectral Image Fusion. NeurIPS 2024 (论文/OpenReview 摘要). [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/82650)  
2. “Probing Synergistic High‑Order Interaction in Infrared and Visible Image Fusion” (SHIP) — CVPR/后续工作（论文摘要与社区解读见 CSDN 博文）。[blog.csdn.net](https://blog.csdn.net/weixin_44184852/article/details/146036111)  
3. DCAFuse: Dual‑Branch Diffusion‑CNN Complementary Feature Aggregation Network for Multi‑Modality Image Fusion, ACM MM 2024（实现/解读与代码说明在社区文章）。[blog.csdn.net](https://blog.csdn.net/qq_42722197/article/details/146433326)  
4. Xu, H., Ma, J., Jiang, J., Guo, X., & Ling, H. U2Fusion: A Unified Unsupervised Image Fusion Network. IEEE Trans. on Pattern Analysis and Machine Intelligence (TPAMI), 2022.（被上列综述与多篇工作引用，作为无监督端到端基线）[参见相关综述引用]  
5. Li, Y., Zhang, Z., & Qi, Y. 基于 Transformer‑CNN 的红外与可见光融合网络 (2025, Journal of Image and Signal Processing). [pdf.hanspub.org/jisp_2670448.pdf](https://pdf.hanspub.org/jisp_2670448.pdf)  
6. Tang, L., Yuan, J., Zhang, H., Jiang, X., & Ma, J. PIAFusion: A Progressive Infrared and Visible Image Fusion Network Based on Illumination Aware. Information Fusion, 2022.（被多篇工作作为对比与启发）[参见相关文献列表]  
7. 汤文超, 丁德锐, 袁浩成, 刘华卿. MCT‑Net: Mix CNN‑Transformer Multi‑scale Feature Network for Liver Tumor Segmentation. Modeling & Simulation, 2025. [pdf.hanspub.org/mos2025141_372572027.pdf](https://pdf.hanspub.org/mos2025141_372572027.pdf)  
8. Chen, Q. 跨模态自适应特征融合的视觉问答方法 (视觉问答方向，2025). [hit.alljournals.cn](https://hit.alljournals.cn/hitxb_cn/article/html/20250410)  
9. 田傲翔, 张长伦. 多模态深度学习中的决策级融合方法及其应用研究. Journal of Image and Signal Processing, 2025.（决策级/证据理论与集成综述）[pdf.hanspub.org/jisp_2670441.pdf](https://pdf.hanspub.org/jisp_2670441.pdf)  
10. 《多模态医学数据融合技术及应用》综述（山东大学学报(医学版), 2025）— 医学多模态融合背景与临床落地挑战总结。[cjournal.hep.com.cn](https://cjournal.hep.com.cn/1671-7554/CN/1190599147562291324)  
11. 关于 DCAFuse / 扩散‑CNN 融合思路的社区/博客总结（用于算法思想与实现细节参考）。[blog.csdn.net](https://blog.csdn.net/qq_42722197/article/details/146433326)  
12. SHIP 及其延伸工作在融合、全色锐化与高阶交互方面的讨论（社区/会议摘要与实现说明）。[blog.csdn.net](https://blog.csdn.net/weixin_44184852/article/details/146036111)

（注）本文重点引用并解读了 2022–2025 年期间公开的代表性论文/综述与社区实现说明；为便于读者后续检索，参考链接采用了检索到的论文/实现或期刊页面（见上文链接）。若需我把每篇论文的 DOI / 原始会议/期刊正式引用条目逐条列出并给出 arXiv/DOI 链接，我可在下一步提供完整 BibTeX/DOI 列表。