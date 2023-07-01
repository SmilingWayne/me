# 离散型随机变量及其分布

- 概率分布
- 离散型随机变量

## 0-1分布

## 二项分布 Binomial

- 某试验只有两个结果，A发生和A不发生，在n次独立重复的伯努利实验中，设每次试验中事件A发生的概率为$p$。用$X$表示$n$重伯努利试验中事件$A$发生的次数，事件${X=k}$即为“$n$次试验中事件A恰好发生$k$次”
- $X \sim b(n,p)$
- 使得$P(n=k)$ 最大的数k，称为最可能成功的次数
- $E(X) = np$
- $D(X) = np(1-p)$

> e.g. 医学中描述病人是否患病；管理学中估计机器故障概率决定所需要的维修工人数量；经济学保险学中用来估计保险费用...
>
> - 一大批产品合格率0.2。从一大批中抽取20个，求20个中合格品个数X的分布律;
>
> $P(X = 20) = (0.2)^{20}; P(X = 19) = (0.2)^{19} \times 0.8 \times C^{1}_{20}; P(X = n) = C^{n}_{20}(0.2)^n \times (0.8)^{20-n}$
>
> (单峰式， 先增后减)
>
> $\dfrac{P(X = k)}{ X = k - 1} = \dfrac{C^k_p p^k q^{n - k}}{C^{k-1}_p p^{k-1}q^{n-k+1}} = \dfrac{(n-k+1)p}{kq} = 1 + \dfrac{(n+1)p - k}{kq}$
>
> 如果$k < (n + 1)p$，增；否则减小；如果想扽好，则有两点max；

---------------
## 泊松分布

如果离散随机变量的分布为：

- $P \{ x = k \} = \dfrac{\lambda^k e^{- \lambda}}{k!}$
- $E(X) = \lambda$
- $D(X) = \lambda$
- $X\sim \pi(\lambda)$
就称其服从泊松分布。

!!! Tip
    什么情况可以视作泊松分布：
    - 事件是独立的；
    - 在任意相同的时间范围内，事件发生的概率相同。（如第一天中奖的概率与第二天中奖的概率相同。）
    - 要求解：某个时间范围内，事件发生 X 次的概率有多大；

> e.g. 一定时间间隔内电话交换台收到的呼唤次数; 一本书的印刷错误数; 某一地区一个时间间隔内发生的交通事故数等都服从泊松分布；排队的人数；
>
> 推导：$\lim \limits_{n \to \infty} P(X_n = k) = \lim \limits_{n \to \infty} C^k_nP_n^k(1-P_n)^{n-k}$
>
> $= \dfrac{n(n-1)(n-2)\dots(n-k+1)}{k!}\dfrac{\lambda}{n}^k(1 - \dfrac{\lambda}{n})^{n-k}$
>
> $(1 \times (1 - 1/n)(1 - 2/n)\dots (1 - (k-1)/n))(1 - \lambda / n)^{-k} \dfrac{\lambda^k}{k!}(1 - \lambda / n)^n = e^{-\lambda}$
>
> - 300台设备故障率0.01，一台故障一人处理，问需要几个人保证发生故障又不及时维修的概率  < 0.01.
>
> - $P( X = 8 ) = \dfrac{3^ke^{-3}}{k!} < 0.01$
- 二项分布可以通过泊松分布来近似，有泊松定理：【补充】、【意义】
  
------

## 几何分布

- 进行重复独立试验, 设每次试验成功的概率为$p$, 失败的概率为$1-p = q$ , 将实验进行到出现一次成功为止，用$X$表示所需的试验次数；
- $p_k = q^{k-1} p, k = 1,2,...,$第一次成功在$k$次实验的概率 
- $E(X) = \dfrac{1}{P}$
  

- $D(X) = \dfrac{1 - P}{P^2}$



# 连续型随机变量及其分布


- 设 $X$ 为连续型 r.v., 它取任一指定的实数值 a 的概率均为0. 即 $P{ X = a} = 0$;

- **讨论某个点的概率是没有意义的，可以认为是0（无穷小），并不代表该事件不发生。**


## 概率

$F(x) = \int^{x}_{-\infty} f(t) dt$，

## 均匀分布

