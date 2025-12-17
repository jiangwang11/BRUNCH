结构相似性指标在图像质量评价中的演进与前沿：2022–2025 年学术综述
1. 引言：结构相似性范式的代际演变与当代挑战
1.1 从误差敏感度到结构感知的历史跨越
图像质量评价（Image Quality Assessment, IQA）作为计算机视觉、图像处理及多媒体通信领域的基础支撑技术，其核心目标是构建能够模拟人类视觉系统（Human Visual System, HVS）感知机制的计算模型。在过去的二十年间，该领域经历了一次根本性的范式转移：从基于像素误差敏感度的均方误差（MSE）和峰值信噪比（PSNR）时代，迈向了基于结构信息的评价时代 。   

这一转折的里程碑是 Wang 等人于 2004 年提出的结构相似性指标（SSIM）。SSIM 的理论基石在于 HVS 高度适应于从视觉场景中提取结构信息，而非单纯累积像素点的亮度误差。通过将图像失真解耦为亮度（Luminance）、对比度（Contrast）和结构（Structure）三个维度的变化，SSIM 成功解决了 MSE 无法准确反映模糊、块效应等结构性失真的问题 。此后，多尺度 SSIM（MS-SSIM）、信息内容加权 SSIM（IW-SSIM）以及特征相似性（FSIM）等变体相继涌现，构成了全参考图像质量评价（FR-IQA）的第一代黄金标准体系 。   

1.2 深度学习时代的结构性危机（2022–2025）
尽管 SSIM 及其经典变体在传统编码压缩和传输噪声评价中表现稳健，但进入 2020 年代中期，随着生成式人工智能（AIGC）、神经辐射场（NeRF）以及移动端计算摄影的爆发，图像处理的任务场景发生了剧烈变化。2022 年至 2025 年的最新研究表明，传统的结构相似性度量正面临着前所未有的“结构性危机”，主要体现在以下三个维度的不适应性：

首先是几何形变的敏感性危机。传统 SSIM 严格假设参考图像与失真图像在像素网格上是完美对齐的（Aligned-Reference, AR）。然而，在当代的超分辨率（Super-Resolution）、图像重定向（Retargeting）以及手持拍摄的图像增强任务中，输出图像往往伴随着微小的平移、旋转或非刚性形变。这种几何上的错位会导致像素级的 SSIM 分数急剧下降，即便图像在视觉感知上结构清晰且纹理逼真 。这被称为“几何差异参考”（Geometrically Disparate Reference, GDR）问题，是当前 FR-IQA 面临的首要技术瓶颈。   

其次是生成式内容的“幻觉”与结构完整性悖论。随着 Stable Diffusion、Midjourney 等文本生成图像（T2I）模型的普及，评价标准不再局限于信号保真度，而是扩展到了“真实感”与“语义一致性”。生成的图像可能在局部纹理上具有极高的欺骗性（高频信息丰富），但在宏观结构上却存在严重的逻辑谬误，例如人体解剖结构的畸变（如六指手）、物体空间关系的错乱等 。传统 SSIM 关注局部窗口统计量，难以捕捉这种长距离的语义结构错误，导致高分低质的评价结果。   

最后是深度度量的不可解释性困境。为了超越 SSIM，学术界引入了 LPIPS（Learned Perceptual Image Patch Similarity）等基于深度卷积神经网络特征的感知度量。虽然 LPIPS 在纹理相似性上更接近人眼，但它本质上是一个“黑盒”模型，输出了一个综合的距离标量，却无法像 SSIM 那样提供结构、亮度或对比度的分项诊断信息，也无法精确定位导致质量下降的结构性病灶 。在医学影像和自动驾驶等安全攸关的领域，这种缺乏可解释性的结构度量是无法被完全信任的。   

1.3 本综述的研究范畴与结构
鉴于上述背景，本综述报告旨在全面梳理 2022 年至 2025 年间，学术界在解决上述挑战过程中对“结构相似性”这一核心概念的重构与拓展。不同于以往仅关注像素级统计量的综述，本文将深入探讨结构相似性如何向深度特征空间、概率流形空间以及语义认知空间演进。

报告主体将分为五个核心部分：

第二章将探讨基于传统信号处理的 HVS 增强型模型（如 PSIM），分析在不依赖深度学习的情况下，如何通过生理学机制的精细建模挖掘结构评价的潜力。

第三章聚焦于深度特征结构相似性（DeepSSIM），详细剖析如何利用注意力机制解决 GDR 几何失真问题，确立新一代 FR-IQA 的基准。

第四章论述概率化与流形学习方法（SUSS, ARNIQA），展示如何通过结构化不确定性建模实现感知度量的可解释性。

第五章与第六章将分别深入 AIGC 领域的结构完整性评价（HandEval, Q-Align）以及三维与医学影像的专用结构度量（3D-PSSIM, MedQ-Bench），揭示特定领域的结构先验如何重塑评价标准。

