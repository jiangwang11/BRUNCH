好的，这是一篇关于2022-2025年生物启发式元启发算法在工程优化中应用的中文学术综述。

## 生物启发式元启发算法在工程优化中的应用：2022-2025年发展综述

### 引言

工程优化问题普遍存在高维度、非线性、多模态、约束复杂等特点，传统优化方法往往难以有效求解。生物启发式元启发算法（Bio-inspired Metaheuristic Algorithms, BIMA）凭借其无需梯度信息、全局寻优能力强、对问题类型适应性好等优势，成为解决复杂工程优化问题的热门工具。BIMA模拟自然界中生物的集体行为或进化过程，如社会协作、觅食策略或遗传变异，通过迭代搜索以逼近最优解。近年来，随着人工智能技术的快速发展，BIMA在理论和应用两方面都取得了显著进展，尤其在算法改进、混合策略以及与机器学习等领域的结合上表现突出。本综述旨在回顾2022-2025年期间生物启发式元启发算法在工程优化领域的代表性工作，分析其核心方法、关键贡献，并展望未来的研究趋势。

### 方法分类与代表作

生物启发式元启发算法种类繁多，多数研究集中于对现有算法的改进或结合多种策略构造新型算法，以增强其全局搜索能力、局部开发能力、收敛速度和对复杂约束的处理能力。

#### 1. 基于群体智能的改进与混合算法

群体智能算法（Swarm Intelligence Algorithms）模拟生物群体协作行为，如觅食、迁徙等。主要代表包括粒子群优化（PSO）、灰狼优化（GWO）、鲸鱼优化（WOA）等。

