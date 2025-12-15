引言  
多标签学习（multi-label learning）在信息检索、图像理解、文本分类与极端标签体系等场景持续快速发展。近三年（2022–2025）研究的主线可概括为：更精细的损失/优化设计以应对正负不平衡与误标（loss-level）；文本/图像与标签的联合嵌入或注意力机制以提升标签判定的判别性（representation-level）；基于图/层次结构的方法用于显式建模标签间相关性（structure-level）；以及将极端/层次多标签问题转为生成或多尺度学习问题（extreme/hierarchical）。下文按方法类别对 2022–2025 年代表性工作作精炼、可复现的综述（每篇 4–6 句，突出问题、方法、实验结论）。

方法分类与代表作

A. 损失与训练策略（处理正负不平衡与误标）  
- Asymmetric Loss (ASL) — IC C V/arXiv (Alibaba-MIIL, 2021) [blog.csdn.net]  
  问题：多标签（尤其图像）中正样本稀少、负样本过多且存在漏标／误标，导致训练被大量简单负样本主导。  
  方法：提出不对称聚焦（γ+、γ−）与概率偏移（p_m = max(p−m,0)）两段机制，分别对正负样本采用不同的聚焦指数并对极易负样本做硬丢弃。  
  实验：在 MS-COCO、Pascal-VOC、NUS-WIDE、Open Images 等多标签基准上，ASL 在 mAP/OF1 等指标上显著优于交叉熵与标准 focal loss，且对标签漏标鲁棒。  
  结论：将“软聚焦 + 硬阈值”结合能同时降低简单负样本影响与抑制误标带来的梯度噪声。  

- ZLPR: zero-bounded log-sum-exp & pairwise rank-based loss — arXiv (2022) [zhuanzhi.ai]  
  问题：文本/多标签分类中标签数量不确定与标签间相关性的建模问题；期望结合 BR/LP/排序损失优点。  
  方法：提出 ZLPR 损失，以 log-sum-exp 的零下界与成对排序思想同时约束正负对，支持不确定目标标签数并保留标签相关性影响。  
  实验：在若干多标签基准上，ZLPR 在多种评价指标上优于二元交叉熵与传统排序损失，同时在计算复杂度上接近 BR。  
  结论：设计对标签数不敏感且能编码标签相关性的损失，有助于提高多标签场景的一致性预测。  

B. 文本/标签联合嵌入与多粒度注意力（representation-level）  
- MIRE: Multi-granularity Information Relations Enhancing (Li et al., Journal of Software, 2023) [jos.org.cn]  
  问题：多标签文本分类中缺乏多粒度（文档级/词级）交互与标签约束性关系利用。  
  方法：文本-标签联合嵌入输入 BERT，构建两级分类模块（文档级浅层注意、词级深层注意）并辅以标签约束性匹配（LCRM）模块；损失为加权 BCE + 辅助分类。  
  实验：在 AAPD、LAIC、医疗问句等数据集上，MIRE 在 Micro/Macro-F1 及 nDCG@k 上超越多种基线（包括 BERT 变体与基于注意力的方法）；消融显示联合嵌入与 LCRM 均贡献明显。  
  结论：在 BERT 基础上并行设计多粒度注意力＋显式标签约束，能在文本多标签任务上同时提高局部与全局匹配精度。  

- 融合注意力机制的多标签文本分类 (Gong et al., CSA, 2024) [pdf.hanspub.org]  
  问题：传统方法忽略标签相关性与文本深层语义；实务中需兼顾多维信息源。  
  方法：提出并行融合注意力（基于 Query/Key/Value 点积）将文本语义表示与标签感知表示并行融合，并以加权求和得到最终表示；结合标签重要性加权与多任务损失优化。  
  实验：在 Reuters-21578、RCV1-v2 上与决策树、SVM、简单注意力叠加模型比较，显示在 Precision/Recall/F1 上有系统提升（论文给出量化表）。  
  结论：并行融合不同注意力视角并用显式标签权重，有助于在传统新闻型数据集上提升标签判定的精确性与召回平衡。  

