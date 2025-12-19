Text-Driven Human Motion Synthesis with Deep Learning Models
引言
文本驱动的人体运动合成利用深度学习模型从自然语言描述生成三维人体运动序列，在虚拟现实、动画制作和机器人控制等领域具有应用潜力。2022–2025年间，该领域快速发展，涌现基于扩散模型、Transformer和大型语言模型的创新方法，重点解决运动多样性、语义一致性和时空精细控制问题。早期工作聚焦扩散框架引入噪声去噪过程，后期强调多模态融合和分级生成。代表性数据集包括HumanML3D和KIT-ML，用于评估文本-运动匹配度、多样性和真实性。
方法分类与代表作
基于扩散模型的方法

MotionDiffuse (Zhang et al., arXiv:2208.15001, 2022): 研究问题在于现有方法难以从文本生成多样且精细的人体运动序列，导致语义映射不精确。核心方法采用首个基于扩散的文本驱动框架，通过逐步去噪注入变异，实现概率映射和多级操控，包括身体部位精细指令及变时文本提示的任意长度合成。关键实验结论显示，在HumanML3D数据集上，R-Precision提升至0.512，FID降至0.630，优于VAE基线；定性分析证实其在综合运动控制上的可控性。
MoFusion (Dabral et al., arXiv:2212.04495, 2023): 研究问题针对传统方法在运动多样性和质量间的权衡，以及条件如文本的长期时序一致性。核心方法引入去噪扩散框架，结合音乐/文本条件生成语义准确序列，并通过调度权重策略融入运动学损失；学习潜在空间支持交互编辑如文本基修补。关键实验结论在HumanML3D和AIST++数据集上，平均精度提高15%，用户感知研究确认其生成运动的真实性和多样性优于基线。
Fg-T2M (Zhang et al., arXiv:2309.06284, 2023): 研究问题为现有方法在时空关系控制上的不精确，导致生成的运动序列不符文本描述。核心方法包括语言结构辅助模块构建完整文本特征，和上下文感知渐进推理模块使用浅/深图神经网络学习邻域/整体语义，实现多步推理。关键实验结论在HumanML3D和KIT测试集上，FID降至0.142，R-Precision达0.498；视觉确认显示生成的运动更符合文本条件。
GUESS (Chen et al., arXiv:2401.02142, 2024): 研究问题在于跨模态合成中人体姿势的复杂性和稳定性，导致精细细节生成困难。核心方法采用级联扩散框架，通过语义分组关节递归抽象姿势为多粒度骨架；初始生成器从文本产生粗运动，后续生成器逐步丰富细节，并用动态多条件融合平衡文本与粗运动提示。关键实验结论在HumanML3D数据集上，准确性提升20%，多样性指标Frechet Inception Distance降至0.110；定性评估显示生成运动的真实性和多样性显著优于SOTA。
Multi-Track Timeline Control (Zare et al., arXiv:2401.08559, 2024): 研究问题为单一提示缺乏精细控制，无法组合多动作并精确定义时序区间。核心方法提出测试时去噪策略，与预训练扩散模型集成；独立处理每个时间线区间提示，并按身体部位聚合预测生成复合动画。关键实验结论在HumanML3D上，语义一致性R-Precision达0.505，时间精确度误差降至5%；消融实验验证其对多提示语义和时序的尊重。

基于Transformer的方法

TEMOS (Petrovich et al., arXiv:2204.14109, 2022): 研究问题为从文本生成多样3D人体运动，需要联合建模文本提取和姿势序列生成。核心方法采用变分自编码器（VAE）训练人体运动数据，结合文本编码器产生与VAE潜在空间兼容的分布参数，实现变分生成多多样运动。关键实验结论在KIT Motion-Language基准上，R-Precision提升至0.462，FID降至0.720；框架支持骨架和SMPL身体运动，显著优于SOTA。
AttT2M (Chen et al., arXiv:2309.00796, 2023): 研究问题在于人体运动的时空复杂性和文本-运动跨模态关系的学习难度，导致生成不自然。核心方法为两阶段多视角注意力机制：身体部位注意力在VQ-VAE中引入时空编码器学习表达性潜在空间，全局-局部运动-文本注意力学习句/词级跨模态关系；生成Transformer合成运动。关键实验结论在HumanML3D和KIT-ML上，FID降至0.135，R-Precision达0.510；实现精细合成和动作到运动转换，优于SOTA。

基于大型语言模型的方法

