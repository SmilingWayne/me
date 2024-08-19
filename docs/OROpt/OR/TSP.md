# TSP 问题

!!! abstract "感谢GPT-4o以及Claude在本文章编写过程中提供的帮助。"
    参考链接：

    - [运筹OR帷幄的文章](https://mp.weixin.qq.com/s/tDYOxlSQHKRJkf5EcaBJ1A) (如果不想看论文，这个几乎是把知识喂给你吃的那种)；

    - [Concorde Solver and intro](https://www.math.uwaterloo.ca/tsp/index.html): 比本页面精致很多、提供了丰富可视化、benchmark、求解器等的网站；
    - [Dantzig, George, Ray Fulkerson, and Selmer Johnson. "Solution of a large-scale traveling-salesman problem." Journal of the operations research society of America 2.4 (1954): 393-410.](https://www.rand.org/content/dam/rand/pubs/papers/2014/P510.pdf); (DFJ formulation)

    - [Miller, Clair E., Albert W. Tucker, and Richard A. Zemlin. "Integer programming formulation of traveling salesman problems." Journal of the ACM (JACM) 7.4 (1960): 326-329.](https://dl.acm.org/doi/10.1145/321043.321046): (MTZ formulation)

    - [Gavish, Bezalel, and Stephen C. Graves. "The travelling salesman problem and related problems." (1978).](https://dspace.mit.edu/handle/1721.1/5363) : (Commodity flow formulation)


## 问题描述与第一种建模方法

**问题描述：** 旅行商问题（Travelling Salesman Problem, TSP），或者说货郎担问题，是一个著名的NP-hard问题。给定一个无向图 $G(V,E)$，其中有 $N$ 个节点。$E$ 为边集。每条边有权重。目标是找到从任意一个节点出发，依次不重复地经过所有的其他节点，最终返回到起点的权重和最小的路径。这是一个著名的NP-hard问题。

> 问题输入：一系列点的坐标或者图的邻接矩阵等类似格式；
>
> 问题输出：一个访问序列，每个节点只被访问一次，每个节点都只被离开一次。

|   符号   |             含义              |
| :------: | :---------------------------: |
| $x_{ij}$ | 0-1变量，从i到j的边是否被选中 |
| $c_{ij}$ |         从i到j的权重          |
|   $V$    |  所有节点(vertex)构成的集合   |
|   $A$    |    所有边 (arcs)构成的集合    |

熟悉简单图论知识的读者可以写出下面的模型：

$$\min \sum_{i \in V} \sum_{j \in V} c_{ij} x_{ij} \\
\text{s.t.} \begin{aligned}\begin{equation*}
\begin{cases}
\sum_{i \in V}x_{ij} = 1, \quad \forall j \in V, i \neq j \\ 
\sum_{j \in V}x_{ij} = 1, \quad \forall i \in V, i \neq j \\ 
x_{ij} \in \{0, 1 \}
\end{cases}
\end{equation*}\end{aligned}$$

但是，上述约束仅仅保证出入度是相等且等于1的，无法保证不形成环路，以下情况可能是不符合要求的.

此时不构成一个回路，而是有两个回路了。

```
1---------2   5---6        1-------2----->
|         |   |   |   =>   |
|         |   |   |   =>   |
|         |   8---7   =>   |
|         |                |
3---------4                3-------4---->
```

所以我们需要加入一个经典的子环路消除约束（Subtour-elimination constraints）。子环路就是“没有包含所有节点 $V$ 的闭环”，访问的所有集合 $S$ 是所有节点的真子集。

我们先观察子环路的特点，比如上面的1-2-3-4 环路，可以发现4个节点中有4个边，也就是节点的数量等于这些点之间的边的数量。反过来，如果我们限制这些点之间边的数量不等于节点数，那么就一定不存在子环路了（逆否命题）。（ $\sum_{i,j \in S} x_{ij} < |S|$，往往写成 $\sum_{i,j \in S} x_{ij} \leq |S| - 1$ ）。**但是别忘了TSP最终是会回到原点的，这意味着结果中其实存在一个最大的环。因此我们需要约束最大的环不被破坏。**

> 怎么理解“这些点之间的边的数量：比如1、2、3、4之间的边可能有哪几条？ $x_{12} ，x_{13}， x_{14} ，x_{23} ，x_{24}， x_{34}$，还有把前后方向对调的 $x_{21}, x_{31} ...$ ，一共有12条边。如果是环路，这十二个边的和一定是3，反之，如果破开了，那么意味着这十二个边的和 <= 2

这个约束可以直接写成：

$\sum_{i,j \in S} x_{ij} \leq |S| - 1, \quad \forall S, 2 \leq |S| \leq |V| - 1$，

> 这个约束实际上是一个枚举的思想，==确保 $V$ 的所有真子集（除去单个节点这种不可能成环的情况）中，节点之间相连的边数都小于等于子集大小减一==。
>

于是我们可以把完整的模型写作如下。这个模型求解效率很不错。

$$\min \sum_{i \in V} \sum_{j \in V} c_{ij} x_{ij} \\
\text{s.t.} \begin{aligned}\begin{equation*}
\begin{cases}
\sum_{i \in V}x_{ij} = 1, \quad \forall j \in V, i \neq j \\ 
\sum_{j \in V}x_{ij} = 1, \quad \forall i \in V, i \neq j \\ 
\sum_{i,j \in S} x_{ij} \leq |S| - 1, \quad \forall S, 2 \leq |S| \leq |V| - 1 \\
x_{ij} \in \{0, 1 \}
\end{cases}
\end{equation*}\end{aligned}$$

这也是经典的DFJ formulation。

!!! example "这个约束的困难之处"
    约束实在是太多了！举个例子。1-2-3-4-5-6，一个六个节点的图。

    光是看包括节点1的情况，我们就要约束：

    1-2，1-3，1-4，1-5，1-6，
    
    1-2-3，1-2-4，1-2-5，1-2-6，1-3-4，1-3-5，1-3-6，1-4-5，1-4-6，1-5-6，
    
    1-2-3-4，1-2-3-5，1-2-3-6，1-3-4-5，1-3-4-6，1-4-5-6，

    1-2-3-4-5，1-2-3-4-6，1-3-4-5-6

    更不用提包括节点2的情况...

    2-3, 2-4, 2-5, 2-6...

    简单来说，我们用组合数可以算出这个约束总共有多少个：比如这里的真子集（且非仅1元素）可以视为，从 $N$ 节点中取2个，3个，4个...$N - 1$个，一共有 $C^2_N + C^3_N + .. + C^{N-1}_N = 2^N -1 - 2N$ 个约束！这是一个指数规模的约束。

!!! note "克服指数规模约束的一个方法"
    当然是，有没有一种方法可以不用添加所有的这种去子环，而是仅仅在“有需要的”地方添加呢？

    > 参考[Gurobi求解TSP问题](https://www.gurobi.com/documentation/current/examples/tsp_py.html)。通过求解器的回调函数，添加惰性约束（Lazy Constraint）对问题求解进行简化。前面的这个链接已经讲得很清楚了。

## 第二种建模方法

除了第一种方法外，还有第二种建模的思路，也叫MTZ约束。针对的同样是子环消除约束。可以理解成子环消除约束的第二种建模方法。

思路是给每个节点设置一个辅助决策变量 $\mu_i， \mu_i \geq 0$ 。对每个边都构建约束 $\mu_i - \mu_j + Mx_{ij} \leq M - 1$。在这里为了保证上界较紧，一般取 $M = N$（也就是节点数）

也就是子环消除约束变成 $\mu_i - \mu_j + N x_{ij} \leq N - 1$ 

!!! note "如何理解这个约束"

    我们分情况讨论。因为 $x_{ij}$ 是一个0-1变量，所以直接枚举两种情况：
    
    - 如果 $x_{ij} = 1$ ，说明 $i$ 在前，$j$ 在后，有 $\mu_i - \mu_j \leq -1$，说明在最优解的环路序列中，先经过了 $i$，下一个节点是 $j$ 节点。约束限制了 $j$节点的辅助变量==至少==比 $i$ 节点的辅助变量大1。（这里约束了相邻节点的最小值）
    - 如果 $x_{ij} = 0$，说明此时在最优解中没有经过路径 $ij$，说明i节点的下一个节点一定不是 $j$。$i$ 和 $j$ 是解中任意两个不相邻的节点。 $\mu_i - \mu_j \leq N - 1$ 。两个不相邻节点的差一定是小于等于 $N - 1$ 的。（这里约束了不相邻节点的最大值）


    ```text

    1 --- > 2 ----> 3 ----> 4 ----> 5

    ```

    > 比如在上面这个例子中，我们取路径中从1到5的这样一段。上面约束过了，相邻节点之间后面的比前面的，一定至少大 1，而不相邻的（比如1到5），中间至少隔了 $5 - 1 = 4$ 个节点。所以，就算我们的5和1是最后一个访问的节点，1是第一个节点（也就是最远的情况），那么这俩之间的辅助决策变量的差值最大只能是 $N - 1$。

    上面两个约束实际上的意思是：确定了一个上界，确定了一个相邻节点递增的下界，迫使每一次相邻节点之间的增长只能是1.

这种建模方法是“不成任何环”的。输出的结果是不返回起点的。为此需要设置一个虚拟的终点，图中共设置 $N+1$ 节点。这个节点没有流出，但是有一个流入，所有除了起点外的节点到虚拟节点的权重等于其到起点的权重。

最终模型如下：


$$\min \sum_{i \in V} \sum_{j \in V} c_{ij} x_{ij} \\
\text{s.t.} \begin{aligned}\begin{equation*}
\begin{cases}
\sum_{i \in V}x_{ij} = 1, \quad \forall j \in \{2,3,...,N+1\}, i \neq j \\ 
\sum_{j \in V}x_{ij} = 1, \quad \forall i \in \{1,2,..., N\}, i \neq j \\ 
\mu_i - \mu_j + Nx_{ij} \leq N - 1, \quad \forall i \in \{1,2,..., N\}, j \in \{2,3,...,N+1\}, i\neq j \\
x_{ij} \in \{0, 1\}, \mu_i \geq 0\end{cases}
\end{equation*}\end{aligned}$$

## 第三种建模方法：基于货物流

这种建模包括：

1. 单类流模型（Single-Commodity Flow，SCM)，（又称作Gavish-Graves（GG）模型）
2. 双类流模型（Two-Commodity Flow，TCM）
3. 多类流模型（Multi-Commodity Flow，MCM）。

单类流模型中，决策变量与DFJ相同， $x_{ij}$，表示边 (i,j) 是否被访问。目标函数、流平衡约束均相同。差别依然是如何对待子回路消除。

$$\min \sum_{i \in V} \sum_{j \in V} c_{ij} x_{ij}$$


$$\begin{aligned}
\begin{cases}
\begin{align}
\sum_{i \in V}x_{ij} = 1, \quad \forall j \in V, i \neq j \quad\\ 
\sum_{j \in V}x_{ij} = 1, \quad \forall i \in V, i \neq j \quad \\ 
y_{ij} \leq (n-1) x_{ij}, \quad \forall i,j \in V, (i, j) \in A \quad \\
\sum_{j \in V, (1, j) \in A} y_{1j} = n - 1 \quad \\
\sum_{i \in V, (i, j) \in A} y_{ij} - \sum_{k \in V, (j, k) \in A } y_{jk} = 1, \quad \forall j \in V \setminus \{1 \} \quad \\
x_{ij} \in \{0, 1 \} \quad \\
\end{align}
\end{cases}
\end{aligned}$$

这里解释一下引入的新辅助变量 $y_{ij}$，可以视为边 $(i, j)$ 上载着的货物的流量。由于总共访问 $n$ 个节点，可以视为访问一个节点后，就在这个节点上卸下一个货，所以从该节点出发的那个边的流量就一定比到达该节点的那个边的流量小1 （对应Constr 5），同理，从起点出发的那个边的流量就一定是 $n - 1$ （对应Constr 4）。

