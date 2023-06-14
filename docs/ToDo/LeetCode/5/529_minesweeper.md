# 529_扫雷游戏

<!-- 所有文件名必须是该题目的英文名 -->

!!! note
    <!-- 这里记载考察的数据结构、算法等 -->
    BFS
    

- 🔑🔑 难度：<span style = "color:gold; font-weight:bold">Medium</span>
<!-- <span style = "color:gold; font-weight:bold">Medium</span> 中等 -->
<!-- <span style = "color:crisma; font-weight:bold">High</span> 困难 -->
<!-- <span style = "color:Green; font-weight:bold">Easy</span> 简单 -->

<!-- 题目简介 -->
- 题目

让我们一起来玩扫雷游戏！

给你一个大小为 m x n 二维字符矩阵 board ，表示扫雷游戏的盘面，其中：

'M' 代表一个 未挖出的 地雷，
'E' 代表一个 未挖出的 空方块，
'B' 代表没有相邻（上，下，左，右，和所有4个对角线）地雷的 已挖出的 空白方块，
数字（'1' 到 '8'）表示有多少地雷与这块 已挖出的 方块相邻，
'X' 则表示一个 已挖出的 地雷。
给你一个整数数组 click ，其中 click = [clickr, clickc] 表示在所有 未挖出的 方块（'M' 或者 'E'）中的下一个点击位置（clickr 是行下标，clickc 是列下标）。

根据以下规则，返回相应位置被点击后对应的盘面：

如果一个地雷（'M'）被挖出，游戏就结束了- 把它改为 'X' 。
如果一个 没有相邻地雷 的空方块（'E'）被挖出，修改它为（'B'），并且所有和其相邻的 未挖出 方块都应该被递归地揭露。
如果一个 至少与一个地雷相邻 的空方块（'E'）被挖出，修改它为数字（'1' 到 '8' ），表示相邻地雷的数量。
如果在此次点击中，若无更多方块可被揭露，则返回盘面。


> 输入：board = [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]], click = [3,0]
> 输出：[["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]


------

> 解析

-------------

=== "这里写编程语言"

    ```java
    class Solution {
        public char[][] updateBoard(char[][] board, int[] click) {
            int x = click[0];
            int y = click[1];
            int countBomb = 0;
            if(board[x][y] == 'M'){
                board[x][y] = 'X';
                return board; 
            }
            else{
                boolean existBomb = false;
                int count = 0;
                for(int i = x - 1; i <= x + 1; i ++ ){
                    for(int j = y - 1; j <= y + 1; j ++ ){
                        if(i < 0 || j < 0 || i > board.length -1 || j > board[0].length -1 || (i == x && j == y)){
                            continue;
                        }
                        else{
                            if(board[i][j] == 'M'){
                                existBomb = true;
                                count ++;
                            }
                        }
                        
                    }

                }
                if(existBomb){
                    board[x][y] = (char)(count + '0');
                    return board;
                }
                else{
                    process(board, x , y);
                }
            }
            return board;
        }
        public void process(char[][] board, int x , int y ){
            if(x < 0 || y < 0 || x >= board.length || y >= board[0].length || board[x][y] == 'M'){
                return ;
            }
            else if(board[x][y] == 'E'){
            boolean isBomb = false;
            int count = 0 ;
            for(int i = x - 1; i <= x + 1; i ++ ){
                for(int j = y - 1; j <= y + 1; j ++ ){
                    if(i < 0 || j < 0 || i > board.length - 1 || j > board[0].length -1){
                        continue;
                    }
                    if(board[i][j] == 'M'){
                    
                        isBomb = true;
                        count ++;
                    }
                }
            }
            if(isBomb){
                board[x][y] = (char)(count + '0');
                    return;
            }
            else{
                board[x][y] = 'B';
                process(board, x + 1, y);
                process(board, x - 1, y);
                process(board, x + 1, y + 1);
                process(board, x - 1, y - 1);
                process(board, x + 1, y - 1);
                process(board, x - 1, y + 1);
                process(board, x , y + 1);
                process(board, x , y - 1);
            }
            }
        }
        
    }

    ```