*   **蜣螂算法 (Dung Beetle Optimizer, DBO) 及其改进**
    *   **研究问题**: 针对电网巡检任务中的车机协同路径规划问题，传统算法计算复杂度高、适应性差，蜣螂算法存在全局搜索能力弱和易陷入局部最优的缺点 [pdf.hanspub.org (基于改进蜣螂算法的车机协同巡检路径规划方法)](https://pdf.hanspub.org/pm2025151_161252697.pdf)。
    *   **核心方法**: [pdf.hanspub.org (基于改进蜣螂算法的车机协同巡检路径规划方法)](https://pdf.hanspub.org/pm2025151_161252697.pdf) 主要进行三方面改进：首先，采用Logistic混沌映射优化初始解分布，提高搜索多样性；其次，在滚球阶段引入鱼鹰算法（Osprey algorithm）的全局搜索策略以增强全局寻优能力和收敛稳定性；最后，在觅食阶段引入自适应t分布策略，增强局部寻优能力，避免局部最优。
    *   **关键实验结论**: 在CEC2021标准函数集测试中，改进蜣螂算法展现出更好的求解精度和收敛速度。在车机协同路径规划案例中，该方法在不同车速下均能有效求解，且在正常场景下节约了6.38分钟的计算时间 [pdf.hanspub.org (基于改进螂算法的车机协同巡检路径规划方法)](https://pdf.hanspub.org/pm2025151_161252697.pdf)。

*   **粒子群优化 (Particle Swarm Optimization, PSO) 及其改进**
    *   **研究问题**: 传统PSO在求解复杂优化问题时易陷入局部最优，限制了其全局搜索性能，且其优化结果可能在数学上满足目标函数但却不符合工程预期（EIS问题） [pdf.hanspub.org (面向全局优化的种群中心引导型粒子群优化算法)](https://pdf.hanspub.org/csa_1543619.pdf), [www.cup.edu.cn (基于工程经验的群智能通用PID参数整定)](https://www.cup.edu.cn/cupai/kxyj/kydt/a8f9f2b9b4c742dc98d4103a3747e96f.htm)。
    *   **核心方法**: 周刘长 (2025年) 提出了面向全局优化的种群中心引导型粒子群优化算法(PSOSI和PSOLP)。PSOSI引入种群中心位置作为额外引导信息增强全局搜索趋势；PSOLP基于种群聚集程度引入扰动策略，促进多样性 [pdf.hanspub.org (面向全局优化的种群中心引导型粒子群优化算法)](https://pdf.hanspub.org/csa_1543619.pdf)。 王铠铭等人（2025年）提出了EE-LMPSO算法，将工程经验与PSO结合，通过定义参数空间并引入参数物理优化方向约束（如开环增益核准则、积分-微分时间比例准则、比例-积分优化协调准则），规避了EIS问题 [www.cup.edu.cn (基于工程经验的群智能通用PID参数整定)](https://www.cup.edu.cn/cupai/kxyj/kydt/a8f9f2b9b4c742dc98d4103a3747e96f.htm)。袁磊（2025年）则针对机械臂时间最优轨迹规划问题，提出了一种基于改进遗传粒子群混合算法的方法，引入罚函数优化适应度函数改进遗传算法，并引入自适应权重因子和柯西变异算子改进粒子群算法，并将改进后的粒子群作为交叉算子融合到遗传算法中 [hndk.hainanu.edu.cn (基于改进遗传粒子群混合算法的机械臂时间最优轨迹规划)](https://hndk.hainanu.edu.cn/article/doi/10.15886/j.cnki.hdxbzkb.2024022201)。
    *   **关键实验结论**: 周刘长 (2025年) 的PSOSI和PSOLP在CEC-2022标准测试集及8个实际工程设计问题上，在优化精度和收敛稳定性方面均优于标准PSO及多种主流对比算法 [pdf.hanspub.org (面向全局优化的种群中心引导型粒子群优化算法)](https://pdf.hanspub.org/csa_1543619.pdf)。王铠铭等人（2025年）的EE-LMPSO算法提高了PID参数调整效率，增强了系统稳定性，在复杂动态环境中实现了更好的控制性能，并有效降低了EIS的发生概率 [www.cup.edu.cn (基于工程经验的群智能通用PID参数整定)](https://www.cup.edu.cn/cupai/kxyj/kydt/a8f9f2b9b4c742dc98d4103a3747e96f.htm)。袁磊（2025年）的混合算法相较于单一遗传算法和粒子群算法，求解精度更高，优化效率显著提高 [hndk.hainanu.edu.cn (基于改进遗传粒子群混合算法的机械臂时间最优轨迹规划)](https://hndk.hainanu.edu.cn/article/doi/10.15886/j.cnki.hdxbzkb.2024022201)。

*   **哈里斯鹰优化 (Harris Hawks Optimization, HHO) 及其改进**
    *   **研究问题**: HHO算法存在种群学习性与适应性不足，在合作觅食中内部交流不足，导致寻优精度与速度有待提高 [www.sciengine.com (基于信噪比的学习型哈里斯鹰优化算法)](https://www.sciengine.com/doi/pdfView/51D19E1CDEC64BA69A61BE2B4D238840)。
    *   **核心方法**: 张林等人（2025年）提出了SLHHO算法，通过引入信噪比（SNR）概念判断个体位置信息，设计了协调学习策略更新个体位置，并对逃逸距离重新设计，使其分布更均匀 [www.sciengine.com (基于信噪比的学习型哈里斯鹰优化算法)](https://www.sciengine.com/doi/pdfView/51D19E1CDEC64BA61BE2B4D238840)。
    *   **关键实验结论**: SLHHO算法在12个基准函数测试中表现出较强的竞争力，在压力容器设计问题中也验证了其实用性，优化后的解更加稳定 [www.sciengine.com (基于信噪比的学习型哈里斯鹰优化算法)](https://www.sciengine.com/doi/pdfView/51D19E1CDEC64BA61BE2B4D238840)。

*   **海鸥优化算法 (Seagull Optimization Algorithm, SOA) 及其改进**
    *   **研究问题**: SOA算法存在种群多样性低、易陷入局部最优从而降低寻优精度的问题 [www.arocmag.cn (一种多策略协同改进的海鸥算法及其应用)](https://www.arocmag.cn/abs/2022.09.0469)。
    *   **核心方法**: 李大海等人（2023年）提出了CMSOA算法。该算法结合多种策略：在迭代过程中使用正余弦算法（SCA）对停滞的海鸥种群个体进行扰动更新，以改善种群多样性；引入缩放因子动态调整个体与最优个体间的相对位移，提高探索与开发能力；采取随机对立学习微调最优个体位置，增强跳出局部最优的能力和寻优精度 [www.arocmag.cn (一种多策略协同改进的海鸥算法及其应用)](https://www.arocmag.cn/abs/2022.09.0469)。
    *   **关键实验结论**: 在14个CEC2017测试函数上，CMSOA在统计学意义上具有寻优优势；在三维无人机路径规划问题中也取得了良好效果 [www.arocmag.cn (一种多策略协同改进的海鸥算法及其应用)](https://www.arocmag.cn/abs/2022.09.0469)。

*   **人工蜂鸟算法 (Artificial Hummingbird Algorithm, AHA) 及其改进**
    *   **研究问题**: AHA算法在寻优精度和收敛速度上存在不足，容易陷入局部最优 [image.hanspub.org (邻域搜索和改进莱维因子的人工蜂鸟优化算法 Neighborhood Search and Artificial Hummingbird Optimization Algorithms with Improved Lévy Factors)](https://image.hanspub.org/Html/1-2571228_81778.htm)。
    *   **核心方法**: 何永康和李旭芳（2024年）提出了ALAHA算法。该算法在引导觅食和领地觅食阶段引入改进莱维飞行作为自适应权重因子调节搜索步长，增强全局搜索能力；根据种群收敛情况在蜂鸟个体周围进行自适应距离围猎搜索，提高算法搜索精度 [image.hanspub.org (邻域搜索和改进莱维因子的人工蜂鸟优化算法 Neighborhood Search and Artificial Hummingbird Optimization Algorithms with Improved Lévy Factors)](https://image.hanspub.org/Html/1-2571228_81778.htm)。
    *   **关键实验结论**: ALAHA算法在23个基准测试函数上，相比其他算法在寻优能力、稳定性和鲁棒性等方面均有提升 [image.hanspub.org (邻域搜索和改进莱维因子的人工蜂鸟优化算法 Neighborhood Search and Artificial Hummingbird Optimization Algorithms with Improved Lévy Factors)](https://image.hanspub.org/Html/1-2571228_81778.htm)。

#### 2. 通用理论框架与新型元启发算法

部分研究尝试为元启发算法建立更通用的框架，或者提出全新的元启发算法以解决特定挑战。

*   **通用进化元启发式算法 (Generalized Evolutionary Metaheuristic, GEM)**
    *   **研究问题**: 现有540多种自然启发式元启发算法缺乏统一理论框架，难以理解其搜索机制，限制了在工程优化中的应用 [themoonlight.io (A Generalized Evolutionary Metaheuristic (GEM) Algorithm for Engineering Optimization)](https://www.themoonlight.io/zh/review/a-generalized-evolutionary-metaheuristic-gem-algorithm-for-engineering-optimization)。
    *   **核心方法**: Xin-She Yang (2025年) 提出了GEM框架，旨在整合20多种现有算法。GEM通过共享基本更新方程和搜索机制，分析不同算法的相似性与差异性，建立统一的理论框架。其具体步骤包括解向量初始化、引导随机化搜索的更新机制（包含当前最佳解和个体最佳解的引导项）、位置更新项（可调参数适应不同算法特性）和基于目标函数值的接收标准 [themoonlight.io (A Generalized Evolutionary Metaheuristic (GEM) Algorithm for Engineering Optimization)](https://www.themoonlight.io/zh/review/a-generalized-evolutionary-metaheuristic-gem-algorithm-for-engineering-optimization)。
    *   **关键实验结论**: 在15个基准测试函数和工程设计案例中，GEM在固定参数下能够在绝大多数情况下找到全局最优解，并在某些案例中超越了现有最佳解 [themoonlight.io (A Generalized Evolutionary Metaheuristic (GEM) Algorithm for Engineering Optimization)](https://www.themoonlight.io/zh/review/a-generalized-evolutionary-metaheuristic-gem-algorithm-for-engineering-optimization)。

*   **鹈鹕优化算法 (Pelican Optimization Algorithm, POA) 及其改进**
    *   **研究问题**: POA算法在求解精度、稳定性方面存在不足，易陷入局部最优 [1951.mtmt.com.cn (基于混合策略改进的鹈鹕优化算法)].
    *   **核心方法**: 苏莹莹和任曼铜 (2024年) 提出了IPOA算法。通过引入反向折射学习机制增强种群随机性和多样性；融合正余弦算法和鹈鹕算法改进猎物搜索方式，增强局部和全局搜索能力；采用Levy飞行机制更新鹈鹕位置；引入自适应t分布变异算子，以迭代次数作为自由度参数增强种群多样性 [1951.mtmt.com.cn (基于混合策略改进的鹈鹕优化算法)].
    *   **关键实验结论**: 在12个标准测试函数测试中，IPOA展现出更好的收敛速度和稳定性。应用于压力容器设计优化问题时，证明了改进算法具有较好的求解性能 [1951.mtmt.com.cn (基于混合策略改进的鹈鹕优化算法)].

#### 3. 约束多目标优化问题 (CMOPs) 算法

CMOPs在工程领域普遍存在，其难点在于需要同时满足复杂约束条件并优化多个相互冲突的目标。

*   **双种群协同进化算法 (Two-population Co-evolutionary Algorithm, TCCMOA)**
    *   **研究问题**: 约束多目标优化问题在复杂可行域下，现有算法在约束满足和目标优化之间存在选择压力矛盾，导致难以搜索到完整的约束前沿或易陷入局部最优 [aas.net.cn (面向复杂可行域约束多目标优化问题的双种群协同进化算法)]。
    *   **核心方法**: 丁炜超等人（2025年）提出了TCCMOA算法。该算法采用双种群协同进化框架，引入粒子群和向量群实现信息共享和优势互补。粒子群使用带辅助档案的粒子群优化器（借助逃逸机制跳出局部最优）实现快速收敛；设计新的$\epsilon$-约束技术动态调整约束松弛因子，使种群在进化初期注重不可行解的遗传信息，跨越不可行区域。向量群使用不考虑约束的参考向量法引导种群进化，保持种群多样性并均匀分布于前沿面 [aas.net.cn (面向复杂可行域约束多目标优化问题的双种群协同进化算法)]。
    *   **关键实验结论**: 在基准测试集及真实世界73个问题上的实验结果表明，TCCMOA在保持种群多样性的同时能快速收敛到约束前沿，超越了对比算法 [aas.net.cn (面向复杂可行域约束多目标优化问题的双种群协同进化算法)]。

### 实验与评价总结

综观2022-2025年间的相关研究，生物启发式元启发算法在解决工程优化问题时，普遍通过以下策略来提升算法性能：

1.  **增强探索与开发平衡**：多数改进算法通过引入混沌映射、Levy飞行、自适应权重因子、多种群或混合搜索策略来平衡全局探索和局部开发，以避免早熟收敛，提高找到全局最优解的能力。
2.  **处理复杂约束的机制**：针对约束优化问题，采用如 $\epsilon$-约束技术、罚函数等机制，使算法在满足约束的同时有效优化目标函数。
3.  **多策略融合**：将不同元启发算法的优势相结合，形成混合算法，或者在单一算法中集成多种改进策略（如混沌初始化、邻域搜索、自适应变异），以克服单一算法的局限性。
4.  **提升种群多样性与信息交流**：通过反向学习机制、种群中心引导、协调学习策略、辅助档案等方法，增加种群的多样性，促进个体间有效信息交流，从而增强算法跳出局部最优的能力和收敛稳定性。
5.  **适用性和鲁棒性**：改进算法在标准基准测试函数（如CEC系列）和实际工程问题（如路径规划、PID参数整定、压力容器设计）上进行广泛验证，以证明其解决复杂问题的能力和对不同问题场景的适应性。

总体而言，研究表明这些改进算法在求解精度、收敛速度和稳定性方面均优于其原始版本或同期其他主流算法。

### 趋势与挑战

2025年前后，生物启发式元启发算法在工程优化领域将继续呈现以下研究趋势：

1.  **通用性框架与理论深化**：鉴于元启发算法数量庞大且缺乏统一性，如GEM算法 [themoonlight.io (A Generalized Evolutionary Metaheuristic (GEM) Algorithm for Engineering Optimization)] 所尝试的，未来研究将更倾向于建立更通用、模块化的算法框架，允许不同搜索机制的灵活组合与切换，并从理论上深入分析这些组合策略的有效性与收敛性。这有助于从“算法动物园”中提炼出普适性原理，指导新算法设计。
2.  **与机器学习/深度学习的融合**：元启发算法与机器学习技术（特别是强化学习、深度学习）的融合将成为重要方向。例如，利用机器学习模型预测优化过程中的有用信息（如最优解区域、参数敏感性），指导元启发算法的搜索方向和参数自适应调整；或者将元启发算法用于优化神经网络结构、超参数或训练过程，形成更强大的混合智能系统。这将有助于解决传统元启发算法在决策复杂、动态变化环境中的局限性。
3.  **面向具体工程领域的定制与高效部署**：随着工业4.0和数字孪生技术的普及，BIMA在实际工程应用中将更加注重定制化和部署效率。这意味着算法不仅要性能优越，还要考虑计算资源、实时性要求、并行处理能力、多目标与多约束的动态处理，以及与现有工程软件和硬件的无缝集成。尤其在航空航天、智能制造、能源管理等关键领域，对BIMA的轻量化、鲁棒性和可解释性将提出更高要求。

### 结论

2022-2025年期间，生物启发式元启发算法在解决工程优化问题上展现出持续的创新活力。研究人员通过引入混沌映射、Levy飞行、多策略融合、种群引导和约束处理机制等多种手段，有效提升了算法的全局搜索能力、局部开发精度及对复杂约束的适应性。未来的研究将进一步探索算法的通用理论框架、与机器学习的深度融合，并致力于提高算法在实际工程场景中的定制化与高效部署能力。

### 参考文献

*   丁炜超, 孙立烨, 罗飞, 顾春华, 董文波. 面向复杂可行域约束多目标优化问题的双种群协同进化算法. 自动化学报, 2025, 51(8): 1−21. [aas.net.cn](https://aas.net.cn/cn/article/doi/10.16383/j.aas.c250023)
*   何永康, 李旭芳. 邻域搜索和改进莱维因子的人工蜂鸟优化算法. 建模与仿真, 2024, 13(2): 987-1003. [image.hanspub.org](https://image.hanspub.org/Html/1-2571228_81778.htm)
*   李大海, 熊文清, 王振东. 一种多策略协同改进的海鸥算法及其应用. 计算机应用研究, 2023, 40(5): 1360-1367,1374. [www.arocmag.cn](https://www.arocmag.cn/abs/2022.09.0469)
*   苏莹莹, 任曼铜. 基于混合策略改进的鹈鹕优化算法. 制造技术与机床, 2024, (3): 146-154. [1951.mtmt.com.cn](https://1951.mtmt.com.cn/article/doi/10.19287/j.mtmt.1005-2402.2024.03.012)
*   王铠铭, 王珠, 周建桥. Engineering experience-based swarm intelligence for generalized PID tuning. 2025 IEEE 14th Data Driven Control and Learning Systems Conference (CAA-A类会议), 2025. [www.cup.edu.cn](https://www.cup.edu.cn/cupai/kxyj/kydt/a8f9f2b9b4c742dc98d4103a3747e96f.htm)
*   袁磊. 基于改进遗传粒子群混合算法的机械臂时间最优轨迹规划. 海南大学学报(自然科学版), 2025, 43(3): 354-361. [hndk.hainanu.edu.cn](https://hndk.hainanu.edu.cn/article/doi/10.15886/j.cnki.hdxbzkb.2024022201)
*   张林, 沈佳颖, 胡传陆, 朱东林. 基于信噪比的学习型哈里斯鹰优化算法. 北京航空航天大学学报, 2025, 51(7): 2360-2373. [www.sciengine.com](https://www.sciengine.com/doi/pdfView/51D19E1CDEC64BA69A61BE2B4D238840)
*   张顺, 刘媛华, 张颢严. 基于改进蜣螂算法的车机协同巡检路径规划方法. 理论数学, 2025, 15(1): 130-142. [pdf.hanspub.org](https://pdf.hanspub.org/pm2025151_161252697.pdf)
*   周刘长. 面向全局优化的种群中心引导型粒子群优化算法. 计算机科学与应用, 2025, 15(5): 173-183. [pdf.hanspub.org](https://pdf.hanspub.org/csa_1543619.pdf)
*   Yang, Xin-She. A Generalized Evolutionary Metaheuristic (GEM) Algorithm for Engineering Optimization. arXiv preprint arXiv:2407.02113, 2024. [themoonlight.io (A Generalized Evolutionary Metaheuristic (GEM) Algorithm for Engineering Optimization)](https://www.themoonlight.io/zh/review/a-generalized-evolutionary-metaheuristic-gem-algorithm-for-engineering-optimization)