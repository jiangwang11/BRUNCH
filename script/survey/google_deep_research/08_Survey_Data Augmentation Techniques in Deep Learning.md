深度学习中的数据增强技术演进：从生成式合成到测试时适应（2022–2025 年综述）
1. 引言
在深度学习的蓬勃发展历程中，数据始终是驱动模型性能跃迁的核心燃料。然而，随着模型参数规模的指数级增长，高质量标注数据的获取成本日益高昂，长尾分布中的样本稀缺性以及非平稳环境下的模型泛化能力不足，已成为制约人工智能系统从实验室走向开放世界应用的关键瓶颈。数据增强（Data Augmentation, DA）作为一种通过对现有数据进行变换或合成以扩充训练集规模、丰富数据多样性的技术，早已成为深度学习训练的标准范式。

回顾 2022 年至 2025 年的研究进展，数据增强技术经历了一场深刻的范式转移。传统的“基于规则的启发式变换”（如图像的旋转、裁剪，文本的同义词替换）虽然在计算上高效，但在语义丰富度和分布覆盖上已显捉襟见肘。伴随着生成式人工智能（Generative AI）的爆发，特别是扩散模型（Diffusion Models）在视觉生成领域的统治地位确立，以及大语言模型（Large Language Models, LLMs）在自然语言处理（NLP）中展现出的涌现能力，数据增强进入了“生成式增强”（Generative Data Augmentation, GDA）的新时代 。此时的增强不再仅仅是针对过拟合的正则化手段，而是演变为一种能够主动重塑数据分布、注入外部先验知识，甚至通过合成数据打破物理世界数据获取边界（Data Wall）的核心策略 。   

与此同时，增强技术的应用场景也从训练阶段（Training-Time）延伸至了推理阶段（Inference-Time）。测试时适应（Test-Time Adaptation, TTA）作为数据增强在推理端的延伸，通过在测试数据上实时更新模型或调整输入，成为解决分布偏移（Distribution Shift）问题的关键前沿方向。此外，随着社会对 AI 可信度的关注，数据增强被赋予了新的使命——在保护隐私和消除偏见中发挥作用，通过合成数据替代敏感数据，或利用增强样本平衡受保护属性的分布。

本综述旨在对 2022–2025 年间深度学习领域的数据增强技术进行详尽的梳理与分析。报告将深入探讨生成式增强的机制创新、测试时适应的理论突破以及面向特定领域（如时间序列、隐私保护）的高效增强策略。通过对代表性工作的深度剖析，本报告旨在揭示数据增强技术如何从一种辅助性的工程技巧，进化为定义下一代 AI 系统数据基础设施的关键技术。

2. 基于扩散模型的生成式视觉增强
在计算机视觉领域，2022 年之前的数据增强主要依赖于几何变换（Geometric Transformations）和光度变换（Photometric Transformations）。虽然 Mixup 和 CutMix 等混合样本方法通过在像素空间进行线性插值提升了模型的鲁棒性，但它们无法引入样本中不存在的语义信息。2023 年至 2025 年间，扩散模型因其卓越的分布建模能力和生成质量，迅速取代 GAN 成为生成式数据增强的主流工具。研究的重心集中在如何解决生成效率低、分布偏移以及对细粒度语义的控制上。

2.1 解决分布偏移与采样效率的协同优化
生成式数据增强（GDA）面临的核心悖论在于：为了获得高质量的增强样本，通常需要使用庞大的预训练扩散模型进行多步采样，这导致训练成本呈指数级上升；同时，合成数据与真实数据之间天然存在的分布偏差（Synthetic-to-Real Bias）可能误导下游分类器，导致性能不升反降。

DAR-GDA: Distillation, Adversarial, and Reweighting for Generative Data Augmentation 针对上述挑战，Ding 等人（2025）在 NeurIPS 上提出的 DAR-GDA 框架代表了该方向的最新进展 。该研究的核心动机是打破生成质量、采样速度与分布对齐之间的“不可能三角”。传统方法要么牺牲质量换速度，要么忽略分布偏差。DAR-GDA 创新性地设计了一个三阶段的协同管线，将模型蒸馏（Distillation）、对抗对齐（Adversarial Alignment）和重要性重加权（Importance Reweighting）融为一体。   

