模型解释性与决策透明度的前沿进展：2022–2025 年学术综述
1. 引言：深度学习解释性的范式重构与历史转折
在人工智能的发展历程中，模型解释性（Explainable AI, XAI）长期处于“为了解释而解释”的辅助地位，主要用于向非专家用户展示模型的关注区域。然而，随着2022年以来大语言模型（LLMs）和多模态基础模型的爆发式增长，参数规模突破万亿级别，模型内部的决策逻辑变得前所未有的晦涩。传统的基于事后（Post-hoc）特征归因的方法，如简单的梯度显著性图或局部线性代理模型，已难以应对Transformer架构中复杂的上下文依赖和非线性推理链条。

2022年至2025年间，XAI领域经历了一场深刻的范式转移：从“黑盒观察”转向“白盒解剖”。学术界不再满足于仅知道模型“看”了哪里，而是致力于揭示模型“想”了什么。这一时期，机械解释性（Mechanistic Interpretability） 异军突起，试图通过逆向工程神经网络的微观结构（如神经元和注意力头）来还原算法层面的计算过程；概念瓶颈模型（Concept Bottleneck Models, CBMs） 通过架构创新，将无法解释的隐层表示强制映射为人类可理解的语义概念，实现了从设计之初的透明化；而特征归因（Feature Attribution） 则在面对对抗攻击的脆弱性危机中，向着高阶交互量化和鲁棒性理论演进。

此外，随着《欧盟人工智能法案》（EU AI Act）在2025年的全面实施，模型决策透明度已从技术选型上升为法律合规的硬性要求 。这种外部监管压力迫使学术界和工业界重新审视解释性技术的可靠性、忠实度（Faithfulness）和可干预性（Intervenability）。本综述将深入剖析这一时间窗口内的代表性研究工作，系统梳理从微观神经元解耦到宏观概念推理的最新技术进展。   

2. 机械解释性：逆向工程神经网络的微观计算逻辑
机械解释性（Mechanistic Interpretability, MI）代表了XAI领域最前沿、最硬核的研究方向。其核心认识论假设是：神经网络并非不可知的混沌，其内部必然存在着通过训练习得的、可被人理解的算法或“回路”（Circuits）。然而，阻碍理解的最大障碍在于“特征叠加”（Superposition）现象——即模型为了在高维空间中存储超过神经元数量的特征，迫使多个不相关的特征共享同一个神经元，导致单个神经元表现出多义性（Polysemanticity）。2023年至2025年的研究重点，正是围绕如何解开这种叠加态，提取出单语义特征，并绘制出模型内部的计算图谱。

2.1 稀疏自编码器（SAE）与单语义性的规模化验证
在解决多义性神经元的问题上，稀疏自编码器（Sparse Autoencoders, SAEs） 成为了事实上的标准工具。这一方法的基本逻辑是：通过训练一个比原模型层宽得多的稀疏自编码器，将模型激活值投影到一个超完备的特征空间，在这个空间中，特征被强制解耦为稀疏的、单语义的方向。

代表性工作分析：

Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 Sonnet (Anthropic, 2024)    

问题背景：在2024年之前，字典学习（Dictionary Learning）和SAE主要在小型“玩具模型”或单层Transformer上进行验证。学术界普遍存在疑虑：这种方法能否扩展到拥有数千亿参数的前沿大模型（Frontier Models）？大模型中的概念是否过于抽象，以至于无法被线性特征捕捉？

方法论：Anthropic的研究团队在生产级的Claude 3 Sonnet模型上应用了大规模稀疏自编码器。他们从模型的中间层（Residual Stream）提取激活向量，训练SAE以重构这些激活值，同时对SAE的隐层施加L1稀疏惩罚。这种方法迫使SAE学习出一组特定的“特征方向”，每个方向对应一个独立的语义概念。

