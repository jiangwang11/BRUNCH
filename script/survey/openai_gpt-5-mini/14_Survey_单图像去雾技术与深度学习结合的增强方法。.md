引言  
单幅图像去雾（single-image dehazing）仍是计算机视觉中的典型病态逆问题：观测 I(x) = J(x)t(x)+A(1−t(x)) 中未知量多、数据域差异大、真实雾像标注稀缺。自 2022 年以来，三条主要研究路线明显加速：一是将高容量的 Transformer /高效自注意力用于端到端恢复以提升高分辨率与远程依赖建模；二是放弃或弱化成对监督，采用非配对/自监督/物理约束方法以缩小合成→真实的域差；三是引入生成式建模（GAN / 扩散 / 物理约束 GAN）与合成-微调策略，改善视觉保真与下游任务鲁棒性。下文在方法分类下按每类 3–5 篇代表作逐一简述（每篇 4–6 句，突出问题、方法与定量结论），随后给出实验/评估的共性结论与 2025 年前后的趋势预测。为便于读者查核，文末列出主要原始论文（顶会 / 顶刊 / arXiv）。

方法分类与代表作
A. 监督端到端与 Transformer 驱动的高质量恢复（3 篇）
- Restormer — Zamir et al., CVPR 2022.  
  研究问题：高分辨率图像恢复中，如何用注意力既高效又能捕捉长程依赖。  
  核心方法：提出基于通道交互的高效 Transformer（Restormer）模块，结合局部卷积与全局注意力，设计用于图像去噪、去雨与其他恢复任务的骨干。  
  关键实验结论：在多项高分辨率恢复任务（含去雾相关基线）上，Restormer 在 PSNR/SSIM 与感知质量之间给出更优的权衡，同时在每像素 FLOPs 与显存使用上优于同等性能的标准 Transformer。  
  （原文：Restormer CVPR2022）

- Uformer — Wang et al., CVPR 2022.  
  研究问题：如何在 U-Net 架构中引入 Transformer 以保持多尺度信息同时扩展感受野。  
  核心方法：将窗口/跨窗口自注意力与 U 形编码器—解码器结合，使用可逆/分层注意力以控制计算开销，适配到图像复原场景。  
  关键实验结论：在多个恢复基准（包括合成去雾子任务）中，Uformer 在细节恢复和结构保真上超越仅用 CNN 的网络，并且在大分辨率输入上更稳定。  
  （原文：Uformer CVPR2022）

- Vision transformers for single image dehazing — Song et al., IEEE TIP 2023.  
  研究问题：直接将 ViT 家族用于单幅去雾时，如何引入透射率/位置先验以避免细节缺失。  
  核心方法：在 Transformer 框架中加入透射率感知的位置嵌入与专门的细节保留分支，兼顾全局传输估计与局部高频恢复。  
  关键实验结论：与传统 CNN/混合模型相比，该方法在 SOTS 等合成测试上提高了结构相似度（SSIM）并减少了天空/高亮区域的伪影，但对真实域（RTTS）仍需域适配策略配合。  
  （参见：TIP2023 相关工作；方法体现了 2022 年后 Transformer 在去雾中的落地方向）

