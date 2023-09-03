# 一份私人的准备


!!! question "什么是VRP问题？"
    给定一组客户点、车辆数量、起始点和终点、对应路段的长度或者行驶成本，目标是找到使得所有客户点都被访问一次的最短路径方案。

    -----

    ==CVRP== ：

    在VRP的基础上，每个客户点有一个特定的需求量，车辆需要满足总容量限制且在不超过容量的情况下为客户提供服务

    ==VRPTW== ：

    在基本VRP的基础上，每个客户点都有一个时间窗口，表示可以在某个时间范围内访问。目标是在满足时间窗口和车辆容量限制的情况下，最小化总行驶距离或成本。

    ==HVRP== ：

    混合车辆路径问题：在优化过程中考虑多个目标函数，而不仅仅是单一的目标。 HVRP涉及在满足车辆容量和其他约束条件的前提下，同时优化多个不同的目标，如最小化总行驶距离、最小化总成本、最小化车辆数量等。


!!! question "TSP问题"
    给定一些城市或者每对城市之间的距离，求解访问完每一座城市并回到最初出发点城市的最短回路。（遍历所有的点）

    -------

    中国邮递员问题：

    邮差设法找到一条路径，遍历所有的边，然后回到出发点。

    ---------

    欧拉回路：每条路都走一次，最后回到起点。



!!! note "大邻域搜索 + 贪心的思路"
    relocate / exchange 等算子对初始可行解进行重新分配

    Greedy：优先考虑最早接受任务的专家

    repair && destroy 


!!! note "列生成"
    求解子问题（sub problem）来找到可以进基的非基变量。如果找不到一个可以进基的非基变量，那么就意味着所有的非基变量的检验数（Reduced Cost，RC）都满足最优解的条件，也就是说，该线性规划的最优解已被找到。

    Master Problem -> sub problem -> new column && check Reduced Cost

    Benders Decomposition的基本思想是通过将求解难度较大的原问题分解为两个更容易求解的问题master problem和subproblem，类似于列生成（Column Generation）方法，不同的是列生成方法通过求解subproblem产生column添加至master problem，而Benders Decomposition通过求解subproblem产生cut添加至主问题（类似row/ constraint generation）。如何产生什么样的cut是我们关心的问题。
