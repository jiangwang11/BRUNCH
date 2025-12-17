# Explainable Artificial Intelligence in Model Interpretation and Decision Transparency: A Comprehensive Review of 2022–2025 Research

**Summary of Key Findings**

The period from 2022 to 2025 has witnessed a fundamental transformation in how researchers approach explainability within machine learning systems, shifting from isolated post-hoc explanation methods toward integrated, multi-stakeholder frameworks that balance interpretability with computational efficiency while addressing domain-specific deployment challenges. This review identifies three major methodological trends: (1) the consolidation of gradient-based and perturbation-based attribution methods into unified evaluation frameworks with improved faithfulness metrics; (2) the emergence of mechanistic interpretability as a complementary discipline to traditional XAI, focusing on reverse-engineering neural network computations; and (3) the development of human-centered evaluation protocols that acknowledge the gap between technical explainability and practical utility for diverse stakeholders. The research landscape demonstrates that contemporary XAI is increasingly pragmatic—prioritizing context-aware explanation over universal comprehensiveness, and recognizing that no single method suffices for heterogeneous user needs across finance, healthcare, autonomous systems, and policy domains.

## Attribution-Based Methods and Unified Evaluation Frameworks

Attribution-based methods have emerged as the dominant paradigm for local explanability in contemporary XAI research. These techniques quantify feature importance by measuring how different input components contribute to model predictions, and the period 2022-2025 has seen significant advances in both their theoretical grounding and practical validation. The foundational contribution remains SHAP (SHapley Additive exPlanations), which computes feature contributions using Shapley values from cooperative game theory[9][42]. SHAP provides both local and global explanations by conceptualizing features as players in a coalition where each receives a fair share of the predictive "payout" based on marginal contributions across all possible feature combinations[9]. A practical guide from 2025 demonstrates that SHAP analysis can be seamlessly integrated into supervised machine learning workflows, with particular utility in drug development and biomedical applications where understanding individual predictions is as critical as aggregate accuracy[42]. The method's advantage over alternatives like LIME lies in its theoretical consistency—SHAP guarantees a fair distribution of predictive contribution, whereas LIME's local linear approximation may miss nonlinear feature interactions[9].

LIME (Local Interpretable Model-agnostic Explanations) remains widely deployed for its computational efficiency and model-agnostic nature[3][5][6]. The technique operates by perturbing input instances to generate synthetic datasets, fitting interpretable surrogate models to approximate black-box decisions in local neighborhoods, and extracting feature weights that indicate importance[3]. Recent applications in natural language processing demonstrate LIME's effectiveness for identifying which words and their weights influence classification probability—higher weights increase likelihood of positive classification, while lower weights decrease it[5]. However, research through 2024-2025 has identified critical limitations: LIME exhibits high sensitivity to perturbation strategies, produces unstable explanations across multiple runs due to random sampling, and fails to capture nonlinear feature dependencies inherent in sophisticated models[9][12]. The comparison study published in 2025 on image data using function-grounded metrics (fidelity, stability, identity, separability, and computational time) reveals that LIME trades interpretability gains for reduced localization precision relative to gradient-based methods[12].

Integrated Gradients emerged in the 2017-2019 period but has received renewed scrutiny in 2024-2025 regarding its reliability as a visual explanation method[14][17]. This technique computes the contribution of each input feature by integrating gradients along a straight path from a baseline input to the actual input[14]. A critical evaluation through 2024 revealed that while Integrated Gradients produces more stable explanations than some alternatives, its sensitivity to baseline selection—a central methodological choice—fundamentally impacts results, and the method exhibits surprising failure modes where it fails to correctly identify whether feature contributions toward model output are positive or negative[14][17]. The paper "Gradient-Based Saliency Maps Are Not Trustworthy Visual Explainers" demonstrated across six gradient-based saliency methods (Grad-CAM, gradient explanation, integrated gradients, Smoothgrad, smooth integrated gradients, and XRAI) that all exhibit concerning trustworthiness gaps: four of six methods failed reproducibility tests when applied to different neural network architectures, and five of six showed high sensitivity to model weight randomization, suggesting these methods may not reliably reflect true model behavior[17].

