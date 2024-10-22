# 网站界面美化：主题、自定义样式

!!! abstract "本部分默认已经完成了[第一篇笔记](./Step1.md)中的内容，即你已经完成了个人网站的搭建，已经按照第一篇文章那样部署并托管在了Github Pages上。本部分将介绍如何美化个人网站，包括主题选择和自定义样式等。"

## Mkdocs 主题 Materials介绍

首先简单说说什么是Materials. 可以看看它们的官网，用Markdown编写文档，在几分钟内创建一个专业的静态文档。最重要的是它基于mkdocs框架，提供了**更现代的主题和样式**，并且支持自定义大部分样式，**这为我们搭建符合自己审美的个人网站提供了更多易上手的选择**。我是没有什么前端后端开发经验的，但是搭建整个网站的过程中，最大的感触就是：“按照说明书一步步执行”。搭建网站的从0到1，**执行力比想象力更重要。**

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202410220956399.png)

## 在网站中应用 Materials

现在我们依然按照上一节的方法，手把手安装和实现。

首先在上次你安装的虚拟环境中，安装一些需要的依赖：

```shell
pip install mkdocs-material
```

现在，在上次生成的那个 `mkdocs.yml` 文件中，加入如下的语句：

```yml
site_name: My Docs
site_url: https://smilingwayne.github.io/LeetCode/
theme:
  name: material
```

这里需要把site_url 后面的链接改成上次部署在Github Pages生成的那个地址，也就是默认 `index.md` 打开的那个链接。具体是什么，上次的文章里有写。记下这个网址。

**好的，现在我们就把materials应用到我们的网站中了！** 你可以在终端里（记得进入你用pip安装了mkdocs的那个虚拟环境中！）执行：

```shell
mkdocs serve
```

然后会出现如下显示：

```txt
(py310_x64) xxMBP:LeetCode apple$ mkdocs serve
INFO    -  Building documentation...
INFO    -  Cleaning site directory
INFO    -  Documentation built in 0.16 seconds
INFO    -  [10:07:30] Watching paths for changes: 'docs', 'mkdocs.yml'
INFO    -  [10:07:30] Serving on http://127.0.0.1:8000/LeetCode/
```

注意最后一行的那个127.0.0.1 开头的链接，在浏览器端打开。就会看到：

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202410221008054.png)

是不是一下子就显得好看多了，干净整洁，而且侧栏、搜索框都有了。这就是Materials的效果。**而且非常好上手，非常容易操作。**


### 设置导航栏

现在我们进一步对自己的网站进行美化。比如我想在网站里设置多个栏目，每个栏目里放不同的文档，从而方便自己进行专业化的管理。

现在我在自己仓库里的 `docs` 文件夹下新建一些文件夹，命名为 `Part1`，`Part2` 等，并且在每个文件夹下新建一个 `index.md` 文件，里面写上一些内容。现在我们的仓库结构：

```text
.
├── README.md
├── docs
│   ├── Part1
│   │   └── index.md
│   ├── Part2
│   │   └── index.md
│   ├── Part3
│   │   └── index.md
│   └── index.md
└── mkdocs.yml

5 directories, 6 files
```

并且把我们的mkdocs.yml 文件修改为：

```yml
site_name: 我的仓库
site_url: https://smilingwayne.github.io/LeetCode/

nav:
  - 首页: index.md
  - 第一部分:
      - Part1/index.md
  - 第二部分:
      - Part2/index.md
  - 第三部分:
      - Part3/index.md
docs_dir: docs/

theme:
  name: material
  features:
    - navigation.tabs
    - search.suggest
    - search.highlight
    - search.share
    - navigation.top
    - navigation.indexes
```

现在来解释一下我们究竟做了什么。首先，需要知道如下两点：

