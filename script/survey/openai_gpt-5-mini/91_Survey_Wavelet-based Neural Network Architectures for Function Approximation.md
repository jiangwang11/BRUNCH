引言  
本综述聚焦 2022–2025 年间以小波变换（Wavelet Transform, WT）为核心组件、用于函数逼近（包括图像/信号重建、算子学习、调制识别等任务）的神经网络架构。与纯时域卷积或傅里叶域方法相比，WT 提供局部化的时频表征，使网络在多尺度上分离低频（全局/形状）与高频（细节/噪声）信息；近年来实证工作表明通过将 WT 嵌入网络层或作为预/后处理模块，可以在参数效率、鲁棒性与有效感受野（ERF）之间取得新的权衡。本文按方法类别——（A）小波域卷积层 / 大感受野模块、（B）多级小波 CNN（低级视觉函数逼近）、（C）小波 + Transformer / 算子学习与信号处理——整理代表性工作并给出统一的实验结论与未来趋势预测。所有引用均为公开论文/预印本或期刊文章；每篇工作介绍限于 4–6 句，突出研究问题、核心方法与关键实验结论。

方法分类与代表作

A. 小波域卷积层与大感受野插件（wavelet-domain convolution modules）
- Finder et al., “Wavelet Convolutions for Large Receptive Fields” (arXiv 2407.05848 / ECCV’24 submission)  
  研究问题：在不成比例增加参数的前提下扩大 CNN 感受野以捕获低频/形状信息并接近 Transformer 的全局混合能力。  
  核心方法：提出 WTConv 层——基于级联 Haar 小波分解，在不同子带上用小卷积核处理并通过逆小波重构，从而以对数级增长的可训练参数实现 k×k 等价的大感受野。  
  关键实验结论：将 WTConv 作为深度可分离卷积替换项插入 ConvNeXt / MobileNetV2，可在 ImageNet 分类与下游分割/检测中提升精度，同时在损坏图像的鲁棒性与对形状（低频）特征的响应上显著增强（相较基线减少参数增长与ERF饱和现象）。  
  参考：见论文/代码与作者说明 [arxiv.org](https://arxiv.org/abs/2407.05848)；汇总页面 [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/38389).

B. 多级小波 CNN：面向图像/医学/遥感的函数逼近（denoising / enhancement / restoration）
（最多选 3 篇代表作）
- Li et al., “WavEnhancer: Unifying Wavelet and Transformer for Image Enhancement” (JCST 2024)  
  研究问题：如何在图像增强任务中从不同频带同时优化局部细节与全局风格？  
  核心方法：将离散小波变换（DWT）分解为低频 LL 与高频 HL/LH/HH 分支，低频由基于 Transformer 的全局风格重映射模块处理，高频由 U-Net 式模块精细化，最后用逆 DWT 重构。  
  关键实验结论：在若干公共增强基准上（PSNR/SSIM/DeltaE 指标）超越对比方法；分析显示小波分解有助于低频颜色/风格保留与高频细节恢复的解耦，从而改善感知与色差指标。 参考：[jcst.ict.ac.cn](https://jcst.ict.ac.cn/cn/article/doi/10.1007/s11390-024-3414-z).

- “WIA‑LD2ND: Wavelet-based Image Alignment for Self-supervised Low‑Dose CT Denoising” (MICCAI 2024 / arXiv preprint)  
  研究问题：在自监督设置下（仅用 NDCT），如何对齐正常剂量与低剂量 CT 的频谱差异以提高去噪效果？  
  核心方法：提出基于小波的图像对齐（WIA）模块：向 NDCT 的高频分量注入噪声以逼近 LDCT 分布；并设计频率感知多尺度损失（FAM），结合小波域的多尺度监督。  
  关键实验结论：在两个公开 LDCT 数据集上，仅使用 NDCT 的自监督方案在高频结构保留与定量指标上优于若干弱/自监督基线，证明小波域对齐对恢复诊断相关高频细节的有效性。 参考：arXiv 摘要/解读 [blog.csdn.net](https://blog.csdn.net/qq_36584673/article/details/147085406)。

- Cheng et al., “Remote Sensing Image Denoising Based On Multi‑Level Wavelet CNN with Attention Mechanism” (Computer Science and Application, 2024)  
  研究问题：在遥感图像去噪中如何扩大感受野同时控制计算成本并保留边缘细节？  
  核心方法：构建多级 DWT/IWT 替代池化/上采样的 U‑Net 风格网络（AMWCNN），在每级用带通道注意力的 CNN 模块处理所有子带以学习频带间重要性。  
  关键实验结论：在 NWPU‑RESISC45 的合成噪声实验中，相较 BM3D、DnCNN 等在 PSNR/SSIM 上取得明显提升，视觉结果显示边缘与纹理更好保留；表明 DWT+注意力可在不丢失信息的下采样下改善恢复质量。 参考：[image.hanspub.org](https://image.hanspub.org/Html/9-1543124_84547.htm)。

C. 小波 + Transformer / 算子学习 / 信号处理方向（函数映射与信号分类）
- Zheng et al., “A Modulation Recognition Method Combining Wavelet Denoising Convolution and Sparse Transformer” (Journal of Electronics & Information Technology, 2025)  
  研究问题：Transformer 在时域信号短长度与序列顺序相关性建模上的局限如何通过小波与稀疏变种弥补以提高调制识别（AMC）性能？  
  核心方法：提出可学习的小波去噪卷积用于生成适配的时频表征，并用稀疏前馈神经网络（SFFN）替代标准自注意力，从而在关键采样点间建模元素关系并减少注意力计算。  
  关键实验结论：在 RadioML2016.10a 与 RML22 数据集上分别将平均识别率提升至 ≈63.8% 与 71.1%，并通过消融展示小波基与采样点设计对性能有系统影响，表明小波域特征与稀疏结构对无线信号分类有实用价值。 参考：[jeit.ac.cn](https://jeit.ac.cn/cn/article/doi/10.11999/JEIT241159?viewType=HTML).

- （对比与基础）Li et al., “Fourier Neural Operator (FNO) for Parametric PDEs” (arXiv / NeurIPS‑family work, 2020)  
  研究问题：如何学习映射函数空间的算子以逼近 PDE 解算子（函数→函数 映射）？  
  核心方法：在频域（傅里叶）上做全局卷积算子学习——通过参数化 Fourier 空间卷积核实现算子通用逼近；为后续基于多尺度/小波的算子学习提供比较基线。  
  关键实验结论：FNO 在若干 PDE 问题上以较少迭代与参数实现高拟合精度；为引入小波域（局部化频率）做算子逼近的后续工作（如 WNO / Wavelet‑based operators）提供了范式与对照。 参考：[arxiv.org](https://arxiv.org/abs/2010.08895).

- 理论与早期坚实基础：Mallat、Bruna 等关于小波散射网络与多分辨率表示的工作（理论支撑）  
  研究问题：如何构建对小变换（平移、旋转等）具有稳定性与不变性的多尺度特征映射？  
  核心方法：小波散射变换（scattering networks）以多尺度小波滤波与模非线性操作串联，形成无学习或弱学习的多层不变表征，能证明对某些变换具有稳定性与保留能量等理论性质。  
  关键结论：散射网络为基于小波的可解释多尺度特征提供理论基石，并被后续可微分小波层/可学小波基的网络化方法借鉴以加强泛化与鲁棒性（参考经典文献）。 代表性参考：Mallat / Bruna 等（见下参考文献）。

实验与评价总结（共性结论，按要求不逐篇复述）
1) 频谱分解带来的低频/高频解耦有助于任务对“形状（低频） vs 细节（高频）”的差异化建模。多篇工作（WTConv、WavEnhancer、WIA‑LD2ND、AMWCNN、JEIT 调制识别）都显示：在相同或更少可训练参数下，采用小波域处理能提高低频信息的利用率并保留高频细节。  
2) 参数与 ERF 的效率改进：将小波分解与小卷积核组合（WTConv 思路）能以对数级参数增长实现大感受野，避免传统大核卷积导致的参数/计算爆炸与 ERF 早期饱和。  
3) 鲁棒性与噪声适应：小波提供的局部时频局部化使网络在面对输入损坏、噪声（高频扰动）时更稳定；在医学 CT 与遥感去噪任务表现为更佳的高频结构保留与主观视觉质量。  
4) 归结性限制与实现成本：DWT/IWT 的离散实现（分解/重构）在 GPU 上并非原生友好，增加了实现复杂度与延迟；不同小波基（Haar、Daubechies 等）在任务上有可观差异，且需额外超参数搜索。  
5) 可解释性与理论支持：小波散射等理论结果为小波层的稳定性与不变性提供支持，但多数端到端可学小波模块的理论逼近性质（特别是在深层网络与算子学习背景下）仍不充分。  

趋势与挑战（面向 2025 年前后、至少 3 点）
1) 从插件模块到端到端可学小波基（learnable wavelet）将成为主流探索方向 —— 趋势理由：WT 的强点在于多尺度分离，但固定基可能欠适配特定数据域；可微分/可学小波基结合轻量化约束能在保持局部化优点同时提高任务特异性（预计 2025–2027 年会出现更多可学小波基的系统化比较研究）。  
2) 小波算子学习（Wavelet Neural Operators）将补足傅里叶算子（FNO）在局部化与边界处理上的不足 —— 趋势理由：算子学习社区已认识到局部化频带对非平稳 PDE 与有界域问题的优势，预计未来 2 年会出现更多基于小波/多尺度基的神经算子并与 FNO 形成体系化比较。  
3) 异构模块协同（小波 + 稀疏注意 / 动态采样）用于短序列 / 实时信号的高效逼近 —— 趋势理由：无线信号、雷达、医疗信号等场景存在短时长与实时性需求；小波去噪 + 稀疏 Transformer/稀疏前馈结构（如 JEIT 提出）是一条可行路径，预计更多工作会优化采样/推理延迟与能耗。  
4) 工程化与硬件友好实现成为瓶颈和研究热点 —— 挑战与方向：DWT/IWT 在主流深度学习库与加速器（Tensor Cores）上尚无充分优化，推动“可微分小波算子的高效 GPU 实现”与“近似多尺度算子的端到端量化/编译”将是可落地研究的关键。  
5) 理论与可证明性：当前多数工作以经验为主，关于“可学小波层对函数空间逼近能力（尤其算子映射）”的定量理论仍不足；从泛化误差、频谱偏差视角给出可测的界将是未来 2–3 年的研究需求。  

