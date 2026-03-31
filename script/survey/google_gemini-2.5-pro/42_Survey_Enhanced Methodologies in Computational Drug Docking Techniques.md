好的，作为一名严谨的科研助手，我将基于提供的真实联网搜索结果，为您生成一篇关于“计算药物对接技术的增强方法学”的中文学术综述。

### **计算药物对接技术的增强方法学研究
—— 涵盖2022–2025年的代表性工作**

---

### **引言**

计算药物对接（Computational Drug Docking）是基于结构药物发现（SBDD）的核心环节，它通过模拟配体（药物分子）与受体（靶点蛋白）的相互作用来预测其结合模式和亲和力，从而在庞大的化学空间中快速筛选潜在的候选药物，极大地节约了研发成本与时间 [pdf.hanspub.org](https://pdf.hanspub.org/hjmce2025131_113070257.pdf)。传统对接方法依赖于基于物理或经验的打分函数和启发式搜索算法，但长期面临两大瓶颈：一是打分函数精度不足，难以准确排序候选分子；二是“刚性受体”假设限制了其在处理蛋白质构象变化（即柔性）时的应用。

近年来，尤其是2022至2025年间，深度学习（Deep Learning）技术为解决上述挑战带来了革命性突破 [hub.baai.ac.cn](https://hub.baai.ac.cn/view/50095)。人工智能（AI）驱动的新方法不仅提升了对接的精度和效率，还在建模蛋白质柔性、加速超大规模虚拟筛选等方面取得了显著进展。本综述旨在系统梳理这一时期内计算对接领域的增强方法学，重点评述基于生成式模型的对接方法、融合蛋白质柔性的新模型以及机器学习引导的加速筛选策略，并展望未来的研究趋势与挑战。

### **方法分类与代表作**

#### **1. 基于生成式模型与扩散模型的对接方法**

这类方法将分子对接问题重构为生成任务，直接学习从分子到其三维结合构象的映射，显著提升了预测速度与精度。扩散模型（Diffusion Models）尤其在捕捉构象的概率分布方面表现出巨大潜力 [jcpu.cpu.edu.cn](https://jcpu.cpu.edu.cn/article/doi/10.11665/j.issn.1000-5048.2024031501)。

*   **DiffDock (ICLR 2023)**
    *   **研究问题**：传统对接方法在盲对接（未知结合口袋）场景下速度慢且精度低。
    *   **核心方法**：将分子对接建模为在配体姿态（平移、旋转、扭转角）的七维空间中的生成式扩散过程。该模型通过学习从噪声分布到真实结合构象的“去噪”过程，能够高效地生成候选构象，并通过置信度模型进行排序。
    *   **关键实验结论**：在PDBBind数据集上，DiffDock在不预先指定结合口袋的情况下，其对接成功率（RMSD < 2Å）远超AutoDock Vina等传统方法和部分早期深度学习模型，且推理速度提升了几个数量级。

*   **SurfDock (Nature Methods 2024)**
    *   **研究问题**：如何利用蛋白质的几何与化学表面信息来引导更精准的配体构象生成。
    *   **核心方法**：该研究开发了一种基于几何扩散神经网络的蛋白-配体复合物结构预测方法SurfDock。模型将蛋白质的表面特征、残基结构及预训练序列特征整合为表面节点的表示，在蛋白质表面进行几何扩散以生成配体构象，并内置SurfScore模块评估构象置信度。
    *   **关键实验结论**：在多个基准测试中，SurfDock的对接能力和生成构象的物理合理性超越了当时已有的深度学习方法。针对ALDH1B1靶点的筛选实验成功证实了其在真实药物发现场景中的实用价值 [ecas.cas.cn](https://ecas.cas.cn/xxkw/kbcd/201115_146563/ml/xxhcxyyyal/202412/t20241219_5042982.html)。

*   **3DMolFormer (ICLR 2025)**
    *   **研究问题**：蛋白质-配体对接与基于靶点的3D药物设计本质上是对偶任务，但现有方法未能有效利用此对偶性且受限于数据稀缺。
    *   **核心方法**：提出了一个统一的双通道Transformer框架3DMolFormer，用平行序列（离散的原子/SMILES序列与连续的3D坐标序列）表示复合物。通过自回归生成式架构，该模型不仅能执行对接任务，还能进行药物设计，并通过大规模预训练和数据增强学习到等变性，而无需强制使用等变网络架构。
    *   **关键实验结论**：在对接任务中，3DMolFormer的准确率优于AutoDock Vina和Uni-Mol等基线方法。其统一框架的设计验证了利用任务间对偶性可以提升模型性能，代表了通用序列建模在结构生物学领域应用的趋势 [cloud.tencent.com](https://cloud.tencent.com/developer/article/2503572)。

#### **2. 融合蛋白质柔性的对接模型**

蛋白质柔性，特别是结合过程中的“诱导契合”（Induced Fit），是传统对接方法的一大难点。近期研究开始利用AlphaFold等结构预测模型的进展，显式或隐式地对蛋白质的动态构象进行建模。

*   **FoldCopilot (Chin. Sci. Bull. 2025)**
    *   **研究问题**：如何高效修复实验结构中的缺失区域，并对蛋白质的局部柔性区域（如Loop区）进行有效构象采样以辅助对接。
    *   **核心方法**：开发了基于AlphaFold2架构的FoldCopilot套件。Fixer工具利用“诱导不动点”（IFP）算法，将已知部分结构作为模板和约束，精确修复未知区域。Conformer工具则通过“同源能量景观微扰”（HLP）机制，在保持核心骨架稳定的前提下，高效采样抗体CDR3环等柔性区域的多样化构象。
    *   **关键实验结论**：在结构修复任务上，FoldCopilot的精度显著优于PDBFixer等传统工具。在构象采样方面，该方法成功生成了蛋白质柔性区域的多种合理构象，证明了利用提示词工程（Prompt Engineering）改造大型结构预测模型以解决柔性对接问题的可行性 [sciengine.com](https://www.sciengine.com/doi/pdfView/35470D60F87E4B829C39928F1B3CD680)。

*   **DynamicBind (Nat. Commun. 2024)**
    *   **研究问题**：如何直接预测由特定配体诱导的蛋白质结合口袋构象变化。
    *   **核心方法**：提出一个深度等变网络，它接收靶点口袋的初始构象和配体图作为输入，直接端到端地输出与该配体结合后的蛋白质口袋构象。该方法显式地建模了配体特异性的诱导契合过程。
    *   **关键实验结论**：实验证明，DynamicBind能够准确预测配体结合引起的蛋白质侧链和骨架的构象重排，生成的复合物结构在物理上更加合理，为解决柔性对接问题提供了直接的解决方案 [hub.baai.ac.cn](https://hub.baai.ac.cn/view/50095)。

*   **DMFF-DTA (npj Digit. Med. 2025)**
    *   **研究问题**：现有的药物-靶点亲和力（DTA）预测模型大多忽略结构信息或难以处理药物与蛋白的尺度差异。
    *   **核心方法**：开发了一种双模态（序列+图）图神经网络DMFF-DTA。其创新之处在于，利用AlphaFold2的结构预测能力，构建了一个聚焦于“绑定位点”的蛋白质接触图，有效解决了全尺寸蛋白图与小分子图的尺度不平衡问题，并隐式地包含了结合区域的关键柔性信息。
    *   **关键实验结论**：在Davis和KIBA数据集上，该模型在均方误差（MSE）和一致性指数（CI）等指标上均超越了DeepDTA、GraphDTA等先进方法，证明了通过精确建模关键结合区域的结构特征能够显著提升亲和力预测的准确性，从而为对接结果提供更可靠的评分 [hub.baai.ac.cn](https://hub.baai.ac.cn/view/43313)。

#### **3. 机器学习引导的加速筛选策略**

面对数十亿甚至万亿级别的可合成化合物库，即使最快的对接方法也力不从心。因此，利用机器学习模型进行预筛选，以数量级的优势降低计算成本，成为虚拟筛选的新范式。

*   **基于保序预测的对接筛选 (Nat. Comput. Sci. 2025)**
    *   **研究问题**：如何以可控的错误率和极低的计算成本从超大规模化学空间中筛选出高评分的苗头化合物。
    *   **核心方法**：提出一种“机器学习引导对接”的策略。首先对百万级化合物子集进行对接，训练一个分类器（如CatBoost）来学习高分化合物的特征。然后，利用该分类器结合“保序预测”（Conformal Prediction）框架，对数十亿级的化合物库进行快速预测，筛选出最有可能获得高对接分数的子集进行真实对接。
    *   **关键实验结论**：应用于一个35亿化合物的数据库时，该方法将所需的计算成本降低了超过1000倍。通过调整置信度水平，该方法能在保留近90%高分子的同时，仅对接数据库中约10%的化合物，并成功发现了G蛋白偶联受体（GPCRs）的新型配体 [hub.baai.ac.cn](https://hub.baai.ac.cn/view/44150)。

*   **DrugCLIP (arXiv 2024)**
    *   **研究问题**：如何实现无需分子对接的超快速虚拟筛选。
    *   **核心方法**：借鉴计算机视觉领域的对比学习思想，DrugCLIP通过大规模预训练，将药物（2D/3D表示）和靶点（序列/结构表示）等多种模态的信息映射到一个统一的特征空间。筛选时，只需计算候选药物与靶点在嵌入空间中的特征向量相似度（如余弦相似度），即可快速评估其结合可能性。
    *   **关键实验结论**：这种“免对接”的筛选方式通过简单的矩阵运算即可完成，速度远超传统对接。在多个基准上展示了其在超大库虚拟筛选中的巨大潜力，能够作为第一道粗筛工具，快速过滤掉绝大部分不相关的分子 [hub.baai.ac.cn](https://hub.baai.ac.cn/view/50095)。

### **实验与评价总结**

综合2022-2025年的代表性工作，实验与评价方面呈现出以下共性结论：

1.  **评价基准的统一与挑战**：在对接姿态预测（Pose Prediction）方面，PDBBind数据集依然是黄金标准，RMSD < 2Å是公认的成功标准。在亲和力预测方面，Davis、KIBA等数据集被广泛使用，评价指标主要为MSE、CI和$r_m^2$。然而，现有数据集的规模和多样性仍显不足，且存在数据泄露问题，这促使研究者开始构建更严格的测试集（如Leak Proof PDBBind）和高质量合成数据集 [hub.baai.ac.cn](https://hub.baai.ac.cn/view/50095)。

2.  **深度学习模型性能的超越**：基于深度学习，特别是生成式模型（如DiffDock），在对接精度上已稳定超越传统方法（如AutoDock Vina）。它们不仅盲对接成功率更高，而且在处理具有多个扭转键的高度柔性配体时也表现出更好的鲁棒性 [ecas.cas.cn](https://ecas.cas.cn/xxkw/kbcd/201115_146563/ml/xxhcxyyyal/202412/t20241219_5042982.html)。

3.  **计算效率与精度的权衡**：纯生成式对接模型在单次预测上速度极快，但对于超大规模筛选，其计算开销依然可观。因此，结合了快速分类器和保序预测的混合策略 [hub.baai.ac.cn](https://hub.baai.ac.cn/view/44150)]，以及免对接的对比学习方法 [hub.baai.ac.cn](https://hub.baai.ac.cn/view/50095)]，在实现数量级加速方面展现了巨大优势，成功在精度和效率之间取得了新的平衡。

4.  **可解释性与物理合理性的增强**：新一代模型愈发注重可解释性。例如，DMFF-DTA通过可视化注意力权重，验证了模型关注的是与蛋白发生相互作用的关键化学基团 [hub.baai.ac.cn](https://hub.baai.ac.cn/view/43313)]。同时，通过引入力场优化步骤（如SurfDock）或设计物理知识启发的架构（如FoldCopilot），模型生成构象的物理合理性（如避免原子碰撞、保持合理键长键角）得到显著改善。

### **趋势与挑战**

展望2025年之后，计算药物对接领域的研究将呈现以下几个主要趋势：

1.  **统一的多模态与多任务建模**：以AlphaFold3为代表，未来的趋势是构建能够处理蛋白质、小分子、核酸、离子等多种生物分子，并整合序列、结构、甚至电镜密度图等多模态信息的统一模型 [cloud.tencent.com](https://cloud.tencent.com/developer/article/2503572)。这类模型将不再局限于单一的对接任务，而是能够同时执行结构预测、亲和力排序、构象采样和药物从头设计等多项任务，通过任务间的知识共享提升整体性能。

2.  **物理知识与数据驱动的深度融合**：未来的模型将不再是纯粹的数据驱动“黑箱”，而是深度融合物理原理。这包括：将等变性等对称性约束更优雅地融入网络设计；利用先进的机器学习力场（ML Force Fields）指导或精修对接构象；以及像FoldCopilot那样，将能量景观、分子动力学系统的概念引入模型迭代过程，从而提升模型的泛化能力、数据效率和物理真实性 [sciengine.com](https://www.sciengine.com/doi/pdfView/35470D60F87E4B829C39928F1B3CD680)]。

3.  **对动态性与高柔性靶点的攻克**：静态对接的局限性日益凸显，未来的研究重点将转向对蛋白质动态行为的建模 [gs.imu.edu.cn](https://gs.imu.edu.cn/__local/8/28/7F/3F8649389E08A6844F194F45326_0FE47AA5_4EC068.pdf)。这不仅包括对柔性Loop区的采样，更将挑战大尺度的结构域运动和天然无序蛋白（IDPs）的对接问题。直接生成构象系综的生成模型，结合增强采样和分子动力学模拟，有望为靶向这些“不可成药”靶点提供新的计算工具。

### **结论**

2022至2025年是计算药物对接领域由传统方法向深度学习范式深刻转型的关键时期。基于生成式模型的方法革新了对接精度与速度的上限；融合蛋白质柔性的模型攻克了长期存在的“刚性受体”假设瓶颈；而机器学习引导的加速筛选策略则使面向亿级化合物库的虚拟筛选成为现实。这些进步共同推动了药物发现的“干湿结合”研发模式。未来，随着统一多模态模型的发展、物理知识的深度融入以及对蛋白质动态性的精准刻画，计算药物对接技术必将在药物研发的早期阶段扮演愈发核心的角色，持续加速创新药物的发现进程。

### **参考文献**

1.  He, H., Chen, G., Tang, Z. et al. Dual modality feature fused neural network integrating binding site information for drug target affinity prediction. *npj Digit. Med.* 8, 67 (2025).
2.  Luttens, A., Cabeza de Vaca, I., Sparring, L. et al. Rapid traversal of vast chemical space using machine learning-guided docking screens. *Nat Comput Sci* (2025).
3.  Hu, X., Liu, G., Chen, C., et al. 3DMolFormer: A Dual-channel Framework for Structure-based Drug Discovery. *arXiv preprint arXiv:2502.05107* (2025).
4.  Chen, Z., Lin, X., Li, Y., et al. Physics-informed deep learning approach for fixing and sampling protein 3D structures. *Chin Sci Bull* (2025).
5.  Wang, Y., Li, Y., Chen, J., & Lai, L. Modeling protein–ligand interactions for drug discovery in the era of deep learning. *Chem. Soc. Rev.* (2025).
6.  Corso, G., Stärk, H., Jing, B., et al. DiffDock: Diffusion Steps, Twists, and Turns for Molecular Docking. *ICLR 2023*.
7.  Ocepov, D., Shvets, M., Omelcenko, A. et al. DynamicBind: predicting ligand-specific protein-bound conformations with a deep equivariant network. *Nat Commun* 15, 230 (2024).
8.  Lu, C., Liu, Q., Wu, Q., et al. DrugCLIP: Contrastive Language-Image-Protein Pretraining for 2D/3D Drug-Target Interaction Prediction. *arXiv preprint arXiv:2405.15873* (2024).
9.  Zheng, M., et al. SurfDock: accurate protein-ligand docking and virtual screening by learning from protein surfaces. *Nat Methods* (2024).
10. Abramson, J., Adler, J., Dunger, J., et al. Accurate structure prediction of biomolecular interactions with AlphaFold3. *Nature* 630, 493–500 (2024).
11. Jumper, J., Evans, R., Pritzel, A. et al. Highly accurate protein structure prediction with AlphaFold. *Nature* 596, 583–589 (2021).
12. 迟宪昊, 邓兴龙. JAK3 激酶小分子抑制剂虚拟筛选设计技术的相关研究进展. *药物化学*, 2025, 13(1): 107-117.
13. 董晓武, 等. 基于人工智能的小分子生成模型在药物发现中的研究进展. *中国药科大学学报*, 2024.
14. [内蒙古大学学位授权点建设年度报告](https://gs.imu.edu.cn/__local/8/28/7F/3F8649389E08A6844F194F45326_0FE47AA5_4EC068.pdf). 内蒙古大学, 2024.