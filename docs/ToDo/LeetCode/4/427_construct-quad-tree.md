#### [427. 建立四叉树](https://leetcode-cn.com/problems/construct-quad-tree/)

🔑🔑 考点：递归 ｜ 数据结构 ｜四叉树

🚴‍♀️🚴‍♀️ 难度： <span style = "color:gold; font-weight:bold">Medium</span>

🔗🔗 链接：https://leetcode-cn.com/problems/construct-quad-tree/

📖📖 题目：【题目过长直接略去了】

给你一个 n * n 矩阵 grid ，矩阵由若干 0 和 1 组成。请你用四叉树表示该矩阵 grid 。

你需要返回能表示矩阵的 四叉树 的根结点。

注意，当 isLeaf 为 False 时，你可以把 True 或者 False 赋值给节点，两种值都会被判题机制 接受 。

四叉树数据结构中，每个内部节点只有四个子节点。此外，每个节点都有两个属性：

val：储存叶子结点所代表的区域的值。1 对应 True，0 对应 False；
isLeaf: 当这个节点是一个叶子结点时为 True，如果它有 4 个子节点则为 False 。

<div style = " margin:auto"> <img style = "float:left;height:50%;width:50%" src = "https://assets.leetcode.com/uploads/2020/02/12/e2mat.png" >
  <img style = "float:left;height:50%;width:50%" src = "https://assets.leetcode.com/uploads/2020/02/12/e2tree.png" >
</div>







💻💻 测试用例：

```
输入：grid = [[1,1,0,0],[1,1,0,0],[0,0,1,1],[0,0,1,1]]
输出：[[0,1],[1,1],[1,0],[1,0],[1,1]]

```

💡💡思路：

-  一开始完全没读懂题目的一道题。实际是一个递归。实现了“把一个0-1数组转化成一棵树，树的每一个节点实际是数组的一个子方阵，方阵里每个元素都是相同的”。例如上图左上的4*4实际上都是1，这就是四叉树一个节点，对于右上 4 * 4，则必须递归地去进行操作，让这个4 * 4再细化到左上2 * 2， 右上2 * 2， 左下2 * 2， 右下2 * 2.
- 注意节点中各个数的含义：有的是表明是否是叶子结点的，有的是标注该节点的数值的。



👩🏻‍💻🧑🏻‍💻 代码：

```Java

class Solution {
    public Node construct(int[][] grid) {
        return recur(grid, 0, 0, grid.length);
    }

    public Node recur(int[][] grid, int x, int y, int count){
        if(count <= 0){
            return null;
        }
        for(int i = x; i < x + count; i ++ ){
            for(int j = y; j < y + count ; j ++ ){
                if(grid[i][j] != grid[x][y]){
                    return new Node(false, false, 
                        recur(grid, x, y, count / 2),
                        recur(grid, x , y + count/ 2, count / 2),
                        recur(grid, x + count/ 2, y, count / 2),
                        recur(grid, x + count/ 2, y+ count/ 2, count / 2));
                }
            }
        }
        return new Node(grid[x][y] == 1, true, null, null, null, null);
    }
}
```