在方法论层面，第一阶段利用分数蒸馏（Score Distillation）技术，将庞大的教师扩散模型压缩为一个单步（One-step）的学生生成器。这一过程不仅将生成单张图像的时间成本降低了两个数量级（>100x），还通过保留教师模型的分数场信息维持了较高的 FID 分数。然而，仅靠蒸馏无法消除合成域与真实域的差异。因此，第二阶段引入了对抗训练机制，学生生成器在模仿教师分数的同时，还需要欺骗一个判别器，该判别器试图区分合成样本与真实样本。这一对抗过程本质上是最小化学生分布与真实数据分布之间的 Jensen-Shannon 散度，从而在特征空间强制对齐。

最具洞察力的是第三阶段的设计。研究者并未丢弃在对抗阶段训练的判别器，而是将其复用为密度比估计器（Density-ratio Estimator）。判别器的输出经过校准后，被转化为样本的重要性权重（Importance Weights）。在训练下游分类器时，这些权重用于调整损失函数，使得对合成数据的训练等效于对真实数据分布的无偏估计。实验结果显示，DAR-GDA 在 CIFAR-10 和 ImageNet-1K 上的性能随 D-A-R 三个阶段逐级提升。在仅使用域内数据的情况下，其增强效果不仅超越了传统的非基础模型 GDA 方法，甚至匹配了使用网络级大规模预训练模型（如 Stable Diffusion）的效果，证明了通过算法设计挖掘域内数据潜力的可行性。

2.2 时间步感知的增强策略
在使用扩散模型生成数据时，另一个被长期忽视的变量是“时间步”（Timestep）。扩散过程是一个逐步去噪的过程，不同时间步对应着从粗糙轮廓到精细纹理的不同生成阶段。

TADA: Timestep-Aware Data Augmentation for Diffusion Models Park 等人（2023）在 NeurIPS Workshop 上发表的 TADA 工作，首次系统地揭示了数据增强在扩散模型训练中的时间异质性 。研究团队提出的核心问题是：在训练扩散模型本身时，如果对所有时间步应用相同强度的传统增强（如旋转、色彩抖动），是否会导致生成的样本分布发生非预期的偏移？   

通过深入的实证分析，研究发现分布偏移并非均匀地源自所有时间步，而是集中在特定的“敏感区间”。例如，几何变换主要影响低频信息的构建阶段（高噪声时间步），而纹理变换则更多干扰高频细节的生成（低噪声时间步）。基于这一发现，TADA 提出了一种时间步感知的自适应增强策略。该方法不再使用全局统一的增强概率，而是引入了一个关于时间步 t 的函数（如二次函数）来动态调整增强强度。在模型对特定增强不敏感的时间步，施加较强的变换以增加多样性；而在敏感时间步，则降低增强强度以保证生成的保真度。

实验结果表明，这种简单而精细的控制策略在数据受限（Data-Limited）的场景下尤为有效。TADA 显著降低了生成样本的 FID 分数，提升了模型的泛化能力，且该方法具有极高的通用性，可无缝集成到 DDPM、Latent Diffusion 等多种架构中。这一工作从机理上阐明了扩散模型训练中数据增强的作用边界，为后续的精细化控制提供了理论支撑。

2.3 面向少样本与新概念的语义增强
当面对训练集中仅有少量样本（Few-Shot）甚至完全未见过的概念（Novel Concepts）时，传统的增强方法往往束手无策。如何利用在大规模互联网数据上预训练的文本到图像模型（如 Stable Diffusion）将通用的先验知识迁移到特定的下游任务中，是 2024 年的一个研究热点。

DA-Fusion: Effective Data Augmentation with Diffusion Models Trabucco 等人（2024）在 ICLR 上提出的 DA-Fusion 旨在解决这一难题 。该研究挑战了传统方法（如 Real Guidance）必须依赖类别名称作为提示词的限制，指出在细粒度分类或专业领域（如特定的杂草种类 Leafy Spurge），通用的类别名称往往无法被预训练模型准确理解。   

DA-Fusion 的核心创新在于结合了文本反转（Textual Inversion）与 SDEdit（随机微分方程编辑）。首先，利用仅有的少量真实样本（如 3-5 张），通过文本反转技术学习代表该特定概念的词嵌入（Token Embedding）。这一步相当于在预训练模型的语义空间中找到了该概念的精确坐标，而非依赖模糊的自然语言描述。随后，将学习到的 Token 作为提示词，结合输入图像的噪声扰动与去噪过程（SDEdit），生成具有不同背景、光照和视角的变体。这种方法既保留了原始样本的核心语义特征，又充分利用了扩散模型的生成多样性。

