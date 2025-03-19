# 机器学习中常用的一些评价指标：AUC, ROC, F1 Score ...

## Confusion Matrix （混淆矩阵）

我们需要一种工具总结某种机器学习方法在测试集上的效果。此时我们可以引入混淆矩阵 （Confusion Matrix）。对于一个二分类问题，很明显有如下4种情况：

1. 原本是Postive，预测为 Positive；（**T**rue **P**ositive）
2. 原本是Negative，预测为 Negative；（**T**rue **N**egative）
3. 原本是Positive，但预测为 Negative；（**F**alse **N**egative）
4. 原本是Negative，但预测为 Positive；（**F**alse **P**ositive）

> 一种记忆方法是，上述所有的Positive 和 Negative 都是基于“预测的结果”。因此，只有当预测和实际是一样的时候，才是 True ~ ，否则是 False ~ ...

我们可以绘制出如下的图：

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202503172348747.png)

举个例子：我们用下表来展示Algo1 / Algo2 两种算法的分类效果：

| Algo1          | Act. Positive | Act.  Negative |     Algo2      | Act. Positive | Act.  Negative |
| :------------- | :-----------: | :------------: | :------------: | :-----------: | :------------: |
| Pred. Positive |      142      |       22       | Pred. Positive |      139      |       20       |
| Pred. Negative |      29       |      110       | Pred. Negative |      32       |      112       |


拓展一下。如果我们不是一个二分类问题，而是一个多分类问题，比如我们需要预测某个Item被分在哪个类中，那么，有$N$个类，就有 $N \times N$ 大小的混淆矩阵，其中的主对角线上表示分类正确的数目。

-----

## Accuracy, Recall, Precision ...

一个显而易见的事情是，我们想知道算法到底分对了多少样本，也就是，对于所有样本，有多少样本本身是Positive，分成Positive，或者本身是Negative，分成了Negative。于是我们有：

$$\dfrac{TP + TN}{TP + FP + TN + FN}$$

这就是**准确率（Accuracy）**。

现在，我们希望知道，有多少原本就是 Positive 的样本，正确地分类为了 Positive(Correctly classified)了。 此时，我们可以：这样算：

$$\dfrac{TP}{TP + FN}$$

这就是“True Positive Rate”，**真阳性率，也叫召回率 （Recall）。**

同样地，我们也希望知道，对于原本就是 Negative 的样本，有多少被错误地分为了 Positive，也就是**假阳性率** （False Positive Rate）：


$$\dfrac{FP}{FP + TN}$$

上面2点都是从样本角度出发进行划分的，我们也可以从预测算法的角度为判断依据进行划分。比如，我们想知道预测为 Positive 的样本中，有多少实际就是 Positive的，也就是：

$$\dfrac{TP}{TP + FP}$$

这个指标就是 Precision （查准率）。

---------


## ROC, AUC

以逻辑回归为例 ... 