1. **我们在网站中展示的文档目录结构，和我们 `docs` 文件夹中的结构是一模一样的**，所以你需要比较谨慎地处理 `docs` 文件夹中的文件。
2. 每个文件夹下都可以视为网站的一个板块（存放一些文档），每个文件夹下如果有 `index.md` 文件，那么网站会自动把这个 `index.md` 作为点开这个板块时默认打开的页面。比如你想对这个板块做一个“总结”，或者写一点“说在前面”，那么你只需要在这个板块下建立 `index.md`文件即可。

!!! note "现在介绍一下刚刚我们的`mkdocs.yml`代码做了什么"
    首先， `nav: ` 后面表示的是网站要显示的目录结构。我们在这里定义了四个板块，分别是首页、第一部分、第二部分、第三部分。其中，首页就是 `docs` 文件夹下的 `index.md` 文件，第一部分就是 `docs` 文件夹下的 `Part1` 文件夹，以此类推。**注意，这里定义的板块顺序，就是网站中显示的顺序。**

    然后，我们在 `theme` 里设置了具体的格式和样式，比如 `navigation.tabs` 表示**显示侧边栏**的标签，`search.suggest` 表示显示**搜索框**，`search.highlight` 表示搜索时高亮显示，`search.share` 表示分享搜索结果，`navigation.top` 表示显示顶栏，`navigation.indexes` 表示显示目录。具体的解释就不展开，你可以参考 mkdocs materials 的官网链接去查看。

现在你再通过 `mkdocs serve` 命令本地预览网站，会发现网站有了新的目录结构，我们也有了页面最上面的导航栏！

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202410221043782.png)

如果我们继续在 `docs/Part1/` 文件夹下添加文档，并且将我们的 `mkdocs.yml` 等的`nav` 部分添加一条关于新的文档的描述，如下：

```yml
nav:
  - 首页: index.md
  - 第一部分:
      - Part1/index.md
      - 随机文本: Part1/File1.md
  - 第二部分:
      - Part2/index.md
  - 第三部分:
      - Part3/index.md
docs_dir: docs/
```

就会发现，点开这一栏目后能显示更多的内容：

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202410221048555.png)

好的！现在你已经学会了如何组织你的页面板块结构并添加更多文档，从现在开始你就可以更新文档并维护自己的网站了！


## 自定义自己的网站细节


### 修改页脚

现在我们来修改一些小的细节。比如，我们想要在页脚的位置，添加一些关于自己的链接。比如你是个Ins重度使用者，或者想公开自己的邮箱，你可以在 `mkdocs.yml` 中添加如下的代码：

```yml
extra:
  social:
    - icon: fontawesome/brands/github
      link: https://github.com/XXXXX
    - icon: fontawesome/brands/instagram
      link: https://www.instagram.com/XXXXXX
    - icon: fontawesome/solid/paper-plane
      link: mailto:XXXX@163.com
copyright: Copyright &copy; 2022 - 2024 xiaoxiaoWayne
```

注意把隐去的部分改成自己的内容。此时你就可以在左侧/右侧页脚看到下面的：

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202410221100475.png)

注意，这些图标都是可以修改的，修改方式依然是参考Materials的官网。


### 增加明暗模式

一般网站都支持明暗模式切换，这样在白天和夜晚浏览时能够比较灵活地处理亮度。在Materials中也提供了很简单的增加这个功能的方法。在 `mkdocs.yml` 中添加如下代码，注意，这里的符号样式也是可以更改的。

```yml
theme:
  palette:
    - media: "(prefers-color-scheme: light)"
      scheme: default
      toggle:
        icon: material/weather-night
        name: Switch to dark mode
    - media: "(prefers-color-scheme: dark)"
      scheme: slate
      toggle:
        icon: material/weather-sunny
        name: Switch to light mode

```

切换后效果：

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202410221153565.png)

其实Materials还有很多其他的新颖的功能，十分建议感兴趣的同学直接去搜 Mkdos Materials 的官网，里面的教程十分容易上手。

后续这个系列会继续更新一些其他我觉得很有用的功能，比如：修改字体、修改主要内容大小、图片同步等。

