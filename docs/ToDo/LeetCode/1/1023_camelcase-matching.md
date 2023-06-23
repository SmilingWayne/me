# 1023_驼峰式匹配


!!! note
    字符串 | 递增子序列

- 🔑🔑 难度： <span style = "color:gold; font-weight:bold">Medium</span>





> 如果我们可以将小写字母插入模式串 pattern 得到待查询项 query，那么待查询项与给定模式串匹配。（我们可以在任何位置插入每个字符，也可以插入 0 个字符。）
> 
> 给定待查询列表 queries，和模式串 pattern，返回由布尔值组成的答案列表 answer。只有在待查项 queries[i] 与模式串 pattern 匹配时， answer[i] 才为 true，否则为 false。



```

输入：queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FB"
输出：[true,false,true,true,false]
示例：
"FooBar" 可以这样生成："F" + "oo" + "B" + "ar"。
"FootBall" 可以这样生成："F" + "oot" + "B" + "all".
"FrameBuffer" 可以这样生成："F" + "rame" + "B" + "uffer".
```

---------

??? note

    要点：先后顺序+检查是否符合大写约束即可
    
    判断方式: 这样需要顺序和模式串一致的，可以长的走一遍，短的采取“匹配则移动，不匹配则不动”的方式，最终判断是否符合要求，只需看短的（模式串）最终下标是不是长度。





=== "Java"

    ```Java
    class Solution {
        List<Boolean> ans = new ArrayList<>();
        public List<Boolean> camelMatch(String[] queries, String pattern) {
            char[] p = pattern.toCharArray();
            for(int i = 0; i < queries.length; i ++ ){
                ans.add(check( queries[i].toCharArray(), p ));
            }
            return ans;
        }

        public boolean check(char[] queries, char[] pattern){
            int idx = 0;
            for(int i = 0; i < queries.length; i ++ ){
                
                if(idx < pattern.length && queries[i] == pattern[idx]){
                    idx ++ ;
                }
                else if(queries[i] >='A' && queries[i] <= 'Z') {
                    if(idx >= pattern.length || pattern[idx] != queries[i]){
                        return false;
                    }
                }
            }
            if(idx != pattern.length){
                return false;
            }
            return true;
        }
    }
    ```

