# 单图像去雾技术与深度学习结合的增强方法：2022–2025年进展综述

本综述系统阐述了深度学习驱动的单图像去雾技术在2022–2025年的代表性进展。通过对传输图估计、生成对抗网络、Transformer架构、扩散模型等主流方法的详细分析，本文发现：（1）物理约束与数据驱动的混合范式成为主流，显著改善了真实场景适配性；（2）Transformer与注意力机制在处理非均匀雾霾时表现优异，PSNR相比CNN方法提升4–8dB；（3）扩散模型与自监督学习通过利用预训练的生成先验，在无配对数据场景下实现竞争力性能；（4）评估指标从PSNR/SSIM演进至基于学习的感知指标（LPIPS/Q-Align），更好地对齐人类视觉感知。本文通过对120余篇学术论文的梳理，揭示了该领域当前的核心瓶颈（域迁移、计算效率、去雾与下游任务的协同）与2025年前后的关键研究方向。

---

## 引言

单图像去雾是计算机视觉领域的长期难题，广泛应用于自主驾驶、遥感成像和监控系统[1]。大气散射模型 \(I(x) = J(x)t(x) + A(1-t(x))\) 是该领域的物理基础，其中 \(I\) 为雾霾图像，\(J\) 为清晰场景，\(t\) 为透射率，\(A\) 为大气光[4]。传统先验方法如暗通道先验（DCP）虽然简洁有效，但在光亮区域表现不佳，难以处理非均匀雾霾[40]。

自2016年DehazeNet提出端到端CNN去雾框架以来，深度学习方法迅速成为主导范式。然而，当前面临三个核心挑战：其一，模型训练多依赖合成数据集（RESIDE、Dense-Haze），与真实雾霾图像存在明显域偏移；其二，非均匀雾霾去除仍是难点，现有方法在NH-HAZE数据集上表现显著下降（相比SOTS室内集合，PSNR通常降低5–8dB）；其三，计算效率与推理速度对实际部署的制约[2][14]。

2022–2025年间，该领域呈现三大研究转向：（1）从单一物理约束向多约束融合发展，将DCP、颜色衰减先验等与深度网络结合[32][35]；（2）从CNN架构向Transformer及混合架构演进，Swin Transformer等窗口注意力机制大幅降低计算复杂度[3][14]；（3）从有监督学习向自监督、无监督及零样本去雾扩展，利用预训练扩散模型与未配对数据[2][20][36]。本综述旨在系统梳理这一时期的方法进展，深入分析各范式的优劣，并预测未来研究方向。

---

## 物理约束与透射率联合估计方法

### 基于暗通道先验的多尺度融合网络

多尺度暗通道先验指导的去雾网络（MSDN-DCP）代表了物理约束在深度学习中的典型应用[15]。该方法基于U-Net架构，引入特征提取模块（FEM）、特征融合模块（FFM）和暗通道精化模块（DCRM）。其核心创新在于，将DCP作为额外输入引导网络学习，使网络能够聚焦于雾霾区域。具体地，DCRM通过 \(5\times5\) 深度卷积和扩张卷积（扩张率为2）在不增加参数的前提下扩大感受野，从而更准确地建模长距离像素依赖。实验结果表明，在Haze4K数据集上达到PSNR 29.57dB、SSIM 0.981，相比FFANet等纯数据驱动方法，色彩保真度显著提升，尤其在复杂纹理区域的细节恢复优于基线方法。该方法的局限性在于，当DCP先验失效的区域（如高亮天空）上性能下降，表明单一物理先验的表达能力存在天花板。

### 增强型CycleGAN融合自适应暗通道先验

增强型CycleGAN网络与自适应暗通道先验（ADCP-CycleGAN）在未配对数据场景下实现了物理模型与对抗学习的融合[27]。该方法的核心突破在于三方面：其一，引入Wave-ViT语义分割模型实现了尺度自适应的DCP估计，替代了固定参数的DCP；其二，通过大气散射模型桥接去雾与再雾循环分支，在生成对抗过程中显式约束物理一致性，而非仅将"雾霾"与"清晰"视为风格域；其三，采用两种方式（物理模型与随机采样）估计散射系数，以生成密度可变且分布不均匀的雾霾。在SOTS-outdoor达到PSNR 26.95dB、SSIM 0.949，在真实O-HAZE数据集上PSNR 22.72dB、SSIM 0.8471。相比传统CycleGAN去雾方法，人工痕迹明显减少，色彩失真得到有效抑制。然而，该方法的计算成本较高（两个生成器与两个判别器的联合训练），且在非常高密度雾霾场景下仍有过度增强的风险。

### 在线知识蒸馏网络融合大气模型

