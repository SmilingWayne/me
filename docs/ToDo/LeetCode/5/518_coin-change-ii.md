# 518_零钱兑换II

<!-- 所有文件名必须是该题目的英文名 -->

!!! note
    <!-- 这里记载考察的数据结构、算法等 -->
    动态规划

- 🔑🔑 难度：<span style = "color:gold; font-weight:bold">Medium</span>
<!-- <span style = "color:gold; font-weight:bold">Medium</span> 中等 -->
<!-- <span style = "color:crisma; font-weight:bold">High</span> 困难 -->
<!-- <span style = "color:Green; font-weight:bold">Easy</span> 简单 -->

<!-- 题目简介 -->
给你一个整数数组 coins 表示不同面额的硬币，另给一个整数 amount 表示总金额。

请你计算并返回可以凑成总金额的硬币组合数。如果任何硬币组合都无法凑出总金额，返回 0 。

假设每一种面额的硬币有无限个。 

题目数据保证结果符合 32 位带符号整数。

> 输入：amount = 5, coins = [1, 2, 5]
> 
> 输出：4
> 
> 解释：有四种方式可以凑成总金额
> 
> 5=5
> 
> 5=2+2+1
> 
> 5=2+1+1+1
> 
> 5=1+1+1+1+1
------

> 解析

-------------

=== "Java"

    ```java
    class Solution {
        public int change(int amount, int[] coins) {
            int[][] dp = new int[coins.length + 1][amount + 1];
            dp[0][0] = 1;
            for(int i = 1 ; i <= coins.length ; i++){
                for(int j = 0; j <= amount; j++){
                    
                    dp[i][j] = dp[i - 1][j];
                    if(coins[i - 1] <= j){
                        dp[i][j] += dp[i][j - coins[i - 1]];
                    }
                }
            }
            return dp[ coins.length ][amount];

        }
    }

    ```