# 灵敏度分析


!!! note "灵敏度分析：对系统或事物因为周围条件变化显示出来的敏感程度的分析，也就是在部分参数发生变化时候，判断问题最优解有什么变化"

回顾单纯形法的几个Notations:


- $b$：右端项（资源上限）；
- $A$：构成单纯形表的 $m \times n$ 的系数矩阵；（ $Ax = b$ ），其各个元素由 $a_{ij}$ 表示。
- $c_j$ :价值系数，也就是目标函数的那个系数。价值系数的变化不影响增广矩阵的状态。


$$\mathop{\max}  z = \sum^{n}_{j = 1}{c_jx_j}$$

$$\text{s.t.} \sum^{n}_{j = 1}{a_{ij} }{x_j} = b_i , (i = 1,...m)$$

$$x_j \geq 0, (j = 1,...n)$$

## 价值系数的变化
> **变化一** ：变成了另外的数字要重新计算检验数；如果又出现检验数大于零了，要在此基础上继续迭代；
> 
> **变化二** ：没有确切数字，变成一个未知数$(1 + \lambda)$，直接求出检验数，然后检验检验数是否小于等于0；


- 例题：比如我们解一个单纯形表：结果如下。

$$\def\arraystretch{1.5}
   \begin{array}{c|c|c|c|c|c|c|c}
   \hline
   \hline
   & & & \textcolor{red}{2} & 2 & 0 & 0 & 0  \cr \hline
   \textbf{c}_{\textbf{B}} & \textbf{x}_{\textbf{B}} & \textbf{b} & x_1 & x_2 & x_3 & x_4 & x_5 \cr \hline
   0 & x_3 & 15/2 & 0  & 0 & 1 & 5/4 & -15/2  \cr \hline
   2 & x_1 & 7/2  & 1 & 0 & 0 & 1/4 & -1/2  \cr \hline
   2 & x_2 & 3/2  & 0 & 1 & 0 & -1/4 & 3/2  \cr \hline
    &  &  & 0 & 0 & 0 & 0 & -2  \cr \hline
    \hline
\end{array}$$


- 如果我们把红色系数变成1.5，用新系数代入单纯形法算检验数会发现： $x_4$ 对应的检验数变成正数了（见下图蓝色值）。
    - 如果检验数均满足条件：仍然是最优的
    - 如果检验数不满足：继续迭代。比如下图标绿色的$\dfrac{5}{4}$. 要按照单纯形法继续迭代。

> 在这个情况下，很明显这张表不是最优解了。所以以绿色框的 $x_4$ 作为入基变量。进行迭代。

$$\def\arraystretch{1.5}
   \begin{array}{c|c|c|c|c|c|c|c}
   \hline
   \hline
   & & & \textcolor{red}{1.5} & 2 & 0 & 0 & 0  \cr \hline
   \textbf{c}_{\textbf{B}} & \textbf{x}_{\textbf{B}} & \textbf{b} & x_1 & x_2 & x_3 & x_4 & x_5 \cr \hline
   0 & x_3 & 15/2 & 0  & 0 & 1 & \textcolor{green}{[5/4]} & -15/2  \cr \hline
   2 & x_1 & 7/2  & 1 & 0 & 0 & 1/4 & -1/2  \cr \hline
   2 & x_2 & 3/2  & 0 & 1 & 0 & -1/4 & 3/2  \cr \hline
    &  &  & 0 & 0 & 0 & \textcolor{blue}{1/8} & \textcolor{blue}{-9/4}  \cr \hline
    \hline
\end{array}$$

- 单纯形迭代的下一个结果如下表所示：