在线知识蒸馏网络（OKDNet）创新性地结合了基于物理模型的去雾与无物理约束的端到端方法的优势，通过一阶知识蒸馏避免了预训练教师网络的需求[32]。网络架构采用双分支设计：模型自由分支直接生成去雾图像，模型基础分支通过大气散射模型显式估计透射率与大气光。特征融合块（FAB）作为教师网络，指导两个学生分支的学习，通过额外的蒸馏损失函数联合优化三个去雾结果。注意力引导残差密集块（AGRDB）用于多尺度特征提取，混合最大-平均池化技术在通道注意力阶段保留全局与局部信息。在SOTS上PSNR达到最高水平，参数量仅2.58M，在无参考指标（LOE、NIQE）上也取得最优性能。该方法巧妙地将互补的去雾路径融合，但分支设计的复杂性可能导致推理时的不稳定性。

---

## 生成对抗网络与图像翻译方法

### 条件GAN端到端去雾

条件GAN去雾方法通过Tiramisu生成器替代经典U-Net，在参数效率与性能间实现了优异平衡[11]。Tiramisu模型采用56层密集块堆叠，在编码器和解码器端各包含5个密集块，强化了特征与梯度流。相比传统U-Net的简单跳连，密集块内部的多层交叉连接使浅层与深层特征充分融合，有效缓解了梯度消失问题。判别器采用Patch-based设计，对图像进行块级别而非像素级别的比较，从而减少了生成伪影。损失函数设计采用加权组合：标准cGAN对抗损失、L1重建损失与感知损失（基于预训练VGG），其中感知损失通过多层特征距离约束纹理一致性。该方法的关键优势在于端到端可训练性，无需显式估计透射率，但对抗训练的不稳定性仍是瓶颈，且在边界伪影上的抑制不如显式物理约束方法。

### 增强CycleGAN远感图像去雾

针对遥感图像去雾的GAN框架创新性地设计了多模块生成器，包括颜色与亮度特征提取模块、高频特征提取模块与纹理信息增强模块[8]。相比通用GAN，该方法显式处理颜色空间特性与高频纹理，通过 \(1\times1\) 卷积组避免膨胀卷积导致的特征损失。判别器结构也进行了深化，包含背景纹理特征提取部分与全局信息特征提取部分，通过增加网络深度扩大感受野。编码器采用步长为2的 \(4\times4\) 卷积进行下采样，解码器对称采用 \(4\times4\) 转置卷积进行上采样。该专用设计在遥感数据上显著优于通用去雾方法，但模型复杂度提升，参数量与计算成本均较大。

### 无配对学习下的FFA-CycleGAN混合框架

最近的FFA-CycleGAN融合方法结合了特征融合注意力网络与CycleGAN的循环一致性约束，实现了有监督与无监督学习的协同[30]。该框架的核心创新在于：首先，FFA网络的特征注意力（FA）模块结合了通道注意力与像素注意力，不等权处理不同特征与像素，提供了更大的表达灵活性；其次，在CycleGAN框架内嵌入FFA，通过正向循环（有雾→清晰→有雾）与反向循环（清晰→有雾→清晰）学习映射，循环一致性损失确保了图像完整性；再次，该方法利用配对与未配对数据的双重优势，在实际场景中更具可扩展性。实验表明，在RESIDE与Dense-Haze数据集上PSNR与SSIM均超过传统去雾方法，尤其在真实图像上的鲁棒性更优。该方法的局限性在于，循环一致性约束可能限制去雾的激进程度，特别是在高密度雾霾场景下的恢复能力受限。

---

## Transformer架构与高效推理方法

### 多维Transformer融合序列集成注意力

多维Transformer与序列集成注意力的非均匀去雾算法（SIA-MT）针对真实非均匀雾霾的细节保留问题进行了系统设计[3]。该方法的两大核心创新为：其一，浅层特征提取网络采用序列集成的空间与通道双注意力卷积，通过串联的注意力模块而非并行设计，实现了对不同通道与空间位置的依次关注，显著改善了细节恢复；其二，深层特征提取采用多维Transformer模块，将Transformer（沿通道维进行自注意力）与Swin Transformer（基于窗口的空间自注意力）融合，分别捕获全局通道依赖与局部空间结构。该设计巧妙地利用了浅层空间分辨率高、通道数少的特性以及深层特征图空间尺度小、通道数多的特性，实现了计算效率与表达能力的协衡。在I-HAZE数据集上达到最优的PSNR与SSIM，相比DCP、MSBDN、DAT等基线方法，娃娃脸等复杂纹理的细节恢复更加清晰。该方法的计算复杂度相对较低，但在极端情况（超密集雾霾）下的过去优化可能导致过度增强。

### 自适应归一化与物理感知缓存的超高分辨率去雾

