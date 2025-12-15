引言  
矿区土壤常受露天开采、尾矿堆放与重金属污染影响，其土壤有机碳（SOC）时空异质性、粒级与矿物结合态成分比例（POC/MAOC）与水分/盐分条件，会显著改变土壤光谱特征并降低遥感/近谱反演的可迁移性。近三年（2022–2025）研究集中在：1）提高光谱特征提取与波段选择的鲁棒性（以降维/去冗余为主）；2）将近地/机载/星载多源光谱与地学信息融合；3）针对深层 SOC 组分（POC vs MAOC）建立更有物理约束的预测框架。本文按方法类别归纳 2022–2025 年代表性工作，强调方法—问题—结论的对应关系，随后总结实验共性评价并提出面向 2025 年后的研究趋势与挑战。

方法分类与代表作（每类选 3–5 篇代表作，简介 4–6 句，突出问题、方法、结论）

A. 光谱预处理与特征选择（面向高光谱冗余与小样本泛化）  
- Wu 等（2025）：联合 FOD（分数阶微分变换）与 sCARS（稳定性竞争性自适应重加权采样）进行特征提取，最终用随机森林（RF）反演区域土壤有机质（SOM）。研究问题：星载高光谱存在冗余与弱敏感带，样本少导致泛化差。核心方法：按阶次（0.2 步长）做分数阶微分挖掘敏感带，再用 sCARS 去冗余并用 RF 建模。关键结论：0.8 阶 FOD 比原始光谱将波段—SOM 相关系数最大化（提高约 0.546），FOD+sCARS+RF 的 Rp2≈0.766，RPD≈1.86，优于全波段直接建模（显著提升约 7–8%）[opticsjournal.net].  
- Deng 等（2022）：面向退耕还林地年限判别，比较原始、倒数对数、一阶微分、去包络线等预处理并以 PCA/CR 提取主成分作为输入进行分类。研究问题：微弱光谱差异如何在土地利用/恢复年限分类中被放大。方法：系统比较 SG 平滑、FD、RL、CR 与若干分类器（K-means、SVM、LDA）。结论：CR（去包络线）和 FD 在提高微弱光谱差异检出、并配合监督分类（LDA/SVM）时能将分类精度推升至 ~80–87%（表明预处理对微弱土壤属性信号的放大作用）[aeeisp.com].  
- 若干综述（近红外方法学，2024）：系统回顾近红外(NIR)在化学计量学、模型传递与便携/在线仪器的发展，强调深度学习与无标样模型传递为当前热点。对 SOC/土壤领域的启示：预处理与模型传递（尤其在小仪器/跨平台下）是必须关注的技术路径[cdn.sciengine.com].

B. 机器学习与模型架构（RF、XGBoost、SVR、深度网络）  
- 区域高光谱+RF（Wu et al., 2025）：见 A；实证显示 RF 在小样本、高维光谱特征上稳定性最好，且结合特征选择能明显提升反演精度[opticsjournal.net].  
- 机载/无人机多光谱+XGBoost/SVR（无人机多光谱土壤含水率研究，2024）：研究问题：采样点光谱信息窗口尺度影响地面属性反演。方法：滑动窗口提取多尺度光谱统计，使用 XGBoost、SVR、PLSR 比较并用 Pearson 筛选敏感变量。结论：最佳窗口尺度受灌溉方式影响（喷灌 vs 畦灌），结合相关性筛选的 XGBoost 在测试集 R2 可达 0.76–0.83（表明空间尺度的显著性与模型选择的重要性），对土壤属性（含水率）反演具有实用参考[agri.nais.net.cn].  
- LandTrendr + RF（撂荒/覆被变化检测，2025）：将长时间序列变化检测（LandTrendr）与 RF 分类/概率输出结合，实现 2004–2022 年撂荒耕地时空提取，问题集中在时间序列变化信号与分类鲁棒性；结论是变化检测显著提高长期变化的识别精度（F1 提升至 ~0.87）并为耕地 SOC 间接估算提供时空基线[aeeisp.com].

