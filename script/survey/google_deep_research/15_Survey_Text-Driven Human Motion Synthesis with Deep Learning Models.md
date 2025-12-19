深度学习驱动的文本生成人体动作综述：从离散表征到物理感知世界模型 (2022–2025)
1. 引言
人体动作合成（Human Motion Synthesis）作为计算机视觉、计算机图形学与人工智能交叉领域的核心课题，长期以来致力于解决如何赋予数字角色以逼真、流畅且富有语义行为能力的问题。随着元宇宙（Metaverse）、数字孪生（Digital Twins）以及具身智能（Embodied AI）的飞速发展，能够通过自然语言指令直接生成三维人体动作的「文本驱动动作生成」（Text-Driven Human Motion Generation）技术，已成为连接人类意图与虚拟/物理世界行为的关键接口。

回顾过去的发展历程，早期的动作生成主要依赖于检索式方法或确定性的序列到序列（Seq2Seq）模型，这类方法往往难以捕捉动作数据的多模态分布特性，即同一句文本描述（如“一个人在高兴地跳舞”）对应着无数种合理的运动轨迹。2022 年前后，随着生成式人工智能（AIGC）的爆发，该领域迎来了范式转移。以扩散模型（Diffusion Models）和自回归大语言模型（LLM-based Autoregressive Models）为代表的深度生成模型，凭借其强大的概率分布建模能力，彻底改变了动作合成的研究格局。

本综述旨在对 2022 年至 2025 年间该领域的代表性研究成果进行穷尽式的梳理与深度剖析。我们将这一时期的技术演进划分为三个阶段：扩散模型的崛起解决了动作多样性与生成质量的矛盾；离散自回归模型的发展实现了动作与语言在语义空间的统一；而物理与交互感知生成的兴起（2024-2025）则标志着研究重心从单纯的“运动学拟合”向“具身物理交互”的跨越。通过对 Motion Diffusion Model (MDM)、MotionGPT、SemGeoMo、WISA 等里程碑式工作的详细解读，本文将揭示从“生成动作”迈向“生成行为”的技术演进逻辑，并基于严谨的实验数据总结各技术路线的优劣，最终展望 2025 年后迈向通用世界模拟器的研究趋势。

2. 方法分类与代表性工作
根据生成机制的数学本质及底层数据表征形式的差异，现有工作可归纳为三大核心类别：基于扩散模型的连续生成框架、基于离散标记的自回归生成框架，以及面向物理与交互的场景感知生成框架。

2.1 基于扩散模型的连续生成 (Diffusion-Based Continuous Generation)
扩散模型通过学习将高斯噪声逐步去噪还原为数据分布的过程，展现出了卓越的生成质量和多样性。在人体动作生成领域，该类方法主要解决如何在高维连续的骨骼空间中建立与文本语义对齐的概率映射。

Motion Diffusion Model (MDM)
来源：ICLR 2023 / arXiv 2022    

研究问题： 传统的 VAE 或 GAN 模型在生成复杂动作时容易出现模式崩塌（Mode Collapse），且难以在长序列生成中保持动作的多样性与时序连贯性。此外，如何将几何约束（如脚不滑步）有效地融入概率生成过程也是一大挑战。

核心方法： MDM 是该领域首个具有里程碑意义的扩散模型框架。其核心创新在于摒弃了图像生成中常用的“预测噪声”（predicting ϵ）策略，转而在每个扩散步直接预测原始信号（predicting x 
0
​
 ）。这种设计使得模型能够在推理的中间步骤直接计算关节位置和速度，从而能够显式地施加几何损失函数（Geometric Losses），如脚部接触一致性损失，强制模型生成符合物理运动学规律的动作。在架构上，MDM 采用了轻量级的 Transformer Encoder，利用分类器无关引导（Classifier-Free Guidance）技术来增强文本条件对生成过程的控制力。

关键实验结论： 在 HumanML3D 和 KIT-ML 基准上，MDM 将 FID 分数降低至 0.611（HumanML3D），显著优于同期基于 VAE 的 TEMOS 方法。实验证明，预测 x 
0
​
  的策略在动作领域不仅收敛更快，而且生成的动作在脚部接触等细节上更加真实，有效缓解了“滑步”现象。

Motion Latent Diffusion (MLD)
来源：CVPR 2023    