B. 非配对 / 无监督 / 物理分解（3 篇）
- D4 (Self‑Augmented Unpaired Image Dehazing via Density and Depth Decomposition) — Yang et al., CVPR 2022.  
  研究问题：如何用非成对（unpaired）数据训练去雾网络并保持物理一致性与泛化能力。  
  核心方法：将透射图分解为雾密度（scattering coefficient β）与场景深度两部分；设计去雾—增雾的自增强循环结构，通过深度估计伪监督和可控重渲染生成多厚度雾样本以提升训练鲁棒性。  
  关键实验结论：在无成对训练设置下，D4 在合成与多种真实数据集上均优于传统 CycleGAN 型非配对方法，证明了基于物理分解的自增强策略能有效缩小域差。[hub.baai.ac.cn](https://hub.baai.ac.cn/view/17272)

- Cycle‑Dehaze (enhanced CycleGAN) — Engin et al., CVPRW 2018.  
  研究问题：用非配对图像实现去雾时如何通过对抗训练保持循环一致性与视觉真实度。  
  核心方法：在 CycleGAN 框架上增加感知损失与循环结构的任务定制化（例如传输一致性），以便在无配对数据下训练去雾与增雾生成器。  
  关键实验结论：在无配对设置上能恢复部分细节，但由于忽略了物理成像特性，常在深度相关场景产生不稳定的传输估计，提示需结合物理约束或深度监督。

- Deep‑DCP (Unsupervised DCP‑loss) — Golts, Freedman & Elad, IEEE TIP 2020.  
  研究问题：如何在无监督框架下利用经典暗通道先验 (DCP) 提供可训练监督信号。  
  核心方法：以暗通道先验构造无监督损失（DCP‑loss）并将其纳入端到端 CAN（context aggregation network），不直接依赖配对清晰图像。  
  关键实验结论：在缺乏配对数据的现实场景中，DCP‑loss 能引导网络学习更稳定的透射估计，改进对天空和稀疏纹理区域的处理，但仍受限于先验在特殊场景（如高亮/低饱和）下失效的问题。  

C. 半监督 / 合成→真实迁移（3 篇）
- PSD (Principled Synthetic‑to‑Real Dehazing Guided by Physical Priors) — Chen et al., CVPR 2021.  
  研究问题：合成对训练的去雾模型在真实世界上泛化差；如何将物理先验作为桥接使合成→真实迁移更稳健。  
  核心方法：结合物理先验与合成-真实协同学习，设计物理兼容头与大气光估计子网，在合成有标签数据上预训练并在真实无标签上以物理正则微调。  
  关键实验结论：PSD 在无参考质量指标与主观视觉评价上均优于直接从合成数据训练的基线，且对下游检测/分割任务的性能下降抑制更明显。

- Semi‑Supervised Image Dehazing — Li et al., IEEE TIP 2020.  
  研究问题：在标注稀缺的现实场景下，如何用少量配对数据＋大量未配对数据训练去雾模型。  
  核心方法：两分支半监督框架（监督分支与无监督分支），使用暗通道损失、总变差等无监督约束与像素级监督结合，并以增强样本缓解真实域稀缺。  
  关键实验结论：在 SOTS/RTTS 等数据上证明半监督训练能显著提高真实图像的视觉质量与 SSIM，表明混合损失与增强策略能缓解域差。

- 合成数据集与基准（背景） — Li et al., "Benchmarking Single‑Image Dehazing and Beyond", IEEE TIP 2019 (RESIDE).  
  研究问题：去雾研究缺乏统一评测与合成→真实评估分离的基准。  
  核心贡献：构建 RESIDE 等合成/真实混合基准、定义多类测试切分与评价协议，为之后的半监督与迁移学习工作提供标准化评测。  
  关键结论：基于合成配对训练的模型在合成测试集上得分高但在真实测试集上性能急剧下降，明确了域差问题的严峻性。  

D. 生成式 / 多任务与物理约束生成模型（3 篇 / 方向性代表）
- TransWeather — Valanarasu et al., CVPR 2022.  
  研究问题：设计一个通用模型处理一系列恶劣天气（雾、雨、雪）下的图像恢复，而不是为单一任务设计专门网络。  
  核心方法：提出基于 Transformer 的单网络多任务恢复框架，利用任务条件嵌入与自适应注意力实现对不同天气退化建模与修复。  
  关键实验结论：在多种天气恢复基准上（含合成去雾场景），统一模型可与或超越专门方法，且模型迁移至真实场景时更稳定，说明多任务学习有助于学习更通用的低级视觉表征。

- Physics‑Constrained GANs / GAN 融合物理约束（代表性思路）  
  研究问题：标准 GAN 可生成视觉上逼真的恢复结果，但往往违反退化物理一致性（例如重构后再退化不匹配观测）。  
  核心方法（代表性工作方向）：在生成器-判别器框架中嵌入物理退化算子 H(·) 并设计额外判别器去判别经物理退化后的重构是否与原观测一致，从而同时保证视觉质量与物理一致性（详见若干论文与综述）。  
  关键实验结论：物理约束显著减少了感知—失真冲突带来的伪影，在去雾等场景中提高了可重构性与下游任务的可靠性（更多方法与综述见 2025 年生成式去雾综述）。（生成式综述参见[arocmag.cn](https://www.arocmag.cn/abs/2025.06.0198)）

- 扩散模型与条件扩散在图像复原的初步尝试（方向性，2023–2025 活跃）  
  研究问题：扩散模型能否取代或补充 GAN/条件网络以获得更高保真且更稳定的恢复？  
  核心方法（代表作分布在图像恢复领域）：将条件扩散（conditioning on degraded image and/or estimated depth/transmission）应用于去雾/去雨等任务，配合物理约束改善重建一致性。  
  关键实验结论（早期工作）：扩散模型在感知质量上显示出潜力，但推理开销与对条件信息（深度/透射）依赖使得实际部署仍需架构与加速优化。相关综述/趋势见 2025 年文献回顾。  

实验与评价总结（只总结共性结论）
- 数据与指标：研究普遍采用 RESIDE（SOTS）、I‑HAZE/O‑HAZE、NH‑HAZE、RTTS 等数据集并以 PSNR / SSIM 作主客观对齐，近年更多论文同时报告感知性指标（LPIPS）与下游任务（检测/分割）表现作为实用性评估。RESIDE‑类合成集仍是方法优化首要平台，但对真实图像（RTTS、BeDDE 等）的泛化才是关键瓶颈。[pdf.hanspub.org](https://pdf.hanspub.org/jisp2025141_32670393.pdf)列出常用数据集与指标。  
- 合成→真实域差（domain gap）是最普遍的实验结论：在合成上取得最高 PSNR/SSIM 的模型往往在真实集上退化明显，因此必须引入非配对训练、物理先验或半监督策略以缓解。多篇工作（PSD、D4、半监督方法）均通过结合物理模型或基于深度的伪监督显著缩小该差距。  
- 感知—失真权衡：Transformer 与扩散/GAN 类方法在主观/感知质量上倾向优于仅以 MSE 为优化目标的 CNN，但可能牺牲 PSNR。物理一致性约束与透明的重建损失（重建→退化一致）能同时改善感知与失真两端的折中。  
- 计算代价与分辨率：Transformer‑based 恢复（Restormer/Uformer）在高分辨率输入上表现优越，但对计算与显存友好性的改进仍是工程关键。4K 级别的去雾方法需专门设计多引导/双边网格策略以降低计算（参见 4kDehazing）。  
- 下游任务影响：越来越多工作直接在目标检测 / 语义分割等下游任务上评估去雾的实用价值，结论是“视觉上更清晰的不一定能提升下游任务准确率”——只有在恢复同时保留语义一致性的方案（物理兼容与对抗判别）才能稳定改善下游性能。

趋势与挑战（针对 2025 年前后预测，至少三点）
1) 混合物理—生成范式成为主流：未来 2–3 年内，单纯端到端的黑箱恢复将逐步让位于“生成模型 + 明确物理约束”的混合范式（例如物理约束的条件扩散或双判别 GAN），因为该范式同时满足视觉保真与可重构性（physics‑consistent）两项关键需求。参见物理约束 GAN 理念与 2025 年生成综述[arocmag.cn](https://www.arocmag.cn/abs/2025.06.0198)。

2) 非配对自监督与深度伪监督将成为现实域泛化的常规做法：D4 等在 CVPR2022 展示的“密度—深度分解 + 重渲染”自增强思路有望扩展，结合合成样本合成策略与真实无配对图像的伪监督将成为工业级去雾流水线的标配（更少依赖人工配对标签）。相关非配对与半监督方法的效果已被多篇工作证实（参见 D4、PSD、Li‑Semi）。

3) 扩散模型与可控生成在去雾中的实际落地：扩散模型在感知质量上优势明显，预计会在 2025 年后被更多实验用于条件去雾（以深度/透射图为条件）；但要解决的两大问题是推理速度（需蒸馏/加速）和条件信息的不确定性（需物理约束或学得的条件解码器）。

4) 任务感知去雾（task‑aware dehazing）：去雾不再只是为了视觉好看，更多研究将以“对检测/分割/重建有利”为目标去设计损失与评估指标（联合训练或任务约束），这会促使去雾模型在下游任务上具有可量化收益（已有工作已开始采用此评估范式）。

