好的，遵照您的指示，这是一篇关于「Lexicon-Enhanced Sentiment Analysis Models Using BERT and CNNs」的中文学术综述。

***

### **融合词典信息的BERT与CNN情感分析模型研究综述 (2022-2025)**

#### **引言**

情感分析，作为自然语言处理（NLP）的关键分支，旨在识别和提取文本中的主观信息、观点和情感色彩。其研究历程从早期的基于情感词典和统计机器学习的方法，逐步演进到以卷积神经网络（CNN）、循环神经网络（RNN）为代表的深度学习时代。近年来，以BERT（Bidirectional Encoder Representations from Transformers）为代表的预训练语言模型（PLM）通过在海量语料上进行无监督学习，极大地提升了模型对文本深层语义的理解能力，在各项NLP任务中取得了突破性进展 [[image.hanspub.org](https://image.hanspub.org/Html/8-2622608_54354.htm)]。

然而，单纯依赖预训练模型进行微调的范式也存在局限，例如对特定领域知识感知不足、对长距离上下文依赖捕捉不充分，或未能充分利用模型内部学习到的多层次特征。针对这些问题，2022至2025年间的研究工作不再满足于单一模型结构，而是探索将BERT的强大语义表征能力与CNN的局部特征提取能力、RNN的序列信息捕捉能力以及外部语言知识（如情感词典、知识图谱）相结合。本综述聚焦于“词典增强”这一核心思想，并将其广义化，涵盖了通过多种方式增强BERT和CNN模型情感分析能力的前沿方法，旨在对近三年来的代表性工作进行分类、梳理与展望。

#### **方法分类与代表作**

基于增强信息的来源与融合方式，可将当前主流方法分为三大类：预训练-微调框架下的混合模型、融合多层次内部特征的模型，以及外部知识增强的模型。

##### **1. 预训练-微调框架下的混合模型**

此类方法的核心思想是将BERT或其变体（如RoBERTa）作为强大的语义编码器，再辅以RNN或CNN等结构捕捉特定类型的文本特征，形成优势互补。

-   **RoBERTa-BiLSTM-Multihead Attention (RBMA)**：该研究针对单一模型难以充分提取深层语义和处理长序列依赖的问题，提出了一种融合模型 [[pdf.hanspub.org](https://pdf.hanspub.org/csa2025154_171543555.pdf)]。方法上，模型首先利用RoBERTa的强大预训练能力捕捉词汇级别的语义信息；随后，通过双向长短期记忆网络（BiLSTM）学习句子的正反向时序关系，以增强对上下文结构和长距离依赖的理解；最后引入多头注意力机制对情感关键词进行加权，从而精准识别情感倾向。在微博评论数据集上的实验表明，RBMA模型相较于单一的RoBERTa模型，在准确率和F1值上分别实现了1.7%和2.0%的提升，验证了混合架构的有效性。

-   **RoBERTa-BiLSTM (Rahman et al., 2024)**：这项工作同样关注长依赖文本和词汇多样性带来的挑战，提出了RoBERTa与BiLSTM的混合模型 [[hub.baai.ac.cn](https://hub.baai.ac.cn/paper/e4d02f18-e465-4970-b66e-88bb2aff94f3)]。其核心思路与RBMA相似，使用RoBERTa生成上下文感知的词嵌入，再由BiLSTM捕获序列的上下文语义。该研究在IMDb、Twitter等多个公开数据集上进行了验证。实验结果显示，RoBERTa-BiLSTM模型在IMDb数据集上实现了92.36%的准确率，显著超越了BERT及RoBERTa-base等基线模型，再次证明了结合序列模型捕捉长依赖关系的价值。

-   **ELMo-CNN-BiGRU (ECB)**：此模型探索了动态与静态词向量融合的策略，并构建了双通道网络结构 [[www.ecice06.com](http://www.ecice06.com/article/2022/1000-3428/228105.htm)]。研究旨在解决传统静态词向量无法处理一词多义的问题。方法上，模型利用ELMo生成动态词向量，Glove生成静态词向量，两者堆叠后输入并联的CNN和BiGRU双通道：CNN通道提取局部特征，BiGRU通道捕获全局上下文信息。与性能较优的H-BiGRU模型相比，ECB模型在IMDb、yelp等数据集上准确率提升了约2-3个百分点，证明了双通道并行结构及动静态词向量融合的优越性。

##### **2. 融合多层次内部特征的模型**

此类方法不依赖外部组件，而是深入挖掘并利用BERT模型内部不同层级所蕴含的丰富语义和句法信息。

-   **BERT-MLF (BERT-Multi-Layer Fusion)**：作为该方向的代表性工作，该研究指出仅使用BERT最后一层输出会忽略其他层学习到的宝贵特征 [[pdf.hanspub.org](https://pdf.hanspub.org/csa20201200000_16146338.pdf)]。研究表明，BERT的底层学习短语信息，中层学习句法结构，高层学习语义特征。BERT-MLF模型融合BERT每一个编码层输出的方面（aspect）特征，然后通过一个卷积层（CNN）在层与层之间提取关键语义，减少冗余信息。在SemEval-2014 Task 4数据集上的实验证明，与仅使用顶层特征的TD-BERT相比，BERT-MLF在Laptop数据集上准确率从80.00%提升至81.30%，有效验证了融合多层内部特征的价值。

##### **3. 外部知识增强的模型**

这类研究将情感词典、句法知识、知识图谱等外部语言知识显式地融入模型，以弥补预训练模型在特定领域或情感常识上的不足。

-   **TIAN (Transformer and Interactive Attention Network)**：该模型针对RNN计算效率低及传统注意力机制可能忽略远距离关键词的问题，提出一种融合Transformer和交互注意力网络的方法 [[html.rhhz.net](https://html.rhhz.net/tis/html/202303016.htm)]。模型首先使用BERT进行词嵌入，并通过Transformer编码器并行处理句子。其核心创新在于，利用基于依存句法树计算的**句法相对距离**（Syntactic Relative Distance）来指导上下文动态掩码（CDM）和动态权重（CDW）机制，使模型能关注与特定方面词有重要句法关系的局部上下文。在Restaurant2014数据集上，TIAN模型准确率达到87.23%，F1值达到81.93%，均优于未引入句法知识的LCF-BERT等强基线模型。

-   **KGDGCN (Knowledge Graph and Dual Graph Convolution)**：该研究致力于解决文本语义表示因缺乏外部知识而不够全面的问题，提出一种基于知识图谱和双重图卷积的模型 [[pdf.hanspub.org](https://pdf.hanspub.org/csa_1543814.pdf)]。模型利用LSTM提取文本上下文，同时通过知识图谱卷积网络（KGCN）获取与文本实体相关的外部知识，并动态融合文本与知识嵌入。最后，将融合后的信息输入句法图卷积网络（Syntactic GCN）和语义图卷积网络（Semantic GCN）以捕捉结构化信息。在电影评论数据集上的实验表明，引入知识图谱后，模型的F1值从0.685提升至0.746，显著增强了语义理解和情感分类的准确性。

#### **实验与评价总结**

-   **数据集与评价指标**：上述研究广泛采用了学术界公认的基准数据集，如英文领域的SemEval系列（Restaurant, Laptop）、Twitter、IMDb，以及中文领域的微博、电商评论等，确保了实验结果的可比性。评价指标主要采用准确率（Accuracy）和宏F1值（Macro-F1），后者在处理类别不平衡的数据集时能更公允地评价模型综合性能。

-   **共性结论**：
    1.  **混合架构的有效性**：无论是BERT+BiLSTM还是BERT+CNN的组合，实验结果一致表明，混合模型通常优于单一的BERT或CNN模型。这证实了不同网络结构在特征提取上具有互补性：BERT/RoBERTa提供强大的底层语义表示，而RNN擅长捕捉序列依赖，CNN则精于提取局部关键模式。
    2.  **特征融合的必要性**：研究表明，无论是融合BERT的内部多层特征，还是融合外部知识（句法、知识图谱），都能为模型带来显著性能提升。简单地将BERT作为黑盒编码器并只取顶层输出是一种次优策略，会导致有价值的句法和词组信息的损失。
    3.  **知识引导的精确性**：基于情感词典、句法依赖或知识图谱等外部知识的方法，能有效引导模型关注更具判别性的情感词汇和语义关系，尤其在处理复杂句子结构和特定领域文本时优势明显。这表明，将符号化的语言知识与分布式的深度学习模型相结合是提升性能的可靠路径。

#### **趋势与挑战**

基于2022-2025年的研究进展，未来该领域的研究将呈现以下趋势并面临相应挑战：

1.  **从词典到知识图谱的演进（Evolution from Lexicon to Knowledge Graph）**：早期的词典增强正迅速向更结构化、更丰富的知识图谱增强演进。未来的研究将不再局限于情感词列表，而是利用知识图谱中的实体、关系和属性来构建更复杂的推理路径，从而实现对文本更深层次的理解，尤其是在方面级情感分析和隐式情感识别等任务中。挑战在于如何高效地从大规模知识图谱中检索相关知识并与文本表示进行有效对齐与融合。

2.  **交互式与细粒度注意力的深化（Deepening of Interactive & Fine-grained Attention）**：注意力机制已成为模型的核心。未来的趋势是发展更为精细和具备解释性的注意力机制。如TIAN模型所示，利用句法或语义先验知识来指导注意力分配权重，将成为主流方向。模型将不仅仅学习“关注哪里”，更要学习“为何关注”，例如通过多任务学习或对比学习，让注意力权重分布更符合语言学逻辑。

3.  **轻量化与高效微调（Lightweight Models & Efficient Fine-tuning）**：随着模型复杂度增加，计算成本成为一个严峻挑战，如RBMA研究中提到的资源需求问题。因此，未来的研究热点将包括：（1）模型压缩与知识蒸馏，将大型复杂模型的知识迁移到小型、推理速度快的模型上；（2）参数高效微调（Parameter-Efficient Fine-Tuning, PEFT），如Adapter-tuning、LoRA等技术，在冻结大部分预训练参数的同时，仅通过训练少量额外参数来适应下游任务，大幅降低训练成本。

#### **结论**

在2022至2025年间，融合词典信息（广义）的BERT与CNN情感分析模型研究取得了显著进展。研究范式已从简单的模型叠加，转向更为精巧的混合架构设计、多维度的特征融合以及外部知识的深度整合。混合模型验证了结构互补的价值，多层特征融合释放了预训练模型内部的潜力，而知识增强则为模型注入了宝贵的语言先验。尽管性能不断提升，但模型的高昂计算成本和对复杂语言现象（如反讽、隐喻）的理解能力仍是未来需要攻克的难题。展望未来，向知识图谱的演进、发展更细粒度的注意力机制以及实现模型轻量化将是该领域的核心研究方向。

#### **参考文献**
[1] 俞凯, 牟兆祥, 王天宇. 针对网络舆情情感分析的RoBERTa-BiLSTM-Multihead Attention模型[J]. 计算机科学与应用, 2025, 15(4): 152-161. [pdf.hanspub.org](https://pdf.hanspub.org/csa2025154_171543555.pdf)
[2] Rahman, M. M., Shiplu, A. I., Watanobe, Y., & Alam, M. A. (2024). RoBERTa-BiLSTM: A Context-Aware Hybrid Model for Sentiment Analysis. *BAAI Acquaintance Hub*. [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/e4d02f18-e465-4970-b66e-88bb2aff94f3)
[3] 李宁健, 方睿. 融合BERT多层特征的方面级情感分析[J]. 计算机科学与应用, 2020, 10(12): 2147-2158. [pdf.hanspub.org](https://pdf.hanspub.org/csa20201200000_16146338.pdf)
[4] 程艳, 胡建生, 赵松华, 等. 融合Transformer和交互注意力网络的方面级情感分类模型[J]. 智能系统学报, 2024, 19(3): 728-737. [html.rhhz.net](https://html.rhhz.net/tis/html/202303016.htm)
[5] 林军利, 李婷. 基于知识图谱与双重图卷积的情感分类模型[J]. 计算机科学与应用, 2025, 15(11): 207-219. [pdf.hanspub.org](https://pdf.hanspub.org/csa_1543814.pdf)
[6] 吴迪, 王梓宇, 赵伟超. ELMo-CNN-BiGRU双通道文本情感分类模型[J]. 计算机工程, 2022, 48(8), 105-112. [www.ecice06.com](http://www.ecice06.com/article/2022/1000-3428/228105.htm)
[7] 孙洋, 冷冠男. 基于BERT模型的网络舆情情感分析——以上海疫情为例[J]. 应用数学进展, 2022, 11(08): 5053-5061. [image.hanspub.org](https://image.hanspub.org/Html/8-2622608_54354.htm)
[8] Devlin, J., Chang, M. W., Lee, K., & Toutanova, K. (2018). BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding. *arXiv preprint arXiv:1810.04805*.
[9] Vaswani, A., Shazeer, N., Parmar, N., et al. (2017). Attention is all you need. *Advances in neural information processing systems, 30*.
[10] Song, Y., Wang, J., Jiang, T., et al. (2019). Attentional Encoder Network for Targeted Sentiment Classification. *arXiv preprint arXiv:1902.09314*.
[11] Ma, D., Li, S., Zhang, X., & Wang, H. (2017). Interactive Attention Networks for Aspect-Level Sentiment Classification. *Proceedings of the Twenty-Sixth International Joint Conference on Artificial Intelligence*. [ijcai.org](https://www.ijcai.org/proceedings/2017/0568.pdf)
[12] Kim, Y. (2014). Convolutional Neural Networks for Sentence Classification. *Proceedings of the 2014 Conference on Empirical Methods in Natural Language Processing (EMNLP)*. [aclweb.org](https://www.aclweb.org/anthology/D14-1181)
[13] Zeng, B., Yang, H., Xu, R., et al. (2019). LCF: a local context focus mechanism for aspect-based sentiment classification. *Applied sciences, 9*(16), 3389. [mdpi.com](https://www.mdpi.com/2076-3417/9/16/3389)