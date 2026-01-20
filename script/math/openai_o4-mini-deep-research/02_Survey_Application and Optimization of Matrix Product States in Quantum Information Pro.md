# 矩阵乘积态在量子信息处理中的应用与优化综述

## 引言

矩阵乘积态（MPS）作为张量网络的一种形式，最初用于高效表示一维量子多体系统的基态，并在密度矩阵重整化群（DMRG）等方法中发挥核心作用。近年，MPS在量子计算与量子信息处理领域的应用也日益广泛。具体来说，研究者利用MPS帮助设计变分量子算法ansatz、完成量子态的高效编码与制备，以及加速量子态断层和噪声缓解等任务。同时，随着计算资源的发展，对MPS模型的优化也成为热点，如将经典MPS计算与量子硬件结合生成高保真态或提高数据加载效率。本综述聚焦2022–2025年期间MPS在量子信息处理中的代表性工作，按照主要方法类别介绍相应的研究成果，并总结其实验与评价结果，最后预测未来研究趋势与挑战。

## 方法分类与代表作

### 基于MPS的量子态制备与变分电路

1. **顺序生成变分量子态**：Hou 等人提出了一种顺序生成的变分量子电路架构 ([arxiv.org](https://arxiv.org/abs/2305.12856#:~:text=propose%20a%20sequentially%20generated%20circuit,number%20of%20quantum%20gate%20operations))。他们的ansatz可以在一维系统中高效生成任意给定键维的MPS（而在二维系统生成串态（string-bond）态），并用于重构能够用MPS表示的未知纯态和混合态。仿真实验表明，该ansatz在寻找典型一维和二维哈伯德模型基态时，仅需较少的量子门操作数即能达到高精度 ([arxiv.org](https://arxiv.org/abs/2305.12856#:~:text=propose%20a%20sequentially%20generated%20circuit,number%20of%20quantum%20gate%20operations))。

2. **基于去纠缠的态编译**：Mansuroglu 和 Schuch 针对量子编译提出了一种经典优化算法 ([arxiv.org](https://arxiv.org/abs/2504.21298#:~:text=We%20study%20the%20classical%20compilation,of%20all%20bonds%20are%20locally))。该算法通过反向施加一系列可参数化的“去纠缠门”层，逐层最小化双体纠缠熵，从而降低MPS的键维。由于可以通过MPS的标准$\Gamma$-$\Lambda$形式局部访问所有Schmidt系数，算法具有良好的并行化和可拓展性。作者在一维局域哈密顿量的基态和人工构造的高纠缠态上验证了该方法的有效性 ([arxiv.org](https://arxiv.org/abs/2504.21298#:~:text=We%20study%20the%20classical%20compilation,classically%20efficient%20even%20for%20deep))。

3. **量子版MPS（qMPS）变分算法**：Liu 等人提出了量子版的矩阵乘积态（qMPS）概念，并发展了在量子设备上以正交规范形式制备qMPS的变分算法 ([arxiv.org](https://arxiv.org/abs/2506.08395#:~:text=barren%20plateaus,fusion%20of%20different%20computing%20systems))。该方法相当于在近似量子设备上运行DMRG，能够显著减少局部优化所需的量子比特数，从而缓解了高维参数优化中的“贫瘠高原”问题。他们指出，与传统的VQE方法相比，qMPS可以在降低量子资源需求的同时获得更高的精度，并具有适用于分布式量子计算系统的潜力 ([arxiv.org](https://arxiv.org/abs/2506.08395#:~:text=barren%20plateaus,fusion%20of%20different%20computing%20systems))。

4. **基于近似量子编译的MPS制备**：Jaderberg 等人针对“规范”MPS提出了一种浅层电路制备方案 ([arxiv.org](https://arxiv.org/abs/2503.09683#:~:text=Preparing%20matrix%20product%20states%20,a%20global%20quench%20over%20the))。他们利用近似量子编译（AQC）的启发式策略，通过自适应构造 ansatz（ADAPT-AQC）和改进的初始化来制备短程关联的MPS。实验证明，该方法可在有限深度的电路下近似任意规范MPS，并应用于模拟50个自旋的Heisenberg XXZ链的动力学，从而实现在当前NISQ器件上制备较长量子链态。

5. **MPS启发的VQE ansatz**：Javanmard 等人提出了一种受DMRG算法启发的VQE电路ansatz，用于在量子硬件上近似解决二维Heisenberg模型的基态问题 ([arxiv.org](https://arxiv.org/abs/2401.02355#:~:text=algorithm%20with%20a%20quantum%20circuit,is%20efficient%20for%20NISQ%20devices))。该ansatz深度低、参数量小，专为片段化的Kagome晶格量子纹理设计。研究者结合零噪声外推技术，在带有实际误差率的模拟条件下，对Kagome模型的一个子区进行求解，并证明了混合DMRG–VQE方法在强关联系统中能接近正确基态表现 ([arxiv.org](https://arxiv.org/abs/2401.02355#:~:text=algorithm%20with%20a%20quantum%20circuit,is%20efficient%20for%20NISQ%20devices))。

### 混合经典–量子算法与噪声缓解

1. **VQE的MPS预优化（VTNE）**：Khan 等人提出了变分张量网络本征求解器（VTNE）框架 ([arxiv.org](https://arxiv.org/abs/2310.12965#:~:text=present%20and%20benchmark%20an%20approach,starting%20VQE%20from%20these%20parameters))。该方法通过限制键信度的MPS近似仿真参数化量子电路，来寻找优化VQE的初始参数。他们在一维和二维费米哈伯德模型上进行测试：在一维系统中，VTNE找到的量子线路参数使得能量误差低于基态能量的0.5% ([arxiv.org](https://arxiv.org/abs/2310.12965#:~:text=the%20parameterized%20quantum%20circuit%20,starting%20VQE%20from%20these%20parameters))；在二维系统中，VTNE预优化得到的参数使VQE显著加速收敛。结果表明，更大的键维MPS预优化可进一步降低需要运行在量子硬件上的迭代次数 ([arxiv.org](https://arxiv.org/abs/2310.12965#:~:text=eigensolver%20,as%20the%20initialization%20for%20the))。

2. **MPS与量子硬件协同模拟**：Anselme Martin 等人将MPS与实际量子器件相结合以进行量子动力学模拟 ([arxiv.org](https://arxiv.org/abs/2305.19231#:~:text=worlds%3A%20the%20short,with%20efficient%20circuit%20transpilation%20we))。他们利用MPS高效处理短时程演化（低纠缠阶段），将所得MPS态编译为浅层电路；随后在量子计算机上增加演化时间，通过优化的矩阵乘积算符（MPO）电路持续演化。仿真表明，这种混合方案显著降低了量子噪声要求：在考虑噪声模型后，该方案在10比特实验装置上比低键信度MPS或纯量子分裂步进（Trotter）演化都能覆盖更长的有效演化时间 ([arxiv.org](https://arxiv.org/abs/2305.19231#:~:text=worlds%3A%20the%20short,with%20efficient%20circuit%20transpilation%20we))。

3. **矩阵乘积量子通道噪声缓解**：Filippov 等人提出了一种基于矩阵乘积张量网络的噪声缓解技术 ([arxiv.org](https://arxiv.org/abs/2212.10225#:~:text=tensor%20network%20representation%20of%20a,parts%20have%20the%20same%20bond))。该方法首先使用量子硬件产生初始近似态，再利用一个参数化的完全正性质子映射（矩阵乘积通道）对噪声态进行后处理，使其向目标基态偏移。在无噪声近似的水分子示例中，通过这种张量网络通道处理得到的能量甚至低于原始无噪声ansatz的结果，表明混合使用量子硬件和经典优化软件（相同键信度条件下）可以优于完全经典策略 ([arxiv.org](https://arxiv.org/abs/2212.10225#:~:text=tensor%20network%20representation%20of%20a,parts%20have%20the%20same%20bond))。

### 量子态断层与验证

1. **基于MPO的可压缩断层**：Zhen Qin 等针对一维量子器件产生的态提出MPO结构的断层方案 ([arxiv.org](https://arxiv.org/abs/2306.09432#:~:text=attempt%20to%20bridge%20this%20gap,POVMs%20that%20can%20be%20implemented))。他们证明，对于有限键信度的MPO态，只需与量子比特数呈线性增长的随机测量数就可以保留全态信息（在高斯测量模型下）。进一步，在可由量子计算机实施的Haar随机POVM测量模型下，所需的态副本数仅随量子数呈多项式增长，以保证有限误差下的MPO恢复 ([arxiv.org](https://arxiv.org/abs/2306.09432#:~:text=recovery%20of%20MPOs%20using%20tools,to%20guarantee%20bounded%20recovery%20error))。这一结果表明，针对结构化低纠缠态的量子态断层在采样复杂度上远优于一般无结构态断层 ([arxiv.org](https://arxiv.org/abs/2306.09432#:~:text=recovery%20of%20MPOs%20using%20tools,to%20guarantee%20bounded%20recovery%20error))。

2. **张量列车交叉断层**：Lidiak 等人提出了一种使用张量列车（TT）交叉近似方法进行全态断层的新方案 ([arxiv.org](https://arxiv.org/abs/2207.06397#:~:text=It%20has%20been%20recently%20shown,for%20unstructured%20states%20and%20local))。该方法使得在每次测量时只需对局部算符进行测量，即可恢复高秩密度矩阵。与传统断层相比，其所需的态副本数呈指数级减少：在已知全局MPS结构下，通过少量局部测量即可准确重建全态；此外，在已收集数据上加入监督学习可以进一步提升重建保真度 ([arxiv.org](https://arxiv.org/abs/2207.06397#:~:text=It%20has%20been%20recently%20shown,for%20unstructured%20states%20and%20local))。研究表明，只要全态能从局部约简推导出来，该方法在规模上是可扩展的 ([arxiv.org](https://arxiv.org/abs/2207.06397#:~:text=It%20has%20been%20recently%20shown,for%20unstructured%20states%20and%20local)) ([arxiv.org](https://arxiv.org/abs/2207.06397#:~:text=measurement%20settings%20using%20a%20method,be%20reconstructed%20from%20local%20reductions))。

### 数据编码与量子机器学习

1. **MPS加速量子核方法**：Metcalf 等人使用MPS模拟器来实现大规模的量子核学习模型 ([arxiv.org](https://arxiv.org/abs/2411.09336#:~:text=employ%20it%20to%20perform%20a,quantum%20model%20performance%20at%20scale))。他们采用一维链式量子电路ansatz，对具有165个特征的6400个训练样本进行分类任务。实验中评估了CPU和GPU平台上MPS模拟的性能，发现随着量子比特间相互作用距离的增加，GPU模拟在某个临界点后运行速度超过CPU ([arxiv.org](https://arxiv.org/abs/2411.09336#:~:text=employ%20it%20to%20perform%20a,quantum%20model%20performance%20at%20scale))。最重要的是，他们首次实验证明，随着输入特征维度和数据量的增加，量子核模型的分类性能持续提升 ([arxiv.org](https://arxiv.org/abs/2411.09336#:~:text=ansatz%20on%20a%20linear%20chain,quantum%20model%20performance%20at%20scale))，表明MPS模拟能够让量子学习方法在更大规模数据上进行评估。

2. **经典数据的MPS编码优化**：Jeon 等人针对将经典数据编码为MPS结构提出了优化策略 ([arxiv.org](https://arxiv.org/abs/2406.06935#:~:text=for%20encoding%20classical%20data,efficient%20and%20accurate%20quantum%20data))。观察到数据排列顺序会影响MPS截断误差后，他们设计了一种寻找最佳量子比特映射的方法，以最小化编码损失。实验证明，在量子分类器任务中采用优化映射比传统映射方式获得了更高的模型准确度 ([arxiv.org](https://arxiv.org/abs/2406.06935#:~:text=finds%20optimal%20qubit%20mapping%20for,efficient%20and%20accurate%20quantum%20data))，说明合理的映射显著提高了MPS作为数据嵌入表达时的效率和保真度。

3. **结构化图像数据编码**：Green 和 Wang 进一步研究了MPS在结构化数据（函数和图像）编码中的潜力 ([arxiv.org](https://arxiv.org/abs/2502.16464#:~:text=range%20of%20functions%20and%20images,on%20a%20circuit%20with%20a))。他们提出基于MPS的去纠缠算法，仅使用$O(n)$深度电路便可编码低阶分段多项式函数，准确度超过99.99%。此外，他们利用MPS对离散小波变换（DWT）系数的近似，实现了128×128医学图像在14个量子比特上的高保真制备（保真度>99.1%） ([arxiv.org](https://arxiv.org/abs/2502.16464#:~:text=range%20of%20functions%20and%20images,on%20a%20circuit%20with%20a))。这些结果展示了MPS在高维数据量子化编码中的高效性。

## 实验与评价总结

上述工作表明，MPS相关方法在多种量子信息处理场景中具备显著优势：首先，它们通常能够**降低量子资源需求**并保持高保真度。例如，Khan等基于MPS的VQE预优化在一维系统中获得了仅0.5%以内的能量误差 ([arxiv.org](https://arxiv.org/abs/2310.12965#:~:text=the%20parameterized%20quantum%20circuit%20,starting%20VQE%20from%20these%20parameters))；Green等利用MPS编码函数和图像在低量子比特数下实现了>99%保真度 ([arxiv.org](https://arxiv.org/abs/2502.16464#:~:text=range%20of%20functions%20and%20images,on%20a%20circuit%20with%20a))。其次，MPS方法有助于**缓解噪声和优化收敛**：Anselme等的混合模拟在含噪环境下将10比特系统的可模拟时间延长到超过传统MPS或纯量子Trotter方案的水平 ([arxiv.org](https://arxiv.org/abs/2305.19231#:~:text=worlds%3A%20the%20short,with%20efficient%20circuit%20transpilation%20we))；Filippov等的矩阵乘积通道结合量子硬件实现了比无噪声ansatz更低的计算能量 ([arxiv.org](https://arxiv.org/abs/2212.10225#:~:text=tensor%20network%20representation%20of%20a,parts%20have%20the%20same%20bond))。此外，在量子机器学习任务中，Metcalf等通过MPS模拟表现出随着数据规模增大模型精度提升的趋势 ([arxiv.org](https://arxiv.org/abs/2411.09336#:~:text=systematically%20increasing%20the%20qubit%20interaction,quantum%20model%20performance%20at%20scale))，Jeon等发现映射优化提高了MPS分类器的性能 ([arxiv.org](https://arxiv.org/abs/2406.06935#:~:text=finds%20optimal%20qubit%20mapping%20for,efficient%20and%20accurate%20quantum%20data))。总体来看，MPS方法能够有效**管理纠缠**、提高计算效率并改善算法表现，但受限于其固定键维，对于高纠缠态或高维系统的表达能力依然有限。

## 趋势与挑战

- **更深度的混合算法开发**：未来研究将进一步探索经典MPS算法与量子硬件的结合，如利用MPS进行更精细的量子电路参数预优化或实时纠缠补偿，以节省量子资源和克服噪声限制。  
- **高维纠缠体系推广**：由于MPS天生适用于一维体系，对二维及更高维度系统则性能受限。研究趋势可能包括将PEPS、树张量网络等扩展方法与MPS思想结合，使得量子算法和模拟能够处理更多维度和高纠缠的场景。  
- **动态自动化与可伸缩优化**：会有更多自动化技术用于选择或优化MPS结构，例如自适应键维调整、智能数据映射，以及与机器学习结合的优化流程，以适应复杂任务需求。  
- **噪声鲁棒性与纠错集成**：在实际量子硬件中，提升MPS算法对噪声的耐受性是关键挑战之一。未来可能整合更多错误缓解和纠错技术，如基于MPS的噪声模型精准化和后处理，以及与量子纠错码的协同设计。  
- **应用领域拓展**：随着量子资源的提升，MPS方法有望在化学分子模拟、量子化学、量子优化等领域发挥更大作用，例如借助MPS进行复杂分子基态搜索或组合优化问题的近似求解。

总的来说，2025年前后MPS在量子信息处理中的研究将着重于提升算法通用性与可扩展性，探索与其他量子计算资源的协同应用，同时不断优化模型效率以应对实际硬件和高维度问题的挑战。

## 结论

本文综述了2022–2025年间矩阵乘积态在量子信息处理中的代表性工作，涵盖了MPS在量子态制备、变分电路设计、混合经典–量子模拟、噪声缓解以及量子态断层和机器学习中的应用。总体看，MPS相关方法在各种任务中表现出高效的资源利用和出色的性能，例如减少所需比特数、提高量子态制备保真度、加速优化算法收敛等。然而，MPS本身的表达能力和可扩展性限制了其在更高纠缠或更多维度场景下的直接应用。面向未来，如何结合更广泛的张量网络结构和量子计算技术，以及开发自动化优化和可靠性的手段，将成为该领域的主要研究方向。

## 参考文献

[1] Yong Liu, Guangyao Huang, Yizhi Wang, Junjie Wu. *Matrix Product State on a Quantum Computer*. arXiv:2506.08395 (2025). 链接：https://arxiv.org/abs/2506.08395.

[2] Refik Mansuroglu, Norbert Schuch. *Preparation Circuits for Matrix Product States by Classical Variational Disentanglement*. arXiv:2504.21298 (2025). 链接：https://arxiv.org/abs/2504.21298.

[3] Ben Jaderberg, George Pennington, Kate V. Marshall, et al. *Variational preparation of normal matrix product states on quantum computers*. arXiv:2503.09683 (2025). 链接：https://arxiv.org/abs/2503.09683.

[4] Xiaokai Hou, Qingyu Li, Man-Hong Yung, et al. *A sequentially generated variational quantum circuit with polynomial complexity*. arXiv:2305.12856 (2023). 链接：https://arxiv.org/abs/2305.12856.

[5] Younes Javanmard, Ugne Liaubaite, Tobias J. Osborne, et al. *Matrix product state ansatz for the variational quantum solution of the Heisenberg model on Kagome geometries*. arXiv:2401.02355 (2024). 链接：https://arxiv.org/abs/2401.02355.

[6] Abid Khan, Bryan K. Clark, Norm M. Tubman. *Pre-optimizing variational quantum eigensolvers with tensor networks*. arXiv:2310.12965 (2023). 链接：https://arxiv.org/abs/2310.12965.

[7] Baptiste Anselme Martin, Thomas Ayral, François Jamet, et al. *Combining Matrix Product States and Noisy Quantum Computers for Quantum Simulation*. arXiv:2305.19231 (2023). 链接：https://arxiv.org/abs/2305.19231.

[8] Sergey Filippov, Boris Sokolov, Matteo A. C. Rossi, et al. *Matrix product channel: Variationally optimized quantum tensor network to mitigate noise and reduce errors for the variational quantum eigensolver*. arXiv:2212.10225 (2022). 链接：https://arxiv.org/abs/2212.10225.

[9] Zhen Qin, Casey Jameson, Zhexuan Gong, et al. *Quantum State Tomography for Matrix Product Density Operators*. arXiv:2306.09432 (2023). 链接：https://arxiv.org/abs/2306.09432.

[10] Alexander Lidiak, Casey Jameson, Zhen Qin, et al. *Quantum state tomography with tensor train cross approximation*. arXiv:2207.06397 (2022). 链接：https://arxiv.org/abs/2207.06397.

[11] Mekena Metcalf, Pablo Andrés-Martínez, Nathan Fitzpatrick. *Realizing Quantum Kernel Models at Scale with Matrix Product State Simulation*. arXiv:2411.09336 (2024). 链接：https://arxiv.org/abs/2411.09336.

[12] Hyeongjun Jeon, Kyungmin Lee, Dongkyu Lee, et al. *Optimal Qubit Mapping Search for Encoding Classical Data into Matrix Product State Representation with Minimal Loss*. arXiv:2406.06935 (2024). 链接：https://arxiv.org/abs/2406.06935.

[13] Josh Green, Jingbo B. Wang. *Quantum Encoding of Structured Data with Matrix Product States*. arXiv:2502.16464 (2025). 链接：https://arxiv.org/abs/2502.16464.