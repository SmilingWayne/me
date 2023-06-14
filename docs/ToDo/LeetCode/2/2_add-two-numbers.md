# 2_中文题目

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
        public ListNode addTwoNumbers(ListNode l1,  ListNode l2) {
            ListNode res = new ListNode(0);
            ListNode ans = res;
            int carry = 0;
            int num = 0;

            while(l1!=null||l2!=null){
                int x;
                int y;
                if(l1!=null)
                    x = l1.val;
                else 
                    x = 0;
                if( l2 != null)
                    y = l2.val;
                else y = 0;
                num = (x+y+carry)%10;
                carry = (int)(x+y+carry)/10;
                res.next = new ListNode(num);
                res = res.next;
                if(l1!=null)
                    l1 = l1.next;
                if(l2!=null)
                    l2 = l2.next;
            }
            if(carry>0)
                res.next = new ListNode(carry);
            return ans.next;
        }
    }
    ```