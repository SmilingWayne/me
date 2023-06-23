# 1513_仅含 1 的子串数


<!-- 所有文件名必须是该题目的英文名 -->

!!! note
    <!-- 这里记载考察的数据结构、算法等 -->
    字符串 | 数据类型转换 

- 🔑🔑 难度：<span style = "color:gold; font-weight:bold">Medium</span>


> 给你一个二进制字符串 s（仅由 '0' 和 '1' 组成的字符串）。
> 
> 返回所有字符都为 1 的子字符串的数目。
> 
> 由于答案可能很大，请你将它对 10^9 + 7 取模后返回。



```
输入：s = "0110111"
输出：9
输入：s = "111111"
输出：21

```

---------

> 只要找“连续1”的个数t，利用$ (t + 1) * t / 2$的公式计算即可
> 
> 该题的难度来自于数据类型转换：统计$(t + 1) * t / 2$ 很容易溢出int 的范围，需要用long进行保存





=== "Java"

    ```Java
    class Solution {
        public int numSub(String s) {
            long ans = 0;
            for(int i = 0; i < s.length();i ++ ){
                long cnt = 0;
                if(s.charAt((int)i) == '1'){
                    while(i < s.length() && s.charAt(i) == '1'){
                        i ++ ;
                        cnt ++ ;
                    }
                    ans += (long)( (cnt + 1) * (cnt )  / 2 );
                    i -- ;
                }
            }
            ans %= (1e9+7);
            return (int)ans;

        }
    }
    ```