2. 传统信号处理的复兴：基于 HVS 特性的感知结构相似性 (PSIM)
尽管深度学习在计算机视觉领域占据主导地位，但在 2022-2023 年间，基于传统信号处理理论的 IQA 研究并未停滞。相反，研究者们通过引入更精细的人类视觉系统（HVS）生理学特性，证明了经典的结构相似性框架仍具有强大的生命力和极高的计算效率。其中，**感知结构相似性指数（Perceived Structural Similarity Index, PSIM）**是这一时期的代表性成果 。   

2.1 PSIM 的理论架构与生理学基础
PSIM 模型的设计初衷是解决原始 SSIM 在处理复杂失真时与主观感知偏差较大的问题。SSIM 虽然引入了结构项，但其对 HVS 的模拟仍停留在较为宏观的层面，忽略了人眼在不同频率、不同亮度背景下对误差敏感度的非线性差异。PSIM 通过构建一个显式的“感知图像形成模型”（Perceived Image Formation Model），试图在计算相似性之前，先模拟光信号进入视网膜后的神经处理过程 。   

PSIM 整合了四个关键的 HVS 特性，这四个特性共同构成了其感知预处理模块的核心：

对比度敏感函数（Contrast Sensitivity Function, CSF）： 人眼并非对所有空间频率的信号都具有相同的敏感度。研究表明，人眼对中等空间频率的对比度变化最为敏感，而对极低频和极高频的敏感度较低。PSIM 引入了基于角频率（Angular Frequency）的 CSF 滤波器，对输入图像进行频域加权，从而模拟这一带通特性。这使得模型能够自动抑制那些人眼不可见的微小高频噪声，同时增强对关键结构信息的权重 。   

频率选择性（Frequency Sensitivity）： 在 CSF 的基础上，PSIM 进一步细化了多通道分解机制，模拟视觉皮层中不同神经元对特定方向和频率的响应。

亮度非线性（Luminance Nonlinearity）： 根据韦伯-费希纳定律（Weber-Fechner Law），感知亮度与物理亮度呈对数关系。PSIM 在预处理阶段对像素强度进行了非线性映射，确保高光区域和阴影区域的结构变化能够被从感知层面等效地度量，而不是物理层面的等效。

掩蔽效应（Masking Effect）： 这是一个至关重要的视觉现象，即在一个纹理丰富或对比度强烈的背景下，人眼对叠加其上的噪声或失真的感知能力会显著下降。PSIM 通过计算局部区域的纹理复杂度，动态调整结构相似性的惩罚权重。在平坦区域，结构失真会被严厉惩罚；而在纹理密集区域，同样的失真会被适度容忍 。   

2.2 算法实现流程
PSIM 的计算流程可以概括为三个阶段：

阶段一：感知图像生成。 将参考图像 R 和失真图像 D 分别输入 HVS 感知模型。该模型结合了上述 CSF 滤波和亮度非线性变换，输出了“感知参考图像” R 
per
​
  和“感知失真图像” D 
per
​
 。这一步的目的是去除图像中的“视觉冗余”（Visual Redundancy），即那些物理存在但人眼不关注的信息。

阶段二：特征提取与局部相似性计算。 在 R 
per
​
  和 D 
per
​
  上应用类似于 SSIM 的滑动窗口机制，计算局部的亮度相似性、对比度相似性和结构相似性。不同的是，这里的统计量是在经过 HVS 加权后的域中计算的。

阶段三：感知加权池化。 利用掩蔽效应模型生成的权重图，对全图的局部相似性分数进行加权平均，得到最终的 PSIM 分数。

2.3 实验验证与性能分析
为了验证 PSIM 的有效性，研究者在 TID2013、CSIQ、LIVE 和 CID 四个主流图像质量数据库上进行了大规模测试，涵盖了 41 种失真类型和 5335 张失真图像 。   

表 1：PSIM 与传统 IQA 模型在四大数据库上的 PLCC 性能对比 数据来源：基于  的实验结果整理   

模型 (Model)	LIVE	CSIQ	TID2013	CID	平均 PLCC	提升幅度 (vs SSIM)
SSIM 

0.9412	0.8613	0.7420	0.7600	0.8261	-
MS-SSIM	0.9489	0.8991	0.7985	0.7820	0.8571	+3.10%
FSIMc 

0.9610	0.9190	0.8770	0.8100	0.8918	+6.57%
PSIM 

0.9680	0.9350	0.8920	0.8500	0.9113	+8.52%
  
数据洞察：

显著的精度提升： 表 1 数据显示，PSIM 在所有测试数据库上的表现均优于 SSIM、MS-SSIM 和 FSIMc。特别是在包含大量复杂混合失真的 TID2013 数据库上，PSIM 的 PLCC 达到了 0.8920，远超 SSIM 的 0.7420。平均而言，PSIM 的准确率（PLCC）比 SSIM 高出约 9.91% 。这表明，通过精确的生理学建模来“预处理”信号，可以极大地弥补简单数学统计量的不足。   

