# 529_省份数量

<!-- 所有文件名必须是该题目的英文名 -->

!!! note
    <!-- 这里记载考察的数据结构、算法等 -->
    ?

- 🔑🔑 难度：<span style = "color:gold; font-weight:bold">Medium</span>
<!-- <span style = "color:gold; font-weight:bold">Medium</span> 中等 -->
<!-- <span style = "color:crisma; font-weight:bold">High</span> 困难 -->
<!-- <span style = "color:Green; font-weight:bold">Easy</span> 简单 -->


有 n 个城市，其中一些彼此相连，另一些没有相连。如果城市 a 与城市 b 直接相连，且城市 b 与城市 c 直接相连，那么城市 a 与城市 c 间接相连。

省份 是一组直接或间接相连的城市，组内不含其他没有相连的城市。

给你一个 n x n 的矩阵 isConnected ，其中 isConnected[i][j] = 1 表示第 i 个城市和第 j 个城市直接相连，而 isConnected[i][j] = 0 表示二者不直接相连。

返回矩阵中 省份 的数量。


<!-- 题目简介 -->
> 输入：isConnected = [[1,1,0],[1,1,0],[0,0,1]]
> 输出：2

------

> 解析

-------------

=== "这里写编程语言"

    ```java
   class Solution {
        public int findCircleNum(int[][] M) {
            int res = 0;
            for(int i = 0 ; i < M.length; i++){
                for(int j = 0; j < M[0].length ; j++){
                    if(M[i][j] == 1){
                        res ++;
                        infect(M,i,j);
                    }
                }
            }
            return res;
        }
        public void infect(int[][] board, int i ,int j){
            board[i][j] = 2;
            for(int k = 0; k < board[0].length; k ++){
                if(board[i][k] == 1 ){
                    infect(board,i,k);
                }
            }
            for(int k = 0; k < board.length; k ++){
                if(board[k][j] == 1 ){
                    infect(board,k,j);
                }
            }
        }
    }


    ```