# 2840_判断通过操作能否让字符串相等 II


<!-- 所有文件名必须是该题目的英文名 -->

!!! note
    <!-- 这里记载考察的数据结构、算法等 -->
    脑筋急转弯 ｜ 字符串

- 🔑🔑 难度：<span style = "color:gold; font-weight:bold">Medium</span>
<!-- <span style = "color:gold; font-weight:bold">Medium</span> 中等 -->
<!-- <span style = "color:crisma; font-weight:bold">High</span> 困难 -->
<!-- <span style = "color:Green; font-weight:bold">Easy</span> 简单 -->

<!-- 题目简介 -->

> 给你两个字符串 s1 和 s2 ，两个字符串长度都为 n ，且只包含 小写 英文字母。你可以对两个字符串中的 任意一个 执行以下操作 任意次：选择两个下标 i 和 j ，满足 i < j 且 j - i 是 偶数，然后 交换 这个字符串中两个下标对应的字符。
> 
> 如果你可以让字符串 s1 和 s2 相等，那么返回 true ，否则返回 false 。


> 
```
输入：s1 = "abcdba", s2 = "cabdab"
输出：true
解释：我们可以对 s1 执行以下操作：
- 选择下标 i = 0 ，j = 2 ，得到字符串 s1 = "cbadba" 。
- 选择下标 i = 2 ，j = 4 ，得到字符串 s1 = "cbbdaa" 。
- 选择下标 i = 1 ，j = 5 ，得到字符串 s1 = "cabdab" = s2 。
```

------

??? note 

    
-------------

=== "Python3"

    ```python
    class Solution:
        def checkStrings(self, s1: str, s2: str) -> bool:
            odd = [0 for _ in range(26)]
            even = [0 for _ in range(26)]

            for i in range(0, len(s1), 2):
                odd[ord(s1[i]) - ord('a')] += 1
                odd[ord(s2[i]) - ord('a')] -= 1
            
            for i in range(1, len(s1), 2):
                even[ord(s1[i]) - ord('a')] += 1
                even[ord(s2[i]) - ord('a')] -= 1
            
            for i in range(26):
                if odd[i] != 0 or even[i] != 0:
                    return False

            return True    
    ```

    当然了这道题可以体现Python的奇巧淫技：

    ```Python
    # 你永远可以相信Counter函数！
    class Solution:
        def checkStrings(self, s1: str, s2: str) -> bool:
            return Counter(s1[::2]) == Counter(s2[::2]) and  Counter(s1[1::2]) == Counter(s2[1::2])
    ```