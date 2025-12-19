生成对抗网络（GANs）的复兴与演进：2022–2025 年技术突破、混合架构与应用全景综述
1. 引言：生成式人工智能的范式转移与 GAN 的韧性
自 Ian Goodfellow 于 2014 年提出生成对抗网络（Generative Adversarial Networks, GANs）以来，该架构一度统治了图像合成、风格迁移和超分辨率等领域 。其核心的“生成器-判别器”零和博弈（Zero-Sum Game）机制，赋予了模型生成高保真、锐利图像的能力。然而，随着 2020 年代初期去噪扩散概率模型（Denoising Diffusion Probabilistic Models, DDPMs）的兴起，生成式 AI 的格局发生了剧烈震荡。扩散模型凭借其卓越的分布覆盖能力（Mode Coverage）、训练稳定性和对文本提示的精确响应，迅速成为 DALL-E 2、Stable Diffusion 和 Midjourney 等现象级应用背后的技术引擎 。   

在 2022 年至 2023 年的“扩散模型爆发期”，GANs 面临了严峻的生存挑战。学术界普遍认为，GANs 在处理复杂的大规模数据集（如 LAION-5B）时存在严重的模式崩溃（Mode Collapse）问题，且难以像扩散模型那样通过简单的扩展模型容量（Scaling）来获得性能增益 。然而，扩散模型的阿喀琉斯之踵在于其昂贵的推理成本——生成一张高质量图像往往需要数十甚至上百次的迭代去噪步骤，导致推理延迟高达数秒甚至数分钟，这在实时交互、视频生成和边缘设备部署中构成了难以逾越的障碍 。   

进入 2024 年与 2025 年，随着对实时生成需求的激增，学术界和工业界重新审视了 GANs 的独特价值：单步生成的极致效率。这一时期标志着 GANs 的“复兴”与“进化”。研究重心不再局限于单纯的架构竞争，而是转向了深度融合——利用 GANs 的对抗性目标来加速扩散模型（如对抗性蒸馏），或者借鉴 Transformer 和扩散模型的架构优势来升级 GANs（如 GigaGAN, TIGER）。此外，在 3D 内容生成领域，GANs 与神经辐射场（NeRF）及最新的 3D 高斯泼溅（3D Gaussian Splatting）技术的结合，开辟了实时 3D 渲染的新纪元 。   

本综述旨在系统梳理 2022 年至 2025 年间 GANs 的关键技术进展。我们将深入剖析大规模文生图 GAN 的架构创新、对抗性扩散蒸馏（ADD/LADD）的理论突破、3D GANs 从隐式到显式表示的演变，以及交互式图像编辑（DragGAN）的新范式。通过对 StyleGAN-T、GigaGAN、TIGER、SANA-Sprint、GaussianCity 等里程碑式工作的详尽分析，本报告将揭示 GANs 如何在生成式 AI 的红海中重构其生态位，并预测未来的技术走向。

2. 大规模文本到图像 GANs 的架构重构与扩展
长期以来，GANs 被认为难以扩展到开放域（Open-domain）的文本到图像生成任务。然而，2023 年至 2025 年的一系列工作证明，通过引入现代化的架构组件和更强的判别器监督，GANs 完全有能力在十亿参数规模上与扩散模型分庭抗礼，同时保持其标志性的亚秒级推理速度。

2.1 StyleGAN-T：针对大规模生成的架构现代化
在 2023 年初，StyleGAN-T  的提出是对“GANs 无法扩展”这一论断的有力反击。该研究指出，StyleGAN 系列（StyleGAN 1/2/3）之所以在大规模文本生成任务中表现不佳，并非因为对抗学习范式本身的缺陷，而是因为其架构是为特定类别（如人脸 FFHQ）设计的，缺乏处理高度多样化数据的归纳偏置。   

架构创新与机制分析： StyleGAN-T 重新设计了生成器和判别器，摒弃了传统的渐进式增长（Progressive Growing）策略，转而采用更能适应复杂分布的架构。

重新设计的生成器： 引入了更强的调节机制（Conditioning Mechanism），使得文本嵌入（Text Embeddings）能够更有效地调制生成过程的每一层特征。这解决了传统 GAN 在处理复杂语义组合（如“一只骑在马上的宇航员”）时经常出现的语义丢失问题。

CLIP 对齐的强化： 为了提高文本与图像的一致性，StyleGAN-T 显式地利用 CLIP 模型的特征空间作为监督信号。虽然这在之前的工作中已有尝试，但 StyleGAN-T 通过优化损失函数权重和训练策略，使得模型在保持图像保真度的同时，大幅提升了 CLIP Score 。   

