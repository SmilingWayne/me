# 智慧物流

## 0918 Class 1


!!! abstract "概述"
    要求：前面会讲一些理论，有一些深度，后面会有具体的优化问题VRP。具体的考核方式：每个人写一个代码，解决这个问题，把自己的算法在汇报中讲清楚（每个人独立完成）

    - 每个人7～8分钟；老师会问一些细节的问题：要花点时间好好学一学。
    - 往年情况：从网上找下来改的。今年开始不能这样找。如果是从网上找的，要搞清楚代码里的所有细节。要认认真真的练习写代码。
    - 没有期末考试。
    - 这门课的前身：**运输与配送。**

> P.S. 物流的：如果模型是有问题的，答辩是不过的。
> 
> - 物流这个专业不适合在好的学校开，尤其是本科学校。一些概念性、流程性的课程不需要在学校里讲授。在这门课上需要讲得深一点。
> 
> - 目前物流很重要 -> 大公司。利用技术手段解决经典问题。
> - 学习一些方法论，可以用到不同的领域；
> - ==难度挺大的==，要有技术的积累。如果你经过短期培训就可以入门，那么说明会有很多的进入者进行竞争。（like data analysis）
> - “沟通业务和算法桥梁的人” -> 现在比较稀缺的人：业务和算法的结合。（要学习 ：哪一类业务需要用哪些算法求解更好？==要知道==。）
>
> **不要按照专业来给自己设置限制。** 要做什么事情跟你掌握了什么方法论相关：对技术有热情的，方法论层面的。
>
> - tips: 毕业选题：要确保目前没有原原本本做过：比如来自企业实际的情况；一些提问：为什么用这个模型？为什么用这个算法？毕业要有一定工作量。

NVIDA的求解VRP问题的求解平台。

!!! note "一些问题的介绍"
    **车辆路径问题**：给定仓库，一组顾客和一个车队，为车队的每一个车规划服务顾客的行驶路径，最小化路径成本。

    - 应用很丰富，难度又很适中。
    - 学术价值很丰富。

    求解方法：用GA这种黑盒算法做的话，就只是黑盒；整数规划也可；

    **三维装箱问题**：给定一组物品和一个箱子，要求在满足约束的前提下尽可能多地把物品装入箱子，最大化箱子的空间利用率。

    **制造业企业智能车辆调度**： 替换人力排车的老方法。提高配送效率，降低成本。

    > 车先到仓库（多点提货、多车型、车是否需要多行程、考虑司机优先级）再到订单卸货点（客户的时间窗、软时间窗和硬时间窗）再回去。这个流程。
    > 
    > - 时间窗约束: 和传统不同；


    **制药企业的多模式运输优化**： 多种运输方式（空运、陆路和快递），Q1：来一批订单，哪些空运陆运，这要综合考虑时效和成本的业务情况。Q2：发货仓库的选择约束。

    > 时间窗：几乎是一定要被考虑；容量约束（药物等特殊物品）；里程约束；运输计费方式；

    **沃尔玛商用超市的配送优化**： 2B（货物运到超市）和2C（货物到客户）

    > 考虑车辆在月台的等待时间：前一个车的时间影响到后一个的时间。（解耦）
    > 
    > 订单拆分的情况（要和路径之间形成配合）
    > 
    > **有效容量约束，** 一个隔板也会影响车辆capacity，车辆的容量也和去的门店的数量有关。
    > 
    > 复杂的时间窗约束；

    **华为三维装箱的优化**：11种不同的约束；

    **跨境物流网络的优化**（联想）：问题 = 网络规划 + 三维装箱。提供了不同场景去勾选，如果没有这个场景，可以选择一个接口去自己设计；

TMS：交通运输管理系统
WMS：仓库管理系统
BOL：Bill of Logistics (类似BOM)


> 价值：
> 
> 1. 获取企业实际数据的；
> 2. 有实际意义；


--------

## 0925 Discrete Optimization

!!! note "preliminaries"
    - Graph Theory / Linear Programming  / duality problem


