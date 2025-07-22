# 深度学习 | 王树森

## 数据处理基础

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202507160041704.png)

上图展示了几种常见的处理：

1. 数字类型，比如年龄；
2. 二分类，比如性别，用 0/1表示；
3. Categorical data，比如国籍，这里需要用到 one-hot embedding。比如有197个国家，那么就有一个长 197 维的向量，每个索引对应一个国家。是哪个国家则对应数字为1，其他为0

> **为什么不用那个国家的数字进行表示呢？**
>
> 答：这样的话不同国家之间就是可加减的了：1 + 2 = 3，这是不符合情况的。而 One-hot则可以更好地表示: [1,0,0,...,0] + [0,1,....0] = [1,1,0,0,0...,0]
>
> 同时，对于没填写这一栏的用户，直接让这个向量每个元素为0即可。

于是，上面的数据可以表示为如下的向量：

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202507160046651.png)

---

对于文本数据，我们首先可以做的就是统计词频，并且按照词频大小从高到低排序，剔除掉频率低的词，仅保留前一部分。这样的好处是：

1. 删除一些无意义的词，比如名字；
2. 删除一些笔误 Typos，比如 prince / prinse；Hamlet, Hemlet

---


## 文本处理与 Word Embedding 

以IMDB文本分类为例：


- **Tokenization**

也就是把句子切分成单词（或者字符）的过程。注意几个细节：

> 1. 大小写是否转换 (Apple, apple)
>
> 2. 停用词 (A, the, of)
>
> 3. 对错误拼写的纠正：gooood -> good

- **Build dictionary**

也就是把每个单词映射到一个索引（Index）中。


![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202507160059469.png)

- **One-hot encoding**

对数据里的每一段文本进行encoding，encoding后的向量长度是这段话里的Token数 （Tokenization）。此时你会发现每一段文本都不一样长。

- **Text Alignment**

考虑到每个文本不一样长 （Token数不一样），而我们希望把数据存储在矩阵或者向量里面，因此我们希望每一段文本都是一样长的，也就是需要把长的截短（仅保留后 M 个，或者前 M 个 Token），以及把短的变长（zero padding），在前面补上 Null凑成更长的向量。


![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202507160104822.png)

### Word Embedding

对于文本而言，用One-hot embedding来表示每一个Token太奢侈了，因为字典很长（10K），而句子里又有很多Token。

我们如何实现呢？我们可以基于每个Token的One-hot向量，应用一个参数矩阵 $\mathbf{P}^T$ 和One-hot向量 $\mathbf{e}_i$ 的乘法，把一个Token映射成一个低维度的向量 $\mathbf{x}_i$。这里的 $d$ 是Token Embedding的维度，需要用户自己指定，$v$ 是字典里Token的数量。

我们机器学习训练的时候就是在根据训练数据调整这个 $\mathbf{P}^T$

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202507160106006.png)

可以想象，参数矩阵 $\mathbf{P}^T$ 的每一列就表示一个Token的感情色彩。

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202507160111576.png)


### Logistic Regression

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202507160117593.png)

设置词向量的维度是 8 （Cross- Validation确定），同时每一个评论取20个Token。先对它进行Embedding，这样每一个评论就变成了 20 * 8；把它压扁变成 160 的向量；最后一层全连接层，其实就是Logistic  Regression，因为我们约束输出在 0~1 之间并且用 sigmoid 函数激活。

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202507160120952.png)

> 解释一下 Epoch，把所有的训练数据 （20000/25000,5000做 Validation）从头到尾扫一遍，就是一个 Epoch。50 Epoch 意思是把训练数据扫50遍；

整个流程如下：

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202507160122655.png)

> 161 Parameter，是因为还有一个偏移量。

## RNN 

与全连接层、CNN不同在于，序列数据不是 One to One的，而是 Many to One/Many的，（比如，CNN的常见任务是给一张图，输出一个结果，分类，概率，这是One-to-One），但是文本/语音翻译/分类，是需要通过句子的若干部分输出一个/一些回复，其长短不一。

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202507160125849.png)


以下是经典的 RNN 的示意图。


![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202507160127145.png)

按照句子的阅读顺序，在 The 的时候，对这个词进行Word Embedding，然后产生状态向量 $h_0$，到下一个词 cat，对这个词进行Word Embedding，更新状态向量 $h_1$，这个向量就包含了 the 和 cat 的信息，以此类推。最后一个状态 $h_t$ 就是整句话的信息都包含在内的一个向量（它积累了信息！）。

**注意在这个过程中，参数矩阵 $A$ 是一直没有变化的。**

具体而言，我们如何通过 $h_{t -1}$ （前一个Token的状态向量）和 $x_{t}$ （Token做embedding后的向量） 计算出 $h_t$ 呢？

