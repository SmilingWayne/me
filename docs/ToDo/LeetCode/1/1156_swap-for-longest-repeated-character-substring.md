# 1156_单字符重复子串的最大长度

!!! note
    <!-- 这里记载考察的数据结构、算法等 -->
    字符串

- 🔑🔑 难度： <span style = "color:gold; font-weight:bold">Medium</span> 




> 如果字符串中的所有字符都相同，那么这个字符串是单字符重复的字符串。
> 
> 给你一个字符串 text，你只能交换其中两个字符一次或者什么都不做，然后得到一些单字符重复的子串。返回其中最长的子串的长度。



```
输入：text = "aaabaaa"
输出：6
```


??? note
    
    一个小小的动态规划
    
    由于仅仅删除一个节点，所以最大的情况是可以预测到的
    
    “aaaa b aaaa”这种情况，需要再进行一次后向搜索


=== "Java"

    ```Java
    class Solution {
        public int maxRepOpt1(String text) {
            int max = 1;
            int idx = 0;
            Map<Character, Integer> map = new HashMap<>();
            for(int i = 0; i < text.length();i ++ ){
                map.put(text.charAt(i), map.getOrDefault(text.charAt(i), 0) + 1);
            }
            while(idx < text.length()){
                int cur_len = count_full(text, idx);
                if(idx + cur_len + 1 < text.length() && text.charAt(idx + cur_len + 1) == text.charAt(idx)){
                    if(map.get(text.charAt(idx)) > (cur_len +
                    count_full(text, idx + cur_len + 1))){
                        max = Math.max(cur_len + count_full(text, idx + cur_len + 1) + 1, max);
                    }
                    else{
                        max = Math.max(cur_len + count_full(text, idx + cur_len + 1), max);
                    }
                }
                else if(idx + cur_len + 1 < text.length() && text.charAt(idx + cur_len + 1) != text.charAt(idx)){
                    if(map.get(text.charAt(idx)) > (cur_len)){
                        max = Math.max(cur_len + 1, max);
                    }
                }
                else {
                    if(map.get(text.charAt(idx)) > cur_len ){
                        max = Math.max(max, cur_len + 1);
                    }
                    else{
                        max = Math.max(cur_len , max);
                    }
                }
                max = Math.max(cur_len, max);
                idx += cur_len;
            }
            return max;

        }

        public int count_full(String a ,int idx){
            int cnt = 1;
            while(idx + 1 < a.length()  && a.charAt(idx) == a.charAt(idx + 1)){
                idx ++ ;
                cnt += 1;
            }
            return cnt;
        }
    }
    ```
