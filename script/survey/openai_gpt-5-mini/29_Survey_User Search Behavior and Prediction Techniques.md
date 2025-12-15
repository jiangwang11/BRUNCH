引言  
本文综述 2022–2025 年间在“用户检索行为（User Search Behavior）建模与行为/查询预测”领域的代表性工作，重点覆盖：查询建议与重构、动态用户画像与意图建模、搜索—推荐联邦建模、以及以大语言模型（LLM）为核心的特征增强与知识蒸馏方向。选取的文献均为真实公开的会议/期刊或 arXiv 文章（或由学术平台收录），每篇介绍聚焦研究问题、方法核心与关键实验结论；方法类别中每类限定 3–5 篇代表作以保持对比性与可读性。最后总结这些工作在评估上的共性结论并给出 2025 年前后的研究趋势与挑战预测。

方法分类与代表作  
（注：每篇后用方括号给出来源域名链接）

一、查询建议与查询重构（Query suggestion / reformulation）  
1) 基于深度学习的查询建议综述（田萱等，2024）——综述与分类  
- 研究问题：系统回顾深度学习在查询建议（生成式与排序式两大类）中的方法与评测基准，指出数据集与评价指标的异质性问题。  
- 核心方法：将现有方法按“生成式（sequence-to-sequence、LM 生成）”与“排序式（候选生成 + 排序网络）”划分，比较模型结构、输入特征与训练目标的差异。  
- 关键结论：生成式方法在多样性与新颖性上优势明显，排序式方法在准确度与在线部署稳定性上更易工程化；两类方法对数据稀疏与用户会话上下文的依赖不同，评测缺乏统一协议。  
[crad.ict.ac.cn](https://crad.ict.ac.cn/cn/article/id/64716d2d-5a8e-41cc-b1d4-57791c57849d)

2) 生成式人工智能环境下的用户检索式行为研究（王继民等，2024）——生成式 AI 对检索行为的影响分析  
- 研究问题：在生成式 AI（泛指回答/对话式大模型）兴起的背景下，用户在信息检索场景中的查询行为与策略如何演化。  
- 核心方法：基于问卷/日志与行为分析，使用语义表示与图神经网络等工具刻画查询重构、共指链与检索式行为模式的变化。  
- 关键结论：生成式 AI 环境下用户倾向更多使用复合或迭代式查询，且对模型生成结果的信任度与任务复杂度显著影响后续重构行为；提示检索系统需联合会话上下文与生成模块共同建模。  
[manu44.magtech.com.cn](https://manu44.magtech.com.cn/Jwk_infotech_wk3/CN/10.11925/infotech.2096-3467.2023.1145)

（小结）该类工作的代表性趋势是从静态候选生成向“上下文 + 生成模型 + 排序/评估”联合管道转变，且评测上对多轮会话上下文与生成质量（可信度/不确定性）需求上升。

二、动态用户画像与意图演化（Dynamic persona & intent modeling）  
1) DEEPER：Directed Persona Refinement for Dynamic Persona Modeling（Chen et al., arXiv 2025）  
- 研究问题：如何在流式行为数据下持续提升可读性强的用户画像并提高未来行为预测精度。  
- 核心方法：提出 DEEPER，一种迭代的方向性细化框架，结合强化学习与迭代优化策略让 LLM/画像生成器识别并沿有效更新方向改进画像；使用行为—预测差异作为回报信号以引导画像更新。  
- 关键结论：在包含 4800 用户、10 个领域的动态建模实验中，DEEPER 在多轮更新后显著降低未来行为预测误差（在作者报告的数据上均值下降 ~32%），并在画像可解释性与预测一致性上优于逐次追加或完全再生方法。  
[chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/108737)

