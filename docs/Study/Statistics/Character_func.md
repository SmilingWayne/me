---
title: 特征函数
slug: study/statistics/character-func
summary: 系统整理特征函数的定义、5 大性质、逆转公式、再生性分布及 4 大应用，涵盖常见分布的特征函数公式与中心极限定理证明思路。
---

# 第 5 章 特征函数

!!! example "本章核心"

    特征函数是分布函数的傅里叶 - 斯蒂尔切斯变换，始终存在且唯一确定分布。通过**独立和的乘积性**将卷积运算转化为乘法，通过**求导**获取矩，是证明极限定理的核心工具。

---

## 5.1 特征函数的定义

### 1. 复随机变量

- **定义**：若 $\xi$ 与 $\eta$ 是概率空间上的实值随机变量，则称 $\zeta = \xi + i\eta$ 为**复随机变量**。
- **数学期望**：$E(\zeta) = E(\xi) + iE(\eta)$。
- **独立性**：若二维向量 $(\xi_1, \eta_1)$ 与 $(\xi_2, \eta_2)$ 独立，则复随机变量 $\zeta_1 = \xi_1 + i\eta_1$ 与 $\zeta_2 = \xi_2 + i\eta_2$ 独立。
- **性质**：若 $\zeta_1, \dots, \zeta_n$ 相互独立，则 $E(\zeta_1 \cdots \zeta_n) = E(\zeta_1) \cdots E(\zeta_n)$。

### 2. 特征函数 (Characteristic Function)

- **定义**：设随机变量 $\xi$ 的分布函数为 $F_\xi(x)$，则称函数

  $$
  \varphi_\xi(t) = E(e^{it\xi}) = \int_{-\infty}^{+\infty} e^{itx} \, \mathrm{d}F_\xi(x), \quad t \in \mathbb{R}
  $$

  为 $\xi$ 的**特征函数**。

- **性质**：
  1.  特征函数是实变量 $t$ 的复值函数。
  2.  由于 $|e^{itx}| = 1$，积分对一切实数 $t$ 均收敛（即**特征函数始终存在**）。
  3.  特征函数由分布函数唯一决定，反之亦然（见 5.3 节）。

- **常见形式的特征函数**：

  - **离散型**（分布律 $P\{\xi = x_j\} = p_j$）：

    $$
    \varphi_\xi(t) = \sum_{j} p_j e^{itx_j}
    $$

  - **连续型**（概率密度为 $p(x)$）：

    $$
    \varphi_\xi(t) = \int_{-\infty}^{+\infty} e^{itx} p(x) \, \mathrm{d}x
    $$

    此时特征函数是密度函数 $p(x)$ 的**傅里叶变换**。

### 3. 重要分布的特征函数

- **退化分布** $I(x-c)$（即 $P\{\xi=c\}=1$）：

  $$
  \varphi(t) = e^{itc}
  $$

- **泊松分布** $P(\lambda)$：

  $$
  \varphi(t) = e^{\lambda(e^{it} - 1)}
  $$

- **$\Gamma$ 分布** $G(\lambda, r)$：

  $$
  \varphi(t) = \left(1 - \frac{it}{\lambda}\right)^{-r}
  $$

- **正态分布** $N(a, \sigma^2)$：

  $$
  \varphi(t) = e^{iat - \frac{1}{2}\sigma^2 t^2}
  $$

  - 特别地，标准正态分布 $N(0, 1)$ 的特征函数为 $e^{-\frac{1}{2}t^2}$。

---

## 5.2 特征函数的性质

### 1. 基本性质

- **有界性与归一性**：
  1.  $\varphi(0) = 1$。
  2.  $|\varphi(t)| \le 1, \quad \forall t \in \mathbb{R}$。
  3.  $\varphi(-t) = \overline{\varphi(t)}$（共轭对称性）。

- **一致连续性**：$\varphi(t)$ 在 $(-\infty, +\infty)$ 上一致连续。

- **非负定性**（本质性质）：

  对于任意正整数 $n$，任意实数 $t_1, \dots, t_n$ 及复数 $\lambda_1, \dots, \lambda_n$，有

  $$
  \sum_{j=1}^n \sum_{k=1}^n \varphi(t_j - t_k) \lambda_j \overline{\lambda_k} \ge 0
  $$

### 2. 运算性质

- **独立和的特征函数**（核心性质）：

  若 $\xi_1, \dots, \xi_n$ 相互独立，则 $\eta = \sum_{k=1}^n \xi_k$ 的特征函数为各特征函数之积：

  $$
  \varphi_\eta(t) = \prod_{k=1}^n \varphi_{\xi_k}(t)
  $$

  - **意义**：将独立随机变量和的分布**卷积运算**转化为特征函数的**乘法运算**，极大简化了计算。

