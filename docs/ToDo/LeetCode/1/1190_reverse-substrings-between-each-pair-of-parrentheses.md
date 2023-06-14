#### [1190. 反转每对括号间的子串](https://leetcode-cn.com/problems/reverse-substrings-between-each-pair-of-parentheses/)

🔑🔑 考点：字符串 ｜ 栈

🚴‍♀️🚴‍♀️ 难度： <span style = "color:darkgreen; font-weight:bold">Medium</span>

🔗🔗 链接：https://leetcode-cn.com/problems/reverse-substrings-between-each-pair-of-parentheses/

📖📖 题目：

给出一个字符串 s（仅含有小写英文字母和括号）。

请你按照从括号内到外的顺序，逐层反转每对匹配括号中的字符串，并返回最终的结果。

注意，您的结果中 不应 包含任何括号

💻💻 测试用例：

```
输入：s = "(ed(et(oc))el)"
输出："leetcode"
解释：先反转子字符串 "oc" ，接着反转 "etco" ，然后反转整个字符串。
```

💡💡思路：

- 要点：如何反转字符串数组中的一部分？reverse(char[], int start, int end)
- 利用栈实现一部分的反转，注意这个Stack里面存储的不是char，而是char[] 的下标，这样实现速度会更加快一点，因为我们每次只需要翻转一部分字符就可以

👩🏻‍💻🧑🏻‍💻 代码：

```Java
class Solution {
    public String reverseParentheses(String s) {
       
        Stack<Character> stack = new Stack<>();
        StringBuilder sb2 = new StringBuilder();
        
        char[] t = s.toCharArray();
        for(int i =0 ; i  < s.length(); i ++ ){
            if(t[i] == ')'){
                sb2 = new StringBuilder();
                
                while(true){
                    if(stack.peek() == '('){
                        stack.pop();
                        break;
                    }
                    else{
                        sb2.append(stack.pop());
                    }
                }
                char[] t2 = sb2.toString().toCharArray();
          
                for(int k = 0; k < t2.length; k ++ ){
                    stack.push(t2[k]);
                }
                
            }
            else{
                stack.push(t[i]);
            }
        }
        StringBuilder sb3 = new StringBuilder();
        while(!stack.isEmpty()){
            sb3.append(stack.pop());
        }
        return sb3.reverse().toString();
    }
}
```

```Java
// 优化后的结果：1ms
class Solution {
    public String reverseParentheses(String s) {
        
        char[] ans = s.toCharArray();
        Stack<Integer> stack = new Stack<>();
        for(int i = 0; i < s.length(); i ++ ){
            if(ans[i] == ')'){
                // continue;
                reverseChar(ans, stack.pop() , i);
            }
            else if(ans[i] == '(' ){
                stack.push(i + 1);
            }
        }
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < ans.length; i ++ ){
            if(ans[i] == '(' || ans[i] == ')'){
                continue;
            }
            sb.append(ans[i]);
        }
        return sb.toString();
    }

    public void reverseChar(char[] ans, int start, int end){
        while(start < end){
            char temp = ans[start];
            ans[start] = ans[end];
            ans[end] = temp;
            start ++ ;
            end -- ;
        }
    }

}
```

