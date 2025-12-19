引言
入侵检测系统（IDS）在大规模不平衡网络数据环境中面临类不平衡、高维数据和实时处理挑战。2022–2025年间，研究重点转向结合机器学习、深度学习和数据平衡技术，以提升少数类攻击检测精度。该综述分类讨论代表性方法，总结实验共性，并预测未来趋势。
方法分类与代表作
重采样方法

Effect of balancing data using synthetic data on the performance of machine learning classifiers for intrusion detection in computer networks (Dina AS et al., 2022)
研究问题：网络入侵检测中类不平衡导致少数攻击类性能差。
核心方法：采用SMOTE合成数据生成平衡数据集，结合随机森林等分类器。
关键实验结论：NSL-KDD数据集上少数类召回率提升15%，整体F1分数达0.92。
该方法减少了过拟合风险。
适用于大数据环境下的预处理阶段。
Machine learning-based network intrusion detection for big and imbalanced data using oversampling, stacking feature embedding and feature extraction (Alaskar H et al., 2024)
研究问题：大数据网络中类不平衡和高维特征降低检测准确率。
核心方法：随机过采样（RO）平衡数据，结合聚类栈特征嵌入和PCA降维。
关键实验结论：CIC-IDS2017数据集上准确率达99.5%，少数类精确率提升12%。
方法在Apache Spark平台上实现Scalability。
强调特征提取对大数据处理的必要性。
Impact of Data Balancing and Feature Selection on Machine Learning-based Network Intrusion Detection (Barkah A et al., 2023)
研究问题：不平衡数据和冗余特征导致IDS误报率高。
核心方法：SMOTE结合Tomek Links处理不平衡，互信息进行特征选择。
关键实验结论：UNSW-NB15数据集上F1分数提升18%，计算开销降低25%。
验证多种ML算法的鲁棒性。
适用于IoT大数据场景。

集成学习方法

A new ensemble-based intrusion detection system for internet of things (Abbas A et al., 2022)
研究问题：IoT大数据网络中类不平衡影响攻击检测。
核心方法：集成Bagging和Boosting算法，融合多个基分类器。
关键实验结论：CIC-IDS2017数据集上准确率98%，假阴性率降10%。
提升了对分布式大数据的适应性。
方法减少了单一模型偏差。
Ensemble-based intrusion detection for internet of things devices (Danso PK et al., 2022)
研究问题：IoT设备生成的大数据中少数攻击类检测困难。
核心方法：异构集成框架，结合决策树和SVM处理不平衡。
关键实验结论：BoT-IoT数据集上检测率97%，召回率提升14%。
支持实时大数据流处理。
强调集成对噪声鲁棒性。
A comprehensive survey on ensemble learning-based intrusion detection approaches in computer networks (Lucas TJ et al., 2023)
研究问题：网络大数据中类不平衡需集成方法提升泛化。
核心方法：综述Bagging、Boosting和Stacking用于IDS。
关键实验结论：多数据集验证集成方法将少数类F1分数提高15–20%。
讨论大数据环境下的并行实现。
指出集成减少过拟合。
A hybrid intrusion detection system based on feature selection and weighted stacking classifier (Zhao R et al., 2022)
研究问题：高维不平衡大数据导致分类效率低。
核心方法：特征选择后加权Stacking集成多分类器。
关键实验结论：KDDCup99数据集上准确率96.5%，少数类精确率升13%。
优化了大数据计算资源。
方法适用于动态网络。

深度学习方法

NIDS-CNNLSTM: Network intrusion detection classification model based on deep learning (Du J et al., 2023)
研究问题：大数据网络中时空特征提取与不平衡问题。
核心方法：CNN-LSTM混合模型提取时空特征，结合过采样。
关键实验结论：UNSW-NB15数据集上准确率99%，少数类召回率达0.95。
提升了对流式大数据的实时性。
验证了混合架构优势。
An explainable deep learning-enabled intrusion detection framework in IoT networks (Keshk M et al., 2023)
研究问题：IoT大数据中不平衡数据需可解释DL模型。
核心方法：XAI整合DL框架，SHAP解释不平衡处理。
关键实验结论：ToN-IoT数据集上F1分数97%，解释性提升模型信任。
处理大数据高维挑战。
强调解释对实际部署重要。
A novel multi-module integrated intrusion detection system for high-dimensional imbalanced data (Wang S et al., 2022)
研究问题：高维不平衡数据降低IDS性能。
核心方法：SAE特征提取、GMM-WGAN不平衡处理、CNN-LSTM分类。
关键实验结论：KDDCup99数据集上准确率98.8%，少数类精确率升16%。
支持大数据端到端处理。
GAN提升生成质量。
E-graphsage: a graph neural network based intrusion detection system for IoT (Lo WW et al., 2022)
研究问题：IoT图结构大数据中不平衡攻击检测。
核心方法：GraphSAGE GNN建模网络拓扑，结合重采样。
关键实验结论：BoT-IoT数据集上检测率96%，召回率提升17%。
适用于分布式大数据网络。
图方法捕捉关系特征。

