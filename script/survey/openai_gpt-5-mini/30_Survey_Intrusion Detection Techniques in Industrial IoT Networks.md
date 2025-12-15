引言  
工业物联网（IIoT）网络的异常/入侵检测在 2022–2025 年出现了几条明确发展脉络：一是将物理过程约束或网络—物理（N–P）模型融入检测以捕获流程相关攻击；二是用时序深度学习（TCN/Transformer/GNN 等）提升对复杂时序/多变量流量的敏感性；三是把联邦学习、差分隐私与轻量化模型结合以满足现场部署与隐私要求；四是面向边缘/雾架构的部署与语义/感知驱动传输逐步进入研究视野。下文按方法类别综述 2022–2025 年代表性工作，重点说明研究问题、方法要点与关键实证结论（每篇 4–6 句）。随后归纳实验/评估共性结论，并给出面向 2025 年前后的趋势与挑战预测。

方法分类与代表作
1) 基于网络—物理模型与不变性检测（检测与区分“与过程相关”的攻击）
- Lin et al., “A Real‑Time Anomaly Detection Method for Industrial Control Systems …” (IEEE Internet of Things Journal, 2025; summarized by a public report) [secrss.com].  
  研究问题：针对 ICS/IIoT 中与过程相关攻击（例如伪装转移、系统恢复）以及丢包/网络延迟导致的误报问题。  
  核心方法：提出以设备级轮询时间模式与基于事件的长短周期确定性有限自动机（LSP‑DFA）为核心的基线模型，并在此基础上发展周期性集成 DFA（PIDFA‑AD），引入转移时间循环排列集与行动时间等新特征以捕捉顺序/时长特性。  
  关键实验结论：在两个实验室规模 ICS 数据集上的对比显示，PIDFA‑AD 在检测率、F1 与误报率上显著优于多种基线方法，尤其能检测伪装转移与区别网络延迟与长时间攻击，从而把误报率降到很低水平 [secrss.com]。

- 综述（背景）: Sun et al., “Overview of anomaly detection techniques for industrial Internet of things” (Journal on Communications, 2022) [joconline.com.cn].  
  研究问题：系统归类 IIoT 的异常检测方法与适用场景（统计、模型化、ML/DL、边缘部署等）。  
  核心内容：对 2000–2021 年方法做体系化分类并指出 CPS/ICS 中基于物理不变性和模型的检测优势与局限（可解释但需良好物理模型或自动化不变性发现）。  
  关键结论：强调状态爆炸、稀有/低频状态处理与网络延迟对基于模型方法的影响，建议与数据驱动方法结合以提高鲁棒性 [joconline.com.cn]。

2) 时序深度学习与图/注意力方法（端到端学习复杂时序/多变量依赖）
- Liu et al., “Multiscale residual temporal convolutional networks‑based intrusion detection model in Internet of things” (Telecommunications Science, 2025) [telecomsci.com].  
  研究问题：在 IoT 流量上提升实时入侵检测的时空表征能力并兼顾计算效率。  
  核心方法：提出 MRID，采用多尺度残差时间卷积模块与改进的流量注意力机制来增强局部/跨尺度时序特征学习，适配雾/边缘部署。  
  关键实验结论：在 CICIDS2017 与 CSE‑CIC‑IDS2018 上报告了较高的准确率与鲁棒性（相对于同类轻量时序网络），并保持在线性计算开销下的实时性 [telecomsci.com]。

- Zhao et al., “Graph Attention Network and Informer for Multivariate Time Series Anomaly Detection” (Sensors, 2024).  
  研究问题：如何在多变量网络流量上同时捕获空间（实体间关系）与长序列时序依赖用于异常检测。  
  核心方法：用图注意力网络（GAT）建模变量间依赖，再用 Informer/长序列 Transformer 变体处理长时序，二者级联以输出异常评分。  
  关键实验结论：在多项公开多变量时序基准上该组合在定位长时依赖异常与减少误报上相对传统 RNN/单一 Transformer 有优势（尤其对稀疏/长周期异常表现更稳健）[doi.org/10.3390/s24051522]。

- UVaydov et al., “DeepSense: Fast wideband spectrum sensing through real‑time in‑the‑loop deep learning” (IEEE INFOCOM 2021 → 被后续 IIoT 工作引用).  
  研究问题：在资源受限的实时系统中如何用深学习替代复杂传统谱估计实现快速感知/检测。  
  核心方法与结论：用轻量化端到端深网络替代频域算法实现快速宽带感知，实测显示能在低延迟下保持较好检测性能；该思路被后续 IIoT/无人机频谱感知与在线模型更新方案所借鉴（参见 JEIT 2025 的谱感知工作）[doi.org/10.1109/INFOCOM42981.2021.9488764]。

