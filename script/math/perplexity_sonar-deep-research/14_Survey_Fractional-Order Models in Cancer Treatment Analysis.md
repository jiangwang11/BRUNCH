# Fractional-Order Models in Cancer Treatment Analysis: A Comprehensive Review of Recent Advances (2022-2025)

Recent advances in mathematical oncology have increasingly employed fractional-order differential equations to capture the memory effects and non-local dynamics inherent in cancer progression and therapeutic response. Unlike conventional integer-order models that assume instantaneous changes, fractional-order approaches incorporate historical dependencies and anomalous diffusion processes, enabling more accurate predictions of tumor dynamics under various treatment modalities. This comprehensive review synthesizes representative works from 2022 to 2025, examining how fractional calculus frameworks enhance our understanding of chemotherapy, immunotherapy, radiotherapy, and combination treatment strategies while addressing critical gaps between theoretical models and clinical outcomes. Key findings demonstrate that fractional-order parameters typically in the range of 0.70 to 0.98 provide superior fits to real patient data compared to classical models, while fractal-fractional operators offer enhanced numerical stability through Mittag-Leffler kernels that better represent the complex tumor microenvironment.

## Introduction to Fractional Calculus in Cancer Modeling

### Theoretical Foundations and Motivation

Fractional-order calculus represents a generalization of classical differentiation and integration to non-integer orders, providing a powerful mathematical framework for systems exhibiting memory effects and long-range interactions. In cancer biology, these properties are fundamentally important because tumor growth and immune responses depend critically on historical states rather than instantaneous conditions alone[2][8]. Traditional integer-order differential equation models assume that system behavior depends only on current state variables, which fails to capture the persistent effects of prior chemotherapy exposures, residual immune cell damage, or the cumulative metabolic stress experienced by cancer cells. The biological justification for fractional modeling in oncology rests on several well-documented phenomena: cancer cells exhibit genomic memory of previous drug exposures that influences mutation rates and resistance development; immune cells display fatigue and activation states that persist beyond immediate stimuli; and tumor microenvironments contain diffusive processes that follow anomalous rather than Fickian kinetics[1][2].

The mathematical advantage of fractional derivatives lies in their ability to characterize non-Markovian processes through memory kernels and power-law decay functions. Rather than assuming exponential relaxation of system components toward equilibrium, fractional models permit algebraic decay rates that more accurately reflect biological timescales observed in clinical practice. For instance, tumor dormancy periods lasting months or years, the slow kinetics of immune checkpoint inhibitor response, and the protracted effects of radiation-induced cellular damage all suggest that cancer systems operate under non-integer orders of dynamics[9][15]. The **Caputo fractional derivative** emerges as the most widely adopted operator in cancer modeling because it accommodates intuitive initial conditions expressed in standard biological units, whereas other definitions like Riemann-Liouville require more abstract initial state specifications[1][12][13].

### Historical Context and Recent Momentum

While fractional calculus has existed as a mathematical discipline since the eighteenth century, its systematic application to disease modeling accelerated substantially during the COVID-19 pandemic and has subsequently become standard in mathematical oncology. Between 2022 and 2025, the number of published studies employing fractional-order cancer models increased dramatically, with particular concentration in journals including *Fractional Calculus and Applied Analysis*, *Mathematical Biosciences and Engineering*, *PLoS ONE*, *Scientific Reports*, and several NIH-indexed databases. This acceleration reflects recognition among computational oncologists that integer-order models systematically underestimate treatment durations and mispredict bifurcation thresholds that trigger tumor relapse. The transition toward clinical validation has intensified as well, with multiple groups developing models parametrized directly from patient cohorts rather than theoretical assumptions[1][40][57].

## Fractional-Order Models of Therapy and Prevention

### Breast Cancer with Integrated Treatment Frameworks

A landmark 2024 study published through NIH repositories analyzed breast cancer dynamics using a comprehensive fractional-order model incorporating therapy intensity and early diagnosis/prevention strategies with Caputo fractional derivatives[1][29]. This work established that fractional orders approximately equal to 0.98 achieve optimal concordance with real patient data spanning multiple disease stages, substantially outperforming both lower fractional orders and integer-order baseline models. The sensitivity analysis revealed **differential parameter influences**: while chemotherapy recovery rates at early cancer stages (stages 1-2) generated mixed effects on patient populations, escalated chemotherapy at stage 4 consistently reduced stage 4 patient numbers while increasing recovery rates through improved disease-free outcomes[1]. The optimal control framework demonstrated that combined therapy strategies outperformed single-modality approaches, with the cost functional analysis confirming reduced treatment expenses when using fractional-order optimization compared to classical methods.

Building upon this foundation, another piecewise fractional-stochastic model for breast cancer progression combined constant-order Caputo proportional operators in early phases, variable-order Caputo operators in intermediate growth stages, and stochastic components during advanced disease to capture the transition from deterministic growth to probabilistic outcomes[40]. Theoretical analysis employing fixed-point theory for fractional phases and Itô calculus for stochastic segments established existence and uniqueness of solutions under specified Lipschitz conditions. Validation against breast cancer registry data from Saudi Arabia spanning 2004-2016 demonstrated that the model accurately reproduced both overall trends and individualized treatment response variability, with numerical simulations capturing chemotherapy-induced cardiotoxicity effects that integer-order models systematically neglected[40].

### Endometrial Cancer Under Chemo-Immunotherapy

Research on endometrial cancer treatment published in 2024 developed mathematical models examining dostarlimab (anti-PD-1 immunotherapy) combined with chemotherapy using both classical and **fractional singular kernel formulations**[13]. The fractional framework proved superior in achieving cost-effective tumor control: fractional-order models reduced cancer cells to lower equilibrium levels while maintaining higher activated CD8+ T-cell populations compared to integer-order equivalents, suggesting that memory effects captured through fractional derivatives better represent immunological persistence and sustained anti-tumor activity[13]. Optimal control analysis demonstrated that combined therapy under fractional-order dynamics achieved faster tumor reduction, sustained elevated immune responses, and achieved lower overall treatment costs by balancing cytotoxic drug dosing with immune activation. The study identified six equilibrium points and analyzed stability through Routh-Hurwitz criteria, establishing conditions under which the system converges to disease-free equilibria rather than tumor-persistent states[13].

## Tumor-Immune Dynamics and Fractal-Fractional Operators

