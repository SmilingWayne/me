**<font FACE = "楷体_GB2312" size = 7 color = crisma > 数量折扣 </font>**

-----

<font FACE = "SimHei" size = 4 color = black ></font>
<font FACE = "SimHei" size = 4 color = black ><font color = DarkBlue>数量折扣</font>(Quantity Discount)指的是当订货量达到一定数量的时候可以获得的价格折扣。譬如订购商品A，供应商提出订货量在1～100时单价为5¥，101～300时单价为4¥，300以上时单价为3¥。这也是规模经济一个比较直观的体现。</font>

<font FACE = "SimHei" size = 4 color = black >在存在数量价格折扣的情况下，EOQ模型依然适用。不过模型应用条件需要做一些调整。包含商品采购价格的总库存成本函数为:</font>

<font FACE = "" size = 5 color = black >$\qquad \qquad TC = \frac{C_oD}{Q} + \frac{C_cQ}{2} + PD$</font>

<font FACE = "SimHei" size = 4 color = black >其中$C_o$是订货成本，$C_c$ 是库存持有成本，$P$是单位商品的价格, $D$是年总需求。在EOQ基本模型中不考虑价格的影响是因为不会对最佳订货批量产生影响（见前两篇笔记的公式）。在没有折扣的情况下，PD是一个常量。成本曲线的最小点不会改变，对应相同的Q值，因此无论是否考虑价格，批量都是一样的。但是存在价格折扣，数量会和订货量有关。这就可能影响最佳订货批量。所以购买者必须在拥有价格折扣后的持有成本和EOQ成本之间做比较。</font>

<br>
<br>
<br>



-----

<center><font FACE = "SimHei" size = 6 color = Crisma >案例</font></center>

------

<font FACE = "SimHei" size = 4 color = black >如果把EOQ模型的成本-订货批量图和数量折扣结合在一起看，大致会呈现下图的状态：</font>

<font FACE = "SimHei" size = 4 color = black >此时该商店需要选择供应商提供的3种价格折扣，在订货量小于100时，订货价格是10💰，如果是100-200订货量，价格是8💰，其他情况就是价格为6💰。按照上述带数量折扣的公式，具体成本如下图中深色实线，呈现阶梯状。在实际中比这个会复杂很多，仅作示意。</font>


<img align="middle"  src = "../picx/QuantityDiscount.png" height = "50%" style = "display:table-cell">

<font FACE = "SimHei" size = 4 color = black >注意到最佳订货批量 $Q_{opt}$ 只对中间的成本曲线 $TC(d_1)$ 是可行的。并不适合最高的成本曲线 $TC$ 和最低的成本曲线 $TC(d_2)$。正在此案例中，由于不适合最低的总成本曲线，所以 $Q_{opt}$对应的总成本必须和最低总成本曲线的折扣店 $Q(d_2)$ 比较来确定最小总成本。</font>
