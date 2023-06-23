# 1249_移除无效的括号

<!-- 所有文件名必须是该题目的英文名 -->

!!! note
    <!-- 这里记载考察的数据结构、算法等 -->
    栈 ｜ 字符串

- 🔑🔑 难度：<span style = "color:gold; font-weight:bold">Medium</span> 
<!-- <span style = "color:gold; font-weight:bold">Medium</span> 中等 -->
<!-- <span style = "color:crisma; font-weight:bold">High</span> 困难 -->
<!-- <span style = "color:Green; font-weight:bold">Easy</span> 简单 -->

<!-- 题目简介 -->

> 给你一个由 '('、')' 和小写字母组成的字符串 s。
> 
> 你需要从字符串中删除最少数目的 '(' 或者 ')' （可以删除任意位置的括号)，使得剩下的「括号字符串」有效。
> 
> 请返回任意一个合法字符串。
> 
> 有效「括号字符串」应当符合以下 任意一条 要求：
> 
> 空字符串或只包含小写字母的字符串
> 
> 可以被写作 AB（A 连接 B）的字符串，其中 A 和 B 都是有效「括号字符串」
> 
> 可以被写作 (A) 的字符串，其中 A 是一个有效的「括号字符串」

```
输入：s = "lee(t(c)o)de)"
输出："lee(t(c)o)de"
解释："lee(t(co)de)" , "lee(t(c)ode)" 也是一个可行答案。

```

------

??? note 
    ？

    
-------------

=== "Java"

    ```java
    
    class Solution {
        public String minRemoveToMakeValid(String s) {
            Stack <Integer> stack = new Stack<>();
            boolean[] judge = new boolean[s.length()];
            StringBuilder sb = new StringBuilder();
            for(int i = 0; i < s.length(); i++){
                if(s.charAt(i) == '('){
                    stack.push(i);
                    judge[i] = true;
                }
                else {
                    if(s.charAt(i) == ')'&&!stack.isEmpty()){
                        judge[stack.peek()] = false;
                        stack.pop();
                        judge[i] = false;
                    }
                    else if(s.charAt(i) == ')'){
                        judge[i] = true;
                    }
                }
            }
            for(int i = 0; i <s.length(); i++){
                if(!judge[i]){
                    sb.append(s.charAt(i));
                }
            }
            return sb.toString();
        }
    }
    ```