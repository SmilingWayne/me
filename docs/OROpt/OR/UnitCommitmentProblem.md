# 发电机组调度问题（Unit-Commitment-Problem）

!!! quote "Reference / 说在前面"
    最开始参考的是这个综述：`IdrissAbdou, Mohamed Tkiouat, Unit Commitment Problem in Electrical Power System:A Literature Review，2018, IJECE.`

    but我开始写此文的时候发现，这篇文章的模型讲述部分问题比较大。后来参考的是这一篇IJOC上的文献：`Bernard Knueven, James Ostrowski, Jean-Paul Watson (2020) On Mixed-Integer Programming Formulations for the Unit Commitment Problem. INFORMS Journal on Computing` ， **这个Paper主要就是讲建模，而且写得很细致**。我觉得**核心的约束**直接看IEEE 这个文章：

    `G. Morales-España, J. M. Latorre and A. Ramos, ”Tight and Compact MILP Formulation for the Thermal Unit Commitment Problem,” in IEEE Transactions on Power Systems,vol. 28, no. 4, pp. 4897-4908, Nov. 2013, doi: 10.1109/TPWRS.2013.22514`

    这个IEEE TPS的文章给出的是比较**紧凑**的MILP建模方式。

    这里依据前文提到的文献，做一个简单的总结和整理。和前面的许多笔记类似，这里会更加侧重确定性下的数学建模，强调约束、目标对应的含义等。至于问题的求解算法、不确定性相关的讨论，本文会一笔带过或者不讨论。

    **另：感谢GPT-4o对本笔记编写提供的帮助。**

## 问题描述

在电力生产行业中，如何根据预测的电力需求以及安全电量，调度每一台发电机组的开关机、开机时的发电功率等，同时满足发电机相关的物理性能、工程检修等的约束，从而最大化总收益或者最小化总成本，是一个经典的优化问题。一般文献中会将其表示为热电机组调度问题：`Unit Commitment Problem`。事实上，大半个世纪之前就已经有相关文献对此进行了刻画和描述。



| 参数             | 意义                           |
| ---------------- | ------------------------------ |
| $P_g$            | 机组 $g$ 的最小输出功率        |
| $\overline{P}_g$ | 机组 $g$ 的最大输出功率        |
| $NG$             | 机组数量                       |
| $NT$             | 时间段数目                     |
| $C_g^{LV}$       | 机组 $g$ 的线性成本            |
| $C_g^{NL}$       | 机组 $g$ 的空载成本            |
| $C_g^{SD}$       | 机组 $g$ 的关停成本            |
| $C_g^{SU}$       | 机组 $g$ 的启动成本            |
| $D_t$            | 未来 $NT$ 时间段的预测负荷     |
| $R_t$            | 未来 $NT$ 时间段的旋转备用负荷 |
| $TD_g$           | 机组 $g$ 的最小关停时间        |
| $TU_g$           | 机组 $g$ 的最小开启时间        |


### 决策变量

> 这里给出的是经典的 `3-binary formulation`，也就是分别用三个0-1变量刻画机组的开关机动作与开关机状态。

| 决策变量  | 意义                                                     | 类型       |
| --------- | -------------------------------------------------------- | ---------- |
| $u_{g,t}$ | 机组 $g$ 在时段 $t$ 内的在线状态，1为运行中，0为脱离运行 | 0-1 Binary |
| $v_{g,t}$ | 机组 $g$ 在时刻 $t$ 的开启动作，1为开启，0为其他         | 0-1 Binary |
| $w_{g,t}$ | 机组 $g$ 在时刻 $t$ 的关停动作，1为关停，0为其他         | 0-1 Binary |
| $p_{g,t}$ | 机组 $g$ 在时段 $t$ 的输出功率                           | Continuous |


## MILP 模型

### 目标函数 