3) 联邦学习 / 隐私保护与跨节点协同（面向跨站点/边缘协作与数据隐私）
- Wang et al., “Network intrusion detection method based on federated learning and spatiotemporal feature fusion” (Journal of Zhejiang University (Engineering Science), 2025) [zjujournals.com].  
  研究问题：在多组织/多边缘节点场景下如何在不共享原始流量数据的前提下构建鲁棒 IDS。  
  核心方法：提出 FL‑CNN‑LSTM 框架，客户端并联 CNN（空间特征）与 LSTM（时间特征），用多头注意力融合并在联邦学习框架下聚合；使用 SMOTE 处理类不平衡以改善少数攻击类别识别。  
  关键实验结论：在 CIC‑IDS2018、NSL‑KDD 与 UNSW‑NB15 上报告联邦训练与集中式训练性能接近（差别 <1%）且在隐私约束下能维持高准确度，显示联邦学习对跨域数据扩充有实际价值 [zjujournals.com].

- Mothukuri et al., “Federated‑learning‑based anomaly detection for IoT security attacks” (IEEE Internet of Things Journal, 2022).  
  研究问题：如何在 IoT 上协作训练异常检测模型同时降低隐私泄露。  
  核心方法：基于 FL 的层次/分层聚合策略结合轻量分类器以降低通信与计算开销；讨论差分隐私与加密的折衷。  
  关键结论：仿真/实验表明在适度的本地训练和聚合策略下，联邦方法能在通信代价受控的情况下提高跨域泛化，但需结合差分隐私以防模型反演攻击（会带来精度下降）[doi.org/10.1109/JIOT.2021.3077803]。

- Dong et al., “Differentially Private Federated Learning Based Wideband Spectrum Sensing for UAV Swarm” (Journal of Electronics & Information Technology, JEIT, 2025).  
  研究问题：在高移动性无人机群中实现协同频谱感知同时保护局部数据隐私（方法可被迁移用于协同入侵检测）。  
  核心方法：提出 FS‑WSSNet（特征拆分轻量网）与基于差分隐私的联邦迁移学习（DP‑FTL）在线自适应方案，上传前对特定层添加噪声并做梯度裁剪。  
  关键实验结论：在多场景仿真中显示 DP‑FTL 在小噪声下可保持接近集中式训练的性能，且显著降低了通信/采样成本；提示 DP 与联邦迁移学习对 IIoT 场景的可行性/挑战（隐私—精度权衡）[jeit.ac.cn].

4) 特征工程 / 传统机器学习与可解释方法（轻量可解释方案）
- Ren et al., “Classification Method of Industrial Internet Intrusion Detection Based on Feature Selection” (Yanshan Univ. / CRAD 2021 summary) [crad.ict.ac.cn/fileJSJYJYFZ].  
  研究问题：在工业流量上通过特征选择改善多类别入侵识别，降低维度与计算开销。  
  核心方法：用 Pearson 相关、独热编码与常用 ML（随机森林、决策树、SVM、MLP）做二分类与多分类比较；在 UNSW‑NB15 与 CSE‑CIC‑IDS2018 上进行验证。  
  关键结论：特征筛选（阈值选择）能在保持或提升检测率的同时大幅减少模型参数，随机森林/决策树在多类识别与可解释性间表现平衡 [crad.ict.ac.cn/fileJSJYJYFZ]。

5) 系统、架构与零信任（部署、可审计性与策略层面）
- 张明强等, “工业物联网智能感知‑传输‑控制融合：关键技术与未来展望” (Journal of Electronics & Information Technology, JEIT, 2025) [jeit.ac.cn].  
  研究问题：把感知—传输—控制视为一体，评估其对安全检测/响应的影响与关键技术需求。  
  核心内容：讨论深度压缩感知、语义通信、信源‑信道联合编码与边缘协同对 IIoT 检测链路的影响，并指出实时性、语义对齐与解释性需求对入侵检测系统设计的制约。  
  关键结论：建议将语义/任务导向通信与边缘推理结合，以降低传输量并提升任务级检测效率（但需新型同步与一致性机制）[jeit.ac.cn].

- 工业零信任综述: Wang et al., “A Review of Zero Trust Security Research in Industrial Internet” (CRAD/ICT, 2025) [crad.ict.ac.cn].  
  研究问题：在 IIoT 场景下如何从体系结构与策略层面引入零信任以支撑细粒度检测与响应。  
  核心内容：系统梳理身份认证、微隔离、软件定义边界与信任评估等构件对检测系统的支撑作用。  
  关键结论：指出零信任需要与实时检测（尤其是流程相关检测）协同，才能在保证可用性的同时限制横向攻击面 [crad.ict.ac.cn]。

