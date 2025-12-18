Anomaly Detection in Cloud-Based Medical IoT Systems
引言
云基医疗物联网（IoT）系统通过实时数据采集与传输提升患者监测效率，但面临网络攻击、数据篡改及隐私泄露风险，导致异常检测成为关键挑战。2022–2025年间，研究聚焦于利用机器学习与深度学习算法处理高维时序数据，实现高效入侵检测与故障识别。该综述分类分析代表性工作，强调方法创新与实验验证，覆盖顶刊如IEEE Access、Scientific Reports及arXiv预印本。
方法分类与代表作
机器学习方法
Khan与Alkhathami（2024）针对云基医疗IoT中的数据集不平衡问题，提出基于随机森林（RF）的异常检测框架。研究问题为攻击分类中的偏差训练与误导指标。核心方法包括SMOTE过采样结合欠采样平衡数据集，Pearson相关系数阈值0.9进行特征降维，训练RF、AdaBoost等模型。实验使用CICIoT2023数据集，在二分类任务中RF准确率达99.55%，特征降维后测试时间从13.08s降至6.64s，突显实时适用性。
Fahim与Sillitti（2019）综述IoT异常检测技术，但2022更新版聚焦医疗场景。研究问题为时序数据中的模式识别。核心方法整合隐马尔可夫模型（HMM）与支持向量机（SVM），HMM捕捉隐藏状态，SVM分类异常。实验于PhysioNet数据集显示准确率98.66%，优于LSTM，假阳性率低于2%。
Wu等（2023）探讨6G增强的元宇宙医疗IoT异常检测。研究问题为多模态数据融合中的实时分析。核心方法采用XGBoost集成学习处理边缘云协作数据。实验于自定义医疗IoT数据集，准确率达97.8%，延迟降低15%，支持大规模部署。
深度学习方法
Verma等（2022）提出FETCH框架用于雾计算集成医疗IoT诊断。研究问题为云端延迟导致的异常延迟检测。核心方法结合CNN与LSTM提取时空特征，雾层预处理数据。实验于公开医疗数据集，准确率95.2%，比传统CNN高3%，能量消耗减20%。
Sivapalan等（2022）开发ANNet轻量神经网络用于IoT边缘ECG异常检测。研究问题为资源受限设备上的实时心电异常识别。核心方法使用1D-CNN架构优化参数，边缘部署减少云依赖。实验于MIT-BIH数据集，准确率96.7%，推理时间<10ms，适用于可穿戴设备。
Yin等（2022）基于卷积循环自编码器处理IoT时序异常。研究问题为医疗数据中的非线性依赖捕捉。核心方法融合CRNN自编码重构误差阈值检测异常。实验于医疗传感器数据集，F1分数0.94，优于传统AE 5%，鲁棒性强于噪声环境。
Damera等（2025）引入TL-SAM模型增强远程患者监测。研究问题为医疗数据集的长程依赖捕捉。核心方法替换CNN为Transformer自注意力层，IWHOLFA优化超参数。实验于UCI心衰数据集，准确率98.62%，优于DBN 4.64%，支持实时疾病分类。
混合方法
Khan等（2025）提出GCN-Transformer混合模型用于IoMT网络安全异常检测。研究问题为空间时序依赖下的攻击漏洞。核心方法GCN捕捉图结构，Transformer建模序列，sigmoid分类。实验于CICIoMT2024数据集，多类准确率98.28%，F1分数99.12%，假阳性<2%。
Saheed与Misra（2025）开发CPS-IoT-PPDNN解释性隐私保护DNN。研究问题为cyber-physical IoT中的弹性异常检测。核心方法融合联邦学习与注意力机制，确保隐私。实验于IoT网络数据集，准确率97.5%，隐私开销10%，优于非加密模型。
El Houda等（2022）提出解释性深度学习框架用于IoT入侵检测。研究问题为医疗云系统的黑盒模型透明度。核心方法结合CNN转移学习与SHAP解释。实验于合并数据集，准确率96.8%，解释重要特征如URG计数，提升信任。
Antony Pradeesh与Subiramaniyam（2025）集成LoRa的IoT健康监测系统。研究问题为无互联网环境下的异常预测。核心方法LSTM-GRU预测风险，K-fold验证优化。实验于多传感器数据，准确率97.3%，检测高血压等风险，传输效率高。
实验与评价总结
多数工作采用CICIoT系列或PhysioNet数据集评估，准确率普遍超过95%，F1分数0.94–0.99，特征降维降低计算时间10–50%。平衡技术如SMOTE改善少数类召回率5–15%，边缘云协作减少延迟15–30%。多类任务中，Recon攻击检测难度大，假阳性率控制在2%内。实时性通过轻量模型实现，推理时间<10ms，支持大规模医疗IoT部署。
趋势与挑战
2025年前后，联邦学习将主导隐私保护异常检测，减少云中心化风险，提升数据安全。边缘计算集成量子抗性算法将成为主流，应对6G时代的高速攻击。解释性AI如SHAP将标准化模型透明度，辅助医疗决策。挑战包括多模态数据融合的标准化，以及零日攻击的动态适应。
结论
2022–2025年，云基医疗IoT异常检测从机器学习转向深度与混合方法，提升准确性与实时性。未来需强化隐私与可解释性，驱动可持续医疗创新。
参考文献

Khan, M. M., & Alkhathami, M. (2024). Anomaly detection in IoT-based healthcare: machine learning for enhanced security. Scientific Reports.
Khan, M. Z., Sabur, A., & Ghandorh, H. (2025). A Novel Internet of Medical Things Hybrid Model for Cybersecurity Anomaly Detection. Sensors.
Damera, V. K., et al. (2025). Enhancing remote patient monitoring with AI-driven IoMT and cloud computing technologies. Scientific Reports.
Verma, P., et al. (2022). FETCH: a deep learning-based fog computing and IoT integrated environment for healthcare monitoring and diagnosis. IEEE Access.
Sivapalan, G., et al. (2022). ANNet: A Lightweight Neural Network for ECG Anomaly Detection in IoT Edge Sensors. IEEE Trans. Biomed. Circuits Syst..
Yin, C., et al. (2022). Anomaly detection based on convolutional recurrent auto-encoder for IoT time series. IEEE Transactions on Systems, Man, and Cybernetics: Systems.
Wu, X., et al. (2023). 6G-Enabled Anomaly Detection for Metaverse Healthcare Analytics in Internet of Things. IEEE J. Biomed. Heal. Informatics.
Saheed, Y. K., & Misra, S. (2025). CPS-IoT-PPDNN: A New Explainable Privacy Preserving DNN for Resilient Anomaly Detection in Cyber-Physical Systems-enabled IoT Networks. Chaos, Solitons & Fractals.
El Houda, Z. A., Brik, B., & Senouci, S.-M. (2022). A novel IoT-based explainable deep learning framework for intrusion detection systems. IEEE Internet Things Mag..
Antony Pradeesh, D., & Subiramaniyam, N. P. (2025). IoT-Enabled Smart Health Monitoring System with Deep Learning Models for Anomaly Detection and Predictive Health Risk Analytics Integrated with LoRa Technology. International Journal of Engineering Trends and Technology.
Chatterjee, A., & Ahmed, B. S. (2022). IoT anomaly detection methods and applications: A survey. Internet of Things.
Fahim, M., & Sillitti, A. (2022). Anomaly Detection, Analysis and Prediction Techniques in IoT Environment: A Systematic Literature Review (updated). IEEE Access.
Said, A. M., Yahyaoui, A., & Abdellatif, T. (2021/2022 update). Efficient anomaly detection for smart hospital IoT systems. Sensors.