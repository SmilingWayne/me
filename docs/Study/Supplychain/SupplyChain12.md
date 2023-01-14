<font color = "DarkPink" size = 4 ><b>供给不确定性对安全库存的影响</b></font>

 <font color = grey size = 4>供给不确定是由包括生产延误、运输延误和质量问题在内的很多因素造成的，譬如苏伊士运河拥堵。因此前一篇笔记考虑了需求不确定下的安全库存，我们这里假定供给的提前期也是不确定的。</font>

 <font color = grey size = 4>已知下列变量:
 
 $D$：每期的平均需求
 $\sigma_D $ ：每期需求的标准差
 $L $ ：平均的<b>补货</b>提前期
 $s_L $ ：提前期的标准差

 考虑该公司采用连续盘点策略计算持有的安全库存（如果提前期内零部件的需求超过ROP，那么公司会面临零部件短缺）。提前期内的需求服从均值$D _L$，标准差为$\sigma_L$的正态分布。

$D_L = D \times L; \sigma_L = \sqrt{L\sigma^{2}_D + D^{2}s^{2}_L}$

如果用$CSL$计算安全库存，那么：

$\qquad ss = F^{-1}_s(CSL) \times \sigma_L \\
  \quad \qquad = NORMSINV(CSL) \times \sigma_L$
 </font>

<br>
<br>
<br>


---

 <font color = "blue" size = 4 ><b>聚集对安全库存的影响</b></font>

 <font color = grey size = 4>实践中，供应链有不同的库存需求水平，面对多个有需求的地区，可以选择在每一个地方存储本地库存，也可以将所有的库存集中在一个仓库中。我们对比两种方法下的安全库存。现有变量如下</font>

<font color = grey size = 4>有$k$个地区，每个地区的需求符合正态分布，
$D_i$ : 地区$i$的周需求均值, $\sigma_i$ 地区$i$的周需求标准差,$i = 1,...k$
$\rho_{ij}$:地区$i$和地区$j$的周需求协方差 $1 \leq i ≠ j \leq k $</font>

 

 <font color = grey size = 4>非聚集策略下总安全库存= $\sum^{k}_{i = 1}{F^{-1}_s{(CSL)} }\times \sqrt{L} \times \sigma_i$ </font>

<font color = grey size = 4>如果所有库存聚集在一个中央仓库，那么需要计算聚集需求的分布。聚集需求服从正态分布，均值$D^C$，标准差$\sigma^{C}_{D} $， 协方差var$(D^{C})$分别计算如下：

$ \qquad D^C = \sum^{k}_{i = 1}D_i \\
    \\
  \qquad VAR(D^C) = \sum^{k}_{i = 1}{\sigma^2_i} + 2\sum_{i > j}{\rho_{ij}\sigma_i\sigma_j}   \\
  \\
  \qquad  \sigma^{C}_D = \sqrt{VAR(D^C)}
$
</font>

<font color = grey size = 4>如果有$k$个地区的需求相互独立$(\rho_{ij} = 0)$且同分布，均值是$D$,标准差是$\sigma_D$, 上面的式子可以简化如下

$ \qquad D^C = kD \\ 
  \qquad \sigma^C_{D} = \sqrt{k}\sigma_D
  $
结合上一篇笔记可以把中央仓库所需的安全库存计算为

$ \qquad ss = F^{-1}_{S}(CSL) \times \sqrt{L} \times \sigma^{C}_D$

<br>
<br>

将库存持有成本节约除以总需求$kD$ 可以得到聚集策略带来的单位销售量的库存持有成本节约，设$H $为单位库存持有成本，此时单位库存持有成本节约为

$\qquad Save = \frac{F^{-1}_{S}(CSL) \times \sqrt{L} \times H}{D^C} \times (\sum^{k}_{i = 1}{\sigma_i} - \sigma^C_{D} )$

差值$(\sum^{k}_{i = 1}{\sigma_i} - \sigma^C_{D})$受相关系数$\rho_{ij}$的影响，相关系数越接近-1（负相关），差值越大，相关系数越接近1（正相关），差值越小。只要相关系数小于1，集聚策略就可以带来库存节约。同时可以得出以下结论：

</font>

- <font color = 'grey' size = 4>聚集策略带来的安全库存节约随着<font color = "darkpink">期望服务水平CSL的增加</font>而增加</font>
- <font color = 'grey' size = 4>聚集策略带来的安全库存节约随着<font color = "darkpink">补货提前期L的延长</font>而增加</font>
- <font color = 'grey' size = 4>聚集策略带来的安全库存节约随着<font color = "darkpink">库存持有成本H的增加</font>而增加</font>
- <font color = 'grey' size = 4>聚集策略带来的安全库存节约随着<font color = "darkpink">相关系数的增加</font>而减少</font>





-----

<font color = darkpink size = 4>案例</font>

<font color = black size = 4>汽车经销商A为服务于B地区的4个零售商供货（非聚集），每个零售店的周需求符合正态分布，均值为D= 25，标准差$\sigma_D = 5$。制造商的补货提前期平均$L = 2$周。现对比4个零售商合并整合为一个大型零售商店的可行性。假设整合后中央零售店的需求相当于所有4个区域的需求之和，经销商期望CSL=0.90，比较相关系数$\rho $在0～1之间变动时两种策略下所需的安全库存。</font>

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br><br>
<br>

---

<font color = violet size = 4>零部件通用性的价值</font>

<font color = black size = 4>汽车经销商A为服务于B地区的4个零售商供货（非聚集），每个零售店的周需求符合正态分布，均值为D= 25，标准差$\sigma_D = 5$。制造商的补货提前期平均$L = 2$周。现对比4个零售商合并整合为一个大型零售商店的可行性。假设整合后中央零售店的需求相当于所有4个区域的需求之和，经销商期望CSL=0.90，比较相关系数$\rho $在0～1之间变动时两种策略下所需的安全库存。</font>

<br>
<br>
