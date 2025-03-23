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

现在，我们希望知道，有多少原本就是 Positive 的样本，正确地分类为了 Positive(Correctly classified)了，也就是**从 Positive的样本视角看**，分类器筛出了多少的比例。即：

$$\dfrac{TP}{TP + FN}$$

这就是“True Positive Rate”，**真阳性率，也叫召回率 （Recall）。**

同样地，我们也希望知道，对于原本就是 Negative 的样本，有多少被错误地分为了 Positive，也就是**假阳性率** （False Positive Rate）：


$$\dfrac{FP}{FP + TN}$$

上面2点都是从样本角度出发进行划分的，我们也可以从**预测算法的角度**为判断依据进行划分。比如，我们想知道预测为 Positive 的样本中，有多少实际就是 Positive的，也就是：

$$\dfrac{TP}{TP + FP}$$

这个指标就是 Precision （查准率）。

---------


## ROC


**ROC曲线（Receiver Operating Characteristic Curve）** 是一种用于评估==二分类模型==性能的可视化工具。它通过展示**不同分类阈值**下模型的 **真阳性率（TPR）** 和 **假阳性率（FPR）** 之间的权衡关系，帮助理解模型对正负样本的区分能力。


**横轴（FPR）**：假阳性率（False Positive Rate），即<span style="color:red">负样本中被错误预测为正样本的比例</span>，计算公式为：  

$$FPR = \frac{FP}{FP + TN}$$

**纵轴（TPR）**：真阳性率（True Positive Rate），即<span style="color:red">正样本中被正确预测的比例</span>，等价于召回率（Recall），计算公式为：  

$$TPR = \frac{TP}{TP + FN}$$

我们知道，以逻辑回归为例，模型通常输出样本属于正类的概率，也就是说，我们可以认为，概率 > 50%的，就是正样本，我们也可以认为，概率 > 60 % 的就是正样本，这里的 50%, 60% 就是**一个阈值**。对于同一个测试集，选择不同的阈值，你可以生成不同的预测结果，而对于你生成的每一个预测结果，你都可以对应计算出这个结果的**真 or 假阳性率**。

对每个阈值，计算对应的TPR和FPR，形成ROC曲线上的一个点。此时我们再连接所有点连成曲线，即为ROC曲线。

!!! note "解读"
    1. **对角线（AUC=0.5）**：表示模型无区分能力（相当于随机猜测）。
    2. **左上角（AUC=1）**：理想模型，所有正样本的预测概率均高于负样本。
    3. **曲线位置**：**曲线越靠近左上角，模型性能越好。**

### 如何画ROC曲线

