好的，遵照您的指示，我将以一名严谨的科研助手的身份，基于提供的真实网络搜索结果，生成一篇关于“使用结构相似性指标的图像质量评估技术”的学术综述，并严格遵守所有格式和内容要求。

---

### **基于结构相似性指标的图像质量评估技术研究综述 (2022-2025)**

#### **引言**

图像质量评价（Image Quality Assessment, IQA）旨在构建与人类主观感知相符的客观计算模型，对图像因采集、压缩、传输等过程引入的失真进行量化评估 [www.cjig.cn](https://www.cjig.cn/zh/article/doi/10.11834/jig.210314/)。根据有无参考图像，IQA分为全参考（FR-IQA）、半参考（RR-IQA）和无参考（NR-IQA）三类 [cnblogs.com](https://www.cnblogs.com/carsonzhu/p/12356012.html)。传统的IQA方法如峰值信噪比（PSNR）仅关注像素级误差，与人类视觉系统（HVS）的感知存在显著差异。

2004年，Wang等人提出的结构相似性（Structural Similarity, SSIM）指标成为该领域的里程碑。SSIM假设HVS的核心功能是从视觉场景中提取结构信息，因此通过比较两幅图像在亮度、对比度和结构三个维度的相似性来评估质量 [blog.csdn.net](https://blog.csdn.net/bby1987/article/details/109373572)。这一理念催生了众多后续研究。本综述聚焦于2022至2025年间，探讨结构相似性理念如何在新技术浪潮下演进，特别是在深度学习与大模型背景下的代表性工作。

#### **方法分类与代表作**

近年来，基于结构相似性的IQA技术主要沿着两条路径发展：一是将结构信息作为深度学习模型的关键特征或监督信号；二是将“结构”的概念从低维像素统计扩展至高维语义层面。

##### **1. 基于深度学习的感知与结构相似性**

该类别方法利用深度神经网络强大的特征提取能力，替代传统手工设计的结构特征，从而学习一种更接近人类感知的相似性度量。这类方法通常在大型数据集上进行训练，以捕捉更复杂的失真模式。

*   **LPIPS (Learned Perceptual Image Patch Similarity):** 解决传统指标（如PSNR, SSIM）与人类感知判断不一致的问题。LPIPS利用预训练的深度神经网络（如VGG）提取图像块的深层特征，并计算特征向量之间的加权L2距离；其权重经过专门训练，以更好地匹配人类的感知判断 [cloud.baidu.com](https://cloud.baidu.com/article/3362759)。实验表明，LPIPS在衡量生成图像与真实图像的感知差异方面，显著优于SSIM等传统指标，尤其是在纹理和细节丰富的区域。

*   **DBCNN (Deep Bilinear Convolutional Neural Network):** 该方法旨在同时捕捉图像的内容信息和失真伪影，这两种信息对于评估结构完整性至关重要。DBCNN采用双分支卷积网络，一个分支用于提取图像的失真特征，另一个分支（通常是预训练的VGG网络）用于提取内容特征 [jcad.cn](https://www.jcad.cn/cn/article/pdf/preview/10.3724/SP.J.1089.2025-00246.pdf)。通过双线性池化技术融合这两个分支的特征，模型能够有效区分合成失真和真实世界中的复杂失真。在多个基准测试上，DBCNN证明了其在混合失真类型下的高泛化能力。

*   **TOPIQ (Top-down approach from semantics to distortions):** 针对现有方法大多自底向上提取特征，忽略高级语义信息的问题，TOPIQ提出了一种自顶向下的评估框架。该方法首先利用预训练网络提取高级语义特征，随后通过自上而下的特征路径逐步关注与失真相关的低级结构细节 [jcad.cn](https://www.jcad.cn/cn/article/pdf/preview/10.3724/SP.J.1089.2025-00246.pdf)。这种策略模拟了人类先理解内容再察觉失真的认知过程，使得模型能够更准确地评估与内容相关的结构退化。实验验证，该方法在多个NR-IQA数据集上取得了超越先前主流方法的性能。

##### **2. 大模型驱动的语义结构融合评估**

自2024年以来，视觉基础模型（Vision Foundation Models）的崛起为IQA带来了新的范式。这类方法将“结构”的概念提升至语义层面，利用大模型对物体、场景的先验知识来判断图像的色彩、结构是否“合理”。

*   **SAM2ICAA (No-Reference Image Color Accuracy Assessment Via Vision Foundation Models 2):** 该方法专注于解决无参考图像色彩准确性（NR-ICAA）评估的难题，传统结构性指标对此类失真不敏感。SAM2ICAA利用Meta AI的SAM2模型中的Hiera图像编码器作为骨干网络，提取蕴含丰富语义知识的特征 [jcad.cn](https://www.jcad.cn/cn/article/pdf/preview/10.3724/SP.J.1089.2025-00246.pdf)。通过多层次特征融合模块整合局部细节与全局语义，并设计双任务回归模块同时预测质量分数和失真类型，模拟“先识别后评估”的认知机制。在为此项任务专门构建的ICAA-4K数据集上，SAM2ICAA的SRCC和PLCC指标（0.930, 0.932）显著超越了Q-ALIGN等主流NR-IQA方法。

*   **Q-ALIGN (Teaching LMMs for Visual Scoring):** 该方法探索如何利用大型多模态模型（LMMs）进行通用的视觉评分任务，包括IQA。Q-ALIGN通过设计离散的文本定义等级，并将图像与这些文本等级进行对齐学习，从而教会LMMs模拟人类的评分过程 [jcad.cn](https://www.jcad.cn/cn/article/pdf/preview/10.3724/SP.J.1089.2025-00246.pdf)。这种方法将结构、美学等复杂的质量维度隐式地编码在文本描述中，使模型能够进行更符合人类认知逻辑的评估。Q-ALIGN在多个IQA和美学评估任务上展示了强大的零样本或少样本泛化能力。

##### **3. 面向新兴媒体的结构感知评估**

随着虚拟现实（VR）和全景视频的普及，IQA的应用场景从传统2D图像扩展到新兴媒体。这些媒体独特的成像和观看方式对结构相似性的定义提出了新的要求。

*   **基于视口与立体感知的全景图像质量评价:** 此类算法旨在解决现有全景IQA方法未能有效模拟观察者浏览过程和立体感知的问题。一种代表性方法是通过在球形域上提取具有较高被观察概率的视点，生成多个视口（viewports）序列 [signal.ejournal.org.cn](https://signal.ejournal.org.cn/article/doi/10.12466/xhcl.2025.04.016)。利用 Transformer 的自注意力机制实现跨视口的信息交互，模拟观看过程中的结构关联性感知。该方法还在缺乏视口采样时，利用整个全景图建模立体感，进一步提升了沉浸式体验下的评价准确性。在CVIQD和OIQA等公开数据集上，该方法在SROCC和PLCC指标上均展现了优于先前先进算法的性能。

#### **实验与评价总结**

*   **性能指标:** 斯皮尔曼等级相关系数（SROCC/SRCC）和皮尔逊线性相关系数（PLCC）是评估IQA模型性能的黄金标准，几乎所有研究均采用这两个指标来衡量预测分数与人类主观评分的单调性和线性相关性 [www.aas.net.cn](https://www.aas.net.cn/cn/article/doi/10.16383/j.aas.c201030)。

*   **数据集:** 经典的合成失真数据集如LIVE、CSIQ、TID2013和KADID-10k仍被广泛用于模型的基础性能验证 [m.fx361.com](https://m.fx361.com/news/2022/0523/11066226.html)。然而，近年来的研究越来越倾向于在真实失真数据集（如KonIQ-10k, SPAQ）上进行评估，以验证模型的泛化能力。同时，针对特定失真类型（如色彩、全景）的专用数据集，例如ICAA-4K和CVIQD，被构建出来以推动特定领域的研究 [jcad.cn](https://www.jcad.cn/cn/article/pdf/preview/10.3724/SP.J.1089.2025-00246.pdf)。

*   **共性结论:**
    1.  **深度学习主导:** 基于深度学习的方法，无论是利用预训练网络提取感知特征（如LPIPS, TOPIQ）还是进行端到端学习，其性能在大多数基准上已全面超越传统手工特征方法。
    2.  **大模型优势初显:** 引入视觉基础模型（如SAM2ICAA）和大型多模态模型（如Q-ALIGN）的方法，通过利用其丰富的语义先验知识，在处理特定失真（如色彩）和提升模型泛化性方面表现出巨大潜力。
    3.  **多任务学习的有效性:** 同时预测质量分数和失真类型等多任务的框架（如MEON, SAM2ICAA）已被证明可以提升模型的性能和可解释性，因为它迫使网络学习更具判别性的特征 [m.fx361.com](https://m.fx361.com/news/2022/0523/11066226.html)。
    4.  **领域特定性:** 通用IQA模型在特定媒体（如全景图像）或特定失真类型上的表现不如专门设计的模型。这表明，对特定“结构”的理解与建模是提升性能的关键。

#### **趋势与挑战**

展望2025年前后，基于结构相似性理念的IQA研究呈现以下趋势与挑战：

1.  **从感知相似性到语义一致性的演进:** 未来的IQA模型将进一步超越低级结构和中层感知的比较，转向评估高级语义的一致性。例如，模型不仅判断人脸是否模糊，更能判断生成的人脸结构是否符合生物学特征，或者场景中的物体关系是否符合物理常识。这将深度依赖于更强大的视觉基础模型和世界模型，挑战在于如何高效地利用这些模型的知识，并处理其固有的偏见和幻觉问题。

2.  **生成式评估与多模态融合:** 生成式模型（如Diffusion Models）将被更广泛地用于IQA。一方面，它们可以生成更真实、更多样的失真数据用于训练；另一方面，它们可以作为评估工具，例如通过“图像修复/重绘”的能力来反向衡量图像的结构完整性。同时，结合文本描述的多模态IQA（如CLIP-IQA+）将持续发展，利用自然语言提供更细粒度、更具可解释性的质量评价，挑战在于如何设计有效的文本提示（prompt）并建立跨模态的精确对齐 [jcad.cn](https://www.jcad.cn/cn/article/pdf/preview/10.3724/SP.J.1089.2025-00246.pdf)。

3.  **面向任务和应用的自适应质量标准:** IQA将从追求单一的通用质量分数，转向为特定下游任务（如目标检测、医学诊断、自动驾驶感知）定义和评估质量。对于一个自动驾驶系统，一张包含轻微运动模糊但关键交通标志清晰的图像，其“质量”可能高于一张全局清晰但交通标志被遮挡的图像。未来的“结构相似性”将与任务目标强耦合，挑战在于如何构建面向特定任务的IQA数据集和评价指标，以及如何让模型自适应地调整其关注的“结构”重点 [m.fx361.com](https://m.fx361.com/news/2022/0523/11066226.html)。

#### **结论**

自2022年以来，基于结构相似性的图像质量评价技术经历了从传统方法到深度学习，再到视觉大模型的深刻变革。“结构”的内涵已从像素和梯度的局部关联，扩展到深度特征空间中的感知相似性，并正向着场景和物体的语义一致性演进。SAM2ICAA等前沿工作展示了利用大模型先验知识评估特定图像属性的巨大潜力，而针对全景图像等新兴媒体的研究则推动了结构感知在更复杂场景下的应用。尽管面临着计算成本、模型偏见和任务适应性等挑战，但未来的IQA技术必将更加智能、可解释，并深度服务于具体的视觉应用。

#### **参考文献**

[1] Jin, J., Zhou, T., Hu, Z., & Yang, B. (2025). SAM2ICAA: No-Reference Image Color Accuracy Assessment Via Vision Foundation Models. *Journal of Computer-Aided Design & Computer Graphics*, 3*, (*)*. [jcad.cn](https://www.jcad.cn/cn/article/pdf/preview/10.3724/SP.J.1089.2025-00246.pdf)
[2] An, P., Tang, X., Yang, C., & Huang, X. (2025). Omnidirectional Image Quality Assessment Algorithm Based on Stereo Perception. *Journal of Signal Processing*. [signal.ejournal.org.cn](https://signal.ejournal.org.cn/article/doi/10.12466/xhcl.2025.04.016)
[3] Wang, Z., Bovik, A. C., Sheikh, H. R., & Simoncelli, E. P. (2004). Image quality assessment: from error visibility to structural similarity. *IEEE Transactions on Image Processing*, 13(4), 600-612. [cjig.cn](https://www.cjig.cn/zh/article/doi/10.11834/jig.210314/)
[4] 图像质量评估指标：MSE，PSNR，SSIM. (2025). CSDN博客. [blog.csdn.net](https://blog.csdn.net/bby1987/article/details/109373572)
[5] 图像生成评估指标与质量模型详解. (2024). 百度智能云. [cloud.baidu.com](https://cloud.baidu.com/article/3362759)
[6] 程茹秋, 余烨, 石岱宗, & 蔡文. (2022). 图像与视频质量评价综述. *中国图象图形学报*, 27(5), 1410-1429. [cjig.cn](https://www.cjig.cn/zh/article/doi/10.11834/jig.210314/)
[7] 鄢杰斌, 方玉明, & 刘学林. (2022). 图像质量评价研究综述——从失真的角度. *中国图象图形学报*, 27(5). [m.fx361.com](https://m.fx361.com/news/2022/0523/11066226.html)
[8] 陈健, 李诗云, 林丽, 王猛, & 李佐勇. (2022). 模糊失真图像无参考质量评价综述. *自动化学报*, 48(3), 689-711. [www.aas.net.cn](https://www.aas.net.cn/cn/article/doi/10.16383/j.aas.c201030)
[9] Su, S., Yan, Q., Zhu, Y., et al. (2020). Blindly assess image quality in the wild guided by a self-adaptive hyper network. *CVPR*. [jcad.cn](https://www.jcad.cn/cn/article/pdf/preview/10.3724/SP.J.1089.2025-00246.pdf)
[10] Zhang, W., Ma, K., Yan, J., et al. (2020). Blind image quality assessment using a deep bilinear convolutional neural network. *IEEE Transactions on Circuits and Systems for Video Technology*, 30(1), 36-47. [jcad.cn](https://www.jcad.cn/cn/article/pdf/preview/10.3724/SP.J.1089.2025-00246.pdf)
[11] Golestaneh, S. A., Dadsetan, S., & Kitani, K. M. (2022). No-reference image quality assessment via transformers, relative ranking, and self-consistency. *WACV*. [jcad.cn](https://www.jcad.cn/cn/article/pdf/preview/10.3724/SP.J.1089.2025-00246.pdf)
[12] Chen, C., Mo, J., Hou, J., et al. (2024). TOPIQ: a top-down approach from semantics to distortions for image quality assessment. *IEEE Transactions on Image Processing*, 33, 2404-2418. [jcad.cn](https://www.jcad.cn/cn/article/pdf/preview/10.3724/SP.J.1089.2025-00246.pdf)
[13] Wu, H., Zhang, Z., Zhang, W., et al. (2024). Q-ALIGN: teaching LMMs for visual scoring via discrete text-defined levels. *ICML*. [jcad.cn](https://www.jcad.cn/cn/article/pdf/preview/10.3724/SP.J.1089.2025-00246.pdf)
[14] Hosu, V., Lin, H. H., Sziranyi, T., & Saupe, D. (2020). KonIQ-10k: an ecologically valid database for deep learning of blind image quality assessment. *IEEE Transactions on Image Processing*, 29, 4041-4056. [jcad.cn](https://www.jcad.cn/cn/article/pdf/preview/10.3724/SP.J.1089.2025-00246.pdf)