!!! note "Overview"
    $P = \min f(x), x \in F$， x 是一组向量，$f$是目标函数；如果 $F \neq 0$， 说明有可行解

    $f(x^*) \leq f(x), \forall x$，最优值；

    $z(P)$：最小的目标函数值。$z(p) = \infty$，不可行, $z(p) = - \infty$，无界解


    ----------

    $$\min f(x) \\
    s.t. \begin{align}\begin{equation*}
    \begin{cases}
    g_i(x) \leq 0, i = 1,...,m \\ 
    h_j(x) = 0,  j = 1,...,p \\
    \end{cases}
    \end{equation*}\end{align}$$

    1. Non-linear Programming (More complex)
    2. Convex ~(Complex)
    3. Linear Programming(Medium)

    ------

    ### 离散优化、组合优化

    $f, g_i, h_j \text{ are linear}, x \in \text{Integer}$

    组合优化：从集合里选择一些元素出来，（选择很多）求使得成本最小的一个 **“组合”**；

    $N = \{1,2... n\}$, finite set.

    $c: n \rightarrow R$ cost functions

    $\mathbf{F}: 2^N$ : 可行集合；

    $w(S) = \sum_{i \in S} c_i$

    Combinatorial Opt Problem: $\min w(S): S \in \mathbf{F}$

    ------------


    IP problem: 

    【建模表示同上，略过】

    MILP：

    【建模同上，略过】


!!! note "TSP"

    $N, (i, j), c(\{i, j\})$：每个城市都是从 $N- 1$ 个边里面选（ $N$ 个城市到其他点的路径构成一个集合，从这个集合里选一个路，和其他 $N- 1$路构成一个“组合”。但是有成环约束；


    $\delta$ 的定义是什么？一个点在这集合里头，一个点不在这个集合里头；

    > 跟这个点相邻的边，一共有两条边；
    > 
    > **子环消除约束**


    $$\min \sum c_e x_e \\
    \text{s.t. } 
    \begin{aligned}\begin{equation*}
    \begin{cases}
    \sum_{e \in \delta(\{h\})} x_e = 2 , \hspace{10pt} \forall h \in V\\
    \sum_{e \in \delta(\{S\})} x_e \geq 2, \hspace{10pt} S \in V, | S | > 2\\
    x_e \in \{ 0, 1\}
    \end{cases}
    \end{equation*}\end{aligned}$$

    $|S|$ 表示集合中边的个数；


    --------------


    ### 另一种技巧

    
    $y_j$ 是这个节点在最终回路中的位置：消除子环约束的时候怎么保证  $x_ij = 1$ 的时候$y_j= y_i+ 1$： 
    
    $y_j \geq y_i + 1 + (x_{ij} - 1)M$ ；这个约束只有 $N - 1$ 个，因为最后一个节点不需要有这个约束；

    - 实际上计算角度来说更好的是上面那个约束更多的模型：因为加了大 M 的算法计算效果普遍不好；因为 $x_j$ 被松弛之后， 这个约束就没用了。

    在这种TSP问题中，模型中一定有一个变量是在表示，随着路径发展不断递增的记录；



!!! example "指派问题"

    $N$ 人 assign 到 $N$ 个任务，总成本最小；

    解的个数 $n!$

    **Advanced: 带容量约束的指派问题。难度就会高一点**。

    问题建模:
    
    $$\min \sum \sum c_{ij} x_{ij} \\
    s.t. 
    \begin{aligned}\begin{equation*}
    \begin{cases}
    \sum_j x_{ij} = 1, \forall i \\ 
    \sum_i x_{ij} = 1, \forall j \\
    x_{ij} = \{0, 1\}
    \end{cases}
    \end{equation*}\end{aligned}$$


    --------

    引入变量 $y_i$ 表示这个节点在环里的位置（借助无向图改成的有向图）

!!! note "0-1 Knapsack"

    问题略过；

==从理论上的问题难度角度说，指派问题（P问题）的难度要简单很多。背包问题是更难的问题。== 虽然实际上可以解得很快；


!!! note "Packing && Cover"

    N 是有限集，M 的每个元素都是 N 的一个子集； M 是其中子集的下标的集合；

    $S \in M$ is a cover ：相当于从 M 中选中几个元素，这些元素的并集恰好可以把原来的N中的所有元素都覆盖住；

    $S \in M$ is a packing：如果从M中选中的子集互相之间是不相交的，那么称这样选中的子集是一个packing。

    如果一个选中的集合既是packing又是cover，说明S是个partition。


    - 最小权重cover问题； w(S) 越小越好；同时也是Cover；
    - 最大packing问题： w(S) 越大越好；同时也是packing；


