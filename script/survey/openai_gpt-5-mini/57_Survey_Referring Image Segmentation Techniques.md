引言  
指代图像分割（Referring Image Segmentation, RIS）旨在根据自然语言表达（referring expression）在像素级定位并分割出被指代的对象。近三年（2022–2025）该领域呈现三条明显发展线：1）基于大规模视觉语言预训练（如 CLIP / ViLT / 通用 VLM）的弱/零样本与开放词汇方法；2）以 transformer 为核心的端到端单阶段模型与早期跨模态融合策略；3）借助大分割模型（如 SAM）或伪标签策略的半/弱监督方法以减少掩码标注需求。下文按方法类别汇总代表性工作，突出研究问题、方法要点与关键实验结论（每篇 4–6 句），随后给出实验/评价的共性总结与 2025 年前后的趋势预测。

方法分类与代表作
A. 基于 Transformer 与早期融合的单阶段/无卷积方法（single-stage / conv-free）
- ReSTR: Convolution-free Referring Image Segmentation Using Transformers (ReSTR, 2022)。该工作提出完全以 Transformer 为骨干的 RIS 架构，强调在视觉编码阶段就将语言信息注入（early fusion），并用自注意力实现跨模态交互；方法替代传统“拼接-卷积-解码”流程，直接生成像素级掩码。实验在主流基准（RefCOCO/RefCOCO+ 等）上展示了相比卷积基线更稳健的跨模态对齐与较少的任务特定模块设计需求，从而在多数据集上取得竞争性表现（参见社区综述与实现笔记）[devpress.csdn.net].  
  参考资料：ReSTR 方法综述与实现说明见社区整理 [devpress.csdn.net](https://devpress.csdn.net/v1/article/detail/124409891).

- LAVT: Language-Aware Vision Transformer for Referring Image Segmentation (LAVT, 2022)。LAVT 在视觉 Transformer 中提出“pixel–word attention module (PWAM)”与语言门控（language gate），实现词级信息对中间视觉 token 的逐层引导（encoder-side fusion）；解码器保持轻量 mask predictor，从而总体参数/计算经济。论文实验表明：早期/多层次的语言注入比解码端后融合在细粒度对齐上更有效，能在保持轻量解码器的同时提升 mIoU 和高阈值精度（见工程复现与笔记）[blog.csdn.net].  
  参考资料：LAVT 阅读笔记见 [blog.csdn.net](https://blog.csdn.net/weixin_42653320/article/details/124401205).

B. 利用大尺度视觉–语言预训练（CLIP 等）与对比式对齐
- CRIS: CLIP-Driven Referring Image Segmentation (2022, 预印本/实现笔记)。针对 RIS 中文本与像素细粒度对齐欠缺的问题，CRIS 借助 CLIP 的语义空间提出 text-to-pixel contrastive learning：把文本投影与像素级视觉特征用对比损失直接对齐，并在解码端用多模态解码器细化掩码。关键结论是：在有限或无额外掩码微调的条件下，CLIP 驱动的对比目标可显著提升开放词汇及零/少样本迁移能力（详见社区笔记）[cnblogs.com].  
  参考资料：CRIS 方法解析见 [cnblogs.com](https://www.cnblogs.com/lipoicyclic/p/16807808.html).

- “Shatter and Gather: Learning Referring Image Segmentation with Text Supervision” (arXiv 2023)。该工作提出仅用图像-文本对（无掩码）进行弱监督 RIS 的框架：先在图像中“碎片化”发现语义实体（shatter），再根据文本约束聚合相关片段（gather）生成候选掩码并用专门设计的损失训练。实验证明，在没有像素级标签的设置下，该方法能在若干公共基准上超越此前的开放词汇/弱监督基线，说明纯文本监督结合合适的聚合与对比损失对掩码学习可行 [arXiv:2308.15512; 参见文献整理]。  
  参考资料：论文预印本与方法说明见 arXiv 摘要汇总 [devpress.csdn.net](https://devpress.csdn.net/v1/article/detail/132752912).

C. 结合显式分组 / 像素级 co-embedding 的迭代 bottom-up + top-down 方法
- See-Through-Text Grouping for Referring Image Segmentation (ICCV 2019)。提出 STEP（See-through-Text Embedding Pixelwise）逐像素视觉-文本共同嵌入并生成底层热力图，随后用 ConvRNN 做自上而下的迭代精炼；强调将 bottom-up 分组线索与 top-down 文本引导融合以获得更精确的像素兼容性评估。实验显示该像素级 co-embedding 策略在多项基准上能显著提升定位精度，尤其在遮挡与背景干扰强的场景中更鲁棒（ICCV 2019 结果）[blog.csdn.net].  
  参考资料：See-Through-Text 阅读笔记与 ICCV 链接见 [blog.csdn.net](https://blog.csdn.net/qq_38929105/article/details/135304928).

D. 半监督 / 弱监督与伪标签增强（SAM 等工具作掩码后处理）
- Learning From Box Annotations for Referring Image Segmentation (TNNLS 2022)。针对仅有边界框监督的弱标注场景，文中提出对抗边界损失以突出前景轮廓并据此过滤 region proposals 生成伪掩码；同时采用 Co-Training（两个网络互相筛选高置信像素）来抑制伪标签噪声。关键结论是：结合轮廓先验与双网自训练策略，基于 box 的弱监督能在多数数据集上接近全监督性能的中高阶指标（尤其在 IoU/Prec@0.5 级别）[blog.csdn.net].  
  参考资料：TNNLS 2022 方法与代码说明见 [blog.csdn.net](https://blog.csdn.net/qq_38929105/article/details/129441551).

- SAM as the Guide: Mastering Pseudo-Label Refinement in Semi-Supervised Referring Expression Segmentation (SemiRES, 2024)。SemiRES 将高质量分割模型 SAM（Segment Anything Model）用于伪标签提取与最优掩码匹配（IOM/CPI），并设计像素级调整策略（PWA）以在匹配失败时修正伪标签。大量半监督实验（RefCOCO/RefCOCO+/G-Ref）表明：在极低标注比例（如 1%）下，用 SAM 精炼的伪标签能带来远超传统自训练的性能增益（例如 val 上可达十余个百分点的提升），尤其在边界质量上改进最明显 [hub.baai.ac.cn].  
  参考资料：SemiRES 方法汇总见 BAAI Hub 梳理 [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/712005f5-dcb2-433e-880a-f27e382fff28).

E. 数据集、基准与评估重审（数据质量与长表达）
- Revisiting Referring Expression Comprehension Evaluation in the Era of Large Multimodal Models — Ref‑L4 (2024)。该工作人工审查并发现现有 REC/RIS 基准（RefCOCO、RefCOCO+、RefCOCOg）存在显著标注噪声（RefCOCO ≈ 14% 错误率等），进而构建 Ref‑L4：一个更大、更长表达、更丰富类别的评测集（约 45k 注释），用于对现代大型多模态模型进行更稳健的评估。实证显示：清理后的基准以及 Ref‑L4 能显著改变模型在不同体系下的相对排名，强调基准质量对 RIS/REC 结论的决定性影响 [hub.baai.ac.cn].  
  参考资料：评估重审与 Ref‑L4 详述见 BAAI Hub 梳理 [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/c581ede2-3854-4820-a9b1-a7f9a6b32d70).

实验与评价总结（共性结论，按要求不逐篇赘述）
- 早期/编码器端跨模态融合 (encoder-side early fusion) 在细粒度对齐（高 IoU 阈值与小对象分割）上普遍优于仅在解码端融合的“拼接-卷积”策略；Transformer-based 多层注入比单次全局融合更有利于词级到像素级的精确匹配。  
- 利用大规模 VL 预训练（CLIP 等）并引入 text–pixel 对比损失，能显著增强开放词汇与零/少样本泛化，但若缺乏像素级细化模块则在边界质量上仍逊于掩码监督方法。  
- 半/弱监督方法的关键瓶颈在于伪标签的边界质量与噪声传播：基于显式轮廓先验（box→轮廓→proposal）或用 SAM 精炼伪掩码能显著提升伪标签的有效性，从而在低标注条件下取得可用性能。  
- 基准数据质量（标签噪声、表达长度与多样性）对模型排名影响很大：清洗后的评测或更大、更长表达的基准（如 Ref‑L4）会揭示不同模型在复杂语言理解与细粒度定位上的真实差异。  
- 现有工作对计算效率与部署友好性的考虑仍不统一：Transformer/conv-free 方法在精度上有潜力，但在嵌入式或实时场景需进一步压缩与加速。

趋势与挑战（面向 2025 年前后；至少三点，均为可验证的研究方向/挑战）
1. 大分割模型 + 语言适配成为常态化工具链：SAM 等通用掩码模型将作为伪标签/先验提供者，与小规模语言适配器（text adapters）结合，促进半/少样本 RIS。挑战在于如何在不泄露下游标签偏差的前提下，自动选择/融合 SAM 掩码以防止“过分分割”（over-segmentation）。参见 SemiRES 的伪标签精炼思路 [hub.baai.ac.cn].  
2. 从“图像作为输入”向“与图像共思考”的范式转移：多模态推理进一步要求模型在推理链中把视觉作为可操作的中间表征（visual chain-of-thought），这需要新的可解释中间表示与交互式训练信号（示例见近期多模态综述方向）。挑战是设计可微、可调的视觉中间表示并提供相应评测。见多模态推理综述与启示（社区讨论）。  
3. 开放词汇与复杂查询的稳健评估将驱动新的基准与训练范式：Ref‑L4 与类似长文本/多实体查询基准暴露出短表达基准的弱点，未来研究需关注长表达、关系约束与跨场景泛化；这要求集合更大规模多语种/长上下文数据与噪声鲁棒训练。参见 Ref‑L4 的数据与评估动议 [hub.baai.ac.cn].  
4. 细粒度对齐（word ↔ pixel）将成为衡量模型能力的核心子任务：对比式像素级损失与层次化注意力（pixel–word attention）是目前最有成效的做法，但仍需改进负样本采样策略与多实例消歧（disambiguation）；这直接影响小物体与重叠对象的分割精度（见 LAVT、CRIS 等工作）。  
5. 减少人工掩码标注的成本并保持边界质量：弱/自监督方法（仅文本、仅 box，或少量掩码+大量未标注）会持续发展，关键技术点包括更可信的伪标签判定、基于几何/轮廓的正则化、以及跨模态一致性损失的设计（参考 TNNLS 2022 与近期 SAM 引导的半监督方法）[blog.csdn.net; hub.baai.ac.cn]。

结论  
2022–2025 年间，RIS 从以往“拼接-卷积-解码”的范式迅速向两端并进：一端是基于 transformer 的早期融合与无卷积设计（提升词级到像素级的对齐能力）；另一端是将大规模 VL 预训练与大分割模型（如 SAM）作为工具纳入训练/伪标签流程以减少对人工掩码的依赖。未来研究需要在开放词汇泛化、伪标签质量控制、长表达理解与部署效率之间寻找平衡，并以更干净、更具挑战性的基准（Ref‑L4 等）来驱动方法的稳健性验证。以上综述基于公开发表或预印本的代表性工作与社区实现/笔记汇总，旨在为后续研究提供紧凑且可操作的路线图。

参考文献（至少 12 篇；含原论文与社区整理/实现笔记以便查阅）  
- ReferIt: “ReferIt game: Referring to objects in photographs of natural scenes”, EMNLP 2014 (数据集). 综述与数据集链接见 [blog.csdn.net](https://blog.csdn.net/qq_33000225/article/details/90486447).  
- Mao et al., “Generation and comprehension of unambiguous object descriptions”, CVPR 2016 (Google-Ref 数据集). 数据集说明见 [blog.csdn.net](https://blog.csdn.net/qq_33000225/article/details/90486447).  
- Yu et al., “MAttNet: Modular Attention Network for Referring Expression Comprehension”, CVPR 2018 (参考表达理解基础工作). 实现与解读见 [blog.csdn.net](https://blog.csdn.net/qq_33000225/article/details/90486447).  
- “See-Through-Text Grouping for Referring Image Segmentation”, ICCV 2019 (See‑Through‑Text / STEP + ConvRNN). 阅读笔记与 ICCV 链接见 [blog.csdn.net](https://blog.csdn.net/qq_38929105/article/details/135304928).  
- “Cross-Modal Self-Attention Network for Referring Image Segmentation (CMSA)”, CVPR 2019 (跨模态自注意力方法). 综述见 [blog.csdn.net](https://blog.csdn.net/m0_37847767/article/details/110188986).  
- “Learning From Box Annotations for Referring Image Segmentation”, IEEE TNNLS 2022（弱监督：box→轮廓→proposal + Co‑T）。方法笔记见 [blog.csdn.net](https://blog.csdn.net/qq_38929105/article/details/129441551).  
- ReSTR: “ReSTR: Convolution-free Referring Image Segmentation Using Transformers” (Transformer‑based, early fusion) — 方法/实现讨论见 [devpress.csdn.net](https://devpress.csdn.net/v1/article/detail/124409891).  
- LAVT: “LAVT: Language‑Aware Vision Transformer for Referring Image Segmentation” (pixel–word attention, encoder fusion). 阅读笔记见 [blog.csdn.net](https://blog.csdn.net/weixin_42653320/article/details/124401205).  
- CRIS: “CRIS: CLIP‑Driven Referring Image Segmentation” (text‑to‑pixel contrastive alignment; 预印本/实现笔记) — 方法解析见 [cnblogs.com](https://www.cnblogs.com/lipoicyclic/p/16807808.html).  
- “Shatter and Gather: Learning Referring Image Segmentation with Text Supervision”, arXiv:2308.15512 (文本监督 / 无掩码弱监督) — 摘要与讨论见 arXiv 汇总 [devpress.csdn.net](https://devpress.csdn.net/v1/article/detail/132752912).  
- “SAM as the Guide: Mastering Pseudo‑Label Refinement in Semi‑Supervised Referring Expression Segmentation” (SemiRES, 2024) — SAM 引导的伪标签精炼与半监督实验报告，资源与解析见 BAAI Hub 梳理 [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/712005f5-dcb2-433e-880a-f27e382fff28).  
- “Revisiting Referring Expression Comprehension Evaluation in the Era of Large Multimodal Models” — Ref‑L4 (2024)：人工清洗/新基准构建与评估，详见 BAAI Hub 梳理 [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/c581ede2-3854-4820-a9b1-a7f9a6b32d70).  

（补充说明：上文方法介绍与要点参考并整合了社区实现笔记与论文综述资源，上述 blog/Hub 链接便于快速查阅原论文、代码与实证细节。为保证学术可验证性，读者在后续实验复现时应直接检索各篇论文的会议/期刊或 arXiv 原文。）