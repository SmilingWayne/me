<h2>2022.3.26 Leetcode 复习

#### [415. 字符串相加](https://leetcode-cn.com/problems/add-strings/)

🔑🔑 考点：字符串 ｜ 大数比较

🚴‍♀️🚴‍♀️ 难度： <span style = "color:gold; font-weight:bold">Medium</span>

🔗🔗 链接：https://leetcode-cn.com/problems/add-strings/

📖📖 题目：

给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和并同样以字符串形式返回。

你不能使用任何內建的用于处理大整数的库（比如 BigInteger）， 也不能直接将输入的字符串转换为整数形式。

💻💻 测试用例：

```
输入：num1 = "11", num2 = "123"
输出："134"
```

💡💡思路：

- 主要是学到如何灵活地实现String/ Integer的相互转化：a - '0' 和StringBuilder (Java)



👩🏻‍💻🧑🏻‍💻 代码：

```Java
// Leetcode 415
class Solution {
    public String addStrings(String num1, String num2) {
        int target = 0;
        int length1 = num1.length();
        int length2 = num2.length();
        int added = 0;
        StringBuilder sb = new StringBuilder();
        while(length1 > 0 || length2 > 0 || added > 0){
            if(length1 > 0){
                added += (num1.charAt(length1 - 1) - '0');
                length1 -- ;
            }
            if(length2 > 0){
                added += (num2.charAt(length2 - 1) - '0');
                length2 -- ;
            }
            sb.append(added % 10);
            added = added / 10;
        }
        return sb.reverse().toString();

    }
}


```















给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和并同样以字符串形式返回。

你不能使用任何內建的用于处理大整数的库（比如 BigInteger）， 也不能直接将输入的字符串转换为整数形式。

```
输入：num1 = "11", num2 = "123"
输出："134"
```

- 主要是记一下这里严格具体的语法

```Java

class Solution {
    public String addStrings(String num1, String num2) {
        int target = 0;
        int length1 = num1.length();
        int length2 = num2.length();
        int added = 0;
        StringBuilder sb = new StringBuilder();
        while(length1 > 0 || length2 > 0 || added > 0){
            if(length1 > 0){
                added += (num1.charAt(length1 - 1) - '0');
                length1 -- ;
            }
            if(length2 > 0){
                added += (num2.charAt(length2 - 1) - '0');
                length2 -- ;
            }
            sb.append(added % 10);
            added = added / 10;
        }
        return sb.reverse().toString();

    }
}

```

