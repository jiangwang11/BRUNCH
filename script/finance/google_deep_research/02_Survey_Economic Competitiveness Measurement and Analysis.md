经济竞争力测度与分析：范式重构、多维融合与前沿方法（2022–2025 年学术综述）
1. 引言：全球变局下的竞争力测度新视野
在 2022 至 2025 年这一充满动荡与变革的历史时期，全球经济格局经历了根本性的重塑。后疫情时代的供应链断裂、地缘政治博弈的加剧（特别是中美战略竞争的深化）、以及以人工智能和绿色转型为代表的“双重转型（Twin Transition）”，共同构成了这一时期经济发展的宏观背景。在这一背景下，传统的经济竞争力测度体系——往往基于静态的 GDP 总量、贸易总额或简单的显示性比较优势（RCA）指数——已显得捉襟见肘，无法准确捕捉国家、区域及微观企业在复杂网络中的真实位势与控制力。

学术界与政策制定者在这一时期展开了密集的理论探索与方法论革新。“经济竞争力”的定义正在从单一的“效率（Efficiency）”向“效率、韧性（Resilience）、安全（Security）与可持续性（Sustainability）”并重的多维复合范式转变。 这一转变不仅体现在测度指标的扩充上，更体现在底层分析逻辑的颠覆：

首先，全球价值链（GVC）的测度逻辑发生了质的飞跃。随着生产工序的碎片化和跨国流动的复杂化，基于总贸易流的统计数据掩盖了真实的价值增值来源。2025 年世界银行发布的最新研究引入了三方分类法（Tripartite Classification），试图在原子层面解构价值链的微观路径，从而更精确地识别国家在特定生产环节（如上游研发或下游组装）的真实依赖度与控制力 。   

其次，数字化与绿色化的协同效应成为新的测度焦点。数字经济不再被视为一个独立的部门，而是作为一种通用目的技术（GPT），渗透至传统产业并重塑其绿色全要素生产率（GTFP）。研究者们利用超效率 SBM 模型（Super-SBM）和耦合协调度模型，试图量化“数据要素”如何替代传统能源要素，从而在不牺牲经济增长的前提下实现环境绩效的提升 。   

最后，数据科学方法的引入彻底改变了微观竞争力的评价手段。面对传统财务指标的滞后性，2022–2025 年间的文献大量采用了自然语言处理（NLP）、文本挖掘和机器学习（Machine Learning）技术。通过对年报、CEO 致辞及专利文本的深度挖掘，研究者能够实时捕捉企业的战略导向、ESG（环境、社会和治理）承诺及潜在的漂绿行为。机器学习模型（如 XGBoost、随机森林）与传统数据包络分析（DEA）的结合，更是将效率评价从“历史回溯”推向了“未来预测”的新高度 。   

本综述旨在系统梳理 2022–2025 年间关于经济竞争力测度与分析的代表性学术工作。全报告将分为六个主要部分：第二部分深入探讨全球价值链网络视角的测度创新；第三部分分析数字经济与绿色转型的协同测度方法；第四部分聚焦于数据科学驱动的微观评价革命；第五部分专门讨论 ESG 评级分歧及其聚合测度难题；第六部分展望 2025 年后的测度趋势，特别关注 AI 算力与能源约束下的新竞争逻辑。

2. 全球价值链（GVC）测度的结构化转向：从流量到网络拓扑
在全球生产网络高度纠缠的今天，一个国家或产业的竞争力不再仅仅取决于其出口的绝对规模，而更多地取决于其在网络中的拓扑位置（Topological Position）以及对关键增值环节的控制能力。2022–2025 年的文献显示，GVC 测度正从基于增加值的会计核算向基于复杂网络的结构分析演进。

2.1 新一代价值增值核算：三方分类法的突破
长期以来，基于 Koopman 等人（2014）的 GVC 分解框架是学界的主流标准。然而，随着跨境生产活动的日益复杂，传统的“向后关联（Backward Linkage）”和“向前关联（Forward Linkage）”二分法在处理某些特定贸易模式时显得力不从心，特别是在区分“简单的再出口”与“深度嵌入的复杂生产”方面存在模糊性。

