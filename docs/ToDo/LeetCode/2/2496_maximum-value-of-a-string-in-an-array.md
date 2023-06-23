# 2496_数组中字符串的最大值

<!-- 所有文件名必须是该题目的英文名 -->

!!! note
    <!-- 这里记载考察的数据结构、算法等 -->
    字符串

- 🔑🔑 难度：<span style = "color:Green; font-weight:bold">Easy</span>
<!-- <span style = "color:gold; font-weight:bold">Medium</span> 中等 -->
<!-- <span style = "color:crisma; font-weight:bold">High</span> 困难 -->
<!-- <span style = "color:Green; font-weight:bold">Easy</span> 简单 -->

<!-- 题目简介 -->

> 一个由字母和数字组成的字符串的 值 定义如下：如果字符串 只 包含数字，那么值为该字符串在 10 进制下的所表示的数字。
> 
> 否则，值为字符串的 长度 。
> 
> 给你一个字符串数组 strs ，每个字符串都只由字母和数字组成，请你返回 strs 中字符串的 最大值 。


```

输入：strs = ["alic3","bob","3","4","00000"]
输出：5
解释：
- "alic3" 包含字母和数字，所以值为长度 5 。
- "bob" 只包含字母，所以值为长度 3 。
- "3" 只包含数字，所以值为 3 。
- "4" 只包含数字，所以值为 4 。
- "00000" 只包含数字，所以值为 0 。
所以最大的值为 5 ，是字符串 "alic3" 的值。

```

------

> 解析
>
> isdigit 逐一判断即可
-------------

=== "Python"

    ```Python
    class Solution:
        def maximumValue(self, strs: List[str]) -> int:
            res = 0
            for i in strs:
                if i.isdigit():
                    temp = i 
                    while len(temp) > 0:
                        if temp[0] == '0':
                            temp = temp[1 :]
                        else:
                            break
                    if len(temp) > 0:
                        res = max(res, int(temp))
                else:
                    res = max(res, len(i))
            return res
    ```