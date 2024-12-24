# 最优化基础

!!! quote "本部分内容由GPT-4o以及Claude-3.5负责整理。"
    注意了GPT默认输出的Markdown格式在我的mkdocs配置下是稍有不同的，有的公式渲染不出来。需要自行Prompt Engineering 一下。

### **向量与矩阵**

1. **向量与矩阵的表示：**
    - 向量通常用**小写字母**表示。
    - 矩阵通常用**大写字母**表示。  

2. **向量和矩阵的空间：**
    - 长度为 $n$ 的实向量的空间表示为 $\mathbb{R}^n$。
    - $m \times n$ 的实矩阵的空间表示为 $\mathbb{R}^{m \times n}$。

3. **对称矩阵的定义：**
    - 如果矩阵 $A \in \mathbb{R}^{n \times n}$ 满足 $A = A^T$，则 $A$ 是**对称矩阵** (symmetric matrix)。

4. **正定矩阵的定义：**
    - 如果对称矩阵 $A$ 满足 $x^T A x > 0, \forall x \neq 0 \in \mathbb{R}^n$，则 $A$ 是**正定矩阵**（$A > 0$） (positive definite)。

5. **半正定矩阵的定义：**
    - 如果对称矩阵 $A$ 满足 $x^T A x \geq 0, \forall x \in \mathbb{R}^n$，则 $A$ 是**半正定矩阵**（$A \geq 0$） (positive semidefinite)。


-----

### **范数 (Norms)**
1. **范数的定义：**
   - 范数 $\|\cdot\|$ 是一个实值函数，满足以下性质：
     - $\|x\| \geq 0$，对所有 $x$（非负性 Non-negativity）。
     - $\|x\| = 0$ 当且仅当 $x = 0$（确定性 Definiteness）。
     - $\|\alpha x\| = |\alpha| \|x\|$，对所有实数 $\alpha$（齐次性 Homogeneity）。
     - $\|x + y\| \leq \|x\| + \|y\|$，对所有 $x, y$（三角不等式 Triangle inequality）。

2. **矩阵范数的扩展：**
   - 对于矩阵范数，有用但非必要的性质：
     - $\|XY\| \leq \|X\| \|Y\|$，适用于所有 $X, Y$ 且 $XY$ 存在的情况。

---

### 标题：**向量范数 (Vector Norms)**

**常见向量范数：**
:   **$l_1$-范数 (L1-norm)**:  
     
    $\|x\|_1 = \sum_{i=1}^n |x_i|$  
     （所有分量绝对值之和）。

:   **欧几里得范数 (Euclidean-norm, $l_2$-norm)**:  
    
    $\|x\|_2 = \sqrt{x^T x} = \sqrt{\sum_{i=1}^n x_i^2}$  （平方和的平方根）。

:   **$l_\infty$-范数 (L∞-norm)**:  
    
    $\|x\|_\infty = \max_{1 \leq i \leq n} |x_i|$  
     （所有分量绝对值的最大值）。

:   **$l_p$-范数 (Lp-norm)**:  
    
    $\|x\|_p = \left( \sum_{i=1}^n |x_i|^p \right)^{1/p}, \forall p \geq 1$  
     （分量绝对值的 $p$ 次方和的 $1/p$ 次方根）。

:   **加权范数 (Weighted norm)**:  
    
    $\|x\|_G = \sqrt{x^T G x}$，其中 $G$ 是一个对称正定矩阵 (Symmetric positive definite matrix)。

**特殊向量范数：**
:   **$l_0$-范数 (L0-norm)**:  
    
    $\|x\|_0$ 是向量中非零元素的总数量。  


---


### 向量范数的性质 (Properties of Vector Norms)

1. **Holder不等式 (Hölder Inequality):**
    - $|x^T y| \leq \|x\|_p \|y\|_q$，其中 $\frac{1}{p} + \frac{1}{q} = 1$。
    - 内积 (Inner product): $x \cdot y \equiv x^T y = \sum_{i=1}^n x_i y_i$。

