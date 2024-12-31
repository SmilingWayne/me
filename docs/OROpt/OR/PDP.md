# 取送货问题(Pickup and Delivery Problem) 以及拓展

!!! quote "参考资料"
    - `Ropke, Stefan & Pisinger, David. (2006). An Adaptive Large Neighborhood Search Heuristic for the Pickup and Delivery Problem with Time Windows. Transportation Science. 40. 455-472. 10.1287/trsc.1050.0135.` (ALNS 开山作)
    - `Cordeau, JF., Laporte, G. The dial-a-ride problem: models and algorithms. Ann Oper Res 153, 29–46 (2007). https://doi.org/10.1007/s10479-007-0170-8` (DARP 一个很好的总结) 
    - 待补充。

## Pickup and Delivery Problem with Time Windows 

一切的开始。取送货问题。在VRP问题中，每个顾客都是独立的，我们的讨论对象是“顾客”。现在，我们的讨论对象，是**订单**。（request）每个订单有一个`pickup`节点，有一个`delivery`节点。每个节点有各自的时间窗。车辆必须==先到 `pickup` 节点取得货物，然后运送到 `delivery` 节点。== 这就有一个先后顺序的情况。

除此之外，时间窗、运载量等基础约束同样成立。

### 决策变量

| 符号       | 解释                                                    |
| ---------- | ------------------------------------------------------- |
| $x_{ij}^k$ | 若车辆 $k$ 行驶弧 $(i, j)$，则 $x_{ij}^k = 1$，否则为 0 |

### 参数

| 符号            | 解释                                                                                                                                      |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| $G = (V, A)$    | 有向图，$V$ 是节点集，$A$ 是弧集                                                                                                          |
| $V$             | 节点集，包括 $0$ 和 $2n+1$（同一配送中心，分别表示起点和终点）以及 $P, D$ （pickup的节点集合、delivery的节点集合）                        |
| $P$             | 提货节点集合，$P = \{1, \dots, n\}$                                                                                                       |
| $D$             | 送货节点集合，$D = \{n+1, \dots, 2n\}$                                                                                                    |
| $(i, n+i)$      | 任务对，$i \in P$，$n+i \in D$                                                                                                            |
| $q_i$           | 节点 $i$ 的载荷，$q_0 = q_{2n+1} = 0$， $q_i \geq 0, \forall i \leq n; q_i \leq 0, \forall i \geq n + 1$                                  |
| $d_i$           | 节点 $i$ 的服务时间，$d_0 = d_{2n+1} = 0$                                                                                                 |
| $A$             | 弧集，$A = \{(i, j): i = 0, j \in P \text{ or } i, j \in P \cup D, i \neq j \text{ and } i \neq n + j \text{ or } i \in D , j = 2n + 1\}$ |
| $Q_k$           | 车辆 $k$ 的最大载重量                                                                                                                     |
| $c_{ij}^k$      | 车辆 $k$ 行驶弧 $(i, j)$ 的成本                                                                                                           |
| $t_{ij}$        | 从节点 $i$ 到节点 $j$ 的行驶时间                                                                                                          |
| $[e_i, \ell_i]$ | 节点 $i$ 的时间窗                                                                                                                         |
| $u_i^k$         | 车辆 $k$ 在节点 $i$ 开始服务的时间                                                                                                        |
| $w_i^k$         | 车辆 $k$ 在节点 $i$ 时的载荷                                                                                                              |



$$\begin{align}
\text{(PDPTW)} \quad & \text{Minimize} \quad \sum_{k \in K} \sum_{i \in V} \sum_{j \in V} c_{ij}^k x_{ij}^k  \\
& \sum_{k \in K} \sum_{j \in V} x_{ij}^k = 1 \quad (i \in P), \\
& \sum_{i \in V} x_{0i}^k = \sum_{i \in V} x_{i,2n+1}^k = 1 \quad (k \in K). \\
\sum_{j \in V} x_{ij}^k - \sum_{j \in V} x_{n+i,j}^k &= 0 \quad (i \in P, k \in K), \\
\sum_{j \in V} x_{ji}^k - \sum_{j \in V} x_{ij}^k &= 0 \quad (i \in P \cup D, k \in K), \\
M(1 - x_{ij}^k) + u_j^k &\geq u_i^k + d_i + t_{ij} \quad (i, j \in V, k \in K), \\
M(1 - x_{ij}^k) + w_j^k &\geq w_i^k + q_j  \quad (i, j \in V, k \in K), \\
u^{k}_{n + i} - (u^k_{i} + d_i) & \geq t_{i,n+i} \quad (i \in P, k \in K), \\
e_i &\leq u_i^k \leq \ell_i \quad (i \in V, k \in K), \\
\max\{0, q_i\} &\leq w_i^k \leq \min\{Q_k, Q_k + q_i\} \quad (i \in V, k \in K), \\
x_{ij}^k &\in \{0, 1\} \quad (i, j \in V, k \in K).
\end{align}$$




-----------


## Dial-a-Ride Problem (DARP)

