# 1014_最佳观光组合

<!-- 所有文件名必须是该题目的英文名 -->

!!! note
    <!-- 这里记载考察的数据结构、算法等 -->
    动态规划

- 🔑🔑 难度：<span style = "color:gold; font-weight:bold">Medium</span>
<!-- <span style = "color:gold; font-weight:bold">Medium</span> 中等 -->
<!-- <span style = "color:crisma; font-weight:bold">High</span> 困难 -->
<!-- <span style = "color:Green; font-weight:bold">Easy</span> 简单 -->

<!-- 题目简介 -->
给你一个正整数数组 values，其中 values[i] 表示第 i 个观光景点的评分，并且两个景点 i 和 j 之间的 距离 为 j - i。

一对景点（i < j）组成的观光组合的得分为 values[i] + values[j] + i - j ，也就是景点的评分之和 减去 它们两者之间的距离。

返回一对观光景点能取得的最高分。


------

> 输入：values = [8,1,5,2,6]
> 
> 输出：11
> 
> 解释：i = 0, j = 2, values[i] + values[j] + i - j = 8 + 5 + 0 - 2 = 11


-------------

=== "Java"

    ```java
    class Solution1 {
        public int maxScoreSightseeingPair(int[] A) {
            int length = A.length;
            if(A.length <=0 ){
                return 0;
            }
            int curMax = A[0];
            int max = 0;
            int index = max;
            for(int i = 0 ; i < A.length; i ++ ){
                index--;
                curMax = index + A[i];
                if(curMax > max){
                    max = curMax;
                }
                if(index < A[i]){
                    index = A[i];
                }
            }
            return max;
        }
    }
    // Greedy Method: 

    class Solution2 {
        public int maxScoreSightseeingPair(int[] A) {
            int record = A[0];
            int max = Integer.MIN_VALUE;
            for(int i = 1 ; i < A.length ; i ++ ){
                max = Math.max(A[i] - i + record, max);
                record = Math.max(A[i] + i, record );

            }
            return max;
        }
    }


    ```