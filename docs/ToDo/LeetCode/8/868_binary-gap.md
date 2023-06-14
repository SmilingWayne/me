#### [868. 二进制间距](https://leetcode-cn.com/problems/binary-gap/)

🔑🔑 考点：字符串 | 位运算

🚴‍♀️🚴‍♀️ 难度： <span style = "color:darkgreen; font-weight:bold">Easy</span>

🔗🔗 链接：https://leetcode-cn.com/problems/binary-gap/

📖📖 题目：

给定一个正整数 n，找到并返回 n 的二进制表示中两个 相邻 1 之间的 最长距离 。如果不存在两个相邻的 1，返回 0 。

如果只有 0 将两个 1 分隔开（可能不存在 0 ），则认为这两个 1 彼此 相邻 。两个 1 之间的距离是它们的二进制表示中位置的绝对差。例如，"1001" 中的两个 1 的距离为 3 。

💻💻 测试用例：

```
输入：n = 22
输出：2
输入：n = 8
输出：0
```

💡💡思路：

- 只要生成这个数字的二进制，然后设置一个idx记载第一个1和后续的出现的1，然后比较之间的长度即可

👩🏻‍💻🧑🏻‍💻 代码：

```Java
class Solution {
    public int binaryGap(int n) {
        StringBuilder sb = new StringBuilder();
        while(n > 0){
            sb.append((char)( n % 2 + '0') );
            n /= 2;
        }
        int pre = -1;
        int ans = 0;
        String t = sb.toString();
        for(int i = 0; i < t.length(); i ++ ){
            if(t.charAt(i) == '1'){
                if(pre != -1)
                    ans = Math.max(i - pre, ans);
                pre = i;
            }
            
        }
        return ans;

    }
}
```