研究问题： 人体动作数据具有极高的时间冗余度，直接在原始骨骼关节空间（Raw Motion Space）进行扩散过程计算开销巨大，且容易引入高频抖动噪声，导致推理速度缓慢，难以满足实时应用需求。

核心方法： MLD 提出了一种“潜在空间扩散”（Latent Diffusion）范式。该方法首先训练一个强大的变分自编码器（Motion VAE），将高维、长序列的动作数据压缩为低维、紧凑的潜在变量（Latent Variables）。随后，扩散模型仅在这一低维潜在空间上进行训练和推理。为了处理变长序列，MLD 在 VAE 的编解码器中引入了掩码机制和位置编码。这种设计将繁重的时序建模任务剥离给 VAE，使得扩散模型能专注于学习动作分布的流形结构。

关键实验结论： MLD 实现了性能与效率的双重突破。在保持 SOTA 生成质量（FID 0.473 on HumanML3D）的同时，其推理速度比原始空间的 MDM 快了两个数量级（约 50 倍）。这证明了动作数据的流形分布实际上位于一个低维空间，潜在扩散是实现高效生成的必经之路。

ReMoDiffuse: Retrieval-Augmented Motion Diffusion
来源：ICCV 2023    

研究问题： 纯生成模型（Generative Models）完全依赖内部参数记忆数据分布，当面对罕见、复杂或组合性的文本描述时（例如“先做一个侧手翻然后跌跌撞撞地后退”），往往因缺乏先验知识而产生语义偏差或动作失真。

核心方法： ReMoDiffuse 引入了检索增强（Retrieval-Augmented）机制，将生成模型从“封闭系统”转变为“开放系统”。在生成过程中，模型首先根据输入文本从外部动作数据库中检索语义最相似的动作片段作为参考。为了有效利用这些参考信息，该论文设计了语义调制注意力机制（Semantic-Modulated Attention, SMA），该模块能够动态地根据文本指令，从检索到的特征中选择性地吸收有用的运动学细节，并注入到扩散模型的去噪过程中。此外，提出的**条件混合（Condition Mixture）**策略优化了分类器无关引导在多条件下的表现。

关键实验结论： 检索增强机制极大地提升了模型对复杂语义的泛化能力。ReMoDiffuse 在 HumanML3D 的 R-Precision (Top-1) 指标上达到了惊人的 0.800+，并在多样性指标上保持领先。实验表明，对于训练集中出现频率较低的动作类别，检索机制能提供关键的运动学先验，显著减少生成伪影。

HOIAnimator: Perceptive Diffusion Models
来源：CVPR 2024    

研究问题： 传统文本生成动作往往忽略环境与物体的存在，导致生成的人体与物体之间缺乏合理的交互（如手穿过桌子、坐姿悬空）。如何在没有显式物体轨迹输入的情况下，仅凭文本生成逼真的人-物交互（HOI）动画是该论文解决的核心问题。

核心方法： HOIAnimator 提出了一种感知扩散模型（Perceptive Diffusion Model）。该模型构建了一个能够感知场景几何特征和物体属性的扩散架构。它不仅将文本作为条件，还将物体的 3D 几何特征（通过点云或体素编码）编码进扩散过程。为了增强交互的物理真实感，模型引入了基于距离场的交互损失函数，并利用一种新颖的接触图预测模块来引导人体关节向物体表面靠拢。

关键实验结论： 在 BEHAVE 和 InterCap 等交互数据集上，HOIAnimator 生成的交互动作在物理接触准确率和语义一致性上均优于基线模型。它证明了将场景感知能力融入扩散模型是实现从“独舞”到“交互”跨越的关键技术路径。

ReMoS: Reactive Motion Synthesis
来源：ECCV 2024    

研究问题： 除人物交互外，**人-人交互（Human-Human Interaction）**更为复杂。如何根据一个人的动作生成另一个人自然的反应动作（如格斗中的闪避、双人舞中的配合），是实现多角色虚拟互动的难点。

核心方法： ReMoS 提出了一种基于去噪扩散的反应动作合成框架。该模型以第一个人的动作序列作为强条件，预测第二个人的反应动作。为了捕捉两人之间复杂的时空依赖关系，ReMoS 设计了时空交叉注意力机制（Spatio-Temporal Cross-Attention），使得生成的反应动作不仅在时间上同步，在空间位置上也具有合理的相对关系（如保持社交距离或接触）。

