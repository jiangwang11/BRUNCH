# Advancements and Applications of Generative Adversarial Networks (2022-2025): A Comprehensive Review

Generative Adversarial Networks have undergone substantial evolution between 2022 and 2025, transitioning from primarily theoretical innovations toward concrete clinical and industrial applications across medical imaging, video synthesis, 3D generation, and domain-specific data augmentation. This comprehensive review synthesizes recent developments across multiple GAN architectures and applications, identifying that the field has achieved significant breakthroughs in training stability, output fidelity, and scalability through innovations such as progressive growing strategies, improved loss functions, and integration with complementary generative approaches like diffusion models. Our analysis reveals convergence toward hybrid architectures combining GANs with transformers and diffusion frameworks, particularly for video and high-dimensional content generation, while simultaneously witnessing the emergence of specialized GAN variants addressing challenges in medical imaging, temporal data synthesis, and adversarial robustness.

## Architectural Innovations and Theoretical Advances

### Evolution of Training Stability and Loss Functions

The persistent challenge of training instability in GANs has been substantially addressed through refined mathematical formulations and regularization techniques. Wasserstein GANs represent a critical theoretical contribution, introducing the Wasserstein distance as a replacement for Jensen-Shannon divergence, which provides a continuous and differentiable measure between distributions enabling stable gradient descent throughout training[25]. The mathematical foundation leverages the Kantorovich-Rubinstein duality, fundamentally addressing mode collapse through weight clipping constraints that ensure critic functions remain in compact spaces. Empirically, WGANs demonstrate significantly improved convergence properties where the critic can be trained to optimality without inducing discriminator overfitting, a property absent in traditional GAN formulations[28].

Building upon these theoretical foundations, more recent work has developed regularized training objectives combining relativistic pairing GAN losses with zero-centered gradient penalties, demonstrating mathematical guarantees of local convergence equivalent to regularized classical GANs[44]. This modern baseline GAN architecture achieves competitive performance against state-of-the-art diffusion models and StyleGAN variants across benchmark datasets including FFHQ (256×256) and ImageNet, with comparable or superior Fréchet Inception Distance scores despite reduced parameter counts. The key innovation involves applying zero-centered gradient penalties to enforce balanced gradient norms on both real and generated data, reducing discriminator overfitting and enabling convergence without manual hyperparameter tuning tricks that historically plagued GAN training[44].

### Progressive Training and High-Resolution Synthesis

Progressive Growing GANs address the fundamental instability of directly training high-resolution generators by incrementally increasing network capacity and image resolution throughout training[13]. This methodology begins with 4×4 resolution images and progressively adds new layers to reach 1024×1024 pixels, allowing generators to initially capture coarse features before progressively refining details. When combined with Wasserstein GANs and gradient penalty regularization (WPGGAN-GP), this approach achieves 1024×1024 resolution facial synthesis with Sliced Wasserstein Distance of 0.026 between real and synthetic distributions, passing Turing tests with 15 expert observers assessing 100 images (50 real, 50 synthetic) with accuracy approaching 95% discrimination threshold[31].

The practical implementation in medical imaging contexts, particularly orthodontic facial profile generation, demonstrates that progressive growing techniques expand beyond face synthesis to domain-specific applications requiring diverse age, gender, and ethnic representation. The WPGGAN-GP model trained on 50,000 profile images achieved quantitative alignment between synthetic and real distributions while maintaining aesthetic realism validated through clinical expert assessment[31]. This represents a critical transition from benchmark dataset validation toward practical clinical validation, indicating the maturation of GAN-based synthesis for specialized medical applications.

## Domain-Specific Applications and Clinical Integration

### Medical Imaging and Virtual Staining

GANs have achieved substantial clinical relevance in medical image synthesis and augmentation, addressing critical data scarcity issues that limit model generalization in specialized medical domains. Virtual staining applications, where GANs translate unstained histopathological images to stained equivalents without chemical processing, represent a paradigm shift in histology workflows. The VISGAB benchmarking framework comprehensively evaluates GAN performance across quantitative metrics including Structural Similarity Index (SSIM), Peak Signal-to-Noise Ratio (PSNR), Fréchet Inception Distance (FID), and perceptual metrics like Learned Perceptual Image Patch Similarity (LPIPS)[51]. Critical thresholds establish FID≤25 as equating with perceived realism in computational histopathology, while LPIPS≤0.15 aligns with pathologist acceptability of synthetic histology images[51].

