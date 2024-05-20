# 213_打家劫舍 - II

<!-- 所有文件名必须是该题目的英文名 -->

!!! note
    <!-- 这里记载考察的数据结构、算法等 -->
    动态规划

- 🔑🔑 难度：<span style = "color:gold; font-weight:bold">Medium</span>
<!-- <span style = "color:gold; font-weight:bold">Medium</span> 中等 -->
<!-- <span style = "color:crisma; font-weight:bold">High</span> 困难 -->
<!-- <span style = "color:Green; font-weight:bold">Easy</span> 简单 -->

<!-- 题目简介 -->

> 你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都 围成一圈 ，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警 。
> 
> 给定一个代表每个房屋存放金额的非负整数数组，计算你 在不触动警报装置的情况下 ，今晚能够偷窃到的最高金额。


```
输入：nums = [2,3,2]
输出：3
解释：你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。
```

------

!!! note "打家劫舍的模板"

    ```Python
    def rob_(nums):
        f0 = f1 = 0
        for x in nums:
            f0, f1 = f1, max(f0 + x, f1)
        return f1
    ```

    
-------------

=== "Python3"

    ```python
    class Solution:
        def rob(self, nums: List[int]) -> int:
            def rob_(nums):
                f0 = f1 = 0
                for x in nums:
                    f0, f1 = f1, max(f0 + x, f1)
                return f1


            return max(nums[0] + rob_(nums[2: - 1]), rob_(nums[1:]))
    ```