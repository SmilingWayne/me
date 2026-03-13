---
title: 随机变量的数字特征
slug: /study/statistics/number-characters
summary: 掌握期望、方差、协方差的核心概念与计算公式，理解全期望公式和条件方差公式的推导与应用，熟练运用相关系数判断随机变量间的线性关系。
---

# 第 4 章 随机变量的数字特征

!!! example "本章核心"

    掌握期望、方差、协方差的核心概念与计算公式，理解全期望公式和条件方差公式的推导与应用，熟练运用相关系数判断随机变量间的线性关系。

---

## 4.1 随机变量的数学期望

### 定义

**离散型随机变量：**

$$E(X) = \sum_{k=1}^{\infty} x_k p_k$$

其中 $P\{X=x_k\} = p_k$，要求级数**绝对收敛**。

**连续型随机变量：**

$$E(X) = \int_{-\infty}^{+\infty} x f(x) dx$$

要求积分**绝对收敛**。

### 常见分布的期望

| 分布 | 期望 |
|------|------|
| (0-1) 分布 | $p$ |
| 二项分布 $b(n,p)$ | $np$ |
| 泊松分布 $\pi(\lambda)$ | $\lambda$ |
| 几何分布 | $\frac{1}{p}$ |
| 均匀分布 $U[a,b]$ | $\frac{a+b}{2}$ |
| 指数分布 $e(\lambda)$ | $\frac{1}{\lambda}$ |
| 正态分布 $N(\mu, \sigma^2)$ | $\mu$ |

### 期望的性质

1. $E(c) = c$（$c$ 为常数）
2. $E(cX) = cE(X)$（$c$ 为常数）
3. $E(X+Y) = E(X) + E(Y)$
4. 若 $X, Y$ 相互独立，则 $E(XY) = E(X)E(Y)$
5. **许瓦尔兹不等式**：$|E(XY)|^2 \leq E(X^2)E(Y^2)$

### 随机变量函数的期望

**离散型：**

$$E[g(X)] = \sum_{k=1}^{\infty} g(x_k) p_k$$

**连续型：**

$$E[g(X)] = \int_{-\infty}^{+\infty} g(x) f(x) dx$$

**二维随机变量：**

$$E[g(X,Y)] = \sum_{i}\sum_{j} g(x_i, y_j) p_{ij}$$

$$E[g(X,Y)] = \int_{-\infty}^{+\infty}\int_{-\infty}^{+\infty} g(x,y) f(x,y) dxdy$$

---

## 4.2 条件期望

### 定义

**离散型：**

$$E(X|Y=y) = \sum_{x} x P(X=x|Y=y) = \sum_{x} x p_{X|Y}(x|y)$$

**连续型：**

$$E(X|Y=y) = \int_{-\infty}^{+\infty} x f_{X|Y}(x|y) dx$$

### 重要性质

**全期望公式：**

$$E(X) = E[E(X|Y)]$$

离散型：

$$E(X) = \sum_{y} E(X|Y=y) P(Y=y)$$

连续型：

$$E(X) = \int_{-\infty}^{+\infty} E(X|Y=y) f_Y(y) dy$$

### 条件期望的性质

1. $E[g(X)|Y=y] = \sum_{x} g(x) p_{X|Y}(x|y)$（离散型）
2. $E[g(X)|Y=y] = \int_{-\infty}^{+\infty} g(x) f_{X|Y}(x|y) dx$（连续型）
3. $E\left[\sum_{i=1}^{n} X_i | Y=y\right] = \sum_{i=1}^{n} E(X_i|Y=y)$

---

## 4.3 方差

### 定义

$$Var(X) = D(X) = E[(X - E(X))^2]$$

**计算公式：**

$$Var(X) = E(X^2) - [E(X)]^2$$

**标准差：** $\sqrt{D(X)}$

### 常见分布的方差

| 分布 | 方差 |
|------|------|
| (0-1) 分布 | $p(1-p)$ |
| 二项分布 $b(n,p)$ | $np(1-p)$ |
| 泊松分布 $\pi(\lambda)$ | $\lambda$ |
| 均匀分布 $U[a,b]$ | $\frac{(b-a)^2}{12}$ |
| 指数分布 $e(\lambda)$ | $\frac{1}{\lambda^2}$ |
| 正态分布 $N(\mu, \sigma^2)$ | $\sigma^2$ |

### 方差的性质

1. $D(c) = 0$（$c$ 为常数）
2. $D(cX) = c^2 D(X)$（$c$ 为常数）
3. 若 $X, Y$ 相互独立，则 $D(X \pm Y) = D(X) + D(Y)$
4. $D(X) = 0$ 的充要条件是 $P\{X = c\} = 1$，其中 $c = E(X)$

**推广：**

$$D\left(\sum_{i=1}^{n} c_i X_i\right) = \sum_{i=1}^{n} c_i^2 D(X_i)$$

（当 $X_1, X_2, \ldots, X_n$ 相互独立时）

