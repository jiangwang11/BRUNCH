## 计算药物对接技术的增强方法学：2022-2025年代表性工作综述

### 引言

计算药物对接（Drug Docking）是结构引导药物设计（SBDD）的核心环节，旨在预测小分子配体与靶蛋白的结合模式和亲和力，从而加速药物发现进程。然而，传统的对接方法往往面临计算效率低、打分函数精度不足以及难以有效处理蛋白构象柔性等挑战。近年来，随着大分子结构数据积累和深度学习技术的飞速发展，计算药物对接领域涌现出大量创新性方法，极大地提升了预测的准确性和效率。本综述将聚焦2022-2025年的代表性工作，系统梳理当前计算药物对接技术的最新进展，并对未来的发展趋势进行展望。

### 方法分类与代表作

当前计算药物对接技术的增强方法学主要集中于以下几个方面：机器学习引导的虚拟筛选、扩散模型在复合物结构预测中的应用、以及结合位点亲和力预测的神经网络模型。

#### 1. 机器学习引导的超大规模虚拟筛选

面对按需合成化学库规模的爆炸式增长（已达数十亿甚至万亿级别），传统的对接方法已无法胜任。机器学习在此背景下展现出强大的加速潜力。

*   **Luttens等，2025** [hub.baai.ac.cn](https://hub.baai.ac.cn/view/44150)：该研究旨在解决超大规模化学库（数十亿至万亿级）的虚拟筛选计算成本问题。研究人员提出了一种结合机器学习（ML）与分子对接的策略，通过在高评分化合物上训练分类算法，并利用保序预测（CP）框架从数十亿化合物库中筛选候选化合物，显著减少了显式对接的分子数量。实验证明，该方法可将计算成本降低超过1000倍，并成功发现了G蛋白偶联受体（GPCRs）配体和具有多靶点活性的化合物。
*   **Wang等，2025** [hub.baai.ac.cn](https://hub.baai.ac.cn/view/50095)：这篇综述总结了深度学习如何与物理原理相结合推动药物发现，其中特别提到了利用深度学习进行分子对接、打分与虚拟筛选。研究指出，基于深度学习的对接方法通过从晶体结构数据中学习相互作用信息，直接建模小分子的结合构象。在超大库虚拟筛选方面，通过主动学习（如Deep Docking、OpenVS）或高效打分（如DrugCLIP）引导虚拟筛选，成功在不同靶标上获得了苗头化合物。

#### 2. 基于生成式AI的蛋白-配体复合物结构预测

生成式AI，尤其是扩散模型，在生成高精度蛋白-配体复合物构象方面取得了突破性进展，有效克服了传统对接方法难以捕捉构象柔性和生成合理构象的难题。

*   **Zheng等，2024** [stcsm.sh.gov.cn](https://stcsm.sh.gov.cn/xwzx/kjzl/20241203/adba32cac41d4de1b0e667889c80098f.html), [simm.cas.cn](https://simm.cas.cn/web/xwzx/ttxw/202412/t20241202_7449173.html), [ecas.cas.cn](https://ecas.cas.cn/xxkw/kbcd/201115_146563/ml/xxhcxyyyal/202412/t20241219_5042982.html)：中国科学院上海药物研究所郑明月团队开发了基于生成式AI的蛋白-配体复合物结构预测方法SurfDock。该方法利用蛋白质表面信息构建几何扩散神经网络，实现了高精度自动生成配体结合构象。SurfDock整合了表面特征、残基结构特征和预训练序列特征到表面节点表示中，并通过SurfScore内部评分模块评估构象置信度，并结合力场优化步骤，在多个基准测试中展现出超越现有深度学习方法的对接能力和构象合理性，尤其在处理高度柔性配体方面表现出色。
*   **Yu等，2025** [hub.baai.ac.cn](https://hub.baai.ac.cn/view/44052)：该研究提出了一种知识引导的扩散框架DiffPhore，用于即时（on-the-fly）3D配体-药效团映射。DiffPhore利用配体-药效团匹配知识指导配体构象生成，并通过校准采样缓解曝光偏差，在结合构象预测方面超越了传统药效团工具和多种先进对接方法。实验证明，DiffPhore在PDBBind测试集上达到了当前最优的结合构象预测成功率，并在先导化合物发现和靶点筛选中展现出卓越的虚拟筛选能力，成功鉴定出结构迥异的人谷氨酰环化酶抑制剂。

#### 3. 双通道/双模态神经网络模型

集成多维度信息并利用任务间的对偶性，成为提升药物对接与设计性能的有效途径。

*   **Hu等，2025** [cloud.tencent.com](https://cloud.tencent.com/developer/article/2503572), [hub.baai.ac.cn](https://hub.baai.ac.cn/view/44038)：清华大学、微软研究院等机构提出了3DMolFormer，一个统一的双通道Transformer框架，旨在解决蛋白质-小分子配体对接和针对靶点口袋的3D药物设计这两个基于结构药物发现的核心挑战。该模型通过设计一种平行序列格式表示3D复合物（离散token序列和连续3D坐标序列），并采用“预训练+微调”范式解决数据稀缺问题。3DMolFormer在对接和3D药物设计任务中均优于此前基线方法，尤其通过在药物设计过程中利用对接功能，有效利用了两项任务之间的对偶性。
*   **He等，2025** [hub.baai.ac.cn](https://hub.baai.ac.cn/view/43313)：该研究聚焦于药物靶点亲和力预测，提出了名为DMFF-DTA的双模态图神经网络模型。DMFF-DTA创新性地整合了序列模态特征和图模态特征提取模块，并通过基于AlphaFold2的结合位点聚焦图构建方法，有效处理了药物分子与蛋白质之间的尺度差异。模型在Davis和KIBA数据集上实现了均方误差和一致性指数的显著提升，并在胰腺癌药物重定位案例中成功预测了潜在药物，展示了高精度预测、可解释性和计算效率的平衡。

### 实验与评价总结

上述方法在广泛认可的基准数据集（如PDBBind、DUD-E、CASP等）上进行了严格评估，并普遍采用了RMSD、AUROC、BEDROC、TM-score以及结合亲和力（如Ki值、EC50）等量化指标。总体而言，这些新兴的计算药物对接技术展示了：

1.  **显著的效率提升**：通过机器学习引导的筛选策略，能够将超大规模化学库的筛选成本降低数千倍，实现对数十亿级化合物的快速遍历。
2.  **更高的构象预测准确性**：生成式AI模型在生成物理合理且接近实验数据的配体结合构象方面表现出色，尤其在处理蛋白质和配体的构象柔性上优于传统方法。预测构象与实验晶体结构高度一致。
3.  **更强的泛化能力和鲁棒性**：通过大规模预训练、知识引导或多模态信息整合，模型在面对未见过的蛋白质、新的结合口袋或高度柔性配体时，仍能保持稳定的预测性能。
4.  **增强的可解释性**：部分模型通过注意力机制或特征融合策略，能够识别药物分子中的关键功能团以及与蛋白质相互作用的具体位点，为理解分子结合机制提供了有价值的洞见。
5.  **在药物发现中的实用价值**：多项研究通过识别具有新骨架的先导分子，或成功发现多靶点活性配体，证明了这些方法在早期药物发现和药物重定位中的直接应用潜力。

### 趋势与挑战

2025年前后，计算药物对接领域的研究将呈现以下趋势：

1.  **多模态数据深度融合**：未来的方法将不仅仅局限于蛋白和配体的结构信息，而是会更深入地融合基因组学、转录组学、表型数据以及疾病通路信息，构建更全面的药物-靶点-疾病图谱，实现更精准的药物预测和设计。
2.  **物理先验与深度学习的协同优化**：尽管深度学习表现出强大能力，但其“黑箱”特性和对训练数据的依赖限制了其在物理合理性方面的保障。未来的研究将更加强调将经典的物理力场、量子化学计算和分子动力学模拟等物理先验知识，以更精妙的方式融入到深度学习模型中，例如通过损失函数、模型架构设计或后处理优化，从而提升预测的准确性、物理合理性和可解释性。
3.  **从单一结合预测迈向多目标优化**：药物研发不仅需要高效结合，还需要优良的药代动力学性质（ADME）、低毒性、高选择性等。未来的药物对接和设计模型将向多目标优化方向发展，能够同时预测和优化化合物的多个生物学和理化性质，甚至考虑多靶点活性、脱靶效应等复杂情况，实现更全面的药物筛选和优化。
4.  **动态结构与构象系综建模**：蛋白质和配体在结合过程中存在显著的构象变化。通过AlphaFold2等模型衍生的多构象采样技术（如FoldCopilot [www.sciengine.com](https://www.sciengine.com/doi/pdfView/35470D60F87E4B829C39928F1B3CD680)），未来的对接方法将从静态结构预测转向动态结合过程的模拟，能够更好地捕捉结合诱导契合、变构调节等复杂机制，从而更准确地预测实际生理环境下的结合模式。

挑战依然存在，包括高质量3D蛋白-配体复合物数据稀缺、模型泛化能力有限（尤其对于新型靶点或化学骨架）、以及如何有效评估模型在真实世界药物发现中的长期有效性等。

### 结论

2022-2025年，计算药物对接技术在机器学习和生成式AI的驱动下取得了里程碑式进展。机器学习引导的虚拟筛选显著提升了筛选效率，生成式AI方法革新了复合物构象预测的精度和合理性，而双通道/双模态神经网络模型则通过整合多维信息和利用任务对偶性，为药物亲和力预测带来了突破。这些新兴方法正逐步克服传统计算药物对接的局限性，为高效、精准地发现新型药物提供了强大工具，并有望深刻改变未来的药物研发格局。

### 参考文献

*   [hub.baai.ac.cn](https://hub.baai.ac.cn/view/44150) Luttens, A., Cabeza de Vaca, I., Sparring, L. et al. Rapid traversal of vast chemical space using machine learning-guided docking screens. Nat Comput Sci (2025).
*   [cloud.tencent.com](https://cloud.tencent.com/developer/article/2503572) Hu, X., Liu, G., Chen, C., Zhao, Y., Zhang, H., and Liu, X. 3DMolFormer: A Dual-channel Framework for Structure-based Drug Discovery. arXiv preprint arXiv:2502.05107 (2025).
*   [hub.baai.ac.cn](https://hub.baai.ac.cn/view/44052) Yu, JL., Zhou, C., Ning, XL. et al. Knowledge-guided diffusion model for 3D ligand-pharmacophore mapping. Nat Commun 16, 2269 (2025).
*   [hub.baai.ac.cn](https://hub.baai.ac.cn/view/44038) Hu, X., Liu, G., Chen, C., Zhao, Y., Zhang, H., and Liu, X. 3DMolFormer: A Dual-channel Framework for Structure-based Drug Discovery. ICLR 2025.
*   [hub.baai.ac.cn](https://hub.baai.ac.cn/view/43313) He, H., Chen, G., Tang, Z. et al. Dual modality feature fused neural network integrating binding site information for drug target affinity prediction. npj Digit. Med. 8, 67 (2025).
*   [hub.baai.ac.cn](https://hub.baai.ac.cn/view/50095) Wang, Y., Li, Y., Chen, J., and Lai, L. Modeling protein–ligand interactions for drug discovery in the era of deep learning. Chemical Society Reviews 2025, doi: 10.1039/D5CS00415B.
*   [ecas.cas.cn](https://ecas.cas.cn/xxkw/kbcd/201115_146563/ml/xxhcxyyyal/202412/t20241219_5042982.html) 中国科学院上海药物研究所郑明月团队. 中国科学院开发出基于生成式AI的蛋白-配体复合物结构预测方法SurfDock. 2024年12月19日.
*   [stcsm.sh.gov.cn](https://stcsm.sh.gov.cn/xwzx/kjzl/20241203/adba32cac41d4de1b0e667889c80098f.html) 上海市科学技术委员会. 科学家开发出基于生成式AI的蛋白-配体复合物结构预测方法. 2024年12月03日.
*   [simm.cas.cn](https://simm.cas.cn/web/xwzx/ttxw/202412/t20241202_7449173.html) 中国科学院上海药物研究所. Nat Methods | SurfDock利用表面信息扩散生成模型实现蛋白质-配体复合物结构的精准预测. 2024年12月02日.
*   [www.sciengine.com](https://www.sciengine.com/doi/pdfView/35470D60F87E4B829C39928F1B3CD680) 陈振宇, 林潇涵, 李彦衡, 马子程, 张骏, 高毅勤. 基于物理启发式的深度学习方法对蛋白质三维结构的修复与扩展采样. 科学通报 (2025).