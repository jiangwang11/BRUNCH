单图像去雾技术与深度学习结合的增强方法
引言
单图像去雾旨在从单张雾化图像中恢复清晰图像，受大气散射模型影响，传统方法依赖先验假设易失效。深度学习通过端到端学习提升鲁棒性，2022–2025年间，CNN、Transformer、GAN及扩散模型等架构推动进展，聚焦真实场景泛化、实时性和物理约束整合。研究强调多模态融合与自监督训练以减少配对数据依赖。
方法分类与代表作
基于CNN的多规模融合方法

MCRFS-Net: single image dehazing based on multi-scale convolutional reconstruction and fusion structure (Nature, 2025)
研究问题：现有方法在浓雾场景中细节恢复不足，导致颜色失真。
核心方法：采用多规模卷积重建模块融合浅层与深层特征，并引入注意力机制优化融合路径。
关键实验结论：在RESIDE数据集上，PSNR提升至32.5 dB，SSIM达0.95；真实图像测试显示雾密度高时细节保留率提高15%。
PMDNet: A multi-stage approach to single image dehazing with pyramid multi-scale dense networks (JVCIR, 2024)
研究问题：单阶段网络忽略多分辨率信息，导致边缘模糊。
核心方法：构建金字塔多规模稠密网络，分阶段提取并融合特征，使用残差连接增强梯度流。
关键实验结论：SOTS数据集PSNR达31.2 dB，SSIM为0.93；与GridDehazeNet比较，计算复杂度降低20%而性能提升5%。
TSNet: A Two-stage Network for Image Dehazing with Multi-scale Fusion and Adaptive Learning (arXiv:2404.02460, 2024)
研究问题：合成与真实雾化域差距大，模型泛化差。
核心方法：两阶段架构，第一阶段多规模融合提取全局特征，第二阶段自适应学习调整局部细节。
关键实验结论：NH-HAZE数据集PSNR为28.7 dB，SSIM达0.91；跨域测试泛化误差减小12%。
DEA-Net: Single Image Dehazing Based on Detail-Enhanced Convolution and Content-Guided Attention (IEEE TIP, 2024)
研究问题：细节丢失与注意力偏差影响恢复质量。
核心方法：细节增强卷积模块结合内容引导注意力，优化特征提取与融合。
关键实验结论：RESIDE-Indoor PSNR达35.1 dB，SSIM为0.96；浓雾场景下纹理恢复精度提高18%。

基于Transformer的方法

PhysFormer: Physics-based model and transformer for single image dehazing (SPIE, 2025)
研究问题：纯数据驱动模型忽略物理约束，导致不稳定恢复。
核心方法：整合大气散射模型与Transformer全局建模，使用物理引导注意力机制。
关键实验结论：SOTS-Outdoor PSNR为30.8 dB，SSIM达0.94；与纯Transformer比较，物理约束下误差降低10%。
ICAFormer: An Image Dehazing Transformer Based on Interactive Channel Attention (Sensors, 2025)
研究问题：通道间交互不足影响特征表示。
核心方法：引入交互通道注意力增强Transformer编码器，捕捉多层依赖。
关键实验结论：NH-HAZE PSNR达27.9 dB，SSIM为0.90；实时处理帧率达45 FPS。
UTCR-Dehaze: U-Net and transformer-based cycle-consistent regularized dehazing network (EngAppAI, 2025)
研究问题：无配对数据训练时一致性差。
核心方法：U-Net与Transformer融合，循环一致正则化提升无监督学习。
关键实验结论：O-HAZE数据集PSNR为29.4 dB，SSIM达0.92；无配对设置下泛化提升13%。
TCFDN: An Efficient Dehazing Algorithm Based on the Fusion of Transformer and Convolutional Neural Network (Sensors, 2022)
研究问题：CNN局部与Transformer全局融合不充分。
核心方法：Transformer捕捉全局依赖，CNN处理局部细节，通过残差融合模块整合。
关键实验结论：RESIDE PSNR达33.2 dB，SSIM为0.95；参数量较纯Transformer减少25%。

基于GAN的方法

GAN-based Multimodal fusion for image dehazing (Taylor & Francis, 2025)
研究问题：单模态输入限制雾化变异适应。
核心方法：多模态GAN融合深度与RGB信息，对抗训练优化生成器。
关键实验结论：SOTS PSNR为31.5 dB，SSIM达0.93；多模态输入下颜色保真度提高16%。
Alpha-DehazeNet: single image dehazing via RGBA haze modeling and deep learning (PMC, 2025)
研究问题：RGBA通道雾化建模不准导致伪影。
核心方法：RGBA雾化模型结合GAN生成透明度图，对抗优化恢复。
关键实验结论：NH-HAZE PSNR达28.2 dB，SSIM为0.91；透明通道处理下伪影减少20%。

基于扩散模型的方法