### 切比雪夫 (Chebyshev) 不等式

设随机变量 $X$ 具有数学期望 $E(X) = \mu$，方差 $D(X) = \sigma^2$，则对任意 $\varepsilon > 0$，有：

$$P\{|X - \mu| \geq \varepsilon\} \leq \frac{\sigma^2}{\varepsilon^2}$$

或等价地：

$$P\{|X - \mu| < \varepsilon\} \geq 1 - \frac{\sigma^2}{\varepsilon^2}$$

### 标准化随机变量

设 $E(X) = \mu$，$D(X) = \sigma^2 > 0$，则

$$X^* = \frac{X - \mu}{\sigma}$$

称为 $X$ 的标准化随机变量，满足：

$$E(X^*) = 0, \quad D(X^*) = 1$$

---

## 4.4 条件方差

### 定义

$$Var(X|Y) = E[(X - E(X|Y))^2 | Y]$$

**计算公式：**

$$Var(X|Y) = E(X^2|Y) - [E(X|Y)]^2$$

### 条件方差公式（重要！）

!!! warning "核心公式"

    $$Var(X) = E[Var(X|Y)] + Var(E(X|Y))$$

**推导过程：**

- $E[Var(X|Y)] = E(X^2) - E[(E(X|Y))^2]$
- $Var(E(X|Y)) = E[(E(X|Y))^2] - (E(X))^2$
- 两式相加即得条件方差公式

---

## 4.5 条件期望及预测

### 最优预测

在均方误差最小的意义下，$Y$ 关于 $X$ 的最优预测为：

$$g(X) = E(Y|X)$$

即：

$$E[(Y - g(X))^2] \geq E[(Y - E(Y|X))^2]$$

### 最优线性预测

当不知道联合分布或计算复杂时，$Y$ 关于 $X$ 的最优线性预测为：

$$\hat{Y} = \mu_y + \rho \frac{\sigma_y}{\sigma_x}(X - \mu_x)$$

其中：

- $\mu_x = E(X)$，$\mu_y = E(Y)$
- $\sigma_x^2 = Var(X)$，$\sigma_y^2 = Var(Y)$
- $\rho$ 为 $X, Y$ 的相关系数

**均方误差：**

$$E[(Y - \hat{Y})^2] = \sigma_y^2(1 - \rho^2)$$

当 $\rho$ 接近 $\pm 1$ 时，均方误差接近于 0。

---

## 4.6 协方差和相关系数

### 协方差的定义

$$Cov(X,Y) = E[(X - E(X))(Y - E(Y))]$$

**计算公式：**

$$Cov(X,Y) = E(XY) - E(X)E(Y)$$

**与方差的关系：**

$$D(X \pm Y) = D(X) + D(Y) \pm 2Cov(X,Y)$$

### 协方差的性质

1. $Cov(X,Y) = Cov(Y,X)$
2. $Cov(a_1X + b_1, a_2Y + b_2) = a_1a_2 Cov(X,Y)$
3. $Cov(X_1 + X_2, Y) = Cov(X_1, Y) + Cov(X_2, Y)$
4. $Cov(X, a) = 0$，$Cov(X, X) = D(X)$
5. 若 $X, Y$ 相互独立，则 $Cov(X,Y) = 0$
6. **$|Cov(X,Y)|^2 \leq D(X) \cdot D(Y)$**（等号成立当且仅当 $X$ 与 $Y$ 有严格线性关系）

**公式：**

$$Cov(aX+bY, cX+dY) = acD(X) + (ad+bc)Cov(X,Y) + bdD(Y)$$

### 相关系数的定义

$$\rho_{XY} = \frac{Cov(X,Y)}{\sqrt{D(X)D(Y)}} = \frac{Cov(X,Y)}{\sigma_X \sigma_Y}$$

其中 $\sigma_X, \sigma_Y > 0$。

**标准化随机变量的协方差：**

$$\rho_{XY} = Cov(X^*, Y^*)$$

其中 $X^* = \frac{X - E(X)}{\sqrt{D(X)}}$，$Y^* = \frac{Y - E(Y)}{\sqrt{D(Y)}}$

### 相关系数的性质

1. **$|\rho_{XY}| \leq 1$**
2. **$|\rho_{XY}| = 1$ 的充要条件：** $X$ 与 $Y$ 以概率 1 线性相关，即存在常数 $a \neq 0, b$，使得 $P\{Y = aX + b\} = 1$
3. 若 $X, Y$ 相互独立，则 $\rho_{XY} = 0$

### 不相关的定义

若 $\rho_{XY} = 0$，称 $X$ 和 $Y$ **不相关**。

!!! note "独立 vs 不相关"

    - 不相关是指没有线性相关关系
    - 相互独立 $\Rightarrow$ 不相关（但逆命题一般不成立）
    - **特殊情况：** 当 $(X,Y)$ 服从二维正态分布时，$X, Y$ 相互独立 $\Leftrightarrow$ $X, Y$ 不相关

---

## 4.7 矩、协方差矩阵

