# 线性回归的复杂度分析

## 最小二乘法线性回归的复杂度分析


最小二乘法的目标是找到一组参数（权重向量 $\mathbf{w}$  和偏置项 $b$），使得线性模型的预测值与真实值之间的**残差平方和**最小。

**损失函数** (Loss Function)：
对于 $n$ 个样本的数据集，损失函数定义为所有预测误差的平方和：

$$J(\mathbf{w}, b) = \sum_{i=1}^{n} \left( y_i - (\mathbf{w} \cdot \mathbf{x}_i + b) \right)^2$$

最小二乘法的一个关键优势是存在**解析解**（闭式解），可以直接通过公式计算得出最优参数。

### 矩阵表示形式

为了简化计算，将偏置项 $b$ 融入权重向量 $\mathbf{w}$ 中：
1.  给特征矩阵 $\mathbf{X}$ ($n \times m$) 添加一列全为1的列向量，构成新矩阵 $\mathbf{\tilde{X}} = [\mathbf{X}, \mathbf{1}]$ ，其维度为 $n \times (m+1)$。
2.  将权重向量扩展为 $\mathbf{\tilde{w}} = [\mathbf{w}; b]$ ，其维度为 $(m+1) \times 1$。
3.  此时，模型预测可表示为：$\mathbf{\hat{y}} = \mathbf{\tilde{X}} \mathbf{\tilde{w}}$
4.  损失函数可重写为：$J(\mathbf{\tilde{w}}) = || \mathbf{y} - \mathbf{\tilde{X}} \mathbf{\tilde{w}} ||^2$

### 推导与求解
1.  **求导**：对损失函数 $J(\mathbf{\tilde{w}})$ 关于 $\mathbf{\tilde{w}}$ 求导，并令其为零：

$$\nabla J(\mathbf{\tilde{w}}) = -2\mathbf{\tilde{X}}^T(\mathbf{y} - \mathbf{\tilde{X}} \mathbf{\tilde{w}}) = 0$$

2.  **正规方程** (Normal Equation)：由上式得到：

$$\mathbf{\tilde{X}}^T \mathbf{\tilde{X}} \mathbf{\tilde{w}} = \mathbf{\tilde{X}}^T \mathbf{y}$$

3.  **闭式解**：最终的最优参数解为：
    $$ \mathbf{\tilde{w}}^* = (\mathbf{\tilde{X}}^T \mathbf{\tilde{X}})^{-1} \mathbf{\tilde{X}}^T \mathbf{y} $$


复杂度来源于求解闭式解 $\mathbf{\tilde{w}}^* = (\mathbf{\tilde{X}}^T \mathbf{\tilde{X}})^{-1} \mathbf{\tilde{X}}^T \mathbf{y}$ 的步骤。假设 $\mathbf{X}$ 是 $n \times m$ 矩阵。

| 计算步骤                                                         | 操作描述                                                                                           | 复杂度           |
| :--------------------------------------------------------------- | :------------------------------------------------------------------------------------------------- | :--------------- |
| 1. 计算 $\mathbf{X}^T\mathbf{X}$                                 | <span style="color:red">$(m \times n)$ 矩阵乘以 $(n \times m)$ 矩阵，得到 $m \times m$ 矩阵</span> | $O(n \cdot m^2)$ |
| 2. 计算 $(\mathbf{X}^T\mathbf{X})^{-1}$                          | <span style="color:red">对 $m \times m$ 矩阵求逆（如使用高斯消元法）</span>                        | $O(m^3)$         |
| 3. 计算 $\mathbf{X}^T\mathbf{y}$                                 | $(m \times n)$ 矩阵乘以 $(n \times 1)$ 向量，得到 $m \times 1$ 向量                                | $O(n \cdot m)$   |
| 4. 计算 $(\mathbf{X}^T\mathbf{X})^{-1} (\mathbf{X}^T\mathbf{y})$ | $m \times m$ 矩阵乘以 $m \times 1$ 向量                                                            | $O(m^2)$         |

**（训练阶段）总复杂度**：$O(n \cdot m^2 + m^3)$

**推理阶段复杂度**：$O (m)$，只需要计算一次矩阵乘法，把新的数据乘以参数矩阵即可。

---

### 复杂度含义
*   **当 $n \gg m$** (样本数远大于特征数)：$O(n \cdot m^2)$ 是主导项，算法相对高效。
*   **当 $m$ 非常大** (特征数很多)：$O(m^3)$ 成为性能瓶颈，计算成本急剧上升。


