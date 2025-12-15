引言  
随着物联网设备在工业、城市与消费场景的大规模部署，基于网络流量的异常检测（anomaly/ intrusion detection）成为保障可用性与防御未知攻击的关键技术路线。近年来（尤其是 2022–2025 年），研究重心从“通用大模型在单机/中心化训练上的精度”向“设备/场景定制化、少样本/零样本泛化、时空/关系建模、联邦/分布式隐私训练以及在线/低延迟部署”转移。本文在 2022–2025 年代表性工作基础上，按照方法学类别（时序深度模型、时空/关系与注意力、无监督自编码/GAN 与在线方法、少样本/度量学习、联邦/隐私分布式学习）逐类梳理代表作并给出共性实验结论与未来趋势预测。文中每篇工作介绍均限于 4–6 句，突出研究问题、核心方法与关键实验结论；实验与评价部分仅总结共性发现，不逐篇赘述。  

方法分类与代表作  
（每类按重要性选 2–5 篇代表工作，优先覆盖 2022–2025 年成果并兼顾必要的基线/奠基工作）  

A. 时序深度模型（LSTM / TCN / Transformer / 混合）  
1) Pan et al., “二次特征提取与 BiLSTM-Attention 的网络流量异常检测” (JEIT, 2023) — [jeit.ac.cn]  
- 问题：在多类、不平衡流量情形下提高多分类异常检测精度并增强特征表征能力。  
- 方法：先用 BiLSTM 提取一阶时序特征，再用注意力机制对特征重要性加权完成二次特征提取；采用“先总分后细分”的多级分类设计。  
- 结论：在 CICIDS2017 等子集上，相较单一 LSTM，F1 与召回显著上升（论文给出 99%+ 的局部指标），并展示注意力模块能提高对少量攻击类的敏感性。  

2) Gu et al., “MSECNN-BiLSTM：基于时空卷积与多头挤压激励的异常流量检测” (JEIT, 2024) — [jeit.ac.cn]  
- 问题：传统方法未充分利用流量的时空尺度信息与自适应通道权重。  
- 方法：1D-CNN 捕获空间尺度特征，Multi-head Squeeze-Excitation 自适应加权，全局特征输入 BiLSTM 建模时间依赖，softmax 分类。  
- 结论：在 NSL‑KDD 等基准上，组合模型在 Accuracy / F1 / MCC 等指标上均优于纯 CNN/纯 BiLSTM 基线，证明时空耦合与通道自适应的重要性。  

3) Liu et al., “基于多尺度残差时间卷积网络的物联网入侵检测（MRID）” (Telecommunications Science, 2025) — [telecomsci.com]  
- 问题：面向雾/边缘部署的实时检测需要在计算效率与时空表征间取得平衡。  
- 方法：提出多尺度残差时间卷积模块（TCN 变体）并结合改进的流量注意力机制以突出关键特征，强调模型轻量化以适配雾计算。  
- 结论：在 CICIDS2017 / CSE‑CIC‑IDS2018 上，MRID 在保持计算效率的同时提高鲁棒性与实时检测吞吐，适合落地于边缘节点。  

（小结）本类工作的共性：①通过时间模型（BiLSTM / TCN / Transformer）提升长期依赖建模能力；②结合空间卷积或注意力可显著改善对短时突发与长期渐进异常的鉴别；③评估集中在公开流量数据集，且对真实长期概念漂移评估不足。[jeit.ac.cn][telecomsci.com][jcs.iie.ac.cn]

B. 时空/关系建模与图注意力方法  
1) Hu et al., “TSAN：基于关系挖掘和注意力的多维时序异常检测” (信息安全学报, 2024) — [jcs.iie.ac.cn]  
- 问题：多维时序中序列间隐含关系（相关/因果）未被充分挖掘，影响异常判别与可解释性。  
- 方法：端到端挖掘序列关系构建稀疏关系图，采用因果推断得到的因果掩码增强可解释性，再基于时空联合注意力网络做预测与异常判定。  
- 结论：在 MSL、SMD 等多维时序数据集上，TSAN 的 F1 优于次优方法 0.9%–2.3%，且跨数据集性能波动最小，显示关系先验能提高泛化稳定性。  