- **线性变换**：

  若 $\eta = a\xi + b$（$a, b$ 为常数），则

  $$
  \varphi_\eta(t) = e^{itb} \varphi_\xi(at)
  $$

### 3. 与矩的关系

- **矩的生成**：若 $\xi$ 的 $n$ 阶矩 $E(\xi^n)$ 存在，则 $\varphi_\xi(t)$ 可微分 $n$ 次，且

  $$
  \varphi_\xi^{(k)}(0) = i^k E(\xi^k), \quad k \le n
  $$

  即

  $$
  E(\xi^k) = \frac{\varphi_\xi^{(k)}(0)}{i^k}
  $$

- **泰勒展开**：若 $n$ 阶矩存在，特征函数可在 $t=0$ 处展开：

  $$
  \varphi_\xi(t) = 1 + \sum_{k=1}^n \frac{(it)^k}{k!} E(\xi^k) + o(t^n)
  $$

---

## 5.3 逆转公式与唯一性定理

### 1. 逆转公式 (Inversion Formula)

- **内容**：设分布函数 $F(x)$ 的特征函数为 $\varphi(t)$，若 $x_1, x_2$ 是 $F(x)$ 的连续点，则

  $$
  F(x_2) - F(x_1) = \lim_{T \to +\infty} \frac{1}{2\pi} \int_{-T}^{T} \frac{e^{-itx_1} - e^{-itx_2}}{it} \varphi(t) \, \mathrm{d}t
  $$

- **密度函数恢复**：若 $\int_{-\infty}^{+\infty} |\varphi(t)| \, \mathrm{d}t < \infty$，则分布函数 $F(x)$ 可导，其密度函数为

  $$
  p(x) = F'(x) = \frac{1}{2\pi} \int_{-\infty}^{+\infty} e^{-itx} \varphi(t) \, \mathrm{d}t
  $$

  此时密度函数与特征函数互为傅里叶变换对。

### 2. 唯一性定理 (Uniqueness Theorem)

- **内容**：分布函数由其特征函数**唯一决定**。
- **意义**：特征函数完全描述了随机变量的统计规律性。**两个随机变量同分布 $\iff$ 它们的特征函数相同**。

---

## 5.4 分布函数的再生性

### 1. 定义

若两个独立随机变量服从某类分布，其和也服从同类分布（参数可能变化），则称该类分布具有**再生性**。

### 2. 常见具有再生性的分布

- **二项分布**：

  若 $\xi_1 \sim b(n_1, p), \xi_2 \sim b(n_2, p)$ 且独立，则

  $$
  \xi_1 + \xi_2 \sim b(n_1 + n_2, p)
  $$

- **泊松分布**：

  若 $\xi_1 \sim \pi(\lambda_1), \xi_2 \sim \pi(\lambda_2)$ 且独立，则

  $$
  \xi_1 + \xi_2 \sim \pi(\lambda_1 + \lambda_2)
  $$

- **正态分布**：

  若 $\xi_1 \sim N(a_1, \sigma_1^2), \xi_2 \sim N(a_2, \sigma_2^2)$ 且独立，则

  $$
  \xi_1 + \xi_2 \sim N(a_1 + a_2, \sigma_1^2 + \sigma_2^2)
  $$

  - **推广**：有限个相互独立的正态变量的线性组合仍服从正态分布。

- **$\Gamma$ 分布**：

  若 $\xi_1 \sim G(\lambda, r_1), \xi_2 \sim G(\lambda, r_2)$ 且独立（注意尺度参数 $\lambda$ 需相同），则

  $$
  \xi_1 + \xi_2 \sim G(\lambda, r_1 + r_2)
  $$

### 3. 分布的分解问题（逆命题）

- **问题**：若两个独立随机变量之和服从某分布，这两个变量是否也服从该分布？
- **结论**：对于**正态分布**和**泊松分布**，该逆命题成立（Cramér 定理等）。

---

## 5.5 多元特征函数

### 1. 定义

- 设 $n$ 维随机向量 $\boldsymbol{\xi} = (\xi_1, \dots, \xi_n)$ 的分布函数为 $F(x_1, \dots, x_n)$，其特征函数定义为：

  $$
  \varphi(t_1, \dots, t_n) = E\left( \exp\left( i \sum_{k=1}^n t_k \xi_k \right) \right) = \int_{-\infty}^{+\infty} \cdots \int_{-\infty}^{+\infty} e^{i(t_1 x_1 + \dots + t_n x_n)} \, \mathrm{d}F(x_1, \dots, x_n)
  $$

