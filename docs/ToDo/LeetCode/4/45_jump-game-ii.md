# 45_跳跃游戏II

<!-- 所有文件名必须是该题目的英文名 -->

!!! note
    <!-- 这里记载考察的数据结构、算法等 -->
    Greedy

- 🔑🔑 难度：<span style = "color:gold; font-weight:bold">Medium</span>
<!-- <span style = "color:gold; font-weight:bold">Medium</span> 中等 -->
<!-- <span style = "color:crisma; font-weight:bold">High</span> 困难 -->
<!-- <span style = "color:Green; font-weight:bold">Easy</span> 简单 -->

<!-- 题目简介 -->

> 给定一个长度为 n 的 0 索引整数数组 nums。初始位置为 nums[0]。
> 
> 每个元素 nums[i] 表示从索引 i 向前跳转的最大长度。换句话说，如果你在 nums[i] 处，你可以跳转到任意 nums[i + j] 处:
> 
> 0 <= j <= nums[i] 
> 
> i + j < n
> 
> 返回到达 nums[n - 1] 的最小跳跃次数。生成的测试用例可以到达 nums[n - 1]。
> 

```
输入: nums = [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。

```

------

??? note 
    用一个MaxRange记录一下，在当前位置能到达的最远距离，以及用curr记录当前的跳跃步骤。

    - 不知道为什么这个玩意现在竟然没写出来...2024.05.20 

    
-------------

=== "Python"

    ```Python
    class Solution:
        def jump(self, nums: List[int]) -> int:
            res = 0
            curr = 0
            maxRange = 0
            for i in range(len(nums) - 1):
                maxRange = max(maxRange, nums[i] + i)
                if i == curr:
                    curr = maxRange
                    res += 1
            return res
                
    ```