实验数据显示，DA-Fusion 在包含常见概念、细粒度概念以及模型完全未见过的全新概念的数据集上，均取得了显著的性能提升。特别是在全新概念的分类任务中，其带来的准确率提升高达 20.8%，远超传统增强方法。这一结果有力地证明了，通过适当的引导机制，基础模型的通用生成能力可以被有效地转化为特定任务的数据优势。

2.4 保持语义协调的目标检测增强
与图像分类不同，目标检测任务要求增强后的图像在几何位置和语义背景上保持高度的一致性。简单的剪切粘贴（Copy-Paste）往往会导致物体与背景的光照不一致或语义违和（例如，将船粘贴到公路上）。

Diverse Generation while Maintaining Semantic Coordination Fang 等人（2024）在 ICPR 上提出的工作针对目标检测中的语义协调性问题进行了深入探索 。研究者指出，现有的基于扩散的检测增强方法往往忽视了物体与周围环境的交互，导致生成的训练样本虽多但质量参差不齐。   

该方法设计了一个包含“类别亲和矩阵”（Category Affinity Matrix）和“周边区域对齐”（Surrounding Region Alignment）的生成框架。类别亲和矩阵用于指导生成器选择在语义上相容的物体类别进行组合，避免了荒谬的物体共现。更关键的是周边区域对齐策略，它在扩散生成过程中利用掩码机制，强制生成的物体在边缘像素上与背景图像平滑过渡，并在光照和纹理上与环境保持一致。最后，引入实例级的过滤模块，剔除生成质量低下的样本。

实验结果表明，该方法在多种检测器架构上平均提升了 1.4% 至 3.4% 的 AP（平均精度）。特别是在细粒度检测数据集上，由于其生成的样本在语义上高度可信，模型能够学习到更鲁棒的上下文特征，性能提升更为显著。这标志着生成式增强在结构化输出任务（Structured Prediction）上的应用达到了新的成熟度。

表 1：代表性生成式视觉增强方法对比

方法名称	核心机制	生成模型类型	解决的关键问题	适用任务
DAR-GDA 

蒸馏+对抗+重加权	扩散模型 (Student)	生成效率低、分布偏差	图像分类
TADA 

时间步感知调节	扩散模型	训练过程中的分布偏移	图像生成/分类
DA-Fusion 

文本反转+SDEdit	预训练 T2I 模型	少样本、新概念、细粒度	少样本分类
Fang et al. 

区域对齐+亲和矩阵	扩散模型	物体与背景的语义不协调	目标检测
  
3. 大语言模型时代的合成数据与自我进化
在自然语言处理领域，2024–2025 年的趋势表明，数据增强已超越了传统的同义词替换或回译，转向利用 LLM 强大的推理和生成能力进行“自我对齐”（Self-Alignment）和“思维链增强”（CoT Augmentation）。合成数据被视为解决高质量文本数据枯竭（Data Exhaustion）和提升模型复杂推理能力的必由之路。

3.1 合成数据的扩展定律与理论边界
随着网络爬取数据的耗尽，学术界开始严肃探讨合成数据是否可以作为一种可持续的“燃料”。核心争议在于：在合成数据上训练模型是否会遵循与真实数据相同的扩展定律（Scaling Laws）？

SynthLLM: Scaling Laws of Synthetic Data for Language Models Qin 等人（2025）在 COLM 上发表的 SynthLLM 是该领域的里程碑式工作 。该研究并未止步于工程实践，而是试图建立合成数据的理论框架。研究者开发了 SynthLLM 框架，利用图算法从预训练语料库中提取高级概念及其拓扑关系，重组生成多样化、高质量的合成数据（特别是数学领域）。   

通过大规模的系统性实验，该研究得出了几个颠覆性的结论。首先，合成数据严格遵循“修正后的扩展定律”（Rectified Scaling Law），即随着合成数据量的增加，模型损失呈现可预测的幂律下降。其次，存在显著的“模型尺寸-数据效率”效应：越大的模型能越快地利用合成数据达到性能峰值。例如，实验显示 8B 参数的模型仅需 1T 合成 Token 即可达到最佳性能，而较小的 3B 模型则需要 4T Token。这一发现暗示大模型具备更强的从合成数据中提取抽象特征的能力。最后，研究也指出了饱和效应，即在特定任务（如数学推理）上，单纯增加合成数据量在达到一定阈值（如 300B Token）后，边际收益会急剧递减，提示未来的增强方向应从“量”转向“质”与“多样性”的控制。

