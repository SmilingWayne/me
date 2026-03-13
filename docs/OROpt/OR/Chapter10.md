# Claude Code: EOQ, 报童模型，(s,S) 策略的深度研究

!!! note "本内容完全生成自Claude Code的深度研究Skills。[来源链接](https://github.com/Weizhena/Deep-Research-skills/blob/master/README.zh.md)"
    经过少量人工核查和来自3个不同AI的辅助核查，修复了 2.4 离散需求下期望成本边际分析的错误。

    - 补充了 3.4 最优参数的适用范围 (by Gemini)

    - 补充了 1.4 EOQ 扩展模型的变量范围 (by Gemini)

    注意本文依然可能存在遗漏或者错误，如发现请及时联系作者（笑笑）。

    ---- 

    原内容参考笔记历史记录。

## Executive Summary

This report provides complete mathematical derivations and comparative analysis of three fundamental inventory models:

| Model            | Type                        | Key Decision                   | Optimal Formula                  |
| ---------------- | --------------------------- | ------------------------------ | -------------------------------- |
| **EOQ**          | Deterministic, Multi-period | Order Quantity Q               | $Q^* = \sqrt{\frac{2DK}{h}}$     |
| **Newsvendor**   | Stochastic, Single-period   | Stock Level Q                  | $F(Q^*) = \frac{C_u}{C_u + C_o}$ |
| **(s,S) Policy** | Stochastic, Multi-period    | Reorder Point s, Order-up-to S | $G(s) = G(S) + K$                |

---

## 1. EOQ Model and Extensions

### 1.1 Basic Model Assumptions

- **Demand**: Constant, known, uniform over time (deterministic rate $D$ units/year)
- **Replenishment**: Instantaneous (entire order arrives at once)
- **Shortages**: Not allowed (basic model)
- **Costs**:
  - $K$ = Fixed ordering cost per order
  - $h$ = Holding cost per unit per year
  - $C$ = Unit purchase cost

### 1.2 Complete Derivation

**Step 1**: Define total annual cost function

$$TC(Q) = \frac{D}{Q}K + \frac{Q}{2}h + DC$$

**Step 2**: Take first derivative with respect to $Q$

$$\frac{dTC}{dQ} = -\frac{DK}{Q^2} + \frac{h}{2}$$

**Step 3**: Set derivative equal to zero for optimality

$$-\frac{DK}{Q^2} + \frac{h}{2} = 0$$

**Step 4**: Solve for $Q^*$

$$Q^* = \sqrt{\frac{2DK}{h}}$$

**Step 5**: Verify second-order condition

$$\frac{d^2TC}{dQ^2} = \frac{2DK}{Q^3} > 0 \quad \text{for } Q > 0$$

### 1.3 Key Results

| Metric                    | Formula                                      |
| ------------------------- | -------------------------------------------- |
| Optimal Order Quantity    | $Q^* = \sqrt{\frac{2DK}{h}}$                 |
| Optimal Cycle Time        | $t^* = \frac{Q^*}{D} = \sqrt{\frac{2K}{Dh}}$ |
| Minimum Total Cost        | $TC^* = \sqrt{2DKh} + DC$                    |
| Number of Orders per Year | $n = \frac{D}{Q^*} = \sqrt{\frac{Dh}{2K}}$   |

### 1.4 Model Extensions

#### Model II: EOQ with Backorders

$$Q^* = \sqrt{\frac{2DK}{h}} \cdot \sqrt{\frac{h+p}{p}}, \quad b^* = Q^* \cdot \frac{h}{h+p}$$

Where $p$ = shortage cost per unit per year.

Where $b^*$ = maximum backordered quantity

#### Model III: Economic Production Quantity (EPQ)

$$Q^* = \sqrt{\frac{2DK}{h}} \cdot \sqrt{\frac{P}{P-D}}$$

Where $P$ = production rate ($P > D$).

#### Model V: Quantity Discounts
Requires iterative algorithm comparing total costs at each price break point.