关键实验结论： 在双人交互数据集（如 ReMoCap）上的实验显示，ReMoS 能够生成高度协调的反应动作，即使在激烈的格斗或复杂的舞蹈场景中，也能保持两人动作的逻辑连贯性，填补了多人交互生成领域的空白。

2.2 基于离散标记的自回归生成 (Token-Based Autoregressive Generation)
受大语言模型（LLM）成功的启发，这一类方法试图将连续的人体动作离散化为类似词汇的 Token 序列，从而利用 Transformer 强大的上下文建模能力，将动作生成转化为“下一个 Token 预测”的分类问题。

T2M-GPT
来源：CVPR 2023    

研究问题： 扩散模型虽然效果好，但推理过程需要迭代去噪，计算成本高。相比之下，自回归模型推理高效，但以往在连续空间上的自回归常因误差累积导致动作“冻结”或发散。如何利用离散表征解决这一问题？

核心方法： T2M-GPT 采用经典的 VQ-VAE + GPT 两阶段架构。第一阶段，训练一个一维卷积 VQ-VAE，将连续的动作帧序列映射为离散的 Codebook 索引序列（Motion Tokens）。第二阶段，使用类似 GPT 的 Transformer Decoder，以文本嵌入为条件，自回归地预测动作 Token 序列。为了解决训练时的“暴露偏差”（Exposure Bias）问题，T2M-GPT 引入了一种简单而有效的随机掩码策略（Corrupt Strategy），在训练中随机替换部分历史 Token，强迫模型学习从含噪历史中恢复未来的能力。

关键实验结论： T2M-GPT 以极简的架构取得了惊艳的效果。在 HumanML3D 上，其 FID 分数降至 0.116，大幅优于同期的扩散模型（如 MotionDiffuse 的 0.630），证明了离散表征能够更有效地滤除高频噪声，生成视觉上更平滑、细节更丰富的动作，且推理速度极快。

MotionGPT
来源：NeurIPS 2023    

研究问题： 现有的 Text-to-Motion 模型通常是单向任务专用的。如何构建一个通用的、多任务的动作模型，实现动作生成、动作描述（Captioning）、动作补全等任务的统一？

核心方法： MotionGPT 提出了**「动作即外语」（Motion as a Foreign Language）的理念。它将离散化的动作 Token 与文本 Token 视为同一词表中的元素，利用预训练的大语言模型（如 T5 或 LLaMA）作为骨干网络。通过构建包含多种任务的指令微调（Instruction Tuning）**数据集，MotionGPT 能够根据不同的自然语言指令执行不同的任务（例如：“生成一个跑步动作” vs “描述这段动作”）。

关键实验结论： MotionGPT 展示了卓越的零样本泛化能力（Zero-shot）。它不仅在标准的生成任务上表现优异，在未见过的动作问答和描述生成任务上也展现出了类似 LLM 的涌现能力，确立了统一多模态动作理解与生成的新范式。

MotionGPT-2
来源：arXiv 2024 / 2025    

研究问题： 前代模型大多忽略了手部手指、面部表情等细粒度动作，导致生成的“全身动作”缺乏表现力。且单一的 Codebook 难以同时编码低频的躯干运动和高频的手部运动。

核心方法： MotionGPT-2 引入了部件感知（Part-Aware）的 VQ-VAE。该框架为躯干和手部构建了独立的 Codebook，并采用分层量化策略，确保了对不同身体部位精细动作的高保真重构。在生成阶段，它采用了**“预训练-微调”**范式，首先在大规模无标注动作数据上进行预训练，然后在构建的高质量多模态指令数据集上进行微调。此外，它支持多种控制信号（如文本、第一帧姿态、轨迹）的混合输入。

关键实验结论： 在 Motion-X 全身数据集上，MotionGPT-2 实现了对手指弯曲等微小动作的精准控制，FID 分数进一步降低至 0.191。其训练效率比从头训练的方法提升了 10 倍，证明了部件解耦与大规模预训练在全身动作生成中的关键作用。

MoSa: Motion Generation with Scalable Autoregressive Modeling
来源：arXiv 2025    

