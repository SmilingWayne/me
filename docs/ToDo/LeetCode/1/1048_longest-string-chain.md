# 1048_最长字符串链

<!-- 所有文件名必须是该题目的英文名 -->

!!! note
    <!-- 这里记载考察的数据结构、算法等 -->
    ?


- 🔑🔑 难度：<span style = "color:gold; font-weight:bold">Medium</span>


> 给出一个单词数组 words ，其中每个单词都由小写英文字母组成。
> 
> 如果我们可以 不改变其他字符的顺序 ，在 wordA 的任何地方添加 恰好一个 字母使其变成 wordB ，那么我们认为 wordA 是 wordB 的 前身 。
> 
> 例如，"abc" 是 "abac" 的 前身 ，而 "cba" 不是 "bcad" 的 前身
> 词链是单词 [word_1, word_2, ..., word_k] 组成的序列，k >= 1，其中 word1 是 word2 的前身，word2 是 word3 的前身，依此类推。一个单词通常是 k == 1 的 单词链 。
> 
> 从给定单词列表 words 中选择单词组成词链，返回 词链的 最长可能长度 。


```
输入：words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
输出：5
解释：所有的单词都可以放入单词链 ["xb", "xbc", "cxbc", "pcxbc", "pcxbcf"].
```

-----


??? note
    待补充


=== "Java"

    ```Java
    // 代码待补
    class Solution {
        public int longestStrChain(String[] words) {
            Arrays.sort(words, new Comparator<String>(){
                public int compare(String a, String b){
                    return  a.length() -b.length()  ;
                }
            });
            // for(String a:words){
            //     System.out.println(a);
            // }
            int[] dp = new int[words.length];
            Arrays.fill(dp, 1);
            for(int i = 1; i < words.length; i ++ ){
                for(int j = i - 1; j >= 0; j -- ){
                    if(words[j].length() + 1 < words[i].length()){
                        break;
                    }
                    if(words[j].length() == words[i].length()){
                        continue;
                    }
                    if(isValid(words[j], words[i])){
                        dp[i] = Math.max(dp[i], dp[j] + 1);
                    }
                }
            }
            int t = 1;
            for(int i = 0; i < dp.length; i ++ ){
                t = Math.max(t, dp[i]);
            }
            return t;


        }

        public boolean isValid(String a,String b){
            int m = a.length();
            int n = b.length();
            int tmp = 0;
            // System.out.println(a);
            // System.out.println(b);
            
            for(int i = 0; i < n; i ++ ){
                if(tmp < a.length () && a.charAt(tmp) == b.charAt(i)){
                    tmp ++ ;
                }
            }
            return tmp == m;
        }
    }
    ```



