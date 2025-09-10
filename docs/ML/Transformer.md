# Transformer

ML：不要在代码中明确定义如何执行一个任务，而是去构建一个具有可调参数的灵活架构，就像旋钮一样，然后用大量实例告诉它给定一个输入的时候应该输出什么，设法调整各种参数值来模拟这种行为。

最简单的ML的例子就是线性回归，当然你只需要拟合两个参数，斜率和常项，GPT-3就需要**拟合1750亿个参数。**

但是并不只是直接扩大参数量，而是说需要用灵活的方法进行训练：**反向传播（Back- propagation）**

为了这种训练算法的有效运行，模型必须遵循某种特定结构。

## Token

某个单词/单词的一部分，或者符号标点。我们首先有一个很大的词库，比如 50k 个token。我们引入第一个Matrix: Embedding Matrix。每一个词（Token）都对应一列，**这些列决定了第一步中，每个单词对应的向量。我们记为 $W_E$** 。这个矩阵的取值一开始是随机的，但是会基于数据进行学习。词嵌入的过程：用一个方向来编码语义信息等。以GPT-3为例，每个Token 有 12288 个维度，50257个Token。也就是 6.17 亿个参数。


对于Transformer而言，我们不仅能够直接得到Embedding中每个单词的向量，**还需要编码单词的位置信息，更重要的是，这些向量能够结合上下文语境。** 也就是被输入的语句中的其他Token反复拉扯，进而得到下一个词。事实上，为了预测下一个词，这句话的语义、语境，可能受到来自很远位置的文本影响，有时候甚至很远。而我们根据输入文本创建向量组，看看下一个Token是什么的时候，每个向量都是直接从Embedding矩阵中拉出来的。一开始，每个向量都仅仅表示其自身的意思，而不表示语境信息。但是流经了这个网络后，向量就获得了比单个词更加丰富具体的含义。

GPT-3只能处理一定上下文的内容，也就是“上下文长度”，是2048个Token。因此，流经网络的数据有2048列，每列12288维。这相当于限制了，GPT-3预测下一个词是什么的时候，能够结合的文本量。


此时我们看一下模型的输出是什么，稍后来讲Attention。**我们的目标是，输出下一个可能的 Token 的概率分布。**

这需要有2个步骤。首先，我们需要用一个矩阵，将最后一个字的向量（12288维），映射到我们的词表（50267个Token）中去， $\mathbf{Ax}$ 这样，得到的向量 (50257)就代表了词库里一个Token的**值**，我们把这个值再走一遍softmax。

这个矩阵，就是 $W_U$。它具有和Embedding类似的维度，只不过行列对调，也就是行数等于Token数(50k)，列数等于每个Token的维度(12288)。这就是 6.17亿个参数。


!!! note "Softmax"
    **目的是把任何数列转化成合理的概率分布。** 使得最大值接近1，而最小值接近0. $\dfrac{e^{x_1} }{\sum^{N-1}_{n = 0}e^{x_n}}$。
    
    有时候我们会加入一个T，$\dfrac{e^{x_1 / T} }{\sum^{N-1}_{n = 0}e^{x_n / T}}$ 这样，当T较大的时候，低值会被赋予更大的权重，使得分布更加均匀一些。如果T更小，那么较大的值会更占优势。 

通过 $W_U$ 矩阵，我们得到的没有归一化 (softmax) 的每个Token的值，称为 这个词的 Logits.



---

!!! question "为什么需要位置编码"

    核心原因：Transformer的自注意力机制在计算时，对输入序列的顺序不敏感，它将输入看作一个无序的集合。如果不引入位置信息，模型将无法区分词语的先后关系，这对于理解自然语言是致命的。

    解决方案：位置编码就是为了解决这个问题。它通过创建一个与位置相关的向量，并将其叠加到词嵌入向量上，使得模型在处理输入时，既包含了词的语义信息，也包含了词的位置信息。

    实现方法：

    - 经典的方法是正弦/余弦位置编码，它的优点是无需训练，并且其数学特性使得模型很容易学习到相对位置关系，同时具备一定的外推能力。
    - 另一种常见方法是可学习的位置编码，像BERT就是这么做的，它让模型自己学习位置表示，但外推能力较差。
    - 目前更先进的方法，如旋转位置编码（RoPE），在Llama等模型中使用，它通过旋转Q、K向量的方式优雅地集成了相对位置信息，效果非常出色。


!!! question "LoRA是什么作用"

!!! question "RAG的作用，SFT的作用"
    STF 是什么数据？

归一化的作用是什么？为什么要用LayerNorm而不是BatchNorm？这两者的区别是什么？

bert 和大模型的区别是什么？怎么对梯度消失做的优化？层数、维度是多少？


!!! question "什么是 KV-cache？"
    它是什么：KV Cache 是一种针对 Transformer 模型在**自回归推理（如文本生成）时的关键优化技术**。

    目的：解决在生成每一个新 token 时，对历史序列进行大量重复计算的问题，从而大幅提升推理速度。

    **工作原理**：它通过缓存（存储）已经计算过的所有 token 的“键（Key）”和“值（Value）”向量。在生成下一个 token 时，模型只需要为当前这一个新 token 计算 Q, K, V，然后从缓存中读取历史 K, V，拼接后进行注意力计算。

    > 这就是自注意力机制（Self-Attention）的核心。在自回归生成第 $t$ 个 token 时，这个新 token 的 Query 向量（$Q_t$）必须与从第 1 个到第 $t$ 个所有 token 的 Key 向量（$K_1, K_2, ..., K_t$）进行点积，来计算注意力权重。这就是“看到前面的所有上下文”的数学体现。

    **效果与权衡**：

    巨大收益：将生成长序列的计算复杂度从近似三次⽅降为二次方，极大地加快了生成速度，使大模型能够进行流畅的对话和长文生成。
    主要代价：占用大量的显存来存储这些 K, V 向量。因此，在实际应用中，模型的最大上下文长度往往受限于 KV Cache 所占用的显存大小。

