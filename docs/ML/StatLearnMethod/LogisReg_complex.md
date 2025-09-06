# 逻辑回归的复杂度分析

## 二分类 ｜ 正则化 ｜ 复杂度

这是一个非常经典且重要的面试考点。逻辑回归虽然名字中有“回归”，但它是一个解决**二（多）分类**问题的线性模型。==它的核心思想是：**利用一个线性函数（决策函数）的输出，再通过一个Sigmoid激活函数，将其映射到(0, 1)区间，将这个值解释为“样本属于正类的概率”。**==

*   **决策函数**：首先，和线性回归一样，计算一个线性得分。

$$ z = \mathbf{w} \cdot \mathbf{x} + b $$

*   **Sigmoid函数**：然后将得分 $z$ 输入Sigmoid函数，将其压缩到(0, 1)之间。

$$ \sigma(z) = \frac{1}{1 + e^{-z}} $$

Sigmoid函数的输出可以直观地解释为概率：$P(y=1 | \mathbf{x}; \mathbf{w}, b) = \sigma(z)$。

*   **最终预测函数**：

$$ \hat{y} = P(y=1 | \mathbf{x}; \mathbf{w}, b) = \sigma(\mathbf{w} \cdot \mathbf{x} + b) = \frac{1}{1 + e^{-(\mathbf{w} \cdot \mathbf{x} + b)}} $$

**决策边界**：逻辑回归的决策边界是一个**线性**超平面。当 $P(y=1 | \mathbf{x}) >= 0.5$ 时，预测为正类（1），这等价于 $\mathbf{w} \cdot \mathbf{x} + b >= 0$。反之，预测为负类（0）。

### 损失函数：极大似然估计（MLE）

!!! question "为什么不能像SGD解决LR一样用MSE作为损失函数？？"
    
    我们不能使用均方误差（MSE）作为损失函数，因为套用Sigmoid后的输出空间是非凸的，**使用MSE会导致很多局部最优点**。


我们转而使用**极大似然估计**来推导损失函数。==思想是：**找到一组参数 $\mathbf{w}, b$，使得在这组参数下，我们观测到的当前这批训练数据的真实标签出现的“可能性”最大。**==

### 似然函数

对于二分类问题，一个样本的标签 $y_i$ 服从伯努利分布。我们可以将**所有样本的联合概率（即似然函数）** 写为：

$$ L(\mathbf{w}, b) = \prod_{i=1}^{n} P(y^{(i)} | \mathbf{x}^{(i)}; \mathbf{w}, b) = \prod_{i=1}^{n} (\hat{y}^{(i)})^{y^{(i)}} (1 - \hat{y}^{(i)})^{(1 - y^{(i)})} $$

*   当 $y^{(i)} = 1$ 时，我们希望 $\hat{y}^{(i)}$（即预测为1的概率）越大越好。
*   当 $y^{(i)} = 0$ 时，我们希望 $1 - \hat{y}^{(i)}$（即预测为0的概率）越大越好。

这个乘积形式完美地融合了这两种情况。

---

### 交叉熵

直接最大化似然函数 $L$ 通常很困难，因为它是一个连乘的形式。我们通常取其对数，转换为**对数似然函数** $\ell$（因为对数函数是单调的，最大化 $\ell$ 等价于最大化 $L$）。

$$ \ell(\mathbf{w}, b) = \log L(\mathbf{w}, b) = \sum_{i=1}^{n} \left[ y^{(i)} \log(\hat{y}^{(i)}) + (1 - y^{(i)}) \log(1 - \hat{y}^{(i)}) \right] $$

==在机器学习中，我们习惯于**最小化**一个损失函数。因此，我们对对数似然取负，得到**负对数似然损失**，也常被称为**交叉熵损失**或**Log Loss**==。

注意，<span style="color:red">这里最前面有一个负号。我们最小化这个似然函数的负数，就等于最大化这个似然函数了</span>。

$$ J(\mathbf{w}, b) = -\ell(\mathbf{w}, b) = -\sum_{i=1}^{n} \left[ y^{(i)} \log(\hat{y}^{(i)}) + (1 - y^{(i)}) \log(1 - \hat{y}^{(i)}) \right] $$

**我们的目标从“最大化似然”转变为“最小化这个交叉熵损失函数”。**

> 为什么交叉熵是这么写。我们想要最大化似然函数，就是要在：样本为真 （1） 的时候，我们预测的值也要尽可能地大 （ $\hat{y}^{(i)}$ 要尽可能地大），样本为阴（0）的时候，我们预测的值 ($\hat{y}^{(i)}$) 要尽可能地小，也就是 $\log(1 - \hat{y}^{(i)})$ 要尽可能地大。
> 

