好的，作为一名严谨的科研助手，我将基于提供的真实网络搜索结果，为您生成一篇关于“组织病理学中用于癌症诊断与预后的深度学习”的学术综述，内容涵盖2022至2025年的代表性工作。

***

### **组织病理学中用于癌症诊断与预后的深度学习技术研究综述**

#### **引言**

组织病理学检查是癌症诊断的“金标准”，但传统的人工阅片存在主观性强、效率低和诊断一致性差等问题。近年来，以深度学习为核心的人工智能技术在计算病理学领域取得了革命性进展，通过对全切片图像（Whole-Slide Images, WSI）进行高通量、定量化分析，极大地提升了癌症诊断、分子分型、预后预测和治疗反应评估的精度与效率 [pdf.hanspub.org](https://pdf.hanspub.org/acm_8104715.pdf)。本综述聚焦于2022至2025年间，系统梳理并评述深度学习在组织病理学癌症研究中的关键方法与代表性工作，重点关注病理基础模型和多模态融合两大前沿方向，并对未来研究趋势与挑战进行展望。

#### **方法分类与代表作**

##### **1. 病理学基础模型 (Foundation Models)**

基础模型通过在海量无标注或弱标注数据上进行大规模预训练，学习通用的、可迁移的病理学特征表示，以适应多种下游任务。这是当前计算病理学领域最核心的研究范式。

*   **Virchow (Nature Medicine, 2024)**
    *   **研究问题**：如何利用单一模型实现覆盖多种常见及罕见癌症的泛癌种检测，以应对罕见癌种训练数据稀缺的挑战 [www.medsci.cn](https://www.medsci.cn/article/show_article.do?id=254a8359e6b7)。
    *   **核心方法**：研究团队开发了迄今规模最大的计算病理学基础模型Virchow。该模型基于Vision Transformer-Huge (ViT-H)架构，利用自监督学习算法（DINO v2）在约150万张覆盖17个主要组织的WSI上进行预训练。
    *   **关键实验结论**：Virchow在泛癌种检测任务中实现了0.95的标本级AUC，显著优于其他模型。尤其是在罕见癌症和分布外（out-of-distribution）数据集上，其性能优势更为突出，证明了大规模预训练带来的卓越泛化能力。

*   **CHIEF (Nature, 2024)**
    *   **研究问题**：解决传统AI模型在应用于不同医院、不同扫描设备或不同人群样本时，因领域偏移（domain shift）导致的性能显著下降问题 [blog.csdn.net](https://blog.csdn.net/m0_59164304/article/details/143807364)。
    *   **核心方法**：CHIEF模型采用一种创新的双重预训练策略。它结合了用于瓦片级（tile-level）特征识别的无监督预训练和用于全切片上下文模式识别的弱监督预训练，在来自19个解剖部位的超过6万张WSI上进行开发。
    *   **关键实验结论**：在包含来自24家国际医院的32个独立测试集上进行验证，CHIEF在处理领域偏移方面的性能比当时最先进的方法提高了高达36.1%，展现了极强的泛化能力和临床适用性。

*   **BEPH (Nature Communications, 2025)**
    *   **研究问题**：如何在不依赖大量专家标注的情况下，构建一个可广泛应用于多种癌症诊断和生存预测任务的通用模型 [m.medsci.cn](https://m.medsci.cn/article/show_article.do?id=81d08609091b)。
    *   **核心方法**：研究者提出了基于自监督学习的基础模型BEPH (BEiT-based model Pre-training on Histopathological image)。该模型在1100万张未标记的组织病理学图像上进行预训练，学习普适性的病理表征。
    *   **关键实验结论**：BEPH在补丁级癌症诊断、WSI级癌症分型和多癌种生存预测等多样化任务中均表现出色。例如，在WSI水平的肾细胞癌亚型分类任务中，AUC达到0.994，证明了其强大的多任务适应性。

##### **2. 多模态融合模型 (Multimodal Models)**

多模态模型通过整合来自不同来源的数据，如病理图像、放射影像（CT/MRI）、基因组学数据和临床信息，以提供比单一模态更全面、更精准的诊断和预后评估。

*   **TITAN (Nature Medicine, 2025)**
    *   **研究问题**：如何将病理图像中的视觉形态特征与病理报告中的文本描述进行有效对齐，使模型能同时“看懂”图像和“理解”语言 [hub.baai.ac.cn](https://hub.baai.ac.cn/view/50285)。
    *   **核心方法**：研究人员提出了多模态病理基础模型TITAN，该模型在超过2100万张WSI及其配对的病理报告上进行预训练。它采用跨模态对比学习，将基于ViT的图像编码器和基于Bio-LLaMA的文本编码器在统一的语义空间中进行对齐。
    *   **关键实验结论**：TITAN在肿瘤分类、分级任务中显著优于纯视觉模型，并能从常规H&E切片中精准预测分子标志物状态（如乳腺癌HER2状态预测AUC达0.94）。其特征空间展现了高度的可解释性，实现了病理形态与诊断语义的统一。

*   **OncoFusion (Nature Cancer, 2025)**
    *   **研究问题**：针对高级别浆液性卵巢癌（HGSOC）等复杂疾病，单一数据模态（如基因组或影像）难以充分解释患者预后的高度异质性 [blog.csdn.net](https://blog.csdn.net/qq_45404805/article/details/148130586)。
    *   **核心方法**：该研究开发了一个多模态机器学习模型，采用晚期融合（late-fusion）策略，整合了治疗前的CT放射组学特征、H&E病理组学特征（如细胞核形态）、基因组数据（如同源重组缺陷状态）以及临床变量。
    *   **关键实验结论**：整合了基因组、放射组学和组织病理学的多模态模型（GRH），其在测试集上的生存预测性能（c-index=0.61）显著高于任何单一模态模型（如单独使用HRD状态的c-index为0.52），证明了多模态信息融合的互补优势。

*   **多模态深度学习用于胰腺癌预后评估 (European Radiology, 2025)**
    *   **研究问题**：胰腺导管腺癌（PDAC）的传统TNM分期预后价值有限，需要更精准的风险分层工具 [www.medsci.cn](https://www.medsci.cn/article/show_article.do?id=fc9c881648fc)。
    *   **核心方法**：研究构建了一个端到端的多模态深度学习模型，整合了增强CT影像和临床变量，用于预测PDAC患者的短期与长期生存风险。
    *   **关键实验结论**：在内部验证中，该多模态模型预测高风险短期生存的AUC为0.637，优于仅使用单一模态的模型。 该研究证明，即使是临床数据与影像数据的简单融合，也能提升预后预测的准确性。

##### **3. 弱监督学习与可解释性增强**

在缺乏像素级精准标注的情况下，弱监督学习（WSL）利用切片级标签进行训练，是计算病理学的主流方法之一。提高其定位精度和可解释性是当前的研究重点。

*   **SMMILe (Nature Cancer, 2025)**
    *   **研究问题**：传统的基于多示例学习（MIL）的弱监督方法虽然在WSI分类任务上表现优异，但通常以牺牲病灶空间定位的精确性为代价 [m.cphi.cn](https://m.cphi.cn/news/show-361138.html)。
    *   **核心方法**：研究团队开发了SMMILe（可度量多示例学习），从数学上证明采用实例级聚合（instance-level aggregation）能够在不损失分类性能的前提下，实现更优的空间量化能力。
    *   **关键实验结论**：在6种癌症类型的8个数据集上进行评估，SMMILe在WSI分类性能上达到或超过了现有主流方法，同时在无需位置标注的情况下，显著提升了对肿瘤区域空间定位和量化的准确性，增强了模型的可解释性。

#### **实验与评价总结**

综合上述代表性工作，可以总结出以下共性结论：

1.  **评估指标标准化**：分类任务普遍采用受试者工作特征曲线下面积（AUC）、准确率（Accuracy）和F1分数进行评估 [www.china-oncology.com](https://www.china-oncology.com/CN/10.19401/j.cnki.1007-3639.2025.08.001)。生存预测任务则以一致性指数（C-index）为核心指标，并结合Kaplan-Meier生存曲线和对数秩检验（log-rank test）进行风险分层验证。
2.  **验证策略的严谨性**：为了证明模型的泛化能力，研究普遍采用严格的验证流程。模型通常在大型公共数据集（如TCGA）和/或内部私有数据上训练，并在完全独立的外部验证集（来自不同医疗中心或国家）上进行测试，以评估其在真实世界数据中的稳健性。
3.  **性能基准对比**：新提出的模型性能通常与多种基准进行对比，包括：（1）最新的同类AI模型（如CTransPath, CLAM）；（2）传统的机器学习方法；（3）单一模态或简化模型；（4）人类病理学家的诊断表现，以证明其临床应用的附加价值。
4.  **可解释性是关键**：几乎所有研究都强调模型可解释性的重要性。通过注意力热图（attention heatmaps）等可视化技术，将模型的预测结果追溯到WSI中的具体组织学形态（如肿瘤细胞密集区、间质或坏死区），确保模型的决策逻辑与病理学知识一致，增强临床医生的信任度。

#### **趋势与挑战**

基于2022-2025年的研究进展，预计2025年前后，计算病理学领域将呈现以下主要研究趋势和挑战：

1.  **病理学大语言模型（LLM）与视觉-语言模型的深度融合**：继TITAN等初步探索之后，未来的研究将构建更强大的病理学视觉-语言模型。这些模型将能够直接生成详细、结构化的病理报告，进行交互式诊断问答，甚至根据文本指令在WSI上定位和分析特定病理特征，实现病理诊断的高度自动化和智能化。
2.  **空间多组学与病理图像的端到端整合**：随着空间转录组学等技术的发展，未来的模型将不再满足于WSI与非空间基因组数据的简单关联。研究重点将转向开发能够端到端融合空间分辨多组学数据与高分辨率病理图像的模型，在单细胞精度上建立形态-分子-功能之间的直接映射关系，从而发现全新的疾病生物标志物和治疗靶点。
3.  **联邦学习与隐私计算在多中心模型训练中的应用**：构建强大的基础模型依赖于海量的多中心数据，但数据隐私和安全是巨大障碍。联邦学习（Federated Learning）等隐私保护技术将成为关键解决方案，允许在不共享原始数据的情况下，协同训练全球规模的病理学模型，从而在保护患者隐私的同时，克服数据孤岛问题，提升模型的泛化能力。

#### **结论**

2022至2025年间，用于癌症诊断与预后的病理学深度学习研究经历了从专用模型向通用基础模型、从单一图像分析向多模态信息融合的深刻范式转变。以Virchow、CHIEF为代表的基础模型展现了前所未有的泛化能力和多任务适应性，而以TITAN和OncoFusion为代表的多模态模型则通过整合基因、影像和临床数据，显著提升了预后预测的精准度。同时，SMMILe等工作持续优化弱监督学习框架，增强了模型的可解释性和临床应用潜力。未来的研究将聚焦于视觉-语言模型的深度融合、空间多组学与病理图像的端到端整合，以及利用联邦学习构建全球协作模型，这些将共同推动计算病理学向更精准、更智能、更安全的临床决策支持工具迈进。

#### **参考文献**

[1] Vorontsov E, Bozkurt A, Casson A, et al. A foundation model for clinical-grade computational pathology and rare cancers detection. *Nat Med*. 2024. [www.medsci.cn](https://www.medsci.cn/article/show_article.do?id=254a8359e6b7)
[2] Lu, M.Y., Chen, T.Y., Williamson, D.F.K. et al. A generalizable pathologic diagnosis and assessment foundation model. *Nature*. 2024. [blog.csdn.net](https://blog.csdn.net/m0_59164304/article/details/143807364)
[3] Yang, Z., Wei, T., Liang, Y. et al. A foundation model for generalizable cancer diagnosis and survival prediction from histopathological images. *Nat Commun*. 2025. [m.medsci.cn](https://m.medsci.cn/article/show_article.do?id=81d08609091b)
[4] Ding, T., Wagner, S.J., Song, A.H. et al. A multimodal whole-slide foundation model for pathology. *Nat Med*. 2025. [hub.baai.ac.cn](https://hub.baai.ac.cn/view/50285)
[5] West, J., Grout, J., Allaway, R. et al. Integrating genomics, radiomics, and histology to improve risk stratification for patients with ovarian cancer. *Nature Cancer*. 2025. [blog.csdn.net](https://blog.csdn.net/qq_45404805/article/details/148130586)
[6] Gao, Z., Chen, C., Yao, H., Li, C., & Gong, T. SMMILe enables accurate spatial quantification in digital pathology using multiple-instance learning. *Nature Cancer*. 2025. [m.cphi.cn](https://m.cphi.cn/news/show-361138.html)
[7] Schuurmans M, Saha A, Alves N, et al. End-to-end prognostication in pancreatic cancer by multimodal deep learning: a retrospective, multicenter study. *Eur Radiol*. 2025. [www.medsci.cn](https://www.medsci.cn/article/show_article.do?id=fc9c881648fc)
[8] 潘炜枫, 肖文波. 影像组学在胰腺导管腺癌诊疗中的研究进展. *临床医学进展*. 2025. [pdf.hanspub.org](https://pdf.hanspub.org/acm_8104715.pdf)
[9] 曾延玮, 徐智坚, 曹鑫, 等. 基于MRI的影像组学和深度学习模型构建：无创鉴别原发颅内弥漫大B细胞淋巴瘤分子亚型. *中国癌症杂志*. 2025. [www.china-oncology.com](https://www.china-oncology.com/CN/10.19401/j.cnki.1007-3639.2025.08.001)
[10] 梁静慧, 王铭, 陈婉婷, 等. 影像组学联合生物标志物预测肝癌微血管侵犯的研究进展. *协和医学杂志*. 2025. [xhyxzz.pumch.cn](https://xhyxzz.pumch.cn/article/doi/10.12290/xhyxzz.2025-0312?viewType=HTML)