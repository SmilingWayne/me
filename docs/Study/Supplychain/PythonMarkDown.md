<h2>什么是幻方？</h2>
<b>幻方(Magic Square)</b>是一种将数字安排在正方形格子中，使每行、列和对角线上的数字和都相等的方法。正方形格子的边长就是阶数。

<br>

譬如下面的四个就都是三阶幻方。其对角线、每行、每列的和都是15。
<br>
<div align=center><img src = "./picx/magic1.png" width = "70%" ></div>
<br>

那么给定阶数$n, n \geq 3$, 如何生成一个可行的幻方呢？如果给定奇数，幻方同样可以生成吗？

答案是肯定的，并且在研究过程中还有多种不同的生成算法。这个“随便写写”系列就是简单地实现了一些相关算法。

具体的思路是把情况分为：
1. 阶数是奇数
2. 阶数是$4n + 2 $型偶数 (也就是6，10，14...这类不能被4整除的)
3. 阶数是$4n $型偶数 (也就是4，8，12...这类能被4整除的)
-----
<h2>阶数为奇数</h2>
<center><h2>罗伯法（连续摆数法）</h2></center>

把1（或最小的数）放在第一行正中，并按以下规律排列剩下的(n×n－1)个数：

- 每一个数放在前一个数的右上一格；
- 如果这个数所要放的格已经超出了顶行那么就把它放在底行，仍然要放在右一列；
- 如果这个数所要放的格已经超出了最右列，那么就把它放在最左列，仍然要放在上一行；
- 如果这个数所要放的格已经超出了顶行且超出了最右列，那么就把它放在底行且最左列；
- 如果这个数所要放的格已经有数填入，那么就把它放在前一个数的下一行同一列的格内。

<div align=center><img src = "./picx/Magic2.png" width = "100%" ></div>

--- 
<h2>阶数是4n型偶数</h2>
<center><h2>海尔法</h2></center>

以8阶幻方为例：

1. 先把数字按顺序填。然后，按4×4把它分割成4块
2. 每个小方阵<b>对角线</b>上的数字，换成和它互补的数。


<div align=center><img src = "./picx/Magic3.png" width = "100%" ></div>

----

<h2>阶数是4n+2型偶数</h2>
<center><h2>斯特雷奇法</h2></center>

当n不可以被4整除时的偶数阶幻方，即4k+2阶幻方，半阶数m = n/2。

**算法：**

以10阶幻方为例。这时，k=2，m = 5。

1. 把n阶矩阵分为$A,B,C,D$四个象限（分别对应象限2,1,3,4），这样每一个象限肯定是奇数阶，阶数为m。按照奇数阶的方法用数字$[1, (n/2)^2]$ 在A象限填写数字，并用A象限初始化其他象限，其中$B = A+2m^2，C = A + 3m^2，D = A + m^2$。如图1。

2. 在A象限的中间行、中间格开始，按自左向右的方向，标出k格。A象限的其它行则标出最左边的$k$格。将这些格，和C象限相对位置上的数，互换位置。如图2。

3. 在B象限任一行的中间格，自右向左，标出$k-1$列。 将B象限标出的这些数，和D象限相对位置上的数进行交换，就形成幻方。



<div align=center><img src = "./picx/Magic4.png" width = "150%" ></div>



--- 

<h3>题目描述：</h3>

> 求正整数N以内的所有素数
> 给定正整数区间[a, b),给出区间内所有的素数

----


<h3>埃氏筛</h3>

做法其实很简单，C语言入门课程都会有讲。首先将2到n范围内的所有整数写在一张一维表里，其中2是最小的素数。将表中所有2的倍数划去，此时表中剩下的最小的数字是3，3无法被更小的数整除，所以3是素数。再将表中所有3的倍数划去......以此类推，如果表中剩余的最小数是m，则m就是素数，将表中所有m的倍数划去，这样反复操作，就能依次枚举n以内的素数，时间复杂度为$O(nloglogn)$

<div align=center><img src = "./picx/sieve1.png" width = "150%" ></div>
<br>

----
<h3>欧拉筛（线性筛）</h3>

