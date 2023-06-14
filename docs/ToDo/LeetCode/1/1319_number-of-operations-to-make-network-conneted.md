# 1319_连通网络的操作次数

<!-- 所有文件名必须是该题目的英文名 -->

!!! note
    <!-- 这里记载考察的数据结构、算法等 -->
    ？

- 🔑🔑 难度：<span style = "color:gold; font-weight:bold">Medium</span>


<!-- <span style = "color:gold; font-weight:bold">Medium</span> 中等 -->
<!-- <span style = "color:crisma; font-weight:bold">High</span> 困难 -->
<!-- <span style = "color:Green; font-weight:bold">Easy</span> 简单 -->

<!-- 题目简介 -->
用以太网线缆将 n 台计算机连接成一个网络，计算机的编号从 0 到 n-1。线缆用 connections 表示，其中 connections[i] = [a, b] 连接了计算机 a 和 b。

网络中的任何一台计算机都可以通过网络直接或者间接访问同一个网络中其他任意一台计算机。

给你这个计算机网络的初始布线 connections，你可以拔开任意两台直连计算机之间的线缆，并用它连接一对未直连的计算机。请你计算并返回使所有计算机都连通所需的最少操作次数。如果不可能，则返回 -1 。 

------

> 解析

-------------

=== "这里写编程语言"

    ```java
    class Solution {
        public  List<Integer>[] graph;
        public  boolean[] visited ;
        public int makeConnected(int n, int[][] connections) {
            if(connections.length < n - 1){
                return -1;
            }
            
            graph = new ArrayList[n];

            visited = new boolean[n];

            for(int i = 0; i < n ; i ++ ){
                graph[i] = new ArrayList<>();

            }
            for(int[] connection : connections){
                graph[connection[0]].add(connection[1]);
                graph[connection[1]].add(connection[0]);
            
            }
            int res = 0 ;
            for(int i = 0 ; i < n; i ++ ){
                if(!visited[i]){
                    dfs(i);
                    res ++ ;
                }
            }
            return res -1;
        }
        public void dfs(int x){
            visited[x] = true;
            for(int i = 0 ; i < graph[x].size(); i ++) {
                if(visited[graph[x].get(i)] == false){
                    dfs(graph[x].get(i));
                }
            }
        }
        
    }


    ```