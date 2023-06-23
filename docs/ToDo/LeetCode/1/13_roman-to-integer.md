# 13_罗马数字转整数

<!-- 所有文件名必须是该题目的英文名 -->

!!! note
    <!-- 这里记载考察的数据结构、算法等 -->
    模拟

- 🔑🔑 难度：<span style = "color:Green; font-weight:bold">Easy</span>
<!-- <span style = "color:gold; font-weight:bold">Medium</span> 中等 -->
<!-- <span style = "color:crisma; font-weight:bold">High</span> 困难 -->
<!-- <span style = "color:Green; font-weight:bold">Easy</span> 简单 -->

<!-- 题目简介 -->

> 例如， 罗马数字 2 写做 II ，即为两个并列的 1 。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。
> 
> 通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：
> 
> I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。 
> 
> X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。  
> 
> C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。 
> 
> 给定一个罗马数字，将其转换成整数。


```
输入: s = "MCMXCIV"
输出: 1994
解释: M = 1000, CM = 900, XC = 90, IV = 4.
```

------

> 解析

-------------

=== "Python"

    ```Python
    class Solution:
        def romanToInt(self, s: str) -> int:
            dic = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
            a = 0
            if len(s) == 1:
                return dic[s]
            a += dic[s[0]]
            for i in range(1,len(s)):
                if dic[s[i]] > dic[s[i-1]]:
                    a = a - dic[s[i-1]] * 2 + dic[s[i]]
                else:
                    a += dic[s[i]]
            return a


    
    ```

=== "Java"

    ```java
    class Solution {
        public int romanToInt(String s) {
            int sum = 0;
            HashMap<Character, Integer> map = new HashMap<>();
            map.put('I', 1);
            map.put('V', 5);
            map.put('X', 10);
            map.put('L', 50);
            map.put('C', 100);
            map.put('D', 500);
            map.put('M', 1000);
            for(int i = 0; i < s.length(); i ++ ){
                int value = map.get(s.charAt(i));
                if(i < s.length() - 1 && value < map.get(s.charAt(i + 1))){
                    sum = sum - value;
                }
                else{
                    sum = sum + value;
                }
            }
            return sum;

        }
    }
    ```
    
    ```