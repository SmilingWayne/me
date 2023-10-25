# WebUI + Stable Diffusion 在 Apple Silicon下的安装教程


!!! abstract "我的设备"
    - 2022年MacBook Pro，512GB + 16GB，Ventura 13.5， Apple Silicon M2


!!! note "参考链接"
    - [英文版：如何在Apple Silicon上安装webUI](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Installation-on-Apple-Silicon)，理论上说这一份文档就够了，但是你需要一些前置知识，并不是零基础。
    - [中文版｜B站｜本地部署Stable Diffusion](https://www.bilibili.com/video/BV1Pb411X79e/?spm_id_from=333.788&vd_source=1a29610636fa88d6406dc45fc2d153ba)：很可爱的Up主，讲得十分干货十分具体，按照她的来就可，她整理的资源也非常全面；


- 简单说来就是几个步骤：

1. 安装[homebrew](https://brew.sh)；macOS使用者几乎必备的工具
2. 安装[Xcode](https://developer.apple.com/xcode/)；非必需，但是我老早以前就装好了，但凡涉及到需要执行`xcode-select --install` 命令的都是这玩意；本来是专门为Apple公司产品开发的一个工具，但是其内部配置和macOS深度集成，一些零基础的同学不妨用空间换效率，虽然大了一点，但是起码可以省很多事；
3. 从[Github仓库](https://github.com/AUTOMATIC1111/stable-diffusion-webui)克隆，可以看我上面的中文推荐链接；
4. 进入下载下的文件夹，执行。


## 我遇到的特殊的bug


1. Intel版本的Homebrew和ARM版本（对应Apple Silicon）的Homebrew兼容的情况（见上面的中文B站讲解[以及这个链接](https://wuyanxin.com/post/mac-m1-brew-both-support-aarm64-and-x86_64.html#:~:text=alias%20brew_arm%3D%27source%20~%2F.brew_arm%27,alias%20brew_intel%3D%22source%20~%2F.brew_intel%22)）；
2. 在第四步骤执行`./webui.sh` 时候总是报错：

```text
INFO: pip is looking at multiple versions of gfpgan to determine which version is compatible with other requirements. This could take a while.
stderr: ERROR: Ignored the following versions that require a different python version: 1.6.2 Requires-Python >=3.7,<3.10; 1.6.3 Requires-Python >=3.7,<3.10; 1.7.0 Requires-Python >=3.7,<3.10; 1.7.1 Requires-Python >=3.7,<3.10
ERROR: Could not find a version that satisfies the requirement tb-nightly (from gfpgan) (from versions: none)
ERROR: No matching distribution found for tb-nightly
```

> 原因：在pip安装包中搜索不到合适的安装版本，安装失败。原来我的pip用的是清华源，但是清华源可能出了点什么问题，所以更换成阿里源，一下子就可以了。这里的运行时间很长，我是一边洗碗一边等它安装的。
>
> 如何更换到阿里源：在终端输入：

```
pip config set global.index-url https://mirrors.aliyun.com/pypi/simple
```

- 正常安装第四步后，终端应该如下：


```text
Tested on Debian 11 (Bullseye)
################################################################

################################################################
Running on apple user
################################################################

################################################################
Repo already cloned, using it as install directory
################################################################

################################################################
Create and activate python venv
################################################################

################################################################
Launching launch.py...
################################################################
Python 3.10.12 (main, Jul 28 2023, 18:34:01) [Clang 14.0.3 (clang-1403.0.22.14.1)]
Version: v1.5.1
Commit hash: 68f336bd994bed5442ad95bad6b6ad5564a5409a
Installing torch and torchvision
Looking in indexes: https://pypi.tuna.tsinghua.edu.cn/simple
Collecting torch==2.0.1
  Using cached https://pypi.tuna.tsinghua.edu.cn/packages/5a/77/778954c0aad4f7901a1ba02a129bca7467c64a19079108e6b1d6ce8ae575/torch-2.0.1-cp310-none-macosx_11_0_arm64.whl (55.8 MB)
Collecting torchvision==0.15.2
  Using cached https://pypi.tuna.tsinghua.edu.cn/packages/d2/bf/4cd5133120e6cbcc2fa5c38c92f2f44a7486a9d2ae851e3d5a7e83f396d5/torchvision-0.15.2-cp310-cp310-macosx_11_0_arm64.whl (1.4 MB)
Collecting filelock (from torch==2.0.1)
  Using cached https://pypi.tuna.tsinghua.edu.cn/packages/00/45/ec3407adf6f6b5bf867a4462b2b0af27597a26bd3cd6e2534cb6ab029938/filelock-3.12.2-py3-none-any.whl (10 kB)
Collecting typing-extensions (from torch==2.0.1)
...
...
Running on local URL:  http://127.0.0.1:7860 

To create a public link, set `share=True` in `launch()`.
Startup time: 3.6s (launcher: 0.2s, import torch: 1.4s, import gradio: 0.4s, setup paths: 0.4s, other imports: 0.4s, load scripts: 0.3s, create ui: 0.3s).
DiffusionWrapper has 859.52 M params.
Applying attention optimization: InvokeAI... done.
Model loaded in 4.4s (load weights from disk: 0.4s, create model: 0.5s, apply weights to model: 1.7s, apply half(): 1.1s, move model to device: 0.5s, calculate empty prompt: 0.2s).
^CInterrupted with signal 2 in <frame at 0x10fc7f290, file '/opt/homebrew/Cellar/python@3.10/3.10.12_1/Frameworks/Python.framework/Versions/3.10/lib/python3.10/threading.py', line 324, code wait>

```

- 在浏览器端打开 “Running on local URL”后的那个链接，即可。

-------------


