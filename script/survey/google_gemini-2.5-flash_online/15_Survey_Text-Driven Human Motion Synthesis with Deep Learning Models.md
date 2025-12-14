好的，这是一篇关于“基于深度学习模型的文本驱动人体动作合成”的学术综述，涵盖 2022-2025 年的代表性工作。

---

## 基于深度学习模型的文本驱动人体动作合成学术综述 (2022-2025)

### 引言

文本驱动人体动作合成（Text-Driven Human Motion Synthesis）旨在从自然语言描述生成逼真、流畅且符合语义的三维人体动作序列，是计算机图形学、虚拟现实、人机交互等领域的核心研究问题。近年来，随着深度学习技术的飞速发展，特别是生成模型与大语言模型（LLM）的兴起，文本驱动人体动作合成取得了显著进展。本综述将聚焦 2022-2025 年间该领域的代表性工作，系统梳理其方法分类、核心技术及发展趋势。

### 方法分类与代表作

当前文本驱动人体动作合成方法主要可分为基于扩散模型、基于自回归模型以及结合分层与掩码策略的模型。

#### 1. 基于扩散模型 (Diffusion Models)

扩散模型因其强大的生成能力和样本多样性，已成为动作合成领域的主流范式。

*   **[themoonlight.io]** 《Multi-Track Timeline Control for Text-Driven 3D Human Motion Generation》提出了一种多轨时间线控制方法，解决了现有方法在精细化控制和组合多个动作方面的不足。其核心思想是允许用户通过并行轨道指定带时间区间的文本提示，并开发了一种时空运动拼贴（Spatio-Temporal Motion Collage, STMC）的测试时去噪方法，能够与预训练的运动扩散模型集成，精确生成复合动画。实验证明 STMC 在 HumanML3D 数据集上优于基线方法，并能忠实执行时间线语义。此外，该工作还改进了MDM模型，提出了MDM-SMPL，直接使用SMPL模型作为运动表示，并加快了采样速度。

*   **[arocmag.cn]** 《基于扩散模型加速和感知优化的高效姿态驱动人体动作生成技术》针对扩散模型生成速度慢、计算成本高的问题，提出了一种加速框架 (DAF-DH)。该框架采用三级加速策略，包括通过 TensorRT 优化扩散模型推理效率、结合降低输入分辨率和抽帧生成低分辨率视频，以及设计轻量化后处理模块提升视频分辨率和流畅度。此外，引入语义特征对齐损失函数以提升主观感知质量，并在MimicMotion基础上实现了5倍加速比，同时提升了生成质量，LPIPS指标降低0.033，FVD指标减少82.9，验证了在实时数字人视频生成应用中的有效性。

*   **[themoonlight.io]** 《SyncDiff: Synchronized Motion Diffusion for Multi-Body Human-Object Interaction Synthesis》提出了 SyncDiff 框架，旨在合成多体人-物交互的协调运动。该方法通过引入“对齐分数”和相应的“对齐损失函数”，以及在推理阶段的显式同步策略，有效处理多体运动同步问题。利用频域运动分解提升运动保真度，并通过损失函数优化数据似然性和对齐有效性。实验表明，SyncDiff 在多个数据集上表现出优越性能，显著提高了多体交互运动的真实性和协调性。

#### 2. 基于分层与掩码策略的模型 (Hierarchical and Masked Modeling)

此类方法通过将复杂的动作分解为不同层次的离散标记或利用掩码预测机制，提升生成动作的细节度和控制性。

*   **[chatpaper.com]** 《MoMask: Generative Masked Modeling of 3D Human Motions》引入了一种新的基于文本驱动的 3D 人类动作生成掩码建模框架。该框架采用分层量化方案将人类动作表示为多层离散动作标记，其中包含一个掩码变换器预测随机掩码的动作标记，以及一个残差变换器逐步预测下一层的标记。MoMask 在 HumanML3D 数据集上的 FID 达到 0.045 (T2M-GPT 为 0.141)，在 KIT-ML 上的 FID 达到 0.228 (0.514)，表明其在文本到动作生成任务中优于现有最先进方法，并可无缝应用于文本引导的时间修复等相关任务。

