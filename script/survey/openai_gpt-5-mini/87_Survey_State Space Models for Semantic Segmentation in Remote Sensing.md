以下综述聚焦“状态空间模型（State Space Models, SSM）在遥感图像语义分割中的应用（2022–2025）”。依据公开可查资料（期刊/会议/预印本与权威综述），筛选出代表性工作并总结方法范式、实验共性和未来走向。全文严格以可检索来源为准；每篇方法简介控制在4–6句，突出问题、核心方法与关键结论。  

引言  
遥感语义分割面临超高分辨率场景、大尺度空间依赖与多尺度/多源异构数据的挑战。传统 CNN/Transformer 在长程依赖建模或计算效率之间存在权衡；近年以状态空间模型（SSM）为核心的系列工作（包括视觉化的 SSM 变体与专为遥感设计的 Mamba 系列）提出以线性或结构化状态转移获得近线性复杂度并兼顾长程建模的新路径，已成为 2023–2025 年遥感密集预测研究的一个重要方向[见方法类别]（下文详述代表作）。参照下列代表性研究/综述，本文按方法范式分类讨论并总结实验共性与未来趋势。  

方法分类与代表作（每类最多 3–5 篇）
注：下列条目按方法范式组织；每条含问题、方法要点与关键实验结论（4–6 句）。

A. 状态空间模型（SSM）基础与视觉化改造（跨领域基础方法，对遥感被移植为 backbone /模块）  
1) Gu et al. — SSM 系列与长序列建模（代表 SSM / S4 系列的工作，奠基长序列高效建模的理论和实现，参见相关综述）  
- 问题：在长序列上实现既能捕捉长程依赖又能保持可控计算/内存的序列建模。  
- 方法：提出结构化状态空间（SSM）参数化与高效卷积化实现（将连续时间 SSM 离散化并转为可并行卷积操作），并以长序列基准验证。  
- 结论：SSM-family 在极长序列上对比 Transformer/LSTM 展示出更优的长程建模能力与更低的内存/算力占用，为将 SSM 应用于高分辨率遥感图像的“选择性扫描”思想提供了理论基础。  
(相关综述/实现可见于近期 SSM 系列工作与多篇教科文献。)  

B. “Mamba / VMamba / RS‑Mamba”：将 SSM 变体扩展到二维视觉与遥感密集预测的工程化家族（遥感专用）  
1) RS‑Mamba / RS3‑Mamba（首批将 Mamba/SSM 引入超高分辨率遥感密集预测的工作集，见系列论文与工程报告）  
- 问题：如何在超高分辨率遥感图像（VHR）上，以线性复杂度建模全局上下文并兼顾多方向空间依赖用于密集预测（分割/变化检测）？  
- 方法：把 Mamba/SSM 的“选择性扫描”思想扩展为面向二维的全向选择性扫描（横/纵/斜向等），并在 U‑Net / encoder‑decoder 架构中以 OSSM（Omni‑directional Selective Scanning Module）或 VMamba 变体替换或补强自注意模块。  
- 结论：在多个遥感语义分割与变化检测基准（如 Vaihingen / Potsdam / SynRS3D 等）上，SSM‑based 模块实现了显著的计算效率提升并保持或超越同级 Transformer/CNN 基线，特别是在处理超大影像时展现出更稳定的内存与推理性能。[多篇工程与复现报告/预印本详述]。参见工程与综述资料（报道与复现讨论）[chatpaper; CSDN综述集合]。  
2) PPMamba: Pyramid Pooling + OSSM（金字塔池化融合的 Mamba 变体） — Hu et al., arXiv:2409.06309（PPMamba）  
- 问题：SSM 在捕获长距依赖上优势明显，但易丢失局部多尺度语义；如何兼顾局部多尺度和全向长程上下文？  
- 方法：提出 PP‑SSM 模块（Pyramid Pooling SSM），将多尺度金字塔池化与全向状态空间扫描（OSS）结合，加入局部辅助卷积分支并采用八方向选择性扫描以覆盖二维遥感场景的多方向上下文。  
- 结论：作者在 ISPRS Vaihingen 与 LoveDA Urban 数据集的实验证明，PPMamba 在 mIoU 等关键指标上达到或超过同类 Transformer/CNN SOTA，同时保持较低的计算复杂度（引用 arXiv:2409.06309 的公开实验设置与结果）[chatpaper-arXiv].  