由于每个大于等于2的合数必定存在一个最小的质因数，所以只要筛去每个质数的倍数就相当于筛去了所有合数。但欧拉筛相比埃氏筛最大的优化就在于欧拉筛保证每个合数只被筛了一次，且是被其<font color = "Darkpink">最小的质因数</font>筛去的，所以欧拉筛的时间复杂度可以达到$O(N)$。

<br>
这种算法也可以快速获取最小质因数。

----
<h3>素数区间筛</h3>

给定整数a和b，请问区间$[a,b)$内有多少个素数？（$a < b \leq 10^{12},b-a \leq 10^6$）

因为$b$以内合数的最小质因数一定不会超过$\sqrt{b}$.

如果有$\sqrt{b}$以内的素数表的话，就可以把埃式筛法用在$[a,b)$上了。也就是说，先分别做好$[2,\sqrt{b})$的表和$[a,b)$的表，然后从$[2,\sqrt{b})$的表中筛得素数的同时，也将其倍数从$[a,b)$的表中筛去，最后剩下的就是区间$[a,b)$内的素数了。






<br>
<br>
<br>
<br>
<br>
<br>
<br><br>
<br>

<br>
<br>

<br>
----

<center><h1>手机App评论爬取</h1></center>

---

<font color = "Blue"><h2>实现思路</h2></font>

<font size = 5>🟥 在移动端浏览请求界面，请求数据</font>
<font size = 5>🟧 在电脑端利用抓包软件抓取移动端接收到的数据</font>
<font size = 5>🟨 对数据进行清洗、整理、汇总</font>

---
<font color = "Red"><h2>技术细节</h2></font>

