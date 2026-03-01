# 我的 Git 使用cheat sheet

!!! note "开发流程"
    改，发pr，检视，合入main。


## 一些使用经验和Tips

!!! note "issue相关"
    提issue，记录开发的新功能等，如果是第12个issue，用 `#12` 可以直接超链接到对应的issue上。

!!! note "pr相关"
    如果是某个merge请求，可通过 `!` + 序号的方式超链接到对应的merge上。比如 `!12`，对应的就是第12个。

!!! note "一些简单的流程"
    有新的需求，要开发新的代码，先提issue。然后拉一个新分支，名称就是issue的序号，根据功能不同设置不同前缀。比如：
     
    > `feature-12` ： 对应第12个issue，开发了一个新的功能；

    > `bugfix-13`： 对应第13个issue，修复某个bug；

    在分支开发完毕之后，提PR （Pull Request），Code Review之后，合并。

    不要一直挂着PR。

!!! note "Git 当前分支落后主干分支的解决办法"
    当前的开发分支：feat-one，主线分支：main


    1.  切换到主线分支main：

    ```shell
    git checkout main
    ```

    2.  拉取远程主线分支main到本地的主线分支main ：

    ```shell
    git pull --rebase
    ```

    3.  切回到当前的开发分支feat-one：

    ```shell
    git checkout feat-one
    ```

    4.  拉取远程分支main 的代码：

    ```shell
    git rebase main
    ```

    5.  将当前开发分支分支feat-one提交到远程分支feat-one：

    ```shell
    git push origin feat-one -f
    ```


!!! note "把main分支同步到自己的分支"

    1. 创建自己分支：

    ```shell
    git checkout -b my-branch
    ```

    2. 提交到自己分支

    ```shell
    git add .
    git commit -m "Commit message"
    ```

    3. 一段时间后发现要合并主分支的修改

    ```shell
    git checkout main
    git pull origin main
    ```

    （切换到main分支，然后把main分支pull下来）

    4. 切换到自己的分支进行合并操作

    ```shell
    git checkout my-branch
    git merge master
    ```

    5. 如果有冲突，git status 查看冲突的文件

    ```shell
    git add conflict-file.txt
    git commit -m "Merge changes from master into my-branch"
    ```