### Atangana-Baleanu Framework for Immune Cell Interactions

A substantial body of recent research has adopted the **Atangana-Baleanu fractal-fractional derivative**, which combines fractal and fractional operators to simultaneously capture memory effects and spatial complexity within tumor microenvironments[2][19][35]. This mathematical framework proves particularly valuable because tumors exhibit fractal-like vascular networks, irregular cellular arrangements, and hierarchical organization across multiple length scales that classical smooth derivatives cannot properly represent[2][4][9]. Studies employing Atangana-Baleanu operators consistently demonstrate that the approximate fractal order 0.5-0.7 optimally represents tumor tissue heterogeneity, with numerical experiments validating this choice through comparison with imaging data showing fractal vasculature[2][19]. The fractal-fractional approach provides numerical stability superior to singular-kernel Caputo derivatives because the Mittag-Leffler kernel exhibits smoother asymptotic behavior, producing more reliable long-term predictions of treatment response[4][9][15][25].

Research investigating tumor-immune cell interactions through fractal-fractional derivatives revealed crucial insights into helper cell and dendritic cell dynamics[2][8][19]. Helper cells exhibit significant temporal fluctuations characterized by initial proliferation followed by gradual decline, reflecting their dynamic role in modulating immune responses through complex feedback mechanisms[2]. Dendritic cells undergo deterioration over time as tumors employ immunosuppressive signaling, shifting these cells from potent defenders into suppressive phenotypes incapable of effective antigen presentation[2][8]. Lagrangian-piecewise interpolation numerical simulations across various fractional and fractal parameters demonstrated that lower fractional orders produce slower convergence toward equilibrium, extending the duration of disease-related complications, while intermediate orders (0.70-0.85) optimize therapeutic timing[2][19][35].

### Stability Analysis via Lyapunov Functions and Fixed-Point Theory

Theoretical advances in fractional cancer modeling have concentrated on rigorous stability analysis employing Lyapunov direct method and fixed-point theorems to establish well-posedness of proposed systems[4][9][15][25]. For fractal-fractional tumor-radiotherapy models, researchers proved global asymptotic stability by constructing Lyapunov functions \(V(t)\) satisfying \(\frac{dV}{dt}\bigg|_{system} \leq 0\) with equality only at equilibrium points[4][9]. The mathematical conditions ensuring stability require that cancer cell growth remains suffressed while healthy cells maintain competitive advantage, formally expressed as constraints on recovery rates and immune killing efficiency[4][25]. Existence and uniqueness of solutions were established through Banach fixed-point theorem, demonstrating that under specified Lipschitz continuous conditions on nonlinear reaction terms, the system admits a unique solution trajectory in appropriate function spaces[2][4][15][35].

These theoretical results provide clinical significance by identifying bifurcation thresholds beyond which the system transitions from tumor-controlled equilibria to disease-persistent states. Hopf bifurcation analysis revealed that critical delay parameters, particularly polarization time for macrophage differentiation and immune response latency, can trigger periodic oscillations representing tumor dormancy-escape cycles[21][24][44][47]. Time-delay studies demonstrated that short delays (<5 days) generally enhance tumor suppression, whereas prolonged delays (>15 days) destabilize the system and facilitate disease recurrence[21][26][44][47]. These findings translate into clinical guidance: immunotherapy timing relative to radiation exposure matters critically, with radiation-induced lymphocyte depletion negating simultaneous CAR-T cell efficacy if administered too closely[44][54].

## Radiotherapy Integration and Fractal-Fractional Frameworks

### Modeling Complex Radiotherapy Responses

Recent mathematical models of cancer radiotherapy adopted fractal-fractional operators to capture how radiation simultaneously damages both malignant and healthy cells while triggering heterogeneous immune responses across spatially irregular tumor architecture[4][9][25][30]. The AMBER (Agent-based fraMework for radioBiological Effects in Radiotherapy) modeling system represents a state-of-the-art approach that discretizes three-dimensional tumor domains into voxels, tracks vessel networks with explicit representation of major vasculature above 100 micrometers while using microvessel density maps for smaller vessels[43]. By integrating TOPAS Monte Carlo radiation transport with biological damage induction-repair models, AMBER achieves realistic representations of dose heterogeneity and hypoxia-driven radiosensitivity variations that pure mathematical models cannot capture[43]. Simulations demonstrated emergence of necrotic cores, angiogenic vasculature expansion, and treatment-induced apoptosis consistent with clinical observations, validating the hybrid ABM-PDE approach[43].

Fractal-fractional mathematical models of radiotherapy captured memory effects through Caputo derivatives of order 0.75-0.90, with fractal dimensions typically around 0.5-0.65 representing tumor microenvironment irregularity[4][9][25]. The mathematical model compares healthy cell dynamics \(H(t)\) and cancer cell dynamics \(C(t)\) under radiation dose \(D(t)\), formulated as coupled fractional differential equations where fractional order reflects how historical radiation exposure influences current radiosensitivity through DNA repair kinetics and immune priming[4][9]. Numerical simulations using Lagrangian-piecewise interpolation methods demonstrated that fractional-order models achieve superior convergence properties and numerical stability compared to classical Caputo approaches with singular kernels[4][9][15][25]. Key results showed radiation dosage impacts cancer and healthy cells differentially: while fractional-order models predicting treatment response exhibited accuracy within 5-8% of clinical outcomes, integer-order models systematically overestimated therapy effectiveness by 15-25%[4][25].

### Abscopal Effects and Immunotherapy Synergy

Mathematical analysis of radiotherapy synergized with immunotherapy revealed conditions under which radiation on primary tumors triggers sufficient immune activation to regress distant metastatic lesions (abscopal effects)[30]. The phenomenological approach based on Gompertz growth laws with fractional parameters demonstrated that specific rate data (tumor growth rate per unit tumor volume) provides more reliable progression indicators than absolute volume changes[30]. Critical conditions derived from the mathematical formalism showed that when radiotherapy achieves sufficient specific rate reduction and immunotherapy response magnitude exceeds critical thresholds \(\epsilon^*\), tumor volume regression becomes possible despite fractioned dose delivery[30]. Optimization of radiation dose fractionation relative to immunotherapy timing proved essential: protracted schedules with low doses per fraction inadvertently cleared radiosensitive lymphocytes from tumor tissues, negating immune activation, while very high single doses (>12 Gy) degraded immunogenic cytosolic DNA, also reducing efficacy[30]. Spatially fractionated radiation therapy combining variable dose regions showed promise for multiple immune activation mechanisms, with clinical data indicating complete response achievement preceding immunotherapy administration in several cases[30].

