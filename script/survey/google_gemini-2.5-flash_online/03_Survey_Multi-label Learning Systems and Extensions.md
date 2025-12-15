## 多标签学习系统及其扩展研究综述 (2022–2025)

### 引言

多标签学习（Multi-label Learning, MLC）是机器学习领域的一个重要分支，旨在处理一个实例可同时关联多个类别标签的问题。与传统的单标签分类不同，MLC 任务更贴近现实世界中复杂对象的描述，例如一张图片可能包含多个物体，一段文本可能涉及多个主题。近年来，随着深度学习技术的发展和大规模多模态数据的涌现，MLC 领域涌现出大量创新性工作。本综述将聚焦 2022-2025 年间 MLC 领域具有代表性的研究进展，总结其核心方法，归纳实验结论，并展望未来的研究趋势与挑战。

### 方法分类与代表作

多标签学习方法大致可分为以下几类：基于损失函数优化、基于特征与标签关系学习、基于层次结构利用以及生成式方法。

#### 1. 基于损失函数优化

此类方法主要通过设计和改进损失函数来解决多标签分类中普遍存在的标签不平衡、难易样本区分等问题。

*   **ASL: Asymmetric Loss For Multi-Label Classification** [blog.csdn.net](https://blog.csdn.net/weixin_43424450/article/details/147364959)
    *   **研究问题**: 针对多标签分类中普遍存在的正负样本严重不平衡以及负样本可能存在的误标问题。
    *   **核心方法**: 提出一种非对称损失 (ASL)，通过“不对称聚焦”对正负样本施加不同的指数衰减因子，并采用“概率偏移”通过硬阈值直接丢弃简单负样本，同时也能剔除误标记的负样本。
    *   **关键实验结论**: 在 MS-COCO、Pascal-VOC、NUS-WIDE 和 Open Images 等多个多标签数据集上取得了当时最先进的结果，显著提升了 mAP 等指标。ASL 的有效性不增加训练时间和复杂度，且易于实施。

#### 2. 基于特征与标签关系学习

这类方法致力于更有效地建模文本特征与标签之间的深层关联，以及标签自身内部的结构关系。

*   **多粒度信息关系增强的多标签文本分类 (Multi-label Text Classification with Enhancing Multi-granularity Information Relations)** [jos.org.cn](https://jos.org.cn/html/2023/12/6802.htm)
    *   **研究问题**: 现有深度学习多标签文本分类方法在特征提取时缺乏多粒度学习，并且对标签间的约束性关系利用不足。
    *   **核心方法**: 提出一种多粒度信息关系增强方法 (MIRE)。通过文本-标签联合嵌入将文本和标签映射到同一语义空间，设计文档级（浅层标签注意力）和词级（深层标签注意力）分类模块进行多粒度学习，并引入标签约束性关系匹配辅助模块。
    *   **关键实验结论**: 在 AAPD、LAIC-争议焦点识别提取、医疗公共健康问句数据集上，MIRE 在 Micro-F1、Macro-F1、nDCG@k、P@k 等主要指标上均取得了最佳效果。消融实验证明了文本-标签联合嵌入和标签约束性关系匹配模块的有效性。

*   **基于标签语义注意力的多标签文本分类 (Multi-label Text Classification Method Based on Label Semantic Information)** [jos.org.cn](https://www.jos.org.cn/html/2020/4/5923.htm)
    *   **研究问题**: 传统多标签文本分类算法多将标签视为无语义符号，未能有效利用标签本身蕴含的语义信息来指导分类。
    *   **核心方法**: 提出一种基于标签语义注意力的多标签文本分类 (LASA) 方法。利用 Bi-LSTM 获取单词隐表示和标签的词向量平均函数获得标签隐表示，通过计算单词与标签的匹配得分来学习每个单词对当前标签的重要性权重，从而为每个标签学习特定的文档表示。
    *   **关键实验结论**: 在 Kanshan-Cup、EUR-Lex 和 AAPD 数据集上，LASA 在 P@k 和 nDCG@k 等指标上均优于其他方法，尤其在尾标签问题上表现突出。热力图分析显示模型能够捕获特定标签对应的关键信息性词汇。

#### 3. 基于层次结构利用

此类方法专注于处理标签之间存在层次结构的多标签分类任务，即层次多标签分类 (Hierarchical Multi-label Classification, HMC)。

*   **ZLPR: A Novel Loss for Multi-label Classification** [zhuanzhi.ai](https://www.zhuanzhi.ai/paper/fd09515cfd452cf42c63785c933fec66)
    *   **研究问题**: 现有排序损失函数在多标签分类中未能很好地处理目标标签数量不确定以及标签间关联性问题。
    *   **核心方法**: 提出 ZLPR (zero-bounded log-sum-exp & pairwise rank-based) 损失。该损失函数能够处理目标标签数量不确定的情况，并考虑标签间的相互关系，同时设计了软版本和 KL 散度计算方法。
    *   **关键实验结论**: 在多个基准数据集和评估指标上验证了 ZLPR 的有效性，并与 Binary Relevance (BR) 和 Label Powerset (LP) 方法具有可比性，在计算复杂性上可以与 BR 方法竞争。

*   **基于多尺度特征提取的层次多标签文本分类方法 (Hierarchical Multi-label Text Classification Method Based on Multi-scale Feature Extraction)** [html.rhhz.net](https://html.rhhz.net/ZZDXXBLXB/html/20250204.htm)
    *   **研究问题**: 现有层次多标签文本分类 (HMTC) 任务中的特征提取方法普遍忽视文本局部与全局的联系，且评价指标存在不合理性。
    *   **核心方法**: 提出 MHGCLR 模型，设计多尺度特征提取模块融合 BERT 词向量和 Doc2Vec 句向量，利用 Graphormer 编码标签层次结构，并通过对比学习增强分类效果。同时提出层次 Micro-F1 和层次 Macro-F1 等新的评价指标。
    *   **关键实验结论**: 在 WOS、RCV1-V2、NYT 和 AAPD 数据集上，MHGCLR 在传统和新提出的层次评价指标上均表现出色。消融实验和分层表现实验证明了多尺度特征提取模块和模型在深层次少样本标签分类上的有效性。

*   **Generation Model for Hierarchical Extreme Multi-label Text Classification** [aclanthology.org](https://aclanthology.org/2022.ccl-1.60.pdf)
    *   **研究问题**: 层次结构极限多标签文本分类任务面临标签数量巨大、标签间层级依赖和同层相关性复杂，以及标签体系可能存在噪声的问题。
    *   **核心方法**: 将 HMTC 任务视为序列转换问题，采用基于并行多头注意力机制的生成模型。通过软约束解码和词表复合映射在解码过程中利用标签的层次结构和相关信息，并确保输出标签存在于标签体系中。
    *   **关键实验结论**: 模型在不同数据集上取得了显著性能提升，能够有效捕获标签间的上下位关系，并对极端多标签体系中的噪声具有容错能力。消融实验表明软约束解码和词表复合映射的有效性。

#### 4. 多模态与知识增强

该方向将多标签学习扩展到多模态数据，或利用外部知识提高学习效率和准确性。

*   **多模态数据的知识增强深度语义学习方法** [paper.edu.cn](https://paper.edu.cn/releasepaper/content/202503-143)
    *   **研究问题**: 在图像-文本检索等多模态任务中，数据呈现多模态、多源异构特点，传统学习方法难以高效管理和利用。
    *   **核心方法**: 提出多模态知识增强的跨模态教育大数据深度语义学习方法，将多模态知识图谱应用于跨模态检索任务，并加入模态内和模态间对比学习损失函数。
    *   **关键实验结论**: 显著提升了多模态检索任务的准确性和效率，验证了其有效性和实用性，有助于多模态数据在统一语义空间下表示学习。

### 实验与评价总结

2022-2025 年间的多标签学习研究普遍通过在公开基准数据集（如 MS-COCO, Pascal-VOC, NUS-WIDE, Open Images, WOS, RCV1-V2, NYT, AAPD 等）上进行对比实验来验证模型性能。常用的评价指标包括平均精度均值 (mAP)、Micro-F1、Macro-F1、P@k、nDCG@k。在处理层次多标签分类时，一些工作还引入了层次相关的评价指标，如层次 Micro-F1 和层次 Macro-F1，以更准确地反映模型对层级依赖的捕获能力。

总体而言，深度学习模型的引入，尤其是预训练语言模型（如 BERT）在文本任务中的应用，显著提升了多标签分类的性能。模型通过多粒度特征提取、标签语义信息利用、标签层次结构建模等方面实现了性能提升。通过消融实验，研究人员系统地验证了模型各组件的有效性。对比学习作为一种强大的自监督范式，也被广泛应用于多标签学习中，以增强模型的表示能力。此外，针对正负样本不平衡、尾标签问题以及标签噪声等固有挑战，新型损失函数和非对称处理机制展现出强大的解决能力。

### 趋势与挑战

展望未来，多标签学习领域将呈现以下趋势：

1.  **大规模与极限多标签分类的持续演进**：随着数据规模的不断扩大，处理类别数量高达数万甚至数十万的极限多标签文本分类将是重要趋势。未来的研究将需要更高效的模型架构和训练策略，以克服计算复杂性和存储限制，并能有效处理高度稀疏的标签分布和长尾问题。生成式模型、词表复合映射和软约束解码等技术将是解决这一问题的关键。
2.  **多模态融合与知识增强的深入研究**：真实世界的数据往往是多模态的。未来的 MLC 系统将更加侧重于融合图像、文本、音频、视频等多种模态信息，并利用外部知识图谱或本体论来增强语义理解和推理能力。如何有效地对异构多模态数据进行对齐、融合表征，并利用结构化知识进行约束和指导，将是核心挑战。对比学习损失函数在模态内和模态间的应用将继续发挥关键作用。
3.  **鲁棒性与可解释性的提升**：实际环境中存在大量标签噪声（如误标、漏标）和数据分布偏移，对模型的鲁棒性提出更高要求。发展能够识别和适应噪声标签、处理域迁移的 MLC 方法将是研究重点。同时，随着模型复杂性的增加，如何提高多标签分类系统的可解释性，理解模型做出决策的依据，也将成为重要的研究方向，尤其是在医疗、法律等关键应用领域。

### 结论

多标签学习作为机器学习中的重要且充满活力的领域，在 2022-2025 年间取得了显著的进展。研究人员在损失函数优化、特征与标签关系建模、层次结构利用以及多模态知识增强等方面提出了诸多创新方法。这些进展有效提升了模型在复杂真实世界任务中的表现，并为未来大规模、多模态、高鲁棒性多标签学习系统的发展奠定了基础。尽管面临数据不平衡、长尾分布和可解释性等挑战，但结合深度学习、对比学习和知识增强的解决方案预示着该领域广阔的研究前景。

### 参考文献

*   [1] Su, J., Zhu, M., Murtadha, A., Pan, S., Wen, B., & Liu, Y. (2022). **ZLPR: A Novel Loss for Multi-label Classification**. *arXiv preprint arXiv:2208.02955*. [zhuanzhi.ai](https://www.zhuanzhi.ai/paper/fd09515cfd452cf42c63785c933fec66)
*   [2] Wu, Z., Wang, Y., & Yu, H. (2025). **Hierarchical Multi-label Text Classification Method Based on Multi-scale Feature Extraction**. *Journal of Zhengzhou University (Natural Science Edition), 57*(2), 24-30. [html.rhhz.net](https://html.rhhz.net/ZZDXXBLXB/html/20250204.htm)
*   [3] Li, F., Su, P., Duan, J., Zhang, S., & Mao, X. (2023). **Multi-label Text Classification with Enhancing Multi-granularity Information Relations**. *Journal of Software, 34*(12), 5686-5703. [jos.org.cn](https://jos.org.cn/html/2023/12/6802.htm)
*   [4] Xiao, L., Chen, B., Huang, X., Liu, H., Jing, L., & Yu, J. (2020). **Multi-label Text Classification Method Based on Label Semantic Information**. *Journal of Software, 31*(4), 1079-1089. [jos.org.cn](https://www.jos.org.cn/html/2020/4/5923.htm)
*   [5] Chen, L., He, D., Xiao, Y., Liu, Y., Lu, J., & Wang, W. (2022). **Generation Model for Hierarchical Extreme Multi-label Text Classification**. *Proceedings of the Chinese Computational Linguistics (CCL)*, 671-683. [aclanthology.org](https://aclanthology.org/2022.ccl-1.60.pdf)
*   [6] Zhuo, Z., & Liang, M. (2025). **Knowledge enhancement of deep semantic learning for multimodal data**. *China Science Paper Online*, 202503-143. [paper.edu.cn](https://paper.edu.cn/releasepaper/content/202503-143)
*   [7] Liu, K., You, M., & Wei, L. (2024). **Label Distribution Learning Based on Hierarchical Tag Structure**. *Data Analysis and Knowledge Discovery, 8*(2), 44-55. [manu44.magtech.com.cn](https://manu44.magtech.com.cn/Jwk_infotech_wk3/CN/abstract/abstract5639.shtml)
*   [8] Liu, R., Liang, W., Luo, W., Song, Y., Zhang, H., Xu, R., Li, Y., & Liu, M. (2023). **Recent Advances in Hierarchical Multi-label Text Classification: A Survey**. *arXiv preprint arXiv:2307.16265*. [zhuanzhi.ai](https://www.zhuanzhi.ai/paper/c9a665a1f4cad6f1705fd734cf38d1e9)
*   [9] Lin, D., Li, Q., Chen, Z., Zhong, F., & Li, L. (2024). **Research advances and challenges in multi-label classification of remote sensing images**. *Remote Sensing for Natural Resources, 36*(2), 10-20. [cgsjournals.com](https://www.cgsjournals.com/article/doi/10.6046/zrzyyg.2023027)
*   [10] Zhang, M. L., & Zhou, Z. H. (2007). **ML-KNN: A lazy learning approach to multi-label learning**. *Pattern Recognition, 40*(7), 2038-2048.
*   [11] Kim, Y. (2014). **Convolutional Neural Networks for Sentence Classification**. *Proceedings of the 2014 Conference on Empirical Methods in Natural Language Processing (EMNLP)*, 1746–1751.
*   [12] Devlin, J., Chang, M. W., Lee, K., & Toutanova, K. (2019). **BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding**. *Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL-HLT)*, 3286–3296.