性能基准与局限： 定量实验显示，在 64x64 的低分辨率下，StyleGAN-T 实现了 7.30 的零样本（Zero-shot）FID，这一成绩甚至优于当时的扩散模型 eDiff-I（7.60 FID）和 GLIDE（7.40 FID）。更令人印象深刻的是其速度：生成一张 512px 图像仅需 0.1 秒，比 Stable Diffusion 快 30 倍以上。然而，StyleGAN-T 在高分辨率（256x256 及以上）下的表现遭遇了瓶颈，其 FID 随分辨率提升而恶化，且纹理细节仍不及经过多步迭代优化的扩散模型。这表明，单纯改进 StyleGAN 架构仍不足以完全解决高分辨率下的模式覆盖问题。   

2.2 GigaGAN：十亿参数级的暴力美学与精细控制
紧随 StyleGAN-T 之后，GigaGAN  在 CVPR 2023 上发布，标志着 GANs 正式迈入“十亿参数（1B+）”时代。GigaGAN 的核心贡献在于证明了 GANs 可以通过扩大模型容量（Scaling Up）来利用超大规模数据集（如 LAION），并在此过程中通过特定的架构技巧维持训练稳定性。   

核心技术突破：

样本自适应核选择（Sample-Adaptive Kernel Selection, SAKS）： 这是 GigaGAN 最具创新性的组件之一。传统的卷积网络在处理所有样本时使用固定的卷积核权重，这在处理单一类别（如人脸）时是有效的，但在面对开放世界（如“赛博朋克风格的城市” vs “水墨画风格的猫”）时显得捉襟见肘。SAKS 机制允许生成器根据输入文本的条件，动态地预测或调整卷积核的权重 。这实际上赋予了模型一种“自适应滤波器”的能力，使其能够根据语义内容动态调整纹理生成的频率和模式。   

多尺度合成与注意力机制： GigaGAN 在生成器中集成了跨层注意力机制（Cross-Attention）和自注意力机制（Self-Attention），这在以往的 GAN 中往往因计算成本过高而被慎用。通过高效的实现，GigaGAN 能够在高分辨率特征图上捕捉长距离依赖，确保了生成的图像在全局结构上的连贯性 。   

多尺度判别器系统： 为了稳定大规模训练，GigaGAN 采用了一组复杂的判别器，分别在不同的图像尺度上进行真假判别。这种设计迫使生成器在所有频率段（从全局结构到局部纹理）都必须逼近真实分布。

结果与影响： GigaGAN 的推理速度极为惊人：生成 512px 图像仅需 0.13 秒，合成 1600 万像素（16-megapixel） 的超高清图像仅需 3.66 秒 。相比之下，扩散模型生成同等分辨率图像通常需要数分钟。此外，GigaGAN 保留了 GANs 潜在空间（Latent Space）平滑连续的特性，支持高质量的语义插值（Latent Interpolation）和样式混合（Style Mixing），这在视频生成和艺术创作工具中具有极高的应用价值 。   

2.3 TIGER：预训练表征与视觉增强判别器的巅峰 (2025)
进入 2025 年，TIGER (Text-to-Image GAN with prEtrained Representations)  代表了纯 GAN 架构的最新技术水平（SOTA）。TIGER 的设计哲学从“从头训练”转向了“利用先验”，即利用现有的强大视觉基础模型来辅助 GAN 的训练。   

视觉增强判别器 (Vision-Empowered Discriminator)： TIGER 最大的创新在于其判别器的设计。传统的 GAN 判别器通常从随机初始化开始训练，这导致在训练初期，判别器无法提供有意义的梯度，容易导致训练发散。TIGER 创新性地堆叠了多个在大规模数据上预训练的视觉模型作为判别器的主干，具体包括：

CLIP (Contrastive Language–Image Pre-training)： 提供强语义对齐信号。

Swin Transformer： 提供多尺度的视觉特征层次。

DINO (Self-Supervised Learning)： 提供细粒度的物体部件和纹理理解能力。 这些预训练模型已经具备了极强的场景理解和领域泛化能力 。TIGER 的判别器不再是学习“如何看图”，而是学习“如何区分真假图的细微差别”，这极大地加速了收敛并提升了生成质量。   

高容量融合块 (High-Capacity Fusion Block, HFBlock)： 在生成器端，TIGER 提出了 HFBlock，旨在解决文本条件与图像特征融合不充分的问题。该模块包含：