!!! example "怎么画这个图呢？"
    
    第一个问题无疑是咱们应该怎么取那个阈值。一个简单的做法是根据我们在测试集上所有输出的概率来取。若模型对3个样本的预测概率为 `[0.2, 0.8, 0.6]`，候选阈值为 `[0.2, 0.8, 0.6]`。额外补充阈值 `0.0`（所有样本均判为正类）和 `1.0`（所有样本均判为负类）作为起点和终点并把前面的阈值升序排一下，就可以了，我们的阈值就是 `[0, 0.2, 0.6, 0.8, 1.0]`

    第二个问题无疑是怎么调整这个阈值。我们让阈值从 `1.0` 逐步降低到 `0.0` 即可。此时 **TPR（真阳性率）** 逐步上升（正样本被正确分类的比例提高）。**FPR（假阳性率）** 也逐步上升（负样本被误判的比例提高）。


    快速看看AUC曲线长啥样！

    ```python
    import numpy as np
    from sklearn.datasets import make_classification
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import roc_curve, roc_auc_score, RocCurveDisplay,  precision_recall_curve
    import matplotlib.pyplot as plt

    X, y = make_classification(n_samples=1000, n_features=20, n_classes=2, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    clf = LogisticRegression()  # Logistics Regression Classifier
    clf.fit(X_train, y_train)   # X_train and y_train for training
    y_score = clf.predict_proba(X_test)[:, 1]  # Predict on x_test
    fpr, tpr, thresholds = roc_curve(y_test, y_score)
    auc_score = roc_auc_score(y_test, y_score)
    display = RocCurveDisplay(fpr=fpr, tpr=tpr, roc_auc=auc_score,
                                    estimator_name='example estimator')
    display.plot()
    plt.plot([0, 1], [0, 1], linestyle='--', color='r', label='Random Classifier')  
    plt.show()
    ```



    一般而言，AUC曲线是呈阶梯状增加的，也就是在相邻两点之间，若FPR或TPR发生变化，则通过线性插值连接。最终曲线呈“阶梯状”，**反映阈值调整时分类结果的离散跳跃。**

    ![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202503232203113.png)

    为什么会出现这样的图像呢？

    我们可以验证一下，比如我们取出上面所有的预测概率值并且从大到小排序。我们基于这些概率分别计算 TPR， FPR。手撕代码如下：

    ```python
    def manual_tpr_fpr(y_true, y_pred_prob, threshold):
        y_pred = np.where(y_pred_prob >= threshold, 1, 0)
        # Get TP, FP, TN, FN
        tp = np.sum((y_pred == 1) & (y_true == 1))
        fp = np.sum((y_pred == 1) & (y_true == 0))
        tn = np.sum((y_pred == 0) & (y_true == 0))
        fn = np.sum((y_pred == 0) & (y_true == 1))
        
        # Get TPR, FPR ... 
        tpr = tp / (tp + fn) if (tp + fn) > 0 else 0.0
        fpr = fp / (fp + tn) if (fp + tn) > 0 else 0.0
        
        return tpr, fpr

    y_true = y_test
    for threshold in threshold_np:
        tpr, fpr = manual_tpr_fpr(y_true, y_score, threshold)
        print(round(threshold,6), round(tpr, 6), round(fpr, 6))
    ```

    其中，第一列对应阈值概率，第二列对应TPR，第三列对应FPR。结果类似：

    ```text
    0.999903 0.006452 0.0
    0.999679 0.012903 0.0
    0.999622 0.019355 0.0
    0.999499 0.025806 0.0
    0.999479 0.032258 0.0
    0.998925 0.03871 0.0
    ......
    ......
    0.018623 0.987097 0.834483
    0.018358 0.987097 0.841379
    0.016268 0.987097 0.848276
    0.016144 0.987097 0.855172
    0.015737 0.987097 0.862069
    ```

    什么意思呢，就是，不同的阈值可能对应了不同TPR，但是相同FPR，或者同一个TPR，但是不同FPR。**对于第一种情况，就类似于这段图像是一个竖直的线，对第二种情况，对应这段图像是一个水平线。** 这种情况是因为某些相邻阈值会导致相同的 TPR/FPR​，<span style="color:red">两个阈值之间无样本被重新分类</span>。正是这么多细小的线水平竖直连接起来，就构成了这么一个阶梯形状的图像。


## AUC 

但是ROC曲线本身的含义还可以进一步被挖掘。比如，我们可以计算出ROC曲线下的面积。这个值对应的是，==若随机抽取一个阳性样本和一个阴性样本，分类器判断阳性样本的值高于阴性样本的概率==。

或者，是模型正确排序一对正负样本的概率。

> 如果模型对正样本的预测概率为0.8，对负样本的预测概率为0.3，则模型**正确排序**了这两个样本。反之，如果两个样本一个 0.7, 一个 0.8，那么它并没有正确排序这两个样本。

现在，一个重要的问题来了，如何计算AUC？和ROC不同，AUC是一个值。

我们可通过梯形法则（Trapezoidal Rule）近似计算离散点的积分，也就是对阈值从高到低排序后计算每个阈值对应的FPR，TPR，然后：

$$AUC = \sum^n_{i = 1} \dfrac{(FPR_i - FPR_{i-1}) \times (TPR_i + TPR_{i - 1})}{2}$$

