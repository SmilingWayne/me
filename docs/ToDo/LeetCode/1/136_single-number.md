# 136_只出现一次的数字

<!-- 所有文件名必须是该题目的英文名 -->

!!! note
    <!-- 这里记载考察的数据结构、算法等 -->
    异或运算

- 🔑🔑 难度：<span style = "color:Green; font-weight:bold">Easy</span>
<!-- <span style = "color:gold; font-weight:bold">Medium</span> 中等 -->
<!-- <span style = "color:crisma; font-weight:bold">High</span> 困难 -->
<!-- <span style = "color:Green; font-weight:bold">Easy</span> 简单 -->

<!-- 题目简介 -->

>
> 
```
```

------

!!! note "异或运算"
    任何数字和他自己进行异或运算的结果都是0。

    
-------------

=== "Python"

    ```Python 
    class Solution:
        def singleNumber(self, nums: List[int]) -> int:
            res = 0
            for i in nums:
                res ^= i
            return res

    ```
