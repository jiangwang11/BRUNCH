# 云医疗物联网系统中的异常检测：方法、评价与趋势（2022–2025）

## 引言

云医疗物联网（Cloud-based Medical IoT, CM-IoT）系统将可穿戴/植入式医疗设备、边缘计算节点与云端分析平台集成，实现远程患者监测、早期疾病预警与智能诊疗。然而，其异构性、资源受限性及高敏感性使系统易受数据篡改、设备劫持、服务拒绝等攻击，亦会因传感器漂移或配置错误产生非恶意异常。2022–2025年间，研究聚焦于在数据标签稀缺、类别极度不平衡、隐私约束严格、设备行为异构等挑战下，构建高精度、低延迟、可解释的异常检测机制。本文系统梳理该方向近三年代表性工作，按方法范式分类评述，并总结实验规律与未来趋势。

## 方法分类与代表作

### 基于自编码器与单分类学习的方法

自编码器（AutoEncoder, AE）及其变体在医疗异常检测中广受青睐，因其能以无监督方式学习正常生理信号的紧凑表示，通过重构误差判别异常。

张月等 \[arocmag.cn\] 提出 **GB-AEnet-FL**，针对物联网设备异常数据稀少与分布异构问题，在潜在特征层引入对抗训练与一致性约束，并通过主动学习重构异常样本以均衡正负类。其在四个IoT数据集上验证，F1分数平均提升4.2%，且联邦学习机制有效保护隐私并加速收敛。

阿里云开发者社区 \[developer.aliyun.com\] 提出 **双阶段医疗异常检测架构**：首先使用3D Residual AutoEncoder对CT/MRI体数据进行无监督特征压缩，再在潜在空间部署ν-SVM单分类器。该方法在脑卒中检测任务中AUC达0.923，假阳性率降低38%，端到端推理时间<800ms，显著优于3D U-Net。

Kitsune \[jos.org.cn\] 是一个通用入侵检测框架，采用多层堆叠自编码器重建网络流量特征向量，以重建误差作为异常评分。在IoT Botnet流量检测中，其F1-score达0.98，证明了AE在高维时序流量建模中的有效性。

### 基于生成对抗网络（GAN）的方法

GAN通过生成器-判别器对抗训练，能更精细地刻画正常数据流形，对偏离流形的异常更敏感。

唐伦等 \[jeit.ac.cn\] 提出 **MCBiWGAN-GTN**，专为云服务器KPI异常检测设计。该方法首先用CEEMDAN将多维时间序列分解为多个本征模态，再通过图卷积（GCN）与时间卷积（TCN）融合的GTN模块提取时空特征，最后以半监督BiWGAN识别异常。在Clearwater和MBD数据集上，F1-score分别达0.960和0.630，显著优于MAD-GAN等基线。

Meidan等 \[jos.org.cn\] 提出 **N-BaIoT**，利用深度自编码器检测被僵尸网络感染的IoT设备。其对正常流量建模后，攻击流量的重建误差显著增大。在实测Mirai攻击流量上，检测准确率超98%，验证了AE在识别恶意指令注入的有效性。

### 基于图神经网络与注意力机制的方法

医疗IoT系统天然具有图结构（设备-患者-服务），图神经网络（GNN）可显式建模实体间依赖。

胡智超等 \[jcs.iie.ac.cn\] 提出 **TSAN**，通过端到端学习挖掘多维时间序列间的动态关系图，并结合因果推断生成掩码以增强可解释性。其时空注意力网络联合建模时间演化与空间依赖，在MSL和SMD数据集上F1-score分别提升0.9%和2.3%，且跨数据集性能波动最小，表明其强泛化能力。

周小晖等 \[crad.ict.ac.cn\] 提出融合时域卷积与自注意力的无监督模型，通过信息共享机制同时捕获局部模式与全局依赖。在多个真实多维时序数据集上，F1-score最高提升0.0882，证明了融合架构对复杂依赖的有效建模。

### 基于联邦学习与小样本学习的方法

隐私法规（如HIPAA）要求医疗数据本地化，联邦学习（FL）成为分布式异常检测的主流范式。

Nguyen等 \[jos.org.cn\] 提出 **DÏoT**，一种联邦自学习异常检测系统。各设备本地训练RNN预测报文概率，仅共享模型参数而非原始数据。该方法在检测DDoS等攻击时准确率达95%，且能适应设备固件更新带来的行为漂移。

尹梓诺等 \[jeit.ac.cn\] 针对网络流量类别不平衡问题，提出 **KAFS+SMLP** 框架。KAFS算法基于K-medoids无监督聚类自适应抽取代表性小样本，SMLP孪生网络则学习样本间距离度量。在CICIDS2017上检测准确率达99.80%，对未知攻击检出率提升2.85%以上。

## 实验与评价总结

近三年研究在实验设计与评价上呈现以下共性：

1. **数据集**：医疗场景多采用私有临床数据或合成数据（如CT/MRI），而IoT底层则依赖公开流量数据集（如N-BaIoT、CICIDS2017/2018、Clearwater）。跨域验证仍显不足。
2. **评价指标**：F1-score、AUC-ROC、AUC-PR成为主流，因类别极度不平衡使准确率（Accuracy）失真。假阳性率（FPR）因临床后果严重被特别关注。
3. **性能权衡**：高精度模型（如TSAN、MCBiWGAN-GTN）通常计算复杂，难以部署于资源受限设备；轻量级模型（如基于规则方法）则泛化能力弱。端到端推理延迟（<1s）成为实用化关键指标。
4. **可解释性**：仅少数工作（如TSAN、阿里云方案）提供注意力热图或异常定位，多数深度模型仍为“黑箱”，阻碍临床信任。

