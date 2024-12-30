# 车辆路径问题（VRP）｜拓展问题｜求解算法等

## 建模篇 

### Start from the easiest!

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
|  $s_{ik}$  |               (new added!)  时间戳辅助变量，非负               |
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



## Benchmark

话不多说，直接上链接：

- [SINTEF](https://www.sintef.no/projectweb/top/pdptw/documentation/): 维护了两个经典的数据集，VRPTW的Solomon数据集、 G & H数据集，以及PDPTW的Li & Lim 数据集。
- [Benchmark Update](http://combopt.org/tables/LiLim/)：同上团队维护，及时更新目前每个Case的最新找到的最优解，包括最新Improve是在什么时候找到的，什么团队找到的等。
- [Vidal's Site](https://w1.cirrelt.ca/~vidalt/en/VRP-resources.html):还是要抱紧大佬大腿，看看人家是怎么整合资料的。
- [Uchoa's dataset](http://www.vrp-rep.org/references/item/uchoa-et-al-2017.html)： Focus 在大规模CVRP问题，同时作者的paper做了一些很有意义的关于benchmark的总结;

## 其他类型的拓展

注意，VRP问题很经典的一个做法（其实也是优化领域很多paper的做法）就是不断加约束。所以，==这部分不会专注于具体的问题模型简写是什么，而专注于“新约束的意义”== ，比如这个约束和其他的不同在哪里，代表了什么等。实际上，这些所有的约束都可以和前面所谓的“Time window”、“capacity”等结合起来看。也正因此，下面的问题会忽略 `TW` 以及 `Capacity` 约束。

### Backhauls：取货完后再送货

送货后取货问题。其实和[取送货问题(Pickup and Delivery Problem)](./PDP.md)非常类似，但是又有不同。区别在于：

本问题下，不再是以“订单”来衡量了，而是回到了“顾客”，不考虑“订单”区分起终点的概念了。但是顾客的属性有区别。有一些是 `linehauls` 顾客，有一些是 `backhauls` 顾客。我们必须先从depot拿货物运给 `linehauls` 顾客，直到**服务完所有的 `linehauls` 顾客后**，再去服务 `backhauls` 顾客，从这些顾客处取。是一个**先送后取**的过程。

同样地，每一个顾客都有时间窗，每一个顾客都有载重量。车辆也有载重量。

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202412291859702.png)

> 图中的 `L` 就是先访问的 `linehauls`，`B` 是后访问的 `backhauls` 顾客们。

建模略。因为你可以**通过定义边的集合**，约束边的情况，其他的约束等，照搬整个VRPTW的模型，是一样的。参考文献：`İlker Küçükoğlu, Nursel Öztürk,An advanced hybrid meta-heuristic algorithm for the vehicle routing problem with backhauls and time windows, Computers & Industrial Engineering,Volume 86,2015,Pages 60-68,ISSN 0360-8352`

### PDVRP (Pickup and Delivery Vehicle Routing Problem)

乍一看，和PDPTW这类的问题有什么区别？

确实没什么区别，区别在于修改了每个顾客节点的重量的情况：某个节点，允许顾客有pickup的需求，或者delivery的需求。建模时候，定义顾客节点的取货重量、送货重量即可。很容易。

一个可能的，与其他取送货问题结合的场景，就是，既有PDP中“订单起终点”概念（某几个节点必须先后访问），又包含单个顾客“Pickup 需求，delivery需求”的混合取送货场景。可以参考 `Meng, S., Guo, X., Li, D., & Liu, G. (2023). The multi-visit drone routing problem for pickup and delivery services. Transportation Research Part E: Logistics and Transportation Review, 169, 102990.` 


### Two-Echelon VRP

两阶段配送VRP。前两年曾经被不少人搞过。目前快被吃烂了。所以很适合被放到我们这个笔记中珍藏起来。嘿嘿！

> 这里正好说一个自己的私货。我觉得这种两阶段的VRP系统的建模与分析特别契合“多式联运”的主题。Therefore, 还是值得看一看的。



## 工具篇

!!! warning "未完待续 ... "

好。最喜欢的部分。因为可以直接放链接。但是在开始之前，还得感谢链接的链接: 小马过河老师的几个推文。本部分的整理十分依赖于他的这个文章！[最新的几个VRP问题求解的开源工具](https://mp.weixin.qq.com/s/esrg4wASSRcowptRu3Ilfw)。

### 各种库

**启发式算法部分**：(标记符号表示我曾经使用过/正在使用)

- [x] [PyVRP](https://github.com/PyVRP/PyVRP)。Python 上能整出这种好活确实是会整活的。工程细节等，参考 IJOC 的这个Paper： `Wouda, N.A., L. Lan, and W. Kool (2024). PyVRP: a high-performance VRP solver package. INFORMS Journal on Computing, 36(4): 943-955. https://doi.org/10.1287/ijoc.2023.0055`
- [x] [ORTools VRP toolkit](https://developers.google.cn/optimization/routing/vrp?hl=zh-cn)。属实是真·开箱即用。支持多种约束。Ortools的经典版本。新手摸一摸，熟悉熟悉，跑跑数值试验，都是可以的。
- [ ] [HGS-CVRP](https://github.com/vidalt/HGS-CVRP)。Vidal 大佬的，用C++写的，用来针对CVRP而设计。提供了Python的Wrapper，[PyHygese](https://github.com/chkwon/PyHygese)但是似乎不是很理想。一个很感兴趣的方法。混合遗传搜索 `(HGS)`。目前启发式SOTA看到几个都是基于此的。文章见[Hybrid genetic search for the CVRP: Open-source implementation and SWAP* neighborhood](https://www.sciencedirect.com/science/article/pii/S030505482100349X)。
- [ ] [Filo2](https://github.com/acco93/filo2):专门为解决极大的CVRP问题（有数十万顾客节点）而设计的一个启发式算法库。特点是采用了非常快速、非常高效的邻域搜索技术。

**精确式算法部分**：

!!! note "如果想要彻底搞清楚精确式求解算法以及对应的细节等，首先你可以先看看发在MP上的这个文章（过于牛了）"
    [A generic exact solver for vehicle routing and related problems. ](https://link.springer.com/article/10.1007/s10107-020-01523-z)
    
    不仅求解了VRP问题，还探讨（并求解了！！）很多类似的复杂组合优化问题。具体有多少还是移步链接查看吧。

- [ ] [VRPSolveEasy](https://github.com/inria-UFF/VRPSolverEasy) ：专注于精确式解法的VRP仓库。作者的技术报告参考：`N. Errami, E. Queiroga, R. Sadykov, E. Uchoa. "VRPSolverEasy: a Python library for the exact solution of a rich vehicle routing problem", Technical report HAL-04057985, 2023.` 。