## Mixed Therapy Models and Optimization

### Chemotherapy and Stem Cell Therapy Integration

A fractal-fractional order mathematical model combining stem cell therapy and chemotherapy employed the **Mittag-Leffler kernel**, capturing both memory effects and complex biological processes inherent in cancer progression and treatment response[20][38]. The model represented stem cells, effector immune cells, tumor cells, and chemotherapy drug concentration as coupled fractional differential equations, with stem cell proliferation effects amplified through immune system activation[20][38]. Stability analysis via Matignon criterion established that equilibrium points represent locally stable attractors, while Adams-Bashforth numerical methods based on two-step Lagrange polynomial interpolation provided accurate solution approximations[20][38]. Simulations revealed that stem cells rapidly decrease from initial values before stabilizing at diminished levels, while effector cell populations increase substantially in response to stem cell-derived signals, demonstrating the amplification of anti-tumor immunity through cellular therapy[20][38].

The coupled dynamics showed interdependence: stem cells undergo attrition from both chemotherapy drug exposure and cancer cell interactions, yet their presence magnifies effector cell-mediated tumor destruction through paracrine signaling[20][38]. Chemotherapy concentration dynamics exhibited first-order kinetics appropriate to drug clearance, with concentration peak times shifting when combined with stem cell therapy due to altered tumor burden affecting drug distribution[20][38]. Different fractional orders (α = 0.70, 0.80, 0.90) produced qualitatively distinct dynamics: lower orders exhibited prolonged transients before reaching equilibrium, while higher orders approached steady-state more rapidly, suggesting fractional order encodes information about cancer aggressiveness or treatment resistance[20][38].

### Combination Immunotherapy and Targeted Therapy for Lung Cancer

Recent work on heterogeneous lung cancer developed a **fractional-order model optimizing combination therapy** integrating immunotherapy and targeted therapy while incorporating Proportional-Integral-Derivative (PID) feedback control mechanisms[27][31][51]. The five-variable model tracked normal cancer cells \(N(t)\), immune cells \(I(t)\), spread cancer cells \(P(t)\), genetic mutations \(M(t)\), and enhanced immune cells \(R(t)\), each governed by fractional differential equations capturing memory-dependent growth, death, and interaction processes[27][31][51]. Unlike previous studies treating therapies independently, this framework explicitly represented interactions between regular and mutated cancer cells, immune cell dynamics responding to mutation burden, and treatment-induced changes in cytotoxic efficacy[27][31][51]. The optimization process minimized a cost functional balancing tumor reduction against treatment toxicity, employing Lagrange interpolation methods for numerical solution[27][31][51].

Results demonstrated that combined therapy achieved superior outcomes compared to monotherapy approaches: tumor reduction reached lowest equilibrium levels when both immunotherapy and targeted therapy were administered optimally, with immune cell activation sustained at higher levels than achievable through single-modality treatment[27][31][51]. Sensitivity analysis highlighted parameter interdependencies: mutation rate critically influenced targeted therapy efficacy, since high mutation burden rapidly generated treatment-resistant phenotypes, while immune cell death rates directly constrained immunotherapy effectiveness[27][31][51]. The PID controller adjustment mechanism enabled dynamic dose modification responding to real-time tumor burden changes, achieving cost-effective control through reduced drug consumption while maintaining therapeutic objectives[27][31][51]. Fractional-order models demonstrated 15-20% faster tumor burden reduction compared to integer-order equivalents when solved under identical parameter constraints[27][31][51].

### Endometrial Cancer with Dostarlimab and Chemotherapy

An investigation of endometrial cancer under dostarlimab-chemotherapy combination employed optimal control frameworks within fractional-order formulations, directly comparing classical integer-order against fractional Caputo-singular kernel models[13]. Both frameworks identified combined therapy as superior to monotherapy, but fractional-order analysis revealed **superior cost-effectiveness**: the fractional model achieved equivalent tumor reduction with 20-30% lower treatment cost by exploiting memory effects for sustained immune cell activation from previous dostarlimab doses[13]. Dostarlimab functions mechanistically by disrupting the PD-1/PD-L1 immune checkpoint, maintaining T-cell activation across multiple therapeutic cycles, and the fractional formulation captured this persistence mathematically through Caputo kernels encoding multi-generational immune memory[13]. Numerical solutions via MATLAB's fde12 solver demonstrated convergence superiority: fractional-order cost functionals achieved minimum values in approximately 8-10 iterations versus 15-20 iterations for integer-order equivalents[13].

The model analysis established six equilibrium points representing distinct disease outcomes: tumor eradication with elevated immune activation (disease-free equilibrium), sustained tumor persistence with compromised immunity (endemic equilibrium), and unstable intermediate states[13]. Stability analysis via Banach fixed-point theorem proved local asymptotic stability of the disease-free equilibrium under specified parameter ranges, with implications for patient selection: individuals with high baseline CD8+ T-cell frequencies (parameter \(\rho_1\)) exhibited greater stability toward disease-free states, suggesting immunotherapy efficacy prediction from pre-treatment immune profiling[13]. Routh-Hurwitz criteria analysis identified critical chemotherapy intensity thresholds: beyond certain dosing levels, further escalation destabilized equilibrium points and triggered oscillatory behavior representing intermittent disease control interrupted by treatment-induced immune exhaustion[13].

## Tumor Growth Models and Parametric Sensitivity

### Colorectal Cancer with Fractional Sensitivity Analysis

A comprehensive fractional-order modeling study of colorectal cancer employed sensitivity analysis to identify critical parameters governing disease progression and treatment response[26]. The model incorporated epithelial cells, adenomatous polyps, oncogenes, tumor suppressor genes, and specific gene mutations (APC, KRAS) as interconnected components governed by fractional Caputo derivatives, enabling capture of how genetic alterations accumulate and influence phenotypic evolution[26]. Sensitivity coefficients \(\frac{\partial X_i}{\partial \theta_j}\) were calculated for each state variable with respect to key parameters, revealing non-uniform parameter importance: mutation rates and gene-specific threshold parameters dominated sensitivity profiles for oncogenic transformation, while immune cell recruitment rates critically governed established tumor dynamics[26]. The analysis demonstrated that some parameters exhibited high sensitivity at certain disease stages but negligible influence at others, suggesting therapeutic windows for intervention could be identified through mathematical profile likelihood analysis[26].

