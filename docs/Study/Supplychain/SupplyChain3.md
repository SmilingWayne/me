<h2 color = darkpink>自适应时间序列预测</h2>

------

<font color = black size = 4>在自适应时间序列预测方法下， 需求水平、需求趋势和季节因素在每一次观察到实际需求之后都要进行更新。</font>

<font color = black size = 4>我们定义下面的概念：</font>

<font color = black size = 4>$L_t $ 时期$t$期末的预计需求水平</font>

<font color = black size = 4>$T_t $ 时期$t$期末的预计需求趋势</font>

<font color = black size = 4>$S_t $ 时期$t$的预计季节性因素</font>

<font color = black size = 4>$F_t $ 时期$t$的预期需求（在$t - 1$时刻或者之前作出的）</font>

<font color = black size = 4>$D_t $ 时期$t$观察到的实际需求</font>

<font color = black size = 4>$E_t = F_t - D_t$ 预测误差</font>

<font color = black size = 4>使用自适应方法，在时刻$t$对时期$t - 1$利用$t$的预计需求水平和需求趋势$L_t, T_t$ 进行预测，公式为<br><br>$F_{t + 1} = (L_t + lT_t)S_{t+1}$</font>
<br>
<br>
<br>
<br>

----

<font color = darkpink size = 4 bold FACE = "KAI">自适应时间序列预测的四大步骤</font>

1. <font color = Navy size = 4>**初始化**:根据给定数据计算$L_0, T_0$, 和季节性因素$S_1,S_2...S_p$的初始值。</font>

2. <font color = Navy size = 4>**预测**:给定时期$t$的估计值，估计时期$t + l$的需求。这里首先要用0时刻的需求水平等来预测时期1的需求</font>

3. <font color = Navy size = 4>**估计误差**:记录到时期$t + 1$的实际需求$D_{t + 1}$，然后计算时期$t + 1$的预测误差$E_{t + 1}$，也就是预测需求和实际需求之间的差距。即为$E_{t + 1} = F_{t +1} - D_{t + 1}$</font>
4. <font color = Navy size = 4>**修正误差**:借助3的预测误差，修正需求水平$L_{t + 1}$、需求趋势等的估计值。如果实际需求低于预测，那么最好将估计调低，否则需要相应地调高。</font>


-----

<font color = black size = 4>**移动平均法**</font>

<font color = black size = 4>当需求中没有观察到需求趋势或季节性因素的时候，采用移动平均法。</font>

<font color = black size = 4>移动平均法把最近$N$期的需求均值作为时期$t$的需求估计水平，这就是$N$的移动平均。方法如下:</font>


<font color = black size = 4>$L_t = (D_t + D_{t - 1} + ... + D_{t - N + 1} ) / N$</font>

<font color = black size = 4>此时我们对未来所有时期的预测都是一样的，都是基于当前对需求水平的预测。所以有:</font>

<font color = black size = 4>$F_{t + 1} = L_t, F_{t + n} = L_t$</font>

<font color = black size = 4>观察到时期$t + l$的需求后，我们对估计值进行如下调整：</font>

<font color = black size = 4>$L_{t + 1} = (D_{t + 1} + D_{t} + ... + D_{t - N + 2} ) /N $ </font>

<font color = black size = 4>为了计算新的移动平均值，我们只需要加入最新观察值并剔除最早的观察之，修正的移动平均值用于下一阶段的预测。</font>

<br>

-----

<font color = black size = 4>**简单指数平滑法**</font>

<font color = black size = 4>适用于需求没有可观察的需求趋势或者季节性因素的情况。需求水平的初始估计被当作历史数据的均值，给定时期1到时期$n$的需求数据，我们有 <br>$L_0 = \frac{1}{n} \sum^{n}_{t = 1}{D_t} $</font>