3.2 自我增强与指令回译机制
高质量的指令微调（Instruction Tuning）数据是训练对齐模型的关键，但人工标注成本极高。如何挖掘现有无标注语料的潜力成为研究热点。

Instruction Backtranslation (Humpback) Li 等人（2024）在 ICLR 上提出的指令回译（Instruction Backtranslation）技术，巧妙地将机器翻译中的回译思想迁移到了指令生成中 。该方法的核心逻辑是：互联网上存在海量的高质量文档（可以看作是潜在的“回复”），缺少的只是触发这些回复的“指令”。   

该方法包含两个循环步骤：自我增强（Self-Augmentation）与自我筛选（Self-Curation）。首先，使用一个少量的种子数据微调出的模型，对无标注的网络文档反向预测其对应的指令（即预测 P(Instruction∣Web Document)）。随后，利用模型自身对生成的（指令，回复）对进行质量打分，筛选出高质量样本用于下一轮微调。实验结果令人瞩目：基于 LLaMA 微调得到的 Humpback 模型，在 Alpaca Leaderboard 上超越了所有非蒸馏模型（即不依赖 GPT-4 生成数据的模型）。更重要的是，该方法生成的指令数据在长尾分布上比人工标注数据更具多样性，有效提升了模型在罕见任务上的指令遵循能力。

3.3 隐式推理作为数据增强
传统的数据增强侧重于扩充输入样本，而最新的研究开始探索如何通过“增强推理过程”来提升模型性能。

Quiet-STaR: Language Models Can Teach Themselves to Think Before Speaking Zelikman 等人（2024）提出的 Quiet-STaR 展示了一种全新的增强维度——内部思维增强 。现有的思维链（CoT）推理通常是显式的，且需要特定的提示词。Quiet-STaR 旨在训练模型在生成每个 Token 之前都进行“隐式思考”。   

该方法在训练过程中，于输入序列的每个 Token 位置并行生成多个内部思考（Rationales），并用 <|startofthought|> 和 <|endofthought|> 标记包裹。随后，训练一个混合头（Mixing Head）将基于思考后的预测结果与基础预测结果融合。通过强化学习（REINFORCE），模型被奖励生成那些有助于预测后续文本的思考。这一过程实质上是将任意文本语料转化为包含推理过程的增强训练数据。实验表明，Quiet-STaR 在没有任何特定任务微调的情况下，显著提升了模型在 GSM8K 和 CommonsenseQA 上的零样本推理性能。特别是对于文本中高困惑度的困难部分，生成的“思考”起到了关键的辅助作用。

3.4 LLM 增强的成本效益分析
尽管 LLM 增强效果显著，但其高昂的推理成本不容忽视。

LLM-based Data Augmentation: Cost-Benefit Analysis 一项发表在 NAACL 2025 的研究对 LLM 增强与传统方法进行了详尽的对比分析 。研究发现，虽然 LLM 生成的数据在语义连贯性和多样性上优于传统方法（如同义词替换），但在数据量较大时，其带来的边际效益会迅速下降。对于资源受限的场景，传统的增强方法在经过精细调优后，往往能以极低的成本达到接近 LLM 增强的效果。该研究建议在低资源（Low-Resource）设定下优先使用 LLM 增强，而在数据充足时应权衡计算成本。   

4. 测试时适应与增强：应对动态环境的鲁棒性
传统的 TTA（Test-Time Augmentation）通常指对测试样本进行多次裁剪、翻转并平均预测结果。2024 年的研究趋势已全面转向更复杂的“测试时适应”（Test-Time Adaptation, TTA），即在测试阶段利用无标签数据实时更新模型参数。这一领域的焦点在于如何解决持续适应中的“灾难性遗忘”和“模型坍塌”问题，并建立无监督的性能评估理论。

