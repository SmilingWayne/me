# GPT 和它的一万种分身

!!! warning "这篇文字绝大多数撰写于2023～2024年初，考虑到大模型和人工智能发展之快，这里的许多内容可能已经过时。"

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
  - 最新更新：大家都快去用他家的[Claude 2](https://claude.ai/chats)！！！谷歌邮箱注册，可以直接读10MB以内的PDF文档！而且还是免费的！（现在有限制了）（要梯子），希望尽快开通API！

- [Bard](https://bard.google.com/): 谷歌的Bard，有时候蠢蠢的（不敢回答），有时候回答很详细，也不知道什么原理，但是注册什么的只要有Google 邮箱。确实非常方便。测试下来他的上下文也不长。个人觉得谷歌是想把大模型融入到用户的日常中，比如AI从你的邮件信息、地址搜索信息、浏览信息中入手，充当你的Personal Assistant。


--------------

- [Llama 2 online](https://huggingface.co/chat/)。在线版的Llama 2，编程效果不好，但是想一些点子，出出主意还是很方便的。中文使用下来感觉一般般，可以凑合地当个翻译；
    - Llama 2 目前7B的版本可以部署在macOS本地并且跑了，但是7B的效果挺差劲的，我看了好几个反馈都是如此，而70B的（也就是上面链接的）效果就还好，建议还是先观望，不着急入手。
    - [Meta自己的Llama实用教程](https://ai.meta.com/llama/get-started/)。

- [免费好用的中文GPT Kimi，可以读文档也可以读网页内容](https://kimi.moonshot.cn/)： 亲测效果不错，而且应该是针对中文做过相关的优化，感觉僵硬感少了很多。无需翻墙。

- [ChatGLM：中国LLM](https://github.com/THUDM/ChatGLM3)

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
- 一些开箱即用的免费文生图： 
    - [playground AI](https://playgroundai.com)，质感特别像Canva。效果不错。支持Canvas直接导入；
    - [Bing Image Creator](https://www.bing.com/images/create), 用的是最新的DALL.E.3，微软自己搞的。每个用户会有初始小金币，可以用来加速生成，但是耗尽了也没问题，因为只会生成速度变慢，不会说完全用不了；但是速度确实比较堪忧；会一下生成4张，效果比我想象的要好很多；
    - [Leonardo AI](https://app.leonardo.ai/ai-generations)，在固定时间内有使用次数限制，但是每天就会更新一次，所以可以续着用。可以有多个模型选，提供了一定程度的定制；

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202310251030259.png)

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202310251030257.jpeg)

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202310251030258.jpg)



> 由上到下分别是： PlayGroundAI, Bing Image Creator, Leonardo AI. Prompt是：pre raphaelite style oil painting texture young lady, flowers nearby, looking at the sea.

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

- [https://chatexcel.com/](https://chatexcel.com/)。效果还不错！免费，限制文件大小5MB，20列
  - 但是如果你是个熟练的Exceler那我还是建议自己抠Excel表格

## 语音转文字

- [Whisper](https://github.com/openai/whisper), 也是OpenAI做的。
    - 一个目前的工作流：下载到视频（[B站](https://xbeibeix.com/api/bilibili/)等对应不同的下载方式），飞书妙记自动识别英文、导出txt文稿；把txt文稿丢到Claude 2 中进行文本问答，从而总结归纳；
    - [一个网页版Demo](https://huggingface.co/spaces/Xenova/distil-whisper-web)：transformer.js 允许你在网页端直接用whisper，甚至你可以直接录一段话让他转译出来。甚至允许你导出成json格式，也可以上传视频！