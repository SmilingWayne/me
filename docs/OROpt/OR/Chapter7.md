# 图论


!!! abstract "路径规划的必修课。"
    参考：
    
    1. [Stanford Course](https://web.stanford.edu/~ashishg/cs261/win21/notes/)
    2. [MIT Course (Old version)](https://ocw.mit.edu/courses/15-082j-network-optimization-fall-2010/download/)

**图，(Graph)**，是一个由点集 $V$ 和 $V$ 中有限个元素的无序对构成的一个集合 $E$，二者组合形成的二元组。记为 $G = (V, E)$。 $V$ 中的元素 $v_i$ 称为顶点（Vertex），$E$ 中的元素称为边（Edge）。

按照图中边的不同属性，可以分为**有向图、无向图**。

一条边的两个端点如果相同，称为“环”。包含环的图，就是有环图。两个顶点如果有多重边，称为多重图。一个既没有环也没有多重边的图，称为**简单图**。

给边或者点赋予一定权重，表示类似成本、流量等的图，称为**赋权图**。

**连通图**
:   如果一个图任意两点间至少存在一条链，那么这个图称为连通图；

**树**
:   连通且不含圈的无向图称为树；

## 最小生成树

### Prim算法

- 每次从没有选的边里选一条边，这个边权值要尽可能地小，并且使它和已有的不够成圈，直到选够 $n - 1$ 个边为止。

!!! tip "🔔 ：小提示"
    有一个并查集的优化：迅速找到父节点并且回到源。

----


### Kruskal 算法

- 找每一个圈，把圈里最大的边删除掉，直到没有圈为止。

## 最短路问题


### 最短路问题的建模(单源最短路)

决策变量： $x_{ij}$ 表示从 $i$ 到 $j$ 的边是否被选中。

目标函数： $\min \sum_{i} \sum_j c_{ij} x_{ij}$

约束条件：

$$\begin{aligned}
\sum_j x_{ij} - \sum_i x_{ji} =  \quad 
\begin{cases}
-1. \quad i = \text{start} \\ 
1 \quad i = \text{terminal} \quad \quad \forall i \in V\\ 
0 \quad else
\end{cases}
\end{aligned}$$

如果精简一下，记图为 $G = (V, E)$, 决策变量精简为 $f_e$ 表明边 $e$ 是否被选择。写法是：

$$\begin{aligned}
\min \sum_{e\in E} f_e c_e \\
\begin{cases}
\sum_{(i, j) \in E} f_{(i,j)} - \sum_{(j, i) \in E} f_{(j, i)} & \geq d_j \quad \quad \forall j \in V  \\ 
f_e & \geq 0 \quad \quad \forall e \in E
\end{cases}
\end{aligned}$$

其中 $d_j$ 是节点 $j$ 的度 （入 - 出）。并且等号约束松弛成标准形式 ($\geq$)


!!! question "针对这个建模的进一步思考"
    最短路问题同样有对偶问题，那么这个对偶问题的含义是什么？

定义一个向量 $d()$。长度是节点个数 $V$。记图为 $G = (V, E)$

目标函数： $\max d(t) - d(s)$

约束条件：

$$\begin{aligned}
\text{s.t.} \begin{cases}
d_v \geq 0 \quad \forall v \in V \\
d(j) - d(i) \leq c_{ij} \quad  \forall (i, j) \in E
\end{cases}
\end{aligned}$$

**解释**
:   这里需要再次回到“对偶”的概念上。找从 $i$ 到 $j$ 的最短路，也就是要在对偶可行的基础上，最大化 $d(v)$.

    为什么目标函数只有两个值了：因为原问题的约束的右端，只有0，1，-1三个值，并且流平衡约束的参数是 0，所以实际上只有两个非 0 右端。对应到目标函数上。

进一步简化：

目标函数： $\max d(t)$

约束条件：

$$\begin{aligned}
\text{s.t.} \begin{cases}
d_s = 0 \\
d(j) - d(i) \leq c_{ij} \quad  \forall (i, j) \in E
\end{cases}
\end{aligned}$$

怎么有启发地理解这个模型呢。就是我们把每个边想象成一个静止长度 $c_e$ 的弹簧。把开始节点设为 0.尝试把这个图拉伸得尽可能地长，直到不能拉伸任何弹簧。我们整个图能被拉伸的最长的距离，也就是从 $s$ 到 $t$ 的最短路。*（这个仔细理解，会发现简直妙极）*

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202406120857738.png)

!!! quote "[参考链接：MIT](https://ocw.mit.edu/courses/15-082j-network-optimization-fall-2010/87ee338a701dcd52784c86daef642113_MIT15_082JF10_lec15.pdf) | [参考链接：Stanford](https://web.stanford.edu/~ashishg/cs261/win21/notes/l9_note.pdf)"


### Dijkstra 算法（单源最短路）

!!! abstract "关于Dijkstra算法"
    一种用于计算从单个源节点到图中所有其他节点的最短路径的算法。适用于加权图，其中要求**边的权重为非负值**

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202407222344256.gif)