2) 相关图/关系方法与工业场景基线（代表性早期/横向工作）  
- TABOR / 图模型类工作与基于背景知识的图异常检测在工业控制系统（ICS）取得了可解释性与低误报的优势（相关综述详见 [joconline.com.cn]）。  

C. 无监督自编码器 / GAN / 在线自适应方法（面向未知/零日）  
1) Mirsky et al., “Kitsune: An ensemble of autoencoders for online network intrusion detection” (NDSS, 2018) — [ndss-symposium.org]（作为线上自编码器代表性基线）  
- 问题：需要低延迟、在线检测并能适应流量分布的实时系统。  
- 方法：将流量映射为多维统计特征，使用多个小自编码器并行重建误差做异常判断，实现轻量在线运行。  
- 结论：在物联网场景的真实测试床上，Kitsune 在低计算资源下实现实时告警，但对概念漂移与长时间泛化仍敏感。  

2) Meidan et al., “N‑BaIoT: Network-based detection of IoT Botnet attacks using deep autoencoders” (IEEE Pervasive Comput., 2018) — （用于说明深自编码器在 IoT 僵尸网络检测的有效性）  
- 结论要点：深自编码器对单一设备、常见僵尸网络样本具有高检出，但对未知攻击变体敏感度下降。  

3) 近年进展（2022–2024）强调模型压缩、在线训练管线与基于重构误差的阈值自适应策略（参见综述与若干 JEIT / 通信学报工作）。[jeit.ac.cn][joconline.com.cn]

D. 少样本、度量学习与自适应抽样（对抗类不平衡）  
1) Yin et al., “无监督自适应抽样与改进孪生网络结合的网络流量异常检测” (JEIT, 2025) — [jeit.ac.cn]  
- 问题：大量流量中攻击样本稀少、类别不平衡导致监督学习偏向正常类；需要在小样本条件下有效识别攻击并提升未知攻击检出。  
- 方法：提出基于 K‑medoids 的自适应小样本抽样算法 KAFS（无监督聚类选择代表样本）构建平衡少样本训练集；设计带鲁棒损失的孪生 MLP（SMLP）学习样本间相似/差异并用于判别。  
- 结论：在 CICIDS2017/2018 上，用极少样本训练时对已知与未知攻击的检出率均较常规模型提升数个百分点，显示了采样+度量学习组合在少样本 IDS 场景的潜力。  

2) 典型少样本/孪生网络基线（IEEE TII 等早期工作）表明度量学习可在样本极稀疏时维持较好泛化；但需注意负样本/伪标签生成的可靠性问题。  

E. 联邦学习 / 隐私保护与分布式检测  
1) Zhang et al., “GB‑AEnet‑FL：基于对抗双编码与联邦学习的物联网异常检测” (计算机应用研究, 2022) — [arocmag.cn]  
- 问题：物联网场景下数据跨域分散，隐私/带宽限制阻碍中心化标注与训练。  
- 方法：提出基于自编码器的对抗训练与异常数据扩充策略，并在联邦学习框架中动态选择参与方以提高聚合效率与隐私保护。  
- 结论：在多个数据集上，联邦对抗编码器方案在不泄露原始流量的前提下提升了跨域泛化能力与准确性，说明联邦策略能在保护隐私的同时保持检测性能。  

2) DÏoT（ICDCS 2019，代表性联邦/自学习系统）和近年的 DeepFed / Deep anomaly 联邦变体（见综述）表明：联邦方案能缓解单域数据稀缺，但对异构性与系统鲁棒性要求高。[arocmag.cn][jos.org.cn]

