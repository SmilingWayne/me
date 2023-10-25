# 高级的运筹学方法与求解技巧


## 列生成算法 / Cutting Stock Problem(CSP)

> 写在前面：
> 
> 主要参考链接：首推[这个B站视频](https://www.bilibili.com/video/BV1Sv411z7VY/)，强烈推荐这个合集，整理得十分详细，中英文课程都有，还有很多参考链接（或者教你找参考链接的方法）。 
>
> 其次推荐Gurobi 官网的 [这个傻瓜教程](https://www.gurobi.com/resources/cutting-stock-problem-with-multiple-master-rolls/)。很专业，你值得拥有。你注册之后甚至直接输入数据，能帮你把可视化结果都搞出来，寓教于乐。
> 
> ![](image/ColumnGeneration/Figure0.png)
> 
> 最后写作过程同样参考了[这个知乎文章](https://zhuanlan.zhihu.com/p/508388014)，以及[这个 OR文章](https://zhuanlan.zhihu.com/p/118516953)（同是OR发电人，相逢何必曾相识）

### Cutting Stock Problem（下料问题）

有三种型号的钢材，9寸、14寸和16寸的木材，其成本分别为5，9，10. 我们也有一系列的订单：

|  原料长度  |   成本   |
| :--------: | :------: |
|     9      |    5     |
|     14     |    9     |
|     16     |    10    |
| 小木材长度 | 需求数量 |
|     4      |    30    |
|     5      |    20    |
|     7      |    40    |




怎么切分这些钢材（假设有无限钢材），使得所用到的木材的成本最小。

这个问题最初是前苏联科学家Kantorovich提出并建模的，最初的模型与现在略有不同，我们暂时不表。先展开目前我们最常用的解决方法。

列出一些（不用列所有的）**切割方法**（Cutting Pattern）。什么是切割方法？比如，对于 **一个** 9寸的木板，我们可以把它切成2个4寸的，也可以把它切成1个4寸的，一个5寸的；对于一个14寸的木板，我们可以切成3个4寸的，也可以切成2个四寸的，一个5寸的，还可以，比如说利用率低一点，只切成2个4寸的（只不过这种情况下你一眼就能看出来，这种切法效率不高，分明可以用1个9寸木板就切出来）…… 如此，每个切法就是一个Pattern。


|   方案   | 切出的4寸个数 | 切出的5寸个数 | 切出7寸的个数 | 需要的成本 |
| :------: | :-----------: | :-----------: | :-----------: | :--------: |
|  $x_1$   |       2       |       0       |       0       |     5      |
|  $x_2$   |       1       |       1       |       0       |     5      |
|  $x_3$   |       0       |       0       |       1       |     5      |
|  $x_4$   |       3       |       0       |       0       |     9      |
|  $x_5$   |       2       |       1       |       0       |     9      |
|  $x_6$   |       1       |       2       |       0       |     9      |
|  $x_7$   |       1       |       0       |       1       |     9      |
|  $x_8$   |       0       |       1       |       1       |     9      |
|  $x_9$   |       0       |       0       |       2       |     9      |
| $x_{10}$ |       4       |       0       |       0       |     10     |
| $x_{11}$ |       2       |       0       |       1       |     10     |
| $x_{12}$ |       1       |       1       |       1       |     10     |
| $x_{13}$ |       0       |       3       |       0       |     10     |
|   ...    |      ...      |      ...      |      ...      |    ...     |

上面列的不是“所有可能的pattern”，仅作示意，实际切法很多，我们主要罗列的是“比较高效利用木板”的切法。

一个示意图如下：

![](image/ColumnGeneration/Figure1.png)

现在我们的目标就变成了“最小化总成本，也就是所用的切法 $\times$ 用这种切法的木板数”。

接下来写数学模型。

$$\min \sum c_j x_j \\
s.t. \begin{aligned}\begin{equation*}
\begin{cases}
\sum \mathbb{a_j} \mathbb{x_j} \geq \mathbb{b} \\
x_j \in \mathbf{Z}
\end{cases}
\end{equation*}\end{aligned}$$

解释一下 $\mathbb{a_j}$ 对应了什么。

这是个向量，$\mathbb{a_j} = \begin{bmatrix} a_{1j} \\ a_{2j} \\ a_{3j} \end{bmatrix}$，表示第 $j$ 个pattern中，切出的第1个长度的木材、第二个长度的木材、第3个长度的木材的数量。(英文的具体解释是 $a_{ij}$ is the quantity of i-th length piece for the j-th cutting pattern) 而 $\mathbb{b}$ 就是，需求的3种木材的数量，在这个例子中就是 $\begin{bmatrix} 30 \\ 20 \\ 40 \end{bmatrix}$。

-------------

#### 求解 

现在怎么求解这个问题？

传统方法，当然是**暴力枚举**。大不了我把所有的pattern都列下来，然后解一个确定模型即可。

$$\min 5x_1 + 5x_2 + ... + 9x_9 + 10x_{10} + 10x_{11} + 10 x_{..}\\
s.t. \begin{aligned}\begin{equation*}
\begin{cases}
2x_1 + x_2 + 3x_4 + 2x_5 + x_6 + x_7 + 4x_{10} + 2x_{11} + x_{12} + .. \geq 30 \\
x_2 + x_5 + 2x_6 + x_7 + x_8 + x_{12} + 3 x_{13} + .. \geq 20 \\ 
x_3 + x_7 + x_8 + 2x_9 + x_{11} + x_{12} + .. \geq 40
\end{cases}
\end{equation*}\end{aligned}$$

这个传统方法有什么问题呢？

1. 如果我木材的长度增加，我可以切出来的木板数量一定是指数增长的，我们上面的式子<u>其实没有枚举完全部的切法。</u>（想象一下，如果你的原材料都是100，150，200的长度木材，但是你需要的都是4，5，9寸这种短木材，你100就可以切：25个4，或者23个4，1 个5 ... 情况很多很多）
2. 有一些切法可以明显看出利用率比较低。但是实现的时候很难具体发现哪些利用率低，而是一股脑把所有的切法都写上去。比如你可能会算出一种 $x_{14}$ pattern，切1个4寸，1个5寸，0个7寸的。这种利用率会比：1个4寸，2个5寸，0个七寸的，浪费很多。

--------



解决这个问题一个最基本也是最重要的思路就是，我们可不可以把一些利用率高、效果好的切法放进去，其他效果不好、利用率低的，就不当作pattern了。

这个insight就是“列生成（Column Generation）”的想法。我们在后面解释这三个字的含义。我们先展开说具体实现。

我们有一个主问题：Master Problem(MP)，这个MP可能不是所有的变量，只有一部分的变量（limited number of patterns，相比较所有的pattern来说）。也正因此我们也叫 **restricted master problem** （RMP）。我们用算法解这个RMP之后，就想，我们能不能得到一个新的Pattern，让原来的结果更好。

> Can I get a pattern, to improve the current solution?
>
> 这里的底层逻辑，和单纯形法是一样的，回想一下，每次进-出基，就是实现了一次Improve。唯一的区别在哪里？在于，单纯形法的进、出基变量，一开始就已经存在在单纯形表里了。**而在列生成里，进基变量不在模型里，而是要你去找的。** 

解好RMP后，我们就能得到每个约束对应的 Dual Cost（就是对偶问题的解），我们要利用Dual Cost，求解子问题（Sub-Problem），从而找到一些“好”的Pattern(s)，这些Pattern(s)不在原来的模型里，但是可以提高当前目标的质量（Improve current Solution）. 我们把这些“好”的Pattern加入到RMP中，继续迭代。

英文描述更加具体：

> In Column Generation, Can we find a $x_{n + 1}$ such that $\delta_{n + 1} - c_{n + 1} > 0$。
> 
> 这个公式实际就反映单纯形法的“检验数”

$\delta_{n + 1} - c_{n + 1} = \omega a_{n + 1} - c_j  = \sum \omega_i a_{ij} - c_j$

这里的 $\omega_i$ 就是约束 $i$ 对应的对偶成本（影子价格）。

!!! note "展开讲讲"
    这里结合一下前面的数据来解释一下对偶的意义。

    案例里约束对应的右端项 $\mathbb{b} = \begin{bmatrix} 30 \\ 20 \\ 40 \end{bmatrix}$ , $\omega_1, \omega_2, \omega_3$ 分别对应这三个约束。经济意义是，要多切出一个（4寸or，5寸or 7寸）的木板，可以**获得的价值**。

    - reduced cost的意义就是， 如果我按照某方案多切的4寸、5寸、7寸的价值，加起来，比我切这个方案花的钱还要多，我就赚了。


我们的子问题就是，对于一个木材，要切几个4寸的，几个5寸的，几个7寸的？这就是 $a_{ij}$。

我们可以写出表达式：

$c_{n + 1}$ 就是“总长度花了的钱”

$$\max \delta_{n + 1} - c_{n + 1} > 0 \\
s.t. \begin{aligned}\begin{equation*}
\begin{cases}
 \sum^m_{i = 1} a_{ij} l_i \leq L_k \\
 a_{ij} \in \mathcal{N^+}
\end{cases}
\end{equation*}\end{aligned}$$


这里的 $L_k$，对应你原材料的长度的种类，比如9，14，15。如果你从9寸的开始切，$L_k = 9$，以此类推。每个长度都算一遍。

这里的 $l_i$ 就是，第 $i$ 种目标木材的长度（对应4，5，7），$m$ 对应目标木材的下标。

这里有一种情况，比如说我们 $L_k$ 有三种情况，会不会每个 $L_k$ 求下来，目标函数总是 $\leq 0$ 的。**这就意味着：不管我怎么折腾3种原材料，怎么切，都不存在一个更好的方案，使得价值 - 成本 > 0了**，也就意味着，我们已经找到了最优解。

if $\max \sum_i \omega_i a_{ij} - c_k \leq 0, \forall k$，stop. Found Opt Sol.

if $\max \sum_i \omega_i a_{ij} - c_k > 0$ , pattern is good, add to RMP.

#### 实战

- **Step 0. Init**  

$a_1 = \begin{bmatrix} 2 \\ 0 \\ 0 \end{bmatrix}, a_2 = \begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix}, a_3 = \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}, c_1 = 5, c_2 = 5, c_3 = 5$， 

- **Iter 1.**

$$\min 5x_1 + 5x_2 + 5x_3 \\ \text{s.t.} \hspace{5pt} a_1 x_1 + a_2x_2 + a_3 x_3 \geq \begin{bmatrix} 20 \\ 40 \\ 50 \end{bmatrix}$$

Solve RMP, $x^* = \begin{bmatrix} 15 \\ 20 \\ 40 \end{bmatrix}, \omega^* = \begin{bmatrix}  2.5 \\ 5 \\ 5 \end{bmatrix}$

- Sub Problem 1. （切9寸长的）

$$\max 2.5 a_{1j} + 5 a_{2j} + 5 a_{3j} - 5 \\
s.t. \begin{aligned}\begin{equation*}
\begin{cases}
4_a{1j} + 5a_{2j} + 7a_{3j} \leq 9 \\
a_{ij} \in Z^*
\end{cases}
\end{equation*}\end{aligned}$$

- Sub Problem 2. （切14寸长的）

$$\max 2.5 a_{1j} + 5 a_{2j} + 5 a_{3j} - 9 \\
s.t. \begin{aligned}\begin{equation*}
\begin{cases}
4_a{1j} + 5a_{2j} + 7a_{3j} \leq 14 \\
a_{ij} \in Z^*
\end{cases}
\end{equation*}\end{aligned}$$

- Sub Problem 3. (切16寸长的)

$$\max 2.5 a_{1j} + 5 a_{2j} + 5 a_{3j} - 10 \\
s.t. \begin{aligned}\begin{equation*}
\begin{cases}
4_a{1j} + 5a_{2j} + 7a_{3j} \leq 16 \\
a_{ij} \in Z^*
\end{cases}
\end{equation*}\end{aligned}$$

仔细看：这三个问题实际上都是背包问题。有很多解法。

- Sub Problem 1. Sol $a_j = \begin{bmatrix} 1 \\ 1 \\ 0 \end{bmatrix}$, Obj = 2.5
- Sub Problem 2. Sol $a_j = \begin{bmatrix} 1 \\ 2 \\ 0 \end{bmatrix}$, Obj = 3.5
- Sub Problem 3. Sol $a_j = \begin{bmatrix} 0 \\ 3 \\ 0 \end{bmatrix}$, Obj = 5

这三个情况下我们发现目标函数都 > 0。我们可以把3个都加到主问题里，也可以只加Obj最大的那个。但是要注意，不同的加法对收敛性的影响是不同的。

我们把第3个情况（max Obj），加入RMP中。新问题就多了一个决策变量，多了一个pattern！如下。

$$\min 5x_1 + 5x_2 + 5x_3  + 10 x_4, \\ s.t. 
a_1 x_1 + a_2x_2 + a_3 x_3 + a_4x_4 \geq \begin{bmatrix} 20 \\ 40 \\ 50 \end{bmatrix}$$


这里就进入下一个迭代。

- Iter 2. 解新的 RMP。

$x^* = \begin{bmatrix} 15 \\ 0 \\ 40 \\ 20 / 3 \end{bmatrix}, \omega = \begin{bmatrix} 5 / 2 \\ 10 /3 \\ 5 \end{bmatrix}$。有变化的是新的 dual Cost.

我们继续按照上面的写子问题，注意**子问题的目标函数参数**也要调整！


- Sub Problem 1. （切9寸长的）

$$\max 2.5 a_{1j} + \frac{10}{3} a_{2j} + 5 a_{3j} - 5 \\
s.t. \begin{aligned}\begin{equation*}
\begin{cases}
4_a{1j} + 5a_{2j} + 7a_{3j} \leq 9 \\
a_{ij} \in Z^*
\end{cases}
\end{equation*}\end{aligned}$$

- Sub Problem 2. （切14寸长的）

$$\max 2.5 a_{1j} + \frac{10}{3} a_{2j} + 5 a_{3j} - 9 \\
s.t. \begin{aligned}\begin{equation*}
\begin{cases}
4_a{1j} + 5a_{2j} + 7a_{3j} \leq 14 \\
a_{ij} \in Z^*
\end{cases}
\end{equation*}\end{aligned}$$

- Sub Problem 3. (切16寸长的)

$$\max 2.5 a_{1j} + \frac{10}{3} a_{2j} + 5 a_{3j} - 10 \\
s.t. \begin{aligned}\begin{equation*}
\begin{cases}
4_a{1j} + 5a_{2j} + 7a_{3j} \leq 16 \\
a_{ij} \in Z^*
\end{cases}
\end{equation*}\end{aligned}$$

解下来结果分别是：

1. $a_j = \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}, \delta_j - c_1 = 0$

