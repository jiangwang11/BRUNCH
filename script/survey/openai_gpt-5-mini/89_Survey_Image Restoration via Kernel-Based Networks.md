以下为题为“Image Restoration via Kernel‑Based Networks”的学术综述（覆盖 2022–2025 代表性工作）。本文严格基于已发表论文 / arXiv 报道与会议论文综述材料（见参考文献）；对每篇代表作的描述限定在 4–6 句，突出研究问题、核心方法与关键实验结论。  

引言  
- 研究背景：图像复原（去噪、去模糊、去雨/去雪、超分等）对局部细节与长程像素关联均有高要求。传统 CNN 受限于局部卷积核导致的有效感受野限制；Transformer 提供全局建模但代价高。近年“基于核（kernel）”的网络设计成为重要路径——包括极大卷积核（large‑kernel CNN / omni‑kernel）、内嵌卷积核的高效 Transformer 变体、以及在频域/状态空间上以“核”概念实现长程或频率依赖建模的方法。  
- 本综述的范围：聚焦 2022–2025 年使用“核/大核/核分解/状态空间/频域核”等思路改进图像复原的代表性工作，按方法类别分类，每类挑选 3–5 篇具代表性的论文并给出简明评述；最后总结实验共性结论并对 2025 年前后的研究趋势与挑战做预测。  

方法分类与代表作  
（注：每篇 4–6 句，首句交代问题，随后给出方法要点与实验结论；括号中为便于查阅的网络来源。）

A. 大核 / Omni‑Kernel 类（直接扩展卷积核以扩大有效感受野，在图像复原瓶颈处部署以控制计算）  
1) Omni‑Kernel Network (OKNet) — “Omni‑Kernel Network for Image Restoration” (AAAI/作者公开稿 /综述)  
- 问题：如何在保持计算效率的前提下，用卷积网络获得接近 Transformer 的全局或大范围感受野以提升复原效果。  
- 方法：提出全核模块（OKM），在瓶颈处并行三路（局部、大核、全局分支）：大分支用极大核（作者探索到高至 63×63 的深度可分解卷积 与条带形状卷积）、全局分支通过“双域通道注意 + 频域空间注意”补偿训练／推理尺度差异、局部分支用 1×1 深度卷积保留局部细节。  
- 实验结论：作者在多个去雾、去模糊、去雪等基准上报告了显著的数值与视觉提升，并指出仅在 bottleneck 部署大核可兼顾性能与 FLOPs（详见实现与消融）。（综见实现与解读）[blog.csdn.net](https://blog.csdn.net/a486259/article/details/142406557) 。  

2) Omni/全核模块在 CNN 中的进一步讨论与落地（OKM 消融与大核取值实验）  
- 问题：大核是否总带来收益与何处部署最有效。  
- 方法要点：将大核（K×K）与基于条带（1×K, K×1）的大核并行使用，并仅放在空间分辨率最低的瓶颈层以节省计算；同时辅以频域或通道注意力增强全局性。  
- 实验结论：作者报告随着核尺寸增长到极大值（如 63）PSNR/SSIM 在若干数据集上连续提升，但代价通过瓶颈放置和分解设计得到缓解；条带卷积能补充不同形状的感受野。（实现与数据见同上）[blog.csdn.net](https://blog.csdn.net/a486259/article/details/142406557) 。

B. 状态空间 / Mamba 与频域耦合类（用选择性状态空间模型或在频域上“核化”长程依赖）  
1) MambaIR: A Simple Baseline for Image Restoration with State‑Space Model — ECCV 2024 (Guo et al.)  
- 问题：如何在低级视觉任务中用线性复杂度的状态空间模型（SSM）建模长程依赖，同时克服 SSM 在局部像素保持与通道冗余方面的劣势。  
- 方法：基于选择性结构 SSM（Mamba），提出 MambaIR：在原始 Mamba 上加入局部增强（利用局部像素相似性）与通道注意力以减少通道冗余，形成适用于图像超分、去噪等任务的简单基线。  
- 实验结论：作者在超分等任务上报告在与 SwinIR 等方法相近计算成本下取得更高 PSNR（文中示例声称超出 SwinIR 多达 ~0.45 dB），并展示更广的有效感受野可视化。详见 ECCV 摘要与代码。[chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/99851) 。  

