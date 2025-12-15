引言  
近年来大规模语言模型（LLMs）因其强大的语义理解与推理能力被广泛引入推荐系统研究，研究路线呈现出从“用LLM直接做推荐（判别/生成）”到“用LLM增强特征/知识/交互数据并与传统协同模型融合”的转变。本文针对 2022–2025 年的代表性工作做凝练性综述，按方法类别挑选每类 3–5 篇最具代表性的论文，逐篇概述其研究问题、方法要点与关键实验结论，并在实验总结与趋势预测中给出跨论文的共同发现与未来研究方向。所有引用均为公开论文或预印本（顶会/期刊/arXiv 等），并在参考文献列出原文链接。

方法分类与代表作  
（说明：每篇 4–6 句，突出研究问题、核心方法、关键实验结论；每类最多 3–5 篇）

A. 提示 / 输入增强（Prompting / Input Augmentation）——将 LLM 用于生成增强的文本输入或自然语言描述以改进下游推荐模型  
1) LLM-Rec: Personalized Recommendation via Prompting LLMs (Lyu et al., 2023).  
- 研究问题：评估通过不同提示策略（basic / recommendation-driven / engagement-guided / 组合）用 LLM 增强文本对个性化推荐性能的提升。  
- 核心方法：以提示为中心的输入增强框架（LLM-Rec），将 LLM 生成的重写/摘要/特征聚合文本与原始内容描述拼接后输入常规模型。  
- 关键结论：系统性实验表明，经提示增强的文本能显著改善内容型推荐的召回与排序，且推荐驱动 + 参与指导的组合效果最佳；论文同时分析了不同提示设计对表现的影响[ zhuanzhi.ai ].  

2) LLMRec: LLM-driven Graph Augmentation (Wei et al., 2023).  
- 研究问题：解决交互稀疏性与低质量辅助信息问题，探索用 LLM 进行图结构增强的有效性。  
- 核心方法：三类图增强策略（强化用户-物品边、增强物品属性语义、从文本角度分析用户节点），并设计去噪机制保障增强数据质量；增强后与协同模型联合训练。  
- 关键结论：在多个基准上，LLM 驱动的图增强能提高稀疏环境下的推荐效果；去噪步骤对稳定性与鲁棒性贡献明显[ hub.baai.ac.cn ]。  

3) Chat-REC: Interactive & Explainable LLM-augmented Recommender (Gao et al., 2023).  
- 研究问题：增强推荐系统的交互性与可解释性，探索将用户档案与历史交互以 prompt 注入 LLM 以实现会话式推荐。  
- 核心方法：把用户画像与交互序列转换为 prompts，利用 LLM 的 in‑context learning 做偏好推断并产出解释性推荐（可用于零样本/冷启动）。  
- 关键结论：实验证明基于提示的 Chat-REC 在 top-k 推荐与零样本评分预测上具优势，并显著提升可解释性与跨域迁移能力[ zhuanzhi.ai ]。

B. 知识图谱 / 语义建模增强（LLM as KG / Knowledge Augmenter）——用 LLM 将结构化知识图谱“语言化”以获得高质量语义表示  
1) KGLM: LLM-enhanced Knowledge Graph Recommender for E‑commerce (Wang et al., 2025).  
- 研究问题：电商场景下 KG 不完备、多跳传播的效率/过平滑问题，以及如何用 LLM 改善 KG 的语义表达以提升冷启动/长尾推荐。  
- 核心方法：将商品/用户的局部 KG 子图转写为自然语言提示并输入预训练 LLM（DeepSeek‑V2），离线生成语义描述并用句向量模型嵌入后与 ID 嵌入对齐，最终在 LightGCN 上训练。  
- 关键结论：在 MovieLens 等基准与消融实验上，KGLM 在 Recall/NDCG 上优于多种 KG 增强基线；二阶提示与物品侧语义贡献最大，且离线语义缓存有利于工程化部署[ pdf.hanspub.org ]。

