引言  
单幅图像去雾（single-image dehazing）旨在从被雾/霾退化的观测图像 I(x) 恢复清晰场景 J(x)，是计算机视觉与图像复原的基础课题之一。自基于物理的大气散射模型与统计先验（如暗通道先验）奠定经典方向后，近年研究重心出现两条并行线索：一是以深度学习为核心的端到端/参数估计方法，二是为缩小合成→真实（synthetic→real）域差而提出的无监督/半监督/物理引导与域适配策略。本文在 2022–2025 年间挑选并比较若干具有代表性的工作，按方法类别归纳其问题定位、核心方法与关键实证结论，最后总结实验评价的共性结论并给出若干面向 2025 年前后的趋势与挑战预测。

方法分类与代表作（每类 3–5 篇，按发表时间或代表性排序；每篇 4–6 句）  

A. 物理模型与先验方法（经典基线，仍作为基准与无监督约束）
1) He et al., “Single Image Haze Removal Using Dark Channel Prior” (TPAMI 2011)  
- 问题：在无对的单幅雾图下估计透射率 t(x) 与大气光 A 以反演大气散射模型。  
- 方法：提出暗通道先验（DCP）：非天空局部区域 RGB 通道存在极小值接近 0，基于此估计透射率并通过软抠图/引导滤波精化。  
- 结论：DCP 在多类自然场景上能有效估计透射率并显著提升可视质量，但在天空、大面积亮区或彩色单调区域会引入伪影和颜色失真。  
- 意义：成为后续无监督损失与先验约束（如以 DCP 为损失项训练网络）的标准参考。  

2) Berman et al., “Non-local Image Dehazing” (CVPR 2016)  
- 问题：传统局部先验对复杂颜色分布与非均匀雾失效。  
- 方法：提出雾线／颜色簇假设：干净图像在 RGB 空间可由若干紧密簇表示，有雾后形成穿过大气光的“雾线”，据此进行非局部聚类与传输估计。  
- 结论：在多样颜色场景（包含天空与复杂纹理）上优于 DCP 类局部方法，能够缓解天空与亮区的误估计，但计算量与对颜色簇假设敏感性需权衡。  

3) Fattal, “Dehazing using Color-Lines” (ACM TOG 2014) — 作为补充经典先验  
- 问题/方法/结论（要点）：利用局部颜色线模型估计传输并重建颜色，改善了在复杂纹理区域的恢复精度，成为颜色空间先验类代表。  

B. 监督深度学习（端到端与参数估计网络）
1) Cai et al., “DehazeNet: An End-to-End System for Single Image Haze Removal” (TIP 2016)  
- 问题：用监督学习替代手工设计的先验与分步流程以估计传输图。  
- 方法：构建端到端 CNN 直接从雾图预测透射率，再结合大气散射公式重建清晰图像；引入多尺度卷积单元以提高特征表达。  
- 结论：在合成数据上显著提高 PSNR/SSIM，展示了学习方法对复杂非线性映射的优势，但对真实图像泛化受限。  

2) Li et al., “AOD-Net: All-in-One Dehazing Network” (ICCV 2017)  
- 问题：减少大气散射模型中多个模块对训练与推理的开销与误差累积。  
- 方法：将透射率与大气光合并为单一可学习映射，提出轻量化端到端网络实现直接从 I → J 的学习。  
- 结论：显著加速推理且在合成数据上性能竞争力强，成为实时/嵌入式去雾方法的先导。  

3) Liu et al., “GridDehazeNet: Attention-Based Multi-Scale Network” (ICCV 2019)  
- 问题：多尺度信息传递与注意力机制如何提升细节恢复与泛化。  
- 方法：提出 GridNet 风格的多尺度网络并结合通道/空间注意力模块以加强跨尺度特征交互。  
- 结论：在合成基准（RESIDE/SOTS）上带来显著改进；但同样显示在真实图像上仍需域适配手段以降低合成-真实差距。  

C. 无监督 / 非配对 / 对抗与基于物理的自监督方法（针对合成→真实域差）
1) Engin et al., “Cycle-Dehaze: Enhanced CycleGAN for Single Image Dehazing” (CVPRW 2018)  
- 问题：成对监督数据难以获取，如何用非配对清晰/雾图训练去雾模型。  
- 方法：基于 CycleGAN 框架加入感知一致性与循环损失，并结合去雾任务专用正则以保持结构与颜色一致性。  
- 结论：在无配对训练场景能够得到视觉上更自然的去雾效果，但生成对抗训练易出现模式崩溃与亮度偏移，需要额外稳定化。  

