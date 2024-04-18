# 141_链表相交

<!-- 所有文件名必须是该题目的英文名 -->

!!! note
    <!-- 这里记载考察的数据结构、算法等 -->
    链表

- 🔑🔑 难度：<span style = "color:gold; font-weight:bold">Medium</span>
<!-- <span style = "color:gold; font-weight:bold">Medium</span> 中等 -->
<!-- <span style = "color:crisma; font-weight:bold">High</span> 困难 -->
<!-- <span style = "color:Green; font-weight:bold">Easy</span> 简单 -->

<!-- 题目简介 -->
> 给定一个链表，如果它是有环链表，实现一个算法返回环路的开头节点。若环不存在，请返回 null。
> 
> 如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。

![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/07/circularlinkedlist.png)

------

??? note
    用快慢指针做。

-------------

=== "Java"

    ```java
    public class Solution {
        public boolean hasCycle(ListNode head) {
            ListNode fast = head;
            ListNode slow = head;
            if(head==null)
            return false;
            while(fast!=null&&fast.next!=null)。 //fast判断放在前面，接下来才是fast.next判断//
            {
                slow = slow.next;
                fast = fast.next.next;
                if(slow == fast)
                return true;
            }
            return false;
        }
    }
        
    ```
=== "Python"
    
    ```Python
    # Definition for singly-linked list.
    # class ListNode:
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None

    class Solution:
        def detectCycle(self, head: ListNode) -> ListNode:
            if head == None or head.next == None:
                return None 
            slow = head 
            fast = head
            while fast != None:
                slow = slow.next 
                if fast.next == None:
                    return None
                fast = fast.next.next 
                if fast == slow:
                    back = head
                    while back != slow:
                        slow = slow.next 
                        back = back.next 

                    return back 

            return None
    ```