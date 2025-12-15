引言  
开放词汇目标检测（Open-Vocabulary Object Detection, OVD）旨在使检测器超越训练集的固定类别、直接利用图文（或大模型）知识在零/少样本下识别任意文本描述的对象。自 2022 年以来，随着大规模图文预训练（特别是 CLIP 类模型）与区域级对齐、以及大语言模型（LLM）在视觉任务中作为监督或数据生成器的应用，OVD 已从“可识别新词汇”演进为兼顾实时性、开放世界未知物体发现与词汇动态扩展的实用系统。本文聚焦 2022–2025 年间在方法范式、可扩展训练策略和开放世界机制上具有代表性的工作，按方法类别归纳每类 3–5 篇关键论文（每篇 4–6 句），并在实验与评价、趋势与挑战中给出基于文献的综合结论与展望。

方法分类与代表作  
（说明：下列论文均为公开发表或 arXiv 预印，本段每篇 4–6 句，突出问题、核心方法与关键实验结论；引用使用检索到的报告/页面以便读者检索原文。）

A. 基于 YOLO / 实时架构的开放词汇预训练与部署  
- YOLO‑World: Real‑Time Open‑Vocabulary Object Detection (Cheng et al., CVPR2024) —（参见汇总）[hub.baai.ac.cn]  
  问题：在保持 YOLO 系列实时性的同时提升开放词汇零样本检测能力。  
  方法：将 CLIP 文本编码器与 YOLO 检测器结合，提出可重参数化的视觉语言路径聚合（RepVL‑PAN）与区域—文本对比预训练；采用“prompt‑then‑detect”的离线词表策略以加速推理。  
  实验结论：在 LVIS 零样本评测上展示强泛化（论文/汇总给出约 35.4 AP 并保持高帧率），并能迁移到实例分割与引用检测等下游任务，证明实时 OVD 可兼顾速度与开放词汇性能。[hub.baai.ac.cn]

- YOLO‑UniOW: Efficient Universal Open‑World Object Detection (arXiv 2412.20645; summary) —（参见汇总）[cloud.tencent.com.cn]  
  问题：统一开放词汇检测（OVD）与开放世界检测（OWOD），并在不依赖增量学习的前提下降低推理开销。  
  方法：基于 YOLOv10 提出自适应决策学习（AdaDL，使用 LoRA 在文本编码器投影层轻量校准）以替代早期层的跨模态融合，并提出“通配符学习”（wildcard）用于无监督检出未知物体与迭代词汇扩展。  
  实验结论：在 LVIS 等基准与若干 OWOD 数据集上取得有竞争力的 AP/未知召回折中指标，同时显著提升推理效率（文献汇总报告的数值如 34.6 AP 与高 FPS），展示了参数高效校准 + 通配符策略的可行性。[cloud.tencent.com.cn]

B. 区域级对齐 / 基于 VLM 的“接地”检测（Region ↔ Text）  
- Grounding DINO: Grounded Object Detection (IDEA‑Research, arXiv 2303.05499) —（参见文档）[opendeep.wiki]  
  问题：实现基于任意文本描述的区域级检测（grounded detection），以支持开放词汇和引用表达式检测。  
  方法：提出 Transformer‑based 多尺度跨模态架构，利用文本引导的查询与多尺度可变形注意力完成区域—文本对齐，设计针对性的损失与解码策略以稳定训练。  
  实验结论：在零样本和少样本下对任意文本（包括自然语言短语）表现出强检出与局部化能力，被广泛用于后续扩展（如集成 SAM、生成式交互等）[opendeep.wiki]。

- OVLW‑DETR: Open‑Vocabulary Light‑Weighted Detection Transformer (2024 report) —（参见汇总）[hub.baai.ac.cn]  
  问题：在保持 DETR 核心端到端优势的同时实现轻量化、开放词汇的检测器。  
  方法：用文本编码器的类嵌入替换或对齐检测器的固定分类层权重，设计端到端训练并减少额外跨模态融合模块，从而实现更小的计算开销。  
  实验结论：在零样本 LVIS 等基准上优于同预算的实时 OVD 方法，表明通过“替换分类权重 + 紧耦合对齐”可实现高效开放词汇迁移。[hub.baai.ac.cn]

C. 多源训练 / 通用检测与概率校准（扩大词汇量与开放世界泛化）  
- Detecting Everything in the Open World: Towards Universal Object Detection (UniDetector, CVPR2023) —（参见综述/报告）[csdn.net]  
  问题：如何利用多源异构标签空间训练，使检测器在开放世界中检测尽可能多的类别（通用检测）。  
  方法：提出分区训练结构以共享主干、隔离分类头；解耦建议（proposal）生成与 RoI 分类并提出类无关本地化网络（CLN）；采用概率校准缓解基类偏置。  
  实验结论：在多数据集混合训练下，对 LVIS / ImageNetBoxes / VisualGenome 等大词汇基准展示更好的零样本泛化——在诸多测试集上相较传统有监督基线实现实质性提升，证明“多源 + 解耦 + 校准”是扩展词汇量的有效路径。[csdn.net]

