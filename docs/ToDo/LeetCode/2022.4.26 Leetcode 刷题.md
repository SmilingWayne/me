#### [883. 三维形体投影面积](https://leetcode-cn.com/problems/projection-area-of-3d-shapes/)

🔑🔑 考点：数组

🚴‍♀️🚴‍♀️ 难度： <span style = "color:darkgreen; font-weight:bold">Easy</span>

🔗🔗 链接：https://leetcode-cn.com/problems/projection-area-of-3d-shapes/

📖📖 题目：

在 n x n 的网格 grid 中，我们放置了一些与 x，y，z 三轴对齐的 1 x 1 x 1 立方体。

每个值 v = grid[i][j] 表示 v 个正方体叠放在单元格 (i, j) 上。

现在，我们查看这些立方体在 xy 、yz 和 zx 平面上的投影。

投影 就像影子，将 三维 形体映射到一个 二维 平面上。从顶部、前面和侧面看立方体时，我们会看到“影子”。

返回 所有三个投影的总面积 。

<img style = "height: 50%; width:50%" src = "https://s3-lc-upload.s3.amazonaws.com/uploads/2018/08/02/shadow.png">

💻💻 测试用例：

```
输入：[[1,2],[3,4]]
输出：17
```

💡💡思路：

- 简单遍历：1）几个地方是有方块的？2）这条面投影哪里方块最多？

👩🏻‍💻🧑🏻‍💻 代码：

```Java
class Solution {
    public int projectionArea(int[][] grid) {
        int ans = 0;
        for(int i = 0; i < grid.length; i ++ ){
            int max = 0;
            for(int j = 0; j < grid[0].length; j ++ ){
                max = Math.max(grid[i][j], max);
                if(grid[i][j] != 0){
                    ans ++ ;
                }
            }
            ans += max;
        }
        for(int i = 0; i < grid[0].length; i ++ ){
            int max = 0;
            for(int j = 0; j < grid.length; j ++ ){
                max = Math.max(grid[j][i], max);
            }
            ans += max;
        }
        return ans;
        

    }
}
```