研究问题： 随着模型规模的增大，自回归模型的推理延迟成为瓶颈。如何在保持高性能的同时，实现模型规模的可扩展性与推理的高效性？

核心方法： MoSa 受到视觉自回归模型（VAR）的启发，提出了一种**多尺度自回归建模（Scalable Autoregressive Modeling）**方法。它不再是逐个 Token 预测，而是基于“下一个尺度预测”（Next-Scale Prediction）的范式，从粗粒度的动作概貌逐步细化到精细的动作 Token。这种层级化的生成方式不仅符合人类先规划后执行的直觉，还大幅减少了自回归的步数。

关键实验结论： MoSa 在 Motion-X 数据集上取得了 0.06 的极低 FID，同时推理速度相比 MoMask 等 SOTA 方法提升了 27%。它证明了多尺度建模是打破自回归生成效率瓶颈的有效手段。

2.3 面向交互与物理约束的场景感知生成 (Interaction & Physics-Aware Generation)
进入 2024 年与 2025 年，学术界的研究焦点从单纯的动作生成转向了更具挑战性的场景：涉及复杂的人-物交互（HOI）、环境几何适应以及物理规律的一致性。

Text2HOI
来源：CVPR 2024    

研究问题： 生成人与物体交互（HOI）时，不仅需要生成人体姿态，还需要预测物体的 6DoF 轨迹，且两者必须在接触点上保持严格的时空对齐，否则会出现“隔空取物”或“穿模”现象。

核心方法： Text2HOI 提出了一种分解生成与接触引导的策略。该方法将复杂的 HOI 生成任务分解为两个子任务：首先基于文本预测接触图（Contact Map），即人体手部与物体表面的接触概率分布；然后以接触图为强约束条件，联合生成人体全身动作与物体轨迹。通过显式地建模接触关系，模型能够“理解”抓取、搬运等动作的物理含义。

关键实验结论： Text2HOI 有效解决了以往方法中物体运动与手部运动不同步的问题。在涉及复杂操作（如倒水、挥舞球拍）的场景中，它生成的交互动作在物理合理性评分上大幅领先，证明了接触关系是连接人与物体的核心纽带。

SemGeoMo
来源：CVPR 2025    

研究问题： 传统的文本生成动作往往是在“真空”中进行的，忽略了环境几何（如椅子高度、台阶坡度）对动作的决定性影响。

核心方法： SemGeoMo 引入了**多层级语义与几何引导（Multi-level Semantic and Geometric Guidance）框架。该方法首先利用大语言模型（LLM）作为语义标注器，将文本指令分解为具体的交互阶段；然后结合场景的点云几何特征，通过一个可供性预测模块（Affordance Prediction Module）**来预测人体与环境的潜在接触点和支撑面。生成模型在这些语义和几何信息的双重引导下，生成适应特定环境的动作。

关键实验结论： 在动态场景交互测试中，SemGeoMo 生成的动作不仅符合文本描述，还能自适应地调整姿态以匹配不同形状的家具或地形，显著提升了动作的几何正确性和环境适应性。

InterDreamer
来源：NeurIPS 2024    

研究问题： 现有的 HOI 数据集规模有限，难以覆盖现实世界中无限可能的交互方式。如何实现**零样本（Zero-shot）**的交互生成？

核心方法： InterDreamer 提出了一个解耦语义与动力学的框架。它利用预训练的 T2M 模型处理高层的语义规划（即“要做什么动作”），同时引入一个**世界模型（World Model）**来处理底层的物理交互（即“物体如何响应”）。世界模型学习了基本的物理定律（如碰撞、摩擦），能够根据人体动作预测物体的状态变化。通过在推理时优化动作以符合世界模型的预测，实现了无需成对 HOI 数据训练的零样本生成。

关键实验结论： InterDreamer 展示了惊人的泛化能力，能够生成训练集中从未出现过的交互组合（如“用脚踢飞笔记本电脑”），证明了将物理世界模型引入生成框架是解决数据稀缺问题的有效途径。

Shape My Moves
来源：CVPR 2025    

研究问题： 现有方法通常假设一个标准体型（Mean Shape），忽略了体型差异（如肥胖、瘦削、高矮）对运动动力学的本质影响。直接将标准动作重定向到不同体型会导致穿模或滑步。

