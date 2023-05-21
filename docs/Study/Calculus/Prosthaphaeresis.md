# 积化和差 ｜ 和差化积


- 积化和差公式是初等数学三角函数部分的一组恒等式，积化和差公式==将两个三角函数值的积化为另两个三角函数值的和的常数倍，达到降次的作用== 。

### 推导过程

- 已知如下公式：

$\cos (\alpha + \beta) = \cos\alpha \cos \beta - \sin \alpha \sin \beta  \hspace{3cm} (1)$ 

$\cos (\alpha - \beta) = \cos\alpha \cos \beta + \sin \alpha \sin  \beta\hspace{3cm} (2)$

$\sin (\alpha + \beta ) = \sin \alpha \cos \beta + \cos \alpha \sin \beta \hspace{3cm} (3)$

$\sin (\alpha - \beta ) = \sin \alpha \cos \beta - \cos \alpha \sin \beta \hspace{3cm} (4)$

- 通过 $[ (1) + (2) ] / 2$ 可以得出 $\cos \alpha \cos \beta$
- 通过 $[ (2) - (1) ] / 2$ 可以得出 $\sin \alpha \sin \beta$
- 通过 $[ (3) + (4) ] / 2$ 可以得出 $\sin \alpha \cos \beta$
- 通过 $[ (3) - (4) ] / 2$ 可以得出 $\cos \alpha \sin \beta$

- 所以可以得出：

$\sin \alpha \sin \beta = \dfrac{1}{2} [ \cos (\alpha - \beta ) - \cos(\alpha + \beta) ] \hspace{3cm} (5)$

$\cos \alpha \cos \beta = \dfrac{1}{2} [ \cos (\alpha + \beta ) + \cos(\alpha - \beta) ] \hspace{3cm} (6)$

$\sin \alpha \cos \beta = \dfrac{1}{2} [ \sin (\alpha + \beta ) + \sin(\alpha - \beta) ] \hspace{3cm} (7)$

$\cos \alpha \sin \beta = \dfrac{1}{2} [ \sin (\alpha + \beta ) - \sin(\alpha - \beta) ] \hspace{3cm} (8)$


- 对于（5）式，可将$\alpha - \beta$ 视作 $A$，$\alpha + \beta$ 视作 $B$。用$A$和$B$表示并反解出 $\alpha, \beta$。
- 同理，对于剩下的三个式子同样可以利用此方法得出结论。

$\cos \alpha - \cos \beta = - 2 \sin (\dfrac{\alpha +\beta }{2})  \sin (\dfrac{\alpha - \beta}{2})$

$\cos \alpha + \cos \beta =  2 \cos (\dfrac{\alpha +\beta }{2})  \cos (\dfrac{\alpha - \beta}{2})$

$\sin \alpha - \sin \beta =  2 \cos (\dfrac{\alpha +\beta }{2})  \sin (\dfrac{\alpha - \beta}{2})$

$\sin \alpha + \sin \beta = 2 \sin (\dfrac{\alpha +\beta }{2})  \cos (\dfrac{\alpha - \beta}{2})$

- 上面四个就是“和差化积”