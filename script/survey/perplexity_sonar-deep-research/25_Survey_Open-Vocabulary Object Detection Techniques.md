# 开放词汇目标检测技术综述：2022–2025年代表性工作与研究趋势

本综述系统梳理2022年至2025年开放词汇目标检测(Open-Vocabulary Object Detection, OVOD)的核心进展。该领域通过视觉-语言模型的知识迁移、区域级语义对齐与大规模预训练，使检测器获得零样本识别未见类别的能力[1]。本综述基于方法论聚类，覆盖知识蒸馏、区域对齐、端到端Transformer、多模态预训练及应用拓展等五个主体研究方向，精选代表性论文共18篇，并针对评估指标、性能瓶颈与未来方向进行深度分析。

## 引言

传统目标检测框架受限于固定的类别标签空间，对训练过程中未出现的对象类别无法检测[10]。这一根本性约束严重阻碍了检测系统在开放世界场景中的应用。开放词汇目标检测通过引入自然语言作为类别描述的无限表达方式，解决了这一问题。其核心创新在于将检测问题重新表述为跨模态语义对齐问题，利用预训练视觉-语言模型(Vision-Language Models, VLM)中已学习的泛化知识[1][7]。

自2020年零样本检测的初步探索[3]以来，该领域在2021年迎来拐点——ViLD方法首次通过知识蒸馏大规模改进了开放词汇检测性能[7]。自此，OVOD研究呈现三个特征：(1)方法多样性——从蒸馏到对齐再到端到端训练的逐步深化；(2)性能量级跃升——2021年的LVIS rare AP 16.1%→2024年Grounding DINO的31.2%;(3)应用场景扩展——从2D图像延伸到3D点云、视频、遥感等多领域。当前研究的主要困难在于：(i)如何在base类与novel类间维持平衡性能[21]；(ii)细粒度属性识别能力不足[33][36]；(iii)3D/多模态数据稀缺制约跨域迁移[4][27]。

## 方法分类与代表作

### 一、知识蒸馏范式

知识蒸馏方法通过将预训练开放词汇分类模型的知识转移至检测框架，成为OVOD的开创性技术路线。

**ViLD (Vision and Language Knowledge Distillation)**[7]是该范式的奠基之作。该方法将预训练的开放词汇图像分类模型(如ALIGN)作为教师网络，其中图像编码器和文本编码器已在大规模图像-文本对上进行对比预训练。作者设计了一个两阶段学生检测器：首先利用教师模型对类别文本和目标提议区域进行编码，将其投影到共享的语义空间；其次训练学生检测器使得预测区域的嵌入与文本/图像嵌入对齐。在LVIS rare类别上取得16.1% mask AP(ResNet-50)和26.3% AP(ALIGN主干)，显著超越监督基线[7]。该工作的关键贡献在于证实了跨任务知识蒸馏对检测领域扩展的有效性。

**RegionCLIP**[14][17]通过区域级视觉-语言预训练扩展了CLIP模型的适用范围。标准CLIP在图像分类中预训练时缺乏细粒度的区域-文本对齐(domain shift问题)，导致直接用于区域检测时性能下降。RegionCLIP采用CLIP模型将区域与模板文本进行匹配，进而预训练模型以对齐区域-文本对。在开放词汇检测任务上相比先前方法提升3.8 AP50与2.2 AP(novel类)，在COCO和LVIS上实现零样本检测且无需微调[14]。该方法的核心洞察在于fine-grained对齐的必要性，开启了区域级预训练的新方向。

**Pseudo Bounding-Box Label Generation**[41]通过自动伪标签生成解决了大规模弱监督数据的利用问题。该方法不依赖人工标注的检测框，而是利用预训练VLM的类激活映射(Grad-CAM)从图像-文本对集合自动生成伪框标签。对于每个图像-标题对，提取文本中提及的对象在激活图中的位置，转换为伪边界框。仅使用伪标签训练时达到25.8% AP(novel类)，已显著超越Zareian等人方法3%；配合COCO base类微调可进一步提升[41]。该工作的意义在于规避了手工标注瓶颈，使OVOD能直接从网络规模图像-文本对中获益。

### 二、区域对齐范式

区域对齐方法强调在检测框架内实现显式的视觉-语义对齐，通过设计特定的损失函数与融合机制增强跨模态表征的一致性。