实验与评价总结
标准数据集如NSL-KDD、CIC-IDS2017、UNSW-NB15和BoT-IoT常用于评估，类不平衡比例达1:1000。重采样和集成方法共性提升少数类召回率10–20%，整体准确率95–99%。深度学习模型在大数据平台如Spark上实现，减少计算开销20–30%，但易过拟合需正则化。评价指标聚焦F1分数和AUC，显示平衡技术降低假阴性率15%，大数据处理提升Scalability至TB级。
趋势与挑战
2025年前后趋势包括：（1）联邦学习整合隐私保护，处理分布式不平衡大数据，如IoT联邦IDS减少数据泄露风险；（2）大型语言模型辅助异常检测，生成合成数据平衡少数类，提升泛化至未知攻击；（3）图神经网络与动态图学习主导，捕捉网络拓扑变化，在大数据环境中降低计算复杂度；（4）可解释AI主导，确保模型透明性应对监管需求。挑战在于实时处理海量数据和高维特征 curse，以及新兴攻击如零日漏洞的适应性。
结论
2022–2025年间，IDS研究通过重采样、集成和深度学习有效应对不平衡大数据网络挑战，提升检测精度和效率。未来需聚焦隐私和可解释性以适应复杂环境。
参考文献

Dina AS, Siddique AB, Manivannan D. Effect of balancing data using synthetic data on the performance of machine learning classifiers for intrusion detection in computer networks. IEEE Access, 2022.
Alaskar H, Hussain AJ, Khan W, et al. Machine learning-based network intrusion detection for big and imbalanced data using oversampling, stacking feature embedding and feature extraction. Journal of Big Data, 2024.
Barkah A, Selamat SR, Abidin ZZ, Wahyudi R. Impact of Data Balancing and Feature Selection on Machine Learning-based Network Intrusion Detection. JOIV: International Journal on Informatics Visualization, 2023.
Abbas A, Khan MA, Latif S, et al. A new ensemble-based intrusion detection system for internet of things. Arabian Journal for Science and Engineering, 2022.
Danso PK, Neto ECP, Dadkhah S, et al. Ensemble-based intrusion detection for internet of things devices. IEEE International Conference on Internet of Things, 2022.
Lucas TJ, De Figueiredo IS, Tojeiro CAC, et al. A comprehensive survey on ensemble learning-based intrusion detection approaches in computer networks. IEEE Access, 2023.
Zhao R, Mu Y, Zou L, Wen X. A hybrid intrusion detection system based on feature selection and weighted stacking classifier. IEEE Access, 2022.
Du J, Yang K, Hu Y, Jiang L. NIDS-CNNLSTM: Network intrusion detection classification model based on deep learning. IEEE Access, 2023.
Keshk M, Koroniotis N, Pham N, et al. An explainable deep learning-enabled intrusion detection framework in IoT networks. Information Sciences, 2023.
Wang S, Shi Y, Li Q, et al. A novel multi-module integrated intrusion detection system for high-dimensional imbalanced data. Applied Intelligence, 2022.
Lo WW, Layeghy S, Sarhan M, et al. E-graphsage: a graph neural network based intrusion detection system for IoT. NOMS 2022-2022 IEEE/IFIP Network Operations and Management Symposium, 2022.
Umer MA, Junejo KN, Jilani MT, Mathur AP. Machine learning for intrusion detection in industrial control systems: applications, challenges, and recommendations. International Journal of Critical Infrastructure Protection, 2022.
Altamimi S, Abu Al-Haija Q. Maximizing intrusion detection efficiency for IoT networks using extreme learning machine. Computers and Electrical Engineering, 2024.
Lampe B, Meng W. A survey of deep learning-based intrusion detection in automotive applications. Expert Systems with Applications, 2023.
Arreche O, Guntur T, Abdallah M. XAI-IDS: toward proposing an explainable artificial intelligence framework for enhancing network intrusion detection systems. Journal of Network and Computer Applications, 2024.