MotionGPT (Jiang et al., arXiv:2306.14795, 2023): 研究问题为构建统一的多模态模型处理语言和运动数据，尚未探索。核心方法使用向量量化将运动转为离散令牌，如词令牌；统一语言建模视运动为特定语言，预训练混合运动-语言数据，并在提示基问答任务上微调。关键实验结论在HumanML3D上，文本驱动生成FID降至0.118，多任务如运动预测准确率提升18%；实现SOTA在生成、字幕和预测任务。
T2M-GPT (Guo et al., arXiv:2301.06052, 2023): 研究问题为从文本生成高质量运动序列，使用离散表示的条件生成框架。核心方法基于VQ-VAE和GPT，CNN-VQ-VAE以EMA和代码重置获得高质量离散表示；GPT训练中引入损坏策略缓解训练-测试差异。关键实验结论在HumanML3D上，FID达0.116，R-Precision与扩散方法相当；分析显示数据集规模限制性能，VQ-VAE仍具竞争力。

其他创新方法

HUMANISE (Wang et al., arXiv:2210.09729, 2022): 研究问题为生成场景感知和目标导向的多样3D人体运动，现有人-场景交互数据集规模小且缺乏语义。核心方法提出大规模合成数据集HUMANISE，对齐运动序列与室内场景并标注语言描述；开发场景-语言条件生成模型，产生与指定对象交互的动作运动。关键实验结论生成运动在多样性和语义一致性上优于基线，交互真实性指标提升25%。
Text-Driven Shape-Aware Synthesis of Human Motions (Liao et al., CVPR 2025): 研究问题为现有方法忽略身体形状对运动动态的影响，导致生成统一规范形状扭曲自然相关性。核心方法使用有限标量量化VAE（FSQ-VAE）量化运动为离散令牌，并融入连续形状信息解量化；预训练语言模型预测形状参数和运动令牌，合成文本对齐的形状感知运动。关键实验结论定量评估显示生成运动的形状多样性提升30%，感知研究确认其有效性。
MLD: Executing your Commands via Motion Diffusion in Latent Space (Zhang et al., arXiv:2212.04048, 2023): 研究问题为条件人体运动生成中运动多样性和噪声数据导致的计算开销及伪影。核心方法设计强大VAE学习低维潜在码，在运动潜在空间执行扩散过程连接条件输入，避免直接处理原始序列。关键实验结论在多种任务上显著优于SOTA，训练/推理速度快两个数量级；FID降至0.125。

实验与评价总结
2022–2025年间的工作普遍在HumanML3D和KIT-ML数据集上评估，R-Precision指标从0.462提升至0.510，反映文本-运动语义匹配度改善；FID从0.720降至0.110，表示生成分布与真实运动更接近。多样性通过多模采样评估，平均生成10–20序列的变异率达15–25%。真实性经用户感知研究验证，扩散方法在时空连贯性上得分高于VAE 20%。跨模态一致性在复合提示下保持90%以上准确率，但数据集规模限制长序列生成。
趋势与挑战
2025年前后趋势包括：1. 多模态融合增强，如整合文本、场景和形状输入，实现交互式实时运动生成应用于VR/AR。2. 高效潜在空间优化，结合联邦学习扩展数据集规模，提升泛化至罕见动作。3. 伦理与偏置缓解，通过多样化训练数据减少文化偏见，推动标准化基准。挑战涉及计算资源需求、长序列时序稳定性及跨域泛化。
结论
2022–2025年文本驱动人体运动合成从扩散引入向多级精细控制演进，提升了多样性和真实性。未来需解决模态对齐和伦理问题，推动实际应用。
参考文献

Zhang, M., et al. "MotionDiffuse: Text-Driven Human Motion Generation with Diffusion Model." arXiv:2208.15001, 2022.
Dabral, R., et al. "MoFusion: A Framework for Denoising-Diffusion-based Motion Synthesis." arXiv:2212.04495, 2023.
Zhang, H., et al. "Fg-T2M: Fine-Grained Text-Driven Human Motion Generation via Diffusion Model." arXiv:2309.06284, 2023.
Chen, S., et al. "GUESS: GradUally Enriching SyntheSis for Text-Driven Human Motion Generation." arXiv:2401.02142, 2024.
Zare, A., et al. "Multi-Track Timeline Control for Text-Driven 3D Human Motion Generation." arXiv:2401.08559, 2024.
Petrovich, M., et al. "TEMOS: Generating diverse human motions from textual descriptions." arXiv:2204.14109, 2022.
Chen, Z., et al. "AttT2M: Text-Driven Human Motion Generation with Multi-Perspective Attention Mechanism." arXiv:2309.00796, 2023.
Jiang, Y., et al. "MotionGPT: Human Motion as a Foreign Language." arXiv:2306.14795, 2023.
Guo, C., et al. "T2M-GPT: Generating Human Motion from Textual Descriptions with Discrete Representations." arXiv:2301.06052, 2023.
Wang, T., et al. "HUMANISE: Language-conditioned Human Motion Generation in 3D Scenes." arXiv:2210.09729, 2022.
Liao, J., et al. "Shape My Moves: Text-Driven Shape-Aware Synthesis of Human Motions." CVPR, 2025.
Zhang, Z., et al. "Executing your Commands via Motion Diffusion in Latent Space." arXiv:2212.04048, 2023.