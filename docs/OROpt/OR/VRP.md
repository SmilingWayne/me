# 车辆路径问题（VRP）及相关

## 建模篇 

### Naive Formulation 

#### VRP

| Notations  |                         Meanings                          |
| :--------: | :-------------------------------------------------------: |
| $i , j, h$ |                         节点索引                          |
|    $k$     |                         车辆索引                          |
| $0,n + 1$  |                   depot，终点depot索引                    |
| $x_{ijk}$  | 决策变量，0-1binary， $k$ 车是否经过边$(i,j), i \neq j$ , |
|  $c_{ij}$  |              车辆 $k$ 经过边 $(i,j)$ 的成本               |
| $\mu_{ij}$ |                    MTZ 约束的辅助变量                     |
|    $V$     |                         节点集合                          |
|    $A$     |                       所有边的集合                        |
|    $K$     |                      所有车辆的集合                       |
|    $C$     |             所有客户点的集合  {1, 2, ..., n}              |


$$\min \sum \limits_{k \in K} \sum \limits_{i \in V} \sum \limits_{j \in V} c_{ij} x_{ijk}$$

$$\text{s.t.} \begin{aligned}
\begin{cases}
\begin{align}
\sum \limits_{k \in K} \sum_{j \in V} x_{ijk}  & =  1 ,\quad \forall i \in C  \quad \\
\sum \limits_{k \in K} x_{0jk}  & = 1, \quad \forall k \in K \quad \\
\sum \limits_{i \in V} x_{i (n+1) k}  & = 1, \quad \forall k \in K \quad \\
\sum \limits_{i \in V} x_{ihk} - \sum \limits_{j \in V} x_{hjk} &  = 0, \quad \forall h \in C, \forall k \in K \quad \\
\mu_{ik} - \mu_{jk} + N x_{ijk} &  \leq N - 1, \quad \forall i \in V / \{n+1\}, \quad \forall j \in V / \{0\} , \forall k \in K \quad \\
x_{ijk} \in \{0, 1\}, &  \quad \forall (i, j) \in A, \forall k \in K \quad \\
\end{align}
\end{cases}
\end{aligned}$$

---

#### CVRP 

| Notations  |                         Meanings                          |
| :--------: | :-------------------------------------------------------: |
| $i , j, h$ |                         节点索引                          |
|    $k$     |                         车辆索引                          |
| $0,n + 1$  |                   depot，终点depot索引                    |
| $x_{ijk}$  | 决策变量，0-1binary， $k$ 车是否经过边$(i,j), i \neq j$ , |
|  $c_{ij}$  |              车辆 $k$ 经过边 $(i,j)$ 的成本               |
| $\mu_{ij}$ |                    MTZ 约束的辅助变量                     |
|    $V$     |                         节点集合                          |
|    $A$     |                       所有边的集合                        |
|    $K$     |                      所有车辆的集合                       |
|    $C$     |             所有客户点的集合  {1, 2, ..., n}              |
|   $q_i$    |              (new added!) 客户 $i$ 处的需求               |
|    $Q$     |                  (new added!)     车容量                  |

$$\min \sum \limits_{k \in K} \sum \limits_{i \in V} \sum \limits_{j \in V} c_{ij} x_{ijk}$$

$$\text{s.t.} \begin{aligned}
\begin{cases}
\begin{align}
\sum \limits_{k \in K} \sum_{j \in V} x_{ijk}  & =  1 ,\quad \forall i \in C  \quad \\
\sum \limits_{k \in K} x_{0jk}  & = 1, \quad \forall k \in K \quad \\
\sum \limits_{i \in V} x_{i (n+1) k}  & = 1, \quad \forall k \in K \quad \\
\sum \limits_{i \in V} x_{ihk} - \sum \limits_{j \in V} x_{hjk} &  = 0, \quad \forall h \in C, \forall k \in K \quad \\
\mu_{ik} - \mu_{jk} + N x_{ijk} &  \leq N - 1, \quad \forall i \in V / \{n+1\}, \quad \forall j \in V / \{0\} , \forall k \in K \quad \\
\sum \limits_{i \in C} \sum \limits_{j \in V} q_i x_{ijk} & \leq Q, \quad \forall k \in K \quad {\color{red}\text{Capacity Constr!}}\\
x_{ijk} \in \{0, 1\}, &  \quad \forall (i, j) \in A, \forall k \in K \quad \\
\end{align}
\end{cases}
\end{aligned}$$

---

#### CVRPTW