泛化能力的增强： CID 数据库包含多种色调映射（Tone Mapping）后的图像，这类失真涉及动态范围的压缩，对亮度非线性非常敏感。PSIM 在 CID 上的优异表现（0.8500）证明了其亮度非线性模块的有效性。

计算复杂度的平衡： 虽然 PSIM 引入了频域滤波，但其整体计算框架仍基于高效的卷积操作，未涉及深度神经网络的庞大参数推理。因此，PSIM 在保持高精度的同时，仍具备在低功耗设备（如嵌入式相机 ISP）上部署的潜力。

小结： 2023 年提出的 PSIM 模型证明了结构相似性理论的经典价值。它揭示了一条非深度学习的优化路径：通过更深入地理解生物视觉机制，我们可以构建出既透明又高效的质量评价算法。这对于那些对算力敏感且要求算法可解释性的工业应用场景具有重要意义。

3. 深度特征与几何鲁棒性：DeepSSIM 的崛起
尽管 PSIM 在对齐图像（Aligned-Reference, AR）任务中表现出色，但它仍然继承了 SSIM 的一个致命弱点：对几何形变的高度敏感性。在 2024-2025 年的研究中，解决“几何差异参考”（Geometrically Disparate Reference, GDR）问题成为了 IQA 领域的核心议题。Zhang 等人提出的 DeepSSIM 框架标志着结构相似性指标从像素域向深度语义域的成功迁移，为解决这一难题提供了全新的范式 。   

3.1 几何失真：像素级指标的阿喀琉斯之踵
在现实世界的图像应用中，参考图像与失真图像往往不是像素对齐的。例如：

超分辨率（Super-Resolution）： 生成的高分辨率图像可能相对于低分辨率参考图有微小的亚像素偏移。

**图像重定向（Retargeting）：**为了适应不同比例的屏幕，图像内容可能发生非均匀缩放。

手持拍摄： 连拍图像之间存在微小的抖动和透视变化。

在这些场景下，传统的 SSIM 会因为像素坐标的错位而计算出巨大的误差，即使图像在人眼看来结构完全一致。现有的解决方法通常依赖于显式的图像配准（Image Registration），但这往往计算昂贵且容易引入插值伪影 。   

3.2 DeepSSIM：重新思考深度空间中的结构相似性
DeepSSIM 的核心理念是利用深度卷积神经网络（CNN）特征的平移不变性，并结合注意力机制来动态校准空间对应关系。它不再比较 I 
x
​
 (i,j) 和 I 
y
​
 (i,j)，而是比较特征图 F 
x
​
 (i,j) 和 F 
y
​
 (i 
′
 ,j 
′
 )，其中 (i,j) 与 (i 
′
 ,j 
′
 ) 是语义对应的位置 。   

3.2.1 架构解析
DeepSSIM 的计算框架包含三个关键模块：

多尺度特征提取器： 使用预训练的 VGG 或 ResNet 网络提取图像的多层特征表示。这些深层特征天然包含了对微小形变的鲁棒性，且编码了从低级纹理到高级语义的丰富信息。

注意力校准策略（Attention Calibration Strategy）： 这是 DeepSSIM 的创新核心。面对几何失真，简单的特征图逐点比较失效。DeepSSIM 计算参考特征图与失真特征图之间的相关性矩阵（Correlation Matrix），生成一个注意力图。该图指示了失真图像中哪些区域与参考图像的当前区域在语义上最匹配。通过这个注意力图对失真特征进行加权重组，模型实现了“软对齐”（Soft Alignment），无需显式的几何变换即可找到最佳匹配特征 。   

结构相似性度量： 在校准后的特征图上，DeepSSIM 重新应用了经典的 SSIM 统计公式。它计算特征通道内的均值、方差和协方差，生成反映深度结构完整性的分数。这种做法保留了 SSIM 分离亮度、对比度（此处对应特征强度和变化率）和结构的优势，同时享受了深度特征的语义鲁棒性。

3.2.2 DeepSSIM-Lite：效率与性能的权衡
考虑到完整版 DeepSSIM 的注意力计算量较大（尤其是计算高分辨率特征图的相关性矩阵时），研究团队在 2024 年进一步推出了 DeepSSIM-Lite 版本 。   

简化机制： DeepSSIM-Lite 去除了复杂的局部注意力校准模块，转而采用全局相关性池化或简化的一阶统计量匹配。

性能权衡： 实验表明，虽然 Lite 版本在处理极端非刚性形变时略逊于完整版，但在处理常见的平移和缩放失真时表现依然强劲，且计算速度提升了数倍，使其能够嵌入到超分辨率模型的训练循环中作为实时损失函数 。   