核心方法： 该论文提出了体型感知（Shape-Aware）的 FSQ-VAE。它将 SMPL 的体型参数（Shape Parameters）显式编码进生成的 Token 中。其核心模块 ShapeMove 能够根据文本描述同时预测体型和动作序列。由于模型在训练时学习了体型与动作的联合分布，因此生成的动作能够自然地反映体型带来的动力学差异（例如，肥胖者走路时的步幅和重心变化）。

关键实验结论： 实验表明，引入体型感知后，动作的物理真实感显著提升。在将动作应用到不同体型的 Avatar 时，该方法生成的动作在穿模率和接触稳定性上均优于传统重定向方法。

WISA: World Simulator Assistant
来源：NeurIPS 2025    

研究问题： 视频或动作生成模型缺乏对物理定律（重力、动量守恒）的显式遵守，常生成反直觉的“幻觉”动作。

核心方法： WISA 提出了物理专家混合注意力机制（MoPA）。它将物理知识分解为动力学、热力学、光学等层级，并通过专门的 Attention Heads 将这些物理约束注入到生成模型中。配合构建的 WISA-80K 物理标注数据集，模型被训练去“理解”物理规律而非仅仅模仿像素。

关键实验结论： WISA 在 VideoPhy 基准上展现了极高的物理一致性，生成的动作和视频大幅减少了违背物理常识的伪影，标志着动作生成向物理仿真迈出了关键一步。

3. 实验与评价总结
本节基于 HumanML3D 、KIT-ML  及 Motion-X  等主流数据集，对上述方法的性能进行横向对比与总结。   

3.1 核心评价指标
FID (Fréchet Inception Distance)：衡量生成动作分布与真实动作分布的距离，数值越低代表动作越逼真。

R-Precision：衡量生成动作与输入文本的语义匹配度（通常取 Top-1, Top-2, Top-3 准确率），数值越高代表语义对齐越好。

Diversity：衡量生成动作的多样性，数值越高代表模型并未坍塌到单一模式。

Multimodality：衡量同一文本描述下生成动作的差异性，反映模型处理一对多映射的能力。

3.2 定量性能对比
下表总结了各类别代表性模型在 HumanML3D 数据集上的性能概览（数据综合自 ）：   

方法类别	代表模型	FID (↓)	R-Precision (Top-3) (↑)	Diversity (→)	推理速度	核心优势
连续扩散	
MDM 

~0.611	~0.780	~9.55	慢	多样性高，易于添加几何损失
潜在扩散	
MLD 

~0.473	~0.772	~9.70	极快	平衡了质量与效率，工业部署首选
离散自回归	
T2M-GPT 

~0.116	~0.775	~9.20	快	FID 最佳，动作平滑度高
检索增强	
ReMoDiffuse 

~0.600	>0.800	~9.64	中等	语义对齐最强，长难句理解能力极佳
全身/交互	
MotionGPT-2 

~0.191	~0.818	~9.86	中等	全身精细控制，多模态指令理解
  
3.3 共性实验结论与洞察
离散表征的保真度优势：T2M-GPT 和 MotionGPT 系列在 FID 指标上持续领先（0.1~0.2 区间），显著优于扩散模型（0.4~0.6）。这表明 VQ-VAE 的量化过程实质上起到了低通滤波的作用，滤除了动作捕捉数据中的高频抖动噪声，使得生成的动作在视觉上更加平滑、自然。

扩散模型的多样性优势：尽管 FID 略逊，但在 Diversity 和 Multimodality 指标上，MDM 和 ReMoDiffuse 往往表现更好。这说明概率扩散过程更能捕捉文本描述中的模糊性（Ambiguity），能够为同一句“跳舞”生成更多样化的舞姿，而自回归模型倾向于生成概率密度最高的“平均”动作。

潜在空间的效率红利：MLD 的成功证明了动作数据的流形分布位于一个极低维的空间。相比于在原始骨骼空间（Raw Space）进行生成，在 Latent Space 进行生成不仅速度提升了 50 倍以上，而且并没有显著损失动作的语义精度。这已成为 2024 年后高效模型的标配设计。

