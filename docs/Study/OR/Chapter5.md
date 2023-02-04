# 非线性规划

!!! Abstract
    前面介绍的都是目标函数和约束条件都是自变量的线性函数，如果目标函数或约束条件中包含一个或者若干自变量的非线性函数，那么这样的规划问题就属于非线性规划（Nonlinear Programming)

### 5.1 概述

#### 5.1.1 举例

- 某化学反应生成物浓度和时间t之间的关系是经验函数 \chi = c_1 + c_2 t + e^{c_3 t}，需要确定参数 c_1, c_2, c_3 使得理论曲线尽可能地和n个测试点吻合。

- 仓库选址问题：n个市场，第j个市场的位置(a_j, b_j)，对某种货物的需求为q_j ( j = 1,2,...,n)。现在计划建立m个仓库，第i个仓库的容量为c_i ( i = 1,2,...,m)，试确定仓库位置，使各个仓库到各个市场的运输量和路程的乘积之和最小。

$$ min \hspace{4pt} \sum \limits^{m}_{i = 1} \sum \limits^{n}_{j=1} w_{ij} \sqrt{(x_i - a_j)^2 + (y_i - b_j)^2}$$

$$s.t. \hspace{4pt} \left\{ \begin{aligned} \sum \limits^{n}_{j = 1} w_{ij} & \leq c_i, i = 1,..,m  \\ \sum \limits^{m}_{i=1} w_{ij} & = q_j, j = 1,2,...,n \\ w_{ij} & \geq 0, i = 1,..,m;j =1,2,...,n  \end{aligned} \right. $$

### 5.1.2 非线性规划的数学模型

非线性规划数学模型的一般形式是： $$min \hspace{4pt} f(x)$$

$$s.t. \left\{ \begin{aligned} g_i(x) & \geq 0, i = 1,2,...,l \\ h_j(x) & = 0, j = 1,2,...,m \end{aligned} \right.$$

这里的x = (x_1, x_2,...,x_n)^{T} 是n维空间R^{n}的点（向量），目标函数f(x)和约束函数g_i(x)，h_j(x) 是x的实函数，且其中至少有一个是x的非线性函数。g_i(x) 称为不等式约束，h_j(x) 是等式约束，若某个不等式是小于等于约束，同乘-1即可，同样，目标函数是极大的话，乘-1变号即可，如果是等式约束h_j(x) = 0，则用 h_j(x) \leq 0 和 h_j(x) \leq 0替换即可。

- 若令 $\Omega$ 为问题的可行解集合（可行域），则上述模型可写为 

$$\mathop{\min}\limits_{x \in \Omega} \hspace{2pt}f(x) \tag{5.4}$$

若$\Omega = \{ x| g_i(x) \geq 0, i = 1,2,..,l \}$ 是 $R^n$ 的一个子集。若 $\Omega = R^n$ ，那么该问题就是一个无约束优化问题(Unconstrained Optimization Problem)，求目标函数极小值或极大值的优化问题也称为极值问题。

## 5.2 非线性规划问题的解

### 5.2.1 解（极值点）的定义

- **局部极小点**：若存在某个 $\varepsilon > 0$，使得对于所有与x^{*} 的距离小于$\varepsilon$ 的$x \in \Omega$，即在$x^{*}$ 的某个邻域 $N_{\varepsilon}(x^{*}) = \{ x \in \Omega | \hspace{6pt} \Vert x - x^{*} \Vert  < \varepsilon \}$中，任意$x \in N_{\varepsilon}(x^{*})$，都有$f(x) \geq f(x^{*})$，则称点$x^{*}$ 为非线性规划问题(5.4)的局部极小点。如果对于任意 $x \in N_{\varepsilon} (x^{*})$且$x \neq x^{*}$，都有$f(x) > f(x^{*})$，则称点$x^{*}$ 为严格局部极小点。
- **严格局部极小点**：若对任意 $x \in N_{\varepsilon}(x^{*})$ 且 $x \neq x^{*}$，都有$f(x) > f(x^{*})$，那么点x^{*}为**严格局部极小点**。

- **全局极小点**：【补充】
  
### 5.2.2 多元函数极值点的存在条件

- **可行方向**：对于给定点 $x \in \Omega$， 向量$p$称为是在点 $x$ 处的一个可行方向，如果存在 $\overline{\alpha} > 0$，使得任意$0 \leq \alpha \leq \overline{\alpha}$，有 $x + \alpha p \in \Omega$。
- **定理5.1**: 设 f 是定义在集合 \Omega \in R^n 上的一阶连续可微函数，如果 x^* 是f在 \Omega 上的局部极小点，那么对 x^{*} 的任意可行方向 p \in R^{n}，有:

$$ \nabla f(x^{*}) = \{ \dfrac{\partial f(x^{*})}{\partial x_1}, \dfrac{}{}, ..., \dfrac{}{}\}$$