# 我用过的一些Prompt

提示：代码块是可以直接在右侧最上角复制的。

## 论文篇

### 学术写作篇

> [参考链接（其一）](https://mp.weixin.qq.com/s/ppszMUR6TvW_mmpQg4UQCA)

```
I'm writing a paper on [topic] for a leading [discipline] academic journal. What I tried to say in the following section is [specific point]. Please rephrase it for clarity, coherence and conciseness, ensuring each paragraph flows into the next. Remove jargon. Use a professional tone.
```

```
If something doesn't quite hit the mark, don't hesitate to say, "This isn't quite what I meant. Let's adjust this part." Or you can commend its improvements: "This is much clearer, but let's tweak the ending for a stronger transition to the next section."
```

### 论文阅读篇

```
Assume you're an expert and seasoned scholar with 20 years of academic experience in [field]. On the basis of my summary of a paper in [field], where the main focus is on [general topic], provide a detailed review of this paper, in the following order: 

1) briefly discuss its core content; 

2) identify its limitations; and 

3) explain the significance of each limitation in order of importance. Maintain a concise and professional tone throughout.
```


中文：

请以[领域]内具有20年研究经验的资深学者视角，基于我对这篇关于[主题]论文的总结，按以下顺序提供详细评审：

1）简要分析核心内容；

2）指出研究局限；

3）按重要性依次说明各项局限的学术影响。请始终保持简洁专业的语气。


### 回复审稿人特供版


```
On the basis of these notes, draft a letter to the author. Highlight the manuscript's key issues and clearly explain why the manuscript, despite its interesting topic, might not provide a substantial enough advancement to merit publication. Avoid jargon. Be direct. Maintain a professional and respectful tone throughout.
```

---


## 翻译篇

> 如果你发现AI写得比较生硬，可能是因为你特意制定了它“翻译”这个工作。此时换个说法或许会有不同：

### 有具体的主题了，需要强调专有名词时

```
这是一篇{topic}相关文章，主要研究了如何量化模型的蒸馏程度，其中 LLM 表示“大语言模型”，Model Distillation表示模型蒸馏，英文人名保持不变，现在请尊重原意的前提下，保持原有格式不变，用中文重写<text></text>中的内容。
```


---

### 没有具体主题，只是翻译

```
请你用简体中文（白话文）重新表述原文，尽可能保持原有风格，避免使用AI中文，保持简洁、灵活、准确、通顺、符合逻辑。我会把需要翻译的内容放在 <text></text> 内。

## AI中文改进要点

避免英语化

*   抽象名词：减少使用，多用动词或具体描述。
    *   例：不说“收入的减少”，说“收入减少”。
*   主语/宾语：少用抽象名词/词组做主语或宾语，多用事情或短句。
    *   例：不说“书籍的选购”，说“选购书籍”。
*   弱动词+抽象名词：少用“作出”、“进行”等，多用直接动词。
    *   例：不说“作出贡献”，说“贡献”。
*   被动语态：尽量用主动语态，避免生硬的“被”字。
    *   例：不说“被接受”，说“大家接受”。

活用

*   成语：适当运用，避免滥用或完全不用。
*   连接词：少用“和”、“与”、“及”、“以及”，活用“而”、“并”、“且”。
*   介词：避免滥用“中间”、“有关”、“关于”、“由于”等，精简表达。
*   副词：避免将动词加“地”转为副词，灵活运用逗号。
    *   例：不说“苦心孤诣地”，说“苦心孤诣，”。
*   形容词：减少“的”字，灵活运用词语搭配。
    *   例：不说“白色的鸭”，说“白鸭”。
*   后饰：灵活运用后置修饰，避免长句堆砌在前。
    *   例：不说“一个长得像你兄弟的陌生男人”，说“一个陌生男人，长得像你兄弟”。

避免冗余

*   伪术语：避免“知名度”、“可读性”等，直接表达。
*   “们”字：名词已表复数，避免多余的“们”字。
    *   例：不说“听众们”，说“听众”。
*   “之一”：避免滥用“之一”，考虑其他表达方式。
    *   例：不说“名著之一”，说“名著”。
*   “其中之一”：避免“其中之一”叠加“之一”，考虑其他表达方式。
*   “最...之一”：避免使用，改用其他更精炼的表达方式。


<text></text>
```