$$\min \sum_{g=1}^{NG} \sum_{t=1}^{NT} \left( C_g^{LV} p_{g,t} + C_g^{NL} u_{g,t} + C_g^{SU} v_{g,t} + C_g^{SD} w_{g,t} \right)$$

其中，各个参数的含义如下表所示：

|        参数        |       意义       |
| :----------------: | :--------------: |
| $C_g^{LV} p_{g,t}$ | 机组线性燃耗成本 |
| $C_g^{NL} u_{g,t}$ |  机组的空载成本  |
| $C_g^{SU} v_{g,t}$ |   机组开启成本   |
| $C_g^{SD} w_{g,t}$ |   机组关停成本   |

其中 $p_{g,t}$ 为连续变量，$u_{g,t}$, $v_{g,t}$, $w_{g,t}$ 为 0-1 变量。

这里，展开 $C_g^{LV} p_{g,t}$ 的计算方法。有的文献会说，实际一般用二次函数对某机组在某时刻的燃料成本与输出功率水平进行刻画：

$$C_g^{LV} p_{g,t} = c_g + b_g p_{g,t} + a_g p_{g,t}^{2}$$

这里的 $a_g, b_g, c_g$ 都是机组 $g$ 的参数。**这个二次函数通常会被建模成分段线性化函数**。(Piece-wise linear function)


###  约束条件


#### 机组输出功率大小约束

$$u_{g,t} P_g^{\min} \leq p_{g,t} \leq u_{g,t} \overline{P}_g \quad \forall g, t$$


任意一台发电机组 $g$ 在任意时间段 $t$ 内处于开启状态，即 $u_{g,t} = 1$，则该发电机组实际运行中的输出功率 $p_{g,t}$ 位于其最大输出功率 $\overline{P}_g$ 以及最小输出功率 $P_g^{\min}$ 之间。

#### 启停时间约束


$$\sum_{i=t-TU_g+1}^{t} v_{g,i} \leq u_{g,t} \quad \forall g, t \in [TU_g, NT]$$


$$\sum_{i=t-TD_g+1}^{t} w_{g,i} \leq 1 - u_{g,t} \quad \forall g, t \in [TD_g, NT]$$


任意一台发电机组 $g$ 在任意时刻 $t$ **一旦开启，必须保持运行状态一段时间才可关停**；同样已关停的发电机组必须保持关停状态一段时间才可以开启。因此有着最小开启时间 $TU_g$ (Minimum uptime of unit $g$ 单位：小时) 和最小关停时间 $TD_g$ (Minimum downtime of unit $g$ 单位：小时) 的限制。

!!! note "对启停时间约束的理解"
      - $\sum \limits_{i=t-TU_g+1}^{t} v_{g,i} \leq u_{g,t} \quad \forall g, t \in [TU_g, NT]$ 可以理解为：
          - 任意一台发电机组 $g$ 在时段内处于**开启**状态，即 $u_{g,t} = 1$，则该发电机组必须在 $t - TU_g + 1, \ldots, t$ 各个时刻中开启且至多开启一次，保证最小开启时间的约束限制。
          - 任意一台发电机组 $g$ 在时段内处于**关停**状态，即 $u_{g,t} = 0$，则该发电机组必须在 $t - TU_g + 1, \ldots, t$ 各个时刻中一直不执行开启动作，保证最小开启时间的约束限制。
          
      - $\sum \limits_{i=t-TD_g+1}^{t} w_{g,i} \leq 1 - u_{g,t} \quad \forall g, t \in [TD_g, NT]$ 可以理解为：
          - 任意一台发电机组 $g$ 在时段内处于关停状态，即 $u_{g,t} = 0$，则该发电机组必须在 $t - TD_g + 1, \ldots, t$ 各个时刻关停且至多关停一次，保证最小关停时间的约束限制。
          - 任意一台发电机组 $g$ 在时段内处于开启状态，即 $u_{g,t} = 1$，则该发电机组必须在 $t - TD_g + 1, \ldots, t$ 各个时刻中一直不执行关停动作，保证最小关停时间的约束限制。

