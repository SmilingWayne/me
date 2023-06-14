#### [334. 递增的三元子序列](https://leetcode-cn.com/problems/increasing-triplet-subsequence/)



难度：【Medium】

---

给你一个整数数组 nums ，判断这个数组中是否存在长度为 3 的递增子序列。

如果存在这样的三元组下标 (i, j, k) 且满足 i < j < k ，使得 nums[i] < nums[j] < nums[k] ，返回 true ；否则，返回 false 。

```
输入：nums = [1,2,3,4,5]
输出：true
解释：任何 i < j < k 的三元组都满足题意
```



- 要点：只需要两个数字：一个保留前面较小的，一个保留较大的。
- 只要出现了一个数字足够小，就更新，只要出现了一个数字比那个数字稍微大一点点，也更新



```Java
class Solution {
    
    public boolean increasingTriplet(int[] nums) {
        int a = 2147483647, b = a;
        for (int n: nums){ 
            if (n <= a){ 
                a = n;
            }
            else if (n <= b) {
                b = n;
            }
            else {
                return true;
            }
        }
        return false;
    }    
}
```

---

