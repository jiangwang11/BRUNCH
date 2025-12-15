引言  
医学图像分割是影像驱动诊疗（放疗靶区勾画、术前规划、病灶定量随访等）的核心技术。近年来（尤其在 2022–2025 年），研究重心从单一卷积网络向 Transformer/混合架构、提示/基础模型（foundation models）适配、多模态/实例分割与轻量化/自动化流水线并行推进。下文按方法类别精选代表性工作并给出要点式解读（每篇 4–6 句，突出问题、方法与关键实验结论），随后总结实验与评价的共性结论，指出面向 2025 年前后的主要趋势与挑战，并列出参考文献（均为公开论文或可查资料/预印本）。

方法分类与代表作
一、基于 CNN 的“可部署/自动化”基线与改进（选 3 篇）
- nnU-Net（自配置框架，代表性基线）  
  说明：nnU-Net 将“网络+训练+后处理”作为自动化流水线，通过数据驱动的超参数与预处理规范化实现对多种医学分割任务的强稳基线；它不是单一新架构而是可复制的自动配置策略，成为多个后续工作对比的默认基准。关键结论：在多器官/肿瘤分割基准（如 AMOS、LiTS、BraTS）上，nnU-Net 的一键复现能力和稳健性常常超过手工调参的专用模型，因而推动了后续模型评估的“基线规范化”。（基础文献与综述可见综述与工具文献）[cjig.cn](https://www.cjig.cn/zh/article/doi/10.11834/jig.240467/)。

- MPUNet（多尺度特征增强 + 池化注意力，皮肤镜分割，2025）  
  说明：针对皮肤镜图像中毛发、血管干扰与边界模糊问题，MPUNet 在 U‑Net 骨干中引入 MS‑Module（按高度/宽度方向分解并用多核卷积提取多尺度局部特征）和 PL‑Module（池化驱动的通道选择与全局注意力）以先抑噪再精修边界。关键结论：在 ISIC2017/2018 与 PH2 三个数据集上，MPUNet 在 Dice 与 mIoU 上相较多种专用与通用方法显著提升（PH2 Dice≈95.2%，ISIC2018 mIoU≈83.5%），表明“先全局抑噪再局部细化”对真实皮损图像有效。[jcad.cn (PDF)](https://www.jcad.cn/cn/article/pdf/preview/10.3724/SP.J.1089.2025-00222.pdf)。

- UCM‑NetV2 / 轻量化工程（代表性轻量方法）  
  说明：为满足临床部署与便携设备需求，近年多工作提出轻量化变体（如 UCM‑NetV2 等），通过通道/算子重参数化与深度可分离卷积在保持精度的同时显著降低 FLOPs 与延迟。关键结论：在皮肤病任务中，轻量化模型在移动/嵌入式场景实现实时分割（延迟与内存占用明显下降），但需在多中心数据上验证泛化性（相关比较见 MPUNet 的对比表）。（见 MPUNet 及相关综述）[jcad.cn](https://www.jcad.cn/cn/article/pdf/preview/10.3724/SP.J.1089.2025-00222.pdf)。

二、Transformer 与混合 CNN–Transformer 架构（选 3 篇）
- TransUNet（Transformer 作编码器强化全局上下文，2021 → 2022–2025 被广泛引用）  
  说明：TransUNet 将 Vision Transformer 作为编码器以补偿 CNN 感受野受限问题，同时保留 U‑Net 的逐层解码和跳跃连接，解决多尺度语义融合；研究问题在于如何把 Transformer 的全局建模和 CNN 局部细节互补。关键结论：在多器官和小体积器官分割上，TransUNet 在若干基准上相较纯 CNN 有 1–3 个百分点的 Dice 提升，但对训练数据量和计算资源更敏感（详见综述与对比）[cjig.cn](https://www.cjig.cn/zh/article/doi/10.11834/jig.240467/)。

- Swin‑UNet / Swin‑UNETR（层次化窗口注意力，2022）  
  说明：Swin Transformer（层次化、窗口化自注意力）被嵌入 U‑Net 结构（Swin‑UNet）或用于 3D‑volumetric（Swin‑UNETR），以更高效地建模远程依赖与多尺度特征。关键结论：在多器官/腹部分割（如 Synapse / BTCV）上，Swin 系列在平均 Dice 与边界（HD95）上优于同规模 CNN，且在保持计算可控的情况下改善了全局上下文对小器官的感知（参考改进工作与 2025 年的 SwinUNet 改进）。改进型 SwinUNet（2025）通过引入 Focal Transformer、ASPP 与 Tokenized Interaction Fusion，在 Synapse 数据集上将平均 DSC 与 HD95 分别优化到约 79.5 和 19.7（较基线有可观提升）。[opticsjournal.net](https://www.opticsjournal.net/Articles/OJ2b2078a8cf027f69/km)、[pdf.hanspub.org](https://pdf.hanspub.org/csa_1543783.pdf)。

- 改进/混合策略的普遍设计要点（综述式结论）  
  说明：近年高效改进集中于（1）局部–全局融合模块（Token/ASPP/Focal）；（2）跳跃连接的语义对齐（tokenized fusion）；（3）在瓶颈层加入多尺度上下文聚合以改善边界刻画。关键结论：这些结构在腹部多器官、胰腺等难分割器官上较单纯 Transformer 或单纯 CNN 均有稳定收益（参见改进 SwinUNet 消融结果）[pdf.hanspub.org](https://pdf.hanspub.org/csa_1543783.pdf)。

三、基础模型（foundation models）与 Promptable / SAM‑类方法（选 3–4 篇）
- Segment Anything Model (SAM) 在医学图像领域的应用与评估（综述，2024）  
  说明：SAM（自然图像大模型）引入“可提示”分割范式（点/框/文本），在医学图像上零样本/少样本应用被广泛评估；研究问题为：如何将以自然图像为主训练的 SAM 适配到灰度、模糊边界、模态多样的医学图像。关键结论：未经微调的 SAM 在某些医学模态（内窥镜、病理 WSI）能取得良好辅助效果，但在 CT/MRI/超声等灰度模态上普遍落后于专用模型；因此产生了大量“微调/适配/自动提示/伪标签”方向的后续工作。[opticsjournal.net (SAM 在医学应用综述)](https://www.opticsjournal.net/Articles/OJda3bfaa1dd74a3a/FullText)。

- MedSAM / SAM‑Med2D / MedSAM2（将 SAM 微调或扩展到医疗大域，2023–2025）  
  说明：为解决 SAM 在医学模态分布不匹配的问题，研究者通过（1）在大规模医学掩码对上微调（MedSAM、SAM‑Med2D）；（2）半监督结合（生成伪标签）与提示自动化（AutoSAM、EviPrompt）；（3）将 SAM 扩展至 3D（3DSAM‑adapter / SAM3D）等手段进行适配。关键结论：MedSAM/相关工作在广泛的医学数据集上（CT、MRI、内窥镜、病理）显著缩小与专用模型的差距并提升泛化；例如较大规模微调的 MedSAM2 报告在多器官、多模态上的泛化提升以及在人机协作标注流程中能将人工成本下调（BAAI 社区总结指出标注成本可降 >85% 的实验结论）。但完全替代专用模型仍需更大范围验证与规范化评价。[hub.baai.ac.cn（MedSAM2 概览）](https://hub.baai.ac.cn/paper/279a8711-cf36-4ca8-b9c9-1f7c35eec72e)、[opticsjournal.net（SAM 医学综述）](https://www.opticsjournal.net/Articles/OJda3bfaa1dd74a3a/FullText)。

- 3D 适配与自动提示（代表性尝试）  
  说明：3D 体控（CT/MRI）分割的做法分为两类：直接在 3D 数据上改造/重训练（SAM‑Med3D / SAM‑Med3D 风格工作），或采用滑窗/切片+切片间后处理（Slide‑SAM / SAM3D adapter）。关键结论：基于提示的 2D → 3D 迁移（加 adapter 或滑动窗口）在参数高效性与三维空间一致性之间取得实用折中，在多器官 CT 的无提示或弱提示条件下展示出与 nnU‑Net 等传统强基线可比的性能提升（参见 SAM 综述与 3D adapter 报告）。[opticsjournal.net](https://www.opticsjournal.net/Articles/OJda3bfaa1dd74a3a/FullText)。

四、多模态与实例分割 / 新范式（选 3 篇）
- VMDC‑Unet（VMamba + CNN 混合，病理切片/病理分割，2025）  
  说明：提出将视觉状态空间模型 VMamba 与 CNN（ConvNeXt 变体）混合，利用 VMamba 低复杂度建模长程依赖的优点与 CNN 的局部细节建模相结合，解决病理切片中长程组织关系与细粒度结构并存的问题。关键结论：在 SJTU_GSFPH 与 GLAS 等病理数据集上，VMDC‑Unet 在 MIOU/Dice 与 HD95 上均优于纯 Transformer 或纯 CNN 的竞品，且在 FLOPs 与参数-效率上取得较好折中（详见 Hanspub 报道及表格）。[pdf.hanspub.org](https://www.hanspub.org/journal/paperinformation?paperid=112526)。

- MSP‑YOLACT（多模态 PET/CT 实例分割，2025）  
  说明：针对 PET/CT 多模态的肿瘤实例分割，MSP‑YOLACT 在单阶段实例分割框架（YOLACT）基础上引入多模态特征混合器、增强特征金字塔与并行预测头以兼顾检测与掩码质量。关键结论：在作者的临床多模态肺肿瘤数据集上，MSP‑YOLACT 在 APdet/APseg 与 mAP 指标上明显优于单模态基线（报告 mAPseg≈65% 的实验值），表明专门设计的多模态交互模块可提升实例级位置与边界精度。[opticsjournal.net (MSP‑YOLACT)](https://www.opticsjournal.net/Articles/OJec7c2770705b1731/FullText)。

- 多尺度/ASPP / TIF 等边界增强模块（代表性工程实践）  
  说明：多个 2024–2025 年工作（改进 SwinUNet、Swin‑UNETR 的 ASPP / TIF / Focal modules 等）共同指出：在瓶颈层或跳跃连接处加入多尺度上下文（ASPP）和跨层 token 交互可以显著降低边界误差（HD95），尤其对胰腺、胰腺肿瘤及小器官有效。[pdf.hanspub.org](https://pdf.hanspub.org/csa_1543783.pdf)。

实验与评价总结（仅总结共性结论）
1) 评价协议与基线规范化：nnU‑Net 与统一的多数据集评估（如 Medical Segmentation Decathlon、Synapse、LiTS、AMOS、BRATS 等）继续作为可信基线；研究者越来越重视多中心/多协议验证而非单一数据集指标。2) 全局建模对小器官/小病灶重要：Transformer/状态空间/VMamba 等能有效提高小体积目标的检出与上下文一致性，但需配合局部细节模块（卷积或专用边界模块）以保证边界精细度。3) 提示式/基础模型的增益在“数据稀缺+人机协同”场景最明显：大规模微调后的 SAM 类模型在伪标签生成与交互式标注加速方面贡献最大，但要实现与专用监督模型的全面替代仍需更大规模医疗数据与任务特定适配。4) 多模态与实例分割：为检测 + 掩码质量联合优化而设计的多模态融合器（像 MSP‑YOLACT）能在实例级任务上改进 AP 与 AR；但多模态配准与配对数据的可获得性仍是瓶颈。5) 部署与效率权衡：轻量化/重参数化方法（DeConv/重参数化、深度可分离卷积、LoRA/Adapter 微调）成为生产化路线，能在近似精度下显著降低推理成本。

趋势与挑战（面向 2025 年前后，至少 3 点）
1) 医学基础视觉模型的落地化（foundation → clinic）：预计更多基于大规模医学掩码对的“Med‑foundation”模型（覆盖 CT/MRI/US/WSI 多模态）将出现，重点在于 PEFT（adapter/LoRA）与提示自动化以降低临床微调成本；但这需要统一的跨机构数据治理与标注规范以保证泛化。参见 MedSAM/MedSAM2 的路线与用户研究报告。[hub.baai.ac.cn](https://hub.baai.ac.cn/paper/279a8711-cf36-4ca8-b9c9-1f7c35eec72e)、[opticsjournal.net](https://www.opticsjournal.net/Articles/OJda3bfaa1dd74a3a/FullText)。

2) 异构融合（3D + 多模态 + 时间/视频）成为常态任务：仅 2D 静态分割已不足以支持放疗/手术导航/超声实时引导，未来方法需本质上支持 3D 空间一致性与多时相（视频）信息的联合建模；3D adapter、Slide‑SAM、SAM3D 等尝试说明了可行方向，但对计算与标注成本提出挑战。[opticsjournal.net](https://www.opticsjournal.net/Articles/OJda3bfaa1dd74a3a/FullText)。

3) 半监督/主动学习 + 大模型结合：由于标注稀缺，半监督框架（Mean Teacher、伪标签+质量筛选）与 SAM 生成的高质量提示/伪标签结合将成为主流，以最小人工成本获得高质量训练集并持续在线微调（人机闭环）。相关工作（SemiSAM、ASLseg 等）已证明伪标签质量对下游提升的决定性作用。[opticsjournal.net](https://www.opticsjournal.net/Articles/OJda3bfaa1dd74a3a/FullText)。

4) 可解释性与不确定性量化进入临床路径：临床接受度要求模型输出不只是掩码，还要提供不确定性估计与可解释证据（热图、不确定区域提示、版本可追溯）；SAM‑U 与 UR‑SAM 之类工作开始探索利用多提示与不确定性校正提升可靠性。5) 标准化 Benchmark 与评估协议的扩展：传统以 Dice 为主的评估不足以反映临床可用性（边界精度、操作时间、审阅负担、回溯性），未来需将“人工修正所需时间/成本”“跨机构一致性”“推理延迟”等指标纳入评价体系（MedSAM2 的用户研究即为示例参考）。[hub.baai.ac.cn](https://hub.baai.ac.cn/paper/279a8711-cf36-4ca8-b9c9-1f7c35eec72e)。

结论  
2022–2025 年间，医学图像分割研究呈现“多范式并进”的格局：Transformer 与混合架构提升了全局语义感知、基础模型（SAM 系列）在数据稀缺与标注加速场景展现出巨大潜力、多模态与实例分割方法推动任务从语义级向实例级与多模态临床场景对接、而轻量化与自动化（nnU‑Net 风格流水线、PEFT）则为部署可行性提供工程路径。未来五年，能否把基础模型安全、合规、跨院商用化并与半监督/主动学习形成闭环，将决定医学图像分割技术在真实临床路径中的大规模落地速度。

参考文献（所列皆为可查资料/论文或公开综述；引用以提供的检索结果为主）  
1. 医学图像分割方法综述（2025）[cjig.cn](https://www.cjig.cn/zh/article/doi/10.11834/jig.240467/).  
2. MPUNet: Multi‑Scale Feature Enhancement and Pooling Attention Network for Skin Disease Segmentation (2025) — JCAD PDF. [jcad.cn](https://www.jcad.cn/cn/article/pdf/preview/10.3724/SP.J.1089.2025-00222.pdf).  
3. 从 U‑Net 到 Transformer：混合模型在医学图像分割中的应用进展（综述，2025）[opticsjournal.net](https://www.opticsjournal.net/Articles/OJ2b2078a8cf027f69/km).  
4. SwinUNet 改进与腹部多器官分割（改进型 SwinUNet，2025）[pdf.hanspub.org](https://pdf.hanspub.org/csa_1543783.pdf).  
5. 基于 VMamba‑CNN 混合的结直肠癌切片图像分割（VMDC‑Unet，2025）[hanspub.org](https://www.hanspub.org/journal/paperinformation?paperid=112526).  
6. MSP‑YOLACT：面向多模态 PET/CT 肺部肿瘤实例分割（2025）[opticsjournal.net](https://www.opticsjournal.net/Articles/OJec7c2770705b1731/FullText).  
7. SAM 在医学图像分割中的应用综述（2024）[opticsjournal.net](https://www.opticsjournal.net/Articles/OJda3bfaa1dd74a3a/FullText).  
8. MedSAM2 / MedSAM 系列工作概览（MedSAM2 用户研究与微调报道，2025）[hub.baai.ac.cn](https://hub.baai.ac.cn/paper/279a8711-cf36-4ca8-b9c9-1f7c35eec72e).  
9. nnU‑Net: self‑configuring method for biomedical segmentation（Isensee et al., Nature Methods / 被广泛引用的自动化基线，参见综述）[cjig.cn](https://www.cjig.cn/zh/article/doi/10.11834/jig.240467/).  
10. TransUNet: Transformers Make Strong Encoders for Medical Image Segmentation（TransUNet 原始/代表性引用，见综述与引用）[cjig.cn](https://www.cjig.cn/zh/article/doi/10.11834/jig.240467/)。  
11. Swin‑UNet / Swin‑UNETR（Swin Transformer 系列在医学分割的应用，参见 ECCV/ MICCAI 引用与综述）[opticsjournal.net](https://www.opticsjournal.net/Articles/OJ2b2078a8cf027f69/km)。  
12. 关于 SAM→3D 适配、自动提示与半监督结合的代表性工作与分析（见 SAM 综述与其中的 3DSAM‑adapter / AutoSAM / SemiSAM 讨论）[opticsjournal.net](https://www.opticsjournal.net/Articles/OJda3bfaa1dd74a3a/FullText)。  
13. 临床/工程实测与综述（CT 自动勾画与 AI 部署综述，2025）[pdf.hanspub.org](https://pdf.hanspub.org/acm_8104511.pdf).  
备注：上文所引用的各篇论文/综述与实验数据均基于公开论文、期刊/会议文章及权威社区汇总（所提供的检索结果与 PDF/页面），读者可按文末链接逐条查阅详细原文与数值。若需我把任一篇论文的具体段落/表格中的数值逐项摘录并给出原始页面截图或 DOI，请告知具体篇目，我将逐篇检索并补充。