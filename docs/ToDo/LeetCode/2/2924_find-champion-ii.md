# 2924_找到冠军 II

<!-- 所有文件名必须是该题目的英文名 -->

!!! note
    <!-- 这里记载考察的数据结构、算法等 -->
    哈希表 | 动态规划

- 🔑🔑 难度：<span style = "color:gold; font-weight:bold">Medium</span>
<!-- <span style = "color:gold; font-weight:bold">Medium</span> 中等 -->
<!-- <span style = "color:crisma; font-weight:bold">High</span> 困难 -->
<!-- <span style = "color:Green; font-weight:bold">Easy</span> 简单 -->

<!-- 题目简介 -->

> 一场比赛中共有 n 支队伍，按从 0 到  n - 1 编号。每支队伍也是 有向无环图（DAG） 上的一个节点。
> 
> 给你一个整数 n 和一个下标从 0 开始、长度为 m 的二维整数数组 edges 表示这个有向无环图，其中 edges[i] = [ui, vi] 表示图中存在一条从 ui 队到 vi 队的有向边。
> 
> 从 a 队到 b 队的有向边意味着 a 队比 b 队 强 ，也就是 b 队比 a 队 弱 。
> 
> 在这场比赛中，如果不存在某支强于 a 队的队伍，则认为 a 队将会是 冠军 。
> 
> 如果这场比赛存在 唯一 一个冠军，则返回将会成为冠军的队伍。否则，返回 -1 。


```
```

------

??? note 
    每个OD的D一定比O要小。只需要看有没有唯一的点没有在D里出现过。

    
-------------

=== "Python"

    ```Python
    class Solution:
        def findChampion(self, n: int, edges: List[List[int]]) -> int:
            if n == 1:
                return 0
            best = [0 for _ in range(n)]
            for edge in edges:
                lower = edge[1]
                if best[lower] == 0:
                    best[lower] = 1
            if sum(best) != n - 1:
                return -1
            else:
                for idx, num in enumerate(best):
                    if num == 0:
                        return idx
                return -1
    
    ```
