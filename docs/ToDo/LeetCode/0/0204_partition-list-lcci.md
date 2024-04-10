# 0204_分割链表


<!-- 所有文件名必须是该题目的英文名 -->

!!! note
    <!-- 这里记载考察的数据结构、算法等 -->
    链表

- 🔑🔑 难度：<span style = "color:gold; font-weight:bold">Medium</span>
<!-- <span style = "color:gold; font-weight:bold">Medium</span> 中等 -->
<!-- <span style = "color:crisma; font-weight:bold">High</span> 困难 -->
<!-- <span style = "color:Green; font-weight:bold">Easy</span> 简单 -->

<!-- 题目简介 -->

> 给你一个链表的头节点 head 和一个特定值 x ，请你对链表进行分隔，使得所有 小于 x 的节点都出现在 大于或等于 x 的节点之前。
> 
> 你不需要 保留 每个分区中各节点的初始相对位置。

![](https://assets.leetcode.com/uploads/2021/01/04/partition.jpg)

```
输入：head = [1,4,3,2,5,2], x = 3
输出：[1,2,2,4,3,5]
```

------

??? note 
    维护两个链表，分别记录比x小的所有节点和不比x小的节点。最后头尾一拼就ok了。
    
-------------


=== "Python"
    ```Python
    # Definition for singly-linked list.
    # class ListNode:
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None

    class Solution:
        def partition(self, head: ListNode, x: int) -> ListNode:
            if head == None or head.next == None:
                return head 
            dummyheadsmall = ListNode(0)
            temp_dummy_small = dummyheadsmall 

            dummyheadlarge = ListNode(0)
            temp_dummy_large = dummyheadlarge 
            while head != None:
                if head.val < x:
                    dummyheadsmall.next = ListNode(head.val)
                    dummyheadsmall = dummyheadsmall.next 
                else:
                    dummyheadlarge.next = ListNode(head.val)
                    dummyheadlarge = dummyheadlarge.next 
                head = head.next 

            dummyheadsmall.next = temp_dummy_large.next
            return temp_dummy_small.next
            
    ```