2. **范数的最大值公式：**
    - $\|x\|_p = \max_{\|y\|_q \leq 1} x^T y$。
    - 当 $p = q = 2$: $|x^T y| \leq \|x\|_2 \|y\|_2$ 且 $\|x\|_2 = \max_{\|y\|_2 \leq 1} x^T y$。
    - 当 $p = 1, q = \infty$: $|x^T y| \leq \|x\|_1 \|y\|_\infty$ 且 $\|x\|_1 = \max_{\|y\|_\infty \leq 1} x^T y$，$\|x\|_\infty = \max_{\|y\|_1 \leq 1} x^T y$。

3. **向量范数的平方关系：**
    - $\|x\|_2^2 + \|y\|_2^2 = \|x + y\|_2^2 - 2x^T y$。
    - 等价形式：$\|x\|_2^2 + \|y\|_2^2 = \|x - y\|_2^2 + 2x^T y$。
    - 平均形式：$= \frac{1}{2}(\|x + y\|_2^2 + \|x - y\|_2^2) \geq 2|x^T y|$。

4. **向量范数的等价性 (Equivalence of vector norms):**
    - $c_1 \|x\|_+ \leq \|x\|_* \leq c_2 \|x\|_+$。
    - $\|x\|_2 \leq \|x\|_1 \leq \sqrt{n}\|x\|_2$。
    - $\|x\|_\infty \leq \|x\|_2 \leq \sqrt{n}\|x\|_\infty$。
    - $\|x\|_\infty \leq \|x\|_1 \leq n\|x\|_\infty$。

----

### 矩阵范数 (Matrix Norms)

1. **矩阵范数的定义：**
   - 矩阵范数通常基于向量范数定义：
     
$$\|A\|_p = \max_{x \neq 0} \frac{\|Ax\|_p}{\|x\|_p}$$

2. **常见的矩阵范数：**
   - **$l_1$-范数 (L1-norm)**:  

$$\|A\|_1 = \max_{1 \leq j \leq n} \sum_{i=1}^m |a_{ij}|$$  
     
     （每列元素绝对值之和的最大值）。
   
   - **$l_2$-范数 (L2-norm)**:  

$$\|A\|_2 = \sqrt{\lambda_{\max}(A^T A)}$$  
     
     （矩阵 $A^T A$ 的最大特征值的平方根）。
   
   - **$l_\infty$-范数 (L∞-norm)**:  

$$\|A\|_\infty = \max_{1 \leq i \leq m} \sum_{j=1}^n |a_{ij}|$$  
     
     （每行元素绝对值之和的最大值）。

3. **Frobenius范数 (Frobenius Norm):**

$$\|A\|_F = \sqrt{\text{tr}(A^T A)} = \sqrt{\sum_{i=1}^m \sum_{j=1}^n a_{ij}^2}$$
   
   - **迹 (Trace)**:  

$$\text{tr}(A^T B) = \sum_{j=1}^n \left( \sum_{i=1}^m a_{ij} b_{ij} \right)$$
   
   - 矩阵加法性质：  

$$\|A + B\|_F^2 = \|A\|_F^2 + \|B\|_F^2 + 2 \text{tr}(A^T B)$$

4. **正交矩阵 (Orthogonal Matrix):**
   - 如果矩阵 $Q$ 是正交矩阵，则满足：

$$Q Q^T = Q^T Q = I$$ 

> (单位矩阵 Identity matrix)
    
因此：$Q^T = Q^{-1}$。
   - 性质：

$$\|A\|_F = \|QA\|_F = \|A\|_2 = \|QA\|_2, \|Qx\|_2 = \|x\|_2$$


### Sherman-Morrison公式 (Sherman-Morrison Formula)