**注意，AUC反映模型对正负样本的排序能力，与样本数量无关。**

---

## PR-curve

PR曲线 **P**recision-**R**ecall Curve. 是另一种评估二分类模型性能的重要工具，尤其在**类别不平衡场景**下比ROC曲线更具参考价值。

### 绘制 PR curve

- **横轴（Recall）**：召回率（真阳性率），计算公式为：
  
$$TPR = \frac{TP}{TP + FN}$$

- **纵轴（Precision）**：精确率，计算公式为：
  
$$Precision = \frac{TP}{TP + FP}$$

> 注意，在ROC中TPR是纵轴，但是在PR curve中，是横轴。

绘制步骤和ROC曲线是类似的：

1. 将预测概率从高到低排序。
2. 依次将每个概率作为阈值，计算对应的Precision和Recall。
3. 连接所有点形成PR曲线。

!!! note "怎么理解"
    - **曲线形状**：呈下降趋势（阈值降低时，Recall上升，但Precision可能下降）。
    - **关键点**：
      - **右上角（Recall=1, Precision=正样本比例）**：所有样本均判为正类。
      - **左上角（Precision=1, Recall=0）**：无样本判为正类。

!!! example "PR曲线的作用"

    1. 类别不平衡场景的敏感性：当负样本远多于正样本时（如欺诈检测中99%为正常交易），ROC曲线的FPR可能被稀释（分母FP+TN过大），导致评估失真。而，Precision关注**预测为正类的准确性**（即“判为正类的样本中有多少是真的正类”）。
    
    > Recall (TPR) 关注**正样本的覆盖率**（即“真实正类中有多少被正确识别”）。两者均聚焦正样本，对类别分布不敏感。

    2. 举个例子，应用在召回正样本时，误判负样本的比例较低（高Precision）。**适用于需要减少误报的场景（如垃圾邮件过滤、医学诊断）。**

试试看！还是先前的代码，但是调个包！Give it a shot!

```python
from sklearn.metrics import PrecisionRecallDisplay
display = PrecisionRecallDisplay.from_estimator(
    clf, X_test, y_test, name="LogisticsRegression", plot_chance_level=True,
)
_ = display.ax_.set_title("2-class Precision-Recall curve")
plt.show()
```

Then you got:

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202503232341873.png)

此时你会发现，sklearn帮你算好了一个叫AP (Average Precision)的指标。实际上这个可以近似理解为**PR-AUC**，也就是这个曲线下的面积，用于量化模型在不同召回率（Recall）下的平均精确率（Precision）。其一般计算公式：

$$AP = \sum_{k=1}^{N} Precision(k) \cdot \Delta Recall(k)$$

必须说一下，sklearn 中的 `average_precision_score` 计算并不是直接使用梯形法则（基于插值），因为 “梯形规则使用线性插值，可能过于乐观。” (`is different from computing the area under the precision-recall curve with the trapezoidal rule, which uses linear interpolation and can be too optimistic`.) **因此如果你直接计算梯形面积会发现和那个值对不上。**

!!! example "结论"
    **AP > 随机基线** → 模型有效。  
    
    **AP越接近1** → 模型性能越接近完美（所有正样本预测概率高于负样本）。

罗列一下PR曲线下的AUC和ROC曲线下的区别与联系：

| **指标**    | **关注点**             | **适用场景**                   | **基线值**           |
| ----------- | ---------------------- | ------------------------------ | -------------------- |
| **AP**      | 正样本的预测准确性     | 类别不平衡（正样本稀少）       | 正样本比例（如0.52） |
| **AUC-ROC** | 正负样本的全局排序能力 | 类别均衡或需全局排序能力的任务 | 0.5（随机猜测）      |

一个简单的例子是，在医学检测中，阳性样本本身不多（正样本占比1%），若模型AP=0.8（基线AP=0.01），说明模型显著优于随机；而ROC-AUC=0.9可能因类别不平衡掩盖问题。


---

## F1 Score 


----

## Multi Class - ROC 

