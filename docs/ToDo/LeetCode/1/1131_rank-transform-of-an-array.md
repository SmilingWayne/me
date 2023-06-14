# 1131_中文题目

<!-- 所有文件名必须是该题目的英文名 -->

!!! note
    <!-- 这里记载考察的数据结构、算法等 -->
    ?

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
        public static int[] arrayRankTransform(int[] arr) {
            int[] helper = new int[arr.length];
            helper = arr.clone();
            Arrays.sort(helper);
            int index = 1;
            Map <Integer, Integer> map = new HashMap<>();
            for(int i = 0; i<helper.length;i++){
                if(i>0&&helper[i]!=helper[i-1]){
                    map.put(helper[i],index);
                    index++;   
                }
                if(i == 0){
                    map.put(helper[i],index);
                    index++;
                }
            }
            for(int i = 0; i < arr.length; i ++){
                arr[i] = map.get(arr[i]);
            }
            return arr; 
        }
    }

    ```