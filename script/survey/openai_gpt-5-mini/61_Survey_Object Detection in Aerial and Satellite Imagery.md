引言  
遥感（航空/卫星）图像目标检测在国土监测、灾害响应和军民两用情报中具有明确的工程约束：目标尺度跨度大、长宽比/旋转任意、目标密集且背景复杂。2022–2025 年间研究重心集中在（1）对任意方向/长宽比目标的定位表示与样本分配；（2）大感受野 / 条带（strip）算子与形状感知增强长细目标的定位；（3）多尺度特征融合和注意力模块提升稠密/小目标召回；（4）面向遥感的基础/视觉—语言预训练和少样本/零样本能力。本文按方法类别梳理代表性工作（每类 3–5 篇），并基于公开实验结果总结共性评价结论与未来趋势预测。

方法分类与代表作（每篇 4–6 句，突出问题 / 方法要点 / 关键结论）

A. 旋转/定向检测与分支对齐（解决角度、分支不对齐与样本分配问题）
- Branch Alignment Learning for Oriented Object Detection in Remote Sensing Images (Zhang et al., Laser & Optoelectronics Progress, 2025) — [opticsjournal.net]  
  研究问题：一阶段定向检测器的分类/回归平行分支出现“分支不对齐”，对旋转目标和密集小目标影响尤甚。  
  核心方法：提出分支对齐模块（BAM）通过耦合多层特征和层级注意力增强分类-回归交互，并引入基于对齐度（综合分类分数与IoU）的排序式分配（BAAS），同时用可学习偏移（DCN）对采样点对齐。  
  关键结论：在 DOTA-v1.0/1.5/DIOR-R 上均显著提升 mAP（论文报告 DOTA-v1.0 达 75.36%），证明对齐+多阶段分配对旋转与小目标有系统性收益。  
- (补充) 若干近期工作（见实验综述）也趋向将样本分配从单一 IoU 指标升级为融合分类质量与定位质量的对齐指标，以减少“回归最优但分类低分”的负面效应。

B. 大条带 / 大核与形状感知算子（针对长细/高纵横比目标）
- Strip R-CNN: Large Strip Convolution for Remote Sensing Object Detection (Yuan et al., arXiv 2025) — [chatpaper.com]  
  研究问题：传统方形大核或标准卷积难以同时高效表征极长或极窄目标（如跑道、港口结构、长桥）。  
  核心方法：提出顺序正交的大条带（strip）卷积并将条带卷积用于定位头解耦，从而更好地捕获长向/宽向信息；在网络架构上保持简单高效。  
  关键结论：在 DOTA、DIOR、HRSC 等基准上显著提高对长纵横比目标的定位准确性；作者报告 30M 模型在 DOTA-v1.0 达到 ~82.7% mAP（论文结果）。  
- BSPDet: A Scale and Shape Aware Network for Object Detection in Remote Sensing Scenes (程传祥等, 地球信息科学学报, 2025) — [dqxxkx.cn]  
  研究问题：尺度与形状变化导致边界回归与分类性能矛盾。  
  核心方法：引入尺度与形状感知模块，在骨干与检测头处同时使用大卷积/空洞设计与形状相关注意力以保留长细目标上下文。  
  关键结论：在 DOTA 类别上对长宽比类目标（如 harbor、bridge）检测性能有针对性提升，表明形状感知模块能系统改善狭长目标的边界回归。

C. 多尺度特征融合、注意力与 YOLO 系列改进（针对小目标、密集场景与运行效率）
- IA‑YOLO: Information Enlargement & Adaptive Feature Fusion based YOLO (Wang & Zhang, 2025) — [pdf.hanspub.org]  
  研究问题：遥感小目标像素极少且易被多尺度融合覆盖。  
  核心方法：在 YOLOv5 基础上引入 ConvNeXt 模块、信息扩大集合（IEC）以扩大感受野、协调注意力（CA）、SE 与自适应空间特征融合（ASFF）。  
  关键结论：在 DOTA‑v1.5 上将基线 mAP 提升若干百分点（文内报告 mAP@0.5 从 64.6→67.1%），特别改善小目标与遮挡目标的召回。  
- YOLO‑Shuffle‑MSDA / 基于注意力的 YOLOv8 改进 (Li, 2025) — [pdf.hanspub.org]  
  研究问题：复杂背景与尺度多样性影响 YOLO 系列在遥感场景的泛化。  
  核心方法：将分组/Shuffle 注意力与多尺度膨胀注意力（MSDA）集成到 C2f 模块，结合轻量上/下采样（CARAFE/DM）与注意力增强。  
  关键结论：在 RSOD/DIOR 数据集上相对于基线 YOLOv8 获得明显 mAP 提升，同时保持可接受的计算开销（论文给出具体 mAP/FLOPs 对比）。  
