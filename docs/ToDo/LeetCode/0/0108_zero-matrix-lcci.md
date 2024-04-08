# 0108_零矩阵

<!-- 所有文件名必须是该题目的英文名 -->

!!! note
    <!-- 这里记载考察的数据结构、算法等 -->
    Array, 首行、首列标记法。单独处理首行首列的情况。

- 🔑🔑 难度：
<!-- <span style = "color:gold; font-weight:bold">Medium</span> 中等 -->
<!-- <span style = "color:crisma; font-weight:bold">High</span> 困难 -->
<!-- <span style = "color:Green; font-weight:bold">Easy</span> 简单 -->

<!-- 题目简介 -->

> 编写一种算法，若M × N矩阵中某个元素为0，则将其所在的行与列清零。
> 
```
```

------

??? note 

    
-------------

=== "Python"

    ```Python
    class Solution:
        def setZeroes(self, matrix: List[List[int]]) -> None:
            """
            Do not return anything, modify matrix in-place instead.
            """
            zerorow, zerocol = False, False
            m , n = len(matrix), len(matrix[0])
            for i in range(n):
                if matrix[0][i] == 0:
                    zerorow = True
                    break
            for j in range(m):
                if matrix[j][0] == 0:
                    zerocol = True
                    break
            for i in range(1, m):
                for j in range(1, n):
                    if matrix[i][j] == 0:
                        matrix[i][0] = 0
                        matrix[0][j] = 0

            for j in range(1, n):
                if matrix[0][j] == 0:
                    for i in range(1, m):
                        matrix[i][j] = 0
            for i in range(1, m):
                if matrix[i][0] == 0:
                    for j in range(1, n):
                        matrix[i][j] = 0
            if zerocol:
                for i in range(m):
                    matrix[i][0] = 0
            if zerorow:
                for j in range(n):
                    matrix[0][j] = 0
    ```