### 矩的定义

设 $X$ 和 $Y$ 是随机变量：

1. **$k$ 阶原点矩：** $E(X^k)$，$k = 1, 2, \ldots$
2. **$k$ 阶中心矩：** $E[(X - E(X))^k]$，$k = 1, 2, \ldots$
3. **$(k+l)$ 阶混合矩：** $E(X^k Y^l)$，$k, l = 1, 2, \ldots$
4. **$(k+l)$ 阶混合中心矩：** $E[(X - E(X))^k (Y - E(Y))^l]$，$k, l = 1, 2, \ldots$

**说明：**

- $E(X), E(Y)$ 为一阶原点矩
- $D(X), D(Y)$ 为二阶中心矩
- $Cov(X,Y)$ 为二阶混合中心矩

### 协方差矩阵

**二维随机变量 $(X_1, X_2)$ 的协方差矩阵：**

$$C = \begin{pmatrix} c_{11} & c_{12} \\ c_{21} & c_{22} \end{pmatrix}$$

其中：

- $c_{11} = E[(X_1 - E(X_1))^2] = D(X_1)$
- $c_{12} = c_{21} = E[(X_1 - E(X_1))(X_2 - E(X_2))] = Cov(X_1, X_2)$
- $c_{22} = E[(X_2 - E(X_2))^2] = D(X_2)$

**$n$ 维随机变量的协方差矩阵：**

$$C = (c_{ij})_{n \times n}$$

其中 $c_{ij} = Cov(X_i, X_j)$，$i, j = 1, 2, \ldots, n$

### 协方差矩阵的性质

1. $C$ 是对称矩阵（$c_{ij} = c_{ji}$）
2. $c_{ii} = D(X_i)$，$i = 1, 2, \ldots, n$
3. $c_{ij}^2 \leq c_{ii} c_{jj}$，$i, j = 1, 2, \ldots, n$
4. $C$ 是非负定矩阵，即对任意向量 $a = (a_1, a_2, \ldots, a_n)^T$，都有 $a^T C a \geq 0$

### $n$ 维正态分布

**定义：**

$n$ 维随机变量 $(X_1, X_2, \ldots, X_n)$ 服从 $n$ 维正态分布，记作：

$$(X_1, X_2, \ldots, X_n) \sim N(\mu, C)$$

其中：

- $\mu = (\mu_1, \mu_2, \ldots, \mu_n)^T$ 为 $n$ 维常向量
- $C$ 为 $n$ 阶对称正定矩阵（协方差矩阵）

**概率密度函数：**

$$f(x_1, x_2, \ldots, x_n) = \frac{1}{(2\pi)^{n/2} |C|^{1/2}} \exp\left\{-\frac{1}{2}(x - \mu)^T C^{-1} (x - \mu)\right\}$$

### $n$ 维正态分布的性质

1. **边缘分布：** $n$ 维正态变量的每一个分量 $X_i$ 都是正态变量；反之，若 $X_1, X_2, \ldots, X_n$ 都是正态变量且相互独立，则 $(X_1, X_2, \ldots, X_n)$ 是 $n$ 维正态变量。

2. **线性组合：** $n$ 维随机变量 $(X_1, X_2, \ldots, X_n)$ 服从 $n$ 维正态分布的充要条件是 $X_1, X_2, \ldots, X_n$ 的任一线性组合 $l_1X_1 + l_2X_2 + \cdots + l_nX_n$ 服从一维正态分布。

3. **线性变换：** 若 $(X_1, X_2, \ldots, X_n)$ 服从 $n$ 维正态分布，设 $Y_1, Y_2, \ldots, Y_n$ 是 $X_j (j = 1, 2, \ldots, n)$ 的线性函数，则 $(Y_1, Y_2, \ldots, Y_n)$ 也服从多维正态分布。

4. **独立与不相关：** 若 $(X_1, X_2, \ldots, X_n)$ 服从 $n$ 维正态分布，则"$X_1, X_2, \ldots, X_n$ 相互独立"与"$X_1, X_2, \ldots, X_n$ 两两不相关"是等价的。

---

## 重要公式总结

!!! example "必须掌握的核心公式"

    1. **全期望公式：** $E(X) = E[E(X|Y)]$

    2. **条件方差公式：** $Var(X) = E[Var(X|Y)] + Var(E(X|Y))$

    3. **协方差计算：** $Cov(X,Y) = E(XY) - E(X)E(Y)$

    4. **相关系数：** $\rho_{XY} = \frac{Cov(X,Y)}{\sqrt{D(X)D(Y)}}$

    5. **方差和：** $D(X \pm Y) = D(X) + D(Y) \pm 2Cov(X,Y)$

    6. **切比雪夫不等式：** $P\{|X - \mu| \geq \varepsilon\} \leq \frac{\sigma^2}{\varepsilon^2}$

    7. **最优线性预测：** $\hat{Y} = \mu_y + \rho \frac{\sigma_y}{\sigma_x}(X - \mu_x)$
