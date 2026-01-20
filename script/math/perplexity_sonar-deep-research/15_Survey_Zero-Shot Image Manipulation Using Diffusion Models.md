# 扩散模型零样本图像编辑：从2022年到2025年的方法综述

本综述系统梳理了扩散模型在零样本图像编辑领域（2022-2025）的发展轨迹，重点分析了五类核心方法：基于提示词的编辑、基于注意力机制的编辑、基于参考图像的编辑、深度感知编辑以及混合条件编辑。通过对70余篇学术论文的深入分析，本综述揭示了该领域的三大研究范式转变：从单一条件到多模态条件融合，从全局编辑到精细区域编辑，从训练导向到推理优化。在实验与评价部分，我们总结了扩散模型在编辑保真度、语义对齐和时间一致性上的共性挑战。趋势分析表明，2025年前后的研究将聚焦于参数高效的适配方法、实时推理加速以及编辑的可解释性与可控性的深度结合。

## 引言

扩散模型自2020年引入以来，凭借其超越生成对抗网络的训练稳定性和生成质量[1][2][3]，迅速成为图像生成与编辑领域的主导范式。与需要大规模成对数据的监督编辑方法相比，零样本图像编辑通过充分利用预训练扩散模型的先验知识，无需微调或少样本数据即可实现高质量的图像修改[4][5]。这一特性使其在实际应用中展现出显著的实用价值，尤其在创意产业、医学影像处理和科学可视化领域具有广泛前景。

当前零样本编辑的核心研究问题集中于三个方面：（1）如何在保留原图像结构与内容的前提下，精确实现用户的编辑意图；（2）如何在文本语义与视觉表示之间建立更强的对齐；（3）如何在多约束条件下维持编辑的高效性与稳定性。随着ControlNet、注意力机制干预以及多模态条件融合等技术的涌现，零样本编辑从早期单纯依赖文本提示，演进为支持深度图、骨骼、边缘等多种控制信号的综合框架[26][49]。

## 方法分类与代表作

### 一、基于提示词编辑的范式

**1. Prompt-to-Prompt编辑框架**

Hertz等人提出的Prompt-to-Prompt方法（SIGGRAPH 2022）标志了零样本文本驱动编辑的关键突破[7][10]。该工作的核心洞察为：交叉注意力层编码了提示词中各语言标记与生成图像中空间位置的对应关系。通过在扩散过程中注入原图像的交叉注意力映射，该方法实现了四类编辑操作：词语替换（word swap）、提示词细化（prompt refinement）、注意力重加权（attention re-weighting）以及全局风格修改（global style modification）。实验表明，在512×512分辨率下，该方法对CLIP引导的文本-图像模型（如Imagen）的编辑成功率达95%以上，且编辑过程中原图像的构图与主体特征得到充分保留。该工作的创新性在于将扩散过程中的注意力机制从黑盒化的模型内部暴露出来，为后续基于注意力干预的编辑方法奠定了理论基础。

**2. 上下文扩散模型（ContextDiff）**

Yang等人在ICLR 2024提交的Contextualized Diffusion Models[3][6]识别了现有文本引导扩散模型的一个根本性不对称问题：大多数方法仅在反向过程（去噪阶段）中融合文本-视觉的交叉模态上下文，而忽视了正向过程（加噪阶段）中的文本约束。这种不对称导致文本语义在生成中的表达不充分。该方法通过在正反向过程的所有时间步均传播交叉模态上下文（包括文本条件与视觉样本的交互），实现了动态的过程轨迹调整。在text-to-image生成与text-to-video编辑两个任务上，ContextDiff相比基线方法在CLIP得分上提升3-5个百分点，在FID指标上提升约2-3个点，同时编辑后的图像与文本提示的语义一致性显著增强。

**3. CLIP驱动的无需训练文本编辑**

Yesiltepe等人的工作（arXiv 2406.00457）[2]提出了利用Stable Diffusion中已有的CLIP文本编码器执行零样本解缠编辑的方法。关键发现为：CLIP的最后一层特征层已包含足够的语义信息，扩散过程本身对语义理解的贡献有限，反而充当"视觉解码器"的角色。通过在扩散的不同阶段应用CLIP嵌入空间中的梯度指导，该方法可实现单个属性的精确操纵（如改变面部表情、改变物体颜色），定量评估显示与最先进编辑方法相比在保留图像保真度的同时提升了属性编辑的独立性。

