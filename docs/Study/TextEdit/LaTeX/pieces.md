
# 一些没用的知识


!!! Tips
    感谢链接 : 

    - [https://www.luogu.com.cn/blog/over-knee-socks/latex-gong-shi-tai-quan-fixed](https://www.luogu.com.cn/blog/over-knee-socks/latex-gong-shi-tai-quan-fixed)
    - [https://katex.org/docs/supported.html](https://katex.org/docs/supported.html)
    - [https://www.mathjax.org](https://www.mathjax.org)
    - [https://facelessuser.github.io/pymdown-extensions/extensions/arithmatex/#loading-katex](https://facelessuser.github.io/pymdown-extensions/extensions/arithmatex/#loading-katex)


## $\TeX$ | $\LaTeX$ | $\KaTeX$

- $\TeX$ 是一个主要由美国计算机教授高德纳（ Donald Ervin Knuth ）编写的排版系统。 TeX 被普遍认为是一个优秀的排版工具，尤其是对于复杂数学公式的处理。利用LaTeX 等终端软件，TeX 就能够排版出精美的文本以帮助人们辨认和查找。

- $\LaTeX$: LaTeX 是一种基于 $\TeX$ 的 ==排版系统== ，由美国计算机科学家莱斯利·兰伯特在 20 世纪 80 年代初期开发，利用这种格式系统的处理，即使用户没有排版和程序设计的知识也可以充分发挥由 TeX 所提供的强大功能，不必一一亲自去设计或校对，能在几天，甚至几小时内生成很多具有书籍质量的印刷品。

- $\text{MathJax}$: Beautiful and accessible math in all browsers. A JavaScript display engine for mathematics that works in all browsers. No more setup for readers. It just works. 一个JavaScript的数学公式显示引擎，在浏览器端提供数学公式的显示效果，无需特殊的浏览器设置，直接在HTML源代码中支持$\LaTeX$，MathML和其他公式标记。


- $\KaTeX$: 最快的浏览器网络数学符号排版库（JavaScript）。它特别强调快速和易于使用。$\KaTeX$ 可以同步呈现其数学运算，无需重排页面。

- $\text{Arithmatex}$： Arithmatex是一个扩展，用于衔接Markdown到网页端显示$\LaTeX$的问题。它在Markdown转换过程中保留了$\LaTeX$数学方程式，以便它们可以与MathJax等库一起使用。如果你更喜欢使用MathJax以外的其他东西，Arithmatex可以输出一种更通用的格式，适合其他库，如$\KaTeX$。这也是本网站搭建的核心组成部分。
- $\text{Markdown}$ 和上述内容的关系：没啥关系。$\TeX$ 系列是专门处理数学公式的，但是 $\text{Markdown}$ 是专门文章排版、结构的。