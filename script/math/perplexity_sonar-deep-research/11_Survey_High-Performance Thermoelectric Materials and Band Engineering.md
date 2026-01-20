# High-Performance Thermoelectric Materials and Band Engineering: Recent Advances and Strategic Design Approaches (2022-2025)

Recent advances in thermoelectric materials have achieved remarkable improvements in the figure of merit (ZT), with several material systems now demonstrating ZT values exceeding 3.0 through sophisticated band engineering and phonon management strategies[1][2][35]. The fundamental challenge of thermoelectric materials—achieving simultaneous enhancement of electrical conductivity and suppression of thermal conductivity—has been addressed through innovative approaches including lattice plainification, high-entropy engineering, topological band inversion, and multi-scale interface design[4][34]. This review synthesizes the most significant developments from 2022 to early 2026, focusing on the underlying mechanisms of band engineering strategies, their experimental validation, and the emerging paradigm of decoupling electron and phonon transport through material design. The confluence of advanced computational methods, high-throughput screening, and fundamental understanding of quantum materials has enabled researchers to move beyond incremental improvements toward transformative advances in thermoelectric efficiency for power generation and solid-state cooling applications.

## Fundamental Concepts and Mechanisms in Thermoelectric Band Engineering

### The Physics of Thermoelectric Figure of Merit and Transport Coefficients

The dimensionless thermoelectric figure of merit (ZT) is defined as \(ZT = \frac{S^2\sigma T}{\kappa}\), where S is the Seebeck coefficient, σ is electrical conductivity, T is absolute temperature, and κ is total thermal conductivity[3][6]. This formulation reveals the fundamental contradiction inherent to thermoelectric materials: conventional electrical conductors are also excellent heat conductors due to the Wiedemann-Franz relationship, which links electronic thermal conductivity (κₑ) directly to electrical conductivity through the Lorentz number. The power factor (PF), defined as \(PF = S^2\sigma\), represents the coupled electronic transport properties and must be optimized while simultaneously reducing lattice thermal conductivity (κₗ), which arises from phonon vibrations in the crystal structure. The Seebeck coefficient depends sensitively on the electronic density of states near the Fermi level, making band structure engineering critical for tailoring the thermoelectric response. Achieving optimal thermoelectric performance requires carrier concentration optimization, typically in the range of 10¹⁹ to 10²¹ cm⁻³, where the trade-offs between these competing parameters are most favorable[6][50].

The role of effective mass in determining thermoelectric performance has become increasingly nuanced through recent theoretical and experimental work. Materials with larger effective masses exhibit enhanced Seebeck coefficients at fixed carrier concentration, as the density-of-states effective mass (m*DOS) appears directly in the Seebeck coefficient expression. However, larger effective masses also reduce carrier mobility and thus electrical conductivity[3][6][55]. This apparent contradiction has spurred investigation into materials with multiple valleys in their electronic band structure, where each valley has a relatively light effective mass but the total density of states is enhanced by multiplying the contribution from many valleys. Band engineering strategies therefore aim to increase the number of conducting valleys (valley degeneracy) while maintaining favorable carrier transport properties[55].

### Valley Degeneracy and Band Convergence Strategies

Valley degeneracy, denoted as Nᵥ, represents the number of equivalent electronic valleys contributing to charge transport in a material. Topological insulators such as Bi₂Te₃ achieve exceptionally high valley degeneracy through strong spin-orbit coupling that causes band inversion and warping of the band structure[13]. The connection between band inversion strength and valley degeneracy has been elucidated through first-principles calculations showing that materials with strongly inverted bands exhibit higher warping and consequently greater valley degeneracy, yielding superior ZT values compared to weakly inverted or non-inverted systems[13]. Band convergence, another powerful strategy, involves aligning multiple valleys at the band extrema that would otherwise be separated in energy, thereby increasing the effective density of states while maintaining high mobility if proper doping is employed[55].

Recent comprehensive studies have demonstrated that successful band convergence requires careful optimization of alloy composition to balance the competing objectives of energy alignment and scattering rate management[6][55]. In materials such as PbTe and its derivatives, band convergence between the L and Σ valleys has been achieved through careful selection of dopants and alloying elements, leading to significant improvements in the Seebeck coefficient without proportional decreases in electrical conductivity[34]. The effectiveness of band convergence strategies depends critically on the strength of intervalley scattering; weak intervalley scattering allows multiple bands to contribute coherently to transport, while strong intervalley scattering may limit the benefits of convergence by preventing efficient carrier redistribution among the valleys[55].

## Band Engineering Strategies in Contemporary Thermoelectric Research

### Bismuth Telluride-Based Materials and Lattice Plainification

Bismuth telluride (Bi₂Te₃) remains the gold standard for room-temperature and near-room-temperature thermoelectric applications, being the only commercially viable thermoelectric material for large-scale deployment[2][17]. Despite decades of research, recent breakthroughs have extended the temperature range of high-performance Bi₂Te₃ through lattice plainification—a strategy that reduces defect scattering by systematically removing disorder from the crystal lattice while modulating electronic band structure through strategic doping[1][2][17]. Recent work demonstrating the incorporation of trace copper (Cu) into n-type Bi₂(Te,Se)₃ revealed that Cu atoms preferentially occupy bismuth vacancies, simultaneously weakening point defect scattering and modulating the relative energy positions of conduction band minima at different k-points in the Brillouin zone[17]. This approach achieved a peak ZT of approximately 1.3 at 300 K with an average ZT of 1.2 across the temperature range of 300–523 K, significantly outperforming prior high-performance n-type Bi₂Te₃ materials and approaching the performance of its p-type counterpart (Bi,Sb)₂Te₃[2][17].

