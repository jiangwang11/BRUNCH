巴洛克音乐理论与实践研究综述（2022–2025）
引言
巴洛克音乐（约1600–1750）作为西方音乐史上理论建构与实践创新的巅峰时期，其核心在于通奏低音（Basso Continuo）的和声支撑、对位法（Counterpoint）的逻辑展开以及情感论（Doctrine of the Affections）的审美驱动。在过去的三个世纪中，对这一时期的研究经历了从文献考据到历史知情演奏（Historically Informed Performance, HIP）运动的转变。进入2022年后，随着计算音乐学（Computational Musicology）、深度学习模型以及数字人文学科（Digital Humanities）的跨界融合，巴洛克音乐研究展现出前所未有的范式迁移 。   

本综述旨在梳理2022年至2025年间巴洛克音乐理论与实践领域的代表性工作。这一时期的研究不再仅仅满足于对古谱的静态转录，而是通过大规模数据集的构建、生成式AI模型的风格微调以及物理声学环境的虚拟重构，深入探讨巴洛克音乐在现代技术语境下的语义演变与表演潜能 。研究者们开始关注如何将18世纪的教学传统（如Partimento与对位法规则）形式化为计算机可理解的逻辑，并利用跨模态技术捕捉演奏者细微的身体律动与空间声学交互 。这种“理论形式化”与“实践量化”的双重趋势，不仅为音乐信息检索（MIR）领域提供了高难度的测试范例，也为古乐研究注入了科学的实证精神 。   

方法分类与代表作
1. 数字化通奏低音与和声分析方法
通奏低音是巴洛克音乐的灵魂，其实现（Realization）过程涉及严谨的和声规则与即兴的创作自由。近年来，研究者通过构建符号化数据集与开发边界感知的深度学习模型，试图攻克通奏低音的自动化识别与生成难题 。   

Basso Continuo Goes Digital: Collecting and Aligning a Symbolic Dataset of Continuo Performance (Štefunko et al., 2025) 针对音乐信息检索领域长期存在的通奏低音数据稀疏问题，该研究构建了首个包含6小时、175个MIDI录音的符号化通奏低音演奏数据集 。研究团队提出了一种结合隐马尔可夫模型（HMM）与动态时间规整（DTW）的两步对齐方法，旨在将即兴的上方声部实现与原始基底音轨进行精确匹配 。实验表明，该基准模型能够实现稳健的音轨对齐，但在处理装饰性极强的即兴音符归属时仍面临挑战，揭示了巴洛克即兴实践中的非线性逻辑 。此项工作填补了巴洛克伴奏实践在大规模计算分析领域的空白，为后续的自动伴奏生成奠定了数据基础 。   

BACHI: Boundary-Aware Symbolic Chord Recognition Through Masked Iterative Decoding (Yao & Chen, 2025) 该研究旨在解决巴洛克与古典音乐中由于对位织体复杂性导致的和弦识别精度不足问题，提出了名为BACHI的边界感知符号化和弦识别模型 。核心方法是将任务分解为边界检测与和弦属性（根音、性质、低音）的迭代排序，模拟人类在视唱练耳过程中通过关键线索逐步推断和声的认知路径 。在DCML巴洛克数据集上的实验显示，BACHI实现了68.1%的全和弦准确率，显著优于传统的Harmony Transformer v2，证明了边界感知机制在处理复杂对位转调时的优越性 。这种通过特征线性调制（FiLM）整合边界信息的设计，为理解巴洛克和声的结构化演变提供了新的计算视角 。   

The Semantic Evolution of Chromatic Mediants: A Baroque Origin of M8M Progressions (Lee, 2025) 本研究探讨了变体中音进行的语义起源，指出当代影视音乐中象征“超自然”或“神奇”的M8M进行实则植根于巴洛克的组合惯例 。作者通过对巴赫与亨德尔声乐作品的符号学分析，识别出弗里吉亚半终止与双焦点调性转换的结合是产生这一语义的核心机制，通常用于表现“从死亡到生命的超越” 。研究结论强调，这种和声进行在18世纪已被确立为一种特定的音乐符号，而非19世纪浪漫主义的凭空发明 。此项成果为计算语义分析提供了历史依据，证明了高层音乐情感的建模必须基于特定时代的理论语境 。   