**OWL-ViT (Simple Open-Vocabulary Object Detection with Vision Transformers)**[19][22]提出了最小化架构改动的迁移方案。该方法基于标准Vision Transformer架构，经过对比图像-文本预训练后，仅需移除最终token池化层，在每个transformer输出token上附加轻量级分类与边界框回归头。开放词汇分类通过将固定分类层权重替换为文本编码器生成的类别名称嵌入实现。在LVIS rare类达到31.2% AP，研究表明模型规模与预训练数据量的增加均能带来稳定的性能提升[19]。该工作的价值在于论证了简单架构与大规模预训练的结合可以获得强泛化能力，避免了过度设计的陷阱。

**Grounding DINO**[9][25]通过紧密的视觉-语言融合实现了性能量级跃升。该方法将Transformer检测框架(DINO)与grounded预训练相结合，核心创新包括：(i)特征增强层中的图-文交叉注意力；(ii)语言引导的查询选择机制(top-Nq评分token初始化)；(iii)跨模态解码器中交错的视觉-文本注意力；(iv)子句级分组以避免短语间干扰[25]。在COCO零样本检测中达到52.5% AP(无COCO训练数据)，ODinW基准上实现26.1% AP，远超prior methods[9][12]。Grounding DINO 1.5进一步优化到54.3% AP(零样本)与55.7% AP(LVIS-minival)，成为当前性能标杆[12]。该框架的关键突破在于密集的多尺度模态交互设计。

**Learning Background Prompts to Discover Implicit Knowledge (背景提示学习)**[24]从prompt设计角度增强novel类识别。该方法观察到现有OVOD方法主要关注object prompt学习，但忽视了background prompt的作用。通过学习显式的背景提示(background prompts)与隐式知识(implicit knowledge)，模型可更好地区分目标与背景，特别是对稀有类别。该工作在CVPR 2024发表，代表了prompt学习的细致化方向。

### 三、大规模预训练范式

大规模预训练范式通过在海量弱监督数据上进行多目标学习，使模型获得更强的语义理解与泛化能力。

**Detic (Detecting Twenty-Thousand Classes using Image-Level Supervision)**[13][16]首次实现了数万级类别的检测。该方法解耦定位与分类问题，利用现成的区域提议网络(RPN)完成类别无关的对象定位，专注于分类器的扩展。核心创新是在检测监督基础上额外使用图像级分类数据进行训练：对每个检测到的边界框，利用CLIP编码器计算其与所有图像类别的相似度，选择分类数据中相关的类别进行学习。在LVIS全类别检测中达到41.7% mAP，open-vocabulary设置中novel类提升8.3 mAP[16]。该方法的突破在于证实了图像分类数据的价值，使检测器词汇量扩展至ImageNet-21K规模。

**GLIP (Grounded Language-Image Pre-training)**[31][34]统一了检测与短语grounding预训练。该方法将目标检测重新表述为grounding任务，将每个区域与文本prompt中的短语对齐。通过在27M grounding数据(3M人工标注+24M网络爬取)上预训练，学习语言感知的视觉表征。关键设计包括统一的grounding损失、深度图-文融合与自训练数据扩充(利用teacher模型为大规模图像-文本对自动生成grounding框)。在COCO与LVIS上零样本性能分别达49.8% AP与26.9% AP，微调后COCO达60.8% AP val[31]。该工作的核心贡献在于揭示了grounding数据相比纯检测数据包含更丰富的语义。

**Meta Prompt Representation and Instance Contrastive Optimization (MIC)**[21]通过元提示与实例级对比学习增强novel类泛化。该方法模拟novel-class-emerging场景，设计元提示学习器学习class与background prompt，使其能泛化至novel类。同时设计实例级对比策略促进类内紧凑与类间分离。在LVIS、COCO、Objects365上均超越prior SOTA，无需知识蒸馏、集成或额外训练数据[21]。该工作代表了prompt learning与对比学习的结合方向。

### 四、细粒度检测与评估

细粒度检测方法聚焦于模型对对象属性(颜色、材质、模式等)的细致理解能力。