!!! note "仓库里的Git文件过大如何解决"

    git的宗旨是记录下你对这个文件夹的所有操作记录，所以如果不小心把一些很大的pdf或者其他中间文件也放上去的话，git中的object会很大。这不仅要求我们注意仓库的文件大小，也说明必须好好搞gitignore 文件！！

    而如果这个情况已经发生了，该怎么减小这个git文件？这就是这里需要解决的事情。准确说你需要一个叫 BFG的清理软件：[跳转链接](https://github.com/rtyley/bfg-repo-cleaner/)。并且在进行所有操作之前，最好先“**暂时关闭分支保护**”


    然后，并不是完全按照官网操作就可以解决问题了，需要在一开始做一个小小的修改，其他步骤按照操作指南分别操作即可。

    前置条件是在电脑上要安装Java虚拟机。这一部分可以自行搜索解决。

    按照[操作指南](https://rtyley.github.io/bfg-repo-cleaner/) 第一步进行操作的时候，要输入：

    ```shell
    git clone --mirror git://example.com/some-big-repo.git
    ```

    这一步是没问题的，但是按照上面的介绍到最后git push 到原来仓库的git文件的时候，如果仓库有关闭的pull request，会提示出错：


    ```shell
    To https://github.com/username/repository.git
    ! [remote rejected]     refs/pull/1/head -> refs/pull/1/head (deny updating a hidden ref)
    error: failed to push some refs to 'https://github.com/username/repository.git'
    ```

    并且在取消分支保护 + 强行合并分支的情况下依然无法解决，后来搜索到的原因见[这个链接](https://stackoverflow.com/questions/34265266/remote-rejected-errors-after-mirroring-a-git-repository)，里面很清楚地解答了：

    > The refs beginning 'refs/pull' are synthetic read-only refs created by GitHub - you can't update (and therefore 'clean') them, because they reflect branches that may well actually come from other repositories - ones that submitted pull-requests to you.

    解决方案是把上面第一步`git clone` 语句 替换成：

    ```shell

    git clone --bare git://example.com/some-big-repo.git

    ```

    然后按照BFG的操作手册进行，就完成了！

    以我的这个仓库为例，最开始瘦身Git之前，repo 大小（在github 的 setting -> repository 里可以查看）是 238 MB，清除完毕后是73.9MB。效果十分显著。

    ---------


!!! note "Github API的一些小技巧"

    如果想要了解特定Github开源仓库的信息，可以直接从API 获取。具体使用方法如下：

    按照链接： `https://api.github.com/repos/{这里写你的用户名，不用加括号}/{这里写你的仓库名，不用加括号}` 在浏览器访问即可。

    比如 https://api.github.com/repos/squidfunk/mkdocs-material 这个链接，就可以直接访问mkdocs materials 作者这个仓库的具体信息。包括仓库大小等具体统计数据。


----

### 移动文件的同时保留原文件的git记录

1. 首先，进入git文件夹的目录中：

```shell
cd /path/to/myproject
```

2. 假定当前路径下，文档目录结构：

```text
.
├── VRP
│   ├── CVRP.ipynb
│   ├── VRPPD.ipynb
│   ├── VRPTW.ipynb
│   └── VRPwithPenality.ipynb
├── assets
│   ├── data
│   └── figures
├── TSP.ipynb
└── requirements.txt
```

我想要把 `TSP.ipynb` 文件移动到 `VRP` 文件夹下。

通过命令：

```shell
git mv TSP.ipynb  VRP/
```

即可。此时观察文件路径，已改变为：

```text
.
├── VRP
│   ├── CVRP.ipynb
│   ├── TSP.ipynb
│   ├── VRPPD.ipynb
│   ├── VRPTW.ipynb
│   └── VRPwithPenality.ipynb
├── assets
│   ├── data
│   └── figures
└── requirements.txt
```

确认一下。首先执行：

```shell
git add .
```

然后执行：

```shell
git status
```

此时不出意外会看到关于 `TSP.ipynb` 的修改情况：

```text
On branch basic-dev
Your branch is up to date with 'origin/basic-dev'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        renamed:    TSP.ipynb -> VRP/TSP.ipynb
```

然后正常commit / push ，即可。


### 一些规范

Git 提交规范（特别是 Angular 规范，这是 Conventional Commits 规范的一个流行实现）中的 `feat`、`fix`、`chore` 以及其他。

这些类型是用来标识每次提交（commit）的主要目的，使得提交历史更加清晰、易于理解，并且可以基于这些类型自动生成更新日志（Changelog）或进行语义化版本控制（Semantic Versioning）。



其中 `<type>` 就是我们讨论的这些关键字。

**`feat` (feature)**
:   表示新增了一个功能（feature）。当你为代码库添加了一个新的特性时使用。这些提交通常会在版本更新时导致次版本号（minor version）增加（例如从 1.1.0 到 1.2.0），并且会出现在最终用户的更新日志中。

- `feat: add user login functionality`
- `feat(api): implement endpoint for fetching user profiles`

**`fix` (bug fix)**
:   表示修复了一个 Bug。当你修复了代码中的一个错误时使用。这些提交通常会在版本更新时导致修订号（patch version）增加（例如从 1.1.0 到 1.1.1），并且也会出现在更新日志中。

- `fix: correct calculation error in payment module`
- `fix(ui): resolve issue where button was not clickable on mobile`

**`chore` (chore / miscellaneous)**
:   表示一些杂项的变动，通常是与构建过程、辅助工具、配置或库的更新等相关，这些变动不直接修改源代码的业务逻辑或用户界面。

用于那些不影响生产代码、用户功能或修复 Bug 的提交。例如：修改 `.gitignore` 文件、更新依赖库（且不涉及功能改变）、调整构建脚本等。`chore` 类型的提交通常**不会**出现在最终用户的更新日志中。


- `chore: update dependencies to latest versions`
- `chore(build): adjust webpack configuration for faster builds`
- `chore: add linting rule for variable naming`

**`perf` (performance):**
:   提升性能的代码更改。 `perf: optimize image loading speed by using lazy loading`

**除了 `feat`、`fix`、`chore` 之外，还有许多其他常用的类型，常见的包括：**

* **`docs`** (documentation):
    * **含义**：仅仅修改了文档（例如 README、注释、JSDoc 等）。

* **`style`**:
    * **含义**：代码格式的修改，不影响代码逻辑（例如空格、格式化、缺少分号等）。
* **`refactor`**:
    * **含义**：代码重构，既没有修复 Bug 也没有添加新功能。指那些改进代码结构、可读性或性能，但并未改变其外在行为的修改。
    * **示例**: `refactor: simplify user authentication logic`

* **`test`**:
    * **含义**：添加缺失的测试或修正现有的测试。
* **`build`**:
    * **含义**：影响构建系统或外部依赖关系的更改（例如 gulp、broccoli、npm、webpack 等）。
    * **示例**: `build: switch from webpack to esbuild for faster bundling`
* **`ci`** (continuous integration):
    * **含义**：对 CI 配置文件和脚本的更改（例如 Travis, Circle, BrowserStack, SauceLabs 等）。
    * **示例**: `ci: fix deployment script for staging environment`
* **`revert`**:
    * **含义**：撤销之前的某个提交。通常会自动生成，格式类似 `revert: feat(auth): add SSO login`，并在 body 中说明撤销了哪个 commit hash。


## 开源许可证速览

开源许可证（Open Source License）是法律合同，规定了他人如何使用、修改和分发你的代码。选择合适的许可证对于保护你的权益以及促进社区协作至关重要。

### MIT 许可证 (The MIT License)

“极度宽松，只要你保留我的署名，你想怎么用都行。”

<span style="color:red;font-weight:bold">主要权限</span>
- ✅ **商业使用：** 允许将代码用于商业产品。
- ✅ **修改代码：** 允许任意修改源代码。
- ✅ **分发：** 允许复制和分发代码。
- ✅ **私有化：** 允许将修改后的代码闭源，作为私有软件发布。
- ✅ **合并：** 允许与其他许可证（包括 GPL）的代码合并。

<span style="color:red;font-weight:bold">主要义务</span>
- ⚠️ **保留声明：** 在代码副本中必须包含原始的版权声明和许可证全文。
- ⚠️ **无担保：** 作者不对代码的使用后果承担任何责任。

<span style="color:red;font-weight:bold">优点</span>
- **简单易懂：** 文本很短，法律术语少。
- **兼容性极强：** 几乎可以与任何其它许可证（包括 GPL）兼容。
- **采用率高：** 许多知名项目（如 React, Vue, jQuery, .NET Core）使用此协议，社区接受度高。

<span style="color:red;font-weight:bold">缺点</span>
- **无专利保护：** 没有明确的专利授权条款。如果贡献者拥有代码相关的专利，理论上他们日后可以起诉使用者侵权（虽然实际案例极少）。
- **无传染性：** 别人拿了你的代码去闭源赚钱，你无法强制他们开源改进部分。

<span style="color:red;font-weight:bold">使用场景</span>
- 希望代码被尽可能广泛地使用（包括商业公司）。
- 小型工具库、插件、前端组件。
- 不希望给使用者增加法律负担。

---

### Apache License 2.0

**核心理念：** “宽松使用，保留署名，并且明确授予专利权限，保护大家不被专利诉讼。”

<span style="color:red;font-weight:bold">主要权限</span>
- ✅ **商业使用：** 允许用于商业产品。
- ✅ **修改代码：** 允许任意修改。
- ✅ **分发：** 允许复制和分发。
- ✅ **私有化：** 允许将修改后的代码闭源。
- ✅ **专利授权：** **（核心区别）** 贡献者明确授予使用者专利许可。

<span style="color:red;font-weight:bold">主要义务</span>
- ⚠️ **保留声明：** 必须保留原始版权、专利、商标和归属声明。
- ⚠️ **状态变更说明：** 如果被修改的文件，需要在文件中添加显著的说明（例如“此文件已被修改”）。
- ⚠️ **NOTICE 文件：** 如果原项目包含 `NOTICE` 文件，你必须在你的分发版本中保留其中的归属信息。
- ⚠️ **无担保：** 作者不承担责任。

<span style="color:red;font-weight:bold">优点</span>
- **专利保护：** 明确解决了专利诉讼风险，对大公司更友好。
- **兼容性良好：** 与 GPL v3 兼容（Apache 代码可以合入 GPL v3 项目）。
- **宽松：** 和 MIT 一样，允许闭源商用。

<span style="color:red;font-weight:bold">缺点</span>
- **文本较长：** 法律条款比 MIT 复杂，阅读成本稍高。
- **不兼容 GPL v2：** Apache 2.0 代码不能合入 GPL v2 项目（因为专利条款冲突）。

<span style="color:red;font-weight:bold">适用场景</span>
- 大型开源项目、企业级软件。
- 担心专利纠纷的项目（如 Android, Kubernetes, TensorFlow）。
- 希望平衡宽松性与法律保护的项目。

---

### GPL 许可证 (GNU General Public License)

**核心理念：** “著作权（Copyright）。如果你用了我的代码，你的项目也必须开源，且必须使用相同的许可证。”

<span style="color:red;font-weight:bold">版本区别</span>
- **GPL v2：** 经典版本（Linux 内核使用）。
- **GPL v3：** 增加了专利保护条款，并防止“硬件锁定”（Tivoization）。

<span style="color:red;font-weight:bold">权限</span>
- ✅ **商业使用：** 允许用于商业产品（但必须提供源码）。
- ✅ **修改代码：** 允许任意修改。
- ✅ **分发：** 允许复制和分发。

<span style="color:red;font-weight:bold">义务</span>
- ⚠️ **开源义务：** 如果你分发基于 GPL 代码的软件（包括修改版或链接了 GPL 库），**整个软件必须开源**。
- ⚠️ **许可证继承：** 衍生作品必须也使用 **GPL 协议**（不能改为 MIT 或 Apache）。
- ⚠️ **提供源码：** 必须向接收者提供完整的源代码。
- ⚠️ **专利授权：** (v3 版本明确包含)。

<span style="color:red;font-weight:bold">优点</span>
- **保护自由：** 确保代码及其改进版本永远保持开源，防止被私有化垄断。
- **社区贡献：** 强制使用者回馈社区（通过开源代码）。

<span style="color:red;font-weight:bold">缺点</span>
- **传染性强（病毒式）：** 一旦你的项目依赖了 GPL 库，你的项目通常也必须变成 GPL。这会导致商业公司不敢使用。
- **兼容性差：** 不能与宽松协议（MIT/Apache）的代码简单混合后闭源。
- **法律风险高：** 合规要求严格，容易无意中违规。

<span style="color:red;font-weight:bold">使用场景</span>
- 桌面应用程序、系统工具。
- 希望强制所有改进都回馈给社区的项目（如 Linux, Git, WordPress）。
- 不希望自己的代码被用于专有闭源软件。

---

### 📊 三种协议对比总结表

| 特性             | MIT                 | Apache 2.0                 | GPL (v2/v3)             |
| :--------------- | :------------------ | :------------------------- | :---------------------- |
| **类型**         | 宽松型 (Permissive) | 宽松型 (Permissive)        | 著佐权型 (Copyleft)     |
| **商业闭源使用** | ✅ 允许              | ✅ 允许                     | ❌ 不允许 (分发时需开源) |
| **修改后需开源** | ❌ 不需要            | ❌ 不需要                   | ✅ 必须 (如果分发)       |
| **专利授权**     | ❌ 无明确条款        | ✅ 明确授予                 | ✅ 明确授予 (v3)         |
| **传染性**       | 无                  | 无                         | **强 (病毒式)**         |
| **保留版权声明** | ✅ 必须              | ✅ 必须                     | ✅ 必须                  |
| **兼容性**       | 极高                | 高 (兼容 GPL v3)           | 低 (排斥闭源)           |
| **代表项目**     | React, Vue, jQuery  | Android, Kubernetes, Swift | Linux, Git, WordPress   |

