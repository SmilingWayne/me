**<font FACE = "楷体_GB2312" size = 7 color = crisma > 运营管理：排队论 </font>**

<font FACE = "Heiti" size = 5 color = Navy >排队论的几个基本概念</font>

-----


<font FACE = "" size = 4><font FACE = "楷体_GB2312" size = 4 color = darkpink >到达率(Arrival Rate)</font>: 在一段时间内顾客到达服务地点的速度，一般用到达间隔时间来衡量；</font>

<font FACE = "" size = 4><font FACE = "楷体_GB2312" size = 4 color = darkpink >服务时间(Service Time)</font>: 描述服务顾客所需时间的情况，或者是单位时间内可以服务的顾客的数量。</font>

<font FACE = "" size = 4><font FACE = "楷体_GB2312" size = 4 color = darkpink >排队规则(Queue Discipline)</font>: 指等待队列中顾客接受服务的顺序。通常是先到先服务(FCFS)，也有可能是后到先服务(FCLS)或者遵循其他优先级规则。本笔记都是先到先服务的规则。</font>

<font FACE = "" size = 4><font FACE = "楷体_GB2312" size = 4 color = darkpink >通道(Channels)</font>：指面向顾客并行的服务窗口的数量。比如🏦有多少个服务窗口，邮局有多少办事员窗口等。</font>
<font FACE = "" size = 4><font FACE = "楷体_GB2312" size = 4 color = darkpink >阶段(Phases）</font>:指每个顾客需要完成服务一次经历的不同服务阶段。比如在装配车间，一个产品需要先后经过多个阶段的组装才能变成产品，在🏥办理手续，需要先到接待室再到门诊部门等。</font>


---

<font FACE = "SimHei" size = 5 color = Crisma>几个常用的排队模型</font>


<font FACE = "" size = 4></font>

<font FACE = "" size = 4 color = Navy>一、基本的单通道类型(M/M/1)</font>

<font FACE = "" size = 4>模型假设如下：</font>

1. <font FACE = "" size = 4>到达率(到达间隔时间）服从指数分布，或者说，顾客的到达是一个泊松过程(Poisson Process)</font>
2. <font FACE = "" size = 4>服务时间服从指数分布</font>
3. <font FACE = "" size = 4>先到先服务的服务规则</font>
4. <font FACE = "" size = 4>队列长度无限</font>
5. <font FACE = "" size = 4>客户源是无限的</font>

<font FACE = "" size = 4>排队模型用六个符号表示，在符号之间用斜线隔开，即 X /Y / Z / A/ B /C 。
- 第一个符号 X 表示顾客到达流或顾客到达间隔时间的分布；
- 第二个符号Y 表示服务时间的分布；
- 第三个符号 Z 表示服务台数目；
- 第四个符号 A 是系统容量限制；
- 第五个符号 B 是 顾客源数目；第六个符号C 是服务规则，如先到先服务 FCFS，后到先服务 LCFS 等。
- 约定，如略去后三项，即指 X /Y / Z / ∞ / ∞ / FCFS的情形。我们只讨论先到先服务 FCFS 的情形，所以略去第六项。
这里的M是指数分布的意思，M是 Markov 的字头，因为指数分布具有无记忆性，即马尔可夫(Markov)性；

例如， M / M /1表示相继到达间隔时间为指数分布、服务时间为指数分布、单服务台的排队系统；
</font>


<font FACE = "" size = 4>我们用下面几个参数表示和计算其运营水平：</font>

<font FACE = "" size = 4>$\quad \lambda$ : 平均到达率</font>
<font FACE = "" size = 4>$\quad \mu$ : 平均服务率</font>
<font FACE = "" size = 4>$\quad n$ : 系统中的客户数量（包括等待的和正在被服务的）</font>

<font FACE = "" size = 4>我们可以给出：<br>系统中没有客户的可能性是$P_0 = 1 - \frac{\lambda}{\mu}$</font>

<font FACE = "" size = 4>系统中有$n$个客户的概率是$P_n = (\frac{\lambda }{\mu} )^n \times P_0$</font>

<font FACE = "" size = 4>系统中的平均客户数是$L = \frac{\lambda}{\mu - \lambda}$</font>

<font FACE = "" size = 4>队列（注意是指正在排队的人）中的平均客户数是$L_q = \frac{\lambda^2}{\mu(\mu - \lambda)}$</font>

<font FACE = "" size = 4>客户在系统中花费的平均时间（包括等待+服务时间）是$W = \frac{L}{\lambda}$</font>

<font FACE = "" size = 4>客户的平均等待时间是：$W_q = \frac{\lambda}{\mu(\mu - \lambda)}$</font>


-----

<font FACE = "" size = 4 color = Navy>二、多通道模型(M/M/s模型)</font>

<font FACE = "" size = 4>在模型一的基础上，假设等待系统中有多个服务人员，譬如机场登机口。只要有空位，顾客就接受服务。此时模型里的c就表示服务台（服务人员）的数量。我们引入一些新数值，并修改模型一的方法来描述这些情况。譬如我们设$s$为服务窗口的数量。</font>

<font FACE = "" size = 4>$\quad P_0$ : 系统中没有客户的概率 $= 1 / (\left[ \sum^{s - 1}_{n = 0}{\frac{1}{n!}(\frac{\lambda}{\mu})^{n} }  \right] + \frac{1}{s!}(\frac{\lambda}{\mu})^s(\frac{s\mu}{s\mu - \lambda}))$</font>

<font FACE = "" size = 4>$\quad L$ : 系统中平均顾客数 <font size = 4>$= \frac{\lambda\mu(\lambda / \mu)^s}{(s-1)!(s\mu - \lambda)^2} P_0 + \frac{\lambda}{\mu}$</font></font>

<font FACE = "" size = 4>$\quad L$ : 排队等待的顾客数 = <font size = 4>$L - \frac{\lambda}{\mu}$</font></font>


<font FACE = "" size = 4>$\quad P_{\omega}$ : 顾客到达时必须等待的概率 = <font size = 5>$\frac{1}{s!}(\frac{\lambda}{\mu})^s \frac{s\mu}{s\mu - \lambda}P_0$</font> </font>

<font FACE = "" size = 4>$\quad W  = $<font size = 4>$L / \lambda$</font></font>

<font FACE = "" size = 4>$\quad W_q  = $<font size = 4>$W - \frac{1}{\mu}$</font></font>

