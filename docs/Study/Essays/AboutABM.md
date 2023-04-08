# guidelines for ABM

##  ABM 是否合适：



## 设计模型：

- Scope of the model: 模型的范围是什么？
- Agents: 主体是什么？
    - 重大工程参与者
- Properties： 属性有哪些？
- Behaviors: 行为
- Environment：环境：物理的、概念的？
- Input and Output：输入和输出是什么？
- Time Step: 哪一步先开始；哪一步随后开始/模型是怎么一步步迭代完成的


## Reference

- Bass, F. M. (1969). A New Product Growth for Model Consumer Durables. Management Science, 15(5), 215–227. doi:10.1287/mnsc.15.5.215 
  - [https://blog.csdn.net/qq_41103204/article/details/105437287](https://blog.csdn.net/qq_41103204/article/details/105437287)
  - 一篇经典的创新扩散效应的论文（描述新产品怎么在群体中获得使用的过程）
  - The coefficient p is called the coefficient of innovation, external influence or advertising effect. The coefficient q is called the coefficient of imitation, internal influence or word-of-mouth effect. 系数p称为创新系数、外部影响系数或广告效应系数。系数q称为模仿系数、内部影响系数或口碑效应系数。




## 我的论文可以借鉴的地方


- 每个人是否购买那个新的物品取决于下面两者中的任意一个：
    - 大众媒体的压力
    - 口口相传的效应 

- 敏感性测试：
    - 在不同的经济环境条件下，对模型的影响（模型中项目的数量：一天几个？）

- **Model verification && Model Validation 模型验证和模型确认**
    - verification: 验证：Verification is the process of determining that a model implementation accurately represents the developer's conceptual description of the model and its solution. 确认模型的实现和模型概念描述中的（模型和解法）是相符合的
    - validation: 确认（预期情况和实际情况是相符合的） “An activity that ensures that an end product stakeholder’s true needs and expectations are met.”
    - 具体方法：
        - verification：代码走查（code walkthrough / debug walkthrough
        - verification：unit test：单元测试（测试不同的情景和场景scenarios，比如顾客通常会更加xxx，决策者往往会xxx等）
        - validation：做一个回归（也有分宏观和微观不同角度的测试的）

- model validation和敏感性分析的区别
    - This is a bit of an oversimplification, but model validation generally tells one about how well the current model fits the data at hand（模型确认是，告诉你你当前的模型和手头数据的拟合情况）. Sensitivity analyses tell one how likely your results based upon that model would change given new information or changes to your assumptions.（灵敏度分析是告诉你在你模型假定的情况下，模型的结果会如何变化）


## TODO

- 找一下，影响选择的原因是什么、队伍（agent）的特点是什么
- 找一下，具体的参数（衡量指标是什么）
- 找一下，项目属性和测定（data collection）
- 找一下，瑜瑜！（✅ 找到了！）