The standardization of XAI evaluation metrics represents a critical advancement in 2023-2025 research. A 2025 contribution introduces F-Fidelity, a robust evaluation framework addressing the Out-of-Distribution (OOD) problem inherent in perturbation-based evaluation[31][34]. Traditional evaluation perturbs features identified as important by XAI methods and observes prediction changes, but this approach generates OOD samples that violate the original data distribution, potentially invalidating conclusions. F-Fidelity employs explanation-agnostic fine-tuning with random masking to ensure removal steps remain in-distribution, and demonstrations across images, time series, and natural language show that F-Fidelity recovers ground-truth explainer rankings significantly more accurately than prior metrics, achieving superior discrimination among state-of-the-art methods[31][34]. This framework specifically addresses information leakage issues in prior approaches like ROAR (RemOve And Retrain), where model retraining based on XAI guidance could artificially inflate evaluation scores[34].

## Transformer-Based and Vision-Language Model Interpretability

Vision Transformers have prompted fundamental reconsideration of XAI approaches, as their inherent attention mechanisms offer built-in interpretability absent in convolutional architectures. The comprehensive review published in 2024 establishes that transformer-based XAI methods perform exceptionally well in medical imaging, with high Intersection-over-Union (IoU) scores in tumor localization tasks, achieving approximately 90% precision in pathology identification where highlighted regions overlap substantially with actual tumor areas[1]. The self-attention mechanism in transformers computes attention weights that directly link input patches to output predictions, providing transparency inherent to the architecture rather than requiring post-hoc approximations[1]. However, critical research through 2024-2025 demonstrates that interpreting transformer attention maps requires considerable caution: attention does not unambiguously represent feature importance, and attention weights may reflect computational patterns unrelated to decision-making[1][13]. A recent approach using masked attention in Vision Transformers for histopathology explicitly masks background patches from contributing to attention mechanisms, ensuring that non-informative regions cannot mislead predictions and producing more clinically meaningful attention heatmaps while maintaining performance comparable to standard self-attention[16].

Large Language Models present unique interpretability challenges distinct from computer vision systems, and the survey "Towards Transparent AI: A Survey on Explainable Large Language Models" provides systematic taxonomy across encoder-only (BERT-like), decoder-only (GPT-like), and encoder-decoder (T5-like) architectures[5]. For decoder-only models like GPT, XAI methods rely on prompt engineering and in-context learning to uncover opaque reasoning processes, exploiting the autoregressive generation mechanism to probe internal representations[5]. The research shows that different architectural families exhibit distinct interpretability signatures: encoder-only models naturally encode linguistic and syntactic information in lower layers and semantic information in upper layers, while decoder-only LLMs show anomalous patterns where upper layers focus excessively on local token-level features, diminishing global semantic representation capacity[19]. A probing study of four major multimodal LLMs (Kosmos-2, LLaVA, Qwen, and MiniCPM) using image-text entailment tasks reveals consistent evidence that topmost layers may sacrifice global cross-modal understanding for next-token prediction optimization, indicating a potential architectural misalignment in LLM pretraining objectives[19].

Knowledge probing methods have matured significantly as a complementary approach to gradient-based explanations. The method KnowProb, published in 2025, moves beyond surface-level text analysis to probe whether black-box language models understand implicit knowledge beyond given text using frame semantic parsing[22]. This approach constructs factual knowledge bases with semantic frames and evaluates whether models capture hidden knowledge that would be necessary for true reasoning versus surface-level pattern matching[22]. Experiments across small-scale (BERT, XLNet) and large-scale (GPT-style) models reveal that current LLMs face significant challenges in capturing hidden knowledge behind given text, particularly when reasoning requires understanding beyond the training distribution[22]. These findings highlight opportunities for improving reasoning capabilities across out-of-domain distributions, suggesting that contemporary LLMs rely more heavily on memorized patterns than genuine semantic understanding[22].

## Mechanistic Interpretability and Neural Circuit Discovery

