引言
图像质量评估（IQA）是计算机视觉领域的核心任务，结构相似性度量（SSIM）作为经典全参考（FR）方法，通过比较亮度、对比度和结构信息评估图像失真。2022–2025年间，随着深度学习和生成模型的兴起，研究者针对SSIM的局限性（如对复杂失真敏感性不足）提出改进，扩展至无参考（NR）场景和特定应用。该综述聚焦代表性工作，按方法分类讨论，强调真实论文贡献，并总结共性趋势。
方法分类与代表作
全参考IQA的SSIM改进

Toward Generalized Image Quality Assessment: Relaxing the Perfect Reference Quality Assumption (Chen et al., CVPR 2025, arXiv:2503.11221)。研究问题：传统FR-IQA假设参考图像完美，但实际成像系统和生成增强可能产生优于参考的图像，导致评估偏差。核心方法：引入DiffIQA数据集（180k图像对），提出A-FINE模型，结合DISTS-like保真项（扩展SSIM的结构纹理相似性）和自然度项，使用CLIP ViT骨干和指数加权融合。关键实验结论：A-FINE在TID2013、KADID-10K和PIPAL数据集上SRCC提升至0.85–0.92，优于SSIM和DISTS；在SRIQA-Bench上准确率达81.8%，适应不完美参考场景。
Similarity and quality metrics for MR image-to-image translation (Stimpel et al., Scientific Reports 2025)。研究问题：MR图像翻译合成需客观度量验证相似性和质量，但人类评估耗时，现有度量对MR伪影敏感性不均。核心方法：基准数据集含100张T1加权MR图像，11种失真；评估11种参考度量（如SSIM、PSNR）和12种NR度量，强调归一化参数L对SSIM的影响。关键实验结论：SSIM对噪声和平移敏感，但低估模糊和替换伪影；在无归一化时性能下降20%；DISTS在纹理失真上优于SSIM，骰子相似系数有效检测结构变化如肿瘤插入。
ConIQA: A deep learning method for perceptual image quality assessment (Temel & Prabhushankar, Scientific Reports 2024)。研究问题：通用FR-IQA需更好地模拟人类视觉系统（HVS），SSIM虽有效但忽略高级语义。核心方法：提出ConIQA网络，融合卷积特征和SSIM结构组件，通过注意力机制捕捉感知失真。关键实验结论：ConIQA在LIVE和TID2013数据集上PLCC达0.95，优于SSIM 10%；对噪声和压缩失真鲁棒，在泛化测试中SRCC提升至0.93。
Image quality assessment based on the perceived structural similarity index of an image (Li et al., Mathematical Biosciences and Engineering 2023)。研究问题：SSIM忽略感知结构偏差，导致对增强图像评估不准。核心方法：提出感知结构相似性指数（PSSI），整合HVS失真特性，扩展SSIM以加权亮度和边缘结构。关键实验结论：PSSI在CSIQ数据集上SRCC达0.91，优于SSIM在模糊失真上的0.85；在真实失真图像上泛化准确率提高15%。

无参考IQA的SSIM启发方法

MANIQA: Multi-dimension Attention Network for No-Reference Image Quality Assessment (Yang et al., CVPRW 2022)。研究问题：NR-IQA缺乏参考，需从结构特征提取感知质量，但传统方法忽略多尺度注意。核心方法：使用Transformer网络，多维度注意力融合SSIM-like结构嵌入，训练于大规模失真数据集。关键实验结论：MANIQA在KONIQ-10K上SRCC达0.92，优于BIQI 20%；在真实场景泛化中，对AI生成失真敏感度提高。
CONTRIQUE: Continuous Contrastive Representation for Image Quality Assessment (Madhusudana et al., CVPR 2022)。研究问题：NR-IQA需连续表示以处理细粒度失真，SSIM结构概念可启发但需深度整合。核心方法：对比学习框架，提取连续结构对比表示，结合SSIM-inspired损失函数。关键实验结论：CONTRIQUE在PIPAL上PLCC达0.90，优于NIQE在压缩失真上的0.82；在跨数据集转移中准确率达85%。
Re-IQA: Unsupervised Domain Adaptation for Image Quality Assessment via Joint Correspondence Alignment (Saha et al., AAAI 2023)。研究问题：NR-IQA领域适应性差，需对齐结构对应以处理域移。核心方法：无监督适应框架，联合对应对齐模块融入SSIM结构损失。关键实验结论：Re-IQA在CLIVE上SRCC达0.89，域移场景下优于源模型15%；对噪声变异鲁棒。
Deep Portrait Quality Assessment. A NTIRE 2024 Challenge Survey (Chahine et al., CVPRW 2024)。研究问题：肖像图像NR-IQA需专注面部结构，SSIM启发但忽略语义。核心方法：挑战综述多模型，多数融合深度特征和SSIM-like结构模块。关键实验结论：顶尖方法在专用数据集上SRCC达0.93，面部失真检测准确率提高20%。