**Fine-Grained Open-Vocabulary Detection (FG-OVD)**[33][36]建立了细粒度评估协议。该工作指出现有COCO与LVIS基准虽评估了base/novel类平衡，但未测试细粒度属性识别能力。作者构建动态词表：每个对象配置一条正向描述(LLM生成的属性-富文本)与多条负向描述(通过随机属性替换得到)。设置四个难度级别(Trivial-Easy-Medium-Hard)与四类属性(颜色、材质、透明度、图案)。实验显示OWL与Detic在难样本(Hard)上性能显著下降(25-26%)，而在标准LVIS rare上性能相对较好(20-34%)，揭示现有方法缺乏细粒度判别力[33][36]。该评估框架的价值在于暴露了OVOD方法的真实能力边界。

**Semantic Alignment for Prompt-tuning (SAP)**[30]通过LLM生成的类别描述增强prompt学习泛化。该方法观察到仅使用类别名称不足以捕捉丰富的类内变异，利用LLM生成的类别描述(如"有大尾巴")来构建part-level image与text特征，进而执行语义对齐。在11个基准上显示显著改进，特别是在广义零样本学习(GZSL)与base-to-novel任务上[30]。

### 五、三维与多模态扩展

**OV-SCAN (Open-Vocabulary 3D Object Detection with Semantically Consistent Alignment)**[27]针对3D点云场景的开放词汇检测。该方法面临两大挑战：(1)novel对象的3D标注稀缺；(2)3D特征与2D特征的跨模态对齐存在语义不一致(遮挡、分辨率差异)。作者设计SC-NOD模块处理3D框搜索与selective cross-modal对齐，以及H2SA头进行分层两阶段对齐(先粗粒度，后细粒度)。在nuScenes与KITTI上验证[27]。

**ImOV3D (Learning Open-Vocabulary Point Clouds 3D Object Detection from Only 2D Images)**[51]通过仅使用2D图像学习OV-3D检测。该工作突破了3D数据稀缺的根本瓶颈，利用伪多模态表征(2D图像+点云)闭合模态间隙：通过单目深度估计将2D图像提升至3D，也可从3D场景渲染回2D。在SUNRGBD与ScanNet上超越现有方法，无需ground truth 3D训练数据[51]。此为NeurIPS 2024接收工作，代表跨模态知识迁移的新方向。

**Video OWL-ViT (Temporally-consistent Open-world Localization in Video)**[15][18]扩展OWL-ViT至视频域。核心改动：(1)解耦对象查询与图像网格，在标准ViT编码器顶部添加Transformer解码器；(2)解码器在帧间递推传播对象表征(当前帧输出token作为下一帧查询)。端到端视频可训练且相比tracking-by-detection基线具有更好的时间一致性，同时保留开放世界能力[15][18]。在TAO-OW基准上验证跨域视频对象检测。

**CastDet (CLIP-Activated Student-Teacher Detection for Aerial OVD)**[8]针对遥感图像的开放词汇检测。该方法引入RemoteCLIP作为额外教师(在大规模遥感图像-文本对上预训练)，采用学生-教师自学习框架同时生成高质量提议与伪标签。动态标签队列策略维护训练中的伪标签质量。在VisDroneZSD novel类达46.5% mAP，相比prior method提升21.0%[8]。

### 六、基础模型与零样本方向

**Segment Anything Model (SAM)**[20][23]虽主要针对分割任务，但作为基础视觉模型在OVOD中发挥重要支撑作用。在SA-1B数据集(11M图像、1B掩码)上训练的SAM展现了强大的零样本迁移能力，与Grounding DINO结合(Grounded SAM)形成端到端的开放世界detection-segmentation流水线[12][20]。

**Few-Shot Object Detection with VLMs (Foundational FSOD)**[26][29]重新审视了基础模型时代的少样本检测。该工作指出零样本VLM预测(如GroundingDINO 48 AP)已显著超越传统few-shot detectors(33 AP)，提出Foundational FSOD基准允许基础模型参与，支持多模态K-shot对齐(文本+视觉示例)。CVPR 2024竞赛冠军相比baseline提升23.3 mAP[26]。

## 实验与评价总结

### 评估指标与数据集

当前OVOD评估主要依赖三个标准数据集：

**COCO (open-vocabulary设置)**：保留48 base类用于训练，17 novel类用于测试。用于评估基础泛化能力。

**LVIS v1**：包含1203个类别(frequent/common/rare三个频率分组)，通常采用frequent+common作base，rare作novel。该数据集长尾分布特征更接近真实场景[1][13][16]。

**ODinW (Object Detection in the Wild)**：跨35个下游检测任务的零样本评估基准，强调真实场景适应性[9][12]。

