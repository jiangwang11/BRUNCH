好的，作为一名严谨的科研助手，我将基于提供的真实网络搜索结果，为您生成一篇关于“标签高效的医学诊断深度学习方法”的中文学术综述。

***

### **面向医学诊断的标签高效深度学习方法研究综述 (2022–2025)**

#### **摘要**

深度学习在医学图像辅助诊断中展现了巨大潜力，但其性能高度依赖大规模、高质量的标注数据集。在医疗领域，获取此类数据集不仅成本高昂，且需耗费大量专家时间，成为制约技术落地应用的关键瓶颈。标签高效学习（Label-Efficient Learning）旨在通过最少的标注数据实现模型性能最大化，是解决此问题的核心途径。本综述聚焦于 2022 年至 2025 年间，系统梳理并总结了面向医学诊断的标签高效深度学习方法的代表性研究，主要涵盖半监督学习、主动学习与人机协同、小样本与元学习，以及联邦学习与知识蒸馏等关键技术分支。通过对各类别核心思想与代表性工作的分析，本综述提炼了现有方法的共性评价模式与实验结论，并对未来三至五年的研究趋势与挑战进行了展望，以期为相关领域的研究人员提供参考。

---

#### **1. 引言**

近年来，以卷积神经网络（CNNs）和视觉变换器（Vision Transformers）为代表的深度学习模型，在各类医学图像诊断任务（如肿瘤分类、病灶分割、疾病分级等）中取得了媲美甚至超越人类专家的表现。然而，这些成就的背后是“数据驱动”的本质，即模型性能的提升强依赖于海量的标注数据。在临床实践中，医学图像的标注工作面临三大挑战：1) **专业性壁垒**：标注需由具备深厚专业知识的资深医师完成，人力资源稀缺；2) **成本与时间**：标注过程耗时费力，经济成本高昂；3) **数据隐私与稀有性**：患者数据隐私保护要求严格，且罕见病病例数据本身就极为稀少。

为了突破“标签瓶颈”，标签高效学习应运而生。它并非单一技术，而是一系列旨在减少对标注数据依赖的方法论集合。其核心目标是在保证或略微牺牲模型性能的前提下，显著降低所需的标注样本数量。本文将系统梳理 2022 年至 2025 年间在医学诊断领域的四类主流标签高效学习方法：半监督学习、主动学习与人机协同、小样本与元学习、以及面向分布式数据的联邦学习与知识蒸馏，并分析其代表性工作、评价体系与未来趋势。

#### **2. 方法分类与代表作**

##### **2.1 半监督学习 (Semi-supervised Learning, SSL)**

半监督学习旨在同时利用少量有标签数据和大量无标签数据进行模型训练。其基本假设是数据在特征空间中存在内在结构（如聚类假设），无标签数据有助于模型学习更鲁棒、泛化能力更强的特征表示。