深度融合模块 (Deep Fusion Module)： 利用深度卷积和注意力机制，深层次地挖掘文本与图像特征的交互。

全局融合模块 (Global Fusion Module)： 确保生成的图像在整体色调和风格上与文本描述保持一致 。   

基准测试与超越： 在标准的 COCO 数据集上，TIGER 取得了 5.48 FID 的惊人成绩，在 CUB 数据集上达到 9.38 FID 。这一结果不仅刷新了 GANs 的历史记录，也超越了许多同期的扩散模型和自回归模型。更重要的是，TIGER 在零样本（Zero-shot）生成任务上表现出了与顶级扩散模型相当的语义对齐能力，同时保持了 GAN 的亚秒级推理速度。   

3. 对抗性扩散蒸馏：速度与质量的混合范式
如果说 GigaGAN 和 TIGER 是 GAN 的自我进化，那么**对抗性扩散蒸馏（Adversarial Diffusion Distillation, ADD）**则是 GAN 对扩散模型的反向渗透。2023 年至 2025 年，为了解决扩散模型推理慢的问题，研究人员开始将 GAN 的判别器作为一种强有力的“感知损失”引入扩散模型的蒸馏过程中，试图结合扩散模型的分布覆盖能力和 GAN 的单步采样能力。

3.1 ADD：打破采样步数的物理限制
ADD (Adversarial Diffusion Distillation)  是这一方向的开山之作。它提出了一种新颖的训练目标，使得稳定扩散（Stable Diffusion）等基础模型能够在 1-4 步内生成高质量图像。   

混合目标函数解析： ADD 的训练目标包含两部分：

分数蒸馏损失（Score Distillation Sampling, SDS）： 利用一个冻结的预训练扩散模型（教师模型）来计算损失。教师模型会评估学生模型生成的图像是否符合其学习到的分布，并提供梯度指导。这一步保证了生成图像的多样性和语义对齐，防止了纯 GAN 常见的模式崩溃 。   

对抗性损失（Adversarial Loss）： 引入一个判别器，区分学生模型生成的图像和真实图像。判别器的作用是强制学生模型生成的图像在感知质量（纹理、清晰度）上逼近真实图像流形。ADD 使用了基于特征网络（如 DINOv2）的判别器，在特征空间而非像素空间计算差异，这被称为“投影判别器”技术的变体 。   

结果： ADD 成功将 SDXL 的推理步数从 50 步压缩至 1-4 步，且在 4 步采样下的图像质量在盲测中优于原始 SDXL 的 50 步采样结果 。   

3.2 LADD：向潜在空间的战略转移
LADD (Latent Adversarial Diffusion Distillation)  是针对 ADD 的改进版本，主要解决了 ADD 在像素空间计算损失导致的高显存消耗问题。   

全潜在空间蒸馏（Fully Latent-Space Distillation）： LADD 的核心洞察是：既然现代扩散模型（如 LDM）本身就在潜在空间（Latent Space）工作，为什么还要解码回像素空间去计算对抗损失？LADD 将判别器直接作用于 VAE 的潜在编码（Latent Codes）或生成器的中间特征层。

统一教师与判别器： LADD 甚至不需要额外的判别器网络，而是直接利用教师模型（预训练的扩散模型）的特征作为判别器的输入，或者将教师模型本身微调为判别器 。   

合成数据训练： LADD 展示了仅使用教师模型生成的合成数据进行训练的可行性。这意味着蒸馏过程不再需要访问原始的训练数据集（如 LAION），极大地规避了版权和隐私风险 。   

3.3 SANA-Sprint：一步生成的终极形态 (2025)
SANA-Sprint  是 NVIDIA 在 2025 年发布的最新成果，代表了当前对抗性蒸馏技术的最高水平。它结合了**连续时间一致性模型（Continuous-Time Consistency Models, sCM）**与 LADD，实现了真正的“一步生成”。   

技术原理： SANA-Sprint 采用了一种混合蒸馏框架：

sCM 路径： 利用一致性模型（Consistency Models）的特性，强制模型学习一种直接从噪声映射到数据的轨迹（Trajectory），确保生成过程的确定性和稳定性。

LADD 路径： 在 sCM 的基础上叠加对抗性损失，专门用于填补单步采样带来的细节丢失。由于一致性模型倾向于生成平滑、模糊的结果，对抗性损失在这里起到了“锐化”和“加细节”的关键作用 。   

