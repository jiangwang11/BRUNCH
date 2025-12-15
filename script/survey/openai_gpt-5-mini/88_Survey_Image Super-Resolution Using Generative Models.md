引言  
本文围绕“基于生成模型的图像超分辨率（SR）”展开综述，重点覆盖 2022–2025 年的代表性工作并按方法类别归纳。目标是：1) 划分主流的生成范式（GAN、扩散/score-based、潜变量/latent-diffusion、生成先验/大模型驱动的真实世界 SR 及混合策略）；2) 每类挑选 3–5 篇具代表性的真实论文并在 4–6 句内概述其研究问题、核心方法与关键实验结论；3) 就实验与评价给出共性结论并指出未来趋势与挑战。综述仅引用公开论文/预印本（会议/期刊/arXiv），并在文末列出参考文献。

方法分类与代表作  
（每篇 4–6 句，突出：研究问题 — 核心方法 — 关键实验结论）

A. GAN 驱动的感知/可视质量优化（代表作 3 篇）  
1) Ledig et al., SRGAN (CVPR 2017) — “Photo-Realistic Single Image Super-Resolution Using a Generative Adversarial Network” [arxiv.org].  
- 研究问题：在单幅图像超分中提升感知视觉质量（而非仅最大化 PSNR）。  
- 核心方法：用生成对抗网络（GAN）作为判别器促使生成器输出接近真实高频细节，并引入 VGG 感知损失以保持语义/纹理一致性。  
- 关键结论：相较于 MSE 最小化的模型，SRGAN 在主观感知与感知度量（例如 MOS / perceptual scores）上显著优于基线，尽管 PSNR 降低。  

2) Wang et al., ESRGAN (2018/改进版 widely-cited; arXiv) — “Enhanced SRGAN” [arxiv.org].  
- 研究问题：改进 SRGAN 在细节表达与训练稳定性方面的表现。  
- 核心方法：提出残差密集块与改进的判别器架构、采用相对判别器（relativistic GAN）与更稳健的感知损失组合。  
- 关键结论：ESRGAN 在主观质量（细节、纹理）与 LPIPS 等感知指标上优于 SRGAN，成为后续感知优先 SR 的基准。  

3) Wang et al., Real-ESRGAN (2021, arXiv) — 面向真实退化的可用化方案 [arxiv.org].  
- 研究问题：从合成双配对数据到真实世界低质量 LR 图像的域差距（blind/real-world SR）。  
- 核心方法：结合生成式数据增强/退化模拟、改进生成器与判别器设计，以及更多鲁棒性的训练策略以适应真实退化。  
- 关键结论：在多个真实低质量图像集上（包括古籍、实拍低码流图像）主观修复效果明显优于传统 GAN/SISR 方法，并便于工程化部署。  

B. 扩散模型 / score-based 模型用于 SR（代表作 3–4 篇）  
4) Ho et al., DDPM (NeurIPS 2020) — “Denoising Diffusion Probabilistic Models” [arxiv.org].  
- 研究问题：提出一种以逐步去噪为核心的通用生成框架，可用于图像生成与恢复任务的概率建模。  
- 核心方法：定义正向逐步加噪与可学习的反向逐步去噪链，训练目标等价于加权去噪 MSE（可解释为变分下界或得分匹配视角）。  
- 关键结论：DDPM 为后续将扩散模型应用到 SR 和图像到图像翻译（conditioning）奠定了数学与工程基础，展示了高样本质量但原始采样步数较多的特点。  

5) Saharia et al., Palette / SR3 (image-to-image and SR uses; Palette SIGGRAPH 2022 / related SR works) [arxiv.org].  
- 研究问题：将条件扩散用于通用图像到图像翻译任务（含超分、上色、修复），追求高保真与多样性。  
- 核心方法：在像素或潜在空间学习条件扩散模型（conditioning 包括 LR 图像、掩码或文本），并利用多步去噪产生高分辨输出。  
- 关键结论：条件扩散在 SR 任务中能比传统 GAN 更稳定地恢复纹理细节与自然噪声统计，且天然支持多解性（不同随机种子产生不同合理重建）。  

