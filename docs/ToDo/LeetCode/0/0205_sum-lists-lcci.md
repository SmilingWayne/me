# 0205_链表求和

<!-- 所有文件名必须是该题目的英文名 -->

!!! note
    <!-- 这里记载考察的数据结构、算法等 -->
    链表 | 复习一下反转链表

- 🔑🔑 难度：<span style = "color:gold; font-weight:bold">Medium</span>
<!-- <span style = "color:gold; font-weight:bold">Medium</span> 中等 -->
<!-- <span style = "color:crisma; font-weight:bold">High</span> 困难 -->
<!-- <span style = "color:Green; font-weight:bold">Easy</span> 简单 -->

<!-- 题目简介 -->

> 给定两个用链表表示的整数，每个节点包含一个数位。
> 
> 这些数位是反向存放的，也就是个位排在链表首部。
> 
> 编写函数对这两个整数求和，并用链表形式返回结果。


```
输入：(7 -> 1 -> 6) + (5 -> 9 -> 2)，即617 + 295
输出：2 -> 1 -> 9，即912
```

------

??? note 

    
-------------

=== "Python"

    ```Python
    # Definition for singly-linked list.
    # class ListNode:
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None

    class Solution:
        def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
            result = ListNode(0)
            res = result
            offset = 0
            while l1 != None or l2 != None:
                if l1 != None:
                    offset += l1.val
                    l1 = l1.next
                if l2 != None:
                    offset += l2.val
                    l2 = l2.next
                
                result.next = ListNode(offset % 10)
                result = result.next
                offset = offset // 10
            if offset > 0:
                result.next = ListNode(offset)
            return res.next
            
    ```
