## 课后习题和建模练习部分


> 带(Hu) 意味着咋i

### 1.1 产品计划问题 (Hu)


某厂生产I、II、 III 三种产品，都分别由A、B两道工序加工而成。A工序由$A_1$, $A_2$ 两个机器完成，有$B1、B2、B3$ 三种设备可用于完成$B$工序。已知产品I可在$A、B$任何一种设备上加工；产品II可在任何规格的$A$设备上加工，但完成$B$工序，只能在$B_1$ 设备上加工; 产品 III 只能在$A_2$与$B_2$设备卜加l。加工单位产品所需工序时间及其他各项数据见表118，试安排最优生产计划，使该厂获利最大。

<table>
   <tr>
      <td rowspan="2">设备</td>
      <td colspan="3">产品</td>
      <td rowspan="2">设备有效台时 / h</td>
      <td rowspan="2">设备加工费 元 / h</td>
   </tr>
   <tr>
      <td>I</td>
      <td>II</td>
      <td>III</td>
   </tr>
   <tr>
      <td>A_1</td>
      <td>5</td>
      <td>10</td>
      <td></td>
      <td>6000</td>
      <td>0.05</td>
   </tr>
   <tr>
      <td>A_2</td>
      <td>7</td>
      <td>9</td>
      <td>12</td>
      <td>10000</td>
      <td>0.03</td>
   </tr>
   <tr>
      <td>B_1</td>
      <td>6</td>
      <td>8</td>
      <td></td>
      <td>4000</td>
      <td>0.06</td>
   </tr>
   <tr>
      <td>B_2</td>
      <td>4</td>
      <td> </td>
      <td>11</td>
      <td>7000</td>
      <td>0.11</td>
   </tr>
   <tr>
      <td>B_3</td>
      <td>7</td>
      <td> </td>
      <td> </td>
      <td>4000</td>
      <td>0.05</td>
   </tr>
   <tr>
      <td>原料费（元/件）</td>
      <td>0.25</td>
      <td>0.35</td>
      <td>0.50</td>
      <td>  </td>
      <td> </td>
   </tr>
   <tr>
      <td>售价（元/件）</td>
      <td>1.25</td>
      <td>2.00</td>
      <td>2.80</td>
      <td>  </td>
      <td> </td>
   </tr>
</table>



### 1.13 人员安排问题 
某快餐店坐落在远离城市的风景区，平时游客较少，而每到双休日游客数量猛增。快餐店主要为游客提供快餐服务，该快餐店雇佣了两名正式职工，主要负责管理工作，每天需要工作8小时，其余的工作都由临时工担任，临时工每天要工作4小时。双休日的营业时间为11:00~22:00，根据游客的就餐情况，在双休日的营业时间内所需的职工数（包括正式工和临时工）如表1.34所示：

- 已知一名正式职工11:00开始上班，工作4小时后休息1小时，而后再工作4小时；另一名正式职工13:00开始上班，工作4小时后休息1小时，而后再工作4小时，又知临时工工资为4元/小时。请问：
  1. 在满足对职工需求的条件下，如何安排临时工的班次，使得使用临时工的成本最低？
  2. 如果临时工每班工作时间可以为4小时，也可以为3小时，那么应该如何安排临时工的班次，使得使用临时职工的总成本最小？这样比方案（1）能节省多少费用？



表1.34  营业时间与所需职工数量

| 营业时间    | 所需职工数/人 | 营业时间    | 所需职工数/人 |
| ----------- | :-----------: | ----------- | :-----------: |
| 11:00~12:00 |       9       | 17:00~18:00 |       6       |
| 12:00~13:00 |       9       | 18:00~19:00 |      12       |
| 13:00~14:00 |       9       | 19:00~20:00 |      12       |
| 14:00~15:00 |       3       | 20:00~21:00 |       7       |
| 15:00~16:00 |       3       | 21:00~22:00 |       7       |
| 16:00~17:00 |       3       |             |               |



### 1.13.1 人员安排问题的思考

海河市公交公司负责全市公交车辆的运行与维修管理，已知每天各时段所需人数如表所示，公司所有人员每天从上班起连续工作6小时，每周安排一天休息要求:
- 该公司需配备多少人员，能满足公司的正常运转;
- 由于工作时间差别，有的早上5 : 00就上班，有的到23 : 00才下班; 每周休息一天，有的安排在周一到周五，有的安排在周六或周日，不够平等。因此提出如何安排一天内的倒班及每周内一天的休息日的日期，关系公司人员的切身利益。怎样才能做到完全公平合理？

> 标号 
> 
> 结合每个时间段安排的人的数量进行安排


| 营业时间    | 所需职工数/人 |  营业时间   | 所需职工数 / 人 |
| ----------- | :-----------: | :---------: | :-------------: |
| 05:00~07:00 |      26       | 13:00~15:00 |       38        |
|             |               | 15:00~17:00 |       50        |
| 07:00~09:00 |      50       | 17:00~19:00 |       46        |
| 09:00~11:00 |      34       | 19:00~21:00 |       36        |
| 11:00~13:00 |      40       | 21:00~23:00 |       26        |


