# 发电机组调度问题（Unit-Commitment-Problem）

!!! quote "Reference / 说在前面"
    最开始参考的是这个综述：IdrissAbdou, Mohamed Tkiouat, Unit Commitment Problem in Electrical Power System:A Literature Review，2018, IJECE.

    but它的模型讲述部分问题比较大。后来参考的是这一篇IJOC上的文献：Bernard Knueven, James Ostrowski, Jean-Paul Watson (2020) On Mixed-Integer Programming Formulations for the Unit Commitment Problem. INFORMS Journal on Computing

    这里依据前文提到的文献，做一个简单的总结和整理。和前面的许多笔记类似，这里会更加侧重确定性下的数学建模，强调约束、目标对应的含义等。至于问题的求解算法、不确定性相关的讨论，本文会一笔带过或者不讨论。

    **另：感谢GPT-4o对本笔记编写提供的帮助。**

**问题描述**

在电力生产行业中，如何根据预测的电力需求以及安全电量，调度每一台发电机组的开关机、开机时的发电功率等，同时满足发电机相关的物理性能、工程检修等的约束，从而最大化总收益或者最小化总成本，是一个经典的优化问题。一般文献中会将其表示为热电机组调度问题：`Unit Commitment Problem`。事实上，大半个世纪之前就已经有相关文献对此进行了刻画和描述。

!!! warning "以下内容，尤其是最小停机/开机时间部分存在问题，待修改。"

- 相关参数: $N$：机组数量; $T$: 时间，24h

- 决策变量：

$I_{it}$： 0-1变量。机组 $i$ 在 $t$ 时刻是否工作，如果是，为1，否则0

$P_{it}$:  连续型变量。机组 $i$ 在 $t$ 时刻的发电功率。

- **目标函数**：

$OC = \sum^N_{i = 1}\sum^T_{t = 1} \text{FC}_{it}(P_{it}) I_{it} + \text{NL}_iI_{it} + \text{ST}_{it} + \text{SD}_{it}$

其中，$\text{FC}$ 是燃料成本，$\text{NL}$ 是 No-load 成本，$\text{ST}$ 是启动成本，$\text{SD}$ 是停机成本。带上下标，可以理解每个标记的具体含义。

这里，展开 $\text{FC}$ 的计算方法。一般用二次函数对某机组在某时刻的燃料成本与输出功率水平进行刻画：

$$\text{FC}_{it}(P_{it}) = c_i + b_iP_{it} + a_i P_{it}^{2}$$

这里的 $a_i, b_i, c_i$ 都是机组 i 的参数。**这个二次函数通常会被建模成分段线性化函数**。(Piece-wise linear function)

$\text{ST}_{it}$ 是重新启动一个热电机组所需要的成本 (restarting a de-commited thermal unit) . 文献认为这取决于 `The temperature of the boiler`. 虽然机组有最小开机时间、最小关机等待时间，但是，在最小关机等待时间后，随着其关机时间不同，水温不同，会导致机器的启动成本不同。文献以此进行描述：

$\text{ST}_{it} =$

$$\begin{aligned}
\begin{cases}
\begin{align}
\text{HSN}_i, \quad  \text{if} \quad \text{MDT} \leq T_{off, i}(t) \leq \text{MDT}_i + T_{\text{cold}, i} \quad \\
\text{CSN}_i, \quad  \text{if} \quad T_{off, i}(t) > \text{MDT}_i + T_{\text{cold}, i} \quad \\
\end{align}
\end{cases}
\end{aligned}$$

这里的 $\text{HSN}$ 和 $\text{CSN}$ 分别是在hot和cold状态下，机组 $i$ 的启动成本。$\text{MDT}_i$ 是 机器 $i$ 的最小关机时间，$T_{cold, i}$ 是机器 $i$ 的冷启动所需时间，$T_{off, i}(t)$ 是机器 $i$ 在 $t$ 时刻的连续停机时间


- **约束条件**

1. **发电机功率限制**

$$P_{it}(\text{min}) < P_{it} < P_{it}(\text{max})$$

其中前后值分别表示机组 $i$ 在 $t$ 时刻的最小和最大发电功率。

2. **功率平衡约束**：在每个时间窗口内的发电功率和需求量(load demand)是平衡的。

$$\sum^N_{i=1} P_{it} I_{it} = D_t$$

3. **最小停机/开机时间约束**

$$T^{\text{on}}_i > \text{MUT}_i$$

其中 $T^{\text{on}}_i$ 表示机组 $i$ 的总开机时间，$\text{MUT}_i$ 是发电机组的最小开机时间。

$$T^{\text{off}}_i > \text{MDT}_i$$

其中 $T^{\text{off}}_i$ 表示机组 $i$ 的总关机时间，$\text{MDT}_i$ 是发电机组的最小关机时间。

4. **功率增速/降速变化约束**

文献里表示为 Ramp rate up/down constraints。发电机组不是一下子就能达到最大开机功率，相同时间间隔内，功率增加/降低的速度不是突变的，而是有最大变化阈值。

$$P_{i,t} - P_{i, t - 1} \leq \text{UR}_i$$

$$P_{i,t - 1} - P_{i, t} \leq \text{DR}_i$$

这里的 $\text{UR}_i$ 和 $\text{DR}_i$ 分别是机器 $i$ 的最大开机功率增速和关机功率减速。

5. **旋转备用(Spinning reserve)功率约束**

!!! note "什么是旋转备用（没错这个东西就是一个专业名词）"

    在电网中，运行储备是系统运营商在短时间内可用的发电能力，以便在发电机出现故障或供应再次中断的情况下满足需求。大多数电力系统的设计都是这样，在正常情况下，运行储备始终至少是最大供应商的容量加上峰值负载的一小部分。（摘自[wikipedia](https://en.wikipedia.org/wiki/Operating_reserve) ）

    意思是啥呢，意思是在这个时间内所有开机状态下的发电机组的最大功率之和必须大于一个给定阈值，以应付可能出现的用电高峰等情况。

$$\sum^N_i I_{it} P_{it} \geq (D_t + R_t), 1 \leq t \leq T$$


这里有点问题。