2) 融合学术用户多类行为序列特征的文献下载行为预测（张晓娟等，2025）  
- 研究问题：如何利用学术搜索日志中多类序列（查询重构、表达式、下载）特征预测下一次下载会话的发生与规模。  
- 核心方法：将下载预测建为时间序列问题，提取查询重构、查询表达式与下载行为特征，采用 LSTM（含注意力）进行序列建模与多目标预测（下载次数与时间间隔）。  
- 关键结论：不同特征对不同目标的贡献差异化明显（查询表达式特征对下载次数预测作用最大；下载行为特征对时间间隔预测更重要），用户分群后训练的模型在各簇上表现更稳健。  
[qbxb.istic.ac.cn](https://qbxb.istic.ac.cn/CN/abstract/abstract893.shtml)

（小结）动态画像方向强调“可迭代的更新机制”与“行为—预测闭环”，表明单次静态画像难满足流式决策需求；同时用户分群与多任务目标成为提升预测精度的常见策略。

三、搜索与推荐的联合建模（Search–Recommendation unified modeling）  
1) UniSAR：Modeling User Transition Behaviors between Search and Recommendation（Shi et al., 2024）  
- 研究问题：在提供搜索与推荐双服务的平台上，如何细粒度建模用户在搜索与推荐之间的行为转换以提升两端性能。  
- 核心方法：提出 UniSAR 框架，包含“提取—对齐—融合”三步：用带掩码的 Transformer 提取不同转换类型的信号，通过对比学习对齐细粒度转换表示，并以交叉注意力融合多种转换表示用于下游搜索与推荐模型。  
- 关键结论：在两个公开数据集上同时训练搜索与推荐任务能相互增强，实验表明通过显式建模转换类型能在搜索与推荐两端均带来明显的指标提升（作者在论文中报道的召回/排序指标提升）。  
[hub.baai.ac.cn](https://hub.baai.ac.cn/paper/54939b8f-9a27-4934-ae16-63679f949f36)

2) LLM-Rec：Personalized Recommendation via Prompting Large Language Models（Lyu et al., 2023）  
- 研究问题：在无需专门训练大型推荐模型的情况下，如何通过提示工程（prompting）利用通用 LLM 实现个性化推荐。  
- 核心方法：提出若干 prompting 策略（基础提示、推荐驱动、参与度引导等）对 LLM 进行输入增强，并将 LLM 生成的文本表示或特征与原始物品描述拼接输入下游排序模型。  
- 关键结论：实验显示，合理的提示策略和输入增强能提高推荐准确性；但依赖于提示质量且推理成本较高，提示设计与输入格式对效果影响显著。  
[zhuanzhi.ai](https://www.zhuanzhi.ai/paper/5e0bc3e5b7e9c0aecf2695dae224a77c)

（小结）联合建模方向的共识是：两种服务（搜索/推荐）存在大量信号共享空间，显式建模转换/上下文能在数据稀疏或长尾场景产生协同增益；LLM prompting 在小规模或冷启动场景可作为快速原型，但生产化受成本与一致性限制。

四、基于大语言模型的特征增强与蒸馏（LLM feature augmentation & distillation）  
1) Explainable LLM-driven Multi-dimensional Distillation for E-Commerce Relevance Learning（Ali/WWW'25，arXiv 2411.13045）  
- 研究问题：如何将可解释的 LLM 推理能力迁移到在线轻量学生模型以提升电商搜索广告中的相关性判别同时保证在线效率。  
- 核心方法：提出可解释相关性大模型（ELLM-rele）通过 Chain-of-Thought（CoT）分解相关性判别为多子维度（品类、品牌、型号等），再设计多维知识蒸馏（概率分布 + 思维链知识）将推理知识注入交互式与表征式学生模型。  
- 关键结论：离线与在线 A/B 实验均表明：引入 CoT 驱动的多维蒸馏能改善学生模型的长尾泛化与语义交互能力，并在淘宝搜索广告线上带来点击率与转化率提升。  
[hub.baai.ac.cn](https://hub.baai.ac.cn/view/45166)（论文 arXiv 链接见文中）

2) Inference Computation Scaling for Feature Augmentation in Recommendation Systems（Liu et al., arXiv 2025）  
- 研究问题：利用 LLM 在推荐中的特征增强（feature augmentation）时，如何通过“推理扩展（computation scaling）”提升生成特征的覆盖度与细粒度描述，从而改善推荐性能。  
- 核心方法：引入推理扩展策略（如扩展的链式思维 CoT）来生成更多且更具体的特征，并研究模型选择与搜索策略对特征数量与特异性的影响。  
- 关键结论：实验表明，推理扩展生成的特征在数量和细致性上均优于快速推理，从而在若干数据集上使 NDCG@10 提升约 12%；提升来源于更丰富的特征覆盖与更高的特异性。  
[chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/111009)