Borin, Mancini 和 Taglioni (2025) 在《世界银行经济评论》上发表的开创性工作，提出了一种新的三方分类法（Tripartite Classification），为精确测度 GVC 参与度提供了新的显微镜。这一方法依据价值增值的来源与去向，将 GVC 活动严格划分为三类：

分类名称	定义描述	经济含义与竞争力启示
纯向前参与 (Pure-Forward)	处于价值链的起始阶段。指本国创造的增加值被出口给直接贸易伙伴，并由该伙伴再出口到第三国。	反映了处于上游的国家（如原材料供应国或核心技术研发国）在价值链源头的控制力。这类参与通常意味着较高的技术含量或资源垄断性。
纯向后参与 (Pure-Backward)	处于价值链的最终环节。指进口的中间投入品（可能经过多次跨境）被用于本国最终产品的生产。	反映了处于下游的国家（如组装中心）的最终需求满足能力。传统指标往往高估此类国家的竞争力，因为其中包含了大量非本国创造的价值。
双向参与 (Two-Sided)	处于价值链的中间位置。指进口的中间品被嵌入本国出口产品中，并由贸易伙伴再次出口。	反映了国家作为“枢纽”或“中转站”的能力。这是深度参与全球分工的标志，但也意味着对外部供需的双重依赖，韧性风险较高。
核心发现与纠偏效应： 利用这一新分类法对全球投入产出数据进行重新测算，Borin 等人发现：

传统指标的低估偏差：传统的基于贸易总值的 GVC 指标显著低估了服务业和上游制造业的全球活动规模。这是因为服务业往往隐含在制成品贸易中，只有通过基于 GDP 和生产数据的综合测度才能被准确捕捉 。   

风险感知的修正：传统指标往往高估了贸易自由化早期的供应链风险，而新的测度显示，通过多元化的“双向参与”，国家实际上可能通过分散化来降低特定冲击的影响。

向后关联的“虚高”：传统的二分法倾向于将许多模糊的中间品贸易归类为向后关联，从而高估了下游组装环节的价值贡献。修正后的数据表明，许多新兴市场国家虽然出口额巨大，但其实际掌握的价值增值环节（即真实的竞争力）远低于预期 。   

2.2 复杂网络分析（CNA）与熵值法的应用
除了会计核算方法的改进，**复杂网络分析（Complex Network Analysis, CNA）**在 2022–2025 年间成为了测度竞争力的主流工具。这种方法将国家或行业视为节点，贸易流视为连边，利用拓扑学指标来评估竞争条件。

熵与网络信息的测度： Angelidis (2020/2024) 等学者的研究将信息熵（Entropy）引入 GVC 分析。在一个完全竞争且随机连接的网络中，熵值通常较高；而在一个由少数核心国家主导的等级制网络中，熵值较低。通过计算网络的熵值变化，研究者可以量化全球生产体系的集中度演变 。   

中心度指标的经济学解释： 不同的中心度指标被赋予了明确的经济含义，用于捕捉不同维度的竞争力 ：   

度中心度（Degree Centrality）：反映一国直接贸易伙伴的数量和贸易量。这是衡量市场广度的基础指标。

特征向量中心度（Eigenvector Centrality）：不仅看“你有多少伙伴”，还看“你的伙伴有多重要”。如果一国与美国、德国、中国等核心节点有紧密联系，其特征向量中心度就会很高。实证数据显示，虽然许多发展中国家的度中心度在提升，但在特征向量中心度上，美、德、中三大枢纽的地位依然稳固，甚至在某些高技术领域有所强化 。   

介数中心度（Betweenness Centrality）：反映一国在网络中作为“桥梁”的能力。介数中心度高的国家掌握着贸易流动的“控制权”和“阻断权”，这在地缘政治博弈中被视为一种战略资源。

数字化对网络中心化的影响： Yuan 等人 (2025) 利用异质性企业模型结合跨国面板数据（2004–2014及后续更新），深入研究了数字经济发展如何重塑 GVC 网络结构。其研究发现：

促进中心化（Centralization）：数字经济的发展显著提升了一个国家在 GVC 网络中的中心度。这种提升并非偶然，而是具有统计显著性的因果关系 。   

双重作用机制：

生产率渠道：数字化降低了企业的边际生产成本和贸易协调成本，使得本国企业能够以更有竞争力的价格进入更多市场，从而提升连接度（Melitz 模型逻辑）。

