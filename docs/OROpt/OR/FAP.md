# 航班分配问题（Fleet Assignment Problem）

需要看MP上一篇很经典的文章：Hane et al., “The fleet assignment problem: Solving a large-scale integer program”, Mathematical Programming, 70 (1995) 211-232。也可以参考梁哲老师的[公众号文章](https://mp.weixin.qq.com/s/m4KhLtzgwakYYi5ZG2MdRw)。时空网络模型、最大化利润。

任务是，给定一个飞行时刻表和可行的飞机。你需要决定哪些类型的飞机执飞哪些航段（flight segment）来最大化盈利或最小化成本，同时满足一系列约束：需求、收益、成本、飞行可行性、飞机维护和运营约束等。

我们把问题刻画成大规模混合整数线性规划，基于多商品网络流模型+侧约束（side constraints）。问题被定义在一个时间拓展的网络上（Time Expanded Network）。


## Mathematical Formulation

### **Sets:**

- \( C \): Set of cities
- \( F \): Set of available fleets，怎么理解呢，就是一个公司可能有 A330，A320，Boeing 777，Boeing 737 max 四种飞机，那么每一种飞机就构成了一个机队。
- \( S(f) \): Number of aircraft available in fleet \( f \)
- \( L \): Set of flights
- \( H \): Set of required flight connections (through-flights)

我们的网络中的节点，通过 ${f, o, t}$ 进行枚举，其中 $f \in F, o \in C, t$ 是在 $o$ 点起飞或者降落点时间

### **Decision Variables:**

- **Binary assignment variables**:

$$X_{fi} = 
  \begin{cases}
  1 & \text{if fleet type } f \text{ flies flight } i \\
  0 & \text{otherwise}
  \end{cases}$$

是否由机队 $f$ 执飞航班 $i$。当然作为初学者似乎更应该写成 $x_{f,o,d,t}$，即，机队 $f$ 执飞从 $t$ 时刻 在 $o$ 城市起飞降落在 $d$ 城市的航班。虽然这样疑似有一些冗长，但是相信我，你会需要一种方式来定义 flight 的.

- **Continuous variables (ground arcs)** representing number of aircraft on the ground:

$$Y_{fo t t^+} \geq 0$$

代表了在 $t,t^+$ 时段内，在 $o$ 地地面上的 机型 $f$ 的飞机数量。模型中用到。你或许会发现为什么这是个continuous。事实上我们已经规定了X是整数了，定下来了 $X$，余下的 $Y$ 应该也是整数。

### **Objective Function:**

- Minimize total assignment cost: 最小化成本。

$$\min \sum_{i \in L} \sum_{f \in F} c_{fi} X_{fi}$$

where \( c_{fi} \) captures:

- Fuel and operating cost of assigning fleet \( f \) to flight \( i \)
- Costs related to lost revenue ("spill") when demand exceeds aircraft capacity

这里的参数 $c_{fi}$ 包含了两个含义：

1. 由机队 $f$ 执飞航班 $i$ 的油料和运营成本；
2. 如果需求超过了飞机的载重，此时供不应求，因此而损失的收益（意味着此时没有派够大的飞机来，丢失了一部分乘客）。

---

## **Constraints:**

1. **Cover Constraints:**

Ensure every flight is covered exactly once: 每个航班被一个机队覆盖；

$$\sum_{f \in F} X_{fi} = 1, \quad \forall i \in L$$

2. **Balance Constraints (Flow conservation):**

Maintain aircraft flow continuity at each station:

$$\sum_{d} X_{fdo t^-} + Y_{fo t^- t} - \sum_{d} X_{fod t} - Y_{fo t t^+} = 0, \quad \forall \{f,o,t\} \in N$$

一个看起来不那么好理解的流平衡：在任何时刻，对一个站点的每一个机队而言，我们向前看，回溯到最后一个有飞机降落的时刻 $t^{-}$ ，向后回溯到第一个有飞机起飞的时刻 $t^{+}$。那么，对这个机队 $f$ 而言，在这个城市 $o$，所有其他城市在 $t^{-}$ 流入该城市的的飞机，加上从 $t^{-}$ 到 $t$ 时刻在地上的该型飞机，等于 $t$ 到 $t^{+}$ 时刻内在地上的该型飞机，加上在 $t^{+}$ 时刻飞走到其他城市的该型飞机。

3. **Required-through Constraints:**

Force certain pairs of flights to be operated by the same fleet:某些航班必须由同一个机队进行服务。

$$X_{fi} - X_{fj} = 0, \quad \forall (i,j) \in H$$

4. **Fleet Size Constraints:**

Ensure the fleet size limit isn't exceeded: 限制机队规模

$$\sum_{i \in O(f)} X_{fi} + \sum_{o \in C} Y_{fo t t^+} \leq S(f), \quad \forall f \in F$$

#### 5. **Variable Bounds:**
- Binary conditions:
  $$
  X_{fi} \in \{0,1\}
  $$
- Non-negativity:
  $$
  Y_{fo t t^+} \geq 0
  $$

---

### **Computational Techniques:**

Due to the large problem scale, several advanced computational techniques are employed:

- **Aggregation and Preprocessing:** Reduce problem size by consolidating nodes and variables.
- **Interior-Point Algorithm:** Solve LP relaxations efficiently.
- **Dual Simplex Algorithm with Steepest Edge Pricing:** Effective for highly degenerate problems.
- **Perturbation Techniques:** Adjust objective coefficients to reduce degeneracy and expedite convergence.
- **Branch-and-Bound Enhancements:** Customized branching rules (e.g., branching on cover rows) improve integer solution finding.

---

### **Results and Performance:**
- Implemented solutions are highly efficient, solving large-scale instances (~2500 flights, 150 cities, 11 fleets) typically within one hour.
- Optimality gaps are typically less than 0.02%, demonstrating high accuracy and efficiency.

---

### **Conclusion:**
The Fleet Assignment Problem is efficiently solvable by sophisticated mathematical programming techniques, which have proven successful in practice for large airlines. Future enhancements can incorporate more complex constraints such as crew scheduling, maintenance operations, and airport-specific limitations.

---

### **Summary of Equations:**
- **Objective:** 
  $$
  \min \sum_{i \in L} \sum_{f \in F} c_{fi} X_{fi}
  $$
- **Cover constraint:** 
  $$
  \sum_{f \in F} X_{fi} = 1, \quad \forall i \in L
  $$
- **Balance constraint:** 
  $$
  \sum_{d} X_{fdo t^-} + Y_{fo t^- t} - \sum_{d} X_{fod t} - Y_{fo t t^+} = 0, \quad \forall \{f,o,t\} \in N
  $$
- **Required-through constraint:** 
  $$
  X_{fi} - X_{fj} = 0, \quad \forall (i,j) \in H
  $$
- **Fleet size constraint:** 
  $$
  \sum_{i \in O(f)} X_{fi} + \sum_{o \in C} Y_{fo t t^+} \leq S(f), \quad \forall f \in F
  $$
- **Bounds and integrality:** 
  $$
  X_{fi} \in \{0,1\}, \quad Y_{fo t t^+} \geq 0
  $$

