# 337_打家劫舍-III

<!-- 所有文件名必须是该题目的英文名 -->

!!! note
    <!-- 这里记载考察的数据结构、算法等 -->
    动态规划｜二叉树

- 🔑🔑 难度：<span style = "color:gold; font-weight:bold">Medium</span>
<!-- <span style = "color:gold; font-weight:bold">Medium</span> 中等 -->
<!-- <span style = "color:crisma; font-weight:bold">High</span> 困难 -->
<!-- <span style = "color:Green; font-weight:bold">Easy</span> 简单 -->

<!-- 题目简介 -->

> 小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为 root 。
> 
> 除了 root 之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果 两个直接相连的房子在同一天晚上被打劫 ，房屋将自动报警。
> 
> 给定二叉树的 root 。返回 在不触动警报的情况下 ，小偷能够盗取的最高金额 。


```
输入: root = [3,2,3,null,3,null,1]
输出: 7 
解释: 小偷一晚能够盗取的最高金额 3 + 3 + 1 = 7
```

------

??? note 
    这里把二叉树和DP结合在一起看，这里，一个节点能获得的最多价值 = 这一家偷，同时下面两家都不偷（的情况下的最大收益） or 这一家不偷，下面两家都偷（的情况下的最大收益之和），所以每一个的返回值有两个，一个是不偷的最大值，一个是偷的最大值；

    
-------------

=== "python"

    ```python
    # Definition for a binary tree node.
        # class TreeNode:
        #     def __init__(self, val=0, left=None, right=None):
        #         self.val = val
        #         self.left = left
        #         self.right = right
        class Solution:
            def rob(self, root: Optional[TreeNode]) -> int:

                
                def dfs(root):
                    if not root:
                        return 0, 0
                    left = dfs(root.left)
                    right = dfs(root.right)
                    steal = root.val + left[1] + right[1]
                    no_steal = max(left) + max(right)
                    return steal, no_steal
                
                return max(dfs(root))


    
    ```