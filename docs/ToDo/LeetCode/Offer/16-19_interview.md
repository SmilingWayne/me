# 面试题16.19_水域大小

<!-- 所有文件名必须是该题目的英文名 -->

!!! note
    <!-- 这里记载考察的数据结构、算法等 -->
    DFS 

- 🔑🔑 难度：<span style = "color:gold; font-weight:bold">Medium</span>
<!-- <span style = "color:gold; font-weight:bold">Medium</span> 中等 -->
<!-- <span style = "color:crisma; font-weight:bold">High</span> 困难 -->
<!-- <span style = "color:Green; font-weight:bold">Easy</span> 简单 -->

<!-- 题目简介 -->
> 你有一个用于表示一片土地的整数矩阵land，该矩阵中每个点的值代表对应地点的海拔高度。若值为0则表示水域。由垂直、水平或对角连接的水域为池塘。池塘的大小是指相连接的水域的个数。编写一个方法来计算矩阵中所有池塘的大小，返回值需要从小到大排序。



------

```
输入：
[
  [0,2,1,0],
  [0,1,0,1],
  [1,1,0,1],
  [0,1,0,1]
]
输出： [1,2,4]

```

-------------

=== "Python"

    ```Python
    
    class Solution:
        def pondSizes(self, land: List[List[int]]) -> List[int]:
            m , n = len(land), len(land[0])
            def dfs(x, y):
                land[x][y] = -1
                cnt = 1
                for i in range(x - 1, x + 2):
                    for j in range(y - 1, y + 2):
                        if i >= 0 and i < m and j >= 0 and j < n:
                            if land[i][j] == 0:
                                cnt += dfs(i, j)
                return cnt 
            
            res = []
            for i in range(m):
                for j in range(n):
                    if land[i][j] == 0:
                        res.append(dfs(i, j))

            res.sort()
            return res             
    ```

=== "Java"

    ```java
    class Solution {
        public int[] pondSizes(int[][] land) {
            int count=0;
            ArrayList<Integer> resList=new ArrayList<>();
            for(int i=0;i<land.length;i++){
                for(int j=0;j<land[0].length;j++){
                    if(land[i][j]==0){
                        count=dfs(land, i, j);
                        resList.add(count);
                    }
                }
            }
            int[] res=new int[resList.size()];
            for(int i=0;i<resList.size();i++){
                res[i]=resList.get(i);
            }
            Arrays.sort(res);
            return res;
        }
        public int dfs(int[][] land, int i, int j){
            if(i<0 || i>=land.length || j<0 || j>=land[0].length || land[i][j]!=0){
                return 0;
            }
            land[i][j]=-1;
            int count=1;
            count+=dfs(land, i+1, j);
            count+=dfs(land, i-1, j);
            count+=dfs(land, i, j+1);
            count+=dfs(land, i, j-1);
            count+=dfs(land, i+1, j+1);
            count+=dfs(land, i-1, j+1);
            count+=dfs(land, i-1, j-1);
            count+=dfs(land, i+1, j-1);
            return count;
        }
    }
    ```