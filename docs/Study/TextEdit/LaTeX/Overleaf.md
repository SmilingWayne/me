# Overleaf 使用技巧

## 设置自动换页、跨多行、自动填满整行的表格

```LaTeX
\begin{footnotesize}
\renewcommand\arraystretch{0.9}
\setlength\LTleft{0pt}
\setlength\LTright{0pt}
\begin{longtable}{@{\extracolsep{\fill}}cccc@{}}
\caption{重大工程创新生态系统与模型的映射关系} 
\label{projection}\\
\toprule
\textbf{主体} & \textbf{属性} & \textbf{现实} & \textbf{模型} \\
\endfirsthead
\endhead
\midrule
\multirow{8}{*}{科研院所} &
  知识资源 &
  \makecell[c]{主体的知识水平，\\ 是推动创新发展的基础；} &
  \multirow{3}{*}{\makecell[b]{主体的知识、信息、技术\\ 资源共同构成其创新资源，\\ 资源总和代表主体体量。\\ 创新资源越多，越容易产生\\ 创新绩效。}} \\
 &
  信息资源 &
  \makecell[c]{主体的信息共享水平，能够\\ 减少主体间摩擦、\\ 提高协作水平；} &
   \\
 &
  技术资源 &
  \makecell[c]{主体的技术水平，项目核心\\ 技术的掌握水平；} &
   \\
 &
  资源吸收水平 &
  科研院所吸收扩散知识的能力 &
  环境中创新资源吸收率 \\
 &
  \makecell[c]{科研单位-企业\\ 协同合作水平} &
  科研成果落地应用、完成转化 &
  科研单位-企业资源转化率 \\
 &
  \makecell[c]{科研单位间\\ 协同合作水平} &
  学术研讨、分享与交流 &
  科研单位间资源转化率 \\
 &
  进入与离开 &
  \makecell[c]{合作中断、主体退出、\\ 主体更换等现象} &
  主体灭亡、复制、置换 \\
 &
  创新成本 &
  \makecell[c]{整合成果，产生创新绩效；\\ 需要消耗一定资源} &
  \makecell[c]{实现创新绩效增长\\ 需要消耗的额外资源}   \\
\multirow{3}{*}{工程企业} &
  \makecell[c]{企业间\\ 合作水平} &
  \makecell[c]{项目工程分包、合作、\\ 企业联盟等} &
  企业间资源转化率 \\
  &
  资源吸收水平 &
  \makecell[c]{工程建设企业吸收\\ 扩散知识的能力} &
  \makecell[c]{与科研单位不同的\\ 创新资源吸收率}   \\
  & 
  行为成本 &
  \makecell[c]{主体合作创新产生的\\ 资源损耗} &
  \makecell[c]{不同种类的主体之间\\ 单位损耗量不同}   \\
业主 &
  补贴主体数量 &
  \makecell[c]{单位时间内给\\ 不同数量主体额外资源} &
  补贴覆盖的主体个数 \\ \bottomrule\end{longtable}
\end{footnotesize}
```


----------

## 设置页眉、页脚、页眉横线

```LaTeX
\usepackage{fancyhdr} %调用宏包

\fancypagestyle{MyFootName} % 这里的MyFootName可以自定义名字
  {
    
    \fancyhf{}
    \fancyhead[c]{\leftmark} 
    \fancyfoot[c]{\thepage}
    \renewcommand{\headrulewidth}{0.5mm}
    \fancypagestyle{plain}{
        \pagestyle{fancy}
    }
    % \renewcommand{\footrulewidth}{0.1mm} // 设置是否有页脚横线
}

\pagestyle{MyFootName}
```

------------


## 添加图片、设置横幅

```LaTeX

\begin{figure}[H]
    \centering
    \includegraphics[width=0.9\textwidth]{pictures/ChinaInfrasturcture.png}
    \caption{2018至2021年中国大型基础设施投资增长率（数据来源：Statista）}
\end{figure} 


\noindent \begin{figure}[H] 
    \centering
    \includegraphics[width=1\textwidth]{pictures/systemdynamics.png}
    \caption{创新生态系统因果反馈回路图}
    \label{sd1}
\end{figure} 


```

-----------

## 取消段落开始的空格

```LaTeX 
\noindent
```


----

## 设置公式的序号


```LaTeX

\begin{equation}P_{coop} = \alpha + k_1 Q + k_2 Z\end{equation}
```


---- 

## 引用自己的文献里的内容

```LaTeX
\cite{ XXX } % 引用参考文献
\ref{} % 引用图片 / 表格，对应 \label{} 中的内容
```


-----

## 处理一些字无法显示

> 首先下载一个字体（我使用SIMSUN.ttf），放到当前的项目根目录下；
>
> 然后导入：

```LaTeX
\usepackage{xeCJK}
```
> 然后对你要写的字

```LaTeX

{\CJKfontspec{SimSun.ttf} 旻}

```