C. 图/注意力建模标签相关性（structure-level）  
- ML-M-GAT: Multi-head Graph Attention for multi-label image classification (Shi et al., CSA, 2023) [c-s-a.org.cn]  
  问题：多标签图像分类中常忽略标签共现的非对称性与语义属性。  
  方法：用 Word2Vec 得到标签语义向量，构造基于标签共现概率的有向加权图，采用多头图注意力（M-GAT）学习非对称标签注意力权重，再用该权重与图像特征融合进行分类。  
  实验：在 VOC-2007 与 COCO-2014 上，ML‑M‑GAT 在 mAP/CP/OP 等指标上均优于 ResNet101、CNN‑RNN 与若干注意力基线；实证显示利用非对称共现提高了稀有标签识别。  
  结论：显式构建基于共现（而非对称）权重的图并用多头 GAT 聚合，可以更准确地把标签互依信息引入最终分类器。  

- ML-GCN (Chen et al., CVPR 2019) [openaccess.thecvf.com]  
  问题：如何将标签语义与共现关系用于多标签识别的判别增强？  
  方法：以标签作为图节点，用图卷积网络 (GCN) 在标签语义图上学习标签向量，然后将其作为分类器权重与图像特征内积预测标签。  
  实验：在多个图像多标签数据集（MS-COCO 等）上，GCN-based 标签嵌入显著改善长尾标签的召回能力。  
  结论：把标签关系显式参数化为 GCN 可学习的表征，有利于在数据稀疏标签上实现迁移性增强。  

D. 层次 / 极端多标签：生成式与多尺度策略（extreme & hierarchical）  
- Generation model for hierarchical extreme multi-label text classification (Chen et al., CCL 2022 / ACL anthology) [aclanthology.org]  
  问题：极限（十万级）层次标签空间下如何同时编码层次信息并避免标签维度爆炸？  
  方法：将层次极端多标签作为序列生成任务，用 seq2seq（并行多头注意）编码文本并在解码端利用软约束与词表复合映射以保留层次结构，采用束搜索生成标签序列。  
  实验：在 MAG 等层次极限数据集上，生成式方法在层次一致性和层间依赖捕获上优于分块/树分类器，且在噪声标签场景下更具容错性。  
  结论：将标签序列化并在解码器注入层次软约束，是处理层次极限标注的一条可行路线。  

- MHGCLR: Multi-scale Hierarchical multi-label classification (WU et al., 2025) [html.rhhz.net]  
  问题：单一尺度特征难以同时捕捉局部与全局语义，影响层次多标签分类效果。  
  方法：融合 BERT 词向量与 Doc2Vec 句向量做多尺度特征提取，采用门控融合、Graphormer 编码层次标签树，并以对比学习增强层次特征。  
  实验：在 WOS、RCV1‑V2、NYT、AAPD 等多数据集上，MHGCLR 在层次 Micro/Macro‑F1 与作者提出的层次化指标（HMicro/HMacro‑F1）上优于多种基线。  
  结论：多尺度特征融合＋层次图编码＋对比学习可缓解层次极端分类的语义断裂与长尾问题。  

E. 其他相关/跨方法工作（补充代表性基线与机制）  
- LEAM: Joint embedding of words and labels (Wang et al., ICLR/2018 arXiv) [arxiv.org]  
  问题：文本与标签的语义不在同一嵌入空间，影响匹配。  
  方法：联合将单词与标签嵌入同一空间，通过标签注意力获得标签特定文本表示；分类器基于相似度得分。  
  实验：在多标签文本数据集上相比纯文本编码器提升了标签判定的可解释性与部分 F1 指标。  
  结论：显式联合嵌入是改善文本–标签交互的有效且计算友好方法。  

