# 43_字符串相乘

<!-- 所有文件名必须是该题目的英文名 -->

!!! note
    <!-- 这里记载考察的数据结构、算法等 -->
    哈希表 | 动态规划

- 🔑🔑 难度： <span style = "color:Green; font-weight:bold">Easy</span> 简单
<!-- <span style = "color:gold; font-weight:bold">Medium</span> 中等 -->
<!-- <span style = "color:crisma; font-weight:bold">High</span> 困难 -->
<!-- <span style = "color:Green; font-weight:bold">Easy</span> 简单 -->

<!-- 题目简介 -->
> 给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。注意：不能使用任何内置的 BigInteger 库或直接将输入转换为整数。

------

> 解析

-------------

=== "这里写编程语言"

    ```java
    class Solution {
        public String multiply(String num1, String num2) {
            if(num1.equals("0") || num2.equals("0")){
                return "0";
            }
            if(num2.length() > num1.length()){
                String temp = num2;
                num2 = num1;
                num1 = temp;
            }
            int[] total = new int[num1.length() + num2.length()];
            int length1 = num1.length();
            int length2 = num2.length();
            for(int i = length1 -1; i >=0 ; i -- ){
                int x = num1.charAt(i) - '0';
                for(int j = length2 - 1; j >=0; j -- ){
                    int y = num2.charAt(j) - '0';
                    total[i + j + 1] += x * y;
                }
            }
            for(int i = length1 + length2 - 1; i > 0; i--){
                total[i - 1] += total[i]/10;
                total[i] = total[i]%10;
            }
            int startPoint = 0;
            for(int i = 0 ; i < length1 + length2 -1; i ++ ){
                if(total[i]!=0){
                    startPoint = i;
                    break;
                }
                if(i == length1 + length2 -2){
                    return total[length1 + length2 -1] + "";
                }
            }
            String ans = "";
            for(int i = startPoint; i < length1 + length2; i ++ ){
                ans = ans + total[i] + "";
            }
            return ans;

            
        }
    }

    ```