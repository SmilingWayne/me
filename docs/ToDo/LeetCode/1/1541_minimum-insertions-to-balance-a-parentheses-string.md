# 1541_检查一个字符串是否包含所有长度为 K 的二进制子串


!!! note
    <!-- 这里记载考察的数据结构、算法等 -->
    位运算

- 🔑🔑 难度：<span style = "color:gold; font-weight:bold">Medium</span>


> 给你一个二进制字符串 `s` 和一个整数 `k` 。如果所有长度为 `k` 的二进制字符串都是 `s` 的子串，请返回 `true` ，否则请返回 `false` 。



```
输入：s = "00110110", k = 2
输出：true
解释：长度为 2 的二进制串包括 "00"，"01"，"10" 和 "11"。它们分别是 s 中下标为 0，1，3，2 开始的长度为 2 的子串。
```

------------

> 原理：长度k的二进制串一定是2^k个
> 可以根据字符串本身进行遍历寻找（反过来想）
> HashSet执行去重，看看整个字符串有多少个不同的k长度的子串


=== "Java"

    ```Java
    class Solution {
        public int minInsertions(String s) {
            char[] chars = s.toCharArray();
            int res = 0, N = chars.length, left = 0;
            for (int i = 0; i < N; i++) {
                if (chars[i] == '(') {
                    left++;
                } else {
                    // 没有左括号了，需要加一个左括号，res++
                    if (left == 0) res++;
                    else left--;
                    
                    // 以下两种情况只有一个右括号，需要再加一个右括号，res++
                    if (i == N - 1 || chars[i + 1] != ')') res++;
                    else i++;
                }
            }
            return res + left * 2; // 剩余的左括号需要2倍的右括号匹配
        }
    }
    ```



