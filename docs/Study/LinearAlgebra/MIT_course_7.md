# 求解 $Ax = 0$, 主变量、特解

!!! abstract "大纲"
    1. $Ax=0$
    2. $Ux=0$
    3. $Rx=0$

这一章的内容开始讲怎么具体地求解$Ax = 0$ 这个问题了。这一块就开始涉及“算法”，具体说就是求解 $Ax = 0$ 的算法。上一章提到$Ax = 0$ 的解就是零空间，所以这一章实际上在解决零空间的求解过程。

## $Ax = 0$ 到 $Ux = 0$

给出$A = \begin{bmatrix} 1 & 2 &2 & 2 \\ 2 & 4 & 6 & 8 \\ 3 & 6 & 8 & 10 \end{bmatrix}$，求解 $Ax = 0$.

先对A进行消元，首先我们明确右端向量为0，所以不需要做任何计算。

$A = \begin{bmatrix} \colorbox{yellow}{1} & 2 & 2 & 4 \\ 0 & 0 & \colorbox{yellow}{2} & 4 \\ 0 & 0 & 0 & 0 \end{bmatrix}$，这个矩阵叫做“行梯形阵？”Lechelon matrix？，记作$U$。于是我们完成了 $Ax = 0$ 到 $Ux = 0$ 的转化。

!!! note "秩"
    这里注意到，我们已经发现了矩阵中最重要的数字：主元的数量。A 的主元数量 = 2，主元的数量也就等于：**矩阵的秩**。`rank` 。这些主元在的列向量就是主变量（pivot），而剩下的列向量就是自由变量（`free variables`），对应$A$ 的第二列和第四列。

    自由变量的意思是，你可以给它们对应的未知数赋予任意的数值，也就是说，把$(x_2, x_4)$ 给定后，你就可以求$x_1,x_3$ 了。如果对前面的知识熟悉，这就是“回代”的过程。

求得了自由变量后，分别给他们赋值，回代，求出所有未知数。可以发现解：$\begin{bmatrix} -2 \\ 1 \\ 0 \\ 0 \end{bmatrix}$ 和 $\begin{bmatrix} 2 \\ 0 \\ -2 \\ 1 \end{bmatrix}$。现在，我们找到了零空间两个线性无关的向量，我们可以通过这两个向量求出整个零空间了。我们回代后求出的两个向量，被称为“特解”（`special solutions`），可以通过特解的线性组合求出整个零空间。

所以零空间为 $c \begin{bmatrix} -2 \\ 1 \\ 0 \\ 0 \end{bmatrix} + d \begin{bmatrix} 2 \\ 0 \\ -2 \\ 1 \end{bmatrix}$

> 对秩的进一步解释：秩的数量，表明了“方程组中起作用的方程”的数量。“不起作用”的意思是这个方程可以被其他方程形成的约束取代。
>
> 一个 $m \times n$ 的矩阵，$n$个变量，秩为$r$, $(n - r)$ 自由变量，这表明有 $n - r$ 个变量可以自由选取。

## $Ux = 0$ 到 $Rx = 0$ 形式

我们对上面的行梯形矩阵再简化，把每一个主元位置的其余元素都消去。

$A = \begin{bmatrix} \colorbox{yellow}{1} & 2 & 2 & 4 \\ 0 & 0 & \colorbox{yellow}{2} & 4 \\ 0 & 0 & 0 & 0 \end{bmatrix} = \begin{bmatrix} \colorbox{yellow}{1} & 2 & \colorbox{yellow}{0} & -2 \\ \colorbox{yellow}{0} & 0 & \colorbox{yellow}{1} & 2 \\ 0 & 0& 0 & 0 \end{bmatrix}$，最终的这个矩阵称为“行简化梯形矩阵”，matlab中可以用 `rref(A)` 获得结果。

这个操作有几个作用：

1. 立刻看出来主元；
2. 发现了一个 $r \times r$ 的单位矩阵。（看主行和主列交汇处，上图高亮部分）
3. 全为0的行意味着，它是其他行的线性组合。

由于右端项是0，所以 $Ax = 0, Ux = 0, Rx = 0$ 的解是 相同的，我们把主元和自由变量分离开来看：$\begin{pmatrix} \text{sol}_1 & 1 & 0 & 2 & -2 \\ \text{sol}_2 &0 & 1 & 0 & 2 \end{pmatrix}$，只需要将自由变量取负，然后各个位置数字按照自由变量赋值位置，重新组合，我们实际上就已经求出了整个零空间。

你可以对照上面求出的解来看，注意那个 $x_1$ 对应的 $2$ 变成了$\text{sol}_1$ 的 $-2$，以此类推。“**自由列中数字的相反数显示在了结果里**”。

$\begin{pmatrix} \text{sol}_1 & \colorbox{lightblue}{1} & \colorbox{lightblue}{0} & \colorbox{lightgreen}{2} & \colorbox{lightgreen}{-2} \\ \text{sol}_2 & \colorbox{lightblue}{0}& \colorbox{lightblue}{1} & \colorbox{lightgreen}{0} & \colorbox{lightgreen}{2} \end{pmatrix}$， $c \begin{bmatrix} \colorbox{lightgreen}{-2} \\ \colorbox{lightblue}{1} \\ \colorbox{lightgreen}{0} \\ \colorbox{lightblue}{0} \end{bmatrix} + d \begin{bmatrix} \colorbox{lightgreen}{2} \\ \colorbox{lightblue}{0} \\ \colorbox{lightgreen}{-2} \\ \colorbox{lightblue}{1} \end{bmatrix}$

这个绿色的部分就是“零空间矩阵”（nullspace matrix），它的列数和特解的列数是相同的。

我们复盘一下具体计算过程。

$R = \begin{bmatrix} I & F \\ O & O \end{bmatrix}$，其中$I$ 是一个 $r\times r$ 的矩阵，$F$ 是一个 $r\times (n - r)$ 的矩阵。问题就变成：$RN = 0$，求$N$。

如果令$N = \begin{bmatrix} -F \\ I \end{bmatrix}$，上述是一定成立的。

这里你需要干的事情，只是“确定好自由向量，把1和0分配进去，然后把F矩阵填到主变量对应位置即可。注意上面式子中前后的两个$I$ 的维度是不一样的，$R$矩阵中的$I$维度是 $r \times r$，放到结果中是$(n - r) \times (n - r)$。

-----------

!!! example "另一个例子"
    我们求上面$A$矩阵转置的情况：

    $\begin{bmatrix} 1 & 2 & 3 \\ 0 & 0 & 0 \\ 0 & 2 & 2 \\ 0 & 4 & 4 \end{bmatrix} = \begin{bmatrix} 1 & 0 & \colorbox{yellow}{1} \\ 0 & 1 & \colorbox{yellow}{1} \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{bmatrix}$，最终的解是$x = c \begin{bmatrix} \colorbox{yellow}{-1} \\ \colorbox{yellow}{-1} \\ 1 \end{bmatrix}$ .

    注意，这里只有一个自由变量，不能给它赋值0，因为给了0，其他的都是0了，没意义，这种情况下统一赋值1. 

    （注意高亮部分矩阵直接加负号对应到主变量即可）

matlab 可以使用null(A)得到零空间矩阵。具体过程是用MatLab先得到R，然后找出主变量和自由变量，然后将1和0分配到自由变量中，然后使用回代求出pivot variables.