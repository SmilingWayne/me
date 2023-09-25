# VS code 快捷键速查表


> ⌘ ： macOS 键盘上的command；
> ↑ / ↓ 键盘上的上下键；


<font size = 4></font>

|          <font size = 4>功能</font>           | <font size = 4>macOS</font>          | <font size = 4>Windows</font>          |
| :-------------------------------------------: | ------------------------------------ | -------------------------------------- |
|      <font size = 4>打开命令面板</font>       | <font size = 4>⌘ + Shift + P</font>  | <font size = 4>Ctrl + Shift + P</font> |
| <font size = 4>剪切（选中/未选中状态）</font> | <font size = 4>⌘ + X</font>          | <font size = 4> Ctrl + X</font>        |
|          <font size = 4>复制</font>           | <font size = 4>⌘ + C</font>          | <font size = 4>Ctrl + C</font>         |
|          <font size = 4>粘贴</font>           | <font size = 4>⌘ + V</font>          | <font size = 4>Ctrl + V</font>         |
|     <font size = 4>撤销前一个操作</font>      | <font size = 4>⌘ + Z</font>          | <font size = 4>Ctrl + Z</font>         |
|     <font size = 4>重做前一个操作</font>      | <font size = 4>Shift + ⌘  + Z</font> | <font size = 4>Ctrl + Y</font>         |
|        <font size = 4>打开终端</font>         | <font size = 4>Shift + ⌘ + Y</font>  | <font size = 4></font>                 |
|          <font size = 4>查找</font>           | <font size = 4>⌘ + F</font>          | <font size = 4>Ctrl + F</font>         |
|   <font size = 4>在目录文件夹中查找</font>    | <font size = 4>Shift + ⌘ + F</font>  | <font size = 4>Ctrl + Shift + F</font> |
| <font size = 4>移动到下一个查找目标处</font>  | <font size = 4>⌘ + D</font>          | <font size = 4>Ctrl + D</font>         |
|      <font size = 4>打开/关闭侧栏</font>      | <font size = 4>⌘ + B</font>          | <font size = 4>Ctrl + B</font>         |
|  <font size = 4>d打开 / 关闭底层面板</font>   | <font size = 4>⌘ + J</font>          | <font size = 4>Ctrl + J</font>         |
|     <font size = 4>查找并选中所有</font>      | <font size = 4>Shift + ⌘ + L</font>  | <font size = 4></font>                 |
|      <font size = 4>注释掉一整行</font>       | <font size = 4>⌘ + /</font>          | <font size = 4>Ctrl + /</font>         |
|        <font size = 4>快速打开</font>         | <font size = 4>⌘ + P</font>          | <font size = 4>Ctrl + P</font>         |
|       <font size = 4>上移动一行</font>        | <font size = 4>Option + ↑ </font>    | <font size = 4>Alt + ↑</font>          |
|       <font size = 4>下移动一行</font>        | <font size = 4>Option + ↓</font>     | <font size = 4>Alt + ↓</font>          |
|        <font size = 4>搜索文档</font>         | <font size = 4>⌘ + P</font>          | <font size = 4>Ctrl + P</font>         |
|   <font size = 4>移动到这一行最前面</font>    | <font size = 4>Option + ←</font>     | <font size = 4>Alt + ←</font>          |
|   <font size = 4>移动到这一行最后面</font>    | <font size = 4>Option + →</font>     | <font size = 4>Alt + →</font>          |
|    <font size = 4>移动到文本最开头</font>     | <font size = 4>⌘ + ↑</font>          | <font size = 4>Ctrl + ↑</font>         |
|    <font size = 4>移动到文本最末尾</font>     | <font size = 4>⌘ + ↓</font>          | <font size = 4>Ctrl + ↓</font>         |
|      <font size = 4>跳跃到某一行</font>       | <font size = 4>ctrl + G</font>       | <font size = 4>Ctrl + G</font>         |
|       <font size = 4>分屏到右边</font>        | <font size = 4>command + \</font>    | <font size = 4>Ctrl + \</font>         |



------

- `launch.json`： 用来debug的文件
- 更换ARM架构的Apple Silicon之后，VS code 提醒

```text
You are running an emulated version of Visual Studio Code. For better performance download the native arm64 version of Visual Studio Code build for your machine.
```

> 表明有更加高效的VS code，自己现在用的是模拟版；解决方法是去官网下载专供Apple Silicon的VScode并最好把自己原来的删除掉（不然你用快捷键打开可能打开的还是原版）
>


- 什么是App的冷启动和热启动？
    - **冷启动**：当启动应用时，后台没有该应用的进程，这时系统会重新创建一个新的进程分配给该应用；
    - **热启动**：当启动应用时，后台已有该应用的进程（例：按home键回到桌面，但是该应用的进程是依然会保留在后台，可进入任务列表查看），所以在已有进程的情况下，这种启动会从已有的进程中来启动应用；

> 用ARM特供的VScode 冷启动速度明显流畅快速了很多。


--------


- 支持在终端中直接用Vscode 打开文件：++command+shift+p++，在窗口中输入shell command 就可以出现“把code添加到路径中”，设置好之后就可以直接通过终端打开当前文件路径的文件夹了。


- 我的快捷输入方式：

> VScode 是支持自定义快速输入的，你只要输入一个短句，会自动把符合格式的长句子输出出来。具体方法是：左上角菜单栏 Code -> Settings -> Configure User Snippets，可以选择在哪些文件中用什么方法输入。

- 运行Markdown preview插件出现："princexml" is required to be installed.的解决方案：

> 没有安装princexml。可以前去 [Princexml install](https://www.princexml.com/doc/installing/) 探索安装；