---

### 随机梯度下降


我们需要计算损失函数 $J$ 关于参数 $\mathbf{w}$ 和 $b$ 的梯度。


推导过程会用到链式法则，我们一步一步推导。

1.  **计算Sigmoid函数的导数**（这是一个非常有用的特性）：

$$ \frac{d\sigma(z)}{dz} = \sigma(z)(1 - \sigma(z)) $$

> 该说不说，这其实也是个很重要的公式...

2.  **定义单个样本的损失**：


$$ L^{(i)} = - \left[ y^{(i)} \log(\hat{y}^{(i)}) + (1 - y^{(i)}) \log(1 - \hat{y}^{(i)}) \right] $$

其中 $\hat{y}^{(i)} = \sigma(z^{(i)})$, $z^{(i)} = \mathbf{w} \cdot \mathbf{x}^{(i)} + b$.

3.  **计算梯度 $\frac{\partial L^{(i)}}{\partial w_j}$**（对某个权重分量）：


$$ \frac{\partial L^{(i)}}{\partial w_j} = \frac{\partial L^{(i)}}{\partial \hat{y}^{(i)}} \cdot \frac{\partial \hat{y}^{(i)}}{\partial z^{(i)}} \cdot \frac{\partial z^{(i)}}{\partial w_j} $$

*   $\frac{\partial L^{(i)}}{\partial \hat{y}^{(i)}} = -\frac{y^{(i)}}{\hat{y}^{(i)}} + \frac{1 - y^{(i)}}{1 - \hat{y}^{(i)}}$

*   $\frac{\partial \hat{y}^{(i)}}{\partial z^{(i)}} = \hat{y}^{(i)}(1 - \hat{y}^{(i)})$ （Sigmoid求导）

*   $\frac{\partial z^{(i)}}{\partial w_j} = x_j^{(i)}$

将三项相乘，得到一个非常简洁的结果：

$$ \frac{\partial L^{(i)}}{\partial w_j} = (\hat{y}^{(i)} - y^{(i)}) x_j^{(i)} $$

4.  **计算梯度 $\frac{\partial L^{(i)}}{\partial b}$**：
    推导过程类似，最后一项 $\frac{\partial z^{(i)}}{\partial b} = 1$，所以：
    
$$ \frac{\partial L^{(i)}}{\partial b} = \hat{y}^{(i)} - y^{(i)} $$

5.  **得到整体梯度**：
    整个训练集的损失 $J$ 是所有 $L^{(i)}$ 的平均，因此梯度也是平均：

$$ \frac{\partial J}{\partial w_j} = \frac{1}{n} \sum_{i=1}^{n} (\hat{y}^{(i)} - y^{(i)}) x_j^{(i)} $$


$$ \frac{\partial J}{\partial b} = \frac{1}{n} \sum_{i=1}^{n} (\hat{y}^{(i)} - y^{(i)}) $$

**这个结果在形式上与线性回归的梯度惊人地相似** 。

### 参数更新规则

有了梯度，就可以用梯度下降法更新参数了（以批量梯度下降为例）：

$$ w_j \leftarrow w_j - \eta \frac{\partial J}{\partial w_j} = w_j - \eta \frac{1}{n} \sum_{i=1}^{n} (\hat{y}^{(i)} - y^{(i)}) x_j^{(i)} $$

$$ b \leftarrow b - \eta \frac{\partial J}{\partial b} = b - \eta \frac{1}{n} \sum_{i=1}^{n} (\hat{y}^{(i)} - y^{(i)}) $$

其中 $\eta$ 是学习率。

---

### 流程

1.  **初始化**：初始化参数 $\mathbf{w}$, $b$。
2.  **前向传播**：对于给定的输入 $\mathbf{X}$，计算模型预测 $\mathbf{\hat{y}} = \sigma(\mathbf{X} \mathbf{w} + b)$。
3.  **计算损失**：根据预测值 $\mathbf{\hat{y}}$ 和真实标签 $\mathbf{y}$，计算交叉熵损失 $J$。
4.  **反向传播**：计算损失函数关于参数的梯度 $\frac{\partial J}{\partial \mathbf{w}}$ 和 $\frac{\partial J}{\partial b}$。
5.  **参数更新**：使用梯度下降法更新参数。
6.  **重复**：重复步骤2-5，直到损失收敛或达到最大迭代次数。