Results indicated that fractional-order parameter values of 0.80-0.95 optimally characterized colorectal cancer progression in population-level data, though substantial between-individual variability (0.70-0.98 range) reflected genetic heterogeneity in tumor evolution rates[26]. Treatment response sensitivity depended critically on when therapy was initiated: early intervention (within adenoma stages) achieved response with lower drug concentrations, while late-stage interventions required 3-4 fold dose escalation to achieve equivalent therapeutic effects[26]. The sensitivity analysis provided practical guidance: targeting APC gene mutation rates through epigenetic modulation or DNA methylation inhibitors emerged as high-sensitivity parameters, suggesting personalized treatment strategies should prioritize pathways with elevated sensitivity coefficients specific to individual patient genotypes[26].

### Glioblastoma Dynamics via Fractional Burgess Equation

Investigation of glioblastoma, the most aggressive brain tumor, employed a fractional-order **Burgess equation** approach capturing variable killing rates of tumor cells through mathematical modeling[5]. The fractional Burgess formulation enabled analytical and numerical solutions through transform methods and Adomian decomposition algorithms, with memory-preserving non-local derivatives acknowledging that glioma cell populations exhibit phenotypic and genetic memory affecting subsequent treatment responses[5]. Solutions revealed how medical care intensity influences glioma eradication dynamics: higher killing rates achieved faster tumor extinction but generated larger gradients in treatment effect requiring precise spatial dose uniformity in radiotherapy delivery[5]. The model provided quantitative predictions of therapy efficacy across variable killing rates, directly translating mathematical results to clinical dosing recommendations[5].

Numerical simulations demonstrated that fractional-order parameters 0.75-0.85 characterize glioblastoma growth dynamics, with lower orders associated with more aggressive phenotypes exhibiting prolonged response latency to therapy[5]. The Adomian decomposition method proved computationally efficient, generating series solutions converging rapidly even for highly nonlinear tumor-drug interactions[5]. This analytical tractability enabled sensitivity studies showing glioma doubling times exhibit exponential sensitivity to fractional order: a 0.1 change in fractional parameter altered predicted tumor burden at 100 days post-treatment by 30-40%, underscoring importance of accurate parameter estimation from individual patient imaging data[5].

### Smoking-Related Cancer Risk Assessment

A mathematical model addressing cancer risk from smoking habits employed ABC (Atangana-Baleanu-Caputo) fractional derivatives within a compartmental framework tracking susceptible individuals, smokers, and cancer patients[10][18][58]. The fractional formulation captured how cumulative smoking exposure creates irreversible epigenetic and genomic changes increasing cancer susceptibility across multiple years or decades[10][18][58]. Sensitivity analysis identified smoking initiation age and intensity (cigarettes per day) as critical parameters: individuals beginning smoking before age 18 experienced 4-6 fold increased cancer risk compared to those initiating at age 25+, even after adjusting for total lifetime cigarette consumption[10][18][58]. The fractional-order model captured this age-dependent acceleration better than integer-order equivalents because it incorporated multi-generational memory of cellular damage accumulation[10][18][58].

Model analysis revealed that fractional orders approximately 0.85-0.95 fit smoking-related cancer epidemiology data across diverse populations[10][18][58]. Bifurcation analysis identified critical smoking prevalence thresholds triggering rapid cancer incidence acceleration in populations: above 20% population prevalence, cancer incidence rates exhibited supralinear growth, whereas below 15% prevalence, incidence scaled sublinearly with smoking rates[10][18][58]. The results supported intensive smoking cessation interventions below these thresholds where modest reduction efforts produce disproportionate cancer prevention benefits[10][18][58].

## Advanced Mathematical Methods and Numerical Schemes

### He-Laplace and Adomian Decomposition Approaches

Recent advances in fractional cancer modeling employed the **He-Laplace method** combining homotopy perturbation method with Laplace transforms to solve complex fractional differential equations[55][59]. This hybrid approach proved particularly valuable for highly nonlinear cancer-immune interaction models where exact analytical solutions remain unavailable[55][59]. The He-Laplace algorithm constructs series solutions through iterative deformation equations, with convergence guaranteed by Cauchy criterion ensuring solution stability and consistency as iteration number approaches infinity[55][59]. Comparative studies of He-Laplace against Runge-Kutta numerical methods demonstrated superior accuracy and computational efficiency, with He-Laplace achieving convergence in 8-12 iterations versus 200+ integration steps for RK4[55][59].

Implementation of He-Laplace to fractional cancer-tumor models with immunotherapy demonstrated that residual error analysis across fractional domains provides quantitative validation: for fractional orders α = 0.22 to 1.0, residual errors decreased systematically, approaching zero as α→1, confirming method reliability[55][59]. Three-dimensional solution profiles showed tumor cell concentration trending toward zero as time and spatial position increase, indicating successful tumor suppression under optimal treatment[55][59]. Comparative analysis of Caputo, Caputo-Fabrizio, and Atangana-Baleanu derivatives revealed Caputo depicted highest cell concentration while Atangana-Baleanu showed least, suggesting kernel choice substantially influences quantitative predictions[59].

The Adomian decomposition method established itself as computationally efficient alternative for fractional cancer models, generating convergent series solutions particularly suitable for hardware implementation in clinical decision support systems[5][14][34]. ADM decomposition polynomials capture nonlinear reaction-diffusion terms through recursive computation, enabling analytical investigation of parameter sensitivities without extensive numerical integration[5][14][34]. Studies comparing ADM against explicit finite difference methods demonstrated ADM consistently achieved higher accuracy with lower computational overhead, particularly advantageous for real-time treatment planning where rapid solution updates are required[5][14][34].

### Hybrid Machine Learning and Fractional Dynamics

Recent work integrated **deep neural networks with fractional-order dynamical models** for breast cancer progression prediction across diagnostic and temporal scales[57]. The hybrid framework achieved 97.72% classification accuracy on Wisconsin Diagnostic Breast Cancer dataset through deep neural network architecture, identifying morphological features (area, radius, texture, concavity) as top malignancy predictors[57]. Beyond static classification, fractional-order models captured temporal dynamics: lower fractional orders (α = 0.60-0.75) correlated with prolonged aggressive growth mimicking certain cancer subtypes, while higher orders (α = 0.90-0.98) indicated rapid stabilization reflecting indolent behavior[57]. The framework developed interactive GUI enabling real-time risk assessment integrated with growth trajectory simulations, demonstrating clinical utility for personalized treatment planning[57].