2) FourierMamba / 频域 + SSM（arXiv / 预印本与后续实现讨论）  
- 问题：雨条纹与某些退化在频域呈现周期/方向性特征，如何在频域中高效关联不同频率以增强去雨/去条纹能力。  
- 方法：将 Mamba / 选择性 SSM 的序列扫描思想引入傅里叶域，设计空间维度的 Z 字形扫描与通道维度的 Mamba 频率关联模块，分别在傅里叶空间的幅度/相位上进行处理并与空间分支融合，形成多尺度 U‑net 风格的恢复结构。  
- 实验结论：在去雨任务的合成与真实数据上，作者报告相较于若干频域或时域基线有定量/定性提升，指出在频域进行有序扫描能增强频率间的互补利用（详见预印本）。[blog.csdn.net](https://blog.csdn.net/qq_42722197/article/details/145314007) 。  

C. 卷积内核与注意力混合（在 Transformer / 注意力结构中内嵌卷积核以兼顾局部与长程）  
1) Restormer — Efficient Transformer for High‑Resolution Image Restoration (Zamir et al., CVPR 2022)  
- 问题：如何将 Transformer 的远程依赖建模能力用于高分辨率图像复原而避免平方级复杂度。  
- 方法：提出 MDTA（Multi‑Dconv Head Transposed Attention）和 GDFN（Gated‑Dconv Feed‑Forward Network），即在注意力与前馈模块中用深度卷积（小核）进行局部上下文富集，并将注意力计算转置到通道维度以达成线性空间复杂度。  
- 实验结论：在图像去噪、去模糊、去雨等多个基准上实现领先或竞争的结果，且在高分辨率输入下保持可行的计算代价；消融显示 Dconv 与门控机制对性能和稳定性均有显著贡献。[cloud.tencent.cn](https://cloud.tencent.cn/developer/article/2398294?policyId=1003) 。  

2) 结合 CNN 大核思想与 Transformer 结构的混合设计（若干工作）  
- 问题：如何把大核 CNN 带来的宽感受野与 Transformer 的全局聚合能力结合，兼顾效率。  
- 方法要点：常见策略包括在 Transformer 的局部处理或 GDFN 中嵌入大尺寸或分解后的深度卷积（以低分辨率瓶颈为主），或在 Transformer 层与 CNN 层并行/串联融合以利用两者互补性。  
- 实验结论（共性）：混合结构在恢复纹理与结构一致性时优于纯 CNN/纯 Transformer 的同等计算预算版本，且局部卷积可稳定训练和提升细节表现（见 Restormer 与 OKNet 的消融）。（参见 Restormer 与 OKNet 讨论）[cloud.tencent.cn](https://cloud.tencent.cn/developer/article/2398294?policyId=1003), [blog.csdn.net](https://blog.csdn.net/a486259/article/details/142406557) 。  

D. 频域与扩散模型结合的“频域核”方法（频域注意力 / 扩散采样以恢复高频细节）  
1) SR‑FDN: Frequency‑Domain Diffusion Network for Image Detail Restoration (JEIT 2025)  
- 问题：扩散模型在超分中能生成细节，但对高频精确恢复与采样效率仍有挑战；频域信息对高频细节至关重要。  
- 方法：提出在扩散／去噪预测器中引入双分支频域注意力（并与空间分支融合）、用小波下采样替代常规下采以更好保留细节，并在损失层增加傅里叶域幅相约束以强化高频恢复。  
- 实验结论：在 DIV2K / FFHQ / CelebA 等基准上作者报告在 LPIPS、SSIM 或部分数据集的 PSNR 上优于若干扩散基线，同时在迭代数与采样时间上给出折衷分析；消融显示频域注意力与频域损失对细节恢复贡献明显。[jeit.ac.cn](https://www.jeit.ac.cn/cn/article/doi/10.11999/JEIT250224?viewType=HTML) 。  

E. 卷积/自注意力混合与退化先验耦合（融合经典先验与数据驱动核设计）  
1) “Dynamic association learning of self‑attention and convolution in image restoration” (Journal of Image and Graphics, 2024)  
- 问题：CNN（局部、平移不变）与自注意力（全局、可变权重）各有优缺，如何在复原任务中动态协同二者以兼顾效率与全局性。  
- 方法：提出多输入注意力模块（MAM）生成退化先验并据此将降质扰动消除与背景修复关联；整体采用并行的残差 Transformer 分支与编码器‑解码 CNN 分支，通过轻量混合块融合。  
- 实验结论：在去雨、低照/水下增强等任务上，相较多种代表方法在 PSNR/视觉质量上均有提升，且证实了退化先验与并行 SA/CNN 融合的有效性。[cjig.cn](https://www.cjig.cn/zh/article/doi/10.11834/jig.230323/) 。  

实验与评价总结（共性结论，非逐篇复述）  
- 有效感受野与长程建模：大核（或 SSM）设计能显著扩大“有效感受野”（ERF），对处理具有大尺度或周期性退化（离焦模糊、雨条纹、周期噪声）尤为关键；在保持参数与 FLOPs 可控的前提下（如将大核放在瓶颈、核分解或条带化）能获得稳定收益。  
- 局部细节与稳定训练：在注意力结构或大核中嵌入局部卷积（深度卷积、小核）是一条公认的工程实践——它既补偿了全局操作对局部纹理的忽视，又能提高训练稳定性（见 MDTA/GDFN、OKM 的局部分支）。  
- 频域与扩散：在复原高频细节（头发、纹理、条纹）方面，引入频域建模或在损失中加入频域约束可显著提升 LPIPS/感知质量；扩散模型在细节生成上强但采样复杂度/时间成本需权衡（采样迭代数与速度是关键瓶颈）。  
- 评测现状：多数工作仍以 PSNR/SSIM/LPIPS 为主要量化指标，并在 DIV2K、DPDD、SOTS、Snow100K、CelebA‑HQ 等数据集上做对比；跨真实/合成域泛化与混合退化下的鲁棒性仍是主要评估缺口。  
- 资源与效率权衡：报告的数值增益通常在 0.1–0.5 dB PSNR 范围（具体随任务与基线而异），但视觉/LPIPS 改善往往更明显；因此单一 PSNR 并不必然反映感知质量的提升。  

趋势与挑战（2025 年前后预测，≥3 点）  
1) 大核与 SSM/频域方法的混合将成为常态化设计  
- 预测：将更多工作把“极大核（或条带）在低分辨率瓶颈 + 状态空间/频域模块”的组合作为主干，以在不同尺度下兼顾长程依赖与高频恢复。研究将集中在如何自适应地选择“在哪些层采用何种核/SSM”以自动权衡效率与效果。  

