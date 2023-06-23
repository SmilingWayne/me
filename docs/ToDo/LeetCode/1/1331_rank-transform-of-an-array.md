# 1331_数组序号转换

<!-- 所有文件名必须是该题目的英文名 -->

!!! note
    <!-- 这里记载考察的数据结构、算法等 -->
    ?

- 🔑🔑 难度：<span style = "color:gold; font-weight:bold">Medium</span>
<!-- <span style = "color:gold; font-weight:bold">Medium</span> 中等 -->
<!-- <span style = "color:crisma; font-weight:bold">High</span> 困难 -->
<!-- <span style = "color:Green; font-weight:bold">Easy</span> 简单 -->

<!-- 题目简介 -->
> 给你一个整数数组 arr ，请你将数组中的每个元素替换为它们排序后的序号。
> 
> 序号代表了一个元素有多大。序号编号的规则如下：
> 
> 序号从 1 开始编号。
> 
> 一个元素越大，那么序号越大。如果两个元素相等，那么它们的序号相同。每个数字的序号都应该尽可能地小。

```
输入：arr = [40,10,20,30]
输出：[4,1,2,3]
解释：40 是最大的元素。 10 是最小的元素。 20 是第二小的数字。 30 是第三小的数字。
```

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