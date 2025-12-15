引言  
矿区土壤往往经历强烈扰动（剥离、回填、冶炼残留），导致有机碳（SOC）含量空间异质性、大气/水文暴露和矿物组成变化，这对基于光谱的快速SOC评估提出特殊挑战：光谱响应受含水率、矿物结合位点、颗粒组分与表层物理结构强烈耦合。近年来（2022–2025），国内外围绕高光谱/近红外（NIR）、中红外（MIR）、傅里叶变换红外-光声（FTIR‑PAS）等测量模态，结合分数阶微分、特征波段选择、窗口尺度优化与机器学习（随机森林、XGBoost、SVM、深度网络）提出了一系列针对复杂场景（包括退耕地、草地、矿区相近地类）的算法与工程实践。本文以方法学为主线，筛选并按类别讨论 2022–2025 年代表性工作（每类不超过 5 篇），重点指出方法原理、实测结论及其对矿区 SOC 评估的适配性与局限性，并基于共性实验结论给出短中期研究趋势与挑战预测。

方法分类与代表作（每篇 4–6 句，突出问题/方法/结论）

A. 星载/星载‑级高光谱反演与特征变换（适用于大尺度矿区制图）  
1) 联合 FOD‑sCARS + 机器学习 以 ZY1‑02D 星载高光谱为源，采用分数阶微分（Fractional‑order differential, FOD）增强与稳定竞争性自适应重加权采样（sCARS）做波段筛选，再用随机森林（RF）等机器学习建模以估测土壤有机质（SOM/SOC）。该研究系统比较了不同阶次 FOD（步长 0.2），报告 0.8 阶可使波段‑SOM 最大相关系数相比原始波段提高 ~0.546；sCARS 有效去冗余且提升模型泛化；在样本 67 的研究区上，基于 FOD‑sCARS + RF 的 Rp2≈0.766，RPD≈1.86，优于全波段建模（Rp2 提升 ≈7.6%）[WU et al., 2025][opticsjournal.net].  
2) 基于高分影像与去包络线（Continuum Removal, CR）+ 主成分分析的高光谱分类/回归研究，用于辨别土地利用年限、间接指示 SOC 改变。冯退耕/年限判别研究表明，CR 处理可显著突出 480、900、1100、1400、1900、2200、2350 nm 处吸收谷并用于年限分类；以 CR‑PCA 作为输入的 LDA 模型在样本分配（3:1）下，总精度可达 87.5%（表明去包络线在提升土壤光谱可判别性方面的工程可用性）[Deng et al., 2022][aeeisp.com].  
3) 时序/降维方法对长时序高光谱/多时相数据的处理（虽以作物分类为例，但方法对多次观测矿区表层演化/扰动有借鉴意义）。改进的拉普拉斯谱降维（LE）结合加权动态时间弯曲（wDTW）可处理时相不等长数据并强调“相同时相差异”，在 Landsat 时序上提升作物类别准确性，为矿区时间序列 SOC/裸地演变监测提供方法学思路[Zhai & Qu, 2018][aeeisp.com].

B. 无人机/地面多光谱与窗口尺度优化（适用于精细矿区调查）  
1) 采样点光谱信息窗口尺度优化 + 多模型（XGBoost、SVR、PLSR）用于无人机多光谱反演土壤含水率，明确“采样点周围平均尺度”对光谱‑土壤属性相关性的影响。研究在喷灌与畦灌条件下通过滑动窗口提取 34 组光谱特征并用交叉验证确定最优窗口尺度，结果表明最优窗口尺度受灌溉方式显著影响（喷灌：11×11~21×21，畦灌：15×15~29×29），并且基于 Pearson 筛选的 XGBoost 模型在玉米灌浆期测试集 R2 可达 0.80–0.83，RMSE 在 0.98%–1.27% 之间，说明窗口尺度与特征筛选对 UAV‑反演精度影响显著且可被工程化[无人机多光谱窗口尺度优化, 2024][agri.nais.net.cn].  
2) 工程启示：对矿区小尺度异质斑块（回填层、冶金粉尘堆），应在取样设计阶段并行优化空间均值窗口以减少像元混合与表面粗糙度噪声。

