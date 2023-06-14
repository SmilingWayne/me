#### [417. 太平洋大西洋水流问题](https://leetcode-cn.com/problems/pacific-atlantic-water-flow/)

🔑🔑 考点：逆向DFS 

🚴‍♀️🚴‍♀️ 难度： <span style = "color:gold; font-weight:bold">Medium</span>

🔗🔗 链接：https://leetcode-cn.com/problems/pacific-atlantic-water-flow/

📖📖 题目：

有一个 m × n 的矩形岛屿，与 太平洋 和 大西洋 相邻。 “太平洋” 处于大陆的左边界和上边界，而 “大西洋” 处于大陆的右边界和下边界。

这个岛被分割成一个由若干方形单元格组成的网格。给定一个 m x n 的整数矩阵 heights ， heights[r][c] 表示坐标 (r, c) 上单元格 高于海平面的高度 。

岛上雨水较多，如果相邻单元格的高度 小于或等于 当前单元格的高度，雨水可以直接向北、南、东、西流向相邻单元格。水可以从海洋附近的任何单元格流入海洋。

返回 网格坐标 result 的 2D列表 ，其中 result[i] = [ri, ci] 表示雨水可以从单元格 (ri, ci) 流向 太平洋和大西洋 。

💻💻 测试用例：

```
输入: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
输出: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
输入: heights = [[2,1],[1,2]]
输出: [[0,0],[0,1],[1,0],[1,1]]
```

💡💡思路：

- 正常思路：遍历所有的点，一旦可以到达Atlantic就把这个坐标+1，一旦可以到达Pacific就也+1，遍历结束之后所有坐标为2的就是同时到达两个地方的“岛”。
- 逆向思路：从两个洋边界分别开始遍历，找出从边界到矩阵内所有可以到达的点，如果某个点均被遍历到，则这个点就是一定可达到两个海洋的。

👩🏻‍💻🧑🏻‍💻 代码：

```Java
class Solution {
    List<List<Integer>> ans = new ArrayList<>();
    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        boolean[][] pacific = new boolean[heights.length][heights[0].length];
        boolean[][] atlantic = new boolean[heights.length][heights[0].length];
        for(int i = 0; i < heights.length; i ++ ){
            dfs(heights, pacific, i, 0, heights[i][0]);
            dfs(heights, atlantic, i, heights[0].length - 1, heights[i][heights[0].length - 1]);
        }
        for(int i = 0; i < heights[0].length; i ++ ){
            dfs(heights, pacific, 0, i, heights[0][i]);
            dfs(heights, atlantic, heights.length - 1, i, heights[heights.length - 1][i]);
        }
        for(int i = 0; i < pacific.length; i ++ ){
            for(int j = 0; j < pacific[0].length; j ++ ){
                if(pacific[i][j] && atlantic[i][j]){
                    List<Integer> t = new ArrayList<>();
                    t.add(i);
                    t.add(j);
                    ans.add(t);
                }
            }
        }
        return ans;
    }
    public void dfs(int[][] heights, boolean[][] isvisited, int x, int y, int pre){
        if(x < 0 || y < 0 || x > heights.length - 1|| y > heights[0].length - 1 || isvisited[x][y] || heights[x][y] < pre){
            return ;
        }
        isvisited[x][y] = true;
        dfs(heights, isvisited, x + 1, y, heights[x][y]);
        dfs(heights, isvisited, x - 1, y,heights[x][y]);
        dfs(heights, isvisited, x, y+1,heights[x][y]);
        dfs(heights, isvisited, x , y-1,heights[x][y]);
    }
}
```



