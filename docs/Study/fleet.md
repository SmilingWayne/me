# 2023 暑期学校笔记

!!! warning "备注"
    一个非常不专业的笔记。而且刚刚入门，啥也不知道。

## 07.07 Morning

!!! note 
    - 拥挤收费
    - 电子路票
    - 香港的交通实践
    - 强化学习AI


> FSD:Tesla 的FSD系统，[完全无人驾驶系统](https://zhuanlan.zhihu.com/p/365142565)。


- 感应控制的红绿灯🚥
    - 诱导需求：数据表明新修的路越多，堵车越严重。
    - 美国不同城市新修的公路数量，以及同一时期这些城市的车开的里程数。它们之间正好是一对一的关系。
    - 新的公路会催生新的司机，其结果就是交通堵塞永远无法缓解。
    - 答案与马路的功能有关：四处移动。事实上，人类喜欢四处蹿。
    - 增加公共交通和改善信号控制会缓堵么？

- 交通拥堵是大量离散有限的智能体在个人利益至上的原则下，又在资源有限条件下，自由地、非合作地博弈出行的结果。


> 拥挤收费：
- 拥挤收费是指出行者在进入交通拥挤区域对，必须支付的那部分道路拥挤费用。用于补偿由于该交通出行者的加入而给社会带来的外部成本，通过提高出行成本，促使出行者重新选择自己的出行行为，减少交通需求的一种交通需求管理措施。
    - 和高速收费站不同
    - 通过费用来调整交通的需求
- 拥挤收费目标是减少收我区域的交通拥济，减少行程时间，提高可靠性，鼓励小汽车出行者在拥挤区域选择其他交通工具出行。

> Braess 悖论

- [ ] 网络达到均衡时候的充分条件（equilihrium)：是一个中长期的概念
- [x] 达到均衡的时候所有人都没有意愿改变自己的选择
- [x] 三条路的走行时间是一致的




--------


SC & OM 中的随机动态优化

Vehicle Route Problem
* sourcing：外包/采购
* SHEIN：跨境电商
* revenue management: 收入管理（易逝性：容量有限（比如库存、航空的座位）；支持提前预定，导致一个座位在距离起飞10天/1小时的机会成本是不同的，资源的稀缺性，机会成本会发生变化）
*  multi-armed bandit problem 老虎机


- 厂区物流送货
- 工厂路径规划
- 背包问题
* 汽车租赁市场


## 07.07 Afternoon

Deterministic Model

- 线性整数规划。

1. Aviation Planning Problems
    1. Schedule Design Problem. (Tactical)
    2. Fleet Assign Problem. (Tactical)
    3. Aircraft Routing. (Operational)
    4. Crew Scheduling Problem
    5. 
- [x] FAP: 
- Input: 
    - A set of legs / fleets
    - A set of fleets for each fleet we know the num of Aircrafts
- output：
    - Assign each leg a fleet
- Assumption:
    - The scheduling is repeated daily(weekly)
- Objective:
    - Max profit && min costs
    - Max / min \sum \ sum x_{ij}; s.t. \sum_j x_{ij} \geq 1 \forall i \sum_i x_{ij} \leq 1; \forall j
- Questions: 
    - 不同的flights 之间是有关联关系的；传统models不可行	
- [x] Time-Space Network：时空网络
- G(N,E)
- Node: N marked by n, represent a takeoff or landing at an airport.
- Edges: 
    - Flight edges: 代表航班
    - Cycle edges: 代表在地面的(aircraft stay on the ground)
    - Warp around edge：aircraft stay overnight

----------


|  Col  | Dep-station | Deptime | ArrS  |  Arr  |
| :---: | :---------: | :-----: | :---: | :---: |
| $f0$  |    $s1$     |  7:00   |  S3   | 10:45 |
| $F1$  |    $S1$     |  8:30   |  S2   | 10:30 |
| $F2$  |    $S2$     |  10:30  |  S3   | 12:10 |
| $F3$  |    $S3$     |  13:15  |  S2   | 14:55 |
| $F6$  |    $S4$     |  7:00   |  S3   | 11:00 |
| $F7$  |    $S3$     |  13:15  |  S4   | 17:00 |

> 这个network对应一个机型的network，一种飞机（A320，787）就对应一个network，有几个机型就几个network。


$F1， F2， X_{fk}:  f: \text{leg}, \text{flight}; k: fleet$

$$\min  \sum \sum C_{f,k } X_{f, k} \\$$ 


