---
statistics: true
---

# <font face = "KaiTi">(๑• . •๑)</font>

<!-- For full documentation visit [mkdocs.org](https://www.mkdocs.org). Nice to see you. This is xiao xiao! -->
<!-- <center><font face = "savoye LET" size = 6>A Very Brief Introduction</font></center> -->
<br>

<p></p>

=== "<font size = 6>:fontawesome-solid-paw: </font><font size = 6 face = "savoye LET" >About Me</font>"

    - 🧑‍🎓 一个时刻想要变得不普通的普通人。你可以叫我 "笑笑" . 

    - 📖 喜欢阅读，有时观影，偶尔编程 :material-language-python: | :material-language-swift: | :material-language-java:，不事劳作。

    - 🎻 “有柴小协[^1]的日子就是好日子。”

    - 💖 “毕竟几人真得鹿，不知终日梦为鱼。”[^2]

    - 🧸 <font face = "American Typewriter" >INFP</font> / 谨慎的自由主义[^3]者 / 努力学习语言.ing。
    
    - 📝 我的书 / 影记录可以看[我的豆瓣](https://www.douban.com/people/174239371/)。那里和这里一样静悄悄。

=== "<font size = 6>:fontawesome-solid-book: </font><font size = 6 face = "savoye LET">About The NoteBook</font>"

    - 💹 网站页面总数：{{pages}} ；
    
    - 🔠 总字数：{{words}} ；
    
    - 🦾 代码块行数：{{codes}} ；

    - 🛩️ 网站运行时间：<span id="web-time"></span>；

=== "<font size = 6>:fontawesome-solid-envelope: </font><font size = 6 face = "savoye LET">Contact Me</font>"

    - 📮 邮箱 `xiaoxiaowayne@163.com`

<br>



<center> <font face = "Apple chancery" size = 5>Bienvenue sur mon site! 🌼</font></center>


- 💻 PC端：点击顶部导航栏选择主题，左侧查看目录；
- 📱 移动端：点击左上角图标选择内容；
- 🔍 搜索：支持中文检索。

[^1]: The Violin Concerto in D major, Op. 35 was the only concerto for violin composed by Pyotr Ilyich __Tchaikovsky__. Composed in 1878, it is one of the best-known violin concertos.
[^2]: 语出宋代黄庭坚[《杂诗七首》](https://www.gushici.net/shici/102/102214.html)。
[^3]: Liberalism is a political and moral philosophy based on the rights of the individual, liberty, consent of the governed, political equality and equality before the law. (From Wiki)



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