实验结论与洞察：研究成功提取了数百万个高质量特征，这些特征表现出极高的单语义性。除了具体的实体概念（如“金门大桥”、“脑科学”），更令人震惊的是发现了高度抽象的特征，例如“代码中的缓冲区溢出漏洞”、“带有偏见的言论”甚至“欺骗性行为”。实验通过“特征操纵”（Feature Steering）验证了因果性：通过人工钳制（Clamping）特定特征的激活值，可以精确控制模型的输出风格或行为倾向（例如，增强“阿谀奉承”特征会导致模型极度迎合用户）。这不仅证明了叠加态可以通过SAE解开，还揭示了SAE性能遵循缩放定律（Scaling Laws），即投入更多算力训练更大的SAE能挖掘出更罕见、更细粒度的特征。

Sparse Autoencoders Find Highly Interpretable Features in Language Models (ICLR 2024)    

问题背景：传统的矩阵分解方法（如PCA或ICA）假设特征是正交的，这与神经网络中特征非正交叠加的现实不符，导致提取的成分依然是多义的混杂体。

方法论：作者在Pythia-410M等开源模型上进行了系统性的SAE训练。与Anthropic的工作类似，该研究强调了L1正则化在诱导稀疏性中的关键作用，并引入了自动化的解释性评分系统，利用另一个语言模型（如GPT-4）来自动为发现的特征生成自然语言解释，并验证其激活模式是否符合解释。

实验结论：实验表明，SAE发现的特征在“间接宾语识别”（IOI）等特定算法任务中，能够比原始神经元更精确地定位因果回路。例如，IOI任务涉及特定的注意力头将信息从前文移动到当前位置，SAE成功分解了负责这一过程的复合神经元。这为“自动化回路发现”提供了坚实的基石，证明了无监督的字典学习可以作为透视模型内部运作的“显微镜”。

Transcoders Find Interpretable LLM Feature Circuits (NeurIPS 2025 Context)    

问题背景：虽然SAE能解释某一层的激活，但要理解模型如何进行推理，我们需要连接层与层之间的因果链。传统的MLP层不仅存在特征叠加，还引入了非线性变换，使得直接追踪特征（Feature Circuits）变得极其困难。

方法论：DeepMind与Anthropic的研究者提出了一种名为**Transcoders（转码器）**的新架构。不同于标准SAE旨在重构同一层的输入，Transcoder被训练用于预测下一层的输出（即跨过MLP层或注意力块）。实际上，这相当于用一个可解释的、稀疏的神经网络组件替换了原始模型中不可解释的MLP层。

实验结论：Transcoders在保持原模型预测性能的同时，生成了可以直接用于构建计算图的稀疏特征。在算术推理和事实检索任务中，研究者利用Transcoders成功绘制出了跨越多个层级的特征依赖图，清晰展示了模型如何从底层感知特征逐步抽象出高层逻辑概念。这被视为连接微观特征分析与宏观行为解释的关键桥梁。

2.2 自动化回路发现与归因修补的高效化
如果说SAE是识别模型的“零件”，那么回路发现（Circuit Discovery）就是绘制“电路图”。由于大模型的参数空间巨大，手动寻找负责特定任务的子图（Sub-graph）已不再可行，自动化方法的效率成为研究焦点。

代表性工作分析：

Attribution Patching Outperforms Automated Circuit Discovery (BlackboxNLP 2024 / NeurIPS 2024 Context)    

问题背景：现有的自动化回路发现算法，如ACDC（Automatic Circuit Discovery），依赖于激活修补（Activation Patching）技术。该技术通过反复替换模型中间激活值并观察输出变化来判定组件重要性，计算成本极高，通常需要对计算图中的每条边进行前向传播，这在时间复杂度上是不可接受的。

方法论：该论文提出了一种基于梯度的近似方法——Edge Attribution Patching (EAP)。EAP利用泰勒展开（Taylor Expansion），将激活修补视为对模型输出的一种微小扰动，从而可以通过计算梯度与激活差值的乘积来线性近似修补效果。这意味着，仅需两次前向传播（一次清洁输入，一次损坏输入）和一次反向传播，即可估算出全图所有边的重要性分数。

