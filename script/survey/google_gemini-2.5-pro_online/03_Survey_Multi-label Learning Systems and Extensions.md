好的，作为一名严谨的科研助手，我将基于您提供的真实网络搜索结果，为您生成一篇关于“多标签学习系统及其扩展”的中文学术综述。

***

### **关于多标签学习系统及其扩展的学术综述 (2022-2025)**

#### **引言**

多标签学习（Multi-label Learning, MLL）旨在为每个实例关联一个或多个相关标签，是机器学习和自然语言处理中的一个核心任务。与单标签分类不同，多标签学习必须处理两个核心挑战：标签空间的高维性以及标签之间复杂的依赖关系 [jos.org.cn](https://jos.org.cn/html/2023/12/6802.htm)。随着应用场景的日益复杂，如科研文献归档、遥感图像分析和法律文书判读，研究领域已从传统的“扁平”多标签分类扩展到更具挑战性的场景，包括层次多标签分类（Hierarchical Multi-label Classification, HMTC）、极限多标签分类（eXtreme Multi-label Classification, XMLC）以及多模态多标签学习 [www.zhuanzhi.ai](https://www.zhuanzhi.ai/paper/c9a665a1f4cad6f1705fd734cf38d1e9)。本综述旨在梳理并总结 2022 年至 2025 年间在多标签学习系统及其扩展领域的代表性研究工作，重点分析其核心方法、实验范式与未来趋势。

#### **方法分类与代表作**

近期的研究工作主要围绕如何更有效地建模文本/数据特征、如何利用标签间的结构信息以及如何应对数据不平衡等问题展开。

**1. 层次多标签分类 (Hierarchical Multi-label Classification, HMTC)**
HMTC 要求模型不仅要预测正确的标签，还要遵循标签之间预定义的层次结构。这类方法的核心在于如何将层次结构信息融入到模型的学习过程中。

*   **MHGCLR (2025)**  
    该研究针对现有特征提取方法忽略文本局部与全局联系的问题，提出了基于多尺度特征提取的层次多标签文本分类方法（MHGCLR） [html.rhhz.net](https://html.rhhz.net/ZZDXXBLXB/html/20250204.htm)。其核心方法是通过一个多尺度特征提取模块，融合BERT提供的词向量和Doc2Vec提供的句向量，以捕捉不同粒度的文本语义。模型利用Graphormer作为图编码器来建模标签的层次结构，并结合对比学习来增强正负样本的区分度，从而提升分类效果。关键的实验结论表明，该模型在WOS、RCV1-V2等多个数据集上的Micro-F1和Macro-F1指标均超越了主流基线模型，同时，其提出的层次Micro-F1（HMicro-F1）等新指标更合理地评估了层次分类的性能。

**2. 多粒度与标签关联性建模**
这类方法致力于从不同粒度（如词级、文档级）提取信息，并显式或隐式地对标签间的共现、互斥等关系进行建模，以增强模型的推理能力。

*   **MIRE (2023)**  
    该工作认为传统方法缺乏对文本信息的多粒度学习和对标签间约束关系的利用，因此提出了一种多粒度信息关系增强的多标签文本分类方法（MIRE） [jos.org.cn](https://jos.org.cn/html/2023/12/6802.htm)。MIRE通过一种新颖的文本-标签联合嵌入方式，将文本和标签映射到同一语义空间，并设计了三个并行模块：文档级浅层交互模块（DISLA）、词级深层交互模块（WIDLA）和标签约束关系匹配辅助模块（LCRM）。实验证明，在AAPD和法律、医疗等中文数据集上，MIRE通过综合利用不同粒度的文本-标签关系及标签间的约束关系，在Micro-F1、Macro-F1和nDCG@k等关键指标上取得了最佳性能，消融实验也验证了联合嵌入和LCRM模块的有效性。

**3. 生成式方法与极限分类**
面对标签数量可达数十万的极限多标签分类（XMLC）任务，近期研究开始探索生成式范式，将任务视为一个序列生成问题，从而直接生成相关的标签序列。

*   **G-HXMLC (2022)**  
    此研究提出将层次结构极限多标签文本分类任务（HXMLC）视为一个序列到序列的生成问题，旨在直接从庞大的标签库中生成与文本相关的标签序列 [aclanthology.org](https://aclanthology.org/2022.ccl-1.60.pdf)。其核心是一种基于软约束的解码机制和词表复合映射策略，该方法在解码过程中利用标签的层次结构信息进行引导，但又不施加硬性约束。这种软约束设计允许模型在面对标签体系中的噪声或不完整信息时具有更好的容错能力。实验分析表明，该生成式方法不仅能有效利用标签的上下位关系，而且相比硬约束方法，在标签数量较多时性能下降更平缓，证明了其在HXMLC任务中的有效性与鲁棒性。

**4. 创新损失函数**
多标签任务固有的正负样本严重不平衡问题是制约模型性能的关键瓶颈。为此，研究者们设计了专门的损失函数以缓解此问题。

*   **Asymmetric Loss (ASL, 2025)**  
    该工作针对多标签分类中普遍存在的正负样本比例悬殊（例如，平均每张图片只有少数正标签，但有大量负标签）以及负样本易被错误标注的问题，提出了一种非对称损失函数（ASL） [blog.csdn.net](https://blog.csdn.net/weixin_43424450/article/details/147364959)。ASL的核心思想是“非对称聚焦”和“概率偏移”，即对正负样本使用不同的聚焦指数（γ+和γ-），并对简单负样本的概率进行硬阈值裁剪。通过对负样本施加更强的衰减，同时保持正样本的梯度贡献，ASL能有效平衡优化过程，避免模型过度关注易分类的负样本。实验表明，在MS-COCO、Pascal-VOC等多个基准数据集上，ASL显著优于传统的交叉熵和Focal Loss，成为解决多标签不平衡问题的有效工具。

**5. 多模态与知识增强扩展**
多标签学习的应用已扩展到多模态数据，并开始融合外部知识库以增强模型的深度语义理解能力。

*   **多模态知识增强的跨模态检索 (2025)**  
    该研究将多标签学习扩展到图像-文本跨模态检索领域，旨在通过融合多模态知识图谱来增强深度语义学习 [paper.edu.cn](https://paper.edu.cn/releasepaper/content/202503-143)。其核心方法是利用图神经网络（GNN）对多模态知识图谱进行编码，并将知识增强后的表示与图像、文本特征进行融合。为了实现多模态数据在统一语义空间下的对齐，该方法引入了模态内和模态间的对比学习损失函数。实验结果显示，通过知识增强和对比学习，模型在跨模态检索任务上取得了显著的性能提升，验证了外部知识在弥合模态差异、提升语义表征质量方面的有效性。
*   **遥感图像多标签分类 (2024)**  
    遥感图像分析是多标签学习的一个重要应用场景，其面临的挑战在于遥感对象尺度、颜色、形状多样 [cgsjournals.com](https://www.cgsjournals.com/article/doi/10.6046/zrzyyg.2023027)。虽然这是一篇综述，但它指出了该领域的研究焦点是图像特征提取和标签特征提取，这与MIRE等工作的思想不谋而合，即关注数据与标签的双向交互。
*   **基于层次标签结构的标记分布学习 (2024)**  
    此项研究将多标签学习推广至标记分布学习（Label Distribution Learning, LDL），并结合了层次结构 [manu44.magtech.com.cn](https://manu44.magtech.com.cn/Jwk_infotech_wk3/CN/abstract/abstract5639.shtml)。LDL不仅关心样本属于哪些标签，还关心其属于每个标签的相对程度。将LDL与层次结构相结合，能够更精细地刻画具有层级依赖的模糊或不确定标签，是多标签学习在表达能力上的重要扩展。

#### **实验与评价总结**

*   **数据集与评价指标**：
    文本分类任务常在WOS、RCV1-V2、AAPD、NYT等公共数据集上进行评估 [html.rhhz.net](https://html.rhhz.net/ZZDXXBLXB/html/20250204.htm)。此外，法律（LAIC）、医疗等领域特定数据集也被用于验证模型的通用性 [jos.org.cn](https://jos.org.cn/html/2023/12/6802.htm)。图像领域则常用MS-COCO、Pascal-VOC和Open Images等 [blog.csdn.net](https://blog.csdn.net/weixin_43424450/article/details/147364959)。评价指标主要包括Micro-F1、Macro-F1、P@k (Precision at k)和nDCG@k。针对层次分类任务，还出现了如HMicro-F1和HMacro-F1等层次感知的约束性指标，这类指标要求一个节点的预测必须以其所有祖先节点被正确预测为前提，从而更严格地评估了模型对层次结构的遵循程度 [html.rhhz.net](https://html.rhhz.net/ZZDXXBLXB/html/20250204.htm)。

*   **共性实验结论**：
    1.  **预训练模型的基石作用**：绝大多数先进模型均基于BERT等大型预训练语言模型进行构建，证明了预训练模型提供了强大的语义表征基础 [jos.org.cn](https://jos.org.cn/html/2023/12/6802.htm)。
    2.  **结构化信息至关重要**：显式地建模标签间的层次或关联关系（如使用GNN或辅助任务）相比扁平化的方法能带来显著的性能提升。消融实验普遍证实，移除标签结构建模模块会导致性能下降 [jos.org.cn](https://jos.org.cn/html/2023/12/6802.htm), [html.rhhz.net](https://html.rhhz.net/ZZDXXBLXB/html/20250204.htm)。
    3.  **多粒度特征融合的有效性**：结合词级、句子级乃至文档级的多尺度特征，能够比单一粒度的特征提供更丰富的语义信息，从而提高分类精度 [html.rhhz.net](https://html.rhhz.net/ZZDXXBLXB/html/20250204.htm), [jos.org.cn](https://jos.org.cn/html/2023/12/6802.htm)。
    4.  **专用损失函数的优势**：针对多标签场景中固有的数据不平衡和标签噪声问题，专门设计的损失函数（如ASL）比通用损失函数能更有效地指导模型优化，并取得实质性改进 [blog.csdn.net](https://blog.csdn.net/weixin_43424450/article/details/147364959)。

#### **趋势与挑战**

基于上述研究，我们预测2025年前后多标签学习系统将呈现以下发展趋势，并面临相应挑战：

1.  **从判别式到生成式范式的转变**：以G-HXMLC为代表的研究表明，生成式模型在处理超大规模标签空间和可变数量标签输出方面具有天然优势 [aclanthology.org](https://aclanthology.org/2022.ccl-1.60.pdf)。未来，研究将进一步探索如何将生成式范式与约束解码、对比学习等技术结合，以提高生成标签的准确性和多样性，特别是在XMLC和HMTC场景下。
2.  **深度融合多模态与外部知识**：随着多模态大模型的发展，未来的多标签学习系统将不再局限于单一模态，而是致力于构建能够理解和关联文本、图像、音频等多源信息的统一模型 [paper.edu.cn](https://paper.edu.cn/releasepaper/content/202503-143)。利用知识图谱、常识库等外部知识增强模型的推理能力，解决仅靠数据驱动难以处理的语义鸿沟问题，将成为一个关键研究方向。
3.  **动态自适应的学习策略与损失函数**：固定的超参数和损失函数难以适应复杂的训练动态。ASL中提出的自适应不对称机制，即在训练中动态调整聚焦参数，预示着未来的研究方向 [blog.csdn.net](https://blog.csdn.net/weixin_43424450/article/details/147364959)。开发能根据训练阶段、样本难度和类别分布自动调整学习策略的模型将是提高模型鲁棒性和泛化能力的重要途径。

同时，该领域依然面临挑战，包括如何高效处理长尾分布下的少样本标签、如何量化和利用更复杂的标签逻辑关系（超越简单的层次结构），以及如何在保证性能的同时降低极限分类模型的计算与存储开销 [jos.org.cn](https://jos.org.cn/html/2023/12/6802.htm)。

#### **结论**

在2022至2025年间，多标签学习系统的研究取得了显著进展。研究重心已从传统的扁平化分类模型转向更加关注标签结构、数据多粒度和模态融合的复杂系统。通过引入层次建模、生成式范式、多粒度特征融合和创新的损失函数，新一代模型在处理标签相关性、数据不平衡和高维标签空间等核心挑战方面展现出更强的能力。未来的研究将在多模态融合、知识增强和自适应学习策略等方面继续深化，以期构建更强大、更通用的多标签智能系统，应对日益复杂的现实世界应用需求。

#### **参考文献**

1.  [blog.csdn.net](https://blog.csdn.net/weixin_43424450/article/details/147364959). (2025). 【读点论文】Asymmetric Loss For Multi-Label Classification不对称损失，改进版的focal loss，分类处理难易样本.
2.  [html.rhhz.net](https://html.rhhz.net/ZZDXXBLXB/html/20250204.htm). (2025). Hierarchical Multi-label Text Classification Method Based on Multi-scale Feature Extraction. *Journal of Zhengzhou University(Natural Science Edition)*, 57(2), 24-30.
3.  [paper.edu.cn](https://paper.edu.cn/releasepaper/content/202503-143). (2025). 多模态数据的知识增强深度语义学习方法. *中国科技论文在线*.
4.  [manu44.magtech.com.cn](https://manu44.magtech.com.cn/Jwk_infotech_wk3/CN/abstract/abstract5639.shtml). (2024). 基于层次标签结构的标记分布学习. *数据分析与知识发现*, 8(2), 44-55.
5.  [cgsjournals.com](https://www.cgsjournals.com/article/doi/10.6046/zrzyyg.2023027). (2024). 多标签遥感图像分类研究现状与展望. *自然资源遥感*, 36(2), 10-20.
6.  [publicadministration.desa.un.org](https://publicadministration.desa.un.org/sites/default/files/publications/report/2024/World%20Public%20Sector%20Report%202023CN0811-ok.pdf). (2024). 世界公共部门报告（2023）. *联合国经济和社会事务部*.
7.  [jos.org.cn](https://jos.org.cn/html/2023/12/6802.htm). (2023). Multi-label Text Classification with Enhancing Multi-granularity Information Relations. *Journal of Software*, 34(12), 5686-5703.
8.  [www.zhuanzhi.ai](https://www.zhuanzhi.ai/paper/c9a665a1f4cad6f1705fd734cf38d1e9). (2023). Recent Advances in Hierarchical Multi-label Text Classification: A Survey. *arXiv*.
9.  [aclanthology.org](https://aclanthology.org/2022.ccl-1.60.pdf). (2022). 生成模型在层次结构极限多标签文本分类中的应用. *Proceedings of the 21st China National Conference on Computational Linguistics*.
10. [www.zhuanzhi.ai](https://www.zhuanzhi.ai/paper/fd09515cfd452cf42c63785c933fec66). (2022). ZLPR: A Novel Loss for Multi-label Classification. *arXiv*.
11. Devlin, J., Chang, M. W., Lee, K., & Toutanova, K. (2019). BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding. *arXiv:1810.04805*. Cited in [jos.org.cn](https://jos.org.cn/html/2023/12/6802.htm).
12. Wang, Z., Wang, P., Huang, L., et al. (2022). Incorporating Hierarchy into Text Encoder: A Contrastive Learning Approach for Hierarchical Text Classification. *Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics*. Cited in [html.rhhz.net](https://html.rhhz.net/ZZDXXBLXB/html/20250204.htm).