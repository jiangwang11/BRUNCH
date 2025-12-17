引言  
混沌（chaos）系统因初值敏感性、伪随机性和遍历性而被大量用于图像加密设计。近几年（特别是 2022–2025 年）研究呈现出三个实用导向：混合/高维混沌映射以扩大密钥空间与提高随机性；将生物编码（DNA/RNA）或位平面操作与混沌置换/扩散结合以增强比特级安全性；以及将混沌与哈希、变换域/可逆嵌入、压缩感知等传统密码或信号处理方法耦合以提升明文敏感性与抗攻击性。下文对方法类别进行分类综述并给出代表性工作（每篇 4–6 句，突出问题、方法与关键实验结论），随后对实验评估的共性结论、存在的局限与 2025 年前后的研究趋势做出预测。

方法分类与代表作  
1) 置换–扩散框架与混合/高维混沌映射（Permutation–Diffusion, mixed/hyperchaotic）  
- Andono & Setiadi (IEEE Access, 2022) — 改进的像素/比特混淆-扩散，采用混合混沌映射并在扩散中嵌入哈希操作以增加明文与密钥耦合。方法在像素级与比特级分别实现置乱与扩散，利用哈希改变密钥流以提高对选择明文攻击的敏感性。作者在标准测试图像上用 NPCR、UACI、信息熵和相邻像素相关性进行评估，报告密钥空间和差分指标满足抗差分分析的典型阈值（NPCR≈99.6%、UACI≈33% 量级）。论文强调通过混合映射扩大密钥空间与提高序列不可预测性，但并未给出形式化的密码学安全证明。([ieee.org](https://doi.org/10.1109/ACCESS.2022.3218886))

- Liang et al. (Journal of Image and Signal Processing, 2021) — 提出基于斜帐篷映射与广义 Arnold 映射的位平面重构+置乱+两阶段扩散算法。关键在“扩张–收缩”策略：高位比特重构为六位平面并与低位平面交互置换，以弱化位平面间相关性。实验给出 NPCR ≈99.62%、UACI ≈33.50% 和接近 8 的信息熵，验证差分敏感性与位平面均匀化效果。该工作说明将位平面操作与经典置换扩散结合能显著降低高位相关性。([hanspub.org](https://image.hanspub.org/Html/5-2670256_42051.htm))

- Xiao et al. (Journal of Electronics & Information Technology, JEIT, 2024) — 针对卫星图像提出改进型无限折叠混沌映射 + 改进 Chebyshev 映射，并用 SHA‑256 生成密钥流实现一图一密的明文敏感性。方法流程：Hilbert 局部置乱 → 基于混沌状态的 DNA 动态编码（见下类）→ 混沌序列扩散；实验报告 NPCR≈99.61%、UACI≈33.47、信息熵≈7.9976，并给出裁剪攻击的鲁棒性分析（可对部分裁剪恢复）。作者把哈希与混沌结合以提高密钥依赖性，但对抗数学上的已知/选择明文攻击分析较简略。([jeit.ac.cn](https://www.jeit.ac.cn/cn/article/doi/10.11999/JEIT230203))

2) 混沌与 DNA/RNA 动态编码（比特/核酸编码层面的扩散与替代）  
- Xiao et al. (JEIT, 2024) — （同上，作为 DNA 动态编码代表）提出用混沌状态选择 DNA 编码规则以实现规则动态化，旨在解决传统 DNA 编码规则数目有限易被穷举的问题。实验显示将像素在 DNA 级别编码后再做混沌扩散，能在信息熵与差分指标上达到接近理想随机分布的数值。该方法改进点在于“规则随状态变换”，提升了对暴力穷举的抗性，但也引入了实现复杂度和额外的密钥管理开销。([jeit.ac.cn](https://www.jeit.ac.cn/cn/article/doi/10.11999/JEIT230203))

- Wang et al. (Multimedia Tools and Applications, 2019) — 设计基于混沌序列与 DNA 平面操作的彩色图像加密方案：先对高位比特平面重构，再通过混沌序列控制的置乱与 DNA 运算实现扩散。实验报告信息熵接近 8、NPCR/UACI 达到常见安全阈值；文章讨论了 DNA 运算并行性与比特级扩散的实现代价。该类方法展示了将“位平面+DNA运算”作为额外扩散层的可行性。([link.springer.com](https://doi.org/10.1007/s11042-019-07794-9))

- Abbasi et al. / Chai et al. 等（Optics/Opt. Laser Tech., 2017–2020）— 多篇工作把 DNA 或 RNA 编码与混沌/进化算法耦合，用生物编码的置换表或核酸真值表做替代运算（substitution），并用混沌序列控制规则选择或位置置乱。总体实验结论是：生物编码层能在比特/核酸级别提供额外的扩散/替代路径，从而提升 NPCR/UACI 与信息熵，但对密钥管理和规则空间的明确定义常被忽略（易形成安全分析盲区）。（示例：ABBASI et al., Optics & Laser Technology 2020）([jeit.ac.cn](https://www.jeit.ac.cn/#b27))

3) 变换域 / 压缩感知 / 密文域可逆嵌入与混沌耦合  
- Fu et al. (Journal of University of Shanghai for Science and Technology, 2022) — 针对医学 DICOM 图像提出密文域可逆信息隐藏（RDH‑EI），选用块加密 + 多高位比特压缩与块编码在加密域嵌入信息。关键贡献是结合加密时保留部分相关性以提高可嵌入空间，实现嵌入率高达数 bpp（论文在不同块尺寸下给出 τ1≈8.3 bpp 的实验值）并能在持有解密密钥时可逆恢复原始图像。该类工作展示了在高像素深度医学图像中，如何用结构化压缩与加密耦合提高密文域隐藏率。([jns.usst.edu.cn](https://jns.usst.edu.cn/html/2022/3/20220307.html))

- Fang et al. / Liu et al.（遥感/压缩感知方向，若干论文）— 将压缩感知与混沌序列用于遥感图像注册/加密，在云场景下面向带宽/存储约束同时兼顾安全性；实验通常通过可重构性、恢复精度和抗噪性度量系统性能。JEIT 的引用列表指出此方向在遥感/卫星影像安全中被广泛采用。([jeit.ac.cn](https://www.jeit.ac.cn/#b1))

- Fang/许静萱等（西华大学学术期刊网，2024）— 将 Logistic 与 Henon 映射生成的混沌序列嵌入密钥矩阵，配合分数傅里叶变换实现对电力网数据的二次加密；实验表明该方法对字符与图像类数据均能实现无损压缩+加密。该工作是混沌与频域/矩阵变换耦合的应用型示例。([xhuqk.com](https://www.xhuqk.com/xhdxxbzkb/article/doi/10.12198/j.issn.1673-159X.5480))

4) 混沌映射设计与密码学分析（map design & cryptanalysis）—— 理论与工程角度的检验  
- Alvarez & Li (Int. J. Bifurcation & Chaos, 2006) — 讨论混沌基密码系统的基本密码学要求（周期性、可控性、密钥空间、统计性质等），并指出许多混沌方案在形式安全性上存在缺陷（特别是置换-仅或可分离设计易受已知明文攻击）。该综述/分析仍被后续工作作为安全设计准则引用。([springer.com](https://doi.org/10.1142/S0218127406015970))

- 诸多近年工作（参见 JEIT 与 IEEE Access 引用）专注于设计 1D/高维混沌映射（如改进 Tent、Chebyshev、Hénon-类复合映射）并用谱熵、李雅普诺夫指数等动力学指标来量化伪随机性；实证证据通常用统计测试（自相关、频谱）、差分指标与密钥敏感性来论证改进。示例性工程论文见上文 Andono 2022 与 Xiao 2024。([jeit.ac.cn](https://www.jeit.ac.cn/cn/article/doi/10.11999/JEIT230203))

实验与评价总结（只列共性结论）  
- 常用评价指标与阈值：绝大多数工作采用 NPCR、UACI、信息熵（接近 8）、相邻像素相关性、密钥空间估算与密钥敏感性测试作为主要指标；实践中把 NPCR≈99.6% 与 UACI≈33% 作为“差分抗性”目标区间。Xiao et al. 给出的具体数值为 NPCR≈99.6109%、UACI≈33.4681%、信息熵≈7.9976，常被视作可比基准（见 [jeit.ac.cn](https://www.jeit.ac.cn/cn/article/doi/10.11999/JEIT230203)）。  
- 明文敏感性与哈希耦合：近年来倾向用哈希（如 SHA‑256）或明文相关初始值生成密钥流以实现“一图一密”，实证上能显著提高对选择/已知明文攻击的抵抗，但这类做法通常未提供形式化的不可区分性 (IND) 或概率性安全证明。  
- 位平面与核酸编码有效性：比特/位平面的交互置换或 DNA/RNA 编码能在统计层面降低高位比特间的相关性，从而在直方图与相邻像素相关性上获得改进；但生物编码方案若规则集合有限，会引入新的穷举面，需通过动态规则或状态驱动规则来缓解（Xiao 2024 提出动态化规则）。  
- 抗攻击性与分析不足并存：多数文章给出对差分攻击、直方图分析和简单裁剪噪声攻击的实验，但对更强的密码分析（选择明文/密文攻击、线性/差分密码学证明）和实现层面（时空复杂度、硬件随机数种子安全）讨论不足。  
- 运行效率与实现代价：引入 DNA/RNA 编码、位平面扩张-收缩或多阶段置乱会显著增加计算与内存开销；在高分辨率遥感或医学 DICOM 场景，这会成为实际部署的瓶颈，促使近期工作关注并行化或硬件加速实现。

趋势与挑战（2025 年前后预测，≥3 点）  
1. 向“混合密码学”与可证明安全性的转变：单纯基于混沌动力学的经验性指标已不足以说服安全关键应用（遥感/医疗）。未来 2–3 年会更多将混沌序列与标准密码原语（哈希、对称块密码、MAC、PKE 的混合）耦合，并试图给出基于信息论或复杂度假设的安全边界（例如将混沌生成序列作为伪随机函数的实例并量化统计距离）。  
2. 从静态规则到学习/可配置规则的演进，但需防范学习型攻击：动态 DNA/RNA 规则、或用小型神经网络学习初值/参数以生成密钥流，会在性能与抗穷举上带来优势；但同时引入可学习攻击面（对抗样本、模型窃取）。对抗与鲁棒性评估将成为必需。  
3. 标准化基准与可复现评测的需求上升：目前多数论文在不同图像集、不同实现细节下报告 NPCR/UACI/熵，缺少统一基准与开源实现。预计社区会推动建立公开基准集合（包含高分辨遥感、DICOM、普通彩色图像）及对抗性评测套件。  
4. 面向资源受限与实时场景的映射设计：高分辨率卫星图像和实时视频场景要求低延迟与低能耗的加密实现，促生硬件友好型 1D/低维混沌映射与位操作优先的轻量级方案；同时，FPGA/ISA‑acceleration 实证将成为衡量实用性的关键指标。  
5. 密文域可逆处理（RDH‑EI）与可解释性需求并存：医疗/司法图像等场景要求在加密后仍能在密文域嵌入认证/水印/索引信息，且在拥有密钥时可完全恢复原像。混沌方法将更多与可逆嵌入、可验证计算和差分隐私等机制结合，以满足合规需求。  
6. 对抗密码学/量子安全的考量开始出现：虽然混沌方法不直接对应量子脆弱性，但未来研究将考虑与后量子公钥体系的联合部署（例如对称密钥的混沌生成器 + PQC 密钥交换）以应对长期安全性需求。

结论  
2022–2025 年间的混沌系统图像加密研究呈现出从“经验性构造”向“工程化/耦合化”演进的特征：研究者在扩大密钥空间与提高差分敏感性的同时，越来越倾向将混沌与哈希、生物编码、变换域方法耦合以满足应用需求。现有工作的共同短板是缺乏形式化安全证明、可复现的基准与硬件/延迟评估。要将混沌加密推广到遥感、医疗等高安全场景，下一步必须同时改进理论安全分析、构建公开可比的基准与实现效率评测，并研究与标准密码学原语的安全耦合策略。

参考文献（按出现顺序与代表性列出 >=12 篇；链接以域名标注）  
- [jeit.ac.cn](https://www.jeit.ac.cn/cn/article/doi/10.11999/JEIT230203) 肖嵩等. 基于混沌理论与DNA动态编码的卫星图像加密算法. 电子与信息学报, 2024.  
- [hanspub.org](https://image.hanspub.org/Html/5-2670256_42051.htm) Liang J., Su J., Wang J., Ye R. Color Image Encryption Algorithm Based on Chaos and Bit Plane Exchange. Journal of Image and Signal Processing, 2021.  
- [ieee.org](https://doi.org/10.1109/ACCESS.2022.3218886) Andono P. N., Setiadi D. R. I. M. Improved pixel and bit confusion-diffusion based on mixed chaos and hash operation for image encryption. IEEE Access, 2022.  
- [jns.usst.edu.cn](https://jns.usst.edu.cn/html/2022/3/20220307.html) Fu D., Kong P., Zhou L., et al. A reversible data hiding method for encrypted medical image. Journal of University of Shanghai for Science and Technology, 2022.  
- [xhuqk.com](https://www.xhuqk.com/xhdxxbzkb/article/doi/10.12198/j.issn.1673-159X.5480) 方圆等. 密钥矩阵节点变换下电力网络双混沌数据安全加密方法. 西华大学学术期刊网, 2024.  
- [link.springer.com](https://doi.org/10.1007/s11042-019-07794-9) Wang X., Wang Y., Zhu X., et al. Image encryption scheme based on chaos and DNA plane operations. Multimedia Tools and Applications, 2019.  
- [hindawi.com](https://www.hindawi.com/journals/ddns/2020/5982743/) Liu J., Wang Y., Han Q., et al. An Image Encryption Algorithm Based on Multichaotic System and DNA Coding. Discrete Dynamics in Nature and Society, 2020.  
- [sciencedirect.com](https://www.sciencedirect.com/science/article/pii/S0143816617300430) Chai X., Chen Y., Broyde L. A novel chaos‑based image encryption algorithm using DNA sequence operations. Optics and Lasers in Engineering, 2017.  
- [doi.org](https://doi.org/10.1142/S0218127406015970) Alvarez G., Li S. Some Basic Cryptographic Requirements for Chaos‑Based Cryptosystem. Int. J. Bifurcation and Chaos, 2006.  
- [ieeexplore.ieee.org](https://ieeexplore.ieee.org/document/5756453) Zhang X. Reversible data hiding in encrypted image. IEEE Signal Processing Letters, 2011.  
- [jeit.ac.cn (refs list)](https://www.jeit.ac.cn/cn/article/doi/10.11999/JEIT230203) JEIT 文章参考文献汇总（含多篇混沌图像加密相关论文，供交叉检索与索引）.  
- [xueshu.baidu.com](https://xueshu.baidu.com/usercenter/data/paperhelp?cmd=paper_forward&longsign=53151318ed8498b032068d1e6e998a23&title=%E5%9F%BA%E4%BA%8E%E5%85%B1%E4%BA%AB%E7%9F%A9%E9%98%B5%E5%92%8C%E6%B7%B7%E6%B2%8C%E7%9A%84%E5%9B%BE%E5%83%8F%E5%88%86%E5%AD%98%E7%AE%97%E6%B3%95) 田小平等. 基于共享矩阵和混沌的图像分存算法（检索条目，含原始期刊索引）。  

（注：以上参考文献包含用户提供的搜索结果页面与若干同行评审期刊文章 DOI 链接，便于读者检索原文与核验数值。文中对各论文实验指标的具体数值均来源于原文或期刊页面所示结果；对于未给出精确数值的工作，描述限定为作者在文中所报的评价指标类别与结论方向。）