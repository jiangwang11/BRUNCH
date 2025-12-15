引言  
本综述聚焦 2022–2025 年间无监督/半监督（self‑/semi‑supervised）单目与多帧深度估计领域的代表性工作，侧重方法学分类、每类关键论文的技术要点与实验结论，以及跨论文的实验共性和未来研究趋势预测。本文仅讨论公开发表于会议/期刊或 arXiv 的工作，并在方法段对每篇论文用 4–6 句概述研究问题、核心方法与关键实验结论（以可重复的技术信息为主，避免泛泛而谈）。

方法分类与代表作  
（注：每条后括号内给出可检索来源/主页）

A. 大规模伪标注与半监督 / 未标注数据的利用
- Depth Anything — 大规模未标注数据与语义特征对齐（CVPR/arXiv, 2024）  
  研究问题：如何把海量未标注单目图像变成对深度估计有用的半监督训练资源以提升零样本泛化。  
  核心方法：先用多数据集训练的教师网络为未标注图像生成伪深度，再在学生训练中对未标注样本施加强扰（色彩失真、CutMix 等）并加入与预训练语义编码器（如 DINOv2）特征的对齐损失以抑制伪标签噪声。  
  关键结论：在大量多样化未标注数据 + 强扰动策略下，学生模型的 zero‑shot 相对深度泛化与微调后度量深度性能均显著优于仅用有标签数据训练的基线（见作者在多个标准数据集上的横向对比）。（详见论文与实现）[blog.csdn.net](https://blog.csdn.net/weixin_43559672/article/details/136353717)

- HCVNet — 混合 CNN‑ViT 与自监督知识蒸馏（Modeling & Simulation, 2024）  
  研究问题：在自监督单目深度估计中如何同时获取局部细节与全局上下文并高效利用未标注数据。  
  核心方法：提出 CNN‑ViT 混合编码器（Conv stem + ConvFFN + 小规模注意力模块）与通道特征聚合模块，并通过一种单阶段/同步的自知识蒸馏（teacher from previous epoch）提供额外监督。  
  关键结论：在 KITTI/Make3D 的实验中，该混合架构与自蒸馏策略能在不显著增加标注数据的情况下提高深度估计精度并改善远景与边界细节，但代价是计算复杂度上升。[image.hanspub.org](https://image.hanspub.org/html/80-2571621_87686.htm)

B. 多帧 / 多视角自监督与成本体构建
- ManyDepth / The Temporal Opportunist（多帧自监督方向的里程碑，CVPR/2021；后续多帧工作延续此思路）  
  研究问题：如何在自监督框架下融合邻帧几何线索以提升深度精度，同时抑制动态物体与遮挡带来的伪信号。  
  核心方法：构建可用时间信息的成本体（cost volume）或多视角融合体，并用单帧线索/掩码去辨别并忽略成本体中不可靠区域（如运动物体）。  
  关键结论：在静态或准静态区域，多帧方法带来明显精度提升；但在动态场景与无纹理区域需要额外的单帧先验或鲁棒机制以避免错误的几何融合（作为后续多帧工作的设计基线）。

- M2Depth — 两帧多摄像头的度量深度估计（2024，预印/实现）  
  研究问题：如何利用车辆环视/多摄像头两帧输入获得具有真实尺度（metric）且鲁棒的周边深度估计。  
  核心方法：在空间与时间两个维度分别构建代价体并提出空间—时间融合模块，结合神经先验（如 SAM 特征）以减少前后景混淆并加强边缘。  
  关键结论：在 nuScenes/DDAD 等多摄像头基准上，该方法在尺度感知的多视角深度上取得领先（实验显示空间—时间代价体对边界与尺度恢复尤为有利）。[hub.baai.ac.cn](https://hub.baai.ac.cn/paper/f0316ba8-fa2c-4e7d-833b-390e3cbe0531)

- 多尺度特征增强的多帧方法（光学期刊，2024）  
  研究问题：在户外自动驾驶场景下，多帧成本体结合更强的空间结构特征能否改善边缘与伪影问题。  
  核心方法：在多帧成本体基础上引入大核注意力（LKA）激活模块、结构增强模块和动态上采样（Dysample）来保留长程空间信息与恢复细节。  
  关键结论：对 KITTI/Cityscapes 的评测表明此类多尺度编码器+结构增强可减少边缘伪影并提升 δ<1.25 等常用指标，但同时带来参数与 FLOPs 增加。[opticsjournal.net](https://www.opticsjournal.net/Articles/OJa00c675cd4311d5f/FullText)

C. 不确定性度量、集成与后处理
- Self‑Supervised Monocular Depth Estimation by Digging into Uncertainty Quantification（JCST，2023）  
  研究问题：如何在自监督训练过程中识别模型对深度预测不确定的区域并据此改进训练与后处理。  
  核心方法：提出基于 snapshot（不同 epoch 模型方差）和 siam‑style（同 epoch 双胞胎模型）两类不确定性测度；把不确定性引导项写入损失并在推理阶段用集成策略对深度图自适应后处理。  
  关键结论：在尖细物体、运动物体边界与弱纹理区域，不确定性引导能定向提升局部精度；集成后处理在视觉效果和若干量化指标上均有改善。[jcst.ict.ac.cn](https://jcst.ict.ac.cn/cn/article/doi/10.1007/s11390-023-3088-y)

D. 鲁棒性 / 对抗训练与安全性
- Self‑supervised Adversarial Training of Monocular Depth Estimation against Physical‑World Attacks（2024）  
  研究问题：单目深度估计在物理世界攻击（如投贴、光照扰动）下的鲁棒性如何提升而不依赖真深度标签。  
  核心方法：在自监督视图合成训练管线中加入 L0‑约束的稀疏扰动并做对抗训练，设计与深度估计任务相关的对比与再投影稳健项以提升真实场景下的鲁棒性。  
  关键结论：针对若干常见物理攻击，该自监督对抗训练显著提高模型的稳健性，同时对未攻击情况下的基线性能影响有限（表明可在自监督设置下兼顾鲁棒性与性能）。[hub.baai.ac.cn](https://hub.baai.ac.cn/paper/ee0c8799-c366-43fa-845c-737990abb745)

E. 架构/注意力设计与通道级增强（单帧改进方向）
- Channel Attentive Self‑supervised Network（GDUT journal，2023）  
  研究问题：通道间信息未被充分利用是否限制了自监督单目深度估计的性能。  
  核心方法：在编码器插入 SE（Squeeze‑and‑Excitation）模块，并在解码器设计多尺度融合的通道注意力密集连接（CADC），以在通道维度上重校准与融合特征。  
  关键结论：在 KITTI 的对比与消融实验表明，通道注意力能改善边界细节还原与总体 AbsRel/SqRel 指标，且计算开销小于大幅增深网络的替代方案。[html.rhhz.net](https://html.rhhz.net/GDGYDXXB/html/1680831667538-1432911339.htm)

- Direction‑aware Cumulative（ICCV 2023 相关工作）  
  研究问题：方向/连接区域（object–ground connection）信息在深度估计中被低估，如何把方向性采样融入卷积以获得更合适的接地线线索。  
  核心方法：提出方向感知模块（可学习仿射变换 + 方向化采样）与累计（cumulative）卷积来强调连接区域的信息，并在解码器结合方向特征。  
  关键结论：在室内/室外基准上方向感知模块对物体底部/接地轮廓的深度恢复有显著改善；该思路提示对卷积采样策略的小改动能带来方向性线索的增益。（相关介绍与讨论见 ICCV23 摘要/复现说明）[blog.csdn.net](https://blog.csdn.net/weixin_43559672/article/details/136353717)

F. 室内场景专用与局部特征引导（2025）
- LoFtDepth — 局部特征引导的室内自监督深度估计（CRAD/2025）  
  研究问题：室内场景（狭小空间、频繁位姿变化）下自监督方法如何利用结构化先验和局部边界特征提升精度。  
  核心方法：用预训练深度估计器生成结构化深度先验，从中提取局部边界特征作为蒸馏目标；引入逆自动掩模加权的表面法线损失与相机位姿残差一致性约束以适应室内运动特性。  
  关键结论：在主要室内数据集上，该训练范式能把相对误差（AbsRel）下降到更低水平并改善无纹理区域的法线一致性，表明“先验＋局部蒸馏＋几何一致性”是室内自监督的有效方向。[crad.ict.ac.cn](https://crad.ict.ac.cn/article/doi/10.7544/issn1000-1239.202440951)

实验与评价总结（跨论文共性结论）  
1) 数据多样性与伪标注质量是关键。将大量异构未标注图像转为伪标签后直接混训练，收益有限；但配合（a）对未标注样本的强扰动以构造“更难的优化目标”、和（b）来自语义/特征先验的对齐/正则化，能够有效提升 zero‑shot 泛化与微调后度量性能（见 Depth Anything 等）。  
2) 多帧/多视角的几何线索显著提升静态场景精度，但在动态物体、遮挡与无纹理区易出错；成功的多帧方法通常引入单帧先验、可靠性掩码或教师‑学生纠正机制来修正有毒代价体（见 ManyDepth、M2Depth 与多尺度特征增强工作）。  
3) 模型架构趋势：大核注意力 / ViT 元素与局部 CNN 的混合在捕获长程上下文与边界细节间取得折中，但带来更高计算开销；因此轻量化的重参数化与自蒸馏成为重要设计点（HCVNet、Act‑VAN 等）。  
4) 不确定性量化与集成（snapshot／siam）在边界/细长物体和移动物体处对性能改进有明确作用；实用系统往往把不确定性用于训练加权与推理后处理。  
5) 鲁棒性研究开始从对抗样本扩展到物理世界攻击（光照、贴纸），自监督对抗训练能在不依赖真深度标签的条件下提升鲁棒性，但仍需评估对正常（非攻击）情况下性能的负面影响。  
6) 常用评估仍以 AbsRel、SqRel、RMSE、RMSElog 与 δ<1.25/1.252/1.253 等指标为主，但越来越多工作同时报告零样本泛化、边界视觉质量与鲁棒性（对抗/物理）实验。

趋势与挑战（2025年前后可预见）  
1) 半监督范式将以“伪标注 + 强扰动 + 特征对齐”为标准实践。Depth Anything 的经验表明：简单大量伪标注本身效果有限，但结合面向泛化的扰动与从大语义模型（DINOv2/SAM/DINOv2‑style）迁移连续特征会成为提升零样本与下游微调性能的常用套路。  
2) 多摄像头与跨时间的空间—时间代价体将成为自动驾驶等需要度量深度场景的主流路线。未来工作会更强调代价体的动态可信度评估（learned masking）、以及与语义/实例先验的协同（M2Depth 展示了初步方向）。  
3) 鲁棒性与安全性的评测成为常规基线：物理攻击、天气/光照域移、现实世界遮挡将被标准化为评测项，更多自监督对抗训练（含 L0 稀疏扰动、物理逼真变换）与不确定性驱动的风险控制策略会出现。  
4) 架构上的轻量化 Transformer/CNN 混合与知识蒸馏（含自蒸馏）将并行发展，以在边缘部署场景兼顾长程依赖、细节恢复与低延迟推理（即保持 ViT 的语义优势同时压缩计算）。  
5) 评测与数据集走向更强调“多任务初始化”：预训练的深度估计编码器会被期待同时作为语义分割/场景理解的通用中级编码器（Depth Anything 已展示该潜力），所以跨任务特征对齐损失与联合微调协议会受到更多关注。  
6) 基于不确定性的训练—推理闭环（uncertainty‑aware loss weighting + post‑hoc ensemble/predictive filtering）会进一步成熟，成为增强边界精度和避免灾难性错误（例如深度位错导致的规划风险）的标准手段。

