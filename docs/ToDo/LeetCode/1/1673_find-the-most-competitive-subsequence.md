# 1673_找出最具竞争力的子序列

<!-- 所有文件名必须是该题目的英文名 -->

!!! note "要点"
    <!-- 这里记载考察的数据结构、算法等 -->
    单调栈

- 🔑🔑 难度：<span style = "color:gold; font-weight:bold">Medium</span>
<!-- <span style = "color:gold; font-weight:bold">Medium</span> 中等 -->
<!-- <span style = "color:crisma; font-weight:bold">High</span> 困难 -->
<!-- <span style = "color:Green; font-weight:bold">Easy</span> 简单 -->

<!-- 题目简介 -->

>
> 给你一个整数数组 nums 和一个正整数 k ，返回长度为 k 且最具 竞争力 的 nums 子序列。
> 
> 
> 数组的子序列是从数组中删除一些元素（可能不删除元素）得到的序列。
> 
> 在子序列 a 和子序列 b 第一个不相同的位置上，如果 a 中的数字小于 b 中对应的数字，那么我们称子序列 a 比子序列 b（相同长度下）更具 竞争力 。 例如，[1,3,4] 比 [1,3,5] 更具竞争力，在第一个不相同的位置，也就是最后一个位置上， 4 小于 5 。



```
输入：nums = [3,5,2,6], k = 2
输出：[2,6]
解释：在所有可能的子序列集合 {[3,5], [3,2], [3,6], [5,2], [5,6], [2,6]} 中，[2,6] 最具竞争力。

```

------

??? note "我的备注"
    单调栈：总是希望尽可能小的数字放在尽可能的前面。
    
-------------

=== "Python"

    ```Python
    class Solution:
        def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
            stack = []
            for idx, num in enumerate(nums):
            
                while len(stack) > 0 and stack[-1] > num and (k - len(stack) + 1 <= len(nums) - idx):
                    stack.pop()
                if len(stack) < k:
                    stack.append(num)
            return stack
    
    ```