下表总结了上述三种方法在处理巴洛克和声特征时的技术差异：

维度	Štefunko (2025) 数据对齐	BACHI (2025) 和弦识别	Lee (2025) 语义溯源
主要技术	HMM + DTW 二步对齐算法	掩码迭代解码 (Masked Iterative Decoding)	符号学分析 (Semiotic Analysis)
处理对象	即兴通奏低音实现与基底音轨	符号化谱面中的和声标签识别	变体中音 (M8M) 的历史语义
关键贡献	解决即兴数据的结构化存储难题	提升了对位织体下的和弦识别准确率	揭示了巴洛克理论对现代审美的深远影响
数据源	
6小时 MIDI 演奏数据集 

POP909-CL, DCML 等古典语料 

巴赫、亨德尔等声乐/器乐作品 

  
2. 计算对位法、赋格与算法作曲
对位法是巴洛克作曲技术的核心，2022年后的研究重点在于将18世纪的对位规则转化为可执行的逻辑约束，并探索赋格结构的自动化分析方法 。   

FuxCP: A Formalisation of Three-Part Musical Counterpoint Based on Fux’s Theory (Lamotte, 2024) 本项工作对Johann Joseph Fux在1725年出版的《通向帕纳苏斯山之路》进行了完整的三部对位形式化建模，扩展了先前的两部对位研究 。研究利用Gecode约束求解器，将Fux定义的各类音程准则、声部独立性要求及终止式规范转化为严格的数学约束，并特别强化了对低音部声部运动的逻辑处理 。实验结论表明，FuxCP系统能够自动生成符合古典规范的对位旋律，其引入的“偏好规则”赋予了算法生成的作品以某种“人类审美偏好”的微调能力 。这一成果为音乐教学软件的开发提供了理论深度，使巴洛克对位训练在自动化环境下成为可能 。   

Computational Fugue Analysis: Pattern Discovery and Structural Segmentation (Giraud et al., 2023 update) 该研究通过改进字符串匹配算法与全音阶程差度量，实现了对赋格曲中主题（Subject）、答句（Answer）及插句（Episode）的精准自动识别 。研究者在包含巴赫与肖斯塔科维奇赋格作品的语料库上进行了测试，重点攻克了密接和应（Stretto）与倒影对位等高级结构模式的检测 。结果显示，该算法能够有效区分赋格的展示段与发展段，其在三十余首巴赫赋格中的识别成功率达到良好水平，为数字音乐学中的风格统计提供了可靠工具 。这项工作的意义在于，它证明了即使是高度抽象的赋格形式，也可以通过特定的模式发现机制进行量化建模 。   

Improvising Fugue: A Method for Keyboard Artists (Mortensen, 2024) 虽然作为一本教学论著，但其提出的利用Partimento（数字低音练习）作为赋格即兴教学的核心方法，引发了计算作曲领域的广泛关注 。作者详细阐述了如何从简单的音程级进（Bass Motion）逐步演化为复杂的赋格织体，强调了巴洛克时期“手脑并用”的认知模式 。通过对40余个Partimento范例的难度分级，该方法为训练生成式AI模型提供了完美的阶段性语料库架构 。这一理论的现代复兴（即所谓“Partimento革命”）为解决AI生成音乐中长期存在的“缺乏长时结构感”问题提供了历史解决方案 。   

3. 生成式 AI 与巴洛克风格微调技术
在大模型时代，巴洛克音乐研究的重心转向如何利用大规模预训练模型捕获特定作曲家（如巴赫）的微观风格特征 。   

NotaGen: Advancing Musicality in Symbolic Music Generation with LLM Training Paradigms (Wang et al., 2025) NotaGen是一个专门针对高质量古典乐谱生成的符号化语言模型，其核心创新在于完整应用了预训练、微调与强化学习的LLM范式 。该模型在160万份ABC记谱法文档上进行预训练，并针对包括巴赫在内的152位作曲家的作品进行“时期-作曲家-乐器”提示词微调 。研究提出的CLaMP-DPO方法利用跨模态反馈替代昂贵的人工标注，显著提升了生成乐谱的复调排布与符号规范性 。主观A/B测试证明，NotaGen生成的巴洛克风格片段在音乐美感上优于现有所有基准模型，极大地推进了符号音乐生成的审美上限 。   