结论  
近三年（含 2024–2025）的研究表明：提升自/半监督深度估计的有效路径不是单一地扩张网络或单靠伪标签数量，而是把数据（尤其是未标注）的多样性、对未标注样本的鲁棒化（强扰动）、以及从大型语义/视觉先验中迁移连续特征三者结合起来；同时，多帧与多摄像头几何仍是获取尺度与精度的核心机制，但必须与可靠性估计与单帧先验共同使用以处理动态与无纹理挑战。未来研究需在“泛化—鲁棒—效率”三者之间寻找可行的工程化折中，并推进更标准化的鲁棒性与零样本评测协议。

参考文献（选择性列举，均可在各自主页/期刊检索）  
- Yuan‑Zhen Li et al., “Self‑Supervised Monocular Depth Estimation by Digging into Uncertainty Quantification” (JCST, 2023). [jcst.ict.ac.cn](https://jcst.ict.ac.cn/cn/article/doi/10.1007/s11390-023-3088-y)  
- Qiqi Kou et al., “Coordinate‑aware attention‑based multi‑frame self‑supervised monocular depth estimation” (2023). [yhztjs.spacejournal.cn](https://yhztjs.spacejournal.cn/article/doi/10.13700/j.bh.1001-5965.2023.0417)  
- Qiqi Kou, Weichen Wang, et al., “Multi‑frame self‑supervised monocular depth estimation with multi‑scale feature enhancement” (Optics and Precision Engineering, 2024). [opticsjournal.net](https://www.opticsjournal.net/Articles/OJa00c675cd4311d5f/FullText)  
- “M2Depth: Self‑supervised Two‑Frame Multi‑camera Metric Depth Estimation” (2024 preprint / project page). [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/f0316ba8-fa2c-4e7d-833b-390e3cbe0531)  
- Zhiyuan Cheng et al., “Self‑supervised Adversarial Training of Monocular Depth Estimation against Physical‑World Attacks” (2024). [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/ee0c8799-c366-43fa-845c-737990abb745)  
- Qianhui Zheng & Lingjun Kong, “Hybrid CNN and ViT for Self‑Supervised Knowledge Distillation Monocular Depth Estimation Method (HCVNet)” (Modeling & Simulation, 2024). [image.hanspub.org](https://image.hanspub.org/html/80-2571621_87686.htm)  
- Jun‑xian Wu & Yuan‑lie He, “Channel Attentive Self‑supervised Network for Monocular Depth Estimation” (Journal of Guangdong University of Technology, 2023). [html.rhhz.net](https://html.rhhz.net/GDGYDXXB/html/1680831667538-1432911339.htm)  
- “Depth Anything: Unleashing the Power of Large‑Scale Unlabeled Data” (Depth Anything — arXiv / CVPR2024 work; 预印与实现讨论见技术博客与论文页面). 相关综述/实现参见作者 arXiv 及社区复现资料和博客（示例）[blog.csdn.net](https://blog.csdn.net/weixin_43559672/article/details/136353717)  
- Ai Haojun et al., “Improving Self‑Supervised Monocular Indoor Depth Estimation with Local Feature Guidance (LoFtDepth)” (CRAD, 2025). [crad.ict.ac.cn](https://crad.ict.ac.cn/article/doi/10.7544/issn1000-1239.202440951)  
- Watson et al., “The Temporal Opportunist: Self‑Supervised Multi‑Frame Monocular Depth” / ManyDepth line (CVPR 2021) — 多帧自监督基线（请检索 CVPR2021 文献与实现）。  
- Godard et al., “Digging into Self‑Supervised Monocular Depth Estimation” (ICCV 2019) — Monodepth2 基线（可检索 ICCV2019 论文）。  
- Liu et al., “Learning to Upsample by Learning to Sample (DySample)” (ICCV 2023) — 动态上采样方法，为多帧解码器重建细节提供参考（被多篇 2024 工作采用/引用）。  

（注：文中引用的中文期刊/会议页与预印本均可通过给出的域名检索到原文或期刊页面；若需我可为上述每篇论文提供精确 DOI / arXiv 链接与关键实验数值表格以便复现与比较。）