### 二、基于注意力机制干预的编辑

**1. 自注意力分解方法**

Self-Attention Decomposition (arXiv 2510.22650)[18]提出了一个分析性框架，直接从预训练扩散模型的参数中推导出语义编辑方向，无需任何微调。该方法通过分解自注意力层中的权重矩阵，将编辑操作表述为特征空间中的线性变换。实验验证表明，通过简单的参数分析即可获得与复杂迭代优化相当甚至更优的编辑效果，大幅降低了计算成本。相比Prompt-to-Prompt方法，该方法在推理效率上提升约40%，且在复杂场景下的编辑稳定性更强。

**2. 跨注意力控制与反演**

Cross Attention Control实现(GitHub项目)[15]进一步细化了对扩散模型内部注意力机制的控制粒度。通过实现修改的DDIM反演过程[11]，该工作将现有图像映射回高斯噪声潜在空间，随后在编辑时通过选择性注入或干预交叉注意力，实现对生成图像中特定对象或区域的精确操纵。对比基础image-to-image方法，该方案在保留原图像细节的同时，对局部编辑的控制精度提升至90%以上（通过用户研究验证）。

### 三、基于参考图像的编辑

**1. 多样化条件融合框架**

一篇arXiv 2504.15723的工作[4]提出了统一文本引导和参考图像引导的扩散框架。该方法的创新在于将两种引导信号视为相互补充而非独立的条件：文本提供语义意图，参考图像提供视觉约束。通过双路径条件注入机制，模型可灵活调整两种条件的权重，支持纯文本编辑、纯参考编辑或混合编辑。在COCO-Edit基准上的评估表明，混合条件下的编辑LPIPS得分相比单一条件下降低30%，说明视觉-语义对齐显著改善。

**2. LoRA动态生成方法**

Learning to Generate LoRA (arXiv:2411.19156)[9]突破了传统编辑方法通常需要成对数据的局限。该工作提出LoRA of Change（LoC）框架，将编辑指令转化为动态的低秩适配权重。关键创新为"LoRA Reverse"训练目标，强制模型学习"变化"而非直接记忆目标图像外观，使得模型可用仅配对数据（前-后图像对）进行大规模训练。在SEED-Data-Edit和MagicBrush数据集上，该方法支持加法、删除、替换、风格迁移等六大类视觉指令，定量评估显示编辑后图像与参考图像的FID得分在2.5以内，相比先前方法Analogist和VISII分别提升15-20个百分点。

**3. 融合前后帧的视频编辑**

LoRA-Edit (arXiv:2506.10082)[12]将参考图像编辑扩展至视频域，提出了掩码感知的LoRA微调方法。通过将编辑的首帧作为参考，结合时空掩码约束，该方法可将编辑效果一致地传播至整个视频序列。相比直接对整个视频应用编辑，该方法在时间一致性指标上提升约35%，同时避免了背景不必要的扰动。

### 四、深度感知与空间约束编辑

**1. 特征引导层合成**

Zero-Shot Depth Aware Image Editing (ICCV 2025)[1]引入了特征引导层合成（Feature-Guided Layer Compositing）方法，充分利用预训练扩散模型的多层次特征表示进行逐层混合。该工作将多平面表示引入扩散潜空间，在固定深度处放置虚拟平面，可独立编辑或组合以实现3D感知的场景修改。为解决直接操作多平面表示导致的身份丧失或混合不真实问题，提出了新型多平面特征指导技术，在去噪的各个步骤中逐步对齐源潜变量与目标编辑。在场景组合和深度感知物体插入两个任务上的用户研究表明，生成图像的真实性与深度准确性相比任务特定基线提升明显，且保持了光照一致性。

**2. Diffusion Compose方法**

Compositional Depth Aware Scene Editing (ICLR 2025 spotlight)[5]专注于多物体的深度感知场景编辑。该工作的创新为：在扩散模型中显式编码深度平面的多平面表示，支持在指定深度处放置物体，同时保持遮挡关系和场景结构。通过渐进式多平面特征指导，该方法确保生成内容与周围环境的混合自然、照明一致。对比基线方法（包括最近的3D感知编辑技术），该方法在物体放置准确性与场景和谐度上的改进幅度达15-25%。

**3. 神经场景设计器（NSD）**