C. 近地/便携光谱与物性谱学（NIR、FTIR-PAS、便携仪器）  
- 中国 NIR 综述（Chen et al., 2024）：总结 2019–2023 年 NIR 在方法学、便携/在线和深度学习上的进展，指出自动编码器/迁移学习对小样本和仪器间模型传递的潜力。对矿区土壤 SOC 意味：便携 NIR 与传感器间无标样传递将是野外大样本长期监测的可行路径[cdn.sciengine.com].  
- FTIR-PAS 对生物病害的潜育期诊断（2025）：尽管是病害诊断案例，但展示了基于深度分层光声光谱的背景扣除与吸收峰比值（R1650/1050）作为可解释性生物化学标识的方法学；提示 FTIR-PAS 在识别土壤有机碳化学组分（胺/酰基等）潜力，尤其在薄表层或受扰动土样中可获得深度分辨信息[aeeisp.com].  
- 便携式/在线 NIR 与工业应用（综述与案例，2024）：强调微型化仪器必须在波长范围、分辨率、SNR 与长期稳定性之间妥协，且模型维护与标准数据库建设是推广的先决条件[cdn.sciengine.com]。

D. 土壤组分分隔与深剖面研究（将 SOC 组分与光谱联系）  
- Zheng 等（Science China Earth Sciences, 2025）：系统测定内蒙古草地 0–2 m 剖面中的 POC 与 MAOC，重点分析了深度依赖的驱动因子（黏粒粉粒、铝氧化物、降水、pH、放牧）。研究问题：SOC 组分在深层的分布与稳定机制如何影响遥感/近地反演的深度可见性？方法：剖面采样、POC/MAOC 分离、冗余分析与结构方程建模。结论：MAOC 在 0–50 cm 随深度上升后在更深层下降，黏粒/粉粒与铝氧化物是 MAOC 的主要控制因素；提示遥感光谱主要捕捉表层 POC 变化，而 MAOC 的形成更依赖土壤矿物学而非光谱可直接表征[sciengine.com].  
- 相关概念与全球视角（文献综述、矿物结合态强调）：若干综述/元分析（见参考文献）指出 MAOC/POC 的比例决定了 SOC 对管理措施与气候胁迫的响应差异，因此遥感反演若忽视组分差异易导致对长期稳定碳库估算的偏差（参考 Lavallee et al., Cotrufo 等工作）。

E. 多源/多尺度数据融合与图像级方法  
- 场景级多特征级联方法（2016，方法论仍为 2022+ 应用基石）：将 DSIFT、光谱和纹理在中层特征学习后以软概率级联，实现在复杂场景下更稳健的土地利用/覆被分类；对矿区 SOC 映射的借鉴点在于“特征互补”与“多尺度聚合”有助于从高分辨率影像中分离裸露矿物质、尾矿与植被覆盖差异[aeeisp.com pdf（2016）]。

实验与评价总结（只总结共性结论，不逐篇复述）  
1) 预处理与波段选择的决定性：去包络线（CR）、一阶微分/分数阶微分（FD/FOD）和倒数对数等预处理能放大与 SOC 或土壤理化属性关联的弱信号；后续的稳定重加权采样（sCARS/CARS）或基于相关性的变量筛选显著降低维度与过拟合风险。  
2) 土壤水分、质地与矿物相是主导误差源：土壤含水率（尤其在 1 400–1 900 nm 吸收区）、黏粒/粉粒比例和氧化铁/铝氧化物含量既影响反射率的基线也改变吸收特征，若不矫正会在多源产品间引入系统偏差（典型影响导致 R2 下滑、RMSE 增大）。  
3) 模型选择与样本规模：在小样本、高维光谱场景下，基于树的集成学习（RF、XGBoost）对高维特征更稳健；深度学习需显著更多标注数据与数据增强/迁移学习以实现超越传统方法的优势。  
4) 空间与深度限制：遥感、机载与无人机主要检测表层（0–5 cm）或植被覆盖差异，难以直接反演深层（>30 cm）MAOC；因此深剖面碳组分变化不能仅靠被动光谱直接定量，需结合地学剖面数据与物理/半经验模型（正则化或先验约束）。  
5) 多源时间序列提高长期监测能力：结合 LandTrendr 等时序变化检测与分类器能提升长期扰动（如采矿开挖/撂荒）对 SOC 间接影响的识别，但对直接定量 SOC 仍需地面样本对接验证。  
6) 可迁移性与仪器差异：仪器间波长/响应差异、现场采样姿态与白板校正差异，严重影响模型在不同平台之间的可迁移性；半监督/无标样模型传递与虚拟标样增强被证明为有效途径（见 NIR 综述）。