2) Yang et al., “Self-Augmented Unpaired Image Dehazing via Density and Depth Decomposition (D4)” (CVPR 2022)  
- 问题：非配对方法常忽略雾的物理可解释性（散射系数与深度耦合），从而难以实现可控增雾与泛化。  
- 方法：将透射图显式分解为密度（scattering coefficient）与场景深度两个物理可解释量；利用估计深度合成不同厚度雾作为自增强数据并以此驱动去雾网络（无配对训练）。  
- 结论：在若干真实集上比传统 CycleGAN 类非配对方法表现更稳定，展示了将物理因子融入无监督框架以提升泛化性的可行路径。  
- 相关资源见社区导读：[hub.baai.ac.cn](https://hub.baai.ac.cn/view/17272).  

3) Golts et al., “Unsupervised Single Image Dehazing Using Dark Channel Prior Loss” (TIP 2020)  
- 问题：如何在无监督训练中利用经典先验作为正则而非强制假设。  
- 方法：把暗通道先验作为可微损失项加入对抗训练，结合上下文聚合网络（CAN）预测透射图并由先验损失约束。  
- 结论：在真实图像上能减少合成数据的过拟合现象，表明“先验损失 + 学习器”是可行的折中方案。  

D. 物理引导的合成→真实桥接与半/自监督方法
1) Chen et al., “PSD: Principled Synthetic-to-Real Dehazing Guided by Physical Priors” (CVPR 2021)  
- 问题：合成训练导致模型在真实图像上性能失配（域差）。  
- 方法：在合成→真实的训练范式中引入物理先验约束与合成-真实一致性损失，设计了物理兼容的网络头与大气光估计子网以缓解域差。  
- 结论：在多项无参考质量指标与下游任务（如检测）上优于单纯监督训练，证明物理先验能作为合成→真实迁移的有效桥梁。  

2) Ju et al., “IDE: Image Dehazing and Exposure using an Enhanced Atmospheric Scattering Model” (TIP 2021) — 作为改进 ASM 的代表  
- 问题：传统 ASM 未考虑亮度/反射的复合效应，导致合成数据偏亮，进而引发去雾后亮度损失。  
- 方法：提出增强的大气散射模型并将曝光/照明因素纳入合成流程，从而得到更接近真实分布的合成数据用于训练。  
- 结论：能显著减少因合成分布偏移引起的去雾亮度衰减问题，是改进数据合成管线的示范。  