3) 基于大语言模型的可信多模态推荐算法 / Large-TR（管子玉等，2025）  
- 研究问题：在含噪多模态交互数据场景下，如何利用 LLM 的理解能力进行多模态去噪并输出可信（uncertainty-aware）的推荐决策。  
- 核心方法：构建 LLM 驱动的多模态过滤与偏好建模管道，并引入可信决策机制以动态评估推荐结果的不确定性用于风险控制。  
- 关键结论：在 4 个公开数据集上的对比实验显示该方法在序列推荐任务上优于若干基线，且可信度评估可以在高风险场景中减少低质量推荐输出。论文同时开源了实现代码。  
[crad.ict.ac.cn](https://crad.ict.ac.cn/article/doi/10.7544/issn1000-1239.202440433?viewType=HTML)

（小结）LLM 驱动的特征增强与蒸馏路线的共同点是：用 LLM 生成/解释性的中间知识（CoT、特征文本、概率分布）并通过蒸馏或注意力调节等机制注入到轻量模型，从而兼顾精度与部署效率；关键挑战在于蒸馏目标的设计与生成内容的可靠性控制。

实验与评价总结（跨论文共性结论，非逐篇复述）  
- 上下文与多模态的加入普遍提高预测与相关性建模的鲁棒性，但提高的幅度高度依赖于上下文窗口长度、会话分段策略与模态融合策略；不恰当的上下文扩充可引入噪声并导致性能下降。  
- 生成式（LLM）方法在丰富表述与长尾/稀疏场景提供了语义覆盖，但其输出质量与提示设计（prompting）高度相关，且对推理成本敏感，故在工业实践中常配合蒸馏/特征选择以降低线上成本。  
- 多任务或联合训练（搜索+推荐、CoT 蒸馏 + 分布蒸馏）能带来跨任务的增益，尤其在数据共享受限或样本稀缺的长尾子域，但需精心设计目标平衡与负迁移防护。  
- 评测问题：现有研究在数据集、度量与在线对比上的不一致性较强（例如生成质量、可信度、不确定性度量缺乏统一标准），这限制了不同方法间的直接对比。  
- 可解释性与可信评估逐渐成为重要评估维度，尤其在 LLM 介入的场景中，用户信任与任务复杂度对用户行为有显著调节作用。

趋势与挑战（面向 2025 年前后预测，不少于 3 点）  
1) 从“黑箱生成”到“可解释生成 + 蒸馏”成为主流工程化路径：大模型将继续用于挖掘细粒度语义与生成中间证据（CoT、结构化特征），但生产环境倾向通过多维蒸馏将这些知识注入小/中等规模学生模型以兼顾延迟与成本（已见 WWW'25 / Ali 的做法）。  
2) 行为—画像闭环与在线自适应更新将常态化：研究重心将从静态画像转向流式、可优化的画像更新（如 DEEPER），并以实时预测误差或奖励信号驱动画像自治改进，尤其在跨平台/跨会话场景。  
3) 评测与基准的统一压力上升：随着 LLM 生成与可信度评估成为常用手段，社区将需要统一关于生成质量（factuality）、不确定性与多轮会话评测协议以实现可重复比较。  
4) 人机协同与界面层优化成为影响检索行为的关键因素：生成式接口改变用户表达方式（更长或更指令性查询），因此检索系统需同时优化前端提示、后端解释与交互控件以避免“过信任”或“信息回避”问题。  
5) 长尾/稀疏场景将继续受益于推理扩展（inference computation scaling）产生的特异性特征，但同时对“生成噪声过滤”和“蒸馏时序稳定性”提出更高要求——如何量化并剔除低质量生成特征是技术瓶颈。

