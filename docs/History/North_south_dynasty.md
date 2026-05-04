# 魏晋、南北朝笔记

说来也巧，前段时间去了趟佛狸祠（参考[不见神鸦社鼓](../Talks/Bilici.md)），然后莫名地对那段混乱的历史有了一点兴趣，挑了小半个下午搜集资料，然后就有了这个笔记。

北朝的就待补充吧！

哦对，感谢豆包的搜集工作与答疑，出乎意料地它搜集得格外的不错，准确度比我想得要高很多，意外之喜。

## 南朝

420-589。宋齐梁陈。“**南朝四百八十寺，多少楼台烟雨中。**”

### 宋

**刘裕**（“人道寄奴曾住”的那个“寄奴”）建立，共传4世8帝，不含1弑父篡权的“元凶”，国祚首尾60年 (420 - 479)，是南朝四代里最长的。

```mermaid
graph TD
    %% 定义样式
    classDef normal fill:#e3f2fd,stroke:#1565c0,stroke-width:2px,color:#000;
    classDef deposed fill:#ffebee,stroke:#c62828,stroke-width:2px,color:#000;
    classDef usurper fill:#f5f5f5,stroke:#616161,stroke-width:2px,stroke-dasharray: 5 5,color:#333;
    classDef founder fill:#e8f5e9,stroke:#2e7d32,stroke-width:3px,color:#000;

    %% 根节点（刘裕之父，虽未称帝但作为世系起点）
    Root[("父: 刘翘")]:::normal

    %% 第一代
    LiuYu["<b>(一) 武帝 刘裕</b><br/>在位: 420—422<br/>享年: 59岁 (363-422)<br/>开国皇帝，永初之治"]:::founder
    
    Root --> LiuYu

    %% 第二代
    LiuYiFu["<b>(二) 少帝 刘义符</b><br/>在位: 422—424<br/>享年: 18岁 (406-424)<br/>刘裕长子<br/>嬉戏无度，被废杀"]:::deposed
    
    LiuYiLong["<b>(三) 文帝 刘义隆</b><br/>在位: 424—453<br/>享年: 46岁 (407-453)<br/>刘裕第三子<br/>元嘉之治，被太子弑杀"]:::normal

    LiuYu --> LiuYiFu
    LiuYu --> LiuYiLong

    %% 第三代 (文帝的儿子们)
    LiuShao["<b>(四) 元凶 刘劭</b><br/>在位: 453.03—453.05<br/>享年: 29岁 (424-453)<br/>刘义隆长子<br/>弑父篡位，在位3个月"]:::usurper

    LiuJun["<b>(五) 孝武帝 刘骏</b><br/>在位: 453—464<br/>享年: 34岁 (430-464)<br/>刘义隆第三子<br/>讨逆即位，晚年奢侈"]:::normal

    LiuYu_Ming["<b>(六) 明帝 刘彧</b><br/>在位: 465—472<br/>享年: 33岁 (439-472)<br/>刘义隆第十一子<br/>杀侄夺位，屠杀兄弟"]:::normal

    LiuYiLong --> LiuShao
    LiuYiLong --> LiuJun
    LiuYiLong --> LiuYu_Ming

    %% 第四代 (孝武帝与明帝的儿子们)
    LiuZiYe["<b>(七) 前废帝 刘子业</b><br/>在位: 464—465<br/>享年: 16岁 (449-465)<br/>刘骏长子<br/>荒淫暴虐，被叔父所杀"]:::deposed

    LiuYu_Hou["<b>(八) 后废帝 刘昱</b><br/>在位: 472—477<br/>享年: 14岁 (463-477)<br/>刘彧长子<br/>生性残暴，被萧道成暗杀"]:::deposed

    LiuZhun["<b>(九) 顺帝 刘准</b><br/>在位: 477—479<br/>享年: 10岁 (469-479)<br/>刘彧第三子<br/>末代皇帝，禅位被杀"]:::deposed

    LiuJun --> LiuZiYe
    LiuYu_Ming --> LiuYu_Hou
    LiuYu_Ming --> LiuZhun

    %% 布局调整（尽量模拟树状结构）
    %% 刘劭虽然也是文帝之子，但为了图表清晰，这里作为分支列出
```

---

### 齐

齐是南朝四代里寿命最短的，仅24年，但共传3代7帝，这还是在**萧赜凭一己之力在位11年**狠狠刷了一波数据之后的结果。

