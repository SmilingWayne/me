# 503_下一个更大元素II

<!-- 所有文件名必须是该题目的英文名 -->

!!! note
    <!-- 这里记载考察的数据结构、算法等 -->
    栈 ｜ 

- 🔑🔑 难度：
<!-- <span style = "color:gold; font-weight:bold">Medium</span> 中等 -->
<!-- <span style = "color:crisma; font-weight:bold">High</span> 困难 -->
<!-- <span style = "color:Green; font-weight:bold">Easy</span> 简单 -->

<!-- 题目简介 -->

> 给定一个循环数组 nums （ nums[nums.length - 1] 的下一个元素是 nums[0] ），返回 nums 中每个元素的 下一个更大元素 。
> 
> 数字 x 的 下一个更大的元素 是按数组遍历顺序，这个数字之后的第一个比它更大的数，这意味着你应该循环地搜索它的下一个更大的数。如果不存在，则输出 -1 。

```
输入: nums = [1,2,1]
输出: [2,-1,2]
解释: 第一个 1 的下一个更大的数是 2；
数字 2 找不到下一个更大的数； 
第二个 1 的下一个最大的数需要循环搜索，结果也是 2。

```

------

??? note 
    ？


    
-------------

=== "Java"

    ```java
    public class Solution {
        public int[] nextGreaterElements(int[] nums) {
            int[] ans = new int[nums.length];
            int n = nums.length;
            Arrays.fill(ans, -1);
            Stack<Integer> stack = new Stack<>();
            for(int i = 0 ; i < n * 2; i ++ ){
                int num = nums[i % n];
                while(!stack.isEmpty() && num > nums[stack.peek()]){
                    ans[stack.pop()] = num;
                }
                if(i < n){
                    stack.add(i);
                }
            }
            return ans;
        }
    }
    
    ```