C. 近红外/中红外与 FTIR‑PAS 实验光谱与化学计量学（实验室/便携式检测）  
1) 近五年中国近红外光谱技术综述（方法学、便携化与在线分析、深度学习在光谱的应用）。该综述系统梳理了 2019–2023 年 NIR 在化学计量学、自动编码器/深度卷积网络、模型传递（无标样/半监督）和便携设备上的进展，指出深度学习能显著提升特征学习与建模稳健性，但存在超参数优化、可解释性与小样本迁移问题；并强调标准化数据库与工业/团体标准对现场 SOC/NIR 扩展应用的关键作用（对矿区现场快检与设备一致性极具参考价值）[Chen et al., 2024][cdn.sciengine.com].  
2) FTIR‑PAS 在病害诊断上的深度分层光谱示例表明：深层（慢速度测量）与浅层（快速度测量）光谱可被区分并用于背景扣除后探测微量病原或化学特征；该方法的 R1650/1050 比值被提出为可解释的判别指标（阈值 0.5 在样本集中总体准确率 87%、F1 0.91，潜育期诊断准确率 80%）—这一实验证明光声 FTIR 对浅表—深层信号分离具有灵敏性，提示其在矿区含机化合物或碳组分快速定性方面的潜在用途（尽管需针对 SOC 成分做专门标定）[FTIR‑PAS 稻瘟病诊断, 2025][aeeisp.com].

D. SOC 组分机理研究（帮助解释光谱信号；对矿区深层/矿物结合态尤其重要）  
1) 内蒙古草地 0–2 m 剖面 POC 与 MAOC 的系统观测（Science China Earth Sciences, 2025）揭示：POC 在绝大多数层位占主导且随深度下降更快，MAOC 对 SOC 稳定性贡献受黏粒/粉粒及铝氧化物控制并呈深度依赖性；冗余分析与结构方程模型显示黏粒/粉粒、Al 氧化物、pH 与年均降水量是解释差异的主要因子。结论指向：在以矿物为主的土壤（如含大量矿渣/氧化物的矿区），矿物结合态（MAOC）和细粒矿物表面积对长期碳稳定性有关键影响，提示光谱模型在矿区必须同时考虑粒径与矿物相参数以减少偏差[Zheng et al., 2025][sciengine.com].  
2) 太行山南麓不同土地利用下 SOC/SOCD 垂向分布研究（2025）提供了土地利用（包括荒地/耕地/林地）对表层 SOC 与密度的量化基线（0–40 cm SOC 平均范围 ≈9.46×10^-3–15.13×10^-3，SOCD 约 1.33–2.27 kg·m^-2），可为矿区近邻对照与基线比对提供参考[太行山南麓, 2025][cgsjournals.com].

E. 变化检测、长时序和模型迁移（对矿区复垦与长期监测重要）  
1) 随时间的撂荒/休耕/土地退耕识别采用 RF + LandTrendr 在 GEE 平台进行长时间序列 LandTrendr 变化检测并结合 RF 分类，得到 2004–2022 年撂荒耕地高精度提取（F1≈0.87–0.89），展示了变化检测工具与机器学习结合以提取长期地表利用/裸露和植被恢复信息的可行性，适合用于矿区复垦监测的时空模式识别[RF + LandTrendr, 2025][aeeisp.com].  
2) 场景级中层/深度特征学习（如 DSIFT+LLC+SPM+SVM 的多特征级联）提升了复杂地物（含裸地/建筑/矿区土壤）在高分影像上的判别能力，为用遥感影像自动化识别矿区裸露补丁及掩埋材料类型提供方法学参考（但需针对光谱差异进行定制化训练）[Liu et al., 2016][aeeisp.com]。