CycleGAN achieves mean LPIPS of 0.083±0.002 between H&E-stained and virtually stained images, establishing synthetic-real indistinguishability meeting clinical acceptability standards[51]. The utility extends to data augmentation for melanoma detection, where GANs address the documented underrepresentation of phototypes IV-VI in dermatological image repositories (only 12% of existing datasets), systematically generating synthetic skin lesion images across diverse phenotypes to reduce diagnostic biases in AI models trained on imbalanced datasets[1]. StyleGAN3-generated amelanotic melanoma images achieve 92% perceptual realism ratings from human evaluators, offering valuable training resources for dermatology residents encountering rare diagnostic scenarios[1].

### Medical Image Segmentation and Synthesis

Adversarial training mechanisms integrated into segmentation networks substantially improve boundary accuracy and handle data imbalance through discriminator-driven feature refinement. The GAN-based segmentation framework trains the generator as a segmentation network learning image-to-mask mappings while the discriminator provides adversarial supervision beyond standard cross-entropy losses, effectively capturing complex feature patterns in medical images. Multi-scale discriminator architectures (SegAN) enhance global and local structural feature distinction through discriminators operating at multiple resolution scales, demonstrating significant performance improvements in retinal vessel segmentation with elevated recall rates compared to single-scale cGAN approaches[21].

Semi-pixel cyclic GAN (SPCGAN) applications to ultrasound imaging for breast cancer lesion detection demonstrate the adaptation of cycle consistency principles to medical imaging domains where paired training data is scarce. Pancreas-GAN introduces recursive adversarial learning enforcing spatial smoothness consistency across successive image slices, addressing the challenge of segmenting small organs with irregular boundaries through global distribution constraints[21]. These specialized architectures highlight the critical shift from generic GAN applications toward clinical domain customization, incorporating anatomical knowledge through architectural modifications that enforce spatial coherence and physiologically plausible segmentation outputs.

### Dermatology and Skin Lesion Analysis

The comprehensive analysis of GAN applications in dermatology identifies eleven distinct clinical use cases spanning synthetic image generation, color standardization, segmentation, denoising, and super-resolution imaging[1]. Critically, the review documents persistent barriers to clinical integration despite promising early results, noting that few GAN models have achieved real-world clinical deployment due to regulatory limitations, insufficient validation in diverse populations, and the absence of standardized evaluation protocols. The technical challenge of addressing skin tone bias appears partially addressable through GAN-based data augmentation and synthetic image generation, yet deployment requires simultaneous advances in clinical validation frameworks and regulatory pathways[1].

StyleGAN and its successors enable facial attribute manipulation and deepfake generation detection through latent space inversion, creating datasets of 11,560 semantically diverse facial images with thirty-eight varying attributes (gender swapping, age progression, makeup application)[7]. The Facial Attribute Manipulation Detection (FAM) Dataset, created through StyleGAN3 inversion on the FFHQ dataset, demonstrates improved facial identity recognition in few-shot scenarios through specialized YOLO-based detectors augmented with Swin Transformer Blocks and Squeeze-Excite Spatial Pyramid Pooling modules, achieving substantially higher accuracy in synthetic face identity recognition compared to standard detectors[7].

## Image Synthesis and Text-to-Image Generation

### Evolution from Pure GAN to Hybrid Architectures

Text-to-image synthesis represents a domain where GANs have progressively yielded to complementary generative approaches, with recent innovations combining GAN advantages with diffusion model strengths. Early GAN-based approaches including StackGAN++ employed tree-structured multi-generator architectures progressively refining images from low to high resolution while incorporating text descriptions through conditional information fusion[8]. HDGAN and domain-specific variants like CookGAN demonstrated flexibility in generating domain-specific visual content, while XMC-GAN introduced cross-modal contrastive learning maximizing mutual information between text and image modalities[8].

