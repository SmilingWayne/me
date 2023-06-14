#### [1305. 两棵二叉搜索树中的所有元素](https://leetcode-cn.com/problems/all-elements-in-two-binary-search-trees/)

🔑🔑 考点：二叉搜素树

🚴‍♀️🚴‍♀️ 难度： <span style = "color:gold; font-weight:bold">Medium</span>

🔗🔗 链接：https://leetcode-cn.com/problems/all-elements-in-two-binary-search-trees/

📖📖 题目：

给你 `root1` 和 `root2` 这两棵二叉搜索树。请你返回一个列表，其中包含 **两棵树** 中的所有整数并按 **升序** 排序。.

💻💻 测试用例：

```
输入：root1 = [2,1,4], root2 = [1,0,3]
输出：[0,1,1,2,3,4]
输入：root1 = [1,null,8], root2 = [8,1]
输出：[1,1,8,8]
```

💡💡思路：

- 最直接的思路：二叉搜索中序是有序的。所以暴力列举然后归并一下就可以了。

👩🏻‍💻🧑🏻‍💻 代码：

```Java

class Solution {
    List<Integer> ans = new ArrayList<>();
    public List<Integer> getAllElements(TreeNode root1, TreeNode root2) {
        List<Integer> arr1 = new ArrayList<>();
        List<Integer> arr2 = new ArrayList<>();
        dfs(arr1, root1);
        dfs(arr2, root2);
        int first = 0;
        int second = 0;
        while(first < arr1.size() && second < arr2.size()){
            if(arr1.get(first) <= arr2.get(second))
                ans.add(arr1.get(first ++ ));
            else
                ans.add(arr2.get(second ++ ));
        }
        while(first < arr1.size())
            ans.add(arr1.get(first ++ ));
        while(second < arr2.size())
            ans.add(arr2.get(second ++ ));
        return ans;
    }
    public void dfs(List<Integer> t, TreeNode root){
        if(root == null) return;
        if(root.left != null) dfs(t, root.left);
        t.add(root.val);
        dfs(t, root.right);
    }
}
```









