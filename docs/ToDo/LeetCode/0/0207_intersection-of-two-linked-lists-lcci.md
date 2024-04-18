# 0207_链表相交

<!-- 所有文件名必须是该题目的英文名 -->

!!! note
    <!-- 这里记载考察的数据结构、算法等 -->
    链表

- 🔑🔑 难度：<span style = "color:Green; font-weight:bold">Easy</span>
<!-- <span style = "color:gold; font-weight:bold">Medium</span> 中等 -->
<!-- <span style = "color:crisma; font-weight:bold">High</span> 困难 -->
<!-- <span style = "color:Green; font-weight:bold">Easy</span> 简单 -->

<!-- 题目简介 -->

> 给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表没有交点，返回 null 。
> 
> 图示两个链表在节点 c1 开始相交：
> 


![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/14/160_statement.png)

------

??? note 
    对齐之后遍历即可。

    
    
-------------

=== "Python"

    ```Python
    # Definition for singly-linked list.
    # class ListNode:
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None

    class Solution:
        def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
            tmpA , tmpB = headA, headB 
            cntA = 0
            cntB = 0
            while tmpA != None:
                cntA += 1
                tmpA = tmpA.next
            while tmpB != None:
                cntB += 1
                tmpB = tmpB.next
            
            if cntA > cntB:
                tmpA, tmpB = headB, headA
                cntA, cntB = cntB, cntA
            else:
                tmpA, tmpB = headA, headB 
            
            for i in range(cntB - cntA):
                tmpB = tmpB.next
            
            while tmpB != None:
                if tmpB == tmpA:
                    return tmpB
                else:
                    tmpB = tmpB.next
                    tmpA = tmpA.next 

            return None
                    
    ```
