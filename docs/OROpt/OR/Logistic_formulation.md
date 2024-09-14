# 记录一个自己做过的多式联运物流配送体系建模

!!! note "问题背景"
    某航空公司货运部门需要对其日常货运订单的运输调度进行优化。首先，货运订单运输流程分为三个阶段，首先需要**从订单出发地借助卡车运输到起飞机场，通过货运飞机抵达目的地机场，在机场借助卡车运输到目的地**。
    
    **场景**：多点出发、多点到达、客户动态持续下单、业务量大；需要将订单分波次进行拆分调度是业内共识，能够大大提高效率。
