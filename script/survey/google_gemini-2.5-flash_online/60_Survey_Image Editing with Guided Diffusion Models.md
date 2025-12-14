## Image Editing with Guided Diffusion Models 综述 (2022-2025)

### 引言

图像编辑是人工智能生成内容（AIGC）领域中的关键任务，旨在根据用户需求修改现有图像。近年来，扩散模型（Diffusion Models, DMs）凭借其卓越的图像生成质量、稳定性及多样性，已成为图像编辑领域的主流技术。与传统生成对抗网络（GANs）受限于模式坍塌和训练不稳定等问题不同，扩散模型通过模拟数据分布的逐步去噪过程，能够实现高保真度且灵活可控的图像编辑。本综述将聚焦于2022年至2025年间，扩散模型在图像编辑领域的代表性工作，系统梳理其主要方法、共性结论，并展望未来研究趋势与挑战。

### 方法分类与代表作

基于扩散模型的图像编辑方法可以根据其核心策略划分为以下几类：专用扩散模型方法、基于预训练扩散模型的适配方法以及推理阶段的组合与控制方法。

#### 1. 专用扩散模型方法

这类方法为特定的图像编辑任务从头设计和训练扩散模型，强调结构化建模以实现高精度控制。

*   **Palette: Image-to-Image Diffusion Models (2022)** [zhuanzhi.ai](https://www.zhuanzhi.ai/paper/a3f477b85ec058045ecbc0eb996860f4)
    该研究提出了一个基于条件扩散模型的统一图像到图像翻译框架，旨在解决图像着色、修复、超分辨率和JPEG修复等任务。其核心方法是采用简单的L2或L1损失进行去噪扩散目标训练，并强调自注意力机制在神经网络结构中的重要性。实验表明，该框架在不进行任务特定超参数调整或架构定制的情况下，在多项任务上超越了GAN和回归基线。该工作为后续图像到图像扩散模型奠定了统一评估协议的基础，并证明了通用多任务扩散模型的有效性。

*   **LayoutDiffusion: Controllable Diffusion Model for Layout-To-Image Generation (2023)** [pdf.hanspub.org](https://pdf.hanspub.org/csa2025154_451543569.pdf)
    该模型旨在实现复杂多物体布局的高保真图像生成和精细控制，解决了传统方法在布局遵循性上的局限。核心方法是采用条件DDPM框架，并设计了布局融合模块（LFM）和物体感知交叉注意力（OaCA）两大组件，强化多物体之间的关系建模，精细注入特定物体特征。实验证明，LayoutDiffusion在复杂场景下生成图像质量高且布局精确，并能明显优于GAN基准，显示了专门设计扩散模型在多物体布局生成上的巨大潜力。

*   **DiffIR: Efficient Diffusion Model for Image Restoration (2023)** [zhuanzhi.ai](https://www.zhuanzhi.ai/paper/246fe9068ef5a64044cb6d4fcbe1574a)
    该研究提出了一种高效的图像修复扩散模型（DiffIR），解决了传统扩散模型在图像修复任务中运行大量迭代导致效率低下的问题。其核心方法是引入紧凑的图像修复先验提取网络（CPEN）、动态IR转换器（DIRformer）和去噪网络，并通过两阶段训练（预训练和DM训练）来捕获和利用紧凑的IR先验表示。实验结果表明，DiffIR在降低计算成本的同时，在多个图像修复任务上达到了最先进的性能，验证了其在效率和性能上的优越性。

#### 2. 基于预训练扩散模型的适配方法

这类方法利用在大规模数据上预训练的扩散模型，通过引入少量参数或调整网络以适应特定的布局或编辑条件，从而兼顾开放世界概念和精细控制。

*   **GLIGEN: Open-Set Grounded Text-To-Image Generation (2023)** [pdf.hanspub.org](https://pdf.hanspub.org/csa2025154_451543569.pdf)
    GLIGEN致力于解决开放集场景下的布局控制问题，允许用户通过自然语言描述任意物体并指定其位置。其核心方法是在预训练的Stable Diffusion模型中添加门控Transformer层，融合边界框等新输入，并保持原有模型权重冻结以避免灾难性遗忘。GLIGEN通过两阶段采样策略（前期融合文本和布局，后期侧重图像质量）巧妙地平衡了控制与质量，实现了零样本布局控制任务的显著效果。

*   **ControlNet: Adding Conditional Control to Text-to-Image Diffusion Models (2023)** [pdf.hanspub.org](https://pdf.hanspub.org/csa2025154_451543569.pdf)
    ControlNet提出了一种通用的条件控制扩散模型方法，旨在为文本到图像扩散模型增加额外的空间控制能力。其核心思想是复制一份UNet结构作为“条件分支”进行训练，该分支接收边缘图、姿态骨架等外部条件，并通过注入与原模型相同尺寸的特征来影响采样过程。ControlNet通过冻结原模型权重、仅训练条件分支，实现了在不改变主模型生成能力的前提下，对生成内容的高度精细控制，并且具有强大的通用性和可扩展性。

*   **InstanceDiffusion: Instance-level Control for Image Generation (2024)** [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/45330)
    InstanceDiffusion致力于为文本到图像模型增加精确的实例级控制，支持每个实例的自由形式语言条件和灵活的位置指定（如点、边界框、分割掩码）。该研究提出了UniFusion模块、ScaleU模块和Multi-instance Sampler三项主要改进：UniFusion融合文本和位置嵌入，ScaleU提高图像保真度，Multi-instance Sampler减少多个实例生成中的混淆。实验结果表明，InstanceDiffusion在每个位置条件下显著超越了现有最先进模型，尤其在COCO数据集上取得了显著的AP50box和IoU提升。

#### 3. 推理阶段的组合与控制方法

这类方法主要通过算法层面在推理阶段对预训练扩散模型进行操作，以实现布局控制和优化，无需或仅需少量额外训练。

*   **Training-Free Text-Guided Image Editing with Visual Autoregressive Model (2025)** [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/125277)
    该研究提出了一种无需训练的文本引导图像编辑框架，旨在解决传统扩散模型反演不准确和文本提示与图像特征纠缠导致的全局变化问题。其核心方法是引入基于VAR（视觉自回归建模）的缓存机制，存储原始图像的标记索引和概率分布，并设计自适应细粒度掩蔽策略动态限制修改区域。通过标记重组方法进一步优化编辑过程，该框架在无训练、高保真度、以及更快的推理速度（1.2秒处理1K分辨率图像）方面超越了现有基于扩散和修正流的方法。

*   **NoiseCollage: A Layout-Aware Text-to-Image Diffusion Model Based on Noise Cropping and Merging (2024)** [pdf.hanspub.org](https://pdf.hanspub.org/csa2025154_451543569.pdf)
    NoiseCollage提出了一种新颖的推理方法，通过直接操纵扩散模型的噪声空间来实现布局控制，实现了零训练开销。其核心想法是在扩散采样的初始阶段，为布局中每个物体单独生成高斯噪声，然后根据边界框将噪声片段裁剪并嵌入到全局噪声图中。这种方法将整体生成拆分成独立局部生成再合并，在一个扩散过程内克服了传统方法的多次连续采样问题。NoiseCollage印证了“噪声是良好直接布局控制媒介”的观点，在无需模型改动或训练的情况下实现了布局控制。

*   **In-Context Edit: Enabling Instructional Image Editing with In-Context Generation in Large Scale Diffusion Transformer (2025)** [themoonlight.io](https://www.themoonlight.io/zh/review/in-context-edit-enabling-instructional-image-editing-with-in-context-generation-in-large-scale-diffusion-transformer)
    本论文提出了一种名为In-Context Edit的新型基于扩散Transformer（DiT）的指令图像编辑方法，在极少量微调数据下实现了先进性能。其核心方法一是构建基于DiT的in-context编辑范式，利用特殊prompt形式进行zero-shot指令遵循；二是通过LoRA-MoE混合微调策略提高稳定性和质量，并结合基于视觉语言模型（VLM）的Early Filter推理时缩放方法增强编辑结果。实验表明，该方法在MagicBrush和Emu基准测试中表现优异，仅需0.5%的训练数据和1%的可训练参数，实现了效率和精度之间的平衡。

### 实验与评价总结

针对基于扩散模型的图像编辑，评价体系趋于完善，不再仅仅依赖 FID 等生成质量指标。除了生成图像的视觉质量和多样性外，更强调编辑的**精确性与可控性**。

1.  **对齐性评估：** 模型生成结果与给定条件（如文本提示、布局信息、特定实例描述等）的对齐程度是核心考量。例如，InstanceDiffusion在COCO数据集上通过AP50box和IoU等指标量化了实例级控制的准确性[chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/45330)。
2.  **保真度与非相关区域保持：** 在进行局部编辑时，模型对图像非编辑区域的原始内容和细节的保持能力至关重要。Training-Free Text-Guided Image Editing等工作强调了避免意外修改和影响保真度的能力[chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/125277)。
3.  **效率与成本：** 随着模型规模增大和应用场景的复杂化，推理速度和训练开销成为重要指标。许多研究致力于实现更快的推理速度（如1.2秒处理1K分辨率图像）和更低的训练或微调成本，例如In-Context Edit仅需极少量数据和参数即可达到SOTA性能[themoonlight.io](https://www.themoonlight.io/zh/review/in-context-edit-enabling-instructional-image-editing-with-in-context-generation-in-large-scale-diffusion-transformer)。
4.  **通用性与泛化能力：** 模型处理未见过的指令、新颖布局或开放集对象的能力。GLIGEN和ControlNet等通过利用预训练模型的知识，展示了强大的零样本泛化能力[pdf.hanspub.org](https://pdf.hanspub.org/csa2025154_451543569.pdf)。
5.  **用户研究与LMM Score：** 为了更准确地评估用户感知和编辑体验，用户研究和利用大型多模态模型（LMMs）进行评估的LMM Score等创新指标被引入，以提供更忠实的定性和定量评价[blog.csdn.net](https://blog.csdn.net/SmartLab307)。

### 趋势与挑战

2025年及前后，Image Editing with Guided Diffusion Models领域将呈现以下趋势与挑战：

1.  **向更高级别的语义理解与交互演进：** 领域将从单纯的“指令执行”转向“语义理解与智能交互”。未来的模型将不仅能根据具体指令修改图像，还能理解指令背后的深层意图、推理物理常识和空间关系，甚至通过多轮对话与用户进行创意协作。挑战在于如何有效地整合视觉语言大模型（VLMs）的推理能力与扩散模型的生成能力，并构建能编码物理属性和运动轨迹的张量表征。
2.  **零样本/少样本编辑的鲁棒性与泛化能力：** 尽管已有零样本编辑方法，但其在处理极端复杂、非规范或训练集中未出现过的场景时仍存在局限。未来研究将聚焦于提升零样本和少样本编辑的鲁棒性和泛化能力，使其能更好地应对“开放世界”中的编辑需求，例如通过更精巧的上下文学习（In-Context Learning）机制，或结合神经符号系统进行逻辑推理。
3.  **动态场景的时空一致性编辑：** 图像编辑将不再局限于静态图片，视频和3D场景的编辑将成为重要方向。核心挑战在于如何实现编辑在时间（视频帧间）和空间（3D场景中）的高度一致性，避免闪烁、变形等伪影。借鉴Sora等模型的时空patch表征和MagicAnimate等技术将是实现动态场景编辑的关键，同时需要解决多物体运动轨迹与外观连续性的协同优化问题。

### 结论

基于扩散模型的图像编辑技术在2022-2025年间取得了显著进展，从早期专用模型到整合预训练大模型的适配方法，再到无需训练的推理控制策略，模型的生成质量、控制精度和效率均大幅提升。未来，该领域将持续向更深层次的语义理解、更强大的泛化能力以及动态场景编辑迈进，同时面临着模型效率、鲁棒性和高级交互设计等挑战。

### 参考文献

1.  [zhuanzhi.ai](https://www.zhuanzhi.ai/paper/a3f477b85ec058045ecbc0eb996860f4) Saharia, C., Chan, W., Chang, H., et al. (2022). Palette: Image-to-Image Diffusion Models. *ArXiv:2111.05826*.
2.  [pdf.hanspub.org](https://pdf.hanspub.org/csa2025154_451543569.pdf) 齐时达. (2025). 基于布局控制的文本到图像扩散模型研究进展. *计算机科学与应用, 15*(4), 443-452.
3.  [zhuanzhi.ai](https://www.zhuanzhi.ai/paper/246fe9068ef5a64044cb6d4fcbe1574a) Xia, B., Zhang, Y., Wang, S., et al. (2023). DiffIR: Efficient Diffusion Model for Image Restoration. *ArXiv:2303.09472*.
4.  [pdf.hanspub.org](https://pdf.hanspub.org/csa2025154_451543569.pdf) Li, Y., Liu, H., Wu, Q., et al. (2023). GLIGEN: Open-Set Grounded Text-To-Image Generation. *2023 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*, 22511-22521.
5.  [pdf.hanspub.org](https://pdf.hanspub.org/csa2025154_451543569.pdf) Zhang, L., Rao, A., & Agrawala, M. (2023). Adding Conditional Control to Text-to-Image Diffusion Models. *2023 IEEE/CVF International Conference on Computer Vision (ICCV)*, 3813-3824.
6.  [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/45330) Wang, X., Darrell, T., Rambhatla, S. S., et al. (2024). InstanceDiffusion: Instance-level Control for Image Generation. *CVPR 2024*.
7.  [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/125277) Wang, Y., Guo, L., Li, Z., et al. (2025). Training-Free Text-Guided Image Editing with Visual Autoregressive Model. *ArXiv:2503.23897*.
8.  [pdf.hanspub.org](https://pdf.hanspub.org/csa2025154_451543569.pdf) Shirakawa, T., & Uchida, S. (2024). NoiseCollage: A Layout-Aware Text-to-Image Diffusion Model Based on Noise Cropping and Merging. *ArXiv:2403.03485*.
9.  [themoonlight.io](https://www.themoonlight.io/zh/review/in-context-edit-enabling-instructional-image-editing-with-in-context-generation-in-large-scale-diffusion-transformer) In-Context Edit: Enabling Instructional Image Editing with In-Context Generation in Large Scale Diffusion Transformer. (2025). *ArXiv:2504.20690*.
10. [blog.csdn.net](https://blog.csdn.net/SmartLab307) Huang, Y., Huang, J., Liu, Y., et al. (2024). 基于扩散模型的图像编辑：首篇综述. *ArXiv:2402.17525*.
11. [blog.csdn.net](https://blog.csdn.net/u012744245/article/details/140287552) Shuai, X., Ding, H., Ma, X., et al. (2024). 最新综述：多模态引导的基于文生图大模型的图像编辑算法. *ArXiv:2406.14555*.
12. [jcst.ict.ac.cn](https://jcst.ict.ac.cn/cn/article/cstr/32374.14.s11390-024-3814-0) 江锐, 郑光聪, 李藤, 等. (2024). 多模态可控扩散模型综述. *计算机科学与技术学报*.
13. [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/116292) Chu, J., Jin, L., Wang, T., et al. (2025). DiffBrush: Just Painting the Art by Your Hands. *ArXiv:2502.20904*.