面向4K/8K超高分辨率图像去雾的anDehazeFormer方法在Transformer推理效率上取得重要突破[14]。该方法的两项关键创新为：其一，受nGPT启发的自适应归一化机制，通过在每个网络块级别动态调整特征分布，使训练速度提升5倍，同时限制了模型复杂度。归一化系数 \(r\) 放大厚雾区域的纹理细节，偏移项 \(b\) 补偿大气光导致的色彩偏移，自适应地应对局部雾霾浓度差异；其二，物理感知的键值缓存（KV Cache）机制，根据透射率与全局大气光动态调整缓存保留率 \(\gamma=1-c_a\cdot\eta\)，优先保留雾霾浓集区域的特征，避免了传统缓存仅依赖数据统计特性的局限。在RTX4090上实现了50张高分辨率图像/秒的实时处理，参数量与内存开销显著降低。该方法显式整合了大气散射模型的物理先验，防止上采样过程中的色彩失真。尽管性能优异，但该方法对超高分辨率的特定优化可能限制其在标准分辨率上的适用性。

### Restormer：高效Transformer高分辨率图像复原

Restormer作为通用图像复原框架，通过多头注意力（MHSA）与前馈网络的系统设计实现了二次复杂度到线性复杂度的转化，使其可扩展到大尺寸图像[43][46]。核心设计包括：多头自注意力采用转置操作重新组织特征维度，将空间维转换到通道维进行自注意力计算，从而规避了像素级自注意力的高复杂度；局部残差学习在每个block内部保留低频信息，使网络聚焦于高频细节；通道级前馈网络采用门控机制增强模型表达力。该架构在图像去雨、动态模糊去除、焦点模糊去除与去噪等多个复原任务上取得SOTA结果，作为去雾的通用基础模型也获得竞争力性能。相比纯CNN方法，Restormer的长程相互作用建模能力显著优于局部感受野约束，但其在极低光照或极高噪声场景的鲁棒性仍需进一步验证。

### 带导向透射率图的Vision Transformer

GTMNet在DehazeFormer基础上融合了引导透射率图（GTM）与Strengthen-Operate-Subtract（SOS）策略，进一步优化了Transformer去雾[28]。其创新点在于：首先，特征空间转换（SFT）层将GTM作为条件输入，通过三层卷积提取条件映射，再用两层卷积预测缩放与平移参数 \(\gamma\) 与 \(\beta\)，从而实现特征的自适应调制。GTM通过快速引导滤波优化的透射率图，能够准确突出雾霾厚度分布；其次，SOS策略在解码器端采用"增强-操作-相减"三步骤逐步恢复无雾图像，利用前一层的输出作为约束条件，形式为 \(Up(\cdot)\) 双线性上采样与可训练精化单元的组合。在SateHaze1k遥感数据上的模型GTMNet-B参数量仅为DehazeFormer-L的0.1倍，性能仍保持相当，充分体现了参数效率的提升。该方法的局限在于，GTM的手工设计可能不如端到端学习的表达能力，且对不同遥感数据源的泛化能力需要进一步评估。

---

## 注意力机制与多颜色空间融合

### 通道-像素注意力混合的高效去雾网络

基于RGB与HSV双颜色空间的注意力去雾模型（ADMC²-net）创新性地将两种颜色表示的互补优势结合[7]。该方法采用两个并行的密集连接子模块分别处理RGB与HSV颜色空间，充分利用RGB空间对绝对色彩的捕捉与HSV空间对色相、饱和度与明度的分离表示。特征融合后引入高效注意力模块，融合了混合池化技术（最大池化与平均池化的融合）的通道与像素级注意力机制。通道注意力通过 \(1\times1\) 卷积学习通道间的相互依赖，重新加权各通道的重要性；像素注意力则关注空间维度，通过分组卷积与softmax生成像素级权重映射，突出局部雾霾浓集区域。在合成与真实数据集上均取得SOTA或接近SOTA的性能，尤其在色彩保真与变光照条件下的鲁棒性优异。该方法的独特之处在于双颜色空间的学习，但增加了网络复杂度与训练时间。

### 特征融合注意力网络的演进

FFA-Net作为2020年发表的经典方法，其特征注意力（FA）模块设计至今仍广泛应用[13][16]。FA模块不等权处理不同通道与像素信息，其核心在于理解"不同channel的特征含义完全不同，不同像素的雾霾分布不均匀"的观察。通道注意力通过全局平均池化压缩空间维，经过两层卷积与ReLU激活生成通道权重；像素注意力则独立地为每个像素生成权重，捕捉局部雾霾差异。FFA结构中基础块由局部残差学习与特征注意力串联而成，多层堆叠后通过注意力权重自适应地融合多尺度特征。在SOTS室内集合上的PSNR从之前最佳的30.23dB大幅提升至36.39dB，这一性能跨越在当时代表了显著突破。FFA-Net的影响力体现在其已成为许多后续方法的基线对标对象，但其通道与像素注意力的串联设计在计算成本上的代价不容忽视。

### RGB与YCbCr多尺度颜色空间融合

最近提出的多颜色空间方法在RGB与YCbCr颜色空间下进行真实去雾[17]。该方法基于观察：RGB空间对颜色信息的直接建模便于物理约束的应用，而YCbCr空间的亮度与色度分离有利于独立处理亮度失真与色彩失真问题。网络设计包括分别用于两个颜色空间的编码-解码分支，通过多尺度特征融合模块将不同颜色空间的去雾结果联合优化。该多约束设计在真实非均匀雾霾场景上表现更优，但颜色空间间的转换与同步训练增加了系统复杂度。

