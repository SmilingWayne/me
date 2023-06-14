#### [905. 按奇偶排序数组](https://leetcode-cn.com/problems/sort-array-by-parity/)

🔑🔑 考点：数组 ｜ 字符串 ｜ 双指针

🚴‍♀️🚴‍♀️ 难度： <span style = "color:darkgreen; font-weight:bold">Easy</span>

🔗🔗 链接：https://leetcode-cn.com/problems/sort-array-by-parity/

📖📖 题目：

给你一个整数数组 `nums`，将 `nums` 中的的所有偶数元素移动到数组的前面，后跟所有奇数元素。

返回满足此条件的 **任一数组** 作为答案。

💻💻 测试用例：

```
输入：nums = [3,1,2,4]
输出：[2,4,3,1]
解释：[4,2,3,1]、[2,4,1,3] 和 [4,2,1,3] 也会被视作正确答案。
```

💡💡思路：

- 经典简单题。双指针，找到前面的偶数和尾部的奇数互换即可。





👩🏻‍💻🧑🏻‍💻 代码：

```Java
class Solution {
    public int[] sortArrayByParity(int[] nums) {
        int left = 0,right = nums.length-1;
        while(left<right){
            while( left < right && nums[left]%2 == 0)
                left++;
            while( left < right && nums[right]%2 == 1) 
                right--;
            if(left<right){
                int temp = nums[left];
                nums[left] = nums[right];
                nums[right] = temp;
                left++;
                right--;
            }
        }
        return nums;
    }
}
```