### 整数规划的建模


!!! abstract "Abstract"
    1. Modeling with Integer Variables Modeling techniques
    2. Modeling with Exponentially Many Constraints（指数级别的约束）
    3. Modeling with Exponentially Many Variables（指数级别的变量）
    4. Notes and References
    5. Bibliography


!!! info "Techniques"
    
    0-1 Binary variables： 
    
    > - Yes or No
    > - 两段不连续的集合；
    > - 包含 “if”这种逻辑决策的话： if ..., then constraint ... 
    > - fixed cost: 选址产生的固定成本；
    > - 分段线性函数；

!!! info "notation"

    - weight of subset S of M: \sum_{j \in S} c_j
    - 某个 $N$ 里的元素 $i$ 出现在 $j$ 指定的子集合里的话，就取 1，否则是 0 （incident matrix） $[ a_{ij} ]$, $n \times m$，每个矩阵元素都是一个0-1变量；

    1. Set Covering Problem: 

    $$\min \sum c_j x_j \\
    \text{s.t.} \hspace{5pt} Ax \geq e$$

    2. Set Packing Problem:

    $$\max \sum c_j x_j \\
    \text{s.t.} \hspace{5pt} Ax \geq e$$

    3. Set Partitioning Problem:


!!! info "forcing constraint"
    
    不带容量限制的选址问题。(UFLP)

    （可以选择的地址）$N = 1,2,3... , n, M = 1,..., m$ (服务的顾客)

    仓库有固定成本 $f_j, \hspace{5pt} j \in N$，考虑运输成本  $c_{ij}$ , 对顾客的需求做了正则化之后，把需求压缩成1.

    $$\min \sum\sum c_{ij} x_{ij}  + \sum f_j y_j \\ 
    \text{s.t.}
    \begin{align}\begin{equation*}
    \begin{cases}
    \sum x_{ij} \leq y_j f_j \\ 
    \sum_i x_{ij} = 1, \forall j \\
    0 \leq x_{ij} \leq 1 , \hspace{5pt} \forall  i \in M, \forall j \in N     \\
    y_j \in \{0, 1\}
    \end{cases}
    \end{equation*}\end{align}$$


!!! info "Disjoint Constraints"

    x 决策变量；

    $ax \leq b, cx \leq d$, 可以同时满足，但是至少要保证一个是可以满足的；

    引入0-1 变量 y：

    $ax \geq yb \hspace{15pt} cx \geq (1 - y)d$，前提是 a, c必须是非负的

    $\sum y_i \geq k, a_i x \geq b_i y_i$： $y_i$ 是 0-1 变量， 至少有 $k$ 个条件满足；


!!! info "分段线性函数"

    用一系列有序数对进行分段线性化： 利用拐点进行表示；

    用 $y_i$ 整数变量查看传入的变量究竟输入哪一段。

    对lambda 也做了正则化处理。

    如果分段线性函数是凸的，此时不需要引入0 - 1整数变量，只需要取最大（？）



## 1009 


### CVRP 问题（基于边的建模）

一条路径上的总需求不能超过车辆的最大容量。

目标函数：最小化车辆走的距离的和。

!!! note "如何建模"

    写论文时候，一定要找到最接近自己的论文的问题：可以借鉴别人建模的方式。

    x_{ij} 在和仓库相邻的边下可以取2。（路径 0 - 1 - 2 - 0）

    子环消除约束 = 看作是TSP的子环消除  + 容量约束；这个约束更强（判断强弱的方法：定义的可行域的范围的大小）
    
    > 这里右边的取值是 >= 1 的，比TSP的 = 1 要更大（考虑了CVRP的特定问题的约束形成了更强的约束）


### Cutting Stock Problem 

基于Pattern 的方式进行建模：给定一个长条的木块，一个可行的切分方案。


### CVRP的另一种建模方式

基于集合的建模方式：用 a_{il} 表示路段i是否出现在路径l中；

约束1:保证每个节点要被访问一次；
约束2:路径的数量 = 车辆的数量；

容量约束不是显式的表示：R 是可行路径集；我们把一部分约束放到定义里了；



