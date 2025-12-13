# 2024年的随笔记

## 0308 

!!! note "调度模式"

    - 一辆车的情况：
      - 货车-无人机协同调度（Collaborative，对应FSTSP）

        飞机需要从车上起降，并且有相关运行约束；

      ![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202403042210041.png)

      
       - 货车-无人机并行调度（Parallel, 对应PDSTSP）：

       同时运行，但是互不干扰；

      ![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202403042208847.png)




### FSTSP

- $x_{ij}$：卡车是否从 $i$ 开往 $j$ 点；
- $y_{ijk}$： UAV是否从 $i$ 起飞服务 $j$ 地最后在 $k$ 降落在卡车上。
- $t_j$： 卡车到达 $j$ 地的时间
- $t_{j}^{'}$： UAV到达 $j$ 地的时间

其他参数：

- $s_L, s_R$: 卡车成员释放无人机和回收无人机所需的时间

- 辅助决策变量： $p_{ij}$ 顾客 $i$ 在 $j$ 之前被服务，则为1，目的是约束飞机的飞行要是连续的。 $p_{0j} = 1$，约束起点必须是在所有顾客之前被访问。

- 辅助决策变量：$1 \leq u_i \leq c + 2$ 。限制子环路。

> 每个飞机每次只能访问一个顾客。



![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202403061443287.png)

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202403061443109.png)


### Heuristic for FSTSP 

先假设所有的点都是卡车访问，然后对每个可以被飞机访问的节点，尝试分配给飞机，从卡车上起飞执行运输。

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202403071642702.png)

然后针对每个可以插入飞行的无人机节点，看看能否产生节约。

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202403071658680.png)

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202403071701593.png)

-------

### PDSTSP

并行调度模式，UAV与卡车独立工作。因为无人机不局限在卡车上，所以无人机可以有很多个。卡车（在这个模型里）只有一个。Murray指出该问题实际上是两个经典问题的结合。TSP + PMS(Parallel Machine Scheduling), 首先对虽有需要卡车访问的地方，就是一个TSP问题，确保每个点可以访问，接下来给无人机访问的地方用并行机调度模型。

(Saleu et al., 2018) 改进了原本的启发式方法，可以求解229个客户点、多UAV的问题。


> MBIADOU SALEU R G，DEROUSSI L，FEILLET D，et al. An Iterative Two-Step Heuristic for the Parallel Drone Scheduling Traveling Salesman Problem[J]. Networks，2018，72（04）：459-474.

- $x_{ij}$， 卡车从 $i$ 开往 $j$ 地；
- $y_{j,v}$, 第 $j$ 个顾客由第 $v$ 个UAV服务；


![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202403061435785.png)

> Here, **each customer represents a ‘‘job’’ to be scheduled**, the ‘‘processing time’’ of each being given by the UAV’s round trip flight time to serve that customer from the distribution center. PMS原本是需要把工作分配到机器上，决定该如何分配；现在把每个飞机视为一台机器，每个顾客视为一个工作。决定如何分配。工作结束时间就是每台机器加工完所有工作的结束时间。
>

-----

### Heuristic for PDSTSP (Murray & Chu, 2015)

> 1. 最开始，先假定所有的在UAV服务半径内可以被服务的顾客，全部安排给UAV去服务，那些不在服务区内的点就分配给车。一般而言，初始化后，车服务的顾客 <<< UAV的顾客。
> 
>  如果UAV的MKspan > Truck 的MKspan：
> > 
> > 把每个UAV的单派给Truck，看看两个方案的最晚时间是否有改进，如果有，Update；


> 2. Swap 函数（实际是一个Operator算子）：上述启发式后，把原来卡车的交给无人机去服务，原来无人机的交给卡车去服务：看看是否会有改进；
> 
> 直到没有优化为止。