The mass production of copper-doped Bi₂(Te,Se)₃ materials has been demonstrated on the kilogram scale with excellent uniformity, addressing a critical challenge for commercial deployment[17]. First-principles calculations revealed that copper incorporation increases the energy separation between the T and Γ points by approximately 0.10 eV compared to pristine Bi₂Te₃, effectively decoupling the conduction band extrema and modulating the band structure to enhance the Seebeck coefficient across multiple valleys[17]. Seven-pair thermoelectric devices constructed from optimized n-type BTS+0.2%Cu coupled with commercial p-type (Bi,Sb)₂Te₃ exhibited maximum cooling temperature differences (ΔTₘₐₓ) of approximately 85.6 K at a hot-side temperature of 343 K and conversion efficiencies of 6.4% for power generation under a temperature difference of 223 K, substantially exceeding commercial device performance[2]. These results underscore how systematic lattice engineering combined with strategic band structure modification can overcome the historical performance plateau of Bi₂Te₃-based thermoelectrics[2][17].

### Topological Band Inversion and Weyl Semimetals

Topological materials, characterized by inverted band structures stabilized by spin-orbit coupling, have emerged as a new frontier for thermoelectric applications[13][21]. The fundamental principle underlying topological thermoelectrics is that band inversion-induced warping of electronic bands leads to high valley degeneracy and complex electronic structures that can simultaneously support high Seebeck coefficients and reasonable electrical conductivity[13]. Bismuth telluride exemplifies this principle, with its strong spin-orbit coupling creating inverted band structures that produce warped bands with six-fold valley degeneracy at the band extrema, in stark contrast to materials like Bi₂Se₃ which exhibit only single-valley electronic structures despite also being topological insulators[13].

First-principles density functional theory calculations have revealed that the quality of band inversion—characterized as the energy separation between inverted band edges—directly correlates with the magnitude of band warping and the resulting valley degeneracy[13]. Materials exhibiting critical band inversion strength demonstrate maximum warping effects and optimal thermoelectric performance when properly doped. This insight has guided the rational design of new topological thermoelectrics beyond binary Bi-chalcogenides, extending to ternary compounds and more complex systems. Recent theoretical investigations of Weyl semimetals such as BaMnSb₂ and their derivatives have identified promising thermoelectric properties arising from low lattice thermal conductivity and anisotropic transport behavior enabled by the topological electronic structure[21]. The exploitation of topological states for thermoelectric applications remains an active frontier, with ongoing work to clarify optimal doping strategies and device configurations that leverage the unique properties of topologically protected surface states[13][21].

### High-Entropy Engineering for Enhanced Phonon Scattering

High-entropy engineering, the deliberate incorporation of multiple alloying elements to maximize compositional disorder while maintaining phase stability, has emerged as a transformative strategy for reducing lattice thermal conductivity to near-theoretical limits[23][20][34]. The underlying mechanism differs fundamentally from classical alloy theory: rather than scattering arising primarily from mass differences between constituent atoms (as predicted by Klemens theory), high-entropy materials exhibit dominant scattering from force constant disorder and charge disorder effects that create complex local chemical environments and extensive strain fields[23]. These mechanisms are particularly effective at scattering phonons across the entire frequency spectrum, from acoustic modes to high-frequency optical modes, thereby suppressing lattice thermal conductivity simultaneously across multiple phonon channels[23].

A landmark study of high-entropy GeTe alloys demonstrated that carefully optimized multielement doping (incorporating Au, Ag, Sb, Pb, and Bi) achieved ultralow lattice thermal conductivity of 0.22 W m⁻¹ K⁻¹ and a maximum ZT of 2.0 at 780 K[20]. The high-entropy approach proved particularly effective for GeTe, a material historically limited by high thermal conductivity and sensitivity to compositional variations. Computational analysis revealed that force constant disorder—arising from the interactions of multiple alloying elements with the GeTe host lattice—provides dominant contributions to phonon scattering, exceeding the effects of mass disorder alone[23]. The success of high-entropy GeTe motivated broader application of this strategy across different material families. For instance, high-entropy lead chalcogenides incorporating both cation and anion site engineering achieved peak ZT values exceeding 1.4 with excellent stability and reproducibility[51]. The integration of high-entropy engineering with other band structure strategies, such as strategic doping for carrier concentration control and defect engineering for enhanced scattering, has proven synergistic, yielding materials with unprecedented combinations of high power factor and low thermal conductivity[23][34].

### Interface Engineering and Topological Surface States

Interface engineering, encompassing strategies from grain boundary design to hybrid nanocomposite architectures and pseudosuperlattice construction, addresses the fundamental problem that charge carriers (electrons and holes) and heat carriers (phonons) scatter through different physical mechanisms at interfaces[1][34][55]. While grain boundaries and nanoscale interfaces strongly scatter phonons and thus reduce thermal conductivity, they frequently also scatter electrons and reduce electrical conductivity through the same barrier potentials. Strategic interface engineering, however, can exploit differences in electronic and phononic properties of distinct materials to preferentially reduce thermal conductivity while preserving or even enhancing electronic transport.

