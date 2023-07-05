# 445_两数相加-ii

<!-- 所有文件名必须是该题目的英文名 -->

!!! note
    <!-- 这里记载考察的数据结构、算法等 -->
    反转链表 ｜ 两数之和

- 🔑🔑 难度：<span style = "color:gold; font-weight:bold">Medium</span>
<!-- <span style = "color:gold; font-weight:bold">Medium</span> 中等 -->
<!-- <span style = "color:crisma; font-weight:bold">High</span> 困难 -->
<!-- <span style = "color:Green; font-weight:bold">Easy</span> 简单 -->

<!-- 题目简介 -->

> 给你两个 非空 链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。
> 
> 你可以假设除了数字 0 之外，这两个数字都不会以零开头。
> 
```

输入：l1 = [7,2,4,3], l2 = [5,6,4]
输出：[7,8,0,7]
```

------

??? note 
    相当于“反转链表 + 两数之和

    
-------------

=== "Python"

    ```Python
    # Definition for singly-linked list.
    # class ListNode:
    #     def __init__(self, val=0, next=None):
    #         self.val = val
    #         self.next = next
    class Solution:

        def reverseList(self, arr):
            if arr is None or arr.next is None:
                return arr
            
            next_node = self.reverseList(arr.next)
            arr.next.next = arr
            arr.next = None
            return next_node

        def addTwo(self, l1, l2, carry = 0):
            if l1 is None and l2 is None:
                return ListNode(carry) if carry else None
            
            if l1 is None :
                l1, l2 = l2, l1
            
            carry += l1.val + (l2.val if l2 else 0) 
            l1.val = carry % 10
            carry = carry // 10
            l1.next = self.addTwo(l1.next, l2.next if l2 else None, carry)
            return l1
            

            return 
        def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
            l1 = self.reverseList(l1)
            l2 = self.reverseList(l2)
            l3 = self.addTwo(l1, l2)
            return self.reverseList(l3)

        
    ```