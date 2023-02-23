2022.3.13 LeetCode 刷题

----

剑指offer36. 二叉搜索树转换为循环双向链表

难度：【Medium】

输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的循环双向链表。要求不能创建任何新的节点，只能调整树中节点指针的指向。

为了让您更好地理解问题，以下面的二叉搜索树为例：

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-cha-sou-suo-shu-yu-shuang-xiang-lian-biao-lcof

![二叉树](https://assets.leetcode.com/uploads/2018/10/12/bstdlloriginalbst.png)

![循环双向链表](https://assets.leetcode.com/uploads/2018/10/12/bstdllreturndll.png)

思路：利用BST的性质进行求解比较迅速，直接利用前序得出排序后的结果，然后直接在vector中对结果进行修正即可。要注意特殊情况下的判断：[]

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

