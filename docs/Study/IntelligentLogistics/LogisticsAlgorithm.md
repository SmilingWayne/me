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