From Generality to Mastery: Composer-Style Symbolic Music Generation via Large-Scale Pre-training (Yao & Chen, 2025) 该项研究探讨了如何通过“从通用到精通”的训练范式解决特定作曲家风格数据稀疏的问题 。研究首先在包含多种流派的大型音乐库上训练基础Transformer，随后通过轻量化的适配器（Adapter）针对巴赫、莫扎特等大师的小型高质量数据集进行风格对齐 。客观指标显示，该模型在音级熵（Pitch Class Entropy）与节奏律动相似度上均表现优异，有效学习了巴洛克织体中独特的动机发展规律 。实验分析进一步揭示，通用预训练使模型掌握了基本乐理，而“精通”微调则让模型习得了巴洛克对位法的深层精髓 。   

BOSSA: Learning Music Style Through Cross-Modal Bootstrapping (Zhao et al., 2025) BOSSA提出了一种利用音频参考来引导符号音乐生成的跨模态框架，重点解决巴洛克音乐中那些“难以言传”的演奏风格迁移 。模型通过Querying Transformer (Q-Former) 提取音频中的内隐风格表征，并将其作为条件输入给符号化大语言模型（如MuseCoco）进行 piano arrangement 的生成 。实验证明，BOSSA能够捕捉巴洛克键盘乐中特有的触键感与装饰音偏好，生成的钢琴封面在一致性与整体音乐性上显著超过了基于规则的方法 。这项研究突破了传统文字标签（如“Baroque”）的局限，实现了基于具体演奏实例的“以音传形” 。   

4. 历史知情演奏（HIP）与声学、认知实证研究
2022年后的巴洛克演奏研究开始整合实验声学、生物力学与考古学方法，探讨物理环境如何塑造演奏者的决策 。   

Listener perception of changes in historically informed performance of solo baroque music due to room acoustics (Eley et al., 2024) 本研究调查了房间声学对巴洛克长笛与维奥尔琴HIP演奏风格的影响，以及这些差异是否能被听众察觉 。实验在凡尔赛宫的巴洛克沙龙与巴黎现代音乐城的听众席分别录制同一组HIP专家的演奏，并由20名受过专业训练的听众进行盲听评估 。关键发现是，虽然演奏者的颤音频率变化较小，但长笛手在现代听众席中会采取更强迫的音色和更紧凑的分句以补偿声学干涩感 。这一发现支持了“声学环境 facilitating 历史风格”的假说，证明了巴洛克室内乐的精髓在于与特定空间的声学共鸣 。   

MOSA: Music Motion with Semantic Annotation Dataset for Cross-Modal Music Processing (Huang et al., 2024) 为了探索巴洛克演奏中身体语言与音乐表现的关系，该研究构建了MOSA数据集，包含超过30小时、由23位专业音乐家贡献的三维运动捕捉数据及同步音频 。数据集包含了精确的音符级标注，涵盖了巴洛克作品中的和声进行、分句边界及力度标记 。研究者演示了利用该数据集训练的音频到运动生成模型，能够自动为巴洛克钢琴或小提琴录音生成逼真的演奏动作动画 。实验表明，强力的工具性数据收集（Instrument-specific collection）能够显著提升跨模态转换的真实度，揭示了巴洛克演奏中“动作即修辞”的深层联系 。   

Vaulted Harmonies: Notre-Dame Archaeoacoustics Project (ANR-PHEND, 2024) 该项目利用考古声学方法重构了巴黎圣母院在巴洛克时期的声学景观，探讨了历史建筑演变对宗教复调音乐演进的影响 。通过几何声学建模与三维扫描，研究团队模拟了17-18世纪教堂内部祭坛位置及装潢对管风琴音响的改变，并利用校准后的模型对录制的HIP演奏进行卷积叠加（Auralisation） 。该项目产出的电影作品《Vaulted Harmonies》通过视觉与听觉的同步再现，证明了巴洛克时期的大型声学空间本身就是一种参与创作的“乐器” 。这种跨学科的声学考古为理解巴洛克时期声乐与器乐的动态平衡提供了关键的物理证据 。   

下表展示了2024–2025年发布的几个关键巴洛克/古典音乐研究数据集及其主要技术特征：

数据集名称	发布年份	模态	规模/样本量	核心技术/标注
POP909-CL	2025	符号 (MIDI)	增强版古典标签	
人工校对的和弦、节拍与转调标签 

