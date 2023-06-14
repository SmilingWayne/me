2022.4.14 Leetcode 日常刷题



---

#### [1452. 收藏清单](https://leetcode-cn.com/problems/people-whose-list-of-favorite-companies-is-not-a-subset-of-another-list/)

难度：【Medium】

给你一个数组 favoriteCompanies ，其中 favoriteCompanies[i] 是第 i 名用户收藏的公司清单（下标从 0 开始）。

请找出不是其他任何人收藏的公司清单的子集的收藏清单，并返回该清单下标。下标需要按升序排列。

```
输入：favoriteCompanies = [["leetcode","google","facebook"],["google","microsoft"],["google","facebook"],["google"],["amazon"]]
输出：[0,1,4] 
解释：
favoriteCompanies[2]=["google","facebook"] 是 favoriteCompanies[0]=["leetcode","google","facebook"] 的子集。
favoriteCompanies[3]=["google"] 是 favoriteCompanies[0]=["leetcode","google","facebook"] 和 favoriteCompanies[1]=["google","microsoft"] 的子集。
其余的收藏清单均不是其他任何人收藏的公司清单的子集，因此，答案为 [0,1,4] 。

```



- 原理很好理解，但是正常思路会写出一个O(N^3)的解法
- 思路1: 利用Java自带特性减少一个N的循环



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

> 这里有两个知识点：HashSet和ArrayList之间的转换
>
> containsAll 方法：直接判断两个set是否可以互相转换



第二个方法：bitset（cpp）或者bitmap（Java），利用一个bit表示0或者1，常用来存储一些非常长的，不需要获取具体名称的东西，例如一个string在一长长的不规则数组中在哪些位置出现过

重要api：

> bitset<size_t>  a("1101")可以把字符串转换成bitset
>
> a.count() 统计1的个数
>
> a.set(i) 把第i个数字设置为1
>
> a.reset(i) 把第i个设置为0
>
> a.test(i) 检测第i个位置是不是1
>
> Bitset 同样支持位运算。复习：& 表示交,  ^ 表示异或，不同设置为1，相同设置为0； | 表示或
>
> 如果统计出现次数，可以通过& + count看是否 > 0；一个经典的操作

```c++
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