### 计算复杂性理论

精确算法：保证求到问题的最优解；

启发式算法：不能保证理论的最优解；经过设计可以返回一个可接受的解；（答辩时候不能说自己达到了最优解！只能说“找到最好的可行解”）

> 论文的实现细节往往不会讲，但是实际上实现是最难的，也是挑战最大的；（对函数做优化）
>
> 可能大作业是装箱：一些类似的种群算法效果就会很不好；

------

算例、算例规模、复杂度（完成所有计算的次数）、最坏情况下的复杂度；

> Big O notation：忽略一些常数；考虑在规模充分大的情况下主要的项（指数最高的那个项）
>
> - 多项式时间：O(N^2)
> - 指数时间

指数时间的是对算法敏感。而启发式算法对问题规模不那么敏感；（不同算法对问题规模的反应是不同的）

----------


NP-complete：是用在决策问题上的（就是结果只有Yes 和No），CVRP就不是一个NP-Complete问题。

背包问题化成决策问题的表示：（11）

决策问题可以分成两类：P问题和NP 问题 ，这两个问题都是和多项式算法相关的。

P：存在一个算法，在多项式时间内可以给出决策问题是Yes还是No。
NP：存在一个多项式算法，可以检验决策问题的答案是否是Yes（给定一个问题和一个解，我可以在多项式时间内判断yes还是No）

$P \in NP$


-------

NP-complete和NP-hard

归约：P1是问题P2的一个特例（special case）：我们就说P1可以归约到P2（具体描述就是给定一个P1的算例，我们总可以把它转化成P2的一个算例）

> P1是TSP，P2是CVRP，TSP可以归约到CVRP

P2是NP-complete的，如果存在一个算法求解

NP-hard 问题：对应的决策问题是一个NP-complete问题；这是用来描述优化问题的。

> CVRP是一个NP-hard问题 ✅
>
> CVRP是一个NP-complete问题 ❌
>
> CVRP是一个NP问题 ❌ 这两个都是涉及决策问题的

### 图论

!!! note "概念"
    基本概念：有向图、无向图、loop, vertex, arc, 带权图, 割集（出去的边、进来的边）, Path（路径），简单路径（不存在一个边经过超过1次）、基本路径（elementary）每个点经过不超过一次、Nonelementary path：允许一个路径经过超过1次、欧拉路径（及其权重）、曼哈顿环（经过所有点并且只经过一次）、部分图（点一样但是边只用一部分）、==子图==（用的更多）、联通图、强联通图、有向无环图（许多算法都可以大大简化，比如找任意两点的最长路径，拓扑排序）、邻接矩阵、关联矩阵（incident matrix，针对有向和无向图的）


$\begin{vmatrix} 1 & 2 & 3 \\ 1 & 2 & 4 \end{vmatrix}$

## 1016 



!!! note "基础"
    欧氏空间、线性组合、子空间、线性无关、基、秩、逆、奇异/非奇异、增广矩阵、线性方程组解的个数、凸集、严格凸组合、极点的定义、超平面、half-space（半空间）、多面体（Polyhedra）、Polytope（有界的Polyhedra）、cone（锥）、方向、

    > 几何展示


- Lemma-1： 多面体是一个凸集；

- 表示定理：线性系统中的一系列极点和极方向把域表示出来（凸组合的形式），两种表示方法在 LA 中是等价的。
- 极点和最优解的关系（如有最优解，一定包含）
- 基本可行解、退化的情况、退化在收敛速度变慢的时候怎么办、

> 建模的时候，有的约束条件可能是冗余约束；（不是最有效的模型）
>
> 极点的数量比基本可行解的数量要少一点。（因为一个极点可能对应多个基本可行解，退化的情况）

--------


- 单纯形法回顾

- Reduced Cost：

- 基变量、非基变量、出入基操作

> 求逆矩阵的时候是最耗时间的；

> 循环的情况什么时候会循环：几何上表示为在同一个点上一直在绕绕绕


------


### 对偶问题

- Farkas Lemma .1  很重要的工具； 意思是如果 $c_0 \leq cx$ 是可行的，那么意味着能找到一个 $u$， 满足 $c \geq uA$ 以及 $c_0 \leq uB$ ， 这里的 $c$ 是向量，$c_0$ 是值；这是一个充要条件；