实验结论：在多个标准解释性任务（如IOI任务、大数加法）中，EAP不仅在速度上比ACDC快了数个数量级，而且在回路恢复的准确率（AUC指标）上表现更优。这一突破使得在商用大模型上实时定位特定任务的推理回路成为可能，不再受限于算力瓶颈。

表 1：机械解释性代表性方法对比

方法类别	代表性论文	核心机制	优势	局限性
稀疏特征提取	
Scaling Monosemanticity 

稀疏自编码器 (SAE) + L1正则	解开特征叠加，实现单语义特征提取与操纵	SAE训练成本高，存在“死神经元”问题
跨层特征映射	
Transcoders 

预测下一层输出的稀疏网络替代MLP	直接构建跨层特征因果图，连接微观与宏观	需要替换原模型组件，可能引入微小性能偏差
回路发现	
Attribution Patching 

线性梯度近似 (Taylor Expansion)	计算效率极高，可扩展至大模型全图分析	线性近似在高度非线性区域可能存在误差
  
3. 概念瓶颈模型：从“黑盒”到“玻璃盒”的架构重构
与机械解释性试图在事后拆解黑盒不同，概念瓶颈模型（Concept Bottleneck Models, CBMs） 选择了一条更为彻底的路径：通过架构设计，强制模型在输入（如图像）和输出（如分类）之间通过一个人类可理解的“概念层”（Concept Layer）。2022年至2025年的研究主要集中在打破CBMs的“性能-解释性权衡”（Accuracy-Interpretability Trade-off），并引入大模型来自动化概念的构建过程。

3.1 视觉-语言引导下的概念自动化与校准
传统的CBM依赖人工定义的概念集（如CUB数据集中的“红色的腿”、“尖锐的喙”），这不仅标注成本高昂，且概念集往往不完备。2024年的研究趋势是利用大语言模型（LLMs）和视觉语言模型（VLMs）来自动化这一过程。

代表性工作分析：

VLG-CBM: Training Concept Bottleneck Models with Vision-Language Guidance (NeurIPS 2024)    

问题背景：现有的自动化CBM面临严重的“忠实度”（Faithfulness）问题。模型可能正确预测了概念（例如“有轮子”），但实际上是依据背景纹理而非物体本身做出的判断。此外，概念之间存在大量信息泄漏，导致“有效概念数量”（Number of Effective Concepts, NEC）虚高，即模型利用了大量冗余概念来堆砌性能。

方法论：VLG-CBM框架引入了开放域目标检测器（如Grounding DINO）和视觉语言模型（如CLIP）作为教师信号。它不直接学习概念分类，而是学习将图像特征映射到VLM定义的语义空间，并强制模型在预测概念时必须关注与该概念语义对应的图像区域（Visual Grounding）。同时，作者提出了NEC指标作为正则化项，惩罚那些对最终预测没有独立贡献的冗余概念。

实验结论：在CUB、Places365等五个标准基准上，VLG-CBM展现了显著的性能提升。在限制仅使用5个有效概念（NEC=5）的严苛条件下，其分类准确率比现有SOTA方法提升了4.27%至51.09%。更重要的是，定性实验显示，VLG-CBM生成的解释热图精确地覆盖了概念对应的物体部件，极大提升了用户信任度。

Concept Bottleneck Models with Large Language Models (Two-step Methodology) (2025)    

问题背景：在医疗影像（如皮肤镜图像）分析中，标注数据极其稀缺，且重新训练一个端到端的CBM成本高昂。如何利用现有的基础模型实现即插即用的解释性？

方法论：该研究提出了一种无需训练（Training-free）的两步法。第一步，利用预训练的医疗领域VLM（如PubMedCLIP）基于图像零样本预测临床概念；第二步，将这些预测出的概念转化为结构化文本Prompt，输入给通用LLM（如GPT-4）进行最终的诊断推理。该框架天然支持“测试时干预”（Test-time Intervention），医生可以直接修改第一步输出的错误概念，系统会自动更新诊断结果。

