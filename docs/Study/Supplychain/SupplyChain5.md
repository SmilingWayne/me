**<font FACE = "楷体_GB2312" size = 7 color = crismo > 规模经济管理：周转库存 </font>**

<font FACE = "Heiti" size = 5 color = Navy >在单个订单中订购多种产品</font>

-----


<font FACE = "" size = 4>✏️ 假设电脑商店的4种电脑都是**同一供应源**提供的，产品经理可以协调供应，使得4种电脑都是用同一种卡车送来。这种“订单聚集”实际上将固定运输成本分担到多种产品上，商店可以通过减少每种商品的订货批量实现财务上的最优。这是降低周转库存和成本的重要方法。</font>


<font FACE = "" size = 5 color = red>要点：</font><font FACE = "SimHei" size = 4 color = black>在单个订单中聚集产品，零售商或供应商的补货可以减少每种产品的订货量，因为这种做法可以将固定订货成本和运输成本分摊。</font><font FACE = "楷体_GB2312" size = 4>（可以理解为把多种产品打包运输）</font>


<font FACE = "Heiti" size = 5 color = Navy >多产品或多顾客的订货批量确定</font>

-----

<font FACE = "" size = 4>上面，包括前一篇笔记的内容都是基于一种理想化情况：运输卡车只运输同一种产品。🚛 这种情况下库存更新和重新入库的工作量要远小于装载很多种产品的一辆卡车，固定成本中与“装货/收货”相关的成本也就小于第二种情况。这里，<font color = DodgerBlue>我们探讨卡车装载多产品情况下，订单固定成本有一部分与装货收货相关时，订货批量确定的方法。</font></font>


<font FACE = "" size = 4>**前置知识与准备：**</font><font FACE = "" size = 4>基本的EOQ模型 📒 ｜ 一只计算器。</font>

<br>



<font FACE = "" size = 4>我们的目标是找到使得总成本最小化的订货批量和订货政策。假设输入如下： </font>

<font FACE = "" size = 4>$ \quad D_i $ : 产品$i$的年需求量</font>
<font FACE = "" size = 4>$ \quad S $ : 每次订货时的订货成本，与订单中产品种类无关</font>
<font FACE = "" size = 4>$ \quad s_i $ :订单中包括产品$i$时产生的额外订货成本</font>

<font FACE = "" size = 4>商店经理的决策主要有以下三种： </font>

<font FACE = "" size = 4>决策一：✅ 每个产品经理独立订购自己负责的型号</font>
<font FACE = "" size = 4>决策二：✅ 产品经理共同订购每一个批次中每一种型号的电脑</font>
<font FACE = "" size = 4>决策三：✅ 产品经理们共同订购，但是每一批次中并非都包含所有型号的电脑（也就是仅包含选定的型号组合）</font>


<font FACE = "" size = 4><font FACE = "楷体_GB2312" size = 5>案例</font>：S公司销售三种电脑 💻：L/M/H，需求分别为$D_L$, $D_M$, $D_H$ = 12000, 1200, 120, 每种电脑的价格均为500，每次订货的固定运输成本为4000，同时订购并且装载在同一个卡车上的每一种型号电脑还会因为收货和仓储多发生1000的固定成本。公司S库存持有成本时20%。</font>

**<font FACE = "楷体_GB2312" size = 5 color = Crisma >决策一：独立订购</font>**

<font FACE = "" size = 4>🌈  计算起来最简单的做法。因为三种电脑订购是相互独立的。所以只需要运用三次EOQ公式$Q = \sqrt{\frac{2DS}{hC} }$ 就可以得出结果（D代表产品需求，S是固定成本，h是库存持有成本，C是单位成本）。注意，这里“每辆卡车每一种型号电脑的仓储和收货的固定成本是1000”，意味着每次运输的固定成本是4000+1000 = 5000。最终计算结果：三种产品每年的订货/库存持有成本155140。L/M/H 的最优订货量：1095/346/110.订货频率分别为：11/3.5/1.1.</font>

----


<br>

**<font FACE = "楷体_GB2312" size = 5 color = Crisma >决策二：三种产品同时订购和运输（完全聚集）</font>**

<font FACE = "" size = 4>🌈 如果每次都定三种型号的电脑，那么每次订货的联合固定成本：$S^{*} = S + s_L + s_M + s_H$</font>

<font FACE = "" size = 4>此时年订货成本$S^{*}n$，年库存持有成本$\frac{D_LhC_L}{2n} + \frac{D_MhC_M}{2n} + \frac{D_HhC_H}{2n}$.总成本为上述两者的和。</font>

<font FACE = "" size = 4>基于总成本对n求一阶导，令其为0，可以得出最优订货频率$n^{*} = \sqrt{\frac{D_LhC_L + D_MhC_M +D_HC_H}{2S^{*} } }$。这个公式可以推广到$k$种产品的情况。这里还需要考虑卡车装载能力的问题：如果最优装载量超过了卡车运载能力，还需要提高卡车运载量。</font>