> “对于线性回归，当特征数较少时（例如小于1000），最小二乘法的闭式解是首选，因为它精确且无需迭代。但当特征数极大或数据量无法全部装入内存时，我们会转向**梯度下降**等迭代优化方法。”

---

## 梯度下降法计算线性回归的复杂度分析

正因为我们计算解析解的开销太大，我们必须引入一些更加有效的方式进行拟合。我们前面方法应用时，往往会面对极大的样本数，计算**整个训练集**的损失函数 $J$ 的**真实梯度** ($\nabla J$) 成本很高，因为它需要遍历所有 $n$ 个样本。因此我们的新方法是：

随机梯度下降（SGD），使用单个样本的损失函数，**来代替原先的全样本的损失函数，从一个猜测点开始，反复地“摸索着”向最低点前进**。

这是采用了一种高效、随机的策略来估计达到目标所需的方向。​​ 它是一种“长远来看是正确的”的近似方法。

注意：==无论用最小二乘法还是SGD，我们**最终的目标是完全一致的**：找到一组参数 $\mathbf{w}, b$，使得基于**所有样本**的总体损失函数最小化==。

也就是最小化一个MSE：

$J(\mathbf{w}, b) = \frac{1}{n} \sum_{i=1}^{n} \frac{1}{2}(y^{(i)} - \hat{y}^{(i)})^2$

SGD的核心思想是：**用单个样本的损失 $L^{(i)}$ 的梯度，来近似（估计）总体损失 $J$ 的真实梯度**。我们悄悄改写了一下损失函数，但是它依然和前面是等价的：

$$ \nabla J(\mathbf{w}, b) = \frac{1}{n} \sum_{i=1}^{n} \nabla L^{(i)}(\mathbf{w}, b) $$

**在SGD的每一步，我们随机抽一个样本 $i$，然后用 $\nabla L^{(i)}$ 来代替 $\nabla J$，并沿着这个方向更新参数。**

!!! question "==为什么可以这么做？？？=="

    1.  **数学期望上的无偏估计**：单个样本的梯度 $\nabla L^{(i)}$ 是总体平均梯度 $\nabla J$ 的一个**无偏估计**。这意味着，如果我们随机采样很多次，这些单个梯度的平均值会收敛到真实的总体梯度。**从长远来看（经过大量迭代），更新方向是正确的。**

    2.  **引入噪声以跳出局部最优**：虽然单个样本的梯度是“嘈杂的”或“随机的”，并不总是指向最陡的下坡方向，但这种噪声在实践中有很大好处。它可以帮助算法跳出局部极小点，并有可能找到更好的全局最优解（或更平坦的极小值点）。

    3.  **实践中的高效性**：对于大规模数据集，计算真实梯度 $\nabla J$（称为批量梯度下降）的每一步成本都极高。SGD虽然方向嘈杂，但每一步的计算成本极低（$O(m)$ vs $O(n \cdot m)$），使得它可以用很多次“小步快跑”的更新，在总体计算成本上远远超越“大步精准”的批量梯度下降。

---

现在我们继续。

### 一种从标量角度的理解

为了推导梯度，我们更关心**单个样本**的损失，因为SGD就是基于**单个样本**的。我们定义样本 $i$ 的损失为：

$$L^{(i)}(\mathbf{w}, b) = \frac{1}{2} (y^{(i)} - (\mathbf{w} \cdot \mathbf{x}^{(i)} + b))^2$$

我们的目标是求 $\nabla_{\mathbf{w}} L^{(i)} = \begin{bmatrix} \frac{\partial L^{(i)}}{\partial w_1} \\ \frac{\partial L^{(i)}}{\partial w_2} \\ \vdots \\ \frac{\partial L^{(i)}}{\partial w_m} \end{bmatrix}$ 和 $\frac{\partial L^{(i)}}{\partial b}$。


这种方法是对权重向量 $\mathbf{w}$ 中的每一个分量 $w_j$ 分别求偏导数。

**第一步：写出损失函数**

$$ L = \frac{1}{2} (y - (w_1x_1 + w_2x_2 + ... + w_mx_m + b))^2 $$

为了简洁，我们暂时省略了上标 $(i)$。

**第二步：对偏置项 $b$ 求导**
应用链式法则，将括号内的项视为一个整体 $u$：

