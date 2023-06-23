# 1365_有多少小于当前数字的数字

<!-- 所有文件名必须是该题目的英文名 -->

!!! note
    <!-- 这里记载考察的数据结构、算法等 -->
    哈希表 | 动态规划

- 🔑🔑 难度：<span style = "color:Green; font-weight:bold">Easy</span>
<!-- <span style = "color:gold; font-weight:bold">Medium</span> 中等 -->
<!-- <span style = "color:crisma; font-weight:bold">High</span> 困难 -->
<!-- <span style = "color:Green; font-weight:bold">Easy</span> 简单 -->

<!-- 题目简介 -->
> 给你一个数组 nums，对于其中每个元素 nums[i]，请你统计数组中比它小的所有数字的数目。
> 
> 换而言之，对于每个 nums[i] 你必须计算出有效的 j 的数量，其中 j 满足 j != i 且 nums[j] < nums[i] 。
> 
> 以数组形式返回答案。


```
输入：nums = [8,1,2,2,3]
输出：[4,0,1,1,3]
解释： 
对于 nums[0]=8 存在四个比它小的数字：（1，2，2 和 3）。 
对于 nums[1]=1 不存在比它小的数字。
对于 nums[2]=2 存在一个比它小的数字：（1）。 
对于 nums[3]=2 存在一个比它小的数字：（1）。 
对于 nums[4]=3 存在三个比它小的数字：（1，2 和 2）。
```
------

> 解析

-------------

=== "Java"

    ```java
    class Solution {
        public int[] smallerNumbersThanCurrent(int[] nums) {
            int[] res = new int[nums.length];
            int[] record = nums.clone();
            Map <Integer, Integer> map = new HashMap<>();
            Arrays.sort(record);
            int flag = 0;
            for(int i = 0; i < nums.length; i ++){
                if(i == 0){
                    map.put(record[i],flag);
                    flag++;
                }
                else if(!map.containsKey(record[i])){
                    map.put(record[i],flag);
                    flag++;
                }
                else{
                    flag++;
                }
                
            }
            for(int i = 0; i < nums.length; i++){
                res[i] = map.get(nums[i]);
            }
            return res;
        }
    }

    ```