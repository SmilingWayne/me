#### [1239. 串联字符串的最大长度](https://leetcode-cn.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/)

🔑🔑 考点：回溯 | 字符串

🚴‍♀️🚴‍♀️ 难度： <span style = "color:gold; font-weight:bold">Medium</span>

🔗🔗 链接：https://leetcode-cn.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/

📖📖 题目：

给定一个字符串数组 arr，字符串 s 是将 arr 的含有 不同字母 的 子序列 字符串 连接 所得的字符串。

请返回所有可行解 s 中最长长度。

子序列 是一种可以从另一个数组派生而来的数组，通过删除某些元素或不删除元素而不改变其余元素的顺序。

💻💻 测试用例：

```
输入：arr = ["un","iq","ue"]
输出：4
解释：所有可能的串联组合是：
- ""
- "un"
- "iq"
- "ue"
- "uniq" ("un" + "iq")
- "ique" ("iq" + "ue")
最大长度为 4。
```

💡💡思路：

- 经典的回溯问题，这里终止的条件是看组成的是否符合唯一性。



👩🏻‍💻🧑🏻‍💻 代码：

```Java
class Solution {
    int ans = 0;
    public void dfs(List<String> arr, StringBuilder sb, int idx){
        if(!judge(sb)){
            return;
        }
        ans = Math.max(ans, sb.length());
        for(int i = idx ;i < arr.size(); i ++ ){
            sb.append(arr.get(i));
            dfs(arr, sb, i + 1);
            sb.delete(sb.length() - arr.get(i).length(), sb.length());
        }
    }
    public int maxLength(List<String> arr) {
        dfs(arr, new StringBuilder(), 0);
        return ans;

    }
    public boolean judge(StringBuilder sb){
        if(sb.length() > 26){
            return false;
        }
        int[] t = new int[26];
        Arrays.fill(t, 0);
        for(int i = 0; i < sb.length(); i ++ ){
            if(t[(int)(sb.charAt(i) - 'a' )] == 1){
                return false;
            }
            t[(int)(sb.charAt(i) - 'a' )] = 1;
        }
        return true;
    }
}
```