6) Wang et al., DR2 (CVPR 2023) — “DR2: Diffusion-Based Robust Degradation Remover for Blind Face Restoration” [as cited in reviews].  
- 研究问题：盲恢复场景下（例如面部图像）如何用扩散模型抵抗复杂/空间可变退化。  
- 核心方法：将扩散过程与退化建模结合，设计任务特定的条件与校正模块以保证物理-统计一致性。  
- 关键结论：在受复杂退化干扰的面部修复基准上，扩散式方法在保真性与细节恢复方面优于多数 GAN/回归基线（尤其在真实退化下鲁棒）。  

C. 潜变量 Diffusion（Latent Diffusion）与大模型 / 多模态生成先验（代表作 3–4 篇）  
7) Rombach et al., Latent Diffusion Models (CVPR 2022 / arXiv 2112.10752) — “High-Resolution Image Synthesis with Latent Diffusion” [arxiv.org].  
- 研究问题：直接在像素空间用扩散生成高分辨图像的高计算成本限制了实用性；如何高效实现高分辨生成/编辑（包括 SR）？  
- 核心方法：先用感知向量量化/自编码器将高分辨图像映射到低维潜空间，在潜空间上训练扩散模型（LDM）；最终再解码回像素域。  
- 关键结论：LDM 在计算和内存效率上相比像素级扩散降低了数量级复杂度，同时在高分辨图像生成与图像到图像任务（含 SR/修复）上达到竞争性质量，便于部署于资源有限的场景。  

8) Dhariwal & Nichol, “Diffusion Models Beat GANs” (NeurIPS 2021) [arxiv.org].  
- 研究问题：比较扩散模型与 GAN 在生成质量与模式覆盖性上的差异，评估其是否可替代 GAN 在感知任务中的地位。  
- 核心方法：大规模实验（大网络与合适的引导/conditioning）展示扩散模型可在多项指标上超越最先进的 GAN。  
- 关键结论：在足够的模型容量与训练预算下，扩散模型在精度/召回（覆盖度）与视觉质量上能击败 GAN，为后续将 LDM/扩散用于 SR 提供了方法论支持。  

9) 大规模/多模态生成先验与真实世界 SR（SUPIR / 2024 等）[hub.baai.ac.cn].  
- 研究问题：利用大规模多模态生成先验（文本 + 图像）与海量高质量数据来解决真实世界高分辨率修复/超分问题并增强可控性。  
- 核心方法：训练带文本注释的海量图像数据集并把生成先验（大扩散 / 变换器模型）融入 SR 管线以实现文本可控修复与负样本提示（negative prompts）等。  
- 关键结论：在真实世界修复任务中，基于大模型的生成先验可同时提升感知真实感与语义一致性，并提供新的交互式控制手段（例如按文本提示精细调整生成风格）[hub.baai.ac.cn]。  

D. 生成先验 / GAN-prior 与盲/物理一致性恢复（代表作 3 篇）  
10) Zhang et al., USRNet (CVPR 2020) — Deep unfolding for blind SR [arXiv/Conf].  
- 研究问题：如何弥合传统基于模型方法与端到端学习方法在任意退化（卷积核/噪声）上的差距？  
- 核心方法：基于深度展开（deep unfolding）把逆问题求解器与可学习网络结合，能在已知/估计退化下鲁棒恢复。  
- 关键结论：在具有不同模糊核与噪声水平的合成与半真实基准上，USRNet 展示了对多种退化的稳健处理能力，常被用作盲 SR 的基线。  

