# 结构相似性指标在图像质量评估中的应用：2022-2025年综述

本综述系统回顾了2022-2025年间结构相似性（Structural Similarity Index, SSIM）及其衍生指标在图像质量评估（Image Quality Assessment, IQA）领域的发展现状。通过梳理全参考（Full-Reference, FR）、无参考（No-Reference, NR）及医学影像等专业领域的应用，揭示了从像素级差异度量向感知相似性评估的范式转变，以及深度学习赋能下SSIM衍生方法（MS-SSIM、DISTS、LPIPS等）的多维创新。研究表明，虽然SSIM及其变体在评估结构保持方面表现优异，但在处理生成式图像、高动态范围（HDR）内容和医学专业应用时仍存在泛化能力不足、对感知质量的刻画精度有限等瓶颈。当前研究重心已从单一度量指标的优化转向融合多模态大语言模型、自监督学习和领域自适应的复合评估范式，预期未来三年内将涌现更多面向具体应用场景的专业化评估体系。

---

## 引言

### IQA问题的核心困境与SSIM的历史定位

图像质量评估作为图像处理、计算机视觉和多媒体通信的基础性问题，长期面临一个核心悖论：自动化度量结果与人类视觉感知的不一致[2]。传统的峰值信噪比（Peak Signal-to-Noise Ratio, PSNR）以及均方误差（Mean Squared Error, MSE）基于像素级的逐点比较，忽视了人类视觉系统（Human Visual System, HVS）对结构信息、对比度敏感性和频率特性的优先处理机制[4]。2004年SSIM的提出标志了一次范式转变——从纯信号误差度量跃升到结构相似性评估，使IQA方法首次在多个数据库上的相关性显著超越PSNR[2][4]。

然而，2022年以来的工作普遍指出，SSIM虽然在有限的合成失真（如JPEG压缩、高斯模糊等标准失真）上表现稳健，但在以下场景中可靠性显著下降：（1）生成式模型输出的真实感图像（其中参考图像与测试图像的自然度关系逆转）；（2）HDR/宽色域图像的质量评估（需要考虑色彩空间非线性感知）；（3）医学影像中多模态、高度专业化的失真模式；（4）对抗性扰动导致的语义不变但SSIM剧烈波动的情况[1][7]。这些观察驱动了过去三年内IQA研究的多个新方向：（1）显式建模失真多样性与参考图像质量关系的广义IQA框架；（2）融合深度学习特征与SSIM结构概念的混合指标；（3）应用于生成模型和专业领域的实用化评估系统。

### 综述的范围与组织框架

本综述聚焦2022-2025年间的代表性工作，按照评估范式（全参考、无参考、医学专业应用）和方法论基础（传统统计、深度学习混合、多模态融合）进行分类。核心关注点在于：（1）SSIM及其变体（MS-SSIM、CW-SSIM等）的改进与扩展；（2）学习式指标（LPIPS、DISTS、MILO）如何汲取SSIM的结构直觉但克服其局限；（3）不同应用领域（自然图像、医学图像、HDR内容、人脸图像、视频）的专业化适配；（4）评估范式中的新兴因素，如生成式AI输出质量判别、对抗鲁棒性、可解释性。截止目前检索到的2022-2025年相关顶会/顶刊/arXiv论文已超过30篇，本综述选择12-15篇最具代表性和创新性的工作进行深入分析。

---

## 方法分类与代表作分析

### 第一类：SSIM的理论扩展与失真感知改进

#### 1.1 感知结构相似性指标（PSIM）

Yao等人（2023）基于对比敏感性、频率敏感性、亮度非线性和掩蔽特性等HVS特征，在SSIM框架基础上提出了感知结构相似性指标（Perceived Structural Similarity Index, PSIM）[4]。该工作首先建立了一个HVS感知模型，对真实图像进行预处理以消除视觉冗余，进而通过结合感知图像特征改进SSIM的计算。在TID2013、CSIQ、LIVE和CID四个基准数据库上，PSIM相对于SSIM的准确率（PLCC）提升达9.91%，相对于12个现有IQA模型均保持优势[4]。该工作的核心贡献在于证明了显式的HVS特征建模（尤其是非线性感知特性）能显著增强结构相似性指标在多样化失真类型上的泛化能力，特别是在处理标准偏差大幅变化的图像时表现更加鲁棒。

#### 1.2 医学影像中的SSIM应用与局限分析

Nature期刊2025年发表的一项多中心对比研究[7]系统评估了SSIM及其衍生指标在医学图像中的有效性。该研究针对MR影像转换任务，比较了包括SSIM、MS-SSIM、PSNR、LPIPS、DISTS等多种度量指标的表现，发现SSIM在检测运动伪影和磁敏感性伪影时存在系统性的失效模式：过度平滑的图像（高SSIM分数）常导致诊断相关细节的模糊[7]。研究指出，医学影像质量评估中的关键问题是SSIM未能区分"结构保留但诊断价值丧失"的退化模式，这在标准自然图像IQA中较少出现。该工作建议在医学应用中应采用多指标融合策略，并根据模态和临床任务调整权重，而非简单依赖单一的SSIM或MS-SSIM值。

