# 1170_比较字符串最小字母出现频次

!!! note
    <!-- 这里记载考察的数据结构、算法等 -->
    字符串 | 字典序 ｜ 前缀和

- 🔑🔑 难度：<span style = "color:gold; font-weight:bold">Medium</span>


> 定义一个函数 f(s)，统计 s  中（按字典序比较）最小字母的出现频次 ，其中 s 是一个非空字符串。
> 
> 例如，若 s = "dcce"，那么 f(s) = 2，因为字典序最小字母是 "c"，它出现了 2 次。
> 
> 现在，给你两个字符串数组待查表 queries 和词汇表 words 。对于每次查询 queries[i] ，需统计 words 中满足 f(queries[i]) < f(W) 的 词的数目 ，W 表示词汇表 words 中的每个词。
> 
> 请你返回一个整数数组 answer 作为答案，其中每个 answer[i] 是第 i 次查询的结果。
> 
> 1 <= queries.length <= 2000
> 
> 1 <= words.length <= 2000
> 
> 1 <= queries[i].length, words[i].length <= 10
> 



```
输入：queries = ["cbd"], words = ["zaaaz"]
输出：[1]
解释：查询 f("cbd") = 1，而 f("zaaaz") = 3 所以 f("cbd") < f("zaaaz")。
```


??? note
    
    方法1： 哈希表。对于words中每个词进行f操作，都保存到一个HashMap（key：下标，value：f值）中，对Query进行遍历，看有哪些words是符合条件的
    
    方法2: 打表。题目中单词长度是有限的（最长为10）。所以意味着f值是最大为10。我们对于每个query元素的f值，只需要找到“words里有多少元素的f值比它还要大”，然后当作结果就可以了。类似于一个打表的过程。


=== "Java"

    ```Java
    class Solution {
    // 优化前：只能O(MN)的复杂度
        public int f(String a){
            if(a.length() == 0){
                return 0;
            }
            int[] dict = new int[26];
            Arrays.fill(dict, 0);
            for(int i = 0; i < a.length(); i ++ ){
                dict[a.charAt(i) - 'a'] ++ ;
            }
            for(int i = 0; i < 26; i ++ ){
                if(dict[i] != 0){
                    return dict[i];
                }
            }
            return 0;
        }
        public int[] numSmallerByFrequency(String[] queries, String[] words) {
            Map<Integer, Integer> map = new HashMap<>();
            for(int i = 0; i < words.length; i ++ ){
                map.put(i, f(words[i]));
            }
            int[] ans = new int[queries.length];
            Arrays.fill(ans, 0);
            for(int i = 0; i < queries.length; i ++ ){
                int curTime = f(queries[i]);
                for(int j = 0; j < words.length; j ++ ){
                    if(map.get(j) > curTime){
                        ans[i] ++ ;
                    }
                }
            }
            return ans;
        }
    }
    ```


    ```Java
    // 优化后：
    class Solution {
        public int f(String a){
            if(a.length() == 0)
                return 0;
            int[] dict = new int[26];
            Arrays.fill(dict, 0);
            for(int i = 0; i < a.length(); i ++ ){
                dict[a.charAt(i) - 'a'] ++ ;
            }
            for(int i = 0; i < 26; i ++ ){
                if(dict[i] != 0)
                    return dict[i];
            }
            return 0;
        }
        public int[] numSmallerByFrequency(String[] queries, String[] words) {
            int[] words_count = new int[12];
            Arrays.fill(words_count, 0);
            int[] ans = new int[queries.length];
            Arrays.fill(ans, 0);
            for(int i = 0; i < words.length; i ++ ){
                String word = words[i];
                words_count[f(word)] ++ ; 
            }
            for(int i = 0; i < 11; i ++ ){
                for(int j = i + 1; j < 12; j ++ )
                    words_count[i] += words_count[j];
            }
            for(int i = 0; i < queries.length; i ++ ){
                ans[i] = words_count[f(queries[i]) + 1];
            }
            return ans;
        }
    }
    ```


