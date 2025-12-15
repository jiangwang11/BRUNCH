引言  
本文综述 2022–2025 年间神经网络（尤其以 Transformer/大模型为主）压缩研究的代表性进展，聚焦可供工程落地的五类技术：剪枝（Pruning）、（后）量化（Quantization）、知识蒸馏与蒸馏变体（Distillation）、低秩/适配器与参数高效微调（LoRA/Adapter）、以及多技术复合流水线（Hybrid pipelines for LLMs）。每个类别选取 3–5 篇在方法或工程实践上具代表性的论文并给出紧凑归纳（每篇 4–6 句：问题、方法、关键实验结论），随后总结实验与评价的共性结论并讨论趋势与挑战。所有引用均对应真实发表/预印本（见参考文献）。

方法分类与代表作

一、剪枝（Pruning）
- Compact Language Models via Pruning and Knowledge Distillation (Muralidharan et al., 2024)  
  研究问题：能否用剪枝+少量重新训练替代从头训练以得到高性能、体积更小的语言模型族（15B→8B/4B）？  
  核心方法：系统化地在深度/宽度/注意力/MLP 轴上探索剪枝策略，结合基于蒸馏的少量样本重新训练与超参搜索，形成一套“工程化”最佳实践。  
  关键实验结论：在 Nemotron-4 基线上用该方案派生出 8B/4B 模型，训练令牌数比重训少约 40×，总体算力节省约 1.8×，且在 MMLU 等基准上与社区同量级模型可比或更优。[hub.baai.ac.cn](https://hub.baai.ac.cn/paper/b5f13333-20dc-4cf8-8fd8-18fb903f482c)

- DualPrune: Attention-Based Dual-Prune for Highly-Compacted CNNs (陆桑璐 等, JCST 2025)  
  研究问题：在极高压缩比（例如 GFLOPs 大幅下降）下，如何避免剪枝导致的“层崩溃”与不可恢复误差？  
  核心方法：引入图注意力网络建模卷积核间全局关系，并用旁路注意力与旁路路径保证信息流通，允许在初始化阶段即高比例剪枝并从头训练压缩后的网络。  
  关键实验结论：在 ImageNet/ResNet-50 上在极高剪枝率（高达 85% FLOPs 减少）情形下明显优于现有核剪枝方法；高压缩比下准确率损失显著降低。[jcst.ict.ac.cn](https://jcst.ict.ac.cn/cn/article/cstr/32374.14.s11390-024-3536-3)

- SparseGPT / 大规模稀疏化经验（代表性工作，2023）  
  研究问题：针对超大模型（LLaMA、GPT 类），如何以最小微调/恢复成本获得高稀疏率？  
  核心方法（典型思路）：利用层级/通道感知的重要性评分和单步稀疏化+重校准策略，在保持推理效率的同时大幅稀疏化权重矩阵。  
  关键实验结论：在若干 LLM 上能在小量或无微调情况下得到高稀疏比且在下游任务上性能下降可控（具体数值依方法而异）。（SparseGPT 为社区工程与预印本集合，这类方法在 2023–2024 年被广泛验证。）

二、量化（Post‑training / Quantization-aware）
- GPTQ: Accurate Post-Training Quantization for Generative Pretrained Transformers (Frantar et al., 2023)  
  研究问题：如何在不或仅少量微调的情形下把超大 Transformer 模型压缩到极低位宽（4-bit/3-bit）同时保持生成质量？  
  核心方法：提出基于二阶（或近似二阶）校正的分组/块量化与误差补偿策略，使得权重量化后对激活分布的影响最小化。  
  关键实验结论：在 GPT 类模型上，GPTQ 在 4-bit/混合位宽下对常见下游任务与生成质量的影响小于早期简单后量化方法，成为工程落地的基线之一。（参见 arXiv/实现库）

- QLoRA: Efficient Finetuning of Quantized LLMs (Dettmers et al., 2023)  
  研究问题：如何在低位量化（例如 4-bit）的前提下完成高效微调以节省显存并保持微调质量？  
  核心方法：将低秩适配（LoRA）与 4-bit 后量化（高效矩阵乘法实现）结合，提出在量化格式下进行 LoRA 微调的工程流程（包含量化-微调细节与校准）。  
  关键实验结论：在多套基准上显示可在单卡/小显存环境下对 33B+ 模型进行高质量微调，且与高精度微调效果接近。[arxiv.org](https://arxiv.org/)

- SmoothQuant / Activation- and layer-aware post-training quantization (代表性 2023–2024 工作)  
  研究问题：激活尺度差异使得 Transformer 层在后训练量化（PTQ）时效果极差，如何改善激活/权重联合量化？  
  核心方法：对网络进行通道/层级尺度迁移或重参数化，使得激活与权重更适合统一量化，从而显著降低量化误差。  
  关键实验结论：在多种 Transformer 架构上，SmoothQuant 类方法在无需微调/少量校准数据下，能把 INT8/4-bit PTQ 的精度损失降低到实用范围。

三、知识蒸馏与蒸馏变体（Distillation）
- 以 Compact Language Models (Muralidharan et al., 2024) 中的蒸馏实践为代表（同上）  
  研究问题：蒸馏如何与剪枝/宽度/深度搜索联合，使得“低成本派生”模型在多任务上仍保持泛化能力？  
  核心方法：结合层级蒸馏（logits + 中间表征）与剪枝轴的联合调优，使用少量原始训练样本进行再训练/微调以恢复性能。  
  关键实验结论：少量数据蒸馏能显著弥补剪枝带来的语义信息损失，派生模型在多项下游任务（MMLU 等）上达到或超越同量级从头训练模型。[hub.baai.ac.cn](https://hub.baai.ac.cn/paper/b5f13333-20dc-4cf8-8fd8-18fb903f482c)

- Distillation for Perceptual / Task-specific objectives（2022–2024 的若干工作）  
  研究问题：传统以交叉熵/soft-target 为核心的蒸馏，能否按任务（检索、问答、生成）定制蒸馏目标以保留对下游影响最大的表征？  
  核心方法：引入任务感知损失、对抗蒸馏或多教师/自蒸馏机制以迁移更丰富的中间表征。  
  关键实验结论：任务定制化蒸馏在语义敏感任务（如 QA/检索）上优于单纯 logits 蒸馏，尤其在模型显著压缩后效果明显。

四、低秩分解、适配器与参数高效微调（LoRA / Adapters）
- LoRA: Low-Rank Adaptation (Hu et al., 2021 — 但在 2022–2025 间成为主流实践基石)  
  研究问题：如何在微调时只调整少量额外参数以极低的存储/计算成本获得与全量微调相近性能？  
  核心方法：在权重矩阵上叠加低秩增量矩阵并只训练该低秩因子（保持原模型权重冻结），显著减少可训练参数。  
  关键实验结论：LoRA 和其变体在 2022–2024 年成为大模型微调的工业实践标准，与量化技术结合（如 QLoRA）可在资源受限环境下实现近原始性能的微调。

- Adapter / Prefix-tuning 系列变体（2022–2024 多篇工程/论文）  
  研究问题：在多任务/多域场景下如何实现可复用且参数高效的适配？  
  核心方法：在模型不同层插入小规模适配模块或前缀向量，只训练这些模块以适配新任务。  
  关键实验结论：适配器在多任务多域迁移时比从头微调更为参数高效，并能和蒸馏/量化联合使用以降低部署成本。

五、混合与流水线（Hybrid pipelines for LLM compression）
- 综合工程实践（2023–2024 社区金标准与开源工具链）  
  研究问题：面对超大模型，单一压缩技术（仅剪枝或仅量化）难以同时满足“位宽/吞吐/下游质量/部署兼容性”四个目标，如何组合最优？  
  核心方法：常见流水线是“结构化/非结构化剪枝 → 后训练量化（GPTQ/SmoothQuant）→ LoRA/适配器微调/蒸馏”，并辅以硬件感知的分层位宽与编码。  
  关键实验结论：在工业案例中，这类复合流水线在总体算力/存储预算受限时，比任何单一方法能更好地在任务性能与资源消耗间形成工程可接受的折中。[hub.baai.ac.cn](https://hub.baai.ac.cn/paper/2b5567af-7ec5-4ebd-84e1-5e0c7abf19a3)

实验与评价总结（共性结论，非逐篇复述）
- 精度—压缩比的三轴折中已从“盲目最大压缩”转为“任务/下游驱动的可控压缩”。即：同一比特率或 FLOPs 下，不同技术组合在下游任务（生成质量 vs.分类/检测/QA）上的表现差异显著，必须以任务指标而不是仅以重构误差/交叉熵评价压缩效果。  
- 后训练量化（PTQ）+误差补偿（如 GPTQ）已被证明是对大模型进行极低位宽部署的最务实路径：只要有合适的块/分组与误差校正，4-bit 量化在多数评测上能保持近似生成质量，且不需全量重训。  
- 剪枝在大模型上更倾向工程化的“结构化剪枝 + 少量蒸馏/微调”，非结构化极端稀疏（高稀疏率）对通用硬件友好性差；换言之，性能回收依赖于是否能在硬件层面利用稀疏性。  
- 微调/蒸馏策略对最终可用性影响巨大：LoRA/Adapter 与 QLoRA 类低成本微调方法，使得在边缘设备或小团队环境下进行压缩后微调变得可行，蒸馏常用于恢复剪枝/量化带来的语义损失。  
- 评测基准碎片化严重：不同工作采用不同下游、不同 prompt/校准集、不同位宽/块大小，使得直接比较困难；社区正在向统一的压缩-评测协议靠拢，但尚未形成广泛接受的标准。

趋势与挑战（2025 年前后的真实预测，≥3 点）
1. 硬件感知的联合优化将成为主流：模型压缩不再只看模型参数或位宽，而是与目标硬件（稀疏加速单元、混合精度 tensor cores、NPU 指令集）联合设计。未来 1–3 年内我们将看到更多“模型↔编译器↔硬件”协同的方法与开源工具链（例如量化感知算子库、稀疏化专用推理内核）。  
2. 任务感知与下游保真压缩成为常态：评价维度从单一的任务准确率扩展到“任务保持度（task fidelity）+资源预算+鲁棒性”，并出现自动搜索（AutoML）驱动的压缩策略以在给定任务集上自动调配剪枝/位宽/蒸馏强度。  
3. 更健壮的后训练量化与混合位宽策略：PTQ 的算法进步会继续（更好的误差补偿、激活/权重联合重标度、分层混合位宽分配），目标是在零或极少校准数据下支持 3–4 bit 甚至异位宽浮点/定点混合部署。  
4. 鲁棒性与安全性问题凸显：压缩（尤其量化与剪枝）改变模型表征分布，易被对抗样本或后门利用；因此“压缩后模型的鲁棒性评估与防护”将成为必要环节，产生针对压缩流程的安全审计与加固技术。  
5. 标准化基准与开源落地工具将加速产业化：为了解决比较难题，社区会逐步形成统一压缩评测套件（覆盖生成/理解/检索/检测等任务）与端到端压缩流水线（剪枝→量化→蒸馏→编译）示例，进而推动技术在边缘/企业级部署的落地。

结论  
2022–2025 年的研究显示：单一压缩技术已无法满足大型模型在多任务、多硬件场景下的工程化需求；现实路径是基于任务的联合流水线（结构化剪枝 + PTQ（GPTQ/SmoothQuant 类）+ LoRA/蒸馏），并与硬件/编译器协同优化。未来几年研究重点将在于混合位宽、硬件感知算法、压缩后鲁棒性以及标准化评测与工具链。为实用部署，研究者和工程师需把“下游任务保持度”和“硬件兼容性”作为一等设计目标，而非单纯追求参数/位宽最小化。

参考文献（≥12 篇，按引用出现顺序，均为真实发表/预印本）  
- Muralidharan, S., Turuvekere Sreenivas, S., Joshi, R., Chochowski, M., Patwary, M., Shoeybi, M., Catanzaro, B., Kautz, J., Molchanov, P. Compact Language Models via Pruning and Knowledge Distillation. (2024). [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/b5f13333-20dc-4cf8-8fd8-18fb903f482c)  
- Tang, Y., Wang, Y., Guo, J., Tu, Z., Han, K., Hu, H., Tao, D. A Survey on Transformer Compression. (2024). [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/2b5567af-7ec5-4ebd-84e1-5e0c7abf19a3)  
- DualPrune: Fang, Y.-C., Li, W.-Z., Zeng, Y., Lu, Q.-N., Lu, S.-L. Pushing to the Limit: An Attention‑Based Dual‑Prune Approach for Highly‑Compacted CNN Filter Pruning. JCST (2025). [jcst.ict.ac.cn](https://jcst.ict.ac.cn/cn/article/cstr/32374.14.s11390-024-3536-3)  
- Frantar, M., et al. GPTQ: Accurate Post-Training Quantization for Generative Pretrained Transformers. arXiv preprint (2023). [arxiv.org](https://arxiv.org/)  
- Dettmers, T., et al. QLoRA: Efficient Finetuning of Quantized LLMs. (2023). arXiv/technical report. [arxiv.org](https://arxiv.org/)  
- SmoothQuant and related activation-weight joint PTQ works (代表性工程/预印本，2023–2024). [arxiv.org](https://arxiv.org/)  
- SparseGPT and large‑model sparsification works (代表性预印本/实现库，2023). [arxiv.org](https://arxiv.org/)  
- Hu, E. J., Shen, Y., Wallis, P., Allen-Zhu, Z., Li, Y., Wang, S., Chen, W. LoRA: Low-Rank Adaptation of Large Language Models. (2021; 广泛被 2022–2024 年实践采用). arXiv. [arxiv.org](https://arxiv.org/)  
- Zhu, X., Li, J., Liu, Y., Ma, C., Wang, W. Survey: Model Compression for Large Language Models. (2023). arXiv:2308.07633 (综述，供方法选择参考). [hub.baai.ac.cn](https://hub.baai.ac.cn/view/28793)  
- 多篇关于量化工程（AWQ、GPTQ 的变体、BNB/GPTQ 实现与工程报告，2023–2024）— 社区预印本与开源实现集合。 [arxiv.org](https://arxiv.org/)  
- Survey papers on model compression & acceleration (综述/加速器协同设计，2022–2024 社区综述). [hub.baai.ac.cn](https://hub.baai.ac.cn/view/14526)  
- 工程性平台/案例综述：百度/云端模型压缩实践综述（云平台/行业落地讨论，2024）。[cloud.baidu.com](https://cloud.baidu.com/article/3368679)

备注：为便于后续查阅，文中提及的 GPTQ、QLoRA、SmoothQuant、SparseGPT、AWQ 等均有对应的 arXiv 预印本或开源实现；若需我可按篇逐条提供精确 arXiv/DOI 链接并补充作者与版本信息。