另一个重要故事是，齐和后来的梁都是“萧”氏创立的，他们都是兰陵萧氏的后代。齐的创立者**萧道成是萧衍（梁的创立者）的族叔**。

```mermaid
graph TD
    %% 定义样式
    classDef emperor fill:#e3f2fd,stroke:#1565c0,stroke-width:3px,color:#000;
    classDef founder fill:#c8e6c9,stroke:#1b5e20,stroke-width:4px,color:#000;
    classDef deposed fill:#ffebee,stroke:#c62828,stroke-width:2px,color:#000;
    classDef ancestor fill:#f5f5f5,stroke:#9e9e9e,stroke-width:1px,color:#666;
    classDef liangFounder fill:#fff8e1,stroke:#f57f17,stroke-width:3px,color:#000;

    %% 共同祖先
    XiaoZheng["萧整<br/>(西晋淮阴令)<br/>兰陵萧氏共同祖先"]:::ancestor

    %% 萧整后裔分两支
    XiaoJuan["萧隽<br/>(长子支)"]:::ancestor
    XiaoXia["萧鎋<br/>(次子支)"]:::ancestor

    XiaoZheng --> XiaoJuan
    XiaoZheng --> XiaoXia

    %% 南齐线 - 萧隽支
    XiaoChengZhi["萧承之<br/>(萧道成之父)"]:::ancestor
    XiaoDaoSheng["萧道生<br/>(萧道成之弟)"]:::ancestor

    XiaoJuan --> XiaoChengZhi
    XiaoJuan --> XiaoDaoSheng

    %% 南齐第一代
    XiaoDaoCheng["<b>(一) 高帝 萧道成</b><br/>在位: 479—482 (3年)<br/>享年: 55岁 (427-482)<br/>建元年间<br/>开国皇帝，代宋建齐<br/>崇尚节俭，革除暴政"]:::founder

    XiaoChengZhi --> XiaoDaoCheng
    XiaoDaoSheng --> XiaoLuan

    %% 南齐第二代
    XiaoZe["<b>(二) 武帝 萧赜</b><br/>在位: 482—493 (11年)<br/>享年: 53岁 (440-493)<br/>永明年间<br/>萧道成长子<br/>永明之治，政局稳定"]:::emperor

    XiaoDaoCheng --> XiaoZe

    %% 文惠太子（萧赜长子，未即位）
    XiaoChangMao["萧长<br/>(文惠太子)<br/>萧赜长子，未即位即卒"]:::ancestor

    XiaoZe --> XiaoChangMao

    %% 南齐第三代
    XiaoZhaoYe["<b>(三) 郁林王 萧昭业</b><br/>在位: 493—494 (1年)<br/>享年: 21岁 (473-494)<br/>萧长懋长子<br/>荒淫无道，被萧鸾废杀"]:::deposed

    XiaoZhaoWen["<b>(四) 海陵王 萧昭文</b><br/>在位: 494.07—494.10 (3月)<br/>享年: 14岁 (480-494)<br/>萧长懋次子<br/>傀儡皇帝，被萧鸾废杀"]:::deposed

    XiaoChangMao --> XiaoZhaoYe
    XiaoChangMao --> XiaoZhaoWen

    %% 萧鸾支系（篡位）
    XiaoLuan["<b>(五) 明帝 萧鸾</b><br/>在位: 494—498 (4年)<br/>享年: 46岁 (452-498)<br/>建武、永泰年间<br/>萧道成侄子<br/>篡位后屠杀宗室殆尽"]:::emperor

    %% 萧鸾的儿子们
    XiaoBaoJuan["<b>(六) 东昏侯 萧宝卷</b><br/>在位: 498—501 (3年)<br/>享年: 18岁 (483-501)<br/>萧鸾次子<br/>昏庸暴虐，被萧衍击败"]:::deposed

    XiaoBaoRong["<b>(七) 和帝 萧宝融</b><br/>在位: 501—502 (1年)<br/>享年: 14岁 (488-502)<br/>萧鸾第八子<br/>末代皇帝，禅位被杀<br/>南齐灭亡"]:::deposed

    XiaoLuan --> XiaoBaoJuan
    XiaoLuan --> XiaoBaoRong

    %% 南梁线 - 萧鎋支
    XiaoShunZhi["萧顺之<br/>(萧衍之父)<br/>萧道成族弟，曾辅佐建齐"]:::ancestor

    XiaoXia --> XiaoShunZhi

    XiaoYan["<b>梁武帝 萧衍</b><br/>在位: 502—549 (47年)<br/>享年: 85岁 (464-549)<br/>萧顺之次子<br/>代齐建梁，南朝在位最长"]:::liangFounder

    XiaoShunZhi --> XiaoYan

    %% 齐梁关系标注
    XiaoDaoCheng -.->|族叔 | XiaoYan
    XiaoDaoCheng -.->|族弟 | XiaoShunZhi

    %% 辈分对齐 - 使用subgraph和rank=same
    subgraph Gen1["第一代（同辈）"]
        direction LR
        XiaoDaoCheng
        XiaoLuan
    end

    subgraph Gen2["第二代（同辈）"]
        direction LR
        XiaoZe
    end

    subgraph Gen3["第三代（同辈）"]
        direction LR
        XiaoChangMao
        XiaoBaoJuan
        XiaoBaoRong
    end

    subgraph Gen4["第四代（同辈）"]
        direction LR
        XiaoZhaoYe
        XiaoZhaoWen
    end

    %% 隐藏连接用于对齐
    XiaoDaoCheng ~~~ XiaoLuan
    XiaoBaoJuan ~~~ XiaoBaoRong
    XiaoZhaoYe ~~~ XiaoZhaoWen
```