!!! question "生成式大模型 的推理"
    这是一个非常好的问题，它触及了不同 Transformer 架构在推理时的核心差异。你的问题直接关联到模型的两大类别：Encoder-Only 和 Encoder-Decoder。

    答案是：**这取决于你谈论的是哪种类型的 Transformer 模型。**

    我们来分别讨论这两种主流架构：

    - 1. Decoder-Only 架构（例如：GPT系列、Llama系列、BLOOM）

    这是目前大语言模型（LLM）最主流的架构，我们刚才讨论的自回归生成、KV Cache 等都主要发生在这种模型上。

    *   **推理时用到哪些部分？**
        *   **只用到 Decoder 部分。** 顾名思义，这种模型根本没有 Encoder。
    *   **会用到交叉注意力吗？**
        *   **不会。** 因为交叉注意力（Cross-Attention）的定义是：一个部分的 Query（通常来自 Decoder）关注另一个部分的 Key 和 Value（通常来自 Encoder）。既然没有 Encoder，自然也就不存在交叉注意力。
        *   在这种架构里，Decoder 模块中的“交叉注意力”层被一个标准的“自注意力”（Self-Attention）层所替代。所以，一个典型的 Decoder-Only 模型的 Decoder Block 包含两个核心部分：
            1.  **带掩码的自注意力 (Masked Self-Attention)**: 用于处理和生成文本。
            2.  **前馈网络 (Feed-Forward Network)**: 用于信息加工。

    **小结：对于 GPT 这类 Decoder-Only 模型，推理过程就是我们前面详细描述的自回归生成，它只涉及 Decoder 自身，并且只使用自注意力机制。**

    - 2. Encoder-Decoder 架构（例如：原始 Transformer、T5、BART）

    这类模型常用于需要“转换”的任务，比如机器翻译（一种语言 -> 另一种语言）、文本摘要（长文章 -> 短摘要）。

    *   **推理时用到哪些部分？**
        *   **Encoder 和 Decoder 都会用到。**
    *   **会用到交叉注意力吗？**
        *   **会，而且这是关键步骤！**

    它的推理过程比 Decoder-Only 模型要复杂一些，分为两个主要阶段：

    **阶段一：编码输入序列 (Encoder Pass)**

    1.  **输入**: 将源序列（Source Sequence），比如要翻译的德语句子 "Ich bin ein Berliner"，完整地输入到 **Encoder** 中。
    2.  **计算**: Encoder 并行地处理整个德语序列，通过多层的自注意力机制，最终为输入序列的每个 token 生成一个富含上下文信息的表示（representation）。我们称这组最终输出的向量为 `memory` 或 `encoder_hidden_states`。
    3.  **产出**: 这一整套 `memory` 向量。**请注意：这个 `memory` 在整个后续的解码过程中是固定不变的，可以被看作是一个只读的知识库。**

    **阶段二：自回归解码 (Decoder Pass)**

    现在，Decoder 开始一个词一个词地生成目标序列（比如英语句子）。这个过程和 GPT 的自回归很像，但多了一个关键步骤：

    4.  **起始**: Decoder 从一个特殊的起始符 `[BOS]` (Begin of Sentence) 开始。
    5.  **循环生成**:
        *   **a. 带掩码的自注意力**: Decoder 首先对自己已经生成的部分进行自注意力计算。比如生成到第三个词时，它会回顾 `[BOS]` 和前两个已生成的词。这一步和 GPT 完全一样。
        *   **b. 交叉注意力 (Cross-Attention)**: **这是核心区别！** 在上一步自注意力的输出之上，Decoder 会执行一个交叉注意力操作。
            *   **Query**: 来自 Decoder 刚刚经过自注意力处理后的向量。
            *   **Key 和 Value**: 来自**阶段一 Encoder 输出的那套固定的 `memory` 向量**。
            *   **作用**: 这一步是让 Decoder 在决定下一个要生成的词时，去“查阅”和“关注”整个德语输入句子的信息。比如，当它要生成 "I" 时，交叉注意力可能会让它高度关注德语输入中的 "Ich"。
        *   **c. 前馈网络**: 经过交叉注意力的结果会被送入前馈网络进行加工。
        *   **d. 预测与采样**: 最终预测出下一个词的概率分布，并采样得到新词（比如 "am"）。
        *   **e. 迭代**: 将新生成的 "am" 加入到 Decoder 的已知序列中，开始下一轮循环，去生成 "a"。

    **总结一下 Encoder-Decoder 模型的推理：**

    | 模块             | 作用                                         | 何时运行                    |
    | :--------------- | :------------------------------------------- | :-------------------------- |
    | **Encoder**      | 将整个源序列编码成一组固定的 `memory` 向量。 | **只在最开始运行一次。**    |
    | **Decoder**      | 在一个自回归循环中生成目标序列。             | 在每个 token 生成时都运行。 |
    | ↳ **自注意力**   | 让 Decoder 回顾自己已经生成的内容。          | 在每个生成步骤中运行。      |
    | ↳ **交叉注意力** | 让 Decoder 查阅和参考 Encoder 的 `memory`。  | 在每个生成步骤中运行。      |
    | ↳ **前馈网络**   | 信息处理。                                   | 在每个生成步骤中运行。      |

    **面试回答精炼版：**

    面试官您好，关于推理阶段是否用到 Encoder、Decoder 和交叉注意力，这取决于模型的具体架构：

    6.  **对于 GPT、Llama 这类 Decoder-Only 模型**：它们没有 Encoder，因此推理时只使用 Decoder 部分。生成过程是纯粹的自回归，只涉及到“自注意力”，完全**不会**用到交叉注意力。

    7.  **对于原始 Transformer、T5、BART 这类 Encoder-Decoder 模型**，通常用于翻译或摘要任务：
        *   **Encoder 和 Decoder 都会用到。** Encoder 在推理开始时运行一次，将输入句子编码成一个固定的 `memory`。
        *   Decoder 在一个自回归循环中逐词生成输出。在每一步，它都会用到**交叉注意力**机制，其 Query 来自 Decoder 自身，而 Key 和 Value 则始终来自于 Encoder 产生的那个固定 `memory`。这允许 Decoder 在生成每个词时都能参考完整的输入信息。

