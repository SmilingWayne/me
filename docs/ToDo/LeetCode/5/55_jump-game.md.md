# 55_跳跃游戏

<!-- 所有文件名必须是该题目的英文名 -->

!!! note
    <!-- 这里记载考察的数据结构、算法等 -->
    哈希表 | 动态规划

- 🔑🔑 难度：<span style = "color:gold; font-weight:bold">Medium</span>
<!-- <span style = "color:gold; font-weight:bold">Medium</span> 中等 -->
<!-- <span style = "color:crisma; font-weight:bold">High</span> 困难 -->
<!-- <span style = "color:Green; font-weight:bold">Easy</span> 简单 -->

<!-- 题目简介 -->

> 给你一个非负整数数组 nums ，你最初位于数组的 第一个下标 。数组中的每个元素代表你在该位置可以跳跃的最大长度。
> 
> 判断你是否能够到达最后一个下标，如果可以，返回 true ；否则，返回 false 。
>

```
输入：nums = [2,3,1,1,4]
输出：true
解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标
```

------

??? note 
    只要还能走，那么就看看还能走多远，走不了就再说。

    
-------------

=== "Python"

    ```Python
    class Solution:
        def canJump(self, nums: List[int]) -> bool:
            if len(nums) == 1:
                return True
            res = nums[0]
            for i in range(1, len(nums)):
                if i > res:
                    return False
                if i <= res:
                    res = max(res, i + nums[i])
            return res >= len(nums) - 1
    ```
