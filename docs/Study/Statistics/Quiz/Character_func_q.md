---
title: 特征函数核心习题精讲
slug: study/statistics/quiz/character-func-q
summary: 系统整理特征函数的核心计算方法与再生性证明，涵盖退化、泊松、Γ、正态、二项分布的解析推导及极限定理应用。
---

#  第 5 章 特征函数 - 习题

!!! example "本章要点"

    系统整理特征函数的核心计算方法与再生性证明，涵盖退化、泊松、Γ、正态、二项分布的解析推导及极限定理应用。

---

## 一、基本分布的特征函数

### 例题 1：退化分布的特征函数

**题目内容**：
求退化分布（单点分布）$I(x-c)$ 的特征函数。即随机变量 $\xi$ 以概率 1 取常数 $c$。

**答案/解答**：
特征函数为：

$$ f(t) = e^{itc} $$

**推导**：
根据特征函数定义 $f(t) = E[e^{it\xi}]$。
因为 $P(\xi = c) = 1$，所以：

$$ f(t) = e^{itc} \cdot 1 = e^{itc} $$

!!! note "考查思路"

    考查特征函数的基本定义以及最简单分布（退化分布）的计算。

!!! abstract "要点重点"

    - **特征函数定义**：$f(t) = E[e^{it\xi}]$
    - 退化分布是随机变量取定值的情况，其期望即为该定值的函数值

---

### 例题 2：泊松分布的特征函数

**题目内容**：
求泊松分布 $P(\lambda)$ 的特征函数。

**答案/解答**：
特征函数为：

$$ f(t) = e^{\lambda(e^{it} - 1)} $$

**推导**：
泊松分布分布律为 $P(\xi = k) = \frac{\lambda^k}{k!} e^{-\lambda}, k=0,1,2,\dots$。

$$ f(t) = \sum_{k=0}^{\infty} e^{itk} \frac{\lambda^k}{k!} e^{-\lambda} = e^{-\lambda} \sum_{k=0}^{\infty} \frac{(\lambda e^{it})^k}{k!} = e^{-\lambda} \cdot e^{\lambda e^{it}} = e^{\lambda(e^{it} - 1)} $$

!!! note "考查思路"

    考查离散型随机变量特征函数的计算公式（级数求和）及指数函数的泰勒展开。

!!! abstract "要点重点"

    - **离散型特征函数公式**：$f(t) = \sum e^{itx_k} p_k$
    - 利用 $\sum \frac{x^k}{k!} = e^x$ 进行化简

---

### 例题 3：$\Gamma$ 分布的特征函数

**题目内容**：
求 $\Gamma$ 分布 $G(\lambda, r)$ 的特征函数。其密度函数为 $p(x) = \frac{\lambda^r}{\Gamma(r)} x^{r-1} e^{-\lambda x}, x > 0$。

**答案/解答**：
特征函数为：

$$ f(t) = \left( 1 - \frac{it}{\lambda} \right)^{-r} $$

**推导**：

$$ f(t) = \int_{0}^{\infty} e^{itx} \frac{\lambda^r}{\Gamma(r)} x^{r-1} e^{-\lambda x} dx = \frac{\lambda^r}{\Gamma(r)} \int_{0}^{\infty} x^{r-1} e^{-(\lambda - it)x} dx $$

利用 $\Gamma$ 函数积分性质 $\int_{0}^{\infty} x^{r-1} e^{-\alpha x} dx = \frac{\Gamma(r)}{\alpha^r}$，令 $\alpha = \lambda - it$：

$$ f(t) = \frac{\lambda^r}{\Gamma(r)} \cdot \frac{\Gamma(r)}{(\lambda - it)^r} = \left( \frac{\lambda}{\lambda - it} \right)^r = \left( 1 - \frac{it}{\lambda} \right)^{-r} $$

!!! note "考查思路"

    考查连续型随机变量特征函数的计算（积分变换）及 $\Gamma$ 函数的性质。

!!! abstract "要点重点"

    - **连续型特征函数公式**：$f(t) = \int_{-\infty}^{\infty} e^{itx} p(x) dx$
    - 特征函数是密度函数的傅里叶变换
    - **积分技巧**：凑 $\Gamma$ 函数形式

---

### 例题 4：正态分布的特征函数

