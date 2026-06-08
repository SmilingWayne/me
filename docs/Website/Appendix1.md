# 后续｜技术上的打算

目前 [mkdocs](https://www.mkdocs.org/) 因为种种原因暂时停止了维护，基于它所做的 mkdocs-materials 也相应地停止开发新功能了转入维护阶段，后续本站点会经过缓慢陆续调整，完成一次框架优化。但是在最终敲定方案、保证流畅迁移之前，目前的界面、流程、UI等均不会变化。

!!! quote ""
    为啥mkdocs停止更新了，以及停止更新到现在发生了什么，我其实很久没关注，简单了解下感觉算是个既难绷又难以避免的事，已经有一些很详细的综述了，参考 jaywhj 的[《MkDocs 的恩怨情仇史》](https://jaywhj.netlify.app/mkdocs-history)。

目前暂定的后续更新方案是使用 [Zensical](https://zensical.org/docs/get-started/)，由 mkdocs-materials 原班团队打造的静态网站构建框架与基础设施，但是毕竟是刚刚开始的项目，许多功能尚未提供完备的支持：

1. `git-info`，这部分是我偏爱的，因为本网站制作的一个相对严肃的初衷就是“为我自己找到一种记录、描绘、刻画、记忆时间的方式”，尤其是这一整套详细的 .git 信息，文本是怎么被修改的，我在什么时候做了什么，又在想什么；目前 [Zensical 的方案](https://zensical.org/compatibility/plugins/) 是提供一个成熟的 public API 这样不仅方便使用，还方便后续开发：**但是目前官方还没有支持**；
2. 文本字数统计，也就是你现在能看到的字数统计部分，后续会（在AI的帮助下）补充一个我自己写的能够在 Zensical 使用的插件（想知道怎么做的可以参考下 NoughtQ 的这个 [repo](https://github.com/NoughtQ/zensical-statistics-plugin)。
4. 阅读量统计，这部分接 API 即可；
5. 接入 AI Agent 尝试：前段时间忙于别的事，这个暂时搁置了，后续会先推全一下 tag 功能，这部分会引入一些 Agent 来做；
6. i18n：暂时未考虑支持；
7. 论坛：暂时未考虑支持；

上述会按照困难度、我的时间、我的心情等诸多因素更新。在最终确定方案前仓库会锁定为目前这套已跑通的老流程继续维护。