做法就是将 $h_{t -1}$ 和 $x_{t}$ concat成一个长的向量，和参数矩阵相乘，得到的结果还是一个向量。

对这个向量的每一个元素做 $\tanh$ 激活函数，将数值压缩到 -1 和 +1 之间。

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202507160133482.png)


!!! question "为什么需要 $\tanh$，可否去掉？会发生什么？"
    ![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202507160139772.png)

    假如某个embedding为0，此时$h_100$会退化到 $A^{100}h_0$，如果 A 的特征值 0.9，那么此时这个向量会非常小；如果特征值稍大一点，那么这个乘积会超级大。通过 $\tanh$，我们成功把每次矩阵乘法得到的结果压缩在一个合理的区间内。

### 参数量的计算｜结果的计算

参考上图，$\mathbf{A}$ 的行数和状态向量的维度是一样的，而列数等于状态向量和embedding向量concat后的向量长度。因此$\mathbf{A}$ **参数量 = shape (h) $\times$ [shape(h) + shape(x)]**

由于状态向量总是积累了其在之前文本的所有信息，因此我们只需要用最后一个Token的状态向量（相当于一个特征），把它丢入分类器，做sigmoid，也就会输出一个分类的结果了。

比如下图我们就以文本长度500，embedding=32进行对齐，状态向量维度32，每次仅保留最后一个Token的状态向量。此时需要2080个参数（考虑到最后的全连接层）。

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202507160152167.png)


### 存在的问题

非常擅长短期预测 (Short Term Prediction)，但是对于很多Token前的，遗忘很严重。如果步长很长，那么它很容易遗忘先前的信息。

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202507160200617.png)


## LSTM 

类似RNN的一种循环神经网络，但是要复杂很多。RNN只有一个参数矩阵，LSTM有四个。

- **传输带** （Conveyer Belt），过去的信息直接通过传输带传送到下一个时刻不会发生太大变化，LSTM就是借助传输带，**避免梯度消失的问题**。

- <span style="color:red">遗忘门</span>

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202507170137571.png)

$f_t$ 是上一个状态 $h_{t -1}$ 和当前输入 $x_t$  的函数，具体而言是用 $W_f$ 和二者的concat做矩阵乘法得到一个向量，对这个向量做sigmoid激活函数，得到 $f_t$。其大小和状态向量$h_{t-1}$ 是相同的，每一个元素都在 (0, 1) 之间。

这里**有一个遗忘门的参数矩阵 $W_f$，需要通过反向传播学习。**

- <span style="color:red">输入门</span>

需要计算一个输入向量 $i_t$，方式和遗忘门相同（用一个参数矩阵和concat后的状态向量+输入做矩阵乘法，然后sigmoid），**这里需要学习一个参数矩阵 $W_i$。**

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202507170141978.png)

- <span style="color:red">New Value 门</span>
除了这个输入向量外还要计算一个New Value向量 $\tilde{C}_t$，这里做法同上，区别在于激活函数是 $\tanh$，这里的向量每个元素都在 $(-1, 1)$ 之间。注意了，这里**我们还需要学习一个参数矩阵 $W_c$。**

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202507170144733.png)

现在，我们有了前面几个环节的结果，是时候利用传送带了。如下图所示。我们利用遗忘门输出 $f_t$，前一个状态向量 $C_{t-1}$，输入门 $i_t$ 以及Value向量 $\tilde{C}_t$，更新传送带上的状态向量 $C_t$。由于我们先前保证了 $C_t$ 和 $f_t$ 以及 $i_t$ 的尺寸相同，因此可以做 Element Piecewise Multiplication.

譬如 $f_t c_{t-1}$ 的结果表示在当前状态选择性地遗忘掉先前状态的东西；$i_t \tilde{c}_{t}$ 表示向传输带上添加某些新的信息。

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202507170147885.png)

- <span style="color:red">输出门</span>

此时我们更新LSTM的输出。此时我们依然是把两部分做concat，然后**学习一个参数矩阵 $W_o$**，经过sigmoid 后输出一个输出向量 $o_t$，这个向量的大小，与传送带上涉及的若干向量都是相同的。


![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202507170154777.png)

这个时候我们需要更新状态向量 $h_t$，对于传送带上的信息 $C_t$，做 $\tanh$ 之后与输出向量做Element Piecewise Multiplication即可。这里的 $h_t$ 既作为下一个状态的状态向量，又可以作为当前的输出结果，因此做2个copy。


![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202507170157630.png)



综上所述，这里的参数量由4个参数矩阵构成，分别属于：**遗忘门、输入门、新值门、输出门**。每个参数矩阵的参数规模 shape(h) $\times$ [shape(h) + shape(x)]，总参数规模 4 $\times$ shape(h) $\times$ [shape(h) + shape(x)]