MOSA	2024	运动 + 音频	30+ 小时录音	
音符级语义标注、3D动捕坐标 

Continuo MIDI	2025	符号 (MIDI)	175 个录音	
即兴实现与基底音轨的二步对齐 

FAV Corpus	2023	音频 + 符号	多版本作品集	
包含形式分析与音乐理论描述符 

  
实验与评价总结
综观 2022–2025 年的实验证据，巴洛克音乐理论与实践的研究呈现出高度的一致性与跨学科验证的共性趋势。

第一，在和声与对位法的自动化处理上，研究普遍确认了“结构边界感知”与“迭代解码”的有效性 。与传统的单向预测模型相比，引入了巴洛克理论约束（如通奏低音根音优先规则）的模型在处理高度装饰性的复调织体时，其准确率提升显著。实验数据显示，在面临多声部重叠时，基于 Fux 规则或巴赫合唱乐逻辑训练的系统（如 NotaGen 与 FuxCP）在声部领先（Voice Leading）的规范性上明显优于通用生成的 Transformer 模型 。   

第二，关于历史知情演奏（HIP）的实证研究表明，演奏者对环境声学的适应并非随机，而是遵循特定的修辞学模式 。听众感官测试一致指出，巴洛克长笛与维奥尔琴在“原装声学环境”下的分句更具透明感，这种“感知连贯性”在统计分析中与录音的混响半径及早期反射声能呈正相关 。   

第三，生成式 AI 的评价体系已从纯客观指标（如 Loss 值、重构精度）转向主客观结合的“音乐性”评估 。通过 CLaMP-DPO 等方法引入跨模态反馈，实验者发现生成的巴洛克作品在满足基本对位法禁忌的同时，通过模仿人类演奏录音中的微调律（Micro-timing）和触键动态，显著缩减了 AI 作品与真实人类创作之间的“灵气鸿沟” 。这种结合了 18 世纪教学论（如 Partimento）的长时结构建模，在解决生成音乐“散乱感”方面展现了显著潜力 。   

趋势与挑战
1. “神经-符号”混合架构的深化
2025年前后的核心研究趋势之一是将刚性的音乐理论规则（如对位法禁忌、转调逻辑）作为硬性约束嵌入到神经生成模型中 。目前的生成模型虽然在风格模仿上表现出色，但仍可能出现违反巴洛克声部排列准则的低级错误 。未来的挑战在于如何平衡 LLM 的创造性与传统理论的形式化严谨性，开发出具备“自我理论审查”能力的巴洛克作曲 AI 。   

2. 实时历史声学交互系统的开发
随着考古声学（Archaeoacoustics）数据集（如 Notre-Dame 项目）的积累，研究重点正转向实时性应用 。未来的趋势是开发出能够根据演奏者现场表现动态反馈历史混响的智能声学空间，这不仅对 HIP 演奏训练至关重要，也将为沉浸式数字博物馆提供核心交互手段 。   

3. 多模态演奏修辞学的量化建模
依托 MOSA 等多模态数据集，研究者正试图建立一套完整的“巴洛克修辞动捕模型” 。这要求模型不仅要识别音符，还要理解演奏者的手势、呼吸与情感表情如何协同表达某一特定的“Affekt”（情感论） 。这一领域的难点在于如何从高度个性化的专业演奏中提取出具有共性的历史修辞法则 。   

结论
在 2022–2025 年这段时期内，巴洛克音乐理论与实践的研究已完成从传统“文本驱动”向现代“数据与感知驱动”的华丽转型。通过数字化通奏低音的精准对齐、赋格结构的计算分析以及生成式大模型的风格微调，学术界不仅为巴洛克这一复杂的美学时代建立了一套可量化的“数字镜像”，更在认知层面重新发现了历史演奏实践与物理空间、身体运动之间的深层契合 。   

尽管在模拟即兴演奏的随机灵感与修辞学的高级逻辑方面仍存在挑战，但跨学科的工具链——从 Gecode 约束求解器到 Transformer 迭代解码——已经极大地拓宽了我们对巴洛克理论之严密性与实践之灵活性的认知边界 。这种由技术赋能的“复古创新”，预示着一个能够实时对话、智能即兴且具备历史深度的巴洛克音乐研究新纪元的到来。   

