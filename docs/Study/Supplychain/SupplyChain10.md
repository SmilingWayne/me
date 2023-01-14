
<font color = "darkpink" size = 4  ><b>安全库存</b></font> :  <font color = grey size = 4>在给定期间内，为了满足超出预期水平而持有的库存。</font>

<font color = "darkpink" size = 4 ><b>提前期(Lead Time)</b></font> :  <font color = grey size = 4>从发出订单到收到订单中货物的时间间隔</font>

<font color = "darkpink" size = 4 ><b>产品满足率(fr)</b></font> <font color = grey size = 4>:  指产品需求中用库存产品得到满足的比例，也就是现有库存满足产品的需求的概率。</font>


<font color = "darkpink" size = 4 ><b>周期服务水平(CSL)</b></font> :  <font color = grey size = 4>所有顾客的需求都得到满足的补货周期所占的比例，也就是一个补货周期内不缺货的概率。如果十个补货周期内有6个周期都不缺货，那么CSL就是60%。</font>

----
<font color = "darkpink" size = 4 ><b>连续盘点</b></font> :  <font color = grey size = 4>不间断地清点库存，降低到再订货点(ROP)的时候，发出订货订单。</font>

<font color = "darkpink" size = 4 ><b>周期盘点</b></font> :  <font color = grey size = 4>定期对库存状况进行盘点，当库存降低到某个阈值的时候通过补货提高库存水平，例如每周清点库存来确保现有库存+订货=某个水平</font>

<font color = "darkpink" size = 4 ><b>补货周期平均预期缺货量(ESC)</b></font> :  <font color = grey size = 4>每个补货周期内无法由现有库存满足的那部分市场需求的平均数量</font>

<br>
<br>

---

<font color = "blue" size = 4 ><b>计算给定补货策略下的<u>安全库存</u></b></font>

 <font color = grey size = 4>假设提前期$L $，每周订单需求的均值是$D $，再订货点$ROP$,  安全库存为$ss$, 有 $ss = ROP - DL $</font>

 <font color = "blue" size = 4 ><b>计算给定补货策略下的<u>周期服务水平</u></b></font>

 <font color = grey size = 4>如果提前期内的需求超过$ROP $， 那么在补货周期内就会出现缺货。我们有CSL = Prob(补货提前期$L $周内的需求 $\leq ROP$) </font>

 <font color = grey size = 4>知道补货提前期内的需求服从均值$D_L$，标准差$\sigma_L$的正态分布，在EXCEL中，我们可以按照下面这个函数计算CSL </font>

<font color = grey size = 4>=NORMDIST ( ROP, $D_L$,$\sigma_L$, 1)</font>

 <font color = "blue" size = 4 ><b>计算给定周期服务水平下的安全库存</b></font>

 <font color = grey size = 4>给定期望周期服务水平$CSL$、提前期内的需求均值$D_L$, 提前期内的需求标准差$\sigma_L$</font>

 $ \qquad  F(D_L + ss, D_L, \sigma_L) = CSL \\
 \\
 \qquad D_L + ss = F^{-1}(CSL, D_L, \sigma_L) = NORMINV(CSL, D_L, \sigma_L) 
 $
 
 <font color = grey size = 4>所以在excel中ss计算如下</font>

$ \qquad \qquad ss = F^{-1}_s(CSL) \times \sigma_L \\
\qquad \qquad \quad = F^{-1}_s(CSL) \times \sqrt{L} \sigma_D\\
\qquad \qquad \quad =NORMINV(CSL) \times \sqrt{L}\sigma_D $

----

 <font color = "blue" size = 4 ><b>计算期望满足率下的安全库存</b></font>

<font color = grey size = 4>给定期望满足率$fr$，订货批量$Q$,提前期内的需求量的标准差$\sigma_L$

可以计算出ESC ;

$ESC = -ss [ 1- F_S(\frac{ss}{\sigma_L})] + \sigma_Lf_s(\frac{ss}{\sigma_L})$

在excel中可以表示为：

$ESC = - ss [1 - NORMDIST(ss / \sigma_L, 0, 1,1)] + \sigma_D \times NORMDIST(ss/\sigma_D, 0,1,0)$

如何已知ESC求出ss呢？ 我们使用Data中的GOALSEEK方法，一直修改ss，直到ESC等于目标值再停止。
</font>

<font color = "blue" size = 4 ><b>减少补货提前期和需求不确定性的好处</b></font>

<font color = grey size = 4>这一部分是对比实验。公式就是上面的

$ss = NORMSINV(CSL) \times \sqrt{L}\sigma_D$

尝试缩短补货提前期/降低预测误差，最终发现所需产品的安全库存均有大幅度的降低。</font>

<font color = grey size = 4></font>

<br>
<br>
<br>

|  单元格   | 函数  | 对应相同单元格 |
|:---|------  | -----|
| F3  | =A3*B3 | F4:F7,E10:E14 |
| G3  | =SQRT(B3)*E3|G4:G7 |
| H3  | =NORMSINV(D3)*G3 | D4:H7|
| H10 | =-G10*(1-NORMDIST(G10/E10,0,1,1))<br>+E10*NORMDIST(G10/E10,0,1,0) |H11:H14|
|E17 | =NORMSINV(C17)*SQRT(B17)*D17 |E18:E21|


<br>
<br>

<br>
<br>
<br>
<br>

<br>
<br>
<br>


---
