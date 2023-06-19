# 686_重复叠加字符串匹配

!!! note
    <!-- 这里记载考察的数据结构、算法等 -->
    哈希表 | 动态规划


- 🔑🔑 难度：<span style = "color:gold; font-weight:bold">Medium</span>

给定两个字符串 a 和 b，寻找重复叠加字符串 a 的最小次数，使得字符串 b 成为叠加后的字符串 a 的子串，如果不存在则返回 -1。

注意：字符串 "abc" 重复叠加 0 次是 ""，重复叠加 1 次是 "abc"，重复叠加 2 次是 "abcabc"。



```
输入：a = "abcd", b = "cdabcdab"
输出：3
解释：a 重复叠加三遍后为 "abcdabcdabcd", 此时 b 是其子串。
```
----
- 一个十分暴力的解法：如果想要能包含解决，一定满足以下条件：
  - Cdabcdabcdab 也就是要么一段里面第前面加上一段，要么是一段里面后面加上一段
  - aaaa 对 a，直接重复
- 可以直接分情况进行讨论



```Java
class Solution {
    public int repeatedStringMatch(String a, String b) {
        for(int i = 0; i < b.length(); i ++ ){
            if(a.indexOf(b.charAt(i)) == -1){
                return -1;
            }
        }
        if(a.length() == 1){
            return b.length();
        }
        StringBuilder sb = new StringBuilder();
        int cnt = 0;
        while(sb.length() < b.length()){
            sb.append(a);
            cnt ++ ;
        }
        for(int i = 0 ; i < 3; i ++ ){
            if(sb.toString().indexOf(b) >= 0){
                return cnt + i;
            }
            sb.append(a);
        }
        return -1;
    }
}

```