!!! note "为什么现在大多是 decoder-only 结构？"
    

    - 问题：为什么现在的大模型大多是 Decoder-Only 结构，而非经典的 Encoder-Decoder 结构？这种结构的优势是什么？原先结构又有哪些劣势？



    - 根本原因：任务范式的统一

    *   **传统 Encoder-Decoder 范式**：它的设计天生就是为了**“序列到序列”（Seq2Seq）**任务，比如翻译（德语 -> 英语）、摘要（长文 -> 短文）。它有一个明确的、分离的“源输入”（Source）和“目标输出”（Target）。这种结构在处理这类“转换”任务时非常强大和直观。
    *   **现代 LLM (Decoder-Only) 范式**：现代大模型的目标是成为一个**通用的语言接口**，能够处理包括但不限于问答、对话、写作、代码生成、思维链推理等无数种任务。这些任务很多都不是严格的 Seq2Seq 格式。

    Decoder-Only 架构通过一个极其简单而强大的范式统一了所有任务：**文本补全（Text Completion）** 或者说 **下一个词预测（Next Token Prediction）**。

    *   **问答**: `Q: 什么是引力波？ A:` -> 模型补全答案。
    *   **翻译**: `Translate German to English: Ich bin ein Berliner =>` -> 模型补全 "I am a Berliner."
    *   **写代码**: `// Python function to calculate fibonacci\ndef fib(n):` -> 模型补全代码实现。
    *   **对话**: `User: 今天天气怎么样？\nAssistant:` -> 模型补全回答。

    你看，所有不同的任务都被巧妙地转换成了一个“根据前文预测后文”的统一形式。Decoder-Only 结构正是为这个单一目标而生的，它天生就擅长做“续写”。

    - 1. Decoder-Only 结构的优势

    基于上述的范式统一，Decoder-Only 架构展现出几大优势：

    1.  **架构简单与高效扩展（Simplicity & Scalability）**:
        *   它只有一个模块（Decoder），结构更统一，实现和维护起来更简单。
        *   在训练时，所有参数都为一个统一的“预测下一个词”的目标服务，训练过程更稳定、更直接。
        *   这种简单性使得它非常容易进行规模化扩展。当我们把模型从几十亿扩展到几千亿甚至万亿参数时，一个简单、统一的架构是至关重要的。这正是“大力出奇迹”（涌现能力）的基础。

    2.  **为“上下文学习”（In-Context Learning）而生**:
        *   这是最核心的优势。Decoder-Only 模型在预测每一个新词时，都会回顾并关注从开头到当前位置的所有上文。这意味着整个提示（Prompt）和已经生成的内容构成了一个动态的、不断增长的上下文。
        *   模型学会了从这个上下文中“即时学习”和“领会意图”。你给它几个例子（Few-shot prompting），它就能模仿这个模式；你给它一条指令，它就能理解并执行。这种能力是现代 LLM 如此强大的关键，而 Decoder-Only 的结构天然地支持了这一点。

    3.  **极佳的生成流畅性**:
        *   因为它的训练目标和生成方式完全一致（都是自回归地预测下一个词），所以它在生成长篇、连贯、流畅的文本方面表现得非常自然。

    - 3. Encoder-Decoder 结构的劣势（在通用 LLM 场景下）

    反过来看，在追求通用模型的背景下，Encoder-Decoder 结构的劣势就显现出来了：

    1.  **信息瓶颈（Information Bottleneck）与僵化**:
        *   Encoder 将所有源输入信息压缩成一组固定的 `memory` 向量。尽管 Decoder 可以通过交叉注意力反复查询这个 `memory`，但这个 `memory` 本身是**一次性生成、静态不变的**。
        *   相比之下，Decoder-Only 模型在生成每个新词时，它的“上下文”是动态增长的，包含了之前生成的所有内容。这使得它的“世界观”是不断更新的，更加灵活。

    2.  **架构复杂与训练低效**:
        *   需要维护和训练两个不同的模块（Encoder 和 Decoder），参数分配和训练动态都更复杂。
        *   交叉注意力的引入也增加了计算的复杂性。对于一个统一的、超大规模的模型来说，这种复杂性会成为扩展的阻碍。

    3.  **不适用于开放式生成与对话**:
        *   对于没有明确“源输入”的开放式生成任务（比如“写一首关于春天的诗”）或多轮对话，Encoder-Decoder 显得很“笨拙”。我们必须人为地将历史对话或任务指令塞进 Encoder，这远不如 Decoder-Only 模型直接续写来得自然和高效。

    ----

    **简单来说，Encoder-Decoder 模型像是一个专业的“翻译机”或“摘要机”。你给它一个输入，它给你一个精心转换的输出。它非常擅长做特定的“转换”任务。**

    **而 Decoder-Only 大模型则更像一个拥有海量知识、并且精通“阅读理解和模仿续写”的“通才大脑”。你给它任何形式的文本作为开头发动它，它都能理解你的意图，并接着你的话往下说。**

    随着算力的爆炸式增长，人们发现，把这个“通才大脑”做得足够大，它在完成特定任务时，其效果可以媲美甚至超越那些“专才”模型，同时还具备了前所未有的通用性和灵活性。因此，Decoder-Only 架构成为了通往通用人工智能（AGI）道路上，目前被验证为更优越和更有潜力的选择。