D. 大语言模型 (LLM) 监督 / 文本生成增强数据与描述蒸馏  
- LLMDet: Learning Strong Open‑Vocabulary Object Detectors under the Supervision of Large Language Models (CVPR2025 report) —（参见博文）[csdn.net]  
  问题：如何利用 LLM 生成的长/短文本描述来强化区域级与图像级语义信号，从而提升 OVD 的词汇理解与定位能力。  
  方法：构建 GroundingCap‑1M（图像 + 区域短语 + 图像级长描述），设计联合训练目标把标准定位损失与描述生成损失耦合；通过投影器将检测器视觉特征映射至 LLM 输入空间，进而用 LLM 生成/对齐监督。  
  实验结论：在用 LLM 生成的丰富描述监督下，检测器在开放词汇任务上取得明显提升；同时该方法能反向促进构建更强的多模态模型，验证了“LLM 作为数据/语义监督器”对 OVD 的价值。[csdn.net]

E. 通配符 / 自监督未知检测与开放世界机制  
- YOLO‑UniOW（同上）中的 Wildcard 学习（see 云端汇总）[cloud.tencent.com.cn]  
  问题：在无未知标签监督下，如何把“未见类别”检测为未知并支持后续词汇扩展。  
  方法：先训练一个通用“object”嵌入（T_obj），以此产生伪标签并进一步自监督学习“unknown”通配符嵌入（T_unk）；设计 IoU+得分阈值筛选和未知预测过滤策略以降低对已知类的干扰。  
  实验结论：在 OWOD 设置下，通配符策略能在不依赖示例重放的条件下提高未知召回率并减小对已知类的干扰，支持迭代将常见未知转入已知词汇表。[cloud.tencent.com.cn]

F. 三维 / 场景上下文与大模型融合的开放词汇延伸（示范性方向）  
- 基于上下文信息和大语言模型的开放词汇室内三维目标检测（程俊，2025） —（期刊报告）[jcjs.siat.ac.cn]  
  问题：将 OVD 思想扩展到室内 3D（点云）检测，同时利用上下文与 LLM 提供语义先验。  
  方法：将点云目标与场景上下文信息结合，借助 LLM 的链式推理或语义提示增强类别判定；提出针对稀疏/噪声点云的上下文融合策略。  
  实验结论：在 SUN RGB‑D / ScanNetV2 等室内数据集上，利用上下文 + LLM 能改进类别判别的准确性，提示 OVD 在 3D 场景下的可行扩展路径。[jcjs.siat.ac.cn]

实验与评价总结（共性结论）  
1) 预训练与对齐仍然是核心：基于大规模图文预训练（CLIP/VLM）并在检测器层面做区域—文本对齐，是绝大多数方法提升零样本性能的共同核心（例如 YOLO‑World、GroundingDINO、UniDetector、OVLW‑DETR）。  
2) 区域级 supervision 比 图片级 supervision 更有效：将文本信息精确对齐至候选区域或查询（region/query level）显著优于仅使用图像级标签进行词汇泛化（GroundingDINO、Region‑level 对齐方法的共识）。  
3) 参数高效适配可兼顾效率与泛化：使用 LoRA / 可学习 prompt / 替换分类权重等轻量化策略（AdaDL、LoRA、替换分类层）在不全量微调大型 VLM 的前提下，能在推理成本可控的同时提升多模态决策边界。  
4) 开放世界（未知发现）与开放词汇（新词识别）是不同的子问题：前者侧重未知样本的检出与后续增量学习（通配符、无监督伪标签、未知过滤），后者侧重词汇扩展与类别语义对齐；最近工作开始尝试在单一体系中统一二者（如 YOLO‑UniOW 的 Uni‑OWD 设定）。  
5) 评估与基准仍不一致：不同工作在 LVIS、COCO→LVIS transfer、M‑OWODB/S‑OWODB、nuScenes 等基准上报告不同指标（AP、APr、未知召回、WI/A‑OSE），导致横向比较困难；多来源训练（UniDetector）显示了“异构数据 + 校准”对实用泛化的重要性。  
6) LLM 作为监督/数据生成器的证据初显：LLMDet 等工作表明，用 LLM 生成的细粒度图像级与区域级描述能提高检测器的语义表示与新词汇识别能力，但也带来描述噪声与“幻觉”治理的挑战。

