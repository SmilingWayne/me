# Chat GPT - Prompt/LLama2 and so on

!!! warning ""
    2025.09.28 本部分的内容会尽快迁移至人工智能模块，目测会大范围修改并删减现有内容。

> reference：[Llama 2 yyds!](https://ai.meta.com/llama/get-started/)

!!! info "prompt是什么"
    
    prompt：提示工程，是自然语言处理 （NLP） 中使用的一种技术，通过为语言模型提供有关手头任务的更多上下文和信息来提高语言模型的性能。通过创建提示（提示是为模型提供附加信息或指导的简短文本），例如它将生成的文本的主题或体裁。通过使用提示，模型可以更好地了解预期的输出类型，并生成更准确和相关的结果。

    - 一些Llama 2 官方给出的prompt技巧：
        - Be clear and concise ：简洁明了：提示应易于理解，并为模型提供足够的信息以生成相关输出。避免使用可能混淆模型的行话或技术术语。
        - Use specific examples ：使用特定示例：在提示中提供特定示例可以帮助模型更好地了解预期的输出类型。例如，如果希望模型生成有关特定主题的故事，请包含有关设置、人物和情节的几句话。
        - Vary the prompts: 改变提示：使用不同的提示可以帮助模型更多地了解手头的任务，并产生更多样化和创造性的输出。尝试使用不同的样式、色调和格式，看看模型如何响应。
        - Test and refine： 测试和优化：创建一组提示后，在模型上测试它们以查看其性能。如果结果与预期不符，请尝试通过添加更多细节或调整语气和样式来优化提示。
        - Use feedback: 使用反馈：最后，使用来自用户或其他来源的反馈来不断改进提示。这可以帮助您确定模型需要更多指导的领域，并做出相应的调整。
        - Role Based Prompts：根据所处理的个人或实体的角色或观点创建提示。此技术可用于从语言模型生成更相关且更具吸引力的响应。

        > e.g. You are a virtual tour guide currently walking the tourists Eiffel Tower on a night tour. Describe Eiffel Tower to your audience that covers its history, number of people visiting each year, amount of time it takes to do a full tour and why do so many people visit this place each year.
        
        - **Chain of Thought Technique**: 涉及为语言模型提供一系列提示或问题，以帮助指导其思维并生成更连贯和相关的响应。此技术可用于从语言模型生成更深思熟虑和更合理的响应。
        
        > e.g. You are a virtual tour guide from 1901. You have tourists visiting Eiffel Tower. Describe Eiffel Tower to your audience. Begin with: 1. Why it was built; 2. Then by how long it took them to build; 3. Where were the materials sourced to build; 4. Number of people it took to build; 5. End it with the number of people visiting the Eiffel tour annually in the 1900's, the amount of time it completes a full tour and why so many people visit this place each year. Make your tour funny by including 1 or 2 funny jokes at the end of the tour.

!!! info "什么是LLM的幻觉（Hallucinations）"
    - **要求语言模型生成对有关它尚未训练的主题的问题的响应**.语言模型可能会产生幻觉信息或编造不准确或没有证据支持的事实。（修复：若要解决此问题，可以为语言模型提供有关主题的更多上下文或信息，以帮助它理解所询问的内容并生成更准确的响应。还可以要求语言模型为其提出的任何声明提供来源或证据，以确保其响应基于事实信息）
    - **要求语言模型生成对需要特定视角或观点的问题的响应。**，语言模型可能会产生幻觉信息或编造与所需观点或观点不一致的事实。（若要解决此问题，可以向语言模型提供有关所需视角或观点的其他信息，例如所针对的个人或实体的目标、价值观或信念。这可以帮助语言模型理解上下文，并生成更符合所需视角或观点的响应。）



--------------

> 以下内容创作自2023.4


## 宗旨



- [https://learningprompt.wiki/docs](https://learningprompt.wiki/docs)：一个prompt指南。最近OpenAI又和Andrew Ng出了一个Prompt的教程，口碑还可以。

### **<font color = Crisma>尽可能地给背景信息、具体需求</font>**

- 如果不给定背景、不限制语境，ChatGPT有时候会发疯乱说，或者完全不回答你想要的，此时**可以补上相关信息**；

<figure markdown>

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202310251052121.png)

</figure>

- **对于给定主题的思想汇报、有背景信息的总结报告效果奇佳**。下面这个“老山精神”的思想汇报，一开始它完全是瞎说，但是你补充了信息之后，他可以做得更好；

<figure markdown>

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202310251052398.png)


</figure>

- 再补充，它一下子学会了，而且改得很快，动动手指就可以效率翻倍：

<figure markdown>

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202310251052399.png)

</figure>


### **<font color = Crisma>成为一个大胆且合格的甲方</font>**



- 把自己的需求尽可能详细地写出来，比如翻译时候，可以补充：“括号内请不要翻译”，然后补充一个例子：





<figure markdown>

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202310251053237.png)

</figure>

- 尽可能地把它的回答限制在你想要的“格式”，比如：你只需要回复一个词；只用一句话表达...


<figure markdown>

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202310251053238.png)

</figure>

### **<font color = Crisma>一步一步来，多交流，逼它改进</font>**


- 这个细节是wb上宝玉老师和木遥老师提到过的，就是，如果你单纯地问它一个数学问题，他可能会犯很低级的错误，他的记忆力甚至会短到难以置信（比如让他统计有多少个数字符合条件，它会很蠢地少算一个）。但是如果你让他“再仔细做一次，按照步骤一步步地完成操作”，那么它很快又会发现自己的错误。
- 启示是如果我们希望它按照一定思路做一个事情，**那么把这个解决问题的过程、思路展示给他**，或者在交流中及时给他灌输我们想要它做的**具体的**步骤，往往更可能得到想要的结果。

- 下面是一个玩（tiao）弄（jiao）ChatGPT的实例：

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202310251053239.png)
![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202310251053240.png)

<figure markdown>

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202310251053241.png)

</figure>