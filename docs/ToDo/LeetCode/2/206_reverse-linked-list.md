# 206_中文题目

<!-- 所有文件名必须是该题目的英文名 -->

!!! note
    <!-- 这里记载考察的数据结构、算法等 -->
    哈希表 | 动态规划

- 🔑🔑 难度：
<!-- <span style = "color:gold; font-weight:bold">Medium</span> 中等 -->
<!-- <span style = "color:crisma; font-weight:bold">High</span> 困难 -->
<!-- <span style = "color:Green; font-weight:bold">Easy</span> 简单 -->

<!-- 题目简介 -->
> Write Here 

------

> 解析

-------------

=== "Java"

    ```java
    
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