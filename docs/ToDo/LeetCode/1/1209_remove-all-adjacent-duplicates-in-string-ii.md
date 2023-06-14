#### [1209. 删除字符串中的所有相邻重复项 II](https://leetcode-cn.com/problems/remove-all-adjacent-duplicates-in-string-ii/)

🔑🔑 考点：

🚴‍♀️🚴‍♀️ 难度： <span style = "color:gold; font-weight:bold">Medium</span>

🔗🔗 链接：https://leetcode-cn.com/problems/remove-all-adjacent-duplicates-in-string-ii/

📖📖 题目：

给你一个字符串 s，「k 倍重复项删除操作」将会从 s 中选择 k 个相邻且相等的字母，并删除它们，使被删去的字符串的左侧和右侧连在一起。

你需要对 s 重复进行无限次这样的删除操作，直到无法继续为止。

在执行完所有删除操作后，返回最终得到的字符串。

本题答案保证唯一。

💻💻 测试用例：

```
输入：s = "abcd", k = 2
输出："abcd"
解释：没有要删除的内容。
```

💡💡思路：

- 如何不超时？如果每次都类似模拟，一定会超时
- 栈的妙用，由于每次删除只会删除当下的这个字符的重复项，前面的字符的情况不受影响，所以可以利用int[] 保留当前字符和已经有的数量，如果遍历到的那个字符和栈顶一样，并且满足了重复个数，就删除。

👩🏻‍💻🧑🏻‍💻 代码：

```Java
// 模拟：一种超时的做法
class Solution {
    public String removeDuplicates(String s, int k) {
        
        while(true){
            int size = s.length();
            char[] t = s.toCharArray();
            Stack<Character> stack = new Stack<>();
            char top_ = '#';
            int top_cnt = 0;
            if(s.length() < k){
                return s;
            }
            for(int i = 0; i < t.length; i ++ ){
                if(top_ == '#'){
                    top_cnt = 1;
                    top_ = t[i];
                    stack.push(t[i]);
                }
                else if(top_ == t[i]){
                    top_cnt ++ ;
                    if(top_cnt == k){
                        for(int j = 0; j < k - 1 ; j ++ ){
                            stack.pop();
                        }
                        top_ = '#';
                    }
                    else{
                        stack.push(t[i]);
                    }
                }
                else{
                    stack.push(t[i]);
                    top_ = t[i];
                    top_cnt = 1;
                }
            }
            s = "";
            StringBuilder sb = new StringBuilder();
            while(!stack.isEmpty()){
                sb.append(stack.pop());
            }   
            s = sb.reverse().toString();
            if(s.length() == size || s.isEmpty()){
                break;
            }
        }
        return s;
    }
}

// 方法二：好慢！
class Solution {
    public String removeDuplicates(String s, int k) {
        
        Stack<int[]> stack = new Stack<>();
        char[] t = s.toCharArray();
        for(int i = 0 ; i < s.length(); i ++ ){
            if(stack.isEmpty()){
                int[] add = {t[i] - 'a', 1};
                stack.push(add);
                continue;
            }
            int[] pre = stack.peek();
            if((char)(pre[0] + 'a') == t[i]){
                if(pre[1] == k - 1){
                    for(int j = 0; j < k - 1; j ++ ){
                        stack.pop();
                    }
                }
                else{
                    int[] add = {t[i] - 'a', pre[1] + 1};
                    stack.push(add);
                }
            }
            else{
                int[] add = {t[i] - 'a', 1};
                stack.push(add);
            }
        }
        StringBuilder sb = new StringBuilder();
        while(!stack.isEmpty()){
            sb.append((char)('a' + stack.pop()[0]  ) );

        }
        return sb.reverse().toString();
    }
}
```



----



