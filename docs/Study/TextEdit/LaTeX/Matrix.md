# 矩阵多行对齐

- 11个矩阵，上下对齐地摆放，空缺的地方留白
- KaTeX控制空白的地方居中：在行末尾加上`\hspace{50cm}`使得这一行左对齐。

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