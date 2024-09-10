# Job Shop Problem (JSP)

!!! note "Reference"
    **Paper 1**: Wen-Yang Ku and J. Christopher Beck, Mixed Integer Programming Models for Job Shop Scheduling: A Computational Analysis, Computers and Operation Research, http://dx.doi.org/10.1016/j.cor.2016.04.006

## 问题描述

现有 $n$ 个**工作**（Jobs），$j \in J；$$m$ 个**机器**（machines），$m \in M$，  每个工作都需要在**每台机器**上进行加工，但是顺序可能不同。我们把每个任务在每个机器上加工的过程称为一个工序 **（Operation）**. 

- 我们用 $( \sigma^j_1, \sigma^j_2, ... , \sigma^j_h, ... ,\sigma^j_m)$ 表示工作 $j$ 的机器加工顺序。其中 $\sigma^j_h$ 表示工作 $j$ 的第 $h$ 道工序所在的机器号。 

- 我们记：$p_{i,j}$ 表示工作 $j$ 在机器 $i$ 上的加工时间。

我们需要决定每个任务的加工顺序，从而最小化最后一道工序的完成时间 (Makespans)。

> The objective is to find a schedule of $J$ on $M$ that minimizes the makespan, i.e., **the maximum completion time of the last operation of any job** in $J$. ==Makespan minimization for the JSP is NP-hard for $n \geq 3$ and $m \geq 2$。==

如下图所示，就是一个可行的任务调度方案。

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202409091714901.png)

> 图中有3个工作 Job 1/2/3，需要被安排在3台机器上：M 1/2/3。每个工作都有3道工序。上半部分表示工作的加工顺序约束，下半部分是从**机器视角**出发，展示每台机器上工作的加工状况。箭头表示工序约束。

## 3种整数规划 (MIP) 建模

### 析取图模型 (Disjunctive Model)

- 决策变量:

$x_{ij}$ :  工作 $j$ 在机器 $i$ 上的开始加工时间，是一个整数。

$z_{ijk}$ : 0-1变量，表示工作 $j$ 是否在工作 $k$ 之前，在机器 $i$ 上加工。


$$\min C_{\max}$$

subject to.

$$\begin{aligned}
\begin{cases}
\begin{align}
x_{ij} \geq 0, \quad \forall j \in J, i \in M \quad \\
x_{\sigma^j_h, j} \geq x_{\sigma^j_{h-1},j} + p_{\sigma^j_{h-1}, j}, \quad \forall j \in J, h = 2,...,m \quad \\
x_{ij} \geq x_{ik} + p_{ik} - V z_{ijk}, \quad \forall j, k \in J, j < k, i \in M \quad \\
x_{ik} \geq x_{ij} + p_{ij} - V (1-z_{ijk}), \quad \forall j, k \in J, j < k, i \in M \quad \\
C_{\max} \geq x_{\sigma^j_{m},j} + p_{\sigma^j_m, j} \quad \forall j \in J \quad \\
z_{ijk} \in \{0,1\} \quad \forall j, k \in J, i \in M \quad \\
\end{align}
\end{cases}
\end{aligned}$$

目标函数的含义是：最小化最晚完成工序的时间。

$V$ 是一个极大值，在模型中可以取 $\sum_{j\in J} \sum_{i \in M }p_{ij}$。因为每个机器上的加工时间必不可能小于所有加工时间求总和的情况。

| 约束编号 |                                含义                                |
| :------: | :----------------------------------------------------------------: |
|    1     |                     每个工作的开始加工时间非负                     |
|    2     | 工序加工顺序约束 (precedence constraints)，确保Job按照工序顺序加工 |
|    3     |         析取约束，同一时刻两个任务不能被分配到同一个机器上         |
|    4     |         析取约束，同一时刻两个任务不能被分配到同一个机器上         |
|    5     |                          最晚完成时间约束                          |
|    6     |                        $z_{ijk}$ 是0-1变量                         |

> 类似3/4这种约束，求解器里有一些加速方法，参考CPLEX indicator constraint.


### 时间索引模型 (Time-indexed Model)

- 决策变量：