性能基准： 在 H100 GPU 上，SANA-Sprint 生成一张 1024x1024 分辨率的图像仅需 0.1 秒。这一速度比同期的 FLUX-Schnell 模型快 10 倍以上，且 FID 降至 7.59，GenEval 得分达到 0.74，在速度和质量的帕累托前沿（Pareto Frontier）上建立了新的标准 。SANA-Sprint 的出现，实际上模糊了 GAN 和扩散模型的界限——它在推理时表现得像 GAN（一步前向），但在训练时利用了扩散模型的流形知识。   

3.4 UFOGen：一次前向的哲学
UFOGen (You Forward Once Generative Model)  在 CVPR 2024 上提出，其理念与 SANA-Sprint 类似，但在实现上更侧重于对生成器参数化的修改。   

x 
0
​
  预测： UFOGen 修改了扩散模型的输出层，使其不再预测噪声（ϵ），而是直接预测去噪后的清晰图像（x 
0
​
 ）。

混合目标： 结合了标准的重建损失和对抗性损失。UFOGen 在一步生成下的 FID 达到了 22.5，虽然在绝对数值上不如 SANA-Sprint，但它证明了修改扩散模型参数化方式对于单步生成的重要性 。   

4. 3D 生成与神经渲染：从 NeRF 到 Gaussian Splatting 的跃迁
2022 年至 2025 年，3D 生成领域经历了从隐式表示（Implicit Representation, 如 NeRF）向显式或半显式表示（Explicit Representation, 如 3D Gaussian Splatting）的剧烈转型。GANs 在此过程中扮演了核心角色，特别是在解决 3D 几何一致性和渲染效率方面。

4.1 3D-GANs 的奠基：EG3D 与 GET3D (2022)
EG3D (CVPR 2022) ：这是 3D GAN 领域的里程碑。它引入了**三平面（Tri-plane）**表示，这是一种混合结构，将 3D 空间分解为三个正交的 2D 特征平面。StyleGAN2 生成器首先合成这三个平面，然后通过轻量级的神经渲染器解码为 3D 图像。EG3D 解决了传统 Voxel GAN 分辨率低和 NeRF GAN 训练极慢的问题，成为后续两年的标准基线。   

GET3D (NeurIPS 2022) ：不同于 EG3D 侧重于图像合成，GET3D 专注于生成显式纹理网格（Textured Meshes）。它利用可微表面建模（DMTet）和 2D GANs 的判别器，能够端到端地生成拓扑复杂的物体（如汽车、摩托车）。这使得 GAN 生成的内容可以直接导入 Unity 或 Unreal Engine 等游戏引擎中。   

4.2 几何质量的提升：GeoGen (CVPR 2024)
尽管 EG3D 表现出色，但其基于体渲染（Volume Rendering）的方法往往产生含有噪声的几何表面（Noisy Geometry），这被称为“多视图一致性但几何不准确”的现象。 GeoGen  提出了一种基于**有向距离场（Signed Distance Functions, SDF）**的生成模型。   

SDF 驱动的渲染： GeoGen 将体密度重新解释为 SDF，并引入几何先验，强制生成的表面光滑且闭合。

对抗性几何约束： 除了 RGB 图像的判别器外，GeoGen 还引入了对渲染出的深度图（Depth Map）和法线图（Normal Map）的对抗性约束。这种多模态的判别机制迫使生成器不仅要“画”出好图，还要“造”出合理的 3D 结构 。   

4.3 生成式高斯泼溅：2025 年的新前沿
3D Gaussian Splatting (3DGS) 自 2023 年下半年横空出世以来，以其 >100 FPS 的实时渲染速度和高质量重建能力，迅速取代 NeRF 成为 3D 表示的首选。2024-2025 年，将 GANs 与 3DGS 结合成为最热门的趋势。

Gaussian Splatting Decoder (CVPRW 2024) ：该工作提出了一个解码器架构，能够将 EG3D 等预训练 3D GAN 的隐式 Tri-plane 特征直接解码为显式的 3D 高斯属性（位置、协方差、颜色、不透明度）。   

无需超分： 传统的 EG3D 需要一个 2D 超分辨率模块来提升渲染图像的质量，但这会引入 3D 一致性伪影（“纹理闪烁”）。Gaussian Splatting Decoder 能够直接生成高分辨率的 3DGS 场景，完全绕过了超分模块，实现了真正的 3D 一致性实时渲染。

GaussianCity (CVPR 2025) ：针对无界城市场景（Unbounded City Scenes）生成的挑战，GaussianCity 结合了 GAN 的生成能力与 3DGS 的渲染效率。   