- **问题描述**  
    - 初始矩阵 $A \in \mathbb{R}^{n \times n}$，扰动矩阵 $B = A + u v^T$，其中 $u, v \in \mathbb{R}^n$。  
    - 已知 $A^{-1}$，如何高效地计算扰动矩阵 $B$ 的逆？

- **矩阵 $(I + uv^T)^{-1}$ 的推导**  
    - 假设 $(I + uv^T)^{-1} = (I + \rho uv^T)$，则：

    $$
    (I + uv^T)(I + \rho uv^T) = I + [1 + \rho(1 + v^T u)] uv^T
    $$

    - 由此可得：

    $$
    \rho = -\frac{1}{1 + v^T u}
    $$

    - 所以：

    $$
    (I + uv^T)^{-1} = I - \frac{uv^T}{1 + v^T u}
    $$

- **使用上述关系计算 $(A + uv^T)^{-1}$**  
    - 根据关系：

    $$
    (A + uv^T)^{-1} = \left(A (I + A^{-1} uv^T) \right)^{-1}
    $$

    - 推导步骤：

    $$
    (A + uv^T)^{-1} = (I + A^{-1} uv^T)^{-1} A^{-1}
    $$

    $$= \left(I - \frac{A^{-1} uv^T}{1 + v^T A^{-1} u}\right) A^{-1}$$

    $$= A^{-1} - \frac{A^{-1} uv^T A^{-1}}{1 + v^T A^{-1} u}$$

- **使用条件**  
    - 当 $1 + v^T A^{-1} u \neq 0$ 时，公式成立。


### 梯度(Gradient) 和Hessian矩阵 

- **函数与梯度**  
    - 设 $f$ 是一个关于 $n$ 个变量的实值函数：
    
    $$
    f(x) = f(x_1, x_2, \cdots, x_n)
    $$

    - $f$ 的一阶偏导数组成的向量称为 **梯度 (Gradient)**，表示为：
    
    $$
    \nabla f(x) = \left(\frac{\partial f(x)}{\partial x_1}, \frac{\partial f(x)}{\partial x_2}, \cdots, \frac{\partial f(x)}{\partial x_n}\right)^T
    $$

- **Hessian矩阵**  
    - $f$ 的二阶偏导数构成的矩阵称为 **Hessian矩阵 (Hessian matrix)** 或简称为 **Hessian**，表示为：
    
    $$
    \nabla^2 f(x)
    $$

    - 其元素的定义为：
    
    $$
    [\nabla^2 f(x)]_{ij} \equiv \frac{\partial^2 f(x)}{\partial x_i \partial x_j}
    $$

- **Hessian矩阵的性质**  
    - 对于具有连续二阶导数的函数，Hessian矩阵是一个 **对称矩阵 (Symmetric matrix)**，因为：
    
    $$
    \frac{\partial^2 f(x)}{\partial x_i \partial x_j} = \frac{\partial^2 f(x)}{\partial x_j \partial x_i}
    $$

----

### 雅可比矩阵 (The Jacobian Matrix)

- **定义**  
    - 设 $f$ 是从 $\mathbb{R}^n$ 到 $\mathbb{R}^m$ 的向量值函数：
    
    $$
    f(x) = f(x_1, x_2, \cdots, x_n) = 
    \begin{pmatrix}
    f_1(x_1, x_2, \cdots, x_n) \\
    f_2(x_1, x_2, \cdots, x_n) \\
    \vdots \\
    f_m(x_1, x_2, \cdots, x_n)
    \end{pmatrix}
    $$

    - $f$ 在点 $x$ 的 **雅可比矩阵 (Jacobian Matrix)** 定义为 $\nabla f(x)^T$，其中：
    
    $$
    \nabla f(x) = (\nabla f_1(x), \nabla f_2(x), \cdots, \nabla f_m(x))
    $$

    - 其元素的定义为：
    
    $$
    [\nabla f(x)^T]_{ij} = \frac{\partial f_i(x)}{\partial x_j}
    $$