Mechanistic interpretability represents a paradigm shift from explaining individual predictions toward reverse-engineering the computational algorithms embedded within neural networks. The 2025 survey on mechanistic interpretability in neural networks defines the field as "the process of studying the inner computations of neural networks and translating them into human-understandable algorithms," fundamentally distinct from post-hoc XAI methods that remain external to model computation[15]. Circuit discovery emerges as the leading task, seeking to identify causal subnetworks of neurons and connections that implement specific computational functions[15]. Empirical validation across toy models and large-scale networks demonstrates that neural networks contain structured circuits rather than relying solely on distributed, uninterpretable representations—a finding that aligns intuitions about algorithmic computation with observed network architecture[15].

However, recent critical analysis raises fundamental questions about mechanistic interpretability's claims. A 2025 paper titled "Everything, Everywhere, All at Once: Is Mechanistic Interpretability Identifiable?" systematically examines whether mechanistic interpretability guarantees unique explanations by implementing both major MI strategies: "where-then-what" (first identifying circuits that replicate behavior, then deriving interpretation) and "what-then-where" (first proposing candidate algorithms, then finding network locations implementing them)[18]. Testing on small MLPs with Boolean function learning reveals overwhelming evidence of non-identifiability: multiple circuits can replicate model behavior, multiple interpretations can explain a single circuit, several algorithms can be causally aligned with the network, and a single algorithm can be causally aligned with different network subspaces[18]. This work challenges whether MI produces scientifically meaningful explanations or merely creates post-hoc narratives that impose human-legible structure on fundamentally non-decomposable computation[18].

Sparse Autoencoders (SAEs) have emerged as promising tools for decomposing entangled network representations into interpretable features. Research through 2024-2025 demonstrates that SAEs transform dense, entangled neural representations into sparse, independent features amenable to individual analysis[15]. This approach has proven particularly successful for word embeddings in LLMs, enabling visualization and analysis of distinct semantic dimensions[15]. However, the extraction of meaningful, stable features remains challenging, and questions persist about whether SAE-discovered features correspond to genuine computational primitives or statistical artifacts of the decomposition procedure.

## Concept-Based and Prototype-Based Explanations

Concept Bottleneck Models (CBMs) provide ante-hoc interpretability by explicitly mapping internal representations to human-understandable concepts during training rather than applying post-hoc techniques. A 2024 contribution introduces Concept-based Memory Reasoner (CMR), designed to provide human-understandable and formally verifiable task predictions[10]. CMR models each prediction as a neural selection mechanism over learnable logic rules followed by symbolic evaluation, enabling domain experts to inspect and formally verify global properties prior to deployment[10]. Experimental results demonstrate that CMR achieves better accuracy-interpretability trade-offs than state-of-the-art CBMs, discovers logic rules consistent with ground truth, and enables meaningful rule interventions and pre-deployment verification—addressing critical limitations of earlier CBMs where task predictors remained opaque[10].

A broader contribution to mechanistic interpretability through concepts is BAGEL (Bias Analysis with a Graph for global Explanation Layers), published in 2024, which extends concept-based interpretability into mechanistic interpretability by analyzing how semantic concepts emerge, interact, and propagate through neural network layers[7]. Unlike prior work isolating individual neurons or predictions, BAGEL systematically quantifies concept representation across network depth, revealing latent circuits and information flow underlying decision-making[7]. The interactive visualization platform presents concept-class relationships as knowledge graphs, enabling users to explore concept-level semantics, identify spurious correlations, and assess model biases at scale[7]. This approach is particularly important for detecting whether models rely on genuine features versus learned spurious correlations, a distinction critical for safety in high-stakes applications.

Prototype-based explanation methods, including ProtoPNet and related architectures, provide interpretability by comparing inputs with learned prototypical representations. Research through 2024-2025 establishes that prototype-based approaches mimic human reasoning—identifying a bird's species by comparing key visual traits (beak, wing, feet) to prototypical examples—and embed interpretability into model architecture rather than applying post-hoc techniques[43]. The model learns prototypical representations during training and derives predictions from similarity to these prototypes, enabling users to understand decisions by inspecting most similar prototypes[43]. Case studies demonstrate successful applications to image classification, time-series analysis, and structured prediction tasks, though two-stage learning (first learning prototypes, then learning decision logic) remains computationally necessary to prevent overly complex, inaccurate models[43].