$$ \frac{\partial L}{\partial b} = \frac{\partial L}{\partial u} \cdot \frac{\partial u}{\partial b} $$
*   $\frac{\partial L}{\partial u} = \frac{\partial}{\partial u} [\frac{1}{2}u^2] = u$
*   $\frac{\partial u}{\partial b} = \frac{\partial}{\partial b} [y - (w_1x_1 + ... + w_mx_m + b)] = -1$
*   所以： $\frac{\partial L}{\partial b} = u \cdot (-1) = (y - (\mathbf{w} \cdot \mathbf{x} + b)) \cdot (-1) = - (y - \hat{y})$

**第三步：对权重分量 $w_j$ 求导**

同样应用链式法则：

$$ \frac{\partial L}{\partial w_j} = \frac{\partial L}{\partial u} \cdot \frac{\partial u}{\partial w_j} $$
*   $\frac{\partial L}{\partial u} = u$ (和上面一样)
*   $\frac{\partial u}{\partial w_j} = \frac{\partial}{\partial w_j} [y - (w_1x_1 + ... + w_jx_j + ... + w_mx_m + b)] = -x_j$
*   所以： $\frac{\partial L}{\partial w_j} = u \cdot (-x_j) = (y - \hat{y}) \cdot (-x_j) = - (y - \hat{y}) \cdot x_j$

**第四步：组合成梯度向量**
我们对所有 $j = 1$ 到 $m$ 都进行了上述计算，因此：

$$ \nabla_{\mathbf{w}} L = \begin{bmatrix} \frac{\partial L}{\partial w_1} \\ \frac{\partial L}{\partial w_2} \\ \vdots \\ \frac{\partial L}{\partial w_m} \end{bmatrix} = \begin{bmatrix} - (y - \hat{y}) \cdot x_1 \\ - (y - \hat{y}) \cdot x_2 \\ \vdots \\ - (y - \hat{y}) \cdot x_m \end{bmatrix} = - (y - \hat{y}) \cdot \begin{bmatrix} x_1 \\ x_2 \\ \vdots \\ x_m \end{bmatrix} = - (error) \cdot \mathbf{x} $$

**结论（标量形式）：**

*   $\nabla_{\mathbf{w}} L^{(i)} = - (y^{(i)} - \hat{y}^{(i)}) \cdot \mathbf{x}^{(i)}$
*   $\frac{\partial L^{(i)}}{\partial b} = - (y^{(i)} - \hat{y}^{(i)})$

---

### 一种从向量角度的理解

这种方法直接对向量 $\mathbf{w}$ 进行操作，更贴近你“对矩阵求导”的直觉。这里需要用到一些向量求导的法则。

**法则**：对于形如 $L = \frac{1}{2} (\mathbf{a} \cdot \mathbf{w} + c)^2$ 的函数，其对向量 $\mathbf{w}$ 的导数为 $\nabla_{\mathbf{w}} L = (\mathbf{a} \cdot \mathbf{w} + c) \cdot \mathbf{a}$。

**第一步：重写损失函数**
令 $error = (y - (\mathbf{w} \cdot \mathbf{x} + b))$，则 $L = \frac{1}{2} (error)^2$。

**第二步：对向量 $\mathbf{w}$ 求导**
我们将 $\mathbf{x} \cdot \mathbf{w} + b$ 视为一个整体。应用链式法则和上面的求导法则：

$$ \nabla_{\mathbf{w}} L = \frac{\partial L}{\partial (error)} \cdot \nabla_{\mathbf{w}} (error) = (error) \cdot \nabla_{\mathbf{w}} (y - \mathbf{x} \cdot \mathbf{w} - b) $$

*   $\nabla_{\mathbf{w}} (y - \mathbf{x} \cdot \mathbf{w} - b) = \nabla_{\mathbf{w}} (-\mathbf{x} \cdot \mathbf{w}) = -\mathbf{x}$
    *   （这里用到了法则：$\nabla_{\mathbf{w}} (\mathbf{a} \cdot \mathbf{w}) = \mathbf{a}$）
*   所以： $\nabla_{\mathbf{w}} L = (error) \cdot (-\mathbf{x}) = - (error) \cdot \mathbf{x}$

**第三步：对标量 $b$ 求导**
$$ \frac{\partial L}{\partial b} = \frac{\partial L}{\partial (error)} \cdot \frac{\partial (error)}{\partial b} = (error) \cdot (-1) = - (error) $$

**结论（向量形式）：**

与标量形式推导结果完全一致：

