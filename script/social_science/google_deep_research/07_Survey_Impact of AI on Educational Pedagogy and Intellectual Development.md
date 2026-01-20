人工智能对教育教学法与智力发展的深层影响：2022–2025年学术综述
引言
自2022年11月生成式人工智能（Generative AI, GenAI）随ChatGPT的发布进入公众视野以来，教育领域经历了一场前所未有的范式重构。这场变革不仅在于工具的更迭，更在于其对底层教学法（Pedagogy）与学习者智力发展（Intellectual Development）的深刻渗透。从2022年到2025年，全球教育系统从最初的“防御性排斥”逐步转向“战略性整合”，研究重点也从简单的效率提升扩展到了对认知结构、高阶思维以及知识所有权的深度剖析 。   

在当代教育语境下，人工智能不再被视为单纯的信息检索手段，而是演变为一种“认知协同者”。根据联合国教科文组织（UNESCO）在2024年发布的建议，AI的整合必须以人为中心，旨在增强人类的决策能力而非取代之 。然而，2023至2025年间的实证研究揭示了一个复杂的悖论：AI在显著提升短期任务产出的同时，可能对长期的技能习得和深层智力发育产生侵蚀作用 。本报告系统梳理了过去三年间在教育技术、认知科学及高等教育研究领域的代表性成果，旨在为学术界和政策制定者提供一份严谨的决策参考。   

方法分类与代表作
2022至2025年间的研究工作可归纳为四大核心方法论类别：基于提示工程的教学脚手架模型、检索增强生成（RAG）驱动的知识系统、多模态自适应交互系统，以及基于人机协作框架的混合教学法。

1. 基于提示工程的教学脚手架模型
此类研究侧重于通过特定的指令设计（Prompt Engineering），将通用大模型转化为具备教育学逻辑的虚拟导师。其核心在于通过“引导”而非“告知”来维持学习者的认知参与度。

代表作一：Bastani et al. (2024) 《Generative AI without guardrails can harm learning: Evidence from high school mathematics》  该研究针对高中数学教育中AI的“护栏”效应展开了大规模随机对照试验（RCT）。研究者对比了标准GPT-4接口（GPT Base）与经过教学提示调优、严禁直接给出答案的“GPT导师”（GPT Tutor）。实验发现，虽然两组学生在练习阶段的表现均优于控制组（分别提升48%和127%），但在随后移除AI辅助的独立闭卷考试中，GPT Base组的得分比控制组低17%，而GPT Tutor组则成功消除了这种负面效应。这一结论证实了无限制的AI访问会诱发“认知走捷径”行为，而精心设计的教学提示能起到关键的智力保护作用 。   

代表作二：Gong et al. (2025) 《Dialogic feedback from GenAI for critical thinking development》  本研究探讨了如何利用GenAI生成的对话式反馈来培养计算机编程学生的批判性思维。研究方法涉及设计一种迭代式的反馈模型，要求AI在指出代码错误的同时，通过追问引导学生自我发现逻辑漏洞。关键实验结论显示，接受对话式反馈的学生在逻辑分解任务中的表现显著优于接受直接修正建议的对照组。该工作强调了AI作为苏格拉底式导师在促进高阶认知过程中的潜力 。   

代表作三：Chu et al. (2025) 《GenAI as a creative scaffolding tool for poetic comprehension》  研究者探讨了将GenAI作为创意脚手架，辅助学生理解抽象诗歌的教学路径。通过让学生输入对诗歌的文字描述并由AI生成视觉图像，该方法试图通过跨模态表征加深学生的语义理解。实验表明，这种视觉脚手架显著提升了学生对诗歌意象的记忆保留率和情感共鸣深度。研究指出，AI在将抽象概念具象化方面的能力是传统教学法的重要补充 。   

2. 检索增强生成（RAG）驱动的知识系统
为了克服大模型在教育应用中的“幻觉”和事实错误，RAG技术成为2024-2025年间构建专业教育系统的核心方法。

代表作一：Oldensand (2024) 《Developing a RAG System for Automatic Question Generation》  本研究针对坦桑尼亚教育部门的需求，开发了一套基于RAG的自动化试题生成系统。该方法通过将LLM接入官方教学大纲数据库，确保生成的测评题目严密遵循教育标准，解决了通用模型经常产生的超纲或事实错误。实验结论显示，RAG系统生成的题目在知识覆盖准确度上达到了92%，显著降低了教师的备课负担，并提高了评估的科学性 。   

代表作二：Klesel & Wittmann (2025) 《Retrieval-Augmented Generation for specialized business education》  该文深入探讨了RAG架构在企业管理与信息系统教育中的应用，旨在解决模型无法获取最新商业政策的问题。研究方法是构建一个非参数化的知识库，将最新的组织数据与预训练参数存储相结合。实验证明，RAG系统在回答知识密集型任务时的准确率提升了约40%，且能够提供可追溯的文档链接。这不仅增强了学生对AI输出的信任，也培养了其在复杂信息环境中的信息验证习惯 。   