实验与评价总结（共性结论，不逐篇复述）  
- 光谱预处理与波段选择决定模型上限：去包络线（CR）、分数阶微分（FOD）、一阶微分等能突出吸收特征并提升与 SOC/成分的相关性；而 sCARS/CARS、主成分或稀疏编码用于去冗余后可明显提升机器学习模型拟合与泛化。  
- 机器学习模型表现与数据与特征工程同等重要：在样本量有限的研究中，随机森林与基于树的 XGBoost 多次被证明对高维光谱特征鲁棒；深度学习在大样本与跨仪器传递场景中显示优势，但需解决超参数与可解释性。  
- 土壤物理化学背景必须并入模型：颗粒组成（黏/粉/砂）、矿物氧化物含量（Fe/Al）、含水率与 pH 对光谱信号具有主导影响，尤其在矿区常见矿渣/氧化物共存时，忽视这些协变量会导致系统偏差。  
- 空间尺度与采样策略关键：无人机/场采的“信息窗口尺度”直接影响混合像元噪声；矿区高异质性要求分层/分区采样与局部校正以避免模型跨区域失效。  
- 时序与变化检测方法对复垦评估有效：结合长时序变化检测与分类（LandTrendr+RF、LE‑wDTW 等）可识别植被恢复和裸露重新暴露，适合矿区长期监测，但需解决成像断档与云/尘干扰。

趋势与挑战（2025 年前后的可验证预测，≥3 点）  
1) 物理‑机制驱动的光谱‑SOC 模型将成为主流：单纯统计回归会向“光谱 + 土壤颗粒/矿物量测（如 XRF/XRD） + POC/MAOC 分馏结果”联合建模转变，尤其在矿区，MAOC 与黏粒/Al、Fe 关系将被纳入先验约束以提高长期稳定性预测（参见内蒙古剖面工作）[sciengine.com]。  
2) 分数阶微分、深度特征学习与可解释 band‑selection 的耦合技术会被更多工程化采用：FOD‑sCARS 等混合特征变换被证明可增强波段‑目标响应并减少冗余，未来将与可解释性约束（例如基于物理的正则化）共同用于矿区 SOC 工程反演[opticsjournal.net; cdn.sciengine.com]。  
3) UAV‑高光谱与窗口尺度自适应采样会成为矿区精细调查常规：研究已显示最优光谱信息窗口随地表管理/灌溉差异而变化，矿区回填/覆土纹理与粗糙度将要求局部优化采样窗口与多角度观测策略以稳定反演精度[agri.nais.net.cn]。  
4) 模型迁移与仪器一致性（无标样或弱标样的域自适应）成关键工程问题：便携仪器、在线与工厂化部署要求模型在不同设备/光源间可靠传递，因此半监督/无监督的模型传递与虚拟标样增强策略将获得更多关注（NIR 综述指出该方向的紧迫性）[cdn.sciengine.com]。  
5) 构建开放、分层的矿区土壤光谱‑元数据集（含 SOC 组分、粒径、矿物、含水率与多传感器观测）将成为研究社区共识；没有此类基准集，跨场景比较与模型通用性评估难以推进（工程与监管部门亦会要求可追溯的基线数据）。

结论  
近年来（2022–2025）关于光谱评估 SOC 的研究在方法上展现出三条相辅相成的路线：一是基于高级光谱变换（FOD、CR）与稀疏/稳定波段选择提升信噪比与相关性；二是将机器学习（RF、XGBoost、深度网络）与物理/化学协变量耦合以提高鲁棒性；三是通过 UAV 与长时序变化检测实现从点到区、从短期到长期的多尺度监测。对于矿区场景，关键在于把矿物学与粒级信息作为必需的协变量、优化采样窗口与尺度，以及发展模型迁移策略与标准化光谱数据库。基于当前证据，未来 3–5 年内可期望物理‑统计混合模型、窗口尺度自适应采样与域自适应传递技术在矿区 SOC 光谱评估中进入工程化应用阶段。