A seminal example involves hybrid materials combining Fe₂VTaAl alloy crystals with bismuth-antimony (BiSb) interlayers, where BiSb forms topological insulator phases with special electronic and phononic properties[1]. The lattice structures of the two materials are sufficiently different that phonon modes cannot transfer coherently across the interface, suppressing thermal transport by over 50% while the electronic band structures remain sufficiently similar that electrons encounter minimal additional scattering at interfaces. The topological insulator phase of BiSb contributes further by providing nearly dissipationless surface charge transport that enhances electronic conductivity despite the interface barriers[1]. This system achieved over 100% efficiency improvement compared to single-phase alternatives, demonstrating the power of deliberately engineering material combinations to decouple phonon and electron transport. The principle of interface engineering has been extended to pseudosuperlattice architectures, where thin layers of different materials are stacked in controlled sequences. Studies of n-type (Bi₂)ₓ(Bi₂Te₃)ᵧ pseudosuperlattice films revealed that interactions between layers induce electronic band structure modification and enhanced electron density through work function differences, while the layered structure provides multiple interfaces for phonon scattering[16]. The optimized (Bi₂)₁₂(Bi₂Te₃)₆ pseudosuperlattice achieved power factors of 1.27 mW m⁻¹K⁻², exceeding pristine Bi₂Te₃ and competing with the best nanostructured systems[16].

## Material Systems Demonstrating State-of-the-Art Performance

### Tin Chalcogenides and the Cmcm Phase Stabilization in SnSe

Tin selenide (SnSe) has attracted intense interest as a lead-free alternative to lead telluride with promising power generation capabilities, though historically limited by low electrical conductivity at room temperature and bipolar transport effects at elevated temperatures[35]. Recent breakthroughs exploiting the high-symmetry orthorhombic Cmcm crystal phase have demonstrated unprecedented performance, with peak ZT values reaching 3.0 at 748 K and average ZT of approximately 3.0 maintained over the broad temperature range of 673–923 K[35]. The key innovation involved lead alloying to simultaneously broaden the stability window of the Cmcm phase and enhance lattice symmetry, thereby enabling three-dimensional carrier transport while maintaining the favorable two-dimensional phonon scattering properties that make SnSe attractive. Specifically, 23% lead doping lowered the Cmcm phase transition temperature and enhanced lattice symmetry, boosting carrier mobility substantially without degrading the Seebeck coefficient[35]. Chlorine doping was employed to render the material n-type through shallow defect states. The resulting optimized SnSe crystals exhibited conversion efficiency approaching 19.1% under a temperature difference of 572 K, competitive with or exceeding the efficiency of state-of-the-art thermoelectric device modules[35].

The success of SnSe exemplifies a broader principle emerging in contemporary thermoelectrics: leverage of structural phase transitions and crystal symmetry modifications to simultaneously optimize electronic and thermal transport[35]. The Cmcm phase of SnSe features more isotropic crystal structure compared to the lower-symmetry Pnma phase, facilitating three-dimensional electronic transport while the layered bonding still provides phonon localization. This interplay of crystal structure and transport properties demonstrates the fundamental importance of crystallographic design in achieving record thermoelectric performance.

### Skutterudite and Half-Heusler Materials for Mid-to-High Temperature Applications

Skutterudite compounds, particularly rare-earth-filled CoSb₃, continue to demonstrate exceptional performance at intermediate and high temperatures (600–900 K), making them ideal for waste heat recovery from industrial processes[3][7]. Recent developments in Yb-filled CoSb₃ have established fast one-step fabrication routes that dramatically reduce processing time while improving mechanical properties and achieving consistent ZT values exceeding 1.12 at 765 K[7]. The incorporation of ytterbium simultaneously optimizes the power factor through band structure engineering while suppressing thermal conductivity through resonant scattering effects and all-scale hierarchical defect structures. The enhanced mechanical properties—Young's modulus of 171.4 GPa and hardness of 8.8 GPa—make these materials practical for module integration. Theoretical studies have attributed the high thermoelectric performance of Yb-filled skutterudites to band convergence effects where multiple carrier pockets at the band extrema contribute coherently to transport, combined with the rattling behavior of the filler atom that scatters phonons across a broad frequency range[7][10].

Half-Heusler alloys based on TaFeSb represent another material class achieving ZT values exceeding 1.2 through sophisticated alloying strategies[8]. The fundamental challenge with TaFeSb is the narrow bandgap and associated bipolar transport at elevated temperatures. Recent work systematically optimized the composition through vanadium and hafnium codoping, achieving peak ZT of 1.20 at 1025 K[8]. The alloying strategy enhanced the power factor substantially through band structure modification while reducing lattice thermal conductivity by 65% at room temperature compared to pristine TaFeSb through mass and strain field fluctuations induced by the diverse alloying elements[8]. These half-Heusler systems are particularly attractive for high-temperature applications above 800 K where conventional Bi-chalcogenide thermoelectrics lose efficiency due to band edge broadening from increased carrier excitation[8].

### Lead Telluride Derivatives and Defect Engineering

Lead telluride (PbTe) and its alloys represent the prototypical system for understanding how defect engineering enables thermoelectric optimization[14][34]. The appeal of PbTe lies in its relatively large bandgap (approximately 0.32 eV), which suppresses minority carrier excitation and extends the useful temperature range to 850 K, combined with excellent intrinsic phonon scattering properties that yield naturally low thermal conductivity[14]. Contemporary studies emphasize that the engineering of point defects through stoichiometric tuning and strategic doping can simultaneously enhance electronic transport through band engineering and suppress thermal transport through phonon scattering[50]. Recent high-entropy variants of lead chalcogenides incorporating multiple dopants achieve ZT values exceeding 1.4 through the synergistic combination of entropy-induced lattice disorder and rational carrier concentration control[51]. The integration of anion doping (such as bromine) with cation engineering demonstrates the importance of multiscale optimization of defect chemistry[51].

