引言  
近年来，基于扩散（diffusion）概率模型的视频生成研究从单帧/短片段扩展到可控文本→视频、多镜头叙事与高分辨率生成。自 2022 年以后出现的一批工作表明：将扩散框架拓展到时空域、将扩散过程放到潜空间（latent）以节省计算、以及采用级联/蒸馏/对抗后训练以加速采样，已成为推动短视频与长视频生成质量与效率提升的三条主线。本文在 2022–2025 年发表或公开的代表性工作基础上梳理方法谱系、提炼实验共性结论，并在最后给出基于现有证据的中期（至 2025 年前后）研究趋势预测。为保证可溯源性，文中所引均为公开论文或技术报告/预印本。

方法分类与代表作  
说明：每个小节选取 3–5 篇代表性工作，按“研究问题 → 核心方法 → 关键实验结论”给出简明介绍（每篇 4–6 句）。

1. 像素空间 / 时空扩散（直接在像素或时空张量上建模）  
- Video Diffusion Models (Ho et al., NeurIPS 2022). 研究问题：将图像扩散推广到视频并同时保证帧间时序一致性与空间细节。核心方法：把 U-Net/时空 U-Net 扩展为时空去噪网络，提出图像+视频联合训练与分辨率/时序逐级扩展策略。关键结论：在 UCF-101 等基准上实现当时领先的 FVD，显示出直接在像素/时空域训练可获得连贯的短视频样本；并证明图像数据混合训练可加速收敛与改善空间保真度 [arxiv.org](https://arxiv.org/abs/2204.03458).  
- MCVD: Masked Conditional Video Diffusion (Voleti et al., NeurIPS 2022). 研究问题：统一视频生成、预测与插值三类任务的条件建模。核心方法：使用掩码条件设计，让单一扩散模型以不同掩码实现无条件/有条件/插值采样；网络采用时空 U-Net 变体与掩码编码。关键结论：单模型通过掩码条件即可覆盖多任务，插值与预测在人为控制下生成连贯过渡，证明掩码条件是视频扩散通用化的有效设计[arxiv.org](https://arxiv.org/abs/2205.09853).  
- GenTron: Diffusion Transformers for Image and Video (Chen et al., CVPR 2024). 研究问题：替换 U-Net，用 Transformer 作为扩散反向网络以增强可扩展性与条件表达。核心方法：提出基于 Transformer 的扩散骨干（DiT 风格延拓），并实证其在图像与视频条件生成上的设计要点。关键结论：在若干文本→图像/视频对比中，Transformer‑based 反向模型在视觉质量与文本对齐上具有竞争力，表明 Transformer 架构是视频扩散向大模型化转变的可行路径 [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/44761).

2. 潜空间 / 级联（VAE + Latent Diffusion / 多阶段超分）  
- Latent Diffusion Models (Rombach et al., CVPR 2022). 研究问题：像素级扩散在高分辨率下计算量大且低效。核心方法：先以感知保持的 VAE 把高分辨率图像编码到低维潜空间，在潜空间上训练扩散模型并解码回像素域；引入 cross‑attention 方便条件控制。关键结论：在相近计算预算下，潜空间扩散在 512×512 等高分辨率任务上显著降低计算并保持或提升感知质量，为后续文本→视频与视频潜空间方法打下基础 [arxiv.org](https://arxiv.org/abs/2112.10752).  
- Make‑A‑Video (Singer et al., Meta AI, 2022). 研究问题：在缺乏成对文本-视频训练数据的情况下实现文本→视频。核心方法：先用大规模图像-文本对训练强文本→图像扩散模型，再用无标注视频学习运动先验并将图像扩散扩展到视频（时空注意力 / 运动模块与分阶段超分流水线）。关键结论：通过分离静态渲染能力与运动学习，可在零或低量文本-视频数据下生成语义匹配且具有合理运动感的短视频样本[arxiv.org](https://arxiv.org/abs/2209.14792).  
- Imagen Video (Saharia et al., Google, 2022). 研究问题：把高质量文本→图像方法扩展为高分辨率文本→视频。核心方法：采用级联视频扩散（先低分辨率时间骨架再逐级空间/时间超分）、强文本编码（T5）与 classifier‑free guidance；并使用渐进式蒸馏以加速采样。关键结论：能生成长达数秒、128 帧级别且在视觉细节与文本对齐上明显领先此前工作，证明级联时空超分是生成高分辨率视频的有效范式[arxiv.org](https://arxiv.org/abs/2210.02303).

3. 可控/编辑与图像→视频（条件控制、编辑与插值）  
- Palette (Saharia et al., SIGGRAPH 2022). 研究问题：统一图像到图像任务（上色、修复、超分等）并扩展为视频情形。核心方法：在扩散框架下设计多种条件化输入（掩码、参考图像、文本），并展示任务通用性。关键结论：单一扩散模型经条件设计可胜任多种图像→图像任务，其思想被迁移到视频修复与编辑（通过逐帧或潜空间方式）[arxiv.org](https://arxiv.org/abs/2111.05826).  
- ControlNet→Video adaptations (series of works 2023–2024). 研究问题：如何将强控制模块（如 ControlNet）从图像扩展到视频以保证跨帧一致性。核心方法：把结构化条件（姿态、深度、边缘）注入扩散 U‑Net，并引入时空注意力或帧间特征传播以维持一致性。关键结论：基于图像的控制模块在视频场景中需配合时序传播/光流或注意力记忆机制方能抑制闪烁并保持一致性（相关实现与评估见下文综合讨论）。（方法思想见 Latent/ControlNet 文献与社区实现; 代表性系统与工程性报告参见后文大型模型报告）[arxiv.org](https://arxiv.org/abs/2112.10752).

4. 大规模/长上下文与高效采样（规模化、长视频与加速）  
- Step‑Video‑T2V (StepFun et al., 2025 technical report). 研究问题：构建大规模文本→视频基座模型以生成更长时序（数百帧）视频。核心方法：提出 Video‑VAE 的深度压缩设计（高空间与时间压缩比）、基于 DiT 的 flow‑matching 视频生成器与视频向 DPO 的后训练方案。关键结论：构建 30B 参数级别模型并在自拟评测（Step‑Video‑T2V‑Eval）上展示对比优势，证明深度压缩 + Transformer 扩散是长序列合成的可行路径 [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/1e8370f5-9db8-4d44-8006-bec0238341f8).  
- Seedance 1.0 (2025). 研究问题：如何在保证质量前提下显著提升推理速度并支持多镜头叙事。核心方法：多源数据构建、潜空间/时空架构优化、后训练的细粒度监督与多维奖励 RLHF、以及多阶段蒸馏与系统级加速。关键结论：报告在 NVIDIA L20 上生成 5 秒 1080p 视频的实测时间（约 41.4 s）并声称约 10× 推理加速，强调系统级优化与蒸馏在工程可用性上的必要性 [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/81777871-7686-4770-9c3c-e65e0b0e9d8f).  
- Long Context Tuning (Guo et al., 2025). 研究问题：如何把单镜头模型扩展为多镜头、场景级连贯生成。核心方法：通过“长上下文调优（LCT）”扩展注意力窗口、引入交错 3D 位置编码与异步噪声策略，并支持联合生成与自回归两种模式。关键结论：在不增加参数量的前提下实现跨镜头连贯性提升，并呈现交互式镜头扩展等 emergent 能力，表明拓宽注意力上下文是多镜头叙事的一条有效路径 [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/05bd1ee3-1dd9-4da4-814c-fc692c94d168).  
- Diffusion Adversarial Post‑Training (Seaweed‑APT, 2025). 研究问题：把多步扩散蒸馏为单步（one‑step）视频生成同时保持质量。核心方法：在扩散预训练后通过对抗式后训练（APT）与判别器稳定化（近似 R1 正则化）对生成器进行适配与微调。关键结论：在若干场景下实现单步生成 2s、1280×720@24fps 视频（报告），表明对抗后训练可以显著缩短采样步数但需要专门的稳定化约束 [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/100355).

实验与评价总结（共性结论，非逐篇复述）  
- 评测指标与人类评估：常见的自动量化指标包括 FVD（Frechet Video Distance）、CLIP‑based 相似度与 frame‑level FID/LPIPS；但对于长视频（多镜头/叙事）这些指标不足以反映叙事一致性与物理合理性，故大量工作仍辅以主观/两两对比的人类评测以评估文本对齐与时序连贯性。  
- 潜空间与级联策略有效降低计算：把扩散放到 VAE 潜空间或采用分阶段（骨架→时序超分→空间超分）的流水线，能够在近似或等质量下显著减少训练/推理成本，这是 Imagen Video、Latent Diffusion、Make‑A‑Video 等共同实践的结论。  
- 控制性依赖中间结构与时序传播：单纯将图像级的控制模块（如 ControlNet）逐帧应用，会导致帧间闪烁；需结合光流/特征传播或时空注意力记忆来维持跨帧一致性（见 MCVD、Control→Video 迁移工作）。  
- 采样速度是主要工程瓶颈：经典 DDPM/score‑based 采样需要数百步，实践中通过 DDIM / DPM‑Solver / 蒸馏 / 对抗后训练与一致性模型蒸馏等手段把步数降到几十步或单步；但单步或极少步数往往需额外训练技巧或牺牲部分分布覆盖，质量-速度权衡仍未彻底解决。  
- 数据规模与标注质量决定通用性：文本→视频模型的质量高度依赖于视频‑文本对的规模与质量；缺乏开放、带丰富元标签（相机运动、镜头切换、角色 ID）的长视频数据集，成为规模化模型泛化与长叙事学习的制约因素（多篇系统报告指出此为关键短板）。

趋势与挑战（基于 2022–2025 证据的预测）  
（至少三点；每点尽量具体并给出支撑要点）

1) 架构由 U‑Net 向 Transformer（DiT / Diffusion Transformer）快速迁移，并伴随大模型化。  
- 证据/理由：GenTron 与 Step‑Video 等工作展示 Transformer 在条件表达与可扩展性上的优势；Transformer 更易与大语言模型（MLLM）或多模态编码器对齐，从而推动统一基座模型发展 [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/44761)、[hub.baai.ac.cn](https://hub.baai.ac.cn/paper/1e8370f5-9db8-4d44-8006-bec0238341f8).  

2) 潜空间 + 级联 + 蒸馏将成为生成长、高分辨率视频的工程常态；同时，长上下文注意力与稀疏/块状注意力用于扩展时序长度。  
- 证据/理由：Latent Diffusion 和 Imagen Video 通过潜空间与级联成功在高分辨率上实用化；Seedance、Step‑Video 与 LCT 强调压缩、KV 缓存与长上下文调优，说明工程化的压缩与注意力策略是放大时长/分辨率的可行路径 [arxiv.org](https://arxiv.org/abs/2112.10752)、[hub.baai.ac.cn](https://hub.baai.ac.cn/paper/81777871-7686-4770-9c3c-e65e0b0e9d8f)、[hub.baai.ac.cn](https://hub.baai.ac.cn/paper/05bd1ee3-1dd9-4da4-814c-fc692c94d168).  

3) 采样一步化/极少步化会成为重要研究方向，但需新范式保证样本多样性与稳定性（对抗后训练、一致性模型、蒸馏结合判别器等）。  
- 证据/理由：Seaweed‑APT（对抗后训练）与一致性模型蒸馏的工程示例表明，通过在扩散预训练后施加对抗或蒸馏目标，可以把步数压缩到单步或数步，但这类方法对稳定性与判别器设计提出新要求 [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/100355).  

4) 长视频的语义/物理一致性将驱动数据与评测基准的发展：更多含镜头切换、相机参数与实体 ID 标注的开源数据集与细粒度评测（叙事一致性 / 物理守恒 / 角色连续性）将出现。  
- 证据/理由：多篇系统报告与大型模型技术报告（如 Step‑Video、Seedance、WAN 报告）指出现有评测不能刻画长叙事质量，呼吁构建分层元数据的基准（电影级别的镜头/场景/角色标注）[hub.baai.ac.cn](https://hub.baai.ac.cn/paper/1e8370f5-9db8-4d44-8006-bec0238341f8).  

5) 多模态统一与“创作工作流级”应用化（文本+图像+音频+动作轨迹的任意组合生成）将加速，但伴随版权/滥用与模型可控性问题。  
- 证据/理由：Wan、Step‑Video 等工程性报告强调多模态输入（双语文本、运动轨迹、深度、音频）与下游集成（个性化、摄像机控制、音频生成），提示未来研究不得不同时面对技术与伦理/合规双重挑战 [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/1e8370f5-9db8-4d44-8006-bec0238341f8)、[blog.csdn.net](https://blog.csdn.net/qq_44681809/article/details/146803878).

结论  
2022–2025 年间，扩散模型在视频生成领域已从早期像素级扩散发展出多条互补路线：潜空间与级联实现高分辨率实用化；掩码条件与控制模块实现多任务与可控编辑；Transformer 与长上下文技术推动大模型与长视频叙事的可行性；而蒸馏/对抗后训练等方法正被用来缩短采样步数以应对工程化部署需求。未来若干年，研究的关键在于把“质量、速度、可控性、长时序一致性”四项目标同时推进——这需要算法创新、数据与评测基准建设以及大规模工程实现三方面协同发力。

参考文献（按出现次序，均为公开论文或技术报告／预印本，便于检索）  
1. Jonathan Ho, Ajay Jain, Pieter Abbeel. Video Diffusion Models. arXiv:2204.03458 (NeurIPS 2022 submission). [arxiv.org](https://arxiv.org/abs/2204.03458)  
2. V. Voleti, et al. MCVD: Masked Conditional Video Diffusion for Prediction, Generation, and Interpolation. arXiv:2205.09853 (NeurIPS 2022). [arxiv.org](https://arxiv.org/abs/2205.09853)  
3. C. Singer, et al. Make‑A‑Video: Text‑to‑Video Generation without Text‑Video Data. arXiv:2209.14792 (Meta AI technical report). [arxiv.org](https://arxiv.org/abs/2209.14792)  
4. Chitwan Saharia, et al. Imagen Video: High Definition Video Generation with Diffusion Models. arXiv:2210.02303 (Google Research). [arxiv.org](https://arxiv.org/abs/2210.02303)  
5. Robin Rombach, et al. High‑Resolution Image Synthesis with Latent Diffusion Models. arXiv:2112.10752 (CVPR 2022). [arxiv.org](https://arxiv.org/abs/2112.10752)  
6. Jonathan Ho, et al. Denoising Diffusion Probabilistic Models (DDPM). arXiv:2006.11239 (NeurIPS 2020). [arxiv.org](https://arxiv.org/abs/2006.11239)  
7. Yang Song & Stefano Ermon. Score‑Based Generative Modeling through Stochastic Differential Equations. arXiv:2011.13456 (ICLR 2021). [arxiv.org](https://arxiv.org/abs/2011.13456)  
8. Chitwan Saharia, et al. Palette: Image‑to‑Image Diffusion Models. arXiv:2111.05826 (SIGGRAPH / NeurIPS lineage). [arxiv.org](https://arxiv.org/abs/2111.05826)  
9. Dhariwal, Prafulla & Nichol, Alex. Diffusion Models Beat GANs on Image Synthesis. arXiv:2105.05233 (NeurIPS 2021). [arxiv.org](https://arxiv.org/abs/2105.05233)  
10. GenTron: Diffusion Transformers for Image and Video Generation (Chen et al., CVPR 2024). Paper summary/listing. [chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/44761)  
11. Seedance 1.0: Exploring the Boundaries of Video Generation Models (technical report; 2025). [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/81777871-7686-4770-9c3c-e65e0b0e9d8f)  
12. Step‑Video‑T2V Technical Report: The Practice, Challenges, and Future of Video Foundation Model (StepFun et al., 2025). [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/1e8370f5-9db8-4d44-8006-bec0238341f8)  
13. Long Context Tuning for Video Generation (Guo et al., 2025). [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/05bd1ee3-1dd9-4da4-814c-fc692c94d168)  
14. Diffusion Adversarial Post‑Training for One‑Step Video Generation (Seaweed‑APT) (Lin et al., 2025, arXiv technical report). [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/100355)  
15. Nichol, Alex & Dhariwal, Prafulla. Improved Denoising Diffusion Probabilistic Models. arXiv:2102.09672 (ICML 2021). [arxiv.org](https://arxiv.org/abs/2102.09672)

（注：文中所用若干系统性或工程性论述来源于上述技术报告与公开预印本；有关工程化实现细节与运行时间的数据以相应技术报告中披露值为准。）