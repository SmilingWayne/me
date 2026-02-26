# 纸笔逻辑谜题网络资源整理

整理一些纸笔逻辑谜题的网络资源。涉及：谜题规则文档、谜题制作分享、谜题求解、社区等多个部分。

首先明确一下本文讨论的对象：（纸笔）逻辑谜题（Logic Puzzles），参考puzzles.wiki 上的定义：

> Logic puzzles are puzzles that revolve around linear thinking and logical deduction. Logic puzzle are fairly common in puzzle hunts, ..., (they) in general require an aspect of mathematical or logical thinking to solve, and often involve a specific path of deductions to be made and followed in order to reach the singular solution at the end.

即一类围绕线性思维、数学或者逻辑推导进行求解的谜题，通常包括一类特定的推理路径来得到最终的唯一解的谜题。它和另一种常见的解谜寻宝 （Puzzle Hunt） 是有所不同的，虽然这类逻辑谜题经常构成解谜寻宝活动的一些子谜题。这里的解谜寻宝（Puzzle Hunt）是指：

> A puzzle hunt, also commonly referred to as a puzzlehunt or hunt for short, is an event where teams or individuals compete to solve a series of puzzles. Puzzle hunts differ from other puzzle collections or competitive puzzles in that each puzzle yields a word or phrase which can often be verified against some answer checking mechanism, and rounds or hunts culminate in metapuzzles that combine these individual answers together in novel ways and which provides an overall conclusion to the narrative of the event (often the location of a hidden object, or the resolution to an initially posited question).

Puzzle Hunt 是团队或个人竞技破解一系列谜题的活动，也是区别于普通谜题集的特色解谜形式： 由多道谜题组成。每道谜题的答案为一个单词或短语，可通过校验机制验证；赛事/轮次最终会有元谜题(meta puzzles)，整合所有单题答案，完成赛事剧情收尾（如找到隐藏物品、解答开篇问题）。

本文讲述的逻辑谜题，是构成 Puzzle Hunt 子谜题的逻辑谜题（Logic Puzzles），而不是解谜寻宝活动。

## 谜题规则、制作、分享

1. **[puzzles.wiki](https://www.puzzles.wiki/wiki/Logic_puzzle)**，谜题维基百科，本文的很多内容就是从这儿抄的。类似 wikipedia 的网页，纯文本，无需魔法。

2. **[nikoli](https://www.nikoli.co.jp)** 公司官网，Nikoli 是一家专注于逻辑谜题的日本出版商，对**数独**（Sudoku）游戏的推广宣传起到了重要作用，并且开发设计了许多很有趣的谜题，比如数回 Slitherlink。

3. **[puzz.link](https://puzz.link/) 及其拓展** （无需魔法），puzz.link 本身是一个在线分享与解谜的工具，其中：

   - [puzz.link/p](https://puzz.link/) 负责谜题制作、分享、在线求解、逻辑验证；
   - [puzz.link/db](https://puzz.link/db) 提供了一些定期更新的爬虫，会获取一些其他玩家制作的 puzz.link 格式的谜题链接。
   - [puzz.link/list.html](https://puzz.link/list.html)：提供了一些简单的逻辑谜题分类、规则介绍；
   - [pzplus](https://pzplus.tck.mn/list.html)： puzz.link 的拓展，包含了更多的谜题，把数据库爬到的链接直接展示在了网页端，不需要费劲跳转到源网页了。支持展示谜题难度、通过人数等（需要注册）
   - [pzv.jp](http://pzv.jp/)：另一个 puzz.link 的拓展，包含了更多的谜题、更详细的谜题分类。

4. **[penpa-edit](https://swaroopg92.github.io/penpa-edit/)** 站点 （源站点部署 github，访问可能不稳定）

penpa-edit 功能上和 puzz.link 有重叠，都是用于创建、分享、求解逻辑谜题的网页工具，它支持从 puzz.link 的谜题链接解析谜题数据。除此之外，**支持更多的形状、符号标记。**

5. [SudokuPad](https://sudokupad.app)，一个用于**数独**及其变体的制作与求解工具，不同于前述链接，提供了手机/平板/PC端使用的软件，你甚至可以在 Steam 上玩。

6. [Puzzle Square JP](https://puzsq.logicpuzzle.app/)，无需魔法，日本谜题爱好者搞的网站，可以看到题目难度等。同样是基于 puzz.link 和 penpa-edit 进行谜题分享（所以熟悉这两个站点真是很有用 plus！）


## 谜题求解

- [nikoli puzzle solver](https://util.in:8102/) by Kevinychen，在[Github](https://github.com/kevinychen/nikoli-puzzle-solver)开源，一个基于 penpa-edit UI 的在线谜题求解工具，目前支持 130+ 种不同谜题，同时提供了对非正方形网格，比如六边形、三角形的支持。基于 z3 solver + Web Assembly。

- [Noqx](https://t0nyx1ang.github.io/noqx/penpa-edit/) by t0nyx1ang，同样 Github 开源，基于 penpa-edit UI 的谜题求解工具，支持更多的谜题（160+），Noqx 本身利用答案集（Answer Set Solving）求解工具 + Web Assembly 进行实现，对于连通类谜题，实测求解效率高于纯 SMT 求解器。这个仓库本身基于 [Noq](https://www.noq.solutions/) 开发而来，Noq 不支持 penpa-edit UI，因此用起来稍稍麻烦一些。

- [pzprrt by semiexp](https://semiexp.net/pzprrt/index.html)，日本谜题爱好者写的网站，提供了大多数 puzz.link 谜题的求解，他们最新的求解后端是 [cspuz-solver2](https://semiexp.net/apps/cspuz-solver2/index.html)，增加了对 penpa-edit 链接导入谜题并求解 -> 可视化，验证唯一解等。网站同样提供了一些数独的推导求解工具。

- [pzprevert](https://reverm.github.io/pzprevert/list.html)：一个基于 puzz.link 构建的谜题求解网站，增加了求解用的 UI，支持大部分 puzz.link 谜题，是基于初代的 pzprrt 魔改而来。