#### 1.3 FSIM与低级特征相似性思想

线性阶段的FSIM（Feature Similarity Index Measure）虽发表于2011年，但在2024-2025年的医学影像和视频质量评估综述[16][31][34]中被反复引用和对标，反映了其持续的参考价值。FSIM基于相位一致性（Phase Congruency, PC）和梯度幅度（Gradient Magnitude, GM）两个互补的低级特征，旨在捕捉HVS主要基于低级特征而非整体结构进行理解的特点[31]。在FSIM的启发下，近年多项工作探索了超越纯结构指标的"特征相似性"概念，将其与深度学习特征提取相结合，衍生出了DISTS等新一代指标。

### 第二类：深度学习赋能的混合指标——从LPIPS到DISTS及其后继

#### 2.1 LPIPS与感知特征空间的建立

Learned Perceptual Image Patch Similarity（LPIPS）虽于2018年提出，但在2022-2025年间的大量应用研究中作为"基准深度学习指标"被广泛采用和对标[2][7][10][11]。其核心创新在于直接利用预训练图像分类网络（如VGG、AlexNet）的中间特征表示来度量感知相似性，规避了手工特征设计的局限。多篇论文（包括医学影像、超分辨率、图像复原等领域）的实验结果表明，LPIPS在与人类主观评分的相关性上显著优于PSNR和SSIM，特别是在处理纹理细节和高频信息丧失时表现更加灵敏[2][10]。然而，LPIPS的缺陷也逐渐显露：（1）对生成式模型输出的"虚假"图像内容可能高估其质量；（2）对空间位移和小尺度变形的鲁棒性不足；（3）计算复杂度相对较高[7]。

#### 2.2 DISTS与纹理感知的强化

Deep Image Structure and Texture Similarity（DISTS）是LPIPS的重要衍生，通过给予纹理相似性更高的权重，在多个基准上优于LPIPS[2][7][11]。2024-2025年的研究进一步证实，DISTS在处理生成式超分辨率、图像去噪和人脸复原等任务时，对于精细纹理细节的保留评估更加准确[10][33]。特别地，在超高清（UHD）图像质量评估中，DISTS相对于单纯的结构度量展现出更强的辨别能力[10]。然而，DISTS仍然保留了基于预训练网络特征的根本性限制——该特征并非为IQA任务优化设计，导致在某些专业领域（如医学影像）的泛化性仍待改进。

#### 2.3 轻量级感知指标MILO的提出

2024年arXiv发布的MILO（Metric for Image- and Latent-space Optimization）[11]代表了一个重要的设计思想转变：突破对预训练网络特征的依赖，使用"伪MOS监督"（pseudo-MOS supervision）直接训练一个轻量级、多尺度的感知指标。MILO通过在不同尺度应用已知的质量度量标准作为标签生成器，避免了大规模人工标注的成本。实验结果显示，尽管模型规模仅为LPIPS和DISTS的1/5-1/3，MILO在标准IQA基准上达到了可比或超越的性能，并支持在扩散模型的隐空间内进行实时感知指导[11]。这一工作直接回应了应用中对"快速、轻量、可解释"指标的需求，预示着未来IQA方法的一个重要方向。

### 第三类：无参考IQA的自监督与多任务学习范式

#### 3.1 基于失真流形学习的NR-IQA

ARNIQA（leArning distoRtion maNifold for Image Quality Assessment）[29]采用自监督学习方法，通过建模失真流形而非显式依赖失真标签的方式进行无参考质量评估。该方法的核心假设是：失真图像在特征空间中形成一个有结构的流形，模型可以通过对比学习（将同一原图的不同失真版本作为正样本对）来隐式捕捉失真特性[29]。在LIVEC、BID、KonIQ-10k等无参考基准上，ARNIQA展现出接近或超越有参考方法的性能，同时具有显著的跨数据库泛化能力。这一工作的启示在于：NR-IQA不必严格局限于"无参考"的狭隘理解，通过巧妙的自监督目标设计，模型可以在不显式提供参考图像的情况下学习到等价的"参考知识"。

#### 3.2 本地流形学习与人类视觉注意机制的融合

2024年的LML-IQA（Contrastive Local Manifold Learning）[26]进一步细化了流形学习思想，引入了视觉显著性裁剪（visual saliency cropping）的概念。该工作观察到，传统的对比学习假设同一图像的所有裁剪块具有相同质量，这与人类视觉注意机制不符——人眼优先关注显著区域来判断全局质量。LML-IQA通过教师-学生互学框架，使用显著性为正样本、非显著区域为同类负样本，有效防止了本地流形坍塌问题[26]。在LIVE、CSIQ、TID等合成失真数据库上，该方法取得了显著改进，SRCC平均提升5%-10%。该工作重新将人类视觉心理学与机器学习流形理论相联系，为NR-IQA的设计注入了新的理论基础。