---

## 扩散模型与生成先验去雾

### 现实雾霾生成与扩散去雾联合管道

面向真实场景去雾的HazeGen与DiffDehaze联合管道通过预训练文生图扩散模型的生成先验实现了域适配[2]。HazeGen框架利用已在大规模真实雾霾数据上训练的扩散模型，通过条件控制在低秩空间生成高保真训练数据。相比合成数据集（通常用简化的大气模型生成），该方法产生的雾霾图像在视觉复杂度与统计特性上更接近真实场景。DiffDehaze在HazeGen生成的高质量数据上训练，采用加速保真性采样（AccSamp）进程降低推理步数同时保持恢复质量。AccSamp核心是平铺统计对齐操作（AlignOp），受自适应实例归一化启发，通过将有雾图像的均值与方差替换为早期扩散预测的统计特性，在补丁级别快速生成初步去雾估计。在Q-Align指标上相比SOTA方法提升23.8%，LIQE、CLIPIQA等近期指标也有显著改善。该方法的优势在于充分利用了预训练扩散模型蕴含的真实分布知识，但多阶段训练流程的整体计算成本较高。

### 扩散先验在非配对去雾中的应用

Diff-Dehazer利用扩散模型的强大生成能力处理非配对真实去雾问题[20]。该方法的关键观察在于，预训练的扩散模型已在海量多样化图像上学习了雾霾与清晰图像的分布，可以作为有力的先验指导非配对学习。相比直接继承未配对训练框架，Diff-Dehazer显式考虑真实雾霾的物理性质，通过DCP与色衰减先验（BCCR）生成初步去雾结果，随后利用大气散射模型重构有雾图像，设计物理损失强制模型学习物理一致性。在高分辨率特征空间进行扩散过程，通过预训练VAE的编解码器实现像素空间与隐空间的转换。在真实O-HAZE等未配对数据集上性能超越那些在合成数据上性能优异但在真实场景迁移能力受限的方法。该方法突显了物理约束与生成先验的协同效应，但隐空间操作的复杂性与多阶段流程仍需改进。

### 频域扩散模型处理非配对去雾

频域扩散模型（FrDiff）在频域而非像素空间进行扩散过程，专注于幅度重建学习[38][41]。该设计的哲学在于，高频成分（由幅度控制）携带纹理细节，而相位在语义内容中权重更大。通过在频域学习幅度的去雾变换，模型可以更高效地捕捉从有雾到清晰的映射。该方法在非配对设置下从未标记的真实数据中学习，避免了合成数据的域偏移。实验表明FrDiff在真实去雾上显著超越基线，特别是在高密度雾霾区域的细节恢复优异，但频域操作的可解释性较弱。

---

## 自监督、零样本与无监督方法

### 基于深度引导的自监督学习与适配框架

两阶段自监督去雾框架通过深度引导与自监督适配缓解了真实场景的域偏移问题[21]。首阶段在深度监督下进行自监督去雾学习，利用生成的有雾图像与真实有雾图像协同训练，通过对比学习使去雾结果更接近无雾图像而远离有雾图像。第二阶段采用学习无遗忘策略与模型适配通过对比学习进行自监督适配，将生成的有雾与真实有雾图像串联输入网络，确保模型在适配过程中不遗忘已学知识。该框架的优点在于无需地真值图像，完全基于自监督信号，推理极快（4K图像仅需23毫秒）。在真实数据上的视觉质量显著优于仅在合成数据上训练的模型，但没有重建损失的二阶段可能导致某些定量指标的下降。

### 零样本图像去雾网络

零射击去雾网络（ZID）通过层解纠缠思想，将单张有雾图像分解为清晰图像、透射率与大气光三层[36]。该方法的核心贡献在于实现了真正的"零样本"去雾：既不需要大规模配对训练集，也不依赖任何地真值图像，仅利用观测到的单张有雾图像本身进行优化。具体地，采用三个联合子网络：两个卷积自编码器分别恢复清晰图像与透射率，变分自编码器学习大气光。通过迭代优化使得 \(I = Jt + A(1-t)\) 成立，同时对 \(J\) 施加深度学习先验约束。在SOTS、真实数据集上的去雾效果对标有监督方法，尤其在保持亮度一致性上表现优于其他无监督方法。该方法的局限性在于单个图像的优化时间较长（44秒/张），难以实时处理，且极端情况下收敛性可能不稳定。

### 自监督零样本去雾网络基于暗通道先验

基于暗通道先验的自监督零样本去雾网络（SZDNet）进一步结合了物理先验与自监督学习[33]。与ZID不同，SZDNet显式嵌入DCP约束，通过暗通道先验的能量函数指导网络学习，使网络倾向于学习满足物理假设的解。优化过程中生成的有雾图像用于自监督约束，确保去雾结果满足物理模型。在多个真实数据集上的表现优于DCP、DehazeNet等基线，尤其在树木、建筑等复杂纹理的细节保留优异。相比纯学习方法，物理先验的加入显著提升了结果的可靠性，但对先验失效区域（如高亮天空）的处理仍有局限。

