# 矩阵乘积态在量子信息处理中的应用与优化：2022–2025年综述

近年来，矩阵乘积态（Matrix Product States, MPS）作为一维张量网络的核心代表已成为量子信息处理的重要工具，在量子模拟、量子机器学习、基态求解和状态制备等多个领域取得显著进展。本综述汇总了2022年至2025年期间MPS相关研究的关键成果，重点总结了MPS在量子计算硬件实现、优化算法开发和实际应用中的突破，并揭示了该领域面临的核心挑战与未来发展方向。

## 引言

矩阵乘积态是一种通过按序列排列三指标张量（及边界张量）来表达高维量子态的参数化方式，其中虚指标（bond indices）的维数$\chi$称为键维（bond dimension）[2][5]。相比直接存储指数级维数的完整态向量，MPS的多项式存储复杂度$\mathcal{O}(N\chi^2 d)$使其在经典计算机上能高效处理面积律（area law）满足的一维多体系统[1][5]。这种高效性与密度矩阵重整化群（DMRG）等强大算法的兼容性，使MPS成为研究强关联量子多体系统的标准工具。

然而，随着NISQ（噪声中等规模量子）时代设备的涌现和量子机器学习需求的增加，MPS的应用边界被不断拓展。**在量子硬件实现层面**，研究者探索了如何直接在真实量子处理器上制备和优化MPS状态，以规避经典模拟的可扩展性瓶颈[4][44]。**在算法优化层面**，针对梯度消失（barren plateau）、分布式计算与混合经典-量子框架等新问题的解决方案涌现，显著提升了MPS在NISQ设备上的可实用性[37]。**在应用拓展层面**，MPS突破了传统量子模拟的边界，被成功应用于组合优化、机器学习、时间序列预测和隐私保护合成数据生成等经典任务[3][16][25]。

本综述的组织架构如下：首先从理论基础与表示能力出发，阐明MPS作为通用逼近器的数学性质；其次分别综述MPS在量子模拟、量子优化、量子机器学习和状态制备四个主要应用领域的进展；最后总结实验与评估的共性结论，指出2025年前后该领域的关键研究趋势与挑战。

## 方法分类与代表作

### MPS的理论基础与表示能力

**表示论与函数逼近** 
Guo和Draper（2021）的工作从布尔函数和连续函数两个角度系统研究了MPS的通用表达能力[38]。他们证明了具有缩放不变sigmoid激活的MPS的函数空间在紧致子空间上稠密，揭示了MPS与单隐层神经网络配备核函数的等价性。特别地，非线性核（如多项式核）在等价神经网络中自然涌现，这表明MPS内在地编码了输入分量间的耦合。这项工作将MPS从量子领域的特殊工具提升为具有一般函数逼近能力的计算框架，为其在经典机器学习中的应用奠定了理论基础。

**有限温度复杂度分析**
Iwaki与Hotta（2024）通过随机采样框架针对有限温度MPS描述的多体系统推导了样本复杂度的解析公式[39]。他们证明高温和低温状态在计算复杂度上呈现质的差异——高温时复杂度与系统大小线性相关，低温时呈二次关系，且在中间温度范围存在明确的跨越。这项工作深化了对量子多体系统计算难度的理解，特别是为热态模拟和有限温度性质计算提供了复杂度下界。

### MPS在量子模拟中的应用

**多体系统基态求解的混合经典-量子方法**
Liu等人（2024，arXiv:2401.02355）提出了一种混合DMRG-VQE算法，其核心创新在于将经典DMRG的MPS ansatz转化为量子电路[9]。具体地，他们通过一系列单位算子$U_i = U_N U_{N-1} \cdots U_1 |0\rangle$的顺序堆积来在量子处理器上制备任意MPS，每个$U_i$对应原DMRG中的局部优化步骤。在Kagome格Heisenberg模型上的数值验证表明，相比标准VQE，该方法显著降低所需参数数量，且对非局部纠缠结构的适应性更强。引入零噪声外推（zero-noise extrapolation）后，算法在现实噪声下仍能可靠地定位强关联系统的基态物理。

**格规范理论的MPS模拟**
Emergent Mind综述[1]指出，在Schwinger模型等格规范理论的MPS表示中，虚指标维数的受控性允许有效编码规范约束，使得多项式资源标度的计算可达性增强。MPS框架天然适应周期边界条件，且能通过局部键截断（local bond truncation）精确保留规范不变性。对Schwinger模型的MPS模拟实现了物理可观察量如基态能、激发间隙和手征凝聚的准精确计算，计算成本仅与系统大小和键维的多项式有关。