资源配置渠道：人工智能和大数据技术缓解了劳动力与资本的错配（Resource Misallocation），用高效的算法替代了低效的通用劳动力，增强了该国作为全球生产节点的吸引力 。   

异质性效应：这种“数字化-中心化”的正向反馈在发达国家和制度质量较高的行业中更为显著，暗示了数字红利分配的不均衡性。

2.3 供应链韧性与外部依赖度测度
在地缘政治紧张局势下，“安全性”成为了竞争力测度的硬指标。2025 年《全球价值链发展报告》指出，企业正在通过区域化和多元化来重构供应链，这要求测度体系必须能够捕捉这种结构性变化 。   

中间品外部依赖度： 针对中国制造业的一项案例研究（2022/2024）提出了细化的“中间品外部依赖度”指标。该指标不只计算进口比例，还结合了进口来源国的集中度（HHI 指数）和该中间品的不可替代性（如技术复杂度或专利集中度）。结果显示，尽管中国在总产出上占据全球主导地位（2023 年制造业增加值达 15.5 万亿美元，占全球 78.6% 的工业产出份额 ），但在特定关键中间品上仍存在较高的非对称依赖，这是其竞争力的软肋 。   

3. 数字经济与绿色转型的双重竞争力测度：协同与耦合
“数字化（Digitalization）”与“绿色化（Greening）”被欧盟委员会称为“双重转型（Twin Transition）”。2022–2025 年的文献不再孤立地看待这两个过程，而是聚焦于测度二者之间的协同效应（Synergy）与耦合协调度（Coupling Coordination）。核心问题在于：数字技术究竟是增加了能源消耗，还是通过效率优化成为了绿色转型的杠杆？

3.1 宏观与区域层面：城市土地绿色利用效率（ULGUE）
在城市经济学领域，测度的核心从单纯的土地产出率转向了城市土地绿色利用效率（Urban Land Green Use Efficiency, ULGUE）。这是一种综合考量经济产出与环境成本的的全要素生产率指标。

Super-SBM 模型的应用： 为了准确测度 ULGUE，研究者广泛采用了超效率 SBM（Super-Slack-Based Measure）模型。

方法论优势：传统的 DEA 模型（如 CCR 或 BCC）无法有效处理非期望产出（如废水、废气、CO2），且由于效率值封顶为 1，难以区分多个高效决策单元的优劣。Super-SBM 模型通过引入非期望产出变量，并允许效率值大于 1，克服了这些缺陷，提供了更精细的排序能力 。   

实证研究：基于中国 282 个地级市（2007–2022）的面板数据研究显示，数字经济发展与 ULGUE 之间存在显著的正相关关系。

测度指标：数字经济发展通常通过“宽带中国”或“国家电子商务示范城市”政策作为代理变量，利用双重差分法（DID）进行因果识别。

机制验证：研究证实了“创新驱动的资源配置优化”路径。数字化通过促进绿色技术创新（Green Technology Innovation）和提高资源利用效率（Resource Use Efficiency）两个中介变量，显著降低了单位 GDP 的土地和能源消耗 。   

空间溢出效应（Spatial Spillovers）：利用空间杜宾模型（SDM-DID）的测度发现，数字经济的红利具有极强的辐射性。核心城市的数字化不仅提升了自身的绿色效率，还通过技术扩散和产业关联，带动了周边 300 公里范围内城市的效率提升（Diffusion-Coordination-Progress 机制） 。   

区域异质性的量化： 测度结果显示出明显的区域梯度。数字经济对 ULGUE 的提升作用在东部沿海地区和早期试点城市最为强烈，呈现出一种“强者愈强”的马太效应；中部次之；西部地区由于基础设施薄弱，其提升效果最弱。这提示政策制定者，数字基础设施的均衡布局是缩小区域绿色竞争力差距的关键 。   

3.2 微观企业层面：绿色创新与企业价值的耦合
在微观层面，研究重点转向测度企业如何利用数字化实现“绿色”与“盈利”的双赢。

电容耦合系数模型（Capacitive Coupling Coefficient Model）： 受物理学中电容耦合概念的启发，研究者构建了用于测度**绿色创新（GI）与企业价值（CV）**之间互动强度的耦合模型。