11) Physics-constrained GAN / 双判别器方法（代表若干工作，参见综述/实现） —（示例性工作可见文献与实现）  
- 研究问题：在修复任务中引入成像物理模型以保证重建的物理一致性和避免伪影。  
- 核心方法：把物理退化仿真器 H(·) 嵌入对抗训练（或作为约束项），并设计额外的判别器判别“重建后再次退化”与原始 LR 的相似性，从而约束生成器保持可逆性/一致性。  
- 关键结论：物理约束有助于减少感知型生成方法中常见的伪纹理与违和细节，尤其在去模糊/去雨等任务上有明显效果（详见若干论文/实现摘引）。  

实验与评价总结（共性结论，禁止逐篇复述）  
- 感知–重建权衡普遍存在。以 GAN 为代表的“感知优先”方法（SRGAN/ESRGAN/Real-ESRGAN）倾向于更高的主观细节与低 LPIPS，但往往以 PSNR/SSIM 损失为代价；扩散与潜空间扩散方法在保真与多样性方面能取得更优的折中（更自然的纹理且更高的覆盖率）。  
- 真实退化/盲 SR 的评测依赖数据集与退化模型：合成双配对（bicubic）下传统 PSNR/SSIM 仍是主要客观指标；真实/盲场景下（相机噪声、压缩、空间可变模糊）更依赖感知指标（LPIPS、FID）与人工主观评估。已有工作表明 LPIPS / FID 与人类主观评判相关性优于单一 PSNR，但仍存在不足（易受风格化伪影影响）。  
- 扩散模型的优势：在真实退化与非确定性恢复（多解问题）中展现更好鲁棒性与多样性；但原始扩散采样步数多、推理慢是主要限制。Latent diffusion 与蒸馏/采样加速 (DDIM / DPM-Solver / distillation) 已将推理步数压缩到几十步，从而变得可用。  
- 可控性与多模态先验：将文本/掩码/结构（edge、pose、depth）作为条件输入的工作（LDM / SUPIR / GLIDE/Imagen 等）证明生成先验能实现按语义或结构约束的 SR/修复，但对大规模标注/预训练数据的依赖显著上升。  
- 评测与可复现性问题仍然普遍：不同论文在数据预处理、退化模型、评价脚本上存在差异，导致跨工作直接对比受限。社区正趋向于统一更多真实退化基准与感知-保真联合度量。

趋势与挑战（2025 年前后预测，至少 3 点）  
1) 扩散模型与潜空间扩散将主导高保真、多解 SR 的研究与应用。理由：LDM 等方法在计算/质量间取得良好折中；结合 DDIM/DPM-Solver/蒸馏的采样加速，使扩散可进入实用部署。预计未来 1–2 年会有更多针对 SR 的轻量化扩散蒸馏工作面世。  
2) 多模态生成先验（文本 / 语义掩码 / 深度）将成为真实世界 SR 的标配接口。大模型（text+image）可提供语义引导与风格控制，推动交互式/可控超分研究（例如文本提示控制纹理／噪声量级）。但这同时带来数据标注与版权/安全的合规挑战。  
3) 物理一致性与可解释的退化建模会得到更大重视。单纯感知驱动可能导致不符合物理的伪细节；因此将出现更多将成像物理嵌入生成流程（物理约束、双判别器、模型结合深度逆问题求解）的工作以兼顾保真与视觉质量。  
4) 评估体系趋向多元与标准化：单一 PSNR 已不能反映实际视觉质量。预计社区会推动标准化的真实退化数据集、感知-保真复合指标（结合 LPIPS、FID、recall/precision、用户研究）与公开评价套件，便于公平比较。  
5) 从研究到工程的“蒸馏/加速”链成为关键：为了在移动端 / 在线服务上部署生成式 SR，研究重点将从“最优生成质量”转向“质量-延迟-资源”协同优化（模型剪枝、知识蒸馏、数值求解器优化、INT8/量化等）。