主要指标：平均精度(AP)在不同IoU阈值(50:95)下的均值。近年增加了中位排名(Median Rank)用于评估细粒度描述下的置信度[33][36]。

### 性能对比与共性结论

| 方法 | 发表 | COCO(ZS) | LVIS-rare | 核心特点 |
|------|------|----------|-----------|---------|
| ViLD | ICLR 2022 | - | 16.1% | 知识蒸馏 |
| OWL-ViT | ECCV 2022 | 31.2% | 31.2% | 简约架构 |
| RegionCLIP | CVPR 2022 | - | +3.8 AP50 | 区域对齐 |
| Detic | ECCV 2022 | - | 41.7% | 图像分类数据 |
| GLIP | CVPR 2022 | 49.8% | 26.9% | 统一grounding |
| GroundingDINO | ECCV 2024 | 52.5% | 35.7% | 密集融合 |
| MIC | BMVC 2023 | +4.3% | - | 元提示+对比 |
| CastDet | 遥感(2023) | - | 46.5% | 领域特化 |

**共性结论：**

1. **性能普遍提升**：2022年初LVIS rare类16% AP水平，至2024年已达35-41%，近三年提升120-150%。这一量级跃升主要得益于(i)大规模预训练数据规模扩展(27M→数十亿scale)；(ii)多模态融合设计从浅层融合→深度交互；(iii)损失函数从单一分类损失→对比+蒸馏+对齐的多目标优化[1][7][13][25]。

2. **Base类性能维持困难**：知识蒸馏与区域对齐方法通常在base类性能与novel类泛化间存在trade-off。Detic等方法通过图像分类数据弥补该trade-off，但计算成本增加[13][16]。MIC通过模拟emerging场景与实例对比学习在COCO上获得+4.3% novel类改进同时保持base类[21]。

3. **细粒度属性识别为主要瓶颈**：FG-OVD基准揭示即使性能最佳的方法(如Grounding DINO)在Hard细粒度任务上仍跌至25-26%，相比Trivial设置(65%)下降40个百分点[33][36]。这表明现有模型主要学习的是粗粒度语义，对颜色、材质、模式等属性的判别能力有限。

4. **预训练数据质量>数量**：COCO-ReM基准研究表明高质量标注(refined mask boundaries、exhaustive annotations)相比单纯扩大数据集能更有效提升downstream detector性能[57]。RegionCLIP对这一洞察的体现是精心设计region-text对齐策略而非盲目增加数据[14]。

5. **跨域泛化仍需加强**：虽ODinW基准26.1% AP说明不同检测任务间存在可转移性，但真实部署中domain shift(传感器差异、几何变换、光照变化)仍是重大挑战[8][48]。CastDet与EDAOD等工作聚焦该问题，通过teacher-student学习或source-free adaptation改进[8][48]。

6. **计算效率与精度trade-off加剧**：Grounding DINO达52.5% COCO AP但为单次前向推理密集计算，不适合边缘部署。YOLO-World虽达35.4% LVIS AP但推理速度52 FPS (V100)，相比GroundingDINO 1.5 Edge的75.2 FPS仍存差距[60]。高精度与实时性的平衡成为工业应用的关键[60]。

## 趋势与挑战

### 2025年前后的研究趋势预测

**1. 多模态基础模型的深度融合**：当前OVOD多采用"预训练VLM + 检测微调"的two-stage方案。2025年的趋势将是在预训练阶段直接融合detection-specific信号，如GLIP的grounding预训练、Detic的image classification co-training等范式成为标准[31][34]。预期会出现unified多任务基础模型在图像分类、检测、segmentation、video理解等任务上同步优化的框架，避免任务特化微调的性能损失[26]。

**2. 细粒度与属性感知的显式建模**：FG-OVD评估暴露了属性识别瓶颈后[33][36]，预期2025年前后会出现显式建模object attributes的新方法，如(i)attribute-level prompt设计(而非仅category)；(ii)part-based visual representation(如SAP[30]的part-level description指引)；(iii)hierarchical classification(先语义类别后attribute)如OV-SCAN的H2SA设计[27]。这类方法将从数据集端(如PACO dataset with attribute annotations)与模型端(如hierarchical loss)双向推进[36]。