## Phonon Engineering and Thermal Transport Reduction

### Multidimensional Defect Scattering Architecture

The fundamental strategy for reducing lattice thermal conductivity without proportionally degrading electrical conductivity exploits the different wavelengths of phonons and electrons at the Fermi level[34][50][55]. Electrons at the Fermi level have de Broglie wavelengths of order 1–10 nm, while phonons contributing to thermal transport range from extremely short wavelength (high-frequency optical phonons with wavelengths of 1 Å) to macroscopic wavelength (low-frequency acoustic phonons with wavelengths of microns)[34][55]. By engineering defects across multiple length scales—from point defects scattering short-wavelength phonons, to nanoscale precipitates scattering intermediate wavelengths, to grain boundaries and interfaces scattering long-wavelength acoustic phonons—researchers can suppress the entire phonon spectrum while maintaining relatively weak scattering for the shorter-wavelength electrons[34][55].

Computational studies utilizing phonon transport calculations have demonstrated the spectral dependence of phonon scattering: point defects are most effective for high-frequency optical modes, dislocations and extended defects are effective for intermediate frequencies, and grain boundaries and interfaces scatter the long-wavelength acoustic modes that typically dominate thermal conductivity at high temperatures[34][55]. Experimental validation through thermal conductivity measurements of samples with deliberately engineered hierarchical microstructures confirms these theoretical predictions. For instance, samples designed with combined nanostructuring and grain boundary engineering exhibit thermal conductivity reductions of 30–50% compared to coarse-grained samples, with electrical conductivity reduced by only 10–20%, yielding net ZT improvements of 50–100%[34][55].

### Anharmonic Phonon Dynamics and Overdamped Modes

Recent advances in computational phonon spectroscopy have revealed that strong anharmonicity in certain materials creates overdamped phonon modes where phonons lose their well-defined quasiparticle character and participate in thermal transport through incoherent processes[39][42]. Copper bismuth iodide (CuBiI₄) exemplifies this extreme regime, where three-phonon scattering mechanisms are so strong that phonon lifetimes become extremely short, yet the lattice thermal conductivity remains well-defined and substantially reduced compared to purely harmonic predictions[42]. The self-consistent phonon theory combined with Wigner transport formalism reveals that even overdamped modes contribute coherent thermal transport channels, necessitating modifications to conventional Boltzmann transport theory that assumes well-defined phonon quasiparticles[42]. This deeper understanding of anharmonic phonon dynamics has implications for designing materials with intrinsically low thermal conductivity through deliberate engineering of materials chemistry to promote strong anharmonic coupling.

Neutron scattering studies have provided experimental validation of the complex phonon dynamics in high-performance thermoelectrics, revealing anomalous phonon damping and band renormalization effects that contribute to low thermal conductivity[19]. The phonon properties of classic thermoelectric materials such as PbTe, SnTe, GeTe, and AgSbTe₂ exhibit common features including softer lattice modes, strong electron-phonon coupling, and phase transitions that modulate thermal transport across operating temperature ranges[19]. Understanding these phonon properties through scattering-based experimental probes has guided material optimization strategies that leverage natural anharmonicity rather than fighting against it[19].

### Resonant Scattering and Rattling Behavior

Rattling—the localized rattling motion of loosely bound atoms within crystal cages—has long been recognized as an effective mechanism for suppressing thermal transport while maintaining electronic properties[34][55]. The classic example is the guest-host interaction in filled skutterudites and half-Heuslers, where rare-earth atoms occupy cage structures and undergo anharmonic vibrations that scatter phonons resonantly. Recent computational and experimental work has clarified that the effectiveness of rattling depends on proper tuning of the vibrational frequencies to overlap with the acoustic phonon spectrum where most heat is carried[34][55]. Resonant doping, an extended concept where impurity atoms introduce resonant energy levels or midgap states in the electronic structure, can simultaneously enhance the Seebeck coefficient through increased density of states near the Fermi level while inducing phonon resonance scattering[26][34].

## Device Engineering and Conversion Efficiency

### Segmented Device Architecture and Temperature-Dependent Optimization

Contemporary high-performance thermoelectric devices exploit the temperature dependence of optimal ZT in different materials to construct segmented thermoelectric modules combining multiple material systems, each optimized for different portions of the temperature gradient[3][4]. A record-high thermoelectric efficiency of 16% has been achieved through finite element analysis optimization of device geometry combined with strategic segmentation using materials such as Ge₁₋ₓ₋ᵧCrₓSbᵧTe alloys[3]. The principle underlying segmented devices is that different materials achieve maximum ZT at different temperatures; by combining these materials in series along the temperature gradient, the overall device can maintain high efficiency across the entire operating range rather than being limited by the single material with the highest average ZT[3][4].

Recent integration of optimized materials with device design reveals that small improvements in ZT translate to substantial increases in conversion efficiency when coupled with careful attention to thermal and electrical contact resistances[2][17]. Seven-pair thermoelectric generators constructed from optimized n-type Bi₂(Te,Se)₃ doped with copper and commercial p-type (Bi,Sb)₂Te₃ demonstrate the practical viability of achieving high conversion efficiency through combined materials and device optimization[2].