4.1 循环环境下的持续适应与防坍塌
在自动驾驶或长期监控等实际应用中，测试环境并非线性变化，而是呈现循环往复的特征（如：白天 → 黑夜 → 白天）。现有的 TTA 方法（如 TENT）在这种“循环 TTA”（Recurring TTA）设定下，极易因误差累积导致模型坍塌（Model Collapse），即模型将所有样本预测为同一类别。

PeTTA: Persistent Test-Time Adaptation Hoang 等人（2024）在 NeurIPS 上提出的 PeTTA 框架，专门解决了这一棘手问题 。PeTTA 的核心思想是引入一种能够感知模型状态并动态调整适应策略的机制。研究者利用特征嵌入空间的统计量（如类原型的均值和协方差）构建了一个“特征空间散度”指标 ψ 
t
​
 ，用于实时衡量当前模型与初始源模型（Source Model）的偏离程度。   

基于这一感知指标，PeTTA 动态调整 Mean Teacher 架构中的两个关键超参数：正则化权重 λ 和动量更新系数 α。当检测到模型有坍塌风险（即 ψ 
t
​
  增大）时，算法会自动增大 λ 并减小 α，优先通过锚点损失（Anchor Loss）将模型拉回源分布的附近，防止过度拟合当前的噪声流。锚点损失通过最小化预测概率分布与源模型的 KL 散度，强制保持输出的一致性。实验表明，在长期的循环测试流中，PeTTA 展现了极高的稳定性，有效遏制了其他 SOTA 方法在多次环境循环后出现的性能崩溃，成功平衡了“适应新域”与“记忆旧域”这一对矛盾目标。

4.2 TTA 的理论基础与无监督性能估计
在 TTA 的实际部署中，由于缺乏测试集的标签，工程师往往难以判断模型适应后的性能究竟如何。

Test-Time Adaptation Induces Stronger Accuracy and Agreement-on-the-Line Kim 等人（2024）在 NeurIPS 上发表的理论工作为 TTA 提供了坚实的数学解释 。先前的研究发现了“Accuracy-on-the-Line”（ACL）现象，即模型在分布内（ID）和分布外（OOD）的精度往往呈线性关系。该研究通过理论推导和大量实验发现，TTA 操作极大增强了这一线性关系，甚至在原本不满足 ACL 的强分布偏移（如高斯噪声）下也能恢复这一特性。   

从机制上讲，TTA 将复杂的高维分布偏移在特征空间中“坍塌”为单一的“缩放”变量（Scaling Variable），从而满足了 ACL 成立所需的严格条件。基于这一发现，作者提出了一种结合 Agreement-on-the-Line (AGL) 的无监督性能估计方法。通过计算 TTA 后模型在不同增强视图下的一致性（Agreement），可以在完全没有标签的情况下，高精度地回归出模型在目标域上的真实准确率。这为 TTA 策略的自动化选择和超参数调优提供了一套无需验证集的解决方案。

4.3 可微的动态测试时增强
除了调整模型参数，另一条路径是调整输入数据。

DynTTA: Dynamic Test-Time Augmentation via Differentiable Functions Enomoto 等人（2024）提出了 DynTTA，一种基于可微函数的数据增强方法 。不同于传统的固定策略 TTA，DynTTA 将增强操作参数化为可微层，允许模型在测试时根据当前的输入图像，通过梯度下降动态优化增强参数（如亮度、对比度的调整值），以生成最利于当前模型识别的“增强视图”。这种方法不仅提高了鲁棒性，还避免了直接修改模型参数可能带来的风险，为高安全性要求的系统提供了一种新的增强思路。   

5. 特定领域的高效与可信增强
除了通用的视觉和语言任务，数据增强在时间序列、隐私保护等特定领域也取得了重要进展。

5.1 时间序列的自动化增强
AutoTSAugment 在时间序列领域，由于数据特征的非直观性，手动设计增强策略极具挑战。AutoTSAugment（2024）提出了一种模块化的自动增强框架 。该框架定义了一个包含多种时间序列变换（如抖动、缩放、时间弯曲）的搜索空间，并利用一种新颖的搜索目标，在无监督的对比学习设置下评估增强质量。实验表明，该框架通过随机搜索或贝叶斯优化找到的策略，在 164 个数据集上均优于手动设计的增强方案，且训练速度提升了 63%。   

5.2 隐私保护与去偏置
数据增强在提升性能的同时，也可能无意中保留甚至放大了训练数据中的敏感信息或偏见。

