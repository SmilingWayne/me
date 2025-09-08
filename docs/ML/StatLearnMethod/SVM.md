# 支持向量机 (SVM)


SVM是一种功能强大且用途广泛的==监督学习==模型，主要用于**分类**问题，也可以用于回归（SVR）。

**核心设计目的**：对于一个二分类问题，如果数据是线性可分的，那么会有无数条直线（或高维平面）可以将两类数据分开。SVM的目的就是找到那条**最优**的分隔超平面。

**什么是最优？**
:   SVM认为，最优的超平面是那个能够以**最大间隔 (Maximum Margin)** 将两类样本分开的平面。这个间隔指的是超平面与两边最近的样本点之间的距离。这些离超平面最近的、用于定义间隔的样本点，就被称为**支持向量 (Support Vectors)**。

**它解决了什么问题？**
1.  **最优分类边界问题**：相较于其他模型（如逻辑回归）可能找到任意一个分类边界，SVM通过最大化间隔，找到了一个理论上泛化能力更强的边界，因为它对噪声的容忍度更高（边界离所有点都尽可能远）。
2.  **非线性分类问题**：通过引入“核技巧 (Kernel Trick)”，SVM能够非常高效地处理线性不可分的数据，实现复杂的非线性分类。

#### 2. 算法流程与数学原理

我们从最简单的情况开始，逐步构建到完整的SVM。假设有训练数据集 $D = \{(\mathbf{x}_1, y_1), (\mathbf{x}_2, y_2), ..., (\mathbf{x}_n, y_n)\}$，其中 $\mathbf{x}_i \in \mathbb{R}^m$ 是一个 $m$ 维的特征向量， $y_i \in \{-1, 1\}$ 是类别标签。

##### A. 线性可分SVM (硬间隔SVM)

这是最理想的情况，数据完全可以用一个超平面分开。

**1. 定义超平面**
一个超平面在特征空间中可以用以下方程描述：
$$
\mathbf{w}^T \mathbf{x} + b = 0
$$
-   $\mathbf{w}$: $m \times 1$ 的法向量，决定了超平面的方向。
-   $b$: $1 \times 1$ 的标量（偏置项），决定了超平面与原点的距离。

**2. 找到最大间隔**
-   **函数间隔**：对于一个样本 $(\mathbf{x}_i, y_i)$，它到超平面的函数间隔是 $\hat{\gamma}_i = y_i(\mathbf{w}^T \mathbf{x}_i + b)$。我们希望所有点的函数间隔都大于0。
-   **几何间隔**：点 $\mathbf{x}_i$ 到超平面的真实几何距离是 $\gamma_i = \frac{y_i(\mathbf{w}^T \mathbf{x}_i + b)}{||\mathbf{w}||}$。
-   我们的目标是最大化这个几何间隔。为了简化问题，我们可以对 $\mathbf{w}$ 和 $b$进行缩放，使得在支持向量 $\mathbf{x}_{sv}$ 上，函数间隔 $| \mathbf{w}^T \mathbf{x}_{sv} + b | = 1$。
-   这样，最大化几何间隔 $2\gamma = \frac{2}{||\mathbf{w}||}$ 就等价于 **最小化 $||\mathbf{w}||$**。为了方便求导，我们通常最小化 $\frac{1}{2}||\mathbf{w}||^2$。

**3. 构建优化问题 (Primal Problem)**
我们的目标是最小化 $\frac{1}{2}||\mathbf{w}||^2$，同时要满足所有点都被正确分类，并且函数间隔至少为1。这构成了一个带约束的凸优化问题：

$$
\begin{aligned}
\min_{\mathbf{w}, b} \quad & \frac{1}{2}||\mathbf{w}||^2 \\
\text{s.t.} \quad & y_i(\mathbf{w}^T \mathbf{x}_i + b) \ge 1, \quad i = 1, 2, ..., n
\end{aligned}
$$

##### B. 线性SVM (软间隔SVM)