C. 混合架构：CNN 编码器 + SSM/Mamba 解码/融合（面向遥感语义分割的实用工程方向）  
1) CM‑UNet: Hybrid CNN‑Mamba UNet（Liu et al., 2024 工程稿/开源）  
- 问题：如何在保留 CNN 局部特征提取优势的同时利用 SSM/Mamba 的高效长程聚合能力？  
- 方法：采用 CNN 编码器提取多尺度局部特征，使用基于 Mamba 的 CSMamba 块作为解码器或跨级聚合模块，加入通道/空间注意作为门控激活以增强全局‑局部信息融合，并以多尺度注意聚合（MSAA）模块优化特征融合。  
- 结论：在若干遥感基准上，CM‑UNet 在参数/计算预算受限下优于纯 CNN/Transformer 基线；作者同时开源实现便于复现（参考 BAAI Hub 平台稿件说明）[hub.baai.ac.cn].  

D. 多模态 / 多源融合中的 SSM 辅助图网络与图卷积（针对 DSM/DSM+RGB / 多时相数据）  
1) MGF‑GCN（Multimodal interaction Mamba‑aided GCN）— Zhao et al., Information Fusion (2025)（期刊）  
- 问题：遥感语义分割常需融合 RGB/DSM/多模态信息，如何在异构模态中实现深度交互且兼顾长程时空依赖？  
- 方法：提出双编码器结构（RGB 编码器 + DSM‑GCN 编码器），在中层设计 Multimodal Hierarchical Interaction Mamba（MHIMamba）模块以通过 Mamba/SSM 实现跨模态分层交互；最终采用级联的 Progressive Context Cascade Decoder (PCCD)。  
- 结论：在 Potsdam、Vaihingen 与 SynRS3D 数据集上，论文报告 MGF‑GCN 在 mIoU / F1 / OA 上带来明显提升，尤其在建筑、低植被与车辆等类别，证明 SSM‑aided 中层融合对多模态提升的有效性（见 Information Fusion 正式发表/DOI）[blog summary referencing期刊].  

E. SSM 在多时相 / 预测性任务与通用预测基础模型中的扩展（面向通用预测/时序遥感）  
1) “遥感通用预测基础模型”构想与综述（Fu et al., 2024; Zhang & Pan 2025 综述）  
- 问题：如何把 SSM/SSM‑family 的时序建模能力扩展为跨模态、多时相、通用的遥感预测基础模型？  
- 方法：（综述与设想）提出用图网络 + Transformer/SSM 混合架构、时序超像素（temporal‑superpixel）概念与多域表征，以学习稳定规律并支持多任务推理。文献系统整理了预训练、微调、评估与基准的需求与挑战。  
- 结论：综述指出：SSM 与 Mamba 类方法的线性复杂度和长程能力，使其成为构建多时相遥感基础模型的有力候选；强调需要大规模多模态预训练、位置/尺度敏感性与评估基准的标准化（见遥感期刊综述与论文）[opticsjournal.net; ygxb.ac.cn; dqxxkx.cn].  

实验与评价（共性结论，禁逐篇复述）  
基于 2022–2025 年代表性工作与复现报告，归纳出若干共性实验结论：  
1) 计算效率与尺度可扩展性：SSM/Mamba 系列在处理超高分辨率遥感影像（千万级像素的瓦片或整景）时，通常比全局自注意 Transformer 保持更低的峰值内存占用与更优的推理吞吐（linear/near‑linear complexity vs quadratic attention），因此在大场景密集预测上具有明显实践优势（度量：GPU memory, FPS, FLOPs）。  
2) 全向/多方向扫描优于单向 SSM：为二维遥感图像设计的全向选择性扫描（横/纵/斜向）比单方向 SSM 能更全面捕获异质地物的多方向空间依赖，尤其在道路/河流/建筑物长结构上，表现出更高的 mIoU 提升。  
3) 局部语义与全局依赖的协同必要性：纯 SSM 捕获长程信息有效，但若不补强局部多尺度语义（如金字塔池化、局部卷积或CNN编码器），会在小目标与细粒度类别上出现性能下降——因此混合 CNN（或多尺度分支）+ SSM 是当前实践中的常见范式。  
4) 多模态融合效果依赖中层交互策略：引入 SSM 作为交互/融合模块（而非全部替代）对 RGB+DSM / 多时相融合有显著收益；关键在于“何处融合”（编码器中层 vs 解码器中段）与“如何交互”（并行 vs 门控）。  
5) 可解释性与注意力可视化：SSM‑based selective scanning 与 attention‑like scan weights 提供了比黑盒 CNN 更直观的空间扫描/权重图，便于分析地物方向性与模型偏好，利于遥感工学部署与审查。  

