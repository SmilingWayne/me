# 机组排班问题

机组排班问题(Crew Scheduling Problem, CSP)，是航空业调度和排班中的一个重要问题。已知一些驾驶舱成员（Cockpit Crew），每个机组有一些可以执飞的航班，称为 Fleet Family，如何在满足诸多约束的情况下，为这些机组安排这些航班，这就是一个典型的机组排班问题。

机组排班问题的输入是一些需要被安排的==航班== (Flight, Flight legs)。如果多个航班连续组成在一起，就形成了一个机组的 ==执勤日== (Duty Period)。如果我们把多天的执勤日串起来，使得机组能够通过一个循环回到初始的基地，这就形成了一些==航班环== (Pairings)，如果多个航班环再串起来，拼成数周乃至一个月的计划，就构成了机组的==月度计划== (Monthly Schedules)。这个过程（Flight legs -> Duty Period -> Pairings -> Monthly Schedules）是机组排班问题的基石。

由上可见，机组排班一个核心的决策就是，给定航班，决定哪些机组分配哪些航班。

**Duty**
:   执勤，是指机组成员按照合格证持有人的要求执行的所有任务，包括飞行值勤、置位、备份、培训等；不一定是航班飞行任务，但是对地理位置会有要求；

**Duty Period 执勤日**
:   A sequence of **flights/duties** that can be flown by a single crew over the course of a work day is a <u>duty period</u>. 我们可以把两个flight中间间隔的时间称为 sit time.

    执勤日很明显需要遵循一些约束：

    1. **时空上**必须是连续的，也就是航班起降、航班时间必须连贯，三个连续航班，A-B,B-C,C-D是允许的，但是 A-B,C-D 这种是不合理的；两个航班10:30-12:05,16:50-17:40 是允许的，但是 10:30-12:05,11:50-13:40 是不合理的；
    2. 确保驾驶员不疲劳以应对轮转，连续航班之间有时间约束，（minimum idle time）；
    3. 一天内有最大飞行时间 (Maximum Flying Time)
    4. ...

    评价执勤日的成本，一般可以通过：(1). 飞行时长；(2). 飞行时长占实际时长的比; (3). ...

**Layover (过夜)**
:   在两个执勤日之间，机组成员需要**过夜（Layover）**，也就是从一个执勤日结束到另一个执勤日开始的阶段，考虑到前后执勤日的结束和开始机场往往不同，机组不会在前一个执勤日结束就回家，第二天再去另一个地方上班，而可能是在一些**指定的过夜机场**进行过夜，第二天直接在这个过夜机场开始新的执勤日，或者在这个过夜机场进行**置位**。

**Pairings(航班环)**
:   如果我们将多个**执勤日**和中间的**过夜**行为串联起来，**使得机组能够从一个Base出发，经过多天执勤，最终返回相同的Base**，那么这一串的执勤日和过夜就构成了一个 Pairing。

    Pairing 面临的约束就更加多了。首先：

    1. 最多执勤任务数量 (maximum number of duties);
    2. 执勤的最小/最大休息时间；
    3. Pairing的最长持续时间 （又被称为 TAFB, **T**ime **A**way **F**rom **B**ase，因为一般Pairing最后要回到开始的机场）
    4. 单日执勤时长加倍休息约束等；

**Schedules**
:   相当于上述汇总：

    Flights - (sit time) - Flight ===> Duty Period

    Duty Period - (layover) - Duty Period ===> Pairings

    Pairings - (time off) - Pairings ===> Schedule

## Crew Pairing Problem

机组配对问题。