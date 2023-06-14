#### [1750. 删除字符串两端相同字符后的最短长度](https://leetcode-cn.com/problems/minimum-length-of-string-after-deleting-similar-ends/)

🔑🔑 考点：字符串 | 数组

🚴‍♀️🚴‍♀️ 难度： <span style = "color:gold; font-weight:bold">Medium</span>

🔗🔗 链接：https://leetcode-cn.com/problems/minimum-length-of-string-after-deleting-similar-ends/

📖📖 题目：

给你一个只包含字符 'a'，'b' 和 'c' 的字符串 s ，你可以执行下面这个操作（5 个步骤）任意次：

选择字符串 s 一个 非空 的前缀，这个前缀的所有字符都相同。
选择字符串 s 一个 非空 的后缀，这个后缀的所有字符都相同。
前缀和后缀在字符串中任意位置都不能有交集。
前缀和后缀包含的所有字符都要相同。
同时删除前缀和后缀。
请你返回对字符串 s 执行上面操作任意次以后（可能 0 次），能得到的 最短长度。

💻💻 测试用例：

```
输入：s = "cabaabac"
输出：0
```

💡💡思路：

- 双端逼近，贪心地删除，直到无法删除为止

👩🏻‍💻🧑🏻‍💻 代码：

```Java
class Solution {
    public int minimumLength(String s) {
        int len = s.length();
        int start = 0;
        int end = s.length() - 1;
        while(start < end){
            if(s.charAt(end) != s.charAt(start)){
                break;
            }
            while(start < end && s.charAt(start) == s.charAt(start + 1)){
                start ++ ;
                if(start == end){
                    return 0;
                }
            }
            while(end > start && s.charAt(end) == s.charAt(end - 1)){
                end -- ;
                if(start == end){
                    return 0;
                }
                
            }
            start ++ ;
            end -- ;
        }
        
        return end - start + 1;
    }
}
```