<span style="color:red">总而言之，LSTM通过一个传送带，让过去信息容易传输到下一时刻，实现了比RNN更好的长期记忆。</span>

## 提升RNN的若干技巧

### 多层RNN (Stacked RNN)

类似于深度卷积神经网络。原先的RNN，每一个输入的状态向量都直接作为输出以及下一个状态向量，而我们可以在此基础上再堆叠一个 RNN，这个RNN的输入不再是embedding了，而是前一个RNN的状态向量，这个第二层RNN有自己的模型参数，会更新和输出自己的状态向量 $h$，而这个状态向量又会作为第三层RNN的输入，以此类推，越来越深。

最上层RNN的状态向量就是最终的输出了，可以用最后一个状态 $h_t$ 可以视为从最底层的数据提取的特征。

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202507180056255.png)

我们可以直接上堆叠一个LSTM，效果是类似的：

实现如下，注意保存 `return_sequences`。最后将最后一层的状态向量丢入MLP中输出分类结果。

> 计算参数量的时候，4 * 65 * 32，因为concat后有一个偏移项的参数也不能遗忘。

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202507180059959.png)

参数统计如下。注意embedding层的参数量很大（<span style="color:red">缺少足够的数据把这部分训练好，很容易overfitting）</span>，同时，在第一和第二层，我们输出了500（文本长度）个状态向量（大小为32），也就是每个状态向量都被我们输出了。

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202507180101460.png)

注意，上图中可以让4个阶段的向量尺寸有所不同，不一定都是相同的。


### 双向 RNN (Bidirectional RNN)

人类有阅读习惯从左向右从上倒下，但是从右往左进行阅读同样可以帮助我们对文本进行分类。对RNN而言，阅读顺序变化并么有太大区别。训练一个从后往前的RNN同样会有很好效果。


![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202507180110391.png)

一个简单的想法是训练两条RNN，一个从右往左，一个从左往右。两条RNN互相独立==不共享参数，会各自输出对应的状态向量==，两个状态向量 concat 起来就形成了真正的状态向量 $y_1, y_2, ... , y_t$。如果有多层RNN，就把输出的 y 作为上层RNN的输入，以此类推。

<span style="color:red">这个双向RNN的输出，就是把两条RNN分别走到最后输出的向量 $h^{'}_t, h_t$ 做一个concat，成为这段文本的特征向量。</span>

> 一般而言，双向RNN效果比单向的要好很多，因为从一个方向阅读容易忘记前面的，现在可以比原先的特征多记住一些信息了（一个记得更靠左边的，一个记得更靠右边的）。

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202507180117820.png)

我们可以发现参数量就是单层的2倍。

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202507180118839.png)

实际做的时候，两种方法都试试（双向+stack）。

### 预训练

Pretrain。一种非常常用的技巧。在CNN里就有涉及。比如你的训练集不够大，但是参数又很多，于是你可以先在一个更大的数据集上训练一个模型，**让神经网络有比较好的初始化参数（尤其是embedding），避免overfitting**。


具体做法：

1. 找一个更大的数据集（最好是接近原先的任务，比如情感分析）；
2. 搭建并训练一个大的神经网络；
3. 只保留embedding和对应参数，训练上层的参数；**embedding这部分的参数固定住不需要训练**

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202507180122940.png)


!!! conclusion "这类问题用LSTM效果往往会好一些，应用时候可以多试试不同的结构，比如Stacked Bi-LSTM等。这几个Idea对所有的RNN都适用。而且LSTM能记住更多信息，不容易遗忘"


## 自动文本生成

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202507230156683.png)

输入半句话，要求预测下一个**字符**。可以训练神经网络，用one-hot embedding来表示每个字符，在大量文本上以字符维度进行训练。最终输出一个向量（用softmax做概率分布）。就可以拿到概率最大的那个字符。


如何训练这个RNN？设置步长stride和每个切片的大小。训练时，需要基于每个切片内的文本，正确给出下一个字符（即为这个字符的概率最大）。此时下一个字符就是label，每个segment就是输入的文本，训练数据就是 (segment, char) 的pair。其实质上就是**一个多分类问题**（类别数是所有的字符数）。


![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202507230203640.png)


> 1. 一些应用：生成名字；这说明文本生成器不是记住数据，而是能够生成新的东西。
>
> 2. SCIGen 

### 简单字符生成器的实现

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202507230209871.png)

> 生成字符切片。

由于我们是字符生成，因此总共可能也就几十个字符，不需要做低维的embedding了，直接用one-hot embedding即可。

现在假设每个片段有60个字符，而我们需要输出的字符总共有57个（字典大小），那么每一segment就是 60 * 57 的矩阵。需要进行一个有 57 分类的多分类预测。

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202507230212027.png)


【待补充】