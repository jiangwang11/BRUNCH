## Visuomotor Policy Learning and Action Representation in Robotic Systems 学术综述 (2022-2025)

### 引言

具身智能 (Embodied AI) 旨在通过智能体与环境的持续交互来增强其能力，在学术界和工业界引起了广泛关注 [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/182383)。视觉-语言-动作 (Vision-Language-Action, VLA) 模型作为一种受大型基础模型启发的通用机器人控制框架，显著提升了具身智能系统中智能体与环境的交互能力，极大地拓展了其应用场景 [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/182383)。VLA 模型通过结合大模型技术，将视觉感知、语义推理与动作生成深度融合，使机器人能够直接从多模态输入中预测连续控制指令，实现从环境理解到物理执行的闭环耦合 [arxiv.org](https://arxiv.org/pdf/2508.15201)。

本综述将聚焦于 2022 年至 2025 年间，视觉运动策略学习 (Visuomotor Policy Learning) 和机器人系统中的动作表示 (Action Representation) 领域的前沿进展。特别地，我们将探讨基于扩散模型和强化学习的方法在提升机器人泛化能力和数据效率方面的代表性工作，并讨论双臂操作和人形机器人控制等新兴应用。

### 方法分类与代表作

#### 1. 基于扩散模型 (Diffusion Models) 的策略学习

扩散模型在生成式任务中展现出强大的分布建模能力，为机器人策略学习中的多模态动作分布建模提供了新思路。

*   **Diffusion Policy: Visuomotor Policy Learning via Action Diffusion (2023)**

    该工作提出了一种新颖的方法，通过将机器人波动运动策略表示为条件去噪扩散过程来生成机器人行为 [yiyibooks.cn](https://yiyibooks.cn/information/arxiv/2303.04137v5/)。研究人员对来自 4 个不同机器人操作基准的 12 个不同任务进行了基准测试，结果显示该方法全面超越了现有最先进的机器人学习方法，平均性能提高了 46.9% [yiyibooks.cn](https://yiyibooks.cn/information/arxiv/2303.04137v5/)。这一方法有效解决了传统确定性连续动作模型难以处理复杂行为多模态性的问题 [arxiv.org](https://arxiv.org/pdf/2508.15201)。

*   **RDT-1B: A Diffusion Foundation Model for Bimanual Manipulation (2025)**

    该工作提出了首个双臂操作的扩散基础模型 RDT-1B，其骨干网络采用改进的 Diffusion Transformer 以缓解多模态动作分布下的平均效应 [arxiv.org](https://arxiv.org/pdf/2508.15201)。该模型使用预训练的视觉编码器 SigLIP 并构建了包含 1M 条轨迹的数据集来支持骨干网络的从零训练 [arxiv.org](https://arxiv.org/pdf/2508.15201)。RDT-1B 在稀缺数据场景下能够生成多模态动作分布，显著提升了复杂协作操纵任务中的稳定性和成功率 [blog.csdn.net](https://blog.csdn.net/weixin_39653948/article/details/145402129)。

*   **3D Diffusion Policy: Generalizable Visuomotor Policy Learning via Simple 3D Representations (2024)**

    该研究将 3D 视觉表示融入扩散策略中，提出名为 DP3 的视觉模仿学习方法 [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/218b0ac1-fc3d-4759-9e39-e0c6c1e79f07)。DP3 利用从稀疏点云中提取的紧凑 3D 视觉表示，在 72 个模拟任务中仅需 10 个演示即可成功处理大多数任务，实现 24.2% 的相对改进 [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/218b0ac1-fc3d-4759-9e39-e0c6c1e79f07)。在真实机器人任务中，DP3 在空间、视角、外观和实例等方面展现出优秀的泛化能力，并很少违反安全要求 [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/218b0ac1-fc3d-4759-9e39-e0c6c1e79f07)。

#### 2. 基于强化学习 (Reinforcement Learning) 的策略微调

强化学习在弥合模型策略与人类偏好之间的差距、改进模型推理方面展现出巨大潜力，特别是在 VLA 模型的后训练阶段。

*   **SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning (2025)**

    该研究提出了 SimpleVLA-RL，一个专为 VLA 模型设计的高效强化学习框架，旨在解决监督微调所需人工操作机器人轨迹数据稀缺且成本高昂的问题，以及模型泛化能力有限的挑战 [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/a87490bb-bcfc-45a1-b076-adc9ed8b3dd7)。该框架基于 veRL，并引入了 VLA 特定的轨迹采样方法、可扩展的并行化处理、多环境渲染技术以及优化后的损失计算方式 [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/a87490bb-bcfc-45a1-b076-adc9ed8b3dd7)。SimpleVLA-RL 应用于 OpenVLA-OFT 模型后，在 LIBERO 任务集上取得了当前最先进的性能，并在 RoboTwin 1.0 和 2.0 平台上通过引入的增强探索策略表现优异 [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/a87490bb-bcfc-45a1-b076-adc9ed8b3dd7)。

*   **ConRFT: A Reinforced Fine-tuning Method for VLA Models via Consistency Policy (2025)**

    该工作提出了一种基于强化微调 (RFT) 的方法 ConRFT，用于在真实环境下高效微调 VLA 模型 [blog.csdn.net](https://blog.csdn.net/Yong_Qi2015/article/details/147343091)。ConRFT 包含离线和在线微调两个阶段，并采用统一的基于一致性策略的训练目标，旨在解决人类演示数据稀缺和策略不一致性导致监督微调性能不佳的问题 [blog.csdn.net](https://blog.csdn.net/Yong_Qi2015/article/details/147343091)。经过 45-90 分钟的在线微调，VLA 模型平均任务成功率达到 96.3%，显著优于基于人类收集数据或强化学习策略数据训练的 SFT 方法，平均成功率提高了 144% [blog.csdn.net](https://blog.csdn.net/Yong_Qi2015/article/details/147343091)。

*   **VLA-RL: Towards Masterful and General Robotic Manipulation with Scalable Reinforcement Learning (2025)**

    这项研究旨在通过可扩展的强化学习方法，实现机器人操作的精通和通用性，旨在解决将强化学习扩展到 VLA 模型所面临的挑战 [arxiv.org](https://arxiv.org/pdf/2508.15201)。VLA-RL 将 PPO 和 RPRM 结合进行微调，并利用并行仿真环境加速训练 [arxiv.org](https://arxiv.org/pdf/2508.15201)。该方法在仿真环境中实现了更快的收敛速度和更高的任务执行性能 [arxiv.org](https://arxiv.org/pdf/2508.15201)。

#### 3. 统一框架与通用策略

面对多样化的机器人任务和环境，开发统一的框架和通用策略成为 VLA 领域的重要趋势。

*   **RoboVLMs: Towards Generalist Robot Policies: What Matters in Building Vision-Language-Action Models (2024)**

    该研究旨在系统性理解 VLA 模型的关键设计选择，特别关注骨干网络、VLA 架构和跨机器人本体数据的应用时机 [blog.csdn.net](https://blog.csdn.net/weixin_39653948/article/details/145402129)。通过对 8 个 VLM 骨干网络、4 种策略架构和 600 多个不同设计实验的广泛研究，该工作开发了新的 VLA 系列 RoboVLMs，在三个模拟任务和现实世界实验中取得了新的最先进性能 [blog.csdn.net](https://blog.csdn.net/weixin_39653948/article/details/145402129)。实验结论强调了全面视觉-语言预训练的重要性，并指出连续动作和策略头集成历史上下文是构建高效 VLA 的关键 [blog.csdn.net](https://blog.csdn.net/weixin_39653948/article/details/145402129)。

*   **AnyBimanual: Transferring Unimanual Policy for General Bimanual Manipulation (2024)**

    针对双臂操作数据收集成本高昂的问题，该研究提出 AnyBimanual，一种即插即用方法，通过少量双臂演示将预训练的单手策略转移到一般双臂操作策略上 [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/88436)。该方法引入技能管理器动态调度从预训练单手策略中发现的技能表示，并提出视觉对齐器以减轻单手和双手系统之间的观察差异 [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/88436)。AnyBimanual 在 RLBench2 的 12 个模拟任务上成功率提高了 12.67%，并在 9 个真实世界任务中平均成功率为 84.62% [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/88436)。

*   **Vid2Robot: End-to-end Video-conditioned Policy Learning with Cross-Attention Transformers (2024)**

    该研究提出 Vid2Robot 视频学习框架，使得机器人能直接从观察人类行为中推断任务，而非依赖文本指令 [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/9c5d6525-4b29-40a1-8da2-cbf980be7ecc)。Vid2Robot 通过在大量人类视频和机器人轨迹数据集上训练统一的表示模型来实现这一目标，并利用交叉注意力机制融合提示视频特征与机器人当前状态 [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/9c5d6525-4b29-40a1-8da2-cbf980be7ecc)。在真实世界机器人上的评估显示，使用人类演示视频时，Vid2Robot 性能比其他视频条件策略提高了 20%，并展现出将观察到的运动从一个物体转移到另一个物体以及长时间跨度组合的新兴能力 [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/9c5d6525-4b29-40a1-8da2-cbf980be7ecc)。

#### 4. 人形机器人控制

人形机器人全身控制面临任务多样性和泛化能力的挑战，行为基础模型为通用人形机器人控制提供了新的方向。

*   **Behavior Foundation Model for Humanoid Robots (2025)**

    该研究提出了行为基础模型 (Behavior Foundation Model, BFM)，旨在为人形机器人捕捉广泛且可复用的行为知识，以解决现有全身控制 (WBC) 框架在技能多样性和泛化能力上的局限性 [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/c900b760-1a67-44ba-a0cf-a2131ef70078)。BFM 是一种在大规模行为数据集上预训练的生成式模型，结合了掩码在线蒸馏框架与条件变分自编码器 (CVAE) 来建模行为分布 [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/c900b760-1a67-44ba-a0cf-a2131ef70078)。在仿真环境和真实人形机器人平台上的大量实验表明，BFM 能够在多种全身控制任务中实现稳健的泛化能力，并快速适应新行为 [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/c900b760-1a67-44ba-a0cf-a2131ef70078)。

### 实验与评价总结

综观近期的研究，在视觉运动策略学习和动作表示方面，研究者们普遍关注以下共性结论：

1.  **数据效率的提升**：扩散模型和强化学习等方法在减少对大规模、高质量人工演示数据的依赖方面表现出显著优势。例如，3D Diffusion Policy (DP3) 仅需少量演示即可处理复杂任务，而 SimpleVLA-RL 通过强化学习有效减少了对大规模监督微调数据的需求。
2.  **泛化能力的增强**： VLA 模型结合大规模预训练的视觉语言模型，显著提升了在未见任务、未知环境和对象上的泛化能力。RoboVLMs 的研究强调了全面的视觉-语言预训练对于实现优越 VLA 性能的关键作用。
3.  **多模态性与连续动作的优势**：建模多模态动作分布对于机器人策略至关重要，扩散模型在此方面表现出色。同时，连续动作表示通常优于离散动作，尤其是在需要高精度和长周期任务中。RoboVLMs 的消融研究也证实了连续动作和历史上下文集成的优越性。
4.  **真实世界部署的潜力**：尽管仍面临 Sim2Real Gap，但诸多研究已在真实机器人上验证了方法的有效性。例如，DP3 在真实机器人上展现出良好的安全性和成功率；ConRFT 的在线微调方法在真实世界任务中显著提升了 VLA 模型的性能。Vid2Robot 在人类演示视频引导下，在真实机器人上取得了显著的性能提升。
5.  **对复杂任务和多机器人系统的支持**：研究开始拓展到双臂操作和全身控制等复杂场景。RDT-1B 专注于双臂操作的扩散模型，AnyBimanual 有效解决了双臂操作的数据稀缺问题。BFM 则为人形机器人的全身控制提供了通用行为基础模型。

### 趋势与挑战

2025 年前后，视觉运动策略学习和动作表示领域将呈现以下趋势和挑战：

1.  **通用基础模型的进一步发展与分层架构的普及**：VLA 模型将更倾向于从预训练的 LLM/VLM 继承权重，构建结构化的通用基础模型。为了处理长时域复杂任务和实时性要求，分层 VLA 架构将成为主流。上层策略（System 2, S2）利用 VLM 进行高级推理和任务分解，下层策略（System 1, S1）则专注于高频、精细的动作生成 [arxiv.org](https://arxiv.org/pdf/2508.15201)。挑战在于如何设计高效层间通信机制（如隐空间向量或动作轨迹），并确保端到端训练的有效性。
2.  **强化学习在后训练和在线学习中的关键作用**：鉴于监督微调在数据质量和一致性方面的局限，强化学习将在 VLA 模型的后训练和持续学习中发挥越来越重要的作用。研究将聚焦于解决真实世界中稀疏奖励、样本效率低和安全性保障等挑战。例如，通过在人机交互中引入人类反馈和专家干预来加速学习，或开发更稠密、更易于获取的奖励机制 [blog.csdn.net](https://blog.csdn.net/Yong_Qi2015/article/details/147343091)。
3.  **多模态融合与 3D 信息的深度利用**：VLA 模型将不再局限于 RGB 图像和文本，而是会更深度地融合触觉、力觉、深度信息、点云等多种传感器数据，以实现对物理世界更全面的理解和精细操作。目前已有一些工作探索 3D 视觉表示 [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/218b0ac1-fc3d-4759-9e39-e0c6c1e79f07)，未来会发展出更强大的 3D 空间感知能力和跨模态对齐技术，尤其是在精细操作和应对复杂物理交互方面 [arxiv.org](https://arxiv.org/pdf/2508.15201)。
4.  **高效推理与实时控制的突破**：随着 VLA 模型参数量的增加，如何在有限的机器人计算资源上实现高效推理和实时控制是一个关键挑战。研究将探索模型剪枝、量化、高效推理架构（如 Mamba 替代 Transformer）以及端云协同部署等技术，以平衡模型的泛化能力和实时性需求 [arxiv.org](https://arxiv.org/pdf/2508.15201)。

### 结论

近期的研究表明，视觉运动策略学习和动作表示在机器人系统中取得了显著进展，特别是在结合扩散模型和强化学习、构建通用 VLA 框架以及拓展至人形机器人控制等领域。尽管已取得了令人瞩目的成就，该领域仍面临诸多挑战，包括数据效率、泛化能力、实时性以及处理复杂物理交互的能力。未来的研究趋势将聚焦于发展更强大的通用基础模型、提升模型在真实世界中的在线学习和适应能力，并深度整合多模态和 3D 信息，以推动具身智能机器人更广泛的应用。

### 参考文献

1.  [yiyibooks.cn](https://yiyibooks.cn/information/arxiv/2303.04137v5/) Chi, C., Feng, S., Du, Y., et al. (2023). Diffusion Policy: Visuomotor Policy Learning via Action Diffusion. *Robotics: Science and Systems*.
2.  [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/a87490bb-bcfc-45a1-b076-adc9ed8b3dd7) Li, H., Zuo, Y., Yu, J., et al. (2025). SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning. *BAAI Tech Report*.
3.  [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/88436) Lu, G., Yu, T., Deng, H., et al. (2024). AnyBimanual: Transferring Unimanual Policy for General Bimanual Manipulation. *arXiv preprint arXiv:2412.06779*.
4.  [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/182383) Li, H., Chen, Y., Cui, W., et al. (2025). Survey of Vision-Language-Action Models for Embodied Manipulation. *arXiv preprint arXiv:2508.15201*.
5.  [arxiv.org](https://arxiv.org/pdf/2508.15201) Li, H., Chen, Y., Cui, W., et al. (2025). 面向具身操作的视觉-语言-动作模型综述. *ACTA AUTOMATICA SINICA*.
6.  [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/9c5d6525-4b29-40a1-8da2-cbf980be7ecc) Jain, V., Attarian, M., Joshi, N. J., et al. (2024). Vid2Robot: End-to-end Video-conditioned Policy Learning with Cross-Attention Transformers. *BAAI Tech Report*.
7.  [blog.csdn.net](https://blog.csdn.net/weixin_39653948/article/details/145402129) Li, X., Li, P., Liu, M., et al. (2024). RoboVLMs: Towards Generalist Robot Policies: What Matters in Building Vision-Language-Action Models. *arXiv preprint arXiv:2412.14058*.
8.  [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/218b0ac1-fc3d-4759-9e39-e0c6c1e79f07) Ze, Y., Zhang, G., Zhang, K., et al. (2024). 3D Diffusion Policy: Generalizable Visuomotor Policy Learning via Simple 3D Representations. *BAAI Tech Report*.
9.  [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/c900b760-1a67-44ba-a0cf-a2131ef70078) Zeng, W., Lu, S., Yin, K., et al. (2025). Behavior Foundation Model for Humanoid Robots. *BAAI Tech Report*.
10. [blog.csdn.net](https://blog.csdn.net/Yong_Qi2015/article/details/147343091) Chen, Y., Tian, S., Liu, S., et al. (2025). ConRFT: A Reinforced Fine-tuning Method for VLA Models via Consistency Policy. *Robotics: Science and Systems XXI*.
11. Liu, S., Wu, L., Li, B., et al. (2025). RDT-1B: A Diffusion Foundation Model for Bimanual Manipulation. *International Conference on Learning Representations*.
12. Lu, G., Guo, W., Zhang, C., et al. (2025). VLA-RL: Towards Masterful and General Robotic Manipulation with Scalable Reinforcement Learning. *arXiv preprint arXiv:2505.18719*.