### 梁

萧衍建立，正统认为梁4帝（萧衍 -> 萧纲 -> 萧绎 -> 萧方智），首尾55年，侯景之乱、北齐干预亦立有3傀儡帝王，并附。

```mermaid
graph TD
    %% 定义样式
    classDef legitimate fill:#e8f5e9,stroke:#2e7d32,stroke-width:3px,color:#000;
    classDef puppet fill:#fff3e0,stroke:#ef6c00,stroke-width:2px,stroke-dasharray: 5 5,color:#000;
    classDef illegitimate fill:#ffebee,stroke:#c62828,stroke-width:2px,color:#000;
    classDef founder fill:#c8e6c9,stroke:#1b5e20,stroke-width:4px,color:#000;

    %% 根节点（萧衍之父）
    Root[("父: 萧顺之")]:::legitimate

    %% 萧衍兄弟辈
    XiaoYi["萧懿<br/>(萧衍之兄)"]:::legitimate
    XiaoHong["萧宏<br/>(萧衍之弟)"]:::legitimate

    Root --> XiaoYi
    Root --> XiaoDer
    Root --> XiaoHong

    %% 第一代 - 开国皇帝
    XiaoDer["<b>(一) 武帝 萧衍</b><br/>👑 正统开国<br/>在位: 502—549 (47年)<br/>享年: 85岁 (464-549)<br/>天监/普通/大通/太清年间<br/>晚年崇佛，侯景之乱饿死台城"]:::founder

    %% 第二代 - 萧衍的儿子们
    XiaoTong["萧统<br/>(昭明太子，萧衍长子)<br/>编《文选》<br/>未即位，31岁早逝"]:::legitimate
    
    XiaoGang["<b>(二) 简文帝 萧纲</b><br/>👑 正统<br/>在位: 549—551 (2年)<br/>享年: 48岁 (503-551)<br/>萧衍第三子<br/>侯景扶持傀儡，后被侯景废杀<br/>擅长宫体诗创作"]:::legitimate

    XiaoYi2["<b>(三) 元帝 萧绎</b><br/>👑 正统<br/>在位: 552—554 (2年)<br/>享年: 46岁 (508-554)<br/>萧衍第七子<br/>江陵称帝，平定侯景之乱<br/>西魏破城被俘遇害，好文学藏书"]:::legitimate

    XiaoDer --> XiaoTong
    XiaoDer --> XiaoGang
    XiaoDer --> XiaoYi2

    %% 第三代 - 萧统的儿子（萧栋之父）
    XiaoHuan["萧欢<br/>(萧统长子)"]:::legitimate
    XiaoTong --> XiaoHuan

    %% 第四代 - 萧衍的曾孙
    XiaoDong["<b>(四) 废帝 萧栋</b><br/>⚠️ 非正统<br/>在位: 551.10—551.11 (1月)<br/>享年: ?岁 (?-552)<br/>萧统之孙/萧衍曾孙<br/>侯景废萧纲后拥立<br/>禅位侯景，后被萧绎赐死"]:::illegitimate

    XiaoHuan --> XiaoDong

    %% 萧衍侄子辈（非正统）
    XiaoZhengDe["<b>(五) 伪帝 萧正德</b><br/>⚠️ 非正统/伪帝<br/>在位: 548—549 (1年)<br/>享年: ?岁 (?-549)<br/>萧宏长子/萧衍侄<br/>侯景之乱投靠侯景被拥立<br/>篡位僭号，后被侯景诛杀"]:::illegitimate

    XiaoYuanMing["<b>(六) 闵帝 萧渊明</b><br/>⚠️ 非正统<br/>在位: 555 (数月)<br/>享年: ?岁 (?-556)<br/>萧懿之子/萧衍侄<br/>北齐扶持立为南朝梁帝<br/>朝臣兵变被废，不久病逝"]:::puppet

    XiaoHong --> XiaoZhengDe
    XiaoYi --> XiaoYuanMing

    %% 第五代 - 萧绎的儿子
    XiaoFangZhi["<b>(七) 敬帝 萧方智</b><br/>👑 正统/末代<br/>在位: 555—557 (2年)<br/>享年: 15岁 (543-558)<br/>萧绎第九子<br/>绍泰/太平年间在位<br/>禅位陈霸先，南梁灭亡<br/>遗言被陈朝诛杀"]:::legitimate

    XiaoYi2 --> XiaoFangZhi

```