------


#### 启停状态逻辑约束


$$u_{g,t} - u_{g,t-1} = v_{g,t} - w_{g,t} \quad \forall g, t$$


- 任意一台发电机组 $g$ 在任意时间段 $t$ 内处于联机（online）运行状态，即 $u_{g,t} = 1$ 的发电机组，那么它可以被关停而不可以开启；
- 处于脱离运行状态（offline），即 $u_{g,t} = 0$ 的发电机组，可以被开启而不可以被关停。

为了解释清楚 $u_{g,t}$ 和 $v_{g,t}, w_{g,t}$ 三者之间的关系，表 1 给出了 $u_{g,t}$ 和 $v_{g,t}, w_{g,t}$ 三者之间的关系举例。

在此例中，任意一台发电机组 $g$，时间段设置为10，设置最小开启时间 $TU_g=2$，最小关停时间 $TD_g=3$，且设定任意一台机组 $g$ 0时刻的状态为 $u_{g,0}=0$。


| Hours       | 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 10  |
| ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $ u_{g,t} $ | 0   | 1   | 1   | 1   | 1   | 0   | 0   | 1   | 1   | 0   | 0   |
| $ v_{g,t} $ | -   | 1   | 0   | 0   | 0   | 0   | 0   | 0   | 1   | 0   | 0   |
| $ w_{g,t} $ | -   | 0   | 0   | 0   | 1   | 0   | 0   | 0   | 0   | 1   | 0   |

> relationship among $u_{g,t}$, $v_{g,t}$, and $w_{g,t}$.

|                     情形                     |                    描述                    |
| :------------------------------------------: | :----------------------------------------: |
| $v_{g,t} = 1, \text{and} \quad  w_{g,t} = 0$ |   表示机组 $g$ 在 $t$ 时刻要进行启动动作   |
| $v_{g,t} = 0, \text{and} \quad  w_{g,t} = 1$ |  表示机组 $g$ 在 $t$ 时刻要进行关停动作；  |
| $v_{g,t} = 0, \text{and} \quad  w_{g,t} = 0$ | 表示机组 $g$ 在 $t$ 时刻要保持原来的状态； |
| $v_{g,t} = 1, \text{and} \quad  w_{g,t} = 1$ |  不存在该情况，机组不可能同时启动和关停；  |

如表所述，时刻1对应 $v_{g,t} = 1 , \text{and} \quad w_{g,t} = 0$，表示机组 $g$ 在时刻 1 进行开启动作；所以： $u_{g,1} - u_{g, 0} = v_{g, 1} - w_{g,1} = 1$，同时 $u_{g, 0} = 0$, 则 $u_{g,1} = 1$，逻辑关系满足；

通过 $u_{g,t}$ 一行可见，连续的1不小于2个，连续的0不小于3个，满足开始设置的 $TU_g = 2， TD_g = 3$ 的约束。

#### 功率平衡约束

$$\sum_{g=1}^{NG} p_{g,t} \geq D_t \quad \forall t$$

$$\sum_{g=1}^{NG} u_{g,t} \overline{P}_g \geq D_t + R_t \quad \forall t$$


解释：所有投入运行的发电机组在任意时间段 $t$ 内发出的功率之和要满足该时间段 $t$ 内的负荷需求，且留有一定**旋转备用**。