## 趋势与挑战

基于2024–2025年已发表及预印本工作，未来研究将聚焦：

1. **多模态融合与跨域对齐**：结合影像、生理信号、电子病历等多源异构数据，利用CLIP等跨模态架构学习统一嵌入空间，提升异常检测的语义一致性 \[developer.aliyun.com\]。
2. **持续学习与概念漂移适应**：医疗IoT设备行为随患者状态、环境动态演化。需开发在线更新机制（如KL散度监控 \[developer.aliyun.com\]），动态调整正常行为基线，避免模型老化。
3. **隐私-效用协同优化**：在联邦学习框架下，探索差分隐私、同态加密与模型性能的帕累托前沿，满足GDPR/HIPAA合规要求的同时最小化精度损失 \[arocmag.cn, jos.org.cn\]。
4. **可解释性与因果推理**：超越相关性分析，结合因果图模型（如TSAN的因果掩码 \[jcs.iie.ac.cn\]）识别异常根因，为临床决策提供可信依据。

## 结论

2022–2025年，云医疗物联网异常检测研究在无监督表示学习、时空依赖建模、隐私保护分布式训练等方向取得显著进展。代表性工作通过自编码器、GAN、GNN与联邦学习等技术，在精度、效率与隐私间取得新平衡。未来，多模态融合、持续学习与因果可解释性将成为突破实用化瓶颈的关键路径。构建兼具高鲁棒性、低延迟与临床可信任的异常检测系统，仍是该领域核心挑战。

## 参考文献

1. Zhang, Y., Tang, L., Wang, K., & Chen, Q. (2022). Anomaly detection algorithm of IoT devices based on GB-AEnet-FL network. *Application Research of Computers*, 39(11), 3410–3416. [arocmag.cn](https://www.arocmag.cn/abs/2022.03.0142)
2. 大熊计算机. (2025). 医疗诊断中的异常检测实战——基于AutoEncoder与One-Class SVM的少样本学习. *阿里云开发者社区*. [developer.aliyun.com](https://developer.aliyun.com/article/1667978)
3. Mirsky, Y., et al. (2018). Kitsune: An ensemble of autoencoders for online network intrusion detection. *NDSS*. Cited in [jos.org.cn](https://jos.org.cn/html/2024/1/6818.htm).
4. Tang, L., Zhao, Y., Xue, C., & Chen, Q. (2024). A Cloud Server Anomaly Detection Model Based on Time Series Decomposition and Spatiotemporal Information Extraction. *Journal of Electronics & Information Technology*, 46(6), 2638–2646. [jeit.ac.cn](https://jeit.ac.cn/cn/article/doi/10.11999/JEIT230679)
5. Meidan, Y., et al. (2018). N-BaIoT—Network-based detection of IoT Botnet attacks using deep autoencoders. *IEEE Pervasive Computing*, 17(3), 12–22. Cited in [jos.org.cn](https://jos.org.cn/html/2024/1/6818.htm).
6. Hu, Z., Yu, X., Liu, L., Zhang, Y., & Yu, H. (2024). Relation Mining and Attention Based Anomaly Detection for Multivariate Time Series. *Journal of Cyber Security*, 9(6), 100–113. [jcs.iie.ac.cn](https://jcs.iie.ac.cn/xxaqxb/ch/reader/view_abstract.aspx?flag=1&file_no=20240607&journal_id=xxaqxb)
7. Zhou, X., Wang, Y., Xu, H., & Liu, M. (2023). Fusion Learning Based Unsupervised Anomaly Detection for Multi-Dimensional Time Series. *Computer Research and Development*. [crad.ict.ac.cn](https://crad.ict.ac.cn/cn/article/doi/10.7544/issn1000-1239.202220490)
8. Nguyen, T. D., et al. (2019). DÏoT: A federated self-learning anomaly detection system for IoT. *ICDCS*. Cited in [jos.org.cn](https://jos.org.cn/html/2024/1/6818.htm).
9. Yin, Z., Chen, H., Ma, H., Hu, T., & Bai, L. (2025). A Network Traffic Anomaly Detection Method Integrating Unsupervised Adaptive Sampling with Enhanced Siamese Network. *Journal of Electronics & Information Technology*. [jeit.ac.cn](https://jeit.ac.cn/cn/article/doi/10.11999/JEIT241115)
10. Fan, L., Li, C., Wu, Y., Duan, C., Wang, Z., Lin, H., & Yang, J. (2024). Survey on IoT Device Identification and Anomaly Detection. *Journal of Software*, 35(1), 288–308. [jos.org.cn](https://jos.org.cn/html/2024/1/6818.htm)
11. Wu, G., & Ling, J. (2023). Time series anomaly detection for cyber physical systems based on adaptive interactive learning. *Application Research of Computers*, 40(10), 2933–2938. [arocmag.cn](https://www.arocmag.cn/abs/2023.03.0095)
12. Cheng, Y., & Zhou, F. (2024). Semi-Supervised Learning-Based Method for Unknown Anomaly Detection. *Computer Research and Development*. [crad.ict.ac.cn](https://crad.ict.ac.cn/cn/article/doi/10.7544/issn1000-1239.202330627)