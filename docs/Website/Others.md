# 本网站格式设定的一些方法

## 如何自定义css样式

在配置文档`mkdocs.yml`下，补充语句：

```yml
extra_css:
  - stylesheets/extra.css
```

然后，在`docs/stylesheets/`目录下（一开始你可能需要自己创建`stylesheets`文件夹），添加`extra.css`文件，会自动用这个css文件里设定的格式覆盖掉原来的默认样式。

## 修改内容部分的宽度

运营之后发现，自己的网站正文，大致呈现一种瘦长型的布局，导致周围有很多留白，空荡荡的。虽说窄窄的呈现方式也有好处（比如我一直劝自己这样向下滑动网页就类似慢慢展开一张信纸📃....)，Anyway, 我更喜欢灵活一点的方法。

你可以在[这个链接](https://squidfunk.github.io/mkdocs-material/setup/setting-up-navigation/#content-area-width)找到具体的实现。

在`docs/stylesheets/`目录下，添加`extra.css`文件。并加入如下语句，即可。效果如下。

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202407271034500.png)

```css
.md-grid {
    max-width: 1280px;   
}
```

## 修改admonition的格式

我们把如下的这种文本框，称作`Admonition`。

!!! note "这是一个Admonition的展示"
    Hello world!这是14px大小的字！看起来大多了！

最开始的时候，文本框内的字体有点小，看起来会比较费力。事实上，可以通过自定义来调节。同样是在`docs/stylesheets/`目录下的`extra.css`文件。加入如下内容。

```css
.md-typeset .admonition,
.md-typeset details {
    font-size: 14px
}
```

就可以把正文的内容设置为14px字体大小的了。

更改后效果：

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202407271040703.png)

## 如何设置你的字体

（待补充）

## 如何设置图片的cdn分发

简单说一下这部分在干什么。一般而言写博客，尤其是知识分享的，会需要放一些图片。一个简单的方法是在你的文本文件夹同目录下，创建一个专门的文件夹存放这些图片。但是这里有个问题。本身文本文件夹就已经有不少文件了，还要专门维护一个图片文件夹，平时找的时候还不方便，还会占用干净的文本目录。比较冗长。

所以，我们可以不可以，实现一种可持久、简单、轻量的管理自己图片的方式呢？譬如，我们是不是可以专门用一个github仓库存放所有的图片，然后通过页面超链接的方式呈现在我们的网站上？

这样做的**好处**是：

1. 网站只存储配置文件和你的内容，你可以更加专注于写作；
2. 你的图片借助GitHub实现了持久化存储；
3. 精简了你的文件目录结构，你的网站文件夹也减轻了配重；

我的解决方案是[Picgo](https://picgo.github.io/PicGo-Doc/)。简单好用，支持多平台（Mac/Win/Linux）。它的官网有中文介绍，包括如何下载、如何配置链接到你的Github、生成key等。按照它的流程走即可。

> 遇到问题多看看它的GitHub Issue及解答。

