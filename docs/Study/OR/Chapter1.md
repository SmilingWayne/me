- 线形规划（Linear Programming）：是在**线形约束**下**求解线性目标函数最优值**的数学理论和方法。
      - 决策变量(Decision Variables):
      - 目标函数(Objective Function):
      - 约束条件(Constraints):

$$max(min)z = \sum^{n}_{j = 1}{c_jx_j}$$

$$s.t. \sum^{n}_{j = 1}{a_{ij} }{x_j} \leq ( =, \geq) b_i , (i = 1,...m)$$

$$x_j \geq 0, (j = 1,...n)$$

- 线性规划模型的标准形式

$$max \quad z = \sum^{n}_{j = 1}{c_jx_j}$$

$$s.t. \sum^{n}_{j = 1}{a_{ij} }{x_j} = b_i , (i = 1,...m)$$

$$x_j \geq 0, (j = 1,...n)$$


- 满足约束条件（1-9）和（1-10）的解 $x = (x_1, x_2,....,x_n)^{T}$ 称为线性规划的**可行解**(Feasible solution)，全部可行解的集合称为**可行域**(Feasible Region).

$$max \quad z = c^{T}x\tag{1-8}$$

$$s.t. Ax = b\tag{1-9}$$

$$ x \geq 0\tag{1-10}$$

- 使目标函数(1-8)达到最大值的可行解称为线性规划问题的**最优解**(Optimal Solution)。
- 考虑等式约束方程组$Ax = b$，一般假设$m \times n$阶的系数矩阵A是行满秩，秩是m，若$B$是$A$中的一个$m \times m$阶的满秩子矩阵，则称$B$是线性规划问题的一个基(Basis)

- 基本解(Basic Solution)：
- 基本解的个数是有限的，最多有？个。
- 基本可行解(Basic Feasible Solution)
- 最优基本可行解(Basic Feasible Solution)
- 最优基（Optimal Basis)
- 凸集(Convex Set):
- 凸集的顶点（极点）：
- 两个凸集的交集仍然是凸集

- 线性规划解的**三个基本定理：**
    - 若线性规划的