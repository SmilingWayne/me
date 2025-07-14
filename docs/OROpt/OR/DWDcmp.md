# Danzig-Wolfe Decomposition: DW 分解

一种用来求解大规模线性规划问题 (Large Scale Linear Programming) 的算法。

推荐视频：[DW Decomposition(YouTube)](https://www.youtube.com/watch?v=IposxYVBUnY) ｜ [带分块的DW分解:例题](https://www.youtube.com/watch?v=wxz0NJvKZNM)；

我们依然看最简单的LP的问题描述：

\[
\begin{aligned}
\min  & c^{\top}x \\
\text{s.t.} & Ax = b, \\[-2pt]
& x \in X
\end{aligned}
\]


- \(X\subseteq\mathbb{R}^n\) 为一个多面体，所谓的 “easy constraints” 描述，是因为 $X$ 的限制（如单纯的界限、区间或网络流平衡）往往局部且易处理，可在子问题里独立优化；

- \(Ax = b\) 被视为 “complicating constraints”。

同时，DW分解离不开一个重要的数学定理：极点表示定理 (Extreme Point Representation Theroem):

!!! example "极点表示定理"

    对于 **有界 多面体**，所有可行点都能写成极点的凸组合（权重非负且和为 1）。

    设 $X \subseteq \mathbb{R}^{n}$ 是一个非空、有界的多面体，其全部极点构成集合
    
    \[
    \mathcal{V}(X) = \bigl\{\,x^{1},\,x^{2},\,\dots,\,x^{t}\bigr\}.
    \]

    则必有
    
    \[
    X = \operatorname{conv}\{x^1,\dots,x^t\} 
    = \Bigl\{\,\sum_{j=1}^{t}\lambda_j x_{j} \Bigm|
    \lambda_j\!\ge\!0, \sum_{j=1}^{t}\lambda_j = 1 \Bigr\}.
    \]

    你可以理解为，对于任意一个多面体内的**向量**，我们都可以用一种统一的、优美的方式（极点的凸组合）进行表达，而这个**被表示的向量**，就是我们大规模LP问题中的 $\mathbf{x}$。

我们充分利用极点表示定理，去重写原问题中的 $x$ 决策变量向量，就是：


\[
\begin{aligned}
z^{*} = \min_{\lambda} & \sum_{j=1}^{t} (c^{\top}x_{j})\,\lambda_{j} \\[4pt]
\text{s.t.} & \sum_{j=1}^{t} (A x_{j})\,\lambda_{j} = b, \\[2pt]
& \sum_{j=1}^{t} \lambda_{j} = 1, \\[2pt]
& \lambda_{j} \ge 0 \quad (j=1,\dots,t).
\end{aligned}
\]

这个变形就是DW- formulation，我们暂时叫他主问题（Master Problem）。重点在于把未知的决策变量 x 都转化成了极点的凸组合，考虑到极点已知了，我们真正的决策变量变成了　 $\lambda_j$ 。换句话讲，新的 formulation中任意一个可行解都对应原问题的一个可行解，其目标函数也是相同的：我们将目标函数和 $Ax=b$ 投影到 $\lambda$ 空间。


## 如何处理过多的极点

原问题的 X 是一个多面体，考虑到大规模问题会有很多的极向量，似乎上面这种变形是无用的：每一列 $(x_{j},\,c^{\top}x_{j},\,A x_{j})$ 对应一个极点，也称 **列**，列数 $t$ 常常巨大甚至无穷，因此不直接全部生成，而是……

1. **列生成 (Column Generation)**
    1. 先解一个含少量列的受限主问题 (RMP)。利用对偶信息在子问题（通常是以 $X$ 为可行域的优化模型）中寻找能改进目标的 **定价列**。
    2. 迭代加入新列直到无列具负 reduced-cost，主问题最优即原 LP 最优。

2. **定价（Pricing）**
    1. 将耦合难点集中在主问题的少量方程 ( $Ax=b$、$\sum\lambda=1$ ) 中；
    2. 子问题仅含“易约束” X，可并行或用专门算法高效解决；
    3. 在大规模或分块结构 LP（车辆路径、列车时刻、装箱等）中显著降低求解难度。

之所以叫前面的问题为主问题就是因为需要遍历所有的极点，而如果我们不计算所有的极点，而是仅仅利用一部分极点，那么得到的解还是可行的，只不过不一定是最优解，也就是说，提供了原问题的一个上界（Upper Bound），因此我们把这个**仅仅利用了一部分极点** (A small subset of extreme points) 的模型称为Restricted Master Problem (RMP)，重点是它不需要遍历所有的极点，因此我们的下标是一个索引的子集：


\[
\begin{aligned}
\bar z = 
\min_{\lambda} &\sum_{j\in I} (c^{\top}x_{j})\,\lambda_{j}\\[2pt]
\text{s.t.} &\sum_{j\in I}(A x_{j})\,\lambda_{j}=b \quad(\text{dual var } y  \rightarrow Ax_j)\\
              &\sum_{j\in I}\lambda_{j}=1 \quad(\text{dual var } \alpha \rightarrow 1)\\
              &\lambda_{j}\ge 0, j\in I,
\end{aligned}
\]

==其中 \(I\) 是已生成列（一部分极点的）索引集合== 。  

此时我们需要检查Reduced Cost是否 < 0，这样我们就需要找最小的 Reduced Cost，如果发现最小的Reduced Cost < 0 的话，那么说明需要找新的列加进去，否则的话，就说明已经找到了最优解。

那么我们加进去的列是什么呢？加进去的列**就是一个极点**！我们之所以是RMP就是因为加进去的极点不充分，而我们现在能够找到一个对解有提升的极点了！

这里需要引入我们的子问题，或者叫做 Column Generation Subproblem (CGSP) ，这个子问题的目的是找到最小的Reduced Cost，其决策变量是一个并且看这个Reduced Cost 是否 $< 0$，如果是，那么这个最优解对应的决策变量就对应了一个新的列，我们把它加入进主问题就（可能）改进主问题的求解质量了；反之，如果 $\geq 0$，说明所有的检验数都非负，那么原问题就最优了。

我们的 Column Generation Subproblem (CGSP) 就可以表示为：

\[
    \hat z =
\min_{j\in 1,..,t}\bigl\{c^{\top}x_j - y^{\top}A x_j - \alpha \bigr\}=-\alpha +\min_{x\in X}\bigl\{(c^{\top}-y^{\top}A)x\bigr\}.
\]

\[
    \text{若}\hat z < 0 \Longrightarrow \text{找到改进列 } x^{\text{new}} \text{ 并加入 } I.
\]

这里的 $\alpha$ 对应第二组约束的对偶变量。

---

我们同样可以用 $\hat z$ 来衡量生成列的 Bound。考虑到主问题中 $x \in X: Ax = b$，注意这里对偶问题决策变量实际就是主问题的一个向量（备选的极点向量），所以 $y^TAx - c^Tx + \alpha \leq \hat z$ 替换 $Ax = b$，即为 $y^Tb - c^Tx + \alpha \leq \hat z$

然后:

$c^Tx \geq y^Tb + \alpha - \hat z$

**可以发现 $y^Tb + \alpha$ 偏偏恰好是 RMP 问题对偶问题的最优解。**

也就是说： $c^Tx \geq \bar z - \hat z$，其中 $\bar z$ 是RMP问题的最优解。这个式子**对于原问题任意一个可行的** $x$ 都是成立的。

进一步地，$c^Tx$ 是原问题的目标函数，也就是说，RMP 问题最优解和 CGSP 问题最优解的差，表示了原问题目标函数优化的幅度。 也就是说 $z^{*} \geq  \bar z - \hat z$，其中 $z^{*}$ 是原问题的最优解。考虑到 RMP 问题是原问题的一个约束情况下的解，所以我们有：

$\bar z \geq z^{*} \geq  \bar z - \hat z$

这是一个很重要的Bound，用来表示每次DW分解每次迭代之后距离最优目标函数还有多远 (How far we are to the optimal).

## 参考笔记

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202507150148475.png)

!!! quote "来自GPT：核心逻辑一句话"

    在每轮迭代里，RMP 给出“当前组合最好怎么配”，CGSP 负责问“还存不存在一列能让目标再降一点？”——二者循环，直到回答是“没有”，这时 列生成 完成，得到原 LP 的最优解与严格界。