代表作三：RAG-based Chatbot for Orthopedic Education (2025)  该研究评估了一个基于RAG的德语骨科医学教育聊天机器人。核心方法是利用RAGAS评价量表，从答案相关性（Answer Relevancy）、上下文精确度（Context Precision）和忠实度（Faithfulness）三个维度进行评估。关键实验结论显示，RAG显著降低了医学领域的“幻觉”率，其上下文精确度均值达到0.891，能够为医学生提供高度精准且基于证据的学习支持。   

3. 多模态交互与具身学习系统
多模态大模型（MLLM）的崛起使得AI能够处理图像、音频和视频，从而支持更具感知力的互动学习体验。

代表作一：Teng et al. (2025) 《Intelligent TA powered by MLLM in computer vision courses》  该研究探讨了GPT-4V等模型作为视觉辅助助教在计算机视觉课程中的表现。方法是允许学生通过上传手绘逻辑图或代码截图，与AI进行视觉层面的深度对话。实验结果表明，这种多模态互动不仅提高了学业成绩，更重要的是帮助学生发展了“主动提问”的高阶思维。学生在AI的视觉提示下，表现出更强的空间推理能力和系统架构理解力 。   

代表作二：Wu et al. (2025) 《AI chatbots in EFL think-pair-share activities》  研究者将多模态AI集成到英语作为外籍语（EFL）的“思考-配对-分享”协作模型中。核心方法是利用AI实时生成的语音和视觉反馈，辅助学生进行口语练习和协作讨论。关键结论显示，AI的介入显著降低了学生的口语焦虑感（Speaking Anxiety），并增加了课堂参与的愉悦感。该研究证明了AI在模拟真实语境和降低情感过滤方面的卓越功效 。   

代表作三：MLLM and visually impaired learners (2025)  这项针对385名视障大学生的定量研究，调查了多模态大模型对教育公平的影响。研究采用偏最小二乘结构方程模型（PLS-SEM）测试假设。结果证实，对LLM的信任能显著预测其使用频率，进而通过提升生活质量（QoL）间接促进学业成功。这一结论凸显了AI在无障碍教育中的潜力，即通过文本描述图像等功能实现智力发展的公平性 。   

4. 协作式人机一体化教学法
这一类别关注如何从制度和流程上重新定义师生与AI的关系，强调“人机共生”而非“替代”。

代表作一：Modular Mastery Threshold Pedagogy (MMTP) (2025)  该研究提出了一种名为“模块化精通阈值教学法”的新框架，并应用于Python编程课程。核心方法是将课程分为七个渐进式模块，学生必须展示100%的精通度（通过AI辅助的代码实现与人工审计结合）才能晋级。实验发现，这种结合了GenAI集成开发的框架显著增强了学生的成长心态（Growth Mindset），并实现了比传统教学更深层次的学习成果。   

代表作二：Guided vs Unguided LLM use (2025)  该实验性研究比较了在学术写作中“有引导的、基于教育学原则的AI使用”与“无引导使用”的效果。方法是将学生分为对照组、无引导组和结构化引导组（接受AI素养培训）。实验结果显示，结构化引导组在写作质量和学业参与度上得分最高，且效应量达到中到大规模。这证明了教学介入在防止AI滥用和提升认知价值方面的决定性作用 。   

代表作三：AT-MCSCL Framework (2025)  基于活动理论与移动计算机支持的协作学习框架，该元分析综合了57项研究。研究发现，GenAI在大学环境中的效应量高达 g=0.804，且对大一新生和语言学习者的支持效果最明显。关键结论指出，当AI被嵌入到明确的社会互动规则中时，其对智力发展的推动力最强 。   

实验评价与认知影响总结
综合2022至2025年间的大量实证数据及元分析结果，AI对教育质量和智力发育的影响呈现出高度的语境依赖性。

1. 学业成就的非均衡分布
多项元分析（Meta-analysis）提供了关于AI干预效果的量化视图。如下表所示，AI在不同学科和学段的效应量存在显著差异：

研究来源	目标群体/学科	样本量 (N)	整体效应量 (g / Hedges 
′
 g)	关键变量影响
Zhu et al. (2025) 

全学段/智力成果	5232	0.372 (Intellectual)	
长期干预（8-16周）优于短期；小学阶段效应最高 

Chen & Cheung (2025) 

高等教育	57项研究	0.804 (Academic Success)	
语言类学科受益最大 (g=2.331) 

Zhu (2025) 

高阶思维 (HOT)	22项研究	Moderate positive	
问题解决能力 > 批判性思维 > 创造力 