2) LREF: LLM‑based Relevance Framework for E‑commerce (Tang et al., JD.COM, 2025).  
- 研究问题：电商检索/相关性评估中如何把 LLM 用作判别器并解决其偏差与泛化问题以带来线下/线上收益。  
- 核心方法：三阶段框架（监督微调 SFT + 多链思维 Multi‑CoT 调优 + 去偏的直接偏好优化 DPO），并在大规模真实数据与线上 A/B 中验证。  
- 关键结论：线下与在线指标均显著提升，且通过 DPO/多链思维可缓解 LLM 的过度乐观召回偏差[ chatpaper.com ].

3) Large‑TR: LLM‑based Trusted Multi‑Modal Recommendation (Yan et al., 2025).  
- 研究问题：多模态（文本+图像等）用户生成内容含噪，如何用 LLM 提高多模态推荐的可信度与不确定性评估。  
- 核心方法：以 LLM 做多模态文本理解与噪声过滤，结合不确定性评估机制（可信决策模块）对高风险场景下的推荐结果做动态控制。  
- 关键结论：在四个公开数据集上，提出方法在噪声场景下的精确性与稳健性优于若干基线，并更好地支持高风险场景下的拒绝/回退策略[ crad.ict.ac.cn ]。

C. 表征学习与协同信息保留（Representation / Embedding Fusion）——如何将 LLM 的语义向量与协同 ID/图嵌入有效融合并解决协同信号衰减问题  
1) Representation Learning with LLMs for Recommendation (RLMRec, Ren et al., The Web Conference 2024).  
- 研究问题：直接用 LLM 表征替代或融合传统协同嵌入时，如何保持推荐任务中必要的协同信号。  
- 核心方法：设计把预训练 LLM 生成的文本语义与协同 ID 嵌入对齐的表示学习流程，并探索不同融合策略（投影/适配器/对比训练）。  
- 关键结论：在 WebConf 的实证中，语义增强在冷启动有显著贡献，但需要显式对齐机制以避免下游协同性能下降（强调语义与协同的权衡）[ doi.org ]。

2) FreLLM4Rec: Preserving Collaborative Frequency Components (Wang et al., 2025 arXiv).  
- 研究问题：预训练 LLM 在层次传播过程中存在“谱内低频协同信号衰减（Intra‑Layer Spectral Attenuation）”，导致基于 LLM 的推荐忽视协同频率成分。  
- 核心方法：提出谱角度的两阶段处理——先用全局图低通滤波器净化嵌入，再通过时间频率调制（TFM）层层保留协同信号；提供理论与频域视角的分析。  
- 关键结论：在四个基准上，FreLLM4Rec 显著缓解了协同信号衰减，并在 NDCG@10 等指标上对比最优基线有可观提升，证明保护频域协同成分对 LLM‑based 推荐至关重要[ chatpaper.com ]。

3) Beyond studies evaluating LLM 表征：若干工作提出“轻量投影/Adapter + 冻结 LLM 语义向量”的实用范式，用以降低训练成本并避免语义向量被下游梯度破坏（见 KGLM 的设计与 RLMRec 的对齐讨论）[ pdf.hanspub.org; doi.org ]。

D. 交互式/可解释与工程化部署研究（Conversational / Explainable / System Deployment）  
1) Is ChatGPT a Good Recommender? (preliminary empirical studies, 2023).  
- 研究问题：评估直接把 ChatGPT/通用 LLM 用作推荐器在准确性、可解释性与使用便利性上的表现与限制。  
- 核心方法：基于问答式提示构建推荐任务实验，比较 ChatGPT 输出与传统协同/内容基线在若干数据集上的 top‑k 性能。  
- 关键结论：LLM 在知识丰富与可解释性方面优于纯协同模型，但在严格的排序精度与高并发在线延迟约束下存在明显不足，提示需要将 LLM 用作增强而非完全替代[ zhuanzhi.ai ]。

2) 系统与工程实践类工作（工业框架与在线 A/B 研究，如 LREF/JD 的 LLM 工程化部署），强调离线语义缓存、提示稳定化、多阶段微调与偏差校正是实现商业化落地的关键（见 LREF 的 SFT+Multi‑CoT+DPO 组合设计）[ chatpaper.com ]。

