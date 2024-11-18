# 网站界面美化：文本块｜字体

本章会简单介绍一下Mkdocs Materials主题如何适配常用的Markdown语法。在阅读后续内容前，需要确保已经实现了[第一篇：网站搭建](./Step1.md) 中的内容，如果已经实现了[第二篇笔记](./Step2.md)，效果会更好。

## [Admonitions](https://squidfunk.github.io/mkdocs-material/reference/admonitions/)

我最喜欢用的是 Admonitions。只需要在 `mkdocs.yml` 中加入以下内容：

```yml
markdown_extensions:
  - admonition
  - pymdownx.details
  - pymdownx.superfences
```

就可以使用了。

效果：

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202411181356572.png)


---

## 自定义样式等若干问题

**这个阶段是个非常好的讲解自定义格式样式的地方**。刚开始使用Admonition的时候，我觉得标题和文本框中的字体大小有点小。就在想，能不能调整调整。

这是可以的！首先你需要在 `docs` 文件夹下创建一个 `stylesheets` 文件夹。然后在这个文件夹下创建一个 `extra.css` 文件。

目录结构：

```text
├── stylesheets
│   └── extra.css
└── Part1
    ├── index.md
    ├── Paper1.md
    ├── Paper2.md
    └── yanTalks.md
```

然后，我们进入 `mkdocs.yml` 文件，加入下面的代码，能够把 `extra.css` 的内容同步到更新中。

```yml
extra_css:
  - stylesheets/extra.css
```

现在在 `extra.css` 中的更新，就可以反映在你的整个网页中了。

比如，我想要调整页面的宽度，就可以加入：

```css
.md-grid {
    max-width: 1440px;   
}
```

效果：

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202411181622158.png)

### 一个简单的例子

从mkdocs的官网可以知道，有一种 inline block 形式的 Admonition，可以在一行中显示多个Admonition。具体的语法是：

```markdown
!!! info inline end "Lorem ipsum"

    Lorem ipsum dolor sit amet, consectetur
    adipiscing elit. Nulla et euismod nulla.
    Curabitur feugiat, tortor non consequat
    finibus, justo purus auctor massa.
```

但是，如果在自己的页面中，一次性用多个内联，会发现经常出现“一行塞不下，两行空太大”的尴尬的情况（感觉前端应该经常出现...），比如：

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202411181646282.png)

**这里我们可以通过修改这个内联的 Admonition 的尺寸来实现一个美观的页面，同时还不影响其他的 Admonition 的格式。** 


我们默认，设置了页面宽度是 1280 px （见前）。此时，在 `extra.css` 中加入语句：

```css
.md-typeset .admonition.inline {
    width: 350px;   
    column-width: auto;
}
```

就可以发现，这个内联的Admonition的宽度被限制小了一点，使得一行中能比较美观地塞下2个框框了。

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202411181658379.png)

> 这个图是配置了字体后截的...懒得修改了，反正目的达到了！

---------

## 设置字体

我的个人网站用的字体是[霞鹜文楷](https://github.com/lxgw/LxgwWenKai)。你可以通过一些简单的设置即可配置。

首先，打开我们操作了很多次的 `mkdocs.yml`，修改 `extra_css` 为：

```yml
extra_css:
  - stylesheets/extra.css
  - https://cdn.jsdelivr.net/npm/lxgw-wenkai-screen-webfont@1.1.0/style.css
```

同时，在你的之前新建的 `extra.css` 中，导入我们的字体：

```css
:root {
    --md-text-font:  "LXGW WenKai Screen", sans-serif; 
    /* --md-code-font:  */
  }


@font-face {  	
    font-family: 'LXGW';  	
    src: url('./LXGWWenKaiGBScreen.woff') format('woff');/*IE*/  	
}
```

大功告成！我们的字体添加完毕了！现在你的页面里有属于自己的一套字体了！

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202411181658025.png)