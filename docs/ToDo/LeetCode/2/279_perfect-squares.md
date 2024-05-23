# 279_完全平方数

<!-- 所有文件名必须是该题目的英文名 -->

!!! note "要点"
    <!-- 这里记载考察的数据结构、算法等 -->
    动态规划

- 🔑🔑 难度：<span style = "color:gold; font-weight:bold">Medium</span>
<!-- <span style = "color:gold; font-weight:bold">Medium</span> 中等 -->
<!-- <span style = "color:crisma; font-weight:bold">High</span> 困难 -->
<!-- <span style = "color:Green; font-weight:bold">Easy</span> 简单 -->

<!-- 题目简介 -->

> 给你一个整数 n ，返回 和为 n 的完全平方数的最少数量 。
> 
> 完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。



```

输入：n = 12
输出：3 
解释：12 = 4 + 4 + 4
```

------

??? note "我的备注"
    打表。

    
-------------

=== "Python"

    ```Python
    class Solution:
        def numSquares(self, n: int) -> int:
            dp = [0] * (n + 1)
            for i in range(1, n + 1):
                tmp, j = 10001 , 1
                while j * j <= i:
                    tmp = min(tmp, dp[i - j * j])
                    j += 1
                dp[i] = tmp + 1
            return dp[-1]
    ```
