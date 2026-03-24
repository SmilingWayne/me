# Skills: format-markdown: mkdocs 格式美化 + 自动总结

## 背景与起因

这是一个我自用的 Claude Code 小 Skills。首先依然是说一下为什么要做这个。

我日常在网站发布笔记，流程如下：

写成 markdown 文件 -> mkdocs （框架） -> material （风格） -> github workflow/ pages （CICD，部署发布）。

理论上，只要做一些和 mkdocs 框架与 mkdocs materials 相适配的格式调整，即可发布到我的网站上了。但是，mkdocs material 支持一些特殊且好用的markdown语法，并且有些地方的规则与默认markdown稍有不同。试举几例：

1) ==段落公式必须与前后段之间空行，否则会渲染出错，同时段落公式内不允许在开头结尾有冗余的空行==，i.e., 对于如下若干格式，只有最后一种能被正确渲染：

=== "Case. 1(❌)"

    ```markdown
    这是我的第一行。
    $$E = mc^2$$
    这是我的第二行。
    ```

=== "Case. 2(❌)"

    ```markdown
    这是我的第三行。
    \[E = mc^2\]
    这是我的第四行。
    ```

=== "Case. 3(❌)"

    ```markdown
    这是我的第三行。

    \[
        
        E = mc^2

    \]

    这是我的第四行。

    ```

=== "Case. 4(✅)"
    ```markdown
    这是我的第五行（⬇️终于正确版）。

    \[E = mc^2\]

    这是我的第四行（⬆️终于正确版）。
    ```

上述代码实际渲染效果如下：

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202603241508627.png)


2) <span style="color:red;font-weight:bold">对于列表、有序列表、表格，必须与前后段落之间保持空行，否则渲染会黏连在一起。</span>

=== "Case. 1(❌)"

    ```markdown
    这是列表前的第一句话。
    - 这是第一点。
    - 这是第二点。
    - 这是第三点。
    这是列表后的第一句话。

    ```

=== "Case. 2(❌)"

    ```markdown
    这是列表前的第一句话。
    * 这是第一点。
    * 这是第二点。
    * 这是第三点。
    这是列表后的第一句话。

    ```

=== "Case. 3(✅)"

    ```markdown
    这是列表前的第一句话。

    - 这是第一点。
    - 这是第二点。
    - 这是第三点。

    这是列表后的第一句话。

    ```

=== "Case. 4(❌)"
    ```markdown
    这是表格前的第一句话。
    | Col1  | Col2  |
    | :---: | :---: |
    | (1,1) | (1,2) |
    | (2,1) | (2,2) |
    | (3,1) | (3,2) |

    这是表格后的第一句话。

    ```

=== "Case. 5(✅)"
    ```markdown
    这是表格前的第一句话。
    
    | Col1  | Col2  |
    | :---: | :---: |
    | (1,1) | (1,2) |
    | (2,1) | (2,2) |
    | (3,1) | (3,2) |

    这是表格后的第一句话。

    ```

上述代码实际渲染效果如下：

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202603241523761.png)


3) 此外，mkdocs material 有一些高度定制化的语法，比如 Admonition，header 与正文之间需要有 4-indent 的缩进。

```markdown

!!! note "This is header."
    This is contents.

```


我发现从各个地方复制过来的 markdown 文本、以前写过的笔记，往往会在很多不经意的角落里，违背这几个准则。我一开始以为可以通过 mkdocs material 的某些默认配置，实现对这几种情况的兼容，但是查阅资料并没有找到证据。同时，上述写法在官方的文档中也是首先采用的。

一方面，**这种格式的修改很让我头疼。考虑到一个300～400行的精修笔记可能有几十处公式，十余处表格，手动进行调整让我觉得效率低下**。

另一方面，这个小问题的存在导致 markdown 的直接可交付性被极大削弱了。我不喜欢这种高度不确定性。


我希望我的Skills能自动把一些内容整理成这个格式的样子，不出格式错误。


## 实现

在实现过程中，深度参考了宝玉老师的 [baoyu-format-markdown](https://github.com/JimLiu/baoyu-skills/tree/main/skills/baoyu-format-markdown)，基础框架只做了一些微调，保留了文章总结功能，剔除更换了 js 脚本：

- 在我的实现中，==会有一个脚本自动提取markdown文件的 AST（抽象语法树）==，这样我可以灵活地检索控制具体的代码块所属的类别（表格、bullet point、公式），然后对于不符合条件的格式进行前后添加空行等操作；
- **严格保证文本一致性**。除了调整格式之外，不对原文做任何操作；
- 流程参数化，可以选择：
    - 是否进行总结
    - 是否运行脚本
    - 单独运行脚本不做其他

这是一个小 Skill，目的是对我计划发布到网站的 .md 文件进行最后一次处理，对格式进行严格的微调以适应渲染的要求，最终会返回我修改的结果。

---

## 结果

放一组输出的markdown文件及渲染结果。图中所有内容均未经过人工调整。

=== "Before (表格渲染错误，公式缩成行内)"
    
    ![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202603241552754.png)

=== "After (理想的干净形式)"

    ![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202603241552718.png)




以及：

=== "Before (表格渲染错误，公式缩成行内)"
    ![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202603241555726.png)

=== "After (理想的干净形式)"

    ![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202603241555800.png)


还有：

=== "Before (表格渲染错误，公式缩成行内)"
    
    ![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202603241601092.png)

=== "After (理想的干净形式)"

    ![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202603241601848.png)


运行中间会自动生成中间文件、生成分析文件和备份。目录如下：

```shell
./docs/Study/Statistics
├── AdvancedStatistics
│   └── class1.md
├── example-analysis.md.     # analysis 
├── example.md               # original
├── example_formatted.md     # final
└── example_formatted.md.backup-2026-03-24T07-47-38.md # backup 
```

最终会输出一份调整报告：

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202603241558396.png)

---


## 使用

可以在 ClawHub 的[这个🔗](https://clawhub.ai/smilingwayne/format-markdown) 使用。

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202603241604625.png)