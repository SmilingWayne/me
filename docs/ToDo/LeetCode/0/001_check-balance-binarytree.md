# 001_检查是否为平衡二叉树

<!-- 所有文件名必须是该题目的英文名 -->

!!! note
    <!-- 这里记载考察的数据结构、算法等 -->
    平衡二叉树

- 🔑🔑 难度：<span style = "color:gold; font-weight:bold">Medium</span>
<!-- <span style = "color:gold; font-weight:bold">Medium</span> 中等 -->
<!-- <span style = "color:crisma; font-weight:bold">High</span> 困难 -->
<!-- <span style = "color:Green; font-weight:bold">Easy</span> 简单 -->

<!-- 题目简介 -->

实现一个函数，检查二叉树是否平衡。在这个问题中，平衡树的定义如下：任意一个节点，其两棵子树的高度差不超过 1。

------

> 解析

-------------

=== "Java"

    ```java
    class Solution {
        public boolean isBalanced(TreeNode root) {
            if(root == null || (root.left == null && root.right == null)){
                return true;
            }   
            if(Math.abs(getHeight(root.left) - getHeight(root.right)) > 1){
                return false;
            }
            else{
                return isBalanced(root.left) && isBalanced(root.right);
            }
        }
        public int getHeight(TreeNode node){
            if(node == null){
                return 0;
            }
            int left = getHeight(node.left);
            int right = getHeight(node.right);
            return Math.max(right, left) + 1;
        }
    }

    ```