实验结论：在皮肤病变诊断任务中，这种无需微调的方法在少样本甚至零样本设置下，性能超越了需要全监督训练的传统CBM。这证明了将“感知”（由VLM负责）与“推理”（由LLM负责）解耦，是提升特定领域解释性系统的有效途径。

3.2 概率化与能量基视角下的概念交互
早期的CBM假设概念是独立的，且概念到标签的映射是单向的。然而，现实世界中的概念往往高度相关（如“有翅膀”与“能飞”），且标签信息可以反向约束概念的合理性。

代表性工作分析：

Energy-Based Concept Bottleneck Models (ECBM) (ICLR 2024)    

问题背景：标准CBM无法处理概念之间的依赖关系，也无法在预测标签时反向利用标签的先验知识来修正不确定的概念。

方法论：ECBM利用基于能量的模型（Energy-Based Models, EBM）框架，定义了一个定义在输入x、概念c和标签y上的联合能量函数E(x,c,y)。通过最小化能量，模型可以同时捕捉P(c∣x)（概念预测）、P(y∣c)（标签预测）以及P(c∣y)（概念反推）。这种统一的概率视角使得ECBM不仅能进行预测，还能进行“概念修正”（Concept Correction），即当用户修正某一概念时，模型能利用学习到的能量景观自动更新其他相关概念。

实验结论：在真实数据集上的实验表明，ECBM在接受单次人工干预后，其性能提升幅度显著优于基线模型。这表明模型成功学会了概念之间的高阶依赖结构（如逻辑蕴含或互斥关系）。

Hybrid Concept Bottleneck Models (HybridCBM) (CVPR 2025)    

问题背景：预定义的概念集永远无法完备覆盖所有分类所需的特征（Concept Completeness Gap）。完全依赖预定义概念会导致性能天花板。

方法论：HybridCBM提出了一种混合架构，包含“静态概念库”和“动态概念库”。静态库由LLM生成，保证解释性；动态库则是可学习的隐向量，用于捕捉那些难以用语言描述但对分类至关重要的视觉特征。

实验结论：该模型在保持高度可解释性的同时，填补了CBM与黑盒ResNet/ViT模型之间的性能差距。研究还引入了新的度量标准来评估动态概念的语义一致性。

4. 特征归因：从脆弱的显著性图到鲁棒的高阶交互
特征归因（Feature Attribution）方法（如LIME, SHAP, Grad-CAM）曾是XAI的主流，但在2022年前后遭遇了信任危机。研究表明，这些方法对输入中的微小噪声极度敏感（Fragility），且容易产生误导性的解释。2023-2025年的工作致力于从数学原理上修复这些缺陷，重点关注鲁棒性（Robustness）和高阶交互（Higher-order Interactions）。

4.1 Shapley值的多阶扩展与效率革命
SHAP-IQ: Unified Approximation of Any-Order Shapley Interactions (NeurIPS 2024)    

问题背景：经典的Shapley值只能告诉我们每个特征单独的重要性，却掩盖了特征之间的协同（Synergy）与冗余（Redundancy）。例如，在自然语言处理中，否定词“不”和形容词“好”单独看都不足以决定情感，只有它们的组合“不好”才具有决定性意义。计算这种高阶交互指数（Shapley Interaction Index）的复杂度随着阶数指数级增长，在实际应用中几乎不可行。

方法论：SHAP-IQ提出了一种基于采样的高效估计器。它利用了“离散半值”（Discrete Semivalues）的理论性质，设计了一种能够最大化样本重用（Maximum Sample Reuse）的采样算法。该算法可以在一次采样过程中同时逼近任意阶（Any-order）的交互指数，从而在有限的计算预算下大幅降低估计方差。

