# 590_N叉树的后续遍历
<!-- 所有文件名必须是该题目的英文名 -->

!!! note
    <!-- 这里记载考察的数据结构、算法等 -->
    哈希表 | 动态规划

- 🔑🔑 难度：
<!-- <span style = "color:gold; font-weight:bold">Medium</span> 中等 -->
<!-- <span style = "color:crisma; font-weight:bold">High</span> 困难 -->
<!-- <span style = "color:Green; font-weight:bold">Easy</span> 简单 -->

<!-- 题目简介 -->


给定一个 n 叉树的根节点 root ，返回 其节点值的 后序遍历 。

 n 叉树 在输入中按层序遍历进行序列化表示，每组子节点由空值 null 分隔（请参见示例）。


------

> 解析
> 
> 思路1：和二叉树一样，先遍历所有子序列然后根节点。**递归**
>
> 思路2:  迭代法： 利用Stack进行压入弹出操作，一定要等到一个父节点的所有的子节点全部被弹出之后才能把父节点的val加入结果中去。这里同样可以使用make_pair 操作辅助判断。

-------------

=== "Java"

    ```Java
    class Solution {
        List<Integer> ans = new ArrayList<>();
        public List<Integer> postorder(Node root) {
            postorder_2(root);
            return ans;
        }

        public void postorder_2(Node root){
            if(root == null){
                return;
            }
            for(Node i :root.children){
                postorder_2(i);
            }
            ans.add(root.val);
        }
    }
    ```

=== "C++"
    
    ```c++
        /*
        // Definition for a Node.
        class Node {
        public:
            int val;
            vector<Node*> children;

            Node() {}

            Node(int _val) {
                val = _val;
            }

            Node(int _val, vector<Node*> _children) {
                val = _val;
                children = _children;
            }
        };
        */
        class Solution {
        public:

            vector<int> ans;
            vector<int> postorder(Node* root) {
                if(root == nullptr){
                    return ans;
                }
                stack<pair<Node *, bool>> stk;
                stk.push(make_pair(root, false));
                while(!stk.empty()){
                    auto& t = stk.top();
                    if(!t.second){
                        int size = t.first->children.size();
                        for(int i = size - 1; i >= 0; --i){
                            stk.push(make_pair(t.first->children[i], false ) );
                        }
                        t.second = true;
                    }
                    else{
                        ans.push_back(t.first->val);
                        stk.pop();
                    }
                }
                return ans;
            }

            
        };
    ```