参考文献（按出现次序，均为真实文献或报告；链接以域名标注以便检索）  
1. WU M‑H, DOU S, LIN N, et al. Hyperspectral Estimation of Soil Organic Matter Based on FOD‑sCARS and Machine Learning Algorithm. Spectroscopy and Spectral Analysis, 2025, 45(1):204. [opticsjournal.net](https://www.opticsjournal.net/Articles/OJbd519047b7be4afd/FullText)  
2. Deng Y‑P, Zhu H‑F, Ding H‑X, et al. Identification of the years of returning farmland to forest land using hyperspectral technology. Transactions of the Chinese Society of Agricultural Engineering, 2022, 38(3):66–74. [aeeisp.com](https://www.aeeisp.com/nygcxb/cn/article/pdf/preview/10.11975/j.issn.1002-6819.2022.03.008.pdf)  
3. Chen P, Yang J, Chu X‑L, et al. Research and Application Progress of Near Infrared Spectroscopy Analytical Technology in China in the Past Five Years. Chinese Journal of Analytical Chemistry (review), 2024. [cdn.sciengine.com](https://cdn.sciengine.com/doi/pdfView/A722DAE618B44AFB8AEE3FFF5780D86E)  
4. Zheng H‑J, Zhang S, Wang G‑C, et al. Depth‑dependent accumulation and controls of particulate and mineral‑associated organic carbon in Inner Mongolian grasslands. Science China Earth Sciences, 2025. [sciengine.com](https://www.sciengine.com/doi/pdf/CA33630FAFBB49BBA4E7833698335202)  
5. “基于采样点光谱信息窗口尺度优化的土壤含水率无人机多光谱遥感反演”. 农业机械学报, 2024;55(1):316–327. [agri.nais.net.cn](https://agri.nais.net.cn/literature/casdd/E1A81990-FF9A-4DD0-A3AA-BF02A63C4BDE.html)  
6. PANG G‑T, LIU X‑H, BA Y‑J, et al. Distribution characteristics of soil organic carbon in different land use types at the southern foot of Taihang Mountains. Geological Survey of China, 2025, 12(4):57–67. [cgsjournals.com](https://www.cgsjournals.com/article/doi/10.19388/j.zgdzdc.2024.227)  
7. LV Gao‑Q, YILIMUNUER W, SHAN D, et al. Spectral characteristics and incubation period diagnosis technology of rice blast disease based on FTIR‑PAS. (FTIR‑PAS application example) 2025. [aeeisp.com](https://www.aeeisp.com/article/doi/10.11975/j.issn.1002-6819.202505101)  
8. “结合RF和LandTrendr算法的黄河流域下游撂荒耕地提取与时空变化分析”. 农业工程学报 / AEEISP, 2025 (RF + LandTrendr 长时序变化提取案例). [aeeisp.com](https://www.aeeisp.com/nygcxb/cn/article/id/49599613-c390-49d0-9a6f-17ce1e651be4)  
9. Liu Y, Wang L, Zhang B, Men J. Scene‑level land use classification based on multi‑features soft‑probability cascading. Transactions of the Chinese Society of Agricultural Engineering, 2016. [aeeisp.com](https://www.aeeisp.com/nygcxb/cn/article/pdf/preview/10.11975/j.issn.1002-6819.2016.22.037.pdf)  
10. Zhai Y‑G, Qu Z‑Y. Crop classification based on nonlinear dimensionality reduction using time series remote sensing images (LE‑wDTW). Transactions of the Chinese Society of Agricultural Engineering, 2018. [aeeisp.com](https://www.aeeisp.com/nygcxb/cn/article/pdf/preview/10.11975/j.issn.1002-6819.2018.19.023.pdf)  
11. “基于高光谱技术的退耕还林地年限判别” — 土壤高光谱特征与去包络线/CR‑PCA 应用示例, 2022. [aeeisp.com](https://www.aeeisp.com/nygcxb/cn/article/pdf/preview/10.11975/j.issn.1002-6819.2022.03.008.pdf)  
12. （综述与方法学背景中引用之工程/方法论文汇总）近红外光谱方法学、仪器便携化、模型传递与深度学习若干代表作，详见 Chen et al., 2024（综述）[cdn.sciengine.com].

（注：上述文献均来自公开可检索的期刊/会议/期刊集合与期刊网站。文中数值与结论均基于各文献实验段落所披露的指标与结论。用户如需我把每篇论文的 DOI/原文 PDF 列表化并按 BibTeX 导出，可继续要求，我将基于公开资源逐条整理。）