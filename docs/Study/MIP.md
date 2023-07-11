# 大规模整数规划算法

## 7.10 Afternoon


- 仿射独立。


- Find XW tomorrow morning?

- 4h? battery? Signature?

- Functional Failure

- useless cut callback


> 一些比较没用的算法：蚁群那种的：都是随机的搜索，跟随你搜索范围的扩大而扩大。


---------


## 7.11 Morning
### The Bin Packing Problem

- 给定 K个容量1的箱子和n个物品（i=1,...n），大小是s_i \in  (0, 1]
- 找到最小的能够装下所有物品的最小的箱子的数量。


- 拉格朗日函数会给出一个下界，我们找一个最好的下界，也就是加一个max函数
- 拉格朗日对偶（LD）两次使用对偶把max-min转化成min。
- 对偶Gap（Duality Gap)


### DW 分解

- 用来求解一些具有特殊性质的线性规划问题。
    - 含有大量的0矩阵，约束条件都是一块一块地在对角线出现等；
    - 利用多面体表示定理，将等式约束F_1 x_1 = b_1, F_2 x_2 = b_2 转换成了许多的新变量；

!!! question 什么是多面体表示定理？
    极点和极线具体怎么做？

- DW分解可以扩展成把矩阵扩展成不止两块的情况；


-----------


### Benders 分解
$\min \sum_{i \in M} \sum_{j \in N} c_{ij} x_{ij} + \sum_{j \in N}f_j y_j$

$\sum_{j \in N} x_{ij} = 1$

$\sum_{} x_{ij} q_i \leq y_i \omega$