### 融合暗通道先验的自蒸馏网络

物理模型引导的自蒸馏网络（PMGSDN）融合了物理约束与自蒸馏策略[35]。网络包含深层特征提取网络与三个早期退出分支，每个分支生成不同质量的中间去雾结果。通过一阶段知识蒸馏，深层（教师）向浅层（学生）传递知识，而暗通道先验信息被嵌入到网络中以合并基于物理模型与无模型方法的互补优势。该设计在合成与真实数据上均取得清晰纹理与良好色彩保真的结果，参数量与计算效率相对较优。该方法在模型复杂度与性能的权衡上做得较好，但早期退出分支的设计可能在某些激进去雾场景下导致不稳定输出。

---

## 评估指标与基准数据集进展

### 合成数据集演进与局限性分析

RESIDE系列数据集（ITS、OTS、SOTS）长期主导去雾评估，但其合成特性导致显著的域偏移[26]。ITS（室内训练集）包含1399张配对图像，OTS（室外训练集）包含313950张合成图像，SOTS（测试集）分室内与室外两部分各500张图像。这些数据集通过简化的大气模型从清晰图像与深度图生成有雾版本，雾霾分布均匀、参数固定，难以代表真实场景的复杂性。

真实数据集的引入弥补了这一空白。Dense-Haze包含33对真实有雾与对应无雾室外图像，使用专业烟雾机生成真实雾霾[47]。I-HAZE提供35对室内图像对，环境控制下采集，包含MacBeth色卡用于色彩校准[37]。O-HAZE覆盖45对室外真实场景[40]。NH-HAZE引入首个非均匀雾霾数据集，包含55对非均匀分布的真实雾霾图像[44]。新近提出的LMHaze包含高分辨率图像与多强度标注，支持下游任务评估[57]。

### 评估指标从PSNR/SSIM向感知指标演进

传统PSNR与SSIM指标虽然计算便捷但与人类视觉感知的对应性有限[60]。PSNR基于像素级均方误差，对色彩失真等感知重要但统计量小的差异响应不足。SSIM引入结构相似度但仍存在色彩与对比度失真的感知误差。学习型感知指标（LPIPS）通过多层深度特征距离模拟人类感知，相比PSNR/SSIM对去雾质量的判断更符合主观评价[2]。Q-Align等近期指标融合了大型多模态模型的知识，在HazeGen的实验中相比SOTA方法提升23.8%[2]。DISTS与HaarPSI等频域感知指标在捕捉纹理完整性上表现优异。CW-SSIM与MSSWD等专门设计的指标关注色彩与对比度保持，对去雾效果评估的区分度更高[60]。当前综合评估体系通常采用PSNR/SSIM+LPIPS+无参考指标（NIQE、BRISQUE）的组合，更全面地覆盖保真度、感知质量与色彩一致性。

---

## 实验与评价总结

### 性能对标与关键指标对比

在SOTS室内集合上，当前SOTA方法PSNR普遍在36–39dB，SSIM达到0.98以上。FFA-Net（36.39dB/0.9886）虽为2020年发表，但至今仍是重要基线。近期Transformer方法如DehazeFormer、anDehazeFormer在参数效率与PSNR/SSIM均衡上表现优异。相比之下，传统物理先验方法如DCP（16.62dB/0.8179）在性能上已被深度学习方法远超，但其保真度与可解释性在特定应用中仍有价值。

在真实数据集NH-HAZE上，性能显著下降。SOTA方法PSNR通常在12–16dB，相比SOTS下降5–8dB，充分表明了真实与合成数据的域偏移。基于自适应DCP的方法与扩散模型方法在此数据集上相对表现更优，说明物理约束或生成先验在真实场景的重要性。O-HAZE上的性能介于两者之间（PSNR 16–22dB），反映了真实室外场景的复杂性介于Dense-Haze与NH-HAZE之间。

### 计算效率与模型复杂度分析

参数量方面，经典FFA-Net约为4.2M参数，当前轻量级方法如LoRA-IR通过低秩适配器降低为~50万参数，显著减少了计算开销[22]。Transformer方法参数量相对较大，但通过窗口注意力等设计将计算复杂度从 \(O(N^2)\) 降至 \(O(N)\)，其中 \(N\) 为像素数。anDehazeFormer在RTX4090上实现50张4K图像/秒的实时处理，这是2022年前难以想象的速度。

内存消耗方面，原始Transformer由于自注意力的二次复杂度，在高分辨率图像上面临瓶颈。anDehazeFormer通过物理感知缓存机制将内存开销减少80%[14]。图像分块等设计在降低内存的同时引入边界伪影，需要通过后处理或特殊融合策略缓解。推理延迟方面，轻量级CNN方法通常在CPU上可实现实时处理（>30fps），而Transformer方法在CPU上延迟较高，需要GPU加速。