---
好的，正则化是机器学习中一个非常重要且常见的概念，用于控制模型复杂度并防止过拟合。我们来详细拆解一下L1和L2正则化。

### 正则化（Regularization）


**问题：过拟合（Overfitting）**：==模型在训练集上表现非常好，但在未见过的测试集上表现很差。这意味着模型过度学习了训练数据中的细节和噪声，而不是其内在的通用规律。模型变得过于复杂==。

**正则化**：通过在损失函数中**添加一个额外的惩罚项**，来对模型的复杂度施加“惩罚”。这个惩罚项会偏好更小的参数值，从而**限制模型的复杂度**，鼓励模型变得更简单、更平滑，最终提升其泛化能力。


---

### L1正则化（Lasso Regression）

*   **惩罚项**：添加了权重向量 $\mathbf{w}$ 的 **L1范数**（即所有权重分量的绝对值之和）。

$$ \text{Penalty} = \lambda ||\mathbf{w}||_1 = \lambda \sum_{j=1}^{m} |w_j| $$


加入L1正则化项后，损失函数变为：

$$ J_{\text{reg}}(\mathbf{w}, b) = J(\mathbf{w}, b) + \lambda ||\mathbf{w}||_1 = J(\mathbf{w}, b) + \lambda \sum_{j=1}^{m} |w_j| $$

其中：
- $\lambda$ 是正则化强度超参数
- $||\mathbf{w}||_1$ 是权重向量的L1范数（各分量绝对值之和）
- 注意：通常**不对偏置项 $b$ 进行正则化**

!!! quote "作用与特点"
    *   **核心作用**：L1正则化不仅会限制模型复杂度，更关键的是它能产生**稀疏解（Sparse Solution）**。这意味着它会**自动进行特征选择**，会将许多不重要的特征的权重直接**压缩到0**。
    *   **为何能产生稀疏性**：从几何角度理解，L1惩罚的等高线是“尖”的（菱形），更容易与损失函数等高线在坐标轴上相交，从而使得某些权重为0。


L1正则化的一个关键特点是==绝对值函数在零点不可导==，这导致我们需要使用**次梯度（subgradient）** 的概念。


$$ \frac{\partial J_{\text{reg}}}{\partial w_j} = \frac{\partial J}{\partial w_j} + \frac{\partial}{\partial w_j} \left( \lambda \sum_{k=1}^{m} |w_k| \right) $$

第一项是原始损失函数的梯度：

$$ \frac{\partial J}{\partial w_j} = \frac{1}{n} \sum_{i=1}^{n} (\hat{y}^{(i)} - y^{(i)}) x_j^{(i)} $$

第二项是正则化项的梯度。由于绝对值函数在 $w_j = 0$ 处不可导，我们使用次梯度：

$$ \frac{\partial |w_j|}{\partial w_j} = 
\begin{cases} 
1 & \text{if } w_j > 0 \\
-1 & \text{if } w_j < 0 \\
[-1, 1] & \text{if } w_j = 0 
\end{cases} $$

在实际应用中，通常选择一个确定的次梯度值，常见的选择是：

$$ \frac{\partial |w_j|}{\partial w_j} = \text{sign}(w_j) $$

其中 $\text{sign}(w_j)$ 是符号函数，定义为：

$$ \text{sign}(w_j) = 
\begin{cases} 
1 & \text{if } w_j > 0 \\
0 & \text{if } w_j = 0 \\
-1 & \text{if } w_j < 0 
\end{cases} $$

因此，组合起来：

$$ \frac{\partial J_{\text{reg}}}{\partial w_j} = \frac{1}{n} \sum_{i=1}^{n} (\hat{y}^{(i)} - y^{(i)}) x_j^{(i)} + \lambda \cdot \text{sign}(w_j) $$


由于正则化项不包含 $b$，所以偏置项的梯度保持不变：

$$ \frac{\partial J_{\text{reg}}}{\partial b} = \frac{\partial J}{\partial b} = \frac{1}{n} \sum_{i=1}^{n} (\hat{y}^{(i)} - y^{(i)}) $$


现在，我们来看L1正则化如何影响梯度下降的参数更新规则。

$$ w_j \leftarrow w_j - \eta \frac{\partial J_{\text{reg}}}{\partial w_j} = w_j - \eta \left[ \frac{1}{n} \sum_{i=1}^{n} (\hat{y}^{(i)} - y^{(i)}) x_j^{(i)} + \lambda \cdot \text{sign}(w_j) \right] $$