2) 硬件友好型核分解与可分离实现成为工程重点  
- 预测：针对实际部署（移动端、嵌入式），核分解（如深度可分离、条带分解、秩约束）与量化/稀疏化将被进一步系统化，以把大核带来的理论增益转化为真实推理速度提升。  

3) 频域‑空间联合损失与可解释性将获更多关注  
- 预测：结合空间域感知损失与幅/相频域约束（以及可解释的 L2/正则化先验）会被广泛采用，以提升对高频细节的可控重建并增强可解释性；同时对频域权重的可视化解释将成为论文中常见的消融/分析项。  

4) 混合退化与无监督/鲁棒评估成为新的基准要求  
- 预测：真实场景通常存在混合退化（噪声+模糊+雨/雾），因此未来工作将侧重于在无/弱监督设定或单幅图像下分离多种退化并进行联合复原；对应的评测协议与数据集也会更强调多退化/域转移性能。  

5) 理论与初始化问题（大核/SSM 的可训练性）成研究瓶颈  
- 预测：如何为极大核或 SSM 提供稳定的参数化与初始化（防止训练时梯度/范数问题）将成为活跃研究方向，理论分析（如 ERF 的量化、频率响应分析）会被更多关注以指导工程设计。  

结论  
- 2022–2025 年间，基于“核”思想的图像复原方法（大核 CNN、SSM/Mamba、在注意力中嵌入卷积核、频域扩散）形成多条并行且互补的发展线索。  
- 实践经验表明：扩大有效感受野、在 Transformer/注意力中保留局部卷积、利用频域约束恢复高频细节以及在瓶颈层部署大核是目前最有效的工程化策略。  
- 未来工作需在提高泛化/鲁棒性、降低部署成本、并通过理论分析指导核设计之间取得平衡。  

