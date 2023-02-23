#### [942. 增减字符串匹配](https://leetcode.cn/problems/di-string-match/)

🔑🔑 考点：双指针 

🚴‍♀️🚴‍♀️ 难度： <span style = "color:darkgreen; font-weight:bold">Easy</span>

🔗🔗 链接：https://leetcode.cn/problems/di-string-match/

📖📖 题目：

由范围 [0,n] 内所有整数组成的 n + 1 个整数的排列序列可以表示为长度为 n 的字符串 s ，其中:

如果 perm[i] < perm[i + 1] ，那么 s[i] == 'I' 
如果 perm[i] > perm[i + 1] ，那么 s[i] == 'D' 
给定一个字符串 s ，重构排列 perm 并返回它。如果有多个有效排列perm，则返回其中 任何一个 。

💻💻 测试用例：

```
输入：s = "IDID"
输出：[0,4,1,3,2]
输入：s = "III"
输出：[0,1,2,3]
```

💡💡思路：

-  其实本质上是个贪心。维护的双指针一个负责保存“目前的最小元素”和“目前的最大元素”，遇到I就说明当前的比较小，自动放最小元素，遇到D就贪心地放入最大元素。最后会形成满足条件的解。

👩🏻‍💻🧑🏻‍💻 代码：

```Java
class Solution {
    public int[] diStringMatch(String s) {
        int len = s.length();
        int start = 0;
        int end = len;
        int[] ans = new int[len + 1];
        for(int i =0 ;i < len; i ++ ){
            if(s.charAt(i) == 'I'){
                ans[i] = start;
                start ++ ;
            }
            else{
                ans[i] = end;
                end -- ;
            }
            if(i == len - 1){
                ans[i + 1] = start;
            }
        }
        return ans;
    }
}
```









