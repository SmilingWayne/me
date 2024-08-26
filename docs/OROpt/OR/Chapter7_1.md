# 最小费用流 

最小费用流问题（Minimal Cost Flow Problem）在网络最优化问题中占有核心地位。可以表述如下：

> 对每个节点 $v_i$ 均给定实数 $b_i$， 如果 $b_i > 0$，那么称 $b_i$ 为发点，可以供给资源，$b_i$ 的值为该点的供给量。如果 $b_i < 0$，那么称 $b_i$ 为收点，需要接收资源 $-b_i$ 为该点的需求量。若  $b_i = 0$，那么称 $b_i$ 为转运点。
>
> 对于每条边 $e_j$，给定实数 $e_j$，它是在边 $e_j$ 上每单位流量的费用，称为费用系数。再给定正数 $u_j$，它是边 $e_j$ 上流量的上界。


最小费用流的问题就是要确定每个边上的流量 $x_j$，使得不超过上界限制，并满足各个节点的供需要求，同时又使得总费用最小。对于网络，我们引入一个 $m \times n$ 的矩阵 $A$。其中每个元素按照如下标准取值：

$$\begin{aligned}\begin{equation*}
a_{ij} = \begin{cases}
1, \hspace{10pt} \text{if } v_i \quad \text{starts from} \quad e_j \\
-1, \hspace{10pt} \text{if } v_i \quad \text{ends at} \quad e_j \\
0, \hspace{10pt} \text{Otherwise}
\end{cases}
\end{equation*}\end{aligned}$$

写成矩阵形式，如下：

$$\begin{bmatrix} 1 & 1 & 0 & 0 & 0 & 1 & 1 & 0 \\ -1 & 0 & 1 & 1 & 0 &  0 & 0 & 0 \\  0 & -1 & -1 & 0 & 1 & 0 & -1 & 0 \\ 0 & 0 & 0 & -1 & -1 & 0 & 0 & -1 \\ 0 & 0 & 0 & 0 & 0 & -1 & 1 & 1 \end{bmatrix}$$

即可表示如图【待补充】的网络。

在前面介绍最短路问题的时候，我们也出现了这个矩阵，一般称之为节点-边关联矩阵（Node-edge incidence matrix）。

于是，我们给出最小费用流的数学模型：

$$\min \mathbf{cx}$$

$$\begin{aligned}
\begin{cases}
\begin{align}
\mathbf{Ax} = \mathbf{b} \quad\\
\mathbf{0} \leq \mathbf{x} \leq \mathbf{u} \quad
\end{align}
\end{cases}
\end{aligned}$$

对于约束 (1) 中的每一个约束，可以表示为：

$$\sum \limits_{j \in E} a_{ij} x_j = b_i , \forall i \in V$$

实际上，左边就是：

$$\sum \limits_{j \in E} a_{ij} x_j = \sum \limits_{a_{ij} = 1} x_{j} - \sum \limits_{a_{ij} = -1} x_j  , \forall i \in V$$

>（因为如果 $a_{ij} = 0$，就不会出现 $x_j$ ）。

等式右边的第一个和式，对应的是所有从 $v_j$ 离开的流量；第二个和式，对应所有汇入 $v_j$ 的流量。 （这里是出度-入度！最短路那里是入度 - 出度，所以正好相反！）