- 找到从某地到某地最短的路径：广度优先搜索解决赋权有向图或者无向图的单源最短路径问题；Dijkstra算法采用的是一种贪心的策略，声明一个数组dis来保存源点到各个顶点的最短距离和一个保存已经找到了最短路径的顶点的集合，初始时，原点 s 的路径权重被赋为 0 。若对于顶点 s 存在能直接到达的边（s,m），则把dis[m]设为w（s, m）,同时把所有其他（s不能直接到达的）顶点的路径长度设为无穷大。初始时，集合T只有顶点s。 
- 然后，从dis数组选择最小值，则该值就是源点s到该值对应的顶点的最短路径，并且把该点加入到T中，OK，此时完成一个顶点，然后，我们需要看看新加入的顶点是否可以到达其他顶点并且看看通过该顶点到达其他点的路径长度是否比源点直接到达短，如果是，那么就替换这些顶点在dis中的值。 
- 然后，又从dis中找出最小值，重复上述动作，直到T中包含了图的所有顶点。

!!! warning "注意！"
    - 无法处理负权问题
    - 节点较多的话，计算量会加大


### Floyd算法 （多源最短路）

- Floyd算法又称为插点法，是一种利用**动态规划的思想**寻找给定的加权图中多源点之间最短路径的算法，

- 通过一个图的权值矩阵求出它的每两点间的最短路径矩阵。
- 我们的点如果在最短路上，那么我们用这个点去松弛最短路上的边的话，必定会松弛成功。因此，我们要想知道一个点在哪些点的最短路上，我们只需要用这个点去松弛所有边即可，松弛指的就是，把这个点作为一个“中转点”，遍历其出度和入度，如果距离更短就刷新图；
- 从一开始的邻接矩阵，遍历所有的节点，每次加入新结点都要更新==所有顶点之间的最短距离==，直到==所有顶点均可以作为中间顶点==之后（也就是对所有点都做了一次松弛），才算更新完毕，即可得到最终结果。

1. 输入权重矩阵： $D^{(0)} = D$
2. 计算 $D^{(k)} = (d^{(k)}_{ij})_{n \times n}$，其中： $d^{(k)}_{ij} = \min \{ d^{(k - 1)}_{ij}, d^{(k - 1)}_{ik} + d^{(k - 1)}_{kj} \}$
3. $D^{(n)} = (d^{(n)}_{ij})_{n \times n}$，元素 $d^{(n)}_{ij}$ 就是从 $i$ 到 $j$ 的最短路长。

----



例题：给定初始矩阵，求任意两点的最短路长。

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202406120859048.png)

$$D = D^{(0)} = \begin{bmatrix}
0 & 5 & 1 & 2 & \infty \\
5 & 0 & 10 & \infty & 2 \\
2 & 3 & 0 & 2 & 8 \\
2 & \infty & 6 & 0 & 4 \\
\infty & 2 & 4 & 4 & 0
\end{bmatrix}$$

开始计算！


$$D^{(1)} = \begin{bmatrix}
0 & 5 & 1 & 2 & \infty \\
5 & 0 & (6) & (7) & 2 \\
2 & 3 & 0 & 2 & 8 \\
2 & (7) & (3) & 0 & 4 \\
\infty & 2 & 4 & 4 & 0
\end{bmatrix}, D^{(2)} = \begin{bmatrix}
0 & 5 & 1 & 2 & (7) \\
5 & 0 & 6 & 7 & 2 \\
2 & 3 & 0 & 2 & (5) \\
2 & 7 & 3 & 0 & 4 \\
(7) & 2 & 4 & 4 & 0
\end{bmatrix}$$

$$D^{(3)} = \begin{bmatrix}
0 & (4) & 1 & 2 & (6) \\
5 & 0 & 6 & 7 & 2 \\
2 & 3 & 0 & 2 & 5 \\
2 & (6) & 3 & 0 & 4 \\
(6) & 2 & 4 & 4 & 0
\end{bmatrix}, D^{(4)} = \begin{bmatrix}
0 & 4 & 1 & 2 & (6) \\
5 & 0 & 6 & 7 & 2 \\
2 & 3 & 0 & 2 & 5 \\
2 & 6 & 3 & 0 & 4 \\
6 & 2 & 4 & 4 & 0
\end{bmatrix},$$