### Cooling Capability and Thermoelectric Module Performance

Solid-state cooling using thermoelectric devices offers advantages over conventional refrigeration including absence of moving parts, silent operation, and precise temperature control[2][17]. Recent advances demonstrating maximum cooling temperature differences (ΔTₘₐₓ) of approximately 85.6 K at a hot-side temperature near room temperature (343 K) represent substantial improvements over prior commercial devices, opening new application niches in precision cooling and localized thermal management[2]. The cooling capability depends sensitively on the temperature dependence of ZT and other transport properties; materials with stable, high ZT across broad temperature ranges (such as lead-free SnSe and optimized Bi₂(Te,Se)₃) enable more effective cooling across temperature differences of practical interest[2][35].

## Computational and Machine Learning Approaches to Materials Discovery

### First-Principles Prediction of Transport Properties

Computational materials discovery using density functional theory and Boltzmann transport theory has accelerated the identification of promising thermoelectric candidates and the optimization of existing systems[3][4][29][34]. Energy-dependent relaxation time approximations that include both electron-phonon scattering and ionized impurity scattering provide more accurate predictions of transport properties compared to simplified constant relaxation time approaches[29]. The computational framework combining electronic structure calculation (DFT), phonon properties (density functional perturbation theory), and linearized Boltzmann transport equation solving has been benchmarked against experimental results for materials ranging from elemental semiconductors to complex multicomponent Zintl phases[29][34].

Recent applications of these computational methods to cubic GeTe revealed the intricate interplay between chemical bonding (characterized through projected density of states and crystal orbital Hamilton population analysis) and thermoelectric properties[29]. Different doping elements were found to exhibit distinct bonding characters: bismuth, antimony, and lead doping (which are isoelectronic to germanium) maintain relatively weak s-p interactions that preserve high mobility, while indium doping (which introduces resonant energy levels) creates stronger s-p interactions that enhance the Seebeck coefficient but reduce mobility[29]. These detailed computational insights guide rational doping strategy selection and explain the experimental observation of structure-property relationships.

### Machine Learning for Inverse Design and Property Prediction

Machine learning approaches have emerged as powerful tools for navigating the vast compositional space of potential thermoelectric materials and predicting optimal doping and alloying strategies[44][47]. Kolmogorov-Arnold Networks (KANs), a novel neural network architecture, demonstrate superior interpretability compared to conventional multilayer perceptrons while maintaining competitive predictive accuracy for both Seebeck coefficient and bandgap[44]. The key advantage of KANs is their ability to generate explicit symbolic representations of structure-property relationships, enabling identification of critical descriptors and physical mechanisms governing thermoelectric behavior. Benchmarking against multilayer perceptrons reveals that KANs avoid physically inconsistent predictions (such as sign inversions in the Seebeck coefficient) that plague conventional deep learning approaches when extrapolating to chemically complex regions[44].

High-throughput screening combining machine learning predictions with experimental validation has accelerated discovery cycles by 40–70% compared to conventional trial-and-error approaches, with particular success in narrow-bandgap semiconductors and complex Zintl phases[47]. The integration of physically-informed machine learning architectures that incorporate constraints from thermoelectric transport theory enhances reliability and enables more confident prediction of material behavior under diverse operating conditions[47]. Recent work constructing datasets of 3,000 thermoelectric materials covering eight major material families enables development of generalizable ML models that can predict properties across chemically diverse systems[47].

## Emerging Material Classes and Future Directions

### Lead-Free Alternatives and Eco-Friendly Thermoelectrics

