# 一个交通er（物流er）给研一新生的Brief

## 论文相关

首先先推荐一个网站：http://www.fms-journal.net/journals/ 可以看看现在管科领域哪些期刊比较好。记得在筛选栏里选择“交通运输管理” 或者 “运筹与管理”。评级A～B的优先看。其他的谨慎看。

> 质量不高的论文越看越GG.

其次需要学会使用Google学术、论文检索技巧。这个就不展开了，我反正会的就只有：

> 是否能够：
>
> - 按照关键词检索
> - 设置文献年份
> - 设置文献期刊来源

差不多了，毕竟无志向于学术...有需要其他更高级检索的话直接Google查一下。<u>不要总是使用CNKI。</u>

丢几个期刊在这里。

Management Science （MS）
:   很顶。感觉更偏模型场景。但是和物流是否相关，要结合论文仔细仔细筛选。

Operations Research (OR)
:   顾名思义。但是有不少和物流不相关的。要筛。

Transportation Science (TS)
:   交通的，够顶，但是和物流是否相关，要结合论文仔细仔细筛选。

Transportation Research (Part A ~ E ) 系列（TR - A/B/C/D/E/F）
:   A： 政策相关，侧重实证研究；

    B： Methodological，其实偏重数理，看起来可能有点难。但是有一些文章是和物流供应链有关。🌟🌟🌟质量很高。

    C：Emerging Technologies，我看得比较多。组内用到较多的交通相关、物流相关都有涉及。质量靠谱。🌟🌟🌟

    D： Transport and Environment，看得不多，也是偏政策和环境。看起来简单一些；

    E：Logistics and Transportation Review，直接与物流相关。可以优先关注。🌟🌟🌟

    F：侧重心理学相关，我不怎么看。（指从没看过）


European Journal of Operational Research(EJOR)
:   涉及的范围也比较广。H组投/看的都比较多。运筹各个领域都有。物流也不少。很推荐去看看。

INFORMS Journal on Computing 
:   往往能找到意外之喜。

其他的一些我想起来的：

- Annals of Operations Research (AOR)
- Transportmetrica A: TS，侧重于政策，感觉写Introduction会用到

-----

接几个中文期刊（我自己看得不算多，CNKI上期刊搜不到好的文章的话，**十分建议**搜硕士/博士论文。记得找一些好一点的学校的）。

- 管理科学学报	
- 管理工程学报	
- 系统工程理论与实践	
- 系统工程学报	
- 管理科学 


-----

## ORer平时可以看的一些信息源

请注意信息搜集和整合的能力。多看多想多实践。有想法要和导师聊。要扩大自己的视野、平台、能力。打赢信息战！

推荐几个微信公众号（ORer应该关注过不少了，因为确实就几个做得不错的）。

|          名称          |                       备注                       |
| :--------------------: | :----------------------------------------------: |
| 交通运输工程与信息学报 |         交通相关的，但是有一些和物流无关         |
|       数据魔术师       |       会有一些国内国外运筹资讯或者报名分享       |
|       运筹OR帷幄       |      什么资料都有。几乎做成国内OR权威平台了      |
|       运筹Offer        |                同上，更侧重offer                 |
|         运小筹         |      有~~一些~~ 不少 代码，是清深那边在维护      |
|       小马过河啊       |     交通相关的为主，可以了解下组内其他的课题     |
|        航音绕梁        | 同济梁哲老师团队运营的。主要是和航空业联系紧密。 |

再分享几个B站的吧。（不代表我自己全都看过）

[3Blue1Brown](https://space.bilibili.com/88461692/) ： 我比较推荐去油管看。很经典的UP。

[交通小张爱摸鱼](https://space.bilibili.com/168828224/)： 东南大学程琳老师课题组的大佬！讲得很细致。从单纯形法到算法。运筹、算法、代码实现。[程老师](https://space.bilibili.com/480968966/)也有B站账号，里面与交通相关（UE均衡、城市交通网络）的不少，也推荐观看。程老师顺便把本科课程的学生汇报上传到了B站，[参考链接](https://space.bilibili.com/1723179839/)。

[王树森](https://space.bilibili.com/1369507485/)： 拓展下视野，想做搜推广、想基础算法速成都可以看。有一些和运筹相关，有一些和ML/DL相关。

[运筹优化与地理信息](https://space.bilibili.com/324539730/)： 有一些搬运的视频不错。也是运筹相关。

[爱可可爱生活](https://space.bilibili.com/23852932/) ： 北邮的老师。可以看他之前的Python课进行快速入门（我的Python就是看他的自学的...)。也有很多AI相关的启蒙。可惜现在不怎么更新了...

最后顺便**打个广告**，中国大学Mooc上可以找到我导的[最优化](https://www.icourse163.org/course/NJU-1465971171)课程。主要是凸优化相关。可以顺带看看。如果还想了解最优化的知识，参考[西北工业大学李原老师的B站](https://space.bilibili.com/507570322/)。

油管也有不少优质的，暂时先不罗列。

----

## 求解器


几乎必须要熟悉的。做物流，整数规划用得多一点。考虑：Gurobi（请自行搜索资料，学会看技术文档（不难找））。入门：[TSP with Lazy Constraint](https://www.gurobi.com/documentation/current/examples/tsp_py.html)

如果是做鲁棒优化这类的，待补充，这里我不是很熟悉！需要艾特G同学。

对于代码，我还是觉得自己上手摸清楚，做一个小项目，是最有用的。

[Ortools for VRP](https://developers.google.cn/optimization/routing/vrp?hl=en)： 快速上手VRP问题。

[Github 低空经济](https://github.com/optimatorlab/mFSTSP-VDS)： 我最近在看的。


----


## 低空经济指南（政策篇）

> 此处内容有删节，因为没什么干货，主要保存一些链接。

首先，看看**二十届三中全会**怎么说：[中共中央关于进一步全面深化改革 推进中国式现代化的决定](https://www.gov.cn/zhengce/202407/content_6963770.htm)，参考 `三·健全推动经济高质量发展体制机制`, 划重点如下：

!!! quote "深化综合交通运输体系改革，推进铁路体制改革，发展通用航空和==低空经济==，推动收费公路政策优化。提高航运保险承保能力和全球服务水平，推进海事仲裁制度规则创新"

接着看看**政府工作报告**怎么说：[2024年政府工作报告全文](https://www.gov.cn/yaowen/liebiao/202403/content_6939153.htm)， 参考 `2024年政府工作任务` 子标题，划重点如下：

!!! quote "巩固扩大智能网联新能源汽车等产业领先优势，加快前沿新兴氢能、新材料、创新药等产业发展，积极打造生物制造、商业航天、==低空经济==等新增长引擎。"

顺带，别忘了看看**人民日报**是怎么释经的: [“低空经济”加速起飞](https://www.gov.cn/yaowen/liebiao/202404/content_6943071.htm) !

同时也要流窜到**新华社**门口看看人家怎么说：[低空，何以经济](https://mp.weixin.qq.com/s/7JlA7yRGFaBdT3ToXE3CWg)；

闲暇之余我们看看**央视怎么宣传**：[2030年低空经济规模可达2万亿元！](https://tv.cctv.com/2024/03/09/VIDEsqWKfdoGiwT8NVH0yDCi240309.shtml)

我们还可以关注几个公众号：

- 低空经济观察

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202409141205109.png)

赢麻了！家人们！

