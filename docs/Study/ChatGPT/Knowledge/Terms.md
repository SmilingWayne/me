# 名词解释


- AI : Artificial Intelligence
- AIGC: Artificial Intelligence Generated Contents AI生成内容
- RLHF: Reinforcement Learning Human Factors?
- LLaMa: Large Language Model Meta AI：参数更少60 ~ 数百亿个参数实现更好的模型效果；一个Meta开源的模型。适合个人微调。
- fine-tuning：模型微调；
- LLM：Large Language Model;
- Vercel:?
- Wolfram: ?
- CI / CD?
- Codium
- Emacs:
> Emacs  ，最初名为 EMACS（“Editor MACroS”的首字母缩写词），是一个以可扩展性为特征的文本编辑器家族。 使用最广泛的变体  GNU Emacs 的手册将其描述为“可扩展、可定制、自文档化、实时显示编辑器”。 第一个 Emacs 的开发始于 20 世纪 70 年代中期，其直接后代 GNU Emacs 的工作仍在积极进行；最新版本为 28.2，于 2022 年 9 月发布。 Emacs 有超过 10,000 个内置命令，其用户界面允许用户将这些命令组合成宏以自动执行工作。 Emacs 的实现通常具有 Lisp 编程语言的方言，允许用户和开发人员为编辑器编写新的命令和应用程序。
- Neovim: 类似Emacs?
> Embedding？
> prompt: 提示词

> clickbait: 标题党

- AutoGPT
> AI 驱动的一个应用程序；LLM自动创建和处理各种工作、简化数据分析、报告等内容；甚至可以分解->把任务分解后逐个完成；
- ChatGPT: Generative Pre-trained Transformer
    - GPT 3.5 ～ GPT 4