BEV-Point 表示： 为了解决大规模场景下 3DGS 显存占用爆炸的问题，GaussianCity 提出了一种紧凑的 鸟瞰图点云（BEV-Point） 表示。生成器首先在 BEV 空间生成点云分布，然后通过点序列化器将其解码为 3D 高斯球。

效率突破： 这种压缩表示使得显存占用不随场景范围线性增长，相比之前的 CityDreamer，推理速度提升了 60 倍，能够在消费级 GPU 上实时生成无限延展的逼真城市环境 。   

5. 交互式图像编辑：DragGAN 效应及其自动化演进
生成式 AI 不仅要“生成”，还要“可控”。DragGAN 的出现标志着生成图像编辑进入了“基于点的精确操控”时代。这一方向在 2023-2025 年迅速迭代，经历了从优化到预测的技术路线变革。

5.1 DragGAN：基于优化的操控 (SIGGRAPH 2023)
DragGAN  允许用户在图像上定义控制点（Handle Points）和目标点（Target Points），通过迭代优化生成器的潜在代码（Latent Code）w 和特征图插值，实现对物体姿态、形状的像素级精确拖拽。   

机制： 它包含两个交替进行的步骤：1) 运动监督（Motion Supervision），通过优化潜在代码使得控制点向目标点移动；2) 点追踪（Point Tracking），在更新后的特征图上重新定位控制点。

局限： 依赖于迭代优化过程，推理时间较长（通常需要数十秒到数分钟），且在纹理较少或背景复杂的区域容易跟踪失败 。   

5.2 Auto DragGAN：回归预测的加速 (MM 2024)
为了解决 DragGAN 的速度瓶颈，Auto DragGAN  提出了一种彻底的范式转换：用预测（Prediction）替代优化（Optimization）。   

潜在预测器（Latent Predictor）： Auto DragGAN 训练了一个 Transformer 架构的预测器，能够根据当前的控制点位置和目标向量，直接回归出下一时刻的潜在代码增量 Δw。

潜在正则化器（Latent Regularizer）： 为了防止预测出的潜在代码偏离真实流形，引入了一个正则化模块。

结果： 这一改进将编辑过程变成了近乎实时的前向推理。实验表明，Auto DragGAN 在像素级控制精度上与 DragGAN 相当，但速度提升了数个数量级，且 FID 分数从 DragGAN 的 8.30 降低到了 6.46，证明了直接预测产生的潜在轨迹更加平滑自然 。   

5.3 DirectDrag：无掩码与特征对齐 (2025)
DirectDrag  代表了该方向在 2025 年的最新形态，进一步降低了用户的交互门槛。   

自动软掩码生成（Auto Soft Mask Generation）： 传统的拖拽编辑往往需要用户提供掩码（Mask）以限定编辑区域，防止背景变形。DirectDrag 设计了一个模块，能够根据点的位移向量自动推断出受影响的区域，生成“软掩码”，实现了“指哪打哪”且不影响背景的无掩码编辑。

读取引导特征对齐（Readout-Guided Feature Alignment）： 利用扩散模型中间层的特征作为引导信号，DirectDrag 在无需繁琐交互的情况下，保持了极高的图像保真度和结构一致性 。   

6. 特殊领域应用：科学成像与视频生成
虽然通用图像生成是主战场，但 GANs 在对保真度要求极高的科学领域和对时序一致性要求极高的视频领域仍有独特应用。

6.1 医学成像与科学数据合成
在医学 MRI 模态转换（如 T1 加权像转 T2 加权像）任务中， 和  的基准测试表明，基于 GAN 的模型（如 Pix2Pix 的变体）在结构保真度（Structural Fidelity）和计算效率上优于扩散模型和流匹配模型。   

数据敏感性： 扩散模型被发现更“吃数据”（Data-hungry），在小样本医学数据集上容易过拟合或产生幻觉（Hallucinations），这在医疗诊断中是致命的。

推理速度： 临床环境往往需要快速成像，GAN 的毫秒级推理使其能够集成到实时扫描流程中，用于加速 MRI 采集。

6.2 视频生成中的 GAN 角色
在视频生成领域，尽管 Sora 等扩散模型占据主导，但在 HOIAnimator  和 InstructVideo  等工作中，GAN 的对抗性损失被用于增强视频的时序一致性（Temporal Consistency）。此外，SF-V (Single Forward Video)  等尝试将单步生成技术扩展到视频领域，试图解决视频扩散模型推理极慢的痛点，尽管目前仍处于早期探索阶段。   