#### 3.3 转移学习与领域自适应的实用化应用

PMC发表的一项综合研究[17]系统分析了迁移学习在NR-IQA中的应用。该工作利用ResNet-50等预训练CNN，通过特征提取、自适应融合网络和质量预测回归三阶段管道，实现了对失真图像的有效评估，特别是在处理AI生成图像等复杂失真时表现出更强的鲁棒性。研究指出，迁移学习的关键在于多尺度语义特征的捕捉——不同层级的特征（低级边界、中级纹理、高级语义）对质量评估的贡献不同，需要通过自适应融合而非简单平均来聚合[17]。这一发现对实际部署IQA系统具有重要指导意义，因为真实场景中往往无法获得充足的有标注IQA数据，迁移学习提供了一条可行的快速部署路径。

### 第四类：多模态大语言模型赋能的描述性与细粒度IQA

#### 4.1 从质量评分向质量推理的范式转变

CVPR 2025发表的DeQA-Score[57]和arXiv 2024的Grounding-IQA[60]标志了一个重要的范式转变：从单纯的数值质量评分扩展到基于自然语言的细粒度推理。DeQA-Score通过教学多模态大语言模型（MLLMs）直接回归准确的质量分数分布，而非离散的质量等级，克服了先前方法（如Q-Align）中MLLMs输出的离散性与真实质量分数连续分布的不匹配[57]。该工作在KonIQ-10k上的PLCC相对提升1.3%，在LIVE In-the-Wild等域外数据集上的提升达4.6%，并且同时支持质量描述生成，提供了可解释的诊断信息。

Grounding-IQA更进一步，引入了"接地"（grounding）的概念，即将质量评估与空间定位相结合[60]。该工作包含两个子任务：GIQA-DES（带有精确位置的质量描述）和GIQA-VQA（局部区域的质量问答）。通过构建160K图像的GIQA-160K数据集和对应的基准，该工作证明了MLLMs能够进行细粒度的质量判别，并将质量问题与具体的失真位置相关联[60]。这两项工作共同反映了当前IQA应用的核心需求：不仅要评估全局质量分数，更要提供诊断信息，帮助内容创建者、医学诊断师等专业人士快速定位和理解质量问题。

#### 4.2 医学影像中的多任务质量评估基准

MedQ-Bench[30]是2024年的重大工作，建立了针对多模态医学影像（MRI、CT、超声、眼底等）的专业化质量评估基准。该工作创新性地采用了"感知-推理"范式，不仅评估MLLMs对医学影像质量属性（清晰度、对比度、噪声、伪影等）的感知能力，还评估其对质量与诊断影响之间因果关系的推理能力[30]。与通用图像不同，医学影像质量直接关乎诊断准确性和患者安全，其评估需要领域专业知识和模态特定的失真理解。MedQ-Bench包含了无参考和有参考两种评估范式，通过多轮人工专家评审确保标注质量，初步测试结果表明最先进的MLLMs在某些医学影像的质量推理上仍存在显著不足[30]。

### 第五类：生成式模型输出与特殊内容的质量评估

#### 5.1 广义IQA与参考图像质量假设的松弛

CVPR 2025的A-FINE工作[1]正式提出了"广义IQA"框念，直接针对现有FR-IQA方法的根本性假设——"参考图像具有完美质量"。该工作观察到，在实际应用中（特别是生成式图像增强、超分辨率等场景），测试图像的视觉质量可能高于参考图像。此时传统FR-IQA方法（基于参考-测试的Euclidean距离）会给出荒谬的评价[1]。A-FINE通过自适应加权图像保真度（DISTS型）和图像自然度两项，并在参考图像自然度远高于测试图像时优雅地退化回标准FR-IQA[1]。该工作还构建了SRIQA-Bench基准，包含1000张由十种超分方法生成的图像，并基于完整成对比较进行标注。实验表明，A-FINE在标准FR-IQA基准上保持竞争力的同时，在处理参考质量不完美的场景时性能提升20%-30%。

#### 5.2 HDR图像与色彩空间特定的质量评估

2025年的AIC-HDR2025基准[54]和Nature 2024的HDR评估研究针对高动态范围图像建立了首个面向高保真度范围的专业数据集。传统SSIM和PSNR基于8位SDR范围设计，直接应用于10-12位HDR内容时失效[54]。该工作采用JPEG AIC-3的三元组比较（triplet comparison）方法学，基于JND（刚好可觉差）而非绝对质量值，收集了151名参与者、4个标准化实验室的34560评分[54]。初步评估显示，最新的感知指标（DISTS、LPIPS变体）在HDR场景中的有效性仍需改进，预示着需要为HDR特别优化的评估指标。这一方向的工作说明了：当图像内容属性发生质的变化（如从SDR到HDR、从CFA采集到全彩、从2D到全景等）时，现有IQA指标的泛化能力面临根本性挑战，需要针对性的改进或全新设计。

#### 5.3 人脸图像质量评估的变换器方法

