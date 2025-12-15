# 人体运动预测算法与技术综述（2022–2025）

## 引言

人体运动预测（Human Motion Prediction）旨在基于观测到的短时人体姿态序列，推断未来若干帧的关节运动轨迹，是人机交互、虚拟现实、自动驾驶等智能系统的基础模块。2022–2025年间，该领域在生成建模范式、感知对齐机制、物理约束引入以及计算效率优化方面取得显著突破。早期以循环神经网络和图卷积为主的方法逐渐被基于Transformer、扩散模型和掩码建模的生成式架构所超越。本文系统梳理近三年代表性工作，按方法范式分类评述其技术路径、评估结果与核心贡献，并基于最新研究动态预测未来趋势。

## 方法分类与代表作

### 1. 扩散模型与生成式预测

扩散模型因其对复杂多模态分布的建模能力，在运动生成中迅速普及。Zhou 等[1]提出一种基于扩散模型的三维人体姿态估计方法，将姿态预测建模为从噪声逐步去噪的逆过程，显著提升模型对输入噪声（如遮挡、低光照）的鲁棒性，在 Human3.6M 数据集上验证了其预测精度优于传统确定性回归方法。

Wang 等[2]针对数字人视频生成中扩散模型推理延迟高的问题，提出了 DAF-DH 框架。该方法结合 TensorRT 加速、低分辨率抽帧生成与后处理超分/插帧模块，实现 5 倍推理加速，同时通过语义特征对齐损失优化主观感知质量，LPIPS 降低 0.033，FVD 减少 82.9，验证了效率与质量可协同提升。

### 2. 掩码建模与离散表示

Guo 等[3]提出的 MoMask 是文本驱动 3D 动作生成的代表性工作。其采用分层量化将连续动作编码为多层离散令牌（基础层 + 残差层），并设计双 Transformer 架构：掩码 Transformer 从空序列迭代填充基础动作令牌（文本条件），残差 Transformer 逐层细化细节。在 HumanML3D 上 FID 降至 0.045（对比 T2M-GPT 的 0.141），且无需微调即可用于时间修补等下游任务。

### 3. 感知对齐与评估驱动优化

评估指标与人类感知的脱节长期制约生成质量提升。Wang 等[4]（ICLR 2025）构建大规模人类感知评估数据集 MotionPercept（含 52590 组动作对），并训练 MotionCritic 模型作为可学习的评估器。实验表明 MotionCritic 评分与人类用户研究（Elo 评分）高度一致，且作为微调监督信号，仅数百步即可显著提升生成动作的自然性与流畅性。

### 4. 骨架行为识别中的时空建模（与预测任务紧密相关）

尽管属于识别范畴，但其时空建模范式深刻影响预测任务。Liang 等[5]提出融合运动学知识的自适应时空 Transformer，设计多时间分支结构捕捉短时子动作，并通过多尺度时间卷积建模长时依赖。在 NTU RGB+D、FineGym 和工业数据集 InHARD 上均超越基准 Transformer，验证了领域知识对时序建模的有效性。

Meng 等[6]系统综述了骨架动作识别四大技术路线（RNN、CNN、GCN、Transformer），指出空间建模（关节关系）与时间建模（动态演化）是两大核心，并强调构建丰富表征（如速度、加速度、轨迹）对性能提升的关键作用——这一结论同样适用于预测任务。

## 实验与评价总结

近年工作普遍在 Human3.6M、HumanML3D、KIT-ML 等标准数据集上评估。共性结论包括：(1) 生成式方法（扩散、掩码建模）在 FID、MM-Dist 等分布指标上显著优于确定性模型，但推理速度仍是瓶颈；(2) 引入人类感知评估（如 MotionCritic）或物理约束可有效缓解“运动模糊”与“生物力学不合理”问题；(3) 多尺度时序建模（短时细节 + 长时语义）是提升预测长期一致性的关键；(4) 离散表示（如 MoMask 的分层令牌）在保留高频运动细节方面具有优势，但量化损失需谨慎处理。

## 趋势与挑战

基于 2025 年初的研究动态，可预测以下趋势：