实验结论：在BERT等语言模型的情感分析任务中，SHAP-IQ成功识别出了注意力头之间复杂的协同模式。这种能力使得研究者首次能够量化Transformer模型中“上下文混合”（Context Mixing）的具体程度，区分哪些特征是独立起作用的，哪些必须依赖上下文。

4.2 频域归因与对抗鲁棒性
Fourier Feature Attribution (arXiv 2025)    

问题背景：现有的归因方法主要在空间域（Spatial Domain）操作（如像素级热图）。然而，神经网络已被证明倾向于依赖频域特征（Spectral Bias）。空间域归因往往受到高频噪声的干扰，导致解释图看起来杂乱无章且不抗攻击。

方法论：该论文提出从信号处理的视角重新审视归因问题，设计了傅里叶特征归因（Fourier Feature Attribution）。该方法通过对输入进行傅里叶变换，在频域内计算各频率分量对模型输出的边际贡献（Marginal Contribution）。由于对抗攻击通常引入的是高频扰动，而在频域归因中这些扰动往往与主要语义特征分离，因此该方法天然具有更强的鲁棒性。

实验结论：在ImageNet数据集上，傅里叶特征归因在“类内集中度”（Intra-class Concentration）和“类间区分度”（Inter-class Distinction）指标上均优于Grad-CAM和IG。这意味着同一类别的图像在频域解释上表现出更一致的模式，更符合人类对“概念”稳定性的直觉。

Towards More Robust Interpretation via Local Gradient Alignment (AAAI 2023 / NeurIPS Context)    

问题背景：对抗攻击可以在不改变预测结果的情况下，通过添加不可察觉的噪声，使梯度方向发生剧烈偏转，从而生成完全错误的解释热图。这被称为“解释性攻击”。

方法论：作者提出了一种新的正则化训练方法。除了最小化预测误差外，还在损失函数中加入了一项正则项，旨在对齐局部梯度。具体而言，该方法不仅约束输入点处的Hessian范数（使损失曲面平滑），还引入了余弦距离准则，强制要求输入点附近的梯度方向保持一致。

实验结论：在CIFAR-10和ImageNet-100的大规模实验中，经此方法训练的模型在遭受PGD等强对抗攻击时，其生成的解释热图依然能稳定地聚焦于目标物体，鲁棒性显著优于仅使用对抗训练的基线模型。

5. 2025年趋势预测与未来展望
综合2024年底至2025年初的顶会论文流向及产业动态，模型解释性与决策透明度领域正呈现出以下四大不可逆转的趋势：

5.1 解释性与安全对齐的深度融合 (From Explanation to Steering)
Anthropic在2024年的单语义性研究开启了“解释即控制”的新篇章。未来的XAI将不再止步于被动地解释模型为何出错，而是将解释性特征作为安全干预的接口。预测在2025年，**基于特征操纵（Feature Steering）**的技术将成为大模型对齐（Alignment）的主流手段。通过钳制特定的不安全特征（如“生物武器制造知识”或“欺骗意图”），开发者可以在不重新训练模型的情况下实现精确的“脑叶切除”，这比传统的RLHF更具针对性和可验证性。

5.2 法律合规驱动的技术标准化 (Standardization via Regulation)
随着《欧盟人工智能法案》（EU AI Act）对通用人工智能（GPAI）透明度要求的生效，XAI将从学术探索走向工业标准。学术界提出的评估基准，如LATEC  和Navigating the Maze ，将逐步演变为法律合规的审计工具。企业将被要求提供技术文档，证明其高风险AI系统的决策过程是可追踪的（Traceable）。这将淘汰大量仅能产生“漂亮图片”但不具备数学严谨性的可视化方法（如某些不稳定的Attention Rollout），转而采用经过形式化验证的归因技术。   

5.3 神经符号AI在科学发现中的回归 (Neurosymbolic Renaissance for Science)
在药物发现、材料科学等“AI for Science”领域，纯黑盒模型因缺乏物理可解释性而面临信任瓶颈。MARS  等工作表明，将深度学习的强拟合能力与符号逻辑的规则推理相结合的**神经符号方法（Neurosymbolic AI）**将强势回归。这类系统利用神经网络学习符号规则的权重，既保留了泛化能力，又保证了推理过程符合领域知识（如化学反应机理），这对于高风险的科学决策至关重要。   