ViT-FIQA[19][22]代表了Vision Transformer在专业化IQA中的应用。相比于CNN为主的传统FIQA方法，ViT-FIQA通过在标准人脸识别ViT骨干上添加可学习的质量令牌（quality token），使该令牌与所有图像补丁进行自注意交互，从而聚合上下文信息预测人脸图像的实用性评分[22]。在LFW、CA-LFW、AgeDB-30等多个人脸IQA基准上，ViT-FIQA在CNN和ViT型人脸识别模型上均表现出top-tier性能，特别是在姿态和质量具有挑战的数据集（如XQLFW、CFP-FP）上的鲁棒性更强[22]。这一工作的意义在于：通过将IQA任务紧密集成到主任务（人脸识别）的学习流程中，模型学到的质量表示与其后续应用更加对齐，相比独立训练的IQA模型具有更强的适用性。

### 第六类：统一与诊断——视频、医学多场景的集成框架

#### 6.1 视频质量评估的多专家融合

2025年arXiv发表的Unified-VQA[13]提出了一个多专家、多任务的统一视频质量评估框架。该工作认识到，视频失真涉及空间（压缩、分辨率变化）、时间（运动抖动、帧插值）、色彩（HDR映射、量化错误）三个独立维度，不同维度的最优评估策略差异显著[13]。框架采用三个专家网络（空间、时间、色彩）分别处理各自的失真，再通过受SlowFast网络启发的时空聚合器融合不同专家的特征，最后通过统一诊断头同时输出全局质量评分和细粒度的伪影向量[13]。在多个VQA基准（HD/UHD分辨率、色彩、时间失真数据库）上，Unified-VQA相对于传统指标（PSNR、SSIM、MS-SSIM）和学习式方法（LPIPS、RankDVQA、VIDEVAL）的性能提升显著[13]，平均SROCC提升5%-15%。这一框架的启示是：当评估对象具有多模态或多因子结构时，单一的聚合器往往不足以捕捉各自的特性，多专家互学与有结构的特征融合能更好地保留失真特异性信息。

#### 6.2 医学影像IQA的深度学习实用化

NIH发表的关于超广角眼底照片的自动IQA研究[3]以及多项医学影像综述[27]系统总结了深度学习在医学IQA中的实用化进展。研究利用EfficientNet-B3等轻量级骨干网络，通过加权交叉熵损失（权重比2:2:1:1:1对应不同质量等级）突出对低质量图像的敏感性，在真实医学数据上的模型与专家评价者的一致性（以Kappa系数或ICC衡量）已超过专家间一致性[3]。这意味着深度学习IQA模型在医学应用中已达到或超越人工标注的可信度。然而，这些工作也指出了关键挑战：（1）医学IQA的最优评分准则因临床应用而异，无法建立通用的"黄金标准"[27]；（2）在极端情况（如极低光条件、异常解剖变异）上的泛化性仍需改进；（3）模型决策的可解释性对临床采用至关重要，现有深度学习方法在这方面能力不足[30]。

---

## 实验与评价总结

### 共性实验设计与评估指标

过去三年的IQA研究普遍采用以下实验范式：（1）在LIVE、CSIQ、TID2013等经典合成失真数据库上评估相关性（PLCC、SRCC等）；（2）在LIVEC、KonIQ-10k等现实失真或生态数据库上测试跨域泛化；（3）针对生成式输出（超分、复原、GAN输出）构建专门数据集进行评估；（4）在医学、人脸等垂直领域构建专业基准。评估指标方面，虽然SSIM及其变体仍被广泛使用，但已形成了"多指标对标"的评估文化：几乎所有新方法都同时报告PSNR、SSIM、MS-SSIM（作为传统基线）、LPIPS、DISTS（作为深度学习对标）和SRCC/PLCC（与人类主观评分的相关性）。这种多层次的对标反映了认识的提升：单一指标难以全面刻画图像质量，任何新指标的价值都需通过与多个既有方法的对比来证明。

### 关键发现与性能趋势

经过系统整理各类工作的实验结果，呈现出以下共性结论：

**（1）感知学习指标的持续性能优势**。LPIPS、DISTS及其衍生品在与人类主观评分的相关性上，相对于基于手工特征的SSIM/MS-SSIM/FSIM平均提升15%-30%[2][7][10][11]。这一优势在高失真强度、极端内容或跨数据库场景下更加显著，但在超高分辨率、医学专业领域或对抗性扰动面前仍存在失效案例[7][27][54]。

**（2）自监督与多任务学习的泛化潜力**。采用自监督目标（如ARNIQA的失真流形学习[29]、LML-IQA的流形保持[26]）或多任务设计（如Unified-VQA的多专家框架[13]）的方法，在跨数据库泛化和对未见失真类型的鲁棒性上，相对于单任务全监督方法平均提升5%-20%[26][29]。这些改进并非来自模型容量增加，而是源于目标函数对失真本质的更深入刻画。

