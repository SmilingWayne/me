# Python智能的模块管理包：pipreqs

在开源Python项目中常常会看到 requirements.txt文件，大概长这样：


<img src = "../../picx/pipreqs1.png" height = "20%">

这种txt文件可以简单清晰地告知其他使用者需要调用的开源模块，方便使用。一种比较常见的方法是，先进入Python安装环境，在终端里用这样一条语句输出requirements：

``` Python
pip freeze > requirements.txt
```

但是这样输出有一些不好，因为它会输出你当前环境中所有的模块，即使相当一部分模块在项目中并没有用到，它也会保存下来，比如这样：

<img src = "../../picx/pipreqs2.png" height = "20%">

很不实用，而且动辄几百行。

这时可以用 `pipreqs` 这个库。使用如下命令安装：


``` Python 
 pip install pipreqs
```
进行安装，安装完毕后在项目根目录下执行（前提是先进入Python环境）
``` Python
pipreqs ./ 
```

它会扫描每一个文档，把其中用到的库（以及版本）都输出，舍弃掉那些没有用到的库。等运行完毕后所以同一个项目内容就缩减到：

<img src = "../../picx/pipreqs3.png" height = "20%">

短短几行。很实用。