Contemporary approaches increasingly integrate CLIP-based language understanding with GAN generation objectives. GALIP and GigaGAN represent the state-of-the-art in pure GAN-based text-to-image synthesis, with GigaGAN achieving high-quality large-scale image synthesis surpassing diffusion model performance on several benchmarks through extensive training on diverse text-image paired datasets[3][8]. UFOGen introduces a hybrid approach combining GANs and diffusion models for ultra-fast one-step text-to-image synthesis, demonstrating the emerging consensus that single-approach solutions are giving way to complementary framework combinations addressing speed-quality tradeoffs[8].

### Super-Resolution and Image Enhancement

GAN-based super-resolution has evolved from SRGAN through ESRGAN toward hybrid frameworks combining diffusion and adversarial training. SupResDiffGAN bridges the performance gap between pure GAN and diffusion approaches for single-image super-resolution, achieving GAN-equivalent inference speeds (comparable to ESRGAN) while generating sharp, detailed outputs exceeding pure diffusion baselines[32]. The architecture leverages latent space representation accelerating diffusion processes to as few as ten steps compared to thousands for traditional diffusion models, while incorporating adaptive noise corruption preventing discriminator overfitting and maintaining generator-discriminator training stability[32]. Extensive benchmark evaluation across standard super-resolution datasets (Set14, BSD100, Urban100) demonstrates that SupResDiffGAN achieves high perceptual quality through LPIPS metrics while maintaining computational efficiency suitable for real-world applications[32].

The broader GAN-based super-resolution landscape continues advancing through architectural innovations incorporating residual learning, perceptual loss functions weighing feature-space distances over pixel-space similarity, and adversarial training on multiple discriminator scales. These techniques maintain relevance particularly in domains emphasizing inference speed and real-time applicability where diffusion models' computational demands become prohibitive[35].

### Layout-Conditional Image Generation

LayoutDiffusion represents the current state-of-the-art in layout-to-image generation, demonstrating that diffusion architectures can exceed prior GAN-based methods (LostGAN-v1, LostGAN-v2, PLGAN) through novel multimodal fusion mechanisms[37][40]. The core innovation involves constructing structural image patches incorporating region information, transforming layout-image fusion into a unified form enabling object-aware cross-attention mechanisms precisely controlling spatial relationships among multiple objects[40]. On COCO-stuff and Visual Genome benchmarks, LayoutDiffusion achieves relative improvements of 46.35% and 26.70% on FID scores compared to prior methods, while maintaining substantially greater control over individual object positioning and size[40]. This progression highlights the critical transition where diffusion models with specialized conditioning mechanisms now exceed GAN capabilities in controllable generation tasks requiring precise spatial reasoning.

## Video Generation and Temporal Modeling

### Diffusion Transformers for Extended Temporal Synthesis

The explosive growth in video generation models during 2024-2025 represents a fundamental architectural transition from convolutional U-Net backbones toward Transformer-based diffusion models enabling efficient scaling analogous to large language models[52]. Diffusion Transformers (DiT) demonstrate exceptional scaling properties where model size and token reduction independently enhance generation quality, with total computational budget (Gflops) serving as the primary performance determinant rather than parameter count alone[5]. DiT architectures operating on spacetime patches rather than pixels achieve substantially improved computational efficiency—at 256×256 resolution, DiT-XL/2 requires only 119 Gflops compared to 742 Gflops for classifier-guided diffusion and 103 Gflops for latent diffusion models, while achieving superior FID scores[5].

Sparse mixture-of-experts variants (DiT-MoE) push scalability to 16.5 billion parameters while maintaining inference efficiency through selective expert routing where each token activates only a subset of experts[2]. DiT-MoE-XL, despite activating merely 1.5 billion parameters, substantially outperforms dense 3-billion and 7-billion parameter baseline transformers, demonstrating that conditional computation strategies dramatically improve scaling efficiency. This architectural advancement enables training of unprecedented model scales while maintaining computational feasibility, establishing the foundation for current large-scale video generation models like OpenAI's Sora[2][17].

### Frame-Aware Video Diffusion and Temporal Coherence