3) Meng et al., “Real-world dehazing method with invariant learning” (Journal of Zhejiang Univ. (Eng.), 2024)  
- 问题：合成训练与真实测试的分布漂移，经常由特征间的虚假相关（spurious correlations）导致。  
- 方法：采用随机傅里叶特征线性化并在表示空间进行全局样本加权去相关（invariant learning），同时用伽玛校正改进合成策略（构建 DarkHaze）。  
- 结论：在真实基准（RTTS/URHI/Fattal）上的无参考质量与 PSNR/SSIM 稳定性提升，表明不变学习与改进合成可协同提升真实场景泛化。[zjujournals.com](https://www.zjujournals.com/eng/article/2024/1008-973X/20240205.shtml)  

E. 近期生成式 / 注意力 /混合机制方法（2022–2025 的延展方向）
1) Zhao & colleagues, “Contextual collaboration & hybrid attention driven dehazing (HACNet)” (Comput. Appl. Res., 2025)  
- 问题：局部/全局特征融合与多尺度雾浓度差异导致细节复原不足。  
- 方法：提出多域混合注意力与上下文协同网络（CAF+CAAC），强调局部-全局特征自适应融合与多尺度空洞卷积感知。  
- 结论：在 RESIDE、NH-HAZE 等基准上在若干指标上优于同类注意力网络，指出注意力与上下文协同对复杂雾分布的作用。[arocmag.cn](https://www.arocmag.cn/abs/2024.10.0506)  

2) 生成式方法综述（2025）——关于 GAN → 扩散模型 的演进趋势（综述）  
- 内容要点：2025 年综述总结生成式建模（GAN、扩散模型）在去雾中的引入与发展脉络，指出扩散模型在保真度与多样性方面的优势及计算代价问题，建议与物理模型结合以提升可控性与稳健性。[arocmag.cn](https://www.arocmag.cn/abs/2025.06.0198)  

3) Sea-fog 专向处理（天空分割 + 自适应修正）——宋晓东等（Laser & Optoelectronics Progress, 2025）  
- 问题：海雾场景中天空与海面反射导致大气光估计误差与颜色偏移。  
- 方法：先精确分割天空区域，基于区域内前 0.1% 亮度像素中值估计 A，引入自适应修正因子与快速引导滤波细化透射图。  
- 结论：在海景数据集上结构相似度和 PSNR 改进明显，表明任务特定的天空分割可有效降低估计误差。[opticsjournal.net](https://www.opticsjournal.net/Articles/OJc38270e9e69cda90/Abstract)

实验与评价总结（共性结论，避免逐篇复述）  
- 合成基准（RESIDE / SOTS / D-HAZY / I-HAZE/O-HAZE/NH-HAZE）仍为定量比较主流；但合成→真实的域差使得单纯在合成上取得高 PSNR/SSIM 的方法未必在真实图像上稳定。参见 Li et al. 的 RESIDE benchmark 工作及多篇后续研究对此的反复验证。  
- 监督方法在合成数据上常占优（PSNR/SSIM 提升），而非配对/半监督/物理引导方法在真实数据的无参考指标与主观视觉保真方面更鲁棒；因此研究评估需同时包含合成参考指标与无参考/下游任务（如检测）评测。  
- 单一像素级指标（PSNR/SSIM）不能完整反映视觉质量或下游任务性能；近年来研究趋向同时报告无参考指标（NIMA/BIQME/PM2.5）、感知损失/下游任务性能以获得更全面评估（见 ZJU 2024 等工作采用的度量体系）。[zjujournals.com](https://www.zjujournals.com/eng/article/2024/1008-973X/20240205.shtml)  
- 将物理先验以“损失项”或“结构化子网”形式融入深度模型（如 PSD、D4、暗通道损失等）能显著缓解合成-真实差距，但需要谨慎处理先验在极端场景（天空、大面积亮区）下的不适用性。  
- 多尺度与注意力机制（如 GridDehazeNet、HACNet）在细节恢复上效果明显；但若无域适配，其提升多半局限于合成基准。  

趋势与挑战（面向 2025 年前后，至少 3 点，具体可执行方向）  
1) 物理可解释的生成模型成为主流探索方向（GAN → 扩散模型 + ASM 约束）  
- 趋势依据：2025 年综述与若干工作指出扩散模型在生成保真度上的潜力，但单纯数据驱动的生成仍面临可控性问题。结合物理可解释变量（散射系数/深度/光照）可实现可控的“重雾-去雾”循环并用于自监督数据增强（如 D4 的思想）。参见 2025 年综述与 D4/CVPR2022。  
- 挑战/方向：需要设计可微分的物理约束以嵌入扩散模型的采样过程，并解决计算成本（加速采样）与数值稳定性。  

2) 不变学习 / 稳定学习 与 合成数据管线改进 的协同（跨域稳健性）  
- 趋势依据：ZJU 2024 的不变学习工作表明，通过在特征表征中去相关与改进合成（伽玛、暗雾采样）可以同时提升真实场景的亮度保真与鲁棒性。PSD 类物理先验也支持“物理+学习”的混合范式。  
- 挑战/方向：构建可扩展的全局记忆/样本加权机制以实现训练时的全局不变性估计，并将该策略推广到视频/时序去雾与下游任务联合训练。  

3) 任务导向评估与联合训练（dehazing ↔ detection/segmentation）常态化  
- 趋势依据：越来越多研究用下游任务性能（目标检测、分割）作为评估标准，表明去雾的最终目标常是提高视觉系统性能而非单纯视觉美观（Li et al. RESIDE 及后续工作）。  
- 挑战/方向：需要构建带注释的真实雾场下游任务数据集与联合损失，研究如何在保证恢复视觉质量同时最大化任务性能。  

4) 轻量化与实时化（在自动驾驶/监控中的部署需求）与可靠性保障并重  
- 趋势依据：AOD-Net、4K-dehazing 等提出轻量或高效架构以满足实时性；未来将更注重在保证泛化的同时压缩模型体积。  
- 挑战/方向：如何在模型压缩/量化过程中保持对物理先验与域适配机制的保真；硬件感知的联合训练（考虑摄像头特性）可能成为方法要点。  

结论  
2022–2025 年间去雾研究呈现从“纯监督的端到端回归”向“物理引导的生成/无监督/域自适应”并行进化的态势。将物理可解释因子（散射系数、深度、天空分割等）与现代生成模型或不变学习策略结合，是提升真实场景泛化性的有效路径。未来工作需在可解释性、计算效率与“任务导向”评估之间找到可操作的平衡，建立更完整的合成→真实闭环（合成策略改进 → 不变学习 → 真实评估）将是关键。

参考文献（选录，保证真实存在；文内已指向若干资源）  
注：下列条目为主要参照文献/综述，按发表年份排序 / 分类给出（并标注可检索处或已在搜索结果中列出的资源）。  