- **练习**  
    - 计算下列函数的 Jacobian：
    
    $$
    f(x) = 
    \begin{pmatrix}
    \sin x_1 + \cos x_2 \\
    e^{3x_1 + x_2^2} \\
    4x_1^3 + 7x_1 x_2^2
    \end{pmatrix}
    $$

---

### 链式法则 (The Chain Rule)

- **定义**  
    - 函数求导中的链式法则用于计算复合函数的导数。

- **复合函数的形式**  
    - 考虑函数 $g(x) = g(x_1, \cdots, x_n)$，且假设每个 $x_i$ 都是变量 $t_1, \cdots, t_m$ 的函数，即 $x_i = x_i(t_1, \cdots, t_m)$。
    - 对于复合函数 $h(t) = g(x(t))$，链式法则表示为：
    
    $$
    \nabla h(t) = \nabla x(t)^T \nabla g(x(t))
    $$

- **应用**  
    - 若 $f : \mathbb{R}^n \to \mathbb{R}$ 是连续可微的，令 $g(x) = f(Ax - b)$，则：
    
    $$
    \nabla g(x) = A^T \nabla f(Ax - b)
    $$

----


### 方向导数 (Directional Derivatives)

- **定义**  
    - 如果 $f$ 是连续可微的，且 $p \in \mathbb{R}^n$，则 $f$ 在方向 $p$ 上的方向导数定义为：

    $$
    \frac{\partial f(x)}{\partial p} \equiv \lim_{\epsilon \to 0} \frac{f(x + \epsilon p) - f(x)}{\epsilon} = p^T \nabla f(x)
    $$

- **验证公式的步骤**  
    - 定义函数 $\phi(\alpha)$ 为：

    $$
    \phi(\alpha) = f(x + \alpha p) = f(y(\alpha))
    $$

    - 注意到以下关系：

    $$
    \lim_{\epsilon \to 0} \frac{f(x + \epsilon p) - f(x)}{\epsilon} = \lim_{\epsilon \to 0} \frac{\phi(\epsilon) - \phi(0)}{\epsilon} = \phi'(0)
    $$

    - $\phi'(\alpha)$ 的计算为：

    $$
    \phi'(\alpha) = \sum_{i=1}^n \frac{\partial f(y(\alpha))}{\partial y_i} p_i = p^T \nabla f(y(\alpha))
    $$

---

### 泰勒级数 (Taylor Series)

- **定义**  
    - 泰勒级数是一种在指定点 $x_0$ 附近对函数 $f$ 进行近似的方法。
    - 通过泰勒级数得到的近似是一种 **多项式 (Polynomial)**。

- **应用场景**  
    - 当函数具有导数时，可以使用泰勒级数，其应用包括：
        - 用于估计函数在给定点附近的值（当函数难以直接计算时）。
        - 近似的导数和积分可用于估计原函数的导数和积分。
        - 用于推导多种算法，如寻找函数零点和优化函数的算法。

- **一维函数的泰勒级数**  
    - 对于具有 $n$ 阶连续导数的一维函数 $f$，在指定点 $x_0$ 的 $n$ 阶泰勒级数近似为：

    $$
    f(x_0 + p) \approx f(x_0) + p f'(x_0) + \frac{1}{2!} p^2 f''(x_0) + \cdots + \frac{p^n}{n!} f^{(n)}(x_0)
    $$

    - 泰勒级数的前两项给出了 $f$ 在 $x_0$ 点的切线方程：

    $$
    y = f(x_0) + (x - x_0) f'(x_0)
    $$

    - 泰勒级数的前三项提供了 $f$ 在 $x_0$ 点的二次近似。

- **多变量函数的泰勒级数**  
    - 对于多变量函数的泰勒级数，表示为：

    $$
    f(x_0 + p) = f(x_0) + p^T \nabla f(x_0) + \frac{1}{2} p^T \nabla^2 f(x_0) p + \cdots
    $$

---

### 泰勒级数的余项形式 (Remainder Form)