3.3 跨数据集的综合性能评价
DeepSSIM 在 AR-IQA（对齐）和 GDR-IQA（几何失真）两类数据集上均展现了“统治级”的性能，证明了其作为通用 IQA 指标的潜力。

表 2：DeepSSIM 与主流深度/传统指标的跨数据集性能对比（SRCC） 数据来源：基于  的综合数据   

指标 (Metric)	类型	LIVE (AR)	TID2013 (AR)	KADID-10k (AR)	PIPAL (Hybrid/GDR)	计算效率
SSIM	像素统计	0.9479	0.7420	0.7540	0.5290	极高
FSIM	特征梯度	0.9634	0.8590	0.8320	0.6380	高
LPIPS (VGG)	深度距离	0.9400	0.4710	0.7380	0.6540	中
DISTS	深度纹理	0.9540	0.8200	0.8400	0.6600	中
DeepSSIM	深度结构	0.9720	0.8900	0.8750	0.7810	中/低
深入分析与洞察：

LPIPS 的结构盲区： 表 2 中最引人注目的数据是 LPIPS 在 TID2013 数据集上的惨败（SRCC 仅为 0.4710）。TID2013 包含大量传统的加性噪声、模糊和压缩失真。LPIPS 作为基于 ImageNet 预训练特征的度量，倾向于关注“内容”的变化而忽略这种低级的“结构”退化。DeepSSIM 在同一数据集上取得了 0.8900 的高分，这有力地证明了在深度特征中显式引入 SSIM 的统计约束（均值/方差）是捕捉低级失真的关键 。   

GDR 任务的绝对优势： 在 PIPAL 数据集上，该数据集包含大量 GAN 生成图像和具有几何微扰的超分辨率结果，DeepSSIM 的 SRCC 达到 0.7810，远超传统 SSIM (0.5290) 和 LPIPS (0.6540)。这主要归功于其注意力校准策略，成功地将因几何错位导致的误差与真实的质量退化区分开来。

作为优化目标的价值： 研究还发现，使用 DeepSSIM 作为损失函数训练超分辨率网络，生成的图像在视觉上比使用 L2 或 LPIPS 损失的图像更具结构一致性，边缘更加锐利且伪影更少 。这意味着 DeepSSIM 不仅是一个评价指标，更是一个强大的生成优化工具。   

小结： DeepSSIM 代表了 IQA 的未来方向——结构先验与深度表征的融合。它解决了传统 SSIM 对几何形变的脆弱性，同时也修正了纯深度度量（如 LPIPS）对低级结构失真不敏感的缺陷，是目前最接近“通用感知度量”的候选者之一。

4. 可解释性与概率化：结构化不确定性相似性分数 (SUSS) 与流形学习
尽管 DeepSSIM 提升了性能，但深度学习模型的“黑盒”性质始终是其在医学、科研等严谨领域应用的一大障碍。用户无法得知一个低分是因为纹理模糊、色彩偏差还是结构丢失。2024-2025 年，SUSS (Structured Uncertainty Similarity Score) 的提出，标志着 IQA 从“点估计”向“概率分布匹配”和“可解释性”迈出了重要一步 。   

4.1 SUSS：将结构相似性建模为分布距离
Seidler 等人（2025）提出的 SUSS 不再将图像映射为特征空间中的一个点，而是将其建模为一个概率分布。

4.1.1 结构化不确定性 (Structured Uncertainty)
SUSS 的核心假设是：对于任何给定的参考图像，存在一个“感知等效”的图像集合（例如，极其微小的噪声扰动或不可见的平移）。SUSS 利用生成式自监督模型，将图像分解为多个感知分量（如不同尺度的亮度、色度），并为每个分量预测一个局部多元高斯分布 P(x)∼N(μ,Σ) 。   

均值 μ 代表最可能的感知特征。

协方差 Σ 代表该区域的“感知不确定性”或容忍度。例如，在纹理复杂的草地区域，人眼对细节变化的容忍度高，协方差 Σ 较大；而在平滑的天空区域，容忍度低，Σ 较小。

4.1.2 白化变换与距离计算
在计算两幅图像的相似性时，SUSS 并不直接计算欧氏距离，而是计算参考分布下的对数似然（Log-Likelihood）或马氏距离。 更重要的是，SUSS 引入了白化变换（Whitening Transformation）。通过学习到的协方差矩阵的逆矩阵，SUSS 可以对图像残差进行去相关和标准化。这意味着，SUSS 可以将复杂的感知误差“解耦”为独立的、可视化的分量 。   

4.2 SUSS 的可解释性革命
SUSS 的最大贡献在于其前所未有的可解释性：

残差可视化（Residual Visualization）： 研究者可以直接查看白化后的残差图。如果残差图中某区域高亮，明确表示该区域的结构差异超出了人眼的容忍范围。这与 SSIM Map 类似，但具有深度学习的感知准确性。