1. He K., Sun J., Tang X., “Single Image Haze Removal Using Dark Channel Prior,” IEEE Trans. Pattern Anal. Mach. Intell., 2011.  
2. Berman D., Treibitz T., Avidan S., “Non-local Image Dehazing,” Proc. CVPR, 2016.  
3. Fattal R., “Dehazing using Color-Lines,” ACM Trans. Graphics (TOG), 2014.  
4. Cai B., Xu X., Jia K., “DehazeNet: An End-to-End System for Single Image Haze Removal,” IEEE Trans. Image Process., 2016.  
5. Li B., Peng X., Wang Z., Xu J., Feng D., “AOD-Net: All-in-One Dehazing Network,” Proc. ICCV, 2017.  
6. Liu X., Ma Y., Shi Z., Chen J., “GridDehazeNet: Attention-Based Multi-Scale Network for Image Dehazing,” Proc. ICCV, 2019.  
7. Li B., Ren W., Fu D., et al., “Benchmarking Single-Image Dehazing and Beyond,” IEEE Trans. Image Process., 2019 (RESIDE benchmark).  
8. Engin D., Genc A., Ekenel H.K., “Cycle-Dehaze: Enhanced CycleGAN for Single Image Dehazing,” CVPR Workshops, 2018.  
9. Golts A., Freedman D., Elad M., “Unsupervised Single Image Dehazing Using Dark Channel Prior Loss,” IEEE Trans. Image Process., 2020.  
10. Chen Z., Wang Y., Yang Y., et al., “PSD: Principled Synthetic-to-Real Dehazing Guided by Physical Priors,” Proc. CVPR, 2021.  
11. Yang Y., Wang C., Liu R., Zhang L., Guo X., Tao D., “Self-Augmented Unpaired Image Dehazing via Density and Depth Decomposition (D4),” Proc. CVPR, 2022. (community summarize: [hub.baai.ac.cn](https://hub.baai.ac.cn/view/17272))  
12. Ju M., Ding C., Ren W., et al., “IDE: Image Dehazing and Exposure using an Enhanced Atmospheric Scattering Model,” IEEE Trans. Image Process., 2021.  
13. Meng X., Feng Y., Su Z., Zhou F., “Real-world dehazing method with invariant learning,” Journal of Zhejiang University (Engineering Science), 2024. [zjujournals.com](https://www.zjujournals.com/eng/article/2024/1008-973X/20240205.shtml)  
14. Zhao D., Gao L., Li L., “A Method for Fast Image Dehazing Based on Prior Knowledge,” Advances in Applied Mathematics, 2025 (先验+联合滤波方向综述/实现). [pdf.hanspub.org](https://pdf.hanspub.org/aam2025144_622624470.pdf)  
15. Song X.D. et al., “Image Defogging Algorithm for Sea Fog Based on Sky Region Segmentation,” Laser & Optoelectronics Progress, 2025 (sky-segmentation for sea fog). [opticsjournal.net](https://www.opticsjournal.net/Articles/OJc38270e9e69cda90/Abstract)  
16. Zhao Z., He J., “Image dehazing algorithm driven by contextual collaboration and hybrid attention mechanism (HACNet),” Comput. Appl. Res. (Application Research of Computers), 2025. [arocmag.cn](https://www.arocmag.cn/abs/2024.10.0506)  
17. Review: “Research review on generative methods for single image dehazing,” Application Research of Computers (优先出版/2025 review indicating GAN→diffusion trend). [arocmag.cn](https://www.arocmag.cn/abs/2025.06.0198)  
18. Xu H., Zhou J., Zhao L., Hu J., “Semi-Supervised Image Dehazing Network Based on Deep Learning,” Computer Science and Application, 2024 (半监督框架与随机掩码增强). [image.hanspub.org](https://image.hanspub.org/Html/19-1543189_84945.htm)  
19. Ancuti C., Ancuti C.O., De Vleeschouwer C., “D-HAZY: A dataset to evaluate quantitatively dehazing algorithms,” ICIP 2016 (数据集).  
20. Additional references cited in文中综述与对比：FFA-Net / GridDehazeNet / MSBDN / PSD 等多篇工作与数据集论文（详见 RESIDE 与各论文原文）。

（注：上述参考文献为核心代表作及近年综述/方法/数据集，文中对 2022–2025 的论述重点引用了 D4（CVPR2022）、PSD（CVPR2021）、不变学习（ZJU 2024）、以及 2024–2025 年期刊/综述对生成式方法、注意力机制与天空分割等方向的讨论；检索与阅读建议优先查阅原始会议论文或期刊论文以获取实现/超参数细节。）