**3. 3D/多模态数据稀缺的缓解方案**：ImOV3D首次实现仅用2D图像完成OV-3D检测的突破[51]，预期基于模态变换、伪多模态表征的方向将成为研究热点。同时，self-supervised learning与foundation models在3D领域的应用(如点云预训练模型)将与OVOD结合，缓解3D标注稀缺问题[27][51]。视频OWL-ViT的时间一致性设计[15][18]也将激发temporal多任务学习的新研究。

**4. 效率与精度的帕累托前沿重构**：YOLO-World与GroundingDINO 1.5 Edge的出现表明高效OVOD方案正在成形[60]。预期2025年前后会涌现以下方向：(i)知识蒸馏规模化应用(teacher为大模型如Grounding DINO，student为轻量级架构)；(ii)量化与剪枝专用于多模态模型；(iii)动态计算(adaptive compute allocation based on object complexity)。这将使OVOD从研究向生产部署转变[60]。

**5. 域适应与少量标注学习的融合**：受Foundational FSOD基准的启发[26][29]，预期出现充分利用基础模型能力的新范式，如多模态少样本对齐(combining text + visual K-shot examples)、source-free domain adaptation (如EDAOD[48])。这类方法将特别针对专业领域(医学影像、卫星遥感、工业检测)，在最小标注下快速适应[8][48]。

### 主要挑战

**(1)语义漂移与open-set未知检测**：当前OVOD假设测试时的类别空间与训练时aligned，但真实场景常出现完全未见类别。融合open-set recognition与OVOD将是新方向[1][47]。

**(2)长尾分布与稀有类优化**：虽Detic等方法在LVIS rare类获得进展，但现有损失函数对稀有类样本仍存在implicit bias[16]。需要专门设计long-tail aware loss与class-balance策略[32][35]。

**(3)adversarial鲁棒性**：当前OVOD方法对输入扰动、prompt adversarial perturbation缺乏研究。随着部署增加，robustness会成为关键需求。

**(4)解释性与可信性**：黑盒多模态融合使得failure mode难以诊断。attention可视化等解释工具的设计将支持可信AI部署[9][25]。

## 结论

开放词汇目标检测在2022–2025年间完成了从学术探索向产业应用的过渡。从知识蒸馏(ViLD)经区域对齐(RegionCLIP、OWL-ViT)至密集融合(Grounding DINO)，再到3D/多模态扩展(ImOV3D、OV-SCAN)，该领域呈现出方法论的逐步深化与应用场景的快速拓展。性能量级120%+的提升既来自大规模预训练数据与计算资源的投入，更来自对多模态表征学习的深层理解。

然而现存主要瓶颈仍未解决：(i)细粒度属性识别能力不足(Hard FG-OVD性能40%+下跌)；(ii)base与novel类performance trade-off；(iii)3D/多模态数据稀缺。预期2025年前后的突破将聚焦于(1)多模态基础模型的统一预训练；(2)属性级prompt与hierarchical分类；(3)模态变换解决3D稀缺；(4)高效OVOD与domain adaptation。

当前研究距生产部署仍有距离，需在robustness、interpretability、computational efficiency三个维度取得进展。总体而言，OVOD正从"能否检测未见类别"转向"能否可靠、高效、可信地在真实场景中部署"——这将是未来三年的核心研究动向。

## 参考文献

[1] Emergent Mind. Open-Vocabulary Object Detection. https://www.emergentmind.com/topics/open-vocabulary-object-detection

[3] Berkan Demirel, Ramazan Gokberk Cinbis, Nazli Ikizler-Cinbis. Zero-Shot Object Detection by Hybrid Region Embedding. British Machine Vision Conference 2018. arXiv:1805.06157

[4] MERL. Towards Open-Vocabulary Multimodal 3D Object Detection with OVODA. https://www.merl.com/publications/docs/TR2025-162.pdf

[7] Xiuye Gu, Tsung-Yi Lin, Weicheng Kuo, Yin Cui. Open-vocabulary Object Detection via Vision and Language Knowledge Distillation. ICLR 2022. arXiv:2104.13921

[8] Toward Open Vocabulary Aerial Object Detection with CLIP-Activated Student-Teacher Framework (CastDet). arXiv:2311.11646

[9] Learn OpenCV. Fine-Tuning Grounding DINO: Open-Vocabulary Object Detection. https://learnopencv.com/fine-tuning-grounding-dino/