Theoretical rigor was maintained through fixed-point theory establishing existence and uniqueness of solutions under Lipschitz continuity conditions[57]. Numerical simulations closely fitted clinical data, with mean squared error remaining below 5% when model parameters were optimized to individual patient cohorts[57]. The integration of machine learning with fractional dynamics represented innovation over previous approaches: rather than treating predictive classification and mechanistic modeling separately, the unified framework captured both static risk factors and dynamic disease progression simultaneously[57].

## Stability Analysis and Control Strategies

### Bifurcation Analysis and Tumor Recurrence Dynamics

Hopf bifurcation analysis of tumor-macrophage models with time delays revealed how polarization lag and immune response latency trigger periodic oscillations representing tumor dormancy-escape cycles[21][44][47]. The mathematical framework tracked tumor cells (T), classically activated macrophages (M1), alternatively activated macrophages (M2), and inactive macrophages (M0) with polarization delay parameter τ governing M0→M1/M2 differentiation[21][44]. Analysis proved that beyond critical delay thresholds \(\tau^* ≈ 8-12\) days, the system undergoes Hopf bifurcation, bifurcating periodic solutions emerging from interior equilibrium[21][44]. These limit cycles mathematically represent oscillatory tumor burdens, clinically manifesting as intermittent disease exacerbation and apparent remission cycles familiar to oncologists observing certain patient subpopulations[21][44].

The normal form and center manifold theorem analysis characterized bifurcation supercriticality: as τ increases through critical value, periodic orbits with small amplitude emerge stably (supercritical bifurcation), predicting that small delays induce mild oscillations whereas larger delays produce substantial amplitude limit cycles[21][44][47]. Parameter sensitivity analysis demonstrated M1 macrophage death rate and tumor killing efficacy critically govern bifurcation location: reducing M1 death or increasing killing efficacy shifts critical delay to longer durations, therapeutically delaying or preventing periodic solutions[21][44][47]. Numerical simulations validated analytical predictions, showing good agreement between theoretical bifurcation values and computationally-determined critical delay transitions[21][44][47].

### Memristor-Based Control and Optimal Dosing

Novel control strategies employing memristor-based feedback mechanisms showed promise for fractional tumor-immune models[23]. The memristor approach introduces adaptive feedback responsive to system history, implementing a control law where current dosing depends on integral of past tumor burden—a natural formulation within fractional calculus frameworks[23]. Generalized Adams-Bashforth-Moulton algorithms solved the controlled fractional tumor-immune system, with numerical dissection via signal flow diagrams clarifying system component interactions[23]. Optimization results demonstrated memristor-controlled dosing achieved 10-15% better tumor suppression compared to standard proportional-integral-derivative controllers, particularly when treatment delivery exhibited delays inherent to clinical administration[23].

Optimal control analysis across multiple cancer models consistently identified dosing intensity and timing as critical coupled parameters: simultaneous escalation of drug dose and increased treatment frequency generally improved outcomes but at marginal benefit once certain thresholds were exceeded[1][13][27][31]. The optimal control framework formulated cancer management as minimization of cost functional \(\mathcal{J}\) balancing competing objectives: \(\mathcal{J} = \int_0^T [c_1 N(t)^2 + c_2 D(t)^2] dt\) where N represents tumor burden, D represents drug dose, and weights \(c_1, c_2\) encode clinical priorities[1][13][27][31]. Optimal solutions identified treatment profiles minimizing tumor burden while restricting cumulative toxicity—mathematically elegant formulations translating directly to clinical practice through model-predictive control implementation[1][13][27][31].

### PID Feedback and Adaptive Treatment Adjustment

Proportional-Integral-Derivative feedback controllers adapted to fractional-order cancer models enabled real-time treatment adjustment maintaining cancer cell populations within specified tolerance bands around target levels[27][31][51]. The PID control law \(u(t) = K_p e(t) + K_i \int_0^t e(s)ds + K_d \frac{de}{dt}\) was formulated within fractional calculus, with integral and derivative terms modified to accommodate fractional orders[27][31][51]. Simulation studies demonstrated PID controllers achieved 20-25% improvement in control precision compared to open-loop (pre-planned) dosing schedules, with adaptation particularly valuable when patient parameters varied unpredictably[27][31][51]. The integration of Lagrange interpolation methods enabled smooth fractional derivatives required for D term implementation, avoiding numerical artifacts plaguing earlier approaches[27][31][51].

## Parametric Identifiability and Model Selection

### Growth Model Comparison and Parameter Recovery

Comparative study of seven cancer growth models (exponential, logistic, Gompertz, Bertalanffy, Weibull, Richards, surface) revealed critical identifiability challenges when fitting synthetic drug response data[33]. The analysis generated synthetic time-courses using each growth model, then systematically fit all models to each dataset, measuring whether true parameters were recovered[33]. Results showed that many growth parameters, particularly those governing long-timescale behavior like carrying capacity or maximum tumor size, exhibited weak practical identifiability when data only spanned short intervals typical of clinical studies[33]. The Bertalanffy model showed unusual behavior as outlier, consistently underestimating drug efficacy parameters when fitting data from other models, suggesting specific mathematical formulation properties critically influence parameter recovery[33].

Importantly, even when identical models generated and fit data, correct parameter recovery often failed: the Gompertz and Mendelssohn models systematically overestimated key coefficients at 5% and 10% noise levels, reflecting mathematical structure limiting identifiability independent of data quality[33]. These findings held critical implications for fractional cancer models: parameter estimation from clinical data requires careful model validation and sensitivity analysis; published parameter values from one cohort may not transfer to other populations[33]. The study recommended statistical approaches quantifying practical identifiability through profile likelihood methods and confidence interval analysis prior to accepting model parameter estimates[33].

### Temporal Scales and Long-Term Behavior

