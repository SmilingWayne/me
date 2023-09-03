# Python CheatSheet 之命令行篇


!!! question "用conda创立一个新的Python环境"

    ```shell
    conda create -n py310 python=3.10
    ```
    
    上面这行命令意思是：“用conda 创建了一个叫做“py310”的Python虚拟环境，这个虚拟环境的版本是Pythob 3.10”

    根据此，可以任意创建你想命名的Python版本了。

!!! question "进入conda创建的新环境中"
    
    ```shell
    conda activate <你的环境名称>

    ```
    如果你的conda 版本不够高，可能提示你用类似下面的命令：

    ```shell
    source activate XXX 
    ```
    

!!! question "罗列conda下所有的Python环境"

    ```shell
    conda env list
    ```

    执行后会出现：

    ```text
    # conda environments:
    #
    py310                    /Users/apple/anaconda3/envs/py310
    py38                  *  /Users/apple/anaconda3/envs/py38
    root                     /Users/apple/anaconda3
    ```

    类似的，标注了“*”的就是你当前处在的环境了。


!!! question "删除conda下的某个Python环境"

    ```shell
    conda env remove --name <环境名称>
    ```



|          操作          |         命令         |
| :--------------------: | :------------------: |
|     更新 homebrew      |    `brew update`     |
| 更新所有安装过的软件包 |    `brew upgrade`    |
|     更新指定软件包     | `brew upgrade *****` |
|       查找软件包       | `brew search *****`  |
|       安装软件包       | `brew install *****` |
|       卸载软件包       | `brew remove *****`  |
|  罗列出已安装的软件包  |     `brew list`      |
|     查找软件包信息     |  `brew info *****`   |
| 罗列出软件包的依赖关系 |  `brew deps *****`   |
|  列出可以更新的软件包  |   `brew outdated`    |


|           pip 操作           |                           命令                            |
| :--------------------------: | :-------------------------------------------------------: |
|       安装指定版本的包       |              `pip install <名称>==<版本号>`               |
|       罗列所有的安装包       |                        `pip list`                         |
|          卸载某个包          |                  `pip uninstall <名称>`                   |
|        更新指定软件包        |                    `pip upgrade *****`                    |
|          查找软件包          |                    `pip search *****`                     |
|     显示某个软件包的版本     |                     `pip show *****`                      |
| 安装的时候不知道安装什么版本 | `pip install numpy==`，会报错，然后提示你有哪些可以输入的 |

> 查找包的版本还可以导入后直接：

```Python
import numpy as np
np.__version__
```

!!! example "pip show XXX"
    ```shell
    (py38) MyMac:apple$ pip show matplotlib
    Name: matplotlib
    Version: 3.6.2
    Summary: Python plotting package
    Home-page: https://matplotlib.org
    Author: John D. Hunter, Michael Droettboom
    Author-email: matplotlib-users@python.org
    License: PSF
    Location: XXXXXXXX
    Requires: python-dateutil, fonttools, packaging, pillow, kiwisolver, numpy, pyparsing, cycler, contourpy
    Required-by: wordcloud, seaborn, sdf-fork, samila, prettymapp, osmnx, matrixprofile, fbprophet, dtreeviz, adtk
    ```