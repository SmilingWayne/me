# 矩阵乘法和逆矩阵

!!! abstract "大纲"
    1. 矩阵乘法的五个视角
       1. 标准形式
       2. 列视角
       3. 行视角
       4. 列 $\times$ 行的视角
       5. 分块相乘的视角
    2. 逆矩阵的计算
    3. Gauss-Jorden Idea



## 矩阵乘法的五个视角


### 标准形式

$\begin{bmatrix} \cdots & \cdots & \cdots  \\ a_{31} & \cdots & a_{3n} \\ \cdots & \cdots & \cdots \end{bmatrix} \begin{bmatrix} \vdots & b_{41} & \vdots  \\ \vdots & b_{42} & \vdots \\ \vdots & b_{4m} & \vdots  \\ \\ \end{bmatrix}$ 

$c_{ij} = A$ 的第 $i$ 行 $\times B$ 的第 $j$ 列，或者说，$AB = C, A_{m\times n} B_{n \times p} = C_{mp}$


### 从整列的角度


$AB = \begin{bmatrix} 1 & 2 & 3 \\ 4  & 5 & 6 \end{bmatrix} \begin{bmatrix} 7 & 13 & 4 \\ 8 & 9 & 8 \\ 9 & 2 & 4 \end{bmatrix}$， 其结果的第 $p$ 列将是 $A$ 的各列的线性组合，其系数对应$B$矩阵的第 $p$ 列：（以结果矩阵第一列为例）$7 \begin{bmatrix} 1 \\ 4 \end{bmatrix} + 8 \begin{bmatrix} 2 \\ 5 \end{bmatrix} + 9 \begin{bmatrix} 3 \\ 6 \end{bmatrix} = \begin{bmatrix} 50 \\ 122 \end{bmatrix}$。

换一种说法是，将 $B$ 考虑成 $p$ 个单独的列向量，用 $A$ 依次乘每个列向量，将列向量排列成结果 $C$ ，$C$的各列是 $A$ 的所有列的线性组合。（Columns of C  are combination of columns of A）


### 从整行的角度

类似上面的，$AB = \begin{bmatrix} 1 & 2 & 3 \\ 4  & 5 & 6 \end{bmatrix} \begin{bmatrix} 7 & 13 & 4 \\ 8 & 9 & 8 \\ 9 & 2 & 4 \end{bmatrix}$ 其结果的第$p$行将是 $B$ 的各行的线性组合，其系数对应$A$矩阵的第$p$行。以结果矩阵的第一行为例：$1 \begin{bmatrix} 7 & 13 & 4 \end{bmatrix} + 2 \begin{bmatrix} 8 & 9 & 8 \end{bmatrix} + 3 \begin{bmatrix} 9 & 2 & 4 \end{bmatrix} = \begin{bmatrix} 50 & 37 & 32 \end{bmatrix}$

> 换一种说法是，将 $A$ 考虑成 $p$ 个单独的行向量，用 $B$ 和行向量对应相乘，得到的行向量排列成结果 $C$ ，$C$的各行是 $B$ 的所有行的线性组合。（Rows of C  are combination of rows of B）

### 从列 乘 行的角度

$AB$ 矩阵乘积，等于$A$的列向量对应 $\times$ B 的行向量的结果的和。$AB$  = Sum of (Cols of $A$) $\times$ (Rows of $B$)

$\begin{bmatrix} 2 \\ 3 \\ 4 \end{bmatrix} \begin{bmatrix} 1 & 6 \end{bmatrix} = \begin{bmatrix} 2 & 12 \\ 3 & 18 \\ 4 & 24 \end{bmatrix}; \hspace{5pt} \begin{bmatrix} 2 & 7 \\ 3 & 8 \\ 4 & 9\end{bmatrix} \begin{bmatrix} 1 & 6 \\ 2 & 3 \end{bmatrix} = \begin{bmatrix} 2 \\ 3  \\ 4  \end{bmatrix}  \begin{bmatrix} 1 & 6 \end{bmatrix} + \begin{bmatrix} 7 \\ 8 \\ 9 \end{bmatrix} \begin{bmatrix} 2 & 3 \end{bmatrix}$

> 注意 $A$ 的第 $k$ 列对应 $B$ 的第 $k$ 行，这样乘起来才对。

注意上面这个计算的例子

$\begin{bmatrix} 2 \\ 3 \\ 4 \end{bmatrix} \begin{bmatrix} 1 & 6 \end{bmatrix} = \begin{bmatrix} 2 & 12 \\ 3 & 18 \\ 4 & 24 \end{bmatrix}$，看出所有的行向量，都在直线 $\begin{bmatrix} 1 & 6 \end{bmatrix}$ 上，所以行空间是向量 $\begin{bmatrix} 1 & 6 \end{bmatrix}$ 上的直线。同理，其列向量也在 $\begin{bmatrix} 2 \\ 3\\ 4 \end{bmatrix}$ 直线上。