论文的数值实验：10～20个客户（小），大部分可被无人机访问；大部分节点都在UAV的可达范围内。 problems were generated with either 10 or 20 customers, such that 80–90% of customers were UAV-eligible. The truck and UAV speeds were fixed at 25 miles/h,  the UAV having a flight endurance of 30 min. The depot location was selected as being either near the center of all customers, near the edge of the customer region, or at the origin (as with the FSTSP test problems). Customer locations were generated such that either 20%, 40%, 60%, or 80% of all customers were located within the UAV’s range of the depot. 两个节点之间的距离，对于卡车是曼哈顿距离，对于无人机，是欧氏距离。

-----

### PDTSP和FSTSP的结果对比：

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202403061524244.png)

作者发现在小规模的场景下，FSTSP效果比PDSTSP要更好。


### Heuristic for PDSTSP(ITERATIVE TWO-STEP HEURISTIC, 2018)

> Two-step 体现在整个问题的两个step：
>
> - 把哪部分工作划分给哪部分交通工具？
> - 划分完毕后，这部分（卡车/UAV）该怎么解决？


![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202403062043076.png)

先假设所有的点都是由卡车访问的。生成TSP。把一部分订单拿出来给无人机执行。同时对删减后的TSP进行优化；对无人机的单用PMS进行优化。

> - 这里需要回答一个问题：怎么划分这些订单呢？

只要新生成的解满足条件：

1. 最迟的返回时间比原来的结果短
2. 最迟返回时间不变，但，$S_1, S_2$的最小返回时间比 $S^{'}_1, S^{'}_2$的要大；

就可更新原来的解，然后继续尝试迭代了。

双标准最短路问题： `Bicriteria shortest Path Problem`。



-----

### 并行机调度问题

!!! note "Parallel Machine Scheduling（PMS）并行机调度问题"
    存在多台相同或不同的机器可以同时处理任务。需要确定每个任务分配到哪台机器以及任务的处理顺序，以达到优化目标，如最小化完成所有任务的总时间或最大化产出等。

    列生成求解：论文：Xu, J., Nagi, R., 2013. Identical parallel machine scheduling to minimise makespan and total weighted completion time: a column generation approach. Int. J. Prod. Res. 51 (23–24), 7091–7104.

    目标函数：最小化加权完成时间的总和与总完工时间。这两个目标函数可以独立，也可以连在一起计算。PDTSP主要解决的问题是第二种场景，也就是仅仅最小化总的完工时间。
    
    > The objective function is to minimize the sum of the weighted completion time of every operation and weighted makespan. 

> ![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202403061429767.png)


$N$ : 所有工作的集合；
$Y$ ：机器的集合；
$w_j$ ：工作j的权重；
$F_j$ ：工作j的完成时间；
$F$：并行机排程问题的最大完成时间；
$B_j$ ： 所有编号小于 $j$ 的工作的集合；

决策变量： 

$x_{iy}$, 工作 $i$ 是否分配给机器 $y$, $\forall i \in N, y \in Y$

$a_{ijy}$, 工作 $i$ 和 $j$ 是否同时被分配给机器 $y$ ；$\forall i \in B_j, j \in N, y \in Y$

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202403050950579.png)

> (1.2.3). 表示不同工作在机器上的分配情况；
> 
> (4). 每个任务只能被分到一个机器上；
> 
> (5). 计算总的完成时间；
> 
> (6). 约束每个任务的完成时间不早于最晚完成时间；
> 

----------


主问题，是在许多个“排班方案”里选择一部分，从而达到最优。

- $s$： 列的序号；
- $S$：列的标号的集合；
- $F^s$ : 该列任务所需的时间；

- $X_{iys}$ : 任务 $i$ 是否被分给 $y$ 机器，并采用 $s$ 列的工序安排；这个值是子问题产生的一个常量。

- $Z_s$: $s$列是否被选作一个解；

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202403072209280.png)

> 主问题与原问题的对应

子问题转化成“生成主问题的一列”，使得这一列的检验数（reduced cost）是负的。这样把这列加入主问题一定可以让主问题更优。

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202403072210659.png)