实验与评价总结（跨论文的共性结论）  
- 语义增强能补足结构化/ID 表征的语义稀疏性：多数工作（KGLM、RLMRec、LLM‑Rec、LLMRec）一致发现，将 LLM 生成的语义描述或文本嵌入作为额外特征能改善冷启动与长尾项目的召回能力。相关性强但稀疏的项目受益尤为明显[ pdf.hanspub.org; zhuanzhi.ai; hub.baai.ac.cn ]。  
- 协同信号易被 LLM 传播/转换过程弱化：多篇研究（RLMRec、FreLLM4Rec）发现未经处理直接把协同 ID 嵌入或交互序列输入 LLM，随着层深会出现低频协同成分衰减，导致排序性能下降，因此需要显式保留/校正策略（投影、频域滤波、Adapter）[ chatpaper.com; doi.org ]。  
- 噪声与鲁棒性问题受重视：将 LLM 应用于多模态/UGC 数据时（Large‑TR、LLMRec），生成/增强的数据可能包含噪声或偏差，去噪机制（隐式反馈剪枝、置信门控、不确定性评估）对上线稳定性贡献显著[ crad.ict.ac.cn; hub.baai.ac.cn ]。  
- 成本/延迟与工程化折衷：工业级实验（LREF）表明完全在推理时调用 LLM 难以满足大规模在线推荐的延迟/成本约束，因而“离线生成语义向量 + 在线轻量融合”的范式最常见且更可实用化[ chatpaper.com; pdf.hanspub.org ]。  
- 评价协议差异影响结论可比性：论文在全排序 vs 负采样评测、是否包含在线 A/B 等方面差异大，跨工作比较需谨慎——尤其是 LLM 输出的可解释性/用户感受指标常不体现在单一的 NDCG/Recall 度量中[ pdf.hanspub.org; zhuanzhi.ai ]。

趋势与挑战（2025 年前后真实可验证的研究走向与挑战，至少三点）  
1) 协同‑语义联合谱方法成为必需：基于频域/谱分析的工作（如 FreLLM4Rec）揭示了 LLM 层内对协同频率成分的系统性衰减；未来研究将更多采用谱滤波、TFM、局部图傅里叶等方法来在网络内部显式保留协同低频成分，同时融合 LLM 的高阶语义。证据来源：2025 年提出的 FreLLM4Rec 及 RLMRec 的对齐分析表明这一方向有效[ chatpaper.com; doi.org ]。  

2) “图‑到‑文（graph‑to‑text）+ 离线语义缓存”将成为工程化范式：KGLM 与多篇工业论文（LREF、LLMRec）已实践将 KG/子图转写为文本并离线编码为语义嵌入，然后用轻量投影 / Adapter 在推荐时对齐与融合，这在成本、实时性与可解释性之间提供了可行折衷，预计此范式将在工业界进一步标准化[ pdf.hanspub.org; chatpaper.com; hub.baai.ac.cn ]。  

3) 多模态与可信决策并重（噪声感知与不确定性）：多模态 UGC 含噪、偏见与隐私风险促使研究聚焦于基于 LLM 的噪声过滤、不确定性估计与可信决策机制（见 Large‑TR），同时加强对提示/生成文本的置信度评估与可审计性设计[ crad.ict.ac.cn ]。  

4) 提示工程 + 微调（SFT/CoT/DPO）的组合策略在工业部署中会更普遍：LREF 等工业工作显示，SFT、链式思维调优与偏差校正（DPO）三阶段联合能在离线/线上同时带来收益，未来研究将更多探索如何用小样本/域适应手段稳定 prompt 生成并减少在线调用频次[ chatpaper.com ]。  

5) 评测基准需扩展：单一的离线 NDCG/Recall 无法完整反映 LLM‑增强推荐的价值（如解释性、公平性、延迟成本、在线用户行为）；因此社区会推动新的综合基准与开放数据集，包含交互延迟、生成可信度与在线 A/B 指标，以便更可比地评估 LLM‑augmented 方法（这一趋势已在 2024–2025 的工业/学术混合研究中初见端倪）[ pdf.hanspub.org; chatpaper.com ]。