**题目内容**：
求正态分布 $N(a, \sigma^2)$ 的特征函数。先讨论标准正态分布 $N(0, 1)$ 的场合。

**答案/解答**：

1.  对于标准正态分布 $N(0, 1)$，特征函数为：


    $$ f(t) = e^{-\frac{t^2}{2}} $$

2.  对于一般正态分布 $N(a, \sigma^2)$，特征函数为：


    $$ f(t) = e^{iat - \frac{1}{2}\sigma^2 t^2} $$

**推导**：
对于 $N(0, 1)$，密度为 $\frac{1}{\sqrt{2\pi}} e^{-\frac{x^2}{2}}$。

$$ f(t) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} e^{itx} e^{-\frac{x^2}{2}} dx $$

利用偶函数性质及微分方程法（文中提到 $\ln f(t)$ 的导数关系），可得 $f(t) = e^{-\frac{t^2}{2}}$。

对于 $N(a, \sigma^2)$，利用性质 $\eta = a + \sigma \xi$（其中 $\xi \sim N(0,1)$），根据特征函数性质 $f_{\eta}(t) = e^{iat} f_{\xi}(\sigma t)$，代入即得。

!!! note "考查思路"

    考查重要分布的特征函数记忆及线性变换性质（性质 6）。

!!! abstract "要点重点"

    - **标准正态分布特征函数** $e^{-t^2/2}$ 是核心结论
    - **线性变换性质**：若 $\eta = a\xi + b$，则 $f_{\eta}(t) = e^{ibt} f_{\xi}(at)$

---

## 二、分布的再生性（可加性）

### 例题 5：二项分布的再生性

**题目内容**：
若 $\xi_1$ 服从二项分布 $b(n, p)$，$\xi_2$ 服从二项分布 $b(m, p)$，而且 $\xi_1$ 与 $\xi_2$ 独立。求证 $\eta = \xi_1 + \xi_2$ 服从 $b(n+m, p)$。

**答案/解答**：

**证明**：

二项分布 $b(n, p)$ 的特征函数为 $f(t) = (pe^{it} + q)^n$，其中 $q=1-p$。

由独立性（性质 4），和的特征函数等于特征函数之积：

$$ f_{\eta}(t) = f_{\xi_1}(t) \cdot f_{\xi_2}(t) = (pe^{it} + q)^n \cdot (pe^{it} + q)^m = (pe^{it} + q)^{n+m} $$

这正是参数为 $n+m$ 和 $p$ 的二项分布的特征函数。

由唯一性定理知，$\eta \sim b(n+m, p)$。

简记作：$b(n, p) * b(m, p) = b(n+m, p)$。

!!! note "考查思路"

    考查特征函数在判断独立随机变量和的分布中的应用（再生性）。

!!! abstract "要点重点"

    - **独立和的特征函数 = 特征函数的乘积**
    - **唯一性定理**：特征函数唯一决定分布函数
    - 二项分布参数 $p$ 必须相同才具有再生性

---

### 例题 6：泊松分布的再生性

**题目内容**：
若 $\xi_1$ 服从泊松分布 $\pi(\lambda_1)$，$\xi_2$ 服从 $\pi(\lambda_2)$，且相互独立。求 $\eta = \xi_1 + \xi_2$ 的分布。

**答案/解答**：

**解**：

泊松分布特征函数为 $f(t) = e^{\lambda(e^{it}-1)}$。

$$ f_{\eta}(t) = e^{\lambda_1(e^{it}-1)} \cdot e^{\lambda_2(e^{it}-1)} = e^{(\lambda_1 + \lambda_2)(e^{it}-1)} $$

故 $\eta$ 服从泊松分布 $\pi(\lambda_1 + \lambda_2)$。

简记作：$\pi(\lambda_1) * \pi(\lambda_2) = \pi(\lambda_1 + \lambda_2)$。

!!! note "考查思路"

    同上，考查泊松分布的再生性。

!!! abstract "要点重点"

    - **参数相加**：$\lambda = \lambda_1 + \lambda_2$

---

### 例题 7：正态分布的再生性

**题目内容**：
若 $\xi_1$ 服从 $N(a_1, \sigma_1^2)$，$\xi_2$ 服从 $N(a_2, \sigma_2^2)$，且相互独立。求 $\eta = \xi_1 + \xi_2$ 的分布。