### 1.13.2 人员安排问题的思考2

源街邮局从周一到周日每天所需的职员人数如下表所示 职员分别 安排在周内某一天开始上班，并连续工作5天，休息2天。

| 周       | 一  | 二  | 三  | 四  | 五  | 六  | 日  |
| -------- | --- | --- | --- | --- | --- | --- | --- |
| 所需人数 | 17  | 13  | 15  | 19  | 14  | 16  | 11  |

要求确定：
- 该邮局至少应配备多少职员，才能满足值班需要；
- 因从周一开始上班的，双休日都能休息；周二或周日开始上班的，双休日内只能
有一天得到休息；其他时间开始上班的，两个双休日都得不到休息，很不合理。因此邮局准备对每周上班的起始日进行轮换(但从起始日开始连续上5天班的规定不变)问如何
安排轮换，才能做到在一个周期内每名职工享受到同等的双休日的休假天数：
- 该邮局职员中有一名领班，一名副领班。为便于领导，规定领班于每周一、三、四、五、六上班，副领班于一、二、三、五、日这5天上班。据此试重新对上述要求 (1)和(2）
建模和求解。




x_3 + x_4 + x_5 + x_6 + x_7 + x_1 = 26
x_4 + x_5 + x_6 + x_7 + x_1 + x_2 = 50
x_5 + x_6 + x_7 + x_1 + x_2 + x_3 = 34
...

```
一个structure：
                    【职工总数】（代表总共的时间）
                    
【所有工作的周期数】（代表当前职工的工作状况）


```

### 1.14 组合投资问题

某投资者有50万元可用于长期投资，可供选择的投资品种包括购买国债、公司债券、股票、投资房地产、银行短期与长期储蓄。各种投资方式每万元的投资期限、年收益率、风险系数和增长潜力如表1.31所示。如果投资者希望其投资组合的平均投资期限不超过5年，平均期望年收益率不低于13%，平均风险系数不超过4，平均收益的增长潜力不低于10%，在满足上述要求的前提下，请帮助该投资者制定一个组合投资方案，使得平均年收益率最高

表1.31  各种投资项目的相关数据

| 序号 | 投资方式 | 投资期限/年 | 年收益率/% | 风险系数 | 增长潜力/% |
| ---- | :------: | :---------: | :--------: | :------: | :--------: |
| 1    |   国债   |      3      |     5      |    1     |     0      |
| 2    | 公司债券 |     10      |     10     |    3     |     15     |
| 3    |   股票   |      6      |     25     |    8     |     30     |
| 4    |  房地产  |      2      |     20     |    6     |     20     |
| 5    | 短期储蓄 |      1      |     3      |    1     |     5      |
| 6    | 长期储蓄 |      5      |     6      |    2     |     10     |


- 一些应用模型：
    - 风险控制问题（例题1.10）【绝对值在线性规划中的处理】：
    - 生产库存问题（例题1.11）
    - 合理下料问题（例题1.12）
    - 人员安排问题（例题1.13）
    - 组合投资问题（例题1.14）


### 1.15 合理下料问题


下料问题在机械行业、建筑业、造纸、服装等行业的原材料加工过程中经常会遇到。根据原材料和加工产品的不同，一般可以分为一维下料问题和二维下料问题。一维下料问题通常只考虑原材料和加工产品长度的问题，如果是同时考虑长度与宽度两个维度的话，则是二维下料问题。下面考虑一个具体的一维下料问题：

已知制造某机床需要A、B、C三种轴，其规格和需求量如下表1.32所示。如果各种轴都用长5.5米的圆钢来截毛坯，现要制造100台机床，请问如何下料使得所用的原材料最省？

表1.32  轴规格和需求量

| 轴类  | 规格：长度（米） | 每台机床所需件数 |
| :---: | :--------------: | :--------------: |
|   A   |       3.1        |        1         |
|   B   |       2.1        |        2         |
|   C   |       1.2        |        4         |




### 1.16 
假设某种小型设备的生产工厂签订了未来 $n$ 个月的交货合同，其中第 $i$ 个月的合同交货量为$d$台, $i =1,..,n$。该工厂每个月在正常生产时间内可生产$r_i$ 台设备，每台生产成本为 $b$ 元。如果加班生产，由于要支付加班费，每台 生产成本为 $c$ 元$(c > b)$ 。生产的设备如果不交货，则每台每月的存储成 本为 $s$ 元。请建立线性规划模型帮助工厂制定合理的生产计划，使得在完成交货合同的前提下最小化总成本。


### 1.17

请给出下列问题等价的LP模型。

$\min 2x_1 + 3 | x_2 - 10 |$

$s.t. |x_1 + 2 | +| x_2| \leq 5$




----------------


## OR by Prof. Hu (Version. 5)