Parameter identifiability depended critically on timescale matching between data observation duration and process dynamics: parameters determining slow processes (e.g., tumor carrying capacity governing long-term growth saturation) exhibited poor identifiability from short observation windows because data did not approach asymptotic behavior[33]. This observation carried direct implications for fractional models: fractional orders governing memory decay timescales similarly required longitudinal data spanning equivalent durations to support identifiable estimation[33]. Shorter clinical studies (weeks to few months) could reliably estimate immediate treatment response parameters but provided insufficient information for accurate fractional-order estimation characterizing disease memory over months or years[33].

## Experimental Validation and Clinical Applications

### Quantitative Validation Against Patient Cohorts

Multiple recent studies validated fractional cancer models against prospective and retrospective patient datasets spanning diverse cancer types. Breast cancer cohort studies from Saudi Arabia spanning 2004-2016 demonstrated that fractional-order breast cancer progression models achieved prediction accuracy within 5-8% mean absolute error, substantially outperforming integer-order baseline models by 10-15% error margins[40]. The piecewise fractional-stochastic framework particularly excelled at capturing individual heterogeneity: while population-level trajectories showed similar patterns, fractional-order variation enabled individualized predictions differing by 20-30% from population means, clinically relevant for treatment personalization[40].

B-lymphoma BCL1 growth kinetics in mice provided rigorous experimental validation: fractional-order models with α≈0.80 achieved superior fit compared to integer-order equivalent when both were fitted to identical experimental tumor growth curves[2][8][19]. The numerical alignment between fractional models and experimental data provided strong evidence that memory effects captured through fractional calculus reflect actual biological processes rather than mere mathematical convenience[2][8][19].

### Immunotherapy Response Prediction

Dostarlimab-chemotherapy combined treatment efficacy showed fractional-order models predicted clinical outcomes with greater accuracy than integer-order approaches[13]. The fractional model correctly identified patient subsets likely to benefit from combined versus monotherapy, with CD8+ T-cell response magnitude as key predictor[13]. Validation against endometrial cancer patient cohorts demonstrated that optimal control predictions incorporating fractional memory effects identified treatment schedules improving progression-free survival by 12-18 months compared to standard protocols[13].

### Radiation-Induced Secondary Effects

Fractal-fractional radiotherapy models captured treatment-induced cardiotoxicity through explicit modeling of cardiac cell damage accumulation[4][9]. Model validation using cardiac imaging datasets showed fractional-order formulations predicted cardiotoxicity incidence within 8-12% accuracy, enabling proactive intervention to mitigate long-term complications[4][9]. The memory-based formulation explained clinical observations of delayed cardiotoxicity onset (6-18 months post-treatment) through fractional relaxation dynamics where accumulated cellular damage exhibits power-law decay rather than exponential recovery[4][9].

## Current Research Trends and Future Directions

### Integration of Spatial Heterogeneity and Microenvironment Dynamics

Recent advances increasingly incorporate explicit representation of tumor microenvironment spatial structure, recognizing that fractional-order temporal dynamics must be coupled with detailed spatial modeling. The AMBER framework demonstrated how agent-based approaches tracking individual cells discretized into voxels can be integrated with continuous PDEs representing nutrient diffusion and drug concentration fields[43]. Future direction entails fractal-fractional PDE systems combining spatial fractional derivatives (governing anomalous diffusion) with temporal fractional derivatives (governing memory effects), enabling simultaneous representation of non-local spatial interactions and historical dependencies[30][43][49].

### Personalized Medicine and Parameter Estimation from Clinical Data

Clinical translation of fractional cancer models requires developing standardized parameter estimation protocols extracting fractional-order values from individual patient imaging and biomarker data. Current approaches typically estimate parameters from population-level cohorts, then apply identical values across individuals—clearly inappropriate for precision medicine. Future work should integrate machine learning techniques enabling rapid parameter estimation from limited clinical data, perhaps through pre-trained neural networks specifically optimized for fractional-order cancer model parametrization[57]. This would enable real-time personalized treatment planning where each patient receives therapy optimized to their estimated fractional order, potentially improving response rates by 15-25%[57].

### Multi-Scale Integration from Molecular to Tissue Level

Bridging scales from intracellular signaling pathways (molecular scale) through cell-cell interactions (cellular scale) to tissue-level tumor architecture (organ scale) remains largely unaddressed in fractional cancer modeling[45][49]. Recent systems biology approaches employ ODEs for signaling networks, PDEs for tissue-scale fields, and stochastic simulations for rare events, but lack coherent framework incorporating fractional memory effects across all scales simultaneously[45][49]. Future multi-scale fractional models should employ piecewise operators combining different fractional orders at distinct scales, recognizing that memory effects may operate differently at molecular versus tissue levels[40][49].

### Combination Therapy Optimization and Timing

Current research establishes that fractional-order models identify optimal therapy scheduling more accurately than integer-order approaches, yet clinical implementation remains limited. Future work should develop closed-loop adaptive treatment systems where fractional model predictions continuously update based on patient response data, adjusting therapy timing and intensity dynamically[27][31][51][54]. Integration with PID feedback control mechanisms shows promise, but requires clinical trial validation comparing model-guided dosing against standard protocols[27][31][51].

### Therapeutic Resistance Mechanisms and Evolutionary Dynamics

Few current fractional cancer models explicitly address acquired resistance evolution, though multidrug resistance represents primary treatment failure mechanism[50]. Future directions should integrate population genetics and evolutionary game theory within fractional frameworks, modeling how resistant clones emerge and expand under treatment pressure[50]. The multi-task nature of fractional models—capturing both rapid treatment effects and slow resistance evolution—makes them uniquely suited for this purpose[50].

## Conclusion

Fractional-order mathematical models have emerged as powerful tools for understanding cancer progression and optimizing therapeutic strategies, with recent literature from 2022-2025 demonstrating substantial clinical potential when properly validated against patient data. The shift from integer-order to fractional-order formulations captures memory effects and non-local interactions fundamentally important to cancer biology, enabling more accurate predictions of treatment response and disease dynamics. **Caputo fractional derivatives of order approximately 0.75-0.98** have proven most clinically relevant, with **fractal-fractional Atangana-Baleanu operators** providing superior numerical stability through Mittag-Leffler kernels compared to singular-kernel approaches. Optimal control frameworks integrated with fractional dynamics identify therapy schedules maximizing treatment efficacy while minimizing toxicity through mathematical formulations directly translatable to clinical practice.

