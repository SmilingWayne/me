# 20_有效的括号

<!-- 所有文件名必须是该题目的英文名 -->

!!! note
    <!-- 这里记载考察的数据结构、算法等 -->
    stack | string

- 🔑🔑 难度：<span style = "color:Green; font-weight:bold">Easy</span>
<!-- <span style = "color:gold; font-weight:bold">Medium</span> 中等 -->
<!-- <span style = "color:crisma; font-weight:bold">High</span> 困难 -->
<!-- <span style = "color:Green; font-weight:bold">Easy</span> 简单 -->

<!-- 题目简介 -->

> 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
> 
> 有效字符串需满足：
> 左括号必须用相同类型的右括号闭合。
> 左括号必须以正确的顺序闭合。
> 每个右括号都有一个对应的相同类型的左括号。

```
输入：s = "()[]{}"
输出：true
```

------

> 解析

-------------

=== "Python"

    ```python
    class Solution:
        def isValid(self, s: str) -> bool:
            stack = []
        
            for item in s:
                if item == '(':
                    stack.append(")")
                elif item == '[':
                    stack.append("]")
                elif item == '{':
                    stack.append("}")
                elif not stack or stack[-1] != item:
                    return False
                else:
                    stack.pop()
            
            return True if not stack else False
    ```

=== "Java"

    ```java
     // 有点丑陋了这里面的代码
    class Solution {
        public boolean isValid(String s) {
            Stack<Character>stack = new Stack<Character>();
            for(char c: s.toCharArray()){
                if(!stack.isEmpty()){
                    char helper = stack.peek();
                    if(helper=='('&&c==')'||helper =='['&&c==']'||helper == '{'&&c=='}')
                    {   stack.pop();
                        continue;
                    }
                }
                stack.push(c);
            }
            return stack.isEmpty();
        }
    }
    
    ```