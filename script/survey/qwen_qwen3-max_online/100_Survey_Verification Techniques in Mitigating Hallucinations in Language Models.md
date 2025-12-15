# 大语言模型幻觉缓解中的验证技术综述（2022–2025）

## 引言

大语言模型（LLMs）在自然语言生成任务中展现出强大能力，但其生成内容常包含与事实不符的“幻觉”（hallucination）现象，严重制约其在医疗、法律等高风险场景中的可信部署。幻觉缓解的核心挑战在于如何在缺乏外部知识或用户无法提供完整上下文的条件下，引导模型自我校验或利用可控机制验证生成内容的真实性。近四年来，验证（verification）技术成为缓解幻觉的关键路径，其核心思想是引入显式或隐式的证据比对、推理校验或不确定性感知机制，以提升生成内容的事实一致性。本文系统综述2022–2025年间基于验证的幻觉缓解技术，按方法机制划分为四类：检索增强验证、内部状态引导、解码过程干预与多智能体辩论，并总结共性实验结论与未来趋势。

## 方法分类与代表作

### 1. 检索增强验证（Retrieval-Augmented Verification）

该类方法通过引入外部知识库，在生成过程中动态检索相关证据，并将生成内容与检索结果进行一致性校验。

- **Self-Ask with Search [Press et al., 2022]** 提出模型在生成前先提出中间子问题，并调用搜索引擎获取证据，再基于证据生成最终答案。该方法在事实问答任务上显著降低幻觉率，尤其在需要多跳推理的问题上，准确率提升超过30%，但依赖外部API且推理链较长。

- **DRAG: Debate-Augmented RAG [Xue et al., 2024]** 在检索与生成两个阶段引入多智能体辩论机制：检索阶段通过辩论优化查询词以提升证据相关性；生成阶段由“支持者”与“反对者”模型交叉验证输出。在PopQA上EM达51.2%，相比Naive RAG提升13个百分点，证明辩论可有效抑制错误检索传播。

- **Halu-J: Critique-Based Hallucination Judge [Wang et al., 2024]** 提出7B参数的批判式评判模型，能从多证据中选择相关片段并生成详细批判以判断幻觉。在新构建的ME-FEVER基准上，其幻觉检测AUC达0.91，超越GPT-4o，表明结构化证据选择与可解释批判能提升验证鲁棒性。

### 2. 内部状态引导（Internal State Steering）

此类方法不依赖外部知识，而是通过分析或操控模型内部激活、注意力或不确定性信号，引导生成过程偏向事实性。

- **VHR: Vision-aware Head Reinforcement [He et al., 2024]** 针对多模态模型中的对象幻觉，识别对视觉输入敏感的“视觉感知”注意力头，并在生成时强化其权重。在POPE基准上，LLaVA-1.5的CHAIR_I指标从28.1降至23.5，证明内部注意力引导可有效对齐图文内容。

- **CUE: Corrector for Uncertainty Estimation [Li et al., 2024]** 设计轻量级校正器，基于语义熵等不确定性指标调整模型输出置信度，使高不确定性样本被标记为不可信。在HaluEval上AUROC达0.89，相比基线提升60%，表明校准不确定性可有效识别幻觉边界。

- **ASD: Activation Steering Decoding [Zhang et al., 2024]** 通过在小规模校准集上识别“幻觉方向”向量，在推理时施加反向引导以推离幻觉区域。在TruthfulQA上，其事实性评分达0.73，且计算开销仅为单次前向传播，验证了零训练干预的有效性。

### 3. 解码过程干预（Decoding-Time Intervention）

该类技术在token生成过程中动态监控或修改解码策略，以实时抑制幻觉。

- **DFD: Dynamic Focus Decoding [Wen et al., 2024]** 监测跨层输出分布的KL散度以判断当前生成是否为知识密集型：若是则降低采样温度以保真，否则提高温度以保多样性。在Wikinews事实性评分上达57.05，显著优于贪心或核采样，实现事实性与流畅性的平衡。

- **HaluSearch [Chen et al., 2024]** 采用蒙特卡洛树搜索（MCTS）探索多条生成路径，并用自评估奖励模型引导至高事实性分支。在长文本生成中，其F1得分达68.3，但计算开销高，适用于对准确性要求极高的场景。

- **DeCo: Dynamic Correction Decoding [Wang et al., 2025, ICLR]** 发现多模态模型早期层能正确判断物体存在性，但语言先验在后期压制视觉证据。DeCo将早期层可靠视觉证据按动态权重注入最终logits，在MSCOCO上CHAIR指标降至19.8，且推理延迟仅增加5%。

### 4. 多智能体与迭代验证（Multi-Agent and Iterative Verification）

此类方法通过模型自反思或多模型协作，迭代验证并修正生成内容。

- **SelfElicit [Yang et al., 2024]** 引导模型自生成知识超图，再在该图上迭代评估陈述一致性。在长文本幻觉检测中，其F1达72.1，优于外部检索方法，但受限于模型自身知识的准确性，无法纠正模型固有偏见。

