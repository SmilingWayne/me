# 最小费用流 

最小费用流问题（Minimal Cost Flow Problem）在网络最优化问题中占有核心地位。可以表述如下：

> 对每个节点 $v_i$ 均给定实数 $b_i$， 如果 $b_i > 0$，那么称 $b_i$ 为发点，可以供给资源，$b_i$ 的值为该点的供给量。如果 $b_i < 0$，那么称 $b_i$ 为收点，需要接收资源 $-b_i$ 为该点的需求量。若  $b_i = 0$，那么称 $b_i$ 为转运点。
>
> 对于每条边 $e_j$，给定实数 $e_j$，它是在边 $e_j$ 上每单位流量的费用，称为费用系数。再给定正数 $u_j$，它是边 $e_j$ 上流量的上界。


最小费用流的问题就是要确定每个边上的流量 $x_j$，使得不超过上界限制，并满足各个节点的供需要求，同时又使得总费用最小。对于网络，我们引入一个 $m \times n$ 的矩阵 $A$。其中每个元素按照如下标准取值：

$$\begin{aligned}\begin{equation*}
a_{ij} = \begin{cases}
1, \hspace{10pt} \text{if } e_j \quad \text{starts from} \quad v_i \\
-1, \hspace{10pt} \text{if } e_j \quad \text{ends at} \quad v_i \\
0, \hspace{10pt} \text{Otherwise}
\end{cases}
\end{equation*}\end{aligned}$$

写成矩阵形式，如下：

$$\begin{bmatrix} 1 & 1 & 0 & 0 & 0 & 1 & 0 & 0 \\ -1 & 0 & 1 & 1 & 0 &  0 & 0 & 0 \\  0 & -1 & -1 & 0 & 1 & 0 & -1 & 0 \\ 0 & 0 & 0 & -1 & -1 & 0 & 0 & -1 \\ 0 & 0 & 0 & 0 & 0 & -1 & 1 & 1 \end{bmatrix}$$

即可表示如图【待补充】的网络。

在前面介绍最短路问题的时候，我们也出现了这个矩阵，**一般称之为节点-边关联矩阵（Node-edge incidence matrix）。** 

!!! note "节点-边关系矩阵"
    $m \times n$ 的矩阵，行表示节点，列表示边。

    对每一列而言，有且仅有一个1和一个-1，1表示从该节点出发，-1表示到该节点。0表示与该节点无关。

    对每一行而言，可能有多个1和多个-1，因为一个节点可能有多条边出发/到达，1的个数，表示从该节点出发的边数（出度）；-1的个数，表示到达该节点的边数（入度）。



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

等式右边的第一个和式，对应的是所有从 $v_j$ 离开的流量；第二个和式，对应所有汇入 $v_j$ 的流量。 

不失一般性，我们可以假设供求总是平衡的，也就是 $\sum_{i \in V} b_i = 0$，对于供大于求的图 ($\sum_{i \in V} b_i > 0$)，可以设置一个虚拟节点，吸收全部的过剩供给量，从每个发点添加一个虚拟边到这个虚拟节点，这个虚拟边的费用是0。这样就转化为一个供求平衡的最小费用流问题。

最小费用流问题是网络流问题的**重要基础**，事实上，许多问题均可以被转化为这类问题，或者是最小费用流问题的一个特例。下面展开几个例子。

---


## 从最小费用流到运输问题

运输问题，具体的问题描述同样可以参考[第三章](./Chapter3.md)。这里简要复习一下。

!!! note "运输问题"
    所有节点分为供给节点和需求节点两类。各个供给节点之间没有边相连，各个需求节点之间也没有边相连，但是供给和需求节点之间可以相互抵达。以图论的概念表示，网络图就是一个Bipartite Graph。

    - 问题:我们需要在事先给定运费和供给量的情况下，规划从不同供给节点到不同需求节点运送的货物量，使得总运输成本最小，同时还能满足所有需求节点的需求。

在[第三章](./Chapter3.md)，我们已经给出了运输问题在供需平衡下的建模：

$$\mathop{\min} \hspace{4pt} z = \sum \limits^{m}_{i = 1} \sum \limits^{n}_{j = 1} c_{ij}x_{ij}$$

$$s.t \hspace{4pt} \left\{ \begin{aligned} \sum \limits^{n}_{j=1} x_{ij} = a_i , i = 1,2,..,m \\ \sum \limits^{n}_{i=1} x_{ij} = b_j , j = 1,2,..,n   \\  x_{ij} \geq 0, i = 1,2,...m, j = 1,2...n  \end{aligned}  \right.$$

