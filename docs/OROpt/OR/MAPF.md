# Multi-Agent Path Finding Problem

- [Book](https://link.springer.com/chapter/10.1007/978-3-030-33274-7_6): Application and review (2019)

> 问题是否是Complete的 / 问题是否能被解到Optimality
>
> NP-hardness 及其证明省略。



!!! note "一些简要的记录"
    - 证明了：同时最小化总时间、最小化最晚到达时间这几个目标，是不可能的。(` optimality cannot always be simultaneously achieved for minimum makespan and minimum total arrival time.`) J. Yu and S. M. LaValle, Structure and Intractability of Op-timal Multi-Robot Path Planning on Graphs. presented atthe Twenty-Seventh AAAI Conference on Artiﬁcial Intelli-gence, Jun. 2013, Accessed: Jul. 27, 2020. [Online]. Available:https://www.aaai.org/ocs/index.php/AAAI/AAAI13/paper/view/6111. 这个文章同样提到的是Multi-robot Path Planning on Graphs with Parallel Moves and Rotations问题。 $MPP_{pr}$ Problem


4-Connected Grid
:   一个精准的描述：二维网格。

WHCA* (Windowed Hierarchical Cooperative A* algorithm)
:   每次预测未来几步要走的路径，然后没到目的地的话就再规划。 [Code(Not verified)](https://github.com/ankx22/Multi-Robot-Motion-Planning-for-Warehouse-Management-using-WHCA-)

Kornhauser’s algorithm 
:   Complicated? 没有找到具体的描述诶。

Push And Swap algorithm
:   [参考链接](https://people.cs.rutgers.edu/~kb572/pubs/push_and_swap_ijcai.pdf)。基于局部的路径进行调整。[Code](https://github.com/msaudulhassan/mapf) (这个课程汇报的小哥做得也太强了吧...)

Well-performed
:   评价算法表现的指标。

Solidable
:   评价表现的指标。

Sam Loyd’s 15-puzzle
:   这不就是华容道？[Wolfram Intro](https://mathworld.wolfram.com/15Puzzle.html).

|            方法             | Intro |
| :-------------------------: | :---: |
|       Extension of A*       |       |
| Increasing cost tree search |       |
|    Conflict-Based Search    |       |
|   Constraint Programming    |       |


> Hailong Huang, https://www.polyu.edu.hk/aae/people/academic-staff/dr-huang-hailong/