<font color = black size = 4>观察到时期$t + 1 $的需求$D_{t+ 1}$后， 我们对需求水平的估计值进行如下修正：$L_{t+ 1} = \alpha D_{t + 1} + (1-\alpha)L_t$, 其中$\alpha$ 是需求水平的**平滑指数**，需求水平的修正值是观察到的时期$t + 1$的需求($D_{t +1}$)和$t$时期的需求水平$L_t$的原有估计值的加权平均。因此我们可以将某个时期的需求水平表示为当前需求和上一期需求水平的函数</font>

<font color = black size = 4>$L_{t + l} = \sum^{t - l}_{n = 0}{\alpha(1-\alpha)^n D_{t + l - n} } + (1 - \alpha)^t D_l$</font>

-----

<font color = black size = 4>**趋势修正后的指数平滑法(Holt模型)**</font>

<font color = black size = 4>如果在上面讨论的方法基础上，再考虑系统成分中包括需求水平和需求趋势，但是不包括季节性因素。</font>

<font color = black size = 4>通过在需求$D_t$和时期$t$之间进行线性回归，可以得到需求水平和需求趋势的估计值 :$D_t = at + b$ </font>

<font color = black size = 4>在时期$t$，给定需求水平$L_t$和需求趋势$T_t$的估计值，未来时期的预测表示为: $F_{t + 1} = F_t + T_t$</font>

<font color = black size = 4>观察到时期$t + 1$的需求$D_t + l$后，我们对需求水平和需求趋势的估计值如下修正：</font>

<font color = black size = 4>$L_{t + 1} = \alpha D_{t + 1} + (1-\alpha)(L_t + T_t)$</font>

<font color = black size = 4>$T_{t + 1} = \beta(L_{t + 1} - L_t) + (1-\beta)T_t$</font>

<font color = black size = 4>其中$\alpha$是需求水平的平滑指数，$\beta$是需求趋势的平滑指数，两个参数取值都在0和1之间。在上面两个更新中，需求水平或需求趋势的修正的估计值都是观察之和原来的估计的加权平均。</font>

<br>

-----

<font color = black size = 4>**趋势修正和季节修正后的指数平滑法(Winter模型)**</font>

<font color = black size = 4>如果在上面讨论的方法基础上，考虑系统成分中包括需求水平和需求趋势和季节性因素。</font>

<font color = black size = 4>通过前一篇笔记发的静态时间序列预测方法，我们估计出需求水平$L_0$，需求趋势$T_0$和季节性因素(S_0, S_1, ... S_p)的初始值。</font>

<font color = black size = 4>在$t$时刻，给定需求水平$L_t$，季节性因素$S_t, S_{t + 1}... S_{t + p - 1}$，未来时期的预测可以表示为<br>$F+{t + 1} = (L_t + T_t) S_{t + 1}, F_{t + 1} = (L_t + lT_t)S_{t + 1}$</font>

<font color = black size = 4>观察到时期$t + 1$的需求$D_t + l$后，进行如下修正：</font>


<font color = black size = 4>$L_{t + 1} = \alpha D_{t + 1}/S_{t + 1} + (1-\alpha)(L_t + T_t)$</font>

<font color = black size = 4>$T_{t + 1} = \beta(L_{t + 1} - L_t) + (1-\beta)T_t$</font>

<font color = black size = 4>$S_{t+p+1} = \gamma(D_{t+1} / L_{t+1}) + (1-\gamma)S_{t+1}$</font>

<font color = black size = 4>其中$\alpha$是需求水平的平滑指数，$\beta$是需求趋势的平滑指数，$\gamma$是季节性因素的平滑指数。三个参数取值都在0和1之间。</font>


<br>
<br>


<font color = black size = 5>**时间序列模型**</font>

<font color = black size = 4>前一篇笔记介绍了用于预测商品需求数量的四种模型，具体内容这里不重复，可以看第10篇笔记。</font>

| <font color = Navy size = 4>具体模型</font> | <font color = Navy size = 4>适用场景和特性</font> |
|:----:| :---:|
|移动平均法 | 不存在需求趋势或者季节性因素|
|简单指数平滑 | 不存在需求趋势或者季节性因素|
|Holt 模型 | 存在需求趋势但是不存在季节性因素|
|Winter 模型 | 存在需求趋势和季节性因素|


