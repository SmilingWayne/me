---
tags:
  - 网站搭建
---

# 从零开始零成本搭建你的个人网站：一

!!! abstract "说在最前面"
    本笔记会0成本、手把手搭建一个和这个页面类似的个人网站。预计会分成好几个部分完成更新。走完这一篇笔记的内容，你可以实现：

    1. 使用 Mkdocs 完成框架搭建；
    2. Git 基础用法；
    3. 使用 Github Pages 完成网站托管，可以通过网址实时访问你的网站。

    现在，**我们直接开始。** 本文需要的前置配置：安装好Python，Git版本控制工具，能够用conda或者类似的依赖管理工具，创建一个Python虚拟环境；注册一个Github账号。就可以开始了。总体而言适合有一定相关基础的同学。也推荐感兴趣的同学边做边看边学。因为**一点也不难**。

## 一、基础设置

一些基础配置的安装并不是本笔记的重点，因此不在本文重点讨论的范围中，依照你的操作系统，可以访问如下链接或者搜索其他网络教程。这里省略。在进入下一个阶段前，你需要：

- [x] 安装好 Python（建议用Anaconda，可以省去很多麻烦）；能够创建一个虚拟环境。
- [x] 注册一个Github账号；
- [x] 安装好Git版本管理工具。

|      操作系统       |  类型  |                                 链接                                  |
| :-----------------: | :----: | :-------------------------------------------------------------------: |
| macOS/Windows/Linux |  Git   |                [下载](https://git-scm.com/downloads/)                 |
| macOS/Windows/Linux | Python | [下载](https://www.python.org/downloads/)<br>https://www.anaconda.com |
|         All         | github |                          https://github.com                           |

以下教程基于我的配置进行。由于我是macOS系统，部分路径等和windows下的稍有不同。

----

## 二、Mkdocs 框架搭建

!!! question "Mkdocs 是什么"

    Mkdocs 是一个用 Markdown 写作，用 Python 编写的静态网站生成器。它非常轻量，可以快速搭建一个静态网站，并且可以方便地部署到 Github Pages 上。Mkdocs 的官方文档：[参考链接](https://www.mkdocs.org/user-guide/installation/)。

首先，你需要先创建一个Python虚拟环境。在终端（对应Windows中的 CMD Lines 命令行工具）里执行：

```shell
conda create -n py310_x64 python=3.10
```

然后激活这个虚拟环境：

```shell
conda activate py310_x64
```

这时，确保你终端中的显示是类似这样的，前面括号内的(py310_x64)表示你当前的虚拟环境。

```text
(py310_x64) xxMBP:Desktop apple$ 
```

接下来，我们用pip安装 Mkdocs：

```shell
pip install mkdocs
```

确保安装完毕后，现在，你需要进入你想要存放网站文件夹的路径，比如电脑桌面：

```shell
cd ~/Desktop
```

此时执行命令：

```shell
mkdocs new LeetCode
```

你需要把 `LeetCode` 改成你想给网站文件夹设置的名字。以上述命令为例，这个命令会创建一个新的、叫做 `LeetCode` 的 Mkdocs 项目。执行时终端会有显示：

```text
(py310_x64) xxMBP:Desktop apple$ mkdocs new LeetCode
INFO    -  Creating project directory: LeetCode
INFO    -  Writing config file: LeetCode/mkdocs.yml
INFO    -  Writing initial docs: LeetCode/docs/index.md
```

注意到，这个时候在你的当前路径下会出现 LeetCode 文件夹。我们打开这个文件夹，会看到已经自动生成了几个简单的文件。如下所示：

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202410120947325.png)

走到这里，你已经完成了Mkdocs整体的框架搭建。你可以在终端中进入刚刚创建的 `LeetCode` 文件夹：

```shell
cd LeetCode
```

然后执行命令：

```shell
mkdocs serve
```

会有如下输出：

```text
(py310_x64) xxMBP:LeetCode apple$ mkdocs serve
INFO    -  Building documentation...
INFO    -  Cleaning site directory
INFO    -  Documentation built in 0.05 seconds
INFO    -  [09:48:41] Watching paths for changes: 'docs', 'mkdocs.yml'
INFO    -  [09:48:41] Serving on http://127.0.0.1:8000/
INFO    -  [09:48:45] Browser connected: http://127.0.0.1:8000/
WARNING -  [09:48:45] "GET /apple-touch-icon-precomposed.png HTTP/1.1" code 404
WARNING -  [09:48:45] "GET /apple-touch-icon.png HTTP/1.1" code 404
```

可以看到一个链接：`http://127.0.0.1:8000/`。在浏览器里打开，你会看到如下界面：

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202410120951134.png)

这些文字是不是很熟悉？没错，就是刚才图里我们点开的 `index.md` 中的文本经过页面渲染后的内容。

嗯。如果走到这一步都显示正常，那恭喜。说明我们的网站框架已经搭建完毕了。

---

## 三、推送到 Github 仓库

现在我们有了自己的本地仓库，**但是没法发布出去，让别人也能够浏览和查看我们的网站**，这时候我们就需要用Github Pages帮我们免费托管。这样，我们就把自己的网站发布出去，别人通过网址就可以访问我们的网站了。这也是这一步和下一步我们实际要做的事情。

!!! example "我们实际上是把自己的网站的整个文件夹放在GitHub的一个仓库里，Github Pages相当于一个==根据这个仓库搭建的网站或者博客==，生成对应的网址。搭配Github Actions，可以在每次我们向这个仓库里推送代码、修改内容的时候自动检测，将更新的内容自动同步到对应的网址上。[参考链接](https://www.github-zh.com/getting-started/github-pages)(中文版)"

所以，首先我们需要建立一个空的Github仓库，把它和我们本地仓库连接起来，在下一个章节再继续讨论如何使用Github Pages. 现在我们新建一个仓库，比如这样：

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202410121010694.png)