$$\left\{ \begin{aligned}
\sum_K x_{f, k} & = 1 , \forall f \\
x_{f, k} \in N^+:&  在\text{f} 天空中的飞机的数量\\
y_{g, k} \in N^+: & 在\text{ground}的机型的数量  \\
y_{g4, k_1} & = y_{g1, k1} + x_{f_0, k_1} \\
y_{g_4, k_2}&  = y_{g_1, k_2} + x_{f_0 k_1} \\
y_{g_9, k_1} & =  x_{f_3, k_1} + x_{f_7, k_1} + y_{g_ {10}, k_1}\end{aligned} \right.$$


$\sum x_{f_{n^+, k}} + y_{g_{n^+},k} = \sum x_{f_{n^-,k}} + y_{g_{n^-}, k}$

- $f_n^+$ : in node；
- 三组constraint：
    - 第一组：
    - 第二组：流入 = 流出的情况
    - 最后一组：对于任何一个time，飞机总数要小于总共的飞机数；$\sum x_{f,k} + \sum y_{g, k} \leq N_k, \forall \text{Time}$


- 入 = 出的，可以consolidate，降低 node 的数量； （node abbreviation），变成一个Node
    > 可以降低模型的系数 
    - 但是要注意是否feasible，连续降落三个再连续起飞三个，和连续起飞3再连续降落3时不可以consolidate，因为可能出现地面数量为负数的情况。


> 单纯形法中是约束还是变量对求解的速度影响更大？
>  - 是约束：因为要求逆矩阵；你总需要求一个$B^{-1}$，这需要一个$O(N^3)$的复杂度 

-----

1. Two constraints
- Update：一些航班必须飞，一些航班可以不飞。
> spoke: 小机场（车轮辐条）：如果一天内先起飞再降落，这样不好，因为有个飞机是一直降落在机场等待起飞的。
> - 如何通过微调航班的时间来规避上面的情况？加入dummy的情况；
>
> 不同飞机的气压还不一样？
>
> 
$\sum x_{f, k} = 1, \forall \text{Core flights}$;

$\sum x_{f, k} \leq 1, \forall \text{Optional flights}$

----------------


2. Multiple Possible Departure


- 连乘航班不同航程的定价？


$\sum x_{f, k_t} \leq 1, \forall t \in \text{all dummy nodes}$

!!! note "Itin-based FAM"
    - $\xi_i$ Number of psgs for itin i
    - $P_i$, ticket price for itin i  
    - $\text{Dmd}_i$ demand i

【补充】

s.t. 
$\sum x_{f, k} = 1 , \hspace{5pt} \forall \text{flt}$

$\xi_i \leq \text{Dmd}_i$

$\sum_{\text{i conains fleet f}} \xi_i \leq \sum \text{cap}_k x_{f, k}, \forall \text{fleet}$

> e.g. $\xi_{AB} + \xi_{AC} \leq 100 x_{f,k_1} + 200 x_{f, k_2}$

- demand 有transfer的过程：如果A-C卖完了，肯定会找A-B-C的过程



------------


- 在某地可以多拿到一个时刻，计算这个时刻“值多少钱”：用“影子价格”
- 多买多少架飞机？ 客 公里
> 大城市之间增长的多：买大飞机，二三线城市：买小飞机。
>
> 考虑飞机折旧和增加的情况？（没懂）

- FAM : Yr. 1 ; $\leq \text{Num}_K;  \forall \text{fleet}$
- FAM : Yr. 2 ; $\leq \text{Num}_K + W_K$



-----------

- weekly schedule：建立一个周的network，把原来的横轴拉长。从周日的最后一个航班到周一到第一个航班：规模变大了。


- schedule consistency：每周的相同航班用不用同一个机型去飞：用同一个机型。



$\sum_k \mu_{\text{fm}, k} \leq 1;  \mu_{\text{fm},k} \in \{ 0, 1\}$

$x_{\text{fm},k} \leq \mu_{\text{fm}, k}， \forall f, \text{fm}$

---------

- 希望在一个station的机型的数量越少越好；尽量不要出现由少换大和由大换小，不然备降维修需要额外花很多成本和调度
> low cost carrier（LCC）
>
> 春秋航空的perfec margin非常好，因为全是同一个机型。

$V_{s, k} \in \{0,1 \}$

$x_{f, k} \leq V_{s, k}$

$\sum V_{s} \leq \text{purity}_s$，限制某个地区的机型的数量；



------------


## 07.08 Afternoon


- Ground Crew Scheduling
> Above wing（办票的、服务人员）、 Under wing（搬行李的）
>
> 1. Shift Planning （排班？）
> 2. Task Assignment（一系列工作，分配给上班的人）
> > 
Tasks （$I$）; Crews $x_{ij} \in \{ 0, 1\}, X \in J$

task 开始/结束的时间：$[ t_{i^-} , t_{i^+} ]$

task：人员开始上班 / 结束的时间：$[ t_{s^-}, t_{s^+ } ]$

$\min \sum \sum c_{ij}x_{ij}$

s.t. 

一、$\sum_{j \in J} x_{ij} = 1, \forall \text{task}_i$ (每个任务都要被分配)

二、如果两个task时间是重叠的，就需要满足：$x_{i_1j} + x_{i_2j} \leq 1 , \hspace{4pt}  \forall j$ （最多有$C^{2}_{n}$ 个约束，$n$是$\text{task}$数量，这个约束最多）存在时间冲突的任务，每个人只能解决其中一个。

!!! note "Conflict Graph"
    ?【待补充图】 有冲突的task之间相互连接起来。

    在图中要找“团”（clique），这个团的每一个node都和其他的node都是相连的。（完全图），这个clique需要“尽可能地大”，而且会包含其他的clique在内。

    > 物理意义：clique中是存在时间冲突的。一个人在一个maximal clique中只能选择一个task。
    > 
    > maximal clique: 大的clique 

$x_{t_1 j} + x_{t_2 j} + x_{t_3 j} \leq 1, \forall j$

$x_{t_2 j} + x_{t_3 j} + x_{t_4 j} + x_{t_5 j} \leq 1, \forall j$

...，可以按照clique来设置constraint。

- ❓最多会有多少个clique呢？🔑🔑：最多有$t$个clique（有且仅有两两之间重叠的情况）
> 概念：Chrodal Graph
>
> 证明：把 $\text{start}$ 和 $\text{end}$ 投射到直线上。遇到$\text{start}$就意味着一个clique出现了。
>
> 最终有2n个点。至少两个才能形成chroal。所以：n；

$t_1 + t_2 + t_3 \leq 3/2$

$t_1 + t_2 + t_3 \leq 1$： 这个约束效果要好于对两两之间进行约束的情况


> facet defining: 约束是最强的。
>
> - 最少需要的人数：4个，和最大的clique的大小是相同的。
> - maximum clique：决定了完成任务最少需要多少人。复杂度$O(N\text{log}N)$（基于task的start和end排序）如果是直接按照图来看，是$N^2$

-------------

- 📒📒 **一些特殊的情况**
- 分了$\dfrac{T}{N}$ 堆，每一堆里有$N$个$\text{task}$, 每个node都可以和其他部分的所有node相连。
> 问：图有多少个maximal clique 有$n^{\frac{T}{N}}$个 maximal clique。是一个指数函数
>
> - 3^{1/3} 是所有的 $N^{1/N}$ 是最大的。
>
> - 对一个一般性的graph，number of clique 是指数增长的，只有对于perfect graph的，才是小于N的。

-------------


### Extension 1 ｜ travel Time

- Travel Time：不再是一个perfect graph， num of clique 可能是指数情况的（exp）
> task1和task5是否在同一个地方。


### Extension 2 ｜Qualification

- 不同的工作用的汽车，不能负责其他的功能。要分配任务，这种qualification一定需要match。记作 $q \in Q$

- $\text{task}_i, Q_i$,每个任务有一个资质需求，满足一定资质才能做这个需求。

!!! question "东航的问题"
    一旦一个qualification的人生病了，很难去替代。（比如一个task人需要同时拥有3个不同资质$Q_1, Q_2, Q_3$才可以），这种情况下最好有两个人同时拥有$Q_1, Q_2, Q_3$ 两个资质才行

    - $\text{task}_1: Q_1,Q_2, Q_3$
    - $\text{task}_2: Q_1,Q_3, Q_2$，可以对比昨天$\text{purity}$的问题，这时候可以把task1的Q3移到task2，把task2的Q2移到task3.


- 解决方法：引入新的变量：$w_{jq} \in \{0,1 \}$： $j$ 这个人需要的资质

$$\sum_j \sum_q w_{jq} \geq x_{ij} , \hspace{6pt} \text{if i need q}$$


$$w_{j_1q_1} \geq x_{i_1j_1} \\ w_{j_1q_2} \geq x_{i_2j_1} \\ w_{j_1q_3} \geq x_{i_3j_1}$$


### Extension 3  Lunch Time

- Lunch Time: $[t_1, t_2]$, $[t^{'}_1, t^{'}_2]$, $[t^{''}_1, t^{''}_2]$
- 把午餐时间也变task，或者所有和task有冲突的task全都不能安排；
- 这三个shift里面只能选一个

$$x_{ij^{'}} = 0;\\ y^{'}_j \in \{0, 1\}, \\y^{''}_j \in \{0, 1\}, \\y^{'''}_j \in \{0, 1\},  \\\sum y^{'}_j + y^{''}_j + y^{'''}_j \leq 1$$
> 因为人可以不吃饭，所以可以小于等于1

### Extension 4 Flexible Shift Time




- 希望排的人的数量和任务的数量最好是严丝合缝的，但是会少于最高峰：减少浪费。

> - 国外的方案：雇人来办事
> - 国内的方案：压缩前面的工作时间干后面的活；或者画一个可以覆盖的大方格。【补充一张图】

- 现在：灵活上下班服务，高效完成工作
> create 很多shift，shift的cost和持续的时间有关；
> 4，5，6...10点上班，10，11, ... ，下班，每个人只能选择其中一个shift
>
> 一个$j$，早4:00～10:00，4:00～11:00；4:00～12:00，这三种情况都属于同一个$j$，$j^{1}_{1}, j^{2}_{1}, j^{3}_{1}$
> 
> 对于每一个班期 $\sum x_{ij} \geq 1, \forall \text{task}$，
> 
> $\sum_{i \in MC} x_{ij} \leq 1, \forall MC, \forall j$ 

- MC: maximal clique
> $y_{j1} + y_{j2} + y_{j3} \leq 1, \forall j_1$
> 
> $y$：这个shift有没有被用， $x_{ij_1} \leq y_{j_1}$


------------


### Extension 5 ?

$$\min \sum \sum c_{ij} x_{ij} + \sum c_j y_j + ... + Wa$$

$$s.t. \left\{ \begin{aligned} \sum x_{ij} & \geq 1, \forall \text{task} \\ \sum x_{ij} & \leq 1, \forall \text{MC} ; \forall j  \\ x_{ij} & \leq y_j\end{aligned} \right.$$



> 问题： 有很多shift 怎么减少？

- 对时间相同的combine起来。但是如果时间不完全相同，不能通过解relaxation找到原方案的。

!!! question 
    先combine一下求得一个下界？

    先产生12～15个邻居，产生很多级进行combine。

    大量的constraint可以被联合在一起从而得到结果。（Associate Clique的概念）

    CONFUSED


---------------


## 07.09 Morning

1. Fleet Assignment 
   1. Aft Routing
   2. Crew Scheduling
2. Ground Crew 

!!! question "Fleet"
    我们知道每一架飞机具体的routing是什么吗？

    - No，飞机机型的assignment


- Input： 知道每一个机型的航班
- Output： 确定每一架飞机具体的飞行路径。
> 确定了Assignment之后，一个fleet构成了一个欧拉图。

!!! quote "欧拉图（Eular Tour）"
    - 哥尼斯堡七桥问题 ｜ 一笔画问题，只用一笔把所有的边连接起来。
    - 结论：对于欧拉图，寻找欧拉回路，算法是多项式复杂度$\theta(E)$ 
    - TSP：要回到起点，每个点都要遍历一次，变成NP-hard问题。
    - 如果对于欧拉图，允许重复，但是需要重复的尽可能少：变成中国邮递员问题。
      - Node routing：（service在节点上）
      - Arc Routing：（Service都是在arc上）

- tactical routing：每个飞机的routing是固定的。
- 1-6-2-3-4-5，两架飞机都要保持这个路线，因为**可以确保两个飞机的飞行强度是相似的**。
    - 要设计大一点的环，让飞机尽可能一直在天上飞。
    - 一天一架飞机要飞10h左右才能让航空公司不亏。一架Boeing 737 在地面停一h，大概有2w成本。

> 如何判断欧拉图：
>
> - 如果对于无向图，看度是多少。如果一个node 的度是3（不是2，不是有进有出的）
> - 对于有向图，对每一个node，都有入度 = 出度，那就一定存在Eular tour


> 如何找欧拉回路：
> - Greedy + backtrack，一旦有没访问过的，就回溯到前一个，直到把所有的node都访问完毕
>
> - 最坏情况：2E

  
-------

### A basic 3-Day routing problem

> $A_1, A_2, A_3,..., A_k$，假设每一个飞机都是一个单独的机型，就变成了Fleet- Assignment Problem。
>
> $\sum {x_{fa}} =1$, $\forall \text{flt in the FAM result} \forall flt$ （boundle constraints）
>
> $\text{In}_{arc} = \text{Out}_{arc}, \forall \text{network node of Aft a}$， flow-balance 的约束
>
> $\leq 1, \forall \text{Aft}$
- 可能遇到的问题：约束太多了。
> DW 分解
>
> Frank Wolfe？
>
> Banders decomposition

> 重新建模，隐含了在原来模型中的一些constraints。
- $y_r$: daily route，r表示route编号

$y_r \in \{0, 1\}$
$\min \sum \sum c_r y_r$

$\sum_{f \in r} y_r = 1, \forall \text{flt f}$

$\sum y_r \leq \text{Num}_k$

$\sum_{\text{r ends at station}} y_r = \sum_{\text{r starts at station}} y_r$

- （约束的数量：441个，也是我们需要选择的route的数量）
> 相比于上面的模型，就是用变量代替约束。基础数学规划都是这种优化思路。
> - 有些变量是没用的。
- LP的本质：每一个约束都对应一个价格。如果能够猜对这个适合的价格，就可以解一个无约束问题。


$\min cx$ 

s.t. 
$$Ax  = b \\ x  \geq 0$$


- ==> $\min  x + (b - Ax)\alpha$，可以看作线性规划的拉格朗日松弛。
  
!!! note "如何评估一个route是好还是不好？"
    - $\alpha_f$：为了cover 这个flight，需要付出多少的effort
    - 检验数： $\bar{c_r} = \sum_{f \in r} \alpha_f - \gamma + \beta_{s^+} - \beta_{s^-} - c_r$ （$\gamma$ 意思是多用一个Aft需要多付出的成本）
    - $\bar{c_r} = \sum_{f \in r} \alpha_f - \gamma + \beta_{s^+} - \beta_{s^-} - \sum_{f \in r} c_f$
    > 检查不同方案的reduced cost判断是否能...


- 把一个evaluation问题变成一个optimization问题（设置一个dummy start和dummy end，找最长路（问题是，weight是怎么确定的））。如果最大的route是 < 0，说明已经找到了最优解。
> 只有在有向无环图（DAG）中，最长路就是最短路问题（ * -1）
>
> - 列生成（Column Generation）


---------

### 飞机的性能约束


- 飞机的零件是不一样的。高原机场的：空气稀薄，速度很快，需要更好的碳刹车、更长的跑道
> ARJ-21

- 把上述异质性体现出来：把一些不能飞特定航线的飞机的擦掉


-------

### Maintenance （维护、检查）


!!! tip “维护的方式”
    > 连续飞行时间超过某个值；
    > 
    > 距离上一次检查的时间超过一个interval
    >
    > Cycle time since last maint，多少次起降之后进行一次检查。


- maint route: 
    - starts at a maint station
    - ends at a maint station 
    - with a maint cost at the end  
- 在第二个约束的$\sum y_r \leq \text{Num}_k$前面，需要加一个约束$b_r$, 因为包括维修一个
- Multi-label shortest path:要考虑节点的属性
-  Cost: Non-decomposible:


-----------

## Delay & Propagated Delay（延误和连锁延误）
- 连锁延误：前一个航班延误了，这一个航班也跟着延误了。
    - 飞机有损伤的延误: $(\text{NDP}_A - \text{Buf}_{AB})^+$,这种延误很难用OR解决。
    - （Non-Drop-Delay）$PD_c = (\text{PD}_{B} - \text{Buf}_{BC})^+  = ((\text{NPP}_A - \text{Buf}_{AB})^+ - \text{Buf}^+_{BC}$ 
    > 根据历史数据算一算延误时间，把时间放到飞行时间中去。 
    - $PD_B = \sum_d (\text{NDP}_{Ad} - \text{Buf}_{AB})^+ \times \text{Prob}_d = \sum_d (\text{NDP}_{Ad} - \text{Buf}_{AB})^+ - \text{Buf}_{BC})^+ \times \text{Prob}_d$


- 用一个good approximation近似一个propagate cost然后放到network里面去。
- determinstic model：把延误的时间尽可能放在前面的flight中；
- stochastic model：如果不延误的话，这些时间就不能全放在最前面第一个航班了。需要放在中间，因为这样只会有前一半/后一半是相互影响的，把影响降低了，同时前面的interval稍微多一点，后面的稍微少一点。

!!! tip "医院的案例"
    Operational Room的stochastic，手术时间：什么分布？用expo近似。



-----------