The environmental and toxicity concerns associated with lead-containing thermoelectrics have motivated intensive research into lead-free alternatives including tin chalcogenides (SnTe, SnSe, SnS), germanium-based compounds, Zintl phases, and organic-inorganic perovskites[34][37][43][46][47]. Tin selenide (SnSe) has emerged as particularly promising, achieving record ZT values of approximately 3.0 through the strategies discussed above[35]. Lead-free halide double perovskites (A₂B'B"X₆ composition) offer another promising avenue, combining environmental friendliness with structural and compositional flexibility that enables band engineering and defect control[43][46]. The optimization of these emerging materials through high-throughput screening and machine learning is currently underway, with predictions of commercially viable lead-free thermoelectrics becoming increasingly realistic[47].

Zintl phase compounds, intermetallic semiconductors with complex crystal structures, have demonstrated exceptional thermoelectric performance through naturally optimized electronic structures featuring multiple valleys and intrinsic point disorder[31][37][40]. Recent optimization of Yb-substituted calcium-zinc-antimony systems through combined cation and anion doping achieved synergistic enhancement of electrical conductivity while maintaining low thermal conductivity[31]. These systems appeal to researchers as alternatives to lead-containing compounds while maintaining performance competitive with conventional materials[31][37][40].

### Topological Surface States and Spin-Related Phenomena

The connection between topological states and thermoelectric properties offers new opportunities for enhancing the Seebeck coefficient and power factor through spin-related effects[13][21][60]. Spin Seebeck effect, magnon drag, and paramagnon drag effects are emerging as complementary mechanisms for temperature-gradient-driven charge generation beyond the conventional Seebeck effect[60]. Magnetic doping strategies have demonstrated surprising effectiveness for enhancing thermoelectric properties; incorporation of magnetic elements such as chromium and iron into high-entropy PbSnTeSe alloys increased ZT from 1.0 to 1.6 through enhanced Seebeck coefficients arising from flat band structures created by magnetic impurity states near the Fermi level[26][41]. These findings challenge conventional understanding and suggest that magnon-electron interactions and spin entropy effects deserve greater attention in thermoelectric materials design[38][41][60].

## Characterization Techniques and Structural Validation

### Advanced Spectroscopic Probes of Electronic Structure

Angle-resolved photoemission spectroscopy (ARPES) has become an essential tool for validating band engineering strategies and directly measuring the electronic structures of high-performance thermoelectrics[16][56][59]. Time-resolved ARPES enables investigation of out-of-equilibrium electronic dynamics, revealing electron-phonon coupling strengths and scattering rates that govern transport properties[59]. Direct visualization of band warping, valley convergence, and topological surface states provides experimental validation of theoretical band structure predictions and guides optimization of material compositions[16][56].

The combination of ARPES with other advanced techniques including X-ray absorption spectroscopy, scanning tunneling microscopy, and resonant photoemission spectroscopy provides complementary information about the local chemical environment, occupancy of specific atomic sites, and spatial distribution of electronic states[16][56]. These multimodal characterization approaches have been critical for understanding the microscopic origins of high thermoelectric performance in complex materials with many atomic sites and diverse bonding environments.

### Thermal Transport Characterization

Time-domain thermoreflectance and other ultrafast thermal measurement techniques provide information about phonon transport at timescales and length scales inaccessible to conventional steady-state thermal conductivity measurements[25][39]. These techniques reveal the contributions of different phonon modes to thermal transport and enable direct measurement of phonon-interface interactions in nanostructured materials and heterostructures[25]. The combination of these ultrafast measurements with steady-state thermal conductivity data and phonon spectroscopy (neutron scattering) provides a comprehensive view of thermal transport across the full spectrum of phonon frequencies and wavelengths[19][25].

## Critical Evaluation of Current State and Remaining Challenges

### Trade-offs Between Competing Design Objectives

Despite remarkable progress, thermoelectric material optimization remains fundamentally constrained by competing physical principles that resist simultaneous optimization[4][34]. Strategies that enhance the Seebeck coefficient through increased density of states near the Fermi level frequently reduce electrical conductivity through shortened carrier lifetimes or increased disorder scattering. Interface engineering approaches that reduce thermal conductivity through phonon scattering often also reduce electrical conductivity, though careful design can mitigate this effect. The bipolar transport problem—where thermal excitation of minority carriers at high temperatures creates opposing contributions to the Seebeck coefficient and enhanced thermal conductivity—fundamentally limits the maximum achievable ZT in materials with narrow bandgaps[14][57].

Systematic optimization of doping and alloy composition remains challenging despite advances in computational screening and machine learning. The vast compositional space of potential materials, combined with non-linear interactions between different doping elements and their temperature-dependent effects, requires either comprehensive experimental mapping (expensive and time-consuming) or reliable predictive models (still under development)[47]. Materials designed to exhibit exceptional ZT at one temperature often show degraded performance at others, necessitating either temperature-dependent optimization strategies or segmented device architectures[3][4].

### Stability and Degradation in Operating Conditions

Chemical stability and mechanical reliability under the temperature gradients and thermal cycling inherent to device operation represent critical but sometimes overlooked challenges[3][34]. Some of the highest-ZT materials exhibit instability during thermal cycling, phase segregation under operating conditions, or reaction with contact materials, limiting practical device lifetimes[34]. Recent work emphasizing lattice plainification and defect control has shown promise for enhancing stability while improving thermoelectric performance, but systematic evaluation of long-term stability across diverse operating conditions remains incomplete[17][34].

## Conclusions and Future Perspectives

The field of high-performance thermoelectric materials has undergone a transformation from incremental improvements in conventional systems toward fundamental restructuring of material design principles through advanced band engineering, phonon management, and interface control. The achievement of ZT values exceeding 3.0 in SnSe, sustained ZT above 1.2 in commercializable Bi₂(Te,Se)₃ systems, and demonstration of conversion efficiencies approaching 20% represent genuine advances beyond the historical performance plateau. The convergence of sophisticated computational methods, high-throughput screening, advanced characterization techniques, and deeper theoretical understanding has enabled researchers to move beyond empirical optimization toward rational design of thermoelectric materials.

Looking forward to 2025 and beyond, three dominant trends are likely to shape thermoelectric research. First, the continuing development of lead-free and environmentally benign alternatives will accelerate as regulatory pressures increase and process costs for tin-based and other emerging systems decrease. Machine learning integration will play a central role in this transition, enabling rapid screening of vast compositional spaces for optimal lead-free candidates[47]. Second, the integration of topological electronic structures, spintronic effects, and magnon-based mechanisms promises fundamentally new pathways for enhancing the Seebeck coefficient and power factor beyond conventional strategies, potentially enabling ZT values above 2.0 in room-temperature systems[13][21][38][41][60]. Third, sophisticated device engineering combining multiple optimized material systems with advanced thermal and electrical interface design will become increasingly important, as improvements in individual materials plateau and further efficiency gains require integrated system optimization[3][4][35].

The commercialization of high-performance thermoelectrics depends not only on achieving high ZT values but on demonstrating practical device reliability, scalable synthesis routes, and cost-effective manufacturing. Recent breakthroughs in mass production of optimized Bi₂(Te,Se)₃ materials and fast fabrication routes for skutterudites have reduced barriers to commercialization[2][7][17]. The emergence of additive manufacturing approaches for thermoelectric generators offers potential for customized device configurations and reduced waste. Integration of thermoelectric power generation with industrial waste heat recovery and mobile device thermal management represents substantial market opportunities that will likely accelerate materials optimization and device development through the remainder of the decade.

---

## References

[1] Garmroudi, F., et al. "New hybrid materials as efficient thermoelectrics." *Nature Communications*, 2021. doi: 10.1038/s41467-021-[CITATION WITHHELD]. *ScienceDaily*, 2025. Accessed April 17, 2025.

[2] Liu, D., et al. "Lattice plainification and band engineering lead to high thermoelectric cooling and power generation in n-type Bi₂Te₃ with mass production." *National Science Review*, vol. 12, no. 2, 2025, article nwae448.

[3] Zhu, J., et al. "Recent trends and future perspectives of thermoelectric materials and their applications." *Nature Reviews Materials*, 2024.

[4] Ming, H., Luo, Z.-Z., Zou, Z., & Kanatzidis, M. G. "Strategies and Prospects for High-Performance Te-Free Thermoelectric Materials." *Chemical Reviews*, vol. 125, no. 7, 2025, pp. 3932–3975.

[5] OpenAccess OAE Publishing. "Lattice plainification and band engineering lead to high thermoelectric cooling." *NIH/PMC*, 2024.

[6] Li, G., et al. "Strategies to Improve the Thermoelectric Figure of Merit in Thermoelectric Materials." *Frontiers in Chemistry*, vol. 10, 2022, article 865281.

[7] Zhou, M., et al. "Fast Fabrication of High-Performance CoSb₃-Based Thermoelectric Generators." *Advanced Functional Materials*, vol. 33, no. 24, 2023, article 202305269.

[8] Luo, P., Lin, C., Li, Z., Zhang, J., & Jun Luo. "TaFeSb-Based Half-Heusler Thermoelectrics with High zT > 1 through the Alloying Effect." *ACS Applied Energy Materials*, vol. 6, no. 19, 2023, pp. 10070–10077.

[9] "High Thermoelectric Performance in SnTe–AgSbTe₂ Alloys." *ACS Energy Letters*, 2018.

[10] "A Chemical Understanding of the Band Convergence in N-Type Skutterudites." *ACS Chemistry of Materials*, 2016.

[11] "Enhanced thermoelectric performance by Hf substitution in p-type half-Heusler TiNi₀.₈Co₀.₂Sn." *Applied Physics Letters*, vol. 126, no. 13, 2025, article 133903.

[12] "High Thermoelectric Performance and Energy Conversion in Hg-doped GeTe." *Advanced Functional Materials*, 2024.

[13] "Are topological insulators promising thermoelectrics?" *Materials Horizons*, RSC Publishing, 2024.

[14] "Thermoelectric Materials Based on Lead Telluride and Prospects." *International Journal of Physical Research and Applications*, 2024.

[15] "Organic–Inorganic Hybrid Perovskite for Ferroelectric Catalysis." *Advanced Materials*, 2024.

[16] Ouyang, Y., et al. "Interactions between Functional Units Inducing Evolution of Electronic Band Structure in n-Type (Bi₂)ₓ(Bi₂Te₃)ᵧ Pseudosuperlattices." *ACS Applied Energy Materials*, vol. 7, no. 11, 2024, article 4c02549.

[17] Liu, D., et al. "Lattice plainification and band engineering lead to high thermoelectric cooling and power generation in n-type Bi₂Te₃." *National Science Review*, 2025, NIH/PMC.

[18] "Unraveling rare ferroelectric-antiferroelectric transitions in 2D organic-inorganic hybrid perovskites." *Physical Review Letters*, 2025.

[19] Zhu, J., Shen, X., Ding, J., et al. "Revealing the phonon properties for thermoelectric materials by neutron scattering." *The Innovation Energy*, vol. 1, no. 4, 2024, article 100049.

[20] Chen, H., et al. "Investigating Thermoelectric Properties of GeTe Alloys with High-Entropy Engineering." *ACS Omega*, 2025.

[21] Chen, Y., Jin, R., Liao, B., & Mu, S. "Thermoelectric transport in Weyl semimetal: A first-principles study." *Physical Review Materials*, vol. 8, 2024, article 085401.

[22] "Unique Semi-Coherent Nanostructure Advancing Thermoelectrics." *Advanced Functional Materials*, 2024.

[23] "Revisiting thermoelectrics with high-entropy design." *Materials Chemistry Frontiers*, RSC Publishing, 2025.

[24] Guo, L.W., & Wang, C.M. "Thermoelectric transport of the coexistence topological semimetal in the quantum limit." *arXiv*, 2024, article 2403.06603.

[25] Shan, S., et al. "Generation of interfacial phonon modes and their contribution to thermal transport." *Physical Review B*, vol. 112, 2025, article 155302.

[26] Kim, S., et al. "Enhanced Thermoelectric Performance by Resonant Doping and Embedded Magnetic Impurity." *Physical Review Applied*, vol. 19, 2023, article 014034.

[27] Fava, M., Lafargue-Dit-Hauret, W., Romero, A.H., & Bousquet, E. "Ferroelectricity and chirality in the crystal." *Physical Review B*, vol. 109, 2024, article 024113.

[28] "Advancing Superconductivity with Interface Engineering." *Advanced Materials*, 2024.

[29] "The interplay of chemical bonding and thermoelectric properties in cubic GeTe." *Royal Society of Chemistry*, vol. 12, 2024, article d4ta01088d.

[30] "Sliding-driven symmetry breaking induced ferroelectric polarization." *Applied Physics Letters*, 2025.

[31] "Synergistic effect of cation substitution and p-type anion doping in Zintl phases." *Energy Materials*, vol. 5, 2025, article 500123.

[32] "Fully 3D Printed Tin Selenide Thermoelectric Generators." *ACS Applied Materials & Interfaces*, 2023.

[33] "Enhanced thermoelectric performance in AgSbTe₂ with grain boundary trapping states." *Applied Physics Letters*, vol. 126, no. 8, 2025, article 083902.

[34] Ming, H., Luo, Z.-Z., & Zou, Z. "Strategies and Prospects for High-Performance Te-Free Thermoelectric Materials." *Chemical Reviews*, vol. 125, no. 7, 2025, pp. 3932–3975.

[35] Gao, et al. "Extending the temperature range of the Cmcm phase of SnSe for high thermoelectric performance." *Science*, 2024, article adt0831.

[36] "High-Performance AgSbTe₂ Thermoelectrics: Comprehensive Review." *Advanced Materials*, 2024.

[37] "Promising High Temperature Thermoelectric Performance of Alkali Metal-Based Zintl Phases." *ACS Applied Energy Materials*, 2025.

[38] "Unexpected p-type thermoelectric transport arising from magnetic doping." *Journal of Materials Chemistry A*, RSC Publishing, 2024.

[39] Dangić, Đ., et al. "Lattice thermal conductivity in the anharmonic overdamped regime." *Physical Review B*, vol. 111, 2025, article 104314.

[40] "Complex Structural Disorder in Thermoelectric Zintl Phases." *Zeitschrift für Anorganische und Allgemeine Chemie*, vol. 550, 2025, article 202500070.

[41] Xia, M., Boulet, P., & Record, M.-C. "Influence of magnetic Cr and Fe doping on thermoelectric performance in PbSnTeSe high-entropy alloy." *Physical Review B*, vol. 111, 2025, article 045149.

[42] "Anharmonic Phonon Dynamics and the Origin of Ultralow Lattice Thermal Conductivity in CuBiI₄." *Chinese Physics Letters*, vol. 42, no. 12, 2024, article 120702.

[43] "Eco-friendly lead-free halide double perovskites A₂CuMCl₆." *Journal of Materials Chemistry A*, RSC Publishing, 2024.

[44] Cirone, P., et al. "Interpretable Machine Learning for Thermoelectric Materials Design Using Kolmogorov-Arnold Networks." *arXiv*, 2025, article 2510.02681.

[45] Onishi, Y., & Fu, L. "Fundamental Bound on Topological Gap." *Physical Review X*, vol. 14, 2024, article 011052.

[46] Ahmad, B., et al. "Lead-Free Double Perovskites: A Review of Structural and Optoelectronic Properties." *Crystals*, vol. 14, no. 1, 2024, article 86.

[47] Tiryaki, et al. "Machine learning for predictive design and optimization of high-performance thermoelectric materials." *Energy Materials*, 2025, article jmi.2025.18.

[48] "Detecting Band Inversions in Topological Insulators with Diffusion Quantum Monte Carlo." *APS March Meeting*, 2024.

[49] "Effect of self-assembled 3D flower-like hierarchical architecture on thermoelectric properties." *RSC Advances*, vol. 4, 2024, article d4ra04467c.

[50] "Defects Engineering with Multiple Dimensions in Thermoelectric Materials." *Science Partner Journal*, vol. 2020, 2020, article 9652749.

[51] "Synergistic engineering of atomic disorder and porous architectures for enhanced thermoelectric performance." *Journal of Materials Chemistry A*, 2025, article d5ta02340h.

[52] "High Thermoelectric Performance in SnTe Nanocomposites with All-Scale Hierarchical Architectures." *ACS Applied Materials & Interfaces*, 2020.

[53] Ahmad, B., Limon, M.S.R., & Ahmad, Z. "Modulation of point defect properties near surfaces in metal halide perovskites." *Physical Review Materials*, vol. 8, 2024, article 125402.

[54] "Confined Dynamic and Static Disorder Realized by Entropy." *Advanced Materials*, 2025, article 202511464.

[55] "Phonon and electron transport engineering for enhanced thermoelectric performance." *Energy Materials*, vol. 5, 2025, article energymater.2025.32.

[56] Mo, S.-K., et al. "Advances in Angle-Resolved Photoemission Spectroscopy." *Synchrotron Radiation News*, vol. 37, no. 5, 2024, pp. 21–45.

[57] "Doping optimization for the power factor of bipolar thermoelectric semiconductors." *arXiv*, 2019, article 1901.04718.

[58] "Hot phonon bottlenecks and the role of non-equilibrium acoustic phonons." *Applied Physics Letters*, vol. 127, no. 16, 2025, article 162101.

[59] Boschini, F., Zonno, M., & Damascelli, A. "Time-resolved ARPES studies of quantum materials." *Reviews of Modern Physics*, vol. 96, 2024, article 015003.

[60] "Evolving Strategies Toward Seebeck Coefficient Enhancement in Thermoelectric Materials." *Accounts of Materials Research*, vol. 4, no. 5, 2023, pp. 448–456.