> 特定的应用：Bus-Drones Collaborative 

---


## 0315

!!! note "点评"

    成本关联矩阵是如何获得的？

    > 矩阵还是向量。

    $I^{rs}$ 的数学含义是什么？

    要搞清楚每个字母表示的意义。

    代码的思路是什么？怎么解的？

    > Frank-Wolfe 的UE怎么实现的？怎么转化成凸锥的问题？

    - 一周把一个小问题讲清楚就好。

    > 最优潮流问题：不一定要讲很全。把一个地方讲细了讲清楚了。基础代码、数值实验等。

    尽量做一个PPT. 简单的。

    - 自己画一个流程图，有一个结构：画画结构、有个整体的流程。
    - 举一些例子。

    带有边约束的交通分配问题；SUE：

## 0329


### 公平出行需求管理的预约限额策略


!!! abstract "Abstract"
    - by Chair Professor Yang, Hai. HKUST. 
    - 了解一下基本的Idea.


> - 限行（Traffic rationing）
> - Booking（预约出行）

如何把上面两种做法结合起来？（TRB）


!!! note "Tradable credit scheme（可交易电子路票）"
    政府给一些纳税人一些路票（免费不收钱），上路是需要路票的。路票可以用来交易。你就需要买一定路票来维持日常出行的开销，而不需要开车出行的人，就可以售卖自己的路票。

    路票实际上是给富人（有更多出行需求的人）把资金流动给低收入群体。

    - 需要建立一个路票交易系统：会不会存在价格波动的问题


- Pricing 
    - 是不是以低收入人群的代价来给高收入群体提供benefit？因为高收入人群更能支付起交通拥挤收费。

- Quantity instrument

- 限行是否是有效的？
    - 如果有两辆车。限行是不是就是无效的。
    - 限行是不是五环内都必须限行？
    - 缺乏灵活性。
- 预约出行是否是有效的？
    - 预约一个路段，在特定时间去走。
    - 存在的问题：抢票！
    - 拍卖预约的问题：不公平！

!!! info "Booking cum Rationing Strategy"
    
    在Bottleneck时间段内，有一定使用额度。同时的日期使用需要预约。

    - Pros: 
        - Flexible for drivers 
        - Control Capacity
        - 实现了Long-term equilibrium ??????
    - Cons：    
        - ? to be determined

> 多接触一些东西。
>


-----------

## 0330 


### 客货共享运输模式


!!! quote   "客货共享运输模式的多阶段运营优化：物流公司和客运公司参与客货共享运输，Presenter: Yuxin Zhen, TongJi University"

!!! quote "背景"
    - 非高峰段的公交车利用率很低；
    - 客运公司、物流公司的**合作**，还是**某一方主导**的。合作，更倾向于Integrated Decision，然后 Profit-Sharing

    ------

    - 乘客的决策
    - 出行成本构成
    - 出行模式选择


> 只考虑公交车在起终点的运输。物流公司有集散点，公交车先去把货带上，然后再去运人，运人之后，再前往货物的终点集散点。
>
> 


- 客运公司决策：最佳发车间隔 $t$ 和乘车价格 $p$；
- 物流公司决策：共享运输补贴价格 (? What is this? == 支付价格？) 、共享运输的运输货量 $m$ ；
- 给出了一个解析解公式？
- 设计了一套算法来解决这个问题。

-  Numerical Analysis   
   - 共享运输补贴价格 vs 第三方物流运输成本

- Conclusion:
    - 物流公司主导的共享运输模式，补贴价格较低的客运时段优先承担共享运输服务;
    - 共享运输车辆货运空间不足，优先将货物分配到补贴价格较低的客运非高峰期进行共享运输；
- Professor Questions：
    - 为什么会在运力分配上发生突变？
    - 图曲线增加的趋势是什么含义？
    - 用什么工具跑出这个结果？
    - 对结论的建议：
        - “大多数情况下，共享运输模式可以实现双赢” --> 什么情况下实现双赢？场景是什么？
        - 一些Interesting的insights