$$ b \leftarrow b - \eta \frac{\partial J_{\text{reg}}}{\partial b} = b - \eta \cdot \frac{1}{n} \sum_{i=1}^{n} (\hat{y}^{(i)} - y^{(i)}) $$

我们可以将权重更新规则重新排列：

$$ w_j \leftarrow w_j - \eta \cdot \frac{1}{n} \sum_{i=1}^{n} (\hat{y}^{(i)} - y^{(i)}) x_j^{(i)} - \eta \lambda \cdot \text{sign}(w_j) $$


从上面的更新规则可以看出L1正则化的独特作用：

==与L2正则化的权重衰减效应不同，L1正则化在每次更新时添加的是一个**常数大小**的项 $\eta \lambda \cdot \text{sign}(w_j)$，而不是与权重值成比例的项==。

这意味着：
- 如果 $w_j > 0$，更新中会减去 $\eta \lambda$
- 如果 $w_j < 0$，更新中会加上 $\eta \lambda$
- 如果 $w_j = 0$，符号函数的不连续性使得我们需要特殊处理

!!! quote "为什么L1正则化可能导致稀疏？"

    L1正则化倾向于产生稀疏权重向量（即许多权重恰好为0），这是它的核心特性。原因如下：

    当 $|w_j|$ 很小时，原始损失函数的梯度 $\frac{\partial J}{\partial w_j}$ 可能也很小，但L1正则化的梯度 $\lambda \cdot \text{sign}(w_j)$ 是常数大小的（$\pm \lambda$）。

    考虑以下情况：
    
    1. 如果 $|\frac{\partial J}{\partial w_j}| < \lambda$，那么正则化项会主导更新方向
    2. 对于正权重：$w_j$ 会不断减小，直到可能变为负值
    3. 对于负权重：$w_j$ 会不断增大，直到可能变为正值
    4. 这种"震荡"最终会导致许多权重被**精确地推向了0**

    在实际实现中，当权重值很小时，我们通常会将其精确设置为0，从而实现特征选择——即完全移除对模型预测没有贡献的特征。


L1正则化的更新可以看作一种"软阈值"（soft thresholding）操作：
$$ w_j \leftarrow \text{sign}(w_j) \cdot \max(0, |w_j| - \eta \lambda) + \text{其他项} $$

这直观地显示了L1正则化如何产生稀疏性：它在每一步都将权重向零收缩一个固定量 $\eta \lambda$，如果权重的绝对值小于这个量，它就会被设置为零。

---


### L2正则化（Ridge Regression）

*   **惩罚项**：添加了权重向量 $\mathbf{w}$ 的 **L2范数**的平方（即所有权重分量的平方和）。

$$ \text{Penalty} = \frac{\lambda}{2} ||\mathbf{w}||_2^2 = \frac{\lambda}{2} \sum_{j=1}^{m} w_j^2 $$

*   $\lambda$ 是一个超参数，称为**正则化强度**。$\lambda$ 越大，对大幅值的权重惩罚就越重，模型就越简单。
*   $\frac{1}{2}$ 是为了后续求导方便，常数项不影响优化本质。

*   **完整的损失函数（以逻辑回归为例）**：

$$ -\sum_{i=1}^{n} \left[ y^{(i)} \log(\hat{y}^{(i)}) + (1 - y^{(i)}) \log(1 - \hat{y}^{(i)}) \right] + \frac{\lambda}{2} ||\mathbf{w}||_2^2 $$

我们将以逻辑回归为例，详细推导L2正则化如何影响梯度下降算法。

$$ J_{\text{reg}}(\mathbf{w}, b) = J(\mathbf{w}, b) + \frac{\lambda}{2} ||\mathbf{w}||_2^2 = J(\mathbf{w}, b) + \frac{\lambda}{2} \sum_{j=1}^{m} w_j^2 $$

其中：
- $\lambda$ 是正则化强度超参数
- $\frac{1}{2}$ 是为了后续求导方便（与平方项的导数中的2抵消）
- 注意：通常**不对偏置项 $b$ 进行正则化**，因为我们希望模型能够学习数据的整体偏移

我们的目标是计算带有L2正则化的损失函数关于参数 $\mathbf{w}$ 和 $b$ 的梯度。

### 带正则化的梯度计算

$$ \frac{\partial J_{\text{reg}}}{\partial w_j} = \frac{\partial J}{\partial w_j} + \frac{\partial}{\partial w_j} \left( \frac{\lambda}{2} \sum_{k=1}^{m} w_k^2 \right) $$

