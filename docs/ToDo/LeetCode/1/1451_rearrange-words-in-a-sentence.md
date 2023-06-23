# 1451_重新排列句子中的单词


!!! note
    <!-- 这里记载考察的数据结构、算法等 -->
    ?


- 🔑🔑 难度：<span style = "color:gold; font-weight:bold">Medium</span>


> 句子 是一个用空格分隔单词的字符串。给你一个满足下述格式的句子 text :
> 
> 句子的首字母大写
> 
> text 中的每个单词都用单个空格分隔。
> 
> 请你重新排列 text 中的单词，使所有单词按其长度的升序排列。如果两个单词的长度相同，则保留其在原句子中的相对顺序。
> 
> 请同样按上述格式返回新的句子。


```
输入：text = "Leetcode is cool"
输出："Is cool leetcode"
解释：句子中共有 3 个单词，长度为 8 的 "Leetcode" ，长度为 2 的 "is" 以及长度为 4 的 "cool" 。
输出需要按单词的长度升序排列，新句子中的第一个单词首字母需要大写。

```

-----


> 难点：Lambda表达式
> 
> String必须转换成char类型才能方便修改


-----

=== "Java"

    ```Java
    class Solution {
        public String arrangeWords(String text) {
            text = text.toLowerCase();
            String[] t = text.split(" ");
            Arrays.sort(t, new Comparator<String>() {
                public int compare(String a , String b){
                    return a.length() - b.length();
                }
            });
            StringBuilder sb = new StringBuilder();
            for(int i = 0; i < t.length; i ++ ){
                sb.append(t[i]);
                // sb.append(" ");
                if(i != t.length - 1){
                    sb.append(" ");
                }
            }
            char[] ans = sb.toString().toCharArray();
            ans[0] = (char)('A' + (int)( ans[0] - 'a' ) );
            return String.valueOf(ans);
        }
    }
    ```





