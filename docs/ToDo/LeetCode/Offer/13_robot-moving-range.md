# Offer-13_机器人的活动范围

<!-- 所有文件名必须是该题目的英文名 -->

!!! note
    <!-- 这里记载考察的数据结构、算法等 -->
    DFS

- 🔑🔑 难度：<span style = "color:gold; font-weight:bold">Medium</span>
<!-- <span style = "color:gold; font-weight:bold">Medium</span> 中等 -->
<!-- <span style = "color:crisma; font-weight:bold">High</span> 困难 -->
<!-- <span style = "color:Green; font-weight:bold">Easy</span> 简单 -->

<!-- 题目简介 -->

> 地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？
>


```
输入：m = 3, n = 1, k = 0
输出：1
```

------

> 解析

-------------

=== "Java"

    ```java
    class Solution {
        boolean[][] visited;
        int count = 0;
        public int movingCount(int m, int n, int k) {
            visited = new boolean[m][n];
            dfs(0,0,k,m,n);
            return count;
        }

        public void dfs(int x, int y, int k, int m, int n){
            if(x >= m || y >= n || visited[x][y] == true ||
                (x % 10 + x / 10 + y % 10 + y / 10 ) > k){
                return;
            }
            visited[x][y] = true;
            count ++ ;
            dfs(x + 1, y, k, m, n);
            dfs(x, y + 1, k, m, n);
        }   
    }
    ```