## 向量篇 | 矩阵篇 | 行列式篇 ：

!!! abstract "事实上已经有非常多人做过这个了，这里记录一些我反复查阅过的内容。"
    Some excellent links: 
    - [LaTeX-Math速查手册 by Emory Huang](https://latex.emoryhuang.cn/guide/)

===  "入门"

    $\begin{pmatrix} a_1 \\ a_2 \end{pmatrix}$

    ```Text
    \begin{pmatrix}

    a_1 \\ a_2
    
    \end{pmatrix}
    ```
=== "通用"
    
    $\begin{pmatrix} a_1 & a_2 \\ a_3 & a_4\end{pmatrix}$

    ```Text
    \begin{pmatrix} 
    a_1 & a_2 \\ 
    a_3 & a_4
    \end{pmatrix}
    ```
=== "进阶"

    $$
    \begin{pmatrix}
     a_{11} & \cdots & a_{1n} \\ 
      \vdots & \ddots & \vdots \\ 
      a_{n1} & \cdots & a_{nn}  
    \end{pmatrix}
    $$

    ```Text

    $$
    \begin{pmatrix}
     a_{11} & \cdots & a_{1n} \\ 
      \vdots & \ddots & \vdots \\ 
      a_{n1} & \cdots & a_{nn}  
    \end{pmatrix}
    $$

    ```
=== "行列式"

    $$
    \begin{vmatrix}
     a_{11} & \cdots & a_{1n} \\ 
      \vdots & \ddots & \vdots \\ 
      a_{n1} & \cdots & a_{nn}  
    \end{vmatrix}
    $$

    ```Text

    $$
    \begin{vmatrix}
     a_{11} & \cdots & a_{1n} \\ 
      \vdots & \ddots & \vdots \\ 
      a_{n1} & \cdots & a_{nn}  
    \end{vmatrix}
    $$

    ```
=== "矩阵"

    $$
    \begin{bmatrix}
     a_{11} & \cdots & a_{1n} \\ 
      \vdots & \ddots & \vdots \\ 
      a_{n1} & \cdots & a_{nn}  
    \end{bmatrix}
    $$

    ```Text

    $$
    \begin{bmatrix}
     a_{11} & \cdots & a_{1n} \\ 
      \vdots & \ddots & \vdots \\ 
      a_{n1} & \cdots & a_{nn}  
    \end{bmatrix}
    $$

    ```
=== "画表格"

    $$
    \def\arraystretch{2}
    \begin{array}{c:c|c}
        a & \beta + \gamma & c \cr \hline
        d & e & f \cr
        \hdashline
        g & h & i
    \end{array}
    $$

    ```LaTeX
    $$
    \def\arraystretch{2}
    \begin{array}{c:c|c}
        a & \beta + \gamma & c \cr \hline
        d & e & f \cr
        \hdashline
        g & h & i
    \end{array}
    % 这里是缩进敏感的
    $$

    ```

## 集合操作与基础符号

|    拼写    |    展示    |       拼写       |       展示       |    拼写     |    展示     |   拼写    |   展示    |
| :--------: | :--------: | :--------------: | :--------------: | :---------: | :---------: | :-------: | :-------: |
|   `\geq`   |   $\geq$   |      `\leq`      |      $\leq$      |   `\neq`    |   $\neq$    | `\forall` | $\forall$ |
|   `\cup`   |   $\cup$   |      `\cap`      |      $\cap$      |   `\land`   |   $\land$   |  `\lor`   |  $\lor$   |
|   `\neg`   |   $\neg$   | `A \setminus B`  | $A \setminus B$  | `\emptyset` | $\emptyset$ | `\subset` | $\subset$ |
|   `\mid`   |   $\mid$   | `A \subsetneq B` | $A \subsetneq B$ |  `\exist`   |  $\exist$   |  `\And`   |  $\And$   |
| `\because` | $\because$ |   `\therefore`   |   $\therefore$   |  `\bar{t}`  |  $\bar{t}$  |  `\bot`   |  $\bot$   |



## 希腊字母

|    拼写     |    展示     |    拼写     |    展示     |   拼写    |   展示    |     拼写      |     展示      |
| :---------: | :---------: | :---------: | :---------: | :-------: | :-------: | :-----------: | :-----------: |
|  `\alpha`   |  $\alpha$   |   `\rho`    |   $\rho$    |  `\iota`  |  $\iota$  |   `\Delta`    |   $\Delta$    |
|   `\beta`   |   $\beta$   |  `\sigma`   |  $\sigma$   | `\kappa`  | $\kappa$  |   `\Theta`    |   $\Theta$    |
|  `\gamma`   |  $\gamma$   | `\varsigma` | $\varsigma$ | `\lambda` | $\lambda$ |   `\Lambda`   |   $\Lambda$   |
|  `\delta`   |  $\delta$   |   `\tau`    |   $\tau$    |   `\mu`   |   $\mu$   |     `\Xi`     |     $\Xi$     |
| `\epsilon`  | $\epsilon$  | `\upsilon`  | $\upsilon$  |   `\mu`   |   $\mu$   |   `\Sigma`    |   $\Sigma$    |
|   `\zeta`   |   $\zeta$   |   `\chi`    |   $\chi$    |   `\nu`   |   $\nu$   |  `\Upsilon`   |  $\Upsilon$   |
|   `\eta`    |   $\eta$    |   `\psi`    |   $\psi$    |   `\xi`   |   $\xi$   |    `\Phi`     |    $\Phi$     |
|  `\theta`   |  $\theta$   |  `\omega`   |  $\omega$   |   `\pi`   |   $\pi$   |    `\Psi`     |    $\Psi$     |
| `\vartheta` | $\vartheta$ |  `\Gamma`   |  $\Gamma$   | `\Omega`  | $\Omega$  |  `\varOmega`  |  $\varOmega$  |
|  `\varPsi`  |  $\varPsi$  |  `\varPhi`  |  $\varPhi$  |   `\Pi`   |   $\Pi$   | `\varepsilon` | $\varepsilon$ |




## 奇异字母与英文字体
### \mathbb{ } 

- Black Board Bold 一般用于表示数学和物理学中的向量或集合的符号

```LaTeX
$\mathbb{ABCDEFGHIJKLMNOPQRSTUVWXYZ}$
$\mathbb{abcdefghijklmnopqrstuvwxyz}$
```

$\mathbb{ABCDEFGHIJKLMNOPQRSTUVWXYZ}$
$\mathbb{abcdefghijklmnopqrstuvwxyz}$
$\mathbb{1234}$

----

### \mathbf{ }

- 正粗体

```LaTeX
$\mathbf{ABCDEFGHIJKLMNOPQRSTUVWXYZ}$
$\mathbf{abcdefghijklmnopqrstuvwxyz}$
$\mathbf{0123456789}$
```

$\mathbf{ABCDEFGHIJKLMNOPQRSTUVWXYZ}$
$\mathbf{abcdefghijklmnopqrstuvwxyz}$
$\mathbf{0123456789}$

----

### \mathit{ }

- 斜体数字


```LaTeX
$\mathit{ABCDEFGHIJKLMNOPQRSTUVWXYZ}$
$\mathit{abcdefghijklmnopqrstuvwxyz}$
$\mathit{0123456789}$
```

$\mathit{ABCDEFGHIJKLMNOPQRSTUVWXYZ}$
$\mathit{abcdefghijklmnopqrstuvwxyz}$
$\mathit{0123456789}$



---

### \mathcal{ }

- 书法字体（**仅限大写**），用于方案识别，密码学概念；


```LaTeX
$\mathcal{ABCDEFGHIJKLMNOPQRSTUVWXYZ}$
```
$\mathcal{ABCDEFGHIJKLMNOPQRSTUVWXYZ}$


----

### \mathscr{ }

- 花体字，常用大写。

```LaTeX
$\mathscr{ABCDEFGHIJKLMNOPQRSTUVWXYZ}$
$\mathscr{abcdefghijklmnopqrstuvwxyz}$
$\mathscr{ 1234567890}$
```

$\mathscr{ABCDEFGHIJKLMNOPQRSTUVWXYZ}$
$\mathscr{abcdefghijklmnopqrstuvwxyz}$
$\mathscr{ 1234567890}$

### \mathfrak{ }

- 哥特式字体

$\mathfrak{ABCDEFGHIJKLMNOPQRSTUVWXYZ}$

$\mathfrak{1234567890}$

$\mathfrak{abcdefghijklmnopqrstuvwxyz}$

```LaTeX
$\mathfrak{ABCDEFGHIJKLMNOPQRSTUVWXYZ}$
$\mathfrak{1234567890}$
$\mathfrak{abcdefghijklmnopqrstuvwxyz}$
```


### \mathtt{ }

- 等宽字体

$\mathtt{ABCDEFGHIJKLMNOPQRSTUVWXYZ}$
$\mathtt{abcdefghijklmnopqrstuvwxyz}$
$\mathtt{ 1234567890}$

```LaTeX
$\mathtt{ABCDEFGHIJKLMNOPQRSTUVWXYZ}$
$\mathtt{abcdefghijklmnopqrstuvwxyz}$
$\mathtt{ 1234567890}$
```

## 杂七杂八

=== "大括号"

    $$\mathop{\max} \left\{ \frac{pV}{nrT} \right\}$$

    ``` LaTeX 
    $$\mathop{\max} \left\{ \frac{pV}{nrT} \right\}$$
    ```

=== "在min/max的正下方打出下标"
  
    $$\mathop{\arg\min}\limits_{\theta} \hspace{8pt} \mathop{\min}\limits_{\theta}$$

    ``` LaTeX

    $\mathop{\arg\min}\limits_{\theta}$

    $\mathop{\min}\limits_{\theta}$

    ```

=== "累乘符号"
    $$\prod \limits_{i=0}^n$$

    ``` LaTeX
    $\prod \limits_{i=0}^n$
    ```
=== "在求和符号正上方和正下方加字母"
  
    $$\sum \limits_{i=1}^{n}$$

    ```LaTeX
    $\sum \limits_{i=1}^{n}$
    ```
=== "求和符号下重叠"
  
    $$\sum_{\substack{0<i<m\cr 0<j<n}}$$

    ```LaTeX
    $\sum_{\substack{0<i<m\cr 0<j<n}}$
    ```

------

=== "在箭头正上方和正下方加字符"

    $$A\stackrel{r/c/}{\rightarrow}B$$

    ```LaTeX
    $A\stackrel{r/c/}{\rightarrow}B$
    ```

=== "约束条件的大括号"

    $$s.t \hspace{4pt} \left\{ \begin{aligned} \sum \limits^{n}_{j=1} x_{ij} \leq a_i , i = 1,2,..,m \\ \sum \limits^{n}_{i=1} x_{ij} = b_j , j = 1,2,..,n     \end{aligned}  \right. $$

    ``` LaTeX
    $$
    s.t. 
    \hspace{4pt} 
    \left\{ 
    \begin{aligned} \sum \limits^{n}_{j=1} x_{ij} \leq a_i , i = 1,2,..,m \\
    \sum \limits^{n}_{i=1} x_{ij} = b_j , j = 1,2,..,n 
    \end{aligned} 
    \right. 
    $$
    ```

=== "🌊 波浪号 | 上波浪 | 对于任意"

    $$\sim  \hspace{10pt}  \tilde{A}  \hspace{10pt} \forall$$

    ```LaTeX
    $$ \sim  \hspace{10pt}  \tilde{A}  \hspace{10pt} \forall$$
    ```

=== "另一种大括号"

    $$f(n)=\begin{dcases} 1 & n = 1 \cr \sum_{i=1}^{n-1} f(i) & \text{Otherwise.}\end{dcases}$$

    ```KaTeX
    $$f(n)=\begin{dcases} 1 & n = 1 \cr \sum_{i=1}^{n-1} f(i) & \text{Otherwise.}\end{dcases}$$
    ```


-----

=== "偏导符号"

    $$\partial y$$
    
    ```LaTeX
    $$ \partial y $$
    ```

=== "积分符号"

    $$\int \limits^{a}_{b}$$

    ```LaTeX
    $$\int \limits^{a}_{b}$$
    ```

=== "范式符号"

    $$\Vert x - y \Vert$$

    ```LaTeX
    $$ \Vert x - y \Vert $$
    ```

=== "梯度符号"

    $$\nabla$$

    ```LaTeX
    $$ \nabla $$
    ```

=== "加注释"

    $$\tag{2.1}E = mc^2$$

    ```LaTeX
    $$\tag{(2.1)}E = mc^2$$
    ```

=== "实数"

    $$\Re \hspace{4pt} \real \hspace{4pt}  \reals \hspace{4pt}  \Reals \hspace{4pt}  \Z$$

    ```LaTeX
    $$\Re \real \reals \Reals \Z$$
    ```

=== "加方框"

    $$\boxed{\pi=\dfrac{c}{d}}$$

    ```LaTeX
    $$\boxed{\pi=\dfrac{c}{d}}$$
    ```

=== "上 / 下总括号"

    $$\overbrace{x+⋯+x}^{n\text{ times}} \hspace{6pt} \underbrace{x+⋯+x}_{n\text{ times}}$$

    ```LaTeX
    $$\overbrace{x+⋯+x}^{n\text{ times}} \hspace{6pt} \underbrace{x+⋯+x}_{n\text{ times}}$$
    ```


-------


=== "表示均值的那个拔：bar"

    $$\bar{A}$$

    ```LaTeX
    $$\bar{A}$$
    ```

=== "表示回归中的期望值的：hat"

    $$\hat{A}$$
    
    ```LaTeX
    $$\hat{A}$$
    ```

=== "粗体"

    $$\textbf{\alpha}$$

    ```LaTeX
    $$\textbf{\alpha}$$
    ```


```LaTeX
$$\text{价格}  \hspace{90pt} \text{容积} \hspace{90pt}  \text{美观} \hspace{50cm} \\[2ex]  B_{1}^{(3)} = \begin{pmatrix}
     1 & 1/5 & 1/8 \\ 
      5 & 1 & 1/4 \\ 
    8 & 4 & 1
    \end{pmatrix} \hspace{5pt} 
 B_{5}^{(3)} = \begin{pmatrix}
     1 & 6 & 4 \\ 
      1/6 & 1 & 1/3 \\ 
    1/4 & 3 & 1
    \end{pmatrix} \hspace{5pt} 
    B_{9}^{(3)} = \begin{pmatrix}
     1 & 1/7 & 3 \\ 
      7 & 1 & 9 \\ 
    1/3 & 1/9 & 1
    \end{pmatrix} \hspace{20cm}$$


$$\text{冷冻}  \hspace{90pt} \text{功率} \hspace{90pt} \text{体积} \hspace{50cm}\\[2ex] B_{2}^{(3)} = \begin{pmatrix}
     1 & 2 & 9 \\ 
      1/2 & 1 & 7 \\ 
    1/9 & 1/7 & 1
    \end{pmatrix} \hspace{5pt} 
B_{6}^{(3)} = \begin{pmatrix}
     1 & 1/8 & 1/4 \\ 
      8 & 1 & 5 \\ 
    4 & 1/5 & 1
    \end{pmatrix}\hspace{5pt} 
B_{10}^{(3)} = \begin{pmatrix}
     1 & 1/7 & 1/2 \\ 
      7 & 1 & 4 \\ 
    2 & 1/4 & 1
    \end{pmatrix} \hspace{50cm}$$


$$\text{快速}  \hspace{90pt} \text{分贝} \hspace{90pt} \text{售后} \hspace{50cm}\\[2ex]  B_{3}^{(3)} = \begin{pmatrix} 
 1 & 5 & 7 \\ 
 1/5 & 1 & 3 \\
 1/7 & 1/3 & 1 
 \end{pmatrix} \hspace{5pt}
B_{7}^{(3)} = \begin{pmatrix} 
  1 & 5 & 8 \\ 
  1/5 & 1 & 4 \\ 
  1/8 & 1/4 & 1 \end{pmatrix}\hspace{5pt}
B_{11}^{(3)} = \begin{pmatrix}
1 & 3 & 9 \\
 1/3 & 1 & 5 \\ 
1/9 & 1/5 & 1
\end{pmatrix} \hspace{50cm}$$

$$\text{制热} \hspace{90pt}  \text{清洗} \hspace{50cm}  \\[2ex]  B_{4}^{(3)} = \begin{pmatrix}
     1 & 1/5 & 4 \\ 
      5 & 1 & 8 \\ 
    1/4 & 1/8 & 1
    \end{pmatrix} \hspace{5pt} 
B_{8}^{(3)} = \begin{pmatrix}
     1 & 4 & 1/5 \\ 
      1/4 & 1 & 1/8 \\ 
    5 & 8 & 1
    \end{pmatrix}\hspace{50cm}$$
```

