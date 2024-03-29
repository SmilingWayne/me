# 苹果工具箱🔧

## AppleScript | Automator 

- [https://discussions.apple.com/thread/253764288?page=1](https://discussions.apple.com/thread/253764288?page=1)，今天试图用Automator功能实现一个PDF合成器，但是发现效果并不好，并且会有一个报错
    - The operation couldn’t be completed. Command line tool returned error 127.: 127
    - 最终上述链接指出问题在于12.3Monteray之后PDF merge似乎取消了对Python命令的支持，所以导致报错；
    - 无意中发现了[https://www.icloud.com/shortcuts/1d06d44ffe7a442a9f90d3eb72164b02](https://www.icloud.com/shortcuts/1d06d44ffe7a442a9f90d3eb72164b02)。这个功能更强并且可以在Finder中直接使用；


- [https://b23.tv/jfi45n4](https://b23.tv/jfi45n4)
    - 在聚焦搜索中选中要打开的，command + 双击可以直接打开文件所在的finder位置


- mac的不分区管理文件的原理📃Finder就是干这个的
    - 自定义边栏、自由度
    - Macintosh HD：mac的硬盘（hard Drive）所在地；就相当于“我的电脑”
        - System 和Library是储存系统软件配置文件的；强烈建议不要动，不到百分百确定不要进行任何修改；
        - Cmd + 方向上键：回到上一个文件夹
        - Clean up 功能：对于图标状态下特别好用
        - 多选后Rename可以提供格式化修改名称的功能
        - 充分利用打标签的功能！


## Safari 浏览器
- Chrome 浏览器和Safari的书签收藏目录是可以互转的；Export to HTML format 就可以直接导入；


## 快速备忘录功能
- 右下角探头探脑的小jiojio
- 快捷键 fn + Q 即可
- Safari 中支持New Quick Note，可以保存网页和内容
<br>
<br>
<br>
<br>
<br>

## macOS  13 输入法卡顿解决方案🔧

- 这个问题还是挺普遍的，原因很清楚了但是Apple似乎一直没有修复这个Bug：简体中文输入法(Simplified Chinese Input Method)和系统不兼容；


- 之前也有小🍠博主推荐了三种解决思路，原po有暂时的方法（1，2）有根治的方法（3），强烈建议大家移步最后一图去详细了解。总共三个：
  1. 👉 终端(terminal)命令强制终止
  2. 👉 活动监视器强制终止
  3. 👉 更换自己的输入法
- 我很有幸在本月（一边写论文一边）卡顿了将近十次。上述三种方法均尝试过，都是有效的，但是遇到了几个问题：
  - **卡顿发生的时候整个电脑几乎全部无响应**，只要点击了程序或者文件，就**立刻无响应需要强制关闭重开**，鼠标点击、键盘输入十分缓慢，以至于解决方案一和二虽能实现，但是耗时太长，很容易心态b溃。我第一次耗了10min才从终端输入完毕
  - 方案3，对原生输入法有巨大依赖的本人不友好，接受不了突然更换输入法，适应时间太长
- 我用图二的方法解决的，思路是在crontab（一种操作系统命令？）中设置每2h关闭重启一次中文输入法。
- 目前没有遇到问题！


1. 先在融合搜索中输入terminal（终端），打开之后输入命令
	
```
crontab -e
```
	
2. 此时会打开一个系统文件，但是你会发现直接输入啥也改不了，需要一些特殊方法输入（熟悉vim的小伙伴应该懂怎么做），具体操作就是先摁一下键盘i 键，然后你就可以在这里输入了，具体只需要输入
	
```
0 */2 * * * kill `pgrep SCIM`
```
	
（注意⚠️ 最后那个不是单引号，是电脑键盘esc下面那个波浪号，用英文输入法打出来就是那个小啾啾了）
	
（再注意⚠️，上面命令里的2表示“每隔两小时kill一次输入法，如果不放心可以把2改成1，这样就每隔一小时kill一次输入法了）
	
3. 输入完了之后先摁一下esc键（退出编辑模式），然后直接输入
	
```
:wq
```
	
注意⚠️ 冒号也是英文的。这个指令表明退出这个文件。
	
4⃣️ 这个时候按道理说会出现图3⃣️说的一个提示，告诉你terminal要更改你的系统设置blabla，点击allow即可。
	
大功告成~
<br>
<br>

<br>

## reminder和备忘录的关键词功能
- 很好用，可以进行一些简单的分类
- 智能文件夹的功能


## 一些零碎小知识


- 什么是repl：

    > 在编程中，REPL 是指“Read-Eval-Print Loop”的缩写，即“读取-求值-打印循环”，是一种交互式的编程环境。在 Swift 中，REPL 是一个交互式的命令行工具，可以在其中输入 Swift 代码，并立即查看结果。
    > 
    > 在 Swift 的 REPL 中，用户可以像在编写脚本一样快速编写和测试代码，以便更快地进行代码迭代和调试。REPL 还可以用于学习 Swift，因为它允许用户快速尝试不同的代码片段，而不必编写完整的应用程序。
    > 
    > Swift REPL 的使用非常简单。用户只需要在终端中输入“swift”命令即可进入 REPL 环境。一旦进入 REPL 环境，用户就可以输入任何有效的 Swift 代码，并查看结果。在 REPL 中，用户可以使用 Swift 中的所有语言特性和标准库函数。
    > 
    > 总的来说，Swift REPL 是一种非常有用的工具，可以加速代码开发和调试的过程，并提高学习 Swift 的效率。   


- 什么是homebrew
> 一种安装命令行程序

- 什么是clang
> Apple 平台的一种编译器。

- 为什么.exe 文件在mac上无法打开使用
> 因为数组组织方式在windows和mac上是完全不同的，必须要用专门的文件方法改变文件的数据组织格式。

- 什么是gcc / g++
> gcc: Linux 平台下一种C语言的编译器
> g++：Linux 平台下cpp的编译器

```text
g++ hello.cpp -o hello.out
```


## 在mac上生成文件目录结构

```
.
├── code
│   └── clean_data.ipynb
├── figures
│   ├── ChannelFigure.png
│   ├── Sales_Sku1_Store1.png
│   └── Sales_Sku432_Store6.png
├── 公开数据
│   ├── offline_store_sku_quant.csv
│   ├── test.csv
│   └── test_item.csv
└── 评测脚本
    └── 参赛选手自测程序说明
```

windows下在CMD中可以直接用指令tree来生成树状图。在mac下也有对应的方法。

1. 用brew安装tree

```shell
brew install tree
```

2. 进入你想要生成结构的文件（根目录）
3. 在命令行执行：

```shell
tree
```

就可以了。如果你想要更加准确地进行控制（比如生成一级目录），那就：

```shell
tree -L 1
```