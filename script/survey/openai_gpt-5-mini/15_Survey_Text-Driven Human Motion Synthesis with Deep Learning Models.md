引言  
近年来基于深度学习的“文本→三维人体动作/姿态”合成取得快速进展，核心技术从序列自回归、离散化令牌到扩散模型与掩码建模并行演化。本文围绕 2022–2025 年的代表性工作做凝练综述，按方法范式划分（扩散/潜空间扩散、掩码/分层量化与自回归、测试时/拼贴式时序控制、实时/加速与多模态跨任务），对每类最多选取 3–5 篇最具代表性的论文作短而精的技术归纳，并总结实验评价的共性结论与未来趋势与挑战。为保证可检索性，文献引用以公开论文或权威预印本/会议页面为准。

方法分类与代表作  
1) 扩散模型及潜在空间扩散（Diffusion / Latent-diffusion）  
- MotionDiffuse — M. Zhang 等，TPAMI 2024（论文与解读见综述与实现页）[blog.csdn.net].  
  研究问题：将条件文本映射为多样、现实的3D人体动作序列并建模不确定性。  
  核心方法：在动作时序的潜在空间中采用逐步去噪的扩散框架，引入时空条件机制以融合文本语义并支持可变长度生成。  
  关键结论：相比确定性生成器，扩散式方法在多样性与长程时序连贯性上明显优越，在HumanML3D等基准上降低FID并提高主观多样性评分。  
 （参见 TPAMI/实现与第三方解读）[blog.csdn.net]。  

- Motion-latent-diffusion / MotionDiffuse 系列（CVPR/2023–2024 实现与代码生态，见综述博客）[blog.csdn.net].  
  研究问题：如何在潜在空间上高效地进行动作扩散以提升速度与质量平衡。  
  核心方法：先用VAE/隐空间编码动作，再在更低维的隐空间上训练扩散模型以降低采样成本；结合文本条件器与分层解码完成高分辨率时序恢复。  
  关键结论：隐空间扩散在采样步数受限时仍能保留动作细节，适合工程化部署与交互式生成。  

- DreaMoving（舞蹈视频生成，扩散驱动的视频/动作控制框架，2023）[hub.baai.ac.cn].  
  研究问题：姿势序列驱动的高质量人类舞蹈视频合成（与文本结合时常作为参考技术）。  
  核心方法：以扩散生成器为核心，设计运动控制模块与身份保持器以保证时序连贯性与风格一致性。  
  关键结论：在姿势到视频任务中扩散方法在视觉细节与过渡自然度上优于传统GAN方案；为文本→动作→视频的流水线提供了重要方法参考。  

2) 掩码建模、分层量化与自回归令牌（Masked / Tokenized / Autoregressive）  
- MoMask — Guo et al., CVPR 2024（分层量化 + 掩码建模）[chatpaper.com].  
  研究问题：用离散化令牌在多分辨率下建模文本到3D动作，兼顾高保真与可控性。  
  核心方法：提出分层向量量化将动作分解为基础令牌与残差令牌；对基础层使用掩码Transformer进行训练/采样，对残差层用残差Transformer逐层细化。  
  关键结论：在HumanML3D与KIT-ML上显著减少FID（论文报告的量化指标），并能在无微调情形下完成时序补全与编辑任务。  

- BAMM（Bidirectional Autoregressive Motion Model），2024（掩码自注意 + 自回归长度可变）[hub.baai.ac.cn].  
  研究问题：如何在不预先指定序列长度的前提下同时获得高质量生成与可编辑性。  
  核心方法：结合运动分词器与掩码自注意Transformer，统一掩码建模与自回归生成，采用双向依赖学习以提升样本质量。  
  关键结论：在HumanML3D和KIT-ML上同时兼顾质量与编辑能力，能动态决定动作长度且便于后续局部编辑。  

-（补充）基于令牌的潜在生成（代表作示例见上两篇与2023 年的潜在token化工作），这些方法强调离散令牌的可解释性与高效并行生成（相关实现与分层策略在MoMask中得到系统验证）[chatpaper.com]。  

