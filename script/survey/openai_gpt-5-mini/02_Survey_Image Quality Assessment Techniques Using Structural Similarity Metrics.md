引言  
结构相似性（structural similarity）度量自 SSIM 被提出以来一直是全参考（FR）图像质量评估（IQA）的核心基石。近三年（2022–2025）IQA 研究的两个显著方向是：一方面以 SSIM 为代表的结构性度量在多尺度/频域变体与工业标准中继续被改进与分析；另一方面深度学习驱动的“感知度量”与 Transformer 架构出现并逐步替代或补强传统结构性度量以适配生成模型与真实失真分布的评估需求。本文围绕“以结构相似性为核心或受其启发的度量体系”做短而严谨的综述，按方法类别选取每类 3–5 篇 2022–2025 年间及其前后具有代表性的工作，突出问题 / 方法 / 关键结论，并在实验与评价段落抽取跨论文的共性结论与局限，最后给出面向 2025 年前后的研究趋势预测。

方法分类与代表作  
（注：下列每篇介绍 4–6 句，突出研究问题、核心方法与关键实验结论；引用使用检索到的公开页面/论文报道。）

1) 经典结构相似性及其多尺度/域变体（基于 SSIM 的工用改良与分析）  
- Wang et al., SSIM（结构相似性指数，基础工作，2004）——经典工作提出以亮度/对比度/结构三分量建模像素块感知相似度，奠定后续多尺度 SSIM、窗口化与频域变体的理论基石，常作为 FR-IQA 的基线和实际工程中快速可解释的度量。[zh.wikipedia.org](https://zh.wikipedia.org/zh-cn/%E7%B5%90%E6%A7%8B%E7%9B%B8%E4%BC%BC%E6%80%A7)  
- MS-SSIM / CW‑SSIM（多尺度与复小波变体，综述条目与后续比较中经常出现）——通过多尺度金字塔或复小波域处理以缓解尺度/平移敏感性；在许多合成失真数据上能显著优于单尺度 SSIM，但对复杂纹理与生成性失真仍存在局限（对几何错位与纹理重采样不鲁棒）。（见综述与数据库比较）[fx361.com](https://m.fx361.com/news/2022/0523/11066226.html)

2) 结构+纹理统一度量：DISTS 及延伸（兼顾结构信息与纹理容忍）  
- Ding et al., DISTS（Deep Image Structure and Texture Similarity，2020/后续发表）——针对“纹理重采样下传统相似度失效”的问题，提出在预训练 CNN 特征上分离结构（相关系数类）与纹理（通道均值统计）分量并在多尺度加权融合；引入纹理不变性正则以提升对纹理 resample 与轻微几何变换的容忍性。实验显示相较于 SSIM/LPIPS 等，DISTS 在纹理相似集合与存在几何偏差的 FR 任务上更接近人类判断（对纹理重采样场景改进显著）。[blog.csdn.net/PixelMind](https://blog.csdn.net/PixelMind/article/details/148381735)  
- 相关后续（基于 DISTS 思想的损失或评价扩展）——将结构/纹理分离思想用于训练感知损失或作为 SR / 复原网络的目标，可在保留纹理多样性的同时避免对像素对齐的硬性依赖（见 DISTS 原文与多任务优化讨论）。[blog.csdn.net/PixelMind](https://blog.csdn.net/PixelMind/article/details/148381735)

3) 学习型感知度量（深度特征 + 统计 / 监督学习）  
- Zhang et al., LPIPS（CVPR 2018）——提出使用在 ImageNet 上预训练网络中间层的特征差异并以感知相关的权重学习，使得度量能更好捕捉高层语义/纹理差异；在图像生成/重建任务（GAN、超分等）上对主观判断的相关性明显高于 SSIM/PSNR。  
- Bosse et al., Deep IQA（TIP 2018）——端到端学习: 将 CNN 直接学习从图像（或 patch）到质量分数的映射，设计局部到全局的池化策略（weighted pooling）来模拟人类的注意权重；在多数据集混合训练时显示出对真实失真更好的泛化性（需大量标注）。[m.fx361.com](https://m.fx361.com/news/2022/0523/11066226.html)  
- 近年代表性改进（排名学习 / 对比学习 / 不确定性建模）——为解决标注稀缺与主观分数噪声，研究者引入排序损失、分布回归或不确定性建模（分数分布学习），这些方法在跨数据集迁移和处理真实失真时获得更稳定的秩相关性能（见综述比较）。[fx361.com](https://m.fx361.com/news/2022/0523/11066226.html)

4) Transformer 与多尺度 / 多视角深入建模（2021 起快速发展，2022–2025 持续涌现）  
- TRIQ / IQT / MUSIQ（Transformer/多尺度 Transformer 驱动的 IQA）——以 Transformer 的自注意力替代或补充 CNN 特征提取，可直接处理不同分辨率/长宽比的图片输入并建模全局相关性；公开报告与竞赛（NTIRE/Perceptual IQA）显示 Transformer 架构在 FR/NR 赛道上多次进入前列，尤其在跨尺度与复杂生成性失真上展现更优的跨域泛化能力。[m.fx361.com](https://m.fx361.com/news/2022/0523/11066226.html)  
- 代表性思路：用 Vision Transformer 作为特征骨干 + Siamese / 多视图融合或相对排序 loss 来增强稳定性；实证上对 AIGC 生成图像和高分辨率场景有更一致的主观相关性（但计算与部署代价显著上升）。[devpress.csdn.net](https://devpress.csdn.net/v1/article/detail/79955454)

5) 内容/场景感知的专用 IQA（立体、全景、屏幕内容等）——结构性度量的内容适配  
- 全景（Omnidirectional）与立体（stereoscopic）IQA：为建模视口采样、沉浸/立体感，近期工作提出以视口采样 + 视口间特征交互（Transformer/GNN）或立体双目交互模块作为 NR-OIQA / NR-SIQA 的核心；公开评测显示把显著性/视口概率与几何/深度信息结合比通用度量更贴近主观评分。[signal.ejournal.org.cn](https://signal.ejournal.org.cn/article/doi/10.12466/xhcl.2025.04.016)  
- 屏幕内容图像（SCI）IQA：屏幕内容混合文本与图像，研究提出区分文本/图像区域并使用不同特征与自适应权重融合的策略（局部结构 + 全局亮度/对比统计），在 SCI 专用数据集上 SROCC/PLCC 提升明显。[www.oejournal.org](https://www.oejournal.org/oee/cn/article/doi/10.12086/oee.2025.240309?viewType=HTML)  
- MPCC（基于对比感知的定义，Yao & Shen, Acta Phys. Sin., 2020）——将人眼对比感知与灰度梯度共生矩阵结合，提出面向对比感知的 IQA 定义并在 LIVE/CSIQ/TID 数据上给出 PLCC 范围（0.8616–0.9622），展示了以对比度建模为核心的结构性策略在传统数据集中的竞争力。[wulixb.iphy.ac.cn](https://wulixb.iphy.ac.cn/article/doi/10.7498/aps.69.20200335)

实验与评价总结（跨论文的共性结论）  
- 评价指标与基准：PLCC、SROCC、RMSE 仍为主流；研究者普遍在 LIVE / CSIQ / TID2008 / TID2013 / KADID 等多数据集上报告数值以证明方法稳健性，但“合成失真 vs. 真实失真”的分布差异导致跨库泛化能力成为更重要的评价维度（在多论文对比中明显）。[aas.net.cn](https://www.aas.net.cn/cn/article/doi/10.16383/j.aas.c201030)  
- 结构性度量（SSIM 及其变体）优点：解释性好、计算简单、在轻度退化（平滑/噪声/模糊）下稳定；缺点：对纹理重采样、几何错配与生成性失真（GAN 伪结构）相关判断失准。DISTS 通过在特征域分离结构/纹理，部分缓解了这些缺陷，但仍依赖预训练特征的语义偏好。[blog.csdn.net/PixelMind](https://blog.csdn.net/PixelMind/article/details/148381735)  
- 学习型感知度量（LPIPS、Deep IQA、Transformer-based）在复杂生成性失真与高语义差异场景（超分 / GAN / 复原）上与主观判断相关性更高，但代价是：需大量多样化标注、训练容易过拟合特定标签分布、对抗性或域漂移下性能下降。为此，排序学习、分布式标签与元学习（MetaIQA / 终生学习）被提出以提升跨域稳健性。[fx361.com](https://m.fx361.com/news/2022/0523/11066226.html)  
- 专用场景（全景/屏幕/立体）：将结构性度量与视口/显著/深度信息结合，在专用数据库上显著超越通用度量；说明“结构相似性”需要与内容模型耦合才能服务好特定应用（VR/SCI/3D）。[signal.ejournal.org.cn](https://signal.ejournal.org.cn/article/doi/10.12466/xhcl.2025.04.016) [www.oejournal.org](https://www.oejournal.org/oee/cn/article/doi/10.12086/oee.2025.240309?viewType=HTML)

趋势与挑战（对 2025 年前后研究的实证预测；至少三点，均基于文献与综述归纳）  
1) 混合型度量将成为主流：结构相似性仍作解释性核心（尤其在工程约束场景），但要与深度语义特征或纹理统计“显式耦合”（例如 DISTS 风格或结构+纹理分量）以获得对生成图像和纹理重采样的鲁棒性；因此未来会出现更多“可解释的学习型度量”——可分解为结构分量与学习分量并且在训练时保留可解释约束。参考：DISTS、MPCC、LPIPS。[[PixelMind]](https://blog.csdn.net/PixelMind/article/details/148381735) [[wulixb]](https://wulixb.iphy.ac.cn/article/doi/10.7498/aps.69.20200335)  
2) 数据与标注范式从单值 MOS 向分布化/对比性标签转变：为缓解主观分数噪声与跨域差异，排序学习、概率分数建模与不确定性量化（预测分数分布或置信度）将成为评估与训练的常态，尤其用于真实失真与 AIGC 场景。该趋势已见于近年多任务/元学习和分布回归工作（综述中多篇论文提出混合训练与不确定性建模）。[[fx361.com]](https://m.fx361.com/news/2022/0523/11066226.html)  
3) 结构度量在专用媒体（360°/立体/SCI）上的“内容适配”将常态化：通过视口概率、双目交互或文本/图像区域自适应权重来修正全局结构度量，使其在沉浸式与屏幕内容上与主观相关性提升（见 2025 年的 OIQA、SCI 文章）。[[signal.ejournal.org.cn]](https://signal.ejournal.org.cn/article/doi/10.12466/xhcl.2025.04.016) [[oejournal.org]](https://www.oejournal.org/oee/cn/article/doi/10.12086/oee.2025.240309?viewType=HTML)  
4) 计算/部署折衷：Transformer 与大模型虽在跨尺度建模上有效，但工程部署（移动/边缘）受限；因此轻量化、蒸馏与可解释的蒸馏目标（将结构性分量作为蒸馏先验）会成为方法工程化的重点（研究与实际落地并行）。  
5) 基准与对比方法标准化的需求加剧：由于合成/真实/生成失真类型日益混杂，社区对大规模、覆盖 AIGC 的主观数据库和统一评测协议的呼声与工作将增多（跨数据库稳定性成为重要比较指标）。

结论  
围绕“结构相似性”发展的 IQA 研究在 2022–2025 年呈现出两条并行且互补的路线：一条是继续打磨 SSIM 系列在多尺度/频域与应用场景下的可解释度量（并与纹理统计相结合），另一条是以深度/Transformer 为代表的学习型感知度量来对抗生成与真实失真分布。当下的研究重点应放在将结构可解释性与学习型泛化能力有机结合、采用分布化标签与不确定性建模改进训练稳健性，并在专用媒体（全景、立体、屏幕）中做内容自适配。期望未来研究同时解决可解释性、泛化与部署三者的平衡，以实现工业可用且与人类主观一致的图像质量度量体系。

参考文献（基于检索结果与论文报道；按出现顺序列出可检索来源）  
- [zh.wikipedia.org](https://zh.wikipedia.org/zh-cn/%E7%B5%90%E6%A7%8B%E7%9B%B8%E4%BC%BC%E6%80%A7) — SSIM 条目（含 Wang et al. 2004 引用）  
- [blog.csdn.net/c9Yv2cf9I06K2A9E](https://blog.csdn.net/c9Yv2cf9I06K2A9E/article/details/146492936) — 2025 IQA 综述（指向 arXiv:2502.08540）  
- [blog.csdn.net/PixelMind](https://blog.csdn.net/PixelMind/article/details/148381735) — DISTS 专题讲解（链接至 arXiv/代码）  
- [wulixb.iphy.ac.cn](https://wulixb.iphy.ac.cn/article/doi/10.7498/aps.69.20200335) — Yao & Shen, “基于图像内容对比感知的图像质量客观评价”(Acta Phys. Sin., 2020; MPCC 模型与数据库实验结果)  
- [signal.ejournal.org.cn](https://signal.ejournal.org.cn/article/doi/10.12466/xhcl.2025.04.016) — 2025 年文章：基于立体感感知的全景图像质量评价算法（Omnidirectional IQA 专用方法）  
- [www.oejournal.org](https://www.oejournal.org/oee/cn/article/doi/10.12086/oee.2025.240309?viewType=HTML) — 2025 年文章：基于多任务注意力机制的无参考屏幕内容图像质量评价（MTA‑SCI）  
- [m.fx361.com](https://m.fx361.com/news/2022/0523/11066226.html) — 2022 年综述（《图像质量评价研究综述》节选，含大量方法/数据库罗列）  
- [www.aas.net.cn](https://www.aas.net.cn/cn/article/doi/10.16383/j.aas.c201030) — 2022 年综述：模糊失真图像无参考质量评价综述（AAS）  
- [blog.csdn.net/bby1987](https://blog.csdn.net/bby1987/article/details/109373572) — PSNR/SSIM/MSE 技术笔记（实现与公式推导；用于方法对比背景）  
- [devpress.csdn.net](https://devpress.csdn.net/v1/article/detail/79955454) — TRIQ/Transformer‑based IQA 等入门资料（指向相关论文与代码）  
- [download.csdn.net](https://download.csdn.net/download/weixin_42116604/18354125) — CNNIQA（CVPR/TIP 早期学习型 NR‑IQA 实现参考）  
- [blog.csdn.net/PixelMind/article/details/148371087](https://blog.csdn.net/PixelMind/article/details/148371087) — 更广的 IQA 专题综述与方法归纳（含 LPIPS / DISTS / SSIM 比较）

（注）本文所有方法/结论均基于以上可检索文献与公开综述的归纳；文中所列代表作与方法论述力求紧贴原文提出的问题、核心设计与公开实验结论，避免未经证实的量化主张。若需我将文中每一项所指的“原始论文 PDF / arXiv / 正刊页码”列出具体 DOI 与链接，我可以基于上述检索结果逐条展开并给出原始论文引用条目。