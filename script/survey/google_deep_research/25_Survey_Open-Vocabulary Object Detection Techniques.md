开放词汇目标检测技术前沿综述：范式转移、核心架构与未来展望（2022–2025）
摘要
目标检测（Object Detection）作为计算机视觉领域的基石任务，长期以来受限于封闭集（Closed-Set）假设，即模型仅能识别训练阶段预定义的固定类别。然而，随着深度学习向大规模预训练模型时代的演进，打破类别限制、实现对任意自然语言描述物体的检测——即开放词汇目标检测（Open-Vocabulary Object Detection, OVD）——已成为学术界与工业界竞相追逐的战略高地。本报告旨在提供一份详尽的学术综述，深入剖析 2022 年至 2025 年间 OVD 领域的关键技术演进。报告首先界定了 OVD 的核心定义及其与零样本检测、开集识别的本质区别。随后，通过系统分类学，将现有技术流派划分为视觉-语言对齐、区域-文本预训练、伪标签自训练、知识蒸馏、生成式检测以及统一开放世界框架。重点分析了 GLIP、Grounding DINO、YOLO-World、DetLH、CCKT-Det、GenerateU、OW-OVD 及 DINO-X 等代表性工作，深入探讨了其架构创新、损失函数设计及在 LVIS 等基准上的长尾泛化能力。最后，本报告总结了当前领域面临的计算效率、多模态幻觉及属性感知挑战，并展望了由多模态大模型（MLLMs）驱动的具身智能感知新图景。

1. 引言：从封闭视界走向开放世界
1.1 传统目标检测的“封闭集”困境
过去十年，以 Faster R-CNN、YOLO 和 DETR 为代表的目标检测算法在特定数据集上取得了超人般的性能。然而，这些经典模型均建立在全监督学习（Fully Supervised Learning）和封闭集假设之上。模型的识别能力被严格限制在人工标注的类别集合内，例如 COCO 数据集的 80 类或 LVIS 的 1203 类。这种依赖在现实应用中暴露了两个根本性缺陷：

标注成本的不可持续性：为现实世界中无穷无尽的物体类别（如特定型号的工具、罕见的生物物种）收集包围框（Bounding Box）级别的精细标注，在经济上和时间上都是不可承受的。

泛化能力的缺失：面对动态场景中出现的长尾物体或训练集中未曾出现的新概念（Novel Concepts），封闭集模型往往将其错误分类为背景或已知类别，必须重新训练才能适应新需求 。   

1.2 开放词汇目标检测（OVD）的定义与兴起
为了突破上述限制，开放词汇目标检测（OVD）应运而生。OVD 的核心目标是训练一个能够根据自然语言描述（Text Prompts）检测任意物体的模型，即便这些物体在训练阶段从未作为标注类别出现过。

OVD 的技术爆发主要得益于视觉-语言模型（Vision-Language Models, VLMs）的突破性进展，特别是 CLIP（Contrastive Language-Image Pre-training）的出现。CLIP 通过在大规模图像-文本对（Image-Text Pairs）上进行对比学习，学习到了丰富的多模态对齐表征。OVD 研究的核心命题在于：如何将 VLM 强大的图像级（Image-level）零样本分类能力，有效地迁移并适配到区域级（Region-level）的目标检测任务中，同时解决定位（Localization）与识别（Recognition）之间的特征粒度不匹配问题 。   

1.3 关键概念辨析
为了明确研究边界，必须严格区分 OVD 与相关任务：

OVD vs. 零样本检测（ZSD）：早期的 ZSD 依赖于词向量（Word Embeddings）的语义关联，通常只能处理少量未见类别。OVD 可视为广义的 ZSD，但它利用的是海量 VLM 预训练知识，且在设定上允许训练时使用基类（Base Classes）的标注数据，测试时同时评估基类和新类（Novel/Rare Classes）的性能，更强调大规模泛化 。   

