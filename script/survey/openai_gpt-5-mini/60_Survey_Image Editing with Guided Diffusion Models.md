引言  
近年来，基于扩散模型（diffusion models）的图像编辑成为视觉生成与交互的重要方向。与以往基于GAN或自回归的方法不同，扩散模型以逐步去噪的生成过程天然支持条件化引导（text / mask / layout / exemplar 等），从而催生了多类编辑范式——从整体语义变换到实例级插入与精确掩码修复。本文聚焦 2022–2025 年代表性工作，按方法类别归纳每类 3–5 篇核心论文，评述其问题设定、方法要点与关键实验证据，随后总结不同方法的共性实验结论并给出未来 2–3 年的研究趋势与挑战。全文力求紧凑、可验证（引用均为公开论文或综述），便于科研与工程参考。

方法分类与代表作  
说明：每篇论文后附与该论文或其综述在本次检索中的来源链接，便于阅读原文或综述背景。

A. 文本/条件引导与无分类器引导（Text-/condition-guided editing）  
- GLIDE — “GLIDE: Towards Photorealistic Image Generation and Editing with Text-Guided Diffusion Models” (OpenAI, 2022)  
  研究问题：将文本条件用于高质量图像生成与图像内局部编辑（text-guided inpainting/editing）。  
  核心方法：在条件扩散框架中采用 classifier-free training（同时训练有条件与无条件模式）并在采样时用线性组合放大条件影响；提出文本条件与输入图像的联合编码以实现编辑。  
  关键结论：在人类评估与文本-图像对齐上显著优于早期方法，且通过无条件/有条件的插值实现可控的区域编辑（可参见相关综述与博客说明）[blog.csdn.net](https://blog.csdn.net/c9Yv2cf9I06K2A9E/article/details/124641910)。  

- DALL·E 2 / unCLIP — “Hierarchical Text-Conditional Image Generation with CLIP Latents” (Ramesh et al., 2022)  
  研究问题：如何把文本语义更健壮地映射为图像以提升文本引导的编辑精度与多样性。  
  核心方法：引入一个先验模块将文本映射到 CLIP image embedding（或用 diffusion/autoregressive prior），再由 decoder（基于扩散）将该 embedding 解码为图像；支持基于 CLIP 向量的图像编辑与重构。  
  关键结论：通过在语义嵌入层进行控制（而非直接在像素级），改善了对复杂指令的理解与多样化生成能力（参见综述中对 DALL·E 2 的讨论）[blog.csdn.net](https://blog.csdn.net/c9Yv2cf9I06K2A9E/article/details/124641910)。  

- Classifier-free guidance（核心技术与分析）  
  研究问题：如何在不训练额外分类器的情况下，增强条件一致性而不损害样本质量。  
  核心方法：训练时随机丢弃条件使模型既能做有条件预测也能做无条件预测；采样时按比例放大（有条件预测 − 无条件预测）实现若干倍的条件强化。  
  关键结论：该技术已成为文本/标签引导扩散模型的标准策略，可在保持模型结构简单的同时显著提升条件对齐（见多篇综述对此方案的总结）[jcst.ict.ac.cn](https://jcst.ict.ac.cn/cn/article/cstr/32374.14.s11390-024-3814-0)。

B. 掩码内/局部编辑与 inpainting（Mask-based / local editing）  
- Palette — “Palette: Image-to-Image Diffusion Models” (Saharia et al., 2022)  
  研究问题：统一多种图像修复 / 翻译任务（inpainting、outpainting、色彩/风格迁移）在单一扩散框架下的解决方案。  
  核心方法：将多种 image-to-image 任务转为条件扩散问题，设计任务感知的条件编码与级联超分/修复模块；在潜空间与像素空间间兼顾质量与效率。  
  关键结论：在一组标准视觉编辑任务上（包括细粒度 inpainting 和风格变化），Palette 在保持结构一致性的同时达到了比早期 GAN/重构方法更好的文本/图像一致性（综述与实验说明见多篇 survey）[blog.csdn.net](https://blog.csdn.net/SmartLab307/article/details/138166955)。  

- Iterative Inpainting / Diagnostic Benchmark — Cho et al. (2023)  
  研究问题：在训练分布外（OOD）或极端布局下，如何通过迭代局部填充提高编辑可靠性。  
  核心方法：把多目标/复杂布局的编辑分解为序列化的局部 inpainting 子任务（逐个物体或区域生成并合成），并提供诊断基准评估失败模式。  
  关键结论：在极端布局与密集物体场景下，逐步局部生成显著提高了布局服从性与语义保真，尽管代价是多个采样过程与更高延迟（详见布局综述）[hanspub.org](https://pdf.hanspub.org/csa2025154_451543569.pdf)。  

- Paint by Example — “Paint by Example: Exemplar-based Image Editing with Diffusion Models” (Yang et al., 2022)  
  研究问题：如何使用 exemplar（参考图像）精确控制编辑目标的外观（例如纹理或风格迁移）而非仅凭文本。  
  核心方法：在扩散训练中引入信息瓶颈与强增强，设计任意形状的 exemplar mask 并利用 classifier-free guidance 增强 exemplar 相似度，引入约束防止直接复制粘贴伪影。  
  关键结论：在保真度与 exemplar 相似性之间取得更好平衡，支持单次前向的高质量编辑而无需迭代优化（参见 zhuanzhi.ai 汇总）[zhuanzhi.ai](https://www.zhuanzhi.ai/paper/2bdb0122df0b032da95290c3fd0a8147)。

C. 布局 / 实例级控制（Layout- / instance-level control）  
- GLIGEN — “GLIGEN: Open-Set Grounded Text-To-Image Generation” (CVPR 2023)  
  研究问题：如何在预训练文本到图像模型中加入开放集的实例级定位（用户给出边界框 + 描述）而不破坏原有模型的语义能力。  
  核心方法：在预训练 Stable Diffusion 内插入可训练的门控 cross-attention 层（或 adapter），在保持大模型权重冻结的前提下学习将框/位置信息注入采样早期。  
  关键结论：实现了零样本或少监督的实例级插入，比单纯在提示中拼接位置信息更稳健；保留了预训练模型的通用概念（见布局综述）[hanspub.org](https://pdf.hanspub.org/csa2025154_451543569.pdf)。  

- ControlNet — “Adding Conditional Control to Text-to-Image Diffusion Models” (ICCV 2023)  
  研究问题：提供一种通用机制把任意结构化条件（边缘、深度、姿态、分割图）与预训练扩散模型耦合，以实现高保真控制。  
  核心方法：复制一份 UNet 作为条件分支（condition branch），该分支接收外部结构信号并在多尺度层注入与主网络相同形状的特征，训练时冻结主模型仅优化条件分支。  
  关键结论：支持多种控制信号的模块化插拔，能在不微调主模型的情况下实现强约束生成（详见综述）[hanspub.org](https://pdf.hanspub.org/csa2025154_451543569.pdf)。  

- InstanceDiffusion (CVPR 2024) — “Instance-level Control for Image Generation” (Wang et al., 2024)  
  研究问题：对图像中每个实例提供自由形式文本 + 灵活位置（点/涂鸦/框/掩码）条件，避免属性泄漏与跨实例混淆。  
  核心方法：提出 UniFusion 融合模块（格式感知地融合文本与位置）、ScaleU 动态重标定 UNet 特征，以及 Multi-instance Sampler（对每实例先分别去噪再聚合）来减少属性串扰。  
  关键结论：在 COCO/LVIS 等基准上对边界框和掩码的布局/属性绑定指标显著提升；消融显示每个组件均对多实例保真和属性一致性有实质贡献[chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/45330)。

D. 训练-免费或少训练的编辑（training-free / test-time methods）  
- NoiseCollage — “NoiseCollage: A Layout-Aware Text-to-Image Diffusion Model Based on Noise Cropping and Merging” (Shirakawa & Uchida, 2024)  
  研究问题：在不训练额外模块的前提下，如何利用扩散噪声的初始配置直接实现布局约束。  
  核心方法：为每个布局实例生成独立的噪声片段并裁剪嵌入到相应位置，形成“噪声拼贴”作为采样起点；通过单一反向扩散流程完成合成。  
  关键结论：作为零训练成本的推理策略，对位置敏感的实例插入表现稳健，且避免了多次 inpainting 的高开销；但对大量互相遮挡或形状复杂目标的适配仍有局限（见布局综述与方法列表）[hanspub.org](https://pdf.hanspub.org/csa2025154_451543569.pdf)。  

- Training-Free AREdit (2025 arXiv) — “Training-Free Text-Guided Image Editing with Visual Autoregressive Model” (Wang et al., 2025)  
  研究问题：消除对扩散/修正流反演的依赖，实现对原图高保真与局部编辑的快速、无训练流程。  
  核心方法：在自回归视觉模型（VAR）上引入缓存机制记录原图标记分布、自适应细粒度掩蔽与标记重组策略，从而在不需显式反演的情况下限制编辑范围并保持未修改区域。  
  关键结论：在一系列编辑任务上展示了接近或优于基于扩散反演方法的保真与局部性保持，并能实现极快的推理（首运行 2.5s / 1K 分辨率，后续 1.2s），表明训练-免费范式的可行性[chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/125277)。

实验与评价总结（共性结论，2022–2025）  
- 条件强度与保真度的权衡是普遍规律。使用 classifier-free guidance 或类似系数放大会提升条件（文本/布局/掩码）对齐，但通常以一定程度牺牲图像自然度或引入伪影；因此常见做法是在采样过程中调参平衡二者（多篇工作与综述均指出）。  
- 预训练模型 + 轻量适配（adapter / gated attention / ControlNet）被证明在泛化和数据效率上优于从头训练：可在少量训练或零样本下支持开放集概念与复杂控制，但在极端 OOD 布局下仍需推理级技巧（如迭代 inpainting 或 noise initialization）来修正。  
- 多实例/实例绑定问题（属性泄漏、颜色/纹理错配、实例重复）是评价重点：InstanceDiffusion 等方法通过结构性模块与多实例采样策略减少了跨实例混淆，但复杂重叠场景仍表现不稳定。  
- 评测体系趋于多模态与人类主观并重：常用自动指标包括 FID、CLIPScore / CLIP-based retrieval、IoU（掩码对齐）与 APbox，且多篇工作辅以大规模人类偏好测试以衡量文本/掩码/布局与视觉保真的综合表现（各综述对基准与指标的盘点详尽）[hub.baai.ac.cn](https://hub.baai.ac.cn/paper/abe0d958-8a3e-4401-b499-8809f6ded938)。  
- 推理效率与采样步数仍为工程瓶颈：少步 DDIM / DPM-Solver / 蒸馏等技术普遍被采用以降低延迟，但快速采样往往需要与方差学习或蒸馏配合以免牺牲编辑质量；训练-免费方法（如 autoregressive 编辑）提供了另一条速效路径，但在可控性与对复杂指令的鲁棒性上仍有差距。

趋势与挑战（基于 2022–2025 证据的预测，至少 3 点）  
1) 更细粒度的一体化实例控制将成为主流研究方向  
   证据与理由：InstanceDiffusion、GLIGEN、ControlNet 等工作显示了将布局/文本/掩码联合注入主模型的有效性。下一步会更多关注“属性绑定 + 遮挡关系 + 物理一致性”的联合建模（例如跨实例注意力屏蔽、基于几何/层次的实例表示），以减少跨实例信息泄漏并支持复杂场景编辑。  

2) 推理级零训练/少训练方法（noise初始化、局部拼接、缓存+掩码策略）将与预训练适配方法并行发展，形成实用化路径  
   证据与理由：NoiseCollage 与 AREdit 等分别证明了零训练与训练-免费范式在不同约束下的可行性；结合预训练大模型的先验，这类方法能在工程实践中快速部署，因此会有更多工作探索“轻量化推理算子 + 自动参数寻优”的组合。  

3) 更严格的、跨模态的评测基线与任务集合将被建立（涵盖属性绑定、布局服从、风格保持与身份保真）  
   证据与理由：当前研究多依赖混合指标与人类评测，社区已提出多项基准（EditEval / DrawBench / COCO/LVIS 专门任务）；预计未来会出现标准化的多维度评测套件，包含自动和人类评估协议以促进公平比较。  

4) 采样加速与模型蒸馏成为实现实时交互编辑的关键工程方向  
   证据与理由：少步 DDIM、DPM-Solver 与蒸馏（甚至一致性模型）已被证明能在不显著损失质量下减少步数；为了支持交互式设计/艺术创作，研究将聚焦将这些加速技术与控制模块（如 ControlNet）无缝集成。  

5) 可解释性与安全性（滥用防控、版权/隐私）将成为必须考虑的研究议题  
   证据与理由：扩散模型生成能力强、易用于伪造或侵权，研究与产业界将并行发展可控生成策略（如拒绝生成敏感内容、生成来源标注/水印）与透明化手段以满足合规性需求（综述多次提及评估与安全问题）[jcst.ict.ac.cn](https://jcst.ict.ac.cn/cn/article/cstr/32374.14.s11390-024-3814-0)。

结论  
过去三年（2022–2025）中，guided diffusion 在图像编辑领域已形成若干清晰的技术分支：一端是以 classifier-free guidance 与语义先验为核心的文本引导与条件编辑；另一端是以布局/实例/掩码为核心的可控合成；此外训练-免费与噪声拼接等推理策略提供了工程化的快捷路径。总体来看，预训练模型 + 轻量适配 + 推理级技巧的组合被证明在准确性、泛化性与效率之间提供了最有竞争力的折中。未来工作需着力解决实例绑定、时空一致性（视频/动态场景扩展）、评测标准化与实时交互性等问题，以推动从研究样例向稳健工程化应用的过渡。

参考文献（按文中出现顺序，检索来源以供进一步查阅；均为公开论文或综述）  
- GLIDE: 详见综述/博客汇总 [blog.csdn.net](https://blog.csdn.net/c9Yv2cf9I06K2A9E/article/details/124641910)（GLIDE 及相关讨论）  
- Ramesh A., et al., “Hierarchical Text-Conditional Image Generation with CLIP Latents” (DALL·E 2 / unCLIP). 参见综述与 arXiv 讨论 [blog.csdn.net](https://blog.csdn.net/c9Yv2cf9I06K2A9E/article/details/124641910)  
- Classifier-Free Guidance (method discussed in multiple surveys); 概览见 JCST 综述 [jcst.ict.ac.cn](https://jcst.ict.ac.cn/cn/article/cstr/32374.14.s11390-024-3814-0)  
- Palette — Saharia C., et al., “Palette: Image-to-Image Diffusion Models” (论文与综述讨论)；方法与任务统一性见综述 [SmartLab307 summary] [chatpaper/博客汇总] [SmartLab307](https://blog.csdn.net/SmartLab307/article/details/138166955)  
- Cho J., et al., “Diagnostic Benchmark and Iterative Inpainting for Layout-Guided Image Generation” (iterative inpainting; arXiv) — 综述引用见 [hanspub.org](https://pdf.hanspub.org/csa2025154_451543569.pdf)  
- Paint by Example — Yang B., et al., “Paint by Example: Exemplar-based Image Editing with Diffusion Models” (arXiv 2022)；收录与解析见 [zhuanzhi.ai](https://www.zhuanzhi.ai/paper/2bdb0122df0b032da95290c3fd0a8147)  
- GLIGEN — Li Y., et al., “GLIGEN: Open-Set Grounded Text-To-Image Generation” (CVPR 2023)；讨论与引用见布局综述 [hanspub.org](https://pdf.hanspub.org/csa2025154_451543569.pdf)  
- ControlNet — Zhang L., Rao A., Agrawala M., “Adding Conditional Control to Text-to-Image Diffusion Models” (ICCV 2023)；综述与方法细节见 [hanspub.org](https://pdf.hanspub.org/csa2025154_451543569.pdf)  
- InstanceDiffusion — Wang X., Darrell T., Rambhatla S.S., et al., “InstanceDiffusion: Instance-level Control for Image Generation” (CVPR 2024 / arXiv)，摘要与解读见 [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/45330)  
- NoiseCollage — Shirakawa T., Uchida S., “NoiseCollage: A Layout-Aware Text-to-Image Diffusion Model Based on Noise Cropping and Merging” (arXiv 2024)，列入布局综述参考 [hanspub.org](https://pdf.hanspub.org/csa2025154_451543569.pdf)  
- AREdit / Training-Free editing — Wang Y., Guo L., Li Z., et al., “Training-Free Text-Guided Image Editing with Visual Autoregressive Model” (arXiv 2025)；检索与摘要见 [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/125277)  
- 领域综述（可参考以核对基准与更广泛文献）：“A Survey of Multimodal Controllable Diffusion Models” / “Controllable Generation with Text-to-Image Diffusion Models: A Survey” 等，见 [jcst.ict.ac.cn](https://jcst.ict.ac.cn/cn/article/cstr/32374.14.s11390-024-3814-0), [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/abe0d958-8a3e-4401-b499-8809f6ded938) 与相关 arXiv 综述（2402–2406 年文献集合）[u012744245 blog summary / arXiv pointers]。  

注：为保证可验证性，文中所述方法与结论均基于公开论文或综述（上列检索来源）。若需我把每篇论文的 arXiv / 官方 PDF 链接逐一列出（便于直接下载），我可继续整理并补充原文 DOI/ArXiv 链接。