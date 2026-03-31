好的，作为一名严谨的科研助手，我将基于提供的真实网络搜索结果，为您生成一篇关于“用于图像识别与处理的可变形卷积网络”的学术综述，内容覆盖2022至2025年的代表性工作。

***

### **用于图像识别与处理的可变形卷积网络：2022-2025年进展综述**

#### **引言**

卷积神经网络（CNN）通过其固有的归纳偏置（如局部性和平移不变性），在计算机视觉领域取得了里程碑式的成功。然而，标准卷积操作在固定、矩形的感受野上采样，这限制了其对物体复杂几何形变的建模能力。为解决此问题，可变形卷积网络（Deformable Convolutional Networks, DCN）被提出，其核心思想是为卷积核的每个采样点学习一个额外的二维偏移量，使感受野能够自适应地贴合物体的实际形状与姿态 [blog.csdn.net](https://blog.csdn.net/m0_38068229/article/details/115503814)。

在最初版本的基础上，DCNv2引入了“调制机制”，即为每个采样点额外学习一个权重标量，使得网络不仅能决定“在哪里采样”，还能控制“采样的重要程度”，从而进一步增强了其特征提取的灵活性与聚焦能力 [www.cnblogs.com](https://www.cnblogs.com/VincentLee/p/12826273.html)。进入2022年以后，研究重点从将DCN作为现有模型的改进插件，转向将其作为构建新一代视觉基础模型的核心算子。本综述旨在系统梳理2022至2025年间可变形卷积的代表性研究进展，主要围绕其在大规模模型中的应用、与注意力机制的融合、算子效率优化以及特定领域应用等方向展开，并对未来的研究趋势进行展望。

#### **方法分类与代表作**

##### **1. 大规模模型构建与算子迭代**

随着Vision Transformer（ViT）的成功，如何构建大规模CNN模型成为焦点。DCN因其动态特性，被视为CNN挑战ViT的关键。该方向的研究致力于将DCN作为核心算子，借鉴ViT的架构设计思想，构建亿级甚至更大参数量的模型，并持续优化DCN算子本身。

*   **InternImage (基于DCNv3) (CVPR 2023 / arXiv 2022)**
    *   **研究问题**: 传统CNN架构难以像ViT一样通过扩大模型和数据规模来持续提升性能，缺乏能够支撑大规模视觉基础模型的CNN核心算子。
    *   **核心方法**: 提出了DCNv3算子，通过引入权重共享、多组机制以及对调制因子进行Softmax归一化，解决了DCNv2在大模型训练中的不稳定性与效率问题。基于DCNv3，构建了名为InternImage的大规模CNN模型，其基本模块借鉴了ViT的设计（如LN、FFN），从而实现了CNN架构的成功扩展。
    *   **关键实验结论**: InternImage-H（10亿参数）在COCO test-dev目标检测任务上取得了65.4mAP的SOTA成绩，显著超越了同期的SwinV2-G等模型。这证明了基于DCN的CNN架构具备与顶级ViT模型相媲美甚至更优的性能与扩展潜力 [developer.volcengine.com](https://developer.volcengine.com/articles/7382310687088836658)。

*   **DCNv4 (CVPR 2024)**
    *   **研究问题**: DCNv3虽然性能强大，但实际部署中速度受限于内存访问（Memory Access Cost, MAC），而非计算量（FLOPs），且其空间聚合中的Softmax归一化可能限制了模型的表达能力。
    *   **核心方法**: 提出了DCNv4算子，进行了两项关键改进：1）在空间聚合中去除了Softmax归一化，增强了动态特性和收敛速度；2）通过向量化加载和优化线程管理等方法，深度优化了CUDA内核，显著减少了冗余的内存访问。基于DCNv4构建的Flash-InternImage网络，在保持甚至提升性能的同时，大幅加快了推理速度。
    *   **关键实验结论**: DCNv4算子的前向推理速度是DCNv3的3倍以上，使Flash-InternImage相比InternImage实现了50%-80%的速度提升。该算子还在Stable Diffusion等生成模型中验证了其通用性与高效性，展现了作为下一代视觉模型基础算子的潜力 [www.shlab.org.cn](https://www.shlab.org.cn/news/5443920)。

##### **2. 与注意力机制的融合探索**

DCN的动态稀疏采样与Transformer中的Attention机制在“关注关键信息”上思想共通。Deformable DETR通过将DCN的稀疏采样思想引入Attention，开创了这一融合方向 [blog.csdn.net](https://blog.csdn.net/m0_38068229/article/details/115503814)。近期的研究则进一步探索了两者之间的深层联系与等价性，甚至尝试相互替代。

*   **DSAN (TNNLS 2025)**
    *   **研究问题**: DCNv3等先进算子因计算和参数量较大，难以应用于资源受限的轻量级CNN模型中，其稀疏采样特性在小模型上效果不佳。
    *   **核心方法**: 该研究探索了可变形卷积与空间注意力之间的关系，提出了可变形空间注意力（Deformable Spatial Attention, DSA）。DSA模块使用一对简化的“可变形条形卷积”（DSCN）来替代DCNv3的复杂操作，并移除了调制掩码分支，代之以空间注意力的乘法形式，从而在模拟DCN动态采样的同时大幅降低了计算与参数量。
    *   **关键实验结论**: 基于DSA模块构建的轻量级网络DSAN，在图像分类、语义分割等任务上，以更少的参数和计算量超越了VAN、MSCAN等其他轻量级模型。例如，在ADE20K语义分割任务上，DSAN-T的mIoU比SegNeXt-T高出1.2% [cnblogs.com](https://www.cnblogs.com/wxkang/p/18886289)。

*   **RFAConv (arXiv 2023)**
    *   **研究问题**: 研究者认为，传统空间注意力（如CBAM）的有效性在于其解决了卷积核参数共享的问题，但其生成的注意力图信息量有限，不足以指导大尺寸卷积核。
    *   **核心方法**: 提出了一种名为感受野注意力（Receptive-Field Attention, RFA）的新机制。与仅关注空间位置的传统注意力不同，RFA为大尺寸卷积核的整个感受野提供有效的注意力权重，从而更充分地解决参数共享带来的信息瓶颈。
    *   **关键实验结论**: RFAConv作为标准卷积的替代品，在几乎不增加计算成本和参数的情况下，能在ImageNet-1k、COCO等多个基准上显著提升网络性能。这项工作虽然不直接改进DCN，但其从“感受野”层面重新思考注意力与卷积关系，与DCN的思想形成了有趣的呼应 [www.zhuanzhi.ai](https://www.zhuanzhi.ai/paper/4e8b273e834fd94cf11d41d92742dcd8)。

##### **3. 特定领域应用与混合模型**

除了作为通用骨干网络的核心，DCN的灵活性也使其在特定应用中表现出色，尤其是在处理具有不规则形状和纹理的缺陷检测等问题上。

*   **Attention Deformable Convolutional Networks for Wooden Panel Defect Recognition (Journal of Southwest University (Natural Science Edition), 2024)**
    *   **研究问题**: 木质板材缺陷的形状、尺寸和纹理复杂多变，传统固定感受野的CNN难以高效准确地识别。
    *   **核心方法**: 提出一个结合DCN、门控循环单元（GRU）和注意力机制的端到端混合模型。DCN用于自适应地捕获缺陷区域的几何特征，GRU层用于学习高级时序（序列）特征，最后的注意力模块则用于加强对最重要瑕疵特征的响应。
    *   **关键实验结论**: 在多个木质板材缺陷数据集上，该方法的准确率达到了99.2%，在准确率、灵敏度和特异性等指标上全面超越了多种对比方法约2.4%至21%。这表明DCN与RNN、Attention的混合架构在处理特定工业检测任务时具有很强的实用价值 [xbgjxt.swu.edu.cn](https://xbgjxt.swu.edu.cn/article/doi/10.13718/j.cnki.xdzk.2024.02.016)。

#### **实验与评价总结**

综合2022-2025年的研究成果，可变形卷积网络在各类实验评测中展现出以下共性结论：

1.  **卓越的性能与扩展性**：基于DCN（特别是DCNv3及后续版本）构建的大规模视觉模型（如InternImage）在目标检测、实例分割和语义分割等密集预测任务上，已经达到了与最先进的Vision Transformer模型同等甚至更高的精度，打破了ViT在大模型时代的性能垄断地位 [developer.volcengine.com](https://developer.volcengine.com/articles/7382310687088836658)。
2.  **效率成为关键优化方向**：尽管DCN在算法层面优势明显，但其非结构化的内存访问模式带来了实际的性能开销。DCNv4的研究明确指出，算子级别的底层优化（如CUDA kernel优化）是释放其潜力的关键，可实现数倍的速度提升，使其在性能和速度上均具备竞争力 [www.shlab.org.cn](https://www.shlab.org.cn/news/5443920)。
3.  **与注意力机制的互补与融合是趋势**：多项研究表明，DCN的动态采样与注意力机制可以相互借鉴、融合甚至替代。DSAN的成功证明了可以用轻量化的可变形卷积思想来设计高效的空间注意力模块，实现了在轻量级模型上的性能突破 [cnblogs.com](https://www.cnblogs.com/wxkang/p/18886289)。
4.  **在不规则目标和密集预测任务中优势显著**：无论是通用的COCO数据集，还是特定的木材缺陷检测任务，DCN都表现出对非刚性、形态多变目标的强大建模能力。消融实验普遍证实，DCN的可变形采样和调制机制是提升性能的核心要素 [cnblogs.com, xbgjxt.swu.edu.cn]。

#### **趋势与挑战**

基于上述进展，预计2025年前后，可变形卷积网络的研究将呈现以下关键趋势和挑战：

1.  **趋势一：算子层面的软硬件协同优化**。DCNv4的成功揭示了算法与底层实现之间优化的巨大空间。未来的研究将更加注重设计硬件友好（Hardware-Aware）的动态算子，不仅仅是理论上的FLOPs，更关注内存访问效率、缓存命中率等实际指标，甚至为特定的AI芯片（如NPU、GPU）定制优化的DCN变体。

2.  **趋势二：与注意力机制及其他动态算子的深度统一**。DCN和Attention的界限正变得模糊。未来的趋势可能是在一个统一的框架下描述这两种操作，例如将Attention看作是一种在全局范围内进行内容寻址的“超大规模”DCN。这将催生出结合两者优点、能够在局部和全局动态调整计算资源的新型混合架构。

3.  **趋势三：向更高维、更多模态数据扩展**。目前DCN主要应用于2D图像。将其高效地扩展到视频（3D时空）、3D点云、医学体积数据等更高维度的领域是一个自然且重要的方向。这需要重新设计偏移量学习机制和插值方法，以适应高维数据的复杂几何与动态变化。

**挑战**：当前DCN的一个核心挑战在于**可解释性与可控性**。尽管其性能优异，但网络如何学习偏移量和调制权重以适应特定任务和数据，其内部决策过程仍是一个“黑箱”。如何引导模型学习到更有意义、更可解释的形变模式，并根据先验知识对形变范围进行有效约束，是一个亟待解决的理论问题。

#### **结论**

在2022至2025年期间，可变形卷积网络（DCN）经历了从一个优秀CNN组件到支撑起SOTA视觉基础模型核心算角的深刻演变。以DCNv3和DCNv4为代表的研究，成功地将DCN扩展到十亿级参数规模，在各大视觉基准上取得了与ViT媲美的成绩。与此同时，与注意力机制的融合（如DSAN）、算子层面的效率优化（如DCNv4）以及在特定领域的应用，展示了DCN强大的生命力与适应性。展望未来，软硬件协同设计、与其它动态算子的统一以及向多维多模态数据的扩展将是DCN发展的关键方向。可变形卷积无疑已成为后ViT时代CNN架构创新的核心驱动力之一。

#### **参考文献**

[1] Dai, J., Qi, H., Xiong, Y., Li, Y., Zhang, G., Hu, H., & Wei, Y. (2017). Deformable convolutional networks. In *Proceedings of the IEEE international conference on computer vision*.

[2] Zhu, X., Hu, H., Lin, S., & Dai, J. (2019). Deformable ConvNets v2: More deformable, better results. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition*. [www.cnblogs.com](https://www.cnblogs.com/VincentLee/p/12826273.html)

[3] Wang, W., et al. (2022). InternImage: Exploring Large-Scale Vision Foundation Models with Deformable Convolutions. arXiv preprint arXiv:2211.05778. [developer.volcengine.com](https://developer.volcengine.com/articles/7382310687088836658)

[4] Wang, Z., et al. (2024). Efficient Deformable ConvNets: Rethinking Dynamic and Sparse Operator for Vision Applications. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*. [www.shlab.org.cn](https://www.shlab.org.cn/news/5443920)

[5] Zhu, X., Su, W., Lu, L., Li, B., Wang, X., & Dai, J. (2020). Deformable detr: Deformable transformers for end-to-end object detection. In *International Conference on Learning Representations*. [blog.csdn.net](https://blog.csdn.net/m0_38068229/article/details/115503814)

[6] Kang, W., et al. (2025). DSAN: Exploring the Relationship between Deformable Convolution and Spatial Attention. *IEEE Transactions on Neural Networks and Learning Systems (TNNLS)*. [cnblogs.com](https://www.cnblogs.com/wxkang/p/18886289)

[7] Zhang, X., Liu, C., Yang, D., Song, T., Ye, Y., Li, K., & Song, Y. (2023). RFAConv: Innovating Spatial Attention and Standard Convolutional Operation. arXiv preprint arXiv:2304.03198. [www.zhuanzhi.ai](https://www.zhuanzhi.ai/paper/4e8b273e834fd94cf11d41d92742dcd8)

[8] Zhu, Y., Li, Y., Xi, Z., & Sheng, H. (2024). Attention Deformable Convolutional Networks for Wooden Panel Defect Recognition. *Journal of Southwest University (Natural Science Edition)*, 46(2), 159-169. [xbgjxt.swu.edu.cn](https://xbgjxt.swu.edu.cn/article/doi/10.13718/j.cnki.xdzk.2024.02.016)

[9] Liu, Z., Lin, Y., Cao, Y., Hu, H., Wei, Y., Zhang, Z., ... & Guo, B. (2022). Swin Transformer V2: Scaling up capacity and resolution. In *Proceedings of the IEEE/CVF conference on computer vision and pattern recognition*.

[10] Liu, Z., Mao, H., Wu, C. Y., Feichtenhofer, C., Darrell, T., & Xie, S. (2022). A convnet for the 2020s. In *Proceedings of the IEEE/CVF conference on computer vision and pattern recognition*.

[11] Ding, X., Zhang, X., Han, J., & Ding, G. (2022). Scaling up your kernels to 31x31: Revisiting large kernel design in cnns. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition*.

[12] Bao, H., Dong, L., Wei, F., et al. (2021). BEiT: BERT Pre-Training of Image Transformers. In *International Conference on Learning Representations*.