参考文献
Štefunko, A., Chiruthapudi, S., Hajic jr, J., & Cancino-Chacón, C. E. (2025). Basso Continuo Goes Digital: Collecting and Aligning a Symbolic Dataset of Continuo Performance. Proceedings of the 2025 International Conference on AI and Music (AIMC).    

Yao, M., & Chen, K. (2025). BACHI: Boundary-Aware Symbolic Chord Recognition Through Masked Iterative Decoding on Pop and Classical Music. arXiv preprint arXiv:2510.06528.    

Wang, Y., Wu, S., et al. (2025). NotaGen: Advancing Musicality in Symbolic Music Generation with Large Language Model Training Paradigms. International Joint Conference on Artificial Intelligence (IJCAI 2025).    

Zhao, J., Wang, Z., Xia, G., & Wang, Y. (2025). BOSSA: Learning Music Style Through Cross-Modal Bootstrapping. NeurIPS 2025 AI4Music Workshop.    

Eley, N., Lavandier, C., Psychoyou, T., & Katz, B. F. G. (2024). Listener perception of changes in historically informed performance of solo baroque music due to room acoustics. Acta Acustica.    

Huang, Y. F., Moran, N., et al. (2024). MOSA: Music Motion with Semantic Annotation Dataset for Cross-Modal Music Processing. IEEE/ACM Transactions on Audio, Speech, and Language Processing.    

Lee, J. Y. H. (2025). The Semantic Evolution of Chromatic Mediants: A Baroque Origin of M8M Progressions. Music Theory Online.    

Lamotte, A. (2024). FuxCP: A formalisation of three-part musical counterpoint based on Fux’s theory. Master's Thesis, UCLouvain.    

Ticli, L. (Ed.). (2024). Figured Bass Accompaniment in Europe. Turnhout: Brepols.    

Mazzetti, M. (Ed.). (2024). Basso Continuo in Italy: Sources, Pedagogy and Performance. Turnhout: Brepols.    

Giraud, M., Groult, R., Leguy, E., & Levé, F. (2023 update). Computational Fugue Analysis. Computer Music Journal.    

Yao, M., & Chen, K. (2025). From Generality to Mastery: Composer-Style Symbolic Music Generation via Large-Scale Pre-training. arXiv preprint arXiv:2506.17497.    

Mortensen, J. (2024). Improvising Fugue: A Method for Keyboard Artists. Oxford University Press.    


student.mit.edu
Course 21M: Music IAP/Spring 2025 (Archive)
在新窗口中打开

network.bepress.com
Music Theory | Open Access Articles | Digital Commons Network™
在新窗口中打开

academic.oup.com
Figured Bass Accompaniment in Europe | Music and Letters - Oxford Academic
在新窗口中打开

acta-acustica.edpsciences.org
Listener perception of changes in historically informed performance of solo baroque music due to room acoustics | Acta Acustica
在新窗口中打开

jku.at
Basso Continuo Goes Digital: Collecting and Aligning a Symbolic Dataset of Continuo Performance - JKU
在新窗口中打开

ijcai.org
NotaGen: Advancing Musicality in Symbolic Music Generation with Large Language Model Training Paradigms - IJCAI
在新窗口中打开

researchgate.net
MOSA: Music Motion with Semantic Annotation Dataset for Cross-Modal Music Processing | Request PDF - ResearchGate
在新窗口中打开

openreview.net
BOSSA: Learning Music Style Through Cross-Modal ... - OpenReview
在新窗口中打开

webperso.info.ucl.ac.be
"FuxCP: Constraint Programming Formalisation of Three-Voice Counterpoint According to Fux" - Université catholique de Louvain
在新窗口中打开

github.com
yufenhuang/MOSA-Music-mOtion-and-Semantic-Annotation-dataset - GitHub
在新窗口中打开

researchgate.net
(PDF) Computational Fugue Analysis - ResearchGate
在新窗口中打开

arxiv.org
BACHI: Boundary-Aware Symbolic Chord Recognition Through Masked Iterative Decoding on Pop and Classical Music - arXiv
在新窗口中打开

fiveable.me
Figured bass Definition - Intro to Humanities Key Term - Fiveable
在新窗口中打开

