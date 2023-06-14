# 94_中文题目

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
        public List<Integer> inorderTraversal(TreeNode root) {
            List<Integer> res = new ArrayList<>();
            Deque<TreeNode> stack = new LinkedList<>();
            TreeNode cur = root;
            while(cur!=null||!stack.isEmpty()){     
                //这里确保！stack.isEmpty()实际上是为了确保有两个字节点都是null的情况//
                if(cur!=null){
                    stack.push(cur);
                    cur = cur.left;
                }
                else{
                    cur = stack.pop();
                    res.add(cur.val);
                    cur = cur.right;
                }
            }
            return res;
        }
    }
    class Solution2 {
        public List<Integer> inorderTraversal(TreeNode root) {
            List<Integer> res = new ArrayList<>();
            search(root,res);
            return res;

        }
        public void search(TreeNode root, List<Integer> res){
            if(root == null){
                return;
            }
            search(root.left,res);
            res.add(root.val);
            search(root.right,res);
        }
    }

    ```