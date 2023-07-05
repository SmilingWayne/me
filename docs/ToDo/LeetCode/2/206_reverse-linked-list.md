# 206_反转链表

<!-- 所有文件名必须是该题目的英文名 -->

!!! note
    <!-- 这里记载考察的数据结构、算法等 -->
    链表 ｜ 经典题

- 🔑🔑 难度：<span style = "color:Green; font-weight:bold">Easy</span>
<!-- <span style = "color:gold; font-weight:bold">Medium</span> 中等 -->
<!-- <span style = "color:crisma; font-weight:bold">High</span> 困难 -->
<!-- <span style = "color:Green; font-weight:bold">Easy</span> 简单 -->

<!-- 题目简介 -->
> 给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。


```
输入：head = [1,2,3,4,5]
输出：[5,4,3,2,1]
```

------

> 解析
> 一种是递归做法，一种是迭代做法

-------------

=== "Java"

    ```java
    // 迭代法
    class Solution {
        public ListNode reverseList(ListNode head) {
            ListNode prev = null;
            ListNode current = head;
            while(current != null){
                ListNode next_current = current.next;
                current.next = prev;
                prev = current;
                current = next_current;
            }
            return prev;
        }
    }
    //Recursion//
    Java.vision2:

    class Solution {
        public ListNode reverseList(ListNode head) {
            //递归终止条件是当前为空，或者下一个节点为空
            if(head==null || head.next==null) {
                return head;
            }
            //这里的cur就是最后一个节点
            ListNode cur = reverseList(head.next);
            //这里请配合动画演示理解
            //如果链表是 1->2->3->4->5，那么此时的cur就是5
            //而head是4，head的下一个是5，下下一个是空
            //所以head.next.next 就是5->4
            head.next.next = head;
            //防止链表循环，需要将head.next设置为空
            head.next = null;
            //每层递归函数都返回cur，也就是最后一个节点
            return cur;
        }
    }

    ```

=== "Python"

    ```Python
    
    # Definition for singly-linked list.
    # class ListNode:
    #     def __init__(self, val=0, next=None):
    #         self.val = val
    #         self.next = next
    class Solution:
        def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
            if head == None or head.next == None:
                return head
            
            cur = self.reverseList(head.next)
            head.next.next = head
            head.next = None
            return cur
    ```

    ```Python

        # 迭代做法 
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre  
    ```