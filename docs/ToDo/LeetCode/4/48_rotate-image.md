# 48_旋转矩阵

<!-- 所有文件名必须是该题目的英文名 -->

!!! note
    <!-- 这里记载考察的数据结构、算法等 -->
    矩阵操作

- 🔑🔑 难度：<span style = "color:gold; font-weight:bold">Medium</span>
<!-- <span style = "color:gold; font-weight:bold">Medium</span> 中等 -->
<!-- <span style = "color:crisma; font-weight:bold">High</span> 困难 -->
<!-- <span style = "color:Green; font-weight:bold">Easy</span> 简单 -->

<!-- 题目简介 -->

> 给你一幅由 N × N 矩阵表示的图像，其中每个像素的大小为 4 字节。请你设计一种算法，将图像旋转 90 度。
> 
> 不占用额外内存空间能否做到？
> 
```
给定 matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 

原地旋转输入矩阵，使其变为:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]

```

------

??? note 

    实际上可以视作4个区域的旋转。具体推理可以参考如下：


    ![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202404161128056.png)

    待补充连接：https://leetcode.cn/problems/rotate-image/

    
-------------

=== "Python"

    ```Python
    class Solution:
        def rotate(self, matrix: List[List[int]]) -> None:
            """
            Do not return anything, modify matrix in-place instead.
            """
            n = len(matrix)
            for i in range(n // 2):
                for j in range((n + 1) // 2):
                    temp = matrix[i][j]
                    matrix[i][j] = matrix[n - j - 1][i]
                    matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
                    matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
                    matrix[j][n - i - 1]  = temp
    
    ```
