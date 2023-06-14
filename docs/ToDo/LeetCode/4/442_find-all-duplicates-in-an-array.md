#### [442. 数组中重复的数据](https://leetcode-cn.com/problems/find-all-duplicates-in-an-array/)

🔑🔑 考点：数组 

🚴‍♀️🚴‍♀️ 难度： <span style = "color:gold; font-weight:bold">Medium</span>

🔗🔗 链接：https://leetcode-cn.com/problems/find-all-duplicates-in-an-array/

📖📖 题目：

给你一个长度为 n 的整数数组 nums ，其中 nums 的所有整数都在范围 [1, n] 内，且每个整数出现 一次 或 两次 。请你找出所有出现 两次 的整数，并以数组形式返回。

你必须设计并实现一个时间复杂度为 O(n) 且仅使用常量额外空间的算法解决此问题。

💻💻 测试用例：

```
输入：nums = [4,3,2,7,8,2,3,1]
输出：[2,3]
输入：nums = [1,1,2]
输出：[1]
```

💡💡思路：

- 一道比较技巧的题。思路在：所有整数在[1, n]中，可以原地修改数组来满足空间复杂度的要求，遍历到这个数组某个元素的时候，就把数组对应元素下标加上一个M，为保证下标不越界，在遍历的时候模上一个M就可以。最后只要看哪些数大于2M即可。

👩🏻‍💻🧑🏻‍💻 代码：

```Java
class Solution {
    public List<Integer> findDuplicates(int[] nums) {
        List<Integer> ans = new ArrayList<>();
        int N = nums.length;
        int M = 100001;
        for(int i= 0; i < N; i ++ ){
            nums[nums[i] % M - 1] += M;
        }
        for(int i = 0; i < N; i ++ ){
            if(nums[i] > 2 * M){
                ans.add(i + 1);
            }
        }
        return ans;
    }
}
```



