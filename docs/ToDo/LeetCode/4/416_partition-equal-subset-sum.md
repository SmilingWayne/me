# 416_分割等和子集

<!-- 所有文件名必须是该题目的英文名 -->

!!! note
    <!-- 这里记载考察的数据结构、算法等 -->
    动态规划

- 🔑🔑 难度：<span style = "color:gold; font-weight:bold">Medium</span>
<!-- <span style = "color:gold; font-weight:bold">Medium</span> 中等 -->
<!-- <span style = "color:crisma; font-weight:bold">High</span> 困难 -->
<!-- <span style = "color:Green; font-weight:bold">Easy</span> 简单 -->

<!-- 题目简介 -->
给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

> 输入：nums = [1,5,11,5]
> 
> 输出：true
> 
> 解释：数组可以分割成 [1, 5, 5] 和 [11] 。

------

> 解析

-------------

=== "Java"

    ```java
    class Solution {
        public boolean canPartition(int[] nums) {
            int n = nums.length;
            if (n < 2) {
                return false;
            }
            int sum = 0, maxNum = 0;
            for (int num : nums) {
                sum += num;
                maxNum = Math.max(maxNum, num);
            }
            if (sum % 2 != 0) {
                return false;
            }
            int target = sum / 2;
            if (maxNum > target) {
                return false;
            }
            boolean[][] dp = new boolean[n][target + 1];
            for (int i = 0; i < n; i++) {
                dp[i][0] = true;
            }
            dp[0][nums[0]] = true;   //这里这样赋值，原因很简单：当i = 0的时候，如果要找nums[0]的数字，只需要拿他自己就行了
            for (int i = 1; i < n; i++) {
                int num = nums[i];
                for (int j = 1; j <= target; j++) {
                    if (j >= num) {
                        dp[i][j] = dp[i - 1][j] || dp[i - 1][j - num];
                    } else {
                        dp[i][j] = dp[i - 1][j];
                    }
                }
            }
            return dp[n - 1][target];
        }
    }


    ```