<style>
.centertable 
{
  width: auto;/*表格宽度*/
  /* display: table;
  margin: auto;
  align: auto; */
}
</style>

# 线性规划的对偶理论


## 2.1 对偶问题


- 对偶：对同一个事物/问题从不同的角度（立场）提出的不同表述；

> 工厂利用手中资源生产两种产品，如何使得利润最大？
> 
> 对偶：假定一个公司试图把工厂的生产资源全部收购，那么至少要付出多少代价才能使工厂放弃生产活动、让出全部资源？

原问题：

$$\mathop{\max} \hspace{3pt} z = \sum^{n}_{j = 1}{c_j x_j}$$

$$s.t. \sum^{n}_{j = 1}{a_{ij}x_j} \leq b_i  \hspace{12pt} ( i =1,...,m)$$

$$x_j \geq 0 \hspace{12pt} (j = 1,...,n)$$

对偶问题：

$$\mathop{\min} \hspace{3pt} w = \sum^{m}_{i = 1}{b_i x_i}$$ 

$$s.t. \sum^{m}_{i = 1}{a_{ij}y_i} \geq c_i  \hspace{12pt} ( j =1,...,n) $$

$$ y_j \geq 0 \hspace{12pt} (i = 1,...,m)$$

- **对称形式**(Symmetric Form)，线性规划问题满足如下条件：一、决策变量均为非负数；约束条件为极大的时候均取"$\leq$"，当目标函数取极小的取"$\geq$"。对于其他形式的线性规划问题，可以先转化为对称形式，然后根据上述规则写出对偶问题。



| 原问题                                                                       |                              对偶问题                              |
| ---------------------------------------------------------------------------- | :----------------------------------------------------------------: |
| 约束条件系数矩阵                                                             |                       约束条件系数矩阵的转置                       |
| 约束条件右端项向量                                                           |                          目标函数系数向量                          |
| 目标函数系数向量                                                             |                         约束条件右端项向量                         |
| 目标函数：$\mathop{\max} \hspace{2pt} z = \sum \limits^{n}_{j = 1}{c_j x_j}$ | $\mathop{\min} \hspace{2pt} w = \sum \limits^{m}_{i = 1}{b_i y_i}$ |
| 约束条件数 $= m$                                                             |                         决策变量个数 $= n$                         |
| 第$i$个约束条件: $\sum^{n}_{j=1}{a_{ij} x_j} \leq b_i$                       |                   第$i$个决策变量：$y_i \geq 0$                    |
| 第$i$个约束条件: $\sum^{n}_{j=1}{a_{ij} x_j} \geq b_i$                       |                   第$i$个决策变量：$y_i \leq 0$                    |
| 第$i$个约束条件: $\sum^{n}_{j=1}{a_{ij} x_j} = b_i$                          |                   第$i$个决策变量：$y_i$ 无约束                    |
| 决策变量个数$=n$                                                             |                          约束条件数 $= m$                          |
| 第$j$个决策变量：$x_j \geq 0$                                                |        第$j$个约束条件$\sum^{n}_{j=1}{a_{ij} y_j} \geq c_i$        |
| 第$j$个决策变量：$x_j \leq 0$                                                |        第$j$个约束条件$\sum^{n}_{j=1}{a_{ij} y_j} \leq c_i$        |
| 第$j$个决策变量：$x_j$ 无约束                                                |         第$j$个约束条件$\sum^{n}_{j=1}{a_{ij} y_j} = c_i$          |


<div class = "centertable">
<table style = "margin: center">
    <tr>
        <td>目标函数</td> 
        <td>max</td> 
        <td>min</td> 
   </tr>
   <tr>
        <td>约束条件系数矩阵</td> 
        <td>A</td> 
        <td>AT</td> 
   </tr>
   <tr>
        <td>约束条件右端项向量</td> 
        <td>b</td> 
        <td>c</td> 
   </tr>
   <tr>
        <td>目标函数的系数向量</td> 
        <td>c</td> 
        <td>b</td> 
   </tr>
    <tr>
  		 <td rowspan = "4">函数约束与变量约束</td> 
      	 <td colspan="2">第k个约束 <----> 第k个向量</td>    
    </tr>
    <tr>
        <td colspan="2">约束个数 = 变量个数</td>    
    </tr>
    <tr>
        <td colspan="2">（非）规范约束 <----> 非负（正）变量</td>    
    </tr>
    <tr>
        <td colspan="2">等式约束 == 自由变量</td>    
    </tr>

</table>
</div>

> 上表中 `规范约束` 指的是前文`对称形式`下求解目标函数的性质和约束条件的大小约束对应关系，即：求解极大对应“$\leq$”，而求解极小对应“$\geq$”

### 2.1.2 对偶问题的矩阵表示

- 我们考虑标准形式：