参考文献（按文中引用顺序与便于检索的公开链接）  
- MambaIR: A Simple Baseline for Image Restoration with State‑Space Model (ECCV 2024) — Hang Guo et al.（论文/摘要与讨论）[chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/99851)。  
- Dynamic association learning of self‑attention and convolution in image restoration (J. Image & Graphics, 2024) — Jiang Kui et al.（期刊文章）[cjig.cn](https://www.cjig.cn/zh/article/doi/10.11834/jig.230323/)。  
- Omni‑Kernel Network for Image Restoration (AAAI/2024 解读与实现说明) — OKNet / Omni‑Kernel Module（论文解读）[blog.csdn.net](https://blog.csdn.net/a486259/article/details/142406557)。  
- Omn i‑Kernel Network 及 OKM 的详细博客与实现说明（论文阅读、消融）[blog.csdn.net](https://blog.csdn.net/a486259/article/details/142406557)（同上，含消融细节）。  
- Restormer: Efficient Transformer for High‑Resolution Image Restoration (CVPR 2022) — Zamir et al.; 方法与实验证明（综述/讲解）[cloud.tencent.cn](https://cloud.tencent.cn/developer/article/2398294?policyId=1003) 。  
- FourierMamba: Fourier Learning Integration with State Space Models for Image Deraining (arXiv / 预印本与解读) — Dong Li et al.（方法综述）[blog.csdn.net](https://blog.csdn.net/qq_42722197/article/details/145314007) 。  
- SR‑FDN: A Frequency‑Domain Diffusion Network for Image Detail Restoration (Journal of Electronics & Information Technology, 2025) — Li Xiumei et al.（期刊论文）[jeit.ac.cn](https://www.jeit.ac.cn/cn/article/doi/10.11999/JEIT250224?viewType=HTML) 。  
- L2‑norm prior 的可解释性深度学习图像复原算法（Laser & Optoelectronics Progress, 2025）— Bu et al.（方法与可解释性讨论）[opticsjournal.net](https://www.opticsjournal.net/Articles/OJ3c8a4a3f8eb7002f/Abstract) 。  
- Image Inpainting Networks with Multi‑Source Feature Encoding (Modeling & Simulation, 2024) — Wang et al.（修复与注意力/ViT 混合）[image.hanspub.org](https://image.hanspub.org/Html/17-2571417_82580.htm) 。  
- Unsupervised Hybrid‑Distorted Image Restoration Method Based on Feature Disentangled Representation Learning (JCAD, 2024) — Fu Ying et al.（无监督混合失真复原）[jcad.cn](https://www.jcad.cn/cn/article/doi/10.3724/SP.J.1089.2024.19717) 。  
- Physics‑Based Generative Adversarial Models for Image Restoration and Beyond（论文解读/实现细节博客）— 解读文章（CV/图像复原中物理约束 GAN 思路）[blog.csdn.net](https://blog.csdn.net/yangqoor/article/details/148351268) 。  
- 论文/方法比较与实现细节（Omni/全核与 SSM 交叉讨论等实现解读合集）[blog.csdn.net](https://blog.csdn.net/qq_42722197/article/details/145314007)（FourierMamba 与 Mamba 家族相关讨论）。  

（注：上述参考条目均对应公开可查的论文/期刊条目或会议论文解读页；文内对具体数值／结论之引用均依据相应论文/官方摘要或作者公开报告的实验结果。为便于读者进一步阅读，我在参考中保留了可访问的综述/期刊页面链接。）  

若需要，我可以基于上述分类为每一类再给出更详细的实验对比表（数据集、基线、PSNR/SSIM/LPIPS 列表）并标注来自各篇论文的具体数值与计算预算（FLOPs / 参数 /推理时间）。