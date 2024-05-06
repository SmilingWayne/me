# Markdown 入门｜我的笔记工作流


!!! note "说在前面"
    - 我的日常记笔记工具：电脑，Visual Studio Code  + Markdown All In One 插件（如下）。安装即用。支持**同步预览**。

    ![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202404221551789.png)

    （正如其简介说的，All You Need to write Markdown）

    我在电脑端的记笔记窗口长这样：


    ![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202404270037162.png)


------------


## 小标题 {##header1}

```

# 这是一个大标题

## 这是小标题

### 这是更小的标题

```


-------------



## 要点 

**语法** :

```
- 这是一个要点 
- 这是第二个要点 
    - 这是一个子要点 
    - 这也是一个子要点
        - 这是子要点的子要点
- 这是第三个要点
```

**预览** :

- 这是一个要点 
- 这是第二个要点 
    - 这是一个子要点 
    - 这也是一个子要点
        - 这是子要点的子要点
- 这是第三个要点

----------

## 有序要点 

**语法** :

```text
1. 这是要点1
2. 这是要点2
    1. 这是子要点1
    2. 这是子要点2 
3. 这是要点3 
```

----------

## 引用 

**语法** : 
```
> 这是一个引用
> 
> 这也是一个引用 
> > 这是引用的引用！ 
> 
> 这还是一个引用

```

**预览** :
> 这是一个引用
> 
> 这也是一个引用 
> > 这是引用的引用！ 
> > > 这是引用的引用的引用！ 
> 
> 这还是一个引用

-------------
## 引用中的要点

**语法** : 

```
> 这是第一句话
> 
> - 这是第一句话的一个要点
> - 这是第一句话的第二个要点
```

**预览** :

> 这是第一句话
> 
> - 这是第一句话的一个要点
> - 这是第一句话的第二个要点





-----------------

## 超链接


**语法** :

```
<YOUR HYPE LINK> 
```

**预览** :

<https://markdown.com.cn>


------

## 带格式化的超链接

```
I love supporting the **[EFF](YOUR LINK 1)**.
This is the *[Markdown Guide](YOUR LINK 2)*.
See the section on [`code`](YOUR LINK 3).
```



**预览：**

I love supporting the **[EFF](https://eff.org)**.
This is the *[Markdown Guide](https://www.markdownguide.org)*.
See the section on [`code`](./MarkdownQuickStart.md).

-----------

## 带超链接的图片

```text
[![This is the homepage of my site]
(YOUR PHOTO PATH "我的网页照片")]
(YOUR HYPER LINK)
```

[![This is the homepage of my site](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202404201118510.png "我的网页照片")](https://smilingwayne.github.io/me/)


----------------------

## 删除线

~~Nooooo!!~~

```
~~Nooooo!!~~
```
    
## 分割线


- 专起一行输入`---------`，只要大于等于3个“-”就行。





## 行内代码块

- 用`\`` 符号对代码进行包裹即可；如： 

> `Hello!`


## 代码块

**语法** : (最后一行 {data-source-line} 是插件自动添加的，不需要写这个，直接用```进行包裹即可)

```text
```Python
print("Hi! This is Python")
```
```

**预览** ：

```Python
print("Hi! This is Python")
```



---------


## CriticMap 的新增格式

!!! example "内容展开"
    - [参考链接](https://github.com/CriticMarkup/CriticMarkup-toolkit)，一种新的 Markdown 编码风格
    - 在这里打总是会自己渲染，呈现原来的方式略显奇怪了～

   


---------------

## 任务列表



**语法** :
```text 
- [x] 任务1
- [x] 任务2
- [ ] 任务3
```

**预览** :

- [x] 任务1
- [x] 任务2
- [ ] 任务3


------

## 输入上下标


!!! note "下标 / 上标"

    **语法** :```H~2~O``` / ```19^th^century```

    **预览** : H~2~O / 19^th^century

    

---------


## 表格 

> **用途** ：不解释。就是表格。


**语法** ：

```text 
| Function name | Description                |
| ------------- | -------------------------- |
| `help()`      | Display the help window.   |
| `destroy()`   | **Destroy your computer!** |
```

**预览**：

| Function name | Description                |
| ------------- | -------------------------- |
| `help()`      | Display the help window.   |
| `destroy()`   | **Destroy your computer!** |



--------

## Admonition 💗💗（👍）

> 备注：我最喜欢的一种语法。可以制作一个文本框。设置文本框样式，在文本框内还可以兼容大部分Markdown语法，显示效果很好。并且在Vscode里预览渲染也很快。


```text 
!!! note / question / abstract / quote / answer / question "你的标题"
    这里是内容
```

规范一点写就是如下的：

```text 
!!! note "这是我的标题"
    这里是我的内容

!!! example "这是一个例子"
    这是例子的内容
```

> *预览如下：*

!!! note "这是我的标题"
    这里是我的内容

!!! example "这是一个例子"
    这是例子的内容
------




## 添加Annotations

> 尝试失败，尚不知具体原因。
>
> 失败链接：[传送门](https://squidfunk.github.io/mkdocs-material/reference/annotations/)

----------

!!! warning "笔者注：以下是一些高阶的markdown使用技巧。不一定所有支持markdown的工具都支持这些语法，但是在 VScode Markdown in One 插件下，均可正常使用"

## 添加缩写（Abbreviation）

```text
Here is What HTML

*[HTML]: Hyper Text Markup Language
```

结果：（鼠标悬浮在文字上即可看到）

Here is What HTML

*[HTML]: Hyper Text Markup Language

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202404221606232.png)

----

## 定义列表（Definition List）

> **用途**：适合使用简单的语法枚举任意键值对的列表，例如函数或模块的参数。

**语法** :
```text
Apple
:   Pomaceous fruit of plants of the genus Malus in 
the family Rosaceae.

Banana
:   Yellow!

Orange
:   The fruit! Not the color!

```
**预览** :

Apple
:   Pomaceous fruit of plants of the genus Malus in 
the family Rosaceae.

Banana
:   Yellow!

Orange
:   The fruit! Not the color!


----------

## 添加脚注（Footnotes）


**语法** :

```text

That's some text with a footnote.[^1]

[^1]: And that's the footnote.

    That's the second paragraph.
```

**预览** :

That's some text with a footnote.[^1]

[^1]: And that's the footnote.

    That's the second paragraph.


----------

## 页面锚点跳转（attribute block）

> **用途**：在同一个页面的不同标题之间进行跳转。

**语法**：

```text 

## 小标题 {##header1}


... (内容省略)

[跳转到小标题一栏](##header1)

```

**预览**：

[跳转到小标题一栏](##header1)

