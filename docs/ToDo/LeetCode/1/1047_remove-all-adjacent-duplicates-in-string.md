# 1047_删除字符串中的所有相邻重复项

<!-- 所有文件名必须是该题目的英文名 -->

!!! note
    <!-- 这里记载考察的数据结构、算法等 -->
    字符串 | 栈

- 🔑🔑 难度：
<!-- <span style = "color:gold; font-weight:bold">Medium</span> 中等 -->
<!-- <span style = "color:crisma; font-weight:bold">High</span> 困难 -->
<!-- <span style = "color:Green; font-weight:bold">Easy</span> 简单 -->

<!-- 题目简介 -->

> 给出由小写字母组成的字符串 S，重复项删除操作会选择两个相邻且相同的字母，并删除它们。
> 
> 在 S 上反复执行重复项删除操作，直到无法继续删除。
> 
> 在完成所有重复项删除操作后返回最终的字符串。答案保证唯一。


```
输入："abbaca"
输出："ca"
解释：
例如，在 "abbaca" 中，我们可以删除 "bb" 由于两字母相邻且相同，这是此时唯一可以执行删除操作的重复项。之后我们得到字符串 "aaca"，其中又只有 "aa" 可以执行重复项删除操作，所以最后的字符串为 "ca"。
```

------

??? note
    ?

-------------

=== "Java"

    ```java
    
    class Solution {
        public String removeDuplicates(String S) {
            Stack <Character> stack = new Stack<>();
            StringBuilder sb = new StringBuilder();
            char[] helper = S.toCharArray();
            for(int i = 0 ; i < helper.length; i++ ){
                if(stack.isEmpty()){
                    stack.push(helper[i]);
                }
                else{
                    if(stack.peek() == helper[i]){
                        stack.pop();
                    }
                    else{
                        stack.push(helper[i]);
                    }
                }
            }
            for(Character c:stack){
                sb.append(c);
            }
            return sb.toString();
        }
    }   
    ```