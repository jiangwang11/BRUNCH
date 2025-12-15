引言  
状态空间模型（State Space Models, SSMs）在序列建模领域因线性复杂度与长程依赖建模能力受到 NLP 社区重视；近三年（2022–2025）SSM 变体（尤其以 Mamba 系列与其衍生工作为代表）被系统地迁移到视觉任务中，成为图像/视频恢复、视觉骨干、视频帧插值与 3D 点云分析等低级与中级视觉任务的新范式。本综述只选取 2022–2025 年间在图像处理方向有明确方法学贡献且可检索的代表性工作，按方法类别总结核心技术路线与实验结论，最后给出基于现有证据的研究趋势与挑战预测。为保证可验证性，文内引用均指向公开论文或预印本页面（见参考文献）。

方法分类与代表作  
说明：每个子节列出 3–5 篇代表性工作，按“研究问题 — 核心方法 — 关键实验结论”依次给出（每篇 4–6 句）。

1. 视觉骨干：将 SSM 用作通用视觉 encoder/骨干  
- Vision Mamba / ViM（双向 Mamba 骨干，视觉表示学习）— 将双向 Mamba（双向状态空间）作为视觉骨干，使用位置嵌入对图像 token 化并在多任务（ImageNet 分类、COCO 检测、ADE20K 分割）上评估；方法以双向扫描克服单向 SSM 的因果限制，并结合层级化架构；实验显示在高分辨率下相比同规模 ViT/Transformer 基线显著降低显存占用并提高推理速度/吞吐（原文及代码在社区多处复现总结）[blog.csdn.net].  
 （参考读物以 ViM 论文和学习笔记为主；实现细节与速度/显存评估见社区精读）[blog.csdn.net].  

- V‑Mamba / Mamba‑Vision 相关工程尝试 — 一系列工作探讨将 Mamba/SMSM 模块与视觉 Transformer 混合以兼顾全局建模与局部感受野；核心策略包括双向/多向选择性扫描与对位置感知的增强（位置嵌入与局部卷积），并报告在 ImageNet/下游任务的可比性能与更低的内存/延迟开销（社区复现与工程化讨论）[blog.csdn.net].  

2. 图像恢复与增强（低级视觉）  
- MambaIR: image restoration baseline（ECCV 2024）— 问题：单图超分／去噪等图像恢复中如何同时获得全局感受野与高效计算；方法：将 Mamba 状态空间块嵌入恢复骨干，提出残差状态空间块（RSSB）——在 SSM 后并入局部卷积与通道注意力以补偿展平序列带来的局部像素遗忘与通道冗余；结论：在多个超分／去噪基准上与经典 Transformer/CNN 基线相比，MambaIR 在 PSNR 上取得稳定提升同时保持类似计算成本（ECCV 摘要与社区复述）[chatpaper.com].  

- MambaIRv2: Attentive State Space Restoration（arXiv）— 问题：如何赋予选择性 SSM 非因果/注意力式的交互能力以改善图像恢复；方法：提出注意状态空间方程（attentive SSM），一次扫描即可促进非因果交互，并引入语义引导邻域机制以鼓励远距离相似像素交互；结论：在轻量级及经典超分任务上均比同类 Transformer 方案有明显 PSNR 提升且参数更少，证明注意化 SSM 对低级视觉有益[chatpaper.com].  

- WaterMamba: underwater image enhancement（arXiv）— 问题：水下图像退化复杂（颜色偏移、散射），现有 CNN/Transformer 在效率或泛化存在权衡；方法：提出基于 SSM 的 WaterMamba，包含空间-通道全向选择扫描（SCCOSS）与多尺度前馈网络，专门在空间与通道维度上用选择性扫描建模频带与像素相关性；结论：在若干 UIE（underwater image enhancement）数据集上，以更少参数/计算优于现有 CNN/Transformer 方法，强调 SSM 对效率—长依赖的天然优势[chatpaper.com].  

3. 频域与任务特定 SSM 变种（频率/傅里叶域）  
- FourierMamba: image deraining（arXiv preprint summarized in blog）— 问题：基于傅里叶的去雨方法很少显式建模频率间相关性；方法：将 Mamba 的选择性扫描机制移入傅里叶域，空间维度采用 Z 字形扫描以建立低频—高频序列关系，通道维度直接用 Mamba 关联频率通道；结论：在合成/真实去雨基准上频域—序列化 SSM 架构有效提升去雨质量并改善频域一致性（博客摘要、实验说明）[blog.csdn.net].  