实验与评价总结（共性结论，按研究维度）  
1. 数据集与基准偏差：主流评估仍集中在 CICIDS2017/CICIDS2018、NSL‑KDD、UNSW、N‑BaIoT / Bot‑IoT 等公开集；这些数据集便于比较但存在攻击分布、流量加密与设备多样性不足的问题，导致模型在真实部署时的概念漂移/泛化能力难以保证。[jeit.ac.cn][joconline.com.cn][jos.org.cn]  
2. 指标与稀疏样本评估：多数工作报告 Precision/Recall/F1/Accuracy 和有时的 MCC；但面对类别不平衡，单一 Accuracy 误导性强。少样本/未知攻击评估应使用检出率（recall）和 FPR（误报率）并报告在未知攻击上的泛化能力；Yin et al. (2025) 明确体现少样本对未知攻击检测的重要提升。  
3. 在线性与延迟衡量不足：少数近年工作（如 MRID、Kitsune）关注实时/边缘部署并给出延迟/吞吐评估，但大多数方法仅报告离线指标，未充分衡量模型更新开销、通信延迟与在嵌入式设备上的部署可行性。  
4. 可解释性与可维护性薄弱：关系/图模型（如 TSAN）与基于规则/行为规范的方法能提供更好的可解释证据；而深度“黑盒”模型在误报分析与长期维护上存在实际障碍。  
5. 联邦/隐私方法的通信-性能折中：联邦学习可保隐私并提升横向泛化，但参与者异构性、通信开销与模型同步延迟会显著影响收敛速度与检测鲁棒性（见 GB‑AEnet‑FL、DÏoT 的讨论）。[arocmag.cn][jeit.ac.cn]  

趋势与挑战（2025 年前后可验证的真实走向，至少三点）  
1. 少样本与度量学习成为常态化方向（短期可验证）：大量现实网络中攻击样本稀少且多变，论文与实证（如 Yin et al., JEIT 2025）显示“无监督/自适应抽样 + 度量/孪生网络”能在有限样本下显著提高未知攻击检出。未来 1–3 年内，少样本/元学习方法将从实验室基线转向生产级少量标注的在线自适应系统。  
2. 联邦与差分隐私驱动的跨域协同检测将加速产业落地，但伴随系统工程问题（异构性、通信/延迟、鲁棒聚合）实用化仍需工程级改进：GB‑AEnet‑FL（2022）与 DÏoT（2019）已证明可行，但 2025 年后将更多关注通信压缩、个性化聚合与对抗鲁棒性。可验证研究将以跨机构联邦基准竞赛/数据集为检验场。  
3. 关系/图与因果建模提升可解释性与跨域迁移能力：TSAN（2024）显示将序列间关系（相似/因果）作为先验能稳定跨数据集性能；未来研究会把图神经网络 + 因果掩码用于发现跨设备传播规律与联合异常（多设备协同攻击），并成为工业级可解释检测的首选方向。  
4. 从离线到在线的评估规范化：社区将逐步采纳包含“长期运行（概念漂移）测试、延迟/资源消耗、误报成本度量（运营成本）、跨域泛化”在内的评估套件；单纯在短期静态数据集上报告高指标将不再能证明工程可用性。  
5. 多模态与跨层检测（流量 + 日志 + 设备指纹 + MUD/行为规范）将成为提升零日检测能力的主流：Paper.edu.cn（2025）关于训练集群网络的流量+日志检测表明，融合多源信号并在应用层/控制层加入行为规范有助于降低误报并加速故障定位；在 IoT 场景，这一策略同样有望提高对复杂攻击链的识别。  

结论  
过去三年（含 2022–2025）有关 IoT 网络异常检测的研究在“精细化时空/关系建模、少样本/度量学习、联邦学习与边缘部署、线上自适应阈值/抽样”几方面均有实质进展。若要把学术成果转向工业可用，需要更严格的长期/跨域评估基准、注重模型可解释性与维护性、以及工程层面的通信与延迟优化。本文按方法类别挑选并精述了代表性工作（含 2022–2025 年成果），总结了实验共性结论，并对 2025 年前后的可验证趋势给出明确指引，供后续研究与工程落地参考。  

参考文献（按文中出现顺序，均为真实已发表工作或公开报告；链接以域名形式给出以便查阅）  