- **定义**  
    - 泰勒级数的另一种形式是 **余项形式 (Remainder Form)**。

- **余项形式的公式**  
    - 若仅使用前三项，其形式如下：
        - 对于一维函数：

        $$
        f(x_0 + p) = f(x_0) + p f'(x_0) + \frac{1}{2!} p^2 f''(\xi)
        $$

        - 对于多变量函数：

        $$
        f(x_0 + p) = f(x_0) + p^T \nabla f(x_0) + \frac{1}{2!} p^T \nabla^2 f(\xi) p
        $$

        - 其中 $\xi$ 是位于 $x_0$ 和 $x_0 + p$ 之间的未知点。

- **精度分析**  
    - 泰勒级数的精度可通过对最后的 **余项 (Remainder)** 项进行界定分析。
    - 泰勒级数的高阶项可以写出，但符号更复杂，并不需要在本课程中使用。

-----


### 仿射集合 (Affine Set)

- **仿射集合的定义**  
    - 若集合 $C$ 满足，对于任意 $x, y \in C$ 和 $\alpha \in \mathbb{R}$，都有：

    $$
    \alpha x + (1 - \alpha)y \in C
    $$

    - 当 $x, y$ 是 $\mathbb{R}^n$ 中的两个不同点，$\alpha \in \mathbb{R}$ 时，由 $z = \alpha x + (1 - \alpha)y$ 表示的点集合是由 $x$ 和 $y$ 决定的 **直线 (Line)**。

- **仿射组合 (Affine Combination)**  
    - 对于 $x_1, x_2, \cdots, x_k \in C$，若系数 $\alpha_1, \alpha_2, \cdots, \alpha_k$ 满足：

    $$
    \sum_{i=1}^k \alpha_i = 1
    $$

    则：

    $$
    y = \sum_{i=1}^k \alpha_i x_i
    $$

    是 $x_1, x_2, \cdots, x_k$ 的仿射组合。

---

### 仿射集合的性质

- **性质 1**  
    - 根据仿射集合的定义，可以证明：若 $C$ 是一个仿射集合，且 $x_1, \cdots, x_k \in C$，$\alpha_1, \cdots, \alpha_k$ 满足：

    $$
    \alpha_1 + \cdots + \alpha_k = 1
    $$

    则点：

    $$
    \alpha_1 x_1 + \cdots + \alpha_k x_k \in C
    $$

- **性质 2**  
    - 仿射集合包含了它所有点的仿射组合。

- **性质 3**  
    - 例如，集合 $\{x \mid Ax = b\}$ 是一个仿射集合。

- **仿射包 (Affine Hull)**  
    - 集合 $C$ 中所有点的仿射组合构成的集合称为 $C$ 的 **仿射包 (Affine Hull)**，表示为：

    $$
    \text{aff } C = \{\alpha_1 x_1 + \cdots + \alpha_k x_k \mid x_1, \cdots, x_k \in C, \alpha_1 + \cdots + \alpha_k = 1\}
    $$

----

### 凸集 (Convex Set)

- **凸集的定义**  
    - 若集合 $C$ 满足，对于任意 $x, y \in C$ 和 $\alpha \in [0, 1]$，都有：

    $$
    \alpha x + (1 - \alpha)y \in C
    $$

    - 换句话说，若 $x, y \in C$，则连接 $x$ 和 $y$ 的线段也属于集合 $C$。

- **凸集的性质**  
    - 若 $C_1$ 和 $C_2$ 是凸集，则以下操作仍然是凸集吗？
        - $\beta C_1$
        - $C_1 + C_2$
        - $C_1 - C_2$
        - $C_1 \cap C_2$
    - 按约定，空集 $\emptyset$ 是凸集。
    - 表达式 $\alpha x + (1 - \alpha)y \in C$ 被称为 $x$ 和 $y$ 的 **凸组合 (Convex Combination)**。

---

### 凸组合与凸包 (Convex Combination and Convex Hull)

