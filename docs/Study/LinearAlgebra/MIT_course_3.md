# 矩阵乘法和逆矩阵

!!! abstract "outline"
    1. 矩阵乘法的五个视角
       1. 标准形式
       2. 列视角
       3. 行视角
       4. 列 * 行的视角
       5. 分块相乘的视角
    2. 逆矩阵的计算



## 矩阵乘法的五个视角


### 标准形式

$\begin{bmatrix} \cdots & \cdots & \cdots  \\ a_{31} & \cdots & a_{3n} \\ \cdots & \cdots & \cdots \end{bmatrix} \begin{bmatrix} \vdots & b_{41} & \vdots  \\ \vdots & b_{42} & \vdots \\ \vdots & b_{4m} & \vdots  \\ \\ \end{bmatrix}$ 

$c_{ij} = A$ 的第 $i$ 行 $\times B$ 的第 $j$ 列，或者说，$AB = C, A_{m\times n} B_{n \times p} = C_{mp}$


### 从整列的角度


$AB = \begin{bmatrix} 1 & 2 & 3 \\ 4  & 5 & 6 \end{bmatrix} \begin{bmatrix} 7 & 13 & 4 \\ 8 & 9 & 8 \\ 9 & 2 & 4 \end{bmatrix}$， 其结果的第 $p$ 列将是 $A$ 的各列的线性组合，其系数对应$B$矩阵的第 $p$ 列：（以第一列为例）$7 \begin{bmatrix} 1 \\ 4 \end{bmatrix} + 8 \begin{bmatrix} 2 \\ 5 \end{bmatrix} + 9 \begin{bmatrix} 3 \\ 6 \end{bmatrix} = \begin{bmatrix} 50 \\ 122 \end{bmatrix}$。

换一种说法是，将 $B$ 考虑成 $p$ 个单独的列向量，用 $A$ 乘每个列向量，排列成结果 $C$ ，C的各列是A的所有列的线性组合。（Columns of C  are combination of columns of A）


### 从整行的角度