| Notations  |                            Meanings                            |
| :--------: | :------------------------------------------------------------: |
| $i , j, h$ |                            节点索引                            |
|    $k$     |                            车辆索引                            |
| $0,n + 1$  |                      depot，终点depot索引                      |
| $x_{ijk}$  |   决策变量，0-1binary， $k$ 车是否经过边$(i,j), i \neq j$ ,    |
|  $c_{ij}$  |                 车辆 $k$ 经过边 $(i,j)$ 的成本                 |
|    $V$     |                            节点集合                            |
|    $A$     |                          所有边的集合                          |
|    $K$     |                         所有车辆的集合                         |
|    $C$     |                所有客户点的集合  {1, 2, ..., n}                |
|   $q_i$    |                       客户 $i$ 处的需求                        |
|    $Q$     |                             车容量                             |
|   $s_{ik}$   |               (new added!)  时间戳辅助变量，非负               |
| $e_i, l_i$ |            (new added!)    $i$ 节点的时间窗下/上界             |
|  $t_{ij}$  |           (new added!)    经过边 $(i,j)$ 所花的时间            |
|    $M$     | (new added!) 一个极大值，下界为 $\max \{ l_i - e_j + t_{ij}\}$ |

$$\min \sum \limits_{k \in K} \sum \limits_{i \in V} \sum \limits_{j \in V} c_{ij} x_{ijk}$$

$$\text{s.t.} \begin{aligned}
\begin{cases}
\begin{align}
\sum \limits_{k \in K} \sum_{j \in V} x_{ijk}  & =  1 ,\quad \forall i \in C  \quad \\
\sum \limits_{k \in K} x_{0jk}  & = 1, \quad \forall k \in K \quad \\
\sum \limits_{i \in V} x_{i (n+1) k}  & = 1, \quad \forall k \in K \quad \\
\sum \limits_{i \in V} x_{ihk} - \sum \limits_{j \in V} x_{hjk} &  = 0, \quad \forall h \in C, \forall k \in K \quad \\
s_{tk} + t_{ij} - M (1 - x_{ijk}) & \leq s_{jk} \quad \forall (i,j) \in A, \forall k \in K \quad  {\color{red}\text{TW Constr!}}\\
e_i \leq s_{ik} & \leq l_i \quad \forall i \in C, \forall k \in K \quad  {\color{red}\text{TW Constr!}}\\
\sum \limits_{i \in C} \sum \limits_{j \in V} q_i x_{ijk} & \leq Q, \quad \forall k \in K \quad \\
x_{ijk} \in \{0, 1\}, &  \quad \forall (i, j) \in A, \forall k \in K \quad \\
\end{align}
\end{cases}
\end{aligned}$$

!!! note "注意在时间窗约束的情况下，不需要考虑去子环了，因为时间窗本来就带有去子环的效果，卡车经过的每一个节点都被赋予一个时间变量。这个变量随着车的运行会严格递增。因此首尾相接的情况必定不会存在。"

### Set partitioning formulation

- 记  $\mathcal{R}$ 表示所有可行的路径的下标集合。

- 记 $a_{i \ell}$ 是一个 0-1 Binary的系数，如果第 $i \in V$ 个节点属于第 $\ell \in  \mathcal{R}$ 个路径。

- 每个路径 $\ell \in  \mathcal{R}$ 有一个对应的成本 $c_{\ell}$

- 记 $\xi_{\ell}$ 是 0-1 Binary, 如果路径 $\ell \in \mathcal{R}$ 在最终解中。

由此可以构建基于集合分割的建模方式。


$$\begin{aligned}
\min & \quad \sum_{\ell \in \mathcal{R}} c_{\ell} \xi_{\ell} \\
\text{s.t.} & \quad 
\begin{cases}
\begin{align}
\sum_{\ell \in \mathcal{R}} a_{i\ell} \xi_{\ell} = 1, \quad \forall i \in \mathcal{V}_c \quad \\
\sum_{\ell \in \mathcal{R}} \xi_{\ell} = M \quad \\
\xi_{\ell} \in \{0,1\}, \quad \forall \ell \in \mathcal{R} \quad
\end{align}
\end{cases}
\end{aligned}$$

注意了，为什么这里没有去子环约束，是因为最开始的“可行路径的下标集合”已经约束了这个路径一定要是可行的（从depot到depot）。

这个建模的方法，很适合“分枝定价”去精确地求解车辆路径问题。这个解法的子问题就是生成一些可行的路径，加入到所有的可行路径中。而这个子问题本身是在求一个“资源限制情况下的最短路问题”。


!!! warning "2024.06.12 已标记为待补充 / 修订。"