## Counterfactual and Causal Explanation Approaches

Counterfactual explanations address a fundamental limitation of feature attribution methods: they explain the decision space only partially and fail to convey actionable insights about what changes would alter predictions. The 2024 method CONFETTI (a multi-objective counterfactual explanation approach for multivariate time series) identifies the Nearest Unlike Neighbor as counterfactual target, locates influential subsequences via Class Activation Maps, generates initial counterfactual explanations through substitution, and optimizes across prediction confidence, proximity, and sparsity while ensuring plausibility and validity by design[8]. Benchmarking across seven datasets demonstrates that CONFETTI consistently outperforms state-of-the-art counterfactual methods in optimization objectives and exhibits ≥10% higher confidence while improving sparsity in ≥40% of test cases[8]. This work illustrates how counterfactual explanations provide minimal, actionable modifications—"what minimal changes to the input would reverse the prediction?"—capturing a different explanatory goal than feature attribution.

Causal AI represents the next frontier, moving beyond correlation-based prediction to understand cause-and-effect relationships. A 2025 analysis traces causal AI's emergence from Judea Pearl's foundational work on Directed Acyclic Graphs and do-calculus through contemporary applications in banking, retail, supply chains, and public health[27][30]. Causal AI fundamentally shifts from "when A happens, B follows" (correlation) to "does A cause B?" (causation), enabling counterfactual reasoning—"if we do X, what will happen?"—that traditional machine learning cannot support[27]. Applications in medical diagnosis demonstrate expert-level performance ranking in top 25% of doctors through causal reasoning about disease mechanisms, whereas conventional machine learning showed middling results[30]. In fraud detection, causal systems identify root causes enabling proactive vulnerability patching rather than reactive flagging of suspicious transactions[30]. These findings indicate that causal reasoning represents a distinct explanatory paradigm increasingly essential for high-stakes decision-making.

## Evaluation Frameworks and Human-Centered Assessment

Evaluation methodologies for XAI have matured substantially, with recognition that technical metrics alone cannot determine explanation utility. A 2024 systematic literature review on human-centered evaluation identifies 30 distinct components of meaningful explanations organized along three dimensions: (1) contextualized quality of explanations, (2) contribution to human-AI interaction, and (3) contribution to human-AI performance[33]. Critically, only 19 of 73 reviewed papers employed evaluation frameworks reused from prior studies, indicating severe lack of standardization across the field[33]. This fragmentation impedes cross-study comparison and general insights about what renders explanations meaningful to users[33]. The taxonomy reveals that user studies prioritize clinical plausibility over developer-emphasized interpretability—a critical gap between algorithmic explainability and stakeholder needs[36].

Human-centered evaluations of XAI in clinical decision support systems reveal persistent adoption barriers including high cognitive load, misalignment with clinical reasoning workflows, and limited meaningful stakeholder engagement[36]. A longitudinal study of an ICU risk prediction system integrating SHAP explanations with 112 clinicians found that developers emphasized model interpretability while clinicians prioritized clinical plausibility, creating design tensions around explanation utility[36]. This misalignment suggests that future XAI systems require ambidextrous design combining interpretability with clinically grounded plausibility, explicitly engaging stakeholders throughout development and evaluation cycles[36]. The framework proposed emphasizes iterative refinement through application-grounded evaluation (most realistic but expensive), human-grounded evaluation (balanced cost and generalizability), and proxy evaluation (scalable but less reflective of real-world deployment).

Robustness and adversarial considerations have become increasingly important. A comprehensive survey on adversarial attacks against XAI methods reveals that explanation techniques themselves can be attacked, fooled, or manipulated—undermining their trustworthiness for high-stakes decision support[32]. The research identifies existing insecurities in XAI, discusses defense mechanisms, and outlines emerging directions in adversarial XAI requiring explanation methods resilient to manipulation[32]. This work emphasizes that achieving trustworthy AI requires not only making predictions interpretable but ensuring interpretability mechanisms themselves resist adversarial exploitation.

## Data Attribution and Training Data Influence