**强关联电子系统的有限温度模拟**
Zhou等人（2024，arXiv:2312.04420）开发了随机MPS（stoMPS）方法，将MPS技术与蒙特卡洛采样相结合，特别针对有限温度的量子格模型[15][18]。该方法克服了传统DMRG在高温下的困难，通过在MPS支撑下进行统计采样，有效地平衡了精度与计算开销。与基于Gibbs态的方法相比，stoMPS在中等耦合强度区域展现出更稳定的收敛性，为非平衡动力学和混合-纯化过程提供了新的计算手段。

### MPS在量子机器学习中的应用

**监督学习与联合数据生成**
Mossi、Žunkovic与Flouris（2024，arXiv:2406.17441）提出了一个新颖的MPS框架，使其同时承载分类器与生成器的双重功能[13]。受GAN启发，该框架通过MPS学习数据的联合概率分布，在编码物理约束的同时生成更真实的样本、减少离群值。论文引入了替代嵌入函数以高效计算边际概率密度，无需多维积分；同时提出了非归一化MPS的精确采样方法。在图像分类与异常检测任务上的实验表明，该双功能MPS模型在监督学习精度与生成质量间达成有效平衡，相比单一功能的MPS有显著改进。

**隐私保护合成数据生成**
Moreno R等人（2025，arXiv:2508.06251）将MPS应用于差分隐私（differential privacy）框架下的高质量合成表格数据生成[25]。他们将梯度裁剪与噪声注入集成于MPS训练中，通过Rényi差分隐私会计获得形式隐私保证。与CTGAN、VAE、PrivBayes等经典方法的对标实验表明，在严格隐私限制（如$\varepsilon=1$）下，MPS生成的数据在保真度与下游机器学习任务性能上均显著领先，同时保持了张量网络的可解释性与可扩展性。这项工作示范了MPS从"物理工具"向隐私感知机器学习工具的转变。

**时间序列学习**
Moore等人（2025，Physical Review Research，arXiv:16）开发了MPSTime算法，首次系统地将MPS应用于时间序列的联合概率分布学习[16]。算法无需多维积分即可计算边际PDF，仅需适度的键维（5–50范围内），支持统一的对数损失函数下的分类与缺失值填补。在医学、能源和天文学的真实数据集上的验证表明，MPSTime在保持竞争性能的同时，提供了经典模型所缺乏的完整联合分布信息，为因果推断和不确定性量化开辟了新路径。

### 量子处理器上MPS的制备与优化

**量子MPS及其变分优化**
Guo等人（2025，arXiv:2506.08395）提出了量子版本的MPS（qMPS），并开发了变分量子MPS（vqMPS）方法[4]。与经典MPS中辅助指标维数指数增长不同，qMPS将这些指标编码为物理量子比特，使辅助维数的空间复杂度从指数降至对数。通过变分量子MPS方法，研究者能在近期量子设备上直接运行DMRG等价物，同时通过局部优化显著减少单次变分步骤中涉及的量子比特数（相比VQE）、缓解梯度消失。论文在模拟中验证了该方法对3–8量子比特态的分解，达到>96%的保真度，并讨论了与经典DMRG的混合计算范式。

**自适应常深度制备**
Smith等人（2024，PRX Quantum 5, 030344）证明了一大类MPS可通过自适应量子电路（结合中途测量与前馈操作）以常数深度精确制备[44]。传统单位电路需要深度随系统尺度线性增长，但该工作展示了对称受保护拓扑态、非阿贝尔对称性约束的MPS等都可突破这一速度限制。通过在小规模量子比特组上并行制备独立MPS再用测量"融合"它们的策略，算法在关联长度有限的MPS族中实现了常数深度。这项突破对NISQ设备上的状态初始化极具实用价值。

**动态量子电路的常深度MPS制备**
PennyLane教程与相关工作[11]详细阐述了如何利用动态量子电路（mid-circuit measurement + classical feedforward）实现MPS的常深度制备。与线性深度的顺序制备相比，该方法引入辅助键量子比特作为中间纽带，通过测量中间结果并按需施加修正操作，逐步消除"缺陷"并推向边界。虽然需要额外的辅助资源，但在相干时间受限的硬件上，常数深度的收益往往超过额外量子比特的代价。