$$\def\arraystretch{1.5}
   \begin{array}{c|c|c|c|c|c|c|c}
   \hline
   \hline
   & & & \textcolor{red}{1.5} & 2 & 0 & 0 & 0  \cr \hline
   \textbf{c}_{\textbf{B}} & \textbf{x}_{\textbf{B}} & \textbf{b} & x_1 & x_2 & x_3 & x_4 & x_5 \cr \hline
   0 & x_4 & 6 & 0  & 0 & 4/5 & 1 & -6  \cr \hline
   1.5 & x_1 & 2  & 1 & 0 & -1/5 & 0 & 1  \cr \hline
   2 & x_2 & 3  & 0 & 1 & 1/5 & 0 & 0  \cr \hline
    &  &  & 0 & 0 & -1/10 & 0 & -3/2  \cr \hline
    \hline
\end{array}$$

- 所有检验数均满足条件。此时是新的最优解。


<!-- 
## 约束系数的变化

> **约束系数的变化$c_j$的变化只会影响到检验数$c_j - z_j$的值。这个可以直接反映在单纯形表中**


- 约束系数的变化，只需要在最终单纯形表中的约束矩阵中加入变化了的系数。
    - 只将变化的那几列的列向量单拎出来；左乘$B^{-1}$，$c$到相应的列上，修改单纯形表的那一列
    - 如果是基变量的约束系数，要先把修正过的表先变成**原来表的样子**（构造出一个000100），再检查检验数；

    - 这时候会出现下面的情况：
        1. 可行性和最优性都满足；（依然是最优的）
        2. 可行性不满足，但是最优性满足；（对偶单纯形法）
        3. 可行性满足，最优性不满足；（继续单纯形）
        4. 都不满足 ；（需要加入人工变量） -->

## 资源限制的变化

<!-- > 该部分增补于2024.04.22 因此例题的参数与上文稍有出入。 -->

通过模型：

$$\min  z = 2x_1 + x_2$$

$$\text{s.t.}\begin{aligned}\begin{equation*}
\begin{cases}
5x_2 \leq 15 \\ 
6x_1 + 2x_2 \leq 24 \\ 
x_1 + x_2 \leq 5
\end{cases}
\end{equation*}\end{aligned}$$

$$x_1, x_2 \geq 0$$

我们看下面这个初始单纯形表。原问题是最小化问题。最优解是： $(\dfrac{7}{2}, \dfrac{3}{2}, \dfrac{15}{2}, 0, 0)^T$

$$\def\arraystretch{1.5}
   \begin{array}{c|c|c|c|c|c|c|c}
   \hline
   \hline
   & & & 2 & 1 & 0 & 0 & 0  \cr \hline
   \textbf{c}_{\textbf{B}} & \textbf{x}_{\textbf{B}} & \textbf{b} & x_1 & x_2 & x_3 & x_4 & x_5 \cr \hline
   0 & x_3 & 15/2 & 0  & 0 & 1 & 5/4 & -15/2  \cr \hline
   2 & x_1 & 7/2  & 1 & 0 & 0 & 1/4 & -1/2  \cr \hline
   1 & x_2 & 3/2  & 0 & 1 & 0 & -1/4 & 3/2  \cr \hline
    &  &  & 0 & 0 & 0 & -1/4 & -1/2  \cr \hline
    \hline
\end{array}$$

现在我们把第二个约束的右端项改成32，也就是 $\mathbf{b} = \begin{bmatrix} 15 \\ 32 \\ 5 \end{bmatrix}$。这张单纯形表的右端项**也就需要重新计算**。

怎么算？我们知道新的右端项相比原来的变化是 $\Delta \mathbf{b}^ = \begin{bmatrix} 0 \\ 8 \\ 0 \end{bmatrix}$，