<font color = black size = 5>**预测误差分析**</font>

<font color = black size = 4>我们定义时期$t$的预测误差$E_t$为$E_t = F_t - D_t$.也就是预测值和实际值的差。</font>

<font color = black size = 4>用来度量时期$t$的预测误差的一种方法是**平均误差(MSE)**，计算公式为$MSE_t = \frac{1}{n}\sum^{n}_{t = 1}{E^{2}_t}$.也可以把$n$替换成$n - 1$。</font>

<font color = black size = 4>由于MSE会放大那些比较大的误差（因为开方了），所以另一种评价方式是使用绝对误差$A_t = | E_t |$，也就是误差的绝对值。</font>


<font color = black size = 4>相对应的，平均绝对误差$MAD_t = \frac{1}{n}\sum^{n}_{t = 1}{A_t}$</font>

<font color = black size = 4>假设随机成分服从正态分布，那么MAD可以用来估计随机成分的标准差。此时随机成分的标准差是$\sigma = 1.25 MAD $</font>

<font color = black size = 4>还有一些其他误差评价方法比如乖离率(bias)偏差等等。这里不赘述。</font>

----

<font color = black size = 5>**案例分析（建议结合后面的图来看）**</font>

<font color = black size = 4>根据上面的总结我们很容易看出，Winter模型能考虑季节因素也考虑需求变化，但是我们先把四种方法逐一尝试，看一下结果⚠️ 案例来源：《供应链管理：战略、计划与运作》</font>


<font color = black size = 5>**移动平均法**</font>

<font color = black size = 4>第一张图展示了移动平均法的效果。K列的TS处于$\pm6$的范围内。说明预测结果不包含显著的偏离率。然而它MAD较大，有9000+，从图中可见，$L_12 = 24500$，所以后续四个时期的估计值都是24500.此时的预测误差的标准差有12148.误差较大。</font>

<font color = black size = 5>**简单指数平滑**</font>

<font color = black size = 4>第二张图展示了简单指数平滑法($\alpha = 0.1$)。这里的参数可以具体调整。初始需求水平是需求均值22083。更新结果如图所示。同样具有较小的TS，但是MAD同样较大，超过了10000.按照这样计算，预测误差估计会达到12761.误差较大</font>



<font color = black size = 5>**Holt模型**</font>

<font color = black size = 4>首先对现有数据回归，得到$L_0, T_0$的结果，我们设定$\alpha  = 0.1, \beta = 0.2$，对现有的12个季度的每一个数据进行预测，更新需求水平，并动态地调整需求趋势。结果如图三所示。此时同样有较小的偏离率，MAD也有所下降，到8836左右，这意味着较小的标准差估计值（11045）并且获得了最新参数$L_{12} = 30443, T_{12} = 1541$， 基于这两个参数可以获得未来的预测<br>$F_{13} = L_{12} + T_{12}, $<br>$F_{14} = L_{12} + 2T_{12}$</font>



<font color = black size = 5>**Winter模型**</font>

<font color = black size = 4>首先估计初始需求水平和初始需求趋势以及季节性因素，建立线性回归。然后利用Winter模型（$\alpha  = 0.1, \beta = 0.2, \gamma = 0.1$，对现有的12个季度的每一个数据进行预测。在本例中，MAD降到1469，远低于其他方法。基于此可以获得未来的预测<br>$F_{13} = (L_{12} + T_{12})S_{13}, $<br>$F_{14} = (L_{12} + 2T_{12})S_{14}$...</font>


<font color = black size = 4>综上所述，团队采用Winter模型，预测结果为：第二季度11940，第三季度17579，第四季度30930，第二年第一季度44928。预测标准差是1836</font>

<br>
<br><br>

<br>
<br>
<br>
<br>
<br>
<br>








