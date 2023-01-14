<font color = violet size = 5>静态方法</font>

---

<font color = black size = 4>静态方法假定对于需求水平，需求趋势和季节性因素的估计不随着观察到的新需求而发生变动。如果我们假定需求的系统成分是混合型的，也就是: </font>

<font color = grey size = 4>需求的系统成分 = (需求水平 + 需求趋势) $\times$ 季节性因素 </font>

<font color = black size = 4>给定定义如下:</font>

<font color = black size = 4>$L$: $t = 0$时期剔除季节因素后的需求估计</font>

<font color = black size = 4>$T$: 需求趋势估计(每个时期的上升或下降)</font>

<font color = black size = 4>$S_t$: 时期$t$的季节性因素估计</font>

<font color = black size = 4>$D_t$: 时期$t$观察到的实际需求</font>

<font color = black size = 4>$F_t$: 时期$t$预测的需求</font>

<font color = black size = 4>我们在$t $时期对$t + l$时期的需求预测可以用下面的公式表示 </font>

$ F_{t + l} = \left[ L + (t + l)T \right] S_{t + l} $

<br>

<font color = Dark size = 5>估计需求水平和需求趋势</font>

---

<font color = black size = 4>我们记$p$ 表示每个季节周期持续的期数，例如，如果按照一年每季度周期观察需求，则周期$p = 4$</font>

<font color = black size = 4>通过分类讨论$p$的情况，可以给出静态条件下，剔除季节因素的需求$\overline{D_t}$的公式如下:</font>

$p$ 为偶数

$\overline{D_t} = \left[ D_{t - p/2} + D_{t + p/2} + \sum^{t - 1+ (p/2)}_{i = t + 1 - p-2}{2D_i} \right] / 2p$

$p$ 为奇数

$\overline{D_t} = \sum^{t + (p-1)/2}_{i= t - (p-1)/2}{D_i} / p $

<font color = black size = 4>基于长期内需求变动，我们认为去除季节性因素的需求$\overline{D_t}$和时期$t$之间存在线性关系</font>

$\overline{D_t} = L + Tt$

<font color = black size = 4>这里$T$代表剔除季节性因素需求的增长率（增长趋势），$L$ 代表需求水平或者基期剔除季节性因素的需求。我们可以用线性回归来估计剔除季节性因素需求的$L , T$。</font>

<font color = black size = 4>此时实际需求$D_t$和剔除季节性因素的需求$\overline{D_t}$之间的比例就是季节性因素的值。</font>



<br>
<br>
<br>
<br>
<br>
<br>

|  单元格   | 函数  | 对应相同单元格 |
|:---|------  | -----|
| C4  | =(B2+B6 +2*SUM(B3:B5))/8 | C5:C11 |
| D2 |=18349+A2*524|D3:D13 |
| E2  | =B2/D2 | E3:E13|