Neural Scene Designer (arXiv:2509.01405)[14]针对编辑过程中风格一致性缺失问题，提出了渐进自风格表示学习（PSRL）模块。该方法基于直观假设：同一图像内不同区域共享一致风格，不同图像间风格迥异。通过对比学习损失函数约束风格表示，NSD能精确捕捉细粒度的风格信息。在文本引导的修补任务上，该方法相比纯粹依赖自注意力的方法，在风格保留指标上提升约20%，生成图像的视觉一致性显著增强。

### 五、高级控制与多条件编辑

**1. ControlNet多模态条件控制**

Adding Conditional Control to Text-to-Image Diffusion Models (ControlNet, 2023)[26][49]引入了条件控制网络，使扩散模型能接纳多种控制信号（边缘图、深度图、人体骨骼、法向量等）。ControlNet通过零初始化附加网络模块与预训练扩散模型并联，在训练时供应文本提示与控制映射（如OpenPose关键点或Canny边缘），模型学习基于两种输入生成图像。每种控制方法独立训练，使得该框架高度模块化与可扩展。相比Prompt-to-Prompt方法，ControlNet通过显式空间约束提升了编辑的精准度，在人体姿态复制任务中的准确率达98%以上。

**2. 图像指导的多ControlNet融合**

Multiple ControlNets with Image Guidance (Leonardo AI)[29]进一步扩展了ControlNet框架，支持同时应用多个ControlNet模型处理单一生成任务。该特性使用户可在调整构图的同时指定人物姿态，或在添加深度纹理时保持字符外观细节的控制。通过为每个ControlNet独立设置权重与应用范围，该方案实现了对复杂多物体场景的细粒度控制。在定性评估中，多ControlNet融合相比单一ControlNet在编辑灵活性与结果多样性上均有显著提升。

**3. 语义分割驱动的编辑**

一篇arXiv:2411.01819的工作[28]融合了语义分割与图像编辑，通过高效利用预训练扩散模型进行基于分割掩码的区域编辑。该方法与标准inpainting不同在于，融合了分割信息以获得更加准确的编辑区域边界。实验表明，结合分割的编辑方法相比无分割指导的方案，编辑后图像的边界平滑度与语义连贯性提升约15-20%。

## 实验与评价总结

### 一、主要评估指标与数据集

在零样本图像编辑的实验评价中，研究界形成了多维度的定量与定性评估体系[37][40]。分布对齐指标中，**Fréchet Inception Distance (FID)**[37][40]是最广泛使用的质量度量，通过比较生成图像与真实图像的InceptionNet特征分布来评估生成质量，FID值越低表示质量越高。**Learned Perceptual Image Patch Similarity (LPIPS)**[37]通过深层网络特征空间衡量感知相似度，优于像素级指标（PSNR、SSIM），更符合人类视觉感知。语义对齐方面，**CLIP Score**[37][59]通过文本嵌入与图像嵌embedding的余弦相似度量化提示词-图像对齐程度，值域为0-100，对文本引导编辑尤为重要[50]。

常用评估基准包括：DrawBench（包含200张多样化提示），COCO-Edit（基于MSCOCO的编辑子集），EditBench（涵盖多类编辑操作），I²EBench（包含2000+编辑图像与4000+指令的综合基准）[59]。近期工作ComplexBench-Edit[56]引入了链式依赖编辑评估，考察模型在多约束条件下的组合推理能力。

### 二、保真度与编辑精度的权衡

所有零样本编辑方法在实验中均面临一个根本性张力：**编辑强度与内容保留的权衡**。基准研究表明[8][17]，对于DDIM反演方法，使用更多的去噪步骤（如50步vs.20步）虽能提升反演保真度（重建FID从8.2降至3.5），但在相同去噪步数下增加编辑强度会急剧降低编辑成功率。多项研究（包括Dual-Schedule Inversion[8]和Faithfulness Guidance and Scheduling[17]）表明，采用分阶段的引导策略——早期步骤强调布局保留，中期步骤引入编辑，后期步骤强化细节——相比恒定引导可将编辑成功率提升15-25%。

特别地，基于参考图像的方法（如LoRA-Edit[12]和ContextDiff[3]）在混合条件下表现更优，相比单纯文本编辑在LPIPS上降低20-30%，说明额外的视觉约束显著增强了编辑的受控性。然而，注意力机制编辑方法（Prompt-to-Prompt、Self-Attention Decomposition）在实现精细控制时往往面临"过度编辑"问题——对注意力映射的过度干预可能导致物体属性混淆或不自然的过渡。