Traditional video diffusion models apply scalar timestep variables at clip-level, limiting capacity to model complex temporal dependencies required for diverse tasks including image-to-video generation, video interpolation, and extended sequence synthesis. Frame-Aware Video Diffusion Models (FVDM) introduce vectorized timestep variables enabling independent noise schedules for each frame, substantially enhancing fine-grained temporal dependency modeling[14]. This architectural innovation permits each frame to traverse independent temporal trajectories during the forward diffusion process while recovering to complete video sequences during reversal, fundamentally improving temporal coherence particularly in long-duration synthesis where traditional models accumulate errors[14].

Empirical evaluation demonstrates FVDM's superiority over state-of-the-art methods including Latte across multiple tasks, with qualitative comparisons revealing substantially smoother transitions and higher fidelity video outputs closely approximating real-world sequences. The model successfully generates 128-frame videos maintaining consistent motion and expression, demonstrating capacity for long-term temporal dependency capture addressing a critical limitation in contemporary video generation—the tendency toward catastrophic forgetting during fine-tuning and limited generalization in zero-shot transfer scenarios[14].

### Multi-Modal and Semantic Video Synthesis

Sora, OpenAI's production-scale video generation model, represents a watershed moment in the field through capacity to generate minute-long high-fidelity videos from text prompts at native resolutions and aspect ratios[49]. The architecture trains text-conditional diffusion transformers jointly on videos and images of variable durations and resolutions through unified spacetime patch representation, enabling dynamic camera motion with 3D-consistent scene evolution, long-range temporal coherence maintaining object permanence despite occlusion, and semantic understanding enabling multiple character appearances maintaining consistent visual identity throughout sequences[49]. Despite current limitations in modeling complex physical interactions (glass shattering, food consumption state changes) and occasional temporal incoherencies in extended generation, Sora demonstrates that scaled video models represent a viable path toward physical world simulation[49].

The convergence toward shared architectural principles across competing video generation models reveals critical design choices: continuous tokenizers without vector quantization preserve quality, latent diffusion frameworks improve computational efficiency, bidirectional spatio-temporal attention enhances expressive power, joint image-video training leverages larger image datasets addressing data scarcity, and progressive training (length then resolution expansion) optimizes computational resource allocation[52].

## 3D Object and Scene Generation

### GAN-based 3D Synthesis Frameworks

3D generation through GANs evolved from initial 3D voxel-based approaches toward sophisticated representations leveraging differentiable rendering and neural radiance fields. HoloGAN pioneered unsupervised 3D representation learning from unlabeled 2D images through 3D convolutional networks generating volumetric features, applying rigid transformations enabling pose adjustment, and differentiable perspective projection synthesizing 2D views for discriminator evaluation[15]. This framework established the principle that 3D-aware GANs can learn implicit 3D structure from 2D supervision alone, enabling arbitrary view synthesis without explicit 3D annotations.

EG3D innovatively integrated tri-plane architecture with StyleGAN2 framework, leveraging triplanar feature representations enabling efficient rendering through volume rendering while maintaining GAN-based generation flexibility[15]. GET3D introduced DMTet geometric representation coupled with tri-plane texture mapping, achieving high-fidelity textured 3D mesh generation through adversarial training. These methodologies established tri-plane representations as a powerful abstraction balancing rendering efficiency against generation quality, enabling practical 3D asset creation for graphics applications[15].

### Emerging 3D Gaussian Splatting Integration

Recent advances transition from NeRF-based geometry representations toward 3D Gaussian Splatting (3DGS) approaches achieving substantially faster convergence and rendering efficiency. DreamGaussian introduces efficient algorithms converting generated Gaussians into textured meshes suitable for interactive applications, while novel methods employ sequential decoders translating tri-plane features into Gaussian attributes through backbone fine-tuning enabling end-to-end conversion from pretrained 3D-aware GANs[15]. Layered Surface Volume representations for articulated digital humans introduce alternative 3D object parameterization leveraging multiple textured mesh layers around conventional templates, rendering through alpha compositing with fast differentiable rasterization while naturally capturing off-surface details like hair and accessories superior to single-layer template approaches[18].

