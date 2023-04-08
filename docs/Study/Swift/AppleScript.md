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