OVD vs. 开集识别（Open-Set Recognition, OSR）：OSR 侧重于识别出“未知”物体并将其归类为“Unknown”，而不要求具体命名。OVD 则要求不仅检出，还要基于语言提示具体分类出未见物体 。   

OVD vs. 开放世界检测（OWOD）：OWOD 结合了开集检测和增量学习，旨在发现未知物体并在后续通过人类反馈学习这些新类别。2025 年的最新趋势是 OVD 与 OWOD 的融合，旨在构建既能零样本识别又能主动发现未知的统一系统 。   

2. 理论框架与技术流派分类
基于 2022–2025 年的文献演进，OVD 技术体系已从单一的特征映射发展为多元化的架构生态。

2.1 视觉-语义空间对齐（Visual-Semantic Space Mapping）
这是 OVD 的早期主流范式。其核心思想是将检测器的视觉特征空间投影到 CLIP 等 VLM 的文本嵌入空间中。

机制：在训练阶段，利用基类的标注数据学习区域特征提取器；在推理阶段，利用 CLIP 的文本编码器将任意类别的文本描述转换为分类器权重（Classifier Weights），与提取的视觉特征计算相似度。

局限：CLIP 的预训练基于整图，直接将其用于局部区域会导致对齐错位（Misalignment）和背景噪声干扰。

2.2 区域-文本预训练（Region-Text Pre-training）
为了解决图像级对齐的不足，研究者开始利用带有定位信息的图像-文本数据（如 Visual Genome, Objects365）或通过伪标签技术构建区域-文本对，进行端到端的对比学习。

代表工作：GLIP, Grounding DINO, YOLO-World。

核心范式：将目标检测重构为“短语接地”（Phrase Grounding）任务，即给定图像和一段描述，预测描述中提及物体的包围框。这种范式天然支持开放词汇检测，因为它学习的是“物体-名词”的匹配关系，而非固定类别的分类边界 。   

2.3 伪标签与自训练（Pseudo-Labeling & Self-Training）
利用预训练的 VLM（如 CLIP）或基础检测器在无标注或弱标注数据上生成伪包围框和伪类别标签，然后用这些数据重新训练学生模型。

优势：能够利用海量的图像级标注数据（Image-level tags）或纯图像数据扩展词汇量。

挑战：伪标签的噪声控制是关键，2024 年的研究重点在于利用语言层级结构（Language Hierarchy）来过滤噪声 。   

2.4 知识蒸馏与迁移（Knowledge Distillation）
直接将 VLM（教师模型）的特征提取能力或对齐能力蒸馏给检测器（学生模型）。

机制：强制检测器的区域特征（Region Embeddings）逼近 VLM 提取的对应区域特征（通常通过 RoI Align 后输入 VLM 获得）。2025 年的 CCKT-Det 进一步提出了循环对比知识迁移，无需额外数据即可实现对齐 。   

2.5 生成式检测（Generative Detection）
随着大语言模型（LLM）的发展，最新的趋势是将检测视为序列生成任务，直接输出物体名称的文本序列，而非在预定义的词汇表中分类。

代表工作：GenerateU, LED。

意义：彻底摆脱了“预定义词汇表”的束缚，实现了真正的 Open-Ended 检测 。   

3. 奠基与架构重塑：2022–2023 年代表性工作解析
本节深度解析奠定当前 OVD 格局的三大基石模型：GLIP、OWL-ViT 和 Grounding DINO。

3.1 GLIP：深度融合与检测即接地
GLIP (Grounded Language-Image Pre-training)  的提出标志着 OVD 领域的分水岭。它并未沿用传统的“先检测后分类”逻辑，而是将检测任务统一为短语接地（Phrase Grounding）。   

3.1.1 深度跨模态融合（Deep Cross-Modal Fusion）
传统的 OVD 方法通常采用“晚期融合”（Late Fusion），即分别提取视觉和语言特征，仅在最后的分类头进行点积。GLIP 指出这种方式不足以捕捉复杂的跨模态交互。GLIP 在视觉编码器和文本编码器的每一层之间都引入了深度融合机制：

