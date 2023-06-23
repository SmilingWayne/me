# 1_两数之和

<!-- 所有文件名必须是该题目的英文名 -->

!!! note
    <!-- 这里记载考察的数据结构、算法等 -->
    

- 🔑🔑 难度：<span style = "color:gold; font-weight:bold">Medium</span>
<!-- <span style = "color:gold; font-weight:bold">Medium</span> 中等 -->
<!-- <span style = "color:crisma; font-weight:bold">High</span> 困难 -->
<!-- <span style = "color:Green; font-weight:bold">Easy</span> 简单 -->

<!-- 题目简介 -->
> Write Here 

------

??? note
    ?

-------------

=== "Java"

    ```java
    class Solution {
        public int[] twoSum(int[] nums, int target) {
            
            Map <Integer,Integer> map = new HashMap<>();
            for(int i = 0; i < nums.length; i ++){
                if(map.containsKey(target - nums[i])){
                    return new int[]{map.get(target-nums[i]),i};
                }
                map.put(nums[i],i);
            }
            return new int[0];


        }
    }


    ```