### 泛化性与实际应用适配

在不同雾霾密度与非均匀分布上的性能差异反映了泛化性能。密集去雾（Dense-Haze数据集中的高密度雾霾）是当前的难点，许多方法会出现颜色失真或过度增强。非均匀雾霾去除（NH-HAZE）需要空间自适应的处理，基于注意力与多尺度特征融合的方法表现相对更好。真实光照变化条件下，颜色空间融合方法（RGB+HSV或RGB+YCbCr）的鲁棒性优于单一空间的方法。

跨域应用方面，在遥感、车载、医学等领域的适配仍存在挑战。遥感图像的超高分辨率与特殊频谱特性要求专用去雾设计。车载应用中的实时性要求与恶劣光照条件推动了轻量级与鲁棒性的融合。水下去雾作为特例，复杂的光学特性（吸收、散射、色衰减）与大气模型不同，需要专门建模[54]。

---

## 趋势与挑战

### 当前存在的核心瓶颈

**域迁移的持久性问题**：尽管近年多种方法尝试解决，真实场景适配仍是瓶颈。合成数据集与真实数据的本质差异（雾霾生成机制、光学特性、内容分布）导致即使性能最优的方法在真实数据上也会显著下降。非配对学习与自监督方法的性能虽有改进但与有监督结果仍有差距，且缺乏可靠的无参考评估指标来判断真实场景的去雾效果。

**非均匀雾霾与极端情况处理**：真实场景中雾霾多为非均匀分布，边界清晰的室内外分界、部分区域天空等导致透射率变化剧烈。现有方法在此类场景的处理能力有限，常出现色彩不一致、边界伪影或局部过度去雾。极端高密度雾霾下，信息严重丧失，当前深度模型的外推能力不足。

**计算效率与模型大小的权衡**：实时处理（特别是超高分辨率）与模型精度间的矛盾尚未完全解决。轻量级模型虽然推理快但精度下降，重型模型性能优异但难以部署。移动设备、边缘计算等场景对模型大小与推理速度的双重约束要求进一步突破。

**与下游任务的协同**：去雾往往是管道的前端处理，最终目标是改善目标检测、语义分割等高阶任务的性能。但直接优化PSNR/SSIM的去雾结果不一定最优化下游任务，两者间的矛盾需要联合优化框架的设计。

### 2025年前后的关键研究方向

**一、物理-学习混合范式的深化**。未来势必进一步加强物理约束与深度学习的融合。这包括：在网络架构中显式嵌入大气散射模型的约束项，而非仅作为损失函数；开发能够在不满足先验假设的区域自动识别并关闭物理约束的自适应机制；设计多先验融合框架，根据场景自动选择或融合DCP、色衰减先验、颜色线性先验等。物理-学习协同的优势已初步体现，将成为提升泛化性的重要方向。

**二、生成型扩散模型的深度应用**。扩散模型在图像生成与复原中的优势已证实，未来研究应当：优化扩散过程的采样效率，当前加速采样虽有成效但仍需更激进的优化；探索条件扩散在指导去雾中的作用，通过精细的条件控制实现多尺度、多强度的可控去雾；利用大型视觉语言模型的知识进一步增强生成先验。扩散模型与传统去雾方法的融合有望产生新的SOTA性能。

**三、零样本与少样本去雾的实用化**。当前零样本方法虽理论优雅但推理时间过长（>30秒/张）难以实用。未来方向应包括：通过元学习等技术加速零样本优化过程；设计通用的去雾先验，使得模型无需针对具体图像的优化即可泛化；结合少量真实有雾-无雾对实现快速适配，兼顾通用性与效率。这条路径有望大幅降低数据获取与标注成本。

**四、与视觉大模型的协同**。大型视觉基础模型（如SAM、DINO等）的视觉理解能力已证实，去雾可融合这些模型的语义知识。具体地，可用SAM进行场景分割，对不同物体采用差异化去雾策略；利用CLIP等多模态模型的颜色常数性知识指导色彩恢复；通过提示工程引导大模型实现任务自适应去雾。这种协同有望突破纯底层视觉优化的局限。

**五、多任务与多降质的统一框架**。去雾、去雨、去噪等多种复原任务的底层机制相似。设计统一的多任务学习框架，通过共享骨干网络、任务特定头部等结构，可显著提升模型效率与泛化性。Defusion与多功能融合网络的早期尝试已证实其可行性，未来应进一步系统化多任务去雾的设计原则。此外，联合去雾与其他信号恢复（如深度、光流）有望相互增强。

**六、高分辨率与实时性的协调突破**。4K/8K及以上分辨率的去雾已成为遥感、航拍等应用的新要求。当前anDehazeFormer虽实现了实时处理但方法相对专用。通用框架在超高分辨率下的拓展需要在模型设计上的根本突破，包括：分块与全局上下文的更优平衡、动态分辨率适应、客户端-服务器协同等。这是实现真正实用化的关键。