### 三、语义理解与对齐的深层问题

一项关键发现来自CLIP驱动编辑研究[50]：Stable Diffusion中的语义理解主要源于CLIP文本编码器，而非扩散过程本身。通过逐层探测分析，该工作表明CLIP输出层的特征-人类语义判断的相关性最高，而随着去噪步骤的进行，这种对齐反而逐步退化。这暗示：现有大规模扩散模型的语义编辑能力本质上受限于其预训练文本编码器的容量，单纯通过提升模型规模或数据量难以突破这一瓶颈。

对象计数错误的系统研究（arXiv:2510.11117）[38]揭示了扩散模型的另一个根本性限制：即使在规模从2B扩展到12B、训练数据从1K增至500K的情况下，生成指定数量物体的准确度仍随目标数量增加而单调下降，在10个物体时的准确率仅约20%。分析表明，扩散模型优化的是噪声先验而非文本指令，物体计数是相对较弱的信号，易被随机噪声模式压过。这一发现对设计编辑约束机制具有重要启示：仅依赖文本提示的编辑方法在处理多物体精确编辑时可靠性有限，必须辅以空间约束（如深度图、掩码或骨骼）。

### 四、时间一致性与视频编辑的挑战

将扩散编辑扩展至视频时，**时间一致性**成为关键瓶颈[33][36]。标准方法（逐帧独立编辑）导致帧间严重闪烁与不连贯。最新工作采用本地-全局策略：本地层面通过时间注意力与3D卷积维持短序列一致性，全局层面引入流引导的循环潜变量传播以确保整个序列的稳定性[33]。即便如此，对于长视频（>100帧），现有方法的时间一致性指标（flow warping error）仍在可接受范围的下界。基于对象中心表示的视频编辑（Compositional Video Synthesis[54]）通过显式建模物体轨迹与姿态变化，在时间一致性上实现了20-30%的改善，但计算成本显著增加。

### 五、方法间的定性对比总结

| 方法类别 | 编辑精度 | 语义保留 | 计算效率 | 适用场景 |
|---------|--------|--------|--------|---------|
| 文本提示编辑 | 中等 | 高 | 高 | 全局风格/内容修改 |
| 注意力干预 | 中 | 中高 | 高 | 局部物体编辑 |
| 参考图像 | 中高 | 中 | 中 | 风格迁移/内容融合 |
| 深度感知 | 高 | 高 | 低 | 3D场景编辑 |
| ControlNet多条件 | 很高 | 中高 | 中 | 精确空间控制 |

## 趋势与挑战

### 一、参数高效适配的深化

当前扩散模型编辑方法的一个重要转向是从全模型微调向**参数高效适配**的演进。LoRA（Low-Rank Adaptation）以其极小的参数增量（通常<1%）展现了强大的适配能力[9][12]。未来研究将深化以下方向：（1）**任务特定LoRA设计**——针对特定编辑类型（人脸、物体、场景）的定制化秩分解策略；（2）**动态LoRA生成**——如LoC框架所示，直接从编辑指令生成LoRA权重，而非依赖预训练权重库；（3）**多LoRA组合**——通过加权融合多个任务特定LoRA实现复杂编辑的协调。这些方向将使模型适配更加灵活且计算高效。

### 二、推理加速与实时编辑

当前扩散编辑的核心瓶颈是**推理延迟**。标准50-100步的去噪过程在消费级GPU上需5-30秒，严重限制了交互式应用[43]。2025年的研究热点将包括：（1）**一步扩散模型**[32]——通过蒸馏或对抗训练将采样步数降至1-4步，已有工作如CycleGAN-Turbo在sketch-to-image任务上实现了与ControlNet相当的质量；（2）**推理时扩展**[46]——通过搜索更优噪声而非增加去噪步数来改善质量，实验表明在相同计算预算下可获得2-3倍的质量提升；（3）**硬件优化与模型压缩**——包括量化、结构化剪枝、DeepCache等缓存技术，业界报告已实现2-5倍的推理加速[58]。

### 三、可解释性与可控性的融合

