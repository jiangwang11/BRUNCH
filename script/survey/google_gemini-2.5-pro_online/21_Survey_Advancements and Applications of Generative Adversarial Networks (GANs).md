好的，作为一名严谨的科研助手，我将基于提供的真实网络搜索结果，为您生成一篇关于“生成对抗网络（GAN）的进展与应用”的中文学术综述。

***

### **生成对抗网络（GAN）的进展与应用研究综述 (2022-2025)**

#### **摘要**
本综述旨在系统梳理 2022 年至 2025 年间生成对抗网络（Generative Adversarial Networks, GANs）领域的最新研究进展与关键应用。在这一时期，生成模型领域经历了以扩散模型（Diffusion Models）为主导的范式转移，其在生成质量和训练稳定性上超越了传统GAN。尽管如此，GANs并未被完全取代，而是在特定方向上演化出新的研究路径。本文将GAN的近期进展归纳为两大主流：1）与扩散模型深度融合的混合架构，旨在克服GAN固有的训练不稳定性；2) 在医学影像等“小数据、高专业”垂直领域内深耕的图像翻译应用。通过对代表性工作的分析，本文总结了当前GAN在定量指标（如FID、IS）与定性评估（如专家盲审）中的表现，并指出其未来的研究趋势主要体现在模型架构的融合、面向特定领域的应用深化，以及生成模型理论边界的模糊与统一。

**关键词：** 生成对抗网络；扩散模型；图像翻译；混合模型；医学影像

---

