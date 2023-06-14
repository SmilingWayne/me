# 3_?

<!-- 所有文件名必须是该题目的英文名 -->

!!! note
    <!-- 这里记载考察的数据结构、算法等 -->
    哈希表 | 动态规划

- 🔑🔑 难度：
<!-- <span style = "color:gold; font-weight:bold">Medium</span> 中等 -->
<!-- <span style = "color:crisma; font-weight:bold">High</span> 困难 -->
<!-- <span style = "color:Green; font-weight:bold">Easy</span> 简单 -->

<!-- 题目简介 -->
> Write Here 

------

> 解析

-------------

=== "Java"

    ```java
    class Solution {
        public int lengthOfLongestSubstring(String s) {
            int n = s.length();
            if(n == 0)
                return 0;
            if(n == 1)
                return 1;
            Map<Character,Integer> map = new HashMap<>();
            int res = 0;
            int rk = -1;
            char[] helper = s.toCharArray();
            for(int i = 0; i < n ; i++){
                if(i!= 0){
                    map.remove(helper[i-1]);

                }
                while( rk + 1 < n && !map.containsKey(helper[rk+1])){
                    map.put(helper[rk+1],rk+1);
                    rk ++;
                }
                res = Math.max(res, rk + 1 - i);
            }
            return res;
        }
    }

    ```