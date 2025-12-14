好的，这是一篇关于2022-2025年「AI驱动的分子设计与优化」的中文学术综述。

## AI驱动的分子设计与优化：2022-2025年进展综述

### 引言

分子设计与优化是材料科学、药物发现和催化剂开发等领域的核心任务，传统方法依赖于高成本的试错实验和经验积累，效率低下。近年来，以大语言模型 (LLMs) 和机器学习 (ML) 为代表的人工智能技术在处理复杂数据、发现潜在规律方面展现出强大潜力，正逐步重塑分子设计范式。本文旨在对2022年至2025年期间AI驱动的分子设计与优化领域的代表性工作进行系统性综述，重点关注知识挖掘、生成模型、预测优化以及实验自动化等关键创新，并展望未来的研究趋势。

### 方法分类与代表作

AI驱动的分子设计与优化主要围绕知识挖掘、分子生成、性能预测与优化以及自动化实验控制等模块展开。

#### 1. 知识挖掘与数据整合

大语言模型凭借其强大的自然语言处理能力，在从海量非结构化文献中提取和整合化学知识方面展现出巨大优势，为材料设计提供了新的起点。

*   **黄钰丹等 (2025)** [wulixb.iphy.ac.cn](https://wulixb.iphy.ac.cn/cn/article/doi/10.7498/aps.74.20250497)：该研究综述了大语言模型在材料科学全链条中的应用。核心方法包括使用检索增强生成 (RAG)、多模态信息检索和知识图谱构建等技术进行知识发现与挖掘。研究结论指出，LLMs 在知识挖掘中可将信息检索准确性提高达29.4%，特别是在材料合成条件预测方面。
*   **郑子立等 (2025)** [hub.baai.ac.cn](https://hub.baai.ac.cn/view/43169)：该综述探讨了LLMs如何革新网状化学。研究指出LLMs可从文献中提取知识、设计材料、收集与解析实验数据。通过提示工程、知识与工具增强及微调优化，LLMs能将传统经验驱动流程转化为基于合成-结构-性质-性能关系的发现循环。
*   **吴思远, 李泓 (2025)** [wulixb.iphy.ac.cn](https://wulixb.iphy.ac.cn/cn/article/doi/10.7498/aps.74.20250572)：作者评估了大语言模型在电池科研全流程中的应用，并构建了无机固态电解质综合数据库。该工作展示了LLMs在聚合电池领域数据整合和知识发现的潜力，为电池材料设计提供了数据基础。

#### 2. 分子生成模型

分子生成是AI驱动分子设计的核心环节，旨在生成具有特定性质的新颖分子结构。

*   **唐谦等 (2024)** [jcpu.cpu.edu.cn](https://jcpu.cpu.edu.cn/article/doi/10.11665/j.issn.1000-5048.2024031501)：该综述分析了小分子生成模型在药物发现中的应用，涵盖生成对抗网络 (GANs)、变分自编码器 (VAEs) 和扩散模型。研究强调了这些模型在优化药物属性和生成复杂分子结构方面的能力。
*   **Chen Linjie等 (2023)** [pps.cpu.edu.cn](https://pps.cpu.edu.cn/cn/article/pdf/preview/10.20053/j.issn1001-5094.2023.12.008.pdf)：该工作详细介绍了深度学习在分子生成中的应用进展。综述了循环神经网络 (RNN)、自编码器 (VAE)、生成对抗网络 (GAN) 和Transformer模型在分子生成中的原理、应用及分子表征形式。其中，Transformer模型因其并行计算能力和强大的特征抽取能力，特别适用于大数据集分子生成任务。
*   **Zhavoronkov等 (2019, 引用自2023综述)** [pps.cpu.edu.cn](https://pps.cpu.edu.cn/cn/article/pdf/preview/10.20053/j.issn1001-5094.2023.12.008.pdf)：该团队提出了GENTRL模型，结合自编码器、强化学习和变分推理，用于从头小分子设计。该模型成功在21天内发现了DDR1激酶的有效抑制剂，并在46天内完成了设计、合成和实验测试，显著加速了药物发现进程。

#### 3. 性能预测与优化

AI模型能够从复杂的多维度数据中学习，实现材料性能的快速预测，并指导优化目标。

*   **张泽熙等 (2025)** [sciengine.com](https://www.sciengine.com/parse/pdf/0023-074X/55CB550E61874E5FB634D7B0D23D1D8D.pdf)：该研究综述了机器学习辅助高分子合成的进展，涵盖聚合物性能正向预测及逆向设计。文中提到Transformer模型（如TransPolymer和polyBERT）能学习聚合物的SMILES编码，实现对电导率、介电常数、结晶度等多项性能的准确预测。
*   **Luttens等 (2025)** [hub.baai.ac.cn](https://hub.baai.ac.cn/view/44150)：该研究提出了一种结合机器学习和分子对接的策略，用于快速遍历广阔化学空间。通过对100万种化合物进行分子对接并训练分类算法，CatBoost分类器在速度和准确性之间取得了最佳平衡，将35亿种化合物的筛选计算成本降低了1000倍以上，成功发现了G蛋白偶联受体配体。
*   **胡建钰等 (2025)** [sciengine.com](https://dds.sciengine.com/cfs/files/pdfs/view/1674-7224/5FED236178C14C67A2A9EEC17ACCF136-mark.pdf)：该研究聚焦于可解释人工智能（XAI）在催化科学理论构建中的应用。通过SISSO等可解释机器学习算法，从海量数据中筛选出关键特征，成功建立了纳米催化剂抗烧结的稳定性理论和金属-载体相互作用的控制方程，实现从"现象归纳"到"机理驱动"的跨越。

#### 4. 自动化实验平台与机器人集成

AI与自动化实验平台的结合，实现了实验流程的智能化控制，显著提升了高通量实验的迭代效率。

*   **黄钰丹等 (2025)** [wulixb.iphy.ac.cn](https://wulixb.iphy.ac.cn/cn/article/doi/10.7498/aps.74.20250497)：该文强调了LLMs与自动化实验平台的深度融合，通过自然语言控制实验流程。例如，CLAIRify框架利用LLMs生成未经验证的结构化语言，并通过验证器将其转化为机器人轨迹，显著提升了高通量实验的迭代效率。

### 实验与评价总结

这些研究普遍利用了跨模态数据处理、智能推理和自动化执行来加速分子设计。在知识挖掘方面，AI模型通过RAG、多模态信息检索和知识图谱构建，有效解决了传统材料研究中数据碎片化和信息提取效率低的问题。在分子生成方面，RNN、VAE、GAN和Transformer等模型能够生成具有特定性质的新颖分子，其中结合强化学习和迁移学习的方法能进一步优化生成分子的生物活性和合成可行性。性能预测方面，机器学习模型通过学习结构-性质关系，实现了对电导率、介电常数、结晶度等材料属性的快速预测，在药物发现中大幅缩短了筛选时间并提高了命中率。AI与自动化实验平台的集成，使得实验流程可以通过自然语言控制，将传统实验室转变为“自驱动”模式，从而显著提升了高通量实验的迭代效率和优化周期。尽管AI在这些方面取得了显著进展，但对高质量数据的依赖、LLMs的“黑箱”特性以及处理复杂材料体系的局限性仍然是其主要挑战。

### 趋势与挑战

AI驱动的分子设计与优化研究正朝着以下几个方向发展：

1.  **多模态融合与跨尺度统一**：未来的研究将更加注重整合文本、图像、结构数据等多种模态信息，并实现原子、分子到宏观材料性能的跨尺度知识融合。这将有助于构建更全面、更精确的分子-性质关系模型，并支持更复杂的材料体系设计 [wulixb.iphy.ac.cn](https://wulixb.iphy.ac.cn/cn/article/doi/10.7498/aps.74.20250497)。
2.  **可解释性AI与物理理论结合**：为了克服AI模型的“黑箱”问题，可解释机器学习（XAI）方法将得到更广泛的应用。同时，AI模型将更紧密地与物理定律和化学原理相结合，从而增强预测的物理清晰度和可靠性，并推动催化科学等领域的理论创新 [sciengine.com](https://dds.sciengine.com/cfs/files/pdfs/view/1674-7224/5FED236178C14C67A2A9EEC17ACCF136-mark.pdf)。
3.  **自主实验与机器人实验室加速闭环研发**：LLMs与自动化实验平台的深度融合将推动自主实验系统的发展，实现从假设生成、实验设计、数据采集、结果分析到模型优化的全链条闭环。这将显著缩短材料研发周期，实现“人工智能驱动的科学家”愿景 [hub.baai.ac.cn](https://hub.baai.ac.cn/view/43169)。
4.  **数据质量与标准化挑战**：高质量、标准化数据仍然是AI模型训练的关键。如何有效整合分散的异构数据，解决数据稀缺性和噪声问题，以及建立针对科学任务的AI评测体系，将是未来需要持续攻克的挑战。

### 结论

2022-2025年期间，AI驱动的分子设计与优化展现出蓬勃的生命力。 LLMs在知识挖掘、分子生成和实验控制方面的应用，结合机器学习在性能预测和优化上的优势，正加速材料科学、药物发现和催化剂开发领域的范式转变。尽管仍面临数据质量、模型可解释性等挑战，但多模态融合、物理约束结合和自主实验等前沿趋势预示着AI将在分子科学领域开辟更广阔的创新空间。

### 参考文献

1.  黄钰丹, 夏琬钧, 杜俊梅, 蒋渝, 汪鑫, 陈元正, 王红艳, 赵纪军, 郭春生. 大语言模型加速材料设计——从知识挖掘到智能设计的全链条赋能. *物理学报*, 2025, 74(18): 188101. [wulixb.iphy.ac.cn](https://wulixb.iphy.ac.cn/cn/article/doi/10.7498/aps.74.20250497)
2.  郑子立, Rampal N, Inizan T J, Borgs C, Chayes J T, Yaghi O M. 大型语言模型驱动的网状化学创新. *Nat. Rev. Mater.*, 2025, DOI: 10.1038/s41578-025-00772-8. [hub.baai.ac.cn](https://hub.baai.ac.cn/view/43169), [cloud.tencent.cn](https://cloud.tencent.cn/developer/article/2494103)
3.  吴思远, 李泓. 大语言模型在电池科研全流程应用的测评与无机固态电解质综合数据库构建. *物理学报*, 2025, 74(16): 160701. [wulixb.iphy.ac.cn](https://wulixb.iphy.ac.cn/cn/article/doi/10.7498/aps.74.20250572)
4.  唐谦, 陈柔棻, 沈哲远, 池幸龙, 车金鑫, 董晓武. 基于人工智能的小分子生成模型在药物发现中的研究进展. *中国药科大学学报*, 2024, DOI: 10.11665/j.issn.1000-5048.2024031501. [jcpu.cpu.edu.cn](https://jcpu.cpu.edu.cn/article/doi/10.11665/j.issn.1000-5048.2024031501)
5.  Chen L, Zhou R, Lyu H, Xu J, He Z, Chen Y. 深度学习在分子生成中的应用进展. *药学进展*, 2023, 47(12): 950-960. [pps.cpu.edu.cn](https://pps.cpu.edu.cn/cn/article/pdf/preview/10.20053/j.issn1001-5094.2023.12.008.pdf)
6.  Zhavoronkov A, Ivanenkov Y A, Aliper A, et al. Deep learning enables rapid identification of potent DDR1 kinase inhibitors. *Nature Biotechnol.*, 2019, 37(9): 1038–1040. (引用自 ref. 5)
7.  张泽熙, 蔡展翔, 张文彬, 吕华, 陈茂. 机器学习辅助高分子合成研究进展. *科学通报*, 2025, 70: 471–480. [sciengine.com](https://www.sciengine.com/parse/pdf/0023-074X/55CB550E61874E5FB634D7B0D23D1D8D.pdf)
8.  Luttens A, Cabeza de Vaca I, Sparring L, et al. 利用机器学习引导的对接筛选，实现快速遍历广阔化学空间. *Nat Comput Sci*, 2025, DOI: 10.1038/s43588-025-00777-x. [hub.baai.ac.cn](https://hub.baai.ac.cn/view/44150)
9.  胡建钰, 杨峻毅, 胡素磊, 刘进勋, 李微雪. 可解释机器学习辅助建立催化科学理论. *中国科学: 化学*, 2025, 55: 1704–1714. [sciengine.com](https://dds.sciengine.com/cfs/files/pdfs/view/1674-7224/5FED236178C14C67A2A9EEC17ACCF136-mark.pdf)
10. Lewis P, Perez E, Piktus A, et al. Retrieval-augmented generation for knowledge-intensive NLP tasks. *34th Conf. Neural Inf. Process. Syst.*, 2020: 16792-16802. (引用自 ref. 1)
11. Yoshikawa N, Skreta M, Darvish K, et al. CLAIRify: From natural language to robot trajectories using large language models. *Auton. Robot.*, 2023, 47: 1057–1076. (引用自 ref. 1)
12. Luo Z M, Yang Z L, Xu Z X, Yang W, Du X Y. Navigating the AI horizon: a comprehensive review of large language models in material science. arXiv: 2501.04306v1 [cs.CL], 2025. (引用自 ref. 1)