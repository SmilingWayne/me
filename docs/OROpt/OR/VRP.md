# 车辆路径问题（VRP）及相关

## 建模篇 （set partitioning formulation）

- 记  $\mathcal{R}$ 表示所有可行的路径的下标集合。

- 记 $a_{i \ell}$ 是一个 0-1 Binary的系数，如果第 $i \in V$ 个节点属于第 $\ell \in  \mathcal{R}$ 个路径。

- 每个路径 $\ell \in  \mathcal{R}$ 有一个对应的成本 $c_{\ell}$

- 记 $\xi_{\ell}$ 是 0-1 Binary, 如果路径 $\ell \in \mathcal{R}$ 在最终解中。

由此可以构建基于集合分割的建模方式。


$$\begin{aligned}
\min & \quad \sum_{\ell \in \mathcal{R}} c_{\ell} \xi_{\ell} \\
\text{s.t.} & \quad 
\begin{cases}
\sum_{\ell \in \mathcal{R}} a_{i\ell} \xi_{\ell} = 1, \quad \forall i \in \mathcal{V}_c \\
\sum_{\ell \in \mathcal{R}} \xi_{\ell} = M \\
\xi_{\ell} \in \{0,1\}, \quad \forall \ell \in \mathcal{R}
\end{cases}
\end{aligned}$$

注意了，为什么这里没有去子环约束，是因为最开始的“可行路径的下标集合”已经约束了这个路径一定要是可行的（从depot到depot）。

这个建模的方法，很适合“分枝定价”去精确地求解车辆路径问题。这个解法的子问题就是生成一些可行的路径，加入到所有的可行路径中。而这个子问题本身是在求一个“资源限制情况下的最短路问题”。


!!! warning "2024.06.12 已标记为待补充 / 修订。"