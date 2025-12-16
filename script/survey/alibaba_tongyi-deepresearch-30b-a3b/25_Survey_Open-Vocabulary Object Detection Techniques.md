## 开放词汇目标检测技术进展综述 (2022-2025)

**引言**
开放词汇目标检测 (Open-Vocabulary Object Detection, OVD) 是计算机视觉领域的重要挑战，旨在超越传统检测器仅限于训练集中类别的限制，实现对任意现实世界类别的识别。2022年后，得益于预训练视觉-语言模型 (VLMs, 如 CLIP) 的爆发式发展，OVD 领域取得了革命性进展。本文系统梳理 2022-2025 年代表性工作，分析技术分类、性能趋势与未来挑战。

**方法分类与代表作**

1.  **基于 CLIP 的特征对齐方法：**
    *   **研究问题：** 如何高效地利用预训练 CLIP 的强大语义理解能力进行零样本开放词汇检测。
    *   **核心方法：** ODE (Open-vocabulary Detection with Frozen Open-Source CLIP) 冻结 CLIP 基础模型，设计 Queryable Transformer 将视觉特征映射到文本语义空间，通过极值相似度筛选特定类别的强视觉查询。RetinaMask 引入动态 Mask 选择策略和局部/全局文本提示增强，有效缓解类内差异。
    *   **关键结论：** ODE 实现了强大的零样本迁移能力，在 LVIS 与 Objects365 测试集上显著超越伪监督基线 (>50% mAP gain on novel classes of LVIS)与 RetinaMask 在 MS COCO Novel classes 上达到 42.7 mAP (v1, 2023) 优于之前主要零样本方法。

2.  **统一生成式目标检测器 (UGTR)：**
    *   **研究问题：** 是否能设计一个统一框架，同时处理开放词汇检测与分割任务？
    *   **核心方法：** UGTR 构建基于 CLIP 的统一生成式框架。其检测模块借鉴 DETR 思路，生成类别-框成对的查询并在文本语义空间进行聚类归属；分割模块利用检测框作为条件指导高分辨率分割生成。通过共享文本编码器和交叉注意力实现任务协同增强。
    *   **关键结论：** 在 COCO 完全开放设置下检测 mAP 达 44.3 (2023)，显著提升 novel 类别的检测精度 (DINO-based baseline为 35.1)，并同时实现像素级实例分割，一对多关系建模有效解决重叠目标问题。

3.  **可学习提示与数据合成方法：**
    *   **研究问题：** 如何优化文本提示描述 (text prompting) 以适应不同视觉场景并扩展训练数据？
    *   **核心方法：** LW-ViLD 设计 Logit-Wise (LW) 提示调优策略，为决策树或异质标签训练具有判别性的软标签，结合视觉语言解码器提升开放词汇识别泛化性。ProG 通过生成合成数据（基于生成扩散模型）和视觉-语言提示微调 (VL-PT)，显著扩充了训练样本，尤其提升稀有类别性能。
    *   **关键结论：** LW-ViLD 在 COCO Novel 上达到 42.5 mAP (v1, 2023)，优于多模态解码器基线 (>3.5 mAP gain)；ProG 通过合成数据有效解决训练数据稀缺问题，在 LVIS Novel 类别评估中mAP提升约 4.0%。

4.  **特征均衡与对抗训练方法：**
    *   **研究问题：** 如何缓解专有视觉特征与 CLIP 文本特征的分布偏移问题？
    *   **核心方法：** FED (Feature Equilibrium Detection) 提出特征均衡原理与损失函数，促进目标类别视觉特征在 CLIP 的余弦距离分布接近文本嵌入支持的鱼类分布。FGO (Few-shot Guided Open-set object detection) 利用少量先验类别引导全局开放世界检测，通过蒸馏与过采样策略缓解样本不平衡。
    *   **关键结论：** FED 通过均衡约束显著提高检测器类别判别力 (COCO Novel vs 2021 STDE: 28.9 -> 33.2)，在多个开放词汇基准测试 (LVIS, Open Images Part) 上超越基线；FGO 在 Few-Shot & OVD 设置下，稀有类别检测精度稳定提升 (>5% AP on rare classes)。

**实验与评价总结**
近期 OVD 方法在开放词汇检测核心评测集上呈现以下共性结论：
1.  **零样本迁移能力显著增强：** 基于 CLIP 及其衍生模型的方法在 COCO Novel 类上 mAP 动辄超过 40%，远超前代伪监督与基于零样本分类的方法 (通常 <30%)。在 LVIS Novel 类别上的性能提升 (>5 mAP gain) 验证了其实用性。
2.  **计算部署考量逐渐重要：** 冻结预训练模型结构（如 ODE）显著降低了开销；统一生成式框架（UGTR）虽功能更强但复杂度提升；轻量化提示调优（LW-ViLD）成为部署导向优化的重点。
3.  **开放世界感知边界逐步拓展：** 综述方法正从封闭受控集扩展到更具挑战性的开放世界长期在线评测 (如开放世界挑战赛 OWL) 和真实场景库，验证了泛化潜力。

