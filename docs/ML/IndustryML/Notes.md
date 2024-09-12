# 实用机器学习 by 李沐

### 3.1 ML Model Overview 



!!! question "机器学习算法的分类"

**监督学习(supervised learning)✨**
:   基于有标记的数据进行训练，并进行预测；

    self-supervised learning: 标记是通过数据本身生成的。e.g. Bert 

半监督学习(semi-supervised learning)
:   有一部分数据有标号，有一部分数据没有标号。基于这些数据进行训练，对标号进行预测等；

无监督学习(unsupervised learning)
:    基于无标记的数据进行训练，并进行预测；GAN，cluster等；

强化学习(Reinforcement Learning)
:   基于环境进行训练，通过不断与环境交互，得到反馈reward，学习到最优策略；



!!! question "监督学习的组成"

模型(Model)
:   根据输入作出输出预测；output predicts from input 

损失函数(Loss Function)
:   衡量预测值与真实值之间的差距，用于优化模型；

目标(objective)
:   Any function to optimize during training. e.g. 使得在训练数据上的损失函数总和最小；

优化(optimization)
:   把模型中可以学习的参数找到对应的值，也就是找到最优模型参数

!!! question "监督学习的分类"

- 决策树(Decision Tree)
- 线性方法(Linear Regression)
- 核函数
- 神经网络