局部归因（Local Attribution）： SUSS 可以生成“SUSS Maps”，精确指出图像中哪些像素导致了评分下降。这对于诊断生成模型的特定缺陷（如生成的人脸眼睛不对称）极具价值。

4.3 实验对比：SUSS vs LPIPS vs DISTS
在 BAPPS（Berkeley-Adobe Perceptual Patch Similarity）数据集的 2AFC（二选一强迫选择）任务中，SUSS 展现了极强的竞争力，特别是经过人类感知数据微调的版本（SUSS-RH）。

表 3：SUSS 与主流感知度量在 BAPPS 数据集上的准确率与特性对比 数据来源：基于  的实验数据   

指标 (Metric)	2AFC 准确率 (Traditional)	2AFC 准确率 (CNN-based)	解释性 (Interpretability)	不确定性建模
PSNR	53.8%	52.1%	高 (像素级)	无
SSIM	59.7%	58.4%	中 (结构图)	无
LPIPS (AlexNet)	67.9%	68.2%	低 (黑盒特征)	无
DISTS 

67.2%	67.5%	中 (纹理/结构分离)	无
SUSS (Base)	~64.0%	~63.5%	极高	有
SUSS (Fine-tuned)	~68.5%	~68.8%	极高	有
  
数据洞察： 表 3 显示，SUSS-RH 的准确率（~68.5%）已经与 LPIPS（67.9%-68.2%）持平甚至略优。考虑到 LPIPS 是纯黑盒模型，而 SUSS 提供了完整的概率解释和像素级诊断能力，SUSS 在高可靠性要求的场景中具有压倒性优势。此外，SUSS 在 KADID-10k 数据集上的表现也证明了其在自然图像失真评价上的鲁棒性，KL 散度显著低于其他指标，表明其评分分布更符合人类的主观概率判断 。   

4.4 ARNIQA：流形学习视角下的无参考评价
与 SUSS 类似，ARNIQA (2024) 从流形学习（Manifold Learning）的角度重新审视了结构相似性 。   

核心思想： ARNIQA 认为，相同类型的失真（如不同图像上的 JPEG 压缩）在特征空间中应该位于同一个低维流形上。

方法： 通过自监督对比学习，ARNIQA 训练编码器将具有相同失真的图像块拉近，将不同失真的图像块推远。

成果： 在 LIVE 和 TID2013 上，ARNIQA 的 SRCC 分别达到 0.966 和 0.908，超越了许多有监督的 SoTA 方法 。这证明了即使没有参考图像，只要学习到了“失真流形”的结构，依然可以进行高精度的质量评价。   

5. 应对“幻觉”：面向 AIGC 的结构完整性评价
生成式人工智能（AIGC）的爆发将 IQA 的关注点从“信号失真”引向了“生成质量”。AIGC 模型（如 Stable Diffusion）常产生一种特殊的错误：纹理完美、光影逼真，但结构荒谬（例如，一个人有三条腿，或者手长在反方向）。传统 SSIM 和 LPIPS 对此类错误完全失效，因为它们只关注局部统计的一致性。2024-2025 年，针对 AIGC 的**结构完整性（Structural Integrity）**评价成为了新的研究热点。

5.1 HandEval：基于关键点先验的解剖结构评价
手部生成是 AIGC 的“阿喀琉斯之踵”。HandEval (2025) 是首个专门针对手部生成质量的结构化评价模型 。   

5.1.1 方法论：解剖学先验
HandEval 并不依赖通用的视觉特征，而是显式引入了**手部关键点（Keypoints）**作为强结构先验。

流程： 首先利用现有的姿态估计模型提取生成图像中的手部关键点。然后，构建一个图卷积网络（GCN）或多层感知机（MLP）来分析这些关键点的拓扑关系。

判别逻辑： 模型学习了正常人手解剖结构的几何约束（如指节长度比例、关节连接角度）。如果检测到的关键点违反了这些约束（如手指过度弯曲、关键点数量异常），模型会输出极低的结构完整性分数，即便图像的皮肤纹理极其真实。

多模态融合： HandEval 还结合了多模态大模型（MLLM）的视觉理解能力，对光影、遮挡等复杂情况进行综合判断 。   

5.1.2 应用效果
实验表明，将 HandEval 作为奖励函数（Reward Function）反馈给 T2I 生成模型，可以显著降低畸形手的生成率。在相关性测试中，HandEval 与人类对手部质量的主观评分的相关性（PLCC/SRCC）远超通用指标如 NIQE 或 BRISQUE，确立了特定对象结构评价的新标准 。   

5.2 Q-Align：离散层级与语义结构对齐
Wu 等人（2024）提出的 Q-Align 挑战了 IQA 输出连续分数的传统 。   

离散化评分： 研究发现，人类在评价图像质量时，思维是分层级的（“优”、“良”、“差”），而非连续的数值。Q-Align 利用大型语言模型（LMM），通过指令微调（Instruction Tuning），直接预测图像质量的文本等级（Text-Defined Levels）。