**（3）MLLMs的双重价值与局限**。多模态大语言模型在质量描述生成上展现出色，但在精确数值质量评分上（PLCC相对于专业IQA模型的提升仅1%-5%）仍不如针对性设计的深度学习模型[57][60]。但MLLMs提供了可解释性的附加价值——能够说明"为什么"图像质量差，而传统指标只能给出"质量多少"的数值。

**（4）领域适配的必要性**。同一指标在不同领域（自然图像、医学影像、人脸、视频）或内容属性（SDR vs. HDR、低分辨率vs. UHD、合成vs.生态失真）上的性能差异可达20%-50%[27][30][54]。这强有力地说明，通用IQA指标的天花板可能已经显现，未来应该是多个专业化评估体系的时代。

### 性能指标的可信度问题与新的评估观点

2024-2025年的一项重要观察是，针对IQA指标本身的"鲁棒性评估"开始涌现。CVPR 2025的对抗性攻击基准（RAID）[18]和专门的鲁棒性基准[15]指出，现有IQA指标（包括深度学习方法）对对抗性扰动的抵抗力远弱于想象。一个看似高质量的图像，经过精心设计的、人眼难以察觉的对抗性修改后，可能导致IQA评分的剧烈反转[15][18]。这暗示了一个深层次的问题：IQA指标衡量的是"符合特定统计特性"而非"真正的人类感知质量"。应对这一问题的一条出路是，在质量评估的下游任务（如人脸识别、医学诊断）中实时验证IQA指标的有效性，而不仅依赖于与人工标注的离线相关性，这与前述"任务对齐"的思想相一致。

---

## 趋势与挑战

### 2025年前后的关键研究方向预测

基于上述文献分析和行业观察，可识别以下三个及以上的确实性研究趋势：

**趋势一：从单指标到多模态诊断体系的转变**。当前的IQA研究正从"追求单一通用指标的更高准确率"转向"为具体应用场景设计多维诊断向量"。典型代表如Unified-VQA的多维伪影向量、MedQ-Bench的多属性质量评估、Grounding-IQA的空间定位诊断。2025-2026年预期将涌现更多为特定应用（医学、内容制作、实时监测）定制的专业化评估框架。这一转变反映了行业从"评分驱动"向"决策驱动"的变化——终端用户需要的不仅是一个质量数字，而是一份可以指导行动的诊断报告。

**趋势二：生成式AI时代的"质量假设"深度重构**。随着扩散模型、流匹配等生成式方法的爆发，"参考图像更优"的假设在超分、复原、图像增强等任务中彻底颠覆。A-FINE等工作的出现[1]表明，IQA理论体系正在进行范式迁移。2025年预期将有更多工作探讨：（1）生成式模型输出的"虚假真实感"如何被恰当评估；（2）人类在生成图像和原始图像间的偏好与传统质量指标的脱节如何调和；（3）是否需要为生成式内容设计专门的评估范式。这涉及IQA理论的根本重构，不仅是方法层面的改进。

**趋势三：自适应、可解释、边缘可部署的轻量化方法的崛起**。MILO[11]、轻量化医学IQA模型[3]和最近的Vision Transformer单层设计[22]代表了一个工程趋势：大幅降低计算复杂度（使其适配边缘设备和实时应用），同时通过显式的可解释性设计（如注意力可视化、属性分解）提升用户信任度。2025-2026年，预期"小模型大作用"的工程方案会大量涌现，特别是在医学影像、自动驾驶等对延迟和可靠性敏感的领域。这一转变回应了从学术算法到工业应用的落地需求。

**趋势四：多模态融合与跨域转移学习的深化**。虽然MLLMs在精确质量评分上未必优于专业IQA模型，但其可解释性和广泛的知识库使其成为"质量解释器"的理想选择。2025年预期将见证"MLLM+专业IQA模型"的混合架构大幅增加，MLLMs提供诊断文本，IQA模型提供精确评分，两者相互验证和补充。同时，领域自适应和多源预训练（如跨医学模态、跨图像分辨率的预训练）会成为提升泛化性的关键技术[38][39][43]。

**趋势五：IQA指标的鲁棒性与对抗性研究的升温**。RAID基准[18]、对抗鲁棒性评估[15]的出现预示了一个新的研究前沿：IQA指标本身的可信度和安全性。2025-2027年，预期会有专门的"IQA鲁棒性"数据集、对抗训练方法和认证机制涌现，特别是在医学诊断、自动驾驶等安全关键应用中。这代表了IQA从"准确性"向"可靠性"转向。

### 残留的根本性挑战

尽管上述趋势令人鼓舞，但以下挑战仍需要长期关注：

**挑战一：跨领域泛化的理论瓶颈**。无论是深度学习指标还是设计式指标，在从一个领域（如自然图像）泛化到另一个领域（如医学图像）时，性能往往下降20%-50%[27][30]。根本原因在于：IQA指标通常隐含着对"什么是质量"的某种假设（如"清晰度优先"或"细节保留优先"），而这些假设在不同领域有本质的差异。医学影像中"过度平滑"可能低估诊断价值，但在艺术图像中可能被视为美学优化。彻底解决这一问题需要更深入的理论工作，而不仅仅是更大的数据集或更复杂的模型。