$$\min c^T x$$

$$\text{s.t.} \left\{ \begin{aligned} Ax = b \\ x \geq 0 \\ \end{aligned} \right.$$

- 其对偶问题是：

$$\max b^T y$$

$$\text{s.t.} \left\{ \begin{aligned} A^Ty \leq c  \end{aligned} \right.$$

---------

- 同理，任何一种线性规划问题都可以写成标准形式并利用标准形式，写出对偶形式，比如我们考虑如下的问题。

$$\min d^T x$$

$$\text{s.t.} \left\{ \begin{aligned} Ax = b \\ x \geq 0 \\ \end{aligned} \right.$$


## 2.2 对偶理论

⏰：针对的是“对称形式”的对偶问题，因为所有非对称形式都可以转化为对称形式；

### 2.2.1 弱对偶定理

- 如果$x = (x_1, x_2, x_3,...x_n)^{T}$是原问题的可行解，$y = (y_1, y_2,...,y_m)^{T}$ 是对偶问题的可行解，那么 $c^{T}x \leq b^T y$

> 说人话版本：原问题最优解目标函数是对偶问题目标函数值下界，对偶问题最优问题目标函数值是原问题目标函数值上界。
#### 推论2.1 

- 如果原问题有可行解并且目标函数值无界，那么它的对偶问题无可行解；同理如果对偶问题有可行解并且目标函数无界，那么原问题无可行解。

### 2.2.2 最优性定理

- 如果$x = (x_1, x_2, x_3,...x_n)^{T}$是原问题的可行解，$y = (y_1, y_2,...,y_m)^{T}$ 是对偶问题的可行解，并且$c^{T}x = b^T y$，（两者的目标函数值是相等的），那么$x$是原问题的最优解，$y$是对偶问题的最优解；

### 2.2.3 对偶定理
- 在互为对偶的两个线性规划问题中，如果其中一个有最优解，那么另外一个也有最优解，并且两者最优目标函数相等

#### 推论2.2 
- 如果原问题有可行解而其对偶问题没有可行解，那么原问题目标函数值无界；同理如果对偶问题有可行解而原问题没有可行解，那么对偶问题目标函数值无界。


### 2.2.4 互补松弛性

- 如果$x = (x_1, x_2, x_3,...x_n)^{T}$是原问题的可行解，$y = (y_1, y_2,...,y_m)^{T}$ 是对偶问题的可行解，那么它们为各自问题的最优解的充要条件是：$y^{T}_s x = 0, x^{T}_s y = 0$
    - 松约束、紧约束
  
- 详细版本：（双最优解情况）若原问题中某一约束条件对应的对偶变量值为非0，那么该约束条件取严格等式，若约束条件取严格等式，那么对应的对偶变量一定为0.也就是
    - 若 $y_i > 0$，那么 $\sum \limits^{n}_{j = 1}{a_{ij} x_j} = b_i$，松弛变量为0
    - 若 $\sum \limits^{n}_{j = 1}{a_{ij} x_j} < b_i$，也就是松弛变量不为0，则$y_i = 0$
> 因为原问题的约束条件对应对偶的目标函数，原问题的松弛变量为0，意味着对应的一个约束条件取等号，也就意味着这个约束条件对应的对偶问题的一个决策变量不为0；如果原问题的松弛变量不为0，那么意味着这是一个松约束，所以对偶问题对应的决策变量就必须为0；
>

## 2.3 影子价格

- ==影子价格==：单位第$i$种资源在最优方案中做出的贡献，或者说是相应资源对目标总利润的边际贡献；
    - 是指依据一定原则确定的，能够反映投入物和产出物真实经济价值、反映市场供求状况、反映资源稀缺程度、使资源得到合理配置的价格。
- 影子价格依赖于**资源的利用情况**。

1. 影子价格的大小客观反映了资源在系统内的**稀缺程度**；
> 互补松弛型：如果生产过程中，资源$b_i$没有充分利用，那么影子价格为0，如果影子价格不为0意味着资源在生产中已经耗尽，也就是说这是一种稀缺资源。增加这种资源可以改善目标函数值，影子价格越高，反应资源在系统内越稀缺，增加该资源的供给对系统目标函数值的贡献越大。
1. 影子价格**实际上是一种机会成本**，检验数$\sigma_j = c_j - \sum \limits^{m}_{i = 1}{a_{ij} y_i}$ 反应的是利润 - 产品消耗的各项影子价格之和。只有利润大于机会成本，才会生产它有利。
2. 在出现退化的最优解的时候，会出现资源耗尽而不稀缺，但影子价格仍然大于0的情况，这时增加$b$只会带来资源的剩余，不增加利润。 

## 2.4 对偶单纯形法


> 单纯形法总体而言在：1. 先找到可行性；2. 再确定最优性；
> 对偶单纯形法相当于反了过来（或者==可以理解成，对这个LP的对偶问题，进行单纯形法求解==），先找对偶问题的可行解（也就是原问题的“最优”解），再寻找符合对偶问题最优性（也就是原问题可行解）的解；

- 我们知道在原问题里，最优性通过检验数$\sigma_j$衡量，可行性通过右端项 $b_i$ 衡量，而对偶单纯形法，首先满足原问题最优性，然后逐渐逼近可行性，所以在第一步的时候，<u>是允许右端项为负的。</u> 理解这个问题有助于我们理解后面的模型变化。
- 然后我们开始求解：

- （1） 列出初始单纯形表，要求$c_j - z_j$ 检验数小满足非正约束，也就是对偶问题为可行解，对$b_i$的值不做要求，
- （2）最优性判断$(B^{-1}b)_{i} < 0$；


- 确定出基变量：没有找到可行解，总存在 $b_i < 0$，选择$b_i$中最小的，对应的变量$x_r$ 就是出基变量；
- 确定入基变量，上一步确定了出基变量，为了确保下一表中出基变量$r$行基变量为正值，需要找对应$a_{rj} < 0 ( j = m + 1,...,n)$的**非基变量**
    > 单纯形法中找的是$a_{is} > 0$的出基；

  
$$\theta = \mathop{\min}  \{ \dfrac{c_j - z_j}{a_{rj} } | a_{rj} < 0 \} = \dfrac{c_s - z_s}{a_{rs} }$$

> 注意，对偶单纯形是先确定出基变量，再入基，而单纯形法正相反！
>
> 这里通过 $\theta$ 来保证每一次迭代后的$b_i$ 都是大于等于0的，就像是单纯形法中，利用$\theta$ 来保证每一次迭代后的检验数都是小于等于0的一样。



!!! Tips
    也就是无论怎么让基变量增大，都无法让$x_r$转换成非负，此时原问题一定找不到可行解，对偶问题目标函数值无界；
    $\theta$，通过这个$\theta$，保证每次迭代后都是$\leq 0$的。

- 由弱对偶性，对偶问题有可行解，那么原问题可能有可行解也可能无解；
    - 对新的基检查是否所有$b_i \geq 0$
    - 如果是，那么原问题有可行解，$CX = Y^{T}b$，原问题和对偶问题均取到最优解；
    - 如果不是，先检查一下$b_r$对应的所有的$a_{rj}$，如果满足对任意$a_{rj}$ 都有 $a_{rj} \geq 0$，那么线性规划问题没有可行解（因为$b$要从负数变成正，变号）；否则将选中变量当作入基变量，继续迭代；

- 继续迭代。直到满足条件或者终止。


### 例题

面对下面这个模型：


$$\min \hspace{4pt} 2x_1 + 3x_2 + 4x_3$$

$$\text{s.t.} \left\{ \begin{aligned} x_1 + 2x_2 + x_3  & \geq 3 \\  2x_1 + x_2 + 3x_3 &  \geq 4 \\ x_1, x_2, x_3 \geq 0  \end{aligned} \right.$$

- 习惯性地，可以把它转化成求最大值问题的标准形式：

$$\max \hspace{4pt} -2x_1 - 3x_2 - 4x_3 \textcolor{red}{+ 0 x_4 + 0x_5}$$

$$\text{s.t.} \left\{ \begin{aligned} x_1 + 2x_2 + x_3 - & x_4 & & = 3 \\  2x_1 + x_2 + 3x_3 & & - x_5 &  = 4 \\ x_1, x_2, x_3, x_4, x_5 \geq 0  \end{aligned} \right.$$

- 因为对偶单纯形法右端项$\textbf{b}$是可以为负的，所以我们统一把所有“ $\geq$ ”的约束两边全部乘 $- 1$ 变号成 “$\leq$” 。这样可以保证添加的虚拟变量都是松弛变量（系数为1，可以形成一个单位阵）。
- 按照上面的思路，我们的模型转化后格式就成了：

$$\max \hspace{4pt} -2x_1 - 3x_2 - 4x_3 \textcolor{red}{+ 0 x_4 + 0x_5}$$

$$\text{s.t.} \left\{ \begin{aligned} -x_1 - 2x_2 - x_3 + & x_4 & & = -3 \\  -2x_1 - x_2 - 3x_3 & & + x_5 &  = -4 \\ x_1, x_2, x_3, x_4, x_5 \geq 0  \end{aligned} \right.$$

- 和一般的单纯形不同，我们首先不看检验数，而是先看$\textbf{b}$那一列。首先找找这一列，所有小于 $0$ 的 $b$ 里面，哪个 $b$ 最小，算下来在下表中也就是 $x_5$ 对应的行$(-4 < -3)$。我们就锁定这一行。
- 紧接着，**我们只看这一行所有$<0$的系数**，<font color = "red">用这些系数下面对应的检验数$\sigma_i$ （也就是标蓝的数字）去除以这个系数，除下来数值最小的那个数字对应的变量就是我们要“入”的基。</font>比如图一里，$x_1, x_3$ 列满足要求，$x_1$ 列运算结果是$(-2) \div (-2) = 1$，$x_3$ 列结果是$(-4) \div (-3) = 4/3$。毫无疑问前者更小，所以我们也确定了选择$x_1$入基。



$$\def\arraystretch{1.5}
   \begin{array}{c|c|c|c|c|c|c|c}
   \hline
   \hline
   & & & -2 & -3 & -4 & 0 & 0  \cr \hline
   \textbf{c}_{\textbf{B}} & \textbf{x}_{\textbf{B}} & \textbf{b} & x_1 & x_2 & x_3 & x_4 & x_5 \cr \hline
   0 & x_4 & \textcolor{red}{-3} & -1 & -2 & -1 & 1 & 0  \cr \hline
   0 & x_5 & \textcolor{red}{-4}  & \textcolor{green}{[-2 ]} & 1 & \textcolor{green}{-3} & 0 & 1  \cr \hline
    &  &  & \textcolor{blue}{-2} & -3 & \textcolor{blue}{-4} & 0 & 0  \cr \hline
    \hline
\end{array}$$

- 上述一通操作最终的结果是确定了**换入的基和换出的基**（也就是$x_5$ 和 $x_1$。接下来运用单纯形法里的“换基”操作进行变换。你可以参考我的运筹学第一篇笔记。如果你熟悉修正单纯形法，你可以直接利用矩阵行变换完成这一操作。
- 变化后的单纯形表如下图所示。此时你发现 $\textbf{b}$ 仍然有负数。继续去重复第一次迭代的步骤（确认换入的基），然后进行换基操作。所有需要比较的元素我用相同颜色标记好了。我们发现$-4 \div (-5/2) = 8/5$，小于$-1 / (-1/2) = 2$。所以把$x_2$换入。

$$\def\arraystretch{1.5}
   \begin{array}{c|c|c|c|c|c|c|c}
   \hline
   \hline
   & & & -2 & -3 & -4 & 0 & 0  \cr \hline
   \textbf{c}_{\textbf{B}} & \textbf{x}_{\textbf{B}} & \textbf{b} & x_1 & x_2 & x_3 & x_4 & x_5 \cr \hline
   0 & x_4 & \textcolor{red}{-1} & 0 & \textcolor{green}{[-5/2]} & 1/2 & 1 & \textcolor{green}{-1/2}  \cr \hline
   -2 & x_1 & 2  & 1 & -1/2 & 3/2 & 0 & -1/2  \cr \hline
    &  &  & 0 & \textcolor{blue}{-4} & -1 & 0 & \textcolor{blue}{-1}  \cr \hline
    \hline
\end{array}$$

- 对上面的表换基后，新的表如下图所示。此时欣喜地发现，所有的$b$ 都是正的了，同时所有的检验数依然保持不为正。意味着我们当前状态的表，既满足了最优，又满足了可行性。这个表就是最终的结果。我们的最优解是$(\dfrac{11}{5}, \dfrac{2}{5}, 0)$。目标函数$\dfrac{28}{5}$ .

$$\def\arraystretch{1.5}
   \begin{array}{c|c|c|c|c|c|c|c}
   \hline
   \hline
   & & & -2 & -3 & -4 & 0 & 0  \cr \hline
   \textbf{c}_{\textbf{B}} & \textbf{x}_{\textbf{B}} & \textbf{b} & x_1 & x_2 & x_3 & x_4 & x_5 \cr \hline
   -3 & x_2 & 2/5 & 0  & 1 & -1/5 & -2/5 & 1/5  \cr \hline
   -2 & x_1 & 11/5  & 1 & 0 & 7/5 & -1/5 & -2/5  \cr \hline
    &  &  & 0 & 0 & -9/5 & -8/5 & -1/5  \cr \hline
    \hline
\end{array}$$


---------

## 什么时候使用对偶单纯形方法

一个比较经典的例子是，当对偶问题的基本可行解已经求好的时候。比如对某个线性规划问题，我们求得了最优基，希望求解同样的问题在不同的右端向量下的解。此时，原问题的最优基在新的 $\bold{b}$ 下可能是原始不可行的，不过，由于 $\bold{b}$ 的取值不影响检验数，这意味着我们即使换了一个 $\bold{b}$，解依然是对偶可行的。所以，与其从零开始，把右端项代入用单纯形法，不如直接把原最优解作为对偶单纯形开始迭代的最优基，从而计算。

> 来源: Bertsimas “Introduction to Linear Optimization” P156

