#### [2182. 构造限制重复的字符串](https://leetcode-cn.com/problems/construct-string-with-repeat-limit/)

🔑🔑 考点：贪心 | 字符串

🚴‍♀️🚴‍♀️ 难度： <span style = "color:gold; font-weight:bold">Medium</span>

🔗🔗 链接：https://leetcode-cn.com/problems/construct-string-with-repeat-limit/

📖📖 题目：

给你一个字符串 s 和一个整数 repeatLimit ，用 s 中的字符构造一个新字符串 repeatLimitedString ，使任何字母 连续 出现的次数都不超过 repeatLimit 次。你不必使用 s 中的全部字符。

返回 字典序最大的 repeatLimitedString 。

如果在字符串 a 和 b 不同的第一个位置，字符串 a 中的字母在字母表中出现时间比字符串 b 对应的字母晚，则认为字符串 a 比字符串 b 字典序更大 。如果字符串中前 min(a.length, b.length) 个字符都相同，那么较长的字符串字典序更大。

💻💻 测试用例：

```
输入：s = "cczazcc", repeatLimit = 3
输出："zzcccac"
输入：s = "aababab", repeatLimit = 2
输出："bbabaa"
```

💡💡思路：

-  数组记录字母出现次数，总是优先选取字典序最大的，如果超过limit向前面借一个字符，如果出现次数不超过限制就直接加到答案里，如果没有可选的了就终止。

👩🏻‍💻🧑🏻‍💻 代码：

```Java
class Solution {
    public String repeatLimitedString(String s, int repeatLimit) {
        int[] maps = new int[26];
        for(char a:s.toCharArray()){
            maps[a - 'a'] ++ ;
        }
        StringBuilder sb = new StringBuilder();
        for(int i = 25; i >=0 ; i -- ){
            while(maps[i] > 0){
                int times = Math.min(repeatLimit, maps[i]);
                maps[i] -= times;
                while(times > 0){
                    sb.append((char)('a' + i));
                    times -- ;
                }
                if(maps[i] == 0){
                    break;
                }
                int idx = i - 1;
                while(idx >= 0 && maps[idx] == 0){
                    idx -- ;
                }
                if(idx < 0){
                    return sb.toString();
                }
                maps[idx] -- ;
                sb.append((char)('a' + idx));
            }
        }
        return sb.toString();
    }
}
```









