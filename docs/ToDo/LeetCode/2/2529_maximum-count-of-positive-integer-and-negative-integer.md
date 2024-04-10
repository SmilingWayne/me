# 2529_正整数和负整数的最大计数

<!-- 所有文件名必须是该题目的英文名 -->

!!! note
    <!-- 这里记载考察的数据结构、算法等 -->
    二分查找

- 🔑🔑 难度：<span style = "color:Green; font-weight:bold">Easy</span> 
<!-- <span style = "color:gold; font-weight:bold">Medium</span> 中等 -->
<!-- <span style = "color:crisma; font-weight:bold">High</span> 困难 -->


<!-- 题目简介 -->

> 给你一个按 非递减顺序 排列的数组 nums ，返回正整数数目和负整数数目中的最大值。
> 
> 换句话讲，如果 nums 中正整数的数目是 pos ，而负整数的数目是 neg ，返回 pos 和 neg二者中的最大值。
> 
> 注意：0 既不是正整数也不是负整数。

```
输入：nums = [-2,-1,-1,1,2,3]
输出：3
解释：共有 3 个正整数和 3 个负整数。计数得到的最大值是 3 。
```

------

??? note 
    二分查找，查找的是第一个0的位置和第一个比0大的数字在大位置。

    
-------------

=== "Python"

    ```Python
    class Solution:
        def low(self, nums, val):
            l, r = 0, len(nums)
            while l < r:
                m = (l + r) // 2
                if nums[m] >= val:
                    r = m 
                else:
                    l = m + 1
            return l

        def maximumCount(self, nums: List[int]) -> int:
            l0 = self.low(nums, 0)
            l1 = self.low(nums, 1)
            return max(l0, len(nums) - l1)
            


    ```