<font size = 5>🟩 抓包软件是Charles,适用性很好(Windows /macOS/Linux都可，Android/iOS全部支持）。我是macOS系统+iOS🍎手机配置，运行时候效果👍</font>
<font size = 5>🟩 Charles正版是收💰的，有条件一定支持一波，可以找到pojie版本，我是在52pojie上找到的，上面也有<u>手把手的Charles</u>使用教程，跟着做就可以</font>
<font size = 5>🟪 数据清洗用了Python，主要做的就是解析Json数据并进行本地存储</font>

---
<font color = "Purple"><h2>具体实现</h2></font>

<font size = 5>⬛️ 以防大家⬇️ 错，我用的Charles长这样👇</font>
<div align=center><img src = "./picx/charles.png" width = "80%" ></div>
<font size = 5>⬛️ Charles数据获取界面👇</font>

<div align=center><img src = "./picx/结果2.png" width = "100%" ></div>

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<center><h1><font color = "DarkBlue" size = 500><u>Python</u> </font>练手项目</h1></center>
<br>
<br>
<br>
<br>
<center><h1><font size = 100 color = "">实现复杂计算器</font></h1></center>
<!-- <center><h3><font color = "DarkPink">Charles抓包</font> | <font color = "Blue">Python 数据处理</font></h3></center> -->
<center><font color = "DarkPink" size = 20>Calculator</font></center>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<h1>什么是拉丁方(Latin Square)</h1>

----
给定正整数$N$，把$N$组1到$N$的正整数填入一个$N \times N$的正方形格子中，使得：

1. 每一行，$1 ～ N$都出现且只出现一次
2. 每一列，$1 ～ N$都出现且只出现一次

例如下面的这个就是一个经典的三阶拉丁方.

<div align=center><img src = "./picx/LatinSquare.jpeg" width = "50%" ></div>

<br>
<br>
拉丁方可以视作数独的一种松弛形式，不同于数独的九宫格，拉丁方没有“宫”的设计，而只有“格”。也就是说，数独是一种更加严格的拉丁方。
<br>
<br>
<br>
<br>

<h1>拉丁方生成算法</h1>

----

$N$是偶数时:第一行：$1，2，N，3，N - 1，4，N - 2...$
随后的每一行都是在前一行的数字上加$1$，如果结果为$N + 1$，就写成$1$。一直运行到最后一行，直到形成拉丁方。

假设$N = 6$，第一行按算法排列为：

$\qquad \qquad \qquad  \qquad \qquad 1, 2, 6, 3, 5,4$,

同理执行剩下的六行，结果为：

$\qquad \qquad \qquad  \qquad \qquad 2, 3, 1, 4, 6, 5$
$\qquad \qquad \qquad  \qquad \qquad 3, 4, 2, 5, 1, 6$
$\qquad \qquad \qquad  \qquad \qquad 4, 5, 3, 6, 2, 1$
$\qquad \qquad \qquad  \qquad \qquad 5, 6, 4, 1, 3, 2$
$\qquad \qquad \qquad  \qquad \qquad 6, 1, 5, 2, 4, 3$

拉丁方就形成了。

$N$是奇数时，按照上面的格式生成一个方阵后，将每一行倒过来，就可以输出拉丁方了。


<br>
<br>
<br>
<br>



<h1>Python 复杂计算器</h1>

----
✅ $\quad$<font size=5 color = "Black">**要求**</font>

<font size=4 color = "grey">输入一个字符串表示的代数式，输出计算结果</font>

✅ $\quad$<font size=5 color = "Black">**特性和功能**</font>


🟪 <font size=4 color = "grey">支持 $+ - \times \div$， 支持乘方运算、三角函数、自然对数、指数函数计算</font>

🟩 <font size=4 color = "grey">保证运算符优先级、括号优先级，可以处理多余括号</font>

🟧 <font size=4 color = "grey">递归法支持嵌套运算</font>

🟦 <font size=4 color = "grey">支持正负数计算</font>

✅ $\quad$<font size=5 color = "Black">**具体实现**</font>

🔴 <font size=4 color = "grey">递归处理函数嵌套</font>

🟡 <font size=4 color = "grey">堆(Stack)+优先性判断处理具体计算</font>


❌ $\quad$<font size=5 color = "Black" >**尚未完成的部分**</font>


☑️  <font size=4 color = "grey">几个其他常用科学计算函数，例如开方、阶乘、任意底数的对数、反三角函数等</font>

☑️  <font size=4 color = "grey">异常情况检测（分母0、对数<0等情况的检查、提示、字符串是否合法）、可视化</font>





<br>
<br>
<br>
<br>

<br>
<br>
<br>
<br>


<br>
<br>
<br>
<br>

<br>
<br>
<br>
<br>

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<center><h1><font color = "DarkBlue" size = 500><u>Python</u> </font>可视化</h1></center>
<br>
<br>
<br>
<br>
<center><h1><font size = 7 color = "">用日历图可视化聊天记录</font></h1></center>
<br>
<center><h3><font color = "DarkPink">Pyecharts</font> | <font color = "Blue">Python Visualization</font>| <font color = "Green">Calendar</font></h3></center>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

<h1>日历图可视化步骤</h1>


✳️ $\quad$<font size=5 color = "Black" face = "Kai">**小记录**</font>

<font size = 4 color = 'grey' face = "HEI">这是半年前一次小的尝试，当时提取微信聊天记录做了一些分析，整理时候发现不少可以用的东西，用笔记记录一下。当然了为了减少个人信息泄露，数据已经做了随机处理。不过模板是可以直接套用的。</font>

✅ $\quad$<font size=5 color = "Black" face = "Kai">**数据预处理**</font>

<font size=4 color = "grey" face = "HEI">整理出聊天记录，利用时间序列数据清洗方法，得到每一天聊天数量，存储为结构化数据。</font>

✅ $\quad$<font size=5 color = "Black" face = "Kai">**Python可视化**</font>

<font size=4 color = "grey" face = "HEI">借助可交互可视化包<font  color = "Purple">`Pyecharts`</font>绘制日历图</font>


✅ $\quad$<font size=5 color = "Black" face = "Kai">**Pyecharts特性**</font>

<font size=4 color = "grey" face = "HEI">比较适合做注入网站动态可视化、用户大数据界面等，但是不大适合用作科研制图，操作不算困难，有中文文档📁。</font>

<font size=4 color = "grey" face = "HEI">具体代码附在后一张图上。</font>

<br>
<br>


<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<center><h1><font color = "DarkBlue" size = 500><u>Python</u></font><font size = 100 face = "Hei"> 机器学习</font size> </h1></center>
<br>
<br>
<br>
<br>
<center><h1><font size = 7 color = "">分类问题模板</font></h1></center>

<center><h1><font size = 6 color = "">Classification</font></h1></center>


<center><h2><font color = "DarkPink"></font> <font color = "Green">SVM | <font color = "GreyYellow">KNN ｜ <font color = "Navy">LR ｜</font> <font color = "DarkPink">Naive Bayes</font></font></font></h2></center>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>




<h2>模板注释</h2>

✳️ $\quad$<font size=5 color = "Black" face = "Kai">**小记录**</font>

<font size = 4 color = 'grey' face = "HEI">从Github上找的一个合集，自己做了一点总结。主要针对分类问题而言的，稍微有条理一些。</font>

🟪 $\quad$<font size=5 color = "Black" face = "Kai">**算法**</font>

<font size=4 color = "grey" face = "HEI">本笔记不会详细展开每一个算法本身，都是一些很著名的、需要仔细琢磨的算法。相关介绍都已经很多了。</font>

🧡 &nbsp; <font size=4 color = "grey" face = "HEI">**线性回归Linear Regression**</font>

💜 &nbsp;  <font size=4 color = "grey" face = "HEI">**支持向量机SVM**</font>

💚 &nbsp; <font size=4 color = "grey" face = "HEI">**朴素贝叶斯Naive Bayes**</font>

💛 &nbsp; <font size=4 color = "grey" face = "HEI">**K近邻算法KNN**</font>

<font size=4 color = "grey" face = "HEI"></font>

✅ $\quad$<font size=5 color = "Black" face = "Kai">**Matplotlib可视化**</font>

<font size=4 color = "grey" face = "HEI">代码里只写了画分类结果图，实际还有ROC曲线之类的，在前段时间LSTM的那个NLP笔记里记录了，可以移步查看。</font>


✅ $\quad$<font size=5 color = "Black" face = "Kai">**备注**</font>

<font size=4 color = "grey" face = "HEI">代码仅仅展示了进行机器学习任务的一个基本流程和代码，具体的算法、数据、优化、调参等过程都是具体而有挑战的，本笔记仅供参考。</font>



<font size=4 color = "grey" face = "HEI">具体代码附在后一张图上。</font>



<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

<center><h1><font color = "DarkBlue" size = 500><u>Python</u></font><font size = 100 face = "Hei"> 算法补全</font size> </h1></center>

<br>
<br>
<br>
<br>
<center><h1><font size = 7 color = "">DFS 深搜</font></h1></center>

<center><h1><font size = 7 color = ""><font color = "DarkPink">记忆化搜索 ｜ 迷宫</font></h1></center>



<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>


<h2>模板注释</h2>

✳️ $\quad$<font size=5 color = "Black" face = "Kai">**小记录**</font>

<font size = 4 color = 'grey' face = "HEI">从Github上找的一个合集，自己做了一点总结。主要针对分类问题而言的，稍微有条理一些。</font>

🟪 $\quad$<font size=5 color = "Black" face = "Kai">**算法**</font>

<font size=4 color = "grey" face = "HEI">本笔记不会详细展开每一个算法本身，都是一些很著名的、需要仔细琢磨的算法。相关介绍都已经很多了。</font>

🧡 &nbsp; <font size=4 color = "grey" face = "HEI">**线性回归Linear Regression**</font>

💜 &nbsp;  <font size=4 color = "grey" face = "HEI">**支持向量机SVM**</font>

💚 &nbsp; <font size=4 color = "grey" face = "HEI">**朴素贝叶斯Naive Bayes**</font>

💛 &nbsp; <font size=4 color = "grey" face = "HEI">**K近邻算法KNN**</font>

<font size=4 color = "grey" face = "HEI"></font>

✅ $\quad$<font size=5 color = "Black" face = "Kai">**Matplotlib可视化**</font>

<font size=4 color = "grey" face = "HEI">代码里只写了画分类结果图，实际还有ROC曲线之类的，在前段时间LSTM的那个NLP笔记里记录了，可以移步查看。</font>


✅ $\quad$<font size=5 color = "Black" face = "Kai">**备注**</font>

<font size=4 color = "grey" face = "HEI">代码仅仅展示了进行机器学习任务的一个基本流程和代码，具体的算法、数据、优化、调参等过程都是具体而有挑战的，本笔记仅供参考。</font>



<font size=4 color = "grey" face = "HEI">具体代码附在后一张图上。</font>

