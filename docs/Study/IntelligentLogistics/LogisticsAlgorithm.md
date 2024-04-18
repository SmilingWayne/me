# 物流优化算法


考核方式：见PPT。都是课堂作业。==这个课的上课时间不是10:10AM，而是10:00AM。别起太迟== .

!!! abstract "计算复杂性理论"

物流在业界的运作，相关应用：

- 码头的运作。车辆运载集装箱：AGV调度问题。
- 集装箱放在什么地方？布局问题。
- 集装箱的码货，怎么操作（推箱子）
- 船的泊位分配、重心的负载分配；
- 哪些货放到哪些船。

!!! note "重要的是课外实践"


-----

## 0307 


> 组合优化中组合爆炸的概念。101个节点的TSP问题：100!个解，即使宇宙里所有的原子都是一个CPU，并行计算，每个解在一个普朗克时间内即可计算完毕，需要的时间也是 $10^{34}$ 级别，超过了宇宙的总年龄。

> CVRP 问题：难度是不亚于TSP问题的。 

> https://github.com/nagata-yuichi/GA-EAX
>
> Exact Solution: Concorde TSP solver

!!! question "什么是元启发式算法？"

    在实践中被证明有效的一些系统的启发式算法思路。

    --------

    1. Constructive Heuristic 
    2. Solution Representation: 不同的解和解之间是有关系的，这些解的集合构成了一个庞大的解空间。可以通过算子来改变不同解之间的关系。
    3. Local search：一些问题适合进行LS（一些车辆路径网络），有些问题并不适合；
    4. Large Neighbourhood Search：
    5. Metaheuristic: Trajectory-based：从轨迹线出发。
    6. Metaheuristic: Population methods：基于种群的迭代进行设计；
    7. Diversification & Intensification：保证种群的多样性（近亲繁殖培养不出更好的解了）、收敛更加快的
    
    Tibault· Vidal: 佬！

    ----------

    元启发式，不存在什么明确的行业定义。

    - Local Heuristic：在局部进行搜索。
    - Moves：两个解进行交换
      - 2-opt 
      - Or-exchange
      - 2-opt* 
      - Cross

    > 优势在于，在O（1）的时间内可以评价修改能否带来改进。


    - 如何跳出局部最优？
        - 重新生成构造一个新的解： 模拟退火：一定概率构造一个更差的解
    - Metaheuristic在于，可以跳脱出局部最优的情况


    Guided-Local Search/ Vari-Local-Search


--------


## 0314 

- 构造算法(Constructive Algorithm)：通过某种方法构造出来一个可行解
- 设计构造启发式：
    - 如何定义choices；
    - 满足Choices的可行性；
    - 如何快速检查choices是否有改进；

> 一些问题，比如可分背包问题，是可以通过构造贪心来获得最优解的。


!!! question "什么样的问题是不适用局部搜索的？"
    这种问题进行局部搜索的代价会很大。

    代价很大：指进行局部搜索的开销 > 构造一个新的解的开销；

    如果计算/判断改进的成本是 O(1) 的，那么可以局部搜索，一般来说，布局的问题



!!! note "Facility Layout Problem"

    不一定可以用“交换”、“relocate”等算子进行优化。复杂度太高。

    【补充一下问题描述】


!!! note "RCPSP 问题(Resources Constrainted Project Scheduling Problem)"
    任务有先后次序，每个任务要消耗资源，资源也是有限的。

    > 最后会形成一个 Project Network. 要确定任务调度，让最早结束时间最早；

    -------

    并不适合local Search的方法。你要给一个项目交换、检查是否可行：已经有O(n)的复杂度了。如果要为这个Project找到一个最好的位置，那么要遍历所有的时间点的。

    -------

    最好的办法：把先后顺序融入到解的表达中；然后用Decode


!!! note "Strip Packing Problem" 

    > INFORMS J. COMP S.Martello An Exact Approach to the ...

    切割一部分矩形，使得最高点最小。比如放置顺序123456.依次放进去。

    每次选最下的可放置的位置，检查下放不放得下。


----------


!!! note "TSP 的一些构造算法"
    - Nearest Neighbour heuristic 每次找最近的两条边连起来，接着找最短的。直到所有的都访问了。

    > 复杂度 $O(n^2)$


    - Cheapest Insertion Heuristic （最小成本插入）先用两个点成环，加入一个点，新的边减去原来成环的一条边，构成一个新环。看看效果是否是会更好。


!!! note "Knapsack Problem"
    (类似 Portfolio 的问题)

    Best-marginal Cost: 接下来放进来的物品的单位收益要是最大的。

!!! note "最小生成树" 
    略。


!!! note "VRP Sweep"
    如果出发的车厂在中心：按照角度最小的点 连在一起。

    > 无法应对诸如时间窗等约束的情况。

> Multi-start： 尝试许多次，加入随机性。
>

!!! note "look ahead Tree search Algorithm"

    用在树搜索中。
    
    Choice 得到一个状态，标准都是基于当前choice。但是你不知最终的解的情况如何。

    所以就再往下走一点，看看再往下的解是否会比只看下一层的结果要更好。



>
> Learning的情况：
>
> Randomization的情况：如果多种heuristic大家都是一样的，怎么选择？（加一个随机选的情况）

------

## 0321  Look Ahead and Tree Search


> Maximal Space 对剩余空间的表达。


!!! note "GRASP"

!!! note "ALNS "
    构造启发式算法



- `container loading problem.`


- 塑料袋装箱问题： $L \times W$  的塑料袋，待装入物品有 $n$ 个 物品 $i$ 的尺寸 $L_i \times w_i \times h_i$ 。