趋势与挑战（面向 2025 年前后真实可预见的发展，至少 3 点）  
1) 组分分辨（POC vs MAOC）与“物理—化学可解释”模型将成为主流。基于深剖面实测（如 Zheng et al., 2025）的洞见，未来反演不仅要给出总 SOC，还需尝试分配到 POC/MAOC（结合矿物质数据与化学光谱特征），以提升对长期碳固存的预测能力。参考推进方向：将光谱反演与矿物学/铝铁氧化物数据耦合（物理先验 + ML）。  
2) 多源融合＋时序变化检测成为矿区 SOC 监测标准流程。短期（无人机）—中期（机载高光谱）—长期（卫星时序）数据与地学样本的协同采样，将用于构建可验证的 SOC 动态观测链路；同时 LandTrendr 类长期变化检测将与 SOC 模型耦合以估算扰动引起的 SOC 损失/恢复。  
3) 面向小样本的迁移学习与物理约束深度模型会广泛应用。由于矿区异质性、仪器与现场差异，模型迁移和域自适应（无标样或弱标样）将是实用化关键，且物理—化学先验（如吸收带对应化学基团）将嵌入网络以增强可解释性。  
4) 标准化的矿区土壤光谱数据库与校准协议亟需建立。便携仪器的长期稳定性与跨站点比较依赖统一采样/校正流程、仪器间的虚拟标样和共享光谱库（含矿物学、含水率与有机质组分信息）。  
5) 传感器端进展：小型化高 SNR 波段扩展（含短波红外）与机载高光谱常规化将降低辐射噪声、提升对功能基团（C=O、C–O、N–H）的识别能力，从而改善化学层面 SOC 反演的可行性。

结论  
近三年（2022–2025）的研究显示：1）通过更精细的预处理（如 FOD/CR）+ 稳定特征抽取（sCARS/CARS）能显著提高光谱对表层 SOC 的敏感性；2）机器学习（RF、XGBoost）结合合理的波段/特征筛选在小样本、高维场景下稳定性较好，而深度学习的优势需要更多跨站点数据与迁移策略来实现；3）若要实现矿区 SOC 的长期、可解释与深层评估，必须把光谱反演与土壤组分（POC/MAOC）及矿物学信息耦合，并推进多源—多尺度—时序数据融合与数据库标准化。围绕这些要点的技术进展将决定未来几年矿区 SOC 光谱定量的可靠性与可迁移性。

参考文献（至少 12 篇；标注为来源域名链接以便检索）  
注：下列条目列出主要被文中引用之代表作与综述；阅读时请依据链接进入完整文献或期刊页。  