- 频域/通道混合 SSM（多篇工作）— 若干近期预印本尝试在频域或通道维度应用 SSM（Mamba/S4 变体）以利用频谱先验，关键发现是频域序列化后 SSM 能更有序地捕获纹理/条纹类退化（论文集合与博客讨论）[blog.csdn.net].  

4. 时序 / 视频与帧间任务（VFI、视频重建）  
- VFIMamba: Video Frame Interpolation with State Space Models（社区/报告）— 问题：视频帧插值中如何有效建模帧间长程运动而兼顾高分辨率计算开销；方法：用混合 SSM 模块（MSB）对交错排列的相邻帧令牌进行多方向 SSM 建模，并引入课程学习策略以按运动幅度递进训练；结论：在高分辨率数据集（X-TEST 等）上对 2K/4K 帧插值取得显著 PSNR 提升，特别在高分辨率场景中 SSM 的线性复杂度优势更明显[hub.baai.ac.cn].  

- 其它视频/时序工作（基于 Mamba 的时序块）— 多篇实现报告显示 SSM 块（Mamba/S4 变体）在视频去噪、插帧与长期时序建模上比局部卷积/窗口化 Transformer 更能以更低 FLOPs 捕获跨帧全局运动（社区技术报告）[hub.baai.ac.cn].  

5. 三维 / 点云与遥感应用  
- PointMamba: point cloud analysis（NeurIPS 2024 / OpenReview）— 问题：点云任务需全局建模但注意力平方复杂；方法：将 Mamba 迁移至点云，利用空间填充曲线（如 Z-order 或 Hilbert）进行点标记化，并用非层次化 Mamba 编码器作为主干以获得线性复杂度的全局建模；结论：在多个点云基准上性能优于同规模 Transformer，同时显著降低 GPU 内存与 FLOPs，证明 SSM 可行于 3D 视觉[chatpaper.com].  

- RSMamba / RS‑Mamba（遥感图像分类/分割）— 问题：高分辨率遥感图像具有大尺度多向空间特征，传统横纵扫描不足；方法：提出动态多路径激活、全向选择性扫描（包括斜向扫描）以捕获多方向大尺度空间依赖；结论：在若干遥感场景分类/分割数据集上取得 SOTA 或接近 SOTA 的结果，并显著降低内存/计算需求（社区综述与实现笔记）[blog.csdn.net].  

实验与评价总结（只总结共性结论，不逐篇复述）  
- 复杂度与尺度：SSM（特别是 Mamba 类）在展平后以并行扫描/并行化实现线性时间复杂度，因而在高分辨率图像与长视频上下文（64K+ token、4K 帧）下显示出优越的计算/内存伸缩性；这一点在图像恢复与视频插值的高分辨率实验中被反复验证。  
- 局部性——全局性互补：纯 SSM（按行/列展平的因果扫描）会丢失二维邻域局部性；成功的视觉 SSM 实践普遍在 SSM 模块后或内嵌局部卷积 / 局部增强（例如残差卷积、DWConv）或通道注意力，以恢复局部纹理信息并缓解通道冗余。  
- 非因果/多向扫描的必要性：单向（因果）SSM 在语言序列中自然适用，但图像/视频需要非因果交互；多向选择性扫描（四向/八向/斜向）或注意化 SSM（允许一次扫描实现非因果交互）在恢复与生成任务上带来一致性能收益。  
- 频域与任务特化：在频域（傅里叶）或通道维度应用 SSM 可有效利用频率先验（如去雨、去条纹），但需定制化的扫描策略（如 Z 字形编码）以保证频率顺序相关性。  
- 易用性与工程优化：许多工作强调工程化策略（并行扫描实现、多方向合并、局部卷积补偿、量化/稀疏化）对真实部署和速度至关重要；换言之，方法学改进需伴随硬件/推理实现优化才能落地。