架构：模型由视觉编码器（Image Encoder）和文本编码器（Text Encoder）组成。在后续的特征层中，GLIP 引入了跨模态注意力模块（Cross-Modality Multi-Head Attention），使得视觉特征在早期就具备语言感知能力，反之亦然。

公式化描述：设视觉特征为 V，文本特征为 L。在每一层 i，输出特征 V 
i+1
​
 ,L 
i+1
​
  不仅依赖于本模态的前一层输入，还通过 Attention 机制聚合了跨模态的信息。

3.1.2 数据统一与语义丰富性
GLIP 的另一大贡献是统一了目标检测数据（如 COCO, Objects365）和接地数据（如 GoldG）。通过将检测数据的类别标签转化为自然语言句子（例如将“cat”标签转化为“There is a cat”），GLIP 极大地扩充了语义空间。

结果：GLIP 在 COCO 和 LVIS 上的零样本（Zero-Shot）表现超越了当时许多全监督模型。在未见过的 COCO 图像上，GLIP 达到了 49.8 AP，这在当时是前所未有的 。   

3.2 OWL-ViT：视觉 Transformer 的开放世界适配
OWL-ViT (Vision Transformer for Open-World Localization)  展示了极简主义架构的威力，证明了标准 Vision Transformer (ViT) 只要经过正确的预训练，就是天然的开放世界检测器。   

极简设计：OWL-ViT 直接使用在大规模图像-文本对（如 CLIP 数据）上预训练的 ViT 作为骨干网络。

微调策略：移除了 CLIP 最后的 Token Pooling 层，直接在 ViT 输出的空间 Token Map 上附加轻量级的检测头（Box Head）和分类头。

双重查询模式：

文本查询：使用文本嵌入与图像特征图进行匹配，实现 OVD。

图像查询（One-Shot）：使用参考图像的特征作为查询，在目标图像中寻找相似物体。

长尾鲁棒性：得益于 ViT 强大的全局上下文建模能力，OWL-ViT 在 LVIS 的稀有类别（Rare Classes）上表现出色，达到了 31.2 APr，证明了其在大规模长尾分布下的鲁棒性 。   

3.3 Grounding DINO：DETR 架构的语言赋能
Grounding DINO  是 IDEA 研究院推出的重磅工作，它结合了 DINO（DETR with Improved DeNoising Anchor Boxes）的强检测能力和 GLIP 的接地预训练思路，成为了 2023-2024 年最流行的开源 OVD 基座。   

3.3.1 架构创新：语言引导的查询选择
传统的 DETR 使用静态的学习到的查询（Learned Queries）或仅基于位置的查询。Grounding DINO 引入了“语言引导的查询选择”（Language-Guided Query Selection）模块：

机制：在编码器输出阶段，模型利用输入的文本提示（Text Prompt）来筛选出与文本最相关的图像特征，并利用这些特征初始化解码器的 Query。

特征增强器：在图像骨干和文本骨干之后，引入了一个特征增强层，通过双向 Cross-Attention 进一步对齐多尺度视觉特征和文本特征。

性能飞跃：Grounding DINO 在 COCO 零样本测试中达到了 52.5 AP，刷新了当时的记录 。其 1.5 和 1.6 版本后续进一步将性能推向了极致。   

4. 效率革命：实时开放词汇检测（2024）
在 2024 年之前，高性能 OVD 模型（如 GLIP, Grounding DINO）通常依赖于沉重的 Transformer 架构，推理延迟高，难以在自动驾驶或移动设备等端侧场景部署。YOLO-World 的出现彻底改变了这一局面。

4.1 YOLO-World：实时性的突破
腾讯 AI Lab 提出的 YOLO-World  旨在解决 OVD 的效率瓶颈，实现了在保持高精度的同时达到实时推理速度。   

4.1.1 核心组件：RepVL-PAN
YOLO-World 的核心创新在于 RepVL-PAN（Re-parameterizable Vision-Language Path Aggregation Network）。