-------------



###  航空紧急恢复 

- 航空紧急恢复的问题：二 紧急恢复：短时间给高质量解；图神经网络。

- **Time Space network in Airline Industry**
- **Delay Propagation**: 


!!! quote "Minimal Connection Time (MCT)"
    任意flight pair的最短链接时间是不一样的。



> Input -> Model Formulation (Time Space Network) -> Solver

- 图注意力网络
- Machine Learning for IP 用ML看看有些column不需要Generate

--------


### 众包物流 CrowdSource delivery Service  (HKU, 土木与制造系统系)

!!! info "Background"   
    众包物流，常见的是众包物流配送模式，是在“互联网+"的时代背景下，随着O20商业模式2及共享经济Q的发展 (O20即Online To Offline），通过调动社会大量闲置人力资源 “顺路”送快递，来解决了"最后一公里"的同城配送Q难题。
    
    众包物流跟滴滴存在相似之处，滴滴是整合了市场上的私家车资源，帮助我们解决出行问题；而众包物流是整合了市场上的工作之外闲置的“人力资源〞，基于互联网平台将应该分配给专职配送员的配送工作转包给企业之外的非专业群体来做。


    - 把潜在的可以利用的运力用来送货物。
    - 对每个出行者，要多一个包裹的拿取和交货。
    - 除了Crowd之外， 不能遗漏专职配送的情况。

    ------

    - 三种主要的运营方式：

    > **Asset-light format**: 只是一个平台(like Uber-ease，做人和货物的match）。如果没match上，这就无法运输了。
    > 
    > **Asset-heavy format**: 公司本身提供配送服务，除了自己的配送服务外，让crowd来帮忙带货。

    > > 涉及相关方：平台、专职服务的配送员、参与众包的普通人、有物流运输需求的客户。

    > **Asset-medium format**: （？）和heavy的区别在于，crowd没有运完的单子，是其他公司的车来运，而不是自己的车来运，是我找其他公司来运（相当于一个outsourcing）。


!!! question "Questions"
    - 激励措施（因为会给正常出行的人带来inconvenience）。
    - 可能有不同商业模式，效果如何。


!!! quote "Two-sided-Market Method"
    - 需要运货的客户在不同运营模式的成本计算方式，对应需求端。
    - 供给方的效用函数（Crowd在这一单子拿到的钱，ta匹配失败造成的失望成本），对应供给端；
    - 平台的匹配函数

    ----------

    - market equilibrium
        - 决策变量：平台如何收费、公司开多少车、定价多少等；

!!! example "Insights"
    - 在平台没有优化他的决策时：
        - Light：只要订单能够成功进行CrowdSourceing 分配，对各方都有利；
        - Medium：在light下没有被匹配的，会带来customer disappointment，但是Medium给第三方运了，没有disappointment，不过platform有一个给第三方物流的cost。（给顾客的定价不变吗？）
        - Heavy：每个
    - 在平台优化了它的决策：
        - maximal它的Profit的话： （Missing Part ...zzzZZZZ💤）
        - maximal社会福利的话： 在什么condition下，（Missing Part ... zzzZZZZ💤）

    - 能不能找到一些 win-win-win outcome？


!!! abstract "基于地铁的物流运输"

    - public-transport-integrated CrowdSourced delivery.
    - 先把卡车从集散点运输到地铁站点。
    
    ------ 



!!! question "Q"
    - 在哪里设置Locker（集散点、取货箱、或者Retailer Store），进行货物集散；
    
    - uncertainty: 人流量的不确定性、人的参与意愿；

!!! info "Contents"
    - Two-stage Stochastic Programming:
        - 先进行选址；时空网络的建立；
        - 再进行货物的分配；

    > Freight Flow 是连续的情况；


    - 订单分配 + 路径优化，不止是配送员，而是一些普通人可以从快递小哥这里帮忙拿掉一些货物进行配送。




!!! conclusion ""
    【见图】

    我的想法：物流运输配送的零散化、去集中化。把末端1km配送化整为零，分配到可以利用的零散运力中，而且这种零散运力的场景是往往是需要和现有的系统整合在一起，做hybrid；或者把市内运输整合进公共交通中。而之前更多想的是集中，集中。


### 不确定交通状况下的城市节能驾驶问题 （HKUST)

> 非高峰时期的出行问题

求解的是，在确定OD的特定路径上每个路段要开多快速度（or加速度？），让油耗更低。（决策：不同时间段的瞬时速度）

节能驾驶模型的建模；


不确定性体现在：车在不同路段因为各种原因（避让、减速等）会导致速度的波动。通过车流速度反映这种波动。


选择不同路径中的哪个路径，能让油耗更加小；

加入：信号灯、车速等更多不确定的因素；



### 考虑不确定时间窗的VRPTW

如果只是对历史数据取均值，会严重低估不确定的影响的。

一些厂商愿意用提高一些成本的方式降低迟到率。


## 0401 

达摩院。


https://opt.aliyun.com/portal

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202404011013704.png)

