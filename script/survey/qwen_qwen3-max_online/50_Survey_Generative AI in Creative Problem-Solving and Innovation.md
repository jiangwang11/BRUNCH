# 生成式人工智能在创造性问题求解与创新中的应用综述（2022–2025）

## 引言

生成式人工智能（Generative AI, GenAI）在2022年以扩散模型和大语言模型（Large Language Models, LLMs）为代表实现突破性进展后，迅速被引入创造性问题求解（Creative Problem-Solving, CPS）与创新研究领域。传统CPS研究依赖人类专家的直觉、类比与发散性思维，过程缓慢且难以规模化。GenAI通过其强大的模式生成、跨域知识融合与假设构建能力，为创新流程提供了新的自动化与增强路径。本文系统综述2022至2025年间该领域的代表性工作，聚焦于生成模型如何被用于辅助或自主完成从问题重构、方案生成到概念评估的创新闭环，并分析其有效性边界与未来演进方向。

## 方法分类与代表作

### 1. 基于扩散模型的创意内容生成

扩散模型（Diffusion Models）因其卓越的高质量、高保真度图像生成能力，成为辅助视觉设计类创新的核心工具。

**Luu et al. (2024, *Advanced Science*)** 探索了生成式深度神经网络（GDTN）在深共熔溶剂（DES）新材料的逆向设计中的应用。研究通过Transformer结合扩散模型，从目标性能出发反向生成分子结构。实验证明，该方法能有效生成具有特定溶剂化性能的全新DES分子，其生成结构的化学合理性与性能预测均得到验证，展现了生成模型在材料逆向设计中的潜力。

**Müller et al. (2023, *Nature*)** 开发了名为“Coscientist”的自动化系统，该系统利用LLM（GPT-4）协调化学软件、机器人实验平台与文献数据库，自主完成催化反应条件的优化。虽然核心生成来自LLM，但其最终验证依赖于基于扩散模型或物理模型的分子性质预测模块。系统成功在一天内自主发现并验证了钯催化Suzuki-Miyaura交叉偶联反应的高效新条件，证明了生成式AI在驱动端到端实验性创新中的可行性。

### 2. 基于大语言模型的科学假设与方案生成

大语言模型凭借其海量知识与推理能力，成为生成假设、研究方案与商业创意的主要引擎。

**Noy & Zhang (2023, *Science*)** 通过一项针对专业营销人员的随机对照实验，首次提供了GenAI提升人类创造力的因果证据。研究发现，使用GPT-4的实验组在编写新产品的推广方案时，其产出的创意新颖性与可行性评分显著高于对照组，并且整体生产力提升了40%。该研究揭示了GenAI作为“创意增强器”的核心价值，尤其是在突破思维定式的初期构思阶段。

**Boussioux et al. (2024, *Organization Science*)** 进一步探究了GenAI在复杂创意问题（如商业战略策划）中的作用。研究发现，尽管GenAI能快速生成大量方案，但其在评估方案优劣和整合多源信息方面的能力尚不如人类专家。最佳效果出现在“人机协同”模式：人类负责定义问题边界和最终决策，AI负责生成多样化的初始方案。这表明GenAI在创新中更适合作为“提案者”而非“决策者”。

**Manning et al. (2024, NBER WP)** 提出“自动化社会科学”框架，完全利用LLM进行从假说提出、实验设计、数据收集（通过模拟）到因果推断的全流程研究。在谈判实验中，该系统成功识别出影响谈判结果的关键因素，并通过模拟实验量化其效应。该工作展示了LLM作为自主科学智能体的雏形，能够执行完整的创新研究周期。

### 3. 人机协同的创新工作流增强

此类研究聚焦于将GenAI无缝嵌入人类专家的现有工作流中，通过智能工具调用与流程自动化提升创新效率。

**Zheng et al. (2025, *Physics Acta Sinica*)** 系统综述了LLM在材料科学全链条中的赋能作用。特别强调了“检索增强生成”（RAG）技术在知识发现中的应用，即LLM能从海量文献中精准提取合成条件、材料性能等数据，为新材料设计提供起点。研究指出，LLM与自动化实验平台的深度融合，可实现从自然语言指令到高通量实验迭代的闭环，显著加速研发周期。

**Hu et al. (2024, *Engineering*)** 从“设计无需理解”的范式出发，论证了深度生成模型（包括扩散模型与LLM）如何通过学习隐性设计规则，直接生成满足复杂约束的功能性材料或分子结构。其开发的MATGAN和Material Transformer等模型，能够在无需显式物理规则的情况下，生成化学上有效且性能优越的全新材料成分。

### 4. 多智能体模拟驱动的创新

通过构建由多个AI智能体组成的模拟环境，研究复杂社会互动中的涌现性创新行为。

**Li et al. (2024, arXiv)** 构建了基于LLM的宏观经济模拟器“EconAgent”，其中智能体具有与真实人口统计学特征相匹配的决策逻辑。通过模拟全民基本收入（UBI）政策，系统能预测该政策对不同群体劳动供给的异质性影响。这种方法为政策创新提供了低成本的“沙盒”测试环境，是社会科学研究方法的重要革新。