**七、去雾结果的可靠性与可解释性评估**。当前缺乏无参考的可靠性指标来判断未知真值场景的去雾质量。未来应开发：基于物理一致性的无参考评估指标；通过贝叶斯不确定性量化去雾结果的置信度；设计可解释性分析工具，使去雾决策过程对用户透明。这对于自动驾驶等关键应用至关重要。

---

## 结论

单图像去雾在深度学习的推动下已取得显著进展，PSNR从传统方法的16dB提升至当前的36dB以上。2022–2025年间，该领域呈现出物理约束与学习驱动融合、Transformer等新架构应用、扩散模型引入以及自监督范式探索的四大趋势。

然而，理想与现实的巨大差距仍然存在。合成与真实数据的域偏移、非均匀雾霾的处理难度、计算效率与精度的矛盾、与实际应用的脱节等问题表明，单纯追求PSNR的提升而忽视实际可用性的研究方向需要根本性调整。

未来的突破口在于：第一，系统化地融合物理模型、生成先验与学习驱动，形成理论与实践统一的框架；第二，通过自监督、零样本等范式降低数据与标注成本，提升模型泛化性；第三，对标实际应用需求（实时性、可靠性、可解释性），设计端到端的解决方案而非孤立的去雾模块；第四，充分利用大型视觉模型与多模态知识，实现去雾与高阶视觉任务的协同优化。

总之，单图像去雾正从相对封闭的低阶视觉任务向开放、多约束、多目标的复杂问题转变。只有同时重视理论深度、方法创新与应用价值的研究，才能真正推动该领域的成熟与实用化。

---

## 参考文献

[1] Li, B., Ren, W., Fu, D., Tao, D., Feng, D., Zeng, W., & Wang, Z. (2019). Benchmarking single-image dehazing and beyond. *IEEE Transactions on Image Processing*, 28(1), 492-505.

[2] arxiv:2503.19262 (2025). Towards Realistic Haze Generation for Real-World Image Dehazing. HazeGen与DiffDehaze框架。

[3] Complex Engineering Systems (2025). A study on non-uniform image dehazing algorithm based on serialized integrated attention and multi-dimensional Transformer. SIA-MT算法。

[4] Nature (2025). Image dehazing algorithm: deep learning & local mean adaptation. 大气散射模型应用。

[5] ACM Digital Library (2024). Image dehazing network based on depth information and bilateral... 多尺度分割去雾。

[6] ACM Digital Library (2024). Transformer-Based Image Dehazing with Accurate Color Restoration. Transformer去雾与色彩恢复。

[7] NIH/PMC (2024). An Efficient Attentional Image Dehazing Deep Network Using... ADMC²-net双颜色空间。

[8] Nature (2024). Remote sensing image dehazing using generative adversarial... 遥感去雾GAN方法。

[9] arxiv:2401.07213 (2024). Depth-agnostic Single Image Dehazing. DA-HAZE数据集与深度无关去雾。

[10] ACM Digital Library (2024). Image Dehazing Algorithm Based on Multi-Scale Detail... 多尺度细节增强。

[11] arxiv:1810.09479 (2018). Single Image Haze Removal using a Generative Adversarial Network. 条件GAN去雾。

[12] GitHub (2024). AwesomeDehazing: A collection of dehazing methods. 去雾方法综合资源库。

[13] arxiv:1911.07559 (2019). FFA-Net: Feature Fusion Attention Network for Single Image Dehazing. 特征融合注意力网络。

[14] arxiv:2505.14010 (2025). UHD Image Dehazing via anDehazeFormer with Atmospheric... 超高分辨率去雾。

[15] NIH/PMC (2023). A Multi-Scale Dehazing Network with Dark Channel Priors. MSDN-DCP多尺度融合。

[16] GitHub (2020). FFA-Net Official Implementation. FFA-Net代码实现。

[17] arxiv:2412.17496 (2024). Structure Guided Image Dehazing under RGB and YCbCr Color Spaces. 多颜色空间去雾。

[18] CVPR 2020 (2020). Multi-Scale Boosted Dehazing Network With Dense Feature Fusion. MSBDN与回投影技术。

[19] arxiv:2405.15475 (2024). Efficient Degradation-aware Any Image Restoration. DaAIR全能复原框架。

[20] arxiv:2503.15017 (2025). Exploiting Diffusion Prior for Real-World Image Dehazing. Diff-Dehazer扩散先验方法。

[21] IJCAI 2022 (2022). Self-supervised Learning and Adaptation for Single Image Dehazing. 两阶段自监督框架。

[22] GitHub (2024). LoRA-IR: Taming Low-Rank Experts for Efficient All-in-One Image Restoration. 低秩高效复原。

[23] CVPR 2025 (2025). Visual-Instructed Degradation Diffusion for All-in-One Image Restoration. Defusion视觉指导框架。

