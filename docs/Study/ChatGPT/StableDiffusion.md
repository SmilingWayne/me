# WebUI + Stable Diffusion 在 Apple Silicon下的安装教程


!!! abstract "我的设备"
    - 2022年MacBook Pro，512GB + 16GB，Ventura 13.5， Apple Silicon M2

    2025.09.28 本部分的内容会尽快迁移至人工智能模块。


!!! note "参考链接"
    - [英文版：如何在Apple Silicon上安装webUI](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Installation-on-Apple-Silicon)，理论上说这一份文档就够了，但是你需要一些前置知识，并不是零基础。不过，无论如何，都建议详细地阅读这个文档的每一个角落。他甚至告诉了你怎么查看模型运行时候的内存压力图。
    - [中文版｜B站｜本地部署Stable Diffusion](https://www.bilibili.com/video/BV1Pb411X79e/?spm_id_from=333.788&vd_source=1a29610636fa88d6406dc45fc2d153ba)：很可爱的Up主，讲得十分干货十分具体，按照她的来就可，她整理的资源也非常全面；


- 简单说来就是几个步骤：

1. 安装[homebrew](https://brew.sh)；macOS使用者几乎必备的工具
2. 安装[Xcode](https://developer.apple.com/xcode/)；非必需，但是我老早以前就装好了，但凡涉及到需要执行`xcode-select --install` 命令的都是这玩意；本来是专门为Apple公司产品开发的一个工具，但是其内部配置和macOS深度集成，一些零基础的同学不妨用空间换效率，虽然大了一点，但是起码可以省很多事；
3. 从[Github仓库](https://github.com/AUTOMATIC1111/stable-diffusion-webui)克隆，可以看我上面的中文推荐链接；
4. 进入下载下的文件夹，执行安装命令。


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

----


## 20240521 更新一下从0到1部署过程中出现的新问题

1. 出现报错：

```
AttributeError: 'NoneType' object has no attribute 'lowvram'
```

这个情况的本质，在[这个链接](https://github.com/AUTOMATIC1111/stable-diffusion-webui/issues/15568)里面已经说得很详细：需要重新安装整个repo，因为一开始下载的Stable Diffusion的模型文件可能是不完整有损坏的。


2. 出现报错 

```
Cannot convert a MPS Tensor to float64 dtype as the MPS framework doesn't support float64. Please use float32 instead
```

这个问题在PyTorch使用中也会出现，主要是Apple Silicon的MPS框架支持的浮点数精度不匹配的问题。在[这个链接](https://github.com/AUTOMATIC1111/stable-diffusion-webui/issues/12907) 已经讨论了很多。也有一些解决方案，但是不少方案的意思是，强制用CPU而不调用GPU进行渲染。

> 比如这一种解决方案：打开 `webui-macos-env.sh`文件，修改同前缀的命令为： `export COMMANDLINE_ARGS="--skip-torch-cuda-test --no-half --use-cpu all"`。

这样可以解决问题但是不治本。因为实际上是强制使用CPU进行渲染，速度真的会慢得感人。同等Prompt以及模型、尺寸，配合Apple Silicon的加速，512x512可以在至少可以在30～40s出图，但是只用cpu会跑201s。

我的解决方案（在Apple Silicon M2, Ventura 13.5上测试通过）：

- 在上面提到的 `webui-macos-env.sh`，对应的那一行，修改成： 

```
export COMMANDLINE_ARGS="--skip-torch-cuda-test --upcast-sampling --no-half-vae --disable-model-loading-ram-optimization"`
```
- 然后， 在运行 `./webui.sh` 命令的时候，修改命令为 

```
./webui.sh --opt-split-attention-v1
```

然后，就可以正常切换模型并运行了。(同样[参考Reddit链接](https://www.reddit.com/r/StableDiffusion/comments/1bk9pc2/cannot_convert_a_mps_tensor_to_float64_dtype_as/))

3. 对于一些Git Fetch超时、无法download 某某文件夹的问题，**优先考虑：自己的梯子是否通畅、网速是否够快。**

-------------


## 一些笔记和记录

- Stable Diffusion 3 （Up to date），目前正在用的是Stable Diffusion 2.1. 请记住这家公司：Stability AI。
- Pruned的模组：生成速度会相比快一点；
- emonly模组：压缩过的模组：图的效果差一点。
- FP16 / FP32：浮点位的精度。FP16是默认的精度：适合用来训练、用插件生成图；
- Full / -trained / emerged： 如果基于LoRA进行训练，要优先选用Full的模组。

!!! note "What is VAE"
    变分自动编码器 （VAE） 是一种技术，用于提高使用文本到图像模型 Stable Diffusion 创建的 AI 生成图像的质量。VAE将图像编码为潜在空间，然后将该潜在空间解码为新的、更高质量的图像。

    - .safecensor / .ckpt / .pt：(直接丢到webui对应的那个文件夹即可)

**What is SDXL**
:    Stable Diffusion XL，也称为 SDXL， 是 Stability AI 发布的下一代开放权重 AI 图像合成模型。代表了 AI 图像生成模型的最新进展。它擅长生成逼真的面孔，在图像中生成清晰的文本，并增强整体图像构图。

    > "more vibrant and accurate colors, better lighting, contrast, and shadows."

    SDXL 也允许用户使用一小组图像专门针对特定主题或主题生成图像。这种微调功能使用户能够更轻松地创建自定义图像。

**What is CLip**
:   查阅一下资料解释。

**What is LoRA**
:   说来话长。这个慢慢解释。

**What is ControlNet**
:   说来话长，这个也慢慢结束。
-----

!!! warning "用于测试的一份cheatsheet"

比如你下载下Counterfeit V3.0 的模型之后，设置Prompt：

```
(masterpiece, best quality),1girl with long white hair sitting in a field of green plants and flowers, her hand under her chin, warm lighting, white dress, blurry foreground
```

其他的随便，图片大小512x512，理应在30s左右能出图。


-----


## 附后记及鸣谢


!!! quote "谨以两张隐去真实信息但取材自真实情感、真实场景的AI创作，表达笔者对某位南国佳人的真挚感谢。"


![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202405270012027.png)