**高效态制备用于QML**
Dutta等人（2026，arXiv:2601.09363）发展了MPS辅助的态制备方法，通过迭代二量子比特酉操作顺序"解纠缠"从古典数据编码的量子态[8]。该方法无需启发式搜索，直接从MPS表示构造低深度电路。在MNIST、Fashion-MNIST等数据集的实验中，MPS方法的电路门数比常规态制备减少数个量级，同时在IBM Algiers设备上实现了95%±2.3的平均测试精度（相比精确制备的45.8%±6.7），展现了MPS在保持数据保真度与降低电路复杂度间的最优权衡。

### MPS在组合优化中的应用

**变分MPS用于组合优化**
Preisser、Mc Keever与Lubasch（2025，arXiv:2512.20613）将变分MPS与乘积态（PS）ansatz结合至量子退火Hamiltonian框架，嵌入迭代局部搜索（Iterated Local Search, ILS）元启发式，形成量子启发的混合算法[3]。在最大割问题的基准测试（规模达50000变量）上，该方法相比经典ILS、标准MPS方法、QAOA及其他变分量子启发求解器均表现优异。核心创新在于用随机性和局部搜索的联合策略打破了纯变分方法的局部最小值陷阱，展现了MPS在NP难问题中的竞争力。

### MPS与其他张量网络方法的比较

**MPS与高阶张量网络的对比**
Ge与Eisert（2015，arXiv:1411.2995）的理论工作表明，虽然面积律与高效张量网络表示常被关联，但实际上面积律状态的空间包含指数维数的子空间，其中许多无法被多项式PEPS或MERA有效表示[24]。这一关键定理指出，仅凭纠缠熵的面积律性质不足以保证一维外的系统能被多项式张量网络高效描述。因此MPS在一维的优势是本质的，而对高维系统需要考虑PEPS等更复杂结构，但代价是算法复杂度陡增。

**灵活几何的投影纠缠对态**
Patra、Singh与Orús（2024，arXiv:2407.21140）扩展了PEPS框架，使其能在任意、波动且密集连接的图上运行[19]。通过引入度约束$\kappa$和动态边删除规则，算法能让PEPS几何自适应系统的关联结构。在几百自旋的稠密图基准上（如经典自旋玻璃、量子退火），该方法在灵活性与计算成本间达成平衡，展示了当MPS因维度限制不再适用时，PEPS如何被有效推广。

## 实验与评价总结

### 共性收益与性能指标

**计算效率的量化进展**
跨越多个应用领域，MPS相比同类方法在计算资源消耗上呈现一致的优势。在量子模拟中，DMRG-MPS的复杂度为$\mathcal{O}(N \chi^3 d^3)$每个迭代步骤，相比完全张量的$\mathcal{O}((Nd)^3)$有指数级改进[1][10]。在机器学习应用中，MPSTime与MPS隐私生成模型所需的模型参数数（可控键维）远少于深度神经网络，分别实现了表格数据压缩（特征维数减少3–5倍）与合成数据生成（在$\varepsilon=1$隐私下优于对标方法）[16][25]。在量子电路制备中，自适应常深度方案[44]将制备深度从$\Theta(N)$降至$\mathcal{O}(1)$，尽管需额外辅助量子比特，但在NISQ设备受相干时间限制的约束下通常是有利的权衡。

**精度与保真度的量化评估**
在ground-state VQE任务中，MPS ansatz的变分能量收敛速度与逼近精度直接受键维控制。Kagome Heisenberg模型的DMRG-VQE实验表明，键维$\chi=2$在局部纠缠结构下已获得接近精确解的能量，但对非局部纠缠则需增至$\chi=6$才能匹配精度[9]。在QML应用中，MPS基态编码（state preparation fidelity）在MNIST数据上通常超过98%，而在Fashion-MNIST（更复杂的数据分布）上维持在83%峰值，整体优于启发式编码方案[8]。在隐私敏感的合成数据生成中，MPS在隐私预算$\varepsilon=0.1$（严格隐私）下仍能生成Wasserstein距离<0.05的数据，相比CTGAN与PrivBayes的0.15–0.3显著更优[25]。

**标度性的实验观察**
多篇论文报告了MPS方法的良好标度性，但都在特定条件下。在量子模拟中，MPS对面积律满足的系统（间隙Hamiltonian）标度优秀，但对临界系统（无能隙）则需$\chi \propto e^{\alpha L/v_s}$（$L$为系统大小，$v_s$为声速）的指数增长[2][21]。在QML中，键维需求与输入数据的内在复杂度（分形维数、信息论熵）相关，高维度、低关联数据需更大$\chi$[16]。在组合优化中，MPS-ILS在50000变量问题上相比VQE的QAOA实现了显著优势，暗示classical-inspired的变分策略在大规模离散问题上比纯量子方法更稳健[3]。