- 尹梓诺, 陈鸿昶, 马海龙, 胡涛, 白禄鑫. 无监督自适应抽样与改进孪生网络结合的网络流量异常检测方法. 电子与信息学报, 2025. [jeit.ac.cn](https://jeit.ac.cn/cn/article/doi/10.11999/JEIT241115?viewType=HTML)  
- 刘丽伟, 赵红超, 李学威, 等. 基于多尺度残差时间卷积网络的物联网入侵检测模型. 电信科学, 2025. [telecomsci.com](https://www.telecomsci.com/zh/article/doi/10.11959/j.issn.1000-0801.2025046/)  
- 潘成胜, 李志祥, 杨雯升, 蔡凌云, 金爱鑫. 基于二次特征提取和BiLSTM-Attention的网络流量异常检测方法. 电子与信息学报, 2023. [jeit.ac.cn](https://www.jeit.ac.cn/cn/article/doi/10.11999/JEIT221296?viewType=HTML)  
- 顾伟, 行鸿彦, 侯天浩. 基于网络流量时空特征和自适应加权系数的异常流量检测方法 (MSECNN‑BiLSTM). 电子与信息学报, 2024. [jeit.ac.cn](https://jeit.ac.cn/cn/article/doi/10.11999/JEIT230825?viewType=HTML)  
- 胡智超, 余翔湛, 刘立坤, 张宇, 于海宁. 基于关系挖掘和注意力的多维时序异常检测 (TSAN). 信息安全学报, 2024. [jcs.iie.ac.cn](https://jcs.iie.ac.cn/xxaqxb/ch/reader/view_abstract.aspx?flag=1&file_no=20240607&journal_id=xxaqxb)  
- Fan LN, Li CL, Wu YC, et al. Survey on IoT Device Identification and Anomaly Detection. Journal of Software, 2024. [jos.org.cn](https://jos.org.cn/html/2024/1/6818.htm)  
- 孙海丽, 龙翔, 韩兰胜, 等. 工业物联网异常检测技术综述. 通信学报, 2022. [joconline.com.cn](https://www.joconline.com.cn/zh/article/doi/10.11959/j.issn.1000-436x.2022032/?viewType=HTML)  
- 张月, 唐伦, 王恺, 陈前斌. 基于 GB‑AEnet‑FL 网络的物联网设备异常检测. 计算机应用研究, 2022. [arocmag.cn](https://www.arocmag.cn/abs/2022.03.0142)  
- 刘贺, 王晓湘. 基于日志与流量分析的大模型训练异常检测. 中国科技论文在线, 2025. [paper.edu.cn](https://www.paper.edu.cn/releasepaper/content/202504-3)  
- Mirsky Y., Doitshman T., Elovici Y., Shabtai A. Kitsune: An ensemble of autoencoders for online network intrusion detection. NDSS Symposium, 2018. [ndss-symposium.org](https://www.ndss-symposium.org/)  
- Meidan Y., Bohadana M., Mathov Y., et al. N‑BaIoT—Network‑based detection of IoT Botnet attacks using deep autoencoders. IEEE Pervasive Computing / related venues, 2018. (见综述引用)  
- Nguyen T.D., Marchal S., Miettinen M., et al. DÏoT: A federated self‑learning anomaly detection system for IoT. ICDCS, 2019. (联邦自学习代表) [ieeexplore.ieee.org](https://ieeexplore.ieee.org/)  
- Sharafaldin I., Lashkari A.H., Ghorbani A.A. Toward generating a new intrusion detection dataset and intrusion traffic characterization (CICIDS 数据集相关工作), 2018. (数据集参考，见 JEIT / 综述引用)  
- Zhou X.K., Liang W., et al. Variational LSTM enhanced anomaly detection for industrial big data. IEEE Transactions on Industrial Informatics, 2020. (时序变分 LSTM 基线，见综述引用)  
- 综述与数据集/基线摘引：见上述 JEIT、通信学报与 Journal of Software 中的参考文献列表以获取完整原始文献索引（多篇核心基线与数据集在这些综述中被详列）。[jeit.ac.cn][joconline.com.cn][jos.org.cn]  

（注：本文中对文献的选择与论述基于 2022–2025 年公开发表/在线可查的期刊会议论文与综述，文中所引 URL 指向相应期刊/会议的官方页面以便读者检索原文。）