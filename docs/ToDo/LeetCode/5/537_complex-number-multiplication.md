2022.4.08 Leetcode 日常刷题

---

#### [537. 复数乘法](https://leetcode-cn.com/problems/complex-number-multiplication/)



【难度】：Medium

复数 可以用字符串表示，遵循 "实部+虚部i" 的形式，并满足下述条件：

实部 是一个整数，取值范围是 [-100, 100]
虚部 也是一个整数，取值范围是 [-100, 100]
i2 == -1
给你两个字符串表示的复数 num1 和 num2 ，请你遵循复数表示形式，返回表示它们乘积的字符串。

```输入：num1 = "1+-1i", num2 = "1+-1i"
输出："0+-2i"
解释：(1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i ，你需要将它转换为 0+-2i 的形式。 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/complex-number-multiplication
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```



- 只需要注意细节和第一个字符是负号的情况



```Java
class Solution {
    public String complexNumberMultiply(String num1, String num2) {
        int[] b = getRealNum(num2);
        int[] a = getRealNum(num1);
        int front = a[0] * b[0] - a[1] * b[1];
        int end = a[1] * b[0] + a[0] * b[1];
        StringBuilder sb = new StringBuilder();
        sb.append(front);
        sb.append("+");
        sb.append(end);
        sb.append("i");
        return sb.toString();
    }

    public int[] getRealNum(String str){
        StringBuilder sb = new StringBuilder();
        StringBuilder sb2 = new StringBuilder();
        int[] ans = new int[2];
        char[] a = str.toCharArray();
        int idx = 0;
        if(a[0] == '-'){
            idx = 1;
            sb.append("-");
            while(idx < str.length() && a[idx]!='+' && a[idx] != '-'){
                sb.append(a[idx]);
                idx ++ ;
            }
        }
        else{
            while(idx < str.length() && a[idx]!='+' && a[idx] != '-'){
                sb.append(a[idx]);
                idx ++ ;
            }

        }
        
        ans[0] = Integer.valueOf(sb.toString());
        char flag = a[idx];
        idx ++ ;
        while(idx < str.length() - 1 ){
            sb2.append(a[idx]);
            idx ++ ;
        }
        ans[1] = Integer.valueOf(sb2.toString());
        if(flag == '-'){
            ans[1] = -1 * ans[1];
        }
        return ans;
    }
}
```