#### **1. 引言**
生成对抗网络（GAN）自2014年被提出以来，一直是生成式人工智能领域的核心驱动力之一，其通过生成器与判别器的对抗博弈机制，在图像生成、风格迁移等任务中取得了里程碑式的成就 [jeit.ac.cn](https://jeit.ac.cn/cn/article/doi/10.11999/JEIT221400?viewType=HTML#:~:text=D%2DWGAN%E4%B8%8D%E4%BB%85%E8%83%BD%E5%A4%9F%E7%94%9F%E6%88%90,%E7%9A%84%E5%BD%A2%E6%80%81%E4%B9%9F%E6%9B%B4%E5%8A%A0%E7%9C%9F%E5%AE%9E%E3%80%82)。然而，GANs固有的训练不稳定、模式坍塌（Mode Collapse）等问题始终是其发展的瓶颈 [pdf.hanspub.org](https://pdf.hanspub.org/csa2025154_451543569.pdf)。

进入2022-2025年，生成模型领域见证了扩散模型的崛起。扩散模型通过一个逐步去噪的逆过程生成数据，展现出前所未有的图像保真度和多样性，在训练稳定性上也显著优于GAN [www.skycaiji.com](https://www.skycaiji.com/aigc/ai9735.html)。一系列综述性研究指出，扩散模型已在诸多大规模生成任务（如文本到图像）中成为主流技术 [pdf.hanspub.org](https://pdf.hanspub.org/csa2025154_451543569.pdf)。

在此背景下，GAN的研究重心发生了显著偏移。本综述聚焦于此期间GAN的演进路径，不再追求于开放域大规模图像合成的正面竞争，而是转向两个核心方向：一是吸收其他模型（尤其是扩散模型）的优点以构建更稳定的混合架构；二是在数据获取成本高、专业性强的垂直领域（如医学影像）中，发挥其在特定图像翻译任务上的优势。

#### **2. 方法分类与代表作**
根据近期研究趋势，我们将GAN的代表性工作分为以下两类。

##### **2.1 扩散-生成对抗混合模型 (Hybrid Diffusion-GAN Models)**
此类方法旨在利用扩散过程的特性来约束或稳定GAN的训练，从而克服其核心缺陷。

*   **D-WGAN (2023)**
    *   **研究问题**: 传统GAN在文本到图像生成任务中普遍存在训练不稳定的问题。
    *   **核心方法**: 该研究提出了一种扩散Wasserstein生成对抗网络（D-WGAN）。其核心创新在于将扩散过程中的随机采样实例噪声注入判别器，利用扩散过程的平滑特性来稳定WGAN的训练。同时，模型引入了CLIP（Contrastive Language-Image Pre-training）来增强文本与生成图像之间的语义一致性。
    *   **关键实验结论**: 在MSCOCO和CUB-200数据集上，D-WGAN不仅实现了稳定的训练过程，还在Fréchet Inception Distance (FID)和Inception Score (IS)等关键指标上取得了优于同期GAN模型（如DF-GAN）的性能，证明了扩散过程作为稳定器的有效性 [jeit.ac.cn](https://jeit.ac.cn/cn/article/doi/10.11999/JEIT221400?viewType=HTML#:~:text=D%2DWGAN%E4%B8%8D%E4%BB%85%E8%83%BD%E5%A4%9F%E7%94%9F%E6%88%90,%E7%9A%84%E5%BD%A2%E6%80%81%E4%B9%9F%E6%9B%B4%E5%8A%A0%E7%9C%9F%E5%AE%9E%E3%80.82)。

##### **2.2 领域专精化的图像翻译与生成 (Domain-Specific Image Translation and Generation)**
在扩散模型需要海量数据进行预训练的背景下，GANs（特别是CycleGAN等变体）因其对非配对数据的高效处理能力，在数据稀缺的专业领域找到了不可替代的应用场景，尤其是在医学影像分析中。

*   **CycleGAN用于痤疮物理治疗效果预测 (2025)**
    *   **研究问题**: 如何为患者和医生提供痤疮物理治疗（如强脉冲光、化学换肤）的直观预后效果，以辅助治疗决策，避免无效治疗。
    *   **核心方法**: 研究构建了一个基于循环一致性生成对抗网络（CycleGAN）的预后生成模型。该模型在非配对的 acne 治疗前后图像数据集上进行训练，学习从治疗前的皮肤状态到治疗后状态的图像翻译映射。
    *   **关键实验结论**: 生成的预测图像在结构相似性指数（SSIM）上与真实预后图像达到99.8%以上的高度相似。更重要的是，在由资深皮肤科医生进行的双盲测试中，医生无法有效区分生成图像与真实图像（总体区分准确率仅为52%），证实了该模型在临床辅助决策中的巨大潜力 [www.sciengine.com](https://www.sciengine.com/doi/pdfView/3F60D7C0D3AB4F3CBCE9D58860F60865)。

*   **MedGAN用于跨模态医学影像重建 (2020, 被2024年综述引用)**
    *   **研究问题**: 在临床实践中，如何从一种模态的医学影像（如PET）生成另一种模态的影像（如CT），以减少患者辐射暴露或补充缺失的影像信息。
    *   **核心方法**: MedGAN模型通过在生成器中级联多个全卷积网络来保证生成图像的细节和分辨率。它被应用于从PET影像重建CT影像，为PET数据的衰减校正提供高质量的解剖学参考。
    *   **关键实验结论**: MedGAN能够生成高分辨率且清晰的CT影像，其后续改进模型UP-GAN通过渐进式训练的方式进一步提升了生成图像的保真度。这一系列工作凸显了GAN在特定医学图像转换任务中的实用价值 [www.medsci.cn](https://www.medsci.cn/article/show_article.do?id=8f69810082ba)。

*   **CycleGAN用于MRI-CT影像合成 (2018-2021, 被2024年综述引用)**
    *   **研究问题**: 在进行放射治疗规划时，通常需要CT影像进行剂量计算，但MRI能提供更好的软组织对比度。如何仅通过MRI生成高质量的合成CT（sCT），从而实现MRI-Only的放疗流程。
    *   **核心方法**: 由于获取同一患者在同一时点的配对MRI和CT影像十分困难，CycleGAN被广泛用于非配对的MRI到CT的翻译任务。后续研究通过引入形状一致性损失或密集连接块等改进，以保留更精确的解剖结构。
    *   **关键实验结论**: 在盆腔等部位，CycleGAN生成的sCT被证实满足临床剂量学的精度要求。尽管在重建复杂病变区域方面仍面临挑战，但它为无CT的放疗规划提供了可行的技术路径 [www.medsci.cn](https://www.medsci.cn/article/show_article.do?id=8f69810082ba)。

#### **3. 实验与评价总结**
在实验评估方面，2022-2025年间的GAN研究呈现出清晰的目标导向性。
*   **对于混合模型**，如D-WGAN，评估的重点在于是否解决了GAN的核心痛点。实验不仅报告了**FID**和**IS**等标准图像生成质量指标的提升，更强调了训练过程的**收斂性**和**稳定性**，以证明其相较于纯GAN基线的架构优势 [jeit.ac.cn](https://jeit.ac.cn/cn.article/doi/10.11999/JEIT221400?viewType=HTML#:~:text=D%2DWGAN%E4%B8%8D%E4%BB%85%E8%83%BD%E5%A4%9F%E7%94%9F%E6%88%90%2C%E7%9A%84%E5%BD%A2%E6%80%81%E4%B9%9F%E6%9B%B4%E5%8A%A0%E7%9C%9F%E5%AE%9E%E3%80%82)。
*   **对于领域专精应用**，特别是在医学影像领域，评估标准超越了传统的视觉保真度，更加注重**临床实用性**和**结构准确性**。例如，痤疮预测模型不仅使用**SSIM**等像素级度量，还引入了**领域专家（皮肤科医生）的双盲评估**，直接衡量其在临床决策辅助中的可信度 [www.sciengine.com](https://www.sciengine.com/doi/pdfView/3F60D7C0D3AB4F3CBCE9D58860F60865)。在跨模态重建任务中，评估则更关注生成影像在下游任务（如放疗剂量计算）中的**精度**是否满足临床标准 [www.medsci.cn](https://www.medsci.cn/article/show_article.do?id=8f69810082ba)。

#### **4. 趋势与挑战**
基于2022-2025年的研究现状，GANs未来的发展趋势及面临的挑战主要体现在以下三个方面：

1.  **从“对抗”走向“融合”：** GANs在开放域高保真图像生成任务中的主导地位已被扩散模型取代。未来的趋势并非是GAN的消亡，而是其角色的转变。如D-WGAN所示，GAN的判别器可被用作一种强大的感知损失或稳定器，嵌入到 diffusione 或其他生成框架中，以提升生成细节的锐利度或加速采样。GAN正从一个独立的生成范式，演变为一个可插拔的“增强模块”。

2.  **深耕“小数据、高专业”的垂直领域：** 扩散模型通常依赖于海量数据进行预训练，这在许多数据稀缺但价值巨大的专业领域（如医疗、材料科学）难以实现。GANs，特别是CycleGAN这类适用于非配对数据的模型，显示出其在“小数据”场景下的独特优势 [www.medsci.cn](https://www.medsci.cn/article/show_article.do?id=8f69810082ba)。未来的研究将进一步集中于如何提升GAN在这类任务中的结构保真度和鲁棒性，使其成为特定领域不可或缺的工具。

3.  **生成模型理论的统一与边界模糊：** 各类生成模型（GAN、VAE、Flow、Diffusion）之间的理论界限正逐渐变得模糊。例如，多篇综述和研究已经揭示了扩散模型、分数匹配（Score Matching）和流模型（Flow Matching）之间的深层联系 [arxiv.org](https://arxiv.org/pdf/2511.13387)。GAN的对抗训练原理也可能被整合到这些更统一的数学框架中。未来的挑战与机遇在于，能否将GAN的博弈思想提炼并融入到一个统一的生成模型理论中，而非仅仅是架构层面的拼接。

#### **5. 结论**
在2022-2025年这一时间窗口内，生成对抗网络（GAN）的研究经历了深刻的范式转型。面对扩散模型在主流生成任务上的 압도적 우위，GAN的研究热点已从追求SOTA图像质量转向解决自身核心缺陷和深耕特定应用领域。一方面，与扩散模型结合的混合架构为解决GAN的训练不稳定性提供了新思路。另一方面，GANs在医学影像跨模态翻译等专业领域展现出强大的生命力和临床价值。展望未来，GAN将不再是孤立的生成模型，而是更多地作为一种关键组件或在特定场景下发挥作用，其发展将与整个生成模型领域的理论统一和应用深化紧密相连。

---

#### **6. 参考文献**
[1] Zhao H, Li W. Text-to-image Generation Model Based on Diffusion Wasserstein Generative Adversarial Networks[J]. Journal of Electronics & Information Technology, 2023. (*Cited via [jeit.ac.cn](https://jeit.ac.cn/cn/article/doi/10.11999/JEIT221400?viewType=HTML#:~:text=D%2DWGAN%E4%B8%8D%E4%BB%85%E8%83%BD%E5%A4%9F%E7%94%9F%E6%88%90,%E7%9A%84%E5%BD%A2%E6%80%81%E4%B9%9F%E6%9B%B4%E5%8A%A0%E7%9C%9F%E5%AE%9E%E3%80%82)*)
[2] Duan L, Dong Z, Yang L, et al. The use of generative adversarial networks to predict the physical outcomes of acne treatment[J]. Chinese Science Bulletin, 2025. (*Cited via [www.sciengine.com](https://www.sciengine.com/doi/pdfView/3F60D7C0D3AB4F3CBCE9D58860F60865)*)
[3] Wu F, et al. A Survey of Image Translation Based on Conditional Generative Adversarial Networks[J]. Journal of Computer-Aided Design & Computer Graphics, 2024. (*Cited via [www.jcad.cn](https://www.jcad.cn/article/doi/10.3724/SP.J.1089.2024.19807)*)
[4] Xiehe Medical Journal. Research progress of generative adversarial networks in cross-modal reconstruction of medical images[J]. MedSci.cn, 2024. (*Cited via [www.medsci.cn](https://www.medsci.cn/article/show_article.do?id=8f69810082ba)*)
[5] Qi S. Research Progress on Text-to-Image Diffusion Models Based on Layout Control[J]. Computer Science and Application, 2025. (*Cited via [pdf.hanspub.org](https://pdf.hanspub.org/csa2025154_451543569.pdf)*)
[6] Kong F. Generalized Denoising Diffusion Codebook Models (gDDCM): Tokenizing Images with Pre-trained Diffusion Models[J]. arXiv preprint, 2025. (*Cited via [arxiv.org](https://arxiv.org/pdf/2511.13387)*)
[7] Wang X, Darrell T, Rambhatla S S, et al. InstanceDiffusion: Instance-level Control for Image Generation[C]. CVPR, 2024. (*Cited via [chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/45330)*)
[8] A Survey on Generative Diffusion Model[J]. arXiv preprint, summarized by skycaiji.com, 2024. (*Cited via [www.skycaiji.com](https://www.skycaiji.com/aigc/ai9735.html)*)
[9] Zhu JY, Park T, Isola P, et al. Unpaired image-to-image translation using cycle-consistent adversarial networks[C]. Proc IEEE Comput Soc Vision Pattern Recognit, 2017. (*Cited in [www.medsci.cn](https://www.medsci.cn/article/show_article.do?id=8f69810082ba)*)
[10] Armanious K, Jiang C, Fischer M, et al. MedGAN: Medical image translation using GANs[J]. Comput Med Imag Grap, 2020. (*Cited in [www.medsci.cn](https://www.medsci.cn/article/show_article.do?id=8f69810082ba)*)
[11] Gao Y, Guo H, et al. Seedance 1.0: Exploring the Boundaries of Video Generation Models[R]. BAAI, 2025. (*Cited via [hub.baai.ac.cn](https://hub.baai.ac.cn/paper/81777871-7686-4770-9c3c-e65e0b0e9d8f)*)
[12] Ho J, Jain A, Abbeel P. Denoising diffusion probabilistic models[J]. Advances in neural information processing systems, 2020. (*Cited in [arxiv.org](https://arxiv.org/pdf/2511.13387)*)
[13] Radford A, Kim J W, Hallacy C, et al. Learning transferable visual models from natural language supervision[C]. The 38th International Conference on Machine Learning, 2021. (*Cited in [jeit.ac.cn](https://jeit.ac.cn/cn/article/doi/10.11999/JEIT221400?viewType=HTML#:~:text=D%2DWGAN%E4%B8%8D%E4%BB%85%E8%83%BD%E5%A4%9F%E7%94%9F%E6%88%90,%E7%9A%84%E5%BD%A2%E6%80%81%E4%B9%9F%E6%9B%B4%E5%8A%A0%E7%9C%9F%E5%AE%9E%E3%80%82)*)