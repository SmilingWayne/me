# 2917_找出数组中的 K-or 值

<!-- 所有文件名必须是该题目的英文名 -->

!!! note ""
    <!-- 这里记载考察的数据结构、算法等 -->
    哈希表 | 动态规划

- 🔑🔑 难度：<span style = "color:Green; font-weight:bold">Easy</span> 

<!-- <span style = "color:gold; font-weight:bold">Medium</span> 中等 -->
<!-- <span style = "color:crisma; font-weight:bold">High</span> 困难 -->

<!-- 题目简介 -->

> 给你一个下标从 0 开始的整数数组 nums 和一个整数 k 。
>
> nums 中的 K-or 是一个满足以下条件的非负整数：
>
> 只有在 nums 中，至少存在 k 个元素的第 i 位值为 1 ，那么 K-or 中的第 i 位的值才是 1 。
> 返回 nums 的 K-or 值。
>
> 注意 ：对于整数 x ，如果 (2i AND x) == 2i ，则 x 中的第 i 位值为 1 ，其中 AND 为按位与运算符。


> 
```
输入：nums = [7,12,9,8,9,15], k = 4
输出：9
解释：nums[0]、nums[2]、nums[4] 和 nums[5] 的第 0 位的值为 1 。
nums[0] 和 nums[5] 的第 1 位的值为 1 。
nums[0]、nums[1] 和 nums[5] 的第 2 位的值为 1 。
nums[1]、nums[2]、nums[3]、nums[4] 和 nums[5] 的第 3 位的值为 1 。
只有第 0 位和第 3 位满足数组中至少存在 k 个元素在对应位上的值为 1 。因此，答案为 2^0 + 2^3 = 9 。
```

------

!!! note "笔记"
    - 想知道某个数字的二进制，第几位是否为1:
    ```Python
    (num >> i) & 1
    ```
    如果为真，那么num的第i位就是1；

    - 想知道某个字符串表示下二进制的值：一直遍历下去即可。

    ```Python
    (num) |= (1 << i)
    ```

    
-------------

=== "Java"

    ```java
    
    ```

=== "Python"

    ```Python
    class Solution:
        def findKOr(self, nums: List[int], k: int) -> int:
            records = [0 for _ in range(32)]
            res = 0
            for i in range(32):
                for idx, num in enumerate(nums):
                    if (num >> i) & 1:
                        records[i] += 1
                if records[i] >= k:
                    res |= (1 << i)
            return (res)
    ```