Tlili et al. (2025) 

数学教育	11项研究	0.67 (STEM specific)	
中学阶段效应量处于中等水平 

  
共性结论表明，AI对语言习得和初级知识理解的提升最为显著，但在深层创造力和复杂数学推理方面的贡献仍有限。尤其是针对大学生的研究显示，AI往往在辅助写作润色和资料总结方面表现优异，但在需要跨学科逻辑建构的任务中效果减弱 。   

2. 认知卸载与元认知退化趋势
实证研究界对“认知卸载”（Cognitive Offloading）及其带来的“智力萎缩”风险表达了深切忧虑。2024年的一系列实验揭示了所谓的“AI蒸发效应”（AI Vaporization of Learning） ：   

浅层理解悖论：Lehmann等人（2025）指出，在编程和法律检索任务中，学生虽然能以更快的速度覆盖更多主题，但这种效率是以牺牲理解深度为代价的。依赖AI生成答案的学生在后续的原理测试中表现出明显的逻辑脱节 。   

记忆编码受损：研究发现，使用AI辅助笔记或论文撰写的学生，对其作品内容的长期保留率显著低于纯人工组。这是因为AI消除了知识习得过程中必要的“理想难度”（Desirable Difficulties），使得大脑未经深度加工便产出了结果 。   

元认知惰性：Lee等（2025）的调研显示，用户对AI的信心与其执行批判性思维的努力程度呈负相关（r=−0.3 左右）。当用户认为AI极度可靠时，会减少事实核查和逻辑审查，这种“元认知懒惰”在17-25岁的青年群体中表现最为突出 。   

3. 社交情感与自我效能感的重塑
AI在智力发展之外的情感维度表现出积极影响。2024-2025年的调查显示，超过86%的大学生在使用AI后报告了学习效率和主动性的提升 。   

焦虑缓解：AI提供的非评判性环境（Non-judgmental Environment）对心理压力较大的学习者具有显著的安抚作用，尤其在口语训练和基础问题咨询中，学生表现出更高的自我效能感 。   

数字鸿沟的新形态：HEPI (2025)的报告指出，AI正在制造新的数字不平等。男性学生、STEM专业学生以及高社会经济地位（SES）的学生在使用AI的频率和策略性上显著领先。这种“熟练度鸿沟”可能在未来转化为更深层次的社会智力分层 。   

趋势与挑战
站在2025年的节点展望，教育人工智能正从“生成热潮”进入“理性重构期”。

1. 从“产出优先”转向“过程导向”的评价范式
随着AI生成内容的普及，传统的以最终作业为考核指标的模式将失效。研究趋势表明，教育界正转向“过程导向评价”（Process-oriented Assessment），重点评估学生如何引导AI、如何验证AI输出以及如何通过AI反馈进行迭代修改。2025年后的主流教学法将把“人机协作足迹”作为智力评价的核心组成部分 。   

2. 教育专属RAG与私有化认知环境
针对隐私和 Hallucination（幻觉）的挑战，未来研究将集中在构建高度闭环的教育RAG系统。这意味着每个学科、甚至每门课程都将拥有经过专家校验的私有知识库。这不仅能保证学术严谨性，还能解决AI训练数据中潜在的偏见问题，为学生提供一个既智能又受控的“认知保护区” 。   

3. 多模态具身认知与AI教师的进化
随着MLLM与机器人技术的结合，AI将从屏幕内的文本框走向具身交互。未来的AI导师将能够通过摄像头观察学生的实验操作或解题笔迹，通过细微的情绪识别捕捉学生的挫败感或认知盲点，并进行实时干预。这种从“离线思考”到“在线观察”的跨越，将彻底改变自适应学习的精度 。   

4. 认知屏蔽与“智力主权”的博弈
最大的伦理与学术挑战在于如何界定“智力主权”。随着AI能够代写论文、代做实验设计，教育界将面临一场关于“人类思维核心领地”的保卫战。这需要开发能够增强而非屏蔽人类思维的工具，例如限制AI输出完整答案，强制学生在获取AI帮助前进行先验思考（Pre-thought）。如何在享受效率红利的同时避免人类智力的系统性退化，是2025年后全球教育界共同面临的终极考题 。   

结论
2022至2025年的学术实践证明，人工智能对教育的影响远超工具层面，它已经深刻改变了人类习得知识的心理机制和认知路径。一方面，AI通过个性化脚手架、多模态支持和RAG系统，为解决教育资源不均和提升学习效率提供了史无前例的机会；另一方面，过度依赖和无护栏的集成正导致认知卸载、元认知退化以及长久智力发展的不确定性。