现实世界的数据往往有噪声或重叠，无法用硬间隔完美分开。软间隔SVM允许一些样本“犯错”，即允许它们出现在间隔内部，甚至是错误的一侧。

**1. 引入松弛变量**
我们为每个样本引入一个松弛变量 $\xi_i \ge 0$。
-   如果 $\xi_i = 0$，样本被正确分类且在间隔边界之外。
-   如果 $0 < \xi_i \le 1$，样本在间隔之内，但依然被正确分类。
-   如果 $\xi_i > 1$，样本被错误分类。

**2. 新的优化问题**
我们将松弛变量作为惩罚项加入到目标函数中。

$$
\begin{aligned}
\min_{\mathbf{w}, b, \mathbf{\xi}} \quad & \frac{1}{2}||\mathbf{w}||^2 + C \sum_{i=1}^{n} \xi_i \\
\text{s.t.} \quad & y_i(\mathbf{w}^T \mathbf{x}_i + b) \ge 1 - \xi_i, \\
& \xi_i \ge 0, \quad i = 1, 2, ..., n
\end{aligned}
$$

-   **超参数 $C$**：这是一个惩罚系数，用于权衡 **“最大化间隔”** 和 **“最小化分类错误”**。
    -   $C$ 很大：对误分类的惩罚很重，模型会努力将所有点都正确分类，趋向于硬间隔。
    -   $C$ 很小：对误分类的容忍度高，模型会允许更多的错误以换取一个更大的间隔。

##### C. 非线性SVM 与 核技巧 (The Kernel Trick)

当数据本身呈现非线性分布时，我们需要一个更强大的工具。

**1. 对偶问题 (Dual Problem)**
直接求解上面的优化问题（原问题）比较困难。通过引入拉格朗日乘子 $\alpha_i \ge 0$，我们可以将其转化为对偶问题。对偶问题只依赖于变量 $\alpha$：

$$
\begin{aligned}
\max_{\mathbf{\alpha}} \quad & \sum_{i=1}^{n} \alpha_i - \frac{1}{2} \sum_{i=1}^{n} \sum_{j=1}^{n} \alpha_i \alpha_j y_i y_j (\mathbf{x}_i^T \mathbf{x}_j) \\
\text{s.t.} \quad & \sum_{i=1}^{n} \alpha_i y_i = 0, \\
& 0 \le \alpha_i \le C, \quad i = 1, 2, ..., n
\end{aligned}
$$

-   $\mathbf{\alpha}$: $n \times 1$ 的拉格朗日乘子向量，每个样本对应一个 $\alpha_i$。
-   **关键发现**：在对偶问题中，数据点总是以内积 $(\mathbf{x}_i^T \mathbf{x}_j)$ 的形式出现。

**2. 核技巧**
-   **思想**：将原始 $m$ 维空间的特征向量 $\mathbf{x}$ 映射到一个更高维（甚至无限维）的特征空间 $\phi(\mathbf{x})$，使得数据在新空间中变得线性可分。
-   **困难**：高维映射 $\phi(\mathbf{x})$ 的计算可能非常复杂甚至不可行。
-   **技巧**：我们发现，我们不需要知道 $\phi$ 的具体形式，只需要能够计算映射后空间中的内积 $\phi(\mathbf{x}_i)^T \phi(\mathbf{x}_j)$ 即可。我们可以定义一个**核函数 (Kernel Function)** $K(\mathbf{x}_i, \mathbf{x}_j)$ 来直接计算这个值。
$$
K(\mathbf{x}_i, \mathbf{x}_j) = \phi(\mathbf{x}_i)^T \phi(\mathbf{x}_j)
$$
-   将对偶问题中的内积 $(\mathbf{x}_i^T \mathbf{x}_j)$ 替换为核函数 $K(\mathbf{x}_i, \mathbf{x}_j)$，我们就得到了非线性SVM的最终优化问题。

