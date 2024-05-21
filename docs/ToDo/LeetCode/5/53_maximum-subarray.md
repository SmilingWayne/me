# 53_最大子数组和

<!-- 所有文件名必须是该题目的英文名 -->

!!! note
    <!-- 这里记载考察的数据结构、算法等 -->
    动态规划

- 🔑🔑 难度：<span style = "color:gold; font-weight:bold">Medium</span>
<!-- <span style = "color:gold; font-weight:bold">Medium</span> 中等 -->
<!-- <span style = "color:crisma; font-weight:bold">High</span> 困难 -->
<!-- <span style = "color:Green; font-weight:bold">Easy</span> 简单 -->

<!-- 题目简介 -->

> 给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。（子数组是数组中的一个连续部分。）
>

```
输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
```

------

??? note 
    动态规划，一个数组的最大字数组和，只取决于前 n - 1 位的最大子数组和与是否选取最后一位。

    
-------------

=== "Python"

    ```Python
    class Solution:
        def maxSubArray(self, nums: List[int]) -> int:
            premax = 0
            res = nums[0]
            for i in range(len(nums)):
                premax = max(premax + nums[i], nums[i])
                res = max(res, premax)
            return res
    
    ```
