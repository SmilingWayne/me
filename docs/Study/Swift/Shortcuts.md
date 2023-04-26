# 快捷指令(shortcuts)使用指南
- 建议当伸手党不要自己写，这个真的自己做的时候非常像是“图形界面版写代码”（真·低代码平台）
- 如果自己写常常会有“原来我也会写脚本了！”的感动；
- [https://support.apple.com/zh-cn/guide/shortcuts/welcome/ios](https://support.apple.com/zh-cn/guide/shortcuts/welcome/ios)；官方链接；有不懂的直接查；写完会有一种成就感；
## 正在研究
1. 将快捷方式接入快捷键；
2. 将快捷方式接入其他软件；[https://support.apple.com/zh-cn/guide/shortcuts-mac/apd8195f96d6/6.0/mac/13.0](https://support.apple.com/zh-cn/guide/shortcuts-mac/apd8195f96d6/6.0/mac/13.0)
3. “内容图引擎”功能
## 我的成果：
- 我最开始的成果是搞了一个“随机吃饭助理”，可以帮你用随机数决策吃饭的地方（南大版），只需要半个下午的时间就可以做出来；
- 支持的功能：
    - 根据地点随机可以吃的饭；
    - 自定义随的内容（最强大功能），增强鲁棒性；
    - 精彩二选一
- 链接：[https://www.icloud.com/shortcuts/d8f7454b5e474e37b7591f0082d1b6eb](https://www.icloud.com/shortcuts/d8f7454b5e474e37b7591f0082d1b6eb) （初代版本）


## 复制粘贴小🔧

- shift + command + 5，截图。选中区域后，按住control + option（去除背景阴影色）再点击截图画面，就可以直接图片复制到剪贴板。



## dock双指上滑展示该程序所有窗口

- 在终端输入：
  
```text
defaults write com.apple.dock scroll-to-open -bool true && killall Dock
```

- 当然也可以在桌面选中这个程序用control + 方向下键

- 如何关闭：

```text
defaults write com.apple.dock scroll-to-open -bool false && killall Dock
```


- preview 中一页一页地滑动而不是一点点地：option  + 方向下键