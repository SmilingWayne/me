# Logistic Regression

一种传统统计学和机器学习中常用的方法。 我们回顾一下线性回归：

给定两个（多个）指标构成的一组点，拟合一条线，我们可以计算 $R^2$，查看两个指标是否相关；通过 p-value 检查是否显著；并通过这个直线进行预测。

> 尽管我们没有提及，但是，根据一系列数据预测某个数据是否落在某类当中，是很经典的机器学习的方法。所以，逻辑回归也是很经典的机器学习方法。

逻辑回归和线性回归很像，是一种广义线性模型（General Linear Model, GLM）。但是不再是预测某个连续值（比如老鼠的大小），而是预测某个事情是 `True` 还是 `False` 的概率（比如，老鼠是否肥胖的概率）。

逻辑回归，是通过逻辑函数 (Logistic Function), 一个 S 形的函数，来判断一个东西是 True，还是 False.

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202505080024035.png)

纵轴从 0 ～ 1，表示，一物在某指标下，是 **真** 的概率 (Probability)。

尽管看起来这是个判定True / False 的问题，但是大多数时候，逻辑回归被用在分类问题上。

并且，逻辑回归**不仅可以用在连续的变量（比如重量），也可以用在多个不同的变量，或者既有连续变量也有离散变量的情况下**。同样的，也有一些检验可以检查哪些变量对分类结果的影响显著，哪些不显著（Wald test）。

正因为它能够输出连续型、离散型变量下某事件为“真”的概率，所以它作为一种常见的机器学习方法，经常被使用。

不同于线性回归用 $R^2$ 衡量拟合效果，逻辑回归基于“极大似然”来进行衡量（Maximum Likelihood）。

> 一句话概括：我们给定阈值50%，如果在给定参数下曲线的纵坐标大于 50%，就判定为 True，否则 False。然后，我们找出一根曲线，利用每个样本的数值，计算它**被判定为真的概率**。然后每个样本的概率相乘，得到一个结果。我们再找出第二个曲线，如法炮制。计算出另一个结果。比较两个结果，概率更大的，也就是更好的那个曲线。

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202505080037203.png)

---

## Detail. 1 Coefficients

我们依然鞭尸一下线性回归。我们用小鼠的体重预测它的大小。如果用直线拟合，有个尴尬的事儿：哪怕小鼠重量是 0，它也有大小，甚至，哪怕它的重量是负数，它也有正数的大小。如图所示。

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202505080043845.png)