Understanding how individual training examples influence model predictions has become increasingly important for accountability and debugging. Influence functions, originating from robust statistics, offer efficient first-order approximation to estimate marginal upweighting effects without expensive retraining[25]. A 2025 comprehensive review establishes that influence functions effectively identify training examples most influential to particular predictions, provide a tractable approach to data attribution, and scale to deep learning scenarios through techniques like TRAK and DataInf[25]. However, computational cost remains substantial—traditional influence functions require Hessian matrix inversion in high-dimensional spaces, motivating efficient approximations. TRAK (Tracing with Approximate Kronecker factors) leverages neural tangent kernel theory for scalable attribution across vision, language, and multimodal models[25]. A recent advance, distributional training data attribution, recognizes that deep learning inherently involves stochasticity in initialization and batching, yet traditional attribution ignores this variation[28]. The framework shows that influence functions are "secretly distributional"—emerging from unrolled differentiation without restrictive convexity assumptions[28]. These advances indicate that data attribution increasingly enables practitioners to identify problematic training examples, verify data quality, and understand how dataset composition influences learned behaviors.

## Recent Advances in Transparency and Regulatory Compliance

The regulatory landscape has accelerated adoption of explainability requirements. The 2025 analysis of XAI in business emphasizes that transparency is no longer optional but mandatory for GDPR compliance, EU AI Act adherence, and competitive positioning[21]. Companies like Liferay have begun comprehensive audits of AI systems to align with transparency principles, demonstrating technical feasibility of explainability at scale[21]. In Spain, authorities enforce similar expectations—AI systems in workplace settings must be auditable and subject to human oversight, with non-compliance risking fines up to €35 million[21]. This regulatory environment transforms explainability from best practice to legal necessity[21].

A 2025 framework from the University of Michigan introduces Constrained Concept Refinement (CCR), addressing a critical problem where previous explainable AI methods add interpretability features after models are trained, leaving concept embeddings fixed and potentially biased[2]. CCR embeds interpretability directly into model architecture, introduces flexibility in concept embeddings allowing task-specific adaptation, and achieves ten-fold runtime reduction while improving both interpretability and accuracy compared to previous concept bottleneck methods[2]. Testing on CIFAR-10/100, ImageNet, and Places365 shows CCR outperforms existing explainable methods while preserving interpretability and reducing computational cost—demonstrating that interpretability need not sacrifice performance[2].

## Integration of Knowledge and Explanation-Based Reasoning

Reasoning with natural language explanations has emerged as a distinct research area acknowledging that human reasoning fundamentally relies on explanations for learning and generalization[38][41]. The EMNLP 2024 tutorial on reasoning with natural language explanations grounds this discussion epistemologically and linguistically, establishing that explanation-based NLI differs fundamentally from end-to-end deep learning by explicitly constructing natural language explanations as intermediate reasoning steps[38][41]. Multi-hop reasoning retrieval-based approaches require selecting, collecting, and linking relevant knowledge to arrive at final answers, while generative approaches leverage LLMs for explanation generation[38][41]. Semantic control for explanatory reasoning combines neural and symbolic approaches to improve quality while providing formal guarantees[38][41]. These advances suggest that future AI systems will necessarily incorporate explicit reasoning chains, making explanation a structural component rather than post-hoc add-on.

## Synthesis of Experimental Evaluations and Common Findings

Across diverse XAI methods and application domains, several consistent conclusions emerge from experimental validation through 2025. First, no single explanation method universally dominates—each exhibits distinct trade-offs between interpretability, computational efficiency, and faithfulness[1][3][12]. Gradient-based methods (Grad-CAM, integrated gradients) achieve high computational efficiency but exhibit reproducibility failures and sensitivity to architectural variations[17]. Perturbation-based methods (LIME, SHAP) provide stronger theoretical guarantees and better stability but require more computation and generate potentially uninformative explanations when features exhibit high collinearity[9][12]. Transformer-based attention methods offer built-in interpretability but attention weights do not unambiguously represent importance[1][13][16]. This heterogeneity necessitates context-aware method selection rather than universal adoption.