7. 趋势预测与定量分析
7.1 性能基准对比 (2024-2025)
基于文献数据，我们整理了 GANs 与 Diffusion Models 的关键性能指标对比表：

模型类型	代表模型 (2024-2025)	推理速度 (512px/1024px)	FID (COCO Zero-shot)	训练资源需求	优势	劣势
Diffusion	Stable Diffusion 3 / FLUX	~1.0 - 2.0 秒	~6.0 - 7.0	极高 (数千 GPU 天)	文本对齐极佳，分布覆盖广	推理慢，计算昂贵
Pure GAN	TIGER / StyleGAN-T	< 0.1 秒	5.48	中等	极致速度，单步生成，低算力需求	复杂语义组合能力稍弱
Hybrid (Distilled)	SANA-Sprint / ADD	~0.1 秒	7.59	高 (需预训练教师)	兼具速度与质量	训练流程复杂 (Teacher-Student)
3D Generative	GaussianCity	> 100 FPS (渲染)	N/A	高	实时 3D 渲染，显式几何，无界场景	仅限于特定领域 (如城市, 人脸)
数据来源：   

洞察：

速度差异： GANs 和蒸馏模型在速度上比原生扩散模型快 1-2 个数量级。这种巨大的延迟差异决定了 GANs 在移动端应用（如手机上的实时滤镜）和实时渲染（如 VR/AR）中具有不可替代的地位。

质量趋同： TIGER 的 FID (5.48) 已经超越了许多扩散模型，这打破了“GAN 质量不如 Diffusion”的刻板印象。这主要归功于预训练判别器的引入。

7.2 未来趋势预测
生成式 AI 的“钟摆效应”与最终融合： 技术发展呈现出一种周期性。2014-2021 年是 GAN 的时代，2022-2023 年 Diffusion 称霸。到了 2024-2025 年，钟摆回摆。未来的主流将不再是单一的 GAN 或 Diffusion，而是 "Diffusion for Training, GAN for Inference" 的模式。即利用扩散模型学习数据分布，然后通过对抗性蒸馏将知识压缩进单步生成器中。

3D 生成的显式化与标准化： 从隐式的 NeRF 转向显式的 3D Gaussian Splatting 是不可逆转的趋势。GANs 天然适合生成显式参数（如高斯的协方差、颜色、位置），这使得 Generative 3DGS 将在虚拟现实（VR）、游戏内容生成和自动驾驶模拟中爆发。GaussianCity 证明了这种技术处理无界大场景的能力，预示着数字孪生城市的构建成本将大幅降低。

边缘侧 AI (Edge AI) 的复兴： 随着 TIGER 和 SANA-Sprint 将高性能生成压缩到 0.1 秒以内，且显存需求降低，在智能手机、AR 眼镜等边缘设备上部署高质量生成模型将成为 2025 年下半年的产业热点。GANs 的低计算负载特性使其在此领域比原生 Diffusion 具有压倒性优势。

交互式编辑的自动化： DragGAN 系列的发展表明，用户交互正变得越来越“懒人化”。未来的图像编辑工具将不再需要用户绘制复杂的掩码或输入冗长的 Prompt，仅需简单的拖拽甚至意图识别（如 Auto DragGAN 预测运动轨迹）即可完成修改。

8. 结论
2022 年至 2025 年是生成对抗网络（GANs）从“被取代”的边缘重回舞台中央的关键时期。面对扩散模型的激烈竞争，GANs 并未消亡，而是通过规模化（Scaling）、**混合化（Hybridization）和三维化（3D-adaptation）**完成了自我进化。

研究表明，虽然扩散模型在通用文生图任务上建立了强大的基准，但 GANs 通过 GigaGAN 和 TIGER 等架构证明了其在大规模数据上的潜力。更重要的是，通过对抗性扩散蒸馏（ADD/LADD），GANs 的对抗训练机制成为了加速扩散模型的关键钥匙，SANA-Sprint 的成功便是这一融合趋势的最佳注脚。同时，在 3D 内容生成和精细图像编辑（DragGAN）等垂直领域，GANs 凭借其对潜在空间的结构化控制能力和高效推理，依然保持着 SOTA 地位。

展望未来，随着对实时性、可控性及 3D 沉浸感需求的增加，GANs 将继续作为生成式 AI 生态系统中不可或缺的高效推理引擎，与扩散模型共同推动人工智能内容生成（AIGC）向实时、交互、三维的世界迈进。