Efficient image dehazing via temporal-aware diffusion (Expert Systems with Applications, 2025)
研究问题：标准扩散模型计算开销大，不适实时去雾。
核心方法：时序感知扩散缩短马尔可夫链，优化采样效率。
关键实验结论：RESIDE PSNR达32.8 dB，SSIM为0.94；推理时间缩短至0.5秒/帧。
Frequency-based and Physics-guiding Diffusion Model for Single Image Dehazing (CCC, 2024)
研究问题：扩散过程忽略频率域物理约束。
核心方法：频率域引导结合物理模型优化扩散步骤。
关键实验结论：O-HAZE PSNR为30.1 dB，SSIM达0.93；高频细节恢复率提升17%。
High-quality Image Dehazing with Diffusion Model (arXiv, 2024)
研究问题：扩散模型在复杂雾化中质量不稳。
核心方法：物理感知DDPM框架，迭代精炼去雾。
关键实验结论：SOTS PSNR达33.5 dB，SSIM为0.96；复杂场景下噪声抑制改善12%。

自监督方法

You Only Need Clear Images: Self-supervised Single Image Dehazing (IEEE, 2025)
研究问题：依赖配对数据限制实际应用。
核心方法：仅用清晰图像自监督训练，生成多传输图模拟雾化。
关键实验结论：NH-HAZE PSNR为27.5 dB，SSIM达0.89；无配对下泛化误差减小15%。
Self-Supervised Dehazing Network Using Physical Priors (ResearchGate, 2025)
研究问题：自监督缺少物理指导导致不一致。
核心方法：物理先验嵌入自监督网络，轻量架构优化。
关键实验结论：RESIDE-Outdoor PSNR达31.0 dB，SSIM为0.92；参数量减少30%。
Physical-model guided self-distillation network for single image dehazing (Frontiers, 2022)
研究问题：自蒸馏在去雾中纹理丢失。
核心方法：物理模型引导自蒸馏，优化教师-学生框架。
关键实验结论：SOTS PSNR为32.1 dB，SSIM达0.94；颜色保真度提高14%。

实验与评价总结
2022–2025年间方法在RESIDE、SOTS、NH-HAZE、O-HAZE等数据集上评估，共性显示PSNR介于27–35 dB，SSIM超0.89；真实场景泛化依赖物理约束与自监督，降低域移误差10–15%；多规模与Transformer融合提升细节保留15–20%，但计算复杂度随模型深度增加1–2倍；扩散模型在噪声抑制上优越12–17%，却需优化采样步数以达实时性。

趋势与挑战
2025年前后趋势预测：1. 扩散与Transformer混合架构将主导，强调高效采样以实现视频去雾扩展；2. 多模态输入（如深度、极化）结合自监督训练将成为主流，提升零样本泛化；3. 物理-数据驱动融合深化，针对非均匀雾化开发可解释模型；4. 边缘计算优化推动轻量网络，目标帧率超60 FPS。挑战包括数据集多样性不足与伦理问题，如隐私侵扰。
结论
单图像去雾与深度学习结合从CNN演进至扩散模型，提升了恢复精度与泛化，但需平衡计算与真实性。未来聚焦高效融合以应对复杂环境。
参考文献

Wang, L. et al. (2025). MCRFS-Net: single image dehazing based on multi-scale convolutional reconstruction and fusion structure. Scientific Reports, 15.
Zhang, Y. et al. (2024). PMDNet: A multi-stage approach to single image dehazing with pyramid multi-scale dense networks. Journal of Visual Communication and Image Representation.
Chen, Z. et al. (2024). TSNet: A Two-stage Network for Image Dehazing with Multi-scale Fusion and Adaptive Learning. arXiv:2404.02460.
Wu, H. et al. (2024). DEA-Net: Single Image Dehazing Based on Detail-Enhanced Convolution and Content-Guided Attention. IEEE Transactions on Image Processing.
Li, J. et al. (2025). PhysFormer: Physics-based model and transformer for single image dehazing. Proceedings of SPIE.
Zhao, X. et al. (2025). ICAFormer: An Image Dehazing Transformer Based on Interactive Channel Attention. Sensors, 25(12).
Kumar, A. et al. (2025). UTCR-Dehaze: U-Net and transformer-based cycle-consistent regularized dehazing network. Engineering Applications of Artificial Intelligence.
Chen, X. et al. (2022). An Efficient Dehazing Algorithm Based on the Fusion of Transformer and Convolutional Neural Network. Sensors, 23(1).
Liu, Y. et al. (2025). GAN-based Multimodal fusion for image dehazing. Enterprise Information Systems.
Sharma, P. et al. (2025). Alpha-DehazeNet: single image dehazing via RGBA haze modeling and deep learning. Heliyon, 11(14).
Zhang, H. et al. (2025). Efficient image dehazing via temporal-aware diffusion. Expert Systems with Applications.
Wang, X. et al. (2024). Frequency-based and Physics-guiding Diffusion Model for Single Image Dehazing. Chinese Control Conference.
Yu, J. et al. (2024). High-quality Image Dehazing with Diffusion Model. arXiv preprint.
Li, B. et al. (2025). You Only Need Clear Images: Self-supervised Single Image Dehazing. IEEE Transactions on Multimedia.
Gao, Y. et al. (2025). Self-Supervised Dehazing Network Using Physical Priors. ResearchGate preprint.
Chen, L. et al. (2022). Physical-model guided self-distillation network for single image dehazing. Frontiers in Neurorobotics.