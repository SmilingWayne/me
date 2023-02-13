# 随机变量的数字特征


## 随机变量函数的数学期望公式


- Y = g(X) 离散型
- 连续型

## 离散型：

P \{ X = x_k \} = p_k, k = 1,2,..

如果级数 \sum \limits^{\infty}_{k= 1} x_k p_k 绝对收敛，那么称呼 \sum \limits^{\infty}_{k= 1} x_k p_k 为随机变量的数学期望，记作 E(X). 如果发散，那么X的数学期望不存在。

### 0-1分布 
- E(X) = np


### binominal

- E(X) = np

### Poisson

- $X \sim \pi(\lambda)$

- $E(X) = \lambda$

### 几何分布
- p_k = q^{k-1} p, k = 1,2,...,第一次成功在k次实验的概率 
- E(X) = \dfrac{1}{p}


## 连续型

r.v. X 概率密度函数：f(x)，如果积分 $\int^{\infty}_{-\infty} xf(x)dx 绝对收敛，就把它叫做r.v.X的数学期望（均值）$

### 均匀分布 

$$f(x) = \left\{ \begin{aligned} \dfrac{1}{b-a} , a \leq x \leq b \\ 0, otherwise   \end{aligned} \right. $$

E(x) = \dfrac{a+b}{2}

### 指数分布
$$f(x) = \left{ \begin{aligned} \lambda e^{-\lambda x} , x \geq 0 \\ 0, x < 0 \end{aligned}$$

- E(x) = \dfrac{1}{\lambda}

### 正态分布

- X \sim N(\mu, \sigma^2)
- E(X) = \mu


## 均值的性质

- E(c) = c ， c是常数
- E(cX) = cE(X)， c是常数
- E(X + Y) = E(X) + E(Y)
- 如果X，Y相互独立，那么 E(XY) = E(X)E(Y)
- | E(XY) |^{2} \leq E(X^2)E(Y^2) 

##  4.2 条件期望

### 利用条件计算期望

- E(X | Y) 表示随机变量Y 的函数，在Y= y处的值为 E(X|Y = y)，这个E(X|Y)本身就是一个随机变量；
- E(X) = E(E(X|Y))

## 4.3 方差

- 描述了r.v对数学期望的离散程度；

- D(X) = var(X) = E[X - E(X)]^2，开根号就是标准差；
- Discrete: D(X) = \sum \limits_{k} (x_k - E(X))^2 p_k
- Continuous: D(X) = \int^{+\infty}_{-\infty} [ x - E(X)]^2 f(x) d(x)
- 计算公式$D(X) = E(X^2) - [E(X)]^2$