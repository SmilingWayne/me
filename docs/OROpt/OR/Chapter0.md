# Linear Programming



> - Introduction to LP
> - Geometric Interpretation of LP
> - Simplex Method
> - Duality and Sensitivity Analysis
> - Interior Point Method （摆脱了Simplex Method的框架，从内部逼近；在有限时间内的多项式算法）
> - Related Topics

!!! abstract "How"
    - Geometric intuiton (相信你的直觉)
    - Algebraic manipulation
    - Computer programming 


## History of LP 

> **Orient** : US Air Force Logistical Supply Program by Danzig, a planning tool by linearizing problems.(最好的东西往往是最大的阻力:
>  Simplex Method)
>
> 可能的问题：顶点的数量可能很大很多，一个顶点一个顶点地走，效果不会很好；
> 
> **1975 Nobel Prize**: Kantorovich, Optimum allocation of resources.
>
> **Ellipsoid Method** : Khachian Poly-nomial time algorithm
>
> **Interior-Point Method** : Karmarkar 1984

- nonlinear：二次做起，把向量用矩阵取代；
- Convex quadratic（二次型）

==Manpower Allocation==

$$\sum^m_{i = 1} \sum^n_{j = 1} c_{ij} x_{ij}$$

$$\text{s.t.} \begin{dcases}  \sum^{m}_{i = 1} x_{ij} \geq b_{j}, \forall j \cr  \sum^{n}_{j = 1} x_{ij} \leq a_{i}, \forall i \cr x_{ij} \geq 0 \end{dcases}$$

- LP 的 fundamental theorem：如果有最优解的话，那么一定有个顶点是最优解；
> 问题出现：如何检查一个解是最优解？


## 如何解LP？
- 线性约束（一条一条线的相交）导致可行域成为凸多面体集合，且有有限的顶点；
- 线性的目标函数对每个给定值的一个linear contour 
- LP的基本定理：
    - 如果线性规划问题的可行域非空，那么它的最优解要么无界，要么至少在在其可行域的一个顶点上； 



- Simplex Method:
    - In general, works very well. Visits around $0.7159\hspace{2pt} m^{0.9522} n^{0.3109}$ 顶点；（$m$个约束，$n$个决策变量）
    - Klee & Minty, 1971 ，需要 $2^n - 1$ 个顶点才可；


- Ellipsoid Method:
    - 对偶 + 原问题合并成新的LP，从最开始的圆形开始，判断最优解的Convex缩小体积：可以在多项式时间内解决；

- Interior Point Method 
    - 如何检查“一个内点是否是最优的？”


## Ongoing / Future work（解决实际问题需要考虑的东西）
    - **special structure**，充分利用问题的结构；
    - **decomposition**， 问题分解：大问题化成小问题；
    - Nonlinear optimization with linear constraints（转化成linear Programming来解）
    - robust optimization
    - semidefinite optimization
    - ...


坦塔罗斯：希腊神话中的吕狄亚国王。因触怒主神宙斯，被罚永世站在水中。水深及下巴，但他口渴要喝水时，水就退去。头上有果树，但他饥饿想吃果子时，树枝就升高。


## Lecture 2: Preliminaries


### Standard form LP 