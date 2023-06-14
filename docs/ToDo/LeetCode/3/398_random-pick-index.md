#### [398. 随机数索引](https://leetcode-cn.com/problems/random-pick-index/)

🔑🔑 考点：随机数生成 | 哈希表 | 数组 | 蓄水池抽样

🚴‍♀️🚴‍♀️ 难度： <span style = "color:gold; font-weight:bold">Medium</span>

🔗🔗 链接：https://leetcode-cn.com/problems/random-pick-index/

📖📖 题目：

给定一个可能含有重复元素的整数数组，要求随机输出给定的数字的索引。 您可以假设给定的数字一定存在于数组中。

注意：
数组大小可能非常大。 使用太多额外空间的解决方案将不会通过测试。

💻💻 测试用例：

```
int[] nums = new int[] {1,2,3,3,3};
Solution solution = new Solution(nums);
// pick(3) 应该返回索引 2,3 或者 4。每个索引的返回概率应该相等。
solution.pick(3);
// pick(1) 应该返回 0。因为只有nums[0]等于1。
solution.pick(1);
```

💡💡思路：

- 1⃣️HashMap存数字和对应下标，随机数生成int在List长度内，然后取出即可
- 2⃣️ 一次遍历：遇到这个字符k次，就有1/k的概率选中它。在Java中Random.nextInt(n)会生成[0, n) 的随机数，每次遇到，都假设随机到0表示选中这个数字，例如，如果这个数字只出现了一次，那么遍历结束一定只会选中这个数字，如果出现了两次，在第二次出现的时候有1/2的概率进行下标替换，第3次有1/3的概率选中....以此类推。

👩🏻‍💻🧑🏻‍💻 代码：

```Java
// HashMap
class Solution {
    Map<Integer, ArrayList<Integer> > map = new HashMap<>();
    public Solution(int[] nums) {
        for(int i = 0; i < nums.length; i ++ ){
            if(map.containsKey(nums[i])){
                map.get(nums[i]).add(i);
            }
            else{
                ArrayList<Integer> t = new ArrayList<>();
                t.add(i);
                map.put(nums[i], t);
            }
        }
    }
    
    public int pick(int target) {
        int size = map.get(target).size();
        int choose = new Random().nextInt(size);
        return map.get(target).get(choose);
    }
}

```