### 2. 性质

- **边际特征函数**：

  $k$ 维边际分布的特征函数可通过令其余 $n-k$ 个变量为 0 得到。例如 $\xi_1$ 的特征函数为 $\varphi(t_1, 0, \dots, 0)$。

- **独立性充要条件**：

  随机变量 $\xi_1, \dots, \xi_n$ 相互独立的充要条件是联合特征函数等于边际特征函数之积：

  $$
  \varphi(t_1, \dots, t_n) = \prod_{k=1}^n \varphi_{\xi_k}(t_k)
  $$

- **随机向量独立性**：

  随机向量 $\boldsymbol{\xi}$ 与 $\boldsymbol{\eta}$ 独立的充要条件是联合特征函数可分离变量：

  $$
  \varphi_{\boldsymbol{\xi}, \boldsymbol{\eta}}(\mathbf{t}, \mathbf{u}) = \varphi_{\boldsymbol{\xi}}(\mathbf{t}) \cdot \varphi_{\boldsymbol{\eta}}(\mathbf{u})
  $$

### 3. 多元逆转公式

- 类似于一元情况，可通过多重积分从多元特征函数恢复联合分布函数。

---

## 5.6 特征函数的应用

### 1. 求数字特征

- 利用性质 $\varphi^{(k)}(0) = i^k E(\xi^k)$ 可直接求期望、方差及各阶矩，避免复杂的积分运算。

  - **例**：正态分布 $N(\mu, \sigma^2)$，$\varphi(t) = e^{i\mu t - \frac{1}{2}\sigma^2 t^2}$。
  - $\varphi'(0) = i\mu \Rightarrow E(\xi) = \mu$。
  - $\varphi''(0) = (i\mu)^2 - \sigma^2 = -\mu^2 - \sigma^2 \Rightarrow E(\xi^2) = \mu^2 + \sigma^2 \Rightarrow D(\xi) = \sigma^2$。

### 2. 求独立随机变量和的分布

- **步骤**：
  1.  写出各变量特征函数。
  2.  相乘得到和的特征函数。
  3.  识别该特征函数对应的分布（利用唯一性定理）。

- 此方法比卷积公式更简便，尤其适用于再生性分布。

### 3. 证明极限定理（中心极限定理）

- **连续性定理**：若特征函数列 $\{\varphi_n(t)\}$ 收敛于一个连续函数 $\varphi(t)$，则 $\varphi(t)$ 是某个分布函数的特征函数，且对应的分布函数列弱收敛。

- **二项分布收敛于正态分布**（De Moivre-Laplace 定理）：

  利用特征函数证明标准化后的二项分布变量特征函数收敛于 $e^{-\frac{1}{2}t^2}$（标准正态特征函数）。

- **泊松分布收敛于正态分布**：

  当 $\lambda \to \infty$ 时，标准化泊松变量的特征函数收敛于标准正态特征函数。

- **独立同分布中心极限定理** (Lindeberg-Levy)：

  若 $\xi_k$ i.i.d.，$E(\xi_k)=a, D(\xi_k)=\sigma^2$，则标准化和 $\frac{\sum \xi_k - na}{\sigma\sqrt{n}}$ 依分布收敛于 $N(0, 1)$。

---

## 重点与难点总结

!!! note "考点速记"

    1.  **核心定义**：特征函数是分布函数的傅里叶 - 斯蒂尔切斯变换，始终存在且唯一确定分布。
    2.  **关键性质**：
        - **独立和的乘积性**：$\varphi_{\sum \xi_i} = \prod \varphi_{\xi_i}$（解题最常用的性质）。
        - **矩的生成性**：通过求导获取矩。
        - **非负定性**：特征函数的本质特征（判定一个函数是否为特征函数的依据）。
    3.  **唯一性与逆转**：理解特征函数与分布函数的一一对应关系，这是利用特征函数研究分布极限理论的基础。
    4.  **再生性分布**：熟记二项、泊松、正态、$\Gamma$ 分布的独立和分布规律，这是计算题的高频考点。
    5.  **极限定理证明思路**：理解如何通过特征函数的收敛性（连续性定理）来证明分布函数的收敛性（中心极限定理的核心逻辑）。
    6.  **多元独立性**：联合特征函数可分解为边际特征函数之积是判断多维变量独立性的有力工具。
