# 纸笔逻辑谜题网络资源整理

带图片版见[知乎](https://zhuanlan.zhihu.com/p/2006473284301108420)。参考了[大佬22年的文章](https://www.bilibili.com/read/cv15380655/?opus_fallback=1)，因此存在一些重复内容。

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
7. [cn.gridpuzzle](https://cn.gridpuzzle.com/) 无需魔法， 类似sudokupad，依然是侧重数独，特色是支持多规则嵌套，也支持若干种其他谜题，比如shakashaka， Tile Paint之类。中文友好。
8. [Puzzle Square JP](https://puzsq.logicpuzzle.app/?)，最好开魔法访问，日本谜题爱好者搞的网站，网页语言可选日语英语（善用翻译插件），包含了很多题目，看索引有十几万条，几百种谜题（包含变体），可以看到题目难度等。几乎完全基于 puzz.link 和 penpa-edit 进行谜题分享，所以熟悉这两个站点真是很有用的呢！
9. [GMpuzzles](https://www.gmpuzzles.com/blog/about-grandmaster-puzzles/): 无需魔法，一个由 Thomas Snyder 创办的益智博客（三届世界数独冠军），包括了多位高产优质的谜题创作者孜孜不倦的更新（Serkan Yürekli, Thomas Snyder etc.），因此能够提供一些最优秀的逻辑谜题。**很好地弥补了penpa-edit网页找不到题来玩的尴尬**。这里的题质量挺高的，几乎全是人工出的题，还会记录一些世界锦标赛上出现的高质量题，有一些数独的谜题，是通过SudokuPad而不是penpa分享的。
10. [Janko.at](https://www.janko.at/Raetsel/index.htm)，无需魔法，推荐过几次了，我的入门款，目前仅支持德语、英语，部分支持日语（善用浏览器插件！），很古老但有生命力的站点，无广告，支持几百种谜题，每种各有几十到几百道题，自带正确性检查。
11. [Krazydad](https://krazydad.com/?mode=interactive)，（？疯狂老爸）免费可打印和互动的数独、迷宫和逻辑谜题，无需魔法。无意中在YTB刷到的，作者原来在迪士尼工作，做谜题生成之类的副业有二十几年了，也做了一些谜题生成的工作，据他说有几百万道题，我没有研究很深入。很有爱的小网站，可以看看作者的介绍[17]。依然是数独为主，辅之以其他谜题。
12. [Logic-masters.de](https://logic-masters.de/Raetselportal/) 无需魔法，谜题爱好者最爱之一，主打数独、Sudoku变体（迷雾、德国耳语线etc），不少的做题链接会跳转到 SudokuPad，一个小小不方便是许多正文没有英文翻译（善用翻译工具+1）。我其实挺佩服上面一些出题人的，脑洞很大，但是对新手可能不太友好。发烧友必备。
13. [puzzle-xx](https://www.puzzle-nonograms.com/?size=2) ：一个无法形容的网站，把 xx 替换成谜题名字就能访问了，比如 puzzle-nonograms。谜题种类不算特别多（相比前面动辄几百种的而言），但应该是机器生成谜题，所以题量都很大，缺点就是题目质量有高有低，很多题就是一眼秒，正因此挺适合新手入门的，还有每日/每周/每月挑战，喜欢超大盘面的有福了：这里的数织每月谜题是 50x50 规模的。
14. [Simon Tatham's Portable Puzzle Collection](https://www.chiark.greenend.org.uk/~sgtatham/puzzles/)，同样是一个颇具历史且经典的谜题收集库，简约无广，可以直接随机做题玩耍，支持自定义盘面规模，也是很适合入门摸鱼的一个小站点。
15. [cross-plus-a](https://www.cross-plus-a.com) ，俄罗斯人开发的工具，应用用于解答填字游戏、基于单词的谜题、数独、Kakuro 以及许多其他逻辑谜题。Cross+A 还提供了灵活且强大的搜索工具。按照网站说法它的功能性是很强的，不仅涵盖了填字游戏的一些辅助工具，还能覆盖数百种谜题的自动生成、求解、批量生成、批量求解，不过考虑到它是一整个软件包，体验版功能十分有限，只支持：View words with 6 letters length; solve and create the classic Sudoku (4 × 4 ... 16 × 16); solve and create Killer Sudoku (4 × 4 ... 12 × 12); solve Nonogram, Kakuro and Hitori. 完全版 25 欧，对于不想折腾破费的小伙伴有门槛。我经常用它来当百科全书。


## 谜题求解

- [nikoli puzzle solver](https://util.in:8102/) by Kevinychen，在[Github](https://github.com/kevinychen/nikoli-puzzle-solver)开源，一个基于 penpa-edit UI 的在线谜题求解工具，目前支持 130+ 种不同谜题，同时提供了对非正方形网格，比如六边形、三角形的支持。基于 z3 solver + Web Assembly。

- [Noqx](https://t0nyx1ang.github.io/noqx/penpa-edit/) by t0nyx1ang，同样 Github 开源，基于 penpa-edit UI 的谜题求解工具，支持更多的谜题（160+），Noqx 本身利用答案集（Answer Set Solving）求解工具 + Web Assembly 进行实现，对于连通类谜题，实测求解效率高于纯 SMT 求解器。这个仓库本身基于 [Noq](https://www.noq.solutions/) 开发而来，Noq 不支持 penpa-edit UI，因此用起来稍稍麻烦一些。

- [pzprrt by semiexp](https://semiexp.net/pzprrt/index.html)，日本谜题爱好者写的网站，提供了大多数 puzz.link 谜题的求解，他们最新的求解后端是 [cspuz-solver2](https://semiexp.net/apps/cspuz-solver2/index.html)，增加了对 penpa-edit 链接导入谜题并求解 -> 可视化，验证唯一解等。网站同样提供了一些数独的推导求解工具。

- [pzprevert](https://reverm.github.io/pzprevert/list.html)：一个基于 puzz.link 构建的谜题求解网站，增加了求解用的 UI，支持大部分 puzz.link 谜题，是基于初代的 pzprrt 魔改而来。

- [Puzzlink-Assistance](https://github.com/LeavingLeaves/Puzzlink_Assistance) 一个浏览器插件，油猴脚本一键安装。能给 puzz.link 支持的谜题提供一些基础的分步推断。美中不足是没有推断名称，只展示结果，但这确实是目前为数不多在网页端从Step by Step的角度推断解题而不只是单纯求解角度做的工作了。

## 解谜寻宝

简单存放一些Puzzle Hunt 相关的入门链接，可惜我对这个还不熟悉，搬运一些我觉得受益匪浅的链接。有经验的伙伴可以补充一些。

- 逐年度的 [MIT Puzzle Hunts](https://puzzles.mit.edu/huntsbyyear.html) 谜题列表：

- 国内也有一些有趣的活动，比如北大的 [P&KU PuzzleHunt](https://info.pkupuzzle.art);

- [Puzzmon](https://puzzmon.world/puzzles) 类似 Puzzle Hunt的网站，我自己还没怎弄明白。

## 其他有趣的逻辑谜题

- Pentominoes of [isomerdesign](https://isomerdesign.com/Pentomino/) . 众所周知 Pentomino 作为一种五连骨牌，有很多类似七巧板拼图的玩法，这里就搜集了一些有趣的图案，以及在识别、生成图案时候一些很有趣的技巧、变换。

- [Polyforms](https://puzzler.sourceforge.net/index.html) Polyform Puzzler 是一套适用于多种多形谜题（如五圆骨牌）的求解器，同时也是用于探索和解决多形谜题的软件工具包。它由一套针对特定多形谜题的前端应用程序和一个承担繁重工作的Python库组成。新的多形体和谜题可以轻松定义和添加。
  - 挺喜欢他这个风格的，简约的可视化，在不同坐标下的精确覆盖问题构成的好看的图案（Square, hex, Sticks, Cubes, Polyiamonds, Strings etc)。有些遗憾的是代码实现有些年代了。

???+ quote "Full Reference"
    - 谜题在线做题网站 by 嘉和逆天 https://www.bilibili.com/read/cv15380655/?opus_fallback=1
    - Puzzles.wiki https://www.puzzles.wiki/wiki/Logic_puzzle
    - Nikoli.co.jp https://www.nikoli.co.jp/
    - 机核的这个文章 https://www.gcores.com/articles/122224
    - puzz.link https://puzz.link/
    - pzprjs https://github.com/robx/pzprjs
    - puzz.link Puzzle List https://puzz.link/list.html
    - pzv.jp http://pzv.jp/
    - Penpa edit official https://swaroopg92.github.io/penpa-edit/
    - Sudoku Pad https://sudokupad.app/
    - Sudokupad-penpa-importer https://marktekfan.github.io/sudokupad-penpa-import/
    - cn.gridpuzzle.com https://cn.gridpuzzle.com
    - Puzzle Square JP https://puzsq.logicpuzzle.app/
    - GM Puzzles  https://www.gmpuzzles.com/blog/about-grandmaster-puzzles/
    - Janko.at https://www.janko.at/Raetsel/index.htm
    - Krazydad's Puzzles https://krazydad.com/?mode=interactive
    - Intro of Krazydad https://www.youtube.com/watch?v=qb4gT9z_Ryo
    - Logic-masters.de https://logic-masters.de/Raetselportal/
    - puzzle-nonogram etc. https://www.puzzle-nonograms.com/?size=2
    - Simon Tatham's Puzzle Collection  https://www.chiark.greenend.org.uk/~sgtatham/puzzles/
    - Cross-Plus-A https://www.cross-plus-a.com
    - Nikoli Puzzle Solver https://util.in:8102/
    - Noqx solver https://t0nyx1ang.github.io/noqx/penpa-edit/
    - Noq https://www.noq.solutions/
    - pzprrt by semiexp https://semiexp.net/pzprrt/index.html
    - pzprevert https://reverm.github.io/pzprevert/list.html
    - Puzzlink Assistance https://github.com/LeavingLeaves/Puzzlink_Assistance