$$D^{(5)} = \begin{bmatrix}
0 & 4 & 1 & 2 & 6 \\
5 & 0 & 6 & (6) & 2 \\
2 & 3 & 0 & 2 & 5 \\
2 & 6 & 3 & 0 & 4 \\
6 & 2 & 4 & 4 & 0
\end{bmatrix},$$


!!! warning "注意"
    不能把负权加上最小的负数变整数这种做法，因为不是分阶段的问题，不能单纯地用DP的思想去解决。

    如果想要知道路径，还需要增加一个路由矩阵。

## 最大流问题

!!! warning "2024.06.12 已标记为待补充 / 修订。"

> 网络流，充分利用各个弧的容量，使得网络的通过流量最大。
>
> 有的问题可能有多个源/汇，但是可以加上虚拟源/汇，使得变成**单一源/汇**的问题，进而构成最大流问题
> **容量网络**：只有一个入次为0的点（源），只有一个出次为0的点（汇），其他的都是中间节点的网络；

- 最大流最小割定理：任何一个可行流的容量不会超过任何一个割集的容量。
    - 引入割的概念：把所有的点分成两个集合，起点在其中一个集合中，终点在另一个集合中，割的大小就是从起点割集S到终点割集T的个数；
    - 最小割：就是所有的割中，求一个最小的割，使得其容量**最小**；
    - 最大流和最小割问题是互为对偶的问题；

### Ford-Fulkson算法

> 在已经“犯错误”的情况下， 依然能够找到下一条路径；
>
> 前一次没有用过的边依然保留，为了纠正以前路径，可以把之前的路径反过来；
> 如此来实现不断地删除增广链；
> 
- 可行流f为最大流的充分必要条件是： ==当且仅当网络不存在增广链==;
- 给出一初始可行流，例如 fij =0
-  寻找增广链，若存在，通过添加反向路径，允许水流按照原来方向流回去，制造反向图residual graph；
      - 如果找到增广链，则通过该增广链调整、增加网络流
      - 若不存在增广链，则网络流不可再增加。求得最大流
- 管道网络中每条边的最大通过能力（容量）是有限的，实际流量不超过容量。最大流问题(maximum flow problem)，一种组合最优化问题，就是要讨论如何充分利用装置的能力，使得运输的流量最大，以取得最好的效果。求最大流的标号算法最早由福特和福克逊于1956年提出，20世纪50年代福特(Ford)、福克逊(Fulkerson)建立的“网络流理论”，是网络应用的重要组成成分。

## 最小费用流问题（Ford-Fulkerson 迭加算法）

- 输油管道，每个管道有运油量约束和成本，现在要从一个出发地运送特定数量的油（小于最大流的数量）到某个目的地，怎么运输，让成本最小。

1. 数学模型
2. 标号算法
3. 具体求解
4. 用它来表示其他问题

- 思路：尽可能发挥费用少的链路的潜力，寻找一条从i到j的费用最少的链路，并使得它的潜力充分发挥出来，直到达到运输数量要求； 总是在费用最小的增广路上增加流值，直到流值达到v。
- 标号算法
1. Dijkstra算法先找到最短路（也就是费用最少的路），用所有边上弧容量最小的；
2. 调整容量
3. 对所有弧，如果是饱和的，就设置原有的弧反向，如果不饱和，就设置一条反向负权弧（权重为费用）
4. 重复1-3操作，不过找最短路时候可以用枚举法操作结束的标志就是再也不存在一条从起点到终点的最短路；
      1. 注意：如果遇到了逆向流，流量最小值要用其原本的流量大小进行比较；

!!! Tip
    Ford-Fulkerson 的核心在于“塑造反向弧”，给了一个“纠错”的空间。使得一个已有的（但是效果不那么好的）可行的解可以在后续找的过程中被优化；

### 用最小费用流表示其他问题的建模

- 运输问题：直接设置一个汇总发地和一个汇总收地，只不过从汇总发地到原发地、原收地到汇总收地的费用全部是0；
  
- 指派问题：设置虚拟头和虚拟尾；每一个人到一个任务的容量都是1，费用即为成本；虚拟头到每个人、虚拟尾到每件事的容量也是1；

- 最短路问题：同指派问题，容量设置成1；起点供应节点设置一单位，需求供应节点设置一单位；
- 最大流问题：头和尾之间连接一条成本$M$的线路

