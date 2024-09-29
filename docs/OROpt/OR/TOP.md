# 定向问题(Orienteering Problem)

!!! quote "说在前面"
    定向问题(Orienteering Problem)，最早的描述出现在1987年的 Paper 中。（`Golden, B. L., Levy, L., & Vohra, R. (1987). The orienteering problem. Naval Research Logistics, 34(3), 307–318.`）。这篇笔记基于2016年的这篇综述展开。`Gunawan, A., Lau, H. C., & Vansteenwegen, P. (2016). Orienteering Problem: A survey of recent variants, solution approaches and applications. European Journal of Operational Research, 255(2), 315–332. doi:10.1016/j.ejor.2016.04`

问题描述是这样的。

给定一个客户节点集合 $\mathcal{N}_c = \{1, 2, ..., |N|\}$。除了这些节点外还有一个出发（返回）节点。所以图中所有节点集合 $\mathcal{N} = \mathcal{N}_c \cup \{ 0\}$。抵达每个节点都可以有一个非负的收益 $p_i$。我们必须从节点 0 出发，并回到节点 0。给定一个时间限制 $T_{\max}$。我们需要在这个时间内==访问其中一部分节点== ，目标是最大化访问这些节点的收益，每个节点至多访问一次。

这是定向问题(OP)的最基本的描述。可以视为这**是一个背包问题 + TSP问题的结合。**

我们接下来给出这个问题的数学规划模型。


**决策变量：**

$x_{ij}$, 0-1变量，表示边 $(i, j)$ 是否被访问。如果访问了就是1，否则就是0。

**目标函数：**

$$\max \sum_{i \in \mathcal{N}} \sum_{j \in \mathcal{N}_c} p_j x_{ij} $$

> 最大化在每个节点的收益。

**约束条件：**


$$\begin{aligned}
\begin{cases}
\begin{align}
\sum_{j \in \mathcal{N}_c} x_{0j} = \sum_{j \in \mathcal{N}_c} x_{j0} = 1 \quad \\
\sum_{i \in \mathcal{N}}x_{ik} = \sum_{j \in \mathcal{N}} x_{kj} \leq 1 ; \quad \forall k \in \mathcal{N} \\
\sum_{i\in \mathcal{N}} \sum_{i\in \mathcal{N}} t_{ij} x_{ij} \leq T_{\max } \quad \\
1 \leq u_i \leq |\mathcal{N}|; \quad \forall i \in \mathcal{N} \quad \\
u_i - u_j + 1 \leq |\mathcal{N}| (1 - x_{ij}) ; \quad \forall i \in \mathcal{N} \quad \\
\end{align}
\end{cases}
\end{aligned}$$

| 约束编号 |                                                   含义                                                   |
| :------: | :------------------------------------------------------------------------------------------------------: |
|    1     |                                         约束从节点0出发，到0结束                                         |
|    2     |                                                流平衡约束                                                |
|    3     | 最大时间约束，这里假定在每个节点没有处理时间；所以这个约束也可以表示为行驶距离约束，比如无人机航程限制。 |
|    4     |                                      去子环约束（MTZ formulation）                                       |
|    5     |                                      去子环约束（MTZ formulation）                                       |

这个模型很容易可以改写成TOP(Team Orienteering Problem)，团队定向问题，本质上是把背包问题和VRP问题结合在一起。

## 考虑收益递减的TOPTW问题

我接触这个问题来源于数据魔术师的一个讲座，Paper场景是基于救灾场景的，意思是抵达每个节点的时间关系到在这个节点的收益。抵达得越晚，救援的效果就会越差。我们不得晚于某个时刻抵达某个节点（对应于带时间窗）。同样地，我们有多个救援队伍。假设队伍用 K 集合表示。车是同质的。

其他参数： $p_i, d_i, s_i, D_i$，分别表示节点 $i$ 的最大收益、收益衰减率、服务时长、服务截止时间。

决策变量： 

$x_{ij}$，0-1变量，表示边 $(i, j)$ 是否被访问。如果访问了就是1，否则就是0。这个和OP问题是一致的。

$y_i$ ： 0-1变量，表示客户 $i$ 是否被服务。

$a_i$： 连续变量，到达客户 $i$ 的时间；

**目标函数：**

$$\max \quad \sum_{i \in \mathcal{N}_c} p_i y_i - d_i a_i$$

**约束条件：**

$$\begin{aligned}
\begin{cases}
\begin{align}
\quad \sum_{j \in \mathcal{N}_c} x_{0j} = K, \quad \forall i \in \mathcal{N}_c \quad \\
\sum_{i \in \mathcal{N}_c} x_{i0} = K, \quad \forall i \in \mathcal{N}_c \quad \\
\sum_{j \in \mathcal{N}, j \neq i} x_{ij} = \sum_{j \in \mathcal{N}, j \neq i} x_{ji}, \quad \forall i \in \mathcal{N}_c \quad \\
\sum_{j \in \mathcal{N}, j \neq i} x_{ji} = y_i, \quad \forall i \in \mathcal{N}_c \quad \\
a_i + s_i + t_{ij} \leq a_j + M_{ij}(1 - x_{ij}), \quad \forall i \in \mathcal{N}_c, j \in \mathcal{N} \quad \\
a_i \geq t_{0i} y_i, \quad \forall i \in \mathcal{N}_c \quad \\
a_i \leq D_i y_i, \quad \forall i \in \mathcal{N}_c \quad \\
a_0 \leq T_{\text{max}} \quad \\
x_{ij} \in \{0, 1\}, \quad \forall i, j \in \mathcal{N} \quad \\
y_i \in \{0, 1\}, \quad \forall i \in \mathcal{N}_c \quad \\
a_i \geq 0, \quad \forall i \in \mathcal{N} \quad \\
\end{align}
\end{cases}
\end{aligned}$$

|  约束编号  |                   含义                   |
| :--------: | :--------------------------------------: |
|    6，7    |  约束从节点0出发，到0结束，总共K个队伍   |
|     8      |                流平衡约束                |
|     9      |      判断某个节点是否被任意车访问过      |
|     10     |      去子环约束（MTZ formulation）       |
| 11，12，13 | 约束到达节点的时间，以及抵达时刻不得太晚 |

> 该模型可以参考：【待补充】

