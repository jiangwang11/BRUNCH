# 面向医学诊断的标签高效深度学习方法综述（2022–2025）

## 引言

医学图像分析中的深度学习模型性能高度依赖于大规模高质量标注数据，然而医学标注成本高昂、耗时且需专业领域知识，这严重制约了模型在临床场景中的泛化能力与部署效率。因此，标签高效（Label-Efficient）学习方法成为医学AI研究的核心方向。本文系统综述2022–2025年间在医学诊断任务中具有代表性的标签高效深度学习方法，涵盖联邦学习、主动学习、多实例学习、提示学习及零样本学习等范式，重点分析其解决数据稀缺、标注异构、类别不平衡及跨中心泛化等关键挑战的机制与实证效果。

## 方法分类与代表作

### 1. 联邦学习与类别不平衡处理

在分布式医疗数据场景下，本地客户端常仅标注部分疾病类别，导致模型对稀有病种（underrepresented classes）学习不足。Dong等人提出的**FedFew**框架（MICCAI 2022）[zhuanzhi.ai](https://zhuanzhi.ai/paper/d0648b22154d63471c2b37d6023d4312) 针对此问题设计三阶段流程：首先通过联邦自监督学习获取通用表征；其次利用部分标注数据训练基于能量的多标签分类器；最后基于能量分数检测稀有类别，并采用原型最近邻进行少样本匹配。在胸部X光多标签疾病分类任务中，FedFew显著优于FedAvg等基线，尤其在仅2–3个客户端拥有某病种标签时仍能有效识别。

### 2. 主动学习与样本选择策略

为最小化人工标注工作量，Wang等人开发了基于深度主动学习的**半自动医学图像标注系统**（《计算机系统应用》，2023）[c-s-a.org.cn](https://www.c-s-a.org.cn/html/2023/2/8962.html)。该系统采用基于委员会（ensemble）的不确定性估计与多样性采样相结合的批量查询策略：先筛选不确定性最高的K个样本，再从中选取k个互不相似的样本交由医生标注。在COVID-19 CT分割数据集上，仅使用50%标注数据即达到全监督U-Net的性能（mean IoU: 0.342 vs. 0.327），显著优于随机采样与最大熵采样等策略。

Quan等人进一步提出**TECP**方法（TMI 2024）[csdn.net](https://blog.csdn.net/qq_42722197/article/details/144947558)，解决“哪些图像最值得标注”的问题。该方法通过自监督预训练提取无标签图像特征，并利用低熵超像素或手工关键点作为代理监督信号，计算候选模板与数据空间的相似性得分以评估其代表性。在多个医学图像分类任务中，仅标注Top-5%高分样本即可使模型性能接近全标注训练结果，验证了其在标注预算受限下的高效性。

### 3. 多实例学习（MIL）与弱监督分析

多实例学习天然适用于全切片图像（WSI）等仅提供图像级标签的场景。谢卓恒等人（《集成技术学报》，2025）[jcjs.siat.ac.cn](https://jcjs.siat.ac.cn/article/doi/10.12146/j.issn.2095-3135.20241111001) 系统综述了MIL在肿瘤检测、亚型分级与生存预测中的进展。代表性工作如TransMIL与ABMIL通过注意力机制聚合实例特征，在Camelyon16等数据集上实现>90%的肿瘤区域检测准确率。近期研究通过引入图神经网络或跨模态对齐（如病理-基因组），进一步提升MIL在异构数据下的判别能力。

### 4. 提示学习与少样本医学分类

面对小样本医学分类任务，Wang等人提出**PM2**（Prompting Multi-modal Model）范式（2024）[baai.ac.cn](https://hub.baai.ac.cn/paper/2b577567-2a8e-43d6-8c04-b55abd60275e)，在冻结的视觉-语言模型（如CLIP）基础上引入可学习的文本与图像提示。PM2实证比较了五种提示方案，并创新性地同时利用类别令牌与视觉令牌进行线性分类，充分挖掘高级视觉特征中的统计信息。在CheXpert、OCT等三个医学数据集上，PM2在1-shot和5-shot设置下均达到SOTA，证明提示工程可有效桥接通用模型与医学专业任务。

### 5. 零样本学习与跨中心泛化

针对模型泛化瓶颈，李海团队开发了**MultiXpert**系统（《Information Processing & Management》，2025）[sciencenet.cn](https://paper.sciencenet.cn/htmlpaper/2025/11/20251121142035592142957.shtm)，实现胸片“零样本”诊断。该框架融合大语言模型与放射科专家知识生成病灶描述，通过双流架构对齐图像与语言语义，在无需任何目标疾病标注的情况下识别新发病症。在十家医院的多中心私有数据上，MultiXpert相较传统监督模型（如ViT）AUC提升13.9%–22.6%，显著优于现有视觉-语言模型，为跨机构部署提供新范式。

## 实验与评价总结

综合近年研究，标签高效方法在医学诊断中的有效性已得到广泛验证。共性结论包括：（1）**自监督预训练**（如SimCLR、DINO）作为通用特征提取器，可显著提升下游任务在低标注量下的性能；（2）**不确定性与多样性联合采样**是主动学习中最有效的样本选择策略，避免冗余标注；（3）**多模态对齐**（图像-文本、病理-基因）通过引入外部知识源，缓解单一模态标注不足的局限；（4）**跨中心/跨设备泛化**仍是核心挑战，零样本与联邦学习方法展现出优于传统迁移学习的鲁棒性；（5）**评估指标需任务定制**，如分割任务侧重Dice/mIoU，分类任务关注AUC/F1，检索任务采用MAP/P@K。

## 趋势与挑战

基于2025年前后研究动态，未来趋势包括：
1. **通用医学基础模型与提示工程深度融合**：如Med-Flamingo、RadFM等模型将通过可组合提示（composable prompts）支持复杂诊断推理，减少任务特定微调。
2. **人机协同闭环系统**：IMIL（Interactive Medical Image Learning）[baai.ac.cn](https://hub.baai.ac.cn/paper/6b3eb1e3-397d-47c1-a10c-7faaefe06de2) 等框架将医生反馈实时融入训练循环，实现动态数据增强与错误修正。
3. **跨模态语义哈希与高效检索**：面向大规模医疗数据库，LLM驱动的跨模态哈希（如LSCH）[jeit.ac.cn](https://www.jeit.ac.cn/cn/article/doi/10.11999/JEIT250529?viewType=HTML) 将提升图文检索精度与效率，支持临床决策支持系统。

主要挑战仍在于：标注噪声的鲁棒性、模型可解释性与临床合规性、以及真实世界中数据异构性（设备、协议、人群）对泛化能力的持续考验。

## 结论

2022–2025年，标签高效深度学习在医学诊断领域取得显著进展，从被动减少标注依赖转向主动引导人机协作与知识融合。未来研究需在保证算法效率的同时，强化与临床工作流的整合，并建立更严谨的评估基准以推动技术落地。

## 参考文献

1. Dong, N., Kampffmeyer, M., & Voiculescu, I. (2022). Learning Underrepresented Classes from Decentralized Partially Labeled Medical Images. *MICCAI*. [zhuanzhi.ai](https://zhuanzhi.ai/paper/d0648b22154d63471c2b37d6023d4312)
2. Wang, H., Feng, R., & Zhang, X. (2023). Semi-automatic Labeling System for Medical Images Based on Deep Active Learning. *Computer Systems and Applications*, 32(2), 75–82. [c-s-a.org.cn](https://www.c-s-a.org.cn/html/2023/2/8962.html)
3. Quan, Q., et al. (2024). Which images to label for few-shot medical image analysis? *IEEE Transactions on Medical Imaging (TMI)*. [csdn.net](https://blog.csdn.net/qq_42722197/article/details/144947558)
4. Xie, Z., Yi, M., & Huang, X. (2025). Application Progress of Multi-instance Learning in Medical Image Analysis. *Journal of Integration Technology*, 14(1). [jcjs.siat.ac.cn](https://jcjs.siat.ac.cn/article/doi/10.12146/j.issn.2095-3135.20241111001)
5. Wang, Z., et al. (2024). PM2: A New Prompting Multi-modal Model Paradigm for Few-shot Medical Image Classification. arXiv. [baai.ac.cn](https://hub.baai.ac.cn/paper/2b577567-2a8e-43d6-8c04-b55abd60275e)
6. Rao, A., et al. (2024). IMIL: Interactive Medical Image Learning Framework. arXiv. [baai.ac.cn](https://hub.baai.ac.cn/paper/6b3eb1e3-397d-47c1-a10c-7faaefe06de2)
7. Liu, Q., et al. (2025). Cross Modal Hashing of Medical Image Semantic Mining for Large Language Model. *Journal of Electronics & Information Technology*. [jeit.ac.cn](https://www.jeit.ac.cn/cn/article/doi/10.11999/JEIT250529?viewType=HTML)
8. Li, H., et al. (2025). MultiXpert: Zero-shot chest X-ray diagnosis via multimodal dual-stream协同 enhancement. *Information Processing & Management*, 104468. [sciencenet.cn](https://paper.sciencenet.cn/htmlpaper/2025/11/20251121142035592142957.shtm)
9. Liu, X., et al. (2025). A generalist medical language model for disease diagnosis assistance. *Nature Medicine*, 31(3), 932–942. [ablesci.com](https://www.ablesci.com/scholar/paper?id=3NVkRpjW3)
10. Yang, L., et al. (2017). Suggestive annotation: A deep active learning framework for biomedical image segmentation. *MICCAI*. (被Wang et al., 2023引用)
11. Zhang, Y., et al. (2021). Deep triplet hashing network for case-based medical image retrieval. *Medical Image Analysis*, 69, 101981.
12. Xu, L., et al. (2022). Multi-manifold deep discriminative cross-modal hashing for medical image retrieval. *IEEE Transactions on Image Processing*, 31, 3371–3385.