实验与评价总结（共性结论，非逐篇复述）
- 数据集与评测基线不一致仍是最大问题：多数工作在 CICIDS、UNSW‑NB15、CSE‑CIC‑IDS2018、私有 ICS 实验台或自建无人机仿真上验证。不同工作使用的特征集合、注入攻击类型与采样率差异导致横向可比性差。综述/实证文章建议建立更多带流程标签的公开 ICS 数据集以评估流程相关攻击检测能力 [joconline.com.cn; secrss.com]。  
- 网络延迟/丢包与流程周期性对检测影响显著：基于 DFA/网络—物理模型的工作显示，若不建模延迟与周期性，误报率和漏报率都会显著上升；相应改进（如行动时间、周期性检测、异常替换）能减少对正常延迟的误判 [secrss.com]。  
- 隐私保护（FL/DP）与性能的折衷是主流难题：联邦/差分隐私方法在多站点协作上能保持泛化，但添加噪声或强隐私约束会降低对低频攻击类别的识别能力；合理选择被加噪参数层与压缩/剪枝策略可部分缓解该损失 [zjujournals.com; jeit.ac.cn]。  
- 轻量化与边缘部署可行但需联合设计：多项工作表明，经过模型剪枝、特征拆分或用 TCN 等轻量时序模块后，可在边缘/雾层实现近实时检测；但必须与通信/采样方案（如深度压缩感知或子奈奎斯特采样）协同设计以满足资源预算 [telecomsci.com; jeit.ac.cn]。  
- 可解释性与流程因果信息提升检测可信度：基于物理不变性或事件驱动模型的检测易解释（能定位哪一设备/转移异常），对工业运维尤为重要；纯黑箱 DL 模型在运营环境中难以直接被接受，混合方案具有更高工程落地价值 [joconline.com.cn; crad.ict.ac.cn]。

趋势与挑战（面向 2025 年前后 的真实预测；不少于 3 点）
1. 网络—物理混合检测将成为主流范式：单纯的流量时序检测难以区分“流程变慢源于网络延迟还是攻击”。未来 2–3 年会有更多方法把物理模型约束（不变性、事件化状态）与可微/学习化时间序列模型融合（例如把 LSP‑DFA 的思想与端到端可学习模块结合），以提升对伪装转移、恢复动作的分辨能力。相关工作已在 2025 年出现并将被扩展 [secrss.com; joconline.com.cn]。

2. 隐私‑可解释‑高效三者联合优化成为研究热点：联邦学习 + 差分隐私 的组合能保护数据，但带来精度与可解释性损失。预计研究会更多关注“选择性私有化”（只对易泄露层加噪）、模型可分层聚合（任务层全局、底层本地）与可解释联邦聚合规则，以在保证隐私的同时保留对关键攻击类型的识别力 [zjujournals.com; jeit.ac.cn]。

3. 语义/任务导向的轻量感知与传输将进入安全检测链：受工业语义通信与深度压缩感知研究推动，未来检测系统将更多在“语义层”而非裸流量层进行预筛（只传输与检测任务相关的语义特征），从而降低边缘通信压力并加速异常响应。该方向要求建立任务级度量与对齐机制（语义一致性）[jeit.ac.cn]。

4. 基准化、流程标签与可复现实验平台的紧迫需求：当前不同论文在数据集、攻击注入与评价指标上的差异，阻碍方法比较与工程采纳。可预见社区会推动带物理/流程标签的开放 ICS/IIoT 基准集、攻击工况描述标准与统一评测套件（包括延迟/丢包扰动注入），以提高研究可复现性与产业信任度 [joconline.com.cn]。

5. 对抗鲁棒性与供给链威胁将成为重点（安全‑安全问题）：随着模型部署到边缘/厂区，模型中毒、反演与对抗样本对工业控制的潜在破坏更严重。未来研究要把鲁棒训练、可审计的模型更新（区块链/可验证日志）与运行时完整性验证结合起来，形成从检测到可信响应的闭环 [crad.ict.ac.cn; jeit.ac.cn]。

结论  
2022–2025 年间 IIoT 入侵检测研究已从“单一流量分类”向“网络—物理联合、隐私保护与边缘可部署”演化。代表性进展包括：基于事件/周期性的 DFA 类网络—物理模型（可识别伪装转移与系统恢复）、多尺度时序深度网络与图/注意力机制用于长时依赖异常、以及联邦/差分隐私技术在跨域协作中的初步工程化尝试。接下来需要在基准化评测、流程标签数据、隐私—精度—可解释三向折衷以及对抗鲁棒性方面开展系统化工作，才能将学术成果稳健地迁移到工业现场。