结论  
2022–2025 年间将 LLM 融入推荐系统的研究已由“可行性验证”逐步进入“方法工程化与理论化”阶段。总体规律是：LLM 能显著增强语义与知识层面的表达，有助于冷启动与长尾问题，但必须通过显式对齐、谱/频域保护与去噪机制来保留协同信号并满足工程化成本约束。未来工作应在保留协同信息、降低实时成本、提高生成可信度与统一评测上投入更多精力。

参考文献（按出现顺序举 12+ 篇代表性论文或报告，均为真实公开资料）  
- Lyu, H., Jiang, S., Zeng, H., Xia, Y., Luo, J., “LLM‑Rec: Personalized Recommendation via Prompting Large Language Models,” arXiv:2307.15780. 见索引页面 [zhuanzhi.ai](https://www.zhuanzhi.ai/paper/5e0bc3e5b7e9c0aecf2695dae224a77c).  
- Wei, W., Ren, X., Tang, J., et al., “LLMRec: Large Language Models with Graph Augmentation for Recommendation,” project/paper summary at [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/c2e79d28-5734-44af-925f-59b307fa2009).  
- Gao, Y., Sheng, T., Xiang, Y., et al., “Chat‑REC: Towards Interactive and Explainable LLMs‑Augmented Recommender System,” arXiv preprint summary [zhuanzhi.ai](https://www.zhuanzhi.ai/paper/71e5a34c2f88c9c3d7f816617416b8be).  
- “Is ChatGPT a Good Recommender? A Preliminary Study,” arXiv / literature summaries; see index [zhuanzhi.ai] (相关评估实验综述页).  
- Ren, X., Wei, W., Xia, L., et al., “Representation Learning with Large Language Models for Recommendation,” The Web Conference 2024 (RLMRec). DOI: 10.1145/3589334.3645458.（会议论文/DOI 页面）[doi.org](https://doi.org/10.1145/3589334.3645458).  
- Wang, M., He, Y., et al., “Beyond Semantic Understanding: Preserving Collaborative Frequency Components in LLM‑based Recommendation” (FreLLM4Rec), arXiv 2025; paper index [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/180641).  
- Tang, T., Tian, Z., Zhu, Z., et al., “LREF: A Novel LLM‑based Relevance Framework for E‑commerce,” arXiv / industrial paper (JD.COM), overview at [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/120050).  
- Wang, Y., Zhang, W., Li, Z., “大语言模型增强的知识图谱推荐算法在电子商务中的应用与推广 (KGLM),” E‑Commerce Letters (2025). PDF at [pdf.hanspub.org](https://pdf.hanspub.org/ecl_2317091.pdf).  
- Yan, M., Xu, C., Huang, H., et al., “基于大语言模型的可信多模态推荐算法 (Large‑TR),” CRAD/ICT 2025 (期刊/会议页面) [crad.ict.ac.cn](https://crad.ict.ac.cn/article/doi/10.7544/issn1000-1239.202440433?viewType=HTML).  
- Ye, Y., et al., “基于大语言模型的双视角多级跨模态推荐 (DPRec),” CRAD/ICT 2025（方法与实验）[crad.ict.ac.cn](https://crad.ict.ac.cn/article/doi/10.7544/issn1000-1239.202550040?viewType=HTML).  
- Fan, W., Zhao, Z., Li, J., Liu, Y., Mei, X., “Recommender Systems in the Era of Large Language Models (LLMs),” IEEE Trans. on Knowledge and Data Engineering (survey / TKDE 2024), see IEEE Xplore entry [ieeexplore.ieee.org](https://ieeexplore.ieee.org/abstract/document/10506571).  
- Wu, L., Zheng, Z., Qiu, Z., et al., “A Survey on Large Language Models for Recommendation,” (survey article referenced in multiple works), DOI / Springer entry [doi.org](https://doi.org/10.1007/s11280-024-01291-2).  
- 其他工程化/综述与实现参考：LLM‑Rec 中文技术解读与实践笔记（开发者社区/技术博客）[cloud.tencent.cn](https://cloud.tencent.cn/developer/article/2326791?policyId=1004)。  

（注：上列引用包含会议论文、arXiv 预印本与期刊文章；文内方法与结论均基于上述公开论文/报告的实验与论述，文中对比与总结尽量以论文给出的度量与消融结论为依据。）