## Data Augmentation and Synthetic Sample Generation

### Tabular Data and Limited-Sample Scenarios

GAN applications to tabular data augmentation address the persistent challenge of limited training samples in specialized domains while maintaining feature correlations and label consistency. Novel GAN approaches designed for high-dimensional low-sample-size (HDLSS) tabular data handle scenarios where feature count substantially exceeds sample count, incorporating skip logic constraints to maintain data validity across complex survey instruments[38]. The methodology augments datasets containing fewer than 258 samples with 210 features through conditional GAN generation, incorporating auxiliary networks performing global feature selection and importance-weighted sampling of conditioning vectors ensuring synthetic samples preserve label-feature relationships[38].

Empirical validation on substance use prediction demonstrates augmentation-derived improvements of 13.4% AUROC increase for binary classification and 15.8% improvement for multiclass ordinal prediction, substantially exceeding performance gains from simple data replication or traditional augmentation[38]. This application validates GANs' capacity to capture complex statistical relationships in limited-data regimes, addressing a persistent practical limitation in healthcare, finance, and specialized domains where data collection remains prohibitively expensive.

### Temporal and Sequential Data Synthesis

Dual-Layer GAN (DLGAN) decomposes time series generation into supervised sequence feature extraction and unsupervised reconstruction stages, combining autoencoder-style supervised learning with GAN-based generative modeling[57]. This architecture ensures generated temporal sequences preserve authentic temporal dependencies through feature-level reconstruction aligned with original time series characteristics. The first-layer generative network learns temporal feature vectors capturing real-time series characteristics while the second layer enhances reconstruction interpretability through unsupervised feature-reconstruction training[57]. Experimental evaluation across four publicly available datasets demonstrates DLGAN's superiority over state-of-the-art methods across multiple evaluation metrics, establishing GAN-based approaches as viable solutions for synthetic time series generation addressing data scarcity in financial, medical, and industrial monitoring applications.

## Generative Adversarial Network-Based Anomaly Detection

### Unsupervised Anomaly Detection through Synthetic Neighbor Analysis

Generative Adversarial Synthetic Neighbors (GASN) methodology combines GAN-based distribution learning with nearest-neighbor techniques, leveraging generators to focus on normal data distribution while synthetic neighbor approaches refine detection accuracy[27]. This two-stage approach trains the generator to produce synthetic normal data samples while measuring anomaly factors through similarity between synthetic and original data, identifying objects deviating significantly from normal distribution patterns. The mechanism exploits the fundamental property that GANs primarily learn normal object distributions during training on mixed datasets containing anomaly objects, with generated synthetic data serving as normal object benchmarks[27].

Experimental validation across multiple public datasets demonstrates GASN outperformance against existing anomaly detection approaches in both generalization and detection performance, with particular robustness in complex application scenarios. This represents a critical advance in unsupervised anomaly detection addressing limitations of traditional statistical methods and classical anomaly detection approaches struggling with complex data distributions[27].

## Deepfake Detection and Face Manipulation

### Hybrid GAN-Transformer Detection Frameworks

Face manipulation detection through combined GAN and Transformer architectures addresses the escalating sophistication of synthetic face generation techniques including DeepfaceLab and FaceSwap implementations. The proposed Fusion Framework for Forgery Detection (FFC) integrates three specialized modules: reconstructed GAN and Transformer feature extraction modules capturing local forgery artifacts through adversarial training and global dependencies through attention mechanisms; frequency domain and noise feature extraction modules identifying residual traces of synthetic generation; and SVM-based classification modules for final detection determination[33]. The innovation leverages the complementary strengths of GANs identifying visual artifacts and Transformers capturing global coherence inconsistencies impossible in natural faces[33].

Experimental results demonstrate substantially improved detection robustness compared to CNN-only or single-GAN approaches, achieving higher accuracy across benchmark deepfake datasets. This detection framework acknowledges the escalating arms race between generation sophistication and detection capability, establishing that multi-modal feature analysis combining spatial artifacts, temporal coherence, and frequency domain anomalies substantially improves detection reliability[33].

## Technical Evaluation Metrics and Benchmarking

