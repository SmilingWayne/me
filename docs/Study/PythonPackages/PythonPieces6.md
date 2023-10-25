# 1行代码生成你的VX读书记录

前两天看Hello Github看到一个很有意思的Python小项目。大家都熟悉Github首页上的日历海报图，像这样：

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202310251151274.png)

但是毫无疑问自己做起来会有麻烦～

这个时候就需要万能的Python出场了。我们用到一个Python包GithubPoster。可以**在Python环境下**用pip直接安装：


``` Shell
pip3 install -U 'github_poster[all]
```

安装过程如下：

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202310251151275.png)

接下来是最难的步骤：获取你微信读书的cookies，有了cookies就可以获取你的阅读记录信息了。步骤如下：

- 1⃣️ 在**电脑端**（推荐，移动端太麻烦）进入浏览器，打开VX阅读官网`https://weread.qq.com`。然后**用手机扫码登录。**


- 2⃣️ 登录后你应该能看到你的书架，这时候在浏览器中按F12进入开发者模式。如果没有效果，可能是没有打开浏览器开发者模式权限，可以baidu获取解决方案。


- 3⃣️ 进入开发者模式后，点击Network → 选择文件 → 点击Headers，这个时候应该可以看到网络请求头。具体操作见后图。
  
- 4⃣️ 在请求头界面下滑，找到一个cookie开头的数据，很长，**全部复制下来**，cookie和冒号**不要复制**，只复制后面的一串数据。至此最重要的一步就完成了。


- 5⃣️ 最后一步，也是你唯一需要执行的代码，进入你的Python环境中，把这句话复制进去：

```Shell
github_poster weread --weread_cookie 
"your weread cookie" --year 2020-2022 --me "your name"
```

⚠️⚠️ 要把"your weread cookie" 替换成**你自己刚刚复制的**， "your name"换成你的用户名。

- 6⃣️ 最后在命令行执行你的一长串字符命令即可。我的命令（的部分）如下：

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202310251151276.png)

- 7⃣️ 等他执行完毕，会在你当前目录下出现一个文件夹：OUT_FOLDER，文件夹里会有一个svg文件，在浏览器或者别的可以打开的软件中打开即可。

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202310251151277.png){: style = "width: 100px"}


![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202310251151278.svg)