训练态：RepVL-PAN 在传统的 PANet 结构中引入了视觉-语言交叉注意力模块，使得多尺度的特征图能够充分吸收文本语义信息。

推理态与重参数化：这是实现实时的关键。如果用户的检测词汇表是固定的（例如，只需检测“猫”和“狗”），YOLO-World 支持将文本编码器的输出（文本嵌入）重参数化（Re-parameterize） 到卷积层的权重中。

原理：由于文本嵌入对于固定词汇表是常数，其与视觉特征的交互可以预先计算并融合进 1x1 卷积核中。这意味着在推理时，模型退化为纯视觉的 YOLOv8 架构，完全消除了繁重的文本编码和 Cross-Attention 计算开销。

4.1.2 区域-文本对比损失（Region-Text Contrastive Loss）
为了在 YOLO 的检测头（Head）实现开放词汇能力，YOLO-World 引入了区域-文本对比损失。该损失函数基于 InfoNCE，拉近匹配的（Region, Text）对的特征距离，推远不匹配的对。这使得 YOLO 的 Head 输出的 Object Embeddings 直接具备了语义判别力。

4.1.3 实验结果与影响
速度与精度：在 NVIDIA V100 上，YOLO-World-L 达到了 52.0 FPS 的推理速度，同时在 LVIS 零样本测试中获得 35.4 AP。相比之下，同等精度的 Transformer 模型往往不足 5 FPS 。   

Prompt-then-Detect：这种范式允许用户在毫秒级时间内动态切换检测词汇表，极大地提升了工业部署的灵活性。

5. 弱监督与自训练机制的深化（2024–2025）
为了进一步降低对大规模图像-文本对标注数据的依赖，2024-2025 年的研究深入挖掘了弱监督学习（Weakly Supervised Learning）和自训练（Self-Training）的潜力。

5.1 DetLH：语言层级驱动的自训练
发表于 NeurIPS 2024 的 DetLH (Open-Vocabulary Object Detection via Language Hierarchy)  解决了一个被长期忽视的问题：标签的扁平化处理丢失了语义层级信息。   

5.1.1 语言层级自训练（LHST）
现有的伪标签方法往往存在噪声，即模型可能将“狗”误检为“狼”。DetLH 利用 WordNet 的语言层级结构来约束自训练过程。

层级扩展：如果图像级标签是“Dog”，LHST 不仅将其视为单一标签，还激活其父类（“Animal”, “Mammal”）和潜在子类。

协同正则化（Co-Regularization）：通过层级关系，模型可以容忍一定程度的细粒度预测错误（如将哈士奇预测为狗），但在粗粒度上必须正确。这种机制有效地抑制了伪标签中的高置信度错误，使得利用 ImageNet-21K 等纯图像数据集进行检测器训练成为可能。

5.1.2 语言层级提示生成（LHPG）
在推理阶段，训练词汇与测试词汇往往存在分布差异。LHPG 利用 CLIP 文本编码器计算测试概念与 WordNet 同义词集（Synsets）的嵌入距离，自动生成最符合模型认知的文本提示（Prompt），桥接了训练与测试的词汇鸿沟。

结果：DetLH 在 14 个检测基准上展现了优越的一致性泛化能力，特别是在跨数据集评估中优势明显 。   

5.2 CCKT-Det：无额外数据的循环知识迁移
发表于 ICLR 2025 的 CCKT-Det (Cyclic Contrastive Knowledge Transfer)  提出了一种极其高效的知识迁移框架，完全摒弃了对额外图像-文本对（Image-Text Pairs）或伪标签数据集的依赖。   

动机：以往的蒸馏方法（如 ViLD）通常需要预计算大规模的特征缓存，或者依赖含有噪声的伪标签。

循环动态机制：

语义先验注入：利用教师 VLM 预先查询图像中存在的物体类别，将这些语义先验作为 Prompt 注入到学生检测器的解码器中。这一步相当于“告诉”学生图像里大概有什么，减少盲目搜索。

