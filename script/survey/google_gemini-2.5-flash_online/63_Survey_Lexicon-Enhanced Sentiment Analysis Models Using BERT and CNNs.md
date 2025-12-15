好的，这是一篇关于“融合词典的BERT与CNN情感分析模型”的中文学术综述，涵盖2022-2025年的代表性工作。

## Lexicon-Enhanced Sentiment Analysis Models Using BERT and CNNs 中文综述 (2022-2025)

### 引言

情感分析旨在识别和提取文本中蕴含的情感极性或强度，在舆情分析、市场营销及推荐系统等领域具有广泛应用前景。传统的深度学习模型（如循环神经网络 (RNN) 和卷积神经网络 (CNN)）在捕获文本语义方面表现出色，然而，面对社交媒体文本的词汇多样性、长距离依赖、隐式情感表达和语义模糊性等挑战时，单一模型仍存在局限 [jns.nju.edu.cn](https://jns.nju.edu.cn/article/2024/0469-5097/0469-5097-2024-60-3-502.shtml)。

近年来，预训练语言模型（如BERT及其变体）以其强大的上下文理解能力显著提升了情感分析的性能 [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/e4d02f18-e465-4970-b66e-88bb2aff94f3)。同时，情感词典作为一种外部知识，能够为模型提供明确的情感倾向信息。将情感词典的知识融入基于BERT和CNN的深度学习模型，被认为是提升情感分析模型性能的有效途径 [jns.nju.edu.cn](https://jns.nju.edu.cn/article/2024/0469-5097/0469-5097-2024-60-3-502.shtml)。本综述旨在回顾2022-2025年间，通过融合情感词典知识增强BERT和CNN模型在情感分析任务上的代表性工作，并探讨其研究趋势。

### 方法分类与代表作

#### 1. 基于BERT-CNN融合情感词典的模型

这类模型将BERT的强大语义编码能力与CNN的局部特征提取优势相结合，并通过情感词典提供额外的情感信息。

*   **桂婷等人 (2023) [ccj.pku.edu.cn](https://ccj.pku.edu.cn/article/info?aid=365665006)**：
    *   **研究问题**：处理中文微博文本稀疏性、高维性及语境依赖性导致的情感分类困难。
    *   **核心方法**：通过对比BERT、BERT-LSTM和BERT-CNN模型，发现BERT-CNN在微博文本情感分类中表现最优。模型利用BERT进行文本深层语义表示，再通过CNN提取局部特征。
    *   **关键实验结论**：BERT-CNN模型在准确率上比单一BERT模型提高了0.26%，在中文微博文本情感分类任务中取得了最佳效果。

*   **朱昆等人 (2024) [pdf.hanspub.org](https://pdf.hanspub.org/mos20240100000_43819890.pdf)**：
    *   **研究问题**：当前情感分类模型未能充分提取短文本的显著特征，导致分类准确率有待提升。
    *   **核心方法**：提出BERT-BiLSTM-BiGRU-CNN模型，融合BERT进行文本表示，并结合BiLSTM、BiGRU和CNN提取多粒度特征。模型中还引入了自注意力机制以增强上下文理解，旨在更全面地捕捉文本情感。
    *   **关键实验结论**：在亚马逊评论数据集上，该模型在准确率、召回率和F1值方面均优于现有对比模型，在二元情感分类中表现出色。Word2Vec与BERT的比较显示，BERT在短文本预训练中的掩码策略有助于提取低层次语义信息。

#### 2. 基于RoBERTa及其融合注意力机制的模型

RoBERTa作为BERT的优化版本，在更大规模数据集上预训练，进一步提升了语言理解能力。与BiLSTM和多头注意力机制结合，可以更精细地捕捉情感信息。

*   **俞凯等人 (2025) [pdf.hanspub.org](https://pdf.hanspub.org/csa2025154_171543555.pdf)**：
    *   **研究问题**：单一模型在网络舆情情感分析中难以充分提取深层语义特征，且对复杂情感转变和长序列依赖处理不佳。
    *   **核心方法**：提出了RoBERTa-BiLSTM-Multihead Attention (RBMA) 融合模型。RoBERTa捕捉词汇语义信息，BiLSTM学习正反向语义关系和上下文依赖，多头注意力机制则对情感信息进行加权计算。
    *   **关键实验结论**：在微博评论数据集上，RBMA模型的准确率、精确率、召回率和F1值均优于LSTM、BERT、RoBERTa等传统模型，特别在处理突发事件舆情时表现出色，提升幅度达1.7%至2.9%。

*   **Rahman, M. M.等人 (2024) [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/e4d02f18-e465-4970-b66e-88bb2aff94f3)**：
    *   **研究问题**：情感分析中存在的词汇多样性、长依赖、未知符号、不平衡数据集等挑战，以及顺序模型处理长文本的效率问题。
    *   **核心方法**：提出RoBERTa-BiLSTM混合深度学习模型。RoBERTa生成有意义的词嵌入向量，BiLSTM有效捕捉长依赖文本的上下文语义，结合了顺序模型和Transformer模型的优点。
    *   **关键实验结论**：在IMDb、Twitter US Airline和Sentiment140数据集上，该模型在准确率和F1分数上超越了BERT、RoBERTa-base等基准模型，最高准确率达到92.36%。

#### 3. 结合知识图谱与多粒度融合的模型

将外部知识图谱作为情感词典的扩展，能够为模型提供更丰富的实体关系和领域知识，进一步增强情感理解。

*   **林军利等人 (2025) [pdf.hanspub.org](https://pdf.hanspub.org/csa_1543814.pdf)**：
    *   **研究问题**：情感分析任务中，文本与外部知识关联不足，导致语义表示不够全面，尤其在方面级情感分析中细粒度不足。
    *   **核心方法**：提出基于知识图谱与双重图卷积的情感分类模型(KGDGCN)。模型首先用LSTM提取文本上下文，同时通过知识图谱卷积网络获取实体外部知识，通过实体对齐和预测动态融合文本与知识嵌入。最后，使用句法GCN和语义GCN获取句法和语义信息。
    *   **关键实验结论**：在电影评论数据集上，KGDGCN在精确率、召回率和F1值方面均优于ATEA-LSTM、IAN和DualGCN，验证了知识图谱融合对情感分类效果的显著提升。

*   **仲兆满等人 (2025) [html.rhhz.net](https://html.rhhz.net/tis/html/202409012.htm)**：
    *   **研究问题**：多模态情感分析中，忽略图像与文本间的情感关联性导致融合特征存在冗余，影响情感预测准确性。
    *   **核心方法**：提出基于卷积交叉注意力与跨模态动态门控的多模态情感分析模型(CCA-CDG)。模型通过卷积交叉注意力模块捕捉图像和文本的一致性表达，并利用跨模态动态门控模块动态调节情感特征融合，同时引入全局特征联合模块进行补充预测。
    *   **关键实验结论**：在MVSA-Single和MVSA-Multi数据集上，CCA-CDG的准确率和F1值均优于现有主流模型，突出了情感关联性识别和动态门控融合对改善多模态情感分析性能的重要性。

#### 4. 融合序贯三支决策和多粒度的模型

这类模型在深度学习框架中融入多粒度决策和不确定性处理机制，以提升对边界模糊情感数据的处理能力。

*   **赵梦宇等人 (2024) [jns.nju.edu.cn](https://jns.nju.edu.cn/article/2024/0469-5097/0469-5097-2024-60-3-502.shtml)**：
    *   **研究问题**：传统深度学习模型在情感分析中对极性不明显（模糊）的数据进行硬分类时准确率欠佳，忽视了阈值边缘对象的影响。
    *   **核心方法**：提出基于BiLSTM和CNN的序贯三支情感分类模型（BiLCNN-S3WD），将序贯三支决策引入深度学习训练过程，以多粒度方式处理极性不明显数据，提供了“接受”、“拒绝”和“延迟决策”三种选项。
    *   **关键实验结论**：在online\_shopping\_10\_cat和微博数据集的对比实验中，BiLCNN-S3WD模型在各项评价标准上均优于七个基线模型，有效提升了分类精度，验证了多粒度序贯三支决策在处理模糊情感数据上的优势。

### 实验与评价总结

综上所述，当前融合BERT、CNN与情感词典增强的情感分析模型，在实验中普遍采用准确率（Accuracy）、精确率（Precision）、召回率（Recall）和F1值作为主要评价指标 [pdf.hanspub.org](https://pdf.hanspub.org/csa2025154_171543555.pdf), [pdf.hanspub.org](https://pdf.hanspub.org/mos20240100000_43819890.pdf), [html.rhhz.net](https://html.rhhz.net/tis/html/202409012.htm)。实验数据集多数来源于社交媒体（如微博、Twitter）和产品评论（如Amazon评论、MVSA） [html.rhhz.net](https://html.rhhz.net/tis/html/202409012.htm), [jns.nju.edu.cn](https://jns.nju.edu.cn/article/2024/0469-5097/0469-5097-2024-60-3-502.shtml), [pdf.hanspub.org](https://pdf.hanspub.org/csa2025154_171543555.pdf), [pdf.hanspub.org](https://pdf.hanspub.org/mos20240100000_43819890.pdf)。

这些研究的共性结论是，相较于单一模态或未融入外部知识的基线模型，BERT与CNN的融合模型在捕获文本语义、处理长距离依赖和上下文信息方面展现出明显优势。同时，通过引入情感词典、知识图谱、注意力机制或多粒度决策机制，能够有效降低模型在处理稀疏、高维或情感模糊文本时产生的冗余特征和误分类问题，从而进一步提升模型在不同情感分类任务中的性能。对于跨模态场景，情感关联性分析和动态门控机制的引入，也显著改善了图文融合的准确性 [html.rhhz.net](https://html.rhhz.net/tis/html/202409012.htm)。

### 趋势与挑战

展望2025年前后，融合词典的BERT与CNN情感分析模型的研究趋势将集中在以下几个方面：

1.  **多模态情感关联的精细化建模**：在图文等多模态情感分析任务中，如何克服模态间情感未对齐带来的冗余特征仍是挑战 [html.rhhz.net](https://html.rhhz.net/tis/html/202409012.htm)。未来的研究将更侧重于设计更加精细化的跨模态注意力机制和动态门控策略，以准确识别和融合模态间的情感关联，同时保留各模态原始特征的关键信息，特别是在图文情感表达不明显或冲突时。
2.  **外部知识图谱的深度融合与动态更新**：情感词典和知识图谱在提供外部语义和常识方面发挥关键作用 [pdf.hanspub.org](https://pdf.hanspub.org/csa_1543814.pdf)。未来的研究将探索更深层次的文本与知识图谱的动态融合方法，例如通过图卷积网络或异构图神经网络，捕捉更复杂的实体关系和领域知识，并解决知识图谱时效性问题，实现知识的动态更新和自适应。
3.  **模型复杂度优化与实时性提升**：当前融合BERT和多层神经网络的模型结构往往较为复杂，导致训练时间长且计算资源需求高，限制了其在实时舆情监控等场景的应用 [pdf.hanspub.org](https://pdf.hanspub.org/csa2025154_171543555.pdf)。未来的研究将致力于模型剪枝、量化、知识蒸馏等轻量化技术，或开发更高效的并行计算优化策略，以在保证性能的同时，显著降低模型复杂度，提高推理速度，使其更适用于资源受限或对实时性要求高的应用场景。
4.  **不确定性情感判别的精细化策略**：针对自然语言中模糊、中性或矛盾的情感表达，传统模型的硬分类方法存在局限 [jns.nju.edu.cn](https://jns.nju.edu.cn/article/2024/0469-5097/0469-5097-2024-60-3-502.shtml)。未来的研究将进一步探索基于序贯三支决策和多粒度分析的软分类或延迟决策机制，为情感不确定性提供更灵活、更接近人类认知模式的处理方式，从而提高模型在细粒度情感辨别上的准确性和鲁棒性。
5.  **隐式情感与反讽识别的突破**：现有模型在处理隐式情感、反讽和双关语等复杂情感现象时仍面临挑战 [pdf.hanspub.org](https://pdf.hanspub.org/mos20240100000_43819890.pdf)。未来的研究需要结合更丰富的语义上下文、篇章级信息，甚至外部常识知识进行推理，发展能够识别言外之意和深层情感的模型，从而提升情感分析在复杂语境下的理解能力。

### 结论

本综述回顾了2022-2025年间利用情感词典增强BERT和CNN模型在情感分析领域的代表性进展。这些研究通过融合BERT的深层语义理解、CNN的局部特征提取以及情感词典等外部知识，显著提升了情感分析的准确性。未来的研究将继续在多模态融合、知识深度集成、模型轻量化、不确定性处理以及复杂情感识别方面寻求突破，以应对日益复杂的现实应用场景。

### 参考文献

1.  仲兆满, 樊继冬, 张渝, 等. 基于卷积交叉注意力与跨模态动态门控的多模态情感分析模型[J]. 智能系统学报, 2025, 20(4): 999-1009. doi: [10.11992/tis.202409012](https://html.rhhz.net/tis/html/202409012.htm)
2.  林军利, 李婷. 基于知识图谱与双重图卷积的情感分类模型[J]. 计算机科学与应用, 2025, 15(11): 207-219. doi: [10.12677/csa.2025.1511298](https://pdf.hanspub.org/csa_1543814.pdf)
3.  俞凯, 牟兆祥, 王天宇. 针对网络舆情情感分析的RoBERTa-BiLSTM-Multihead Attention模型[J]. 计算机科学与应用, 2025, 15(4): 152-161. doi: [10.12677/csa.2025.154088](https://pdf.hanspub.org/csa2025154_171543555.pdf)
4.  Zhao Mengyu, Sun Jingbo, Wei Zuntian, et al. Research on sequential three⁃way sentiment classification model based on BiLSTM and CNN[J]. Journal of Nanjing University (Natural Sciences), 2024, 60(3): 502-510. doi: [10.13232/j.cnki.jnju.2024.03.013](https://jns.nju.edu.cn/article/2024/0469-5097/0469-5097-2024-60-3-502.shtml)
5.  Md. Mostafizer Rahman, Ariful Islam Shiplu, Yutaka Watanobe, Md. Ashad Alam. RoBERTa-BiLSTM: A Context-Aware Hybrid Model for Sentiment Analysis[R/OL]. 2024, [https://arxiv.org/abs/2406.00783](https://hub.baai.ac.cn/paper/e4d02f18-e465-4970-b66e-88bb2aff94f3).
6.  朱昆, 刘姜, 倪枫, 朱佳怡. 基于BERT-BiLSTM-BiGRU-CNN的文本情感分析模型[J]. 建模与仿真, 2024, 13(1): 42-49. doi: [10.12677/mos.2024.131005](https://pdf.hanspub.org/mos20240100000_43819890.pdf)
7.  桂婷, 马子璇, 梁泽. 基于BERT-CNN模型的微博文本情感分类研究[J]. 网络安全技术与应用, 2023(11): 34-35. doi: [10.19358/j.issn.1008-6721.2023.11.014](https://ccj.pku.edu.cn/article/info?aid=365665006)
8.  郝星跃. 基于多头注意力机制的BiGRU-CNN文本情感分析[J]. 计算机科学与应用, 2022, 12(1): 123-134. doi: [10.12677/csa.2022.121014](https://pdf.hanspub.org/csa20220100000_60521281.pdf)
9.  Zhong Zhaoman, Fan Jidong, Zhang Yu, et al. Multimodal sentiment analysis model with convolutional cross-attention and cross-modal dynamic gating [J]. CAAI Transactions on Intelligent Systems, 2025, 20(4): 999-1009. doi: [10.11992/tis.202409012](https://html.rhhz.net/tis/html/202409012.htm)
10. Lin, J. Lin, T. Emotion Classification Model Based on Knowledge Graph and Dual Graph Convolution [J]. Computer Science and Application, 2025, 15(11), 207-219. doi: [10.12677/csa.2025.1511298](https://pdf.hanspub.org/csa_1543814.pdf)
11. Yu, K. Mu, Z. Wang, T. RoBERTa-BiLSTM-Multihead Attention Model for Online Public Opinion Sentiment Analysis [J]. Computer Science and Application, 2025, 15(4), 152-161. doi: [10.12677/csa.2025.154088](https://pdf.hanspub.org/csa2025154_171543555.pdf)
12. Zhu, K., Liu, J., Ni, F., Zhu, J. Sentiment Analysis of Text Based on BERT-BiLSTM-BiGRU-CNN Model [J]. Modeling and Simulation, 2024, 13(1), 42-49. doi: [10.12677/mos.2024.131005](https://pdf.hanspub.org/mos20240100000_43819890.pdf)