Second, evaluation metrics remain inadequately standardized, preventing fair comparison across methods and domains. Traditional metrics (deletion, insertion) suffer from Out-of-Distribution problems, faithfulness evaluation remains subjective, and localization accuracy depends critically on application context[31][34][12]. F-Fidelity addresses OOD issues through explanation-agnostic fine-tuning, but broader standardization remains absent[31][34]. This metric fragmentation allows unreliable explanations to proliferate unchecked in practice.

Third, human-centered evaluation consistently reveals gaps between technical explainability and stakeholder utility. Developers prioritize interpretability metrics while clinicians prioritize clinical plausibility, security experts prioritize robustness to adversarial attack, and business stakeholders prioritize actionability and compliance demonstration[33][36][21]. This divergence indicates that XAI must be explicitly stakeholder-aligned rather than pursuing context-agnostic explanations.

Fourth, mechanistic interpretability reveals fundamental non-identifiability—multiple distinct explanations can account for identical model behavior, challenging whether unique scientific understanding is achievable[18]. This finding suggests limits to deterministic, uniquely-valued explanations, potentially necessitating ensemble or probabilistic explanation frameworks.

## Emerging Trends and Future Directions (2025 and Beyond)

**Trend 1: Hybrid Neuro-Symbolic Approaches Integrating Formal Verification.** The convergence between neural and symbolic AI accelerates through 2025, exemplified by approaches combining LLM-based explanation generation with theorem provers for logical validity verification and external tools for evaluating explanation properties like uncertainty and coherence[38][41]. This integration addresses a critical gap: neural explanations lack formal guarantees while symbolic explanations lack flexibility. Future systems will increasingly employ dual-path architectures where neural networks generate candidate explanations and symbolic systems verify logical consistency, enabling trustworthy AI for safety-critical domains requiring both interpretability and formal guarantees.

**Trend 2: Stakeholder-Centric, Context-Aware Explanation Frameworks Replacing Universal Methods.** The recognition that explanation utility depends fundamentally on stakeholder role, domain requirements, and task context will drive development away from universal XAI methods toward modular frameworks enabling stakeholder-specific explanation selection. The Holistic XAI framework exemplifies this direction, allowing users to select from multiple explanation methods adapted to specific questions and hypotheses[4]. Future research will formalize stakeholder taxonomies, develop domain-specific benchmarks, and create adaptive systems dynamically selecting explanation types based on user expertise and decision requirements.

**Trend 3: Mechanistic Interpretability Transitioning from Descriptive to Prescriptive Frameworks.** As evidence of non-identifiability accumulates, mechanistic interpretability will shift from claiming to uniquely identify model computation toward explicitly characterizing multiple valid explanations and establishing probabilistic confidence over explanation sets[18]. This paradigm change acknowledges that complete reverse-engineering may be impossible, instead focusing on discovering computational motifs, identifying sufficient explanations for practical purposes, and characterizing explanation uncertainty. Prescriptive frameworks will guide which explanations to prioritize for specific applications rather than seeking absolute truth.

**Trend 4: Causal AI Becoming Standard in High-Stakes Decision Systems.** The demonstrated superior performance of causal approaches in medical diagnosis, fraud detection, and policy evaluation will accelerate integration of causal inference into mainstream AI deployment[27][30]. Banking, insurance, healthcare, and government sectors will increasingly demand causal models for decision justification, moving beyond predictive accuracy toward evidence-based reasoning about interventions and counterfactuals. This shift requires substantial investment in causal discovery research, domain-specific causal model specification, and training practitioners in causal inference methodologies—representing a fundamental reorientation of AI development practices.

## Conclusion

Explainable artificial intelligence has matured from a specialized research subdomain toward a critical infrastructure requirement for responsible AI deployment. The 2022-2025 period demonstrates fundamental progress along multiple dimensions: standardized evaluation frameworks addressing Out-of-Distribution pitfalls, recognition of mechanistic interpretability's theoretical limitations, integration of human-centered design into XAI systems, and emergence of causal reasoning as a distinct explanatory paradigm complementing traditional feature attribution. Yet substantial challenges persist. No unified evaluation standard enables fair comparison across methods, stakeholder alignment remains poorly formalized, adversarial vulnerabilities of explanations themselves remain underexplored, and fundamental questions about whether unique explanations are achievable continue unresolved.