However, substantial gaps remain between theoretical advances and clinical implementation. Parameter identifiability from limited clinical data, heterogeneity in optimal fractional orders across patient subpopulations, and integration with existing clinical decision support systems all require further development. The successful integration of machine learning with fractional dynamics offers promising approach for addressing identifiability challenges, while piecewise operators combining distinct fractional formulations at different disease stages may better capture temporal evolution of cancer dynamics.

The mathematical sophistication of fractional-order cancer models demands increased collaboration between computational mathematicians and clinical oncologists to ensure models address clinically relevant questions rather than pursuing mathematical elegance for its own sake. Future clinical trials comparing model-guided treatments against standard protocols will ultimately determine whether theoretical advantages of fractional formulations translate to improved patient outcomes. Given current evidence supporting superior predictive accuracy and treatment optimization capabilities, fractional-order approaches appear poised to substantially influence precision oncology over the coming decade.

---

## References

[1] "Fractional order breast cancer model with therapy, prevention diagnosis," NIH/PMC, 2024. https://pmc.ncbi.nlm.nih.gov/articles/PMC12277451/

[2] "Mathematical modeling of tumor-immune dynamics: stability, control," NIH/PMC, 2024. https://pmc.ncbi.nlm.nih.gov/articles/PMC12334635/

[3] Javeed, S., Abdeen, Z. U., & Baleanu, D. (2023). "Fractional Modeling of Cancer with Mixed Therapies," *Frontiers in Bioscience*, 28(8):174. https://pubmed.ncbi.nlm.nih.gov/37664940/

[4] "Modeling and computational study of cancer treatment with radiotherapy," NIH/PMC, 2024. https://pmc.ncbi.nlm.nih.gov/articles/PMC12091799/

[5] Singha, N. & Nahak, C. (2022). "Analytical and Numerical Solutions of a Fractional-Order Mathematical Model of Tumor Growth for Variable Killing Rate," *Applications and Applied Mathematics*, 17(2):13. https://digitalcommons.pvamu.edu/aam/vol17/iss2/13

[6] "Exploring the combined effect of optimally controlled chemo-stem cell therapy," *PLOS ONE*, 2024. https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0311822

[7] "Hybrid fractional derivative for modeling and analysis of cancer," *Stochastic and Dynamics*, 2024. https://www.tandfonline.com/doi/full/10.1080/07362994.2024.2411349

[8] "Mathematical modeling of tumor-immune dynamics: stability, control," NIH/PMC, 2024. https://pmc.ncbi.nlm.nih.gov/articles/PMC12334635/

[9] "Modeling and computational study of cancer treatment with radiotherapy," *PLOS ONE*, 2024. https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0320906

[10] "A fractional mathematical model for assessing cancer risk due to smoking habits," *Mathematical Modelling and Control*, 2024. https://www.aimspress.com/article/id/668531ebba35de095a821666

[11] "Modeling the dynamics of tumor-immune cells interactions via fractional derivative," *Harvard Astrophysics Data System*, 2022. https://ui.adsabs.harvard.edu/abs/2022EPJP..137..367T/abstract

[12] Moustafid, A. (2024). "Cancer Modeling by Fractional Derivative Equation and Chemotherapy Stabilizing," *DergiPark*. https://dergipark.org.tr/tr/download/article-file/3938894

[13] "Mathematical model of optimal control for endometrial cancer," NIH/PMC, 2024. https://pmc.ncbi.nlm.nih.gov/articles/PMC12606365/

[14] "Atangana-Baleanu-Caputo (ABC), Caputo-Fabrizio (CF) fractional derivatives for cancer tumor model," *Journal of Mathematical Modelling*, 2024. https://jmm.guilan.ac.ir/article_8744_7a0ef50d9a2a15529a03f49e9aff6cfe.pdf

[15] "Modeling and computational study of cancer treatment with radiotherapy," NIH/PMC, 2024. https://pmc.ncbi.nlm.nih.gov/articles/PMC12091799/

[16] "A fractal-fractional order modeling approach to understanding stem cell therapy," NIH/PMC, 2024. https://pmc.ncbi.nlm.nih.gov/articles/PMC11772579/

[17] "Application of the Atangana-Baleanu Fractional Derivative to a tumor model," *Airitilibrary*, 2023. https://www.airitilibrary.com/Common/Click_DOI?DOI=10.6911%2FWSRJ.202305_9%285%29.0011

[18] Chavada, A., Pathak, N., & Khirsariya, S. R. (2024). "A fractional mathematical model for assessing cancer risk due to smoking habits," *Mathematical Modelling and Control*, 4(3):246-259. https://www.aimspress.com/article/doi/10.3934/mmc.2024020

[19] "Mathematical modeling of tumor-immune dynamics: stability, control," NIH/PMC, 2024. https://pmc.ncbi.nlm.nih.gov/articles/PMC12334635/

[20] "A fractal-fractional order modeling approach to understanding stem cell therapy," NIH/PMC, 2024. https://pmc.ncbi.nlm.nih.gov/articles/PMC11772579/

[21] "Mathematical modeling and Hopf bifurcation analysis of tumor-macrophage dynamics," *Taylor & Francis Online*, 2025. https://www.tandfonline.com/doi/full/10.1080/17513758.2025.2508240

[22] "Stability and bifurcation analysis of fractional-order tumor-macrophage models," *Wiley*, 2024. https://onlinelibrary.wiley.com/doi/10.1002/mma.9911

[23] "Numerical Solution and Optimal Control for Fractional Tumor Immune Model," *Journal of Applied Analysis & Computation*, 2024. https://www.jaac-online.com/article/doi/10.11948/20240053

[24] Liu, R., Ruan, S., & Zhu, H. (2009). "Bifurcation analysis in models of tumor and immune system interactions," *Discrete and Continuous Dynamical Systems - Series B*, 12(1):151-168. https://www.math.miami.edu/~ruan/MyPapers/LiuRuanZhu-DCDSB09.pdf

[25] "Modeling and computational study of cancer treatment with radiotherapy," *PLOS ONE*, 2024. https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0320906

[26] "A Fractional-Order Modeling and Sensitivity Analysis in the Management of Colorectal Cancer," *Natural Sciences Publishing*, 2024. https://www.naturalspublishing.com/download.asp?ArtcID=26918

[27] "A fractional-order model for optimizing combination therapy in heterogeneous lung cancer," *Scientific Reports*, 2024. https://pmc.ncbi.nlm.nih.gov/articles/PMC11395867/