- SGM / Seq2Set / Classifier-Chain 等序列/链式方法（Nam, Yang 等；SGM 2018–2019；Seq2set）[jos.org.cn references in MIRE]  
  问题：标签间相关性建模与标签集合无序性之间的矛盾。  
  方法：将多标签视为序列生成（Seq2Seq/decoding）或链式预测，并引入集合解码或顺序无关技巧以降低顺序敏感性。  
  实验与结论：序列生成方法能捕捉复杂标签依赖，但需防范暴露偏差与过拟合标签顺序；Seq2Set/Order‑free 变体可缓解排序敏感问题。  

实验与评价总结（跨论文的共性结论，禁止逐篇复述）  
1) 损失设计的两端需求：在高度负样本多且存在漏标/误标的数据集中，单纯的样本重加权或 focal‑style 聚焦通常不足；结合对负样本的硬丢弃（概率阈值）与对困难样本的软聚焦可同时抑制噪声与保留少数正样本梯度（ASL、ZLPR 的共识）。  
2) 表示学习的双重性：联合文本/标签嵌入或多粒度注意力（word/document）能在多数文本多标签任务中提高检索式指标（nDCG@k、P@k）與 Micro/Macro‑F1，但前提是嵌入或注意力模块要有显式的标签语义或约束（MIRE、LEAM）。  
3) 标签关系显式建模能改善稀有/长尾标签召回：基于共现/语义图（有向或加权）并用 GCN/GAT 学习标签表示，能把信息从高频标签传播到低频标签，从而显著提升稀有标签的召回率（ML‑GCN、ML‑M‑GAT）。  
4) 层次与极端空间：生成式（seq2seq）和多尺度/对比学习为层次极端多标签提供了可行解——生成式利于保持层次一致性与容错，multi‑scale+Graphormer 则改善层次判别与长尾（Generation‑model, MHGCLR 的经验）。  
5) 多任务 / 多组件训练的不稳定性：联合多任务或将过多不同目标并入同一共享层，会出现梯度冲突和性能退化；因此实际系统常需用辅助损失、路由或按任务调度（见 MTL 文献）来缓解。  

趋势与挑战（2025 年前后可验证的、基于上述工作与证据的预测，至少 3 点）  
1) 更广泛的“损失+结构”协同设计：未来方法将不再单独只做损失改进或只做标签图建模，而会把不对称损失（处理误标/长尾）与标签图/层次结构耦合，通过任务/类条件化阈值与图态势感知的阈控来联合抑噪并传播信号。  
2) 生成式与判别式混合解法成为主流：对极端层次标签体系，纯判别器难以扩展，纯生成器又面临序列偏差；短期内混合架构（生成标签序列 + 判别式重排序/校验）将在实际极端系统中取代单一范式。  
3) 可解释且可控的标签交互模块：为满足下游可审计与业务约束（如法律/医学标签互斥），研究将倾向于可控图模型（可注入约束的 GAT/Graphormer）或可约束解码（软/硬约束）以保证输出的层次一致性与业务合规性。  
4) 参数高效、模块化微调成为工程常态：LoRA / Low‑rank / Adapter 等参数高效方法需与多标签特性（长尾、层次）做适配，出现按标签群/层次自适应的低秩适配器将是研究热点。  
5) 标注噪声的自监督与对比增强并行化：对缺标/漏标问题，未来更强调自监督对比信号（token/label-level）与小样本正则化的联合，以提高少样本标签的表征质量和下游判别。  

结论  
近三年（2022–2025）对多标签学习的进展显示出“损失稳健化、表示多粒度化、标签关系显式化、层次/极端问题生成化”这四条并行演进路径。实证上，ASL、ZLPR、MIRE、ML‑M‑GAT 与生成式层次方法分别在其目标子问题上给出可复现的改进；下一步研究需聚焦如何将这些方向以可控、参数高效和任务鲁棒的方式整合到端到端系统中。  

