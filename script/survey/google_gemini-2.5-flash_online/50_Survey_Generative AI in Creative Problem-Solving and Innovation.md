## 生成式人工智能在创新性问题解决中的应用与发展综述 (2022–2025)

### 引言
近年来，以大型语言模型（LLMs）为代表的生成式人工智能（Generative AI, GenAI）技术飞速发展，其在理解、生成和处理多模态信息方面的强大能力，正逐步改变各行各业的生产范式，尤其在创意问题解决与创新领域展现出前所未有的潜力。GenAI已从传统的“知识工程”时代（2020-2023）迈向“认知工程”时代（2024年至今），模型开始具备深度思考和持续复杂推理能力，从知识管理工具演变为认知管理工具 [cccf.hrbeu.edu.cn](https://cccf.hrbeu.edu.cn/article/doi/10.11991/cccf.202511004)。本综述旨在系统梳理2022年至2025年间生成式AI在创意问题解决与创新中的代表性工作，涵盖其在研究构想、设计、内容生成及人机协作等方面的应用，并总结现有实验评价的共性结论，最终对未来发展趋势提出预测。

### 方法分类与代表作

本部分将GenAI在创意问题解决与创新方面的应用划分为四个主要类别：研究构想与假设生成、创意内容生成、人机协作模式优化以及材料与药物设计加速。

#### 1. 研究构想与假设生成
GenAI通过其强大的语义理解和生成能力，在学术研究的早期阶段辅助研究人员进行头脑风暴、提出研究问题和生成假设。

*   **[gaiforresearch.com](https://gaiforresearch.com/zh/post/%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD%E8%BE%85%E5%8A%A9%E5%AD%A6%E6%9C%AF%E7%A0%94%E7%A9%B6%E7%9A%84%E6%AD%A3%E5%8F%8D%E4%B8%A4%E9%9D%A2%EF%BC%9A%E4%BB%8E%E8%BF%BD%E6%B1%82%E6%95%88%E7%8E%87%E5%88%B0%E4%B8%A5%E8%B0%A8%E6%B1%82%E7%9C%9F)** **LLMs在研究构想中的作用** (Van Quaquebeke et al., 2025): 该研究探讨了GenAI如何重塑研究构想阶段，指出LLMs能够辅助研究者进行头脑风暴和生成研究问题，甚至检索被忽视的交叉领域主题。研究证实，AI生成的想法在新颖性评估中可超越人类专家的构想。其核心方法是利用LLMs的生成能力进行创意启发，并通过“反驳式提示”（counter-prompting）与AI互动以突破固有思维。然而，研究也警示了AI可能导致“算法单一文化”和“锚定效应”，限制专家创造力。
*   **[zhuanzhi.ai](https://www.zhuanzhi.ai/vip/f15b0fa5f13d42ba34af44aced1a81fa)** **知识整合与假设生成** (Zhou et al., 2025): 这篇综述将AI辅助科研划分为假设提出、假设验证和成果发布三个阶段。在假设提出阶段，AI通过知识整合辅助研究者获取和理解现有文献，并在此基础上生成新的研究假设。核心方法包括语义匹配的推荐系统和多智能体系统迭代优化大纲以生成文献综述，以及通过优化输入数据和输出评估提升假设的科学性和创新性。研究强调了AI在处理信息过载方面的优势，但指出其在生成具有颠覆性的理论方面仍有局限性。
*   **[nsd.pku.edu.cn](https://nsd.pku.edu.cn/docs/20251013163525261099.pdf)** **大模型作为科学家的“参谋”角色** (Hu & Yi, 2025): 该文将大语言模型在经济管理研究中的应用定义为“参谋”、“助研”、“智能体”和“朋友”四种角色。作为“参谋”，LLMs辅助研究者澄清研究思路，进行信息资料收集，并提供研究反馈。核心方法是利用LLMs的生成和理解能力，通过对话互动，帮助研究者探索研究主题、明确问题与假设，并进行批判性思考。研究指出，AI在提出开放性问题、生成简明理论框架和发现混淆因素方面表现出色，但其价值高度依赖于研究者的引导。

#### 2. 创意内容生成
GenAI不仅能启发构想，还能直接参与生成各种创意内容，尤其在视觉和文本领域。

*   **[2048.csdn.net](https://2048.csdn.net/6801ff30c89bb16498818fc1.html)** **生成式思维链 (GoT) 在视觉生成与编辑中的推理能力释放** (Fang et al., 2025): 该研究提出了GoT范式，通过显式的语言推理过程指导图像生成与编辑，而非直接映射文本提示。其核心方法是构建大规模GoT数据集，包含语义-空间推理链，并结合Qwen2.5-VL与经过语义-空间引导模块增强的扩散模型。实验结果表明，GoT框架在生成和编辑任务上取得了显著性能提升，并支持交互式视觉生成，生成图像更符合人类意图。
*   **[wulixb.iphy.ac.cn](https://wulixb.iphy.ac.cn/cn/article/doi/10.7498/aps.74.20250497)** **大语言模型加速材料设计** (Huang et al., 2025): 该综述系统性阐述了LLMs在材料科学全链条中的创新应用，包括知识发现、材料设计、结构与性质预测以及逆向设计。核心方法是利用LLMs高效的信息检索和数据提取能力，通过跨尺度知识融合与智能推理发现数据间的潜在关联，加速材料研发流程。研究表明，LLMs在知识挖掘方面将信息检索准确率提高了29.4%，显著提升了材料科研效率。

#### 3. 人机协作模式优化
GenAI的引入改变了传统的工作模式，促进了人机之间的新型协作关系。

*   **[gaiforresearch.com](https://gaiforresearch.com/zh/post/%E5%92%8C-ai-%E6%90%AD%E6%A1%A3%E5%88%9B%E4%BD%9C%EF%BC%9F%E5%A4%A7%E5%9E%8B%E8%AF%AD%E8%A8%80%E6%A8%A1%E5%9E%8B%EF%BC%88llms%EF%BC%89%E5%A6%82%E4%BD%95%E6%94%B9%E5%8F%98%E5%88%9B%E6%84%8F%E6%B8%B8%E6%88%8F%E8%A7%84%E5%88%99%EF%BC%9F)** **LLMs在创意工作中的协作模式与用户专业知识的作用** (Chen & Chan, 2024): 该研究通过广告文案创作的实验，考察了LLM作为“代笔人”和“意见征询者”两种协作模式的效果。结果发现，LLM作为“意见征询者”能有效弥合非专家与专家之间的创意质量差距。然而，作为“代笔人”时可能引发“锚定效应”，反而对专家表现产生不利影响。研究强调了根据用户专业知识选择合适LLM协作模式的重要性。
*   **[nsd.pku.edu.cn](https://nsd.pku.edu.cn/docs/20251013163525261099.pdf)** **大模型作为助研与智能体** (Hu & Yi, 2025): 这项工作进一步探索了LLMs作为研究助手的角色，包括完成重复性工作（如参考文献格式调整、代码编写）和作为智能体进行行为模拟。大模型通过自然语言生成能力自动化繁琐任务，并能在给定情境下模拟个体行为，例如在经济学中进行政策模拟。研究指出，AI在编程语言（如Python）和数理推导方面展现出较强能力，且在宏观经济模拟和博弈情境中表现出模拟人类决策行为的潜力，为社会科学研究提供了新的工具。

#### 4. 检索增强生成 (RAG) 在信息获取与推理中的应用
RAG技术显著提升了LLMs在知识密集型任务中的事实性和时效性，通过结合外部知识库来增强生成过程。

*   **[ywlxbx.whuznhmedj.com](https://ywlxbx.whuznhmedj.com/journal/481.html)** **RAG技术在医学人工智能中的应用** (Jin et al., 2025): 该文系统阐述了RAG技术如何解决LLMs在医学领域面临的“幻觉”和知识过时问题，并通过连接外部文献数据库和知识图谱，在生成阶段引入可验证的证据和实时知识。核心方法是在生成前先检索，生成中融入检索内容，显著提高了回答的可信度与可溯源性。研究指出，RAG在临床决策支持、新药研发、药物警戒和罕见病诊疗等方面具有广泛应用，通过提供高准确度、可追溯的信息，提升了医疗AI的安全性与可靠性。
*   **[cccf.hrbeu.edu.cn](https://cccf.hrbeu.edu.cn/article/doi/10.11991/cccf.202511004)** **认知工程：生成式人工智能的第二幕** (Liu & Lu, 2025): 该研究指出，生成式AI正从“知识工程”迈向“认知工程”，其关键突破在于AI具备深度思考和持续复杂推理能力。RAG是实现这一转变的重要技术之一，通过提供更好、推理更密集的数据，以及结合预训练与强化学习的协同设计，使模型能进行包含反思、纠错和回溯的完整决策过程学习，从而将大模型提升为认知管理工具。

### 实验与评价总结
综合上述研究，可以得出以下共性结论：

1.  **创意生成能力增强**：GenAI，特别是LLMs，在文本（如广告文案、研究问题、论文摘要）和视觉内容（如图像生成与编辑）的生成方面展现出显著能力。其生成的创意在新颖性评估中甚至能超越人类专家，尤其在处理复杂语义和空间布局时，通过引入推理链（如GoT）可使输出更符合人类意图。
2.  **知识整合与检索效率提升**：GenAI在处理和整合海量异构数据方面具有强大优势，能够辅助研究者快速梳理文献、识别研究空白、提取事实信息，并加速材料与药物设计中的知识发现。RAG技术的应用显著降低了LLMs的“幻觉”风险，并通过实时检索和引用外部知识，提高了信息输出的权威性、准确性与可溯源性，尤其在知识密集型的医学和科学领域价值突出。
3.  **人机协作模式多样化**：GenAI支持多种人机协作模式，包括作为“参谋”提供思想启发、“助研”处理重复性任务（如格式调整、代码编写）、甚至作为“智能体”模拟行为进行社会实验。实验表明，AI作为“意见征询者”对非专家有明显提升作用，但作为“代笔人”时可能引发“锚定效应”，显示出人机协同的复杂性以及对人类干预和引导的依赖。
4.  **技术水平分化与局限**：GenAI在不同领域的应用效果存在差异。在Python等主流编程语言中的代码生成能力较强，但在小众语言如Stata中表现相对较弱。对于复杂数学推导和高级结构化模型（如BLP模型），仍然存在“数学幻觉”问题，需要研究者具备清晰的领域知识进行拆解和验证。此外，GenAI在生成长篇复杂、需要跨文档整合语义信息的内容时，仍存在碎片化和一致性问题，且对多模态与时序信息的处理尚有不足。
5.  **对齐与规范化需求**：模型输出的质量和行为受到预训练语料和后训练阶段的显著影响，特别是在“指令遵从”和“人类偏好对齐”方面。有效利用提示工程（Prompt Engineering），包括清晰的指令、角色设定和少量示例，是提升模型输出质量的关键。对齐过程也可能引入模型自身的偏好，如政治态度上的“左倾”特征，需在使用中加以考量。

### 趋势与挑战
2025年及以后，GenAI在创意问题解决与创新领域将呈现以下趋势并面临相应挑战：

1.  **多模态深度融合突破认知瓶颈**：未来的GenAI将不再局限于单一模态或简单的多模态组合，而是实现图像、文本、语音、视频、结构化数据乃至具身智能的深度融合 [hub.baai.ac.cn](https://hub.baai.ac.cn/view/46618)。这将使模型能够更全面地理解复杂创意任务的上下文，并支持更复杂的跨模态推理。例如，医疗诊断将结合影像、基因组测序与文本信息，形成更完备的辅助诊断体系。挑战在于如何有效处理多模态数据间的语义鸿沟、保证跨模态信息整合的一致性与准确性，并进一步提升模型在复杂、长链条推理任务中的深度思考能力，实现从“知识管理”到“认知管理”的全面跃迁。
2.  **交互式智能与用户中心设计**：GenAI系统将更强调用户参与和交互式的创新过程。通过可解释的AI设计，用户能够更清晰地理解AI的生成逻辑和决策过程，并能更灵活地修改AI的推理步骤以精确调整输出，实现“交互式视觉生成” [2048.csdn.net](https://2048.csdn.net/6801ff30c89bb16498818fc1.html)。这将有助于解决专家在AI“代笔人”模式下可能遇到的“锚定效应”，提升人类专家的创意产出。AI的自我反思和纠错能力将进一步增强，并通过“旅程学习”机制而非“捷径学习”，促进模型学习完整的决策过程，从而优化人机协作效率。
3.  **专业化与个性化模型的崛起**：通用GenAI模型的“天花板效应”将促使专业化LLMs的发展。针对特定领域（如材料科学、医学）进行深度训练的模型，将更能提供传统通用模型难以企及的视角和知识 [wulixb.iphy.ac.cn](https://wulixb.iphy.ac.cn/cn/article/doi/10.7498/aps.74.20250497)。同时，考虑到个人偏好、文化背景和专业经验的差异，未来的GenAI将进一步支持个性化定制，例如通过少量用户数据进行微调以适配特定用户的创作风格或研究习惯。这将对数据隐私和模型伦理治理提出更高要求，如何在个性化与通用性之间取得平衡，并确保模型在专业领域的鲁棒性、可信度和合规性，是核心挑战。

### 结论
生成式人工智能在人类创意问题解决与创新领域展现出革命性的影响力。从辅助研究构想、生成多模态创意内容，到优化人机协作模式、增强信息检索能力，GenAI正逐步改变知识生产的范式。尽管面临“幻觉”、数据偏见、伦理风险等挑战，但通过多模态深度融合、交互式设计以及专业化与个性化发展，GenAI有望在未来成为人类不可或缺的认知智能伙伴，推动社会科学和工程技术研究进入人机协作的新时代。

### 参考文献

*   [cccf.hrbeu.edu.cn](https://cccf.hrbeu.edu.cn/article/doi/10.11991/cccf.202511004) Liu, P., & Lu, P. (2025). Cognition Engineering: The Second Act of Generative Artificial Intelligence. *Journal of Computer Applications*, *45*(11), 10.11991/cccf.202511004.
*   [gaiforresearch.com](https://gaiforresearch.com/zh/post/%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD%E8%BE%85%E5%8A%A9%E5%AD%A6%E6%9C%AF%E7%A0%94%E7%A9%B6%E7%9A%84%E6%AD%A3%E5%8F%8D%E4%B8%A4%E9%9D%A2%EF%BC%9A%E4%BB%8E%E8%BF%BD%E6%B1%82%E6%95%88%E7%8E%87%E5%88%B0%E4%B8%A5%E8%B0%A8%E6%B1%82%E7%9C%9F) Van Quaquebeke, N., Tonidandel, S., & Banks, G. C. (2025). Beyond efficiency: How artificial intelligence (AI) will reshape scientific inquiry and the publication process. *The Leadership Quarterly*, *36*, 101895.
*   [zhuanzhi.ai](https://www.zhuanzhi.ai/vip/f15b0fa5f13d42ba34af44aced1a81fa) Zhou, Z., Feng, X. (2025). From Hypothesis to Publication: A Comprehensive Survey of AI-Driven Research Support Systems. arXiv preprint arXiv:2503.01424.
*   [nsd.pku.edu.cn](https://nsd.pku.edu.cn/docs/20251013163525261099.pdf) Hu, S., & Yi, J. (2025). The Light of Intelligence: A New Era of Economic Management Research in Human-Machine Collaboration. *Peking University National School of Development Working Paper*.
*   [2048.csdn.net](https://2048.csdn.net/6801ff30c89bb16498818fc1.html) Fang, R., et al. (2025). GoT: Unleashing Multimodal Large Language Models' Reasoning Capabilities in Visual Generation and Editing. arXiv preprint arXiv:2503.10639.
*   [wulixb.iphy.ac.cn](https://wulixb.iphy.ac.cn/cn/article/doi/10.7498/aps.74.20250497) Huang, Y., et al. (2025). Material design accelerated by large language models: end-to-end empowerment from knowledge mining to intelligent design. *Acta Phys. Sin.*, *74*(18), 188101.
*   [gaiforresearch.com](https://gaiforresearch.com/zh/post/%E5%92%8C-ai-%E6%90%AD%E6%A1%A3%E6%B0%91%E5%88%9B%E4%BD%9C%EF%BC%9F%E5%A4%A7%E5%9E%8B%E8%AF%AD%E8%A8%80%E6%A8%A1%E5%9E%8B%EF%BC%88llms%EF%BC%89%E5%A6%82%E4%BD%95%E6%94%B9%E5%8F%98%E5%88%9B%E6%84%8F%E6%B8%B8%E6%88%8F%E8%A7%84%E5%88%99%EF%BC%9F) Chen, Z., & Chan, J. (2024). Large Language Model in Creative Work: The Role of Collaboration Modality and User Expertise. *Management Science*, *70*(12), 9101–9117.
*   [ywlxbx.whuznhmedj.com](https://ywlxbx.whuznhmedj.com/journal/481.html) Jin, Z., et al. (2025). Application and frontier exploration of retrieval-augmented generation technology in medical artificial intelligence. *Journal of Drug Epidemiology*, *34*(8), 962-971.
*   [hub.baai.ac.cn](https://hub.baai.ac.cn/view/46618) Xue, L., & Jiang, L. (2025). Generative AI Drives Paradigm Shift in Future Industrial Innovation. *Bulletin of the Chinese Academy of Sciences*, *40*(5), 820-827.
*   [smartblogchen.wordpress.com](https://smartblogchen.wordpress.com/2025/07/28/looking-inward-language-models-can-learn-about-themselves-by-introspection%E5%90%91%E5%86%85%E7%9C%8B%EF%BC%9A%E8%AF%AD%E8%A8%80%E6%A8%A1%E5%9E%8B%E5%8F%AF%E4%BB%A5%E9%80%9A%E8%BF%87%E8%87%AA/) UC San Diego, Stanford University, Truthful AI. (2025). Looking Inward: Language Models Can Learn About Themselves by Introspection. arXiv preprint arXiv:2410.13787.
*   [smartblogchen.wordpress.com](https://smartblogchen.wordpress.com/2024/07/25/promises-and-challenges-of-human-computational-ethology-%E6%96%87%E7%AB%A0%E8%A7%A3%E8%AF%BB/) London University, Caltech, Columbia University, DeepMind. (2024). Promises and challenges of human computational ethology. *Nature Neuroscience*, *27*, 1867-1877.
*   [smartblogchen.wordpress.com](https://smartblogchen.wordpress.com/2024/07/23/computational-neuroethology-a-call-to-action-%E6%96%87%E7%AB%A0%E8%A7%A3%E8%AF%BB/) California Institute of Technology, Howard Hughes, Harvard Medical School, Princeton University. (2024). Computational Neuroethology: A Call to Action. *Neuron*, *112*(16), 2530-2545.