**3. 常用核函数**
-   **线性核 (Linear Kernel)**: $K(\mathbf{x}_i, \mathbf{x}_j) = \mathbf{x}_i^T \mathbf{x}_j$。等价于原始空间中的线性SVM。
-   **多项式核 (Polynomial Kernel)**: $K(\mathbf{x}_i, \mathbf{x}_j) = (\gamma \mathbf{x}_i^T \mathbf{x}_j + r)^d$。
-   **高斯核 / 径向基函数核 (RBF Kernel)**: $K(\mathbf{x}_i, \mathbf{x}_j) = \exp(-\gamma ||\mathbf{x}_i - \mathbf{x}_j||^2)$。这是最常用的核函数，因为它可以映射到无限维空间，能处理非常复杂的非线性关系。

#### 3. 算法复杂度分析

假设有 $n$ 个样本，每个样本 $m$ 维。

##### 训练复杂度

训练SVM的核心是求解一个二次规划 (Quadratic Programming, QP) 问题，变量是 $n$ 个拉格朗日乘子 $\alpha_i$。

1.  **构造核矩阵 (Gram Matrix)**：首先需要计算一个 $n \times n$ 的核矩阵 $\mathbf{K}$，其中 $K_{ij} = K(\mathbf{x}_i, \mathbf{x}_j)$。
    -   计算每个元素 $K(\mathbf{x}_i, \mathbf{x}_j)$ 的复杂度取决于核函数和特征维度 $m$。对于线性核，是 $O(m)$。对于高斯核，也是 $O(m)$。
    -   总共有 $n^2$ 个元素，所以构造核矩阵的复杂度是 $\mathbf{O(n^2m)}$。

2.  **求解QP问题**：
    -   通用的QP求解器求解一个有 $n$ 个变量的问题，其复杂度大约在 $\mathbf{O(n^2)}$ 到 $\mathbf{O(n^3)}$ 之间。
    -   在实践中，SVM通常使用专门的优化算法，如**序列最小最优化 (Sequential Minimal Optimization, SMO)**。SMO算法通过将大问题分解为一系列最小的QP子问题（每次只优化两个 $\alpha_i, \alpha_j$），从而大大提高了效率。SMO的实际复杂度通常在 $O(n)$ 到 $O(n^2)$ 之间，具体取决于数据集和参数 $C$。但在最坏情况下，仍然可能接近 $O(n^3)$。

**总训练复杂度**：主要由QP求解主导，可以认为是介于 $\mathbf{O(n^2)}$ 和 $\mathbf{O(n^3)}$ 之间。对于面试，可以回答：“主要开销在求解QP问题上，一般认为是 $O(n^3)$ 量级，但通过SMO等高效算法，实际表现通常在 $O(n^2)$ 左右。”

##### 预测复杂度

在模型训练完成后，我们得到了支持向量（即那些 $\alpha_i > 0$ 的样本）和偏置 $b$。对于一个新的测试点 $\mathbf{x}_{new}$，其决策函数为：

$$
f(\mathbf{x}_{new}) = \text{sign} \left( \sum_{i=1}^{n} \alpha_i y_i K(\mathbf{x}_i, \mathbf{x}_{new}) + b \right) = \text{sign} \left( \sum_{i \in SV} \alpha_i y_i K(\mathbf{x}_i, \mathbf{x}_{new}) + b \right)
$$

-   $SV$ 是支持向量的集合。设支持向量的数量为 $n_{sv}$。
-   预测时，我们需要计算新样本与 **每一个支持向量** 的核函数值。
-   计算一次核函数的复杂度是 $O(m)$。

**总预测复杂度**：$\mathbf{O(n_{sv} \cdot m)}$。
-   这是一个关键点：SVM的预测速度不依赖于总训练样本数 $n$，而只依赖于支持向量的数量 $n_{sv}$。如果支持向量的数量不多，SVM的预测速度会很快。反之，如果几乎所有样本都成为支持向量（例如 $C$ 非常大或数据非常复杂），预测会变慢。