参考文献（所列均为真实出版/公开记录；页面或 DOI 链接用于快速查验）  
1. Sun H., Long X., Han L., et al., “Overview of anomaly detection techniques for industrial Internet of things,” Journal on Communications, 2022. [joconline.com.cn](https://www.joconline.com.cn/zh/article/doi/10.11959/j.issn.1000-436x.2022032/?viewType=HTML)  
2. Lin X., Yao Y., Hu B., et al., “A Real‑Time Anomaly Detection Method for Industrial Control Systems Based on Long‑Short Period Deterministic Finite Automaton,” (reported/summary), IEEE Internet of Things Journal, 2025. Summary page: [secrss.com](https://www.secrss.com/articles/76382)  
3. Liu L., Zhao H., Li X., et al., “Multiscale residual temporal convolutional networks‑based intrusion detection model in Internet of things,” Telecommunications Science, 2025. [telecomsci.com](https://www.telecomsci.com/zh/article/doi/10.11959/j.issn.1000-0801.2025046/)  
4. Zhao M., Peng H., Li L., et al., “Graph Attention Network and Informer for Multivariate Time Series Anomaly Detection,” Sensors, 2024. DOI: [doi.org/10.3390/s24051522](https://doi.org/10.3390/s24051522)  
5. Wang L., Liu X., Li J., Feng Z., “Network intrusion detection method based on federated learning and spatiotemporal feature fusion,” Journal of Zhejiang University (Engineering Science), 2025. [zjujournals.com](https://www.zjujournals.com/eng/article/2025/1008-973X/20250611.shtml)  
6. Mothukuri V., Khare P., Parizi R. M., et al., “Federated‑learning‑based anomaly detection for IoT security attacks,” IEEE Internet of Things Journal, 2022. DOI: [doi.org/10.1109/JIOT.2021.3077803](https://doi.org/10.1109/JIOT.2021.3077803)  
7. Dong P., Jia J., Zhou F., Wu Q., “Differentially Private Federated Learning Based Wideband Spectrum Sensing for the Low‑Altitude UAV Swarm,” Journal of Electronics & Information Technology (JEIT), 2025. [jeit.ac.cn](https://jeit.ac.cn/cn/article/doi/10.11999/JEIT241042?viewType=HTML)  
8. Zhang M., Ma X., Yang Y., et al., “Industrial IoT intelligent perception‑transmission‑control fusion: key technologies and future outlook,” JEIT, 2025. [jeit.ac.cn](https://www.jeit.ac.cn/cn/article/doi/10.11999/JEIT250305)  
9. Ren J., Zhang Y., Zhang B., Li S., “Classification Method of Industrial Internet Intrusion Detection Based on Feature Selection,” Yanshan Univ. / CRAD repository (method paper, 2021). [crad.ict.ac.cn](https://crad.ict.ac.cn/fileJSJYJYFZ/journal/article/jsjyjyfz/HTML/2022-05-1148.shtml)  
10. Wang Hangyu, Lü Fei, Cheng Yuliang, Lü Shichao, Sun Degang, Sun Limin, “A Review of Zero Trust Security in Industrial Internet,” CRAD/ICT (2025 review). [crad.ict.ac.cn](https://crad.ict.ac.cn/article/doi/10.7544/issn1000-1239.202440840?viewType=HTML)  
11. McMahan B., Moore E., Ramage D., et al., “Communication‑efficient learning of deep networks from decentralized data,” AISTATS (FL foundational paper), 2017. [mlr.press](https://proceedings.mlr.press/v54/mcmahan17a.html)  
12. Dwork C., Roth A., “The Algorithmic Foundations of Differential Privacy,” Now Publishers / monograph, 2014. DOI: [doi.org/10.1561/0400000042](https://doi.org/10.1561/0400000042)  
13. UVaydov D., D’Oro S., Restuccia F., et al., “DeepSense: Fast wideband spectrum sensing through real‑time in‑the‑loop deep learning,” IEEE INFOCOM 2021. DOI: [doi.org/10.1109/INFOCOM42981.2021.9488764](https://doi.org/10.1109/INFOCOM42981.2021.9488764)  

（注：文中对 2025 年新工作的描述基于公开论文/会议摘要与权威期刊报道/期刊网站的可验证资料；部分工程验证结果为作者在公开文献或项目页披露的数据摘要，读者如需复现请参照原始论文与开源实现。）