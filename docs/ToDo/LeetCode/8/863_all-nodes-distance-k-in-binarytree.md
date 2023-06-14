# 863_二叉树中所有距离为 K 的结点

<!-- 所有文件名必须是该题目的英文名 -->

!!! note
    <!-- 这里记载考察的数据结构、算法等 -->
    

- 🔑🔑 难度：<span style = "color:gold; font-weight:bold">Medium</span>
<!-- <span style = "color:gold; font-weight:bold">Medium</span> 中等 -->
<!-- <span style = "color:crisma; font-weight:bold">High</span> 困难 -->
<!-- <span style = "color:Green; font-weight:bold">Easy</span> 简单 -->

<!-- 题目简介 -->
给定一个二叉树（具有根结点 root）， 一个目标结点 target ，和一个整数值 k 。

返回到目标结点 target 距离为 k 的所有结点的值的列表。 答案可以以 任何顺序 返回。

> 输入：root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
> 输出：[7,4,1]
> 解释：所求结点为与目标结点（值为 5）距离为 2 的结点，值分别为 7，4，以及 1

------

> 解析

-------------

=== "这里写编程语言"

    ```java
    class Solution {
        List<Integer> res = new ArrayList<>();
        HashMap<TreeNode, TreeNode> map = new HashMap<>();
        HashSet<TreeNode> visited = new HashSet<>();
        public List<Integer> distanceK(TreeNode root, TreeNode target, int K) {
            int k = K;
            buildMap(root, target);
            dfs(target, K, 0);
            return res;

            
        }
        public void dfs(TreeNode root, int K ,int n){
            if(n > K || root == null || visited.contains(root)){
                return ;
            }
            visited.add(root);
            if(n == K){
                res.add(root.val);
            }
            dfs(root.left, K, n + 1);
            dfs(root.right, K , n + 1);
            dfs(map.get(root), K , n + 1);
        }
        
        public void buildMap(TreeNode root, TreeNode target){
            if(root == target){
                return ;
            }
            if(root.left != null){
                map.put(root.left, root);
                buildMap(root.left , target);
            }
            if(root.right != null){
                map.put(root.right, root);
                buildMap(root.right, target);
            }
        }

    }


    ```