5) 资源/部署导向的轻量化 Transformer 与可解释性：在移动/自动驾驶等场景中，轻量化的 Transformer（或混合 CNN‑Transformer）同时配备物理可解释模块（例如显式透射估计头）将成为主流，以便满足实时性与可审计性的行业要求（参见 Restormer/Uformer 的架构演进）。

结论  
2022–2025 年的研究显示：单幅去雾正从“追求合成集高分”向“同时满足真实泛化、物理一致性与下游任务效用”转变。代表性的方向包括 Transformer 驱动的高质量恢复、基于物理分解的无配对/自增强训练、以及以物理约束为核心的生成式方法（GAN/扩散）。未来工作需聚焦（1）可验证的物理一致性约束；（2）合成→真实的可控迁移策略；（3）在保证实时性的前提下用生成模型提升感知质量并服务下游视觉任务。

参考文献（所列为原始论文／权威基准或会议论文，按出现顺序；为便于检索，括注会议/年份）
- Yang Y., Wang C., Liu R., Zhang L., Guo X., Tao D. Self‑Augmented Unpaired Image Dehazing via Density and Depth Decomposition. CVPR 2022. [hub.baai.ac.cn](https://hub.baai.ac.cn/view/17272)  
- Valanarasu J.M.J., Yasarla R., Patel V.M. TransWeather: Transformer‑based restoration of images degraded by adverse weather conditions. CVPR 2022.  
- Zamir S.W., Arora A., Khan S., et al. Restormer: Efficient Transformer for High‑Resolution Image Restoration. CVPR 2022.  
- Wang Z., Cun X., Bao J., et al. Uformer: A General U‑shaped Transformer for Image Restoration. CVPR 2022.  
- Song Y., He Z., Qian H., et al. Vision transformers for single image dehazing. IEEE Transactions on Image Processing, 2023.  
- Chen Z., Wang Y., Yang Y., Liu D. PSD: Principled Synthetic‑to‑Real Dehazing Guided by Physical Priors. CVPR 2021.  
- Li L., Dong Y., Ren W., Pan J., Gao C., Sang N., et al. Semi‑Supervised Image Dehazing. IEEE Transactions on Image Processing, 2020.  
- Li B., Ren W., Fu D., Tao D., Feng D., Zeng W., et al. Benchmarking Single‑Image Dehazing and Beyond (RESIDE). IEEE Transactions on Image Processing, 2019.  
- Engin D., Genc A., Ekenel H.K. Cycle‑Dehaze: Enhanced CycleGAN for Single Image Dehazing. CVPR Workshops 2018.  
- Golts A., Freedman D., Elad M. Unsupervised Single Image Dehazing Using Dark Channel Prior Loss. IEEE Transactions on Image Processing, 2020.  
- Cai B., Xu X., Jia K., Qing C., Tao D. DehazeNet: An End‑to‑End System for Single Image Haze Removal. IEEE Transactions on Image Processing, 2016.  
- Liu X., Ma Y., Shi Z., Chen J. GridDehazeNet: Attention‑Based Multi‑Scale Network for Image Dehazing. ICCV 2019.  
- Qin X., Wang Z., Bai Y., et al. FFA‑Net: Feature Fusion Attention Network for Single Image Dehazing. AAAI 2020.  
- Zheng Z., Ren W., Cao X., Hu X., Wang T., Song F., et al. Ultra‑High‑Definition Image Dehazing via Multi‑Guided Bilateral Learning. CVPR 2021 (4kDehazing).  
- Berman D., Treibitz T., Avidan S. Non‑Local Image Dehazing. CVPR 2016 / TPAMI 2020.  
- Engin D. et al. (Supplementary review / datasets) — I‑HAZE / O‑HAZE dataset papers (Ancuti et al., 2018) cited in community benchmarks.  
- 《基于深度学习的图像去雾研究综述》— Ji & Lu, 2025 (综述；数据集与指标汇总) [pdf.hanspub.org](https://pdf.hanspub.org/jisp2025141_32670393.pdf)  
- 曹倩雯、李恭如. 单幅图像去雾的生成式方法研究现状 (生成式综述，优先出版 2025). [arocmag.cn](https://www.arocmag.cn/abs/2025.06.0198)  

（注：本文主体对各代表工作之技术与结论基于其原始会议/期刊论文；同时参照了近年综述与数据集整理以保证实验结论的共性总结，例见上两项综述链接。）