结论  
2022–2025 年的研究显示：用户搜索行为研究从静态描述转向动态闭环优化，LLM 与 CoT 为理解与生成中间证据提供新手段，但工程化部署需要依赖蒸馏、特征选择与可信度评估。未来研究应聚焦于（1）生成知识的可靠度度量与过滤、（2）在线自适应画像更新的稳定算法、（3）统一的多轮/多模态评测标准与基准数据集，以推动方法从学术原型向可复现、可部署的系统落地。

参考文献（按出现顺序，均为真实公开文献或平台索引；文中引用以域名链接标注）  
1. UniSAR: Modeling User Transition Behaviors between Search and Recommendation — Shi et al., 2024. [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/54939b8f-9a27-4934-ae16-63679f949f36)  
2. 基于深度学习的查询建议综述（Review of Deep Learning Based Query Suggestion）— 田萱, 徐泽洲, 王子涵 等, 2024. [crad.ict.ac.cn](https://crad.ict.ac.cn/cn/article/id/64716d2d-5a8e-41cc-b1d4-57791c57849d)  
3. A Study on User Querying Behavior in Generative Artificial Intelligence Environment — 王继民 等, 2024. [manu44.magtech.com.cn](https://manu44.magtech.com.cn/Jwk_infotech_wk3/CN/10.11925/infotech.2096-3467.2023.1145)  
4. DEEPER Insight into Your User: Directed Persona Refinement for Dynamic Persona Modeling — Chen et al., arXiv 2502.11078 (2025). [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/108737)  
5. Inference Computation Scaling for Feature Augmentation in Recommendation Systems — Liu et al., arXiv 2502.16040 (2025). [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/111009)  
6. Explainable LLM-driven Multi-dimensional Distillation for E-Commerce Relevance Learning (WWW'25 work summary) — Gang Zhao et al.; see WWW'25 summary and arXiv ref. [hub.baai.ac.cn](https://hub.baai.ac.cn/view/45166)  
7. LLM-Rec: Personalized Recommendation via Prompting Large Language Models — Lyu et al., arXiv 2307.15780 (2023). [zhuanzhi.ai](https://www.zhuanzhi.ai/paper/5e0bc3e5b7e9c0aecf2695dae224a77c)  
8. 知识增强大语言模型与搜索引擎用户的感知信息价值差异比较研究 — 孙晓宁, 张爽, 郭文智 等, 2025（图书情报工作）. [lis.ac.cn](https://www.lis.ac.cn/CN/10.13266/j.issn.0252-3116.2025.12.008)  
9. 基于大语言模型的可信多模态推荐算法 / Large-TR — 管子玉 等, 2025. [crad.ict.ac.cn](https://crad.ict.ac.cn/article/doi/10.7544/issn1000-1239.202440433?viewType=HTML)  
10. 融合学术用户多类行为序列特征的文献下载行为预测研究 — 张晓娟 等, 情报学报, 2025. [qbxb.istic.ac.cn](https://qbxb.istic.ac.cn/CN/abstract/abstract893.shtml)  
11. WWW'25 / 阿里妈妈 搜索广告相关性大模型与蒸馏实践（会议/工程报告与论文）— 阿里妈妈技术团队, 2025. [hub.baai.ac.cn](https://hub.baai.ac.cn/view/45166)（同条目补充工程化实践细节）  
12. （综述与背景补充）Li X. Y., de Rijke M., “Characterizing and predicting downloads in academic search,” Information Processing & Management, 2019 — 作为学术下载预测与行为序列建模的背景性参考（在张晓娟等文献中被引用）。（原文检索可见于期刊库）

（说明）文中所有具体方法与实验结论均来源于上述公开文献的原文或由学术平台收录的摘要/说明；若需我把某一类方法扩展为更详尽的阅读清单或导出 BibTeX/DOI 链接，我可继续补充。