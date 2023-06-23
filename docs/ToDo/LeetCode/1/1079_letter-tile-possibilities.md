# 1079_活字印刷

!!! note
    回溯 ｜ 剪枝 ｜ 去重

- 🔑🔑 难度： <span style = "color:gold; font-weight:bold">Medium</span>


> 你有一套活字字模 tiles，其中每个字模上都刻有一个字母 tiles[i]。返回你可以印出的非空字母序列的数目。
> 
> 注意：本题中，每个活字字模只能使用一次。


```
输入："AAB"
输出：8
解释：可能的序列为 "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA"。
```

??? note

  - 经典回溯模版：只能使用一次的字符
  
  - 如何设置结束条件/ 返回最终结果

  - 从什么地方开始遍历

  - 优化思路：从哈希表到自动排序

  - 先排序，一旦排好序之后，只要相同字符在这一次遍历当中选取了，别的就都不用遍历了

  - 这里还有一个附加的好处是可以排除空字符串的影响




=== "Java"

    ```Java
    // 第一次的超时版本
    class Solution {

        Set<String> set = new HashSet<>();
        char[] all;
        List<String> ans = new ArrayList<>();
        public int numTilePossibilities(String tiles) {
            all = tiles.toCharArray();
            boolean[] used = new boolean[tiles.length()];
            Arrays.fill(used, false);
            dfs(new StringBuilder(), used , 0);
            
            return ans.size();
        }

        public void dfs(StringBuilder tiles, boolean[] used, int idx){
            if(idx == all.length){
                String temp = tiles.toString();
                if(!set.contains(temp) && temp.length() > 0)
                    ans.add(temp);
                    set.add(temp);
                return;
            }
            else{
                // System.out.println(all.length);
                for(int i = 0; i < all.length; i ++ ){
                    if(!used[i]){
                        used[i] = true;
                        tiles.append(all[i]);
                        dfs(tiles, used, idx + 1);
                        tiles.deleteCharAt(tiles.length()-1);
                        used[i] = false;
                        
                    }
                    dfs(tiles, used, idx + 1);
                }
            }
        }
    }
    ```





    ```Java
    // Leetcode 1079 优化后
    class Solution {

        int count = 0;
        
        public int numTilePossibilities(String tiles) {
            char[] all = tiles.toCharArray();
            Arrays.sort(all);
            boolean[] used = new boolean[tiles.length()];
            Arrays.fill(used, false);
            dfs(used , 0, all);
            return count;
        }

        public void dfs(boolean[] used, int idx, char[] all){

            
            char last = '*';
            for(int i = 0; i < all.length; i ++ ){
                if(!used[i] && all[i] != last){
                    count ++ ;
                    used[i] = true;
                    dfs(used, idx + 1 , all);
                    used[i] = false;
                    last = all[i];
                }
            }
            
        }
    }
    ```





    ```Java

    class Solution {

        int count = 0;
        
        public int numTilePossibilities(String tiles) {
            char[] all = tiles.toCharArray();
            Arrays.sort(all);
            boolean[] used = new boolean[tiles.length()];
            Arrays.fill(used, false);
            dfs(used , 0, all);
            return count;
        }

        public void dfs(boolean[] used, int idx, char[] all){

            
            char last = '*';
            for(int i = 0; i < all.length; i ++ ){
                if(!used[i] && all[i] != last){
                    count ++ ;
                    used[i] = true;
                    dfs(used, idx + 1 , all);
                    used[i] = false;
                    last = all[i];
                }
            }
            
        }
    }
    ```