Future progress requires acknowledging inherent tensions between interpretability and performance, between technical explainability and stakeholder utility, and between universal frameworks and context-specific deployment. Rather than seeking perfect explanations applicable everywhere, the field must embrace pragmatic pluralism—developing modular, adaptive systems that select explanation types based on specific stakeholder needs, formal requirements, and domain constraints. The period 2025-2027 will likely see increased regulatory mandates for explanation capabilities, accelerated integration of causal reasoning into mainstream systems, and maturation of hybrid neuro-symbolic approaches combining neural flexibility with symbolic guarantees. Organizations proactively adopting human-centered, stakeholder-aligned XAI frameworks will gain competitive and reputational advantages, while those treating explainability as retroactive compliance theater will face legal, ethical, and operational risks. The transformation of AI from opaque prediction engines to interpretable, trustworthy decision-support systems is both technically achievable and increasingly necessary—success depends on embracing complexity and context-specificity rather than pursuing impossible universality.

---

## References

[1] Comprehensive Review of Explainable Artificial Intelligence (XAI) in Computer Vision. PMC National Center for Biotechnology Information, PMC12252469, 2024.

[2] DeLacey, P., et al. Explainable AI: New framework increases transparency in decision-making systems. University of Michigan College of Engineering, 2025.

[3] Malhotra, A., et al. A state-of-the-art approach using SHAP, LIME and Grad-CAM. PLOS ONE, 0318542, 2024.

[4] Holistic Explainable AI (H-XAI). arXiv:2508.05792, 2024.

[5] Towards Transparent AI: A Survey on Explainable Large Language Models. arXiv:2506.21812, 2025.

[6] Interpreting artificial intelligence models: A systematic review on the detection of Alzheimer's disease. PMC National Center for Biotechnology Information, PMC10997568, 2024.

[7] Concept-Based Mechanistic Interpretability Using Knowledge Graphs. arXiv:2507.05810, 2024.

[8] Counterfactual Explainable AI (XAI) Method for Deep Learning Models on Multivariate Time Series Data. arXiv:2511.13237, 2024.

[9] A Perspective on Explainable Artificial Intelligence Methods: SHAP and LIME. arXiv:2305.02012, 2023.

[10] Interpretable Concept-Based Memory Reasoning. NeurIPS 2024 Poster, 2024.

[11] A comprehensive analysis of perturbation methods in explainable AI. Nature, 2025.

[12] A comparative evaluation of explainability techniques for image data. Nature Scientific Reports, 2025.

[13] An autoencoder and vision transformer based interpretability framework. Nature Scientific Reports, 2025.

[14] Reliability of Integrated Gradients-Based Saliency Maps for 3D Point Clouds. Computer Graphics Forum, 2024.

[15] Mechanistic Interpretability for Algorithmic Understanding of Neural Networks. arXiv:2511.19265, 2025.

[16] Masked Attention as a Mechanism for Improving Interpretability of Vision Transformers. arXiv:2404.18152, MIDL 2024.

[17] Gradient-Based Saliency Maps Are Not Trustworthy Visual Explainers. PMC National Center for Biotechnology Information, PMC11522229, 2024.

[18] Everything, Everywhere, All at Once: Is Mechanistic Interpretability Identifiable? ICLR 2025 Poster, 2025.

[19] Probing Multimodal Large Language Models for Global and Local Semantic Representation. ACL Anthology, 2024.

[20] Model compression using knowledge distillation with integrated gradients. arXiv:2506.14440, 2024.

[21] Explainable AI (XAI) in 2025: How to Trust AI in 2025. Bismart Blog, 2025.

[22] Explaining Black-box Language Models with Knowledge Probing. arXiv:2508.16969, 2025.

[23] Knowledge distillation and dataset distillation of large language models. PMC National Center for Biotechnology Information, PMC12634706, 2024.

[24] Bias evaluation. European Data Protection Board, 2025.

[25] Revisiting Data Attribution for Influence Functions. arXiv:2508.07297, 2025.