*   **[chatpaper.com]** 《MIMO: Controllable Character Video Synthesis with Spatial Decomposed Modeling》提出了 MIMO 框架，用于可控角色视频合成。该方法通过空间分解建模，将 2D 视频编码为紧凑的空间编码，并基于深度信息将视频分解为主要人物、底层场景和浮动遮挡三个空间组件。这些组件被编码为规范身份编码、结构化运动编码和完整场景编码，作为合成过程的控制信号，实现了对角色、动作和场景属性的灵活用户控制。实验证明 MIMO 在新创建的 HUD-7K 数据集上，能生成高质量的角色视频，并对未知 3D 动作和交互场景具有良好的泛化能力。

#### 3. 基于自回归模型 (Autoregressive Models)

自回归模型通过逐步预测动作序列，尤其在处理变长动作生成方面展现出优势。

*   **[hub.baai.ac.cn]** 《BAMM: Bidirectional Autoregressive Motion Model》提出了一种新的文本到动作生成框架——双向自回归运动模型（BAMM）。该模型包含一个运动分词器将 3D 人体运动转化为潜在空间中的离散标记，以及一个掩码自注意力变换器通过混合注意力掩码策略自回归地预测随机掩码标记。BAMM 解决了现有去噪模型对动作长度先验知识的限制，通过统一生成掩码建模和自回归建模，捕捉了运动标记之间丰富的双向依赖关系，并能够动态调整运动序列长度。在 HumanML3D 和 KIT-ML 数据集上的实验表明，BAMM 在定性和定量指标上均超过了当前最先进的方法，实现了高质量运动生成和内置的运动可编辑性。

### 实验与评价总结

综上所述，当前文本驱动人体动作合成模型的实验评估主要围绕以下几个方面展开：

1.  **动作质量与逼真度：** 采用 FID (Fréchet Inception Distance)、Diversity 和 R-Precision 等量化指标，评估生成动作与真实动作分布的相似度、样本多样性和文本-动作匹配度。最新研究如 MoMask 在 FID 指标上已达到 0.045，显著优于以往模型。
2.  **语义一致性：** 评估生成动作是否准确反映文本描述的语义内容，通常通过 R-Precision 或用户研究进行定性或定量分析。
3.  **动作流畅度与自然性：** 通过关节速度、加速度、平滑度等指标评估动作的物理合理性，并通过用户主观感知反馈进行补充。
4.  **泛化能力：** 在未见过的文本指令、新颖动作或不同角色上测试模型的性能，例如 MIMO 在新姿态和交互场景上的表现。
5.  **效率与实时性：** 评估生成速度和计算资源消耗，如 DAF-DH 实现了 5 倍加速，这对实时应用至关重要。
6.  **可控性与可编辑性：** 考察模型是否能实现精细化的动作控制（如多轨时间线控制）、局部动作编辑以及生成结果的灵活组合。

值得注意的是，随着模型性能的提升，评估方法也日益精进。 **[hub.baai.ac.cn]** 《MotionCritic：对齐人类感知的动作生成与评价》便提出了一种数据驱动的方法——MotionCritic，通过大规模人类感知评估数据集 MotionPercept 训练，以捕捉人类的运动感知偏好。该模型不仅能作为更准确的度量标准进行评估，还能作为监督信号集成到生成模型中进行优化，有效弥补传统客观指标与人类主观感知之间的鸿沟。

### 趋势与挑战

面向 2025 年及更远的未来，文本驱动人体动作合成领域将呈现以下趋势：

1.  **更高保真度与复杂性动作合成：** 模型将不断提升生成动作的物理真实感、细节丰富度和动作库的覆盖范围，超越简单的重复动作，能够合成具有情感、多重交互和复杂叙事性的动作序列。例如，SyncDiff已经开始关注多体人-物交互的复杂同步。未来研究将进一步探索如何生成更自然的面部表情、手部细节及微小姿态变化，以实现真正令人信服的数字人。
2.  **更精细化与多模态控制：** 除了文本控制外，更多模态输入（如音频、图像、视频片段、情绪标签甚至生物传感数据）将与文本结合，实现更具表现力和情境感的动作生成。模型将允许用户对动作的风格、强度、节奏、空间位置以及与环境的交互进行更细粒度的控制，如 Multi-Track Timeline Control 实现了对时间线和身体部位的精确控制。
3.  **实时生成与部署优化：** 随着对实时交互和应用需求的增加，模型效率将成为重要考量。未来的工作将专注于提高生成速度，减少计算资源消耗，使文本驱动动作合成技术能够广泛应用于游戏、虚拟现实、电影预演制作等需要即时反馈的场景中。DAF-DH 和 BAMM 的工作已展现出在该方向的努力。

**挑战：**

