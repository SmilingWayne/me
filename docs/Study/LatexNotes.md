## 向量篇：


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

## 字母篇

=== "小写 Part I"

    $$\alpha \hspace{9pt} \beta \hspace{9pt} \gamma \hspace{9pt} \delta \hspace{9pt} \sigma \hspace{9pt} \epsilon \hspace{9pt} \varepsilon \hspace{9pt} \zeta \hspace{9pt} \eta \hspace{9pt} \theta \hspace{9pt} \iota  \hspace{9pt} \kappa \hspace{9pt} \lambda$$

    ```
      $\alpha  \beta \gamma \delta

       \sigma \epsilon \varepsilon  \zeta  

       \eta  \theta  \iota   \kappa  \lambda$

    ```

=== "小写 Part II"

    $$\mu \hspace{9pt} \nu \hspace{9pt} \xi \hspace{9pt} \omicron \hspace{9pt} \rho \hspace{9pt} \sigma \hspace{9pt} \tau \hspace{9pt} \upsilon \hspace{9pt} \phi \hspace{9pt} \varphi \hspace{9pt} \chi  \hspace{9pt} \psi \hspace{9pt}$$

    ```
      $$\mu \hspace{9pt} \nu \hspace{9pt} \xi \hspace{9pt} \omicron
      
       \hspace{9pt} \rho \hspace{9pt} \sigma \hspace{9pt} \tau 

       \hspace{9pt} \upsilon \hspace{9pt} \phi \hspace{9pt} \varphi 

       \hspace{9pt} \chi  \hspace{9pt} \psi \hspace{9pt}$$
       
    ```
=== "大写 Part I"

    $$\Gamma \hspace{9pt} 
      \Delta \hspace{9pt} \Sigma \hspace{9pt} \hspace{9pt} 
      \Theta \hspace{9pt} \hspace{9pt} 
      \Lambda$$

    ```
      $$\Gamma \hspace{9pt} 
      
      \Delta \hspace{9pt} \Sigma \hspace{9pt} \hspace{9pt} \Zeta \hspace{9pt} \Eta \hspace{9pt} 
      
      \Theta \hspace{9pt} \Iota  \hspace{9pt} \Kappa \hspace{9pt} 
      
      \Lambda$$

    ```

=== "大写 Part II"

    $$ \Xi \hspace{9pt} \Sigma \hspace{9pt} \Upsilon \hspace{9pt} \Phi \hspace{9pt} \Psi \hspace{9pt}$$

    ```
      $$ \Xi \hspace{9pt} \Sigma \hspace{9pt} \Upsilon \hspace{9pt} 
      
      \Phi \hspace{9pt} \Psi \hspace{9pt}$$
       
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

-----

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