#### [1461. 检查一个字符串是否包含所有长度为 K 的二进制子串](https://leetcode-cn.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/)

🔑🔑 考点：集合 ｜ 逆向思维

🚴‍♀️🚴‍♀️ 难度： <span style = "color:gold; font-weight:bold">Medium</span>

🔗🔗 链接：https://leetcode-cn.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/

📖📖 题目：

给你一个二进制字符串 `s` 和一个整数 `k` 。如果所有长度为 `k` 的二进制字符串都是 `s` 的子串，请返回 `true` ，否则请返回 `false` 。

💻💻 测试用例：

```
输入：s = "00110110", k = 2
输出：true
解释：长度为 2 的二进制串包括 "00"，"01"，"10" 和 "11"。它们分别是 s 中下标为 0，1，3，2 开始的长度为 2 的子串。
```

💡💡思路：

- 原理：长度k的二进制串一定是2^k个
- 可以根据字符串本身进行遍历寻找（反过来想）
- HashSet执行去重，看看整个字符串有多少个不同的k长度的子串

👩🏻‍💻🧑🏻‍💻 代码：

```Java
class Solution {
    public boolean hasAllCodes(String s, int k) {
        Set<String> set = new HashSet<>();
        int start = 0, end = k;
        int len = s.length();
        while(end <= len){
            set.add(s.substring( start, end));
            end ++ ;
            start ++ ;
        }
        if(set.size() != Math.pow(2,k)){
            return false;
        }
        return true;
    }
}
```



