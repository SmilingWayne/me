# 1365_中文题目

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