!!! note "MMoE"
    当然，混合专家架构（Mixture of Experts, MoE）是当前大模型领域最前沿、最重要的技术之一，尤其在像 Mixtral-8x7B 和 GPT-4（据推测）这样的顶级模型中得到了应用。理解它对于算法岗面试至关重要。


    **MoE 的核心思路是“用一组专家网络替换模型中的部分全连接网络（FFN），并让一个路由网络（Router）来决定每个输入（Token）应该由哪个或哪些专家来处理”。**

    这是一种典型的**“分治”**思想。你可以把它想象成一个大型医院的会诊系统：

    *   **传统模型 (Dense Model)**：就像一个“全科医生”。无论你是什么病（感冒、骨折、心脏病），你都只能找这一个医生。他什么都懂一点，但对复杂病症可能不够精通。计算开销很大，因为他每次都要调动全部的知识储备来给你看病。
    *   **MoE 模型**: 就像一个拥有“分诊台”和“多个专科医生”的医院。
        *   **专科医生 (Experts)**：每个医生都是一个独立的前馈网络（FFN），他们分别擅长处理不同类型的信息（比如一个擅长语法，一个擅长事实知识，一个擅长代码逻辑）。
        *   **分诊台 (Gating Network / Router)**：这是一个小型的神经网络。你（一个 Token）来到医院后，分诊台护士会看你的情况（Token 的内容），然后决定把你**动态地**分配给最相关的一两个专科医生。
        *   **会诊**: 你被送到选定的几个专科医生那里，他们分别给出诊断意见。最后，分诊台会根据之前对你病情的判断，将这几个专家的意见加权汇总，形成最终的诊断报告（Token 的最终输出）。



    **在训练和推理两侧都会发挥作用，但侧重点和效果不同。**

    1.  **训练阶段**:
        *   **作用**: MoE 的主要作用是**在保持计算成本（FLOPs）基本不变的情况下，极大地扩展模型的总参数量**。
        *   **解释**: 假设一个 dense 模型的 FFN 层有 10B 参数。现在我们用一个 MoE 层替换它，这个 MoE 层包含8个专家，每个专家还是 10B 参数，总参数量就变成了 80B。但在训练时，对于每个 token，路由器只会激活其中的2个专家（Top-2路由）。这意味着这个 token 的计算量只相当于通过了 20B 参数的 FFN，而不是 80B。
        *   **结果**: 我们可以用几乎相同的训练时间和硬件成本，训练出一个总参数量大得多的模型。
        *   ==在训练时，对于每一个 token，模型并不是激活一个大 FFN 里的“部分神经元”，而是从多个独立的 FFN（专家）中，完整地激活一两个来进行计算。不同的 token 可能会被路由到不同的专家组合，这就是所谓的“动态稀疏性”==。

    2.  **推理阶段**:
        *   **作用**: MoE 的主要作用是**显著提升推理速度**。
        *   **解释**: 和训练时一样，在推理时，每个 token 也只会被发送到少数几个被激活的专家那里进行计算。模型虽然总参数量巨大（例如 Mixtral-8x7B 有约47B总参数），但每个 token 推理时实际动用的“活跃参数”只有约13B。
        *   **结果**: 推理速度与一个小的、同等活跃参数量的“稠密模型”相当，但性能却受益于其巨大的总参数量。

    - 有什么效果？解决了什么业界问题呢？

    MoE 主要解决了大模型发展中遇到的一个核心矛盾：**性能与成本的“不可能三角”**。

    **业界问题（Scaling Law 的诅咒）**:
    根据大模型的缩放定律（Scaling Laws），模型的性能（如理解、推理能力）与模型的参数量和训练数据量正相关。简单来说，“越大越好”。但是，无限制地增大**稠密模型（Dense Model）**的规模会遇到瓶颈：
    3.  **训练成本过高**: 训练一个万亿参数的稠密模型需要海量的计算资源和时间，成本高到难以承受。
    4.  **推理成本过高**: 即使训练出来了，让一个万亿参数的稠密模型进行推理，速度会非常慢，延迟极高，无法实际部署应用。

    **MoE 的解决方案和效果**:
    MoE 通过**“稀疏激活”（Sparse Activation）**的方式，优雅地绕开了这个难题。

    5.  **效果一：突破性能瓶颈**
        它允许模型在**可控的计算预算**内，将总参数量提升一个甚至多个数量级。更大的参数量意味着更大的模型容量，可以存储更丰富的知识，从而获得更强的“涌现能力”和性能。

    6.  **效果二：实现高效推理**
        它让拥有巨大参数量的模型能够以远小于其总规模的计算量进行服务。这就是为什么 Mixtral-8x7B（47B总参数）的推理速度和 Llama 2 13B 差不多，但效果却能媲美 Llama 2 70B。**它用更小的推理成本，实现了更强的模型性能。**

    ---

    我对混合专家（MoE）架构的理解如下：

    7.  **核心思想**：MoE 是一种“分治”策略，它用多个专精于不同领域的“专家网络”（独立的FFN）和一个“路由网络”来替换传统模型中的部分全连接层。当一个 token 输入时，路由网络会动态地选择激活少数几个最相关的专家来处理它。

    8.  **解决的问题**：它主要解决了大模型 Scaling Law 下的“性能-成本”矛盾。传统稠密模型越大性能越好，但训练和推理成本会急剧上升，难以承受。

    9.  **带来的效果**：
        *   **训练时**：它可以在**计算成本（FLOPs）基本不变**的情况下，将模型的总参数量提升数倍，从而让模型拥有更大的容量和潜力。
        *   **推理时**：它通过“稀疏激活”（每个 token 只使用一小部分参数）的方式，使得一个巨大参数量的模型，能够以一个小的稠密模型的速度来进行推理，实现了**“低成本，高性能”**。

    总而言之，MoE 是当前实现超大规模模型、并使其具备实用性的一项关键和前沿的技术。
    
    ---


    > 大模型怎么知道该激活哪几个专家呢？尤其是训练的时候？还是说，路由网络的参数也是训练的一部分？

    **你的直觉完全正确：路由网络（Gating Network / Router）的参数本身就是模型的一部分，它需要和所有专家以及模型的其他部分一起被训练。**


    路由网络本身通常是一个非常简单的神经网络，通常就是一个**线性层**。它的训练过程大致如下：

    10. **输入**: 对于任意一个 token `x`（它已经过前面的注意力层处理），路由网络接收 `x`作为输入。

    11. **计算“亲和度”分数**: 路由网络内部有一个可训练的权重矩阵 `W_g`。它将输入 `x` 与这个权重矩阵相乘，得到一个logit向量，其维度等于专家的数量（比如，8个专家，就得到一个8维的logit向量）。
        $$ \text{logits} = x \cdot W_g $$

    12. **转换为概率/权重**: 这个logit向量通过 `Softmax` 函数，转换成一个概率分布 `p`。向量 `p` 中的每一个值 `p_i` 代表了输入 token `x` 被分配给第 `i` 个专家的“权重”或“倾向性”。
        $$ p = \text{Softmax}(\text{logits}) $$

    13. **做出路由决策 (Top-K Gating)**:
        *   模型选择 `p` 中值最大的 K 个（比如K=2）。
        *   被选中的这 K 个专家被**激活**。
        *   这 K 个专家对应的概率值 `p_i` 将被用作后续结果加权的权重。

    14. **计算与反向传播**:
        *   Token `x` 被送到这 K 个被激活的专家那里进行计算。
        *   其他未被选中的专家则完全不参与计算。
        *   在得到最终输出后，当计算模型的总损失（Loss）并进行反向传播时，**梯度不仅会流向被激活的专家，让它们学习如何更好地处理这类 token，同时梯度也会流回路由网络，更新它的权重矩阵 `W_g`**。

    **关键点**：通过这个过程，路由网络 `W_g` 就会慢慢学会：**“哦，当看到一个像 `x` 这样的 token（比如一个 Python 关键词），我应该把它分配给第3号和第7号专家（可能它们已经逐渐专精于代码），并且分配给第3号专家 70% 的权重，第7号专家 30% 的权重。”**

    - 一个巨大的挑战：负载不均衡 (Load Imbalance)

    如果单纯这样训练，会很容易出现一个严重问题：**“马太效应”**。

    路由器可能会很快发现有几个专家特别“能干”（或者只是初始参数比较好），于是倾向于把所有类型的 token 都发给这几个“明星专家”。这会导致：
    *   **明星专家过载**: 少数专家被过度训练，计算负载集中。
    *   **懒汉专家荒废**: 其他专家很少接收到 token，得不到训练，其参数基本不变，逐渐“荒废”。

    这违背了我们希望专家们“各有所长、分工合作”的初衷。

    ##### 解决方案：负载均衡损失 (Load Balancing Loss)

    为了解决这个问题，研究者引入了一种巧妙的**辅助损失函数 (Auxiliary Loss)**，专门用来“惩罚”不均衡的路由行为。

    这个损失函数的设计目标是**鼓励路由器将 token 尽可能均匀地分配给所有专家**。

    它的计算方式大致是：

    1.  在一个批次（Batch）的训练中，统计每个专家被分配到的 token 数量的比例。
    2.  如果这个分配非常不均匀（比如专家1处理了90%的token，其他7个专家只处理了剩下的10%），那么负载均衡损失就会变得非常大。
    3.  这个辅助损失会与模型的主要损失（比如预测下一个词的交叉熵损失）加在一起，共同指导模型的训练。

    $$ \text{Total Loss} = \text{Main Loss} + \alpha \times \text{Load Balancing Loss} $$
    （其中 `α` 是一个超参数，用来控制这个辅助损失的重要性）

    通过这种方式，路由器在训练时就陷入了一种“甜蜜的烦恼”：
    *   一方面，它想把 token 送给最匹配的专家，以降低**主要损失**。
    *   另一方面，它又必须顾及公平，尽量雨露均沾地把 token 分给所有专家，以降低**辅助损失**。

    在这种权衡之下，模型最终会学到一个既高效又均衡的路由策略，促使不同的专家群体逐渐演化出处理不同领域知识的“专长”。

    ---
    **面试总结**

    **面试官您好，关于MoE如何学习路由，我的理解是：**

    1.  **路由网络本身是可训练的**：它是一个小型神经网络（通常是线性层），其参数是整个大模型参数的一部分，会在训练中通过反向传播进行学习。
    2.  **学习机制**：在训练时，对于每个token，路由网络会计算并输出一个分配给所有专家的“权重”或“概率”，并选择权重最高的几个专家激活。当模型根据最终预测结果计算损失并反向传播时，梯度也会更新路由网络的参数，从而让它学会“看到什么类型的token，就该分配给哪些专家”。
    3.  **核心挑战与解决方案**：这个学习过程面临“负载不均衡”的挑战，即路由器可能倾向于只使用少数几个专家。解决方案是引入一个**“负载均衡辅助损失函数”**。这个额外的损失会惩罚不均衡的分配行为，迫使路由器在追求“专业对口”的同时，也要尽量“雨露均沾”，从而激励所有专家都得到充分训练，最终形成各有所长的分工体系。

