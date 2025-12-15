# 基于深度学习的文本驱动人体动作合成研究综述（2022–2025）

## 引言

文本驱动人体动作合成（Text-Driven Human Motion Synthesis）旨在将自然语言描述转化为时空连续、语义一致且物理合理的3D人体动作序列。该任务横跨自然语言处理、计算机视觉与生成式人工智能，近年来因扩散模型（Diffusion Models）、掩码建模（Masked Modeling）等生成范式的突破而取得显著进展。早期方法多基于自回归或变分自编码器结构，难以兼顾动作多样性、语义对齐与长期时序一致性。自2022年起，以Motion Diffusion Model（MDM）为代表的扩散方法成为主流，并在2023–2025年间衍生出物理约束、多轨控制、感知对齐等方向。本文系统梳理2022至2025年间该领域的代表性工作，按方法范式分类评述其技术路径与局限，并总结实验评价共识，最后展望未来研究趋势。

## 方法分类与代表作

### 1. 扩散模型（Diffusion Models）

扩散模型通过迭代去噪过程生成高维动作序列，在多样性与质量上显著优于确定性方法。  
**MotionDiffuse**（Zhang et al., TPAMI 2024）[csdn.net](https://blog.csdn.net/qq_42722197/article/details/140107485) 是最早将扩散机制引入文本到动作生成的工作之一。其采用关节位置序列表示动作，通过文本条件引导的去噪过程生成任意长度序列，并支持对身体部位的细粒度指令。实验表明其在HumanML3D上FID为0.105，优于同期自回归模型，且能响应时变文本提示实现多阶段动作合成。  

**PhysDiff**（Yuan et al., arXiv 2022）[zhuanzhi.ai](https://zhuanzhi.ai/paper/ae828b2ad699bb2825909389960b12a4) 针对扩散模型常产生“脚滑”“漂浮”等物理不合理动作的问题，提出物理引导机制。其在每步去噪后引入基于仿真的运动投影模块（motion projection），将预测动作映射至物理可行空间，并将投影结果反馈至下一去噪步骤。在AMASS数据集上，该方法将物理合理性指标提升78%以上，同时保持生成多样性。  

**DAF-DH**（王家松等，《计算机应用研究》2025）[arocmag.cn](https://www.arocmag.cn/abs/2025.03.0057) 聚焦扩散模型推理效率低的问题，提出三级加速框架：先通过TensorRT优化扩散模型，再以低分辨率/帧率生成初始视频，最后用轻量超分与插帧模块提升质量。在MimicMotion基础上实现5倍加速，LPIPS降低0.033，FVD减少82.9，适用于实时数字人应用。

### 2. 掩码建模与离散表示（Masked Modeling & Discrete Tokens）

该类方法将动作量化为离散令牌，利用掩码语言建模范式进行生成，强调语义结构建模。  
**MoMask**（Guo et al., CVPR 2024）[chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/46930) 提出分层量化方案：基础层通过向量量化获得动作主干令牌，高层存储残差细节令牌。训练时使用掩码变换器预测被掩令牌（条件为文本）；推理时从空序列迭代填充，再由残差变换器逐层细化。在HumanML3D上FID达0.045（T2M-GPT为0.141），且无需微调即可支持文本引导的时间修补（temporal inpainting）。

### 3. 多轨控制与时空拼贴（Multi-Track & Spatio-Temporal Composition）

为实现复杂动作的组合与精确时序控制，近期工作引入多轨接口与测试时拼贴策略。  
**Multi-Track Timeline Control**（arXiv 2024）[themoonlight.io](https://www.themoonlight.io/zh/review/multi-track-timeline-control-for-text-driven-3d-human-motion-generation) 允许用户在多轨时间线上指定重叠或顺序的文本提示。其提出**Spatio-Temporal Motion Collage (STMC)** 方法：先通过LLM将提示标注至身体部位，再在扩散去噪每一步中对各时间段独立去噪，并按身体部位拼接结果。实验显示STMC能忠实地合成“左手挥手+右脚踏步”等复合动作，优于基线MDM。

### 4. 人类感知对齐（Human Perception Alignment）

传统指标（如FID）与人类主观评价存在偏差，新工作致力于构建感知一致的评估与优化机制。  
**MotionCritic**（ICLR 2025）[hub.baai.ac.cn](https://hub.baai.ac.cn/view/43445) 构建大规模动作对偏好数据集MotionPercept（含52,590组人工标注），训练DSTFormer结构的评价模型。该模型不仅能作为评估指标（与User Study的Spearman相关性达0.89），还可作为监督信号微调生成器。实验表明，仅数百步微调即可显著提升生成动作的自然性与流畅性，且无需修改生成架构。

### 5. 人-物交互与物理仿真（Human-Object Interaction）

复杂交互需建模手-物接触与动力学约束。  
**InterMimic**（Xu et al., arXiv 2025）[hub.baai.ac.cn](https://hub.baai.ac.cn/paper/e0809fbb-23e4-49e4-9185-5487fde4edf6) 提出“先完善再扩展”的蒸馏框架：先用教师策略优化含噪声的MoCap交互数据，再将知识蒸馏至单一学生策略，并结合强化学习微调以超越模仿。该方法在Grasp-It!和Bimanual Actions数据集上实现逼真交互，且能零样本泛化至新物体。  
**SyncDiff**（arXiv 2024）[themoonlight.io](https://www.themoonlight.io/zh/review/syncdiff-synchronized-motion-diffusion-for-multi-body-human-object-interaction-synthesis) 将人-手-物运动视为联合高维序列，设计对齐分数（alignment scores）与损失函数，约束交互部位的运动同步性。其在推理中引入显式同步策略，显著减少穿插与失配，提升多体协调性。

## 实验与评价总结

2022–2025年间的实验评价呈现以下共性结论：  
1. **指标局限性被广泛认知**：FID、MM-Dist等分布距离指标与人类主观质量相关性弱（MotionCritic指出Spearman相关性常低于0.5），促使社区转向User Study与感知模型。  
2. **数据集集中于HumanML3D与KIT-ML**：绝大多数工作在HumanML3D（文本-动作对）上报告FID，但对其动作复杂度（多为行走、挥手等简单动作）的批评日益增多，推动新数据集如MotionPercept、DH-Motion的构建。  
3. **物理合理性成为新焦点**：自PhysDiff起，脚滑、穿透等物理错误被量化评估（如Foot Skating Distance、Penetration Volume），并作为核心指标。  
4. **实时性需求催生效率研究**：DAF-DH等表明，5倍以上加速可在轻微质量损失下实现，为工业部署铺路。  
5. **零样本泛化能力受重视**：InterMimic、SyncDiff等强调在未见物体或动作组合上的泛化，反映对真实场景鲁棒性的追求。

## 趋势与挑战

基于2025年前后进展，可预测以下趋势：  
1. **多模态条件融合成为标配**：未来系统将同时支持文本、语音、图像甚至场景上下文作为输入（如T3M从语音生成动作），需解决跨模态对齐与冲突消解问题。  
2. **具身智能驱动闭环生成**：动作生成将与物理仿真、任务规划结合，形成“生成-执行-反馈”闭环（如InterMimic的RL微调），以支持机器人等真实交互场景。  
3. **评估体系向人类感知对齐**：MotionCritic类感知评价模型将逐步替代传统指标，甚至成为生成训练的内嵌组件，推动“生成即优化”范式。  
主要挑战仍存：长时序动作的全局一致性（>10秒）、细粒度语义控制（如“略带犹豫地转身”）、以及高质量人-物交互数据的稀缺性。

## 结论

2022–2025年，文本驱动人体动作合成在生成范式（扩散/掩码）、控制粒度（多轨/部位级）、物理合理性和感知对齐等方面取得突破。扩散模型主导了高质量生成，而掩码建模在结构化控制上具优势；物理约束与感知评价正从“后处理”走向“内生设计”。未来工作需在多模态融合、闭环具身智能和评估标准化上深化，以迈向真实世界应用。

## 参考文献

1. Zhang, M., et al. MotionDiffuse: Text-Driven Human Motion Generation with Diffusion Model. *IEEE TPAMI*, 2024. [csdn.net](https://blog.csdn.net/qq_42722197/article/details/140107485)  
2. Yuan, Y., et al. PhysDiff: Physics-Guided Human Motion Diffusion Model. *arXiv:2212.02500*, 2022. [zhuanzhi.ai](https://zhuanzhi.ai/paper/ae828b2ad699bb2825909389960b12a4)  
3. Guo, C., et al. MoMask: Generative Masked Modeling of 3D Human Motions. *CVPR*, 2024. [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/46930)  
4. Wang, J., et al. Efficient pose-driven human motion generation with diffusion model acceleration and perceptual optimization. *Application Research of Computers*, 42(10), 2025. [arocmag.cn](https://www.arocmag.cn/abs/2025.03.0057)  
5. Multi-Track Timeline Control for Text-Driven 3D Human Motion Generation. *arXiv:2401.08559*, 2024. [themoonlight.io](https://www.themoonlight.io/zh/review/multi-track-timeline-control-for-text-driven-3d-human-motion-generation)  
6. MotionCritic: Aligning Human Motion Generation with Human Perceptions. *ICLR*, 2025. [hub.baai.ac.cn](https://hub.baai.ac.cn/view/43445)  
7. Xu, S., et al. InterMimic: Towards Universal Whole-Body Control for Physics-Based Human-Object Interactions. *arXiv:2502.16342*, 2025. [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/e0809fbb-23e4-49e4-9185-5487fde4edf6)  
8. SyncDiff: Synchronized Motion Diffusion for Multi-Body Human-Object Interaction Synthesis. *arXiv:2412.20104*, 2024. [themoonlight.io](https://www.themoonlight.io/zh/review/syncdiff-synchronized-motion-diffusion-for-multi-body-human-object-interaction-synthesis)  
9. Tevet, G., et al. Human Motion Diffusion Model. *ICLR*, 2023.  
10. Jiang, Y., et al. Text2Performer: Text-Driven Human Video Generation. *arXiv:2303.11318*, 2023. [hub.baai.ac.cn](https://hub.baai.ac.cn/view/25619)  
11. Kim, J., et al. FLAME: Free-form Language-based Motion Synthesis & Editing. *AAAI*, 2023.  
12. Guo, C., et al. Action2Motion: Conditioned Generation of 3D Human Motions. *ACM Multimedia*, 2020.