$$f(x) = \left\{ \begin{aligned} \dfrac{1}{b-a} , a \leq x \leq b \\ 0, otherwise   \end{aligned} \right. $$

$$E(x) = \dfrac{a+b}{2}$$


## 指数分布

- $$f(x) = \left\{ \begin{aligned} \lambda e^{-\lambda x} , x \geq 0 \\ 0, x < 0 \end{aligned} \right.$$
- $E(x) = \dfrac{1}{\lambda}$
- 指数分布具有**无记忆**的关键性质。这表示如果一个随机变量呈指数分布，当$s,t>0$时有$P(T>t+s|T>t)=P(T>s)$。即，如果$T$是某一元件的寿命，已知元件使用了$t$小时，它总共使用至少$s+t$小时的条件概率，与从开始使用时算起它使用至少$s$小时的概率相等。

## 正态分布(高斯分布)

- $f(x) = \dfrac{1}{\sqrt{2\pi}\sigma} e^{-\dfrac{(x-\mu)^2}{2\sigma^2}}$，记作$X \sim N(\mu, \sigma^2)$

- $E(X) = \mu， \mu$ 也是位置参数；
- $D(X) = \sigma^2 , \sigma$ 决定了图像的尖锐程度，$\sigma$ 越小，图像越尖；
### 标准正态分布

- 期望为0，方差为1的正态分布
- $\Phi(X) =  1 - \Phi(-X)$
- 上$\alpha$分位点：设$X \sim N(0,1)$，如果$Z_{\alpha}$ 满足 $P (X > Z_{\alpha}) = \alpha， \alpha \in (0,1)$，那么点 $Z_{\alpha}$ 就是标准正态分布的上 $\alpha$ 分位点。 $Z_{0.05} = 1.645； Z_{0.025} = 1.96$
> - 考试均分72，96分以上的占比2.3%；求在60～84分之间的概率。
> > $\Phi(\dfrac{96-72}{\sigma}) = 97.7\%$， 求$\sigma$， 然后概率分布函数直接计算$\Phi((84 - 72)/\sigma) - \Phi((60 - 72)/\sigma)$
> - VaR(Value At Risk)是财务核算中的核心概念，投资的VaR可以定义为一个值$v$，满足投资的损失大于$v$的概率只有1%。这个v希望越小越好（ ==比如，我们同样一个投资，能确保损失大于100元的概率 = 其他投资损失大于10000元的投资，说明这个方案很好== ）如果投资收益 X 服从正态分布$N(\mu, \sigma^2)$，那么，因为损失是收益的相反数，所以损失$-X \sim N(-\mu, \sigma^2)$；$0.01 = P(- X > v)$; $0.01 = P(\dfrac{-X + \mu}{\sigma} > \dfrac{v + \mu}{\sigma}) = 1 - \Phi( \dfrac{v + \mu}{\sigma})$
> > 所以 $v = \Phi^{-1}(0.99) * \sigma - \mu$；最终应该选择所有投资选择中能够使得 $\mu - \Phi^{-1}(0.99) * \sigma$ 最大的投资

----------


## Gamma 分布

- 如果连续型随机变量X的概率密度为：
$$f(x) = \left\{ \begin{aligned} \dfrac{\lambda^p}{\Gamma(p)}x^{p-1}e^{-\lambda x} , x > 0 \\ 0, x \leq 0 \end{aligned}  \right.$$

其中 $\lambda > 0, p > 0$ 为参数，$\Gamma$ 函数 $\Gamma(p) = \int^{+\infty}_{0} x^{p-1}e^{-x} dx$，就称$X$服从$\Gamma$分布，记为 $X \sim \Gamma(p, \lambda)$


- 待补充


# 随机变量的函数的分布


>  通过已知的r.v. X的分布，求得其函数 Y = g(X) 的分布（其中g(.) 是已知的连续函数）；
## X 是离散型r.v.

1. 记y_i = g(x_i)， (i = 1,2,...), y_i 的值互不相同；列表；
2. 如果g(x_i) 中的值不是互不相等的，需要把相等的类别和冰，根据加法公式把p_i 相加。得到对应的概率分布率；

## X 是连续型r.v.


- 设r.v. X具有概率密度 f_X(x)，求Y = 2X + 8的概率密度；$f_X(x) = \left\{ \begin{aligned} x / 8,& 0 < x < 4 \\ 0, & \text{others}\end{aligned} \right.$

> 先求$Y = 2X + 8$ 的分布函数$F_Y(y)；F_Y(y) = P \{ Y \leq y \} = P\{2X + 8 \leq y\}$；
>
> $P(X \leq \dfrac{y-8}{2}) = \int \limits^{(y-8)/2}_{-\infty}f_X(x) dx$
>
> $= \dfrac{(y-8)^2}{64}, 8 < y < 16$
>
> $f_Y(y) = F^{'}_Y(y) = \dfrac{y - 8}{32}, 8 < y < 32$

### 分布函数法


- 设随机变量$X$具有概率密度$f_X(x)， -\infty < x \infty$， 又设函数处处可导且恒有$g^{'}(x) > 0$（或者恒有$g^{'}(x) < 0$），那么$Y = g(X)$ 是连续型随机变量，其概率密度为：

$f_Y(y) = \left\{ \begin{aligned} f_X(h(y)) | h^{'}(y) | &, \alpha < y < \beta \\ 0 &, \text{Others} \end{aligned} \right.$

> 其中 $\alpha = \text{min} \{ g(-\infty), g(\infty)\}， \beta = \text{max} \{ g(-\infty), g(\infty)\}$，$h(y)$ 是$y = g(x)$ 的反函数；
