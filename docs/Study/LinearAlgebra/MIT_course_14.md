# 子空间投影


!!! abstract "大纲"
    1. 投影
    2. 最小二乘
    3. 投影矩阵

【补充图片】

### 投影的概念

如图所示。给出两个向量a, b，我们希望在a上找到离b最近的点。方法就是借助b在a上的投影实现。这个距离像是一个“误差”e，用来表示a和b的差距。e = diff between b and p，这里的p可以记作 p = xa. 我们要找的投影点，相当于找这个x等于多少。

所以图中的内容可以描述为：a和误差e垂直：$a^Te = 0$，也就是 $a^T(b - xa) = 0$。$a^Tb - a^Txa = 0 \rightarrow a^Txa = a^Tb \rightarrow xa^Ta = a^Tb \rightarrow x = \dfrac{a^Tb}{a^Ta}$。

注意上面式子里头 $a^Ta$ 是一个数字。$x$ 也就相当于是一个系数。所以可以把向量 $p$ 表示出来。 $p = \dfrac{a^Tb}{a^Ta}a$ .

!!! note "讨论"

    如果 b 翻倍了， p 怎么变化？

    > 放大同样倍数。 $p_2 = 2p_1$

    如果被投影的向量翻倍了，p怎么变化？

    > 不变。因为上下会抵消。

---------

上面的内容还有另一个理解方式。我们从 $p = xa$ 开始，这里 $x = \dfrac{a^Tb}{a^Ta}$，是个系数，所以 $p = xa = ax = a \dfrac{a^Tb}{a^Ta}$ ，利用结合律，有 $p = \dfrac{aa^T}{a^Ta} b$。这个变换实际上是把 $b$ 分离出来了，$p$ 可以看作是 $\dfrac{aa^T}{a^Ta}$ 和 向量 $b$ 的乘积。这里的 $\dfrac{aa^T}{a^Ta}$ 是一个矩阵 $P$ （这里用大写字母标记，和向量区分开来，实现了 $p = Pb$ ），我们称为投影矩阵（projection matrice），因为分子上是一个矩阵，分母是一个数。

思考这个矩阵 $P$，它的秩是多少？

> $r(P) = 1$. 因为是 $aa^T$，它的列空间就是经过 $a$ 的一条直线。这是一个秩1矩阵。


思考这个矩阵 P，它是对称的。

如果做两次投影会怎样（也就是$P^2$）。第二次投影后，投影仍在原来位置上。

!!! note "为什么要做投影"

    $Ax = b$ 有时候可能是无解的。可能一堆等式都是 $0 = b(b \neq 0)$. 我们就去解最接近的能解的问题。

    $Ax$ 是在 $A$ 的列空间内，$b$ 不在，这时候我们就把 $b$ 投影到列空间上，选列空间内距离 $b$ 最近的向量 $p$ 代替。我们实际上就是在求 $Ax = p$ 的解。$p$ 是 $b$ 在列空间上的投影。这时候 $p$ 实际上是列空间内最适合的右侧向量。我们解  $A\hat{x} = p$ 即可。这里加上hat是为了和原来的区别，因为 $x$ 不是原来等式里的$x$ 了。而是一个近似。

    ----------


    现实场景：比如我们在做一些观测时，假设我们观测一个系统的运行表现，这个系统的运行通过参数 $x$ 决定，我们观察的是它的运行结果$b$. 我们每观察一次，得到一个 $b$，观察很多次自然得到很多 $b$. 我们希望通过我们观测到的 $b$ 来反推系统的参数配置 $x$ 是什么。

    在实际问题中，当方程数特别多时，右侧的b难免会混入一些“坏数据”、“噪音”，于是Ax=b就解不出来了。我们甚至不知道b中哪一个数据出了问题。这样b中既有好数据，也有坏数据。好数据，这里是说能帮助我们求出正确x的数据。此时，我们需要把这些“坏数据”给筛选出来。这正是线性代数需要解决的问题。

    1. 一种代数是不断去掉一些方程，直到剩下一个可逆的方阵，然后求出它的解。但是这种方法并不完美。因为对于所有的测量值而言，我们无从判断哪些数据是好数据，哪些数据是坏数据。我们希望利用所有的测量值求出“最优值”，从而得到最完整的信息。

    2. 另外一种方法是进行方程变换，之前的消元法能告诉我们方程组是否有解。消元之后，如果 $A$ 中有0行，而对应的 $b$ 的部分不为0，则方程组无解。这里的问题是消元法识别了方程组无解后，怎么办？这里就用到了我们的投影方法。


【补充图片】

现在我们的任务实际上是，找一个使 b 投影到平面的最近点上的漂亮公式，首先需要知道平面的基向量。

现在我们假设基向量为 $a_1, a_2, e = b - p = b - A\hat{x}$, $p$ 是 $a_1, a_2$ 的一个线性组合。（寻找一个合适的基向量组合，好让误差向量垂直于平面）

e 和平面的任意向量都是正交的。所以 

$$\begin{aligned}\begin{equation*}
\begin{cases}
a_1^T (b - A\hat{x}) = 0 \\ 
a_2^T (b - A\hat{x}) = 0 
\end{cases}
\end{equation*}\end{aligned}$$

让 $A = \begin{bmatrix} a^T_1 \\ a^T_2 \end{bmatrix}$, 有 $A^T(b - A\hat{x}) = 0$。把括号拆开，就出现了 $A^TA\hat{x} = A^Tb$。和我们前面投影向量的投影，在形式上一模一样。不过差别是向量投影部分， $a$ 是向量，这里 $A$ 是矩阵。


----------

## 三个公式

1. $\hat{x} = (A^TA)^{-1}A^Tb$
2. $p = A\hat{x} = A(A^TA)^{-1}A^Tb$，称为投影向量。
3. 这里 $P = A(A^TA)^{-1}A^T$ 是投影矩阵。

!!! note "公式解读"
    这个P的公式很长，为什么不能把 $A^TA$ 写在分母上，因为 $A^TA$ 是**一个矩阵乘积**，不像向量部分 $a^Ta$ 是一个**常数**

    - 如果A的列空间是整个 R^n 空间，那么投影矩阵 P 就是单位矩阵。
    - 如果把b投影到3维空间，那么b本身就是3维。

同样需要记一些P的性质： $P^T = P$. 

> $P^T = (A^T)^T((A^TA)^{-1})^TAT$， 这里的 (A^TA)^{-1} 也是一个对称矩阵，它的逆也是对称的。
>
> 也可以证得 $P^2 = P$

只要A是列满秩的，那么 A^TA 就是满秩的方阵，就是可逆的。r(A) = n，意味着A的零空间只有 0 向量，Ax = 0 只有 0 解，此时Ax = b 就有唯一特解。因此 A^TA 是可逆的，当且仅当 A 的各列线性无关，列满秩。

这是A^TA 很重要的性质：此时 $A^TA\hat{x} = A^Tb$ 一定有唯一解。


## 应用：最小二乘法


【待补充】