趋势与挑战（2025 年前后真实研究方向预测，至少三点）  
1) 模型级与训练级的“效率—泛化”折中将成为主战场：在边缘/实时部署需求下，未来更会出现以 LoRA、替换层、离线词表预计算与更廉价对齐损失为核心的工程化 OVD 方案（见 YOLO‑UniOW / OVLW‑DETR），目标是在资源受限设备上维持较高的开放词汇覆盖率。  
2) Open‑World 与 Open‑Vocabulary 的统一标准化评估将被推动：为解决目前指标与数据集不一致的问题，社区可能推出覆盖已知/未知/零样本三维度的统一基准与评价协议（结合 AP、未知召回、干扰度指标），并鼓励公开的多源混合训练基线（借鉴 UniDetector 的思路）。  
3) LLM ↔ VLM 协同训练与以 LLM 生成的高质量区域描述将成为提升语义细粒度的可行路径：但质量控制（幻觉过滤、事实性检验）与高效投影器设计是关键工程问题（参见 LLMDet 的 GroundingCap‑1M 做法）。  
4) 自动未知发现与迭代词汇扩展（无需人工重标注）的闭环将成为部署必备能力：以通配符/伪标签为核心的自监督策略需与主动学习或弱监督标注流水线结合，实现“模型建议 → 人工确认（或 LLM 辅助）→ 词汇扩展”的低成本闭环。  
5) 跨模态交互从“点对点对齐”向“场景级、因果/关系级”演进：尤其在 3D、视频与多视角场景中，融合上下文（关系、场景属性）与语言推理将是提高开放词汇判别精度的方向（参见 3D 点云 + LLM 的探索性工作）。  
6) 可解释性与安全性（错误归类/幻觉）将受重视：OVD 在实际场景（自动驾驶、安防）中的误报成本高，未来会发展对模型不确定性、语义置信度校准与可追溯伪标签来源的研究。

结论  
2022–2025 年间 OVD 从以 CLIP 为代表的图文预训练开始，迅速分化出（1）面向实时部署的工程化方案（YOLO‑World、YOLO‑UniOW、OVLW‑DETR）；（2）以区域级对齐与 grounding 为核心的学术模型（GroundingDINO、OVLW‑DETR）；（3）通过多源训练与概率校准扩展词汇量的系统性方法（UniDetector）；（4）以 LLM 为新型监督或数据源的增强范式（LLMDet）。共性的研究结论显示：区域级对齐、参数高效适配与多源训练是提升零样本/开放世界泛化的三大有效策略；但评测标准不统一、未知检测与词汇扩展闭环尚不成熟、LLM 引入的语义噪声需治理，这些是未来 2–3 年内需要集中解决的问题。希望本文的分类与总结能为后续方法设计与评测基线选择提供参考。

参考文献（按出现或主题相关，均为公开论文/主要报告或 arXiv/会议条目；检索链接以便定位原文或权威概述）  
（注：下列项给出论文名 + 便捷检索链接／综述页面）

1. YOLO‑World: Real‑Time Open‑Vocabulary Object Detection (Cheng et al., CVPR2024) — 汇总/讲解页面 [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/875de057-0739-403a-9847-0042f5923b28)  
2. YOLO‑UniOW: Efficient Universal Open‑World Object Detection (arXiv/tech report summary) — 综述页 [cloud.tencent.com.cn](https://cloud.tencent.com.cn/developer/article/2508448)  
3. Grounding DINO: Grounded Object Detection (IDEA‑Research, arXiv 2303.05499) — 概览/文档 [opendeep.wiki](https://opendeep.wiki/IDEA-Research/GroundingDINO/grounded-object-detection)  
4. Detecting Everything in the Open World: Towards Universal Object Detection (UniDetector), CVPR2023 — 综述/导读 [csdn.net](https://blog.csdn.net/qq_40279050/article/details/131517817)  
5. OVLW‑DETR: Open‑Vocabulary Light‑Weighted Detection Transformer (2024 report) — 概要 [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/ff92e11a-fa8b-4db1-91af-887ad24e7602)  
6. LLMDet: Learning Strong Open‑Vocabulary Object Detectors under the Supervision of Large Language Models (CVPR2025 report / code) — 介绍 [csdn.net](https://blog.csdn.net/fengdu78/article/details/148546526)  
7. ViLD / Region‑level distillation and early region‑CLIP style works — 视觉‑语言蒸馏与区域对齐代表作（请参见各自 arXiv/会议页；区域对齐/蒸馏为 OVD 基石）。示例检索：RegionCLIP / ViLD / GLIP（检索原论文以获取具体实现与实验）。  
8. Detic: Detecting Twenty‑Thousand Classes Using Image‑level Supervision (代表大词汇弱监督训练思路；详见相应 arXiv/会议页面)。  
9. OWL‑ViT: Open‑Vocabulary Localization/Detection with CLIP (代表以 CLIP 为核心的检测对齐方法；详见 arXiv/发表页)。  
10. “开放词汇目标检测方法综述” (聂秀山 等, 2025) — 期刊综述（中文版，涵盖 OVD 的方法分类与进展）[cjournal.hep.com.cn](https://cjournal.hep.com.cn/1672-3961/CN/1160168911137333430)  
11. 基于上下文信息和大语言模型的开放词汇室内三维目标检测 (程俊, 2025) — 期刊/会议稿 [jcjs.siat.ac.cn](https://jcjs.siat.ac.cn/article/doi/10.12146/j.issn.2095-3135.20241201003)  
12. GroundingDINO / Grounded object detection 原始 arXiv 与实现（用于 region‑text grounding 的关键参考，见上 opendeep.wiki 链接）[opendeep.wiki](https://opendeep.wiki/IDEA-Research/GroundingDINO/grounded-object-detection)

（附：由于 OVD 领域跨模态进展迅速，读者在深入实现或复现时应检索各论文的 arXiv / 会议最终版本以获取完整的实验设置、代码与权重；上文引用的汇总与博客页便于快速定位与理解原论文思路。）