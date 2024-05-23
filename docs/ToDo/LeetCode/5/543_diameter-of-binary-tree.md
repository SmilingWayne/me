# 543_二叉树的直径

<!-- 所有文件名必须是该题目的英文名 -->

!!! note ""
    <!-- 这里记载考察的数据结构、算法等 -->
    DFS

- 🔑🔑 难度：<span style = "color:Green; font-weight:bold">Easy</span>
<!-- <span style = "color:gold; font-weight:bold">Medium</span> 中等 -->
<!-- <span style = "color:crisma; font-weight:bold">High</span> 困难 -->
<!-- <span style = "color:Green; font-weight:bold">Easy</span> 简单 -->

<!-- 题目简介 -->

>
> 给你一棵二叉树的根节点，返回该树的 直径 。
> 
> 二叉树的 直径 是指树中任意两个节点之间最长路径的 长度 。这条路径可能经过也可能不经过根节点 root 。
> 
> 两节点之间路径的 长度 由它们之间边数表示。
> 

![](https://assets.leetcode.com/uploads/2021/03/06/diamtree.jpg)

```
输入：root = [1,2,3,4,5]
输出：3
解释：3 ，取路径 [4,2,1,3] 或 [5,2,1,3] 的长度。
```

------

??? note 
    实际上是二叉树的深度。检查每个节点左右孩子的深度，其和 - 1就一定是最大深度。

    
-------------

=== "Python"

    ```Python 
    # Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, val=0, left=None, right=None):
    #         self.val = val
    #         self.left = left
    #         self.right = right
    class Solution:
        def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
            self.res = -1
            def depth(node):
                if not node :
                    return 0
                L = depth(node.left)
                R = depth(node.right)
                self.res = max(self.res, L + R + 1)
                return max(L, R) + 1
            depth(root)
            return self.res - 1
    
    ```