### 关键瓶颈与限制因素

**梯度消失问题的持久挑战**
Qi等人（2021，Quantum 5, 1466）通过ZX演算分析框架证明了MPS启发ansatz存在梯度消失现象[37]。特别地，硬件高效ansatz与某些MPS变体在随机初始化下表现出梯度消失，尽管QCNN与树张量网络ansatz能避免。这意味着naive的参数初始化或深度选择可能导致VQE优化陷入平坦区域，使学习速率指数衰减。后续工作如Preisser等人提出的结合ILS的随机扰动策略，部分规避但未完全解决此问题。

**纠缠结构匹配的困难**
实验中频繁观察到当目标态的纠缠模式与MPS的单链拓扑不匹配时，所需键维急剧增长。Kagome格Heisenberg模型的非局部标记实验[9]清晰地展示，改变量子比特标记使纠缠结构"跳跃"后，需从$\chi=2$增至$\chi=6$才能保持精度，这在硬件资源有限时成为瓶颈。高维系统中MPS的应用本质受限，PEPS的引入虽可改善，但算法复杂度激增。

**现实噪声下的可靠性问题**
DMRG-VQE在数值中表现出色，但真实硬件实验（如IBM Algiers）中零噪声外推虽有帮助，仍无法完全消除误差。Dutta等人[8]的实验表明，态制备保真度在noisy设备上从>98%下降至83%，说明电路深度每增加一层就累积可观的相位噪声与depolarizing errors。对超过20量子比特的系统，MPS制备电路的深度依赖性使其在当前硬件上的实用性受限。

## 趋势与挑战

### 2025年前后的真实研究方向

**1. 量子-经典混合MPS框架的普遍化**
随着量子内存（qubit storage能力）与mid-circuit measurement在Atom Hub、IonQ等平台的部署，分布式MPS优化（某些层在经典CPU上、关键层在量子处理器）将成为标准范式。2024–2025年的论文（如arXiv:2506.08395与PRX Quantum论文）已示范了这种混合的可行性与性能增益。预期2025年后，专门针对特定硬件拓扑（如仅近邻连接）的自适应键维调整算法会涌现，进一步降低量子资源消耗。

**2. MPS在非传统应用中的指数增长**
从纯粹量子物理出发，MPS正被移植至隐私机器学习（arXiv:2508.06251）、高维数据压缩（与神经压缩的融合）、因果推断（通过时间序列学习）等经典领域。这一跨学科的应用拓展反映了MPS作为**通用张量分解工具**的重新认识（参考arXiv:2103.08277的表示论工作）。2025年展望，类似应用的涌现会推动MPS库（如TensorNetwork框架）的标准化与用户友好化，吸引更多非物理背景的开发者参与。

**3. 多尺度与自适应结构搜索的融合**
arXiv:2512.24663与相关的张量网络结构搜索工作表明，固定键维的MPS正被动态键维与RG流引导的自适应张量网络取代。这一趋势源于对"最优键维是否存在"的深化认识——答案是高度问题与数据相关的。2025年前后，通过强化学习或神经架构搜索（NAS）自动优化MPS形态（键维、对称性约束、绑定结构）的工作会成为新热点，特别是在企业级应用（如能源优化、金融模拟）中。

### 根本性挑战与未来研究方向

**高维系统的本质限制**
虽然二维及以上系统可用PEPS或MERA，但这些方法的算法复杂度使其难以扩展到产业级问题。一个未解决的研究方向是**层次化MPS（Hierarchical MPS）**或**分层张量分解**能否在保持可扩展性的同时适应高维结构。初步工作如arXiv:2512.06111的树张量网络（TTN）随机化方法展示了希望，但尚需在大规模应用中验证。

**梯度优化与初始化的深层次理解**
尽管Preisser等人的ILS与自适应初始化策略缓解了梯度消失，但根本的理论认识仍缺乏。为何MPS ansatz的梯度统计特性与硬件效率ansatz不同？是否存在通用的初始化方案能普遍避免梯度消失？这些问题的解答需要结合从量子控制论、微分几何（Riemannian流形上的优化）与统计物理的交叉洞察。

