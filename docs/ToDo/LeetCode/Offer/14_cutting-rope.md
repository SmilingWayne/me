# Offer-14-I_割绳子

<!-- 所有文件名必须是该题目的英文名 -->

!!! note
    <!-- 这里记载考察的数据结构、算法等 -->
    动态规划

- 🔑🔑 难度：<span style = "color:gold; font-weight:bold">Medium</span>
<!-- <span style = "color:gold; font-weight:bold">Medium</span> 中等 -->
<!-- <span style = "color:crisma; font-weight:bold">High</span> 困难 -->
<!-- <span style = "color:Green; font-weight:bold">Easy</span> 简单 -->

<!-- 题目简介 -->

> 给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 k[0],k[1]...k[m-1] 。请问 k[0]*k[1]*...*k[m-1] 可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。


```
输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36
```

------

> 解析
>
> 第一个思路是，直接用$n^2$的DP，dp[i] = max(dp[i - j] * j, j * (i - j))
>
> 第二个思路是，通过数学计算判断只可能从4个数字中获得下一个解

-------------

=== "Python"

    ```Python
    
    class Solution:
        def cuttingRope(self, n: int) -> int:
            res = [0 for _ in range(n + 1)]
            res[2] = 1

            for i in range(3, n + 1):
                res[i] = max(max(2 * res[i - 2], 2 * (i - 2)), max(3 * ( i -3), 3 * res[i - 3]))
            return res[-1]

    class Solution:
        def cuttingRope(self, n: int) -> int:
            res = [0 for _ in range(n + 1)]
            for i in range(2, n + 1):
                tmp = 0
                for j in range(1, i):
                    tmp = max(tmp, max(res[i - j] * j, j * (i - j)))
            # print(res)
                res[i] = tmp
            return res[-1]
    ```