*   $\nabla_{\mathbf{w}} L^{(i)} = - (y^{(i)} - \hat{y}^{(i)}) \cdot \mathbf{x}^{(i)}$
*   $\frac{\partial L^{(i)}}{\partial b} = - (y^{(i)} - \hat{y}^{(i)})$


| 参数                      | 梯度                                                       |
| :------------------------ | :--------------------------------------------------------- |
| **权重向量 $\mathbf{w}$** | $\nabla_{\mathbf{w}} L = - (y - \hat{y}) \cdot \mathbf{x}$ |
| **偏置项 $b$**            | $\frac{\partial L}{\partial b} = - (y - \hat{y})$          |

**直观理解**：
*   梯度始终是 **“误差”** × **“导致该误差的输入”**。
*   对于权重 $w_j$，其对应的输入是特征 $x_j$，所以梯度是 $-error \cdot x_j$。
*   对于偏置 $b$，你可以认为它总是乘以一个虚拟的输入特征 “1”，所以梯度是 $-error \cdot 1$。

在SGD的更新规则中，我们沿着**负梯度**方向更新参数，所以符号变为正：


$$ \nabla_{\mathbf{w}} J^{(i)} = - (y_i - (\mathbf{w} \cdot \mathbf{x}_i + b)) \cdot \mathbf{x}_i = - (error) \cdot \mathbf{x}_i $$

$$ \nabla_{b} J^{(i)} = - (y_i - (\mathbf{w} \cdot \mathbf{x}_i + b)) = - (error) $$

由于有：

$$ \mathbf{w} \leftarrow \mathbf{w} - \eta \cdot \nabla_{\mathbf{w}} J^{(i)} $$

$$ b \leftarrow b - \eta \cdot \nabla_{b} J^{(i)} $$

所以：

$$ \mathbf{w} \leftarrow \mathbf{w} - \eta \cdot (-\ error \cdot \mathbf{x}) = \mathbf{w} + \eta \cdot error \cdot \mathbf{x} $$

$$ b \leftarrow b - \eta \cdot (-\ error) = b + \eta \cdot error $$


复杂度主要来源于内层循环的迭代次数和每次迭代的计算成本。

**单样本梯度计算复杂度**：$O(m)$，一个样本在所有维度上的初等计算；

在**训练阶段**，我们记 需要训练 $n_{epoch}$ 次。每次 epoch 都需要处理所有 $n$ 个样本。


**训练阶段总复杂度：$O(n_{epoch} \cdot n \cdot m)$**

推理阶段，依然只需要计算一个输入在所有维度的数值，所以是 $O(m)$

### 与解析解的对比

| 特性           | 随机梯度下降 (SGD)                             | 最小二乘法 (闭式解)                                            |
| :------------- | :--------------------------------------------- | :------------------------------------------------------------- |
| **训练复杂度** | $O(T \cdot n \cdot m)$                         | $O(n \cdot m^2 + m^3)$                                         |
| **推理复杂度** | $O(m)$                                         | $O(m)$                                                         |
| **适用场景**   | **$n$ 很大**，**$m$ 很大**（在线学习、大数据） | **$m$ 较小**（$m < 1000$），$n$ 可大可小                       |
| **内存需求**   | **低**，每次处理一个样本                       | **高**，需在内存中构建 $X^TX$ ($m \times m$ 矩阵)              |
| **额外优势**   | 易于实现在线学习，跳出局部极小点（非凸时）     | 得到精确解，无需担心收敛问题                                   |
| **劣势**       | 需调试学习率 $\eta$，需监控收敛，结果非精确解  | 无法处理大数据（内存限制），无法处理在线学习，$m$ 大时计算昂贵 |

<!-- ## 4. 总结与面试要点

当被问到SGD用于线性回归的复杂度时，可以这样回答：

**“随机梯度下降通过迭代方式优化线性回归的损失函数。其训练复杂度为 $O(T \cdot n \cdot m)$，其中 $T$ 是迭代次数，$n$ 是样本数，$m$ 是特征数。这意味着它的计算成本与数据规模和特征维度呈线性关系，这与最小二乘法 $O(m^3)$ 的立方关系形成鲜明对比。”**

**“因此，SGD的核心优势在于它能高效处理海量数据（$n$ 很大）或高维数据（$m$ 很大）的场景，因为它不需要将整个数据集一次性加载到内存中进行计算，并且避免了昂贵的矩阵求逆操作。但它需要手动设置学习率等超参数，并且得到的是近似解。”** -->