参考文献（按文中出现顺序，均为真实出版物/预印本）  
- ZLPR: A Novel Loss for Multi‑label Classification (arXiv:2208.02955) — Jianlin Su et al., 2022. [zhuanzhi.ai](https://www.zhuanzhi.ai/paper/fd09515cfd452cf42c63785c933fec66)  
- Li, F.-F., Su, P.-Z., Duan, J.-W., Zhang, S.-C., Mao, X.-L., “Multi‑granularity Information Relations Enhancing for Multi‑label Text Classification (MIRE)”, Journal of Software, 2023. [jos.org.cn](https://jos.org.cn/html/2023/12/6802.htm)  
- Shi, X.-Y., Li, S.-Y., Han, X., “Multi‑label Image Classification Based on Multi‑head Graph Attention Network and Graph Model (ML‑M‑GAT)”, Computer Systems and Applications, 2023. [c-s-a.org.cn](https://www.c-s-a.org.cn/html/2023/6/9148.html)  
- “Generation Model for Hierarchical Extreme Multi‑label Text Classification”, Chen Linqing et al., CCL 2022 (CCL proceedings / ACL anthology). [aclanthology.org](https://aclanthology.org/2022.ccl-1.60.pdf)  
- Asymmetric Loss For Multi‑Label Classification (ASL), Alibaba‑MIIL, ICCV/ArXiv 2021 (arXiv:2009.14119) — implementation & analysis summaries. [blog.csdn.net discussion & pointers to arXiv; original paper arXiv/ICCV] [blog.csdn.net](https://blog.csdn.net/weixin_43424450/article/details/147364959)  
- WU Zixuan, WANG Ye, YU Hong, “Hierarchical Multi‑label Text Classification Method Based on Multi‑scale Feature Extraction (MHGCLR)”, Journal of Zhengzhou University (Natural Science Edition), 2025. [html.rhhz.net](https://html.rhhz.net/ZZDXXBLXB/html/20250204.htm)  
- “Label Distribution Learning Based on Hierarchical Tag Structure”, Liu Kan et al., Data Analysis and Knowledge Discovery, 2024. [manu44.magtech.com.cn](https://manu44.magtech.com.cn/Jwk_infotech_wk3/CN/10.11925/infotech.2096-3467.2022.1278)  
- Gong, J., Liu, X., Fan, J., “Research on Multi‑Label Text Classification Method Based on Fusion Attention Mechanism”, Computer Science and Application, 2024 (HansPub). [pdf.hanspub.org](https://pdf.hanspub.org/csa20241412_101543424.pdf)  
- Chen, Z., Wei, X., Wang, P., et al., “Multi‑label Image Recognition with Graph Convolutional Networks”, CVPR 2019. [openaccess.thecvf.com](https://openaccess.thecvf.com/content_CVPR_2019/papers/Chen_Multi-Label_Image_Recognition_With_Graph_Convolutional_Networks_CVPR_2019_paper.pdf)  
- Wang, G., Li, C.-Y., Wang, W.-L., et al., “Joint embedding of words and labels for text classification (LEAM)”, arXiv:1805.04174 / ICLR related work, 2018. [arxiv.org](https://arxiv.org/abs/1805.04174)  
- Yang, P.-C., Sun, X., Li, W., Ma, S.-M., Wu, W., Wang, H.-F., “SGM: Sequence Generation Model for Multi‑label Classification”, COLING 2018/2019 proceedings. (sequence generation baselines cited by MIRE). [jos.org.cn references in MIRE] [jos.org.cn](https://jos.org.cn/html/2023/12/6802.htm)  
- Nam, J., Mencía, E.L., Kim, H.J., Fürnkranz, J., “Maximizing subset accuracy with recurrent neural networks in multi‑label classification”, NeurIPS 2017. (RNN sequence approaches to multi‑label) [papers: NeurIPS proceedings / arXiv]  
- Additional baseline / survey references cited in本文：XML‑CNN (Liu et al., SIGIR 2017), X‑BERT / extreme multi‑label methods, and multi‑task / loss modulation works referenced in context (详见各文献内部引用与比较表).  

（注：文内所述实验结论均来自各论文的公开结果与消融/基线比较；上文已尽量只列出 2022–2025 期间或直接相关的代表性工作，并标明出处以便复核。）