### Image Quality Assessment and Distribution Matching

Quantitative evaluation of generated images relies on metrics capturing distribution similarity and perceptual quality. Fréchet Inception Distance (FID) measures distributional similarity between generated and real images through features extracted from pretrained Inception networks, with FID≤7.4 at 128×128 resolution representing state-of-the-art performance on ImageNet conditional synthesis[13]. Inception Score (IS) evaluates both quality and diversity through KL divergence between predicted class distributions for generated versus real samples. Structural Similarity Index (SSIM) and Learned Perceptual Image Patch Similarity (LPIPS) capture pixel-level and perceptual feature-space differences respectively, with LPIPS≤0.15 establishing acceptability thresholds for synthetic histopathology[51].

Novel metrics specifically designed for medical image synthesis (Histopathological Stain Fidelity Index, HSFI) demonstrate strong negative correlation with FID (r=-0.956), KID (r=-0.931), and LPIPS (r=-0.942), validating alignment with standard realism metrics while capturing domain-specific diagnostic fidelity requirements[51].

### Video Generation Evaluation and Beyond FVD

Traditional Fréchet Video Distance (FVD) relies on Gaussianity assumptions about video feature distributions extracted from 3D ConvNets, exhibiting reliability limitations particularly with varying clip durations and non-Gaussian feature clusters by dataset. JEDi (JEPA Embedding Distance) addressing FVD's limitations employs Maximum Mean Discrepancy with polynomial kernels eliminating parametric distribution assumptions, requiring substantially fewer samples (700-800 versus 4,000-4,700 for FVD convergence) while tracking incremental model improvements more accurately across training checkpoints[54]. This advancement represents critical progress toward video generation evaluation methodologies capable of reliably distinguishing qualitative improvements as models scale toward production deployment.

## Emerging Challenges and Regulatory Barriers

Despite substantial technical advances, clinical integration of GAN-based medical imaging solutions faces persistent regulatory limitations, ethical concerns regarding synthetic data deployment in clinical practice, and challenges related to algorithmic fairness across diverse patient populations. The dermatology review explicitly documents the absence of standardized protocols for clinical validation, insufficient representation of diverse skin phenotypes despite GAN-based augmentation capacity, and the need for regulatory clarity regarding synthetic data utilization in diagnostic contexts[1]. Privacy-preserving GAN training approaches integrating differential privacy mechanisms remain nascent, with ADAM-DPGAN representing preliminary work toward privacy-preserving adversarial training[47].

## Convergent Architectures and Future Directions

### Hybrid Generative Frameworks

The period 2022-2025 witnessed decisive movement toward hybrid frameworks combining GANs with complementary generative approaches. Diffusion-GAN combinations in super-resolution and text-to-image synthesis leverage GAN efficiency advantages with diffusion model quality benefits[32]. Equilibrium Matching frameworks learning energy landscapes rather than time-conditional velocities offer theoretical alternatives to both GANs and diffusion models, achieving FID of 1.90 on ImageNet 256×256 while supporting optimization-driven sampling enabling adaptive computational resource allocation[56].

### Scalability Through Sparse Computation

Mixture-of-Experts strategies enabling conditional computation through selective expert routing represent critical breakthroughs in model scaling. DiT-MoE architectures scaling beyond 16 billion parameters while maintaining inference efficiency establish sparse computation as a fundamental scaling principle transferable across generative domains[2]. This approach diverges from dense scaling practices limiting practical deployment through computational demands, instead enabling model capacity expansion compatible with resource-constrained inference environments.

### Data and Representation Standardization

The field exhibits emerging convergence toward standardized representations addressing heterogeneous input handling. Spacetime patch-based representations enabling joint image-video training at variable resolutions and aspect ratios represent a paradigm shift toward flexible input handling rather than fixed-size assumptions[49]. Continuous tokenizers replacing vector quantization preserve signal fidelity while enabling progressive training strategies optimizing computational resource allocation[52].

## Conclusion