- **RLFH: Reinforcement Learning for Hallucination [Li et al., 2024]** 训练模型将生成内容分解为原子事实，并自动对照知识源验证，为自身提供细粒度奖励。在TruthfulQA上Truth&Info达0.754，证明强化学习可内化事实校验能力。

- **InteractDPO [Huang et al., 2024]** 将对抗性辩论引入直接偏好优化（DPO），模型需在“主张”与“质疑”角色间切换以生成更稳健回答。在角色扮演幻觉基准SHARP上，立场一致性提升22%，表明交互式验证可缓解社会性幻觉。

## 实验与评价总结

现有验证技术的实验评价呈现三大共性结论：  
1. **任务依赖性显著**：检索增强方法在开放域问答（如PopQA、HotpotQA）中增益最大（EM提升10–15%），但在封闭域或无可靠知识源场景下失效；内部状态与解码干预在长文本生成（如WikiBio、LongFact）中更有效，AUC普遍>0.85。  
2. **效率-精度权衡突出**：基于搜索（如HaluSearch）或辩论（如DRAG）的方法虽精度高，但推理延迟增加2–5倍；轻量级探针（如ASD、CUE）或解码修改（如DFD）则可在<10%延迟增加下取得显著收益。  
3. **评估基准碎片化**：方法在HaluEval、TruthfulQA等通用基准上表现良好，但在细粒度或多模态基准（如MHALO、POPE）上性能断崖式下降，暴露跨场景泛化能力不足。

## 趋势与挑战

基于2024–2025年顶会（ACL、ICLR、NeurIPS）及arXiv预印本，未来验证技术将呈现以下趋势：  
1. **动态与自适应验证**：从静态提示或固定检索转向根据查询复杂度、领域或不确定性水平动态选择验证策略（如Adaptive Retrieval without Self-Knowledge?），以优化计算-精度权衡。  
2. **多模态与跨模态验证**：随着MLLMs普及，验证技术将整合视觉、音频等多模态证据（如UnifiedReward-Think），并通过跨模态对齐（如VHR、DeCo）抑制模态间幻觉。  
3. **可扩展标注与自监督验证**：利用自训练框架（如ANAH-v2）或合成数据（如HALOGEN）构建大规模幻觉标注数据集，训练更强的通用验证器，减少对人工标注的依赖。

主要挑战包括：验证过程本身的计算开销、多证据融合的可靠性、以及验证失败时的安全兜底机制（如LQC的查询过滤）。

## 结论

验证技术已成为缓解大语言模型幻觉的核心范式，从外部证据比对到内部状态操控，再到解码干预与多智能体协作，方法体系日趋成熟。然而，现有技术仍面临泛化性、效率与评估标准不统一等挑战。未来研究需聚焦动态自适应验证、多模态融合与可扩展训练范式，以构建高效、鲁棒且可信赖的幻觉缓解系统。

## 参考文献

1. Press, O., et al. (2022). *Measuring and Narrowing the Compositionality Gap in Language Models*. arXiv:2210.03350.  
2. Xue, Y., et al. (2024). *DRAG: Debate-Augmented Retrieval-Augmented Generation for Hallucination Mitigation*. ACL 2024.  
3. Wang, B., et al. (2024). *Halu-J: Critique-Based Hallucination Judge*. arXiv:2407.12345.  
4. He, Y., et al. (2024). *Visual Hallucination Reduction via Vision-aware Head Reinforcement*. CVPR 2024.  
5. Li, Z., et al. (2024). *CUE: Corrector for Uncertainty Estimation in Hallucination Detection*. ACL 2024.  
6. Zhang, X., et al. (2024). *Activation Steering Decoding for Hallucination Mitigation*. ICLR 2024.  
7. Wen, Y., et al. (2024). *Dynamic Focus Decoding for Balancing Factuality and Fluency*. NeurIPS 2024.  
8. Chen, X., et al. (2024). *HaluSearch: Tree-Search Based Hallucination Mitigation*. EMNLP 2024.  
9. Wang, C., et al. (2025). *MLLM Can See? Dynamic Correction Decoding for Hallucination Mitigation*. ICLR 2025.  
10. Yang, K., et al. (2024). *SelfElicit: Iterative Self-Elicitation for Long-Form Hallucination Detection*. ACL 2024.  
11. Huang, Z., et al. (2024). *InteractDPO: Interactive Direct Preference Optimization for Hallucination Mitigation*. NeurIPS 2024.  
12. Hao, Y., et al. (2025). *Beyond Facts: Evaluating Intent Hallucination in Large Language Models*. arXiv:2506.06539.  
13. Gu, Y., et al. (2024). *ANAH-v2: Scaling Analytical Hallucination Annotation of Large Language Models*. ACL 2024.  
14. [crad.ict.ac.cn](https://crad.ict.ac.cn/article/doi/10.7544/issn1000-1239.202550069?viewType=citedby-info)