Privacy-Preserving Debiasing using Data Augmentation and Machine Unlearning Pan 等人（2024）提出了一种结合数据增强与机器遗忘（Machine Unlearning）的创新框架 。该方法旨在解决两个问题：一是通过扩散模型生成的增强数据平衡受保护属性（如种族、性别）的分布，从而减少模型偏见；二是在增强的同时，利用多片遗忘（Multi-shard Unlearning）技术，主动从模型中“擦除”原始敏感数据的特征指纹。实验证明，这种迭代式的“增强-遗忘”机制，既显著降低了模型对成员推理攻击（Membership Inference Attacks）的脆弱性，又提升了公平性指标，为可信 AI 的数据治理提供了新范式。   

6. 趋势、挑战与未来展望
通过对 2022–2025 年文献的综合梳理，我们可以清晰地描绘出数据增强技术的发展脉络与未来图景。

核心趋势：

从操作为中心转向数据为中心 (Operation-centric to Data-centric): 研究焦点已从设计复杂的几何变换组合（如 AutoAugment），彻底转向利用生成模型直接合成符合目标语义的高保真数据。

合成数据的闭环生态 (Synthetic Data Loop): 在 NLP 和视觉领域，模型生成数据 → 训练模型 → 生成更好数据的闭环已成为标准范式。SynthLLM 和 Humpback 等工作证明了这一闭环在一定条件下具备正向放大的扩展能力。

动态适应与上下文感知 (Dynamic & Adaptive): 无论是在视觉的 TADA 中根据时间步调整增强强度，还是在 PeTTA 中根据特征偏移动态调整 TTA 策略，增强技术正变得越来越“智能”，能够根据数据状态和模型反馈实时调整。

多模态融合的深化: 利用 LLM 的文本生成能力辅助视觉增强（如通过生成 Prompt 控制图像合成），或利用视觉模型辅助文本理解，多模态增强正在打破单一模态的信息边界。

面临的挑战：

模型自噬与同质化风险: 随着互联网充斥着 AI 生成的内容，如果模型长期在自身的输出来源上训练，可能会导致分布坍塌或多样性丧失。如何维持合成数据的长尾多样性（如 Humpback 所强调的）是未来的关键难题。

计算成本与绿色 AI: 基于扩散模型和 LLM 的增强极其昂贵。尽管 DAR-GDA 通过蒸馏技术将成本降低了两个数量级，但相比传统的 Crop/Flip，生成式增强的能耗仍高出许多，限制了其在端侧设备的普及。

理论基础的滞后: 尽管实验效果显著，但关于合成数据为何有效、TTA 何时会失效的理论分析（如 ACL/AGL 工作）相对较少，仍需进一步完善。

结论： 2022 至 2025 年是数据增强技术发生质变的三年。它已从一种辅助性的数据预处理手段，升维为深度学习模型训练与推理的核心组件。生成式数据增强打破了有限训练数据的边界，测试时适应技术赋予了模型在开放世界中持续进化的能力。未来，随着理论的完善和计算效率的提升，数据增强将成为构建自进化、可信赖 AI 系统不可或缺的基石。

参考文献
   

Ding, Z., et al. (2025). "DAR-GDA: Distillation, Adversarial, and Reweighting for Generative Data Augmentation." NeurIPS 2025 (Poster).

   

Park, T., et al. (2023). "TADA: Timestep-Aware Data Augmentation for Diffusion Models." NeurIPS 2023 Workshop on Diffusion Models / arXiv.

   

Trabucco, B., et al. (2024). "Effective Data Augmentation With Diffusion Models." ICLR 2024.

   

Fang, Y., et al. (2024). "Diverse Generation while Maintaining Semantic Coordination: A Diffusion-Based Data Augmentation Method for Object Detection." ICPR 2024.

   

Qin, Z., et al. (2025). "Scaling Laws of Synthetic Data for Language Models." COLM 2025.

   

Li, X., et al. (2024). "Self-Alignment with Instruction Backtranslation." ICLR 2024.

   

Zelikman, E., et al. (2024). "Quiet-STaR: Language Models Can Teach Themselves to Think Before Speaking." arXiv preprint arXiv:2403.09629.

   

Hoang, T., et al. (2024). "Persistent Test-time Adaptation in Recurring Testing Environments." NeurIPS 2024.

   

Kim, E., et al. (2024). "Test-Time Adaptation Induces Stronger Accuracy and Agreement-on-the-Line." NeurIPS 2024.

   