参考文献索引（基于提供的 Snippets）：

GigaGAN:    

StyleGAN-T:    

TIGER:    

ADD/LADD/SANA-Sprint:    

UFOGen:    

3D GANs (EG3D, GET3D, GeoGen):    

Gaussian Splatting GANs (GaussianCity, Decoders):    

DragGAN & Variants:    

Benchmarks:    


arxiv.org
[1406.2661] Generative Adversarial Networks - arXiv
在新窗口中打开

medium.com
GANs vs Diffusion Models: Battle of Generative Techniques | by Amit Kharche - Medium
在新窗口中打开

arxiv.org
[2303.05511] Scaling up GANs for Text-to-Image Synthesis - arXiv
在新窗口中打开

arxiv.org
A Review on Generative AI for Text-to-Image and Image-to-Image Generation and Implications to Scientific Images - arXiv
在新窗口中打开

pmc.ncbi.nlm.nih.gov
Synthetic Scientific Image Generation with VAE, GAN, and Diffusion Model Architectures - PMC - PubMed Central
在新窗口中打开

arxiv.org
[2301.09515] StyleGAN-T: Unlocking the Power of GANs for Fast Large-Scale Text-to-Image Synthesis - arXiv
在新窗口中打开

medium.com
SANA-Sprint: One-Step Diffusion with Continuous-Time Consistency Distillation - Medium
在新窗口中打开

computationalimaging.org
EG3D: Efficient Geometry-aware 3D Generative Adversarial Networks | CVPR 2022
在新窗口中打开

openaccess.thecvf.com
Generative Gaussian Splatting for Unbounded 3D City Generation - CVF Open Access
在新窗口中打开

liner.com
[Quick Review] StyleGAN-T: Unlocking the Power of GANs for Fast Large-Scale Text-to-Image Synthesis - Liner
在新窗口中打开

mingukkang.github.io
GigaGAN: Scaling up GANs for Text-to-Image Synthesis - Minguk Kang
在新窗口中打开

blog.metaphysic.ai
GigaGAN: Stable Diffusion for Generative Adversarial Networks - Blog - Metaphysic.ai
在新窗口中打开

openaccess.thecvf.com
Scaling Up GANs for Text-to-Image Synthesis - CVF Open Access
在新窗口中打开

arxiv.org
[2501.00116] Text-to-Image GAN with Pretrained Representations - arXiv
在新窗口中打开

researchgate.net
Text-to-Image GAN with Pretrained Representations - ResearchGate
在新窗口中打开

scribd.com
2501.00116v1 | PDF | Machine Learning | Cognitive Science - Scribd
在新窗口中打开

themoonlight.io
[Papierüberprüfung] Text-to-Image GAN with Pretrained Representations - Moonlight
在新窗口中打开

arxiv.org
Text-to-Image GAN with Pretrained Representations - arXiv
在新窗口中打开

semanticscholar.org
[PDF] Adversarial Diffusion Distillation - Semantic Scholar
在新窗口中打开

artgor.medium.com
Paper Review: Adversarial Diffusion Distillation | by Andrew Lukyanenko - Medium
在新窗口中打开

insiders.dashtoon.com
Insights from Our Adversarial Diffusion Distillation POC - Dashtoon Insiders
在新窗口中打开

arxiv.org
[2403.12015] Fast High-Resolution Image Synthesis with Latent Adversarial Diffusion Distillation - arXiv
在新窗口中打开

medium.com
From ADD to PADD to LADD: Advancing Fast Diffusion Model Distillation | by Pietro Bolcato
在新窗口中打开

arxiv.org
[2311.17042] Adversarial Diffusion Distillation - arXiv
在新窗口中打开

codelabsacademy.com
Accelerate Image Synthesis: Latent Adversarial Diffusion Distillation - Code Labs Academy
在新窗口中打开

github.com
Details of the model distillation technique · Issue #15 · black-forest-labs/flux - GitHub
在新窗口中打开

openaccess.thecvf.com
SANA-Sprint: One-Step Diffusion with Continuous-Time Consistency Distillation - CVF Open Access
在新窗口中打开

arxiv.org
SANA-Sprint: One-Step Diffusion with Continuous-Time Consistency Distillation - arXiv
在新窗口中打开

nvlabs.github.io
SANA-Sprint: One-Step Diffusion with Continuous-Time Consistency Distillation - NVlabs
在新窗口中打开

