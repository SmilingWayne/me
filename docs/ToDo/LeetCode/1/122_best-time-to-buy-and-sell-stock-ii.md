# 122_买卖股票的最佳时机II

<!-- 所有文件名必须是该题目的英文名 -->

!!! note
    <!-- 这里记载考察的数据结构、算法等 -->
    动态规划

- 🔑🔑 难度：<span style = "color:gold; font-weight:bold">Medium</span>
<!-- <span style = "color:gold; font-weight:bold">Medium</span> 中等 -->
<!-- <span style = "color:crisma; font-weight:bold">High</span> 困难 -->
<!-- <span style = "color:Green; font-weight:bold">Easy</span> 简单 -->

<!-- 题目简介 -->

> 给你一个整数数组 prices ，其中 prices[i] 表示某支股票第 i 天的价格。
> 
> 在每一天，你可以决定是否购买和/或出售股票。你在任何时候 最多 只能持有 一股 股票。你也可以先购买，然后在 同一天 出售。
> 
> 返回 你能获得的 最大 利润 。


```
输入：prices = [7,1,5,3,6,4]
输出：7
解释：在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5 - 1 = 4 。
     随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6 - 3 = 3 。
     总利润为 4 + 3 = 7 。
```

------

!!! note 
    想状态转移方程！想状态转移方程！状态只有“是否持有”这两个！

    
-------------

=== "Python"

    ```python 
        class Solution:
            def maxProfit(self, prices: List[int]) -> int:


                dp = [[0, 0] for _ in range(len(prices))]
                dp[0][0] , dp[0][1] = 0, -prices[0]

                for i in range(1, len(prices)):
                    dp[i][0] = max(prices[i] + dp[i - 1][1], dp[i - 1][0])
                    dp[i][1] = max(dp[i - 1][0] - prices[i], dp[i - 1][1])
                
                return dp[len(prices) - 1][0]

    ```