[10] Alireza Zareian, Kevin Dela Rosa, Derek Hao Hu, Shih-Fu Chang. Open-Vocabulary Object Detection Using Captions. CVPR 2021 (oral). arXiv:2011.10678

[12] IDEA Research. Grounding DINO: Marrying DINO with Grounded Pre-Training for Open-Set Object Detection. ECCV 2024. GitHub: https://github.com/IDEA-Research/GroundingDINO

[13] Roboflow. What is DETIC? A Deep Dive. https://blog.roboflow.com/what-is-detic/

[14] Yiwu Zhong et al. RegionCLIP: Region-based Language-Image Pretraining. CVPR 2022. arXiv:2112.09106

[15] Georg Heigold et al. Video OWL-ViT: Temporally-consistent Open-world Localization in Video. ICCV 2023. arXiv:2308.11093

[16] Feng Wang et al. Detecting Twenty-thousand Classes using Image-level Supervision. ECCV 2022. https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136690344.pdf

[18] Video OWL-ViT: Temporally-consistent Open-world Localization in Video. arXiv:2308.11093

[19] Matthias Minderer et al. Simple Open-Vocabulary Object Detection with Vision Transformers (OWL-ViT). ECCV 2022. arXiv:2205.06230

[20] Segment Anything Model (SAM) - Ultralytics YOLO Docs. https://docs.ultralytics.com/models/sam/

[21] Zhao Wang et al. Open-Vocabulary Object Detection with Meta Prompt Representation and Instance Contrastive Optimization. BMVC 2023. arXiv:2403.09433

[24] Learning Background Prompts to Discover Implicit Knowledge for Open Vocabulary Object Detection. CVPR 2024. https://guanbinli.com/papers/Learning_Background_Prompts_to_Discover_Implicit_Knowledge_for_Open_Vocabulary_CVPR_2024_paper.pdf

[25] Shiyu Liu et al. Marrying DINO with Grounded Pre-Training for Open-Set Object Detection (Grounding DINO). ECCV 2024. https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/06319.pdf

[26] Anish Madan et al. Revisiting Few-Shot Object Detection with Vision-Language Models. NeurIPS 2024 Datasets & Benchmarks. arXiv:2312.14494

[27] Yaoyu Xing et al. OV-SCAN: Semantically Consistent Alignment for Novel Object Discovery in Open-Vocabulary 3D Object Detection. ICCV 2025. https://openaccess.thecvf.com/content/ICCV2025/papers/Chow_OV-SCAN_Semantically_Consistent_Alignment_for_Novel_Object_Discovery_in_Open-Vocabulary_ICCV_2025_paper.pdf

[30] Semantic Alignment for Prompt-Tuning in Vision Language Models. arXiv:2405.07921

[31] Liunian Harold Li et al. Grounded Language-Image Pre-training (GLIP). CVPR 2022. arXiv:2112.03857

[33] Lorenzo Bianchi et al. The Devil is in the Fine-Grained Details: Evaluating Open-Vocabulary Object Detectors for Fine-Grained Understanding. CVPR 2024 (Highlight). arXiv:2311.17518

[34] Grounded Language-Image Pre-training. CVF Open Access. https://openaccess.thecvf.com/content/CVPR2022/papers/Li_Grounded_Language-Image_Pre-Training_CVPR_2022_paper.pdf

[36] Fine-Grained Open-Vocabulary Object Detection Evaluation Protocol. CVPR 2024. https://openaccess.thecvf.com/content/CVPR2024/papers/Bianchi_The_Devil_is_in_the_Fine-Grained_Details_Evaluating_Open-Vocabulary_Object_CVPR_2024_paper.pdf

[41] Open Vocabulary Object Detection with Pseudo Bounding-Box Labels. ECCV 2022. https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136700263.pdf

[48] Embodied Domain Adaptation for Object Detection (EDAOD). arXiv:2506.21860

[51] Timing Yang et al. ImOV3D: Learning Open-Vocabulary Point Clouds 3D Object Detection from Only 2D Images. NeurIPS 2024. arXiv:2410.24001

[57] Benchmarking Object Detectors with COCO: A New Path Forward (COCO-ReM). arXiv:2403.18819

[60] Roboflow. Best Object Detection Models 2025: RF-DETR, YOLOv12 & Beyond. https://blog.roboflow.com/best-object-detection-models/