随着扩散模型在高风险领域（医学影像、司法鉴定）的应用增加，**编辑过程的可解释性**成为迫切需求。最近工作（ConceptAttention[48]、DF-RISE可视化[45]）通过注意力热力图、概念激活向量等技术揭示了模型在各去噪步骤的关注焦点。2025年的研究将进一步：（1）**细粒度因果干预**——精确定位和分离模型中导致特定编辑效果的因果因子；（2）**交互式编辑界面设计**——将可解释性转化为用户可直观控制的参数（如概念滑块、区域权重等）；（3）**编辑可逆性保证**——通过可证明的约束确保编辑操作在指定范围内，防止不可预期的副作用。

### 四、多模态条件融合的标准化

当前多条件编辑（文本+图像+空间约束）缺乏统一框架。不同工作采用独立或串行的条件注入策略，导致条件间的相互干扰与冲突[29][44]。2025年的研究方向：（1）**标准化多模态条件融合架构**——建立文本、参考图像、空间约束在潜空间中的协调注入机制；（2）**条件冲突解决机制**——当多个条件给出矛盾指示时的自适应权重调整或显式冲突消解策略；（3）**跨模态语义对齐**——确保不同模态条件在语义层面的一致性，避免"多条件陷阱"（multiple conditions trap）导致的质量下降。

### 五、边界场景与失败模式的深度理解

尽管零样本编辑已取得显著进展，但其在复杂、边界场景中的可靠性仍待提升。最近的失败模式分析[41]表明，看似自然的文本提示可能触发意外生成错误——例如"一个红色的苹果在桌子上"可能生成形状扭曲的物体。2025年的研究需要：（1）**系统化失败模式分类与检测**——建立可自动诊断编辑失败原因的工具；（2）**鲁棒性增强**——通过对抗训练、不确定性量化或集成方法提升编辑在分布外示例上的鲁棒性；（3）**用户反馈的闭环优化**——将编辑过程中的失败案例作为反馈信号，实现模型的持续改进。

## 结论

扩散模型驱动的零样本图像编辑在2022-2025年间实现了从概念验证向实用工具的转变。通过Prompt-to-Prompt的注意力机制启蒙、ControlNet的多模态条件控制、以及LoRA动态生成等创新，该领域已形成了五大技术范式。当前主要挑战包括：编辑精度与语义保留的张力、语言模型容量的瓶颈、视频序列的时间一致性难题，以及边界场景的可靠性不足。

展望2025年及之后，该领域将沿着三条主线演进：一是**参数高效与推理加速的深度结合**，通过LoRA+一步扩散+硬件优化实现真正的实时交互；二是**多模态条件的标准化融合与冲突解决**，为复杂场景编辑提供坚实基础；三是**可解释性与用户可控性的深度融合**，将黑盒模型变为透明、可审计的编辑工具。这些方向的推进将使零样本图像编辑从学术工具演进为创意、医学、科学等领域的核心生产力工具。同时，安全性、公平性与版权保护等社会层面的议题也将成为该领域不可回避的研究命题。

## 参考文献

[1] Parihar R, et al. Zero-Shot Depth Aware Image Editing with Diffusion Models[C]//Proceedings of ICCV, 2025.

[2] Yesiltepe H, Dalva Y, Yanardag P. The Curious Case of End Token: A Zero-Shot Disentangled Image Editing using CLIP[J]. arXiv preprint arXiv:2406.00457, 2024.

[3] Yang L, Zhang Z, Yu Z, et al. Contextualized Diffusion Models for Text-Guided Image and Video Generation[J]. arXiv preprint arXiv:2402.16627, 2024.

[4] Anonymous. A Diffusion-Based Framework for Zero-Shot Image Editing[J]. arXiv preprint arXiv:2504.15723, 2025.

[5] Parihar R, et al. Diffusion Compose: Compositional Depth Aware Scene Editing in Diffusion Models[C]//Proceedings of ICLR 2025 Spotlight.

[6] Yang L, et al. Cross-Modal Contextualized Diffusion Models for Text-Guided Visual Generation and Editing[C]//Proceedings of ICLR, 2024.

[7] Hertz A, Mokady R, Tenenbaum J, et al. Prompt-to-Prompt Image Editing with Cross Attention Control[J]. arXiv preprint arXiv:2208.01626, 2022.

[8] Huang J, Huang Y, Liu J, et al. Dual-Schedule Inversion: Training- and Tuning-Free Inversion for Real Image Editing[J]. arXiv preprint arXiv:2412.11152, 2024.