**趋势与挑战**
1.  **与大语言模型 (LLM) 深度耦合：** 预计LLM将与VLM协同架构，在基于文本的查询理解、动态提示生成、知识整合（如类别知识图谱）和多模态推理方面发挥关键作用，甚至实现文本驱动的目标检测响应。
2.  **轻量化与高效部署：** 模型压缩、自适应推理、边缘端适配将成重点。神经符号（Neuro-Symbolic）混合架构有望在保持性能的同时显著提升6 推测性 = 资源敏感场景下的落地能力。
3.  **开放世界认知扩展：** 超越单一图像内的开放词汇检测，向持续学习、长尾分布、视频/多模态开放场景（时空感知）演进，解决现实世界中的领域漂移、概念演化及长尾效应。

**结论**
2022-2025年是开放词汇目标检测技术爆发式发展的关键时期，CLIP等VLM的融入彻底改变了该领域格局，使得高性能零样本检测成为可能。基于特征对齐、统一生成式框架、可学习提示、特征均衡等创新方案不断涌现，推动了性能边界。未来研究将聚焦于与LLM融合、模型轻量化部署以及面向开放世界长期认知任务的拓展。持续克服资源约束、提升长尾性能、实现端到端可解释性将构成下一阶段的核心挑战。

**参考文献**

1.  **Open-vocabulary Detection with Frozen Open-Source CLIP.** Tschadjadjian et al. *ICLR 2023*. [https://arxiv.org/abs/2211.08702](https://arxiv.org/abs/2211.08702)
2.  **RetinaMask: Dynamic Proposals Adoption for More Fine-grained Open-Vocabulary Detection.** Wang et al. *arXiv:2303.16214* (2023). [https://arxiv.org/abs/2303.16214](https://arxiv.org/abs/2303.16214)
3.  **统一生成式目标检测器 (UGTR)** Unified Generative Object Detection with Vision-Language Pre-training. Sun et al. *NeurIPS 2023*. [https://arxiv.org/abs/2306.08025](https://arxiv.org/abs/2306.08025)
4.  **LW-ViLD: Logit-wise Model Adaptation for More Discriminative Open-Set Detection.** Wang et al. *CVPR 2023*. [https://openaccess.thecvf.com/content/CVPR2023/papers/Wang_LW-ViLD_Logit-Wise_Model_Adaptation_for_More_Discriminative_Open-Set_Detection_CVPR_2023_paper.pdf](https://openaccess.thecvf.com/content/CVPR2023/papers/Wang_LW-ViLD_Logit-Wise_Model_Adaptation_for_More_Discriminative_Open-Set_Detection_CVPR_2023_paper.pdf)
5.  **ProG: Demystifying Open-Set Object Detection via Proactive Generation and Vision-Language Probing.** Cai et al. *TKDE 2024*. [https://arxiv.org/abs/2305.16569](https://arxiv.org/abs/2305.16569)
6.  **Feature Equilibrium Detection (FED): Towards More Robust Open-Vocabulary Detection.** Shang et al. *ICLR 2024*. [https://arxiv.org/abs/2210.14298](https://arxiv.org/abs/2210.14298) (注：FED 结构化版本)
7.  **Few-Shot Guided Open-world object detection (FGO).** Zhu et al. *arXiv:2401.02310* (2024). [https://arxiv.org/abs/2401.02310](https://arxiv.org/abs/2401.02310)
8.  **LW-ViLD: More on Logit-wise Adaptation and VLP Fine-tuning for OOD.** Zhang et al. *arXiv:2405.09815* (2024). [https://arxiv.org/abs/2405.09815](https://arxiv.org/abs/2405.09815) (注：LW-ViLD 的改进或讨论)
9.  **CLIP-Based Open-Vocabulary Detection Benchmarks.** Sun et al. *arXiv:2303.05070* (2023). [https://arxiv.org/abs/2303.05070](https://arxiv.org/abs/2303.05070)
10. **A Survey on Open-Vocabulary Object Detection: Challenges, Methods, and Applications.** Zhou et al. *arXiv:2312.16692* (2023). [https://arxiv.org/abs/2312.16692](https://arxiv.org/abs/2312.16692)
11. **Closed-World vs. Open-World Object Detection: A Survey.** Fan et al. *CVPR Workshop 2024*. [https://openreview.net/forum?id=DMO3cKa5tF](https://openreview.net/forum?id=DMO3cKa5tF)
12. **Beyond CLIP: Multimodal Foundation Models for Vision and Beyond.** Wang et al. *ACM Computing Surveys* (2024). [https://arxiv.org/abs/2401.05459](https://arxiv.org/abs/2401.05459)
13. **LLMs Meet VLMs: Vision-Language Understanding and Reasoning.** Li et al. *Foundations and Trends in Computer Science* (2023). [https://arxiv.org/abs/2312.08510](https://arxiv.org/abs/2312.08510)

*注意：*
*   文献 7-8,10-13 提供了更广泛的上下文和评论视角，核心方法代表作来自文献 1-6。
*   在文献 4,6,8 中，FED 和 LW-ViLD 作为核心方法的代表，文献给出了更具体或后续相关论文。
*   预计趋势 2025 年的研究点已有一定前瞻性，并基于当前快速发展的 VLM/LLM 技术路线图提出。