---

## 2. Newsvendor Model (Newsboy Problem)

### 2.1 Model Assumptions

- **Demand**: Random, follows known probability distribution $F(x)$
- **Replenishment**: Single ordering opportunity before selling season
- **Shortages**: Lost sales (not backordered)
- **Costs**:
  - $c$ = Unit purchase cost
  - $p$ = Unit selling price ($p > c$)
  - $s$ = Unit salvage value ($s < c$)
  - $C_u = p - c$ = Underage cost (lost profit per unit)
  - $C_o = c - s$ = Overage cost (loss per unsold unit)

### 2.2 Complete Derivation (Continuous Demand)

**Step 1**: Expected profit function

$$E[\pi(Q)] = p \cdot E[\min(Q,D)] + s \cdot E[\max(Q-D,0)] - cQ$$

**Step 2**: Express using integrals

$$E[\pi(Q)] = p\int_0^Q x f(x)dx + p\int_Q^\infty Q f(x)dx + s\int_0^Q (Q-x)f(x)dx - cQ$$

**Step 3**: Simplify

$$E[\pi(Q)] = (p-c)Q - (p-s)\int_0^Q F(x)dx$$

**Step 4**: First-order condition

$$\frac{dE[\pi]}{dQ} = (p-c) - (p-s)F(Q) = 0$$

**Step 5**: Solve for $Q^*$

$$F(Q^*) = \frac{p-c}{p-s} = \frac{C_u}{C_u + C_o}$$

**Step 6**: Second-order condition

$$\frac{d^2E[\pi]}{dQ^2} = -(p-s)f(Q) < 0 \quad \text{(confirms maximum)}$$

### 2.3 Critical Fractile Formula

$$\boxed{Q^* = F^{-1}\left(\frac{C_u}{C_u + C_o}\right)}$$

| Demand Distribution     | Optimal $Q^*$                                            |
| ----------------------- | -------------------------------------------------------- |
| Normal($\mu, \sigma^2$) | $\mu + z_\alpha \sigma$ where $z_\alpha = \Phi^{-1}(CR)$ |
| Uniform($a, b$)         | $a + CR \cdot (b-a)$                                     |
| Exponential($\lambda$)  | $-\frac{\ln(1-CR)}{\lambda}$                             |

### 2.4 Discrete Demand Case (Model VI)

Using marginal analysis for expected cost:

$$\Delta C(Q) = C(Q+1) - C(Q) = (C_o + C_u)\sum_{r=0}^Q P(r) - C_u$$

Optimal $Q^*$ satisfies $\Delta C(Q^*) \ge 0$ and $\Delta C(Q^*-1) < 0$, which yields:

$$F(Q^*-1) < \frac{C_u}{C_u + C_o} \leq F(Q^*)$$

---

## 3. (s,S) Inventory Policy

### 3.1 Model Assumptions

- **Demand**: Stochastic, i.i.d. across periods
- **Replenishment**: Instantaneous or with lead time $L$
- **Shortages**: Backordered with penalty cost
- **Costs**:
  - $K$ = Fixed ordering cost
  - $h$ = Holding cost per unit per period
  - $p$ = Shortage cost per unit per period
  - $c$ = Unit purchase cost

### 3.2 Policy Definition

$$(s,S) \text{ Policy: } \begin{cases} \text{If } I < s: & \text{Order } S - I \\ \text{If } I \geq s: & \text{Do not order} \end{cases}$$

Where $I$ = current inventory level.

### 3.3 Mathematical Foundation: K-Convexity

**Definition**: A function $g(x)$ is K-convex if for any $x_1, x_2$ and $\lambda \in [0,1]$:

$$g(\lambda x_1 + (1-\lambda)x_2) \leq \lambda g(x_1) + (1-\lambda)g(x_2) + K(1-\lambda)$$

**Scarf's Theorem (1960)**: Under general conditions, the value function in the dynamic inventory problem is K-convex, and an (s,S) policy is optimal.