指标构建：

实质性协同（Substantive Synergy）：测度高质量的绿色发明专利与企业长期价值（如 Tobin's Q）的共振。

策略性协同（Strategic Synergy）：测度低质量的绿色实用新型专利与短期财务绩效的关系 。   

测度发现：2024 年发表在《PLOS ONE》上的研究利用中国上市公司数据（2011–2020）证实，数字经济是驱动 GI 与 CV 从“低水平耦合”向“高水平协调”跃升的核心动力。

调节效应测度：通过引入交互项（Interaction Terms），研究发现政府的环境规制和绿色补贴显著增强了这种协同效应。换言之，在严格的环保执法和积极的财政支持下，企业的数字化投入更容易转化为绿色竞争优势 。   

行业差异：一个反直觉的测度结果是，数字经济对非重污染企业的协同效应促进作用强于重污染企业。这可能是因为非重污染企业（如高技术制造、服务业）的资产结构更轻，更容易进行数字化改造和流程重组，而重污染企业的转型包袱更重 。   

4. 数据科学驱动的微观评价方法：从历史数据到预测性分析
2022–2025 年间，经济竞争力分析方法论最显著的变化是数据科学（Data Science）技术的全面渗透。传统的计量经济学方法（解释过去）正在与机器学习方法（预测未来）深度融合。

4.1 文本挖掘与战略一致性测度
企业的年报、社会责任报告（CSR/ESG 报告）以及管理层讨论与分析（MD&A）包含了大量关于企业战略、风险感知和未来规划的非结构化信息。传统的财务指标无法捕捉这些软信息，而**自然语言处理（NLP）**技术填补了这一空白。

词频分析与战略聚类： 2025 年的一项研究对 2021–2023 年间的 390 份 CEO 致辞进行了深度文本挖掘。

TF-IDF 算法：用于识别最具区分度的关键词。分析发现，“ESG”、“Sustainable”、“Society”、“Stakeholders”是出现频率最高且权重最大的词汇，表明可持续发展已从边缘话题进入核心战略话语体系 。   

CONCOR（迭代相关收敛）分析：通过计算关键词之间的共现网络，研究者识别出了四大战略集群：

技术竞争力集群（Technology, Competitiveness, Innovation）：反映企业通过研发构建护城河的意图。

生态友好能源集群（Carbon, Eco-friendly, Energy）：反映企业的脱碳路径。

ESG 管理集群（Governance, Growth, Customer）：反映企业的利益相关者治理模式。

全球危机应对集群（COVID-19, Global, Crisis）：反映企业的韧性建设 。   

网络中心度分析：在语义网络中，“Sustainable”和“Innovation”具有最高的介数中心度，说明它们是连接其他战略目标的枢纽。如果一家企业的 CEO 致辞中缺失这些核心节点，往往预示着其战略竞争力的脱节。

检索增强生成（RAG）与财务分析： 为了解决大语言模型（LLMs）在处理专业财务数据时的“幻觉”问题，2025 年的研究引入了**检索增强生成（Retrieval-Augmented Generation, RAG）**技术。

应用场景：自动分析上市公司的年度报告，提取关键财务比率和定性风险披露。

效能评估：对比实验显示，引入 RAG 后，AI 生成的财务分析报告在**相关性（Relevance）上提升了 0.66 分（5 分制），在可验证性（Verifiability）**上提升了 0.71 分。这使得基于大规模文本分析的自动化竞争力评价成为可能，大大降低了投资者和监管机构的信息处理成本 。   

4.2 机器学习与 DEA 的融合：效率的预测性测度
数据包络分析（DEA）是测度多投入-多产出效率的经典方法，但其本质是静态的、基于历史数据的。2023–2025 年的研究前沿是将 DEA 与**机器学习（Machine Learning, ML）**结合，构建“预测性效率评价框架”。

混合框架的构建逻辑：

第一阶段（测度）：利用 SBM-DEA 或 Super-SBM 模型计算决策单元（如企业、城市）的历史效率得分。

第二阶段（训练）：将计算出的效率得分作为目标变量（Label），将企业的特征变量（财务数据、宏观环境、文本特征等）作为输入，训练非线性机器学习模型。

