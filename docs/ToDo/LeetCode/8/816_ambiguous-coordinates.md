#### [816. 模糊坐标](https://leetcode-cn.com/problems/ambiguous-coordinates/)

难度：【Medium】

我们有一些二维坐标，如 "(1, 3)" 或 "(2, 0.5)"，然后我们移除所有逗号，小数点和空格，得到一个字符串S。返回所有可能的原始字符串到一个列表中。

原始的坐标表示法不会存在多余的零，所以不会出现类似于"00", "0.0", "0.00", "1.0", "001", "00.01"或一些其他更小的数来表示坐标。此外，一个小数点前至少存在一个数，所以也不会出现“.1”形式的数字。

最后返回的列表可以是任意顺序的。而且注意返回的两个数字中间（逗号之后）都有一个空格



```
示例 1:
输入: "(123)"
输出: ["(1, 23)", "(12, 3)", "(1.2, 3)", "(1, 2.3)"]
```



```Java
class Solution {
    public List<String> ambiguousCoordinates(String s) {
        // for(int i = 0; i < s.length(); i ++ )
        s = s.substring(1, s.length() - 1);
        List<String> ans = new ArrayList<>();
        
        for(int i = 1; i < s.length(); i ++ ){
            String t = s.substring(0, i);
            String p = s.substring(i, s.length() );
            List<String> pre = getAll(t);
            List<String> post = getAll(p);
            if(pre.size() > 0 && post.size() > 0){
                // sb.append("(");
                for(int j = 0; j < pre.size(); j ++ ){
                    StringBuilder sb = new StringBuilder();
                    sb.append("(");
                    sb.append(pre.get(j));
                    sb.append(", ");
                    for(int k = 0; k < post.size(); k ++ ){
                        sb.append(post.get(k));
                        sb.append(")");
                        ans.add(sb.toString());
                        sb.delete(sb.length() - (post.get(k).length() +1), sb.length());
                    }
                }
            }
        }
        return ans;
    }

    public List<String> getAll(String t){
        List<String> res = new ArrayList<>();
        if(t.length() == 1){
            res.add(t);
            return res;
        }
        char[] s = t.toCharArray();
        if(s[0] == '0'){
            if(s[s.length - 1] == '0'){
                return res;
            }
            else{
                StringBuilder sb = new StringBuilder();
                sb.append(s[0]);
                sb.append('.');
                for(int i = 1; i < s.length; i ++ ){
                    sb.append(s[i]);
                }
                res.add(sb.toString());
                return res;
            }
        }
        if(s[s.length - 1] == '0'){
            res.add(t);
            return res;
        }
        StringBuilder sb = new StringBuilder();
        sb.append(t);
        res.add(sb.toString());
        for(int i = 1; i < sb.length(); i ++ ){
            sb.insert(i, '.');
            res.add(sb.toString());
            sb.delete(i, i + 1);
        }
        return res;
    }
}
```

