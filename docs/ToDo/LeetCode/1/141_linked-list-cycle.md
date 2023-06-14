# 141_?

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