2. $a_j = \begin{bmatrix} 0 \\ 0 \\ 2 \end{bmatrix},\delta_j - c_2 = 1$

3. $a_j = \begin{bmatrix} 0 \\ 0 \\ 2 \end{bmatrix},\delta_j - c_3 = 0$

我们当然选第二个 a_j 加入RMP中。

- Iter 3: 这时候RMP有5个变量了。解下来 $x^* = \begin{bmatrix} 15 \\ 0 \\ 0 \\ 20  / 3 \\ 20 \end{bmatrix}, \delta^* = 322. \omega = \begin{bmatrix} 5 / 2 \\ 10 / 3 \\ 9 / 2 \end{bmatrix}$

这里继续求解子问题。公式就不列了！太长了！直接写结果。

1. $a_j = \begin{bmatrix} 1 \\ 1 \\ 0 \end{bmatrix}, \delta_j - c_1 = 0.82$;

2. $a_j = \begin{bmatrix} 1 \\ 2 \\ 0 \end{bmatrix}, \delta_j - c_2 = 0.17$;

3. $a_j = \begin{bmatrix} 0 \\ 3 \\ 0 \end{bmatrix}, \delta_j - c_3 = 0$,

选择 $a_j = \begin{bmatrix} 1 \\ 1 \\ 0 \end{bmatrix}$ 加入主问题，继续迭代。