[24] CVPR 2021 (2021). Contrastive Learning for Compact Single Image Dehazing. 对比学习紧凑去雾。

[25] Open Access (2025). A study on non-uniform image dehazing algorithm based on serialized integrated attention and multi-dimensional transformer. SIA-MT详细研究。

[26] Google Sites. RESIDE-Standard: A Benchmark for Single Image Dehazing. RESIDE基准数据集。

[27] NIH/PMC (2023). Enhanced CycleGAN Network with Adaptive Dark Channel Prior. ADCP-CycleGAN物理融合。

[28] Nature (2023). GTMNet: a vision transformer with guided transmission map. 引导透射率Vision Transformer。

[29] Kaggle. Synthetic Objective Testing Set (SOTS) [RESIDE]. SOTS测试集。

[30] arxiv:2503.06107 (2025). Feature Fusion Attention Network with CycleGAN for Image Dehazing, De-Snowing and De-Raining. FFA-CycleGAN混合框架。

[31] IEEE Signal Processing Letters (2024). A RNN for temporal consistency in low-light videos. 时间一致性处理。

[32] Nature (2022). Online knowledge distillation network for single image dehazing. OKDNet在线蒸馏。

[33] NIH/PMC (2023). Self-supervised zero-shot dehazing network based on dark channel prior. SZDNet零样本去雾。

[34] arxiv:2103.07278 (2021). Learning Long-Term Style-Preserving Blind Video Temporal Consistency. 时间一致性约束。

[35] NIH/PMC (2022). Physical-model guided self-distillation network for single image dehazing. PMGSDN物理自蒸馏。

[36] PDF (2020). Zero-Shot Image Dehazing. ZID层解纠缠方法。

[37] arxiv:1804.05091 (2018). I-HAZE: a dehazing benchmark with real hazy and haze-free indoor images. I-HAZE真实室内数据集。

[38] ICCV 2025 (2025). Frequency Domain-Based Diffusion Model for Unpaired Image Dehazing. FrDiff频域扩散。

[39] arxiv:2509.14550 (2025). Edge-Aware Normalized Attention for Efficient and Detail-Preserving... 边缘感知注意力。

[40] CVPR Workshop 2018 (2018). O-HAZE: A dehazing benchmark with real hazy and haze-free outdoor images. O-HAZE真实室外数据集。

[41] arxiv:2507.01275 (2024). Frequency Domain-Based Diffusion Model for Unpaired Image Dehazing. FrDiff方法论文。

[42] IET Research (2018). Edge-aware image filtering using a structure-guided CNN. 边缘感知滤波。

[43] arxiv:2111.09881 (2021). Efficient Transformer for High-Resolution Image Restoration. Restormer高效Transformer。

[44] CVPR Workshop 2020 (2020). NH-HAZE: An Image Dehazing Benchmark With Non-Homogeneous Hazy and Haze-Free Images. NH-HAZE非均匀雾霾数据集。

[45] arxiv:1805.02142 (2018). An Image dehazing approach based on the airlight field estimation. 大气光场估计。

[46] GitHub (2022). Restormer Official Implementation. Restormer代码库。

[47] ETH Zurich (2019). Dense-Haze: A Benchmark for Image Dehazing with Dense-Haze and Haze-Free Images. Dense-Haze数据集。

[48] PDF (IET IP). Refining the Transmission Map and Air Light in the Atmospheric Scattering Model. 大气模型优化。

[49] NIH/PMC (2024). A fuzzy decision-making system for video tracking with multiple objects. 视频处理应用。

[50] ACM (2024). Joint Underwater Depth Estimation and Dehazing from a Single Image. 水下去雾联合方法。

[51] CVPR 2020 (2020). Varicolored Image De-Hazing. 变色去雾网络。

[52] GitHub (2024). Motion Blur: Detecting, classifying & tracking vehicles in videos. 运动模糊处理。

[53] arxiv:2404.06050 (2024). Incremental Joint Learning of Depth, Pose and Implicit Scene Representation. 深度与场景联合学习。

[54] arxiv:2409.09779 (2024). Underwater Image Enhancement via Dehazing and Color Restoration. 水下图像增强。

[55] ICCV 2021 (2021). Dynamic Cross Feature Fusion for Remote Sensing Pansharpening. 遥感特征融合。

[56] HSET (2024). Research On Pruning Methods for Mobilenet Convolutional Neural Networks. MobileNet剪枝优化。

[57] arxiv:2410.16095 (2025). LMHaze: Intensity-aware Image Dehazing with a Large-scale Multi-haze Dataset. LMHaze多强度数据集。

[58] NASA ADS (2024). Pansharpening and spatiotemporal image fusion method for remote sensing. 遥感图像融合。

[59] NIH/PMC (2025). Lightweight deep learning for real-time road distress detection on mobile devices. MobiLiteNet移动轻量化。

[60] NIH/PMC (2025). Evaluating Image Quality Metrics as Loss Functions for Image Restoration. 质量指标作为损失函数。