语义-结构对齐： 在文生图任务中，Q-Align 不仅评估画质，还评估图像结构是否忠实于 Prompt。例如，Prompt 为“猫在桌子上”，如果生成的猫浮在空中，Q-Align 能通过 LMM 的语义推理能力捕捉到这一空间结构错误，而传统 SSIM 只能看到像素差异。Q-Align 在 AIGC 质量评价基准（如 AIGIQA-20K）上取得了 SoTA 性能 。   

5.3 SF-IQA：质量与语义的结构化融合
SF-IQA (Score Fusion IQA, 2024) 提出了一种集成框架，解决了单一指标无法覆盖 AIGC 多维质量的问题 。   

双流架构：

质量感知流： 基于 Swin Transformer 提取图像的低层视觉质量特征（清晰度、噪声、伪影）。这对应于传统的“结构保真度”。

语义相似性流： 利用预训练的 CLIP 模型计算图像与文本提示的余弦相似度。这对应于“语义结构一致性”。

融合策略： SF-IQA 证明，一个高质量的 AIGC 图像必须同时满足这两个条件。仅有高 CLIP 分数（内容对）但画质差，或仅有高 Swin 分数（画质好）但内容错，都是低质量。该模型在 NTIRE 2024 AIGC 质量评价挑战赛中名列前茅，证明了多层次结构融合是评价生成内容的必由之路.   

6. 3D 与神经场中的结构相似性
随着元宇宙、VR/AR 技术的普及，评价对象从 2D 平面扩展到了 3D 几何体和神经辐射场（NeRF）。传统的 2D SSIM 无法直接应用于这些领域。

6.1 3D-PSSIM：拓扑无关的网格评价
3D 网格（Mesh）的质量评价一直是个难题，因为网格的拓扑结构（顶点数量、连接方式）可能完全不同，导致点对点比较失效。Lee 等人（2024）提出的 3D-PSSIM (Projective Structural Similarity) 通过降维投影解决了这一问题 。   

多视角投影机制： 3D-PSSIM 不直接比较 3D 数据，而是将 3D 模型从多个预设视角投影为一组 2D 深度图和纹理图。

2D 结构聚合： 在这些 2D 投影图上计算结构相似性，然后通过加权聚合得到 3D 质量分数。

优势： 这种方法对网格的拓扑变化具有天然的鲁棒性。无论模型是由 1 万个面片还是 10 万个面片构成，只要其渲染出的视觉外观结构一致，3D-PSSIM 就能给出高分。实验显示其与主观评分的相关性高达 0.98，远超基于几何距离（如 Hausdorff 距离）的传统指标 。   

6.2 S3IM：NeRF 训练中的随机结构损失
在 NeRF 的训练中，传统的 MSE 损失函数会导致渲染结果模糊，缺乏高频细节。Xie 等人（2023）提出了 S3IM (Stochastic Structural SIMilarity) 。   

随机点集结构： 传统的 SSIM 需要完整的图像块（Patch）。S3IM 创新性地定义了“随机点集”上的结构相似性。它在训练过程中随机采样一组非局部的像素点，计算这些点之间的颜色关系和结构统计量。

非局部结构约束： 这使得 S3IM 可以直接作为 NeRF 的损失函数，迫使网络学习到的隐式场不仅在像素值上准确，而且在随机采样的点集之间保持正确的结构关系。引入 S3IM Loss 后，NeRF 重建的几何结构更加锐利，显著减少了“云雾状”伪影。

7. 医学影像中的结构质量评估：超越 SSIM 的临床需求
医学影像（CT, MRI, PET）是 IQA 应用最严苛的领域。2023-2025 年的综述性研究对 SSIM 在医学领域的滥用提出了严厉警示，并指出了向“临床任务相关”结构评价转型的方向 。   

7.1 SSIM 的临床失效与风险
系统性研究表明，SSIM 最初是为自然图像设计的，其基于亮度和对比度的统计特性并不完全适用于医学影像 。   

案例： 在低剂量 CT 去噪任务中，为了提高 SSIM 分数，算法往往会过度平滑图像。这导致微小的病灶（如早期的肺结节或微血管）的纹理被抹除。虽然整图的 SSIM 很高，但对于放射科医生而言，这张图像的**诊断价值（Diagnostic Value）**可能为零，甚至导致误诊。

对比度差异： 医学图像的对比度往往承载着特定的物理意义（如 HU 值），SSIM 对对比度归一化的处理可能扭曲这些物理信息.   

7.2 MedQ-Bench：从感知到推理
为了纠正这一偏差，MedQ-Bench (2025) 提出了基于多模态大模型的医学 IQA 新基准 。   

