# 56_合并区间

<!-- 所有文件名必须是该题目的英文名 -->

!!! note
    <!-- 这里记载考察的数据结构、算法等 -->
    列表操作 ｜ 排序

- 🔑🔑 难度：<span style = "color:gold; font-weight:bold">Medium</span>
<!-- <span style = "color:gold; font-weight:bold">Medium</span> 中等 -->
<!-- <span style = "color:crisma; font-weight:bold">High</span> 困难 -->
<!-- <span style = "color:Green; font-weight:bold">Easy</span> 简单 -->

<!-- 题目简介 -->

> 以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。
> 

```
示例 1：

输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
输出：[[1,6],[8,10],[15,18]]
解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].

```

------

??? note ""

    
-------------

=== "Python"

    ```Python
    class Solution:
        def merge(self, intervals: List[List[int]]) -> List[List[int]]:

            intervals.sort(key=lambda x: x[0])
            res = []
            l , r = 0, 0
            
            while r < len(intervals):
                curl , curr = intervals[l][0], intervals[l][1]
                while r < len(intervals) and (intervals[r][0] <= curr ):
                    curr = max(intervals[r][1], curr)
                    r += 1
                res.append([curl, curr])
                l = r 
            return res
    ```