<font FACE = "" size = 4>🌈 我们假设卡车运载量足够。把上面的案例数据代入，订货成本是4000 + 1000 * 3 = 7000（因为每次运输都是三种货物一起，要把三种货物的固定卸货成本都算进来）</font>

<font FACE = "" size = 4>此时最优订货频率 $n^{*} = \sqrt{ \frac{12000 \times 100 + 1200 \times 100 + 120 \times 100}{2 \times 7000} } = 9.75 $。电脑$i$ 的最优订货批量为$D_i / n^{*} $。此时的总订货成本136528，其中，L/M/H 的订货批量为1230， 123， 12.3. 这标志了相比于第一种决策，联合订购将总成本降低了12% 。</font>

<font FACE = "" size = 4>上面的数据忽略了这样一种情况：把三种电脑都放在卡车上运输，卡车的运载量小于最优装载量。此时只能提高订货频率，降低装载量，使得装载量满足约束。</font>


<br>

----

**<font FACE = "楷体_GB2312" size = 5 color = Crisma >决策三：定制化聚集，选定产品组合的联合运输配送</font>**

<font FACE = "" size = 4>🌈 决策二是个很经典也很明显的优化。但是我们同样可以进一步协调订货。因为决策二中，三种产品的订货量每次都是相同的，如果可以定制并灵活协调每一次每种产品的订货量，甚至每一次运输不必订购全部三种产品，可以更加节约成本。</font>

<font FACE = "" size = 4>⏰ ⏰ <font color = red>（划重点）</font>我们采用如下启发式算法进行计算：</font>

1. <font FACE = "" size = 4>找出订货频率最高的产品。假设每个产品都是独立订货。此时每种产品分配的固定成本$S + S_i$. 产品 $i$的订货频率 $n_i = \sqrt{\frac{hC_iD_i}{2(S+s_i)} }$，记$n^{*} , i^{*}$为订货频率最大值和订货频率最高的产品</font>
2. <font FACE = "" size = 4>对于除了订货频率最高的其他所有产品，计算订货频率$n_i = \sqrt{\frac{hC_iD_i}{2s_i} }$。</font>
3. <font FACE = "" size = 4>我们目标是确定所有$i \neq i^{*}$的产品在整数订货次数后与最高订货频率产品$i^{*}$一起订货。因此计算相对最高订货产品，其定货频率为$m_i = \lceil n_i /n^{*} \rceil$ 。这里向上取整。</font>
4. <font FACE = "" size = 4>确定每个产品的订货频率后，重新计算最高订货频率产品$i^{*}$的订货频率$n$，即 <br></font><font FACE = "" size = 5>$ \qquad \qquad n = \sqrt{\frac{\sum^{i}_{i = 1}{hC_im_iD_i} }{2(S + \sum^{i}_{i = 1}{s_i / m_i} ) } }$</font>
5. <font FACE = "" size = 4>对于每种产品，计算订货频率$n_i = n / m_i$ 和该订货策略下的总成本。年总成本为<br>$\qquad \qquad TC = nS + \sum^{i}_{i = 1}{n_is_i} + \sum^{i}_{i = 1}{(\frac{D_i}{2n_i})hC_i}$</font>


<br>

<font FACE = "" size = 4>这种算法介绍的过程就是定制化聚集(Tailored Aggregation)，也就是高需求的产品订货频率较高，但是低需求的产品订货频率较低。</font>


<font FACE = "" size = 4>将案例数据代入上述算法计算，L/M/H的具体订货频率为11.47/5.74/2.29。订货批量分别为1046/209/52。此时的年库存成本+运输成本为130767。与决策二相比，定制化聚集节省了5716，相当于4%。</font>

<font FACE = "" size = 5 color = red>要点：</font><font FACE = "" size = 4>降低周转库存关键在于<font color = DarkGreen bold>减少订货批量。在不增加成本的前提下减少订货批量的关键是减少和每个批次的固定成本，</font>这既可以通过降低固定成本实现，也可以通过聚集多个产品/顾客/供应商的订货来实现。</font>
<font FACE = "楷体_GB2312" size = 5>在与产品相关的特定订货成本较小时，应当采用完全聚集，当和产品相关的特定订货成本较大，应该采用定制化聚集。</font>



<br>
<br>
<br>
<br>
<center><b><font face = "楷体_GB2312" size = 200>供应链管理笔记</font></b></center>
<br>
<br>
<br>
<br>
<center><h1><font size = 500 color = "" face = "楷体_GB2312">周转库存<br><br><font size = 100>与 规模经济管理</font></font></h1></center>
<center><h2><font color = "DarkPink" >定制化聚集</font> ｜<font color = "Green" >EOQ模型推广</font> </h2><h2><font color = "Navy" >启发式算法</font> ｜<font color = "Brown" >订购策略</font> </h2></center>

