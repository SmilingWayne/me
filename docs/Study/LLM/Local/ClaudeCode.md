# Claude Code 入坑安装指南

这个笔记现在写其实有点子晚了，感觉身边不少小伙伴已经跟 Claude Code 快乐玩耍很久了，我还没怎么~~调教~~使用得明白 Cursor，就又硬着头换过来用。

我是原 VS Code 忠实铁粉，用了两个月 Cursor 后换回 VS Code 老本行。于是我的工作流主要还是基于 VSCode 的开发插件来做。

现在直接进入安装流程。**本教程针对 macOS 用户**。参考了如下内容：

- [智谱的API接入Claude Code教程](https://docs.bigmodel.cn/cn/coding-plan/tool/claude) 和 [插件教程](https://docs.bigmodel.cn/cn/coding-plan/tool/claude-for-ide);
- [阿里百炼的API接入Claude Code](https://help.aliyun.com/zh/model-studio/claude-code-coding-plan?spm=a2c4g.11186623.help-menu-2400256.d_0_2_2_2.47324c4dIjZQM1&scm=20140722.H_3023078._.OR_help-T_cn~zh-V_1)；

当然你看过之后就知道这都大差不差，门槛极低。

## 流程

### node.js

首先安装 [node.js](https://nodejs.org/en/download/)，直接下载或者命令行安装（我更喜欢这个）。

他的官网命令需要你在terminal中按顺序执行如下四五个步骤，如果正常就OK。

```shell
# Download and install nvm:
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.4/install.sh | bash
# in lieu of restarting the shell
\. "$HOME/.nvm/nvm.sh"
# Download and install Node.js:
nvm install 24
# Verify the Node.js version:
node -v # Should print "v24.14.0".
# Verify npm version:
npm -v # Should print "11.9.0".
```

!!! question "什么是 node.js, nvm, npm，如果我以前装过一个旧版的npm怎么办？"
    - node.js: Node.js 不是一门编程语言，是一个基于 Chrome V8 引擎的 ==JavaScript 运行时环境==。JavaScript 原本只能在浏览器里 “干活”（比如操作网页 DOM、响应用户点击），Node.js 相当于给这个厨师搭了一个 “全能工作室”，让 JavaScript 可以脱离浏览器，在电脑的操作系统（Windows/Mac/Linux）上直接运行。
    
    - npm (Node Package Manager)：==是 Node.js 的包管理器==（解决 “安装 / 管理第三方代码包” 的问题），
    - nvm (Node Version Manager)：==是管理 Node.js 版本的工具==（解决 “不同项目需要不同 Node 版本” 的问题）；

    按上述命令安装后你应该同时有了 node.js, nvm, npm 这三个家伙。

    如果你以前有一个旧的 npm 管理器（比如我），你的新版本的 npm 会与他共存，比如你可以终端执行：
    
    ```bash
    nvm list
    ```
    
    如果有老的就会显示：

    ```text
           v16.20.2
    ->     v24.13.1
            system
    default -> v16.20.2

    ```

    有一种可能，如上面这个输出显示的（which is exactly 我遇到的），系统的在执行终端命令时默认打开着老的 npm 管理器。

    此时在终端里执行：

    ```shell
    nvm alias default v24.13.1
    ```

    这里的 `v24.13.1`，改成你安装的那个新的npm 版本（也就是 `nvm list` 列出来的那串字符即可。

    > 因为你直接操作的话，后面claude会装在新的你刚下的npm里，如果过两天你重新开终端，打开的是老npm，你运行`claude` 就会出现奇怪问题。

### claude code

现在可以装 Claude Code 了。在终端里运行：

```shell
npm install -g @anthropic-ai/claude-code
```

然后运行：

```shell
claude --version
```

如果输出类似的版本号:

```text
2.1.49 (Claude Code)
```

那就大功告成！

### API 

我们首先把“在终端跑通自己的API”这事给弄好。

为了快乐自由地在 Claude Code里用其他各种模型，你需要一个API。这个API可以是很多供应商的，DeepSeek, 智谱、Qwen，这里我们以 Qwen3.5 plus 为例进行展示。

你可以在[这里](https://help.aliyun.com/zh/model-studio/coding-plan?spm=a2c4g.11186623.help-menu-2400256.d_0_2_0.65ef6fd1nx52zE&scm=20140722.H_3005961._.OR_help-T_cn~zh-V_1) 获取API并一步步按照说明书地走到底。小白可以买一个Lite 版本试着玩玩，第一个月 7.9 元 （2026-03-02）。

一些备选方案比如 DeepSeek API（这玩意不行就不行在 128 K Context ，需要谨慎管理上下文长度，总感觉活还没干呢就已经被榨干了（误），过短上下文对于 Agent 确实有些不友好。感兴趣可以参考[deepseek API usage](https://platform.deepseek.com/usage)。

这一部分不同API供应商都有自己的讲解，这里略过。

这一部分完成的标志，是你在自己的终端里随便打开一个文件夹 `cd ~/Desktop/xxxx`，然后运行：

```shell
claude
```

会出现这个经典的界面，并且这个界面显示了你自己的那个API服务的模型：

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202603021533578.png)

那么这一步你也搞定了！

!!! question ""
    这一part有一些不熟悉的伙伴可能遇到需要在终端里向 `~/.bashrc` （或者 `~/.zshrc` ）写入文本的问题，一些教程会让你在终端用 vim 改来改去，然后怎么改都不舒服。实际上你可以直接在VScode里编辑（省得不会用 vim），编辑好了保存。

    保存好后记得要在终端里运行：
    
    ```
    source ~/.bashrc
    ```
    
    不然不会激活你的修改。

---

### 接入到 VS code 插件中

不少人被劝退主要还是因为终端操作太反人类了（我只坚持了一天就败下阵来），于是这里搬出 Claude Code for VS Code：

在 VS Code 插件市场搜索 Claude Code for VS code:

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202603021536481.png)

安装后点击插件的小齿轮进入设置，找到这个环境变量，去settings.json中设置他：

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202603021538792.png)


在打开的文本里粘贴：

```
"claudeCode.environmentVariables": [
    {
      "name": "ANTHROPIC_BASE_URL",
      "value": "YOUR_BASE_URL"
    },
    {
      "name": "ANTHROPIC_API_KEY",
      "value": "YOUR_API_KEY"
    },
    {
      "name": "ANTHROPIC_MODEL",
      "value": "YOUR_MODEL_NAME"
    },
    {
      "name": "ANTHROPIC_DEFAULT_SONNET_MODEL",
      "value": "YOUR_MODEL_NAME",
    },
    {
      "name": "ANTHROPIC_DEFAULT_HAIKU_MODEL",
      "value": "YOUR_MODEL_NAME",
    },
    {
      "name": "ANTHROPIC_DEFAULT_OPUS_MODEL",
      "value": "YOUR_MODEL_NAME",
    },
    {
      "name": "ANTHROPIC_DEFAULT_SUBAGENT_MODEL",
      "value": "YOUR_MODEL_NAME",
    }
  ],
```

实测你只写自己的模型好像总有问题，得把 “ANTHROPIC_DEFAULT_SONNET_MODEL” 这几个也写上当 placeholder占位，这个模型名可以用你 API 的模型，比如你是 Qwen 的就可以是 `qwen3.5-plus`，如果是 deepseek 就可以是 `deepseek-chat` 以此类推。

最后把插件这个 “selected model”部分的名字改成你自己的，比如 qwen3.5-plus

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202603021544858.png)


这里成功的标志是，你在VS Code中打开 Claude Code 插件对话框，输入：

```
/model
```

然后会让你选择模型，你可以看到除了 Claude 的几个模型外，出现了你自己的模型：

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202603021553643.png)

