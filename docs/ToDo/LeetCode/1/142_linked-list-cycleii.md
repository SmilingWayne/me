# 142_?

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
    public class Solution {
        public ListNode detectCycle(ListNode head) {
            ListNode fast = head;
            ListNode slow = head;
            if(head == null||head.next==null)
            return null;
            while(fast!=null){
                slow = slow.next;
                if(fast.next!=null){
                    fast = fast.next.next;
                }
                else{
                    return null;
                }
                if(fast == slow){
                    ListNode str = head;
                    while(str != slow){
                        str = str.next;
                        slow = slow.next;
                        
                    }
                    return str;
                }
            }
            return null;
        }
    }

    //Java.Version2:

    /**
     * Definition for singly-linked list.
     * class ListNode {
     *     int val;
     *     ListNode next;
     *     ListNode(int x) {
     *         val = x;
     *         next = null;
     *     }
     * }
     */
    
    
    public class Solution2 {
        public ListNode detectCycle(ListNode head) {
            ListNode fast = head;
            ListNode slow = head;
            if(head == null||head.next==null)
            return null;
            Map<ListNode, Integer> map = new HashMap<>();
            while(fast!=null&&fast.next!=null){
                if(map.containsKey(fast))
                return fast;
                else{
                    map.put(fast,fast.val);
                    fast = fast.next;
                }
            }
            return null;
        }
    }

    /*方法三和方法二原理是一样的
    */
    public class Solution3 {
        public ListNode detectCycle(ListNode head) {
            Set<ListNode> set = new HashSet<>();
            ListNode help = head;
            while(help != null){
                if(! set.add(help)){
                    return help;
                }
                help = help.next;
            }
            return null;
        }
    }

    ```