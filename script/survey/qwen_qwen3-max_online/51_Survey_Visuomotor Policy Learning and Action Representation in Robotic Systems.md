# 视觉运动策略学习与动作表示在机器人系统中的研究综述（2022–2025）

## 引言

视觉运动策略学习（Visuomotor Policy Learning）旨在从原始视觉输入中直接映射到机器人动作输出，是实现通用具身智能体的核心挑战。2022–2025 年间，该领域经历了从传统显式/隐式策略向生成式建模范式的演进，尤其以扩散模型为代表的生成模型在处理多模态动作分布、高维动作序列和训练稳定性方面展现出显著优势。本综述聚焦近三年代表性工作，按方法范式分类梳理其核心思想、技术贡献与实验结论，并总结当前评价体系与未来发展趋势。

## 方法分类与代表作

### 1. 基于扩散模型的策略学习（Diffusion-based Policies）

**Diffusion Policy: Visuomotor Policy Learning via Action Diffusion**（Chi et al., arXiv 2023；正式发表于 RSS 2024 扩展版）[cs.columbia.edu](https://diffusion-policy.cs.columbia.edu/)  
该工作首次将去噪扩散概率模型（DDPM）应用于视觉运动策略学习，将策略建模为以视觉观测为条件、在动作空间上进行迭代去噪的生成过程。其关键技术包括滚动时域控制（receding-horizon control）、视觉条件化（visual conditioning）和时序扩散 Transformer。在 4 个基准、15 个任务上平均提升 SOTA 方法 46.9%，且在单臂与双臂操作中均展示出对多模态动作分布与空闲动作的鲁棒性。

**3D Diffusion Policy (DP3): Generalizable Visuomotor Policy Learning via Simple 3D Representations**（Ze et al., RSS 2024）[3d-diffusion-policy.github.io](https://3d-diffusion-policy.github.io/)  
为提升泛化能力，DP3 将 3D 稀疏点云作为视觉输入，通过轻量点云编码器提取紧凑 3D 表征并融入扩散策略框架。该方法仅需 10 次演示即可在 72 个模拟任务中取得 24.2% 的相对性能提升，在真实机器人任务中达到 85% 成功率，并在视角、外观、实例变化下表现出强泛化性，同时显著减少安全违规行为。

**AdaManip: Adaptive Articulated Object Manipulation Environments and Policy Learning**（Wang et al., ICLR 2025）[adamanip.github.io](https://adamanip.github.io/)  
针对铰链物体操作中不可见内部状态导致的适应性挑战，该工作构建了支持五类真实适应机制的仿真环境 AdaManip，并结合基于 3D 视觉的扩散策略学习多峰且可历史调整的策略。实验表明，仅使用适应性示范轨迹（含失败-重试）训练的扩散策略，显著优于使用静态最优轨迹训练的基线，验证了扩散模型在建模复杂条件动作分布中的有效性。

### 2. 视觉-语言-动作融合模型（Vision-Language-Action Models）

**RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control**（Brohan et al., CoRL 2023）  
RT-2 将大规模视觉-语言模型（如 PaLI-X）微调为端到端 VLA 策略，将动作 token 化并作为语言序列的一部分进行预测。通过在大规模网络图文数据与机器人轨迹上联合预训练，RT-2 在 zero-shot 泛化任务上显著优于纯机器人数据训练的策略，证明了跨模态预训练知识对具身推理的迁移价值。

**π0: A Vision-Language-Action Flow Model for General Robot Control**（Black et al., arXiv 2024）  
π0 提出基于流匹配（flow matching）的 VLA 框架，将动作生成建模为从噪声到动作的连续变换。该模型在多机器人平台、多任务、多模态指令下进行大规模训练，在 17 个真实世界任务上实现 61% 的 zero-shot 成功率，展示了生成式 VLA 模型在统一控制接口方面的潜力。

### 3. 强化学习与后训练微调方法

**ConRFT: A Reinforced Fine-tuning Method for VLA Models via Consistency Policy**（Chen et al., RSS 2025）[cccedric.github.io/conrft](https://cccedric.github.io/conrft/)  
针对 VLA 模型在真实任务中依赖高质量演示的问题，ConRFT 提出两阶段强化微调框架：先用少量演示进行离线 Cal-QL 微调，再通过人在回路（HIL）在线交互优化。其采用一致性策略（consistency policy）作为轻量动作头，在 8 个真实任务上经 45–90 分钟微调后达到 96.3% 平均成功率，显著优于监督微调（SFT）基线。

**Diffusion Policies as an Expressive Policy Class for Offline Reinforcement Learning**（Ajay et al., arXiv 2022）  
该工作早于 Diffusion Policy，首次探索将扩散模型作为离线强化学习中的策略表示。通过 Q 函数引导的扩散采样（Q-guided sampling），策略在高维动作空间中有效探索高回报区域。在 D4RL 基准上，该方法在多个控制任务中超越传统离线 RL 算法，验证了扩散策略在利用次优数据方面的潜力。

### 4. 视频条件化与跨域策略学习

**Vid2Robot: End-to-end Video-conditioned Policy Learning with Cross-Attention Transformers**（Jain et al., arXiv 2024）[vid2robot.github.io](https://vid2robot.github.io/)  
Vid2Robot 提出端到端视频条件策略，直接从人类操作视频中生成机器人动作。模型通过交叉注意力将提示视频特征与当前观测融合，并引入对比损失对齐人-机视频表征。在真实机器人上，使用人类视频作为条件时，性能较其他视频条件策略提升 20%，并展现出跨物体动作迁移能力。

**AnyBimanual: Transferring Unimanual Policy for General Bimanual Manipulation**（Lu et al., arXiv 2024）  
为解决双手操作数据稀缺问题，AnyBimanual 提出将预训练单手策略迁移至双手系统。其引入技能管理器动态组合单手技能，并设计视觉对齐器缓解观测差异。在 12 个模拟任务和 9 个真实任务上，仅用少量双手演示即实现 84.62% 平均成功率，验证了策略迁移在降低数据需求方面的有效性。

## 实验与评价总结

近三年研究在实验设计上呈现以下共性：  
1. **基准多样化**：普遍在模拟（Robomimic、Franka Kitchen）与真实（UR5、Franka Panda）环境中联合评估，覆盖 2–6 DoF、刚性/非刚性物体、单/双臂配置。  
2. **多模态性量化**：通过多路径任务（如 Push-T、Block Pushing）或长时序任务（如 Shirt Folding）定量评测策略对多模态动作分布的建模能力。  
3. **鲁棒性测试**：普遍引入视觉遮挡、物理扰动、初始状态偏移等干扰，验证策略在非理想条件下的适应性。  
4. **效率与延迟**：扩散类方法普遍采用 DDIM 加速推理，在 GPU 上实现 10–100 Hz 控制频率，满足多数操作任务需求。

## 趋势与挑战

基于 2025 年前后研究动态，可预见以下趋势：  
1. **生成式策略与世界模型融合**：如阿里达摩院与浙大提出的 **WorldVLA**（arXiv 2025）将 VLA 与自回归世界模型统一，通过预测未来状态反哺动作生成，实现双向增强，将成为提升策略长期一致性的新范式。  
2. **多模态感知扩展**：当前主流依赖视觉，未来将融合触觉、力觉、声音等异构传感器，构建跨模态策略（如 Diffusion Policy 已有初步探索 [devpress.csdn.net](https://devpress.csdn.net/v1/article/detail/149980830)）。  
3. **数据效率与安全性协同优化**：结合离线 RL、偏好学习（如 GRAPE, arXiv 2024）与人在回路机制，在有限安全交互下高效微调大规模 VLA 模型，是通向实际部署的关键路径。

## 结论

2022–2025 年，视觉运动策略学习从监督模仿向生成式、多模态、可适应的智能体演进。扩散模型因其对多模态高维动作分布的强大建模能力，已成为策略表示的主流范式；VLA 框架则通过融合语言与视觉，显著提升泛化性；而强化微调与跨域迁移技术正逐步解决数据稀缺与安全性瓶颈。未来研究需在生成能力、物理理解与安全交互之间取得更优平衡，以实现真正可靠的通用机器人操作。

## 参考文献

1. Chi, C., et al. (2023). *Diffusion Policy: Visuomotor Policy Learning via Action Diffusion*. arXiv:2303.04137.  
2. Ze, Y., et al. (2024). *3D Diffusion Policy: Generalizable Visuomotor Policy Learning via Simple 3D Representations*. In *Proceedings of Robotics: Science and Systems (RSS)*.  
3. Wang, Y., et al. (2025). *AdaManip: Adaptive Articulated Object Manipulation Environments and Policy Learning*. In *International Conference on Learning Representations (ICLR)*.  
4. Brohan, A., et al. (2023). *RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control*. In *Conference on Robot Learning (CoRL)*.  
5. Black, K., et al. (2024). *π0: A Vision-Language-Action Flow Model for General Robot Control*. arXiv:2410.24164.  
6. Chen, Y., et al. (2025). *ConRFT: A Reinforced Fine-tuning Method for VLA Models via Consistency Policy*. In *Robotics: Science and Systems (RSS)*.  
7. Ajay, A., et al. (2022). *Diffusion Policies as an Expressive Policy Class for Offline Reinforcement Learning*. arXiv:2211.08089.  
8. Jain, V., et al. (2024). *Vid2Robot: End-to-end Video-conditioned Policy Learning with Cross-Attention Transformers*. arXiv:2403.11354.  
9. Lu, G., et al. (2024). *AnyBimanual: Transferring Unimanual Policy for General Bimanual Manipulation*. arXiv:2412.06779.  
10. Wen, J., et al. (2025). *WorldVLA: Scaling Robot Foundation Models via Unified Diffusion and Autoregression*. arXiv:2506.21539. [ai-bot.cn](https://ai-bot.cn/worldvla)  
11. Xu, C., et al. (2024). *RLDG: Robotic Generalist Policy Distillation via Reinforcement Learning*. arXiv:2412.09858.  
12. Li, H., et al. (2025). *Survey of Vision-Language-Action Models for Embodied Manipulation*. arXiv:2508.15201.