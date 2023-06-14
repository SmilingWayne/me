# 题号_中文题目

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