Voila！大功告成，你现在不止可以在终端里用 VS Code （谁还记得这才是它的本意），还能用 VS Code 插件了！

### FAQ

一个有意思的小问题是，你在终端里运行 Claude Code，能打开，但是你到 Vscode 里整一个终端，却发现没法用 Claude Code（非插件），这是豆包的分析，which 最终解决了我的问题：

**系统终端能用 `claude`，但 VSCode 终端提示 `command not found`**，核心原因是：**VSCode 终端默认以「非登录 shell」启动，没加载你的 zsh 配置（`.zshrc`/`.zprofile`），导致 `PATH` 里缺少 `claude` 所在路径**。


- 方案1：让 VSCode 终端以「登录 shell」启动（最推荐）

让 VSCode 终端和系统终端一样加载 `.zprofile`/`.zshrc`：
1. 打开 VSCode → 按 `Cmd+,` 打开设置
2. 右上角点击 **打开设置 (JSON)**
3. 添加/修改这行（macOS zsh）：
```json
"terminal.integrated.defaultProfile.osx": "zsh",
"terminal.integrated.profiles.osx": {
  "zsh": {
    "path": "/bin/zsh",
    "args": ["-l", "-i"]
  }
}
```
4. 重启 VSCode 终端 → 再试 `claude`