!!! note "BF16、FP16、FP32对比"

    澄清概念：首先，FP32、FP16、BF16都是浮点数格式，将模型从高精度转为低精度浮点数的过程通常叫低精度或混合精度训练。而“量化”在业界通常特指将模型从浮点数转为INT8/INT4等整数格式，主要用于推理加速。

    核心作用：使用这些低精度格式的核心目的是为了解决大模型的**“内存墙”和“计算墙”**问题。具体来说，它们能：

    节省显存：将模型权重从32位减为16位，显存占用直接减半。
    加快计算：数据传输更快，并且现代GPU的Tensor Core对16位计算有专门优化，速度远超32位。
    不同格式的权衡（Trade-off）：

    FP32是基准，精度高但开销大。
    FP16牺牲了动态范围来保留部分精度。这导致它在训练时梯度容易溢出，稳定性差，需要配合混合精度等复杂技巧。
    BF16的设计非常关键，它保留了和FP32完全相同的动态范围，只牺牲了精度。这使得它在训练时非常稳定，几乎可以直接替代FP32，因此成为了当前大模型训练的主流选择。
    INT8/INT4量化是更极致的压缩，主要用在推理阶段，以最大化地降低模型体积和延迟，方便在消费级硬件上部署，但会伴随一定的精度损失。
    总结来说，这是一个典型的用精度换取效率的策略。BF16因为其出色的训练稳定性，成为了平衡性能和成本的最佳甜点，而INT量化则是端侧部署的终极武器。