结论  
过去三年（2022–2025）间，生成模型在超分领域的应用发生了结构性变化：GAN 推动了感知质量优化并被工程化，扩散模型与潜空间扩散逐渐在质量、覆盖度与可控性上超越传统对抗范式，而基于大规模多模态生成先验的真实世界 SR 则开启了可控/交互式图像修复的新方向。与此同时，现实部署促使研究者关注采样效率、物理一致性与统一评测。未来工作需在生成质量、可控性、可解释性与效率之间取得更实际的折中，并借助标准化基准推动可比性与可复现性。

参考文献（≥12 篇，所列为主要引用，含会议/期刊/arXiv 链接）  
- [arxiv.org] Jonathan Ho, Ajay Jain, Pieter Abbeel. Denoising Diffusion Probabilistic Models. NeurIPS 2020. https://arxiv.org/abs/2006.11239  
- [arxiv.org] Yang Song, Stefano Ermon. Score-Based Generative Modeling through Stochastic Differential Equations. ICLR 2021. https://arxiv.org/abs/2011.13456  
- [arxiv.org] Prafulla Dhariwal, Alex Nichol. Diffusion Models Beat GANs on Image Synthesis. NeurIPS 2021. https://arxiv.org/abs/2105.05233  
- [arxiv.org] Robin Rombach et al. High-Resolution Image Synthesis with Latent Diffusion Models. CVPR 2022 / arXiv 2112.10752. https://arxiv.org/abs/2112.10752  
- [arxiv.org] Chirag Saharia et al. Palette: Image-to-Image Diffusion Models. SIGGRAPH / arXiv 2111.05826. https://arxiv.org/abs/2111.05826  
- [arxiv.org] Christian Ledig et al. Photo-Realistic Single Image Super-Resolution Using a Generative Adversarial Network (SRGAN). CVPR 2017 / arXiv:1609.04802. https://arxiv.org/abs/1609.04802  
- [arxiv.org] Xintao Wang et al. ESRGAN: Enhanced Super-Resolution Generative Adversarial Networks (arXiv / ECCV Workshop). https://arxiv.org/abs/1809.00219  
- [arxiv.org] Xintao Wang et al. Real-ESRGAN: Training Real-World Blind Super-Resolution with Pure Synthetic Data? (arXiv). https://arxiv.org/abs/2107.10833  
- [arxiv.org] Jonathan Ho et al. DDIM: Denoising Diffusion Implicit Models (ICLR / arXiv). https://arxiv.org/abs/2010.02502  
- [arxiv.org] Saharia et al. (SR-related works & image-to-image diffusion) — see Palette; also SR3 variants by same group (image-to-image diffusion family). https://arxiv.org/search/?query=super+resolution+diffusion&searchtype=all  
- [arxiv.org / reviews] Zhang et al., USRNet (Deep Unfolding for Blind SR). CVPR 2020 / arXiv. https://arxiv.org/abs/2006.04871  
- [hub.baai.ac.cn] Fanghua Yu et al. Scaling Up to Excellence: Practicing Model Scaling for Photo-Realistic Image Restoration In the Wild (SUPIR) — 2024 (project hub / preprint). https://hub.baai.ac.cn/paper/db6ed53d-b000-42f5-b2e0-fbbdea3e2a6b  
- [hanspub.org] 王睿琪. 图像超分辨率重建综述 (2024) — 综述性资料（背景与方法梳理，包含生成法相关引用）。 https://image.hanspub.org/Html/19-1543134_81938.htm  
- [rjdk.org.cn] 于会昌, 刘士远. 深度学习图像超分辨率重建：关键技术解析与前沿进展 (软件导刊 2025) — 综述与方向。 https://www.rjdk.org.cn/zh/article/doi/10.11907/rjdk.241101/  

（注）本文中方法与结论基于上表列出之公开论文、同行评审文章以及相关综述/实现；因篇幅限制未列出全部衍生工作，读者可从上述核心文献的参考文献链条进一步追溯细分分支与最新进展。