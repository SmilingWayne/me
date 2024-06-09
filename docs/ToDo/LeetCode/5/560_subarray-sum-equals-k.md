# 560_和为k的子数组

<!-- 所有文件名必须是该题目的英文名 -->

!!! note "要点"
    <!-- 这里记载考察的数据结构、算法等 -->
    哈希表 | 前缀和

- 🔑🔑 难度：<span style = "color:gold; font-weight:bold">Medium</span>
<!-- <span style = "color:gold; font-weight:bold">Medium</span> 中等 -->
<!-- <span style = "color:crisma; font-weight:bold">High</span> 困难 -->
<!-- <span style = "color:Green; font-weight:bold">Easy</span> 简单 -->

<!-- 题目简介 -->

> 给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的子数组的个数 。
> 
> 子数组是数组中元素的连续非空序列。
> 


```

示例 1：

输入：nums = [1,1,1], k = 2
输出：2
示例 2：

输入：nums = [1,2,3], k = 3
输出：2
```

------

??? note "我的备注"
    前缀和。同时，记录每一个前缀和出现的次数，这样出现一个新的数字之后，就可以根据“包含这个数字，同时余下数字的和是 k - num[i] 的前缀的数量”，就可以知道包含这个数字的和为k的子数组的个数。

    
-------------

=== "Python"

    ```Python
    class Solution:
        def subarraySum(self, nums: List[int], k: int) -> int:  
            dic = dict()
            dic[0] = 1
            cnt = 0
            pre = 0
            for i in range(len(nums)):
                pre += nums[i]
                if pre - k  in dic:
                    cnt += dic[pre - k]
                if pre not in dic:
                    dic[pre] = 1
                else:
                    dic[pre] = dic[pre] + 1
            return cnt

    ```
