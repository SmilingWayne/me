# 整数变量建模/线性化的一些小技巧

## 0-1变量的三种问题结构

$x_i$ 表示 方案 $j$ 是否在所有方案的集合 $M$ 中。

- Set-Covering Problem (SCP)

$$\min \sum_{j \in M} c_j x_j$$

subject to:

$$Ax \geq e$$

- Set Packing Problem (SPK)

$$\max \sum_{j \in M} c_j x_j$$

subject to:

$$Ax \leq e$$

- Set Partitioning Problem (SPP) 

$$\max / \min \sum_{j \in M} c_j x_j$$

subject to:

$$Ax = e$$

## 析取约束

有非负向量 $x$，是决策变量；

我们有两个约束 $ax \geq b$ 和 $cx \geq d$，此处保证 $a, c$ 均为非负的。

现在我们想表达：**上述两个约束，至少有一个是满足的。**

此时，引入一个新的变量 $y$，$y \in \{0, 1\}$，将原来的约束表示为：

$$ax \geq yb, \quad \quad cx \geq (1-y)d$$

不失一般性地，如果我们有 $m$ 个约束： $a_i x \geq b_i, a_i \geq 0, i = 1, 2, .., m$，我们想要表达：**这 $m$ 个约束至少有 $k$ 个约束被满足**，则可以建模成：

$$\sum^m_{i = 1} y_i \geq k, \quad \quad a_i x \geq b_i y_i, \quad  y_i \in \{0, 1\}, \forall i \in \{1,2,...,m \}$$

## 0-1变量的乘积式


比如，我们有如下的情况：

$$y = x_1 * x_2, x_1, x_2 \in \{0,1 \}$$

如何表示y呢？

你可以这样表示：

$$\begin{align}
\begin{cases}
y \leq x_1, \\ 
y \leq x_2, \\
y \geq x_1 + x_2 - 1 \\
y \in \{ 0, 1\}
\end{cases}
\end{align}$$

怎么检查正确性呢？你可以把所有 $x_1, x_2$ 的情况展示出来，会发现 $y$ 每次都能准确地表示成你想要的数字。

----

如果我们问题更加复杂一点：

$$y = x_1 * x_2, x_1 \in \{0,1 \}, x_2 \in [0, u]$$

方法其实是一样的。因为有一个 0-1 变量，所以实际上一旦 $x_1 = 0$，那么 $y$ 其实一直是 $0$，我们的重点就是 $y$ 和 $x_2$ 的关系。

$$\begin{align}
\begin{cases}
y \leq u x_1, \\ 
y \leq x_2, \\
y \geq x_2 - u(1 - x_1) \\
y \in [0, u]
\end{cases}
\end{align}$$

我们可以总结这个trick为更加一般的情况：

$$y = x_1 * x_2, x_1 \in \{0,1 \}, x_2 \in [l, u]$$

$$\begin{align}
\begin{cases}
y \leq x_2, \\ 
y \geq x_2 - u(1 - x_1) \\
ux_1 \geq y \leq ux_1
\end{cases}
\end{align}$$


-----

## max min / min max 问题

这个很浅显易懂了：比如我们想要：$\min \{ \max x_i \}$。那么：

$$\min z$$ 

$$z \geq x_i, \forall  i \qquad$$

同样地可以对 $\max \{ \min x_i \}$ 问题进行类似的操作。

$$\max z$$ 

$$z \leq x_i, \forall  i \qquad$$

## 分段线性成本函数

一般而言，我们用分段线性成本函数的场景是这样的：

我们有一个成本函数 $f(x)$ 是非线性的，我们打算在这个函数图像上取一系列的点，依次相连组成一个个相连的线段。假设我们取了 k 个点，分别用有序数对 $(a_i, f(a_i)), i = 1,...,k$ 表示。我们希望给定一个点 x，表示分段线性函数上这个点的因变量的值。

此时，我们引入一个0-1变量 $y_i$，用来表示点 $x$ 是否满足 $a_i \leq x \leq a_{i + 1}$.

我们同时引入辅助连续变量 $\lambda_i$，利用凸组合 $\sum \limits^k_{i = 1} \lambda_i f(a_i)$ 来表达要求的线性化后，位于 x 点的函数值。

因为所有的 $y_i$ 只有一个是为1的，其他均为0，所以，我们一定只能留出两个非 0 的 $\lambda_i$，这两个辅助变量对应着包含 $x$ 的间隔的两个点。

$$\min \sum^k_{i = 1} \lambda_i f(a_i)$$

subject to:

$$\begin{aligned}
\begin{cases}
\begin{align}
\lambda_1 \leq y_1 \quad \\
\lambda)k \leq y_{k-1} \quad \\
\sum^k_{i = 1} \lambda_i = 1 \quad \\
\sum^{k-1}_{i=1} y_i = 1 \quad \\
\lambda_i \geq 0 \quad (i = 1,...,k) \quad \\
y_i \in \{0, 1\} \quad (i = 1,...,k - 1) \quad \\
\end{align}
\end{cases}
\end{aligned}$$


-----

