# 1248_统计“优美子数组”

<!-- 所有文件名必须是该题目的英文名 -->

!!! note
    <!-- 这里记载考察的数据结构、算法等 -->
    双指针

- 🔑🔑 难度：<span style = "color:gold; font-weight:bold">Medium</span>
<!-- <span style = "color:gold; font-weight:bold">Medium</span> 中等 -->
<!-- <span style = "color:crisma; font-weight:bold">High</span> 困难 -->
<!-- <span style = "color:Green; font-weight:bold">Easy</span> 简单 -->

<!-- 题目简介 -->
> 给你一个整数数组 nums 和一个整数 k。如果某个连续子数组中恰好有 k 个奇数数字，我们就认为这个子数组是「优美子数组」。
> 
> 请返回这个数组中 「优美子数组」 的数目。



```
输入：nums = [1,1,2,1,1], k = 3
输出：2
解释：包含 3 个奇数的子数组是 [1,1,2,1] 和 [1,2,1,1] 。
```


------

??? note 
    
-------------

=== "Java"

    ```java

    class Solution {
        public int numberOfSubarrays(int[] nums, int k) {
            int len = nums.length;
            int res = 0;
            int oddcount = 0;
            int[] arr = new int[len+2];
            for(int i = 0 ; i < len; i++){
                if((nums[i]&1)==1){
                    arr[++oddcount] = i;
                }
            }
            arr[0] = -1;
            arr[oddcount+1] = len;
            for(int i = 1; i + k < oddcount+2; i++){
                res += (arr[i] - arr[i - 1])*(arr[i + k ]- arr[i+k-1]);
            }
            return res;
        }
    }
    ```