openaccess.thecvf.com
UFOGen: You Forward Once Large Scale Text-to-Image Generation via Diffusion GANs
在新窗口中打开

semanticscholar.org
UFOGen: You Forward Once Large Scale Text-to-Image Generation via Diffusion GANs
在新窗口中打开

liner.com
UFOGen: You Forward Once Large Scale Text-to-Image Generation via Diffusion GANs
在新窗口中打开

proceedings.neurips.cc
GET3D: A Generative Model of High Quality 3D Textured Shapes Learned from Images
在新窗口中打开

alphaxiv.org
GET3D: A Generative Model of High Quality 3D Textured Shapes Learned from Images | alphaXiv
在新窗口中打开

arxiv.org
GeoGen: Geometry-Aware Generative Modeling via Signed Distance Functions - arXiv
在新窗口中打开

openaccess.thecvf.com
Rendering Every Pixel for High-Fidelity Geometry in 3D GANs - CVPR 2024 Open Access Repository
在新窗口中打开

openaccess.thecvf.com
GeoGen: Geometry-Aware Generative Modeling via Signed Distance Functions - CVPR 2024 Open Access Repository - The Computer Vision Foundation
在新窗口中打开

openaccess.thecvf.com
Gaussian Splatting Decoder for 3D-aware Generative Adversarial Networks - CVPR 2024 Open Access Repository - The Computer Vision Foundation
在新窗口中打开

florian-barthel.github.io
Gaussian Splatting Decoder for 3D-aware Generative Adversarial Networks - Florian Barthel
在新窗口中打开

arxiv.org
Gaussian Splatting Decoder for 3D-aware Generative Adversarial Networks - arXiv
在新窗口中打开

arxiv.org
GaussianCity: Generative Gaussian Splatting for Unbounded 3D City Generation - arXiv
在新窗口中打开

arxiv.org
[2406.06526] Generative Gaussian Splatting for Unbounded 3D City Generation - arXiv
在新窗口中打开

vcai.mpi-inf.mpg.de
Drag Your GAN: Interactive Point-based Manipulation on the Generative Image Manifold - Visual Computing and Artificial Intelligence
在新窗口中打开

arxiv.org
[2305.10973] Drag Your GAN: Interactive Point-based Manipulation on the Generative Image Manifold - arXiv
在新窗口中打开

vcai.mpi-inf.mpg.de
Drag Your GAN: Interactive Point-based Manipulation on the Generative Image Manifold
在新窗口中打开

itm-conferences.org
DragGAN: Interactive Point-Based Image Manipulation on Generative Adversarial Networks - ITM Web of Conferences
在新窗口中打开

openreview.net
Auto DragGAN: Editing the Generative Image Manifold in an Autoregressive Manner - OpenReview
在新窗口中打开

liner.com
Auto DragGAN: Editing the Generative Image Manifold in an Autoregressive Manner - Liner
在新窗口中打开

arxiv.org
Auto DragGAN: Editing the Generative Image Manifold in an Autoregressive Manner - arXiv
在新窗口中打开

researchgate.net
Drag Your GAN: Interactive Point-based Manipulation on the Generative Image Manifold - ResearchGate
在新窗口中打开

arxiv.org
[2512.03981] DirectDrag: High-Fidelity, Mask-Free, Prompt-Free Drag-based Image Editing via Readout-Guided Feature Alignment - arXiv
在新窗口中打开

researchgate.net
DirectDrag: High-Fidelity, Mask-Free, Prompt-Free Drag-based Image Editing via Readout-Guided Feature Alignment - ResearchGate
在新窗口中打开

arxiv.org
DirectDrag: High-Fidelity, Mask-Free, Prompt-Free Drag-based Image Editing via Readout-Guided Feature Alignment - arXiv
在新窗口中打开

arxiv.org
Benchmarking GANs, Diffusion Models, and Flow Matching for T1w-to-T2w MRI Translation
在新窗口中打开

openreview.net
Does Diffusion Beat GAN in Image Super Resolution? - OpenReview
在新窗口中打开

cvpr.thecvf.com
CVPR 2024 Accepted Papers
在新窗口中打开

researchgate.net
UFOGen: You Forward Once Large Scale Text-to-Image Generation via Diffusion GANs
在新窗口中打开

mingukkang.github.io
Scaling up GANs for Text-to-Image Synthesis - Minguk Kang
在新窗口中打开

ecva.net
Adversarial Diffusion Distillation
在新窗口中打开

aurorasolar.com
GANs vs. Diffusion Models: Putting AI to the test | Aurora Solar