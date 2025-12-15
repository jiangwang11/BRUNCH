# 用户搜索行为建模与预测技术综述（2022–2025）

## 引言

用户搜索行为预测旨在从历史交互序列中建模用户意图演化，为推荐、广告、查询建议等下游任务提供精准表征。2022–2025 年间，该领域经历了从传统序列模型向大语言模型（LLM）与多任务联合建模范式的演进。研究焦点从单一行为建模转向跨域行为转换（如搜索与推荐）、多粒度意图解析与可信预测机制构建。本文系统梳理该时期内方法论进展，按技术路线划分为四类：基于深度序列建模的方法、搜索与推荐联合建模、LLM 增强的行为理解与生成、以及面向可信性的预测机制设计，并总结实验范式与未来趋势。

## 方法分类与代表作

### 1. 基于深度序列建模的行为预测

该方向聚焦于利用 RNN、Transformer 等架构捕捉行为序列中的时序依赖。  
**Gu et al. (2023)** 针对短视频场景中多行为点击预测问题，提出 USCP 模型，在 DeepFM 基础上引入 Word2Vec 对用户行为序列进行嵌入学习，以建模动态兴趣演化。在真实短视频数据集上，USCP 在 GAUC 指标上优于 Wide&Deep、MMOE 等基线，表明序列建模能有效提升多行为预测精度 [jeit.ac.cn](https://jeit.ac.cn/cn/article/doi/10.11999/JEIT211458?viewType=HTML)。  
**Zhang et al. (2025)** 将学术用户文献下载行为预测建模为时间序列问题，分别从查询重构、查询表达式和下载行为中提取特征，并利用 LSTM 建模会话序列。实验表明，查询表达式特征对下载次数预测最有效，而历史下载特征对时间间隔预测更优，验证了多源行为特征的互补性 [qbxb.istic.ac.cn](https://qbxb.istic.ac.cn/CN/abstract/abstract893.shtml)。  
**Chen et al. (2025)** 提出 DEEPER 框架，通过强化学习迭代优化用户画像，利用行为-预测残差指导画像更新方向。在包含 4800 用户的动态数据集上，四轮更新后行为预测误差平均降低 32.2%，显著优于重生成或增量扩展基线，证明了定向细化对动态画像的有效性 [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/108737)。

### 2. 搜索与推荐的联合建模

随着平台融合搜索与推荐入口，建模二者间的行为转换成为新范式。  
**Shi et al. (2024)** 提出 UniSAR 框架，通过“提取-对齐-融合”三阶段建模用户在搜索与推荐间的细粒度行为转换：使用掩码 Transformer 提取行为、对比学习对齐转换、交叉注意力融合多类转换。在 Amazon 和 Yelp 两个公共数据集上，UniSAR 同时提升了搜索与推荐任务的性能，验证了联合建模的互益性 [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/54939b8f-9a27-4934-ae16-63679f949f36)。

### 3. LLM 增强的行为理解与生成

LLM 被用于提升查询建议、相关性判断与特征生成的质量。  
**Tian et al. (2024)** 系统综述了基于深度学习的查询建议方法，将其分为生成式（如 Seq2Seq、VAE）与排序式（如基于 BERT 的重排序）两类，并分析了各模型在特征利用与生成质量上的差异。该综述指出，融合上下文与会话历史的 LLM 方法在多样性与相关性上更具优势 [crad.ict.ac.cn](https://crad.ict.ac.cn/cn/article/id/64716d2d-5a8e-41cc-b1d4-57791c57849d)。  
**Zhao et al. (2025)** 针对电商搜索广告相关性建模，提出可解释 LLM（ELLM-rele），将相关性判断重构为品类、品牌等维度的思维链（CoT）推理，并通过多维知识蒸馏（MKD）将概率分布与 CoT 知识迁移到在线小模型。离线与在线实验均表明 MKD 显著提升长尾场景的泛化能力与用户体验 [hub.baai.ac.cn](https://hub.baai.ac.cn/view/45166)。  
**Liu et al. (2025)** 探索在推荐系统中使用 LLM 进行特征增强，发现标准快速推理生成的特征存在覆盖不全、描述笼统问题。引入推理计算扩展（如 CoT）后，模型生成更多细粒度、具体化的用户偏好特征，使 NDCG@10 提升 12%，证明了扩展推理对特征质量的提升作用 [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/111009)。

### 4. 面向可信性的预测机制

面对多模态数据噪声与预测不确定性，可信推荐机制被提出。  
**Yan et al. (2025)** 提出 Large-TR 算法，利用 LLM 强大的语言理解能力过滤多模态数据（如评论、图片）中的噪声，并设计可信决策机制动态评估推荐结果的不确定性。在四个公开数据集上，Large-TR 均优于基线，尤其在高噪声场景下表现稳健 [crad.ict.ac.cn](https://crad.ict.ac.cn/article/doi/10.7544/issn1000-1239.202440433?viewType=HTML)。  
**Wang et al. (2024)** 通过用户实验比较 LLM 与传统搜索引擎在不同任务复杂度下的信息价值感知差异，发现 LLM 在复杂任务中提供更高感知价值，但在简单任务中易因“幻觉”降低可信度。该研究为 LLM 与搜索系统的协同设计提供了用户行为依据 [lis.ac.cn](https://www.lis.ac.cn/CN/10.13266/j.issn.0252-3116.2025.12.008)。

## 实验与评价总结

2022–2025 年相关研究在实验设计上呈现以下共性：  
- **数据集**：普遍采用真实平台日志（如短视频、电商、学术搜索）或公共数据集（Amazon、Yelp），注重行为序列的时序性与多行为标签。  
- **评价指标**：排序任务多用 NDCG、MRR、GAUC；分类任务用 Accuracy、F1；新引入的可信性评估依赖不确定性量化或人工评估。  
- **核心结论**：  
  1. 建模用户行为序列的动态性（如通过 LSTM、Transformer）显著优于静态特征模型；  
  2. 联合建模搜索与推荐、或引入多模态信号，能有效缓解数据稀疏与冷启动问题；  
  3. LLM 作为特征生成器或教师模型，在提升细粒度理解与长尾泛化方面效果显著，但需通过蒸馏或可信机制解决部署与幻觉问题；  
  4. 用户行为预测的准确性高度依赖于行为类型的细粒度划分与特征工程（如查询重构、表达式解析）。

## 趋势与挑战

基于近期工作，2025 年前后的主要研究趋势包括：  
1. **推理扩展在行为建模中的系统化应用**：继 Liu et al. (2025) 的初步探索，未来将发展更高效的推理策略（如自适应 CoT、多步验证）用于生成高保真用户画像与行为预测，而非仅用于特征增强。  
2. **跨模态、跨任务的统一行为表征**：UniSAR 等工作开启了统一建模的先河，下一步将融合文本、视觉、交互等多模态信号，构建可迁移的通用用户行为基础模型（User Behavior Foundation Model）。  
3. **可信与可解释性的内生设计**：如 Large-TR 和 ELLM-rele 所示，未来模型将不再仅追求性能，而是将不确定性估计、反事实解释、偏差检测等机制嵌入架构本身，以满足高风险场景（如医疗、金融信息检索）的合规需求。

主要挑战包括：LLM 推理成本与在线延迟的平衡、多源行为数据的异构对齐、以及用户隐私保护下的分布式行为建模。

## 结论

2022–2025 年，用户搜索行为预测研究从序列建模走向 LLM 增强的多模态、跨任务联合学习，并开始关注可信性与可解释性。代表性工作如 UniSAR、ELLM-rele、DEEPER 和 Large-TR 展示了深度学习与大模型在细粒度行为理解、动态画像更新与噪声鲁棒性方面的突破。未来研究将聚焦于高效推理、统一表征与内生可信机制，推动用户行为建模向更智能、可靠与普适的方向发展。

## 参考文献

1. Gu, Y., Wang, Y., & Yang, H. (2023). 基于用户行为序列的短视频用户多行为点击预测模型. *电子与信息学报*, 45(2), 672–679. [jeit.ac.cn](https://jeit.ac.cn/cn/article/doi/10.11999/JEIT211458?viewType=HTML)  
2. Zhang, X., Guo, J., Yang, S., & Gui, S. (2025). 融合学术用户多类行为序列特征的文献下载行为预测研究. *情报学报*, 44(4), 482–494. [qbxb.istic.ac.cn](https://qbxb.istic.ac.cn/CN/abstract/abstract893.shtml)  
3. Chen, A., Du, C., Chen, J., et al. (2025). DEEPER Insight into Your User: Directed Persona Refinement for Dynamic Persona Modeling. *arXiv preprint arXiv:2502.11078*. [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/108737)  
4. Shi, T., Si, Z., Xu, J., et al. (2024). UniSAR: Modeling User Transition Behaviors between Search and Recommendation. *arXiv preprint arXiv:2404.09876*. [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/54939b8f-9a27-4934-ae16-63679f949f36)  
5. Tian, X., Xu, Z., & Wang, Z. (2024). 基于深度学习的查询建议综述. *计算机研究与发展*. [crad.ict.ac.cn](https://crad.ict.ac.cn/cn/article/id/64716d2d-5a8e-41cc-b1d4-57791c57849d)  
6. Zhao, G., Zhang, X., Lu, C., et al. (2025). Explainable LLM-driven Multi-dimensional Distillation for E-Commerce Relevance Learning. In *Proceedings of the ACM Web Conference (WWW'25)*. [hub.baai.ac.cn](https://hub.baai.ac.cn/view/45166)  
7. Liu, W., Du, Z., Zhao, H., et al. (2025). Inference Computation Scaling for Feature Augmentation in Recommendation Systems. *arXiv preprint arXiv:2502.16040*. [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/111009)  
8. Yan, M., Xu, C., Huang, H., Zhao, W., & Guan, Z. (2025). 基于大语言模型的可信多模态推荐算法. *计算机学报*. [crad.ict.ac.cn](https://crad.ict.ac.cn/article/doi/10.7544/issn1000-1239.202440433?viewType=HTML)  
9. Wang, R., Zhang, S., & Guo, W. (2025). 知识增强大语言模型与搜索引擎用户的感知信息价值差异比较研究. *图书情报工作*, 69(12), 90–103. [lis.ac.cn](https://www.lis.ac.cn/CN/10.13266/j.issn.0252-3116.2025.12.008)  
10. Wang, J., Fan, K., Liu, Z., & Wang, J. (2024). 生成式人工智能环境下用户信息检索式行为研究. *数据分析与知识发现*, 8(8-9), 20–30. [manu44.magtech.com.cn](https://manu44.magtech.com.cn/Jwk_infotech_wk3/CN/10.11925/infotech.2096-3467.2023.1145)  
11. Rendle, S. (2010). Factorization machines. In *2010 IEEE International Conference on Data Mining* (pp. 995–1000).  
12. Cheng, H. T., et al. (2016). Wide & deep learning for recommender systems. In *DLRS 2016* (pp. 7–10).