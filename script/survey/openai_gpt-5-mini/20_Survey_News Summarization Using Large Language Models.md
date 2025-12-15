引言  
随着大语言模型（LLMs）在生成与推理能力上的迅速演进，新闻摘要研究在 2022–2025 年出现了两个显著方向：一是将 LLM 直接作为端到端抽象生成器或评估器，用于少样本/提示式摘要；二是结合检索、索引或结构化表示（knowledge graph / community summaries /检索模块）来应对新闻语料的长文本、跨文档和查询导向需求。本文在 2022–2025 年时间窗内，按方法类别选取代表性工作（每类不超过 3–5 篇），对方法要点与实证结论做精炼比较，并总结实验共性、开放问题与 2025 年前后的研究趋势预测。文中仅引用公开论文/预印本与可核验出版物（参考文献列出）。

方法分类与代表作（每篇 4–6 句，突出问题 / 方法 / 关键结论）

1) 检索增强的图/社区索引与 Query-Focused Summarization（应对全语料/多文档新闻的全局查询）  
- From Local to Global: A Graph RAG Approach to Query-Focused Summarization — GraphRAG（论文，arXiv）  
  问题：传统 RAG 难以回答“针对整个语料库的全局/主题性问题（query‑focused summarization）”。  
  方法：用 LLM 提取实体/关系并构建图索引，基于社区检测（hierarchical communities）生成社区级摘要，采用 map‑reduce（并行生成社区答案 + 汇总）来扩展到百万级令牌语料。  
  关键结论：在两个 ~1M 令牌级数据集上，GraphRAG 在“全面性（comprehensiveness）”和“多样性（diversity）”指标上显著优于简单 RAG，且在低级社区摘要下可节省大量 token 成本（文中呈现不同层级的权衡）。[arxiv.org](https://arxiv.org/abs/2404.16130)（参见同题解析与实现讨论）[csdn.net](https://blog.csdn.net/qq_41185868/article/details/138982960)。  
- URaG: Unified Retrieval and Generation in Multimodal LLMs for Efficient Long Document Understanding（2025，arXiv）  
  问题：多模态 LLM 在长文档上受信息干扰与 Transformer 二次计算成本困扰，影响新闻图片/版面密集型长报道的摘要与问答性能。  
  方法：在模型内部把早期 Transformer 层作为轻量检索模块（跨模态相似性），保留 top‑k 相关页面并丢弃无关令牌，随后在深层集中生成；两阶段训练（检索预训练 + LoRA 联合微调）。  
  关键结论：在多模态长文档基准上同时提高准确性并将 FLOPs、内存与推理时间显著下降（文中报告 44–56% FLOPs 减少与峰值内存降幅）。[chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/209352)。  

2) 多‑LLM 协同生成与评估（利用多个 LLM 提升稳健性与多样性）  
- Multi‑LLM Text Summarization（arXiv 2412.15487）  
  问题：单一 LLM 在摘要质量或稳健性上受限；如何用多模型协作提升最终摘要质量且成本可控？  
  方法：提出中心化与去中心化两类多‑LLM 框架：多模型并行生成候选摘要，再由中央 LLM 或多模型投票评估并选取/迭代生成最终摘要；可做多轮生成‑评估对话以收敛共识。  
  关键结论：在 ArXiv/GovReport 等长文本基准上，多‑LLM 框架对比单模型基线有显著提升（报告平均提升幅度大幅优于单模型），且在许多情形下只用两个 LLM 与单轮评估即可获得成本/性能最优点。有关实现与消融在不同评估器与决胜模型间表现一致。[www.cnblogs.com](https://www.cnblogs.com/tunancbq/p/18687748)。  

3) LLM‑辅助的长文本抽取式/高效生成（针对单篇长新闻或多篇新闻汇总的分块 + LLM 驱动）  
- EYEGLAXS：基于 LLM 的长文本抽取式摘要框架（arXiv 2408.15801，技术报告/预印）  
  问题：直接用 LLM 生成长文本摘要易产生幻觉/事实错误；抽取式方法在长文场景中更稳健但受编码器长依赖限制。  
  方法：构建以 LLM（如 LLaMA2）为评估/选择器的抽取式管道，通过块化 + LLM 选择/排序候选句子并串联，再用较小模型或 LLM 做二次整合。  
  关键结论：在长文本抽取式基线上，利用 LLM 的检索/评分能力能在保持事实性的同时提升 ROUGE/检索相关性；但成本—延迟权衡与上下文截断策略仍是瓶颈。[blog.csdn.net（含论文链接）](https://blog.csdn.net/Yuleave/article/details/145271560)。  
- QDGenSumRT / QDGenSumRT‑style（实时查询驱动摘要的工程化框架，arXiv 2508.20559 提案）  
  问题：工业级搜索中的 Query‑Driven Text Summarization 需在低延迟下对海量检索结果生成高质量摘要。  
  方法：用大模型生成高质量蒸馏数据训练轻量化专家模型（0.1B 级），结合偏好对齐与推理优化（量化 + 前瞻解码）实现实时部署。  
  关键结论：在工业指标与在线 A/B 实验中，作者报告显著降低延迟并在 ROUGE 与用户偏好上超越生产基线；展示了模型蒸馏 + RLHF/偏好对齐在工程化环境下的可行路径。[blog.csdn.net（含 arXiv 引用）](https://blog.csdn.net/weixin_46739757/article/details/151051384)。  

4) 面向时间线与多粒度新闻摘要（动态粒度、多文档时间线构建）  
- DTELS: Towards Dynamic Granularity of Timeline Summarization（arXiv 2411.09297）  
  问题：传统时间线摘要固定粒度，无法满足用户对“粗/细”不同粒度的需求（尤其在新闻事件的演进跟踪中）。  
  方法：提出 DTELS 任务设定、数据集与评价框架（信息量、粒度一致性、事实性、连贯性四维）；比较 LLM‑based 方法与现有 TLS 方法并给出基准。  
  关键结论：基于 LLM 的方法在多粒度时间线生成上显示出有效性，但在保持信息丰富性与粒度一致性间仍难以兼顾，提示任务本身具有挑战性并需要专门的数据与评价指标。[chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/76321)。  

5) 预处理 / 事件结构与小模型 + LLM 增强的两阶段流程（提高事实性与效率）  
- “基于大模型增强的两阶段高效事件共指消解方法”（CCL/CCL2025）  
  问题：事件共指（event coreference）对新闻多文档摘要/事件聚合至关重要，但两阶段方法要么高效但性能差，要么性能好但复杂度高。  
  方法：在第一阶段用 LLM 做触发词同义聚类以提升召回，第二阶段用 LLM 生成触发词解释文本增强小判别器，并加入辅助损失引导判别器关注触发词特征。  
  关键结论：在 ECB+ 和 GVC 数据集上，在保持近似线性复杂度前提下，CoNLL F1 分别提升了若干百分点（文中报告具体提升：ECB+ +2.9，GVC +8.0），表明 LLM 增强可显著改善两阶段高效方法的精度—效率权衡。[aclanthology.org](https://aclanthology.org/2025.ccl-1.7.pdf)。  
- 经典/传统 Seq2Seq 改进（用于比较基线）——BiGRU + Attention（期刊文章，2025）  
  问题：在受限计算或无大模型资源情形下，如何提升生成式摘要模型的连贯性与信息覆盖。  
  方法：在编码器采用 BiGRU 并在解码器加入注意力机制，使用 Word2Vec 预训练词向量并在 CNN/DailyMail 数据集上训练对照。  
  关键结论：相较于传统 Seq2Seq，BiGRU+Attention 在 ROUGE‑1/ROUGE‑L 上有小幅但稳定提升（文中报告具体数值），但与 LLM 方案的事实性/多样性差距仍存在。[pdf.hanspub.org](https://pdf.hanspub.org/csa_1543819.pdf)。  

实验与评价总结（只汇总共性结论，不逐篇复述）  
- 长文本与多文档场景：所有工作均强调“分块+索引/检索/聚合”是可扩展处理百万级令牌新闻语料的实用范式；单纯扩大单模型上下文窗口并不能系统解决信息丢失与计算成本问题。  
- 事实性（faithfulness）与抽象度之间存在明确权衡：检索增强或抽取式链路在事实性上更稳健，而纯生成（端到端 LLM）在语言流畅性和抽象表达上占优；工程实践倾向于混合方案（检索 + LLM 生成/评估）。  
- 多模型与评估器的加入（如 Multi‑LLM 框架或 LLM 作为评估器）能显著提升最终摘要的稳定性与多样性，但带来额外成本；论文普遍指出“两个 LLM + 单轮评估”经常是成本—收益的折衷最优点。  
- 多粒度与任务导向评价：研究趋向在评价上超越单一 ROUGE，采用任务导向指标（信息覆盖、粒度一致性、连贯性、检索准确性、用户感知度量或 LLM‑as‑judge 评估），因为新闻摘要的用途高度依赖下游任务（舆情监测、事件跟踪、问答）。  
- 效率工程化：工业部署工作强调蒸馏、量化、推理优化（如 QDGenSumRT 所示）的重要性——在保持用户偏好/质量的同时，显著降低延迟与算力成本是可行路径。  

趋势与挑战（对 2025 年前后真实研究走向的预测，≥3 点）  
1. 混合索引‑生成范式将成主流：以图/社区索引、嵌入+检索与早期层检索（如 URaG 内部检索）为代表的“模型内/外统一检索”将被更多采纳，以在端到端训练与工程化约束间取得更好折衷。  
2. LLM 作为评估器和管道控制器常态化：LLM‑as‑judge 与多轮生成‑评估循环（Multi‑LLM）将在提高摘要稳健性和减少幻觉方面继续发挥作用，但会催生更多关于评估偏差与自信校准的研究（如何避免评估器放大模型偏误）。  
3. 以任务/用户为中心的多粒度摘要与交互式流程：新闻摘要不再仅输出单一固定粒度摘要，系统将提供可调节粒度、时间线视图与查询导向的交互式摘要界面（DTELS、GraphRAG 的思想将被产品化）。  
4. 事实性保障与检索/知识对齐成为硬指标：对新闻场景尤其重要的事实一致性检验（基于检索证据回溯、证据可视化、引用绑定）将成为新的评测基准，促使更多工作在生成时显式附带证据页面/片段。  
5. 低延迟/大吞吐的轻量化专家将系统化：工业需求促使“用大模型生成高质量训练信号，再训练/蒸馏轻量专家模型”的流水线化（QDGenSumRT 类），该方向会与模型量化、编译器优化共同推进。  
6. 多模态新闻摘要与版面/图表理解的研究爆发：随着图像/表格密集型新闻（财经、科技报道）增多，像 URaG 这类将检索与多模态对齐嵌入到模型内部的工作会快速发展，以支持跨模态证据定位与凝练。  

结论  
2022–2025 年的研究显示：单一策略不足以同时满足新闻摘要对长文本可扩展性、事实性和用户导向性的要求；检索/索引（图/社区/早期层检索）与 LLM 的协同、以及多模型评估机制，构成当前最有前景的技术栈。未来研究需把注意力集中在事实性保障、成本—性能工程化、以及面向用户的多粒度交互式摘要评价体系上。  

参考文献（按文内引用、均为公开论文/预印本或期刊/会议论文，URL 用来源域名标注便于核验；至少 12 篇）

- Graph RAG: From Local to Global: A Graph RAG Approach to Query‑Focused Summarization. arXiv:2404.16130. [arxiv.org](https://arxiv.org/abs/2404.16130)；相关解读与实现讨论见 [csdn.net](https://blog.csdn.net/qq_41185868/article/details/138982960).  
- DTELS: Towards Dynamic Granularity of Timeline Summarization. Chenlong Zhang et al., arXiv:2411.09297 (2024). [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/76321).  
- Multi‑LLM Text Summarization. arXiv:2412.15487 (2024). 综述与实现说明见 [www.cnblogs.com](https://www.cnblogs.com/tunancbq/p/18687748).  
- URaG: Unified Retrieval and Generation in Multimodal LLMs for Efficient Long Document Understanding. Yongxin Shi et al., arXiv:2511.10552 (2025). [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/209352).  
- EYEGLAXS / 长文本抽取式摘要（基于 LLM 的抽取式框架），详见 arXiv:2408.15801（论文摘要/解读）与实现讨论 [blog.csdn.net](https://blog.csdn.net/Yuleave/article/details/145271560).  
- QDGenSumRT: Leveraging Generative Models for Real‑Time Query‑Driven Text Summarization in Large‑Scale Web Search. arXiv:2508.20559 (2025). 解读见 [blog.csdn.net](https://blog.csdn.net/weixin_46739757/article/details/151051384).  
- A Comprehensive Survey on Process‑Oriented Automatic Text Summarization (survey, 2024). Hanlei Jin et al. [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/50aa243f-7dbc-48fb-a6d8-fd443bc5846a).  
- “多文档摘要研究综述”／An Overview of Research on Multi‑Document Summarization (2024)。孙海春等，期刊论文。 [manu44.magtech.com.cn](https://manu44.magtech.com.cn/Jwk_infotech_wk3/CN/10.11925/infotech.2096-3467.2022.1245).  
- Two‑stage LLM‑enhanced event coreference (CCL 2025 paper): “An Efficient Event Coreference Resolution Method Based on Two‑Stage Enhancement with Large Language Model”. CCL 2025. [aclanthology.org](https://aclanthology.org/2025.ccl-1.7.pdf).  
- BiGRU + Attention 改进 Seq2Seq（新闻摘要基线比较），Xu & Qiu, 2025（期刊）。 [pdf.hanspub.org](https://pdf.hanspub.org/csa_1543819.pdf).  
- Retrieval‑Augmented Generation (RAG) — Lewis et al., 2020 (方法学基础与早期 RAG 框架). arXiv:2005.11401. [arxiv.org](https://arxiv.org/abs/2005.11401).  
- 相关阅读/工程实践与开源实现注：GraphRAG 实现资源与社区讨论集合（若干实现与衍生工程）参见相关开源与博文汇总 [csdn.net](https://blog.csdn.net/qq_41185868/article/details/138982960) 与 community posts。  
- 其它补充材料与评测方法讨论：关于以查询为中心的评估与 LLM‑as‑judge 的方法论、社区实现与数据集详情，参见 GraphRAG 原文与随附补充材料（arXiv 链接已列）。[arxiv.org](https://arxiv.org/abs/2404.16130)。

（注：文中所列论文、预印本与期刊均可通过上述链接或 DOI 检索核验；为保持综述学术密度，本文选择在 2022–2025 时间窗内具有代表性的方向与工作进行精炼呈现，而非穷尽列举。）