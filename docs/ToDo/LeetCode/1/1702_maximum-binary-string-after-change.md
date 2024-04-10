# 1702_修改后的最大二进制字符串

<!-- 所有文件名必须是该题目的英文名 -->

!!! note
    <!-- 这里记载考察的数据结构、算法等 -->
    脑筋急转弯

- 🔑🔑 难度：<span style = "color:gold; font-weight:bold">Medium</span>
<!-- <span style = "color:gold; font-weight:bold">Medium</span> 中等 -->
<!-- <span style = "color:crisma; font-weight:bold">High</span> 困难 -->
<!-- <span style = "color:Green; font-weight:bold">Easy</span> 简单 -->

<!-- 题目简介 -->

> 给你一个二进制字符串 binary ，它仅有 0 或者 1 组成。你可以使用下面的操作任意次对它进行修改：
> 
> 操作 1 ：如果二进制串包含子字符串 "00" ，你可以用 "10" 将其替换。
> 
> 比方说， "00010" -> "10010"
> 
> 操作 2 ：如果二进制串包含子字符串 "10" ，你可以用 "01" 将其替换。
> 
> 比方说， "00010" -> "00001"
> 
> 请你返回执行上述操作任意次以后能得到的 最大二进制字符串 。如果二进制字符串 x 对应的十进制数字大于二进制字符串 y 对应的十进制数字，那么我们称二进制字符串 x 大于二进制字符串 y 。
> 

```
输入：binary = "000110"
输出："111011"
解释：一个可行的转换为：
"000110" -> "000101" 
"000101" -> "100101" 
"100101" -> "110101" 
"110101" -> "110011" 
"110011" -> "111011"
```

------

??? note 
    注意到，最终答案里如果有0的话，只可能有1个0.

    注意到，所有的0只能左移，不能右移。

    所以，第一个0右边的1一定都会在右边。其他的位置的1都可以变为0
    
-------------

=== "Python"

    ```Python
    class Solution:
        def maximumBinaryString(self, binary: str) -> str:
            if len(binary) <= 1 or binary == "10" or binary == "11":
                return binary 
            
            oneNums = binary.count("1")
            oneBefore = 0
            if oneNums == len(binary):
                return binary
            for i in range(len(binary)):
                if binary[i] == "1":
                    oneBefore += 1
                elif binary[i] == "0":
                    break
            
            return "1" * (len(binary) - oneNums + oneBefore - 1) + "0" + "1" * (oneNums - oneBefore)
    ```