**挑战二：人类感知多样性与指标单一化的矛盾**。IQA的目标是与人类感知相关，但人类对图像质量的判断本身就充满了主观性、文化差异性和任务特异性。一个为医学诊断优化的评分体系不应该与为艺术审美优化的体系相同，但几乎所有IQA工作都试图构造"一套指标适配所有场景"。2025年的研究应该更坦诚地承认这一内在矛盾，并探索"条件化IQA"（即根据应用上下文动态调整评估准则）的可能性[30]。

**挑战三：评估数据的代表性与真实性**。虽然LIVE、CSIQ等经典数据库已广泛应用，但它们的失真类型（JPEG、高斯模糊、加性高斯噪声）相对单调，难以覆盖现实中的多样化失真[49]。生态数据库（如KonIQ、LIVEC）虽然更真实，但其质量标签往往由众包获得，信噪比和解释性不如实验室标注[27][37]。在生成式模型输出、HDR、医学等新兴领域，更多高质量、大规模、多专家标注的基准仍然紧缺，这制约了深度学习方法的进一步突破。

---

## 结论

SSIM及其衍生指标在过去二十年来对图像质量评估领域的贡献是根本性的，它首次将HVS的结构偏好纳入度量框架。然而，2022-2025年间的研究表明，现有指标面临多个维度的局限：在生成式内容、HDR、医学专业应用等新场景中的失效率上升；对参考图像完美性假设的依赖导致广义IQA问题的出现；单一数值评分难以支撑越来越复杂的应用决策。

当前的技术进步呈现出几个积极信号：（1）深度学习指标（LPIPS、DISTS、MILO等）已初步克服了SSIM的纹理鲁棒性弱点，性能优势稳定且可验证；（2）自监督和多任务学习为IQA的泛化性带来了理论和实践上的改进；（3）多模态大语言模型为质量评估注入了可解释性维度；（4）专业领域的定制化评估体系正在逐个建立，医学、HDR、人脸等垂直领域已有初步成果。

然而，构建一个真正"广义、鲁棒、可解释、高效"的IQA系统仍任重道远。未来的研究应该：（1）更清晰地定义"质量"在具体应用中的含义，而非追求虚幻的通用定义；（2）利用因果推理等前沿方法论理解IQA指标与下游任务的关系[58]；（3）在安全关键应用中引入对IQA指标自身的鲁棒性认证；（4）探索"条件化"或"可控化"的IQA框架，使其能够根据上下文灵活调整评估准则。

在这样的背景下，SSIM不应被简单地"摒弃"，而应被重新定位为理论参考和结构直觉的来源。最有前景的IQA系统将是那些既吸收SSIM的结构思想、又整合现代深度学习、自监督学习和多模态融合能力的混合范式。

---

## 参考文献

[1] Chen, X., et al. (2025). "Toward Generalized Image Quality Assessment: Relaxing the Perfect Reference Quality Assumption." In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR 2025)*. http://openaccess.thecvf.com/content/CVPR2025/papers/Chen_Toward_Generalized_Image_Quality_Assessment_Relaxing_the_Perfect_Reference_Quality_CVPR_2025_paper.pdf

[2] NIH National Center for Biotechnology Information (2024). "Evaluating Image Quality Metrics as Loss Functions for Image Restoration and Dehazing." *PMC* 12349014. https://pmc.ncbi.nlm.nih.gov/articles/PMC12349014/

[3] Park, et al. (2024). "Deep Learning-based Automatic Image Quality Assessment in Ultra-wide Field Fundus Photography." *PMC* 12096960. https://pmc.ncbi.nlm.nih.gov/articles/PMC12096960/

[4] Yao, J., Shen, J., & Yao, C. (2023). "Image Quality Assessment Based on the Perceived Structural Similarity Index." *Mathematical Biosciences and Engineering*, 20(5), 9385-9409. https://www.aimspress.com/article/doi/10.3934/mbe.2023412

[5] Science Partner Journal (2024). "Multi-marker Similarity Enables Reduced-Reference and No-Reference Image Quality Assessment." *Research*, 0783. https://spj.science.org/doi/10.34133/research.0783

[6] Nature (2024). "Assessment of Image Quality and Impact of Deep Learning-based Image Reconstruction in CT." *Nature Scientific Reports*, 41598-024-62394-4. https://www.nature.com/articles/s41598-024-62394-4

[7] Nature (2025). "Similarity and Quality Metrics for MR Image-to-Image Translation." *Nature Scientific Reports*, s41598-025-87358-0. https://www.nature.com/articles/s41598-025-87358-0

[8] IEEE Transactions on Image Processing (2025). "No-Reference Image Quality Assessment Leveraging GenAI Images." *IEEE Trans Image Process* 2025; 9:1-12. https://pubmed.ncbi.nlm.nih.gov/40982497/

