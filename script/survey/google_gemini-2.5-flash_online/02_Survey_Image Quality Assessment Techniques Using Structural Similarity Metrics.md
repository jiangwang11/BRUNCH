## 图像质量评估中结构相似性度量技术综述

### 引言

图像质量评估 (Image Quality Assessment, IQA) 是计算机视觉和图像处理领域中的一个核心研究方向，旨在通过计算模型量化图像的感知质量。其应用广泛，涵盖图像压缩、传输、增强、复原等多个方面。传统IQA方法主要依赖于误差可见性，例如均方误差 (Mean Squared Error, MSE) 和峰值信噪比 (Peak Signal-to-Noise Ratio, PSNR) [blog.csdn.net/bby1987](https://blog.csdn.net/bby1987/article/details/109373572)。然而，这些指标通常未能充分捕捉人类视觉系统 (Human Visual System, HVS) 对图像质量的感知，特别是对结构信息的敏感性。

结构相似性 (Structural Similarity, SSIM) [blog.csdn.net/bby1987](https://blog.csdn.net/bby1987/article/details/109373572) 及其变体作为一类半参考甚至无参考的图像质量评估方法，通过模拟HVS感知图像结构、亮度和对比度的机制，显著提升了客观评价与主观感知的一致性。本综述旨在梳理2022年至2025年间，IQA领域中利用结构相似性度量技术进行图像质量评估的代表性工作，总结其方法、实验结论，并展望未来发展趋势。

### 方法分类与代表作

本节将结构相似性度量技术在IQA中的应用分为三个主要类别：SSIM基础与改进、多尺度与变换域SSIM，以及结合深度学习的结构相似性度量。

#### 1. SSIM基础与改进

SSIM通过亮度、对比度和结构三个分量来衡量两幅图像的相似性，其核心在于图像局部区域的统计特性提取 [blog.csdn.net/bby1987](https://blog.csdn.net/bby1987/article/details/109373572)。

*   **《Assessment of the Image Quality of Virtual Non-Contrast Dual-energy CT Liver Scans Using Both PSNR and SSIM Methods》 (2025)** [cttacn.org.cn](https://cttacn.org.cn/article/doi/10.15953/j.ctta.2024.151)
    *   **研究问题：** 探讨双能量CT肝脏虚拟平扫（VNC）图像替代真实平扫（TNC）图像的可行性及其图像质量评估。
    *   **核心方法：** 联合使用PSNR和SSIM方法对VNC和TNC图像进行整体及局部比对分析，并测量CT值、噪声值、信噪比（SNR）和对比噪声比（CNR）。
    *   **关键实验结论：** 整体及局部比较显示，VNC与TNC图像的PSNR和SSIM差异无统计学意义，表明VNC图像能较好还原TNC图像，满足临床诊断需求，同时可降低约29.63%的辐射剂量。

#### 2. 多尺度与变换域SSIM

多尺度结构相似性 (MS-SSIM) 通过在不同分辨率下计算SSIM分量并加权组合，进一步提升了评估的鲁棒性和对不同失真类型的敏感性 [blog.csdn.net/bby1987](https://blog.csdn.net/bby1987/article/details/109373572)。

*   **《MUSIQ: Multi-scale Image Quality Transformer》 (2021)** [zhuanzhi.ai](https://zhuanzhi.ai/paper/f8f32014a424d8c112d966eb8bd0dcd3)
    *   **研究问题：** 现有IQA方法受限于批量训练中的固定形状约束，导致图像质量退化，难以处理具有不同尺寸和宽高比的原始分辨率图像。
    *   **核心方法：** 提出多尺度图像质量Transformer (MUSIQ)，处理不定尺寸的原始分辨率图像，并通过多尺度图像表示捕捉不同粒度下的图像质量。引入基于哈希的2D空间嵌入和尺度嵌入以支持多尺度表示中的位置编码。
    *   **关键实验结论：** MUSIQ在PaQ-2-PiQ、SPAQ和KonIQ-10k等多个大型IQA数据集上实现先进性能。

#### 3. 结合深度学习的结构相似性度量

深度学习在IQA领域的兴起，为结构相似性度量提供了新的结合方式，例如将SSIM作为损失函数的一部分，或通过学习特征来隐式地捕捉结构相似性。

*   **《SAM2ICAA: 基于视觉大模型的无参考图像色彩准确性评估方法》 (2025)** [jcad.cn](https://www.jcad.cn/cn/article/pdf/preview/10.3724/SP.J.1089.2025-00246.pdf)
    *   **研究问题：** 现有无参考图像质量评估 (NR-IQA) 方法主要关注结构性失真，缺乏针对色彩保真度的有效评估模型与数据集。
    *   **核心方法：** 提出基于视觉大模型SAM2的无参考图像色彩准确性评估方法SAM2ICAA。构建ICAA-4K色彩准确性评估数据集，利用SAM2视觉大模型作为骨干网络，通过多层次特征融合模块整合局部细节和全局语义信息，并设计双任务回归模块同时预测色彩质量分数和失真类型。
    *   **关键实验结论：** SAM2ICAA在ICAA-4K数据集上，SRCC和PLCC等评价指标超越了现有主流NR-IQA方法，达到新的技术基准。
*   **《图像与视频质量评价综述》 (2024)** [cjig.cn](https://www.cjig.cn/zh/article/doi/10.11834/jig.210314/)
    *   **研究问题：** 综合梳理图像/视频质量评估领域的发展历程，包括传统方法与深度学习方法，并分析其优缺点。
    *   **核心方法：** 回顾全参考、半参考和无参考三类评价方法，具体涵盖基于结构信息、人类视觉系统和自然图像统计的方法。分析代表性算法在LIVE、CSIQ、TID2013等公开数据集上的性能。
    *   **关键实验结论：** 传统SSIM算法作为里程碑意义的方法，显著提升了客观评价与主观感知的一致性；深度学习方法在复杂场景中表现出更高的复杂性与更好的性能。

### 实验与评价总结

结构相似性度量方法，包括SSIM、MS-SSIM以及基于其思想的改进算法，在图像质量评估领域展现出较好的性能。相较于传统的MSE和PSNR，SSIM类指标能够更好地捕捉人类视觉感知的高级特性，尤其是在图像结构保持方面的优势显著。在标准公开数据集，如LIVE、CSIQ、TID2013等上的实验结果普遍表明，SSIM及其变体与人类主观评价具有更高的一致性，通过Spearman秩次相关系数 (SRCC) 和Pearson线性相关系数 (PLCC) 等指标体现出更强的单调性和准确性 [cjig.cn](https://www.cjig.cn/zh/article/doi/10.11834/jig.210314/)。

随着深度学习的兴起，SSIM与其他先进技术（如Transformer、多尺度特征融合等）的结合，进一步推动了IQA领域的发展，尤其是在处理复杂失真和无参考场景下。例如，在色彩准确性评估和多尺度图像处理任务中，结合深度学习的模型能够从大量数据中学习更具判别力的特征，从而更好地预测图像质量并识别失真类型 [jcad.cn](https://www.jcad.cn/cn/article/pdf/preview/10.3724/SP.J.1089.2025-00246.pdf), [zhuanzhi.ai](https://zhuanzhi.ai/paper/f8f32014a424d8c112d966eb8bd0dcd3)。

### 趋势与挑战

结构相似性度量技术在图像质量评估领域持续演进，未来将面临以下趋势与挑战：

1.  **多模态与跨模态融合：** 传统的IQA主要关注单一模态图像，未来将更多地整合文本描述、语义信息、深度信息等多模态数据，以实现更全面的感知质量评估。例如，结合视觉大模型如SAM2ICAA，将图像语义与色彩准确性评估相结合 [jcad.cn](https://www.jcad.cn/cn/article/pdf/preview/10.3724/SP.J.1089.2025-00246.pdf)。
2.  **泛化能力与小样本学习：** 现有深度学习模型在特定训练数据集上表现优异，但在面对未见过或少量样本的失真类型时，泛化能力有待提高。发展更鲁棒的小样本、零样本或持续学习 (continual learning) 机制，以适应开放世界中的多样化图像失真。
3.  **可解释性与因果关系：** 随着深度学习模型复杂性增加，其决策过程的透明度降低。未来的研究将致力于提升SSIM类模型的解释性，理解模型为何做出特定质量判断，并探索图像质量失真与人类感知之间的因果关系，而非仅仅相关性。

### 结论

本综述回顾了2022-2025年间图像质量评估领域中结构相似性度量技术的重要进展。从SSIM的基础改进、多尺度与变换域扩展，到与深度学习的深度融合，这些方法在提升图像质量评估的准确性和与人类感知的一致性方面取得了显著成就。特别是，结合Transformer和视觉大模型的技术路线，展现出处理复杂和无参考质量评估任务的巨大潜力。未来的研究将聚焦于多模态融合、提升模型泛化能力和可解释性，以应对不断涌现的图像处理应用需求与挑战。

### 参考文献

1.  Jin, J., Zhou, T., Hu, Z., & Yang, B. (2025). SAM2ICAA: No-Reference Image Color Accuracy Assessment Via Vision Foundation Models. *Journal of Computer-Aided Design & Computer Graphics*, 3*(?).* [jcad.cn](https://www.jcad.cn/cn/article/pdf/preview/10.3724/SP.J.1089.2025-00246.pdf)
2.  Ke, J., Wang, Q., Wang, Y., Milanfar, P., & Yang, F. (2021). MUSIQ: Multi-scale Image Quality Transformer. *ICCV 2021*. [zhuanzhi.ai](https://zhuanzhi.ai/paper/f8f32014a424d8c112d966eb8bd0dcd3)
3.  Li, Y., Li, J., Xue, T., Mu, J., Wang, Q., Zheng, L., Wang, Y., & Lei, L. (2025). 基于PSNR和SSIM方法评估双能量CT肝脏虚拟平扫图像质量研究. *CT理论与应用研究*, 34*(?)*. [cttacn.org.cn](https://cttacn.org.cn/article/doi/10.15953/j.ctta.2024.151)
4.  Mittal, A., Moorthy, A. K., & Bovik, A. C. (2012). No-reference image quality assessment in the spatial domain. *IEEE Transactions on Image Processing*, 21(12), 4695-4708. [blog.csdn.net/bby1987](https://blog.csdn.net/bby1987/article/details/109373572) (cited as general SSIM reference)
5.  Wang, Z., Bovik, A. C., Sheikh, H. R., & Simoncelli, E. P. (2004). Image quality assessment: From error visibility to structural similarity. *IEEE Transactions on Image Processing*, 13(4), 600-612. [blog.csdn.net/bby1987](https://blog.csdn.net/bby1987/article/details/109373572) (cited as general SSIM reference)
6.  Cheng, R., Yu, Y., Shi, D., & Cai, W. (2024). 图像与视频质量评价综述. *中国图象图形学报*, 27(5), 1410-1429. [cjig.cn](https://www.cjig.cn/zh/article/doi/10.11834/jig.210314/)
7.  Chen, J., Li, S., Lin, L., Wang, M., & Li, Z. (2022). 模糊失真图像无参考质量评价综述. *自动化学报*, 48(3), 689−711. [aas.net.cn](https://www.aas.net.cn/cn/article/doi/10.16383/j.aas.c201030)
8.  Yang, W., Qiu, T., Zhang, Z., Shi, B., & Zhang, M. (2024). 基于深度学习的视频质量评价方法研究综述. *现代信息科技*, 2024(7), 73-81. [m.fx361.com](https://m.fx361.com/news/2024/0618/24274642.html)
9.  Fang, Y., Sui, X., Yan, J., Liu, X., & Huang, L. (2021). Progress in no-reference image quality assessment. *Journal of Image and Graphics*, 26(2), 265-286. [m.fx361.com](https://m.fx361.com/news/2022/0523/11066226.html) (cited as general IQA review)
10. Anonymous. (2022). 图像质量评价领域前沿综述（2022）. [blog.csdn.net/qq_36306288](https://blog.csdn.net/qq_36306288/article/details/124016593) (cited as general IQA review)
11. Ponomarenko, N., Ieremeiev, O., Lukin, V., Egiazarian, K., Jin, L. N., Astola, J., & Kuo, C. C. J. (2015). Image database TID2013: Peculiarities, results and perspectives. *Signal Processing: Image Communication*, 30, 57-77. [m.fx361.com](https://m.fx361.com/news/2022/0523/11066226.html) (cited as dataset reference)
12. Larson, E. C., & Chandler, D. M. (2010). Most apparent distortion: full-reference image quality assessment and the role of strategy. *Journal of Electronic Imaging*, 19(1), 011006. [m.fx361.com](https://m.fx361.com/news/2022/0523/11066226.html) (cited as dataset reference)