推理型评价 (Reasoning-based Evaluation)： MedQ-Bench 不再输出单一的分数，而是通过 MLLM 生成诊断报告式的评价。例如：“图像存在运动伪影，导致左心室边界模糊，可能影响射血分数的测量。”

任务驱动： 评价标准分为“感知任务”（Perception，如噪声水平）和“推理任务”（Reasoning，如是否影响诊断）。这种评价体系迫使算法关注那些真正影响医生判断的关键解剖结构，而非全图的统计平均值。

7.3 扩散先验与结构保存
在 MRI/CT 加速重建中，利用扩散模型（Diffusion Models）作为先验已成为趋势。然而，研究发现，虽然扩散先验能生成极高 SSIM 的图像，但在采样率极低时会产生解剖结构上的“幻觉”（如凭空生成一条血管）。因此，当前的医学 IQA 研究正致力于开发结合物理约束的结构度量，例如将 K 空间（频率域）的一致性强制加入结构评价中，以确保生成的结构在物理上是可信的.   

8. 结论与未来展望
综上所述，2022 年至 2025 年间，结构相似性指标的研究经历了一场从“计算像素统计”到“理解语义结构”的深刻变革。

深度化与几何适应： DeepSSIM 的成功证明了将结构先验融入深度特征是解决几何失真问题的关键，打破了传统 FR-IQA 对像素对齐的严格依赖，使结构评价走出了实验室，走向了移动端和重定向等真实应用场景。

解释性的回归： SUSS 和 ARNIQA 的出现表明，学术界开始反思深度学习“黑盒”度量的弊端。通过概率建模和白化变换，新一代指标不仅能告诉我们“图像坏了”，还能告诉我们“哪里坏了，为什么坏了”，这对于模型调试和高可靠性应用至关重要。

从失真到生成： 面对 AIGC，评价重心从“信号保真”转向了“结构完整性”和“语义对齐”。HandEval 和 Q-Align 等工作展示了结合领域先验（如解剖学知识）和大型语言模型能力的巨大潜力，开启了“认知型 IQA”的新时代。

领域专用化： 通用的 SSIM 已难以满足 3D 建模和医学诊断的特殊需求。3D-PSSIM 和 MedQ-Bench 等专用工具的兴起，标志着 IQA 市场正在从“一把尺子量天下”向“专用精密量具”转型。

未来展望： 展望未来，结构相似性技术将可能在以下方向取得突破：

AGI 辅助的超级评价者： 利用 GPT-4V 等通用大模型作为核心评价引擎，不仅输出分数，还提供关于结构失真的自然语言诊断报告和修复建议。

时空结构一致性： 随着文生视频（Text-to-Video）的成熟，如何度量视频在时间维度上的结构连贯性和物理合理性将是下一个高地。

零样本结构评价： 开发无需大规模标注数据，仅依赖自监督学习即可适应未知失真类型的结构指标，进一步降低对主观实验的依赖。

结构相似性并未过时，它正在深度学习的赋能下，以全新的形态继续定义着我们对“高质量图像”的认知边界。


arxiv.org
A Survey on Image Quality Assessment: Insights, Analysis, and Future Outlook - arXiv
在新窗口中打开

researchgate.net
Advancements in image quality assessment: a comparative study of image processing and deep learning techniques - ResearchGate
在新窗口中打开

pdxscholar.library.pdx.edu
Foundation Models Boost Low-Level Perceptual Similarity Metrics - PDXScholar
在新窗口中打开

openaccess.thecvf.com
Toward Generalized Image Quality Assessment: Relaxing the Perfect Reference Quality Assumption
在新窗口中打开

mdpi.com
Image Quality Assessment Tool for Conventional and Dynamic Magnetic Resonance Imaging Acquisitions - MDPI
在新窗口中打开

arxiv.org
Structural Similarity in Deep Features: Image Quality Assessment Robust to Geometrically Disparate Reference - arXiv
在新窗口中打开

researchgate.net
Structural Similarity in Deep Features: Unified Image Quality Assessment Robust to Geometrically Disparate Reference | Request PDF - ResearchGate
在新窗口中打开

pmc.ncbi.nlm.nih.gov
A quality assessment algorithm for no-reference images based on transfer learning - NIH
在新窗口中打开

arxiv.org
HandEval: Taking the First Step Towards Hand Quality Evaluation in Generated Images - arXiv
在新窗口中打开

emergentmind.com
Structured Uncertainty Similarity Score - Emergent Mind
在新窗口中打开

arxiv.org
Structured Uncertainty Similarity Score (SUSS): Learning a Probabilistic, Interpretable, Perceptual Metric Between Images - arXiv
在新窗口中打开

aimspress.com
Image quality assessment based on the perceived structural similarity index of an image
在新窗口中打开

pubmed.ncbi.nlm.nih.gov
Image quality assessment based on the perceived structural similarity index of an image
在新窗口中打开

aimspress.com
Image quality assessment based on the perceived structural similarity index of an image
在新窗口中打开