5.4 解释性与性能的“双赢”而非“权衡” (Breaking the Trade-off)
长期以来，学界认为提高解释性必然牺牲性能。然而，VLG-CBM  和 Transcoders  的成功打破了这一迷思。通过引入外部知识（如VLM的视觉定位能力）或更高效的稀疏架构，2025年的模型有望在保持甚至超越SOTA性能的同时，提供细粒度的白盒解释。未来的基础模型架构在设计之初就将包含“解释性接口”，而非事后外挂解释器。   

参考文献
   

Templeton, A., et al. (2024). Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 Sonnet. Anthropic Research.

   

Cunningham, H., et al. (2024). Sparse Autoencoders Find Highly Interpretable Features in Language Models. International Conference on Learning Representations (ICLR).

   

Srivastava, D., Yan, G., & Weng, T.-W. (2024). VLG-CBM: Training Concept Bottleneck Models with Vision-Language Guidance. Advances in Neural Information Processing Systems (NeurIPS).

   

Xu, X., et al. (2024). Energy-Based Concept Bottleneck Models: Unifying Prediction, Concept Intervention, and Probabilistic Interpretations. International Conference on Learning Representations (ICLR).

   

Fumagalli, F., et al. (2024). SHAP-IQ: Unified Approximation of Any-Order Shapley Interactions. Advances in Neural Information Processing Systems (NeurIPS).

   

Syed, A., Rager, C., & Conmy, A. (2024). Attribution Patching Outperforms Automated Circuit Discovery. Proceedings of the 7th BlackboxNLP Workshop at EMNLP (Best Paper Context).

   

Liu, Y., Zhang, T., & Gu, S. (2025). Hybrid Concept Bottleneck Models. IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR).

   

Dunefsky, J., et al. (2024). Transcoders Find Interpretable LLM Feature Circuits. Advances in Neural Information Processing Systems (NeurIPS).

   

Liu, Z., et al. (2025). Fourier Feature Attribution: A New Efficiency Attribution Method. arXiv preprint arXiv:2504.02016.

   

Klein, L., et al. (2024). Navigating the Maze of Explainable AI: A Systematic Approach to Evaluating Methods and Metrics. Advances in Neural Information Processing Systems (NeurIPS).

   

Joo, S., et al. (2023). Towards More Robust Interpretation via Local Gradient Alignment. AAAI Conference on Artificial Intelligence.

   

DeLong, L. N., et al. (2024). MARS: A Neurosymbolic Approach for Interpretable Drug Discovery. arXiv preprint arXiv:2410.05289.

   

Vandenhirtz, M., et al. (2024). Stochastic Concept Bottleneck Models. Advances in Neural Information Processing Systems (NeurIPS).

   

Patricio, C., et al. (2025). Concept Bottleneck Models with Large Language Models. Research Network of Computational and Structural Biotechnology.

   

Protiviti & Bond Schoeneck & King PLLC. (2025). EU AI Act: Explainability Requirements and Compliance Timeline. Legal Analysis Reports.


protiviti.com
A guide to the EU AI Act: Regulations, compliance and best practices - Protiviti
在新窗口中打开

bsk.com
The EU AI Act: What U.S. Companies Need to Know
在新窗口中打开

transformer-circuits.pub
Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 Sonnet
在新窗口中打开

lesswrong.com
A “Scaling Monosemanticity” Explainer - LessWrong
在新窗口中打开

anthropic.com
The engineering challenges of scaling interpretability - Anthropic
在新窗口中打开

iclr.cc
ICLR 2024 Papers
在新窗口中打开

chatpaper.com
Sparse Autoencoders Find Highly Interpretable Features in Language Models - ChatPaper
在新窗口中打开

