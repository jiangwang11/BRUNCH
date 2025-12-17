# 多模态图像合成与编辑综述（2022–2025）

## 引言

多模态图像合成与编辑（Multimodal Image Synthesis and Editing, MISE）旨在根据文本、视觉布局、音频或其他模态的引导信号生成或修改图像，模拟人类跨模态想象力。随着扩散模型（Diffusion Models）在2022年后成为主流生成范式，该领域从早期以GAN为主的架构转向以扩散为核心、融合大语言模型（LLM）与视觉语言模型（VLM）的统一框架。本文综述2022–2025年间该领域的代表性工作，按方法范式分类，聚焦其技术突破、评估范式与未来挑战。

---

## 方法分类与代表作

### 1. 基于扩散模型的多模态引导生成

**Imagen (Saharia et al., 2022, arXiv)**  
针对文本到图像生成中语义对齐不足的问题，提出利用大型预训练语言模型（T5）作为文本编码器，而非专用多模态编码器。方法采用级联扩散架构：先生成64×64图像，再通过两个超分辨率扩散模型上采样至1024×1024。实验表明，仅使用文本语料预训练的语言模型在生成语义保真度上显著优于CLIP等对齐模型，在人工评估中超越DALL·E。

**GLIGEN (Li et al., 2023, CVPR)**  
解决开放词汇下基于布局（如边界框+文本）的图像生成问题。方法在冻结Stable Diffusion权重的前提下，插入可训练的门控注意力层，融合文本与空间坐标。训练采用混合数据（文本+框、纯文本），实现零样本布局控制。在COCO和自建布局数据集上，其生成图像在对象位置准确性和开放类别支持上显著优于LayoutGAN等GAN方法。

**LayoutDiffusion (Zheng et al., 2023, CVPR)**  
面向复杂多对象布局到图像生成任务，设计专用扩散模型。提出物体感知交叉注意力（OaCA）与布局融合模块（LFM），将边界框与类别联合编码为序列，并在UNet中实现位置-语义对齐。在COCO Layout数据集上，其AP50达到58.2，比LostGAN-v2高12.1点，且支持25步快速采样，验证了扩散模型在布局控制中的高保真优势。

---

### 2. 基于大模型推理链的生成与编辑

**GoT (Fang et al., 2025, arXiv)**  
指出当前文生图模型缺乏对空间关系与语义逻辑的显式推理。提出“生成式思维链”（Generation Chain-of-Thought），先由Qwen2.5-VL生成包含对象位置、关系与属性的结构化推理链，再由扩散模型执行。构建含900万样本的GoT数据集。在GenEval和Reason-Edit基准上，其CLIP-T分数达0.276，显著优于InstructPix2Pix（0.192），并支持交互式修改推理步骤。

**DreamOmni (Xia et al., 2025, CVPR)**  
针对现有T2I模型需依赖ControlNet等插件实现编辑的碎片化问题，提出统一生成与编辑的单一模型。采用DiT+UNet混合架构，并设计合成拼贴数据流水线自动生成修复、拖拽、指令编辑等多任务数据。在512×512分辨率下，其T2I生成在GenEval上SOTA，同时在指令编辑任务中FID比MGIE低3.2，证明联合训练可提升多任务一致性。

---

### 3. 实例级精细控制方法

**InstanceDiffusion (Wang et al., 2024, CVPR)**  
解决文生图模型无法对单个实例进行独立控制的问题。提出支持点、涂鸦、框、掩码等多种位置格式，并为每个实例分配独立文本描述。核心组件包括UniFusion（格式感知融合）、ScaleU（动态特征重校准）和多实例采样器。在COCO上，其AP50_box为38.8，比GLIGEN高20.4%；在LVIS密集场景中仍保持高属性绑定准确率（颜色+25.2%）。

**Imagic (Kawar et al., 2023, CVPR)**  
实现对单张真实图像的复杂非刚性编辑（如“狗坐下”）。方法通过三步：1) 优化文本嵌入使其重建输入图像；2) 微调扩散模型；3) 在优化嵌入与目标文本嵌入间线性插值。在自建TEdBench基准上，人类偏好率达70%以上，首次证明扩散模型可对真实图像执行细粒度语义编辑而无需掩码或参考图。

---

### 4. 零训练推理控制策略

**NoiseCollage (Shirakawa & Uchida, 2024, arXiv)**  
提出无需训练的布局控制方法：为每个对象生成独立高斯噪声，按边界框位置拼贴为全局初始噪声，再送入预训练扩散模型去噪。该方法在Stable Diffusion上实现零样本布局生成，避免注意力干扰。实验证明其在简单布局下效果接近LayoutDiffusion，但对重叠对象泛化有限，凸显推理阶段控制的灵活性与局限性。