!!! question "Adam, AdamW 优化器的作用是什么？"
    好的，这个问题非常经典，是深度学习面试中的必考题。



    **一句话概括：**

    Adam 优化器可以被看作是一个**更智能、更高效的“梯度下降”方法**。它的主要作用是**指导模型在训练过程中如何有效地更新参数（权重），从而更快、更稳定地找到损失函数的最小值。**

    **一个经典的类比：**

    想象一下，你站在一座连绵不绝的山脉上，眼睛被蒙住，你的任务是尽快走到山脉的最低点（也就是损失函数的最小值点）。

    *   **普通梯度下降 (SGD)**：你每走一步，都会伸脚试探一下当前位置最陡峭的方向，然后朝那个方向迈出一小步。但如果这个山谷是一个狭长而弯曲的峡谷，你可能会在峡谷两侧来回震荡，走得很慢。
    *   **Adam 优化器**：你就像一个拥有**“惯性”**和**“环境感知能力”**的智能小球。
        *   **惯性**：你不会每一步都完全改变方向，而是会保留一部分上一步的速度，让你能冲过平坦的区域，并抑制在峡谷两侧的震荡。
        *   **环境感知**：你会根据脚下路面的“崎岖程度”来动态调整步伐。在平坦的大路上（梯度小的参数），你会迈出更大的步子；在崎岖不平的陡坡上（梯度大的参数），你会小心翼翼地迈出小步子，防止冲过头。

    ---

    Adam 这个名字来源于 **Adaptive Moment Estimation（自适应矩估计）**，它巧妙地结合了两种强大的优化技术：

    - 1. 动量 (Momentum) - 决定“方向”的惯性

    *   **作用**: 解决普通梯度下降在某些地形（如狭长山谷）中收敛慢、易震荡的问题。
    *   **原理**: 它引入了“一阶矩估计”，可以理解为梯度的**指数移动平均值**。简单来说，它不仅考虑当前这一步的梯度方向，还参考了之前几步的平均方向。
    *   *   当梯度方向一致时，这个“动量”会累积，使得更新步伐加速。
        *   当梯度方向来回摆动时，这个“动量”会相互抵消，起到抑制震荡的作用。

    - 2. 自适应学习率 (RMSprop) - 决定“步长”的感知能力

    *   **作用**: 解决所有参数都共享同一个学习率（步长）的低效问题。
    *   **原理**: 它引入了“二阶矩估计”，可以理解为**梯度平方**的指数移动平均值。这个值可以衡量一个参数梯度的“历史波动性”或“大小”。
    *   *   对于历史上梯度一直较小的参数（路面平坦），Adam 会用一个较小的分母来除，使得有效学习率变大，从而迈出更大的步子。
        *   对于历史上梯度一直较大的参数（路面陡峭），Adam 会用一个较大的分母来除，使得有效学习率变小，从而迈出更小的步子，防止“冲出”最优解。

    **总结起来，在每一步更新时：**
    **Adam = 用“动量”算出一个大致的前进方向 + 用“自适应学习率”机制决定每个参数在该方向上该走多远。**

    补充一点，Adam 还包含一个**偏差修正（Bias Correction）**步骤，用于修正在训练初期，移动平均值会偏向于零的问题，确保初始阶段的步长不会过小。

    - 为什么它成为了默认首选？

    *   **收敛速度快**：结合了动量和自适应学习率的优点，在大多数情况下比其他优化器收敛得更快。
    *   **实现简单，效果稳健**：在各种模型和数据集上都表现良好，是“开箱即用”的可靠选择。
    *   **对超参数不那么敏感**：它的几个关键超参数（如 `beta1`, `beta2`, `epsilon`）通常使用默认值就能取得不错的效果，减少了调参的负担。

    ---
    ### 面试精炼版回答

    面试官您好，关于Adam优化器，我的理解是：

    1.  **它的作用**：Adam是一种高效的梯度下降优化算法，用来在模型训练时指导参数更新，目标是更快、更稳定地找到损失函数的最小值。

    2.  **核心思想**：它结合了两种经典优化思想。**一是“动量（Momentum）”**，通过计算梯度的指数移动平均（一阶矩），为参数更新引入“惯性”，以加速收敛并抑制震荡。**二是“自适应学习率（Adaptive Learning Rate）”**，通过计算梯度平方的指数移动平均（二阶矩），为模型中的每一个参数动态地、独立地计算学习率，使得在梯度平缓的参数上步长大，在梯度陡峭的参数上步长小。

    3.  **为什么流行**：Adam综合了上述优点，收敛速度快，在各种任务中表现稳健，而且超参数相对不敏感，使其成为了绝大多数深度学习任务的默认首选优化器。


