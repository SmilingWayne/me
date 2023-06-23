# 2_两数相加

<!-- 所有文件名必须是该题目的英文名 -->

!!! note
    <!-- 这里记载考察的数据结构、算法等 -->
    链表

- 🔑🔑 难度：<span style = "color:gold; font-weight:bold">Medium</span>
<!-- <span style = "color:gold; font-weight:bold">Medium</span> 中等 -->
<!-- <span style = "color:crisma; font-weight:bold">High</span> 困难 -->
<!-- <span style = "color:Green; font-weight:bold">Easy</span> 简单 -->

<!-- 题目简介 -->
> 给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
> 
> 请你将两个数相加，并以相同形式返回一个表示和的链表。
> 
> 你可以假设除了数字 0 之外，这两个数都不会以 0 开头。


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