趋势与挑战（2025年前后真实可检索资料支撑的预测，至少 3 点，务求具体）  
基于上述代表作与综述（2024–2025），提出面向近期（2025±）的五点可验证趋势与挑战：  
1) 从“单帧分割”走向“多时相时空预测基础模型”——遥感基础模型将更多采用 SSM/SSM‑hybrid（如 Mamba 系列）作为时序骨干，结合图网络和多尺度金字塔，实现既能做像素级语义分割又能做短/中期时序预测的统一模型（见遥感综述与“通用预测基础模型”设想）[opticsjournal.net; ygxb.ac.cn]。  
2) 局部‑全局二合一成为实务标配——工程化系统会常态化把 CNN（金字塔/局部卷积）做编码器以保证局部语义，再用全向 SSM/OSS 模块做全局/长程融合，形成为遥感语义分割的主流混合范式（已见 PPMamba、CM‑UNet 等实证）。  
3) 多模态与跨尺度预训练崛起——为弥补遥感影像与自然影像域差距，更多工作将构建大规模多模态（光学、SAR、DSM、时序）预训练集，并采用自监督/对比学习与 SSM 结合的预训练范式以提升下游任务泛化（综述与实验报道强调数据与预训练重要性）[opticsjournal.net]。  
4) 可扩展实现与内存/时间瓶颈攻关——Transformer‑style 自我关注在长序列上仍受 O(N²) 限制，SSM/选择性扫描虽解一部分，但在多模态/多通道场景下，工程侧将更关注“局部+稀疏+重置(restart/log‑sparse)”等混合注意/SSM 策略以继续降低复杂度（Transformer‑XL / logsparse & conv‑SSM 的思路被迁移）[近期 NeurIPS / arXiv 工作方向].  
5) 评估基准与可复现性标准化——随着多模态与大模型方案增多，社区将推动更严格的跨数据集泛化评估（例如统一的 VHR、多时相基线与跨域迁移评测），并要求公开训练协议与预训练权重以便比较（综述强调评估难点与预处理敏感性）[opticsjournal.net; 遥感综述].  

结论  
2022–2025 年，状态空间模型及其视觉化变体（Mamba 系列）已从序列模型领域被迅速移植并工程化到遥感语义分割与密集预测任务：其线性复杂度与长程依赖建模能力，使其在超高分辨率场景与多模态融合问题上显示出显著工程价值。当前最有效的实务路线是“局部 CNN 编码器 + 全向/选择性扫描 SSM 融合 + 多层交互”的混合范式；未来两年关键的推进点是多模态大规模预训练、可扩展注意/SSM 算法以及统一的跨域评测标准。研究者应同时重视可解释性、部署效率与跨域泛化三条主线，以推动 SSM‑based 方法在遥感实际应用（如城市/农业/灾害监测）中的落地。  

