# Offer-36_二叉搜索树转换为循环双向链表

<!-- 所有文件名必须是该题目的英文名 -->

!!! note
    <!-- 这里记载考察的数据结构、算法等 -->
    哈希表 | 动态规划

- 🔑🔑 难度：<span style = "color:gold; font-weight:bold">
<!-- <span style = "color:gold; font-weight:bold">Medium</span> 中等 -->
<!-- <span style = "color:crisma; font-weight:bold">High</span> 困难 -->
<!-- <span style = "color:Green; font-weight:bold">Easy</span> 简单 -->

<!-- 题目简介 -->
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的循环双向链表。要求不能创建任何新的节点，只能调整树中节点指针的指向。

为了让您更好地理解问题，以下面的二叉搜索树为例：


![二叉树](https://assets.leetcode.com/uploads/2018/10/12/bstdlloriginalbst.png)

![循环双向链表](https://assets.leetcode.com/uploads/2018/10/12/bstdllreturndll.png)

------

> 思路：利用BST的性质进行求解比较迅速，直接利用前序得出排序后的结果，然后直接在vector中对结果进行修正即可。要注意特殊情况下的判断：[]


-------------


=== "C++"

    ```C++
    /*
    // Definition for a Node.
    class Node {
    public:
        int val;
        Node* left;
        Node* right;

        Node() {}

        Node(int _val) {
            val = _val;
            left = NULL;
            right = NULL;
        }

        Node(int _val, Node* _left, Node* _right) {
            val = _val;
            left = _left;
            right = _right;
        }
    };
    */
    class Solution {
    public:

        vector<Node*> ans;
        Node* treeToDoublyList(Node* root) {
            if(root == nullptr){
                return root;
            }
            dfs(root);
            int N = ans.size();
            for(int i = 0; i < N; i ++ ){
                ans[i]->left = ans[( N + i - 1) % N ];
                ans[i]->right = ans[ (i + 1) % N];
            }
            return ans[0];
            
        }

        void dfs(Node *a){
            if(a == nullptr){
                return;
            }
            dfs(a->left);
            ans.emplace_back(a);
            dfs(a->right);
        }

    
    };
    ```