- `Project Scheduling`

- `Diving heuristic`


--------------


## 0328 Solution Representation 

为什么这么重要？会影响算法实现的效果。

可能用到的数据结构：BitSet, Tree, List


- 0-1背包问题，项目数量很多，但是实际背包里选择的项目比较有限，此时选择BitSet效果更好；


- n 皇后问题。如何输出所有的解。

> 二维数组， 或者一个一维数组，第k个元素表示第k列的皇后所在的位置（可以减少很多解的检查）；或者， [(a,1), (b,2 )....]


!!! note "TSP with Hard Time Windows" 
    记时间窗口 $[a, b]$ 如果在开始之前到达，必须等到开始时间才能上架。如果在结束之后到达，就是不可行的；

    如何设计解的表达。

    > 9 AM （服务A）, (+40min), 10 AM （服务B）... 存在的问题：可能有很多的可行解，因为也可以 9:01 AM （服务A） （+40min）, 10: 04 AM （服务B）...

    这种表达不好。

    改成序列表示。访问的序列只是和你在不同节点之间的距离有关。所以可以用TSP的表达。但，这里的解的表达对应的是**一组可行解**。

    > $[ A, B, C, E, D, G, H, F, I]$。把第一层决策：决定访问顺序，当作一个主问题，而从这一组可行解里得到具体的访问时间，通过解决子问题来求解。

    如何求解子问题：遍历这些硬时间窗，解码出一个可行解。


!!! note "TSP with Hard and Soft Time Windows"

    允许早到，但是要有惩罚值，允许晚到，但是晚到也有惩罚值；同时也有硬的时间窗口（很大）。用于在Hard TW找不到可行解的情况下。

    依然是先确定访问顺序，再确定访问时间。

    用DP可以在$O(n\log n)$ 来求解最好的访问的时间。`IBaraki An iterated local Search algorithm` 


!!! note "2-D Strip Packing"
    可以确定一个货物的摆放序列，只知道货物放的顺序，不知道具体放在哪里。而且没法在多项式时间内算出最佳摆放位置。


    解决子问题就是用构造式算法来解码。

> 上述这些依赖解码的都是“非直接解表达”

!!! note "CVRP"
    Heuristic-Lin-Kernighan. 研究一下。

> 如果解码不能实现解空间的一一对应，而是两个解码后对应到同一个解，或者说


!!! note "2DVPP-GC: A packing Problem"  

    怎么设计解的表达？

    一个序列，进行划分。怎么进行划分，让最后的费用最小。

    把划分问题转换成**最短路问题**。

!!! note "TPTT 问题"
    先决策选哪些承运人。一串 $[0, 1]$。如何给这些承运人分配集装箱的量。  

    最后有一个虚拟节点。从0到2的线实际上装的是0和1两个物品。

    

## 0411 如何对解构造一个搜索空间

> 清明假期后的第一次课。

邻域搜索算法。

如果删除的边超过2个，那么拼接方式就有很多种。选哪一个看自己的选择策略。

!!! example "现实背景：Orienteering Problem"
    物流订单量，有哪些应该是自己来服务，有哪些给第三方物流外包进行服务？

    > 美团骑手的分配：3类骑手分配。让哪些骑手服务哪些订单？

    选择高价值的客户优先进行服务。

    -----

    如何去描述这种算子定义的邻域？

    010/ 011 / ... 

    每个节点都有3条边相连。算子Flip，把任意一个位置的数字变成别的数字。

    - 可能存在的问题：局部最优的情况：周围的都比它差。一定需要一个跳出局部最优的方法。
    - 计算效率的情况： $n = 10000$，有一个很大的网络。

!!! example "TSP里，一些经典的算子"
    - 算子 Switch: 把第 $i$ 和 $i+1$ 的顺序改变。
    - Swap：交换任意两个节点位置。
    - Relocate：随机选一个放到新的位置，做一个插入。
    - K-Opt，删除K个边，有更多的拼接。
    - Or-Opt，
    - Intra-route Neighbourhoods: 
    - Swap*，基于2-exchange， 不再是直接插入到一个固定的位置上，而是插入到这个路径上的任何一个位置。[论文链接](https://arxiv.org/abs/2012.10384)

!!! example "适合邻域搜索的一些算子"

    网络流、路径规划。

    设计邻域时候，需要Problem Specific，要根据问题设计算法。要知道问题是否适合用邻域搜索。

    会不会有一些搜索的算子是重复的，已经实现的。

    first-Accept / Best-Accept： 是一有更好的解就拿，还是找所有里面最好的解再拿。

    Delayed accepted 是否立刻接受这个更好的解；


!!! note "一些实际出现的奇怪的情况"

    约束很复杂的情况：
    - 允许接受不可行解，但是让目标值变得很差。

- 写代码时候的一些Trick：有一些边不在区域里面，有一些边的概率使用的概率不大。对地图需要进行预处理。

> Technique note: Split Algorithm in O(n) for the capacited vehicle routing problem.

## 0418 大邻域搜索

对应的邻域是指数级别的：大邻域搜索算法。实现最为简单并且有效。适合规模比较大的计算场景。

局部最优：任意一个邻居，结果都比当前解差。

如果 $K \leq 3$，都算是小邻域。如果邻域更大。

不进行全搜索。选择一块区域，把区域内所有的边全部都删除（Destroy）。基于这个部分解进行一次构造（Repair）。

!!! question "问题"
    如何删除？

    如何增加？

相当于一次操作，都进行了很多次2-Opt操作。

自适应的情况：要给删除算子计算一个权重。怎么选的过程就体现了自适应的情况。

轮盘赌的算法：通过随机概率来选择算子。