[26] Layer-Wise Relevance Propagation with Weight-Dependent Baseline. SSRN, 2023.

[27] Causal AI: How cause and effect will change artificial intelligence. S&P Global Research Insights, 2025.

[28] Distributional Training Data Attribution: What do Influence Functions Sample? NeurIPS 2025 Spotlight, 2025.

[29] Layer-Wise Relevance Propagation: An Overview. Semantic Scholar, 2024.

[30] Causal AI Disruption Across Industries (2025-2026). Acalytica Blog, 2025.

[31] F-Fidelity: A Robust Framework for Faithfulness Evaluation of Explainable AI. OpenReview, ICLR 2025, 2025.

[32] Adversarial attacks and defenses in explainable artificial intelligence: A survey. arXiv:2306.06123, Information Fusion, 2024.

[33] Human-centered evaluation of explainable AI applications. Frontiers in Artificial Intelligence, 2024.

[34] F-Fidelity: A Robust Framework for Faithfulness Evaluation of Explainable AI. arXiv:2410.02970, ICLR 2025, 2025.

[35] Adversarial Robustness and Explainability of Machine Learning Models. ACM Digital Library, 2024.

[36] A Survey on Human-Centered Evaluation of Explainable AI Methods in Clinical Decision Support Systems. arXiv:2502.09849, 2025.

[37] Interpreting Vision-Language Models with VLM-LENS. ACL Anthology EMNLP Demos, 2025.

[38] Reasoning with Natural Language Explanations. EMNLP 2024 Tutorial, 2024.

[39] A Review of Interpretability Methods for Gradient Boosting Decision Trees. Journal of the Brazilian Computer Society, 2025.

[40] Interpretable Zero-Shot Learning with Locally-Aligned Vision-Language Model. ICCV 2025 Papers, 2025.

[41] Reasoning with Natural Language Explanations. arXiv:2410.04148, 2024.

[42] Practical guide to SHAP analysis: Explaining supervised machine learning models. PMC National Center for Biotechnology Information, PMC11513550, 2024.

[43] Prototype-Based Methods in Explainable AI and Emerging Applications. arXiv:2410.19856, 2024.

[44] Quantifying calibration error in neural networks through evidence-based theory. arXiv:2411.00265, 2024.

[45] An explainability-aware metric for evaluating the semantic fidelity of synthetic tabular data. arXiv:2511.17590, 2025.

[46] Example or Prototype? Learning Concept-Based Explanations in Time-Series. PMLR, Asian Conference on Machine Learning, 2023.

[47] A Primer on Uncertainty and Calibration in Deep Learning. Vizuara Substack, 2025.

[48] Measuring Fidelity Decay: A Framework for Semantic Drift and Collapse. Figshare, 2025.

[49] Multimodal LLM Augmented Reasoning for Interpretable Visual Perception Analysis. arXiv:2504.12511, 2025.

[50] Permutation importance: A corrected feature importance measure. Bioinformatics, 26(10):1340-1347, 2010.

[51] Neuron-Level Activation Learning in Neural Networks: A Self-Configuring AI Approach. SSRN, 2025.

[52] Understanding Llava's Visual Question Answering in a Mechanistic View. OpenReview ICLR 2025, 2025.

[53] Top-k Feature Importance Ranking. arXiv:2509.15420, 2025.

[54] Activation functions in neural networks. SuperAnnotate Blog, 2024.

[55] The 2025 AI Index Report. Stanford HAI, 2025.

[56] Semantic Faithfulness and Entropy Production Measures to Tame LLM Hallucinations. arXiv:2512.05156, 2025.

[57] GOAt: Explaining Graph Neural Networks via Graph Output Attribution. arXiv:2401.14578, ICLR 2024, 2024.

[58] 25 AI benchmarks: Examples of AI models evaluation. Evidently AI Blog, 2025.

[59] Drift: Enhancing LLM Faithfulness in Rationale Generation via Dual Inference. ACL Long, 2025.

[60] GOAt: Explaining Graph Neural Networks via Graph Output Attribution. OpenReview ICLR 2024, 2024.