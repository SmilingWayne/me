2022.3.13 Leetcode练习

----

894. 所有可能的满二叉树

[ Tag: 二叉树 递归 全排列]

满二叉树是一类二叉树，其中每个结点恰好有 0 或 2 个子结点。

返回包含 N 个结点的所有可能满二叉树的列表。 答案的每个元素都是一个可能树的根结点。

答案中每个树的每个结点都必须有 node.val=0。

你可以按任何顺序返回树的最终列表。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/all-possible-full-binary-trees

输入：7
输出：[[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]

![示意图](https://aliyun-lc-upload.oss-cn-hangzhou.aliyuncs.com/aliyun-lc-upload/uploads/2018/08/24/fivetrees.png)

思路：

- 经典的递归选出全排列
- 要点：偶数个是一定不会出现满二叉树的情况的
- 要分别罗列出剩下的情况中所有可能组合然后循环配对即可
- 要点：n < 20 说明数据量不会很大

```C++ 
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
   
    vector<TreeNode*> allPossibleFBT(int n) {
        vector<TreeNode*> ans;
        if(n % 2 == 0){
            return ans;
        }
        if(n == 1){
            TreeNode *root = new TreeNode(0);
            ans.push_back(root);
            return ans;
        }
        
        for(int i = 1; i < n ; i += 2 ){
            vector<TreeNode*> left_Node = allPossibleFBT(i);
            vector<TreeNode*> right_Node = allPossibleFBT(n - i - 1);
            for(auto l : left_Node){
                for(auto r: right_Node ){
                    TreeNode *root = new TreeNode(0);
                    root->left = l;
                    root->right = r;
                    ans.push_back(root);
                }
            }
        }
        return ans;

    }
};
```

