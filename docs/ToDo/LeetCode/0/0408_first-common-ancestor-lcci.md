# 0408_第一个公共祖先

<!-- 所有文件名必须是该题目的英文名 -->

!!! note
    <!-- 这里记载考察的数据结构、算法等 -->
    递归 ｜ 二叉树 

    2024.05.03 复习到一次。没做出来。

- 🔑🔑 难度：<span style = "color:gold; font-weight:bold">Medium</span>
<!-- <span style = "color:gold; font-weight:bold">Medium</span> 中等 -->
<!-- <span style = "color:crisma; font-weight:bold">High</span> 困难 -->
<!-- <span style = "color:Green; font-weight:bold">Easy</span> 简单 -->

<!-- 题目简介 -->

> 设计并实现一个算法，找出二叉树中某两个节点的第一个共同祖先。不得将其他的节点存储在另外的数据结构中。注意：这不一定是二叉搜索树。
> 
> 例如，给定如下二叉树: root = [3,5,1,6,2,0,8,null,null,7,4]
> 
```
输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出: 3
解释: 节点 5 和节点 1 的最近公共祖先是节点 3。
```

------

??? note 

    
-------------

=== "Python"

    ```Python
    # Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None

    class Solution:
        def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
            if  not root:
                return None
            
            if root == p or root == q:
                # 一旦这个节点等于p或q的任何一个，返回非空的这个节点
                return root 

            nodel = self.lowestCommonAncestor(root.left, p, q)
            # 如果在left分支没有p，q，这个nodel一定是None的，只要有一个p，q出现，nodel就不是负的
            noder = self.lowestCommonAncestor(root.right ,p, q)

            if nodel and noder:
                return root
            
            if nodel:
                return nodel
            else:
                return noder
    ```