[9] Chen J, et al. Learning to Generate LoRA for the Editing Instruction from A Single Image[J]. arXiv preprint arXiv:2411.19156, 2024.

[10] Hertz A, et al. Prompt-to-Prompt Image Editing with Cross Attention Control[C]//Proceedings of SIGGRAPH, 2022.

[11] Rombach R, et al. High-Resolution Image Synthesis with Latent Diffusion Models[C]//CVPR, 2022. (Referenced as DDIM Inversion context)

[12] Gao C, et al. LoRA-Edit: Controllable First-Frame-Guided Video Editing via Mask-Aware LoRA Fine-Tuning[J]. arXiv preprint arXiv:2506.10082, 2025.

[13] Runware Documentation. Inpainting: Selective Image Editing[EB/OL]. https://runware.ai/docs/image-inference/inpainting, 2024.

[14] Anonymous. Neural Scene Designer: Self-Styled Semantic Image Manipulation[J]. arXiv preprint arXiv:2509.01405, 2024.

[15] Bloc97. Cross Attention Control with Stable Diffusion[EB/OL]. https://github.com/bloc97/CrossAttentionControl, 2023.

[16] FullStack Data Science. Edit Your Images Easily with Inpainting and Diffusion[EB/OL]. https://fullstackdatascience.com/blogs/edit-your-images-easily-with-inpainting-and-diffusion-ksvvij, 2024.

[17] Cho J, et al. Faithfulness Guided Image-to-Image Diffusion[J]. Emergent Mind, 2025.

[18] Anonymous. Self-Attention Decomposition For Training Free Diffusion Editing[J]. arXiv preprint arXiv:2510.22650, 2024.

[19] Ruiz N, Li Y, Jampani V, et al. DreamBooth: Fine Tuning Text-to-Image Diffusion Models for Subject-Driven Generation[J]. arXiv preprint arXiv:2208.12242, 2022.

[20] Gal R, et al. An Image is Worth One Word: Personalizing Text-to-Image Generation using Textual Inversion[C]//ICLR, 2023.

[21] Zheng C, et al. EditableNeRF: Editing Topologically Varying Neural Radiance Fields by Key Points[C]//CVPR, 2023.

[22] Ruiz N, et al. DreamBooth Official Project[EB/OL]. https://dreambooth.github.io, 2022.

[23] Hugging Face. Textual Inversion Documentation[EB/OL]. https://huggingface.co/docs/diffusers/en/training/text_inversion, 2024.

[24] Chen J-K, Lyu J, Wang Y-X. NeuralEditor: Editing Neural Radiance Fields via Manipulating Point Clouds[C]//CVPR, 2023.

[25] Anonymous. Unleashing the Potential of the Diffusion Model in Few-shot Semantic Segmentation[J]. Proceedings of NeurIPS, 2024.

[26] Zhang L, Agrawala M. Adding Conditional Control to Text-to-Image Diffusion Models[C]//ICCV, 2023.

[27] Anonymous. Latent Diffusion-based Art Style Transfer Model[J]. CS231n Course Project, 2024.

[28] Anonymous. Integration of Semantic Segmentation and Image Editing using Pretrained Diffusion Models[J]. arXiv preprint arXiv:2411.01819, 2024.

[29] Leonardo AI. Multiple ControlNets with Image Guidance[EB/OL]. https://leonardo.ai/news/multiple-controlnets-with-image-guidance/, 2024.

[30] Cheung J, et al. Towards Highly Realistic Artistic Style Transfer via Stable Diffusion with Step-Aware and Layer-Aware Prompt[J]. arXiv preprint arXiv:2404.11474, 2024.

[31] Zhang J, Li X, Zhang Q, et al. HumanRef: Single Image to 3D Human Generation via Reference-Guided Diffusion[J]. arXiv preprint arXiv:2311.16961, 2023.

[32] Parmar G, Park T, Narasimhan S, et al. One-Step Image Translation with Text-to-Image Models[J]. arXiv preprint arXiv:2403.12036, 2024.

[33] Zhou S, et al. Upscale-A-Video: Temporal-Consistent Diffusion Model for Real-World Video Super-Resolution[C]//CVPR, 2024.

[34] Anonymous. Guided Image-to-Image Diffusion Models[J]. OpenReview, 2024.