**答案/解答**：

**解**：

正态分布特征函数为 $f(t) = e^{iat - \frac{1}{2}\sigma^2 t^2}$。

$$ f_{\eta}(t) = e^{ia_1 t - \frac{1}{2}\sigma_1^2 t^2} \cdot e^{ia_2 t - \frac{1}{2}\sigma_2^2 t^2} = e^{i(a_1+a_2)t - \frac{1}{2}(\sigma_1^2 + \sigma_2^2)t^2} $$

故 $\eta$ 服从 $N(a_1+a_2, \sigma_1^2 + \sigma_2^2)$。

!!! note "考查思路"

    考查正态分布的可加性。

!!! abstract "要点重点"

    - **均值相加**：$a = a_1 + a_2$
    - **方差相加**：$\sigma^2 = \sigma_1^2 + \sigma_2^2$

---

### 例题 8：$\Gamma$ 分布的再生性

**题目内容**：
若 $\xi_1$ 服从 $G(\lambda, r_1)$，$\xi_2$ 服从 $G(\lambda, r_2)$，而且 $\xi_1$ 与 $\xi_2$ 独立。求 $\eta = \xi_1 + \xi_2$ 的分布。

**答案/解答**：

**解**：

$\Gamma$ 分布特征函数为 $f(t) = (1 - \frac{it}{\lambda})^{-r}$。

$$ f_{\eta}(t) = \left( 1 - \frac{it}{\lambda} \right)^{-r_1} \cdot \left( 1 - \frac{it}{\lambda} \right)^{-r_2} = \left( 1 - \frac{it}{\lambda} \right)^{-(r_1 + r_2)} $$

故 $\eta$ 服从 $G(\lambda, r_1 + r_2)$。

!!! note "考查思路"

    考查 $\Gamma$ 分布的再生性。

!!! abstract "要点重点"

    - 尺度参数 $\lambda$ 必须相同
    - **形状参数相加**：$r = r_1 + r_2$

---

## 三、特征函数的应用

### 应用题 1：利用特征函数求正态分布的数字特征

**题目内容**：
求 $N(\mu, \sigma^2)$ 分布的数学期望和方差。

**答案/解答**：

**解**：

已知 $N(\mu, \sigma^2)$ 的特征函数为 $\varphi(t) = e^{i\mu t - \frac{1}{2}\sigma^2 t^2}$。

利用性质：$E(\xi^k) = \frac{\varphi^{(k)}(0)}{i^k}$。