物理与语义的权衡（Trade-off）：引入显式的物理或几何约束（如 SemGeoMo, WISA, Shape My Moves）通常会导致 FID 分数轻微上升（变差）。这是因为现有的 FID 计算是基于存在物理瑕疵的 MoCap 数据集的，过于完美的物理动作反而可能偏离数据集分布。但在人工评测（User Study）中，物理感知模型的得分显著更高，这提示我们需要超越 FID，发展基于物理一致性的新评价指标。

4. 趋势与挑战
基于 2024–2025 年的最新文献，该领域正处于从“数据驱动”向“物理与知识驱动”转型的关键时期。

4.1 2025 年前后的研究趋势预测
迈向「世界模拟器」的物理感知生成 (From Motion to World Simulators)： 2025 年的研究（如 WISA ）表明，未来的模型将不再孤立地生成“动作”，而是生成符合物理定律的“行为”。结合物理引擎（Physics Engine）与数据驱动模型的混合架构将成为主流。模型不仅要学会“走”，还要学会重力、惯性以及与流体或刚体的相互作用。这标志着 Text-to-Motion 正演变为 Text-to-Simulation。   

统一的多模态具身大模型 (Unified Embodied Foundation Models)： MotionGPT-2  展示了将动作作为一种模态并入 LLM 的潜力。未来的趋势是构建单一的 Foundation Model，它能同时理解视频、文本、3D 场景和动作指令，直接输出机器人可执行的控制信号。动作生成将成为具身智能（Embodied AI）大脑的一部分，而非独立的图形学任务。这种模型将具备“通感”能力，即看到椅子就能联想到坐下的动作。   

4D 动态场景中的情境化生成 (Contextualized Generation in 4D Scenes)： CVPR 2025 的 SemGeoMo  和 Shape My Moves  揭示了“脱离环境谈动作”的局限性。研究将从生成“真空中的人”彻底转向生成“场景中的人”。这意味着生成模型必须实时感知动态变化的 3D 环境（如避开移动障碍物、适应地形变化），实现 4D 时空的一致性。这也将推动生成模型与 SLAM（同步定位与地图构建）技术的深度融合。   

4.2 核心挑战
数据稀缺与质量瓶颈：尽管有 Motion-X 等数据集，但高质量、含物理标注（如力、摩擦系数）、含精细交互（如手指接触）的数据依然极度匮乏。现有的 MoCap 数据往往缺乏场景信息，限制了场景感知模型的训练。

长序列生成的漂移问题：无论是自回归还是扩散模型，在生成超过 10 秒的长序列复杂交互时，仍容易出现动作崩塌或语义漂移。如何维持分钟级的长程连贯性仍是未解难题。

实时性与可控性的矛盾：高保真的扩散模型推理慢，难以满足游戏或元宇宙的实时交互需求；而快速模型（如 LCM, Turbo）往往牺牲了物理约束的严谨性。如何在毫秒级延迟下实现物理正确的生成是工业界关注的重点。

5. 结论
2022 至 2025 年，文本驱动的人体动作合成经历了从“能动”到“动得真实”，再到“动得合理”的跨越式发展。扩散模型（如 MDM, MLD）的确立解决了动作生成的多样性难题，而离散自回归模型（如 T2M-GPT, MotionGPT）则在动作保真度和语义统一性上建立了新标准。

最新的前沿工作（SemGeoMo, Text2HOI, WISA）表明，单纯的运动学拟合已触及天花板。未来的核心竞争力在于物理感知（Physics-Awareness）、环境交互（Interaction）和全身精细控制（Whole-body Control）。随着具身智能的兴起，动作合成技术正在超越图形学的范畴，成为构建数字世界与物理世界互动的核心引擎。我们有理由相信，下一代模型将不仅是“动画师”，更是理解物理法则与人类意图的“数字代理人”。