!!! note "补充：旋转备用（Spinning Reserve,没错这个东西就是一个专业名词）"

    在电网中，**运行储备**（旋转备用）是系统运营商在短时间内可用的发电能力，以便在发电机出现故障或供应再次中断的情况下满足需求。大多数电力系统的设计都是这样，在正常情况下，运行储备始终至少是最大供应商的容量加上峰值负载的一小部分。（摘自[wikipedia](https://en.wikipedia.org/wiki/Operating_reserve) ）

    **意思是在这个时间内所有开机状态下的发电机组的最大功率之和必须大于一个给定阈值，以应付可能出现的用电高峰等情况。**

    这个实际上对应的就是上述第二个约束。当前处在开机状态的所有机器的最大功率之和必须大于一个给定阈值，这个阈值一般是大于需求 $D_t$ 的。这里就涉及到一个问题，**如果一个机器刚刚开机但还没达到输出功率（这里需结合第5条约束，也就是机器功率增速不是迅速增加来看）**，此时，这台机器所能提供的最大功率不能直接用 $\overline{P}_g$ 来表示了，所以严格地说，上述刻画还不够准确，一种准确的刻画是：

    我们用 $P^{\max}_{gt}$ 表示机组 $g$ 在 $t$ 时刻**能提供的最大功率**。所以用如下两个式子进行约束：

    $$P^{\max}_{gt} \leq u_{g,t} \overline{P}_g , \forall u, \forall t$$

    $$P^{\max}_{gt} \leq  p_{g,t-1} + u_{g,t-1} \text{UR}_g + \overline{P}_g(1 - u_{g,t-1}),\quad \forall u, \forall t = 2,3....,T$$

    所以，功率平衡约束的第二个约束，应该改写成：

    $$\sum_{g=1}^{NG} P^{\max}_{gt} \geq D_t + R_t \quad \forall t$$

    这个表述参考了文献 `Ana Viana, João Pedro Pedroso, A new MILP-based approach for unit commitment in power production planning, International Journal of Electrical Power & Energy Systems, Volume 44, Issue 1,` 的相关表述。



!!! note "补充：重新启动成本 $C^{\text{SU}}_g$"
    $C^{\text{SU}}_g$ 是重新启动一个热电机组所需要的成本 (restarting a de-commited thermal unit) . 有的文献认为这取决于 `The temperature of the boiler`. 虽然机组有最小开机时间、最小关机等待时间，但是，在最小关机等待时间后，随着其关机时间不同，水温不同，会导致机器的启动成本不同。有的文献会这样刻画：

    $C^{\text{SU}}_g = $

    $$\begin{aligned}
    \begin{cases}
    \begin{align}
    \text{HSN}_g, \quad  \text{if} \quad \text{TD}_g \leq T_{off, g}(t) \leq \text{TD}_g + T_{\text{cold}, g} \quad \\
    \text{CSN}_g, \quad  \text{if} \quad T_{off, g}(t) > \text{TD}_g + T_{\text{cold}, g} \quad \\
    \end{align}
    \end{cases}
    \end{aligned}$$

    这里的 $\text{HSN}$ 和 $\text{CSN}$ 分别是在hot和cold状态下，机组 $g$ 的启动成本。$\text{TD}_g$ 是 机器 $g$ 的最小关机时间，$T_{cold, g}$ 是机器 $g$ 从关机到变为冷启动的时间，也就是说，在(1) 式的范围内，该发电机如果要继续开机，则属于热启动； $T_{off, g}(t)$ 是机器 $g$ 在 $t$ 时刻的**连续停机时间**。




#### 功率增速/降速变化约束


文献里表示为 Ramp rate up/down constraints。其实际含义是，发电机组不是一开机就能达到最大开机功率的，也不是一关机就立刻回到0功率，而是在相同时间间隔内，功率增加/降低的速度不是突变的，是有最大变化阈值的。

$$p_{g,t} - p_{g, t - 1} \leq \text{UR}_g$$

$$p_{g,t - 1} - p_{g, t} \leq \text{DR}_g$$

这里的 $\text{UR}_g$ 和 $\text{DR}_g$ 分别是机器 $g$ 的**最大开机功率增量**和**关机功率减量**。

#### 其他可能考虑的约束

实际上很多论文也在约束上下了很多功夫，包括但不限于：电网传输相关约束、时间依赖的启动成本(Time-dependent startup cost)，关停成本、人员检修约束、机器维修约束等；