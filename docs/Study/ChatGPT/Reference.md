# GPT 和它的一万种分身


## 关于汇总的汇总

- [https://gitlab.com/awesomeai/awesome-chatgpt-zh](https://gitlab.com/awesomeai/awesome-chatgpt-zh)： 一个长期更新的汇总；

- [Poe](https://poe.com/)：我愿称之关于汇总的汇总。免费注册可以免费使用Claude-instant / Sage / ChatGPT免费版，付费使用GPT-4等大模型。
    - 这些模型各异，他们的使用区别见[https://zhuanlan.zhihu.com/p/614720305](https://zhuanlan.zhihu.com/p/614720305)
## 链接大汇总

- [ChatGPT](https://chat.openai.com/): 不解释；

- [https://github.com/reorx/awesome-chatgpt-api](https://github.com/reorx/awesome-chatgpt-api)；

- Claude，OpenAI前科学家搞的，效果很不错，一些特定回答水平已经超过ChatGPT。我最开始是在slack上用的，后来还是选择去网页端；
  - 个人感觉Claude在解决“单次提问型问题”上思路有时超过ChatGPT，但是写代码和上下文逻辑理解是比较落后的
  - 一个典型的例子是通过和他沟通我的毕业论文，他很精确地给出了一个量化思路；但是GPT比较浮于表面
  - 另一个典型例子是解决Excel的问题时候，他给出的步骤往往非常详尽。
  - 免费，但是现在需要梯子了。
  - 最新更新：大家都快去用他家的[Claude 2](https://claude.ai/chats)！！！谷歌邮箱注册，可以直接读10MB以内的PDF文档！而且还是免费的！（要梯子），希望尽快开通API！

- [Bard](https://bard.google.com/): 谷歌的Bard，有时候蠢蠢的（不敢回答），有时候回答很详细，也不知道什么原理，但是注册什么的只要有Google 邮箱确实非常方便；

--------------

- [Llama 2 online](https://huggingface.co/chat/)。在线版的Llama 2，编程效果不好，但是想一些点子，出出主意还是很方便的。中文使用下来感觉一般般，可以凑合地当个翻译；
    - Llama 2 目前7B的版本可以部署在macOS本地并且跑了，但是7B的效果挺差劲的，我看了好几个反馈都是如此，而70B的（也就是上面链接的）效果就还好，建议还是先观望，不着急入手。

- 下面是我自己用过的：

## 读论文篇

- [https://chatdoc.com](https://chatdoc.com)
- [https://www.chatpdf.com](https://www.chatpdf.com)
    - 使用方法：把文档拖拽进去然后AI会学习PDF文档，你可以跟他交互、问他问题
- 免费，每天5篇文献的额度；
 
## 🎨艺术篇

- Midjourney: 有免费额度；效果很好；在discord上使用；
- Stable Diffusion，想试试Apple Silicon 上可以搞定的那个SD。见[具体链接](./StableDiffusion.md)。部署在本地的webui。
  - [https://zhuanlan.zhihu.com/p/610580694](https://zhuanlan.zhihu.com/p/610580694)，从Mochi Diffusion 上手开始实现

## 浏览器插件

- [https://immersive-translate.owenyoung.com](https://immersive-translate.owenyoung.com)：沉浸式多平台翻译工具；支持Safari, Chrome, Edge，最重要的是他能给你把显示的翻译、原文都显示在网页上；效果很不错；
- Voice Control，在小红书看到的一个GPT插件，可以支持语音输入+把GPT输出语音读出来，很适合**模拟英文面试**！
- Z-library Finder，找书插件，见[链接](../../Study/Swift/FindBooks.md).

## 自动生成网页 / PPT 等 
- [Gamma](https://gamma.app/): Gamma App，适合生成PPT / 网站等；

## iOS AI 生产力插件

- [https://github.com/reorx/Share-to-ChatGPT-Shortcut](https://github.com/reorx/Share-to-ChatGPT-Shortcut)，一个将Apple的快捷方式接入ChatGPT API 的方法。很好用！我已经安装上了！不出意外是需要梯子的！其他都是免费；


## NLP其他

- [https://wantquotes.net](https://wantquotes.net)清华开发的一个反向字典，可以根据你想要的意思输出相关名言名句。免费，微信登录即可；


## 让机器人帮你操作GPT

- [https://chatexcel.com/](https://chatexcel.com/)。效果还不错！免费，限制文件大小5MB，20行
  - 但是如果你是个熟练的Exceler那我还是建议自己抠Excel表格

## 语音转文字

- [Whisper](https://github.com/openai/whisper), 也是OpenAI做的。
    - 一个目前的工作流：下载到视频（[B站](https://xbeibeix.com/api/bilibili/)等对应不同的下载方式），飞书妙记自动识别英文、导出txt文稿；把txt文稿丢到Claude 2 中进行文本问答，从而总结归纳；