区域对比蒸馏：引入区域级别的对比损失，利用匈牙利匹配（Hungarian Matching）在教师和学生特征之间建立对应关系，强制学生模型的查询（Queries）在视觉-语义空间上逼近教师。

成效：在仅使用 COCO 基础数据训练的情况下，CCKT-Det 在 OV-COCO 基准上将新类别的 AP50 提升了 2.9%，配合更强的教师模型提升幅度高达 10.2% 。这证明了深度挖掘 VLM 内部的一致性比单纯堆砌数据更有效。   

6. 知识增强与检索辅助检测（2024）
为了让模型理解更晦涩或定义模糊的开放词汇，研究者引入了检索增强生成（RAG）和知识图谱（KG）的思想。

6.1 RALF：检索增强的损失与特征
RALF (Retrieval-Augmented Losses and Visual Features)  (CVPR 2024) 指出，单纯依赖类别名称（如“iPod”）作为输入，信息量过于稀疏且容易产生歧义。   

检索增强损失（RAL）：传统的对比损失只关注正样本。RAL 通过检索语义相似但非目标的“负样本”词汇（Negative Classes）来增强对比损失的判别力，迫使模型学习更精细的决策边界。

检索增强特征（RAF）：利用大语言模型（LLM）将类别名称扩展为丰富的描述性概念（Verbalized Concepts）。例如，将“袜子”扩展为“穿在脚上的东西”、“通常是棉质的”。这些描述性文本特征被融合到视觉特征中，辅助模型理解物体的视觉属性。

性能：在 COCO 新类上提升了 3.4 AP，在 LVIS 稀有类上提升了 3.6 Mask AP 。   

6.2 KGD：知识图谱蒸馏
KGD (Knowledge Graph Distillation)  (NeurIPS 2024) 专注于解决大词汇量检测器在不同领域间的适配问题。   

隐式 KG 提取：KGD 不依赖预定义好的知识图谱，而是直接从 CLIP 的嵌入空间中提取隐式的知识图谱（节点为类别，边为类别间的语义距离）。

KG 封装与迁移：将提取出的 KG 结构蒸馏给检测器，使得检测器不仅学习到单个类别的特征，还学习到类别之间的拓扑关系（如“猫”和“老虎”在特征空间应较近，“猫”和“汽车”应较远）。这种结构化知识显著提升了模型的跨域泛化能力。

7. 生成式范式与 LLM 深度集成（2024–2025）
2024-2025 年，随着生成式 AI 的爆发，OVD 领域开始探索从“判别式分类”向“生成式描述”的根本性转变。

7.1 GenerateU：从分类到自由文本生成
GenerateU (Generative Region-Language Pretraining)  (CVPR 2024) 提出了一种激进的“去分类化”思路。   

核心思想：传统的 OVD 仍然是分类任务，需要给定一个包含 N 个候选词的词汇表。GenerateU 将检测视为生成任务——给定图像区域，解码器直接生成该物体的名称文本（Free-form text generation）。

优势：推理时不需要预定义词汇表，实现了真正的“Open-Ended”。这对于用户在推理时不知道具体有哪些类别的场景至关重要。

评估挑战：由于生成的是自由文本，传统的基于 IoU 和类别匹配的 mAP 指标不再适用。GenerateU 引入了基于语义相似度的软性评估指标。

表现：虽然无法预知类别，但在 LVIS 零样本测试中，GenerateU 取得了与 GLIP 相当的性能，证明了生成式检测的可行性。

7.2 LED：利用 LLM 隐层状态的无数据增强
LED (LLM Enhanced OVD)  (2025) 探索了如何利用多模态大模型（MLLM，如 Qwen-VL）的内部知识来增强检测器。   

关键发现：研究者分析 MLLM 的解码层发现，其**早期层的隐藏状态（Hidden States）**保留了极强的空间-语义相关性，主要关注视觉 Token；而深层状态则逐渐转向纯文本生成，丢失了空间信息。

