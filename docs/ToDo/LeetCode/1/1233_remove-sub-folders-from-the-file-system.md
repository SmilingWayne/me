#### [1233. 删除子文件夹](https://leetcode-cn.com/problems/remove-sub-folders-from-the-filesystem/)

---

难度：【Medium】

你是一位系统管理员，手里有一份文件夹列表 folder，你的任务是要删除该列表中的所有 子文件夹，并以 任意顺序 返回剩下的文件夹。

如果文件夹 folder[i] 位于另一个文件夹 folder[j] 下，那么 folder[i] 就是 folder[j] 的 子文件夹 。

文件夹的「路径」是由一个或多个按以下格式串联形成的字符串：'/' 后跟一个或者多个小写英文字母。

例如，"/leetcode" 和 "/leetcode/problems" 都是有效的路径，而空字符串和 "/" 不是。



```
输入：folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
输出：["/a","/c/d","/c/f"]
解释："/a/b/" 是 "/a" 的子文件夹，而 "/c/d/e" 是 "/c/d" 的子文件夹。

输入: folder = ["/a/b/c","/a/b/ca","/a/b/d"]
输出: ["/a/b/c","/a/b/ca","/a/b/d"]
```



- 思路：暴力存到set里面 注意一种特殊情况，/a/b/c 和/a/b/ca 要判断是否在后续段中存在“/”

```Java
class Solution {
    public List<String> removeSubfolders(String[] folder) {
        Arrays.sort(folder);
        Set<String> set = new HashSet<>();
        for(int i = 0; i < folder.length; i ++ ){
            if(set.isEmpty()){
                set.add(folder[i]);
                continue;
            }
            for(String k : set){
                if(folder[i].indexOf(k) == 0){
                    if(folder[i].substring(k.length(), folder[i].length()).indexOf("/") != -1){ 
                        folder[i] = "#";
                        break;

                    }
                }
            }
            if(!folder[i].equals("#")){
                set.add(folder[i]);
            }
            
        }
        List<String> ans = new ArrayList<>();
        for(String s : set){
            ans.add(s);

        }
        return ans;

    }
}

// 上述速度比较慢

// 如果不排序 直接根据目录前缀遍历比较 速度稍微快一点
class Solution {
    public List<String> removeSubfolders(String[] folder) {
        HashSet<String> set = new HashSet<>();
        for (String s : folder)
            set.add(s);
        ArrayList<String> res = new ArrayList<>();
        for (String s : set) {
            int len = s.length();
            boolean tag = true;
            for (int i = len-1; i >= 0; --i) {
                if (s.charAt(i) == '/' && set.contains(s.substring(0,i))){
                    tag = false;
                    break;
                }
            }
            if (tag)
                res.add(s);
        }
        return res;
    }
}

```







