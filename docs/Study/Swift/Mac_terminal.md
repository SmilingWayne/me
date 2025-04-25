# macOS 终端操作指南


```shell
echo $SHELL
```

查看当前 Shell（命令行解释器）的版本。一般而言是bash或者zsh。用于用户与操作系统交互。


--- 

## 安装 oh-my-zsh 美化你的终端


直接在终端内输入：

```shell
$ sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

安装 Oh-my-zsh.

或者用 gitee 的源：

```shell
sh -c "$(curl -fsSL https://gitee.com/shmhlsy/oh-my-zsh-install.sh/raw/master/install.sh)"
```

以防万一，你可以先check一下你在 原先 bash 下的配置，把 bashrc 里面的内容复制一下。

```shell
cat ~/.bashrc
``` 

然后打开 zshrc：

```shell
nano ~/.zshrc
```

你就可以在终端里编辑了。编辑完后，用：

```shell
source ~/.zshrc 
```

更新你对 zshrc 文件所做的更新。

一般而言你下载好 oh my zsh 会自动让你选择一些样式，按照自己喜欢的选就行了。选好了之后你的终端会稍微带上一点彩色：

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202504260044853.png)

事实上zsh有很多很丰富的主题。你可以通过命令：

```shell
cd ~/.oh-my-zsh/themes && ls
```

进行查看。有的教程（比如我参考的）就会推荐你安装 powerlevel10k 主题。做法是：

执行：

```shell
git clone --depth=1 https://gitee.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k
```

进入 `.zshrc` 文件，将主题名称改为：

```txt
ZSH_THEME="powerlevel10k/powerlevel10k"
```

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202504260049375.png)

然后保存，重新启动一下终端就行。

```shell
source ~/.zshrc 
```

---

你可以安装一些很有意思的插件：

比如自动补全你想要的功能，那么：

```shell
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions

```

**然后，在 `.zshrc` 文件中**，加入这句命令：

```shell
source ~/.zsh/zsh-autosuggestions/zsh-autosuggestions.zsh 
```

然后别忘了source命令保存更改。

这样每次启动zsh的时候都会启用自动补全功能了。注意不要只在终端里执行，否则只有当前有效。