openreview.net
Sparse Autoencoders Find Highly Interpretable Features in Language Models
在新窗口中打开

arxiv.org
Sparse Autoencoders Find Highly Interpretable Features in Language Models - arXiv
在新窗口中打开

researchgate.net
Transcoders find interpretable LLM feature circuits - ResearchGate
在新窗口中打开

openreview.net
Transcoders find interpretable LLM feature circuits | OpenReview
在新窗口中打开

proceedings.com
Transcoders find interpretable LLM feature circuits - proceedings.com
在新窗口中打开

aclanthology.org
Attribution Patching Outperforms Automated Circuit Discovery - ACL Anthology
在新窗口中打开

semanticscholar.org
[PDF] Attribution Patching Outperforms Automated Circuit Discovery | Semantic Scholar
在新窗口中打开

nips.cc
NeurIPS 2024 Papers
在新窗口中打开

arxiv.org
VLG-CBM: Training Concept Bottleneck Models with Vision-Language Guidance - arXiv
在新窗口中打开

lilywenglab.github.io
VLG-CBM: Training Concept Bottleneck Models with Vision-Language Guidance
在新窗口中打开

pmc.ncbi.nlm.nih.gov
A two-step concept-based approach for enhanced interpretability and trust in skin lesion diagnosis - NIH
在新窗口中打开

openreview.net
Energy-Based Concept Bottleneck Models: Unifying Prediction, Concept Intervention, and Probabilistic Interpretations | OpenReview
在新窗口中打开

wanghao.in
energy-based concept bottleneck models: unifying prediction, concept intervention - Hao Wang
在新窗口中打开

arxiv.org
Energy-Based Concept Bottleneck Models: Unifying Prediction, Concept Intervention, and Probabilistic Interpretations - arXiv
在新窗口中打开

chatpaper.com
Hybrid Concept Bottleneck Models - ChatPaper
在新窗口中打开

openaccess.thecvf.com
Hybrid Concept Bottleneck Models - CVPR 2025 Open Access Repository
在新窗口中打开

proceedings.neurips.cc
One Sample Fits All: Approximating All Probabilistic Values Simultaneously and Efficiently - NIPS papers
在新窗口中打开

epub.ub.uni-muenchen.de
shapiq: Shapley Interactions for Machine Learning - Open Access LMU
在新窗口中打开

proceedings.neurips.cc
shapiq: Shapley Interactions for Machine Learning
在新窗口中打开

arxiv.org
Fourier Feature Attribution: A New Efficiency Attribution Method - arXiv
在新窗口中打开

researchgate.net
Fourier Feature Attribution: A New Efficiency Attribution Method | Request PDF
在新窗口中打开

arxiv.org
[2504.02016] Fast Fourier Correlation is a Highly Efficient and Accurate Feature Attribution Algorithm from the Perspective of Control Theory and Game Theory - arXiv
在新窗口中打开

researchgate.net
Towards More Robust Interpretation via Local Gradient Alignment - ResearchGate
在新窗口中打开

researchgate.net
Navigating the Maze of Explainable AI: A Systematic Approach to Evaluating Methods and Metrics | Request PDF - ResearchGate
在新窗口中打开

proceedings.com
Navigating the Maze of Explainable AI: A Systematic Approach to Evaluating Methods and Metrics - proceedings.com
在新窗口中打开

arxiv.org
MARS: A neurosymbolic approach for interpretable drug discovery - arXiv
在新窗口中打开

openreview.net
Navigating the Maze of Explainable AI: A Systematic Approach to Evaluating Methods and Metrics | OpenReview
在新窗口中打开

arxiv.org
[2410.05289] MARS: A neurosymbolic approach for interpretable drug discovery - arXiv
在新窗口中打开

research-collection.ethz.ch
Stochastic Concept Bottleneck Models - ETH Zurich Research Collection
在新窗口中打开

openreview.net
Stochastic Concept Bottleneck Models - OpenReview