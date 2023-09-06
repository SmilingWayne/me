# 方程组的几何解释

!!! note "线性代数最基本的问题"
    **线性代数最基本的问题，就是求解线性方程组的问题。**

    - 线性方程组就是一个由线性等式构成的系统。一般而言，方程组的数量和未知数的数量是一样的，比如 $n$ 个线性方程，$n$ 个未知数。


- 列方向形式

针对二元方程组的求解引出相关概念：

## $2 \times 2$ 的情况


$$\begin{align}\begin{equation*}
\begin{cases}
2x -y = 0\\
-x + 2y = 3 
\end{cases}
\end{equation*}\end{align}$$

这里一行对应一个方程，两个方程对应到图形上就是两条线相交。这是row picture。

我们同样可以列成下面的列向量的形式：

$$\begin{align} x \begin{bmatrix} 2 \\ -1 \end{bmatrix} + y \begin{bmatrix} -1 \\ 2 \end{bmatrix} = \begin{bmatrix} 0 \\ 3 \end{bmatrix}  \end{align}$$

此时我们的任务就是找一个列向量 $\begin{bmatrix} 2 \\ -1 \end{bmatrix}$ 和列向量 $\begin{bmatrix} -1 \\ 2 \end{bmatrix}$的**线性组合（Linear Combination）**，满足上述等式。显而易见， $x = 1, y = 2$ 是满足需求的。

!!! note "拓展"
    如果我们不考虑等号右边，而是让x和y取任意实数，会怎么样？

    可以在平面直角坐标系中作出向量 $\begin{bmatrix} 2 \\ -1 \end{bmatrix}$ 和 $\begin{bmatrix} -1 \\ 2 \end{bmatrix}$，对这两个向量进行任意程度的放大和缩小，最终这个向量组**能覆盖整个二维平面。**

    思考：满足什么样的条件，我们就可以判断，一组列向量的线性组合可以填充满整个 $N$ 维平面？

    > 我们给出**代数解释**：我们把这组向量组合起来形成矩阵$A$，列出同维向量$x$ 和右端向量 $b$，$Ax = b$，这个方程是否对所有的右端项都是有解的？
    > 
    > - 关于这个代数解释的解释：“填满整个空间”意思就是在这个空间里任意取向量 $b$，总能找到一个向量 $x$ 使得这个向量组经过线性组合可以得到 $b$。

## $3 \times 3$ 的情况

考虑一个三元方程组：


$$\begin{align}\begin{equation*}
\begin{cases}
2x - y = 0 \\
-x + 2y - z = -1 \\
-3y + 4z = 4
\end{cases}
\end{equation*}\end{align}$$

此时对于方程组中的每一个方程，其解都对应三维空间的一个平面。三个平面交于同一点，也就是这个方程组的解 $(0,0,1)$；

写成向量线性组合的形式就是。


$$x \begin{bmatrix} 2 \\ -1 \\ 0 \end{bmatrix} + y \begin{bmatrix} -1 \\ 2 \\ -3 \end{bmatrix} + z \begin{bmatrix} 0 \\ -1 \\ 4 \end{bmatrix} = \begin{bmatrix} 0 \\ -1 \\ 4 \end{bmatrix}$$

和二维的情况一样，如果我们考虑不同的右侧向量，比如 $\begin{bmatrix}  1 \\ 1 \\ -3 \end{bmatrix}$ ， 此时解为 $( 1, 1, 0)$，依然是三个列向量的重新线性组合。


> ==划重点：向量的线性组合的概念==，解线性方程组实际上就是在“寻找一个合适的线性组合”。

--------

我们同样可以把上述内容写成矩阵形式(Matrix form):  $Ax = b$，其中$A = \begin{bmatrix} 2 & -1 & 0 \\ -1 & 2 & -1 \\ 0 & -3 & 4 \end{bmatrix}$，$x = \begin{bmatrix} x \\ y \\ z \end{bmatrix}$, $b = \begin{bmatrix} 0 \\-1 \\4 \end{bmatrix}$

!!! note "列的线性组合能否覆盖所有的三维空间呢？"
    如果可以，矩阵形式的$A$就称为为**非奇异矩阵**（Non-singular matrix）或者**可逆矩阵**（Invertible matrix）

    如果不可以，这意味着**三个列向量在同一个平面上**，所以无论怎么对三个列向量线性组合，他们的结果也一定在这个平面上，不可能覆盖所有三维空间。（e.g. column 3 = column 2 + column 1）

    --------

    进一步拓展，我们考虑更高维度的情况，比如$n = 9$的九维。

    $x_1\begin{bmatrix} a_{11} \\ a_{21} \\ \vdots \\ a_{91} \end{bmatrix} + x_2\begin{bmatrix} a_{12} \\ a_{22} \\ \vdots \\ a_{92} \end{bmatrix} + \cdots + x_9\begin{bmatrix} a_{19} \\ a_{29} \\ \vdots \\ a_{99} \end{bmatrix} = b$;

    这种情况，我们能否表示所有的$b$？

    <u>试想一下，如果一个列向量“没有贡献”，可以被剩下来8个列向量表示，那么这九个列向量就变成了“可以在九维空间展开的一个八维平面，此时那些不在这个八维平面的 $b$ 向量就没法被表示出来了。</u>


---------

## 矩阵形式 

如果考虑“矩阵*向量”的情况：

$Ax = \begin{bmatrix} 2 & 5 \\ 1 & 3 \end{bmatrix} \begin{bmatrix} 1 \\ 2 \end{bmatrix} = 1 \begin{bmatrix} 2 \\1  \end{bmatrix} + 2 \begin{bmatrix} 5 \\ 3 \end{bmatrix} = \begin{bmatrix} 12 \\ 7 \end{bmatrix}$

可以把 $Ax$ 视作A矩阵的线性组合，其系数对应 $x$ 每一列的各个元素。

> Ax is a combination of A columns. 

这里还有另一种计算方式，用传统的**点积**，（dots），也就是 $\begin {bmatrix} 2*1 + 5 * 2 \\ 1*1 + 3*2 \end{bmatrix}$，但在数据量变大的时候，这一种方法不太实用，所以倾向于使用前一种理解。


--------

如果考虑“向量*矩阵”的情况：

$\begin{bmatrix} 1 & 2  \end{bmatrix} \begin{bmatrix} 2 & 5 \\ 1 & 3 \end{bmatrix} = 1 * \begin{bmatrix} 2 * 5 \end{bmatrix} + 2 * \begin{bmatrix} 1 & 3 \end{bmatrix} = \begin{bmatrix} 4 & 11 \end{bmatrix}$

我们得到结论：

- 矩阵**右乘向量**，可以看作是在对矩阵的列向量进行线性组合，得到一个**列向量**；
- 矩阵**左乘向量**，可以看作是在对矩阵的行向量进行线性组合，得到一个**行向量**；