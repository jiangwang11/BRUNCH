引言  
视频修复（video restoration）涵盖去噪、去模糊、超分辨率、修补（inpainting）与上色等任务，目标是在保持时间一致性的同时从真实退化中恢复高质量帧序列。2022–2025 年间，研究呈现三条并行且相互交织的主线：基于显式/隐式对齐的帧间信息传播（propagation/alignment）、基于Transformer与状态空间的长程时空建模，以及基于扩散/生成模型的高保真、感知优化修复。下文按方法类别归纳代表工作，随后总结实验评估的共性结论并给出趋势与挑战预测。文中所引均为真实公开的论文/预印本或权威综述（见参考文献）。

方法分类与代表作  
（每篇 4–6 句，突出问题、方法与关键实验结论）

A. 基于对齐与帧间传播的方法（经典与改进）  
- EDVR — Video restoration with enhanced deformable convolutional networks（Wang et al., CVPRW 2019；综述收录）  
  研究问题：多帧视频超分辨率/恢复中如何高效对齐并融合多帧信息以恢复细节。  
  核心方法：引入增强型可变形卷积模块（Pyramid, Cascading, Deformable alignment, PCDA）和局部-全局融合机制以实现隐式对齐与多尺度特征聚合。  
  关键实验结论：在合成与真实退化基准（如REDS）上，EDVR 在 PSNR/SSIM 与视觉细节保留上显著优于当时主流方法，且对大幅运动场景比显式光流方法更鲁棒。[aas.net.cn](https://aas.net.cn/)  
- BasicVSR / BasicVSR++（Chan et al., CVPR 2021 / CVPR 2022；综述收录）  
  研究问题：如何设计简单而稳健的帧间传播框架以实现高效且时间一致的视频恢复。  
  核心方法：BasicVSR 提出双向（forward/backward）隐式特征传播与融合策略，利用光流或隐式对齐进行跨帧信息流动；BasicVSR++ 在此基础上改进了对齐与传播模块以提高精度与效率。  
  关键实验结论：BasicVSR 系列在多个数据集上（REDS、Vimeo-90K 等）达到了极具竞争力的 PSNR/SSIM，同时证明了长时间范式（全帧传播）对时间一致性与细节重建的有效性。[aas.net.cn](https://aas.net.cn/)

B. Transformer 与长程时空建模方法  
- VRT — Video Restoration Transformer（Liang et al., IEEE TIP 2024；综述收录）  
  研究问题：传统卷积或局部注意力在高分辨率视频恢复中受限于局部视野或计算开销，如何进行高效的全局时空建模？  
  核心方法：提出多尺度时空Transformer 结构，结合局部与全局注意力策略，设计适用于视频的时空注意力与高效的特征传递机制。  
  关键实验结论：VRT 在多项视频恢复基准上（含降噪/超分）提升了主观细节与 LPIPS 等感知指标，且在对复杂运动与纹理保留上优于纯 CNN 架构。[aas.net.cn](https://aas.net.cn/)  
- CTVSR — Collaborative Spatial-Temporal Transformer for VSR（Tang et al., TCSVT 2024；综述收录）  
  研究问题：在 VSR 中如何协调空间局部细节与时间一致性以减少帧间伪影？  
  核心方法：引入协同空间-时间注意力模块，显式分配不同注意力路径以分别负责局部纹理与跨帧一致性；结合残差传播机制稳定训练。  
  关键实验结论：CTVSR 在标准基准上实现了 PSNR/SSIM 的提升，并在视觉连贯性测试（temporal metrics）上显示出更少的闪烁伪影。[aas.net.cn](https://aas.net.cn/)  
- RVRT — Recurrent Video Restoration Transformer（相关会议论文 /综述收录）  
  研究问题：如何在保证长程信息利用的同时控制 Transformer 的内存与计算成本？  
  核心方法：将 Transformer 设计为循环/递归结构，采用引导性 deformable attention 与时序记忆单元以实现可扩展的长序列建模。  
  关键实验结论：RVRT 在长序列恢复任务上展现出更好的标度性（scaleability）与较低的内存占用，同时保持或提升恢复质量。[aas.net.cn](https://aas.net.cn/)

C. 基于扩散/生成模型的视频修复与超分（近年快速发展）  
- Upscale-A-Video — Temporal-consistent diffusion model for real-world VSR（Zhou et al., CVPR 2023；综述收录）  
  研究问题：基于扩散模型能否在视频超分中合成高频细节且保持时间一致性？  
  核心方法：在潜在空间中训练视频扩散模型并加入时间一致性正则与运动引导（optical flow / temporal conditioning），以生成连贯细节。  
  关键实验结论：在真实退化集（RealVSR 等）上，扩散方法在 LPIPS / FID 等感知指标上优于传统回归式网络，但计算开销与采样时间仍是主要限制。[aas.net.cn](https://aas.net.cn/)  
- Learning spatial adaptation and temporal coherence in diffusion models for VSR（CVPR 2024 摘要/论文，综述收录）  
  研究问题：扩散模型在视频任务中常引入幻觉（hallucination）与时间不一致，如何通过空间自适应与时域正则控制？  
  核心方法：提出空间适应模块与时间一致性损失，将扩散采样过程与光流/帧对齐结合以抑制非一致生成。  
  关键实验结论：在合成与真实数据上既减轻了伪影又改善了 LPIPS，证明了条件化与显式时序约束对扩散视频恢复的必要性。[aas.net.cn](https://aas.net.cn/)  
- SeedVR / VideoPainter（2025 年新近工作）  
  SeedVR：提出扩散变换器并通过可变大小的移位窗口注意力处理任意长度与分辨率视频修复，强调在空间-时间边界的窗口可变性与因果视频 VAE 的配合。[hub.baai.ac.cn](https://hub.baai.ac.cn/paper/0e87d0a7-4467-4119-87bd-0cebfe408c85)  
  VideoPainter（SIGGRAPH 2025 / arXiv 报道）：采用双分支（背景保留 + 前景生成）设计与修复区域 ID 重采样以在长视频中保持物体 ID 一致性并兼容 DiT 骨干；同时发布了大规模 VPData 数据集以增强长视频训练鲁棒性。[blog.csdn.net](https://blog.csdn.net/AITIME_HY/article/details/147200218)  
  关键实验结论（合并）：两类工作均展示了扩散/DiT 在生成细节与编辑灵活性上的优势；但对长序列的 ID 保持与运行效率仍需工程化设计（如 ID 重采样、VAE 压缩）。[hub.baai.ac.cn](https://hub.baai.ac.cn/), [blog.csdn.net](https://blog.csdn.net/AITIME_HY/article/details/147200218)

D. 高效骨干与状态空间模型（效率与全局感受野）  
- Restormer — Efficient Transformer for high-resolution image restoration（CVPR 2022，工程化迁移到视频场景）  
  研究问题：如何在保持全局上下文建模能力的同时降低 Transformer 在高分辨率恢复上的二次复杂度？  
  核心方法：提出跨通道的多 DConv 头“转置”注意（MDTA）与门控 DConv 前馈网络（GDFN），以线性复杂度实现对高分辨率图像的高效恢复。  
  关键实验结论：在多项图像恢复任务中以较低计算成本实现或超越当时最强基线，为视频场景的高分辨率逐帧恢复或潜在空间处理提供有效骨干。[cloud.tencent.cn](https://cloud.tencent.cn/developer/article/2398294?policyId=1003)  
- MambaIR / MambaIRv2（ECCV 2024 / arXiv 2411.15269）  
  研究问题：如何用选择性状态空间模型（SSM）在图像恢复中同时获得线性复杂度与大感受野？  
  核心方法：将 Mamba 状态空间架构适配到视觉场景，加入局部增强与通道注意力（MambaIR），并在 v2 中扩展为非因果注意状态空间以模拟 ViT 式的全局交互。  
  关键实验结论：在超分与去噪任务上，MambaIR 系列在 PSNR 上优于同等计算量的 Transformer（如 SwinIR/HAT），表明 SSM 在低级视觉恢复中的工程潜力并能兼顾效率与全局性。[chatpaper.com](https://chatpaper.com/zh-CN/paper/99851), [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/85148)

E. 人脸与专向视频恢复（统一与多任务）  
- SVFR — A Unified Framework for Generalized Video Face Restoration（arXiv:2501.01235）  
  研究问题：视频人脸恢复需同时处理盲恢复、补画、上色等多任务，且要兼顾时间一致性与面部结构保真。  
  核心方法：提出基于视频扩散（Stable Video Diffusion）为基础的统一框架，加入任务嵌入、统一潜在正则化与面部先验学习，并用自我参考精炼提高时序稳定性。  
  关键实验结论：在人脸视频基准上统一框架在感知指标与时间一致性上均优于单任务基线，说明多任务潜在空间正则化能促进跨任务信息共享与稳健恢复。[themoonlight.io](https://www.themoonlight.io/zh/review/svfr-a-unified-framework-for-generalized-video-face-restoration)

实验与评价总结（只总结共性结论，不逐篇复述）  
1) 评价指标分化：传统像素指标（PSNR/SSIM）仍用于合成降级的最优性比较；但感知导向任务（尤其扩散/生成方法）更依赖 LPIPS、FID 与用户主观评测；因此单一指标不足以衡量“质量 vs 真实感 vs 一致性”三者的权衡。  
2) 时间一致性衡量尚不统一：多数工作在设计上显式约束时间一致性（双向传播、流引导、参考帧注入或时序损失），但用于衡量的一致性指标分散（temporal warping error、temporal LPIPS、光流一致性等），导致横向比较困难。  
3) 对齐策略影响巨大：在大运动场景中，隐式对齐（deformable / attention-based）往往比依赖精确光流的显式对齐更稳健；但显式运动先验在控制扩散模型幻觉方面仍十分关键。  
4) 扩散/生成方法的双刃剑：扩散模型能显著提升感知质量与细节合成，但带来采样成本高、出现伪影（尤其在无充分运动约束时）与一致性风险；工程上常借助潜在空间 VAE 压缩、时序正则与先验条件以缓解。  
5) 速度/资源权衡：高质量（感知优先）方法通常牺牲实时性；而用于边缘/在线场景的工作侧重递归传播或轻量化骨干（SSM/Restormer/MambaIR）以兼顾效率与长序列处理能力。  
6) 数据集与真实退化差距：众多方法在合成降级上取得高分但在 RealVSR / VideoLQ 等真实数据集上出现显著降级；因此泛化能力与退化建模仍是核心瓶颈。

趋势与挑战（2025 年前后真实可观测的方向，≥3 点）  
1) 扩散 + 运动先验的混合范式将成为主流工程路线：单纯的无条件扩散在视频上易生幻觉，因而未来工作会更普遍地把光流/稠密运动场/隐式对齐或 VAE 潜在运动表示与扩散过程耦合（已见 Upscale-A-Video、CVPR2024 的时序正则及 SeedVR 的时空窗口策略）。[aas.net.cn](https://aas.net.cn/), [hub.baai.ac.cn](https://hub.baai.ac.cn/)  
2) 潜在空间压缩（高比例 VAE/Video-VAE）+ 长序列扩散/Transformer 将成为处理超长视频的关键：Step-Video-T2V 等工作展示了深度压缩 VAE 与 Flow Matching/Video-DPO 等技术可以在多语言、长帧数生成上扩展，这也意味着视频修复将更多在更低维的潜在时空上进行。（参见 Step-Video-T2V 技术报告）[hub.baai.ac.cn](https://hub.baai.ac.cn/paper/1e8370f5-9db8-4d44-8006-bec0238341f8)  
3) 状态空间模型与高效 Transformer 的融合将加速部署级别的高分辨率恢复：MambaIR 系列与 Restormer 表明 SSM/MDTA 等结构能在保持全局感受野的同时实现线性复杂度，未来视频恢复骨干会更多采用混合 SSM–Transformer–卷积设计以满足高分辨率、低延迟的工程需求。[chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/99851), [cloud.tencent.cn](https://cloud.tencent.cn/developer/article/2398294?policyId=1003)  
4) 评价协议标准化与多维度基准将被推动：鉴于“像素/感知/一致性/ID 保真”四维要求在不同应用中的权重不同，社区将推动包含 LPIPS、temporal LPIPS、warp-error、ID-preservation（对人脸/对象）及用户研究在内的复合基准（VideoPainter 的 VPBench 是此方向的实例），以促进更可比的进展。[blog.csdn.net](https://blog.csdn.net/AITIME_HY/article/details/147200218)  
5) 面向长视频的身份一致性与可控编辑成为热点：VideoPainter 等工作已提出修复区域 ID 重采样用于长视频一致性，未来研究会把 ID 保真（尤其在人脸/目标修复与编辑场景）与生成灵活性结合为重要目标。[blog.csdn.net](https://blog.csdn.net/AITIME_HY/article/details/147200218)  
6) 能效与实时性压力推动模型压缩、蒸馏与 one-step 采样研究：为缩短扩散采样与减小算力，单步/少步扩散、蒸馏到一次性恢复网络或混合生成-回归流水线将成为实用化重要手段（参见一系列 2024–2025 工程化探索）。[aas.net.cn](https://aas.net.cn/)

结论  
2022–2025 年的视频修复研究既延续了对齐与传播范式在时间一致性与高 PSNR 方面的优势，也见证了 Transformer 与状态空间模型在长程时空建模与效率上的提升；近两年扩散与 DiT 类生成模型大幅推动了感知质量与编辑能力，但同时暴露出一致性、效率与泛化挑战。短期内（2–3 年）可预期的是混合范式（扩散+运动先验、SSM/Transformer 混合骨干）与更严格的多维评价协议将主导方向，从而推进视频修复向工程可用、长序列一致且可控的方向发展。

参考文献（均为公开论文/预印本或权威综述，文中按出现次序引用；点击域名以查看对应来源页面）  
- A comprehensive review and many VSR references: [aas.net.cn](https://aas.net.cn/cn/article/doi/10.16383/j.aas.c240235?viewType=HTML)  
- SeedVR (2025) — 扩散变换器用于通用视频修复（论文摘要页）: [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/0e87d0a7-4467-4119-87bd-0cebfe408c85)  
- Step-Video-T2V technical report (2025) — 文本到视频基础模型实践: [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/1e8370f5-9db8-4d44-8006-bec0238341f8)  
- VideoPainter (SIGGRAPH 2025 报道 / arXiv 索引说明): [blog.csdn.net](https://blog.csdn.net/AITIME_HY/article/details/147200218)  
- SVFR (arXiv 2501.01235) — 统一视频人脸恢复综述/预印本摘录: [themoonlight.io](https://www.themoonlight.io/zh/review/svfr-a-unified-framework-for-generalized-video-face-restoration)  
- Restormer (CVPR 2022 说明与解读): [cloud.tencent.cn](https://cloud.tencent.cn/developer/article/2398294?policyId=1003)  
- MambaIR (ECCV 2024) & MambaIRv2 (arXiv／摘要页面): [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/99851), [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/85148)  
- Two-stage high-resolution image restoration with pre-trained diffusion model (期刊 / 2025): [arocmag.cn](https://www.arocmag.cn/abs/2024.10.0438)  
- EDVR / BasicVSR / BasicVSR++ / many VSR classics & comparisons (详尽综述与表格): [aas.net.cn](https://aas.net.cn/cn/article/doi/10.16383/j.aas.c240235?viewType=HTML)  
- Upscale-A-Video（CVPR 2023，视频扩散用于真实 VSR，综述中引用）: [aas.net.cn](https://aas.net.cn/cn/article/doi/10.16383/j.aas.c240235?viewType=HTML)  
- 学界对扩散在 VSR 中的空间适应与时间一致性方法（CVPR2024 类工作，综述收录）: [aas.net.cn](https://aas.net.cn/cn/article/doi/10.16383/j.aas.c240235?viewType=HTML)  
- DiffuEraser 报道（基于稳定扩散的视频修复技术介绍）: [blog.csdn.net](https://blog.csdn.net/weixin_42380711/article/details/145371669)  
- 关于视频基础模型的系统讨论（Step-Video-T2V 报告中亦有技术与评估观察）: [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/1e8370f5-9db8-4d44-8006-bec0238341f8)

（注）本综述引用的多数方法与基准在 AAS 的 2025 年综述条目中被系统梳理；此外，文中对 2024–2025 新兴工作（SeedVR、VideoPainter、SVFR、MambaIRv2、Step-Video-T2V 等）基于其公开摘要/预印本或会议摘要进行归纳与事实性表述，力求准确描述方法核心与实验结论。若需某篇原始论文 PDF 链接或更细致的数值表格对比，我可基于具体目标数据集（如 REDS / Vimeo-90K / RealVSR / VPBench）补充表格化比较。