- Claude: 类ChatGPT软件。需要🪜。
> 安装教程：[https://www.jianshu.com/p/b4a0211cae97](https://www.jianshu.com/p/b4a0211cae97)。支持Google mail和Apple ID登录。类似于加入群组的讨论方式。

- cloudflare: 
- LangChain:
- Azure: 


- 显卡：（Video card，Graphics card）全称显示接口卡，又称显示适配器，是计算机最基本配置、最重要的配件之一。就像电脑联网需要网卡，**主机里的数据要显示在屏幕上**就需要显卡。因此，显卡是电脑进行数模信号转换的设备，承担输出显示图形的任务。具体来说，显卡接在电脑主板上，它将电脑的数字信号转换成模拟信号让显示器显示出来。   
    - 原始的显卡一般都是集成在主板上，只完成最基本的信号输出工作，并不用来处理数据。随着显卡的迅速发展，就出现了GPU的概念，显卡也分为独立显卡和集成显卡。
- 计算机指令集：指令集，就是CPU中用来计算和控制计算机系统的一套指令的集合，而每一种新型的CPU在设计时就规定了一系列与其他硬件电路相配合的指令系统。而指令集的先进与否，也关系到CPU的性能发挥，它也是CPU性能体现的一个重要标志。
    - (x86 （主流电脑的）/ ARM )：CPU架构，如何操纵、控制CPU；X86更快；此外，ARM具有其与X86架构电脑不可对比的优势，该优势就是：功耗。Apple M2用的也是ARM架构；
    - 复杂指令集（CISC）和精简指令集（RISC）；
- CPU：**显卡**之前进行处理（运算、建模，显卡负责后面的显示等步骤）：CPU和显卡在一个程序的运行中各司其职，有先有后，互相影响。CPU的处理速度决定了显卡能否全速运行，显卡的处理速度也影响着最终呈现的效果。<u>GPU之于显卡，就相当于CPU之于电脑的关系。</u> 
    - 也就是说电脑运行的软件有的对CPU要求高，有的对CPU要求低。如果使用i5+GTX 1070的配置运行一款对CPU要求高而对显卡要求低的程序，那么CPU满载而显卡不满载，是很正常的；相反，如果运行一款对CPU要求低而对显卡要求高的程序，**CPU就不会满载而显卡则会满载**。
- GPU：GPU是显卡上的一块芯片，就像CPU是主板上的一块芯片。那么1999年之前显卡上就没有GPU吗？当然有，只不过那时候没有人给它命名，也没有引起人们足够的重视，发展比较慢。    自Nvidia提出GPU这个概念后，GPU就进入了快速发展时期。简单来说，其经过了以下几个阶段的发展：1）仅用于图形渲染，此功能是GPU的初衷，这一点从它的名字就可以看出：Graphic Processing Unit，图形处理单元；2）后来人们发现，GPU这么一个强大的器件只用于图形处理太浪费了，它应该用来做更多的工作，例如浮点运算。怎么做呢？直接把浮点运算交给GPU是做不到的，因为它只能用于图形处理（那个时候）。最容易想到的，是把浮点运算做一些处理，包装成图形渲染任务，然后交给GPU来做。这就是GPGPU（General Purpose GPU）的概念。不过这样做有一个缺点，就是你必须有一定的图形学知识，否则你不知道如何包装。
    - 在没有GPU之前，基本上所有的任务都是交给CPU来做的。有GPU之后，二者就进行了分工，CPU负责逻辑性强的事物处理和串行计算，GPU则专注于执行高度线程化的并行处理任务（大规模计算任务）。为什么这么分工？这是由二者的硬件构成决定的。
- CUDA: CUDA(Compute Unified Device Architecture)，通用并行计算架构，是一种运算平台。它包含CUDA指令集架构以及GPU内部的并行计算引擎。你只要使用一种类似于C语言的CUDA C语言，就可以开发CUDA程序，从而可以更加方便的利用GPU强大的计算能力，而不是像以前那样先将计算任务包装成图形渲染任务，再交由GPU处理。


- NVIDA ：创始人黄仁勋（美籍华人）；1999年，NVIDIA定义了GPU，这极大地推动了PC游戏市场的发展，重新定义了现代计算机图形技术，并彻底改变了并行计算。2017年6月，入选《麻省理工科技评论》“2017 年度全球50大最聪明公司”榜单。
    - NVIDIA公司专门打造面向计算机、消费电子和移动终端，能够改变整个行业的创新产品。这些产品家族正在改变视觉丰富和运算密集型应用例如视频游戏、电影产业、广播、工业设计、财政模型、空间探索以及医疗成像；
- AMD：**AMD半导体公司**专门为计算机、通信和消费电子行业设计和制造各种创新的微处理器（CPU、GPU、主板芯片组、电视卡芯片等），以及提供闪存和低功率处理器解决方案；






- RTX 3090 / RTX 4090 / 2080: NVIDA 的显卡的型号；里面集成了CUDA 和 GPU 等上述内容；RTX的意思就是实时光线追踪。
> P.S. 了解一下：电竞显卡。4k～6k RMB起步？
> 建模、光线追踪、求导运算

- Amphere 架构和图灵架构：新的GPU的架构
- NVIDIA A100是首款基于NVIDIA Ampere架构的GPU。作为一款通用型工作负载加速器，A100还被设计用于数据分析、科学计算和云图形。


- [HuggingFace](https://huggingface.co)。开源框架transformers.
    1. Datasets：数据集，以及数据集的下载地址
    2. Models：各个预训练模型
    3. course：免费的nlp课程，可惜都是英文的
    4. docs：文档

- Transformers：**利用注意力机制来提高模型训练速度的模型**(Attention is all you need)。
    - Attention: 注意力机制：
    一般transformer模型有三个部分组成：
    - 1.tokennizer;Tokenizer就是把输入的文本做切分，然后变成向量
    - 2.Model;Model负责根据输入的变量提取语义信息，输出logits；Model又可以分为三种模型，针对不同的NLP任务，需要选取不同的模型类型：
        - Encoder模型（如Bert，常用于句子分类、命名实体识别（以及更普遍的单词分类）和抽取式问答。），
        - Decoder模型（如GPT，GPT2，常用于文本生成），
        - sequence2sequence模型（如BART，常用于摘要，翻译，生成性问答等）
    - 3.Post processing。最后Post Processing根据模型输出的语义信息，执行具体的nlp任务，比如情感分析，文本自动打标签等；可见Model是其中的核心部分，

- [PyTorch](https://pytorch.org):
- 什么是QKV？
- Bert  / Transformers / 
- PyTorch  / Tensorflow 
- LLM : Large Language Model



  


## discord

- discord: （我的midjourney 和 网页版zlibrary都跳转到这个软件上了


- [https://zhuanlan.zhihu.com/p/540400071](https://zhuanlan.zhihu.com/p/540400071)
- Discord 是一款免费的通讯软件，让你可以与你的好友，游戏社群以及游戏开发者们进行语音，视频及文字聊天。这款软件有着数亿用户，使其成为了世界上最受欢迎的与线上的好友建立连接的方式之一。Discord 可以在几乎全部流行的平台与设备上使用，例如 Windows、macOS、Linux、iOS、iPadOS 和 Android，也可以通过网页浏览器运行。
- 可以建立自己相应的服务器
- 你也可以创建一个链接，让任何持有链接的人无需直接被你邀请，而是通过该链接加入服务器。当其他人将该链接输入浏览器地址栏时，将会在应用中跳转到你的服务器


- DNN 

- CNN 

- RNN 

- GCN





!!! notes
    - [https://zhuanlan.zhihu.com/p/612273051](https://zhuanlan.zhihu.com/p/612273051)
    - [https://zhuanlan.zhihu.com/p/621854926](https://zhuanlan.zhihu.com/p/621854926)