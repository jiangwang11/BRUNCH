# 基于深度学习的组织病理学在癌症诊断与预后中的应用：2022–2025年研究综述

## 引言

组织病理学图像作为癌症诊断的“金标准”，蕴含丰富的形态学与微环境信息。传统人工判读高度依赖经验、效率低下且存在主观变异。2022年以来，深度学习（Deep Learning, DL）技术，尤其是自监督学习（Self-Supervised Learning, SSL）和基础模型（Foundation Model）范式的兴起，极大推动了计算病理学的发展。这些方法能够从十亿像素级的全切片图像（Whole Slide Image, WSI）中自动提取高维、可泛化的特征，实现从癌症检测、分子亚型分类到患者生存预测的端到端分析。本文综述2022–2025年间该领域的代表性工作，系统梳理方法演进、共性结论，并对未来趋势进行展望。

## 方法分类与代表作

### 1. 基于自监督学习的基础模型

自监督学习通过设计预训练任务（如掩码图像建模、对比学习）从海量无标注病理图像中学习通用表征，解决了标注数据稀缺的核心瓶颈。

**BEPH (Nat Commun, 2025)**：俞章盛与张岳团队开发的BEiT-based foundation model，利用掩码图像建模（Masked Image Modeling, MIM）在1100万张未标记病理图像上进行预训练。该模型在补丁级诊断、WSI级癌症分类（如肾细胞癌、肺癌亚型）及六种癌症的生存预测任务上均超越了现有最优模型，证明了其强大的泛化能力与任务适应性[medsci.cn](https://m.medsci.cn/article/show_article.do?id=81d08609091b)。

**Virchow (Nat Med, 2024)**：该模型是迄今为止规模最大的计算病理学基础模型，基于DINOv2自监督算法，在来自约10万患者的150万张WSI上训练。Virchow在9种常见癌和7种罕见癌的检测中达到0.95的平均AUC，尤其在数据稀缺的罕见癌上性能超越特定任务模型，展示了大规模基础模型在应对分布外（out-of-distribution）数据上的优越性[medsci.cn](https://www.medsci.cn/article/show_article.do?id=254a8359e6b7)。

**CHIEF (Nature, 2024)**：由哈佛与腾讯AI Lab联合开发，CHIEF采用无监督（瓦片级）与弱监督（WSI级）相结合的预训练策略。该模型在涵盖19个解剖部位的6万余张WSI上训练，并在32个独立数据集上验证。CHIEF在癌症检测、肿瘤起源识别、基因突变预测和生存分析等任务上，比现有方法性能提升最高达36.1%，有效缓解了由不同扫描协议和人群差异引起的领域偏移[csdn.net](https://blog.csdn.net/m0_59164304/article/details/143807364)。

### 2. 面向特定癌症的诊断与分型模型

针对特定癌症类型，研究者开发了精细的深度学习架构以解决其独特的临床问题。

**HIPOS (Genome Med, 2025)**：应建明/杨琳团队为解决小细胞肺癌（SCLC）高度异质性与风险分层难题，开发了基于深度学习的组织形态学表型（HIPO）分析框架。该框架从H&E染色WSI中鉴定出15种独特的组织形态学表型，并据此将SCLC分为HIPOS-I（免疫浸润型，预后好）和HIPOS-II（纤维化/冷肿瘤型，预后差）两个亚型，为SCLC的精准管理提供了新依据[medsci.cn](https://www.medsci.cn/article/show_article.do?id=bc6b891046ab)。

### 3. 多模态融合与预后预测模型

将病理图像与其他数据源（如临床信息、基因组学）融合，可构建更全面的预后预测模型。

**多参数MRI影像组学/DL (中国癌症杂志, 2025)**：曾延玮等针对弥漫大B细胞淋巴瘤（DLBCL），基于多参数MRI（T1-CE, T2-FLAIR, ADC）构建了影像组学和深度学习模型以无创鉴别其GCB与non-GCB亚型。研究发现，高斯过程（GP）影像组学模型（AUC=0.900）和DenseNet121深度学习模型（AUC=0.846）性能均显著优于经验丰富的放射科医师（最高AUC=0.678），展示了多模态影像在无创分子分型中的巨大潜力[china-oncology.com](https://www.china-oncology.com/CN/10.19401/j.cnki.1007-3639.2025.08.001)。

**直肠癌肿瘤出芽评估 (磁共振成像, 2025)**：Liu等采用3D Vision Transformer (3D ViT)模型，直接处理三维MRI数据来预测直肠癌的肿瘤出芽（TB）分级。其AUC（0.796-0.896）显著高于传统影像组学模型（0.614-0.754），证明了3D Transformer在捕捉肿瘤三维空间异质性特征方面的优势[med-sci.cn](https://www.med-sci.cn/cgzcx/articlexml.asp?doi=10.12015%2Fissn.1674-8034.2025.08.033&html=)。

**胃癌预后与治疗反应 (中国癌症杂志, 2025)**：彭东阁等综述指出，结合多组学数据的AI模型在胃癌化疗和靶向治疗反应预测方面展现出巨大潜力。例如，基于CNN和Transformer混合架构的MuMo模型，在预测HER2阳性胃癌患者靶向治疗疗效时，AUC分别达到0.821和0.914，能有效进行风险分层[china-oncology.com](https://www.china-oncology.com/CN/abstract/abstract2187.shtml)。

## 实验与评价总结

对上述代表性工作的实验结果进行归纳，可得出以下共性结论：
1.  **基础模型的泛化优势**：基于大规模无/弱监督预训练的基础模型（如BEPQ, Virchow, CHIEF）在跨癌种、跨数据集的诊断和预测任务上，其性能和鲁棒性普遍优于在单一任务上从头训练或在自然图像上预训练的模型。
2.  **数据效率的提升**：自监督预训练显著降低了对下游任务标注数据的依赖。例如，BEPH模型仅用50%的训练数据即可达到在100%数据上训练的弱监督模型的性能。
3.  **多模态融合的价值**：将病理图像与其他模态（如MRI、临床数据）信息融合，或在模型内部引入多尺度、3D上下文信息（如3D ViT），能够更全面地刻画肿瘤的生物学特性，从而提升诊断准确性（如DLBCL亚型分类）和预后预测能力（如直肠癌TB分级）。
4.  **可解释性与生物学关联**：先进的可视化技术（如Grad-CAM、热力图）能够将模型关注区域与病理学家标注的病变区域对齐，并揭示模型决策所依据的形态学特征（如肿瘤浸润淋巴细胞、坏死区域），增强了模型的可信度和生物学意义。

## 趋势与挑战

基于2022–2025年的研究进展，预测未来1-2年该领域将呈现以下趋势：
1.  **通用病理大模型的持续演进与开源**：以CHIEF、BEPH等为代表的通用基础模型将成为计算病理学的新基础设施。未来工作将聚焦于更大规模、更多样化的数据集训练，以及更高效的预训练算法。同时，模型开源（如BEPH已开源）将加速社区协作与临床转化。
2.  **从诊断到治疗决策的闭环构建**：研究重点将从单纯的诊断/预后预测，转向构建能够直接指导治疗选择的AI系统。这要求模型不仅能预测生存，还需准确预测对特定化疗、放疗、免疫或靶向治疗的反应，并与临床决策流程深度整合。
3.  **多模态、多尺度数据的深度融合**：未来的前沿模型将不再局限于单一的WSI，而是系统性地整合病理图像、放射影像（CT/MRI/PET）、基因组学、转录组学、蛋白质组学及电子健康记录等多维度数据，构建患者的“数字孪生”，以实现真正意义上的精准医疗。

然而，这些趋势的实现仍面临严峻挑战，包括高质量、多中心、标准化标注数据集的匮乏，模型在真实世界临床环境中的前瞻性验证不足，以及算法“黑箱”特性带来的信任与责任问题。

## 结论

2022–2025年是深度学习驱动计算病理学从研究走向临床应用的关键时期。自监督学习和基础模型范式成功解决了数据标注瓶颈，显著提升了模型的泛化能力和跨任务适应性。面向特定癌症的精细模型和多模态融合策略，则在无创分型、预后评估和治疗反应预测等临床关键问题上取得了实质性突破。展望未来，构建可信赖、可解释、能融入临床工作流并指导精准治疗的多模态AI系统，将是该领域最核心的发展方向。

## 参考文献

1.  Yang, Z., Wei, T., Liang, Y. et al. A foundation model for generalizable cancer diagnosis and survival prediction from histopathological images. Nat Commun 16, 2366 (2025).
2.  Vorontsov, E., Bozkurt, A., Casson, A. et al. A foundation model for clinical-grade computational pathology and rare cancers detection. Nat Med (2024).
3.  Wang, X.Y., Zhao, J.H., Marostica, E. et al. A pathology foundation model for cancer diagnosis and prognosis prediction. Nature 634, 970–978 (2024).
4.  Zhang, Y., Liu, S., Chen, J. et al. Deep learning-based histomorphological subtyping and risk stratification of small cell lung cancer from hematoxylin and eosin-stained whole slide images. Genome Med 17, 98 (2025).
5.  Zeng, Y., Xu, Z., Cao, X. et al. MRI-based radiomics and deep learning model construction: non-invasive differentiation of molecular subtypes in primary intracranial diffuse large B-cell lymphoma. China Oncol 35, 735-742 (2025).
6.  Liu, Z., Yang, H., Nie, L. et al. Prediction of tumor budding grading in rectal cancer using a multiparametric MRI radiomics combined with a 3D vision transformer deep learning approach. Acad Radiol 32, 4512-4523 (2025).
7.  Peng, D., Wan, Z. & Lu, N. Artificial intelligence in gastric cancer diagnosis, treatment and prognostic prediction: current application and future perspective. China Oncol 35, 496-504 (2025).
8.  张小燕, 刘念军, 张益铭, 等. 多模态磁共振成像及影像组学评估直肠癌肿瘤出芽的研究进展. 磁共振成像, 2025, 16(8): 221-227.
9.  曾延玮, 徐智坚, 曹鑫, 等. 基于MRI的影像组学和深度学习模型构建：无创鉴别原发颅内弥漫大B细胞淋巴瘤分子亚型. 中国癌症杂志, 2025, 35(8): 735-742.
10. Marra, A., Morganti, S., Pareja, F. et al. Artificial intelligence entering the pathology arena in oncology: current applications and future perspectives. Ann Oncol. 2025 Jul;36(7):712-725.
11. Peng, L., Wang, D., Zhuang, Z. et al. Preoperative noninvasive evaluation of tumor budding in rectal cancer using multiparameter MRI radiomics. Acad Radiol, 2024, 31(6): 2334-2345.
12. Chen, Z., Chen, Y., Sun, Y. et al. Predicting gastric cancer response to anti-HER2 therapy or anti-HER2 combined immunotherapy based on multi-modal data. Signal Transduct Target Ther 9, 222 (2024).