Generative Adversarial Networks have matured substantially during 2022-2025 through convergence on hybrid architectural principles, integration with complementary generative frameworks, and domain-specific specialization addressing concrete clinical and industrial requirements. Theoretical advances in training stability through refined loss functions and regularization techniques have substantially mitigated historical training instability, enabling production-scale deployment across medical imaging, video synthesis, and data augmentation domains. Simultaneously, diffusion-based generative approaches have emerged as competitive alternatives to pure GAN implementations for certain tasks, catalyzing the field toward pragmatic framework combinations leveraging complementary strengths rather than monolithic GAN reliance.

The period 2025 and beyond will likely witness three decisive trends: (1) regulatory and clinical validation frameworks enabling GAN-based synthetic data deployment in clinical diagnostics, currently absent but essential for translating technical advances to patient care; (2) continued architectural convergence toward sparse computation through mixture-of-experts and conditional computation strategies enabling larger models compatible with resource constraints; and (3) explicit integration of fairness and privacy-preservation mechanisms within GAN frameworks, addressing ethical concerns currently limiting adoption in sensitive domains including healthcare and financial applications. These developments will determine whether technical maturation translates to widespread practical deployment or remains confined to research contexts.

## References

[1] Bioengineering (Basel). 2025 Oct 16;12(10):1113. "Generative Adversarial Networks in Dermatology: A Narrative Review"

[2] arXiv:2407.11633. "Scaling Diffusion Transformers to 16 Billion Parameters"

[3] Tiffin University. "Advances in AI-Generated Images and Videos"

[4] arXiv:1809.11096. "Large Scale GAN Training for High Fidelity Natural Image Synthesis"

[5] Youngdo Lee. "[Generative Model] Diffusion Transformer (DiT)"

[7] Nature. 2025. "Facial identity recognition using StyleGAN3 inversion and improved Tiny YOLOv7"

[8] arXiv:2403.07389. "Text-to-Image Synthesis: A Decade Survey"

[10] arXiv:2212.09102. "Face Generation and Editing with StyleGAN: A Survey"

[14] arXiv:2410.03160v1. "Redefining Temporal Modeling in Video Diffusion: The Vectorized Timestep Variable"

[15] arXiv:2504.11734v1. "Recent Advance in 3D Object and Scene Generation: A Survey"

[18] Computational Imaging Organization. "Efficient 3D GANs with Layered Surface Volumes"

[21] PMC. 2024. "Medical Image Segmentation: A Comprehensive Review of Deep Learning"

[25] GeeksforGeeks. "Wasserstein Generative Adversarial Networks (WGANs)"

[27] Nature. 2024. "Generative adversarial synthetic neighbors-based unsupervised anomaly detection"

[28] PMLR. 2017. "Wasserstein Generative Adversarial Networks"

[31] PMC. 2025. "Developing an artificial intelligence-based progressive growing GAN with gradient penalty for facial profile synthesis"

[32] arXiv:2504.13622v1. "SupResDiffGAN a new approach for the Super-Resolution task"

[33] PMC. 2025. "Exposing Face Manipulation Based on Generative Adversarial Networks and Transformers"

[35] JETIR. 2024. "Advancements High-Quality Image Enhancement Using GAN-Based Super Resolution"

[37] CVPR 2023. "LayoutDiffusion: Controllable Diffusion Model for Layout-to-Image Generation"

[38] IJCAI. 2024. "A Novel GAN Approach to Augment Limited Tabular Data"

[40] arXiv:2303.17189. "Controllable Diffusion Model for Layout-to-image Generation"

[44] arXiv:2501.05441v1. "The GAN is dead; long live the GAN! A Modern Baseline GAN"

[49] OpenAI. 2024. "Video generation models as world simulators"

[51] Nature. 2025. "VISGAB: Virtual staining-driven GAN benchmarking for optimizing generative models"

[52] Yen-Chen Lin. 2025. "Video Generation Models Explosion 2024"

[54] arXiv:2410.05203v2. "Beyond FVD: Enhanced Evaluation Metrics for Video Generation"

[56] OpenReview ICLR 2026. "Equilibrium Matching: Generative Modeling with Implicit Energy-Based Models"

[57] arXiv:2508.21340v1. "DLGAN: Time Series Synthesis Based on Dual-Layer Generative Adversarial Networks"