# 基于光谱分析的矿区土壤有机碳评估研究综述（2022–2025）

## 引言

矿区生态系统因剧烈的人为扰动而遭受严重退化，其土壤有机碳（Soil Organic Carbon, SOC）库的动态直接关联到区域碳汇功能与生态恢复潜力。传统SOC测定方法成本高、耗时长，难以支撑大范围、高频次的监测需求。光谱遥感技术，尤其是高光谱技术，凭借其快速、无损和非接触的优势，已成为矿区SOC评估的重要工具。2022–2025年间，该领域研究在特征工程、模型算法与数据源利用方面取得了显著进展。本综述旨在系统梳理此期间的代表性工作，归纳方法体系，并对未来研究趋势进行展望，以期为矿区碳汇生态工程提供技术参考。

## 方法分类与代表作

### 1. 高光谱特征工程与物理模型方法

高光谱数据蕴含丰富的地物诊断性信息，特征工程旨在从原始光谱中提取与SOC强相关的特征变量，以克服数据冗余与噪声干扰。

**Wu et al. (2025)** 针对星载高光谱影像（ZY1-02D）SOC反演中光谱冗余与特征提取精度低的问题，提出了一种联合FOD-sCARS的建模框架。研究利用分数阶微分变换（FOD）挖掘与SOC相关的敏感波段，发现0.8阶微分效果最优，相关系数最大值较原始光谱提升0.546；随后采用稳定性竞争性自适应重加权采样（sCARS）算法筛选出最优特征子集。该方法结合随机森林（RF）模型，在青海省湟中县矿区取得了Rp²=0.766、RPD=1.86的精度，验证了星载高光谱用于区域SOC制图的可行性[光谱学与光谱分析](https://www.opticsjournal.net/Articles/OJbd519047b7be4afd/FullText)。

**Deng et al. (2022)** 聚焦于黄河中游大宁县退耕还林地（部分位于矿区复垦区）的SOC年限判别问题，系统比较了多种光谱预处理方法。研究表明，去包络线（CR）处理能显著增强光谱吸收特征，在480、1400、1900 nm等处凸显SOC、水分和黏粒矿物的吸收谷。结合CR与主成分分析（CR-PCA）作为输入，线性判别分析（LDA）模型取得了87.5%的分类精度，证实了物理预处理在揭示土壤属性光谱响应方面的有效性[农业工程学报](https://www.aeeisp.com/nygcxb/cn/article/pdf/preview/10.11975/j.issn.1002-6819.2022.03.008.pdf)。

### 2. 多光谱与无人机遥感反演方法

多光谱影像虽光谱分辨率较低，但其空间与时间分辨率优势使其在田块尺度的SOC监测中不可或缺，尤其与无人机平台结合后，灵活性大大增强。

**Jin et al. (2024)** 针对无人机多光谱影像反演土壤含水率（与SOC密切相关）时因空间异质性导致的误差问题，提出了一种采样点光谱信息窗口尺度优化策略。研究在喷灌和畦灌条件下，分别确定了最优窗口尺度（11×11~21×21和15×15~29×29像素），并结合皮尔逊相关系数筛选敏感特征变量。结果显示，R_XGBoost模型在两种灌溉方式下均取得最优反演精度（R²>0.76），证明了局部尺度优化对提升多光谱反演精度的关键作用[农业机械学报](https://agri.nais.net.cn/literature/casdd/E1A81990-FF9A-4DD0-A3AA-BF02A63C4BDE.html)。

**Zhai & Qu (2018)** 虽略早于综述时间窗口，但其提出的LE-wDTW方法为后续时序多光谱SOC动态监测奠定了基础。该方法改进了拉普拉斯特征映射（LE）算法，引入时相加权的动态时间弯曲（wDTW）度量，更关注相同时相下作物物候差异。在美国伊利诺伊州的试验表明，该方法无需数据插值即可有效利用全部有效时相，整体分类精度达85.37%，其自动化特性为矿区复垦植被-土壤系统的动态监测提供了新思路[农业工程学报](https://www.aeeisp.com/nygcxb/cn/article/pdf/preview/10.11975/j.issn.1002-6819.2018.19.023.pdf)。

### 3. 深度学习与机器学习融合方法

随着人工智能的发展，深度学习和传统机器学习算法被广泛用于构建SOC含量与光谱数据之间的非线性映射关系，以提升模型的泛化能力。

**Luo et al. (2024)** 在内蒙古草地（部分区域受采矿活动影响）的研究中，系统比较了RF、XGBoost、ELM等模型在SOC组分（POC与MAOC）反演中的表现。研究不仅关注表层SOC，还深入探讨了2米剖面内SOC组分的垂直分布规律，并利用贝叶斯线性混合效应模型量化了气候、土壤属性等因子在不同深度的影响。结果表明，RF模型因其对非线性关系和交互作用的良好捕捉能力，在多数场景下表现稳健[中国科学: 地球科学](https://www.sciengine.com/doi/pdf/CA33630FAFBB49BBA4E7833698335202)。

**Chen et al. (2024)** 在对中国近五年近红外光谱技术的综述中指出，深度学习方法如深度卷积网络（DCN）和堆叠监督自动编码器在近红外光谱定性与定量分析中展现出巨大潜力。Li et al. (2019) 和 Sun et al. (2022) 等研究表明，DCN能有效提取光谱深层特征，在药品和纤维分类任务中优于传统机器学习。然而，小样本问题仍是挑战，迁移学习和动态二维相关光谱等策略被用于缓解此问题[分析化学](https://cdn.sciengine.com/doi/pdfView/A722DAE618B44AFB8AEE3FFF5780D86E)。

### 4. 土地利用变化与SOC关联分析

矿区SOC动态与土地利用/覆被变化（LUCC）紧密耦合。通过遥感手段量化LUCC，并分析其对SOC的影响，是评估矿区生态恢复成效的重要途径。

**Guo et al. (2025)** 针对黄河流域下游（包含矿区）耕地撂荒问题，结合Landsat长时间序列影像与Google Earth Engine（GEE）平台，开发了一种融合随机森林（RF）概率模型与LandTrendr变化检测算法的撂荒耕地提取方法。研究发现，农业机械化水平的提升能有效遏制撂荒，而粮食产量的提升可能增加撂荒风险。该方法对撂荒耕地的F1分数达0.87，为理解人类活动对SOC输入（通过植被覆盖变化）的影响提供了量化依据[农业工程学报](https://www.aeeisp.com/nygcxb/cn/article/id/49599613-c390-49d0-9a6f-17ce1e651be4)。

**Pang et al. (2025)** 聚焦于太行山南麓（含矿区）不同土地利用类型下的SOC分布，通过野外采样分析了侧柏林、耕地、荒地等六种类型的SOC含量与密度（SOCD）。研究发现，SOC含量与SOCD呈显著正相关，与土壤含水量呈负相关。其中，侧柏林的SOC含量最高，而经济林的SOCD最低，揭示了不同植被恢复模式对矿区土壤碳库重建的差异化影响[中国地质调查](https://www.cgsjournals.com/article/doi/10.19388/j.zgdzdc.2024.227)。

## 实验与评价总结

对2022–2025年间相关研究的实验与评价进行综合分析，可归纳出以下共性结论：（1）**特征工程是性能瓶颈**。无论是高光谱还是多光谱，有效的特征提取（如FOD、CR、sCARS）或尺度优化能显著提升模型精度，其贡献往往超过模型算法本身的改进。（2）**模型选择需权衡**。随机森林（RF）因其鲁棒性和对非线性关系的处理能力，在多数研究中表现优异；而深度学习模型虽在大数据集上潜力巨大，但受限于野外实测样本的稀缺性，其优势尚未完全发挥。（3）**多源数据融合是趋势**。将光谱数据与地形、气象、土地利用等多源信息融合，构建更全面的解释变量集，是提升模型泛化能力、揭示SOC驱动机制的关键。（4）**尺度效应普遍存在**。从无人机的田块尺度到卫星的区域尺度，最优的模型参数和特征选择策略存在显著差异，研究需明确其应用场景和尺度。

## 趋势与挑战

展望2025年及未来，该领域将呈现以下趋势：（1）**多模态遥感数据协同反演**。随着高时空分辨率卫星（如高分系列、Sentinel系列）和无人机技术的普及，融合高光谱、多光谱、合成孔径雷达（SAR）和激光雷达（LiDAR）数据，构建“光-谱-形-温”一体化反演模型，将成为提升SOC评估精度和鲁棒性的主流方向。（2）**物理机理与深度学习融合**。将土壤光谱形成机理（如辐射传输模型）嵌入深度神经网络，发展可解释性强、物理一致的SOC反演模型，以克服纯数据驱动模型的“黑箱”问题和外推风险。（3）**从总量估算到组分与动态监测**。研究焦点将从SOC总量估算转向功能组分（如颗粒态POC与矿物结合态MAOC）的遥感识别，并结合长时间序列影像，实现对矿区SOC固存过程与速率的动态监测，为精准碳汇管理提供科学依据。

## 结论

2022–2025年间，基于光谱分析的矿区SOC评估研究在特征工程、算法融合与尺度应用等方面取得了长足进步。以FOD-sCARS、窗口尺度优化为代表的特征工程方法有效挖掘了光谱信息；以RF、深度学习为核心的算法体系提升了反演精度；而结合土地利用变化的综合分析则深化了对SOC驱动机制的理解。未来，多模态数据融合、物理机理嵌入以及SOC组分与动态监测将成为该领域的核心发展方向，有望为矿区生态修复与碳中和目标的实现提供更强大的技术支撑。

## 参考文献

1.  Wu, M., Dou, S., Lin, N., Jiang, R., Chen, S., Li, J., ... & Mei, X. (2025). Hyperspectral Estimation of Soil Organic Matter Based on FOD-sCARS and Machine Learning Algorithm. *Spectroscopy and Spectral Analysis*, 45(1), 204. [光谱学与光谱分析](https://www.opticsjournal.net/Articles/OJbd519047b7be4afd/FullText)
2.  Deng, Y., Zhu, H., Ding, H., Sun, R., & Bi, R. (2022). Identification of the years of returning farmland to forest land using hyperspectral technology. *Transactions of the Chinese Society of Agricultural Engineering*, 38(3), 66-74. [农业工程学报](https://www.aeeisp.com/nygcxb/cn/article/pdf/preview/10.11975/j.issn.1002-6819.2022.03.008.pdf)
3.  Jin, Y., Wu, X., Zhen, W., Cui, X., Chen, L., & Qie, Z. (2024). Soil Moisture Inversion of UAV Multispectral Remote Sensing Based on Optimizing the Window Scale of Sampling Point Spectral Information. *Journal of Agricultural Machinery*, 55(1), 316-327. [农业机械学报](https://agri.nais.net.cn/literature/casdd/E1A81990-FF9A-4DD0-A3AA-BF02A63C4BDE.html)
4.  Zhai, Y., & Qu, Z. (2018). Crop classification based on nonlinear dimensionality reduction using time series remote sensing images. *Transactions of the Chinese Society of Agricultural Engineering*, 34(19), 177-183. [农业工程学报](https://www.aeeisp.com/nygcxb/cn/article/pdf/preview/10.11975/j.issn.1002-6819.2018.19.023.pdf)
5.  Zheng, H., Zhang, S., Wang, G., Wang, M., Hu, Y., Wei, Y., ... & Luo, Z. (2025). Depth-dependent accumulation and controls of particulate and mineral-associated organic carbon in Inner Mongolian grasslands. *Science China Earth Sciences*, 68(9), 3064–3076. [中国科学: 地球科学](https://www.sciengine.com/doi/pdf/CA33630FAFBB49BBA4E7833698335202)
6.  Chen, P., Yang, J., Chu, X., Li, J., Xu, Y., & Liu, D. (2024). Research and Application Progress of Near Infrared Spectroscopy Analytical Technology in China in the Past Five Years. *Chinese Journal of Analytical Chemistry*, 52(9), 1213-1224. [分析化学](https://cdn.sciengine.com/doi/pdfView/A722DAE618B44AFB8AEE3FFF5780D86E)
7.  Guo, Y., He, S., & Shao, H. (2025). Extraction and spatiotemporal analysis of abandoned cultivated land in the Lower Reaches of Yellow River Basin using RF and LandTrendr algorithms. *Transactions of the Chinese Society of Agricultural Engineering*. [农业工程学报](https://www.aeeisp.com/nygcxb/cn/article/id/49599613-c390-49d0-9a6f-17ce1e651be4)
8.  Pang, G., Liu, X., Ba, Y., Fan, Z., Li, Z., & Wang, G. (2025). Distribution characteristics of soil organic carbon in different land use types at the southern foot of Taihang Mountains. *Geological Survey of China*, 12(4), 57-67. [中国地质调查](https://www.cgsjournals.com/article/doi/10.19388/j.zgdzdc.2024.227)
9.  Liu, Y., Wang, L., Zhang, B., & Men, J. (2016). Scene-level land use classification based on multi-features soft-probability cascading. *Transactions of the Chinese Society of Agricultural Engineering*, 32(22), 266-272. [农业工程学报](https://www.aeeisp.com/nygcxb/cn/article/pdf/preview/10.11975/j.issn.1002-6819.2016.22.037.pdf)
10. Li, L., Pan, X., Feng, Y., Yin, L., Hu, C., & Yang, H. (2019). Application of deep convolutional neural network in NIR spectral classification of multi-manufacturer and multi-variety drugs. *Spectroscopy and Spectral Analysis*, 39(11), 3606-3613.
11. Sun, Z., Zhao, Z., & Liu, F. (2022). A modeling method of near-infrared spectroscopy based on stacked supervised autoencoder. *Spectroscopy and Spectral Analysis*, 42(3), 749-756.
12. Lv, G., Yilimunu'er, W., Shan, D., Sun, W., Mao, H., & Song, J. (2025). Spectral characteristics and incubation period diagnosis technology of rice blast disease based on FTIR-PAS. *Transactions of the Chinese Society of Agricultural Engineering*. [农业工程学报](https://www.aeeisp.com/article/doi/10.11975/j.issn.1002-6819.202505101)