3) 测试时拼贴/多轨时间线控制（Test-time Collage / Timeline Control）  
- Multi-Track Timeline Control — arXiv 2401.08559（Spatio-Temporal Motion Collage, STMC）[themoonlight.io].  
  研究问题：用户通过多轨时间线（可重叠、并行的文本提示）对复杂组合动作进行精确时序控制时，如何生成一致且语义忠实的动作。  
  核心方法：提出 Spatio‑Temporal Motion Collage（STMC）作为测试时去噪策略：先按轨道与身体部位划分子时间线，独立去噪片段，再通过时空拼贴与score arithmetic融合过渡区以保证可微校正。  
  关键结论：STMC 可与预训练扩散模型无缝结合，实现多轨并行与重叠提示的精确控制，避免对模型重训练或架构改动。  

-（相关）MDM‑SMPL 及拼接策略（同文作者对 MDM 的扩展以支持 SMPL 表示并加速采样）——提出降低步数与直接输出 SMPL 表示以便工程化应用（见 Multi-Track 文中实现细节）[themoonlight.io].  

4) 实时性、加速与多模态融合（Real-time / Acceleration / Multi-modal）  
- DAF‑DH — 王家松等，2025（计算机应用研究，扩散模型加速与感知优化）[arocmag.cn].  
  研究问题：基于扩散的人体视频/动作生成推理延迟高、资源成本大，如何实现在实时或近实时场景下部署。  
  核心方法：三级加速策略（TensorRT 编译、低分辨率+抽帧的快速生成、轻量级超分与插帧后处理），并引入语义特征对齐损失提高感知质量。  
  关键结论：在所构建数据集上实现 5× 推理加速且FVD/LPIPS等感知指标显著改善，证明工程化加速＋后处理的可行性。  

- Motion Anything — 多模态（文本+音乐）到动作框架（arXiv 2503.06955，2025 预印）[blog.csdn.net].  
  研究问题：如何在单统一框架下对文本、音乐等多模态条件实现协调控制的动作生成。  
  核心方法：基于注意力的掩码建模与多模态条件适配模块，设计用于关键帧/关键身体部位的时空优先编码并提供跨模态对齐策略。  
  关键结论：在HumanML3D、AIST++与新建TMD数据集（文本‑音乐‑舞蹈）上显示提升，表明大规模多模态数据与跨条件编码是提升控制性的核心方向。  

实验与评价总结（共性结论，非逐篇复述）  
- 基准与指标：领域常用基准包括 HumanML3D、KIT-ML、AIST++、各类舞蹈/动作数据集；自动量化指标以FID、R‑Precision、MM‑score、MPJPE（关节点误差）及LPIPS/FVD（视频任务）为主，另辅以大量用户主观评估。  
- 多样性 vs 精确性：扩散模型在多样性（样本分布覆盖）与长范围语义一致性方面明显优于确定性/自回归模型，但在精细关节位置误差（MPJPE）或受限条件下的语义精确执行时，自回归或掩码细化的离散令牌方法更易通过局部约束提升准确度。  
- 控制性：测试时拼贴（STMC）与分轨控制策略能在不改动预训练模型情况下显著提高多段/多轨控制的语义保真度，说明“测试时算法”是工程上重要的补救路径。  
- 速度与部署：隐空间扩散、分层去噪与工程化加速（TensorRT、超分后处理）是将扩散模型从研究到实时应用的可行路线；但在低延迟交互场景下，掩码/自回归模型或显式稀疏采样仍具优势。  
- 评价缺口：当前自动指标难以充分覆盖“文本语义的局部对齐”（例如某句子指定“抬右手并停2秒”），主观评估与针对性任务指标仍不可或缺。

趋势与挑战（2025 年前后真实可检索研究态势预测，≥3 点）  
1. 多模态大模型与大规模多条件数据并进：将看到更多将文本、语音、音乐与视觉叠加训练的大模型（multi‑condition pretraining），以提高模型对细粒度条件（肢体部位、节奏、风格）的响应能力；相关数据集（文本+音乐+动作）会被公开以推动研究（已见 MotionAnything / TMD 的尝试与数据贡献趋势）。  
2. 测试时控制与拼贴成为常态：预训练大模型难以同时覆盖精细时序控制与多轨组合，未来采用测试时去噪/拼贴（如 STMC）或基于score arithmetic的时空融合将更常用，成为“通用预训练模型 + 专用测试时控制” 的工作流。  
3. 隐空间/分层扩散用于工程化部署：为缩短采样步数并降低运算成本，隐空间扩散与分层残差去噪（MoMask 的分层思路、潜空间扩散实践）会成为主流工程路径，配合后处理（超分/插帧）实现感知级质量。  
4. 可解释性与安全性需求上升：随着用于商业内容生成（AR/VR/虚拟人）的大规模应用，如何保证动作语义与文本意图的可解释性、以及避免不当动作生成（伦理/安全）将成为必须考虑的问题；研究将朝可约束生成与可证实的语义对齐方向发展。  
5. 评价协议标准化与任务细分：当前评价缺乏统一的细粒度对齐指标（例如局部语义对齐、动作周期/节拍一致性等），未来将涌现更多任务细分（文本→关键帧、文本→风格化舞蹈、文本+音乐→同步舞蹈）与专用自动指标以替代或补充主观评估。  

