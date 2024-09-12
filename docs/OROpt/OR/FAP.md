# 航班分配问题

$$\max \quad \sum_{l \in L} \sum_{k \in K} p_{lk} x_{lk}$$

参考梁哲老师的[公众号文章](https://mp.weixin.qq.com/s/m4KhLtzgwakYYi5ZG2MdRw)。时空网络模型、最大化利润。

$$\begin{aligned}
\begin{cases}
\begin{align}
\quad \sum_{k \in K} x_{lk} \leq 1 \quad \forall l \in L  \quad \\
\sum_{l \in L_{n^+}} x_{lk} + y_{n^+} - \sum_{l \in L_{n^-}} x_{lk} - y_{n^-} = 0 \quad \forall n \in N_k, \ \forall k \in K  \quad \\
\sum_{l \in L^P} x_{lk} + \sum_{n \in N_k^P} y_{n^+} \leq M_k \quad \forall k \in K  \quad \\
x_{lk} \in \{0, 1\} \quad \forall l \in L, \ \forall k \in K  \quad \\
y_{n^+}, y_{n^-} \geq 0 \quad \forall n \in N_k, \ \forall k \in K  \quad \\
\end{align}
\end{cases}
\end{aligned}$$