第一项是<span style="color:red">原始损失函数的梯度</span>，我们之前已经推导过：

$$ \frac{\partial J}{\partial w_j} = \frac{1}{n} \sum_{i=1}^{n} (\hat{y}^{(i)} - y^{(i)}) x_j^{(i)} $$

第二项是<span style="color:red">正则化项的梯度</span>：

$$ \frac{\partial}{\partial w_j} \left( \frac{\lambda}{2} \sum_{k=1}^{m} w_k^2 \right) = \frac{\lambda}{2} \cdot 2w_j = \lambda w_j $$

因此，组合起来：

$$ \frac{\partial J_{\text{reg}}}{\partial w_j} = \frac{1}{n} \sum_{i=1}^{n} (\hat{y}^{(i)} - y^{(i)}) x_j^{(i)} + \lambda w_j $$


由于正则化项不包含 $b$，所以偏置项的梯度保持不变：

$$ \frac{\partial J_{\text{reg}}}{\partial b} = \frac{\partial J}{\partial b} = \frac{1}{n} \sum_{i=1}^{n} (\hat{y}^{(i)} - y^{(i)}) $$

现在，我们来看L2正则化如何影响梯度下降的参数更新规则。

<!-- ### 3.1 原始梯度下降更新（无正则化）

$$ w_j \leftarrow w_j - \eta \frac{\partial J}{\partial w_j} = w_j - \eta \cdot \frac{1}{n} \sum_{i=1}^{n} (\hat{y}^{(i)} - y^{(i)}) x_j^{(i)} $$
$$ b \leftarrow b - \eta \frac{\partial J}{\partial b} = b - \eta \cdot \frac{1}{n} \sum_{i=1}^{n} (\hat{y}^{(i)} - y^{(i)}) $$ -->

$$ w_j \leftarrow w_j - \eta \frac{\partial J_{\text{reg}}}{\partial w_j} = w_j - \eta \left[ \frac{1}{n} \sum_{i=1}^{n} (\hat{y}^{(i)} - y^{(i)}) x_j^{(i)} + \lambda w_j \right] $$

$$ b \leftarrow b - \eta \frac{\partial J_{\text{reg}}}{\partial b} = b - \eta \cdot \frac{1}{n} \sum_{i=1}^{n} (\hat{y}^{(i)} - y^{(i)}) $$

我们可以将权重更新规则重新排列，以更清楚地看到L2正则化的影响：

$$ w_j \leftarrow { w_j (1 - \eta \lambda) - \eta} \cdot \frac{1}{n}  \sum_{i=1}^{n} (\hat{y}^{(i)} - y^{(i)}) x_j^{(i)} $$



!!! quote "作用与别名"
    *   **作用**：L2正则化会**倾向于让所有权重值都变小**，并趋向于0（但通常不会精确地等于0）。它使得模型的输出函数更加平滑，对输入特征的变化不那么敏感，从而有效防止过拟合。
    *   **别名**：权重衰减（Weight Decay）。在梯度下降的更新公式中，可以看到权重会不断地乘以一个小于1的因子，像“衰减”一样。



从上面的更新规则可以看出L2正则化的核心作用：

**在每次更新时，L2正则化会先让权重 $w_j$ 乘以一个小于1的因子 $(1 - \eta \lambda)$，然后再进行正常的梯度更新。**

这就是为什么L2正则化又被称为"权重衰减"（Weight Decay）的原因。它有效地在每一步都让权重向零缩小，防止权重变得过大。

### 为什么L2正则化能防止过拟合

!!! question "为什么L2正则化能防止过拟合"

    1. **限制模型复杂度**：通过惩罚大权重，L2正则化鼓励模型使用所有特征但每个特征的贡献都很小，而不是依赖少数几个特征及其大权重。这使模型更加稳定，对输入数据中的小变化不那么敏感。

    2. **改善条件数**：从数值计算的角度，L2正则化通过向 $X^TX$ 矩阵添加 $\lambda I$ 来改善其条件数，使矩阵求逆更加稳定。
    
    $$ (X^TX + \lambda I)^{-1} X^T y $$

    这在解析解中更为明显，但也影响了梯度下降的优化过程。

---

### ==复杂度分析==

利用随机梯度下降进行计算，此时对每个样本进行梯度下降更新权重时依然只需要计算它的各个特征的梯度，也就是 $O(m)$，那么假设迭代次数 $n_{epoch}$，样本数 $n$，此时，训练阶段，逻辑回归的算法复杂度就是 $O(n_{epoch} m n)$。不管如何进行正则化，复杂度都是这个。

