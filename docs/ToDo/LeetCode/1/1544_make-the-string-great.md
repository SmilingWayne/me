# 1544_整理字符串

<!-- 所有文件名必须是该题目的英文名 -->

!!! note
    <!-- 这里记载考察的数据结构、算法等 -->
    哈希表 | 动态规划

- 🔑🔑 难度：<span style = "color:Green; font-weight:bold">Easy</span>
<!-- <span style = "color:gold; font-weight:bold">Medium</span> 中等 -->
<!-- <span style = "color:crisma; font-weight:bold">High</span> 困难 -->
<!-- <span style = "color:Green; font-weight:bold">Easy</span> 简单 -->

<!-- 题目简介 -->

> 给你一个由大小写英文字母组成的字符串 s 。
> 
> 一个整理好的字符串中，两个相邻字符 s[i] 和 s[i+1]，其中 0<= i <= s.length-2 ，要满足如下条件:
> 
> 若 s[i] 是小写字符，则 s[i+1] 不可以是相同的大写字符。
> 若 s[i] 是大写字符，则 s[i+1] 不可以是相同的小写字符。
> 请你将字符串整理好，每次你都可以从字符串中选出满足上述条件的 两个相邻 字符并删除，直到字符串整理好为止。
> 
> 请返回整理好的 字符串 。题目保证在给出的约束条件下，测试样例对应的答案是唯一的。
> 
> 注意：空字符串也属于整理好的字符串，尽管其中没有任何字符。

 
```
输入：s = "abBAcC"
输出：""
解释：存在多种不同情况，但所有的情况都会导致相同的结果。例如：
"abBAcC" --> "aAcC" --> "cC" --> ""
"abBAcC" --> "abBA" --> "aA" --> ""

```

------

> 解析

-------------

=== "Java"

    ```java
    class Solution {
        public String makeGood(String s) {
            StringBuffer ret = new StringBuffer();
            int retIndex = -1;
            int length = s.length();
            for(int i = 0 ; i < length; i ++ ){
                char helper = s.charAt(i);
                if(ret.length() > 0 &&Math.abs(ret.charAt(retIndex) - helper)==32){
                    ret.deleteCharAt(retIndex);
                    retIndex--;
                }
                else{
                    ret.append(helper);
                    retIndex++;
                }
            }
            return ret.toString();
        }
    }

    ```