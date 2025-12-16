# 引言  
随着深度学习模型在医疗、金融、安防等高风险领域的广泛应用，其“黑箱”特性引发了对决策透明度和可解释性的迫切需求 ([arxiv.org](https://arxiv.org/abs/2505.14510#:~:text=introduce%20BACON%2C%20a%20novel%20framework,verifiable%20decision%20logic)) ([www.sciencedirect.com](https://www.sciencedirect.com/science/article/pii/S1566253523001148#:~:text=Artificial%20intelligence%20,in%20AI%20models%20has%20arisen))。可解释人工智能（XAI）旨在揭开模型决策过程，提升用户信任和专家监管能力。已有综述从不同视角划分XAI技术，如数据可解释性、模型可解释性、后验可解释性和解释评估等范畴 ([www.sciencedirect.com](https://www.sciencedirect.com/science/article/pii/S1566253523001148#:~:text=common%20definitions%2C%20and%20summarizing%20recently,conducted%20by%20looking%20at%20410))。本文聚焦2022–2025年代表性工作，按方法类型归纳分析模型解释与决策透明度方面的进展。

## 方法分类与代表作  

### 特征归因方法  
**DIME** ([arxiv.org](https://arxiv.org/abs/2203.02013#:~:text=model%20disentanglement%20into%20unimodal%20contributions,model%20behavior%2C%20and%20presents%20a))面向多模态模型解释，其核心思想是将模型的决策拆解为各模态（如图像、文本等）的单独贡献和多模态交互，然后为每个模态生成细粒度归因。实验表明，DIME能够在合成与真实任务中产生准确的、可解耦的解释，帮助用户更深入地理解模型行为 ([arxiv.org](https://arxiv.org/abs/2203.02013#:~:text=model%20disentanglement%20into%20unimodal%20contributions,model%20behavior%2C%20and%20presents%20a))。  
**T-Explainer** ([arxiv.org](https://arxiv.org/abs/2404.16495#:~:text=result%20from%20similar%20or%20even,into%20a%20comprehensive%20XAI%20framework))提出了一种基于泰勒展开的局部可加归因解释器，通过保证局部准确性和一致性来提高归因稳定性。作者在多个基准数据集上对比测试了T-Explainer与传统归因方法的性能，结果显示其能够在解释质量与重复性方面优于现有方法 ([arxiv.org](https://arxiv.org/abs/2404.16495#:~:text=result%20from%20similar%20or%20even,into%20a%20comprehensive%20XAI%20framework))。该方法还附带了一整套评估和可视化工具，使其成为一个完善的模型无关的XAI框架。

### 规则与局部解释方法  
**DeltaXplainer** ([arxiv.org](https://arxiv.org/abs/2309.17095#:~:text=Explainable%20AI%20,world%20datasets))关注模型之间的差异解释问题。针对两个二分类器的比较，提出了一种模型无关的基于规则的解释方法，可自动挖掘两个模型预测差异背后的决策规则。作者在合成数据和真实数据（含不同类型概念漂移）上进行实验，验证了DeltaXplainer在捕获模型行为差异上的有效性 ([arxiv.org](https://arxiv.org/abs/2309.17095#:~:text=Explainable%20AI%20,world%20datasets))。  

### 对比与反事实解释  
**TIME** ([arxiv.org](https://arxiv.org/abs/2309.07944#:~:text=target%20classifier,box%20setting))利用文本-图像生成模型产生反事实示例，专门为图像分类器提供对比性解释。该方法通过Stable Diffusion注入“环境偏置”和“类别偏置”引导生成，将原始图像的关键特征最小化地修改以改变模型预测。实验表明，在仅获取原始图片和预测结果的黑箱设置下，TIME生成的反事实图片能够有效揭示导致预测变化的特征，解释效果与有信息量的方法相当 ([arxiv.org](https://arxiv.org/abs/2309.07944#:~:text=target%20classifier,box%20setting))。  
**s(CASP)** ([arxiv.org](https://arxiv.org/abs/2310.14497#:~:text=paper%20focuses%20on%20the%20latter,We))引入了基于约束答案集编程（ASP）和s(CASP)系统的反事实解释框架。该工作针对贷款审批等高风险决策场景，自动寻找使模型输出改变的最小输入约束，并以形式化证明树的形式提供反事实说明。通过在多个“可能世界”中搜索假设，s(CASP)方法为每个反事实提供了可溯源的逻辑证明，有助于分析模型的因果可解释性 ([arxiv.org](https://arxiv.org/abs/2310.14497#:~:text=paper%20focuses%20on%20the%20latter,We))。

### 可解释模型设计  
**BACON** ([arxiv.org](https://arxiv.org/abs/2505.14510#:~:text=introduce%20BACON%2C%20a%20novel%20framework,verifiable%20decision%20logic))提出了一种端到端可解释的决策模型框架，采用分级逻辑实现决策推理。该系统在维持高预测准确性的同时，提供了完全可视的决策结构和精确的逻辑符号解释。作者在经典布尔近似、鸢尾花分类、购房决策和乳腺癌诊断任务上训练BACON模型，每个案例均得到高性能且输出紧凑且人可验证的决策逻辑表述 ([arxiv.org](https://arxiv.org/abs/2505.14510#:~:text=introduce%20BACON%2C%20a%20novel%20framework,verifiable%20decision%20logic))，显示了该方法在可解释AI中的实用潜力。  
**神经原型树（NPT）** ([pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/39636692#:~:text=interpretability%20,001))将卷积神经网络与基于“原型”的决策树结合，用于医疗图像分类的可解释性研究。该模型在深度特征空间内学习代表性“原型”图像斑块，并基于它们构建决策路径。实验结果表明，随着模型解释复杂度的提高，NPT的分类性能显著提升；然而，可解释性的提升也伴随着公平性指标的降低 ([pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/39636692#:~:text=interpretability%20,001))。这一工作揭示了性能、可解释性与公平性之间的权衡，为设计实用的可解释深度模型提供了经验参考。

### 概念驱动解释方法  
**SurroCBM** ([arxiv.org](https://arxiv.org/abs/2310.07698#:~:text=Concept%20Bottleneck%20Surrogate%20Models%20,the%20field%20of%20explainable%20AI))提出了一种概念瓶颈替代模型，用于自动发现解释黑箱模型的概念表示。该框架无需人工概念标注，自动挖掘各黑箱模型间的共性与差异概念，并训练一个可解释的替代模型来提供后验解释。作者设计了基于自生成数据的迭代训练策略，在图像分类等任务上通过大量实验验证了SurroCBM在概念发现和解释方面的有效性 ([arxiv.org](https://arxiv.org/abs/2310.07698#:~:text=Concept%20Bottleneck%20Surrogate%20Models%20,the%20field%20of%20explainable%20AI))。  
**BotCL** ([arxiv.org](https://arxiv.org/abs/2304.10131#:~:text=relationship%20between%20some%20concepts%20and,com))（Bottleneck Concept Learner）是另一种概念瓶颈方法，旨在用高层次概念重构神经网络。BotCL将输入图像仅表示为语义概念的有无，通过自监督和专门的正则化使学习到的概念具有可人类理解的语义。在若干图像分类任务上，实验结果证明了BotCL能够以有限的概念集重建网络决策流程，从而使模型行为更易于解释 ([arxiv.org](https://arxiv.org/abs/2304.10131#:~:text=relationship%20between%20some%20concepts%20and,com))。

## 实验与评价总结  
上述工作在多种数据集和任务上进行了广泛测试，共同揭示了XAI方法的现状。总体来看，许多方法在合成和实际场景中均能提供直观的解释，并能够按照预期突出影响预测的关键因素 ([arxiv.org](https://arxiv.org/abs/2203.02013#:~:text=model%20disentanglement%20into%20unimodal%20contributions,model%20behavior%2C%20and%20presents%20a)) ([arxiv.org](https://arxiv.org/abs/2309.07944#:~:text=target%20classifier,box%20setting))。同时，这些实验也暴露出解释可靠性问题：例如Šimić等人 ([www.nature.com](https://www.nature.com/articles/s41598-025-09538-2#:~:text=which%20revealed%20flaws%20in%20the,provide%20guidelines%20for%20future%20AM))表明，传统扰动验证指标在时序数据上存在缺陷，并提出了新的指标（CMI）和更健壮的验证流程以评估特征归因的忠实度。这类研究还强调，对完整性评估多样、解释目标不同的方法难以统一比较；而且如神经原型树所示，可解释性增强往往会带来性能-公平性的权衡 ([pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/39636692#:~:text=interpretability%20,001))。因此，当前XAI研究趋势是结合定量评估指标和用户研究，综合考量解释准确性、可理解性与应用场景需求。

## 趋势与挑战  
面向未来，XAI研究将呈现多条重点发展趋势：  
- **大模型与多模态解释**：随着大型预训练模型（如大规模语言模型和多模态模型）的兴起，对其内部机制的解释需求激增。如何针对这类模型设计高效的全局和局部解释方法将是重点。  
- **因果与交互式解释**：仅静态特征归因已无法满足可操作性要求，更多研究将结合因果推断生成具有行动指导意义的对比/反事实解释，并引入用户反馈进行解释迭代与定制。  
- **统一评估与标准化**：将探索更统一的评估基准和指标，以解决当前解释方法难以量化比较的问题。伴随法规（如欧盟“AI法案”）的推动，解释质量和可靠性将得到更多关注并纳入认证标准。  
- **公平性与可靠性**：如何在提高解释透明度的同时兼顾模型公平与鲁棒，是未来亟待解决的挑战。跨学科研究将加强对XAI输出进行心理学和社会学评估的方法开发，确保解释结果真正符合人类需求。

## 结论  
近期XAI领域在可解释模型设计、后验解释算法和自动化概念发现等方面取得了丰富成果，但也面临评估标准不统一、解释与性能/公平冲突等挑战。未来工作需要更加注重解释的可验证性和用户适用性，发展可交互、可定制的解释系统，并将可靠性评估融入消费者和监管者视角，以推动XAI在实际高风险场景中的可信部署。

## 参考文献  
- Bai, H., Dujmovic, J., Wang, J. (2025). *BACON: A fully explainable AI model with graded logic for decision making problems*. [arXiv:2505.14510](https://arxiv.org/abs/2505.14510). ([arxiv.org](https://arxiv.org/abs/2505.14510#:~:text=introduce%20BACON%2C%20a%20novel%20framework,verifiable%20decision%20logic))  
- Ortigossa, E. S. et al. (2024). *T-Explainer: A Model-Agnostic Explainability Framework Based on Gradients*. [arXiv:2404.16495](https://arxiv.org/abs/2404.16495). ([arxiv.org](https://arxiv.org/abs/2404.16495#:~:text=result%20from%20similar%20or%20even,into%20a%20comprehensive%20XAI%20framework))  
- Rida, A. et al. (2023). *Dynamic Interpretability for Model Comparison via Decision Rules*. [arXiv:2309.17095](https://arxiv.org/abs/2309.17095). ([arxiv.org](https://arxiv.org/abs/2309.17095#:~:text=Explainable%20AI%20,world%20datasets))  
- Dasgupta, S. et al. (2023). *Counterfactual Explanation Generation with s(CASP)*. [arXiv:2310.14497](https://arxiv.org/abs/2310.14497). ([arxiv.org](https://arxiv.org/abs/2310.14497#:~:text=paper%20focuses%20on%20the%20latter,We))  
- Jeanneret, G. et al. (2023). *Text-to-Image Models for Counterfactual Explanations: a Black-Box Approach*. [arXiv:2309.07944](https://arxiv.org/abs/2309.07944). ([arxiv.org](https://arxiv.org/abs/2309.07944#:~:text=target%20classifier,box%20setting))  
- Pan, B. et al. (2023). *SurroCBM: Concept Bottleneck Surrogate Models for Generative Post-hoc Explanation*. [arXiv:2310.07698](https://arxiv.org/abs/2310.07698). ([arxiv.org](https://arxiv.org/abs/2310.07698#:~:text=Concept%20Bottleneck%20Surrogate%20Models%20,the%20field%20of%20explainable%20AI))  
- Wang, B. et al. (2023). *Learning Bottleneck Concepts in Image Classification*. [arXiv:2304.10131](https://arxiv.org/abs/2304.10131). ([arxiv.org](https://arxiv.org/abs/2304.10131#:~:text=relationship%20between%20some%20concepts%20and,com))  
- Chen, H. et al. (2024). *Intersection of Performance, Interpretability, and Fairness in Neural Prototype Tree for Chest X-Ray Pathology Detection: Algorithm Development and Validation Study*. *JMIR Form. Res.*, 8:e42741. ([pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/39636692#:~:text=interpretability%20,001))  
- Šimić, I., Veas, E., Sabol, V. (2025). *A comprehensive analysis of perturbation methods in explainable AI feature attribution validation for neural time series classifiers*. *Sci. Rep.* 15:26607. ([www.nature.com](https://www.nature.com/articles/s41598-025-09538-2#:~:text=which%20revealed%20flaws%20in%20the,provide%20guidelines%20for%20future%20AM))  
- Lyu, Y. et al. (2022). *DIME: Fine-grained Interpretations of Multimodal Models via Disentangled Local Explanations*. [arXiv:2203.02013](https://arxiv.org/abs/2203.02013). ([arxiv.org](https://arxiv.org/abs/2203.02013#:~:text=model%20disentanglement%20into%20unimodal%20contributions,model%20behavior%2C%20and%20presents%20a))  
- Patidar, N. et al. (2024). *Transparency in AI Decision Making: A Survey of Explainable AI Methods and Applications*. *Adv. Robot. Technol.*, 2(1):22–31. ([papers.ssrn.com](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4766176#:~:text=Transparency%20in%20AI%20Decision%20Making%3A,Explainable%20AI%20Methods%20and%20Applications))