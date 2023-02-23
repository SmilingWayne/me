<center>2022.3.27 Leetcode 刷题</center>

---

#### [32. 最长有效括号](https://leetcode-cn.com/problems/longest-valid-parentheses/)

难度【Medium】

给你一个只包含 `'('` 和 `')'` 的字符串，找出最长有效（格式正确且连续）括号子串的长度。

```
输入：s = "(()"
输出：2
解释：最长有效括号子串是 "()"
```

- 思路：（1）对于有效括号问题，想到stack的压入和弹出
- 如何找到有效的长度?
- 思路：每一个括号的有效情况都是可以被判断出来的，
  - （1）一个单独压入stack 的左括号一定是不合理的
  - （2）在出入stack 的操作结束之后所有的剩下来的括号一定都是不合理的

- 笨方法如下：
  - 判断在整个字符串中一个括号是否是可行的，分别标记，问题就转化成求一个最长的可行的序列

```Java 
class Solution {
    int ans = 0;
    public int longestValidParentheses(String s) {
        int[] list = new int[s.length()];
        Stack<Integer> stack = new Stack<>();
        for(int i = 0; i < s.length(); i ++ ){
            if(stack.size() == 0 && s.charAt(i) == ')'){
                list[i] = 1;
            }
            else if(stack.size() > 0 && s.charAt(i) == ')'){
                stack.pop();
            }
            else{
                stack.push(i);
            }
        }
        while(stack.size() > 0){
            list[stack.pop()] = 1;
        }
        for(int i = 0; i < s.length() - 1; i ++ ){
            if(list[i] == 1){
                continue;
            }
            int temp = 0;
            while(i < list.length && list[i] == 0){
                temp ++ ;
                i ++ ;
            }
            ans = Math.max(ans, temp);
        }
        return ans;
    }
}
```



- 或者DP解法同样是可行的选择

```Java

class Solution {
   
    public int longestValidParentheses(String s) {
        int ans = 0;
        int[] dp = new int[s.length()];
        for(int i = 1; i < s.length(); i ++ ){
            
            // ()()     (())
            if(s.charAt(i) == ')'){
                
                    int j = i - dp[i - 1] - 1;
                    if(j >=0 && s.charAt(j)== '('){
                        dp[i] = dp[i -1] + 2;
                        if(j > 0){
                            dp[i] += dp[j - 1];
                        }
                    } 
                    
                
            }
        }
        for(int i = 0; i < dp.length; i ++ ){
            ans = Math.max(ans ,dp[i]);
        }
        return ans;
        
    }
}