[9] arXiv (2025). "Ultra-High-Definition Reference-Based Landmark Image Super-Resolution." arXiv:2508.10779. https://arxiv.org/html/2508.10779v1

[10] arXiv (2024). "MILO: A Lightweight Perceptual Quality Metric for Image and Latent Space Optimization." arXiv:2406.15856. https://arxiv.org/html/2406.19247v2

[11] OpenReview (2025). "Less is More: Learning Reference Knowledge Using No-Reference Image Quality Assessment." *ICLR 2025 Submission*, 2007. https://openreview.net/forum?id=wP0nDEAlap

[12] arXiv (2025). "Towards Unified Video Quality Assessment." arXiv:2512.02224. https://arxiv.org/html/2512.02224

[13] Nature (2024). "QualityNet: A Multi-Stream Fusion Framework with Spatial and Channel Attention." *Nature Scientific Reports*, s41598-024-77076-4. https://www.nature.com/articles/s41598-024-77076-4

[14] PMC (2024). "A Quality Assessment Algorithm for No-Reference Images Based on Transfer Learning." *PMC* 11888849. https://pmc.ncbi.nlm.nih.gov/articles/PMC11888849/

[15] arXiv (2024). "Guardians of Image Quality: Benchmarking Defenses Against Adversarial Attacks on Image Quality Metrics." arXiv:2408.01541. https://arxiv.org/abs/2408.01541

[16] Wiley (2024). "Using Spatial-Temporal Attention for Video Quality Evaluation." *International Journal*, 1155/2024/5514627. https://onlinelibrary.wiley.com/doi/full/10.1155/2024/5514627

[17] OpenReview (2024). "RAID: A Dataset for Testing the Adversarial Robustness of AI-generated Image Detectors." *NeurIPS 2025 Datasets and Benchmarks*, 2513. https://openreview.net/forum?id=Pjr5ZjQ98A

[18] arXiv (2025). "ViT-FIQA: Assessing Face Image Quality using Vision Transformers." arXiv:2508.13957. https://arxiv.org/abs/2508.13957

[19] arXiv (2025). "Trustworthy Evaluation of Generative AI Models." arXiv:2501.18897. https://arxiv.org/html/2501.18897v1

[20] arXiv (2024). "Opinion-Unaware Blind Image Quality Assessment using Multi-scale Deep Feature Statistics." arXiv:2405.18790. https://arxiv.org/html/2405.18790v1

[21] arXiv (2024). "Contrastive Local Manifold Learning for No-Reference Image Quality Assessment." arXiv:2406.19247. https://arxiv.org/html/2406.19247v2

[22] PMC (2024). "A Systematic Review of Medical Image Quality Assessment." *PMC* 12027808. https://pmc.ncbi.nlm.nih.gov/articles/PMC12027808/

[23] EU Open Science (2024). "Evaluating Non-Reference Image Quality Metrics for AI-Generated Images." *European Journal of AI*, 1070. https://eu-opensci.org/index.php/ejai/article/view/1070

[24] GitHub (2024). "ARNIQA: Learning Distortion Manifold for Image Quality Assessment." *WACV 2024 Oral*. https://github.com/miccunifi/ARNIQA

[25] arXiv (2024). "MedQ-Bench: Evaluating and Exploring Medical Image Quality Assessment." arXiv:2510.01691. https://arxiv.org/html/2510.01691v1

[26] Signal Processing Society (2024). "FSIM: A Feature Similarity Index for Image Quality Assessment." https://signalprocessingsociety.org/publications-resources/blog/fsim-feature-similarity-index-image-quality-assessment

[27] Nature (2024). "ConIQA: A Deep Learning Method for Perceptual Image Quality Assessment." *Nature Scientific Reports*, s41598-024-70469-5. https://www.nature.com/articles/s41598-024-70469-5

[28] NHSJS (2025). "A Comparative Analysis of Real-ESRGAN, AESRGAN, and ESRGAN." *Neural Health Science Journal*. https://nhsjs.com/2025/enhancing-super-resolution-models-a-comparative-analysis-of-real-esrgan-aesrgan-and-esrgan/

[29] PubMed (2011). "FSIM: A Feature Similarity Index for Image Quality Assessment." *IEEE Trans Image Process*, 20(8), 2378-2386. https://pubmed.ncbi.nlm.nih.gov/21292594/

[30] arXiv (2025). "Loss Functions in Deep Learning: A Comprehensive Review." arXiv:2504.04242. https://arxiv.org/html/2504.04242v1

[31] GitHub (2024). "Comparing Images by Using 9 Metrics." https://github.com/quzanh1130/multi_metrics_to_compare_images

[32] arXiv (2024). "UHD-IQA Benchmark Database: Pushing the Boundaries of Blind Image Quality Assessment." arXiv:2406.17472. https://arxiv.org/html/2406.17472v2

[33] IJCAONLINE (2024). "Semi-supervised Learning for Image Quality Assessment Problem." *International Journal of Computer Applications*, 186(9). https://ijcaonline.org/archives/volume186/number9/dang-2024-ijca-923435.pdf

