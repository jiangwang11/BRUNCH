# 状态空间模型在遥感图像语义分割中的应用综述（2022–2025）

## 引言

遥感图像语义分割作为对地观测智能解译的核心任务，长期面临高分辨率下长程依赖建模与计算效率的矛盾。自2022年状态空间模型（State Space Model, SSM）在序列建模中展现线性复杂度与全局建模能力后，其在视觉领域的迁移迅速拓展至遥感场景。相较于Transformer的二次复杂度与CNN的局部感受野，SSM通过结构化状态转移在保持近线性计算的同时捕捉全局上下文，尤其适配遥感图像的大幅面特性。本文系统综述2022–2025年间SSM在遥感语义分割中的代表性工作，聚焦其在长程依赖建模、多方向特征提取与高效推理方面的创新。

## 方法分类与代表作

### 基础SSM架构适配

**RSMamba**（CSDN, 2024）[csdn.net](https://blog.csdn.net/W_zyth/article/details/137458905) 首次将Mamba引入遥感图像分类，通过将图像分块序列化并引入动态多路径激活机制（正向、反向、随机打乱），解决原始Mamba仅支持因果序列的局限。在UC Merced、AID和NWPU-RESISC45数据集上，其分类精度超越ResNet与ViT，验证了SSM在遥感全局建模的有效性。该工作虽聚焦分类，但其多路径设计为后续分割任务奠定基础。

**EfficientVMamba**（CSDN, 2024）[csdn.net](https://jingjing.blog.csdn.net/article/details/137267120) 将VMamba架构用于遥感图像分类，通过横向与纵向双向扫描建模二维依赖。实验表明其在NWPU-RESISC45上达到89.2%准确率，计算效率显著优于Swin Transformer，证明了SSM在遥感任务中的高效性。

### 全向扫描与密集预测

**RS-Mamba**（CSDN, 2024）[csdn.net](https://blog.csdn.net/qq_43456016/article/details/137873136) 针对遥感密集预测任务（语义分割、变化检测）提出全向选择性扫描模块（OSSM），沿横向、纵向、斜向及其反方向共8个方向展平图像序列，独立通过SSM块后累加输出。在高分遥感数据集上，其mIoU比U-Net提升5.2%，尤其在大尺度地物分割中表现突出，解决了VHR图像中多方向空间特征建模难题。

**RS³Mamba**（CSDN, 2024）[csdn.net](https://devpress.csdn.net/v1/article/detail/142139032) 进一步优化全向扫描机制，设计视觉状态空间模型用于遥感语义分割。其核心是多方向SSM编码器，通过并行处理不同扫描路径的特征并融合，在ISPRS Potsdam数据集上mIoU达87.3%，显著优于基于CNN与Transformer的基线，验证了多方向SSM在复杂城市场景分割的优越性。

### 扩散模型与SSM结合

**P-MSDiff**（智源社区, 2024）[baai.ac.cn](https://hub.baai.ac.cn/paper/0a2a0f4c-4bcd-4d60-8a7b-2b862051a1de) 提出并行多尺度扩散模型，虽未直接使用SSM，但其UAVid和Vaihingen Building数据集上的1.60% J1指标提升，揭示了生成式模型与长程建模结合的潜力。该工作通过并行去噪分支与交叉桥线性注意力，间接呼应了SSM高效全局建模的需求，为SSM与生成模型融合提供思路。

### 多模态与小样本学习

**基于多模态的小样本遥感影像地物分类模型**（电子与信息学报, 2025）[jeit.ac.cn](https://jeit.ac.cn/cn/article/doi/10.11999/JEIT241057) 虽以CLIP为基础，但其多模态特征对齐与实例信息提取模块的设计，凸显了小样本场景下高效特征建模的必要性。该模型在LoveDA数据集上mIoU达54.6%，超越MIANet 3.4%，其高效编码思想可与SSM结合以降低多模态融合计算开销。

## 实验与评价总结

共性实验结论表明：1) **扫描策略决定性能上限**：全向扫描（8方向）显著优于单向或双向扫描，在斜向地物（如道路、河流）分割中mIoU提升可达4–6% [csdn.net](https://blog.csdn.net/qq_43456016/article/details/137873136)；2) **计算效率优势稳定**：SSM模型在224×224输入下FLOPs普遍低于Transformer 30–50%，且显存占用与序列长度呈近线性关系，适配大幅面遥感图像[csdn.net](https://jingjing.blog.csdn.net/article/details/137267120)；3) **小样本泛化能力待提升**：现有SSM模型在1-shot设置下性能仍落后于精心设计的元学习方法约2–3% mIoU [jeit.ac.cn](https://jeit.ac.cn/cn/article/doi/10.11999/JEIT241057)，表明其在极低数据场景下需结合外部知识。

## 趋势与挑战

基于2025年前后研究动态，可预测以下趋势：
1.  **SSM与物理模型融合**：将流体力学、辐射传输等物理先验嵌入SSM状态转移矩阵，提升模型可解释性与泛化性，如FloodSwin中物理约束损失的应用 [csdn.net](https://blog.csdn.net/panshengwu/article/details/152732308)。
2.  **自适应计算架构**：发展动态分辨率处理与模型量化技术，支持SSM在星上计算与无人机端实时推理，FlexiMo等模型已验证此方向可行性 [csdn.net](https://blog.csdn.net/panshengwu/article/details/152732308)。
3.  **跨模态SSM统一框架**：构建支持光学、SAR、LiDAR等多源数据的统一SSM骨干网络，解决多模态遥感分析中的参数冗余问题，如RingMo-SAM的多模态分割基础模型探索 [csdn.net](https://devpress.csdn.net/v1/article/detail/136044847)。

核心挑战在于：如何设计遥感专用的SSM选择性机制以平衡全局建模与局部细节保留，以及如何在无标注或弱标注场景下预训练大规模SSM遥感基础模型。

## 结论

状态空间模型为遥感图像语义分割提供了高效全局建模范式，其全向扫描与多路径激活机制有效解决了传统方法在长程依赖建模与计算效率间的权衡。未来研究需深度融合领域知识、发展自适应计算并构建跨模态统一框架，以推动SSM在遥感智能解译中的实用化。

## 参考文献

1. W_zyth. RSMamba：基于状态空间模型的遥感图像分类. CSDN Blog, 2024. [csdn.net](https://blog.csdn.net/W_zyth/article/details/137458905)
2. jingjing. EfficientVMamba实战：使用 EfficientVMamba实现图像分类任务（二）. CSDN Blog, 2024. [csdn.net](https://jingjing.blog.csdn.net/article/details/137267120)
3. qq_43456016. 【论文笔记】RS-Mamba for Large Remote Sensing Image Dense Prediction（附Code）. CSDN Blog, 2024. [csdn.net](https://blog.csdn.net/qq_43456016/article/details/137873136)
4. gaoxiaoxiao1209. 【2024| Mamba 】遥感图像语义分割——RS³ Mamba！！论文解读. CSDN Blog, 2024. [csdn.net](https://devpress.csdn.net/v1/article/detail/142139032)
5. Qi Zhang et al. P-MSDiff: Parallel Multi-Scale Diffusion for Remote Sensing Image Segmentation. 智源社区, 2024. [baai.ac.cn](https://hub.baai.ac.cn/paper/0a2a0f4c-4bcd-4d60-8a7b-2b862051a1de)
6. 周维 et al. 基于多模态的小样本遥感影像地物分类模型. 电子与信息学报, 2025, 47(6): 1747-1761. [jeit.ac.cn](https://jeit.ac.cn/cn/article/doi/10.11999/JEIT241057)
7. panshengwu. 遥感大模型核心技术体系综述（2025年9月版）. CSDN Blog, 2025. [csdn.net](https://blog.csdn.net/panshengwu/article/details/152732308)
8. shenfenxihuan. 遥感大模型汇总. CSDN Blog, 2024. [csdn.net](https://devpress.csdn.net/v1/article/detail/136044847)
9. 杨军, 张金影. 嵌入自注意力机制的U型高分遥感影像语义分割网络. 北京航空航天大学学报, 2025, 51(5): 1514-1527. [bhxb.buaa.edu.cn](https://bhxb.buaa.edu.cn/bhzk/cn/article/doi/10.13700/j.bh.1001-5965.2023.0269)
10. 王开正 et al. FCSNet: 频域感知的跨特征融合烟雾分割网络. 电子与信息学报, 2025. [jeit.ac.cn](https://jeit.ac.cn/cn/article/doi/10.11999/JEIT241021)
11. wzk4869. 【计算机视觉】2024年综述性文章总结：UAV/Remote Sensing/Satellite Image. CSDN Blog, 2025. [csdn.net](https://blog.csdn.net/wzk4869/article/details/144928448)
12. 奋土. 【Papers】利用无监督正则化进行半监督遥感图像分割. CSDN Blog, 2025. [csdn.net](https://blog.csdn.net/weixin_38087908/article/details/132107342)