# 1663_具有给定数值的最小字符串

!!! note
    <!-- 这里记载考察的数据结构、算法等 -->
    贪心 | 字符串

- 🔑🔑 难度：<span style = "color:gold; font-weight:bold">Medium</span>


> 小写字符 的 数值 是它在字母表中的位置（从 1 开始），因此 a 的数值为 1 ，b 的数值为 2 ，c 的数值为 3 ，以此类推。
> 
> 字符串由若干小写字符组成，字符串的数值 为各字符的数值之和。例如，字符串 "abe" 的数值等于 1 + 2 + 5 = 8 。
> 
> 给你两个整数 n 和 k 。返回 长度 等于 n 且 数值 等于 k 的 字典序最小 的字符串。



```
输入：n = 3, k = 27
输出："aay"
输入：n = 5, k = 73
输出："aaszz"
```

-------


??? note

    一道贪心：字典序小：前面的先放a，放不满了就从后到前补‘z'

    这样可以保证最后一个a后面紧跟的一定是个比较小的字母，字典序就最小了



=== "Java"

    ```Java
    class Solution {
        public String getSmallestString(int n, int k) {
            char[] ans = new char[n];
            Arrays.fill(ans, 'a');
            int cur_all = n;
            int idx = n -1;
            while(cur_all < k){
                ans[idx] = 'z';
                idx -- ;
                cur_all += 25;
            }
            char cur_rep = (char)('z' - (cur_all - k));
            if(idx < n - 1)
                ans[idx + 1] = cur_rep;
            return String.valueOf(ans);
        }
    }
    ```









