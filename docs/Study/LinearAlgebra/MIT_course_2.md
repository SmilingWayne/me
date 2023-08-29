# 消元法（Elimination）

!!! note "简单引入"
    求解线性方程组的方法，最常用的就是消元法。消元法可以判断一个矩阵是否是一个“好的”矩阵，或者是否存在问题，为了得到具体的求解结果，还需要有一个“回代”的步骤。

    - 方法：Gauss Elimination
    - Gauss-Jordan Elimination


## 步骤

给出如下的公式：

$$\begin{align}\begin{equation*}
\begin{cases}
x  + 2y + z   = 2 \\ 3x + 8y + z = 12 \\ 4y + z = 2
\end{cases}
\end{equation*}\end{align}$$

初高中数学已经教过，第一个方程3个未知数，第二个方程也有三个未知数，可以消去第二个中的$x$，第二个方程就只有2个未知数了，第三个方程再借助第二个方程消去$y$，就只有一个$z$了。每次计算时候，我们把左上角的第一个元素叫做**主元**，（pivot）

$\begin{bmatrix} \colorbox{yellow}{1} & 2 & 1 \\ 3 & 8 & 1 \\ 0 & 4 & 1 \end{bmatrix} \xRightarrow{\text{r2 - r1 * 3}}  \begin{bmatrix}   \colorbox{yellow}{1} & 2 & 1 \\ 0 & \colorbox{yellow}{2} & -2 \\ 0 & 4 & 1 \end{bmatrix} \xRightarrow{\text{r3 - r2 * 2}} \begin{bmatrix} \colorbox{yellow}{1} & 2 & 1 \\ 0 & \colorbox{yellow}{2} & -2 \\ 0 & 0 & \colorbox{yellow}{5} \end{bmatrix}$

> 标记黄色的即为“主元”。
>
> 这个时候，我们最终的矩阵对角线以下的元素全为0，这样子的矩阵称为上三角矩阵（Upper triangular matrix），用$U$来表示。


刚刚我们对A矩阵进行了操作，为了保证方程组形式不变，右端项也需要进行调整，从 $\begin{bmatrix} 2 \\ 12 \\ 2 \end{bmatrix} \xRightarrow{} \begin{bmatrix} 2 \\ 6 \\ -10 \end{bmatrix} = c$，方法同$A$的操作，$\text{r2 - r1 * 3}$，然后 $\text{r3 - r2 * 2}$ 。

这个时候，方程组变化为： $Ux = c$。 这是最后的矩阵形式。

计算出 $U$ 之后，Jordan提出了“回代”的思想（Back substitution），也就是，最后一行把$z$求出来之后，把$z$的值回代到第二行，第二行只剩一个未知数$y$，直接求出来，然后把$y,z$ 都代入第一个方程，遂求出$x, y, z$

-----------

## 拓展思考

!!! question "思考"
    我们能否用矩阵形式，把这种“消元”的过程表示出来？

第一节提到，用行向量左乘矩阵，实际进行的是==矩阵各行的线性组合== ，而消元实际上就是在进行矩阵各行线性组合，比如如下操作：

$\begin{bmatrix} 1 & 0 & 0 \end{bmatrix} \begin{bmatrix} 1 & 2  &1 \\ 3 & 8 & 1 \\ 0 & 4 & 1 \end{bmatrix} = \begin{bmatrix} 1 & 2 & 1 \end{bmatrix}$ ，相当于: $\text{r1 * 1+ r2 * 0+ r3 * 0}$ 

所以，“将第一行乘$-3$再加到第二行上去”这个操作，可以表示为：

$\begin{bmatrix} 1 & 0 & 0 \\ -3 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix} \begin
{bmatrix} 1 & 2  &1 \\ 3 & 8 & 1 \\ 0 & 4 & 1 \end{bmatrix} = \begin{bmatrix} 1 & 2  &1 \\ 0 & 2 & -2 \\ 0 & 4 & 1 \end{bmatrix}$

前面的矩阵 $\begin{bmatrix} 1 & 0 & 0 \\ -3 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}$ 称为**初等矩阵**（elementary matrix），记作 $E_{21}$，表示“消去第2行第1列的元素”。

按照正常顺序，$(2,1)$ 位置消去后，消去 $(3,1)$ 位置，然后 $(3,2)$ 位置，但是这个矩阵 $(3,1)$ 位置已经是0了，所以我们直接左乘$E_{32}$位置进行操作即可。

$E_{32} E_{21} A = U = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & -2 & 1 \end{bmatrix} \begin{bmatrix} 1 & 0 & 0 \\ -3 & 1 & 0 \\ 0 & 0 & 1  \end{bmatrix} \begin{bmatrix} 1 & 2  &1 \\ 3 & 8 & 1 \\ 0 & 4 & 1 \end{bmatrix} = \begin{bmatrix} 1 & 2 & 1 \\ 0 & 2 & -2 \\ 0 & 0 & 5 \end{bmatrix}$

!!! tip "细节"
    这里可以做一个小小的推广，比如，由于矩阵右乘相当于列变换，所以如果你想要调换两列的位置，你可以右乘一个“置换矩阵”（permutation matrix）

    $\begin{bmatrix} a & b \\ c & d \end{bmatrix}  \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix} = \begin{bmatrix} b & a \\ d & c \end{bmatrix}$

    同样的，你想要调换两行的位置，那么**左乘**一个置换矩阵即可。

    $\begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix} \begin{bmatrix} a & b \\ c & d \end{bmatrix} = \begin{bmatrix} c & d  \\ a & b \end{bmatrix}$


!!! notes "矩阵乘法重点" 
    ==你无法改变矩阵乘法的顺序==。

    $AB$和$BA$，不一定相等。**矩阵乘法没有交换律。**


----------


!!! question "从 $U$ 变回 $A$ 的逆变换"
    刚才实现的是从A变成上三角矩阵$U$，那么该怎么从$U$变回去呢？

    很简单，只需要把原来加上的再减去，原来减去的再加上即可。比如原来第二行减去了3倍的第一行，那么这里只需要在第二行加上3倍的第一行就行。按照道理说，这样的操作对 $A$ 没有任何变化。

    $\begin{bmatrix} 1 & 0 & 0 \\ 3 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} 1 & 0 & 0 \\ -3 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix} = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix} = I$

    $I$ 就是单位矩阵（Identical matrix）