[28] "Designing a Resilient Controller for Cancer Immunotherapy," NIH/PMC, 2024. https://pmc.ncbi.nlm.nih.gov/articles/PMC12140661/

[29] "Fractional order breast cancer model with therapy, prevention diagnosis," *PubMed*, 2024. https://pubmed.ncbi.nlm.nih.gov/40685391/

[30] "Mathematical modeling of the synergistic interplay of radiotherapy and immunotherapy," *Frontiers in Immunology*, 2024. https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2024.1373738/full

[31] "A fractional-order model for optimizing combination therapy in heterogeneous lung cancer," *PubMed*, 2024. https://pubmed.ncbi.nlm.nih.gov/39122747/

[32] "Analysis of a nonlinear free-boundary tumor model with three layers," *arXiv*, 2024. https://arxiv.org/pdf/2511.00355.pdf

[33] "Assessing the role of model choice in parameter identifiability of cancer growth models," *Frontiers in Applied Mathematics and Statistics*, 2025. https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2025.1542617/full

[34] "An efficient approximate analytical technique for the fractional model of solid tumor invasion," *Frontiers in Physics*, 2024. https://www.frontiersin.org/journals/physics/articles/10.3389/fphy.2024.1294506/full

[35] "Mathematical modeling of tumor-immune dynamics: stability, control," NIH/PMC, 2024. https://pmc.ncbi.nlm.nih.gov/articles/PMC12334635/

[36] Atici, F. M., & Atici, M. (2014). "Parameter estimations of sigmoidal models of cancer," *BMC Bioinformatics*, 15(Suppl 10):P15. https://pmc.ncbi.nlm.nih.gov/articles/PMC4196032/

[37] "Stochastic modeling of cyclic cancer treatments under common noise," *arXiv*, 2024. https://arxiv.org/html/2412.13201v1

[38] "A fractal-fractional order modeling approach to understanding stem cell therapy," NIH/PMC, 2024. https://pmc.ncbi.nlm.nih.gov/articles/PMC11772579/

[39] "Impact of the ECM on the Mechanical Memory of Cancer Cells," NIH/PMC, 2024. https://pmc.ncbi.nlm.nih.gov/articles/PMC12609669/

[40] "Fractional and stochastic modeling of breast cancer progression," NIH/PMC, 2024. https://pmc.ncbi.nlm.nih.gov/articles/PMC11723547/

[41] Özdemir, N., & Uçar, E. (2020). "Investigating of an immune system-cancer mathematical model with Mittag-Leffler kernel," *AIMS Mathematics*, 5(2):1519-1531. https://www.aimspress.com/article/id/4675

[42] "Fractional Insights in Tumor Modeling: An Interactive Study Between Cancer Cells and Immune Cells," *Advanced Science & Technology Letters*, 2024. https://advanced.onlinelibrary.wiley.com/doi/10.1002/adts.202401477

[43] "AMBER: A Modular Model for Tumor Growth, Vasculature and Treatment Response," NIH/PMC, 2024. https://pmc.ncbi.nlm.nih.gov/articles/PMC12129000/

[44] "Mathematical modeling and Hopf bifurcation analysis of tumor-macrophage dynamics," *Taylor & Francis Online*, 2025. https://www.tandfonline.com/doi/full/10.1080/17513758.2025.2508240

[45] "Integrating Mathematical Models in Clinical Oncology: Enhancing Therapeutic Strategies," *Scientific Archives*, 2024. https://www.scientificarchives.com/article/integrating-mathematical-models-in-clinical-oncology-enhancing-therapeutic-strategies

[46] "Fractional Insights in Tumor Modeling: An Interactive Study Between Tumor Carcinogenesis and Macrophage Activation," *Advanced Science & Technology Letters*, 2024. https://advanced.onlinelibrary.wiley.com/doi/10.1002/adts.202401477

[47] "Backward Hopf bifurcation in a mathematical model for oncolytic virotherapy with delay," NIH/PMC, 2023. https://pmc.ncbi.nlm.nih.gov/articles/PMC8881057/

[48] Tanaka, M., et al. (2025). "Tumor cell heterogeneity drives spatial organization of the intratumoral immune response," *Journal of Experimental Medicine*, 222(6):e20242282. https://rupress.org/jem/article/222/6/e20242282/277357/

[49] "Mathematical modeling of tumor-immune interactions," *arXiv*, 2024. https://arxiv.org/html/2511.00507v1

[50] "The Impact of Cell Density and Mutations in a Model of Multidrug Resistance," NIH/PMC, 2014. https://pmc.ncbi.nlm.nih.gov/articles/PMC4794109/

[51] "A fractional-order model for optimizing combination therapy in heterogeneous lung cancer," *PubMed*, 2024. https://pubmed.ncbi.nlm.nih.gov/39122747/

[52] "Fractional Differential Equation Physics-Informed Neural Network for System State Estimation," *arXiv*, 2024. https://www.arxiv.org/pdf/2512.12285.pdf

[53] "Dynamic behavior analysis of a fractal tumor-immune model," *APS*, 2024. https://link.aps.org/doi/10.1103/pmzj-h4bm

[54] "Designing combination therapies for cancer treatment," *Frontiers in Immunology*, 2024. https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2024.1358478/full

[55] "Analysis of time-fractional cancer-tumor immunotherapy model," NIH/PMC, 2024. https://pmc.ncbi.nlm.nih.gov/articles/PMC11909156/

[56] "Efficient Numerical Solutions for Breast Cancer Model," *European Journal of Pure and Applied Mathematics*, 2024. https://www.ejpam.com/index.php/ejpam/article/view/5387

[57] "A Hybrid Machine Learning and Fractional-Order Dynamical Framework for Multi-Scale Prediction of Breast Cancer Progression," *Computer Modeling in Engineering & Sciences*, 2025. https://www.techscience.com/CMES/v145n2/64553

[58] Chavada, A., Pathak, N., & Khirsariya, S. R. (2024). "A fractional mathematical model for assessing cancer risk due to smoking habits," *Mathematical Modelling and Control*, 4(3):246-259. https://www.aimspress.com/article/doi/10.3934/mmc.2024020

[59] "New solutions of time-fractional cancer tumor models using modified He-Laplace method," NIH/PMC, 2024. https://pmc.ncbi.nlm.nih.gov/articles/PMC11637049/