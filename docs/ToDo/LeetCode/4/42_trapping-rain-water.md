# 42_接雨水

<!-- 所有文件名必须是该题目的英文名 -->

!!! note
    <!-- 这里记载考察的数据结构、算法等 -->
    动态规划

- 🔑🔑 难度：<span style = "color:crisma; font-weight:bold">High</span>
<!-- <span style = "color:gold; font-weight:bold">Medium</span> 中等 -->
<!-- <span style = "color:crisma; font-weight:bold">High</span> 困难 -->
<!-- <span style = "color:Green; font-weight:bold">Easy</span> 简单 -->

<!-- 题目简介 -->

> 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
> 
```
```

------

??? note 
    左边的最大值，右边的最大值。两者的最小值 - 当前位置的高度。
    
-------------

=== "Python"

    ```Python
    class Solution:
        def trap(self, height: List[int]) -> int:
            n = len(height)
            if n == 0:
                return 0
            leftMax = [height[0]] + [0] * ( n - 1 )
            rightMax = [0] * (n - 1) + [height[-1]] 
            for i in range(1, n):
                leftMax[i] = max(leftMax[i - 1], height[i])
            for i in range(n - 2, -1, -1):
                rightMax[i] = max(rightMax[i + 1], height[i])
            ans = 0
            for i in range(n):
                ans += min(leftMax[i], rightMax[i]) - height[i] 
            return ans 


    ```