- Iter 4. 解RMP，$x^* = \begin{bmatrix} 5 \\ 0 \\ 0 \\ 20 \\ 20 \end{bmatrix}，\delta = 305， \omega = \begin{bmatrix} 5 /2 \\ 5 /2 \\  9 /2 \end{bmatrix}$

继续解子问题～

1. $a_j = \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}, \delta_j - c_1 = -0.5$;

2. $a_j = \begin{bmatrix} 0 \\ 0 \\ 2 \end{bmatrix}, \delta_j - c_2 = 0$;

3. $a_j = \begin{bmatrix} 0 \\ 0 \\ 2 \end{bmatrix}, \delta_j - c_3 = 0$,

我们发现所有的检验数都是非正的。找到最优解了。停止迭代。


!!! note "备注"
    这里还需要注意，我们求背包问题的时候，对具体的求解算法**没有具体要求**，我们甚至不一定要求到子问题的最优解。在实际问题中，最优解的求解反而可能是十分困难的。面对复杂的子问题，我们只要求得一个可以Improve 原问题的解，就够了。这意味着哪怕是启发式的算法、遗传算法之类，同样可以在求解子问题上发挥作用。

!!! info "一些小问题的处理"

    这个例子很经典，答案也很好，但是有个小问题。我们解最后一个RMP得到的正好是整数，（线性松弛问题解出的正好是IP的解）。如果解不到整数解怎么办？

    1. 用你生成的所有变量（e.g. 有6000个），解RMP，不过不再是解LP，而是添加IP约束。一般情况下，IP和LP之间的Gap，会很小。
    2. 如果第一种方法还是不好，就需要用 Branch-And-Price 去解决这个问题。这个想法就是把 Branch and Bound 和Column Generation结合起来。


---------

## Benders 分解 




-------------


## Branch and Price 





------------