通过Farkas Lemma引出对偶。因为对偶问题的形式可以从原始线性规划问题构造。

> 看一下几何表示。

!!! note "对偶问题的写法（不用记表）"

    用拉格朗日的方式构造对偶：

    $$\min cx \\
    \text{s.t.}
    \begin{aligned}\begin{equation*}
    \begin{cases}
    Ax = b \\ 
    x \geq 0
    \end{cases}
    \end{equation*}\end{aligned}$$

    把拉格朗日乘子罚上去：

    $$\min cx + \mu (b - Ax) \\
    \text{s.t.} 
    \begin{aligned}\begin{equation*}
    \begin{cases}
    x \geq 0 
    \end{cases}
    \end{equation*}\end{aligned}$$

    -----

    改写一下： $\min (c - \mu A)x + \mu b$

    是要求拉格朗日函数的下界；如果 $c- \mu A$ 是 $< 0$ 的，此时目标函数就可以无限小了（因为 $x$ 非负），就必须约束 $c - \mu A \geq 0$

    $\max L(\mu) = \mu b , \mu A \leq c$

    对偶问题的约束的系数是大于还是小于，主要看决策变量的系数，不需要看表；

!!! note "强弱对偶性"
    看PPT！


!!! note "互补松弛性"

    列生成，我已经加了一个新的列进去了，为什么还会有检验数是负数的？

    > 因为你的代码是错的。这一列不应该加入进去。

------

### 对偶单纯形法


## 1023 不同的建模方式（Alternative Formulations）


整数规划

表示定理：两种表示方式。


### Uncapacitated Lot-Sizing Problem 

$f_t$：在 $t$ 周期是否生产
$p_t$：在 $t$ 周期的单位生产成本
$h_t$：单位库存成本；
$d_t$：在 $t$ 时期的需求


----------

### 1030 Branch and Bound // Cutting Planes 

Branch and Bound: 把整数规划问题进行分解。目的是让目标取值一定要是整数。对凸包，关注优化方向相关的区域。

Cutting planes: 把优化方向的非整数部分切割掉。（有效不等式 -> 得到更强的模型和更好的界）

对系数全部 除以一个正整数，并且向下取整。（有一个数学证明）


CUT!

所有的有效割平面可以通过同样的方法得到。

- Clique Cut. 

$$\begin{aligned}\begin{equation*}
\begin{cases}
x_1 + x_2 \leq 1 \\ 
x_2 + x_3 \leq 1 \\ 
x_1 + x_3 \leq 1 \\
\end{cases}
\end{equation*}\end{aligned}$$

有：$$x_1 + x_2 + x_3 \leq 1$$

【补充一张图】

如果冲突图是完全的，那么就构成了Clique Cut（团割）


$$\min \sum_{p \in P}c_p x_p \\
\text{s.t.} 
\begin{aligned}\begin{equation*}
\begin{cases}
\sum a_{ip} x_p = 1, \forall i 
\end{cases}
\end{equation*}\end{aligned}$$

**subset row inequality**


$$\sum \frac{a_{ip} + a_{jp} + a_{kp}}{2} x_p \leq  3/2, a_{ip} \in Z$$

如果P属性中3个有至少2个是1，那么 $x_p$ 就一定要选。


## Cover Cut 

$$\sum a_i x_i \leq b, a_i, b \in Z, x_i \in \{0, 1\}$$

$$7x_1 + 6x_2 + 5x_3 + 4x_4 \leq 12$$ 

有： 
$$\begin{aligned}\begin{equation*}
\begin{cases}
x_1 + x_2 \leq 1 \\ 
x_3 + x_4  +x_5 \leq 2
\end{cases}
\end{equation*}\end{aligned}$$

进一步地，有 $x_1 + x_2 + x_3 + x_4 \leq 2$。升维操作。


e.g. 

$$7x_1 + 8x_2 + 6x_3  + 4x_4 + 6x_5 + 5x_6 \leq 24$$


$$\begin{aligned}\begin{equation*}
\begin{cases}
x1 + x2 + x3 + x5 \leq 3 \\
x_1 + x_2 + x_3 + x_4 + x_5 + x_6 \leq 4
\end{cases}
\end{equation*}\end{aligned}$$