Enomoto, S., et al. (2024). "Dynamic Test-Time Augmentation via Differentiable Functions." IEEE Access.

   

Use of Automated Time Series Augmentation (AutoTSAugment) referenced in OpenReview 2024.

   

Pan, Z., et al. (2024). "Privacy-Preserving Debiasing using Data Augmentation and Machine Unlearning." arXiv preprint arXiv:2404.13194.

   

Xu, Y., et al. (2024). "A Comprehensive Survey of Data Augmentation Techniques for Deep Learning: From Operations to Modalities." arXiv preprint arXiv:2405.09591.

   

Cegin, J., et al. (2025). "LLM-based Data Augmentation for Text Classification: A Cost-Benefit Analysis." NAACL 2025.


arxiv.org
A Comprehensive Survey on Data Augmentation - arXiv
在新窗口中打开

arxiv.org
A Survey on State-of-the-art Deep Learning Applications and Challenges - arXiv
在新窗口中打开

arxiv.org
Scaling Laws of Synthetic Data for Language Models - arXiv
在新窗口中打开

neurips.cc
Generative Data Augmentation via Diffusion Distillation, Adversarial Alignment, and Importance Reweighting - NeurIPS 2025
在新窗口中打开

arxiv.org
A Comprehensive Survey for Generative Data Augmentation - arXiv
在新窗口中打开

openreview.net
Generative Data Augmentation via Diffusion ... - OpenReview
在新窗口中打开

openreview.net
TADA: TIMESTEP-AWARE DATA AUGMENTATION FOR DIFFUSION MODELS - OpenReview
在新窗口中打开

neurips.cc
NeurIPS TADA: Timestep-Aware Data Augmentation for Diffusion ...
在新窗口中打开

openreview.net
Effective Data Augmentation With Diffusion Models - OpenReview
在新窗口中打开

arxiv.org
Effective Data Augmentation With Diffusion Models - arXiv
在新窗口中打开

arxiv.org
Diverse Generation while Maintaining Semantic Coordination: A Diffusion-Based Data Augmentation Method for Object Detection - arXiv
在新窗口中打开

microsoft.com
SynthLLM: Breaking the AI "data wall" with scalable synthetic data - Microsoft Research
在新窗口中打开

arxiv.org
self-alignment with instruction backtrans - arXiv
在新窗口中打开

training.continuumlabs.ai
Self-Alignment with Instruction Backtranslation | Continuum Labs
在新窗口中打开

openreview.net
Quiet-STaR: Language Models Can Teach Themselves to Think Before Speaking
在新窗口中打开

arxiv.org
Quiet-STaR: Language Models Can Teach Themselves to Think ...
在新窗口中打开

aclanthology.org
LLMs vs Established Text Augmentation Techniques for Classification: When do the Benefits Outweight the Costs? - ACL Anthology
在新窗口中打开

arxiv.org
LLMs vs Established Text Augmentation Techniques for Classification: When do the Benefits Outweight the Costs? - arXiv
在新窗口中打开

openreview.net
Persistent Test-time Adaptation in Recurring Testing Scenarios - OpenReview
在新窗口中打开

arxiv.org
[2311.18193] Persistent Test-time Adaptation in Recurring Testing Scenarios - arXiv
在新窗口中打开

neurips.cc
Persistent Test-time Adaptation in Recurring Testing Scenarios
在新窗口中打开

proceedings.neurips.cc
Test-Time Adaptation Induces Stronger Accuracy and Agreement-on-the-Line - NIPS papers
在新窗口中打开

arxiv.org
Test-Time Adaptation Induces Stronger Accuracy and Agreement-on-the-Line - arXiv
在新窗口中打开

ieeexplore.ieee.org
Dynamic Test-Time Augmentation via Differentiable Functions | IEEE Journals & Magazine
在新窗口中打开

arxiv.org
[2212.04681] Dynamic Test-Time Augmentation via Differentiable Functions - arXiv
在新窗口中打开

openreview.net
AutoTSAugment: Model-Agnostic Automated Data Augmentation for ...
在新窗口中打开

arxiv.org
Privacy-Preserving Debiasing using Data Augmentation and Machine Unlearning - arXiv
在新窗口中打开

arxiv.org
A Comprehensive Survey on Data Augmentation - arXiv