一种特殊的取送货问题。在前面提到的PDP问题中，一个订单有一个固定的pickup的位置，一个delivery的位置（以及对应节点的时间窗口）。但是，如果时间窗口比较松的话，一个货物装上车可以一直呆在车上。DARP问题对应的是一个新的情况。更多针对的是==为老年人或者其他有需要的人提供"Door-to-Door"运输的场景==，而不只是送货物。因此，需要更多地考虑**乘客的福祉**。（`What makes the DARP different from most such routing problems is the human perspective. When transporting passengers, reducing user inconvenience must be balanced against minimizing operating costs.`）

乘客福祉体现在约束中，**就是“每个顾客的在途时间必须进行限制，不能让乘客在车上停留太久”**。

另一个方面，数值上，在传统`VRP/PDP`问题中，车辆载重一般是冗余的，主要起作用的是时间窗，但是，在DARP中，**我们的运输车辆可能是普通汽车，载客量较少**。因此，单车辆的容量相比货运物流场景的车辆更加小。

### 决策变量

| 符号       | 解释                                                    |
| ---------- | ------------------------------------------------------- |
| $x_{ij}^k$ | 若车辆 $k$ 行驶弧 $(i, j)$，则 $x_{ij}^k = 1$，否则为 0 |

### 参数

| 符号                 | 解释                                                                                                                                      |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| $G = (V, A)$         | 有向图，$V$ 是节点集，$A$ 是弧集                                                                                                          |
| $V$                  | 节点集，包括 $0$ 和 $2n+1$（同一配送中心，分别表示起点和终点）以及 $P, D$ （pickup的节点集合、delivery的节点集合）                        |
| $P$                  | 提货节点集合，$P = \{1, \dots, n\}$                                                                                                       |
| $D$                  | 送货节点集合，$D = \{n+1, \dots, 2n\}$                                                                                                    |
| $(i, n+i)$           | 任务对，$i \in P$，$n+i \in D$                                                                                                            |
| $q_i$                | 节点 $i$ 的载荷，$q_0 = q_{2n+1} = 0$， $q_i \geq 0, \forall i \leq n; q_i \leq 0, \forall i \geq n + 1$                                  |
| $d_i$                | 节点 $i$ 的服务时间，$d_0 = d_{2n+1} = 0$                                                                                                 |
| $A$                  | 弧集，$A = \{(i, j): i = 0, j \in P \text{ or } i, j \in P \cup D, i \neq j \text{ and } i \neq n + j \text{ or } i \in D , j = 2n + 1\}$ |
| $Q_k$                | 车辆 $k$ 的最大载重量                                                                                                                     |
| $c_{ij}^k$           | 车辆 $k$ 行驶弧 $(i, j)$ 的成本                                                                                                           |
| $t_{ij}$             | 从节点 $i$ 到节点 $j$ 的行驶时间                                                                                                          |
| $\textcolor{red}{L}$ | **最大乘客行驶时间**  (新增)                                                                                                              |
| $[e_i, \ell_i]$      | 节点 $i$ 的时间窗                                                                                                                         |
| $u_i^k$              | 车辆 $k$ 在节点 $i$ 开始服务的时间                                                                                                        |
| $w_i^k$              | 车辆 $k$ 在节点 $i$ 时的载荷                                                                                                              |
| $r_i^k$              | 用户 $i$ 的乘车时间                                                                                                                       |



$$\begin{aligned}
\text{(DARP)} \quad & \text{Minimize} \quad \sum_{k \in K} \sum_{i \in V} \sum_{j \in V} c_{ij}^k x_{ij}^k  \\
& \sum_{k \in K} \sum_{j \in V} x_{ij}^k = 1 \quad (i \in P)  \\
& \sum_{i \in V} x_{0i}^k = \sum_{i \in V} x_{i,2n+1}^k = 1 \quad (k \in K). \\
\sum_{j \in V} x_{ij}^k - \sum_{j \in V} x_{n+i,j}^k &= 0 \quad (i \in P, k \in K), \\
\sum_{j \in V} x_{ji}^k - \sum_{j \in V} x_{ij}^k &= 0 \quad (i \in P \cup D, k \in K), \\
M(1 - x_{ij}^k) + u_j^k &\geq u_i^k + d_i + t_{ij} \quad (i, j \in V, k \in K), \\
M(1 - x_{ij}^k) + w_j^k &\geq w_i^k + q_j  \quad (i, j \in V, k \in K), \\
r_i^k &\geq u_{n+i}^k - (u_i^k + d_i) \quad (i \in P, k \in K), \\
e_i &\leq u_i^k \leq \ell_i \quad (i \in V, k \in K), \\
t_{i,n+i} &\leq r_i^k \leq L \quad (i \in P, k \in K), \textcolor{red}{\text{New Constr!!}}\\
\max\{0, q_i\} &\leq w_i^k \leq \min\{Q_k, Q_k + q_i\} \quad (i \in V, k \in K), \\
x_{ij}^k &\in \{0, 1\} \quad (i, j \in V, k \in K).
\end{aligned}$$


## Simultaneous Pickup and Delivery (SPD)

待补充。


