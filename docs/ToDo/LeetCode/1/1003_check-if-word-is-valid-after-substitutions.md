# 1003_检查替换后的词是否有效

!!! note
    
    栈

- 🔑🔑 难度：<span style = "color:gold; font-weight:bold">Medium</span>



> 给你一个字符串 s ，请你判断它是否 有效 。
> 
> 字符串 s 有效 需要满足：假设开始有一个空字符串 t = "" ，你可以执行 任意次 下述操作将 t 转换为 s ：
> 
> 将字符串 "abc" 插入到 t 中的任意位置。形式上，t 变为 tleft + "abc" + tright，其中 t == tleft + tright 。注意，tleft 和 tright 可能为 空 。
> 
> 如果字符串 s 有效，则返回 true；否则，返回 false。



```
输出：true
解释：
"" -> "abc" -> "abcabc" -> "abcabcabc" -> "abcabcababcc"
因此，"abcabcababcc" 有效。
```


??? note
    
    思路：字符串 + Stack 只需根据前面的一个字母就可以判断当前是否合法:只要当前是a，先入栈；如果当前是b，栈顶不是a或者栈是空，输出false，否则入栈；如果当前是c，栈顶不是b或者栈是空，输出false；如果c符合条件，自动把栈的前两个pop掉。

--------

=== "Java"

    ```Java
    class Solution {
        public boolean isValid(String s) {
            
            Stack<Character> stack = new Stack<>();
            char[] t = s.toCharArray();
            if(s.charAt(0) != 'a'){
                return false;
            }
            for(int i = 0; i < t.length; i ++ ){
                if(t[i] == 'a'){
                    stack.push(t[i]);
                }
                else if(t[i] == 'b'){
                    if(stack.isEmpty() || stack.peek() != 'a'){
                        return false;
                    }
                    else{
                        stack.push(t[i]);
                    }
                }
                else{
                    if(stack.isEmpty() || stack.peek() != 'b'){
                        return false;
                    }
                    else{
                        for(int k = 0; k < 2; k ++ ){
                            stack.pop();
                        }
                    }
                }
            }
            return stack.isEmpty();
        }
    }
    ```