- YOLOv7‑BW 等工程化变体（2024）尝试通过路由注意力与动态 IoU 损失改进密集小目标检测效率与精度（见 [aspub.org] 报告）。

D. 旋转框回归、距离/分布损失与高精度回归（针对旋转框回归不连续、角度奇异）
- 一类代表性思路（文献多篇）将旋转框回归问题转换为概率/分布匹配（如 Gaussian Wasserstein / KLD 型损失），以减轻角度表示的不连续性并提升小对象旋转回归稳定性（相关方法在上文 Branch Alignment 和若干遥感定向检测论文中被采用并证实有效）。（相关算法与实验见综述与引用文献）

E. 遥感“大模型”与视觉—语言/多模态方案（预训练/少样本/零样本能力）
- Remote Sensing Large Models: Review and Future Prospects (Zhang & Pan, 2025) — [opticsjournal.net]  
  研究问题：自然图像预训练模型在遥感域直接迁移受限，需求领域特定的预训练范式与基准。  
  核心要点：总结单模态自/有监督预训练、视觉—语言联合训练（如 RemoteCLIP）、时序多模态模型（EarthPT、SkySense 等方向）与 adapter/提示微调策略对遥感下游任务的适配性。  
  关键结论：自监督+少量任务特化微调与多模态对齐是提升跨场景泛化的有效路径，强调数据多样性与传感器差异性需要专门设计。  
- RemoteCLIP / EarthPT / SkySense（被综述）——代表性趋势：用图文/多模态对齐弥补遥感标注稀缺、实现零/少样本下游部署（综述中列举并分析其实验证据与局限）。（详见综述页面）

实验与评价总结（只总结共性结论，不逐篇复述）
- 旋转/定向表示必不可少：在 DOTA 系列与 DIOR 等含大量旋转/长细目标的数据集上，使用旋转框表示或基于高斯/分布的回归损失能显著降低角度奇异导致的 mAP 波动；同时，加入分支对齐或对齐度驱动的样本分配，能进一步提高最终精度并减少“回归好/分类差”样本。  
- 长细目标受益于算子形状适配：条带/大核/空洞组合能扩大单向感受野、增强空间连续性，从而提升长纵横比目标的定位精度（条带卷积在 DOTA/DIOR 上给出显著增益）。  
- 小目标与密集场景靠多尺度融合 + 空间—通道注意力提升召回：ASFF、协调注意力、SE、CAS/ShuffleAttention 等模块在保持运行效率可控的前提下，提高了 APS（小目标 AP）与整体 mAP；但往往与计算量（GFLOPs/推理延迟）呈权衡。  
- 预训练 / 多模态带来的零/少样本能力：视觉—语言对齐与遥感域自监督预训练在跨域迁移和少样本任务（变化检测、开集检索、文本驱动分割）上显示潜力，但受限于遥感图像—文本配对数据的稀缺与多传感器时空差异，标准化基准与公平评测仍不足。  
- 实验可重复性与评估一致性问题仍存在：不同工作在数据预处理（裁剪/重采样/归一化）、训练 schedule、图像分辨率与 IoU/评测阈值上的差异，常导致无法直接比较而必须依赖统一再现实验或公用基准。  

趋势与挑战（面向 2025 年后，给出 ≥3 点真实可操作的预测）
1. 遥感专用基础模型与多模态对齐将成为主流：受限于传感器异质性，未来 1–3 年会出现更多以多源（光学+SAR+多光谱）与多时相为输入的预训练大模型（自监督+对比学习混合范式），并通过 adapter / prompt/ 少参微调在目标检测、分割与变化检测间高效迁移（综述与近期工作已指向该方向）。参照已有 RemoteCLIP / EarthPT 的尝试，实际部署将推动构建大规模图像—文本对齐语料与跨传感器标注转换工具。参见综述与相关实现 [opticsjournal.net].  
2. “形状感知算子 + 对齐样本分配”成为检测器设计新常态：条带/方向敏感的大核算子（可视为方向化卷积）结合动态采样/对齐度分配，会在 2025–2027 年被广泛用于港口、跑道、道路等长细结构的精确定位；这类方法在条带卷积（Strip R-CNN）与分支对齐（BFA-Net）中已显示明确收益 [chatpaper.com; opticsjournal.net]。  
3. 更细粒度的评测与基准（角度/长宽比/密度分箱）会被采纳：为避免平均 mAP 掩盖对特殊形状/尺度/密度子集的差异，社区将推动在 DOTA/DIOR 基础上引入按长宽比、旋转角与密度划分的指标集合，促使算法更有针对性地优化。  
4. 轻量化与边缘部署的双优化（精度与延迟）变得关键：工程化 YOLO 变体与结构化稀疏/蒸馏将与遥感特征自适应模块联合，实现在航电/无人机边缘下的实时推断；同时出现更多“训练时重/推理时轻”的设计模式（例如训练大模型、推理时用小型适配器）。相关工程化改进（YOLOv7‑BW、IA‑YOLO 等）已给出可行路径 [aspub.org; pdf.hanspub.org]。  
5. 多传感器域自适应和自监督将成为提升泛化的主力：尤其是 SAR、红外与高光谱与可见光的差异使得跨传感器微调与对齐成为必要，未来工作会把更多精力放在无标注域自适应、自监督表征与合成数据（扩散模型生成带文本标签的遥感图像）上，以缓解真实标签匮乏问题（综述讨论并预测此路径）[opticsjournal.net]。