第三阶段（预测）：利用训练好的模型预测未来的效率走势 。   

实证案例与精度比较：

秘鲁区域竞争力预测：研究者利用梯度提升（Gradient Boosting）、随机森林（Random Forest）、XGBoost 等六种算法预测秘鲁 25 个区域的竞争力指数。结果显示，梯度提升和随机森林模型的预测精度（R² > 0.97）远超传统的线性回归模型和神经网络。这证明了竞争力决定因素之间存在复杂的非线性交互关系，只有树模型等非线性算法才能有效捕捉 。   

越南中小企业（MSMEs）绩效：针对 5400 多家中小企业的研究表明，DEA-ML 混合模型在预测企业生存率和增长潜力方面表现优异，能够帮助银行和投资者更早识别出具有高竞争力的“隐形冠军” 。   

云服务产业动态：结合 Super-SBM 和 Bootstrap 重采样技术，研究者成功预测了美国云计算领军企业在 2021–2024 年间的 Malmquist 生产率指数（MPI），揭示了技术进步而非纯技术效率改善是该行业竞争力的主要驱动力 。   

5. ESG 评级分歧与聚合测度难题
虽然 ESG 已成为衡量企业长期竞争力的“第四张报表”，但 2024–2025 年的文献集中揭示了 ESG 评级中的**“总体混淆（Aggregate Confusion）”**现象，即不同评级机构对同一企业的评价存在巨大分歧。这种分歧严重干扰了对企业真实竞争力的判断。

5.1 评级分歧的来源测度
研究者将 ESG 评级分歧分解为三个维度进行量化 ：   

范围分歧（Scope Divergence）：不同机构选择的指标集不同（例如，一家机构考量生物多样性，另一家不考量）。

测量分歧（Measurement Divergence）：对同一指标的测量方法不同（例如，碳排放是计算总量还是强度，是否包含 Scope 3）。

权重分歧（Weight Divergence）：对不同指标赋予的权重不同（例如，环境 E 和社会 S 哪个更重要）。

实证数据显示，Scope 和 Measurement 分歧是导致评级不一致的主要原因。这种分歧导致 ESG 评级之间的相关系数往往低于 0.5，远低于信用评级（通常高于 0.9） 。   

5.2 解决方案：聚合与共识构建
为了获得更稳健的竞争力评价，学术界提出了一系列聚合方法：

机器学习聚合：利用无监督学习（如 PCA）提取多源评级的公共因子，或利用监督学习（如 XGBoost）预测市场反应，从而构建一个“最优共识分” 。   

元分析（Meta-Analysis）证据：2025 年的一项涵盖 83.5 万个观测值的元分析显示，尽管存在评级噪音，数字化转型总体上对 ESG 绩效有显著正向影响。但这种影响受到行业属性的强烈调节：在制造业和服务业中，数字化对 ESG 的提升效果更为明显，而在采矿业等传统行业则较弱 。   

6. 行业特定竞争力分析：制造、算力与服务
不同行业的竞争力逻辑在 2022–2025 年间呈现出截然不同的演化轨迹。

6.1 制造业：增加值与规模优势的固化
根据 2024 年《国际工业统计年鉴》，2023 年全球制造业增加值达到 15.5 万亿美元（2015 年不变价）。尽管这也面临着去工业化的讨论，但数据表明制造业依然是全球经济竞争的压舱石。GVC 参与度依然是制造业出口竞争力的最强解释变量，尤其是在促进全要素生产率（TFP）和产业升级方面 。   

6.2 AI 与算力产业：能源约束下的新竞争
随着生成式 AI 的爆发，半导体和算力产业的竞争力测度出现了新的维度：能源效率。

算力需求激增：预计到 2026 年，数据中心、AI 和加密货币的电力需求将翻倍，达到 1000 TWh 以上 。   

能源瓶颈：未来的竞争力不仅取决于“拥有多少 GPU”，还取决于“能否提供足够的清洁能源来运行这些 GPU”。能源成本和电力获取能力（Access to Electricity）正在成为衡量数字竞争力的关键约束条件。

市场预测：生成式 AI 芯片市场预计在 2025 年将超过 1500 亿美元，但这部分价值将高度集中在少数能够解决“能耗-算力”平衡的企业和国家手中 。   