$\Delta \mathbf{b}^{'} = \mathbf{B}^{-1} \mathbf{b} = \begin{bmatrix} 1 & 5/4 & -15/2\\ 0 &1/4 &-1/2 \\ 0& -1/4&3/2  \end{bmatrix} \begin{bmatrix} 0\\ 8 \\ 0  \end{bmatrix} = \begin{bmatrix} 10 \\ 2 \\ -2 \end{bmatrix}$

新右端项 $\mathbf{b}^{'} = \mathbf{b} + \Delta \mathbf{b}^{'}$，可以算出新的右端项 $= \begin{bmatrix} 35/2 \\ 11/2 \\ -1/2 \end{bmatrix}$，构成新的单纯形表。

$$\def\arraystretch{1.5}
   \begin{array}{c|c|c|c|c|c|c|c}
   \hline
   \hline
   & & & 2 & 1 & 0 & 0 & 0  \cr \hline
   \textbf{c}_{\textbf{B}} & \textbf{x}_{\textbf{B}} & \textbf{b} & x_1 & x_2 & x_3 & x_4 & x_5 \cr \hline
   0 & x_3 & \textcolor{blue}{35/2} & 0  & 0 & 1 & 5/4 & -15/2  \cr \hline
   2 & x_1 & \textcolor{blue}{11/2}  & 1 & 0 & 0 & 1/4 & -1/2  \cr \hline
   1 & x_2 & \textcolor{red}{-1/2}  & 0 & 1 & 0 & \textcolor{green}{[-1/4]} & 3/2  \cr \hline
    &  &  & 0 & 0 & 0 & -1/4 & -1/2  \cr \hline
    \hline
\end{array}$$

我们发现，有个资源约束是**负的**。在这情况下，$x_2$ 就等于 $-1/2$ 了，为非可行解。此时需要使用**对偶单纯形法**。[参考链接](./Chapter2.md)。把表中绿色部分入基。

迭代一次后结果如下：

$$\def\arraystretch{1.5}
   \begin{array}{c|c|c|c|c|c|c|c}
   \hline
   \hline
   & & & 2 & 1 & 0 & 0 & 0  \cr \hline
   \textbf{c}_{\textbf{B}} & \textbf{x}_{\textbf{B}} & \textbf{b} & x_1 & x_2 & x_3 & x_4 & x_5 \cr \hline
   0 & x_3 & 15 & 0  & 5 & 1 & 0 & 0  \cr \hline
   2 & x_1 & 5  & 1 & 1 & 0 & 0 & 1  \cr \hline
   0 & x_4 & 2  & 0 & -4 & 0 & 1 & -6  \cr \hline
    &  &  & 0 & -1 & 0 & 0 & -2  \cr \hline
    \hline
\end{array}$$

检验数满足条件，说明找到了最优解 $(5, 0, 0, 0, 0)^T$


!!! question "思考题：如果资源限制在一个 $\lambda$ 中变化，判断如何最优解不会变化。"


## 新增一个变量的分析

同样考虑“资源限制变化”一节中的模型。但是新增决策变量 $x_3$，建模如下：

$$\min  z = 2x_1 + x_2 + 3x_3$$

$$\text{s.t.}\begin{aligned}\begin{equation*}
\begin{cases}
5x_2 + 3x_3 \leq 15 \\ 
6x_1 + 2x_2 + 4x_3 \leq 24 \\ 
x_1 + x_2 + 2x_3\leq 5
\end{cases}
\end{equation*}\end{aligned}$$

$$x_1, x_2, x_3 \geq 0$$

可以求出如下的单纯形表：

$$\def\arraystretch{1.5}
   \begin{array}{c|c|c|c|c|c|c|c|c}
   \hline
   \hline
   & & & 2 & 1 & 0 & 0 & 0 & 3  \cr \hline
   \textbf{c}_{\textbf{B}} & \textbf{x}_{\textbf{B}} & \textbf{b} & x_1 & x_2 & x_3 & x_4 & x_5 & x_6 \cr \hline
   0 & x_3 & 15/2 & 0  & 0 & 1 & 5/4 & -15/2  &  -7 \cr \hline
   2 & x_1 & 7/2  & 1 & 0 & 0 & 1/4 & -1/2   & 0\cr \hline
   1 & x_2 & 3/2  & 0 & 1 & 0 & -1/4 & 3/2  & [2] \cr \hline
    &  &  & 0 & 0 & 0 & -1/4 & -1/2  &  1 \cr \hline
    \hline
\end{array}$$

注意，这里实际上只是增加了一列，这一列，检验数可以直接通过 $\sigma_3^{'} = 3 - (0, 1/4, 1/2) \begin{bmatrix} 3\\4\\2 \end{bmatrix} = 1$ 求得。（目标函数系数 - 增加的虚拟变量的检验数  $\times$ 新增加一列的系数。而A矩阵新增的一列，通过虚拟向量构成的矩阵 $P = \begin{bmatrix} 1 &5/4 & -15/2 \\ 0 & 1/4 & -1/2\\ 0& -1/4& 3/2\end{bmatrix} \begin{bmatrix} 3 \\ 4  \\2 \end{bmatrix} = \begin{bmatrix} -7 \\ 0 \\ 2 \end{bmatrix}$ 得到。

这里可以发现加了一个新的列进来，检验数又不对了，所以只能再次单纯形迭代一下。新结果如下，发现满足最优解，为 $(\dfrac{7}{2}, 0, \dfrac{51}{4}, 0, 0, 0)^T$

$$\def\arraystretch{1.5}
   \begin{array}{c|c|c|c|c|c|c|c|c}
   \hline
   \hline
   & & & 2 & 1 & 0 & 0 & 0 & 3  \cr \hline
   \textbf{c}_{\textbf{B}} & \textbf{x}_{\textbf{B}} & \textbf{b} & x_1 & x_2 & x_3 & x_4 & x_5 & x_6 \cr \hline
   0 & x_3 & 51/4 & 0  & 7/2 & 1 & 3/8 & -9/4  &  0 \cr \hline
   2 & x_1 & 7/2  & 1 & 0 & 0 & 1/4 & -1/2   & 0\cr \hline
   3 & x_6 & 3/4  & 0 & 1/2 & 0 & -1/8 & 3/4  & 1 \cr \hline
    &  &  & 0 & -1/2 & 0 & -1/8 & -5/4  &  0 \cr \hline
    \hline
\end{array}$$

!!! note  新增了一个产品，此时产生了新的价值系数（直接在最终单纯形表上修改）、约束系数变化用价值系数左乘$B^{-1}$，形成新的列，加入单纯形表中，检验是否满足检验数；如果不满足，要继续迭代。


## 新增一个约束条件的分析

- 增加一个约束条件在实际问题中相当于增添一道工序。分析的方法是先将原问题最优解的变量值代入新增的约束条件，如满足，说明新增约束未起到限制作用，原最优解
不变。否则，将新增的约束直接反映到最终单纯形表中再进一步分析。
- 例题：先看单纯形表：

$$\def\arraystretch{1.5}
   \begin{array}{c|c|c|c|c|c|c|c}
   \hline
   \hline
   & & & 2 & 1 & 0 & 0 & 0  \cr \hline
   \textbf{c}_{\textbf{B}} & \textbf{x}_{\textbf{B}} & \textbf{b} & x_1 & x_2 & x_3 & x_4 & x_5 \cr \hline
   0 & x_3 & 15/2 & 0  & 0 & 1 & 5/4 & -15/2  \cr \hline
   2 & x_1 & 7/2  & 1 & 0 & 0 & 1/4 & -1/2  \cr \hline
   1 & x_2 & 3/2  & 0 & 1 & 0 & -1/4 & 3/2  \cr \hline
    &  &  & 0 & 0 & 0 & -1/4 & -1/2  \cr \hline
    \hline
\end{array}$$

- 增加一个约束条件 $3x_1 + 2x_2 \leq 12$。由于原来只有3个剩余变量，必须补一个变量 $x_6$ 才能凑全单位矩阵（原来是$3 \times 3$， 现在必须变成 $4 \times 4$）。此时把表扩充。

$$\def\arraystretch{1.5}
   \begin{array}{c|c|c|c|c|c|c|c|c}
   \hline
   \hline
   & & & 2 & 1 & 0 & 0 & 0 & \textcolor{blue}{0} \cr \hline
   \textbf{c}_{\textbf{B}} & \textbf{x}_{\textbf{B}} & \textbf{b} & \textcolor{red}{x_1} & \textcolor{red}{x_2} & \textcolor{red}{x_3} & x_4 & x_5 & \textcolor{blue}{x_6}\cr \hline
   0 & x_3 & 15/2 & 0  & 0 & 1 & 5/4 & -15/2 & \textcolor{blue}{0} & (1)   \cr \hline
   2 & x_1 & 7/2  & 1 & 0 & 0 & 1/4 & -1/2 & \textcolor{blue}{0} & (2) \cr \hline
   1 & x_2 & 3/2  & 0 & 1 & 0 & -1/4 & 3/2 & \textcolor{blue}{0} & (3)\cr \hline
   \textcolor{blue}{0} & \textcolor{blue}{x_6} & \textcolor{blue}{12}  & \textcolor{blue}{3} & \textcolor{blue}{2} & \textcolor{blue}{0} & \textcolor{blue}{0} & \textcolor{blue}{0} & \textcolor{blue}{1} & (4)\cr \hline
    &  &  & 0 & 0 & 0 & -1/4 & -1/2 & 0 \cr \hline
    \hline
\end{array}$$

- 注意到当加入（4）这一行之后，原来三个单位向量$x_1, x_2, x_3$ 都不是单位向量了，需要先整理表（进行初等行变换），直到出现四个单位向量为止。


$$\def\arraystretch{1.5}
   \begin{array}{c|c|c|c|c|c|c|c|c}
   \hline
   \hline
   & & & 2 & 1 & 0 & 0 & 0 & 0 \cr \hline
   \textbf{c}_{\textbf{B}} & \textbf{x}_{\textbf{B}} & \textbf{b} & x_1 & x_2 & x_3 & x_4 & x_5 & x_6\cr \hline
   0 & x_3 & 15/2 & 0  & 0 & 1 & 5/4 & -15/2 & 0 & (1)   \cr \hline
   2 & x_1 & 7/2  & 1 & 0 & 0 & 1/4 & -1/2 & 0 & (2) \cr \hline
   1 & x_2 & 3/2  & 0 & 1 & 0 & -1/4 & 3/2 & 0 & (3)\cr \hline
   0 & x_6 & \textcolor{red}{-3/2}  & 0 & 0 & 0 & -1/4 & \textcolor{green}{[-3/2]} & 1 & (4)\cr \hline
    &  &  & 0 & 0 & 0 & -1/4 & -1/2 & 0 \cr \hline
    \hline
\end{array}$$


- 注意到这个表的对偶问题是可行解（检验数均为非正的），但是原问题不是可行的（$b$ 有负数）。此时需要用**对偶单纯形法**进行迭代计算。具体步骤可以参考[对偶单纯形法的求解](./Chapter2.md)。按照出入基操作，我们需要选定$x_5$。进行换基操作：完成表如下。

$$\def\arraystretch{1.5}
   \begin{array}{c|c|c|c|c|c|c|c|c}
   \hline
   \hline
   & & & 2 & 1 & 0 & 0 & 0 & 0 \cr \hline
   \textbf{c}_{\textbf{B}} & \textbf{x}_{\textbf{B}} & \textbf{b} & x_1 & x_2 & x_3 & x_4 & x_5 & x_6\cr \hline
   0 & x_3 & 15/2 & 0  & 0 & 1 & 5/4 & -15/2 & 0 & (1)   \cr \hline
   2 & x_1 & 7/2  & 1 & 0 & 0 & 1/4 & -1/2 & 0 & (2) \cr \hline
   1 & x_2 & 3/2  & 0 & 1 & 0 & -1/4 & 3/2 & 0 & (3)\cr \hline
   0 & x_6 & -3/2  & 0 & 0 & 0 & -1/4 & [-3/2] & 1 & (4)\cr \hline
    &  &  & 0 & 0 & 0 & -1/4 & -1/2 & 0 \cr \hline
    \hline
\end{array}$$

- 对偶单纯形解完之后的结果就是加入约束条件后的最优解。


- 灵敏度分析一词的含义是指对系统或事物因周围条件变化显示出来的敏感程度的分析。