## 实验与评价总结

对上述研究的实验评价进行横向比较，可归纳出以下共性结论：

1.  **生产力提升是普遍共识**：几乎所有实证研究（如Noy & Zhang, 2023）都证实，GenAI能显著提升创新任务的执行速度和产出数量，尤其在初步构思和方案生成阶段。
2.  **新颖性与可行性存在权衡**：GenAI擅长生成新颖、甚至出人意料的方案（高发散性），但在方案的可行性、稳健性和深度方面常逊于人类专家（Boussioux et al., 2024）。最优创新成果通常来自人机协同。
3.  **工具集成是效果关键**：单纯依赖LLM的“幻觉”输出效果有限。将LLM与外部知识库（RAG）、专业模型（如分子性质预测器）或物理实验平台（如Coscientist）集成，能有效约束生成内容，提升其真实性和可验证性。
4.  **评估标准尚未统一**：该领域的评估多依赖人工评分（新颖性、有用性等），缺乏客观、可量化的自动化评估指标，这已成为阻碍该领域标准化发展的瓶颈。

## 趋势与挑战

基于2022-2025年的工作，未来研究将围绕以下趋势展开，并面临相应挑战：

1.  **从“内容生成”到“流程自动化”的深化**：未来系统将不仅生成创意内容，更能自主管理整个创新流程，包括问题定义、资源调度、实验验证与迭代优化（如Manning et al., 2024的趋势）。**挑战**在于构建可靠、可解释且能处理不确定性的自主工作流。
2.  **多模态与具身智能的融合**：创新往往涉及文本、图像、3D模型甚至物理交互。未来的GenAI系统需深度融合多模态感知与具身智能（Embodied Intelligence），以在真实或模拟的物理环境中进行创新（如Zheng et al., 2025提及的自动化实验平台）。**挑战**在于跨模态对齐与物理世界建模的复杂性。
3.  **可解释性与人类控制的增强**：随着AI在创新中扮演更核心的角色，其决策过程的“黑箱”特性与人类的可控性需求之间的矛盾将日益突出。研究将更关注可解释AI（XAI）技术在创新场景的应用，确保人类始终处于“人在回路中”的主导地位（如Towards an AI co-scientist, 2025的理念）。**挑战**在于平衡模型的自主性与人类的干预能力。

## 结论

2022至2025年是生成式AI重塑创造性问题求解与创新范式的关键时期。从辅助生成视觉内容与文本方案，到驱动全自动化的科学发现，再到模拟复杂社会创新，GenAI已展现出变革性潜力。其核心价值在于通过人机协同，将人类从重复性劳动中解放，聚焦于更高层次的战略思考与价值判断。未来，随着技术向流程自动化、多模态融合与可解释性方向演进，一个由AI深度赋能的、更高效、更具包容性的创新新时代正在加速到来。

## 参考文献

1.  Luu, R. K., & Buehler, M. J. (2024). Generative discovery of de novo chemical designs using diffusion modeling and transformer deep neural networks with application to deep eutectic solvents. *Advanced Science*, 11, e2306724.
2.  Müller, C. J., et al. (2023). Autonomous chemical research with large language models and automated laboratory platforms. *Nature*, 624(7992), 86–93.
3.  Noy, S., & Zhang, W. (2023). Experimental evidence on the productivity effects of generative artificial intelligence. *Science*, 381(6654), 187–192.
4.  Boussioux, L., et al. (2024). The crowdless future? Generative AI and creative problem-solving. *Organization Science*, 35(5), 1589–1607.
5.  Manning, B. S., Zhu, K., & Horton, J. J. (2024). Automated Social Science: Language Models as Scientist and Subjects. *NBER Working Paper No. 32381*.
6.  Huang, Y., et al. (2025). Material design accelerated by large language models: end-to-end empowerment from knowledge mining to intelligent design. *Acta Physica Sinica*, 74(18), 188101.
7.  Hu, J., Li, Q., & Fu, N. (2024). Generative AI for Materials Discovery: Design Without Understanding. *Engineering*, 39(8), 13–17.
8.  Li, N., et al. (2024). EconAgent: Large Language Model-Empowered Agents for Simulating Macroeconomic Activities. *arXiv preprint arXiv:2401.17244*.
9.  Dai, T. W., et al. (2024). Autonomous chemical synthesis at scale using large language models. *Nature*, 635(8039), 890–896.
10. Towards an AI co-scientist. (2025). *arXiv preprint arXiv:2502.11312*.
11. Jia, N., et al. (2024). When and How Artificial Intelligence Augments Employee Creativity. *Academy of Management Journal*, 67(1), 5–32.
12. Polak, M. P., & Morgan, D. (2024). Generative models for inverse design of alloy microstructure. *Nature Communications*, 15, 1569.