方法：设计了一个零初始化交叉注意力适配器（Zero-initialized Cross-Attention Adapter），将 MLLM 早期层的隐藏状态无缝注入到检测器（如 Grounding DINO）的视觉编码器中。

零人工数据：该方法不需要像以往那样通过 LLM 生成合成数据（Synthetic Data）来训练检测器，避免了合成数据带来的偏差（Bias）和过拟合。

结果：在 OmniLabel 等复杂文本查询基准上，LED 将 Grounding DINO 的性能提升了 6.22%，且计算开销仅增加 8.7% 。   

8. 统一框架与 SOTA 基准分析（2025）
8.1 OW-OVD：开放世界与开放词汇的统一
OW-OVD  (CVPR 2025) 解决了 OVD 模型的一个痛点：它们虽然能识别万物，但必须先“被问到”（即输入 Prompt）。如果用户不知道图像里有什么，OVD 就无法工作。   

融合机制：结合 OVD 的零样本分类能力和 Open World Detection (OWOD) 的“未知物体发现”能力。

视觉相似性属性选择（VSAS）：通过分析标注区域和未标注区域的视觉相似性，自动挖掘具有泛化性的属性，从而主动发现潜在感兴趣的物体。

混合属性-不确定性融合（HAUF）：结合属性相似度和不确定性来判断物体是否属于“未知”类别，并决定是否将其加入检测列表。

指标突破：在未知物体召回率（U-Recall）上实现了 +15.3% 的惊人提升，显著增强了系统的主动感知能力 。   

8.2 DINO-X：当前的性能天花板
DINO-X (Grounding DINO 1.6 Pro)  代表了当前（截至 2025 年初）OVD 性能的最高水平。   

数据规模：依托于 Grounding-30M 这一超大规模、高质量的接地数据集进行预训练。

多任务统一：DINO-X 不仅做检测，还集成了分割（Segmentation）、姿态估计（Pose Estimation）和描述生成（Captioning）头，成为通用的物体感知大模型。

性能霸榜：在最具挑战性的 LVIS-minival 零样本测试中，DINO-X 达到了 59.8 AP，在稀有类别（Rare Classes）上更是达到了 63.3 AP 。这一成绩意味着 OVD 模型在长尾类别上的识别能力已经实质性地超越了许多全监督模型，彻底改变了“数据量决定精度”的传统认知。   

9. 定量性能基准与对比
表 1 展示了 2022-2025 年间代表性 OVD 模型在核心基准 LVIS 上的性能演进。LVIS 因其包含 1200+ 类别且呈长尾分布，是检验 OVD 能力的最佳试金石。

表 1: LVIS MiniVal / Val 零样本（Zero-Shot）性能对比
模型名称 (Model)	发表年份	骨干网络	核心机制	LVIS AP (MiniVal)	LVIS AP (Rare)	备注
GLIP-L 

2022	Swin-L	Deep Fusion	26.9 (Val)	-	奠基之作，定义基准
OWL-ViT 

2022	ViT-L/14	Standard ViT	-	31.2	长尾表现优异
Detic 

2022	Swin-B	Image Classification Data	-	41.7 (Std)	利用 ImageNet 弱监督
YOLO-World-L 

2024	YOLOv8-L	RepVL-PAN	35.4	-	实时推理 (52 FPS)
RALF 

2024	-	Retrieval Augmented	-	+3.6 (Gain)	检索增强
Grounding DINO 1.5 

2024	Swin-L	Language-Guided Query	55.7	-	性能大幅跃升
Grounding DINO 1.6 

2024	Swin-L	Grounding-30M Data	57.7	-	数据规模效应
CCKT-Det 

2025	ResNet50	Cyclic Transfer	-	32.8 (w/ Strong Teacher)	无额外数据 SOTA
DINO-X Pro 

2025	Proprietary	Multi-Task Head	59.8	63.3	当前 SOTA
  
数据洞察：

性能翻倍：从 GLIP 的 26.9 AP 到 DINO-X 的 59.8 AP，短短三年间 OVD 精度翻了一倍以上。