1.  **求一阶导数**：


    $$ \varphi'(t) = (i\mu - \sigma^2 t) \varphi(t) $$

    $$ \varphi'(0) = i\mu \cdot 1 = i\mu $$

    $$ E(\xi) = \frac{\varphi'(0)}{i} = \mu $$

2.  **求二阶导数**：


    $$ \varphi''(t) = -\sigma^2 \varphi(t) + (i\mu - \sigma^2 t)^2 \varphi(t) $$

    $$ \varphi''(0) = -\sigma^2 + (i\mu)^2 = -\sigma^2 - \mu^2 $$

    $$ E(\xi^2) = \frac{\varphi''(0)}{i^2} = \frac{-\sigma^2 - \mu^2}{-1} = \sigma^2 + \mu^2 $$

3.  **计算方差**：


    $$ D(\xi) = E(\xi^2) - [E(\xi)]^2 = \sigma^2 + \mu^2 - \mu^2 = \sigma^2 $$

!!! note "考查思路"

    考查特征函数与矩的关系（性质 5）。

!!! abstract "要点重点"

    - **矩公式**：$f^{(k)}(0) = i^k E(\xi^k)$
    - 通过求导在 $t=0$ 处的值来获取矩，避免复杂的积分运算

---

### 应用题 2：独立正态变量和的分布

**题目内容**：
设 $\xi_j (j=1, 2, \dots, n)$ 是相互独立的正态随机变量，$\xi_j \sim N(a_j, \sigma_j^2)$。试求 $\xi = \sum_{j=1}^{n} \xi_j$ 的分布。

**答案/解答**：

**解**：

利用特征函数性质 4 推广到 $n$ 个独立变量：

$$ f_{\xi}(t) = \prod_{j=1}^{n} f_{\xi_j}(t) = \prod_{j=1}^{n} e^{ia_j t - \frac{1}{2}\sigma_j^2 t^2} = e^{i(\sum a_j)t - \frac{1}{2}(\sum \sigma_j^2)t^2} $$

故 $\xi$ 服从正态分布 $N\left( \sum_{j=1}^{n} a_j, \sum_{j=1}^{n} \sigma_j^2 \right)$。

!!! note "考查思路"

    考查独立随机变量和的特征函数性质及正态分布的可加性推广。

!!! abstract "要点重点"

    - **独立和的特征函数 = 特征函数的乘积**
    - 正态分布的和仍为正态分布

---

### 应用题 3：证明二项分布收敛于正态分布（棣莫弗 - 拉普拉斯定理）

**题目内容**：
在 $n$ 重贝努里实验中，事件 $A$ 每次出现的概率为 $p (0<p<1)$，$\mu_n$ 为 $n$ 次试验中事件 $A$ 出现的次数。证明当 $n \to \infty$ 时，标准化后的 $\mu_n$ 收敛于标准正态分布。即证明：

$$ \lim_{n \to \infty} P\left\{ \frac{\mu_n - np}{\sqrt{npq}} < x \right\} = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{x} e^{-\frac{t^2}{2}} dt $$

**答案/解答**：

**证明思路**：

1.  $\mu_n$ 服从二项分布 $b(n, p)$，可看作 $n$ 个独立的 0-1 分布变量之和。
2.  设 $\xi_k$ 为第 $k$ 次试验指示变量，$E(\xi_k)=p, D(\xi_k)=pq$。
3.  考虑标准化变量 $\eta_n = \frac{\sum \xi_k - np}{\sqrt{npq}}$。
4.  计算 $\eta_n$ 的特征函数。利用二项分布特征函数 $(pe^{it} + q)^n$ 及泰勒展开。
5.  当 $n \to \infty$ 时，$\eta_n$ 的特征函数收敛于 $e^{-\frac{t^2}{2}}$（标准正态分布的特征函数）。
6.  由连续性定理，分布函数收敛于标准正态分布函数。

!!! note "考查思路"

    考查特征函数在证明极限定理（中心极限定理特例）中的应用。

!!! abstract "要点重点"

    - **特征函数收敛 ⇒ 分布函数收敛**（连续性定理）
    - 泰勒展开在特征函数极限分析中的作用
    - **标准化处理**：减去均值，除以标准差

---

### 应用题 4：泊松分布收敛于正态分布

**题目内容**：
简述泊松分布收敛于正态分布的结论。

**答案/解答**：

**结论**：

若 $\xi_\lambda$ 服从泊松分布 $P(\lambda)$，当 $\lambda \to \infty$ 时，标准化变量 $\frac{\xi_\lambda - \lambda}{\sqrt{\lambda}}$ 的分布收敛于标准正态分布 $N(0, 1)$。
即：

$$ \lim_{\lambda \to \infty} P\left\{ \frac{\xi_\lambda - \lambda}{\sqrt{\lambda}} < x \right\} = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{x} e^{-\frac{t^2}{2}} dt $$

!!! note "考查思路"

    考查另一类中心极限定理的应用场景。

!!! abstract "要点重点"

    - 泊松分布参数 $\lambda$ 很大时，可用正态分布近似
    - 同样基于特征函数的收敛性证明

---

## 四、核心公式速查表

| 分布          | 记号             | 特征函数 $f(t)$                              |
| ------------- | ---------------- | -------------------------------------------- |
| 退化分布      | 定值 $c$         | $e^{itc}$                                    |
| 二项分布      | $b(n, p)$        | $(pe^{it} + q)^n$                            |
| 泊松分布      | $P(\lambda)$     | $e^{\lambda(e^{it} - 1)}$                    |
| $\Gamma$ 分布 | $G(\lambda, r)$  | $\left( 1 - \frac{it}{\lambda} \right)^{-r}$ |
| 正态分布      | $N(a, \sigma^2)$ | $e^{iat - \frac{1}{2}\sigma^2 t^2}$          |
| 标准正态      | $N(0, 1)$        | $e^{-\frac{t^2}{2}}$                         |