参考文献
 Tevet, G., Raab, S., Gordon, B., et al. "Human Motion Diffusion Model." International Conference on Learning Representations (ICLR), 2023. (arXiv preprint arXiv:2209.14916, 2022).   

 Chen, X., Jiang, B., Liu, W., et al. "Executing your Commands via Motion Diffusion in Latent Space." IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2023.   

 Zhang, J., Zhang, Y., Cun, X., et al. "Generating Human Motion from Textual Descriptions with Discrete Representations." IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2023.   

 Zhang, M., Guo, X., Pan, L., et al. "ReMoDiffuse: Retrieval-Augmented Motion Diffusion Model." IEEE/CVF International Conference on Computer Vision (ICCV), 2023.   

 Jiang, B., Chen, X., Liu, W., et al. "MotionGPT: Human Motion as a Foreign Language." Advances in Neural Information Processing Systems (NeurIPS), 2023.   

 Cha, J., Kim, J., Yoon, J. S., et al. "Text2HOI: Text-guided 3D Motion Generation for Hand-Object Interaction." IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2024.   

 Song, W., Zhang, X., Li, S., et al. "HOIAnimator: Generating Text-prompt Human-object Animations using Novel Perceptive Diffusion Models." IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2024.   

 Ghosh, A., Dabral, R., Golyanik, V., et al. "ReMoS: 3D Motion-Conditioned Reaction Synthesis for Two-Person Interactions." European Conference on Computer Vision (ECCV), 2024.   

 Wang, Z., Yu, P., Zhao, Y., et al. "MotionGPT-2: A General-Purpose Motion-Language Model for Motion Generation and Understanding." arXiv preprint arXiv:2410.21747, 2024.   

 Xu, S., Wang, Z., Wang, Y.-X., et al. "InterDreamer: Zero-Shot Text to 3D Dynamic Human-Object Interaction." Advances in Neural Information Processing Systems (NeurIPS), 2024.   

 Cong, P., Wang, Z., Ma, Y., et al. "SemGeoMo: Dynamic Contextual Human Motion Generation with Semantic and Geometric Guidance." IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2025.   

 Liao, T.-H., Zhou, Y., Shen, Y., et al. "Shape My Moves: Text-Driven Shape-Aware Synthesis of Human Motions." IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2025.   

 Wang, J., Ma, A., Cao, K., et al. "WISA: World simulator assistant for physics-aware text-to-video generation." Advances in Neural Information Processing Systems (NeurIPS), 2025.   

 Liu, M., Yan, S., Wang, Y., et al. "MoSa: Motion Generation with Scalable Autoregressive Modeling." arXiv preprint arXiv:2511.01200, 2025.   


openreview.net
Human Motion Diffusion Model - OpenReview
在新窗口中打开

arxiv.org
[2209.14916] Human Motion Diffusion Model - arXiv
在新窗口中打开

arxiv.org
FG-MDM: Towards Zero-Shot Human Motion Generation via Fine-Grained Descriptions
在新窗口中打开

ieeexplore.ieee.org
Motion Latent Diffusion for Stochastic Trajectory Prediction - IEEE Xplore
在新窗口中打开

arxiv.org
[2212.04048] Executing your Commands via Motion Diffusion in Latent Space - arXiv
在新窗口中打开

openaccess.thecvf.com
Executing Your Commands via Motion Diffusion in Latent Space - CVF Open Access
在新窗口中打开

github.com
ReMoDiffuse: Retrieval-Augmented Motion Diffusion Model - GitHub
在新窗口中打开

mingyuan-zhang.github.io
ReMoDiffuse: Retrieval-Augmented Motion Diffusion Model - Mingyuan Zhang
在新窗口中打开

liner.com
[Quick Review] ReMoDiffuse: Retrieval-Augmented Motion Diffusion Model - Liner
在新窗口中打开

openaccess.thecvf.com
ReMoDiffuse: Retrieval-Augmented Motion Diffusion Model - CVF Open Access
在新窗口中打开

cvpr.thecvf.com
CVPR 2024 Accepted Papers
在新窗口中打开

researchgate.net
HOIAnimator: Generating Text-Prompt Human-Object Animations Using Novel Perceptive Diffusion Models | Request PDF - ResearchGate
在新窗口中打开

openaccess.thecvf.com
HOIAnimator: Generating Text-prompt Human-object Animations using Novel Perceptive Diffusion Models - CVF Open Access
在新窗口中打开

proceedings.neurips.cc
InterDreamer: Zero-Shot Text to 3D Dynamic Human-Object Interaction - NIPS papers
在新窗口中打开

github.com
soraproducer/Awesome-Human-Interaction-Motion-Generation - GitHub
在新窗口中打开

arxiv.org
ReactionMamba: Generating Short & Long Human Reaction Sequences - arXiv
在新窗口中打开

ecva.net
ReMoS: 3D Motion-Conditioned Reaction Synthesis for Two-Person Interactions - European Computer Vision Association
在新窗口中打开