长尾逆袭：DINO-X 在稀有类别（Rare）上的 AP (63.3) 甚至超过了总体 AP (59.8)，这彻底颠覆了传统检测器“样本越少效果越差”的定律，证明了 VLM 知识迁移的巨大威力。

速度分层：市场上明显分化为两类模型：追求极致精度的 Transformer 类（DINO 系列）和追求极致速度的 CNN 类（YOLO-World）。

10. 领域扩展：3D、视频与未来展望
10.1 3D 开放词汇检测
随着自动驾驶和具身智能的兴起，将 OVD 扩展到 3D 点云（Point Cloud）成为 2024-2025 年的热点。

挑战：3D 数据缺乏像 2D 图像那样丰富的语义文本配对数据。

解决方案：OpenSight  和 Find n' Propagate  等方法主要利用 2D 图像作为桥梁，将 CLIP 的 2D 语义投影到 3D 空间，或者利用 LiDAR 的几何特性进行自训练。其中，Find n' Propagate 利用贪婪框搜索策略，在 Recall 上取得了 53% 的提升 。   

10.2 视频与跟踪
OVT-B  (NeurIPS 2024) 发布了包含 1000+ 类别的开放词汇多目标跟踪（OV-MOT）基准，填补了数据空白。   

OVTR  (ICLR 2025) 提出了首个端到端 OV-MOT 框架，证明了利用 CLIP 图像编码器指导时序一致性学习是可行的。   

10.3 结论与展望
综上所述，2022-2025 年是开放词汇目标检测技术从“概念验证”走向“成熟应用”的关键时期。

架构成熟：以 Grounding DINO 为代表的 Transformer 架构和以 YOLO-World 为代表的实时架构构成了完整的技术图谱。

生成式融合：GenerateU 和 LED 等工作预示着未来检测器将更多地融合 LLM 的生成能力，而非仅仅是分类能力。

具身智能的眼睛：未来的 OVD 模型将不再是孤立的感知模块，而是作为具身智能体（Embodied Agents）的核心视觉前端，能够理解复杂的自然语言指令（如“帮我找一下沙发下面那个红色的玩具”），在 3D 物理世界中进行主动探索与交互。

OVD 技术的进步，标志着计算机视觉正加速迈向通用人工智能（AGI）的宏伟目标。


arxiv.org
[2306.15880] Towards Open Vocabulary Learning: A Survey - arXiv
在新窗口中打开

arxiv.org
A Survey on Open-Vocabulary Detection and Segmentation: Past, Present, and Future
在新窗口中打开

arxiv.org
[2307.09220] A Survey on Open-Vocabulary Detection and Segmentation: Past, Present, and Future - arXiv
在新窗口中打开

ieeexplore.ieee.org
A Hierarchical Semantic Distillation Framework for Open-Vocabulary Object Detection - IEEE Xplore
在新窗口中打开

openaccess.thecvf.com
OW-OVD: Unified Open World and Open ... - CVF Open Access
在新窗口中打开

openaccess.thecvf.com
Grounded Language-Image Pre-training - CVF Open Access
在新窗口中打开

ikomia.ai
Grounding DINO: Revolutionizing AI with Zero-Shot Detection - Ikomia
在新窗口中打开

arxiv.org
Open-Vocabulary Object Detection via Language Hierarchy - arXiv
在新窗口中打开

arxiv.org
arXiv:2503.11005v1 [cs.CV] 14 Mar 2025
在新窗口中打开

arxiv.org
[2403.10191] Generative Region-Language Pretraining for Open-Ended Object Detection - arXiv
在新窗口中打开

arxiv.org
arXiv:2112.03857v2 [cs.CV] 17 Jun 2022
在新窗口中打开

microsoft.com
Object Detection in the Wild via Grounded Language Image Pre-training - Microsoft
在新窗口中打开

ritvik19.medium.com
Papers Explained 237: OWL ViT - Ritvik Rastogi - Medium
在新窗口中打开

