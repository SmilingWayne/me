# 变上/下限积分函数


!!! note
    参考链接：
    [链接1](https://zhuanlan.zhihu.com/p/376629429)
    [链接2](https://zhuanlan.zhihu.com/p/376629429)

- 设函数 $f(x)$ 在区间 $[a, b]$ 上连续，设$x$为区间$[a, b]$上的一点，考察定积分 $\int^{}_{}f(x) dx = \int^{x}_{a} f(t) dt$ 。
- 如果上限$x$在区间 $[a, b]$上任意变动，则对每一个取定的$x$，定积分都有一个对应值，所以它在区间 $[a , b]$ 上定义了一个函数，记为 $\Phi(x) = \int^{x}_{a} f(t)dt$
- 这个函数就是变上限积分函数。
- 同样地，我们可以定义变下限积分函数。譬如 $\int^{a}{x} f(t)dt$。


## 变限积分函数求导公式

- 如果 $f(x)$ 连续，$\phi(x)$ 和 $\varphi(x)$可导，那么变限积分函数的求导公式可以表述为 

$$\Phi^{'}(x) = \dfrac{d \int^{\phi(x)}_{\varphi(x)}f(t)dt}{dx} = f[\phi(x)] \phi^{'}(x) - f[\varphi(x)] \varphi^{'}(x)$$

- 于是可以得到常见的几个公式：

$$\Phi(x) = \int^{x}_{a} tf(t) dt \\ \Phi^{'}(x) = xf(x)$$


$$\Phi(x) = \int^{\infty}_{x} f(t) dt \\ \Phi^{'}(x) = -f(x)$$

## 扩展


1. 遇到函数：

$$F(x) = \int^{x}_{a}g(x)f(t)dt$$

- 把 $g(x)$ 提到前面去，借助求导的乘法法则求得

$$F^{'} = g^{'}(x) \int^{x}_{a}f(t)dt + g(x)f(x)$$


2. 遇到

$$F(x) = \int^{x}_{a}f(t, x)dt$$

- 采取换元，将 $x$ 分离出来。