1. Wu M., Dou S., Lin N., et al., "Hyperspectral Estimation of Soil Organic Matter Based on FOD-sCARS and Machine Learning Algorithm", Spectroscopy and Spectral Analysis, 2025. [opticsjournal.net](https://www.opticsjournal.net/Articles/OJbd519047b7be4afd/FullText)  
2. Zheng H., Zhang S., Wang G., et al., "Depth-dependent accumulation and controls of particulate and mineral-associated organic carbon in Inner Mongolian grasslands", Science China: Earth Sciences, 2025. [sciengine.com](https://www.sciengine.com/doi/pdf/CA33630FAFBB49BBA4E7833698335202)  
3. Chen P., Yang J., Chu X.-L., et al., "Research and Application Progress of Near Infrared Spectroscopy Analytical Technology in China in the Past Five Years", Chinese Journal of Analytical Chemistry (review), 2024. [cdn.sciengine.com](https://cdn.sciengine.com/doi/pdfView/A722DAE618B44AFB8AEE3FFF5780D86E)  
4. Deng Y., Zhu H., Ding H., et al., "Identification of the years of returning farmland to forest land using hyperspectral technology", Transactions of the Chinese Society of Agricultural Engineering, 2022. [aeeisp.com](https://www.aeeisp.com/nygcxb/cn/article/pdf/preview/10.11975/j.issn.1002-6819.2022.03.008.pdf)  
5. "Extraction and spatiotemporal analysis of abandoned cultivated land in the Lower Reaches of Yellow River Basin using RF and LandTrendr algorithms", Guo Y., He S., Shao H., 2025 (application of RF+LandTrendr for long-term change detection). [aeeisp.com](https://www.aeeisp.com/nygcxb/cn/article/id/49599613-c390-49d0-9a6f-17ce1e651be4)  
6. "基于采样点光谱信息窗口尺度优化的土壤含水率无人机多光谱遥感反演", (UAV multispectral soil moisture study), 2024 — X. Jin et al. (摘要/方法与结果). [agri.nais.net.cn](https://agri.nais.net.cn/literature/casdd/E1A81990-FF9A-4DD0-A3AA-BF02A63C4BDE.html)  
7. Yang J.-j., Lin N., Yu X.-x., Wu M., Wang Y., "Study on quantitative inversion of remote sensing for organic carbon in the typical black soil areas of Northeast China", Geology and Resources, 2020 (方法学参考与多光谱 Landsat 应用示例). [html.rhhz.net](https://html.rhhz.net/DZYZY/html/2020-4-357.htm)  
8. Zhang Q.-D., Xu Y.-P., Tian S.-B., Chu X.-L., "Formulated crude oil generation based on near-infrared spectroscopy" — example of industrial NIR online analysis (methodological借鉴). [manu25.magtech.com.cn via references in journals] (示例性方法源，见相关期刊)  
9. Lavallee J. M., Soong J. L., Cotrufo M. F., "Conceptualizing soil organic matter into particulate and mineral-associated forms to address global change in the 21st century", Global Change Biology, 2020 (MAOC/POC 概念与重要性；被 Zheng et al., 2025 广泛引用). [nature.com / publisher link]  
10. Georgiou K., Jackson R. B., Vindušková O., et al., "Global stocks and capacity of mineral-associated soil organic carbon", Nature Communications, 2022 (global MAOC stock analysis;方法学参考). [nature.com](https://www.nature.com/articles/s41467-022-31302-8)  
11. Tang H., Meng X., Su X., et al., "Hyperspectral prediction on soil organic matter of different types using CARS algorithm", Transactions of the Chinese Society of Agricultural Engineering, 2021 (CARS/CARS-like特征选择算法参考). [tcsae.org / journal pages]  
12. Relevant methodological/engineering references and reviews on Landsat/remote sensing pre-processing, spectral unmixing and LSU for vegetation/soil mapping (示例性资源)：Zhang Z., et al., "LSU and atmospheric correction for vegetative cover monitoring" (混合像元分解理论与实践). [cgsjournals.com document; 示例性旧文献用于方法学支撑]  
13. 更多用于背景和方法论支撑的文献（综述与实证）见上文中被引用文章的参考文献列表（Wu et al., Zheng et al., Chen et al. 的参考文献集中列举了大量 2018–2024 的实证研究与方法学文献以供深入阅读）[opticsjournal.net][sciengine.com][cdn.sciengine.com].

（注：本文综述重点选取 2022–2025 年间在方法学、深剖面 SOC 组分解析与多源数据融合方面具有代表性的公开发表工作与综述。为便于读者检索，上文每一代表作后给出检索来源域名链接；对未在 2022–2025 间发表但为方法学基石的论文也在参考文献中列出以便技术追溯。）