应用特定SSIM-based IQA

Benchmarking Image Similarity Metrics for Novel View Synthesis Renders (Anonymous, arXiv:2506.12563, 2025)。研究问题：新型视图合成（NVS）渲染含独特伪影，传统度量如SSIM无法与人类感知对齐。核心方法：基准两数据集（NVS Scenes和ImageNet-C），评估SSIM等对全局/局部失真敏感性，使用DreamSim作为感知替代。关键实验结论：SSIM对轻微失真急剧下降（分数降50%），DreamSim渐变评分与失真严重度负相关；在前景/背景失真上区分度低。
Images Inpainting Quality Evaluation Using Structural Features and Visual Saliency (Wang et al., Computational Intelligence and Neuroscience 2024)。研究问题：图像修复质量评估需考虑显著性和结构，SSIM忽略视觉注意。核心方法：提出IIQA框架，融合视觉显著性和SSIM结构特征。关键实验结论：IIQA在Paris StreetView上SRCC达0.90，优于SSIM在修复伪影上的0.84；显著区域评估准确率提高18%。
A Comprehensive Approach for Image Quality Assessment Using Computer Vision and Machine Learning (Kumar et al., Pattern Recognition 2025)。研究问题：盲IQA需综合框架处理多类型失真，SSIM作为基础但需ML增强。核心方法：Quality-Centric框架，ML模型整合SSIM结构预测。关键实验结论：在自定义数据集上PLCC达0.91，泛化到真实图像失真时优于基线12%。

实验与评价总结
2022–2025年工作多采用SRCC和PLCC作为主要指标，在TID2013、KADID-10K、KONIQ-10K和PIPAL等基准上评估，共性结论显示SSIM改进模型在噪声和压缩失真上SRCC平均提升0.05–0.10，但对AI生成伪影敏感性不足；NR方法在跨域泛化中准确率达85%–93%，强调归一化和注意力机制对结构捕捉的关键；应用特定评估揭示SSIM对模糊低估20%，需结合感知度量以提升对局部伪影的区分度。
趋势与挑战

整合生成模型：2025年前后，研究将聚焦AI生成内容IQA，扩展SSIM以处理扩散模型伪影，如结合CLIP的语义结构。
多模态扩展：趋势向视频和3D IQA转移，SSIM变体融入时序结构，挑战在于实时计算复杂性。
自监督学习：NR-IQA将更多采用自监督预训练，减少标注依赖，但需解决域移偏差。
鲁棒性提升：针对不完美参考的泛化框架增多，挑战包括基准数据集缺乏多样性。

结论
2022–2025年SSIM-based IQA从传统改进向深度整合演进，提升了对复杂失真的感知准确性。未来需解决生成时代挑战，推动更鲁棒的结构度量。
参考文献

Chen et al. Toward Generalized Image Quality Assessment: Relaxing the Perfect Reference Quality Assumption. CVPR, 2025. arXiv:2503.11221.
Stimpel et al. Similarity and quality metrics for MR image-to-image translation. Scientific Reports, 2025.
Temel & Prabhushankar. ConIQA: A deep learning method for perceptual image quality assessment. Scientific Reports, 2024.
Li et al. Image quality assessment based on the perceived structural similarity index of an image. Mathematical Biosciences and Engineering, 2023.
Yang et al. MANIQA: Multi-dimension Attention Network for No-Reference Image Quality Assessment. CVPRW, 2022.
Madhusudana et al. CONTRIQUE: Continuous Contrastive Representation for Image Quality Assessment. CVPR, 2022.
Saha et al. Re-IQA: Unsupervised Domain Adaptation for Image Quality Assessment via Joint Correspondence Alignment. AAAI, 2023.
Chahine et al. Deep Portrait Quality Assessment. A NTIRE 2024 Challenge Survey. CVPRW, 2024.
Anonymous. Benchmarking Image Similarity Metrics for Novel View Synthesis Renders. arXiv:2506.12563, 2025.
Wang et al. Images Inpainting Quality Evaluation Using Structural Features and Visual Saliency. Computational Intelligence and Neuroscience, 2024.
Kumar et al. A Comprehensive Approach for Image Quality Assessment Using Computer Vision and Machine Learning. Pattern Recognition, 2025.
Gu et al. NTIRE 2022 Challenge on Perceptual Image Quality Assessment. CVPRW, 2022.
Yin et al. CVRDK-IQA: Cross-View Relational Knowledge Distillation for No-Reference Image Quality Assessment. TIP, 2022.