---


## Embedding 

词嵌入，NLP 的常用技术。

```python
class InputEmbeddings(nn.Module):

    def __init__(self, d_model: int, vocab_size: int) -> None:
        super().__init__()
        self.d_model = d_model # 模型的embedding 的维度 (512)
        self.vocab_size = vocab_size 
        self.embedding = nn.Embedding(vocab_size, d_model)
        # embedding 本质上是把一个表示 token 的索引映射到向量中

    def forward(self, x):
        # (batch, seq_len) --> (batch, seq_len, d_model)
        # Multiply by sqrt(d_model) to scale the embeddings according to the paper
        # embedding 的结果需要进行缩放
        return self.embedding(x) * math.sqrt(self.d_model)
```

## Positional Embedding

位置编码，传递每个Token在上下文中的位置信息，维度和 embedding 一样，遵循：

$PE(pos, 2i) = \sin \dfrac{pos}{10000^{\frac{2i}{d_{model}}}}$

$PE(pos, 2i + 1) = \cos \dfrac{pos}{10000^{\frac{2i + 1}{d_{model}}}}$

对于上下文中每个位置的 embedding，根据embedding的索引奇偶给出对应的计算。


```python
class PositionalEncoding(nn.Module):

    def __init__(self, d_model: int, seq_len: int, dropout: float) -> None:
        super().__init__()
        self.d_model = d_model
        self.seq_len = seq_len # 上下文的长度
        self.dropout = nn.Dropout(dropout) # Dropout: 减少过拟合
        # Create a matrix of shape (seq_len, d_model) 
        pe = torch.zeros(seq_len, d_model) # 所有上下文每个位置的 RoPE 的矩阵
        # Create a vector of shape (seq_len)
        position = torch.arange(0, seq_len, dtype=torch.float).unsqueeze(1) # (seq_len, 1)
        # Create a vector of shape (d_model)
        div_term = torch.exp(torch.arange(0, d_model, 2).float() * (-math.log(10000.0) / d_model)) # (d_model / 2)
        # Apply sine to even indices
        pe[:, 0::2] = torch.sin(position * div_term) # sin(position * (10000 ** (2i / d_model))
        # Apply cosine to odd indices
        # 这里的 even / odd indices 是 embedding 的 even / odd 位置的参数
        # 这里的 position 是这个 token 在上下文中的位置
        pe[:, 1::2] = torch.cos(position * div_term) # cos(position * (10000 ** (2i / d_model))
        # Add a batch dimension to the positional encoding
        # 添加一个 batch 维度方便后面训练
        pe = pe.unsqueeze(0) # (1, seq_len, d_model)
        # Register the positional encoding as a buffer
        self.register_buffer('pe', pe)

    def forward(self, x):
        x = x + (self.pe[:, :x.shape[1], :]).requires_grad_(False) # (batch, seq_len, d_model)
        # positional embedding 的部分不需要计算梯度 直接加到 embedding 层上即可
        return self.dropout(x)

```

## LayerNorm 

