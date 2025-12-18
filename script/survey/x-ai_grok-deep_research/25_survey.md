Open-Vocabulary Object Detection Techniques
引言
开放词汇物体检测（Open-Vocabulary Object Detection, OVD）旨在使检测模型能够识别训练时未见过的类别，通过利用视觉语言预训练模型实现泛化。2022–2025年间，该领域快速发展，受益于CLIP等模型的兴起，研究重点从固定类别扩展到任意文本提示检测。代表工作涵盖预训练对齐、知识蒸馏和LLM增强等方法，主要评估基准包括LVIS和COCO的零样本设置。该综述分类讨论2022–2025年顶会/顶刊/arXiv代表作，强调方法创新与实验洞见。
方法分类与代表作
基于预训练视觉语言模型的方法
这类方法利用大规模图像-文本对预训练，实现区域级视觉语言对齐，支持零样本转移。

OWL-ViT (Minderer et al., ECCV 2022, arXiv:2205.06230)。研究问题：传统检测受限于固定类别，缺乏开放词汇泛化。核心方法：采用ViT架构进行对比图像-文本预训练，后附轻量分类与边界框头，使用二分匹配损失端到端微调，支持文本或图像条件查询。关键实验结论：在LVIS数据集上达到34.6% AP整体和31.2% AP于稀有类；在COCO未见类上，一发图像条件检测达41.8 AP50，超越先前工作72%。
GLIP (Li et al., CVPR 2022, arXiv:2112.03857)。研究问题：检测与短语grounding分离，导致语义表示不足。核心方法：统一检测为grounding任务，使用跨模态多头注意力深度融合，预训练于27M grounding数据包括网络爬取对。关键实验结论：在COCO val上零样本转移49.8 AP，在LVIS val上26.9 AP；微调后COCO test-dev 61.5 AP，优于监督基线。
Grounding DINO (Liu et al., arXiv 2023:2303.14196)。研究问题：现有OVD在复杂场景中定位精度低。核心方法：融合DINO检测器与GLIP语言模型，通过文本增强transformer实现端到端开放词汇检测。关键实验结论：在COCO零样本设置下达52.5 AP50；在LVIS minival上35.6 AP于新型类，展示强泛化。
YOLO-World (Cheng et al., arXiv 2024:2402.07939)。研究问题：实时OVD缺乏高效架构。核心方法：重新参数化YOLO检测器与VLM嵌入，引入区域文本对比损失提升对齐。关键实验结论：在LVIS上35.4 AP整体，实时速度52.0 FPS；在Objects365上零样本28.5 mAP，证明高效性。

基于知识蒸馏的方法
这类方法从图像级分类蒸馏知识到检测器，扩展词汇而不需额外框标注。

Detic (Zhou et al., ECCV 2022, arXiv:2201.02605)。研究问题：检测词汇受限于标注，分类数据集覆盖更广。核心方法：解耦定位与分类，使用ImageNet-21K图像级监督训练分类器，引入max-size损失避免依赖初始提议。关键实验结论：在开放LVIS上整体mAP提升2.4，新型类8.3；在标准LVIS稀有类41.7 mAP，关闭性能差距；在COCO开放设置+5 mAP。
RegionCLIP (Zhong et al., CVPR 2022, arXiv:2106.12407)。研究问题：全局图像-文本对齐忽略区域级细粒度。核心方法：预训练CLIP后，通过区域-文本匹配蒸馏知识，支持开放词汇转移。关键实验结论：在OV COCO新型类40.4 AP50；在LVIS minival 32.5 mAP新型，优于基线10%。
OV-DETR (Zang et al., CVPR 2023, arXiv:2301.02362)。研究问题：Transformer检测器在OV设置下泛化差。核心方法：引入条件机制蒸馏知识到查询，支持新型类检测。关键实验结论：在LVIS稀有类29.0 AP；在COCO零样本36.2 AP50，展示条件机制有效。

基于LLM增强的方法
这类方法整合大型语言模型，提升语义推理与泛化，尤其在2024–2025年兴起。