**Paint-with-Words (Balaji et al., 2023, eDiff-I)**  
通过人为干预扩散模型的跨注意力图实现区域控制。用户提供语义分割掩码，系统在采样时增强对应文本token对指定区域的注意力权重。该方法无需训练，可直接用于任意文生图模型，在纠正对象错位方面有效，但依赖用户精确掩码，自动化程度低。

---

## 实验与评价总结

当前评估呈现三大共性趋势：  
1. **多维指标并用**：除传统FID、IS外，广泛采用CLIP Score（文本-图像对齐）、Layout Fidelity（如AP50_box、IoU_mask）及人类偏好研究（如TEdBench上的2AFC）。  
2. **复杂场景基准兴起**：GenEval、Reason-Edit、TEdBench等强调多对象、空间推理与非刚性编辑，推动方法从“生成漂亮图”转向“精确执行指令”。  
3. **零样本与泛化能力受重视**：在LVIS、OpenImages等开放类别数据集上测试成为标配，反映对真实世界适用性的关注。

然而，评估仍存缺陷：CLIP Score对细粒度语义不敏感；人工评估成本高且主观；缺乏对物理合理性（如遮挡、透视）的自动化度量。

---

## 趋势与挑战（2025年前后）

1. **推理驱动的生成架构**：GoT等工作预示未来模型将分离“规划”与“渲染”，由MLLM生成结构化场景描述（含空间、物理、因果关系），扩散模型仅负责高质量渲染，提升可控性与可解释性。  
2. **3D-2D联合生成**：受Sora等视频生成模型启发，NeRF与扩散模型融合（如Dream Fields、AvatarCLIP）将从静态3D建模转向动态、可编辑的3D场景生成，实现“文生3D+任意视角渲染”。  
3. **高效统一多任务框架**：DreamOmni表明，通过合成数据与混合架构，单一模型可同时胜任生成、修复、拖拽、参考等任务，减少插件依赖。未来方向包括DiT架构优化、LoRA微调与推理控制的结合，以平衡性能与效率。  
4. **安全与版权机制内嵌**：随着滥用风险上升，2025年后研究将更关注生成内容的可追溯性（如水印）、偏见抑制与训练数据版权合规，可能催生“负责任生成”新子领域。

---

## 结论

2022–2025年，多模态图像合成与编辑完成从GAN到扩散模型的范式迁移，并正迈向“推理+生成”统一架构。代表性工作在布局控制、实例编辑、真实图像修改等方面取得突破，但评估体系、物理合理性与计算效率仍是瓶颈。未来研究将深度融合多模态大模型的推理能力与扩散模型的生成能力，向3D、视频及安全可控方向演进。

---

## 参考文献

1. Saharia, C., et al. (2022). *Photorealistic Text-to-Image Diffusion Models with Deep Language Understanding*. arXiv:2205.11487.  
2. Li, Y., et al. (2023). *GLIGEN: Open-Set Grounded Text-to-Image Generation*. CVPR.  
3. Zheng, G., et al. (2023). *LayoutDiffusion: Controllable Diffusion Model for Layout-to-Image Generation*. CVPR.  
4. Fang, R., et al. (2025). *GoT: Generation Chain-of-Thought for Reasoning-Driven Visual Generation and Editing*. arXiv:2503.10639.  
5. Xia, B., et al. (2025). *DreamOmni: Unified Image Generation and Editing*. CVPR.  
6. Wang, X., et al. (2024). *InstanceDiffusion: Instance-level Control for Image Generation*. CVPR.  
7. Kawar, B., et al. (2023). *Imagic: Text-Based Real Image Editing with Diffusion Models*. CVPR.  
8. Shirakawa, T., & Uchida, S. (2024). *NoiseCollage: A Layout-Aware Text-to-Image Diffusion Model Based on Noise Cropping and Merging*. arXiv:2403.03485.  
9. Balaji, Y., et al. (2023). *eDiff-I: Text-to-Image Diffusion Models with an Ensemble of Expert Denoisers*. arXiv:2211.01324.  
10. Shuai, X., et al. (2024). *A Survey of Multimodal-Guided Image Editing with Text-to-Image Diffusion Models*. arXiv:2406.14555.  
11. Qi, S. (2025). *Research Progress on Text-to-Image Diffusion Models Based on Layout Control*. Computer Science and Application, 15(4), 443–452.  
12. He, Y., et al. (2024). *LLMs Meet Multimodal Generation and Editing: A Survey*. arXiv:2405.18045.