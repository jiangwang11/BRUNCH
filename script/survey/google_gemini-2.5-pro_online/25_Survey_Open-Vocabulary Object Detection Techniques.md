好的，遵照您的指示，我将以严谨的科研助手身份，基于提供的网络搜索结果，为您生成一篇关于“开放词汇目标检测技术”的中文学术综述。

---

### **关于开放词汇目标检测（Open-Vocabulary Object Detection）技术的学术综述 (2022–2025)**

#### **引言**

传统的目标检测模型受限于其“封闭集（closed-set）”设计，即只能识别在训练阶段预先定义的固定类别。这一根本性局限严重制约了其在真实世界复杂动态场景中的应用。为突破此限制，开放词汇目标检测（Open-Vocabulary Object Detection, OVD）应运而生。OVD旨在利用自然语言的开放性，使模型能够检测任意文本描述的物体，即使这些物体的类别从未在带边界框标注的数据中出现过。

OVD的核心挑战在于如何将从有限“基类（base classes）”中学到的视觉定位能力，有效泛化到无限的“新颖类（novel classes）”。近年来的研究主要借助大规模视觉-语言预训练模型（Vision-Language Models, VLM），如CLIP，通过对齐视觉与文本特征空间，赋予检测器零样本（Zero-Shot）识别能力。本综述将梳理2022年至2025年间OVD领域的代表性方法，总结其关键技术、实验范式，并展望未来的研究趋势与挑战。

#### **方法分类与代表作**

随着研究的深入，OVD技术已从早期的知识蒸馏范式，发展到更为复杂的统一预训练、与大语言模型（LLM）深度融合等阶段。

##### **1. 基于伪标签生成与多样化数据训练**

此类方法着重于扩充训练数据的广度与多样性，通过自动生成标签或整合异构数据集来提升模型的泛化能力。

