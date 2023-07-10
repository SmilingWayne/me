# 436_找到右区间

<!-- 所有文件名必须是该题目的英文名 -->

!!! note
    <!-- 这里记载考察的数据结构、算法等 -->
    排序 + 二分

- 🔑🔑 难度：<span style = "color:gold; font-weight:bold">Medium</span>
<!-- <span style = "color:gold; font-weight:bold">Medium</span> 中等 -->
<!-- <span style = "color:crisma; font-weight:bold">High</span> 困难 -->
<!-- <span style = "color:Green; font-weight:bold">Easy</span> 简单 -->

<!-- 题目简介 -->

> 给你一个区间数组 intervals ，其中 intervals[i] = [starti, endi] ，且每个 starti 都 不同 。
>
> 区间 i 的 右侧区间 可以记作区间 j ，并满足 startj >= endi ，且 startj 最小化 。注意 i 可能等于 j 。
>
> 返回一个由每个区间 i 的 右侧区间 在 intervals 中对应下标组成的数组。如果某个区间 i 不存在对应的 右侧区间 ，则下标 i 处的值设为 -1 。

```
输入：intervals = [[3,4],[2,3],[1,2]]
输出：[-1,0,1]
解释：对于 [3,4] ，没有满足条件的“右侧”区间。
对于 [2,3] ，区间[3,4]具有最小的“右”起点;
对于 [1,2] ，区间[2,3]具有最小的“右”起点

```

------

??? note 
    排序加二分，Python要记住bisect_left啊！！

    把bisect 的实现看一下。
    
-------------

=== "Python"

    ```Python
    class Solution:
        def findRightInterval(self, intervals: List[List[int]]) -> List[int]:

            for idx, interval in enumerate(intervals):
                interval.append(idx)
            intervals.sort()
            res = [ -1 for _ in range(len(intervals))]
            for _, end, idx in intervals:
                i = bisect_left(intervals, [end])
                if i < len(intervals):
                    res[idx] = intervals[i][2]
            return res
            
    ```