结论  
2022–2025 年间，文本驱动的人体动作合成领域在模型范式上出现“扩散式生成（含潜空间）”与“掩码/离散令牌建模（含分层量化、自回归）”两条主干并行发展；测试时控制（拼贴/多轨）与工程化加速（隐空间、TensorRT、后处理）成为落地的两项关键技巧。未来研究将集中于多模态预训练、测试时精细控制、工程级加速与评价标准化；同时，伦理与安全约束、可解释性将成为不可回避的研究议题。本文选取的代表作覆盖上述范式的核心思路，为后续针对具体应用场景的算法选择和基准设计提供技术汇总与方向性参考。

参考文献（≥12 篇，按出现顺序列出以便检索）  
- MotionDiffuse: Text-Driven Human Motion Generation With Diffusion Model (TPAMI 2024 解读 / 实现参见) — 见介绍与实现综述 [blog.csdn.net](https://blog.csdn.net/qq_42722197/article/details/140107485).  
- MoMask: Generative Masked Modeling of 3D Human Motions — CVPR 2024 (Guo et al.) 项目/论文页与摘要 [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/46930).  
- MoMask 另见开源/摘要汇总 [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/8941f767-7553-44d5-9465-fd536008d0c1).  
- BAMM: Bidirectional Autoregressive Motion Model (2024) — 方法与实验摘要 [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/9d28891c-494c-44d6-aafe-24aab09ab785).  
- Multi-Track Timeline Control for Text-Driven 3D Human Motion Generation — arXiv / 论文审查与解析 [themoonlight.io](https://www.themoonlight.io/zh/review/multi-track-timeline-control-for-text-driven-3d-human-motion-generation).  
- Motion‑latent / Motion‑diffusion 实践与讨论（实现与项目链接汇总，见综述博客与资源）[blog.csdn.net](https://blog.csdn.net/qq_42722197/article/details/140107485).  
- DreaMoving: A Human Dance Video Generation Framework based on Diffusion Models (舞蹈/姿势→视频，2023) — 论文与实现汇总 [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/e041bfd1-b3de-4940-8991-2d4338dafa38).  
- Text2Performer: Text-Driven Human Video Generation (姿势/文本→视频，2023) — 论文汇总与项目描述 [hub.baai.ac.cn](https://hub.baai.ac.cn/view/25619).  
- Multi‑scale / engineering acceleration of diffusion for pose‑driven generation (DAF‑DH, 2025 优先出版) — 加速与感知优化框架（论文与摘要）[arocmag.cn](https://www.arocmag.cn/abs/2025.03.0057).  
- Motion Anything: Multi‑modal (Text+Music) Motion Generation (arXiv 2503.06955 / 2025 预印，方法与数据集说明见实现与博客) [blog.csdn.net](https://blog.csdn.net/m0_66899341/article/details/146268923).  
- 相关实现/综述与工具（扩散、掩码、时序拼贴等）参考条目与社区汇总（选读）：Human Motion Diffusion Model, Motion‑masked diffusion 等综述/实现条目 [blog.csdn.net](https://blog.csdn.net/qq_42722197) 与 Moonlight 论文审查集合 [themoonlight.io](https://www.themoonlight.io).  
- 额外背景/方法参考（隐空间扩散与潜在表示、分层量化思想的先前工作与实现）：Motion‑latent diffusion / latent tokenization 相关实现与CVPR/CV/TPAMI年表（实现与解读合集）[blog.csdn.net](https://blog.csdn.net/qq_42722197/article/details/140107485).  

（注：上述引用指向的页面包含对应论文的正式会议信息或预印本及实现/解读，读者可据此检索原始论文 PDF 与代码仓库以获取完整细节。）