# 860_中文题目

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
        public boolean lemonadeChange(int[] bills) {
            int i=bills.length;
            int count5=0,count10=0;
            if(bills[0]>5){
                    return false;
            }
            for(int a = 0; a < i;a++){
                if(bills[a]==5){
                    count5++;
                }
                else if(bills[a] == 10){
                    count10++;
                    count5--;
                }
                else if(bills[a]==20){
                    if(count10>=1){
                        count10--;
                        count5--;
                    }
                    else{
                        count5-=3;
                    }
                }
                if(count5<0||count10<0){
                    return false;
                }
            }
            return true;
        }
    }

    ```