$x_{ijt}$ 0-1变量，如果工作 $j$ 在时刻 $t$ 于机器 $i$ 上开始加工，则为 1，否则为 0.


$$\min C_{\max}$$

subject to. 

$$\begin{aligned}
\begin{cases}
\begin{align}
\sum_{t \in H} x_{ijt} = 1, \quad \forall j \in J, i \in M \quad \\
\sum_{t \in H} (t + p_{ij}) x_{ijt} \leq C_{\max} , \quad \forall j \in J, i \in M \quad \\
\sum_{j\in J} \sum_{t^{'} \in T_{ijt}} x_{ijt^{'}} \leq 1 , \quad \forall i \in M, t \in H, \text{where} \quad T_{ijt} = \{ {t - p_{ij} + 1, ..., t}  \} \quad \\
\sum_{t \in H} (t + p_{\sigma^j_{h-1}, j}) x_{\sigma^j_{h-1},jt} \leq \sum_{t \in H} t   x_{\sigma^j_{h},j,t}, \quad \forall j \in J, h = 2,...,m \quad \\
x_{ijt} \in \{0,1\} \quad \forall j \in J, i \in M, t \in H \quad \\
\end{align}
\end{cases}
\end{aligned}$$

目标函数不变。

| 约束编号 |                                    含义                                     |
| :------: | :-------------------------------------------------------------------------: |
|    7     |                       每个工作只在每个机器上加工一次                        |
|    8     |                              最晚完成时间约束                               |
|    9     | 在每个时间时间点，每台机器只能加工一个工作，不能超额加工 (Over-capacitated) |
|    10    |                 加工顺序约束，保证工作按照给定顺序完成加工                  |

### 基于排序的模型 (Rank-based model)

- 决策变量：

$x_{ijk}$： 0-1变量，如果工作 $j$ 被安排在机器 $i$ 的第 $k$ 个位置上，则为 1，否则为 0。

$h_{ik}$：机器 $i$ 上的第 $k$ 个位置上的工作的开始加工时间。

我们引入参数  $r_{ijk}$，0-1变量，表示工作 $j$ 的第 $k$ 个工序是否需要机器 $i$。如果需要，则为 1. 否则为 0.

$$\min C_{\max}$$

subject to. 

$$\begin{aligned}
\begin{cases}
\begin{align}
\sum_{j \in J} x_{ijk} = 1, \quad \forall i \in M, k = 1,...,n \quad \\
\sum^n_{k = 1} x_{ijk} = 1, \quad \forall j \in J, i \in M \quad \\
h_{ik} + \sum_{j \in J} p_{ij} x_{ijk}  \leq h_{i, k+1} \quad \forall i \in M, k = 1,...,n \quad \\
\sum_{i \in M}r_{ijl}h_{ik} + \sum_{i \in M} r_{ijl} p_{ij} \leq V (1 - \sum_{i \in M} r_{ijl} x_{ijk}) + V (1 - \sum_{i\in M} r_{ij,l+1}x_{ijk^{'}}) + \\ \sum_{i \in M} r_{ij,l+1} h_{ik^{'}}, \quad \forall j \in J, i \in M, ,,k^{'} = 1,...,n, l = 1,...,m-1 \quad \\
h_{in} + \sum_{j \in J} p_{ij} x_{ijk} \leq C_{\max} ,\forall i \in M \quad \\
h_{ik} \geq 0, \forall i \in M, k = 1,2,...,n \quad \\
x_{ijk} \in \{0,1\} \quad \forall j \in J, i \in M, k = 1,2,...,n \quad \\
\end{align}
\end{cases}
\end{aligned}$$


| 约束编号 |                                   含义                                   |
| :------: | :----------------------------------------------------------------------: |
|    12    |                    每个机器的每个位置都只能放一个工作                    |
|    13    |                    每个任务只只占据每个机器的一个位置                    |
|    14    | 约束一台机器上一个工作的开始加工时间必须不小于该机器前一个工作的完成时间 |
|    16    |                               加工顺序约束                               |
|    17    |                    最大完成时间约束，用以标记目标函数                    |
|    18    |            任何工作在任何机器的位置上的加工开始时间不得小于0             |

