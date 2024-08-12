# 最小费用流 

最小费用流问题（Minimal Cost Flow Problem）在网络最优化问题中占有核心地位。可以表述如下：

> 对每个节点 $v_i$ 均给定实数 $b_i$， 如果 $b_i > 0$，那么称 $b_i$ 为发点，$b_i$ 的值为该点的供给量。如果 $b_i < 0$，那么称 $b_i$ 为收点， $-b_i$ 为该点的需求量。若  $b_i = 0$，那么称 $b_i$ 为转运点。
>
> 对于每条边 $e_j$，给定实数 $e_j$，它是在边 $e_j$ 上每单位流量的费用，称为费用系数。再给定正数 $u_j$，它是边 $e_j$ 上流量的上界。


最小费用流的问题就是要确定每个边上的流量 $x_j$，使得不超过上界限制，并满足各个节点的供需要求，同时又使得总费用最小。对于网络，我们引入一个 $m \times n$ 的矩阵 $A$。其中每个元素按照如下标准取值：

$$\begin{aligned}\begin{equation*}
a_{ij} = \begin{cases}
1, \hspace{10pt} \text{if } v_i \text{starts from} e_j \\
-1, \hspace{10pt} \text{if } v_i \text{ends at} e_j \\
0, \hspace{10pt} \text{Otherwise}
\end{cases}
\end{equation*}\end{aligned}$$

写成矩阵形式，如下：

$$\begin{bmatrix} 1 & 1 & . & . & . & 1 & 1 & . \\ -1 & . & 1 & 1 & . &  . & . & . \\  . & -1 & -1 & . & 1 & . & -1 & . \\ . & . & . & -1 & -1 & . & . & -1 \\ . & . & . & . & . & -1 & 1 & 1 \end{bmatrix}$$

即可表示如图