为了避免后续推代码给新手带来困扰，我们一开始不需要加一些额外的东西，就用如上设置。

创建好了github仓库之后，需要把我们在第二步创建的网站文件夹和仓库连接起来。接下来是经典的几个git 操作。依然在终端（命令行界面）完成。注意，你必须先进入刚刚的路径中。

依次执行：

```shell
git init
```

```shell
git add .
```

```shell
git commit -m "init repo"
```

> 这里的 `init repo` 可以更换成任意描述，用来概括你此次提交代码的行为。

```shell
git branch -M main
```
> 切换到main分支


```shell
git remote add origin https://github.com/YourGithubName/YourRepoName.git
```

> 连接远程分支。注意把YourGithubName替换成你的github账号，YourRepoName替换成你的仓库名


最后一步，执行：

```shell
git push -u origin main
```

推送代码。

此时你再访问你的github仓库，诶，会发现里面有东西了。


![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202410121019638.png)

> 这里我在推送之前，多新建了 `README.md` 文件，所以会在仓库首页显示一个README。如果你没有添加，则显示会略有不同，但是没有什么影响。反正后续再推送代码就可以了。

如果你实现到这一步，说明推送到 GitHub 仓库这一步你也顺利完成了！我们即将进入最后一步。

----

## 四、使用 Github Pages 完成网站托管

现在我们到关键一步。我们需要用Github自带的 Github Actions自动化地执行我们想要的操作。比如，我们希望它在每次我们更新main分支的时候，自动地部署我们的网页内容到Github Pages上。该怎么实现呢？

首先，在我们刚刚创建的仓库（LeetCode）里**创建一个文件夹**：`.github`。注意！这个文件名前面有一个英文的 `.` 别忘记了！**这个文件名不能修改。**

在这个 `.github` 文件夹下**再创建**一个文件夹 `workflows`。**这个文件夹名字也不能更改。**

然后，在 `.github/workflows` 文件夹下创建一个文件：`update.yml` 。这个文件名可以改，但是必须要是一个 `.yml` 文件。

然后，把下面这段内容复制到这个 `update.yml` 文件中：

```yml
name: update
on:
  push:
    branches:
      - main
permissions:
  contents: write
env:
  TZ: Asia/Shanghai
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Configure Git Credentials
        run: |
          git config user.name github-actions[bot]
          git config user.email 41898282+github-actions[bot]@users.noreply.github.com
      - uses: actions/setup-python@v5
        with:
          python-version: 3.x
      - run: echo "cache_id=$(date --utc '+%V')" >> $GITHUB_ENV 
      - uses: actions/cache@v4
        with:
          key: mkdocs-material-${{ env.cache_id }}
          path: .cache
          restore-keys: |
            mkdocs-material-
      - run: pip install mkdocs-material 
      - run: mkdocs gh-deploy --force
```

复制完了之后，你的本地文件结构和内容应该长这样：

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202410121034087.png)

然后，按照三中类似步骤，把我们的上述更新推送到仓库中。具体的指令就不赘述了。

这时其实还是没有托管成功的。推送完毕后，你需要前往你的仓库的 `Settings` 部分，选择左侧栏中的 `Pages`，修改构建的分支为 `gh-pages`。也就是改成下面的样子。

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202410121052492.png)


现在，再在本地随便改些东西，比如我在 `index.md` 里加一些新的文字。**再重新提交代码**，推送到仓库里。

此时访问你的仓库，会发现右下角有个 `Deployments`，里面显示你的 github-pages 在排队，等待服务器部署。然后，大概等个一两分钟，就会显示部署结果。是绿色，说明部署好了。

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202410121100960.png)

此时，检验成果的时候到了。点击上图中部署完的那个github-pages，会出现部署详情。注意在部署成功的后面有一个包含 `github.io` 的网页链接。点击那个链接，就可以跳转到你部署的网页。

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202410121103393.png)

点开如图：

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202410121105600.png)

会发现中间有一行我们刚刚添加的新的文字。说明我们刚刚的更新成功了！

大功告成！

**现在，你已经完成了Github Pages 的托管。你在这个仓库的main分支上的所有更新，都会及时同步到上述链接上发不出来。这也是个人网站/个人博客等的最原始、最基本的起点。** 后续会基于这个笔记，继续展开几个内容：

1. 如何给网站赋予一些主题？
2. 如何编排自己的目录？
3. 如何自定义格式？
4. 如何处理和存储网站中的图片？
5.  ... 
6.  

!!! note "END"

