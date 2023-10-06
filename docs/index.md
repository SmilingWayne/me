---
statistics: true
hide:
  - feedback
---

# (๑• . •๑)


<br>

<p></p>

=== "<font size = 6>:fontawesome-solid-paw: </font><font size = 6 face = "savoye LET" >About Me</font>"

    - 🧑‍🎓 一个时刻想要变得不普通的普通人。你可以叫我 "笑笑" 。

    - 📖 喜欢阅读，有时观影，偶尔编程 :material-language-python: | :material-language-swift: | :material-language-java:，不事劳作。

    - 🎻 “有柴小协[^1]的日子就是好日子。”

    - 🥀 “知君兴尽欲回舟，日暮天寒不可留。”[^2]

    - 🧸 <font face = "American Typewriter" >INFJ-T</font>[^3] / 谨慎的自由主义[^4]者 / 努力学习语言中。
          
        > (中文 / English / Français)。

    - 🌏 暂居南京。

=== "<font size = 6>:fontawesome-solid-book: </font><font size = 6 face = "savoye LET">About The NoteBook</font>"

    - 💹 网站页面总数：{{pages}} ；
    
    - 🔠 总字数：{{words}} ；
    
    - 🤖 代码块行数：{{codes}} ；

    - 🛩️ 网站运行时间：<span id="web-time"></span> ；

    !!! abstract "本站点溯源"

        最初计划是一个电子读书笔记仓库，记录阅读感想、生活思考和碎碎念，后陆续增补观影笔记、学习笔记、课程笔记、刷题记录，体量渐增。

        - 2023.06.14  增补 Leetcode 刷题记录；
        - 2023.04.17  增加全新的字数统计功能；
        - 2023.02 增补学习笔记；
        - 2022.12.30 开始搭建电子读书笔记仓库；


=== "<font size = 6>:fontawesome-solid-envelope: </font><font size = 6 face = "savoye LET">Contact Me</font>"

    - :fontawesome-solid-envelope:  <a href="mailto:xiaoxiaowayne@163.com">个人邮箱</a>，:fontawesome-regular-envelope: <a href = "mailto:zx_wang@smail.nju.edu.cn">NJU 邮箱</a>；

    - :fontawesome-solid-pen-nib: [我的豆瓣](https://www.douban.com/people/174239371/)；

    - 小红书: [Wayne是笑笑🦆](https://www.xiaohongshu.com/user/profile/5d1238860000000011038629)；


<!-- brands/regular/solid -->
<br>


<center> <font face = "Apple chancery" size = 5>Bienvenue sur mon site! 🌼</font></center>


- 💻 PC端：点击顶部导航栏选择主题，左侧查看目录；
- 📱 移动端：点击左上角图标选择内容；
- 🔍 搜索：支持中文检索。

[^1]: The Violin Concerto in D major, Op. 35 was the only concerto for violin composed by Pyotr Ilyich __Tchaikovsky__. Composed in 1878, it is one of the best-known violin concertos.(From [WiKi](https://en.wikipedia.org/wiki/Violin_Concerto_(Tchaikovsky)))
[^2]: 语出清代黄景仁[《冬日克一过访和赠·其三》](https://www.gushici.net/shici/941/941269.html)。
[^3]: In personality typology, the **Myers–Briggs Type Indicator** (MBTI) is an introspective self-report questionnaire indicating differing psychological preferences in how people perceive the world and make decisions. It enjoys popularity despite being widely regarded as pseudoscience by the scientific community. <font face = "American Typewriter" >INFJ-T</font> means ==advocates==, former 4 letters indicates **"Introverted, Intuitive, Feeling, and Judging"**, meanwhile the last T stands for **"Turbulent"**. (From [Wiki](https://en.wikipedia.org/wiki/Myers–Briggs_Type_Indicator) and [Source](https://psychreel.com/infj-t/)).
[^4]: Liberalism is a political and moral philosophy based on the rights of the individual, liberty, consent of the governed, political equality and equality before the law. (From [WiKi](https://en.wikipedia.org/wiki/Liberalism))



<script>
function updateTime() {
    var date = new Date();
    var now = date.getTime();
    var startDate = new Date("2022/12/29 09:10:12");
    var start = startDate.getTime();
    var diff = now - start;
    var y, d, h, m;
    y = Math.floor(diff / (365 * 24 * 3600 * 1000));
    diff -= y * 365 * 24 * 3600 * 1000;
    d = Math.floor(diff / (24 * 3600 * 1000));
    h = Math.floor(diff / (3600 * 1000) % 24);
    m = Math.floor(diff / (60 * 1000) % 60);
    if (y == 0) {
        document.getElementById("web-time").innerHTML = d + "<span class=\"heti-spacing\"> </span>天<span class=\"heti-spacing\"> </span>" + h + "<span class=\"heti-spacing\"> </span>小时<span class=\"heti-spacing\"> </span>" + m + "<span class=\"heti-spacing\"> </span>分钟";
    } else {
        document.getElementById("web-time").innerHTML = y + "<span class=\"heti-spacing\"> </span>年<span class=\"heti-spacing\"> </span>" + d + "<span class=\"heti-spacing\"> </span>天<span class=\"heti-spacing\"> </span>" + h + "<span class=\"heti-spacing\"> </span>小时<span class=\"heti-spacing\"> </span>" + m + "<span class=\"heti-spacing\"> </span>分钟";
    }
    setTimeout(updateTime, 1000 * 60);
}
updateTime();
function toggle_statistics() {
    var statistics = document.getElementById("statistics");
    if (statistics.style.opacity == 0) {
        statistics.style.opacity = 1;
    } else {
        statistics.style.opacity = 0;
    }
}
</script>