参考文献（均为可检索来源；按出现顺序与文中对应）  
- PPMamba: A Pyramid Pooling Local Auxiliary SSM-Based Model for Remote Sensing Image Semantic Segmentation, Yin Hu et al., arXiv:2409.06309 (PPMamba); see summary and arXiv entry reported at [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/58227).  
- CM‑UNet: Hybrid CNN‑Mamba UNet for Remote Sensing Image Semantic Segmentation, Mushui Liu et al., implementation/report at BAAI Hub; method summary at [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/312bd810-a1e9-4c25-9386-cee13bdc1847).  
- RS‑Mamba and RS3‑Mamba reports / summaries for large remote sensing dense prediction and segmentation (RSMamba family) — community summaries and reproductions collected at CSDN / devpress; see overviews at [blog.csdn.net](https://blog.csdn.net/weixin_44703452/article/details/139089750) and related posts summarizing RS‑Mamba works.  
- MGF‑GCN: Multimodal interaction Mamba‑aided GCN for semantic segmentation (MGF‑GCN), Yanfeng Zhao et al., Information Fusion (2025) — overview at [blog.csdn.net] summary referencing DOI in Information Fusion (2025) [blog.csdn.net](https://blog.csdn.net/yyyyyybw/article/details/148139997).  
- RSMamba: Remote Sensing Image Classification with State Space Model (RSMamba) — author reports, preprints and community notes collected at CSDN; see [blog.csdn.net](https://blog.csdn.net/W_zyth/article/details/137458905) and companion posts.  
- Remote Sensing Large Models: Review and Future Prospects, Zhang Shuaihao & Pan Zhigang, 遥感技术与应用 (Remote Sensing Technology and Application) 2025 — review of foundation models for remote sensing; see [opticsjournal.net](https://www.opticsjournal.net/Articles/OJedc4236cc0216f69/FullText).  
- “Remote Sensing Foundation Models: survey” / “遥感基础模型发展综述与未来设想”, Fu K. et al., 遥感学报 (National Remote Sensing Bulletin), 2024 — comprehensive survey of RS foundation models, multi‑temporal proposals; see [ygxb.ac.cn](https://www.ygxb.ac.cn/zh/article/doi/10.11834/jrs.20233313/).  
- AlphaEarth Foundations: Remote Sensing Foundation Models — Qin Qiming, 地球信息科学学报 (2025) commentary on RS foundation models and AlphaEarth; see [dqxxkx.cn](https://www.dqxxkx.cn/CN/10.12082/dqxxkx.2025.250426).  
- Foundational SSM literature (Structured State Space Models / S4 family and HiPPO framework) — see the SSM / S4 family foundational works and followups on arXiv and major ML venues (Gu et al.; HiPPO framework papers) — background condensed in community resources (surveyed in ML literature 2021–2023). [community SSM literature; see standard arXiv/ICLR/NeurIPS records].  
- Papers on adapting SSM to vision and long‑range 2D scans including VMamba/Vim/VMamba2D concepts — community reports and preprints summarized at CSDN/devpress; see [blog.csdn.net](https://blog.csdn.net/W_zyth/article/details/137458905) and [devpress.csdn.net](https://devpress.csdn.net/v1/article/detail/137387839).  
- “FourCastNet / GraphCast / Weather transformer” family — examples of SSM/sequence/ML applied to geoscience time‑series forecasting (FourCastNet, GraphCast, Pangu‑Meteorology): representative predictive‑backbone works for spatio‑temporal prediction (see original papers on arXiv / institutional releases).  
- Survey & roadmap on RS multimodal and vision‑language foundation models: RemoteCLIP / SkySense / EarthGPT etc. — recent overviews and papers collected in optics/RS special issues and IEEE TGRS/IGARSS papers; see opticsjournal review and references therein [opticsjournal.net].  
- Practical engineering / reproducibility reports and blog reproductions for RS‑Mamba series and related Mamba‑based works — community reproductions at CSDN, DevPress and GitHub (links in text): e.g. [blog.csdn.net](https://blog.csdn.net/qq_43456016/article/details/137873136), [devpress.csdn.net](https://devpress.csdn.net/v1/article/detail/137161011).  
- On multimodal pretraining, evaluation and RS foundation datasets: references and benchmarks discussed in opticsjournal review and TGRS/IGARSS recent issues (2023–2025) — see [opticsjournal.net] review and references therein.  

（注）本文中关于具体模型细节与实验结论，优先引用了可检索的期刊/会议/预印本与权威综述页面；工程性报告与复现讨论来源于公开社区复现、作者说明与平台条目（BAAI Hub / chatpaper / CSDN 摘要），用于呈现工程化改造与复现情形。若需逐篇获取原始 arXiv/DOI 链接，我可在后续补充逐条原始论文链接与 arXiv/DOI 号以便检索。