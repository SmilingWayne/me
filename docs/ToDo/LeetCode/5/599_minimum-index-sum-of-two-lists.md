2022.3.14 LeetCode 每日一题

---

599. 两个列表的最小索引和

难度：【Easy】

假设 Andy 和 Doris 想在晚餐时选择一家餐厅，并且他们都有一个表示最喜爱餐厅的列表，每个餐厅的名字用字符串表示。

你需要帮助他们用最少的索引和找出他们共同喜爱的餐厅。 如果答案不止一个，则输出所有答案并且不考虑顺序。 你可以假设答案总是存在。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-index-sum-of-two-lists

输入: list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]，list2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
输出: ["Shogun"]
解释: 他们唯一共同喜爱的餐厅是“Shogun”。

- 思路：直接hashMap解决，记得要把每个可能的都遍历到，防止出现：【一个在list1的前面，一个在list2的很后面，和两个都在中间这种情况

```C++
class Solution {
public:
    vector<string> findRestaurant(vector<string>& list1, vector<string>& list2) {
        // map<string> hashMap;
        unordered_map<string, int> hashMap;
        vector<string> res;
        int min_index = list1.size() + list2.size() - 2;
        for(int i = 0; i < list1.size(); i ++ ){
            hashMap.insert(make_pair(list1[i], i));
        }
        for(int i = 0; i < list2.size(); i ++ ){
            if(hashMap.count(list2[i])){
                if(hashMap[list2[i]] + i == min_index){
                    res.push_back(list2[i]);
                }
                else if(hashMap[list2[i]] + i < min_index){
                    res.clear();
                    res.push_back(list2[i]);
                    min_index = hashMap[list2[i]] + i;
                }
            }
        }
        return res;
    }
};
```

