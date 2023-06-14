<h1>2022.4.19 Leetcode 日常刷题</h1>

---

📖📖 821. 字符的最短距离

✏️✏️难度：<span style = "color: green; font-weight:bold">Easy</span>
     
🔗🔗 : https://leetcode-cn.com/problems/shortest-distance-to-a-character/

💡💡
```
给你一个字符串 s 和一个字符 c ，且 c 是 s 中出现过的字符。
返回一个整数数组 answer ，其中 answer.length == s.length 且 
answer[i] 是 s 中从下标 i 到离它 最近 的字符 c 的 距离 。
两个下标 i 和 j 之间的 距离 为 abs(i - j) ，其中 abs 是绝对值函数。
```

💻💻：
```
输入：s = "loveleetcode", c = "e"
输出：[3,2,1,0,1,0,0,1,2,2,1,0]
```
- 思路：小DP
- 每个位置的数字只有两种情况：这个数字距离前面的那个c，或这个数字距离后面那个c，两者进行比较即可


```java
class Solution {
    public int[] shortestToChar(String s, char c) {
        int[] ans = new int[s.length()];
        Arrays.fill(ans, s.length() + 1);
        int idx = -10005;
        for(int i = 0; i < s.length(); i ++ ){
            if(c == s.charAt(i)){
                idx = i;
            }
            ans[i] = i - idx;
        }
        idx = 20010;
        for(int i = s.length() - 1; i >= 0; i -- ){
            if(c == s.charAt(i)){
                idx = i;
            }
            ans[i] = Math.min(ans[i], idx - i);
        }
        return ans;

    }
}

```