结论  
2022–2025 年的代表性工作已把小波从“传统信号处理工具”逐步转化为“神经网络结构化模块/先验”，在函数逼近任务上展示了参数效率、ERF 可扩展性与对低频几何信息的增强。实证证明小波域处理对去噪、图像增强、调制识别与某些算子学习问题具有实际价值；但若要从学术到工程广泛落地，仍需解决可学小波基设计、硬件友好实现与严格理论保证三方面的不足。基于上述趋势预测，未来两年可期待小波算子学习、可微分小波层、以及面向实时/嵌入式的高效实现成为研究热点。

参考文献（不少于 12 篇，按出现顺序/主题混合列出；所有为公开论文或预印本）
- Finder S. E., Amoyal R., Treister E., Freifeld O., “Wavelet Convolutions for Large Receptive Fields,” arXiv:2407.05848 (2024). 资源页与摘要：[chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/38389) / arXiv 上文档 [arxiv.org](https://arxiv.org/abs/2407.05848).  
- Li Z.‑N., Chen X.‑H., Guo S.‑N., Wang S.‑Q., Pun C.‑M., “WavEnhancer: Unifying Wavelet and Transformer for Image Enhancement,” Journal of Computer Science and Technology (JCST), 2024. 论文页：[jcst.ict.ac.cn](https://jcst.ict.ac.cn/cn/article/doi/10.1007/s11390-024-3414-z).  
- Zhao et al., “WIA‑LD2ND: Wavelet‑based Image Alignment for Self‑supervised Low‑Dose CT Denoising,” MICCAI 2024 / arXiv preprint (arXiv:2403.11672). 解读与链接：[blog.csdn.net](https://blog.csdn.net/qq_36584673/article/details/147085406).  
- Cheng L., Yuan H., Li Z., Jia X., “Remote Sensing Image Denoising Based On Multi‑Level Wavelet CNN with Attention Mechanism,” Computer Science and Application (Hanspub), 2024. 文章页：[image.hanspub.org](https://image.hanspub.org/Html/9-1543124_84547.htm).  
- Zheng Q., Liu F., Yu L., Jiang W., Huang C., Gui G., “A Modulation Recognition Method Combining Wavelet Denoising Convolution and Sparse Transformer,” Journal of Electronics & Information Technology (JEIT), 2025. 期刊页：[jeit.ac.cn](https://jeit.ac.cn/cn/article/doi/10.11999/JEIT241159?viewType=HTML).  
- Li Z., Kovachki N., Azizzadenesheli K., et al., “Fourier Neural Operator for Parametric Partial Differential Equations,” arXiv:2010.08895 (2020) — 算子学习基线与比较者。[arxiv.org](https://arxiv.org/abs/2010.08895).  
- Bruna J., Mallat S., “Invariant Scattering Convolution Networks,” IEEE Transactions on Pattern Analysis and Machine Intelligence, 2013 — 小波散射网络的代表性理论工作（多尺度不变/稳定性基础）。（检索页例）：[ieeexplore.ieee.org](https://ieeexplore.ieee.org).  
- Mallat S., “A Theory for Multiresolution Signal Decomposition: The Wavelet Representation,” IEEE Transactions on Pattern Analysis and Machine Intelligence, 1989 — 小波理论基础。检索页：[ieeexplore.ieee.org](https://ieeexplore.ieee.org).  
-（方法延伸/实现与应用类）“WTConv 在工程集成与博客/实现综述与社区实现说明”，多篇在线汇总与代码仓库（实现与复现实用信息）：示例汇总页 [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/38389)；社区复述 [blog.csdn.net](https://blog.csdn.net/lichlee/article/details/142910207).  
-（地学方向）Shi C., Li J., Yan H., “DEM Generalization Based on Curvature Wavelet Transform,” Journal on Earth Information Science, 2025. 期刊页：[dqxxkx.cn](https://www.dqxxkx.cn/CN/10.12082/dqxxkx.2025.250073).  
-（实现/集成/综述）若干 2022–2025 年小波 + 深度学习在超分、去噪、单像素成像等领域的期刊/会议工作与技术报告（代表性实现讨论、注意力融合、可微分小波包实现等），参考示例与实现讨论页：[devpress.csdn.net](https://devpress.csdn.net)、[blog.csdn.net](https://blog.csdn.net)（工业/工程实现细节补充）。  
- Hornik K., Stinchcombe M., White H., “Multilayer feedforward networks are universal approximators,” Neural Networks, 1989 — 函数逼近理论背景（经典）。检索页：[sciencedirect.com](https://www.sciencedirect.com).

（注）文献选择优先列出公开论文/预印本与期刊文章；上文中含若干技术实现或社区汇总链接用于说明工程集成与实现注意事项（实现细节、代码仓库与博客），它们并非用于理论主张但对复现/部署有参考价值。若需我可按类别输出各论文的精读要点、实验设置（数据集、评价指标、训练细节）与可复现代码链接清单。