### 陈

陈，南朝的最后一个国家，共传三世五帝，首尾 33 年。陈朝的传承比较特殊——皇位从陈霸先传给了**侄子**陈蒨，后来又发生了**叔父陈顼**废侄子陈伯宗的事件。

```mermaid
graph TD
    %% 定义样式
    classDef emperor fill:#e3f2fd,stroke:#1565c0,stroke-width:3px,color:#000;
    classDef founder fill:#c8e6c9,stroke:#1b5e20,stroke-width:4px,color:#000;
    classDef deposed fill:#ffebee,stroke:#c62828,stroke-width:2px,color:#000;
    classDef ancestor fill:#f5f5f5,stroke:#9e9e9e,stroke-width:1px,color:#666;

    %% 根节点（陈霸先之父）
    ChenWenZan[("父: 陈文赞")]:::ancestor

    %% 陈霸先兄弟辈
    ChenDaoTan["陈道谭<br/>(陈霸先之兄)<br/>陈蒨、陈顼之父"]:::ancestor

    ChenWenZan --> ChenBaXian
    ChenWenZan --> ChenDaoTan

    %% 第一代 - 开国皇帝
    ChenBaXian["<b>(一) 武帝 陈霸先</b><br/>在位: 557—559 (2年)<br/>享年: 56岁 (503-559)<br/>永定年间<br/>开国皇帝，代梁建陈<br/>平定江南内乱，稳固基业"]:::founder

    %% 第二代 - 陈蒨（陈霸先之侄）
    ChenQian["<b>(二) 文帝 陈蒨</b><br/>在位: 559—566 (7年)<br/>享年: 44岁 (522-566)<br/>陈道谭长子/陈霸先侄<br/>天嘉、天康年间<br/>励精图治，开创天嘉之治"]:::emperor

    ChenDaoTan --> ChenQian

    %% 陈蒨的儿子们
    ChenBoZong["<b>(三) 废帝 陈伯宗</b><br/>在位: 566—568 (2年)<br/>享年: 16岁 (554-570)<br/>陈蒨长子<br/>光大年间<br/>年幼懦弱，被皇叔陈顼废黜<br/>降为临海王后遇害"]:::deposed

    ChenQian --> ChenBoZong

    %% 陈蒨的弟弟 - 陈顼
    ChenXu["<b>(四) 宣帝 陈顼</b><br/>在位: 568—582 (14年)<br/>享年: 52岁 (530-582)<br/>陈道谭次子/陈蒨弟<br/>太建年间<br/>废侄即位，勤政安民<br/>太建北伐收淮南，后期奢靡"]:::emperor

    ChenDaoTan --> ChenXu

    %% 第三代 - 陈叔宝（陈顼之子）
    ChenShuBao["<b>(五) 后主 陈叔宝</b><br/>在位: 582—589 (7年)<br/>享年: 51岁 (553-604)<br/>陈顼长子<br/>至德、明年间<br/>耽于酒色，宠信佞臣<br/>隋军南下灭陈，被俘入隋<br/>终老洛阳，南朝终结"]:::deposed

    ChenXu --> ChenShuBao

    %% 布局说明
    %% 传承线：陈霸先 → 陈蒨(侄) → 陈伯宗(子) → 陈顼(叔父废侄) → 陈叔宝(子)
```