本报告认为，AI时代的智力发展不应是人机竞争，而应是人类在高阶思维、批判性验证和伦理判断力上的持续进化。未来的教学法必须有意识地保留“必要的难度”，利用AI的效率红利腾出空间，引导学生进入更深层次的探究性学习。唯有建立起严密的监管框架、科学的评价体系以及以人为本的技术护栏，我们才能确保教育人工智能在重塑教学法的同时，真正赋能而非削弱人类的智力主权。


tandfonline.com
Full article: Mastering knowledge: the impact of generative AI on student learning outcomes
在新窗口中打开

arxiv.org
From Superficial Outputs to Superficial Learning: Risks of Large Language Models in Education - arXiv
在新窗口中打开

pmc.ncbi.nlm.nih.gov
Developing an AI framework for learning in higher education: a humanities perspective from English Literature - PMC - PubMed Central
在新窗口中打开

pnas.org
Generative AI without guardrails can harm learning: Evidence from high school mathematics | PNAS
在新窗口中打开

microsoft.com
Learning outcomes with GenAI in the classroom - Microsoft
在新窗口中打开

researchgate.net
Generative AI without guardrails can harm learning: Evidence from high school mathematics
在新窗口中打开

hamsabastani.github.io
Generative AI Without Guardrails Can Harm Learning: Evidence from High School Mathematics - Hamsa Sridhar Bastani
在新窗口中打开

assets-eu.researchsquare.com
assets-eu.researchsquare.com
在新窗口中打开

mdpi.com
Retrieval-Augmented Generation (RAG) Chatbots for Education: A ...
在新窗口中打开

researchgate.net
(PDF) Retrieval-Augmented Generation (RAG) - ResearchGate
在新窗口中打开

ai.jmir.org
Development and Evaluation of a Retrieval-Augmented Generation Chatbot for Orthopedic and Trauma Surgery Patient Education: Mixed-Methods Study - JMIR AI
在新窗口中打开

pmc.ncbi.nlm.nih.gov
Measuring the Impact of Large Language Models on Academic Success and Quality of Life Among Students with Visual Disability: An Assistive Technology Perspective - PMC - PubMed Central
在新窗口中打开

iacis.org
a new way to teach programming using generative ai and modular mastery threshold pedagogy (mmtp)
在新窗口中打开

frontiersin.org
Optimizing academic engagement and mental health through AI: an experimental study on LLM integration in higher education - Frontiers
在新窗口中打开

scribd.com
1-s2.0-S1747938X25000740-main | PDF | Meta Analysis | Metacognition - Scribd
在新窗口中打开

researchgate.net
Exploring the impact of generative artificial intelligence on students ...
在新窗口中打开

pmc.ncbi.nlm.nih.gov
Does Generative Artificial Intelligence Improve Students' Higher-Order Thinking? A Meta-Analysis Based on 29 Experiments and Quasi-Experiments - PMC - PubMed Central
在新窗口中打开

researchgate.net
(PDF) The Impact of Generative AI on Student Learning Achievement in Secondary STEM Education: A Meta-Analysis - ResearchGate
在新窗口中打开

frontiersin.org
The impact of generative AI on academic reading and writing: a synthesis of recent evidence (2023–2025) - Frontiers
在新窗口中打开

edutopia.org
How AI Vaporizes Long-Term Learning - Edutopia
在新窗口中打开

arxiv.org
Understanding, Protecting, and Augmenting Human Cognition with Generative AI: A Synthesis of the CHI 2025 Tools for Thought Workshop - arXiv
在新窗口中打开

nsta.org
To Think or Not to Think: The Impact of AI on Critical-Thinking Skills | NSTA
在新窗口中打开

microsoft.com
The Impact of Generative AI on Critical Thinking: Self-Reported Reductions in Cognitive Effort and Confidence Effects From a Survey of Knowledge Workers - Microsoft
在新窗口中打开

pmc.ncbi.nlm.nih.gov
Educational impacts of generative artificial intelligence on learning ...
在新窗口中打开

sites.campbell.edu
AI in Higher Education: A Meta Summary of Recent Surveys of Students and Faculty
在新窗口中打开

hepi.ac.uk
Student Generative AI Survey 2025 - HEPI - Higher Education Policy Institute
在新窗口中打开

frontierspartnerships.org
Generative AI in Higher Education: Balancing Innovation and Integrity - Frontiers Publishing Partnerships
在新窗口中打开

mdpi.com
Generative AI and Academic Integrity in Higher Education: A Systematic Review and Research Agenda - MDPI
在新窗口中打开

pmc.ncbi.nlm.nih.gov
Enhancing medical AI with retrieval-augmented generation: A mini narrative review - NIH
在新窗口中打开

academic.oup.com
survey on multimodal large language models | National Science Review - Oxford Academic
在新窗口中打开

mdpi.com
The Impact of Artificial Intelligence (AI) on Students' Academic Development - MDPI