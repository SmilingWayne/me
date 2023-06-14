# 876_中文题目

<!-- 所有文件名必须是该题目的英文名 -->

!!! note
    <!-- 这里记载考察的数据结构、算法等 -->
    ?

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
        public ListNode middleNode(ListNode head) {
            ListNode fast=head,slow=head;
            while (fast!=null && fast.next!=null){
                fast=fast.next.next;
                slow=slow.next;
            }
            return slow;
        }
    }

    ```