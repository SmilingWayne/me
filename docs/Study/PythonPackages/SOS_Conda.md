# 一个老登踩坑Conda环境的悲惨经历

事情是这样的。

接到上级通知“熟悉摸索”一下Mindopt求解器的过程中，有一个调用求解器的方法是把安装包放到本地，然后用Python调用，这样可以不依赖阿里达摩院提供的在线建模平台进行本地使用。中间有一个步骤是这样的。[网页看这里](https://solver.damo.alibaba.com/doc/html/testing/compile-python.html#python-installation-pip)

**用conda安装mindoptpy的注意事项**
:    安装Python库之前，对于使用 conda 环境的 macOS 用户，需保持 conda 和 macOS 的架构信息相符，可通过判断 `conda info` 输出的 `__archspec` 字段与 `uname -m` 的输出是否一致进行判断。

    我一开始没当回事，在自己电脑上运行，安装mindoptpy也能成功，不过本地跑Python，会报错：
    
    ```text
    from .mindoptpy import *

    ImportError: dlopen(/Users/apple/anaconda3/envs/py39/lib/python3.9/site-packages/mindoptpy/mindoptpy.so, 0x0002): tried: '/Users/apple/mindopt/1.2.1/osx64-aarch/lib/mindoptpy.so' (no such file), 
    ```

接下来这个故事就进入了一个有点魔幻的问题。也就是，本地的conda版本过于落后，以至于只能支持x86_64，但是第三方依赖要求在Apple Silicon上的架构必须是ARM。

比如我这台电脑上的Conda，可以追溯到我2019年用的那一款2017年产的MacBook Air（软件、数据都是直接迁移过来的），conda等一直也没有升级，所以conda info里的参数都十分的老：


```
 active environment : base
    active env location : [XXXX]
            shell level : 2
       user config file : /Users/apple/.condarc
 populated config files : /Users/apple/.condarc
          conda version : 4.6.5
    conda-build version : 3.7.3
         python version : 3.6.5.final.0
       virtual packages : __archspec=x86_64
                          __conda=4.6.5
                          __osx=10.15
            .....
            .....
               platform : osx-x86
```

我的第一想法是，那我把当前的conda环境升级成支持ARM的，不就可以啦！

现在最新的conda已经遥遥领先（真的），毕竟最新的版本是24.1.2，并且根据[链接](https://www.anaconda.com/blog/new-release-anaconda-distribution-now-supporting-m1)的数据，2022年版本的conda就提供了原生ARM架构的M1的支持。而Apple也提供了通过Rosetta（一种转换工具），在ARM指令集架构的Apple Silicon上运行包含x86_64指令的应用程序。（[参考链接](https://developer.apple.com/documentation/virtualization/running_intel_binaries_in_linux_vms_with_rosetta)）。一些关于这种方法的介绍可以参考[这个链接](https://or-levi.medium.com/python-management-on-apple-silicon-arm-x86-with-pyenv-f786cf8a48f8) （🪜may needed）.

而且这个Conda提供的基础Python环境还是Python3.6.5。有一点点老了。所以，毫无疑问，我的第一个想法是赶紧升级我的conda。（强迫症）。

然后噩梦和奇怪的东西就开始出现了。

查询所有的资料，你毫无疑问会在 [这里](https://docs.anaconda.com/free/anaconda/install/update-version/) 找到方案。

```shell 
conda update conda
```

但是，这个命令在我的这版老态龙钟的conda面前，显得如此无力：


然后后面是：

```
The environment is inconsistent, please check the package plan carefully
The following package are causing the inconsistency:
```

具体的情况在 [StackOverflow的这个问题](https://stackoverflow.com/questions/55527354/the-environment-is-inconsistent-please-check-the-package-plan-carefully)下有相关的具体描述。

而且，在罗列了40+个冲突不一致的依赖后，终端依然在运行，后台Memory占用也达到了近70%。我以为这个命令是可以运行结束的。

但是，情况并不是这样。它一直在运行，我也坚持地等了6个小时（13:XX～19:YY），依然没有结束。好像在跑一场永远不会结束的马拉松。这个情况也在[这个链接](https://stackoverflow.com/questions/53348953/anaconda-python-ver5-3-hangs-at-update-forever)里得到了描述。

按照道理，终端此时在处理我这个老而沉的conda环境（其中有Python 3.6.5， Python 3.8.0， Python 3.10.5 等多个不同的Python环境）的冲突、依赖检查等等一些我不知道的东西。

在晚上，我试了多个可能可以绕开这个问题的方法。包括但不限于：


```shell
conda install --rev 0
```

以及：

```shell
conda update --all
```

还有：

```shell
conda update --force conda
```

一开始的运行结果可能会有不同，但是殊途同归，都会在显示完所有的inconsistent dependencied之后，卡住（ > 30 min ）不动。

> 这里吐槽一下conda的命令行使用。我根本不知道后台在执行什么命令，也没有运行进程的展示，我看到的只有一个 "\ / \ / " 在不停滴变换。
>

同样地，我们还能找到一些其他的可能解决这个问题的解决方案。比如借助一些更加高效的conda的管理包，来加速这个过程。比如：[libmamba工具](https://www.anaconda.com/blog/a-faster-conda-for-a-growing-community) （嗯，反正都是各种🐍的名字）、比如[miniconda](https://docs.conda.io/en/latest/miniconda.html)。这些工具都可以采取一些优化的方法（并行balaba），来加速依赖的安装、加速冲突依赖的检查等。

比如你可能会看到诸如：

```shell
mamba upgrade conda
```

但是，这些包想要顺利地安装到我的conda里，我首先需要做一个任务：

升级我的conda 到一个更加新的版本。

也就是说，我陷入了一个：“想要加快conda升级 ---> 需要用一些新工具 ---> 需要先升级一下conda” 的死循环中。

也就是那个恐怖的马拉松命令：

```shell
conda update conda
```

我有些累了。

忘记补充，在所有的所有的最开始，一些常见的解决 conda 安装速度过慢的方法，比如架好梯子、更换conda安装源等（请自行搜索）都已经尝试过，但是都没有效果。

> 这里有个小Tip，一些“换源”，是针对PIP的，在conda上是无用的。

!!! tip "另一些小TIP"
    macOS下，一些特定软件会有其对应的配置文件（平时是隐藏的，需要 ++shift++ + ++command++ + ++.++ 来显示），它们的命名是有规律的。一般是在默认的根目录 `~/` 下，`.{你的软件名}rc`

    比如你想要配置 `bash` 的，配置文件所在路径 `~/.bashrc`  ；

    比如最开始说的 `mindopt` 的，配置文件所在路径 `~/.mindoptrc` ；

    比如配置 `conda` 的环境变量，配置文件所在路径： `~/.condarc` ；

    以此类推。

于是，做了一个违背祖宗的决定：

重装一个conda！直接洗牌！

!!! warning "在此之前，建议对 `/Users/{你的用户名}/anaconda3/envs` 下的环境做一个简单的备份。 "

哇，效果拔群。直接删除 `~/anaconda3` 文件夹，按照[官网](https://docs.anaconda.com/free/anaconda/install/mac-os/)的方案，下载 Apple Silicon对应的版本，一路Agree就可以了。等待的时间在5min内。

这是安装好后的base环境的 `conda info`


```txt
active environment : base
    active env location : /Users/apple/anaconda3/envs/py310_arm
            shell level : 2
       user config file : /Users/apple/.condarc
 populated config files : /Users/apple/.condarc
          conda version : 24.1.2
    conda-build version : 24.1.2
         python version : 3.11.7.final.0
                 solver : libmamba (default)
       virtual packages : __archspec=1=m2
                          __conda=24.1.2=0
                          __osx=13.5=0
                          __unix=0=0
       base environment : /Users/apple/anaconda3  (writable)
      conda av data dir : /Users/apple/anaconda3/etc/conda
  conda av metadata url : None
           channel URLs : https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/osx-arm64
                          https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/noarch
                          https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r/osx-arm64
                          https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r/noarch
                          https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2/osx-arm64
                          https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2/noarch
          package cache : /Users/apple/anaconda3/pkgs
                          /Users/apple/.conda/pkgs
       envs directories : /Users/apple/anaconda3/envs
                          /Users/apple/.conda/envs
               platform : osx-arm64
             user-agent : conda/24.1.2 requests/2.31.0 CPython/3.11.7 Darwin/22.6.0 OSX/13.5 solver/libmamba conda-libmamba-solver/24.1.0 libmambapy/1.5.6 aau/0.4.3 c/0Obw83PXeM3UtHlkLD_amg s/-16NoNRKZrgfgkz_p3tJcg e/f5CO1Nv4Lhz7LpIazgf6cQ
                UID:GID : 501:20
             netrc file : /Users/apple/.netrc
           offline mode : False
```

可以看到环境一下干净了很多，版本也升级了。缺陷是你需要重新创建一些新的Python环境。

和之前的版本不同的是，platform变成了 ` platform : osx-arm64`，`__archspec=1=m2`，系统也变成了 `__osx=13.5=0`。

在同样的环境下，本地 Python调用和运行mindoptpy也顺利多了。


最后的最后，如果我们想要对自己的依赖进行更加精细的管理，<u>比如我既想要有一个兼容性更好的Python 3.10（也就是基于x86_64的），又想要有一个能够充分利用ARM性能的Python 3.10环境*也就是基于 ARM64的），那么该怎么操作呢？</u>

你可能需要下面的命令：

```shell
CONDA_SUBDIR=osx-arm64 conda create -n py310_arm python=3.10
```

这里的含义是，基于 `osx-arm64` 架构创建了一个叫做 `py310_arm` 的Python 3.10（默认是最新版本：3.10.14）环境。

而如果你想要 `x86_64` 的， 你需要下面的命令：

```shell
CONDA_SUBDIR=osx-64 conda create py310_x64 python=3.10
```

这里的含义是，基于 `osx-64` 架构创建了一个叫做 `py310_x64` 的Python 3.10（默认是最新版本：3.10.14）环境。

------

!!! quote "我只有一个感触：重装确实能解决问题。如果没有，那就多重装几个。"