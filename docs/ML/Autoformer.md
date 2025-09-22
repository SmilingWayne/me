# 长周期时间序列预测：Autoformer

## Motivation

传统的时序分解方法 decomposition 可以将原始时间序列分解为更好预测的稳定内容，**但是因为预测的序列未知一般只能在数据预处理阶段使用而无法提取未来序列的内在依赖**。所以作者考虑将decomposition集成在模型中成为一种operation。

本文还观察到处于时序不同周期相同位置的子序列往往具有相同的趋势，所以作者考虑不再像self-attention一样从节点的角度下手而是计算sub-series间的相似度。

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202509222043620.png)

1. 作者提出了名为 `Autoformer` 的框架，其遵循 Transformer 的框架设计，新添加 decomposition block，提取模型中隐藏状态的内在复杂时序趋势。

2. 作者提出Auto-Correlation机制替代self-attention，其考虑sub-series间的相似度，能更好的捕捉到趋势性，不仅保证了的复杂度，也防止了信息的丢失，做到了又快又好。



## 序列分解模块

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202509222057822.png)

> 这两个部分，一个可以反应短期的波动另一个则反应长期的季节性。

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202509222059343.png)

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202509222059415.png)