github.com
Code for ReMoS: 3D-Motion Conditioned Reaction Synthesis for Two-person Interactions (ECCV 2024) - GitHub
在新窗口中打开

github.com
Zilize/awesome-text-to-motion: Text-driven human motion generation surveys, datasets and models. - GitHub
在新窗口中打开

liner.com
Generating Human Motion from Textual Descriptions with Discrete Representations - Liner
在新窗口中打开

voxel51.com
Generate Movement from Text Descriptions with T2M-GPT - Voxel51
在新窗口中打开

researchgate.net
T2M-GPT: Generating Human Motion from Textual Descriptions with Discrete Representations - ResearchGate
在新窗口中打开

ojs.aaai.org
Light-T2M: A Lightweight and Fast Model for Text-to-motion Generation - AAAI Publications
在新窗口中打开

github.com
[NeurIPS 2023] MotionGPT: Human Motion as a Foreign Language, a unified motion-language generation model using LLMs - GitHub
在新窗口中打开

papers.nips.cc
Appendix of MotionGPT - NIPS papers
在新窗口中打开

arxiv.org
MotionGPT-2: A General-Purpose Motion-Language Model for Motion Generation and Understanding - arXiv
在新窗口中打开

researchgate.net
(PDF) MotionGPT-2: A General-Purpose Motion-Language Model for Motion Generation and Understanding - ResearchGate
在新窗口中打开

arxiv.org
Enhancing Motion Generation with Decomposed Chain-of-Thought and RL Binding - arXiv
在新窗口中打开

researchgate.net
(PDF) MoSa: Motion Generation with Scalable Autoregressive Modeling - ResearchGate
在新窗口中打开

chatpaper.com
MoSa: Motion Generation with Scalable Autoregressive Modeling - ChatPaper
在新窗口中打开

researchgate.net
Visual Autoregressive Modeling: Scalable Image Generation via Next-Scale Prediction | Request PDF - ResearchGate
在新窗口中打开

researchgate.net
Text2HOI: Text-Guided 3D Motion Generation for Hand-Object Interaction | Request PDF
在新窗口中打开

arxiv.org
Text2HOI: Text-guided 3D Motion Generation for Hand-Object Interaction - arXiv
在新窗口中打开

openaccess.thecvf.com
Text2HOI: Text-guided 3D Motion Generation for Hand-Object Interaction - CVPR 2024 Open Access Repository - The Computer Vision Foundation
在新窗口中打开

cvpr.thecvf.com
CVPR Poster SemGeoMo: Dynamic Contextual Human Motion ...
在新窗口中打开

arxiv.org
SemGeoMo: Dynamic Contextual Human Motion Generation with Semantic and Geometric Guidance - arXiv
在新窗口中打开

liner.com
[Quick Review] SemGeoMo: Dynamic Contextual Human Motion Generation with Semantic and Geometric Guidance - Liner
在新窗口中打开

openaccess.thecvf.com
SemGeoMo: Dynamic Contextual Human Motion Generation with Semantic and Geometric Guidance
在新窗口中打开

sirui-xu.github.io
InterDreamer: Zero-Shot Text to 3D Dynamic Human-Object Interaction - Sirui Xu
在新窗口中打开

openaccess.thecvf.com
Shape My Moves: Text-Driven Shape-Aware Synthesis of Human Motions - CVF Open Access
在新窗口中打开

liner.com
ShapeWords: Guiding Text-to-Image Synthesis with 3D Shape-Aware Prompts - Liner
在新窗口中打开

openreview.net
WISA: World simulator assistant for physics-aware text-to-video ...
在新窗口中打开

arxiv.org
NewtonGen: Physics-Consistent and Controllable Text-to-Video Generation via Neural Newtonian Dynamics - arXiv
在新窗口中打开

arxiv.org
MoReGen: Multi-Agent Motion-Reasoning Engine for Code-based Text-to-Video Synthesis
在新窗口中打开

openreview.net
LEARNING TEXT-DRIVEN 3D HUMAN MOTION GEN - OpenReview
在新窗口中打开

github.com
HumanML3D: A large and diverse 3d human motion-language dataset. - GitHub
在新窗口中打开

arxiv.org
MoSa: Motion Generation with Scalable Autoregressive Modeling - arXiv