??? question "这个添加的 macOS zsh 命令啥意思呢？豆包说："
    这段配置的核心是：**强制 VSCode 内置的 zsh 终端以「登录交互式 shell」的方式启动**，这样它就会加载和系统终端完全一样的环境配置（比如 `.zshrc`/`.zprofile`），解决 `claude` 命令找不到的问题。

    ### 逐行拆解含义
    ```json
    "terminal.integrated.profiles.osx": {
    "zsh": {
        "path": "/bin/zsh",
        "args": ["-l", "-i"]
    }
    }
    ```

    `"terminal.integrated.profiles.osx"`
    - 这是 VSCode 的配置项名称，专门用于**定义 macOS 系统下内置终端的「配置文件」**（可以理解为“终端启动规则”）。
    - 简单说：这行是告诉 VSCode“接下来要设置你在 macOS 上启动 zsh 终端的规则”。

    `"zsh": { ... }`
    - 这是针对 `zsh` 这个 shell 的具体配置，意思是“下面的规则只适用于 zsh 终端”（如果你的终端是 bash，就对应写 `"bash": { ... }`）。

    `"path": "/bin/zsh"`
    - 指定 VSCode 启动 zsh 时，要调用的 zsh 程序的**实际路径**。
    - `/bin/zsh` 是 macOS 系统默认的 zsh 安装路径（你可以在终端执行 `which zsh` 验证，输出就是这个路径）。
    - 作用：确保 VSCode 用的是系统正确的 zsh，而不是其他路径的 zsh 版本。

    `"args": ["-l", "-i"]`
    这是最关键的部分，`args` 是“启动参数”，`["-l", "-i"]` 是给 zsh 加的两个核心参数：
    | 参数 | 全称            | 含义                                                                                                                                |
    | ---- | --------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
    | `-l` | `--login`       | 以「登录 shell」模式启动 zsh → 会自动加载 `~/.zprofile`、`~/.zlogin` 等登录配置文件（nvm、claude 的路径通常写在这些文件里）。       |
    | `-i` | `--interactive` | 以「交互式 shell」模式启动 zsh → 会加载 `~/.zshrc`（你自定义的 alias、PATH 等都在这里），并允许你和终端交互（输入命令、执行操作）。 |

    ### 为什么默认 VSCode 终端不行？
    - VSCode 内置终端默认启动 zsh 时，**不加 `-l` 和 `-i` 参数**，属于「非登录非交互式 shell」，只会加载 `~/.zshenv`（极少人会把配置写在这里），不会加载 `.zshrc`/`.zprofile` → 导致 `PATH` 里没有 claude、nvm 的路径，命令就找不到。
    - 加上这两个参数后，VSCode 终端就和你手动打开的系统终端（比如「终端.app」）启动方式完全一致，环境变量、命令路径也就都匹配了。

    
    ### 总结
    1. 这段配置的核心是给 VSCode 的 zsh 终端加了 `-l`（登录）和 `-i`（交互式）参数；
    2. `-l` 让终端加载登录配置，`-i` 让终端加载交互式配置，两者结合补全了环境变量；
    3. 最终效果：VSCode 终端和系统终端的环境完全一致，能找到 `claude` 等依赖配置的命令。