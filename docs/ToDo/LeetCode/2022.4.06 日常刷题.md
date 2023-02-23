<h3 style = "color :pink; text-align:center">2022.04.06 日常刷题</h3>



#### [166. 分数到小数](https://leetcode-cn.com/problems/fraction-to-recurring-decimal/)

🔑🔑 考点：字符串 | 模拟

🚴‍♀️🚴‍♀️ 难度： <span style = "color:gold; font-weight:bold">Medium</span>

🔗🔗 链接：https://leetcode-cn.com/problems/fraction-to-recurring-decimal/

📖📖 题目：

给定两个整数，分别表示分数的分子 numerator 和分母 denominator，以 字符串形式返回小数 。

如果小数部分为循环小数，则将循环的部分括在括号内。

如果存在多个答案，只需返回 任意一个 。

对于所有给定的输入，保证 答案字符串的长度小于 $10^4$ 。

💻💻 测试用例：

```
输入：numerator = 1, denominator = 2
输出："0.5"
输入：numerator = 1, denominator = 3
输出："0.(3)"
```

💡💡思路：

- 要点：模拟除法的手动计算过程
- 难点：如何确定每一个循环节？一旦遇到一个出现过的被除数就停止，遇到0就不需要进行循环了
- StringBuilder 同样可以使用insert操作
- 每次被除数都是原数字 * 10 再除以除数
- 非常烦恼的Long int转换：建议一开始就直接实现转换以减少错误

👩🏻‍💻🧑🏻‍💻 代码：

```Java
class Solution {
    public String fractionToDecimal(int numerator, int denominator) {
        StringBuilder sb = new StringBuilder();
        long num1 = (long)numerator;
        long num2 = (long)denominator;
        if(num1 < 0 && num2 > 0){
            num1 = (-1) * num1; 
            sb.append("-");
        }
        else if(num1 > 0 && num2 < 0){
            num2 = (-1) * num2;
            sb.append("-");
        }
        else if(num1 < 0 && num2 < 0){
            num1 = (-1) * num1;
            num2 = (- 1) * num2;
        }
        if(num1 % num2 == 0){
            sb.append((long )(num1 / num2));
            return sb.toString();
        }
        String next = get_underZero((num1 * 10), num2);
        if(num1 > num2){
            next =  get_underZero(((num1 % num2 ) * 10), num2);
        }
        else{
            next = get_underZero((num1 * 10), num2);
        }
        
        sb.append((long)(num1 / num2) );
        sb.append(".");
        sb.append(next);   
        return sb.toString();
    }

    public String get_underZero(Long a, Long b){
        
        Map<Long, Integer> map = new HashMap<>();
        StringBuilder sb = new StringBuilder();
        int idx = 0;
        while(!map.containsKey(a)){
            map.put(a , idx ++ );
            sb.append((int)(a / b));
            a = (a % b) * 10;
            if(a == 0){
                return sb.toString();
            }
        }
        sb.insert(map.get(a), "(");
        sb.append(")");
        return sb.toString();
        
    }
}
```

-----



#### [1023. 驼峰式匹配](https://leetcode-cn.com/problems/camelcase-matching/)

🔑🔑 考点：字符串 | 递增子序列

🚴‍♀️🚴‍♀️ 难度： <span style = "color:gold; font-weight:bold">Medium</span>

🔗🔗 链接：https://leetcode-cn.com/problems/camelcase-matching/

📖📖 题目：

如果我们可以将小写字母插入模式串 pattern 得到待查询项 query，那么待查询项与给定模式串匹配。（我们可以在任何位置插入每个字符，也可以插入 0 个字符。）

给定待查询列表 queries，和模式串 pattern，返回由布尔值组成的答案列表 answer。只有在待查项 queries[i] 与模式串 pattern 匹配时， answer[i] 才为 true，否则为 false。

💻💻 测试用例：

```

输入：queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FB"
输出：[true,false,true,true,false]
示例：
"FooBar" 可以这样生成："F" + "oo" + "B" + "ar"。
"FootBall" 可以这样生成："F" + "oot" + "B" + "all".
"FrameBuffer" 可以这样生成："F" + "rame" + "B" + "uffer".
```

💡💡思路：

- 要点：先后顺序+检查是否符合大写约束即可
- 判断方式: 这样需要顺序和模式串一致的，可以长的走一遍，短的采取“匹配则移动，不匹配则不动”的方式，最终判断是否符合要求，只需看短的（模式串）最终下标是不是长度。



👩🏻‍💻🧑🏻‍💻 代码：

```Java
class Solution {
    List<Boolean> ans = new ArrayList<>();
    public List<Boolean> camelMatch(String[] queries, String pattern) {
        char[] p = pattern.toCharArray();
        for(int i = 0; i < queries.length; i ++ ){
            ans.add(check( queries[i].toCharArray(), p ));
        }
        return ans;
    }

    public boolean check(char[] queries, char[] pattern){
        int idx = 0;
        for(int i = 0; i < queries.length; i ++ ){
            
            if(idx < pattern.length && queries[i] == pattern[idx]){
                idx ++ ;
            }
            else if(queries[i] >='A' && queries[i] <= 'Z') {
                if(idx >= pattern.length || pattern[idx] != queries[i]){
                    return false;
                }
            }
        }
        if(idx != pattern.length){
            return false;
        }
        return true;
    }
}
```



-----



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



#### [1239. 串联字符串的最大长度](https://leetcode-cn.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/)

🔑🔑 考点：回溯 | 字符串

🚴‍♀️🚴‍♀️ 难度： <span style = "color:gold; font-weight:bold">Medium</span>

🔗🔗 链接：https://leetcode-cn.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/

📖📖 题目：

给定一个字符串数组 arr，字符串 s 是将 arr 的含有 不同字母 的 子序列 字符串 连接 所得的字符串。

请返回所有可行解 s 中最长长度。

子序列 是一种可以从另一个数组派生而来的数组，通过删除某些元素或不删除元素而不改变其余元素的顺序。

💻💻 测试用例：

```
输入：arr = ["un","iq","ue"]
输出：4
解释：所有可能的串联组合是：
- ""
- "un"
- "iq"
- "ue"
- "uniq" ("un" + "iq")
- "ique" ("iq" + "ue")
最大长度为 4。
```

💡💡思路：

- 经典的回溯问题，这里终止的条件是看组成的是否符合唯一性。



👩🏻‍💻🧑🏻‍💻 代码：

```Java
class Solution {
    int ans = 0;
    public void dfs(List<String> arr, StringBuilder sb, int idx){
        if(!judge(sb)){
            return;
        }
        ans = Math.max(ans, sb.length());
        for(int i = idx ;i < arr.size(); i ++ ){
            sb.append(arr.get(i));
            dfs(arr, sb, i + 1);
            sb.delete(sb.length() - arr.get(i).length(), sb.length());
        }
    }
    public int maxLength(List<String> arr) {
        dfs(arr, new StringBuilder(), 0);
        return ans;

    }
    public boolean judge(StringBuilder sb){
        if(sb.length() > 26){
            return false;
        }
        int[] t = new int[26];
        Arrays.fill(t, 0);
        for(int i = 0; i < sb.length(); i ++ ){
            if(t[(int)(sb.charAt(i) - 'a' )] == 1){
                return false;
            }
            t[(int)(sb.charAt(i) - 'a' )] = 1;
        }
        return true;
    }
}
```





