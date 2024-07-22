# 运筹学、数学建模、优化理论

!!! example "广告一则"
    运筹相关的源代码，高质量的不多，求解器的使用，大家还是极度依赖于各种官方给出的一些零散的demo，在落地到实际问题的时候就蒙圈了。越在圈子里摸爬滚打越能体会到这种“拔剑四顾心茫然”[^1]的无助感。
    
    所以自己搞了一个开源的[代码仓库](https://github.com/SmilingWayne/PuzzleSolver)，里面有一些模型求解demo代码、一些问题的变型、一些有趣的游戏。绝大多数与运筹或者数学建模相关，自卖自夸一下我认为的优点：
    
    - 覆盖了线性规划、混合整数线性规划、约束优化求解器；
    - 涉及路线规划、生产调度等多个应用场景；
    - 包含了一些有趣的逻辑游戏的运筹解法。一些游戏 (Slither Link, Simple Loop, Creek, Sandwich Sudoku)，目前少有开源的解决方案；
    - 包含了一些高级运筹学技巧的实现、修正和数值试验；
    - 包含了多款求解器的调用。(Commercial and Open Source included)；

    如果对你有帮助，一个小小的Star就可以～

    有好的建议，欢迎提PR或issue。会及时更新。




!!! abstract "目录"
    - **Chapter. 0** [一些经典运筹习题](./ORExercise/Works.md)
    - **Chapter. 1** [线性规划](./Chapter1.md) 🌟🌟🌟
    - **Chapter. 2** [线性规划的对偶理论](./Chapter2.md) 🌟🌟
    - **Chapter. 3** [线性规划的扩展](./Chapter3.md)
    - **Chapter. 4** [整数规划](./Chapter4.md)
    - **Chapter. 5** [非线形规划](./Chapter5.md)
    - **Chapter. 6** [动态规划](./Chapter1.md)
    - **Chapter. 7** [图与网络](./Chapter1.md)
    - **Chapter. 9** [排队论](./Chapter9.md) 
    - **Chapter. 10** [存储论](./Chapter10.md)
    - **Chapter. 11** [博弈论](./Chapter11.md)
    - **Chapter. 12** 一些高级的运筹学技巧与建模
        - [列生成算法](./Chapter12.md)：征服大规模线性规划问题的第一步；
        - [分支定价算法](./BranchAndPrice.md)：更快，更标准，更严格的整数规划。
        - Benders Decomposition：好羡慕学得懂的那些孩子。
        - [拉格朗日松弛](./LR.md): 拉格朗日松弛，养活了大半个运筹理论。
        - Danzig Wolfe Decomposition：好像还是没有学会。
        - [Travelling Salesman Problem](./TSP.md)：旅行商问题：建模篇。


- 本部分来源《运筹学》 机械工业出版社。如有需要建议使用清华的运筹教材，英文教材推荐 Bertsimas 和 Tsitsiklis 1997 的 [Introduction to linear optimization](https://book.douban.com/subject/2157943/)。Bertsimas，受我一拜！

[^1]: 语出唐代李白[《行路难·其一》](https://www.gushiwen.cn/mingju_524.aspx)。