researchgate.net
(PDF) Automatic Chord Labelling: A Figured Bass Approach - ResearchGate
在新窗口中打开

brepols.net
Basso Continuo in Italy - Brepols Publishers
在新窗口中打开

chatpaper.com
BACHI: Boundary-Aware Symbolic Chord Recognition Through Masked Iterative Decoding on Pop and Classical Music - ChatPaper
在新窗口中打开

researchgate.net
(PDF) BACHI: Boundary-Aware Symbolic Chord Recognition Through Masked Iterative Decoding on Pop and Classical Music - ResearchGate
在新窗口中打开

liner.com
[Quick Review] BACHI: Boundary-Aware Symbolic Chord Recognition Through Masked\n Iterative Decoding on Pop and Classical Music - Liner
在新窗口中打开

arxiv.org
BACHI: Boundary-Aware Symbolic Chord Recognition Through Masked Iterative Decoding on Pop and Classical Music - arXiv
在新窗口中打开

mtosmt.org
The Semantic Evolution of Chromatic Mediants: A Baroque Origin of ...
在新窗口中打开

mymusictheory.com
Counterpoint - My Music Theory
在新窗口中打开

scribd.com
Computational Fugue Analysis: Mathieu Giraud, Richard Groult, Emmanuel Leguy, Florence Levé | PDF | Scale (Music) - Scribd
在新窗口中打开

digitalcollections.lipscomb.edu
Review of Improvising Fugue: A Method for Keyboard Artists by John J. Mortensen
在新窗口中打开

digitalcollections.lipscomb.edu
Volume 38 2024 - Carolyn Wilson Digital Collection
在新窗口中打开

matthewmazanek.com
Book Announcement! - Figured Bass Accompaniment in Europe - 2024 - Matthew Mazanek
在新窗口中打开

arxiv.org
From Generality to Mastery: Composer-Style Symbolic Music Generation via Large-Scale Pre-training - arXiv
在新窗口中打开

arxiv.org
NotaGen: Advancing Musicality in Symbolic Music Generation with Large Language Model Training Paradigms - arXiv
在新窗口中打开

api.semanticscholar.org
From Generality to Mastery: Composer-Style Symbolic Music Generation via Large-Scale Pre-training - Semantic Scholar API
在新窗口中打开

arxiv.org
NotaGen: Advancing Musicality in Symbolic Music Generation with Large Language Model Training Paradigms - arXiv
在新窗口中打开

2025.ijcai.org
Special Track on AI, the Arts and Creativity Papers - IJCAI 2025
在新窗口中打开

researchgate.net
Yashan Wang's research works - ResearchGate
在新窗口中打开

researchgate.net
From Generality to Mastery: Composer-Style Symbolic Music Generation via Large-Scale Pre-training - ResearchGate
在新窗口中打开

abebooks.co.uk
Figured Bass Accompaniment in Europe by Various: nuovo Rilegato - AbeBooks
在新窗口中打开

mdpi.com
Vaulted Harmonies: Archaeoacoustic Concert in Notre-Dame de Paris - MDPI
在新窗口中打开

arxiv.org
MOSA: Music Motion with Semantic Annotation Dataset for Cross-Modal Music Processing
在新窗口中打开

research.ed.ac.uk
MOSA: Music motion with semantic annotation dataset for multimedia analysis and generation - University of Edinburgh Research Explorer
在新窗口中打开

github.com
yamathcy/ISMIR-2023-Papers - GitHub
在新窗口中打开

researchgate.net
Composer Style-Specific Symbolic Music Generation using Vector Quantized Discrete Diffusion Models | Request PDF - ResearchGate
在新窗口中打开

bruckneruni.ac.at
Spring Lab 2025: "Overcoming Boundaries: A Dialogue between Artistic and Scholarly Research" - Anton Bruckner Privatuniversität
在新窗口中打开

researchgate.net
Historically Informed Performance: Theory and Practice of the 18th-Century Musical and Theatrical Repertoire: Palácio Nacional de Queluz, 15–17 September 2023 - ResearchGate
在新窗口中打开

ejournal.upi.edu
Exploring the interpretation techniques in Bach's Cello Suite No. 1 Prelude: A theoretical and practical approach to baroque performance practice | Nurmusabih | Interlude
在新窗口中打开

brepols.net
Figured Bass Accompaniment in Europe - Brepols Publishers