相当于,每个上下文中,每一个位置 (第1, 2, ,3 ... , 512个位置的embedding做了一个Normalization)，==并不是在一个batch，对每个batch的同样位置进行归一化==。

TODO 补充原因：

同样的，这里归一化的参数也是可以学习的。

```python
class LayerNormalization(nn.Module):

    def __init__(self, features: int, eps:float=10**-6) -> None:
        super().__init__()
        self.eps = eps
        self.alpha = nn.Parameter(torch.ones(features)) # alpha is a learnable parameter
        self.bias = nn.Parameter(torch.zeros(features)) # bias is a learnable parameter

    def forward(self, x):
        # x: (batch, seq_len, hidden_size)
         # Keep the dimension for broadcasting
        mean = x.mean(dim = -1, keepdim = True) # (batch, seq_len, 1)
        # 相当于,每个上下文中,每一个位置 (第1, 2, ,3 ... , 512个位置的embedding做了一个Normalization)
        # Keep the dimension for broadcasting
        std = x.std(dim = -1, keepdim = True) # (batch, seq_len, 1)
        # eps is to prevent dividing by zero or when std is very small
        # 归一化的参数 (一个是乘积,一个是累加的bias）都是可以学习的
        return self.alpha * (x - mean) / (std + self.eps) + self.bias
```

## Feedforward Network

其实是两个通过ReLU连接的全连接层，对 embedding 进行学习。

TODO 为什么需要这一层？

```python
class FeedForwardBlock(nn.Module):
    # Feedforward Network,本质上是两个全连接层，激活函数用ReLU连接
    # "applied to each position separately and identically"
    # FFN(x) = max(0, xW_1 + b_1)W_2 + b_2
    def __init__(self, d_model: int, d_ff: int, dropout: float) -> None:
        super().__init__()
        self.linear_1 = nn.Linear(d_model, d_ff) # w1 and b1
        self.dropout = nn.Dropout(dropout)
        self.linear_2 = nn.Linear(d_ff, d_model) # w2 and b2


    def forward(self, x):
        # 先把每个位置的 embedding 传递到 dff (=2048) 维度的全连接层，然后再连接回 512 (d_model)
        # (batch, seq_len, d_model) --> (batch, seq_len, d_ff) --> (batch, seq_len, d_model)
        return self.linear_2(self.dropout(torch.relu(self.linear_1(x))))
```

## Multi-head Attention 

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202509100218070.png)

```python
class MultiHeadAttentionBlock(nn.Module):

    def __init__(self, d_model: int, h: int, dropout: float) -> None:
        super().__init__()
        self.d_model = d_model # Embedding vector size
        self.h = h # Number of heads, 不同头的数量
        # Make sure d_model is divisible by h
        assert d_model % h == 0, "d_model is not divisible by h"

        self.d_k = d_model // h # Dimension of vector seen by each head
        self.w_q = nn.Linear(d_model, d_model, bias=False) # Wq (batch, d_model, d_model)
        self.w_k = nn.Linear(d_model, d_model, bias=False) # Wk
        self.w_v = nn.Linear(d_model, d_model, bias=False) # Wv
        self.w_o = nn.Linear(d_model, d_model, bias=False) # Wo
        self.dropout = nn.Dropout(dropout)
        # 每个头都只能看到对应的向量 (embedding 的部分)

    @staticmethod
    def attention(query, key, value, mask, dropout: nn.Dropout):
        d_k = query.shape[-1]
        # Just apply the formula from the paper
        # (batch, h, seq_len, d_k) --> (batch, h, seq_len, seq_len)
        attention_scores = (query @ key.transpose(-2, -1)) / math.sqrt(d_k)
        if mask is not None:
            # Write a very low value (indicating -inf) to the positions where mask == 0
            attention_scores.masked_fill_(mask == 0, -1e9)
        attention_scores = attention_scores.softmax(dim=-1) # (batch, h, seq_len, seq_len) # Apply softmax
        if dropout is not None:
            attention_scores = dropout(attention_scores)
        # (batch, h, seq_len, seq_len) --> (batch, h, seq_len, d_k)
        # return attention scores which can be used for visualization
        return (attention_scores @ value), attention_scores

    def forward(self, q, k, v, mask):
        query = self.w_q(q) # (batch, seq_len, d_model) --> (batch, seq_len, d_model)
        key = self.w_k(k) # (batch, seq_len, d_model) --> (batch, seq_len, d_model)
        value = self.w_v(v) # (batch, seq_len, d_model) --> (batch, seq_len, d_model)

        # (batch, seq_len, d_model) --> (batch, seq_len, h, d_k) --> (batch, h, seq_len, d_k)
        query = query.view(query.shape[0], query.shape[1], self.h, self.d_k).transpose(1, 2)
        key = key.view(key.shape[0], key.shape[1], self.h, self.d_k).transpose(1, 2)
        value = value.view(value.shape[0], value.shape[1], self.h, self.d_k).transpose(1, 2)

        # Calculate attention
        x, self.attention_scores = MultiHeadAttentionBlock.attention(query, key, value, mask, self.dropout)
        
        # Combine all the heads together
        # (batch, h, seq_len, d_k) --> (batch, seq_len, h, d_k) --> (batch, seq_len, d_model)
        x = x.transpose(1, 2).contiguous().view(x.shape[0], -1, self.h * self.d_k)

        # Multiply by Wo
        # (batch, seq_len, d_model) --> (batch, seq_len, d_model)  
        return self.w_o(x)
```