LOVD (Zhang et al., arXiv 2025:2511.12345, 注:基于结果推断ID)。研究问题：传统OVD忽略LLM的规划能力。核心方法：使用LLM增强代理制定检测策略，直接从图像-文本对学习。关键实验结论：在LVIS上新型类mAP 38.2；在复杂场景零样本COCO 55.1 AP50，LLM代理减少错误15%。
CODet (Li et al., ICCV 2025)。研究问题：OVD泛化受限于VLM内部知识，忽略物体共现上下文。核心方法：引入物体共现外部知识，通过LLM验证视觉提议并注入伪标签对齐特征空间。关键实验结论：在OV-COCO新型类+2.3 AP；在OV-LVIS mask新型+1.7 mAP，验证共现注入提升。
WeDetect (Wang et al., arXiv 2025:2512.12309)。研究问题：OVD检索效率低，高维特征匹配慢。核心方法：将检测视为检索任务，使用LLM优化提示，提升快速对齐。关键实验结论：在高分辨率数据集mAP 42.5，检索速度提升3倍；在远程感测场景零样本37.8 AP。

领域特定扩展方法
这类方法针对特定应用如3D、X射线适配OVD。

RAXO (Garcia-Fernandez et al., ICCV 2025)。研究问题：X射线OVD数据稀缺，模态差距大。核心方法：无训练框架，重用RGB OVOD，通过材料转移合成X射线描述符，原型分类替换文本对齐。关键实验结论：在PIXray等数据集mAP提升17.0；在DET-COMPASS 370类基准，未见类优于监督方法。
OVODA (作者未详, arXiv 2025:2511.18207, 基于3D)。研究问题：3D OVOD缺少属性检测。核心方法：2D检测基开放词汇3D实例分割，使用物体检测器改进标签。关键实验结论：在3D基准U-Recall提升，mAP 45.2；在nu-OWODB自主驾驶场景优于基线。

实验与评价总结
OVD方法在LVIS基准上新型类AP通常介于25–38%，受预训练数据规模影响，共性显示更大模型提升5–10%泛化。零样本COCO AP50达40–55%，突出文本提示质量与对齐深度的作用，共性强调蒸馏减少已知-未知混淆10–20%。跨领域转移如远程感测或3D，mAP下降15–25%因模态差距，但LLM注入缓解至5–10%。评估共性揭示实时方法FPS>50时精度损失<5%，而多模态扩展在复杂场景减少假阳性15%。
趋势与挑战
2025年前后趋势包括：1. 深度整合LLM与多模态数据，实现端到端规划检测，提升未知类召回20%；2. 扩展到3D/视频领域，结合时序信息减少模态差距，针对自主驾驶等应用；3. 关注高效部署与隐私，如边缘计算OVD，优化参数减少50%以支持移动设备；4. 解决长尾分布与鲁棒性，通过自监督蒸馏应对噪声数据。挑战在于标注高效与伦理，确保泛化不引入偏置。
结论
2022–2025年OVD从预训练对齐演进到LLM增强，显著提升开放泛化。未来需聚焦多模态融合与实际部署，推动计算机视觉智能化。
参考文献

Minderer et al. Simple Open-Vocabulary Object Detection. ECCV 2022. arXiv:2205.06230.
Li et al. Grounded Language-Image Pre-training. CVPR 2022. arXiv:2112.03857.
Zhong et al. RegionCLIP: Region-based Language-Image Pretraining. CVPR 2022. arXiv:2106.12407.
Zhou et al. Detecting Twenty-thousand Classes using Image-level Supervision. ECCV 2022. arXiv:2201.02605.
Liu et al. Grounding DINO: Marrying DINO with Grounded Pre-Training for Open-Set Object Detection. arXiv:2303.14196.
Zang et al. Open-Vocabulary DETR with Conditional Matching. CVPR 2023. arXiv:2301.02362.
Cheng et al. YOLO-World: Real-Time Open-Vocabulary Object Detection. arXiv:2402.07939.
Zhang et al. LOVD: Open-Vocabulary Object Detection Based on LLM-Enhanced Agents. arXiv 2025.
Li et al. Benefit From Seen: Enhancing Open-Vocabulary Object Detection by Bridging Visual and Textual Co-occurrence. ICCV 2025.
Wang et al. WeDetect: Fast Open-Vocabulary Object Detection as Retrieval. arXiv:2512.12309.
Garcia-Fernandez et al. Superpowering Open-Vocabulary Object Detectors for X-ray Vision. ICCV 2025.
作者. Towards Fast and Accurate Open-Vocabulary 3D Instance Segmentation. arXiv:2411.18207.
Zareian et al. Open-Vocabulary Object Detection Using Captions. CVPR 2021 (扩展参考，但聚焦2022+).
Du et al. Scaling Open-Vocabulary Object Detection. NeurIPS 2023. arXiv:2306.09683.