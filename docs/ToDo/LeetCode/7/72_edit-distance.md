# 72_编辑距离

<!-- 所有文件名必须是该题目的英文名 -->

!!! note
    <!-- 这里记载考察的数据结构、算法等 -->
    动态规划

- 🔑🔑 难度：<span style = "color:gold; font-weight:bold">Medium</span>
<!-- <span style = "color:gold; font-weight:bold">Medium</span> 中等 -->
<!-- <span style = "color:crisma; font-weight:bold">High</span> 困难 -->
<!-- <span style = "color:Green; font-weight:bold">Easy</span> 简单 -->

<!-- 题目简介 -->

> 给你两个单词 word1 和 word2， 请返回将 word1 转换成 word2 所使用的最少操作数  。

> 你可以对一个单词进行如下三种操作：

> 插入一个字符
> 
> 删除一个字符
> 
> 替换一个字符

```
输入：word1 = "intention", word2 = "execution"
输出：5
解释：
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')

```

------

??? note 

    
-------------

=== "Python"

    ```Python
    class Solution:
        def minDistance(self, word1: str, word2: str) -> int:
            dp = [[0] * (len(word1) + 1) for _ in range(len(word2) + 1)]
            for i in range(len(word1) + 1):
                dp[0][i] = i 
            for j in range(len(word2) + 1):
                dp[j][0] = j
            
            for i in range(1, len(word2) + 1):
                for j in range(1, len(word1) + 1):
                    if word2[i - 1] == word1[j - 1]:
                        dp[i][j] = dp[i - 1][j - 1]
                    else:
                        dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1

            return dp[-1][-1]
    
    ```
