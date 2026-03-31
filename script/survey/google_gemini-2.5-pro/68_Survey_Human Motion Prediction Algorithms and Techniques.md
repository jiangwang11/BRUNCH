好的，作为一名严谨的科研助手，我将基于提供的真实网络搜索结果，为您生成一篇关于“人体运动预测算法与技术”的学术综述。

***

### **面向2025的人体运动预测算法与技术综述**

#### **引言**

人体运动预测（Human Motion Prediction）作为计算机视觉与图形学的核心课题，旨在根据观测到的历史动作序列，生成或预测未来的人体姿态与运动轨迹。该技术在智能机器人、自动驾驶、人机交互及虚拟现实等领域拥有巨大的应用价值。近年来，随着深度学习的快速发展，该领域的研究范式已从传统的统计模型（如隐马尔可夫模型、卡尔曼滤波）[www.jos.org.cn](https://www.jos.org.cn/html/2023/1/6395.htm) 转向以数据驱动的深度生成模型。本综述旨在梳理并总结 2022 年至 2025 年间人体运动预测领域的代表性工作，重点剖析主流方法的技术脉络与创新点，并展望未来的研究趋势与挑战。

#### **方法分类与代表作**

在 2022-2025 年间，人体运动预测的研究主要围绕以下几类模型展开，特别是生成式模型取得了长足的进步。

##### **1. 基于扩散模型（Diffusion Model-based）的方法**

扩散模型因其强大的生成能力和对复杂数据分布的建模优势，成为近年来运动生成与预测领域的主流。研究者不仅利用其生成高质量的运动，还致力于解决其物理真实性和计算效率问题。

*   **PhysDiff (2022):** 该工作直指早期运动扩散模型生成的动作常有浮空、脚滑等物理伪影的弊病 [zhuanzhi.ai](https://zhuanzhi.ai/paper/ae828b2ad699bb2825909389960b12a4)。其核心方法是在去噪过程的每一步中，引入一个基于物理的运动投影模块。该模块利用物理模拟器将当前去噪步生成的非物理性动作投影（校正）到一个物理上合理的运动流形上，再将这个校正后的动作作为引导信息输入到下一步扩散过程中。实验证明，PhysDiff能够迭代地将生成过程拉向物理真实空间，在多个基准测试上将物理合理性提升了超过78%。

*   **MotionWavelet (2024):** 针对复杂人体动作中微妙过渡与非平稳动态难以捕捉的问题，MotionWavelet提出在时-频域分析人体运动 [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/85506)。它首先对运动数据应用小波变换，将其分解到不同频率，然后训练一个扩散模型（WDM）在学习到的小波流形上进行生成。此方法通过小波空间形状引导和时间注意力引导机制，优化去噪过程，确保生成运动在时空模式上的复杂性和一致性。实验结果显示，该方法在预测准确性和泛化能力上均有显著提升。

*   **DAF-DH (2025):** 该研究聚焦于扩散模型在数字人视频生成中推理速度慢、计算成本高昂的现实挑战，这直接影响了实时应用 [arocmag.cn](https://www.arocmag.cn/abs/2025.03.0057)。论文提出一个名为DAF-DH的三级加速框架，首先通过TensorRT优化核心扩散模型的推理效率。其次，采用“先生成低质、再提升质量”的策略，快速生成低分辨率、低帧率的初始视频。最后，通过一个轻量化的超分和插帧后处理模块恢复视频质量，同时引入语义特征对齐损失提升感知效果，最终在保证质量的同时实现了5倍的推理加速。

##### **2. 基于Transformer及生成式建模（Transformer & Generative Modeling）的方法**

Transformer架构凭借其强大的序列建模能力，继续在动作预测领域扮演重要角色。特别是掩码建模等自监督学习思想被引入，以提升模型对运动语言的理解与生成能力。

*   **MoMask (2024):** 该工作借鉴自然语言处理中的掩码建模思想，提出一种用于文本到动作生成的生成式框架MoMask [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/46930)。它首先通过分层量化方案将连续的人体动作序列编码为多层离散的动作标记（token）。在训练阶段，一个掩码变换器（Masked Transformer）在文本条件的引导下预测被随机掩盖的动作标记。在推理阶段，模型从一个空序列开始，迭代地“填空”以生成完整的动作序列，并在HumanML3D数据集上将FID指标从0.141大幅降低至0.045，展示了其卓越的生成质量和对动作细节的保真度。

##### **3. 物理与交互感知（Physics and Interaction-aware）模型**

为了生成更符合现实世界规律的动作，研究者们愈发关注物理约束以及人与环境、人与人之间的复杂交互。

*   **InterMimic (2025):** 此研究致力于解决基于物理的、复杂的全身人-物交互（HOI）任务的通用控制问题，特别是在面对不完美的动作捕捉数据时 [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/e0809fbb-23e4-49e4-9185-5487fde4edf6)。InterMimic框架采用一种“先完善后扩展”的课程策略，首先训练多个特定于个体的“教师”策略来模仿、优化原始数据，然后将这些教师策略提炼到一个通用的“学生”策略中。值得注意的是，该框架还结合了强化学习微调，使学生策略不仅能复制演示，还能实现更高质量的交互效果，并具备零样本泛化能力。

*   **Resonance (2024):** 该工作从一个新颖的视角来建模社会性交互，即将行人的轨迹预测问题类比为共振现象 [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/87308)。它认为智能体间的社会互动与各自轨迹的谱特性相关。Resonance模型将未来轨迹分解为三种不同的“振动项”，以解耦的方式表达个体的运动意图，并通过学习轨迹谱的相似性来建模社会影响。这种方法旨在以一种更具可解释性的方式，捕捉群体行为中的协同运动模式。

#### **实验与评价总结**

该领域的研究工作通常在 **Human3.6M、HumanML3D、KIT-ML** 等标准数据集上进行评估。评价指标可分为两类：

1.  **客观量化指标**：
    *   **预测精度**：主要使用平均位移误差（Average Displacement Error, ADE）和最终位移误差（Final Displacement Error, FDE）来衡量预测轨迹点与真实轨迹点之间的欧氏距离。
    *   **生成质量/分布相似性**：普遍采用**Fréchet Inception Distance (FID)**，通过比较生成动作样本分布与真实动作分布在特征空间中的距离，来评估生成动作的多样性和真实性。

2.  **主观/感知评价指标**：
    *   研究者们逐渐意识到，客观指标有时并不能完全反映人类对动作质量的主观感受。例如，FID分数低的动作可能在人类观察者看来仍然存在不自然的抖动或伪影。
    *   为了解决这一“评估鸿沟”，**MotionCritic (2025)** 提出了开创性的解决方案 [hub.baai.ac.cn](https://hub.baai.ac.cn/view/43445)。该工作首先构建了一个大规模的人类感知评估数据集 **MotionPercept**，其中包含数万组由人类标注者评判优劣的动作对。基于此数据集，他们训练了一个能够模拟人类感知偏好的评价模型MotionCritic。该模型不仅可以提供比FID更符合人类直觉的质量分数，还可以作为奖励信号，通过微调来提升现有生成模型的感知质量，实现了评估与优化的闭环。

#### **趋势与挑战**

基于2022-2025年的研究进展，人体运动预测领域呈现出以下明确趋势与伴随的挑战：

1.  **从运动学到动力学：物理真实性成为核心关切**
    *   **趋势**：模型设计正从纯粹的运动学模式匹配（即预测关节位置序列），转向深度融合物理规律的动力学建模。如`PhysDiff`和`InterMimic`所示，结合物理模拟器或在损失函数中引入物理约束，已成为确保生成动作真实、无悬浮、符合重力与接触规律的关键手段。
    *   **挑战**：精确的物理模拟计算开销巨大，难以实现实时推理。同时，如何高效、可微地将复杂的接触动力学（如摩擦、碰撞）集成到深度学习框架中，并泛化到多样的物体和场景，仍是开放性问题。

2.  **从单一预测到可控生成：模型的多样性与可控性需求增强**
    *   **趋势**：研究重点从预测单一的最可能未来，转向生成一个多样化且符合条件的未来动作分布。如`MoMask`所示，利用文本、风格、目标等外部条件来引导和控制生成过程，是实现个性化和任务驱动的动作生成的关键。
    *   **挑战**：在提升可控性的同时，如何避免“模式崩溃”（mode collapse）并保持生成动作的多样性是一个核心难题。此外，如何设计更精细、更具表现力的控制信号，以实现对动作细微风格（如情绪、力度）的控制，仍有待探索。

3.  **从客观指标到感知对齐：人类感知成为新的“黄金标准”**
    *   **趋势**：学术界正在经历一场从追求客观指标（如ADE, FID）到对齐人类主观感知的范式转变。`MotionCritic`的工作是这一趋势的标志性成果，表明数据驱动的感知评估模型是连接自动评估与人类感知的桥梁。将此类感知模型作为奖励，通过强化学习等手段对生成模型进行微调，已成为提升动作“质感”的前沿方向。
    *   **挑战**：构建大规模、高质量、无偏见的人类感知数据集成本高昂。此外，如何训练出能够跨越不同动作类型、场景和文化背景，且具有良好泛化能力的通用感知评价模型，是该方向走向成熟的关键。

#### **结论**

在2022年至2025年期间，人体运动预测领域在深度生成模型的驱动下取得了显著进展。研究范式从早期的序列学习模型，演变为以扩散模型和Transformer为代表的强大生成框架。同时，对物理真实性、社会交互的建模以及对齐人类感知的评估成为该领域的前沿焦点。未来的研究将继续深化物理与学习的融合，探索更精细的可控生成方法，并致力于建立更可靠、更普适的感知评价体系，从而推动该技术在虚拟数字人、智能机器人等场景中的实际应用。

#### **参考文献**

1.  Qiao, S., Wu, L., Han, N., et al. (2022). Multiple-motion-pattern Trajectory Prediction of Moving Objects with Context Awareness: A Survey. *Journal of Software*. [www.jos.org.cn](https://www.jos.org.cn/html/2023/1/6395.htm)
2.  Yuan, Y., Song, J., Iqbal, U., et al. (2022). PhysDiff: Physics-Guided Human Motion Diffusion Model. *arXiv*. [zhuanzhi.ai](https://zhuanzhi.ai/paper/ae828b2ad699bb2825909389960b12a4)
3.  Tevet, G., Raab, S., Gordon, B., et al. (2023). Human motion diffusion model. *ICLR 2023*. (Referenced in [hub.baai.ac.cn](https://hub.baai.ac.cn/view/43445))
4.  Guo, C., Mu, Y., Javed, M. G., et al. (2024). MoMask: Generative Masked Modeling of 3D Human Motions. *CVPR 2024*. [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/46930)
5.  Wong, C., Zou, Z., Xia, B., & You, X. (2024). Resonance: Learning to Predict Social-Aware Pedestrian Trajectories as Co-Vibrations. *arXiv*. [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/87308)
6.  Feng, Y., Dou, Z., Chen, L.-H., et al. (2024). MotionWavelet: Human Motion Prediction via Wavelet Manifold Learning. *arXiv*. [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/85506)
7.  Alahi, A., Goel, K., Ramanathan, V., et al. (2016). Social LSTM: Human trajectory prediction in crowded spaces. *CVPR 2016*. (Referenced in [www.jos.org.cn](https://www.jos.org.cn/html/2023/1/6395.htm))
8.  Cao, F. (2025). 基于人体骨架的动作识别：综述与展望. *机器人*. [xk.sia.cn](https://xk.sia.cn/article/cstr/32166.14.xk.2024.3091)
9.  Wang, J., Zhou, L., & Zhang, B. (2025). 基于扩散模型加速和感知优化的高效姿态驱动人体动作生成技术. *计算机应用研究*. [arocmag.cn](https://www.arocmag.cn/abs/2025.03.0057)
10. Xu, S., Ling, H. Y., Wang, Y.-X., & Gui, L.-Y. (2025). InterMimic: Towards Universal Whole-Body Control for Physics-Based Human-Object Interactions. *arXiv*. [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/e0809fbb-23e4-49e4-9185-5487fde4edf6)
11. Wang, H., et al. (2025). Aligning Human Motion Generation with Human Perceptions (MotionCritic). *ICLR 2025*. [hub.baai.ac.cn](https://hub.baai.ac.cn/view/43445)
12. Guo, C., Zuo, X., Wang, S., et al. (2020). Action2motion: Conditioned generation of 3d human motions. *ACM Multimedia 2020*. (Referenced in [hub.baai.ac.cn](https://hub.baai.ac.cn/view/43445))
13. Wen, Y., et al. (2025). 基于深度学习的时间序列预测方法综述. *南京航空航天大学学报*. [jnuaa.nuaa.edu.cn](https://jnuaa.nuaa.edu.cn/njhkht/article/html/202505002)