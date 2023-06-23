# 1452_收藏清单


!!! note
    <!-- 这里记载考察的数据结构、算法等 -->
    哈希表

- 🔑🔑 难度：<span style = "color:gold; font-weight:bold">Medium</span>



> 给你一个数组 favoriteCompanies ，其中 favoriteCompanies[i] 是第 i 名用户收藏的公司清单（下标从 0 开始）。
> 
> 请找出不是其他任何人收藏的公司清单的子集的收藏清单，并返回该清单下标。下标需要按升序排列。


```
输入：favoriteCompanies = [["leetcode","google","facebook"],["google","microsoft"],["google","facebook"],["google"],["amazon"]]
输出：[0,1,4] 
解释：
favoriteCompanies[2]=["google","facebook"] 是 favoriteCompanies[0]=["leetcode","google","facebook"] 的子集。
favoriteCompanies[3]=["google"] 是 favoriteCompanies[0]=["leetcode","google","facebook"] 和 favoriteCompanies[1]=["google","microsoft"] 的子集。
其余的收藏清单均不是其他任何人收藏的公司清单的子集，因此，答案为 [0,1,4] 。

```

---------

> 原理很好理解，但是正常思路会写出一个O(N^3)的解法
> 
> 思路1: 利用Java自带特性减少一个N的循环
> 


---------

=== "Java"

  ```Java
  class Solution {
      public List<Integer> peopleIndexes(List<List<String>> favoriteCompanies) {
          ArrayList<Integer> ans = new ArrayList<>();
          int len = favoriteCompanies.size();
          for(int i = 0; i < len; i ++ ){
              boolean flag = false;
              for(int j = 0; j < len; j ++ ){
                  if(i == j || favoriteCompanies.get(i).size() > favoriteCompanies.get(j).size()){
                      continue;
                  }
                  flag = new HashSet<>(favoriteCompanies.get(j)).containsAll(favoriteCompanies.get(i));
                  if(flag){
                      break;
                  }
                  
              }
              if(!flag){
                  ans.add(i);
              }
          }
          return ans;

      }
  }
  ```

=== "C++"

    ```C++
    class Solution {
      public:
        vector<int> peopleIndexes(vector<vector<string>>& favoriteCompanies) {
          unordered_map<string, bitset<512>> nmap;
          vector<int> ret;
          for(int i = 0; i < favoriteCompanies.size(); ++i)
            for(auto &word: favoriteCompanies[i])
              nmap[word].set(i);
          for(int i = 0; i < favoriteCompanies.size(); ++i) {
            auto bits = nmap[favoriteCompanies[i][0]];
            for(int j = 1; j < favoriteCompanies[i].size(); ++j)
              bits &= nmap[favoriteCompanies[i][j]];
            if(bits.count() <= 1)
              ret.push_back(i);
          }
          return ret;
        }
    };
    ```

