# 2022.3.11Leetcode 刷题

---

2049.统计最高分的节点数目

给你一棵根节点为 0 的 二叉树 ，它总共有 n 个节点，节点编号为 0 到 n - 1 。同时给你一个下标从 0 开始的整数数组 parents 表示这棵树，其中 parents[i] 是节点 i 的父节点。由于节点 0 是根，所以 parents[0] == -1 。

一个子树的 大小 为这个子树内节点的数目。每个节点都有一个与之关联的 分数 。求出某个节点分数的方法是，将这个节点和与它相连的边全部 删除 ，剩余部分是若干个 非空 子树，这个节点的 分数 为所有这些子树 大小的乘积 。

请你返回有 最高得分 节点的 数目 。



![示意图](https://assets.leetcode.com/uploads/2021/10/03/example-1.png)

输入：parents = [-1,2,0,2,0]
输出：3
解释：

- 节点 0 的分数为：3 * 1 = 3
- 节点 1 的分数为：4 = 4
- 节点 2 的分数为：1 * 1 * 2 = 2
- 节点 3 的分数为：4 = 4
- 节点 4 的分数为：4 = 4
最高得分为 4 ，有三个节点得分为 4 （分别是节点 1，3 和 4 ）。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-nodes-with-the-highest-score

- 一道经典的模拟题，只能通过对每个可能删除的情况作出计算然后求出最大值
- 对于DFS会自动求到最底层，把所有的子树删除情况都计算出来，注意特殊情况是：根节点没有父节点，别的节点都会有父节点上得到的那个非空子树
- 将计算最大的乘积的过程放在dfs中进行完成
- 注意long的使用 可能会导致count数量超过int范围。【坑】

```C++
class Solution {
public:
    int max_size = 0;
    long max_count = 1;
    int N = 0;
    vector<vector<int> > children;

    int dfs(int n){
        int size = N - 1;
        long temp_count = 1;
        for(auto i : children[n]){
            int temp = dfs(i);
            size -= temp;
            temp_count *= temp;
        }
        if(n != 0){
            temp_count *= size;
        }
        if(temp_count > max_count){
            max_count = temp_count;
            max_size = 1;
        }
        else if(temp_count ==  max_count){
            max_size ++ ;
        }
        return N - size;

    }
    int countHighestScoreNodes(vector<int>& parents) {
        this->N = parents.size();
        this->children = vector<vector<int> >(N);
        for(int i = 0; i < N; i ++ ){
            int p = parents[i];
            if(p != -1){
                children[p].emplace_back(i);
            }
        }
        dfs(0);
        return max_size;
        
    }
};
```

