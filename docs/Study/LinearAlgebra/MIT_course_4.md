# 矩阵的LU分解


!!! abstract "框架"
    1. AB的逆的补充解释
    2. 转置矩阵的逆
    3. 消元和$LU$分解
    4. 消元法的操作次数
    5. 引入：转置和置换


## AB的逆的补充解释

Inverses of $AB$ : 已知$A$和$B$的逆，求$AB$的逆（保证逆存在）

$(AB)^{-1} = B^{-1} A^{-1}$ .代入$(AB)^{-1}(AB)$计算一下即可。

## 转置矩阵（transpose）的逆

考虑到$AA^{-1} = I$，我们对等式两边同时取转置：

$(AA^{-1})^{T} = I^{T} = (A^{-1})^{T}A^T = I$

看后一个等式，结果恰恰说明，$(A^T)^{-1} = (A^{-1})^T$

- 转置和逆对于同一个矩阵而言，其顺序可颠倒。

---------

## 消元和LU分解

在代数计算中，考虑行变换无疑是正确的：$E_nE_{n-1}..EA = U$，因为左乘一个初等矩阵等于对矩阵进行行变换。

LU分解就是把矩阵分解成一个下三角矩阵（Lower matrix）和上三角矩阵的乘积。e.g.

$\begin{bmatrix} 2 & 1 \\ 8 & 7 \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 4 & 1  \end{bmatrix} \begin{bmatrix} 2 & 1 \\ 0 & 3 \end{bmatrix}$

> 有时候会把 $\begin{bmatrix}  2 & 1 \\ 0 & 3  \end{bmatrix}$ 单独拆分成主元和另一个矩阵的乘积


!!! question "问题"
    为了方便思考我们先考虑$3 \times 3$ 的情况：将矩阵消元实际上就是进行：$E_{32}E_{31}E_{21}A = U$，当然这种情况是没有行交换（row exchange）的。此时我们想做$A = LU$的分解，需要把这些$E_{ab}^{-1}$ 直接乘右边，这样会得到：$A = E_{21}^{-1}E_{31}^{-1}E_{32}^{-1}U$ 。那么为什么这里不直接把$E_{ab}$ 保留，用不需要求逆的$EA = U$ 形式呢？


    我们可以先把三个初等矩阵分别算出来，这里假设三个矩阵分别为：

    $E_{21} = \begin{bmatrix} 1 & 0 & 0 \\ -2 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix} ，E_{31} = \begin{bmatrix} 1 & 0 &  0\\0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}, E_{32} = \begin{bmatrix} 1 & 0& 0 \\ 0 & 1 & 0 \\ 0 & -5 & 1 \end{bmatrix}$

    如果使用$EA = U$ 的形式，我们可以计算最终的$E = \begin{bmatrix} 1 & 0 & 0 \\ -2 & 1 & 0 \\ \colorbox{yellow}{10} & -5 & 1 \end{bmatrix}$

    这个矩阵上半部分一定全是0，因为U矩阵的上半部分完全没有改变；但是为什么左下有一个10：

    > 因为行变换的时候先有了 $r2 + r1 \times (-2)$，而在$r3$ 处又有 $r3 - 5\times r2$，所以实际上$r3$ 在减去$r2$的基础上上，利用了先前$r1$的操作，$r1$影响到了$r3$，在$r3$上加上了10倍的$r1$。

    而之所以化为$A = LU$，就是因为，如果我们用初等矩阵的逆做：

    $E_{21}^{-1}E_{31}^{-1}E_{32}^{-1} = \begin{bmatrix} 1 & 0 & 0 \\ 2 & 1 & 0 \\ 0 & 0 & 1  \end{bmatrix} \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}\begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 5 & 1 \end{bmatrix} = \begin{bmatrix} \colorbox{yellow}{1} & 0 & 0 \\ \colorbox{lightblue}{2} & \colorbox{yellow}{1}  & 0 \\ 0 & \colorbox{lightblue}{5} & \colorbox{yellow}{1} \end{bmatrix}$

    这个结果很好，因为按照顺序进行消元的乘数，对应消元去掉的元素的位置，保留在了矩阵$L$中。

    > 什么是对应去掉的元素的位置，就是你消去的是第二行第一列的元素，那么你的这个乘数也写在$L$矩阵的第二行第一列。

    什么是乘数，就是你消元时候，比如 $r2 - r1 \times 2$，**需要乘以并减去的那个数字**（这里就是$2$）就是乘数。

    > 当消元完毕，（比如得到消元后的第二行）的同时，也就获得了对应的 $L$ 的这一行。

--------------


## 消元法的操作次数


- 接下来我们需要解决一个新的问题：在刚刚的消元过程中，总共进行了多少次操作？

!!! note "备注"
    为什么要考虑这个，因为现实中需要消元的矩阵可能十分巨大，这样我们才能获得更加详细的数据和信息，数据巨大了我们就需要考虑其计算成本和计算时间，大到什么规模我们可以计算，什么情况下我们就不大好算了。（e.g. $n \times n$ 的矩阵，$n = 100? 1000? 10000$ 情况分别是什么样子的？

    - 这里我们规定，把一个数字乘以一个数，然后再用另一个数字减去刚刚的结果，这个过程叫做一次“操作”Operations。

我们假设 $n = 100$，从第一个元素开始对矩阵进行消元，可以看出当我们把第一列整理完毕成 $\begin{bmatrix} \cdots & \cdots & \cdots \\ 0 & \cdots & \cdots \\ \vdots & \vdots & \vdots \\ 0 & \cdots & \cdots \end{bmatrix}$ 这种形式后，进行了$100 \times 100$ 次操作（如果考虑上第一行），从第二列始，大概要 $99\times 99$ 次操作，以此类推，总操作次数大概是：$100^2 + 99 ^2 + \cdots + 3^2 + 2^2 + 1$，借助平方和公式 $\sum \limits^{i = 1}_{n} n^2 = \dfrac{n(n+1)(2n + 1)}{6}$，约等于 $\dfrac{1}{3} n^3$。这大概就是总的计算次数。

> 老师这里还讲了用微积分来推导这个$\dfrac{1}{3} n^3$的过程。

- 那么，对于右侧向量$b$，大概要多少次操作？$n^2$。可以理解为：第一列：100次，第二列：99次...相当于 $\dfrac{n(n + 1)}{2}$。


## 引入：转置(transpose)和置换(permutations)

置换矩阵的概念在[MIT系列第二章](./MIT_course_2.md)其实已经提到过了，简单说就是，矩阵左乘置换矩阵可以进行行变换。给定N的维度后，其可以进行的行变换是有限的，例如我们可以列出 $N = 3$ 时候的所有置换矩阵：

$\begin{bmatrix} 0 &1 &0 \\ 1 & 0 &  0  \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} 0 & 0 & 1 \\ 0 & 1 & 0 \\ 1 & 0 & 0  \end{bmatrix} \begin{bmatrix} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 1 & 0 \end{bmatrix}$

$\begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} 0 & 1 & 0 \\ 0 & 0  &1 \\ 1 & 0 & 0 \end{bmatrix} \begin{bmatrix} 0 & 0 & 1 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{bmatrix}$

- $3\times 3$ 总共有6个置换矩阵，这6个矩阵中任意两个相乘，结果也一定在这6个矩阵中；
- 如果对这6个矩阵中的任何一个取逆，其逆矩阵也在其中。
- 事实上，对于置换矩阵而言，**其逆等于其转置**。

> $n \times n$ 的矩阵，有 $n!$ 种不同的置换矩阵。