1.  **数据稀缺与偏见：** 高质量、大规模、多样化且具有丰富语义标注的动作数据集仍然是瓶颈。现有数据集往往覆盖范围有限，并且可能存在特定动作模式或体格的偏见，影响模型泛化能力。
2.  **物理真实性与可解释性：** 生成动作的物理合理性（如平衡、碰撞避免、力反馈）和生物力学约束仍然难以完全保证。同时，深度学习模型通常是黑箱模型，其内部决策过程缺乏可解释性，导致在出现不自然动作时难以进行诊断和修复。
3.  **评估指标与人类感知对齐：** 尽管 MotionCritic 等工作试图弥合差距，但如何建立全面、鲁棒且与人类主观感知高度一致的自动化评估指标仍是一个开放性问题。

### 结论

文本驱动人体动作合成在近两年取得了显著进展，扩散模型、分层掩码建模以及自回归模型等方法不断刷新性能上限，实现了更高质量、更具细节和更可控的动作生成。从 MoMask 的高精度生成到 Multi-Track Timeline Control 的精细化控制，再到 DAF-DH 对效率的优化和 SyncDiff 对多体交互的突破，以及 MotionCritic 对评估范式的革新，该领域正稳步迈向生成更加逼真、多样、且能与人类感知对齐的数字人体动作。未来的研究将继续在动作复杂性、多模态控制、实时效率以及评估机制等方向发力，以期在更广泛的应用场景中发挥其巨大潜力。

### 参考文献

1.  Guo, C., Mu, Y., Javed, M. G., Wang, S., & Cheng, L. (2024). MoMask: Generative Masked Modeling of 3D Human Motions. *CVPR 2024*. [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/46930)
2.  Wang, J., Zhou, L., & Zhang, B. (2025). 基于扩散模型加速和感知优化的高效姿态驱动人体动作生成技术. *计算机应用研究*, 42(10). [arocmag.cn](https://www.arocmag.cn/abs/2025.03.0057)
3.  Xu, S., Ling, H. Y., Wang, Y.-X., & Gui, L.-Y. (2025). InterMimic: Towards Universal Whole-Body Control for Physics-Based Human-Object Interactions. [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/e0809fbb-23e4-49e4-9185-5487fde4edf6)
4.  Pinyoanuntapong, E., Saleem, M. U., Wang, P., Lee, M., Das, S., & Chen, C. (2024). BAMM: Bidirectional Autoregressive Motion Model. [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/9d28891c-494c-44d6-aafe-24aab09ab785)
5.  Wang, H., et al. (2025). MotionCritic: Aligning Human Motion Generation with Human Perceptions. *ICLR 2025*. [hub.baai.ac.cn](https://hub.baai.ac.cn/view/43445)
6.  Jiang, Y., Tong, S. Y., Koh, L., Wu, W., Loy, C. C., & Liu, Z. (2023). Text2Performer: Text-Driven Human Video Generation. [hub.baai.ac.cn](https://hub.baai.ac.cn/view/25619)
7.  Men, Y., Yao, Y., Cui, M., & Bo, L. (2024). MIMO: Controllable Character Video Synthesis with Spatial Decomposed Modeling. [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/61437)
8.  Tevet, G., Raab, S., Gordon, B., Shafir, Y., Cohen-or, D., & Bermano, A. H. (2023). Human Motion Diffusion Model. *ICLR 2023*. (引用自 MotionCritic 论文)
9.  Kim, J., Kim, J., & Choi, S. (2023). FLAME: Free-Form Language-Based Motion Synthesis & Editing. *AAAI 2023*. (引用自 MotionCritic 论文)
10. Guo, C., Zuo, X., Wang, S., Zou, S., Sun, Q., Deng, A., Gong, M., & Cheng, L. (2020). Action2Motion: Conditioned Generation of 3D Human Motions. *ACM Multimedia 2020*. (引用自 MotionCritic 论文)
11. Piao, Z., Huang, Y., Tang, Y., Wu, W., Liu, L., & Li, H. (2025). Multi-Track Timeline Control for Text-Driven 3D Human Motion Generation. [themoonlight.io](https://www.themoonlight.io/zh/review/multi-track-timeline-control-for-text-driven-3d-human-motion-generation)
12. Xu, S., et al. (2025). SyncDiff: Synchronized Motion Diffusion for Multi-Body Human-Object Interaction Synthesis. [themoonlight.io](https://www.themoonlight.io/zh/review/syncdiff-synchronized-motion-diffusion-for-multi-body-human-object-interaction-synthesis)