### 分块矩阵相乘的角度

> Block Multiplication

$\begin{bmatrix} A_1 & A_2 \\ A_3 & A_4 \end{bmatrix} \begin{bmatrix} B_1 & B_2 \\ B_3 & B_4 \end{bmatrix} = \begin{bmatrix} C_1 & C_2 \\ C_3 & C_4 \end{bmatrix}$，其中求 $\begin{bmatrix} C_1 \end{bmatrix}$ 这一块的表达式：$A_1B_1+ A_2B_3$：将矩阵切割成块，然后对块进行乘法。


------------


## 逆矩阵


### 存在的判定

逆矩阵，方阵的逆：Square Inverses. 并不是所有的矩阵都有逆矩阵。如果一个矩阵$A$的逆存在，我们有：$A^{-1}A = AA^{-1} = I$，也就是，对于可逆矩阵，$A$的左逆等于右逆。

> Invertible = non-Singular，也就是可逆 = 非奇异。

对于不可逆的情况：$\begin{bmatrix} 1 & 3 \\ 2 & 6 \end{bmatrix}$，分析如下：

!!! note "分析矩阵不可逆的情况"
    1. 你可以算他的行列式：=0
    2. 假设存在一个矩阵 $A^{-1}$ 满足 $A^{-1}A = I$，那么必须通过行变换得出 $\begin{bmatrix} 1 & 0 \end{bmatrix}$ （或者列变换得出 $\begin{bmatrix} 1 \\ 0 \end{bmatrix}$），但是这在变换中显然是不可能的。这个解释的本质需要回归到：这个矩阵的两列都在同一个直线上  / 两行也在同一个直线上，而 $\begin{bmatrix} 1 & 0 \end{bmatrix}$ 方向不在这个直线上。
    3. ==这也是最重要的一个解释==。 如果对于一个矩阵而言，我们可以找到一个非零向量$x$，满足$Ax = 0$，那么这个矩阵就是奇异的，非可逆的。
       > if I Can find a vector $x$ with $Ax = 0$, then the matrix has no inverties.
       > 
       > - 如果其中一列，对线性组合毫无贡献，那么矩阵不可能有逆；
       > - 上面这句话反过来说就是，==奇异矩阵可以通过列的线性组合形成零向量==。 从行的视角看，就是奇异矩阵可以通过行的线性组合形成零向量（some of the row(s) is dependent on others）。
       > 
       > 上面这个证明也很好证：左右两边乘$A^{-1}$ 会得到 $x = 0$，和条件矛盾。

### 如何计算逆矩阵

$\begin{bmatrix} 1 & 3 \\ 2 & 7 \end{bmatrix} \begin{bmatrix} a & b \\ c& d \end{bmatrix} = I \Rightarrow \begin{bmatrix} 1 & 3 \\ 2 & 7 \end{bmatrix} \begin{bmatrix} a \\ c \end{bmatrix}  = \begin{bmatrix} 1 \\0 \end{bmatrix} \text{and}  \begin{bmatrix} 1 & 3 \\ 2 & 7 \end{bmatrix} \begin{bmatrix} b \\ d \end{bmatrix} = \begin{bmatrix} 0 \\1 \end{bmatrix}$

又回到解线性方程组的问题了。这里就需要用到 **“Gauss-Jordan Ideas”**，相比Gauss elimination，在上三角矩阵的基础上继续消元，直到把左边的矩阵变成单位阵$I$，最后直接得到$A$的逆（也就是虚线右边的矩阵）。这样可同时处理两个方程组。

$\left[
	\begin{array}{cc|cc}
		1 & 3 & 1 & 0 \\
		2 & 7 & 0 & 1   
	\end{array}
\right] = \left[
	\begin{array}{cc|cc}
		1 & 3 & 1 & 0 \\
		0 & 1 & -2 & 1   
	\end{array}
\right] = \left[
	\begin{array}{cc|cc}
		1 & 0 & 7 & -3 \\
		0 & 1 & -2 & 1   
	\end{array}
\right]$

!!! note "那么为什么这么做是对的？"
    记得之前的“初等矩阵”的概念，左乘一些初等矩阵，相当于对矩阵进行行变换。我们复原上述计算为：

    $E\left[
        \begin{array}{c|c}
            A & I
        \end{array}
    \right] = \left[
	\begin{array}{c|c}
            EA & E
        \end{array}
    \right]$，考虑到最终$EA = I$，所以$E = A^{-1}$，也就是，增广矩阵右边这个$E$，就是要求的的逆矩阵。

    "That's why Gauss-Jordan Idea works!"
    


