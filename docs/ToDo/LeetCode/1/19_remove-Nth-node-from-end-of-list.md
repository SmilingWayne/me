# 19_删除链表的倒数第N个结点

<!-- 所有文件名必须是该题目的英文名 -->

!!! note
    <!-- 这里记载考察的数据结构、算法等 -->
    哈希表 | 动态规划

- 🔑🔑 难度： <span style = "color:gold; font-weight:bold">Medium</span>

<!-- 题目简介 -->

给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

------

> 解析

-------------

=== "Java"

    ```java
    class Solution {
        public ListNode removeNthFromEnd(ListNode head, int n) {
            ListNode fast = head;
            ListNode slow = head;
            if(n == 1){
                if(slow.next == null){
                    return null;
                }
                while(slow.next.next!=null){
                    slow = slow.next;   //就是这里：十分重要！！！！！！
                }
                slow.next = null;
            }
            else {
                for(int i = 1; i < n; i++){
                    fast = fast.next;
                }
                while(fast.next != null){
                    slow = slow.next;
                    fast = fast.next;
                }
                if(slow.next != null){
                    if(slow.next != null ){
                        slow.val = slow.next.val;
                        slow.next = slow.next.next;
                    }
                    else{
                        slow.val = slow.next.val;
                        slow.next = null;
                    }
                }
                else{
                    slow = null;
                }

            }
            return head;
        }
    }

    
    ```