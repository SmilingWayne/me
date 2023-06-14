# 435_无重叠区间

<!-- 所有文件名必须是该题目的英文名 -->

!!! note
    <!-- 这里记载考察的数据结构、算法等 -->
    ？

- 🔑🔑 难度：<span style = "color:gold; font-weight:bold">Medium</span>
<!-- <span style = "color:gold; font-weight:bold">Medium</span> 中等 -->
<!-- <span style = "color:crisma; font-weight:bold">High</span> 困难 -->
<!-- <span style = "color:Green; font-weight:bold">Easy</span> 简单 -->

<!-- 题目简介 -->
给定一个区间的集合 intervals ，其中 intervals[i] = [start_i, end_i] 。返回 需要移除区间的最小数量，使剩余区间互不重叠 。


------

> 解析

-------------

=== "这里写编程语言"

    ```java
    class Solution {
        public int eraseOverlapIntervals(int[][] intervals) {
            if(intervals.length == 0 ){
                return 0;
            }
            Arrays.sort(intervals, new Comparator<int[]>(){
                public int compare(int[] a1, int[] a2){
                    return a1[1] - a2[1];
                }
            } );
            int end = intervals[0][1];
            int count = 1;
            for(int i = 0 ; i < intervals.length ; i ++ ){
                if(intervals[i][0] < end){
                    continue;
                }
                end = intervals[i][1];
                count ++ ;
            }
            return intervals.length - count;
        }
    }

    ```