*   **UniSAL (Unified Semi-supervised Active Learning)**：该研究针对组织病理学图像分类中标注成本高的问题，提出了一个统一的半监督主动学习框架 [blog.csdn.net](https://blog.csdn.net/weixin_38594676/article/details/148796230)。UniSAL采用双网络架构，通过“双视图高置信度伪训练(DHPT)”机制，使两个网络相互提供高质量伪标签，从未标注数据中学习。同时，引入伪标签引导的类内对比学习，强制不同类别的特征在潜在空间中分离。实验表明，该方法仅需约10%的标注数据，即可达到与全监督学习相当的性能，显著降低了标注需求。

*   **USSL4MIC (Universal Semi-Supervised Learning for Medical Image Classification)**：该工作面向更真实的“开放世界”场景，即未标注数据可能包含未知类别或来自不同领域。研究者提出了一个普适性半监督学习框架，能够处理类别和领域不匹配的问题 [blog.csdn.net](https://blog.csdn.net/qq_42722197/article/details/144948598)。其核心是“双路径异常估计(DOE)”技术，结合特征相似性和分类器置信度来识别未知类别样本。对于未知领域样本，则通过变分自编码器(VAE)预训练进行检测，并利用领域自适应技术对齐特征。该框架在皮肤病和眼科数据集上验证了其在复杂、异构数据环境下的有效性。

##### **2.2 主动学习 (Active Learning, AL) 与人机协同**

主动学习的核心思想是“让模型选择最值得标注的样本”。模型通过查询策略（Query Strategy）识别出对自身学习最“有价值”（如最不确定或最具代表性）的未标注样本，交由专家进行标注，然后用新增的标注数据迭代更新模型。

*   **基于深度主动学习的半自动标注系统**：该研究设计并实现了一个Web化的医学图像半自动标注系统，其核心是一种混合式主动学习查询策略 [www.c-s-a.org.cn](https://www.c-s-a.org.cn/html/2023/2/8962.html)。该策略分两阶段进行：首先，基于委员会（Ensemble）模型间的预测差异，筛选出一批不确定性最高的样本；然后，在这些样本中，通过计算特征相似度，选出多样性最好、最不相似的一批样本提交给用户标注。在新冠肺炎CT分割数据集上的实验证明，该方法仅用50%的标注量就基本达到了全量标注的效果，有效降低了标注冗余。

*   **IMIL (Interactive Medical Image Learning Framework)**：此研究提出了一种更为直接的人机交互学习框架，让临床医生的指导贯穿于训练过程 [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/6b3eb1e3-397d-47c1-a10c-7faaefe06de2)。当模型对某些样本做出错误预测时，临床医生可以介入，通过交互式工具“涂黑”图像中的无关区域（如伪影或背景），强制模型关注与诊断相关的核心视觉特征。这种针对性的数据增强方式能够有效纠正模型的“注意力偏差”。在仅对4%的训练集应用IMIL后，ResNet-50模型的分类准确率提升了4.2%，证明了专家先验知识在矫正模型学习路径上的巨大价值。

##### **2.3 小样本学习 (Few-shot Learning, FSL) 与元学习**

小样本学习专注于让模型从每个类别仅有的极少数（通常为1-10个）标注样本中学习。元学习（Meta-Learning），或称“学会学习”，是实现小样本学习的主流方法之一，它通过在大量相似任务上进行训练，使模型掌握快速适应新任务的元知识。

*   **基于深度元学习的医学图像分类研究**：该工作提出了一种结合迁移学习和元学习的多阶段小样本学习方法 [image.hanspub.org](https://image.hanspub.org/html/15-1543024_75899.htm)。首先，使用预训练的Vision Transformer (ViT)作为强大的特征提取器；其次，在大型通用数据集(Mini-ImageNet)上训练一个原型网络（Prototypical Network），使其学会通用的度量学习能力；最后，在目标医学图像任务上仅微调一个轻量级的分类器。在血液和病理学两个数据集的3-way 10-shot任务上，该方法分别取得了95.3%和94.93%的准确率，验证了其有效性。

*   **PM2 (Prompting Multi-modal Model Paradigm)**：这项2024年的研究探索了利用大型多模态模型进行小样本医学图像分类的新范式 [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/2b577567-2a8e-43d6-8c04-b55abd60275e)。其核心思想是，除了输入图像，还为模型提供描述图像或类别概念的文本“提示（Prompt）”，将图像分类任务转化为图文匹配问题。通过实证研究五种不同的提示方案，该方法显著增强了模型在少样本场景下的学习能力。这项工作表明，融合文本模态的先验知识能有效弥补视觉样本的不足。

##### **2.4 联邦学习 (Federated Learning, FL) 与知识蒸馏**

当数据因隐私法规或机构壁垒无法集中时，联邦学习提供了一种在保护数据隐私的前提下进行协同训练的方案。知识蒸馏则是一种模型压缩和知识迁移技术，可以将一个大型、复杂的“教师模型”的知识迁移到一个轻量级的“学生模型”中。

*   **FedFew (Federated Few-shot Learning)**：此研究解决了联邦学习中一个非常实际的挑战：部分客户端（医院）可能只拥有少数罕见病的少量标注样本 [zhuanzhi.ai](https://zhuanzhi.ai/paper/d0648b22154d63471c2b37d6023d4312)。标准联邦学习在这种极端类别不平衡和数据异构性下容易失效。FedFew框架通过三阶段解决此问题：首先通过联邦自监督学习获取通用的表征；然后利用部分标注数据学习常见病的分类器；最后，基于能量模型检测出代表性不足的罕见类别，并使用基于原型的少样本匹配方法进行识别。

*   **ProtoKD (Prototype Knowledge Distillation)**：该方法旨在解决多模态医学图像分割中常见的“模态缺失”问题，即训练时拥有多模态数据（如MRI的T1、T2、FLAIR序列），但推理时可能只有单一模态可用 [www.zhuanzhi.ai](https://www.zhuanzhi.ai/paper/00ac389db451f7f5a93aae3e4af92a83)。ProtoKD通过原型知识蒸馏，将一个在多模态数据上训练的教师模型的知识（包括像素级知识和类内/类间特征变化）迁移给一个仅在单模态上训练的学生模型。这使得学生模型仅使用单一模态输入，也能达到接近教师模型的分割性能，在BraTS基准测试上取得了SOTA表现。

#### **3. 实验与评价总结**

综合上述代表性工作，可以总结出以下共性结论：

1.  **评价标准**：标签高效学习的评价核心是“性价比”，即在给定标注预算（如使用1%、5%、10%的标签）下，模型性能（如准确率、F1分数、Mean IoU）能达到全监督学习性能的何种程度。因此，性能-标注量曲线是该领域论文中最核心的评价图表。
2.  **数据集选择**：研究普遍在公开的医学图像数据集（如皮肤镜图像ISIC系列、组织病理学NCT-CRC-100K、眼底图像等）上进行验证。部分元学习方法会使用大型非医学数据集（如Mini-ImageNet）进行元知识的预训练，以增强模型泛化性。此外，如 **MedXpertQA** [c3i.ee.tsinghua.edu.cn](https://c3i.ee.tsinghua.edu.cn/publication/yuxin_zuo_medxpertqa-benchmarking-expert-level-medical-reasoning-and-understanding_arxiv2025/) 这样的新型、高难度基准的出现，正推动评价标准从简单的图像分类向复杂的临床推理能力演进。
3.  **通用发现**：
    *   **混合方法优势**：将不同范式结合（如UniSAL中的半监督与主动学习）通常比单一方法更有效，能够互补短板。
    *   **先验知识的重要性**：无论是通过迁移学习利用预训练权重，还是通过多模态提示（PM2）引入文本知识，亦或是通过人机交互（IMIL）注入专家经验，外部先验知识的融入是弥补标签稀缺的有效手段。
    *   **对真实世界问题的关注**：最新的研究（如USSL4MIC, FedFew）已不再满足于理想化的“封闭世界”假设，而是开始着手解决数据异构、类别不均衡、模态缺失等更贴近临床的复杂问题。

#### **4. 趋势与挑战**

基于2024-2025年的最新研究，未来医学诊断领域的标签高效学习将呈现以下趋势与挑战：

1.  **从单一范式到统一框架的演进**：未来的研究将更倾向于构建能够同时处理多种数据不完美（如标签稀疏、类别开放、领域迁移、数据异构）的统一框架。如USSL4MIC和UniSAL所示，单一的SSL或AL已不足以应对真实世界数据的复杂性，集成开放集识别、领域自适应、主动学习和半监督学习的统一模型将是重要方向。
2.  **与大型基础模型的深度融合**：大型语言模型（LLMs）和大型多模态模型（LMMs）的崛起为医学诊断带来了新的机遇。如PM2的探索，未来的研究将不仅限于用文本提示辅助图像分类，更会发展为利用LMMs强大的上下文理解和推理能力，直接整合电子病历（EMR）、检验报告、影像学报告和医学图像，进行端到端的、更接近临床医生思维方式的诊断。`MedXpertQA`基准的提出正是为了衡量这种高级推理能力。
3.  **交互式学习与可解释性的结合**：为了让模型真正成为医生的可靠助手，“黑箱”属性必须被打破。IMIL框架是一个开端，未来的系统将更加注重交互性与可解释性。医生不仅是标注者，更是模型的“导师”和“审查员”，他们需要理解模型为何做出某个判断（可解释性），并能高效地纠正其错误（交互式学习）。这将建立人机之间的信任，是AI在严肃医疗领域落地的必要条件。
4.  **联邦学习与隐私计算的深化**：随着全球数据安全法规的日益严格，FedFew所代表的联邦学习方法将从“可选项”变为“必需品”。未来的挑战在于如何在保证隐私和安全的前提下，高效处理各节点（医院）间的统计异质性（Non-IID）和系统异质性，并结合差分隐私等更强的隐私保护技术，实现既安全又高效的标签高效协同学习。

#### **5. 结论**

标签高效深度学习是推动人工智能在医学诊断领域广泛应用的关键技术。本综述通过梳理2022至2025年的代表性工作，展示了半监督学习、主动学习、小样本学习及联邦学习等方法在该领域的最新进展。研究趋势表明，该领域正从解决理想化问题，转向构建能够应对真实世界复杂性的统一、交互式、多模态智能框架。尽管挑战依然存在，但随着技术的不断演进，标签高效学习必将为构建更智能、更可靠、更易于部署的临床决策支持系统铺平道路。

---

#### **6. 参考文献**

1.  Dong, N., Kampffmeyer, M., & Voiculescu, I. (2022). *Learning Underrepresented Classes from Decentralized Partially Labeled Medical Images*. In MICCAI 2022. [[zhuanzhi.ai](https://zhuanzhi.ai/paper/d0648b22154d63471c2b37d6023d4312)]
2.  Wang, Z., Sun, Q., Zhang, B., et al. (2024). *PM2: A New Prompting Multi-modal Model Paradigm for Few-shot Medical Image Classification*. arXiv preprint. [[hub.baai.ac.cn](https://hub.baai.ac.cn/paper/2b577567-2a8e-43d6-8c04-b55abd60275e)]
3.  Rao, A., Fisher, A., Chang, K., et al. (2024). *IMIL: Interactive Medical Image Learning Framework*. arXiv preprint. [[hub.baai.ac.cn](https://hub.baai.ac.cn/paper/6b3eb1e3-397d-47c1-a10c-7faaefe06de2)]
4.  Wang, S., Yan, Z., Zhang, D., et al. (2023). *Prototype Knowledge Distillation for Medical Segmentation with Missing Modality*. In ICASSP 2023. [[www.zhuanzhi.ai](https://www.zhuanzhi.ai/paper/00ac389db451f7f5a93aae3e4af92a83)]
5.  Dong, D., Zhang, Z., & Zhang, Q. (2023). Research on Medical Image Classification Based on Deep Meta-Learning. *Computer Science and Application*, 13(11). [[image.hanspub.org](https://image.hanspub.org/html/15-1543024_75899.htm)]
6.  Wang, H., Feng, R., & Zhang, X. (2023). Semi-automatic Labeling System for Medical Images Based on Deep Active Learning. *Computer Systems & Applications*, 32(2). [[www.c-s-a.org.cn](https://www.c-s-a.org.cn/html/2023/2/8962.html)]
7.  Zuo, Y., Qu, S., Xie, L., et al. (2025). *MedXpertQA: Benchmarking Expert-Level Medical Reasoning and Understanding*. In ICML 2025 (expected). [[c3i.ee.tsinghua.edu.cn](https://c3i.ee.tsinghua.edu.cn/publication/yuxin_zuo_medxpertqa-benchmarking-expert-level-medical-reasoning-and-understanding_arxiv2025/)]
8.  (2025). *UniSAL: Unified Semi-supervised Active Learning for histopathological image classification*. Blog post summarizing recent work. [[blog.csdn.net](https://blog.csdn.net/weixin_38594676/article/details/148796230)]
9.  Ju, L., Wu, Y., Feng, W., et al. (2024). *Universal Semi-Supervised Learning for Medical Image Classification*. In MICCAI 2024. [[blog.csdn.net](https://blog.csdn.net/qq_42722197/article/details/144948598)]