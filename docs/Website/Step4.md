# 一些废话

如果你想直接快速复现这个仓库，而你又有一丁点（真的只需要一丁点！）编程基础，就会发现你需要：

1. Python环境 （python 3.10）
2. Git。

就ok了！

但是如果直接贸然安装本网站的 requirements.txt 会发现有个statistics 的插件没有安装。这是因为每次部署时候我会用一版自己魔改的插件进行替换。

也就是你需要在你刚刚的Python环境下，**先后**执行下面三行脚本：


```bash
git clone https://github.com/SmilingWayne/mkdocs-statistics-plugin
pip install ./mkdocs-statistics-plugin
rm -rf mkdocs-statistics-plugin
```

这样就可以手动安装上魔改后的一个插件了。

具体的Github Workflow 可以参考本仓库的 `.github` 文件夹下的脚本。

已标记为待整理。