而推理阶段的算法复杂度就是 $O(m)$.



### 5. 总结

在逻辑回归（以及大多数线性模型）中，L2正则化通过以下方式影响梯度下降：

1. 在损失函数中添加 $\frac{\lambda}{2} ||\mathbf{w}||_2^2$ 项
2. 这导致权重梯度中增加了一个 $\lambda w_j$ 项
3. 权重更新规则变为：$w_j \leftarrow w_j (1 - \eta \lambda) - \eta \cdot \text{原始梯度}$
4. 这种"权重衰减"效应防止权重变得过大，从而控制模型复杂度，防止过拟合
5. 偏置项 $b$ 通常不受正则化影响

理解这一推导过程对于掌握机器学习中的正则化概念至关重要，也是面试中常见的问题。


<!-- ---

## 4. L1 vs L2 正则化对比总结

| 特性         | L1 正则化 (Lasso)                    | L2 正则化 (Ridge)                          |
| :----------- | :----------------------------------- | :----------------------------------------- |
| **惩罚项**   | $\lambda \|\|\mathbf{w}\|\|_1$       | $\frac{\lambda}{2} \|\|\mathbf{w}\|\|_2^2$ |
| **解的性质** | **稀疏解**                           | **非稀疏解**                               |
| **特征选择** | **内置特征选择**，会产生稀疏模型     | 无特征选择，保留所有特征                   |
| **权重趋向** | 将不重要特征的权重**压缩至0**        | 将所有权重**均匀地缩小**                   |
| **别名**     | Lasso Regression                     | Ridge Regression, Weight Decay             |
| **几何解释** | 与损失函数等高线在**坐标轴**上相交   | 与损失函数等高线在**某个点**上相切         |
| **计算**     | 在零点不可导，优化更复杂（需次梯度） | 处处可导，优化简单                         |

### 可视化理解
想象一个只有两个权重 $(w_1, w_2)$ 的模型。
*   **L2** 的约束区域是一个**圆形**。最优解更容易落在“圆”的边界上，使得 $w_1$ 和 $w_2$ 都变小但不为0。
*   **L1** 的约束区域是一个**菱形**。最优解更容易落在“菱形”的**角点**上，而角点往往位于坐标轴上，这意味着某个权重（如 $w_2$）会等于0。


*(这是一个经典的示意图，展示了L1和L2约束区域的形状如何导致不同的解)*

---

## 5. 弹性网络（Elastic Net）

**Elastic Net** 是L1和L2正则化的一个折中方案，同时包含两种惩罚项，旨在结合两者的优点。
$$ J(\mathbf{w})_{\text{Elastic Net}} = \frac{1}{n}\sum_{i=1}^{n}(y^{(i)} - \hat{y}^{(i)})^2 + \lambda_1 ||\mathbf{w}||_1 + \lambda_2 ||\mathbf{w}||_2^2 $$

它特别适用于特征数量远大于样本数量（$m \gg n$）或者特征之间存在高度相关性的情况。

---

## 面试回答技巧

当被问到“L1和L2正则化有什么区别”时，可以这样回答：

**“L1和L2正则化都是在损失函数中添加一个惩罚项来防止模型过拟合。它们的核心区别在于使用的范数不同，导致其作用效果有显著差异。”**

**“L2正则化，也叫权重衰减，添加的是权重的平方和。它的作用是让所有权重均匀地变小，使得模型更加平滑稳定，但不能将权重压缩到零。”**

**“L1正则化，添加的是权重的绝对值和。它的关键特性是能产生稀疏解，可以将不重要的特征对应的权重直接置为零，因此它自带特征选择的功能。在选择上，如果我们认为只有少数特征重要，就用L1；如果我们认为大部分特征都有用，只是权重不能太大，就用L2。对于非常复杂的情况，也可以使用结合两者的Elastic Net。”**

这样的回答既准确又体现了你对不同场景下技术选型的思考。

### 面试要点

!!! question ""
    1. 逻辑回归的核心优势之一是它的输出具有明确的概率意义（$P(y=1 | \mathbf{x})$），而不仅仅是类别标签。
    2. 说出为什么用交叉熵损失而不是MSE（非凸、梯度消失等问题）
    3. **正则化**：为了防止过拟合，几乎总是在损失函数中加入正则化项（L1或L2）。L1正则化可以产生稀疏模型，L2正则化更常用。 -->
