好的，遵照您的指示。以下是基于真实网络搜索结果生成的关于“基于结构相似性度量的图像质量评价技术”的学术综述。

***

### **基于结构相似性度量的图像质量评价技术研究综述 (2022-2025)**

**摘要：** 图像质量评价（Image Quality Assessment, IQA）是计算机视觉领域的关键任务，旨在建立与人类主观感知一致的客观评价模型。结构相似性（SSIM）作为里程碑式的全参考（Full-Reference, FR）度量，因其有效模拟了人类视觉系统（HVS）对结构信息的敏感性，对该领域产生了深远影响。本综述聚焦于2022至2025年间，系统梳理了以结构相似性为核心思想或受其启发的图像质量评价技术的最新进展。首先，本文回顾了传统SSIM的扩展与应用；其次，重点阐述了深度学习，特别是视觉大模型在无参考（No-Reference, NR）IQA任务中的代表性工作，这些方法将“结构”概念从显式计算推向了隐式高级语义学习。最后，本文总结了当前主流的实验评价范式，并对未来三至五年的研究趋势与挑战进行了展望，包括视觉大模型的应用深化、领域特定IQA的兴起以及多模态与可解释性的融合。

### **1. 引言**

图像质量评价（IQA）旨在自动评估图像的视觉质量，在图像处理、传输和存储等领域至关重要。传统的IQA方法如均方误差（MSE）和峰值信噪比（PSNR）僅在像素层面计算误差，其结果常与人类主观感知存在显著偏差 [blog.csdn.net](https://blog.csdn.net/edogawachia/article/details/78756680)。为解决此问题，Wang等人于2004年提出结构相似性指数（SSIM），该度量从亮度、对比度和结构三个维度比较参考图像与失真图像的相似度，更好地模拟了人类视觉系统优先提取场景结构信息的特性 [blog.csdn.net](https://blog.csdn.net/edogawachia/article/details/78756680)。

SSIM的提出标志着IQA研究从像素保真度向量感知保真度的重要转变。然而，随着失真类型的日益复杂以及无参考（NR-IQA）场景需求的激增，传统SSIM的局限性也逐渐显现。近年来，尤其是2022-2025年间，研究范式经历了显著演进：一方面，研究者在传统SSIM的基础上进行扩展，以适应更多应用场景；另一方面，深度学习模型，特别是视觉大模型（Vision Foundation Models, VFMs），通过从海量数据中学习丰富的结构与语义先验，正在重新定义NR-IQA的边界。本综述旨在系统梳理这一时期的代表性工作，揭示该领域从显式结构度量到隐式语义感知的技术演进脉络。

### **2. 方法分类与代表作**

#### **2.1 传统结构相似性指标的扩展与应用**

尽管深度学习成为主流，但直接基于SSIM思想的扩展和创新应用仍在特定领域展现价值。这类方法的核心在于对SSIM的组成部分进行优化，或将其应用于新的问题场景。

*   **L0-SSIM**: 该方法针对图像修复任务，提出了一种结合L0范数和SSIM的混合评价指标。研究认为，单一的SSIM无法充分惩罚修复结果中产生的伪影。L0SSIM通过引入L0范数来度量修复图像与原始图像在稀疏性上的差异，结合SSIM对结构保真度的考量，提供了一个更全面的评价维度。实验表明，L0SSIM能够同时评估修复图像的结构相似度和伪影程度，比单独使用SSIM或L0范斯更符合主观评价 [blog.csdn.net](https://blog.csdn.net/qq_45790998/article/details/129416622)。

*   **基于SSIM的动态事件监测**: 在灾害监测等实际应用中，SSIM被创造性地用于分析时序影像的变化。一项研究利用SSIM指标分析CCTV监控视频，以探测山体滑坡等地质灾害。该研究的核心方法是计算视频序列中相邻帧之间的SSIM值，通过监测SSIM值的剧烈下降（如从0.98骤降至0.78）来识别结构发生显著变化的时刻和区域。研究结论证实，SSIM整合了亮度、对比度和结构信息，对微小变化具有高度敏感性，可有效捕捉崩塌等突发事件的初始时间和空间位置，展现了其在动态场景结构变化监测中的应用潜力 [www.ncdr.nat.gov.tw](https://www.ncdr.nat.gov.tw/presentation2025/pdf/area2/1/05-%E5%9D%A1%E6%B4%AA%E7%B5%84-%E7%A0%94%E7%99%BC%E9%A1%9E-%E6%87%89%E7%94%A8SSIM%E6%8C%87%E6%A8%99%E6%8E%A2%E8%A8%8ECCTV%E5%BD%B1%E5%83%8F%E4%B9%8B%E5%B4%A9%E5%A1%8C%E8%AE%8A%E5%8C%96.pdf)。

#### **2.2 基于深度学习的无参考图像质量评价**

近年来，深度学习模型，特别是Transformer和视觉大模型，已成为NR-IQA领域的主流。这些方法不再依赖手工设计的结构特征，而是通过端到端的学习，从大规模数据中自主提取与图像质量高度相关的多层次特征。

*   **MUSIQ (Multi-scale Image Quality Transformer)**: 该工作针对现有基于CNN的方法通常需要将输入图像缩放至固定尺寸，从而导致原始质量信息损失的问题。MUSIQ采用Transformer架构，能够直接处理不同分辨率和长宽比的原生图像。其核心方法是利用多尺度图像表示，捕捉从局部细节到全局布局的不同粒度质量特征，并通过新颖的哈希二维空间嵌入和尺度嵌入来维持多尺度表示中的位置信息。在SPAQ和KonIQ-10k等大规模IQA数据集上的实验证明，MUSIQ的性能超越了当时主流的基于CNN的方法 [zhuanzhi.ai](https://zhuanzhi.ai/paper/f8f32014a424d8c112d966eb8bd0dcd3)。

*   **SAM2ICAA (SAM2-based Image Color Accuracy Assessment)**: 这项2025年的研究工作聚焦于一个特定的IQA子问题：无参考图像色彩准确性评估，并指出当前主流NR-IQA方法对此关注不足。为解决该问题，研究者首先构建了一个专门的色彩失真基准数据集ICAA-4K。其核心方法是利用视觉大模型SAM2的Hiera图像编码器作为骨干网络，通过多层次特征融合模块整合局部细节与全局语义，并设计一个双任务回归模块同时预测质量分数和失真类型。实验结果显示，在ICAA-4K数据集上，SAM2ICAA的性能在SRCC和PLCC指标上均显著超过了包括TReS、TOPIQ和Q-ALIGN在内的主流NR-IQA模型，有望成为色彩质量评估领域的新基准 [www.jcad.cn](https://www.jcad.cn/cn/article/pdf/preview/10.3724/SP.J.1089.2025-00246.pdf)。

### **3. 实验与评价总结**

该领域的研究普遍遵循一套标准的实验与评价范式。

*   **评价指标**: 客观IQA模型的性能通常通过其预测分数与人类主观平均意见分（Mean Opinion Score, MOS）之间的相关性来衡量。最常用的两个指标是**斯皮尔曼等级相关系数（SROCC）**和**皮尔逊线性相关系数（PLCC）** [www.cjig.cn](https://www.cjig.cn/zh/article/doi/10.11834/jig.210314/)。SROCC评估预测的单调性，而PLCC在经过非线性拟合后评估预测的准确性。高SROCC和PLCC值（接近1）代表模型预测结果与人类感知高度一致。

*   **数据集**: 实验通常在公开的大规模IQA数据集上进行，如早期的LIVE、CSIQ、TID2013，以及近年来更具挑战性的真实失真数据集KonIQ-10k、SPAQ等 [www.cjig.cn](https://www.cjig.cn/zh/article/doi/10.11834/jig.210314/)。值得注意的是，如SAM2ICAA的研究表明，为特定质量维度（如色彩）构建专门的基准数据集是推动领域发展的重要方向 [www.jcad.cn](https://www.jcad.cn/cn/article/pdf/preview/10.3724/SP.J.1089.2025-00246.pdf)。

*   **共性结论**:
    1.  **感知度量优于像素度量**: SSIM相比于PSNR/MSE，与人类主观评价的相关性更高，这已成为共识 [blog.csdn.net](https://blog.csdn.net/edogawachia/article/details/78756680)。
    2.  **深度学习模型性能占优**: 基于深度学习的NR-IQA方法（如MUSIQ, SAM2ICAA）在各项指标上已全面超越传统的、基于自然场景统计（NSS）的NR-IQA方法 [www.jcad.cn](https://www.jcad.cn/cn/article/pdf/preview/10.3724/SP.J.1089.2025-00246.pdf)。
    3.  **高级特征的重要性**: 基于深度学习的感知度量（如LPIPS）和生成模型评估指标（如FID）通过比较深度特征空间的距离，比SSIM更能捕捉高级语义和纹理差异，尽管其计算复杂度更高 [hackmd.io](https://hackmd.io/@HowWang/BysMuNL7A)。

### **4. 趋势与挑战**

展望2025年前后，基于结构相似性思想的IQA技术正朝着以下几个方向演进：

1.  **视觉大模型的深度融合**: SAM2ICAA的应用预示着一个明确的趋势：利用视觉大模型（如SAM、DINOv2、CLIP）作为NR-IQA的强大骨干网络 [www.jcad.cn](https://www.jcad.cn/cn/article/pdf/preview/10.3724/SP.J.1089.2025-00246.pdf)。这些模型在海量数据上进行了预训练，蕴含了关于世界物体、场景和物理规律的丰富先验知识。这种知识对于NR-IQA任务至关重要，因为它弥补了“无参考”所带来的信息缺失，使模型能够基于内部知识判断图像质量是否“合理”。

2.  **领域特定与任务驱动的质量评价**: 通用IQA指标（包括SSIM）在特定领域的适用性受到挑战。例如，研究指出SSIM和PSNR在评估MRI、CT等医学图像时可能失效，因为医学图像的统计特性与自然图像截然不同，伪影的感知重要性也完全不同 [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/adf89510-9d96-43fb-9685-eb1e97c26e14)。未来的研究将更加关注“fitness-for-purpose”，即为特定应用（如自动驾驶、医学诊断、工业检测）设计定制化的IQA指标，评估图像质量是否满足下游任务的需求，而非追求普适的“好看”。

3.  **多模态与可解释性增强**: 未来的IQA模型不仅要给出一个分数，还要解释“为什么”。CLIP-IQA等模型通过引入文本提示（如“清晰的照片” vs “模糊的照片”）进行质量评估，开启了多模态IQA的探索 [blog.csdn.net](https://blog.csdn.net/weixin_45897172/article/details/143203942)。SAM2ICAA的双任务设计（预测分数和失真类型）也是迈向可解释性的一步 [www.jcad.cn](https://www.jcad.cn/cn/article/pdf/preview/10.3724/SP.J.1089.2025-00246.pdf)。预计未来将出现更多结合语言、声音等多模态信息、能够生成可解释性报告（如定位质量缺陷区域、说明失真类型）的IQA系统。

### **5. 结论**

自SSIM提出以来，图像质量评价领域的研究思想已从手工设计的显式结构比较，演进为基于深度学习的隐式、多层次特征学习，并正迈向利用视觉大模型进行语义感知的全新阶段。在2022-2025年间，以Transformer和视觉大模型为代表的技术显著提升了NR-IQA的性能上限，并推动了研究焦点向特定质量维度和特定应用领域的转移。尽管SSIM的原始公式可能不再是最新SOTA模型的核心，但其“结构信息对感知质量至关重要”的核心思想，已内化为现代深度模型的学习目标。未来的IQA技术将更加智能、专业和可信，为各类视觉应用提供更可靠的质量保障。

### **6. 参考文献**

1.  Jin, J., Zhou, T., Hu, Z., & Yang, B. (2025). SAM2ICAA: No-Reference Image Color Accuracy Assessment Via Vision Foundation Models. *Journal of Computer-Aided Design & Computer Graphics*. [www.jcad.cn](https://www.jcad.cn/cn/article/pdf/preview/10.3724/SP.J.1089.2025-00246.pdf)
2.  Ke, J., Wang, Q., Wang, Y., Milanfar, P., & Yang, F. (2021). MUSIQ: Multi-scale image quality transformer. *Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV)*. [zhuanzhi.ai](https://zhuanzhi.ai/paper/f8f32014a424d8c112d966eb8bd0dcd3)
3.  Wei, X., et al. (2025). *Applying SSIM Index to Investigate Collapse Changes in CCTV Images*. Presentation, National Science and Technology Center for Disaster Reduction. [www.ncdr.nat.gov.tw](https://www.ncdr.nat.gov.tw/presentation2025/pdf/area2/1/05-%E5%9D%A1%E6%B4%AA%E7%B5%84-%E7%A0%94%E7%99%BC%E9%A1%9E-%E6%87%89%E7%94%A8SSIM%E6%8C%87%E6%A8%99%E6%8E%A2%E8%A8%8ECCTV%E5%BD%B1%E5%83%8F%E4%B9%8B%E5%B4%A9%E5%A1%8C%E8%AE%8A%E5%8C%96.pdf)
4.  Breger, A., Biguri, A., Landman, M. S., et al. (2024). A study of why we need to reassess full reference image quality assessment with medical images. *arXiv preprint*. [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/adf89510-9d96-43fb-9685-eb1e97c26e14)
5.  Cheng, R., Yu, Y., Shi, D., & Cai, W. (2022). The critical review of image and video quality assessment methods. *Journal of Image and Graphics*, *27*(5), 1410-1429. [www.cjig.cn](https://www.cjig.cn/zh/article/doi/10.11834/jig.210314/)
6.  Wang, Z., Bovik, A. C., Sheikh, H. R., & Simoncelli, E. P. (2004). Image quality assessment: from error visibility to structural similarity. *IEEE transactions on image processing*, *13*(4), 600-612. [blog.csdn.net](https://blog.csdn.net/edogawachia/article/details/78756680)
7.  Zhang, R., Isola, P., Efros, A. A., Shechtman, E., & Wang, O. (2018). The unreasonable effectiveness of deep features as a perceptual metric. *Proceedings of the IEEE conference on computer vision and pattern recognition (CVPR)*. [blog.csdn.net](https://blog.csdn.net/qq_45790998/article/details/129416622)
8.  Zhang, K., Zuo, W., Zhang, L., & Meng, D. (2018). L0-Sparse and SSIM-Regularized Image Restoration. *IEEE Transactions on Image Processing*, *27*(9), 4275-4286. [blog.csdn.net](https://blog.csdn.net/qq_45790998/article/details/129416622)
9.  Su, S., Yan, Q., Zhu, Y., et al. (2020). Blindly assess image quality in the wild guided by a self-adaptive hyper network. *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*.
10. Zhang, W., Ma, K., Yan, J., et al. (2020). Blind image quality assessment using a deep bilinear convolutional neural network. *IEEE Transactions on Circuits and Systems for Video Technology*, *30*(1), 36-47.
11. Golestaneh, S. A., Dadsetan, S., & Kitani, K. M. (2022). No-reference image quality assessment via transformers, relative ranking, and self-consistency. *Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision*.
12. Chen, C., Mo, J., Hou, J., et al. (2024). TOPIQ: a top-down approach from semantics to distortions for image quality assessment. *IEEE Transactions on Image Processing*, *33*, 2404-2418.
13. Wu, H., Zhang, Z., Zhang, W., et al. (2024). Q-ALIGN: teaching LMMs for visual scoring via discrete text-defined levels. *Proceedings of the 41st International Conference on Machine Learning (ICML)*.