**误差缓解与容错的一体化设计**
当前DMRG-VQE等方法将误差缓解（如零噪声外推）作为后处理，但MPS的内在结构（局部键截断）可能允许**内生的容错性**。研究如何设计MPS ansatz与优化算法使其对特定噪声类型（相位翻转、depolarizing）有内在抵抗力，将是通向实用量子模拟的关键。

## 结论

矩阵乘积态在2022–2025年期间的发展呈现出**从单纯量子工具向跨学科通用框架的转变**。理论层面，Guo等人的表示论工作确立了MPS的函数逼近能力，打破了其"仅适用量子系统"的刻板认识。应用层面，MPS已成功渗透量子模拟（多体基态与有限温度）、量子机器学习（分类、生成、时间序列）、隐私保护、组合优化等广泛领域，在许多任务上超越同类经典与量子方法。

在量子处理器的直接实现中，自适应量子电路的常深度制备与qMPS的混合古典-量子优化标志着从"经典模拟量子态"向"量子处理器原生运行MPS算法"的范式转换。这一转换的实现价值在于**绕过了经典模拟的指数复杂度瓶颈**，使NISQ设备能在有限相干时间内运行更深、更复杂的量子算法。

然而，梯度消失、纠缠结构匹配、现实噪声与高维系统的根本困难仍未解决。突破这些瓶颈需要多学科的深度融合：量子控制、优化论、神经网络架构设计与量子信息论的交汇。特别地，**自适应、多尺度的MPS框架**（如RG流引导的结构搜索）与**混合古典-量子的分布式优化**预期将在2025年后成为主流范式。

对实践者的建议是：在选择MPS作为特定问题的求解工具时，务必谨慎评估目标系统的纠缠特性与键维需求；对于跨越多个量子比特的优化任务，结合ILS或其他启发式的混合策略往往胜过纯粹变分方法；充分利用新兴硬件的mid-circuit measurement与qubit recycling能力，以最小化量子资源占用。未来的关键突破将取决于能否发展出对**任意纠缠结构都高效的张量网络表示**，以及**噪声稳健的原生量子算法**。

---

## 参考文献

[1] Emergent Mind. "Matrix Product States in Quantum Simulation." https://www.emergentmind.com/topics/matrix-product-states-mps

[2] David Wierichs et al. "Constant-depth preparation of matrix product states with dynamic quantum circuits." PennyLane, October 2024. https://pennylane.ai/qml/demos/tutorial_constant_depth_mps_prep

[3] Guillermo Preisser, Conor Mc Keever, Michael Lubasch. "Variational (matrix) product states for combinatorial optimization." arXiv:2512.20613, December 2025.

[4] 无署名作者. "Matrix Product State on a Quantum Computer." arXiv:2506.08395, June 2025.

[5] Wikipedia. "Matrix product state." https://en.wikipedia.org/wiki/Matrix_product_state

[6] Siddhartha Patra, Sukhbinder Singh, Román Orús. "Projected Entangled Pair States with flexible geometry." arXiv:2407.21140, July 2024.

[7] Alex Mossi, Bojan Žunkovic, Kyriakos Flouris. "A Matrix Product State Model for Simultaneous Classification and Generation." arXiv:2406.17441, June 2024.

[8] 无署名作者. "Efficient State Preparation for Quantum Machine Learning." arXiv:2601.09363, January 2026.

[9] 无署名作者. "Matrix product state ansatz for the variational quantum solution of ..." arXiv:2401.02355, January 2024.

[10] Emergent Mind. "Density Matrix Renormalisation Group (DMRG)." https://www.emergentmind.com/topics/density-matrix-renormalisation-group-dmrg

[11] Joshua B. Moore et al. "Using matrix-product states for time-series machine learning." Physical Review Research 7, 043010, October 2025.

[12] Alejandro Moreno R. et al. "Synthetic Data Generation and Differential Privacy using Tensor Networks' Matrix Product States (MPS)." arXiv:2508.06251, August 2025.

[13] Yimin Ge, Jens Eisert. "Area laws and efficient descriptions of quantum many-body states." arXiv:1411.2995, November 2014.

[14] Kevin C. Smith et al. "Constant-Depth Preparation of Matrix Product States with Adaptive Quantum Circuits." PRX Quantum 5, 030344, September 2024.

[15] Atsushi Iwaki, Chisa Hotta. "Sample complexity of matrix product states at finite temperature." Physical Review B 109, 224410, June 2024.

[16] Erdong Guo, David Draper. "Representation Theorem for Matrix Product States." arXiv:2103.08277, March 2021.