趋势与挑战（面向 2025 年前后预测，至少 3 点，基于已发表工作与共性结论）  
1. 从单向 SSM 到“注意化 / 双向” SSM 将成为主流：原始 SSM 的因果限制在视觉任务上是主要瓶颈，未来工作会更多采用注意化状态方程或一次扫描实现全局非因果交互（例如 MambaIRv2 的方向），并结合语义引导邻域以提升恢复质量。已有预印本已证明该方向在超分和恢复中效果显著。  
2. 频域/多域混合 SSM 将扩大应用范围：把 SSM 放到傅里叶或通道频谱上（如 FourierMamba）可以更直接地利用周期性/条纹性退化先验；未来会涌现更多“域化 SSM”（时域/空域/频域联合）以针对性解决去雨、去条纹、去模糊等任务。  
3. SSM 与局部卷积 / 局部注意力的混合架构成为标准设计模式：实践表明纯 SSM 易丢局部结构，因而最有效的视觉骨干/恢复网络会把 SSM 作为长程通道（global aggregator），同时保留轻量级局部算子补偿邻域信息。工程化的验证（内存/延迟）会推动该混合范式成为工业实现主流。  
4. 视频/时序任务对 SSM 的拉动作用增强：高分辨率视频插值、去噪与长期一致性任务天然受益于线性复杂度的 SSM（VFIMamba 等），未来 SSM 在视频生成与视频编辑（包括交互式/实时）中的占比将增长。  
5. 硬件/推理友好型 SSM 优化将成为研究热点：要把 SSM 成果落地，需改进并行扫描内核、量化与投机采样等工程策略；因此方法论文必须同时给出实际推理优化与基准（延迟/吞吐/内存）对比。  
6. 监督/自监督预训练结合：面向视觉的 SSM 基座（例如 Vision‑Mamba）将与大规模视觉自监督预训练方法结合，用以构建多任务视觉基础模型（classification→detection→restoration→video），并以少量微调适配下游视觉场景。

结论  
过去三年出现的以 Mamba 为代表的 SSM 家族已证明：通过合理的扫描策略（多向/注意化）与局部补偿（卷积/通道注意力），SSM 可以在图像恢复、视觉骨干、视频插值与 3D 点云等视觉任务中以更低的计算代价实现长程依赖建模。未来的研究需要在方法泛化（跨域/频域）、非因果交互机制、以及系统级推理优化之间找到平衡，以便把 SSM 从有吸引力的学术方法进一步推进为可规模化部署的视觉基座。

参考文献（按出现顺序列出；均指向可检索页面）  
- MambaIR: A Simple Baseline for Image Restoration with State-Space Model (ECCV 2024) — 论文与摘要汇总页 [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/99851)  
- MambaIRv2: Attentive State Space Restoration (arXiv 2411.15269) — 预印本摘要 [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/85148)  
- WaterMamba: Visual State Space Model for Underwater Image Enhancement (arXiv 2405.08419) — 预印本摘要 [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/20753)  
- Vision Mamba: Efficient Visual Representation Learning with Bidirectional State Space Model (preprint summary / 学习笔记引用，原 arXiv:2401.09417) — 社区精读 [blog.csdn.net](https://blog.csdn.net/qq_46981910/article/details/139058346)  
- VFIMamba: Video Frame Interpolation with State Space Models (实现/报告页面) — 智源社区报告 [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/b2942421-c3a9-42bb-bda6-6262b3e2637b)  
- PointMamba: A Simple State Space Model for Point Cloud Analysis (NeurIPS 2024 / OpenReview entry) — 论文汇总 [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/83497)  
- FourierMamba: Fourier Learning Integration with State Space Models for Image Deraining (arXiv/预印本，论文解读) — 技术解读 [blog.csdn.net](https://blog.csdn.net/qq_42722197/article/details/145314007)  
- RSMamba / RS‑Mamba: Remote Sensing Image Classification/Segmentation with State Space Models — 综述与实现笔记 [blog.csdn.net](https://blog.csdn.net/qq_45880982/article/details/137541159)  
- Vision Mamba / ViM 系列多篇社区精读与实现笔记（双向 SSM 视觉骨干讨论汇总）[blog.csdn.net](https://blog.csdn.net/qq_46981910/article/details/139058346)  
- Mamba 系列在多模态/3D/遥感等方向的工程化报告与复现集合（社区汇总）[devpress.csdn.net](https://devpress.csdn.net) / [blog.csdn.net](https://blog.csdn.net)（若干实现与复现文章）  
- ECCV/NeurIPS/社区讨论与实现仓库（MambaIR 代码仓、PointMamba/Github 链接） — 由各作者在论文或代码页公开（参见上文各条目内的原始链接）[chatpaper.com](https://chatpaper.com) / [github.com (via paper pages)](https://github.com)  
注：综述中所引用的论文与项目以可检索的会议论文、arXiv 预印本与社区官方论文页面为准；上文所列链接指向检索/摘要与实现汇总页面（社区与会议信息），读者可沿每条页面进一步访问原始 PDF 与代码仓库以获取方法细节与数据。