### 3.4 Characterization of Optimal Parameters

Let $G(y) = h \cdot E[(y-D)^+] + p \cdot E[(y-D)^-]$ be the single-period expected cost.

**Optimal $S^*$**: Minimizes $G(y)$

$$\frac{dG}{dy} = 0 \implies F(S^*) = \frac{p}{h+p}$$

> Note: This strictly applies to the single-period problem; for multi-period, it serves as a myopic approximation.

**Optimal $s^*$**: Satisfies the indifference condition

$$G(s^*) = G(S^*) + K$$

### 3.5 Solution Method

1. Compute critical ratio: $CR = \frac{p}{h+p}$
2. Find $S^* = F^{-1}(CR)$
3. Solve $G(s) = G(S^*) + K$ numerically for $s$

For normal demand with lead time $L$:

$$S^* = \mu_L + z \cdot \sigma_L \quad \text{where } z = \Phi^{-1}(CR)$$

---

## 4. Comparative Analysis

### 4.1 Decision Framework

| Use Model When                                                                        |
| ------------------------------------------------------------------------------------- |
| **EOQ**: Demand is stable and predictable; holding and ordering costs dominate        |
| **Newsvendor**: Single selling opportunity; high demand uncertainty; perishable goods |
| **(s,S)**: Stochastic demand over multiple periods; significant fixed ordering costs  |

### 4.2 Assumptions Comparison

| Aspect           | EOQ                  | Newsvendor           | (s,S)               |
| ---------------- | -------------------- | -------------------- | ------------------- |
| Demand           | Deterministic        | Stochastic           | Stochastic          |
| Time Horizon     | Infinite             | Single Period        | Infinite            |
| Review           | Continuous           | Single               | Continuous/Periodic |
| Fixed Order Cost | Yes                  | N/A                  | Yes                 |
| Key Trade-off    | Holding vs. Ordering | Overage vs. Underage | Three-way balance   |

### 4.3 Real-World Applications

| Industry          | EOQ                  | Newsvendor              | (s,S)                  |
| ----------------- | -------------------- | ----------------------- | ---------------------- |
| **Retail**        | Staple goods         | Fashion, seasonal items | High-value electronics |
| **Healthcare**    | Routine supplies     | Vaccines (expiry)       | Critical medications   |
| **Manufacturing** | Component production | Customized products     | MRO items              |

---

## 5. Key Insights

### EOQ Model
- The square-root relationship means quadrupling demand only doubles optimal order quantity
- Total ordering cost equals total holding cost at the EOQ (in basic model)
- Cost curve is flat near optimum - model is robust to parameter errors

### Newsvendor Model
- The critical ratio $\frac{C_u}{C_u+C_o}$ represents the optimal service level
- Higher underage cost leads to higher order quantities
- When $C_u = C_o$, optimal service level is 50%

### (s,S) Policy
- K-convexity is the mathematical property guaranteeing (s,S) optimality
- The gap $S-s$ increases with setup cost $K$
- As $K \to 0$, (s,S) converges to base-stock policy

---

## 6. References

### Foundational Papers
1. Harris, F.W. (1913). "How Many Parts to Make at Once". *Factory, The Magazine of Management*, 10(2), 135-136.
2. Arrow, K.J., Harris, T., & Marschak, J. (1951). "Optimal Inventory Policy". *Econometrica*, 19(3), 250-272.
3. Scarf, H. (1960). "The Optimality of (s,S) Policies in the Dynamic Inventory Problem". In *Mathematical Methods in the Social Sciences*, Stanford University Press.

### Textbooks
1. Zipkin, P.H. (2000). *Foundations of Inventory Management*. McGraw-Hill.
2. Silver, E.A., Pyke, D.F., & Peterson, R. (1998). *Inventory Management and Production Planning and Scheduling*. Wiley.
3. Nahmias, S. & Olsen, T.L. (2015). *Production and Operations Analysis*. Waveland Press.

*Report generated from deep research conducted on 2026-03-10*


