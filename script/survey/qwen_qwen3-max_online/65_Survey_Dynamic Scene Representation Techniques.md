# 动态场景表示技术研究综述（2022–2025）

## 引言

动态场景表示旨在对随时间演化的三维环境进行结构化建模，支撑机器人导航、自动驾驶、虚拟现实等下游任务。不同于静态重建，动态表示需联合建模几何、外观、运动及语义的时空演化，其核心挑战在于数据稀疏、运动模糊、时序一致性以及开放词汇泛化等。2022 年以来，神经辐射场（NeRF）与 3D 高斯泼溅（3D Gaussian Splatting）的演进推动了该领域的范式迁移。本文综述 2022–2025 年间代表性工作，按技术路线分为四类：基于 NeRF 的隐式动态表示、基于高斯泼溅的显式动态建模、4D 语言场与开放词汇查询、以及弱监督与端到端动态图生成，并总结实验评价共性与未来趋势。

## 方法分类与代表作

### 1. 基于 NeRF 的隐式动态表示

早期工作延续 NeRF 框架，通过引入变形场建模动态性。**D-NeRF**（Pumarola et al., 2021）虽早于 2022 年，但其逆向映射（backward flow）范式在后续工作中被广泛沿用。**Nerfies**（Park et al., CVPR 2021）通过学习规范空间与观测空间的双向映射提升泛化，但在高速运动下易出现伪影。**EmerNeRF**（Yang et al., ICLR 2024）[iclr.cc](https://openreview.net/forum?id=ycv2z8TYur) 提出纯自监督的时空分解：将场景解耦为静态场、动态场与感应流场，无需动态分割或光流真值。其在传感器模拟中 PSNR 提升达 3.25 dB，且通过 2D 视觉基础模型（如 DINOv2）特征提升，占用预测准确率提高 78.5%。该方法证明了从野外视频中自举学习动态表示的可行性。

### 2. 基于高斯泼溅的显式动态建模

3D 高斯泼溅因实时渲染与高保真特性成为新范式。**Deformable 3D Gaussians**（Yang et al., CVPR 2024）[eet-china.com](https://www.eet-china.com/mp/a297533.html) 首次将可变形场与高斯联合优化，前向映射（forward flow）提升 D-NeRF 数据集 PSNR 超 10 点。其退火平滑训练（AST）机制有效缓解真实场景相机位姿噪声。**4D-GS**（Wu et al., 2023）[hub.baai.ac.cn](https://hub.baai.ac.cn/paper/2157451e-6f34-44f4-9a74-4f038d07f579) 提出 4D 神经体素与 3D 高斯联合表示，在 RTX 3090 上实现 82 FPS 实时渲染，显著优于 NeRF 系方法。**Event-guided 3D Gaussian Splatting**（Yin et al., 2025）[chatpaper.com](https://chatpaper.com/zh-CN/chatpaper/paper/191193) 引入事件相机数据，通过事件引导损失匹配亮度变化与事件流，在高速运动模糊场景下 LPIPS 降低 15% 以上，验证了多模态传感对动态建模的增益。

### 3. 4D 语言场与开放词汇查询

开放词汇动态理解是近年热点。**4D LangSplat**（Zhou et al., CVPR 2025）[hub.baai.ac.cn](https://hub.baai.ac.cn/view/44343) 利用多模态大模型（Qwen-7B）生成物体状态描述，再通过 e5-mistral 提取句子特征，替代 CLIP 的静态语义。其状态变形网络（Status Deformable Network）将语义变化建模为状态线性组合，确保时序平滑。在自建 HyperNeRF/Neu3D 动态查询数据集上，时间敏感查询 ACC 提升 29.03%，vIoU 提升 27.54%。**Learning 4D Panoptic Scene Graph**（Wu et al., 2025）[chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/122417) 提出 2D 到 4D 迁移学习框架，通过链式 LLM 推理利用开放词汇能力，在 4D-PSG 基准上显著超越基线，缓解了 4D 数据稀缺与词汇外问题。

### 4. 弱监督与端到端动态图生成

动态场景图（DSG）生成关注物体关系建模。**TRKT**（Xu et al., ICCV 2025）[thepaper.cn](https://m.thepaper.cn/newsDetail_forward_31534960) 指出弱监督 DSG 的瓶颈在于静态检测器在动态场景中定位不准。其提出时序增强关系敏感注意力图，通过双流融合模块提升检测 AP 13.0%，最终 SGDET Recall@50 提升 2.42%。**3DET-Mamba**（Li et al., NeurIPS 2024）[chatpaper.com](https://chatpaper.com/chatpaper/zh-CN/paper/79995) 首次将状态空间模型（Mamba）引入 3D 检测，设计 Inner/Dual/Query-aware Mamba 模块，在 ScanNet 上 AP@0.25 达 70.4%，超越 3DETR 5.4 个百分点。**DetAny4D**（Hou et al., 2025）[blog.csdn.net](https://blog.csdn.net/weixin_49587977/article/details/154842120) 构建大规模 DA4D 数据集，并提出因果注意力解码器实现端到端 4D 检测，时序抖动（边界框方差）降低 15–20%，解决逐帧检测的不一致性问题。

## 实验与评价总结

共性实验结论可归纳为三点：  
1. **表示效率与质量权衡**：显式方法（如 3D 高斯）在渲染速度（>60 FPS）与几何保真度（PSNR >35 dB）上全面优于隐式 NeRF，但内存占用更高；  
2. **时序一致性成为新指标**：除 PSNR/SSIM/LPIPS 外，边界框时序方差（Var）、运动轨迹平滑度（Jerk）等被广泛采用，以量化动态稳定性；  
3. **数据驱动范式主导**：无论是自监督（EmerNeRF）、弱监督（TRKT）还是大规模合成（DetAny4D），高质量动态数据集的构建是性能突破的前提，而多模态先验（如深度、事件、语言）显著提升泛化。

## 趋势与挑战

基于 2025 年前后进展，可预测以下趋势：  
1. **统一 4D 基础模型兴起**：如 Depth Anything 3（ByteDance, 2025）[blog.csdn.net](https://blog.csdn.net/weixin_49587977/article/details/154842120) 以单一 Transformer 架构统一深度、位姿、渲染任务，预示动态场景表示将向多任务、少专家模型演进；  
2. **物理可执行性成为新目标**：PhysX-Anything（Cao et al., 2025）[blog.csdn.net](https://blog.csdn.net/weixin_49587977/article/details/154842120) 与 URDF-Anything（2025）[blog.csdn.net](https://blog.csdn.net/weixin_49587977/article/details/154842120) 证明，生成模型需输出可直接用于仿真的物理参数（密度、关节、URDF），而非仅几何外观；  
3. **程序化生成与符号修正融合**：Procedural Scene Programs（Gumin et al., SIGGRAPH Asia 2025）[arxiv.org](https://arxiv.org/abs/2510.16147) 通过程序语言生成场景并自动纠错，为解决重叠、漂浮等几何错误提供新路径，预示“神经+符号”混合范式将成为高保真动态世界构建的关键。

## 结论

2022–2025 年，动态场景表示技术从隐式 NeRF 迁移至显式高斯泼溅，并深度融合语言、事件、物理等多模态先验。核心进展体现在实时渲染、时序一致、开放词汇与物理可执行四个维度。未来研究需在统一基础模型、物理仿真就绪、程序化可控三方面突破，以支撑具身智能与数字孪生等高阶应用。

## 参考文献

1. Yang, J., et al. (2024). EmerNeRF: Emergent Spatial-Temporal Scene Decomposition via Self-Supervision. *ICLR*. [https://openreview.net/forum?id=ycv2z8TYur](https://openreview.net/forum?id=ycv2z8TYur)  
2. Yang, Z., et al. (2024). Deformable 3D Gaussians for High-Fidelity Monocular Dynamic Scene Reconstruction. *CVPR*. [https://arxiv.org/abs/2309.13101](https://arxiv.org/abs/2309.13101)  
3. Wu, G., et al. (2023). 4D Gaussian Splatting for Real-Time Dynamic Scene Rendering. *arXiv:2310.08528*. [https://hub.baai.ac.cn/paper/2157451e-6f34-44f4-9a74-4f038d07f579](https://hub.baai.ac.cn/paper/2157451e-6f34-44f4-9a74-4f038d07f579)  
4. Yin, X., et al. (2025). Event-guided 3D Gaussian Splatting for Dynamic Human and Scene Reconstruction. *arXiv:2509.18566*. [https://chatpaper.com/zh-CN/chatpaper/paper/191193](https://chatpaper.com/zh-CN/chatpaper/paper/191193)  
5. Zhou, R., et al. (2025). 4D LangSplat: Dynamic Semantic Fields for Open-Vocabulary Temporal Queries. *CVPR*. [https://arxiv.org/abs/2503.10437](https://hub.baai.ac.cn/view/44343)  
6. Wu, S., et al. (2025). Learning 4D Panoptic Scene Graph Generation from Rich 2D Visual Scene. *arXiv:2503.15019*. [https://chatpaper.com/chatpaper/zh-CN/paper/122417](https://chatpaper.com/chatpaper/zh-CN/paper/122417)  
7. Xu, Z., et al. (2025). TRKT: Weakly Supervised Dynamic Scene Graph Generation with Temporal-enhanced Relation-aware Knowledge Transferring. *ICCV*. [https://arxiv.org/abs/2508.04943](https://m.thepaper.cn/newsDetail_forward_31534960)  
8. Li, M., et al. (2024). 3DET-Mamba: Causal Sequence Modelling for End-to-End 3D Object Detection. *NeurIPS*. [https://openreview.net/forum?id=RVVPxVuwae](https://chatpaper.com/chatpaper/zh-CN/paper/79995)  
9. Hou, J., et al. (2025). DetAny4D: Detect Anything 4D Temporally in a Streaming RGB Video. *arXiv:2511.18814*. [https://blog.csdn.net/weixin_49587977/article/details/154842120](https://blog.csdn.net/weixin_49587977/article/details/154842120)  
10. Cao, Z., et al. (2025). PhysX-Anything: Simulation-Ready Physical 3D Assets from Single Image. *arXiv:2511.13648*. [https://blog.csdn.net/weixin_49587977/article/details/154842120](https://blog.csdn.net/weixin_49587977/article/details/154842120)  
11. Gumin, M., et al. (2025). Procedural Scene Programs for Open-Universe Scene Generation: LLM-Free Error Correction via Program Search. *SIGGRAPH Asia*. [https://arxiv.org/abs/2510.16147](https://arxiv.org/abs/2510.16147)  
12. ByteDance Seed Team. (2025). Depth Anything 3: Recovering the Visual Space from Any Views. *arXiv:2511.10647*. [https://blog.csdn.net/weixin_49587977/article/details/154842120](https://blog.csdn.net/weixin_49587977/article/details/154842120)