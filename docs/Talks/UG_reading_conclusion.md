# 一份机缘巧合下制作的借书情况统计

!!! quote "感谢GPT-4o在本文章编写中提供的帮助。"

事情是这样的。2023年从仙林离开之后，暑假期间学校清空了毕业生的统一身份认证信息，本科阶段的绿卡（指该卡的颜色是绿色，无褒贬义）也就失效了，连带着图书馆、体育馆的身份认证也都没了。当时只顾着玩，没在乎那么多。等到了研究生阶段发现，自己没那么多空看书了，每天浑浑噩噩。就想着找找自己当初的阅读记录，看看自己阅读过哪些书。

不过..不过为时已晚，我的统一身份认证无法登陆信息门户，并且由于注册了新的研究生信息，我的登录状态也维持在了研究生的新卡。没法搞到过去的数据了。当时懊恼了很久。

然后，在2024年4月16号，一本研究生期间借阅的福柯的书没及时归还。闲着没事就去图书馆微信公众号上看看有什么恶劣影响（其实啥也没有，5天内还到图书馆你1分钱的罚金也不用交）。然后就震惊地发现一个林间小路：

在**南京大学图书馆**微信公众号上，对话窗口里选择 “我” ，跳转到首页后选择 “我的借阅” ，右上角选择：“借阅历史”。你会看到：自己的本科借阅记录竟然安安静静地躺在这！应该是本科阶段用自己的身份认证登录过图书馆，毕业后没有用新身份登录，所以阴差阳错地被我发现了。

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202405201211453.PNG)

在公众号里用浏览器打开，可以直接走到网页版。走到网页版，就可以在浏览器的开发者模式把源码拉下来。



通过一些精妙的正则表达式，可以顺藤摸瓜把所有的书以及相关信息整理出来。

> 存储借阅信息的网页源码：

```

<body>
<div class="page">
    <div class="weui-tab">
        <div class="weui-navbar">
            <div href="#tab1" class="weui-navbar__item">当前借阅</div>
            <div href="#tab2" class="weui-navbar__item weui-bar__item_on">借阅历史</div>
        </div>
        <div class="weui-tab__panel">
            <div class="tab_item" id="tab1">
                <div id="LoanShowArea">

                </div>
                <div class="weui-panel__ft" id="LoanListMore">
                    <a href="javascript:void(0);" class="weui-cell weui-cell_access weui-cell_link">
                        <div class="weui-cell__bd">查看更多</div>
                        <span class="weui-cell__ft"></span>
                    </a>
                </div>
            </div>
            <div class="tab_item active" id="tab2">
                <div id="HistoryShowArea">

                <div class="history_item">
                        <p class="history_title">
                           <a href="/weixin/searchResultDetail/getDetail?recordId=481281&amp;mappingPath=njulib&amp;groupCode=200027&amp;openid=oeL7DjuxMvReE0VnpXsDJU4EJTR4&amp;pubId=1">
                              <b>书名</b>
                           </a>
                        </p>
                        <p class="history_info">
                            作者
                        </p>
                        <p class="history_info">
                            条码号
                        </p>
                        <p class="history_info">
                            财产号
                        </p>
                        <p class="history_info">
                            年卷期
                        </p>
                        <p class="history_info">
                            所属馆藏地：仙林图书借阅区
                        </p>
                        <p class="history_info">
                            借阅日期：2023-05-19&nbsp;|&nbsp;应还日期：2023-06-19&nbsp;|&nbsp;实还日期：2023-06-16
                        </p>
                    </div>
```

整理到Excel后，删除一些无用数据（当天因为技术原因借阅即归还的不在统计范围内），用Python做一些简单的可视化：

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202405201156059.png)

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202405201156987.png)

在仙林的四年（实际上是3年半，因为2020年1月到8月因为一些众所周知的原因，全部在家，没有借阅记录），共记录下了**221条图书借阅记录**，**最长的借阅时间225天**（感谢疫情，这个记录估计很难被打破了）。总借阅天数：**6579天** （ = $\sum$ 借阅天数 $\forall$ Books ）。

阅读的峰值出现在2021年（尤其是3～6月份）。而年级增高，自己的阅读真是直线下降。

而到了研究生，这个数据（估计）就更加不堪入目了。

往之不可谏，知来者之可追。埋一个小宝藏在这里。