[35] TensorFlow. pix2pix: Image-to-image Translation with a Conditional GAN[EB/OL]. https://www.tensorflow.org/tutorials/generative/pix2pix, 2024.

[36] Weng L. Diffusion Models for Video Generation[EB/OL]. https://lilianweng.github.io/posts/2024-04-12-diffusion-video/, 2024.

[37] Pruna AI. Measuring What Matters: Objective Metrics for Image Generation Assessment[EB/OL]. https://huggingface.co/blog/PrunaAI/objective-metrics-for-image-generation-assessment, 2024.

[38] Anonymous. Demystifying Numerosity in Diffusion Models—Limitations and Insights[J]. arXiv preprint arXiv:2510.11117, 2024.

[39] UnitX Labs. Exploring Diffusion Models in Machine Vision Systems 2025[EB/OL]. https://www.unitxlabs.com/diffusion-models-machine-vision-systems-2025/, 2025.

[40] Paperspace Blog. A Review of the Image Quality Metrics used in Image Generative Models[EB/OL]. https://blog.paperspace.com/review-metrics-image-synthesis-models/, 2024.

[41] Anonymous. Discovering Failure Modes of Text-Guided Diffusion Models[C]//ICLR, 2024.

[42] JetBrains AI Blog. Why Diffusion Models Could Change Developer Workflows in 2026[EB/OL]. https://blog.jetbrains.com/ai/2025/11/why-diffusion-models-could-change-developer-workflows-in-2026/, 2025.

[43] ApX Machine Learning. Latency & Throughput Considerations in Diffusion Models[EB/OL]. https://apxml.com/courses/deploying-diffusion-models-scale/chapter-1-scaling-challenges-architectures/latency-throughput-considerations, 2025.

[44] Qin Z, Shuai X, Ding H. SceneDesigner: Controllable Multi-Object Image Generation with 9-DoF Pose Manipulation[C]//NeurIPS 2025 Spotlight.

[45] Anonymous. Explaining Generative Diffusion Models via Visual Analysis and Attention Maps[J]. arXiv preprint arXiv:2402.10404, 2024.

[46] Anonymous. Inference-Time Scaling for Diffusion Models Beyond Scaling Denoising Steps[J]. arXiv preprint arXiv:2501.09732, 2025.

[47] Anonymous. Towards Generalized Multi-Image Editing for Unified Multimodal Models[J]. arXiv preprint arXiv:2601.05572, 2025.

[48] Anonymous. ConceptAttention: Diffusion Transformers Learn Highly Interpretable Representations[C]//ICML, 2025.

[49] ControlNet Stable Diffusion Art Guide[EB/OL]. https://stable-diffusion-art.com/controlnet/, 2024.

[50] Anonymous. CLIP is All You Need for Human-like Semantic Representations in Stable Diffusion[J]. arXiv preprint arXiv:2511.08075, 2024.

[51] Anonymous. Compositional Scene Modeling with An Object-Centric Diffusion Transformer[J]. OpenReview ICLR 2025 Submission.

[52] TroubleChute. Mastering ControlNet on Stable Diffusion: Your Complete Guide[EB/OL]. https://www.youtube.com/watch?v=BbYJd9kRjLg, 2023.

[53] Liu X, et al. More Control for Free! Image Synthesis with Semantic Diffusion Guidance[C]//WACV, 2023.

[54] Akan A K, Yemez Y. Compositional Video Synthesis by Temporal Object-Centric Learning[J]. arXiv preprint arXiv:2507.20855, 2025.

[55] Anonymous. Vision Foundation Model Aligned VAE for Latent Diffusion Models[J]. arXiv preprint arXiv:2501.01423, 2025.

[56] Anonymous. ComplexBench-Edit: Benchmarking Complex Instruction Following in Image Editing[J]. arXiv preprint arXiv:2506.12830, 2025.

[57] Hooda A, et al. Adversarially Robust Deepfake Detection via Feature Similarity Learning[J]. arXiv preprint arXiv:2403.08806, 2024.

[58] AIoT-MLSys Lab. Efficient Diffusion Models: A Survey[J]. TMLR, 2025.

[59] Anonymous. A Comprehensive Benchmark for Instruction-based Image Editing (I²EBench)[J]. arXiv preprint arXiv:2408.14180, 2024.

[60] Hooda A, et al. Detection of Adversarial Diffusion Deepfakes Using Disjoint Ensembles (D4)[C]//WACV, 2024.