**自动建模**：在开源基座上训练出来的LLM、凸化；


!!! note "How to train LLM？（DistRun）"
    教学科研上的应用：想用的算力不够，闲置的算力很多。

    不会使用多机多卡。

    资源管理。

    云、多平台、突发情况下的短期应急使用。

    自助定制。（for AB testing / Distributed Computing)

    基于MPI 的HPC

    南方电网AI大赛。
    
Decision Intelligence Lab 

!!! question "Why NN to Solve MILP?"

    - Learning to optimize.
    - 端到端。end to end .
    

    Direct AI Solver:


    **Primal Dual Intergral**

    把优化问题的vectors进行图建模（Bipartite Graph）
    - 对局部信息进行汇总、转化成新的params
    - 优点：不变性、协变性：用其他的NN难以学习到，浪费大量时间。
    - 
    > Weisfeiler Lehman test 

    **Message-Passing** 

---

## 0426

交通配流问题（TAP），混合车辆、路径生成。

目标函数：充电成本；

!!! note "标记"
    用Link Type区分充电路段和常规路段；（给每条路打个标签）
    
    > Path / Link
    > 
    > $\alpha^{rs}_{akg}$ : 路段-路径关联矩阵（每次迭代会更新这个矩阵），是一个输入的参数。
     

- 一开始就去找一些可行路径集，用这个子集去构建路段路径关联矩阵。

先要得到UE均衡下的 $x_a$，代入求出路段成本。这时候每个OD对都得到了一个成本最低的路径。

迭代终止条件：从每个路径成本找到当前路径集合中最小的路径成本。

所有的可行路径集。

> 后续的应用：心理预算不同对同一个事物的感知是不同的。可以考虑用户异质性、价格的影响。
>
> 充电需求的不确定性：到底有多少充电车去充电了？到了充电站的车充了多少电呢？
>
> 充电量不一样了，充电时长是不是也不确定了。

后续的方向：与电网的交互。

---

!!! example "Review"
    **线性因子模型** ：把确定的部分和不确定的部分分开来；

    **线性约束情况**下对模型的推导：
    
    1. Box  Uncertainty
    2. Ellipsoid Uncertainty set
    3. 无穷范数交二范数：推导到一个二阶锥规划的模型
    4. Budget Uncertainty Set：**最重要的模型**。无穷范数交一范数。正方形和菱形相交。


## 0517

主要汇报了：

论文相关的若干成果：1. Time dependency （ only for trucks ）2. En-route charging

解谜游戏的若干成果：Slither Link， 割平面， Callback function.

-----

基于不确定矩信息的分布鲁棒模型、分布式鲁棒优化。

单领导者多追随者的斯塔克伯格模型：多维电网的电动公交调度。两个主体都要有自己获利的动机。每个时间段都要进行一次模型的求解。

和公交车配合的无人机的物流相关。无人机不一定自己飞，而是和无人机配合的。