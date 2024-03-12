# 1261_在受污染的二叉树中查找元素

<!-- 所有文件名必须是该题目的英文名 -->

!!! note ""
    <!-- 这里记载考察的数据结构、算法等 -->
    哈希表 | DFS

- 🔑🔑 难度： <span style = "color:gold; font-weight:bold">Medium</span> 中等
<!-- <span style = "color:crisma; font-weight:bold">High</span> 困难 -->
<!-- <span style = "color:Green; font-weight:bold">Easy</span> 简单 -->

<!-- 题目简介 -->

> 给出一个满足下述规则的二叉树：

> root.val == 0
> 
> 如果 treeNode.val == x 且 treeNode.left != null，那么 treeNode.left.val == 2 * x + 1
> 
> 如果 treeNode.val == x 且 treeNode.right != null，那么 treeNode.right.val == 2 * x + 2
> 
> 现在这个二叉树受到「污染」，所有的 treeNode.val 都变成了 -1。
>
> 请你先还原二叉树，然后实现 FindElements 类：
>  
> FindElements(TreeNode* root) 用受污染的二叉树初始化对象，你需要先把它还原。
> 
> bool find(int target) 判断目标值 target 是否存在于还原后的二叉树中并返回结果。
> 
> 
```
```

------

??? note 

    
-------------

=== "Python3"

    ```Python3
    # Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, val=0, left=None, right=None):
    #         self.val = val
    #         self.left = left
    #         self.right = right
    class FindElements:

        def __init__(self, root: Optional[TreeNode]):
            s = set()
            def dfs(root):
                if not root:
                    return
                s.add(root.val)
                if root.left:
                    root.left.val = root.val * 2 + 1
                    dfs(root.left)
                if root.right:
                    root.right.val = root.val * 2 + 2
                    dfs(root.right)
            root.val = 0
            dfs(root)
            self.s = s

        def find(self, target: int) -> bool:
            return target in self.s

    # Your FindElements object will be instantiated and called as such:
    # obj = FindElements(root)
    # param_1 = obj.find(target)
    ```