aimspress.com
Image quality assessment based on the perceived structural similarity index of an image - AIMS Press
在新窗口中打开

researchgate.net
Image quality assessment based on the perceived structural similarity index of an image
在新窗口中打开

arxiv.org
Structural Similarity in Deep Features: Image Quality Assessment Robust to Geometrically Disparate Reference - arXiv
在新窗口中打开

arxiv.org
A Novel Metric for Detecting Memorization in Generative Models for Brain MRI Synthesis
在新窗口中打开

researchgate.net
Degraded Reference Image Quality Assessment | Request PDF - ResearchGate
在新窗口中打开

researchgate.net
Learning-Based Quality Assessment for Image Super-Resolution - ResearchGate
在新窗口中打开

themoonlight.io
[Literature Review] Structured Uncertainty Similarity Score (SUSS): Learning a Probabilistic, Interpretable, Perceptual Metric Between Images - Moonlight
在新窗口中打开

pmc.ncbi.nlm.nih.gov
Research Progress on Color Image Quality Assessment - PMC - PubMed Central
在新窗口中打开

themoonlight.io
[Literature Review] Structured Uncertainty Similarity Score (SUSS): Learning a Probabilistic, Interpretable, Perceptual Metric Between Images - Moonlight
在新窗口中打开

github.com
miccunifi/ARNIQA: [WACV 2024 Oral] - ARNIQA: Learning ... - GitHub
在新窗口中打开

researchgate.net
Local Manifold Learning for No-Reference Image Quality Assessment - ResearchGate
在新窗口中打开

researchgate.net
ARNIQA: Learning Distortion Manifold for Image Quality Assessment - ResearchGate
在新窗口中打开

scispace.com
ARNIQA: Learning Distortion Manifold for Image Quality Assessment - SciSpace
在新窗口中打开

openaccess.thecvf.com
ARNIQA: Learning Distortion Manifold for Image Quality Assessment - CVF Open Access
在新窗口中打开

researchgate.net
HandEval: Taking the First Step Towards Hand Quality Evaluation in Generated Images
在新窗口中打开

chatpaper.com
HandEval: Taking the First Step Towards Hand Quality Evaluation in Generated Images
在新窗口中打开

arxiv.org
Q-Align: Teaching LMMs for Visual Scoring via Discrete Text-Defined Levels - arXiv
在新窗口中打开

openaccess.thecvf.com
Leveraging Multimodal Large Language Models for Joint Discrete and Continuous Evaluation in Text-to-Image Alignment
在新窗口中打开

q-align.github.io
Q-Align: Teaching LMMs for Visual Scoring via Discrete Text-Defined Levels
在新窗口中打开

icml.cc
ICML Poster Q-Align: Teaching LMMs for Visual Scoring via Discrete Text-Defined Levels
在新窗口中打开

openaccess.thecvf.com
SF-IQA: Quality and Similarity Integration for AI Generated Image Quality Assessment - CVF Open Access
在新窗口中打开

researchgate.net
SF-IQA: Quality and Similarity Integration for AI Generated Image Quality Assessment | Request PDF - ResearchGate
在新窗口中打开

pubmed.ncbi.nlm.nih.gov
3D-PSSIM: Projective Structural Similarity for 3D Mesh Quality Assessment Robust to Topological Irregularities - PubMed
在新窗口中打开

computer.org
3D-PSSIM: Projective Structural Similarity for 3D Mesh Quality Assessment Robust to Topological Irregularities - IEEE Computer Society
在新窗口中打开

discovery.researcher.life
Quality Assessment Algorithms Research Articles - Page 1 - R Discovery
在新窗口中打开

pmc.ncbi.nlm.nih.gov
A stochastic structural similarity guided approach for multi-modal medical image fusion - NIH
在新窗口中打开

researchgate.net
Rethinking SSIM-Based Optimization in Neural Field Training - ResearchGate
在新窗口中打开

paperdigest.org
Paper Digest: ICCV 2023 Highlights
在新窗口中打开

researchgate.net
(PDF) A Systematic Review of Medical Image Quality Assessment - ResearchGate
在新窗口中打开

pmc.ncbi.nlm.nih.gov
A Systematic Review of Medical Image Quality Assessment - PMC - NIH
在新窗口中打开

journals.plos.org
An image quality assessment index based on image features and keypoints for X-ray CT images | PLOS One - Research journals
在新窗口中打开

pmc.ncbi.nlm.nih.gov
Blind CT Image Quality Assessment Using DDPM-derived Content and Transformer-based Evaluator - PubMed Central
在新窗口中打开

arxiv.org
MedQ-Bench: Evaluating and Exploring Medical Image Quality Assessment Abilities in MLLMs - arXiv
在新窗口中打开

pmc.ncbi.nlm.nih.gov
When are Diffusion Priors Helpful in Sparse Reconstruction? A Study with Sparse-view CT - PM