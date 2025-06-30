# 多商品网络流问题

这一讲记录一下自己复习多商品网络流的经历。

我们先进入问题。

## 问题描述

给定一个有向网络 (Directed Network)，给定每个边的容量 (Capacity) $u$, 以及每个边的成本 $c$.

给定一个集合 $K$，表示 $k$ 种不同的商品 (Community)，每个商品 $i  \in K$ 用一个三元组来表示： $(s_i, t_i, d_i)$，分别表示 source, sink, demand，即商品的出发地、结束地，以及需求总量。

对于每一个商品，你需要找到一个可行的流，同时满足联合容量约束 (Joint Capacity Constraints)。

我们用数学语言对**问题约束和变量**进行描述。


我们记 $f_i(v,w)$ 是商品 $i$ 在边 $(v,w)$ 上的流量。

$$
\sum_w f_i(v,w) - \sum_w f_i(w,v) = \begin{cases}
0 & \text{if } v \neq s \text{ and } v \neq t \\
d_i & \text{if } v = s \\
-d_i & \text{if } v = t
\end{cases} \quad \forall v \in V, i \in K
$$

$$\sum_{i \in K} f_i(v,w) \le u(v,w) \quad \forall (v,w) \in E$$

$$f_i(v,w) \ge 0 \quad \forall (v,w) \in E$$

我们在这里分析一下，这个问题和单商品不同，每个商品的start可能不同，也就是在这个图里，每个节点都可能成为某个商品的起点/终点。

- 单商品网络流：$m$ variables, $m+n$ constraints，其中 $m$ 为边的数量，$n$ 为节点的数量。
- 多商品网络流：$km$ variables, $kn+m$ constraints，$km$ non-negativity constraints，其中 $m$ 为边的数量，$n$ 为节点的数量。

现在我们需要探讨一下可能的目标函数（决策目标）：

1. 给定边成本，找到一个可行的流，使得最小化 $\sum_i \sum_{vw} c_{v,w} f_i(v,w)$
2. 没有给定需求，最大化总流量；
3. 没有给定需求，最小化总成本；
4. 至少send $z \%$ 的需求，要最大化 $z$ （Concurrent flow）