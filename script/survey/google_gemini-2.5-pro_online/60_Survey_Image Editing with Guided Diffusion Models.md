好的，遵照您的指示，作为一名严谨的科研助手，我将基于提供的真实网络搜索结果，生成一份关于“基于引导扩散模型的图像编辑”的中文学术综述。

***

### **基于引导扩散模型的图像编辑技术研究综述 (2022-2025)**

#### **引言**

近年来，扩散概率模型（Diffusion Models）已成为图像生成领域的主流范式，其在生成样本的保真度和多样性上均表现出卓越性能 [hub.baai.ac.cn](https://hub.baai.ac.cn/view/16914)。然而，原始的无条件扩散模型缺乏可控性，无法满足精确的图像编辑需求。为解决此问题，研究者们提出了引导扩散（Guided Diffusion）机制，通过引入外部条件信号来指导模型的逆向去噪过程，从而实现对生成内容的精细调控 [jcst.ict.ac.cn](https://jcst.ict.ac.cn/cn/article/cstr/32374.14.s11390-024-3814-0)。

本综述聚焦于 2022 年至 2025 年间基于引导扩散模型的图像编辑技术，旨在梳理其核心方法、分类、代表性工作及未来发展趋势。此阶段的研究核心在于如何设计高效且精准的引导机制，以响应日益复杂的编辑指令，涵盖从全局风格修改到局部实例级操作的广泛应用场景。

#### **方法分类与代表作**

根据引导信号的类型与控制粒度的不同，可将主流方法分为以下三类：文本与指令引导、空间与实例级引导、以及多模态与通用图像编辑。

**1. 文本与指令引导**

此类方法利用自然语言指令作为核心引导信号，是当前最主流的研究方向。其关键在于让模型准确理解并执行复杂的文本描述。

*   **In-Context Edit (2025)**
    *   **研究问题**: 如何在仅需极少量微调数据的情况下，实现遵循复杂指令的高性能图像编辑，以平衡效率与精度。
    *   **核心方法**: 论文提出了一种基于大型扩散Transformer（DiT）的“上下文编辑”（In-Context Edit）范式。该方法设计了包含源图像和编辑指令的结构化提示（IC prompt），利用DiT的上下文学习能力进行编辑。为提升性能，作者进一步引入了LoRA-MoE混合微调策略和基于VLM的推理时筛选方法，以极高的参数效率实现了对模型的适配。
    *   **关键实验结论**: 实验表明，该方法仅使用同类方法约0.5%的训练数据和1%的可训练参数，便在MagicBrush和Emu等基准上达到了最先进的编辑性能，验证了其在精度与效率上的巨大优势 [themoonlight.io](https://www.themoonlight.io/zh/review/in-context-edit-enabling-instructional-image-editing-with-in-context-generation-in-large-scale-diffusion-transformer)。

*   **基于视觉自回归模型的无训练编辑 (2025)**
    *   **研究问题**: 传统基于扩散模型的编辑方法依赖于图像反演（inversion），其过程中的不准确性会引入伪影并影响保真度。
    *   **核心方法**: 该工作提出一种基于视觉自回归模型（VAR）的无训练编辑框架，规避了扩散模型的反演过程。它通过缓存原始图像的token索引与概率分布，捕捉源图像与文本的关联。编辑时，一种自适应掩蔽策略会识别并限制修改区域，从而在保留非编辑区内容的同时实现精确修改。
    *   **关键实验结论**: 该方法在无需训练的情况下，实现了高保真编辑，其推理速度在A100 GPU上处理1K分辨率图像仅需约1.2秒，证明了在特定任务上，非扩散模型路径也能提供高效率和高质量的解决方案 [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/125277)。

**2. 空间与实例级引导**

此类方法专注于对图像中特定对象的位置、形状、颜色等属性进行精细控制，通常需要借助掩码（Mask）、边界框（Bounding Box）或涂鸦（Scribble）等空间信号。

*   **InstanceDiffusion (2024)**
    *   **研究问题**: 现有的文本到图像模型难以对单个或多个实例进行独立、精确的属性和位置控制。
    *   **核心方法**: InstanceDiffusion通过三大模块实现实例级控制：UniFusion模块融合每个实例的文本描述和位置信息（支持点、框、掩码等多种形式）；ScaleU模块动态调整U-Net特征以提升保真度；Multi-instance Sampler在推理时减少实例间的属性混淆。该方法还构建了一个大规模数据集以支撑多格式、实例级的训练。
    *   **关键实验结论**: 在COCO数据集上，InstanceDiffusion在边界框引导下的AP50指标比之前的SOTA模型高出20.4%，在掩码引导下的IoU指标提升了25.4%，展示了其在复杂场景下对多个实例进行精确控制的强大能力 [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/45330)。

*   **DiffBrush (2025)**
    *   **研究问题**: 如何让用户以直观、免训练的方式，通过手绘草图来控制图像编辑，降低专业文本提示的门槛。
    *   **核心方法**: DiffBrush是一种与现有文本到图像（T2I）模型兼容的免训练框架。它通过在去噪过程中持续引导潜在空间和实例级注意力图，使生成结果朝向用户手绘的粗略掩码和颜色收敛。此外，该方法还提出一种潜在空间再生技术，优化初始噪声布局，以更好地匹配用户的空间意图。
    *   **关键实验结论**: 该方法允许用户仅通过在画布上绘制粗略的彩色掩码，即可在相应位置自然生成目标实例，且无需额外训练成本，证明了通过操纵模型内部表征实现直观控制的可行性 [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/116292)。

**3. 多模态与通用图像编辑**

此类方法旨在构建能够处理多种编辑任务或接受多种引导信号的统一框架，如图像修复、风格迁移和范例指导的编辑。

*   **Palette (2022)**
    *   **研究问题**: 如何构建一个统一的图像到图像（Image-to-Image）翻译框架，以处理着色、修复、扩展等多种任务，而无需为每个任务定制模型架构或损失函数。
    *   **核心方法**: Palette使用单一的条件扩散模型处理多种图像翻译任务。模型以源图像（如灰度图、带掩码的图）为条件，通过标准的去噪目标进行训练。该研究还系统比较了L1和L2损失对样本多样性的影响，并强调了自注意力机制在模型架构中的重要性。
    *   **关键实验结论**: 在ImageNet上进行的标准化评估表明，Palette在所有四项任务（着色、修复、扩展、JPEG复原）上均优于强大的GAN和回归基线，证实了扩散模型作为通用图像编辑框架的潜力 [www.zhuanzhi.ai](https://www.zhuanzhi.ai/paper/a3f477b85ec058045ecbc0eb996860f4)。

*   **Paint by Example (2022)**
    *   **研究问题**: 如何利用一个参考图像（exemplar）来指导对源图像的编辑，从而实现比纯文本引导更精确的视觉风格和内容控制。
    *   **核心方法**: 该工作提出了一种基于范例的图像编辑框架。它通过自监督训练来解耦源图像和范例图像的信息，并利用信息瓶颈和强数据增强来避免简单的“复制粘贴”伪影。为确保可控性，用户可以为范例提供一个任意形状的掩码，并通过无分类器引导（classifier-free guidance）增强生成结果与范例的相似性。
    *   **关键实验结论**: 该方法仅需一次前向传播即可完成编辑，无需迭代优化。实验证明，它能够在野外图像上实现高保真的可控编辑，有效迁移范例图像的纹理和风格 [www.zhuanzhi.ai](https://www.zhuanzhi.ai/paper/2bdb0122df0b032da95290c3fd0a8147)。

#### **实验与评价总结**

综合各项研究，可总结出以下共性结论：

*   **评价指标多样化**: 除了通用的生成质量指标（如FID），针对不同编辑任务的专用指标至关重要。例如，文本对齐度通常使用CLIP Score衡量；空间控制精度则依赖IoU和AP等检测/分割指标；对于主观性强的编辑任务，人类评估（Human Evaluation）仍然是黄金标准，被广泛用于评估布局保真度和指令遵循度 [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/45330)。
*   **精度与保真度的权衡**: 更强的引导（如精细的掩码）能提高编辑的精确度，但也可能导致生成图像的局部区域与整体不协调，或产生伪影。因此，如何在指令遵循度和图像整体的自然度、保真度之间取得平衡，是所有引导扩散模型面临的核心挑战。
*   **数据的重要性**: 高质量、大规模的配对数据（如图像-文本-掩码）是训练强大可控模型的关键。由于此类数据稀缺，自动化数据标注流程（如InstanceDiffusion中利用Grounded-SAM和BLIP-V2自动生成标注）已成为一种重要且有效的数据获取策略 [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/45330)。

#### **趋势与挑战**

基于2025年前后的最新研究，未来基于引导扩散模型的图像编辑将呈现以下趋势，并面临相应挑战：

1.  **向大型Transformer架构迁移**: 随着DiT等基于Transformer的扩散模型展现出优越的可扩展性和上下文学习能力，未来的图像编辑模型将更多地基于此类架构。这不仅能更好地融合多模态引导信息，还能通过上下文学习实现更复杂的零样本或少样本编辑，如In-Context Edit所示 [themoonlight.io](https://www.themoonlight.io/zh/review/in-context-edit-enabling-instructional-image-editing-with-in-context-generation-in-large-scale-diffusion-transformer)。**挑战**在于巨大的计算和内存开销。

2.  **参数与数据效率的提升**: 训练大型模型的成本高昂。因此，参数高效微调（Parameter-Efficient Fine-Tuning, PEFT）技术，如LoRA及其变体（如LoRA-MoE），将成为主流。同时，免训练（Training-Free）方法通过操纵预训练模型的内部表征来实现编辑，仍是一个富有吸引力的方向，因为它最大程度地降低了特定任务的适配成本 [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/116292)。**挑战**在于如何在不牺牲鲁棒性和性能的前提下，进一步提升效率。

3.  **任务通用性与专业化的结合**: 一方面，研究人员将继续探索像Palette一样的通用编辑模型，使其能处理更多任务。另一方面，针对特定应用（如图像修复），设计更高效的专用模型（如DiffIR，通过预测紧凑先验而非全图来提速）也将是重要趋势。未来可能会出现一种“通用骨干+专业化适配器”的模式 [www.zhuanzhi.ai](https://www.zhuanzhi.ai/paper/246fe9068ef5a64044cb6d4fcbe1574a)。**挑战**在于如何设计一个既通用又易于专业化的框架。

#### **结论**

自2022年以来，基于引导扩散模型的图像编辑技术取得了长足的进步。研究范式已从单一的文本引导演变为融合文本、空间布局、视觉范例等信号的多模态精确控制。代表性工作如InstanceDiffusion和In-Context Edit，分别在实例级控制和指令遵循的效率与精度上树立了新的标杆。未来的研究将继续围绕提升模型的控制精度、效率和通用性展开，大型Transformer架构、参数高效微调以及更智能的引导机制将是推动该领域发展的核心驱动力。

#### **参考文献**

1.  [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/45330) (InstanceDiffusion: Instance-level Control for Image Generation, 2024)
2.  [themoonlight.io](https://www.themoonlight.io/zh/review/in-context-edit-enabling-instructional-image-editing-with-in-context-generation-in-large-scale-diffusion-transformer) (In-Context Edit: Enabling Instructional Image Editing with In-Context Generation in Large Scale Diffusion Transformer, 2025)
3.  [www.zhuanzhi.ai](https://www.zhuanzhi.ai/paper/a3f477b85ec058045ecbc0eb996860f4) (Palette: Image-to-Image Diffusion Models, 2022)
4.  [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/116292) (DiffBrush: Just Painting the Art by Your Hands, 2025)
5.  [www.zhuanzhi.ai](https://www.zhuanzhi.ai/paper/2bdb0122df0b032da95290c3fd0a8147) (Paint by Example: Exemplar-based Image Editing with Diffusion Models, 2022)
6.  [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/125277) (Training-Free Text-Guided Image Editing with Visual Autoregressive Model, 2025)
7.  [jcst.ict.ac.cn](https://jcst.ict.ac.cn/cn/article/cstr/32374.14.s11390-024-3814-0) (多模态可控扩散模型综述, 2024)
8.  [hub.baai.ac.cn](https://hub.baai.ac.cn/view/16914) (基于扩散模型的文本引导图像生成算法, 2022)
9.  [www.zhuanzhi.ai](https://www.zhuanzhi.ai/paper/246fe9068ef5a64044cb6d4fcbe1574a) (DiffIR: Efficient Diffusion Model for Image Restoration, 2023)
10. [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/498ec22a-4f09-4515-893f-359748713dd8) (CCDM: Continuous Conditional Diffusion Models for Image Generation, 2024)