6.3 生产性服务业：制造业的赋能者
服务业，特别是知识密集型服务业（KIBS），被证实是制造业竞争力的重要来源。针对中国制造业与生产性服务业协同集聚（Collaborative Agglomeration）的研究表明，这种空间上的共生关系显著降低了制造业的成本并提升了创新能力。网络分析显示，服务贸易网络的中心度与制造业 GVC 位置的攀升存在显著的正相关 。   

7. 2025 年后的趋势展望：迈向实时、安全与智能的测度体系
基于当前的文献前沿和主要国际机构（OECD, IMF, Deloitte）的预测报告，未来的经济竞争力测度将呈现以下三大趋势：

7.1 算力与能源的耦合测度（The Compute-Energy Nexus）
随着 AI 模型训练成本的指数级增长，单一的数字指标将失效。未来的指标体系将显性包含**“单位算力碳排放”和“能源自主性”**。对于发展中国家而言，缺乏廉价且稳定的电力可能成为数字时代的“贫困陷阱”，导致其在全球数字分工中被边缘化 。   

7.2 安全性与地缘政治距离的量化
“效率优先”的时代已终结。未来的 GVC 测度将引入更多政治经济学变量：

地缘政治距离（Geopolitical Distance）：在贸易引力模型中加入基于投票记录或联盟关系的权重。

友岸外包指数（Friend-shoring Index）：测度供应链中有多少比例位于盟友国家。

冗余度（Redundancy）：将供应链的闲置产能和多元化程度视为正向资产而非效率损失 。   

7.3 从“年度体检”到“实时监测”
依托大数据和 AI，竞争力评价将从年度报告转变为实时仪表盘（Dashboard）。

卫星遥感数据：实时监测工业园区活动和港口吞吐量。

高频交易数据与网络搜索：实时捕捉市场情绪和消费者偏好。

预测性模型：机器学习模型将成为标准配置，用于模拟外部冲击（如关税、疫情、断供）下的系统反应，从而实现竞争力的“压力测试（Stress Testing）” 。   

8. 结论
2022 至 2025 年，经济竞争力测度与分析领域经历了一场深刻的方法论革命。我们见证了从“贸易总值”向“三方价值增值”的核算回归，从“原子式个体”向“复杂网络节点”的视角转换，以及从“单一经济指标”向“数字-绿色-安全多维协同”的范式重构。

Borin 等人的三方分类法和 Angelidis 等人的熵值网络分析，为我们理解全球价值链的权力结构提供了新的透镜，揭示了隐藏在流量背后的控制力。数字经济与绿色转型的协同测度研究，通过 Super-SBM 和耦合模型，证实了数字化是实现可持续竞争力的关键杠杆，但这一杠杆的效用受到区域和行业特征的显著制约。最令人振奋的是，NLP 和机器学习等数据科学工具的引入，使得微观层面的战略一致性分析和预测性效率评价成为可能，极大地拓展了竞争力分析的颗粒度和前瞻性。

展望未来，随着 AI 技术的指数级进步和地缘政治格局的固化，经济竞争力的内核将更加侧重于系统的生存能力（Viability）与进化适应性（Adaptability）。对于研究者而言，掌握跨学科的测度工具，将复杂的非线性关系和非结构化数据纳入分析框架，将是解读未来经济竞争密码的关键。

参考文献索引表
为便于查阅，下表总结了本综述引用的核心文献及其对应的方法论贡献：

领域分类	核心方法/理论模型	代表性文献 ID	关键贡献与发现
GVC 测度	三方分类法 (Tripartite Classification)		纠正了传统指标对上游和服务业的低估；区分纯向前/纯向后/双向参与。
GVC 网络	复杂网络分析 (CNA), 熵值法		利用中心度（度、特征向量、介数）测度网络控制力；证实数字化促进 GVC 中心化。
供应链安全	外部依赖度测度, 网络级联失效模型		量化中间品进口依赖与不可替代性；模拟供应链断裂风险。
数字-绿色协同	Super-SBM 模型, 耦合协调度模型		解决非期望产出测度问题；证实数字化通过资源配置优化提升 ULGUE 和 ESG 协同。
文本挖掘	NLP, TF-IDF, CONCOR 聚类, RAG		从 CEO 致辞提取“技术”、“生态”战略集群；利用 RAG 提升财务分析可验证性。
效率预测	DEA + 机器学习 (Random Forest, XGBoost)		构建两阶段混合模型，实现对区域和企业未来效率的高精度非线性预测。
ESG 评价	评级分歧分解, 元分析 (Meta-Analysis)		将分歧分解为范围、测量、权重维度；通过元分析确认数字化对 ESG 的正向影响。
产业洞察	算力-能源约束分析		提出算力与能源效率是未来 AI 时代竞争力的核心约束。
  