*   **Detic (ECCV 2022)**
    该研究旨在解决传统检测器因分类头受限而无法识别海量类别的问题 [developer.aliyun.com](https://developer.aliyun.com/article/1277444)。其核心方法是使用图像级（Image-level）标签来“监督”检测器，将包含21K个类别的ImageNet等分类数据集与传统检测数据集进行联合训练。对于分类图像，Detic仅在最大尺寸的图像区域上进行分类，并与检测数据共享分类器权重。关键实验结论表明，仅使用图像级弱监督，即可显著扩展检测器的词汇量，使其能够检测数万个物体类别，证明了数据广度对OVT的决定性作用。

*   **UniDetector (CVPR 2023)**
    该工作正式提出了“通用目标检测（Universal Object Detection）”任务，旨在利用多源、异构标签空间的数据进行训练，并泛化至开放世界 [blog.csdn.net](https://blog.csdn.net/qq_40279050/article/details/131517817)。其核心方法包括：1) 采用分区结构，使共享主干网络能处理来自COCO、Objects365等不同数据集的图像，同时为各数据集保留独立的分类头以避免标签冲突；2) 解耦类别无关的区域提议生成（Proposal Generation）与类别相关的RoI分类，以防止分类任务对泛化定位能力的伤害。实验证明，该框架在LVIS等大规模词汇数据集上实现了强大的零样本泛化，其AP指标比传统的全监督基线高出4%以上。

*   **DetCLIP (NeurIPS 2022)**
    该研究关注于如何高效地整合多源数据（检测数据、定位数据、图文对）并解决类别空间不统一的问题 [cloud.tencent.com.cn](https://cloud.tencent.com.cn/developer/article/2193587)。DetCLIP提出了一种并行的视觉-概念预训练框架，取代了GLIP中将类别名拼接成句子的串行方式，显著提升了训练效率。同时，它构建了一个包含类别定义与关系的“物体知识库（Dictionary）”，用于丰富类别文本表示和采样负样本，增强模型对稀有类别的区分能力。实验表明，DetCLIP在LVIS零样本检测任务上取得了显著优于GLIP的性能，且训练与推理效率分别提升了5倍和20倍。

##### **2. 统一检测、定位与语言理解**

这类方法将目标检测重构为一种更通用的视觉-语言定位（Grounding）任务，通过在更大规模的图文对数据上进行端到端预训练，实现更强的零样本能力。

*   **Grounding DINO (2023)**
    该工作旨在将基于Transformer的闭集检测器DINO与语言定位预训练相结合，构建一个强大的开集检测器 [blog.csdn.net](https://blog.csdn.net/m0_55898550/article/details/141865236)。其核心思想是将闭集检测器概念性地划分为特征提取、查询选择和跨模态解码三个阶段，并在每个阶段紧密融合语言信息。通过在海量定位（Grounding）数据上进行预训练，Grounding DINO学会了根据任意文本输入（类别、属性、关系）来定位目标。关键实验结论是，该模型在COCO零样本迁移基准上达到了52.5 AP，无需任何COCO训练数据，展示了SOTA级别的开集检测性能 [opendeep.wiki](https://opendeep.wiki/IDEA-Research/GroundingDINO/grounded-object-detection)。

*   **OV-DETR (2022)**
    该研究致力于解决传统OVD方法依赖的区域提议网络（RPN）对新类别泛化能力差的问题 [developer.aliyun.com](https://developer.aliyun.com/article/1276461)。OV-DETR通过改造DETR框架，将其从闭集匹配问题转化为条件二元匹配问题。具体而言，它将类别名或样本图像的CLIP嵌入作为条件输入，调整Transformer解码器中的对象查询（object queries），并学习一个“匹配”与“不匹配”的二元目标。这使得模型能够直接学习查询与对象间的对应关系，而无需生成中间提议。实验表明，作为首个端到端的基于Transformer的OVD模型，OV-DETR在OV-LVIS和OV-COCO基准的新类别上均取得了显著性能提升。

##### **3. 融合大语言模型与高效框架**

2024年以来的最新趋势是将能力更强的大语言模型（LLM）融入OVD，并追求框架的实时性与通用性，使其超越单纯的OVD任务。

*   **YOLO-World (2024)**
    该研究旨在将YOLO系列检测器的高效率与开放词汇能力相结合，实现实时的OVD [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/875de057-0739-403a-9847-0042f5923b28)。其核心是提出了一种可重参数化的视觉-语言路径聚合网络（RepVL-PAN）和区域-文本对比损失，以促进视觉和语言信息的有效交互。用户可以在推理时设置一个动态词汇表，模型能够实时地检测这些指定的类别。实验结果显示，YOLO-World在保持高帧率（V100上52.0 FPS）的同时，在LVIS数据集上取得了35.4 AP的优异性能，在准确性和速度上均超越了许多SOTA方法。

*   **LLMDet (CVPR 2025, Fictional Date)**
    该研究探索了如何利用LLM的强大描述与理解能力来监督OVD模型的训练，而非仅仅使用其嵌入 [blog.csdn.net](https://blog.csdn.net/fengdu78/article/details/148546526)。LLMDet让LLM为图像生成详细的图像级长描述和区域级短语，并以此构建了包含100万样本的GroundingCap-1M数据集。检测器的训练目标包括标准的定位损失和由LLM监督的描述生成损失，从而学习到更丰富的视觉-语言表示。该工作证明，通过LLM进行深度监督，可以显著提升检测器的开放词汇能力，且改进后的检测器可以作为更强的视觉基础模型，反哺大型多模态模型（LMM）。

*   **YOLO-UniOW (2025)**
    该工作提出了一个名为“通用开放世界检测（Uni-OWD）”的新范式，旨在用一个统一高效的框架同时解决开放词汇检测（识别新类别）和开放世界检测（发现未知物体）的挑战 [cloud.tencent.com.cn](https://cloud.tencent.com.cn/developer/article/2508448)。其核心创新在于：1) 提出自适应决策学习（AdaDL），用轻量级的潜在空间对齐取代计算密集的跨模态融合；2) 设计通配符学习（Wildcard Learning）策略，使模型能将词汇表外的物体检测为“未知”，并支持动态词汇扩展，且无需增量学习。实验表明，YOLO-UniOW在多个基准上树立了新的标杆，在LVIS上达到34.6 AP，同时保持69.6 FPS的高速。

#### **实验与评价总结**

*   **基准数据集与评价指标**：OVD研究普遍采用**LVIS**数据集进行评估，因其类别数量庞大（超过1200类）且存在长尾分布，能有效衡量模型对罕见类（`APr`）的泛化能力。**COCO**数据集也常被用于基类（base）与新颖类（novel）的划分评估。此外，**ODinW (Object Detection in the Wild)** 等基准被用于测试模型在多样化、真实场景下的零样本性能。
*   **共性结论**：
    1.  **数据源是关键**：在更大规模、更多样化的图文对或定位数据（如GLIP、DetCLIP所用）上进行预训练，是提升零样本性能的最有效途径。
    2.  **架构选择影响权衡**：基于DETR的架构（如Grounding DINO、OV-DETR）通常在精度上领先，但计算成本高；而基于YOLO的架构（如YOLO-World、YOLO-UniOW）则在速度与效率上展现出巨大优势，推动了OVD的实际应用。
    3.  **对齐质量决定泛化水平**：无论是通过对比学习、知识蒸馏还是统一的定位损失，其核心都是提升视觉区域特征与文本语义特征的对齐质量。高质量的对齐是模型能够泛化到新颖类的根本。
    4.  **识别未知成为新目标**：简单的OVD已不能满足所有需求，模型不仅要能识别“新”的已知类别，还需具备处理“完全未知”物体的能力，这是向开放世界智能迈进的必然要求。

#### **趋势与挑战**

展望2025年及以后，OVD领域的研究呈现出以下几个明确的趋势，并伴随着相应的挑战：

1.  **与大语言模型（LLM）的深度融合**：未来的OVD将不仅使用LLM的嵌入或监督信号，更会利用其强大的**推理和组合泛化能力**。例如，模型需要能够理解复杂的、带有属性、关系和动作的自然语言指令（如“检测那只正在追逐球的棕色小狗”），这要求检测器与LLM进行更深层次的交互式推理 [jcjs.siat.ac.cn](https://jcjs.siat.ac.cn/cn/article/id/3faf7b9b-d78c-4bc4-804f-c88ea9f874eb)。挑战在于如何在保持效率的同时，实现视觉感知与语言推理的有效协同。

2.  **从开放词汇到通用感知（Universal Perception）的统一**：当前研究已开始统一OVD与开放世界检测（OWOD），但未来的趋势是构建一个能够处理**检测、分割、关系理解、属性识别**等多任务的通用感知系统。这意味着模型需要在一个统一的框架内，根据任意形式的语言输入，输出对场景的全方位、细粒度理解。挑战在于如何设计一个可扩展的架构来处理异构的任务输出和训练目标。

3.  **面向现实世界的高效性、鲁棒性与持续学习**：随着YOLO-World等工作的成功，将OVD部署到资源受限的平台（如机器人、边缘设备）成为可能。未来的研究将更加关注**模型量化、轻量化设计和推理加速**。同时，模型需要能够应对真实世界的光照变化、遮挡和对抗性扰动，并具备在不遗忘旧知识的前提下，从新数据中**持续学习（Continual Learning）**新类别的能力。

#### **结论**

自2022年以来，开放词汇目标检测（OVD）领域取得了飞速发展。研究范式从早期的知识迁移，演进到以Grounding DINO为代表的视觉-语言统一预训练，再到近期与大语言模型深度融合、追求实时高效的YOLO-World和YOLO-UniOW。这些工作极大地扩展了目标检测器的能力边界，使其从一个封闭集工具逐步转变为能够理解开放世界、响应自然语言的智能感知系统。未来，随着与LLM的更深度融合以及对通用感知能力的追求，OVD技术将在自动驾驶、智能交互、机器人等领域释放出更大的应用潜力。

---

#### **参考文献**

1.  Detic: Detecting Twenty-thousand Classes using Image-level Supervision
2.  Detecting Everything in the Open World: Towards Universal Object Detection
3.  DetCLIP: Dictionary-Enriched Visual-Concept Paralleled Pre-training for Open-world Detection
4.  Grounding DINO: Marrying DINO with Grounded Pre-Training for Open-Set Object Detection
5.  Open-Vocabulary DETR with Conditional Matching
6.  YOLO-World: Real-Time Open-Vocabulary Object Detection
7.  LLMDet: Learning Strong Open-Vocabulary Object Detectors under the Supervision of Large Language Models
8.  YOLO-UniOW: Efficient Universal Open-World Object Detection
9.  OVR-CNN: Open-Vocabulary Object Detection Using Captions
10. ViLD: Open-Vocabulary Object Detection via Vision and Language Knowledge Distillation
11. RegionCLIP: Region-based Language-Image Pretraining
12. GLIP: Grounded Language-Image Pre-training
13. 基于上下文信息和大语言模型的开放词汇室内三维目标检测