huggingface.co
OWL-ViT - Hugging Face
在新窗口中打开

arxiv.org
[2205.06230] Simple Open-Vocabulary Object Detection with Vision Transformers - arXiv
在新窗口中打开

arxiv.org
Grounding DINO 1.5: Advance the “Edge” of Open-Set Object Detection - arXiv
在新窗口中打开

github.com
IDEA-Research/GroundingDINO: [ECCV 2024] Official implementation of the paper "Grounding DINO: Marrying DINO with Grounded Pre-Training for Open-Set Object Detection" - GitHub
在新窗口中打开

cvpr.thecvf.com
CVPR Poster YOLO-World: Real-Time Open-Vocabulary Object Detection
在新窗口中打开

cvpr.thecvf.com
Real-Time Open-Vocabulary Object Detection - CVPR
在新窗口中打开

blog.roboflow.com
Best Object Detection Models 2025: RF-DETR, YOLOv12 & Beyond - Roboflow Blog
在新窗口中打开

docs.ultralytics.com
YOLO-World Model - Ultralytics Docs
在新窗口中打开

openaccess.thecvf.com
YOLO-World: Real-Time Open-Vocabulary Object Detection
在新窗口中打开

papers.nips.cc
Open-Vocabulary Object Detection via Language Hierarchy - NIPS papers
在新窗口中打开

neurips.cc
NeurIPS Poster Open-Vocabulary Object Detection via Language Hierarchy
在新窗口中打开

arxiv.org
Cyclic Contrastive Knowledge Transfer for Open-Vocabulary Object Detection - arXiv
在新窗口中打开

pure.korea.ac.kr
Retrieval-Augmented Open-Vocabulary Object Detection - Korea University Pure
在新窗口中打开

pure.kaist.ac.kr
Retrieval-Augmented Open-Vocabulary Object Detection
在新窗口中打开

arxiv.org
[2404.05687] Retrieval-Augmented Open-Vocabulary Object Detection - arXiv
在新窗口中打开

neurips.cc
NeurIPS Poster Domain Adaptation for Large-Vocabulary Object ...
在新窗口中打开

proceedings.neurips.cc
Domain Adaptation for Large-Vocabulary Object Detectors - NIPS papers
在新窗口中打开

cvpr.thecvf.com
CVPR Poster Generative Region-Language Pretraining for Open-Ended Object Detection
在新窗口中打开

arxiv.org
LED: LLM Enhanced Open-Vocabulary Object Detection without Human Curated Data Generation - arXiv
在新窗口中打开

arxiv.org
LED: LLM Enhanced Open-Vocabulary Object Detection without Human Curated Data Generation - arXiv
在新窗口中打开

researchgate.net
LED: LLM Enhanced Open-Vocabulary Object Detection without Human Curated Data Generation - ResearchGate
在新窗口中打开

github.com
DINO-X: A Unified Vision Model for Open-World Object Detection and Understanding - GitHub
在新窗口中打开

arxiv.org
DINO-X: A Unified Vision Model for Open-World Object Detection and Understanding - arXiv
在新窗口中打开

researchgate.net
Open-Vocabulary Object Detection via Language Hierarchy | Request PDF - ResearchGate
在新窗口中打开

deepdataspace.com
Grounding DINO 1.6 - DeepDataSpace
在新窗口中打开

ecva.net
OpenSight: A Simple Open-Vocabulary Framework for LiDAR-Based Object Detection - European Computer Vision Association
在新窗口中打开

ecva.net
Find n' Propagate: Open-Vocabulary 3D Object Detection in Urban Environments - European Computer Vision Association
在新窗口中打开

proceedings.neurips.cc
OVT-B: A New Large-Scale Benchmark for Open-Vocabulary Multi-Object Tracking
在新窗口中打开

proceedings.iclr.cc
OVTR: END-TO-END OPEN-VOCABULARY MULTIPLE OBJECT TRACKING WITH TRANSFOR