academic.oup.com
Economic Consequences of Trade and Global Value Chain ...
在新窗口中打开

frontiersin.org
How does digital economy development influence urban ... - Frontiers
在新窗口中打开

journals.plos.org
Can digital economy foster synergistic increases in green innovation ...
在新窗口中打开

pmc.ncbi.nlm.nih.gov
Assessing regional competitiveness in Peru: An approach using ...
在新窗口中打开

ideas.repec.org
Predicting the performance of MSMEs: a hybrid DEA-machine ...
在新窗口中打开

researchgate.net
(PDF) Competitive Conditions in Global Value Chain Networks: An Assessment Using Entropy and Network Analysis - ResearchGate
在新窗口中打开

journals.plos.org
Digital economy development and global value chain network ...
在新窗口中打开

edspace.american.edu
Global Value Chain Development Report 2025 – Executive Summary - EdSpace
在新窗口中打开

ideas.repec.org
Firm-Level Analysis of Global Supply Chain Network: Role of Centrality on Firm's Performance - IDEAS/RePEc
在新窗口中打开

pmc.ncbi.nlm.nih.gov
Can digital economy foster synergistic increases in green innovation and corporate value? Evidence from China - PubMed Central
在新窗口中打开

mdpi.com
Trends of CEO Messages in Corporate Sustainability Reports: Text ...
在新窗口中打开

mdpi.com
Analysis of Large Language Models for Company Annual Reports Based on Retrieval-Augmented Generation - MDPI
在新窗口中打开

researchgate.net
DEA and Machine Learning for Performance Prediction - ResearchGate
在新窗口中打开

mdpi.com
Effective Decision Making: Data Envelopment Analysis for Efficiency Evaluation in the Cloud Computing Marketplaces - MDPI
在新窗口中打开

academic.oup.com
Aggregate Confusion: The Divergence of ESG Ratings* | Review of Finance | Oxford Academic
在新窗口中打开

pmc.ncbi.nlm.nih.gov
Divergence and aggregation of ESG ratings: A survey - PMC
在新窗口中打开

tandfonline.com
Full article: Digital levers for sustainability: a meta-analytic review of digital transformation's influence on ESG performance - Taylor & Francis
在新窗口中打开

tandfonline.com
Digital levers for sustainability: a meta-analytic review of digital ...
在新窗口中打开

dco.org
DIGITAL ECONOMY TRENDS 2025
在新窗口中打开

deloitte.com
2025 Global Semiconductor Industry Outlook - Deloitte
在新窗口中打开

jorae.cn
Topological Characteristics and Influencing Factors of the Global Productive Service Trade Network Based on a Social Network Analysis Method - Journal of Resources and Ecology
在新窗口中打开

bioone.org
Topological Characteristics and Influencing Factors of the Global Productive Service Trade Network Based on a Social Network Analysis Method - BioOne Complete
在新窗口中打开

oecd.org
General assessment of the macroeconomic situation: OECD Economic Outlook, Volume 2025 Issue 1
在新窗口中打开

dhs.gov
Improving United States Economic Competitiveness in the Global Market - Homeland Security
在新窗口中打开

academic.oup.com
geopolitical underpinning of global value chains and production networks: US–China technological rivalry in a longer-range perspective | Journal of Economic Geography | Oxford Academic
在新窗口中打开

mdpi.com
Digital–Intelligent Transformation and Urban Carbon Efficiency in the Yellow River Basin: A Hybrid Super-Efficiency DEA and Interpretable Machine-Learning Framework - MDPI
在新窗口中打开

mdpi.com
ESG Rating Divergence: Existence, Driving Factors, and Impact Effects - MDPI