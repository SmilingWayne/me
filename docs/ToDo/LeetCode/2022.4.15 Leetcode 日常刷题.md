2022.4.15 Leetcode 日常刷题

---

#### [1525. 字符串的好分割数目](https://leetcode-cn.com/problems/number-of-good-ways-to-split-a-string/)

难度：【Medium】

```
给你一个字符串 s ，一个分割被称为 「好分割」 当它满足：将 s 分割成 2 个字符串 p 和 q ，它们连接起来等于 s 且 p 和 q 中不同字符的数目相同。

请你返回 s 中好分割的数目。

 

示例 1：

输入：s = "aacaba"
输出：2
解释：总共有 5 种分割字符串 "aacaba" 的方法，其中 2 种是好分割。
("a", "acaba") 左边字符串和右边字符串分别包含 1 个和 3 个不同的字符。
("aa", "caba") 左边字符串和右边字符串分别包含 1 个和 3 个不同的字符。
("aac", "aba") 左边字符串和右边字符串分别包含 2 个和 2 个不同的字符。这是一个好分割。
("aaca", "ba") 左边字符串和右边字符串分别包含 2 个和 2 个不同的字符。这是一个好分割。
("aacab", "a") 左边字符串和右边字符串分别包含 3 个和 1 个不同的字符。

```

- 字符串 + 动态规划 
- 前缀和后缀和，不需要map

```Java
class Solution {
    public int numSplits(String s) {
        int n = s.length();
        int[] left = new int[n + 2];
        int[] right = new int[n + 2];
        boolean[] recLeft = new boolean[26];
        boolean[] recRight = new boolean[26];
        for (int i = 1; i <= n; i++) {
            int c = s.charAt(i - 1) - 'a';
            if (recLeft[c]) {
                left[i] = left[i - 1];
            } else {
                recLeft[c] = true;;
                left[i] = left[i - 1] + 1;
            }
        }
        for (int i = n; i > 0; i--) {
            int c = s.charAt(i - 1) - 'a';
            if (recRight[c]) {
                right[i] = right[i + 1];
            } else {
                recRight[c] = true;
                right[i] = right[i + 1] + 1;
            }
        }
        int ret = 0;
        for (int i = 1; i < n; i++) {
            if (left[i] == right[i + 1]) {
                ret++;
            }
        }
        return ret;
    }
}
```