- **凸组合 (Convex Combination)**  
    - 对于 $x_1, x_2, \cdots, x_k \in C$，若系数 $\alpha_1, \alpha_2, \cdots, \alpha_k$ 满足：

    $$
    \sum_{i=1}^k \alpha_i = 1 \quad \text{且} \quad \alpha_i \geq 0, \; i = 1, \cdots, k
    $$

    则：

    $$
    y = \sum_{i=1}^k \alpha_i x_i
    $$

    是 $x_1, x_2, \cdots, x_k$ 的凸组合。

- **凸集的判定**  
    - 一个集合是凸集，当且仅当它包含所有点的凸组合。

- **凸包 (Convex Hull)**  
    - 集合 $C$ 中所有点的凸组合构成的集合称为 $C$ 的 **凸包 (Convex Hull)**，表示为：

    $$
    \text{conv } C = \{\alpha_1 x_1 + \cdots + \alpha_k x_k \mid x_1, \cdots, x_k \in C, \alpha_1 + \cdots + \alpha_k = 1, \alpha_i \geq 0\}
    $$

----

### 超平面与半空间 (Hyperplane and Halfspace)

- **超平面 (Hyperplane)**  
    - 定义为：

    $$
    H = \{x \mid a^T x = b\}, \; (a \neq 0)
    $$

- **半空间 (Halfspace)**  
    - 上半空间 (Upper halfspace):

    $$
    H^+ = \{x \mid a^T x \leq b\}, \; (a \neq 0)
    $$

    - 下半空间 (Lower halfspace):

    $$
    H^- = \{x \mid a^T x \geq b\}, \; (a \neq 0)
    $$

- **性质**  
    - 超平面和半空间都是凸集 (Convex)。

- **多面体 (Polyhedron)**  
    - 多面体是有限个半空间与超平面的交集，定义为：

    $$
    P = \bigcap_{i=1}^m H_i, \quad 
    $$

    >  $H_i$ 是超平面或半空间。


----


### 范数球与范数锥 (Norm Ball and Norm Cone)

- **范数球 (Norm Ball)**  
    - 以点 $x_c$ 为中心，半径为 $r$ 的范数球定义为：

    $$
    B(x_c, r) = \{x \mid \|x - x_c\| \leq r\}
    $$

    - 常见的范数球包括：
        - $l_1$-球：$\{x \mid \|x - x_c\|_1 \leq r\}$
        - $l_\infty$-球：$\{x \mid \|x - x_c\|_\infty \leq r\}$
        - $l_2$-球 (欧几里得球, Euclidean Ball)：$\{x \mid \|x - x_c\|_2 \leq r\}$

- **范数锥 (Norm Cone)**  
    - 范数锥定义为：

    $$
    \{(x, t) \mid \|x\|_2 \leq t\} \subseteq \mathbb{R}^{n+1}
    $$

    - 欧几里得范数锥也被称为 **二阶锥 (Second-order Cone)** 或 **冰淇淋锥 (Ice-cream Cone)**。

- **性质**  
    - 范数球和范数锥都是凸集 (Convex)。

---

### 锥与锥组合 (Cone and Conic Combination)

- **锥的定义 (Cone)**  
    - 如果对于集合 $C$ 中的任意元素 $x$，$\theta x \in C$ 且 $\forall \theta \geq 0$，则集合 $C$ 是一个锥。

- **锥组合 (Conic Combination)**  
    - 定义为：

    $$
    x = \theta_1 x_1 + \theta_2 x_2, \quad \text{其中 } \theta_1 \geq 0, \; \theta_2 \geq 0
    $$

- **凸锥 (Convex Cone)**  
    - 包含其所有点的锥组合的集合称为 **凸锥**。
    - 若对任意标量 $\alpha, \beta \geq 0$ 和任意 $x, y \in C$，$\alpha x + \beta y \in C$，则锥 $C$ 是凸锥。