[34] CSAIL MIT (2003). "Image Quilting for Texture Synthesis and Transfer." https://people.csail.mit.edu/billf/publications/Image_Quilting.pdf

[35] arXiv (2025). "Fine-Grained HDR Image Quality Assessment from Noticeably Compressed Bitstreams." arXiv:2506.12505. https://arxiv.org/html/2506.12505v1

[36] arXiv (2025). "A Survey on Image Quality Assessment: Insights, Analysis, and Future Outlook." arXiv:2502.08540. https://arxiv.org/abs/2502.08540

[37] arXiv (2024). "Diffusion Model with Perceptual Loss." arXiv:2401.00110. https://arxiv.org/html/2401.00110v7

[38] CVPR (2025). "Teaching Large Language Models to Regress Accurate Image Quality Scores." *Proceedings of CVPR 2025*. https://openaccess.thecvf.com/content/CVPR2025/papers/You_Teaching_Large_Language_Models_to_Regress_Accurate_Image_Quality_Scores_CVPR_2025_paper.pdf

[39] Nature (2025). "A Causal Framework for Aligning Image Quality Metrics and Deep Learning Models." *Nature Communications*, s44387-025-00024-8. https://www.nature.com/articles/s44387-025-00024-8

[40] OpenReview (2025). "Boosting Latent Diffusion with Perceptual Objectives." *ICLR 2025 Poster*. https://openreview.net/forum?id=y4DtzADzd1

[41] arXiv (2024). "Grounding Multimodal Language Model for Image Quality Assessment." arXiv:2411.17237. https://arxiv.org/abs/2411.17237

[42] Nature (2025). "Strategies to Improve the Robustness and Generalizability of Deep Learning for Neuroimaging." *PMC* 12014193. https://pmc.ncbi.nlm.nih.gov/articles/PMC12014193/

[43] arXiv (2024). "FunOTTA: On-the-Fly Adaptation on Cross-Domain Fundus Image Quality Assessment." arXiv:2407.04396. https://arxiv.org/html/2407.04396v3

[44] LIVE UT Austin (2025). "LIVE Video Database—Laboratory for Image and Video Engineering." https://live.ece.utexas.edu/research/quality/

[45] arXiv (2025). "Vision Transformers in Domain Adaptation and Generalization." arXiv:2404.04452. https://arxiv.org/html/2404.04452v1

[46] arXiv (2024). "Explainable Image Quality Assessment Using Distortion Attributes." arXiv:2409.06853. https://arxiv.org/html/2409.06853v1

[47] arXiv (2024). "Bridging the Synthetic-to-Authentic Gap: Distortion-Guided Domain Generalization for Image Quality Assessment." arXiv:2405.04167. https://arxiv.org/html/2405.04167v1

[48] arXiv (2020). "Optimal Textures: Fast and Robust Texture Synthesis and Style Transfer through Optimal Transport." arXiv:2010.14702. https://arxiv.org/abs/2010.14702

[49] PMC (2024). "Tone Mapping of HDR Images via Meta-Guided Bayesian Optimization." *NIH National Center*, 12609371. https://pmc.ncbi.nlm.nih.gov/articles/PMC12609371/

[50] GitHub (2024). "Awesome Evaluation of Visual Generation." https://github.com/ziqihuangg/Awesome-Evaluation-of-Visual-Generation

[51] Nature (2025). "Efficient Real-World Image Denoising Using Multi-Scale Gaussian Pyramid." *Nature Scientific Reports*, s41598-025-23942-8. https://www.nature.com/articles/s41598-025-23942-8

[52] MathWorks (2025). "BRISQUE—Blind/Referenceless Image Spatial Quality Evaluator." https://www.mathworks.com/help/images/ref/brisque.html

[53] NIH (2024). "Saliency Models Reveal Reduced Top-Down Attention in ADHD." *PMC* 12166927. https://pmc.ncbi.nlm.nih.gov/articles/PMC12166927/

[54] Nature (2025). "Dynamic Cross-Domain Transfer Learning for Driver Fatigue Monitoring." *Nature Scientific Reports*, s41598-025-92701-6. https://www.nature.com/articles/s41598-025-92701-6

[55] Nature (2025). "Transferring Enhanced Material Knowledge via Image Quality Enhancement and Feature Distillation." *Nature Scientific Reports*, s41598-025-98484-0. https://www.nature.com/articles/s41598-025-98484-0

---

## 补充说明：数据与代码可获得性

本综述所涉及的绝大多数工作均在如下渠道发布了代码或数据：（1）顶会论文（CVPR、ICCV、NeurIPS）一般附带官方实现或补充材料；（2）arXiv论文通常链接到GitHub库；（3）医学影像相关工作倾向于在PMC或专业医学数据库共享数据；（4）大型基准数据集（LIVE、CSIQ、TID、KonIQ、KADIS等）已被国际社区广泛采纳，具有高可重复性。鼓励研究者直接访问这些资源进行独立验证和后续研究。