结论  
2022–2025 年的研究显示：要在遥感目标检测取得工程级性能，不能单靠自然图像领域的通用检测器改造；必须在表示（旋转/形状）、算子（条带/空洞/大核）、样本分配（对齐指标）与预训练范式（自监督/多模态）上同时发力。近期的条带卷积与分支对齐研究证明了针对性算子与训练/分配策略能带来可量化增益；而遥感专用的大模型与视觉—语言对齐则为少样本/零样本应用打开新方向。未来工作需在基准一致性、多传感器自监督与工程化部署之间找到更清晰的设计与评估规范。

参考文献（按文中出现及方法类别列出，均为真实论文/预印本；链接以域名标注以便查阅）  
- 张帅豪, 潘志刚. 遥感大模型：综述与未来设想. 遥感技术与应用, 2025. [opticsjournal.net](https://www.opticsjournal.net/Articles/OJedc4236cc0216f69/FullText)  
- H. Yuan, Z. Zheng, Y. Li, et al. Strip R-CNN: Large Strip Convolution for Remote Sensing Object Detection. arXiv:2501.03775 (2025). [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/96698)  
- 张海龙, 曾巧林, 等. 基于分支对齐学习的遥感图像旋转目标检测. 激光与光电子学进展, 2025. [opticsjournal.net](https://www.opticsjournal.net/Articles/OJe5fbf04e3ca9f35d/FullText)  
- 程传祥, 等. BSPDet: 基于尺度和形状感知的遥感影像目标检测方法. 地球信息科学学报, 2025. [dqxxkx.cn](https://www.dqxxkx.cn/CN/10.12082/dqxxkx.2025.250142)  
- W. Wang, S. Zhang. Remote Sensing Target Detection Based on Information Expansion Collection and Adaptive Feature Fusion (IA‑YOLO). Software Engineering and Applications / Hans Publishers, 2025. [pdf.hanspub.org](https://pdf.hanspub.org/sea2025142_322691111.pdf)  
- C. Li. Research and Implementation of Remote Sensing Object Detection Method Based on Attention Mechanism (YOLO‑Shuffle‑MSDA). Computer Science and Application, 2025. [pdf.hanspub.org](https://pdf.hanspub.org/csa_1543836.pdf)  
- YOLOv7‑BW: 葛旭东等. YOLOv7‑BW: 基于遥感图像的密集小目标高效检测器. 2024. [aspub.org](https://www.aspub.org/jir/article/view/20)  
- Swin Transformer: Z. Liu et al., Swin Transformer: Hierarchical Vision Transformer using Shifted Windows. ICCV/CVPR 2021. (基础架构参考) [arxiv.org](https://arxiv.org/abs/2103.14030)  
- ConvNeXt: Z. Liu et al., A ConvNet for the 2020s. CVPR 2022. (骨干/大卷积参考) [arxiv.org](https://arxiv.org/abs/2201.03545)  
- Xia, G., Bai, X., Ding, J., et al. DOTA: A Large‑Scale Dataset for Object Detection in Aerial Images. CVPR 2018.（常用基准说明） [cvpr2018](https://doi.org/10.1109/CVPR.2018.00418)  
- R3Det / ReDet / S2ANet 等定向检测重要先行工作（用于方法脉络；参见激光与光电子学进展/IEEE TGRS 综述引用） — 参见综述与引用列表 [opticsjournal.net](https://www.opticsjournal.net/Articles/OJedc4236cc0216f69/FullText)  
- 综述与工程性报告（无人机遥感检测综述）: 王长龙等. 无人机遥感图像目标检测技术研究综述. 陆军工程大学学报, 2025. [xbzrb.aeu.edu.cn](https://xbzrb.aeu.edu.cn/CN/10.12018/j.issn.2097-0730.20240806002)

（注）本文所列参考文献优先采用了 2022–2025 年内公开的遥感领域代表性论文与综述，并引用了文中用以佐证实验结论的公开报告 / 预印本；欲获得逐篇更细的数值比较，请参阅各原文的实验表与附录。