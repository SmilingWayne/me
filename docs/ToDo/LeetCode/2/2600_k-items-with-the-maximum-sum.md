# 2600_k件商品的最大和

<!-- 所有文件名必须是该题目的英文名 -->

!!! note
    <!-- 这里记载考察的数据结构、算法等 -->
    简单题

- 🔑🔑 难度：<span style = "color:Green; font-weight:bold">Easy</span>
<!-- <span style = "color:gold; font-weight:bold">Medium</span> 中等 -->
<!-- <span style = "color:crisma; font-weight:bold">High</span> 困难 -->
<!-- <span style = "color:Green; font-weight:bold">Easy</span> 简单 -->

<!-- 题目简介 -->

> 袋子中装有一些物品，每个物品上都标记着数字 1 、0 或 -1 。
> 
> 给你四个非负整数 numOnes 、numZeros 、numNegOnes 和 k 。
> 
> 袋子最初包含：

> numOnes 件标记为 1 的物品。
> 
> numZeroes 件标记为 0 的物品。
> 
> numNegOnes 件标记为 -1 的物品。
> 
> 现计划从这些物品中恰好选出 k 件物品。返回所有可行方案中，物品上所标记数字之和的最大值

```
输入：numOnes = 3, numZeros = 2, numNegOnes = 0, k = 2
输出：2
解释：袋子中的物品分别标记为 {1, 1, 1, 0, 0} 。取 2 件标记为 1 的物品，得到的数字之和为 2 。
可以证明 2 是所有可行方案中的最大值。

```

------

??? note 

    
-------------

=== "Python"

    ```Python
    class Solution:
        def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
            if k <= numOnes:
                return k 
            
            elif k <= numOnes + numZeros:
                return numOnes
            
            else:
                return numOnes + ( numZeros + numOnes - k)

    
    ```