1. **感知-物理联合约束成为新范式**：仅依赖数据驱动难以保证长期物理合理性。GIC 等工作[7]将物理模拟（如 MPM）与神经表示（Gaussian Splatting）结合，预示运动生成将融合可微物理引擎以确保动力学一致性。
2. **评估体系向人类中心迁移**：MotionCritic 等工作标志着自动化评估从“逼近真值”转向“对齐人类感知”。未来评估指标将更注重可解释性与主观质量，甚至成为训练信号的一部分。
3. **效率-质量-泛化三角平衡**：DAF-DH 等加速框架表明，面向实时应用（如数字人直播）的轻量化生成模型是迫切需求。未来研究将聚焦于模型压缩、蒸馏与硬件协同设计，以降低部署门槛。

主要挑战包括：(1) 长期预测中的动作语义漂移；(2) 小样本/零样本场景下的泛化能力；(3) 多人交互运动的联合建模与冲突消解。

## 结论

2022–2025 年，人体运动预测技术从确定性回归走向基于扩散、掩码建模等生成式范式，并逐步引入人类感知对齐与物理约束机制。代表性工作在生成质量、评估合理性与计算效率方面取得实质性进展。未来研究将更强调物理真实性、人类主观体验与实际部署可行性之间的协同优化，推动该技术从实验室走向规模化应用。

## 参考文献

[1] Zhou S, Zhang M. A 3D Human Pose Estimation Method Based On Diffusion Model. *Sciencepaper Online*. 2025. [paper.edu.cn](https://paper.edu.cn/releasepaper/content/202504-223)

[2] Wang J, Zhou L, Zhang B. Efficient pose-driven human motion generation with diffusion model acceleration and perceptual optimization. *Application Research of Computers*. 2025;42(10). [arocmag.cn](https://www.arocmag.cn/abs/2025.03.0057)

[3] Guo C, Mu Y, Javed M G, et al. MoMask: Generative Masked Modeling of 3D Human Motions. *CVPR*. 2024. [openaccess.thecvf.com](https://openaccess.thecvf.com/content/CVPR2024/html/Guo_MoMask_Generative_Masked_Modeling_of_3D_Human_Motions_CVPR_2024_paper.html)

[4] Wang H, et al. Aligning Human Motion Generation with Human Perceptions. *ICLR*. 2025. [motioncritic.github.io](https://motioncritic.github.io/)

[5] Liang C, Yang J, Jiang S, et al. Fusion of Motion Domain Knowledge and Adaptive Spatio-Temporal Transformer for Skeleton-based Human Action Recognition. *Journal of Computer Research and Development*. 2025. [crad.ict.ac.cn](https://crad.ict.ac.cn/article/doi/10.7544/issn1000-1239.202440558)

[6] Meng X, Li S, Yuan M, et al. Action Recognition Based on Human Skeleton: Review and Prospect. *Acta Automatica Sinica*. 2025. [xk.sia.cn](https://xk.sia.cn/cn/article/id/f0728f3d-3f0c-43cc-a121-5f1cef09ee7b)

[7] Cai J, Yang Y, Yuan W, et al. GIC: Gaussian-Informed Continuum for Physical Property Identification and Simulation. *arXiv preprint arXiv:2406.14927*. 2024.

[8] Liu T, Weng C, Wang B, et al. Human-centric Smart Manufacturing: Analysis and Prospects of Human Activity Recognition. *Journal of Mechanical Engineering*. 2025;61(15):57–81. [qikan.cmes.org](https://qikan.cmes.org/jxgcxb/CN/10.3901/JME.2025.15.057)

[9] Tevet G, Raab S, Gordon B, et al. Human Motion Diffusion Model. *ICLR*. 2023.

[10] Guo C, Zuo X, Wang S, et al. Action2motion: Conditioned generation of 3d human motions. *ACM Multimedia*. 2020.

[11] Kim J, Kim J, Choi S. FLAME: Free-form language-based motion synthesis & editing. *AAAI*. 2023.

[12] Zhu W, Ma X, Liu Z, et al. Learning human motion representations: A unified perspective. *ICCV*. 2023.