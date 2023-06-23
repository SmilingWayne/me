# 1021_删除最外层的括号

<!-- 所有文件名必须是该题目的英文名 -->

!!! note
    <!-- 这里记载考察的数据结构、算法等 -->
    字符串

- 🔑🔑 难度：
<!-- <span style = "color:gold; font-weight:bold">Medium</span> 中等 -->
<!-- <span style = "color:crisma; font-weight:bold">High</span> 困难 -->
<!-- <span style = "color:Green; font-weight:bold">Easy</span> 简单 -->

<!-- 题目简介 -->

> 有效括号字符串为空 ""、"(" + A + ")" 或 A + B ，其中 A 和 B 都是有效的括号字符串，+ 代表字符串的连接。
> 例如，""，"()"，"(())()" 和 "(()(()))" 都是有效的括号字符串。
> 
> 如果有效字符串 s 非空，且不存在将其拆分为 s = A + B 的方法，我们称其为原语（primitive），其中 A 和 B 都是非空有效括号字符串。
> 
> 给出一个非空有效字符串 s，考虑将其进行原语化分解，使得：s = P_1 + P_2 + ... + P_k，其中 P_i 是有效括号字符串原语。
> 对 s 进行原语化分解，删除分解中每个原语字符串的最外层括号，返回 s 。
 
```
输入：s = "(()())(())"
输出："()()()"
解释：
输入字符串为 "(()())(())"，原语化分解得到 "(()())" + "(())"，
删除每个部分中的最外层括号后得到 "()()" + "()" = "()()()"。

```
-----

??? note
    ?

-------------

=== "Java"

    ```java

    class Solution {
        public String removeOuterParentheses(String S) {
            StringBuilder sb = new StringBuilder();
            int level = 0;
            for (char c : S.toCharArray()) {
                if (c == ')') --level;
                if (level >= 1) sb.append(c);
                if (c == '(') ++level;
            }
            return sb.toString();
        }
    }


    
    ```