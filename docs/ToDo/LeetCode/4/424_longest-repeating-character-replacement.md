2022.04.07 Leetcode 日常刷题

---

#### [424. 替换后的最长重复字符](https://leetcode-cn.com/problems/longest-repeating-character-replacement/)

给你一个字符串 s 和一个整数 k 。你可以选择字符串中的任一字符，并将其更改为任何其他大写英文字符。该操作最多可执行 k 次。

在执行上述操作后，返回包含相同字母的最长子字符串的长度。

```
输入：s = "ABAB", k = 2
输出：4
解释：用两个'A'替换为两个'B',反之亦然。
```



- 经典的滑动窗口问题
- 速度怎么优化提升



```Java 

class Solution {
    public int characterReplacement(String s, int k) {
        int ans = 0;

        int[] count = new int[26];
        if(k == s.length()){
            return s.length();
        }
        char[] t = s.toCharArray();
        for(int i = 0; i < s.length() - k; i ++ ){
            int temp = check(t, i, k);
            // System.out.println(temp);
            if(temp > ans){
                ans = temp;
            }
        }
        return ans;

    }

    public int check(char[] t, int idx, int k){
        int[] count = new int[26];
        Arrays.fill(count, 0);
        int max_ = 0;
        for(int i = idx; i < t.length; i ++ ){
            count[t[i] - 'A'] ++ ;
            max_ = Math.max(max_, count[t[i] - 'A']);
            if((i - idx + 1) - max_> k){
                return i - idx;
            }
        }
        return t.length - idx;

    }
}


```

```C++
// 原理其实一样，需要固定住左边然后向右边滑动
class Solution {
public:
    int characterReplacement(string s, int k) { 
        vector<int> count(26,0);
        int left = 0, res = 0, maxN = 0;
        for(int i = 0; i < s.size(); i ++ ){
            count[s[i] - 'A'] ++ ;
            maxN = max(maxN, count[s[i] - 'A']);
            while(i - left - maxN + 1 > k ){
                
                count[s[left] - 'A'] -- ;
                left ++ ;
            }
            res = max(res, i - left + 1);
        }
        return res;
    }
};
```